---
number: 17
slug: reform-timeline
title: Reform Timeline and Pipeline
summary: What is in force on 6 Oct 2026, every dated rule change since 2018, version gates for backtests, and the pipeline led by Nasdaq Eqlipse on 23 Nov 2026, whose rule changes still await SEC approval.
part: Evidence and synthesis
---

This chapter is the knowledge base's currency anchor. It says what was in force on 6 October 2026, what changed between 2018 and that date and when, which rule set governs which trade dates, and what has been announced but is not in force. Other chapters carry the mechanics and link here for dates; every row below names its implementing document, so where a chapter and this one disagree on a date, this one wins.

Two things break assumptions carried over from other venues or from older documentation. **The largest change is still pending**: PSE's Nasdaq Eqlipse engine is scheduled to replace PSEtrade XTS on Monday 23 November 2026 in one cut-over with limit orders only on Day 1, and the rule changes it depends on (one-share lots, a new tick table, no odd-lot market, a changed run-off rule, Negotiated Trades) had no SEC approval on record on 6 October 2026. Every XTS-era rule in this knowledge base is therefore "in force on 6 October 2026, subject to change from 23 November". **The public record of the rules is also stale in places**: PSE publishes no consolidated Revised Trading Rules (the posted text is the June 2010 base, effective 26 July 2010, plus separate amendment memos),[^pse-revised-trading-rules:1][^pse-implementing-guidelines-trading-rules:1][^pse-web-reg-trading-participants] SCCP's posted rulebook is the 13 March 2018 T+3 text,[^sccp-clearing-house-rules-2018:1][^sccp-web-rules-page] and PSE's own "Investing at PSE" page prints a 15:15 close next to a 15:30 close. The rule set is reconstructed from dated circulars, and each reconstruction below says which.

## In force on 6 Oct 2026

"Since" is the date the current value took effect (trade date unless stated). The last column says where the mechanics live.

