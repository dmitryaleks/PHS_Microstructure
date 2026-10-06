# PSE equity market reform timeline, 2018 to 6 October 2026 (currency check for Chapter 17)

**Status of this file:** v3, 6 Oct 2026. Revision log: v1 = first complete draft (chronology, pipeline, conflicts, execution implications, source catalog); v2 = adds the primary text of the 13th negative list, the 2024 and 2025 president's reports (slippage record, board-lot filing, PDTC lending-agent approval), broker-failure and delisting events, the 6 Oct 2026 EDGE outage, the 2023 MPO consultation, BSP foreign-investment notices, a version-gating table, SCCP post-trade rule changes and a products row; v3 = cross-check against the sibling notes 01-10 and primary re-reads: adds baseline rows (DMA algorithmic ban, ETF market making, short-selling legal base, commission cap, 2012 MPO rule, CMIC), the 2020 IPO-tax repeal, listing and disclosure rule changes (2021 Main/SME recut, 2022 backdoor-listing and preferred-share rules, 2023 REIT and stabilisation rules, EDGE cut-offs, ALMF), corporate and broker-failure events, pipeline row P21, a look-ahead calendar (2D) and conflicts C17-C20, and corrects the SCCP allocation-algorithm description (the old text had it backwards), the PDTC approval wording and the SEC MC 13-2017 date. Every cited slug and page number was machine-checked against kb/pdfs.

**As-of date:** 6 October 2026. **Evidence cut-off:** PSE circular/announcement index and New Trading Engine (NTE) pages fetched 6 Oct 2026 (index re-fetched about 14:30 and again about 22:00 local; the NTE "Updates" tab still lists only CN-2025-0046). The newest entries are three EDGE-outage notices posted 6 Oct 2026, then TPA-2026-0041 (2 Oct) and PSE's relay of an SEC request for comments on broker-dealer capital (1 Oct); nothing was posted 3-5 Oct. FTSE Russell's 2026 country-classification announcement (scheduled 6 Oct) was still a "Document to follow" placeholder at the same re-check. SEC, BIR and Official Gazette sites were blocked or unavailable, so SEC/BIR items after 17 Aug 2026 are known only through PSE's relays and the press. The shared WebSearch quota (200 calls) ran out mid-task, so the last third of discovery relied on PSE's own indexes and direct fetches; news cross-checks are fewer than planned.

**Citation convention.** `[^slug:N]` = physical page N (PDF-viewer page, not the printed folio) of kb/pdfs/slug.pdf. `[^slug]` = a web page or a whole document. Every slug is defined in the "Source catalog" at the end, with URL and edition. Many PSE PDFs are scanned images; those were read from rendered page images.

**Evidence labels.** P = primary (statute, regulator, PSE/SCCP/PDS/BIR/SEC document). S = secondary only (press, law-firm or consultancy note; no primary retrieved). I = my inference from the cited facts.

**Status vocabulary.** In force; Superseded (was in force, replaced by a later row); Approved, not yet effective (decided/approved, with a future effective or go-live date); Proposed (consultation, exposure draft, or filed with the regulator and awaiting action); Abandoned (proposed, never adopted, replaced by a different proposal); Historical (one-off event, no continuing rule).

---

## 1. Chronology of rule and structural changes, 2018 to 6 October 2026

### Takeaway
The PSE order book's static parameters moved little in 2018-2026: the 15-band board-lot/tick table is the same one that appears as "existing" in PSE's December 2025 consultation, and PSE's web list of amendments to the Revised Trading Rules shows nothing between 2013 and the 2020 COVID measures, then only VWAP and minimum-commission items in 2024 (the list omits the 2025 halt/typhoon amendments, so it is not exhaustive). What changed was (1) cost and tax: STT 0.5% to 0.6% on 1 Jan 2018 (TRAIN) and 0.6% to 0.1% on 1 Jul 2025 (CMEPA), IPO tax repealed Sep 2020 (RA 11494), minimum commission removed 18 Apr 2024; (2) session design: shortened hours Mar 2020-Dec 2021, a new 09:30-15:00 schedule on 6 Dec 2021, and a Closing VWAP session that moved the close to 15:15 on 1 Mar 2024; (3) risk controls: lower static floor -50% to -30% (24 Mar 2020), three-level index circuit breaker (4 May 2020), ">50% of ADTV" halt trigger and typhoon rule (20 Aug 2025); (4) post-trade: SCCP new clearing system (27 Mar 2023) and T+3 to T+2 (24 Aug 2023), plus SCCP rule changes on collateral (20 Feb 2023), client assets (23 Aug 2023), allocation algorithm and early delivery (21 Jan 2025) and CTGF refunds (2018 and 2025); (5) shorting: guidelines effective 2 Oct 2023, go-live 6 Nov 2023; (6) ownership and benchmarks: index free-float floor 12% to 15% to 20%, MidCap/DivY indices, tiered minimum public ownership (11 Aug 2026), Class A/B declassification, RA 11647/11659 and the 12th/13th negative lists; (7) corporate: PSE took control of PDS Group in Dec 2024, after a 2018 rights offering to meet the broker-ownership cap; (8) listing and disclosure rules: Main/SME recut (24 Mar 2021), backdoor-listing and preferred-share rules (2022), REIT and stabilisation rules (2023), EDGE release cut-off 3:30 pm then 4:00 pm (25 May 2026). The biggest microstructure change (Nasdaq Eqlipse engine, one-share lots, negotiated trades) is scheduled for 23 Nov 2026 and is NOT live.

### Cited Findings

#### 1A. Snapshot: parameters in force on 6 Oct 2026

| Parameter | In force on 6 Oct 2026 | In force since | Next change on the table | Sources | Ev |
|---|---|---|---|---|---|
| Full-day timetable | 09:00 pre-open; 09:15 pre-open no-cancel; 09:30 open; 12:00-13:00 recess; 14:45 pre-close; 14:48 pre-close no-cancel; 14:50 run-off/trading-at-last (orders only at closing price); 15:00-15:15 Closing VWAP session; 15:15 close | 1 Mar 2024 (close moved 15:00 to 15:15); morning/afternoon/pre-close times unchanged since 1 Mar 2022 | NTE go-live (target 23 Nov 2026); no new session times announced | [^pse-approved-rules-vwap-trading-2024:3][^pse-approved-rules-vwap-trading-2024:6][^pse-cn-2024-0012-vwap-go-live:1][^pse-cn-2022-0009-trading-schedule-mar-2022:1][^pse-web-investing-at-pse] | P |
| Half-day timetable | 09:00/09:15/09:30; pre-close 11:57; no-cancel 11:59; run-off 12:00; Closing VWAP 12:10; close 12:25 | 1 Mar 2024 | none announced | [^pse-approved-rules-vwap-trading-2024:3][^pse-approved-rules-vwap-trading-2024:5] | P |
| Settlement | T+2; settlement deadline 12:00 noon; ex-date one trading day before record date | 24 Aug 2023 | none announced; no T+1 plan found in PSE/SEC documents reviewed | [^pse-cn-2023-0031-t2-settlement:1][^pse-cn-2023-0040-t2-go-live:1-3] | P (absence of T+1 plan is I) |
| Board lot and tick | 15 price bands; lot 1,000,000 shares (price 0.0001-0.0099) down to 5 shares (price 1,000+); tick 0.0001 up to 5.00 (full table in Section 2) | No amendment found since at least Nov 2013 | One Lot One Share (lot = 1) plus a new tick table; awaiting SEC approval; target with NTE | [^pse-cn-2025-0046-board-lot-trading-at-last:4][^pse-web-investing-at-pse][^pse-web-reg-trading-participants] | P; "unchanged since 2013" is I |
| Static threshold | +50% / -30% of reference price (previous close or last adjusted closing price); PSE can lift the lower bound for a security (e.g. follow-on listing day) | 24 Mar 2020 | not mentioned in NTE materials | [^pse-cn-2020-0028:1-2][^pse-cn-2021-0055-lift-lower-static-threshold-sgp:1] | P |
| Dynamic threshold | Per-security cap on the change from the preceding last-traded price: 10% (more than 500 trades in prior six months), 15% (21-500 trades), 20% (20 or fewer); reclassified each Feb and Aug | 7 Aug 2026 (prior reset 2 Feb 2026) | next semiannual reset about Feb 2027 (I) | [^pse-tpa-2026-0036-dynamic-threshold-review:1][^pse-tpa-2026-0002-dynamic-threshold-review:1][^pse-web-investing-at-pse] | P |
| Index circuit breaker | PSEi down 10% / 15% / 20% vs previous close triggers a 15 / 30 / 60-minute market-wide halt; each level once per day; higher level supersedes; halts crossing the recess include it | 4 May 2020 | none | [^pse-cn-2020-0044:1-4] | P |
| Market halt and calamity rules | Exchange may halt the market if TPs with more than 50% of six-month ADTV (ex-block) cannot trade; every TP must have a correspondent TP; PAGASA signal 3-5 in NCR = no trading, signal 1-2 = regular trading | 20 Aug 2025 (correspondent-TP duty after 2-month grace) | none | [^pse-cn-2025-0037:1-2][^pse-cn-2025-0037:4] | P |
| Taxes and fees | STT 0.1% of gross selling price, seller-paid (also on domestic shares listed abroad); PSE fee 0.005% per side plus 12% VAT; SCCP 0.01% per side (VAT-inclusive); SEC "SRC fee" 0.005% per side (PSE illustration); broker commission capped at 1.5% plus VAT with no regulatory minimum; dividend withholding per CREATE schedule | STT 1 Jul 2025; minimum commission removed 18 Apr 2024; PSE fee rate unchanged 2018-2026 as far as found | none announced | [^ra-12214-cmepa:16][^bir-rr-20-2025-stt:4][^pse-cn-2024-0029-min-commission-removal:1][^pse-web-investing-at-pse][^pse-annual-report-2018:88][^pse-annual-report-2019:48] | P |
| Short selling | Allowed since 6 Nov 2023 for PSEi, MidCap, Dividend Yield constituents and ETFs (53 eligible securities on the first Daily Short Selling Report, 52 on 5 Oct 2026; both reports show zero short-sale volume and no short interest in any security); short-interest ratio at or below 10% of outstanding shares; uptick rule (SRC Rule 24.2-2); not accepted in pre-open or pre-close; day orders only; no aggregation; none in odd-lot market or block sales; naked shorting prohibited | 6 Nov 2023 | revised PSE SBL rules (directed pooled lending, onshore lending agent) filed with SEC 16 Apr 2026, awaiting approval | [^pse-cn-2023-0048:8-10][^pse-cn-2023-0056:1][^pse-dssr-2023-11-06:1-2][^pse-dssr-2026-10-05:1-2][^pse-web-sbl-short-selling][^pse-pr-regulatory-reforms-2026-06-15] | P |
| SBL plumbing | MSLA/GMSLA registered with BIR; PSE sole pre-clearing body for MSLAs; PDTC Lending Agency Service live with cash-collateral borrowers; offshore collateral allowed for deals with a foreign party | PDTC pool Apr-May 2026; MSLA guidelines approved by the SEC 15 May 2026 | SEC decision on revised SBL rules | [^pse-cn-2026-0022:1-2][^pse-cn-2026-0025:1][^pse-cn-2023-0027-offshore-collateral-sbl:1][^pse-cn-2024-0035:1-2] | P |
| PSE index series | PSEi 30 stocks; MidCap 20; Dividend Yield 20; six sector indices; free float of at least 20%; Feb/Aug reviews; liquidity = median daily value rank (old test) | PSEi membership changes 3 Aug 2026; float 20% applied from the Dec 2022 review | revised methodology (98% cumulative market cap; MTAR + MADV; 15% float exception at PHP250bn+) at the Feb 2027 rebalance | [^pse-cn-2021-0046-index-policy-revision-2021:1][^pse-cn-2026-0035:1][^pse-cn-2026-0033b:1] | P |
| Minimum public ownership | IPO: 33% (market cap up to PHP500M), 25% (to PHP1bn, offer at least PHP165M), 20% (to PHP50bn, offer at least PHP250M), 15% (above PHP50bn, offer at least PHP10bn); REIT 33.33%; maintenance 20% (15% above PHP50bn); possible 12% floor for PHP200bn+ listings; pre-2017 listings 10% and 2017-2026 listings 20% grandfathered | 11 Aug 2026 | none | [^pse-amended-mpo-rule-2026-08:2-4] | P |
| Engine, clearing, floor | PSEtrade XTS (Nasdaq X-stream) since 22 Jun 2015; SCCP on LSEG Millennium since 27 Mar 2023; floorless trading since 27 Jun 2022 | as stated | Nasdaq Eqlipse NTE target 23 Nov 2026 | [^pse-annual-report-2015:42][^pse-pr-sccp-new-clearing-system-2023-03-31][^pse-pr-trading-floor-closed-2022-06-24] | P |
| Block sale / crosses / VWAP | Regular block sale at least PHP20M within +/-5% of reference price; special block sale at least PHP50M; crosses within best bid/offer; Closing VWAP trades at least PHP500,000, single TP, executed only 15 min after run-off | 1 Mar 2024 (VWAP) | Negotiated Trades (proposed) | [^pse-cn-2026-0031-negotiated-trades:3][^pse-approved-rules-vwap-trading-2024:7] | P |
| Products | Common stocks (Main and SME boards), dollar-denominated preferred series (four series, two of them suspended), REITs (8 listed since AREIT on 13 Aug 2020; trading restricted to PSE-"eligible" brokers), one ETF (FMETF, listed 2 Dec 2013, one market maker), preferred shares, two PDRs (ABSP, GMAP) and one company-warrant series (AGIW, listed 19 Dec 2025). Not available: derivatives, GPDRs, structured warrants, market-maker programmes beyond the ETF | REITs 2020; warrants Dec 2025; others unchanged | GPDR, structured warrants, index futures, ETF rule changes (all Proposed, Section 2) | [^pse-web-new-listings][^pse-cn-2020-0066-reit-broker-eligibility:1-2][^pse-web-etf-page][^pse-press-agi-warrants][^pse-listed-company-directory-frame][^pse-sec-frames-snapshot][^pse-annual-report-2013:22][^gma-2023-10-20-short-selling-nov-6][^pse-analyst-briefing-1h-2026:9-10] | P/S |
| Foreign ownership law | 13th Regular Foreign Investment Negative List (EO 113, signed 13 Apr 2026; effective 15 days after publication, reported as 1 or 2 May 2026): no foreign equity in mass media/internet business, corporate practice of architecture, cooperatives, private security, small-scale mining; up to 25% private recruitment and defense construction; 30% advertising; 40% for public utilities (six categories), natural resources (renewables fully open), private land, retail trade with paid-up capital under PHP25M, educational institutions, condominiums; telecom operation 100% with reciprocity, 50% without. RA 11659 limits "public utility" to six categories; RA 11647 amends the Foreign Investments Act | 2022 statutes; 13th list May 2026 | none | [^eo-113-2026-13th-finl:1-5][^ra-11659-public-service-act-amendments:4][^ra-11659-public-service-act-amendments:14][^ra-11647-foreign-investments-act-amendments:8][^kpmg-2026-04-13th-finl] | P (effective date S) |
| Benchmarks | MSCI Philippines Index has 9 constituents (30 Sep 2026); FTSE classifies the Philippines "Secondary emerging" (Sep 2026 ground rules); MSCI 2026 market classification announcement did not mention the Philippines | Aug-Sep 2026 | FTSE Russell's 2026 annual country-classification announcement was scheduled for Tue 6 Oct 2026 (FTSE's page still showed only a "Document to follow" placeholder when checked); MSCI's November review date not retrieved | [^msci-philippines-index-factsheet-2026-09:1][^ftse-geis-ground-rules-2026-09:45][^ftse-country-classification-interim-2026-03:5][^ftse-equity-country-classification-page][^ladige-2026-06-msci-mcr] | P/S |

#### 1B. Dated chronology (effective date first; implementing document in the Sources column)

**B0. Pre-window baseline (state on 1 Jan 2018, for before/after comparisons)**

| ID | Date | Area | State | Status (6 Oct 2026) | Sources | Ev |
|---|---|---|---|---|---|---|
| B0.1 | 2013-11-04 | Session timetable | 09:00 pre-open; 09:30 open; 12:00 recess; 13:30 resume; 15:15 pre-close (auction 15:15-15:18, no-cancel 15:18-15:20); 15:20 run-off/trading-at-last; 15:30 close. Pre-close lengthened from 3 to 5 min (SEC approval 26 Sep 2013); the 2012 timetable (effective 2 Jan 2012) had pre-close 15:17 | Superseded (R2.4, R3.4) | [^pse-memo-extended-pre-close-implementation-2013:1][^pse-memo-pre-close-schedule-2013:1][^pse-memo-new-trading-hours-2011:1] | P |
| B0.2 | 2015-06-22 | Engine | Migration to PSEtrade XTS (Nasdaq X-stream) | In force until NTE | [^pse-annual-report-2015:42] | P |
| B0.3 | to 2023-08-23 | Settlement | T+3 | Superseded (R4.8) | [^pse-cn-2023-0031-t2-settlement:1] | P |
| B0.4 | to 2017-12-31 | STT | One-half of 1% (0.5%) of gross selling price | Superseded (R1.1) | [^pse-cn-2017-0082-stt-increase-advisory:1] | P |
| B0.5 | to 2020-03-23 | Price limits | Static band +50% / -50%; single circuit breaker (PSEi -10% = 15-minute halt, an offshoot of the 2008 crisis) | Superseded (R2.5, R2.6) | [^pse-cn-2020-0028:1][^pse-cn-2020-0044:1] | P |
| B0.6 | to 2018-02 | Index policy | PSEi/sector-index free-float floor 12%; recompositions in March and September | Superseded (R1.2) | [^pse-cn-2018-0013-index-policy-revision-2018:1] | P |
| B0.7 | pre-2018 | Board lot / tick | Same 15-band table as the "existing" table in the Dec 2025 consultation | In force | [^pse-cn-2025-0046-board-lot-trading-at-last:4] | P |
| B0.8 | 2014-01-02 | Algorithmic and high-frequency access | PSE Direct Market Access (DMA) Rules (SEC-approved; PSE memo 26 Nov 2013) take effect on the first trading day of 2014: the DMA facility may not be used for high-frequency or algorithmic trading; Sponsored Access only for QIBs; six-month transition for existing DMA offerings | In force (the Sep 2023 proposal to allow algorithmic trading, R4.10, has no approval on record) | [^pse-memo-sec-approved-dma-rules-2013-11-26:1][^pse-memo-sec-approved-dma-rules-2013-11-26:8] | P |
| B0.9 | 2013-03-18 | ETF and market making | SEC-approved PSE ETF Rules including Part C ETF Market Making Rules: two-way quotes within a maximum spread of 20 / 15 / 10 / 5 ticks by price band, at least 5 board lots per order, a wide spread (3 minutes) cured within 90 seconds, presence at least 50% of each day and 80% of the month. FMETF, still the only ETF, listed 2 Dec 2013 | In force (amendments proposed in 2026, P10) | [^pse-etf-rules:1][^pse-etf-rules:22-23][^pse-annual-report-2013:22] | P |
| B0.10 | 2007-02-15 to 2015-11-09 | Short selling and SBL (legal base) | PSE SBL Rules (SEC-approved 16 Nov 2006) and SBL Guidelines effective 15 Feb 2007; Revised Trading Rules with short-selling provisions published 8 Jun 2010 and effective with the new trading system on 26 Jul 2010 (PSE may stop or cap short selling in a stock and require disclosure of short positions); SRC IRR Rule 24.2-2 (uptick test) effective 9 Nov 2015. The programme itself only went live on 6 Nov 2023 | Superseded by the programme rules (R1.7, R4.11, R4.13) | [^pse-sbl-short-selling-intro-presentation:2][^pse-implementing-guidelines-trading-rules:1][^pse-revised-trading-rules:20][^sec-2015-src-irr:71][^sec-2015-src-irr-notice-of-effectivity:1] | P |
| B0.11 | to 2024-04-17 | Commission | PD 154 (14 Mar 1973) capped broker commission at 1% with a PHP20 minimum; the SEC raised the cap to 1.5% on 14 Dec 1977; PSE's rule on minimum commission rates set a size-graded minimum of 0.25% to 0.05% of the value of the trade | Superseded (R5.8); the 1.5% cap remains | [^pse-cn-2024-0029-min-commission-removal:2] | P |
| B0.12 | 2012-01-01 | Minimum public ownership | PSE Amended MPO Rule (SEC approval 19 Dec 2011) effective 1 Jan 2012: a company that is non-compliant from 1 Jan 2013 is suspended for up to six months and then automatically delisted (no involuntary-delisting procedure; five-year relisting bar). SEC MC 13-2017, issued 1 Dec 2017, later required IPO issuers to have 20% public ownership and to keep it at all times (12 months to cure a shortfall) | Superseded for new listings (R2.10, R7.14); the suspend-then-delist ladder is carried into the 2026 rule | [^pse-sr6-mpo-rule-2012:1][^pse-sr6-mpo-rule-2012:3][^pse-sr6-2-mpo-initial-backdoor-2020:3] | P |
| B0.13 | 2012-02-02 | Surveillance and halts | CMIC begins as PSE's independent audit, surveillance and compliance arm (SEC authority with provisional SRO status from 2 Feb 2012). Its rules (V1.2, 15 Dec 2011) let CMIC, with the PSE President's approval, restrict, halt or suspend trading in a listed security, or by a TP in it, on breach of pre-established price or volume benchmarks | In force | [^pse-annual-report-2025:8][^pse-cmic-rules:112] | P |

**B1. 2018-2019**

| ID | Effective date | Area | Change (before to after) | Status | Sources | Ev |
|---|---|---|---|---|---|---|
| R1.1 | 2018-01-01 | Tax (RA 10963 TRAIN) | Stock transaction tax on listed shares 0.5% to 0.6% (6/10 of 1%) of gross selling price, seller-paid. TRAIN approved 19 Dec 2017; PSE advisories 26 and 29 Dec 2017. BIR forms and eFPS were not updated at start (RMC 2-2018) | Superseded 1 Jul 2025 (R6.7) | [^ra-10963-train:24][^ra-10963-train:54][^pse-cn-2017-0082-stt-increase-advisory:1][^pse-cn-2017-0084-stt-increase-effectivity:1][^pse-cn-2018-0003-train-transition:1-2] | P |
| R1.2 | 2018-02-12 memo; applied in the recomposition effective 2018-02-19 | PSEi methodology | Free-float floor for PSEi (and sector indices) 12% to 15%; recomposition months March/September to February/August; financial criteria may be used for screening | Superseded for the float floor (R3.3) | [^pse-cn-2018-0013-index-policy-revision-2018:1][^pse-cn-2018-0014-index-recomposition-2018-02:1][^pse-index-policy-feb2018:5-6] | P |
| R1.3 | 2018-02 | Venue | HQ moves to PSE Tower (BGC); one unified trading floor replaces separate Makati and Pasig floors | Superseded (floor closed R3.15) | [^pse-pr-trading-floor-closed-2022-06-24] | P |
| R1.4 | 2018-03-22 | PSE corporate | PSE stock rights offering: 11.5M new shares at PHP252 (offer period 12-16 Mar 2018, listed 22 Mar 2018, PHP2.90bn gross), part of PSE's plan to bring trading-participant ownership within the 20% limit of SRC Sec. 33.2 and to fund the planned purchase of PDS Holdings; PSE's 2018 President's message says the offering and later administrative steps took TP ownership below 20% | Historical | [^pse-annual-report-2018:8][^pse-annual-report-2018:68] | P |
| R1.5 | 2018-04-10 (proposal) | Trading days | Proposed rule that PSE stays open on special non-working days in NCR and on government-only suspension days, with SCCP/CMIC "trading without settlement" guidelines; comments to 25 Apr 2018. Outcome not found | Proposed (adoption not verified) | [^pse-cn-2018-0023-trading-without-settlement-proposal:1] | P (proposal); outcome unknown |
| R1.6 | 2018-04-16 | PSE corporate (PDS) | PSE files an SEC Form 17-C rejecting a press report (Inquirer, 16 Apr 2018) that it had backed out of buying PDS Holdings after the share-purchase-agreement timetable lapsed on 31 Mar 2018; it says it remains committed to unifying the fixed-income and equity markets. The stake stayed at 20.98% until the Dec 2024 agreements (R5.14) | Historical | [^pse-17c-2018-04-16-pds-deal-clarification:3][^pse-annual-report-2025:19] | P |
| R1.7 | 2018-06-05 SEC approval; PSE memo 2018-06-22 | Short selling | SEC approves PSE Guidelines for Short Selling Transactions (eligible: PSEi members and ETFs; short-interest ratio at or below 10%); effectivity left "in due course" and in fact took until 2 Oct 2023 | Superseded (R4.11, R4.13) | [^pse-cn-2018-0035-short-selling-guidelines-sec-approved:1-2] | P |
| R1.8 | 2018-08-01 effective (SEC approval 2018-03-13) | Clearing fund | SCCP Rule 5.2 and Operating Procedure 4.3.1.3 amended: contributions to the Clearing and Trade Guaranty Fund (CTGF) become refundable, as trade-related assets, when a clearing member ceases business or terminates membership, for TPs and clearing members actively operating at the effective date; the 2013 rule had said there was no return of cash contributions (except excess initial contributions). SCCP's posted consolidated rulebook carries the 13 Mar 2018 revision date | In force (refund conditions changed 8 Jul 2025, R6.9) | [^sccp-clearing-house-rules-2018:35][^pse-sccp-revised-rules:35][^pse-annual-report-2018:47] | P |
| R1.9 | 2018-10-05 | Broker control | At CMIC's request PSE denies Meridian Securities access to the trading facilities for one day (start of day 5 Oct 2018); it may resume on the next trading day | Historical | [^pse-cn-2018-0048-cmic-denial-of-access-meridian:1] | P |
| R1.10 | 2018-10-29 (signed) | Foreign ownership | EO 65: 11th Regular Foreign Investment Negative List | Superseded (R3.16) | [^lawphil-eo-65-2018] | P |
| R1.11 | 2019-01-22/23 | Short selling | Guidelines amended: short orders barred only in pre-open and pre-close (previously also run-off), to match system configuration and SRC Rule 40.3.3 | Incorporated in Oct 2023 text | [^pse-cn-2019-0004-short-selling-guidelines-amendment:1] | P |
| R1.12 | 2019-02-05 BSP Circular 1030; PSE notice 2019-07-08 | Foreign investment access | BSP liberalised its FX rules: exchange-traded funds added to the instruments eligible for registered inward foreign investment (repatriation of capital and income through the banking system) | In force | [^pse-cn-2019-0037-foreign-investment-etf:1] | P |
| R1.13 | 2019-03-22 | Listing fees and offer rules | CN-2019-0012 introduces a new fee framework for listing applications, and CN-2019-0013 requires the price range to be disclosed for follow-on offerings and stock rights offerings of common shares and ETFs (titles from the CLDR supplemental-rule index; the texts were not read) | In force | [^pse-listing-disclosure-rules:14] | P (titles) |
| R1.14 | 2019-06-04 | Incident | Trading halted at 11:45 for a fire drill at PSE Tower; resumed 13:30; close unchanged at 15:30 | Historical | [^pse-cn-2019-0031-trading-halt-fire-drill:1] | P |

