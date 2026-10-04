# Branding repository agent guide

This repository owns PHIOON visual source assets, distribution metadata and
brand guidance. It does not own application behavior, deployment, or consumer
layout decisions. Current user scope governs; this guide does not authorize
tagging, merging, deployment, or changes in consumer repositories. Authorized
implementation follows the task-publication gates below. Start with [README](README.md),
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

For every Branding task, the coordinator runs the full Python 3.12
[Branding local profile](../bknd/docs/agent-workflow.md#branding-local-verification)
with `verify-local --repo branding` at the final clean committed task HEAD.
It executes all three commands below and records generated identity-bound evidence;
manual command output or tested notes cannot replace it. GitHub Actions is retired.
Manifest/source checks do not establish visual approval or a consumer release.

```sh
python3 scripts/brand_distribution.py generate --check
python3 scripts/brand_distribution.py check-source
python3 -m unittest discover -s tests -v
```

Update the affected `_docs` guidance when behavior, release contents or consumer
contracts change. Existing local guides/changelog remain migration debt; retain
release metadata consumed by tools with its concrete consumer justification.

## Ownership and configuration

The coordinator explicitly assigns a bounded Branding writer; there is no new
standing Branding role. The existing `phioon_webapp` role covers assigned Website,
Webapp or Admin web work and does not confer Branding write access. Approved
identity rules govern consumer visuals; Creative Tim discovery and local templates
guide consumer composition only. See [frontend guidance](../bknd/docs/agent-workflow.md#frontend-and-brand-guidance).
Managed `.codex/` files come from `bknd/.codex/` through the
[configuration workflow](../bknd/docs/agent-workflow.md#configuration-and-discovery).
Do not edit copies independently or overwrite conflicting custom settings.


Branding always retains its complete profile: the asset manifest hashes governance
and managed `.codex` files too. Regenerate it after those edits; the sibling
instruction-only lightweight route does not apply here. No brand version, artwork
or consumer-pin change follows from workflow maintenance.

## Shared delivery checklist

Follow [proportionate delivery](https://github.com/phioon/_docs/blob/main/handbook/engineering/agents-and-workflow/proportionate-delivery.md)
for routing, finite acceptance, check selection and stopping conditions. It owns
those decisions; local check/design pages retain their command and evidence mechanics.

- Routine, reversible, understood work within an accepted design may proceed on
  Sol/medium with a concise coordinator rationale, without specialist triage or
  heavy code review. A new feature or another repository alone is not a risk trigger.
- Consequential execution, risk, financial/statistical methods, protocol, security/
  authorization, persistent state, recovery, workflow authority, destructive tooling
  or material uncertainty require Astra/high triage (xhigh for complex reasoning),
  Astra/high implementation and separate Astra/xhigh review. Automatically delegate
  required review to an agent distinct from triager and implementers; unavailable
  capability blocks that gate. Keep approved model IDs; do not browse releases per task.
- Accept a bounded brief with observable acceptance and the minimum sufficient
  evidence. A blocker needs a concrete failure trigger and material impact or an
  unmet mandatory gate. Keep optional improvements separate. Small corrections
  inside the brief need affected-delta review, not a full planning restart.
- Use a registered task/owner, named task worktree and fresh recorded baseline.
  Preserve others' work; never stash, reset, copy credentials or force-push.
  Keep independent work in disjoint paths and designate one check owner.
- Finish source/docs before final checks. The coordinator runs generated
  `verify-local` evidence at the final clean committed HEAD; reuse evidence only
  while its exact SHA, helper, owner, environment and command bindings remain valid.
  Required application/runtime checks and hosted CI remain required.
- Review affected documentation semantically, including a short independent review
  for routine work. Update owning `_docs` pages or record a specific reviewed
  `none` rationale with exact references/targets through the lifecycle. Report
  Documentation: Updated, None or Pending. Preserve historical evidence and existing
  local authority until reviewed migration; do not create routine task journals.
- The coordinator alone stages reviewed changes, uses lifecycle `commit` with
  Phi Codex author/committer, and `publish` with the pinned App and verified
  `phi-codex[bot]` creator. Unless local-only is requested, publish the registered PR;
  retain BLOCKED until required evidence permits `--ready`, using `--regular-pr`
  where required. Workers never commit, publish, merge, deploy, sync or clean up.
- The user merges manually unless explicitly delegated. Publication does not
  authorize deployment or cleanup. Report stage facts at exact commits, including
  unknown/not applicable. After reported merges, the coordinator follows
  [preservation-gated closeout](https://github.com/phioon/_docs/blob/main/handbook/engineering/agents-and-workflow/task-closeout.md);
  respect retained worktrees. No guide grants production authority.
