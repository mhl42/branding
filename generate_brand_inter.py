#!/usr/bin/env python3
"""
Mostly Harmless · MHL · 42 — brand asset generator (Inter, outlined).

Every text element is converted to vector <path> data using Inter font files,
so the SVG renders identically anywhere — no font dependency, no fallback drift.
"""
from pathlib import Path
import textwrap
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.misc.transform import Identity

# ============================================================
# Paths & tokens
# ============================================================
ROOT = Path("/sessions/gracious-confident-cannon/mnt/mostlyharmless/branding")
LOGOS = ROOT / "logos"
ICONS = ROOT / "icons"
SOCIAL = ROOT / "social"
FONT_DIR = Path("/sessions/gracious-confident-cannon/mnt/outputs/fonts")

INK = "#0E1116"
PAPER = "#FAF6EE"
GOLD = "#F5C518"

# Inter weight files
WEIGHT_FILES = {
    400: FONT_DIR / "Inter-Regular.ttf",
    500: FONT_DIR / "Inter-Medium.ttf",
    700: FONT_DIR / "Inter-Bold.ttf",
    800: FONT_DIR / "Inter-ExtraBold.ttf",
}
_FONT_CACHE = {}


def get_font(weight):
    if weight not in _FONT_CACHE:
        _FONT_CACHE[weight] = TTFont(str(WEIGHT_FILES[weight]))
    return _FONT_CACHE[weight]


def text_path(text, x, y, size, weight=400, letter_spacing=0, anchor="start", fill=INK):
    """Return an SVG <path> string equivalent to a <text> element rendered with Inter."""
    font = get_font(weight)
    cmap = font.getBestCmap()
    gset = font.getGlyphSet()
    upem = font["head"].unitsPerEm
    scale = size / upem

    # Compute advances per character
    advances = []
    glyph_names = []
    for ch in text:
        gid = cmap.get(ord(ch))
        if gid is None:
            # skip unknown — leave a half-em gap
            advances.append(size * 0.5)
            glyph_names.append(None)
            continue
        glyph_names.append(gid)
        adv = gset[gid].width * scale
        advances.append(adv)

    # Total width — letter-spacing is added between glyphs
    n = len([g for g in glyph_names if g is not None])
    total = sum(advances) + max(0, n - 1) * letter_spacing

    if anchor == "middle":
        cursor = x - total / 2
    elif anchor == "end":
        cursor = x - total
    else:
        cursor = x

    parts = []
    for i, gid in enumerate(glyph_names):
        if gid is not None:
            pen = SVGPathPen(gset)
            t = Identity.translate(cursor, y).scale(scale, -scale)
            tpen = TransformPen(pen, t)
            gset[gid].draw(tpen)
            d = pen.getCommands()
            if d:
                parts.append(d)
        cursor += advances[i] + letter_spacing

    if not parts:
        return ""
    return f'<path d="{" ".join(parts)}" fill="{fill}"/>'


# ============================================================
# Tile primitives — text replaced with text_path() calls
# ============================================================

def tile(stroke=INK, accent=GOLD, label=INK, mhl_color=None, fill="none"):
    mhl_color = mhl_color or stroke
    return "\n  ".join([
        f'<rect x="20" y="20" width="200" height="200" rx="20" fill="{fill}" stroke="{stroke}" stroke-width="6"/>',
        text_path("42", x=40, y=64, size=28, weight=700, letter_spacing=-0.5, fill=label),
        f'<circle cx="200" cy="48" r="6" fill="{accent}"/>',
        text_path("MHL", x=120, y=160, size=80, weight=800, letter_spacing=-3, anchor="middle", fill=mhl_color),
        text_path("MOSTLY HARMLESS", x=120, y=198, size=13, weight=500, letter_spacing=2.5, anchor="middle", fill=mhl_color),
    ])


def tile_no_phrase(stroke=INK, accent=GOLD, mhl_color=None, fill="none"):
    mhl_color = mhl_color or stroke
    return "\n  ".join([
        f'<rect x="20" y="20" width="200" height="200" rx="20" fill="{fill}" stroke="{stroke}" stroke-width="6"/>',
        text_path("42", x=40, y=64, size=28, weight=700, letter_spacing=-0.5, fill=mhl_color),
        f'<circle cx="200" cy="48" r="6" fill="{accent}"/>',
        text_path("MHL", x=120, y=148, size=80, weight=800, letter_spacing=-3, anchor="middle", fill=mhl_color),
    ])


