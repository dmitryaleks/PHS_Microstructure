"""Compile authored chapters + the source catalog + extracted PDF text into the static kb/ bundle.

Two hard constraints shape this script:

  * The output must open from file://, where fetch(), XMLHttpRequest and ES-module
    imports are blocked by the opaque-origin rule. Every byte of data is therefore
    emitted as a classic script assigning a global (window.KB_CHAPTERS,
    window.KB_FULLTEXT) and loaded with a plain <script src>. Nothing is fetched.

  * Every factual claim must resolve to a real catalogued source, and a cited PDF page
    must exist. Unresolvable citations fail the build instead of becoming dead links.

Citation syntax in content/*.md (pages are PHYSICAL, 1-based -- what #page=N opens):

    [^slug:12]      page 12 of an archived PDF
    [^slug:12-14]   a page range (links to the first page)
    [^slug]         a whole document or web page

Cross-references between chapters:  [Chapter 4](#/ch/order-types)  or  (#/ch/order-types/tick-sizes)

Usage:  python tools/build_kb.py            # release build: every check is fatal
        python tools/build_kb.py --draft    # while authoring: links to unwritten chapters only warn
"""

from __future__ import annotations

import html as htmllib
import json
import re
import sys
import unicodedata
from dataclasses import dataclass, field
from datetime import date, datetime
from pathlib import Path

import yaml
from markdown_it import MarkdownIt

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"
CATALOG = ROOT / "sources" / "catalog.yaml"
FULLTEXT = ROOT / "build" / "fulltext.json"
KB = ROOT / "kb"
DATA = KB / "data"

KB_TITLE = "Philippine Stock Exchange Equity Microstructure"
KB_SUBTITLE = "execution reference"
# The date the research was last checked against live sources. Every chapter states
# its sources' edition span; this is the single date the whole book is "as of".
AS_OF = "2026-10-06"

CITE = re.compile(r"\[\^([a-z0-9][a-z0-9-]*)(?::([0-9]+(?:-[0-9]+)?|[ivxlc]+))?\]", re.I)
LEFTOVER_CITE = re.compile(r"\[\^[^\]]*\]")
XREF = re.compile(r"\]\(#/ch/([a-z0-9-]+)(?:/([a-z0-9-]+))?\)")
FRONTMATTER = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n", re.S)

PDF_TYPES = {"pdf"}
VALID_TYPES = {"pdf", "web", "paper", "dataset"}
VALID_EDITIONS = {"in-force", "superseded", "historical", "n/a"}


class BuildError(Exception):
    pass


@dataclass
class Chapter:
    number: int
    slug: str
    title: str
    summary: str
    part: str | None
    body_md: str
    path: Path
    body_resolved: str = ""
    html: str = ""
    sections: list[dict] = field(default_factory=list)
    references: list[dict] = field(default_factory=list)
    plain_text: str = ""


def slugify(text: str) -> str:
    text = unicodedata.normalize("NFKD", text)
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"[^\w\s-]", "", text).strip().lower()
    return re.sub(r"[\s_]+", "-", text) or "section"


def norm_date(value) -> str | None:
    """YAML turns unquoted 2024-05-01 into a date object; normalise to ISO text."""
    if value in (None, "", "undated"):
        return None
    if isinstance(value, (date, datetime)):
        return value.strftime("%Y-%m-%d")
    return str(value)


SYNCED_FIELDS = ("status", "bytes", "sha256", "page_count", "fetch_route")


