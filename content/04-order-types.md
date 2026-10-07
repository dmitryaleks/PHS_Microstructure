---
number: 4
slug: order-types
title: Order Types, Tick Sizes and Board Lots
summary: The rulebook lists six order types but the new engine opens with limits only; re-pricing or upsizing costs queue priority; a 15-band PHP lot and tick table makes the relative tick jump at band edges.
part: Trading mechanics
---

PSE's order model is rule-rich but thinly documented. The June 2010 Revised Trading Rules (RTR) define limit, market, market-to-limit, stop (stop-limit and stop-loss), market-on-opening/closing and cross orders, six validity types and two volume qualifiers; the only engine-level document in the public record is a 2015 FIX specification for PSEtrade XTS that enumerates fewer of them; and the engine that replaces XTS on 23 Nov 2026 will accept **limit orders only** on its first day.[^pse-revised-trading-rules:21-23][^pse-fix-specification-v2-5:52][^pse-nte-faq-2026-08:1] The practical common denominator is a Day limit order; anything else must be confirmed with the broker's certified front end before it is relied on.

Two behaviours break assumptions carried over from other venues. First, **tick and board lot are set by the day's reference price through a 15-band table unchanged since 26 Jul 2010**. The relative tick runs from 4 to 25 basis points above PHP 5 and steps up at most band edges (2.5x at PHP 20, 500 and 5,000; 2x at most others), so queue economics change discontinuously as a stock crosses PHP 20, 100 or 500.[^pse-revised-trading-rules:21] Second, **queue priority is lost on re-pricing and on any size increase but kept on size decreases and validity changes**; the no-cancel windows (from 09:15 and 14:48), the recess and any freeze remove the ability to cancel; and no cancel-on-disconnect is documented.[^pse-revised-trading-rules:25] A pending change (One Lot One Share, a 10-band tick table, no odd-lot market) is covered in [its own section](#/ch/order-types/one-lot-one-share-proposed); it is **not in force**.

## Order types and validity

### What the rulebook defines and what the engine exposes

The tables set RTR Article IV Section 9 against the PSEtrade XTS FIX specification v2.5 (10 Aug 2015). Neither states what a given broker's front end lets a client send.

| Order type | Rule text (RTR Art. IV §9, 2010) | XTS FIX v2.5 | NTE Day 1 |
|---|---|---|---|
| **Limit** | Entered Pre-Open to Trading-at-Last with a limit price within the Static Threshold; executes at the limit or better; the remainder queues[^pse-revised-trading-rules:21] | OrdType 2[^pse-fix-specification-v2-5:52] | Yes (only type)[^pse-nte-faq-2026-08:1] |
| **Market** | No price; executes "either at the BBO or the LTP, whichever is better"; enterable from Pre-Open to continuous trading; the remainder is "added and queued in the Order book for immediate execution"[^pse-revised-trading-rules:21-22] | OrdType 1: "executes against the best prices order on the opposite side"[^pse-fix-specification-v2-5:52] | No |
| **Market-to-Limit** | Continuous trading only; executes at the best price between the BBO and the LTP; the remainder becomes a limit order at the executed price; eliminated if there is no counterpart on entry[^pse-revised-trading-rules:22] | No enumeration | No |
| **Stop / Stop-Limit / Stop-Loss** | Inactive until a trade occurs at the trigger or better; the trigger must be better than the LTP (buy above, sell below); Stop-Limit has a trigger and a limit price; Stop-Loss has only a trigger and becomes a market order[^pse-revised-trading-rules:22] | OrdType 3 Stop and 4 Stop Limit with a TriggeringInstruction block (TriggerPriceType 2 = Last Trade); status X while untriggered[^pse-fix-specification-v2-5:48-49][^pse-fix-specification-v2-5:52] | No |
| **Market-on-Opening / Closing** | Entered in Pre-Open or Pre-Close; executable only at the indicative opening or closing price; if unmatched at the end of the call it becomes a limit order at that price[^pse-revised-trading-rules:22] | No enumeration | No |
| **Cross order** | Buy and sell orders of the same TP executed at an agreed quantity and price within the BBO[^pse-revised-trading-rules:22] | New Order Cross (35=s): CrossType 1 (Cross AON), limit only, TIF IOC[^pse-fix-specification-v2-5:16-17][^pse-fix-specification-v2-5:50] | Not stated |

| Validity | Rule text | XTS FIX TimeInForce |
|---|---|---|
| **Day** | Valid until the end of the Trading Day[^pse-revised-trading-rules:22] | 0 (also the default when the field is absent) |
| **GTC** | Valid until cancelled or until the security's set expiration date[^pse-revised-trading-rules:23] | 1 |
| **GTD** | Valid until the date specified[^pse-revised-trading-rules:23] | 6, with ExpireDate (432) |
| **GTW** (Good Till Week) | Seven calendar days from posting[^pse-revised-trading-rules:23] | None; use GTD |
| **Sliding Validity** | One calendar year[^pse-revised-trading-rules:23] | None |
| **Fill-and-Kill (FAK)** | In Pre-Open/Pre-Close, executed "to the fullest extent possible" at the end of the call, remainder eliminated; in continuous trading or run-off, executed immediately on entry, remainder eliminated[^pse-revised-trading-rules:23] | 3 (IOC/FaK) |
| **Fill-or-Kill** | Not in the RTR or IG | 4 (added in FIX v2.5)[^pse-fix-specification-v2-5:3] |
| **Session** | Not in the RTR or IG | 8 |

TimeInForce values are FIX Appendix C.[^pse-fix-specification-v2-5:16][^pse-fix-specification-v2-5:53]

