# PSE Order Matching, Auctions, Block Sales and Crossing (research notes for KB Chapters 5 "Matching" and 6 "Auctions")

*Prepared 6 October 2026 for the Philippine Stock Exchange (PSE) equity-microstructure knowledge base. Scope: how PSE matches orders, how the opening and closing auctions set prices, how the official close is defined, and how block sales, crosses and related pre-arranged facilities work. Price-control thresholds, circuit breakers, tick/lot tables and market-data dissemination are covered by other researchers and are touched only where they change matching behaviour.*

**Evidence tags used in every bullet.** `[P]` = stated in a primary document (PSE rulebook, memorandum, circular, vendor specification, SEC/Republic Act text). `[P*]` = my own computation from primary data (PSE daily reports) - reproducible but not stated by PSE. `[S]` = secondary source only (news/web article). `[I]` = my inference or reading of ambiguous text. Citation format: `[^slug:N]` = archived PDF `kb/pdfs/<slug>.pdf`, physical page N; `[^slug]` = web page (not archived as PDF).

**Abbreviations.** XTS = PSEtrade XTS, the current engine (Nasdaq X-stream). NTE = New Trading Engine (Nasdaq Eqlipse Trading), scheduled go-live 23 Nov 2026. RTR = Revised Trading Rules (June 2010 base text); IG = Implementing Guidelines; TP = Trading Participant (broker); IOP = indicative opening price; LTP = last traded price; LACP = last adjusted closing price; BBO = best bid and offer; MOO/MOC = market-on-opening/closing order; FAK = fill-and-kill; DT/ST = dynamic/static threshold.

---

## 0. What is in force today (6 Oct 2026) and what changes on 23 Nov 2026

### Takeaway
The rules in force today are the SEC-approved Revised Trading Rules and Implementing Guidelines that took effect with the new trading system on 26 Jul 2010, as amended piecemeal (2011, 2013, 2020, 2021 hours, 2024 VWAP, 2025 market-halt rules), running on PSEtrade XTS since 22 Jun 2015; PSE publishes no consolidated current rulebook. A new engine (Nasdaq Eqlipse) is scheduled to go live on 23 Nov 2026 with a one-share lot (odd-lot market abolished), a changed run-off rule and a "Negotiated Trades" facility, but as of PSE's own 17 Aug 2026 status slide these amendments had not yet been approved by the SEC and I found no later approval notice.

### Cited Findings
- `[P]` The SEC approved the Revised Trading Rules by letter of 1 Jun 2010; PSE's memo of 8 Jun 2010 says they take effect on the launch date of the New Trading System (NTS).[^pse-revised-trading-rules:1][^pse-revised-trading-rules:2] The Implementing Guidelines "shall take effect upon launching of the New Trading System on Monday, 26 July 2010".[^pse-implementing-guidelines-trading-rules:1]
- `[P]` PSE's rules page still serves the June 2010 compilation as "Revised Trading Rules" and lists only separate amendment documents: 2011 trading-rule and IG amendments (TPA 2011-0110, 2011-0124), 2013 unbundling deadline / extended pre-close / done-through memos (TPA 2013-0109, -0185, -0200), 2020 static-threshold and circuit-breaker amendments, and the 2024 VWAP rules.[^pse-regulation-trading-participants] No consolidated, current text is published.
- `[P]` Engine history: PSEtrade XTS (Nasdaq X-stream) went live 22 Jun 2015 and replaced the NSC platform of NYSE Euronext Technologies.[^pse-psetrade-xts] `[I]` NSC was therefore the engine behind the July 2010 new trading system, so the 2010 rulebook was written for NSC; PSE circulated XTS-driven revisions on 3 Nov 2014 ("will be implemented together with the launch date of PSE trade XTS"): Art. IV s.9 order types, s.20 error transactions, Art. VII ss.1, 2, 4 security states, Art. VIII s.1 circuit breaker.[^pse-memo-revisions-trading-rules-consultation-2014:1]
- `[P]` Next engine: PSE disclosed on 22 May 2025 a contract with Nasdaq Technology AB for "Nasdaq Eqlipse Trading", a multi-asset engine.[^pse-17c-2025-05-22-nasdaq-eqlipse-contract:2] Project schedule (9 Jul 2026 broker forum): FEOMS certification 10-23 Sep 2026; pre-production testing 12-22 Oct; Saturday market rehearsals 31 Oct, 7 Nov, 14 Nov; **go-live 23 Nov 2026**.[^pse-nte-broker-forum-2026-07-09:9] FAQ: "no parallel runs ... big bang approach".[^pse-nte-faq-2026-08:1] News (Philstar, 23 Jul 2026) reports go-live "by November".[^philstar-nte-golive-2026-07-23] `[S]`
- `[P]` Rule changes tied to the NTE: (i) "One Lot One Share" - lot size 1 for all securities, Odd Lot Market abolished;[^pse-cn-2025-0046-board-lot-trading-at-last:3][^pse-cn-2025-0046-board-lot-trading-at-last:5] (ii) Art. IV s.18 run-off rule rewritten (orders accepted at the closing price even when better-priced passive orders exist);[^pse-cn-2025-0046-board-lot-trading-at-last:5][^pse-cn-2025-0046-board-lot-trading-at-last:8] (iii) Negotiated Trades facility;[^pse-cn-2026-0031-negotiated-trades:3] (iv) "On Day 1 of the New Trading Engine, only limit order will be supported."[^pse-nte-faq-2026-08:1]
- `[P]` Status: PSE's 1H-2026 analyst briefing (17 Aug 2026) shows "One Share, One Lot" as "Status: For SEC Approval - Targeted for implementation in Q4 2026 alongside the new trading engine" and "Negotiated Trades" as "Status: Revising per Public Comments".[^pse-analyst-briefing-1h-2026:9] CN-2025-0046 (consultation closed 31 Dec 2025) bundles the board-lot and run-off changes;[^pse-cn-2025-0046-board-lot-trading-at-last:1] CN-2026-0031 (Negotiated Trades; comments to 7 Jul 2026) is still a "Consultation Paper" whose "final version ... may differ".[^pse-cn-2026-0031-negotiated-trades:1][^pse-cn-2026-0031-negotiated-trades:2] Re-checked on 6 Oct 2026: the "Updates" tab of PSE's NTE page lists only CN-2025-0046 (15 Dec 2025 request for comments) and no approval notice, and no new circular (CN-2026-0045 onward, TPA-2026-0042 onward) was retrievable.[^pse-new-trading-engine]
- `[P]` Trading schedule in force (whole-day): Pre-Open 09:00, Pre-Open No-Cancel 09:15, Market Open 09:30, Recess 12:00, Resume 13:00, Pre-Close 14:45, Pre-Close No-Cancel 14:48, Run-off/Trading-at-Last 14:50, Closing VWAP Session 15:00, Market Close 15:15. Introduced by CN-2021-0059 effective 6 Dec 2021 "until further notice";[^pse-cn-2021-0059:1] the 15:00-15:15 VWAP session was added by the SEC-approved VWAP Trading Rules (CN-2024-0010, 1 Feb 2024; half-day: Pre-Open 09:00, No-Cancel 09:15, Open 09:30, Pre-Close 11:57, No-Cancel 11:59, Run-off 12:00, Closing VWAP 12:10, Close 12:25).[^pse-approved-rules-vwap-trading-2024:3] PSE's website shows the same table.[^pse-investing-at-pse]
- `[P]` Article numbering differs between documents: the 2010 base text has Cross Transactions and Block Sale as Art. VI;[^pse-revised-trading-rules:31] the 2024 VWAP annex labels the new VWAP article "Article VI";[^pse-approved-rules-vwap-trading-2024:4] the July 2026 draft calls Cross/Block/Negotiated Trades "Article VII";[^pse-cn-2026-0031-negotiated-trades:7] the Aug 2025 halt amendment still refers to Market Halt as Art. VIII s.2.[^pse-cn-2025-0037:3] I cite base-text article numbers and flag that they may have shifted.

**Parameter cheat-sheet (legacy XTS rules in force on 6 Oct 2026; NTE changes in brackets)**
| Item | Value | Source |
|---|---|---|
| Opening call | 09:00-09:15 enter/amend/cancel; 09:15-09:30 enter only; uncross 09:30:00; five-step price rule, reference = previous close/ACP | [^pse-approved-rules-vwap-trading-2024:6][^pse-revised-trading-rules:24] |
| Closing call | 14:45-14:48 enter/amend/cancel; 14:48-14:50 enter only; uncross 14:50; same rule, reference = LTP | [^pse-cn-2021-0059:1][^pse-revised-trading-rules:24] |
| Run-off | 14:50-15:00, orders only at the closing price [NTE draft: also against better-priced passive orders] | [^pse-revised-trading-rules:27][^pse-cn-2025-0046-board-lot-trading-at-last:5] |
| Closing VWAP session | 15:00-15:15, VWAP price, >= PHP 500,000, one firm [NTE draft: + negotiated trades within +/-5% of VWAP] | [^pse-approved-rules-vwap-trading-2024:7][^pse-cn-2026-0031-negotiated-trades:3] |
| Regular block sale | >= PHP 20m; price within +/-5% of previous close/LACP; <= 4 decimals; application before run-off; approval <= 30 min | [^pse-implementing-guidelines-trading-rules:23][^pse-tpa-2011-0124-amended-implementing-guidelines:4] |
| Special block sale | >= PHP 50m; underlying agreement; COO approval <= 2 working days; Market Control executes | [^pse-implementing-guidelines-trading-rules:24] |
| DDS block sale | USD 500,000 regular / USD 1,000,000 special | [^pse-dds-rules:7] |
| Cross | within BBO; never in pre-open/pre-close; at closing price in run-off; not for block-eligible deals | [^pse-revised-trading-rules:31] |
| Iceberg | displayed >= 10% of order and a board-lot multiple | [^pse-revised-trading-rules:23] |
| Odd lot | separate book, continuous trading only [NTE: abolished, lot = 1 share] | [^pse-implementing-guidelines-trading-rules:20][^pse-nte-faq-2026-08:1] |
| Day-1 NTE order types | limit orders only | [^pse-nte-faq-2026-08:1] |

### Inferences
- `[I]` Anything an execution engine does before 23 Nov 2026 faces XTS behaviour: validate against the XTS FIX specification v2.5 and ITCH specification v2.3 (both archived) rather than the 2010 rule text alone, because the 2010 text predates XTS (e.g. FIX has no Market-to-Limit or GTW/Sliding validity).[^pse-fix-specification-v2-5:52][^pse-fix-specification-v2-5:53]
- `[I]` Because the run-off, odd-lot and Negotiated-Trade changes were still unapproved at last PSE status, the day-1 NTE rule set is uncertain; treat every NTE item below as "planned, unapproved".

### Gaps
- No consolidated current Revised Trading Rules/IG; the final SEC-approved text of the Nov 2014 XTS revisions (market-order remainder, MOO cancellation, freeze rules) was not found.
- No public SEC approval of CN-2025-0046 or CN-2026-0031 located. Circulars CN-2026-0036 to -0042 could not be retrieved (404), so an approval inside that range cannot be excluded.
- NTE order-entry (FIX v1.1, 8 Jun 2026) and market-data (ITCH/MDF v1.2, 17 Jul 2026) specifications are distributed only on request.[^pse-new-trading-engine]

### Execution implications
- Run two rule-sets behind a date switch (legacy XTS until the last session before 23 Nov 2026; NTE after), and keep a third "NTE as-approved" configuration ready to flip once PSE publishes the SEC-approved text.
- Day-1 NTE accepts limit orders only: any logic that relies on market orders, MOO/MOC, stop or market-to-limit orders needs a marketable-limit replacement before go-live.[^pse-nte-faq-2026-08:1]
- Plan for a one-share lot and no odd-lot book from go-live (position-sizing, odd-lot sweeps and "round-down to board lot" logic change).[^pse-nte-faq-2026-08:1]

---

## 1. Continuous matching: priority, order types, partial fills, price improvement, self-match

### Takeaway
Continuous trading is a central limit order book per board with strict price-then-time priority and trades printing at the resting order's price; order types, validity and iceberg rules are defined in RTR Art. IV s.9, while the FIX specification shows which of them XTS actually supports. PSE has no self-trade-prevention rule - instead RTR Art. VI s.2 gives a TP priority to match against its own earlier order ("automatic cross") and wash trades are policed under SRC s.24 and CMIC surveillance.

### Cited Findings
**Priority and execution price**
- `[P]` "Except for Block Sales, the Trading System shall match Orders at the Best Price."[^pse-revised-trading-rules:24] Orders are ranked by type then price then time: (1) Market Order, (2) Market-on-Opening/Closing Order, (3) Limit Order; same-type market/MOO orders by time of entry; limit orders "first by price (for buying side, Order with higher price will be given priority; while for the selling side, Order with lower price will be given priority), and then by time of entry".[^pse-implementing-guidelines-trading-rules:12]
- `[P]` Modification keeps queue priority when it involves "a decrease in its volume; a modification of validity type; or a modification of client account code"; it loses priority for "an increase in its volume; a modification of the limit price entered; or a modification of the trigger price".[^pse-revised-trading-rules:24][^pse-revised-trading-rules:25] The XTS FIX specification repeats this ("Any change to the price or trigger price of an order, or increasing quantities will result in the order losing its priority") and notes the exchange order id may change after amendment.[^pse-fix-specification-v2-5:25][^pse-fix-specification-v2-5:26] Client-to-proprietary modification is not allowed.[^pse-revised-trading-rules:25]
- `[P]` Price improvement: the aggressor trades at the resting order's price (limit orders execute "at the entered limit price or better").[^pse-revised-trading-rules:21][^pse-revised-trading-rules:24] `[I]` I found no mid-point, hidden-liquidity or odd-lot price-improvement mechanism in any PSE rule document. The only structural exception is the run-off period, where every execution is at the closing price (section 3).

