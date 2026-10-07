---
number: 0
slug: at-a-glance
title: PSE at a Glance
summary: "Parameter cheat sheet for PSE equities on 6 Oct 2026: timetable, ticks, controls, costs, settlement, access, what the 23 Nov Eqlipse cut-over may change, and ten things that break ported algorithms."
part: Start here
---

This is the one-sitting version of the knowledge base. Each row gives the rule in force on **6 October 2026**, its key source and the chapter that develops it. The rules are the June 2010 Revised Trading Rules plus dated circulars, running on PSEtrade XTS; PSE publishes no consolidated text, so memo numbers and dates are the stable keys.[^pse-revised-trading-rules:1][^pse-web-regulatory-framework]

Three facts frame the rest. There is one exchange, one central counterparty and one depository, so the problem is scheduling, broker choice and counterparty risk, not routing. Algorithms must run inside the broker's system, because the DMA rules bar them from a client's line.[^pse-dma-rules:7] And a new engine, Nasdaq Eqlipse ("NTE"), is scheduled to replace XTS on **Monday 23 November 2026** (big bang, no parallel run, limit orders only on Day 1) while the rule changes it was meant to carry had no SEC approval on record on 6 October.[^pse-nte-broker-forum-2026-07-09:9][^pse-nte-faq-2026-08:1][^pse-analyst-briefing-1h-2026:9]

<div class="callout warn">
<span class="label">Scheduled change: 23 Nov 2026, subject to SEC approval</span>

Every row below is the XTS-era rule set unless it says "proposed". No NTE parameter is in force; the last tables list what is pending and when. "No approval found" means not found, not not granted.
</div>

## Venue and liquidity

