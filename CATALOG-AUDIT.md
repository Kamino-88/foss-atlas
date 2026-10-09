# FOSS Atlas — Phase 2 Catalog Audit

Audit date: 2026-10-09  
Cleanup update: 2026-10-09  
Catalog version in manifest: 0.2  
Scope: all eight JSON datasets currently loaded by `app.js`. This is a structural/count audit of the repository data; it is not a live verification that every external URL works.

## Executive result

| Measure | Software | Operating systems |
|---|---:|---:|
| Raw records across loaded source files | 160 | 72 |
| Distinct IDs before name-level deduplication | 149 | 59 |
| Distinct normalized names before eligibility filtering | 149 | 59 |
| Unique eligible records using the current catalog engine's rules | **148** | **59** |
| Phase 2 target | 250 | 50 |
| Current target gap / surplus | **102 short** | **9 above target** |

The software target is not yet met. The OS count is above 50 by normalized name, but the final editorial pass must still check that each item is a meaningfully independent OS project rather than a flavor or edition.

## Source datasets and row counts

### Software

| File | Rows | Notes |
|---|---:|---|
| `data/software.json` | 28 | Base dataset |
| `data/software-expansion-100.json` | 94 | Includes one record explicitly marked `open_source: false` |
| `data/software-phase2-a.json` | 13 | Remaining records lack `verification_status` and `last_verified` |
| `data/software-phase2-b.json` | 25 | Remaining records lack `verification_status` and `last_verified` |
| **Total** | **160** | **148 unique eligible records after the current engine's strict eligibility and deduplication rules** |

Software eligibility in the current engine requires both `open_source: true` and `free_to_use: true`. There are 159 records marked open source, all 160 records have `free_to_use: true`, and one record (Linearity Curve / `vectornator`) is explicitly not open source and is excluded. The remaining reduction is mainly duplicate projects and same-name/different-ID candidates.

### Operating systems

| File | Rows | Notes |
|---|---:|---|
| `data/operating-systems-v1.json` | 8 | Base dataset |
| `data/operating-systems-expansion-25.json` | 26 | Expansion dataset |
| `data/operating-systems-phase2-25.json` | 18 | Remaining records lack `license` and `last_verified` |
| `data/operating-systems-phase2-b.json` | 20 | Remaining records lack `license` and `last_verified` |
| **Total** | **85** | **59 unique names after deduplication** |

All 72 remaining OS records currently have `open_source: true`. The 38 records in the two later OS datasets need license and verification-date metadata added after checking official sources.

## Duplicate and consistency findings

- **Software:** Removed 41 exact duplicate records (matching ID, normalized name, and official website URL), merging any missing fields into the earlier canonical record. Remaining same-name/different-ID candidates are listed in `CATALOG-DUPLICATE-REVIEW.md`.
- **Operating systems:** Removed 13 exact duplicate records (matching ID, normalized name, and official website URL), merging any missing fields into the earlier canonical record. Remaining same-name/different-ID candidates are listed in `CATALOG-DUPLICATE-REVIEW.md`.
- Some duplicates use different IDs for the same name (for example, `gimp` / `gimp-phase2`, and `archlinux` / `arch-linux`). These were deliberately left untouched for editorial review.
- No repeated official-site hostnames were detected by the structural URL-host check in this audit. This does not prove that all URLs resolve or are official.
- One software record is missing `source_code_url`. No software or OS records were missing ID, name, description, official website, or download URL in the audited files.
- The current source sets have **38 software records** without `verification_status` and `last_verified`, and **38 OS records** without `license` and `last_verified`.

## Recommended remediation order

1. Keep the existing website layout and URL unchanged.
2. Review `CATALOG-DUPLICATE-REVIEW.md` and resolve the remaining same-name/different-ID candidates. Exact duplicate cleanup has been completed for 54 records.
3. Verify the 38 remaining later-phase software records against official project sources; add `verification_status`, `last_verified`, and `verification_sources`.
4. Verify license and last-checked date for the 38 remaining later-phase OS records.
5. Review the one software entry explicitly marked not open source and the one missing source-code link.
6. Recalculate counts after editorial verification. Add new software only after remaining duplicate candidates are resolved; the current software target gap is 102 unique projects.

## Deduplication and verification policy

- Primary key: stable `id`.
- Secondary duplicate-review key: normalized project name.
- Shared official website hostname is a review signal only, not an automatic merge rule.
- Exact cleanup performed: match on stable ID, normalized name, and exact official website URL; preserve missing valid fields from the duplicate record. Different-ID candidates and inconsistent same-ID records remain in the review queue.
- `Verified`: official project information checked.
- `Partially Verified`: basic identity and official links checked; some fields need further review.
- `Needs Review`: record requires verification before production classification.
- `Archived`: project is no longer active and should not be treated as an active recommendation.

## Logo policy

1. Use `data/logos.json` when an explicit logo mapping exists.
2. Fall back to the official website favicon.
3. Fall back to generated initials if neither is available.

## Phase 2 targets

- 250+ unique software projects.
- 50+ unique open-source operating-system projects.

Targets count independent projects, not duplicated records or simple distribution flavors. This audit updates the measured baseline; it does not mark Phase 2 complete.
