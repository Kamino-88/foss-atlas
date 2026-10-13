#!/usr/bin/env python3
"""Conservatively check FOSS Atlas catalog URLs and write CSV/JSON reports.

This is a reachability diagnostic, not a software-safety or release verification
tool. Automated 404/410 responses are labelled SUSPECTED_DEAD_LINK so that
transient responses, access policies, and host-specific behavior do not get
mistaken for definitive evidence that a project or URL is gone.
"""
from __future__ import annotations

import csv
import json
import random
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

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
TIMEOUT = 15
MAX_WORKERS = 8
RETRIES = 2
RETRYABLE_STATUS = {408, 425, 429, 500, 502, 503, 504}
HEAD_GET_FALLBACK = {400, 403, 404, 405, 406, 409, 410, 429, 501}
MANUAL_REVIEW_STATUS = {401, 403, 407, 429}
USER_AGENT = (
    "Mozilla/5.0 (compatible; FOSS-Atlas-Link-Checker/2.0; "
    "+https://kamino-88.github.io/foss-atlas/)"
)


class TrackingRedirectHandler(urllib.request.HTTPRedirectHandler):
    """Follow redirects and preserve their chain for the report."""
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        chain = list(getattr(req, "_foss_redirect_chain", []))
        chain.append({"status": code, "url": newurl})
        redirected = super().redirect_request(req, fp, code, msg, headers, newurl)
        if redirected is not None:
            redirected._foss_redirect_chain = chain
        return redirected


OPENER = urllib.request.build_opener(TrackingRedirectHandler())


def _request(url: str, method: str):
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Encoding": "identity",
    }
    if method == "GET":
        # Request only a tiny byte range where supported. Some servers ignore
        # Range, but the response body is never read or saved.
        headers["Range"] = "bytes=0-0"
    req = urllib.request.Request(url, method=method, headers=headers)
    with OPENER.open(req, timeout=TIMEOUT) as response:
        chain = list(getattr(response, "_foss_redirect_chain", []))
        return {
            "http_status": response.getcode(),
            "final_url": response.geturl(),
            "redirect_chain": chain,
            "detail": "",
        }


def _request_with_retries(url: str, method: str):
    last = None
    for attempt in range(RETRIES + 1):
        try:
            result = _request(url, method)
            if result["http_status"] not in RETRYABLE_STATUS or attempt == RETRIES:
                return result
            last = result
        except urllib.error.HTTPError as exc:
            chain = list(getattr(exc, "_foss_redirect_chain", []))
            last = {
                "http_status": exc.code,
                "final_url": exc.geturl(),
                "redirect_chain": chain,
                "detail": str(exc),
            }
            if exc.code not in RETRYABLE_STATUS or attempt == RETRIES:
                return last
        except (TimeoutError, OSError, urllib.error.URLError) as exc:
            last = {
                "http_status": None,
                "final_url": "",
                "redirect_chain": [],
                "detail": f"{type(exc).__name__}: {exc}",
            }
            if attempt == RETRIES:
                return last
        time.sleep((0.8 * (2 ** attempt)) + random.uniform(0, 0.35))
    return last or {"http_status": None, "final_url": "", "redirect_chain": [], "detail": "No response"}


def check_url(url: str) -> dict:
    parsed = urlparse(url)
    if parsed.scheme not in ("http", "https") or not parsed.netloc:
        return {"http_status": None, "final_url": "", "redirect_chain": [],
                "result": "INVALID_URL", "detail": "Only absolute HTTP(S) URLs are checked"}

    # HEAD is cheap but often blocked or implemented incorrectly. Try a small
    # GET on common HEAD restrictions and on 404/410 before classifying a URL.
    head = _request_with_retries(url, "HEAD")
    head_code = head["http_status"]
    result = head
    method_note = "HEAD request"

    if head_code is None or head_code in HEAD_GET_FALLBACK:
        get = _request_with_retries(url, "GET")
        result = get
        method_note = "GET fallback after HEAD response " + str(head_code)
        if get["http_status"] is None:
            # Preserve useful status/final URL information from HEAD if GET
            # also fails at the network layer.
            if head_code is not None:
                result = {**head, "detail": f"GET fallback also failed; HEAD: {head.get('detail', '')}; GET: {get.get('detail', '')}"}
            else:
                result = get
        elif get["http_status"] in (401, 403, 407, 429):
            result["result"] = "MANUAL_REVIEW"
            result["detail"] = "Host may block automated requests or rate-limit; confirm in a browser"
            return result

    code = result["http_status"]
    if code is None:
        result["result"] = "MANUAL_REVIEW"
        result["detail"] = (result.get("detail") or "Request timed out or failed") + "; automated access is inconclusive"
    elif code in (401, 403, 407, 429):
        result["result"] = "MANUAL_REVIEW"
        result["detail"] = "Host may block automated requests or rate-limit; confirm in a browser"
    elif code in (404, 410):
        # Avoid asserting that a project is dead from a single automated check.
        result["result"] = "SUSPECTED_DEAD_LINK"
        result["detail"] = f"HTTP {code} persisted after fallback/retries; manually verify in a browser before changing the catalog"
    elif 200 <= code < 400:
        result["result"] = "OK"
        result["detail"] = method_note
    elif code in RETRYABLE_STATUS:
        result["result"] = "MANUAL_REVIEW"
        result["detail"] = f"Transient/server response HTTP {code} persisted after retries"
    else:
        result["result"] = "HTTP_ERROR"
        result["detail"] = f"HTTP {code}; review manually"
    return result