**B2. 2020**

| ID | Effective date | Area | Change (before to after) | Status | Sources | Ev |
|---|---|---|---|---|---|---|
| R2.1 | 2020-01-13 | Incident | No trading at PSE and no clearing or settlement at SCCP for the day (Taal volcano ash emission) | Historical | [^pse-cn-2020-0002-trading-suspension-2020-01-13:1] | P |
| R2.2 | 2020-02-07 | REIT regime | SEC approves PSE Amended REIT Listing Rules (effective immediately); SEC REIT Rules (MC 1-2020) effective the same date | In force | [^pse-cn-2020-0005-amended-reit-listing-rules:1][^sec-mc-1-2020-reit-irr:1] | P |
| R2.3 | 2020-02-25 | Short selling oversight | SEC-approved CMIC Implementing Guidelines on Securities Borrowing and Lending and Short Selling take effect (CMIC memorandum 2020-005 of 10 Feb 2020; effective 25 Feb 2020, fifteen days after publication); the guidelines' content beyond the cover memo was not re-read here | In force | [^cmic-sbl-short-selling-guidelines:1] | P |
| R2.4 | 2020-03-16 to 2020-03-19 | Session timetable | Shortened hours announced 15 Mar (16 Mar: 09:00 pre-open, 09:30 open, 12:45 pre-close, 12:50 run-off, 13:00 close); full suspension of trading and clearing from 17 Mar (ECQ); resumption Thu 19 Mar with 09:00/09:30/12:45/12:50/13:00 and trading floor closed (offsite trading). Extended 30 Apr, 15 May, then "until further notice" | Superseded 6 Dec 2021 (R3.4) | [^pse-cn-2020-0017:1][^pse-cn-2020-0021:1][^pse-cn-2020-0025-resumption-of-trading:1] | P |
| R2.5 | 2020-03-24 | Price limit | Lower static threshold 50% to 30% below reference price (SEC approval 20 Mar 2020); upper stays +50% | In force | [^pse-cn-2020-0028:1-2][^pse-pr-lower-static-threshold-2020] | P |
| R2.6 | 2020-05-04 | Circuit breaker | Single trigger (PSEi -10% = 15-minute halt) replaced by three levels: -10% / -15% / -20% = 15 / 30 / 60 minutes; each level once per day; level cut-off times defined against the then 15:15 pre-close (L1 until 14:55, L2 until 14:40, L3 until 14:10; shortened schedule 12:25 / 12:10 / 11:40). SEC approved 20 Mar 2020 | In force | [^pse-cn-2020-0044:1-4] | P |
| R2.7 | 2020-05-26 PSE notice | Foreign investment access | BSP confirms that non-resident investments in REIT securities (onshore-listed equity) can be registered for repatriation of capital and earnings | In force | [^pse-cn-2020-0052-nonresident-reit-investment:1] | P |
| R2.8 | 2020-06-01 | Floor and hours | GCQ in Metro Manila: trading floor reopens with health protocols; shortened hours continue | Superseded (R3.4, R3.15) | [^pse-cn-2020-0051-gcq-floor-reopening:1] | P |
| R2.9 | 2020-07-15 | REIT trading access | Only "eligible" TPs (REIT training attended, operational-readiness certification) may trade REIT shares; IPO allocations 20% brokers / 10% local small investors | In force (PSE REIT page still hosts the forms) | [^pse-cn-2020-0066-reit-broker-eligibility:1-2] | P |
| R2.10 | 2020-08-03 | MPO | SEC-approved PSE guidelines: IPO offer 33% or PHP50M (market cap to PHP500M), 25% or PHP100M (to PHP1bn), 20% or PHP250M (above PHP1bn); maintain at least 20%; listing by introduction and backdoor listing at least 20% | Superseded 11 Aug 2026 (R7.14) | [^pse-sr6-2-mpo-initial-backdoor-2020:1] | P |
| R2.11 | 2020-08-13 | Products | First REIT (AREIT) lists on the Main Board; PSE's list of REIT listings now shows AREIT, DDMPR, FILRT, MREIT, RCR, CREIT, VREIT, PREIT | Historical | [^pse-web-new-listings] | P |
| R2.12 | 2020-08-14 | Listing rules (SME lock-up) | CN-2020-0080 revises the mandatory lock-up rule for SME Board listings (title from the CLDR supplemental-rule index; the text was not read) | Superseded in part (lock-up amendments of 13 Jun 2022, R3.13) | [^pse-listing-disclosure-rules:14] | P (title) |
| R2.13 | 2020-09-11 approved (RA 11494; effective on publication) | Tax (Bayanihan II) | NIRC Sec. 127(B), the IPO tax, is repealed (Sec. 6 of RA 11494): it had charged 4% / 2% / 1% of the gross selling price of shares of a closely held corporation sold through an IPO, by the share of outstanding stock sold, paid by the issuer (primary) or the seller (secondary). CMEPA later re-used subsection (B) for domestic shares listed abroad (R6.7), so the current Code has no IPO tax; the STT on listed-share sales is untouched | In force | [^ra-11494-bayanihan-ii:20][^ra-11494-bayanihan-ii:25][^ra-8424-nirc-1997:165-166][^ra-12214-cmepa:16] | P |
| R2.14 | 2020-12-21 | Voluntary delisting | SEC-approved amendments to the Voluntary Delisting Rules, effective immediately: approval by two-thirds of the entire board (including a majority, and not fewer than two, of the independent directors) and by holders of two-thirds of outstanding and listed shares, with votes against at most 10%; minimum tender price is the higher of the independent fairness-opinion valuation (SRC Rule 19.2.6) and the one-year VWAP before the board-approval disclosure | In force (2023 proposals to amend, R4.9, not confirmed adopted) | [^pse-sr8-1-voluntary-delisting-2020:1] | P |

**B3. 2021-2022**

