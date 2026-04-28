#!/usr/bin/env python3
"""Render every SVG in /branding to PNG at sensible sizes."""
from pathlib import Path
import cairosvg

ROOT = Path("/sessions/gracious-confident-cannon/mnt/mostlyharmless/branding")
PNG_OUT = ROOT / "png"
PNG_OUT.mkdir(exist_ok=True)

# SVG path -> output PNG width(s) in px. Aspect is preserved.
RENDER_LIST = [
    # Logos — render at 1024 wide for hi-res use
    ("logos/01-mark-with-phrase-light.svg", [1024, 256]),
    ("logos/02-mark-with-phrase-dark.svg",  [1024, 256]),
    ("logos/03-mark-no-phrase-light.svg",   [1024, 256]),
    ("logos/04-mark-no-phrase-dark.svg",    [1024, 256]),
    ("logos/05-mark-mono-black.svg",        [1024]),
    ("logos/06-mark-mono-white.svg",        [1024]),
    ("logos/07-lockup-horizontal-light.svg",[2000]),
    ("logos/08-lockup-horizontal-dark.svg", [2000]),
    ("logos/09-lockup-vertical-light.svg",  [1200]),
    ("logos/10-lockup-vertical-dark.svg",   [1200]),
    ("logos/11-wordmark-with-phrase-light.svg",[1200]),
    ("logos/12-wordmark-with-phrase-dark.svg", [1200]),
    ("logos/13-wordmark-no-phrase-light.svg",  [1200]),
    ("logos/14-wordmark-no-phrase-dark.svg",   [1200]),
    # Icons
    ("icons/app-icon-gold-512.svg", [1024, 512, 256]),
    ("icons/app-icon-ink-512.svg",  [1024, 512, 256]),
    ("icons/favicon.svg",           [192, 64, 32, 16]),
    ("icons/favicon-light.svg",     [192, 64, 32, 16]),
    # Social — at native size + 2x for retina
    ("social/og-image-1200x630.svg",       [1200, 2400]),
    ("social/linkedin-banner-1584x396.svg",[1584]),
    ("social/x-header-1500x500.svg",       [1500]),
    ("social/email-signature-600x180.svg", [600, 1200]),
    ("social/avatar-square-512.svg",       [512, 1024]),
]

for rel, widths in RENDER_LIST:
    src = ROOT / rel
    if not src.exists():
        print(f"MISSING: {rel}")
        continue
    stem = src.stem
    sub = src.parent.name  # logos / icons / social
    out_dir = PNG_OUT / sub
    out_dir.mkdir(exist_ok=True)
    for w in widths:
        out = out_dir / f"{stem}-{w}.png"
        cairosvg.svg2png(url=str(src), write_to=str(out), output_width=w)
        print(f"  -> {out.relative_to(ROOT)}")

print("Done.")