def main() -> None:
    checked_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    rows = []
    pending = []
    for file_name in DATA_FILES:
        file_path = ROOT / file_name
        if not file_path.exists():
            rows.append({
                "checked_at_utc": checked_at, "data_file": file_name,
                "record_id": "", "project_name": "", "url_field": "",
                "url": "", "http_status": "", "final_url": "",
                "redirect_chain": "[]", "result": "DATA_ERROR",
                "detail": "Expected catalog dataset file is missing",
            })
            continue
        try:
            records = json.loads(file_path.read_text(encoding="utf-8"))
            if not isinstance(records, list):
                raise ValueError("Dataset root must be a JSON array")
        except Exception as exc:
            rows.append({
                "checked_at_utc": checked_at, "data_file": file_name,
                "record_id": "", "project_name": "", "url_field": "",
                "url": "", "http_status": "", "final_url": "",
                "redirect_chain": "[]", "result": "DATA_ERROR", "detail": str(exc),
            })
            continue
        for record in records:
            for field in URL_FIELDS:
                url = str(record.get(field) or "").strip()
                item = {
                    "checked_at_utc": checked_at, "data_file": file_name,
                    "record_id": record.get("id", ""),
                    "project_name": record.get("name", ""),
                    "url_field": field, "url": url,
                }
                if not url:
                    rows.append({**item, "http_status": "", "final_url": "",
                                 "redirect_chain": "[]", "result": "MISSING_URL",
                                 "detail": "URL field is empty"})
                else:
                    pending.append(item)

    unique_urls = sorted({item["url"] for item in pending})
    checked = {}
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as pool:
        futures = {pool.submit(check_url, url): url for url in unique_urls}
        for future in as_completed(futures):
            url = futures[future]
            try:
                checked[url] = future.result()
            except Exception as exc:
                checked[url] = {
                    "http_status": None, "final_url": "", "redirect_chain": [],
                    "result": "MANUAL_REVIEW",
                    "detail": f"Unexpected checker error: {type(exc).__name__}: {exc}",
                }

    for item in pending:
        result = dict(checked[item["url"]])
        result["redirect_chain"] = json.dumps(result.get("redirect_chain", []), ensure_ascii=False)
        rows.append({**item, **result})

    out_dir = ROOT / "link-check-reports"
    out_dir.mkdir(exist_ok=True)
    fields = [
        "checked_at_utc", "data_file", "record_id", "project_name",
        "url_field", "url", "http_status", "final_url", "redirect_chain",
        "result", "detail",
    ]
    csv_path = out_dir / "catalog-link-check.csv"
    json_path = out_dir / "catalog-link-check.json"
    with csv_path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)

    counts = {}
    for row in rows:
        counts[row["result"]] = counts.get(row["result"], 0) + 1
    report = {
        "checked_at_utc": checked_at,
        "total_checks": len(rows),
        "unique_urls_checked": len(unique_urls),
        "results": counts,
        "items": rows,
        "methodology": {
            "head_first": True,
            "get_fallback_for_restricted_or_not_found_head": True,
            "retry_attempts_after_initial_request": RETRIES,
            "timeout_seconds_per_request": TIMEOUT,
            "max_workers": MAX_WORKERS,
            "redirect_chain_recorded": True,
            "suspected_dead_link_policy": "404/410 remains SUSPECTED_DEAD_LINK after fallback/retries; manually confirm before editing catalog",
            "manual_review_policy": "Access-denied, rate-limited, timeout, and persistent transient/server errors are inconclusive",
        },
    }
    json_path.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({
        "checked_at_utc": checked_at,
        "total_checks": len(rows),
        "unique_urls_checked": len(unique_urls),
        "results": counts,
        "csv": str(csv_path),
        "json": str(json_path),
    }, indent=2))


if __name__ == "__main__":
    main()
