"""Extract per-page text from every archived PDF into build/fulltext.json.

The text feeds two things: the in-browser full-text search over source documents, and
the authoring instruments (tools/lookup.py) used to ground citations to a page.
Pages are PHYSICAL and 1-based, matching [^slug:page].

Scanned PDFs without a text layer produce empty pages; they are reported, not OCR'd.

Usage:  python tools/extract_text.py
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import yaml
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parent.parent
CATALOG = ROOT / "sources" / "catalog.yaml"
KB = ROOT / "kb"
OUT = ROOT / "build" / "fulltext.json"


def clean(text: str) -> str:
    text = text.replace("­", "")              # soft hyphens
    text = re.sub(r"-\n(?=[a-z])", "", text)        # words hyphenated across lines
    return re.sub(r"[ \t\r\f\v]+", " ", text).strip()


def main() -> int:
    data = yaml.safe_load(CATALOG.read_text("utf-8")) or {}
    out: dict[str, dict] = {}
    empty_docs: list[str] = []
    n_pages = 0
    for s in data.get("sources", []):
        lp = s.get("local_path")
        if not lp or s.get("status") != "ok" or not lp.lower().endswith(".pdf"):
            continue
        path = KB / lp
        try:
            reader = PdfReader(str(path))
        except Exception as exc:
            print(f"  !! {s['slug']}: unreadable ({exc})")
            continue
        pages = []
        chars = 0
        for i, page in enumerate(reader.pages, start=1):
            try:
                t = clean(page.extract_text() or "")
            except Exception:
                t = ""
            chars += len(t)
            pages.append({"page": i, "text": t})
        n_pages += len(pages)
        if chars < 50 * max(1, len(pages)) * 0.1:
            empty_docs.append(s["slug"])
        out[s["slug"]] = {"title": s["title"], "publisher": s["publisher"], "local_path": lp, "pages": pages}

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, ensure_ascii=False), "utf-8")
    print(f"documents  {len(out)}")
    print(f"pages      {n_pages}")
    if empty_docs:
        print(f"no text layer (scanned?): {', '.join(empty_docs)}")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
