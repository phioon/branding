# PHIOON visual identity 1.0 / proposed web distribution 3.0.0

Refined from the selected **01 — Original, preserved** direction, 23 September 2026.

## Start here

- **PHIOON-Identity-Preview.png**: the final horizontal logo in color and white.
- **PHIOON-Website-Preview.png**: an illustrative placement in the current website style.
- **PHIOON-Brand-Guide-v1.pdf**: the updated 11-page brand guide.
- **svg/phioon-horizontal-color.svg**: the primary vector master.

## What changed

The original PHIOON letterforms, thin weight, circular cut O shapes and internal letter spacing are preserved as vector paths. No font substitution or outline thickening was applied.

The Portfolio Weave is now approximately the same height as the capitals: 185.64 design units beside a 184-unit wordmark. This reduces the symbol by approximately 11.4% relative to the selected study. The gap increased from 84.36 to 92 design units, approximately half the capital height. Both shapes are vertically centered by their outline bounds.

The primary color logo combines deep teal #007F78, ink #10252B and the historical petrol-blue O accent #3A5966. White, ink and pure-black variants are included. Supporting colors and fonts continue the preceding brand system.

## Package

| Folder | Contents |
|---|---|
| svg | 22 outlined SVG assets: horizontal, stacked, wordmark, symbol and optical small symbol in color/ink/black/white; plus two named background variants |
| png | Matching exports, 1800 px wide for lockups and wordmarks; 512 px for symbols |
| icons | Square icons from 16 to 512 px, SVG favicon, four-size ICO, app icon SVG and manifest |
| fonts | Manrope variable and IBM Plex Mono regular/medium, with original licenses |
| docs | Placement instructions, verification notes and digital size proofs |

`brand-tokens.css` contains side-effect-free supporting type and color tokens
under `--phioon-*`; it never loads fonts. Optional `font-faces.css` loads the
bundled local fonts and is excluded from the web allowlist. Consumers may use
their own font loader. `geometry.json` records the outlines and placement
dimensions. `Asset-Manifest.json` lists release files and checksums;
`Web-Distribution.json` defines the approved consumer subset.

Read [AGENTS.md](AGENTS.md), [repository controls](docs/Repository.md),
[distribution](docs/Distribution.md), [implementation](docs/Implementation.md)
and [verification](docs/Verification.md) before integrating the release.

## Sizes and spacing

Minimum digital widths refer to the complete supplied canvas:

- Horizontal: **220 px minimum**, 240–280 px preferred; the website preview uses 260 px.
- Wordmark: **170 px minimum**.
- Stacked: **220 px minimum**.
- App icon: **16 px minimum**; use the optical variant below 48 px.

The horizontal canvas is approximately 1493.153 × 265.64 units. Its built-in clear space is 40 units on each side. Preserve the viewBox and proportions. Do not crop away the padding.

Physical print starting sizes are 45 mm horizontal, 35 mm stacked and 10 mm symbol. These require a physical proof. Web colors are sRGB; no press-specific CMYK or Pantone match is claimed.

## Scope

The selected identity is implemented in the supplied files. Supporting typography,
brand principles and the optional line “Trade with clarity. Live in balance.”
are carried forward from the previous guide; the line remains an editorial option.
This repository provides source assets, not evidence of a deployed consumer.
The PHIOON artwork is preserved byte-for-byte from user input revision
`a2154f5128b3715162a61d1ebc78b11c44d55c71`. The legacy kit remains in Git history;
this release has no runtime, build or verification dependency on `mishkal/`.

The wordmark comes from the supplied original PHIOON vector PDF. The weave comes from the existing approved identity. Only arrangement and size changed in the main logo.

## Web consumer upgrade

Distribution 2.0.0 intentionally changes asset filenames, CSS token names,
minimum logo sizes and browser favicon treatment. Browser/app/touch icons now
use the supplied white-on-Deep-Navy treatment. Website and Webapp must update
their own text, metadata, layouts and asset references alongside the assets.
Proposed distribution 3.0.0 changes generated provenance and consumer-lock
repository identity to `phioon/branding`. It preserves distribution 2.0.0's
artwork bytes, managed asset paths and schema 1. The identity change requires
consumer verifier updates before adoption; Website and Webapp adoption remains
pending in separate tasks. This source preparation does not create a tag or release.

From a clean committed Branding release:

```sh
python3 scripts/brand_distribution.py sync --consumer-root ../webapp
python3 scripts/brand_distribution.py check-consumer --consumer-root ../webapp
```

Sync writes the exact source revision into `brand.lock.json`. It can migrate the
approved 1.1.0 lock by retiring only unchanged, allowlisted old filenames; unknown,
modified or symlinked legacy entries fail before writes. Consumer-owned
`public/brand/SOURCE.md` is preserved. Review the generated assets and lock
together. See [the migration contract](docs/Distribution.md#migration-from-110).

The coordinator runs Python 3.12 local verification at the final clean committed
HEAD through the registered lifecycle. Source checks do not establish visual
approval, consumer integration or deployment.
