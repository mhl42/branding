# Mostly Harmless · brand assets

Brand assets and guidelines for **Mostly Harmless** ([mhl42.ai](https://mhl42.ai)), an AI security consultancy for agentic systems. The identity is the *Element 42* tile mark in three colours (Ink, Paper, Don't-Panic Gold), set in Inter.

Open `brand-sheet.html` in a browser for a visual index of every asset with download links. Read `GUIDELINES.md` for the rules.

## What is here

```
brand-sheet.html    Visual index of every asset, with downloads
GUIDELINES.md       Voice, colour, typography, the mark, imagery, layout
tokens.css          Design tokens as CSS custom properties, plus @font-face for Inter
LICENSE             Brand assets reserved · code MIT · Inter under the SIL OFL
logos/              17 SVGs: mark, lockups, name lockup, wordmark · light / dark / mono
icons/              App icons and favicons (SVG)
social/             OG image, LinkedIn banner, X header, email signature, avatar (SVG)
illustrations/      Editorial line illustrations used on the website (JPG)
fonts/              Inter .woff2 · 400 / 500 / 700 / 800
png/                Raster exports of logos, icons and social assets at practical sizes
```

SVG is canonical. Text in every SVG is outlined to paths, so the files render identically without the font installed. Use the PNGs only where a tool cannot take SVG.

## Quick picks

| Use | File |
|---|---|
| Website favicon | `icons/favicon.svg` |
| GitHub or app avatar | `png/social/avatar-square-512-512.png` |
| LinkedIn cover | `png/social/linkedin-banner-1584x396-1584.png` |
| X header | `png/social/x-header-1500x500-1500.png` |
| Deck cover | `logos/07-lockup-horizontal-light.svg` |
| Email signature | `png/social/email-signature-600x180-1200.png` |
| Open Graph share image | `png/social/og-image-1200x630-1200.png` |
| Starting a new build | `tokens.css` and `fonts/` |

## Using the tokens

`tokens.css` declares the colour, type, spacing, radius and motion tokens on `:root`, wires up Inter with `@font-face`, and sets base element styles. Either link it directly or paste the `:root` block into your own stylesheet. The font paths are relative, so keep `fonts/` next to it or adjust the URLs.

```html
<link rel="stylesheet" href="tokens.css">
```

## License

Short version, full terms in [`LICENSE`](./LICENSE):

- **Brand assets** (the mark, wordmark, the name "Mostly Harmless" and everything derived from them) are © Beyer Ventures, S.L. and reserved. You may reference them editorially. You may not use them to represent another entity, product or service.
- **Code** (`brand-sheet.html`, `tokens.css`) is MIT licensed.
- **Inter** is © The Inter Project Authors, SIL Open Font License 1.1.

Questions about permitted use, partnerships or trademark matters: info@mhl42.ai
