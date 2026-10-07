---
number: 11
slug: market-data
title: Market Data, Transparency and Indices
summary: A full-depth anonymous ITCH book whose fills probably carry broker codes, the published fees, EDGE timing, PSEi and MSCI/FTSE rules with rebalance-day volumes, and the feed change due 23 Nov 2026.
part: Post-trade and information
---

The PSE feed is more transparent than most frontier-market engineers expect and less convenient than they assume. ITCH Total View is a market-by-order book with a day-unique number on every resting order and live indicative auction prices, but it carries **no running statistics**, in Total View ordinary trades are **not** trade messages (only intentional crosses, block sales and manual trades arrive as Trade messages), and a resting order never shows its broker. Broker identity appears on **executions and trades**, subject to a "Broker Anonymity" switch that the exchange said in 2014 it would turn on "but not on Go-Live" and that no public document shows was ever turned on. For a fund, the safe assumption is that every fill prints the executing broker's code.

Information also reaches the market on the exchange's schedule, not yours. Corporate disclosures are posted through PSE EDGE with a **4:00 pm** same-day cut-off, 45 minutes after the 3:15 pm close, and index events dominate flow: MSCI Philippines Standard has only **nine** constituents, MSCI implementation days trade a median of about 3x normal value, and a PSEi addition rose 38.9% in one session. Two changes are pending and are flagged where they bite: the PSEi's revised methodology (from the February 2027 rebalance) and the new Nasdaq Eqlipse engine with new ITCH and MDF feeds (scheduled 23 November 2026). Everything about feeds below describes the PSEtrade XTS generation, specification v2.3.

## What the exchange feed shows

### The four ITCH feeds

The PSE sells four ITCH feeds on the XTS engine.[^pse-itch-equities-feed-spec-v2-3:22-24] They run on different ports.[^pse-fix-itch-session-week01-2014-10-03:10]

| Feed | Content | Depth | Application-form label |
|---|---|---|---|
| **Total View** | Every order and every execution on all listed equities: Add, Replace, Delete, Executed, Executed-with-Price, Broken Trade, Indicative Price/Quantity, Trade (cross/block/manual only) | **Full depth, market-by-order**; the spec describes no depth limit, the book is the sum of live Add and Replace orders[^pse-itch-equities-feed-spec-v2-3:22] | "Real Time with Order Book (Level 2)"[^pse-data-feed-application-form:2] |
| **Basic with Last Sale** | Best bid/offer price with the aggregated visible size at that price, plus **every** trade[^pse-itch-equities-feed-spec-v2-3:20][^pse-itch-equities-feed-spec-v2-3:23][^pse-itch-equities-feed-spec-v2-3:28] | **Top of book only**; on 3 Oct 2014 the PSE refused a 5-level BBO: "the standard for ITCH Basic is that only top of book is published"[^pse-fix-itch-session-week01-2014-10-03:10] | "Real Time Feed without Order Book (Level 1)"[^pse-data-feed-application-form:2] |
| **Index** | Index values (PSEi, All Shares, sector indices) and, at start of day, each index's member weights[^pse-itch-equities-feed-spec-v2-3:13][^pse-itch-equities-feed-spec-v2-3:24] | n/a | "Real Time Market Index"[^pse-data-feed-application-form:2] |
| **News** | Trading announcements, ETF iNAV (one item per minute), system events, company disclosures and exchange notices[^pse-itch-equities-feed-spec-v2-3:29-30][^pse-data-products-page] | n/a | "ITCH News"[^pse-data-feed-application-form:2] |

Transport is SoupBinTCP v3.0 point-to-point, with MoldUDP64 named for one-to-many multicast.[^pse-itch-equities-feed-spec-v2-3:7] Every message carries nanoseconds since the last seconds message ([T]), and a [T] is repeated each second in which messages flow.[^pse-itch-equities-feed-spec-v2-3:9][^pse-fix-itch-session-week06-2014-11-07:21] The specification is v2.3 of 5 October 2018, whose only change from v2.2 was the title-page logo; its last content change was v2.2 (19 Mar 2015, a NewsId clarification), and v2.1 (2 Mar 2015) added the company-disclosure news feed and the short-sell value B.[^pse-itch-equities-feed-spec-v2-3:3]

### Message set

| Msg | Name | Feeds | What matters for an implementation |
|---|---|---|---|
| T, S | Time stamp (seconds); System Event | all | [S] codes: O start of messages, S pre-open, R pre-open no-cancel, Q open, A/B break start/end, L pre-close, J pre-close no-cancel, P Trading At Last, M end of market hours, E end of trading, C end of messages[^pse-itch-equities-feed-spec-v2-3:10] |
| s, L, M, R, k | Trading schedule; price and quantity tick tables; Orderbook Directory; Restrictions | Total View and Basic at start of day ([R] also on News and Index) | [R]: orderbook id, ISIN, code, currency, group (N normal, O odd lot, I index), lot size, tick-table ids, price decimals, delisting date, instrument type (C common, P preferred, W warrant, E ETF, D PDR, I index), shares outstanding[^pse-itch-equities-feed-spec-v2-3:11-12]. [k]: short-sell eligible flag (Y, N and, since v2.1, B), high/low static collar, circuit-breaker limit up/down percentage[^pse-itch-equities-feed-spec-v2-3:12-13] |
| f | Foreign Shares Available | Total View | product code, ownership rule id, sign, shares available (see below)[^pse-itch-equities-feed-spec-v2-3:19-20][^pse-itch-equities-feed-spec-v2-3:22] |
| H | Orderbook Trading Action | Total View, Basic | T trading / V suspended, with reason N normal, S suspended by market control, F frozen (circuit breaker), H halted (intraday auction)[^pse-itch-equities-feed-spec-v2-3:13-14] |
| A | Add Order | Total View | day-unique order number, side, quantity, orderbook, price (0x7FFFFFFF = market order); **no broker field**[^pse-itch-equities-feed-spec-v2-3:14] |
| E / e | Order Executed | Total View | passive order number, executed quantity, match number; **no price and no orderbook**; [e] adds passive and active broker ID[^pse-itch-equities-feed-spec-v2-3:15] |
| C / c | Order Executed With Price | Total View | auction and post-freeze executions: order number, quantity, match number, Printable flag, price; [c] adds broker IDs[^pse-itch-equities-feed-spec-v2-3:15-16] |
| B, D, U | Broken Trade; Order Delete; Order Replace | Total View | [B] cites a match number (reason S, supervisory); [U] issues a **new** order number with the new open quantity and price[^pse-itch-equities-feed-spec-v2-3:16-17] |
| I | Indicative Price/Quantity | Total View | theoretical auction quantity and price, best bid, best offer; auction type O (opening), I (intraday/halt), C (closing)[^pse-itch-equities-feed-spec-v2-3:17-18] |
| P / p | Trade | Total View: cross, block, manual only. Basic: all trades | quantity, orderbook, Printable flag, price, match number, indicator (blank regular, C cross, B block, M manual); [p] adds buy and sell broker IDs[^pse-itch-equities-feed-spec-v2-3:18-19][^pse-itch-equities-feed-spec-v2-3:28] |
| O | BBO Quotation | Basic | best bid/offer price and aggregated **visible** shares[^pse-itch-equities-feed-spec-v2-3:20] |
| N | News Item | News | disclosures, notices, iNAV (below)[^pse-itch-equities-feed-spec-v2-3:20-21] |
| Y, Z | Index Member Directory; Index Value | Index | member weights at start of day; index levels[^pse-itch-equities-feed-spec-v2-3:13] |

Three in-band conventions are easy to miss. A reference price arrives as an [A] with order number 0 and quantity 0 (Total View) or as an [O] with both sizes 0x7FFFFFFFFFFFFFFF (Basic). The **close price** arrives as a [P]/[p] with quantity 0 and match number 0, sent immediately after the Trading At Last system event.[^pse-itch-equities-feed-spec-v2-3:27] And an incoming order that matches completely never produces an [A]; only the booked balance of an aggressor does, so the aggressor's size is visible only through the passive orders' [E]/[e] messages.[^pse-itch-equities-feed-spec-v2-3:28]

**Worked example: rebuilding a print.** A passive bid arrives as [A] order 1001, buy, 5,000 at 52.10. A seller hits it for 2,000: the feed sends [E] order 1001, quantity 2,000, match 7001, with no price and no orderbook. The print is 2,000 at 52.10, found by looking up order 1001 in your own order map (built from [A] and [U]); the remaining 3,000 is your decrement, not a message. If the owner then reprices, [U] retires order 1001 and issues a new number carrying the new open quantity and price.[^pse-itch-equities-feed-spec-v2-3:14-17] A Sec Code is derived from an [e] the same way: order number to [A], then orderbook to [R].[^pse-fix-itch-session-week06-2014-11-07:20]

### What ITCH does not carry

- **Statistics.** "ITCH does not publish running market statistics (high, low, last)"; subscribers track executions and trades.[^pse-itch-equities-feed-spec-v2-3:32] Volume must combine [E]/[e] and [C]/[c] with [P]/[p] (Total View sends [P]/[p] only for cross, block and manual trades), honour the Printable flag, and process [B] broken trades.[^pse-itch-equities-feed-spec-v2-3:15-19][^pse-itch-equities-feed-spec-v2-3:28]
- **Static fields.** In October 2014 the PSE listed 11 fields it could not put in ITCH: stock code, long and short names, previous close (LACP), par value, strike price, PN status, Shariah indicator, float level, capitalization adjustment coefficient and sector mapping; they were to be supplied in a daily file.[^pse-fix-itch-session-week01-2014-10-03:9] The current Securities Static Data file (v1.0, 22 Jun 2026; `securities_YYYYMMDD_HHMMSS.txt`, pipe-delimited, header row first) carries stock code, long and short names, sector and sub-sector, listing date, par value, LACP (last adjusted close) and a short-sell flag (B buy-back only, Y short sale and buy-back, N neither); the Index Member Static Data file (`indexmembers_YYYYMMDD_HHMMSS.txt`) carries only index code and security code.[^pse-securities-static-data-file:4-5][^pse-index-member-static-data-file:4-5] The ITCH Index feed adds member weights at start of day, and the PSE's Market Capitalization file carries float shares (below).
- **Market-maker or iceberg tags.** [A] has no such field. The spec says "visible" only for the aggregated size in [O]; whether [A] shows total or disclosed quantity for an order with hidden quantity is not stated. Test in the customer test environment.[^pse-itch-equities-feed-spec-v2-3:14][^pse-itch-equities-feed-spec-v2-3:20]

### Auction and halt transparency

