# PSE equity market microstructure: market-data transparency and dissemination; PSEi and external-index construction and index events

Research date: 6 October 2026 (Manila). Scope: Philippine Stock Exchange (PSE) equities, for Chapter 11 ("Market data") and the index sections of the knowledge base.

**How to read these notes.**
- "In force today" means in force on 6 Oct 2026. Every state is given with the date it took effect and what it replaced; future-dated changes are labelled as such.
- Citations: `[^slug:N]` = physical (1-based) page N of `kb/pdfs/<slug>.pdf`; `[^slug]` = web page or dataset (see the Source catalog at the end, which gives URLs and edition status).
- Evidence labels: **[P]** primary (PSE, MSCI or FTSE Russell document, or PSE-published data); **[S]** secondary only (news, broker or analyst commentary); **[I]** my inference or my own computation from primary data (method stated).
- Currency flags that matter most: (1) the PSE's trading engine, and with it the ITCH market-data feed, is scheduled to change on **Mon 23 Nov 2026** (Section 1.6); (2) the PSE's revised index policy is announced but **not yet in force** (applies from the Feb 2027 rebalance; Section 4); (3) FTSE Russell's 2026 annual country-classification announcement is scheduled for **6 Oct 2026 (today)** and was not yet posted when I checked (Section 5).

**Headline facts**
1. Today's engine is PSEtrade XTS (Nasdaq X-stream), live since 22 Jun 2015. Market data is the ITCH family (Total View = full order-by-order book; Basic = top of book plus trades; Index; News). Broker IDs are attached to executions and trades only (never to resting orders) and only while "Broker Anonymity" is not in force; I found no PSE announcement that anonymity was ever switched on (Section 1).
2. Data licensing: real-time fees are not public. Non-display usage (algorithmic trading, derived data) is USD 7,500 per quarter per category since 1 Oct 2017; historical per-day order-book data is PHP 10,000 and per-trade data PHP 7,500 (Section 2).
3. Disclosures flow through PSE EDGE (since 27 Dec 2013); issuers must disclose within 10 minutes and before any media release; in-hours material news triggers a halt lifted one hour after dissemination (Section 3).
4. PSEi: 30 stocks, free-float-adjusted, uncapped, reviewed semi-annually (Feb/Aug), announced about 3 to 5 trading days ahead and effective at the start of a Monday. The current policy (Jan 2024 version) is replaced from the Feb 2027 review by a July 2026 revision (MTAR plus MADV liquidity tests, a 98% cumulative market-cap screen, a 15% float exception for stocks of PHP 250bn or more) (Section 4).
5. MSCI Philippines Standard has only 9 constituents (30 Sep 2026; USD 30.5bn float-adjusted; about 0.25% of MSCI EM by my computation). FTSE classes the Philippines as Secondary Emerging and does not list it on its watch list (Mar 2026). On MSCI implementation days the PSE trades a median of about 3x its trailing 20-day median daily value (11 of 12 days at or above 2x, against a 5.9% base rate), with foreign net selling on most (Section 5).

---

## 1. Pre- and post-trade transparency (order-book depth, broker IDs, block sales, odd lots)

### Takeaway
On the PSEtrade XTS engine in force today, the full-depth ITCH Total View feed is market-by-order: every order has a day-unique number and the whole book can be rebuilt, with no top-N cut in the specification. Broker identifiers appear only on executions and trades (never on resting orders), and only when the exchange has not switched on "Broker Anonymity". The PSE announced anonymity in January 2014, then said on 3 Oct 2014 it would implement it "but not on go-live" (22 Jun 2015). I found no later PSE announcement that anonymity was ever activated, so the best-supported state is "orders anonymous pre-trade, brokers identified post-trade", but it is not confirmed for 2026. A new Nasdaq Eqlipse engine (new ITCH and MDF feeds, no odd-lot market) is scheduled for 23 Nov 2026.

### Cited Findings

**1.1 What the exchange feed carries (XTS engine, in force today)**
- **[P]** Four ITCH feeds exist: Total View, Basic with Last Sale, News, Index.[^pse-itch-equities-feed-spec-v2-3:22-24] The PSE's own wording: Total View "provides data on real-time orders and trades on all listed equities"; Basic "provides data on real-time trades"; Index carries index levels for the PSEi, All Shares and sector indices.[^pse-data-products-page] The data-feed application form labels Basic "Real Time Feed without Order Book (Level 1)" and Total View "Real Time with Order Book (Level 2)".[^pse-data-feed-application-form:2]
- **[P]** Total View is order-by-order (market-by-order): Add Order [A] (day-unique order number, side, quantity, orderbook, price; price 0x7FFFFFFF = market order), Order Executed [E]/[e] (references the passive order number, executed quantity, match number), Order Executed With Price [C]/[c] (used for auction executions; Printable flag; price), Order Delete [D], Order Replace [U] (new order number), Indicative Price/Quantity [I] (auctions), Broken Trade [B] (reason "S" = supervisory), and Trade [P]/[p].[^pse-itch-equities-feed-spec-v2-3:14-19] The spec describes no depth limit on Total View; the book is the sum of live [A]/[U] orders.[^pse-itch-equities-feed-spec-v2-3:22]
- **[P]** Basic is top-of-book only: BBO Quotation [O] gives best bid/offer price and "aggregated number of visible shares" at that price, plus every trade as [P]/[p].[^pse-itch-equities-feed-spec-v2-3:20,23,28] On 3 Oct 2014 the PSE refused a request for a 5-level BBO in Basic: "the standard for ITCH Basic is that only top of book is published".[^pse-fix-itch-session-week01-2014-10-03:10]
- **[P]** ITCH publishes no running statistics (high/low/last); subscribers must derive them from executions and trades.[^pse-itch-equities-feed-spec-v2-3:32]
- **[P]** Reference price and close price are signalled in-band: [A] with order number 0 and quantity 0 carries the reference price (Total View); [O] with both sizes 0x7FFFFFFFFFFFFFFF does so in Basic; a [P]/[p] with quantity 0 and match number 0 carries the close price, sent immediately after the "Trading At Last" system event.[^pse-itch-equities-feed-spec-v2-3:27]
- **[P]** Auction transparency: [I] publishes theoretical auction quantity, price, best bid and offer, with auction type O (opening/pre-open), I (intraday/halt) or C (closing/pre-close).[^pse-itch-equities-feed-spec-v2-3:17-18] System events mark each phase and state which actions are allowed (order entry, amend/cancel, trading), including 'R' pre-open no-cancel, 'L' pre-close, 'J' pre-close no-cancel and 'P' Trading At Last (entry allowed, amend/cancel not).[^pse-itch-equities-feed-spec-v2-3:10]
- **[P]** Halts/suspensions are signalled by [H]: "V"+"S" suspended, "V"+"F" frozen (circuit breaker), "T"+"H" halted (intraday auction), back to "T"+"N".[^pse-itch-equities-feed-spec-v2-3:13-14] Reference data pushed at start of day includes lot size, tick tables, price decimals, shares outstanding, instrument type (C/P/W/E/D/I), static collars and circuit-breaker limits, short-sell eligibility, and foreign shares available.[^pse-itch-equities-feed-spec-v2-3:11-13,19-20]
- **[P]** Timestamps are "nanoseconds since last Time Stamp seconds message" ([T]); transport is SoupBinTCP v3.0 point-to-point, with MoldUDP64 named for one-to-many multicast.[^pse-itch-equities-feed-spec-v2-3:7,9] Basic, Total View, Index and News are disseminated on different ports.[^pse-fix-itch-session-week01-2014-10-03:10]

