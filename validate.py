#!/usr/bin/env python3
"""validate.py — deployment readiness check for zenodo-auto-publish."""

import importlib.util
import os
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).parent.resolve()

PASS = "\033[32m✅ PASS\033[0m"
FAIL = "\033[31m❌ FAIL\033[0m"
WARN = "\033[33m⚠️  WARN\033[0m"


def check(label: str, condition: bool, warning: bool = False) -> bool:
    status = (WARN if warning else FAIL) if not condition else PASS
    print(f"  {status}  {label}")
    return condition


def section(title: str) -> None:
    print(f"\n{'─' * 60}")
    print(f"  {title}")
    print(f"{'─' * 60}")


def main() -> int:
    failures = 0

    # ── 1. Essential files ────────────────────────────────────────────────
    section("1. Essential files")
    essential_files = [
        "zenodo_auto_publish.py",
        "README.md",
        "CHANGELOG.md",
        "DEPLOYMENT_GUIDE.md",
        "GO_TO_MARKET.md",
        "LICENSE",
    ]
    for f in essential_files:
        ok = (REPO_ROOT / f).is_file()
        if not check(f, ok):
            failures += 1

    # ── 2. GitHub infrastructure ──────────────────────────────────────────
    section("2. GitHub infrastructure")
    github_files = [
        ".github/labels.yml",
        ".github/workflows/sync-labels.yml",
        ".github/PULL_REQUEST_TEMPLATE.md",
        ".github/ISSUE_TEMPLATE/feature.yml",
        ".github/ISSUE_TEMPLATE/bug.yml",
        ".github/ISSUE_TEMPLATE/work-request.yml",
    ]
    for f in github_files:
        ok = (REPO_ROOT / f).is_file()
        if not check(f, ok):
            failures += 1

    # ── 3. Security: no committed secrets ────────────────────────────────
    section("3. Security: no committed secrets")
    sensitive_patterns = [".env"]
    for pattern in sensitive_patterns:
        found = list(REPO_ROOT.glob(pattern))
        clean = len(found) == 0
        if not check(f"No {pattern} committed", clean):
            failures += 1

    # ── 4. Python importability ───────────────────────────────────────────
    section("4. Core script importability")
    script_path = REPO_ROOT / "zenodo_auto_publish.py"
    if script_path.is_file():
        spec = importlib.util.spec_from_file_location("zenodo_auto_publish", script_path)
        mod = importlib.util.module_from_spec(spec)  # type: ignore[arg-type]
        try:
            spec.loader.exec_module(mod)  # type: ignore[union-attr]
            ok = True
        except Exception as exc:
            ok = False
            print(f"    Error: {exc}")
        if not check("zenodo_auto_publish.py imports cleanly", ok):
            failures += 1
    else:
        failures += 1

    # ── 5. Dependencies available ─────────────────────────────────────────
    section("5. Dependencies")
    deps = ["requests"]
    for dep in deps:
        available = importlib.util.find_spec(dep) is not None
        if not check(f"pip package '{dep}' installed", available):
            failures += 1

    # ── 6. README completeness ────────────────────────────────────────────
    section("6. README completeness")
    readme = (REPO_ROOT / "README.md").read_text() if (REPO_ROOT / "README.md").is_file() else ""
    readme_checks = {
        "Has Features section": "## Features" in readme,
        "Has Installation section": "## Installation" in readme,
        "Has Usage section": "## Usage" in readme,
        "Has example command": "--token" in readme,
    }
    for label, ok in readme_checks.items():
        if not check(label, ok):
            failures += 1

    # ── 7. CHANGELOG up-to-date ───────────────────────────────────────────
    section("7. CHANGELOG")
    changelog = (REPO_ROOT / "CHANGELOG.md").read_text() if (REPO_ROOT / "CHANGELOG.md").is_file() else ""
    if not check("CHANGELOG.md is non-empty", len(changelog) > 100):
        failures += 1

    # ── Summary ───────────────────────────────────────────────────────────
    print(f"\n{'═' * 60}")
    if failures == 0:
        print("  \033[32m🚀 All checks passed. Ready to ship.\033[0m")
    else:
        print(f"  \033[31m🚫 {failures} check(s) failed. Fix before shipping.\033[0m")
    print(f"{'═' * 60}\n")

    return 0 if failures == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
