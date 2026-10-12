# FOSS Atlas — Phase 2 Catalog Audit

Audit date: 2026-10-12  
Catalog version: 0.3  
Scope: all eight JSON datasets loaded by `app.js`. This combines structural counts with a targeted official-source review; it is not yet a full HTTP check of every URL.

## Executive result

| Measure | Software | Operating systems |
|---|---:|---:|
| Raw records across loaded source files | 148 | 59 |
| Distinct IDs | 148 | 59 |
| Distinct normalized names | 148 | 59 |
| Unique open-source and free-to-use software / OS entries under current engine rules | **147** | **59** |
| Phase 2 target | 250 | 50 |
| Current target gap / surplus | **103 short** | **9 above target** |

The project owner previously confirmed that the website displayed 148 software projects and 59 operating systems before this cleanup. Removing the separate FreeCAD Path Workbench entry changes the raw software count to 148 and eligible count to 147. The OS total still needs an editorial check to distinguish independent projects from editions and flavors.

## Source datasets and row counts

### Software

| File | Rows |
|---|---:|
| `data/software.json` | 28 |
| `data/software-expansion-100.json` | 92 |
| `data/software-phase2-a.json` | 11 |
| `data/software-phase2-b.json` | 17 |
| **Total** | **148** |

The engine requires `open_source: true` and `free_to_use: true`. Linearity Curve (`vectornator`) remains marked `open_source: false` and excluded from the eligible count. One non-standalone listing, FreeCAD Path Workbench, was removed because it is a built-in FreeCAD workbench (called CAM Workbench in current FreeCAD documentation), not a separate software project.

### Operating systems

| File | Rows |
|---|---:|
| `data/operating-systems-v1.json` | 8 |
| `data/operating-systems-expansion-25.json` | 26 |
| `data/operating-systems-phase2-25.json` | 9 |
| `data/operating-systems-phase2-b.json` | 16 |
| **Total** | **59** |

## Targeted status and link review — 2026-10-12

- **Stacer:** marked `Archived`. Its official GitHub README explicitly says the project has been abandoned and there will be no further releases. [Official repository](https://github.com/oguzhaninan/Stacer).
- **Valkey:** renamed the record ID from `redis` to `valkey`, added a Valkey logo mapping, and retained the BSD-3-Clause license. The official repository identifies Valkey as a distinct Redis-compatible project and lists BSD-3-Clause. [Valkey repository](https://github.com/valkey-io/valkey).
- **Apache OpenOffice:** retained status `Maintenance`. The official project blog reported on 26 September 2026 that 4.1.17 was in preparation and described further development towards a future major release. [Official development update](https://openoffice.apache.org/blog/what-is-going-on-in-Apache-OpenOffice-development.html).
- **Dia:** updated its download link to the GNOME source release directory referenced by the archived GNOME download page. The GNOME wiki warns that its version information may be outdated, so current binary availability still needs confirmation. [Archived download page](https://wiki.gnome.org/Apps/Dia/Download).
- **Natron:** retained status `Maintenance`, but marked `Needs Review` because its legacy website and download page require a current release/link check. It has not been labelled discontinued without sufficient evidence.
- **FreeCAD Path Workbench:** removed as a separate catalog item because current FreeCAD documentation describes CAM as a workbench inside FreeCAD. [Official FreeCAD documentation](https://github.com/FreeCAD/FreeCAD-documentation-docusaurus/blob/Stable/docs/workbenches/path.md).
- **Clear Linux OS:** already marked `Discontinued` / `Archived` based on Intel's archived project repository.
- **Linearity Curve:** remains excluded from the FOSS count because it is marked non-open-source and lacks a source-code URL.

## What is and is not verified

The targeted status decisions above are based on the official project sources linked in this report. **Not every download/source URL in all 207 remaining catalog records has been independently requested and tested.** A browser-visible page, a source repository, and a working downloadable binary are separate checks. To avoid false assurances, unresolved links remain flagged rather than being assigned a successful verification date.

A weekly automated link-check workflow is now available at [GitHub Actions](https://github.com/Kamino-88/foss-atlas/actions/workflows/catalog-link-check.yml). It tests official website, download and source URLs, records HTTP status/errors, and preserves CSV/JSON report artifacts for 90 days. HTTP errors such as 403/429 are treated as “needs manual review”, not automatically as dead links. The first workflow run has not yet been executed by this edit.

## Duplicate cleanup

- Earlier exact-match cleanup removed 41 software rows and 13 OS rows.
- Phase 2C duplicate review consolidated 11 more software rows and 13 more OS rows.
- Total removed across those duplicate passes: **52 software rows and 26 OS rows**.
- A further separate non-project entry (FreeCAD Path Workbench) was removed in this review.
- Canonical IDs and the list of duplicate merges are documented in [`CATALOG-DUPLICATE-REVIEW.md`](https://github.com/Kamino-88/foss-atlas/blob/main/CATALOG-DUPLICATE-REVIEW.md).

## Remaining work

1. Run the new automated link-check workflow and fix genuine 404/410 or invalid redirects.
2. Manually inspect blocked, rate-limited, JavaScript-only and mirror links.
3. Review the 59 OS entries to distinguish independent projects from editions and flavors.
4. Add at least 103 eligible unique software projects to reach the 250-project target.
5. Recheck current release/version licensing before upgrading any entry to `Verified`.

## Verification policy

- Stable `id` is the primary key.
- Normalized project name and official website URL are used for duplicate review.
- Shared website hostnames alone are not sufficient to merge records.
- `Verified`: required fields and official sources checked to the catalog's full editorial standard.
- `Partially Verified`: identity and selected metadata/source links reviewed, but some fields or bundled-component details remain unchecked.
- `Needs Review`: record requires source verification.
- `Archived`: project is no longer maintained and is shown only if the directory retains discontinued projects.

## Logo policy

1. Use `data/logos.json` when an explicit logo mapping exists.
2. Fall back to the official-site favicon.
3. Fall back to generated initials if neither is available.

## Phase 2 targets

- 250+ unique open-source and free-to-use software projects.
- 50+ unique open-source operating-system projects.

Targets count independent projects, not duplicate records. This audit updates the measured baseline; it does not mark Phase 2 complete.
