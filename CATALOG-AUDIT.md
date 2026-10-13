# FOSS Atlas — Phase 2 Catalog Audit

Audit date: 2026-10-13  
Catalog version: 0.3  
Scope: all eight JSON datasets loaded by `app.js`. This combines structural counts, targeted official-source review, and the first automated HTTP link-check run.

## Executive result

| Measure | Software | Operating systems |
|---|---:|---:|
| Raw records across loaded source files | 148 | 59 |
| Distinct IDs | 148 | 59 |
| Distinct normalized names | 148 | 59 |
| Unique open-source and free-to-use entries under current engine rules | **147** | **59** |
| Phase 2 target | 250 | 50 |
| Current target gap / surplus | **103 short** | **9 above target** |

The OS total still needs an editorial check to distinguish independent projects from editions and flavors.

## Source datasets and row counts

### Software

| File | Rows |
|---|---:|
| `data/software.json` | 28 |
| `data/software-expansion-100.json` | 92 |
| `data/software-phase2-a.json` | 11 |
| `data/software-phase2-b.json` | 17 |
| **Total** | **148** |

The engine requires `open_source: true` and `free_to_use: true`. Linearity Curve (`vectornator`) remains marked `open_source: false` and excluded from the eligible count. FreeCAD Path Workbench was removed because it is part of FreeCAD, not a separate software project.

### Operating systems

| File | Rows |
|---|---:|
| `data/operating-systems-v1.json` | 8 |
| `data/operating-systems-expansion-25.json` | 26 |
| `data/operating-systems-phase2-25.json` | 9 |
| `data/operating-systems-phase2-b.json` | 16 |
| **Total** | **59** |

## Targeted status review

- **Stacer:** marked `Archived` because the [official repository](https://github.com/oguzhaninan/Stacer) explicitly says it is abandoned.
- **Valkey:** corrected the record ID to `valkey`, added logo mapping, and retained BSD-3-Clause licensing. [Official repository](https://github.com/valkey-io/valkey).
- **Apache OpenOffice:** retained `Maintenance`; the [official development update](https://openoffice.apache.org/blog/what-is-going-on-in-Apache-OpenOffice-development.html) dated 26 September 2026 says 4.1.17 is in preparation.
- **Dia:** changed download URL to the GNOME source release directory; binary availability remains to be checked. [Archived download page](https://wiki.gnome.org/Apps/Dia/Download).
- **Natron:** marked `Needs Review`; not labelled discontinued without evidence.
- **Clear Linux OS:** already marked `Discontinued` / `Archived` based on Intel's archived project repository.
- **Linearity Curve:** excluded from the FOSS count because it is marked non-open-source and lacks a source-code URL.

## Automated link-check results and follow-up

Workflow: [Catalog Link Check](https://github.com/Kamino-88/foss-atlas/actions/workflows/catalog-link-check.yml). Checker: [scripts/check_catalog_links.py](https://github.com/Kamino-88/foss-atlas/blob/main/scripts/check_catalog_links.py).

The first successful run on 2026-10-12 checked **621 URL fields** and returned 571 `OK`, 24 `DEAD_LINK` (404/410), 22 `MANUAL_REVIEW`, 3 `HTTP_ERROR`, and 1 `MISSING_URL`. The missing source URL was on Linearity Curve, which is excluded from eligible FOSS count. Blocked or timed-out URLs are not automatically considered dead.

On 2026-10-13, official/fallback URLs were updated for MyPaint, Pencil2D, OpenToonz, Natron (homepage fallback), Quod Libet, nomacs, Code::Blocks, IfcOpenShell, Freeciv, BorgBackup, Kiwix, Immich, EndeavourOS, OpenIndiana (homepage fallback), OpenMandriva Lx, Peppermint OS (homepage fallback), and Porteus. Ambiguous source links were checked independently against official project documentation. BRL-CAD now points to its canonical active repository; Bodhi Linux to its official source-code page; Xubuntu and Kubuntu to their Ubuntu Launchpad source-package pages; Slax to its official source-and-license page; and Porteus to the Codeberg organization referenced by the project's forum. ArcoLinux's download URL was corrected using its official download guidance. Alpine Linux's source link returned HTTP 418 to the automated checker, an access restriction rather than proof of a dead repository. GNU Emacs's HTTP 502 is also treated as inconclusive.

**Important:** the 621-check report predates these edits. Run the workflow again to measure the repaired links. A reachable homepage is not proof that a current installer exists; entries remain partially verified or flagged until checked to the full editorial standard.

## Remaining work

1. Rerun the automated link-check workflow and review the new report.
2. Manually inspect blocked, rate-limited, JavaScript-only, mirror, and ambiguous source links.
3. Review 59 OS records to distinguish independent projects from editions/flavors.
4. Add at least 103 eligible unique software projects to reach the 250-project target.
5. Recheck current release/version and licensing before marking any entry `Verified`.

## Verification policy

- Stable `id` is the primary key.
- Normalized project name and official website URL are used for duplicate review.
- Shared website hostnames alone are not sufficient to merge records.
- `Verified`: required fields and official sources checked to the catalog's full editorial standard.
- `Partially Verified`: identity and selected metadata/source links reviewed, but some fields remain unchecked.
- `Needs Review`: record requires source verification.
- `Archived`: project is no longer maintained and is retained only if the directory includes discontinued projects.

## Logo policy

1. Use `data/logos.json` when an explicit logo mapping exists.
2. Fall back to the official-site favicon.
3. Fall back to generated initials if neither is available.

## Phase 2 targets

- 250+ unique open-source and free-to-use software projects.
- 50+ unique open-source operating-system projects.

Targets count independent projects, not duplicate records. This audit updates the measured baseline; it does not mark Phase 2 complete.
