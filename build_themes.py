# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (C) 2026 quasa0
"""Build the declarative Telegram theme. Python standard library only."""
from pathlib import Path
import colorsys
import hashlib
import re
import struct
import zipfile
import zlib

ROOT = Path(__file__).resolve().parent
BG = '#0a0e14'
SURFACE = '#0d1016'
RAISED = '#161f2a'
SELECTED = '#292d36'
FG = '#b3b1ad'
SECONDARY = '#8a939e'
MUTED = '#626a73'
ACCENT = '#e6b450'
RED = '#f07178'
GREEN = '#c2d94c'

# Map Telegram's complete official night palette, then set critical semantic roles.
def recolor(value):
    rgb = tuple(int(value[i:i+2], 16) / 255 for i in (1, 3, 5))
    hue, saturation, brightness = colorsys.rgb_to_hsv(*rgb)
    alpha = value[7:]
    if saturation < 0.18 or brightness < 0.22:
        base = FG if brightness > .7 else SECONDARY if brightness > .4 else MUTED if brightness > .3 else RAISED if brightness > .15 else BG
    elif brightness < .37:
        base = RAISED if brightness > .22 else BG
    elif 0.47 <= hue <= 0.7:
        base = ACCENT
    elif hue > .92 or hue < .05:
        base = RED
    elif hue < .19:
        base = '#ffb454'
    elif hue < .46:
        base = GREEN if hue < .37 else '#95e6cb'
    else:
        base = '#c594c5'
    return base + alpha

rows = []
for line in (ROOT / 'source/telegram-night-base.tdesktop-palette').read_text().splitlines():
    match = re.match(r'^(\w+):\s*(#[0-9a-fA-F]{6}(?:[0-9a-fA-F]{2})?|\w+);', line)
    if match:
        key, value = match.groups()
        rows.append((key, recolor(value) if value.startswith('#') else value))
palette = dict(rows)
overrides = {
    'windowBg': BG, 'windowFg': FG, 'windowBgOver': RAISED, 'windowBgRipple': SELECTED,
    'windowFgOver': FG, 'windowBoldFg': FG, 'windowBoldFgOver': FG,
    'windowSubTextFg': SECONDARY, 'windowSubTextFgOver': FG,
    'windowBgActive': ACCENT, 'windowFgActive': BG, 'windowActiveTextFg': ACCENT,
    'windowShadowFg': '#00010a', 'windowShadowFgFallback': BG,
    'activeButtonBg': ACCENT, 'activeButtonBgOver': '#e1af4b', 'activeButtonBgRipple': '#d5a33f',
    'activeButtonFg': BG, 'activeButtonFgOver': BG,
    'activeButtonSecondaryFg': RAISED, 'activeButtonSecondaryFgOver': RAISED,
    'activeLineFg': ACCENT, 'lightButtonBg': BG, 'lightButtonBgOver': RAISED,
    'lightButtonFg': ACCENT, 'lightButtonFgOver': ACCENT,
    'menuBg': SURFACE, 'menuBgOver': RAISED, 'menuFgDisabled': MUTED,
    'menuIconFg': SECONDARY, 'menuIconFgOver': FG, 'menuSeparatorFg': SELECTED,
    'placeholderFg': SECONDARY, 'placeholderFgActive': SECONDARY,
    'inputBorderFg': SELECTED, 'filterInputBorderFg': SELECTED, 'filterInputInactiveBg': SURFACE,
    'checkboxFg': MUTED, 'sliderBgInactive': SELECTED, 'sliderBgActive': ACCENT,
    'tooltipBg': SURFACE, 'tooltipFg': FG, 'tooltipBorderFg': SELECTED,
    'titleBg': BG, 'titleBgActive': BG, 'titleFg': SECONDARY, 'titleFgActive': FG,
    'boxBg': BG, 'boxTitleFg': FG, 'boxTitleAdditionalFg': SECONDARY, 'boxSearchBg': SURFACE,
    'contactsBg': BG, 'contactsBgOver': RAISED, 'contactsStatusFg': SECONDARY,
    'contactsStatusFgOver': SECONDARY, 'contactsStatusFgOnline': ACCENT,
    'dialogsBg': BG, 'dialogsBgOver': SURFACE, 'dialogsBgActive': RAISED,
    'dialogsNameFg': FG, 'dialogsNameFgOver': FG, 'dialogsNameFgActive': FG,
    'dialogsTextFg': SECONDARY, 'dialogsTextFgOver': FG, 'dialogsTextFgActive': FG,
    'dialogsDateFg': SECONDARY, 'dialogsDateFgOver': SECONDARY, 'dialogsDateFgActive': SECONDARY,
    'dialogsTextFgService': ACCENT, 'dialogsTextFgServiceOver': ACCENT,
    'dialogsTextFgServiceActive': ACCENT, 'dialogsSentIconFg': ACCENT,
    'dialogsSentIconFgOver': ACCENT, 'dialogsSentIconFgActive': ACCENT,
    'dialogsUnreadBg': ACCENT, 'dialogsUnreadBgOver': ACCENT, 'dialogsUnreadBgActive': ACCENT,
    'dialogsUnreadFg': BG, 'dialogsUnreadFgOver': BG, 'dialogsUnreadFgActive': BG,
    'dialogsUnreadBgMuted': SECONDARY, 'dialogsUnreadBgMutedOver': SECONDARY,
    'dialogsUnreadBgMutedActive': SECONDARY, 'dialogsOnlineBadgeFg': GREEN,
    'dialogsOnlineBadgeFgActive': GREEN, 'topBarBg': BG, 'searchedBarBg': SURFACE,
    'historyTextInFg': FG, 'historyTextOutFg': FG,
    'historyTextInFgSelected': FG, 'historyTextOutFgSelected': FG,
    'historyLinkInFg': ACCENT, 'historyLinkOutFg': ACCENT,
    'historyLinkInFgSelected': '#ffb454', 'historyLinkOutFgSelected': '#ffb454',
    'historyOutIconFg': ACCENT, 'historyOutIconFgSelected': ACCENT,
    'msgInBg': SURFACE, 'msgOutBg': RAISED, 'msgInBgSelected': SELECTED, 'msgOutBgSelected': SELECTED,
    'msgInDateFg': SECONDARY, 'msgOutDateFg': SECONDARY,
    'msgInDateFgSelected': FG, 'msgOutDateFgSelected': FG,
    'msgInServiceFg': ACCENT, 'msgOutServiceFg': ACCENT,
    'msgInReplyBarColor': ACCENT, 'msgOutReplyBarColor': ACCENT,
    'msgInMonoFg': '#95e6cb', 'msgOutMonoFg': '#95e6cb',
    'msgServiceBg': '#161f2ad5', 'msgServiceBgSelected': SELECTED, 'msgServiceFg': FG,
    'historyComposeAreaBg': BG, 'historyComposeAreaFg': FG,
    'historyComposeIconFg': SECONDARY, 'historyComposeIconFgOver': FG,
    'historySendIconFg': ACCENT, 'historySendIconFgOver': '#ffb454',
    'historyPinnedBg': SURFACE, 'historyReplyBg': BG,
    'mainMenuBg': BG, 'mainMenuCoverBg': SURFACE, 'mainMenuCoverFg': FG,
    'mainMenuCloudBg': RAISED, 'mainMenuCloudFg': ACCENT,
    # Keep light ink on dark overlays and dark ink on bright badges/buttons.
    'radialFg': FG, 'stickerPanDeleteFg': FG, 'historyForwardChooseFg': FG,
    'toastFg': FG, 'mediaviewMenuFg': FG, 'mediaviewControlFg': FG,
    'trayCounterFg': BG, 'profileVerifiedCheckFg': BG,
    'historyFileInIconFg': BG, 'historyFileInIconFgSelected': BG,
    'historyFileInRadialFg': BG, 'historyFileOutIconFg': BG,
    'historyFileOutIconFgSelected': BG, 'historyFileOutRadialFg': BG,
    'historyFileOutRadialFgSelected': BG,
    'emojiPanHeaderBg': '#0d1016f2',
    'callIconFg': BG, 'callCancelFg': BG, 'callBarFg': BG,
    'callBarBgMuted': SECONDARY,
    'mediaviewTransparentBg': SURFACE, 'mediaviewTransparentFg': RAISED,
}
assert set(overrides) <= set(palette), set(overrides) - set(palette)
palette.update(overrides)