def _str_width(text, size, weight, letter_spacing):
    font = get_font(weight)
    cmap = font.getBestCmap()
    gset = font.getGlyphSet()
    upem = font["head"].unitsPerEm
    scale = size / upem
    advs = [gset[cmap[ord(c)]].width * scale for c in text]
    return sum(advs) + max(0, len(advs) - 1) * letter_spacing


def wordmark_block(text_color=INK, accent=GOLD, with_phrase=True, anchor="start", x=0, y=56):
    """The 'mhl42.ai' wordmark with an accent dot, optionally with caption below."""
    base_size = 64
    ls = -2
    width_mhl42 = _str_width("mhl42", base_size, 800, ls)
    width_ai = _str_width("ai", base_size, 800, ls)
    gap_for_dot = base_size * 0.32
    full = width_mhl42 + gap_for_dot + width_ai

    # Compute the left edge of the full wordmark
    if anchor == "middle":
        left = x - full / 2
    elif anchor == "end":
        left = x - full
    else:
        left = x

    parts = []
    # Always render mhl42 left-aligned at `left`
    parts.append(text_path("mhl42", x=left, y=y, size=base_size, weight=800, letter_spacing=ls, anchor="start", fill=text_color))

    seam_x = left + width_mhl42
    dot_cx = seam_x + base_size * 0.10
    dot_cy = y - base_size * 0.10
    parts.append(f'<circle cx="{dot_cx:.2f}" cy="{dot_cy:.2f}" r="{base_size*0.07:.2f}" fill="{accent}"/>')

    ai_x = seam_x + gap_for_dot
    parts.append(text_path("ai", x=ai_x, y=y, size=base_size, weight=800, letter_spacing=ls, anchor="start", fill=text_color))

    if with_phrase:
        cap_x = (left + full / 2) if anchor == "middle" else (left + 4)
        cap_anchor = "middle" if anchor == "middle" else "start"
        parts.append(text_path("MOSTLY HARMLESS", x=cap_x, y=y + 30, size=14, weight=500, letter_spacing=3, anchor=cap_anchor, fill=text_color))

    return "\n  ".join(parts)


