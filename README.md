# Philippine Stock Exchange Equity Microstructure Knowledge Base

An offline, self-contained knowledge base on how equities trade on the Philippine Stock Exchange
(PSE), assembled for hedge-fund trading and execution-algorithm design. Eighteen authored chapters,
substantive claims footnoted to a specific page of a source document, and the source documents
archived alongside. **Researched to 6 October 2026.**

**Open `kb/index.html` in any browser.** No server, no network, no build step required to read it.

```
kb/                     the deliverable -- copy this folder anywhere
  index.html
  assets/               app.css, app.js, minisearch.min.js (vendored, MIT)
  data/                 kb-chapters.js, kb-fulltext.js  (globals, not fetched)
  pdfs/                 archived source documents
content/                the chapters, as markdown with [^slug:page] citations
sources/catalog.yaml    the source registry: provenance, edition dates, checksums
sources/ocr/            OCR text for scanned source PDFs (Windows OCR; committed, slow to redo)
research_notes/         the raw research notes the chapters were synthesised from
reports/                executive summary of the research
tools/                  the pipeline (see below)
build/                  intermediate artifacts (extracted text, de-duplicated files)
```

<!-- CONTENTS:START -->
<!-- CONTENTS:END -->

## Why the data is loaded the way it is

`file://` is an opaque origin: `fetch()`, `XMLHttpRequest` and ES-module imports are all blocked.
The obvious design — ship `data.json` and fetch it on load — produces a blank page. So every byte of
data is emitted as a **classic script assigning a global** and loaded with a plain `<script src>`.
The full-text payload is loaded lazily on first search by injecting a script tag, the only cross-file
loader available at that origin. `tools/verify_kb.py` enforces this; `tools/smoke_test.py` proves it
in a real browser at a real `file://` origin.

## Citation conventions

| Form | Meaning |
|---|---|
| `[^slug:12]` | physical page 12 of an archived PDF — the page a viewer shows and `#page=12` opens, not the printed folio |
| `[^slug:12-14]` | a page range (links to the first page) |
| `[^slug]` | a whole document or a web page |
| `[Chapter 4](#/ch/order-types)` | a cross-reference; `#/ch/<slug>/<anchor>` deep-links a section |

Each chapter states the edition-date span of the sources it cites and the date the research was
checked against live sources. Callouts distinguish rule text from analysis: *Consequence* (what a rule
forces), *warn* (changed recently, pending, or sources conflict) and *Inference* (analysis, not rule).

## Pipeline

```bash
python tools/collect_sources.py   # research-note "Source catalog" blocks -> sources/catalog.yaml
python tools/dedupe_archive.py    # collapse byte-identical PDFs onto one slug (--apply)
python tools/sync_sources.py      # reconcile catalog with kb/pdfs: status, sha256, page counts
python tools/extract_text.py      # per-page text -> build/fulltext.json
python tools/ocr_sources.py       # Windows OCR for scanned PDFs -> sources/ocr/ (then re-run extract)
python tools/build_kb.py          # render + index -> kb/data/*.js   (--draft while authoring)
python tools/verify_kb.py         # static consistency checks over the shipped bundle
python tools/smoke_test.py        # headless Chrome at a real file:// origin, every route
python tools/rebuild.py --smoke   # sync -> extract -> build -> verify -> smoke, in order
```

### Authoring instruments

```bash
python tools/lookup.py "board lot"                        # phrase -> [^slug:page] hits
python tools/lookup.py -r "pre-?open" -s pse-revised-trading-rules
python tools/pdf_pages.py pse-revised-trading-rules 12-14 # read specific pages
python tools/pdf_grep.py "static threshold"               # search PDFs not yet catalogued
```

Concurrent authors never edit `sources/catalog.yaml` directly: each writes corrections and additions to
`sources/pending/<name>.yaml`, which the build merges on the fly and
`python tools/collect_sources.py --fold-pending` folds in when authoring is done.

## Build guarantees

`build_kb.py` fails rather than shipping a defect when:

- a citation names a catalog entry that does not exist, or is malformed;
- a citation names an archived document whose file is missing or unreadable;
- a citation points **past the last page** of its document;
- a cited PDF carries **no edition date** and is not explicitly marked `undated`;
- a cross-reference names an unknown chapter, section or reference;
- two search documents would share an id (MiniSearch would refuse the whole corpus at page load).

It reports every failure in every chapter in one pass. `verify_kb.py` re-checks the shipped bundle:
classic scripts only, no remote assets, data files decode, archived files match their recorded SHA-256,
every reference resolves, and the bundle is not older than its inputs. `smoke_test.py` loads the home
page, every chapter (checking its title and reference count), the source library and a search —
including the lazily loaded full-text index — in headless Chrome under a throwaway profile.

These guards follow the lessons recorded in the SAE knowledge base this one is modelled on: the worst
defect a reference like this can have is being accurate about an old date and saying so nowhere. The
archive is good for *finding* documents and useless for *dating* them, so edition dates here are read
from each document's own cover or amendment history, and every chapter renders the span of its
sources' dates.

<!-- PROVENANCE:START -->
<!-- PROVENANCE:END -->

## Known limits

<!-- LIMITS:START -->
- **Synthesis, not advice.** Chapters are synthesis for trading design, not legal, tax or compliance
  advice. Inference is marked as inference.
<!-- LIMITS:END -->
