"""Run every self-contained Python lesson test file."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def main() -> None:
    tests = sorted((ROOT / "lessons").rglob("test_*.py"))
    if not tests:
        raise SystemExit("No lesson tests found")

    for test in tests:
        print(f"\n==> {test.relative_to(ROOT)}", flush=True)
        subprocess.run([sys.executable, test.name], cwd=test.parent, check=True)

    print(f"\nAll {len(tests)} lesson test file(s) passed.")


if __name__ == "__main__":
    main()
