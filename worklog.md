# Worklog

## 2026-10-02 — Public repository and downloads verified

- Created https://github.com/quasa0/ayu-dark-meta-telegram as PUBLIC and pushed source commit 5e75707911e776dfc5aa25683b0c499cd639c45e to default branch quasa0/main.
- Anonymous downloads of the README, checksums, Desktop theme/palette/wallpaper and both Web files matched the local bytes. The README's direct theme-download link works; the downloaded archive passes ZIP/member validation.
- The upstream palette has four original trailing spaces. Added a file-specific Git whitespace attribute so diff checks preserve that pinned source byte-for-byte. Project-authored files remain subject to normal whitespace checks.
- Extended the generator to write SHA256SUMS. Repeated generation is byte-identical for all four generated artifacts; each checksum matches its file. No personal settings, backups, screenshots, iOS build or background process published.

## 2026-10-02 — Standalone public Telegram theme repository

- Prepared the Desktop theme archive, readable 467-entry palette, solid navy PNG, optional CSS-only Web extension, dependency-free generator, source provenance/audit inventory, and installation/restore guide. The public source matches the installed Desktop theme's color entries.
- Pinned Telegram's baseline to 837b256778dbc6824957af345941d6ac183f07e0 and verified its extracted source SHA-256. Included GPL-3.0-or-later license and upstream terms/attribution. Linked the unlicensed original allmeta reference without redistributing its VS Code JSON or VSIX.
- Kept personal appearance snapshots, local editor customization/restore scripts, screenshots, and previous workspace logs outside this repository. Commit identity uses the GitHub noreply address. User authorized creation and publication of quasa0/ayu-dark-meta-telegram.
- Verification passed: two builds byte-identical; all 467 generated colors match the installed theme; palette aliases resolve; core message, button and badge contrast >= 4.5:1; ZIP members/content and PNG chunks/color valid; Web manifest scoped to web.telegram.org with no JavaScript, external assets or explicit API permissions; public-file privacy scan clean.
- Desktop import and original-theme restoration were tested on Telegram Desktop 6.2.4 for macOS during theme creation. Web K preview was checked; persistent extension installation and Web A remain untested. An iOS port is not included.
- No server, watcher, or background process started.
