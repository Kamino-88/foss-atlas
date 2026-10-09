# FOSS Atlas — Duplicate Review Queue

Audit date: 2026-10-09

## What was cleaned

- Removed 54 records only where the record ID, normalized name, and official website URL matched an earlier canonical record.
- The canonical record was kept; any missing non-empty fields from the duplicate were merged into it before removal.
- Raw software records: 201 → 160.
- Raw operating-system records: 85 → 72.
- No UI, CSS, JavaScript, website URL, or hosting configuration was changed.
- Similar names with different IDs, and same IDs with inconsistent names, were deliberately not auto-removed.

## Remaining same-name / different-ID candidates

These pairs appear to describe the same project based on matching normalized names and official website URLs. Confirm the canonical ID before merging them.

### Software: GIMP
- `gimp` — `data/software.json` — https://www.gimp.org/
- `gimp-phase2` — `data/software-phase2-b.json` — https://www.gimp.org/
### Software: VLC media player
- `vlc` — `data/software.json` — https://www.videolan.org/vlc/
- `vlc-phase2` — `data/software-phase2-a.json` — https://www.videolan.org/vlc/
### Software: OBS Studio
- `obs` — `data/software.json` — https://obsproject.com/
- `obs-studio` — `data/software-phase2-a.json` — https://obsproject.com/
### Software: KeePassXC
- `keepassxc` — `data/software.json` — https://keepassxc.org/
- `keepassxc-phase2` — `data/software-phase2-b.json` — https://keepassxc.org/
### Software: JupyterLab
- `jupyter` — `data/software-expansion-100.json` — https://jupyter.org/
- `jupyterlab` — `data/software-phase2-b.json` — https://jupyter.org/
### Software: Notepad++
- `notepadpp` — `data/software-expansion-100.json` — https://notepad-plus-plus.org/
- `notepad-plus-plus` — `data/software-phase2-b.json` — https://notepad-plus-plus.org/
### Software: Docker Engine
- `docker` — `data/software-expansion-100.json` — https://www.docker.com/
- `docker-engine` — `data/software-phase2-b.json` — https://www.docker.com/
### Software: Apache HTTP Server
- `apache-httpd` — `data/software-expansion-100.json` — https://httpd.apache.org/
- `apache-http-server` — `data/software-phase2-b.json` — https://httpd.apache.org/
### Software: Signal Desktop
- `signal` — `data/software-expansion-100.json` — https://signal.org/
- `signal-desktop` — `data/software-phase2-b.json` — https://signal.org/
### Software: GNU Emacs
- `cowsay` — `data/software-expansion-100.json` — https://www.gnu.org/software/emacs/
- `emacs` — `data/software-phase2-b.json` — https://www.gnu.org/software/emacs/
### Operating system: Arch Linux
- `archlinux` — `data/operating-systems-expansion-25.json` — https://archlinux.org/
- `arch-linux` — `data/operating-systems-phase2-25.json` — https://archlinux.org/
### Operating system: elementary OS
- `elementary` — `data/operating-systems-expansion-25.json` — https://elementary.io/
- `elementary-os` — `data/operating-systems-phase2-25.json` — https://elementary.io/
### Operating system: Zorin OS
- `zorin` — `data/operating-systems-expansion-25.json` — https://zorin.com/os/
- `zorin-os` — `data/operating-systems-phase2-25.json` — https://zorin.com/os/
### Operating system: Rocky Linux
- `rocky` — `data/operating-systems-expansion-25.json` — https://rockylinux.org/
- `rocky-linux` — `data/operating-systems-phase2-25.json` — https://rockylinux.org/
### Operating system: AlmaLinux
- `almalinux` — `data/operating-systems-expansion-25.json` — https://almalinux.org/
- `alma-linux` — `data/operating-systems-phase2-25.json` — https://almalinux.org/
### Operating system: Void Linux
- `voidlinux` — `data/operating-systems-expansion-25.json` — https://voidlinux.org/
- `void-linux` — `data/operating-systems-phase2-25.json` — https://voidlinux.org/
### Operating system: Alpine Linux
- `alpine` — `data/operating-systems-expansion-25.json` — https://www.alpinelinux.org/
- `alpine-linux` — `data/operating-systems-phase2-25.json` — https://www.alpinelinux.org/
### Operating system: MX Linux
- `mxlinux` — `data/operating-systems-expansion-25.json` — https://mxlinux.org/
- `mx-linux` — `data/operating-systems-phase2-25.json` — https://mxlinux.org/
### Operating system: Parrot OS
- `parrot` — `data/operating-systems-expansion-25.json` — https://www.parrotsec.org/
- `parrot-os` — `data/operating-systems-phase2-25.json` — https://www.parrotsec.org/
### Operating system: Kali Linux
- `kali` — `data/operating-systems-expansion-25.json` — https://www.kali.org/
- `kali-linux` — `data/operating-systems-phase2-b.json` — https://www.kali.org/
### Operating system: Raspberry Pi OS
- `raspios` — `data/operating-systems-expansion-25.json` — https://www.raspberrypi.com/software/
- `raspberry-pi-os` — `data/operating-systems-phase2-b.json` — https://www.raspberrypi.com/software/
### Operating system: Artix Linux
- `artix` — `data/operating-systems-expansion-25.json` — https://artixlinux.org/
- `artix-linux` — `data/operating-systems-phase2-b.json` — https://artixlinux.org/
### Operating system: SerenityOS
- `serenity` — `data/operating-systems-expansion-25.json` — https://serenityos.org/
- `serenityos` — `data/operating-systems-phase2-b.json` — https://serenityos.org/

## Same-ID record requiring editorial review

- ID `nginx`: canonical `NGINX Open Source` in `data/software-expansion-100.json` (https://nginx.org/); candidate `NGINX` in `data/software-phase2-b.json` (https://nginx.org/). Keep both records unchanged until the display name is decided.

## Next safe step

Review the pairs above, select one stable ID for each true duplicate, and then merge records while preserving useful metadata. Separately audit verification dates, license fields, and the one software entry that is not confirmed open-source.