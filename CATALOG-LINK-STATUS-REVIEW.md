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
- Marked source/download entries for BRL-CAD, ArcoLinux, Bodhi Linux, Xubuntu, Kubuntu, and Slax as `Needs Review` where the checker result did not establish a reliable canonical URL.
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

The report reflects the initial run before these URL edits. Run the workflow again to measure the repaired URLs. The checker does not download/install applications and does not certify software safety.


## Manual link confirmation — 2026-10-13

The project owner manually opened and confirmed that the following entries/URLs are accessible: **BRL-CAD, Bodhi Linux, Xubuntu, Kubuntu, and Slax**, along with other URLs reported by the first automated run. Their prior `Needs Review` labels caused solely by the automated HTTP result have been changed to `Partially Verified`, and the record notes now explain the discrepancy. These are user-reported manual checks, not an independently repeated automated test. Keep the checker report as a diagnostic and do not infer that an HTTP 404/403/timeout alone means a project or URL is discontinued.