def load_catalog() -> dict[str, dict]:
    """The registry is sources/catalog.yaml plus any fragments in sources/pending/*.yaml.

    Fragments let several authors add or correct entries concurrently without racing on
    one file: an entry whose slug already exists updates that entry's fields (never the
    fields sync_sources.py owns); a new slug adds an entry. tools/collect_sources.py
    --fold-pending folds them into the catalog when authoring is done.
    """
    if not CATALOG.exists():
        raise BuildError(f"missing {CATALOG.relative_to(ROOT)}")
    data = yaml.safe_load(CATALOG.read_text("utf-8")) or {}
    entries: list[dict] = list(data.get("sources", []))
    index = {s.get("slug"): s for s in entries}
    for frag in sorted((ROOT / "sources" / "pending").glob("*.yaml")):
        try:
            fdata = yaml.safe_load(frag.read_text("utf-8")) or []
        except yaml.YAMLError as exc:
            raise BuildError(f"{frag.relative_to(ROOT)}: invalid YAML ({str(exc).splitlines()[0]})")
        if isinstance(fdata, dict):
            fdata = fdata.get("sources", [])
        for e in fdata:
            if not isinstance(e, dict) or not e.get("slug"):
                continue
            if e["slug"] in index:
                index[e["slug"]].update({k: v for k, v in e.items() if k not in SYNCED_FIELDS})
            else:
                entries.append(dict(e))
                index[e["slug"]] = entries[-1]
    out: dict[str, dict] = {}
    for s in entries:
        slug = s.get("slug")
        if not slug:
            raise BuildError(f"catalog entry without slug: {s!r:.120}")
        if slug in out:
            raise BuildError(f"catalog: duplicate slug '{slug}'")
        # An archived file not yet reconciled by sync_sources.py (e.g. added through a
        # fragment) is checked here directly, so a citation can still be page-validated.
        lp = s.get("local_path")
        if lp and not s.get("status"):
            path = KB / lp
            if path.exists() and path.read_bytes()[:5] == b"%PDF-":
                try:
                    from pypdf import PdfReader
                    s["page_count"] = len(PdfReader(str(path)).pages)
                    s["status"] = "ok"
                except Exception:
                    s["status"] = "corrupt"
            else:
                s["status"] = "missing"
        for key in ("title", "publisher", "type"):
            if not s.get(key):
                raise BuildError(f"catalog '{slug}': missing '{key}'")
        if s["type"] not in VALID_TYPES:
            raise BuildError(f"catalog '{slug}': type '{s['type']}' not in {sorted(VALID_TYPES)}")
        if s.get("edition") and s["edition"] not in VALID_EDITIONS:
            raise BuildError(f"catalog '{slug}': edition '{s['edition']}' not in {sorted(VALID_EDITIONS)}")
        if str(s.get("amended_through", "")).strip().lower() == "undated":
            s["undated"] = True
        s["amended_through"] = norm_date(s.get("amended_through"))
        out[slug] = s
    return out


def load_chapters() -> list[Chapter]:
    chapters: list[Chapter] = []
    for path in sorted(CONTENT.glob("*.md")):
        raw = path.read_text("utf-8")
        m = FRONTMATTER.match(raw)
        if not m:
            raise BuildError(f"{path.name}: missing YAML frontmatter")
        meta = yaml.safe_load(m.group(1)) or {}
        for key in ("number", "slug", "title", "summary"):
            if key not in meta:
                raise BuildError(f"{path.name}: frontmatter missing '{key}'")
        chapters.append(
            Chapter(
                number=int(meta["number"]),
                slug=str(meta["slug"]),
                title=str(meta["title"]),
                summary=str(meta["summary"]),
                part=meta.get("part"),
                body_md=raw[m.end():],
                path=path,
            )
        )
    chapters.sort(key=lambda c: c.number)
    nums = [c.number for c in chapters]
    slugs = [c.slug for c in chapters]
    if len(set(nums)) != len(nums):
        raise BuildError(f"duplicate chapter numbers: {nums}")
    if len(set(slugs)) != len(slugs):
        raise BuildError(f"duplicate chapter slugs: {slugs}")
    return chapters


