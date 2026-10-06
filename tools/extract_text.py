"""Extract per-page text from every archived PDF into build/fulltext.json.

The text feeds two things: the in-browser full-text search over source documents, and
the authoring instruments (tools/lookup.py) used to ground citations to a page.
Pages are PHYSICAL and 1-based, matching [^slug:page].

Scanned PDFs have no text layer. For those, OCR text produced by tools/ocr_sources.py
(sources/ocr/<slug>.txt, one "===== page N / M =====" marker per page) is used for
every page whose text layer is empty; such pages are flagged "ocr": true.

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
OCR_DIR = ROOT / "sources" / "ocr"
OUT = ROOT / "build" / "fulltext.json"
PAGE_MARK = re.compile(r"^===== page (\d+) / \d+ =====\s*$", re.M)


def clean(text: str) -> str:
    text = text.replace("­", "")              # soft hyphens
    text = re.sub(r"-\n(?=[a-z])", "", text)        # words hyphenated across lines
    return re.sub(r"[ \t\r\f\v]+", " ", text).strip()


def load_ocr(slug: str) -> dict[int, str]:
    path = OCR_DIR / f"{slug}.txt"
    if not path.exists():
        return {}
    raw = path.read_text("utf-8", errors="replace")
    parts = PAGE_MARK.split(raw)
    # split() yields [preamble, page_no, text, page_no, text, ...]
    return {int(n): clean(t) for n, t in zip(parts[1::2], parts[2::2])}


def main() -> int:
    data = yaml.safe_load(CATALOG.read_text("utf-8")) or {}
    out: dict[str, dict] = {}
    scanned: list[str] = []
    n_pages = n_ocr = 0
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
        ocr = load_ocr(s["slug"])
        pages = []
        layer_chars = 0
        for i, page in enumerate(reader.pages, start=1):
            try:
                t = clean(page.extract_text() or "")
            except Exception:
                t = ""
            layer_chars += len(t)
            rec = {"page": i, "text": t}
            if len(t) < 20 and ocr.get(i):
                rec = {"page": i, "text": ocr[i], "ocr": True}
                n_ocr += 1
            pages.append(rec)
        n_pages += len(pages)
        if layer_chars < 5 * max(1, len(pages)) and not ocr:
            scanned.append(s["slug"])
        out[s["slug"]] = {"title": s["title"], "publisher": s["publisher"], "local_path": lp,
                          "text_layer_chars": layer_chars, "pages": pages}

    OUT.parent.mkdir(parents=True, exist_ok=True)
    # Atomic replace: authors may be running tools/lookup.py against this file right now.
    tmp = OUT.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(out, ensure_ascii=False), "utf-8")
    tmp.replace(OUT)
    print(f"documents  {len(out)}")
    print(f"pages      {n_pages} ({n_ocr} from OCR)")
    if scanned:
        print(f"no text layer and no OCR yet ({len(scanned)}) -- run tools/ocr_sources.py: {', '.join(scanned)}")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