**Order types (RTR Art. IV s.9, June 2010 text) and what XTS exposes**
- `[P]` Limit order: entered Pre-Open to Trading-at-Last with a limit price inside the static threshold; remainder is queued.[^pse-revised-trading-rules:21] Market order: entered without price, "executed either at the BBO or the LTP, whichever is better", enterable Pre-Open to continuous trading only; unexecuted remainder is "added and queued in the Order book for immediate execution".[^pse-revised-trading-rules:21][^pse-revised-trading-rules:22] Market-to-Limit: continuous trading only, executes at the best price between BBO and LTP, remainder becomes a limit order at the executed price, eliminated if no counterpart.[^pse-revised-trading-rules:22] Stop, Stop-Limit and Stop-Loss orders are released when a trade occurs at the trigger or better; a triggered Stop-Loss becomes a market order.[^pse-revised-trading-rules:22] MOO/MOC: entered in Pre-Open/Pre-Close, executable only at the indicative price; the unmatched balance becomes a limit order at that price.[^pse-revised-trading-rules:22]
- `[P]` XTS FIX specification v2.5 (10 Aug 2015): OrdType 1 Market ("executes against the best prices order on the opposite side"), 2 Limit, 3 Stop, 4 Stop Limit;[^pse-fix-specification-v2-5:52] TimeInForce 0 Day, 1 GTC, 3 IOC/FAK, 4 FOK, 6 GTD, 8 Session;[^pse-fix-specification-v2-5:53] MinQty and DisplayQty fields;[^pse-fix-specification-v2-5:16] ExecInst S/q moves an order to or from the private order book.[^pse-fix-specification-v2-5:50] Market-to-Limit, MOO/MOC, GTW and Sliding validity do not appear in the FIX enumerations.
- `[P]` A November 2014 consultation for the XTS launch proposed: market-order remainder queued "as limit order at the last executed price unless set as Immediate or Fill-and-Kill (FAK) in which case, unexecuted portion will be withdrawn", market order rejected "if no orders on the opposite side", and MOO/MOC cancelled when no indicative price exists.[^pse-memo-revisions-trading-rules-consultation-2014:2][^pse-memo-revisions-trading-rules-consultation-2014:3][^pse-memo-revisions-trading-rules-consultation-2014:4] Whether the SEC-approved wording matches is not public.
- `[P]` Validity types: Day; GTC; GTD; Good-Till-Week (7 calendar days); Sliding Validity (1 calendar year); FAK (in pre-open/pre-close "executed to the fullest extent possible at the end of Pre-Open/Pre-Close" with the remainder eliminated; in continuous/run-off executed immediately with the remainder eliminated).[^pse-revised-trading-rules:22][^pse-revised-trading-rules:23] XTS keeps non-day orders overnight; GTC/GTD orders priced outside the day's static threshold get "Unplaced" status and are invisible until re-activated.[^pse-psetrade-xts]
- `[P]` Volume qualifiers: Minimum-quantity (limit or market-to-limit; executed immediately to at least the minimum, else eliminated) and Iceberg ("disclosed quantity"; limit or stop-limit only; disclosed quantity "not less than 10% of the total quantity" and in board-lot multiples; "successively entered in the Order book").[^pse-revised-trading-rules:23] Permitted by phase: iceberg allowed for Day/GTD/GTC/Sliding orders in all phases but not with FAK; minimum quantity not allowed in pre-open/pre-close but allowed in continuous trading and run-off.[^pse-implementing-guidelines-trading-rules:12]
- `[P]` Per-order value limit set by TP per trader, capped by the Exchange limit; applies per order, not per day; the block-sale facility observes it too.[^pse-implementing-guidelines-trading-rules:17]

**Partial fills and cancellation**
- `[P]` Partially matched orders remain Active, the unmatched portion can be modified (without losing priority if only reduced) and cancelled.[^pse-implementing-guidelines-trading-rules:17][^pse-implementing-guidelines-trading-rules:18][^pse-revised-trading-rules:25] The Exchange cancels all active orders on corporate actions that adjust the closing price or when a security changes board-lot size, and cancels orders "that cross a Board Lot"; the Dec 2011 amendment (effective Jan 2012) also cancels orders "on the ex-date for Securities with cash and/or property dividends", so GTC/GTD/sliding orders do not survive an ex-date.[^pse-implementing-guidelines-trading-rules:18][^pse-revised-trading-rules:25][^pse-tpa-2011-0110-amended-revised-trading-rules:4]
- `[P]` When a partly matched limit order's remainder would breach the dynamic threshold, intermediate trades inside the threshold stand and the remainder goes to Market Control; orders at the BBO beyond the DT are auto-accepted; crosses that breach DT are auto-accepted (price-control detail belongs to the thresholds chapter).[^pse-implementing-guidelines-trading-rules:26]

**Phase permissions (XTS engine states)**
- `[P]` ITCH system-event table: 'S' Pre-Open (entry Y, amend/cancel Y, trading N); 'R' Pre-Open No-Cancel (Y/N/N); 'Q' Market Hours (Y/Y/Y; "Pre-Open uncross occurs, and continuous trading begins"); 'A'/'B' scheduled break (N/N/N then Y/Y/Y); 'L' Pre-Close (Y/Y/N); 'J' Pre-Close No-Cancel (Y/N/N); 'P' Trading At Last (entry Y, amend/cancel **N**, trading "Y*"); 'M' End of Market Hours (N/N/N).[^pse-itch-equities-feed-spec-v2-3:10] The IG, by contrast, says TPs may cancel active orders during Trading-at-Last/Run-Off and (Dec 2011 amendment) "from Pre-Open Period to Trading-at-Last Period, except during the Pre-Open No-Cancel Period, Pre-Close No-Cancel Period and Market Recess".[^pse-implementing-guidelines-trading-rules:18][^pse-tpa-2011-0124-amended-implementing-guidelines:3] Conflict unresolved (see Gaps).

**Self-match, internalisation and wash trades**
- `[P]` RTR Art. VI s.2 "Automatic Cross Transactions": "There shall be an automatic cross during the Market Open/Continuous Trading and Trading-at-Last/Run-Off Period when a Trading Participant has a posted Order and then posts another counterpart Order at the same or better price. In such event, the Trading Participant shall have the priority among Trading Participants who posted earlier in the queue. The newly posted counterpart Order shall be matched with its earlier posted Order regardless of its position in the queue."[^pse-revised-trading-rules:31] A "Cross Order" is "buying and selling Orders of the same Trading Participant that are simultaneously executed at the agreed quantity and price within the BBO" (details in section 6).[^pse-revised-trading-rules:22]
- `[P]` ITCH Trade Indicator 'C' marks an "intentional cross trade (the same user simultaneously entered both sides of the trade)"; the Total View feed publishes intentional cross, block and manual (market-control) trades through the Trade message, not through order-executed messages.[^pse-itch-equities-feed-spec-v2-3:18][^pse-itch-equities-feed-spec-v2-3:28]
- `[P]` No self-trade-prevention flag exists in the XTS FIX order-entry specification (order fields: ClOrdID, Parties, Account, ExecInst, OrderQty, OrdType, Price, Side, MinQty, TimeInForce, DisplayQty, triggers).[^pse-fix-specification-v2-5:15][^pse-fix-specification-v2-5:16] All FIX users of one firm receive execution reports for each other's orders.[^pse-fix-itch-session-week01-2014-10-03:6]
- `[P]` Wash trades and matched orders are unlawful: SRC s.24.1(a) bars transactions that involve "no change in the beneficial ownership" and orders entered "with the knowledge that a simultaneous order ... of substantially the same size, time and price" will be entered;[^ra-8799-src:24] the 2015 IRR lists wash sales, improper matched orders, painting the tape and marking the close as prohibited conduct.[^sec-2015-src-irr:68] CMIC surveillance (Korea Exchange TMS) polices this.[^pse-investing-at-pse]
- `[P]` Client-before-proprietary: "Customer First" Policy - "The Dealer-Broker shall give priority to the orders of its customers over trades for its own account" (SRC IRR Rule 34.1.2); clients' orders "shall have in all cases priority over orders for the account of the registered person" (Rule 30.2.1.2.6.1.1).[^sec-2015-src-irr:111][^sec-2015-src-irr:94] PSE requires separate traders for proprietary and client accounts (a TP may designate at most two "PC Traders", only one of which may handle both on a given day).[^pse-implementing-guidelines-trading-rules:8][^pse-implementing-guidelines-trading-rules:9]
- `[P]` Short-sell orders are rejected in the Pre-Open and Pre-Close phases, must be day orders, cannot be aggregated, and are not accepted in the Odd Lot Market or for Block Sales.[^pse-short-selling-guidelines-2023-10:2]

### Inferences
- `[I]` The automatic-cross rule is a broker-level internalisation priority: if TP A has an earlier resting buy and later sends a sell at the same or better price, the sell hits A's own buy first, ahead of other TPs' earlier orders at that price. The text does not say how it interacts with strictly better-priced orders of other TPs (price priority should still dominate); test in UAT before relying on it.
- `[I]` XTS probably does not offer GTW, Sliding Validity or Market-to-Limit (absent from FIX enumerations although in the 2010 text); the NTE FAQ confirms an even narrower Day-1 set (limit only).
- `[I]` An iceberg refill is "successively entered in the Order book", so each tranche most likely re-queues behind existing orders at the price; PSE does not publish refill-priority rules.

### Gaps
- Exact behaviour of a market order that exhausts the book (rests as limit at last execution price vs rejected) in current XTS; whether Market-to-Limit/GTW/Sliding exist on XTS.
- Whether amendments/cancels are rejected during Trading-at-Last on XTS (ITCH state table says N; IG says cancel allowed).
- Whether self-trade prevention exists in the NTE (no public statement).
- Interaction of automatic cross with price priority; whether a TP's two accounts (client vs proprietary) can auto-cross (SRC s.24 and the Customer First rule still apply).

### Execution implications
- Assume pure price-time priority; queue position is lost on price change or size increase, kept on size decrease. Cancel/replace logic should prefer "reduce" over "re-price" when queue position matters.
- Queue priority at a price level can be overtaken by a single TP that holds both sides (automatic cross): expect lower passive fill probability at the touch in names where large brokers hold offsetting client flow, and expect your own broker to internalise offsetting client orders ahead of other TPs' earlier orders. Information about your order is also visible to the broker's other desks.
- Iceberg minimum display is 10% of order size and a board-lot multiple (until the one-share lot arrives); do not model hidden quantity as free of queue-priority loss.
- No STP flag: your own algo must avoid trading against its own resting orders across child orders/accounts (wash-trade exposure under SRC s.24).
- Do not short-sell into the pre-open/pre-close auctions (rejected by the system).

---

## 2. Pre-open (opening) auction

### Takeaway
The opening price is set by a single-price call auction that runs from the 09:00 pre-open to a fixed 09:30:00 uncross, with free order entry/amendment/cancellation until 09:15 and entry-only from 09:15 to 09:30. The price is the tick-aligned level that maximises executed volume, with four published tie-breaks (minimum unmatched volume, market pressure, nearest to the reference price, then the reference price itself) and the previous close (or adjusted close) as reference; indicative price and volume are broadcast in real time on the ITCH Total View feed.

### Cited Findings
**Timeline and order-entry rules**
- `[P]` Whole-day and half-day schedule (current IG text, 2024): 09:00 Pre-Open - "No matching of Orders can occur, but Trading Participants (TPs) can enter, modify, or cancel Orders"; 09:15 Pre-Open No-Cancel - "TPs are allowed to enter Orders but cannot cancel or modify Orders"; 09:30 Opening - "Opening Price for all Securities is calculated. The Order book is frozen and Order entry, modification and cancellation by TPs are not allowed"; 09:30 Continuous Trading - "Orders are automatically matched at the Best Price".[^pse-approved-rules-vwap-trading-2024:5][^pse-approved-rules-vwap-trading-2024:6] The 2010 original added that pre-open orders "will be processed based on the pre-opening algorithm".[^pse-implementing-guidelines-trading-rules:4]
- `[P]` In the XTS engine the uncross is tied to the state change: ITCH event 'Q' ("Start of Market Hours. The Pre-Open uncross occurs, and continuous trading begins") follows 'S' (Pre-Open) and 'R' (Pre-Open No Cancellation).[^pse-itch-equities-feed-spec-v2-3:10] The exchange publishes a Trading Schedule message with each event's scheduled time in seconds after midnight.[^pse-itch-equities-feed-spec-v2-3:10][^pse-itch-equities-feed-spec-v2-3:11] `[I]` No randomised end or extension exists in any rule or the ITCH spec: the uncross time is deterministic (09:30:00).
- `[P]` Defined terms: "Pre-Open Period" = period when "Orders accepted and queued are considered in the determination of the Opening Price. Orders during this period will not trade until the market opens"; "Intervention-Before-Opening/Closing" = the latter phase of pre-open/pre-close "where Order modification or cancellation is not allowed".[^pse-revised-trading-rules:9][^pse-revised-trading-rules:10]
- `[P]` Permitted in the pre-open book: limit orders priced inside the static threshold, market orders (enterable "from Pre-Open to Market Open/Continuous Trading"), MOO orders (executable only at the indicative price; unmatched balance becomes a limit order at that price), FAK (executed "to the fullest extent possible at the end of Pre-Open", remainder eliminated), and iceberg quantity for non-FAK orders; minimum-quantity orders and Market-to-Limit are not allowed.[^pse-revised-trading-rules:21][^pse-revised-trading-rules:22][^pse-revised-trading-rules:23][^pse-implementing-guidelines-trading-rules:12] Crosses may not be entered in Pre-Open/Pre-Close;[^pse-revised-trading-rules:31] short sales are rejected;[^pse-short-selling-guidelines-2023-10:2] the odd-lot market has no pre-open.[^pse-implementing-guidelines-trading-rules:20]
- `[P]` Foreign buy orders are "earmarked" at entry against the available foreign-ownership room ("will limit the available volume for succeeding foreign buying Orders"), so pre-open foreign bids consume room even before they execute.[^pse-revised-trading-rules:17]
- `[P]` Block sales may be executed "from the Market Pre-Open to the Trading-at-Last/Run-Off period" (Dec 2011 amendment adds "including Market Recess"), and special block sales with a pre-determined execution date are executed during the Pre-Open of that date.[^pse-tpa-2011-0110-amended-revised-trading-rules:5][^pse-implementing-guidelines-trading-rules:25]

