"""Collapse byte-identical documents in kb/pdfs/ onto one canonical slug.

Researchers working in parallel sometimes archive the same PDF under two names
(e.g. pse-cn-2022-0010.pdf and pse-cn-2022-0010-edge-cutoff-330pm.pdf). Two slugs for
one document split its citations and double-count it in the source library, so this
picks one canonical slug per SHA-256 and rewrites every reference to the others:

  * [^dup:N] / [^dup] citations and `slug: dup` lines in research_notes/ and content/;
  * pdfs/dup.pdf paths in those files and in sources/catalog.yaml (duplicate entries
    are dropped, their notes merged into the canonical entry).

The canonical name is the shortest stem (ties broken alphabetically) -- usually the
bare document identifier. Duplicates are moved to build/dupes/, not deleted.

Usage:
    python tools/dedupe_archive.py            # report only
    python tools/dedupe_archive.py --apply    # rewrite references and move duplicates
"""

from __future__ import annotations

import hashlib
import re
import shutil
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
PDFS = ROOT / "kb" / "pdfs"
CATALOG = ROOT / "sources" / "catalog.yaml"
DUPES = ROOT / "build" / "dupes"
TEXT_ROOTS = [ROOT / "research_notes", ROOT / "content"]


def sha256(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    apply = "--apply" in sys.argv
    groups: dict[str, list[Path]] = {}
    for p in sorted(PDFS.glob("*")):
        if p.is_file():
            groups.setdefault(sha256(p), []).append(p)
    mapping: dict[str, str] = {}
    for files in groups.values():
        if len(files) < 2:
            continue
        stems = sorted((f.stem for f in files), key=lambda s: (len(s), s))
        canon = stems[0]
        for s in stems[1:]:
            mapping[s] = canon
    if not mapping:
        print("no duplicates")
        return 0
    for dup, canon in sorted(mapping.items()):
        print(f"  {dup}  ->  {canon}")
    if not apply:
        print(f"\n{len(mapping)} duplicate(s); re-run with --apply to rewrite references and move them")
        return 0

    # 1. rewrite references in notes and chapters
    pats = [(re.compile(r"\[\^" + re.escape(d) + r"(?=[:\]])"), "[^" + c) for d, c in mapping.items()]
    pats += [(re.compile(r"(slug:\s*['\"]?)" + re.escape(d) + r"(?=['\"]?\s*$)", re.M), r"\g<1>" + c) for d, c in mapping.items()]
    pats += [(re.compile(r"pdfs[/\\]" + re.escape(d) + r"\.pdf"), "pdfs/" + c + ".pdf") for d, c in mapping.items()]
    changed = 0
    for root in TEXT_ROOTS:
        for f in root.rglob("*.md"):
            text = f.read_text("utf-8", errors="replace")
            new = text
            for pat, rep in pats:
                new = pat.sub(rep, new)
            if new != text:
                f.write_text(new, "utf-8")
                changed += 1
    print(f"rewrote references in {changed} file(s)")

    # 2. merge catalog entries
    if CATALOG.exists():
        data = yaml.safe_load(CATALOG.read_text("utf-8")) or {}
        by_slug = {s["slug"]: s for s in data.get("sources", [])}
        kept = []
        for s in data.get("sources", []):
            canon = mapping.get(s["slug"])
            if canon:
                target = by_slug.get(canon)
                if target is not None:
                    extra = (s.get("note") or "").strip()
                    if extra and extra not in (target.get("note") or ""):
                        target["note"] = ((target.get("note") or "") + " | " + extra).strip(" |")
                    continue
                s["slug"] = canon
                s["local_path"] = f"pdfs/{canon}.pdf"
            kept.append(s)
        data["sources"] = kept
        CATALOG.write_text(
            "# Source registry: one entry per document. Citations in content/ resolve against `slug`.\n"
            "# status/bytes/sha256/page_count are written by tools/sync_sources.py -- do not hand-edit them.\n"
            + yaml.safe_dump(data, sort_keys=False, allow_unicode=True, width=110), "utf-8")
        print("merged catalog entries")

    # 3. move the duplicate files aside
    DUPES.mkdir(parents=True, exist_ok=True)
    for dup in mapping:
        src = PDFS / f"{dup}.pdf"
        if src.exists():
            shutil.move(str(src), str(DUPES / src.name))
    print(f"moved {len(mapping)} duplicate file(s) to {DUPES.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