def svg_doc(viewbox, body, bg=None):
    bg_rect = f'<rect width="100%" height="100%" fill="{bg}"/>' if bg else ""
    return textwrap.dedent(f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="{viewbox}" preserveAspectRatio="xMidYMid meet">
  {bg_rect}
  {body}
</svg>
''').lstrip()


# ============================================================
# LOGOS
# ============================================================

(LOGOS / "01-mark-with-phrase-light.svg").write_text(svg_doc("0 0 240 240", tile()))
(LOGOS / "02-mark-with-phrase-dark.svg").write_text(svg_doc("0 0 240 240", tile(stroke=PAPER, mhl_color=PAPER, label=PAPER), bg=INK))
(LOGOS / "03-mark-no-phrase-light.svg").write_text(svg_doc("0 0 240 240", tile_no_phrase()))
(LOGOS / "04-mark-no-phrase-dark.svg").write_text(svg_doc("0 0 240 240", tile_no_phrase(stroke=PAPER, mhl_color=PAPER), bg=INK))
(LOGOS / "05-mark-mono-black.svg").write_text(svg_doc("0 0 240 240", tile_no_phrase(stroke="#000000", accent="#000000", mhl_color="#000000")))
(LOGOS / "06-mark-mono-white.svg").write_text(svg_doc("0 0 240 240", tile_no_phrase(stroke="#FFFFFF", accent="#FFFFFF", mhl_color="#FFFFFF"), bg=INK))

# Horizontal lockup
hl_light = f'<g>{tile_no_phrase()}</g>\n  <g transform="translate(280,0)">{wordmark_block(y=140)}</g>'
(LOGOS / "07-lockup-horizontal-light.svg").write_text(svg_doc("0 0 760 240", hl_light))
hl_dark = f'<g>{tile_no_phrase(stroke=PAPER, mhl_color=PAPER)}</g>\n  <g transform="translate(280,0)">{wordmark_block(text_color=PAPER, y=140)}</g>'
(LOGOS / "08-lockup-horizontal-dark.svg").write_text(svg_doc("0 0 760 240", hl_dark, bg=INK))

# Vertical lockup
def vlockup(stroke, mhl_color, text_color):
    return (
        f'<g transform="translate(80,0)">{tile_no_phrase(stroke=stroke, mhl_color=mhl_color)}</g>\n'
        f'  <g transform="translate(200,0)">{wordmark_block(text_color=text_color, anchor="middle", x=0, y=300)}</g>'
    )
(LOGOS / "09-lockup-vertical-light.svg").write_text(svg_doc("0 0 400 360", vlockup(INK, INK, INK)))
(LOGOS / "10-lockup-vertical-dark.svg").write_text(svg_doc("0 0 400 360", vlockup(PAPER, PAPER, PAPER), bg=INK))

# Wordmark variants
(LOGOS / "11-wordmark-with-phrase-light.svg").write_text(svg_doc("0 0 380 110", f'<g transform="translate(8,16)">{wordmark_block()}</g>'))
(LOGOS / "12-wordmark-with-phrase-dark.svg").write_text(svg_doc("0 0 380 110", f'<g transform="translate(8,16)">{wordmark_block(text_color=PAPER)}</g>', bg=INK))
(LOGOS / "13-wordmark-no-phrase-light.svg").write_text(svg_doc("0 0 380 80", f'<g transform="translate(8,16)">{wordmark_block(with_phrase=False)}</g>'))
(LOGOS / "14-wordmark-no-phrase-dark.svg").write_text(svg_doc("0 0 380 80", f'<g transform="translate(8,16)">{wordmark_block(text_color=PAPER, with_phrase=False)}</g>', bg=INK))

# ============================================================
# ICONS
# ============================================================

def app_icon(bg_fill, mark_color, accent, num_color):
    return f'''
  <rect width="512" height="512" rx="112" fill="{bg_fill}"/>
  <g transform="translate(56,56) scale(1.667)">
    <rect x="20" y="20" width="200" height="200" rx="20" fill="none" stroke="{mark_color}" stroke-width="8"/>
    {text_path("42", x=40, y=64, size=28, weight=700, letter_spacing=-0.5, fill=num_color)}
    <circle cx="200" cy="48" r="7" fill="{accent}"/>
    {text_path("MHL", x=120, y=148, size=80, weight=800, letter_spacing=-3, anchor="middle", fill=mark_color)}
  </g>
'''.strip()

(ICONS / "app-icon-gold-512.svg").write_text(svg_doc("0 0 512 512", app_icon(GOLD, INK, INK, INK)))
(ICONS / "app-icon-ink-512.svg").write_text(svg_doc("0 0 512 512", app_icon(INK, PAPER, GOLD, PAPER)))

# Favicon — minimal MHL + dot
def favicon(stroke=None, fill_bg=None, text_color=PAPER, accent=GOLD):
    bg = f'<rect x="0" y="0" width="64" height="64" rx="11" fill="{fill_bg}"/>' if fill_bg else \
         f'<rect x="2" y="2" width="60" height="60" rx="10" fill="none" stroke="{stroke}" stroke-width="3"/>'
    return f'''
  {bg}
  <circle cx="52" cy="14" r="4" fill="{accent}"/>
  {text_path("MHL", x=32, y=44, size=22, weight=800, letter_spacing=-1, anchor="middle", fill=text_color)}
'''.strip()

(ICONS / "favicon.svg").write_text(svg_doc("0 0 64 64", favicon(fill_bg=INK)))
(ICONS / "favicon-light.svg").write_text(svg_doc("0 0 64 64", favicon(stroke=INK, text_color=INK)))

# ============================================================
# SOCIAL BANNERS
# ============================================================

# OG image — 1200x630
og = f'''
  <defs>
    <pattern id="dots" width="24" height="24" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1.2" fill="rgba(14,17,22,0.07)"/>
    </pattern>
  </defs>
  <rect width="1200" height="630" fill="url(#dots)"/>
  <g transform="translate(80,135) scale(1.6)">
    {tile_no_phrase()}
  </g>
  <g>
    {text_path("Mostly Harmless", x=490, y=240, size=68, weight=800, letter_spacing=-2, fill=INK)}
    {text_path("AI security · agents · safety · studio", x=490, y=292, size=26, weight=500, letter_spacing=-0.3, fill=INK)}
    <line x1="490" y1="332" x2="570" y2="332" stroke="{GOLD}" stroke-width="6"/>
    {text_path("mhl42.ai", x=490, y=372, size=24, weight=700, letter_spacing=2, fill=INK)}
  </g>
'''
(SOCIAL / "og-image-1200x630.svg").write_text(svg_doc("0 0 1200 630", og, bg=PAPER))

# LinkedIn banner — 1584x396
li = f'''
  <defs>
    <linearGradient id="lg" x1="0" x2="1" y1="0" y2="0">
      <stop offset="0" stop-color="{INK}"/>
      <stop offset="1" stop-color="#1A1F28"/>
    </linearGradient>
  </defs>
  <rect width="1584" height="396" fill="url(#lg)"/>
  <line x1="0" y1="380" x2="1584" y2="380" stroke="{GOLD}" stroke-width="4"/>
  <g transform="translate(80,78)">
    {tile_no_phrase(stroke=PAPER, mhl_color=PAPER)}
  </g>
  <g>
    {text_path("Mostly Harmless", x=360, y=170, size=62, weight=800, letter_spacing=-1.5, fill=PAPER)}
    {text_path("AI security consulting · agentic AI · education · safety · intelligent apps", x=360, y=214, size=24, weight=500, letter_spacing=-0.3, fill=PAPER)}
    {text_path("mhl42.ai", x=360, y=262, size=20, weight=700, letter_spacing=2.5, fill=GOLD)}
  </g>
'''
(SOCIAL / "linkedin-banner-1584x396.svg").write_text(svg_doc("0 0 1584 396", li))

# X header — 1500x500
xh = f'''
  <defs>
    <pattern id="xdots" width="22" height="22" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1.1" fill="rgba(250,246,238,0.08)"/>
    </pattern>
  </defs>
  <rect width="1500" height="500" fill="{INK}"/>
  <rect width="1500" height="500" fill="url(#xdots)"/>
  <rect x="0" y="0" width="14" height="500" fill="{GOLD}"/>
  <g transform="translate(120,140)">
    {tile_no_phrase(stroke=PAPER, mhl_color=PAPER)}
  </g>
  <g>
    {text_path("Mostly Harmless", x=420, y=236, size=76, weight=800, letter_spacing=-2, fill=PAPER)}
    {text_path("an AI lab & studio — agents, security, safety, training", x=420, y=286, size=28, weight=500, letter_spacing=-0.3, fill=PAPER)}
    {text_path("mhl42.ai", x=420, y=340, size=22, weight=700, letter_spacing=2.5, fill=GOLD)}
  </g>
'''
(SOCIAL / "x-header-1500x500.svg").write_text(svg_doc("0 0 1500 500", xh))

# Email signature — 600x180
sig = f'''
  <rect width="600" height="180" fill="{PAPER}"/>
  <line x1="20" y1="20" x2="20" y2="160" stroke="{GOLD}" stroke-width="4"/>
  <g transform="translate(40,10) scale(0.55)">
    {tile_no_phrase()}
  </g>
  <g>
    {text_path("Stefan Beyer", x=180, y=68, size=22, weight=800, letter_spacing=-0.5, fill=INK)}
    {text_path("Mostly Harmless · AI Lab & Studio", x=180, y=90, size=14, weight=500, fill=INK)}
    {text_path("mhl42.ai", x=180, y=116, size=13, weight=700, letter_spacing=2, fill=GOLD)}
    {text_path("stefan@mhl42.ai", x=300, y=116, size=13, weight=500, letter_spacing=0.5, fill=INK)}
  </g>
'''
(SOCIAL / "email-signature-600x180.svg").write_text(svg_doc("0 0 600 180", sig))

# Square avatar — uses ink app icon
(SOCIAL / "avatar-square-512.svg").write_text(svg_doc("0 0 512 512", app_icon(INK, PAPER, GOLD, PAPER)))

print("Done.")
print(f"  Logos: {len(list(LOGOS.glob('*.svg')))}")
print(f"  Icons: {len(list(ICONS.glob('*.svg')))}")
print(f"  Social: {len(list(SOCIAL.glob('*.svg')))}")
