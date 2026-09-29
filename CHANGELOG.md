# Changelog

## 3.0.0 - Proposed

- Change generated provenance and new consumer locks to canonical repository
  identity `phioon/branding`. This incompatible verifier contract requires a
  major distribution version; visual identity remains 1.0 and schema remains 1.
- Preserve all distributed artwork/font/token bytes, destination paths, artwork
  source revision and the frozen 1.1.0 retirement manifest. Historical 2.0.0
  distributions are unchanged; the old identity remains accepted only for
  checksum-verified 1.1.0 filename retirement.
- Website/Webapp verifier and lock adoption remains separately pending. Source
  preparation does not create a tag/release or sync/deploy consumers.

## 2.0.0 - 2026-09-23

- Adopt supplied PHIOON visual identity 1.0 without altering artwork bytes.
  Replace Mishkal asset filenames and CSS tokens with PHIOON names; minimum
  horizontal/wordmark widths are 220/170 px, with built-in clear space retained.
- Adopt supplied white-on-Deep-Navy browser favicons, app and touch icons.
- Keep tokens side-effect-free and optional font loading in `font-faces.css`.
  Include all supporting fonts and SIL licenses independently of the legacy kit.
- Regenerate deterministic manifests and add narrowly scoped 1.1.0 consumer
  migration: validate the legacy lock, topology and old-file checksums before
  writing, retire only approved unchanged old filenames, preserve unknown files
  by failing preflight, and retain read-only strict consumer verification.
- Keep the legacy distribution manifest as frozen migration metadata. The old
  artwork remains in Git history and is not required by this release.

## Unreleased

- Add the canonical `phioon_*` Codex roles while retaining bounded `mishkal_*`
  aliases for mixed-version clients. Update the managed defaults header and
  repository guidance; artwork, brand version and web distribution are unchanged.

- Replace `brand-kit` GitHub Actions with coordinator-run Python 3.12 manifest,
  source and distribution checks at the final clean task commit. Preserve review
  and other protection-template controls; remote configuration is separate.
  Regenerate governance inventory without changing artwork, version, web
  distribution or consumer locks. This supersedes the hosted CI policy below.

- Synchronize the reviewer xhigh trial and conditional complex-triage guidance;
  retain explicit approved models and reviewed future upgrades. Regenerate the
  governance inventory without changing brand version, artwork or web distribution.

- Document public, exact-revision consumer acquisition and remove the obsolete
  private-repository credential requirement. This changes no artwork, release
  version, web distribution or consumer lock.

- Cancel superseded CI runs within the same pull request and add a provisional
  10-minute `brand-kit` timeout. Keep all checks and `main` runs; document usage
  reporting and regenerate the full inventory without changing brand assets,
  release version or the web distribution.

- Align standalone triage, review, task publication and documentation gates with
  the six-repository workflow; clarify Branding and frontend ownership and
  managed Codex configuration. Artwork, version and web distribution are unchanged.

## 1.1.0 - 2026-09-20

- Adopt the approved transparent Mishkal Teal browser favicons from webapp
  revision `65f7a3374e3b60c326692a6d05a680eff38a5a36`; installed-app and touch
  icons remain white-on-Navy.
- Add a deterministic, checksummed web distribution and consumer sync/check
  tool that preflights all manifest paths and consumer topology before writing,
  rejects root/managed-path symlinks and unsupported or misplaced entries, and
  refuses extras without traversing extra directories or deleting entries.
  Invalid paths or topology leave the whole consumer tree unchanged; regular
  missing/tampered files remain repairable and matching files retain mtimes.
- Generate a deterministic consumer `brand.lock.json` binding version, exact
  committed Branding source and web-manifest checksum; validate it in read-only
  consumer CI and reject dirty/uncommitted source identities.
- Separate semantic design tokens from optional local `@font-face`
  declarations.
- Correct the canonical PDF and identity-preview filenames.
- Add repository guidance, automated verification, and a proposed repository
  `main` protection payload.

## 1.0.0 - 2026-09-19

- Initial production kit for the approved A1.2 / Light direction.
