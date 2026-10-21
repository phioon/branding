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

[AGENTS.md](../AGENTS.md) carries the active Vibe workflow and PHIOON delivery
and documentation preferences. Select native agents/models by the task under
Vibe; the former PHIOON domain profiles, routing, registered-worktree requirements
and configuration synchronization are deferred. Preserve local client settings.
After applicable checks and review, create the task PR by default unless local-only
or another explicit restriction applies. Keep `[READY]`/`[BLOCKED]` truthful;
the user merges manually. Publication grants no deployment or cleanup authority.

Governance maintenance belongs under Unreleased and does not bump the brand
version or alter the web allowlist or consumer locks. Regenerate the full asset
manifest after tracked governance/configuration changes, then run all required
[checks](../AGENTS.md#required-checks). Consumer updates remain separately scoped
under [Distribution](Distribution.md); source integration is not deployed evidence.

The exact root `.codex/config.toml` and `AGENTS.override.md` are host-local and
excluded from the release inventory. Stable templates and other governance files
remain hashed. This is not a blanket `.codex` or Git-ignored-file exemption;
nested files with the same names remain inventoried. Local settings/overlays do
not change the brand release or web consumer distribution.

Generated `graphify-out/` graphs and caches are also excluded from the release
inventory. Their creation or refresh must not change release metadata.

Run the Python 3.12 commands in [Required checks](../AGENTS.md#required-checks)
directly. Distribution-tooling changes also require the unit suite. Regenerate
metadata after inventoried source edits; incomplete/stale checks or documentation
block `[READY]`. These checks need no old registration, routing or ledger.

Historical CI retirement: the `brand-kit` Actions job was removed; the former
Backend-profile prerequisite and Git-common-directory evidence applied to that
retirement, not new Vibe tasks. Preserve those records. The direct checks above
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
