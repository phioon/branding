#!/usr/bin/env python3
"""Generate, verify, and synchronize the approved PHIOON web distribution."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import shutil
import stat
import subprocess
import sys
import tempfile


RELEASE_VERSION = "3.0.0"
REPOSITORY = "phioon/branding"
SCHEMA_VERSION = 1
ROOT = Path(__file__).resolve().parents[1]
ASSET_MANIFEST = ROOT / "Asset-Manifest.json"
WEB_MANIFEST = ROOT / "Web-Distribution.json"
CONSUMER_LOCK = "brand.lock.json"
ARTWORK_SOURCE_REVISION = "a2154f5128b3715162a61d1ebc78b11c44d55c71"
LEGACY_MANIFEST_PATH = "scripts/legacy-web-distribution-1.1.0.json"
LEGACY_MANIFEST_SHA256 = "db853db68195a17c80ab876b3a9f696cc595e7475de28ae5e62fdbe81f81460f"

# This allowlist is the reviewed web consumer contract. Keep source paths sorted.
WEB_PATHS = {
    "brand-tokens.css": "public/brand/brand-tokens.css",
    "fonts/IBMPlexMono-Medium.ttf": "app/fonts/IBMPlexMono-Medium.ttf",
    "fonts/IBMPlexMono-OFL.txt": "public/brand/fonts/IBMPlexMono-OFL.txt",
    "fonts/IBMPlexMono-Regular.ttf": "app/fonts/IBMPlexMono-Regular.ttf",
    "fonts/Manrope-OFL.txt": "public/brand/fonts/Manrope-OFL.txt",
    "fonts/Manrope-Variable.ttf": "app/fonts/Manrope-Variable.ttf",
    "icons/favicon.ico": "public/brand/icons/favicon.ico",
    "icons/favicon.svg": "public/brand/icons/favicon.svg",
    "icons/phioon-icon-128.png": "public/brand/icons/phioon-icon-128.png",
    "icons/phioon-icon-16.png": "public/brand/icons/phioon-icon-16.png",
    "icons/phioon-icon-180.png": "public/brand/icons/phioon-icon-180.png",
    "icons/phioon-icon-192.png": "public/brand/icons/phioon-icon-192.png",
    "icons/phioon-icon-24.png": "public/brand/icons/phioon-icon-24.png",
    "icons/phioon-icon-256.png": "public/brand/icons/phioon-icon-256.png",
    "icons/phioon-icon-32.png": "public/brand/icons/phioon-icon-32.png",
    "icons/phioon-icon-48.png": "public/brand/icons/phioon-icon-48.png",
    "icons/phioon-icon-512.png": "public/brand/icons/phioon-icon-512.png",
    "icons/phioon-icon-64.png": "public/brand/icons/phioon-icon-64.png",
    "icons/site.webmanifest": "public/brand/icons/site.webmanifest",
    "svg/phioon-horizontal-color.svg": "public/brand/svg/phioon-horizontal-color.svg",
    "svg/phioon-horizontal-white.svg": "public/brand/svg/phioon-horizontal-white.svg",
    "svg/phioon-symbol-color.svg": "public/brand/svg/phioon-symbol-color.svg",
    "svg/phioon-symbol-small-color.svg": "public/brand/svg/phioon-symbol-small-color.svg",
    "svg/phioon-symbol-small-white.svg": "public/brand/svg/phioon-symbol-small-white.svg",
    "svg/phioon-symbol-white.svg": "public/brand/svg/phioon-symbol-white.svg",
    "svg/phioon-wordmark-ink.svg": "public/brand/svg/phioon-wordmark-ink.svg",
    "svg/phioon-wordmark-white.svg": "public/brand/svg/phioon-wordmark-white.svg",
}

MANAGED_CONSUMER_ROOTS = (
    "app/fonts",
    "public/brand/fonts",
    "public/brand/icons",
    "public/brand/svg",
)
MANAGED_CONSUMER_FILES = ("public/brand/brand-tokens.css",)
IGNORED_RELEASE_PARTS = {".git", "__pycache__", ".pytest_cache"}
IGNORED_RELEASE_NAMES = {".DS_Store", "Asset-Manifest.json"}


class VerificationError(Exception):
    """A manifest or consumer tree does not match the approved distribution."""


def _safe_relative(value: str) -> Path:
    if not isinstance(value, str) or not value or "\0" in value:
        raise VerificationError(f"unsafe relative path: {value!r}")
    pure = PurePosixPath(value)
    if (
        pure.is_absolute()
        or not pure.parts
        or ".." in pure.parts
        or pure.as_posix() != value
    ):
        raise VerificationError(f"unsafe relative path: {value!r}")
    return Path(*pure.parts)


def _digest(path: Path) -> tuple[int, str]:
    data = path.read_bytes()
    return len(data), hashlib.sha256(data).hexdigest()


def _entry(path: Path, relative: str, *, consumer_path: str | None = None) -> dict:
    size, digest = _digest(path)
    result = {"path": relative, "bytes": size, "sha256": digest}
    if consumer_path is not None:
        result["consumerPath"] = consumer_path
    return result


def _release_paths() -> list[str]:
    paths: list[str] = []
    for path in ROOT.rglob("*"):
        relative = path.relative_to(ROOT)
        if any(part in IGNORED_RELEASE_PARTS for part in relative.parts):
            continue
        if path.name in IGNORED_RELEASE_NAMES or not path.is_file():
            continue
        paths.append(relative.as_posix())
    return sorted(paths)


def asset_manifest() -> dict:
    return {
        "schemaVersion": SCHEMA_VERSION,
        "name": "PHIOON brand kit",
        "version": RELEASE_VERSION,
        "visualIdentityVersion": "1.0",
        "order": "path (ascending Unicode code point order)",
        "selfHash": False,
        "files": [
            _entry(ROOT / _safe_relative(path), path) for path in _release_paths()
        ],
    }


def web_manifest() -> dict:
    files = []
    for source_path in sorted(WEB_PATHS):
        consumer_path = WEB_PATHS[source_path]
        files.append(
            _entry(
                ROOT / _safe_relative(source_path),
                source_path,
                consumer_path=consumer_path,
            )
        )
    return {
        "schemaVersion": SCHEMA_VERSION,
        "name": "PHIOON approved web distribution",
        "version": RELEASE_VERSION,
        "visualIdentityVersion": "1.0",
        "order": "path (ascending Unicode code point order)",
        "selfHash": False,
        "provenance": {
            "browserFavicons": {
                "repository": REPOSITORY,
                "revision": ARTWORK_SOURCE_REVISION,
                "treatment": "white optical symbol on Deep Navy",
                "paths": [
                    "icons/favicon.ico",
                    "icons/favicon.svg",
                ],
            }
        },
        "managedConsumerRoots": list(MANAGED_CONSUMER_ROOTS),
        "managedConsumerFiles": list(MANAGED_CONSUMER_FILES),
        "files": files,
    }


def _json_bytes(document: dict) -> bytes:
    return (json.dumps(document, indent=2, ensure_ascii=False) + "\n").encode()


def _write_atomic(path: Path, content: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    try:
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(content)
        os.replace(temporary, path)
    except BaseException:
        Path(temporary).unlink(missing_ok=True)
        raise


def generate(*, check: bool) -> None:
    # The full manifest includes the web manifest, so generate/check it first.
    outputs = ((WEB_MANIFEST, web_manifest()),)
    for path, document in outputs:
        expected = _json_bytes(document)
        if check:
            if not path.exists() or path.read_bytes() != expected:
                raise VerificationError(f"generated file is stale: {path.name}")
        else:
            _write_atomic(path, expected)

    asset_expected = _json_bytes(asset_manifest())
    if check:
        if not ASSET_MANIFEST.exists() or ASSET_MANIFEST.read_bytes() != asset_expected:
            raise VerificationError(f"generated file is stale: {ASSET_MANIFEST.name}")
    else:
        _write_atomic(ASSET_MANIFEST, asset_expected)


def _read_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as error:
        raise VerificationError(f"cannot read {path.name}: {error}") from error


def check_licenses(manifest: dict) -> None:
    distributed = {entry["path"] for entry in manifest.get("files", [])}
    requirements = {
        "fonts/Manrope-Variable.ttf": "fonts/Manrope-OFL.txt",
        "fonts/IBMPlexMono-Regular.ttf": "fonts/IBMPlexMono-OFL.txt",
        "fonts/IBMPlexMono-Medium.ttf": "fonts/IBMPlexMono-OFL.txt",
    }
    for font_path, license_path in requirements.items():
        if font_path in distributed and license_path not in distributed:
            raise VerificationError(f"{font_path} is distributed without {license_path}")
        license_text = (ROOT / license_path).read_text(encoding="utf-8")
        if "SIL OPEN FONT LICENSE" not in license_text.upper():
            raise VerificationError(f"invalid or missing SIL license: {license_path}")


def check_source() -> dict:
    generate(check=True)
    if _digest(ROOT / LEGACY_MANIFEST_PATH)[1] != LEGACY_MANIFEST_SHA256:
        raise VerificationError("frozen legacy 1.1.0 distribution manifest differs from approved bytes")
    manifest = _read_json(WEB_MANIFEST)
    if manifest != web_manifest():
        raise VerificationError(f"inconsistent manifest: {WEB_MANIFEST.name}")
    if _read_json(ASSET_MANIFEST) != asset_manifest():
        raise VerificationError(f"inconsistent manifest: {ASSET_MANIFEST.name}")
    check_licenses(manifest)
    return manifest


def _source_revision() -> str:
    """Only committed, clean release sources may identify a consumer lock."""
    def git(*args: str) -> str:
        try:
            return subprocess.run(
                ["git", "-C", str(ROOT), *args], check=True,
                capture_output=True, text=True,
            ).stdout.strip()
        except (OSError, subprocess.CalledProcessError) as error:
            raise VerificationError("Branding source must be a committed Git checkout") from error

    if Path(git("rev-parse", "--show-toplevel")).resolve() != ROOT.resolve():
        raise VerificationError("Branding source must be the root of its Git checkout")
    revision = git("rev-parse", "--verify", "HEAD")
    if not re.fullmatch(r"[0-9a-f]{40}|[0-9a-f]{64}", revision):
        raise VerificationError("invalid Branding source revision")
    if git("status", "--porcelain", "--untracked-files=all"):
        raise VerificationError("Branding source has dirty or uncommitted files")
    # Verify release bytes against HEAD, including ignored files and tracked
    # files hidden from status by assume-unchanged/skip-worktree index flags.
    committed = {}
    for record in git("ls-tree", "-r", "-z", "HEAD").split("\0"):
        if record:
            metadata, path = record.split("\t", 1)
            mode, kind, digest = metadata.split()
            committed[path] = (mode, kind, digest)
    algorithm = "sha256" if len(revision) == 64 else "sha1"
    for relative in ["Asset-Manifest.json", *_release_paths()]:
        path = ROOT / relative
        record = committed.get(relative)
        if (
            not record or record[0] not in ("100644", "100755")
            or not stat.S_ISREG(path.lstat().st_mode)
        ):
            raise VerificationError(f"uncommitted or unsupported Branding source: {relative}")
        content = path.read_bytes()
        blob = b"blob " + str(len(content)).encode() + b"\0" + content
        if hashlib.new(algorithm, blob).hexdigest() != record[2]:
            raise VerificationError(f"Branding source differs from committed revision: {relative}")
    return revision


def consumer_lock(manifest: dict) -> dict:
    return {
        "schemaVersion": 1,
        "repository": REPOSITORY,
        "version": manifest["version"],
        "revision": _source_revision(),
        "webDistributionSha256": _digest(WEB_MANIFEST)[1],
    }


def _check_consumer_lock(path: Path, expected: dict) -> None:
    if not path.is_file():
        raise VerificationError(f"missing: {CONSUMER_LOCK}")
    actual = _read_json(path)
    if actual != expected or path.read_bytes() != _json_bytes(expected):
        raise VerificationError(f"stale, malformed or mismatched: {CONSUMER_LOCK}")


def _consumer_expected(manifest: dict) -> dict[str, dict]:
    expected: dict[str, dict] = {}
    for entry in manifest.get("files", []):
        _safe_relative(entry["path"])
        consumer_path = entry.get("consumerPath")
        _safe_relative(consumer_path)
        if consumer_path in expected:
            raise VerificationError(f"duplicate consumer path: {consumer_path}")
        expected[consumer_path] = entry
    return expected


def _consumer_target(consumer_root: Path, relative: str) -> Path:
    relative_path = _safe_relative(relative)
    target = consumer_root
    for index, part in enumerate(relative_path.parts):
        target /= part
        try:
            mode = target.lstat().st_mode
        except FileNotFoundError:
            return consumer_root / relative_path
        offender = target.relative_to(consumer_root).as_posix()
        if stat.S_ISLNK(mode):
            raise VerificationError(f"symlink in managed consumer path: {offender}")
        if index < len(relative_path.parts) - 1 and not stat.S_ISDIR(mode):
            raise VerificationError(f"unsupported managed path component: {offender}")
    return target


def _require_type(path: Path, relative: str, *, directory: bool = False) -> None:
    try:
        mode = path.lstat().st_mode
    except FileNotFoundError:
        return
    if stat.S_ISLNK(mode):
        raise VerificationError(f"symlink in managed consumer path: {relative}")
    if not (stat.S_ISDIR(mode) if directory else stat.S_ISREG(mode)):
        kind = "directory" if directory else "regular file"
        raise VerificationError(f"unsupported managed consumer entry: {relative} (expected {kind})")


def _check_managed_entries(
    consumer_root: Path, directory: Path, expected: set[str], allowed_dirs: set[str]
) -> None:
    pending = [directory]
    while pending:
        current = pending.pop()
        with os.scandir(current) as children:
            for child in sorted(children, key=lambda entry: entry.name):
                path = Path(child.path)
                relative = path.relative_to(consumer_root).as_posix()
                if child.is_symlink():
                    raise VerificationError(f"symlink in managed consumer tree: {relative}")
                if child.is_dir(follow_symlinks=False):
                    if relative not in allowed_dirs:
                        raise VerificationError(f"extra: {relative}")
                    pending.append(path)
                elif child.is_file(follow_symlinks=False):
                    if relative not in expected:
                        raise VerificationError(f"extra: {relative}")
                else:
                    raise VerificationError(
                        f"unsupported filesystem entry in managed consumer tree: {relative}"
                    )


def _consumer_preflight(
    consumer_root: Path, manifest: dict, *, retired: dict | None = None
) -> tuple[dict, dict]:
    # Validate the whole contract before inspecting or changing the consumer.
    expected = _consumer_expected(manifest)
    permitted = {**expected, **(retired or {})}
    for relative in permitted:
        _safe_relative(relative)
    managed_roots = manifest["managedConsumerRoots"]
    managed_files = manifest["managedConsumerFiles"]
    for relative in (*managed_roots, *managed_files):
        _safe_relative(relative)
    # Do not resolve the root: that would hide a consumer-root symlink.
    _require_type(consumer_root, ".", directory=True)
    targets = {}
    for relative in (*permitted, *managed_files, CONSUMER_LOCK):
        target = _consumer_target(consumer_root, relative)
        _require_type(target, relative)
        targets[relative] = target
    allowed_dirs = {
        parent.as_posix()
        for relative in permitted
        for parent in PurePosixPath(relative).parents
    }
    for relative in managed_roots:
        directory = _consumer_target(consumer_root, relative)
        _require_type(directory, relative, directory=True)
        if directory.exists():
            _check_managed_entries(consumer_root, directory, set(permitted), allowed_dirs)
    return expected, targets


def _retired_files(manifest: dict) -> dict[str, dict]:
    """Only the frozen 1.1.0 allowlist grants permission to retire old names."""
    legacy = _consumer_expected(_read_json(ROOT / LEGACY_MANIFEST_PATH))
    current = _consumer_expected(manifest)
    return {path: entry for path, entry in legacy.items() if path not in current}


def _retirement_preflight(targets: dict, retired: dict) -> list[Path]:
    present = [path for path in retired if targets[path].exists()]
    if not present:
        return []
    lock_path = targets[CONSUMER_LOCK]
    if not lock_path.is_file():
        raise VerificationError("legacy migration requires a 1.1.0 brand.lock.json")
    lock = _read_json(lock_path)
    if not isinstance(lock, dict) or (
        set(lock) != {"schemaVersion", "repository", "version", "revision", "webDistributionSha256"}
        or lock.get("schemaVersion") != 1
        or lock.get("repository") != "mishkal-ai/branding"
        or lock.get("version") != "1.1.0"
        or not isinstance(lock.get("revision"), str)
        or not re.fullmatch(r"[0-9a-f]{40}|[0-9a-f]{64}", lock["revision"])
        or lock.get("webDistributionSha256") != LEGACY_MANIFEST_SHA256
    ):
        raise VerificationError("legacy migration requires the approved 1.1.0 brand.lock.json")
    for path in present:
        entry = retired[path]
        if _digest(targets[path]) != (entry["bytes"], entry["sha256"]):
            raise VerificationError(f"modified legacy file; preserve and reconcile before migration: {path}")
    return [targets[path] for path in present]


def check_consumer(consumer_root: Path, manifest: dict | None = None) -> None:
    manifest = manifest or check_source()
    expected, targets = _consumer_preflight(consumer_root, manifest)
    _check_consumer_lock(targets[CONSUMER_LOCK], consumer_lock(manifest))
    problems: list[str] = []
    for relative, entry in expected.items():
        target = targets[relative]
        if not target.is_file():
            problems.append(f"missing: {relative}")
            continue
        size, digest = _digest(target)
        if size != entry["bytes"] or digest != entry["sha256"]:
            problems.append(f"tampered: {relative}")

    if problems:
        raise VerificationError("consumer verification failed:\n  " + "\n  ".join(problems))


def sync_consumer(consumer_root: Path) -> None:
    manifest = check_source()
    retired = _retired_files(manifest)
    expected, targets = _consumer_preflight(consumer_root, manifest, retired=retired)
    retirement_targets = _retirement_preflight(targets, retired)
    lock_bytes = _json_bytes(consumer_lock(manifest))

    for consumer_path, entry in expected.items():
        source = ROOT / _safe_relative(entry["path"])
        target = targets[consumer_path]
        if target.is_file() and _digest(target) == (entry["bytes"], entry["sha256"]):
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        descriptor, temporary = tempfile.mkstemp(prefix=f".{target.name}.", dir=target.parent)
        os.close(descriptor)
        try:
            shutil.copyfile(source, temporary)
            os.replace(temporary, target)
        except BaseException:
            Path(temporary).unlink(missing_ok=True)
            raise
    for target in retirement_targets:
        target.unlink()
    lock_target = targets[CONSUMER_LOCK]
    if not lock_target.is_file() or lock_target.read_bytes() != lock_bytes:
        _write_atomic(lock_target, lock_bytes)
    check_consumer(consumer_root, manifest)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    generate_parser = subparsers.add_parser("generate", help="write manifests")
    generate_parser.add_argument("--check", action="store_true", help="fail if stale")
    subparsers.add_parser("check-source", help="verify source files and licenses")
    for command in ("sync", "check-consumer"):
        command_parser = subparsers.add_parser(command)
        command_parser.add_argument(
            "--consumer-root", type=Path, required=True, help="consumer repository root"
        )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        if args.command == "generate":
            generate(check=args.check)
        elif args.command == "check-source":
            check_source()
        elif args.command == "sync":
            sync_consumer(args.consumer_root)
        elif args.command == "check-consumer":
            check_consumer(args.consumer_root)
    except VerificationError as error:
        print(error, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