# Resolve every alias to verify the complete palette before importing it.
def resolve(key, seen=()):
    assert key not in seen, (key, seen)
    value = palette[key]
    if value.startswith('#'):
        assert re.fullmatch(r'#[0-9a-fA-F]{6}(?:[0-9a-fA-F]{2})?', value), (key, value)
        return value
    return resolve(value, seen + (key,))
for key in palette:
    resolve(key)

text = '// Ayu Dark Meta — adapted from allmeta.ayu-dark-meta 0.0.1.\n'
text += '// SPDX-License-Identifier: GPL-3.0-or-later\n'
text += '// Navy surfaces, warm gray text, gold accents, and Ayu syntax hues.\n'
text += '\n'.join(f'{key}: {value};' for key, value in palette.items()) + '\n'
(ROOT / 'Ayu Dark Meta.tdesktop-palette').write_text(text)

def png_solid(width, height, color):
    rgb = bytes.fromhex(color.lstrip('#'))
    raw = b''.join(b'\x00' + rgb * width for _ in range(height))
    def chunk(kind, data):
        return struct.pack('!I', len(data)) + kind + data + struct.pack('!I', zlib.crc32(kind + data) & 0xffffffff)
    return b'\x89PNG\r\n\x1a\n' + chunk(b'IHDR', struct.pack('!2I5B', width, height, 8, 2, 0, 0, 0)) + chunk(b'IDAT', zlib.compress(raw)) + chunk(b'IEND', b'')

background = png_solid(128, 128, BG)
(ROOT / 'Ayu Dark Meta background.png').write_bytes(background)
# Fixed timestamps and permissions keep the bundle reproducible.
with zipfile.ZipFile(ROOT / 'Ayu Dark Meta.tdesktop-theme', 'w') as bundle:
    for name, data in [('colors.tdesktop-theme', text.encode()), ('background.png', background)]:
        entry = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
        entry.create_system = 3
        entry.external_attr = 0o100644 << 16
        entry.compress_type = zipfile.ZIP_DEFLATED
        bundle.writestr(entry, data)

artifacts = ['Ayu Dark Meta.tdesktop-theme', 'Ayu Dark Meta.tdesktop-palette',
             'Ayu Dark Meta background.png']
(ROOT / 'SHA256SUMS').write_text(''.join(
    f'{hashlib.sha256((ROOT / name).read_bytes()).hexdigest()}  {name}\n'
    for name in artifacts
))
print(f'Generated {len(palette)} Telegram colors, the theme bundle, and checksums.')
