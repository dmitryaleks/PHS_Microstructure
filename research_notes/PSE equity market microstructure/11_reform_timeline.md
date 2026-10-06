# PSE equity market reform timeline, 2018 to 6 October 2026 (currency check for Chapter 17)

**Status of this file:** v2, 6 Oct 2026. Revision log: v1 = first complete draft from the material gathered first (chronology, pipeline, conflicts, execution implications, source catalog); v2 = adds the primary text of the 13th negative list, the 2024 and 2025 president's reports (slippage record, board-lot filing, PDTC lending-agent approval), broker-failure and delisting events, the 6 Oct 2026 EDGE outage, the 2023 MPO consultation, BSP foreign-investment notices, a version-gating table, and a products row; every cited slug and page number was machine-checked against kb/pdfs.

**As-of date:** 6 October 2026. **Evidence cut-off:** PSE circular/announcement index and New Trading Engine (NTE) pages fetched 6 Oct 2026 (index re-fetched about 14:30 local). The newest entries are three EDGE-outage notices posted 6 Oct 2026, then TPA-2026-0041 (2 Oct) and PSE's relay of an SEC request for comments on broker-dealer capital (1 Oct); nothing was posted 3-5 Oct. SEC, BIR and Official Gazette sites were blocked or unavailable, so SEC/BIR items after 17 Aug 2026 are known only through PSE's relays and the press. The shared WebSearch quota (200 calls) ran out mid-task, so the last third of discovery relied on PSE's own indexes and direct fetches; news cross-checks are fewer than planned.

**Citation convention.** `[^slug:N]` = physical page N (PDF-viewer page, not the printed folio) of kb/pdfs/slug.pdf. `[^slug]` = a web page or a whole document. Every slug is defined in the "Source catalog" at the end, with URL and edition. Many PSE PDFs are scanned images; those were read from rendered page images.

**Evidence labels.** P = primary (statute, regulator, PSE/SCCP/PDS/BIR/SEC document). S = secondary only (press, law-firm or consultancy note; no primary retrieved). I = my inference from the cited facts.

**Status vocabulary.** In force; Superseded (was in force, replaced by a later row); Approved, not yet effective (decided/approved, with a future effective or go-live date); Proposed (consultation, exposure draft, or filed with the regulator and awaiting action); Abandoned (proposed, never adopted, replaced by a different proposal); Historical (one-off event, no continuing rule).

---

## 1. Chronology of rule and structural changes, 2018 to 6 October 2026

### Takeaway
The PSE order book's static parameters moved little in 2018-2026: the 15-band board-lot/tick table is the same one that appears as "existing" in PSE's December 2025 consultation, and PSE's web list of amendments to the Revised Trading Rules shows nothing between 2013 and the 2020 COVID measures, then only VWAP and minimum-commission items in 2024 (the list omits the 2025 halt/typhoon amendments, so it is not exhaustive). What changed was (1) cost and tax: STT 0.5% to 0.6% on 1 Jan 2018 (TRAIN) and 0.6% to 0.1% on 1 Jul 2025 (CMEPA), minimum commission removed 18 Apr 2024; (2) session design: shortened hours Mar 2020-Dec 2021, a new 09:30-15:00 schedule on 6 Dec 2021, and a Closing VWAP session that moved the close to 15:15 on 1 Mar 2024; (3) risk controls: lower static floor -50% to -30% (24 Mar 2020), three-level index circuit breaker (4 May 2020), ">50% of ADTV" halt trigger and typhoon rule (20 Aug 2025); (4) post-trade: SCCP new clearing system (27 Mar 2023) and T+3 to T+2 (24 Aug 2023); (5) shorting: guidelines effective 2 Oct 2023, go-live 6 Nov 2023; (6) ownership and benchmarks: index free-float floor 12% to 15% to 20%, MidCap/DivY indices, tiered minimum public ownership (11 Aug 2026), Class A/B declassification, RA 11647/11659 and the 12th/13th negative lists; (7) corporate: PSE took control of PDS Group in Dec 2024. The biggest microstructure change (Nasdaq Eqlipse engine, one-share lots, negotiated trades) is scheduled for 23 Nov 2026 and is NOT live.

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
| Minimum public ownership | IPO: 33% (market cap up to PHP500M), 25% (to PHP1bn, offer at least PHP165M), 20% (to PHP50bn, offer at least PHP250M), 15% (above PHP50bn, offer at least PHP10bn); REIT 33.33%; maintenance 20% (15% above PHP50bn); possible 12% floor for PHP200bn+ listings; pre-2017 listings 10% and 2017-2026 listings 20% grandfathered | 11 Aug 2026 | none | [^pse-memo-2026-08-11-mpo-rule-effectivity:2-4] | P |
| Engine, clearing, floor | PSEtrade XTS (Nasdaq X-stream) since 22 Jun 2015; SCCP on LSEG Millennium since 27 Mar 2023; floorless trading since 27 Jun 2022 | as stated | Nasdaq Eqlipse NTE target 23 Nov 2026 | [^pse-annual-report-2015:42][^pse-pr-sccp-new-clearing-system-2023-03-31][^pse-pr-trading-floor-closed-2022-06-24] | P |
| Block sale / crosses / VWAP | Regular block sale at least PHP20M within +/-5% of reference price; special block sale at least PHP50M; crosses within best bid/offer; Closing VWAP trades at least PHP500,000, single TP, executed only 15 min after run-off | 1 Mar 2024 (VWAP) | Negotiated Trades (proposed) | [^pse-cn-2026-0031-negotiated-trades:3][^pse-approved-rules-vwap-trading-2024:7] | P |
| Products | Common stocks (Main and SME boards), dollar-denominated securities, REITs (8 listed since AREIT on 13 Aug 2020; trading restricted to PSE-"eligible" brokers), one ETF (FMETF), preferred shares. Not available: derivatives, GPDRs, structured warrants, market-maker programmes beyond ETFs | REITs 2020; others unchanged | GPDR, structured warrants, index futures, ETF rule changes (all Proposed, Section 2) | [^pse-web-new-listings][^pse-cn-2020-0066-reit-broker-eligibility:1-2][^pse-web-etf-page][^gma-2023-10-20-short-selling-nov-6][^pse-analyst-briefing-1h-2026:9-10] | P/S |
| Foreign ownership law | 13th Regular Foreign Investment Negative List (EO 113, signed 13 Apr 2026; effective 15 days after publication, reported as 1 or 2 May 2026): no foreign equity in mass media/internet business, corporate practice of architecture, cooperatives, private security, small-scale mining; up to 25% private recruitment and defense construction; 30% advertising; 40% for public utilities (six categories), natural resources (renewables fully open), private land, retail trade with paid-up capital under PHP25M, educational institutions, condominiums; telecom operation 100% with reciprocity, 50% without. RA 11659 limits "public utility" to six categories; RA 11647 amends the Foreign Investments Act | 2022 statutes; 13th list May 2026 | none | [^eo-113-2026-13th-finl:1-5][^ra-11659-public-service-act-amendments:4][^ra-11659-public-service-act-amendments:14][^ra-11647-foreign-investments-act-amendments:8][^kpmg-2026-04-13th-finl] | P (effective date S) |
| Benchmarks | MSCI Philippines Index has 9 constituents (30 Sep 2026); FTSE classifies the Philippines "Secondary emerging" (Sep 2026 ground rules); MSCI 2026 market classification announcement did not mention the Philippines | Aug-Sep 2026 | MSCI/FTSE reviews (dates not retrieved) | [^msci-philippines-index-factsheet-2026-09:1][^ftse-geis-ground-rules-2026-09:45][^ladige-2026-06-msci-mcr] | P/S |

