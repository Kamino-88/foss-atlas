# FOSS Atlas — Phase 2 Catalog Audit

Audit date: 2026-10-12  
Catalog version in manifest: 0.2  
Scope: all eight JSON datasets currently loaded by `app.js`. This is a structural metadata audit; external URLs and license claims have not all been independently live-tested.

## Executive result

| Measure | Software | Operating systems |
|---|---:|---:|
| Raw records across loaded source files | 149 | 59 |
| Distinct IDs | 149 | 59 |
| Distinct normalized names | 149 | 59 |
| Unique eligible records using current catalog-engine rules | **148** | **59** |
| Phase 2 target | 250 | 50 |
| Current target gap / surplus | **102 short** | **9 above target** |

The project owner previously confirmed that the website displays 148 software projects and 59 operating systems. These counts match the current data. The OS total still needs an editorial check to distinguish independent OS projects from editions and flavors.

## Source datasets and row counts

### Software

| File | Rows |
|---|---:|
| `data/software.json` | 28 |
| `data/software-expansion-100.json` | 93 |
| `data/software-phase2-a.json` | 11 |
| `data/software-phase2-b.json` | 17 |
| **Total** | **149** |

The engine requires `open_source: true` and `free_to_use: true`. Linearity Curve (`vectornator`) is marked `open_source: false`, is excluded from the eligible software count, and has no `source_code_url`.

### Operating systems

| File | Rows |
|---|---:|
| `data/operating-systems-v1.json` | 8 |
| `data/operating-systems-expansion-25.json` | 26 |
| `data/operating-systems-phase2-25.json` | 9 |
| `data/operating-systems-phase2-b.json` | 16 |
| **Total** | **59** |

All 59 current OS records are marked open source and free to use. Operating-system license metadata is now present for the 25 records that lacked it; because distributions bundle many components, most use the careful label “Mixed open-source licenses; package-specific” rather than implying a single license covers the entire distribution.

## Duplicate cleanup

- Earlier exact-match cleanup removed 41 software rows and 13 OS rows.
- Phase 2C duplicate review consolidated 11 more software rows and 13 more OS rows.
- Total removed across both passes: **52 software rows and 26 OS rows**.
- Current structural check finds no repeated normalized project names in the eight loaded datasets.
- Canonical IDs and the list of merged records are documented in [`CATALOG-DUPLICATE-REVIEW.md`](https://github.com/Kamino-88/foss-atlas/blob/main/CATALOG-DUPLICATE-REVIEW.md).

## Verification metadata status

- The 27 software records that lacked verification metadata now have `verification_status` and `verification_sources` fields. Six records are labelled `Partially Verified`; the other 21 are labelled `Needs Review`.
- Those 27 records still lack `last_verified`. No verification date was invented.
- The 25 OS records that lacked license metadata now have `license`, `verification_status`, and `verification_sources` fields. They are marked `Partially Verified`, and still lack `last_verified`.
- The source fields point to the project's official website and source repository as references. Their presence does not itself mean the URLs were successfully tested or that every license was independently confirmed.
- Linearity Curve (`vectornator`) remains excluded pending a decision on whether it belongs in a directory specifically for open-source software.

## Recommended next steps

1. Open the official project and source links for the 27 software records and 25 OS records; record a real verification date only after checking them.
2. Check package-specific license information for distributions; do not substitute a single blanket license where it would be misleading.
3. Decide whether to remove or separately classify Linearity Curve.
4. Review whether the 59 OS entries represent distinct projects, editions, or flavors.
5. Add at least 102 additional verified unique software projects to reach the 250-project target.

## Deduplication and verification policy

- Stable `id` is the primary key.
- Normalized project name and official website URL are used for duplicate review.
- Shared website hostnames alone are not sufficient to merge records.
- `Verified`: official project information has been checked.
- `Partially Verified`: identity or some metadata has been reviewed, but important fields remain unchecked.
- `Needs Review`: record needs verification before being treated as fully verified.
- `Archived`: project is no longer active and should not be treated as an active recommendation.

## Logo policy

1. Use `data/logos.json` when an explicit logo mapping exists.
2. Fall back to the official website favicon.
3. Fall back to generated initials if neither is available.

## Phase 2 targets

- 250+ unique open-source and free-to-use software projects.
- 50+ unique open-source operating-system projects.

Targets count independent projects, not duplicate records. This audit updates the measured baseline; it does not mark Phase 2 complete.
