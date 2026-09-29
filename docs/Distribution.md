# Web distribution contract

`Web-Distribution.json` is the approved web subset of proposed PHIOON web distribution 3.0.0 (visual identity 1.0). Schema
version 1 records the release `version`, deterministic `order`, `selfHash`
policy, exact artifact `provenance`, managed consumer paths, and sorted file
records containing source `path`, `consumerPath`, `bytes`, and SHA-256.

The current contract places supporting font binaries under `app/fonts`, while
logos, icons, licenses and semantic tokens live under `public/brand`.
Consumer-owned `public/brand/SOURCE.md` is outside managed roots and is
preserved. Consumer paths are a contract: coordinate changes with consumers.

## Versioning and release procedure

The kit follows semantic versioning: incompatible consumer-path or contract
changes require a major version; additive approved assets/features use a minor
version; compatible corrections use a patch version. Proposed release `3.0.0`
changes producer/lock repository identity to `phioon/branding`, which requires
consumer verifier updates and therefore a major version. Artwork bytes, managed
consumer paths, schema 1 and the artwork source revision remain unchanged from
2.0.0. The planned tag name is `v3.0.0`; source preparation creates neither a tag
nor a release. A published version/tag must not be retargeted;
corrections require a new version. The lock records the version without the `v`
prefix and binds the full commit, not a mutable branch or tag name.

Unreleased governance-only maintenance may update repository guides and managed
agent configuration without changing `RELEASE_VERSION`, artwork or the approved
`Web-Distribution.json` bytes. Record it under Unreleased and regenerate the full
`Asset-Manifest.json` inventory, then run the same required source checks. Such a
commit is not a new brand release or an instruction to repoint a consumer lock.
Do not retag an existing version, create a release or sync consumers as part of
that maintenance; actual release/consumer changes follow the procedure below.

1. Make approved changes and update `RELEASE_VERSION`, the allowlist and current
   documentation in the same task.
2. Run `python3 scripts/brand_distribution.py generate` after all source,
   documentation, and test edits.
3. Run the three checks in `docs/Verification.md` and inspect the complete diff.
4. Publish the reviewed task through the repository lifecycle. After the user
   merges it, verify the clean release commit and its checks. Only when separately
   authorized, create the immutable `v3.0.0` tag and release at that exact commit;
   record its commit and `Web-Distribution.json` SHA-256 in the release notes.
5. In a separately authorized consumer task, acquire that committed source,
   run `sync`, review the assets and lock diff together, update consumer-owned
   provenance notes, and run the complete consumer local profile before publication. Tagging or release
   publication does not sync or deploy consumers.

Generation writes `Web-Distribution.json` before calculating the full release
inventory. `Asset-Manifest.json` therefore checksums the web manifest but
excludes itself. The web manifest includes neither manifest, avoiding recursive
hash dependencies.

## Consumer lock and upgrades

Sync writes a deterministic root `brand.lock.json` after copying the assets:

```json
{
  "schemaVersion": 1,
  "repository": "phioon/branding",
  "version": "3.0.0",
  "revision": "<full Branding commit>",
  "webDistributionSha256": "<SHA-256 of exact Web-Distribution.json bytes>"
}
```

The angle-bracket values above are documentation placeholders; sync computes
both values. Commit this lock alongside the consumer assets. It is generated
consumer metadata, not a copied source asset, and therefore has no entry in the
web manifest's source-file hashes. Matching assets and matching lock bytes keep
their modification times. `check-consumer` is read-only and rejects absent,
malformed, stale or mismatched locks as well as asset drift.

Both consumer commands require a clean, committed Branding checkout. All release
files must be committed at its `HEAD` and match their Git blob bytes. Dirty,
staged, untracked or status-hidden modifications cannot claim a committed release
identity. `generate`, `check-source` and unit tests still support work in progress;
they do not establish a publishable revision. Source archives without Git metadata
cannot be used for sync/check-consumer.

To upgrade, explicitly acquire and verify the approved new Branding commit, then
run its `sync` command. Sync repairs or replaces a regular stale/malformed lock;
it rejects a symlink or unsupported lock entry before any asset writes. Review
the version, revision, checksum and asset changes together. An empty new commit
still changes the lock revision even when its manifest checksum is identical.

Website and Webapp adoption of 3.0.0 is pending separately: their existing
validators accept the historical repository identity and must be updated before
new locks are adopted. The current checker accepts only the canonical identity
for a current lock. Existing 2.0.0 locks remain bound to their original committed
source and checker; this change does not rewrite historical distributions or
grant the new checker permission to accept arbitrary repository identities.
The 1.1.0 identity is retained only for the bounded retirement preflight below.

## Consumer-local verification