| Item | On 6 Oct 2026 | Detail |
|---|---|---|
| Chain | One exchange; SCCP (100% PSE) is the CCP; PDTC is the depository, inside the PDS Group, 94.55% owned by PSE since 4 Feb 2026.[^pse-annual-report-2025:9][^pse-17c-2026-02-04-pdic-pdshc-shares:3] | [Ch 1](#/ch/market-architecture) |
| Engine, access | PSEtrade XTS since 22 Jun 2015; broker-certified FEOMS or PSETradeX over FIX 5.0 SP1; DMA may not be used for algorithmic or high-frequency trading; no co-location, no published message limit.[^pse-annual-report-2015:42][^pse-fix-specification-v2-5:8][^pse-dma-rules:7] | [Ch 1](#/ch/market-architecture), [Ch 13](#/ch/regulatory-constraints) |
| Brokers | 123 participants (121 active); the top ten took 64.99% of broker-ranked value on 5 Oct 2026.[^pse-web-tp-directory][^pse-web-broker-ranking] | [Ch 1](#/ch/market-architecture) |
| Instruments | 387 live lines, 280 issuers: 285 common (including 8 REITs), 98 preferred, 2 PDRs, 1 warrant series, 1 ETF (FMETF); 65 suspended; no listed derivatives.[^pse-sec-frames-snapshot] | [Ch 2](#/ch/instruments) |
| Turnover | PHP 7.71bn a day in 2026 to 2 Oct (about US$120m); block sales were 18.4% of 2026 value; the top ten names are about 60% of regular value; the foreign ratio (share of trade sides) is 49.0%.[^pse-weekly-report-2026-10-02:1][^pse-dqr-2026-ytd-block-parse][^pse-dqr-dataset] | [Ch 15](#/ch/empirical) |
| Quote quality | Median end-of-day spread 31 bp for the ten most-traded names, 87 bp for ranks 61–100, 227 bp beyond (computed proxy); the PSEi closes at the day's high or low in 38% of sessions.[^pse-dqr-dataset][^pse-weekly-reports-dataset] | [Ch 15](#/ch/empirical) |
| Market making | None for any single stock; FMETF's maker owes a spread cap (ten ticks at its price) and five-lot quotes.[^pse-etf-rules:22-23] | [Ch 8](#/ch/market-making) |

## The trading day (PHT)

| PHT | Phase | Orders |
|---|---|---|
| 09:00 | Pre-open | Enter, amend, cancel; no matching |
| 09:15 | Pre-open no-cancel | Enter only |
| 09:30:00 | Open | Five-step uncross at the scheduled second; continuous trading follows |
| 12:00–13:00 | Recess | Nothing can be entered, amended or cancelled |
| 14:45 | Pre-close | Enter, amend, cancel |
| 14:48 | Pre-close no-cancel | Enter only |
| 14:50 | Run-off | Closing price struck; orders only at that price |
| 15:00–15:15 | Closing VWAP session | VWAP-only trades, at least PHP 500,000, one participant; no ordinary orders |
| 15:15 | Close | End of trading |

Source: RTR Article II as restated on 1 Feb 2024.[^pse-approved-rules-vwap-trading-2024:3][^pse-approved-rules-vwap-trading-2024:6] Detail: [Chapter 3](#/ch/sessions), [Chapter 6](#/ch/auctions).

- **Hard windows.** Last cancel or amend 09:14:59 and 14:47:59; nothing at all in the recess. The closing price is struck at 14:50, 25 minutes before the 15:15 close, so run-off flow cannot move it. The close was 15:30 until 13 Mar 2020, 13:00 in the 2020–22 shortened-hours periods and 15:00 until 29 Feb 2024; PSE's own web prose still prints stale hours.[^pse-cn-2022-0009-trading-schedule-mar-2022:1][^pse-cn-2024-0012-vwap-go-live:1][^pse-web-investing-at-pse]
- **Auction price.** Five steps: maximum matched volume; least unmatched; market pressure; nearest the reference (previous close at the open, last traded price at the close); the reference. No random end, no extension, no volatility auction; the indicative price is on ITCH Total View only, and PSE's six worked examples are test vectors.[^pse-implementing-guidelines-trading-rules:13-16][^pse-itch-equities-feed-spec-v2-3:17-18]
- **Run-off.** XTS rejects an incoming closing-price order if a better-priced passive order rests; the NTE draft accepts it and matches at the closing price. The closing price when the pre-close does not cross is not public.[^pse-cn-2025-0046-board-lot-trading-at-last:5]
- **Calendar.** Closures arrive by circular 4 to 25 days ahead; a PAGASA signal of 3 or higher over NCR at 06:00 cancels the day (since 20 Aug 2025); 16–18 Nov 2026 is unresolved (CN-2026-0043 withdrawn by CN-2026-0044).[^pse-cn-2025-0037:4-5][^pse-cn-2026-0043:1][^pse-trading-day-advisory-2026-11-16-18:1]

## Lots, ticks and the band-edge cliffs

| Reference price (PHP) | Tick | Lot (shares) | Tick at band floor (bp) |
|---|---|---|---|
| 0.0001–0.0099 | 0.0001 | 1,000,000 | 10,000 |
| 0.0100–0.0490 | 0.001 | 100,000 | 1,000 |
| 0.0500–0.2490 | 0.001 | 10,000 | 200 |
| 0.2500–0.4950 | 0.005 | 10,000 | 200 |
| 0.5000–4.9900 | 0.01 | 1,000 | 200 |
| 5.0000–9.9900 | 0.01 | 100 | 20 |
| 10.0000–19.9800 | 0.02 | 100 | 20 |
| 20.0000–49.9500 | 0.05 | 100 | 25 |
| 50.0000–99.9500 | 0.05 | 10 | 10 |
| 100.0000–199.9000 | 0.10 | 10 | 10 |
| 200.0000–499.8000 | 0.20 | 10 | 10 |
| 500.0000–999.5000 | 0.50 | 10 | 10 |
| 1,000–1,999 | 1.00 | 5 | 10 |
| 2,000–4,998 | 2.00 | 5 | 10 |
| 5,000 and up | 5.00 | 5 | 10 |

Source: RTR Article IV Section 8, unchanged since 26 Jul 2010.[^pse-revised-trading-rules:21] Lot and tick key on the previous (or adjusted) close, not the live price. The relative tick runs 4–25 bp above PHP 5 and jumps **2.5x at PHP 20, 500 and 5,000**, 2x at 0.50, 10, 100, 200, 1,000 and 2,000, 5x at 0.25 and 9.9x at 0.01: crossing a one-tick spread on PHP 10m costs PHP 5,005 (5.0 bp) at a 19.98 reference and PHP 12,500 (12.5 bp) at 20.00. Whether the engine applies the tick by reference or order price near an edge is unstated, so use prices valid under both. Odd lots (below one lot) trade only in a separate continuous-only book.[^pse-implementing-guidelines-trading-rules:19][^pse-implementing-guidelines-trading-rules:20] Proposed, not approved: lot 1, ten tick bands, no odd-lot market.[^pse-cn-2025-0046-board-lot-trading-at-last:3-5] Detail: [Chapter 4](#/ch/order-types/board-lots-and-tick-sizes).

## Orders, validity and priority

| Item | Rule | Detail |
|---|---|---|
| Types | Rulebook: limit, market, market-to-limit, stop and stop-limit, market-on-open/close, cross; XTS FIX lists market, limit, stop, stop-limit; **NTE Day 1: limit only**.[^pse-revised-trading-rules:21-23][^pse-fix-specification-v2-5:52][^pse-nte-faq-2026-08:1] | [Ch 4](#/ch/order-types) |
| Market order | Executes at the best bid or offer or last traded price, whichever is better; the remainder is "queued ... for immediate execution" (approved wording not public); unfilled at the open it reserves the stock.[^pse-revised-trading-rules:21-22][^pse-revised-trading-rules:33] | [Ch 4](#/ch/order-types) |
| Validity | Day, GTC, GTD, GTW, sliding (one year), fill-and-kill; fill-or-kill and Session exist only in FIX; PSETradeX is dropping GTC and next-day.[^pse-revised-trading-rules:22-23][^pse-nte-user-group-2026-01-15:17] | [Ch 4](#/ch/order-types) |
| Qualifiers | Iceberg shows at least 10% of quantity in board-lot multiples; minimum quantity is barred in auctions.[^pse-revised-trading-rules:23][^pse-implementing-guidelines-trading-rules:12] | [Ch 4](#/ch/order-types) |
| Priority | Price then time. Kept on a size decrease, validity change or account-code change; lost on a price or trigger change or size increase.[^pse-revised-trading-rules:24-25] | [Ch 4](#/ch/order-types/priority-and-amendments) |
| Cancel windows | None from 09:15, none after 14:48, none in the recess; run-off amend and cancel is contradicted, so design for none.[^pse-approved-rules-vwap-trading-2024:6][^pse-itch-equities-feed-spec-v2-3:10] | [Ch 4](#/ch/order-types), [Ch 6](#/ch/auctions) |
| Self-trades, disconnects | No self-trade prevention: a participant's counterpart order matches its own earlier order regardless of queue position; no documented cancel-on-disconnect; mass cancel only after a FEOMS or gateway failure.[^pse-revised-trading-rules:31][^pse-fix-specification-v2-5:14] | [Ch 5](#/ch/matching) |
| Exchange purge | The Exchange cancels resting orders on cash- or property-dividend ex-dates, adjusted-close actions and lot changes.[^pse-revised-trading-rules:25] | [Ch 10](#/ch/clearing-settlement) |
| Entry controls | Per-order value limit set by the participant under an unpublished Exchange cap; foreign buy orders are earmarked at entry.[^pse-implementing-guidelines-trading-rules:17][^pse-revised-trading-rules:17] | [Ch 4](#/ch/order-types), [Ch 14](#/ch/foreign-access) |

## Price controls

| Control | Rule | Detail |
|---|---|---|
| Static band | +50% / −30% of the reference price since 24 Mar 2020; lifted case by case; not for warrants.[^pse-cn-2020-0028:1-2] | [Ch 7](#/ch/price-controls) |
| Dynamic threshold | Cap on the jump from the last traded price: 20% (20 or fewer trades in six months), 15% (21–500), 10% (over 500); clusters of 62, 88 and 235 securities on the list of 7 Aug 2026, reset each Feb and Aug.[^pse-tpa-2026-0036-dynamic-threshold-review:1] | [Ch 7](#/ch/price-controls) |
| Freeze | A breaching order freezes the security for all: no posting, amending or cancelling until Market Control acts (about 5 minutes); a dynamic breach by an order at the best bid or offer, or by a cross, is auto-accepted and one in the 5 minutes before pre-close is auto-rejected; more than three a day per participant is a violation; no volatility auction.[^pse-implementing-guidelines-trading-rules:26] | [Ch 7](#/ch/price-controls) |
| Halt, suspension | A halt keeps resting orders (nothing matches); a suspension purges them; disclosure halts lift an hour after dissemination; a late cure resumes after 50 minutes suspended and 10 reserved (10:30).[^pse-implementing-guidelines-trading-rules:26-28][^pse-listing-disclosure-rules:140] | [Ch 7](#/ch/price-controls) |
| Circuit breaker | PSEi −10/−15/−20% from the previous close: 15/30/60-minute market halt, once per level per day; no trigger since 2020; clock cut-offs never restated for the 14:45 pre-close.[^pse-cn-2020-0044:2-4] | [Ch 7](#/ch/price-controls) |
| System failure, weather | Market halt if participants with over 50% of six-month ADTV (ex-block) cannot trade, even via a correspondent; PAGASA signal 3–5 over NCR at 06:00 cancels the day (since 20 Aug 2025).[^pse-cn-2025-0037:1-2][^pse-cn-2025-0037:4] | [Ch 7](#/ch/price-controls) |

## Blocks, crosses and the VWAP session

| Facility | Minimum | Price | Window and approval | Detail |
|---|---|---|---|---|
| Regular block sale | PHP 20m (dollar securities USD 500k) | Within ±5% of the previous or adjusted close, at most 4 decimals | Pre-open to run-off including the recess; apply before the run-off; Exchange decides in 30 minutes.[^pse-implementing-guidelines-trading-rules:23-25] | [Ch 5](#/ch/matching/block-sales) |
| Special block sale | PHP 50m (USD 1m) | Agreed; no band in the guidelines | COO approval, 2 working days; Market Control executes.[^pse-implementing-guidelines-trading-rules:23-24] | [Ch 5](#/ch/matching/block-sales) |
| Cross | None, but a block-eligible deal must be a block | Inside the best bid and offer; the closing price in the run-off | Continuous trading and run-off; different beneficial owners.[^pse-revised-trading-rules:31] | [Ch 5](#/ch/matching/crosses) |
| Closing VWAP trade | PHP 500,000 | Day's VWAP excluding blocks, crosses and odd lots | 15:00–15:15; one participant on both sides.[^pse-approved-rules-vwap-trading-2024:7] | [Ch 6](#/ch/auctions) |
| Negotiated Trades (proposed) | None | ±5% of the full-day VWAP | 15 minutes after run-off, one firm; "Revising per Public Comments".[^pse-cn-2026-0031-negotiated-trades:3][^pse-analyst-briefing-1h-2026:9] | [Ch 5](#/ch/matching) |

Blocks print outside a stock's own volume but inside headline turnover (18.4% of 2026 value). The guidelines say regular blocks settle T+0 while the market is T+2, and the 2018 SCCP procedures exclude blocks from the guarantee: unresolved.[^pse-eod-daily-quotation-2026-10-02:11][^pse-implementing-guidelines-trading-rules:24][^sccp-clearing-house-operating-procedures-2018:23] Detail: [Chapter 5](#/ch/matching).

## Settlement, cut-offs and the fail ladder

| Item | Rule | Detail |
|---|---|---|
| Cycle | T+2 since 24 Aug 2023 (T+3 before); settlement date follows the SCCP and BSP calendar; no T+1 plan found; SCCP's posted rulebook is still the 13 Mar 2018 T+3 text.[^pse-cn-2023-0040-t2-go-live:1-3][^sccp-clearing-house-rules-2018:1] | [Ch 10](#/ch/clearing-settlement) |
| Deadline | 12:00 noon on the settlement date for cash and securities; double-settlement days use 11:00 and 14:00 batches.[^sccp-memo-06-0823-sec-approval-t2-amendments:2][^sccp-memo-07-0823-sec-approved-amendments:7-8] | [Ch 10](#/ch/clearing-settlement) |
| Fail ladder | 12:00–14:00: PHP 1,000 + 0.125% of the fail; after 14:00: PHP 1,000 + 0.25% compounded daily; cure by 09:15 on SD+1; buy-in or sell-out at 10:00; cash close-out at the highest regular-lot price + 10%. A +5% buy-in on PHP 25m costs about 20 times the later fine.[^sccp-memo-06-0823-sec-approval-t2-amendments:2][^sccp-memo-06-0823-sec-approval-t2-amendments:4] | [Ch 10](#/ch/clearing-settlement/fails-buy-ins-and-penalties) |
| Collateral | Daily mark-to-market on two days of unsettled trades, due 12:00 next business day; haircuts 25% (PSEi, MidCap, Dividend Yield shares) and 35% (other eligible); no initial margin; early delivery by SD−1 at SCCP's call.[^sccp-memo-07-0823-sec-approved-amendments:3-4][^sccp-memo-02-0125-sec-approval-rules-3-4-5-1-4-6-2-8-7-6:3] | [Ch 10](#/ch/clearing-settlement) |
| Ex-date | One trading day before the record date since 24 Aug 2023; the Jan 2025 listing compilation still prints three.[^pse-cn-2023-0031-t2-settlement:1] | [Ch 10](#/ch/clearing-settlement/corporate-actions) |
| Custodians | Secondary only (Clearstream): pre-match 09:00 on SD−1, PHP funding 14:30 on SD−1, instruction by 09:35 on SD, no partial settlement.[^clearstream-ph-settlement-services][^clearstream-ph-settlement-times] | [Ch 10](#/ch/clearing-settlement) |

## Costs and taxes

| Per-side item (percent of gross value) | Rate | Detail |
|---|---|---|
| Commission | Negotiated; cap 1.5%; no minimum since 18 Apr 2024; plus 12% VAT.[^pse-cn-2024-0029-min-commission-removal:1] | [Ch 12](#/ch/costs) |
| PSE fee; SCCP fee | 0.005% plus VAT (0.56 bp); 0.01% (1.00 bp).[^pse-investing-at-pse] | [Ch 12](#/ch/costs) |
| SEC "SRC fee" | 0.005% (0.5 bp); secondary-only, so show figures with and without.[^pse-investing-at-pse] | [Ch 12](#/ch/costs) |
| Stock transaction tax | 0.1% of the gross selling price, seller only, by **trade date** from 1 Jul 2025 (0.6% from 1 Jan 2018).[^ra-12214-cmepa:16][^pse-cn-2025-0028-cmepa-effectivity:1] | [Ch 12](#/ch/costs) |

**Round trip: RT = 2.24c + 14.12 bp** for commission c in bp. PHP 10m at c = 25 bp costs PHP 70,120 (70.12 bp), against 120.12 bp before 1 Jul 2025, and 69.12 bp without the SRC fee. The tax is not netted for round trips: 20 turns a year is about 2% of capital in tax alone.[^bir-rr-20-2025-stt:2]

| Tax item | Rule | Detail |
|---|---|---|
| Listed-share gains | Tax on sale only; no capital-gains tax.[^ra-12214-cmepa:16] | [Ch 12](#/ch/costs/investor-level-taxes) |
| Cash dividends, non-resident corporation | 25%; 15% if the home country credits 10 points or taxes nothing; PSE's own page still says 30%.[^bir-rr-21-2025-cmepa-income:7][^bir-rr-21-2025-cmepa-income:8][^ra-11534-create:12] | [Ch 12](#/ch/costs/investor-level-taxes) |
| REIT dividends; PHP interest | 10%; 25%.[^bir-rr-21-2025-cmepa-income:7] | [Ch 12](#/ch/costs/investor-level-taxes) |
| Off-exchange transfers; lending | Off-exchange, the 15% net-gain tax and stamp tax apply instead (inference); borrowing and lending escape tax only with a BIR-registered securities lending agreement.[^bir-rr-21-2025-cmepa-income:4][^bir-rr-10-2006-sbl:4] | [Ch 12](#/ch/costs/investor-level-taxes) |

Detail: [Chapter 12](#/ch/costs).

## Foreign access

| Item | Rule | Detail |
|---|---|---|
| Limits | 218 of the 281 companies on PSE EDGE (about 93.5% of market capitalisation shown) at 40%; 46 at 100%; 15 at 0%; all eight REITs and FMETF at 40%.[^pse-edge-stock-data] | [Ch 14](#/ch/foreign-access) |
| Earmark | Valid foreign buy orders are earmarked at entry against the room; blocking others is a major violation.[^pse-revised-trading-rules:17][^pse-revised-trading-rules:37] | [Ch 14](#/ch/foreign-access/behaviour-at-the-limit) |
| Breach | Unwind at market the same day or at the next open, with SRC §54 penalties (since 9 Aug 2025).[^pse-cn-2025-0035-sec-declassification-mandate:3] | [Ch 14](#/ch/foreign-access/behaviour-at-the-limit) |
| Feed, flag | ITCH [f] shows shares available (signed); EDGE shows the limit, not the level; every account code carries a local or foreign flag.[^pse-itch-equities-feed-spec-v2-3:19-20][^pse-implementing-guidelines-trading-rules:21-22] | [Ch 14](#/ch/foreign-access) |
| BSP | Listed equities register through a registering bank, no BSRD; convert FX through an authorised bank; full repatriation; FX hedge notional no more than the exposure; no offshore peso market.[^bsp-fx-manual-morfxt-2025-05:46][^bsp-fx-manual-morfxt-2025-05:47][^bsp-fx-manual-morfxt-2025-05:73] | [Ch 14](#/ch/foreign-access) |
| Class A/B; indices | A/B shares are being abolished (five pairs unmerged); MSCI rates five accessibility criteria "−", including foreign-limit level, stock lending and short selling; FTSE: Secondary Emerging.[^pse-listed-company-directory-frame][^msci-accessibility-comparison-2026:5][^ftse-country-classification-interim-2026-03:5] | [Ch 14](#/ch/foreign-access) |

## Data, transparency and disclosure

| Item | Rule | Detail |
|---|---|---|
| Feeds | ITCH Total View is a full-depth market-by-order book with indicative auction prices; Basic is top of book; no running high, low or last; fills arrive without a price, so keep an order map.[^pse-itch-equities-feed-spec-v2-3:22-24][^pse-itch-equities-feed-spec-v2-3:28][^pse-itch-equities-feed-spec-v2-3:32] | [Ch 11](#/ch/market-data) |
| Broker IDs | Not on resting orders; on executions (passive and active) and trades unless anonymity is on, which PSE deferred on 3 Oct 2014 and nobody has found activated: assume visible.[^pse-itch-equities-feed-spec-v2-3:14-16][^pse-fix-itch-session-week01-2014-10-03:11] | [Ch 11](#/ch/market-data/broker-identifiers-and-information-leakage) |
| Fees | Non-display licence for automated trading USD 7,500 a quarter per legal entity; historical order book PHP 10,000 a day; real-time fees and latency not public.[^pse-non-display-usage-policy-2017:2-3][^pse-data-products-page] | [Ch 11](#/ch/market-data) |
| Disclosure | Material news within 10 minutes and before the media; EDGE same-day cut-off 4:00 pm since 25 May 2026 (3:30 pm before), 45 minutes after the close; EDGE failed on 19 Jan and 6 Oct 2026.[^pse-listing-disclosure-rules:139][^pse-cn-2026-0024-edge-cutoff-4pm:1][^pse-cn-2026-0046-edge-outage-access-to-disclosures:1] | [Ch 11](#/ch/market-data), [Ch 13](#/ch/regulatory-constraints) |

## Indices and index events

| Item | Fact | Detail |
|---|---|---|
| PSEi, Jan 2024 policy | 30 stocks, free-float weighted, uncapped; float at least 20%; liquidity top 25% by median daily value in 9 of 12 months; insert at rank 25 or better, delete at 36 or worse; reviews each Feb and Aug, announced 3–5 trading days ahead, effective a Monday.[^pse-index-policy-2024:5-9][^pse-index-policy-2024:13] | [Ch 11](#/ch/market-data) |
| PSEi, revised | 98% market-cap screen, MTAR and MADV liquidity tests, 15% float floor from PHP 250bn market capitalisation; from the Feb 2027 rebalance.[^pse-cn-2026-0033b:1] | [Ch 11](#/ch/market-data) |
| MSCI | Philippines Standard: 9 constituents, ICTSI 44.73%, USD 30.5bn (about 0.25% of MSCI EM); implementation days median 3.04x normal value, 11 of 12 at 2x or more, net foreign selling on 10 of 12 (computed).[^msci-philippines-index-factsheet-2026-09:1-2][^msci-em-index-factsheet-2026-09:2][^pse-daily-quotation-report-series] | [Ch 11](#/ch/market-data) |
| FTSE | Secondary Emerging; 2026 announcement due 6 Oct 2026, outcome unknown; third-Friday days about 2.1x normal.[^ftse-country-classification-interim-2026-03:2-5][^pse-daily-quotation-report-series] | [Ch 11](#/ch/market-data) |

## Shorting, lending, market making and hedges

| Item | Status | Detail |
|---|---|---|
| Short selling | Live since 6 Nov 2023 in 52 names; short-interest ratio at most 10%; uptick test; Day orders; none in pre-open, pre-close, odd lots or blocks; borrow before sale; zero volume to date.[^pse-short-selling-guidelines-2023-10:1][^pse-short-selling-guidelines-2023-10:2][^pse-dssr-2026-10-05:1-2] | [Ch 9](#/ch/short-selling) |
| Lending | Onshore PDTC pool onboarded first participants in Apr–May 2026, cash collateral only; agreement must be BIR-registered within 2 weeks (1 month if signed abroad); foreign-lender rules filed 16 Apr 2026, awaiting SEC.[^pse-cn-2026-0022:1-2][^pse-msla-clearance-guidelines-2026:2][^pse-analyst-briefing-1h-2026:9] | [Ch 9](#/ch/short-selling) |
| Margin | SRC Rule 48.1: 50% credit, 25% long and 30% short maintenance; a 60% draft was exposed on 25 Aug 2026.[^sec-2015-src-irr:165][^sec-rfq-2026-src-rule-48-1-margin:9] | [Ch 9](#/ch/short-selling) |
| Derivatives | None listed; index futures at request-for-information and funding stage; hedges are offshore.[^pse-analyst-briefing-1h-2026:10] | [Ch 9](#/ch/short-selling) |

## What is pending, with dates

| Item | Status on 6 Oct 2026 | Date | Detail |
|---|---|---|---|
| Nasdaq Eqlipse (NTE) | Scheduled: big bang, no parallel run, limit orders only on Day 1; pre-production testing 12–22 Oct.[^pse-nte-broker-forum-2026-07-09:9][^pse-nte-faq-2026-08:1] | **Mon 23 Nov 2026**; rehearsals Sat 31 Oct, 7 Nov, 14 Nov | [Ch 1](#/ch/market-architecture), [Ch 17](#/ch/reform-timeline/the-eqlipse-cut-over-23-nov-2026) |
| One Lot One Share, 10-band tick table, no odd-lot market | "For SEC Approval"; no approval circular found.[^pse-analyst-briefing-1h-2026:9][^pse-asm-2026-president-report:22] | Targeted with the NTE | [Ch 4](#/ch/order-types/one-lot-one-share-proposed) |
| Run-off change; Negotiated Trades | Proposed with the lot rule; Negotiated Trades "Revising per Public Comments".[^pse-cn-2025-0046-board-lot-trading-at-last:5][^pse-cn-2026-0031-negotiated-trades:3] | With the NTE | [Ch 6](#/ch/auctions), [Ch 5](#/ch/matching) |
| Foreign-lender SBL; GPDRs; market-making rules; ETF changes; structured warrants | Awaiting SEC approval or at exposure-draft stage; SEC market-making rules take effect 15 days after publication.[^pse-analyst-briefing-1h-2026:9][^pse-cn-2026-0039-sec-market-making-rfc:13] | No dates | [Ch 8](#/ch/market-making), [Ch 9](#/ch/short-selling) |
| SEC margin and broker-capital drafts | Rule 48.1 comments closed 15 Sep; SRC Rules 28.1 and 33.1 comments open.[^sec-rfq-2026-src-rule-48-1-margin:1][^pse-memo-2026-10-01-sec-rfc-src-28-1-33-1-capital:1-2] | 14 Oct 2026 | [Ch 9](#/ch/short-selling), [Ch 1](#/ch/market-architecture) |
| Trading status of 16–18 Nov | Unresolved; PSE's final advisory awaited.[^pse-trading-day-advisory-2026-11-16-18:1] | Before 16 Nov | [Ch 3](#/ch/sessions/trading-calendar) |
| BSP 22/7 peso RTGS | Soft launch targeted; no SCCP memo yet.[^bsp-faqs-22x7-peso-rtgs-2026-07:1-4] | Nov 2026 | [Ch 10](#/ch/clearing-settlement) |
| MSCI review; FTSE classification | MSCI date not retrieved; FTSE outcome unknown.[^ftse-country-classification-interim-2026-03:5] | Nov 2026; 6 Oct 2026 | [Ch 11](#/ch/market-data) |
| Revised PSEi policy | Approved, not yet effective.[^pse-cn-2026-0033b:1] | Feb 2027 rebalance (about Mon 1 Feb) | [Ch 11](#/ch/market-data) |
| Large listings | Vitro REIT (about PHP 24.19bn) and Mynt (about PHP 92bn).[^pse-asm-2026-president-report:8] | 12 Oct and 20 Oct 2026 | [Ch 2](#/ch/instruments) |
| Not found | T+1, extended hours, fractional trading, a derivatives date.[^pse-annual-report-2025:38] | None | [Ch 17](#/ch/reform-timeline) |

PSE's targets slip when SEC approval is the open item (short selling took over five years from approval to go-live) and held when the date followed approval (T+2, VWAP): treat 23 Nov as a target with execution risk (inference).[^pse-cn-2018-0035-short-selling-guidelines-sec-approved:1][^pse-cn-2023-0056:1][^pse-cn-2023-0040-t2-go-live:1] Full pipeline: [Chapter 17](#/ch/reform-timeline/pipeline-as-of-6-oct-2026).

## What is not in the public record

- The NTE FIX, ITCH and MDF specifications, and how the new engine treats thresholds, breakers, auctions and order types beyond limit.
- SEC approval or effectivity of the lot, tick, run-off and Negotiated Trades package.
- Whether executions carry broker IDs today; real-time data fees and latency.
- The per-order value limit, message-rate limits, cancel-on-disconnect behaviour and iceberg priority.
- Effective spreads, depth, intraday volume curves and the closing-auction share; any PSE-specific microstructure study.
- Institutional commission rates, borrow fees, post-2019 settlement statistics and the guarantee status of blocks.

## Ten things that break a ported algorithm

Each is developed, with its fix and sources, in [Chapter 16](#/ch/execution-implications/the-ten-things-that-break-a-ported-algorithm), which also covers [post-trade deadlines](#/ch/execution-implications/post-trade-operations), the [cost model](#/ch/execution-implications/cost-model) and the [table of what to switch on which circular](#/ch/execution-implications/version-gating-for-the-eqlipse-cut-over).

1. **Client-side algorithms cannot run on DMA**: host the schedule in the broker's certified front end; there is no co-location or published message limit ([hosting](#/ch/execution-implications/designing-the-order-placer)).
2. **Market orders do not sweep and Day 1 is limit-only**: use marketable limits priced inside the dynamic threshold ([order placer](#/ch/execution-implications/designing-the-order-placer)).
3. **A breach freezes the stock for everyone**, with no cancels for up to five minutes and no volatility auction ([risk checks](#/ch/execution-implications/price-control-aware-risk-checks)).
4. **The close is struck at 14:50, cancels stop at 14:48 and 15:00–15:15 is VWAP-only** ([auction and close](#/ch/execution-implications/auction-and-close-participation)).
5. **Tick and lot jump at band edges (2.5x at PHP 20, 500, 5,000) and the table may be rewritten on 23 Nov** ([order placer](#/ch/execution-implications/designing-the-order-placer)).
6. **Priority dies on repricing or upsizing, there is no self-trade prevention and ex-dates purge resting orders** ([order placer](#/ch/execution-implications/designing-the-order-placer)).
7. **Headline volume includes 18% blocks, event days run 2–6x and the close is often the day's extreme** ([scheduler](#/ch/execution-implications/designing-the-scheduler)).
8. **Fills carry your broker's code and news can land until 4:00 pm** ([information leakage](#/ch/execution-implications/information-leakage)).
9. **Resting foreign bids consume foreign room and a breach is force-sold at market** ([risk checks](#/ch/execution-implications/price-control-aware-risk-checks)).
10. **Shorting has never printed and hedges are offshore** ([shorting and hedging](#/ch/execution-implications/shorting-and-hedging-reality)).
