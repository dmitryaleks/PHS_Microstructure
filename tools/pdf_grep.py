"""Search archived PDFs for a regex and report slug:page hits, for grounding citations.

Pages are PHYSICAL and 1-based, matching the [^slug:page] citation convention.

Usage:
    python tools/pdf_grep.py "board lot"                         # every PDF in kb/pdfs
    python tools/pdf_grep.py "pre-?open" pse-revised-trading-rules  # one document (slug or path)
    python tools/pdf_grep.py -C 300 "static threshold"           # wider context (chars)
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

from pypdf import PdfReader

ROOT = Path(__file__).resolve().parent.parent
PDFS = ROOT / "kb" / "pdfs"


def main() -> int:
    args = sys.argv[1:]
    ctx = 160
    if len(args) >= 2 and args[0] == "-C":
        ctx = int(args[1])
        args = args[2:]
    if not args:
        print(__doc__)
        return 1
    pattern = re.compile(args[0], re.I)
    targets: list[Path] = []
    for a in args[1:]:
        p = Path(a)
        if not p.exists():
            p = PDFS / (a if a.endswith(".pdf") else f"{a}.pdf")
        targets.append(p)
    if not targets:
        targets = sorted(PDFS.glob("*.pdf"))

    hits = 0
    for path in targets:
        try:
            reader = PdfReader(str(path))
        except Exception as exc:
            print(f"!! {path.name}: unreadable ({exc})")
            continue
        for i, page in enumerate(reader.pages, start=1):
            try:
                text = page.extract_text() or ""
            except Exception:
                continue
            flat = re.sub(r"\s+", " ", text)
            for m in pattern.finditer(flat):
                a, b = max(0, m.start() - ctx), min(len(flat), m.end() + ctx)
                print(f"[{path.stem}:{i}] ...{flat[a:b]}...")
                hits += 1
    print(f"\n{hits} hit(s)")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