<div class="callout warn">
<span class="label">What the public record cannot settle</span>

The rulebook and the FIX specification disagree on the order set: market-to-limit, market-on-opening/closing, GTW and Sliding Validity have no FIX value, while FOK and Session appear in FIX but not in the rulebook, so the 2010 text may describe types XTS maps differently or does not offer. PSE publishes no broker order-type matrix. A broker's front end "may accept or internally process other types of Orders", but "only Order types that are offered and/or used by the PSE Trading System shall be forwarded and accepted", so trailing stops, OCO and similar retail conditionals are broker-side constructs unless they map to a type above.[^pse-implementing-guidelines-trading-rules:31] No fully hidden, pegged or stand-alone all-or-none order type is described in the RTR or IG (absence of evidence).
</div>

### XTS order states

- **Private book and unplaced orders.** FIX ExecInst S ("suspend: move to private book") and q ("unsuspend: enter into the market") store an order un-released (status Z). PSE's XTS page says GTC/GTD orders priced outside the day's static floor or ceiling are held as "Unplaced" (status U), invisible, and activate on a later day if they fall inside the new thresholds.[^pse-fix-specification-v2-5:50][^pse-fix-specification-v2-5:52][^pse-web-xts] Multi-day orders are restated in execution reports at market start.[^pse-fix-specification-v2-5:20]
- **Status vocabulary in PSE terminals (IG X):** Active, Cancelled, Error, Executed, Frozen, Market Eliminated (cancelled by Market Control or automatically under market rules), Modified, Scheduled (released at a pre-set time), Sent, Sending, Waiting.[^pse-implementing-guidelines-trading-rules:17]

### Market-order behaviour

The 2010 text leaves an unfilled market-order remainder "queued ... for immediate execution".[^pse-revised-trading-rules:22] PSE's November 2014 consultation for the XTS launch proposed that the remainder rest as a limit order at the last executed price (withdrawn if the order is FAK) and that a market order be rejected when the opposite side is empty; the SEC-approved wording is not public.[^pse-memo-revisions-trading-rules-consultation-2014:2-3] An unfilled market order at the open triggers "reservation" of the security.[^pse-revised-trading-rules:33] Under the rule text market orders may be entered only from Pre-Open to continuous trading, not in Pre-Close or run-off; the 2010 and 2013 IG run-off wording allowed "Market Orders" there, the Dec 2011 wording was limit-only, and the 2024 wording says only "Orders at the Closing Price".[^pse-revised-trading-rules:21-22][^pse-tpa-2013-0185-extended-pre-close:7][^pse-tpa-2011-0124-amended-implementing-guidelines:3][^pse-approved-rules-vwap-trading-2024:6]

<div class="callout infer">
<span class="label">Inference</span>

Do not assume a PSE market order sweeps the book to completion. Whether the remainder rests as a limit at the last execution price (2014 draft) or stays "for immediate execution" (2010 text) is not settled publicly, and on the new engine's first day a marketable limit is the only option anyway. Use marketable limits priced inside the dynamic threshold ([Chapter 7](#/ch/price-controls)).
</div>

### Execution implications