def resolve_citations(ch: Chapter, catalog: dict[str, dict], warnings: list[str]) -> str:
    """Replace [^slug:page] with numbered superscript links; collect references.

    Every bad citation in the chapter is reported, not just the first, so an author can
    fix them in one pass.
    """
    order: dict[tuple[str, str], int] = {}
    errs: list[str] = []
    where_ch = f"chapter {ch.number:02d} '{ch.slug}'"

    def repl(m: re.Match) -> str:
        slug, page = m.group(1).lower(), (m.group(2) or "")
        src = catalog.get(slug)
        if src is None:
            errs.append(f"citation [^{m.group(1)}{':' + page if page else ''}] refers to no catalog entry")
            return m.group(0)
        is_pdf = src["type"] in PDF_TYPES
        if is_pdf and src.get("local_path") and src.get("status") != "ok":
            errs.append(f"cites '{slug}', whose archived copy is missing (status={src.get('status')}) "
                        f"-- run tools/sync_sources.py")
            return m.group(0)
        if is_pdf and not src.get("local_path"):
            warnings.append(f"{where_ch}: cites '{slug}', which is not archived locally")
        # The defect this design guards against: a knowledge base accurate about an old
        # date that says so nowhere. Every cited PDF carries an edition date, or is
        # explicitly marked undated so the gap is visible rather than silent.
        if is_pdf and not (src.get("amended_through") or src.get("undated")):
            errs.append(f"cites '{slug}', which has no 'amended_through' (or 'undated') in the catalog")
            return m.group(0)
        first_page = page.split("-", 1)[0] if page else ""
        if page and first_page.isdigit():
            n_pages = src.get("page_count")
            last = page.split("-", 1)[-1]
            if n_pages and int(last) > int(n_pages):
                errs.append(f"citation [^{slug}:{page}] is past the end of that document ({n_pages} pages)")
                return m.group(0)
            if int(first_page) < 1:
                errs.append(f"citation [^{slug}:{page}] -- pages are 1-based")
                return m.group(0)
        key = (slug, page)
        if key not in order:
            order[key] = len(order) + 1
            ch.references.append(
                {
                    "n": order[key],
                    "slug": slug,
                    "page": page,
                    "firstPage": first_page,
                    "title": src["title"],
                    "publisher": src["publisher"],
                    "type": src["type"],
                    "local_path": src.get("local_path") if src.get("status") == "ok" else None,
                    "canonical_url": src.get("canonical_url"),
                    "amended_through": src.get("amended_through"),
                    "undated": bool(src.get("undated")),
                    "edition": src.get("edition"),
                }
            )
        n = order[key]
        if page:
            where = f", pp. {page.replace('-', '–')}" if "-" in page else f", p. {page}"
        else:
            where = ""
        tip = htmllib.escape(f"{src['title']}{where}", quote=True)
        # The href is a full route, never a bare "#ref-...": the app is hash-routed, so
        # a bare fragment would parse as an unknown route and land on the home page.
        return (
            f'<sup class="cite"><a href="#/ch/{ch.slug}/ref-{n}" '
            f'data-cite="{n}" title="{tip}">{n}</a></sup>'
        )

    resolved = CITE.sub(repl, ch.body_md)
    if errs:
        raise BuildError("\n".join(f"{where_ch}: {e}" for e in errs))
    # Anything still shaped like a footnote is a malformed citation; a markdown
    # renderer would print it literally. Fail loudly instead.
    left = [x for x in LEFTOVER_CITE.findall(resolved)]
    if left:
        raise BuildError(f"{where_ch}: malformed citation(s): {left[:8]}")
    return resolved


def render(ch: Chapter, md: MarkdownIt) -> None:
    tokens = md.parse(ch.body_resolved)
    # Stable, de-duplicated ids on h2/h3 so sections are deep-linkable and searchable.
    # "Execution implications" repeats in nearly every chapter; colliding ids would break
    # deep links and make MiniSearch refuse the corpus (it rejects duplicate ids).
    seen: dict[str, int] = {}
    for i, tok in enumerate(tokens):
        if tok.type == "heading_open" and tok.tag in ("h2", "h3"):
            text = tokens[i + 1].content
            base = slugify(text)
            if base.startswith("ref-"):
                base = "s-" + base  # never collide with reference anchors
            seen[base] = seen.get(base, 0) + 1
            anchor = base if seen[base] == 1 else f"{base}-{seen[base]}"
            tok.attrSet("id", anchor)
            clean = re.sub(r"<[^>]+>", "", md.renderInline(text)).strip()
            ch.sections.append({"anchor": anchor, "title": htmllib.unescape(clean), "level": int(tok.tag[1])})
    html = md.renderer.render(tokens, md.options, {})
    # Wide tables scroll inside their own box rather than widening the page.
    html = html.replace("<table>", '<div class="tablewrap"><table>').replace("</table>", "</table></div>")
    ch.html = html
    ch.plain_text = strip_html(html)


def strip_html(html: str) -> str:
    text = re.sub(r'<sup class="cite">.*?</sup>', " ", html, flags=re.S)
    text = re.sub(r"<[^>]+>", " ", text)
    return re.sub(r"\s+", " ", htmllib.unescape(text)).strip()


