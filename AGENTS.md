# Branding repository agent guide

This repository owns PHIOON visual source assets, distribution metadata and
brand guidance. It does not own application behavior, deployment, or consumer
layout decisions. Current user scope governs; this guide does not authorize
tagging, merging, deployment, or changes in consumer repositories. Authorized
implementation follows the delivery preferences below. Start with [README](README.md),
[repository controls](docs/Repository.md) and [distribution](docs/Distribution.md).
Read applicable guides before editing sibling repositories; the umbrella guide
is not automatically loaded in a standalone clone.

## Working rules

- Preserve approved artwork geometry, clear-space frames, palette roles and
  installed-app icon treatment. Do not redraw assets without explicit approval.
- Preserve the supplied PHIOON browser favicon, app and touch icon treatment:
  white symbol on Deep Navy. This deliberately supersedes the transparent
  Mishkal Teal favicon in distribution 1.1.0.
- Keep `brand-tokens.css` side-effect free. Optional local font loading belongs
  in `font-faces.css` and consumers may choose their own loading mechanism.
- Change the web allowlist in `scripts/brand_distribution.py` deliberately.
  Consumer paths are a contract; coordinate their changes with every consumer.
- Proposed distribution 3.0.0 uses `phioon/branding` producer/lock identity and
  preserves distribution 2.0.0's PHIOON filenames/tokens and visual identity 1.0.
  The frozen 1.1.0 manifest grants only checksum-verified retirement of its old
  managed filenames during sync. Never broaden it to delete unknown files.
- Regenerate both manifests after release-file changes, then run the complete
  verification commands below. `Asset-Manifest.json` intentionally excludes
  itself, and `Web-Distribution.json` is not self-hashed.
- Font binaries must retain the matching bundled SIL Open Font License files.
  Never place credentials or private consumer data in this repository.
- Preserve unrelated work. Do not hand-edit generated checksums, discard user
  changes, or claim that source checks establish deployed consumer state.

## Required checks

For Branding source or consumer-contract changes, run the applicable Python 3.12
checks below. Run the full set for distribution behavior; for documentation or
instruction-only edits, run relevant source/manifest checks and `git diff --check`.
These checks do not establish visual approval or a consumer release.

```sh
python3 scripts/brand_distribution.py generate --check
python3 scripts/brand_distribution.py check-source
python3 -m unittest discover -s tests -v
```

Update the affected `_docs` guidance when behavior, release contents or consumer
contracts change. Existing local guides/changelog remain migration debt; retain
release metadata consumed by tools with its concrete consumer justification.

## Ownership and configuration

Branding owns source assets, distribution metadata and identity rules. Consumer
repositories own layout and composition; approved identity rules govern how they
use assets. See [frontend guidance](../bknd/docs/agent-workflow.md#frontend-and-brand-guidance).
Agent profiles are no longer distributed from Backend. Preserve unrelated
client configuration; Vibe governs task-specific delegation.


Branding's asset manifest hashes governance and stable managed `.codex` files too.
Only the exact root `.codex/config.toml` and local `AGENTS.override.md` are excluded. Regenerate the
manifest after stable-source edits. Workflow documentation does not imply a brand
version, artwork or consumer-pin change.

## Commands

Use the source/manifest and distribution checks in **Required checks** above.

## Shared Vibe workflow

This repository inherits common Vibe instructions from the PHIOON umbrella.
Explicitly read the umbrella's `AGENTS.md` and `.codex/delegation-brief.md` before
Vibe task work. Codex does not automatically load guidance above a Git root.
For the primary checkout, the umbrella is its parent. In a linked worktree, use
`git rev-parse --path-format=absolute --git-common-dir` to locate the primary
checkout's `.git` directory, then its parent workspace; do not use the temporary
worktree's parent. If the expected shared files are unavailable, report the gap
before dependent workflow actions; do not silently substitute an older local copy.

The umbrella owns shared lifecycle, cleanup, delegation and security procedures.
Those instructions supersede older Vibe procedure copies in this repository and
linked workflow pages. Repository-specific product rules, tests, documentation
ownership, publication authority and explicit user constraints remain binding.
Read this checkout's `.codex/vibe-workflow.toml` for its own preferences and
opt-outs. Inheritance does not enable worker selection or local model routing,
copy umbrella settings, approve hooks, or change model/provider/authentication.
Keep hook commands and scripts local. Resolve declarations from the guard's
actual harness root: standalone repository chats keep their own declaration root;
umbrella chats use the umbrella guard's root. Shared policy is not shared runtime
ownership. Preserve running workers and other tasks' worktrees.

## Documentation and delivery

Follow the [documentation policy](https://github.com/phioon/_docs/blob/main/handbook/engineering/agents-and-workflow/documentation-policy.md).
Private canonical prose belongs in `_docs` (`handbook`, `work`, `records`,
`templates`); keep existing contracts until reviewed migration. Public product
docs retain their own authority. Before delivery, report `Documentation: Updated`,
reviewed `None`, or `Pending`, with paths/source revisions and an independent
semantic check. Do not put private evidence in public PRs.

The coordinator has standing authorization to commit reviewed work, push a task
branch and create/update its PR after applicable local checks and required review.
Task-specific limits prevail; stage only intended files. Use `[READY]` and non-draft
state only when required local/CI checks, review and docs pass at the current head.
Otherwise use `[BLOCKED]` and draft with a concrete resolution. Failed local checks
or incomplete review block initial publication unless the user requests an early
draft. Record companion PRs and exact revisions. The user merges manually; do not
merge, enable auto-merge, deploy or clean up unrelated resources.
