"""Print the text of selected pages of a PDF, with page markers, for grounding citations.

Page numbers are PHYSICAL pages, 1-based -- the number a PDF viewer shows and the
number a `#page=N` link opens -- not the folio printed on the page. Citations in
content/ ([^slug:N]) use the same convention.

Usage:
    python tools/pdf_pages.py kb/pdfs/pse-revised-trading-rules.pdf          # page count + all pages
    python tools/pdf_pages.py kb/pdfs/pse-revised-trading-rules.pdf 12-14    # pages 12..14
    python tools/pdf_pages.py pse-revised-trading-rules 7                    # slug shorthand
"""

from __future__ import annotations

import sys
from pathlib import Path

from pypdf import PdfReader

ROOT = Path(__file__).resolve().parent.parent
PDFS = ROOT / "kb" / "pdfs"


def resolve(arg: str) -> Path:
    p = Path(arg)
    if p.exists():
        return p
    q = PDFS / (arg if arg.endswith(".pdf") else f"{arg}.pdf")
    if q.exists():
        return q
    raise SystemExit(f"no such PDF: {arg}")


def parse_range(spec: str, n: int) -> list[int]:
    pages: list[int] = []
    for part in spec.split(","):
        if "-" in part:
            a, b = part.split("-", 1)
            pages.extend(range(int(a), int(b) + 1))
        else:
            pages.append(int(part))
    return [p for p in pages if 1 <= p <= n]


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 1
    path = resolve(sys.argv[1])
    reader = PdfReader(str(path))
    n = len(reader.pages)
    pages = parse_range(sys.argv[2], n) if len(sys.argv) > 2 else list(range(1, n + 1))
    print(f"# {path.name}: {n} pages")
    for p in pages:
        try:
            text = reader.pages[p - 1].extract_text() or ""
        except Exception as exc:  # malformed page streams happen in scanned rulebooks
            text = f"<extract failed: {exc}>"
        print(f"\n===== page {p} / {n} =====\n{text}")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
