"""OCR every archived PDF that has no text layer, into sources/ocr/<slug>.txt.

Several key sources are scans -- the 2010 Revised Trading Rules, the DMA and CMIC
rules, BIR revenue regulations, Republic Acts -- so without OCR they are invisible
to full-text search and to tools/lookup.py. OCR runs on the engine built into
Windows (tools/ocr_pdf.ps1). Its output is committed under sources/ocr/ rather than
build/, because it is slow to produce and Windows-only to reproduce;
tools/extract_text.py then uses it for any page whose text layer is empty.

A document is OCR'd when at least 30% of its pages have no usable text layer (under
20 characters) in build/fulltext.json -- a per-page test, because a typed cover sheet
stapled to scanned rule pages defeats any whole-document average. Documents already
OCR'd are skipped.

Usage:
    python tools/extract_text.py      # first, to find the scanned documents
    python tools/ocr_sources.py       # OCR them (Windows only)
    python tools/extract_text.py      # again, to merge the OCR text in
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FULLTEXT = ROOT / "build" / "fulltext.json"
OCR_DIR = ROOT / "sources" / "ocr"
PS1 = ROOT / "tools" / "ocr_pdf.ps1"


def main() -> int:
    if sys.platform != "win32":
        print("OCR uses the Windows OCR engine; run this on Windows (existing sources/ocr/ text is still used)")
        return 2
    if not FULLTEXT.exists():
        print("no build/fulltext.json -- run tools/extract_text.py first")
        return 1
    docs = json.loads(FULLTEXT.read_text("utf-8"))
    todo = []
    for slug, doc in docs.items():
        pages = doc["pages"]
        if not pages or (OCR_DIR / f"{slug}.txt").exists():
            continue
        # Per-page test: a typed cover sheet stapled to scanned rule pages has plenty of
        # text on average but none where it matters, so count pages without a text layer.
        empty = sum(1 for p in pages if not p.get("ocr") and len(p["text"]) < 20)
        if empty / len(pages) >= 0.3:
            todo.append((slug, doc["local_path"]))
    print(f"{len(todo)} scanned document(s) to OCR")
    failed = 0
    for i, (slug, lp) in enumerate(todo, 1):
        out = OCR_DIR / f"{slug}.txt"
        cmd = ["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", str(PS1),
               "-PdfPath", str(ROOT / "kb" / lp), "-OutPath", str(out)]
        r = subprocess.run(cmd, capture_output=True, text=True)
        if r.returncode != 0 or not out.exists():
            failed += 1
            print(f"  [{i}/{len(todo)}] FAILED {slug}: {(r.stderr or r.stdout).strip().splitlines()[-1:]}")
        else:
            print(f"  [{i}/{len(todo)}] {slug}: {r.stdout.strip()}")
        sys.stdout.flush()
    print(f"done: {len(todo) - failed} ok, {failed} failed")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
