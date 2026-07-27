#!/usr/bin/env python3
"""Run one example per unique code snippet and report failures.

The 2000 example files come from ~156 unique snippets, so we run each snippet
once instead of 2000 times. Snippets that need a library you have not installed
(torch, sklearn) are reported separately from real errors.

Run:  python tools/smoke_examples.py
"""
from __future__ import annotations

import hashlib
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    seen: dict[str, Path] = {}
    for path in sorted(ROOT.glob("Day*/examples/*.py")):
        src = path.read_text(encoding="utf-8")
        # Strip the generated header/footer so identical lessons collapse to one run.
        body = src.split('"""', 2)[-1].split("# ----------------------")[0]
        key = hashlib.sha256(body.encode()).hexdigest()
        seen.setdefault(key, path)

    failures, missing_dep = [], []
    with tempfile.TemporaryDirectory() as tmp:
        for i, path in enumerate(seen.values(), 1):
            proc = subprocess.run(
                [sys.executable, str(path)],
                capture_output=True, text=True, timeout=180, cwd=tmp,
            )
            if proc.returncode != 0:
                tail = (proc.stderr or proc.stdout).strip().splitlines()
                last = tail[-1] if tail else "(no output)"
                if "ModuleNotFoundError" in proc.stderr:
                    missing_dep.append((path, last))
                else:
                    failures.append((path, last))

    print(f"ran {len(seen)} unique examples")
    if missing_dep:
        print(f"\nskipped — library not installed ({len(missing_dep)}):")
        for p, msg in missing_dep:
            print(f"  {p.relative_to(ROOT)}: {msg}")
    if failures:
        print(f"\nFAILURES ({len(failures)}):")
        for p, msg in failures:
            print(f"  {p.relative_to(ROOT)}: {msg}")
        return 1
    print("\nno failures")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
