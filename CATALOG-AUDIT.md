# FOSS Atlas — Phase 2 Catalog Audit

Date: 2026-09-19
Catalog version: 0.2

## Audit scope

The FOSS Atlas data is currently modular so it remains easy to maintain on GitHub Pages and embed through Google Sites or Zoho Sites. The master manifest is `data/master-catalog-manifest.json`.

## Software source datasets

- `data/software.json`
- `data/software-expansion-100.json`
- `data/software-phase2-a.json`
- `data/software-phase2-b.json`

A software record is eligible for the public FOSS Atlas catalog when `open_source` is `true` and it is not explicitly marked `free_to_use: false`.

## Operating-system source datasets

- `data/operating-systems-v1.json`
- `data/operating-systems-expansion-25.json`
- `data/operating-systems-phase2-25.json`
- `data/operating-systems-phase2-b.json`

OS records are treated as open-source catalog records unless explicitly marked otherwise. Editions/flavors should not be counted as independent operating-system projects unless they have a meaningful independent project identity.

## Deduplication rules

Primary key: `id`.

Secondary review keys:

1. Normalized project name.
2. Official website hostname.

When duplicate records exist, retain the record with the stronger verification state (`Verified` > `Partially Verified` > `Needs Review` > `Archived`).

## Verification states

- `Verified`: official project information checked.
- `Partially Verified`: basic project identity and official links checked; additional fields may still require review.
- `Needs Review`: record requires verification before production classification.
- `Archived`: project is no longer active and should not be treated as an active recommendation.

## Logo policy

1. Use `data/logos.json` when an explicit logo mapping exists.
2. Fall back to the official website favicon.
3. Fall back to generated initials if neither is available.

## Phase 2 targets

- 250+ unique software projects.
- 50+ unique open-source operating-system projects.

The target must be reached with unique projects, not duplicated records or simple distribution flavors counted as independent projects.

## Next audit action

Before declaring Phase 2 complete, perform a final project-by-project verification pass for records marked `Partially Verified` or `Needs Review`, and verify that official website, download, source-code and logo references resolve correctly.