#### 1B. Dated chronology (effective date first; implementing document in the Sources column)

**B0. Pre-window baseline (state on 1 Jan 2018, for before/after comparisons)**

| ID | Date | Area | State | Status (6 Oct 2026) | Sources | Ev |
|---|---|---|---|---|---|---|
| B0.1 | 2013-11-04 | Session timetable | 09:00 pre-open; 09:30 open; 12:00 recess; 13:30 resume; 15:15 pre-close (auction 15:15-15:18, no-cancel 15:18-15:20); 15:20 run-off/trading-at-last; 15:30 close. Pre-close lengthened from 3 to 5 min (SEC approval 26 Sep 2013); the 2012 timetable (effective 2 Jan 2012) had pre-close 15:17 | Superseded (R2.2, R3.3) | [^pse-memo-extended-pre-close-implementation-2013:1][^pse-memo-pre-close-schedule-2013:1][^pse-memo-new-trading-hours-2011:1] | P |
| B0.2 | 2015-06-22 | Engine | Migration to PSEtrade XTS (Nasdaq X-stream) | In force until NTE | [^pse-annual-report-2015:42] | P |
| B0.3 | to 2023-08-23 | Settlement | T+3 | Superseded (R4.4) | [^pse-cn-2023-0031-t2-settlement:1] | P |
| B0.4 | to 2017-12-31 | STT | One-half of 1% (0.5%) of gross selling price | Superseded (R1.1) | [^pse-cn-2017-0082-stt-increase-advisory:1] | P |
| B0.5 | to 2020-03-23 | Price limits | Static band +50% / -50%; single circuit breaker (PSEi -10% = 15-minute halt, an offshoot of the 2008 crisis) | Superseded (R2.3, R2.4) | [^pse-cn-2020-0028:1][^pse-cn-2020-0044:1] | P |
| B0.6 | to 2018-02 | Index policy | PSEi/sector-index free-float floor 12%; recompositions in March and September | Superseded (R1.2) | [^pse-cn-2018-0013-index-policy-revision-2018:1] | P |
| B0.7 | pre-2018 | Board lot / tick | Same 15-band table as the "existing" table in the Dec 2025 consultation | In force | [^pse-cn-2025-0046-board-lot-trading-at-last:4] | P |

**B1. 2018-2019**

| ID | Effective date | Area | Change (before to after) | Status | Sources | Ev |
|---|---|---|---|---|---|---|
| R1.1 | 2018-01-01 | Tax (RA 10963 TRAIN) | Stock transaction tax on listed shares 0.5% to 0.6% (6/10 of 1%) of gross selling price, seller-paid. TRAIN approved 19 Dec 2017; PSE advisories 26 and 29 Dec 2017. BIR forms and eFPS were not updated at start (RMC 2-2018) | Superseded 1 Jul 2025 (R6.4) | [^ra-10963-train:24][^ra-10963-train:54][^pse-cn-2017-0082-stt-increase-advisory:1][^pse-cn-2017-0084-stt-increase-effectivity:1][^pse-cn-2018-0003-train-transition:1-2] | P |
| R1.2 | 2018-02-12 memo; applied in the recomposition effective 2018-02-19 | PSEi methodology | Free-float floor for PSEi (and sector indices) 12% to 15%; recomposition months March/September to February/August; financial criteria may be used for screening | Superseded for the float floor (R3.2) | [^pse-cn-2018-0013-index-policy-revision-2018:1][^pse-cn-2018-0014-index-recomposition-2018-02:1][^pse-index-policy-feb2018:5-6] | P |
| R1.3 | 2018-02 | Venue | HQ moves to PSE Tower (BGC); one unified trading floor replaces separate Makati and Pasig floors | Superseded (floor closed R3.9) | [^pse-pr-trading-floor-closed-2022-06-24] | P |
| R1.4 | 2018-04-10 (proposal) | Trading days | Proposed rule that PSE stays open on special non-working days in NCR and on government-only suspension days, with SCCP/CMIC "trading without settlement" guidelines; comments to 25 Apr 2018. Outcome not found | Proposed (adoption not verified) | [^pse-cn-2018-0023-trading-without-settlement-proposal:1] | P (proposal); outcome unknown |
| R1.5 | 2018-06-05 SEC approval; PSE memo 2018-06-22 | Short selling | SEC approves PSE Guidelines for Short Selling Transactions (eligible: PSEi members and ETFs; short-interest ratio at or below 10%); effectivity left "in due course" and in fact took until 2 Oct 2023 | Superseded (R4.7, R4.9) | [^pse-cn-2018-0035-short-selling-guidelines-sec-approved:1-2] | P |
| R1.6 | 2018-10-29 (signed) | Foreign ownership | EO 65: 11th Regular Foreign Investment Negative List | Superseded (R3.10) | [^lawphil-eo-65-2018] | P |
| R1.7 | 2019-01-22/23 | Short selling | Guidelines amended: short orders barred only in pre-open and pre-close (previously also run-off), to match system configuration and SRC Rule 40.3.3 | Incorporated in Oct 2023 text | [^pse-cn-2019-0004-short-selling-guidelines-amendment:1] | P |
| R1.8 | 2019-02-05 BSP Circular 1030; PSE notice 2019-07-08 | Foreign investment access | BSP liberalised its FX rules: exchange-traded funds added to the instruments eligible for registered inward foreign investment (repatriation of capital and income through the banking system) | In force | [^pse-cn-2019-0037-foreign-investment-etf:1] | P |

**B2. 2020**