def section_documents(ch: Chapter) -> list[dict]:
    """Split a chapter into per-section search documents (h2/h3 boundaries)."""
    base = {"type": "chapter", "chapter": ch.number, "chapterSlug": ch.slug, "chapterTitle": ch.title}
    parts = re.split(r'<h[23] id="([^"]+)">', ch.html)
    docs: list[dict] = []
    lead = strip_html(parts[0])
    if lead:
        docs.append({**base, "id": f"ch:{ch.slug}:_intro", "title": ch.title, "anchor": "", "text": lead})
    by_anchor = {s["anchor"]: s["title"] for s in ch.sections}
    for anchor, chunk in zip(parts[1::2], parts[2::2]):
        docs.append({**base, "id": f"ch:{ch.slug}:{anchor}", "title": by_anchor.get(anchor, anchor),
                     "anchor": anchor, "text": strip_html(chunk)})
    if not docs:
        docs.append({**base, "id": f"ch:{ch.slug}", "title": ch.title, "anchor": "", "text": ch.plain_text})
    return docs


def chapter_vintage(ch: Chapter) -> dict:
    """Edition-date span of a chapter's sources, so a reader sees how current it can be."""
    dates = sorted(r["amended_through"] for r in ch.references if r.get("amended_through"))
    # Web pages are living documents; only fixed documents (PDFs, papers) can be "undated".
    undated = len({r["slug"] for r in ch.references
                   if r["type"] in ("pdf", "paper") and not r.get("amended_through")})
    return {
        "oldest": dates[0] if dates else None,
        "newest": dates[-1] if dates else None,
        "undated": undated,
        "sources": len({r["slug"] for r in ch.references}),
        "citations": len(ch.references),
    }


def check_xrefs(chapters: list[Chapter], draft: bool, warnings: list[str], broken: set[str]) -> None:
    """Every [text](#/ch/slug/anchor) must land on a real chapter, section or reference."""
    anchors = {c.slug: {s["anchor"] for s in c.sections} | {f"ref-{r['n']}" for r in c.references} for c in chapters}
    errs: list[str] = []
    for c in chapters:
        where = f"chapter {c.number:02d} '{c.slug}'"
        for slug, anchor in XREF.findall(c.body_md):
            if slug not in anchors:
                # --draft: chapters are written in parallel, so a link may point at one
                # that does not exist yet. Tolerate it while drafting, never in a release build.
                if draft:
                    warnings.append(f"{where}: link to not-yet-written chapter '#/ch/{slug}'")
                    continue
                errs.append(f"{where}: link to unknown chapter '#/ch/{slug}'")
            elif slug in broken:
                warnings.append(f"{where}: link into '{slug}', which failed to build -- anchor not checked")
            elif anchor and anchor not in anchors[slug]:
                known = ", ".join(sorted(a for a in anchors[slug] if not a.startswith("ref-"))[:12])
                errs.append(f"{where}: link to unknown section '#/ch/{slug}/{anchor}' (known: {known})")
    if errs:
        raise BuildError("\n".join(errs))


def js_payload(varname: str, obj) -> str:
    """Emit `window.X = JSON.parse("...")`.

    JSON.parse over a string literal parses markedly faster than an object literal,
    which matters for the multi-megabyte full-text payload. Double-encoding yields a
    correctly escaped JS string; the substitutions stop the payload from terminating
    a <script> element or tripping on JS line terminators.
    """
    inner = json.dumps(obj, ensure_ascii=False, separators=(",", ":"))
    literal = json.dumps(inner, ensure_ascii=False)
    literal = literal.replace("</script", "<\\/script").replace("<!--", "<\\!--")
    literal = literal.replace("\u2028", "\\u2028").replace("\u2029", "\\u2029")
    return f"window.{varname} = JSON.parse({literal});\n"


