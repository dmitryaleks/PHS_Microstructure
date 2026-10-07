---
number: 6
slug: auctions
title: Opening and Closing Auctions
summary: Call auctions set the open at 09:30:00 and the close at 14:50, then 10 minutes trade at that fixed close; the price rule is published and reproducible, with no random end and no volatility auction.
part: Trading mechanics
---

PSE's auctions are plain call auctions with published rules and no randomness. A 30-minute pre-open (free entry, amendment and cancellation until 09:15, entry only from 09:15) uncrosses at the scheduled 09:30:00; a 5-minute pre-close (cancellation allowed until 14:48) sets the closing price at 14:50.[^pse-approved-rules-vwap-trading-2024:6] The price comes from a five-step equilibrium rule that can be reproduced exactly, and PSE's own six worked examples are used below as test vectors.[^pse-implementing-guidelines-trading-rules:13] No rule or specification describes a random end, an imbalance extension or a volatility auction.

Two behaviours break assumptions carried over from other venues. **The official close is set at 14:50, not at the 15:15 market close.** It is followed by a ten-minute run-off in which every trade is at that fixed price, and then by a 15-minute Closing VWAP session that trades at the day's VWAP and does not change the close. And **the run-off on the current engine rejects an incoming order if a better-priced passive order rests in the book**, while the rule for a pre-close that does not cross is not public.

<div class="callout warn">
<span class="label">Scheduled change: 23 Nov 2026, subject to SEC approval</span>

With the new engine (Nasdaq Eqlipse, "NTE"), PSE proposes (CN-2025-0046, comments closed 31 Dec 2025) to rewrite the run-off rule so that an order at the closing price is accepted and matched against better-priced passive orders at the closing price, and to rename the Closing VWAP session the "Closing VWAP Negotiated Trades Session" with the same 15:00-15:15 slot.[^pse-cn-2025-0046-board-lot-trading-at-last:5][^pse-cn-2026-0031-negotiated-trades:6] The NTE goes live on 23 Nov 2026 (Saturday rehearsals on 31 Oct, 7 Nov and 14 Nov) and **on day 1 only limit orders will be supported**, so market-on-open and market-on-close orders will not be available.[^pse-nte-broker-forum-2026-07-09:9][^pse-nte-faq-2026-08:1] PSE's 17 Aug 2026 slide shows the lot change "For SEC Approval" and Negotiated Trades "Revising per Public Comments"; the run-off change has no separate status, and no approval or effectivity circular had been found by 6 Oct 2026.[^pse-analyst-briefing-1h-2026:9] No change to session times is announced. Whether the auction uncross logic is identical on the NTE is unconfirmed: the consultation presents the run-off as one gap found in PSE's and Nasdaq's gap analysis and proposes no change to the opening or closing price rules, which suggests the uncross logic is expected to be equivalent (inference), but no document says so.[^pse-cn-2025-0046-board-lot-trading-at-last:5] Everything below is the XTS-era rule set.
</div>

## Timeline and permissions

