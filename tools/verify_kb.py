"""Static consistency checks over the built kb/ bundle, the catalog and the archive.

build_kb.py refuses to build from bad inputs; this checks the *output* and the archive
as shipped, so a stale or hand-edited bundle is caught too.

Fails (exit 1) when:
  * the page would not run from file:// (module scripts, remote scripts, fetch/XHR use);
  * a data file is missing, malformed, or not a classic script assigning its global;
  * an archived file is missing or its sha256 no longer matches the catalog;
  * a reference names an unknown source, or a page past the end of its document;
  * a cross-chapter link points at an unknown chapter, section or reference;
  * two search documents share an id (MiniSearch would refuse the whole corpus);
  * the bundle is older than content/ or the catalog (forgot to rebuild).
Warns on: uncited sources, uncatalogued archive files, placeholder text, not-archived PDFs.

Usage:  python tools/verify_kb.py
"""

from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
KB = ROOT / "kb"
CONTENT = ROOT / "content"
CATALOG = ROOT / "sources" / "catalog.yaml"

errors: list[str] = []
warnings: list[str] = []


def err(msg: str) -> None:
    errors.append(msg)


def warn(msg: str) -> None:
    warnings.append(msg)


def load_global(path: Path, name: str):
    if not path.exists():
        err(f"{path.relative_to(ROOT)} missing -- run tools/build_kb.py")
        return None
    raw = path.read_text("utf-8")
    prefix = f"window.{name} = JSON.parse("
    if not raw.startswith(prefix) or not raw.rstrip().endswith(");"):
        err(f"{path.relative_to(ROOT)} is not a classic script assigning window.{name}")
        return None
    literal = raw[len(prefix): raw.rstrip().rfind(");")]
    try:
        return json.loads(json.loads(literal.replace("<\\/script", "</script").replace("<\\!--", "<!--")))
    except Exception as exc:
        err(f"{path.relative_to(ROOT)} does not decode: {exc}")
        return None


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def check_page_shell() -> None:
    html = (KB / "index.html").read_text("utf-8")
    for m in re.finditer(r"<script\b([^>]*)>", html, re.I):
        attrs = m.group(1)
        if re.search(r'type\s*=\s*["\']module', attrs, re.I):
            err("index.html loads an ES module -- blocked at file://")
        src = re.search(r'src\s*=\s*["\']([^"\']+)', attrs)
        if src:
            if re.match(r"(?i)https?:|//", src.group(1)):
                err(f"index.html loads a remote script ({src.group(1)}) -- the KB must work offline")
            elif not (KB / src.group(1)).exists():
                err(f"index.html references missing script {src.group(1)}")
    for m in re.finditer(r'<link\b[^>]*href\s*=\s*["\']([^"\']+)', html, re.I):
        if re.match(r"(?i)https?:|//", m.group(1)):
            err(f"index.html loads a remote stylesheet ({m.group(1)})")
    js = (KB / "assets" / "app.js").read_text("utf-8")
    for bad in ("fetch(", "XMLHttpRequest", "import("):
        if bad in js:
            err(f"app.js uses {bad!r} -- blocked at file://")


def main() -> int:
    check_page_shell()
    data = load_global(KB / "data" / "kb-chapters.js", "KB_CHAPTERS")
    ft = load_global(KB / "data" / "kb-fulltext.js", "KB_FULLTEXT")
    catalog = {s["slug"]: s for s in (yaml.safe_load(CATALOG.read_text("utf-8")) or {}).get("sources", [])}

    # ---- archive integrity
    claimed = set()
    for slug, s in catalog.items():
        lp = s.get("local_path")
        if not lp:
            if s.get("type") == "pdf":
                warn(f"source '{slug}' is a PDF that is not archived locally")
            continue
        p = KB / lp
        claimed.add(p.resolve())
        if not p.exists():
            err(f"source '{slug}': archived file {lp} is missing")
        elif s.get("sha256") and sha256(p) != s["sha256"]:
            err(f"source '{slug}': {lp} sha256 differs from catalog -- re-run tools/sync_sources.py")
        elif not s.get("sha256"):
            err(f"source '{slug}': no sha256 recorded -- run tools/sync_sources.py")
    for p in sorted((KB / "pdfs").glob("*")):
        if p.is_file() and p.resolve() not in claimed:
            warn(f"archived file not in catalog: pdfs/{p.name}")

    if data is None:
        return report()

    # ---- staleness of the bundle itself
    bundle_mtime = (KB / "data" / "kb-chapters.js").stat().st_mtime
    newest_input = max([p.stat().st_mtime for p in CONTENT.glob("*.md")] + [CATALOG.stat().st_mtime])
    if newest_input > bundle_mtime + 1:
        err("kb/data/kb-chapters.js is older than content/ or the catalog -- re-run tools/build_kb.py")

    # ---- chapters, references, links
    chapters = data["chapters"]
    md_files = list(CONTENT.glob("*.md"))
    if len(chapters) != len(md_files):
        err(f"bundle has {len(chapters)} chapters but content/ has {len(md_files)} files")
    anchors = {c["slug"]: {s["anchor"] for s in c["sections"]} | {f"ref-{r['n']}" for r in c["references"]}
               for c in chapters}
    cited: set[str] = set()
    for c in chapters:
        if "[^" in c["html"]:
            err(f"chapter {c['number']} contains an unresolved citation marker")
        if re.search(r"\b(TODO|TBD|FIXME|XXX|lorem ipsum)\b", c["html"]):
            warn(f"chapter {c['number']} contains placeholder text")
        for r in c["references"]:
            s = catalog.get(r["slug"])
            cited.add(r["slug"])
            if s is None:
                err(f"chapter {c['number']}: reference to unknown source '{r['slug']}'")
                continue
            first = (r.get("page") or "").split("-")[-1]
            if first.isdigit() and s.get("page_count") and int(first) > int(s["page_count"]):
                err(f"chapter {c['number']}: [^{r['slug']}:{r['page']}] beyond {s['page_count']} pages")
        for slug, anchor in re.findall(r'href="#/ch/([a-z0-9-]+)(?:/([a-z0-9-]+))?"', c["html"]):
            if slug not in anchors:
                err(f"chapter {c['number']}: link to unknown chapter '{slug}'")
            elif anchor and not anchor.startswith("cite-") and anchor not in anchors[slug]:
                err(f"chapter {c['number']}: link to unknown anchor '#/ch/{slug}/{anchor}'")
    for slug in sorted(set(catalog) - cited):
        warn(f"source '{slug}' is catalogued but never cited")

    # ---- search corpus
    ids = [d["id"] for d in data["searchDocs"]] + [d["id"] for d in (ft or [])]
    if len(ids) != len(set(ids)):
        dupes = sorted({i for i in ids if ids.count(i) > 1})
        err(f"duplicate search ids: {dupes[:5]}")

    print(f"chapters {len(chapters)} · references {sum(len(c['references']) for c in chapters)} · "
          f"sources {len(catalog)} ({len(cited)} cited) · search docs {len(ids)}")
    return report()


def report() -> int:
    for w in warnings:
        print(f"  warn: {w}")
    for e in errors:
        print(f"  FAIL: {e}")
    print("\nverify " + ("FAILED" if errors else "ok") + f" ({len(errors)} errors, {len(warnings)} warnings)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
