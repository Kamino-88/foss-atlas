# FOSS Atlas — Status and Link Review

Review date: 2026-10-13  
Catalog version: 0.3

This is a targeted editorial review of known-risk entries plus a first automated HTTP link-check run. An HTTP response is a reachability signal, not proof that an application is safe, current, or downloadable.

## Status decisions already made

| Project / record | Action | Reason / source |
|---|---|---|
| Stacer (`stacer`) | Marked `Archived` | The [official repository](https://github.com/oguzhaninan/Stacer) says the project is abandoned and there will be no further releases. |
| Valkey (`valkey`) | Corrected ID, logo mapping and review date | The [official Valkey repository](https://github.com/valkey-io/valkey) identifies the distinct BSD-3-Clause Redis-compatible project. |
| Apache OpenOffice (`openoffice`) | Kept `Maintenance` | The [official development update](https://openoffice.apache.org/blog/what-is-going-on-in-Apache-OpenOffice-development.html), dated 26 September 2026, says 4.1.17 is in preparation. |
| Dia (`freeplane-extra`) | Updated download URL to GNOME source releases | The [archived GNOME download page](https://wiki.gnome.org/Apps/Dia/Download) warns its information may be outdated; current binary availability still needs manual confirmation. |
| Natron (`natron`) | `Needs Review`; not marked discontinued | Its legacy download page returned 404. The official homepage remains the fallback link pending current release verification. |
| FreeCAD Path Workbench | Removed as separate project | [FreeCAD documentation](https://github.com/FreeCAD/FreeCAD-documentation-docusaurus/blob/Stable/docs/workbenches/path.md) describes it as a workbench within FreeCAD. |

## First automated link-check run

The successful GitHub Actions run on 2026-10-12 checked **621 URL fields** across the catalog. The initial report recorded:

- **571 OK**
- **24 DEAD_LINK** (HTTP 404/410)
- **22 MANUAL_REVIEW** (blocked, timed out, rate-limited or otherwise not reliably testable)
- **3 HTTP_ERROR** (other HTTP status errors)
- **1 MISSING_URL** (Linearity Curve source URL; the record is excluded from eligible FOSS count)

A 404/410 is a candidate for repair, not proof the software project is discontinued. 403s and timeouts are not automatically treated as dead links.

## Link repairs and review flags applied on 2026-10-13

- Repaired or replaced reported URLs for MyPaint, Pencil2D, OpenToonz, Natron (fallback homepage), Quod Libet, nomacs, Code::Blocks (official source page), IfcOpenShell, Freeciv, BorgBackup, Kiwix, Immich, EndeavourOS, OpenIndiana (fallback homepage), OpenMandriva Lx, Peppermint OS (fallback homepage), and Porteus.
- The initial checker flagged several source URLs; these have since been independently reviewed against official project documentation and corrected where a canonical official source page was identified. Automated failures are treated as signals for review, not proof of project discontinuation.
- Flagged GNU Emacs and Alpine Linux source links for manual review because the checker returned HTTP 502 and 418 respectively; those responses alone do not prove the links are dead.
- Some replacement links are official project homepages or documentation pages used as safer fallbacks, not a claim that a direct binary download was confirmed. They remain `Partially Verified` or `Needs Review` as appropriate.

## Catalog counts after cleanup

- Software source rows: **148**.
- Eligible software under the app's current open-source + free-to-use rule: **147**.
- Operating-system source rows: **59**.
- Software target: **250**; remaining gap: **103**.
- OS target: **50**; current listed count: **59**, pending editorial review of editions/flavors.

Linearity Curve remains in the raw software source as an excluded record because it is marked non-open-source and has no source-code URL.

## Automated checker

Workflow: [Catalog Link Check](https://github.com/Kamino-88/foss-atlas/actions/workflows/catalog-link-check.yml)  
Checker: [scripts/check_catalog_links.py](https://github.com/Kamino-88/foss-atlas/blob/main/scripts/check_catalog_links.py)

The workflow runs weekly on Mondays and can also be started manually from GitHub Actions. It checks official website, download, and source-code URLs, then uploads CSV/JSON reports as a 90-day artifact.

- `OK`: HTTP response appears successful.
- `DEAD_LINK`: HTTP 404 or 410.
- `HTTP_ERROR`: another HTTP error; review whether transient or changed.
- `MANUAL_REVIEW`: blocked, rate-limited, timed out or otherwise inconclusive.
- `MISSING_URL`: a required URL field is empty.
- `DATA_ERROR`: a source JSON file could not be parsed.

The initial report predates the URL edits. The checker now retries transient failures, falls back from HEAD to a small GET for common server restrictions and 404/410 responses, records redirect chains, reduces concurrency to limit rate-limiting, and labels persistent 404/410 results `SUSPECTED_DEAD_LINK` rather than definitive dead links. Access-denied responses, timeouts and persistent transient errors remain `MANUAL_REVIEW`. Run the workflow again to measure current reachability. The checker does not download/install applications and does not certify software safety.


## Manual link confirmation — 2026-10-13

The project owner manually opened and confirmed that the following entries/URLs are accessible: **BRL-CAD, Bodhi Linux, Xubuntu, Kubuntu, and Slax**, along with other URLs reported by the first automated run. Their prior `Needs Review` labels caused solely by the automated HTTP result have been changed to `Partially Verified`, and the record notes now explain the discrepancy. These are user-reported manual checks, not an independently repeated automated test. Keep the checker report as a diagnostic and do not infer that an HTTP 404/403/timeout alone means a project or URL is discontinued.


## Checker improvements — 2026-10-13

The automated checker was updated to reduce false positives:
- Retries timeouts and transient HTTP responses (408, 425, 429, and common 5xx responses) with a short backoff.
- Uses a browser-like user agent and lower concurrency to reduce simplistic bot blocks and rate limits.
- Falls back from HEAD to a small GET for common HEAD restrictions and for 404/410 responses.
- Follows redirects and records the redirect chain and final URL.
- Reports persistent 404/410 responses as `SUSPECTED_DEAD_LINK`, requiring manual confirmation before catalog changes.
- Keeps access-denied, rate-limited, timeout and persistent transient/server failures as `MANUAL_REVIEW` when automated evidence is inconclusive.

The updated checker has been committed, but a fresh GitHub Actions run is still needed to validate the new behavior against the full live catalog.


## Second automated run and checker refinements — 2026-10-13

The second successful GitHub Actions run (#2) checked **621 URL fields** covering **575 unique URLs**. Its initial results, before the new owner-confirmation override file was added, were:

- **589 OK**
- **23 MANUAL_REVIEW**
- **7 SUSPECTED_DEAD_LINK**
- **1 HTTP_ERROR**
- **1 MISSING_URL**

Compared with run #1, the checker now records final URLs and redirect chains, retries timeouts and transient server errors, falls back from HEAD to a small GET for common HEAD restrictions and 404/410 responses, and labels persistent 404/410 as `SUSPECTED_DEAD_LINK` rather than definitive dead links. The result demonstrates that 404/410 flags fell from 24 to 7, although this is not a controlled apples-to-apples comparison because network conditions and URLs changed.

### Independent review of run #2 candidates

The second run's seven `SUSPECTED_DEAD_LINK` results were BRL-CAD source, ArcoLinux download, Bodhi Linux source, Xubuntu source, Kubuntu source, Slax source, and Porteus source. I independently checked official project pages and corrected these fields where an authoritative destination was identifiable:
- BRL-CAD now points to the active canonical repository at `https://github.com/BRL-CAD/BRL-CAD`.
- Bodhi Linux points to its official source-code page, which links the project's source resources.
- Xubuntu and Kubuntu point to their respective Ubuntu Launchpad source-package pages.
- Slax points to its official source-and-license information page rather than a non-existent project-wide GitHub organization.
- Porteus points to the Codeberg organization referenced by the Porteus forum's source-repository notice.
- ArcoLinux download points to the official download destination referenced by ArcoLinux's own guidance.

The Alpine Linux source URL returned HTTP 418, which indicates automated access was refused and is not proof of a dead source repository. Porteus's downloads page returned HTTP 500 in run #2, which is likewise inconclusive. The single missing URL remains the Linearity Curve source URL, whose record is excluded from the eligible FOSS count.

No owner-reported manual URL overrides are used. Decisions are based on independent official-source research and the automated reports.

### Runtime warning

The workflow actions were upgraded from checkout v4, setup-python v5 and upload-artifact v4 to their newer major versions to address the Node.js 20 deprecation warning shown in the run summary. The next GitHub Actions run must confirm those versions execute successfully on the runner.


## Independent link-check run #4 — 2026-10-13

The project owner ran Catalog Link Check #4 successfully. I retrieved and inspected its uploaded JSON report directly. It contains **621 URL-field checks** across **575 unique URLs**:

- **594 OK**
- **23 MANUAL_REVIEW**
- **2 SUSPECTED_DEAD_LINK**
- **1 HTTP_ERROR**
- **1 MISSING_URL**

The two suspected dead links were:
1. **BRL-CAD source:** `https://github.com/BRL-CAD/BRL-CAD` returned 404. Independent search confirmed the canonical active repository uses the path `https://github.com/BRL-CAD/brlcad`; the catalog has been corrected to that URL.
2. **ArcoLinux download:** `https://arcolinux.info/download/` returned 404. Independent search identified the official Downloads page at `https://www.arcolinux.info/downloads/`; the catalog has been corrected to that URL.

The one HTTP error was Alpine Linux's source repository returning HTTP 418, which indicates the automated request was refused and does not establish that the source is dead. The one missing field is Linearity Curve's source URL; this item is excluded from the eligible FOSS count. The 23 manual-review results include access restrictions and network/server responses where automated checking cannot establish whether the URL is genuinely unavailable.

These corrections were made using independent official-source research, not user-reported manual checks. A new workflow run is needed to confirm both corrected URLs from the runner.


## Independent link-check run #5 — 2026-10-13

The manually triggered **Catalog Link Check #5** completed successfully on commit `f8b6844f2796626e3f708e828e3b5087a31aa0a6`. The workflow itself succeeded; that means the checker completed, not that every catalog URL is valid.

- URL-field checks: **621**
- OK: **597**
- Manual review: **20**
- Suspected dead link: **2**
- HTTP error: **1**
- Missing URL: **1**

Compared with run #4, the checker returned three more OK fields and three fewer manual-review fields. The two corrected URLs did **not** both pass: the runner still reports 404 for the BRL-CAD repository URL and ArcoLinux downloads page. Because GitHub and project sites may behave differently for automated clients, these are not automatically treated as proof that the projects themselves are unavailable.

### Decisions after run #5

- **BRL-CAD:** Keep the project listed, but treat its repository URL as unresolved until the exact canonical URL is confirmed from the project's own source documentation. A 404 from this runner alone is not enough to remove the project.
- **ArcoLinux:** Mark as a legacy/archived entry rather than presenting it as an actively maintained distribution. Its downloads URL is unresolved; do not imply that a current ISO is available until the official project page is confirmed.
- **Alpine Linux:** HTTP 418 remains inconclusive and is not counted as a dead link.
- **Linearity Curve:** the source-code URL remains missing; this item is excluded from the eligible open-source count.
- **Other manual-review results:** 403 access blocks, timeouts, DNS failures, and transient 5xx responses require separate official-source review; they do not by themselves prove a dead project.

The run also displayed a GitHub Actions Node.js 20 deprecation warning. The check completed successfully, but the workflow's action/runtime compatibility should be reviewed separately before the announced runner transition.