| ID | Effective date | Area | Change (before to after) | Status | Sources | Ev |
|---|---|---|---|---|---|---|
| R2.1 | 2020-02-07 | REIT regime | SEC approves PSE Amended REIT Listing Rules (effective immediately); SEC REIT Rules (MC 1-2020) effective the same date | In force | [^pse-cn-2020-0005-amended-reit-listing-rules:1][^sec-mc-1-2020-reit-irr:1] | P |
| R2.2 | 2020-03-16 to 2020-03-19 | Session timetable | Shortened hours announced 15 Mar (16 Mar: 09:00 pre-open, 09:30 open, 12:45 pre-close, 12:50 run-off, 13:00 close); full suspension of trading and clearing from 17 Mar (ECQ); resumption Thu 19 Mar with 09:00/09:30/12:45/12:50/13:00 and trading floor closed (offsite trading). Extended 30 Apr, 15 May, then "until further notice" | Superseded 6 Dec 2021 (R3.3) | [^pse-cn-2020-0017:1][^pse-cn-2020-0021:1][^pse-cn-2020-0025-resumption-of-trading:1] | P |
| R2.3 | 2020-03-24 | Price limit | Lower static threshold 50% to 30% below reference price (SEC approval 20 Mar 2020); upper stays +50% | In force | [^pse-cn-2020-0028:1-2][^pse-pr-lower-static-threshold-2020] | P |
| R2.4 | 2020-05-04 | Circuit breaker | Single trigger (PSEi -10% = 15-minute halt) replaced by three levels: -10% / -15% / -20% = 15 / 30 / 60 minutes; each level once per day; level cut-off times defined against the then 15:15 pre-close (L1 until 14:55, L2 until 14:40, L3 until 14:10; shortened schedule 12:25 / 12:10 / 11:40). SEC approved 20 Mar 2020 | In force | [^pse-cn-2020-0044:1-4] | P |
| R2.5 | 2020-05-26 PSE notice | Foreign investment access | BSP confirms that non-resident investments in REIT securities (onshore-listed equity) can be registered for repatriation of capital and earnings | In force | [^pse-cn-2020-0052-nonresident-reit-investment:1] | P |
| R2.6 | 2020-06-01 | Floor and hours | GCQ in Metro Manila: trading floor reopens with health protocols; shortened hours continue | Superseded (R3.3, R3.9) | [^pse-cn-2020-0051-gcq-floor-reopening:1] | P |
| R2.7 | 2020-07-15 | REIT trading access | Only "eligible" TPs (REIT training attended, operational-readiness certification) may trade REIT shares; IPO allocations 20% brokers / 10% local small investors | In force (PSE REIT page still hosts the forms) | [^pse-cn-2020-0066-reit-broker-eligibility:1-2] | P |
| R2.8 | 2020-08-03 | MPO | SEC-approved PSE guidelines: IPO offer 33% or PHP50M (market cap to PHP500M), 25% or PHP100M (to PHP1bn), 20% or PHP250M (above PHP1bn); maintain at least 20%; listing by introduction and backdoor listing at least 20% | Superseded 11 Aug 2026 (R7.13) | [^pse-cn-2020-0076-mpo-initial-backdoor-listing:1] | P |
| R2.9 | 2020-08-13 | Products | First REIT (AREIT) lists on the Main Board; PSE's list of REIT listings now shows AREIT, DDMPR, FILRT, MREIT, RCR, CREIT, VREIT, PREIT | Historical | [^pse-web-new-listings] | P |

**B3. 2021-2022**

| ID | Effective date | Area | Change (before to after) | Status | Sources | Ev |
|---|---|---|---|---|---|---|
| R3.1 | 2021-03-26 approved (RA 11534 CREATE) | Tax | Corporate income tax 30% to 25% from 1 Jul 2020 (20% for small firms); non-resident foreign corporation income tax 30% to 25% from 1 Jan 2021; final tax on non-resident foreign corporation dividends 15% only if the home country credits tax, else 25%. Act effective 15 days after publication (secondary: 11 Apr 2021) | In force | [^ra-11534-create:6][^ra-11534-create:11][^ra-11534-create:77] | P (11 Apr date: S/I) |
| R3.2 | 2021-08-05 memo; 2021-08-16 | PSEi methodology | Float floor 15% to 20% (first applied at the Dec 2022 review, i.e. the Feb 2023 recomposition); early-inclusion provision; PSEi insertion if ranked 25th or higher and removal if 36th or lower by full market cap | In force (partly replaced at the Feb 2027 rebalance, P13) | [^pse-cn-2021-0046-index-policy-revision-2021:1] | P |
| R3.3 | 2021-12-06 | Session timetable | New full-day schedule: 09:00 pre-open, 09:30 open, 12:00 recess, 13:00 resume, 14:45 pre-close, 14:50 run-off, 15:00 close. PSE calls it the "pre-pandemic" schedule, but the pre-March-2020 schedule resumed at 13:30 and closed at 15:30 (see conflicts C1) | Superseded 1 Mar 2024 for the close time (R5.3) | [^pse-cn-2021-0059:1] | P |
| R3.4 | 2022-01-04 | Incident | Trading cancelled for the day: failure to connect the Nasdaq trading engine and the Flextrade front-end (43 of 125 TPs could not connect) | Historical | [^pse-cn-2022-0001-delay-market-opening:1][^pse-cn-2022-0002-cancellation-of-trading-2022-01-04:1] | P |
| R3.5 | 2022-01-14 to 2022-02-28 | Session timetable | Omicron shortened schedule: 09:00 pre-open, 09:15 no-cancel, 09:30 open, 12:45 pre-close, 12:48 no-cancel, 12:50 run-off, 13:00 close (to 31 Jan; run to 28 Feb is implied by R3.6) | Historical | [^pse-cn-2022-0004:1][^pse-cn-2022-0009-trading-schedule-mar-2022:1] | P/I |
| R3.6 | 2022-03-01 | Session timetable | Full-day schedule restored with 09:15 and 14:48 no-cancel phases listed | Superseded 1 Mar 2024 (close) | [^pse-cn-2022-0009-trading-schedule-mar-2022:1] | P |
| R3.7 | 2022-03-02 and 2022-03-21 approved | Foreign ownership | RA 11647 amends the Foreign Investments Act; RA 11659 amends the Public Service Act: "public utility" (60/40 Filipino ownership) limited to six categories (electricity distribution, electricity transmission, petroleum pipelines, water and sewerage pipelines, seaports, public utility vehicles); Sec. 34 amends the foreign-ownership limits in the laws covering BOT projects, domestic shipping, civil aviation, toll roads, transport network vehicles and public telecommunications (RA 7925), so telecoms, airlines, shipping and toll operators are no longer constitutional "public utilities". Both Acts effective 15 days after publication | In force | [^ra-11647-foreign-investments-act-amendments:8][^ra-11659-public-service-act-amendments:4][^ra-11659-public-service-act-amendments:14][^ra-11659-public-service-act-amendments:15] | P |
| R3.8 | 2022-03-28 | Indices | PSE MidCap and PSE Dividend Yield indices launched (20 members each; base 1,000 at 30 Dec 2010; float floor 15% at launch) | In force | [^pse-cn-2022-0013-launch-midcap-divy-indices:1-3][^pse-pr-new-indices-2022-03-28] | P |
| R3.9 | 2022-06-24 last floor day; floorless from 2022-06-27 | Venue | Trading floor closed permanently (only 29 of 85 booth-leasing TPs renewed) | In force | [^pse-pr-trading-floor-closed-2022-06-24] | P |
| R3.10 | 2022-06-27 signed | Foreign ownership | EO 175: 12th Regular Foreign Investment Negative List (replaced the 11th); effective 15 days after publication | Superseded by EO 113 (R7.7) | [^eo-175-2022-12th-finl:1] | P |
| R3.11 | 2022-09-21 announced; live Aug 2023 | Retail access | GCash "GStocks" (AB Capital Securities as broker, PSE tech support) announced; PSE later reports over 1.7 million registered users and 15,000 on Maya Stocks | In force | [^pse-pr-gcash-gstocks-2022-09-21][^pse-analyst-briefing-3m-2026:21] | P |
| R3.12 | 2022-09-26 | Incident | Typhoon: no trading and no clearing/settlement | Historical | [^pse-cn-2022-0035-trading-suspension-2022-09-26:1] | P |

