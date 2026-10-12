#!/usr/bin/env python3
"""Check catalog website, download, and source URLs; produce CSV and JSON reports.

HTTP 403/429 and similar access restrictions are marked MANUAL_REVIEW rather than
DEAD_LINK. This checker does not execute downloads or install software.
"""
from __future__ import annotations
import csv
import json
from concurrent.futures import ThreadPoolExecutor, as_completed
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_FILES = [
    "data/software.json",
    "data/software-expansion-100.json",
    "data/software-phase2-a.json",
    "data/software-phase2-b.json",
    "data/operating-systems-v1.json",
    "data/operating-systems-expansion-25.json",
    "data/operating-systems-phase2-25.json",
    "data/operating-systems-phase2-b.json",
]
URL_FIELDS = ("official_website", "download_url", "source_code_url")
TIMEOUT = 8
MAX_WORKERS = 16


def check_url(url: str) -> dict:
    headers = {"User-Agent": "FOSS-Atlas-Link-Checker/1.0 (+https://kamino-88.github.io/foss-atlas/)"}
    req = urllib.request.Request(url, method="HEAD", headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as response:
            code = response.getcode()
            return {"http_status": code, "final_url": response.geturl(),
                    "result": "OK" if 200 <= code < 400 else "HTTP_ERROR", "detail": ""}
    except urllib.error.HTTPError as exc:
        if exc.code in (403, 405, 429, 501):
            # Some hosts reject HEAD or block automated clients; retry a small GET.
            get_req = urllib.request.Request(url, method="GET", headers={**headers, "Range": "bytes=0-0"})
            try:
                with urllib.request.urlopen(get_req, timeout=TIMEOUT) as response:
                    code = response.getcode()
                    return {"http_status": code, "final_url": response.geturl(),
                            "result": "OK" if 200 <= code < 400 else "HTTP_ERROR",
                            "detail": "GET fallback after HEAD restriction"}
            except urllib.error.HTTPError as get_exc:
                if get_exc.code in (401, 403, 405, 429):
                    return {"http_status": get_exc.code, "final_url": get_exc.geturl(),
                            "result": "MANUAL_REVIEW", "detail": "Host blocks automated checks or rate-limits requests"}
                return {"http_status": get_exc.code, "final_url": get_exc.geturl(),
                        "result": "HTTP_ERROR", "detail": str(get_exc)}
            except Exception as get_exc:
                return {"http_status": None, "final_url": "", "result": "MANUAL_REVIEW",
                        "detail": f"GET fallback failed: {type(get_exc).__name__}: {get_exc}"}
        return {"http_status": exc.code, "final_url": exc.geturl(),
                "result": "DEAD_LINK" if exc.code in (404, 410) else "HTTP_ERROR", "detail": str(exc)}
    except Exception as exc:
        return {"http_status": None, "final_url": "", "result": "MANUAL_REVIEW",
                "detail": f"{type(exc).__name__}: {exc}"}


def main() -> None:
    checked_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    rows = []
    pending = []
    for file_name in DATA_FILES:
        file_path = ROOT / file_name
        if not file_path.exists():
            continue
        try:
            records = json.loads(file_path.read_text(encoding="utf-8"))
        except Exception as exc:
            rows.append({"checked_at_utc": checked_at, "data_file": file_name, "record_id": "",
                         "project_name": "", "url_field": "", "url": "", "http_status": "",
                         "final_url": "", "result": "DATA_ERROR", "detail": str(exc)})
            continue
        for record in records:
            for field in URL_FIELDS:
                url = str(record.get(field) or "").strip()
                if not url:
                    rows.append({"checked_at_utc": checked_at, "data_file": file_name,
                                 "record_id": record.get("id", ""), "project_name": record.get("name", ""),
                                 "url_field": field, "url": "", "http_status": "", "final_url": "",
                                 "result": "MISSING_URL", "detail": "URL field is empty"})
                    continue
                pending.append({"checked_at_utc": checked_at, "data_file": file_name,
                                "record_id": record.get("id", ""), "project_name": record.get("name", ""),
                                "url_field": field, "url": url})

    # Check each unique URL once, concurrently, then attach its result to every record using it.
    unique_urls = sorted({item["url"] for item in pending})
    checked = {}
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as pool:
        futures = {pool.submit(check_url, url): url for url in unique_urls}
        for future in as_completed(futures):
            url = futures[future]
            try:
                checked[url] = future.result()
            except Exception as exc:
                checked[url] = {"http_status": None, "final_url": "", "result": "MANUAL_REVIEW",
                                "detail": f"Checker error: {type(exc).__name__}: {exc}"}
    for item in pending:
        rows.append({**item, **checked[item["url"]]})

    out_dir = ROOT / "link-check-reports"
    out_dir.mkdir(exist_ok=True)
    csv_path = out_dir / "catalog-link-check.csv"
    json_path = out_dir / "catalog-link-check.json"
    fields = ["checked_at_utc", "data_file", "record_id", "project_name", "url_field",
              "url", "http_status", "final_url", "result", "detail"]
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)
    counts = {}
    for row in rows:
        counts[row["result"]] = counts.get(row["result"], 0) + 1
    report = {"checked_at_utc": checked_at, "total_checks": len(rows),
              "results": counts, "items": rows}
    json_path.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"checked_at_utc": checked_at, "total_checks": len(rows),
                      "results": counts, "csv": str(csv_path), "json": str(json_path)}, indent=2))


if __name__ == "__main__":
    main()