**1.2 Broker identifiers: exactly what is attached to what**
- **[P]** The Add Order message [A] has no broker field.[^pse-itch-equities-feed-spec-v2-3:14] Broker IDs exist only in the execution/trade variants: [e] (Passive Broker ID and Active Broker ID, 4-char alpha, blank if unset), [c] (same, plus execution price), and [p] (Buy Broker ID and Sell Broker ID, 4-char alpha).[^pse-itch-equities-feed-spec-v2-3:15-16,19]
- **[P]** Which variant is sent depends on "whether the market is implementing Broker Anonymity or not, as announced by the exchange": anonymity in force uses [E], [C], [P]; not in force uses [e], [c], [p].[^pse-itch-equities-feed-spec-v2-3:25] The Total View and Basic message tables repeat this ("* sent when the market has Broker Anonymity; ** sent when the market does not").[^pse-itch-equities-feed-spec-v2-3:22-23]
- **[P]** The spec's own change history: v1.2 (4 Sep 2014) "Reinstate [C], [E], [P] messages for when Broker Anonymity is enforced"; v2.3 is dated 5 Oct 2018 (title-page change only).[^pse-itch-equities-feed-spec-v2-3:2-3] The PSE data-products page still links v2.3 as the current ITCH specification for the XTS feeds.[^pse-data-products-page]
- **[P]** Post-trade identification to participants: the Consolidated Trade File (CTF), generated for each broker daily at market close, carries "Contra Broker" (the counterpart broker id, 3 digits), trader ID, board (N normal / O odd lot / B block), local/foreign flag, principal/client flag, cross-trade indicator, short flag and investor ID.[^pse-consolidated-tp-file-spec-2015:1-2] The FIX trade ExecutionReport carries Party Role 17 = ContraFirm (and 20 = contra give-up clearing firm).[^pse-fix-specification-v2-5:2,21] The PSE's Aug 2026 new-engine FAQ says there are "no changes" to the CTF specification.[^pse-nte-faq-2026-08:2]
- **[P]** ID conventions: PSETradeX/FIX trader ID = 8 characters = 3-digit broker ID + 2-digit type (00 = PSETradeX, 01 = broker's own front-end) + 3-digit trader ID.[^pse-fix-itch-session-week14-2015-02-13:16] Broker codes are 3-digit numbers.[^pse-psetradex-installation-guidelines:17]
- **[S]** Broker-level post-trade analytics exist at a local broker: Philstocks' "Broker Activity" screen (tabs Ranking, Activity, Net Buying & Net Selling, Transactions; "All Market Data Provided by PSE"). The page I retrieved was undated and showed zero values.[^philstocks-broker-activity] The PSE itself sells a monthly "Trading Participants Ranking Report" by value turnover.[^pse-data-products-page]

**1.3 History of the broker-anonymity plan (dated)**
- **[S]** 27 Jan 2014: a PSE media release (as reported by Rappler) said the PSE would "start implementing broker anonymity" from March 2015, described as "the practice of not showing the broker identifiers for trading matched at the trading engine". Stated current practice: "broker IDs are not displayed pre-trade or when orders are still being queued. But once orders are matched, the broker IDs of the executing brokers become visible." Two phases: from March 2014 only brokers and their systems see IDs in matched trades; from March 2015 IDs anonymous to all.[^rappler-2014-01-27-broker-anonymity]
- **[S]** 12 May 2014 (Philstar, "Fear of the dark"): restates the pre-trade/post-trade split; reports the objection that anonymity would "highlight the information advantage that big hedge funds, foreign and local institutional investors already have against small retail investors" (Khoo Boo Boon) and that the post-trade identities "compensate the less informed traders"; notes a PSE COO response dated 2 May 2014.[^philstar-2014-05-12-fear-of-the-dark]
- **[P]** 3 Oct 2014 (PSE FIX/ITCH project session, Q&A issue #4): "Will PSE implement broker anonymity once ITCH goes live? We will implement broker anonymity but not on Go-Live. Hence, we included the messages in the final ITCH specs so vendors can just switch 'on' and 'off' broker anonymity feature so that no software release is needed once we decide to implement it."[^pse-fix-itch-session-week01-2014-10-03:11] XTS went live on 22 Jun 2015.[^pse-psetrade-xts-page]
- **[P, absence]** Neither the Jan 2026 nor the Jul 2026 new-engine broker-forum decks list broker anonymity among the "major changes" (lot size, tick size, Run-Off/Trading-at-Last, negotiated trades).[^pse-nte-user-group-2026-01-15:9-11][^pse-nte-broker-forum-2026-07-09:7-8]

**1.4 Block sales, crosses, odd lots, auctions**
- **[P]** In Total View the Trade message [P]/[p] is used "to publish intentional cross, block and manually entered (market control) trades only"; ordinary and auction executions use [E]/[e] and [C]/[c]. In Basic, [P]/[p] publishes all trades. Trade Indicator: blank regular, 'C' intentional cross, 'B' block sale, 'M' manual (market control).[^pse-itch-equities-feed-spec-v2-3:18,28] During testing the PSE restated the mapping: negotiated deals (cross, block) "go to Trade[p]".[^pse-fix-itch-session-week06-2014-11-07:20]
- **[P]** Block trades are reported by the trading participant through a FIX Trade Capture Report; the counterparty confirms or declines; "the exchange confirms the Confirmed Trade to all involved parties".[^pse-fix-specification-v2-5:34-35]
- **[P]** Odd lots trade on a separate board: the Orderbook Directory [R] "Group" field is N (normal), O (odd lot) or I (index), so odd-lot orderbooks are separate instruments in the feed.[^pse-itch-equities-feed-spec-v2-3:11-12] The new engine removes the odd-lot market (Section 1.6).
- **[P]** Public end-of-day reporting of block, odd-lot and VWAP trades: the free Daily Quotation Report lists odd-lot volume/value, and each block sale with price, volume and value (no broker IDs); later reports also list VWAP-facility trades.[^pse-dqr-2023-05-31:11][^pse-dqr-2026-08-28:11] The DQR is published as a PDF at `documents.pse.com.ph/market_report/<Month DD, YYYY>-EOD.pdf`.[^pse-daily-quotation-report-series]

**1.5 What the free public side shows**
- **[P]** The DQR (free PDF) gives per issue: closing bid/ask, open/high/low/close, volume, value, net foreign buying/(selling); sector and index summary (PSEi, All Shares); number of trades, advances/declines; foreign buying, selling and net totals; securities under suspension.[^pse-dqr-2023-05-31:1,11-12] The format added a dated header and a VWAP section between 2023 and 2026; the 2026-08-28 report is the current layout.[^pse-dqr-2026-08-28:11-12]
- **[P]** Delayed data: "at least fifteen (15) minutes" delayed data is available only through PSE-licensed data vendors.[^pse-data-products-page]

**1.6 Change scheduled: Nasdaq Eqlipse "new trading engine" (NTE)**
- **[P]** 22 May 2025: PSE announced the agreement to adopt Nasdaq Eqlipse; it continues the Nasdaq relationship that supplies PSEtrade XTS.[^pse-new-trading-engine-page]
- **[P]** As of the 9 Jul 2026 broker forum: certification for brokers' own front-ends 10-23 Sep 2026; pre-production connectivity 29 Sep-9 Oct; pre-production testing 12-22 Oct; Saturday market rehearsals 31 Oct, 7 Nov and 14 Nov 2026; **go-live 23 Nov 2026**.[^pse-nte-broker-forum-2026-07-09:9] No parallel run; "big bang" cutover.[^pse-nte-faq-2026-08:1] I found no later primary document re-confirming or moving the date (labelled: as of 9 Jul 2026).
- **[P]** Market data on the NTE: two protocols, ITCH and "MDF" (Nasdaq market data feed), each on "their own dedicated TCP connections and incoming data feeds"; both delivered over SoupBinTCP but with different message formats. Final specs were released to brokers and vendors on 23 Jul 2026.[^pse-nte-faq-2026-08:2-3] The PSE site lists ITCH and MDF specification versions v1.0 (29 Jan 2026), v1.1 (8 Jun 2026), v1.2 (17 Jul 2026), "please contact" the PSE market-data e-mail; they are not public.[^pse-new-trading-engine-page] Static-data file specs (securities, index members, DDS exchange rate) dated 22 Jun 2026 are public.[^pse-securities-static-data-file:4][^pse-index-member-static-data-file:4]
- **[P]** Content changes announced for the NTE feeds: cross-trade information is provided "through the Cross Indicator field in the Order Executed with Price [C] and Trade [P] messages"; negotiated-trade details are disseminated "through the Market Data Feed as news/announcement".[^pse-nte-faq-2026-08:3]
- **[P]** Trading-rule changes that change what the feed shows: standard lot size 1 share (so "the Odd Lot Market will no longer be available"); only limit orders on day 1; orders in the Run-Off/Trading-at-Last period can be entered, modified and executed only at the closing price; a Negotiated Trade facility (price within +/-5% of the full-day VWAP, four decimals, no volume/value limit, execution window 15 minutes after Run-Off/Trading-at-Last, one-firm trades only), which does not replace the block sale.[^pse-nte-faq-2026-08:1][^pse-nte-broker-forum-2026-07-09:7-8][^pse-cn-2025-0046-board-lot-trading-at-last:3-5]
- **[P]** Vendor/broker obligations: a sublicensing agreement with the PSE (required under the PSE's licence with Nasdaq) for access to Eqlipse interfaces and documentation; recertification of front-end systems; new leased lines (2 Mbps minimum).[^pse-nte-user-group-2026-01-15:4-5,7] Readiness at 9 Jul 2026: 7 data vendors and 21 trading participants with market data; of 28 respondents 19 analysing specs, 10 developing, 12 not started, 6 not responding.[^pse-nte-broker-forum-2026-07-09:6]
- **Unknown:** whether the new ITCH/MDF carries broker IDs on executions or has an anonymity switch (the specs are not public). The FAQ's references to [C] and [P] use the upper-case names that the old spec reserved for the anonymous variants, but the Nasdaq message names may simply differ; I do not infer anything from that.

### Inferences
- **[I]** For XTS as of 2026 the working assumption should be: resting orders anonymous; executions and trades identified by broker whenever the exchange has anonymity switched off. This is consistent with (a) the PSE's 2014 statement of current practice, (b) the 2014 "not on go-live" answer, (c) the unchanged 2018 spec, (d) the CTF/FIX contra-broker fields, (e) local broker-flow screens. It is not proven for 2026; the decisive test is a vendor sample of ITCH [e]/[c]/[p] messages with non-blank broker fields.
- **[I]** Because [e]/[c] give both passive and active broker IDs, the tape reveals not only who traded but which side was resting, so aggressor-broker footprints are reconstructible even without order-level attribution.
- **[I]** Because [A]/[U]/[D] carry order numbers, an algo can track each resting order's life (cancel/replace behaviour, refresh patterns) without any broker attribution; "visible" size in [O] implies iceberg/disclosed-quantity orders show only the disclosed part (the spec says "visible shares").
- **[I]** Odd-lot books being separate instruments means board-lot-only depth models must exclude group "O"; after 23 Nov 2026 that group should disappear.

### Gaps
- No PSE statement from 2015 to 2026 about whether Broker Anonymity was ever enforced (absence found, not proof). Ask a vendor or broker for live samples.
- New-engine ITCH/MDF specifications (v1.2/final) are not public; broker-ID treatment, depth limits and message layouts are unknown.
- How retail platforms (PSETradeX, local brokers) truncate or label depth is undocumented in what I retrieved.
- Whether the PSE's historical "Orderbook Data" and "Per Trade Data" products include broker IDs is not stated.
- The Rappler and Philstar items are the only sources for the January/May 2014 plan details (secondary).

### Execution implications
1. **Information leakage:** assume every fill prints your broker's code (buy-broker and sell-broker on [p]; active/passive on [e]/[c]) and that vendors sell broker net-buy/sell analytics. For parent orders of any size, use several brokers, avoid one code carrying a multi-day programme, and consider the block/cross/negotiated routes (post-trade reporting only, no broker ID in the public DQR list) for size.
2. **Pre-trade is anonymous at order level:** no queue-attribution signal, but MBO order numbers let you model resting-order behaviour directly; do not rely on broker-code queue reading.
3. **Rebuild stats yourself:** ITCH has no high/low/last; volume must combine [E]/[e]/[C]/[c] with [P]/[p] (only for cross/block/manual in Total View), honour the Printable flag and [B] broken trades.
4. **Closing mechanics matter for sizing:** [I] gives live indicative closing price/quantity during pre-close; the no-cancel window starts at 2:48 pm and Run-Off/Trading-at-Last at 2:50 pm per the PSE site table (another chapter owns the trading-session detail; verify there).[^pse-investing-page]
5. **23 Nov 2026 cutover:** plan a protocol switch (ITCH and MDF both new), lot size 1 and a streamlined tick table, no odd-lot book, negotiated trades arriving as news items rather than book events, and a Nasdaq sublicence; with no parallel run, keep a fallback to EOD files and a rollback plan.

---

## 2. Data products, feeds, vendors, licensing and latency

### Takeaway
The PSE sells real-time ITCH data (Total View, Basic, Index, News) directly or through licensed vendors; delayed data (at least 15 minutes) only through vendors; end-of-day text files by FTP; paid historical data (including per-day order-book and per-trade files); reports; and index services. Real-time fees and latency figures are not public. The only published fee schedules are the non-display-usage (NDU) policy (USD 7,500 per quarter for automated trading and for derived data, USD 900 a year for other uses; effective 1 Oct 2017), the historical-data price list, the index bundle (USD 500 one-time plus USD 500 a year) and the listed-company stock feed (PHP 10,000 to 45,000). The feeds are TCP (SoupBinTCP) over leased lines, with co-location and cross-connect offered at the PSE.

### Cited Findings

**2.1 Product catalogue (PSE "Data Products" page, retrieved 6 Oct 2026)**
- **[P]** Real-time: ITCH Equities Data Feed in three variants (Total View, Basic, Index), "available directly from the Exchange or through PSE's licensed Data Vendors (list of data vendors available upon request)"; applications go to the Market Data Department (market.data@pse.com.ph per the forms).[^pse-data-products-page][^pse-data-feed-application-form:1]
- **[P]** Delayed: "Delayed market information by at least fifteen (15) minutes may be sourced through PSE's licensed Data Vendors."[^pse-data-products-page]
- **[P]** Non-display usage (NDU) is a separate licence: use of real-time data "for automated trading applications or for the creation of new products, where the raw data is not displayed".[^pse-data-products-page]
- **[P]** News: the Corporate Announcements Feed (CAF; e-mail or FTP, PDF and HTML, "as soon as the documents have been uploaded in the PSE EDGE website") and the ITCH News Feed ("trading announcements, ETF iNAV, system events, listed company announcements and exchange notices").[^pse-data-products-page]
- **[P]** Connectivity: "Co-Location and Cross-Connect services for Trading Participants and Data Vendors".[^pse-data-products-page]
- **[P]** End-of-day (EOD): text files by FTP, also via vendors: Daily Quotation Report (price, volume, value, net foreign for all listed securities, plus index and sector/board summaries); Market Data EOD file; Last Traded Price file; Market Capitalization file (last prices, outstanding shares, free-float shares).[^pse-data-products-page]
- **[P]** Reports: monthly Foreign Ownership Level report (Excel by e-mail); PSE Weekly Report; PSE Monthly Report; monthly Trading Participants Ranking Report (ranked by value turnover).[^pse-data-products-page]
- **[P]** Index services: Index Licensing (required for funds tracking PSE indices; gives use of the index and trademarks, a complimentary EOD file of the licensed index, and announcements of constituent, weight or float changes); Index Bundle (PSEi EOD file by FTP, e-mail announcements on recomposition and rebalancing, quarterly index free-float file); ETF Index Licensing (for ETFs naming the PSE as index provider).[^pse-data-products-page]

**2.2 Protocols, connectivity and latency**
- **[P]** ITCH over SoupBinTCP v3.0 (point-to-point), with MoldUDP64 ("a sequenced and recoverable UDP multicast stream") named for one-to-many distribution; timestamps in nanoseconds since the last seconds message.[^pse-itch-equities-feed-spec-v2-3:7,9] The data page says the feed "broadcasts data directly from the trading engine".[^pse-data-products-page]
- **[P]** XTS-era connectivity: leased line 1 Mbps minimum, 2 Mbps recommended; handover serial V.35 or Ethernet copper (recommended); a dropwire option for Ayala Tower 1 tenants.[^pse-psetrade-xts-page] NTE-era: dropwire 100 Mbps (PSE Tower BGC tenants only), leased line 1 Mbps minimum and 2 Mbps recommended, Ethernet copper handover; new parallel leased lines at 2 Mbps minimum were to be in place by May 2026 (PLDT, ETPI, Globe named as carriers).[^pse-new-trading-engine-page][^pse-nte-user-group-2026-01-15:7]
- **[P]** No latency, throughput or SLA figures are published. The PSE's "Data Feed Infra" section for the new engine is marked "Coming Soon".[^pse-new-trading-engine-page]
- **[P]** Not everything is in ITCH: in Oct 2014 the PSE listed 11 static fields not carried in ITCH (stock code, long and short names, previous close (LACP), par value, strike price, PN status, Shariah indicator, float level, capitalization adjustment coefficient, sector mapping) and said it would supply them in a daily file.[^pse-fix-itch-session-week01-2014-10-03:9] The current (22 Jun 2026) Securities Static Data file (pipe-delimited) carries stockcode, long/short names, sector/sub-sector, listing date, par value, LACP and short-sell eligibility (B buyback only / Y short-sell and buyback / N neither); the Index Member Static Data file carries only `indexcode|seccode`.[^pse-securities-static-data-file:4][^pse-index-member-static-data-file:4] ITCH Index [Y] gives member weights at start of day.[^pse-itch-equities-feed-spec-v2-3:13]

**2.3 Licensing and published fees**
- **[P]** Non-Display Usage Policy Guidelines v1.0 (announced 1 Jun 2017; fees effective 1 Oct 2017 for existing end-users, new users to licence on request): (A) Automated Trading Application, USD 7,500 per quarter; (B) Derived Data (index/product creation that cannot be reverse-engineered), USD 7,500 per quarter; (C) Other applications (funds administration, risk, portfolio valuation, quant analysis), USD 900 per year; one-time fee waived; counted per legal entity (affiliates and subsidiaries count separately); fees cover unlimited programmes within a category; delayed and EOD data are not subject to the fees; a Data License Agreement is needed if raw data is displayed or redistributed. "Algorithmic trading, program trading or the automated monitoring of trading activities (in compliance with the PSE Rules on Direct Market Access (DMA))" is the named example of category A.[^pse-non-display-usage-policy-2017:1-3]
- **[P]** The Data Feed Application Form asks about redistribution to clients, entitlement control, usage reporting, direct vs vendor connection, network topology and affiliates, and lists subscription types: ITCH Basic (Level 1), ITCH Total View (Level 2), ITCH Index, ITCH News, Delayed Feed with and without order book (via data vendor), End-of-Day Feed Full (PHIP), End-of-Day Index (IDX), End-of-Day PSEi, Creation of Customized Index.[^pse-data-feed-application-form:1-3]
- **[P]** Standard subscriber terms (EOD/historical forms): personal or internal business use only; no redistribution, including on web pages, without a PSE-approved access-control mechanism; PSE may amend fees on 30 days' written notice; trading participants' subscription fees are billed on the PSE invoice; breaches carry fines and penalties, with arbitration at the Philippine Dispute Resolution Center.[^pse-market-data-subscription-form:2]
- **[P]** Index Bundle: USD 500 one-time charge and USD 500 annual subscription (VAT exclusive) for the PSEi EOD file, recomposition e-mails and the quarterly free-float report.[^pse-index-subscription-bundle-form:1]
- **[P]** Historical data price list (PHP, per request; from the PSE page): Orderbook Data, Excel, all securities, per day, **PHP 10,000** (earliest 1998); Per Trade Data, Excel, all securities, per day, **PHP 7,500** (earliest 1998); Market Capitalization (with outstanding shares and last traded price) PHP 320 per period-end (from 2008); Daily Foreign Buying and Selling PHP 240 per security-year (1998); Daily Market Indices OHLC PHP 240 per index-year (2007); Daily OHLC/volume/value/trades PHP 240 per security-year (1997); Daily Quotation Report PDF PHP 100 per day; Public Ownership PHP 720 per quarter (2006); List of Index Members per Recomposition PHP 160 per period-end (1994); Financial Ratios PHP 1,760 and Financial Information PHP 1,680 per quarter (2006); BOD and Officers PHP 3,040.[^pse-data-products-page]
- **[P]** Listed Company Stock Feed (LCSF): web service for display exclusively on listed companies' websites; snapshot every minute, delayed 15 minutes; XML or JSON; IP whitelisting; fields: symbol, security name, last traded price, open, high, low, previous close, change, %change, volume, value, average price, 52-week high/low, date of previous close. Fees: basic subscription one-time PHP 10,000 plus annual PHP 30,000 (either format) or PHP 45,000 (XML+JSON bundle); extra website PHP 10,000 or 25,000; additional security PHP 20,000 or 35,000; additional listed company PHP 20,000 or 35,000.[^pse-listed-company-stock-feed-brochure:2]
- **[P]** Real-time ITCH subscription fees are not published anywhere I could retrieve ("contact market.data@pse.com.ph").[^pse-data-products-page]
- **[P]** Market data was about 6% of PSE revenue in the first nine months of 2014 (PHP 66m against PHP 55m a year earlier); the 2015 plan listed "collaboration with Deutsche Boerse on market data products".[^pse-tokyo-roadshow-2015-01:23,29]

**2.4 Vendors**
- **[P]** The PSE keeps the vendor list "available upon request" and defines Direct Data Vendors (connected directly to PSE market-data servers) and Indirect Data Vendors (receiving via direct vendors).[^pse-data-products-page][^pse-non-display-usage-policy-2017:1] Seven data vendors were in the new-engine migration programme at 9 Jul 2026.[^pse-nte-broker-forum-2026-07-09:6]
- **[P]** ICE lists PSE as a data set delivering "streaming data for equities and indices, including Level 1 and Level 2 pricing via ICE Consolidated Feed", through ICE Connect Desktop, ICE XL and enterprise integration; it gives no fee, latency or vendor-chain information.[^ice-developer-pse]
- **Not documented in what I retrieved:** Bloomberg, LSEG (Refinitiv) and local-vendor product pages for PSE.

**2.5 EOD and back-office files (formats)**
- **[P]** EOD "PHIP" file (`PHIPyyyymmdd.txt`, fixed width): per issue traded, trade date, symbol, name, closing best bid/offer, open, high, low, close, previous close, total volume and value; index records for PSE Composite, All Shares and sectoral indices (open, high, low, close, volume, value).[^pse-eod-market-data-spec-v1-3:2]
- **[P]** MCAP file (`MCAPmmdd.txt`, fixed width, spec dated 26 Feb 2016): close/last price, outstanding shares and "market float shares = outstanding shares x float factor / 100" (rounded up), by sector.[^pse-mcap-eod-spec-v1-0:2] This is the float basis used for index replication (Section 4).
- **[P]** Trading-participant EOD files (CTF, ABC, Quote, Price.lis) move to the new PSE Portal; the Daily Transaction Report is discontinued; the Aug 2026 FAQ says the ABC and CTF specifications do not change and negotiated trades will appear in the CTF.[^pse-nte-user-group-2026-01-15:19][^pse-nte-faq-2026-08:2]

### Inferences
- **[I]** For a hedge fund running algorithms on a vendor-delivered Level 2 feed, the PSE's own recurring charge is the NDU licence: category (A) alone is USD 30,000 a year per legal entity, and categories (A)+(B) are USD 60,000; vendor, line and co-location costs sit on top.
- **[I]** At the published historical prices, one year (about 250 trading days) of per-day order-book data is about PHP 2.5m and per-trade data about PHP 1.9m (arithmetic from the list above); sampling event days is the economical route.
- **[I]** "Delayed Feed with Order Book (via Data Vendor)" on the application form implies a delayed Level 2 vendor product exists, but I found no vendor documentation.
- **[I]** The NDU policy is dated 2017 and still the only public one; the new engine's licensing (a Nasdaq sublicence for Eqlipse interfaces) may add terms I cannot see.

### Gaps
- Real-time ITCH fees, vendor list, vendor-side latency and any PSE latency/throughput statistics.
- Whether the NDU fee schedule has been revised since 2017 (no later public policy found).
- Content of the historical Orderbook/Per Trade files (fields, broker IDs, timestamps).
- Bloomberg/LSEG coverage specifics; how delayed Level 2 is priced.

### Execution implications
1. Budget the licence stack: vendor feed, NDU (A) USD 30,000 a year per legal entity (plus (B) if you build derived signals), line or co-location at the PSE.
2. Use Total View (Level 2) for any execution logic; Basic is top-of-book only, so queue-depth, imbalance and closing-auction signals need Total View.
3. Do not expect statistics in the feed (no high/low/last), nor static fields (sector, LACP, short-sell flag); join the static and MCAP/PHIP files by symbol every morning and reconcile against the DQR.
4. Build with the protocol change in mind: from 23 Nov 2026 the data arrive as new ITCH and MDF streams over separate SoupBinTCP sessions; test in the PSE's customer test environment (credentials separate for market data and FIX).[^pse-nte-broker-forum-2026-07-09:4]
5. Latency: no public benchmark; if latency matters, measure from your own timestamps against ITCH nanosecond offsets and compare vendor vs direct paths; the exchange offers cross-connect/co-location only to trading participants and data vendors, so a fund generally reaches the feed through its broker or a vendor.


---

## 3. Corporate-disclosure dissemination (PSE EDGE) and disclosure-linked halts (brief)

### Takeaway
Disclosures are filed on PSE EDGE (in use since 27 Dec 2013) and released after Exchange approval; since **25 May 2026** the same-day posting cut-off is **4:00 pm** (it was 3:30 pm from 1 Mar 2022). Machine-readable channels are the ITCH News feed and the e-mail/FTP Corporate Announcements Feed (CAF); I found no public EDGE API. Issuers must disclose material information to the PSE within 10 minutes and before any media release; if the news arises in trading hours the issuer must request a halt, lifted one hour after dissemination (next trading day if released within an hour of the close). EDGE was unavailable for part of 19 Jan 2026, which shows the fall-back path (PSE website plus an e-mail "emergency disclosure" route).

### Cited Findings

**3.1 System, channels and timing**
- **[P]** PSE EDGE (Electronic Disclosure Generation Technology) has been used for all corporate disclosures and PSE listing/disclosure notices since 27 Dec 2013 (PSE Memorandum DA-2013-0726).[^pse-listing-disclosure-rules:138]
- **[P]** Release timing rule in force today: effective **25 May 2026** (CN-2026-0024 dated 22 May 2026) the EDGE posting cut-off is 4:00 pm; disclosures received on or before it, "including end-of-day disclosures of exchange traded funds", are released the same trading day; later ones are posted the next trading day; the submission system stays open after the cut-off but late items follow the next-day schedule.[^pse-cn-2026-0024-edge-cutoff-4pm:1] It replaced the 3:30 pm cut-off set by CN-2022-0010 (24 Feb 2022), effective 1 Mar 2022 "until further notice" when the PSE returned to a five-hour trading day.[^pse-cn-2022-0010-edge-cutoff-330pm:1] The Jan 2025 Consolidated Listing and Disclosure Rules still print the 3:30 pm figure (Guidance Note 15) and are therefore out of date on this point.[^pse-listing-disclosure-rules:139]
- **[P]** Disclosures pass through an approval step: listed companies may post a disclosure on their own sites "only upon receipt of the approval email from the Exchange or upon posting of the disclosures in the Exchange's website".[^pse-listing-disclosure-rules:138] The CAF "Upload Date and Time Stamp" is defined as "the date and time the disclosure and/or notice is approved for dissemination".[^pse-caf-spec-v6-0:4]
- **[P]** CAF (market-data product): each announcement e-mailed (subject line pipe-delimited: feed type | reference number | upload timestamp | title | symbol | PSE form number), with a URL to the document; FTP server holding the running 30 days; an end-of-day e-mail digest of all announcements. Reference formats: structured filings CRnnnnn-yyyy, unstructured announcements Cnnnnn-yyyy, listing notices LNnnnnn-yyyy, disclosure notices DNnnnnn-yyyy. Spec v6.0 dated 9 Sep 2019.[^pse-caf-spec-v6-0:2-5]
- **[P]** ITCH News feed (since spec v2.1, 2 Mar 2015): company disclosures and exchange notices submitted through EDGE are sent as News Item [N] messages; FirmId "EXCH"; Title = the disclosure template name (examples "(4-34) Voluntary Trading Suspension", "(17-2) Quarterly Report", "MJIC - Trading Halt"); Reference = the EDGE URL; NewsText carries the reference number and timestamp; orderbook = 0 for listing and disclosure notices. "The disclosures will be released every trading day. Disclosures released when the trading engine is not available will be sent the next trading day."[^pse-itch-equities-feed-spec-v2-3:3,30-31] ETF iNAV items are sent every minute on the same message type.[^pse-itch-equities-feed-spec-v2-3:29]
- **[P]** The EDGE document links in the feeds are `edge.pse.com.ph/openDiscViewer.do?edge_no=<id>` and `downloadPdf.do?edge_no=<encrypted>`; the specs describe no query API.[^pse-itch-equities-feed-spec-v2-3:30][^pse-caf-spec-v6-0:4] (`edge.pse.com.ph` also rejected non-browser clients when I tried it.)
- **[P]** New engine: negotiated-trade details will "be disseminated through the Market Data Feed as news/announcement".[^pse-nte-faq-2026-08:1,3]

**3.2 Issuer duties that set the timing**
- **[P]** Material information (Art. VII Sec. 4.1): disclose to the Exchange "within ten (10) minutes from the receipt of such information or the happening or occurrence of said act, development or event. Disclosure must be made to the Exchange prior to its release to the news media"; the original must follow within 24 hours.[^pse-listing-disclosure-rules:139]
- **[P]** Selective disclosure of material non-public information is prohibited unless disclosed simultaneously to the Exchange (exceptions: persons bound by confidence, or by written undertaking).[^pse-listing-disclosure-rules:140-141]
- **[P]** The Exchange may request an issuer to confirm or deny market rumours; issuers must reply before the next pre-open if asked outside hours; if the issuer fails to confirm or deny, a trading halt follows that "shall be lifted at 10:00 a.m. even in the absence of any reply".[^pse-listing-disclosure-rules:145]

**3.3 Disclosure-linked halts (brief; the halt chapter owns the detail)**
- **[P]** If the event occurs during trading hours the issuer "must request a halt in the trading of its shares"; if it occurs after hours and cannot be disclosed before the next pre-open, the issuer must also request a halt; "in both cases, the trading halt shall be lifted one (1) hour after the information has been disseminated"; if disseminated one hour or less before the close, the halt lifts on the next trading day. Exceptions: soft information, or where disclosure would breach law. In a "Trading Halt" orders other than cross transactions can still be posted, modified and cancelled; in a suspension they cannot.[^pse-listing-disclosure-rules:140]
- **[P]** Additional-listing transactions that rely on the exceptions to the rights/public-offering requirement (Art. V Part A Sec. 5; placing-and-subscription deals are covered by Guidance Note 10): a one-hour halt on announcement and another one-hour halt on dissemination of the Comprehensive Corporate Disclosure, which is due within five trading days of the initial disclosure.[^pse-listing-disclosure-rules:101-102]
- **[P]** Example, 19 Jan 2026: the Exchange imposed a one-hour halt on MRC Allied (MRC) from 9:30 to 10:30 am after its disclosure of a 315m-share issuance.[^pse-cn-2026-0004-2-emergency-disclosures-trading-halt:1-2]
- **[P]** Feed signalling: a halt appears as [H] "T"+"H" (halted) and the halt auction as [I] type "I" (intra-day auction); lifting returns "T"+"N".[^pse-itch-equities-feed-spec-v2-3:14,18,26]

**3.4 EDGE outage and fall-back (19 Jan 2026)**
- **[P]** CN-2026-0003 (19 Jan 2026): "The PSE disclosure system is currently unavailable"; the public was told to check the PSE website; issuers unable to reach EDGE could e-mail disclosure@pse.com.ph with subject "Emergency Disclosure [stock symbol] - [template, e.g. 4-30 Material Information]".[^pse-cn-2026-0003-1-edge-unavailable:1] CN-2026-0006 (same day): EDGE systems accessible again at edge.pse.com.ph.[^pse-cn-2026-0006-edge-accessible:1]

**3.5 Trading hours for context**
- **[P]** The PSE site's current schedule lists pre-open 9:00, pre-open no-cancel 9:15, open 9:30, recess 12:00, resume 1:00 pm, pre-close 2:45, pre-close no-cancel 2:48, Run-off/Trading-at-Last 2:50, Closing VWAP Session 3:00, close 3:15 pm; the same page still carries an older table (close 3:30 pm).[^pse-investing-page] The trading-session chapter should confirm the effective dates; they are not established here.

### Inferences
- **[I]** Because release follows an approval step and the cut-off is a posting rule, the public timestamp can lag the issuer's own filing time; the only machine-readable timestamps are CAF's approval time and ITCH News arrival time. Any event study should use those, not the template's "date of event".
- **[I]** After-hours items filed after 4:00 pm are posted the next trading day, so they reach the market with the pre-open (9:00) order-entry window; an issuer that cannot file before pre-open must request a halt, so the open can be delayed until an hour after release.

### Gaps
- No public EDGE API, SLA or latency statistics; no published list of what share of disclosures are released after 3:15 pm.
- Whether the Closing VWAP Session and the 3:15 pm close alter the halt-lifting arithmetic ("one hour or less before the close") is not documented; the Jan 2025 rules text predates the 4:00 pm cut-off.
- The Jan 2026 outage notices do not state what time EDGE failed or recovered.

### Execution implications
1. Subscribe to the ITCH News feed (or CAF) rather than scraping EDGE; key the news handler on the reference number and treat template codes as event types (4-xx unstructured, 17-xx structured).
2. Expect a halt at the moment of a material in-hours release; halted books still accept orders and cancels (not crosses), then re-open through an intraday auction ([I] type "I"); size and price orders for the auction rather than for continuous matching.
3. Pre-position for the 9:00 pre-open when news posts after the 4:00 pm cut-off; the 10-minute and "before media" rules mean the PSE copy should be the first public one.
4. Have a second news path for EDGE downtime: the PSE website and the emergency e-mail route were used on 19 Jan 2026.


---

## 4. PSEi methodology, review calendar, recent constituent changes and event-day behaviour

### Takeaway
In force today (6 Oct 2026) is the PSE "Policy on Index Management" in its January 2024 version: 30 stocks, free-float-adjusted and uncapped, main-board common stocks listed at least 12 months, free float at least 20%, liquidity = top 25% by median daily value in 9 of 12 months, final pick = 30 largest by full market capitalisation (12-month VWAP basis), insert at rank 25 or better and delete at rank 36 or worse, reviewed twice a year with a 3-to-5-trading-day notice and effect at the open of a Monday. A **revised policy announced 21 Jul 2026 (CN-2026-0033/0033B) takes effect only at the February 2027 rebalance**: new MTAR and MADV liquidity tests, a 98% cumulative market-cap screen, a 15% float exception for stocks of PHP 250bn or more, and four-period persistence rules for rank-based entry and exit. Between Feb 2023 and Aug 2026 the PSEi had seven membership-changing events (ten stocks swapped in) and three unchanged reviews (table below); China Banking (CBC), added at the Feb 2025 review, rose 38.9% on the last trading day before inclusion, on 62.9m shares (PHP 5.6bn) against a median daily value of about PHP 63m.

### Cited Findings

**4.1 The index family and calculation**
- **[P]** PSE Index Series: PSEi, six sector indices (Financials, Industrial, Holding Firms, Property, Services, Mining & Oil) and the All Shares Index (all common stocks, full market capitalisation, SME board excluded); all free-float-adjusted except All Shares. PSEi: fixed basket of 30, base 1,022.045 at 28 Feb 1990; the name "PSEi" dates from April 2006.[^pse-index-policy-2024:2-3] The PSE MidCap and PSE Dividend Yield (DivY) indices (20 members each, base 1,000 at 30 Dec 2010) were launched on 28 Mar 2022 and have their own policies; the PSEi Total Return Index was launched 4 Feb 2019 (base 1,000 at 28 Dec 2007, calculated at end of day).[^pse-indices-page][^pse-midcap-index-policy-2024:2-4][^pse-divy-index-policy-2024:3-4]
- **[P]** Calculation (Jan 2024 policy): last traded prices; base calculation every 15 seconds, broadcast every 60 seconds, two decimals; index level = sum(price x shares outstanding x free-float factor) divided by a base capitalisation, times the previous close; adjustments for stock dividends, rights, splits; computed and broadcast through the trading engine to members and vendors.[^pse-index-policy-2024:3,13-14] The ITCH Index feed carries index values [Z] and the member directory with weights [Y] at start of day.[^pse-itch-equities-feed-spec-v2-3:13,24]
- **[P]** No weight cap applies to the PSEi: the formula has no cap term; a 10% cap on the highest weight appears only in the DivY formula of the July 2026 policy.[^pse-index-policy-2024:13][^pse-cn-2026-0033:17] At end-Sep 2025 the largest PSEi weight was ICTSI at 14.0%; top five (ICT, SM, BDO, BPI, SMPH) = 50.6%; sector weights Financials 24.6%, Industrial 15.4%, Holding Firms 26.1%, Property 13.1%, Services 20.8%, Mining & Oil 0%; full market capitalisation of the 30 stocks PHP 8,588.8bn (sector free-float capitalisations sum to about PHP 3,473bn by my addition).[^pse-psei-factsheet-2025-09:2] These weights are 12 months old and the membership has since changed; current weights and float factors are by subscription (Section 2).
- **[P]** Corrections: errors above 0.10% are corrected only if found within 10 trading days; correction is made the trading day after discovery and announced in the Daily Quotation Report, with vendors e-mailed.[^pse-index-policy-2024:14]

**4.2 In-force rules (January 2024 policy, valid to the Feb 2027 rebalance)**
- **[P]** Eligibility: common stocks on the main board listed at least 12 months in the review period; foreign companies also listed abroad excluded from the PSEi; convertible preferreds, ETFs/funds and dollar-denominated securities excluded; companies expected to be untradable for a significant period in the next six months (delisting proceedings, suspension) ineligible.[^pse-index-policy-2024:5]
- **[P]** Free float must be **at least 20%** of outstanding shares at the end of the 12-month review period; the policy notes "effective December 2022. Prior to this, the free float requirement for index inclusion is 15%". Deducted as strategic: founders, directors, officers and families; pension and social-security funds (SSS, GSIS) only when the fund holds a board seat (clause amended by CN-2024-0008 on 26 Jan 2024, to "take effect immediately"); restricted or locked-up shares; treasury; ESOP; affiliates; holders of 10% or more; controlling shareholders and voting trusts. PCD Nominee lodgements, PDR underlyings and depositary-receipt underlyings count as free float unless the holder has 10% or more or is strategic; for dual-listed firms only shares traded on the PSE or held by locally domiciled investors count. Data source: quarterly Public Ownership Reports.[^pse-index-policy-2024:5-7][^pse-cn-2024-0008:1]
- **[P]** Liquidity: median daily trading value of the regular board per month (zero-trade days included); a PSEi stock must rank in the **top 25% by median daily value in 9 of the 12 months**; if fewer than 30 qualify the Management Committee may widen in 5-point steps; sector indices need top 50% in 8 of 12 months.[^pse-index-policy-2024:7]
- **[P]** Selection: eligible stocks ranked by full market capitalisation using the 12-month VWAP (all share classes and PDRs combined); the 30 largest form the PSEi; the PSE may apply financial criteria to new entrants. Rank rules: **insert at rank 25 or better, replacing the lowest-ranked member; delete at rank 36 or worse**, replaced by the highest-ranked eligible stock.[^pse-index-policy-2024:8-9]
- **[P]** Calendar: semi-annual review; Jan-Dec data drives the February recomposition ("mid-February"), Jul-Jun data the August one ("mid-August"); announcement "as much as practicable, five trading days prior to their implementation" by press release and website memorandum.[^pse-index-policy-2024:9]
- **[P]** Off-cycle: removal on delisting, loss of eligibility or loss of a reliable price, with replacement "simultaneously, no later than five (5) trading days from the announcement"; **early inclusion** for stocks listed at least 6 months if rank 25 or better by market capitalisation at the end of the review period, within the float rule, and in the top 20% by median daily trade for at least 6 months or 75% of the months listed (whichever is higher); merger: survivor stays; a suspended constituent may stay up to 10 business days at its last price, after which the Management Committee decides, and a removed stock must wait for the next regular review.[^pse-index-policy-2024:10-11]
- **[P]** Float and share updates: full float review each semi-annual recomposition (end-Dec and end-Jun POR) regardless of size; float levels re-based on end-Mar and end-Sep POR with effect each May and November only if the cumulative change is at least 5%; offerings reflected after an updated POR; float adjustments effective within five trading days of announcement; sector reclassification coincides with a membership change.[^pse-index-policy-2024:11-12]

**4.3 What replaced what (policy history)**
- **[P/S]** Float minimum 12% to 15%: the PSE announced with the Feb 2018 review that it "increased the minimum free float level requirement from 12 percent to 15 percent"; the Feb 2018 policy text says 15%.[^pse-pr-2018-02-no-changes-float-15pct][^pse-index-policy-feb2018:5]
- **[P]** Float 15% to 20%: announced in Aug 2021 for the review after the Aug 2022 recomposition ("This is the last index recomposition with a free float requirement of at least 15 percent. As announced in August 2021, companies should have a public ownership level of at least 20 percent to qualify for index inclusion in the next review period"); the Jan 2024 policy dates the 20% rule from December 2022.[^pse-pr-2022-08-semirara-in-security-bank-out][^pse-index-policy-2024:5] (The 2021 circular, CN-2021-0046, is archived but image-only and I could not read it.)
- **[P]** The liquidity rule (top 25% median daily value, 9 of 12 months) and rank cut-offs (25 / 35-36) are the same in the Feb 2018 and Jan 2024 texts; wording moved from "rises above the 25th / falls below the 35th" to "25th and above / 36th and below".[^pse-index-policy-feb2018:7,9][^pse-index-policy-2024:7,9]
- **[S]** A press account calls the July 2026 revision the biggest overhaul "in more than 15 years" replacing rules "largely unchanged since April 2011".[^insiderph-2026-07-index-overhaul]

**4.4 Revised policy announced 21 Jul 2026: not in force until the Feb 2027 rebalance**
- **[P]** CN-2026-0033 (and a re-issue, CN-2026-0033B,[^pse-cn-2026-0033b:1] whose text I found identical apart from the circular number) announces three amendments, "implemented in the February 2027 index rebalancing": (1) a 98% cumulative market-capitalisation threshold as an additional criterion; (2) MTAR and MADV as new liquidity measures "replacing the previous liquidity criterion"; (3) minimum free float 20% reduced to 15% for companies with market capitalisation of at least PHP 250,000,000,000.[^pse-cn-2026-0033:1]
- **[P]** Detail: only companies within the top 98% of the cumulative total market capitalisation of eligible securities qualify (PSEi, DivY, MidCap, sectors).[^pse-cn-2026-0033:6] **MTAR** = twelve-month cumulative sum of monthly ratios, each = (median daily value traded x number of days the security traded in the month) / free-float market capitalisation at month-end; required MTAR 15% for PSEi/DivY/MidCap entrants, 10% for existing constituents, 7% for sector indices. **MADV** = monthly total value / trading days; top 25% in 9 of 12 months for PSEi, MidCap and DivY (the MidCap threshold was top 35% under the 2024 MidCap policy), top 50% in 8 of 12 for sector indices; if too few qualify, MTAR may be lowered by one point at a time and the MADV bucket widened by five points at a time.[^pse-cn-2026-0033:7][^pse-midcap-index-policy-2024:3]
- **[P]** Float: at least 20%, or at least 15% where market capitalisation is PHP 250bn or more.[^pse-cn-2026-0033:8] Rank rules now include persistence: insert if rank 25 or better in the current review **or** rank 30 or better in four consecutive reviews; delete if rank 36 or worse **or** rank 31 or worse in four consecutive reviews; notice "at least five trading days" before implementation.[^pse-cn-2026-0033:11] Early inclusion now needs MTAR of at least 15% and top 20% MADV for at least six months or 75% of months listed.[^pse-cn-2026-0033:13] The DivY index gets a 10% weight cap applied before each rebalancing; all divisors are recalculated at each day's end for the next day, including "constituent changes scheduled for the next trading day".[^pse-cn-2026-0033:17]
- **[P]** The PSE president said (Aug 2026) that the next review, "which covers the January to December 2026 period, will utilize our revised index criteria that puts premium on the liquidity of a stock".[^pse-pr-2026-08-mynld-joins-psei]
- **[S]** Context from press accounts: a newly added stock "surged sharply in a single day as funds tracking the index scrambled to buy shares" despite meeting the float test; one internal estimate put the pool passing the 98% screen at about 100 companies; market chatter named Aboitiz Power and Synergy Grid as rising on possible inclusion and China Banking and DigiPlus as at risk.[^insiderph-2026-07-insider-info-overhaul][^insiderph-2026-07-index-overhaul]

**4.5 PSEi composition changes, 2023-2026 (effective date = first trading day of the new composition)**

| Effective | Announced | PSEi in | PSEi out | Basis |
|---|---|---|---|---|
| Mon 6 Feb 2023 | late Jan 2023 (about 27 Jan) | DMC, UBP | MEG, RLC | Jan-Dec 2022 review; [S] press report[^manilatimes-2023-01-28-dmc-ubp] |
| Mon 7 Aug 2023 | 28 Jul 2023 | none | none | Jul 2022-Jun 2023 review[^pse-cn-2023-0039:1][^pse-pr-2023-08-psei-retains-composition] |
| Tue 26 Sep 2023 (start of day) | 20 Sep 2023 | BLOOM, CNPF | AP, MPI | off-cycle, "recent developments in certain constituents"; identities by my diff of the circular lists [I][^pse-cn-2023-0044:1-2] |
| Wed 4 Oct 2023 (start of day) | 28 Sep 2023 | NIKL (by list diff [I]) | UBP | UBP's float cut below the 20% minimum after the PSE reclassified shares as non-public[^pse-cn-2023-0047:1] |
| Mon 5 Feb 2024 | 26 Jan 2024 | none | none | Jan-Dec 2023 review; PSEi list unchanged from Oct 2023 by my diff [I][^pse-cn-2024-0008:1-2] |
| Mon 12 Aug 2024 | 5 Aug 2024 | none | none | Jul 2023-Jun 2024 review[^pse-cn-2024-0042:1] |
| Mon 3 Feb 2025 | 24 Jan 2025 | AREIT, CBC | NIKL, WLCON | Jan-Dec 2024 review[^pse-cn-2025-0005:1] |
| Mon 18 Aug 2025 | 8 Aug 2025 | PLUS | BLOOM | Jul 2024-Jun 2025 review[^pse-cn-2025-0034:1] |
| Mon 2 Feb 2026 | about 27 Jan 2026 ([S] date; PSE release gives only the effective date) | RCR | AGI | Jan-Dec 2025 review[^pse-pr-2026-02-rcr-replaces-agi] |
| Mon 3 Aug 2026 | 27 Jul 2026 | MYNLD (early inclusion) | CNVRG | Jul 2025-Jun 2026 review[^pse-cn-2026-0035:1][^pse-pr-2026-08-mynld-joins-psei] |

- **[P]** The Aug 2026 release says MYNLD "is only the third company to qualify for early PSEi inclusion since we introduced this rule in 2021"; CNVRG moves to MidCap (with Philex in, Asia United out), AEV enters the DivY index, and RRHI was removed from MidCap and DivY on 16 Jul 2026 after a trading suspension following its tender offer, which cut its public float below the Exchange minimum.[^pse-pr-2026-08-mynld-joins-psei] Sector-index changes the same day: Industrial adds BSC, MYNLD, TOP and drops CIC, PPC, VITA; Financials adds BNCOM, NRCP; Holding Firms adds LPZ; Property drops VLL, VREIT; Services drops ALLDY, HOME; Mining & Oil adds OV.[^pse-cn-2026-0035:1]
- **[P]** PSEi members in force from 3 Aug 2026 (30): AC, ACEN, AEV, ALI, AREIT, BDO, BPI, CBC, CNPF, DMC, EMI, GLO, GTCAP, ICT, JFC, JGS, LTG, MBT, MER, MONDE, MYNLD, PGOLD, PLUS, RCR, SCC, SM, SMC, SMPH, TEL, URC.[^pse-cn-2026-0035:2]
- **[I]** Lead time from announcement to the last trading day before effect was 3 to 5 trading days (5 in Aug 2023, Jan 2024, Jan 2025, Aug 2025; 4 in Aug 2024 and Jul 2026; 3 in the two off-cycle moves of Sep-Oct 2023 and, if the 27 Jan date is right, Feb 2026), i.e. the "five trading days" is a target, not a guarantee. February effective dates were the first Monday of February in 2023, 2024, 2025 and 2026; August dates ranged from 3 to 18 August; the policy's "mid-February/mid-August" wording is stale.

**4.6 How a change is implemented**
- **[P]** Circulars say changes are "effected on" the Monday (semi-annual) or "effective on start of day" (off-cycle).[^pse-cn-2025-0005:1][^pse-cn-2023-0044:1][^pse-cn-2023-0047:1] The July 2026 policy states each day's divisor is recomputed at the end of the trading day for the next day, including constituent changes scheduled for it.[^pse-cn-2026-0033:17]
- **[I]** Hence the index switches membership between the last close before the effective date and the next open: an index fund must hold the new basket at that last close (Friday for a Monday effect). A press account describes the First Metro Philippine Equity Exchange Traded Fund (listed 2013) as the country's first and still only ETF (that it tracks the PSEi is my background knowledge, not shown in the sources I read); I found no figure for assets tracking PSE indices.[^insiderph-2026-07-etf-reboot]

**4.7 Documented event-day behaviour on the last trading day before inclusion/exclusion (my computation from PSE Daily Quotation Reports)**
- **[I]** Method: for each stock, value and volume from the DQR on the last trading day before the effective date, compared with that stock's median daily value over the prior 20 trading days; returns are close-to-close; "+5d" is the return from that day's close to the close five trading days later. Reports are public PDFs (Section 1.4); the event-day PDFs are archived as `pse-dqr-<date>`.

| Last trading day | Stock (action) | Value (PHP) | x own 20-day median value | Day return | Close vs day's range | Net foreign (PHP) | +5d |
|---|---|---|---|---|---|---|---|
| 2025-01-31 | CBC (in)[^pse-dqr-2025-01-31:1] | 5.60bn (62.9m sh) | 89x | **+38.9%** (66.95 to 93.00) | at day high | +0.66bn | -6.1% |
| 2025-01-31 | AREIT (in)[^pse-dqr-2025-01-31:4] | 2.72bn | 35x | +7.7% | at high | +0.99bn | -5.8% |
| 2025-01-31 | NIKL (out)[^pse-dqr-2025-01-31:7] | 0.48bn (215m sh) | 122x | **-17.8%** | at low | +0.01bn | +19.8% |
| 2025-01-31 | WLCON (out)[^pse-dqr-2025-01-31:7] | 0.82bn | 29x | -1.6% | at low | +0.11bn | +7.6% |
| 2025-08-15 | PLUS (in)[^pse-dqr-2025-08-15:6] | 1.98bn | 2.0x | +8.1% | n/a | -0.21bn | -3.3% |
| 2025-08-15 | BLOOM (out)[^pse-dqr-2025-08-15:6] | 0.49bn | 6.4x | +9.1% | n/a | -0.03bn | -7.2% |
| 2026-01-30 | RCR (in)[^pse-dqr-2026-01-30:5] | 2.50bn (341m sh) | 17x | -4.9% | at low | -1.16bn | +3.7% |
| 2026-01-30 | AGI (out)[^pse-dqr-2026-01-30:3] | 0.40bn | 21x | +2.1% | at high | +0.02bn | +14.2% |
| 2026-07-31 | MYNLD (in, early)[^pse-dqr-2026-07-31:2] | 1.43bn | 20x | -2.6% | at low | -0.49bn | -1.7% |
| 2026-07-31 | CNVRG (out)[^pse-dqr-2026-07-31:5] | 0.83bn | 15x | +6.1% | upper part | -0.01bn | +1.3% |

Market totals for each day are on pp.12-13 of the same DQRs; +5d returns use the adjacent DQRs in the public series.[^pse-daily-quotation-report-series]
- **[I]** Market-wide value traded on those days, relative to the prior-20-day median ex-block: 2025-01-31 5.0x (but the PSEi fell 4.0% that day, so it is not a clean index effect); 2025-08-15 1.6x; 2026-01-30 2.1x; 2026-07-31 1.8x; 2023-10-03 (off-cycle) 1.5x; days before reviews with no PSEi change 1.15x and 1.2x (2024-08-09 and 2024-02-02). Base rate since Jan 2024: median 1.0x, 90th percentile 1.4x (ex-block).
- **[I]** Reading: PSEi events move individual stocks a lot (a 39% one-day move in CBC, whose normal daily value is small next to index-fund demand; an 18% fall in a deleted small name on 215m shares) but move total market turnover little, consistent with the small amount of money that tracks the PSEi compared with MSCI-benchmarked money (Section 5). Additions: 3 of 5 rose on the day (CBC, AREIT, PLUS) and 4 of 5 were lower five days later (all but RCR). Deletions: the two largest falls on the day were NIKL and WLCON, and 4 of 5 were higher five days later (all but BLOOM). So the pattern is run-up into the last close and partial reversal, not a permanent re-rating, but the sample is ten stocks.

**4.8 Related PSE plans**
- **[P]** The PSE is developing a derivatives market "starting with Index Futures which will be based on the PSEi" (early exposure draft released; request for information to technology vendors targeted; no launch date).[^pse-asm-2026-president-report:24] **[I]** I found no PSEi derivative listed on the PSE; a Jan 2015 PSE deck lists "SGX-PSE MSCI PH Index Futures" as a new product, which trades in Singapore (current status not verified).[^pse-tokyo-roadshow-2015-01:7]
- **[P]** The PSE publishes the list of index members and index data on a subscription basis through its Market Data Department.[^pse-cn-2026-0035:1]

### Inferences
- **[I]** For the Feb 2027 review (Jan-Dec 2026 data under the new rules), the decisive variables are free-float market capitalisation at each month-end, median daily value, the number of days each stock traded, and rank by full market cap; all can be approximated from the public DQR series and the public ownership reports.
- **[I]** If the February pattern holds, the effective date will be Monday 1 Feb 2027 and the last PSE trading day before it Friday 29 Jan 2027, with the announcement about 3 to 5 trading days earlier (late January 2027). The PSE has not announced the 2027 timetable.
- **[I]** The 98% screen, the MTAR floor and the four-period persistence rule all reduce turnover and single-name squeezes of the CBC type; they also raise the barrier for low-float names, which matters for the DivY and MidCap indices as well as the PSEi.

### Gaps
- The June 2021 policy text and the 2021-22 revisions (CN-2021-0046, CN-2018-0013, CN-2018-0014 are archived but image-only here); the exact Feb 2023 and Jan 2026 circulars were not retrieved (press releases or secondary reports used).
- Current PSEi weights, float factors and the 2026 Public Ownership Report data (subscription).
- Assets tracking PSE indices (FMETF, UITFs, mutual funds, MidCap/DivY products) and the timing conventions their managers use.
- Whether PSE publishes a 2027 review calendar.

### Execution implications
1. **Calendar:** assume announcement 3 to 5 trading days before and implementation at the open of a Monday; for PSEi trackers the volume sits in the last close before it. Check the PSE holiday list for each review.
2. **Single-name risk:** additions whose normal turnover is small next to index-fund demand can gap violently into the last close (CBC +38.9%, AREIT +7.7%) and give some back within a week; deletions of small names can fall 15% to 20% on huge volume and rebound. Position size to the stock's own 20-day median value, not to the index.
3. **February 2027:** build an MTAR/MADV/98% screener now; names near the entry thresholds (MTAR 15%, existing members 10%) will drive the trade; the 15% float exception benefits only stocks of PHP 250bn or more.
4. **Weights are uncapped:** a few names (ICTSI at 14%) dominate index risk; hedge with PSEi-correlated baskets accordingly.
5. **Do not extrapolate:** index-event turnover across the whole market is modest (about 1.5x to 2x), so liquidity into the PSEi close is thin outside the changing names.


---

## 5. External indices (MSCI, FTSE Russell, S&P) and rebalancing-day effects on the PSE

### Takeaway
MSCI's Philippines Standard index is now tiny: 9 constituents on 30 Sep 2026 (USD 30.5bn float-adjusted, about 0.25% of MSCI Emerging Markets by my computation), down from 11 earlier in 2026 after Ayala Land's deletion (effective as of the 31 Aug 2026 close, a PSE holiday, so the trade fell on Fri 28 Aug). FTSE Russell classes the Philippines as Secondary Emerging and does not list it on its watch list (Mar 2026); its 2026 annual announcement was due on 6 Oct 2026 and was not yet posted when I looked. On the 12 MSCI implementation days I measured (May 2023 to Aug 2026) the PSE traded a median 3.0x its trailing 20-day median daily value (2.6x excluding block trades), against a 1.0x median and 5.9% frequency of days at 2x or more; deleted names typically closed at the day's low and then rebounded within five days. FTSE days run at about 2.1x and PSEi-recomposition days at about 1.6x (ex-block).

### Cited Findings

**5.1 MSCI: composition, size, weight**
- **[P]** MSCI Philippines Index (Standard, large and mid cap), 30 Sep 2026: **9 constituents**, "covers about 85% of the Philippines equity universe"; float-adjusted market capitalisation USD 30,500.43m (largest 13,641.85m; smallest 1,199.26m; mean 3,388.94m; median 1,856.94m). Weights: ICTSI 44.73%, BDO 13.41%, BPI 8.38%, SM Prime 7.72%, Ayala Corp 6.09%, Metrobank 5.74%, SM Investments 5.72%, PLDT 4.27%, Meralco B 3.93%; sectors Industrials 56.54%, Financials 27.53%, Real Estate 7.72%, Communication Services 4.27%, Utilities 3.93%; last-12-month one-way turnover 10.77%; index launched 29 Apr 1988.[^msci-philippines-index-factsheet-2026-09:1-2]
- **[P]** MSCI Philippines IMI (large, mid and small): 34 constituents, USD 43,676.74m; Ayala Land appears in its top ten (2.98%).[^msci-philippines-imi-factsheet-2026-09:1-2] MSCI Emerging Markets Index: 1,165 constituents, USD 12,281,841.19m (all 30 Sep 2026).[^msci-em-index-factsheet-2026-09:2]
- **[I]** Implied weights: Standard = 30,500.43 / 12,281,841.19 = **0.248% of MSCI EM**; the 25 small-cap names add about USD 13.2bn (IMI minus Standard). The EM factsheet does not list the Philippines separately (it sits in "Other 15.12%").[^msci-em-index-factsheet-2026-09:2]
- **[S]** Abacus Securities (reported 25 Aug 2026): the Philippines' MSCI weight is at a "decade, if not all-time, low"; Standard count 9, "down from 11 earlier this year", against about 21 for Malaysia, 18 Thailand, 16 Singapore; about 0.3% of MSCI Asia ex-Japan, versus close to 3% a decade ago.[^bilyonaryo-2026-08-25-msci-presence-abacus]
- **[P]** MSCI's May 2026 review: announced 12 May 2026; "implemented for the market cap indexes as of the close of May 29, 2026"; effective date 1 Jun 2026; the review used MSCI's new enhanced free-float rounding methodology for the first time, "the primary driver of the higher number of free float updates and elevated turnover".[^msci-index-review-factsheet-2026-05:2]
- **[S]** Dated MSCI Philippines changes (news-sourced; MSCI's own country lists returned HTTP 403 to scripted access): May 2023: Monde Nissin removed from MSCI Philippines (PSE value traded PHP 24.2bn on 31 May 2023, "6x-7x" the usual, foreign net selling PHP 4.15bn);[^metrobank-what-is-msci-rebalancing] Feb 2025 (effective 28 Feb): JG Summit and URC moved from Standard to Small Cap, Monde Nissin added to Small Cap, with AP Securities estimating flows of about -USD 30m (URC), -USD 23m (JGS), +USD 9.5m (Monde);[^philstar-2025-02-15-msci-jgs-urc] Feb 2026 (after the 27 Feb close): Standard unchanged, Apex Mining and Maynilad added to Small Cap (headline and summary seen only in search results; the Inquirer page returned HTTP 403),[^inquirer-2026-02-msci-standard-unchanged] after First Metro had said Jollibee was "very likely to stay" in Standard and Apex and Maynilad were likely Small Cap entrants;[^insiderph-2026-02-first-metro-msci] Aug 2026: Ayala Land removed from Standard to Small Cap "after Aug. 31, 2026", the stock falling 5.7% to PHP 14.98 on the reaction day.[^insiderph-2026-08-ali-msci]
- **[P]** The PSE was closed on Fri 21 Aug and **Mon 31 Aug 2026** (National Heroes Day).[^pse-cn-2026-0034b-non-trading-days-aug-2026:1] **[I]** MSCI's effective date therefore fell on a PSE holiday and index funds had to trade by the Fri 28 Aug close, which is where the volume appears (Section 5.4).
- **[I]** May 2026: the Standard count fell from 11 to 10 before the Aug 2026 deletion; the deleted name is not shown in any MSCI document I could open, but Jollibee is absent from the 30 Sep 2026 Standard list while First Metro had thought it would stay in Feb 2026, and it traded PHP 6.1bn (28x its median) and fell 6.1% to its day low on 29 May 2026. I treat "JFC deleted in May 2026" as an inference. Meralco's PHP 4.4bn (32x) on the same day coincides with MSCI's free-float rounding change and is more likely a weight change than a deletion (Meralco B remains in the index).
- **Reclassification risk:** I retrieved no MSCI market-classification review document. The only commentary is Abacus's remark that MSCI could move Indonesia toward frontier status and South Korea toward developed, which would not by itself change the Philippines' status. No source I read suggests an MSCI reclassification of the Philippines.[^bilyonaryo-2026-08-25-msci-presence-abacus]

**5.2 FTSE Russell**
- **[P]** The Philippines is **Secondary Emerging** in the FTSE Global Equity Index Series (ground rules v14.4, September 2026, Appendix E) and was added to the series on 1 Jul 1996 (with Indonesia).[^ftse-geis-ground-rules-2026-09:43,45] The 7 Apr 2026 interim announcement lists the Philippines under Secondary Emerging; its watch list contained only **Egypt** (possible Secondary Emerging to Frontier on stock count); Nigeria was moved to Frontier effective 21 Sep 2026; Vietnam stays scheduled to move from Frontier to Secondary Emerging effective the open of Mon **21 Sep 2026**, in multiple tranches "beginning in September 2026 and concluding in 2027"; Greece moves to Developed on 21 Sep 2026.[^ftse-country-classification-interim-2026-03:2-6][^ftse-country-classification-annual-2025-09:2-3] The Sep 2025 annual announcement (published 7 Oct 2025) did not place the Philippines on the watch list.[^ftse-country-classification-annual-2025-09:2]
- **[P]** Process: annual review with results each September (published in early October), a watch list published in March and September, and "at least six months' notice before changing the classification of any country".[^ftse-geis-ground-rules-2026-09:9] The next announcement is "Tuesday 06 October 2026"; on 6 Oct 2026 the FTSE page showed the 2026 announcement as "Document to follow".[^ftse-country-classification-interim-2026-03:5][^ftse-equity-country-classification-page] **So no 2026 classification outcome is known to me.**
- **[P]** FTSE "Quality of Markets" ratings for the Philippines (as at March 2026; my reading of the Philippines column by position, verify visually): Transparency (market depth information, visibility and timely trade reporting) Pass; Efficient trading mechanism Pass; Brokerage Pass; Off-exchange transactions Pass; CCP and CSD Pass; settlement T+2; Restricted on minority-shareholder treatment, foreign-ownership restrictions, stock lending, short sales, free delivery and custody account structure; Not Met on developed FX market, transaction costs and developed derivatives market.[^ftse-quality-of-markets-asia-pacific-2026-03:1] The watch-list criteria sheet (March 2026) names no Philippine criterion.[^ftse-watch-list-2026-03:1]
- **[P]** Index mechanics: semi-annual reviews in March and September for Asia Pacific ex China ex Japan (data as of the last business day of December and June); constituent changes "implemented after the close of business on the third Friday (i.e. effective the following Monday)" of March and September; quarterly reviews in June and December; securities with free float of 5% or below are excluded (except very large ones); weights adjusted for foreign ownership limits and a minimum foreign-headroom test; a semi-annual median-volume liquidity screen; the PSE main board and ordinary shares are eligible; for a market closed on a day, the last close is used.[^ftse-geis-ground-rules-2026-09:13,18,20,32,36,41]
- **[S]** FTSE's September 2026 review (announced 21 Aug): Emperador (EMI) re-enters the FTSE Global Equity Index Series as a Small Cap, the only new Philippine addition in that review.[^insiderph-2026-08-emperador-ftse]

**5.3 S&P and others**
- Not researched beyond a tertiary table that lists S&P Dow Jones as treating the Philippines as emerging. No S&P Philippine methodology, consultation or constituent document was retrieved.

**5.4 Documented impact on PSE volume and prices (my computation from archived PSE Daily Quotation Reports)**
- **[I]** Method: for each event date (PSE session on which the index change is traded), total value = DQR grand total (main board, odd lot, block and VWAP); baseline = median of the previous 20 trading days; "ex-block" removes the DQR block-sale value from both. Sample: 715 DQRs covering 17 Apr-5 Jun 2023, 2-10 Oct 2023 and 2 Jan 2024-5 Oct 2026 (so the MSCI events of Feb, Aug and Nov 2023 and the FTSE events of Jun, Sep and Dec 2023 are not measured). Base rate over 674 days from Jan 2024: median 1.01x; 90th percentile 1.58x; 95th 2.14x; 99th 4.03x; 5.9% of days at 2x or more, 2.1% at 3x or more (ex-block: 90th 1.40x, 95th 1.73x). The median absolute daily net foreign flow over the last year is PHP 0.44bn.

MSCI implementation days (PSE session; date set by MSCI as "as of the close"; the 2023-05-31, 2025-02-28, 2026-02-27, 2026-05-29 and 2026-08-28 dates are confirmed by the sources above, the others follow MSCI's usual last-business-day pattern and the volume peak in the DQRs):

| PSE session | Total value (PHP bn) | x 20-day median | x ex-block | Net foreign (PHP bn) | PSEi day | Largest single-name effect |
|---|---|---|---|---|---|---|
| 2023-05-31[^pse-dqr-2023-05-31:12] | 24.54 | 5.3 | 6.2 | -4.15 | -0.5% | MONDE PHP 4.41bn (53x own median; 18% of the day's value) |
| 2024-02-29[^pse-dqr-2024-02-29:13] | 11.96 | 2.4 | 2.6 | +0.44 | +1.0% | broad-based |
| 2024-05-31[^pse-dqr-2024-05-31:13] | 22.72 | 3.9 | 4.6 | -5.23 | +1.0% | AEV PHP 5.48bn (106x; 24% of the day) |
| 2024-08-30[^pse-dqr-2024-08-30:13] | 13.31 | 2.4 | 2.6 | -0.31 | +0.1% | broad-based |
| 2024-11-25[^pse-dqr-2024-11-25:13] | 9.98 | 1.8 | 2.0 | -0.31 | +1.0% | broad-based |
| 2025-02-28[^pse-dqr-2025-02-28:13] | 20.63 | 3.6 | 3.9 | -3.43 | -2.1% | URC PHP 4.35bn (22x) and JGS PHP 3.15bn (33x): together 36% of the day |
| 2025-05-30[^pse-dqr-2025-05-30:13] | 40.03 | 6.2 | 2.7 | -15.31 | -1.1% | PHP 24.5bn of block trades (Robinsons Retail PHP 15.8bn, BDO PHP 8.4bn), unrelated to the index; ex-block 2.7x |
| 2025-08-26[^pse-dqr-2025-08-26:13] | 14.32 | 2.1 | 2.1 | -2.04 | -2.2% | broad-based; BDO -8.0% on PHP 2.18bn (5x), net foreign -PHP 1.08bn |
| 2025-11-24[^pse-dqr-2025-11-24:13] | 13.69 | 2.1 | 2.3 | -0.82 | +0.4% | BPI PHP 2.75bn (8x); broad-based |
| 2026-02-27[^pse-dqr-2026-02-27:13] | 19.62 | 2.8 | 2.2 | +0.92 | -0.2% | PHP 6.4bn blocks (AREIT); MYNLD PHP 1.87bn (13x) |
| 2026-05-29[^pse-dqr-2026-05-29:13] | 26.47 | 4.4 | 4.9 | -6.65 | -1.6% | JFC PHP 6.10bn (28x; 23% of day), MER PHP 4.39bn (32x) |
| 2026-08-28[^pse-dqr-2026-08-28:12] | 18.81 | 3.2 | 3.5 | -3.51 | -0.8% | ALI PHP 7.23bn (39x; 38% of the day, 466m shares) |

- **[I]** Summary: median 3.04x (mean 3.36x) total; median 2.63x ex-block; 11 of 12 days at or above 2.0x against a 5.9% base rate; net foreign selling on 10 of 12 days, six of them at PHP 3.4bn or more (8x to 35x the typical absolute daily flow of PHP 0.44bn; the PHP 15.3bn of 30 May 2025 is inflated by the unrelated block trades). May reviews are the heaviest in this sample (5.3x, 3.9x, 6.2x total / 2.7x ex-block, 4.4x); February and August reviews run 2x to 4x; November 2024 and 2025 about 2x (MSCI calls its May and November reviews 'semi-annual' and February and August 'quarterly'; that naming is my background knowledge, not checked in the documents retrieved).

FTSE third-Friday days (semi-annual March and September; quarterly June and December; the PSE session is the third Friday itself):

| PSE session | Total value (PHP bn) | x 20-day median | x ex-block | Net foreign (PHP bn) |
|---|---|---|---|---|
| 2024-03-15[^pse-dqr-2024-03-15:13] | 20.08 | 4.1 | 4.1 | -4.30 |
| 2024-06-21[^pse-dqr-2024-06-21:13] | 8.26 | 1.7 | 1.8 | -1.34 |
| 2024-09-20[^pse-dqr-2024-09-20:13] | 16.98 | 2.8 | 2.6 | +1.28 |
| 2024-12-20[^pse-dqr-2024-12-20:13] | 6.95 | 1.2 | 1.5 | -0.78 |
| 2025-03-21[^pse-dqr-2025-03-21:13] | 11.77 | 1.9 | 2.0 | +1.04 |
| 2025-06-20[^pse-dqr-2025-06-20:13] | 12.27 | 2.0 | 2.1 | -0.84 |
| 2025-09-19[^pse-dqr-2025-09-19:13] | 14.30 | 2.3 | 2.4 | +0.22 |
| 2025-12-19[^pse-dqr-2025-12-19:13] | 18.72 | 2.7 | 1.9 | -0.10 |
| 2026-06-19[^pse-dqr-2026-06-19:13] | 11.18 | 1.6 | 1.8 | -0.45 |
| 2026-09-18[^pse-dqr-2026-09-18:12] | 16.23 | 2.8 | 2.8 | -1.46 |

- **[I]** FTSE days: ex-block median 2.07x (mean 2.30x); March 2024 (4.1x) is the largest; no DQR exists for 20 Mar 2026 in the public series (a non-trading day or a missing file), so that event is not measured. Third Fridays are also quarterly-expiry dates in many other markets and rebalance dates for other index providers (my background knowledge), so attribution to FTSE alone is not clean.

Stock-level evidence on MSCI deletions and additions (raw, not market-adjusted; "announcement" = close on the MSCI announcement date, which reaches Manila the next morning; announcement dates other than 12 May 2026 are as reported or inferred):

| Stock (MSCI action) | Announcement close | Implementation-day close | Announcement to implementation | Implementation day | Close in day's range | Net foreign on the day | +5 trading days |
|---|---|---|---|---|---|---|---|
| MONDE 2023-05-31 (removed; [S])[^pse-dqr-2023-05-31:2] | 9.32 (11 May) | 8.10 | -13.1% | -1.2% | 0.18 | -PHP 1.12bn | +13.5% |
| AEV 2024-05-31 (inferred)[^pse-dqr-2024-05-31:3] | 38.35 (14 May) | 35.05 | -8.6% | -5.3% | at low | -PHP 3.03bn | +9.8% |
| JGS 2025-02-28 (to Small Cap; [S])[^pse-dqr-2025-02-28:4] | 15.02 (11 Feb) | 15.86 | +5.6% | -7.1% | at low | -PHP 1.41bn | +14.2% |
| URC 2025-02-28 (to Small Cap; [S])[^pse-dqr-2025-02-28:2] | 61.90 | 66.20 | +6.9% | -2.9% | 0.37 | -PHP 1.50bn | +8.5% |
| MONDE 2025-02-28 (added to Small Cap; [S])[^pse-dqr-2025-02-28:2] | 7.55 | 7.55 | 0.0% | -5.5% | at low | -PHP 0.07bn | +2.9% |
| JFC 2026-05-29 (inferred)[^pse-dqr-2026-05-29:2] | 144.00 (12 May, the MSCI announcement date[^msci-index-review-factsheet-2026-05:2]) | 126.90 | -11.9% | -6.1% | at low | -PHP 2.79bn | +7.4% |
| MER 2026-05-29 (weight change, inferred)[^pse-dqr-2026-05-29:2] | 650.00 | 570.50 | -12.2% | -4.8% | at low | -PHP 1.49bn | -2.5% |
| MYNLD 2026-02-27 (added to Small Cap; [S])[^pse-dqr-2026-02-27:2] | 19.62 (10 Feb) | 22.00 | +12.1% | +0.9% | 0.55 | +PHP 0.38bn | -5.9% |
| APX 2026-02-27 (added to Small Cap; [S])[^pse-dqr-2026-02-27:7] | 14.98 | 17.50 | +16.8% | 0.0% | 0.40 | +PHP 0.17bn | -8.9% |
| ALI 2026-08-28 (to Small Cap; [S])[^pse-dqr-2026-08-28:4] | 15.88 (12 Aug) | 15.54 | -2.1% | +0.3% | 0.76 | -PHP 1.56bn | -2.8% (-3.3% next day) |

- **[I]** Reading: (1) heavy deletions are absorbed into the last close with day moves of -3% to -7% for AEV, JGS, URC, JFC and MER (MONDE -1.2% after a 13% slide from the announcement), a close in the bottom 40% of the day's range for all six (at the low for four), and a rebound of 7% to 14% within five trading days for five of the six (MONDE, AEV, JGS, URC, JFC; MER did not rebound); (2) price pressure begins at the announcement: Ayala Land fell 5.7% on the reaction day (13 Aug; the DQR close of 14.98 confirms it),[^pse-daily-quotation-report-series] then held up into the trade date (+0.3%) and kept drifting lower afterwards, so for a stock with weak fundamentals the rebound did not occur; (3) additions to the Small Cap index drew modest volume, ran up beforehand (MYNLD +12%, APX +17% from announcement) and fell after (-6% to -9% at five days); (4) one deleted stock can be 18% to 38% of the whole market's value that day. The closing-auction share cannot be isolated, because the DQR reports only daily totals and the close; the pattern of closes at the day's low is consistent with late-session and closing-auction selling but is not proof of it.
- **[I]** Calendar check: with MSCI's date on a PSE holiday the flow arrived at the Fri 28 Aug 2026 close (ALI PHP 7.2bn); the first session after the holiday (Tue 1 Sep) still traded 1.8x the baseline (PHP 10.5bn) with ALI down 3.3%.

### Inferences
- **[I]** MSCI-linked money dominates passive flow in the PSE (the PSEi-tracking base is small, Section 4): the Standard index has 9 names, so a single deletion matters: Ayala Land (about USD 1.3bn float-adjusted market capitalisation, roughly 4% of the Standard index before it left) traded PHP 7.2bn on its deletion day, 38% of the whole market's value.
- **[I]** Because the Standard index is so concentrated (ICTSI 44.7%), future migrations of mid-caps to Small Cap (or a Standard-index weight change for ICTSI) are the main source of flow risk; the 9-name count is now a fact to watch, although I found no documented MSCI rule that this triggers a reclassification.
- **[I]** FTSE's Vietnam reclassification (tranches from 21 Sep 2026 through 2027) adds a Secondary Emerging market that competes for the same allocation; any effect on Philippine weights is not quantified in the documents I read.

### Gaps
- MSCI primary lists for the Philippines (Feb 2025, Feb 2026, May 2026, Aug 2026) and MSCI's June 2026 market classification review could not be retrieved; MSCI's November 2026 dates are not known to me. Check whether Mon 30 Nov 2026 is a PSE holiday before assuming an MSCI trade date.
- FTSE's 2026 annual announcement (6 Oct 2026) and the Philippines' status after it.
- S&P Dow Jones documents; passive AUM benchmarked to MSCI or FTSE Philippines indices; the amount tracking the PSEi.
- Closing-auction volume and price discovery on event days (needs ITCH [I]/[C] data or a vendor's auction-volume field).
- Attribution: several event days coincide with other flows (blocks, earnings, quarterly expiries); the numbers above are descriptive.

### Execution implications
1. Treat MSCI implementation days as 2x to 6x volume days with price pressure concentrated into the last close and net foreign selling when names are deleted; size and schedule other orders away from the close unless you are supplying liquidity to the deletion.
2. For deletions the pattern is: pressure from the announcement date (about 2.5 weeks before), a final push into the last close, then a rebound within about a week for fundamentally sound names; build the trade on the rebound only where the stock is not in a downtrend (ALI did not rebound).
3. When MSCI's effective date is a PSE holiday, the PSE trade date is the previous session (28 Aug 2026); check both calendars for every review.
4. FTSE days are smaller (about 2x) but frequent (March, June, September, December; Sep 2026 had the Vietnam and Greece changes at the open of 21 Sep).
5. The new engine's Run-Off/Trading-at-Last rule (orders can be entered and executed only at the closing price) and the negotiated-trade facility (within +/-5% of the full-day VWAP, 15 minutes after the run-off) change how large index orders can be crossed; the first MSCI implementation after the 23 Nov 2026 cutover (November 2026 review) will be the first live test.


---

## Source catalog

Edition values follow the brief: `in-force` = governing on 6 Oct 2026; `superseded` = replaced (date given in the note); `historical` = a dated record or past event; `n/a` = proposal, announced-not-yet-effective, or a data page. `amended_through` is taken from the document's own cover, history table or body date; "undated" where none is printed (page captions such as "as at March 2026" are recorded in the note). URLs marked "(not verified)" are where the archiving researcher did not record the address and my probe returned 404.

```yaml
# ---- PSE market data, feeds, specifications ----
- slug: pse-itch-equities-feed-spec-v2-3
  title: "PSE Equities Feed Specification v2.3 (ITCH Total View / Basic / News / Index, for X-stream)"
  publisher: "The Philippine Stock Exchange (content copyright OMX Technology AB 2014)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2024/03/PSE_Equities_Feed_Specification_v2.3.pdf"
  local_path: pdfs/pse-itch-equities-feed-spec-v2-3.pdf
  edition: in-force
  amended_through: "2018-10-05"
  note: "Feed spec for PSEtrade XTS; byte-identical copy also served under /2021/02/. Replaced for the new engine by ITCH v1.x/MDF (not public) from the scheduled 23 Nov 2026 cutover."
- slug: pse-fix-itch-session-week01-2014-10-03
  title: "Session on FIX and ITCH, week 1 (Q&A incl. broker anonymity and Level 1 depth)"
  publisher: "The Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2021/01/Session-on-FIX-and-ITCH-week-1.pdf"
  local_path: pdfs/pse-fix-itch-session-week01-2014-10-03.pdf
  edition: historical
  amended_through: "2014-10-03"
  note: "Project-session deck dated on its cover; source of the 'broker anonymity but not on Go-Live' answer and the top-of-book-only Level 1 answer."
- slug: pse-fix-itch-session-week06-2014-11-07
  title: "Session on FIX and ITCH, week 6 (ITCH Basic vs Total View mapping)"
  publisher: "The Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2021/01/Session-on-FIX-and-ITCH-week6.pdf"
  local_path: pdfs/pse-fix-itch-session-week06-2014-11-07.pdf
  edition: historical
  amended_through: "2014-11-07"
  note: "Cover date; p.20 states which trades go to Trade [p] in Basic vs Total View."
- slug: pse-fix-itch-session-week14-2015-02-13
  title: "Session on FIX and ITCH, week 14 (trader ID convention)"
  publisher: "The Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2021/01/Session-on-FIX-and-ITCH-week14.pdf"
  local_path: pdfs/pse-fix-itch-session-week14-2015-02-13.pdf
  edition: historical
  amended_through: "2015-02-13"
  note: "Cover date; p.16 gives the 8-character trader ID convention."
- slug: pse-fix-specification-v2-5
  title: "PSE FIX Specification v2.5 (X-stream)"
  publisher: "The Philippine Stock Exchange (OMX Technology AB)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2021/01/PSE_FIX_Specification_v2_5-10-August-2015.pdf"
  local_path: pdfs/pse-fix-specification-v2-5.pdf
  edition: in-force
  amended_through: "2015-08-10"
  note: "Archived by another researcher; used here for ContraFirm (party role 17) on trade ExecutionReports and the block-trade capture workflow. Date from the PSE listing title; replaced for the new engine by FIX v1.1 specs (8 Jun 2026, not public)."
- slug: pse-consolidated-tp-file-spec-2015
  title: "Consolidated Trade File (CTF) File Specifications v2.3"
  publisher: "The Philippine Stock Exchange, Market Operations Division"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2021/01/Consolidated-TP-File-Updated-as-of-March-31-2015.pdf"
  local_path: pdfs/pse-consolidated-tp-file-spec-2015.pdf
  edition: in-force
  amended_through: "2015-03-30"
  note: "Per-broker EOD trade file incl. Contra Broker; the Aug 2026 FAQ says CTF specification does not change with the new engine."
- slug: pse-non-display-usage-policy-2017
  title: "Non-Display Usage Policy Guidelines v1.0"
  publisher: "The Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2021/02/PSE_Non-Display_Usage_Policy_Guidelines_v1.0_June_1_2017.pdf"
  local_path: pdfs/pse-non-display-usage-policy-2017.pdf
  edition: in-force
  amended_through: "2017-06-01"
  note: "Announcement date on the document; fees effective 1 Oct 2017; no later public revision found."
- slug: pse-data-feed-application-form
  title: "Data Feed Application Form"
  publisher: "The Philippine Stock Exchange, Market Data Department"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2021/02/PSE_Data_Feed_Application_Form.pdf"
  local_path: pdfs/pse-data-feed-application-form.pdf
  edition: in-force
  amended_through: "undated"
  note: "Lists ITCH Basic (Level 1), Total View (Level 2), Index, News, delayed and EOD subscription types; no fees."
- slug: pse-market-data-subscription-form
  title: "Market Data Department Subscription Form (EOD and historical data terms)"
  publisher: "The Philippine Stock Exchange, Market Data Department"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2021/03/Market-Data-Subscription-Form.pdf"
  local_path: pdfs/pse-market-data-subscription-form.pdf
  edition: in-force
  amended_through: "undated"
  note: "Footer reads 'MDD Subscription Form / February 2021'."
- slug: pse-index-subscription-bundle-form
  title: "Market Data Application Form: Index Subscription Bundle"
  publisher: "The Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2021/02/PSE_Index-Subscription-Bundle_Application_Form.pdf"
  local_path: pdfs/pse-index-subscription-bundle-form.pdf
  edition: in-force
  amended_through: "undated"
  note: "Footer 'Ver 1.0 / Jan 2019'; USD 500 one-time plus USD 500 annual."
- slug: pse-caf-spec-v6-0
  title: "Corporate Announcements Feed Specifications v6.0"
  publisher: "The Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2021/02/CAF-v6.0.pdf"
  local_path: pdfs/pse-caf-spec-v6-0.pdf
  edition: in-force
  amended_through: "2019-09-09"
  note: "Revision-history date of v6.0."
- slug: pse-eod-market-data-spec-v1-3
  title: "End-of-Day Market Data Specifications v1.3 (PHIP file)"
  publisher: "The Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2021/02/EOD-Market-Data-v1.3.pdf"
  local_path: pdfs/pse-eod-market-data-spec-v1-3.pdf
  edition: in-force
  amended_through: "undated"
  note: "Schedule A to the EOD data licence."
- slug: pse-mcap-eod-spec-v1-0
  title: "Market Capitalization (MCAP) Report End-of-Day Market Data Product Specifications v1.0"
  publisher: "The Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2021/02/PSE_MCAP_Report_End-of-Day_Market_Data_Product_Technical_Specifications_v1.0.pdf"
  local_path: pdfs/pse-mcap-eod-spec-v1-0.pdf
  edition: in-force
  amended_through: "2016-02-26"
  note: "Document date line; 'as of 29 February 2016'."
- slug: pse-listed-company-stock-feed-brochure
  title: "Listed Company Stock Feed brochure v1.0"
  publisher: "The Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2021/02/PSE_Listed_Company_Stock_Feed_Brochure_v1.0.pdf"
  local_path: pdfs/pse-listed-company-stock-feed-brochure.pdf
  edition: in-force
  amended_through: "undated"
  note: "15-minute-delayed feed and fee table (PHP)."
- slug: pse-securities-static-data-file
  title: "PSE Securities Static Data Specifications v1.0"
  publisher: "The Philippine Stock Exchange, CMDD-Market Data Department"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2026/07/PSE_Securities-Static-Data_File_v1.0-1.pdf"
  local_path: pdfs/pse-securities-static-data-file.pdf
  edition: in-force
  amended_through: "2026-06-22"
  note: "New-engine static data; pipe-delimited."
- slug: pse-index-member-static-data-file
  title: "PSE Index Member Static Data Specifications v1.0"
  publisher: "The Philippine Stock Exchange, CMDD-Market Data Department"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2026/07/PSE_Index-Member-Static-Data_File_v1.0-1.pdf"
  local_path: pdfs/pse-index-member-static-data-file.pdf
  edition: in-force
  amended_through: "2026-06-22"
  note: "indexcode|seccode only."
- slug: pse-psetradex-installation-guidelines
  title: "PSETradex Installation Guidelines (incl. broker code / silo table)"
  publisher: "The Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2021/01/PSETradex-Installation-Guidelines8536.pdf"
  local_path: pdfs/pse-psetradex-installation-guidelines.pdf
  edition: historical
  amended_through: "undated"
  note: "Archived by another researcher; used only for the 3-digit broker codes."
- slug: pse-tokyo-roadshow-2015-01
  title: "PSE investor roadshow (Tokyo) presentation"
  publisher: "The Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/4/2021/02/17-C-22-January-2015-PSE-Tokyo-Roadshow.pdf"
  local_path: pdfs/pse-tokyo-roadshow-2015-01.pdf
  edition: historical
  amended_through: "undated"
  note: "Content covers 9M 2014 results and 2015 plans (market data fee share, X-stream adoption); the URL names 22 January 2015."

# ---- PSE new trading engine (Nasdaq Eqlipse) ----
- slug: pse-nte-user-group-2026-01-15
  title: "New Trading Engine, PSETradeX, Back-office Updates: Broker Forum (15 Jan 2026)"
  publisher: "The Philippine Stock Exchange, Market Operations Division"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2026/06/NTE-User-Group.pdf"
  local_path: pdfs/pse-nte-user-group-2026-01-15.pdf
  edition: historical
  amended_through: "2026-01-15"
  note: "Superseded in detail by the 9 Jul 2026 deck; archived by another researcher."
- slug: pse-nte-broker-forum-2026-07-09
  title: "New Trading Engine, PSETradeX, Back-office Updates: Broker Forum (9 Jul 2026)"
  publisher: "The Philippine Stock Exchange, Market Operations Division"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2026/07/PSE-New-Trading-Engine-TradeX-Back-office_Broker-Forum_07092026-1.pdf"
  local_path: pdfs/pse-nte-broker-forum-2026-07-09.pdf
  edition: in-force
  amended_through: "2026-07-09"
  note: "Project schedule incl. go-live 23 Nov 2026; no later primary re-confirmation found."
- slug: pse-nte-faq-2026-08
  title: "Frequently Asked Questions: New Trading Engine / market data / back-office"
  publisher: "The Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2026/08/Frequent-Asked-Questions.pdf"
  local_path: pdfs/pse-nte-faq-2026-08.pdf
  edition: in-force
  amended_through: "undated"
  note: "Refers to final specs released 23 Jul 2026; so published after that date."
- slug: pse-cn-2025-0046-board-lot-trading-at-last
  title: "CN-2025-0046: Request for Comments on Proposed Amendments to the PSE Board Lot and Rule on Trading during Run-Off / Trading-at-Last"
  publisher: "The Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2025-0046.pdf"
  local_path: pdfs/pse-cn-2025-0046-board-lot-trading-at-last.pdf
  edition: n/a
  amended_through: "2025-12-15"
  note: "Consultation memo (proposal), tied to the new engine; the rules take effect with the cutover. Archived by another researcher."

# ---- PSE disclosure rules and EDGE ----
- slug: pse-listing-disclosure-rules
  title: "Consolidated Listing and Disclosure Rules (published as of January 2025)"
  publisher: "The Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2025/01/Consolidated-Listing-and-Disclosure-Rules-Updated-011025.pdf"
  local_path: pdfs/pse-listing-disclosure-rules.pdf
  edition: in-force
  amended_through: "undated"
  note: "Cover 'Published as of January 2025'. Guidance Note 15 (3:30 pm EDGE cut-off) in this text is superseded by CN-2026-0024. Archived by another researcher."
- slug: pse-cn-2022-0010-edge-cutoff-330pm
  title: "CN-2022-0010: Cut-off for Posting Disclosures on PSE EDGE Portal"
  publisher: "The Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2022-0010.pdf"
  local_path: pdfs/pse-cn-2022-0010-edge-cutoff-330pm.pdf
  edition: superseded
  amended_through: "2022-02-24"
  note: "3:30 pm cut-off effective 1 Mar 2022; superseded by CN-2026-0024 effective 25 May 2026. Archived by another researcher."
- slug: pse-cn-2026-0024-edge-cutoff-4pm
  title: "CN-2026-0024: Cut-off for Posting Disclosures on EDGE Portal (4:00 pm)"
  publisher: "The Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://www.pse.com.ph/ (circular CN-2026-0024; direct PDF address not recorded and not verified)"
  local_path: pdfs/pse-cn-2026-0024-edge-cutoff-4pm.pdf
  edition: in-force
  amended_through: "2026-05-22"
  note: "Effective 25 May 2026. Archived by another researcher."
- slug: pse-cn-2026-0003-1-edge-unavailable
  title: "CN-2026-0003: Access to Disclosures via PSE Website and Filing of Emergency Disclosures"
  publisher: "The Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2026-0003.pdf (the live file currently shows the later 'EDGE systems now accessible' text; this archived copy is the earlier notice)"
  local_path: pdfs/pse-cn-2026-0003-1-edge-unavailable.pdf
  edition: historical
  amended_through: "2026-01-19"
  note: "EDGE outage notice. Archived by another researcher."
- slug: pse-cn-2026-0006-edge-accessible
  title: "CN-2026-0006: EDGE Systems Now Accessible"
  publisher: "The Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://www.pse.com.ph/ (circular CN-2026-0006; direct PDF address not recorded and not verified)"
  local_path: pdfs/pse-cn-2026-0006-edge-accessible.pdf
  edition: historical
  amended_through: "2026-01-19"
  note: "Archived by another researcher."
- slug: pse-cn-2026-0004-2-emergency-disclosures-trading-halt
  title: "CN-2026-0004: Emergency Disclosures and Trading Halt (MRC Allied, with Disclosure Notice)"
  publisher: "The Philippine Stock Exchange, Disclosure Department"
  type: pdf
  canonical_url: "https://www.pse.com.ph/ (circular CN-2026-0004; direct PDF address not recorded and not verified)"
  local_path: pdfs/pse-cn-2026-0004-2-emergency-disclosures-trading-halt.pdf
  edition: historical
  amended_through: "2026-01-19"
  note: "One-hour halt on MRC, 9:30-10:30 am. Archived by another researcher."
- slug: pse-cn-2026-0034b-non-trading-days-aug-2026
  title: "CN-2026-0034B: Non-Trading Days (August 2026)"
  publisher: "The Philippine Stock Exchange, Market Operations Division"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2026-0034B.pdf (not verified; probe returned 404)"
  local_path: pdfs/pse-cn-2026-0034b-non-trading-days-aug-2026.pdf
  edition: in-force
  amended_through: "2026-07-27"
  note: "No trading 21 Aug and 31 Aug 2026. Archived by another researcher."

# ---- PSE index policy, circulars, factsheets ----
- slug: pse-index-policy-2024
  title: "Policy on Index Management (January 2024 version)"
  publisher: "The Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2024/01/Policy-on-Index-Management-ver-2024.pdf"
  local_path: pdfs/pse-index-policy-2024.pdf
  edition: in-force
  amended_through: "2024-01-26"
  note: "Cover 'January 2024'; incorporates the 2.2.3(b) pension-fund amendment of CN-2024-0008 (26 Jan 2024). In force until the Feb 2027 rebalance, then replaced by the July 2026 revision."
- slug: pse-cn-2026-0033
  title: "CN-2026-0033: Revised Policy on Index Management (July 2026)"
  publisher: "The Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2026-0033.pdf"
  local_path: pdfs/pse-cn-2026-0033.pdf
  edition: n/a
  amended_through: "2026-07-21"
  note: "Announced, applies from the February 2027 index rebalancing; NOT in force today."
- slug: pse-cn-2026-0033b
  title: "CN-2026-0033B: Revised Policy on Index Management (re-issue)"
  publisher: "The Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2026/07/CN-2026-0033B.pdf"
  local_path: pdfs/pse-cn-2026-0033b.pdf
  edition: n/a
  amended_through: "2026-07-21"
  note: "Text identical to CN-2026-0033 apart from the circular number (my diff)."
- slug: pse-midcap-index-policy-2024
  title: "Policy on Index Management: PSE MidCap Index (January 2024)"
  publisher: "The Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2024/01/Policy-on-Index-Management_PSE-MidCap-Index_Jan-2024.pdf"
  local_path: pdfs/pse-midcap-index-policy-2024.pdf
  edition: in-force
  amended_through: "undated"
  note: "Cover 'January 2024'; MidCap rules (top 35% median daily trade, 95% cumulative market cap) valid until Feb 2027."
- slug: pse-divy-index-policy-2024
  title: "Policy on Index Management: PSE Dividend Yield Index (January 2024)"
  publisher: "The Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2024/01/Policy-on-Index-Management_PSE-DiY-Index_Jan2024.pdf"
  local_path: pdfs/pse-divy-index-policy-2024.pdf
  edition: in-force
  amended_through: "undated"
  note: "Cover 'January 2024'."
- slug: pse-index-policy-feb2018
  title: "Policy on Index Management (February 2018 version)"
  publisher: "The Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2021/01/Policy-on-Index-Management-Feb2018.pdf"
  local_path: pdfs/pse-index-policy-feb2018.pdf
  edition: superseded
  amended_through: "undated"
  note: "Cover 'February 2018'; 15% float; rank-25 / rank-35 rules; superseded by later versions (June 2021 version not retrieved)."
- slug: pse-cn-2023-0039
  title: "CN-2023-0039: Results of the Review of PSE Indices (Jul 2022-Jun 2023)"
  publisher: "The Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2023-0039.pdf"
  local_path: pdfs/pse-cn-2023-0039.pdf
  edition: historical
  amended_through: "2023-07-28"
  note: "Effective 7 Aug 2023."
- slug: pse-cn-2023-0044
  title: "CN-2023-0044: Changes to the PSE Indices (off-cycle)"
  publisher: "The Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2023-0044.pdf"
  local_path: pdfs/pse-cn-2023-0044.pdf
  edition: historical
  amended_through: "2023-09-20"
  note: "Effective start of day 26 Sep 2023."
- slug: pse-cn-2023-0047
  title: "CN-2023-0047: Removal of Union Bank of the Philippines from the PSE Indices"
  publisher: "The Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2023-0047.pdf"
  local_path: pdfs/pse-cn-2023-0047.pdf
  edition: historical
  amended_through: "2023-09-28"
  note: "Effective start of day 4 Oct 2023; free float below 20%."
- slug: pse-cn-2024-0008
  title: "CN-2024-0008: Results of the Review of PSE Indices and Index Policy Update (Jan-Dec 2023)"
  publisher: "The Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2024-0008.pdf"
  local_path: pdfs/pse-cn-2024-0008.pdf
  edition: historical
  amended_through: "2024-01-26"
  note: "Effective 5 Feb 2024; amends 2.2.3(b)."
- slug: pse-cn-2024-0042
  title: "CN-2024-0042: Results of the Review of PSE Indices (Jul 2023-Jun 2024)"
  publisher: "The Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2024-0042.pdf"
  local_path: pdfs/pse-cn-2024-0042.pdf
  edition: historical
  amended_through: "2024-08-05"
  note: "Effective 12 Aug 2024."
- slug: pse-cn-2025-0005
  title: "CN-2025-0005: Results of the Review of PSE Indices (Jan-Dec 2024)"
  publisher: "The Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2025-0005.pdf"
  local_path: pdfs/pse-cn-2025-0005.pdf
  edition: historical
  amended_through: "2025-01-24"
  note: "Effective 3 Feb 2025."
- slug: pse-cn-2025-0034
  title: "CN-2025-0034: Results of the Review of PSE Indices (Jul 2024-Jun 2025)"
  publisher: "The Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2025-0034.pdf"
  local_path: pdfs/pse-cn-2025-0034.pdf
  edition: historical
  amended_through: "2025-08-08"
  note: "Effective 18 Aug 2025."
- slug: pse-cn-2026-0035
  title: "CN-2026-0035: Results of the Review of PSE Indices (Jul 2025-Jun 2026)"
  publisher: "The Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2026-0035.pdf"
  local_path: pdfs/pse-cn-2026-0035.pdf
  edition: in-force
  amended_through: "2026-07-27"
  note: "Effective 3 Aug 2026; lists the 30 PSEi members now in force."
- slug: pse-psei-factsheet-2025-09
  title: "PSEi and PSEi TRI Factsheet (data as of end-September 2025)"
  publisher: "The Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2025/11/PSEi-PSEi-TRI-Factsheet_202509.pdf"
  local_path: pdfs/pse-psei-factsheet-2025-09.pdf
  edition: in-force
  amended_through: "undated"
  note: "Latest factsheet linked on the PSE indices page, but data are 30 Sep 2025 and stale."
- slug: pse-asm-2026-president-report
  title: "President's Report, 2026 Annual Stockholders' Meeting"
  publisher: "The Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://corporate.pse.com.ph/ (stockholders' meeting materials; direct PDF address not recorded)"
  local_path: pdfs/pse-asm-2026-president-report.pdf
  edition: in-force
  amended_through: "undated"
  note: "Archived by another researcher; p.24 gives the PSEi index-futures plan; content dated mid-2026."

# ---- PSE Daily Quotation Reports (event days; one dataset entry for the series) ----
- slug: pse-daily-quotation-report-series
  title: "PSE Daily Quotation Report (EOD market report), daily series"
  publisher: "The Philippine Stock Exchange"
  type: dataset
  canonical_url: "https://documents.pse.com.ph/market_report/<Month DD, YYYY>-EOD.pdf (e.g. https://documents.pse.com.ph/market_report/May%2031,%202023-EOD.pdf)"
  local_path: null
  edition: in-force
  amended_through: "2026-10-05"
  note: "Free public PDFs; 715 reports (17 Apr-5 Jun 2023, 2-10 Oct 2023, 2 Jan 2024-5 Oct 2026) were parsed for the baselines; only the event-day files below are archived. Format change: dated header and VWAP lines in recent reports."
- {slug: pse-dqr-2023-05-31, title: "PSE Daily Quotation Report 2023-05-31", publisher: "The Philippine Stock Exchange", type: pdf, canonical_url: "https://documents.pse.com.ph/market_report/May%2031,%202023-EOD.pdf", local_path: pdfs/pse-dqr-2023-05-31.pdf, edition: historical, amended_through: "2023-05-31", note: "MSCI day; grand total p.12"}
- {slug: pse-dqr-2024-02-29, title: "PSE Daily Quotation Report 2024-02-29", publisher: "The Philippine Stock Exchange", type: pdf, canonical_url: "https://documents.pse.com.ph/market_report/February%2029,%202024-EOD.pdf", local_path: pdfs/pse-dqr-2024-02-29.pdf, edition: historical, amended_through: "2024-02-29", note: "MSCI day"}
- {slug: pse-dqr-2024-05-31, title: "PSE Daily Quotation Report 2024-05-31", publisher: "The Philippine Stock Exchange", type: pdf, canonical_url: "https://documents.pse.com.ph/market_report/May%2031,%202024-EOD.pdf", local_path: pdfs/pse-dqr-2024-05-31.pdf, edition: historical, amended_through: "2024-05-31", note: "MSCI day"}
- {slug: pse-dqr-2024-08-30, title: "PSE Daily Quotation Report 2024-08-30", publisher: "The Philippine Stock Exchange", type: pdf, canonical_url: "https://documents.pse.com.ph/market_report/August%2030,%202024-EOD.pdf", local_path: pdfs/pse-dqr-2024-08-30.pdf, edition: historical, amended_through: "2024-08-30", note: "MSCI day"}
- {slug: pse-dqr-2024-11-25, title: "PSE Daily Quotation Report 2024-11-25", publisher: "The Philippine Stock Exchange", type: pdf, canonical_url: "https://documents.pse.com.ph/market_report/November%2025,%202024-EOD.pdf", local_path: pdfs/pse-dqr-2024-11-25.pdf, edition: historical, amended_through: "2024-11-25", note: "MSCI day"}
- {slug: pse-dqr-2025-02-28, title: "PSE Daily Quotation Report 2025-02-28", publisher: "The Philippine Stock Exchange", type: pdf, canonical_url: "https://documents.pse.com.ph/market_report/February%2028,%202025-EOD.pdf", local_path: pdfs/pse-dqr-2025-02-28.pdf, edition: historical, amended_through: "2025-02-28", note: "MSCI day (JGS, URC)"}
- {slug: pse-dqr-2025-05-30, title: "PSE Daily Quotation Report 2025-05-30", publisher: "The Philippine Stock Exchange", type: pdf, canonical_url: "https://documents.pse.com.ph/market_report/May%2030,%202025-EOD.pdf", local_path: pdfs/pse-dqr-2025-05-30.pdf, edition: historical, amended_through: "2025-05-30", note: "MSCI day; PHP 24.5bn block trades on p.12"}
- {slug: pse-dqr-2025-08-26, title: "PSE Daily Quotation Report 2025-08-26", publisher: "The Philippine Stock Exchange", type: pdf, canonical_url: "https://documents.pse.com.ph/market_report/August%2026,%202025-EOD.pdf", local_path: pdfs/pse-dqr-2025-08-26.pdf, edition: historical, amended_through: "2025-08-26", note: "MSCI day"}
- {slug: pse-dqr-2025-11-24, title: "PSE Daily Quotation Report 2025-11-24", publisher: "The Philippine Stock Exchange", type: pdf, canonical_url: "https://documents.pse.com.ph/market_report/November%2024,%202025-EOD.pdf", local_path: pdfs/pse-dqr-2025-11-24.pdf, edition: historical, amended_through: "2025-11-24", note: "MSCI day"}
- {slug: pse-dqr-2026-02-27, title: "PSE Daily Quotation Report 2026-02-27", publisher: "The Philippine Stock Exchange", type: pdf, canonical_url: "https://documents.pse.com.ph/market_report/February%2027,%202026-EOD.pdf", local_path: pdfs/pse-dqr-2026-02-27.pdf, edition: historical, amended_through: "2026-02-27", note: "MSCI day (MYNLD, APX additions)"}
- {slug: pse-dqr-2026-05-29, title: "PSE Daily Quotation Report 2026-05-29", publisher: "The Philippine Stock Exchange", type: pdf, canonical_url: "https://documents.pse.com.ph/market_report/May%2029,%202026-EOD.pdf", local_path: pdfs/pse-dqr-2026-05-29.pdf, edition: historical, amended_through: "2026-05-29", note: "MSCI day (JFC, MER)"}
- {slug: pse-dqr-2026-08-28, title: "PSE Daily Quotation Report 2026-08-28", publisher: "The Philippine Stock Exchange", type: pdf, canonical_url: "https://documents.pse.com.ph/market_report/August%2028,%202026-EOD.pdf", local_path: pdfs/pse-dqr-2026-08-28.pdf, edition: historical, amended_through: "2026-08-28", note: "Last PSE session before the MSCI 31 Aug 2026 date (ALI); current report layout"}
- {slug: pse-dqr-2024-03-15, title: "PSE Daily Quotation Report 2024-03-15", publisher: "The Philippine Stock Exchange", type: pdf, canonical_url: "https://documents.pse.com.ph/market_report/March%2015,%202024-EOD.pdf", local_path: pdfs/pse-dqr-2024-03-15.pdf, edition: historical, amended_through: "2024-03-15", note: "FTSE third-Friday day"}
- {slug: pse-dqr-2024-06-21, title: "PSE Daily Quotation Report 2024-06-21", publisher: "The Philippine Stock Exchange", type: pdf, canonical_url: "https://documents.pse.com.ph/market_report/June%2021,%202024-EOD.pdf", local_path: pdfs/pse-dqr-2024-06-21.pdf, edition: historical, amended_through: "2024-06-21", note: "FTSE day"}
- {slug: pse-dqr-2024-09-20, title: "PSE Daily Quotation Report 2024-09-20", publisher: "The Philippine Stock Exchange", type: pdf, canonical_url: "https://documents.pse.com.ph/market_report/September%2020,%202024-EOD.pdf", local_path: pdfs/pse-dqr-2024-09-20.pdf, edition: historical, amended_through: "2024-09-20", note: "FTSE day"}
- {slug: pse-dqr-2024-12-20, title: "PSE Daily Quotation Report 2024-12-20", publisher: "The Philippine Stock Exchange", type: pdf, canonical_url: "https://documents.pse.com.ph/market_report/December%2020,%202024-EOD.pdf", local_path: pdfs/pse-dqr-2024-12-20.pdf, edition: historical, amended_through: "2024-12-20", note: "FTSE day"}
- {slug: pse-dqr-2025-03-21, title: "PSE Daily Quotation Report 2025-03-21", publisher: "The Philippine Stock Exchange", type: pdf, canonical_url: "https://documents.pse.com.ph/market_report/March%2021,%202025-EOD.pdf", local_path: pdfs/pse-dqr-2025-03-21.pdf, edition: historical, amended_through: "2025-03-21", note: "FTSE day"}
- {slug: pse-dqr-2025-06-20, title: "PSE Daily Quotation Report 2025-06-20", publisher: "The Philippine Stock Exchange", type: pdf, canonical_url: "https://documents.pse.com.ph/market_report/June%2020,%202025-EOD.pdf", local_path: pdfs/pse-dqr-2025-06-20.pdf, edition: historical, amended_through: "2025-06-20", note: "FTSE day"}
- {slug: pse-dqr-2025-09-19, title: "PSE Daily Quotation Report 2025-09-19", publisher: "The Philippine Stock Exchange", type: pdf, canonical_url: "https://documents.pse.com.ph/market_report/September%2019,%202025-EOD.pdf", local_path: pdfs/pse-dqr-2025-09-19.pdf, edition: historical, amended_through: "2025-09-19", note: "FTSE day"}
- {slug: pse-dqr-2025-12-19, title: "PSE Daily Quotation Report 2025-12-19", publisher: "The Philippine Stock Exchange", type: pdf, canonical_url: "https://documents.pse.com.ph/market_report/December%2019,%202025-EOD.pdf", local_path: pdfs/pse-dqr-2025-12-19.pdf, edition: historical, amended_through: "2025-12-19", note: "FTSE day; PHP 7.35bn block trades"}
- {slug: pse-dqr-2026-06-19, title: "PSE Daily Quotation Report 2026-06-19", publisher: "The Philippine Stock Exchange", type: pdf, canonical_url: "https://documents.pse.com.ph/market_report/June%2019,%202026-EOD.pdf", local_path: pdfs/pse-dqr-2026-06-19.pdf, edition: historical, amended_through: "2026-06-19", note: "FTSE day"}
- {slug: pse-dqr-2026-09-18, title: "PSE Daily Quotation Report 2026-09-18", publisher: "The Philippine Stock Exchange", type: pdf, canonical_url: "https://documents.pse.com.ph/market_report/September%2018,%202026-EOD.pdf", local_path: pdfs/pse-dqr-2026-09-18.pdf, edition: historical, amended_through: "2026-09-18", note: "FTSE Sep 2026 review day; grand total p.12"}
- {slug: pse-dqr-2025-01-31, title: "PSE Daily Quotation Report 2025-01-31", publisher: "The Philippine Stock Exchange", type: pdf, canonical_url: "https://documents.pse.com.ph/market_report/January%2031,%202025-EOD.pdf", local_path: pdfs/pse-dqr-2025-01-31.pdf, edition: historical, amended_through: "2025-01-31", note: "Last session before PSEi change of 3 Feb 2025 (CBC, AREIT in; NIKL, WLCON out)"}
- {slug: pse-dqr-2025-08-15, title: "PSE Daily Quotation Report 2025-08-15", publisher: "The Philippine Stock Exchange", type: pdf, canonical_url: "https://documents.pse.com.ph/market_report/August%2015,%202025-EOD.pdf", local_path: pdfs/pse-dqr-2025-08-15.pdf, edition: historical, amended_through: "2025-08-15", note: "Last session before PSEi change of 18 Aug 2025 (PLUS in, BLOOM out)"}
- {slug: pse-dqr-2026-01-30, title: "PSE Daily Quotation Report 2026-01-30", publisher: "The Philippine Stock Exchange", type: pdf, canonical_url: "https://documents.pse.com.ph/market_report/January%2030,%202026-EOD.pdf", local_path: pdfs/pse-dqr-2026-01-30.pdf, edition: historical, amended_through: "2026-01-30", note: "Last session before PSEi change of 2 Feb 2026 (RCR in, AGI out)"}
- {slug: pse-dqr-2026-07-31, title: "PSE Daily Quotation Report 2026-07-31", publisher: "The Philippine Stock Exchange", type: pdf, canonical_url: "https://documents.pse.com.ph/market_report/July%2031,%202026-EOD.pdf", local_path: pdfs/pse-dqr-2026-07-31.pdf, edition: historical, amended_through: "2026-07-31", note: "Last session before PSEi change of 3 Aug 2026 (MYNLD in, CNVRG out)"}

# ---- MSCI ----
- slug: msci-philippines-index-factsheet-2026-09
  title: "MSCI Philippines Index (USD) factsheet"
  publisher: "MSCI Inc."
  type: pdf
  canonical_url: "https://www.msci.com/documents/10199/255599/msci-philippines-index.pdf"
  local_path: pdfs/msci-philippines-index-factsheet-2026-09.pdf
  edition: in-force
  amended_through: "2026-09-30"
  note: "Data as of 30 Sep 2026 (the live URL is overwritten monthly); 9 constituents."
- slug: msci-philippines-imi-factsheet-2026-09
  title: "MSCI Philippines IMI (USD) factsheet"
  publisher: "MSCI Inc."
  type: pdf
  canonical_url: "https://www.msci.com/documents/10199/bc7baeb7-5945-4191-aa9f-88e5e024b28c"
  local_path: pdfs/msci-philippines-imi-factsheet-2026-09.pdf
  edition: in-force
  amended_through: "2026-09-30"
  note: "34 constituents; data as of 30 Sep 2026."
- slug: msci-em-index-factsheet-2026-09
  title: "MSCI Emerging Markets Index (USD) factsheet"
  publisher: "MSCI Inc."
  type: pdf
  canonical_url: "https://www.msci.com/documents/10199/c0db0a48-01f2-4ba9-ad01-226fd5678111"
  local_path: pdfs/msci-em-index-factsheet-2026-09.pdf
  edition: in-force
  amended_through: "2026-09-30"
  note: "1,165 constituents; USD 12.28 trillion; Philippines not shown separately."
- slug: msci-index-review-factsheet-2026-05
  title: "Insights from MSCI: May 2026 Index Review"
  publisher: "MSCI Inc."
  type: pdf
  canonical_url: "https://www.msci.com/downloads/web/msci-com/indexes/quarterly-index-review/Index%20Rebalance%20Factsheet_MAy%202026%203.pdf"
  local_path: pdfs/msci-index-review-factsheet-2026-05.pdf
  edition: historical
  amended_through: "2026-05-12"
  note: "Announcement date stated in the document; implementation as of the close of 29 May 2026; no country detail."

# ---- FTSE Russell ----
- slug: ftse-geis-ground-rules-2026-09
  title: "FTSE Global Equity Index Series Ground Rules v14.4"
  publisher: "FTSE Russell (LSEG)"
  type: pdf
  canonical_url: "https://www.lseg.com/content/dam/ftse-russell/en_us/documents/ground-rules/ftse-global-equity-index-series-ground-rules.pdf"
  local_path: pdfs/ftse-geis-ground-rules-2026-09.pdf
  edition: in-force
  amended_through: "undated"
  note: "Cover 'v14.4, September 2026' (no day); Appendix E classification; sections 4 and 7."
- slug: ftse-country-classification-interim-2026-03
  title: "FTSE Equity Country Classification: March 2026 Interim Announcement"
  publisher: "FTSE Russell (LSEG)"
  type: pdf
  canonical_url: "https://www.lseg.com/content/dam/ftse-russell/en_us/documents/country-classification/ftse-interim-country-classification-review-2026.pdf"
  local_path: pdfs/ftse-country-classification-interim-2026-03.pdf
  edition: in-force
  amended_through: "2026-04-07"
  note: "Published date on the cover; states the 2026 annual announcement is due 6 Oct 2026."
- slug: ftse-country-classification-annual-2025-09
  title: "FTSE Equity Country Classification: September 2025 Announcement"
  publisher: "FTSE Russell (LSEG)"
  type: pdf
  canonical_url: "https://www.lseg.com/content/dam/ftse-russell/en_us/documents/country-classification/ftse-country-classification-update-2025.pdf"
  local_path: pdfs/ftse-country-classification-annual-2025-09.pdf
  edition: in-force
  amended_through: "2025-10-07"
  note: "Published date on the cover; to be superseded by the 2026 annual announcement."
- slug: ftse-watch-list-2026-03
  title: "FTSE Quality of Markets Criteria (Watch List) as at March 2026"
  publisher: "FTSE Russell (LSEG)"
  type: pdf
  canonical_url: "https://www.lseg.com/content/dam/ftse-russell/en_us/documents/country-classification/watch-list-latest.pdf"
  local_path: pdfs/ftse-watch-list-2026-03.pdf
  edition: in-force
  amended_through: "undated"
  note: "Page caption 'as at March 2026'; names Egypt only."
- slug: ftse-quality-of-markets-asia-pacific-2026-03
  title: "FTSE Quality of Markets Criteria (Asia Pacific) as at March 2026"
  publisher: "FTSE Russell (LSEG)"
  type: pdf
  canonical_url: "https://www.lseg.com/content/dam/ftse-russell/en_us/documents/country-classification/asia-pacific-latest.pdf"
  local_path: pdfs/ftse-quality-of-markets-asia-pacific-2026-03.pdf
  edition: in-force
  amended_through: "undated"
  note: "Page caption 'as at March 2026'; the Philippines column was read by cell position (verify visually)."
- slug: ftse-equity-country-classification-page
  title: "FTSE Equity Country Classification (landing page)"
  publisher: "FTSE Russell (LSEG)"
  type: web
  canonical_url: "https://www.ftserussell.com/equity-country-classification"
  local_path: null
  edition: in-force
  amended_through: "undated"
  note: "Retrieved 6 Oct 2026; links the 2026 annual announcement as 'Document to follow'."

# ---- PSE web pages ----
- slug: pse-data-products-page
  title: "PSE Data Products (real-time, delayed, NDU, news, EOD, historical, reports, index services)"
  publisher: "The Philippine Stock Exchange"
  type: web
  canonical_url: "https://www.pse.com.ph/data-products/"
  local_path: null
  edition: in-force
  amended_through: "undated"
  note: "Retrieved 6 Oct 2026; contains the historical price list."
- slug: pse-new-trading-engine-page
  title: "PSE Trading Engine 2026 (Nasdaq Eqlipse): overview, system features, market data feed, FAQs"
  publisher: "The Philippine Stock Exchange"
  type: web
  canonical_url: "https://www.pse.com.ph/pse-new-trading-engine/"
  local_path: null
  edition: in-force
  amended_through: "undated"
  note: "Retrieved 6 Oct 2026; lists ITCH/MDF spec versions (not public) and static-data specs."
- slug: pse-psetrade-xts-page
  title: "PSEtrade XTS (current engine): overview, connectivity, ITCH specs, FIX specs"
  publisher: "The Philippine Stock Exchange"
  type: web
  canonical_url: "https://www.pse.com.ph/psetrade-xts/"
  local_path: null
  edition: in-force
  amended_through: "undated"
  note: "Retrieved 6 Oct 2026; states migration to XTS on 22 Jun 2015."
- slug: pse-investing-page
  title: "Investing at PSE (trading hours and holidays)"
  publisher: "The Philippine Stock Exchange"
  type: web
  canonical_url: "https://www.pse.com.ph/investing-at-pse/"
  local_path: null
  edition: in-force
  amended_through: "undated"
  note: "Retrieved 6 Oct 2026; shows a current table (close 3:15 pm) and an older table (close 3:30 pm)."
- slug: pse-indices-page
  title: "PSE Indices (series overview, factsheets, policy links)"
  publisher: "The Philippine Stock Exchange"
  type: web
  canonical_url: "https://www.pse.com.ph/indices/"
  local_path: null
  edition: in-force
  amended_through: "undated"
  note: "Retrieved 6 Oct 2026; still links the Jan 2024 policy and Sep 2025 factsheets."
- slug: pse-pr-2026-08-mynld-joins-psei
  title: "MYNLD to join PSEi, replacing CNVRG (PSE press release)"
  publisher: "The Philippine Stock Exchange"
  type: web
  canonical_url: "https://www.pse.com.ph/mynld-to-join-psei-replacing-cnvrg/"
  local_path: null
  edition: historical
  amended_through: "undated"
  note: "Context date about 27 Jul 2026; includes the statement that the next review will use the revised criteria."
- slug: pse-pr-2026-02-rcr-replaces-agi
  title: "RCR replaces AGI in PSE index (PSE press release)"
  publisher: "The Philippine Stock Exchange"
  type: web
  canonical_url: "https://www.pse.com.ph/rcr-replaces-agi-in-pse-index/"
  local_path: null
  edition: historical
  amended_through: "undated"
  note: "Effective 2 Feb 2026."
- slug: pse-pr-2023-08-psei-retains-composition
  title: "PSEi retains composition in recent index review (PSE press release)"
  publisher: "The Philippine Stock Exchange"
  type: web
  canonical_url: "https://www.pse.com.ph/psei-retains-composition-in-recent-index-review/"
  local_path: null
  edition: historical
  amended_through: "undated"
  note: "Jul 2022-Jun 2023 review."
- slug: pse-pr-2022-08-semirara-in-security-bank-out
  title: "PSE index changes: Semirara Mining in, Security Bank out (PSE press release)"
  publisher: "The Philippine Stock Exchange"
  type: web
  canonical_url: "https://www.pse.com.ph/pse-index-changes-semirara-mining-in-security-bank-out/"
  local_path: null
  edition: historical
  amended_through: "undated"
  note: "Effective 8 Aug 2022; records the Aug 2021 announcement of the 20% float rule."
- slug: pse-pr-2018-02-no-changes-float-15pct
  title: "No changes in PSEi members in latest PSE review (PSE press release)"
  publisher: "The Philippine Stock Exchange"
  type: web
  canonical_url: "https://www.pse.com.ph/no-changes-in-psei-members-in-latest-pse-review/"
  local_path: null
  edition: historical
  amended_through: "undated"
  note: "Effective 19 Feb 2018; float requirement raised from 12% to 15%."

# ---- Secondary and other sources ----
- slug: rappler-2014-01-27-broker-anonymity
  title: "PSE to implement broker anonymity by 2015"
  publisher: "Rappler"
  type: web
  canonical_url: "https://www.rappler.com/?p=48994"
  local_path: null
  edition: historical
  amended_through: "2014-01-27"
  note: "Secondary; reports the PSE media release of 27 Jan 2014."
- slug: philstar-2014-05-12-fear-of-the-dark
  title: "Fear of the dark"
  publisher: "The Philippine Star"
  type: web
  canonical_url: "https://www.philstar.com/business/2014/05/12/1322021/fear-dark"
  local_path: null
  edition: historical
  amended_through: "2014-05-12"
  note: "Secondary opinion/analysis on the anonymity proposal."
- slug: philstocks-broker-activity
  title: "Philstocks One Screen: Broker Activity"
  publisher: "Philstocks (Accord Capital Equities Corp.)"
  type: web
  canonical_url: "https://my.philstocks.ph/onescreen/brokerActivity.cshtml?bid=911"
  local_path: null
  edition: n/a
  amended_through: "undated"
  note: "Secondary; undated screen, values shown as zero when retrieved."
- slug: ice-developer-pse
  title: "ICE Fixed Income Data Services catalogue: Philippine Stock Exchange (PSE)"
  publisher: "Intercontinental Exchange"
  type: web
  canonical_url: "https://developer.ice.com/fixed-income-data-services/catalog/philippine-stock-exchange-pse"
  local_path: null
  edition: in-force
  amended_through: "undated"
  note: "Vendor description of PSE coverage; no fees or latency."
- slug: manilatimes-2023-01-28-dmc-ubp
  title: "DMCI, UnionBank to make PSEi return"
  publisher: "The Manila Times"
  type: web
  canonical_url: "https://manilatimes.net/2023/01/28/business/top-business/dmci-unionbank-to-make-psei-return/1876168"
  local_path: null
  edition: historical
  amended_through: "2023-01-28"
  note: "Secondary; Feb 2023 PSEi change."
- slug: metrobank-what-is-msci-rebalancing
  title: "What is the MSCI rebalancing?"
  publisher: "Metrobank Wealth Insights"
  type: web
  canonical_url: "https://wealthinsights.metrobank.com.ph/explainer/what-is-the-msci-rebalancing/"
  local_path: null
  edition: historical
  amended_through: "undated"
  note: "Secondary; 31 May 2023 volume and foreign-flow figures (match the DQR)."
- slug: philstar-2025-02-15-msci-jgs-urc
  title: "JG Summit, URC deleted from MSCI Philippines Index"
  publisher: "The Philippine Star"
  type: web
  canonical_url: "https://www.philstar.com/business/2025/02/15/2421549/jg-summit-urc-deleted-frommsci-philippines-index"
  local_path: null
  edition: historical
  amended_through: "2025-02-15"
  note: "Secondary; AP Securities flow estimates."
- slug: inquirer-2026-02-msci-standard-unchanged
  title: "MSCI Philippines standard index unchanged; Maynilad, Apex enter small-cap basket"
  publisher: "Philippine Daily Inquirer"
  type: web
  canonical_url: "https://business.inquirer.net/573496/msci-philippines-standard-index-unchanged-maynilad-apex-enter-small-cap-basket"
  local_path: null
  edition: historical
  amended_through: "undated"
  note: "Secondary; headline and summary seen only in search results, page returned HTTP 403."
- slug: insiderph-2026-02-first-metro-msci
  title: "First Metro: MSCI shake-up unlikely for PH main index; Apex, Maynilad in focus"
  publisher: "InsiderPH"
  type: web
  canonical_url: "https://insiderph.com/first-metro-msci-shake-up-unlikely-for-ph-main-index-apex-maynilad-in-focus"
  local_path: null
  edition: historical
  amended_through: "undated"
  note: "Secondary; Feb 2026 pre-review view (First Metro Securities)."
- slug: insiderph-2026-07-index-overhaul
  title: "PSE modernizes benchmark indices in biggest overhaul in 15 years"
  publisher: "InsiderPH"
  type: web
  canonical_url: "https://insiderph.com/pse-modernizes-benchmark-indices-in-biggest-overhaul-in-15-years"
  local_path: null
  edition: historical
  amended_through: "2026-07-21"
  note: "Secondary; dated in the site's headline feed."
- slug: insiderph-2026-07-insider-info-overhaul
  title: "INSIDER INFO: Inside PSE's biggest index overhaul in 15 years"
  publisher: "InsiderPH"
  type: web
  canonical_url: "https://insiderph.com/insider-info-i-inside-pses-biggest-index-overhaul-in-15-years"
  local_path: null
  edition: historical
  amended_through: "undated"
  note: "Secondary; anonymous-source account of the rationale."
- slug: insiderph-2026-07-etf-reboot
  title: "PSE opens door to global stocks, bonds and crypto in ETF market reboot"
  publisher: "InsiderPH"
  type: web
  canonical_url: "https://insiderph.com/pse-opens-door-to-global-stocks-bonds-and-crypto-in-etf-market-reboot"
  local_path: null
  edition: historical
  amended_through: "undated"
  note: "Secondary; says the first and only PSE ETF is the First Metro Philippine Equity ETF (2013)."
- slug: insiderph-2026-08-ali-msci
  title: "Ayala Land loses MSCI index spot, moves to small-cap after stock decline"
  publisher: "InsiderPH"
  type: web
  canonical_url: "https://insiderph.com/ayala-land-loses-msci-index-spot-moves-to-small-cap-after-stock-decline"
  local_path: null
  edition: historical
  amended_through: "undated"
  note: "Secondary; Aug 2026 MSCI change."
- slug: insiderph-2026-08-emperador-ftse
  title: "Emperador returns to FTSE global index in boost for foreign investor reach"
  publisher: "InsiderPH"
  type: web
  canonical_url: "https://insiderph.com/emperador-returns-to-ftse-global-index-in-boost-for-foreign-investor-reach"
  local_path: null
  edition: historical
  amended_through: "undated"
  note: "Secondary; FTSE Sep 2026 review, announced 21 Aug."
- slug: bilyonaryo-2026-08-25-msci-presence-abacus
  title: "Philippines' MSCI presence sinks to decade low as stock market loses ground to ASEAN peers: Abacus"
  publisher: "Bilyonaryo"
  type: web
  canonical_url: "https://bilyonaryo.com/2026/08/25/philippines-msci-presence-sinks-to-decade-low-as-stock-market-loses-ground-to-asean-peers-abacus/money/"
  local_path: null
  edition: historical
  amended_through: "2026-08-25"
  note: "Secondary; publication timestamp in page metadata."
```
