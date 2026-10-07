"""Regenerate the generated sections of README.md from the chapters and the source catalog.

README.md carries two marked regions that would otherwise drift out of date:

    <!-- CONTENTS:START --> ... <!-- CONTENTS:END -->       chapter table
    <!-- PROVENANCE:START --> ... <!-- PROVENANCE:END -->   source and archive statistics

Everything outside the markers is hand-written and left untouched.

Usage:  python tools/update_readme.py
"""

from __future__ import annotations

import collections
import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"
CONTENT = ROOT / "content"
CATALOG = ROOT / "sources" / "catalog.yaml"
OCR_DIR = ROOT / "sources" / "ocr"
FULLTEXT = ROOT / "build" / "fulltext.json"
CITE = re.compile(r"\[\^([a-z0-9][a-z0-9-]*)(?::[0-9ivxlc-]+)?\]", re.I)
FRONT = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n", re.S)


def chapters() -> list[dict]:
    out = []
    for p in sorted(CONTENT.glob("*.md")):
        raw = p.read_text("utf-8")
        m = FRONT.match(raw)
        meta = yaml.safe_load(m.group(1))
        body = raw[m.end():]
        out.append({**meta, "file": p.name, "kb": len(raw.encode("utf-8")) / 1024,
                    "cites": len(CITE.findall(body)), "slugs": set(s.lower() for s in CITE.findall(body))})
    return sorted(out, key=lambda c: c["number"])


def contents(chs: list[dict]) -> str:
    rows = ["| # | Chapter | What it settles | KB | Citations |", "|---|---|---|---|---|"]
    for c in chs:
        rows.append(f"| {c['number']:02d} | [{c['title']}](content/{c['file']}) | {c['summary']} | "
                    f"{c['kb']:.0f} | {c['cites']} |")
    total_kb = sum(c["kb"] for c in chs)
    total_cites = sum(c["cites"] for c in chs)
    rows.append(f"| | **{len(chs)} chapters** | | **{total_kb:,.0f}** | **{total_cites:,}** |")
    return "## Contents\n\n" + "\n".join(rows) + "\n"


def provenance(chs: list[dict]) -> str:
    srcs = (yaml.safe_load(CATALOG.read_text("utf-8")) or {}).get("sources", [])
    cited = set().union(*(c["slugs"] for c in chs)) if chs else set()
    by_type = collections.Counter(s.get("type") for s in srcs)
    archived = [s for s in srcs if s.get("status") == "ok"]
    arch_bytes = sum(s.get("bytes") or 0 for s in archived)
    pages = sum(s.get("page_count") or 0 for s in archived)
    cited_archived = sum(1 for s in archived if s["slug"] in cited)
    eds = collections.Counter((s.get("edition") or "n/a") for s in srcs if s["slug"] in cited)
    pubs = collections.Counter(s.get("publisher") for s in srcs if s["slug"] in cited)
    ocr_docs = len(list(OCR_DIR.glob("*.txt")))
    ocr_pages = 0
    if FULLTEXT.exists():
        ft = json.loads(FULLTEXT.read_text("utf-8"))
        ocr_pages = sum(1 for d in ft.values() for p in d["pages"] if p.get("ocr"))
    lines = [
        "## Provenance", "",
        f"**{len(srcs)} sources catalogued, {len(cited & {s['slug'] for s in srcs})} cited.** "
        f"{len(archived)} documents are archived in `kb/pdfs/` ({arch_bytes / 1e6:,.0f} MB, {pages:,} pages), "
        f"{cited_archived} of them cited; every archived file's SHA-256 and page count is recorded in "
        f"`sources/catalog.yaml` and re-checked by `verify_kb.py`. Uncited archived documents are kept "
        f"for completeness and appear in the source library.", "",
        "| Source type | Catalogued |", "|---|---|",
        *[f"| {t} | {n} |" for t, n in by_type.most_common()], "",
        "| Edition status of cited sources | Count |", "|---|---|",
        *[f"| {e} | {n} |" for e, n in eds.most_common()], "",
        "| Most-cited publishers | Sources cited |", "|---|---|",
        *[f"| {p} | {n} |" for p, n in pubs.most_common(12)], "",
        f"**Scanned documents.** {ocr_docs} archived PDFs are wholly or partly scanned. Their text was "
        f"recovered with the OCR engine built into Windows ({ocr_pages:,} pages, `sources/ocr/`), so "
        f"they are searchable and citable by page like any other source.", "",
        "**Retrieval notes.** `www.pse.com.ph` serves non-browser clients; `www.sec.gov.ph` and "
        "`www.sccp.com.ph` answer HTTP 403 to every non-browser client, and `edge.pse.com.ph` was "
        "intermittently unavailable (it failed on 19 Jan and 6 Oct 2026). Documents from those hosts "
        "came through PSE re-postings, the Internet Archive or other mirrors; citations link the "
        "canonical URL while the reference list opens the archived copy.",
    ]
    return "\n".join(lines) + "\n"


def splice(text: str, name: str, body: str) -> str:
    pat = re.compile(rf"(<!-- {name}:START -->)(.*?)(<!-- {name}:END -->)", re.S)
    if not pat.search(text):
        raise SystemExit(f"README.md has no {name} markers")
    return pat.sub(lambda m: f"{m.group(1)}\n{body}{m.group(3)}", text)


def main() -> int:
    chs = chapters()
    text = README.read_text("utf-8")
    text = splice(text, "CONTENTS", contents(chs))
    text = splice(text, "PROVENANCE", provenance(chs))
    README.write_text(text, "utf-8")
    print(f"README.md updated: {len(chs)} chapters")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
