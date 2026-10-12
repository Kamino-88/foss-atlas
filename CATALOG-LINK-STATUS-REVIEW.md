# FOSS Atlas — Status and Link Review

Review date: 2026-10-12  
Catalog version: 0.3

This is a targeted editorial review of known-risk entries. It is not a claim that every URL has been live-tested. A scheduled GitHub Actions checker is now available to test the official website, download, and source-code URLs across all catalog datasets.

## Changes made

| Project / record | Action | Reason / source |
|---|---|---|
| Stacer (`elementary-tweaks`) | Marked `Archived`; updated verification date | The official [Stacer repository](https://github.com/oguzhaninan/Stacer) explicitly says the project is abandoned and there will be no further releases. |
| Valkey (`valkey`) | Corrected ID from `redis` to `valkey`; added logo mapping; recorded review date | The [official Valkey repository](https://github.com/valkey-io/valkey) identifies the project and lists BSD-3-Clause licensing. Valkey is separate from current Redis releases. |
| Apache OpenOffice (`openoffice`) | Kept status `Maintenance`; updated review date and notes | The [official development update](https://openoffice.apache.org/blog/what-is-going-on-in-Apache-OpenOffice-development.html), dated 26 September 2026, says 4.1.17 is in preparation and describes further development. |
| Dia (`freeplane-extra`) | Updated download URL to `https://download.gnome.org/sources/dia/`; added review note | The [archived GNOME download page](https://wiki.gnome.org/Apps/Dia/Download) warns its information may be outdated and points users to GNOME source releases. Current binary availability still needs a manual check. |
| Natron (`natron`) | Marked `Needs Review`; did not mark discontinued | Its legacy website/download page needs a current release and link check. Lack of recent visible activity alone is not enough evidence to mark it discontinued. |
| FreeCAD Path Workbench | Removed as a separate software record | Current [FreeCAD documentation](https://github.com/FreeCAD/FreeCAD-documentation-docusaurus/blob/Stable/docs/workbenches/path.md) describes the CAM/Path workbench as part of FreeCAD, not a separate independent project. |

## Catalog counts after cleanup

- Software source rows: **148**.
- Eligible software under the app's current open-source + free-to-use rule: **147**.
- Operating-system source rows: **59**.
- Software target: **250**; remaining gap: **103**.
- OS target: **50**; current listed count: **59**, pending an editorial check of editions/flavors.

Linearity Curve remains in the raw software source as an excluded record because it is marked non-open-source and has no source-code URL.

## Automated link checks

Workflow: [Catalog Link Check](https://github.com/Kamino-88/foss-atlas/actions/workflows/catalog-link-check.yml)  
Checker: [scripts/check_catalog_links.py](https://github.com/Kamino-88/foss-atlas/blob/main/scripts/check_catalog_links.py)

The workflow runs weekly on Mondays and can also be started manually from the GitHub Actions page. It checks the official website, download, and source-code URLs and uploads CSV and JSON reports as an artifact for 90 days.

Interpretation:
- `OK`: HTTP response appears successful.
- `DEAD_LINK`: HTTP 404 or 410; inspect and repair the record.
- `HTTP_ERROR`: other HTTP error; review the response and whether the URL changed.
- `MANUAL_REVIEW`: blocked, rate-limited, timed out, or otherwise not reliably testable automatically.
- `MISSING_URL`: a required URL field is empty.
- `DATA_ERROR`: a source JSON file could not be parsed.

The checker does not download/install applications and does not certify software safety. A 403/429 is not automatically treated as a dead link. The first scheduled run has not yet been executed by this edit, so there is no fabricated test result here.