**B4. 2023**

| ID | Effective date | Area | Change (before to after) | Status | Sources | Ev |
|---|---|---|---|---|---|---|
| R4.1 | 2023-02-10 memo (SEC approval 2022-12-13) | Clearing collateral | SCCP Rule 8.1.8: securities of the PSEi, MidCap and Dividend Yield indices (and PSE shares) accepted as collateral in the mark-to-market collateral deposit (MMCD) system, haircut 25% (PSE shares 35%), aligned with the RBCA position-risk factors. Effective date not stated in the part read | In force | [^sccp-memo-02-0223-collateral-haircut-rates:1] | P |
| R4.2 | 2023-03-27 | Clearing | SCCP moves to LSEG Technology Millennium Clearing/Risk (multi-currency; settles multiple trade dates in one day; prerequisite for T+2) | In force | [^pse-pr-sccp-new-clearing-system-2023-03-31] | P |
| R4.3 | 2023-05-24 | SBL | SEC approves offshore collateral for SBL with at least one foreign party (cash USD/EUR/JPY/GBP/AUD; OECD government/agency debt rated BBB or better; constituents of WFE-member benchmark indices), for Qualified Buyers. SEC also approved PDTC as a Lending Agent on 21 Jul 2023 | In force | [^pse-cn-2023-0027-offshore-collateral-sbl:1][^pse-cn-2023-0048:2][^pse-asm-2024-presidents-report:24] | P |
| R4.4 | 2023-08-24 | Settlement | T+3 to T+2 (first T+2 trade date 24 Aug; SEC En Banc approval 10 Aug). Trades of 23 Aug (last T+3) and 24 Aug (first T+2) both settled on 29 Aug 2023. Ex-date moves to one trading day before record date. Deadline 12:00 noon (temporarily 13:00 until 11 Sep). SCCP rule amendments effective on go-live | In force | [^pse-cn-2023-0031-t2-settlement:1-2][^pse-cn-2023-0040-t2-go-live:1-3][^sccp-memo-06-0823-sec-approval-t2-amendments:1][^sccp-memo-07-0823-sec-approved-amendments:1] | P |
| R4.5 | 2023-08-25 consultation | MPO | PSE proposes amendments to the Public Ownership Guidelines, the Amended MPO Rule and the Amended Voluntary Delisting Rules (codify MPO levels by listing vintage and monthly public-ownership-report triggers; delisting vote basis); comments to 8 Sep 2023. Adoption date not found; the Aug 2026 rule restates the codified levels | Proposed (outcome unclear) | [^pse-cn-2023-0041-mpo-delisting-consult:1-3] | P; adoption unknown |
| R4.6 | 2023-09-05 consultation | Algorithmic trading / VWAP | PSE proposes allowing algorithmic trading (DMA Rules then prohibited it via DMA, with exemptions for child orders of conditioned parent orders) and a VWAP facility. VWAP adopted (R5.3); no approval notice for the algorithmic-trading part was found | Algo part: Proposed (outcome unknown); VWAP part: In force | [^pse-cn-2023-0043:2][^pse-cn-2023-0043:4] | P; algo outcome unknown |
| R4.7 | 2023-10-02 | Short selling | PSE Guidelines for Short Selling Transactions declared effective; eligible set widened from PSEi + ETFs to PSEi + MidCap + Dividend Yield + ETFs; BIR (letter 6 Sep 2023) accepts registration of a GMSLA with a foreign party; offshore collateral recognised | In force | [^pse-cn-2023-0048:1-2][^pse-cn-2023-0048:8][^pse-pr-short-selling-effectivity-2023-10-02] | P |
| R4.8 | 2023-10-09 consultation | Board lot | Proposal to cut lot sizes to allow a PHP100 minimum investment (e.g. 1,000,000 to 20,000; 100 to 20 for 5-9.99; 10 to 2 for 50-99.95; 10 to 1 for 100+); comments to 23 Oct 2023. PSE's July 2024 report says it was "awaiting SEC approval" (maximum lot 1,000,000 cut to 20,000; minimum 5 cut to 1); no approval was ever announced, the July 2025 report does not mention it, and the Dec 2025 paper shows the old table as "existing" and proposes one-share lots instead | Abandoned (filed, never approved, replaced by R6.10; I) | [^pse-cn-2023-0051:1][^pse-cn-2023-0051:3-4][^pse-asm-2024-presidents-report:18][^pse-cn-2025-0046-board-lot-trading-at-last:4] | P; "abandoned" is I |
| R4.9 | 2023-11-06 | Short selling | Program go-live (postponed from 23 Oct 2023 to give more preparation time); FEOMS recertification needed to tag short sales; Daily Short Sell Report published; its first edition (6 Nov 2023) lists 53 eligible securities, all with zero volume | In force | [^pse-cn-2023-0056:1][^pse-dssr-2023-11-06:1-2][^gma-2023-10-20-short-selling-nov-6] | P |

**B5. 2024**

