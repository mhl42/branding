# MHL · 42 — Presentation rules

Captured from real corrections on shipped decks. The general design rules in
`README.md` always apply; these add the deck-specific tightening that came up
in review.

## Colour & contrast

- **Never put Paper text on Gold.** Gold is an accent surface — text on Gold is
  always Ink.
- **Never put Paper on Paper, or Ink on Ink.** When a card inverts to Ink in
  dark mode, flip *every* descendant: body, list markers, em/strong, captions,
  chips, code.
- **`<strong>` / `<em>` inherit the card colour**, not the page default. If you
  override one, override the other.
- Body text on Ink is `rgba(250, 246, 238, .82)`, not pure Paper. Headings only
  go to full Paper.

## Decorative dot motif

- The gold dot lives in **card chrome** — top-right of tiles, threat tiles,
  channel tiles, code blocks. It does **not** sit over typography.
- One dot per card. **No dot on the threat divider's big numerals** — the
  numeral is the graphic.
- If a dot would land within 16px of a glyph, drop it.

## Logo / lockup

- **One lockup per slide.** The cover carries either the wordmark or the
  periodic tile, never both.
- Ship `lockup-light.svg` + `lockup-dark.svg` as a pair. Switch with CSS on
  `body[data-theme]`. **Never** recolour the SVG via `filter: invert()`.
- The periodic tile in SVG uses `currentColor` for stroke and glyphs so it
  inverts with the theme automatically. Gold accent stays as `var(--gold)`.

## Imagery

- Hardware / product photography: `aspect-ratio: 16/9` + `object-fit: contain`
  against an Ink panel. **Never** crop product photos with `cover`.
- Avatar / portrait crops: `object-fit: cover` is fine; frame with a 3px Ink
  border and a 6px Gold offset.

## QR codes

- QR is a **static asset**, not runtime-generated. Inline SVG.
- Paper background, Ink foreground. The URL is captioned below the code in
  mono, uppercase tracking.
- Border-radius on the wrap, not on the QR itself.

## Tweaks panel (when present)

- Square corners, hairline Ink frame, **8px hard offset shadow** in Ink (Gold
  in dark). No glass / no blur.
- Header is an Ink strip with a gold dot. Section labels use the gold bar +
  uppercase + `0.22em` tracking treatment.
- Segmented controls have Gold thumbs; selected text stays Ink on Gold.
- Inverts on `body[data-theme="dark"]` — no separate panel theme.

## Type scale floors (1920 × 1080)

- Body minimum **24px**, eyebrow minimum **22px**.
- Stat numerals stay **80 – 96px** — never shrink to fit. Re-flow the layout
  instead.
- `text-wrap: pretty` on every paragraph. `letter-spacing: -0.02em` on titles
  ≥ 56px.

## Authoring

- Slides are **static HTML** inside `<deck-stage>`. Don't loop slides from a JS
  array — it kills direct edit.
- Sizing via CSS custom properties in `<style>`, not JS constants.
- Speaker notes only when explicitly requested.
