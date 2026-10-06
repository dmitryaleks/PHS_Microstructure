"""Load the real kb/index.html at a real file:// origin in headless Chrome and check
that every route renders -- the failure modes static checks cannot see (a blank page
from a blocked load, a search index that refuses its corpus, a link that lands on
the wrong view).

Each route is loaded with --dump-dom after a virtual-time budget, so the lazy
full-text load and the asynchronous index build complete before the DOM is read.
A throwaway --user-data-dir keeps the run isolated from any Chrome the user has open.

Checks:
  * home renders the contents grid with one card per chapter;
  * every chapter renders its title and exactly its number of references;
  * deep links to a section and to a reference land on an existing element;
  * the source library lists every catalogued source;
  * a search returns chapter hits and, when source text exists, source-page hits.

Usage:  python tools/smoke_test.py [--chrome PATH] [--query "board lot"]
"""

from __future__ import annotations

import argparse
import html as htmllib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
KB = ROOT / "kb"
CANDIDATES = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe"),
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/usr/bin/google-chrome", "/usr/bin/chromium", "/usr/bin/chromium-browser",
]


def load_data() -> dict:
    raw = (KB / "data" / "kb-chapters.js").read_text("utf-8")
    literal = raw[raw.index("JSON.parse(") + len("JSON.parse("): raw.rstrip().rfind(");")]
    return json.loads(json.loads(literal.replace("<\\/script", "</script").replace("<\\!--", "<!--")))


def dump(chrome: str, profile: str, hash_route: str, budget_ms: int = 8000) -> str:
    url = (KB / "index.html").resolve().as_uri() + hash_route
    cmd = [chrome, "--headless=new", "--disable-gpu", "--no-first-run", "--no-default-browser-check",
           f"--user-data-dir={profile}", f"--virtual-time-budget={budget_ms}", "--dump-dom", url]
    out = subprocess.run(cmd, capture_output=True, timeout=120)
    return out.stdout.decode("utf-8", "replace")


def text_of(fragment: str) -> str:
    return re.sub(r"\s+", " ", htmllib.unescape(re.sub(r"<[^>]+>", " ", fragment))).strip()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--chrome")
    ap.add_argument("--query", default="settlement")
    args = ap.parse_args()
    chrome = args.chrome or next((c for c in CANDIDATES if Path(c).exists()), None) or shutil.which("chrome")
    if not chrome:
        print("no Chrome/Chromium/Edge found -- pass --chrome PATH")
        return 2

    data = load_data()
    failures: list[str] = []
    profile = tempfile.mkdtemp(prefix="kb-smoke-")
    checks = 0

    def expect(cond: bool, msg: str) -> None:
        nonlocal checks
        checks += 1
        if not cond:
            failures.append(msg)
            print(f"  FAIL {msg}")

    try:
        dom = dump(chrome, profile, "#/")
        expect('data-ready="1"' in dom, "home: app did not finish initialising")
        expect(dom.count('class="card"') == len(data["chapters"]), "home: card count != chapter count")

        for c in data["chapters"]:
            dom = dump(chrome, profile, f"#/ch/{c['slug']}")
            h1 = re.search(r"<h1>(.*?)</h1>", dom, re.S)
            expect(bool(h1) and text_of(h1.group(1)) == htmllib.unescape(c["title"]),
                   f"ch {c['number']}: title not rendered")
            n_refs = len(re.findall(r'<li id="ref-\d+"', dom))
            expect(n_refs == len(c["references"]), f"ch {c['number']}: {n_refs} references rendered, expected {len(c['references'])}")
            if c["sections"]:
                a = c["sections"][-1]["anchor"]
                expect(f'id="{a}"' in dom, f"ch {c['number']}: section anchor '{a}' missing")
            print(f"  ok  ch {c['number']:>2} {c['slug']}  ({n_refs} refs)")

        dom = dump(chrome, profile, "#/sources")
        n_src = len(re.findall(r'<div class="src" id="src-', dom))
        expect(n_src == len(data["sources"]), f"sources: {n_src} rendered, expected {len(data['sources'])}")

        dom = dump(chrome, profile, "#/search/" + args.query.replace(" ", "%20"), budget_ms=20000)
        ch_hits = re.search(r"Chapters \((\d+)\)", dom)
        expect(bool(ch_hits) and int(ch_hits.group(1)) > 0, f"search '{args.query}': no chapter results")
        ft_size = (KB / "data" / "kb-fulltext.js").stat().st_size
        if ft_size > 200:
            expect('data-ft="ready"' in dom, "search: full-text index never became ready")
            src_hits = re.search(r"Source documents \((\d+)\)", dom)
            expect(bool(src_hits) and int(src_hits.group(1)) > 0, f"search '{args.query}': no source-document results")
    finally:
        shutil.rmtree(profile, ignore_errors=True)

    print(f"\nsmoke test {'FAILED' if failures else 'ok'}: {checks - len(failures)}/{checks} checks passed")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