| ID | Effective date | Area | Change (before to after) | Status | Sources | Ev |
|---|---|---|---|---|---|---|
| R5.1 | 2024-01-03 | Incident | Market halted 09:32; resumed 11:56 (technical issue with a third-party front-end provider); afternoon on schedule | Historical | [^pse-cn-2024-0001-market-halt:1][^pse-cn-2024-0003-update-market-halt:1] | P |
| R5.2 | 2024-01-26 memo; effective 2024-02-05 | PSEi methodology | Pension-fund/SSS/GSIS shares counted as free float unless the fund has a board seat (effective immediately); semiannual membership changes effective 5 Feb 2024 | In force | [^pse-cn-2024-0008:1] | P |
| R5.3 | 2024-02-01 SEC-approved rules effective; 2024-03-01 go-live | Closing sequence | VWAP Trading Rules: Closing VWAP session 15:00-15:15; market close 15:00 to 15:15 (half-day: Closing VWAP 12:10-12:25, close 12:25). VWAP trades at least PHP500,000, single TP, executed only in the 15 minutes after run-off at the full-day VWAP computed by PSE (excluding block sales, intentional crosses and odd lots) | In force | [^pse-approved-rules-vwap-trading-2024:1][^pse-approved-rules-vwap-trading-2024:3][^pse-approved-rules-vwap-trading-2024:7][^pse-cn-2024-0012-vwap-go-live:1][^pse-pr-vwap-2024-02-16] | P |
| R5.4 | 2024-03-05 memo (SEC approval 2024-01-09) | Settlement batch | SCCP Operating Procedure 2.5.3.2: the settlement batch run (normally 12:00) may start earlier once all cash and securities obligations are delivered, with 10 minutes' notice to clearing members and settlement banks | In force | [^sccp-memo-01-0324-early-batch-run-effectivity:1] | P |
| R5.5 | 2024-04-18 | Commission | SEC MC 7-2024 (16 Apr 2024) removes the minimum broker commission; PSE's minimum-commission rule (0.25% to 0.05% bands) ceased to be in force; PD 154 maximum of 1.5% remains | In force | [^pse-cn-2024-0029-min-commission-removal:1-3][^pse-pr-cmepa-day1-2025-07-01] | P |
| R5.6 | 2024-06-05 | SBL tax | BIR RR 10-2024 amends RR 10-2006: MSLA/GMSLA approval retroacts to complete submission; one registration for multilateral MSLA with accession agreements; counterparties may switch lender/borrower roles | In force | [^pse-cn-2024-0035:1-2] | P |
| R5.7 | 2024-09-26 consultation | Products | PSE Rules for Global Philippine Depositary Receipts (GPDR) opened for comment to 16 Oct 2024 | Proposed (awaiting SEC; see Section 2) | [^pse-cn-2024-0047:1] | P |
| R5.8 | 2024-10-09/10 | Broker failure | SEC involuntary suspension and preservation order against Equitiworld Securities; CMIC special audit of its books; CMIC later took over its operations (PSE circular titled "Take Over of the Operations of Equitiworld Securities, Inc.", Nov 2024) | Historical (liquidation plan approved Mar 2026, R7.5) | [^pse-cn-2024-0053-equitiworld-involuntary-suspension:1][^pse-web-announcements-archive] | P (take-over: title only) |
| R5.9 | 2024-12-09 | Incident | Pre-open delayed; open moved to 09:55 | Historical | [^pse-cn-2024-0061-adjusted-schedule-2024-12-09:1] | P |
| R5.10 | 2024-12-26 | Corporate | PSE signs to buy 61.92% of PDS Holdings (PHP600/share, PHP2.32bn) on top of its 20.98%; PDS consolidated as a majority-owned subsidiary in Dec 2024 | In force (ownership 94.55% at 5 Mar 2026) | [^pse-pr-pds-acquisition-2024-12-26][^philstar-2025-12-24-pds-landbank][^pse-analyst-briefing-3m-2026:25] | P/S |

**B6. 2025**

| ID | Effective date | Area | Change (before to after) | Status | Sources | Ev |
|---|---|---|---|---|---|---|
| R6.1 | 2025-01-21 memo | Settlement allocation | SEC approves SCCP Rules 3.4 (allocation algorithm: largest outstanding netted amounts settled first; partial deliveries; Annex 11), 5.1.4, 6.2.8 and 7.6 | In force | [^sccp-memo-02-0125-sec-approval-rules-3-4-5-1-4-6-2-8-7-6:1] | P |
| R6.2 | 2025-03-24 | Incident | System connectivity issue: market open delayed to 11:10 | Historical | [^pse-cn-2025-0015-adjusted-schedule-2025-03-24:1] | P |
| R6.3 | 2025-05-22 | Technology | PSE and Nasdaq announce the upgrade from PSEtrade XTS to Nasdaq Eqlipse Trading | Approved, not yet effective (NTE, Section 2) | [^pse-pr-nasdaq-eqlipse-2025-05-22][^pse-analyst-briefing-3m-2026:24] | P |
| R6.4 | 2025-07-01 (signed 2025-05-29) | Tax (RA 12214 CMEPA) | STT 0.6% to 0.1% of gross selling price on "shares of stock and other securities" listed and traded on a local exchange (and, new, on domestic shares listed on foreign exchanges), with "securities" defined broadly; sale of listed shares exempt from DST; DST on original issuance 1% to 0.75%; final tax on bank interest 20%. PSE applies 0.1% to trades from 1 Jul 2025 (Tuesday) | In force | [^ra-12214-cmepa:3][^ra-12214-cmepa:16][^ra-12214-cmepa:17-18][^ra-12214-cmepa:25][^pse-cn-2025-0026-stt-decrease-advisory:1][^pse-cn-2025-0028-cmepa-effectivity:1][^bir-rr-20-2025-stt:4][^pse-pr-cmepa-day1-2025-07-01][^pse-analyst-briefing-3m-2026:20][^pse-annual-report-2025:39] | P |
| R6.5 | 2025-07-04 / 2025-07-15 | Tax operations | BIR advisory: eBIRForms/eFPS lacked the new STT rate, so brokers file BIR Form 2552 manually and pay at an Authorized Agent Bank | Interim (current status not checked) | [^pse-cn-2025-0032-bir-stt-advisory:1] | P |
| R6.6 | 2025-07-08 memo | Clearing fund | SEC approves amended SCCP Rule 5.2 and Operating Procedures on refund of Clearing and Trade Guaranty Fund contributions (conditions when a clearing member ceases business) | In force | [^sccp-memo-01-0725-ctgf-refund-sec-approval:1] | P |
| R6.7 | 2025-08-05 | Tax regulations | BIR RR 19-2025 (DST), RR 20-2025 (STT; signed 29 Jul, effective 1 Jul 2025), RR 21-2025 (CMEPA income-tax provisions) | In force | [^bir-rr-19-2025-dst:1][^bir-rr-20-2025-stt:1][^bir-rr-20-2025-stt:4][^bir-rr-21-2025-cmepa-income:1] | P |
| R6.8 | 2025-08-09 effective; 2025-08-11 first trading day | Share classes | SEC MC 10-2025 (7 Aug) repeals the 1973 Class A/B regular-board rule: buyers receive the class they bought (from 11 Aug 2025); companies must declassify by amending Articles by 9 Aug 2026; PSE (10 Sep 2026): two-day trading suspension before delisting of the classified shares, price adjusted to the higher of the A/B closes | In force; migration ongoing | [^pse-cn-2025-0035-sec-declassification-mandate:1-3][^pse-cn-2025-0036-declassification-effectivity:1][^pse-cn-2026-0041-declassification-price-suspension:1-2] | P |
| R6.9 | 2025-08-20 (SEC-approved) | Halts and calamities | Market-wide halt trigger changed from "at least one-third of TPs cannot access the system" to "TPs with more than 50% of six-month ADTV (ex-block) cannot trade, directly or via their correspondent TP"; every TP needs a correspondent TP; new calamity guidelines (signal 3-5 in NCR = no trading). Consultation was May 2022 | In force | [^pse-cn-2025-0037:1-2][^pse-cn-2025-0037:4][^pse-cn-2022-0020-market-halt-consultation:4][^pse-annual-report-2025:40] | P |
| R6.10 | 2025-12-15 consultation | Lot size / closing | PSE proposes One Lot One Share, a new tick table, removal of the odd-lot market and a change to run-off/trading-at-last matching, tied to the new engine; comments to 31 Dec 2025 | Proposed (Section 2) | [^pse-cn-2025-0046-board-lot-trading-at-last:1][^pse-cn-2025-0046-board-lot-trading-at-last:3-5] | P |
| R6.11 | 2025-12-24 | Corporate | PSE raises its PDS stake to 94.21% (Landbank shares); DBP the main holdout (3.08%) | In progress | [^philstar-2025-12-24-pds-landbank] | S |

