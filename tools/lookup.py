"""Find a phrase across the extracted source text and print slug:page hits.

Works off build/fulltext.json (run tools/extract_text.py first), so it is fast enough
to use while writing. For a one-off search of a PDF not yet catalogued, use
tools/pdf_grep.py, which reads the PDFs directly.

Usage:
    python tools/lookup.py "board lot"                    # literal phrase, case-insensitive
    python tools/lookup.py -r "pre-?open"                 # regex
    python tools/lookup.py "static threshold" -s pse-revised-trading-rules
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FULLTEXT = ROOT / "build" / "fulltext.json"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("query")
    ap.add_argument("-r", "--regex", action="store_true")
    ap.add_argument("-s", "--slug", action="append", help="restrict to these slugs")
    ap.add_argument("-C", "--context", type=int, default=140)
    args = ap.parse_args()

    if not FULLTEXT.exists():
        print("no build/fulltext.json -- run tools/extract_text.py first")
        return 1
    docs = json.loads(FULLTEXT.read_text("utf-8"))
    pat = re.compile(args.query if args.regex else re.escape(args.query), re.I)
    hits = 0
    for slug, doc in docs.items():
        if args.slug and slug not in args.slug:
            continue
        for page in doc["pages"]:
            flat = re.sub(r"\s+", " ", page["text"])
            for m in pat.finditer(flat):
                a, b = max(0, m.start() - args.context), min(len(flat), m.end() + args.context)
                print(f"[^{slug}:{page['page']}]  ...{flat[a:b]}...")
                hits += 1
    print(f"\n{hits} hit(s)")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
