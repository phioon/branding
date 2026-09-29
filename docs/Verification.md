# Verification record: PHIOON identity 1.0 / proposed distribution 3.0.0

23 September 2026. The artwork checks below are the supplied identity author's
record, preserved from input commit `a2154f5128b3715162a61d1ebc78b11c44d55c71`;
they are not a claim that release tooling re-rendered the PDF or repeated the
author's visual approval.

- 22 SVGs parsed successfully. No raster images or live text are embedded in the logo masters.
- All eight original PHIOON outline path strings are preserved exactly in every word-bearing SVG. Scaling and placement are uniform, without distorting letter proportions.
- 22 matching PNG exports have the expected dimensions; background-free versions retain alpha transparency.
- Square icon dimensions verified at all ten supplied sizes. ICO frames match the individual supplied PNGs exactly.
- Manifest icon paths resolve.
- The 11-page PDF was rendered and visually reviewed. Text bounds checked; obsolete lowercase, split-k and old logo-size references removed.
- Horizontal color/white proofs inspected from 160 to 320 px; 220 px chosen as a conservative minimum. Wordmark and stacked proofs inspected at 170 and 220 px. Optical symbol proofs inspected from 16 px.
- Font licenses retained from the prior kit.

These checks cover supplied digital artwork, not deployment in the live site, physical printing, signage, embroidery or platform-specific app-store masking.

## Distribution verification

The release retains the supplied SVG, PNG, icon, font, geometry and PDF bytes.
The browser favicon intentionally uses the supplied white-on-Deep-Navy design.
Semantic tokens have no font-loading side effects; optional local font loading
remains in `font-faces.css`. All fonts and matching SIL licenses are present
outside the legacy archive. The generated manifests identify distribution
3.0.0 and visual identity 1.0 with canonical producer/lock identity
`phioon/branding`. The 3.0.0 preparation preserves every distributed asset byte
and consumer destination path from 2.0.0, the artwork source revision and frozen
1.1.0 manifest. Website/Webapp verifier and lock adoption remains pending in
separate consumer tasks; no tag or release is established by these source checks.

Run after all source/docs/test changes:

```sh
python3 scripts/brand_distribution.py generate
python3 scripts/brand_distribution.py generate --check
python3 scripts/brand_distribution.py check-source
python3 -m unittest discover -s tests -v
```

Tests cover deterministic manifests, licensed fonts, side-effect-free tokens,
idempotent sync, canonical provenance, exact committed locks, rejection of other
repository identities, read-only checking, legacy filename
retirement and refusal of modified/unknown legacy entries, symlinks and invalid
topology before any write. Legacy migration uses a frozen checksummed allowlist,
never the removed archive folder.

Before READY, the coordinator must run the fixed Python 3.12 local profile at
the clean committed final task HEAD as described in [Repository](Repository.md).
Manual development checks do not replace that identity-bound evidence.
Consumer source, build, runtime and deployed-state verification remain separate.
