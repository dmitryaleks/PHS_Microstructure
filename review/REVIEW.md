# Review — PSE Equity Microstructure Knowledge Base

**Reviewed** 7 October 2026 · **research as of** 6 October 2026 · **scope** headline-parameter
verification and assembly defects. Machine-readable record: [`findings.yaml`](findings.yaml).

---

## How the book was checked

Three layers, each independent of the one before:

1. **Researchers** (11) archived the primary documents they relied on and cited them to physical
   pages; each validated its own citations against the PDFs' page counts.
2. **Chapter writers** (11, then one synthesis writer) re-checked the key parameters of their
   chapters against the PDFs — rendering scanned pages as images where the text layer was missing
   or misleading (strikethrough redlines extract as if in force) — and corrected the notes where
   the source disagreed.
3. **This review** re-checked the parameters an execution engine or cost model would hard-code
   against the archived page, using the extracted text and Windows OCR of scanned documents.

On top of that, `tools/build_kb.py` refuses any citation to an unknown source, an unarchived file,
a page past the end of its document, or an undated PDF, and `tools/verify_kb.py` re-checks the
shipped bundle against the archive's SHA-256 checksums.

## Headline parameters: all confirmed

| # | Parameter | Source page | Result |
|---|---|---|---|
| V-01 | 15-band board-lot and tick table, unchanged since 26 Jul 2010 | RTR p.21 (OCR); CN-2025-0046 p.4 | confirmed |
| V-02 | Static band +50% / −30%, effective 24 Mar 2020 | CN-2020-0028 pp.1–2 | confirmed |
| V-03 | PSEi breaker −10/−15/−20% → 15/30/60-minute halts | CN-2020-0044 p.2 | confirmed |
| V-04 | Dynamic thresholds 20/15/10% by six-month trade count | TPA-2026-0036 p.1 (OCR) | confirmed |
| V-05 | Timetable 09:00 · 09:15 · 09:30 · 12:00–13:00 · 14:45 · 14:48 · 14:50 · 15:00 · 15:15 | VWAP rules pp.3, 5–6 (OCR) | confirmed |
| V-06 | Stock transaction tax 6/10 of 1% → 1/10 of 1% | RA 12214 p.16; CN-2025-0028 p.1 | confirmed |
| V-07 | Minimum commission removed 18 Apr 2024 | CN-2024-0029 p.1 | confirmed |
| V-08 | T+2 from trade date 24 Aug 2023 | CN-2023-0031 p.1 | confirmed |
| V-09 | Regular block ≥ PHP 20m within ±5% of LACP | Implementing Guidelines p.23 | confirmed |
| V-10 | EDGE cut-off 4:00 pm from 25 May 2026 | CN-2026-0024 p.1 | confirmed |
| V-11 | Eqlipse go-live 23 Nov 2026; rehearsals 31 Oct, 7 Nov, 14 Nov | NTE broker forum p.9 | confirmed |
| V-12 | Market-wide halt trigger: TPs > 50% of ADTV unable to trade | CN-2025-0037 p.1 | confirmed |
| V-13 | Zero short-sale volume in the daily short-sell report | DSSR 5 Oct 2026 p.2 | confirmed |

## Defects found during assembly — all fixed

| # | Defect | Fix |
|---|---|---|
| F-01 | The markdown typographer turned "(c)" into "©", corrupting citations such as "s.10(c)" | Typographer replacements disabled in the build |
| F-02 | 83 source PDFs were fully or partly scanned — including the Revised Trading Rules, DMA, VWAP and CMIC rules, BIR regulations and Republic Acts — invisible to search | Windows OCR of every document with ≥ 30% text-less pages; 1,346 pages recovered (`sources/ocr/`). The first pass averaged over whole documents and missed typed cover sheets over scanned rule pages; detection is now per page |
| F-03 | Chapter 11 said a halted book "re-opens through an intraday auction" — stronger than the ITCH spec | Aligned with chapters 06/07; marked as inference |
| F-04 | Chapter 17 dated CN-2026-0022 18 May 2026; the circular says 6 May | Corrected |
| F-05 | Byte-identical PDFs archived under two slugs by parallel researchers | Merged onto canonical slugs; citations rewritten |

## Stale public documents the book corrects

The PSE's own published material is not always current, and the book says so where it matters:

- The January 2025 consolidated listing rules print an ex-date of record date − 3 trading days; it
  has been record date − 1 since T+2 (24 Aug 2023), confirmed on 493 EDGE dividend records.
- The same compilation prints a 3:30 pm EDGE cut-off; 4:00 pm since 25 May 2026.
- SCCP's website posts the 2018 T+3 rulebook; the in-force text is that rulebook as amended by memos
  through 8 Jul 2025 (chapter 10 reconstructs it).
- PSE's investor page shows 30% dividend withholding for non-resident foreign corporations; it has
  been 25% (15% on the tax-sparing route) since CREATE.
- PSE's FY2025 statements describe T+2 as aligned with the US and Canada, which moved to T+1 in 2024.

## What remains open

These are not defects in the book — they are not in the public record, and each is stated as an
open question in the relevant chapter with a working assumption for design:

- whether ITCH broker anonymity was ever switched on (working assumption: fills are broker-identified);
- amend/cancel in the run-off (design for none) and the closing price when the pre-close does not cross;
- block-sale settlement date and SCCP guarantee coverage of blocks;
- circuit-breaker clock cut-offs, never restated for the 14:45 pre-close;
- the Nasdaq Eqlipse specifications and the SEC's approval of the rules that depend on it — One Lot
  One Share, the new tick table, the run-off change and Negotiated Trades;
- the 16–18 Nov 2026 trading status and FTSE's 6 Oct 2026 classification announcement;
- real-time data fees, latency, message-rate limits, institutional commissions, SBL volumes and fees.

The engine cut-over on 23 Nov 2026 is the single largest currency risk: every chapter describes the
XTS-era rules as in force and isolates the Eqlipse deltas in dated warnings, and chapter 17 lists
what to re-verify and where.
