"""Collect the "## Source catalog" YAML blocks from the research notes into sources/catalog.yaml.

Each research note ends with a YAML list of the sources it relied on. This merges them
by slug into the single source registry the build resolves citations against, and adds
a stub for any archived file in kb/pdfs/ that no note claimed -- so nothing on disk is
silently uncatalogued.

Merging rules for a slug reported by several notes:
  * a real local_path beats null; a concrete date beats "undated";
  * two different concrete dates are a conflict: the later is kept and the conflict is
    written into the entry's note, to be resolved by reading the document's cover;
  * notes are concatenated (deduplicated).

Entries already present in sources/catalog.yaml are preserved and take precedence, so
hand corrections survive a re-run. Use --fresh to rebuild from the notes alone.

Usage:
    python tools/collect_sources.py                 # merge notes into the existing catalog
    python tools/collect_sources.py --fresh         # rebuild from notes only
    python tools/collect_sources.py --dry-run       # report, write nothing
    python tools/collect_sources.py --fold-pending  # fold sources/pending/*.yaml into the catalog
"""

from __future__ import annotations

import re
import sys
from datetime import date, datetime
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
NOTES = ROOT / "research_notes"
CATALOG = ROOT / "sources" / "catalog.yaml"
PDFS = ROOT / "kb" / "pdfs"

FIELDS = ["slug", "title", "publisher", "type", "canonical_url", "local_path", "edition",
          "amended_through", "chapters", "note"]
TYPE_MAP = {"html": "web", "webpage": "web", "web page": "web", "article": "web", "news": "web",
            "press release": "web", "report": "pdf", "law": "pdf", "journal": "paper", "data": "dataset"}
EDITION_MAP = {"in force": "in-force", "inforce": "in-force", "current": "in-force", "in_force": "in-force",
               "historic": "historical", "na": "n/a", "none": "n/a", "": "n/a", "superceded": "superseded",
               "draft": "historical", "proposed": "historical"}