**B7. 2026 (to 6 Oct)**

| ID | Effective date | Area | Change (before to after) | Status | Sources | Ev |
|---|---|---|---|---|---|---|
| R7.1 | 2026-01-19 | Incident | PSE EDGE disclosure system outage; one-hour news halt of MRC shares (09:30-10:30) | Historical | [^pse-cn-2026-0004-2-emergency-disclosures-trading-halt:1-2] | P |
| R7.2 | 2026-01-25 (SEC MC 1-2026 issued 8 Jan) | REIT regime | REIT eligible assets widened (indirect holdings through 2/3-owned SPVs; toll roads, railways, airports, ICT, energy, data centres; reinvestment period 2 years) | In force | [^pse-analyst-briefing-3m-2026:17][^philstar-2026-07-17-sec-accomplishments] | P/S |
| R7.3 | 2026-02-02 | Dynamic threshold | Semiannual reclustering (Jul-Dec 2025 data); cluster rules unchanged | Superseded by R7.12 | [^pse-tpa-2026-0002-dynamic-threshold-review:1] | P |
| R7.4 | 2026-02 (SEC MC 11-2026 signed; effective on publication) | MPO | New SEC minimum-public-ownership rules for listed issuers | In force (PSE rule R7.13) | [^pse-cn-2026-0020-mpo-consult:7-10] | P |
| R7.5 | 2026-03-19 | Broker failure | CMIC notice (relayed by PSE): SEC approves CMIC's proposed liquidation and allocation plan for distributing Equitiworld Securities' trade-related assets | In progress | [^pse-cn-2026-0012:1] | P |
| R7.6 | 2026-04-03 | Universe | Asian Terminals (ATI) delisted voluntarily (approved 25 Mar 2026) | Historical | [^pse-cn-2026-0013-ati-voluntary-delisting:1] | P |
| R7.7 | 2026-04-13 signed; effective 15 days after publication (reported 1 or 2 May 2026) | Foreign ownership | EO 113: 13th Regular Foreign Investment Negative List. List A (constitution/specific laws): no foreign equity in mass media and internet business, corporate practice of architecture, cooperatives, private security, small-scale mining, marine resources; up to 25% private recruitment and defense-related construction; 30% advertising; 40% for public utilities (the six RA 11659 categories), natural resources including water (renewables fully open), private land, retail trade with paid-up capital under PHP25M, educational institutions, rice and corn, government procurement, fishing vessels, condominiums; telecom operation and management 100% with reciprocity, 50% without (RA 11659 Sec. 25). List B (security, health, SMEs): 40% for firearms/explosives, military materiel (RA 12024), gambling, micro and small domestic enterprises under US$200,000 paid-in capital. KPMG reports the telecom, architecture, retail and materiel items as changes from the 12th list | In force | [^eo-113-2026-13th-finl:1-2][^eo-113-2026-13th-finl:3-7][^kpmg-2026-04-13th-finl] | P (change-vs-12th: S) |
| R7.8 | 2026-04-22 (PDS memo); 2026-05-18 (PSE CN-2026-0022) | SBL | PDTC Lending Agency Service onboards first lenders and borrowers with BIR-registered agreements (cash collateral); more participants invited | In force | [^pse-cn-2026-0022:1-2] | P |
| R7.9 | 2026-05-15 SEC approval, effective immediately; PSE memo 2026-05-22 | SBL approvals | SEC approves PSE's 2026 Revised Guidelines for MSLA clearance: PSE acts as one-stop shop for MSLA and accession-agreement pre-clearance and BIR registration (no separate SEC and BIR approval per MSLA). Press adds that registration time falls from 7 to 5 working days and the SEC fee of PHP5,030 is removed (Philstar, 10 Jun 2026) | In force | [^pse-cn-2026-0025:1][^philstar-2026-06-10-sec-msla][^pse-analyst-briefing-1h-2026:9] | P/S |
| R7.10 | 2026-07-31 | Broker failure | CMIC imposes involuntary suspension on Benjamin Co Ca & Company, Inc. | Historical (status after suspension not checked) | [^pse-tpa-2026-0035-benjamin-co-ca-involuntary-suspension:1] | P |
| R7.11 | 2026-08-03 | Indices and back-office | PSEi: Maynilad (MYNLD) in, Converge (CNVRG) out; MidCap, DivY and sector changes; new PSE Portal go-live for back-office files | In force | [^pse-cn-2026-0035:1][^pse-nte-faq-2026-08:2] | P |
| R7.12 | 2026-08-07 | Dynamic threshold | Semiannual reclustering (Jan-Jun 2026 data) | In force | [^pse-tpa-2026-0036-dynamic-threshold-review:1] | P |
| R7.13 | 2026-08-11 | MPO | PSE Amended MPO Rule and Revised Public Ownership Guidelines effective immediately (tiered IPO float 33/25/20/15%; REIT 33.33%; maintenance 20%/15%; lower float down to 12% possible above PHP200bn) | In force | [^pse-memo-2026-08-11-mpo-rule-effectivity:1-4] | P |
| R7.14 | 2026-08-12 | Listing | Rule on listing preferred shares by IPO or direct listing: minimum offer PHP100M (was PHP1bn), 100 holders (was 1,000); direct-listed preferreds tradable immediately | In force | [^pse-cn-2026-0037-preferred-shares-rule-effectivity:1-2][^pse-analyst-briefing-1h-2026:16] | P |
| R7.15 | 2026-08-31 (after close) | Benchmarks | MSCI Philippines Index drops Ayala Land (reported reason: share-price decline and weaker H1 earnings): 9 constituents; ICTSI 44.73%, BDO 13.41%, BPI 8.38%, SM Prime 7.72% at 30 Sep 2026 | In force | [^newswav-2026-08-msci-ali][^msci-philippines-index-factsheet-2026-09:1-2] | S/P |
| R7.16 | 2026-08-31 | Universe | Robinsons Retail Holdings (RRHI) delisted voluntarily (approved 20 Aug 2026); PSE had already announced its removal from the Dividend Yield, MidCap and Services indices (CN-2026-0032, 14 Jul 2026, title only) | Historical | [^pse-cn-2026-0038-rrhi-voluntary-delisting:1][^pse-web-announcements-archive] | P |
| R7.17 | 2026-10-06 | Incident | PSE EDGE portal again unavailable (second time in 2026 after 19 Jan); PSE directs the public to its website and companies to submit emergency disclosures (CN-2026-0046; batches for Globe, Jollibee, Ayala Corp, PLDT, ACEN and others posted the same day). No trading halt notice seen | Historical (same-day; resolution not checked) | [^pse-cn-2026-0046-edge-outage-access-to-disclosures:1][^pse-web-announcements-archive] | P |

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
| | 0.1% | 2025-07-01 | open | R6.4 |
| Settlement cycle | T+3 | before 2023 | 2023-08-23 | B0.3 |
| | T+2 | 2023-08-24 | open | R4.4 |
| Lower static threshold | -50% | before 2020 | 2020-03-23 | B0.5 |
| | -30% | 2020-03-24 | open | R2.3 |
| Index circuit breaker | single -10% = 15 min | before 2020 | 2020-05-03 | B0.5 |
| | three levels -10/-15/-20% | 2020-05-04 | open | R2.4 |
| Official close | 15:30 | 2013-11-04 | about 2020-03-13 (last full-day schedule; I) | B0.1 |
| | 13:00 (no trading 17-18 Mar 2020) | 2020-03-16 | 2021-12-03 | R2.2 |
| | 15:00 | 2021-12-06 | 2024-02-29 (13:00 from 2022-01-14 to 2022-02-28) | R3.3, R3.5, R3.6 |
| | 15:15 (Closing VWAP 15:00-15:15) | 2024-03-01 | open | R5.3 |
| Short selling | not operating | before 2023-11-06 | 2023-11-05 | R4.9 |
| | operating (eligible list) | 2023-11-06 | open | R4.9 |
| Broker minimum commission | sliding 0.25% to 0.05% | before 2024 | 2024-04-17 | R5.5 |
| | none (maximum 1.5% remains) | 2024-04-18 | open | R5.5 |
| Market-halt trigger | one-third of TPs unable to access | before 2025-08-20 | 2025-08-19 | R6.9 |
| | TPs above 50% of six-month ADTV | 2025-08-20 | open | R6.9 |
| Class A/B delivery on the regular board | either class | before 2025-08-11 | 2025-08-10 | R6.8 |
| | class purchased | 2025-08-11 | open (declassification by 9 Aug 2026) | R6.8 |
| PSEi / sector float floor | 12% | before 2018-02 | 2018-02-18 | B0.6 |
| | 15% | 2018-02-19 | Feb 2023 recomposition (I) | R1.2 |
| | 20% | Feb 2023 recomposition (I) | Feb 2027 rebalance | R3.2 |
| Board lot / tick table | single 15-band table | at least 2013 | open (NTE target 2026-11-23) | B0.7, P2 |