| Parameter | In force on 6 Oct 2026 | Since | Detail |
|---|---|---|---|
| **Trading engine** | PSEtrade XTS (Nasdaq X-stream); floorless trading; SCCP clearing on LSEG Millennium.[^pse-annual-report-2015:42][^pse-pr-trading-floor-closed-2022-06-24][^pse-pr-sccp-new-clearing-system-2023-03-31] | 22 Jun 2015; 27 Jun 2022; 27 Mar 2023 | [Ch 1](#/ch/market-architecture) |
| **Whole-day timetable** | 09:00 pre-open; 09:15 pre-open no-cancel; 09:30 open; 12:00 recess; 13:00 resume; 14:45 pre-close; 14:48 pre-close no-cancel; 14:50 run-off / trading-at-last (orders only at the closing price); 15:00-15:15 Closing VWAP session; 15:15 close.[^pse-approved-rules-vwap-trading-2024:3][^pse-web-investing-at-pse] | Close 1 Mar 2024 (was 15:00); other times 1 Mar 2022[^pse-cn-2022-0009-trading-schedule-mar-2022:1][^pse-cn-2024-0012-vwap-go-live:1] | [Ch 3](#/ch/sessions), [Ch 6](#/ch/auctions) |
| **Half-day timetable** | Rule text: pre-close 11:57, no-cancel 11:59, run-off 12:00, Closing VWAP 12:10, close 12:25. None announced; last used 24 and 31 Dec 2021 with different pre-close times.[^pse-approved-rules-vwap-trading-2024:3][^pse-cn-2021-0063-half-day-trading-2021-12:1] | 1 Feb 2024 (rule text) | [Ch 3](#/ch/sessions) |
| **Board lot and tick** | One 15-band PHP table: lot 1,000,000 shares (PHP 0.0001-0.0099) down to 5 shares (PHP 1,000 and above); tick PHP 0.0001 up to PHP 5.00. The same table is in the 2010 rulebook and is shown as "existing" in PSE's Dec 2025 consultation.[^pse-revised-trading-rules:21][^pse-cn-2025-0046-board-lot-trading-at-last:4] | 26 Jul 2010 text; no later amendment found | [Ch 4](#/ch/order-types) |
| **Static threshold** | +50% / -30% of the reference price (previous close or last adjusted close); PSE can lift the band case by case.[^pse-cn-2020-0028:1-2][^pse-cn-2021-0055-lift-lower-static-threshold-sgp:1] | 24 Mar 2020 | [Ch 7](#/ch/price-controls) |
| **Dynamic threshold** | Cap on the move from the preceding last-traded price: 10% (traded more than 500 times in the prior six months), 15% (21-500 times), 20% (20 or fewer); clusters reset each Feb and Aug.[^pse-tpa-2026-0036-dynamic-threshold-review:1] | List of 7 Aug 2026 (previous 2 Feb 2026)[^pse-tpa-2026-0002-dynamic-threshold-review:1] | [Ch 7](#/ch/price-controls) |
| **Index circuit breaker** | PSEi -10% / -15% / -20% against the previous close halts the whole market for 15 / 30 / 60 minutes; each level fires once a day; a higher level supersedes; a halt that crosses the recess includes it.[^pse-cn-2020-0044:1-4] | 4 May 2020 | [Ch 7](#/ch/price-controls) |
| **System-failure halt; typhoon rule** | Market-wide halt if TPs with more than 50% of six-month ADTV (ex-block) cannot trade, directly or through their mandatory correspondent TP; PAGASA signal 3-5 over NCR at 06:00 means no trading, signals 1-2 regular trading.[^pse-cn-2025-0037:1-2][^pse-cn-2025-0037:4] | 20 Aug 2025 (correspondent duty after two months) | [Ch 3](#/ch/sessions), [Ch 7](#/ch/price-controls) |
| **Settlement** | T+2; deadline 12:00 noon on settlement date; the batch run may start earlier once all obligations are in; DVP multilateral net at clearing-member level.[^pse-cn-2023-0040-t2-go-live:1-3][^sccp-memo-01-0324-early-batch-run-effectivity:1] | Trades from 24 Aug 2023; early batch 5 Mar 2024 | [Ch 10](#/ch/clearing-settlement) |
| **Ex-date** | One trading day before the record date.[^pse-cn-2023-0031-t2-settlement:1] | 24 Aug 2023 | [Ch 10](#/ch/clearing-settlement) |
| **Taxes and fees** | STT 0.1% of gross selling price, seller-paid (now also on domestic shares listed abroad); PSE fee 0.005% per side plus 12% VAT; SCCP fee 0.01% per side (VAT-inclusive); SEC "SRC fee" 0.005% per side in PSE's own illustration; broker commission capped at 1.5% plus VAT, no minimum.[^ra-12214-cmepa:16][^bir-rr-20-2025-stt:4][^pse-web-investing-at-pse][^pse-cn-2024-0029-min-commission-removal:1-3] | STT 1 Jul 2025; commission floor removed 18 Apr 2024; fee rates unchanged since 2018 as far as found[^pse-annual-report-2018:88][^pse-annual-report-2019:48] | [Ch 12](#/ch/costs) |
| **Short selling** | Allowed for PSEi, MidCap and Dividend Yield constituents and ETFs (52 securities on the 5 Oct 2026 report); short-interest ratio at or below 10%; uptick rule; no short orders in pre-open or pre-close; day orders only. The first (6 Nov 2023) and the latest (5 Oct 2026) daily reports both show zero short-sale volume, and MSCI (Jun 2026) calls the programme "not yet an established market practice".[^pse-cn-2023-0048:8-10][^pse-dssr-2023-11-06:1-2][^pse-dssr-2026-10-05:1-2][^msci-accessibility-review-2026:43] | 6 Nov 2023 | [Ch 9](#/ch/short-selling) |
| **Securities lending** | MSLA/GMSLA registered with the BIR; PSE pre-clears MSLAs as a one-stop shop; the PDTC Lending Agency Service is live with cash-collateral borrowers; offshore collateral is allowed where a party is foreign.[^pse-cn-2026-0025:1][^pse-cn-2026-0022:1-2][^pse-cn-2023-0027-offshore-collateral-sbl:1] | 24 May 2023 (collateral); 15 May 2026 (MSLA); Apr-May 2026 (PDTC pool) | [Ch 9](#/ch/short-selling) |
| **Market making** | ETF rules only (Part C of the PSE ETF Rules): one ETF (FMETF), one market maker; no single-stock market making.[^pse-etf-rules:1][^pse-web-etf-page] | 18 Mar 2013 | [Ch 8](#/ch/market-making) |
| **Disclosure cut-off** | EDGE same-day release cut-off 4:00 pm; issuers disclose material information within 10 minutes and before the media.[^pse-cn-2026-0024-edge-cutoff-4pm:1][^pse-listing-disclosure-rules:139] | 25 May 2026 (3:30 pm from 1 Mar 2022) | [Ch 11](#/ch/market-data), [Ch 13](#/ch/regulatory-constraints) |
| **PSEi policy** | 30 stocks; free float at least 20%; liquidity = top 25% by median daily value in 9 of 12 months; insert at rank 25 or better, delete at rank 36 or worse; reviews each Feb and Aug; membership last changed 3 Aug 2026.[^pse-index-policy-2024:5-9][^pse-cn-2026-0035:1] | Jan 2024 policy text; 20% float from the Dec 2022 review | [Ch 11](#/ch/market-data) |
| **Minimum public ownership** | IPO float 33% / 25% / 20% / 15% by expected market capitalisation (REIT 33.33%); maintenance 20% (15% above PHP 50bn); a breach means immediate suspension for up to six months, then automatic delisting.[^pse-amended-mpo-rule-2026-08:2-4][^pse-amended-mpo-rule-2026-08:5-6] | 11 Aug 2026 | [Ch 2](#/ch/instruments) |
| **Foreign ownership** | Per-issuer limits, enforced through an order-level local/foreign account flag; a trade that breaches a limit must be unwound at market the same day or at the next open; the 13th Regular Foreign Investment Negative List (EO 113) applies.[^pse-implementing-guidelines-trading-rules:21][^pse-cn-2025-0035-sec-declassification-mandate:3][^eo-113-2026-13th-finl:1-2] | Unwind rule 9 Aug 2025; EO 113 about 1-2 May 2026 | [Ch 14](#/ch/foreign-access) |
| **Class A/B shares** | Regular-board buyers receive the class they bought; companies must declassify (articles amended by 9 Aug 2026); each declassification carries a two-trading-day suspension and an adjusted price equal to the higher of the A and B closes. Five A/B pairs were still listed separately on 6 Oct 2026.[^pse-cn-2025-0036-declassification-effectivity:1][^pse-cn-2026-0041-declassification-price-suspension:1-2][^pse-listed-company-directory-frame] | 11 Aug 2025 | [Ch 2](#/ch/instruments), [Ch 10](#/ch/clearing-settlement) |
| **Algorithmic access** | The DMA facility may not be used for high-frequency or algorithmic trading; Sponsored Access is for QIBs only; the 2023 proposal to permit algorithmic trading has no approval on record.[^pse-memo-sec-approved-dma-rules-2013-11-26:1][^pse-memo-sec-approved-dma-rules-2013-11-26:8][^pse-cn-2023-0043:2] | First trading day of 2014 | [Ch 13](#/ch/regulatory-constraints) |
| **Blocks, crosses, VWAP** | Regular block sale at least PHP 20m within +/-5% of the reference price; special block sale at least PHP 50m; crosses inside the best bid/offer; Closing VWAP trades at least PHP 500,000, single TP, executed only in the 15 minutes after run-off.[^pse-cn-2026-0031-negotiated-trades:3][^pse-approved-rules-vwap-trading-2024:7] | VWAP 1 Mar 2024 | [Ch 5](#/ch/matching) |
| **Products** | Common stocks (Main and SME boards), preferred shares, 8 REITs, one ETF (FMETF), two PDRs (ABSP, GMAP), one warrant series (AGIW, listed 19 Dec 2025). Not available: derivatives, GPDRs, structured warrants.[^pse-web-new-listings][^pse-press-agi-warrants][^pse-analyst-briefing-1h-2026:9-10] | n/a | [Ch 2](#/ch/instruments) |
| **Benchmarks** | MSCI Philippines Index has 9 constituents (30 Sep 2026); FTSE classifies the Philippines Secondary Emerging; FTSE's 2026 annual announcement was scheduled for 6 Oct 2026 and its outcome is not known to this knowledge base.[^msci-philippines-index-factsheet-2026-09:1][^ftse-geis-ground-rules-2026-09:45][^ftse-country-classification-interim-2026-03:5] | n/a | [Ch 11](#/ch/market-data), [Ch 14](#/ch/foreign-access) |

<div class="callout warn">
<span class="label">Scheduled change: 23 Nov 2026, subject to SEC approval</span>

The table above is the PSEtrade XTS rule set. PSE's Nasdaq Eqlipse engine ("NTE") is scheduled to replace it on Monday 23 November 2026, with no parallel run and limit orders only on Day 1.[^pse-nte-broker-forum-2026-07-09:9][^pse-nte-faq-2026-08:1] Five rule changes are tied to it. On PSE's 17 Aug 2026 status slide the board-lot amendments were "For SEC Approval" and Negotiated Trades were "Revising per Public Comments".[^pse-analyst-briefing-1h-2026:9] No approval or effectivity circular had been found by 6 Oct 2026. Never present an NTE parameter as current; see the pipeline below.
</div>

<div class="callout warn">
<span class="label">Evidence cut-off and stale sources</span>

PSE's circular index and NTE page were read on 6 Oct 2026, but the SEC, BIR and Official Gazette sites were unreachable, so an SEC approval issued after PSE's last relay (about 1-2 Oct) would not appear here: "no approval found" means not found, not "not granted". Several authoritative-looking pages are stale. "Investing at PSE" shows the current timetable beside a 15:30 one, a trading-hours FAQ of 9:30-12:00 and 13:30-15:30, a +/-50% static-threshold FAQ and a 30% dividend tax for non-resident corporations (its 0.1% STT line is current).[^pse-web-investing-at-pse] The January 2025 listing and disclosure compilation still prints the RD-3 ex-date and the 3:30 pm EDGE cut-off.[^pse-listing-disclosure-rules:107][^pse-listing-disclosure-rules:139] Use dated circulars; see Conflicts and stale facts.
</div>

### Execution implications

- **Key every parameter by trade date and engine version**, never by calendar year or "current". The Since column is the key; the version gates below turn it into ranges.
- **Do not hard-code lot or tick.** Read both per security from the security master or PSE's static-data files. If the NTE goes live before the SEC approves the new table, PSE's materials do not say whether the old table runs on the new engine, so the router must tolerate either.
- **Source priority:** dated circular, then rulebook text, then PSE FAQ pages, then broker pages. Broker fee pages are the least reliable (some still show 0.6% STT).
- **Calendar service:** settlement dates follow BSP and SCCP business days rather than PSE's own trading calendar (inference from the SCCP business-day definition and the 2017-2024 closures), and the status of 16-18 Nov 2026 is open (see Dated events to February 2027).[^sccp-clearing-house-rules-2018:4]

## Chronology, 2018 to 6 Oct 2026

Rows give the effective date, the change (before to after where a parameter moved) and the implementing document. PSE circulars are CN-yyyy-nnnn (to the public) or TPA-yyyy-nnnn (to trading participants). Listing-rule memos known only by title are grouped and say so.

### Baseline on 1 Jan 2018

The state at the start of the window, for before/after comparisons.

| Area | State on 1 Jan 2018 | Replaced |
|---|---|---|
| Session | 09:00 pre-open (09:15 no-cancel); 09:30 open; 12:00 recess; 13:30 resume; 15:15 pre-close (auction to 15:18, no-cancel to 15:20); 15:20 run-off; 15:30 close. Pre-close had been lengthened from 3 to 5 minutes on 4 Nov 2013.[^pse-memo-pre-close-schedule-2013:1][^pse-memo-extended-pre-close-implementation-2013:1] | 16 Mar 2020; 6 Dec 2021 |
| Settlement | Rolling T+3.[^pse-cn-2023-0031-t2-settlement:1] | 24 Aug 2023 |
| Seller tax | STT 0.5% of gross selling price to 31 Dec 2017.[^pse-cn-2017-0082-stt-increase-advisory:1] | 1 Jan 2018 |
| Price limits | Static band +50% / -50%; one circuit breaker: PSEi -10% = 15-minute halt, "an offshoot of the 2008 global financial crisis".[^pse-cn-2020-0028:1][^pse-cn-2020-0044:1] | 24 Mar 2020; 4 May 2020 |
| Lot and tick | The 15-band table in force today.[^pse-revised-trading-rules:21] | Pending (NTE) |
| Index | PSEi and sector free-float floor 12%; recompositions each March and September.[^pse-cn-2018-0013-index-policy-revision-2018:1] | Feb 2018 |
| Algorithmic access | DMA Rules (SEC-approved, memo 26 Nov 2013) effective the first trading day of 2014: no high-frequency or algorithmic trading through DMA; Sponsored Access for QIBs only.[^pse-memo-sec-approved-dma-rules-2013-11-26:1][^pse-memo-sec-approved-dma-rules-2013-11-26:8] | Unchanged |
| Market making | ETF rules (Part C), SEC-approved 18 Mar 2013; FMETF, still the only ETF, listed 2 Dec 2013.[^pse-etf-rules:1][^pse-annual-report-2013:22] | Unchanged |
| Short selling | Legal base only: SBL Rules effective 15 Feb 2007; short-selling provisions of the Revised Trading Rules effective 26 Jul 2010; SRC Rule 24.2-2 uptick test effective 9 Nov 2015. The programme was not live.[^pse-sbl-short-selling-intro-presentation:2][^pse-revised-trading-rules:20][^sec-2015-src-irr:71][^sec-2015-src-irr-notice-of-effectivity:1] | 6 Nov 2023 |
| Commission | PD 154 capped commission at 1% (raised to 1.5% by the SEC on 14 Dec 1977); PSE rule set a sliding minimum of 0.25% to 0.05% of trade value.[^pse-cn-2024-0029-min-commission-removal:2] | 18 Apr 2024 (minimum) |
| Minimum public ownership | 10% (Amended MPO Rule, effective 1 Jan 2012); SEC MC 13-2017 (1 Dec 2017) raised the IPO requirement to 20%, maintained at all times.[^pse-sr6-mpo-rule-2012:1][^pse-sr6-2-mpo-initial-backdoor-2020:3] | 3 Aug 2020; 11 Aug 2026 |
| Surveillance | CMIC (from 2 Feb 2012) may, with the PSE President's approval, restrict, halt or suspend a security, or a TP's trading in it, on breach of price or volume benchmarks.[^pse-annual-report-2025:8][^pse-cmic-rules:112] | Unchanged |

### Trading schedule and engine

| Effective | Change | Implementing document |
|---|---|---|
| 16 Mar 2020 | Shortened hours: 09:00 pre-open, 09:30 open, no recess, 12:45 pre-close, 12:50 run-off, 13:00 close. No trading or clearing 17-18 Mar (Luzon ECQ); trading resumes 19 Mar on the same timetable with the floor closed; extended to 30 Apr, 15 May, then "until further notice". Superseded 6 Dec 2021 | CN-2020-0017, -0021, -0025, -0046[^pse-cn-2020-0017:1][^pse-cn-2020-0021:1][^pse-cn-2020-0025-resumption-of-trading:1][^pse-cn-2020-0046:1] |
| 6 Dec 2021 | Full-day schedule: 09:00 pre-open, 09:30 open, 12:00 recess, 13:00 resume, 14:45 pre-close, 14:50 run-off, 15:00 close. PSE called it "pre-pandemic"; the pre-March-2020 day resumed at 13:30 and closed at 15:30 (Conflicts: C1) | CN-2021-0059[^pse-cn-2021-0059:1] |
| 24 and 31 Dec 2021 | Half-day trading, the last documented use: pre-close 11:55, no-cancel 11:58, run-off 12:00, close 12:10 | CN-2021-0063[^pse-cn-2021-0063-half-day-trading-2021-12:1] |
| 14 Jan to 28 Feb 2022 | Omicron hours: 09:00, 09:15, 09:30, no recess, pre-close 12:45, no-cancel 12:48, run-off 12:50, close 13:00 (announced to 31 Jan; the run to 28 Feb is implied by CN-2022-0009) | CN-2022-0004; CN-2022-0009[^pse-cn-2022-0004:1][^pse-cn-2022-0009-trading-schedule-mar-2022:1] |
| 1 Mar 2022 | Full-day schedule restored with the 09:15 and 14:48 no-cancel phases listed (close 15:00); EDGE same-day cut-off set at 3:30 pm | CN-2022-0009; CN-2022-0010[^pse-cn-2022-0009-trading-schedule-mar-2022:1][^pse-cn-2022-0010-edge-cutoff-330pm:1] |
| 27 Jun 2022 | Floorless trading: the trading floor closed permanently after 24 Jun (only 29 of 85 booth-leasing TPs renewed); it had reopened under GCQ on 1 Jun 2020 | PSE press release; CN-2020-0051[^pse-pr-trading-floor-closed-2022-06-24][^pse-cn-2020-0051-gcq-floor-reopening:1] |
| 1 Mar 2024 | Closing VWAP session 15:00-15:15; official close 15:00 to 15:15 (half-day close 12:25). VWAP trades: at least PHP 500,000, single TP, executed only in the 15 minutes after run-off at the full-day VWAP (excluding block sales, intentional crosses and odd lots). The SEC-approved rules took effect 1 Feb 2024; the launch date was announced 15 Feb | CN-2024-0010; CN-2024-0012; PSE press release[^pse-approved-rules-vwap-trading-2024:1][^pse-approved-rules-vwap-trading-2024:7][^pse-cn-2024-0012-vwap-go-live:1][^pse-pr-vwap-2024-02-16] |
| 22 May 2025 | PSE and Nasdaq announce the upgrade from PSEtrade XTS to Nasdaq Eqlipse Trading | PSE press release; SEC Form 17-C[^pse-pr-nasdaq-eqlipse-2025-05-22][^pse-17c-2025-05-22-nasdaq-eqlipse-contract:2] |
| 15 Dec 2025 | Consultation on One Lot One Share, a new tick table, odd-lot removal and a run-off change, all tied to the new engine; not in force (P2, P3) | CN-2025-0046[^pse-cn-2025-0046-board-lot-trading-at-last:1] |

### Price controls and halts

| Effective | Change | Implementing document |
|---|---|---|
| 24 Mar 2020 | Lower static threshold -50% to -30% of the reference price (upper +50% unchanged); SEC approval 20 Mar, circular 21 Mar | CN-2020-0028[^pse-cn-2020-0028:1-2] |
| 4 May 2020 | Single breaker (PSEi -10% = 15-minute halt) replaced by three levels: -10% / -15% / -20% = 15 / 30 / 60 minutes, each once a day; SEC approval 20 Mar 2020 | CN-2020-0044[^pse-cn-2020-0044:1-4] |
| 20 Aug 2025 | Market-wide halt trigger: at least one-third of TPs unable to access the system, replaced by TPs with more than 50% of six-month ADTV (ex-block) unable to trade even through their correspondent TP; every TP must have a correspondent TP (two-month grace); NCR PAGASA signal 3-5 = no trading. First consulted May 2022 (CN-2022-0020) and Oct 2023 (CN-2023-0055) | CN-2025-0037[^pse-cn-2025-0037:1-2][^pse-cn-2025-0037:4][^pse-cn-2022-0020-market-halt-consultation:4][^pse-cn-2023-0055:1] |
| 2 Feb 2026; 7 Aug 2026 | Dynamic-threshold semiannual reclustering (Jul-Dec 2025 data; Jan-Jun 2026 data); 20 / 15 / 10% by trade count, rules unchanged | TPA-2026-0002; TPA-2026-0036[^pse-tpa-2026-0002-dynamic-threshold-review:1][^pse-tpa-2026-0036-dynamic-threshold-review:1] |

### Settlement and clearing

| Effective | Change | Implementing document |
|---|---|---|
| 1 Aug 2018 | SCCP Rule 5.2: CTGF contributions refundable, as trade-related assets, when a clearing member ceases business (the 2013 rule allowed no return of cash contributions); conditions changed 8 Jul 2025 | SCCP Rules (SEC approval 13 Mar 2018)[^sccp-clearing-house-rules-2018:35][^pse-sccp-revised-rules:35] |
| 20 Feb 2023 | Rule 8.1.8: PSEi, MidCap and Dividend Yield constituents (25% haircut) and PSE shares (35%) accepted as mark-to-market collateral; the list follows each index review (latest archived: memo 01-0126, effective 2 Feb 2026) | SCCP memo 02-0223 (SEC approval 13 Dec 2022); memo 01-0126[^sccp-memo-02-0223-collateral-haircut-rates:1-2][^sccp-memo-01-0126-eligible-collateral-list:1] |
| 27 Mar 2023 | SCCP moves to the LSEG Millennium clearing and risk system: multi-currency, settles several trade dates in one day, prerequisite for T+2 | PSE press release[^pse-pr-sccp-new-clearing-system-2023-03-31] |
| 23 Aug 2023 | Rule 2.3.5 bars using one client's shares to settle another's obligations except under an SBL arrangement; buy-in and sell-out trades settle early where practicable; settlement dates adjust for holidays and unexpected events; multiple trade dates may settle in one day | SCCP memo 07-0823[^sccp-memo-07-0823-sec-approved-amendments:1-2] |
| 24 Aug 2023 | T+3 to T+2 (SEC En Banc approval 10 Aug). Trades of 23 Aug (last T+3) and 24 Aug (first T+2) both settled 29 Aug (28 Aug was a holiday). Deadline 12:00 noon (1:00 pm until 11 Sep). Ex-date moves to one trading day before the record date. Mark-to-market window cut from three to two days | CN-2023-0031; CN-2023-0040; SCCP memos 04-0823, 06-0823[^pse-cn-2023-0031-t2-settlement:1-2][^pse-cn-2023-0040-t2-go-live:1-3][^sccp-memo-06-0823-sec-approval-t2-amendments:1] |
| 5 Mar 2024 | The settlement batch run may start before 12:00 once all cash and securities obligations are delivered, with 10 minutes' notice (SEC approval 9 Jan 2024) | SCCP memo 01-0324[^sccp-memo-01-0324-early-batch-run-effectivity:1] |
| 21 Jan 2025 | If SCCP cannot pay every member in full it settles price first (highest buy and lowest sell), then lowest quantity, then pseudo-random, with partial securities deliveries; this replaces "largest outstanding netted amounts first". Also: supplemental CTGF contributions with SEC approval; early delivery by SD-1 in five situations; a defaulter bears lost interest on Clearing Fund advances | SCCP memo 02-0125[^sccp-memo-02-0125-sec-approval-rules-3-4-5-1-4-6-2-8-7-6:1-3] |
| 8 Jul 2025 | CTGF refund requires regulatory clearances, all liabilities settled and audited proof that the member absorbed the contributions rather than collecting them from clients | SCCP memo 01-0725[^sccp-memo-01-0725-ctgf-refund-sec-approval:1-2] |

### Costs and taxes

| Effective | Change | Implementing document |
|---|---|---|
| 1 Jan 2018 | STT on listed shares 0.5% to 0.6% of gross selling price, seller-paid (TRAIN) | RA 10963; CN-2017-0082, -0084[^ra-10963-train:24][^ra-10963-train:54][^pse-cn-2017-0082-stt-increase-advisory:1][^pse-cn-2017-0084-stt-increase-effectivity:1] |
| 11 Sep 2020 | IPO tax (NIRC section 127(B): 4% / 2% / 1% of the gross selling price of closely held shares sold through an IPO) repealed, effective on publication (exact date not retrieved) | RA 11494 (Bayanihan II)[^ra-11494-bayanihan-ii:20][^ra-11494-bayanihan-ii:25] |
| 1 Jan 2021 | CREATE (approved 26 Mar 2021): income tax on non-resident foreign corporations 30% to 25% from 1 Jan 2021; final tax on their dividends 15% where the home country credits the tax, otherwise 25% (PSE's own page still shows 30%; Conflicts: F11) | RA 11534[^ra-11534-create:6][^ra-11534-create:11] |
| 18 Apr 2024 | Minimum broker commission removed: PSE's sliding 0.25%-0.05% minimum ceased; the 1.5% cap remains | SEC MC 7-2024 via CN-2024-0029[^pse-cn-2024-0029-min-commission-removal:1-3] |
| 2 Jan 2025 | Annual listing maintenance fee cap PHP 2.0m to PHP 3.5m per Main Board company (rate 1/100 of 1% of market capitalisation, floor PHP 250,000) | CN-2024-0068[^pse-cn-2024-0068-almf-effectivity:1] |
| 1 Jul 2025 | **STT 0.6% to 0.1%** on listed shares through a local exchange and, new, on domestic shares listed abroad; sale of listed shares exempt from DST; DST on original issue 1% to 0.75%. Applies to transactions made from 1 Jul 2025 | RA 12214 (CMEPA) sections 17, 29; CN-2025-0026, -0028; BIR RR 20-2025[^ra-12214-cmepa:16][^ra-12214-cmepa:25][^pse-cn-2025-0026-stt-decrease-advisory:1][^pse-cn-2025-0028-cmepa-effectivity:1][^bir-rr-20-2025-stt:4] |
| 4 and 15 Jul 2025 | BIR advisory: forms and eFPS lacked the new rate, so brokers file Form 2552 manually and pay at an authorised agent bank (later status not checked) | CN-2025-0032[^pse-cn-2025-0032-bir-stt-advisory:1] |
| 5 Aug 2025 | BIR RR 19-2025 (DST), RR 20-2025 (STT, signed 29 Jul, effective 1 Jul) and RR 21-2025 (CMEPA income-tax provisions) issued | BIR[^bir-rr-19-2025-dst:1][^bir-rr-20-2025-stt:1][^bir-rr-21-2025-cmepa-income:1] |
| 4 Sep 2025 | Brokers begin passing the 12% VAT on the PSE fee to clients (broker pages only; PSE's own illustration already showed VAT in 2024, so this is probably pass-through rather than a new levy: inference). Worth 0.06 bp per side | Broker fee pages[^firstmetrosec-fees-and-charges][^oecd-capital-market-review-philippines-2024:45] |

The exchange-side fees did not change in the window as far as found: PSE's 0.005% transaction fee appears in the 2018 and 2019 annual-report revenue notes and on PSE's 2026 page, and the SCCP fee is 1 bp, VAT-inclusive, in the 13 Mar 2018 rulebook and on PSE's 2026 page.[^pse-annual-report-2018:88][^pse-annual-report-2019:48][^sccp-clearing-house-rules-2018:62][^pse-web-investing-at-pse] The cost stack by regime, in basis points of gross value:

| Component | 2018 to 30 Jun 2025 | From 1 Jul 2025 |
|---|---|---|
| STT (seller only) | 60 | 10 |
| PSE fee (per side, plus 12% VAT) | 0.5 | 0.5 |
| SCCP clearing fee (per side, VAT-inclusive) | 1.0 | 1.0 |
| SEC "SRC fee" (per side; PSE's illustration and the OECD table list it, no primary rule for the rate found, several brokers do not itemise it: flag as secondary-only) | 0.5 | 0.5 |
| Commission (per side, plus 12% VAT) | Negotiated; minimum 0.25% to 0.05% until 17 Apr 2024; cap 1.5% | Negotiated; cap 1.5% |

<div class="callout">
<span class="label">Consequence: the STT cut is the largest cost discontinuity in the window</span>

Per side the stack, SRC fee included, is 1.12c + 2.06 bp (c = commission in bp), so a round trip costs 2.24c + 4.12 bp plus the seller tax. On PHP 10m at a 25 bp commission that is **120.12 bp (PHP 120,120) at 0.6% STT and 70.12 bp (PHP 70,120) at 0.1%**; the whole PHP 50,000 difference is the tax.[^pse-web-investing-at-pse] On the 2008 schedule, the latest found, a trade up to PHP 100m could not be priced below 25 bp before 18 Apr 2024, so a pre-2024 backtest needs the commission minimum as well as the tax rate (inference that the schedule was unchanged until then).[^pse-memo-2008-0467-minimum-commission-rates:2] A cost model spanning 1 Jul 2025 must switch the seller tax by trade date, not by calendar year. Details in [Chapter 12](#/ch/costs).
</div>

### Shorting, lending, market making and products

| Effective | Change | Implementing document |
|---|---|---|
| 5 Jun 2018 | SEC approves PSE Guidelines for Short Selling Transactions (PSEi members and ETFs eligible; short-interest ratio at or below 10%); effectivity left "in due course" and in fact took until 2 Oct 2023 | CN-2018-0035 (memo 22 Jun 2018)[^pse-cn-2018-0035-short-selling-guidelines-sec-approved:1-2] |
| 22 Jan 2019 | Short orders barred only in pre-open and pre-close (previously also run-off) | CN-2019-0004[^pse-cn-2019-0004-short-selling-guidelines-amendment:1] |
| 25 Feb 2020 | SEC-approved CMIC guidelines on securities lending and short selling take effect | CMIC memo 2020-005[^cmic-sbl-short-selling-guidelines:1] |
| 7 Feb 2020; 15 Jul 2020; 13 Aug 2020 | REIT regime: SEC approves the PSE Amended REIT Listing Rules and SEC REIT Rules (MC 1-2020); only "eligible" TPs may trade REITs; AREIT lists as the first REIT (eight listed since) | CN-2020-0005; CN-2020-0066; PSE listings page[^pse-cn-2020-0005-amended-reit-listing-rules:1][^sec-mc-1-2020-reit-irr:1][^pse-cn-2020-0066-reit-broker-eligibility:1-2][^pse-web-new-listings] |
| 24 May 2023 | SEC approves offshore collateral for SBL with at least one foreign party (cash in USD, EUR, JPY, GBP, AUD; OECD government debt rated BBB or better; constituents of WFE-member benchmark indices); PDTC approved as lending agent 21 Jul 2023 (called conditional in PSE's Oct 2023 deck; Conflicts: C19) | CN-2023-0027[^pse-cn-2023-0027-offshore-collateral-sbl:1][^pse-cn-2023-0048:2][^pse-sbl-short-selling-webinar-2023:3] |
| 2 Oct 2023 | Short Selling Guidelines declared effective; eligible set widened from PSEi and ETFs to PSEi, MidCap, Dividend Yield and ETFs; BIR (letter of 6 Sep 2023) accepts registration of a GMSLA with a foreign party | CN-2023-0048[^pse-cn-2023-0048:1-2][^pse-cn-2023-0048:8][^pse-pr-short-selling-effectivity-2023-10-02] |
| 6 Nov 2023 | Short-selling programme goes live (postponed from 23 Oct); TPs re-certify front-ends to tag short orders; the Daily Short Selling Report starts (53 eligible securities, all with zero volume) | CN-2023-0056[^pse-cn-2023-0056:1][^pse-dssr-2023-11-06:1-2] |
| 5 Jun 2024 | BIR RR 10-2024: MSLA/GMSLA approval retroacts to a complete submission; one registration for a multilateral MSLA with accession agreements; counterparties may switch lender and borrower roles | CN-2024-0035[^pse-cn-2024-0035:1-2] |
| 19 Dec 2025 | Alliance Global's warrants (AGIW; 2.2bn; PHP 12 exercise price) list, +100% on day one; warrants are exempt from the static price limit | PSE press release; Revised Trading Rules[^pse-press-agi-warrants][^pse-revised-trading-rules:20] |
| 25 Jan 2026 | SEC MC 1-2026 widens REIT eligible assets (indirect holdings through two-thirds-owned SPVs; toll roads, railways, airports, ICT, energy, data centres) | SEC MC 1-2026[^pse-analyst-briefing-3m-2026:17][^philstar-2026-07-17-sec-accomplishments] |
| 22 Apr and 6 May 2026 | PDTC Lending Agency Service onboards its first lenders and borrowers (cash collateral); PSE announces readiness (CN-2026-0022 is dated 6 May 2026 on its face; some sources give 18 May) | CN-2026-0022[^pse-cn-2026-0022:1-2] |
| 15 May 2026 | SEC approves PSE's 2026 Revised MSLA Guidelines, effective immediately: PSE is the one-stop shop for MSLA pre-clearance and BIR registration (PSE memo 22 May) | CN-2026-0025[^pse-cn-2026-0025:1] |

### Listing, minimum public ownership and indices

| Effective | Change | Implementing document |
|---|---|---|
| 19 Feb 2018 | PSEi and sector free-float floor 12% to 15%; recompositions move from March and September to February and August | CN-2018-0013, -0014[^pse-cn-2018-0013-index-policy-revision-2018:1][^pse-cn-2018-0014-index-recomposition-2018-02:1] |
| 3 Aug 2020 | IPO float by offer size: 33% or PHP 50M (market capitalisation to PHP 500M), 25% or PHP 100M (to PHP 1bn), 20% or PHP 250M (above); maintain at least 20%; listing by introduction and backdoor listing at least 20%. Superseded 11 Aug 2026 | CN-2020-0076[^pse-sr6-2-mpo-initial-backdoor-2020:1] |
| 21 Dec 2020 | Voluntary delisting needs two-thirds of the board (a majority, and at least two, of the independent directors) and of holders, with votes against at most 10%; minimum tender price is the higher of the fairness-opinion value and the one-year VWAP | CN-2020-0104[^pse-sr8-1-voluntary-delisting-2020:1] |
| 24 Mar 2021 | Main Board and SME Board listing rules recut; SME listing under a sponsor model; COVID profitability relief for IPO applications filed in 2021-2022 | CN-2021-0021[^pse-cn-2021-0021-amended-listing-rules:1-2] |
| 16 Aug 2021 | PSEi float floor 15% to 20% (first applied at the Dec 2022 review, so from the Feb 2023 recomposition; inference); early-inclusion provision; insert if ranked 25th or higher and delete if 36th or lower by full market capitalisation | CN-2021-0046[^pse-cn-2021-0046-index-policy-revision-2021:1] |
| 28 Mar 2022 | PSE MidCap and PSE Dividend Yield indices launched (20 members each) | CN-2022-0013[^pse-cn-2022-0013-launch-midcap-divy-indices:1-3] |
| 22 Jun 2022 | Backdoor-listing rules: PSE suspends trading on evaluating the disclosure and lifts the suspension one full trading day after the comprehensive disclosure; a one-hour halt follows disclosure of the final follow-on offer price | CN-2022-0026[^pse-sr7-backdoor-listing-2022:1][^pse-sr7-backdoor-listing-2022:4] |
| 26 Jan 2024 | Pension-fund, SSS and GSIS shares count as free float unless the fund holds a board seat (effective immediately; the review changes took effect 5 Feb) | CN-2024-0008[^pse-cn-2024-0008:1] |
| 5 Jan 2026 | Sector reclassification of 13 companies (a company is classified by the activity giving at least 60% of revenue) | CN-2025-0047[^pse-cn-2025-0047-sector-reclassification:1-2] |
| 3 Aug 2026 | PSEi: Maynilad in, Converge out; MidCap, Dividend Yield and sector changes; new PSE Portal live for back-office files | CN-2026-0035[^pse-cn-2026-0035:1][^pse-nte-faq-2026-08:2] |
| 11 Aug 2026 | **Amended MPO Rule** and Revised Public Ownership Guidelines effective immediately (SEC MC 11-2026): IPO float 33 / 25 / 20 / 15% by market capitalisation, REIT 33.33%, maintenance 20% (15% above PHP 50bn), possible relief to 12% for listings of PHP 200bn or more | PSE memo of 11 Aug 2026[^pse-amended-mpo-rule-2026-08:1-4] |
| 12 Aug 2026 | Preferred shares by IPO or direct listing: minimum offer PHP 100M (was PHP 1bn) and 100 holders (was 1,000); direct-listed preferreds tradable immediately | CN-2026-0037[^pse-cn-2026-0037-preferred-shares-rule-effectivity:1-2] |
| 31 Aug 2026 | MSCI Philippines drops Ayala Land (reported); the Standard index has 9 constituents on 30 Sep | MSCI factsheet; press[^newswav-2026-08-msci-ali][^msci-philippines-index-factsheet-2026-09:1-2] |

Smaller listing-rule changes: REIT listing amendments of 9 Mar 2023 (90% distribution policy, public-company status; CN-2023-0010) and a stabilisation fund of 10-15%, 12.5-15% or 15% of the base offer, by offer size, required for secondary offerings from 12 May 2023 (CN-2023-0022).[^pse-sr3-2-reit-listing-amend-2023:2][^pse-cn-2023-0022-stabilization-fund:1-2] Titles known only from the supplemental-rule index of the Jan 2025 compilation, with texts not read: CN-2019-0012 (listing fee framework) and -0013 (price-range disclosure for follow-on and rights offerings), CN-2020-0080 (SME lock-up), MEA-2022-0001 to -0003 (REIT, Local Small Investor and lock-up amendments, 13 Jun 2022) and CN-2023-0009 and -0012 (sponsor accreditation; listing of issued and outstanding shares).[^pse-listing-disclosure-rules:13-15]

### Ownership and access

| Effective | Change | Implementing document |
|---|---|---|
| 29 Oct 2018 | EO 65: 11th Regular Foreign Investment Negative List | EO 65[^lawphil-eo-65-2018] |
| 8 Jul 2019; 26 May 2020 | BSP lets ETFs (Circular 1030 of 5 Feb 2019) and non-resident investments in REIT securities be registered for repatriation through the banking system | CN-2019-0037; CN-2020-0052[^pse-cn-2019-0037-foreign-investment-etf:1][^pse-cn-2020-0052-nonresident-reit-investment:1] |
| 2 and 21 Mar 2022 | RA 11647 (Foreign Investments Act) and RA 11659 (Public Service Act): "public utility" limited to six categories (electricity distribution and transmission, petroleum pipelines, water and sewerage pipelines, seaports, public utility vehicles); effective 15 days after publication | RA 11647; RA 11659[^ra-11647-foreign-investments-act-amendments:8][^ra-11659-public-service-act-amendments:4][^ra-11659-public-service-act-amendments:14] |
| 27 Jun 2022 | EO 175: 12th negative list, replacing the 11th | EO 175[^eo-175-2022-12th-finl:1] |
| Aug 2023 | GCash "GStocks" retail access (announced 21 Sep 2022); over 1.7 million registered users by 2026 | PSE press release; PSE briefing[^pse-pr-gcash-gstocks-2022-09-21][^pse-analyst-briefing-3m-2026:21] |
| 11 Apr 2024 | BSP Circular 1192: equities listed onshore, ETFs and PDRs are registered when the registering agent bank reports them; no BSRD is issued for them (route read from the May 2025 manual) | BSP FX Manual[^bsp-fx-manual-morfxt-2025-05:42][^bsp-fx-manual-morfxt-2025-05:46] |
| 9 and 11 Aug 2025 | SEC MC 10-2025 (effective 9 Aug): Class A/B regular-board rule repealed; buyers receive the class bought from 11 Aug; articles to be amended by 9 Aug 2026; a trade that breaches a foreign-ownership limit is unwound at market the same day or at the next open | CN-2025-0035, -0036[^pse-cn-2025-0035-sec-declassification-mandate:1-3][^pse-cn-2025-0036-declassification-effectivity:1] |
| 13 Apr 2026 | EO 113: 13th negative list, effective 15 days after publication (reported as 1 or 2 May 2026) | EO 113; KPMG[^eo-113-2026-13th-finl:1-5][^kpmg-2026-04-13th-finl] |
| 10 Sep 2026 | PSE mechanics for each declassification: two-trading-day suspension before delisting; adjusted price equal to the higher of the A and B closes | Memo filed as 2026-0041[^pse-cn-2026-0041-declassification-price-suspension:1-2] |

### Incidents and corporate events

These matter as engine-replacement priors and as operational calendar risks; none changes a rule.

| Date | Event | Implementing document |
|---|---|---|
| 5 Oct 2018; 4 Jun 2019; 13 Jan 2020 | CMIC denies Meridian Securities access for one day (5 Oct 2018); trading halted from 11:45 for a fire drill, resumed 13:30 (4 Jun 2019); no trading or clearing for the Taal ash emission (13 Jan 2020) | CN-2018-0048; CN-2019-0031; CN-2020-0002[^pse-cn-2018-0048-cmic-denial-of-access-meridian:1][^pse-cn-2019-0031-trading-halt-fire-drill:1][^pse-cn-2020-0002-trading-suspension-2020-01-13:1] |
| 4 Jan 2022 | Trading cancelled for the day: the Nasdaq engine and the Flextrade front-end could not connect (43 of 125 TPs unable to connect) | CN-2022-0001, -0002[^pse-cn-2022-0001-delay-market-opening:1][^pse-cn-2022-0002-cancellation-of-trading-2022-01-04:1] |
| 26 Sep 2022; 24 Jul 2024 | Weather closures: no trading and no SCCP clearing (26 Sep 2022); no trading (24 Jul 2024) | CN-2022-0035; CN-2024-0038[^pse-cn-2022-0035-trading-suspension-2022-09-26:1][^pse-cn-2024-0038-trading-suspension-2024-07-24:1] |
| 3 Jan 2024 | Market halted 09:32 to 11:56 (third-party front-end provider); afternoon on schedule | CN-2024-0001, -0003[^pse-cn-2024-0001-market-halt:1][^pse-cn-2024-0003-update-market-halt:1] |
| 9 Dec 2024; 24 Mar 2025 | Late opens at 09:55 and 11:10; remaining phases unchanged | CN-2024-0061; CN-2025-0015[^pse-cn-2024-0061-adjusted-schedule-2024-12-09:1][^pse-cn-2025-0015-adjusted-schedule-2025-03-24:1] |
| 25 Mar 2024 to 17 Mar 2026 | EquitiWorld Securities: suspended as clearing member 25-27 Mar 2024; SEC involuntary suspension and preservation order 9-10 Oct 2024, then CMIC take-over (circular of Nov 2024, title only); SEC approves CMIC's liquidation and allocation plan 17 Mar 2026 | SCCP memo 03-0324; CN-2024-0053; CN-2026-0012[^sccp-memo-03-0324-clearing-member-suspension:1][^pse-cn-2024-0053-equitiworld-involuntary-suspension:1][^pse-web-announcements-archive][^pse-cn-2026-0012:1-2] |
| 26 Dec 2024 to 5 Mar 2026 | PSE buys control of PDS Holdings (61.92% at PHP 600 a share; stake 20.98% before, 94.55% at 5 Mar 2026) | PSE press release; briefing[^pse-pr-pds-acquisition-2024-12-26][^pse-analyst-briefing-3m-2026:25] |
| 9 Jul 2025; 13 Aug 2025; 31 Jul 2026 | CMIC involuntary suspensions of TPs for capital breaches: Globalinks (lifted 14 Oct 2025), Mount Peak, Benjamin Co Ca; client transfers only with CMIC approval | TPA-2025-0040, -0061, -0050; TPA-2026-0035[^pse-tpa-2025-0040-globalinks-involuntary-suspension:1-2][^pse-tpa-2025-0061-globalinks-lifting-of-suspension:1-2][^pse-tpa-2025-0050-mount-peak-involuntary-suspension:1-2][^pse-tpa-2026-0035-benjamin-co-ca-involuntary-suspension:1] |
| 19 Jan 2026 | EDGE outage; one-hour news halt of MRC Allied (09:30-10:30) | CN-2026-0004[^pse-cn-2026-0004-2-emergency-disclosures-trading-halt:1-2] |
| 3 Apr 2026; 31 Aug 2026 | Asian Terminals and Robinsons Retail delisted voluntarily after tender offers; PSE suspended each stock before removal (see [Chapter 2](#/ch/instruments) for the public-ownership mechanics) | CN-2026-0013; CN-2026-0038[^pse-cn-2026-0013-ati-voluntary-delisting:1][^pse-cn-2026-0038-rrhi-voluntary-delisting:1][^pse-tpa-2026-0012-block-sale-ati-tender-offer:1][^pse-cn-2026-0032-rrhi-index-removal:1] |
| 6 Oct 2026 | EDGE unavailable again (second time in 2026); PSE directs the public to its website; no trading-halt notice seen | CN-2026-0046[^pse-cn-2026-0046-edge-outage-access-to-disclosures:1] |

### Execution implications

- **"Close" has four regimes**: 15:30 (to 13 Mar 2020), 13:00 (Mar 2020 to Dec 2021), 15:00 (Dec 2021 to Feb 2024) and 15:15 (from 1 Mar 2024). Continuous trading ends at pre-close (15:15, then 12:45, then 14:45), so the last continuous print is not the official close. PSE's retained old timetable is the likeliest source of a wrong 15:30 assumption in post-2021 data (inference).
- **The 1 Jul 2025 tax cut is the biggest cost step; the 24 Aug 2023 move is the biggest calendar step.** Settlement and ex-date changed on the same day, so a corporate-action or cum/ex calendar spanning that date needs both switches.
- **SCCP rule changes arrive by memo, not as PSE trading-rule amendments.** Rule 2.3.5 (23 Aug 2023) matters for omnibus and prime-broker set-ups, the collateral list is re-set after each index review (which changes a broker's financing capacity in specific names), and the early batch run can release proceeds before noon. Re-read SCCP memos monthly; the posted rulebook is stale.[^sccp-memo-07-0823-sec-approved-amendments:2][^sccp-memo-01-0126-eligible-collateral-list:1]
- **Disclosure timing and the close moved in opposite directions.** The 4:00 pm cut-off lets company news be released 45 minutes after the 15:15 close and still count as same-day, so treat 15:15-16:00 as an information window with no continuous market (inference).
- **The -30% floor compounds**: two floor days is -51%, three is -66% (0.7 to the power n). Exit models for gap-down names must allow several sessions.
- **Outage priors:** four technical stoppages or late opens in 2022-2025, three of them in the third-party front-end or connectivity layer rather than the matching engine (inference).

## Version gates for backtests and replay

Key every gate on the trade date in Manila. Both tables are derived from the rows above; a gate is only as good as the document named beside it.

### Session timetable by period

Whole-day trading; times are Manila time. "n/l" = not listed in the document.

| Trade dates | Pre-open | No-cancel | Open | Recess / resume | Pre-close | Pre-close no-cancel | Run-off | Closing VWAP | Close |
|---|---|---|---|---|---|---|---|---|---|
| 4 Nov 2013 to 13 Mar 2020 | 09:00 | 09:15 | 09:30 | 12:00 / 13:30 | 15:15 | 15:18 | 15:20 | none | 15:30 |
| 16 Mar 2020; 19 Mar 2020 to 3 Dec 2021 | 09:00 | n/l | 09:30 | none | 12:45 | n/l | 12:50 | none | 13:00 |
| 6 Dec 2021 to 13 Jan 2022 | 09:00 | n/l | 09:30 | 12:00 / 13:00 | 14:45 | n/l | 14:50 | none | 15:00 |
| 14 Jan to 28 Feb 2022 | 09:00 | 09:15 | 09:30 | none | 12:45 | 12:48 | 12:50 | none | 13:00 |
| 1 Mar 2022 to 29 Feb 2024 | 09:00 | 09:15 | 09:30 | 12:00 / 13:00 | 14:45 | 14:48 | 14:50 | none | 15:00 |
| 1 Mar 2024 to now | 09:00 | 09:15 | 09:30 | 12:00 / 13:00 | 14:45 | 14:48 | 14:50 | 15:00-15:15 | 15:15 |

Sources by row: [^pse-memo-pre-close-schedule-2013:1][^pse-implementing-guidelines-trading-rules:4-5]; [^pse-cn-2020-0025-resumption-of-trading:1][^pse-cn-2020-0046:1][^pse-cn-2020-0051-gcq-floor-reopening:1]; [^pse-cn-2021-0059:1]; [^pse-cn-2022-0004:1]; [^pse-cn-2022-0009-trading-schedule-mar-2022:1]; [^pse-approved-rules-vwap-trading-2024:3]. No trading 17-18 Mar 2020 (CN-2020-0021). Half-day variants: 24 and 31 Dec 2021 (close 12:10) and the 2024 rule text (close 12:25). The 09:15 no-cancel phase in the 2013-2020 row is in the 2010 Implementing Guidelines timetable; later memos did not restate it, so it is carried forward (inference for 2013-2020).

### Gates by parameter

| Gate | Regime | Trade dates (inclusive) | Document |
|---|---|---|---|
| Seller tax (STT) | 0.5% | to 31 Dec 2017 | CN-2017-0082[^pse-cn-2017-0082-stt-increase-advisory:1] |
| | 0.6% | 1 Jan 2018 to 30 Jun 2025 | RA 10963[^ra-10963-train:24] |
| | 0.1% | from 1 Jul 2025 | RA 12214; CN-2025-0026[^ra-12214-cmepa:16][^pse-cn-2025-0026-stt-decrease-advisory:1] |
| Commission floor | Sliding minimum 0.25% to 0.05% | to 17 Apr 2024 | CN-2024-0029[^pse-cn-2024-0029-min-commission-removal:2] |
| | None (cap 1.5%) | from 18 Apr 2024 | SEC MC 7-2024[^pse-cn-2024-0029-min-commission-removal:1-3] |
| Dividend tax, non-resident corporations | 30% | to 31 Dec 2020 | RA 11534[^ra-11534-create:11] |
| | 25% (15% with home-country credit); the Act was approved 26 Mar 2021 and dates the rate 1 Jan 2021 | from 1 Jan 2021 | RA 11534[^ra-11534-create:11][^ra-11534-create:77] |
| IPO tax | 4% / 2% / 1% | to Sep 2020 | RA 8424[^ra-8424-nirc-1997:165-166] |
| | Repealed | from Sep 2020 (publication date not retrieved) | RA 11494[^ra-11494-bayanihan-ii:20] |
| Settlement cycle | T+3 | to 23 Aug 2023 | CN-2023-0031[^pse-cn-2023-0031-t2-settlement:1-2] |
| | T+2 | from 24 Aug 2023 | CN-2023-0040[^pse-cn-2023-0040-t2-go-live:1-3] |
| Ex-date | Three trading days before the record date (still printed in the Jan 2025 compilation) | ex-dates before 24 Aug 2023 | CLDR[^pse-listing-disclosure-rules:107] |
| | One trading day before the record date | ex-dates from 24 Aug 2023 | CN-2023-0031[^pse-cn-2023-0031-t2-settlement:1] |
| Static threshold | +50% / -50% | to 23 Mar 2020 | RTR[^pse-revised-trading-rules:20] |
| | +50% / -30% | from 24 Mar 2020 | CN-2020-0028[^pse-cn-2020-0028:1-2] |
| Index circuit breaker | PSEi -10% = 15-minute halt | to 3 May 2020 | CN-2020-0044[^pse-cn-2020-0044:1] |
| | -10% / -15% / -20% = 15 / 30 / 60 minutes | from 4 May 2020 | CN-2020-0044[^pse-cn-2020-0044:1-4] |
| System-failure halt trigger | One-third of TP users cannot access | to 19 Aug 2025 | CN-2025-0037[^pse-cn-2025-0037:1] |
| | TPs above 50% of six-month ADTV cannot trade; PAGASA rule | from 20 Aug 2025 | CN-2025-0037[^pse-cn-2025-0037:1-2][^pse-cn-2025-0037:4] |
| Closing VWAP session | None | to 29 Feb 2024 | CN-2024-0010[^pse-approved-rules-vwap-trading-2024:1] |
| | 15:00-15:15 | from 1 Mar 2024 | CN-2024-0012[^pse-cn-2024-0012-vwap-go-live:1] |
| Board lot and tick | One 15-band PHP table (no amendment found; PSE's own amendment list is not exhaustive) | to the last session before the NTE cut-over | RTR; CN-2025-0046[^pse-revised-trading-rules:21][^pse-cn-2025-0046-board-lot-trading-at-last:4][^pse-web-reg-trading-participants] |
| | Lot 1 and a 10-band tick table (not approved) | from 23 Nov 2026 if approved | CN-2025-0046[^pse-cn-2025-0046-board-lot-trading-at-last:3-5] |
| Short selling | Programme not operating | to 5 Nov 2023 | CN-2023-0056[^pse-cn-2023-0056:1] |
| | Operating (eligible list moves with each index review) | from 6 Nov 2023 | CN-2023-0056[^pse-cn-2023-0056:1] |
| EDGE same-day cut-off | Not established | before 1 Mar 2022 | n/a |
| | 3:30 pm | 1 Mar 2022 to 22 May 2026 | CN-2022-0010[^pse-cn-2022-0010-edge-cutoff-330pm:1] |
| | 4:00 pm | from 25 May 2026 | CN-2026-0024[^pse-cn-2026-0024-edge-cutoff-4pm:1] |
| Class A/B delivery | Either class | to 8 Aug 2025 (Mon 11 Aug is the first session under the new rule) | SEC MC 10-2025[^pse-cn-2025-0036-declassification-effectivity:1] |
| | Class bought | from 11 Aug 2025 | CN-2025-0036[^pse-cn-2025-0036-declassification-effectivity:1] |
| PSEi float floor | 12% | to Feb 2018 recomposition | CN-2018-0013[^pse-cn-2018-0013-index-policy-revision-2018:1] |
| | 15% | 19 Feb 2018 to the Feb 2023 recomposition (inference) | CN-2018-0013; CN-2021-0046[^pse-cn-2021-0046-index-policy-revision-2021:1] |
| | 20% | Feb 2023 recomposition to the Feb 2027 rebalance | CN-2021-0046[^pse-cn-2021-0046-index-policy-revision-2021:1] |
| | 20%, or 15% at PHP 250bn market capitalisation; MTAR, MADV and 98% screens (approved, not yet effective) | from the Feb 2027 rebalance | CN-2026-0033B[^pse-cn-2026-0033b:1][^pse-cn-2026-0033b:7-8] |
| IPO minimum public ownership | 10% | 1 Jan 2012 to about Nov 2017 (inference) | CN-2012-0003[^pse-sr6-mpo-rule-2012:1] |
| | 20%; tiers 33 / 25 / 20% from 3 Aug 2020 | about Dec 2017 to 10 Aug 2026 | SEC MC 13-2017; CN-2020-0076[^pse-sr6-2-mpo-initial-backdoor-2020:1-3] |
| | Tiers 33 / 25 / 20 / 15%; REIT 33.33% | from 11 Aug 2026 | PSE memo 11 Aug 2026[^pse-amended-mpo-rule-2026-08:2-4] |
| Foreign negative list | 11th (EO 65, signed 29 Oct 2018) | to the 12th | EO 65[^lawphil-eo-65-2018] |
| | 12th (EO 175, signed 27 Jun 2022) | to the 13th | EO 175[^eo-175-2022-12th-finl:1] |
| | 13th (EO 113, signed 13 Apr 2026; effective about 1-2 May) | from about 1-2 May 2026 | EO 113[^eo-113-2026-13th-finl:1-2] |
| Trading engine | PSEtrade XTS | 22 Jun 2015 to the last session before cut-over | AR 2015[^pse-annual-report-2015:42] |
| | Nasdaq Eqlipse (scheduled) | from 23 Nov 2026 | Broker forum[^pse-nte-broker-forum-2026-07-09:9] |

### Worked boundaries

- **STT straddle.** PSE keyed the new rate to the day the transaction is made ("transactions through the Exchange made on July 1, 2025 onwards"), so the trade date, not the settlement date, is the gate: a sale on Mon 30 Jun 2025 (settling Wed 2 Jul) is a 0.6% trade and a sale on Tue 1 Jul 2025 (settling Thu 3 Jul) a 0.1% trade (inference for the straddle case; no document addresses it).[^pse-cn-2025-0028-cmepa-effectivity:1]
- **T+2 transition.** Trades of Wed 23 Aug 2023 (T+3) and Thu 24 Aug 2023 (T+2) both settled Tue 29 Aug 2023, because Mon 28 Aug was National Heroes Day. A settlement-date model of the form "trade date plus N business days" is wrong for that week; take dates from SCCP memos.[^pse-cn-2023-0040-t2-go-live:1-3]
- **Ex-date arithmetic.** For a record date of Thu 15 Oct 2026 the ex-date is Wed 14 Oct and the last cum-date is Tue 13 Oct (a trade on the 13th settles T+2 on the record date). Under the old RD-3 convention the ex-date would have been Mon 12 Oct and the last cum-date Fri 9 Oct. The old convention carried a one-day buffer over the T+3 arithmetic, so the move to RD-1 shifted the ex-date two trading days closer to the record date (inference); on PSE EDGE, 457 of 502 dated records show the record date exactly one weekday after the ex-date, and a calendar-aware re-scan in [Chapter 10](#/ch/clearing-settlement) finds all 493 records with ex-dates from 20 Oct 2023 on the last trading day before the record date (the weekday exceptions are PSE closures and pre-T+2 entries).[^pse-cn-2023-0031-t2-settlement:1][^pse-edge-dividends-rights]
- **Close versus last print.** From 1 Mar 2024 Closing VWAP trades print between 15:00 and 15:15 at the day's VWAP, not at the closing price set in the 14:45 call, so "last print of the day" is not the close (inference; the XTS-era ITCH specification signals the close separately).[^pse-approved-rules-vwap-trading-2024:7][^pse-itch-equities-feed-spec-v2-3:27]

### Execution implications

- Implement every gate as a dated, table-driven configuration, not as code branches, and unit-test both sides of each boundary: 23/24 Mar 2020, 3/4 May 2020, 23/24 Aug 2023, 29 Feb/1 Mar 2024, 17/18 Apr 2024, 30 Jun/1 Jul 2025, 19/20 Aug 2025, 10/11 Aug 2025 and 22/25 May 2026.
- Carry an "as announced" flag beside "in force" so that pipeline items (Feb 2027 index policy, NTE lot and tick) can be switched on in a simulation without being confused with history.
- Reproduce the SCCP and BSP holiday pairing for settlement; the dynamic-threshold clusters and the collateral list change twice a year and need their own dated lists.

## Pipeline as of 6 Oct 2026

Status vocabulary: **in force**; **approved, not yet effective**; **awaiting SEC approval** (filed or "For SEC Approval"); **SEC exposure draft**; **consultation**; **RFI** (groundwork only); **slipped** (target missed, no new date); **not found**. The Eqlipse cut-over leads because five other rows depend on it.

### P1 to P21 at a glance

| ID | Item | Status on 6 Oct 2026 | Target | Evidence |
|---|---|---|---|---|
| P1 | **New Trading Engine (Nasdaq Eqlipse Trading, "NTE")**: new FIX, ITCH and market-data (MDF) specifications; big-bang cut-over with no parallel run; limit orders only on Day 1; new leased lines (at least two: production and UAT/DR) | Approved, not yet effective; schedule published; execution risk | Go-live **Mon 23 Nov 2026**; Saturday rehearsals 31 Oct, 7 Nov, 14 Nov. Earlier wording: "2026" (Dec 2025), "Q4 2026" (Jul-Aug 2026) | [^pse-nte-broker-forum-2026-07-09:4][^pse-nte-broker-forum-2026-07-09:9][^pse-nte-faq-2026-08:1-2][^pse-web-nte-page][^pse-cn-2025-0046-board-lot-trading-at-last:3] |
| P2 | **One Lot One Share and a new tick table**: lot 1 share for PHP and USD securities; PHP tick table cut from 15 to 10 bands; odd-lot market removed; TPs may set a minimum order value (not above the maximum commission) | **Awaiting SEC approval**: "awaiting SEC approval" (4 Jul 2026), "For SEC Approval" (17 Aug 2026); no approval found | Q4 2026 with the NTE | [^pse-cn-2025-0046-board-lot-trading-at-last:3-5][^pse-nte-user-group-2026-01-15:9-10][^pse-asm-2026-president-report:22][^pse-analyst-briefing-1h-2026:9] |
| P3 | **Run-off / trading-at-last change**: XTS rejects an incoming closing-price order when a better-priced passive order rests; Eqlipse accepts and matches it at the closing price; run-off orders may be entered, modified and executed only at the closing price | Proposed with P2; separate SEC status not stated | With the NTE | [^pse-cn-2025-0046-board-lot-trading-at-last:5][^pse-nte-user-group-2026-01-15:11-15][^pse-nte-broker-forum-2026-07-09:7] |
| P4 | **Negotiated Trades**: pre-arranged trades between different clients of one firm, price within +/-5% of the full-day VWAP, no size limit, 15-minute window after run-off, web-based, reported on the feed as news, counted in value and the CTF; does not replace block sales | Consultation 1-7 Jul 2026; "Revising per Public Comments" (17 Aug 2026) | With the NTE (design shown 9 Jul 2026) | [^pse-cn-2026-0031-negotiated-trades:1][^pse-cn-2026-0031-negotiated-trades:3][^pse-nte-broker-forum-2026-07-09:8][^pse-nte-faq-2026-08:1-2][^pse-analyst-briefing-1h-2026:9] |
| P5 | **PSETradeX** (PSE-hosted terminal): GTC and next-day validity removed; "Good Till 3 Months" for the cloud version; 2FA replaces the RSA token; 5,000 client accounts per broker; cloud migration deferred (9 Jul 2026) | Announced; timing of the GTC removal not restated | With the NTE (inference) | [^pse-nte-user-group-2026-01-15:17][^pse-nte-broker-forum-2026-07-09:11] |
| P6 | **Back-office files**: Daily Transactions Report retired; EOD files (ABC, CTF, unchanged specifications) through the new PSE Portal; Weekly Tax Report data only from 3 Aug 2026 | Portal live 3 Aug 2026; DTR retirement with the NTE | With the NTE | [^pse-nte-user-group-2026-01-15:19][^pse-nte-faq-2026-08:2][^pse-nte-broker-forum-2026-07-09:13] |
| P7 | **Revised PSE SBL rules**: directed pooled lending; SEC-registered onshore lending agent for foreign-lender/foreign-borrower deals; SBL report rationalisation | **Awaiting SEC approval** (consulted 3-18 Feb 2026; filed 16 Apr 2026) | None stated | [^pse-cn-2026-0009:1][^pse-pr-regulatory-reforms-2026-06-15][^pse-analyst-briefing-1h-2026:9] |
| P8 | **GPDR** (peso depositary receipts on foreign-listed securities) | **Awaiting SEC approval, slipped**: revised rules filed 24 Jun 2026, approval "targeted within the quarter" (by 30 Sep); no approval seen to 2 Oct | "2025" (Jul 2024), Q1 2025 (Oct 2024), first issuer "2H 2026" | [^pse-analyst-briefing-1h-2026:10][^pse-asm-2026-president-report:24][^pse-cn-2024-0047:1][^pse-annual-report-2025:38][^pse-asm-2024-presidents-report:25][^bworld-2024-10-23-gpdr-derivatives-targets] |
| P9 | **Market-making rules**: PSE general framework for all products with ETF and GPDR annexes (today ETFs only); SEC "Rules on Market Making" | Consultation, "Revising per Public Comments" (PSE, comments to 23 Jun 2026); **SEC exposure draft** (En Banc 13 Aug 2026, comments to 28 Aug; effective 15 days after publication) | None stated | [^pse-cn-2026-0026:1][^pse-cn-2026-0026:3][^pse-pr-market-making-2026-06-04][^pse-cn-2026-0039-sec-market-making-rfc:1-2] |
| P10 | **ETF rule amendments**: trust-type and actively managed ETFs, multiple sub-funds, issuer capitalisation PHP 250M to PHP 50M, single authorised participant | Consultation closed 30 Jun 2026; "Revising per Public Comments" | None stated | [^pse-cn-2026-0029-etf-amend-consult:1][^pse-analyst-briefing-1h-2026:16] |
| P11 | **Structured warrants** | **SEC exposure draft** (comments to 13 May 2026); PSE aligning its draft | None stated | [^pse-cn-2026-0018:1][^pse-analyst-briefing-1h-2026:10] |
| P12 | **Derivatives** (PSEi index futures first) | **RFI** to technology vendors (July 2026); funding talks; **slipped**, no launch date | "2026" (Jul 2024), "Q1 2026" (Oct 2024); FY2025 report: rules "slated to be finalized" in 2H 2026 | [^pse-analyst-briefing-1h-2026:10][^pse-asm-2026-president-report:24][^pse-annual-report-2025:38][^pse-asm-2024-presidents-report:25][^fow-2024-08-29-derivatives-2026] |
| P13 | **PSE index policy revision**: 98% cumulative market-capitalisation screen; MTAR and MADV liquidity tests; free-float floor 15% for market capitalisation of PHP 250bn or more | Approved, not yet effective | Feb 2027 rebalance (about Mon 1 Feb 2027; inference) | [^pse-cn-2026-0033b:1][^pse-cn-2026-0033b:7-8] |
| P14 | **Broker capital**: PSE proposes unimpaired paid-up capital of at least PHP 50M by 31 Dec 2027, surety bond PHP 12M to PHP 20M by 31 Dec 2028 for TPs under PHP 100M, PHP 100M by 31 Dec 2029; SEC draft of SRC Rules 28.1 and 33.1 | Consultation (PSE, to 31 Jul 2026); **SEC exposure draft** (En Banc 24 Sep, comments to 14 Oct 2026) | 2027-2029 | [^pse-memo-tp-paid-up-capital-increase-2026-07:3][^pse-memo-2026-10-01-sec-rfc-src-28-1-33-1-capital:1-2] |
| P15 | **SEC margin Rule 48.1 overhaul**: credit cap 50% to 60% of market value, maintenance 25% / 30% to 30%, PSE to write Exchange Margin Trading Rules | **SEC exposure draft** (En Banc 25 Aug 2026; comments to 15 Sep) | None stated | [^sec-rfq-2026-src-rule-48-1-margin:1][^sec-rfq-2026-src-rule-48-1-margin:9] |
| P16 | **SEC Capital Market Master Plan** (with ADB) and derivatives roadmap; strategic sandbox | In preparation; press report only, no document retrieved | 2030 horizon | [^philstar-2026-07-17-sec-accomplishments] |
| P17 | **SME Board and other listing rules**: sponsor-model amendments (CN-2026-0041, 28 Aug 2026); Green Equity Label consultation (CN-2026-0042) | Consultation | None stated | [^pse-analyst-briefing-1h-2026:16][^pse-web-announcements-archive] |
| P18 | **PDS integration**: consolidation of 13 systems; Phase 2 single post-trade system (clearing, settlement, depository), fixed-income collateral, wider Name-on-Central-Depository coverage; new PDTC depository system | In progress | Phase 2 target 2027 | [^pse-analyst-briefing-1h-2026:31][^pse-analyst-briefing-3m-2026:24] |
| P19 | **T+1 settlement; extended hours; fractional trading** | T+1 and extended hours: **not found**. Fractional trading: PSE's 2023 pipeline slide lists it with "Phase 1 to focus on amendment of board lot structure" (that is P2); no later phase, rules or date found | None | [^pse-asm-2023-presidents-report:40][^pse-analyst-briefing-1h-2026:9][^pse-annual-report-2025:38][^pse-asm-2025-presidents-report:30] |
| P20 | **MSCI and FTSE classification**: Philippines stays Emerging (MSCI) and Secondary Emerging (FTSE); MSCI's 2026 classification release did not mention the Philippines | No change known; FTSE outcome pending | FTSE announcement scheduled Tue 6 Oct 2026; MSCI November review date not retrieved | [^ftse-geis-ground-rules-2026-09:45][^ftse-country-classification-interim-2026-03:5][^ftse-equity-country-classification-page][^ladige-2026-06-msci-mcr] |
| P21 | **Consultations with no recorded outcome** | See the section below | None | n/a |

### The Eqlipse cut-over, 23 Nov 2026

**Schedule.** FEOMS certification 10-23 Sep 2026 (still possible later); pre-production connectivity 29 Sep-9 Oct; pre-production testing 12-22 Oct; Saturday rehearsals 31 Oct, 7 Nov and 14 Nov in the pre-production environment over the new production links; go-live Monday 23 Nov. PSE: "There will be no parallel runs ... a big bang approach."[^pse-nte-broker-forum-2026-07-09:9][^pse-nte-faq-2026-08:1]

**Readiness on 9 Jul 2026.** Of 40 TPs with their own front-end order management system: 18 were analysing and developing the FIX specification, 9 analysing but not developing, 2 had not started, 11 had not responded; for connectivity, 1 had completed testing, 3 were testing, 3 were installing lines, 17 were negotiating with telcos, 5 had not started and 11 had not responded. Market data (7 vendors and 21 TPs): 10 developing, 12 not started, 6 silent.[^pse-nte-broker-forum-2026-07-09:5][^pse-nte-broker-forum-2026-07-09:6] In August PSE said the new server addresses were "not yet available" and only point-to-point link tests were complete.[^pse-nte-faq-2026-08:3]

**Specifications.** FIX order entry, session gateway and drop copy v1.1 (8 Jun 2026); ITCH and MDF v1.2 (17 Jul 2026; the FAQ says final specifications were released 23 Jul, Conflicts: C11); ITCH and MDF run on separate SoupBinTCP sessions; cross trades carry a Cross Indicator; negotiated trades are published as news; the CTF and ABC file specifications do not change.[^pse-web-nte-page][^pse-nte-faq-2026-08:2-3] Whether execution reports carry broker identifiers or an anonymity switch is not public (Conflicts: F3).

| Rule | XTS (in force) | NTE (planned; not approved) |
|---|---|---|
| Lot size | 15 bands, 1,000,000 to 5 shares | 1 share, PHP and USD securities |
| Tick (PHP) | 15 bands, 0.0001 to 5.00 | 10 bands, 0.001 to 5; coarser below PHP 0.01 (0.0001 to 0.001), at PHP 0.10-0.249 (0.001 to 0.005) and at PHP 10-19.98 (0.02 to 0.05); finer at PHP 0.50-0.995 (0.01 to 0.005); other bands the same (a comparison made here, not a PSE statement) |
| Tick (USD) | Bands 0.01 to 1.00 | Merged bands, same ticks; lot 1 |
| Odd-lot market | Separate "O" book, continuous trading only | Abolished |
| Minimum order value | None | TPs may impose one, not above the maximum commission |
| Run-off at the closing price | Incoming order rejected if a better-priced passive order exists | Accepted and matched at the closing price; entry, modification and execution only at the closing price |
| Block and negotiated trades | Block sale at least PHP 20m within +/-5% of reference price | Block sales stay; Negotiated Trades add one-firm trades within +/-5% of VWAP, any size, 15 minutes after run-off |
| Order types | Market, limit, stop and stop-limit in the XTS FIX specification; more at rule level ([Chapter 4](#/ch/order-types))[^pse-fix-specification-v2-5:52] | Limit orders only on Day 1 |
| Validity (PSETradeX) | GTC and next-day available | GTC and next-day removed |
| Sessions, thresholds, circuit breakers | As in the snapshot | Not stated; no change announced |

Sources by row: [^pse-cn-2025-0046-board-lot-trading-at-last:3-5][^pse-nte-user-group-2026-01-15:9-10][^pse-nte-faq-2026-08:1][^pse-nte-broker-forum-2026-07-09:7-8][^pse-nte-user-group-2026-01-15:17].

<div class="callout infer">
<span class="label">Inference</span>

The tick change alters relative tick cost sharply at the bottom of the price range: a PHP 15.00 stock moves from a 0.02 tick (13.3 bp) to 0.05 (33.3 bp), and at PHP 10.00 from 20 bp to 50 bp, while its minimum order falls from PHP 1,500 (100 shares) to PHP 15 (one share). A PHP 0.50 stock moves the other way, from 0.01 (200 bp) to 0.005 (100 bp). Passive-fill economics, queue value and the spread floor change at the cut-over for those names; see [Chapter 4](#/ch/order-types) for the full tables.
</div>

<div class="callout warn">
<span class="label">Day-1 scope and approvals</span>

Only limit orders are supported on Day 1; any logic that relies on market, stop, market-on-open or market-on-close orders needs a marketable-limit replacement before 23 Nov.[^pse-nte-faq-2026-08:1] If the SEC has not approved One Lot One Share by then, PSE would either keep the existing lot table on the new engine or delay the engine, and its materials do not say which (inference). The NTE go-live depends on three things PSE does not control: SEC approval of P2-P4, broker front-end readiness and vendor-layer connectivity. No deferral had been announced on 6 Oct 2026.
</div>

### Track record: how PSE targets slip

| Item | Milestones | Lag |
|---|---|---|
| Short selling | SEC-approved guidelines 5 Jun 2018; effective 2 Oct 2023; live 6 Nov 2023, itself moved from 23 Oct | More than five years[^pse-cn-2018-0035-short-selling-guidelines-sec-approved:1][^pse-cn-2023-0048:1][^pse-cn-2023-0056:1] |
| GPDR | "Target Launch: 2025" (Jul 2024); Q1 2025 (Oct 2024); filed with the SEC Jan 2025; SEC comments 26 May 2025; revised rules filed 24 Jun 2026; still pending | Two missed targets[^pse-asm-2024-presidents-report:25][^bworld-2024-10-23-gpdr-derivatives-targets][^pse-asm-2025-presidents-report:30][^pse-annual-report-2025:38] |
| Derivatives | "Target Launch: 2026" (Jul 2024); "Q1 2026" (Oct 2024); "set to launch index futures" (Jul 2025); RFI Jul 2026; no date | Q1 2026 missed[^pse-asm-2024-presidents-report:25][^fow-2024-08-29-derivatives-2026][^pse-analyst-briefing-1h-2026:10] |
| Board lot | 2023 proposal filed with the SEC, "awaiting approval" Jul 2024, never approved; 2025 proposal tied to the NTE and awaiting approval | Not adopted in three years[^pse-cn-2023-0051:1][^pse-asm-2024-presidents-report:18][^pse-asm-2026-president-report:22] |
| Market-halt rule | Consulted May 2022; effective Aug 2025 | Three years[^pse-cn-2022-0020-market-halt-consultation:3][^pse-cn-2025-0037:1] |
| Counter-evidence | T+2 held its announced date (24 Aug 2023) once the SEC approved on 10 Aug; VWAP launched on the date announced (1 Mar 2024) | None[^pse-cn-2023-0040-t2-go-live:1][^pse-cn-2024-0012-vwap-go-live:1] |

<div class="callout infer">
<span class="label">Inference</span>

Treat 23 Nov 2026 as a target with execution risk until PSE confirms the rehearsal results. Dates held when the SEC had approved the rule and the date was announced after approval (T+2, VWAP); they slipped where SEC approval was the open item (short selling, GPDR, board lot). The Eqlipse date was announced before the approval it needs.
</div>

### Dated events to February 2027

| Date | Event | Why it matters |
|---|---|---|
| Tue 6 Oct 2026 | FTSE Russell's 2026 annual country-classification announcement scheduled; the Philippines is Secondary Emerging and the March watch list named only Egypt; FTSE page showed a "Document to follow" placeholder when checked | FTSE gives at least six months' notice before changing a classification[^ftse-country-classification-interim-2026-03:2][^ftse-country-classification-interim-2026-03:5][^ftse-geis-ground-rules-2026-09:9][^ftse-equity-country-classification-page] |
| 6-12 Oct 2026 | Mynt (GCASH) IPO offer period: up to 8.03bn shares at up to PHP 10.00; tentative listing 20 Oct (4 Jul deck: 19 Oct; Conflicts: C17) | Largest IPO to date if completed; retail subscriptions also through GStocks; supply and index-inclusion events follow[^pse-press-mynt-ipo-approval][^pse-asm-2026-president-report:8][^pse-analyst-briefing-1h-2026:13] |
| 12 Oct 2026 | Vitro REIT IPO (about PHP 24.19bn) scheduled to list | First large REIT under the 2026 SEC framework; REIT minimum public ownership 33.33%[^pse-asm-2026-president-report:8][^pse-analyst-briefing-1h-2026:13] |
| 12-22 Oct 2026 | NTE pre-production testing; rehearsals follow on 31 Oct, 7 Nov, 14 Nov | Last windows to certify front-end, FIX and ITCH changes[^pse-nte-broker-forum-2026-07-09:9] |
| 14 Oct 2026 | Comment deadline on the SEC's draft broker-dealer capital rules (SRC Rules 28.1, 33.1) | Counterparty-capital proposal (P14)[^pse-memo-2026-10-01-sec-rfc-src-28-1-33-1-capital:1-2] |
| 16-18 Nov 2026 | Whether PSE trades during the ASEAN Summit days is unresolved: CN-2026-0043 said "regular trading days", and CN-2026-0044 the same day withdrew it and promised a final advisory | The calendar service must allow either outcome; clearing follows BSP business days; the last rehearsal (Sat 14 Nov) falls just before[^pse-cn-2026-0043:1][^pse-trading-day-advisory-2026-11-16-18:1] |
| Mon 23 Nov 2026 | NTE go-live: no parallel run; limit orders only on Day 1; one-share lots and the new tick table only if SEC approval has arrived | Hard cut-over[^pse-nte-broker-forum-2026-07-09:9][^pse-nte-faq-2026-08:1] |
| Nov 2026 | BSP targets a soft launch of 22/7 Peso RTGS operations (22 hours a day, 7 days a week, not on nationwide holidays); SCCP had issued no corresponding memo through 11 Sep | Settlement cash leg; no change to SCCP cut-offs announced[^bsp-faqs-22x7-peso-rtgs-2026-07:1][^sccp-web-memos-index] |
| Nov 2026 | MSCI November index review (date not retrieved); FTSE's December review follows | Index implementation days have run at about 2x to 6x normal value ([Chapter 11](#/ch/market-data)); the first after the cut-over is a live test of the new run-off rule (inference)[^msci-philippines-index-factsheet-2026-09:1] |
| About Mon 1 Feb 2027 | First application of the revised PSE index policy (98% screen, MTAR and MADV tests, 15% float exception); recent February effective dates were the first Monday of the month and announcements 3-5 trading days earlier. The semiannual dynamic-threshold reset also falls about then (inference) | Index-flow positioning[^pse-cn-2026-0033b:1][^pse-cn-2026-0033b:7-8] |

### What was not found

- **No T+1 or other shorter settlement cycle.** None appears in PSE's decks of March, July and August 2026, the 2024-2026 President's reports, the FY2025 annual report, SCCP's memo index to 11 Sep 2026 or PSE's circular index to 6 Oct 2026; PSE's 10 Sep 2026 circular still calls T+2 "the standard" cycle.[^pse-analyst-briefing-3m-2026:14][^pse-annual-report-2025:38][^pse-cn-2026-0041-declassification-price-suspension:1][^sccp-web-memos-index] The SCCP system supports any cycle, so a later shortening would be technically cheap, but nothing has been proposed (inference).
- **No extended or after-hours session** for ordinary orders. The only segment after run-off is the 15-minute Closing VWAP session, with the Negotiated Trades window proposed inside it.[^pse-approved-rules-vwap-trading-2024:7][^pse-cn-2026-0031-negotiated-trades:3]
- **No fractional-share launch date or rules.** PSE's 2023 pipeline slide describes fractional trading (buying partial shares and trading by peso value) and says "Phase 1 to focus on amendment of board lot structure".[^pse-asm-2023-presidents-report:40] One Lot One Share is that first phase; no later phase, rule text or timeline has been found, and the lowest lot proposed is one share.
- **No statement** on whether static or dynamic thresholds, circuit breakers, order types beyond limit, or session times change with the NTE.
- **No SEC approval** on record for P2-P4, the algorithmic-trading article, the revised SBL rules or the GPDR rules.

### Execution implications

- **Plan a hard cut-over on 23 Nov 2026.** No fall-back engine, Day-1 limit orders only, new FIX, ITCH and MDF specifications, new production links. Freeze router changes before 14 Nov, use the three Saturdays, confirm each broker's certification and UAT status (many were not started on 9 Jul), keep a manual or kill-switch fallback and assume elevated incident risk in the first weeks.
- **Run three configurations behind date switches:** XTS as in force; NTE as approved (unknown until PSE publishes it); and NTE with the legacy lot and tick table, in case the SEC has not approved P2.
- **Closing strategies change.** Today a closing-price order meeting a better-priced passive order is rejected; under Eqlipse it matches at the closing price. Negotiated Trades (one firm, +/-5% of VWAP) share the 15-minute post-run-off window with Closing VWAP.
- **Day-1 order types:** replace market, stop and MOO/MOC logic with marketable limit orders; do not rely on GTC through PSETradeX.
- **Do not model instruments that do not exist:** GPDRs, structured warrants, index futures, market-maker incentives and broader ETFs.
- **Index calendar:** build the MTAR, MADV and 98% screens now for the first review under the revised policy; index events concentrate flow in few names (MSCI Philippines has nine).

## Consultations with no recorded outcome

PSE consultations whose adoption or rejection could not be found (P21). Silence in the public record is the finding; confirm with a broker before relying on either outcome.

| Consultation | Proposal | What was found |
|---|---|---|
| CN-2017-0060 (16 Oct 2017); CN-2018-0023 (10 Apr 2018) | State that PSE stays open on days when BSP or PCHC clearing is suspended, and on special non-working days in NCR, with SCCP "trading without settlement" guidelines | Adoption not found; the question returns with 16-18 Nov 2026[^pse-cn-2017-0060-proposed-amendments-trading-rules:1-2][^pse-cn-2018-0023-trading-without-settlement-proposal:1] |
| CN-2022-0045 (16 Nov 2022) | Make a disclosure-halt request voluntary and drop the automatic halt when an issuer fails to confirm or deny a rumour | Jan 2025 compilation still carries the old wording[^pse-cn-2022-0045-consultation-2022-part-ii:1][^pse-cn-2022-0045-consultation-2022-part-ii:4][^pse-listing-disclosure-rules:145] |
| CN-2023-0041 (25 Aug 2023) | Codify minimum public ownership by listing vintage, monthly public-ownership-report triggers, delisting vote basis | MPO levels restated in the 11 Aug 2026 rule; the voluntary-delisting changes are unconfirmed[^pse-cn-2023-0041-mpo-delisting-consult:1-3] |
| CN-2023-0043 (5 Sep 2023) | Allow algorithmic trading (parent order entered manually, limit child orders) and a VWAP facility | VWAP adopted (CN-2024-0010); no approval of the algorithmic article found[^pse-cn-2023-0043:2][^pse-cn-2023-0043:4] |
| CN-2023-0051 (9 Oct 2023) | Cut lot sizes so a PHP 100 minimum investment is possible (for example 1,000,000 to 20,000, 100 to 20 at PHP 5-9.99) | PSE's Jul 2024 report: "awaiting SEC approval"; never announced as approved; the Dec 2025 paper shows the old table as "existing" and proposes one-share lots, so treated as abandoned (inference)[^pse-cn-2023-0051:3-4][^pse-asm-2024-presidents-report:18][^pse-cn-2025-0046-board-lot-trading-at-last:4] |
| CN-2024-0048 (30 Sep 2024) | Extend the black-out rule to the issuer with a 30-day earnings black-out; cap the penalty for trading unlisted shares at PHP 50m; leave error-account liquidation to the TP with no one-month limit | Adoption not found; the Jan 2025 compilation shows the old text[^pse-cn-2024-0048-consultation-blackout-rule:1][^pse-cn-2024-0048-consultation-blackout-rule:4-5][^pse-cn-2024-0048-consultation-blackout-rule:9-10] |
| Mar 2025 (reported) | Temporary cut in the IPO public float from 20% to 15% with a follow-on within two to three years | Daily Tribune quoting PSE's CEO; no PSE circular; overtaken by the 11 Aug 2026 tiers[^tribune-pse-eases-float-2025] |
| SCCP memo 03-1121 (24 Nov 2021) | Draft "2022 Revised Clearinghouse Rules": new system terms, T+2, Rule 7.6, a CTGF order of application, a SCCP guarantee for conforming block sales | Parts adopted (later memos use its numbering: T+2, Rule 7.6, Annex 11); no consolidated approved text published; the block-sale guarantee has no adoption on record[^sccp-memo-03-1121-proposed-amendments:3-4][^sccp-memo-03-1121-proposed-amendments:16-17] |

## Conflicts and stale facts

C = the reform-timeline notes' conflict list; F = the cross-chapter flags. One resolution is used throughout the knowledge base.

| Ref | Topic | Conflict | Resolution used here |
|---|---|---|---|
| C1, F2 | "Pre-pandemic" schedule | CN-2021-0059 calls the 6 Dec 2021 timetable "pre-pandemic"; the 2012-Mar 2020 day resumed at 13:30 and closed at 15:30 | Give dated timetables; 6 Dec 2021 was a new, shorter day[^pse-cn-2021-0059:1][^pse-memo-pre-close-schedule-2013:1][^pse-cn-2020-0044:2] |
| C2, C5, C13, C14 | PSE web and index hygiene | "Investing at PSE" mixes current and stale tables; the announcement index has date typos ("June 30, 2027" for a 21 Jul 2026 memo; "August 13, 2036"; "6 Nov 2024" for the 2023 go-live); two circulars carry number 2026-0041; March 2025 notices are dated 24 Mar inside but listed under 31 Mar | The circular's own date and title govern; the index's second line (posting date) is usually right[^pse-web-investing-at-pse][^pse-web-announcements-archive][^pse-cn-2025-0015-adjusted-schedule-2025-03-24:1] |
| C3 | PSE SBL page | One FAQ says only PSEi and ETFs are eligible; CN-2023-0048 adds MidCap and Dividend Yield | CN-2023-0048[^pse-web-sbl-short-selling][^pse-cn-2023-0048:2] |
| C4, F10 | RA 12214 effectivity | lawphil transcription: 15 days after publication; signed PDF and BIR: 1 Jul 2025 | **1 Jul 2025**[^lawphil-ra-12214-2025][^ra-12214-cmepa:25][^bir-rr-20-2025-stt:4] |
| C6, C7, C16 | Press and index dates | Lower static threshold: PSE press page 16 Apr 2020, circular 21 Mar, effective 24 Mar; short-selling guidelines: index 22 Jul 2018, memo 22 Jun 2018 (SEC 5 Jun), "effective" 2 Oct 2023 versus "live" 6 Nov 2023; MSLA guidelines: SEC 15 May 2026, press 10 Jun | Use circular and memo dates; keep effective and go-live apart[^pse-pr-lower-static-threshold-2020][^pse-cn-2018-0035-short-selling-guidelines-sec-approved:1][^philstar-2026-06-10-sec-msla][^pse-cn-2026-0025:1] |
| C8 | 13th negative list effectivity | 15 days after publication: KPMG says 1 May 2026, another report 2 May | "About 1-2 May 2026"[^eo-113-2026-13th-finl:2][^kpmg-2026-04-13th-finl] |
| C9 | Foreign-ownership framing | MSCI (Jun 2026): all industries "in general" at 40%; the statutes and negative lists open several sectors | The per-issuer limit binds; most issuers carry 40% ([Chapter 14](#/ch/foreign-access))[^msci-accessibility-review-2026:43][^ra-11659-public-service-act-amendments:4] |
| C10, C11, C12 | NTE wording and dates | "2026" (Dec 2025), "Q4 2026" (decks), "Nov 23, 2026" (9 Jul); specs v1.2 dated 17 Jul on PSE's page, "released 23 Jul" in the FAQ; text extraction attaches "For SEC Approval" to the SBL item but the slide shows it on One Share One Lot | Only the last wording gives a date; read badges from the slide image[^pse-cn-2025-0046-board-lot-trading-at-last:3][^pse-nte-broker-forum-2026-07-09:9][^pse-web-nte-page][^pse-nte-faq-2026-08:2][^pse-analyst-briefing-1h-2026:9] |
| C15 | GPDR and derivatives targets | Oct 2024 press: GPDR Q1 2025, derivatives Q1 2026; Aug 2026: GPDR pending SEC, derivatives undated | The Aug 2026 PSE status[^bworld-2024-10-23-gpdr-derivatives-targets][^pse-analyst-briefing-1h-2026:10] |
| C17, F16 | Mynt listing date | 19 Oct (4 Jul deck) versus 20 Oct (18 Sep PSE release) | 20 Oct (later PSE release); check the final prospectus calendar[^pse-press-mynt-ipo-approval][^pse-asm-2026-president-report:8] |
| C18, C19, F17 | SBL enabling steps | BIR letter dated 6 Sep 2023; PSE's Oct 2023 deck gives 25 Sep as receipt on one slide; PDTC's lending-agent approval is "approval" (Jul 2024 report) or "conditional" (Oct 2023 deck) | 6 Sep is the letter date, 25 Sep PSE's receipt; treat PDTC approval as conditional, conditions not found[^pse-cn-2023-0048:2][^pse-sbl-short-selling-webinar-2023:3][^pse-asm-2024-presidents-report:24] |
| C20, F14 | SCCP allocation algorithm | Text extraction of the redlined memo shows the old "largest outstanding netted amounts first" wording beside the new rule | Price, then lowest quantity, then pseudo-random (21 Jan 2025); read amendment memos from the page image[^sccp-memo-02-0125-sec-approval-rules-3-4-5-1-4-6-2-8-7-6:1] |
| F1 | Ex-date | The Jan 2025 compilation prints RD-3; CN-2023-0031 sets RD-1 from 24 Aug 2023; all 493 EDGE dividend records with ex-dates from 20 Oct 2023 agree (calendar-aware scan, Chapter 10) | **RD-1 since 24 Aug 2023**; the compilation text is stale[^pse-listing-disclosure-rules:107][^pse-cn-2023-0031-t2-settlement:1][^pse-edge-dividends-rights] |
| F3 | Broker anonymity | Announced Jan 2014; on 3 Oct 2014 PSE said "not on Go-Live"; no activation found | Broker IDs appear on executions and trades, not on resting orders, unless anonymity is on; activation unconfirmed, evidence suggests IDs are visible[^pse-fix-itch-session-week01-2014-10-03:11][^pse-itch-equities-feed-spec-v2-3:25] |
| F4 | EDGE cut-off | Jan 2025 rules print 3:30 pm | **4:00 pm since 25 May 2026**[^pse-listing-disclosure-rules:139][^pse-cn-2026-0024-edge-cutoff-4pm:1] |
| F5 | Clearing members versus TPs | SCCP lists 125 clearing members (122 active, 3 suspended); PSE's directory lists 123 TPs (121 active, 2 suspended); an SCCP snapshot of 14 Sep 2025 showed 124 | Report each with its date and source; do not merge[^sccp-web-membership][^sccp-web-membership-2025-09-14][^pse-active-tp-summary-2026-07-20:1-6][^pse-web-tp-directory] |
| F6 | Block-sale settlement | The Implementing Guidelines say T+0; the market moved to T+2; no block-specific amendment found; SCCP's 2018 procedures exclude blocks and negotiated deals from CTGF, fails and collateral coverage | Unresolved; blocks sit outside the SCCP guarantee per the 2018 procedures[^pse-implementing-guidelines-trading-rules:23-24][^sccp-clearing-house-operating-procedures-2018:23] |
| F7 | Run-off amend and cancel | The ITCH state table allows no amend or cancel in trading-at-last; the Implementing Guidelines allow cancel | Conflicting; design for no-cancel[^pse-itch-equities-feed-spec-v2-3:10][^pse-implementing-guidelines-trading-rules:18] |
| F8 | Closing price when the pre-close does not cross | No public rule | Working assumption: last traded price (inference) |
| F9 | SRC fee and SIPF | No primary document for the 0.005% SRC fee; PSE's page and the OECD 2024 table list it; most broker pages do not itemise it; SIPF 0.001% appears on one broker page for block sales | Model with a secondary-only flag, stack shown with and without[^pse-web-investing-at-pse][^oecd-capital-market-review-philippines-2024:45][^bpi-trade-fees-faq] |
| F11 | Dividend tax, non-resident corporations | PSE's table shows the pre-2021 30% | 25% (CREATE), 15% on the tax-sparing route; PSE's table is stale[^ra-11534-create:11][^pse-web-investing-at-pse] |
| F12 | 16-18 Nov 2026 | PSE said "regular trading days", then withdrew it the same day | Open as of 6 Oct 2026[^pse-cn-2026-0043:1][^pse-trading-day-advisory-2026-11-16-18:1] |
| F13 | FTSE 2026 classification | Announcement scheduled 6 Oct 2026; not published at check time | Secondary Emerging, not on the watch list (Mar 2026 interim); outcome unknown[^ftse-country-classification-interim-2026-03:5][^ftse-equity-country-classification-page] |
| F15 | Circuit-breaker cut-offs | CN-2020-0044's clock times (14:55, 14:40, 14:10) are written for a 15:15 pre-close and were not republished for 14:45 | Unresolved; by subtraction 14:25 / 14:10 / 13:40 (inference)[^pse-cn-2020-0044:2] |
| F18 | SCCP rulebook currency | sccp.com.ph still posts the 13 Mar 2018 T+3 text | In-force text = that text plus memos to 8 Jul 2025 (reconstruction)[^sccp-web-rules-page][^sccp-clearing-house-rules-2018:1] |
| F19 | "T+2 aligns with the US and Canada" | PSE's FY2025 statements; the US and Canada moved to T+1 on 28 May 2024 | Stale PSE statement (general market knowledge)[^pse-audited-fs-2025:41] |
| F20 | Static-threshold rounding | Ceiling and floor appear to snap inward (ceiling down, floor up), from four data points | Inference; read the engine's own collars where available[^pse-itch-equities-feed-spec-v2-3:12] |

## What is not in the public record

- A **consolidated, current Revised Trading Rules and Implementing Guidelines**: the archived text is the 2010 base plus memos, and article and part numbers have drifted between memos.
- **SEC approval or effectivity** of One Lot One Share, the new tick table, odd-lot removal, the run-off change and Negotiated Trades; PSE's last status is 17 Aug 2026, and its circular index to 2 Oct shows no approval memo.
- **How the NTE treats** thresholds, circuit breakers, session phases, auction order types, throttles and cancel-on-disconnect: the Eqlipse FIX and ITCH/MDF specifications are released to participants only.
- **A PSE decision on 16-18 Nov 2026** and whether it interacts with the 23 Nov cut-over.
- **Outcome of the 2022-2024 consultations** listed above, and whether PSE has corrected its stale web FAQs.
- **Exact effective dates** of RA 11647, RA 11659, EO 175 and RA 11534 (each effective 15 days after a publication date that was not retrieved) and of EO 113 (1 or 2 May 2026).
- **Full texts** of the CMIC lending and short-selling guidelines beyond the cover memo, the BSP circulars behind the registration route, and the listing-rule memos known only by title.
- **FTSE's 6 Oct 2026 announcement** and MSCI's November 2026 review date.
- **Any T+1, extended-hours or fractional-share rule**, and SEC or SCCP statements on them.

## Re-verify after 6 Oct 2026

| Check | Where | Why |
|---|---|---|
| SEC approval or rejection of One Lot One Share, tick table, odd-lot removal, run-off change, Negotiated Trades | PSE circular index (`pse.com.ph/news-and-announcement-archive/`); the "Updates" tab of PSE's NTE page (`pse.com.ph/pse-new-trading-engine/`); SEC website | Decides the lot and tick regime on Day 1 |
| NTE go-live reaffirmed or deferred; rehearsal results of 31 Oct, 7 Nov, 14 Nov | PSE circulars and NTE page; your broker's certification status | A deferral keeps the XTS rules in force |
| NTE order-entry, validity and threshold behaviour | Eqlipse FIX and ITCH/MDF specifications through your broker | Not public; Day 1 is limit-only |
| 16-18 Nov 2026 trading status | PSE's "final advisory" promised by CN-2026-0044; BSP/PhilPaSS calendar | Trading and settlement calendar; sits between the last rehearsal and go-live |
| FTSE Russell 2026 annual country classification | FTSE Russell's equity country classification page (`lseg.com/en/ftse-russell/equity-country-classification`) | Reclassification risk; FTSE gives at least six months' notice |
| MSCI November 2026 review | MSCI announcement and PSE's holiday list (check whether the effective date is a PSE holiday) | Index-implementation volume and the first test of the new engine |
| SEC action on revised SBL rules, GPDR rules, market-making rules, ETF rules, structured warrants | PSE circulars; SEC website | Opens foreign borrowing, new instruments and market makers |
| SEC final Rule 48.1 (margin) and SRC Rules 28.1 and 33.1 (broker capital) | SEC website; PSE relays (comment deadlines 15 Sep and 14 Oct 2026) | Financing capacity and counterparty capital |
| Dynamic-threshold cluster list and SCCP collateral-eligible list | TPA circulars (next about Feb 2027); SCCP memo index (`sccp.com.ph/main/memos.html`; memo 01-0726 of 28 Jul 2026 not archived) | Both change twice a year |
| February 2027 PSEi review announcement | PSE circular late Jan 2027 | First review under the revised policy |
| Short-selling usage and eligibility | Daily Short Selling Report; PSE eligible-list page | Zero volume to date; the list moves with index reviews |
| Remaining A/B pairs after the 9 Aug 2026 deadline | PSE listed-company directory; PSE declassification circulars | Each carries a suspension and a price adjustment |
| EDGE availability and the 4:00 pm cut-off | PSE circulars; EDGE | Two outages in 2026; news-timing assumptions |
| Mynt and Vitro REIT listing dates and terms | PSE circulars; prospectuses | Large supply events under the new minimum-ownership tiers |
| BIR STT filing mechanics and any ETF or SBL ruling | BIR issuances; PSE relays | Post-CMEPA operational detail was interim in Jul 2025 |
