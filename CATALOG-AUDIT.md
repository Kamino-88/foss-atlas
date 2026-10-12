# FOSS Atlas — Phase 2 Catalog Audit

Audit date: 2026-10-12  
Catalog version in manifest: 0.2  
Scope: all eight JSON datasets currently loaded by `app.js`. This report distinguishes a source review from a complete legal/license audit.

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

## Verification pass — 2026-10-12

The four later-phase datasets were reviewed against their listed official project websites and source-code repositories. All **28 software records** and **25 OS records** in these four files now have `last_verified: "2026-10-12"` and source-reference URLs.

- Software: 27 records are marked `Partially Verified`; GNU Emacs was already partially verified and its date was refreshed. The review covers project identity and the listed official/source links; this does not imply every platform build, download mirror, dependency, or every third-party component was independently tested.
- Operating systems: 24 records are marked `Partially Verified`; Clear Linux OS is marked `Archived` with `status: "Discontinued"`, based on Intel's archived project repository, which explicitly says it is no longer maintained. See [Intel's archived Clear Linux repository](https://github.com/clearlinux/distribution).
- OS licenses are described as mixed and package-specific where appropriate. They should not be interpreted as one blanket license for every bundled package.
- A small number of license labels were corrected or qualified during the pass: LibreCAD (GPL-2.0-only), SolveSpace (GPL-3.0-only), Anki (AGPL-3.0-or-later), and Forgejo (GPL-3.0-or-later for versions 9.0+; older versions through 8.0 were MIT). Check the specific release/version before relying on a license statement.
- Source URLs are recorded in each record's `verification_sources`. This was a manual editorial source review, not automated uptime monitoring or legal advice. A record remains `Partially Verified` where version-specific licensing or all included components could not be fully confirmed.

Examples of direct repository license evidence reviewed include [Pinta](https://github.com/PintaProject/Pinta), [MeshLab](https://github.com/cnr-isti-vclab/meshlab), [Mixxx](https://github.com/mixxxdj/mixxx), [mpv](https://github.com/mpv-player/mpv), [Spyder](https://github.com/spyder-ide/spyder), [Neovim](https://github.com/neovim/neovim), [Jenkins](https://github.com/jenkinsci/jenkins), [Gitea](https://github.com/go-gitea/gitea), and [Immich](https://github.com/immich-app/immich).

## Duplicate cleanup

- Earlier exact-match cleanup removed 41 software rows and 13 OS rows.
- Phase 2C duplicate review consolidated 11 more software rows and 13 more OS rows.
- Total removed across both passes: **52 software rows and 26 OS rows**.
- Current structural check finds no repeated normalized project names in the eight loaded datasets.
- Canonical IDs and the list of merged records are documented in [`CATALOG-DUPLICATE-REVIEW.md`](https://github.com/Kamino-88/foss-atlas/blob/main/CATALOG-DUPLICATE-REVIEW.md).

## Remaining work

1. Decide whether to remove or separately classify Linearity Curve, which is explicitly marked non-open-source.
2. Review whether the 59 OS entries represent distinct projects, editions, or flavors.
3. Confirm the exact current release/version license for entries where the license varies by release or bundled components.
4. Test all download URLs and source links for reachability on a scheduled basis.
5. Add at least 102 additional verified unique software projects to reach the 250-project target.

## Verification policy

- Stable `id` is the primary key.
- Normalized project name and official website URL are used for duplicate review.
- Shared website hostnames alone are not sufficient to merge records.
- `Verified`: the required fields and official sources have been checked to the catalog's full editorial standard.
- `Partially Verified`: identity and selected metadata/source links were checked, but some fields or bundled-component details remain unchecked.
- `Needs Review`: record requires source verification.
- `Archived`: project is no longer maintained and is shown only if the directory retains discontinued projects.

## Logo policy

1. Use `data/logos.json` when an explicit logo mapping exists.
2. Fall back to the official website favicon.
3. Fall back to generated initials if neither is available.

## Phase 2 targets

- 250+ unique open-source and free-to-use software projects.
- 50+ unique open-source operating-system projects.

Targets count independent projects, not duplicate records. This audit updates the measured baseline; it does not mark Phase 2 complete.