**Short selling and SBL: sequence.** 30 Nov 2017 consultation (CN-2017-0068, title only) then SEC approval 5 Jun 2018 (R1.5), amendment Jan 2019 (R1.7), offshore collateral 24 May 2023 (R4.3), BIR GMSLA acceptance 6 Sep 2023 and guideline effectivity 2 Oct 2023 (R4.7), go-live 6 Nov 2023 (R4.9), BIR RR 10-2024 on 5 Jun 2024 (R5.6), PDTC lending pool Apr-May 2026 (R7.8), SEC-approved MSLA guidelines 15 May 2026 (R7.9); revised SBL rules filed with SEC 16 Apr 2026 (pending). MSCI's June 2026 accessibility review says the program "was implemented in November 2023. However, it is not yet an established market practice." [^msci-accessibility-review-2026:43]. Uptick rule text (SRC Rule 24.2-2.5): price above last sale, or equal to last sale only if that price exceeds the preceding different sale [^pse-web-sbl-short-selling].

**PSEi methodology: sequence.** Float floor 12% to 15% (Feb 2018, R1.2); to 20% (Aug 2021 memo, first applied Dec 2022 review, R3.2); MidCap and Dividend Yield indices (Mar 2022, R3.8); pension-fund float clarification (Jan 2024, R5.2). Approved but not yet effective: 21 Jul 2026 revised policy to apply at the February 2027 rebalance (98% cumulative market-cap screen; MTAR of at least 15% (10% for incumbents) plus MADV top-25% in 9 of 12 months replaces the single median-daily-value test; float floor 20% with a 15% exception for companies of PHP250bn market capitalisation or more) [^pse-cn-2026-0033b:1][^pse-cn-2026-0033b:7-8]. PSEi 2018 liquidity test for comparison: top 25% by median daily value in 9 of 12 months [^pse-index-policy-feb2018:6].

**Participant base.** Active trading participants: 132 when PSE moved to PSE Tower in Feb 2018 [^pse-pr-trading-floor-closed-2022-06-24]; 125 on 4 Jan 2022 [^pse-cn-2022-0001-delay-market-opening:1]; 123 in PSE's public directory of 20 Jul 2026 (my count of "Nominee" entries) [^pse-active-tp-summary-2026-07-20:1-6]. Of these, 40 run their own front-end order management systems (FEOMS) and so must certify against the new engine [^pse-nte-broker-forum-2026-07-09:5]. Investor accounts: 1.62 million (2021) to 3.64 million (2025), 88.6% online [^pse-analyst-briefing-1h-2026:8]. Listed companies: 280 at 14 Aug 2026 [^pse-analyst-briefing-1h-2026:3].

**Operational incidents that bear on engine-replacement risk** (all P): 4 Jan 2022 full-day cancellation (engine-to-front-end connection) [^pse-cn-2022-0002-cancellation-of-trading-2022-01-04:1]; 3 Jan 2024 halt 09:32-11:56 [^pse-cn-2024-0003-update-market-halt:1]; 9 Dec 2024 late open 09:55 [^pse-cn-2024-0061-adjusted-schedule-2024-12-09:1]; 24 Mar 2025 late open 11:10 [^pse-cn-2025-0015-adjusted-schedule-2025-03-24:1]; weather closures 26 Sep 2022 and 24 Jul 2024 [^pse-cn-2024-0038-trading-suspension-2024-07-24:1]. Three of four technical incidents involved the third-party front-end or connectivity layer rather than the matching engine (I).