[I] publishes the theoretical auction quantity, price, best bid and best offer during the opening auction (pre-open), the closing auction (pre-close) and halt auctions, with the auction type coded O, C or I.[^pse-itch-equities-feed-spec-v2-3:17-18] The system-event table states which actions each phase allows. The pre-open and pre-close no-cancel phases (codes R and J) allow entry only; Trading At Last (code P) allows entry and trading, not amendment or cancellation.[^pse-itch-equities-feed-spec-v2-3:10] The archived (2010) Implementing Guidelines, by contrast, say the trading participant "may cancel active Orders during Trading-at-Last/Run-Off Period".[^pse-implementing-guidelines-trading-rules:18] The two conflict and no later text resolves them, so design for no cancel (see [Chapter 6](#/ch/auctions)). A halt is signalled by [H] with state T and reason H, followed by the intraday auction, and lifted by [H] with T and N.[^pse-itch-equities-feed-spec-v2-3:14][^pse-itch-equities-feed-spec-v2-3:25-26] Session times are in [Chapter 3](#/ch/sessions); halt rules in [Chapter 7](#/ch/price-controls).

### The foreign-shares-available message

[f] gives, per product code and foreign-ownership rule id, the number of shares currently available to foreign investors, with an explicit sign (+ or minus) so that a negative balance can be expressed. It is a start-of-day reference message and also a dynamic one; product codes that do not allow foreign ownership send none.[^pse-itch-equities-feed-spec-v2-3:19-20][^pse-itch-equities-feed-spec-v2-3:25] It is the real-time input to any foreign-room check. The ownership limits themselves, how room is consumed and what happens at the cap are in [Chapter 14](#/ch/foreign-access); the spec does not say when the value goes negative. The PSE also sells a monthly Foreign Ownership Level report (Excel by e-mail), FTSE's index weighting applies a foreign-headroom test defined as (limit minus foreign holdings) divided by the limit, and MSCI's June 2026 accessibility review finds more than 1% of the MSCI Philippines IMI affected by low foreign room.[^pse-data-products-page][^ftse-geis-ground-rules-2026-09:13][^msci-accessibility-review-2026:43]

## Broker identifiers and information leakage

### What carries a broker code

| Where | What is identified | Condition |
|---|---|---|
| ITCH [A] Add Order | **Nothing**: no broker field[^pse-itch-equities-feed-spec-v2-3:14] | always |
| ITCH [e] / [c] | passive and active broker ID, 4-character alpha, blank if unset[^pse-itch-equities-feed-spec-v2-3:15-16] | sent when anonymity is **not** in force |
| ITCH [p] | buy broker ID and sell broker ID[^pse-itch-equities-feed-spec-v2-3:19] | sent when anonymity is **not** in force |
| ITCH [E] / [C] / [P] | no broker IDs[^pse-itch-equities-feed-spec-v2-3:25] | sent when anonymity **is** in force |
| Consolidated Trade File (to each broker, daily at close) | contra broker (3 digits), trader id, board (N normal, O odd lot, B block), local/foreign flag, principal/client flag, cross-trade indicator, short flag, investor id[^pse-consolidated-tp-file-spec-2015:1-2] | always, for the broker's own trades |
| FIX trade ExecutionReport | party role 17 = ContraFirm, 20 = contra give-up clearing firm[^pse-fix-specification-v2-5:21] | always |
| Daily Quotation Report (public, free) | no broker IDs; block sales listed by security, price, volume and value[^pse-dqr-2026-08-28:11] | always |

Which variant the feed sends depends on "whether the market is implementing Broker Anonymity or not, as announced by the exchange".[^pse-itch-equities-feed-spec-v2-3:25] Trader ids are eight characters: three-digit broker id, two digits for the front end (00 PSETradeX, 01 the broker's own front end) and a three-digit trader id.[^pse-fix-itch-session-week14-2015-02-13:16] Broker codes elsewhere are three-digit numbers,[^pse-psetradex-installation-guidelines:17] while the ITCH field is four characters; the mapping is not documented.

### The anonymity switch: what is on the record

| Date | Event |
|---|---|
| 27 Jan 2014 | A PSE media release, reported by Rappler, says the PSE will "start implementing broker anonymity" from March 2015, to attract participants, curb "herding" and tighten spreads. Stated practice at the time: broker IDs are not shown pre-trade or while orders queue; once orders match the executing brokers' IDs become visible. Two phases: from March 2014 only brokers and their systems see IDs on matched trades, from March 2015 IDs are anonymous to all (secondary source; no PSE document found)[^rappler-2014-01-27-broker-anonymity] |
| 12 May 2014 | A Philstar column (Philequity Corner) prints a reader's letter arguing that anonymity "may therefore highlight the information advantage that big hedge funds, foreign and local institutional investors already have against small retail investors" and that post-trade identities "compensate the less informed traders"; the column notes a reply by the PSE's COO dated 2 May 2014 (secondary)[^philstar-2014-05-12-fear-of-the-dark] |
| 4 Sep 2014 | ITCH spec v1.2: "Reinstate [C], [E], [P] messages for when Broker Anonymity is enforced"[^pse-itch-equities-feed-spec-v2-3:2] |
| 3 Oct 2014 | PSE Q&A: "We will implement broker anonymity but not on Go-Live. Hence, we included the messages in the final ITCH specs so vendors can just switch 'on' and 'off' broker anonymity feature so that no software release is needed once we decide to implement it."[^pse-fix-itch-session-week01-2014-10-03:11] |
| 22 Jun 2015 | PSEtrade XTS goes live[^pse-psetrade-xts-page] |
| Jan and Jul 2026 | Neither new-engine broker-forum deck lists broker anonymity among its "major changes" (lot size, tick size, run-off, negotiated trades); an absence, not a statement[^pse-nte-user-group-2026-01-15:9-11][^pse-nte-broker-forum-2026-07-09:7-8] |

<div class="callout warn">
<span class="label">Conflict: anonymity status is unconfirmed</span>

No PSE announcement was found, from 2015 to 6 October 2026, saying that anonymity was switched on, and the specification still describes both variants. The best-supported working state is **resting orders anonymous, executions and trades identified by broker**. That matches the PSE's 2014 statement of practice, the "not on Go-Live" answer, the unchanged 2018 specification, the contra-broker fields in the trade file and FIX, and a local broker's "Broker Activity" screen (tabs Ranking, Activity, Net Buying and Net Selling, Transactions; "All Market Data Provided by PSE", though the retrieved page was undated and showed zero values).[^philstocks-broker-activity] It is **not proven for 2026**. The decisive test is a vendor sample of ITCH [e]/[c]/[p] messages with non-blank broker fields.
</div>

<div class="callout infer">
<span class="label">Inference</span>

Because [e] and [c] carry both passive and active broker IDs, the tape reveals not only who traded but which side was resting, so aggressor-broker footprints can be reconstructed without any order-level attribution. Because [A], [U] and [D] carry order numbers, an algorithm can follow each resting order's life (refresh and cancel patterns) with no broker attribution, but cannot read queue ownership from broker codes.
</div>

### Execution implications

- **Treat broker routing as a disclosure decision.** Assume every fill prints your broker's code, on both the Total View tape and Basic, and that vendors and local brokers sell broker net-buy and net-sell analytics. A resting order is anonymous only until it fills: [e] and [c] name the **passive** broker too, so patient limit orders leak identity at each fill just as aggressive ones do. For a parent order of any size, split across several brokers and do not let one code carry a multi-day programme. The 2014 debate framed post-trade identities as compensating less-informed (retail) traders for institutions' information advantage; for a large fund that means it is the party being read (inference).[^philstar-2014-05-12-fear-of-the-dark]
- **Block, cross and negotiated routes remove the resting-order footprint, not the broker print.** They leave no resting order, and the public Daily Quotation Report lists blocks without brokers; but the specification publishes them on ITCH as [p] with buy and sell broker IDs unless anonymity is on (live practice for block prints is not documented).[^pse-itch-equities-feed-spec-v2-3:18-19][^pse-dqr-2026-08-28:11] Mechanics and limits are in [Chapter 5](#/ch/matching).
- **Pre-trade, you read order behaviour, not identities.** Order numbers give each order's life; do not build queue-reading logic on broker codes.
- **Test the anonymity state before and after the cutover.** Pull a day of [e]/[c]/[p] samples from a vendor and count non-blank broker fields; repeat on the new feed (see the section on the new-engine feeds below).

## Trade marking: block, cross, manual and odd-lot

| Trade type | Total View | Basic | Public end-of-day report | Trade file board / flags |
|---|---|---|---|---|
| Regular continuous | [E]/[e] on the passive order, [A] for any booked balance | [P]/[p], indicator blank | in normal-market totals | board N |
| Auction (open, close, halt) | [C]/[c] per executed order, Printable flag | [P]/[p] | in normal-market totals | board N |
| Intentional cross (the same user enters both sides) | [P]/[p], indicator **C** | [P]/[p], indicator C | cross trades are not listed separately | cross-trade indicator 1 (entered in the cross-order window); 0 = normal or auto-cross |
| Block sale | [P]/[p], indicator **B** | [P]/[p], indicator B | each block listed with security, price, volume, value; totals in "Block sale volume/value" | board B |
| Manual trade (market control) | [P]/[p], indicator **M** | [P]/[p], indicator M | not listed separately | n/a |
| Odd lot | separate orderbook, group **O** | separate orderbook | "Oddlot volume/value" | board O |
| Closing VWAP trade (since 1 Mar 2024) | not in the v2.3 spec, which predates the facility | not documented | "VWAP volume/value" and a VWAP list in the 2026 layout | not documented |

Sources: indicator values and which feed carries which trade;[^pse-itch-equities-feed-spec-v2-3:18][^pse-itch-equities-feed-spec-v2-3:28] the PSE's restatement during testing that cross trades and block sales "go to Trade[p]";[^pse-fix-itch-session-week06-2014-11-07:20] orderbook groups;[^pse-itch-equities-feed-spec-v2-3:11-12] the trade-file fields;[^pse-consolidated-tp-file-spec-2015:1-2] the public report layout.[^pse-dqr-2026-08-28:11-12] Block trades are reported by the trading participant through a FIX Trade Capture Report, the counterparty confirms or declines, and "the exchange confirms the Confirmed Trade to all involved parties".[^pse-fix-specification-v2-5:34-35] Because odd lots are separate instruments in the feed, a board-lot depth model must exclude group O; the new engine removes the odd-lot market (see the section on the new-engine feeds).

### The free public side: Daily Quotation Report

The Daily Quotation Report (DQR) is a free PDF published for each trading day at `documents.pse.com.ph/market_report/<Month DD, YYYY>-EOD.pdf`; the day is zero-padded (for example "February 02, 2026").[^pse-daily-quotation-report-series] Per issue it gives bid, ask, open, high, low, close, volume, value and net foreign buying or (selling); the closing pages give advances, declines, unchanged and traded issues, number of trades, odd-lot volume and value, block-sale volume and value with every block sale, VWAP volume and value with each VWAP trade, the sectoral summary, the PSEi and All Shares, the grand total, foreign buying, selling, net and total, and the list of securities under suspension.[^pse-dqr-2026-08-28:1][^pse-dqr-2026-08-28:11-12] The 2023 layout had no VWAP section and the grand total covered normal, odd-lot and block-sale trades only; the 2026 layout adds VWAP lines (the Closing VWAP facility began on 1 Mar 2024) and includes them in the total. Odd-lot, block and VWAP lines include dollar-denominated trades converted to pesos at the previous day's exchange rate.[^pse-dqr-2023-05-31:11-12][^pse-dqr-2026-08-28:11-12][^pse-cn-2024-0012-vwap-go-live:1] The PSE website also shows a one-day top-10 broker ranking by value (two-sided), with no history; broker concentration is in [Chapter 1](#/ch/market-architecture).[^pse-web-broker-ranking]

### Execution implications

- **Rebuild everything from messages.** Keep an order map from [A] and [U], apply [D], derive prints from [E]/[e]/[C]/[c] by lookup, add [P]/[p] for crosses, blocks and manual trades, and honour Printable and [B]. Reconcile your day totals against the DQR grand total each evening (normal, odd-lot, block and VWAP value; dollar-denominated trades are converted at the prior day's rate in the DQR, so expect small differences there).
- **Use Total View for any execution logic.** Basic is top of book only, so queue depth, imbalance, resting-size dynamics and closing-auction signals need Total View.
- **Join static data every morning.** Sector, LACP, par value and short-sell flag are not in the book feed; take them from the static-data and MCAP/PHIP files and reconcile with the DQR.
- **Keep separate books** for normal (N), odd-lot (O) and index (I) groups, and for dollar-denominated issues by currency in [R].
- **Closing signals.** During pre-close the [I] message gives the live indicative closing price and quantity; the session schedule is in [Chapter 3](#/ch/sessions) and the closing mechanics in [Chapter 6](#/ch/auctions).

## Data products, licensing and fees

### Product catalogue

| Product | What it is | Delivery | Fees published? |
|---|---|---|---|
| ITCH Total View, Basic, Index (real time) | the feeds above, "broadcast directly from the trading engine"[^pse-data-products-page] | direct from the PSE or through licensed data vendors | **No** (contact the Market Data Department) |
| ITCH News; Corporate Announcements Feed (CAF) | news items as documents are uploaded to EDGE[^pse-data-products-page] | ITCH [N]; CAF by e-mail and FTP (PDF and HTML) | No |
| Delayed data | "at least fifteen (15) minutes" delay[^pse-data-products-page] | **only** through licensed data vendors; the application form lists delayed feeds with and without order book[^pse-data-feed-application-form:2] | No |
| Non-display usage licence | real-time data used for automated trading or product creation where raw data is not displayed[^pse-data-products-page] | separate licence | **Yes** (below) |
| End-of-day files | Daily Quotation Report; Market Data EOD file (`PHIPyyyymmdd.txt`); Last Traded Price file; Market Capitalization file (`MCAPmmdd.txt`: close or last price, outstanding shares, market float shares = outstanding x float factor / 100, rounded up, so the float basis for replicating an index; inference)[^pse-data-products-page][^pse-eod-market-data-spec-v1-3:2][^pse-mcap-eod-spec-v1-0:2] | text files by FTP; also via vendors | No (historical list below) |
| Historical data | order-book and per-trade files, daily statistics, ownership, index members[^pse-data-products-page] | Excel/PDF on request | **Yes** (below) |
| Reports | monthly Foreign Ownership Level (Excel by e-mail); Weekly; Monthly; monthly Trading Participants Ranking[^pse-data-products-page] | e-mail | No |
| Trading-participant files (for brokers) | ABC report, Consolidated Trade File, Quote file (end-of-day security prices), Price file, Daily Transactions Report and Weekly Tax Report; downloaded via iPSE, moving to the new PSE Portal, and the Daily Transactions Report is discontinued with the new engine[^pse-psetrade-xts-page][^pse-nte-user-group-2026-01-15:19] | portal | No |
| Index services | **Index Licensing** (required for funds that track PSE indices: use of the index and trademarks, a complimentary end-of-day file of the licensed index, announcements of constituent, weight or float changes); **Index Bundle**; ETF Index Licensing for ETFs naming the PSE as index provider[^pse-data-products-page] | agreement; FTP; e-mail | Bundle only |
| Co-location and cross-connect | "for Trading Participants and Data Vendors"[^pse-data-products-page] | at the PSE | No |

### Published fees

| Item | Fee | Basis |
|---|---|---|
| Non-display (A) **Automated trading application** | **USD 7,500 per quarter** | per legal entity; affiliates and subsidiaries count separately; covers unlimited programmes in the category[^pse-non-display-usage-policy-2017:2-3] |
| Non-display (B) Derived data (index or product creation that cannot be reverse-engineered) | USD 7,500 per quarter | as above |
| Non-display (C) Other (funds administration, risk, portfolio valuation, quantitative analysis) | USD 900 per year | as above |
| Non-display one-time fee | waived | fees effective 1 Oct 2017 for existing end-users (policy announced 1 Jun 2017); new users licence on request[^pse-non-display-usage-policy-2017:1] |
| Index Bundle (PSEi end-of-day file by FTP, recomposition e-mails, quarterly free-float report) | USD 500 one-time + USD 500 per year, VAT exclusive | form version Jan 2019[^pse-index-subscription-bundle-form:1] |
| Historical **order-book data** (Excel, all securities) | **PHP 10,000 per day** | earliest 1998[^pse-data-products-page] |
| Historical **per-trade data** (Excel, all securities) | PHP 7,500 per day | earliest 1998 |
| Daily statistics (Excel): foreign buying and selling per security (from 1998); OHLC, volume, value, trades per security (from 1997); market indices OHLC per index (from 2007); total-market volume, value, trades (from 1998) | PHP 240 per series-year | |
| Market capitalization with outstanding shares and last price | PHP 320 per period-end | from 2008 |
| Daily Quotation Report PDF | PHP 100 per day | availability on request |
| Public ownership (all securities); list of index members per recomposition | PHP 720 per quarter (from 2006); PHP 160 per period-end (from 1994) | |
| Financial ratios / financial information | PHP 1,760 / PHP 1,680 per quarter | from 2006 |
| Listed Company Stock Feed (15-minute-delayed web service for issuers' own websites) | PHP 10,000 one-time + PHP 30,000 per year (PHP 45,000 for the XML+JSON bundle) | listed companies only[^pse-listed-company-stock-feed-brochure:2] |

Delayed and end-of-day data are not subject to the non-display fees, though the PSE asks to be told of any non-display use of them.[^pse-non-display-usage-policy-2017:1] The standard subscriber terms (end-of-day and historical forms) restrict use to personal or internal business use, prohibit redistribution including on web pages without a PSE-approved access-control mechanism, allow the PSE to amend fees on 30 days' written notice, and provide for fines and arbitration at the Philippine Dispute Resolution Center.[^pse-market-data-subscription-form:2] A Data License Agreement is required if raw data is displayed or redistributed; the data feed application form also asks about redistribution to clients, entitlement control, usage reporting and direct versus vendor connection.[^pse-non-display-usage-policy-2017:2][^pse-data-feed-application-form:1-3]

**Worked cost examples (arithmetic on the published fees).** One legal entity running algorithms on real-time data pays category (A) alone at 4 x USD 7,500 = **USD 30,000 a year**; adding a derived-data signal (B) makes USD 60,000; a fund group with three separate legal entities each running algorithms pays three times (A). These are the PSE's own recurring charges, before vendor, line and co-location costs. One year of historical order-book data, about 250 trading days at PHP 10,000, costs about **PHP 2.5m**, and per-trade data about PHP 1.9m; sampling event days is the economical route.

### Connectivity, vendors and what is not public

- **Connectivity (XTS era).** Leased line 1 Mbps minimum, 2 Mbps recommended; handover serial V.35 or Ethernet copper (recommended); a dropwire option for Ayala Tower 1 tenants.[^pse-psetrade-xts-page] The new-engine page lists a 100 Mbps dropwire for PSE Tower BGC tenants only and the same leased-line figures with Ethernet copper handover; at least two leased lines are required (production and UAT/disaster recovery).[^pse-new-trading-engine-page][^pse-nte-faq-2026-08:2]
- **Vendors.** The PSE keeps its vendor list "available upon request" and distinguishes Direct Data Vendors (connected to the PSE's market-data servers) from Indirect Data Vendors (supplied by direct vendors); seven data vendors were in the new-engine programme at 9 Jul 2026.[^pse-data-products-page][^pse-non-display-usage-policy-2017:1][^pse-nte-broker-forum-2026-07-09:6] ICE lists the PSE as streaming equity and index data including Level 1 and Level 2 pricing, with no fee or latency information; Bloomberg, LSEG and local-vendor product pages for the PSE were not found.[^ice-developer-pse]

<div class="callout">
<span class="label">What is not in the public record</span>

Real-time ITCH subscription fees, the vendor list and vendor fees, any PSE latency, throughput or SLA figure, whether the 2017 non-display fee schedule has been revised since (no later public policy found), and the fields of the historical order-book and per-trade files (including whether they carry broker IDs).[^pse-data-products-page][^pse-non-display-usage-policy-2017:2] The PSE's "Data Feed Infra" section for the new engine is marked "Coming Soon".[^pse-new-trading-engine-page]
</div>

### Execution implications

- **Budget the licence stack:** vendor or direct feed, non-display category (A) at USD 30,000 a year per legal entity (plus (B) for derived signals), line or co-location. Co-location and cross-connect are offered only to trading participants and data vendors, so a fund normally reaches the feed through its broker or a vendor.
- **Latency has no public benchmark.** Measure it from your own timestamps against the ITCH nanosecond offsets, and compare vendor and direct paths. The new engine's licensing (a sublicence for Nasdaq Eqlipse interfaces) may add terms that are not visible.[^pse-nte-user-group-2026-01-15:5]
- **Do not pay for history you can sample.** Event-day files cost the same as any other day; buy the days around index events and halts rather than a year.

## Corporate-disclosure dissemination: PSE EDGE

### Channels and timing

Corporate disclosures and PSE listing and disclosure notices have been filed through **PSE EDGE** (Electronic Disclosure Generation Technology) since 27 December 2013.[^pse-listing-disclosure-rules:138] A disclosure passes an approval step before release: listed companies may post it on their own sites "only upon receipt of the approval email from the Exchange or upon posting of the disclosures in the Exchange's website", and the CAF "Upload Date and Time Stamp" is "the date and time the disclosure and/or notice is approved for dissemination".[^pse-listing-disclosure-rules:138][^pse-caf-spec-v6-0:4]

| Effective | Same-day release cut-off | Source |
|---|---|---|
| 1 Mar 2022 to 22 May 2026 | **3:30 pm** ("until further notice"; set when the full five-hour day returned) | CN-2022-0010, 24 Feb 2022[^pse-cn-2022-0010-edge-cutoff-330pm:1] |
| **25 May 2026** onward | **4:00 pm**; disclosures received by then, "including end-of-day disclosures of exchange traded funds", are released the same trading day, later ones the next trading day; the submission system stays open after the cut-off | CN-2026-0024, 22 May 2026[^pse-cn-2026-0024-edge-cutoff-4pm:1] |

<div class="callout warn">
<span class="label">Stale text: the January 2025 rulebook prints 3:30 pm</span>

The Consolidated Listing and Disclosure Rules ("published as of January 2025") still state a 3:30 pm cut-off in Guidance Note 15.[^pse-listing-disclosure-rules:139] CN-2026-0024 supersedes it from 25 May 2026. With the market closing at 3:15 pm (since 1 Mar 2024),[^pse-approved-rules-vwap-trading-2024:3] same-day company news can now be released up to **45 minutes after the close** and still count as same-day; treat 15:15 to 16:00 as an information window with no continuous market.
</div>

| Channel | What it gives | Notes |
|---|---|---|
| **ITCH News [N]** | company disclosures and exchange notices submitted through EDGE; FirmId "EXCH"; Title = disclosure template name (for example "(4-34) Voluntary Trading Suspension", "(17-2) Quarterly Report", "MJIC - Trading Halt"); Reference = the EDGE URL; NewsText = reference number and timestamp; orderbook 0 for listing and disclosure notices[^pse-itch-equities-feed-spec-v2-3:30-31] | "Disclosures released when the trading engine is not available will be sent the next trading day"[^pse-itch-equities-feed-spec-v2-3:30] |
| **Corporate Announcements Feed (CAF)** | each announcement e-mailed (pipe-delimited subject: feed type, reference number, upload timestamp, title, symbol, form number) with a URL; an FTP folder holding the running 30 days; an end-of-day digest e-mail at about 6:30 to 8:30 pm[^pse-caf-spec-v6-0:3-7] | reference formats: structured CRnnnnn-yyyy, unstructured Cnnnnn-yyyy, listing notice LNnnnnn-yyyy, disclosure notice DNnnnnn-yyyy; spec v6.0 of 9 Sep 2019[^pse-caf-spec-v6-0:2-4] |
| **EDGE portal** | documents at `edge.pse.com.ph/openDiscViewer.do?edge_no=<id>` and `downloadPdf.do?edge_no=<encrypted>`[^pse-itch-equities-feed-spec-v2-3:30][^pse-caf-spec-v6-0:4] | **no public API** was found and no spec describes a query interface |
| PSE website announcements | circulars and company disclosures[^pse-web-announcements-archive] | the fall-back the PSE pointed to during both 2026 outages[^pse-cn-2026-0003-1-edge-unavailable:1][^pse-cn-2026-0046-edge-outage-access-to-disclosures:1] |

Template codes act as event types: unstructured disclosures are 4-xx (for example 4-30 Material Information/Transactions, 4-13 Clarification of News Reports, 4-32 Reply to Exchange's Query, 4-33 Voluntary Trading Halt, 4-34 Voluntary Trading Suspension), dividends 6-1 to 6-3, buy-backs 9-1, structured reports 17-xx (17-1 annual, 17-2 quarterly, 17-7 changes in beneficial ownership, 17-13 Foreign Ownership Report), POR-1 Public Ownership Report, and exchange notices DD-4 Trading Halt, DD-5 Trading Suspension, DD-6 Lifting of Trading Suspension, DD-10 Change in Stock Symbol.[^pse-caf-spec-v6-0:8-12] The list is as of the 2019 specification; templates added since are not in it.

### Issuer duties that set the timing

| Rule | Content |
|---|---|
| Material information (Art. VII Sec. 4.1) | disclose to the Exchange "within ten (10) minutes from the receipt of such information or the happening or occurrence of said act, development or event", **prior to release to the news media**; the original follows within 24 hours[^pse-listing-disclosure-rules:139] |
| Selective disclosure (Sec. 4.2) | prohibited unless disclosed simultaneously to the Exchange; exceptions for persons bound by confidence and persons who agree in writing to keep it confidential[^pse-listing-disclosure-rules:140-141] |
| Rumours (Sec. 4.5) | the Exchange may ask an issuer to confirm or deny; reply before the next pre-open if asked outside hours; on failure a trading halt follows that "shall be lifted at 10:00 a.m. even in the absence of any reply"[^pse-listing-disclosure-rules:145] |
| Material event in hours | the issuer "must request a halt in the trading of its shares"; if after hours and not disclosable before the next pre-open, it must also request a halt; "in both cases, the trading halt shall be lifted one (1) hour after the information has been disseminated"; if disseminated one hour or less before the close, the halt lifts the next trading day. Exceptions: soft information, or disclosure contrary to law[^pse-listing-disclosure-rules:140] |

In a "Trading Halt" orders other than cross transactions can still be posted, modified and cancelled; in a suspension they cannot.[^pse-listing-disclosure-rules:140] Additional-listing transactions that rely on the rights-offering exceptions carry a one-hour halt on announcement and another on dissemination of the Comprehensive Corporate Disclosure, due within five trading days.[^pse-listing-disclosure-rules:101-102] The Exchange can also halt on its own: on 19 January 2026 it imposed a one-hour halt on MRC Allied from 9:30 to 10:30 am after its disclosure of a 315m-share issuance.[^pse-cn-2026-0004-2-emergency-disclosures-trading-halt:1-2] A halt shows as [H] with T and H and re-opens through an intraday auction ([I], type I).[^pse-itch-equities-feed-spec-v2-3:14][^pse-itch-equities-feed-spec-v2-3:18] Halt mechanics are in [Chapter 7](#/ch/price-controls); whether the 15:15 close and the Closing VWAP session change the "one hour or less before the close" arithmetic is not documented.

### EDGE outages and the fall-back path

| Date | Event |
|---|---|
| 19 Jan 2026 | CN-2026-0003: "The PSE disclosure system is currently unavailable"; the public is told to check the PSE website, and issuers unable to reach EDGE may e-mail disclosure@pse.com.ph with the subject "Emergency Disclosure [stock symbol] - [template, e.g. 4-30 Material Information]"; CN-2026-0006 the same day: EDGE accessible again at edge.pse.com.ph; the MRC halt above was imposed the same day[^pse-cn-2026-0003-1-edge-unavailable:1][^pse-cn-2026-0006-edge-accessible:1] |
| **6 Oct 2026** | CN-2026-0046: "The PSE EDGE Portal is currently unavailable"; the public is directed to pse.com.ph for company disclosures. The PSE's announcements index shows company disclosures posted the same day; no trading-halt notice was seen and the resolution time was not checked[^pse-cn-2026-0046-edge-outage-access-to-disclosures:1][^pse-web-announcements-archive] |

Neither notice states when EDGE failed or recovered, so the outage window is not reconstructable from public documents.

### Execution implications

- **Subscribe to ITCH News or CAF; do not scrape EDGE.** Key the handler on the announcement reference number and treat the template code as the event type. The only machine-readable timestamps are the CAF approval time and the ITCH News arrival time; an event study should use those, not the template's "date of event". The public timestamp can lag the issuer's own filing time because release follows an approval step (inference).
- **After-close items need the CAF or the website.** ITCH News is carried by the trading engine and "will be sent the next trading day" when the engine is unavailable, so items released between the 3:15 pm close and the 4:00 pm cut-off are best taken from CAF e-mail or the PSE website (inference from the spec wording; the engine's end-of-day shutdown time is not published).
- **Pre-position for the 9:00 pre-open when news posts after 4:00 pm.** Submissions after the cut-off are posted the next trading day, so they reach the market with the pre-open order-entry window; an issuer that cannot file before pre-open must request a halt, so the open can be delayed until an hour after release (inference).
- **Expect a halt at a material in-hours release.** Halted books still accept orders and cancels (not crosses), and the engine publishes indicative prices for the halted book as an intraday auction (auction type `I`); the specification does not say whether an uncross runs when the halt is lifted ([Chapter 6](#/ch/auctions), [Chapter 7](#/ch/price-controls)). Inference: size and price for a possible uncross at the lift, not for continuous matching.
- **Run a second news path.** EDGE has failed twice in 2026 (19 Jan and 6 Oct); the PSE website and the e-mail emergency route were the fall-back.

## The PSEi and the PSE index family

### Index family and calculation

| Index | Members | Base | Calculation | Notes |
|---|---|---|---|---|
| **PSEi** | 30 | 1,022.045 at 28 Feb 1990; named "PSEi" since April 2006 | every minute (15-second base calculation, 60-second broadcast), two decimals | free-float-adjusted, **uncapped**; reviewed Feb and Aug[^pse-index-policy-2024:2-3][^pse-index-policy-2024:13][^pse-indices-page] |
| PSEi Total Return | same 30 | 1,000 at 28 Dec 2007; launched 4 Feb 2019 | end of trading day | cash dividends reinvested[^pse-indices-page] |
| Six sector indices | by sector | Financials 1,000 (14 Nov 1996); Industrial 1,422.20 (28 Feb 1990); Holding Firms 1,000 (29 Dec 2005); Property 1,000 (30 Sep 1994); Services 1,000 (29 Dec 2005); Mining & Oil 4,752.45 (28 Feb 1990) | free-float-adjusted | sector liquidity test: top 50% by median daily value in 8 of 12 months[^pse-index-policy-2024:3][^pse-index-policy-2024:7] |
| All Shares | all common stocks | 1,000 at 14 Nov 1996 | full market capitalization | SME board excluded[^pse-index-policy-2024:3] |
| MidCap; Dividend Yield (DivY) | 20 each | 1,000 at 30 Dec 2010; both launched 28 Mar 2022 | end of day | own policies; MidCap: top 35% median daily trade in 9 of 12 months and top 95% cumulative market cap; DivY: three-year average dividend yield[^pse-indices-page][^pse-midcap-index-policy-2024:3-4][^pse-divy-index-policy-2024:3-4] |

Calculation (January 2024 policy): "actual last traded prices" (how the closing-auction price feeds the index close is not described); index level = sum of (price x shares outstanding x free-float factor) divided by the base free-float capitalization, times the previous close, with adjustments for stock dividends, rights, splits and reverse splits; computed on the XTS engine and broadcast to members and vendors.[^pse-index-policy-2024:13-14] Errors above 0.10% are corrected only if discovered within 10 trading days; the correction is made the trading day after discovery and announced in the Daily Quotation Report, with vendors e-mailed.[^pse-index-policy-2024:14] At end-September 2025 the largest PSEi weight was ICTSI at 14.0%; sector weights were Financials 24.6%, Industrial 15.4%, Holding Firms 26.1%, Property 13.1%, Services 20.8% and Mining & Oil 0%, and the full market capitalization of the 30 stocks was PHP 8,588.8bn.[^pse-psei-factsheet-2025-09:2] Those weights are a year old and membership has changed; current weights and float factors are available only by subscription.

### Methodology in force: the January 2024 policy

<div class="callout warn">
<span class="label">In force today; replaced from the February 2027 rebalance</span>

The "Policy on Index Management" (January 2024 version) governs every review until the February 2027 rebalance. A revised policy announced on 21 July 2026 (CN-2026-0033, re-issued as CN-2026-0033B) takes over from that rebalance; its differences are tabulated below. The PSE's indices page still links the January 2024 policy and the September 2025 factsheets.[^pse-cn-2026-0033b:1][^pse-indices-page]
</div>

| Rule | January 2024 policy |
|---|---|
| Universe | main-board common stocks listed at least 12 months in the review period; foreign companies also listed abroad are not eligible for the PSEi (sector indices only); convertible preferreds, ETFs and funds, and dollar-denominated securities excluded; ineligible if likely untradable for a significant period in the next six months (delisting proceedings, suspension)[^pse-index-policy-2024:5] |
| **Free float** | at least **20%** of outstanding shares at the end of the 12-month review period (effective December 2022; 15% before); the Exchange may impose a higher level[^pse-index-policy-2024:5-6] |
| Deducted as strategic | founders, directors, officers and families; restricted or locked-up shares; treasury; employee ownership plans; affiliates; holders of 10% or more; controlling shareholders and voting trusts; pension and social-security funds (SSS, GSIS) **only when the fund holds a board seat** (clause amended by CN-2024-0008 on 26 Jan 2024, "effective immediately")[^pse-index-policy-2024:6][^pse-cn-2024-0008:1] |
| Counted as free float | PCD Nominee lodgements, PDR underlyings and overseas depositary-receipt underlyings unless the holder has 10% or more or is strategic; for dual-listed companies only shares traded on the PSE or held by locally domiciled investors; source: quarterly Public Ownership Reports[^pse-index-policy-2024:6-7] |
| **Liquidity** | median daily trading value of the regular board per month (zero-trade days included); a PSEi stock must rank in the **top 25% in 9 of the 12 months**; if fewer than 30 qualify, the Management Committee may widen the threshold in 5-point steps (30%, 35%...)[^pse-index-policy-2024:7] |
| Selection | eligible stocks ranked by **full** market capitalization at the 12-month VWAP (all share classes and PDRs combined); the 30 largest form the PSEi; financial criteria may be applied to new entrants[^pse-index-policy-2024:8] |
| **Buffers** | **insert at rank 25 or better**, replacing the lowest-ranked member; **delete at rank 36 or worse**, replaced by the highest-ranked eligible stock[^pse-index-policy-2024:9] |
| Review calendar | semi-annual: January to December data drives the February recomposition ("mid-February"), July to June data the August one ("mid-August"); announcement "as much as practicable, five trading days prior to their implementation" by press release and website memorandum[^pse-index-policy-2024:9] |
| Off-cycle removal | delisting, a corporate action that changes eligibility, or loss of a reliable price; replacement "simultaneously, no later than five (5) trading days from the announcement"[^pse-index-policy-2024:10] |
| Early inclusion | listed at least 6 months, rank 25 or better by market capitalization at the end of the review period, within the float rule, and in the top 20% by median daily trade for at least 6 months or 75% of the months listed, whichever is higher[^pse-index-policy-2024:10] |
| Mergers, suspension | the survivor stays; a suspended constituent may stay up to 10 business days at its last price, then the Management Committee decides; a removed stock waits for the next regular review[^pse-index-policy-2024:11] |
| Float and share updates | full float review at each semi-annual recomposition (end-December and end-June reports), whatever the size; float re-based on end-March and end-September reports, effective each **May and November**, only if the cumulative change is at least 5%; offerings reflected after an updated report; float adjustments effective within five trading days of announcement; a sector reclassification coincides with a membership change[^pse-index-policy-2024:11-12] |

### Policy history

| Date | Document | What changed |
|---|---|---|
| 12 Feb 2018 | CN-2018-0013 | PSEi float minimum **12% to 15%** (also applied to sector indices), made "in anticipation of the plan of the Securities and Exchange Commission to increase the minimum public ownership"; financial criteria for new PSEi and sector-index members; recomposition moved to **February and August** from March and September; effective with the Feb 2018 recomposition. The Feb 2018 text: insert if a stock "rises above the 25th position", delete if it "falls below the 35th position"; liquidity top 25% in 9 of 12 months; no early-inclusion rule[^pse-cn-2018-0013-index-policy-revision-2018:1][^pse-pr-2018-02-no-changes-float-15pct][^pse-index-policy-feb2018:5][^pse-index-policy-feb2018:7][^pse-index-policy-feb2018:9-11] |
| 5 Aug 2021 | CN-2021-0046 | float **15% to 20%**, to apply from the December 2022 index review (the Aug 2022 recomposition was "the last ... with a free float requirement of at least 15 percent"); a new **early-inclusion** provision; insertion at rank **25th or higher** and deletion at **36th or lower** by full market capitalization. The early-inclusion and rank rules were applied in the June 2021 review; changes effective Mon 16 Aug 2021[^pse-cn-2021-0046-index-policy-revision-2021:1][^pse-pr-2022-08-semirara-in-security-bank-out] |
| 28 Mar 2022 | n/a | MidCap and Dividend Yield indices launched[^pse-indices-page] |
| 26 Jan 2024 | CN-2024-0008 | pension and social-security fund shares are strategic only where the fund holds a board seat; the January 2024 policy text incorporates it[^pse-cn-2024-0008:1] |
| 21 Jul 2026 | CN-2026-0033 / 0033B | revised policy, applied from the February 2027 rebalance (below)[^pse-cn-2026-0033b:1] |

A press account headlines the July 2026 revision as the biggest overhaul "in 15 years", replacing rules that "had largely remained unchanged since April 2011", and says the new rules will first be applied in the February 2027 rebalancing "using full-year 2026 trading data" (secondary).[^insiderph-2026-07-index-overhaul]

### The revised policy (announced 21 July 2026, not in force)

<div class="callout warn">
<span class="label">Scheduled change: February 2027 rebalance</span>

CN-2026-0033 announces three amendments, "implemented in the February 2027 index rebalancing": a 98% cumulative market-capitalization screen, new liquidity measures (MTAR and MADV) "replacing the previous liquidity criterion", and a 15% free-float minimum for companies of at least PHP 250bn.[^pse-cn-2026-0033b:1] The attached policy text also contains other changes (four-period persistence rules for PSEi insertion and deletion, a divisor-based calculation, a 10% weight cap for the DivY index) for which **no separate effective date is stated**. Treat them as applying from the same rebalance (inference). The PSE's president said in August 2026 that the next review, "which covers the January to December 2026 period, will utilize our revised index criteria that puts premium on the liquidity of a stock".[^pse-pr-2026-08-mynld-joins-psei]
</div>

| Item | January 2024 (in force) | Revised policy (from the Feb 2027 rebalance) |
|---|---|---|
| Market-cap screen | none | only companies within the top **98%** of cumulative total market capitalization of eligible securities qualify (PSEi, DivY, MidCap, sector indices)[^pse-cn-2026-0033b:6] |
| Liquidity | top 25% median daily value, 9 of 12 months | **MTAR**: twelve-month sum of monthly ratios, each = (median daily value x days traded in the month) / month-end free-float market capitalization; at least **15%** for PSEi/DivY/MidCap entrants, **10%** for existing constituents, 7% for sector indices. **MADV** (monthly total value / trading days): top 25% in 9 of 12 months (PSEi, MidCap, DivY), top 50% in 8 of 12 (sectors). If too few qualify, MTAR may be lowered one point at a time and the MADV bucket widened five points at a time[^pse-cn-2026-0033b:7] |
| Free float | at least 20% | at least 20%, or **15% if market capitalization is at least PHP 250bn**[^pse-cn-2026-0033b:8] |
| PSEi insertion | rank 25 or better | rank 25 or better in the current review, **or rank 30 or better in four consecutive reviews**[^pse-cn-2026-0033b:11] |
| PSEi deletion | rank 36 or worse | rank 36 or worse, **or rank 31 or worse in four consecutive reviews**[^pse-cn-2026-0033b:11] |
| Early inclusion | top 20% median daily trade for 6 months or 75% of months listed | MTAR at least 15% and top 20% MADV for at least 6 months or 75% of months listed[^pse-cn-2026-0033b:13] |
| MidCap liquidity | top 35% median daily trade, 9 of 12 months | top 25% MADV (as the PSEi) plus the 98% screen[^pse-midcap-index-policy-2024:3][^pse-cn-2026-0033b:7] |
| Calculation | base-capitalization formula | divisor method; each index's divisor is recalculated at the end of every day for the next day, including constituent changes scheduled for it; DivY highest weight capped at 10% before each rebalancing[^pse-cn-2026-0033b:16-17] |
| Engine reference | "calculated and broadcasted through the PSEtrade XTS" | "through the trading engine" (engine-neutral)[^pse-index-policy-2024:3][^pse-cn-2026-0033b:4] |
| Notice | "as much as practicable, five trading days" | "as much as practicable, at least five trading days"[^pse-cn-2026-0033b:11] |

**Worked example: MTAR (arithmetic illustration, not a PSE example).** A stock with free-float market capitalization of PHP 10bn at each month-end, a median daily value of PHP 5m and 20 trading days a month has a monthly ratio of 5m x 20 / 10bn = 1.0%; twelve months sum to 12%. That clears the 10% bar for an existing constituent but fails the 15% bar for an entrant, so the same stock can be kept in the PSEi yet not admitted to it. In effect MTAR is a median-based annual turnover of the free float (inference).[^pse-cn-2026-0033b:7]

Press accounts add context (secondary): a newly added stock "surged sharply in a single day as funds tracking the index scrambled to buy shares" despite meeting the float test; one internal estimate put the pool passing the 98% screen at about 100 companies; market chatter named Aboitiz Power and Synergy Grid as possible entrants and China Banking and DigiPlus as at risk.[^insiderph-2026-07-insider-info-overhaul][^insiderph-2026-07-index-overhaul]

### Review calendar and implementation timing

| Effective (first trading day) | Announced | PSEi in | PSEi out | Basis |
|---|---|---|---|---|
| Mon 6 Feb 2023 | about 27 Jan 2023 | DMC, UBP | MEG, RLC | Jan to Dec 2022 review; secondary press report[^manilatimes-2023-01-28-dmc-ubp] |
| Mon 7 Aug 2023 | 28 Jul 2023 | none | none | Jul 2022 to Jun 2023 review[^pse-cn-2023-0039:1][^pse-pr-2023-08-psei-retains-composition] |
| Tue 26 Sep 2023 (start of day) | 20 Sep 2023 | BLOOM, CNPF | AP, MPI | off-cycle, "recent developments in certain constituents"; identities by list comparison[^pse-cn-2023-0044:1-2] |
| Wed 4 Oct 2023 (start of day) | 28 Sep 2023 | NIKL | UBP | UBP's float fell below the 20% minimum after the PSE reclassified shares it reported as public[^pse-cn-2023-0047:1-2] |
| Mon 5 Feb 2024 | 26 Jan 2024 | none | none | Jan to Dec 2023 review[^pse-cn-2024-0008:1-2] |
| Mon 12 Aug 2024 | 5 Aug 2024 | none | none | Jul 2023 to Jun 2024 review[^pse-cn-2024-0042:1] |
| Mon 3 Feb 2025 | 24 Jan 2025 | AREIT, CBC | NIKL, WLCON | Jan to Dec 2024 review[^pse-cn-2025-0005:1] |
| Mon 18 Aug 2025 | 8 Aug 2025 | PLUS | BLOOM | Jul 2024 to Jun 2025 review[^pse-cn-2025-0034:1] |
| Mon 2 Feb 2026 | about 27 Jan 2026 (press date; the PSE release gives only the effective date) | RCR | AGI | Jan to Dec 2025 review[^pse-pr-2026-02-rcr-replaces-agi] |
| Mon 3 Aug 2026 | 27 Jul 2026 | **MYNLD** (early inclusion) | CNVRG | Jul 2025 to Jun 2026 review; "only the third company to qualify for early PSEi inclusion since we introduced this rule in 2021"[^pse-cn-2026-0035:1][^pse-pr-2026-08-mynld-joins-psei] |

Between Feb 2023 and Aug 2026 there were seven membership-changing events (ten stocks added) and three unchanged reviews (Aug 2023, Feb 2024, Aug 2024). Members in force from 3 Aug 2026 (30): AC, ACEN, AEV, ALI, AREIT, BDO, BPI, CBC, CNPF, DMC, EMI, GLO, GTCAP, ICT, JFC, JGS, LTG, MBT, MER, MONDE, MYNLD, PGOLD, PLUS, RCR, SCC, SM, SMC, SMPH, TEL, URC.[^pse-cn-2026-0035:2] On the same day CNVRG and PX (Philex) joined MidCap and AUB (Asia United) left, AEV entered the DivY index, and every sector index changed (Industrial, for example, adds BSC, MYNLD, TOP and drops CIC, PPC, VITA).[^pse-cn-2026-0035:1][^pse-pr-2026-08-mynld-joins-psei] RRHI was removed from MidCap and DivY on 16 Jul 2026 after a trading suspension following its tender offer cut its public float below the Exchange minimum.[^pse-pr-2026-08-mynld-joins-psei] A separate reclassification of 13 companies between sectors took effect on Monday 5 Jan 2026, with matching sector-index membership changes.[^pse-cn-2025-0047-sector-reclassification:1-2]

**Implementation timing.** Circulars say changes are "effected on" the Monday (semi-annual) or "effective on start of day" (off-cycle).[^pse-cn-2025-0005:1][^pse-cn-2023-0044:1] Counting trading days from the announcement to the last session before the effective date, lead time was **5** in Aug 2023, Jan 2024, Jan 2025 and Aug 2025, **4** in Aug 2024 and Jul 2026, and **3** for the two off-cycle moves of Sep and Oct 2023 (and for Feb 2026 if the 27 Jan date is right): the "five trading days" is a target, not a guarantee (computed from the circular dates). February effective dates were the first Monday of February in 2023, 2024, 2025 and 2026; August dates ranged from 3 to 18 August, so the policy's "mid-February" and "mid-August" wording is stale. The revised policy states each day's divisor is recomputed at the end of the trading day for the next day, including scheduled constituent changes,[^pse-cn-2026-0033b:17] so an index fund must hold the new basket at the **last close before the effective date** (Friday for a Monday effect; inference). A press account describes the First Metro Philippine Equity ETF (listed 2013) as the country's first and still only ETF; that it tracks the PSEi is background knowledge, not shown in the sources read, and no figure for assets tracking PSE indices was found.[^insiderph-2026-07-etf-reboot]

### Event-day behaviour on the last session before a PSEi change (computed)

<div class="callout infer">
<span class="label">Computed from PSE Daily Quotation Reports</span>

Method: for each stock, value and volume from the DQR on the last trading day before the effective date, compared with that stock's median daily value over the prior 20 trading days; returns are close to close; "+5d" is the return from that day's close to the close five trading days later. The multiples and returns are computed, not published; the DQRs are public PDFs.[^pse-daily-quotation-report-series]
</div>

| Last session | Stock (action) | Value (PHP) | x own 20-day median value | Day return | Close vs range | Net foreign (PHP) | +5d |
|---|---|---|---|---|---|---|---|
| 31 Jan 2025 | **CBC** (in)[^pse-dqr-2025-01-31:1] | 5.60bn (62.9m shares) | 89x | **+38.9%** (66.95 to 93.00) | at day high | +0.66bn | -6.1% |
| 31 Jan 2025 | AREIT (in)[^pse-dqr-2025-01-31:4] | 2.72bn | 35x | +7.7% | at high | +0.99bn | -5.8% |
| 31 Jan 2025 | NIKL (out)[^pse-dqr-2025-01-31:7] | 0.48bn (215m shares) | 122x | **-17.8%** | at low | +0.01bn | +19.8% |
| 31 Jan 2025 | WLCON (out)[^pse-dqr-2025-01-31:7] | 0.82bn | 29x | -1.6% | at low | +0.11bn | +7.6% |
| 15 Aug 2025 | PLUS (in)[^pse-dqr-2025-08-15:6] | 1.98bn | 2.0x | +8.1% | upper part | -0.21bn | -3.3% |
| 15 Aug 2025 | BLOOM (out)[^pse-dqr-2025-08-15:6] | 0.49bn | 6.4x | +9.1% | at high | -0.03bn | -7.2% |
| 30 Jan 2026 | RCR (in)[^pse-dqr-2026-01-30:5] | 2.50bn (341m shares) | 17x | -4.9% | at low | -1.16bn | +3.7% |
| 30 Jan 2026 | AGI (out)[^pse-dqr-2026-01-30:3] | 0.40bn | 21x | +2.1% | at high | +0.02bn | +14.2% |
| 31 Jul 2026 | MYNLD (in, early)[^pse-dqr-2026-07-31:2] | 1.43bn | 20x | -2.6% | at low | -0.49bn | -1.7% |
| 31 Jul 2026 | CNVRG (out)[^pse-dqr-2026-07-31:5] | 0.83bn | 15x | +6.1% | upper part | -0.01bn | +1.3% |

**Worked example: CBC.** On Friday 31 Jan 2025, the last session before CBC joined the PSEi on Monday 3 Feb, CBC traded 62.9m shares for PHP 5.6bn, about 89 times its own median daily value (roughly PHP 63m), and rose from 66.95 to 93.00 (+38.9%), closing at the day's high; five trading days later it was 6.1% lower.

**Market-wide turnover on PSEi event days (computed).** Total value relative to the prior-20-day median, ex-block, was 1.6x (15 Aug 2025), 2.1x (30 Jan 2026), 1.8x (31 Jul 2026) and 1.5x for the 3 Oct 2023 off-cycle move (median of the four about 1.7x), against a base rate since January 2024 of median 1.0x and 90th percentile 1.4x ex-block; the sessions before the Feb 2024 and Aug 2024 reviews, which changed nothing, ran 1.2x and 1.15x. The 31 Jan 2025 session (5.0x) is not clean because the PSEi fell 4.0% that day.

<div class="callout infer">
<span class="label">Inference</span>

PSEi events move individual stocks a great deal but total market turnover little, consistent with the small amount of money that tracks the PSEi compared with MSCI-benchmarked money (below). Additions: 3 of 5 rose on the day and 4 of 5 were lower five days later. Deletions: the two largest falls on the day were NIKL and WLCON and 4 of 5 were higher five days later. The pattern is run-up into the last close and partial reversal, not a permanent re-rating, but the sample is ten stocks.
</div>

The PSE is developing a derivatives market "starting with Index Futures which will be based on the PSEi"; no PSEi derivative is listed and no launch date is set (see [Chapter 17](#/ch/reform-timeline)).[^pse-asm-2026-president-report:24]

### Execution implications

- **Calendar.** Assume announcement 3 to 5 trading days before and implementation at the open of a Monday; for PSEi trackers the volume sits in the last close before it. Check the PSE holiday list for each review ([Chapter 3](#/ch/sessions)).
- **Single-name risk.** Additions whose normal turnover is small next to index-fund demand can gap violently into the last close (CBC +38.9%, AREIT +7.7%) and give some back within a week; small deleted names can fall 15% to 20% on huge volume and rebound. Size to the stock's own 20-day median value, not to the index.
- **February 2027.** Build an MTAR, MADV and 98% screener now from the public DQR series and the quarterly Public Ownership Reports; names near the entry thresholds (MTAR 15%, existing members 10%) drive the trade, and the 15% float exception helps only stocks of PHP 250bn or more. If February follows the recent pattern the effective date is Monday 1 Feb 2027, the last session before it Friday 29 Jan 2027, and the announcement late January; the PSE has not announced a 2027 timetable (inference).
- **Weights are uncapped.** A few names (ICTSI at 14% of the PSEi) dominate index risk; hedge with PSEi-correlated baskets accordingly.
- **Membership drives other lists.** The short-sale eligible list ([Chapter 9](#/ch/short-selling)) and SCCP collateral eligibility ([Chapter 10](#/ch/clearing-settlement)) follow index membership, so an addition or deletion also changes borrowing and broker financing, not only index-fund demand.
- **Do not extrapolate.** Whole-market turnover on PSEi event days is modest (about 1.5x to 2.1x ex-block), so liquidity into the PSEi close is thin outside the changing names.

## External indices: MSCI, FTSE Russell and S&P

### MSCI Philippines

The MSCI Philippines Index (Standard, large and mid cap) had **9 constituents** at 30 Sep 2026 and "covers about 85% of the Philippines equity universe"; float-adjusted market capitalization USD 30,500.43m (largest 13,641.85m, smallest 1,199.26m, median 1,856.94m); last-12-month one-way turnover 10.77%; launched 29 Apr 1988.[^msci-philippines-index-factsheet-2026-09:1-2]

| Constituent | Float-adjusted cap (USD bn) | Weight | Sector |
|---|---|---|---|
| ICTSI | 13.64 | **44.73%** | Industrials |
| BDO Unibank | 4.09 | 13.41% | Financials |
| BPI | 2.56 | 8.38% | Financials |
| SM Prime | 2.36 | 7.72% | Real Estate |
| Ayala Corp | 1.86 | 6.09% | Industrials |
| Metrobank | 1.75 | 5.74% | Financials |
| SM Investments | 1.75 | 5.72% | Industrials |
| PLDT | 1.30 | 4.27% | Communication Services |
| Meralco B | 1.20 | 3.93% | Utilities |

Sector weights: Industrials 56.54%, Financials 27.53%, Real Estate 7.72%, Communication Services 4.27%, Utilities 3.93%.[^msci-philippines-index-factsheet-2026-09:2] The MSCI Philippines IMI (large, mid and small) has **34 constituents** and USD 43,676.74m, with ICTSI at 31.23% and Ayala Land still in its top ten at 2.98%; the MSCI Emerging Markets Index has 1,165 constituents and USD 12,281,841.19m.[^msci-philippines-imi-factsheet-2026-09:1-2][^msci-em-index-factsheet-2026-09:2] **Computed:** the Standard index is 30,500.43 / 12,281,841.19 = **0.248% of MSCI EM**, and the 25 small-cap names add about USD 13.2bn (IMI minus Standard). The EM factsheet does not list the Philippines separately (it sits in "Other 15.12%").[^msci-em-index-factsheet-2026-09:2] Abacus Securities (reported 25 Aug 2026) calls the weight a "decade, if not all-time, low", with a Standard count of 9 "down from 11 earlier this year" against about 21 for Malaysia, 18 for Thailand and 16 for Singapore, and about 0.3% of MSCI Asia ex-Japan versus close to 3% a decade ago (secondary).[^bilyonaryo-2026-08-25-msci-presence-abacus]

| MSCI review | Philippine change | Status of evidence |
|---|---|---|
| May 2023 (traded 31 May 2023) | Monde Nissin removed from MSCI Philippines; PSE value traded PHP 24.2bn, "6x-7x" the usual, foreign net selling PHP 4.15bn | secondary; the DQR confirms the totals[^metrobank-what-is-msci-rebalancing][^pse-dqr-2023-05-31:12] |
| Feb 2025 (effective 28 Feb) | JG Summit and URC moved from Standard to Small Cap; Monde Nissin added to Small Cap; AP Securities flow estimates about -USD 30m (URC), -USD 23m (JGS), +USD 9.5m (Monde) | secondary[^philstar-2025-02-15-msci-jgs-urc] |
| Feb 2026 (after the 27 Feb close) | Standard unchanged; Apex Mining and Maynilad added to Small Cap, after First Metro had said Jollibee was "very likely to stay" in Standard | secondary; the headline and summary only, the page could not be opened[^inquirer-2026-02-msci-standard-unchanged][^insiderph-2026-02-first-metro-msci] |
| May 2026 (announced 12 May; implemented as of the close of 29 May; effective 1 Jun) | MSCI's document gives no country detail. A count of 11 to 10 and a **Jollibee deletion are inferred**: the stock is absent from the Sep 2026 Standard list, traded PHP 6.1bn (28x its median) and fell 6.1% to the day low on 29 May | dates primary; deletion inferred, no MSCI country list was available[^msci-index-review-factsheet-2026-05:1-2] |
| Aug 2026 (after the 31 Aug close) | **Ayala Land** moved from Standard to Small Cap after losing 29% of its value in 2026; Standard count 9. Computed from the DQRs: it fell 5.7% to PHP 14.98 on 13 Aug, the first session after the 12 Aug announcement | secondary; count confirmed by the factsheet[^insiderph-2026-08-ali-msci][^newswav-2026-08-msci-ali][^pse-daily-quotation-report-series] |

The May 2026 review used MSCI's new enhanced free-float rounding methodology for the first time, "the primary driver of the higher number of free float updates and elevated turnover"; the changes were announced 12 May and implemented for the market-cap indexes as of the close of 29 May 2026.[^msci-index-review-factsheet-2026-05:1-2] Meralco's PHP 4.4bn (32x its median) on the same day coincides with that rounding change and is more likely a weight change than a deletion (Meralco B remains in the index; inference).

<div class="callout">
<span class="label">When MSCI's date is a PSE holiday</span>

MSCI's Ayala Land change took effect as of the 31 Aug 2026 close. The PSE was closed on Fri 21 Aug and **Mon 31 Aug 2026** (National Heroes Day), so index funds had to trade by the **Fri 28 Aug** close, which is where the volume appears: Ayala Land traded PHP 7.23bn (466m shares, 39x its median), 38% of the whole market's PHP 18.8bn that day. The first session after the holiday, Tue 1 Sep, still traded 1.8x the baseline with Ayala Land down 3.3% (computed).[^pse-cn-2026-0034b-non-trading-days-aug-2026:1][^pse-dqr-2026-08-28:12] Check both calendars for every review. The November implementation fell on Mon 25 Nov 2024 and Mon 24 Nov 2025 (identified from the volume peaks, not from an MSCI document), so the 2026 date cannot be assumed to be month-end: Mon 30 Nov 2026 (Bonifacio Day) is listed as a holiday under Proclamation 1006 with no PSE circular yet (see [Chapter 3](#/ch/sessions)), and a date in the week of 23 Nov would fall on the new engine's first sessions. MSCI's November 2026 schedule was not retrieved (inference).
</div>

**Reclassification risk.** No source read suggests an MSCI reclassification of the Philippines. MSCI's 2026 Market Classification Review release (June 2026, read in a Business Wire translation) names Bulgaria, Indonesia, Turkey, Bangladesh, Korea and Greece and does not mention the Philippines, and MSCI's June 2026 accessibility review still lists foreign-ownership, FX and short-selling frictions, noting that the Philippine short-selling programme "was implemented in November 2023. However, it is not yet an established market practice."[^ladige-2026-06-msci-mcr][^msci-accessibility-review-2026:43] The foreign-ownership detail is in [Chapter 14](#/ch/foreign-access) and short selling in [Chapter 9](#/ch/short-selling). The nine-name count is a fact to watch; no MSCI rule that it triggers a reclassification was found.

### FTSE Russell

The Philippines is **Secondary Emerging** in the FTSE Global Equity Index Series (ground rules v14.4, September 2026, Appendix E) and has been in the series since 1 Jul 1996, with Indonesia.[^ftse-geis-ground-rules-2026-09:43][^ftse-geis-ground-rules-2026-09:45] The 7 Apr 2026 interim announcement lists the Philippines under Secondary Emerging; its watch list contained only **Egypt** (possible Secondary Emerging to Frontier on stock count); Nigeria moves to Frontier at the open of 21 Sep 2026, Vietnam from Frontier to Secondary Emerging at the open of Mon 21 Sep 2026 in multiple tranches "beginning in September 2026 and concluding in 2027", and Greece to Developed on 21 Sep 2026.[^ftse-country-classification-interim-2026-03:2-6] The September 2025 announcement (published 7 Oct 2025) did not place the Philippines on the watch list.[^ftse-country-classification-annual-2025-09:2]

<div class="callout warn">
<span class="label">Outcome of the 6 October 2026 announcement is unknown</span>

FTSE's annual review results are published each September and normally carry "at least six months' notice before changing the classification of any country".[^ftse-geis-ground-rules-2026-09:9] The 2026 annual announcement was scheduled for **Tuesday 6 October 2026**; when checked that day FTSE's page still showed "Document to follow".[^ftse-country-classification-interim-2026-03:5][^ftse-equity-country-classification-page] No 2026 classification outcome is known to this knowledge base. Under the stated process a country is placed on the watch list before any reclassification and given at least six months' notice, and the Philippines was not on the watch list, so no change taking effect soon is expected (inference).
</div>

**Quality-of-markets ratings, Philippines (FTSE table "as at March 2026"; read from the rendered table by column).**[^ftse-quality-of-markets-asia-pacific-2026-03:1]

| Criterion | Rating |
|---|---|
| Transparency: market depth information, visibility and timely trade reporting | **Pass** |
| Efficient trading mechanism; brokerage competition; off-exchange transactions; tax; regulator monitoring | Pass |
| Central securities depository; CCP clearing house (equities); settlement costs of failed trades; custodian competition | Pass |
| Settlement cycle (DvP) | T+2 |
| Capital repatriation; registration of foreign investors | Pass |
| Fair treatment of minority shareholders; foreign ownership restrictions; stock lending; short sales; free delivery; custody account structure | **Restricted** |
| Developed foreign exchange market; transaction costs; developed derivatives market | **Not Met** |

The foreign-exchange cell is the only Philippine cell carrying the table's change marker (dotted shading with a heavy outline; the legend reads "Shading indicates a rating change from September 2025"), so that rating changed since September 2025; the direction is not shown. GNI per capita is rated Lower Middle and credit worthiness Investment. FTSE's separate watch-list sheet (March 2026) names no Philippine criterion.[^ftse-watch-list-2026-03:1]

**Index mechanics.** Semi-annual reviews in March and September for Asia Pacific ex China ex Japan, on data as of the last business day of December and June; changes are "implemented after the close of business on the third Friday (i.e. effective the following Monday)"; quarterly reviews in June and December; securities with free float of 5% or below are excluded (except very large ones); weights are adjusted for foreign ownership limits and a minimum foreign-headroom test; a semi-annual median-volume liquidity screen applies.[^ftse-geis-ground-rules-2026-09:13][^ftse-geis-ground-rules-2026-09:18][^ftse-geis-ground-rules-2026-09:20] FTSE's September 2026 review (announced 21 Aug) re-admits Emperador as a Small Cap, the only new Philippine addition (secondary).[^insiderph-2026-08-emperador-ftse]

### S&P and others

No S&P Dow Jones methodology, consultation or constituent document was retrieved, and passive assets benchmarked to MSCI, FTSE or PSE indices were not found; the flow estimates above are the only sizing in the record.

## Rebalance-day statistics (computed)

<div class="callout infer">
<span class="label">Computed, not published</span>

Every figure in this section is computed from 715 archived PSE Daily Quotation Reports (17 Apr to 5 Jun 2023, 2 to 10 Oct 2023 and 2 Jan 2024 to 5 Oct 2026). For each event date, total value is the DQR grand total (main board, odd lot, block and, in later layouts, VWAP); the baseline is the median of the previous 20 trading days; "ex-block" removes the DQR block-sale value from both. The MSCI events of Feb, Aug and Nov 2023 and the FTSE events of Jun, Sep and Dec 2023 fall outside the sample and are not measured. Base rate over the 674 days from January 2024: median about 1.0x, 90th percentile about 1.6x, 95th about 2.1x to 2.2x, 99th about 4.0x; 5.9% of days at 2x or more and 2.1% at 3x or more (ex-block: 90th about 1.4x, 95th about 1.7x); median absolute daily net foreign flow over the last year PHP 0.44bn. For scale, the median daily total value from 1 Jan to 5 Oct 2026 was about PHP 6.9bn.[^pse-daily-quotation-report-series]
</div>

### MSCI implementation days

The 31 May 2023, 28 Feb 2025, 27 Feb 2026, 29 May 2026 and 28 Aug 2026 dates are confirmed by the sources above; the others are identified from MSCI's usual implementation pattern and the volume peak in the DQRs (the November dates fall before month-end, not on its last business day).

| PSE session | Total value (PHP bn) | x 20-day median | x ex-block | Net foreign (PHP bn) | PSEi day | Largest single-name effect |
|---|---|---|---|---|---|---|
| 31 May 2023[^pse-dqr-2023-05-31:12] | 24.54 | 5.3 | 6.2 | -4.15 | -0.5% | MONDE PHP 4.41bn (53x own median; 18% of the day) |
| 29 Feb 2024[^pse-dqr-2024-02-29:13] | 11.96 | 2.4 | 2.6 | +0.44 | +1.0% | broad-based |
| 31 May 2024[^pse-dqr-2024-05-31:13] | 22.72 | 3.9 | 4.6 | -5.23 | +1.0% | AEV PHP 5.48bn (106x; 24% of the day) |
| 30 Aug 2024[^pse-dqr-2024-08-30:13] | 13.31 | 2.4 | 2.6 | -0.31 | +0.1% | broad-based |
| 25 Nov 2024[^pse-dqr-2024-11-25:13] | 9.98 | 1.8 | 2.0 | -0.31 | +1.0% | broad-based |
| 28 Feb 2025[^pse-dqr-2025-02-28:13] | 20.63 | 3.6 | 3.9 | -3.43 | -2.1% | URC PHP 4.35bn (22x) and JGS PHP 3.15bn (33x): 36% of the day |
| 30 May 2025[^pse-dqr-2025-05-30:13] | 40.03 | 6.2 | 2.7 | -15.31 | -1.1% | PHP 24.5bn of block trades (Robinsons Retail PHP 15.8bn, BDO PHP 8.4bn), unrelated to the index |
| 26 Aug 2025[^pse-dqr-2025-08-26:13] | 14.32 | 2.1 | 2.1 | -2.04 | -2.2% | broad-based; BDO -8.0% on PHP 2.18bn (5x), net foreign -PHP 1.08bn |
| 24 Nov 2025[^pse-dqr-2025-11-24:13] | 13.69 | 2.1 | 2.3 | -0.82 | +0.4% | BPI PHP 2.75bn (8x); broad-based |
| 27 Feb 2026[^pse-dqr-2026-02-27:13] | 19.62 | 2.8 | 2.2 | +0.92 | -0.2% | PHP 6.4bn of block trades (AREIT PHP 3.7bn, PLUS PHP 1.9bn); MYNLD PHP 1.87bn (13x) |
| 29 May 2026[^pse-dqr-2026-05-29:13] | 26.47 | 4.4 | 4.9 | -6.65 | -1.6% | JFC PHP 6.10bn (28x; 23% of the day), MER PHP 4.39bn (32x) |
| 28 Aug 2026[^pse-dqr-2026-08-28:12] | 18.81 | 3.2 | 3.5 | -3.51 | -0.8% | ALI PHP 7.23bn (39x; 38% of the day, 466m shares) |

**Summary (computed):** median **3.04x** (mean 3.36x) total value and 2.63x ex-block; **11 of 12 days at or above 2.0x** against a 5.9% base rate; net foreign selling on 10 of 12 days, six of them at PHP 3.4bn or more (8x to 35x the typical absolute daily flow of PHP 0.44bn; the PHP 15.3bn of 30 May 2025 is inflated by unrelated block trades). May reviews are the heaviest in the sample (5.3x, 3.9x, 6.2x total or 2.7x ex-block, 4.4x); February and August reviews run 2x to 4x; November 2024 and 2025 about 2x.

### FTSE third-Friday days

| PSE session | Total value (PHP bn) | x 20-day median | x ex-block | Net foreign (PHP bn) |
|---|---|---|---|---|
| 15 Mar 2024[^pse-dqr-2024-03-15:13] | 20.08 | 4.1 | 4.1 | -4.30 |
| 21 Jun 2024[^pse-dqr-2024-06-21:13] | 8.26 | 1.7 | 1.8 | -1.34 |
| 20 Sep 2024[^pse-dqr-2024-09-20:13] | 16.98 | 2.8 | 2.6 | +1.28 |
| 20 Dec 2024[^pse-dqr-2024-12-20:13] | 6.95 | 1.2 | 1.5 | -0.78 |
| 21 Mar 2025[^pse-dqr-2025-03-21:13] | 11.77 | 1.9 | 2.0 | +1.04 |
| 20 Jun 2025[^pse-dqr-2025-06-20:13] | 12.27 | 2.0 | 2.1 | -0.84 |
| 19 Sep 2025[^pse-dqr-2025-09-19:13] | 14.30 | 2.3 | 2.4 | +0.22 |
| 19 Dec 2025[^pse-dqr-2025-12-19:13] | 18.72 | 2.7 | 1.9 | -0.10 |
| 19 Jun 2026[^pse-dqr-2026-06-19:13] | 11.18 | 1.6 | 1.8 | -0.45 |
| 18 Sep 2026[^pse-dqr-2026-09-18:12] | 16.23 | 2.8 | 2.8 | -1.46 |

FTSE days: median **2.1x** of the 20-day median on total value (2.07x ex-block, mean 2.30x); March 2024 (4.1x) is the largest. No DQR exists for 20 Mar 2026 in the public series, so that event is not measured. Third Fridays are also quarterly-expiry dates in many other markets and rebalance dates for other index providers (general knowledge), so attribution to FTSE alone is not clean.

### Stock-level evidence on MSCI deletions and additions

"Announcement" is the close on the MSCI announcement date, which reaches Manila the next morning; announcement dates other than 12 May 2026 are as reported or inferred. Returns are raw, not market-adjusted.

| Stock (MSCI action) | Announcement close | Implementation-day close | Announcement to implementation | Implementation day | Close in day's range (0 = low, 1 = high) | Net foreign on the day | +5 trading days |
|---|---|---|---|---|---|---|---|
| MONDE 31 May 2023 (removed; secondary)[^pse-dqr-2023-05-31:2] | 9.32 (11 May) | 8.10 | -13.1% | -1.2% | 0.18 | -PHP 1.12bn | +13.5% |
| AEV 31 May 2024 (inferred)[^pse-dqr-2024-05-31:3] | 38.35 (14 May) | 35.05 | -8.6% | -5.3% | at low | -PHP 3.03bn | +9.8% |
| JGS 28 Feb 2025 (to Small Cap; secondary)[^pse-dqr-2025-02-28:4] | 15.02 (11 Feb) | 15.86 | +5.6% | -7.1% | at low | -PHP 1.41bn | +14.2% |
| URC 28 Feb 2025 (to Small Cap; secondary)[^pse-dqr-2025-02-28:2] | 61.90 | 66.20 | +6.9% | -2.9% | 0.37 | -PHP 1.50bn | +8.5% |
| MONDE 28 Feb 2025 (added to Small Cap; secondary)[^pse-dqr-2025-02-28:2] | 7.55 | 7.55 | 0.0% | -5.5% | at low | -PHP 0.07bn | +2.9% |
| JFC 29 May 2026 (inferred)[^pse-dqr-2026-05-29:2] | 144.00 (12 May) | 126.90 | -11.9% | -6.1% | at low | -PHP 2.79bn | +7.4% |
| MER 29 May 2026 (weight change, inferred)[^pse-dqr-2026-05-29:2] | 650.00 | 570.50 | -12.2% | -4.8% | at low | -PHP 1.49bn | -2.5% |
| MYNLD 27 Feb 2026 (added to Small Cap; secondary)[^pse-dqr-2026-02-27:2] | 19.62 (10 Feb) | 22.00 | +12.1% | +0.9% | 0.55 | +PHP 0.38bn | -5.9% |
| APX 27 Feb 2026 (added to Small Cap; secondary)[^pse-dqr-2026-02-27:7] | 14.98 | 17.50 | +16.8% | 0.0% | 0.40 | +PHP 0.17bn | -8.9% |
| ALI 28 Aug 2026 (to Small Cap; secondary)[^pse-dqr-2026-08-28:4] | 15.88 (12 Aug) | 15.54 | -2.1% | +0.3% | 0.76 | -PHP 1.56bn | -2.8% (-3.3% next day) |

**Reading (computed, descriptive).** (1) Heavy deletions are absorbed into the last close with day moves of -3% to -7% for AEV, JGS, URC, JFC and MER (MONDE -1.2% after a 13% slide from the announcement), a close in the bottom 40% of the day's range for all six and at the low for four, and a rebound of 7% to 14% within five trading days for five of the six (MONDE, AEV, JGS, URC, JFC; MER did not rebound). (2) Price pressure begins at the announcement: Ayala Land fell 5.7% on the reaction day (13 Aug), held up into the trade date (+0.3%) and kept drifting lower, so for a stock with weak fundamentals the rebound did not occur. (3) Additions to the Small Cap index drew modest volume, ran up beforehand (MYNLD +12%, APX +17% from the announcement) and fell after (-6% to -9% at five days). (4) One deleted stock can be 18% to 38% of the whole market's value that day. The closing-auction share cannot be isolated because the DQR reports only daily totals and the close; closes at the day's low are consistent with late-session and closing-auction selling but are not proof of it. Several event days coincide with other flows (blocks, earnings, quarterly expiries), so the numbers are descriptive.

### Execution implications

- **Treat MSCI implementation days as 2x to 6x days** with price pressure concentrated into the last close and net foreign selling when names are deleted. Size and schedule other orders away from the close unless you are supplying liquidity to the deletion; the closing-auction mechanics are in [Chapter 6](#/ch/auctions).
- **For deletions the pattern is:** pressure from the announcement (about 2.5 weeks before), a final push into the last close, then a rebound within about a week for fundamentally sound names. Build the trade on the rebound only where the stock is not in a downtrend (Ayala Land did not rebound).
- **Check both calendars** (MSCI's and the PSE's) for every review; when MSCI's date is a PSE holiday the PSE trade date is the previous session.
- **FTSE days are smaller (about 2x) but frequent** (March, June, September, December; the September 2026 review also had the Vietnam and Greece changes at the open of 21 Sep).
- **The November 2026 MSCI implementation may coincide with the new engine's first days.** The last two November reviews were traded on 25 Nov 2024 and 24 Nov 2025; the 2026 date is unknown (see above). Either way, the first MSCI implementation on the new engine will be the first live test of its closing rules and the negotiated-trade facility, which change how large index orders can be crossed (see [Chapter 5](#/ch/matching) and [Chapter 6](#/ch/auctions)).

## Scheduled change: the new-engine feeds (23 November 2026)

<div class="callout warn">
<span class="label">Scheduled change: 23 Nov 2026, subject to SEC approval of the rule changes</span>

The PSE announced on 22 May 2025 that it will replace PSEtrade XTS with Nasdaq Eqlipse (the "NTE").[^pse-new-trading-engine-page] As of the 9 Jul 2026 broker forum: certification of brokers' own front ends 10 to 23 Sep 2026; pre-production connectivity 29 Sep to 9 Oct; pre-production testing 12 to 22 Oct; Saturday market rehearsals 31 Oct, 7 Nov and 14 Nov; **go-live Monday 23 Nov 2026**, with no parallel run ("big bang") and limit orders only on day 1.[^pse-nte-broker-forum-2026-07-09:9][^pse-nte-faq-2026-08:1] No later primary document re-confirming or moving the date was found by 6 Oct 2026. The rule changes tied to it (one-share lots, removal of the odd-lot market, a new tick table, a changed run-off rule, Negotiated Trades) were still marked for SEC approval or revision on PSE's 17 Aug 2026 analyst-briefing slide, and no approval or effectivity circular was found.[^pse-analyst-briefing-1h-2026:9] Everything above about ITCH v2.3, [R] groups and [P]/[p] marking describes XTS and should be version-gated on the engine date. The master pipeline is in [Chapter 17](#/ch/reform-timeline).
</div>

| Item | Known (primary) | Unknown |
|---|---|---|
| Protocols | two: **ITCH** and **MDF** (Nasdaq market data feed), each on its own dedicated TCP connection and incoming feed, both over SoupBinTCP but with different message formats[^pse-nte-faq-2026-08:3] | message layouts: the specifications are not public |
| Specification status | versions v1.0 (29 Jan 2026), v1.1 (8 Jun 2026), v1.2 (17 Jul 2026) listed on the PSE site ("please contact" the market-data e-mail); the FAQ says final specs were released 23 Jul 2026[^pse-new-trading-engine-page][^pse-nte-faq-2026-08:2] | which version is final (the dates differ by six days) |
| Broker IDs | nothing stated | whether executions carry broker IDs and whether an anonymity switch exists; the FAQ's [C] and [P] use the upper-case names that the old spec reserved for the anonymous variants, but Nasdaq message names may simply differ, so nothing is inferred |
| Cross trades | "provided through the Cross Indicator field in the Order Executed with Price [C] and Trade [P] messages"[^pse-nte-faq-2026-08:3] | exact semantics |
| Negotiated trades | price within +/-5% of the full-day VWAP, four decimals, no volume or value limit, execution window 15 minutes after run-off, one-firm trades only; details "disseminated through the Market Data Feed as news/announcement"; counted in the day's total value; included in the trade file; **does not replace** the block sale[^pse-nte-broker-forum-2026-07-09:8][^pse-nte-faq-2026-08:1-2] | message format and timing |
| Odd lots | standard lot size 1 share, so "the Odd Lot Market will no longer be available"[^pse-nte-faq-2026-08:1] | whether group O disappears from [R] |
| Order types | day 1: limit orders only[^pse-nte-faq-2026-08:1] | when others follow |
| Run-off | orders in the run-off / Trading-at-Last period can be entered, modified and executed only at the closing price[^pse-nte-broker-forum-2026-07-09:7][^pse-cn-2025-0046-board-lot-trading-at-last:3-5] | ITCH state-table treatment |
| Static data | Securities and Index Member static-data files and a DDS exchange-rate file, v1.0 dated 22 Jun 2026, are public[^pse-securities-static-data-file:4][^pse-index-member-static-data-file:4] | other fields |
| Credentials and access | FIX credentials are shared but **market data uses different credentials**, with different port assignments and server IP addresses; test environment from 13 Jul 2026[^pse-nte-broker-forum-2026-07-09:4]; the August FAQ says new server IPs were not yet available and only point-to-point testing was complete[^pse-nte-faq-2026-08:3]; a sublicensing agreement with the PSE (required under its licence with Nasdaq) for vendors and for brokers with their own front ends; parallel leased lines of 2 Mbps minimum[^pse-nte-user-group-2026-01-15:4-5][^pse-nte-user-group-2026-01-15:7] | sublicence fees and terms |
| End-of-day files | CTF and ABC specifications unchanged; the Daily Transactions Report is discontinued; files move to the new PSE Portal[^pse-nte-faq-2026-08:2][^pse-nte-user-group-2026-01-15:19] | |
| Index feed | the revised index policy no longer names XTS[^pse-cn-2026-0033b:4] | whether the Index feed ([Y]/[Z]) and index calculation timing change |
| Readiness (9 Jul 2026) | 7 data vendors and 21 trading participants with market data: 10 developing, 12 not started, 6 not responding; UAT connection complete for 2[^pse-nte-broker-forum-2026-07-09:6] | |

### Execution implications

- **Plan a protocol switch, not a patch.** Both ITCH and MDF are new, on separate sessions with separate credentials; test in the PSE's customer test environment, and keep an end-of-day-file fallback and a rollback plan, because there is no parallel run.
- **Re-baseline the book model.** Lot size 1 and a streamlined tick table change depth and tick-size logic (see [Chapter 4](#/ch/order-types)); the odd-lot book should disappear; negotiated trades arrive as news items rather than book events, so a volume model that counts only book events will miss them.
- **Re-test broker-ID visibility and the aggressor model** on day 1: count non-blank broker fields on executions and trades, and check whether [e]/[c]-style passive and active IDs still exist.
- **Do not hard-code either regime.** Read lot size, tick tables and short-sell flags from [R], [L], [M], [k] and the static-data files on the new feed, and gate engine-specific logic on the go-live date until the PSE confirms the final rehearsals.

## What is not in the public record

- **Broker anonymity in production** (2015 to 2026): no PSE statement either way; ask a vendor or broker for live samples.
- **New-engine ITCH and MDF specifications**: broker-ID treatment, depth limits, timestamps and message layouts are unknown; the PSE's "Data Feed Infra" page is "Coming Soon".
- **Real-time ITCH fees**, the vendor list, vendor-side latency, any PSE latency or throughput statistic, and whether the 2017 non-display schedule has been revised.
- **Contents of the historical order-book and per-trade files** (fields, timestamps, broker IDs), and how delayed Level 2 is priced.
- **What retail platforms (PSETradeX, local brokers) display**: how they truncate or label depth, and whether they show broker codes.
- **How Closing VWAP trades appear in ITCH**, and whether the 15:15 close changes the disclosure-halt arithmetic.
- **EDGE**: any API, SLA or latency statistic, the share of disclosures released after 3:15 pm, and the failure and recovery times of the January and October 2026 outages.
- **Index data**: current PSEi weights, float factors and the 2026 Public Ownership Report data (subscription); assets tracking PSE, MSCI or FTSE Philippine indices; the PSE's 2027 review calendar; the MSCI November 2026 review date.
- **FTSE's 2026 classification outcome** (announcement scheduled 6 Oct 2026) and any S&P Dow Jones treatment.
- **Closing-auction volume and price discovery on event days**: needs ITCH [I]/[C] data or a vendor's auction-volume field.