def slugify(s: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", str(s).lower()).strip("-")
    return s or "source"


def norm_date(v):
    if v is None:
        return None
    if isinstance(v, (date, datetime)):
        return v.strftime("%Y-%m-%d")
    s = str(v).strip()
    if not s or s.lower() in ("null", "none", "n/a", "unknown"):
        return None
    if s.lower() == "undated":
        return "undated"
    m = re.match(r"^(\d{4})(?:-(\d{1,2}))?(?:-(\d{1,2}))?", s)
    if m:
        y, mo, d = m.group(1), m.group(2), m.group(3)
        return y + (f"-{int(mo):02d}" if mo else "") + (f"-{int(d):02d}" if d else "")
    return s


def norm_local(lp):
    if not lp or str(lp).strip().lower() in ("null", "none", ""):
        return None
    name = Path(str(lp).replace("\\", "/")).name
    return f"pdfs/{name}"


def extract_blocks(text: str) -> list:
    """Return the YAML list(s) that follow a '## Source catalog' heading."""
    m = re.search(r"^#{2,3}\s*Source catalog[^\n]*\n", text, re.I | re.M)
    if not m:
        return []
    rest = text[m.end():]
    nxt = re.search(r"^##\s+(?!#)", rest, re.M)
    if nxt:
        rest = rest[: nxt.start()]
    fenced = re.findall(r"```(?:ya?ml)?\s*\n(.*?)```", rest, re.S)
    chunks = fenced or [rest]
    items: list = []
    for chunk in chunks:
        try:
            data = yaml.safe_load(chunk)
        except yaml.YAMLError as exc:
            print(f"    yaml error: {str(exc).splitlines()[0]}")
            continue
        if isinstance(data, dict) and "sources" in data:
            data = data["sources"]
        if isinstance(data, list):
            items.extend(x for x in data if isinstance(x, dict))
    return items


def normalise(e: dict, origin: str) -> dict | None:
    slug = e.get("slug")
    if not slug:
        return None
    out = {k: e.get(k) for k in FIELDS if e.get(k) is not None}
    out["slug"] = slugify(slug)
    t = str(out.get("type", "web")).strip().lower()
    out["type"] = TYPE_MAP.get(t, t if t in ("pdf", "web", "paper", "dataset") else "web")
    out["local_path"] = norm_local(e.get("local_path"))
    if out["local_path"] and out["local_path"].lower().endswith(".pdf"):
        out["type"] = "pdf" if out["type"] != "paper" else "paper"
    ed = str(out.get("edition", "n/a")).strip().lower()
    out["edition"] = EDITION_MAP.get(ed, ed if ed in ("in-force", "superseded", "historical", "n/a") else "n/a")
    out["amended_through"] = norm_date(e.get("amended_through") or e.get("effective") or e.get("date"))
    out["_origin"] = {origin}
    return out


def merge(a: dict, b: dict) -> dict:
    for k in ("title", "publisher", "canonical_url"):
        if not a.get(k) and b.get(k):
            a[k] = b[k]
    if not a.get("local_path") and b.get("local_path"):
        a["local_path"] = b["local_path"]
        a["type"] = b["type"]
    da, db = a.get("amended_through"), b.get("amended_through")
    if db and db != "undated":
        if not da or da == "undated":
            a["amended_through"] = db
        elif da != db:
            later = max(da, db)
            a["amended_through"] = later
            conflict = f"[date conflict between notes: {da} vs {db}; kept {later} -- verify against the cover]"
            if conflict not in (a.get("note") or ""):
                a["note"] = ((a.get("note") or "") + " " + conflict).strip()
    if (a.get("edition") in (None, "n/a")) and b.get("edition") not in (None, "n/a"):
        a["edition"] = b["edition"]
    nb = (b.get("note") or "").strip()
    if nb and nb not in (a.get("note") or ""):
        a["note"] = ((a.get("note") or "") + " | " + nb).strip(" |")
    a["_origin"] |= b["_origin"]
    return a


class Dumper(yaml.SafeDumper):
    pass


Dumper.add_representer(str, lambda d, s: d.represent_scalar("tag:yaml.org,2002:str", s, style="|" if "\n" in s else None))


SYNCED = ("status", "bytes", "sha256", "page_count", "fetch_route")


def fold_pending() -> int:
    """Fold sources/pending/*.yaml fragments (written by concurrent authors) into the catalog."""
    pending = sorted((ROOT / "sources" / "pending").glob("*.yaml"))
    if not pending:
        print("no pending fragments")
        return 0
    data = yaml.safe_load(CATALOG.read_text("utf-8")) or {}
    entries = data.get("sources", [])
    index = {e["slug"]: e for e in entries}
    added = updated = 0
    for frag in pending:
        fdata = yaml.safe_load(frag.read_text("utf-8")) or []
        if isinstance(fdata, dict):
            fdata = fdata.get("sources", [])
        for e in fdata:
            if not isinstance(e, dict) or not e.get("slug"):
                continue
            e = {k: v for k, v in e.items() if k not in SYNCED}
            if e.get("amended_through") is not None:
                e["amended_through"] = norm_date(e["amended_through"])
            if e["slug"] in index:
                index[e["slug"]].update(e)
                updated += 1
            else:
                entries.append(e)
                index[e["slug"]] = e
                added += 1
        done = ROOT / "build" / "pending-folded"
        done.mkdir(parents=True, exist_ok=True)
        frag.replace(done / frag.name)
    data["sources"] = entries
    CATALOG.write_text(
        "# Source registry: one entry per document. Citations in content/ resolve against `slug`.\n"
        "# status/bytes/sha256/page_count are written by tools/sync_sources.py -- do not hand-edit them.\n"
        + yaml.dump(data, Dumper=Dumper, sort_keys=False, allow_unicode=True, width=110), "utf-8")
    print(f"folded {len(pending)} fragment(s): {added} added, {updated} updated -- now run tools/sync_sources.py")
    return 0


def main() -> int:
    if "--fold-pending" in sys.argv:
        return fold_pending()
    fresh, dry = "--fresh" in sys.argv, "--dry-run" in sys.argv
    merged: dict[str, dict] = {}
    for note in sorted(NOTES.rglob("*.md")):
        items = extract_blocks(note.read_text("utf-8", errors="replace"))
        print(f"  {note.parent.name}/{note.name}: {len(items)} catalog entries")
        for raw in items:
            e = normalise(raw, note.stem)
            if not e:
                continue
            merged[e["slug"]] = merge(merged[e["slug"]], e) if e["slug"] in merged else e

    existing: dict[str, dict] = {}
    if CATALOG.exists() and not fresh:
        for s in (yaml.safe_load(CATALOG.read_text("utf-8")) or {}).get("sources", []):
            existing[s["slug"]] = s

    # Archived files nobody catalogued get a stub, so the gap is visible.
    by_path = {e["local_path"] for e in list(merged.values()) + list(existing.values()) if e.get("local_path")}
    stubs = 0
    for p in sorted(PDFS.glob("*.pdf")):
        lp = f"pdfs/{p.name}"
        if lp in by_path:
            continue
        slug = slugify(p.stem)
        if slug in merged or slug in existing:
            (existing.get(slug) or merged[slug])["local_path"] = lp
            continue
        merged[slug] = {"slug": slug, "title": p.stem, "publisher": "UNKNOWN", "type": "pdf", "canonical_url": None,
                        "local_path": lp, "edition": "n/a", "amended_through": "undated",
                        "note": "STUB: archived by research but not catalogued -- fill in title/publisher/date or remove.",
                        "_origin": {"stub"}}
        stubs += 1

    final: list[dict] = []
    for slug, e in merged.items():
        if slug in existing:
            continue
        e = {k: e[k] for k in FIELDS if k in e and e[k] is not None} | {"local_path": e.get("local_path")}
        e.setdefault("title", slug)
        e.setdefault("publisher", "UNKNOWN")
        final.append({k: e.get(k) for k in FIELDS if k in e})
    out = list(existing.values()) + final

    missing_files = [e["slug"] for e in out if e.get("local_path") and not (ROOT / "kb" / e["local_path"]).exists()]
    print(f"\nentries        {len(out)}  ({len(existing)} kept from catalog, {len(final)} from notes, {stubs} stubs)")
    print(f"archived       {sum(1 for e in out if e.get('local_path'))}")
    print(f"date conflicts {sum(1 for e in out if 'date conflict' in (e.get('note') or ''))}")
    if missing_files:
        print(f"local_path set but file absent: {', '.join(missing_files)}")
    if not dry:
        CATALOG.parent.mkdir(parents=True, exist_ok=True)
        CATALOG.write_text(
            "# Source registry: one entry per document. Citations in content/ resolve against `slug`.\n"
            "# status/bytes/sha256/page_count are written by tools/sync_sources.py -- do not hand-edit them.\n"
            + yaml.dump({"sources": out}, Dumper=Dumper, sort_keys=False, allow_unicode=True, width=110),
            "utf-8",
        )
        print(f"wrote {CATALOG.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