### Inferences
- The 1 Jul 2025 STT cut is the single largest discontinuity in transaction cost in the window: sell-side tax fell from 60 bp to 10 bp, so any cost model or backtest spanning that date must switch rates by trade date, not by calendar year (I, from R6.4 and R1.1).
- "Close time" has three regimes: 15:30 (to 13 Mar 2020), 13:00 (Mar 2020 to Dec 2021), 15:00 (Dec 2021 to Feb 2024), 15:15 (from 1 Mar 2024); continuous trading ends at pre-close (15:15, then 12:45, then 14:45) so the last continuous print is not the official close (I, from the timetable table).
- Circuit-breaker cut-off clock times in CN-2020-0044 were written against a 15:15 pre-close; no republished clock times for the 14:45 pre-close were found, so either the cut-offs scale with pre-close (14:25 / 14:10 / 13:40 by subtraction) or they stayed absolute. Not resolvable from documents reviewed (I).
- PSE's web list of amendments to the Revised Trading Rules (not exhaustive: it omits the Aug 2025 halt amendments) shows no change to the lot/tick article after 2013, no circular in the 2017-2026 index announces one, and the Dec 2025 paper reproduces the same table as "existing"; so treating lot size and tick size as a pure function of price band for 2018 to Nov 2026 looks safe, but "unchanged since 2013" rests on absence of evidence (I) [^pse-web-reg-trading-participants][^pse-cn-2025-0046-board-lot-trading-at-last:4].
- PSE targets have repeatedly slipped (short selling: SEC-approved Jun 2018, live Nov 2023; GPDR: Q1 2025 target, still at SEC in Oct 2026; derivatives: Q1 2026 target, no date now), so the 23 Nov 2026 NTE date should be treated as a target with execution risk until PSE confirms the final rehearsals (I; see Section 2).

### Gaps
- Exact publication dates (and therefore effective dates) for RA 11647, RA 11659, EO 175 and RA 11534 were not retrieved; EO 113's date is reported as 1 May (KPMG, from a 16 Apr publication) or 2 May 2026 (another report); CREATE's reported 11 Apr 2021 is secondary.
- Consolidated, current text of the PSE Revised Trading Rules and Implementing Guidelines was not found; the archived versions are 2010-2013 vintages, so the static/dynamic threshold wording after 2020 rests on circulars (CN-2020-0028, CN-2020-0044, CN-2021-0055) and the PSE web page.
- Outcome of the 2018 "trading without settlement" proposal and of the 2023 algorithmic-trading proposal not found.
- SEC MC 13-2017 (earlier MPO rule) effective date and SEC MC 11-2026 publication date not retrieved.
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
| P20 | MSCI / FTSE classification | Philippines stays Emerging (MSCI) and Secondary emerging (FTSE); MSCI 2026 market classification announcement named other markets but not the Philippines; MSCI's June 2026 accessibility review still lists foreign-ownership, FX and short-selling frictions | No change pending | MSCI/FTSE calendars not retrieved | [^ftse-geis-ground-rules-2026-09:45][^ladige-2026-06-msci-mcr][^msci-accessibility-review-2026:43] | P/S |

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

### Inferences
- The NTE go-live depends on three things PSE does not control: SEC approval of the lot/tick, trading-at-last and negotiated-trade rule changes; broker FEOMS readiness (many TPs had not started on 9 Jul); and vendor-layer connectivity. No deferral has been announced as of 6 Oct 2026, but given the readiness figures and the SEC dependencies the schedule risk is non-trivial (I).
- If SEC does not approve One Lot One Share before 23 Nov, PSE would either keep the existing lot table on the new engine or delay the engine; PSE materials do not say which (I). Code should read lot size and tick size from the security master (PSE static-data files) rather than hard-coding either regime.
- Two large listings are scheduled in October 2026 (Vitro REIT on 12 Oct and Globe Fintech/Mynt on 19 Oct; PNB Holdings by introduction on 25 Sep) and will be among the first under the new tiered MPO rule (REIT 33.33%; issuers above PHP50bn 15% with an offer of at least PHP10bn). PSE's deck gives amounts (PHP24.19bn and PHP92.31bn) without saying whether they are offer size or valuation, so any MPO or index-inclusion conclusion needs the prospectuses (I) [^pse-analyst-briefing-1h-2026:13][^philstar-2026-07-17-sec-accomplishments][^pse-memo-2026-08-11-mpo-rule-effectivity:2].

### Gaps
- No PSE notice after 25 Sep 2026 on the NTE; the 25 Sep "trading day advisory" for 16-18 Nov 2026 is a placeholder promising a final advisory [^pse-trading-day-advisory-2026-11-16-18:1]. Whether the 16-18 Nov operations interact with the 23 Nov cutover is unknown.
- SEC approval status of the board-lot, trading-at-last and negotiated-trade rules after 17 Aug 2026 is unknown; PSE's circular index to 2 Oct shows no approval memo.
- No statement on whether static/dynamic thresholds, circuit breakers, order types beyond limit, or session times change with the NTE.
- FTSE and MSCI review calendars and any pending watch-list for the Philippines were not retrieved (only classification tables and the MSCI index factsheet).
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
- slug: pse-active-tp-summary-2026-07-20
  title: "PSE Active Trading Participants public directory as of 20 Jul 2026"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://www.pse.com.ph/directory/"
  local_path: pdfs/pse-active-tp-summary-2026-07-20.pdf
  edition: in-force
  amended_through: "2026-07-20"
  note: "Count of 123 entries is this researcher's tally of 'Nominee' lines. Archived by another researcher; original URL not recorded."
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
- slug: pse-cn-2019-0004-short-selling-guidelines-amendment
  title: "PSE Memorandum CN-No. 2019-0004: Amendments to the PSE Guidelines for Short Selling Transactions"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2019-0004.pdf"
  local_path: pdfs/pse-cn-2019-0004-short-selling-guidelines-amendment.pdf
  edition: superseded
  amended_through: "2019-01-23"
  note: "Incorporated in the Oct 2023 text."
- slug: pse-cn-2019-0037-foreign-investment-etf
  title: "PSE Memorandum CN-No. 2019-0037: Foreign investment into Philippine Exchange-Traded Fund (BSP Circular 1030 s. 2019)"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2019-0037.pdf"
  local_path: pdfs/pse-cn-2019-0037-foreign-investment-etf.pdf
  edition: historical
  amended_through: "2019-07-08"
  note: ""
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
- slug: pse-cn-2020-0076-mpo-initial-backdoor-listing
  title: "PSE Memorandum CN-No. 2020-0076: Guidelines on minimum public ownership for initial and backdoor listings"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2020-0076.pdf"
  local_path: pdfs/pse-cn-2020-0076-mpo-initial-backdoor-listing.pdf
  edition: superseded
  amended_through: "2020-08-03"
  note: "Replaced by the Aug 2026 Amended MPO Rule."
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
- slug: pse-index-policy-feb2018
  title: "PSE Policy on Index Management (February 2018)"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://www.pse.com.ph/indices/"
  local_path: pdfs/pse-index-policy-feb2018.pdf
  edition: superseded
  amended_through: "2018-02-12"
  note: "Cover says February 2018; date taken from the covering memo CN-2018-0013. Archived by another researcher; original URL not recorded."
- slug: pse-memo-2026-08-11-mpo-rule-effectivity
  title: "PSE Memorandum: effectivity of the PSE Amended Rule on Minimum Public Ownership and Revised Guidelines in Determining Public Ownership"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2026/08/Memo-to-Public_Effectivity-of-the-Amended-MPO-Rule-Rvsd-PO-Guidelines-v2.pdf"
  local_path: pdfs/pse-memo-2026-08-11-mpo-rule-effectivity.pdf
  edition: in-force
  amended_through: "2026-08-11"
  note: ""
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
```
