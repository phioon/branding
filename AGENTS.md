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
- Distribution 2.0.0 uses PHIOON filenames/tokens and visual identity 1.0.
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

Before task readiness, the coordinator runs the fixed Python 3.12
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

Update `README.md`, `CHANGELOG.md`, and the relevant document under `docs/`
when behavior, release contents, or the consumer contract changes.

## Ownership and configuration

The coordinator explicitly assigns a bounded Branding writer; there is no new
standing Branding role. The existing `mishkal_webapp` role covers assigned Website
or Webapp frontend work and does not confer Branding write access. Approved
identity rules govern consumer visuals; Creative Tim discovery and local templates
guide consumer composition only. See [frontend guidance](../bknd/docs/agent-workflow.md#frontend-and-brand-guidance).
Managed `.codex/` files come from `bknd/.codex/` through the
[configuration workflow](../bknd/docs/agent-workflow.md#configuration-and-discovery).
Do not edit copies independently or overwrite conflicting custom settings.

## Initial triage

Use Astra/xhigh for independent consequential review. Ordinary triage stays
Astra/high; architecture decisions, cross-repository contract reasoning and unclear
recovery root causes require Astra/xhigh. A fixed loaded role cannot be upgraded
by a prompt: use an explicit Astra/xhigh default agent with the complete role
instructions and read-only boundaries, or report the unavailable prerequisite.
Follow the [shared model policy](../bknd/docs/model-policy.md) for dated official-guidance checks, measured trials
and reviewed model upgrades; never silently select a newly released model.


Before implementation, invoke triage (Astra/high ordinarily; Astra/xhigh for complex cases above)
for every new feature,
cross-repo change, unclear bug or consequential execution, risk, protocol,
persistent-state, recovery, workflow-authority, security or destructive-tooling
change. Uncertainty requires triage. Only narrow, obvious, non-consequential edits
may bypass it; record the reason. Small implementation tasks may still stay with
the coordinator after triage or a justified bypass.

The coordinator records and accepts a concise brief within the user's authorized
scope: source evidence/assumptions, acceptance criteria, repositories/contracts,
write owners, models/effort, checks/docs and escalation conditions. Keep routine
coordination on Sol/medium and consequential implementers on Astra/high regardless
of a cheaper recommendation. Workers follow the brief but challenge conflicting
evidence; pause affected implementation and return material discoveries for
retriage. Independent consequential review must use a different agent from the
triager and implementers and challenge both plan and diff. Triage cannot waive
existing gates. If the custom role is unavailable, use an explicitly assigned
read-only Astra agent with high for ordinary triage or xhigh for complex triage;
if the required model/effort is unavailable, report the blocker before affected implementation.

## Coordination, evidence and delivery

When independent review is required, this guide explicitly requests delegation:
the coordinator must automatically invoke a separate reviewer without asking the
user for additional confirmation. Preserve the required model/effort (Astra/xhigh
for consequential review), read-only boundaries and separation from the triager
and implementers. If a higher-priority instruction or unavailable capability
prevents delegation, report the concrete blocker and keep the task blocked; do
not substitute self-review or waive the review/readiness gates. See
[review delegation](../bknd/docs/agent-workflow.md#automatic-review-delegation).

The coordinator owns scope, acceptance criteria, shared contracts and final integration. Use a registered named task worktree for every change; preserve unrelated edits and never stash, reset, copy credentials or discard work. Start from freshly fetched `origin/main`, record each repo baseline, and use lifecycle status before editing. A different baseline needs a recorded dependency reason. Usual sibling checkouts remain clean `main`; workers have disjoint writable paths and do not update them.

Use compact handoffs: task/owner, checkout/baseline, objective/acceptance criteria, writable paths, required guides/docs, sibling revisions, checks and next action. The coordinator reads relevant context once and hands workers paths/symbols; workers still read applicable guides. Reuse investigators and omit full history by default. Keep small/tightly coupled work with the coordinator; add workers only for independent benefit. The concurrency ceiling is not a quota. Isolate shared test resources or run sequentially; designate one check owner.

Choose Sol medium for routine coordination/implementation, Terra low (builtin explorer model) for focused read-only exploration, and Astra high for consequential execution, risk, protocol, persistent-state, recovery, workflow-authority, security or destructive-tooling analysis/implementation; independently review those changes with Astra xhigh. Ultra needs explicit exceptional escalation. Do not stop unfinished requirements for budget. After repeated failed approaches, preserve evidence and escalate the blocker or request runtime evidence. Where telemetry exists, measure usage per accepted PR; do not equate tokens with billed credits or promise savings.

Reuse a check only for its unchanged exact SHA, environment and command; required CI and independent review remain required. Finish source/docs before tests and rerun only checks affected by later changes. The coordinator reviews the whole task diff against baseline. The local register/lock coordinate local work only. Workers do not publish, merge, deploy or clean up. Unless the user explicitly requests local-only work, every implementation task commits, pushes and opens/updates its registered PR; reconcile uncertainty and never force-push. Use `--regular-pr` and BLOCKED/`--ready` evidence as required; they are not GitHub protection. The user merges manually unless explicitly delegated. Publication never authorizes merge, deployment or cleanup.

Report implementation, checks, review, push/PR readiness, merge, deployment and cleanup separately at exact commits; refresh Git/GitHub facts and state unknown/not applicable. Record cross-repo compatibility/order. Do not author Django migrations or run `makemigrations`; give the user the exact task checkout, revision, environment and command and review the resulting migration history. See [agent workflow](../bknd/docs/agent-workflow.md).

## Documentation completion gate

For code, configuration, tests, examples or layout changes, read applicable guides, identify authoritative docs/sibling consumers, search affected symbols and update current contracts/examples/navigation with behavior. Preserve and label history/plans and generated/frozen artifacts; do not hide a discrepancy by rewriting a requirement. Before handoff, review the complete task diff against baseline, distinguish existing edits and safely check affected links/examples/commands. The integrator owns this across repos. Report `Documentation: Updated` with paths/checks, `None` with reviewed paths/reason, or `Pending` with missing action/evidence. Missing sibling/runtime evidence is a gap, never proof. Avoid no-op doc edits.

## Review focus

Review changed behavior, defaults, contracts, state formats, paths and commands for stale docs and siblings; shared-contract/recovery work receives explicit documentation review. Links, Markdown edits, clean worktrees and local locks do not prove semantic alignment, readiness, branch protection, integration or deployment.
