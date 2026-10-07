"""Reconcile sources/catalog.yaml with the archived documents in kb/pdfs/.

For every catalog entry with a local_path this records what is actually on disk --
status, bytes, sha256, page_count -- so that the build can refuse citations that point
at missing files or past the last page. It also reports archived files that no catalog
entry claims (orphans), and can try to fetch missing documents.

Fetch routes, in order: the publisher's URL with a browser User-Agent ("direct"), then
the Internet Archive's raw replay of the same URL ("wayback"). www.sec.gov.ph and
www.sccp.com.ph answer 403 to every non-browser client, so for those the archive is
usually the only automated route.

Usage:
    python tools/sync_sources.py            # reconcile only (safe to re-run)
    python tools/sync_sources.py --fetch    # also try to download missing documents
"""

from __future__ import annotations

import hashlib
import sys
import time
from datetime import date, datetime
from pathlib import Path

import requests
import yaml
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parent.parent
CATALOG = ROOT / "sources" / "catalog.yaml"
KB = ROOT / "kb"
PDFS = KB / "pdfs"
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def pdf_pages(path: Path) -> int | None:
    try:
        return len(PdfReader(str(path)).pages)
    except Exception:
        return None


def try_fetch(url: str, dest: Path) -> str | None:
    """Download url to dest; return the route that worked, or None."""
    routes = [("direct", url), ("wayback", f"https://web.archive.org/web/2026id_/{url}")]
    for route, u in routes:
        for attempt in range(3):
            try:
                r = requests.get(u, headers={"User-Agent": UA}, timeout=60, allow_redirects=True)
            except requests.RequestException:
                break
            if r.status_code == 429:
                time.sleep(10 * (attempt + 1))
                continue
            if r.status_code == 200 and r.content[:5] == b"%PDF-":
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_bytes(r.content)
                return route
            break
    return None


class Dumper(yaml.SafeDumper):
    pass


def _str_presenter(dumper, data):
    style = "|" if "\n" in data else None
    return dumper.represent_scalar("tag:yaml.org,2002:str", data, style=style)


Dumper.add_representer(str, _str_presenter)


def main() -> int:
    fetch = "--fetch" in sys.argv
    data = yaml.safe_load(CATALOG.read_text("utf-8")) or {}
    sources = data.get("sources", [])
    claimed: set[str] = set()
    counts = {"ok": 0, "missing": 0, "not-archived": 0, "web": 0, "fetched": 0}

    for s in sources:
        for k in ("amended_through", "accessed"):
            if isinstance(s.get(k), (date, datetime)):
                s[k] = s[k].strftime("%Y-%m-%d")
        lp = s.get("local_path")
        if not lp:
            if s.get("type") == "pdf":
                s["status"] = "not-archived"
                counts["not-archived"] += 1
            else:
                s["status"] = "web"
                counts["web"] += 1
            for k in ("sha256", "bytes", "page_count"):
                s.pop(k, None)
            continue
        path = KB / lp
        claimed.add(path.resolve().as_posix().lower())
        if not path.exists() and fetch and s.get("canonical_url"):
            route = try_fetch(s["canonical_url"], path)
            if route:
                s["fetch_route"] = route
                s["fetched_by_sync"] = True
                counts["fetched"] += 1
                print(f"  fetched {s['slug']} via {route}")
        if not path.exists():
            s["status"] = "missing"
            counts["missing"] += 1
            print(f"  MISSING {s['slug']}: {lp}")
            continue
        is_pdf = path.suffix.lower() == ".pdf"
        if is_pdf and path.read_bytes()[:5] != b"%PDF-":
            s["status"] = "corrupt"
            counts["missing"] += 1
            print(f"  CORRUPT {s['slug']}: {lp} is not a PDF (an HTML error page saved as .pdf?)")
            continue
        s["status"] = "ok"
        s["bytes"] = path.stat().st_size
        s["sha256"] = sha256(path)
        if is_pdf:
            n = pdf_pages(path)
            if n is None:
                s["status"] = "corrupt"
                counts["missing"] += 1
                print(f"  UNREADABLE {s['slug']}: {lp}")
                continue
            s["page_count"] = n
        # fetch_route is recorded only when this script downloaded the file itself; the
        # research pass archived most documents by hand-picked routes it did not log, and an
        # invented "direct" would misstate provenance.
        if s.get("fetch_route") == "direct" and not s.get("fetched_by_sync"):
            s.pop("fetch_route", None)
        counts["ok"] += 1

    orphans = [p for p in sorted(PDFS.glob("*")) if p.is_file() and p.resolve().as_posix().lower() not in claimed]

    CATALOG.write_text(
        "# Source registry: one entry per document. Citations in content/ resolve against `slug`.\n"
        "# status/bytes/sha256/page_count are written by tools/sync_sources.py -- do not hand-edit them.\n"
        + yaml.dump(data, Dumper=Dumper, sort_keys=False, allow_unicode=True, width=110),
        "utf-8",
    )
    print(f"catalog entries   {len(sources)}")
    print(f"  archived ok     {counts['ok']}")
    print(f"  missing/corrupt {counts['missing']}")
    print(f"  pdf not archived {counts['not-archived']}")
    print(f"  web/other       {counts['web']}")
    if fetch:
        print(f"  fetched now     {counts['fetched']}")
    if orphans:
        print(f"orphans (archived but uncatalogued): {len(orphans)}")
        for p in orphans:
            print(f"  {p.relative_to(KB).as_posix()}")
    return 1 if counts["missing"] else 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