**Price-determination algorithm (RTR Art. IV s.10; IG VIII)**
- `[P]` RTR text: the system computes the Opening Price "based on its Reference Price and Orders posted during the Pre-Open Period ... a determination of all prices which have possible matching, and the volumes that could be matched at each of the prices", subject to: (a) the price with the maximum number of shares matched; (b) if tied, the price with "the least quantity unfilled or unmatched"; (c) if tied, "the price from the buy side (highest bid) or the price from the sell side (lowest offer), depending on where the Market Pressure is"; (d) if tied, "the price that is nearest to the Reference Price"; (e) if tied, "the Reference Price". "The same algorithm shall apply for Closing Price calculation with the LTP as the Reference Price."[^pse-revised-trading-rules:23][^pse-revised-trading-rules:24]
- `[P]` Definitions: "Market Pressure" applies "to the buy or sell side of a Security's order book, depending on the side that registers the higher volume or quantity".[^pse-revised-trading-rules:10] IG VIII: possible prices are all prices between the highest and lowest prices with probable matches (in the IG example the grid is every tick between the lowest offer 900 and highest bid 920; 870 and 925 are excluded); matched quantity at a price = min(buy volume, sell volume) with buy volume = all bids at or above the price and sell volume = all offers at or below it; unmatched quantity = the difference; buy-side pressure selects the highest remaining price, sell-side pressure the lowest; if pressure "cannot be determined because (1) volume for both the buy and sell side of all the possible Opening prices is equal or (2) ... counterbalanced", choose the price closest to the Reference Price; the Reference Price is chosen if it is among the remaining prices and nothing else decides.[^pse-implementing-guidelines-trading-rules:13][^pse-implementing-guidelines-trading-rules:14][^pse-implementing-guidelines-trading-rules:15][^pse-implementing-guidelines-trading-rules:16]
- `[P]` Reference Price for the open "shall be the Previous Closing Price or, when applicable, the Last Adjusted Closing Price"; RTR s.6 adds "the Last Traded Price or the last ACP in cases where there is no trading activity for the Security in the immediately preceding Trading Day".[^pse-implementing-guidelines-trading-rules:16][^pse-revised-trading-rules:20]
- `[P*]` Verification: I coded the five-step rule exactly as above (grid = every tick from the lowest limit offer to the highest limit bid; matched = min(buy,sell); unmatched = |buy-sell|; "pressure" = sign of buy-minus-sell, unanimous across the tied prices) and it reproduces all six IG worked examples (table below).

| IG example (tick 5) | Reference | Candidate prices (buy / sell vol -> matched) | Result | Deciding rule |
|---|---|---|---|---|
| 1 (bids 920x5,000; 905x50,000; 900x72,500; 870x5,030; offers 900x134,000; 905x1,000; 925x15,000) | 910 | 920,915,910: 5,000/135,000 -> 5,000; 905: 55,000/135,000 -> 55,000; 900: 127,500/134,000 -> 127,500 | **900** | max matched |
| 2 (bids 905x10,000; 900x7,000; 890x72,500; 870x5,030; offers 900x10,000; 905x1,000; 925x15,000) | 910 | 905: 10,000/11,000 -> 10,000 (1,000 unmatched); 900: 17,000/10,000 -> 10,000 (7,000 unmatched) | **905** | min unmatched |
| 3 (bids 915x40,000; 910x10,000; offers 905x40,000; 915x20,000) | 900 | 915: 40,000/60,000; 910: 50,000/40,000; 905: 50,000/40,000 (matched 40,000 each; unmatched 20,000/10,000/10,000) | **910** | market pressure (buy) -> highest of 910/905 |
| 4.1 (bids 910x10,000; 895x1,000; 890x72,500; offers 900x10,000; 925x16,000) | 890 | 910, 905, 900: 10,000/10,000 each | **900** | nearest to reference (no pressure) |
| 4.2 (bids 905x10,000; 900x1,000; offers 900x10,000; 905x1,000) | 890 | 905: 10,000/11,000; 900: 11,000/10,000 (pressure counterbalanced) | **900** | nearest to reference |
| 5 (bids 920x10,000; 900x1,000; offers 900x10,000; 920x1,000) | 915 | 920 and 900 eliminated by min-unmatched; 915, 910, 905 remain with equal volumes | **915** | reference price |