The whole-day schedule below has applied since 1 Mar 2022 (the same pre-close and run-off times first applied on 6 Dec 2021), with the 15:15 close since 1 Mar 2024;[^pse-cn-2022-0009-trading-schedule-mar-2022:1][^pse-cn-2021-0059:1] the full calendar and schedule history are in [Chapter 3](#/ch/sessions). Half-day: pre-open 09:00, no-cancel 09:15, open 09:30, pre-close 11:57, no-cancel 11:59, run-off 12:00, Closing VWAP 12:10, close 12:25.[^pse-approved-rules-vwap-trading-2024:3]

| Time | Rule-level phase | What TPs may do (rule text) | ITCH event: entry / amend-cancel / trading |
|---|---|---|---|
| 09:00 | Pre-Open | Enter, modify or cancel; no matching; orders are processed by the pre-opening algorithm | `S`: Y / Y / N |
| 09:15 | Pre-Open No-Cancel | Enter only | `R`: Y / N / N |
| 09:30:00 | Opening | Opening price calculated; order book frozen; no entry, modification or cancellation | `Q` "The Pre-Open uncross occurs, and continuous trading begins": Y / Y / Y |
| 12:00-13:00 | Market Recess | No trading, entry, modification or cancellation | `A` then `B`: N / N / N then Y / Y / Y |
| 14:45 | Pre-Close | "Same as Pre-Open": enter, modify or cancel | `L`: Y / Y / N |
| 14:48 | Pre-Close No-Cancel | Enter only | `J`: Y / N / N |
| 14:50 | Run-Off/Trading-at-Last | Enter orders at the closing price only | `P` "The Closing Auction uncross occurs, and traders can then enter limit orders for execution at the determined closing price": Y / N / Y* |
| 15:00 | Closing VWAP Session | VWAP transactions only, at VWAP | None: the ITCH specification (v2.3, Oct 2018) predates the session |
| 15:15 | Market Close | End of trading; no entry, modification or cancellation | `M`: N / N / N; timing relative to 15:00 and 15:15 not documented |

Sources: rule text,[^pse-approved-rules-vwap-trading-2024:6] ITCH event table.[^pse-itch-equities-feed-spec-v2-3:10] The Exchange publishes a Trading Schedule message with each event's scheduled time in seconds after midnight.[^pse-itch-equities-feed-spec-v2-3:10][^pse-itch-equities-feed-spec-v2-3:11] PSE's website shows the same table.[^pse-investing-at-pse] Rule text also lets the Exchange change the schedule "as the circumstance warrants".[^pse-approved-rules-vwap-trading-2024:3]

The rules define the "Intervention-Before-Opening/Closing" phase as the latter part of the pre-open or pre-close "where Order modification or cancellation is not allowed",[^pse-revised-trading-rules:9] and the Pre-Open and Pre-Close Periods as the periods when orders "accepted and queued are considered in the determination" of the opening or closing price and "will not trade" until the market opens or moves to the run-off.[^pse-revised-trading-rules:10]

<div class="callout infer">
<span class="label">Inference</span>

No randomised end or extension appears in any rule or in the ITCH specification, so the uncross is treated as deterministic at the scheduled second (09:30:00 and 14:50:00). The opening "freeze" has no separate ITCH state and its duration is not stated in any rule.
</div>

### What can enter an auction

Order-type semantics are in [Chapter 4](#/ch/order-types); this is the auction-specific view.

| Order | In the pre-open and pre-close |
|---|---|
| Limit (Day, GTD, GTC, Sliding) | Allowed, priced inside the static threshold; iceberg (disclosed) quantity allowed, at least 10% of the order and a board-lot multiple; minimum quantity not allowed[^pse-implementing-guidelines-trading-rules:12][^pse-revised-trading-rules:23] |
| Market order | Enterable from Pre-Open; an unfilled market order at the open triggers reservation[^pse-revised-trading-rules:21][^pse-revised-trading-rules:33] |
| Market-on-Opening/Closing | Executable only at the indicative price; the unmatched balance becomes a limit order at that price[^pse-revised-trading-rules:22] |
| Fill-and-Kill | Executed "to the fullest extent possible at the end of Pre-Open/Pre-Close", remainder eliminated; no disclosed quantity with FAK[^pse-revised-trading-rules:23][^pse-implementing-guidelines-trading-rules:12] |
| Market-to-Limit | Not allowed: continuous trading only[^pse-revised-trading-rules:22] |
| Cross orders | Not allowed[^pse-revised-trading-rules:31] |
| Short-sell orders | Rejected in Pre-Open and Pre-Close (since the January 2019 revision)[^pse-short-selling-guidelines-2023-10:2] |
| Odd-lot orders | No auction in the Odd Lot Market[^pse-implementing-guidelines-trading-rules:20] |
| Block sales | May execute from Pre-Open; a block with a pre-determined date executes in the Pre-Open of that date[^pse-implementing-guidelines-trading-rules:25] |
| Foreign buy orders | Earmarked at entry against the available foreign-ownership room, so pre-open foreign bids consume room even before they execute ([Chapter 14](#/ch/foreign-access))[^pse-revised-trading-rules:17] |

The auctions apply to the Normal Market board. Dollar-denominated securities use the same calculation.[^pse-dds-rules:7] ETFs, preferred shares, warrants and SME-board names appear to share the normal-board engine states (the ITCH feed has only Normal, Odd-lot and Index groups, and the Index group carries index values, not orders), and no security-class exemption was found (inference).[^pse-itch-equities-feed-spec-v2-3:9]

### Execution implications

- Commit before 09:15 and 14:48: after those times you can only add orders. The only information-bearing actions in the last 15 minutes of the pre-open and the last 2 minutes of the pre-close are additions, and the indicative price is the only thing to react to.
- Drive the state machine from ITCH system events and the Trading Schedule message, not from wall-clock constants. Last cancel or modify is just before 09:15:00 and 14:48:00.
- Do not send short sales, crosses, market-to-limit or minimum-quantity orders into an auction: the rules do not permit them, and short sales are rejected by the system.
- Avoid market-on-open and market orders in thin names: no indicative price puts the stock into reservation and delays trading (see below). On the NTE's day 1 they will not be supported.
- Foreign buyers: cancel unused pre-open bids before 09:15.
- Short sales cannot join either auction, so short-covering or buy-back exposure can only be hedged in continuous trading and the run-off ([Chapter 9](#/ch/short-selling)).

## The equilibrium-price rule

RTR Art. IV s.10 (in force since 26 Jul 2010) has the system compute the opening price "based on its Reference Price and Orders posted during the Pre-Open Period", through "a determination of all prices which have possible matching, and the volumes that could be matched at each of the prices". "The same algorithm shall apply for Closing Price calculation with the LTP as the Reference Price."[^pse-revised-trading-rules:23][^pse-revised-trading-rules:24] The IG (Part VIII) gives the working rules and six examples.[^pse-implementing-guidelines-trading-rules:12][^pse-implementing-guidelines-trading-rules:13]

### The five steps

Candidate prices are every tick between the lowest offer and the highest bid; prices with no possible match (the IG excludes 870 and 925 in its first example) are not candidates. For each candidate price p:

- buy volume B(p) = all bids at or above p; sell volume S(p) = all offers at or below p;
- matched M(p) = min(B, S); unmatched U(p) = |B - S|.

| Step | Rule | Source |
|---|---|---|
| 1 | The price with the maximum matched volume | RTR s.10, item a |
| 2 | If tied, the price with the least unmatched ("unfilled") quantity | s.10, item b |
| 3 | If tied, market pressure: the side registering the higher volume decides; buy-side pressure takes the highest remaining price, sell-side pressure the lowest | s.10, item c; IG p.14 |
| 4 | If tied (pressure cannot be determined because buy and sell volumes are equal at every remaining price, or are counterbalanced), the price nearest the Reference Price | s.10, item d; IG p.15 |
| 5 | If still tied and the Reference Price is among the remaining prices, the Reference Price | s.10, item e; IG p.16 |

The Reference Price for the open is the previous Closing Price or, when applicable, the Last Adjusted Closing Price (RTR s.6 adds the last traded price or last adjusted close where the security did not trade the previous day). For the close it is the Last Traded Price.[^pse-implementing-guidelines-trading-rules:16][^pse-revised-trading-rules:20] The IG reaches step 5 in its example 5, where the Reference Price is itself one of the remaining candidates; the nearest-price test of step 4 would return the same answer. Step 5 is otherwise only reachable when two candidates are equidistant from an off-grid reference, a corner the rules do not resolve.

### Reference implementation

Limit orders only, prices as integers in ticks or centavos. It reproduces all six IG examples and the two constructed examples below.

```python
def uncross(bids, offers, ref, tick):
    """bids/offers: [(price, qty)]. Returns (price, matched_qty) or None if the book does not cross."""
    if not bids or not offers: return None
    lo, hi = min(p for p, _ in offers), max(p for p, _ in bids)
    if lo > hi: return None
    row = {}
    for p in range(lo, hi + 1, tick):
        buy = sum(q for bp, q in bids if bp >= p)       # all bids at or above p
        sell = sum(q for sp, q in offers if sp <= p)    # all offers at or below p
        row[p] = (min(buy, sell), abs(buy - sell), (buy > sell) - (buy < sell))
    c = list(row)
    c = [p for p in c if row[p][0] == max(row[x][0] for x in c)]     # 1. maximum matched
    c = [p for p in c if row[p][1] == min(row[x][1] for x in c)]     # 2. least unmatched
    if len(c) > 1:                                                   # 3. market pressure
        if all(row[p][2] > 0 for p in c): c = [max(c)]
        elif all(row[p][2] < 0 for p in c): c = [min(c)]
    if len(c) > 1:                                                   # 4. nearest the reference
        d = min(abs(p - ref) for p in c); c = [p for p in c if abs(p - ref) == d]
    price = ref if (len(c) > 1 and ref in c) else c[0]               # 5. the reference price
    return price, row[price][0]
```

Allocation after the price is set (inference; the IG does not describe it): every order trades at the single auction price; orders priced through the auction price fill first, then orders at it by the order-type and price-time ranking of IG VII (market, then MOO/MOC, then limit; time of entry within a type).[^pse-implementing-guidelines-trading-rules:12] Market, MOO and MOC orders have no price, so they add to buy and sell volume at every candidate price (inference). Unmatched limit orders appear to roll into the continuous book with their original priority; no rule describes re-timestamping at the open (inference), and a MOO remainder becomes a limit order at the opening price.[^pse-revised-trading-rules:22]

<div class="callout">
<span class="label">Consequence</span>

The auction price is a deterministic function of the visible book and the reference price, with no random element and no discretion. An execution system can therefore replicate the indicative price tick for tick and test how its own orders would move it before sending them.
</div>

### Worked examples

**Market pressure (IG example 3).** Reference 900, tick 5. Bids 915 x 40,000 and 910 x 10,000; offers 905 x 40,000 and 915 x 20,000.

| Price | Buy volume | Sell volume | Matched | Unmatched |
|---|---|---|---|---|
| 915 | 40,000 | 60,000 | 40,000 | 20,000 |
| 910 | 50,000 | 40,000 | 40,000 | 10,000 |
| 905 | 50,000 | 40,000 | 40,000 | 10,000 |

Step 1 ties at 40,000; step 2 removes 915 (20,000 unmatched); step 3 finds buy pressure at 910 and 905 (50,000 against 40,000) and takes the higher: **910**.[^pse-implementing-guidelines-trading-rules:14]

**A closing auction (constructed; reproduced with the reference implementation).** Last traded price 40.00, tick 0.05. Bids 40.20 x 30,000, 40.10 x 20,000, 39.90 x 50,000; offers 40.00 x 25,000, 40.10 x 20,000, 40.30 x 40,000.

| Price | Buy volume | Sell volume | Matched |
|---|---|---|---|
| 40.20 | 30,000 | 45,000 | 30,000 |
| 40.15 | 30,000 | 45,000 | 30,000 |
| **40.10** | 50,000 | 45,000 | **45,000** |
| 40.05 | 50,000 | 25,000 | 25,000 |
| 40.00 | 50,000 | 25,000 | 25,000 |

Step 1 alone decides: **closing price 40.10**, 45,000 shares. The 40.20 bid fills 30,000 and 15,000 of the 20,000 at the 40.10 bid fill; both offers fill (the 40.00 offer sells at 40.10). The 5,000 left on the 40.10 bid stay in the book, so a 5,000 sell at 40.10 in the run-off would trade at the closing price. The 39.90 bid and the 40.30 offer are untouched. A second book (last traded price 40.10; bids 40.20 x 10,000 and 39.90 x 5,000; offers 40.00 x 10,000 and 40.30 x 7,000) matches 10,000 with zero imbalance at every price from 40.00 to 40.20, so step 4 returns the reference: **40.10**.

**PSE's six examples** (IG VIII; tick 5; non-crossing orders omitted where they do not affect a candidate; reproduced exactly by the reference implementation):[^pse-implementing-guidelines-trading-rules:13][^pse-implementing-guidelines-trading-rules:14][^pse-implementing-guidelines-trading-rules:15][^pse-implementing-guidelines-trading-rules:16]

| Example | Book (bids; offers) | Reference | Result | Deciding step |
|---|---|---|---|---|
| 1 | 920 x 5,000, 905 x 50,000, 900 x 72,500; 900 x 134,000, 905 x 1,000, 925 x 15,000 | 910 | **900** (matched 127,500 against 55,000 at 905 and 5,000 at 920-910) | 1: maximum matched |
| 2 | 905 x 10,000, 900 x 7,000; 900 x 10,000, 905 x 1,000 | 910 | **905** (10,000 matched at both; 1,000 against 7,000 unmatched) | 2: least unmatched |
| 3 | 915 x 40,000, 910 x 10,000; 905 x 40,000, 915 x 20,000 | 900 | **910** | 3: market pressure (buy) |
| 4.1 | 910 x 10,000, 895 x 1,000; 900 x 10,000, 925 x 16,000 | 890 | **900** (910, 905, 900 all 10,000 matched, 0 unmatched) | 4: nearest the reference |
| 4.2 | 905 x 10,000, 900 x 1,000; 900 x 10,000, 905 x 1,000 | 890 | **900** (905 has sell pressure, 900 buy pressure: counterbalanced) | 4: nearest the reference |
| 5 | 920 x 10,000, 900 x 1,000; 900 x 10,000, 920 x 1,000 | 915 | **915** (920 and 900 eliminated at step 2; 915, 910, 905 remain with equal volumes) | 5: the reference price |

### Execution implications

- The rule maximises matched volume, so a large marketable limit order moves the indicative price up the supply curve until matched volume stops rising. Model the indicative price exactly with the function above and test it against the ITCH `I` stream.
- When matched and unmatched volumes tie, market pressure pushes the price to the heavier side (buy-heavy gives the highest tied price). When there is no imbalance at all, the price falls back to the reference: previous close at the open, last traded price at the close. A zero-imbalance book anchors to the reference.
- Unspecified details to validate in UAT: allocation among orders at the auction price, whether iceberg hidden quantity counts in the uncross, the candidate grid when ticks change across a price band, and step 5 when two candidates are equidistant from an off-grid reference.

## Indicative price dissemination

The ITCH Indicative Price/Quantity message (`I`) carries the Theoretical Auction Quantity ("total quantity eligible to be matched at the current Theoretical Auction Price"), best bid, best offer, Theoretical Auction Price and an Auction Type: `O` Opening Auction (pre-open), `I` Intra-day Auction (halt), `C` Closing Auction (pre-close).[^pse-itch-equities-feed-spec-v2-3:17][^pse-itch-equities-feed-spec-v2-3:18] It is part of the Total View feed, not Basic.[^pse-itch-equities-feed-spec-v2-3:22][^pse-itch-equities-feed-spec-v2-3:23]

- Throughout the pre-open the feed sends Add Order, Order Delete, Indicative Price/Quantity and Orderbook Trading Action messages. The start-of-day reference price is an Add Order with order number and quantity both zero.[^pse-itch-equities-feed-spec-v2-3:27]
- Opening-auction fills arrive as one Order Executed With Price message per executed order, and so do executions on thawing after a freeze; the Trade message is not used for them. The specification does not describe the closing uncross separately.[^pse-itch-equities-feed-spec-v2-3:27][^pse-itch-equities-feed-spec-v2-3:28]
- The closing price is published as a Trade message with executed quantity and match number both zero, sent immediately after the `P` event.[^pse-itch-equities-feed-spec-v2-3:18][^pse-itch-equities-feed-spec-v2-3:27]
- Whether retail users and data vendors see the indicative price is not shown on PSE's public pages. The NTE feed specifications are available on request only.[^pse-new-trading-engine]

Subscribe to the `I` stream for pre-open and pre-close decisions; ITCH Basic is not sufficient for auction logic.

**The opening price in the end-of-day file.** PSE's end-of-day price file defines the Opening Price as the "price of the security at market open or price at which the security was first traded for a given day".[^pse-quote-file-eod-spec-2014:1] If the pre-open does not cross, the first continuous trade therefore becomes the open (inference).

## Reservation

The rules contain no imbalance extension. PSE's analogue is **reservation**, a call-auction-style hold. A security is reserved when (i) a market-on-opening order is posted but there is no indicative opening price, (ii) a market order is unfilled at the open, or (iii) the indicative opening price breaches the static threshold; it is also reserved manually before a trading suspension is lifted. Orders other than crosses can still be posted, modified and cancelled during reservation.[^pse-revised-trading-rules:33][^pse-implementing-guidelines-trading-rules:26] Where a suspension is cured after 4 pm, the IG halt and suspension matrix prescribes 50 minutes of suspension followed by a 10-minute reservation before trading resumes; an earlier cure resumes in the Pre-Open of the corresponding day.[^pse-implementing-guidelines-trading-rules:28] The November 2014 XTS draft kept the three triggers and added automatic cancellation of a market-on-opening or closing order when no indicative price exists; whether the SEC-approved text matches is not public.[^pse-memo-revisions-trading-rules-consultation-2014:8][^pse-memo-revisions-trading-rules-consultation-2014:4]

The duration and exit procedure of an automatic reservation are a Market Control action and are not specified. No reservation trigger is listed for the close; instead any order that breaches the dynamic threshold in the five minutes before the Pre-Close is rejected rather than reviewed.[^pse-implementing-guidelines-trading-rules:26] Threshold levels, freezing and halts are in [Chapter 7](#/ch/price-controls).

## The pre-close and the official closing price

"Closing Price shall mean the price determined during the Pre-Close Period."[^pse-revised-trading-rules:8] The pre-close runs 14:45-14:50 (entry, modification and cancellation until 14:48, entry only afterwards), uses the same five-step rule and takes the last traded price as reference.[^pse-approved-rules-vwap-trading-2024:6][^pse-implementing-guidelines-trading-rules:16] The price is published as the Trade message described above. The VWAP rules exclude block sales and intentional crosses from the VWAP computation,[^pse-approved-rules-vwap-trading-2024:7] but no document says whether they update the last traded price used as the closing reference; the daily report shows block prints outside the stock's own open, high, low and close ([Chapter 5](#/ch/matching)).

**What the close is used for.** It is the next day's Reference Price (RTR s.6), the basis of adjusted closing prices after corporate actions,[^pse-revised-trading-rules:20] and the "Day Close" in PSE's end-of-day price file ("If there is no trade for the day, Day Close has no value").[^pse-quote-file-eod-spec-2014:1] PSE's index policy says only that indices use "actual last traded prices"; how the closing auction price feeds the index close is not described ([Chapter 11](#/ch/market-data)).[^pse-index-policy-2024:13]

<div class="callout infer">
<span class="label">Inference</span>

**The closing price when the pre-close does not cross.** No PSE document says what the closing price is if the 14:45-14:50 book does not cross. The closing algorithm's reference is the last traded price, and the end-of-day file leaves Day Close empty only when there was no trade at all, so the working assumption is closing price = the day's last traded price, and no close if there was no trade. Treat as unverified. PSE's two illustrations of the NTE run-off change do not settle it: the January 2026 broker-forum deck shows a closing price of 10.00 equal to the day's only trade (13:30, 1,000 shares at 10.00) in a non-crossing book (bids 8.90 and 8.80, offer 9.00), consistent with a last-traded-price fallback; CN-2025-0046 shows the same book with the 13:30 trade at 10.24 and a closing price of 10.00, which is not.[^pse-nte-user-group-2026-01-15:12][^pse-cn-2025-0046-board-lot-trading-at-last:6]
</div>

<div class="callout">
<span class="label">Consequence</span>

The official close is struck at 14:50: ten minutes before the last ordinary order and twenty-five minutes before the market closes. Nothing that trades after 14:50 can change it. To influence or match the close you must be in the 14:45-14:50 call; to trade at it afterwards you use the run-off.
</div>

### Execution implications

- To control the official close (an index or ETF benchmark), participate in the 14:45-14:50 auction. Use limit orders priced to guarantee participation: the run-off cannot change the price, and orders added after 14:48 cannot be cancelled. PSE lengthened the pre-close in 2013 partly because ETFs and index funds "are mostly benchmarked against the close price".[^pse-memo-extended-pre-close-consultation-2013:2]
- Because the run-off executes at a price fixed ten minutes earlier, the pre-close is the only venue where a trader can establish the official close; run-off flow cannot move it.
- Closing-auction price risk is real: size participation conservatively and prefer the run-off for residuals when the closing price is acceptable ([Chapter 15](#/ch/empirical)).

## The run-off period

"All Orders during the Run-Off/Trading-at-Last Period are executed only at the Closing Price. In cases where prices of posted Orders in the Order book are better than the Closing Price, no Orders will be accepted by the Trading System." (RTR Art. IV s.18, unchanged since 2010 and still the "current rule" in PSE's December 2025 consultation.)[^pse-revised-trading-rules:27][^pse-cn-2025-0046-board-lot-trading-at-last:8] The run-off lasts from 14:50 to 15:00.[^pse-approved-rules-vwap-trading-2024:6] Crosses in the run-off must be at the closing price,[^pse-revised-trading-rules:31] and block sales may execute up to the run-off ([Chapter 5](#/ch/matching)). The wording of the permitted order types appears in four versions:

| Source | Text for the run-off |
|---|---|
| IG, 26 Jul 2010 | "Limit Orders at the Closing Price only or Market Orders but matching is executed only at the Closing Price for both Order types"[^pse-implementing-guidelines-trading-rules:4] |
| TPA 2011-0124, for 2 Jan 2012 | "Limit Orders at the Closing Price only"[^pse-tpa-2011-0124-amended-implementing-guidelines:3] |
| TPA 2013-0185, from 4 Nov 2013 | Back to limit or market orders, matching only at the closing price[^pse-tpa-2013-0185-extended-pre-close:7] |
| CN-2024-0010, 1 Feb 2024 | "TPs can enter Orders at the Closing Price only"[^pse-approved-rules-vwap-trading-2024:6] |

The XTS ITCH description of the run-off mentions limit orders only (inference: market orders are not accepted there).[^pse-itch-equities-feed-spec-v2-3:10] The October 2023 short-selling guidelines bar short-sell orders in the Pre-Open and Pre-Close only; PSE's older SBL web page still lists the run-off, so design for no short orders there unless a broker confirms otherwise ([Chapter 9](#/ch/short-selling)).[^pse-short-selling-guidelines-2023-10:2]

<div class="callout warn">
<span class="label">Conflict: can orders be amended or cancelled in the run-off?</span>

The IG says TPs may cancel active orders during the Trading-at-Last/Run-Off Period (2010 text) and, after the December 2011 amendment, "from Pre-Open Period to Trading-at-Last Period, except during the Pre-Open No-Cancel Period, Pre-Close No-Cancel Period and Market Recess".[^pse-implementing-guidelines-trading-rules:18][^pse-tpa-2011-0124-amended-implementing-guidelines:3] The ITCH state table says order amend and cancel are **not** allowed in the `P` (Trading At Last) state.[^pse-itch-equities-feed-spec-v2-3:10] The proposed NTE text says run-off orders "can be entered, modified, and executed only at the Closing Price".[^pse-cn-2025-0046-board-lot-trading-at-last:8] Unresolved from public documents. Design for no-cancel.
</div>

<div class="callout infer">
<span class="label">Inference</span>

The XTS rejection rule can bind only when the closing price is not itself an auction price. After a genuine uncross at price P, no resting bid above P and no resting offer below P can remain, because such an order would have raised the matched volume or won the tie-break at a better price. So a "better-priced passive order" exists at 14:50 essentially only when the pre-close did not cross and the close fell back to the last traded price. That is the case in both PSE illustrations (closing price 10.00, offer at 9.00). In a thin name with a stale last trade, run-off liquidity may therefore be nil.
</div>

**Planned NTE change.** PSE and Nasdaq's gap analysis found that "PSEtrade XTS automatically rejects an incoming order during the Run-Off/Trading-at-Last period if the price of the counterpart passive order in the order book is better than the established Closing Price", whereas with Eqlipse "the incoming order will be accepted by the trading engine provided it is at the Closing Price, and the counterpart passive order will be matched with the incoming order at the Closing Price".[^pse-cn-2025-0046-board-lot-trading-at-last:5] Scenario 1: closing price 10.00, resting offer 9.00 x 2,000, incoming buy 2,000 at 10.00; today rejected, proposed to execute 2,000 at 10.00. Scenario 2 mirrors it for a resting bid at 11.00 and an incoming sell at 10.00.[^pse-cn-2025-0046-board-lot-trading-at-last:6][^pse-cn-2025-0046-board-lot-trading-at-last:7] The draft carries over the second sentence of s.18 unchanged ("no Orders will be accepted"), which contradicts the scenarios; the final approved text is not public.[^pse-cn-2025-0046-board-lot-trading-at-last:8] Under the draft the passive side gets price improvement (a resting offer at 9.00 sells at 10.00) while the aggressor gets none.

### Execution implications

- Check the book state at 14:50 before relying on run-off liquidity: on XTS an incoming order that would trade against a better-priced passive order is rejected. Under the draft NTE rule you could trade the residual at the closing price.
- The run-off is a fixed-price venue: zero tracking error against the official close, with only fill uncertainty. Pair it with the auction rather than treating it as price discovery.
- Code both behaviours behind the engine/rule-set switch ([Chapter 16](#/ch/execution-implications)).

## The Closing VWAP session

Since **1 Mar 2024** the market closes at 15:15 rather than 15:00, with a Closing VWAP session in 15:00-15:15 (half-day 12:10-12:25). The SEC-approved VWAP Trading Rules (CN-2024-0010, 1 Feb 2024) "take effect immediately"; PSE announced the launch on 1 Mar 2024 on 15 Feb 2024.[^pse-approved-rules-vwap-trading-2024:1][^pse-cn-2024-0012-vwap-go-live:1]

| Parameter | Rule |
|---|---|
| Window | Only "within fifteen (15) minutes after the Run-off/Trading-at-Last Period"[^pse-approved-rules-vwap-trading-2024:7] |
| Price | The Exchange-computed full-day VWAP, at most 4 decimals; all trades are included except block sales, intentional crosses and odd-lot transactions[^pse-approved-rules-vwap-trading-2024:7] |
| Minimum value | PHP 500,000[^pse-approved-rules-vwap-trading-2024:7] |
| Parties | A single TP only; a two-firm facility is reserved for a later date and SEC approval[^pse-approved-rules-vwap-trading-2024:7] |
| Securities | Not for a currently suspended or halted security[^pse-approved-rules-vwap-trading-2024:4] |
| Controls | Only authorised salesmen or traders; the TP's per-order value limit applies[^pse-approved-rules-vwap-trading-2024:4] |
| Settlement | "Based on Clearing Agency Rules"[^pse-approved-rules-vwap-trading-2024:4] |
| Disruption | If the VWAP display is delayed the session is suspended; resumed if at least 5 minutes remain, otherwise VWAP trading is cancelled for the day[^pse-approved-rules-vwap-trading-2024:7] |
| Reporting | Included in end-of-day reports[^pse-approved-rules-vwap-trading-2024:7] and in the headline grand total[^pse-eod-daily-quotation-2026-10-02:12] |

The session is a separate execution venue that does not alter the close: it trades at a price computed from the day's trades. Use it for benchmark-VWAP mandates, not for the close. PSE says the planned Negotiated Trades facility will be web-based "similar to the VWAP facility", which implies VWAP trades are not entered through FIX order entry (inference).[^pse-nte-faq-2026-08:1]

**Usage.** Computed from PSE's Daily Quotation Reports, 2 Jan to 2 Oct 2026: VWAP trades occurred on 67 of 186 days and made up 0.12% of headline value.[^pse-dqr-2026-ytd-block-parse] The VWAP of a thin security can rest on a handful of shares. On 2 Oct 2026 the regular market in GLO PREF ANV (GLOBA) traded 10 shares at 1,944 (PHP 19,440), and the VWAP session then executed 3,750 shares at 1,944.00, PHP 7.29m.[^pse-eod-daily-quotation-2026-10-02:8][^pse-eod-daily-quotation-2026-10-02:11]

### Execution implications

- A VWAP print is neither a way to hit the close nor a way to move it. For close-benchmarked mandates the auction is the capture point.
- Thin names: a VWAP built on very little volume is cheap to influence, which raises market-conduct exposure around the VWAP ([Chapter 13](#/ch/regulatory-constraints), inference).
- Under the draft NTE rules Negotiated Trades share the same 15-minute window.

## Choosing a closing venue

A design guide built from the rules above, not rule text. The four venues differ in what they fix, when they trade and what can go wrong.

| Goal | Venue and window | What fixes the price | Main risk |
|---|---|---|---|
| Participate in setting the official close | Pre-close call, 14:45-14:50 (cancel until 14:48) | The five-step rule on the whole book | Price moves against a passive limit; no cancel after 14:48 |
| Trade at the official close once it is known | Run-off, 14:50-15:00, limit orders at the closing price | The closing price struck at 14:50 | Fill uncertainty; on XTS rejection if a better-priced passive order rests, which happens when the close did not come from a cross |
| Match the full-day VWAP | Closing VWAP session, 15:00-15:15, at least PHP 500,000, one TP | The Exchange's VWAP, excluding blocks, crosses and odd lots | Thin names: a VWAP built on a few shares; broker facility, not FIX |
| Pre-arranged size within ±5% of VWAP | Proposed Negotiated Trades, same window | Agreed price inside the VWAP band | Not in force; subject to SEC approval |

## History of the closing mechanism

| Date | Event |
|---|---|
| 23 Dec 1997 | Circular 248-97 "Updated and Consolidated Trading Rules": a digest.ph preview shows articles on opening-price calculation, cross transactions and special block sales; the text, and the pre-2010 closing-price method, could not be retrieved.[^digest-ph-pse-circular-248-97] |
| 1 Jun 2010 / 26 Jul 2010 | The SEC approves the RTR (letter of 1 Jun 2010); they take effect with the new trading system on 26 Jul 2010. The Pre-Close is introduced at 3 minutes "in consideration of the Exchange's half day trading" (pre-close 11:57-11:59, no-cancel 11:59-12:00, run-off 12:00-12:10).[^pse-revised-trading-rules:1][^pse-implementing-guidelines-trading-rules:1][^pse-memo-extended-pre-close-consultation-2013:1][^pse-implementing-guidelines-trading-rules:4] |
| 2 Jan 2012 | Whole-day trading with SEC-approved amendments (letter of 25 Oct 2011): pre-close 15:17-15:19, no-cancel 15:19-15:20, run-off 15:20-15:30, close 15:30.[^pse-memo-new-trading-hours-2011:1][^pse-tpa-2011-0124-amended-implementing-guidelines:2][^pse-tpa-2011-0110-amended-revised-trading-rules:2] |
| 4 Nov 2013 | Pre-close lengthened from 3 to 5 minutes (Board 10 Jul 2013; SEC letter 26 Sep 2013): auction 15:15-15:18, no-cancel 15:18-15:20, run-off 15:20-15:30. PSE had "the shortest pre-close period in the region" (Bursa Malaysia 5 minutes, SGX 6, SET 10, IDX 10, HoSE 15) and wanted TPs able "to assess and counter a sharp price move at the close".[^pse-memo-extended-pre-close-consultation-2013:1][^pse-tpa-2013-0185-extended-pre-close:10][^pse-tpa-2013-0185-extended-pre-close:9] |
| 22 Jun 2015 | Engine migration from NSC to PSEtrade XTS; the closing-auction and trading-at-last states carry over (ITCH `L`, `J`, `P`).[^pse-annual-report-2015:42][^pse-itch-equities-feed-spec-v2-3:10] |
| 19 Mar 2020 to 3 Dec 2021 | Shortened hours: pre-close 12:45, run-off 12:50, close 13:00.[^pse-cn-2020-0025-resumption-of-trading:1] |
| 6 Dec 2021 | Whole-day schedule reset: pre-close 14:45, run-off 14:50, close 15:00 (circular of 22 Nov 2021). The 14:48 pre-close no-cancel phase is listed explicitly from 1 Mar 2022.[^pse-cn-2021-0059:1][^pse-cn-2022-0009-trading-schedule-mar-2022:1] |
| 1 Mar 2024 | Closing VWAP session 15:00-15:15; market close moves from 15:00 to 15:15.[^pse-approved-rules-vwap-trading-2024:3] |
| 15 Dec 2025 and 1 Jul 2026 (proposals) | Run-off rewrite (with the NTE); Closing VWAP Negotiated Trades Session.[^pse-cn-2025-0046-board-lot-trading-at-last:8][^pse-cn-2026-0031-negotiated-trades:6] |

## Marking the close

"Marking the close" ("buying and selling securities at the close of the market in an effort to alter the closing price") is listed prohibited conduct in the 2015 SRC IRR alongside wash sales and improper matched orders,[^sec-2015-src-irr:68] and CMIC's rules reach bids or offers "at or near the close of the market, whether matched/executed or not".[^pse-cmic-rules:117] The structure of the close limits the opportunity: a call auction sets the price rather than the last trade, the last two minutes of the pre-close cannot be cancelled, run-off executions cannot move the price, short sales are barred in the pre-close,[^pse-short-selling-guidelines-2023-10:2] and orders that breach the dynamic threshold just before the pre-close are rejected.[^pse-implementing-guidelines-trading-rules:26] Enforcement and surveillance detail is in [Chapter 13](#/ch/regulatory-constraints).

Closing-auction participation is legitimate to achieve the close and problematic to set it. Where a mandate's value depends on the close, log the intent and size per child order, and treat cancelled orders near the close as regulated too.

## No volatility auction

PSE has no scheduled intraday auction and no price-triggered volatility auction. Its substitutes are the freeze (Market Control validates or rejects an order that would breach a threshold, normally within five minutes), reservation as above, and halts during which orders keep accumulating.[^pse-implementing-guidelines-trading-rules:26] The XTS engine models a halt as an "Intra-day Auction": the indicative message carries Auction Type `I`, and lifting the halt returns the book to normal trading.[^pse-itch-equities-feed-spec-v2-3:18][^pse-itch-equities-feed-spec-v2-3:26] The rules do not describe an uncross algorithm for a halt or reservation, and the specification does not say whether an uncross runs when a halt is lifted; if one does, assume the same five-step rule (inference). A large aggressive order therefore freezes the book rather than calling an auction. Thresholds, halts and circuit breakers are in [Chapter 7](#/ch/price-controls); note that the circuit-breaker cut-offs were written against the old 15:15 pre-close (level 1 until 14:55, level 2 until 14:40, level 3 until 14:10) and have not been restated for the 14:45 pre-close, and the circular describes no reopening auction.[^pse-cn-2020-0044:2]

## What is not in the public record

- The closing price when the pre-close does not cross (last traded price versus previous close versus VWAP), and whether block sales or intentional crosses update the last traded price used as the closing reference.
- Whether orders can be amended or cancelled in the run-off on XTS (the IG and the ITCH state table disagree).
- How market, MOO and MOC volume enters the candidate grid when one side has only unpriced orders; whether iceberg hidden quantity counts in the uncross; allocation among orders at the auction price (time priority is implied, pro-rata is not mentioned).
- The duration and exit procedure of an automatic reservation, and whether retail users or vendors see the indicative price.
- The final SEC-approved run-off text (the draft keeps a contradictory sentence) and whether the NTE auction logic is equivalent to XTS; the NTE specifications are not public.
- Published statistics on the closing auction's share of volume, and any enforcement case for closing-price manipulation within the sources reviewed.
- How the closing auction price feeds the PSEi close, and when the ITCH `M` event is sent relative to the Closing VWAP session.
