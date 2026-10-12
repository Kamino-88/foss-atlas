# FOSS Atlas — Phase 2 Catalog Audit

Audit date: 2026-10-12  
Catalog version in manifest: 0.2  
Scope: all eight JSON datasets currently loaded by `app.js`. This is a structural/count audit of repository data; it is not a live verification that every external URL resolves.

## Executive result

| Measure | Software | Operating systems |
|---|---:|---:|
| Raw records across loaded source files | 149 | 59 |
| Distinct IDs | 149 | 59 |
| Distinct normalized names | 149 | 59 |
| Unique eligible records using current catalog-engine rules | **148** | **59** |
| Phase 2 target | 250 | 50 |
| Current target gap / surplus | **102 short** | **9 above target** |

The website was previously confirmed by the project owner to display 148 software projects and 59 operating systems. This matches the eligible counts calculated from the current data. The software target is not yet met. The OS count exceeds 50, but the editorial review should still ensure that entries are meaningfully independent projects rather than editions or flavors.

## Source datasets and row counts

### Software

| File | Rows | Notes |
|---|---:|---|
| `data/software.json` | 28 | Base dataset |
| `data/software-expansion-100.json` | 93 | Includes one record explicitly marked `open_source: false` |
| `data/software-phase2-a.json` | 11 | Remaining metadata review is needed |
| `data/software-phase2-b.json` | 17 | Remaining metadata review is needed |
| **Total** | **149** | **148 eligible open-source and free-to-use projects** |

The current engine requires both `open_source: true` and `free_to_use: true`. One record, Linearity Curve (`vectornator`), is explicitly marked not open source and is excluded. That record also lacks a `source_code_url`.

### Operating systems

| File | Rows | Notes |
|---|---:|---|
| `data/operating-systems-v1.json` | 8 | Base dataset |
| `data/operating-systems-expansion-25.json` | 26 | Expansion dataset |
| `data/operating-systems-phase2-25.json` | 9 | Metadata review is needed |
| `data/operating-systems-phase2-b.json` | 16 | Metadata review is needed |
| **Total** | **59** | **59 unique OS names** |

All 59 current OS records have `open_source: true` and `free_to_use: true`. Twenty-five OS records still need a license field and last-verified date.

## Duplicate cleanup results

- Earlier exact-match cleanup removed 41 software records and 13 OS records.
- Phase 2C review consolidated another 11 software records and 13 OS records whose normalized names and official website URLs matched.
- Total removed during both cleanup passes: **52 software rows and 26 OS rows**.
- Current duplicate check finds **zero repeated normalized project names** across the loaded datasets.
- Canonical IDs and merged-record details are documented in [`CATALOG-DUPLICATE-REVIEW.md`](https://github.com/Kamino-88/foss-atlas/blob/main/CATALOG-DUPLICATE-REVIEW.md).

## Remaining verification findings

- 27 software records lack both `verification_status` and `last_verified`.
- 25 OS records lack both `license` and `last_verified`.
- One software record (Linearity Curve / `vectornator`) is explicitly marked `open_source: false` and is missing `source_code_url`; it is excluded from the eligible software count.
- This is a structural audit, not a live test of every external website, source repository, download link, or license statement.

## Recommended remediation order

1. Verify the 27 software records against official project sources; then add `verification_status`, `last_verified`, and `verification_sources`.
2. Verify license and current status for the 25 OS records; then add `license` and `last_verified`.
3. Decide whether to retain or remove Linearity Curve from a directory specifically for open-source software.
4. Recalculate the catalog and review OS independence before expansion.
5. Add at least 102 verified, genuinely unique software projects to reach the 250-project target.

## Deduplication and verification policy

- Primary key: stable `id`.
- Secondary review key: normalized project name, cross-checked against official website URL.
- Shared official website hostname alone is a review signal, not an automatic merge rule.
- Exact duplicate cleanup preserves the retained record and fills missing fields from the removed record where available.
- `Verified`: official project information checked.
- `Partially Verified`: basic identity and official links checked; some fields need review.
- `Needs Review`: record requires verification before production classification.
- `Archived`: project is no longer active and should not be treated as an active recommendation.

## Logo policy

1. Use `data/logos.json` when an explicit logo mapping exists.
2. Fall back to the official website favicon.
3. Fall back to generated initials if neither is available.

## Phase 2 targets

- 250+ unique open-source and free-to-use software projects.
- 50+ unique open-source operating-system projects.

Targets count independent projects, not duplicate records. This audit updates the measured baseline; it does not mark Phase 2 complete.
