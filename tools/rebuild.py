"""Run the whole pipeline in order, stopping at the first failure.

    sync_sources  ->  extract_text  ->  build_kb  ->  verify_kb  [->  smoke_test]

Usage:
    python tools/rebuild.py            # reconcile archive, extract text, build, verify
    python tools/rebuild.py --smoke    # ... and load every route in headless Chrome
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

TOOLS = Path(__file__).resolve().parent
STEPS = ["sync_sources.py", "extract_text.py", "build_kb.py", "verify_kb.py"]


def main() -> int:
    steps = STEPS + (["smoke_test.py"] if "--smoke" in sys.argv else [])
    for step in steps:
        print(f"\n=== {step} ===", flush=True)
        rc = subprocess.call([sys.executable, str(TOOLS / step)])
        if rc != 0:
            print(f"\npipeline stopped: {step} exited {rc}")
            return rc
    print("\npipeline ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