| ID | Effective date | Area | Change (before to after) | Status | Sources | Ev |
|---|---|---|---|---|---|---|
| R3.1 | 2021-03-24 | Listing rules (Main and SME boards) | CN-2021-0021: SEC (approval of 4 Feb 2021) amends the Main Board and SME Board listing rules (Art. III Parts D and E) and adds Part E-1, SME Board listing under a sponsor model; replaces the 2013 Main/SME rules (CN-2013-0023); temporary COVID relief for IPO applications filed in 2021 and 2022 (profitability may be judged on any two of the three latest fiscal years, excluding the year of impact). Effective immediately | In force | [^pse-cn-2021-0021-amended-listing-rules:1-2][^pse-listing-disclosure-rules:5][^pse-listing-disclosure-rules:14] | P |
| R3.2 | 2021-03-26 approved (RA 11534 CREATE) | Tax | Corporate income tax 30% to 25% from 1 Jul 2020 (20% for small firms); non-resident foreign corporation income tax 30% to 25% from 1 Jan 2021; final tax on non-resident foreign corporation dividends 15% only if the home country credits tax, else 25%. Act effective 15 days after publication (secondary: 11 Apr 2021) | In force | [^ra-11534-create:6][^ra-11534-create:11][^ra-11534-create:77] | P (11 Apr date: S/I) |
| R3.3 | 2021-08-05 memo; 2021-08-16 | PSEi methodology | Float floor 15% to 20% (first applied at the Dec 2022 review, i.e. the Feb 2023 recomposition); early-inclusion provision; PSEi insertion if ranked 25th or higher and removal if 36th or lower by full market cap | In force (partly replaced at the Feb 2027 rebalance, P13) | [^pse-cn-2021-0046-index-policy-revision-2021:1] | P |
| R3.4 | 2021-12-06 | Session timetable | New full-day schedule: 09:00 pre-open, 09:30 open, 12:00 recess, 13:00 resume, 14:45 pre-close, 14:50 run-off, 15:00 close. PSE calls it the "pre-pandemic" schedule, but the pre-March-2020 schedule resumed at 13:30 and closed at 15:30 (see conflicts C1) | Superseded 1 Mar 2024 for the close time (R5.4) | [^pse-cn-2021-0059:1] | P |
| R3.5 | 2021-12-24 and 2021-12-31 | Session timetable | Half-day trading: 09:00 pre-open, 09:15 no-cancel, 09:30 open, 11:55 pre-close, 11:58 no-cancel, 12:00 run-off, 12:10 close (the last documented use of a half-day timetable) | Historical | [^pse-cn-2021-0063-half-day-trading-2021-12:1] | P |
| R3.6 | 2022-01-04 | Incident | Trading cancelled for the day: failure to connect the Nasdaq trading engine and the Flextrade front-end (43 of 125 TPs could not connect) | Historical | [^pse-cn-2022-0001-delay-market-opening:1][^pse-cn-2022-0002-cancellation-of-trading-2022-01-04:1] | P |
| R3.7 | 2022-01-14 to 2022-02-28 | Session timetable | Omicron shortened schedule: 09:00 pre-open, 09:15 no-cancel, 09:30 open, 12:45 pre-close, 12:48 no-cancel, 12:50 run-off, 13:00 close (to 31 Jan; run to 28 Feb is implied by R3.8) | Historical | [^pse-cn-2022-0004:1][^pse-cn-2022-0009-trading-schedule-mar-2022:1] | P/I |
| R3.8 | 2022-03-01 | Session timetable | Full-day schedule restored with 09:15 and 14:48 no-cancel phases listed | Superseded 1 Mar 2024 (close) | [^pse-cn-2022-0009-trading-schedule-mar-2022:1] | P |
| R3.9 | 2022-03-01 | Disclosure timing | EDGE posting cut-off set at 3:30 pm: disclosures received by then are released the same trading day, later ones the next trading day (effective with the return to the full-day schedule) | Superseded 25 May 2026 (R7.10) | [^pse-cn-2022-0010-edge-cutoff-330pm:1] | P |
| R3.10 | 2022-03-02 and 2022-03-21 approved | Foreign ownership | RA 11647 amends the Foreign Investments Act; RA 11659 amends the Public Service Act: "public utility" (60/40 Filipino ownership) limited to six categories (electricity distribution, electricity transmission, petroleum pipelines, water and sewerage pipelines, seaports, public utility vehicles); Sec. 34 amends the foreign-ownership limits in the laws covering BOT projects, domestic shipping, civil aviation, toll roads, transport network vehicles and public telecommunications (RA 7925), so telecoms, airlines, shipping and toll operators are no longer constitutional "public utilities". Both Acts effective 15 days after publication | In force | [^ra-11647-foreign-investments-act-amendments:8][^ra-11659-public-service-act-amendments:4][^ra-11659-public-service-act-amendments:14][^ra-11659-public-service-act-amendments:15] | P |
| R3.11 | 2022-03-28 | Indices | PSE MidCap and PSE Dividend Yield indices launched (20 members each; base 1,000 at 30 Dec 2010; float floor 15% at launch) | In force | [^pse-cn-2022-0013-launch-midcap-divy-indices:1-3][^pse-pr-new-indices-2022-03-28] | P |
| R3.12 | 2022-05-24 | Listing rules (preferred shares) | CN-2022-0023: rule on initial listing through a preferred-share offering without listing common shares: minimum public offering of PHP1bn or 20% of the market capitalisation of the preferred shares, at least 1,000 holders each with at least one board lot, 20% public ownership maintained | Superseded 12 Aug 2026 (R7.15) | [^pse-listing-disclosure-rules:14][^pse-listing-disclosure-rules:90-91] | P |
| R3.13 | 2022-06-13 | Listing rules (REIT, local small investors, lock-up) | Three amendment memos take effect: MEA-2022-0001 (REIT listing rules: lock-up exemption and stockholders' equity), MEA-2022-0002 (rules for Local Small Investors) and MEA-2022-0003 (lock-up rule in the Main and SME Board listing rules); titles from the CLDR index, texts not re-read here | In force | [^pse-listing-disclosure-rules:13][^pse-listing-disclosure-rules:14] | P (titles) |
| R3.14 | 2022-06-22 | Listing rules (backdoor listing) | CN-2022-0026 (further amending CN-2022-0024 of 26 May 2022) sets the Revised Rules on Backdoor Listing: PSE suspends trading immediately after evaluating the disclosure and lifts the suspension one full trading day after it disseminates the comprehensive corporate disclosure (and any SEC confirmations); a one-hour halt follows disclosure of the final price of the mandatory follow-on offering; effective immediately | In force | [^pse-sr7-backdoor-listing-2022:1][^pse-sr7-backdoor-listing-2022:4] | P |
| R3.15 | 2022-06-24 last floor day; floorless from 2022-06-27 | Venue | Trading floor closed permanently (only 29 of 85 booth-leasing TPs renewed) | In force | [^pse-pr-trading-floor-closed-2022-06-24] | P |
| R3.16 | 2022-06-27 signed | Foreign ownership | EO 175: 12th Regular Foreign Investment Negative List (replaced the 11th); effective 15 days after publication | Superseded by EO 113 (R7.7) | [^eo-175-2022-12th-finl:1] | P |
| R3.17 | 2022-09-21 announced; live Aug 2023 | Retail access | GCash "GStocks" (AB Capital Securities as broker, PSE tech support) announced; PSE later reports over 1.7 million registered users and 15,000 on Maya Stocks | In force | [^pse-pr-gcash-gstocks-2022-09-21][^pse-analyst-briefing-3m-2026:21] | P |
| R3.18 | 2022-09-26 | Incident | Typhoon: no trading and no clearing/settlement | Historical | [^pse-cn-2022-0035-trading-suspension-2022-09-26:1] | P |
| R3.19 | 2022-11-16 consultation | Disclosure halts and trading rules | CN-2022-0045 (2022 amendments, Part II; comments to 1 Dec 2022) proposes making a disclosure-halt request voluntary and removing the automatic halt when an issuer fails to confirm or deny a rumour (penalties instead); the Jan 2025 consolidated rules still carry the old wording | Proposed (adoption not found) | [^pse-cn-2022-0045-consultation-2022-part-ii:1][^pse-cn-2022-0045-consultation-2022-part-ii:4][^pse-listing-disclosure-rules:145] | P; adoption unknown |

**B4. 2023**

| ID | Effective date | Area | Change (before to after) | Status | Sources | Ev |
|---|---|---|---|---|---|---|
| R4.1 | 2023-02-20 (SCCP memo 2023-02-10; SEC approval 2022-12-13) | Clearing collateral | SCCP Rule 8.1.8: securities of the PSEi, MidCap and Dividend Yield indices (and PSE shares) accepted as collateral in the mark-to-market collateral deposit (MMCD) system, haircut 25% (PSE shares 35%), aligned with the RBCA position-risk factors; effective Monday 20 Feb 2023. The eligible list follows PSE's index reviews (latest archived: memo 01-0126 of 28 Jan 2026, effective 2 Feb 2026: PSEi adds RCR and drops AGI; MidCap adds AGI and APX and drops DD and RCR; Dividend Yield adds OGP and URC and drops KEEPR and SECB) | In force | [^sccp-memo-02-0223-collateral-haircut-rates:1-2][^sccp-memo-01-0126-eligible-collateral-list:1] | P |
| R4.2 | 2023-03-07 to 2023-03-21 | Listing rules (sponsors, issued shares) | CN-2023-009 (7 Mar 2023) sets documentary requirements and fees for accrediting sponsors and for SME listing under the sponsor model; CN-2023-0012 (21 Mar 2023) issues implementing guidelines for the listing of issued and outstanding shares (titles from the CLDR index; the texts were not read) | In force | [^pse-listing-disclosure-rules:15] | P (titles) |
| R4.3 | 2023-03-09 | Listing rules (REIT) | CN-2023-0010 issues the 2023 amendments to the Amended REIT Listing Rules and the consolidated listing rules; the 2023 text requires a 90% distribution policy and public-company status on and after listing (at least 1,000 public shareholders each holding at least 50 shares, together at least one-third) and does not apply the three-year same-business test to REITs (which of these provisions are new in 2023 was not isolated) | In force | [^pse-listing-disclosure-rules:13][^pse-sr3-2-reit-listing-amend-2023:2] | P |
| R4.4 | 2023-03-27 | Clearing | SCCP moves to LSEG Technology Millennium Clearing/Risk (multi-currency; settles multiple trade dates in one day; prerequisite for T+2) | In force | [^pse-pr-sccp-new-clearing-system-2023-03-31] | P |
| R4.5 | 2023-05-12 | Listing rules (price stabilisation) | CN-2023-0022 inserts CLDR Art. III Part A Sec. 13: an applicant conducting a secondary offering must hold a stabilisation fund (offers up to PHP10bn: 10-15% of the base offer; PHP10-25bn: 12.5-15%; above PHP25bn: 15%); stabilisation may not breach the minimum public ownership; weekly reports to PSE; prior SEC approval; effective immediately | In force | [^pse-cn-2023-0022-stabilization-fund:1-2] | P |
| R4.6 | 2023-05-24 | SBL | SEC approves offshore collateral for SBL with at least one foreign party (cash USD/EUR/JPY/GBP/AUD; OECD government/agency debt rated BBB or better; constituents of WFE-member benchmark indices), for Qualified Buyers as defined in SRC Rule 10.1.3 as amended by SEC MC 6-2021 (a client of a prime broker must itself be a Qualified Buyer). PDTC received the SEC's approval (called conditional in PSE's Oct 2023 retail webinar deck) to act as a Lending Agent on 21 Jul 2023 | In force | [^pse-cn-2023-0027-offshore-collateral-sbl:1][^pse-cn-2023-0048:2][^pse-asm-2024-presidents-report:24][^pse-sbl-short-selling-webinar-2023:3] | P |
| R4.7 | 2023-08-23 | Clearing (client assets, buy-ins) | SCCP memo 07-0823: SEC-approved amendments in force immediately: Rule 2.3.5 bars clearing members from using one client's shares to settle another client's obligations unless under a securities borrowing and lending arrangement; buy-in and sell-out trades settle earlier than the regular cycle where practicable; settlement dates are adjusted for holidays and unexpected events; multiple trade dates can settle in one day | In force | [^sccp-memo-07-0823-sec-approved-amendments:1-2] | P |
| R4.8 | 2023-08-24 | Settlement | T+3 to T+2 (first T+2 trade date 24 Aug; SEC En Banc approval 10 Aug). Trades of 23 Aug (last T+3) and 24 Aug (first T+2) both settled on 29 Aug 2023. Ex-date moves to one trading day before record date. Deadline 12:00 noon (temporarily 13:00 until 11 Sep). SCCP rule amendments effective on go-live | In force | [^pse-cn-2023-0031-t2-settlement:1-2][^pse-cn-2023-0040-t2-go-live:1-3][^sccp-memo-06-0823-sec-approval-t2-amendments:1][^sccp-memo-07-0823-sec-approved-amendments:1] | P |
| R4.9 | 2023-08-25 consultation | MPO | PSE proposes amendments to the Public Ownership Guidelines, the Amended MPO Rule and the Amended Voluntary Delisting Rules (codify MPO levels by listing vintage and monthly public-ownership-report triggers; delisting vote basis); comments to 8 Sep 2023. Adoption date not found; the Aug 2026 rule restates the codified levels | Proposed (outcome unclear) | [^pse-cn-2023-0041-mpo-delisting-consult:1-3] | P; adoption unknown |
| R4.10 | 2023-09-05 consultation | Algorithmic trading / VWAP | PSE proposes allowing algorithmic trading (DMA Rules then prohibited it via DMA, with exemptions for child orders of conditioned parent orders) and a VWAP facility. VWAP adopted (R5.4); no approval notice for the algorithmic-trading part was found | Algo part: Proposed (outcome unknown); VWAP part: In force | [^pse-cn-2023-0043:2][^pse-cn-2023-0043:4] | P; algo outcome unknown |
| R4.11 | 2023-10-02 | Short selling | PSE Guidelines for Short Selling Transactions declared effective; eligible set widened from PSEi + ETFs to PSEi + MidCap + Dividend Yield + ETFs; BIR (letter 6 Sep 2023; PSE's Oct 2023 deck says PSE received the confirmation on 25 Sep 2023) accepts registration of a GMSLA with a foreign party; offshore collateral recognised | In force | [^pse-cn-2023-0048:1-2][^pse-cn-2023-0048:8][^pse-pr-short-selling-effectivity-2023-10-02][^pse-sbl-short-selling-webinar-2023:3] | P |
| R4.12 | 2023-10-09 consultation | Board lot | Proposal to cut lot sizes to allow a PHP100 minimum investment (e.g. 1,000,000 to 20,000; 100 to 20 for 5-9.99; 10 to 2 for 50-99.95; 10 to 1 for 100+); comments to 23 Oct 2023. PSE's July 2024 report says it was "awaiting SEC approval" (maximum lot 1,000,000 cut to 20,000; minimum 5 cut to 1); no approval was ever announced, the July 2025 report does not mention it, and the Dec 2025 paper shows the old table as "existing" and proposes one-share lots instead | Abandoned (filed, never approved, replaced by R6.15; I) | [^pse-cn-2023-0051:1][^pse-cn-2023-0051:3-4][^pse-asm-2024-presidents-report:18][^pse-cn-2025-0046-board-lot-trading-at-last:4] | P; "abandoned" is I |
| R4.13 | 2023-11-06 | Short selling | Program go-live (postponed from 23 Oct 2023 to give more preparation time); FEOMS recertification needed to tag short sales; Daily Short Sell Report published; its first edition (6 Nov 2023) lists 53 eligible securities, all with zero volume | In force | [^pse-cn-2023-0056:1][^pse-dssr-2023-11-06:1-2][^gma-2023-10-20-short-selling-nov-6] | P |

**B5. 2024**

| ID | Effective date | Area | Change (before to after) | Status | Sources | Ev |
|---|---|---|---|---|---|---|
| R5.1 | 2024-01-03 | Incident | Market halted 09:32; resumed 11:56 (technical issue with a third-party front-end provider); afternoon on schedule | Historical | [^pse-cn-2024-0001-market-halt:1][^pse-cn-2024-0003-update-market-halt:1] | P |
| R5.2 | 2024-01-26 memo; effective 2024-02-05 | PSEi methodology | Pension-fund/SSS/GSIS shares counted as free float unless the fund has a board seat (effective immediately); semiannual membership changes effective 5 Feb 2024 | In force | [^pse-cn-2024-0008:1] | P |
| R5.3 | 2024-01-30 | PSE governance | Supreme Court decides three consolidated petitions over PSE Nomelec rules on broker voting in PSE (G.R. 198425, 201174, 244462): injunctions against the SEC are reversed; the injunction against PSE and PSE Nomelec is affirmed (for Rule 2 of the 2010 Nomelec rules in G.R. 244462) | Historical | [^pse-annual-report-2025:11] | P |
| R5.4 | 2024-02-01 SEC-approved rules effective; 2024-03-01 go-live | Closing sequence | VWAP Trading Rules: Closing VWAP session 15:00-15:15; market close 15:00 to 15:15 (half-day: Closing VWAP 12:10-12:25, close 12:25). VWAP trades at least PHP500,000, single TP, executed only in the 15 minutes after run-off at the full-day VWAP computed by PSE (excluding block sales, intentional crosses and odd lots) | In force | [^pse-approved-rules-vwap-trading-2024:1][^pse-approved-rules-vwap-trading-2024:3][^pse-approved-rules-vwap-trading-2024:7][^pse-cn-2024-0012-vwap-go-live:1][^pse-pr-vwap-2024-02-16] | P |
| R5.5 | 2024-03-05 memo (SEC approval 2024-01-09) | Settlement batch | SCCP Operating Procedure 2.5.3.2: the settlement batch run (normally 12:00) may start earlier once all cash and securities obligations are delivered, with 10 minutes' notice to clearing members and settlement banks | In force | [^sccp-memo-01-0324-early-batch-run-effectivity:1] | P |
| R5.6 | 2024-03-25 | Clearing member sanction | SCCP suspends EquitiWorld Securities as a clearing member from 25 to 27 Mar 2024 under Rule 2.5.1 for persistent or repeated late cash payments from Feb 2020 to Nov 2023; the SEC's involuntary suspension follows in Oct 2024 (R5.12) | Historical | [^sccp-memo-03-0324-clearing-member-suspension:1] | P |
| R5.7 | 2024-04-11 | Foreign investment registration (BSP) | BSP Circular 1192 amends the FX Manual, including the sections on registering inward investments. In the manual as updated in May 2025, equity securities listed at an onshore exchange (e.g. PSE), ETFs and PDRs are registered when the registering authorised agent bank (AAB) reports them to the BSP, and a BSRD is no longer issued for them; the circular itself was not retrieved, so which amendment introduced the AAB-only route is not established | In force | [^bsp-fx-manual-morfxt-2025-05:42][^bsp-fx-manual-morfxt-2025-05:46] | P (route); date from the manual's amendment footnotes |
| R5.8 | 2024-04-18 | Commission | SEC MC 7-2024 (16 Apr 2024) removes the minimum broker commission; PSE's minimum-commission rule (0.25% to 0.05% bands) ceased to be in force; PD 154 maximum of 1.5% remains | In force | [^pse-cn-2024-0029-min-commission-removal:1-3][^pse-pr-cmepa-day1-2025-07-01] | P |
| R5.9 | 2024-06-05 | SBL tax | BIR RR 10-2024 amends RR 10-2006: MSLA/GMSLA approval retroacts to complete submission; one registration for multilateral MSLA with accession agreements; counterparties may switch lender/borrower roles | In force | [^pse-cn-2024-0035:1-2] | P |
| R5.10 | 2024-09-26 consultation | Products | PSE Rules for Global Philippine Depositary Receipts (GPDR) opened for comment to 16 Oct 2024 | Proposed (awaiting SEC; see Section 2) | [^pse-cn-2024-0047:1] | P |
| R5.11 | 2024-09-30 consultation | Disclosure and trading rules | CN-2024-0048 (comments to 11 Oct 2024) proposes extending the black-out rule to the issuer itself (no sale or buy-back) with a 30-calendar-day earnings black-out, capping the penalty for trading unlisted shares at PHP50m and, in the Revised Trading Rules, leaving the liquidation of error-account positions to the trading participant (no one-month limit) | Proposed (adoption not found) | [^pse-cn-2024-0048-consultation-blackout-rule:1][^pse-cn-2024-0048-consultation-blackout-rule:4-5][^pse-cn-2024-0048-consultation-blackout-rule:9-10] | P; adoption unknown |
| R5.12 | 2024-10-09/10 | Broker failure | SEC involuntary suspension and preservation order against Equitiworld Securities; CMIC special audit of its books; CMIC later took over its operations (PSE circular titled "Take Over of the Operations of Equitiworld Securities, Inc.", Nov 2024) | Historical (liquidation plan approved Mar 2026, R7.5) | [^pse-cn-2024-0053-equitiworld-involuntary-suspension:1][^pse-web-announcements-archive] | P (take-over: title only) |
| R5.13 | 2024-12-09 | Incident | Pre-open delayed; open moved to 09:55 | Historical | [^pse-cn-2024-0061-adjusted-schedule-2024-12-09:1] | P |
| R5.14 | 2024-12-26 | Corporate | PSE signs to buy 61.92% of PDS Holdings (PHP600/share, PHP2.32bn) on top of its 20.98%; PDS consolidated as a majority-owned subsidiary in Dec 2024 | In force (ownership 94.55% at 5 Mar 2026) | [^pse-pr-pds-acquisition-2024-12-26][^philstar-2025-12-24-pds-landbank][^pse-analyst-briefing-3m-2026:25] | P/S |

**B6. 2025**

| ID | Effective date | Area | Change (before to after) | Status | Sources | Ev |
|---|---|---|---|---|---|---|
| R6.1 | 2025-01-02 | Listing fees | Upper limit of the annual listing maintenance fee (ALMF) raised from PHP2.0m to PHP3.5m per Main Board company (rate 1/100 of 1% of market capitalisation, floor PHP250,000); the SME Board ALMF is unchanged (PHP100 per PHP1m, PHP50,000 to PHP250,000). SEC-approved; circular dated 19 Dec 2024 | In force | [^pse-cn-2024-0068-almf-effectivity:1] | P |
| R6.2 | 2025-01-21 memo (effective immediately) | Settlement allocation and risk containment | SEC approves SCCP Rule 3.4 with a new Annex 11: when SCCP cannot pay every member in full it settles by price first (highest buy price and lowest sell price), then lowest quantity, then a pseudo-random process, and may make partial securities deliveries; this replaces the old priority list that settled the largest outstanding netted amounts first. Also approved: Rule 5.1.4(3) (supplemental CTGF contributions, with SEC approval, when the fund no longer matches trade volume), Rule 6.2.8 (a defaulting member bears costs, taxes and lost interest on Clearing Fund advances) and Rule 7.6 (early delivery by SD-1 in five situations) | In force | [^sccp-memo-02-0125-sec-approval-rules-3-4-5-1-4-6-2-8-7-6:1-3] | P |
| R6.3 | 2025-02-24 to 2025-05-15 | PSE corporate (PDS) | After the Dec 2024 agreements (R5.14), PSE reports its stake in PDS Holdings at 78.33% (24 Feb 2025), 79.9% (end-Mar 2025) and 91.6% (15 May 2025), up from 20.98% | In progress (94.55% at 5 Mar 2026) | [^pse-press-fy2024-results][^pse-press-q1-2025-results] | P (issuer press releases) |
| R6.4 | 2025-03-19 (reported) | IPO float | PSE's CEO says the SEC approved a temporary cut in the minimum public ownership for IPOs from 20% to 15%, on condition of a follow-on offering or private placement within two to three years to reach 20% (extendable by two years); no PSE circular found | Unclear (overtaken by the tiered MPO rule of 11 Aug 2026, R7.14) | [^tribune-pse-eases-float-2025] | S |
| R6.5 | 2025-03-24 | Incident | System connectivity issue: market open delayed to 11:10 | Historical | [^pse-cn-2025-0015-adjusted-schedule-2025-03-24:1] | P |
| R6.6 | 2025-05-22 | Technology | PSE and Nasdaq announce the upgrade from PSEtrade XTS to Nasdaq Eqlipse Trading | Approved, not yet effective (NTE, Section 2) | [^pse-pr-nasdaq-eqlipse-2025-05-22][^pse-analyst-briefing-3m-2026:24] | P |
| R6.7 | 2025-07-01 (signed 2025-05-29) | Tax (RA 12214 CMEPA) | STT 0.6% to 0.1% of gross selling price on "shares of stock and other securities" listed and traded on a local exchange (and, new, on domestic shares listed on foreign exchanges), with "securities" defined broadly; sale of listed shares exempt from DST; DST on original issuance 1% to 0.75%; final tax on bank interest 20%. PSE applies 0.1% to trades from 1 Jul 2025 (Tuesday) | In force | [^ra-12214-cmepa:3][^ra-12214-cmepa:16][^ra-12214-cmepa:17-18][^ra-12214-cmepa:25][^pse-cn-2025-0026-stt-decrease-advisory:1][^pse-cn-2025-0028-cmepa-effectivity:1][^bir-rr-20-2025-stt:4][^pse-pr-cmepa-day1-2025-07-01][^pse-analyst-briefing-3m-2026:20][^pse-annual-report-2025:39] | P |
| R6.8 | 2025-07-04 / 2025-07-15 | Tax operations | BIR advisory: eBIRForms/eFPS lacked the new STT rate, so brokers file BIR Form 2552 manually and pay at an Authorized Agent Bank | Interim (current status not checked) | [^pse-cn-2025-0032-bir-stt-advisory:1] | P |
| R6.9 | 2025-07-08 memo (effective immediately) | Clearing fund | SEC approves amended SCCP Rule 5.2 and Operating Procedures 4.2.1.3 on the refund of Clearing and Trade Guaranty Fund contributions when a clearing member ceases business: regulatory clearances and the SEC cancellation order, all liabilities settled, and audited proof that the member shouldered the contributions rather than collecting them from clients (refund only to the extent proved) | In force | [^sccp-memo-01-0725-ctgf-refund-sec-approval:1-2] | P |
| R6.10 | 2025-07-09 | Broker suspension | CMIC places Globalinks Securities & Stocks under involuntary suspension for continuing breaches of the capitalisation (RBCA) requirements of CMIC Rules Art. VIII (access to PSE, PDTC and SCCP systems restricted; client transfers and done-through sells allowed with CMIC approval; proprietary and related-party trades barred); CMIC lifts it on 14 Oct 2025 after a capital infusion | Historical (lifted) | [^pse-tpa-2025-0040-globalinks-involuntary-suspension:1-2][^pse-tpa-2025-0061-globalinks-lifting-of-suspension:1-2] | P |
| R6.11 | 2025-08-05 | Tax regulations | BIR RR 19-2025 (DST), RR 20-2025 (STT; signed 29 Jul, effective 1 Jul 2025), RR 21-2025 (CMEPA income-tax provisions) | In force | [^bir-rr-19-2025-dst:1][^bir-rr-20-2025-stt:1][^bir-rr-20-2025-stt:4][^bir-rr-21-2025-cmepa-income:1] | P |
| R6.12 | 2025-08-09 effective; 2025-08-11 first trading day | Share classes | SEC MC 10-2025 (7 Aug) repeals the 1973 Class A/B regular-board rule: buyers receive the class they bought (from 11 Aug 2025); companies must declassify by amending Articles by 9 Aug 2026; PSE (10 Sep 2026): two-day trading suspension before delisting of the classified shares, price adjusted to the higher of the A/B closes | In force; migration ongoing (PSE's directory of 6 Oct 2026 still lists five A/B pairs separately: ATN/ATNB, FJP/FJPB, LC/LCB, MA/MAB, OPM/OPMB) | [^pse-cn-2025-0035-sec-declassification-mandate:1-3][^pse-cn-2025-0036-declassification-effectivity:1][^pse-cn-2026-0041-declassification-price-suspension:1-2][^pse-listed-company-directory-frame] | P |
| R6.13 | 2025-08-13 | Broker failure | CMIC places Mount Peak Securities under involuntary suspension (investigations over capitalisation requirements; access to PSE, PDTC and SCCP restricted; clients may request transfers or done-through sells with CMIC approval; proprietary and related-party trades barred) | Historical (later status not checked) | [^pse-tpa-2025-0050-mount-peak-involuntary-suspension:1-2] | P |
| R6.14 | 2025-08-20 (SEC-approved) | Halts and calamities | Market-wide halt trigger changed from "at least one-third of TPs cannot access the system" to "TPs with more than 50% of six-month ADTV (ex-block) cannot trade, directly or via their correspondent TP"; every TP needs a correspondent TP; new calamity guidelines (signal 3-5 in NCR = no trading). Consulted in May 2022 (CN-2022-0020) and, for Part XXI of the Implementing Guidelines and the natural-disaster guidelines, on 17 Oct 2023 (CN-2023-0055; comments to 24 Oct 2023) | In force | [^pse-cn-2025-0037:1-2][^pse-cn-2025-0037:4][^pse-cn-2022-0020-market-halt-consultation:4][^pse-cn-2023-0055:1][^pse-annual-report-2025:40] | P |
| R6.15 | 2025-12-15 consultation | Lot size / closing | PSE proposes One Lot One Share, a new tick table, removal of the odd-lot market and a change to run-off/trading-at-last matching, tied to the new engine; comments to 31 Dec 2025 | Proposed (Section 2) | [^pse-cn-2025-0046-board-lot-trading-at-last:1][^pse-cn-2025-0046-board-lot-trading-at-last:3-5] | P |
| R6.16 | 2025-12-19 | Products (warrants) | Alliance Global Group's 2.2bn warrants (AGIW) list: PHP12 exercise price, five-year exercise period, PHP1.1bn gross proceeds; +100% on the first day (warrants are exempt from the static price limit) | In force | [^pse-press-agi-warrants][^pse-revised-trading-rules:20] | P |
| R6.17 | 2025-12-24 | Corporate | PSE raises its PDS stake to 94.21% (Landbank shares); DBP the main holdout (3.08%) | In progress | [^philstar-2025-12-24-pds-landbank] | S |
| R6.18 | 2025-12-26 (effective 2026-01-05) | Sector classification | CN-2025-0047 reclassifies 13 companies effective Monday 5 Jan 2026 (for example DITO from IT services to telecommunications, ATN from Holding Firms to Industrial, UNH, WIN and JAS to Property); sector-index membership changes accordingly. PSE classifies a company by the activity that generates at least 60% of its revenue | In force | [^pse-cn-2025-0047-sector-reclassification:1-2] | P |

**B7. 2026 (to 6 Oct)**

| ID | Effective date | Area | Change (before to after) | Status | Sources | Ev |
|---|---|---|---|---|---|---|
| R7.1 | 2026-01-19 | Incident | PSE EDGE disclosure system outage; one-hour news halt of MRC shares (09:30-10:30) | Historical | [^pse-cn-2026-0004-2-emergency-disclosures-trading-halt:1-2] | P |
| R7.2 | 2026-01-25 (SEC MC 1-2026 issued 8 Jan) | REIT regime | REIT eligible assets widened (indirect holdings through 2/3-owned SPVs; toll roads, railways, airports, ICT, energy, data centres; reinvestment period 2 years) | In force | [^pse-analyst-briefing-3m-2026:17][^philstar-2026-07-17-sec-accomplishments] | P/S |
| R7.3 | 2026-02-02 | Dynamic threshold | Semiannual reclustering (Jul-Dec 2025 data); cluster rules unchanged | Superseded by R7.13 | [^pse-tpa-2026-0002-dynamic-threshold-review:1] | P |
| R7.4 | 2026-02 (SEC MC 11-2026 signed; effective on publication) | MPO | New SEC minimum-public-ownership rules for listed issuers | In force (PSE rule R7.14) | [^pse-cn-2026-0020-mpo-consult:7-10] | P |
| R7.5 | 2026-03-19 | Broker failure | CMIC notice (relayed by PSE): SEC approves CMIC's proposed liquidation and allocation plan for distributing Equitiworld Securities' trade-related assets | In progress | [^pse-cn-2026-0012:1] | P |
| R7.6 | 2026-04-03 | Universe | Asian Terminals (ATI) delisted voluntarily (approved 25 Mar 2026) | Historical | [^pse-cn-2026-0013-ati-voluntary-delisting:1] | P |
| R7.7 | 2026-04-13 signed; effective 15 days after publication (reported 1 or 2 May 2026) | Foreign ownership | EO 113: 13th Regular Foreign Investment Negative List. List A (constitution/specific laws): no foreign equity in mass media and internet business, corporate practice of architecture, cooperatives, private security, small-scale mining, marine resources; up to 25% private recruitment and defense-related construction; 30% advertising; 40% for public utilities (the six RA 11659 categories), natural resources including water (renewables fully open), private land, retail trade with paid-up capital under PHP25M, educational institutions, rice and corn, government procurement, fishing vessels, condominiums; telecom operation and management 100% with reciprocity, 50% without (RA 11659 Sec. 25). List B (security, health, SMEs): 40% for firearms/explosives, military materiel (RA 12024), gambling, micro and small domestic enterprises under US$200,000 paid-in capital. KPMG reports the telecom, architecture, retail and materiel items as changes from the 12th list | In force | [^eo-113-2026-13th-finl:1-2][^eo-113-2026-13th-finl:3-7][^kpmg-2026-04-13th-finl] | P (change-vs-12th: S) |
| R7.8 | 2026-04-22 (PDS memo); 2026-05-18 (PSE CN-2026-0022) | SBL | PDTC Lending Agency Service onboards first lenders and borrowers with BIR-registered agreements (cash collateral); more participants invited | In force | [^pse-cn-2026-0022:1-2] | P |
| R7.9 | 2026-05-15 SEC approval, effective immediately; PSE memo 2026-05-22 | SBL approvals | SEC approves PSE's 2026 Revised Guidelines for MSLA clearance: PSE acts as one-stop shop for MSLA and accession-agreement pre-clearance and BIR registration (no separate SEC and BIR approval per MSLA). Press adds that registration time falls from 7 to 5 working days and the SEC fee of PHP5,030 is removed (Philstar, 10 Jun 2026) | In force | [^pse-cn-2026-0025:1][^philstar-2026-06-10-sec-msla][^pse-analyst-briefing-1h-2026:9] | P/S |
| R7.10 | 2026-05-25 | Disclosure timing | EDGE posting cut-off moves from 3:30 pm to 4:00 pm (CN-2026-0024 of 22 May 2026): disclosures received by 4:00 pm are released the same trading day, later ones the next trading day; the submission system stays open after the cut-off. Supersedes the 3:30 pm cut-off of 1 Mar 2022 (R3.9) | In force | [^pse-cn-2026-0024-edge-cutoff-4pm:1] | P |
| R7.11 | 2026-07-31 | Broker failure | CMIC imposes involuntary suspension on Benjamin Co Ca & Company, Inc. | Historical (status after suspension not checked) | [^pse-tpa-2026-0035-benjamin-co-ca-involuntary-suspension:1] | P |
| R7.12 | 2026-08-03 | Indices and back-office | PSEi: Maynilad (MYNLD) in, Converge (CNVRG) out; MidCap, DivY and sector changes; new PSE Portal go-live for back-office files | In force | [^pse-cn-2026-0035:1][^pse-nte-faq-2026-08:2] | P |
| R7.13 | 2026-08-07 | Dynamic threshold | Semiannual reclustering (Jan-Jun 2026 data) | In force | [^pse-tpa-2026-0036-dynamic-threshold-review:1] | P |
| R7.14 | 2026-08-11 | MPO | PSE Amended MPO Rule and Revised Public Ownership Guidelines effective immediately (tiered IPO float 33/25/20/15%; REIT 33.33%; maintenance 20%/15%; lower float down to 12% possible above PHP200bn) | In force | [^pse-amended-mpo-rule-2026-08:1-4] | P |
| R7.15 | 2026-08-12 | Listing | Rule on listing preferred shares by IPO or direct listing: minimum offer PHP100M (was PHP1bn), 100 holders (was 1,000); direct-listed preferreds tradable immediately | In force | [^pse-cn-2026-0037-preferred-shares-rule-effectivity:1-2][^pse-analyst-briefing-1h-2026:16] | P |
| R7.16 | 2026-08-31 (after close) | Benchmarks | MSCI Philippines Index drops Ayala Land (reported reason: share-price decline and weaker H1 earnings): 9 constituents; ICTSI 44.73%, BDO 13.41%, BPI 8.38%, SM Prime 7.72% at 30 Sep 2026 | In force | [^newswav-2026-08-msci-ali][^msci-philippines-index-factsheet-2026-09:1-2] | S/P |
| R7.17 | 2026-08-31 | Universe | Robinsons Retail Holdings (RRHI) delisted voluntarily (approved 20 Aug 2026); PSE had already announced its removal from the Dividend Yield, MidCap and Services indices (CN-2026-0032, 14 Jul 2026, title only) | Historical | [^pse-cn-2026-0038-rrhi-voluntary-delisting:1][^pse-web-announcements-archive] | P |
| R7.18 | 2026-10-06 | Incident | PSE EDGE portal again unavailable (second time in 2026 after 19 Jan); PSE directs the public to its website and companies to submit emergency disclosures (CN-2026-0046; batches for Globe, Jollibee, Ayala Corp, PLDT, ACEN and others posted the same day). No trading halt notice seen | Historical (same-day; resolution not checked) | [^pse-cn-2026-0046-edge-outage-access-to-disclosures:1][^pse-web-announcements-archive] | P |

#### 1C. Supporting detail

**Session timetable history (all variants since 2013; times are 24-hour local)**

| Period | Pre-open | Pre-open no-cancel | Open | Recess / resume | Pre-close | Pre-close no-cancel | Run-off | Closing VWAP | Close | Sources |
|---|---|---|---|---|---|---|---|---|---|---|
| 2013-11-04 to 2020-03-13 | 09:00 | 09:15 (I: from PSE's retained older table) | 09:30 | 12:00 / 13:30 | 15:15 | 15:18 | 15:20 | none | 15:30 | [^pse-memo-pre-close-schedule-2013:1][^pse-web-investing-at-pse] |
| 2020-03-19 to 2021-12-03 | 09:00 | not listed | 09:30 | none (continuous to pre-close) | 12:45 | not listed | 12:50 | none | 13:00 | [^pse-cn-2020-0025-resumption-of-trading:1][^pse-cn-2020-0046:1][^pse-cn-2020-0051-gcq-floor-reopening:1] |
| 2021-12-06 to 2022-01-13 | 09:00 | not listed | 09:30 | 12:00 / 13:00 | 14:45 | not listed | 14:50 | none | 15:00 | [^pse-cn-2021-0059:1] |
| 2022-01-14 to 2022-02-28 | 09:00 | 09:15 | 09:30 | none | 12:45 | 12:48 | 12:50 | none | 13:00 | [^pse-cn-2022-0004:1] |
| 2022-03-01 to 2024-02-29 | 09:00 | 09:15 | 09:30 | 12:00 / 13:00 | 14:45 | 14:48 | 14:50 | none | 15:00 | [^pse-cn-2022-0009-trading-schedule-mar-2022:1] |
| 2024-03-01 to now | 09:00 | 09:15 | 09:30 | 12:00 / 13:00 | 14:45 | 14:48 | 14:50 | 15:00-15:15 | 15:15 | [^pse-approved-rules-vwap-trading-2024:3] |

**Fees and taxes on a PSE equity trade (6 Oct 2026)**

| Item | Rate | Change history found | Sources |
|---|---|---|---|
| Stock transaction tax (seller) | 0.1% of gross selling price | 0.5% to 31 Dec 2017; 0.6% 1 Jan 2018-30 Jun 2025; 0.1% from 1 Jul 2025 | [^pse-cn-2017-0082-stt-increase-advisory:1][^ra-12214-cmepa:16] |
| PSE transaction fee | 0.005% of value per side, plus 12% VAT (PSE's illustration charges PHP0.56 per PHP10,000, VAT included); block sales also 0.005% | Same rate in 2018 and 2019 annual-report revenue notes and on the 2026 PSE page | [^pse-annual-report-2018:88][^pse-annual-report-2019:48][^pse-web-investing-at-pse] |
| SEC "SRC fee" (SRC Sec. 35) | 0.005% of transaction value per side in PSE's cost illustration (PHP0.50 per PHP10,000); brokers' itemisation varies | No change history found | [^pse-web-investing-at-pse] |
| SCCP clearing and settlement fee | 0.01% of value per side, VAT-inclusive | 2018 rate not retrieved; no change announcement found | [^pse-web-investing-at-pse] |
| Broker commission | Maximum 1.5% plus VAT; no minimum since 18 Apr 2024 (previously 0.25% to 0.05% sliding minimum) | Minimum removed by SEC MC 7-2024 | [^pse-cn-2024-0029-min-commission-removal:1-3][^pse-pr-cmepa-day1-2025-07-01] |
| Dividend withholding | Resident individuals 10%; non-resident foreign corporations 25% (15% where the home country credits the tax) after CREATE | CREATE 2021 (PSE page still shows 30%, a stale value) | [^ra-11534-create:11][^pse-web-investing-at-pse] |

**Version-gating table for backtests and replay (regime by date; derived from the rows cited)**

| Parameter | Regime | From (trade date) | To (inclusive) | Row |
|---|---|---|---|---|
| Stock transaction tax | 0.5% | before 2018 | 2017-12-31 | B0.4 |
| | 0.6% | 2018-01-01 | 2025-06-30 | R1.1 |
| | 0.1% | 2025-07-01 | open | R6.7 |
| Settlement cycle | T+3 | before 2023 | 2023-08-23 | B0.3 |
| | T+2 | 2023-08-24 | open | R4.8 |
| Lower static threshold | -50% | before 2020 | 2020-03-23 | B0.5 |
| | -30% | 2020-03-24 | open | R2.5 |
| Index circuit breaker | single -10% = 15 min | before 2020 | 2020-05-03 | B0.5 |
| | three levels -10/-15/-20% | 2020-05-04 | open | R2.6 |
| Official close | 15:30 | 2013-11-04 | about 2020-03-13 (last full-day schedule; I) | B0.1 |
| | 13:00 (no trading 17-18 Mar 2020) | 2020-03-16 | 2021-12-03 | R2.4 |
| | 15:00 | 2021-12-06 | 2024-02-29 (13:00 from 2022-01-14 to 2022-02-28) | R3.4, R3.7, R3.8 |
| | 15:15 (Closing VWAP 15:00-15:15) | 2024-03-01 | open | R5.4 |
| Short selling | not operating | before 2023-11-06 | 2023-11-05 | R4.13 |
| | operating (eligible list) | 2023-11-06 | open | R4.13 |
| Broker minimum commission | sliding 0.25% to 0.05% | before 2024 | 2024-04-17 | R5.8 |
| | none (maximum 1.5% remains) | 2024-04-18 | open | R5.8 |
| Market-halt trigger | one-third of TPs unable to access | before 2025-08-20 | 2025-08-19 | R6.14 |
| | TPs above 50% of six-month ADTV | 2025-08-20 | open | R6.14 |
| Class A/B delivery on the regular board | either class | before 2025-08-11 | 2025-08-10 | R6.12 |
| | class purchased | 2025-08-11 | open (declassification by 9 Aug 2026) | R6.12 |
| PSEi / sector float floor | 12% | before 2018-02 | 2018-02-18 | B0.6 |
| | 15% | 2018-02-19 | Feb 2023 recomposition (I) | R1.2 |
| | 20% | Feb 2023 recomposition (I) | Feb 2027 rebalance | R3.3 |
| Board lot / tick table | single 15-band table | at least 2013 | open (NTE target 2026-11-23) | B0.7, P2 |
| EDGE same-day release cut-off | 3:30 pm | 2022-03-01 | 2026-05-22 | R3.9 |
| | 4:00 pm | 2026-05-25 | open | R7.10 |
| Annual listing maintenance fee cap (Main Board) | PHP2.0m | before 2025-01-02 | 2025-01-01 | R6.1 |
| | PHP3.5m | 2025-01-02 | open | R6.1 |
| IPO tax (NIRC Sec. 127(B)) | 4% / 2% / 1% of gross selling price | 1998-01-01 | on publication of RA 11494 (approved 2020-09-11; exact date not retrieved) | R2.13 |
| | repealed | Sep 2020 | open | R2.13 |
| Minimum public ownership at IPO | 10% (2012 rule) | 2012-01-01 | about Nov 2017 (I) | B0.12 |
| | 20%, with offer-size tiers 33/25/20% from 2020-08-03 | about Dec 2017 (I) | 2026-08-10 | B0.12, R2.10 |
| | tiered 33/25/20/15% (REIT 33.33%); maintenance 20% (15% above PHP50bn) | 2026-08-11 | open | R7.14 |

**Short selling and SBL: sequence.** Legal base 2006-2015 (B0.10), 30 Nov 2017 consultation (CN-2017-0068, title only), SEC approval 5 Jun 2018 (R1.7), amendment Jan 2019 (R1.11), CMIC guidelines effective 25 Feb 2020 (R2.3), offshore collateral 24 May 2023 (R4.6), BIR GMSLA acceptance 6 Sep 2023 and guideline effectivity 2 Oct 2023 (R4.11), SCCP client-share rule 23 Aug 2023 (R4.7), go-live 6 Nov 2023 (R4.13), BIR RR 10-2024 on 5 Jun 2024 (R5.9), PDTC lending pool Apr-May 2026 (R7.8), SEC-approved MSLA guidelines 15 May 2026 (R7.9); revised SBL rules filed with SEC 16 Apr 2026 (pending). MSCI's June 2026 accessibility review says the program "was implemented in November 2023. However, it is not yet an established market practice." [^msci-accessibility-review-2026:43]. Uptick rule text (SRC Rule 24.2-2.5): price above last sale, or equal to last sale only if that price exceeds the preceding different sale [^pse-web-sbl-short-selling].

**PSEi methodology: sequence.** Float floor 12% to 15% (Feb 2018, R1.2); to 20% (Aug 2021 memo, first applied Dec 2022 review, R3.3); MidCap and Dividend Yield indices (Mar 2022, R3.11); pension-fund float clarification (Jan 2024, R5.2). Approved but not yet effective: 21 Jul 2026 revised policy to apply at the February 2027 rebalance (98% cumulative market-cap screen; MTAR of at least 15% (10% for incumbents) plus MADV top-25% in 9 of 12 months replaces the single median-daily-value test; float floor 20% with a 15% exception for companies of PHP250bn market capitalisation or more) [^pse-cn-2026-0033b:1][^pse-cn-2026-0033b:7-8]. PSEi 2018 liquidity test for comparison: top 25% by median daily value in 9 of 12 months [^pse-index-policy-feb2018:6].

**Participant base.** Active trading participants: 132 when PSE moved to PSE Tower in Feb 2018 [^pse-pr-trading-floor-closed-2022-06-24]; 125 on 4 Jan 2022 [^pse-cn-2022-0001-delay-market-opening:1]; 123 in PSE's public directory of 20 Jul 2026 (my count of "Nominee" entries) [^pse-active-tp-summary-2026-07-20:1-6]. Of these, 40 run their own front-end order management systems (FEOMS) and so must certify against the new engine [^pse-nte-broker-forum-2026-07-09:5]. Investor accounts: 1.62 million (2021) to 3.64 million (2025), 88.6% online [^pse-analyst-briefing-1h-2026:8]. Listed companies: 280 at 14 Aug 2026 [^pse-analyst-briefing-1h-2026:3].

**Operational incidents that bear on engine-replacement risk** (all P): 4 Jan 2022 full-day cancellation (engine-to-front-end connection) [^pse-cn-2022-0002-cancellation-of-trading-2022-01-04:1]; 3 Jan 2024 halt 09:32-11:56 [^pse-cn-2024-0003-update-market-halt:1]; 9 Dec 2024 late open 09:55 [^pse-cn-2024-0061-adjusted-schedule-2024-12-09:1]; 24 Mar 2025 late open 11:10 [^pse-cn-2025-0015-adjusted-schedule-2025-03-24:1]; weather closures 26 Sep 2022 and 24 Jul 2024 [^pse-cn-2024-0038-trading-suspension-2024-07-24:1]. Three of four technical incidents involved the third-party front-end or connectivity layer rather than the matching engine (I).

### Inferences
- The 1 Jul 2025 STT cut is the single largest discontinuity in transaction cost in the window: sell-side tax fell from 60 bp to 10 bp, so any cost model or backtest spanning that date must switch rates by trade date, not by calendar year (I, from R6.7 and R1.1).
- "Close time" has three regimes: 15:30 (to 13 Mar 2020), 13:00 (Mar 2020 to Dec 2021), 15:00 (Dec 2021 to Feb 2024), 15:15 (from 1 Mar 2024); continuous trading ends at pre-close (15:15, then 12:45, then 14:45) so the last continuous print is not the official close (I, from the timetable table).
- Circuit-breaker cut-off clock times in CN-2020-0044 were written against a 15:15 pre-close; no republished clock times for the 14:45 pre-close were found, so either the cut-offs scale with pre-close (14:25 / 14:10 / 13:40 by subtraction) or they stayed absolute. Not resolvable from documents reviewed (I).
- PSE's web list of amendments to the Revised Trading Rules (not exhaustive: it omits the Aug 2025 halt amendments) shows no change to the lot/tick article after 2013, no circular in the 2017-2026 index announces one, and the Dec 2025 paper reproduces the same table as "existing"; so treating lot size and tick size as a pure function of price band for 2018 to Nov 2026 looks safe, but "unchanged since 2013" rests on absence of evidence (I) [^pse-web-reg-trading-participants][^pse-cn-2025-0046-board-lot-trading-at-last:4].
- PSE targets have repeatedly slipped (short selling: SEC-approved Jun 2018, live Nov 2023; GPDR: Q1 2025 target, still at SEC in Oct 2026; derivatives: Q1 2026 target, no date now), so the 23 Nov 2026 NTE date should be treated as a target with execution risk until PSE confirms the final rehearsals (I; see Section 2).
- Disclosure timing and the close have moved in opposite directions: the same-day EDGE release cut-off was 3:30 pm (1 Mar 2022 to 22 May 2026), only 15 minutes after the 15:15 close that applies since 1 Mar 2024, and is 4:00 pm since 25 May 2026, so company news can now be released 45 minutes after the close and still count as same-day; event strategies should treat 15:15-16:00 as an information window with no continuous market (I, from the cut-off, session and close rows).
- SCCP's post-trade rule changes (collateral list, client-asset rule, allocation algorithm, early delivery by SD-1, CTGF refund conditions) were all approved by the SEC and took effect by memo, not through PSE trading-rule amendments; the posted SCCP rulebook is still the 13 Mar 2018 text, so reading the rulebook alone gives stale T+3 wording and stale allocation, collateral and refund rules (I, from the SCCP rows and the 2018 edition).

### Gaps
- Exact publication dates (and therefore effective dates) for RA 11647, RA 11659, EO 175 and RA 11534 were not retrieved; EO 113's date is reported as 1 May (KPMG, from a 16 Apr publication) or 2 May 2026 (another report); CREATE's reported 11 Apr 2021 is secondary.
- Consolidated, current text of the PSE Revised Trading Rules and Implementing Guidelines was not found; the archived versions are 2010-2013 vintages, so the static/dynamic threshold wording after 2020 rests on circulars (CN-2020-0028, CN-2020-0044, CN-2021-0055) and the PSE web page.
- Outcome of the 2018 "trading without settlement" proposal, the 2022 disclosure-halt proposals (CN-2022-0045), the 2023 algorithmic-trading proposal and the 2024 black-out and error-account proposals (CN-2024-0048) not found (pipeline P21).
- Content of the CMIC SBL and short-selling guidelines beyond the cover memo, the text of BSP Circulars 1192 and 1212, and the 2022 and 2023 listing-rule memos known here only by their CLDR index titles (MEA-2022-0001 to -0003, CN-2024-0024) were not re-read.
- SEC MC 13-2017 (the earlier MPO rule: 20% at IPO, maintained at all times) was issued 1 Dec 2017 [^pse-sr6-2-mpo-initial-backdoor-2020:3]; its effectivity date is not stated there, and the SEC MC 11-2026 publication date was not retrieved.
- SCCP fee level for 2018 and any SCCP/PSE fee waivers or incentive schemes not verified.
- Whether the 2024-2025 PCC or other regulator approvals were needed for the PDS purchase was not found (SEC exemptive relief of Dec 2023 is reported by Philstar only).
- SEC (sec.gov.ph), BIR and Official Gazette pages could not be fetched (403/Cloudflare; Wayback had no capture), so SEC approvals or new circulars issued after the PSE's last relay (about 1 Oct 2026) would not appear here; SEC MC numbers are cited through PSE attachments only.

---

## 2. Reform pipeline as of 6 October 2026 (announced or proposed, not in force)

### Takeaway
The gating item is the Nasdaq Eqlipse "New Trading Engine" (NTE), scheduled for a "big bang" go-live on Monday 23 Nov 2026 after three Saturday rehearsals (31 Oct, 7 Nov, 14 Nov). Several rule changes that the NTE depends on (one-share lots, new tick table, odd-lot market removal, trading-at-last change, negotiated trades) still need or are awaiting SEC approval, and PSE's August 2026 deck labels One Share One Lot "For SEC Approval". Everything else (GPDR, market-making, ETF rules, structured warrants, SBL rule overhaul, SEC margin rules, broker capital increase) is Proposed. Derivatives have no date. No T+1 or extended-hours plan was found in any PSE or SEC document reviewed.

### Cited Findings

#### 2A. Pipeline table

| ID | Item | Before to after | Status on 6 Oct 2026 | Target / schedule | Sources | Ev |
|---|---|---|---|---|---|---|
| P1 | New Trading Engine (Nasdaq Eqlipse Trading) | PSEtrade XTS to Eqlipse; new FIX, ITCH and market-data (MDF) specs; no parallel run ("big bang"); only limit orders on Day 1; new leased lines (at least two: production and UAT/DR) | Approved, not yet effective (scheduled) | Go-live 23 Nov 2026; FEOMS certification 10-23 Sep; pre-production connectivity 29 Sep-9 Oct; pre-production testing 12-22 Oct; Saturday rehearsals 31 Oct, 7 Nov, 14 Nov. Earlier wording: "scheduled to be rolled out in 2026" (Dec 2025), "Q4 2026" (Jul-Aug 2026) | [^pse-nte-broker-forum-2026-07-09:4][^pse-nte-broker-forum-2026-07-09:9][^pse-nte-faq-2026-08:1][^pse-web-nte-page][^pse-cn-2025-0046-board-lot-trading-at-last:3][^pse-analyst-briefing-1h-2026:9] | P |
| P2 | One Lot One Share and new tick table | Lot size 1,000,000-5 shares by price band to 1 share everywhere (PHP and USD securities); tick table streamlined; odd-lot market removed; brokers may set a minimum order value (not exceeding the maximum commission rate) | Proposed (SEC approval pending; badge "For SEC Approval" on 17 Aug 2026; "awaiting SEC approval" on 4 Jul 2026) | Q4 2026 together with the NTE | [^pse-cn-2025-0046-board-lot-trading-at-last:3-5][^pse-nte-user-group-2026-01-15:9-10][^pse-analyst-briefing-1h-2026:9][^pse-asm-2026-president-report:22][^pse-nte-faq-2026-08:1] | P |
| P3 | Run-off / trading-at-last | Today an incoming order at the closing price is rejected if a passive order is better than the closing price; under Eqlipse it is accepted and matched with the passive order at the closing price; all run-off orders may be entered, modified and executed only at the closing price | Proposed with P2 (separate SEC status not stated; I) | With the NTE | [^pse-cn-2025-0046-board-lot-trading-at-last:5][^pse-nte-user-group-2026-01-15:11-15][^pse-nte-broker-forum-2026-07-09:7] | P |
| P4 | Negotiated Trades | New facility for pre-arranged trades between different clients of one firm: price within +/-5% of full-day VWAP (4 decimals), no volume or value limit, execution window 15 minutes after run-off, one-firm only, web-based like the VWAP facility, reported through the feed as news/announcement and included in value and CTF | Proposed (consultation 1-7 Jul 2026; "Revising per Public Comments" on 17 Aug 2026) | With the NTE (design shown to brokers 9 Jul 2026) | [^pse-cn-2026-0031-negotiated-trades:1][^pse-cn-2026-0031-negotiated-trades:3][^pse-nte-broker-forum-2026-07-09:8][^pse-nte-faq-2026-08:1-2][^pse-analyst-briefing-1h-2026:9] | P |
| P5 | PSETradeX changes (retail/TP platform) | GTC and next-day order validity removed; new "Good Till 3 Months" for the cloud version; 2FA replaces RSA token; 5,000 client accounts per broker; VIP accounts; cloud migration of TP version later deferred | Proposed/mixed (cloud migration deferred 9 Jul 2026; GTC removal timing not restated) | with the NTE (I) | [^pse-nte-user-group-2026-01-15:17][^pse-nte-broker-forum-2026-07-09:11] | P |
| P6 | Back-office files | Daily Transactions Report (DTR) retired; files via new PSE Portal; Weekly Tax Report data only from 3 Aug 2026 | Approved, not yet effective for DTR (portal live 3 Aug 2026) | with the NTE | [^pse-nte-user-group-2026-01-15:19][^pse-nte-faq-2026-08:2][^pse-nte-broker-forum-2026-07-09:13] | P |
| P7 | Revised PSE SBL rules (directed pooled lending; SEC-registered onshore lending agent for foreign lender/foreign borrower deals; SBL report rationalisation) | Foreign lenders/borrowers can use PDTC's facility with an onshore agent; collateral management carved out of the agent's role | Proposed (consulted 3-18 Feb 2026; filed with SEC 16 Apr 2026; "awaiting SEC approval" in Jul-Aug 2026) | none stated | [^pse-cn-2026-0009:1][^pse-pr-regulatory-reforms-2026-06-15][^pse-analyst-briefing-1h-2026:9] | P |
| P8 | GPDR (Global Philippine Depositary Receipts) | New peso-denominated depositary receipts on foreign-listed securities | Proposed (revised rules submitted to SEC 24 Jun 2026; PSE aimed for approval and publication "within the quarter", i.e. by 30 Sep 2026; no approval notice seen in PSE's index to 2 Oct 2026) | Slipped: "Target Launch: 2025" (Jul 2024 report); Q1 2025 (Oct 2024); rules filed with SEC Jan 2025, SEC comments received 26 May 2025, revised rules filed 24 Jun 2026; "ready issuer by 2H 2026" (2025 annual report) | [^pse-analyst-briefing-1h-2026:10][^pse-asm-2026-president-report:24][^pse-cn-2024-0047:1][^pse-annual-report-2025:38][^pse-asm-2024-presidents-report:25][^pse-asm-2025-presidents-report:30][^bworld-2024-10-23-gpdr-derivatives-targets] | P/S |
| P9 | Market-making rules | PSE general framework for all products with ETF and GPDR annexes (accreditation, maximum spreads, minimum quote sizes, presence, incentives incl. fee concessions); today PSE's rules cover ETFs only. SEC "Rules on Market Making" exposure draft approved by the SEC En Banc 13 Aug 2026 (comments to 28 Aug), effective 15 days after publication | Proposed (PSE: "Revising per Public Comments"; SEC: exposure draft) | none stated | [^pse-cn-2026-0026:1][^pse-cn-2026-0026:3][^pse-pr-market-making-2026-06-04][^pse-cn-2026-0039-sec-market-making-rfc:1-2][^pse-analyst-briefing-1h-2026:9] | P |
| P10 | ETF rule amendments | Trust-type and actively managed ETFs, multiple sub-funds, issuer capitalisation PHP250M to PHP50M (as low as PHP1M with a 5-year record), single authorised participant, market maker need not be an AP | Proposed (comments to 30 Jun 2026; "Revising per Public Comments") | none stated | [^pse-cn-2026-0029-etf-amend-consult:1][^pse-pr-regulatory-reforms-2026-06-15][^pse-analyst-briefing-1h-2026:16] | P |
| P11 | Structured warrants | SEC regulations for registration and trading of structured warrants; PSE aligning draft rules | Proposed (SEC draft out for comment to 13 May 2026) | none stated | [^pse-cn-2026-0018:1][^pse-analyst-briefing-1h-2026:10] | P |
| P12 | Derivatives (PSEi index futures first) | New market; exposure draft shared with selected institutions; RFI to technology vendors July 2026; talks with multilaterals for funding; derivatives rules "slated to be finalized" in 2H 2026. Groundwork: MOU with TWSE (27 Aug 2024; XBRL, SBL, derivatives via TAIFEX), MOU with Taipei Exchange (10 Jun 2025), learning sessions with TAIFEX/TPEx/TWSE (15-18 Dec 2025) | Proposed (no launch date) | Slipped: "Target Launch: 2026" (Jul 2024 report), "first derivatives in 2026" (Aug 2024), "Q1 2026" (Oct 2024), "set to launch index futures" (Jul 2025 report) | [^pse-analyst-briefing-1h-2026:10][^pse-asm-2026-president-report:24][^pse-annual-report-2025:38][^pse-asm-2024-presidents-report:25][^pse-asm-2025-presidents-report:30][^bworld-2024-10-23-gpdr-derivatives-targets][^fow-2024-08-29-derivatives-2026][^pse-analyst-briefing-3m-2026:15] | P/S |
| P13 | PSE index policy revision | 98% cumulative market-cap screen; MTAR and MADV liquidity tests; float floor 15% (instead of 20%) for market cap of at least PHP250bn | Approved, not yet effective | February 2027 rebalance | [^pse-cn-2026-0033b:1] | P |
| P14 | Broker capital | PSE proposal: unimpaired paid-up capital at least PHP50M by 31 Dec 2027, surety bond PHP12M to PHP20M by 31 Dec 2028 for sub-PHP100M TPs, PHP100M by 31 Dec 2029; SEC exposure draft of amended SRC Rules 28.1/33.1 (En Banc 24 Sep 2026, comments to 14 Oct 2026) | Proposed | 2027-2029 | [^pse-memo-tp-paid-up-capital-increase-2026-07:3][^pse-memo-2026-10-01-sec-rfc-src-28-1-33-1-capital:1-2] | P |
| P15 | SEC margin rule 48.1 overhaul | New principles-based margin-financing framework with Exchange Margin Trading Rules | Proposed (SEC En Banc 25 Aug 2026; comments to 15 Sep 2026) | none stated | [^sec-rfq-2026-src-rule-48-1-margin:1] | P |
| P16 | SEC Capital Market Master Plan (with ADB) and derivatives roadmap | Plan to position the Philippines among Southeast Asia's leading capital markets by 2030; roadmap covers options, futures, ETFs, GPDRs and possibly commodity futures; SEC strategic sandbox has approved 24 applications (foreign equities, tokenized real-world assets, crypto derivatives, margin trading) | In preparation (no document retrieved) | 2030 horizon | [^philstar-2026-07-17-sec-accomplishments] | S |
| P17 | SME Board and other listing rules | SME Board sponsor-model amendments (CN-2026-0041, 28 Aug 2026); sponsor model "Ongoing Review"; Green Equity Label rules consultation (CN-2026-0042) | Proposed | none stated | [^pse-analyst-briefing-1h-2026:16][^pse-web-announcements-archive] | P |
| P18 | PDS integration and other infrastructure | Phase 1 consolidation of 13 systems; Phase 2 single post-trade system (clearing, settlement and depository), fixed-income assets as clearing collateral, wider Name-on-Central-Depository coverage; also listed as technology upgrades: new central depository system for PDTC, new surveillance system for CMIC, XBRL-based disclosure platform | In progress | Phase 2 target 2027 | [^pse-analyst-briefing-1h-2026:31][^pse-analyst-briefing-3m-2026:24] | P |
| P19 | T+1 settlement; extended trading hours; fractional (sub-one-share) trading | none | No proposal found in the PSE decks (Mar, Jul, Aug 2026), the 2024-2026 president's reports, the 2025 annual report, or the PSE circular index to 6 Oct 2026; one-share lots (P2) are the lowest lot proposed | none | [^pse-analyst-briefing-3m-2026:14][^pse-analyst-briefing-1h-2026:9][^pse-annual-report-2025:38][^pse-asm-2024-presidents-report:25][^pse-asm-2025-presidents-report:30] | I (absence) |
| P20 | MSCI / FTSE classification | Philippines stays Emerging (MSCI) and Secondary emerging (FTSE); MSCI 2026 market classification announcement named other markets but not the Philippines; MSCI's June 2026 accessibility review still lists foreign-ownership, FX and short-selling frictions | No change known; FTSE outcome pending | FTSE annual announcement scheduled Tue 6 Oct 2026 (placeholder only when checked); next MSCI review date not retrieved | [^ftse-geis-ground-rules-2026-09:45][^ftse-country-classification-interim-2026-03:5][^ftse-equity-country-classification-page][^ladige-2026-06-msci-mcr][^msci-accessibility-review-2026:43] | P/S |
| P21 | Rule consultations with no recorded outcome | PSE consultations whose adoption was not found: CN-2018-0023 trading without settlement (Apr 2018), CN-2022-0045 disclosure-halt changes (Nov 2022), CN-2023-0043 algorithmic trading (Sep 2023; the VWAP part was adopted), CN-2023-0041 MPO and voluntary-delisting amendments (Aug 2023; MPO levels restated in the Aug 2026 rule), CN-2024-0048 black-out and error-account changes (Sep 2024) | Proposed (outcome unknown) | none | [^pse-cn-2018-0023-trading-without-settlement-proposal:1][^pse-cn-2022-0045-consultation-2022-part-ii:1][^pse-cn-2023-0043:2][^pse-cn-2023-0041-mpo-delisting-consult:1-3][^pse-cn-2024-0048-consultation-blackout-rule:1] | P (proposals); outcomes unknown |

#### 2B. NTE detail that execution code will need

- **Schedule and readiness (PSE, 9 Jul 2026).** Of 40 TPs with their own front-end order management system (FEOMS): 18 analysing FIX specs and developing, 9 analysing but not started, 2 neither, 11 not responding; for UAT connectivity 11 not responding, 17 talking to telcos, 3 in installation, 3 testing, 1 completed, 5 not started. Market data: 7 vendors and 21 TPs; ITCH/MDF development 10 ongoing, 12 not started, 6 not responding [^pse-nte-broker-forum-2026-07-09:5-6]. August FAQ: certification beyond 23 Sep still possible; new server IPs not yet available; no parallel run [^pse-nte-faq-2026-08:1-3].
- **Specs.** PSE's NTE page lists FIX Order Entry / Session Gateway / Drop Copy v0.1 (30 Jan 2026) and v1.1 (8 Jun 2026); ITCH and MDF v1.0 (29 Jan), v1.1 (8 Jun), v1.2 (17 Jul 2026); static-data files (securities, index members, DDS exchange rate) v1.0 dated 22 Jun 2026 [^pse-web-nte-page]. ITCH and MDF run on separate SoupBinTCP sessions; cross trades carry a Cross Indicator in messages C and P [^pse-nte-faq-2026-08:3].
- **Tick and lot comparison (PHP securities).**

| Price band (PHP) | Current tick | Current lot | NTE tick | NTE lot | Tick change (my comparison) |
|---|---|---|---|---|---|
| 0.0001-0.0099 | 0.0001 | 1,000,000 | 0.001 (band "up to 0.099") | 1 | coarser |
| 0.0100-0.0490 | 0.001 | 100,000 | 0.001 | 1 | same |
| 0.0500-0.0990 | 0.001 | 10,000 | 0.001 | 1 | same |
| 0.1000-0.2490 | 0.001 | 10,000 | 0.005 (band 0.10-0.995) | 1 | coarser |
| 0.2500-0.4950 | 0.005 | 10,000 | 0.005 | 1 | same |
| 0.5000-0.9950 | 0.01 | 1,000 | 0.005 | 1 | finer |
| 1.0000-4.9900 | 0.01 | 1,000 | 0.01 (band 1-9.99) | 1 | same |
| 5.0000-9.9900 | 0.01 | 100 | 0.01 | 1 | same |
| 10.0000-19.9800 | 0.02 | 100 | 0.05 (band 10-99.95) | 1 | coarser |
| 20.0000-49.9500 | 0.05 | 100 | 0.05 | 1 | same |
| 50.0000-99.9500 | 0.05 | 10 | 0.05 | 1 | same |
| 100.00-199.90 | 0.10 | 10 | 0.10 | 1 | same |
| 200.00-499.80 | 0.20 | 10 | 0.20 | 1 | same |
| 500.00-999.50 | 0.50 | 10 | 0.50 | 1 | same |
| 1,000-1,999 | 1 | 5 | 1 | 1 | same |
| 2,000-4,998 | 2 | 5 | 2 | 1 | same |
| 5,000 and up | 5 | 5 | 5 | 1 | same |

  Sources: current table [^pse-cn-2025-0046-board-lot-trading-at-last:4]; NTE table [^pse-nte-user-group-2026-01-15:9]. The "tick change" column is my comparison, not a PSE statement (I). For dollar-denominated securities the proposal merges bands to: up to 9.99 tick 0.01; 10-19.98 tick 0.02; 20-99.95 tick 0.05; then 0.10 / 0.20 / 0.50 / 1.00, lot 1 [^pse-nte-user-group-2026-01-15:10].

#### 2C. Slippage record (useful as a prior for the NTE date)
- Short selling: SEC-approved guidelines 5 Jun 2018 -> effective 2 Oct 2023 -> go-live 6 Nov 2023, itself pushed from 23 Oct 2023 [^pse-cn-2018-0035-short-selling-guidelines-sec-approved:1][^pse-cn-2023-0048:1][^pse-cn-2023-0056:1].
- GPDR/DRs: "Target Launch: 2025" (Jul 2024) -> Q1 2025 (Oct 2024) -> rules filed with SEC Jan 2025 -> SEC comments 26 May 2025 -> revised rules filed 24 Jun 2026 -> still pending [^pse-asm-2024-presidents-report:25][^bworld-2024-10-23-gpdr-derivatives-targets][^pse-asm-2025-presidents-report:30][^pse-annual-report-2025:38][^pse-analyst-briefing-1h-2026:10].
- Derivatives: "Target Launch: 2026" (Jul 2024) -> "Q1 2026" (Oct 2024) -> "set to launch index futures" (Jul 2025) -> RFI July 2026, funding talks, no launch date (Aug 2026) [^pse-asm-2024-presidents-report:25][^fow-2024-08-29-derivatives-2026][^pse-asm-2025-presidents-report:30][^pse-analyst-briefing-1h-2026:10].
- Board lot: 2023 proposal filed with SEC and "awaiting approval" in Jul 2024, never approved; 2025 proposal tied to the NTE and awaiting SEC approval [^pse-cn-2023-0051:1][^pse-asm-2024-presidents-report:18][^pse-asm-2026-president-report:22].
- Market-halt rule: consulted May 2022, effective Aug 2025 [^pse-cn-2022-0020-market-halt-consultation:3][^pse-cn-2025-0037:1].
- Counter-evidence: T+2 held its announced date (24 Aug 2023) once SEC approved on 10 Aug, and VWAP launched on the date announced (1 Mar 2024) [^pse-cn-2023-0040-t2-go-live:1][^pse-cn-2024-0012-vwap-go-live:1].

#### 2D. Look-ahead calendar to February 2027 (dated items only; none of these changes a rule except where stated)

| Date | Event | Why it matters to execution | Sources | Ev |
|---|---|---|---|---|
| Tue 2026-10-06 | FTSE Russell's 2026 annual country-classification announcement is scheduled; the Philippines is Secondary Emerging and the March 2026 watch list named only Egypt. FTSE's page still linked a two-page "Document to follow" placeholder when checked | Classification change risk (none signalled); FTSE normally gives at least six months' notice before changing a country's classification | [^ftse-country-classification-interim-2026-03:2][^ftse-country-classification-interim-2026-03:5][^ftse-geis-ground-rules-2026-09:9][^ftse-equity-country-classification-page] | P |
| 2026-10-06 to 2026-10-12 | Mynt (GCASH) IPO offer period (price fixed 1 Oct; up to 8.03bn shares at up to PHP10.00; PSE gives tentative listing as 20 Oct, the 4 Jul ASM deck says 19 Oct; conflict C17) | Very large IPO (PHP92.31bn sized in the 4 Jul deck); retail subscriptions also through GStocks; supply and index-inclusion events follow | [^pse-press-mynt-ipo-approval][^pse-asm-2026-president-report:8] | P |
| 2026-10-12 | Vitro REIT IPO (about PHP24.19bn) scheduled to list | First large REIT under the Jan 2026 SEC framework; REIT MPO 33.33% (R7.14) | [^pse-asm-2026-president-report:8] | P |
| 2026-10-12 to 2026-10-22 | NTE pre-production testing; Saturday rehearsals 31 Oct, 7 Nov and 14 Nov | Last windows to certify FEOMS, FIX and ITCH changes | [^pse-nte-broker-forum-2026-07-09:9] | P |
| 2026-10-14 | Comment deadline on the SEC's draft higher capital rules for broker-dealers (SRC Rules 28.1 and 33.1) | Counterparty-capital proposal (P14) | [^pse-memo-2026-10-01-sec-rfc-src-28-1-33-1-capital:1-2] | P |
| 2026-11-16 to 2026-11-18 | Whether PSE trades during the ASEAN Summit days is unresolved: a circular saying "regular trading days" was followed the same day by one promising a final advisory | Calendar service must allow either outcome; clearing follows BSP business days | [^pse-trading-day-advisory-2026-11-16-18:1] | P |
| Mon 2026-11-23 | NTE go-live (no parallel run; limit orders only on day 1; one-share lots and new tick table only if SEC approval has arrived) | Hard cutover; see Execution implications 1-3 | [^pse-nte-broker-forum-2026-07-09:9][^pse-nte-faq-2026-08:1] | P |
| Nov 2026 | MSCI November index review (date not retrieved); FTSE December quarterly review follows | Index-implementation days are high-volume days (see the market-data and indices chapter) | [^msci-philippines-index-factsheet-2026-09:1] | I (dates unknown) |
| about 2027-02-01 | First application of PSE's revised index policy (98% cumulative market-cap screen, MTAR and MADV tests, 15% float exception from PHP250bn) at the February rebalance; recent February effective dates were the first Monday of the month | Index-flow positioning; the announcement is usually 3 to 5 trading days earlier | [^pse-cn-2026-0033b:1][^pse-cn-2026-0033b:7-8] | P (policy); date I |

Non-trading days for the rest of 2026 are covered in the calendar chapter.

### Inferences
- The NTE go-live depends on three things PSE does not control: SEC approval of the lot/tick, trading-at-last and negotiated-trade rule changes; broker FEOMS readiness (many TPs had not started on 9 Jul); and vendor-layer connectivity. No deferral has been announced as of 6 Oct 2026, but given the readiness figures and the SEC dependencies the schedule risk is non-trivial (I).
- If SEC does not approve One Lot One Share before 23 Nov, PSE would either keep the existing lot table on the new engine or delay the engine; PSE materials do not say which (I). Code should read lot size and tick size from the security master (PSE static-data files) rather than hard-coding either regime.
- Two large listings are scheduled in October 2026 (Vitro REIT on 12 Oct and Globe Fintech/Mynt on 19 Oct; PNB Holdings by introduction on 25 Sep) and will be among the first under the new tiered MPO rule (REIT 33.33%; issuers above PHP50bn 15% with an offer of at least PHP10bn). PSE's deck gives amounts (PHP24.19bn and PHP92.31bn) without saying whether they are offer size or valuation, so any MPO or index-inclusion conclusion needs the prospectuses (I) [^pse-analyst-briefing-1h-2026:13][^philstar-2026-07-17-sec-accomplishments][^pse-amended-mpo-rule-2026-08:2].

### Gaps
- No PSE notice after 25 Sep 2026 on the NTE; the 25 Sep "trading day advisory" for 16-18 Nov 2026 is a placeholder promising a final advisory [^pse-trading-day-advisory-2026-11-16-18:1]. Whether the 16-18 Nov operations interact with the 23 Nov cutover is unknown.
- SEC approval status of the board-lot, trading-at-last and negotiated-trade rules after 17 Aug 2026 is unknown; PSE's circular index to 2 Oct shows no approval memo.
- No statement on whether static/dynamic thresholds, circuit breakers, order types beyond limit, or session times change with the NTE.
- FTSE's 2026 annual classification announcement was due on 6 Oct 2026 and had not been posted when checked (the March 2026 interim watch list named only Egypt); MSCI's November 2026 review date and any MSCI watch-list for the Philippines were not retrieved (only classification tables, the June 2026 accessibility review and the index factsheet).
- The SEC Capital Market Master Plan document itself and any SEC statement on T+1, trading hours or short-selling reform were not found.

---

## 3. Source conflicts and stale-fact flags

### Takeaway
PSE's own public website contradicts itself on trading hours, price bands, dividend tax and short-selling eligibility, and one transcription of RA 12214 on lawphil gives a different effectivity clause from the official copy. Use circulars and the official statute PDFs, not the website FAQ, and ignore the "date" column on PSE's announcement index (it contains typos such as 2036 and 2045).

### Cited Findings
- **C1. "Pre-pandemic" schedule label.** CN-2021-0059 (22 Nov 2021) says PSE "will go back to its pre-pandemic full day-5-hour trading schedule" with 13:00 resume, 14:45 pre-close and 15:00 close [^pse-cn-2021-0059:1]. The pre-March-2020 schedule resumed at 13:30, had pre-close 15:15 and closed at 15:30 [^pse-memo-pre-close-schedule-2013:1][^pse-cn-2020-0044:2]. So 6 Dec 2021 was a new, shorter day, not a restoration. Press coverage repeated the "pre-pandemic" wording (not independently archived).
- **C2. PSE "Investing at PSE" page contradicts itself.** The same page shows (a) a current table ending with "Closing VWAP Session 3:00 pm, Market Close 3:15 pm" and "Trading days are Monday to Friday, 9:00 a.m. to 3:15 p.m."; (b) an older table (08:45 anthem, 09:00 pre-open auction, 13:30 continuous, 15:15 pre-close auction, 15:20 run-off, 15:30 close); (c) an FAQ saying trading runs "9:30 AM to 12:00 NN and 1:30 PM to 3:30 PM"; (d) a static-threshold FAQ saying prices are frozen at +/-50% (the floor has been -30% since 24 Mar 2020); (e) a dividend-tax table with 30% for non-resident foreign corporations (CREATE: 25%, or 15% with tax-credit reciprocity) [^pse-web-investing-at-pse][^pse-cn-2020-0028:1][^ra-11534-create:11]. The STT line on the same page (0.1%) is current.
- **C3. PSE SBL page.** One FAQ says only PSEi constituents and ETFs are eligible for short-sale SBL; another (and CN-2023-0048) says PSEi, MidCap, Dividend Yield and ETFs [^pse-web-sbl-short-selling][^pse-cn-2023-0048:2].
- **C4. RA 12214 effectivity text.** Lawphil's transcription of Sec. 29 reads "shall take effect after fifteen (15) days following the completion of its publication", whereas the archived official copy reads "shall take effect on July 1, 2025, following its complete publication" and Sec. 28 refers to instruments issued "prior to July 1, 2025" [^lawphil-ra-12214-2025][^ra-12214-cmepa:25]. PSE (CN-2025-0026) and BIR (RR 20-2025, Sec. 10) both use 1 July 2025 [^pse-cn-2025-0026-stt-decrease-advisory:1][^bir-rr-20-2025-stt:4]. Treat 1 Jul 2025 as correct; the lawphil text is a transcription discrepancy (I).
- **C5. PSE announcement-index dates are unreliable.** Examples: "Revised Policy on Index Management" (CN-2026-0033B) shows "June 30, 2027" though the memo is dated 21 Jul 2026; "Request for Comments on SEC's Proposed Rules on Market Making" shows "August 13, 2036" though dated 20 Aug 2026; "Short Selling Program Go Live" shows 6 Nov 2024 though the program went live 6 Nov 2023 [^pse-web-announcements-archive][^pse-cn-2026-0033b:1][^pse-cn-2026-0039-sec-market-making-rfc:1][^pse-cn-2023-0056:1]. The second line of each index entry (posting date) is usually right; the circular's own date is authoritative.
- **C6. Lower static threshold dates.** PSE's press-release page is dated 16 Apr 2020; the circular is dated 21 Mar 2020 (SEC approval 20 Mar) and the change took effect 24 Mar 2020 [^pse-pr-lower-static-threshold-2020][^pse-cn-2020-0028:1-2][^pse-cn-2020-0044:1].
- **C7. Short-selling guideline dates.** PSE index lists CN-2018-0035 as 22 Jul 2018; the memo is dated 22 Jun 2018 and records SEC approval on 5 Jun 2018 [^pse-cn-2018-0035-short-selling-guidelines-sec-approved:1]. "Effective" (2 Oct 2023) and "go-live" (6 Nov 2023; first announced 23 Oct 2023) are different dates [^pse-cn-2023-0048:2][^pse-cn-2023-0056:1].
- **C8. 13th negative list effectivity.** EO 113 takes effect 15 days after publication; KPMG says 1 May 2026 (publication 16 Apr), another report says 2 May 2026 [^eo-113-2026-13th-finl:2][^kpmg-2026-04-13th-finl].
- **C9. Foreign-ownership framing.** MSCI's June 2026 accessibility review says all industries are "in general subject to a 40 percent foreign ownership limit", affecting over 10% of the market [^msci-accessibility-review-2026:43]; the 2022 statutes and negative lists open several sectors (RA 11659 confines 60/40 to six public-utility categories), and SEC MC 10-2025 notes PSE "strictly monitors and enforces foreign ownership limits" in its trading system [^ra-11659-public-service-act-amendments:4][^pse-cn-2025-0035-sec-declassification-mandate:2]. Per-issuer limits remain binding.
- **C10. NTE timing language.** "Scheduled to be rolled out in 2026" (CN-2025-0046, Dec 2025) [^pse-cn-2025-0046-board-lot-trading-at-last:3]; "Q4 2026" (decks) [^pse-analyst-briefing-1h-2026:9]; "Go-Live Nov 23, 2026" (Broker Forum 9 Jul 2026) [^pse-nte-broker-forum-2026-07-09:9]. Not a contradiction, but only the last gives a date.
- **C11. NTE final-spec date.** PSE's NTE page shows ITCH and MDF v1.2 dated 17 Jul 2026, while the August FAQ says final specs "has been released last July 23, 2026" [^pse-web-nte-page][^pse-nte-faq-2026-08:2].
- **C12. Status badges in the Aug 2026 deck.** Text extraction attaches "For SEC Approval" to the SBL item; the slide shows that badge on "One Share, One Lot" (SBL carries no badge, though its text says PSE is awaiting SEC approval of the revised SBL rules) [^pse-analyst-briefing-1h-2026:9]. The 4 Jul 2026 report confirms the board-lot approval is pending [^pse-asm-2026-president-report:22].
- **C13. Circular numbering.** The 10 Sep 2026 declassification-mechanics memo is filed as "2026-0041" while CN-2026-0041 is also the SME Board sponsor-model consultation of 28 Aug 2026 [^pse-cn-2026-0041-declassification-price-suspension:1][^pse-web-announcements-archive].
- **C14. Notice dates for the March 2025 delay.** CN-2025-0011/0014/0015 carry the date 24 Mar 2025 inside the notice, while PSE's index lists them under 31 Mar 2025 [^pse-cn-2025-0015-adjusted-schedule-2025-03-24:1][^pse-web-announcements-archive].
- **C15. Derivatives and GPDR targets.** Press quotes from Oct 2024 (GPDR Q1 2025; derivatives Q1 2026) conflict with the Aug 2026 position (GPDR pending SEC; derivatives undated) [^bworld-2024-10-23-gpdr-derivatives-targets][^pse-analyst-briefing-1h-2026:10].
- **C16. MSLA guideline approval date.** PSE's memo of 22 May 2026 says the SEC approved the 2026 Revised MSLA Guidelines on 15 May 2026, effective immediately [^pse-cn-2026-0025:1]; the press report is dated 10 Jun 2026 [^philstar-2026-06-10-sec-msla]. Use 15 May 2026 (the PSE index lists the memo under 25 May).

- **C17. Mynt (GCASH) listing date.** PSE's 18 Sep 2026 release gives a tentative listing date of 20 Oct 2026; the 4 Jul 2026 annual-meeting deck lists the IPO on 19 Oct 2026 [^pse-press-mynt-ipo-approval][^pse-asm-2026-president-report:8]. Use the later PSE release and re-check against the final prospectus calendar.
- **C18. BIR acceptance of the GMSLA.** CN-2023-0048 and PSE's 2025 deck give 6 Sep 2023 (BIR letter); PSE's Oct 2023 retail webinar deck dates PSE's receipt of the confirmation to 25 Sep 2023 on one slide and repeats "6 September 2023" on another [^pse-cn-2023-0048:2][^pse-asm-2024-presidents-report:24][^pse-sbl-short-selling-webinar-2023:3]. Treat 6 Sep as the letter date and 25 Sep as when PSE says it received it.
- **C19. PDTC as lending agent.** PSE's July 2024 report says "Approval of PDTC as a Lending Agent (SEC)" on 21 Jul 2023; the Oct 2023 webinar deck says "conditional approval" [^pse-asm-2024-presidents-report:24][^pse-sbl-short-selling-webinar-2023:3]. The conditions were not found.
- **C20. Redlined SCCP memos lose their strikethrough in text extraction.** SCCP memo 02-0125 shows the old Rule 3.4 wording ("largest outstanding netted amounts first") and the new Annex 11 algorithm side by side; only the rendered page shows which is struck through. The new rule is price first, then lowest quantity, then pseudo-random [^sccp-memo-02-0125-sec-approval-rules-3-4-5-1-4-6-2-8-7-6:1]. Read amendment memos from the page image, not the text layer.

### Inferences
- The knowledge base should cite PSE circulars by number and date, treat the PSE website FAQ as stale unless a circular confirms it, and tag every parameter with an "in force since" date (I).
- The PSE site's retained old trading-hours table is the most likely source of wrong "15:30 close" assumptions in post-2021 data processing (I).

### Gaps
- Whether PSE has corrected the stale FAQ items is unknown after 6 Oct 2026.
- The lawphil/official-gazette discrepancy for RA 12214 Sec. 29 was resolved only by the archived official PDF; the Official Gazette page itself was blocked (403).

---

## Execution implications

1. **Plan for a hard cutover on 23 Nov 2026.** No parallel run, Day-1 limit orders only, new FIX/ITCH/MDF specs (FIX v1.1; ITCH/MDF v1.2), new leased lines, certification windows 10-23 Sep and Saturday rehearsals 31 Oct, 7 Nov, 14 Nov. Version-gate every PSE-specific rule by date; keep a manual/kill-switch fallback; assume elevated incident risk in the first weeks (four technical incidents in 2022-2025). [^pse-nte-broker-forum-2026-07-09:9][^pse-nte-faq-2026-08:1]
2. **Lot and tick logic must be data-driven.** Today's table runs 1,000,000 down to 5 shares by price band; the NTE proposal sets lot 1 and changes ticks in four bands (coarser below 0.01, 0.10-0.249 and 10-19.98; finer at 0.50-0.995). Odd-lot market disappears. Do not hard-code either regime; read static data. [^pse-cn-2025-0046-board-lot-trading-at-last:4][^pse-nte-user-group-2026-01-15:9]
3. **Closing-auction strategies change.** Present: pre-close 14:45 (cancellations allowed), no-cancel 14:48, run-off 14:50 at the closing price only, orders better than the close are rejected; Closing VWAP 15:00-15:15 (at least PHP500,000, single TP); official close 15:15. Under Eqlipse: run-off orders at the close are accepted and match resting better-priced orders at the closing price; negotiated trades (+/-5% of VWAP) share the 15-minute post-run-off window. [^pse-approved-rules-vwap-trading-2024:6-7][^pse-cn-2025-0046-board-lot-trading-at-last:5][^pse-nte-broker-forum-2026-07-09:8]
4. **Price-limit and halt model.** Static +50%/-30% from the reference price; dynamic 10/15/20% by trade-count cluster (reset Feb/Aug; next about Feb 2027); index breakers 10/15/20% for 15/30/60 minutes; broker-outage halts now need TPs with more than 50% of ADTV affected; no trading when PAGASA signal 3+ in NCR (the Sep 2022 closure also suspended clearing and settlement). Clock cut-offs for the breakers are ambiguous after the 14:45 pre-close. [^pse-cn-2020-0028:1][^pse-tpa-2026-0036-dynamic-threshold-review:1][^pse-cn-2020-0044:1-4][^pse-cn-2025-0037:1-4]
5. **Cost model by trade date.** STT 60 bp from 1 Jan 2018 to 30 Jun 2025, 10 bp from 1 Jul 2025 (seller); PSE fee 0.5 bp (plus VAT), SEC "SRC fee" 0.5 bp and SCCP 1 bp per side; broker commission up to 1.5% with no minimum since 18 Apr 2024; STT now also covers domestic shares listed abroad. [^ra-10963-train:24][^ra-12214-cmepa:16][^pse-web-investing-at-pse][^pse-cn-2024-0029-min-commission-removal:1]
6. **Settlement and corporate-action calendar.** T+2 with noon deadlines; ex-date one trading day before record date since 24 Aug 2023; declassification events add a two-day suspension and a price adjustment (higher of the A/B closes). No T+1 plan found. [^pse-cn-2023-0031-t2-settlement:1][^pse-cn-2026-0041-declassification-price-suspension:1-2]
7. **Short selling is available but unused so far.** PSE's Daily Short Selling Reports for 6 Nov 2023 and 5 Oct 2026 both show zero short-sale volume in every eligible security (two reports checked; a sibling note reports zero on every report). Eligible: PSEi, MidCap and Dividend Yield members plus ETFs (list moves with the Feb/Aug reviews); short-interest ratio cap 10%; uptick rule; no short orders in pre-open/pre-close; day orders only; borrow needs MSLA registered with BIR (PDTC pool cash-collateral only so far); MSCI calls it not yet established practice. Revised SBL rules for foreign participants are pending at the SEC. [^pse-cn-2023-0048:8-10][^pse-cn-2026-0022:1-2][^msci-accessibility-review-2026:43]
8. **Index-event calendar.** Reviews take effect in early Feb and early Aug (3 Aug 2026 last); methodology change (98% cap screen, MTAR/MADV, 15% float exception) applies at the Feb 2027 rebalance; MSCI Philippines now has only nine names, with ICTSI near 45%. Expect index-driven flows to concentrate. [^pse-cn-2026-0035:1][^pse-cn-2026-0033b:1][^msci-philippines-index-factsheet-2026-09:1]
9. **Foreign-ownership and share-class rules.** Foreign-room checks stay issuer-specific; Class A/B shares are being merged (articles to be amended by 9 Aug 2026); the 13th negative list took effect about 1-2 May 2026. [^pse-cn-2025-0036-declassification-effectivity:1][^eo-113-2026-13th-finl:1-2]
10. **Back-office feeds.** DTR file retired with the NTE; EOD files (ABC, CTF, Quote, Price.lis) via the new PSE Portal; Weekly Tax Report only from 3 Aug 2026. [^pse-nte-user-group-2026-01-15:19][^pse-nte-faq-2026-08:2]
11. **Instruments that do not yet exist.** GPDRs, structured warrants, index futures, market-maker incentives and broader ETFs are not tradable; do not model them before PSE circulars and SEC approvals appear. [^pse-analyst-briefing-1h-2026:9-10]
12. **News timing.** Issuers must disclose material information to PSE within 10 minutes and before the media, and may halt their own stock; EDGE releases same-day only if received by the cut-off, which has been 4:00 pm since 25 May 2026 (3:30 pm from 1 Mar 2022 to 22 May 2026), so filings between 15:15 and the cut-off can move prices after the close. PSE can also impose a short news halt itself (MRC, 19 Jan 2026). [^pse-listing-disclosure-rules:139][^pse-cn-2026-0024-edge-cutoff-4pm:1][^pse-cn-2022-0010-edge-cutoff-330pm:1][^pse-cn-2026-0004-2-emergency-disclosures-trading-halt:1-2]
13. **Clearing rules that touch strategies.** SCCP collateral eligibility (PSEi, MidCap and Dividend Yield constituents at a 25% haircut, PSE shares 35%) is re-set after each index review (20 Feb 2023, 2 Feb 2026), which changes brokers' financing capacity for specific names; Rule 2.3.5 (23 Aug 2023) stops a clearing member using one client's shares to settle another's trade except under an SBL arrangement, so omnibus or prime-broker set-ups should be checked for it; the settlement batch may start before 12:00 once all obligations are in (5 Mar 2024). [^sccp-memo-02-0223-collateral-haircut-rates:1-2][^sccp-memo-01-0126-eligible-collateral-list:1][^sccp-memo-07-0823-sec-approved-amendments:2][^sccp-memo-01-0324-early-batch-run-effectivity:1]

---

## Source catalog

```yaml
- slug: bir-rr-19-2025-dst
  title: "BIR Revenue Regulations No. 19-2025: DST rate adjustments under RA 12214"
  publisher: "Bureau of Internal Revenue"
  type: pdf
  canonical_url: "https://www.bir.gov.ph/"
  local_path: pdfs/bir-rr-19-2025-dst.pdf
  edition: in-force
  amended_through: "2025-08-05"
  note: "Scanned; covers transactions from 1 Jul 2025. Archived by another researcher; original URL not recorded."
- slug: bir-rr-20-2025-stt
  title: "BIR Revenue Regulations No. 20-2025: Stock Transaction Tax rate adjustment under RA 12214"
  publisher: "Bureau of Internal Revenue"
  type: pdf
  canonical_url: "https://www.bir.gov.ph/"
  local_path: pdfs/bir-rr-20-2025-stt.pdf
  edition: in-force
  amended_through: "2025-08-05"
  note: "Signed by the Finance Secretary 29 Jul 2025; Sec. 10 effective 1 Jul 2025 (PDF p4). Archived by another researcher; original URL not recorded."
- slug: bir-rr-21-2025-cmepa-income
  title: "BIR Revenue Regulations No. 21-2025: income-tax amendments under RA 12214"
  publisher: "Bureau of Internal Revenue"
  type: pdf
  canonical_url: "https://www.bir.gov.ph/"
  local_path: pdfs/bir-rr-21-2025-cmepa-income.pdf
  edition: in-force
  amended_through: "2025-08-05"
  note: "Scanned. Archived by another researcher; original URL not recorded."
- slug: bsp-fx-manual-morfxt-2025-05
  title: "BSP Manual of Regulations on Foreign Exchange Transactions (MORFXT), updated May 2025 (amended through Circular 1212 of 11 Apr 2025)"
  publisher: "Bangko Sentral ng Pilipinas"
  type: pdf
  canonical_url: "https://www.bsp.gov.ph/"
  local_path: pdfs/bsp-fx-manual-morfxt-2025-05.pdf
  edition: in-force
  amended_through: "2025-05-31"
  note: "Archived by another researcher; original URL not recorded (bsp.gov.ph blocks automated clients). Inward-investment sections 32-38 on PDF p42-48; Sec. 37 (registration through AABs) on p46."
- slug: cmic-sbl-short-selling-guidelines
  title: "CMIC Memorandum 2020-005 with the SEC-approved Implementing Guidelines on Securities Borrowing and Lending and Short Selling"
  publisher: "Capital Markets Integrity Corporation (CMIC)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2021/01/SBL_02_RulesRegulations_CMIC_Guidelines-on-SBL-and-Short-Selling.pdf"
  local_path: pdfs/cmic-sbl-short-selling-guidelines.pdf
  edition: in-force
  amended_through: "2020-02-10"
  note: "Scanned; cover memo on p1 (effective 25 Feb 2020). Archived by another researcher."
- slug: eo-113-2026-13th-finl
  title: "Executive Order No. 113 s. 2026, Thirteenth Regular Foreign Investment Negative List"
  publisher: "Office of the President"
  type: pdf
  canonical_url: "https://lawphil.net/executive/execord/eo2026/eo_113_2026.html"
  local_path: pdfs/eo-113-2026-13th-finl.pdf
  edition: in-force
  amended_through: "2026-04-13"
  note: "Signed 13 Apr 2026; effective 15 days after publication; lawphil copy omits the attached lists. Original download URL not recorded."
- slug: eo-175-2022-12th-finl
  title: "Executive Order No. 175 s. 2022, Twelfth Regular Foreign Investment Negative List"
  publisher: "Office of the President"
  type: pdf
  canonical_url: "https://lawphil.net/executive/execord/eo2022/eo_175_2022.html"
  local_path: pdfs/eo-175-2022-12th-finl.pdf
  edition: superseded
  amended_through: "2022-06-27"
  note: "Superseded by EO 113 (2026). Original download URL not recorded."
- slug: ftse-country-classification-interim-2026-03
  title: "FTSE Equity Country Classification: March 2026 Interim Announcement"
  publisher: "FTSE Russell (LSEG)"
  type: pdf
  canonical_url: "https://www.lseg.com/content/dam/ftse-russell/en_us/documents/country-classification/ftse-interim-country-classification-review-2026.pdf"
  local_path: pdfs/ftse-country-classification-interim-2026-03.pdf
  edition: in-force
  amended_through: "2026-04-07"
  note: "Cover date 7 Apr 2026; p5 says the 2026 annual announcement will be published on Tuesday 6 October 2026. Archived by another researcher."
- slug: ftse-geis-ground-rules-2026-09
  title: "FTSE Global Equity Index Series ground rules v14.4 (September 2026), Appendix E country classification"
  publisher: "FTSE Russell"
  type: pdf
  canonical_url: "https://www.lseg.com/en/ftse-russell"
  local_path: pdfs/ftse-geis-ground-rules-2026-09.pdf
  edition: in-force
  amended_through: "undated"
  note: "Cover says September 2026; Philippines 'Secondary emerging' on p45. Archived by another researcher; original URL not recorded."
- slug: msci-accessibility-review-2026
  title: "MSCI 2026 Global Market Accessibility Review"
  publisher: "MSCI Inc."
  type: pdf
  canonical_url: "https://www.msci.com/our-solutions/indexes/market-classification"
  local_path: pdfs/msci-accessibility-review-2026.pdf
  edition: in-force
  amended_through: "undated"
  note: "Cover dated June 2026; Philippines section p43. Archived by another researcher; original URL not recorded."
- slug: msci-philippines-index-factsheet-2026-09
  title: "MSCI Philippines Index factsheet (as of 30 Sep 2026)"
  publisher: "MSCI Inc."
  type: pdf
  canonical_url: "https://www.msci.com/indexes/index/860800/msci-philippines-index"
  local_path: pdfs/msci-philippines-index-factsheet-2026-09.pdf
  edition: in-force
  amended_through: "2026-09-30"
  note: "Archived by another researcher."
- slug: pse-17c-2018-04-16-pds-deal-clarification
  title: "SEC Form 17-C (16 Apr 2018): clarification of the news report 'Bourse backs out of PDS deal'"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/4/2021/02/17-C-16-April-2018-Clarification-of-news-article-on-PDS-deal.pdf"
  local_path: pdfs/pse-17c-2018-04-16-pds-deal-clarification.pdf
  edition: historical
  amended_through: "2018-04-16"
  note: "Archived by another researcher; quotes the Inquirer report (SPA timetable lapsed 31 Mar 2018) and PSE's denial."
- slug: pse-active-tp-summary-2026-07-20
  title: "PSE Active Trading Participants public directory as of 20 Jul 2026"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://www.pse.com.ph/directory/"
  local_path: pdfs/pse-active-tp-summary-2026-07-20.pdf
  edition: in-force
  amended_through: "2026-07-20"
  note: "Count of 123 entries is this researcher's tally of 'Nominee' lines. Archived by another researcher; original URL not recorded."
- slug: pse-amended-mpo-rule-2026-08
  title: "Effectivity of the PSE Amended Rule on Minimum Public Ownership and Revised Guidelines in Determining the Public Ownership of Listed Companies"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2026/08/Memo-to-Public_Effectivity-of-the-Amended-MPO-Rule-Rvsd-PO-Guidelines-v2.pdf"
  local_path: pdfs/pse-amended-mpo-rule-2026-08.pdf
  edition: in-force
  amended_through: "2026-08-11"
  note: ""
- slug: pse-analyst-briefing-1h-2026
  title: "PSE STAR briefing: 1H 2026 updates (17 Aug 2026)"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/4/2026/08/2026.08.17-PSE-STAR-1H-2026.pdf"
  local_path: pdfs/pse-analyst-briefing-1h-2026.pdf
  edition: in-force
  amended_through: "2026-08-17"
  note: "Status badges must be read from the slide image (p9)."
- slug: pse-analyst-briefing-3m-2026
  title: "PSE Overview analyst briefing (18 Mar 2026)"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/4/2026/07/3M-2026-PSE-Analyst-Briefing.pdf"
  local_path: pdfs/pse-analyst-briefing-3m-2026.pdf
  edition: in-force
  amended_through: "2026-03-18"
  note: ""
- slug: pse-annual-report-2013
  title: "PSE Annual Report 2013"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://www.pse.com.ph/"
  local_path: pdfs/pse-annual-report-2013.pdf
  edition: n/a
  amended_through: "2013-12-31"
  note: "Archived by another researcher; direct PDF URL not recorded. FMETF listing on p22 and p25."
- slug: pse-annual-report-2015
  title: "PSE Annual Report 2015"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://ir.pse.com.ph/"
  local_path: pdfs/pse-annual-report-2015.pdf
  edition: historical
  amended_through: "undated"
  note: "FY2015 report; PSEtrade XTS migration on p42. Archived by another researcher; original URL not recorded."
- slug: pse-annual-report-2018
  title: "PSE Annual Report 2018 (audited statements; revenue-recognition notes)"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://ir.pse.com.ph/"
  local_path: pdfs/pse-annual-report-2018.pdf
  edition: historical
  amended_through: "undated"
  note: "FY2018 report; 0.005% transaction fee note on p88. Archived by another researcher; original URL not recorded."
- slug: pse-annual-report-2019
  title: "PSE Annual Report 2019"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://ir.pse.com.ph/"
  local_path: pdfs/pse-annual-report-2019.pdf
  edition: historical
  amended_through: "undated"
  note: "FY2019 report; 0.005% transaction fee note on p48. Archived by another researcher; original URL not recorded."
- slug: pse-annual-report-2025
  title: "PSE Annual Report 2025"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://ir.pse.com.ph/"
  local_path: pdfs/pse-annual-report-2025.pdf
  edition: in-force
  amended_through: "undated"
  note: "FY2025 report with events to about Mar 2026; pipeline statements p37-39. Archived by another researcher; original URL not recorded."
- slug: pse-approved-rules-vwap-trading-2024
  title: "PSE Memorandum CN-No. 2024-0010: Approved Rules on VWAP Trading (Annex A: Revised Trading Rules and Implementing Guidelines amendments)"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2024/02/CN-2024-0010.pdf"
  local_path: pdfs/pse-approved-rules-vwap-trading-2024.pdf
  edition: in-force
  amended_through: "2024-02-01"
  note: "Scanned Annex A: p3 trading-hours schedule, p4 Art. VI, p5-6 phase descriptions, p7 Guideline XXV VWAP parameters."
- slug: pse-asm-2024-presidents-report
  title: "PSE President's Report to stockholders (annual stockholders' meeting, 6 Jul 2024)"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://corporate.pse.com.ph/"
  local_path: pdfs/pse-asm-2024-presidents-report.pdf
  edition: historical
  amended_through: "2024-07-06"
  note: "Board lot 'awaiting SEC approval' p18; short-selling/SBL milestones p24; DR 2025 and derivatives 2026 targets p25. Archived by another researcher; original URL not recorded."
- slug: pse-asm-2025-presidents-report
  title: "PSE President's Report to stockholders (annual stockholders' meeting, 12 Jul 2025)"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://corporate.pse.com.ph/"
  local_path: pdfs/pse-asm-2025-presidents-report.pdf
  edition: historical
  amended_through: "2025-07-12"
  note: "Nasdaq Eqlipse p25; pipeline (ETF, derivatives, market making, GPDR comments received 26 May 2025) p30. Archived by another researcher; original URL not recorded."
- slug: pse-asm-2026-president-report
  title: "PSE President's Report to stockholders (annual stockholders' meeting, 4 Jul 2026)"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://corporate.pse.com.ph/"
  local_path: pdfs/pse-asm-2026-president-report.pdf
  edition: in-force
  amended_through: "2026-07-04"
  note: "Archived by another researcher; original URL not recorded."
- slug: pse-cmic-rules
  title: "Capital Markets Integrity Corporation Rules v1.2 (15 Dec 2011) with SEC approval letters"
  publisher: "Capital Markets Integrity Corporation (CMIC) / PSE"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2021/04/Approved-CMIC-Rules-2.pdf"
  local_path: pdfs/pse-cmic-rules.pdf
  edition: in-force
  amended_through: "2012-02-23"
  note: "Image-only PDF; Art. XI-A (restriction, halt or suspension orders) on p112. Later amendments not located. Archived by another researcher."
- slug: pse-cn-2017-0082-stt-increase-advisory
  title: "PSE Memorandum CN-No. 2017-0082: Increase in Stock Transaction Tax (STT)"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2017-0082.pdf"
  local_path: pdfs/pse-cn-2017-0082-stt-increase-advisory.pdf
  edition: historical
  amended_through: "2017-12-26"
  note: "Scanned."
- slug: pse-cn-2017-0084-stt-increase-effectivity
  title: "PSE Memorandum CN-No. 2017-0084: Advisory on Increase in STT (TRAIN effective 1 Jan 2018)"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2017-0084.pdf"
  local_path: pdfs/pse-cn-2017-0084-stt-increase-effectivity.pdf
  edition: historical
  amended_through: "2017-12-29"
  note: "Scanned."
- slug: pse-cn-2018-0003-train-transition
  title: "PSE Memorandum CN-No. 2018-0003: Transition procedures for RA 10963 (TRAIN), with BIR RMC 2-2018"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2018-0003.pdf"
  local_path: pdfs/pse-cn-2018-0003-train-transition.pdf
  edition: historical
  amended_through: "2018-01-08"
  note: "Scanned attachment (RMC 2-2018) on p2-3."
- slug: pse-cn-2018-0013-index-policy-revision-2018
  title: "PSE Memorandum CN-No. 2018-0013: Revised Policy on Index Management (12% to 15% float; Feb/Aug schedule)"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2018-0013.pdf"
  local_path: pdfs/pse-cn-2018-0013-index-policy-revision-2018.pdf
  edition: superseded
  amended_through: "2018-02-12"
  note: "Scanned."
- slug: pse-cn-2018-0014-index-recomposition-2018-02
  title: "PSE Memorandum CN-No. 2018-0014: Recomposition of PSE indices effective 19 Feb 2018"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2018-0014.pdf"
  local_path: pdfs/pse-cn-2018-0014-index-recomposition-2018-02.pdf
  edition: historical
  amended_through: "2018-02-12"
  note: "Scanned."
- slug: pse-cn-2018-0023-trading-without-settlement-proposal
  title: "PSE Memorandum CN-No. 2018-0023: Proposed rule amendment and guidelines for trading without settlement"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2018-0023.pdf"
  local_path: pdfs/pse-cn-2018-0023-trading-without-settlement-proposal.pdf
  edition: historical
  amended_through: "2018-04-10"
  note: "Proposal only; outcome not found."
- slug: pse-cn-2018-0035-short-selling-guidelines-sec-approved
  title: "PSE Memorandum CN-No. 2018-0035: PSE Guidelines for Short Selling Transactions (SEC-approved 5 Jun 2018)"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2018-0035.pdf"
  local_path: pdfs/pse-cn-2018-0035-short-selling-guidelines-sec-approved.pdf
  edition: superseded
  amended_through: "2018-06-22"
  note: "PSE announcement index lists this as 22 Jul 2018 (typo; the memo is dated 22 Jun 2018)."
- slug: pse-cn-2018-0048-cmic-denial-of-access-meridian
  title: "PSE Memorandum CN-No. 2018-0048: Implementation of CMIC action on Meridian Securities, Inc. (one-day denial of access)"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2018-0048.pdf"
  local_path: pdfs/pse-cn-2018-0048-cmic-denial-of-access-meridian.pdf
  edition: historical
  amended_through: "2018-10-05"
  note: "Archived by another researcher."
- slug: pse-cn-2019-0004-short-selling-guidelines-amendment
  title: "PSE Memorandum CN-No. 2019-0004: Amendments to the PSE Guidelines for Short Selling Transactions"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2019-0004.pdf"
  local_path: pdfs/pse-cn-2019-0004-short-selling-guidelines-amendment.pdf
  edition: superseded
  amended_through: "2019-01-23"
  note: "Incorporated in the Oct 2023 text."
- slug: pse-cn-2019-0031-trading-halt-fire-drill
  title: "PSE Memorandum CN-No. 2019-0031: Trading halt due to fire drill (4 Jun 2019)"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2019-0031.pdf"
  local_path: pdfs/pse-cn-2019-0031-trading-halt-fire-drill.pdf
  edition: historical
  amended_through: "2019-06-04"
  note: "Archived by another researcher."
- slug: pse-cn-2019-0037-foreign-investment-etf
  title: "PSE Memorandum CN-No. 2019-0037: Foreign investment into Philippine Exchange-Traded Fund (BSP Circular 1030 s. 2019)"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2019-0037.pdf"
  local_path: pdfs/pse-cn-2019-0037-foreign-investment-etf.pdf
  edition: historical
  amended_through: "2019-07-08"
  note: ""
- slug: pse-cn-2020-0002-trading-suspension-2020-01-13
  title: "PSE Memorandum CN-No. 2020-0002: Trading suspension, 13 Jan 2020 (Taal volcano ash)"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2020-0002.pdf"
  local_path: pdfs/pse-cn-2020-0002-trading-suspension-2020-01-13.pdf
  edition: historical
  amended_through: "2020-01-13"
  note: "Archived by another researcher."
- slug: pse-cn-2020-0005-amended-reit-listing-rules
  title: "PSE Memorandum CN-No. 2020-0005: Effectivity of the Amended Listing Rules for REITs"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2020-0005.pdf"
  local_path: pdfs/pse-cn-2020-0005-amended-reit-listing-rules.pdf
  edition: in-force
  amended_through: "2020-02-07"
  note: "Scanned attachment."
- slug: pse-cn-2020-0017
  title: "PSE Memorandum CN-No. 2020-0017: Shortened trading hours (16 Mar to 14 Apr 2020)"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2020-0017.pdf"
  local_path: pdfs/pse-cn-2020-0017.pdf
  edition: historical
  amended_through: "2020-03-15"
  note: ""
- slug: pse-cn-2020-0021
  title: "PSE Memorandum CN-No. 2020-0021: Trading suspension starting 17 Mar 2020"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2020-0021.pdf"
  local_path: pdfs/pse-cn-2020-0021.pdf
  edition: historical
  amended_through: "2020-03-16"
  note: ""
- slug: pse-cn-2020-0025-resumption-of-trading
  title: "PSE Memorandum CN-No. 2020-0025: Resumption of trading and settlement (19 Mar 2020)"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2020-0025.pdf"
  local_path: pdfs/pse-cn-2020-0025-resumption-of-trading.pdf
  edition: historical
  amended_through: "2020-03-17"
  note: ""
- slug: pse-cn-2020-0028
  title: "PSE Memorandum CN-No. 2020-0028: Amendment of rule on static threshold (lower bound 50% to 30%)"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2020-0028.pdf"
  local_path: pdfs/pse-cn-2020-0028.pdf
  edition: in-force
  amended_through: "2020-03-21"
  note: ""
- slug: pse-cn-2020-0044
  title: "PSE Memorandum CN-No. 2020-0044: Amendment of circuit breaker rules (three-level system from 4 May 2020)"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2020-0044.pdf"
  local_path: pdfs/pse-cn-2020-0044.pdf
  edition: in-force
  amended_through: "2020-04-29"
  note: ""
- slug: pse-cn-2020-0046
  title: "PSE Memorandum CN-No. 2020-0046: Shortened trading hours under MECQ"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2020-0046.pdf"
  local_path: pdfs/pse-cn-2020-0046.pdf
  edition: historical
  amended_through: "2020-05-14"
  note: ""
- slug: pse-cn-2020-0051-gcq-floor-reopening
  title: "PSE Memorandum CN-No. 2020-0051: Guidelines for GCQ (floor reopening 1 Jun 2020; shortened hours continue)"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2020-0051.pdf"
  local_path: pdfs/pse-cn-2020-0051-gcq-floor-reopening.pdf
  edition: historical
  amended_through: "2020-05-29"
  note: ""
- slug: pse-cn-2020-0052-nonresident-reit-investment
  title: "PSE Memorandum CN-No. 2020-0052: Non-resident investment into Philippine REIT (BSP registration)"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2020-0052.pdf"
  local_path: pdfs/pse-cn-2020-0052-nonresident-reit-investment.pdf
  edition: in-force
  amended_through: "2020-05-26"
  note: ""
- slug: pse-cn-2020-0066-reit-broker-eligibility
  title: "PSE Memorandum CN-No. 2020-0066: Broker eligibility guidelines to trade REIT securities"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2020-0066.pdf"
  local_path: pdfs/pse-cn-2020-0066-reit-broker-eligibility.pdf
  edition: in-force
  amended_through: "2020-07-15"
  note: ""
- slug: pse-cn-2021-0021-amended-listing-rules
  title: "PSE Memorandum CN-No. 2021-0021: Amended Listing Rules (Main and SME Board listing rules; sponsor model; COVID relief)"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2021-0021.pdf"
  local_path: pdfs/pse-cn-2021-0021-amended-listing-rules.pdf
  edition: in-force
  amended_through: "2021-03-24"
  note: "Archived by another researcher; Annex A (24 pages) follows the 2-page memo."
- slug: pse-cn-2021-0046-index-policy-revision-2021
  title: "PSE Memorandum CN-No. 2021-0046: Revised Policy on Index Management and results of index review (float 15% to 20%)"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2021-0046.pdf"
  local_path: pdfs/pse-cn-2021-0046-index-policy-revision-2021.pdf
  edition: in-force
  amended_through: "2021-08-05"
  note: "Scanned."
- slug: pse-cn-2021-0055-lift-lower-static-threshold-sgp
  title: "PSE Memorandum CN-No. 2021-0055: Synergy Grid (SGP): lifting of lower static threshold"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2021-0055.pdf"
  local_path: pdfs/pse-cn-2021-0055-lift-lower-static-threshold-sgp.pdf
  edition: historical
  amended_through: "2021-10-27"
  note: ""
- slug: pse-cn-2021-0059
  title: "PSE Memorandum CN-No. 2021-0059: Adjustments in trading hours (effective 6 Dec 2021)"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2021-0059.pdf"
  local_path: pdfs/pse-cn-2021-0059.pdf
  edition: superseded
  amended_through: "2021-11-22"
  note: ""
- slug: pse-cn-2021-0063-half-day-trading-2021-12
  title: "PSE Memorandum CN-No. 2021-0063: Half-day trading on 24 and 31 December 2021"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2021-0063.pdf"
  local_path: pdfs/pse-cn-2021-0063-half-day-trading-2021-12.pdf
  edition: historical
  amended_through: "2021-12-15"
  note: "Archived by another researcher."
- slug: pse-cn-2022-0001-delay-market-opening
  title: "PSE Memorandum CN-No. 2022-0001: Delay in market opening and trading (4 Jan 2022)"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2022-0001.pdf"
  local_path: pdfs/pse-cn-2022-0001-delay-market-opening.pdf
  edition: historical
  amended_through: "2022-01-04"
  note: ""
- slug: pse-cn-2022-0002-cancellation-of-trading-2022-01-04
  title: "PSE Memorandum CN-No. 2022-0002: Cancellation of trading (4 Jan 2022)"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2022-0002.pdf"
  local_path: pdfs/pse-cn-2022-0002-cancellation-of-trading-2022-01-04.pdf
  edition: historical
  amended_through: "2022-01-04"
  note: ""
- slug: pse-cn-2022-0004
  title: "PSE Memorandum CN-No. 2022-0004: Shortened trading hours (14-31 Jan 2022)"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2022-0004.pdf"
  local_path: pdfs/pse-cn-2022-0004.pdf
  edition: historical
  amended_through: "2022-01-11"
  note: ""
- slug: pse-cn-2022-0009-trading-schedule-mar-2022
  title: "PSE Memorandum CN-No. 2022-0009: Trading schedule effective 1 Mar 2022"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2022-0009.pdf"
  local_path: pdfs/pse-cn-2022-0009-trading-schedule-mar-2022.pdf
  edition: superseded
  amended_through: "2022-02-17"
  note: ""
- slug: pse-cn-2022-0010-edge-cutoff-330pm
  title: "PSE Memorandum CN-No. 2022-0010: Cut-off for posting disclosures on the PSE EDGE portal (3:30 pm)"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2022-0010.pdf"
  local_path: pdfs/pse-cn-2022-0010-edge-cutoff-330pm.pdf
  edition: superseded
  amended_through: "2022-02-24"
  note: "Archived by another researcher; superseded by CN-2026-0024 (4:00 pm)."
- slug: pse-cn-2022-0013-launch-midcap-divy-indices
  title: "PSE Memorandum CN-No. 2022-0013: Launch of the PSE Dividend Yield and PSE MidCap indices"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2022-0013.pdf"
  local_path: pdfs/pse-cn-2022-0013-launch-midcap-divy-indices.pdf
  edition: in-force
  amended_through: "2022-03-28"
  note: ""
- slug: pse-cn-2022-0020-market-halt-consultation
  title: "PSE Memorandum CN-No. 2022-0020: Proposed amendments to Revised Trading Rules and Consolidated Listing and Disclosure Rules (market-halt threshold)"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2022-0020.pdf"
  local_path: pdfs/pse-cn-2022-0020-market-halt-consultation.pdf
  edition: historical
  amended_through: "2022-05-11"
  note: "Consultation; the halt-threshold change took effect 20 Aug 2025."
- slug: pse-cn-2022-0035-trading-suspension-2022-09-26
  title: "PSE Memorandum CN-No. 2022-0035: Trading suspension (26 Sep 2022)"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2022-0035.pdf"
  local_path: pdfs/pse-cn-2022-0035-trading-suspension-2022-09-26.pdf
  edition: historical
  amended_through: "2022-09-25"
  note: "Original URL assumed from PSE's standard pattern."
- slug: pse-cn-2022-0045-consultation-2022-part-ii
  title: "PSE Memorandum CN-No. 2022-0045: Request for comments: proposed amendments to the Consolidated Listing and Disclosure Rules and Revised Trading Rules (2022 amendments, Part II)"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2022-0045.pdf"
  local_path: pdfs/pse-cn-2022-0045-consultation-2022-part-ii.pdf
  edition: historical
  amended_through: "2022-11-16"
  note: "Archived by another researcher; consultation only."
- slug: pse-cn-2023-0022-stabilization-fund
  title: "PSE Memorandum CN-No. 2023-0022: Amendments to Article III, Part A of the Consolidated Listing and Disclosure Rules (stabilisation fund)"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2023-0022.pdf"
  local_path: pdfs/pse-cn-2023-0022-stabilization-fund.pdf
  edition: in-force
  amended_through: "2023-05-12"
  note: "Scanned; archived by another researcher."
- slug: pse-cn-2023-0027-offshore-collateral-sbl
  title: "PSE Memorandum CN-No. 2023-0027: Acceptance of offshore collateral in SBL transactions involving at least one foreign party"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2023-0027.pdf"
  local_path: pdfs/pse-cn-2023-0027-offshore-collateral-sbl.pdf
  edition: in-force
  amended_through: "2023-05-24"
  note: "Scanned."
- slug: pse-cn-2023-0031-t2-settlement
  title: "PSE Memorandum CN-No. 2023-0031: Migration to the T+2 settlement cycle (with SCCP Memo 01-0623)"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2023-0031.pdf"
  local_path: pdfs/pse-cn-2023-0031-t2-settlement.pdf
  edition: historical
  amended_through: "2023-06-23"
  note: ""
- slug: pse-cn-2023-0040-t2-go-live
  title: "PSE Memorandum CN-No. 2023-0040: Go-live of the migration to T+2 on 24 Aug 2023 (with SCCP Memo 04-0823)"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2023/08/CN_2023-0040-1.pdf"
  local_path: pdfs/pse-cn-2023-0040-t2-go-live.pdf
  edition: historical
  amended_through: "2023-08-15"
  note: ""
- slug: pse-cn-2023-0041-mpo-delisting-consult
  title: "PSE Memorandum CN-No. 2023-0041: Proposed amendments to the Public Ownership Guidelines, the Amended MPO Rule and the Amended Voluntary Delisting Rules"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2023-0041.pdf"
  local_path: pdfs/pse-cn-2023-0041-mpo-delisting-consult.pdf
  edition: historical
  amended_through: "2023-08-25"
  note: "Consultation (comments to 8 Sep 2023); adoption date not found. Archived by another researcher."
- slug: pse-cn-2023-0043
  title: "PSE Memorandum CN-No. 2023-0043: Proposed amendments to Revised Trading Rules re algorithmic trading and VWAP trading"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2023-0043.pdf"
  local_path: pdfs/pse-cn-2023-0043.pdf
  edition: historical
  amended_through: "2023-09-05"
  note: "VWAP part adopted 2024; algorithmic part outcome not found."
- slug: pse-cn-2023-0048
  title: "PSE Memorandum CN-No. 2023-0048: Regulatory framework for SBL and short selling (effectivity of Short Selling Guidelines)"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2023-0048.pdf"
  local_path: pdfs/pse-cn-2023-0048.pdf
  edition: in-force
  amended_through: "2023-10-02"
  note: "Pages 8-11 hold the guidelines text 'as of January 2019'."
- slug: pse-cn-2023-0051
  title: "PSE Memorandum CN-No. 2023-0051: Proposed amendments to the PSE Board Lot (2023 consultation)"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2023-0051.pdf"
  local_path: pdfs/pse-cn-2023-0051.pdf
  edition: historical
  amended_through: "2023-10-09"
  note: "Scanned; proposal not adopted."
- slug: pse-cn-2023-0055
  title: "PSE Memorandum CN-No. 2023-0055: Request for comments: proposed amendments to Part XXI of the Implementing Guidelines and Guidelines on Natural Disasters or Extraordinary Circumstances"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2023-0055.pdf"
  local_path: pdfs/pse-cn-2023-0055.pdf
  edition: superseded
  amended_through: "2023-10-17"
  note: "Archived by another researcher; consultation only (final form CN-2025-0037)."
- slug: pse-cn-2023-0056
  title: "PSE Memorandum CN-No. 2023-0056: Short Selling Program go-live (6 Nov 2023)"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2023-0056.pdf"
  local_path: pdfs/pse-cn-2023-0056.pdf
  edition: historical
  amended_through: "2023-10-19"
  note: ""
- slug: pse-cn-2024-0001-market-halt
  title: "PSE Memorandum CN-No. 2024-0001: Market halt (3 Jan 2024)"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2024-0001.pdf"
  local_path: pdfs/pse-cn-2024-0001-market-halt.pdf
  edition: historical
  amended_through: "2024-01-03"
  note: ""
- slug: pse-cn-2024-0003-update-market-halt
  title: "PSE Memorandum CN-No. 2024-0003: Update on the market halt (3 Jan 2024)"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2024-0003.pdf"
  local_path: pdfs/pse-cn-2024-0003-update-market-halt.pdf
  edition: historical
  amended_through: "2024-01-03"
  note: ""
- slug: pse-cn-2024-0008
  title: "PSE Memorandum CN-No. 2024-0008: Results of the review of PSE indices and index policy update"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2024-0008.pdf"
  local_path: pdfs/pse-cn-2024-0008.pdf
  edition: in-force
  amended_through: "2024-01-26"
  note: ""
- slug: pse-cn-2024-0012-vwap-go-live
  title: "PSE Memorandum CN-No. 2024-0012: VWAP trading go-live (1 Mar 2024)"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2024-0012.pdf"
  local_path: pdfs/pse-cn-2024-0012-vwap-go-live.pdf
  edition: historical
  amended_through: "2024-02-15"
  note: ""
- slug: pse-cn-2024-0029-min-commission-removal
  title: "PSE Memorandum CN-No. 2024-0029: Removal of minimum commission charges (SEC MC 7-2024 attached)"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2024-0029.pdf"
  local_path: pdfs/pse-cn-2024-0029-min-commission-removal.pdf
  edition: in-force
  amended_through: "2024-05-17"
  note: "Pages 2-3 hold SEC MC 7-2024 (16 Apr 2024)."
- slug: pse-cn-2024-0035
  title: "PSE Memorandum CN-No. 2024-0035: Amendments to BIR Revenue Regulations on SBL (RR 10-2024)"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2024-0035.pdf"
  local_path: pdfs/pse-cn-2024-0035.pdf
  edition: in-force
  amended_through: "2024-07-09"
  note: "Scanned annex."
- slug: pse-cn-2024-0038-trading-suspension-2024-07-24
  title: "PSE Memorandum CN-No. 2024-0038: Trading suspension (24 Jul 2024)"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2024/09/CN-2024-0038.pdf"
  local_path: pdfs/pse-cn-2024-0038-trading-suspension-2024-07-24.pdf
  edition: historical
  amended_through: "2024-07-24"
  note: ""
- slug: pse-cn-2024-0047
  title: "PSE Memorandum CN-No. 2024-0047: Proposed rules for Global Philippine Depositary Receipts"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2024-0047.pdf"
  local_path: pdfs/pse-cn-2024-0047.pdf
  edition: historical
  amended_through: "2024-09-26"
  note: "Consultation; rules still awaiting SEC approval (Aug 2026)."
- slug: pse-cn-2024-0048-consultation-blackout-rule
  title: "PSE Memorandum CN-No. 2024-0048: Request for comments: proposed amendments to the Listing and Disclosure Rules and Revised Trading Rules (black-out rule, error-account liquidation)"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2024-0048.pdf"
  local_path: pdfs/pse-cn-2024-0048-consultation-blackout-rule.pdf
  edition: historical
  amended_through: "2024-09-30"
  note: "Archived by another researcher; consultation only."
- slug: pse-cn-2024-0053-equitiworld-involuntary-suspension
  title: "PSE Memorandum CN-No. 2024-0053: Equitiworld Securities, Inc.: involuntary suspension and preservation order"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2024-0053.pdf"
  local_path: pdfs/pse-cn-2024-0053-equitiworld-involuntary-suspension.pdf
  edition: historical
  amended_through: "2024-10-10"
  note: ""
- slug: pse-cn-2024-0061-adjusted-schedule-2024-12-09
  title: "PSE Memorandum CN-No. 2024-0061: Adjusted trading schedule (9 Dec 2024)"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2024-0061.pdf"
  local_path: pdfs/pse-cn-2024-0061-adjusted-schedule-2024-12-09.pdf
  edition: historical
  amended_through: "2024-12-09"
  note: ""
- slug: pse-cn-2024-0068-almf-effectivity
  title: "PSE Memorandum CN-No. 2024-0068: Effectivity of the amended annual listing maintenance fee (ALMF) upper limit"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2024-0068.pdf"
  local_path: pdfs/pse-cn-2024-0068-almf-effectivity.pdf
  edition: in-force
  amended_through: "2024-12-19"
  note: "Archived by another researcher."
- slug: pse-cn-2025-0015-adjusted-schedule-2025-03-24
  title: "PSE Memorandum CN-No. 2025-0015: Adjusted trading schedule (24 Mar 2025)"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2025-0015.pdf"
  local_path: pdfs/pse-cn-2025-0015-adjusted-schedule-2025-03-24.pdf
  edition: historical
  amended_through: "2025-03-24"
  note: "Notice text is dated 24 Mar 2025; PSE index shows 31 Mar 2025."
- slug: pse-cn-2025-0026-stt-decrease-advisory
  title: "PSE Memorandum CN-No. 2025-0026: Advisory on decrease of Stock Transaction Tax"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2025-0026.pdf"
  local_path: pdfs/pse-cn-2025-0026-stt-decrease-advisory.pdf
  edition: in-force
  amended_through: "2025-06-11"
  note: ""
- slug: pse-cn-2025-0028-cmepa-effectivity
  title: "PSE Memorandum CN-No. 2025-0028: Effectivity of RA 12214 (CMEPA)"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2025-0028.pdf"
  local_path: pdfs/pse-cn-2025-0028-cmepa-effectivity.pdf
  edition: in-force
  amended_through: "2025-06-26"
  note: ""
- slug: pse-cn-2025-0032-bir-stt-advisory
  title: "PSE Memorandum CN-No. 2025-0032: BIR tax advisory on manual payment of the revised STT under CMEPA"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2025/07/CN-2025-0032.pdf"
  local_path: pdfs/pse-cn-2025-0032-bir-stt-advisory.pdf
  edition: historical
  amended_through: "2025-07-15"
  note: "Archived by another researcher (a different file version from the one fetched by this researcher)."
- slug: pse-cn-2025-0035-sec-declassification-mandate
  title: "PSE Memorandum CN-No. 2025-0035: SEC mandate of declassification of Class A and Class B shares (SEC MC 10-2025 attached)"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2025-0035.pdf"
  local_path: pdfs/pse-cn-2025-0035-sec-declassification-mandate.pdf
  edition: in-force
  amended_through: "2025-08-11"
  note: ""
- slug: pse-cn-2025-0036-declassification-effectivity
  title: "PSE Memorandum CN-No. 2025-0036: Effectivity of SEC circular mandating declassification of Class A/B shares"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2025-0036.pdf"
  local_path: pdfs/pse-cn-2025-0036-declassification-effectivity.pdf
  edition: in-force
  amended_through: "2025-08-15"
  note: ""
- slug: pse-cn-2025-0037
  title: "PSE Memorandum CN-No. 2025-0037: Amendments to Revised Trading Rules (market halt), correspondent TP guidelines, natural-disaster guidelines"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2025-0037.pdf"
  local_path: pdfs/pse-cn-2025-0037.pdf
  edition: in-force
  amended_through: "2025-08-20"
  note: ""
- slug: pse-cn-2025-0046-board-lot-trading-at-last
  title: "PSE Memorandum CN-No. 2025-0046: Request for comments: proposed amendments to the PSE board lot and rule on trading during run-off/trading-at-last"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2025-0046.pdf"
  local_path: pdfs/pse-cn-2025-0046-board-lot-trading-at-last.pdf
  edition: in-force
  amended_through: "2025-12-15"
  note: "Consultation paper; not yet adopted. Page 4 holds the current and proposed lot/tick tables."
- slug: pse-cn-2025-0047-sector-reclassification
  title: "PSE Memorandum CN-No. 2025-0047: Sector reclassification of 13 companies (effective 5 Jan 2026)"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2025-0047.pdf"
  local_path: pdfs/pse-cn-2025-0047-sector-reclassification.pdf
  edition: in-force
  amended_through: "2025-12-26"
  note: "Archived by another researcher."
- slug: pse-cn-2026-0004-2-emergency-disclosures-trading-halt
  title: "PSE Memorandum CN-No. 2026-0004: Emergency disclosures and trading halt (MRC Allied)"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2026/01/CN-2026-0004-2.pdf"
  local_path: pdfs/pse-cn-2026-0004-2-emergency-disclosures-trading-halt.pdf
  edition: historical
  amended_through: "2026-01-19"
  note: "Archived by another researcher."
- slug: pse-cn-2026-0009
  title: "PSE Memorandum CN-No. 2026-0009: Proposed amendments to the PSE Rules on SBL and rationalization of SBL reports"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2026-0009.pdf"
  local_path: pdfs/pse-cn-2026-0009.pdf
  edition: in-force
  amended_through: "2026-02-03"
  note: "Consultation; revised SBL rules awaiting SEC approval."
- slug: pse-cn-2026-0012
  title: "PSE Memorandum CN-No. 2026-0012: Updates on Equitiworld Securities, Inc. (CMIC notice of 19 Mar 2026 on SEC-approved liquidation and allocation plan)"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2026-0012.pdf"
  local_path: pdfs/pse-cn-2026-0012.pdf
  edition: historical
  amended_through: "2026-03-19"
  note: "Page 2 (CMIC notice) is a scan I did not read in full. Archived by another researcher."
- slug: pse-cn-2026-0013-ati-voluntary-delisting
  title: "PSE Memorandum CN-No. 2026-0013: Asian Terminals, Inc.: approval of petition for voluntary delisting (effective 3 Apr 2026)"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2026-0013.pdf"
  local_path: pdfs/pse-cn-2026-0013-ati-voluntary-delisting.pdf
  edition: historical
  amended_through: "2026-03-25"
  note: ""
- slug: pse-cn-2026-0018
  title: "PSE Memorandum CN-No. 2026-0018: Request for comments on SEC's proposed regulations for structured warrants"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2026-0018.pdf"
  local_path: pdfs/pse-cn-2026-0018.pdf
  edition: in-force
  amended_through: "2026-04-30"
  note: "Scanned; comments to the SEC until 13 May 2026."
- slug: pse-cn-2026-0020-mpo-consult
  title: "PSE Memorandum CN-No. 2026-0020: 2026 proposed revisions to the Amended Rule on Minimum Public Ownership (SEC MC 11-2026 attached)"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2026-0020.pdf"
  local_path: pdfs/pse-cn-2026-0020-mpo-consult.pdf
  edition: superseded
  amended_through: "2026-05-13"
  note: "Annex A (p6-10) is the SEC MC 11-2026 text, 'Done this __ February 2026'."
- slug: pse-cn-2026-0022
  title: "PSE Memorandum CN-No. 2026-0022: Updates on PDTC Lending Agency Service for the PSE SBL Program (with PDS Group Memo 03-2026)"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2026/05/Memorandum-Updates-on-PDTC-Lending-Agency-Service-for-PSE-SBL-1.pdf"
  local_path: pdfs/pse-cn-2026-0022.pdf
  edition: in-force
  amended_through: "2026-05-18"
  note: "Scanned; PDS Group memo on p2 dated 22 Apr 2026. Archived by another researcher."
- slug: pse-cn-2026-0024-edge-cutoff-4pm
  title: "PSE Memorandum CN-No. 2026-0024: cut-off for posting disclosures on the EDGE portal (4:00 pm, effective 25 May 2026)"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2026/05/CN-No.-2026-0024.pdf"
  local_path: pdfs/pse-cn-2026-0024-edge-cutoff-4pm.pdf
  edition: in-force
  amended_through: "2026-05-22"
  note: "Archived by another researcher."
- slug: pse-cn-2026-0025
  title: "PSE Memorandum CN-No. 2026-0025: 2026 Revised Guidelines for Master Securities Lending Agreement (MSLA) clearance (SEC-approved 15 May 2026)"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2026/05/CN-2026-0025.pdf"
  local_path: pdfs/pse-cn-2026-0025.pdf
  edition: in-force
  amended_through: "2026-05-22"
  note: "Scanned; PSE index lists the memo under 25 May 2026. Archived by another researcher."
- slug: pse-cn-2026-0026
  title: "PSE Memorandum CN-No. 2026-0026: Invitation to submit comments on the amendments to the PSE Market Making Rules"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2026-0026.pdf"
  local_path: pdfs/pse-cn-2026-0026.pdf
  edition: in-force
  amended_through: "2026-06-03"
  note: "Scanned; consultation (comments to 23 Jun 2026)."
- slug: pse-cn-2026-0029-etf-amend-consult
  title: "PSE Memorandum CN-No. 2026-0029: Proposed amendments to PSE Rules on Exchange Traded Funds"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2026-0029.pdf"
  local_path: pdfs/pse-cn-2026-0029-etf-amend-consult.pdf
  edition: in-force
  amended_through: "2026-06-16"
  note: "Scanned; consultation (comments to 30 Jun 2026)."
- slug: pse-cn-2026-0031-negotiated-trades
  title: "PSE Memorandum CN-No. 2026-0031: Proposed Rules on Negotiated Trades"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2026-0031.pdf"
  local_path: pdfs/pse-cn-2026-0031-negotiated-trades.pdf
  edition: in-force
  amended_through: "2026-07-01"
  note: "Consultation (comments 1-7 Jul 2026). Archived by another researcher."
- slug: pse-cn-2026-0033b
  title: "PSE Memorandum CN-No. 2026-0033B: Revised Policy on Index Management (July 2026 policy attached)"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2026/07/CN-2026-0033B.pdf"
  local_path: pdfs/pse-cn-2026-0033b.pdf
  edition: in-force
  amended_through: "2026-07-21"
  note: "Methodology changes apply at the Feb 2027 rebalancing."
- slug: pse-cn-2026-0035
  title: "PSE Memorandum CN-No. 2026-0035: Results of the review of PSE indices (effective 3 Aug 2026)"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2026-0035.pdf"
  local_path: pdfs/pse-cn-2026-0035.pdf
  edition: in-force
  amended_through: "2026-07-27"
  note: ""
- slug: pse-cn-2026-0037-preferred-shares-rule-effectivity
  title: "PSE Memorandum CN-No. 2026-0037: Effectivity of the PSE rule on listing through IPO or direct listing of preferred shares"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2026/08/CN-No.-2026-0037.pdf"
  local_path: pdfs/pse-cn-2026-0037-preferred-shares-rule-effectivity.pdf
  edition: in-force
  amended_through: "2026-08-12"
  note: ""
- slug: pse-cn-2026-0038-rrhi-voluntary-delisting
  title: "PSE Memorandum CN-No. 2026-0038: Approval of the voluntary delisting of Robinsons Retail Holdings, Inc. (effective 31 Aug 2026)"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2026/08/CN-No.-2026-0038.pdf"
  local_path: pdfs/pse-cn-2026-0038-rrhi-voluntary-delisting.pdf
  edition: historical
  amended_through: "2026-08-20"
  note: ""
- slug: pse-cn-2026-0039-sec-market-making-rfc
  title: "PSE Memorandum CN-No. 2026-0039: request for comments on SEC's proposed Rules on Market Making (SEC notice and draft attached)"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2026/08/CN-No.-2026-0039.pdf"
  local_path: pdfs/pse-cn-2026-0039-sec-market-making-rfc.pdf
  edition: in-force
  amended_through: "2026-08-20"
  note: "SEC exposure draft (En Banc 13 Aug 2026; comments to 28 Aug 2026); not a final rule. Archived by another researcher."
- slug: pse-cn-2026-0041-declassification-price-suspension
  title: "PSE Memorandum (filed as 2026-0041): price adjustment upon declassification of shares and trade suspension prior to delisting"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2026/09/2026-0041-Declassification-Price-Adjustment-and-Trading-Suspension-Mechanics.pdf"
  local_path: pdfs/pse-cn-2026-0041-declassification-price-suspension.pdf
  edition: in-force
  amended_through: "2026-09-10"
  note: "PSE also uses CN-2026-0041 for the SME Board sponsor-model consultation of 28 Aug 2026. Archived by another researcher."
- slug: pse-cn-2026-0046-edge-outage-access-to-disclosures
  title: "PSE EDGE announcement CN-No. 2026-0046: Access to disclosures via PSE website (EDGE portal unavailable, 6 Oct 2026)"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2026/10/Access-to-Disclosures-via-PSE-Website.pdf"
  local_path: pdfs/pse-cn-2026-0046-edge-outage-access-to-disclosures.pdf
  edition: historical
  amended_through: "2026-10-06"
  note: "CN number taken from the follow-up batches that cite it; the memo itself shows no number."
- slug: pse-dssr-2023-11-06
  title: "PSE Daily Short Selling Report, 6 Nov 2023 (first day of the program)"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://www.pse.com.ph/market-report/"
  local_path: pdfs/pse-dssr-2023-11-06.pdf
  edition: historical
  amended_through: "2023-11-06"
  note: "53 eligible securities, all with zero short-sale volume. Archived by another researcher; original URL not recorded."
- slug: pse-dssr-2026-10-05
  title: "PSE Daily Short Selling Report, 5 Oct 2026"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://www.pse.com.ph/market-report/"
  local_path: pdfs/pse-dssr-2026-10-05.pdf
  edition: in-force
  amended_through: "2026-10-05"
  note: "52 eligible securities plus previously eligible entries, all with zero short-sale volume and null short-interest ratio. Archived by another researcher; original URL not recorded."
- slug: pse-etf-rules
  title: "SEC Approved PSE ETF Rules (18 Mar 2013), incl. Part C ETF Market Making Rules"
  publisher: "The Philippine Stock Exchange, Inc. (PSE) / Securities and Exchange Commission"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2021/04/PSE-ETF-RULES-A-B-C-for-Website.pdf"
  local_path: pdfs/pse-etf-rules.pdf
  edition: in-force
  amended_through: "2013-03-18"
  note: "Archived by another researcher; market-maker obligations on p22-23; amendments proposed in 2026 (CN-2026-0029) are not in force."
- slug: pse-implementing-guidelines-trading-rules
  title: "Implementing Guidelines of the Revised Trading Rules (PSE memorandum 2010-0340 of 22 Jul 2010)"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2021/04/Implementing-Guidelines-of-the-Revised-Trading-Rules.pdf"
  local_path: pdfs/pse-implementing-guidelines-trading-rules.pdf
  edition: superseded
  amended_through: "2010-07-22"
  note: "Archived by another researcher; effective with the new trading system on 26 Jul 2010 (p1); later amended (2011, 2013, 2020, 2024, 2025)."
- slug: pse-index-policy-feb2018
  title: "PSE Policy on Index Management (February 2018)"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://www.pse.com.ph/indices/"
  local_path: pdfs/pse-index-policy-feb2018.pdf
  edition: superseded
  amended_through: "2018-02-12"
  note: "Cover says February 2018; date taken from the covering memo CN-2018-0013. Archived by another researcher; original URL not recorded."
- slug: pse-listing-disclosure-rules
  title: "PSE Consolidated Listing and Disclosure Rules (published as of January 2025)"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2025/01/Consolidated-Listing-and-Disclosure-Rules-Updated-011025.pdf"
  local_path: pdfs/pse-listing-disclosure-rules.pdf
  edition: in-force
  amended_through: "2025-01-08"
  note: "Archived by another researcher; the supplemental-rule index (PDF p13-15) lists each amendment memo with its date; later changes (MPO 11 Aug 2026, preferred shares 12 Aug 2026, EDGE cut-off) are separate memoranda."
- slug: pse-memo-2026-10-01-sec-rfc-src-28-1-33-1-capital
  title: "PSE Memorandum: SEC request for comments on proposed amendments to SRC Rules 28.1 and 33.1 (broker-dealer paid-up capital and surety bond)"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2026/10/SEC-Request-for-Comments-on-Proposed-Amendments-to-SRC-Rules-28.1-and-33.1.pdf"
  local_path: pdfs/pse-memo-2026-10-01-sec-rfc-src-28-1-33-1-capital.pdf
  edition: in-force
  amended_through: "2026-10-01"
  note: "SEC exposure draft (En Banc 24 Sep 2026; comments to 14 Oct 2026); not a final rule."
- slug: pse-memo-extended-pre-close-implementation-2013
  title: "PSE Memorandum TPA-2013-0165: implementation of extended pre-close period (from 4 Nov 2013)"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://www.pse.com.ph/regulation-trading-participants/"
  local_path: pdfs/pse-memo-extended-pre-close-implementation-2013.pdf
  edition: historical
  amended_through: "2013-10-14"
  note: "Archived by another researcher; original URL not recorded."
- slug: pse-memo-new-trading-hours-2011
  title: "PSE Memorandum TPA-2011-0108: PSE new trading hours (effective 2 Jan 2012)"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://www.pse.com.ph/regulation-trading-participants/"
  local_path: pdfs/pse-memo-new-trading-hours-2011.pdf
  edition: historical
  amended_through: "2011-12-06"
  note: "Archived by another researcher; original URL not recorded."
- slug: pse-memo-pre-close-schedule-2013
  title: "PSE Memorandum TPA-2013-0167: pre-close schedule (from 4 Nov 2013)"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://www.pse.com.ph/regulation-trading-participants/"
  local_path: pdfs/pse-memo-pre-close-schedule-2013.pdf
  edition: historical
  amended_through: "2013-10-16"
  note: "Archived by another researcher; original URL not recorded."
- slug: pse-memo-sec-approved-dma-rules-2013-11-26
  title: "PSE memorandum of 26 Nov 2013 with the SEC-approved Rules on Direct Market Access (DMA)"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/AnnouncementOPSPDF/SEC-Approved%20Direct%20Market%20Access%20(DMA)%20Rules.pdf"
  local_path: pdfs/pse-memo-sec-approved-dma-rules-2013-11-26.pdf
  edition: in-force
  amended_through: "2013-11-26"
  note: "Archived by another researcher; scanned; effective on the first trading day of 2014 (p1); Sec. 9 restrictions on p8."
- slug: pse-memo-tp-paid-up-capital-increase-2026-07
  title: "PSE consultation paper: proposed increase in minimum unimpaired paid-up capital of trading participants"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2026/07/Memo-to-Public_Proposed-Increase-in-the-Unimpaired-Paid-Up-Capital-of-TP-1.pdf"
  local_path: pdfs/pse-memo-tp-paid-up-capital-increase-2026-07.pdf
  edition: in-force
  amended_through: "2026-07-21"
  note: "Consultation (comments to 31 Jul 2026). Archived by another researcher."
- slug: pse-nte-broker-forum-2026-07-09
  title: "PSE Broker Forum deck: New Trading Engine, PSETradeX, PSE Back-office Updates (9 Jul 2026)"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2026/07/PSE-New-Trading-Engine-TradeX-Back-office_Broker-Forum_07092026-1.pdf"
  local_path: pdfs/pse-nte-broker-forum-2026-07-09.pdf
  edition: in-force
  amended_through: "2026-07-09"
  note: "Project schedule on p9 (go-live 23 Nov 2026). Archived by another researcher."
- slug: pse-nte-faq-2026-08
  title: "PSE New Trading Engine: Frequently Asked Questions"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2026/08/Frequent-Asked-Questions.pdf"
  local_path: pdfs/pse-nte-faq-2026-08.pdf
  edition: in-force
  amended_through: "undated"
  note: "Posted August 2026 (path year/month); text refers to 23 Sep certification and 23 Jul final specs. Archived by another researcher."
- slug: pse-nte-user-group-2026-01-15
  title: "PSE Broker Forum deck: New Trading Engine, PSETradeX, Back-office (15 Jan 2026)"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2026/06/NTE-User-Group.pdf"
  local_path: pdfs/pse-nte-user-group-2026-01-15.pdf
  edition: in-force
  amended_through: "2026-01-15"
  note: "Lot/tick tables p9-10; run-off examples p11-15. Archived by another researcher."
- slug: pse-revised-trading-rules
  title: "PSE Revised Trading Rules (SEC-approved 1 Jun 2010; scanned)"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2021/04/Revised-Trading-Rules.pdf"
  local_path: pdfs/pse-revised-trading-rules.pdf
  edition: superseded
  amended_through: "undated"
  note: "Archived by another researcher; image-only 2010 base text (memo 2010-0275); amended piecemeal since (2011, 2013, 2020, 2024, 2025). Art. IV Sec. 7 (static threshold; warrants exempt) on p20."
- slug: pse-sbl-short-selling-intro-presentation
  title: "PSE presentation: An Introduction to the PSE SBL and Short Selling Programs (Nov 2018)"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2021/01/Presentation_Introduction-to-the-PSE-SBL-and-Short-Selling-Programs.pdf"
  local_path: pdfs/pse-sbl-short-selling-intro-presentation.pdf
  edition: historical
  amended_through: "2018-11"
  note: "Archived by another researcher; milestone dates 2006-2018 on p2."
- slug: pse-sbl-short-selling-webinar-2023
  title: "PSE webinar deck: PSE's SBL and Short Selling Programs for retail investors (Oct 2023)"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2023/10/SBL-and-Short-Selling-Webinar-for-Retail-Investors-jgg.pdf"
  local_path: pdfs/pse-sbl-short-selling-webinar-2023.pdf
  edition: historical
  amended_through: "2023-10-06"
  note: "Archived by another researcher; regulatory milestones on p3 and p22."
- slug: pse-sccp-revised-rules
  title: "SCCP Revised Clearinghouse Rules as amended effective 23 Jul 2012 (PSE-hosted copy)"
  publisher: "Securities Clearing Corporation of the Philippines (SCCP)"
  type: pdf
  canonical_url: "https://www.sccp.com.ph/"
  local_path: pdfs/pse-sccp-revised-rules.pdf
  edition: superseded
  amended_through: "2012-07-23"
  note: "Archived by another researcher; Rule 5.2 on p35 still says there is no return of cash contributions."
- slug: pse-sr3-2-reit-listing-amend-2023
  title: "PSE Listing Rules for REITs (2023 amendments; CN-2023-0010 of 9 Mar 2023)"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://www.pse.com.ph/regulation-listed-company/"
  local_path: pdfs/pse-sr3-2-reit-listing-amend-2023.pdf
  edition: in-force
  amended_through: "2023-03-09"
  note: "Archived by another researcher; 22 pages; Sec. 4 criteria on p2-3. Original URL not recorded."
- slug: pse-sr6-2-mpo-initial-backdoor-2020
  title: "PSE Memorandum CN-No. 2020-0076: Guidelines on minimum public ownership for initial and backdoor listings"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2020-0076.pdf"
  local_path: pdfs/pse-sr6-2-mpo-initial-backdoor-2020.pdf
  edition: superseded
  amended_through: "2020-08-03"
  note: "Replaced by the Aug 2026 Amended MPO Rule."
- slug: pse-sr6-mpo-rule-2012
  title: "PSE Amended Rule on Minimum Public Ownership (CN-2012-0003 of 3 Jan 2012; effective 1 Jan 2012)"
  publisher: "The Philippine Stock Exchange, Inc. (PSE) / Securities and Exchange Commission"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2022/08/Supplemental-Rule-6-Amended-MPO-Rule.pdf"
  local_path: pdfs/pse-sr6-mpo-rule-2012.pdf
  edition: superseded
  amended_through: "2012-01-03"
  note: "Archived by another researcher; scanned; superseded for new listings by the Aug 2026 rule."
- slug: pse-sr7-backdoor-listing-2022
  title: "PSE CN-2022-0026 (22 Jun 2022): Revised Rules on Backdoor Listing"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://www.pse.com.ph/regulation-listed-company/"
  local_path: pdfs/pse-sr7-backdoor-listing-2022.pdf
  edition: in-force
  amended_through: "2022-06-22"
  note: "Archived by another researcher; original URL not recorded; Sec. 3 (trading suspension and halts) on p4."
- slug: pse-sr8-1-voluntary-delisting-2020
  title: "PSE CN-2020-0104 (21 Dec 2020): amendments to the Voluntary Delisting Rules (Supplemental Rule 8.1)"
  publisher: "The Philippine Stock Exchange, Inc. (PSE) / Securities and Exchange Commission"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2022/07/Supplemental-Rule-8.1-Amendments-to-the-Voluntary-Delisting-Rules.pdf"
  local_path: pdfs/pse-sr8-1-voluntary-delisting-2020.pdf
  edition: in-force
  amended_through: "2020-12-21"
  note: "Archived by another researcher; scanned. 2023 proposals to amend (CN-2023-0041) not confirmed adopted."
- slug: pse-tpa-2025-0040-globalinks-involuntary-suspension
  title: "PSE TPA-2025-0040: Globalinks Securities & Stocks, Inc. - involuntary suspension (CMIC memorandum 2025-022)"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/TPA-2025-0040.pdf"
  local_path: pdfs/pse-tpa-2025-0040-globalinks-involuntary-suspension.pdf
  edition: historical
  amended_through: "2025-07-09"
  note: "Archived by this researcher (browser User-Agent; %PDF verified); suspension effective 9 Jul 2025 for RBCA capitalisation breaches."
- slug: pse-tpa-2025-0050-mount-peak-involuntary-suspension
  title: "PSE TPA-2025-0050: Mount Peak Securities, Inc. - involuntary suspension (CMIC memorandum 2025-024)"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/TPA-2025-0050.pdf"
  local_path: pdfs/pse-tpa-2025-0050-mount-peak-involuntary-suspension.pdf
  edition: n/a
  amended_through: "2025-08-13"
  note: "Archived by another researcher."
- slug: pse-tpa-2025-0061-globalinks-lifting-of-suspension
  title: "PSE TPA-2025-0061: Globalinks Securities & Stocks, Inc. - lifting of involuntary suspension (CMIC memorandum 2025-032)"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/TPA-2025-0061.pdf"
  local_path: pdfs/pse-tpa-2025-0061-globalinks-lifting-of-suspension.pdf
  edition: historical
  amended_through: "2025-10-14"
  note: "Archived by this researcher (browser User-Agent; %PDF verified); suspension lifted 14 Oct 2025."
- slug: pse-tpa-2026-0002-dynamic-threshold-review
  title: "PSE TPA-2026-0002: Dynamic Threshold semi-annual review (effective 2 Feb 2026)"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2026/01/TPA-2026-0002.pdf"
  local_path: pdfs/pse-tpa-2026-0002-dynamic-threshold-review.pdf
  edition: superseded
  amended_through: "2026-01-19"
  note: ""
- slug: pse-tpa-2026-0035-benjamin-co-ca-involuntary-suspension
  title: "PSE TPA-2026-0035: Benjamin Co Ca & Company, Inc., involuntary suspension (CMIC notice, effective 31 Jul 2026)"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/TPA-2026-0035.pdf"
  local_path: pdfs/pse-tpa-2026-0035-benjamin-co-ca-involuntary-suspension.pdf
  edition: historical
  amended_through: "2026-07-31"
  note: "Archived by another researcher."
- slug: pse-tpa-2026-0036-dynamic-threshold-review
  title: "PSE TPA-2026-0036: Dynamic Threshold semi-annual review (effective 7 Aug 2026)"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/TPA-2026-0036.pdf"
  local_path: pdfs/pse-tpa-2026-0036-dynamic-threshold-review.pdf
  edition: in-force
  amended_through: "2026-08-03"
  note: "Archived by another researcher."
- slug: pse-trading-day-advisory-2026-11-16-18
  title: "PSE CN-No. 2026-0044: Trading Day Advisory (16-18 Nov 2026), placeholder pending a final advisory"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2026/09/November-16-18_Trading-Days_hold_updated.pdf"
  local_path: pdfs/pse-trading-day-advisory-2026-11-16-18.pdf
  edition: in-force
  amended_through: "2026-09-25"
  note: "Archived by another researcher."
- slug: ra-10963-train
  title: "Republic Act No. 10963, Tax Reform for Acceleration and Inclusion (TRAIN)"
  publisher: "Congress of the Philippines"
  type: pdf
  canonical_url: "https://lawphil.net/statutes/repacts/ra2017/ra_10963_2017.html"
  local_path: pdfs/ra-10963-train.pdf
  edition: historical
  amended_through: "2017-12-19"
  note: "Scanned two-up pages; Sec. 39 (NIRC Sec. 127, 6/10 of 1%) on PDF p24; Sec. 87 effectivity on p54. Original download URL not recorded."
- slug: ra-11494-bayanihan-ii
  title: "Republic Act No. 11494, Bayanihan to Recover as One Act (Sec. 6 repeals the IPO tax)"
  publisher: "Congress of the Philippines"
  type: pdf
  canonical_url: "https://lawphil.net/statutes/repacts/ra2020/pdf/ra_11494_2020.pdf"
  local_path: pdfs/ra-11494-bayanihan-ii.pdf
  edition: in-force
  amended_through: "2020-09-11"
  note: "Archived by another researcher; scanned two-up pages: Sec. 6 on PDF p20, Sec. 18 (effectivity on publication) and approval date on p25."
- slug: ra-11534-create
  title: "Republic Act No. 11534, Corporate Recovery and Tax Incentives for Enterprises (CREATE) Act"
  publisher: "Congress of the Philippines"
  type: pdf
  canonical_url: "https://lawphil.net/statutes/repacts/ra2021/ra_11534_2021.html"
  local_path: pdfs/ra-11534-create.pdf
  edition: in-force
  amended_through: "2021-03-26"
  note: "Effective 15 days after publication (p77). Original download URL not recorded."
- slug: ra-11647-foreign-investments-act-amendments
  title: "Republic Act No. 11647, amending the Foreign Investments Act of 1991"
  publisher: "Congress of the Philippines"
  type: pdf
  canonical_url: "https://lawphil.net/statutes/repacts/ra2022/ra_11647_2022.html"
  local_path: pdfs/ra-11647-foreign-investments-act-amendments.pdf
  edition: in-force
  amended_through: "2022-03-02"
  note: "Scanned. Effective 15 days after publication. Original download URL not recorded."
- slug: ra-11659-public-service-act-amendments
  title: "Republic Act No. 11659, amending the Public Service Act (Commonwealth Act 146)"
  publisher: "Congress of the Philippines"
  type: pdf
  canonical_url: "https://lawphil.net/statutes/repacts/ra2022/ra_11659_2022.html"
  local_path: pdfs/ra-11659-public-service-act-amendments.pdf
  edition: in-force
  amended_through: "2022-03-21"
  note: "Scanned two-up pages; 'public utility' definition on PDF p4. Original download URL not recorded."
- slug: ra-12214-cmepa
  title: "Republic Act No. 12214, Capital Markets Efficiency Promotion Act (CMEPA)"
  publisher: "Congress of the Philippines"
  type: pdf
  canonical_url: "https://lawphil.net/statutes/repacts/ra2025/ra_12214_2025.html"
  local_path: pdfs/ra-12214-cmepa.pdf
  edition: in-force
  amended_through: "2025-05-29"
  note: "Archived PDF is an official copy (original download URL not recorded by this researcher); its Sec. 29 reads effective 1 July 2025, unlike the lawphil HTML transcription. Sec. 17 (STT) on p16."
- slug: ra-8424-nirc-1997
  title: "Republic Act No. 8424, National Internal Revenue Code of 1997 (as originally enacted)"
  publisher: "Congress of the Philippines"
  type: pdf
  canonical_url: "https://lawphil.net/statutes/repacts/ra1997/pdf/ra_8424_1997.pdf"
  local_path: pdfs/ra-8424-nirc-1997.pdf
  edition: historical
  amended_through: "1997-12-11"
  note: "Archived by another researcher. Original Sec. 127 (STT 1/2 of 1%; IPO tax 4/2/1%) on PDF p165-166."
- slug: sccp-clearing-house-rules-2018
  title: "Revised Clearinghouse Rules of the Securities Clearing Corporation of the Philippines (revised 13 Mar 2018)"
  publisher: "Securities Clearing Corporation of the Philippines (SCCP)"
  type: pdf
  canonical_url: "https://www.sccp.com.ph/resources/files/rules/SCCP_Revised_Rules_-_Approved_by_the_SEC_031318.pdf"
  local_path: pdfs/sccp-clearing-house-rules-2018.pdf
  edition: superseded
  amended_through: "2018-03-13"
  note: "Archived by another researcher; still the version posted on sccp.com.ph (T+3 wording); superseded in part by SCCP memoranda (T+2, collateral, allocation)."
- slug: sccp-memo-01-0126-eligible-collateral-list
  title: "SCCP Memo 01-0126 (28 Jan 2026): list of securities eligible as collateral (effective 2 Feb 2026)"
  publisher: "Securities Clearing Corporation of the Philippines (SCCP)"
  type: pdf
  canonical_url: "https://www.sccp.com.ph/"
  local_path: pdfs/sccp-memo-01-0126-eligible-collateral-list.pdf
  edition: in-force
  amended_through: "2026-01-28"
  note: "Archived by another researcher; original URL not recorded. A newer list memo 01-0726 (28 Jul 2026) was not archived."
- slug: sccp-memo-01-0324-early-batch-run-effectivity
  title: "SCCP Memo 01-0324: effectivity of the amendment to the Operating Procedures on early commencement of the batch run (SEC approval 9 Jan 2024)"
  publisher: "Securities Clearing Corporation of the Philippines (SCCP)"
  type: pdf
  canonical_url: "https://www.sccp.com.ph/"
  local_path: pdfs/sccp-memo-01-0324-early-batch-run-effectivity.pdf
  edition: in-force
  amended_through: "2024-03-05"
  note: "Archived by another researcher; original URL not recorded."
- slug: sccp-memo-01-0725-ctgf-refund-sec-approval
  title: "SCCP Memo 01-0725: SEC approval of amendments on the refund of contributions to the Clearing and Trade Guaranty Fund"
  publisher: "Securities Clearing Corporation of the Philippines (SCCP)"
  type: pdf
  canonical_url: "https://www.sccp.com.ph/"
  local_path: pdfs/sccp-memo-01-0725-ctgf-refund-sec-approval.pdf
  edition: in-force
  amended_through: "2025-07-08"
  note: "Archived by another researcher; original URL not recorded."
- slug: sccp-memo-02-0125-sec-approval-rules-3-4-5-1-4-6-2-8-7-6
  title: "SCCP Memo 02-0125: SEC approval of amendments to SCCP Rules 3.4, 5.1.4, 6.2.8 and 7.6"
  publisher: "Securities Clearing Corporation of the Philippines (SCCP)"
  type: pdf
  canonical_url: "https://www.sccp.com.ph/"
  local_path: pdfs/sccp-memo-02-0125-sec-approval-rules-3-4-5-1-4-6-2-8-7-6.pdf
  edition: in-force
  amended_through: "2025-01-21"
  note: "Archived by another researcher; original URL not recorded."
- slug: sccp-memo-02-0223-collateral-haircut-rates
  title: "SCCP Memo 02-0223: new eligible securities collateral and haircut rates (SEC approval of Rule 8.1.8 on 13 Dec 2022)"
  publisher: "Securities Clearing Corporation of the Philippines (SCCP)"
  type: pdf
  canonical_url: "https://www.sccp.com.ph/"
  local_path: pdfs/sccp-memo-02-0223-collateral-haircut-rates.pdf
  edition: in-force
  amended_through: "2023-02-10"
  note: "Archived by another researcher; original URL not recorded."
- slug: sccp-memo-03-0324-clearing-member-suspension
  title: "SCCP Memo 03-0324 (22 Mar 2024): suspension of clearing member EquitiWorld Securities"
  publisher: "Securities Clearing Corporation of the Philippines (SCCP)"
  type: pdf
  canonical_url: "https://sccp.com.ph/resources/files/memos/2024/03-0324%20Announcement%20of%20EquitiWorld%20Suspension.pdf"
  local_path: pdfs/sccp-memo-03-0324-clearing-member-suspension.pdf
  edition: historical
  amended_through: "2024-03-22"
  note: "Archived by another researcher."
- slug: sccp-memo-06-0823-sec-approval-t2-amendments
  title: "SCCP Memo 06-0823: SEC approval of T+2-related amendments to SCCP Rules and Operating Procedures"
  publisher: "Securities Clearing Corporation of the Philippines (SCCP)"
  type: pdf
  canonical_url: "https://www.sccp.com.ph/"
  local_path: pdfs/sccp-memo-06-0823-sec-approval-t2-amendments.pdf
  edition: in-force
  amended_through: "2023-08-18"
  note: "Archived by another researcher; original URL not recorded."
- slug: sccp-memo-07-0823-sec-approved-amendments
  title: "SCCP Memo 07-0823: SEC-approved amendments (buy-in/sell-out, MTM collateral haircuts, settlement dates, multiple trade dates)"
  publisher: "Securities Clearing Corporation of the Philippines (SCCP)"
  type: pdf
  canonical_url: "https://www.sccp.com.ph/"
  local_path: pdfs/sccp-memo-07-0823-sec-approved-amendments.pdf
  edition: in-force
  amended_through: "2023-08-23"
  note: "Archived by another researcher; original URL not recorded."
- slug: sec-2015-src-irr
  title: "2015 Implementing Rules and Regulations of the Securities Regulation Code"
  publisher: "Securities and Exchange Commission"
  type: pdf
  canonical_url: "https://www.sec.gov.ph/"
  local_path: pdfs/sec-2015-src-irr.pdf
  edition: in-force
  amended_through: "2015-11-09"
  note: "Archived by another researcher; original URL not recorded (sec.gov.ph blocks automated clients). Rule 24.2-2.5 (uptick rule) on p71."
- slug: sec-2015-src-irr-notice-of-effectivity
  title: "SEC notice: effectivity of the 2015 SRC Rules on 9 November 2015"
  publisher: "Securities and Exchange Commission"
  type: pdf
  canonical_url: "https://appointment.sec.gov.ph/wp-content/uploads/2019/11/2015-SRC-Rules-Notice-of-Effectivity-of-SRC-IRR-Nov-09-2015.pdf"
  local_path: pdfs/sec-2015-src-irr-notice-of-effectivity.pdf
  edition: in-force
  amended_through: "2015-11-05"
  note: "Archived by another researcher."
- slug: sec-mc-1-2020-reit-irr
  title: "SEC Memorandum Circular No. 1 s. 2020: Revised IRR of RA 9856 (REIT Act of 2009)"
  publisher: "Securities and Exchange Commission"
  type: pdf
  canonical_url: "https://www.sec.gov.ph/"
  local_path: pdfs/sec-mc-1-2020-reit-irr.pdf
  edition: in-force
  amended_through: "2020-02-07"
  note: "Effectivity stated on p1 as 7 Feb 2020. Archived by another researcher; original URL not recorded."
- slug: sec-rfq-2026-src-rule-48-1-margin
  title: "SEC notice: proposed amendments to SRC Rule 48.1 (Margin), request for comments"
  publisher: "Securities and Exchange Commission"
  type: pdf
  canonical_url: "https://www.sec.gov.ph/"
  local_path: pdfs/sec-rfq-2026-src-rule-48-1-margin.pdf
  edition: in-force
  amended_through: "2026-08-25"
  note: "Exposure draft (En Banc 25 Aug 2026; comments to 15 Sep 2026); not a final rule. Archived by another researcher; original URL not recorded."
- slug: bworld-2024-10-23-gpdr-derivatives-targets
  title: "BusinessWorld (via Metrobank Wealth Insights): PSE eyes Q1 2025 for GPDR launch, derivatives by 2026"
  publisher: "BusinessWorld / Metrobank Wealth Insights"
  type: web
  canonical_url: "https://wealthinsights.metrobank.com.ph/bworldonline/pse-eyes-q1-2025-for-gpdr-launch-derivatives-by-2026"
  local_path: null
  edition: n/a
  amended_through: "2024-10-23"
  note: "Secondary."
- slug: fow-2024-08-29-derivatives-2026
  title: "FOW: Philippine Stock Exchange plans first derivatives in 2026"
  publisher: "FOW (Informa)"
  type: web
  canonical_url: "https://www.fow.com/insights/3702078-philippine-stock-exchange-plans-first-derivatives-in-2026"
  local_path: null
  edition: n/a
  amended_through: "2024-08-29"
  note: "Secondary; paywalled, headline and teaser only."
- slug: ftse-equity-country-classification-page
  title: "FTSE Russell web page 'Equity Country Classification'"
  publisher: "FTSE Russell (LSEG)"
  type: web
  canonical_url: "https://www.lseg.com/en/ftse-russell/equity-country-classification"
  local_path: null
  edition: n/a
  amended_through: "undated"
  note: "Fetched 6 Oct 2026: the 'Annual Country Classification - Sep 2026' link led to a two-page PDF reading 'Document to follow' (not archived). A sibling note cites ftserussell.com/equity-country-classification for the same page."
- slug: gma-2023-10-20-short-selling-nov-6
  title: "GMA News: PSE to launch short selling program on Nov. 6"
  publisher: "GMA News Online"
  type: web
  canonical_url: "https://www.gmanetwork.com/news/money/companies/885794/pse-to-launch-short-selling-program-on-nov-6/story"
  local_path: null
  edition: n/a
  amended_through: "2023-10-20"
  note: "Secondary; source of '53 eligible securities'."
- slug: kpmg-2026-04-13th-finl
  title: "KPMG Philippines: Special inTAX April 2026 (13th Regular Foreign Investment Negative List)"
  publisher: "KPMG R.G. Manabat"
  type: web
  canonical_url: "https://kpmg.com/ph/en/insights/2026/04/special-intax-april-2026-issue-1-volume-2.html"
  local_path: null
  edition: n/a
  amended_through: "undated"
  note: "Secondary; April 2026 issue."
- slug: ladige-2026-06-msci-mcr
  title: "L'Adige (Business Wire translation): MSCI announces results of the 2026 Market Classification Review"
  publisher: "L'Adige / Business Wire"
  type: web
  canonical_url: "https://www.ladige.it/business-wire/msci-annuncia-i-risultati-della-msci-2026-market-classification-review-ckjig862"
  local_path: null
  edition: n/a
  amended_through: "undated"
  note: "Secondary translation of MSCI's June 2026 release; the Philippines is not mentioned."
- slug: lawphil-eo-65-2018
  title: "Executive Order No. 65 s. 2018, Eleventh Regular Foreign Investment Negative List (HTML)"
  publisher: "Arellano Law Foundation (lawphil.net)"
  type: web
  canonical_url: "https://lawphil.net/executive/execord/eo2018/eo_65_2018.html"
  local_path: null
  edition: superseded
  amended_through: "2018-10-29"
  note: "HTML only; not archived."
- slug: lawphil-ra-12214-2025
  title: "RA 12214 as transcribed on lawphil.net (HTML)"
  publisher: "Arellano Law Foundation (lawphil.net)"
  type: web
  canonical_url: "https://lawphil.net/statutes/repacts/ra2025/ra_12214_2025.html"
  local_path: null
  edition: in-force
  amended_through: "2025-05-29"
  note: "Sec. 29 transcription says effective 15 days after publication; conflicts with the official PDF (see conflict C4). HTML only; not archived."
- slug: newswav-2026-08-msci-ali
  title: "Newswav: Ayala Land dropped from MSCI's PH index"
  publisher: "Newswav"
  type: web
  canonical_url: "https://newswav.com/article/ayala-land-dropped-from-msci-s-ph-index-A2608_BWfgI5"
  local_path: null
  edition: n/a
  amended_through: "2026-08-14"
  note: "Secondary; effective after close 31 Aug 2026."
- slug: philstar-2025-12-24-pds-landbank
  title: "Philippine Star: PSE hikes stake in PDS via acquisition of Landbank shares"
  publisher: "The Philippine Star"
  type: web
  canonical_url: "https://www.philstar.com/business/2025/12/24/2496342/pse-hikes-stake-pds-acquisition-landbank-shares"
  local_path: null
  edition: n/a
  amended_through: "2025-12-24"
  note: "Secondary."
- slug: philstar-2026-06-10-sec-msla
  title: "Philippine Star: SEC streamlines securities borrowing, lending framework"
  publisher: "The Philippine Star"
  type: web
  canonical_url: "https://www.philstar.com/business/2026/06/10/2534005/sec-streamlines-securities-borrowing-lending-framework"
  local_path: null
  edition: n/a
  amended_through: "2026-06-10"
  note: "Secondary; press report date. PSE memo CN-2026-0025 gives the SEC approval date as 15 May 2026."
- slug: philstar-2026-07-17-sec-accomplishments
  title: "Philippine Star: SEC cites accomplishments"
  publisher: "The Philippine Star"
  type: web
  canonical_url: "https://www.philstar.com/business/2026/07/17/2542599/sec-cites-accomplishments"
  local_path: null
  edition: n/a
  amended_through: "2026-07-17"
  note: "Secondary; source for the Capital Market Master Plan with ADB."
- slug: pse-listed-company-directory-frame
  title: "PSE Listed Company Directory (frames.pse.com.ph/listedCompany)"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: web
  canonical_url: "https://frames.pse.com.ph/listedCompany"
  local_path: null
  edition: n/a
  amended_through: "2026-10-06"
  note: "Retrieved 6 Oct 2026 by another researcher; security types, boards and listing dates."
- slug: pse-pr-cmepa-day1-2025-07-01
  title: "PSE press release: PBBM leads PSE bell ringing to welcome Day 1 of CMEPA law"
  publisher: "The Philippine Stock Exchange, Inc. (PSE) corporate site"
  type: web
  canonical_url: "https://corporate.pse.com.ph/pbbm-leads-pse-bell-ringing-to-welcome-day-1-of-cmepa-law"
  local_path: null
  edition: n/a
  amended_through: "2025-07-01"
  note: ""
- slug: pse-pr-gcash-gstocks-2022-09-21
  title: "PSE press release: GCash introduces PH stock trading with AB Capital, PSE"
  publisher: "The Philippine Stock Exchange, Inc. (PSE) corporate site"
  type: web
  canonical_url: "https://corporate.pse.com.ph/gcash-introduces-ph-stock-trading-with-ab-capital-pse"
  local_path: null
  edition: n/a
  amended_through: "2022-09-21"
  note: ""
- slug: pse-pr-lower-static-threshold-2020
  title: "PSE press release: PSE reduces lower static threshold of share prices"
  publisher: "The Philippine Stock Exchange, Inc. (PSE) corporate site"
  type: web
  canonical_url: "https://corporate.pse.com.ph/pse-reduces-lower-static-threshold-of-share-prices"
  local_path: null
  edition: n/a
  amended_through: "2020-04-16"
  note: "Page date 16 Apr 2020 conflicts with circular date 21 Mar 2020."
- slug: pse-pr-market-making-2026-06-04
  title: "PSE press release: PSE releases amendments to market making rules for public comment"
  publisher: "The Philippine Stock Exchange, Inc. (PSE) corporate site"
  type: web
  canonical_url: "https://corporate.pse.com.ph/pse-releases-amendments-to-market-making-rules-for-public-comment"
  local_path: null
  edition: n/a
  amended_through: "2026-06-04"
  note: ""
- slug: pse-pr-nasdaq-eqlipse-2025-05-22
  title: "PSE/Nasdaq press release: PSE adopts Nasdaq Eqlipse Trading"
  publisher: "The Philippine Stock Exchange, Inc. (PSE) corporate site"
  type: web
  canonical_url: "https://corporate.pse.com.ph/philippine-stock-exchange-adopts-nasdaq-eqlipse-trading-to-enhance-market-infrastructure"
  local_path: null
  edition: n/a
  amended_through: "2025-05-22"
  note: ""
- slug: pse-pr-new-indices-2022-03-28
  title: "PSE press release: PSE launches two new indices"
  publisher: "The Philippine Stock Exchange, Inc. (PSE) corporate site"
  type: web
  canonical_url: "https://corporate.pse.com.ph/pse-launches-two-new-indices"
  local_path: null
  edition: n/a
  amended_through: "2022-03-28"
  note: ""
- slug: pse-pr-pds-acquisition-2024-12-26
  title: "PSE press release: PSE to acquire 61.92 percent of PDS for P2.32B"
  publisher: "The Philippine Stock Exchange, Inc. (PSE) corporate site"
  type: web
  canonical_url: "https://corporate.pse.com.ph/pse-to-acquire-61-92-percent-of-pds-for-p2-32b"
  local_path: null
  edition: n/a
  amended_through: "2024-12-26"
  note: ""
- slug: pse-pr-regulatory-reforms-2026-06-15
  title: "PSE press release: PSE to introduce additional regulatory reforms (ETF rules, negotiated trades, SBL directed pooled lending)"
  publisher: "The Philippine Stock Exchange, Inc. (PSE) corporate site"
  type: web
  canonical_url: "https://corporate.pse.com.ph/pse-to-introduce-additional-regulatory-reforms"
  local_path: null
  edition: n/a
  amended_through: "2026-06-15"
  note: ""
- slug: pse-pr-sccp-new-clearing-system-2023-03-31
  title: "PSE press release: SCCP migrates to new clearing and settlement technology"
  publisher: "The Philippine Stock Exchange, Inc. (PSE) corporate site"
  type: web
  canonical_url: "https://corporate.pse.com.ph/sccp-migrates-to-new-clearing-and-settlement-technology"
  local_path: null
  edition: n/a
  amended_through: "2023-03-31"
  note: ""
- slug: pse-pr-short-selling-effectivity-2023-10-02
  title: "PSE press release: PSE announces effectivity of short selling guidelines, other relevant SBL developments"
  publisher: "The Philippine Stock Exchange, Inc. (PSE) corporate site"
  type: web
  canonical_url: "https://corporate.pse.com.ph/pse-announces-effectivity-of-short-selling-guidelines-other-relevant-sbl-developments"
  local_path: null
  edition: n/a
  amended_through: "2023-10-02"
  note: ""
- slug: pse-pr-trading-floor-closed-2022-06-24
  title: "PSE press release: PSE closes trading floor permanently"
  publisher: "The Philippine Stock Exchange, Inc. (PSE) corporate site"
  type: web
  canonical_url: "https://corporate.pse.com.ph/pse-closes-trading-floor-permanently"
  local_path: null
  edition: n/a
  amended_through: "2022-06-24"
  note: ""
- slug: pse-pr-vwap-2024-02-16
  title: "PSE press release: PSE to implement VWAP trading on March 1"
  publisher: "The Philippine Stock Exchange, Inc. (PSE) corporate site"
  type: web
  canonical_url: "https://corporate.pse.com.ph/pse-to-implement-vwap-trading-on-march-1"
  local_path: null
  edition: n/a
  amended_through: "2024-02-16"
  note: ""
- slug: pse-press-agi-warrants
  title: "PSE press release: Alliance Global Group, Inc. marks warrants listing (22 Dec 2025)"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: web
  canonical_url: "https://www.pse.com.ph/alliance-global-group-inc-marks-warrants-listing/"
  local_path: null
  edition: n/a
  amended_through: "2025-12-22"
  note: "AGIW listed Fri 19 Dec 2025; 2.2bn warrants; PHP12 exercise price; five-year exercise period; PHP1.1bn gross proceeds."
- slug: pse-press-fy2024-results
  title: "PSE press release: PSE posts P1.2B net income in 2024 (3 Mar 2025)"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: web
  canonical_url: "https://www.pse.com.ph/pse-posts-p1-2b-net-income-in-2024/"
  local_path: null
  edition: n/a
  amended_through: "2025-03-03"
  note: "PSE's PDS stake 78.33% as of 24 Feb 2025 (from 20.98%)."
- slug: pse-press-mynt-ipo-approval
  title: "PSE press release: PSE clears Mynt, Inc. for IPO (18 Sep 2026)"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: web
  canonical_url: "https://www.pse.com.ph/pse-clears-mynt-inc-for-ipo/"
  local_path: null
  edition: n/a
  amended_through: "2026-09-18"
  note: "Offer period 6-12 Oct 2026; price set 1 Oct; tentative listing 20 Oct 2026; symbol GCASH."
- slug: pse-press-q1-2025-results
  title: "PSE press release: PSE net earnings rise 5 percent in Q1 2025 (16 May 2025)"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: web
  canonical_url: "https://www.pse.com.ph/pse-net-earnings-rise-5-percent-in-q1-2025/"
  local_path: null
  edition: n/a
  amended_through: "2025-05-16"
  note: "PSE's PDS stake 79.9% at end-Mar 2025 and 91.6% as of 15 May 2025."
- slug: pse-sec-frames-snapshot
  title: "PSE security information frames (frames.pse.com.ph/security/<symbol>), snapshot of 6 Oct 2026"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: dataset
  canonical_url: "https://frames.pse.com.ph/security/FMETF"
  local_path: null
  edition: in-force
  amended_through: "2026-10-06"
  note: "Status, last price and board lot per security; fetched 6 Oct 2026 by another researcher."
- slug: pse-web-announcements-archive
  title: "PSE web page 'News and Announcement Archive' (circulars index)"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: web
  canonical_url: "https://www.pse.com.ph/news-and-announcement-archive/"
  local_path: null
  edition: n/a
  amended_through: "undated"
  note: "Fetched 6 Oct 2026; date column contains typos; the second line of each entry is the posting date."
- slug: pse-web-etf-page
  title: "PSE web page 'Exchange Traded Fund' (overview and ETF participants)"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: web
  canonical_url: "https://www.pse.com.ph/exchange-traded-fund/"
  local_path: null
  edition: n/a
  amended_through: "undated"
  note: "Fetched 6 Oct 2026; the only ETF linked is FMETF (First Metro Philippine Equity ETF)."
- slug: pse-web-investing-at-pse
  title: "PSE web page 'Investing at PSE' (fees, taxes, trading hours, FAQ)"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: web
  canonical_url: "https://www.pse.com.ph/investing-at-pse/"
  local_path: null
  edition: n/a
  amended_through: "undated"
  note: "Fetched 6 Oct 2026; contains current and stale tables (see conflict C2)."
- slug: pse-web-new-listings
  title: "PSE web page 'New Listings / IPO'"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: web
  canonical_url: "https://www.pse.com.ph/new-listings-ipo/"
  local_path: null
  edition: n/a
  amended_through: "undated"
  note: "Fetched 6 Oct 2026; AREIT listing 13 Aug 2020."
- slug: pse-web-nte-page
  title: "PSE web page 'PSE Trading Engine 2026' (overview, system features, specifications, updates)"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: web
  canonical_url: "https://www.pse.com.ph/pse-new-trading-engine/"
  local_path: null
  edition: n/a
  amended_through: "undated"
  note: "Fetched 6 Oct 2026; tabs ?tab=system-features, ?tab=fix-gateway, ?tab=market-data-feed, ?tab=updates, ?tab=faqs."
- slug: pse-web-reg-trading-participants
  title: "PSE web page 'Regulation: Trading Participants' (rules and amendment list)"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: web
  canonical_url: "https://www.pse.com.ph/regulation-trading-participants/"
  local_path: null
  edition: n/a
  amended_through: "undated"
  note: "Fetched 6 Oct 2026; lists amendments to the Revised Trading Rules."
- slug: pse-web-sbl-short-selling
  title: "PSE web page 'SBL and Short Selling' (FAQ)"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: web
  canonical_url: "https://www.pse.com.ph/sbl-short-selling/"
  local_path: null
  edition: n/a
  amended_through: "undated"
  note: "Fetched 6 Oct 2026; contains one stale eligibility FAQ."
- slug: tribune-pse-eases-float-2025
  title: "Daily Tribune: PSE eases public float level to 15% (19 Mar 2025)"
  publisher: "Daily Tribune"
  type: web
  canonical_url: "https://tribune.net.ph/2025/03/19/pse-eases-public-float-level-to-15"
  local_path: null
  edition: n/a
  amended_through: "2025-03-19"
  note: "Secondary; quotes PSE's CEO on the SEC-approved temporary cut in the IPO public float from 20% to 15%; no PSE circular found."
```