(Source for all six: IG VIII examples.[^pse-implementing-guidelines-trading-rules:13][^pse-implementing-guidelines-trading-rules:14][^pse-implementing-guidelines-trading-rules:15][^pse-implementing-guidelines-trading-rules:16] Non-crossing orders listed in the IG - bids 890x72,500 and 870x5,030, offer 925x15,000 - are omitted where they do not affect any candidate price; prices are in the IG's illustrative units with tick size 5.)

**Constructed closing-auction examples (my own, validated with the same code, tick 0.05).** (A) LTP/reference 40.00; bids 40.20x30,000, 40.10x20,000, 39.90x50,000; offers 40.00x25,000, 40.10x20,000, 40.30x40,000. Candidates 40.00-40.20: matched 25,000 / 25,000 / **45,000 at 40.10** / 30,000 / 30,000 -> closing price **40.10** (rule 1). Fills: 30,000 at the 40.20 bid and 15,000 of the 20,000 at the 40.10 bid; both offers (25,000 + 20,000) fill; 5,000 at 40.10 remain bid, so a 5,000 sell at 40.10 in the run-off would trade at the closing price. (B) LTP 40.10; bids 40.20x10,000, 39.90x5,000; offers 40.00x10,000, 40.30x7,000. Every price from 40.00 to 40.20 matches 10,000 with zero imbalance and no pressure -> nearest to the reference 40.10 -> closing price **40.10** (rule 4). `[P*]`/`[I]`

**Compact algorithm spec (pseudocode, equivalent to RTR s.10 / IG VIII)**
```
inputs: limit bids {price,qty}, limit offers {price,qty}, ref, tick   # ref = prior close/ACP (open) or LTP (close)
lo = min offer price; hi = max bid price; if no bids or no offers or lo > hi: no auction price
for p in lo, lo+tick, ..., hi:  B(p)=sum bid qty with price>=p ; S(p)=sum offer qty with price<=p
                               M(p)=min(B,S) ; U(p)=abs(B-S)
C = argmax M ; if |C|>1: C = argmin U within C
if |C|>1: pressure = sign(B-S) over C; if all > 0 -> price = max(C); if all < 0 -> price = min(C)
if still |C|>1: C = prices in C nearest to ref ; if |C|>1: price = ref
execute min(B,S) at price; allocate by priority: market > MOO/MOC > limit (higher bid / lower offer first, then time of entry)
```
`[I]` Market, MOO and MOC orders have no price, so they add to B and S at every candidate price; PSE does not publish how the candidate grid is built when one side has only market orders (see Gaps).

**Indicative price/volume dissemination and outputs**
- `[P]` ITCH Indicative Price/Quantity message [I] carries Theoretical Auction Quantity ("total quantity eligible to be matched at the current Theoretical Auction Price"), best bid, best offer, Theoretical Auction Price and Auction Type ('O' Opening Auction (Pre-open), 'I' Intra-day Auction (Halt), 'C' Closing Auction (Pre-close)); it is part of the Total View feed, not the Basic feed.[^pse-itch-equities-feed-spec-v2-3:17][^pse-itch-equities-feed-spec-v2-3:18][^pse-itch-equities-feed-spec-v2-3:22][^pse-itch-equities-feed-spec-v2-3:23] Throughout the pre-open the feed sends Add Order, Order Delete, Indicative Price/Quantity and Trading Action messages; auction fills are sent as one "Order Executed With Price" message per executed order, and the Trade message is not used for them.[^pse-itch-equities-feed-spec-v2-3:27][^pse-itch-equities-feed-spec-v2-3:28]
- `[P]` Reference price is published at start of day as an Add Order message with order number and quantity zero.[^pse-itch-equities-feed-spec-v2-3:27]
- `[P]` End-of-day price files define "Opening Price" as the "Price of the security at market open or Price at which the security was first traded for a given day".[^pse-quote-file-eod-spec-2014:1] `[I]` If the auction produces no price, the first continuous trade becomes the open.

**Reservation (the PSE's call-auction extension at the open)**
- `[P]` A security is reserved when (i) a market-on-opening order is posted but there is no indicative opening price, (ii) a market order is unfilled at the open, or (iii) the indicative opening price breaches the static threshold; orders other than crosses can still be posted, modified and cancelled during reservation.[^pse-revised-trading-rules:33][^pse-implementing-guidelines-trading-rules:26] The November 2014 XTS draft kept these triggers and added cancellation of MOO orders when no indicative price exists.[^pse-memo-revisions-trading-rules-consultation-2014:8][^pse-memo-revisions-trading-rules-consultation-2014:4]

### Inferences
- `[I]` Unmatched limit orders from the pre-open simply roll into the continuous book with their original priority (the rules say orders "queued in the Order book"; none describes re-timestamping at the open); MOO remainders become limit orders at the opening price.
- `[I]` The five-step rule is the same one used by the NSC platform in 2010; PSE's December 2025 NTE gap analysis names only the run-off period as a functional gap between Nasdaq Eqlipse and XTS, which suggests the auction uncross logic is expected to be equivalent on the NTE, but no document says so.[^pse-cn-2025-0046-board-lot-trading-at-last:5]
- `[I]` With a 15-minute no-cancel window and a fixed uncross time, the only informative actions in the last 15 minutes are additions; observing the indicative price moves is the only way to react (no cancels).

### Gaps
- How market/MOO volume feeds the candidate grid when only one side has limit orders; whether iceberg hidden quantity counts in the uncross; allocation when many orders share the uncross price (time priority is implied, pro-rata not mentioned).
- Whether and how non-subscribers (retail, data vendors) see the indicative price; PSE's public pages do not show it.
- Duration/exit procedure of an automatic "reservation" (Market Control action; only the 10-minute reservation after a suspension is specified).
- NTE equivalence of the auction logic (unconfirmed).

### Execution implications
- Pre-open is a 30-minute call with a hard 15-minute commitment: submit anything you may want to cancel before 09:15; between 09:15 and 09:30 you can only add.
- The rule maximises matched volume, so a large marketable limit order moves the opening price up the supply curve until matched volume stops rising; with equal matched/unmatched volume the "market pressure" step pushes the price toward the heavier side (buy-heavy -> highest tied price). Model it exactly with the algorithm above and test against the ITCH 'I' stream.
- Avoid MOO/market orders in thin names: no indicative price puts the stock into reservation and delays trading.[^pse-revised-trading-rules:33]
- Foreign buyers: pre-open bids earmark foreign-ownership room at entry; cancel before 09:15 if you will not use it.[^pse-revised-trading-rules:17]
- Short sales cannot join either auction (rejected), so short-covering/buy-back exposure can only be hedged in continuous trading.[^pse-short-selling-guidelines-2023-10:2]

---

## 3. Closing auction (Pre-Close), Run-Off/Trading-at-Last and the official close

### Takeaway
PSE's closing price is the output of a closing call auction ("Pre-Close"): 14:45-14:48 free entry/amendment, 14:48-14:50 entry-only, uncross at 14:50 using the same five-step rule as the open but with the last traded price as the reference. The 10-minute Run-Off/Trading-at-Last period that follows executes only at that closing price. The 15:00-15:15 Closing VWAP session trades at the day's VWAP and does not alter the close. The closing mechanism has existed since the 2010 trading-system launch; the pre-close was lengthened from 3 to 5 minutes on 4 Nov 2013, the whole-day schedule was reset on 6 Dec 2021, and an NTE rule change would let run-off orders execute at the closing price against better-priced passive orders. PSE publishes no explicit fallback if the auction does not cross.

### Cited Findings
**Definition and algorithm**
- `[P]` "Closing Price shall mean the price determined during the Pre-Close Period"; "Pre-Close Period" = "the period prior to the Run-Off/Trading-at-Last when Orders accepted and queued are considered in the determination of the Closing Price. Orders during this period will not be traded until the market transitions to Run-Off/Trading-at-Last"; "Run-Off Period/Trading-at-Last Period" = "the period after the Pre-Close when Orders are accepted and executed only at the Closing Price".[^pse-revised-trading-rules:8][^pse-revised-trading-rules:10][^pse-revised-trading-rules:11]
- `[P]` Algorithm: the s.10 five-step rule "shall apply for Closing Price calculation with the LTP as the Reference Price"; the IG repeats: "The Reference Price for calculating the Closing Price shall be the Last Traded Price of the Security."[^pse-revised-trading-rules:24][^pse-implementing-guidelines-trading-rules:16] The pre-close "is the same as Pre-Open. TPs can enter, modify or cancel Orders" and the pre-close no-cancel period allows entry only.[^pse-approved-rules-vwap-trading-2024:6]
- `[P]` Engine behaviour: ITCH 'L' (Pre-Close commences; entry Y, amend/cancel Y), 'J' (No Cancellation), then 'P' "Trading At Last. The Closing Auction uncross occurs, and traders can then enter limit orders for execution at the determined closing price." The close price is published as a Trade message with executed quantity and match number both zero, sent "immediately after the 'Trading At Last' System Event Message".[^pse-itch-equities-feed-spec-v2-3:10][^pse-itch-equities-feed-spec-v2-3:27] Indicative closing price/quantity are published as Indicative Price/Quantity messages with Auction Type 'C'.[^pse-itch-equities-feed-spec-v2-3:18]
- `[P]` Run-off rule (RTR Art. IV s.18, 2010 text, still the "current rule" in Dec 2025): "All Orders during the Run-Off/Trading-at-Last Period are executed only at the Closing Price. In cases where prices of posted Orders in the Order book are better than the Closing Price, no Orders will be accepted by the Trading System."[^pse-revised-trading-rules:27][^pse-cn-2025-0046-board-lot-trading-at-last:8] IG text: "TPs can enter Orders at the Closing Price only" (2024 wording); the 2010 and Nov 2013 wording allowed limit orders at the closing price "or Market Orders but matching is executed only at the Closing Price for both Order types", while the Dec 2011 wording said "Limit Orders at the Closing Price only".[^pse-approved-rules-vwap-trading-2024:6][^pse-implementing-guidelines-trading-rules:4][^pse-tpa-2013-0185-extended-pre-close:7][^pse-tpa-2011-0124-amended-implementing-guidelines:3] Crosses in run-off must be done at the closing price.[^pse-revised-trading-rules:31]
- `[P]` Official close and downstream use: the closing price is the next day's Reference Price (RTR s.6) and the starting point for corporate-action adjusted closing prices;[^pse-revised-trading-rules:20] PSE indices use "actual last traded prices" at a 15-second base frequency;[^pse-index-policy-2024:13] the EOD file defines Day Close as "Price of a security at market close. If there is no trade for the day, Day Close has no value."[^pse-quote-file-eod-spec-2014:1]
- `[P]` Closing VWAP session: SEC-approved VWAP Trading Rules (CN-2024-0010, 1 Feb 2024, "shall take effect immediately"; launched Fri 1 Mar 2024 per PSE/ASEAN Exchanges announcement) allow VWAP transactions only "within fifteen (15) minutes after the Run-off/Trading-at-Last Period", executed only at the VWAP computed by the Exchange, minimum value PhP 500,000, single-TP (one-firm) only, with "Block Sales, intentional cross and Odd Lot transactions" excluded from the VWAP computation; if the VWAP display is delayed the session is suspended and cancelled for the day if fewer than 5 minutes remain.[^pse-approved-rules-vwap-trading-2024:1][^pse-approved-rules-vwap-trading-2024:7] Launch date: PSE's announcement says it "will open Volume Weighted Average Price (VWAP) trading on Friday, March 1, 2024";[^pse-vwap-announcement-2024] `[S]` ASEAN Exchanges repeats this and the 3:00-3:15 p.m. window.[^aseanexchanges-vwap-2024]
- `[P*]` Usage: from PSE's 186 daily quotation reports of 2 Jan-2 Oct 2026, VWAP trades occurred on 67 days and totalled 0.12% of grand-total value (single day 2 Oct 2026: 3,750 shares, PHP 7.29m).[^pse-eod-daily-quotation-2026-10-02:11]

**Eligible securities and boards**
- `[P]` The auctions and run-off apply to the Normal Market board; the Odd Lot Market has "no Pre-Open, Pre-Close and Run-Off/Trading-at-Last Period".[^pse-implementing-guidelines-trading-rules:20] Dollar-denominated securities (DDS) are explicitly subject to the same calculation: "The Opening and Closing Price calculation in the Normal Market under Article IV, Section 10 of the Revised Trading Rules ... shall apply to DDS", with the same Reference Price and Trading Threshold rules, a USD tick/lot table and DDS-specific block minimums (section 5).[^pse-dds-rules:7][^pse-dds-rules:6]
- `[I]` ETFs, preferred shares, warrants, SME-board names and index-constituent stocks all trade on the same normal-board engine states (ITCH has only three groups: Normal, Oddlot, Index), so they share the pre-open, pre-close and run-off phases; I found no security-class exemption from the auctions. The "Index" group carries index values, not tradable orders.[^pse-itch-equities-feed-spec-v2-3:9]

**History of the closing mechanism (dated)**
| Date | Event | Source |
|---|---|---|
| 23 Dec 1997 | `[S]` PSE Circular 248-97 "Updated and Consolidated Trading Rules": the digest.ph preview shows a table of contents with articles on opening-price calculation, cross transactions, block sales/special block sales; the text (and the pre-2010 closing-price method) was not retrievable. | [^digest-ph-pse-circular-248-97] |
| 1 Jun 2010 / 26 Jul 2010 | SEC approves RTR (letter 1 Jun 2010); Pre-Close period introduced with the new trading system "PSE trade" at a 3-minute duration "given in consideration of the Exchange's half day trading"; rules effective with the NTS launch 26 Jul 2010. Half-day schedule: pre-close 11:57-11:59, no-cancel 11:59-12:00, run-off 12:00-12:10. | [^pse-revised-trading-rules:2][^pse-memo-extended-pre-close-consultation-2013:1][^pse-implementing-guidelines-trading-rules:4] |
| 13 Jul 2011 (Board) / 28 Jul 2011 | Board approves extended hours 09:00-15:30 in two phases (1 Oct 2011: 09:00-13:00; 1 Jan 2012: 09:00-12:00 and 13:30-15:30). | [^pse-memo-extended-trading-proposal-2011:1] |
| 25 Oct 2011 (SEC) / 7 Dec 2011 / 2 Jan 2012 | SEC-approved amendments take effect January 2012; whole-day schedule: pre-close 15:17, run-off 15:20, close 15:30 (pre-close 3 min: 15:17-15:19 auction, 15:19-15:20 no-cancel). IG run-off wording becomes "Limit Orders at the Closing Price only". | [^pse-tpa-2011-0110-amended-revised-trading-rules:1][^pse-tpa-2011-0110-amended-revised-trading-rules:3][^pse-memo-new-trading-hours-2011:1][^pse-tpa-2011-0124-amended-implementing-guidelines:2][^pse-tpa-2011-0124-amended-implementing-guidelines:3] |
| 10 Jul 2013 (Board) / 26 Sep 2013 (SEC) / 4 Nov 2013 | Pre-close lengthened from 3 to 5 minutes (15:15-15:18 auction, 15:18-15:20 no-cancel); run-off 15:20-15:30; wording again allows market orders in run-off. Reasons: PSE had "the shortest pre-close period in the region" (Bursa 5 min, SGX 6, SET 10, IDX 10, HoSE 15); to "allow the TPs to assess and counter a sharp price move at the close"; to give TPs more time because ETFs and index funds "are mostly benchmarked against the close price". | [^pse-memo-extended-pre-close-consultation-2013:1][^pse-memo-extended-pre-close-consultation-2013:2][^pse-tpa-2013-0185-extended-pre-close:10][^pse-tpa-2013-0185-extended-pre-close:9][^pse-tpa-2013-0185-extended-pre-close:7] |
| 22 Jun 2015 | Engine migration NSC -> PSEtrade XTS (Nasdaq X-stream); closing auction and trading-at-last states carried over (ITCH 'L','J','P'). | [^pse-psetrade-xts][^pse-itch-equities-feed-spec-v2-3:10] |
| 22 Nov 2021 -> 6 Dec 2021 | Current whole-day schedule: pre-close 14:45, no-cancel 14:48, run-off 14:50, close then 15:00. | [^pse-cn-2021-0059:1] |
| 1 Feb 2024 / 1 Mar 2024 | VWAP Trading Rules approved by SEC; Closing VWAP session 15:00-15:15 added after the run-off; market close becomes 15:15. | [^pse-approved-rules-vwap-trading-2024:1][^pse-approved-rules-vwap-trading-2024:3] |
| 15 Dec 2025 (proposal) | Draft: run-off orders accepted at the closing price even if better-priced passive orders exist ("Scenario 1/2"); status "For SEC approval" in Aug 2026; applies with the NTE. | [^pse-cn-2025-0046-board-lot-trading-at-last:6][^pse-cn-2025-0046-board-lot-trading-at-last:7][^pse-analyst-briefing-1h-2026:9] |
| 1 Jul 2026 (proposal) | Draft: Closing VWAP session becomes "Closing VWAP Negotiated Trades Session" (15:00-15:15; half-day 12:10-12:25). | [^pse-cn-2026-0031-negotiated-trades:6] |

**Proposed NTE run-off behaviour (draft)**
- `[P]` PSE and Nasdaq's gap analysis found that "PSEtrade XTS automatically rejects an incoming order during the Run-Off/Trading-at-Last period if the price of the counterpart passive order in the order book is better than the established Closing Price", whereas "With Nasdaq Eqlipse Trading, the incoming order will be accepted by the trading engine provided it is at the Closing Price, and the counterpart passive order will be matched with the incoming order at the Closing Price."[^pse-cn-2025-0046-board-lot-trading-at-last:5] Scenario 1: closing price 10.00, resting offer 9.00 x 2,000, incoming buy 2,000 @ 10.00 - today rejected; proposed: executes 2,000 @ 10.00 ("Seller will not be disadvantaged because it is able to sell at a higher price than its original offer"). Scenario 2 mirrors it for a resting bid at 11.00 and an incoming sell at 10.00 (executes at 10.00).[^pse-cn-2025-0046-board-lot-trading-at-last:6][^pse-cn-2025-0046-board-lot-trading-at-last:7]
- `[P]` Proposed s.18 text: "All Orders during the Run-Off/Trading-at-Last Period are can be entered, modified, and executed only at the Closing Price. In cases where prices of posted Orders in the Order book are better than the Closing Price, no Orders will be accepted by the Trading System." - the second sentence is carried over unchanged in the draft and contradicts the scenarios (drafting inconsistency in the consultation).[^pse-cn-2025-0046-board-lot-trading-at-last:8][^pse-nte-user-group-2026-01-15:11]

**Measures bearing on closing-price manipulation**
- `[P]` Law/regulation: "marking the close" ("Buying and selling securities at the close of the market in an effort to alter the closing price of the security") is listed prohibited conduct under SRC s.24 implementing rules, alongside wash sales and improper matched orders.[^sec-2015-src-irr:68][^ra-8799-src:24]
- `[P]` Structural features: the close is set by a call auction rather than the last trade; a no-cancel window (the last 2 minutes of pre-close); run-off executions only at the closing price; short sales barred in pre-close;[^pse-short-selling-guidelines-2023-10:2] orders that breach the dynamic threshold within 5 minutes before Pre-Close are rejected rather than reviewed.[^pse-implementing-guidelines-trading-rules:26]
- `[P]` One of the three stated reasons for lengthening the pre-close in 2013 was to "allow the TPs to assess and counter a sharp price move at the close" (the others: regional alignment and index/ETF benchmarking).[^pse-memo-extended-pre-close-consultation-2013:1][^pse-memo-extended-pre-close-consultation-2013:2] CMIC (operational March 2012) runs the Korea Exchange-built Total Market Surveillance system and investigates unusual price/volume movements.[^pse-investing-at-pse]

### Inferences
- `[I]` Fallback when no closing price is produced: the rule set contains no explicit statement. The closing algorithm's Reference Price is the LTP and the EOD spec leaves Day Close empty only when there was no trade at all, so the working assumption is Closing Price = the day's last traded price when the pre-close does not cross (and no close if there was no trade). Treat as unverified.
- `[I]` PSE's own run-off illustration in the NTE user-group deck shows a closing price of 10.00 equal to the day's only trade (13:30, 1,000 shares at 10.00) in a book with no crossing orders, consistent with a last-traded-price fallback; the CN-2025-0046 version of the same scenario shows that trade at 10.24, so the illustration is not reliable evidence.[^pse-nte-user-group-2026-01-15:12][^pse-cn-2025-0046-board-lot-trading-at-last:6]
- `[I]` Because the Run-Off executes at a price fixed 10 minutes earlier, the closing auction is the only venue where a trader can establish the official close; run-off flow cannot move it. For index-tracking benchmarks (ETFs, index funds) the closing auction is the capture point, consistent with PSE's 2013 rationale.
- `[I]` Under the draft NTE rule the passive side of a run-off trade can receive price improvement (a resting offer at 9.00 sells at 10.00) while the aggressor gets none; XTS today simply blocks the aggressor from trading at all when better-priced passive orders sit in the book.

### Gaps
- No public rule for the closing price when the auction does not cross (LTP vs previous close vs VWAP); no public statement whether block sales/intentional crosses update the LTP used as the closing reference (daily quotation reports show block prints do not enter the stock's OHLC - see section 5).
- Whether amend/cancel is possible in Trading-at-Last on XTS (ITCH says no, IG says cancel allowed).
- No published statistics on closing-auction volume share, no public enforcement cases for closing-price manipulation found within the research constraints.
- The closing-price method before the 2010 trading system (e.g. last trade or average) could not be established; the 1997 consolidated rules were not retrievable in full.
- Final approved NTE run-off text (draft retains a contradictory sentence).

### Execution implications
- To control the official close (index/ETF benchmark), participate in the 14:45-14:50 auction; orders added after 14:48 cannot be cancelled; use limit orders priced to guarantee participation because run-off cannot change the price.
- If better-priced passive orders are still in the book at 14:50 (for example an offer below the closing price), an incoming run-off order that would trade against them is rejected on XTS; under the draft NTE rule you could trade the residual at the closing price. Check the book state at 14:50 before relying on run-off liquidity.
- Closing VWAP session is a separate execution venue (>= PHP 500,000, single-firm) priced at the full-day VWAP excluding blocks/crosses/odd lots - use it for benchmark-VWAP mandates, not for the close.[^pse-approved-rules-vwap-trading-2024:7]
- Remember the half-day calendar (pre-close 11:57-11:59, run-off 12:00-12:10, VWAP 12:10-12:25, close 12:25).[^pse-approved-rules-vwap-trading-2024:3]

---

## 4. Intraday and volatility auctions (security-level states)

### Takeaway
PSE has no scheduled intraday auction and no price-triggered volatility auction. Its substitutes are (a) "freezing" of a security when an order would breach the dynamic/static threshold (Market Control validates or rejects, normally within 5 minutes), (b) "reservation" - a call-auction-style hold used when a market order cannot open the book, when the indicative opening price breaches the static threshold, and for 10 minutes before a suspended stock resumes, and (c) trading halts during which orders keep accumulating. The XTS engine models halts as an "Intra-day Auction". Threshold levels and circuit breakers are covered in the price-controls chapter.

### Cited Findings
- `[P]` Freezing: when an order would breach the Trading Threshold the security is frozen, "Orders cannot be posted, modified or cancelled", and Market Control acts "immediately or no later than five (5) minutes"; in-threshold intermediate fills of a partly matched order stand; orders at the BBO beyond the DT, and crosses beyond the DT, are auto-accepted; any order breaching the DT within the 5 minutes before Pre-Close is rejected automatically.[^pse-revised-trading-rules:33][^pse-implementing-guidelines-trading-rules:25][^pse-implementing-guidelines-trading-rules:26]
- `[P]` Reservation triggers: market-on-opening order with no indicative opening price; an unfilled market order at the open; indicative opening price breaching the static threshold. Orders other than crosses may be posted, modified and cancelled while reserved. A security also "shall undergo reservation prior to lifting a trading suspension".[^pse-revised-trading-rules:33][^pse-implementing-guidelines-trading-rules:26]
- `[P]` Halt/suspension matrix (IG): after an uncured halt/suspension "Trading will be suspended for fifty (50) minutes, and will be reserved ten (10) minutes thereafter", with "Trading to resume during Market Pre-Open Period of the corresponding day".[^pse-implementing-guidelines-trading-rules:28]
- `[P]` Trading halt = stoppage "not lasting longer than one Trading Day"; orders other than crosses can be posted, modified and cancelled during a halt; during a suspension orders cannot be posted/modified/cancelled and posted orders are purged; derivatives of the halted security (warrants, PDRs) are halted too.[^pse-implementing-guidelines-trading-rules:26][^pse-implementing-guidelines-trading-rules:27][^pse-revised-trading-rules:33][^pse-revised-trading-rules:34]
- `[P]` The Block Sale Market adopts the normal-market security states "other than freezing and reservation"; the odd-lot market is unaffected by normal-market freezing/reservation.[^pse-revised-trading-rules:32][^pse-revised-trading-rules:26]
- `[P]` XTS/ITCH state machine: Trading Action reasons 'S' suspended by market control, 'F' frozen "due to circuit breaker (dynamic limit)", 'H' "Halted (intraday auction)"; during a HALT the Indicative Price/Quantity message carries Auction Type 'I' ("Intra-day Auction (Halt)"), and lifting the halt returns the book to 'T'/'N'; "An Order Executed With Price message may also be sent for an order executed when thawing after a freeze".[^pse-itch-equities-feed-spec-v2-3:14][^pse-itch-equities-feed-spec-v2-3:18][^pse-itch-equities-feed-spec-v2-3:26][^pse-itch-equities-feed-spec-v2-3:28]
- `[P]` Market-wide halts and circuit breakers are Art. VIII of the base text; the Aug 2025 amendment changed the halt trigger to participants accounting for >50% of average daily trading value "(exclusive of block sales)" being unable to trade (see price-controls/halts chapter).[^pse-cn-2025-0037:1][^pse-cn-2025-0037:3]

- `[P]` Market-wide circuit breaker (CN-2020-0044, 29 Apr 2020, effective 4 May 2020): three levels (PSEi down at least 10%/15%/20% from the previous close) halt the whole market for 15/30/60 minutes, each level once per day, and a level "will not be triggered at a specific time prior to the pre-close" - the memo states the cut-offs for a pre-close starting 15:15 (14:55, 14:40, 14:10). It describes no reopening auction.[^pse-cn-2020-0044:1][^pse-cn-2020-0044:2]

### Inferences
- `[I]` The circuit-breaker cut-offs above are written for the old 15:15 pre-close; with the pre-close now at 14:45 the equivalent cut-offs would be 20, 35 and 65 minutes before it (14:25, 14:10, 13:40) if the same offsets apply, but I found no updated PSE statement (price-controls chapter should confirm).
- `[I]` In practice a halt in XTS behaves like an intraday call auction (orders accumulate, an indicative price is published with auction type 'I', and an uncross occurs on lift); the rules do not describe the uncross algorithm, so assume the same five-step rule as the open.
- `[I]` Because there is no volatility auction, large aggressive orders that would breach the DT do not "call" an auction: they freeze the book and wait for Market Control to confirm or reject the order by phone/within 5 minutes.

### Gaps
- Duration and exit mechanics of an automatic (non-suspension) reservation; whether the uncross after halt/reservation publishes indicative prices to the public feed.
- No evidence of any PSE rule for scheduled intraday auctions (none found).

### Execution implications
- During a freeze you cannot cancel resting orders; size child orders so that a sweep cannot breach the dynamic threshold relative to the LTP, or accept the 5-minute review risk.
- After a suspension the stock reopens only via pre-open with a 10-minute reserved call; expect an auction-style gap rather than continuous repricing.
- Do not rely on cross orders during halts/reservation (crosses are the one order type blocked).

---

## 5. Block sales (Block Sale Market) and "special block sales"

### Takeaway
Block sales are pre-arranged, exchange-reported trades executed outside the order book. A regular block needs at least PHP 20 million of value and a price within +/-5% of the previous close (LACP); a special block needs at least PHP 50 million, an underlying agreement and COO approval and is keyed in by Market Control, with no price band in the IG text. Both thresholds were still described as current by PSE on 1 Jul 2026. Block prints are reported separately (not in the stock's OHLC/volume/value) but are counted in headline turnover: in 2026 YTD they were 18.4% of headline value (median day 12.4%, peak 82% on 11 Sep 2026), so regular-market ADV is only about 81.5% of the headline figure.

### Cited Findings
**Eligibility, price and timing (IG XVIII, RTR Art. VI s.3)**
- `[P]` Definitions: Block Sale = "a pre-arranged transaction which is executed through the facilities of the Exchange and compliant with the requirements of the Implementing Guidelines"; Block Sale Market = "the market where all pre-arranged transactions meeting the requirements set by the Exchange are executed".[^pse-revised-trading-rules:8]
- `[P]` Regular block sale: value "no less than PhP20 million"; price "not more than five percent (5%) above or below the Last Adjusted Closing Price (LACP)"; prices not more than 4 decimals; volume may be non-multiples of the board lot; settlement "within the execution date (T+0)". Special block sale: value "no less than PhP50 million"; prices not more than 4 decimals; non-board-lot volume allowed; "The underlying agreement and other supporting documents shall be provided by the selling Trading Participant"; settlement on execution date unless the parties' agreement provides otherwise. No price band is listed for special blocks.[^pse-implementing-guidelines-trading-rules:23][^pse-implementing-guidelines-trading-rules:24]
- `[P]` PSE's own restatement on 1 Jul 2026: "For regular block sales, the minimum transaction value is PhP20 million and the execution price should not be more than five percent (5%) above or below the Reference Price (i.e. Previous Closing Price or Last Adjusted Closing Price in the event of corporate actions). Special block sales, on the other hand, must have a transaction value of at least PhP50 million."[^pse-cn-2026-0031-negotiated-trades:3] The base rule keys the band to "the previous Trading Day's Closing Price or the ACP in the event of corporate actions, or the last ACP in cases where there is no trading activity".[^pse-revised-trading-rules:31]
- `[P]` Participants and mechanics: one or two TPs but "different clients for the buying and the selling side"; in a two-TP block an unconfirmed declaration "shall be eliminated after the period set by the Exchange" (IG: 15 minutes from the declaration); settled under Clearing Agency rules; executable "from the Market Pre-Open to the Trading-at-Last/Run-Off period, including Market Recess" (Dec 2011 wording); same security states as the normal market except freezing and reservation.[^pse-revised-trading-rules:31][^pse-tpa-2011-0110-amended-revised-trading-rules:5][^pse-implementing-guidelines-trading-rules:25]
- `[P]` Approval and entry windows: the TP submits a block-sale application before execution; regular blocks may be executed "anytime during trading hours" provided the application was filed "before Run-Off Period" (original 2010 text: "no later than 12 noon"), the Exchange approves or disapproves within 30 minutes (prior approval of the MOD head), and the TP enters a trade declaration in the Trading Confirmation System (TCS) before Market Close with side, security, quantity, price, counterpart member code and client account ID; special blocks are approved within 2 working days with COO approval and "the PSE Market Control Department ... shall execute a special Block Sale in the Trading System"; execution must follow within 5 minutes of approval, otherwise (after-hours approval or a pre-determined execution date) the block is executed during the next Market Pre-Open; the trader value limit applies to TCS entries (Market Control can execute on the TP's behalf). RTR: "Requests for Block Sales shall be acted upon within two (2) Trading Days".[^pse-implementing-guidelines-trading-rules:24][^pse-implementing-guidelines-trading-rules:25][^pse-tpa-2011-0124-amended-implementing-guidelines:4][^pse-revised-trading-rules:32]
- `[P]` Reporting and disclosure: application form includes a certification that the facility is not used to circumvent the National Internal Revenue Code and "shall be filed ... within thirty (30) days of the closing date or execution date, whichever comes later" (IG items 2-3, as written); executing TPs report settlement promptly and, "No later than five (5) trading days from the execution date", disclose to MRD "the identity of all the clients who transacted on the Security from the time the Block Sale request was filed"; for a pre-determined execution date MOD publishes on the PSE website the security, number of shares, execution price, value and execution date.[^pse-implementing-guidelines-trading-rules:24][^pse-implementing-guidelines-trading-rules:25]
- `[P]` Order-book separation: pre-arranged trades that meet block requirements "shall be executed in the Block Sale Market and not through a Cross Order entry"; short sales are not accepted for block sales; block sales are excluded from the VWAP computation and from the halt-trigger trading-value base.[^pse-revised-trading-rules:31][^pse-short-selling-guidelines-2023-10:2][^pse-approved-rules-vwap-trading-2024:7][^pse-cn-2025-0037:3]
- `[P]` Protocol (XTS): FIX Trade Capture Report with TrdType 0 = Regular Block Sale, 1 = Special Block Sale (52/46 = trade with/without impact entered by Market Control); one-party reports need counterparty Accept/Decline and time out as "Defaulted"; a "Cross Block Sale" can be reported by one TP with both sides; news category 95 = BlockSale.[^pse-fix-specification-v2-5:35][^pse-fix-specification-v2-5:38][^pse-fix-specification-v2-5:40][^pse-fix-specification-v2-5:51]

**Dollar-denominated securities (DDS)**
- `[P]` DDS blocks use USD thresholds - "Five Hundred Thousand US dollars (USD500,000.00) for regular Block Sales" and "One Million US dollars (USD1,000,000.00) for special Block Sales" - and "All other conditions for Block Sales in the Revised Trading Rules, such as price limit and reportorial requirements, shall apply to DDS" (so the +/-5% band applies to regular DDS blocks); DDS orders are converted to pesos at the previous day's exchange rate for the per-order value limit; done-through DDS trades are allowed only among eligible brokers.[^pse-dds-rules:7] The daily report converts DDS odd-lot and block trades to pesos at the previous day's rate.[^pse-eod-daily-quotation-2024-05-24:12]

**How blocks actually price versus the reference close (2026 data)**
- `[P*]` Reference = the stock's most recent non-empty daily close before the block date (no corporate-action adjustment, so ex-date and split cases are noisy). Of 1,596 block prints with a reference, 98.0% priced within +/-5% of it, including **all 793 prints between PHP 20m and PHP 50m** (below the special-block minimum, so most likely regular blocks, although a special block can be split into smaller prints) - consistent with the regular-block band being binding. Among the 800 prints of PHP 50m or more, 96.2% were inside the band; the 32 outside-band prints are overwhelmingly deal-priced special blocks (e.g. FGEN 36.00 vs 26.90 reference, +33.8%, PHP 25.8bn on 11 Sep 2026; RRHI 48.30 vs 38.00, +27.1%; ATI tender-offer block 36.00 vs 29.00, +24.1%; DHI 1.7032 vs about 4.0-4.3, about -58 to -60%; PAL 1.33 vs 3.40) plus a few moderate breaches that may reflect un-adjusted references (SMPH 18.12 vs 19.58, -7.5%; AREIT 35.60 vs 38.50, -7.5%; RCR 7.40 vs 7.84, -5.6%; CREC 4.70 vs 4.95, -5.05%).
- `[P*]` Distribution of block price / reference close - 1 (all prints): median 0.00%, p25 -0.43%, p75 +0.35%, p5 -4.29%, p95 +1.33%, mean -0.50%; 57.8% of prints within +/-0.5% of the reference; by bucket: below -5%: 24; -5% to -4%: 62; -4% to -2%: 51; -2% to 0%: 605; 0 to +2%: 811; +2% to +4%: 27; +4% to +5%: 8; above +5%: 8. Many block prices carry four decimals (e.g. TEL 1,407.0316 and BDO 136.5562 on 24 May 2024), i.e. averaged/negotiated prices rather than book ticks.[^pse-eod-daily-quotation-2024-05-24:12]

**Publication and effect on price statistics**
- `[P]` Daily Quotation Report prints a block-sale list (security, price, volume, value) and states "Sectoral and Grand Total include Normal Market, Odd Lot, Block Sale and VWAP transactions".[^pse-eod-daily-quotation-2026-10-02:11][^pse-eod-daily-quotation-2026-10-02:12] ITCH publishes block trades through the Trade message with Trade Indicator 'B' (not through order-executed messages) and carries a "Printable" flag for whether an execution enters statistics.[^pse-itch-equities-feed-spec-v2-3:18][^pse-itch-equities-feed-spec-v2-3:28]
- `[P*]` Block prints do not enter the stock's own OHLC/volume/value row. Example, DQR 2 Oct 2026: CREC block of 100,000,000 shares at 4.85 (PHP 485.1m) while the regular row shows open/high/low/close 4.62 with volume 20,000; GTCAP blocks at 415.00 (1,639,980 and 1,420,390 shares) while the regular row shows range 417-426, close 419.8, volume 19,900.[^pse-eod-daily-quotation-2026-10-02:1][^pse-eod-daily-quotation-2026-10-02:3][^pse-eod-daily-quotation-2026-10-02:11] `[I]` Hence block sales neither set the last traded price/close of the regular market nor feed the index (PSE indices use last traded prices);[^pse-index-policy-2024:13] PSE does not state this in a rule.
- `[P]` Clearing-fund contributions are based on trade value "net of block sales and cross transactions of the same flag".[^sccp-clearing-house-rules-2018:33]

**Practice: special blocks are announced one day ahead (2026 examples)**
- `[P]` TPA-2026-0010 (6 Mar): SPM 29,925,960 shares at 2.70 = PHP 80,800,092, executed 10 Mar 2026 (the DQR shows two prints, 29,886,494 + 39,466 shares = the notice total, i.e. one block split into pieces; the smaller piece was only PHP 106,558).[^pse-tpa-2026-0010-block-sale-spm:1] TPA-2026-0012 (12 Mar): ATI 31,721,200 and 177,612,478 shares ("Tender Offer results") executed 13 Mar 2026, stated values PHP 1,141,963,200 and PHP 6,394,049,208 (= shares x 36.00; the notice's price column reads "3.60", an evident typo), followed by a trading suspension for the minimum-public-ownership breach.[^pse-tpa-2026-0012-block-sale-ati-tender-offer:1] TPA-2026-0023 (28 May): PAL 464,230,075 shares at 0.4305 = PHP 199,851,047 executed 29 May 2026.[^pse-tpa-2026-0023-block-sale-pal:1] `[P*]` The 3 sub-PHP-20m prints in the 2026 daily reports (PHP 99,688; 106,558; 202,484) are all pieces of such special blocks.

**Share of turnover (computed from PSE's daily quotation reports, 2 Jan-2 Oct 2026)**
- `[P*]` Headline value ("GRAND TOTAL") = normal + odd-lot + block + VWAP; my H1-2026 average of PHP 7.72bn/day equals PSE's published "Average Daily Value Traded Php 7.72 bn" for the same period, so the report total is PSE's headline figure.[^pse-infographic-2q26:1] Block sales were 16.5% of H1 value and 18.4% of the 186-day total (PHP 263.6bn of PHP 1,434.7bn); odd lot 0.013%; VWAP 0.124%; normal market about 81.5%. Every one of the 186 days had block sales; median daily block share 12.4% (p10 4.3%, p90 32.8%, max 82.2%).
| 2026 month | days | headline value (PHP bn) | block (PHP bn) | block share | median day | max day |
|---|---|---|---|---|---|---|
| Jan | 21 | 156.24 | 19.15 | 12.3% | 7.8% | 48.6% |
| Feb | 19 | 147.17 | 23.89 | 16.2% | 14.1% | 32.8% |
| Mar | 21 | 178.72 | 42.02 | 23.5% | 16.6% | 65.0% |
| Apr | 19 | 131.79 | 16.51 | 12.5% | 12.9% | 26.3% |
| May | 19 | 138.07 | 19.19 | 13.9% | 14.9% | 41.5% |
| Jun | 21 | 174.55 | 32.39 | 18.6% | 15.7% | 44.1% |
| Jul | 23 | 155.39 | 29.80 | 19.2% | 11.1% | 72.5% |
| Aug | 19 | 142.98 | 29.79 | 20.8% | 8.7% | 64.8% |
| Sep | 22 | 194.09 | 46.85 | 24.1% | 9.9% | 82.2% |
| Oct (1-2) | 2 | 15.73 | 4.00 | 25.4% | 25.2% | 32.1% |
- `[P*]` Print-level distribution (1,608 prints; parsed prints equal 98.5% of reported block value): median print PHP 50.0m; p10 PHP 23.5m; p25 30.8m; p75 103.7m; p90 281.5m; 799 prints between PHP 20m and 50m, 806 at or above PHP 50m (421 at or above PHP 100m; 84 at or above PHP 500m); prints at or above PHP 50m carry 90.1% of block value; median 9 prints on a block day. Largest: FGEN 715,855,362 shares at 36.00 = PHP 25.77bn on 11 Sep 2026, when block value of PHP 26.86bn was 82% of the day's PHP 32.70bn grand total.[^pse-eod-daily-quotation-2026-09-11:11][^pse-eod-daily-quotation-2026-09-11:12]
- `[P*]` Older samples: 24 May 2024 block value PHP 575.3m of PHP 4,468.3m grand total (12.9%);[^pse-eod-daily-quotation-2024-05-24:12][^pse-eod-daily-quotation-2024-05-24:13] 2 Oct 2026 PHP 2,625.7m of PHP 8,182.6m (32.1%).[^pse-eod-daily-quotation-2026-10-02:11][^pse-eod-daily-quotation-2026-10-02:12]

### Inferences
- `[I]` The IG lists no price band for special blocks although RTR Art. VI s.3(d) says block-sale prices are bounded by "a prescribed ratio" of the previous close; in practice special blocks (tender-offer settlements, MPO cures) appear to be priced at the agreed/tender price without the +/-5% test, but PSE approves them case by case.
- `[I]` Value thresholds apply per transaction/application, not per print: a special block can be split into several prints (SPM example), so a print below PHP 20m is not evidence of a rule breach.
- `[I]` A policy that routes "large trade near the market" to the block facility needs three tests in this order: value >= PHP 20m? price within +/-5% of the previous close/LACP? timing (application filed before the run-off)? If the price is outside the band the only block route is a special block (>= PHP 50m, documented agreement, COO approval, T+2 working days).

### Gaps
- Current settlement date for blocks (IG says T+0 for regular blocks; regular trades migrated from T+3 to T+2 with the SEC-approved go-live of 24 Aug 2023;[^sccp-memo-04-0823-t2-go-live:1] I found no block-specific amendment, so whether T+0 block settlement still applies is unverified).
- Whether block sales may be executed during the 15:00-15:15 Closing VWAP session; whether blocks are time-stamped into the ITCH feed in real time to all subscribers (the Trade message is on Total View only).
- Official PSE aggregate statistics for block-sale share (none located; shares above are my computation from 186 daily reports; reference-price analysis uses carried-forward closes without corporate-action adjustment).
- Approval criteria for special blocks beyond "underlying agreement and supporting documents".

### Execution implications
- Eligibility function for pre-arranged size: `shares_min = ceil(20,000,000 / price)`; band = [0.95, 1.05] x previous close (LACP-adjusted); outside the band you need a special block (>= PHP 50m with documents and COO approval; 2 working days).
- Block trades are not part of the tape that drives LTP/close/VWAP-session pricing, so executing size as a block removes it from benchmark-VWAP/close calculations but also from the free price-discovery pool: do not compute market-impact baselines from headline volumes that include blocks.
- For participation-rate algorithms use the regular-market ADV (roughly 81.5% of headline) and treat days with a >30% block share (20 of 186 days in 2026, 10.8%; >50% on 5 days) as non-representative. The simple mean of daily block shares is 15.3% (value-weighted 18.4%).
- Special blocks tied to tender offers are pre-announced about a day ahead with price, size and date (TPA notices): a source of event signals.
- Remember surveillance: executing TPs must name every client that traded the security between the block request and execution within 5 trading days.

---

## 6. Crosses, put-throughs, agency crosses, VWAP and (proposed) negotiated trades

### Takeaway
A PSE "cross" is a single-TP, simultaneous buy-and-sell entry in the normal market at an agreed quantity and price that must lie within the best bid and offer (at the closing price in the run-off, never in pre-open/pre-close) and may not be used for deals that qualify as block sales. Pre-arranged trades therefore route by size and price: block-eligible deals go to the Block Sale Market, smaller deals inside the BBO may be crossed, and today nothing exists for small deals priced outside the BBO - the gap the proposed Negotiated Trades facility (priced within +/-5% of the day's VWAP, one firm, in the 15-minute session after the run-off) is designed to fill. Client orders must take priority over a broker's own account under the SEC's "Customer First" rule. The PSE documents I searched never use the term "put-through": the equivalents are the Cross Order (within the spread) and the Block Sale (large, pre-arranged).

### Cited Findings
**Cross rules (RTR Art. VI ss.1-2, definitions)**
- `[P]` Definition: "Cross Transaction" = "a transaction where the same Broker executes buying and selling Orders of different clients or its proprietary account for different beneficial Owners for the same Security and at the same price and quantity."[^pse-revised-trading-rules:9] The Cross Order type: "buying and selling Orders of the same Trading Participant that are simultaneously executed at the agreed quantity and price within the BBO."[^pse-revised-trading-rules:22]
- `[P]` Requirements (Art. VI s.1): (a) "Its price shall be within the BBO"; (b) "In the absence of the BBO, the price shall observe the limitations set out in the Implementing Guidelines"; (c) "It shall not be entered during the Pre-Open/Pre-Close Period"; (d) "When done during the Run-Off/Trading-at-Last Period, it shall be at the Closing Price"; (e) "All pre-arranged transactions meeting the requirements set by the Exchange shall be executed in the Block Sale Market and not through a Cross Order entry."[^pse-revised-trading-rules:31] I found no IG text that sets the "limitations" referred to in (b).[^pse-implementing-guidelines-trading-rules:2]
- `[P]` PSE's restatement (1 Jul 2026): a pre-arranged transaction below the block minimums "cannot be executed in the Block Sale Market but may be entered as a cross transaction in the regular market, provided the execution price is within the best bid and offer"; "there is presently no execution facility for trades that do not meet the minimum value thresholds required for block sales, but likewise fail to satisfy the price constraints for cross transactions because the price is outside the BBO."[^pse-cn-2026-0031-negotiated-trades:3]
- `[P]` Engine mechanics (XTS FIX): crosses use the New Order Cross message with CrossType 1 (Cross AON), CrossPrioritization 0 (none), OrdType 2 (Limit) with a price, TimeInForce 3 (IOC) and the same quantity on both sides; each side carries its own executing trader/account.[^pse-fix-specification-v2-5:16][^pse-fix-specification-v2-5:17] ITCH tags intentional crosses with Trade Indicator 'C' ("the same user simultaneously entered both sides of the trade").[^pse-itch-equities-feed-spec-v2-3:18]
- `[P]` A cross that breaches the dynamic threshold is auto-accepted; crosses are the one order type not allowed while a security is reserved or halted; crosses are allowed in the Odd Lot Market on the same rules; automatic internal crossing of a TP's own orders has queue priority (section 1).[^pse-implementing-guidelines-trading-rules:26][^pse-implementing-guidelines-trading-rules:27][^pse-implementing-guidelines-trading-rules:20][^pse-revised-trading-rules:31]
- `[P]` Intentional crosses are excluded from the VWAP computation (VWAP session, proposed Negotiated Trades) and cross trades "of the same flag" are netted out of the SCCP clearing-fund contribution base.[^pse-approved-rules-vwap-trading-2024:7][^pse-cn-2026-0031-negotiated-trades:11][^sccp-clearing-house-rules-2018:33]
- `[P]` Client-before-proprietary: SEC IRR Rule 34.1 ("Customer First" Policy) - "The Dealer-Broker shall give priority to the orders of its customers over trades for its own account"; Rule 30.2.1.2.6.1.1 - orders of clients "shall have in all cases priority over orders for the account of the registered person"; aggregated orders must allocate to clients first when not all orders fill. PSE adds a Best Execution Rule ("reasonable diligence to ascertain the best available price ... as favorable as possible to the client") and separate trader IDs for client and proprietary accounts.[^sec-2015-src-irr:111][^sec-2015-src-irr:94][^pse-revised-trading-rules:29][^pse-implementing-guidelines-trading-rules:9]
- `[P]` Wash trading limits: transactions with "no change in the beneficial ownership" are unlawful manipulation (SRC s.24.1(a)(i); IRR 24.1.5.5 "wash sales").[^ra-8799-src:24][^sec-2015-src-irr:68] `[I]` This is consistent with the cross definition's requirement of "different beneficial Owners": a cross between accounts of the same beneficial owner would be a wash trade.

**Related pre-arranged/give-up facilities**
- `[P]` Done-Through: a Requesting TP may ask an Executing TP to execute orders for the Requesting TP's clients; the executing TP must use a "Special Account Institutional" (local or foreign by beneficial owner) and both TPs report client details to CMIC by 12:00 of T+1; amendments of done-through trades are prohibited (SEC-approved Dec 2013, effective by 2 Jan 2014).[^pse-tpa-2013-0200-done-through-transactions:1][^pse-tpa-2013-0200-done-through-transactions:7][^pse-tpa-2013-0200-done-through-transactions:11] Give-up/Take-up (assign an order to another TP for clearing and settlement) is allowed for client orders, not proprietary orders.[^pse-revised-trading-rules:27][^pse-revised-trading-rules:28]
- `[P]` VWAP trades (since 1 Mar 2024): single-TP, >= PHP 500,000, at the Exchange-computed VWAP, 15:00-15:15 (half-day 12:10-12:25); a two-firm version is reserved for later SEC approval.[^pse-approved-rules-vwap-trading-2024:2][^pse-approved-rules-vwap-trading-2024:7]
- `[P]` Proposed Negotiated Trades (CN-2026-0031, comments to 7 Jul 2026; status "Revising per Public Comments" on 17 Aug 2026): "a pre-arranged transaction executed at the agreed price"; no volume or value restriction; executed in a "Closing VWAP Negotiated Trades Session" 15:00-15:15 (half-day 12:10-12:25) "or within fifteen (15) minutes after the Run-off/Trading-at-Last Period"; price within +/-5% of that day's VWAP (VWAP over all trades from the opening to the closing period except block sales and intentional crosses; if no trade that day, +/-5% of the previous close/LACP); up to 4 decimals; one firm only; not for suspended/halted securities; included in end-of-day reports; session suspended/cancelled if the VWAP is delayed (same rule as VWAP trading).[^pse-cn-2026-0031-negotiated-trades:3][^pse-cn-2026-0031-negotiated-trades:4][^pse-cn-2026-0031-negotiated-trades:7][^pse-cn-2026-0031-negotiated-trades:11][^pse-analyst-briefing-1h-2026:9] NTE FAQ: executed on a web-based platform "similar to the VWAP facility"; "Negotiated Trades will not replace the current Block Sale"; counted in the day's total trading value "(subject to further confirmation)", in the CTF/EOD files and disseminated on the market-data feed as news/announcements.[^pse-nte-faq-2026-08:1][^pse-nte-faq-2026-08:2][^pse-nte-faq-2026-08:3] Broker-forum slide: "Only 1-firm trades shall be allowed."[^pse-nte-broker-forum-2026-07-09:8]

### Inferences
- `[I]` Routing logic for a pre-arranged trade today: (1) value >= PHP 20m and price within +/-5% of the previous close -> must be a regular block sale (cross prohibited); (2) value >= PHP 50m, price outside the band, documented agreement -> special block; (3) value < PHP 20m and price inside the BBO during continuous trading (or at the closing price in run-off) -> cross order; (4) anything else has no on-exchange route until Negotiated Trades are approved (alternatives: VWAP session for benchmark-priced trades >= PHP 500k).
- `[I]` Whether "within the BBO" includes the BBO prices themselves is not stated; the 2026 PSE wording ("within the best bid and offer") and the FIX AON/IOC design suggest inclusive bounds with execution against existing orders at the touch not guaranteed. Test in UAT before building policies that depend on trading at the touch.
- `[I]` The "different beneficial owners" requirement plus Customer First means a broker cannot cross a client against its own principal book without explicit best-execution/priority justification; for an agency cross between two clients, price must still sit inside the public spread, so the price improvement is shared, not captured by the broker.

### Gaps
- IG "limitations" when no BBO exists (RTR s.1(b)); inclusivity of the BBO test; whether a cross can print at the touch while resting orders exist at that price (queue-jumping).
- Final approved text of Negotiated Trades and whether it will coexist with the VWAP session on the NTE.
- Treatment of agency-cross consent/disclosure (no PSE-specific rule found beyond SRC Customer First and Best Execution).

### Execution implications
- Build the routing function above and log which leg of the test failed (value, band, BBO, session): eligibility is rule-driven (e.g., a cross is not allowed in pre-open/pre-close), so a rejected or mis-routed pre-arranged trade should be explainable from the log.
- A natural block that sits within 5% but below PHP 20m must be crossed inside the spread: if the spread is one tick there is no price room; consider splitting across days or using the VWAP session.
- Do not cross against accounts with the same beneficial owner (wash-sale exposure); keep the client/proprietary trader segregation intact.
- Crosses are blocked during halts/reservation and rejected in the auctions, so schedule them for continuous trading (09:30-14:45 session minus recess).

---

## 7. Odd lots (separate book; abolished on the NTE)

### Takeaway
Under XTS, orders smaller than the board lot trade in a separate Odd Lot Market with its own book (symbol prefix "O", FIX board code 'O'): continuous trading only, no auctions or run-off, limit and market orders only, partial fills allowed, no dynamic threshold, with the Normal Market's adjusted close as the day's reference price. It carries negligible value (about 0.013% of headline turnover in 2026) and disappears when the one-share lot takes effect with the NTE.

### Cited Findings
- `[P]` RTR s.17: odd-lot orders are orders "with quantity less than the defined Board Lot", executed in the Odd Lot Market, open only during Market Open/Continuous Trading, partial matching allowed, unaffected by normal-market freezing and reservation, with penalties for abuse.[^pse-revised-trading-rules:26]
- `[P]` IG XIV: "O" prefix appended to the symbol; order types Limit and Market only; validity Day, Good-Till-Week, Good-Till-Date, Good-Till-Cancelled, Sliding; cross transactions allowed on the same rules; modification rules as in the Normal Market; "There is no Pre-Open, Pre-Close and Run-Off/Trading-at-Last Period in the Odd Lot Market"; start-of-day reference price for both markets is the Normal Market's LACP; the odd-lot closing price is the last traded price during continuous trading or, when applicable, the LACP; "There is no Dynamic Threshold in the Odd Lot Market"; no reservation before lifting a suspension; TPs set their own charges; the market may be used "strictly for the purpose of trading Odd Lot Orders" (using it to execute a normal-market transaction is a violation).[^pse-implementing-guidelines-trading-rules:19][^pse-implementing-guidelines-trading-rules:20]
- `[P]` DDS "can be traded in the Odd Lot Market".[^pse-dds-rules:7]
- `[P]` Engine: the FIX Instrument block uses SecuritySubType 'N' (normal board), 'O' (odd-lot board), 'I' (index board); ITCH groups orderbooks as Normal/Oddlot/Index.[^pse-fix-specification-v2-5:47][^pse-itch-equities-feed-spec-v2-3:9] Short-sell orders are not accepted in the Odd Lot Market; odd-lot trades are excluded from the VWAP computation.[^pse-short-selling-guidelines-2023-10:2][^pse-approved-rules-vwap-trading-2024:7]
- `[P*]` Size of the market: DQR odd-lot totals - 24 May 2024: 761,654 shares, PHP 285,701.91;[^pse-eod-daily-quotation-2024-05-24:12] 2 Oct 2026: 3,183,528 shares, PHP 816,741.51;[^pse-eod-daily-quotation-2026-10-02:11] 2026 YTD (186 days) odd-lot value = 0.013% of headline value.
- `[P]` Abolition: with a one-share standard lot "PSE will no longer operate an Odd Lot Market. All orders will be matched on the normal market in the new trading engine"; FAQ: "with the standard lot size set at 1, the Odd Lot Market will no longer be available in the New Trading Engine"; TPs may impose their own minimum order value subject to the commission cap.[^pse-cn-2025-0046-board-lot-trading-at-last:5][^pse-nte-faq-2026-08:1][^pse-nte-user-group-2026-01-15:9]

### Inferences
- `[I]` The odd-lot book is an independent price-time book; nothing in the rules links its prices to the normal-market BBO, so odd-lot prices can sit away from the board and carry no best-price protection.
- `[I]` Because odd lots never enter an auction, residual odd lots from an auction fill (when board lots exceed 1) can only be worked in continuous trading.

### Gaps
- Tick table used by the odd-lot book (assumed the same as the normal board); priority rules inside the book (assumed price-time).
- Reporting of odd-lot trades to index/last-price calculations (separate from the regular LTP per DQR layout).

### Execution implications
- Until 23 Nov 2026 treat odd lots as a separate, thin venue for residuals only; never include them in auction logic or VWAP-benchmark computations.
- After the NTE go-live (if the one-share lot is approved) remove all odd-lot sweeps and board-lot rounding; lot-size logic becomes 1, but broker-imposed minimum order values may still apply.

---

## 8. Order-book transparency (brief; detailed dissemination is another chapter)

### Takeaway
XTS publishes a full order-by-order book on the ITCH "Total View" feed (price/size per order, no broker ID on resting orders) and a top-of-book "Basic" feed; broker IDs are attached to executions/trades unless "Broker Anonymity" is switched on, which PSE said in 2014 it would implement later (current status unknown). Indicative auction price and quantity are broadcast during pre-open, pre-close and halts; block, cross and manual trades carry type flags.

### Cited Findings
- `[P]` ITCH Total View carries Add Order, Order Executed (with/without broker ID), Executed With Price, Order Delete/Replace, Indicative Price/Quantity, Trade and Broken Trade messages; ITCH Basic carries BBO quotations and trades; ITCH does not publish running high/low/last statistics (subscribers derive them).[^pse-itch-equities-feed-spec-v2-3:22][^pse-itch-equities-feed-spec-v2-3:23][^pse-itch-equities-feed-spec-v2-3:32] PSE declined to offer five-level BBO because "the standard for ITCH Basic is that only top of book is published".[^pse-fix-itch-session-week01-2014-10-03:10]
- `[P]` The Add Order message has no participant field; broker identifiers appear only in executed/trade messages ('e', 'c', 'p': passive/active or buy/sell Broker ID) and only when the market does not run Broker Anonymity, "as announced by the exchange".[^pse-itch-equities-feed-spec-v2-3:14][^pse-itch-equities-feed-spec-v2-3:15][^pse-itch-equities-feed-spec-v2-3:19][^pse-itch-equities-feed-spec-v2-3:25] In Oct 2014 PSE said: "We will implement broker anonymity but not on Go-Live", with both message sets in the spec so the switch needs no software release.[^pse-fix-itch-session-week01-2014-10-03:11]
- `[P]` Auction transparency: Indicative Price/Quantity messages with auction types 'O', 'C', 'I' (section 2); trade flags ' ' regular, 'C' intentional cross, 'B' block sale, 'M' manual (market control).[^pse-itch-equities-feed-spec-v2-3:18]
- `[P]` NTE: ITCH and MDF protocols each with dedicated SoupBinTCP connections; cross trades identified by a Cross Indicator field in the Order Executed With Price and Trade messages; Negotiated Trades disseminated as news/announcements.[^pse-nte-faq-2026-08:3]

### Inferences
- `[I]` Depth is order-by-order but anonymous at order level, so queue position can be inferred from order numbers and timestamps, while counterparty identity is visible only post-trade (if anonymity is off).

### Gaps
- Whether Broker Anonymity has been enforced since 2015 (not found); what retail/vendor products display; NTE message differences (specs not public).

### Execution implications
- Reconstruct the book from Total View (order-level) to estimate queue position; use executed-trade broker IDs, when present, to profile your own broker's footprint before choosing slicing across brokers.
- Subscribe to the Indicative Price/Quantity stream for pre-open/pre-close decision-making; ITCH Basic is not sufficient for auction logic.

---

## Source catalog

```yaml
- slug: pse-revised-trading-rules
  title: "PSE Revised Trading Rules (SEC-approved 1 Jun 2010; PSE memo TPA 2010-0275, 8 Jun 2010)"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: https://documents.pse.com.ph/wp-content/uploads/sites/15/2021/04/Revised-Trading-Rules.pdf
  local_path: pdfs/pse-revised-trading-rules.pdf
  edition: in-force
  amended_through: "2010-06-08"
  note: "Scanned (image-only) base text still hosted by PSE as the Revised Trading Rules; later amendments are separate documents (2011, 2013, 2020, 2024, 2025). Page cites are physical pages; OCR used by me."
- slug: pse-implementing-guidelines-trading-rules
  title: "Implementing Guidelines of the Revised Trading Rules (PSE memo 2010-0340, effective 26 Jul 2010)"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: https://documents.pse.com.ph/wp-content/uploads/sites/15/2021/04/Implementing-Guidelines-of-the-Revised-Trading-Rules.pdf
  local_path: pdfs/pse-implementing-guidelines-trading-rules.pdf
  edition: in-force
  amended_through: "2010-07-22"
  note: "Base IG; trading hours, block-sale application timing and other parts were later amended (TPA 2011-0124, 2013-0185, CN-2024-0010, CN-2025-0037). Contains the opening/closing price algorithm and worked examples (pp.12-16)."
- slug: pse-tpa-2011-0110-amended-revised-trading-rules
  title: "SEC-approved amendments to the Revised Trading Rules (TPA 2011-0110)"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: https://documents.pse.com.ph/wp-content/uploads/sites/15/2024/08/1_Amended-Revised-Trading-Rules_TPA_2011-0110.pdf
  local_path: pdfs/pse-tpa-2011-0110-amended-revised-trading-rules.pdf
  edition: in-force
  amended_through: "2011-12-07"
  note: "Scanned. Art. II hours (superseded by later schedules), Art. IV ss.13-14, Art. VI s.3 block sales (still the latest block-sale article text), Art. VIII. SEC letter 25 Oct 2011 on p.2."
- slug: pse-tpa-2011-0124-amended-implementing-guidelines
  title: "Amended sections of the Implementing Guidelines (TPA 2011-0124)"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: https://documents.pse.com.ph/wp-content/uploads/sites/15/2024/08/2_Amended-IRR_TPA_2011-0124.pdf
  local_path: pdfs/pse-tpa-2011-0124-amended-implementing-guidelines.pdf
  edition: in-force
  amended_through: "2011-12-28"
  note: "New hours effective 2 Jan 2012 (superseded), order cancel/modify wording, XVIII.4 block-sale application 'before Run-Off Period', market-halt extensions."
- slug: pse-tpa-2013-0185-extended-pre-close
  title: "Approved amendment regarding the Extended Pre-Close Period (TPA 2013-0185, with TPA 2013-0167 and 2013-0165)"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: https://documents.pse.com.ph/wp-content/uploads/sites/15/2024/08/4_Extended-Pre-Close_TPA_2013-0185.pdf
  local_path: pdfs/pse-tpa-2013-0185-extended-pre-close.pdf
  edition: superseded
  amended_through: "2013-11-14"
  note: "Scanned. Pre-close 3 -> 5 minutes effective 4 Nov 2013 (SEC letters 26 Sep and 29 Oct 2013). Clock times superseded by CN-2021-0059; 5-minute structure and run-off wording lineage retained."
- slug: pse-memo-extended-pre-close-consultation-2013
  title: "For public comments: Extended Pre-Close Period (TPA 2013-0107)"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: "not recorded (PSE announcement archive; archived by another researcher)"
  local_path: pdfs/pse-memo-extended-pre-close-consultation-2013.pdf
  edition: historical
  amended_through: "2013-07-17"
  note: "Gives origin of the pre-close (June 2010, 3 minutes) and the 2013 rationale and regional peer table."
- slug: pse-memo-extended-trading-proposal-2011
  title: "Proposed amendment of trading rules in relation to extended trading (TPA 2011-0030)"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: "not recorded (PSE announcement archive; archived by another researcher)"
  local_path: pdfs/pse-memo-extended-trading-proposal-2011.pdf
  edition: historical
  amended_through: "2011-07-28"
  note: "Two-phase extension of trading hours (1 Oct 2011 and 1 Jan 2012)."
- slug: pse-memo-new-trading-hours-2011
  title: "PSE new trading hours (TPA 2011-0108)"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: "not recorded (PSE announcement archive; archived by another researcher)"
  local_path: pdfs/pse-memo-new-trading-hours-2011.pdf
  edition: historical
  amended_through: "2011-12-06"
  note: "Schedule effective 2 Jan 2012: pre-close 15:17, run-off 15:20, close 15:30."
- slug: pse-memo-revisions-trading-rules-consultation-2014
  title: "For public comments: Revisions in the PSE Trading Rules for PSE trade XTS (TPA 2014-0133)"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: "not recorded (PSE announcement archive; archived by another researcher)"
  local_path: pdfs/pse-memo-revisions-trading-rules-consultation-2014.pdf
  edition: historical
  amended_through: "2014-11-03"
  note: "Consultation draft only; the SEC-approved final text was not found."
- slug: pse-tpa-2013-0200-done-through-transactions
  title: "Account codes and Done-Through transactions (TPA 2013-0200)"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: https://documents.pse.com.ph/wp-content/uploads/sites/15/2024/08/5_MOD_Done-Through-Transactions_TPA_2013-0200.pdf
  local_path: pdfs/pse-tpa-2013-0200-done-through-transactions.pdf
  edition: in-force
  amended_through: "2013-12-13"
  note: "Scanned fax-quality copy; also reproduces Art. I definitions as amended in 2013."
- slug: pse-approved-rules-vwap-trading-2024
  title: "Approved Rules on VWAP Trading (CN-2024-0010)"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: https://documents.pse.com.ph/wp-content/uploads/sites/15/2024/05/Approved-Rules-on-VWAP-Trading.pdf
  local_path: pdfs/pse-approved-rules-vwap-trading-2024.pdf
  edition: in-force
  amended_through: "2024-02-01"
  note: "Scanned. SEC-approved, effective immediately; current IG trading-hours text; launch 1 Mar 2024 per ASEAN Exchanges/PSE."
- slug: pse-cn-2020-0044
  title: "Amendment of Circuit Breaker Rules (CN-2020-0044)"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: https://documents.pse.com.ph/CircularOPSPDF/CN-2020-0044.pdf
  local_path: pdfs/pse-cn-2020-0044.pdf
  edition: in-force
  amended_through: "2020-04-29"
  note: "Three-level market-wide circuit breaker effective 4 May 2020; cut-offs stated against a 15:15 pre-close; owned by the price-controls researcher."
- slug: pse-cn-2021-0059
  title: "Adjustments in trading hours (CN-2021-0059)"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: https://documents.pse.com.ph/CircularOPSPDF/CN-2021-0059.pdf
  local_path: pdfs/pse-cn-2021-0059.pdf
  edition: in-force
  amended_through: "2021-11-22"
  note: "Whole-day schedule effective 6 Dec 2021 until further notice."
- slug: pse-cn-2025-0037
  title: "Amendments to the Revised Trading Rules (market halt), Correspondent TP and Natural Disasters guidelines (CN-2025-0037)"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: https://documents.pse.com.ph/CircularOPSPDF/CN-2025-0037.pdf
  local_path: pdfs/pse-cn-2025-0037.pdf
  edition: in-force
  amended_through: "2025-08-20"
  note: "SEC-approved; halt trigger excludes block sales from the trading-value base; shows Art. VIII numbering still in use."
- slug: pse-cn-2025-0046-board-lot-trading-at-last
  title: "Proposed amendments to the PSE board lot and rule on trading during Run-Off/Trading-at-Last (CN-2025-0046)"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: https://documents.pse.com.ph/CircularOPSPDF/CN-2025-0046.pdf
  local_path: pdfs/pse-cn-2025-0046-board-lot-trading-at-last.pdf
  edition: n/a
  amended_through: "2025-12-15"
  note: "Consultation paper (comments to 31 Dec 2025); 'For SEC approval' per PSE 17 Aug 2026; applies with the Nasdaq Eqlipse NTE."
- slug: pse-cn-2026-0031-negotiated-trades
  title: "Proposed Rules on Negotiated Trades (CN-2026-0031)"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: https://documents.pse.com.ph/CircularOPSPDF/CN-2026-0031.pdf
  local_path: pdfs/pse-cn-2026-0031-negotiated-trades.pdf
  edition: n/a
  amended_through: "2026-07-01"
  note: "Consultation paper (comments to 7 Jul 2026); restates current block-sale and cross thresholds."
- slug: pse-nte-user-group-2026-01-15
  title: "New Trading Engine, PSETradeX, PSE Back-office Updates - Broker Forum (15 Jan 2026)"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: https://documents.pse.com.ph/wp-content/uploads/sites/15/2026/07/NTE-User-Group.pdf
  local_path: pdfs/pse-nte-user-group-2026-01-15.pdf
  edition: in-force
  amended_through: "2026-01-15"
  note: "Deck date per PSE NTE page; one-lot-one-share tables and run-off scenarios; also served at .../2026/06/NTE-User-Group.pdf."
- slug: pse-nte-broker-forum-2026-07-09
  title: "New Trading Engine, PSETradeX, Back-office - Broker Forum (9 Jul 2026)"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: https://documents.pse.com.ph/wp-content/uploads/sites/15/2026/07/PSE-New-Trading-Engine-TradeX-Back-office_Broker-Forum_07092026-1.pdf
  local_path: pdfs/pse-nte-broker-forum-2026-07-09.pdf
  edition: in-force
  amended_through: "2026-07-09"
  note: "Go-live 23 Nov 2026 schedule; negotiated-trade salient features."
- slug: pse-nte-faq-2026-08
  title: "Frequently Asked Questions - New Trading Engine"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: https://documents.pse.com.ph/wp-content/uploads/sites/15/2026/08/Frequent-Asked-Questions.pdf
  local_path: pdfs/pse-nte-faq-2026-08.pdf
  edition: in-force
  amended_through: undated
  note: "Undated; posted under the 2026/08 upload path; refers to events after 3 Aug 2026."
- slug: pse-analyst-briefing-1h-2026
  title: "PSE STAR - 1H 2026 analysts' briefing"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: https://documents.pse.com.ph/wp-content/uploads/sites/4/2026/08/2026.08.17-PSE-STAR-1H-2026.pdf
  local_path: pdfs/pse-analyst-briefing-1h-2026.pdf
  edition: in-force
  amended_through: "2026-08-17"
  note: "Slide 9 gives status of rule amendments (One Share One Lot: for SEC approval; Negotiated Trades: revising per public comments)."
- slug: pse-17c-2025-05-22-nasdaq-eqlipse-contract
  title: "PSE SEC Form 17-C: contract signing with Nasdaq (Eqlipse Trading), disclosure C03654-2025"
  publisher: The Philippine Stock Exchange, Inc. / SEC
  type: pdf
  canonical_url: "https://edge.pse.com.ph/ (disclosure C03654-2025)"
  local_path: pdfs/pse-17c-2025-05-22-nasdaq-eqlipse-contract.pdf
  edition: n/a
  amended_through: "2025-05-22"
  note: "Contract signing date for the new trading engine."
- slug: pse-fix-specification-v2-5
  title: "PSE FIX Specification for X-stream, version 2.5 (10 Aug 2015)"
  publisher: OMX Technology AB / PSE
  type: pdf
  canonical_url: https://documents.pse.com.ph/wp-content/uploads/sites/15/2021/01/PSE_FIX_Specification_v2_5-10-August-2015.pdf
  local_path: pdfs/pse-fix-specification-v2-5.pdf
  edition: in-force
  amended_through: "2015-08-10"
  note: "XTS order-entry/trade-capture spec; superseded by the NTE FIX spec (v1.1, June 2026, not public) at go-live."
- slug: pse-itch-equities-feed-spec-v2-3
  title: "PSE Equities Feed (ITCH) Specification for X-stream, version 2.3 (5 Oct 2018)"
  publisher: OMX Technology AB / PSE
  type: pdf
  canonical_url: https://documents.pse.com.ph/wp-content/uploads/sites/15/2024/03/PSE_Equities_Feed_Specification_v2.3.pdf
  local_path: pdfs/pse-itch-equities-feed-spec-v2-3.pdf
  edition: in-force
  amended_through: "2018-10-05"
  note: "System events, indicative price/quantity, trade flags, broker anonymity; superseded by NTE ITCH/MDF v1.2 (July 2026, not public) at go-live."
- slug: pse-fix-itch-session-week01-2014-10-03
  title: "FIX/ITCH user group session, week 1 (3 Oct 2014)"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: https://www.pse.com.ph/psetrade-xts/
  local_path: pdfs/pse-fix-itch-session-week01-2014-10-03.pdf
  edition: historical
  amended_through: "2014-10-03"
  note: "Linked from the PSEtrade XTS page (Fix Gateway - User Group Forum Presentation); exact file URL not recorded."
- slug: pse-short-selling-guidelines-2023-10
  title: "PSE Guidelines on Short Selling Transactions (as of October 2023, v3)"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: https://documents.pse.com.ph/wp-content/uploads/sites/15/2024/05/PSE-Guidelines-on-Short-Selling-Transactions_Oct2023_v3.pdf
  local_path: pdfs/pse-short-selling-guidelines-2023-10.pdf
  edition: in-force
  amended_through: "2023-10-16"
  note: "Short-sell orders rejected in Pre-Open/Pre-Close, odd lot and block sales. A byte-identical duplicate exists as pse-short-selling-guidelines-2023-10-v3."
- slug: sec-2015-src-irr
  title: "2015 Implementing Rules and Regulations of the Securities Regulation Code"
  publisher: Securities and Exchange Commission (Philippines)
  type: pdf
  canonical_url: "not recorded (SEC; archived by another researcher)"
  local_path: pdfs/sec-2015-src-irr.pdf
  edition: in-force
  amended_through: undated
  note: "Rule 24.1.5 (marking the close, wash sales), Rule 34.1 Customer First, Rule 30.2.1.2.6.1."
- slug: ra-8799-src
  title: "Republic Act No. 8799, The Securities Regulation Code"
  publisher: Republic of the Philippines
  type: pdf
  canonical_url: "not recorded (archived by another researcher)"
  local_path: pdfs/ra-8799-src.pdf
  edition: in-force
  amended_through: undated
  note: "Section 24.1 manipulation of security prices (wash sales, matched orders)."
- slug: pse-quote-file-eod-spec-2014
  title: "End of Day Price File (Quote File) File Specifications v2.0 (as of 4 Nov 2014)"
  publisher: The Philippine Stock Exchange, Inc., Market Operations Division
  type: pdf
  canonical_url: https://documents.pse.com.ph/wp-content/uploads/sites/15/2021/01/Quote-File-for-End-of-Dat-Security-Prices-updated-as-of-November-04-2014.pdf
  local_path: pdfs/pse-quote-file-eod-spec-2014.pdf
  edition: in-force
  amended_through: "2014-11-04"
  note: "Definitions of Opening Price and Day Close."
- slug: pse-index-policy-2024
  title: "Policy on Index Management (2024 version)"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: https://documents.pse.com.ph/wp-content/uploads/sites/15/2024/01/Policy-on-Index-Management-ver-2024.pdf
  local_path: pdfs/pse-index-policy-2024.pdf
  edition: superseded
  amended_through: undated
  note: "Indices use actual last traded prices; PSE announced a revised index-management policy on 21 Jul 2026 (CN-2026-0033), not reviewed here."
- slug: pse-eod-daily-quotation-2026-10-02
  title: "Daily Quotation Report, 2 Oct 2026"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: "https://documents.pse.com.ph/market_report/October%2002,%202026-EOD.pdf"
  local_path: pdfs/pse-eod-daily-quotation-2026-10-02.pdf
  edition: n/a
  amended_through: "2026-10-02"
  note: "Block-sale list, odd-lot, VWAP and grand totals; 185 further daily reports of 2026 (same URL pattern, 2 Jan-1 Oct 2026) were parsed but not archived."
- slug: pse-eod-daily-quotation-2026-09-11
  title: "Daily Quotation Report, 11 Sep 2026"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: "https://documents.pse.com.ph/market_report/September%2011,%202026-EOD.pdf"
  local_path: pdfs/pse-eod-daily-quotation-2026-09-11.pdf
  edition: n/a
  amended_through: "2026-09-11"
  note: "Peak block-share day of 2026 (FGEN 715.9m shares at 36.00); archived by another researcher."
- slug: pse-eod-daily-quotation-2024-05-24
  title: "Daily Quotation Report, 24 May 2024"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: "https://documents.pse.com.ph/market_report/May%2024,%202024-EOD.pdf"
  local_path: pdfs/pse-eod-daily-quotation-2024-05-24.pdf
  edition: n/a
  amended_through: "2024-05-24"
  note: "Earlier sample of block-sale/odd-lot/VWAP reporting."
- slug: pse-infographic-2q26
  title: "PSE 2Q 2026 infographic (stock market indicators)"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: "not recorded (PSE documents site; archived by another researcher)"
  local_path: pdfs/pse-infographic-2q26.pdf
  edition: in-force
  amended_through: undated
  note: "Average daily value traded PHP 7.72bn YTD (to 30 Jun 2026) - used to validate the DQR grand total."
- slug: pse-tpa-2026-0010-block-sale-spm
  title: "Execution of block sale for SPM shares (TPA-2026-0010)"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: https://documents.pse.com.ph/CircularOPSPDF/TPA-2026-0010.pdf
  local_path: pdfs/pse-tpa-2026-0010-block-sale-spm.pdf
  edition: n/a
  amended_through: "2026-03-06"
  note: "Pre-announcement of a special block sale (one day ahead)."
- slug: pse-tpa-2026-0012-block-sale-ati-tender-offer
  title: "Execution of block sales for ATI shares (TPA-2026-0012)"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: https://documents.pse.com.ph/CircularOPSPDF/TPA-2026-0012.pdf
  local_path: pdfs/pse-tpa-2026-0012-block-sale-ati-tender-offer.pdf
  edition: n/a
  amended_through: "2026-03-12"
  note: "Tender-offer block; price column typo (3.60 vs values at 36.00)."
- slug: pse-tpa-2026-0023-block-sale-pal
  title: "Execution of block sale for PAL shares (TPA-2026-0023)"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: https://documents.pse.com.ph/CircularOPSPDF/TPA-2026-0023.pdf
  local_path: pdfs/pse-tpa-2026-0023-block-sale-pal.pdf
  edition: n/a
  amended_through: "2026-05-28"
  note: "Pre-announced block sale."
- slug: sccp-clearing-house-rules-2018
  title: "Revised Rules of the Securities Clearing Corporation of the Philippines (SCCP)"
  publisher: Securities Clearing Corporation of the Philippines
  type: pdf
  canonical_url: https://documents.pse.com.ph/wp-content/uploads/sites/15/2021/04/SCCP_Revised_Rules.pdf
  local_path: pdfs/sccp-clearing-house-rules-2018.pdf
  edition: in-force
  amended_through: undated
  note: "Clearing-fund contribution base is net of block sales and same-flag crosses (p.33)."
- slug: pse-dds-rules
  title: "PSE Rules on Dollar Denominated Securities (DDS Rules)"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: https://documents.pse.com.ph/wp-content/uploads/sites/15/2021/01/Approved_DDS_Rules.pdf
  local_path: pdfs/pse-dds-rules.pdf
  edition: in-force
  amended_through: undated
  note: "Undated approved rules; Part C s.1 (pp.6-7): DDS block minimums USD 500k/1m, same opening/closing price calculation, odd-lot trading allowed. CN-2025-0046 proposes a one-share DDS lot."
- slug: sccp-memo-04-0823-t2-go-live
  title: "SCCP Memo for Brokers 04-0823: Go-live of the migration to the T+2 settlement cycle on 24 Aug 2023"
  publisher: Securities Clearing Corporation of the Philippines
  type: pdf
  canonical_url: "not recorded (SCCP memo; archived by another researcher)"
  local_path: pdfs/sccp-memo-04-0823-t2-go-live.pdf
  edition: in-force
  amended_through: "2023-08-11"
  note: "SEC En Banc approved the T+2 go-live effective 24 Aug 2023; no block-sale-specific settlement text."
- slug: pse-regulation-trading-participants
  title: "PSE Regulation - Trading Participants rules page (lists Revised Trading Rules and amendment documents)"
  publisher: The Philippine Stock Exchange, Inc.
  type: web
  canonical_url: https://www.pse.com.ph/regulation-trading-participants/
  local_path: null
  edition: in-force
  amended_through: undated
  note: "Viewed 6 Oct 2026; shows the June 2010 compilation plus seven amendment documents and the VWAP rules; no consolidated text."
- slug: pse-psetrade-xts
  title: "PSEtrade XTS overview and system features"
  publisher: The Philippine Stock Exchange, Inc.
  type: web
  canonical_url: https://www.pse.com.ph/psetrade-xts/
  local_path: null
  edition: in-force
  amended_through: undated
  note: "XTS go-live 22 Jun 2015 (replaced NSC); private order book and 'Unplaced' orders."
- slug: pse-new-trading-engine
  title: "PSE Trading Engine 2026 (Nasdaq Eqlipse) overview, system features, updates, FAQs"
  publisher: The Philippine Stock Exchange, Inc.
  type: web
  canonical_url: https://www.pse.com.ph/pse-new-trading-engine/
  local_path: null
  edition: in-force
  amended_through: undated
  note: "Viewed 6 Oct 2026; FIX/ITCH/MDF specifications are available on request only."
- slug: pse-investing-at-pse
  title: "Investing at PSE: trading hours, FAQs (PSEtrade XTS, CMIC surveillance)"
  publisher: The Philippine Stock Exchange, Inc.
  type: web
  canonical_url: https://www.pse.com.ph/investing-at-pse/
  local_path: null
  edition: in-force
  amended_through: undated
  note: "Current trading-hours table (first table); a stale 2013-era table appears further down the same page."
- slug: philstar-nte-golive-2026-07-23
  title: "New PSE trading engine goes live by November (Philstar, 23 Jul 2026)"
  publisher: Philstar.com
  type: web
  canonical_url: https://www.philstar.com/business/business-as-usual/2026/07/23/2543942/new-pse-trading-engine-goes-live-november
  local_path: null
  edition: n/a
  amended_through: "2026-07-23"
  note: "Secondary source; go-live 'by November', capacity and cost figures."
- slug: pse-vwap-announcement-2024
  title: "PSE to implement VWAP trading on March 1 (PSE announcement)"
  publisher: The Philippine Stock Exchange, Inc.
  type: web
  canonical_url: https://www.pse.com.ph/yearone/vwap/
  local_path: null
  edition: n/a
  amended_through: undated
  note: "Announcement that the SEC-approved VWAP trading opens Fri 1 Mar 2024 (page excerpt only; viewed 6 Oct 2026)."
- slug: digest-ph-pse-circular-248-97
  title: "PSE Circular No. 248-97, Updated and Consolidated Trading Rules (digest.ph preview)"
  publisher: digest.ph
  type: web
  canonical_url: https://www.digest.ph/corporate/updated-and-consolidated-trading-rules
  local_path: null
  edition: historical
  amended_through: "1997-12-23"
  note: "Secondary/aggregator preview: only the table of contents is visible (full text behind login); used only to show that opening-price, cross and special-block-sale articles already existed in 1997."
- slug: aseanexchanges-vwap-2024
  title: "PSE to implement VWAP trading on March 1 (ASEAN Exchanges)"
  publisher: ASEAN Exchanges
  type: web
  canonical_url: https://www.aseanexchanges.org/content/pse-to-implement-vwap-trading-on-march-1/
  local_path: null
  edition: n/a
  amended_through: undated
  note: "Secondary source for the 1 Mar 2024 VWAP launch date and 15:00-15:15 window."
```
