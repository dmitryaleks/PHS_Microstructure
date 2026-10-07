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
review/                 coordinator review: parameters re-checked against source pages, defects fixed
tools/                  the pipeline (see below)
build/                  intermediate artifacts (extracted text, de-duplicated files)
```

<!-- CONTENTS:START -->
## Contents

| # | Chapter | What it settles | KB | Citations |
|---|---|---|---|---|
| 00 | [PSE at a Glance](content/00-at-a-glance.md) | Parameter cheat sheet for PSE equities on 6 Oct 2026: timetable, ticks, controls, costs, settlement, access, what the 23 Nov Eqlipse cut-over may change, and ten things that break ported algorithms. | 28 | 151 |
| 01 | [Market Architecture](content/01-market-architecture.md) | One exchange, one CCP, one depository and no co-location. Who runs and regulates PSE equities, how orders reach the engine, and why the 23 Nov 2026 Eqlipse cut-over is the date to design around. | 61 | 343 |
| 02 | [Instruments, Boards and Listings](content/02-instruments.md) | Two listing boards, 387 live lines (65 suspended), one ETF; since 11 Aug 2026 a float breach means immediate suspension with no cure period; the odd-lot book ends 23 Nov 2026 if SEC approves. | 102 | 425 |
| 03 | [Trading Sessions and Calendar](content/03-sessions.md) | One whole-day session, 09:00-15:15, with two call auctions, hard no-cancel windows, a recess and a VWAP-only last 15 minutes; closures arrive by circular and the engine changes on 23 Nov 2026. | 36 | 169 |
| 04 | [Order Types, Tick Sizes and Board Lots](content/04-order-types.md) | The rulebook lists six order types but the new engine opens with limits only; re-pricing or upsizing costs queue priority; a 15-band PHP lot and tick table makes the relative tick jump at band edges. | 41 | 137 |
| 05 | [Matching, Block Sales and Crosses](content/05-matching.md) | Price-time matching with no self-trade prevention, and how pre-arranged size routes to crosses, block sales or (proposed) negotiated trades; block sales were 18.4% of 2026 turnover value. | 46 | 169 |
| 06 | [Opening and Closing Auctions](content/06-auctions.md) | Call auctions set the open at 09:30:00 and the close at 14:50, then 10 minutes trade at that fixed close; the price rule is published and reproducible, with no random end and no volatility auction. | 40 | 135 |
| 07 | [Price Controls, Halts and Circuit Breakers](content/07-price-controls.md) | Static band +50%/−30%, dynamic 10–20% thresholds that freeze the stock instead of auctioning it, PSEi breakers at −10/−15/−20%, and how halts and suspensions treat resting orders. | 47 | 177 |
| 08 | [Market Making and Liquidity Provision](content/08-market-making.md) | The only obligated liquidity at the PSE is ETF market making for one fund, FMETF, under loose 2013 rules; no equity has a market maker and two draft regimes remain unadopted. | 36 | 167 |
| 09 | [Short Selling, Lending, Margin and Hedging](content/09-short-selling.md) | Short selling has been legal in 52 names since 6 Nov 2023 yet every daily report shows zero volume; borrow, margin and hedging routes are partial, pending or offshore. | 52 | 243 |
| 10 | [Clearing, Settlement and Corporate Actions](content/10-clearing-settlement.md) | One CCP with no initial margin and a capped PHP 1.77bn fund, T+2 with a noon deadline, ex-date one trading day before record date with resting orders cancelled, and a stale posted rulebook. | 88 | 346 |
| 11 | [Market Data, Transparency and Indices](content/11-market-data.md) | A full-depth anonymous ITCH book whose fills probably carry broker codes, the published fees, EDGE timing, PSEi and MSCI/FTSE rules with rebalance-day volumes, and the feed change due 23 Nov 2026. | 89 | 335 |
| 12 | [Trading Costs and Taxes](content/12-costs.md) | Explicit PSE costs per side, the sell-only 0.1% stock transaction tax since 1 Jul 2025 (was 0.6%), a PHP 10m round trip at 70.12 bp, and the dividend and capital-gains tax matrix for non-residents. | 44 | 162 |
| 13 | [Regulatory Constraints and Market Conduct](content/13-regulatory-constraints.md) | Orders count whether or not executed, issuers disclose within 10 minutes, ownership triggers sit at 5/10/15/35/50%, foreign-limit breaches are unwound at once, and DMA rules ban algorithmic flow. | 41 | 188 |
| 14 | [Foreign Access and Ownership Limits](content/14-foreign-access.md) | Which PSE stocks foreigners may own (218 of 281 capped at 40%, 15 at 0%), how the cap is policed order by order, and the BSP registration, FX and index-provider facts that gate foreign flow. | 47 | 131 |
| 15 | [Empirical Liquidity and Market Quality](content/15-empirical.md) | A thin, concentrated, foreign-sensitive market whose closes often print the day's extreme; spreads and depth are not public and PSE-specific microstructure research is almost absent. | 96 | 431 |
| 16 | [Execution Algorithm Design Implications](content/16-execution-implications.md) | The knowledge base reduced to design decisions for a scheduler, order placer, risk layer and cost model on PSE equities, version-gated for the 23 Nov 2026 Eqlipse cut-over. Inference is marked. | 45 | 198 |
| 17 | [Reform Timeline and Pipeline](content/17-reform-timeline.md) | What is in force on 6 Oct 2026, every dated rule change since 2018, version gates for backtests, and the pipeline led by Nasdaq Eqlipse on 23 Nov 2026, whose rule changes still await SEC approval. | 87 | 506 |
| | **18 chapters** | | **1,025** | **4,413** |
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
python tools/update_readme.py     # regenerate this README's contents and provenance sections
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
## Provenance

**759 sources catalogued, 670 cited.** 448 documents are archived in `kb/pdfs/` (632 MB, 7,035 pages), 411 of them cited; every archived file's SHA-256 and page count is recorded in `sources/catalog.yaml` and re-checked by `verify_kb.py`. Uncited archived documents are kept for completeness and appear in the source library.

| Source type | Catalogued |
|---|---|
| pdf | 446 |
| web | 287 |
| dataset | 13 |
| paper | 13 |

| Edition status of cited sources | Count |
|---|---|
| in-force | 256 |
| historical | 212 |
| n/a | 169 |
| superseded | 33 |

| Most-cited publishers | Sources cited |
|---|---|
| The Philippine Stock Exchange, Inc. | 429 |
| Securities Clearing Corporation of the Philippines | 37 |
| BusinessWorld | 36 |
| The Philippine Star | 21 |
| InsiderPH | 12 |
| Republic of the Philippines | 9 |
| Clearstream Banking | 9 |
| Securities and Exchange Commission (Philippines) | 8 |
| LawPhil Project (Arellano Law Foundation) | 7 |
| Bangko Sentral ng Pilipinas | 7 |
| Bureau of Internal Revenue | 7 |
| MSCI | 7 |

**Scanned documents.** 83 archived PDFs are wholly or partly scanned. Their text was recovered with the OCR engine built into Windows (1,346 pages, `sources/ocr/`), so they are searchable and citable by page like any other source.

**Retrieval notes.** `www.pse.com.ph` serves non-browser clients; `www.sec.gov.ph` and `www.sccp.com.ph` answer HTTP 403 to every non-browser client, and `edge.pse.com.ph` was intermittently unavailable (it failed on 19 Jan and 6 Oct 2026). Documents from those hosts came through PSE re-postings, the Internet Archive or other mirrors; citations link the canonical URL while the reference list opens the archived copy.
<!-- PROVENANCE:END -->

## Known limits

<!-- LIMITS:START -->
- **The trading engine changes on 23 Nov 2026.** The PSE plans a big-bang cut-over from PSEtrade XTS
  (Nasdaq X-stream, live since 2015) to Nasdaq Eqlipse. The book describes the XTS-era rules as in
  force on 6 Oct 2026 and isolates every announced Eqlipse change in a dated warning; the
  rule changes tied to it (One Lot One Share, a new tick table, odd-lot removal, a run-off rewrite,
  Negotiated Trades) had no SEC approval on record. Chapter 17 lists what to re-verify, and where.
- **There is no consolidated current rulebook.** The PSE still posts its 2010 Revised Trading
  Rules and Implementing Guidelines as the base text; the rules in force are that text as amended
  by circulars, and article numbering has drifted across amendments. Chapters cite the circulars.
  SCCP likewise posts its 2018 T+3 rulebook; chapter 10 reconstructs the in-force text from memos.
- **Some things are not in the public record**, and each chapter ends by listing them: whether
  ITCH broker anonymity was ever switched on, amend/cancel in the run-off, the closing price when
  the pre-close does not cross, block-sale settlement and guarantee coverage, real-time data fees
  and latency, message-rate limits, institutional commission rates, securities-lending volumes and
  fees, and enforcement statistics after 2019. Working assumptions are labelled as inference.
- **Computed statistics are labelled as such.** Several empirical figures — block share of value,
  closing-print behaviour, index-event volumes, spread proxies — were computed from the PSE's daily
  quotation and weekly reports over stated sample periods; they are not PSE-published figures.
- **Scanned sources are read through OCR.** 83 archived documents carry no (or a partial) text layer;
  their searchable text is Windows OCR and can contain recognition errors. Key parameters cited from
  scanned pages were checked against the rendered page images (see `review/`).
- **Secondary-only facts are flagged in the text.** The SEC and SCCP websites refuse automated
  clients, so a few documents were reached only through re-postings or the Internet Archive, and a
  few facts rest on news reports or broker pages; the chapter says so wherever that is the case.
- **Synthesis, not advice.** Chapters are synthesis for trading design, not legal, tax or compliance
  advice. Inference is marked as inference.
- **Size.** The archive is ~600 MB; `kb/pdfs/pse-cmic-rules.pdf` (51 MB) is over GitHub's
  recommended 50 MB file size (under the 100 MB hard limit).
<!-- LIMITS:END -->