def main() -> int:
    warnings: list[str] = []
    draft = "--draft" in sys.argv
    try:
        catalog = load_catalog()
        chapters = load_chapters()
        if not chapters:
            raise BuildError("no chapters found in content/")
        md = MarkdownIt("commonmark", {"html": True, "typographer": True}).enable(
            ["table", "strikethrough", "replacements", "smartquotes"]
        )
    except BuildError as exc:
        print(f"BUILD FAILED: {exc}", file=sys.stderr)
        return 1
    # Chapters are checked independently and every failure is reported, so one broken
    # chapter does not hide the state of the others.
    failures: list[str] = []
    broken: set[str] = set()
    search_docs: list[dict] = []
    for ch in chapters:
        try:
            ch.body_resolved = resolve_citations(ch, catalog, warnings)
            render(ch, md)
            search_docs.extend(section_documents(ch))
        except BuildError as exc:
            failures.append(str(exc))
            broken.add(ch.slug)
    try:
        check_xrefs(chapters, draft, warnings, broken)
    except BuildError as exc:
        failures.append(str(exc))
    if failures:
        print("BUILD FAILED:\n  " + "\n  ".join("\n".join(failures).splitlines()), file=sys.stderr)
        return 1

    # MiniSearch refuses a corpus with duplicate ids -- and fails at page load, not
    # here -- so uniqueness is asserted at build time.
    ids = [d["id"] for d in search_docs]
    if len(ids) != len(set(ids)):
        dupes = sorted({i for i in ids if ids.count(i) > 1})
        print(f"BUILD FAILED: duplicate search ids would break the in-browser index: {dupes[:5]}", file=sys.stderr)
        return 1

    cited_by: dict[str, set[int]] = {}
    for c in chapters:
        for r in c.references:
            cited_by.setdefault(r["slug"], set()).add(c.number)

    payload = {
        "title": KB_TITLE,
        "subtitle": KB_SUBTITLE,
        "asOf": AS_OF,
        "builtAt": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "chapters": [
            {
                "number": c.number,
                "slug": c.slug,
                "title": c.title,
                "summary": c.summary,
                "part": c.part,
                "html": c.html,
                "sections": c.sections,
                "references": c.references,
                "vintage": chapter_vintage(c),
                "words": len(c.plain_text.split()),
            }
            for c in chapters
        ],
        "sources": sorted(
            (
                {
                    "slug": s["slug"],
                    "title": s["title"],
                    "publisher": s["publisher"],
                    "type": s["type"],
                    "edition": s.get("edition"),
                    "amended_through": s.get("amended_through"),
                    "undated": bool(s.get("undated")),
                    "note": s.get("note"),
                    "citedIn": sorted(cited_by.get(s["slug"], set())),
                    "local_path": s.get("local_path") if s.get("status") == "ok" else None,
                    "canonical_url": s.get("canonical_url"),
                    "bytes": s.get("bytes"),
                    "pages": s.get("page_count"),
                    "sha256": s.get("sha256"),
                    "fetch_route": s.get("fetch_route"),
                }
                for s in catalog.values()
            ),
            key=lambda s: (str(s["publisher"]).lower(), str(s["title"]).lower()),
        ),
        "searchDocs": search_docs,
    }

    DATA.mkdir(parents=True, exist_ok=True)
    (DATA / "kb-chapters.js").write_text(js_payload("KB_CHAPTERS", payload), "utf-8")

    ft_docs: list[dict] = []
    if FULLTEXT.exists():
        fulltext = json.loads(FULLTEXT.read_text("utf-8"))
        for slug, doc in fulltext.items():
            src = catalog.get(slug)
            if not src:
                continue  # an archived file the catalog no longer lists
            # Only cited sources (or ones explicitly flagged `index: true`) go into the
            # browser's full-text index: the archive holds hundreds of documents, and
            # indexing all of them would make the first search take many seconds.
            if slug not in cited_by and not src.get("index"):
                continue
            for page in doc["pages"]:
                if not page["text"].strip():
                    continue
                ft_docs.append({
                    "id": f"pdf:{slug}:{page['page']}",
                    "type": "source",
                    "slug": slug,
                    "title": src["title"],
                    "publisher": src["publisher"],
                    "path": src.get("local_path"),
                    "page": page["page"],
                    "text": page["text"],
                })
    else:
        print("  (no build/fulltext.json -- run tools/extract_text.py to enable PDF full-text search)")
    (DATA / "kb-fulltext.js").write_text(js_payload("KB_FULLTEXT", ft_docs), "utf-8")

    n_refs = sum(len(c.references) for c in chapters)
    cited = len(cited_by)
    print(f"chapters        {len(chapters)}")
    print(f"sections        {sum(len(c.sections) for c in chapters)}")
    print(f"words           {sum(len(c.plain_text.split()) for c in chapters):,}")
    print(f"citations       {n_refs} resolved, 0 unresolved")
    print(f"sources         {len(catalog)} catalogued, {cited} cited, "
          f"{sum(1 for s in catalog.values() if s.get('status') == 'ok')} archived locally")
    print(f"search docs     {len(search_docs)} chapter sections + {len(ft_docs)} pdf pages")
    print(f"kb-chapters.js  {(DATA / 'kb-chapters.js').stat().st_size / 1e6:6.2f} MB")
    print(f"kb-fulltext.js  {(DATA / 'kb-fulltext.js').stat().st_size / 1e6:6.2f} MB")
    for w in sorted(set(warnings)):
        print(f"  warn: {w}")
    print("\nbuild ok")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