Consumer local verification must acquire the locked source from the trusted
public `phioon/branding` repository through anonymous Git acquisition;
no dedicated cross-repository credential or Actions run is required.
Read `revision` from the committed consumer lock, require a full lowercase
40- or 64-character hexadecimal commit, and check out that exact commit in a
separate Branding directory in detached-HEAD mode. Do not use an unpinned
`main`, a moving tag, or an arbitrary sibling checkout. Confirm the acquired
checkout's `git rev-parse HEAD` equals the requested revision before invoking
its checker. No credentials belong in the lock or repository.

From the consumer root, with that checkout supplied as `BRANDING_ROOT`:

```sh
python3 "$BRANDING_ROOT/scripts/brand_distribution.py" check-consumer --consumer-root .
```

This invocation is read-only in the consumer and requires no consumer sync during verification.
The checker independently verifies the source's clean committed bytes, matches
the lock's exact commit/version/manifest checksum, then verifies every managed
asset and the topology. A provided source checkout at a different commit fails
even if the assets happen to match. A missing lock fails; verification must not repair it
by running sync. Acquiring the source requires Git repository access; verification
itself uses only Python's standard library and local Git, with no network access.

For example, the local acquisition step validates the lock revision before
checking out that exact commit from the fixed trusted repository:

```sh
python3 -c 'import json, re; lock = json.load(open("brand.lock.json")); revision = lock["revision"]; assert isinstance(revision, str) and re.fullmatch(r"[0-9a-f]{40}|[0-9a-f]{64}", revision); print(revision)'
```

The checkout repository is fixed in the consumer verification configuration; never derive a clone URL
or executable path from lock contents. Review lock updates as dependency upgrades.

## Filesystem safety

Sync validates all manifest paths and preflights the consumer root, every managed
destination, intervening component, and managed directory before its first write.
It rejects symlinks (including root, internal, external, dangling, and matching-byte
links), unsupported entry types, and files/directories in the wrong position.
Unexpected files and directories fail preflight; extra directories are not
traversed. Only verified retired 1.1.0 filenames are removed during the explicit
migration described below. No arbitrary extras are deleted. Diagnostics identify the consumer-relative
offender (`.` denotes the consumer root). Invalid paths or topology leave the
entire consumer tree unchanged, including files that otherwise need repair.

Missing or tampered regular files remain repairable; matching regular files keep
their modification times. Consumer verification uses the same topology checks.
Run with exclusive access to the consumer tree: preflight is not protection
against concurrent filesystem changes, and per-file atomic replacement is not
a transaction rolling back unrelated I/O failures during sync.

## Migration from 1.1.0

Version 2.0.0 changed managed asset filenames to `phioon-*` and tokens to
`--phioon-*`. It keeps the schema version and destination roots unchanged.
The `visualIdentityVersion` manifest field distinguishes the supplied visual
identity 1.0 from the distribution version. Proposed 3.0.0 preserves those paths
and tokens and supports the same bounded 1.1.0 retirement. The provenance
record identifies the preserved PHIOON input commit and its white-on-Deep-Navy
browser favicons under canonical repository identity `phioon/branding`; its
artwork source revision remains `a2154f5128b3715162a61d1ebc78b11c44d55c71`.
That repository value identifies the renamed current location of the preserved
artwork; historical 2.0.0 manifest and lock bytes retain their original identity.

`scripts/legacy-web-distribution-1.1.0.json` is the frozen previous allowlist,
including checksums. It is migration metadata, not a dependency on an archived
artwork folder. Do not edit this historical contract to accommodate drift.

When sync encounters any of the 18 retired icon/SVG filenames, it requires a
schema-1 lock for `mishkal-ai/branding` version `1.1.0`, a full hexadecimal
revision and the exact frozen manifest checksum. Every present retired file
must be a regular file with its approved bytes and SHA-256. The complete
consumer topology, legacy lock and retirement checks run before any write.
Unknown files, modified retired files, symlinks and misplaced entries fail
without changing the consumer tree; preserve and reconcile them explicitly.

After preflight, sync copies the new release, unlinks only the verified retired
files and writes the new lock. It does not recursively delete directories.
Missing legacy files are permitted so an interrupted migration can be retried;
matching current files retain their modification times. Per-file writes are
atomic, but the whole operation is not a transaction: use exclusive tree access
and rerun after an ordinary I/O failure. Fresh consumers need no legacy lock.
Read-only `check-consumer` never migrates and rejects any remaining legacy files.

The consumer owner must update visible/accessibility text, metadata, asset and
token references, logo sizing, and consumer-owned provenance documentation in
the same upgrade. Sync cannot update application code, domains or deployment
configuration. Upgrade Branding source first, then consumer assets/lock and
application references together; run each consumer's complete local profile.
Publication does not authorize merging, release tagging, deployment or moving
the user's legacy archive.