- Treat **limit-Day as the lowest common denominator** across XTS and NTE Day 1. Emulate market orders with marketable limits and keep stop, market-to-limit and market-on-open/close logic in the router until PSE publishes the NTE order-entry specification.
- Multi-day orders are fragile: the Exchange cancels orders on every cash-dividend ex-date, on corporate actions that adjust the closing price, and when the board lot changes ([cancellation](#/ch/order-types/cancellation-mass-cancel-and-disconnects)). Re-enter GTC/GTD interest daily. The PSETradeX terminal is also dropping GTC and next-day validity and adding a "Good Till 3 Months" type for its cloud version (the cloud migration was reported deferred on 9 Jul 2026); whether that reflects engine-level limits is not stated.[^pse-nte-user-group-2026-01-15:17][^pse-nte-broker-forum-2026-07-09:11]
- Assume resting non-Day orders do **not** survive the 23 Nov 2026 cut-over unless the broker confirms otherwise.

## Volume qualifiers: minimum quantity and iceberg

A **minimum-quantity** order applies only to limit or market-to-limit orders: it must execute immediately to at least the minimum (the rest is added to the book) or it is eliminated. An **iceberg** applies only to limit or stop-limit orders; it is also called "disclosed quantity" or "quantity shown", is "successively entered in the Order book, and disclosed to the market at specified tranches", and the disclosed quantity must be **at least 10% of the total quantity and a multiple of the board lot**.[^pse-revised-trading-rules:23] The IG permits these combinations for limit orders:[^pse-implementing-guidelines-trading-rules:12]

| Combination | Pre-Open / Pre-Close | Continuous | Run-off |
|---|---|---|---|
| FAK, standard | Allowed | Allowed | Allowed |
| FAK + minimum quantity | Not allowed | Allowed | Allowed |
| FAK + disclosed quantity | Not allowed | Not allowed | Not allowed |
| Day / GTD / GTC / Sliding, standard | Allowed | Allowed | Allowed |
| Day / GTD / GTC / Sliding + minimum quantity | Not allowed | Allowed | Allowed |
| Day / GTD / GTC / Sliding + disclosed quantity | Allowed | Allowed | Allowed |

In FIX the fields are MinQty (110) and DisplayQty (1138, replacing MaxFloor); every fill report returns DisplayQty, equal to LeavesQty for non-iceberg orders.[^pse-fix-specification-v2-5:16][^pse-fix-specification-v2-5:23] (The amendable-field list prints the legacy tag 111, a specification inconsistency to test in UAT.[^pse-fix-specification-v2-5:25])

**Worked example (derived).** A PHP 10 million buy at PHP 20.00 is 500,000 shares with a board lot of 100. As an iceberg it must show at least 50,000 shares (PHP 1 million) at all times, so at most 90% can be hidden.

<div class="callout infer">
<span class="label">Inference</span>

PSE publishes no rule on iceberg replenishment priority. Because each tranche is "successively entered in the Order book", assume every refresh re-queues behind existing orders at the price, so an iceberg in a deep queue can be materially worse than a sequence of ordinary orders. The rules also do not say whether an increase in disclosed quantity loses priority.
</div>

### Execution implications

- Hidden size is bounded: at least 10% must be shown, in board-lot multiples. Further concealment has to come from scheduling, not order type.
- Minimum-quantity orders are unavailable in the 09:00-09:30 and 14:45-14:50 calls.
- Iceberg and minimum-quantity support on the NTE is not stated; build slicing and minimum-fill logic in the router. If One Lot One Share is approved the board-lot-multiple constraint disappears, but PSE has not said whether the 10% rule survives.

## Priority and amendments

Matching is price then time. Orders rank by type first (market orders, then market-on-opening/closing, then limit orders); market and market-on-open/close orders by time of entry; limit orders by price (higher bid, lower offer) and then time.[^pse-implementing-guidelines-trading-rules:12] There is no broker-priority rule, but an automatic cross lets a TP's new counterpart order match its own earlier posted order "regardless of its position in the queue" ([Chapter 5](#/ch/matching)).[^pse-revised-trading-rules:31]

| Amendment to a posted, unmatched order | Queue priority |
|---|---|
| Decrease in volume | **Kept** |
| Change of validity type | **Kept** |
| Change of client account code | **Kept** |
| Increase in volume | **Lost** |
| Change of limit price | **Lost** |
| Change of trigger price | **Lost** |

Source: RTR Article IV Section 13 and IG XI.[^pse-revised-trading-rules:24-25][^pse-implementing-guidelines-trading-rules:18] The FIX specification says the same: "Any change to the price or trigger price of an order, or increasing quantities will result in the order losing its priority in the market."[^pse-fix-specification-v2-5:26]

- **Windows.** Modification is allowed from Pre-Open to Trading-at-Last except in the two No-Cancel periods and the Market Recess.[^pse-tpa-2011-0124-amended-implementing-guidelines:3]
- **Ownership.** No unmatched order can be modified from client to proprietary or the reverse; a PC trader cannot modify others' orders without taking ownership, and the trader who last acted on an order bears responsibility for it.[^pse-revised-trading-rules:25][^pse-implementing-guidelines-trading-rules:18]
- **FIX mechanics.** Amendment is Order Cancel/Replace (35=G) carrying the full requested new state, not a delta, with a new ClOrdID; the exchange may change the OrderID afterwards. Amendable fields: ClOrdID, quantity, display quantity, price, order type, TIF, expiry date, give-up firm, account, MinQty, text, trigger price, ExecInst, and side (buy to buy-in and sell to short sell, and back; Side values are 1 Buy, 2 Sell, 5 Short Sell, Z Buy Back).[^pse-fix-specification-v2-5:25-26][^pse-fix-specification-v2-5:53] Cancel/Replace is also how to reduce an order partly.[^pse-fix-specification-v2-5:17] The exchange "may not check" ClOrdID uniqueness, so the firm must guarantee it within a trading day and across all its FIX connections.[^pse-fix-specification-v2-5:25]

### Execution implications

- **Downsizing is free; upsizing and re-pricing are not.** To cut exposure at a price, amend down rather than cancel and replace; to add exposure, send a new order when queue position has value.
- **Validity changes keep priority**, so extending a working order's life costs nothing.
- Expect lower passive fill probability at the touch where a large broker holds both sides (automatic-cross priority), and expect your own broker to cross offsetting client orders ahead of others' earlier orders (inference).
- The XTS order-entry fields carry no self-trade-prevention flag,[^pse-fix-specification-v2-5:15-16] and wash trades are prohibited conduct ([Chapter 13](#/ch/regulatory-constraints)): the algorithm itself must avoid trading against its own resting orders across child orders and accounts.

## Cancellation, mass cancel and disconnects

Phase by phase on the whole-day schedule (the clock is in [Chapter 3](#/ch/sessions/the-trading-day)):

| Phase | Enter | Modify | Cancel |
|---|---|---|---|
| Pre-Open 09:00-09:15 | Yes | Yes | Yes |
| Pre-Open No-Cancel 09:15-09:30 | Yes | No | No |
| Opening (book frozen) | No | No | No |
| Continuous 09:30-12:00, 13:00-14:45 | Yes | Yes | Yes (including the unmatched remainder of a partial fill) |
| Recess 12:00-13:00 | No | No | No |
| Pre-Close 14:45-14:48 | Yes | Yes | Yes |
| Pre-Close No-Cancel 14:48-14:50 | Yes | No | No |
| Run-off 14:50-15:00 | Closing Price only | Sources conflict | Sources conflict |
| Closing VWAP 15:00-15:15, Close | No ordinary orders | No | No |

Sources: [^pse-approved-rules-vwap-trading-2024:6][^pse-implementing-guidelines-trading-rules:17-18][^pse-tpa-2011-0124-amended-implementing-guidelines:3] A frozen security (an order that would breach a price threshold) takes no posting, modification or cancellation until Market Control acts; halted and reserved securities allow them except for crosses ([Chapter 7](#/ch/price-controls)).[^pse-revised-trading-rules:33]

<div class="callout warn">
<span class="label">Run-off: cancel and amend are contradicted</span>

IG XI and XII say modification and cancellation are allowed up to Trading-at-Last except in the no-cancel periods and the recess, and that a TP may cancel active orders during run-off.[^pse-implementing-guidelines-trading-rules:17-18] The XTS ITCH system-event table shows, for event P (Trading At Last), order entry Y but amend-and-cancel N.[^pse-itch-equities-feed-spec-v2-3:10] PSE's December 2025 draft for the new engine says run-off orders "can be entered, modified, and executed only at the Closing Price".[^pse-cn-2025-0046-board-lot-trading-at-last:8] The conflict is unresolved: design for **no cancel in run-off**.
</div>

- **Exchange-initiated cancellation.** The RTR says the Exchange "shall cancel" orders for a security on corporate actions that adjust the closing price, **on the ex-date of securities with cash or property dividends**, and for securities that cross a board lot; the IG words the first and last as "may cancel all active Orders". A suspended security's posted orders are purged upon suspension.[^pse-revised-trading-rules:25][^pse-implementing-guidelines-trading-rules:18][^pse-implementing-guidelines-trading-rules:27] Ex-date arithmetic is in [Chapter 10](#/ch/clearing-settlement).
- **Mass cancel.** A TP "can only direct the Exchange to execute a cancellation of all the Orders already posted" when its PSE-certified FEOMS or the Exchange's Common Customer Gateway (CCG) suffers a failure or interruption. In a CCG failure the market halts for the outage plus ten minutes and Market Control acts on active orders at the client's request.[^pse-revised-trading-rules:25][^pse-implementing-guidelines-trading-rules:18][^pse-implementing-guidelines-trading-rules:30]
- **No documented cancel-on-disconnect.** Nothing in the RTR, IG or FIX specification cancels a session's orders when it drops. At the session layer a silent counterpart is sent a Test Request after HeartBtInt plus a reasonable transmission time, and "the connection should be considered lost and corrective action be initiated"; with HeartBtInt = 30 the server disconnects in 66 seconds (2 x HeartBtInt + 6).[^pse-fix-specification-v2-5:14] The specification is silent on the fate of resting orders (absence of evidence).

### Execution implications

- The last cancel opportunities are 09:14:59 and 14:47:59; nothing can be touched from 12:00:00 to 13:00:00.
- **Do not rely on exchange-side cancel-on-disconnect.** Build a router-side kill switch and a broker or Market Control mass-cancel procedure, which exists only for FEOMS or CCG failures.
- During a freeze you cannot cancel: size child orders so a sweep cannot breach the dynamic threshold relative to the last traded price, or accept the review risk.
- Re-enter GTC/GTD interest on ex-dates, after corporate actions and board-lot changes, and at the engine cut-over.

## Board lots and tick sizes

### The PHP table in force (RTR Article IV Section 8, effective 26 Jul 2010)

"The Board Lot and Price Fluctuation of a Security for any Trading Day shall be based on the Security's Reference Price."[^pse-revised-trading-rules:21] The table is reproduced as printed in the RTR; it is identical to the "Existing" table in PSE's October 2023 and December 2025 consultations and the January 2026 engine deck, and to PSE's website and a broker FAQ.[^pse-revised-trading-rules:21][^pse-cn-2023-0051:3-4][^pse-cn-2025-0046-board-lot-trading-at-last:4][^pse-nte-user-group-2026-01-15:9][^pse-web-investing-at-pse][^firstmetrosec-faqs-681]

| # | Price from | Price to | Tick size | Lot size (shares) |
|---|---|---|---|---|
| 1 | 0.0001 | 0.0099 | 0.0001 | 1,000,000 |
| 2 | 0.0100 | 0.0490 | 0.0010 | 100,000 |
| 3 | 0.0500 | 0.2490 | 0.0010 | 10,000 |
| 4 | 0.2500 | 0.4950 | 0.0050 | 10,000 |
| 5 | 0.5000 | 4.9900 | 0.0100 | 1,000 |
| 6 | 5.0000 | 9.9900 | 0.0100 | 100 |
| 7 | 10.0000 | 19.9800 | 0.0200 | 100 |
| 8 | 20.0000 | 49.9500 | 0.0500 | 100 |
| 9 | 50.0000 | 99.9500 | 0.0500 | 10 |
| 10 | 100.0000 | 199.9000 | 0.1000 | 10 |
| 11 | 200.0000 | 499.8000 | 0.2000 | 10 |
| 12 | 500.0000 | 999.5000 | 0.5000 | 10 |
| 13 | 1000.0000 | 1999.0000 | 1.0000 | 5 |
| 14 | 2000.0000 | 4998.0000 | 2.0000 | 5 |
| 15 | 5000.0000 | UP | 5.0000 | 5 |

```text
# from,to,tick,lot  (RTR Art. IV Sec. 8; key on the day's Reference Price; UP = no upper bound)
0.0001,0.0099,0.0001,1000000
0.0100,0.0490,0.0010,100000
0.0500,0.2490,0.0010,10000
0.2500,0.4950,0.0050,10000
0.5000,4.9900,0.0100,1000
5.0000,9.9900,0.0100,100
10.0000,19.9800,0.0200,100
20.0000,49.9500,0.0500,100
50.0000,99.9500,0.0500,10
100.0000,199.9000,0.1000,10
200.0000,499.8000,0.2000,10
500.0000,999.5000,0.5000,10
1000.0000,1999.0000,1.0000,5
2000.0000,4998.0000,2.0000,5
5000.0000,UP,5.0000,5
```

### Application rules

- **Reference Price** is the previous Trading Day's Closing Price; the Adjusted Closing Price after a corporate action; or the last traded or last adjusted price if the security did not trade the previous day.[^pse-revised-trading-rules:20] Key every lookup on that (LACP), not the live price. PSE's NTE static-data file carries LACP but no tick or lot field.[^pse-securities-static-data-file:4]
- **Valid prices** step from the band's lower bound in tick increments to its upper bound (10.00, 10.02 ... 19.98; 20.00, 20.05 ... 49.95); the bands join without gaps (inference from the table). "Price Fluctuation or Tick Size" means "the allowed price step based on a given price range for a Security".[^pse-revised-trading-rules:10]
- **Quantity.** Orders below one board lot are odd-lot orders (below). Normal-market quantities are board-lot multiples, in contrast to block sales, which "may be non-multiples of the board lot"; the rules do not say whether an order above one lot but not a multiple is rejected or split (inference and gap).[^pse-implementing-guidelines-trading-rules:19][^pse-implementing-guidelines-trading-rules:24] Block sales may be priced to four decimals, as may VWAP and proposed negotiated trades, so they are not tick-constrained.[^pse-implementing-guidelines-trading-rules:24][^pse-approved-rules-vwap-trading-2024:7][^pse-cn-2026-0031-negotiated-trades:11]
### Relative tick cost at band edges (derived)

Relative tick = tick / price, in basis points (bp). "Jump" divides the relative tick at a band's lower edge by that at the previous band's upper edge: the discontinuity a stock crosses when its reference price moves one tick over the boundary.

| # | Band (PHP) | Tick | Lot | bp at lower edge | bp at upper edge | Jump into band | Lot value, lower-upper (PHP) |
|---|---|---|---|---|---|---|---|
| 1 | 0.0001-0.0099 | 0.0001 | 1,000,000 | 10,000 | 101.0 | - | 100-9,900 |
| 2 | 0.0100-0.0490 | 0.001 | 100,000 | 1,000.0 | 204.1 | 9.9x | 1,000-4,900 |
| 3 | 0.0500-0.2490 | 0.001 | 10,000 | 200.0 | 40.2 | 1.0x | 500-2,490 |
| 4 | 0.2500-0.4950 | 0.005 | 10,000 | 200.0 | 101.0 | 5.0x | 2,500-4,950 |
| 5 | 0.5000-4.9900 | 0.01 | 1,000 | 200.0 | 20.0 | 2.0x | 500-4,990 |
| 6 | 5.0000-9.9900 | 0.01 | 100 | 20.0 | 10.0 | 1.0x | 500-999 |
| 7 | 10.0000-19.9800 | 0.02 | 100 | 20.0 | 10.0 | 2.0x | 1,000-1,998 |
| 8 | 20.0000-49.9500 | 0.05 | 100 | 25.0 | 10.0 | **2.5x** | 2,000-4,995 |
| 9 | 50.0000-99.9500 | 0.05 | 10 | 10.0 | 5.0 | 1.0x | 500-999.50 |
| 10 | 100.0000-199.9000 | 0.10 | 10 | 10.0 | 5.0 | 2.0x | 1,000-1,999 |
| 11 | 200.0000-499.8000 | 0.20 | 10 | 10.0 | 4.0 | 2.0x | 2,000-4,998 |
| 12 | 500.0000-999.5000 | 0.50 | 10 | 10.0 | 5.0 | **2.5x** | 5,000-9,995 |
| 13 | 1,000-1,999 | 1.00 | 5 | 10.0 | 5.0 | 2.0x | 5,000-9,995 |
| 14 | 2,000-4,998 | 2.00 | 5 | 10.0 | 4.0 | 2.0x | 10,000-24,990 |
| 15 | 5,000 and up | 5.00 | 5 | 10.0 | toward 0 | **2.5x** | 25,000 and up |

Above PHP 5 the relative tick sits between 4 and 25 bp. It peaks at each band floor (20 bp at PHP 5.00 and 10.00, 25 bp at 20.00, 10 bp from PHP 50 up) and falls to 10 bp at the top of bands 6-8 and 4-5 bp from PHP 50 upward; below PHP 5 it runs from 20 bp (at 4.99) to 10,000 bp.

### Worked example: the PHP 20 cliff

A stock with a reference price of PHP 19.98 ticks at 0.02 (10.0 bp). At a reference of PHP 20.00, two cents later, the tick is 0.05 (25.0 bp). With a one-tick spread, buying PHP 10 million at the offer pays half the spread against the mid:

- At 19.98: 500,500 shares (5,005 lots); half-spread 0.01 x 500,500 = **PHP 5,005 (5.0 bp)**.
- At 20.00: 500,000 shares; half-spread 0.025 x 500,000 = **PHP 12,500 (12.5 bp)**.

The same order costs 2.5x as much to cross, PHP 7,495 more on PHP 10 million. Stepping ahead of a queue costs one tick: 10 bp at 19.98 (to 20.00) against 25 bp at 20.00 (to 20.05). Lots step too: at a reference of 49.95 the lot is 100 shares (PHP 4,995), at 50.00 it is 10 (PHP 500), so a 60-share residual is an odd-lot order on the first day and a six-lot normal order the next.

<div class="callout infer">
<span class="label">Inference</span>

The rule text fixes lot and tick for the whole day by the **reference price**, so a stock with a reference of 19.98 would keep a 0.02 tick all day even if it trades at 20.02. The legacy ITCH feed, however, models tick as a table of (price start, tick) pairs attached to each order book, which would make the tick a function of the **order price**; PSE does not say which the engine applies when the live price crosses an edge.[^pse-revised-trading-rules:21][^pse-itch-equities-feed-spec-v2-3:11-12] Near an edge the two readings give different ladders (after 20.00: 20.02 or 20.05). A price valid under both is a common multiple of the two ticks (for 0.02 and 0.05, any multiple of 0.10); test the behaviour in UAT.
</div>

### Dollar-denominated securities (DDS)

DDS use their own table (DDS Rules, Part C Section 1), keyed on the same Reference Price; they follow the same Trading Threshold and opening/closing rules, value limits convert to pesos at the previous day's exchange rate, and DDS can trade in the odd-lot market.[^pse-dds-rules:6][^pse-dds-rules:7]

| Price (USD) | Tick (USD) | Lot | bp at lower edge | bp at upper edge | Lot value (USD) |
|---|---|---|---|---|---|
| down to 0.99 | 0.01 | 100 | 10,000 (at 0.01) | 101.0 | 1-99 |
| 1.00-4.99 | 0.01 | 20 | 100.0 | 20.0 | 20-99.80 |
| 5.00-9.99 | 0.01 | 10 | 20.0 | 10.0 | 50-99.90 |
| 10.00-19.98 | 0.02 | 10 | 20.0 | 10.0 | 100-199.80 |
| 20.00-49.95 | 0.05 | 10 | 25.0 | 10.0 | 200-499.50 |
| 50.00-99.95 | 0.05 | 5 | 10.0 | 5.0 | 250-499.75 |
| 100.00-199.90 | 0.10 | 5 | 10.0 | 5.0 | 500-999.50 |
| 200.00-499.80 | 0.20 | 5 | 10.0 | 4.0 | 1,000-2,499 |
| 500.00-999.50 | 0.50 | 5 | 10.0 | 5.0 | 2,500-4,997.50 |
| 1,000.00 and up | 1.00 | 5 | 10.0 | toward 0 | 5,000 and up |

The rule prints the first band as "DOWN 0.99" with no lower bound; the 0.01 floor behind the basis points is an assumption of this table. The USD ticks equal the PHP ticks from 0.50 to 1,000 and then stay at 1.00 with no further steps, so the same cliffs apply at USD 10 (2.0x), 20 (2.5x), 100 (2.0x), 200 (2.0x), 500 (2.5x) and 1,000 (2.0x).

### ETFs, warrants, REITs, preferreds and GPDRs

- **ETFs** use the ordinary PHP table: PSE's ETF Rules illustrate an ETF at PHP 25.00 with tick 0.05 and lot 100. Market-maker spread caps are written in ticks (20 ticks to PHP 0.4950, 15 to PHP 19.98, 10 to PHP 999.50, 5 from PHP 1,000; quotes of at least five board lots), so their width in basis points follows the table above ([Chapter 8](#/ch/market-making)).[^pse-etf-rules:22-23]
- **Warrants** are exempt from the static threshold, but no separate tick or lot table exists for warrants, preferred shares or REITs in the public record; the same table is assumed (inference).[^pse-revised-trading-rules:20]
- **GPDRs** (draft rules, not approved) "shall generally follow the rules and procedures of trading of equity securities", with PSE able to adjust their trading hours to the underlying's overseas hours.[^pse-cn-2024-0047:23]

### The odd-lot market (until the new engine)

Orders smaller than the board lot cannot enter the normal market. They trade only in the separate **Odd Lot Market** (symbol prefix "O", so BC becomes OBC), as limit or market orders, in continuous trading only.[^pse-implementing-guidelines-trading-rules:19][^pse-implementing-guidelines-trading-rules:20] Its book, reference price, thresholds and exclusions are in [Chapter 5](#/ch/matching/odd-lots). For sizing, the consequence is that a quantity below one lot at the day's band can never reach the auctions or the run-off, and that using the odd-lot board to execute a normal-market transaction is a violation.[^pse-implementing-guidelines-trading-rules:20] The rules do not tie odd-lot prices to the board-lot BBO (inference) or address odd-lot settlement.

### Execution implications

- **Quantity rounding:** floor to a multiple of the lot for the day's reference-price band, looked up on LACP before 09:00. A board lot is worth roughly PHP 500-5,000 for most prices below PHP 1,000 and PHP 5,000-25,000 and more above, so the lot is the minimum child size.
- **Price rounding:** use the day's band; near an edge prefer a price valid under both readings. For names within a tick or two of an edge, tomorrow's lot or tick may differ, and the Exchange cancels multi-day orders when the lot changes.
- **Join versus improve:** improving a quote costs one tick, 25 bp at PHP 20.00 but 4 bp at PHP 499.80; use tick-aware thresholds per band. In the PHP 20-50 band, where the relative tick is largest above PHP 5, spreads are tick-constrained and queue position dominates (inference).
- **Residuals:** work odd-lot residuals in the odd-lot book in continuous trading; there is no auction path.

## Risk controls at order entry

PSE publishes no maximum order quantity. The controls are a per-order value limit, price collars, front-end and DMA filters, and a foreign-ownership earmark.

| Control | Rule |
|---|---|
| **Per-order value limit** | A TP sets a value limit **per order** for each trader, not exceeding the Exchange-required limit; deviation needs Exchange approval; the limit is per order, not a daily total; changes are requested by form at least one day ahead; the block-sale facility and VWAP trading observe it; DDS orders convert at the previous day's rate. The Exchange's numeric limit is not published[^pse-revised-trading-rules:24][^pse-implementing-guidelines-trading-rules:17][^pse-approved-rules-vwap-trading-2024:4][^pse-dds-rules:7] |
| **Price collars** | An order must be within the Trading Threshold: the static band (+50% / -30% of the reference price since 24 Mar 2020) and the dynamic threshold (10%, 15% or 20% by trade-count cluster; latest review effective 7 Aug 2026). A breach freezes the security until Market Control accepts or rejects ([Chapter 7](#/ch/price-controls))[^pse-cn-2020-0028:1-2][^pse-tpa-2026-0036-dynamic-threshold-review:1][^pse-revised-trading-rules:33] |
| **Certified FEOMS** | Front ends must be PSE-certified and re-certified for each change; one FEOMS log-in to the CCG per TP; "the PSE reserves the right to impose message flow controls for the FEOMS"; no numeric message limit is public[^pse-implementing-guidelines-trading-rules:30-31] |
| **Correspondent TP** | Every TP must designate a correspondent TP (different FEOMS vendor, or a separate silo and FIX gateway) and execute through it on a done-through account code; two months were allowed from 20 Aug 2025[^pse-cn-2025-0037:2][^pse-cn-2025-0037:6-7] |

**DMA filters.** A TP offering DMA must define automated pre-trade filters before a client is given access and run them before the order reaches PSEtrade: at minimum a **trade-exposure** limit (gross or net), an **order-size** limit (peso value, share volume, or both) and a **price limit** (percentage or ticks from the last traded or last adjusted closing price). Parameters are reviewed daily and changed only by authorised persons, every accept or reject is logged for at least five years, the facility must prevent wash sales, and Sponsored Access is confined to qualified institutional buyers.[^pse-dma-rules:5][^pse-dma-rules:7-10] The rules were transmitted by the SEC on 29 Oct 2013 and took effect on the first trading day of 2014 ([Chapter 1](#/ch/market-architecture/dma-rules-and-algorithmic-trading)).[^pse-dma-rules:1][^pse-memo-sec-approved-dma-rules-2013-11-26:1]

**Algorithmic trading.** "The DMA Facility shall not be used for High-Frequency and/or Algorithmic trading."[^pse-dma-rules:7] PSE says it has granted exemptions for child orders from conditioned parent orders; its September 2023 proposal to allow algorithmic trading (manually entered parent orders, limit-order children) was never approved, and only its VWAP part was adopted.[^pse-cn-2023-0043:3][^pse-cn-2023-0043:6-9][^pse-approved-rules-vwap-trading-2024:1] See [Chapter 1](#/ch/market-architecture/dma-rules-and-algorithmic-trading) and [Chapter 13](#/ch/regulatory-constraints).

**Foreign-ownership earmark.** "The Trading System will earmark all valid foreign buying Orders which will limit the available volume for succeeding foreign buying Orders within the applicable foreign ownership limits"; posting a foreign buy order for the "malicious purpose" of limiting the volume for foreign buyers attracts penal sanctions.[^pse-revised-trading-rules:17] Every account code carries a Local or Foreign flag, and an order combining local and foreign clients must use the foreign bundled account.[^pse-implementing-guidelines-trading-rules:21-22] Limits and mechanics are in [Chapter 14](#/ch/foreign-access).

### Execution implications

- Keep marketable limits inside the dynamic threshold of the last traded price (10% for the most liquid, cluster C): an order beyond it freezes the stock.
- Pre-check each order's value against the broker's per-trader limit, and ask the broker for it before sizing slices; the Exchange's own cap is undisclosed.
- Do not route algorithmic child orders through a pure DMA facility without broker clarity; the practical route is the broker's certified FEOMS with human-entered parent orders and limit-only child orders (inference from the DMA Rules and the 2023 proposal).
- A foreign buy order consumes foreign-ownership room at entry, before it executes: cancel stale foreign bids quickly in limit-constrained names, and before 09:15 if unused.[^pse-revised-trading-rules:17]

## One Lot One Share (proposed)

<div class="callout warn">
<span class="label">Not in force: awaiting SEC approval, targeted with the 23 Nov 2026 engine change</span>

PSE's consultation CN-2025-0046 (15 Dec 2025; comments to 31 Dec) proposes **One Lot One Share**: a one-share lot for every security regardless of price (PHP and USD), a 10-band PHP tick table (which the January 2026 deck calls "streamlined"), removal of the Odd Lot Market ("All orders will be matched on the normal market in the new trading engine") and a TP-set minimum order value, provided commission does not exceed the legal maximum.[^pse-cn-2025-0046-board-lot-trading-at-last:3-5][^pse-nte-user-group-2026-01-15:9] **No SEC approval or effectivity circular had appeared by 6 Oct 2026.** PSE's 4 Jul 2026 report says it is "awaiting SEC approval of the proposed Board Lot amendments, targeted for implementation in Q4 2026 alongside the new trading engine"; its 17 Aug status slide marks "One Share, One Lot" "For SEC Approval"; the 9 Jul broker forum lists "Lot sizes will be standardized at 1 share for both DDS and PHP securities"; and the August FAQ says the Odd Lot Market "will no longer be available in the New Trading Engine".[^pse-asm-2026-president-report:22][^pse-analyst-briefing-1h-2026:9][^pse-nte-broker-forum-2026-07-09:7][^pse-nte-faq-2026-08:1] PSE's engine page still lists CN-2025-0046 as its only update, and its announcements archive through 6 Oct 2026 shows no approval.[^pse-web-nte][^pse-web-announcements-archive][^pse-web-circulars-index]

**Stated intent.** PSE's 2023 President's Report frames the change as Phase 1 of a "Fractional Trading" initiative that "allows an investor to buy partial shares of a stock and make trades based on peso value instead of number of shares", with "Phase 1 to focus on amendment of board lot structure". No later phase, rule or date was found.[^pse-asm-2023-presidents-report:40]

**A prior attempt did not land.** CN-2023-0051 (9 Oct 2023) proposed lots of 20,000 / 5,000 / 2,000 / 400 / 100 / 20 / 10 / 5 / 2 / 1 / 1 / 1 / 1 / 1 / 1 down the 15 bands "to accommodate a Php100 minimum investment" (band 4 stretched to 0.2500-0.9950 at tick 0.005, band 5 starting at 1.0000).[^pse-cn-2023-0051:3-4] PSE's July 2024 report still described it as awaiting SEC approval; it was never approved, and the December 2025 paper shows the 2010 table as "Existing" (that it was abandoned is inference).[^pse-asm-2024-presidents-report:18][^pse-cn-2025-0046-board-lot-trading-at-last:4] PSE targets have slipped before ([Chapter 17](#/ch/reform-timeline)): if the SEC does not approve before 23 Nov, PSE would either keep the existing table on the new engine or delay the engine, and its materials do not say which (inference).
</div>

### Proposed tables (not in force)

| Price (PHP) | Tick | Lot |
|---|---|---|
| Up to 0.099 | 0.001 | 1 |
| 0.10-0.995 | 0.005 | 1 |
| 1-9.99 | 0.01 | 1 |
| 10-99.95 | 0.05 | 1 |
| 100-199.90 | 0.10 | 1 |
| 200-499.80 | 0.20 | 1 |
| 500-999.50 | 0.50 | 1 |
| 1,000-1,999 | 1 | 1 |
| 2,000-4,998 | 2 | 1 |
| 5,000 and up | 5 | 1 |

| Price (USD) | Tick | Lot |
|---|---|---|
| Up to 9.99 | 0.01 | 1 |
| 10-19.98 | 0.02 | 1 |
| 20-99.95 | 0.05 | 1 |
| 100-199.90 | 0.10 | 1 |
| 200-499.80 | 0.20 | 1 |
| 500-999.50 | 0.50 | 1 |
| 1,000 and up | 1 | 1 |

Sources: the consultation paper and the January 2026 engine deck.[^pse-cn-2025-0046-board-lot-trading-at-last:4-5][^pse-nte-user-group-2026-01-15:9-10] The draft rule text keeps tick and lot "based on the given price range for the Security's Reference Price".[^pse-cn-2025-0046-board-lot-trading-at-last:3]

**What changes in the relative tick (derived).** Bands from PHP 20 upward are unchanged:

| Reference price (PHP) | Current tick (bp range) | Proposed tick (bp range) | Effect |
|---|---|---|---|
| Below 0.01 | 0.0001 (10,000 to 101) | 0.001 (1,010 at 0.0099) | 10x coarser (assumes the "up to 0.099" band covers prices below 0.01; inference) |
| 0.01-0.099 | 0.001 | 0.001 | Unchanged |
| 0.10-0.249 | 0.001 (100 to 40) | 0.005 (500 to 201) | 5x coarser |
| 0.25-0.495 | 0.005 | 0.005 | Unchanged |
| 0.50-0.995 | 0.01 (200 to 101) | 0.005 (100 to 50) | 2x finer |
| 1.00-9.99 | 0.01 | 0.01 | Unchanged |
| 10.00-19.98 | 0.02 (20 to 10) | 0.05 (50 to 25) | 2.5x coarser; minimum spread rises from 10-20 bp to 25-50 bp |

The cliffs move too: the PHP 20 cliff disappears (0.05 on both sides), while PHP 10 becomes the sharpest edge (10.0 bp at 9.99 to 50 bp at 10.00, a 5x jump) and PHP 0.10 jumps 4.95x (101 bp to 500 bp).

### Execution implications

- Parameterise **both** regimes (lot table, tick table, odd-lot logic) behind a flag flipped on PSE's effectivity circular, not on the engine date alone: the engine may go live on the old tables if approval is late. The NTE static-data file has no tick or lot field, so key the tables on LACP.[^pse-securities-static-data-file:4]
- Under One Lot One Share board-lot rounding stops constraining child sizes; each broker's minimum order value and commission floor do, so keep a "broker minimum order value" parameter per participant.
- At cut-over, switch the price grid in the bands PHP 0.10, 0.50-0.995 and 10-20, and retire the odd-lot book.

## What is not in the public record

- SEC approval and effectivity of One Lot One Share, the new tick table and odd-lot removal; whether the approved text equals the December 2025 draft; how the new engine treats existing GTC/GTD orders when the lot changes.
- The NTE order-entry specification (order types, validities, qualifiers, auction handling, risk controls); the only public statement is "limit orders only on Day 1".
- Which of market-to-limit, GTW, Sliding Validity, FOK, Session, stop and market-on-open/close orders XTS exposes to external FEOMS clients; any PSE broker order-type matrix.
- XTS handling of a market order's unfilled remainder (the approved wording after the November 2014 draft); whether an order above one lot but not a lot multiple is rejected or split.
- Iceberg replenishment priority, and whether an increase in disclosed quantity loses priority.
- Run-off amend/cancel behaviour on XTS (IG and ITCH conflict).
- The Exchange-required per-order value limit, any message-rate limits, self-trade-prevention flags, and any cancel-on-disconnect behaviour.
- Whether XTS applies the tick by reference-price band or by order-price band when the live price crosses an edge.
- Separate tick or lot tables for preferred shares, warrants or REITs, pre-2010 tables, and odd-lot settlement.
