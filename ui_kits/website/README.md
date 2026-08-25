# MHL · 42 — Website UI Kit

Faithful recreation of **mhl42.ai**, built from the live source of the `website/` codebase. Single page: nav → hero (animated starfield + orbital system) → services grid → sample-work strip → contact form → footer.

## Files

| | |
|---|---|
| `index.html` | The site, end-to-end. Asset paths rewritten to `../../site/`. PDF download stubbed in preview. |

## What's faithful, what's flagged

- Verified: **Markup, CSS, copy, hero SVG** lifted verbatim from the live `index.html`.
- Verified: All logos, icons (`ai_security` / `training` / `agentic_ai` / `research`), and the threat-model cover are first-party files copied out of the attached `website/assets/`.
- Verified: Inter from Google Fonts, the same four-color palette (Ink, Paper, Don't-Panic Gold, plus the teal/plum/coral accents only used in the services-grid eyebrows), the same hairline-border vocabulary.
- Note: The **threat-model PDF download** is stubbed in this preview (clicking shows an alert) — production link is `assets/threat-model-openclaw-example-2026-05-04.pdf` on the real domain.
- Note: `legal.html` / `privacy.html` link out to `https://mhl42.ai` rather than to local copies.
- Note: The **contact form POST** hits `/contact` (a Cloudflare worker route on the live site). In preview it will surface a network error — that's expected.

## Reference

The canonical source is the live `website/` codebase. When iterating, edit `index.html` here and diff against that if anything drifts.
