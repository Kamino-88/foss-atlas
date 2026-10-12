# FOSS Atlas — Duplicate Review Queue

Audit date: 2026-10-12

## Phase 2C result

The remaining same-name duplicate candidates have now been consolidated after matching project names and official website URLs. The catalog keeps the established base ID wherever possible and merges missing fields from the removed record into the retained record.

- Software records consolidated in this pass: 11.
- Operating-system records consolidated in this pass: 13.
- Remaining duplicate groups by normalized name across the eight loaded datasets: **0**.
- The separate NGINX naming inconsistency has been resolved by keeping the canonical name **NGINX Open Source** under ID `nginx`.
- GNU Emacs is retained under ID `emacs`; the erroneous duplicate record that used ID `cowsay` was merged into it.
- No website layout, CSS, app behavior, hosting configuration, or GitHub Pages URL was changed.

## Records consolidated

### Software

| Retained ID | Name | Removed ID |
|---|---|---|
| `gimp` | GIMP | `gimp-phase2` |
| `vlc` | VLC media player | `vlc-phase2` |
| `obs` | OBS Studio | `obs-studio` |
| `keepassxc` | KeePassXC | `keepassxc-phase2` |
| `jupyter` | JupyterLab | `jupyterlab` |
| `notepadpp` | Notepad++ | `notepad-plus-plus` |
| `docker` | Docker Engine | `docker-engine` |
| `nginx` | NGINX Open Source | duplicate `nginx` record |
| `apache-httpd` | Apache HTTP Server | `apache-http-server` |
| `signal` | Signal Desktop | `signal-desktop` |
| `emacs` | GNU Emacs | `cowsay` |

### Operating systems

| Retained ID | Name | Removed ID |
|---|---|---|
| `archlinux` | Arch Linux | `arch-linux` |
| `elementary` | elementary OS | `elementary-os` |
| `zorin` | Zorin OS | `zorin-os` |
| `rocky` | Rocky Linux | `rocky-linux` |
| `almalinux` | AlmaLinux | `alma-linux` |
| `voidlinux` | Void Linux | `void-linux` |
| `alpine` | Alpine Linux | `alpine-linux` |
| `mxlinux` | MX Linux | `mx-linux` |
| `parrot` | Parrot OS | `parrot-os` |
| `kali` | Kali Linux | `kali-linux` |
| `raspios` | Raspberry Pi OS | `raspberry-pi-os` |
| `artix` | Artix Linux | `artix-linux` |
| `serenity` | SerenityOS | `serenityos` |

## Remaining data-quality work

- One software record, Linearity Curve (`vectornator`), is explicitly marked `open_source: false` and has no `source_code_url`; it is excluded from the eligible FOSS software count.
- 27 remaining software records lack both `verification_status` and `last_verified`.
- 25 remaining OS records lack both `license` and `last_verified`.
- These metadata fields should be completed only after checking official project sources. Do not invent verification dates or licenses.

## Links

- [FOSS Atlas website](https://kamino-88.github.io/foss-atlas/)
- [Catalog audit](https://github.com/Kamino-88/foss-atlas/blob/main/CATALOG-AUDIT.md)
