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

## Codex workflow

Read the [current Codex workflow](https://github.com/phioon/_docs/blob/main/handbook/engineering/agents-and-workflow/codex-workflow.md)
before nontrivial work; in the umbrella, use the local `_docs` copy. It maps
[Vibe Prompt 12](https://github.com/soumatheusgomes/vibe-coding-toolkit/blob/790a895304e0c08b70a5b215c9d334f1c86b816c/docs/prompts/12-existing-project-setup.md)
to the [Codex guide](https://github.com/soumatheusgomes/vibe-coding-toolkit/blob/790a895304e0c08b70a5b215c9d334f1c86b816c/docs/tools/15-codex-workflow.md),
shared agreements and subagent policy. The Claude onboarding playbook is not the
Codex integration specification. Read applicable local skills explicitly when the
umbrella does not advertise them; a standalone repository does not inherit its
parent workspace instructions.

Use Ponytail full and concise Caveman replies; keep persisted prose normal. Use
relevant Superpowers skills and Context7 under the user's existing authorization.
Preserve the main model, provider and authentication; choose supported subagent
capability by task and authorized policy. Graphify/Caveman LLM work preserves this
client's model/settings/authentication; use local `GRAPHIFY_BACKEND=none` when
native semantic delegation is unavailable. Do not enable a proxy or new API billing.

Read the [delegation policy](.codex/delegation-brief.md) before choosing local or
native execution. The main agent is Coordinator; each worker has an explicit role
and separate specialty. Prefer local execution only when enabled routing, existing
approval, matching assessment evidence and safe capacity permit the complete task.
Otherwise retain authorized native execution. Unknown roles are rejected; a custom,
nonempty specialty is allowed but remains **Not assessed** without matching evidence.
Role labels never select a native profile or change model, reasoning, provider,
authentication or permissions. Preserve these settings and all explicit user limits.
The [optional native display adapter](.codex/native-display.md) only fills absent
or null `agent_role`; any supplied value wins. Installing its files does not
activate it. Reuse an already qualified shared integration without adding wrappers;
actual badge delivery needs separate client evidence.

Use native subagent tools with the [bounded brief](.codex/delegation-brief.md).
Write `.codex-delegations/<task_name>.json` before spawning. Include exactly one
project-root-relative declaration pointer in the native task message; require the
child to read it and compare the declared objective, writable scope, dependencies
and checks with the assigned task. A missing, ambiguous, unsafe, unreadable or
inconsistent pointer/record blocks work. Compare trusted native task identity
with the record when available (the final component of a canonical task path);
a mismatch blocks work. When trusted identity is unavailable, continue only the
authorized declared scope and report `native identity binding unverified` in
`risks`. Do not derive identity from freeform text. Keep transient declarations
out of Git, graphs and release packages.
Give each file one writer; isolate mutable resources and serialize dependencies.
Reviewers work read-only. Confirm a failed/interrupted worker stopped before
handing over its files. The coordinator checks actual diffs and evidence.
Trusted project hooks check brief/report structure on intercepted events; they do
not create a read-only sandbox, prove findings or enforce file ownership.

Preserve user changes, security, accessibility, validation and explicit limits.
Never author Django migrations or run `makemigrations`. Run repository checks
directly. Do not invoke legacy onboarding/startup, registration, profile routing,
configuration sync, `verify-local` or Git-lifecycle tools to start/deliver a task.
Preserve legacy tools and records. Status questions do not cancel authorized work;
continue independent work around blockers and respect pauses/cancellation. Verify
checkout/process state when resuming; keep a short handoff in the existing plan.

## Vibe task lifecycle

Use the reviewed installed Vibe Setup helper at
`$HOME/.codex/skills/vibe-setup/workflow.py` and its adjacent `task-lifecycle.md`.
Resolve the installed skill's actual path if this location differs; do not copy
its helper into this repository. Normal tasks use the helper directly, without
repeating full onboarding. Read `.codex/vibe-workflow.toml`: lifecycle and cleanup
default ON; preserve independent `enabled=false` and `auto_cleanup=false` choices.

Inspect first. Unless opted out, create or adopt a linked worktree and require
`start` to return `implementation=worktree_verified` before editing. Use its
returned command and worker roots; a failed verification never permits primary
checkout edits. Preview setup with `inspect --task-id`, apply the reviewed plan,
and resume the same operation after interruption. With lifecycle disabled, use
the reviewed component installer and ordinary authorized delivery instead.

Follow the installed lifecycle contract for `sync` and `resume`, under the
repository's publication authority. Stop writers and supply explicit files plus
current checks and independent review. Plan at most four routine checkpoints or one per
phase. READY, reopen and blocker events reuse existing milestones without
consuming that budget; refreshed inputs require a fresh READY event and current
gates. PRs start draft `[BLOCKED]`; `[READY]` requires current local/remote
checks, review and non-draft status. Withdraw READY before further edits, preserve
human content, reconcile uncertain results and never auto-merge. Publication
failure means “blocked; PR update pending”, with a concrete next action.

Cleanup follows the installed lifecycle contract after observed terminal PR state.
Remote deletion and worktree removal have independent opt-outs; preserve both and
`auto_cleanup=false`. Merged tasks permit eligible cleanup; closed-unmerged tasks
retain their worktrees, while recorded supersession can permit removal. Keep local
branch refs. Verify ownership, stopped writers, clean files and remote absence
before removal when enabled. Managed worktrees require native archive preflight
and their native owner; queued archival stays pending until absence is verified.
Reuse existing cleanup and supersession operations without legacy tools or polling.
For required companion PRs, use `check-completion` with every required Vibe task
before claiming overall completion. Installation, discovery and execution remain
separate evidence.

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

## Vibe worker selection

The project owner authorized full applicable Vibe adoption on 2026-10-23, including
explicit difficulty-based worker selection. Read the installed Vibe Setup
`delegation-brief.md` and the matching project copy before delegating. The
`[worker_selection]` section in `.codex/vibe-workflow.toml` records this choice
independently of lifecycle and cleanup preferences. Do not silently fall back to
an older PHIOON inheritance-only policy.

Keep the Coordinator's model, reasoning, provider, authentication and permissions
unchanged. Classify the task's difficulty and risk; use deterministic tools or the
Coordinator when delegation adds no value. Prefer approved, assessed local models
within their exact scope and capacity. Otherwise select a qualified native model
and reasoning pair through supported controls. A full-history fork inherits
settings; explicit selection requires fresh context and supported overrides.
Record the selection reason, qualification reference, requested and observed
settings, outcomes and fallback cause privately. Availability or a successful
model-control probe does not establish task competence or savings. Missing matching
qualification retains the authorized inherited route and must be reported as a
qualification gap. This adoption does not authorize new model assessments, paid
benchmarks, providers, billing, local approvals or plugin releases.

Use the installed Vibe lifecycle and security contracts as current authority:
worktree verification, bounded publication checkpoints, independent cleanup
preferences, supersession, cross-repository completion and proportional security
validation apply under their existing gates. At each readiness, release or explicit
security gate, inspect Trail of Bits updates and bind required checks and review
to the exact snapshot. Release preflight remains required with lifecycle disabled.
Task startup does not independently trigger a security audit. Preserve manual
merging, existing product checks, user customizations and needed legacy evidence.

Before native dispatch, put the declaration at the active harness root owning the
executing hook, not whichever repository is the current command directory. Name
that root and the software worktree separately in the message; include exactly
one harness-root-relative declaration pointer. An umbrella chat uses the umbrella
root; a direct repository chat uses that repository's harness root. Verify actual
client loading and worker settings separately from installation. Keep primary
activation and requested-client qualification pending until observed.
