# Ayu Dark Meta for Telegram

A dark Telegram theme with a navy canvas, warm gray text, and gold accents. It recreates the palette of [Ayu Dark Meta](https://github.com/allmeta/Ayu-Dark-Meta) without installing the VS Code extension.

## Install on Telegram Desktop

1. Download [Ayu Dark Meta.tdesktop-theme](https://github.com/quasa0/ayu-dark-meta-telegram/raw/refs/heads/quasa0/main/Ayu%20Dark%20Meta.tdesktop-theme).
2. Open **Settings → Chat Settings → ⋮ → Create new theme**.
3. Select **Import existing theme** in the initial dialog. Choose the downloaded file.
4. Click **Keep changes** before the countdown expires.

The file includes 467 palette entries and a solid navy wallpaper. This path applies the theme locally. The theme editor’s **Save theme** flow creates a cloud theme.

Verified on Telegram Desktop 6.2.4 for macOS. This is the cross-platform Telegram Desktop client. The separate native macOS client uses a different format.

## Restore your previous theme

Before importing, select **Create new theme → Create** to open the local palette editor. Use the editor’s **⋮ → Export theme** menu to save the current colors and wallpaper. Close the editor without saving changes.

To restore that exported file, use the same **Import existing theme** steps above. Click **Keep changes**. Export/import restoration was tested on Telegram Desktop 6.2.4.

## Optional Telegram Web theme

The [telegram-web](telegram-web/) folder is a CSS-only Chromium extension. It contains two files: a manifest and a stylesheet. It has no JavaScript, background worker, remote assets, or explicit API permissions. Its only match is `https://web.telegram.org/*`.

1. Download or clone this repository.
2. Open `chrome://extensions` in Helium or another Chromium browser.
3. Enable **Developer mode**. Click **Load unpacked** and select the `telegram-web` folder.
4. Reload Telegram Web.

Disable **Ayu Dark Meta — Telegram colors** and reload to restore the original Web appearance. The stylesheet changes colors and hides the wallpaper canvas. It leaves Telegram’s stored theme preferences unchanged.

Web K was visually checked through a temporary CSS preview. Persistent extension installation has not been tested. Web A variables are included, but Web A has not been tested. Telegram Web updates can change selectors and require stylesheet changes.

## iOS

An iOS port is not included. Telegram iOS requires a separate `.tgios-theme` file. Renaming the Desktop file does not convert it. See [Telegram’s iOS theme implementation](https://github.com/TelegramMessenger/Telegram-iOS/blob/master/submodules/TelegramCore/Sources/Themes.swift).

## Palette and source

| Role | Color |
| --- | --- |
| Canvas | `#0a0e14` |
| Text | `#b3b1ad` |
| Accent | `#e6b450` |
| Incoming / outgoing bubbles | `#0d1016` / `#161f2a` |
| Secondary text | `#8a939e` |

The readable [palette](Ayu%20Dark%20Meta.tdesktop-palette) is included. [build_themes.py](build_themes.py) rebuilds the palette, wallpaper PNG, and theme archive with Python 3’s standard library. Run `python3 build_themes.py` from the checkout. The archive uses fixed metadata for reproducible output.

The generator starts from Telegram Desktop’s official night palette, pinned to commit `837b256778dbc6824957af345941d6ac183f07e0`. It maps the colors to Ayu and overrides semantic roles for text, buttons, badges, and message bubbles. [Source provenance](source/provenance.json) records the source paths and hashes.

## Source audit

The visual reference is Marketplace `allmeta.ayu-dark-meta` version `0.0.1`. Its audited VSIX SHA-256 is `c26114dfb49512f8ba1f39bbcbb35a092449134b7e72655912e5f0adfcc9bc2d`.

The package contains five metadata/theme files. It has no executable entry points, activation events, runtime dependencies, or extension pack. This finding covers that exact package, not future updates. The [audit inventory](source/audit.json) includes each file’s size and hash.

The original VS Code theme JSON and VSIX are not redistributed. No license is stated in the source repository. Its current theme JSON also differs from the published package in eight workbench colors. The Telegram palette uses the published package as its visual reference.

Sources: [Ayu Dark Meta repository](https://github.com/allmeta/Ayu-Dark-Meta), [Marketplace listing](https://marketplace.visualstudio.com/items?itemName=allmeta.ayu-dark-meta), [audited VSIX](https://marketplace.visualstudio.com/_apis/public/gallery/publishers/allmeta/vsextensions/ayu-dark-meta/0.0.1/vspackage), [pinned Telegram night theme](https://github.com/telegramdesktop/tdesktop/blob/837b256778dbc6824957af345941d6ac183f07e0/Telegram/Resources/night.tdesktop-theme).

## License

GPL-3.0-or-later. See [LICENSE](LICENSE) and [NOTICE](NOTICE). This is an independent theme adaptation, not an official Telegram or Ayu release.
