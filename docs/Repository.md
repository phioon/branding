# Repository controls

The proposed source release is PHIOON visual identity 1.0 / web distribution 3.0.0.
The incompatible consumer upgrade is governed by [Distribution](Distribution.md).
Artwork and fonts are self-contained at the root; no script, build or check may
depend on the optional legacy `mishkal/` archive. The frozen 1.1.0 manifest under
`scripts/` is retained solely to validate retirement of old consumer filenames.
Generated provenance and new locks use the canonical repository `phioon/branding`.
Distribution 2.0.0 remains immutable history. The proposed 3.0.0 contract changes
producer identity only; consumer verifier and lock adoption are separate pending
Website/Webapp tasks. No tag or release is created by source preparation.

[AGENTS.md](../AGENTS.md) carries the standalone triage, model, independent-review,
registered-worktree, publication and documentation gates. The coordinator assigns
a bounded Branding writer; the stable frontend role covers assigned Website or
Webapp consumers. Backend [agent workflow](../../bknd/docs/agent-workflow.md) owns
lifecycle commands and canonical managed `.codex/` configuration. Synchronize only
inside registered task worktrees and preserve custom configuration conflicts.
The shared [model policy](../../bknd/docs/model-policy.md) defines the reviewer
xhigh trial, complex-triage escalation and evaluated future model upgrades.
Unless the user explicitly requests local-only work, the coordinator commits and
publishes each implementation task through that lifecycle; workers do not publish.
Use explicit `--regular-pr`/BLOCKED/`--ready` evidence as required. The user merges
manually unless delegated; publication never authorizes deployment or cleanup.

Governance maintenance belongs under Unreleased and does not bump the brand
version or alter the web allowlist or consumer locks. Regenerate the full asset
manifest after tracked governance/configuration changes, then run all required
[checks](../AGENTS.md#required-checks). Consumer updates remain separately scoped
under [Distribution](Distribution.md); source integration is not deployed evidence.

The coordinator runs the complete fixed `branding-python312-v1` profile through
[Branding local verification](../../bknd/docs/agent-workflow.md#branding-local-verification).
It uses Python 3.12 for manifest freshness, source validation and all distribution
unit tests. Missing prerequisites or failed/incomplete/stale evidence blocks READY.
All source/docs must be committed before this check; regenerate the full manifest
after tracked governance changes. No documentation-only exemption applies.

The `brand-kit` Actions job is removed. Merge the Backend profile support before
this companion retirement. There is no automatic PR or post-merge hosted run;
local logs/evidence remain in the repository Git common directory. These checks
validate asset inventory and tooling, not design quality, deployed consumer assets
or GitHub-enforced merge rules.

`.github/main-protection.json` is a GitHub branch-protection API payload for this
public repository. Its `required_status_checks: null` removes the retired hosted requirement;
there is no status-based up-to-date-branch requirement. It retains one approving review from someone other than the last pusher, resolved conversations,
linear history, and administrator enforcement. Force pushes and branch deletion
are disabled. It grants no repository access.

Applying it changes remote policy and is intentionally not part of source
verification. An authorized administrator may apply it only after confirming
the repository, default branch, plan-supported features, existing settings and
completed local-profile transition. Do not overwrite newer remote controls:

```sh
gh api --method PUT \
  repos/phioon/branding/branches/main/protection \
  --input .github/main-protection.json
```

Presence of the payload does not prove that remote protection is configured.

On 2026-09-23, querying live Branding branch protection returned HTTP 404. Live
protection is therefore unverified; no remote settings were changed. Before manual
merge, reconcile obsolete hosted requirements if remote rules actually enforce them.
A template in Git neither applies policy nor reports local results to GitHub.
