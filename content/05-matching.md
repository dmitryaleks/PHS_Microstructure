---
number: 5
slug: matching
title: Matching, Block Sales and Crosses
summary: Price-time matching with no self-trade prevention, and how pre-arranged size routes to crosses, block sales or (proposed) negotiated trades; block sales were 18.4% of 2026 turnover value.
part: Trading mechanics
---

PSE's central limit order book is simple: strict price-then-time priority, trades at the resting order's price, no size, pro-rata or broker tier. Three behaviours still break assumptions carried over from other venues. First, **there is no self-trade prevention**. Instead, RTR Art. VI s.2 gives a Trading Participant (TP) that posts a counterpart order at the same or better price priority to match it against its own earlier order *regardless of queue position*.[^pse-revised-trading-rules:31] Second, **a pre-arranged trade does not choose its venue**: anything that qualifies as a block sale (PHP 20 million, within ±5% of the previous close) must go through the Block Sale Market and not through a cross,[^pse-implementing-guidelines-trading-rules:23] and block prints sit outside the stock's own open, high, low, close and volume yet inside headline turnover. They were 18.4% of value in 2026 to 2 October (computed from PSE's daily reports).[^pse-dqr-2026-ytd-block-parse] Third, nothing on the exchange handles a small pre-arranged trade priced outside the best bid and offer; that is the gap the proposed Negotiated Trades facility targets.[^pse-cn-2026-0031-negotiated-trades:3]

The rules in force are the SEC-approved June 2010 Revised Trading Rules (RTR) and Implementing Guidelines (IG), effective with the new trading system on 26 Jul 2010 and amended piecemeal since,[^pse-implementing-guidelines-trading-rules:1] running on PSEtrade XTS since 22 June 2015.[^pse-annual-report-2015:42] PSE publishes no consolidated current text.[^pse-regulation-trading-participants] Article numbers have also drifted: Cross Transactions and Block Sale are Art. VI in the 2010 base text,[^pse-revised-trading-rules:31] but the 2024 VWAP rules inserted a new "Article VI" and the July 2026 draft calls Cross, Block and Negotiated Trades "Article VII".[^pse-approved-rules-vwap-trading-2024:4][^pse-cn-2026-0031-negotiated-trades:7] Section references below use the base-text numbering.

<div class="callout warn">
<span class="label">Scheduled change: 23 Nov 2026, subject to SEC approval</span>

PSE's new engine (Nasdaq Eqlipse, "NTE") is scheduled for a big-bang go-live on 23 Nov 2026 (Saturday rehearsals on 31 Oct, 7 Nov and 14 Nov); on day 1 **only limit orders will be supported**.[^pse-nte-faq-2026-08:1][^pse-nte-broker-forum-2026-07-09:9] Rule changes tied to it that touch this chapter: lot size of one share with the Odd Lot Market abolished,[^pse-cn-2025-0046-board-lot-trading-at-last:5] and a new Negotiated Trades facility.[^pse-cn-2026-0031-negotiated-trades:3] PSE's 17 Aug 2026 status slide shows One Share, One Lot as "For SEC Approval" and Negotiated Trades as "Revising per Public Comments".[^pse-analyst-briefing-1h-2026:9] No approval or effectivity circular had been found by 6 Oct 2026. No change to the cross or block-sale rules has been announced. Everything below is the XTS-era rule set unless a section says "proposed". The NTE order-entry and market-data specifications are distributed only on request, so self-trade handling and trade flags on the NTE are unconfirmed.[^pse-new-trading-engine]
</div>

## Continuous matching

Continuous trading is the period "when matching of Orders at the Best Price takes place".[^pse-revised-trading-rules:10] The matching rule is one sentence: "Except for Block Sales, the Trading System shall match Orders at the Best Price."[^pse-revised-trading-rules:24]

| Item | Rule |
|---|---|
| Priority between order types | 1. Market order; 2. Market-on-Opening/Closing order; 3. Limit order[^pse-implementing-guidelines-trading-rules:12] |
| Priority within a type | Market and MOO/MOC orders by time of entry; limit orders first by price (higher bid, lower offer), then by time of entry[^pse-implementing-guidelines-trading-rules:12] |
| Trade price | The resting (passive) order's price; limit orders execute "at the entered limit price or better"[^pse-revised-trading-rules:21] |
| Price improvement | None found beyond the resting-price rule: no mid-point, hidden-liquidity or odd-lot improvement mechanism appears in any PSE rule document. The one structural exception is the run-off, where every execution is at the closing price ([Chapter 6](#/ch/auctions)) |
| Partial fills | The order stays Active; its unmatched portion can still be modified or cancelled[^pse-implementing-guidelines-trading-rules:17][^pse-implementing-guidelines-trading-rules:18] |
| Size, pro-rata, broker tiers | None: no such provision appears in the rules |
| Per-order value limit | Set by the TP per trader and capped by the Exchange's limit; applies per order, not per day; the block-sale facility observes it too[^pse-implementing-guidelines-trading-rules:17] |
| Price controls | An order that would breach a threshold freezes the security for up to five minutes; intermediate trades inside the dynamic threshold stand, and orders at the BBO or crosses beyond it are auto-accepted ([Chapter 7](#/ch/price-controls))[^pse-implementing-guidelines-trading-rules:26] |

What keeps or loses queue position is set out in [Chapter 4](#/ch/order-types). The short version: a volume decrease, a validity-type change or an account-code change keeps priority; a volume increase, a limit-price change or a trigger-price change loses it.[^pse-implementing-guidelines-trading-rules:18] The XTS FIX specification repeats the price and quantity-increase rule and says the exchange order id may change after an amendment.[^pse-fix-specification-v2-5:25-26]

### Execution implications

- Model the book as pure price-time. Queue position is lost on a price change or a size increase and kept on a size decrease, so prefer "reduce" over "re-price" when position has value.
- Do not model price improvement for aggressive orders: you pay the resting price. Market-order and limit-order semantics are in [Chapter 4](#/ch/order-types).
- Size child orders so that a sweep cannot breach the dynamic threshold against the last traded price, or accept the freeze review risk ([Chapter 7](#/ch/price-controls)).
- Multi-day orders do not survive every day: the Exchange cancels active orders on corporate actions that adjust the closing price, on a board-lot change and on cash- or property-dividend ex-dates, so GTC and GTD orders must be re-entered ([Chapter 4](#/ch/order-types)).[^pse-revised-trading-rules:25]

## No self-trade prevention and the automatic cross

PSE has no self-trade-prevention rule and the XTS FIX order-entry specification carries no self-trade-prevention flag.[^pse-fix-specification-v2-5:15][^pse-fix-specification-v2-5:16] What exists instead is RTR Art. VI s.2, "Automatic Cross Transactions".

> There shall be an automatic cross during the Market Open/Continuous Trading and Trading-at-Last/Run-Off Period when a Trading Participant has a posted Order and then posts another counterpart Order at the same or better price. In such event, the Trading Participant shall have the priority among Trading Participants who posted earlier in the queue. The newly posted counterpart Order shall be matched with its earlier posted Order regardless of its position in the queue.[^pse-revised-trading-rules:31]

Related facts:

- All FIX users of one firm receive execution reports for each other's orders.[^pse-fix-itch-session-week01-2014-10-03:6]
- The ITCH Trade Indicator `C` marks an "intentional cross trade (the same user simultaneously entered both sides of the trade)". Intentional crosses, block sales and manual (Market Control) trades are published through the Trade message, not through the Order Executed messages.[^pse-itch-equities-feed-spec-v2-3:18][^pse-itch-equities-feed-spec-v2-3:28]
- Wash trades and matched orders are unlawful: SRC s.24.1(a) bars transactions involving "no change in the beneficial ownership" and orders entered with knowledge that a simultaneous order of substantially the same size, time and price will be entered,[^ra-8799-src:24] and the 2015 IRR lists wash sales, improper matched orders, painting the tape and marking the close as examples.[^sec-2015-src-irr:68] CMIC surveillance (a Korea Exchange system) polices this ([Chapter 13](#/ch/regulatory-constraints)).[^pse-investing-at-pse]

<div class="callout infer">
<span class="label">Inference</span>

The automatic cross is a broker-level internalisation priority: if TP A holds an earlier resting buy and later sends a sell at the same or better price, the sell hits A's own buy first, ahead of other TPs' earlier orders at that price. The text is written at the level of the TP, not the beneficial owner, so two clients of one broker, or a client and the broker's own book, can be matched by it. The rule does not say how it interacts with strictly better-priced orders of other TPs (price priority should still dominate), nor whether a TP's client and proprietary accounts can auto-cross. Test in UAT before relying on it.
</div>

### Execution implications

- Build self-trade prevention yourself. Your algorithm must not trade against its own resting orders across child orders, strategies, accounts or brokers; the exchange will not stop it, and SRC s.24 applies to the outcome.
- Offsetting orders routed through one broker can be matched by the automatic cross (inference from the rule's TP-level wording). Check mandate and fund cross-trade constraints before sending offsetting flow through a single TP.
- Expect lower passive fill probability at the touch in names where a large broker holds offsetting client flow: that broker can internalise ahead of earlier queue positions. Information about your order is also visible to the broker's other desks.

## Crosses

### Definition and conditions

A cross transaction is one "where the same Broker executes buying and selling Orders of different clients or its proprietary account for different beneficial Owners for the same Security and at the same price and quantity".[^pse-revised-trading-rules:9] The Cross Order type is buying and selling orders of the same TP "simultaneously executed at the agreed quantity and price within the BBO".[^pse-revised-trading-rules:22] RTR Art. VI s.1 sets five conditions:[^pse-revised-trading-rules:31]

1. Its price shall be within the BBO.
2. In the absence of a BBO, the price shall observe "the limitations set out in the Implementing Guidelines" (the IG's table of contents has no cross-transaction part, and no such text was located).[^pse-implementing-guidelines-trading-rules:2]
3. It shall not be entered during the Pre-Open/Pre-Close Period.
4. When done in the Run-Off/Trading-at-Last Period, it shall be at the Closing Price.
5. All pre-arranged transactions meeting the Exchange's requirements shall be executed in the Block Sale Market and not through a Cross Order entry.

PSE restated the consequence on 1 Jul 2026: a pre-arranged transaction below the block minimums "cannot be executed in the Block Sale Market but may be entered as a cross transaction in the regular market, provided the execution price is within the best bid and offer". There is "presently no execution facility" for trades that miss the block value threshold and are priced outside the BBO.[^pse-cn-2026-0031-negotiated-trades:3]

### Where a cross can be entered

| Phase or state | Cross allowed? | Price rule |
|---|---|---|
| Pre-Open (09:00-09:30), Pre-Close (14:45-14:50) | No[^pse-revised-trading-rules:31] | n/a |
| Continuous trading (09:30-12:00, 13:00-14:45) | Yes | Within the BBO[^pse-revised-trading-rules:31] |
| Run-Off/Trading-at-Last (14:50-15:00) | Yes | At the Closing Price[^pse-revised-trading-rules:31] |
| Market Recess (12:00-13:00) | No: TPs cannot enter orders[^pse-approved-rules-vwap-trading-2024:6] | n/a |
| Closing VWAP Session (15:00-15:15) | No: only VWAP transactions[^pse-approved-rules-vwap-trading-2024:6] | n/a |
| Security reserved or halted | No: crosses are the one order type blocked; other orders can still be posted, modified and cancelled[^pse-implementing-guidelines-trading-rules:26][^pse-implementing-guidelines-trading-rules:27] | n/a |
| Cross that breaches the dynamic threshold | Auto-accepted by Market Control[^pse-implementing-guidelines-trading-rules:26] | n/a |
| Odd Lot Market | Yes, on the same rules[^pse-implementing-guidelines-trading-rules:20] | As Normal Market |
| Deal that is block-eligible | No: must use the Block Sale Market | n/a |

**Engine mechanics (XTS).** FIX uses the New Order Cross message: CrossType 1 (Cross AON), CrossPrioritization 0 (none), two sides carrying the same quantity, each with its own executing trader and account and an optional Giveup Clearing Firm, OrdType 2 (Limit) with a price, and TimeInForce 3 (IOC).[^pse-fix-specification-v2-5:16][^pse-fix-specification-v2-5:17] Intentional crosses are excluded from the VWAP computation,[^pse-approved-rules-vwap-trading-2024:7] and block sales and cross trades "of the same flag" are netted out of the SCCP clearing-fund contribution base.[^sccp-clearing-house-rules-2018:33] On the NTE, crosses are to be identified by a Cross Indicator field in the Order Executed With Price and Trade messages.[^pse-nte-faq-2026-08:3]

### Client priority, give-up and done-through

- **Client before proprietary.** SEC IRR Rule 34.1.2 ("Customer First"): "The Dealer-Broker shall give priority to the orders of its customers over trades for its own account"; Rule 30.2.1.2.6.1.1 gives client orders "in all cases" priority over the registered person's own.[^sec-2015-src-irr:111][^sec-2015-src-irr:94] PSE adds the Best Execution Rule (RTR Art. IV s.23: "reasonable diligence to ascertain the best available price")[^pse-revised-trading-rules:29] and separate traders for client and proprietary accounts. A TP may designate at most two "PC Traders", and only one of them may handle both kinds of account on a given day.[^pse-revised-trading-rules:28][^pse-implementing-guidelines-trading-rules:9] By inference, a broker cannot cross a client against its own principal book without a client-priority and best-execution justification, and in an agency cross between two clients the price must still sit inside the public spread, so the improvement is shared between the clients and not captured by the broker.
- **Give-up/Take-up.** A TP may assign a client's outstanding order to another TP for clearing and settlement; the Settling TP assumes the liabilities by agreement, the Assigning TP stays solidarily liable, and **proprietary orders cannot be given up**.[^pse-revised-trading-rules:27][^pse-revised-trading-rules:28]
- **Done-through.** A Requesting TP may ask an Executing TP to execute for the requester's clients. The executing TP must use a dedicated "Special Account Institutional" code (local or foreign by the beneficial owners' nationality; a mixed set uses the foreign code), may not aggregate these orders with other clients' orders, and may not amend the trades. Both TPs report client details to CMIC by 12:00 noon on T+1.[^pse-tpa-2013-0200-done-through-transactions:7][^pse-tpa-2013-0200-done-through-transactions:11]
- **Same beneficial owner.** The cross definition requires "different beneficial Owners". A cross between accounts with the same beneficial owner is a wash trade (inference from the definition and SRC s.24.1(a)).[^ra-8799-src:24]

### Execution implications

- Crosses are for continuous trading and the run-off only. Schedule them away from the auctions and the recess, and expect rejection in a reserved or halted security.
- A natural block that sits within 5% of the previous close but below PHP 20m must be crossed inside the spread. If the spread is one tick there is no price room: split across days, or use the Closing VWAP session ([Chapter 6](#/ch/auctions)).
- Keep client and proprietary trader segregation intact and never cross against an account with the same beneficial owner.
- Whether "within the BBO" includes the touch prices is not stated; the FIX design (AON, IOC) suggests inclusive bounds with execution against resting orders at the touch not guaranteed (inference). Test before building policies that depend on trading at the touch.

## Block sales

A **block sale** is "a pre-arranged transaction which is executed through the facilities of the Exchange" and compliant with the IG; the **Block Sale Market** is where such transactions are executed.[^pse-revised-trading-rules:8] Block sales may involve one or two TPs but must have different clients on the buying and the selling side.[^pse-revised-trading-rules:31] They are matched outside the order book: the best-price rule excludes them.[^pse-revised-trading-rules:24]

### Eligibility and price

| Parameter | Regular block sale | Special block sale |
|---|---|---|
| Minimum value | PHP 20 million | PHP 50 million |
| Price | Within ±5% of the Last Adjusted Closing Price (LACP); at most 4 decimals | At most 4 decimals; **no price band is listed in the IG** |
| Volume | May be a non-multiple of the board lot | Same |
| Approval | Application filed before the Run-Off Period (the 2010 text said 12 noon); Exchange decides within 30 minutes; prior approval of the MOD head | Exchange decides within 2 working days; prior approval of the COO; underlying agreement and supporting documents supplied by the selling TP |
| Who executes | The TP, by a trade declaration in the Trading Confirmation System (TCS) before Market Close | PSE Market Control, in the Trading System |
| Settlement (IG text) | "Within the execution date (T+0)" | Execution date unless the parties' agreement says otherwise |

Sources: IG XVIII (in force since 26 Jul 2010),[^pse-implementing-guidelines-trading-rules:23][^pse-implementing-guidelines-trading-rules:24] and the Dec 2011 amendment to the application deadline (from 2 Jan 2012).[^pse-tpa-2011-0124-amended-implementing-guidelines:4] PSE restated both thresholds on 1 Jul 2026: for regular blocks the price may not be more than 5% above or below the "Reference Price (i.e. Previous Closing Price or Last Adjusted Closing Price in the event of corporate actions)".[^pse-cn-2026-0031-negotiated-trades:3] The base rule keys the band to the previous trading day's close, the adjusted close after corporate actions, or the last adjusted close if the security did not trade the previous day.[^pse-revised-trading-rules:31]

**Dollar-denominated securities (DDS)** use USD 500,000 for regular and USD 1,000,000 for special blocks; "all other conditions for Block Sales ... such as price limit and reportorial requirements, shall apply", so the ±5% band applies to regular DDS blocks. DDS orders are converted to pesos at the previous day's exchange rate for the per-order value limit, and the daily report converts DDS block and odd-lot trades the same way.[^pse-dds-rules:7][^pse-eod-daily-quotation-2026-10-02:11]

<div class="callout infer">
<span class="label">Inference</span>

The IG lists no price band for special blocks, although the RTR says block-sale prices are bounded by "a prescribed ratio" of the previous close.[^pse-revised-trading-rules:31] In practice, special blocks (tender-offer settlements, minimum-public-ownership cures) print at the agreed or tender price without the ±5% test, but PSE approves them case by case. Thresholds apply per transaction, not per print: a special block can be split into several prints, so a print below PHP 20m is not evidence of a breach.
</div>

### Approval, entry and reporting

| Step | Rule |
|---|---|
| Window | From Market Pre-Open to the Trading-at-Last/Run-Off period, **including Market Recess** (Dec 2011 wording).[^pse-tpa-2011-0110-amended-revised-trading-rules:5] Whether a block may print in the 15:00-15:15 Closing VWAP session is not addressed |
| Security state | The Block Sale Market adopts the normal-market security states except freezing and reservation[^pse-revised-trading-rules:32] |
| Application | Duly executed form with a certification that the facility is not used to circumvent the National Internal Revenue Code; the IG also contains a 30-day filing clause that sits oddly with the apply-before-execution rule[^pse-implementing-guidelines-trading-rules:24] |
| Execution timing | Within 5 minutes of approval. Approval after hours: executed in the next Market Pre-Open. A delay is allowed only for a problem affecting the transaction or settlement, or for a pre-determined execution date, when the block executes in that day's Pre-Open[^pse-implementing-guidelines-trading-rules:25] |
| Two-firm blocks | A declaration the counterpart TP does not confirm within 15 minutes is eliminated automatically[^pse-implementing-guidelines-trading-rules:25] |
| TCS fields | Side, security, quantity, price, counterpart member code, client account ID[^pse-implementing-guidelines-trading-rules:24] |
| Value limit | The TCS observes the trader value limit; the TP can request a temporary lift or ask Market Control to execute (also on technical difficulty)[^pse-implementing-guidelines-trading-rules:24][^pse-implementing-guidelines-trading-rules:25] |
| Public notice | For a pre-determined execution date, MOD publishes security, number of shares, price, value and date on the PSE website once approved[^pse-implementing-guidelines-trading-rules:25] |
| Client disclosure | Within 5 trading days of execution the executing TPs disclose to MRD **the identity of all clients who transacted the security from the time the block-sale request was filed**[^pse-implementing-guidelines-trading-rules:25] |
| Settlement report | TPs promptly report the fact of settlement to MRD; a TP unable to settle by the settlement date is penalised[^pse-implementing-guidelines-trading-rules:25] |
| Short sales | Short-sell orders are not accepted for block sales ([Chapter 9](#/ch/short-selling))[^pse-short-selling-guidelines-2023-10:2] |
| FIX | Trade Capture Report (AE) with TrdType 0 = Regular Block Sale, 1 = Special Block Sale (52 and 46: Market Control trades with and without impact). A one-party report needs counterparty accept or decline and times out as "Defaulted"; a two-sided "cross block" report can be submitted by one TP; FIX news category 95 is BlockSale[^pse-fix-specification-v2-5:35][^pse-fix-specification-v2-5:38][^pse-fix-specification-v2-5:40][^pse-fix-specification-v2-5:51] |

Special blocks tied to tender offers are pre-announced by Trading Participant Advisory one to two trading days ahead, with security, size, price and date. Examples from 2026:

| Notice | Announced | Executed | Shares | Price | Value (PHP) |
|---|---|---|---|---|---|
| TPA-2026-0010 (SPM)[^pse-tpa-2026-0010-block-sale-spm:1] | 6 Mar | 10 Mar | 29,925,960 | 2.70 | 80,800,092 |
| TPA-2026-0012 (ATI, tender-offer results)[^pse-tpa-2026-0012-block-sale-ati-tender-offer:1] | 12 Mar | 13 Mar | 31,721,200 and 177,612,478 | 36.00 (notice prints "3.60", an evident typo) | 1,141,963,200 and 6,394,049,208 |
| TPA-2026-0015 (DHI)[^pse-tpa-2026-0015-block-sale-dhi:1] | 16 Mar | 17 Mar | 191,854,123 | 1.7032 | 326,765,942.29 |
| TPA-2026-0023 (PAL)[^pse-tpa-2026-0023-block-sale-pal:1] | 28 May | 29 May | 464,230,075 | 0.4305 | 199,851,047.29 |

The ATI notice also announced a trading suspension after execution for non-compliance with the minimum public ownership rule. The four-decimal prices and non-lot quantities show these are averaged or negotiated prices, not book ticks; the same is true of ordinary blocks (24 May 2024: TEL at 1,407.0316 and BDO at 136.5562).[^pse-eod-daily-quotation-2024-05-24:12]

### Block prints in the daily report

The Daily Quotation Report lists each block sale (security, price, volume, value) with no broker identity, and its sectoral and grand totals "include Normal Market, Odd Lot, Block Sale and VWAP transactions".[^pse-eod-daily-quotation-2026-10-02:11][^pse-eod-daily-quotation-2026-10-02:12] **Block prints do not enter the stock's own open, high, low, close, volume or value row.** On 2 Oct 2026 a CREC block of 100,000,000 shares at 4.85 (PHP 485.1m) sits beside a regular row of open, high, low and close all 4.62 on 20,000 shares; two GTCAP blocks at 415.00 (1,639,980 and 1,420,390 shares) printed below the regular day's low of 417, with a regular close of 419.8 on 19,900 shares.[^pse-eod-daily-quotation-2026-10-02:1][^pse-eod-daily-quotation-2026-10-02:3][^pse-eod-daily-quotation-2026-10-02:11] Blocks are likewise excluded from the VWAP computation and from the trading-value base of the market-halt trigger.[^pse-approved-rules-vwap-trading-2024:7][^pse-cn-2025-0037:3]

<div class="callout infer">
<span class="label">Inference</span>

Block sales neither set the last traded price or close of the regular market nor feed the indices, which use "actual last traded prices".[^pse-index-policy-2024:13] PSE states this in no rule; it is read from the report layout.
</div>

### Measured block share, 2026

The figures in this subsection are **computed from PSE's Daily Quotation Reports** (186 reports, 2 Jan to 2 Oct 2026), not published by PSE.[^pse-dqr-2026-ytd-block-parse] The report's grand total is PSE's headline turnover: the H1 average of PHP 7.72bn a day equals PSE's published average daily value traded.[^pse-infographic-2q26:1] As an independent check, PSE's August 2026 Monthly Report gives non-regular (block plus odd-lot) value of PHP 1,314.15m against a total of PHP 7,561.17m average daily value over the 162 days to 31 August, 17.4%;[^pse-monthly-report-2026-08:1] the same months in the daily-report parse give 17.4% (PHP 212.7bn of PHP 1,224.9bn). PSE's monthly reports define non-regular as block sales plus odd lots.[^pse-monthly-report-sample:11]

**Block sales were 18.4% of headline value over the 186 days (PHP 263.6bn of PHP 1,434.7bn); 16.5% in H1.** Odd lots were 0.013% and the VWAP session 0.124%, leaving about 81.5% for the normal market. Every one of the 186 days had block sales.

| 2026 month | Days | Headline value (PHP bn) | Block (PHP bn) | Block share | Median day | Max day |
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

- **Daily distribution.** Median day 12.4% (p10 4.3%, p90 32.8%, maximum 82.2%). The simple mean of daily shares is 15.3% against the value-weighted 18.4%. Days above 30%: 20 of 186 (10.8%); above 50%: 5 days.
- **Print size.** 1,608 prints: median PHP 50.0m; p10 23.5m; p25 30.8m; p75 103.7m; p90 281.5m. 799 prints fall between PHP 20m and 50m and 806 are at or above PHP 50m (421 at or above PHP 100m, 84 at or above PHP 500m); prints of PHP 50m or more carry 90.1% of block value. The median block day has 9 prints.
- **Extreme day.** 11 Sep 2026: an FGEN block of 715,855,362 shares at 36.00 (PHP 25.77bn) made block value PHP 26.86bn, 82% of that day's PHP 32.70bn total.[^pse-eod-daily-quotation-2026-09-11:11][^pse-eod-daily-quotation-2026-09-11:12] On 2 Oct 2026 blocks were PHP 2,625.7m of PHP 8,182.6m (32.1%).[^pse-eod-daily-quotation-2026-10-02:11][^pse-eod-daily-quotation-2026-10-02:12] An earlier sample, 24 May 2024: PHP 575.3m of PHP 4,468.3m (12.9%).[^pse-eod-daily-quotation-2024-05-24:12][^pse-eod-daily-quotation-2024-05-24:13]

**How blocks price against the reference close** (reference = the stock's latest non-empty daily close before the block date, with no corporate-action adjustment, so ex-date and split cases are noisy):

| Subset of prints | Prints | Priced within ±5% of the reference |
|---|---|---|
| All prints with a reference | 1,596 | 98.0% |
| PHP 20m to 50m | 793 | All |
| PHP 50m or more | 800 | 96.2% |

All 793 prints between PHP 20m and 50m are consistent with a binding regular-block band (below the special-block minimum, so most likely regular blocks, although a special block can be split). The 32 outside-band prints are overwhelmingly deal-priced special blocks: FGEN 36.00 against a 26.90 reference (+33.8%, PHP 25.8bn, 11 Sep 2026); RRHI 48.30 against 38.00 (+27.1%); ATI's tender-offer block at 36.00 against 29.00 (+24.1%); DHI 1.7032 against roughly 4.0-4.3 (about -58% to -60%); PAL 1.33 against 3.40. A few moderate breaches (SMPH -7.5%, AREIT -7.5%, RCR -5.6%, CREC -5.05%) may reflect unadjusted references.

| Block price / reference close - 1 | Prints |
|---|---|
| Below -5% | 24 |
| -5% to -4% | 62 |
| -4% to -2% | 51 |
| -2% to 0% | 605 |
| 0 to +2% | 811 |
| +2% to +4% | 27 |
| +4% to +5% | 8 |
| Above +5% | 8 |

Median 0.00%, p25 -0.43%, p75 +0.35%, p5 -4.29%, p95 +1.33%, mean -0.50%; 57.8% of prints within ±0.5% of the reference. The discount tail is fatter than the premium tail (62 prints between -5% and -4% against 8 between +4% and +5%).

<div class="callout">
<span class="label">Consequence</span>

Headline turnover overstates the liquidity an algorithm can reach: about 18% of 2026 value (and over 30% on one day in nine) is block value that never touches the order book, never prints in the stock's own row and cannot be worked with participation logic. Budget from regular-market volume, and treat block-heavy days as outliers rather than as high-liquidity days.
</div>

### Settlement and guarantee status

<div class="callout warn">
<span class="label">Unresolved: when blocks settle and who guarantees them</span>

The IG says regular blocks settle "within the execution date (T+0)"; special blocks on the execution date unless the parties agree otherwise.[^pse-implementing-guidelines-trading-rules:24] The RTR says blocks "shall be settled based on Clearing Agency rules".[^pse-revised-trading-rules:32] Regular trades moved from T+3 to T+2 on 24 Aug 2023,[^sccp-memo-04-0823-t2-go-live:1] and **no block-specific amendment was found**, so the current block settlement date is unverified. SCCP's 2018 operating procedures say trades covered by the clearing-fund guarantee, the fails system and the collateral deposit system "shall specifically exclude PSE block transactions and negotiated deals".[^sccp-clearing-house-operating-procedures-2018:23] A November 2021 SCCP consultation proposed that block sales conforming to the settlement cycle be settled and guaranteed by SCCP;[^sccp-memo-03-1121-proposed-amendments:4] whether that was adopted is unverified, and the posted rulebook is the 2018 text. Until confirmed, treat blocks as **outside the SCCP guarantee** and ask your broker and custodian for the settlement date and the credit exposure ([Chapter 10](#/ch/clearing-settlement)). The FIX Trade Capture Report carries an optional settlement-date field.[^pse-fix-specification-v2-5:41]
</div>

### Execution implications

- Eligibility test for pre-arranged size: `shares_min = ceil(20,000,000 / price)`; band = [0.95, 1.05] x previous close (or LACP after corporate actions); price at most 4 decimals. Outside the band you need a special block: at least PHP 50m, documents, COO approval, two working days.
- Budget capacity from regular-market ADV (about 81.5% of the headline figure) and treat days with a block share above 30% (20 of 186 in 2026) as non-representative. Do not compute market-impact baselines from headline volumes that include blocks ([Chapter 15](#/ch/empirical)).
- Pre-announced special blocks (tender-offer settlements, minimum-public-ownership cures) are event signals one to two trading days ahead.
- Surveillance: your executing broker must name every client that traded the security between the block request and execution within 5 trading days, so a client's trading between request and execution is visible to MRD.

## Odd lots

Orders below the board lot trade in a separate Odd Lot Market with its own price-time book (symbol prefix "O"; FIX board code `O`; ITCH group "Oddlot").[^pse-implementing-guidelines-trading-rules:19][^pse-fix-specification-v2-5:47][^pse-itch-equities-feed-spec-v2-3:9]

| Item | Rule |
|---|---|
| Hours | Continuous trading only. No Pre-Open, Pre-Close or Run-Off[^pse-implementing-guidelines-trading-rules:20] |
| Order types and validity | Limit and market; Day, Good-Till-Week, Good-Till-Date, Good-Till-Cancelled, Sliding[^pse-implementing-guidelines-trading-rules:20] |
| Matching | Partial matching allowed; modification as in the Normal Market; crosses allowed on the same rules[^pse-implementing-guidelines-trading-rules:20] |
| Reference price | Both markets start the day on the Normal Market's LACP; the odd-lot close is the last odd-lot trade in continuous trading or, if none, the LACP[^pse-implementing-guidelines-trading-rules:20] |
| Thresholds | No Dynamic Threshold; normal-market freezing and reservation do not carry across in either direction; no reservation before lifting a suspension[^pse-implementing-guidelines-trading-rules:20][^pse-revised-trading-rules:26] |
| Excluded | Short-sell orders[^pse-short-selling-guidelines-2023-10:2]; the VWAP computation[^pse-approved-rules-vwap-trading-2024:7] |
| Charges | TPs set their own; using the market to execute a normal-market transaction is a violation[^pse-implementing-guidelines-trading-rules:20] |
| DDS | Can trade in the Odd Lot Market[^pse-dds-rules:7] |
| Size | 2 Oct 2026: 3,183,528 shares, PHP 816,741.51;[^pse-eod-daily-quotation-2026-10-02:11] 24 May 2024: 761,654 shares, PHP 285,701.91;[^pse-eod-daily-quotation-2024-05-24:12] 2026 to 2 Oct: 0.013% of headline value (computed)[^pse-dqr-2026-ytd-block-parse] |

The odd-lot book is independent: nothing in the rules links its prices to the normal-market BBO, so odd-lot prices carry no best-price protection (inference).

<div class="callout warn">
<span class="label">Scheduled change: 23 Nov 2026, subject to SEC approval</span>

With a one-share standard lot "PSE will no longer operate an Odd Lot Market. All orders will be matched on the normal market in the new trading engine"; TPs may impose their own minimum order value, subject to the commission cap.[^pse-cn-2025-0046-board-lot-trading-at-last:5][^pse-nte-faq-2026-08:1] PSE's August 2026 status for the lot change is "For SEC Approval".[^pse-analyst-briefing-1h-2026:9] Keep the odd-lot code path behind the engine/rule-set switch ([Chapter 16](#/ch/execution-implications)).
</div>

### Execution implications

- Until the one-share lot takes effect, treat odd lots as a thin, separate venue for residuals only. Never include them in auction logic or in benchmark-VWAP computations. A board-lot residual cannot be worked in an auction or the run-off.
- If the lot change is approved, remove odd-lot sweeps and board-lot rounding; lot-size logic becomes 1, though broker-imposed minimum order values may still apply. Read lot and tick from the security master rather than hard-coding either regime.

## Negotiated Trades (proposed)

<div class="callout warn">
<span class="label">Proposed, not in force: Negotiated Trades</span>

CN-2026-0031 (1 Jul 2026; comments to 7 Jul) proposes a facility for pre-arranged trades that fit neither a cross nor a block. PSE's status on 17 Aug 2026 was "Revising per Public Comments", and the consultation paper itself says the final rules "may differ from the draft".[^pse-analyst-briefing-1h-2026:9][^pse-cn-2026-0031-negotiated-trades:2] No approval had been found by 6 Oct 2026, and the facility is tied to the NTE go-live on 23 Nov 2026. Do not build to these parameters as current rules.
</div>

| Parameter (draft) | Proposed rule |
|---|---|
| Definition | "A pre-arranged transaction executed at the agreed price", executed by a TP for different clients or its proprietary account[^pse-cn-2026-0031-negotiated-trades:5][^pse-cn-2026-0031-negotiated-trades:7] |
| Size | No volume or value restriction[^pse-cn-2026-0031-negotiated-trades:3] |
| Window | 15 minutes after the Run-Off/Trading-at-Last period: a "Closing VWAP Negotiated Trades Session", 15:00-15:15 (half-day 12:10-12:25)[^pse-cn-2026-0031-negotiated-trades:6][^pse-cn-2026-0031-negotiated-trades:11] |
| Price | Within ±5% of the full-day VWAP (all trades from the Opening Period to the Closing Period except block sales and intentional crosses); if the security did not trade, within ±5% of the previous close or LACP; at most 4 decimals[^pse-cn-2026-0031-negotiated-trades:11] |
| Parties | One firm only[^pse-cn-2026-0031-negotiated-trades:4][^pse-nte-broker-forum-2026-07-09:8] |
| Securities | Not for a currently suspended or halted security[^pse-cn-2026-0031-negotiated-trades:7] |
| Settlement | "Based on SCCP Rules"; no guarantee statement[^pse-cn-2026-0031-negotiated-trades:7] |
| Disruption | Session suspended if the VWAP is delayed; execution cancelled for the day if fewer than 5 minutes remain[^pse-cn-2026-0031-negotiated-trades:11] |
| Platform | Web-based, "similar to the VWAP facility"[^pse-nte-faq-2026-08:1] |
| Relation to blocks | "Negotiated Trades will not replace the current Block Sale": a variant of the existing block-sale framework[^pse-nte-faq-2026-08:1] |
| Reporting | In the consolidated trade file and end-of-day reports; counted in the day's total trading value "(subject to further confirmation)"; disseminated on the market-data feed as news or announcement[^pse-nte-faq-2026-08:1][^pse-nte-faq-2026-08:2][^pse-nte-faq-2026-08:3] |

The facilities compared (XTS-era rules in force; the last column is the proposal):

| | Cross order | Regular block | Special block | VWAP trade | Negotiated Trade (proposed) |
|---|---|---|---|---|---|
| Minimum value | None, but not for block-eligible deals | PHP 20m (DDS USD 500k) | PHP 50m (DDS USD 1m) | PHP 500,000 | None |
| Price | Within the BBO; closing price in run-off | ±5% of previous close or LACP | Agreed; no band in the IG | Full-day VWAP | ±5% of full-day VWAP |
| Window | Continuous trading and run-off | Pre-Open to Run-Off, including recess | Same; Pre-Open if date pre-set | 15:00-15:15 | 15:00-15:15 |
| Parties | One TP; different beneficial owners | One or two TPs; different clients | Same | One TP | One TP |
| Approval | None | 30 minutes | 2 working days, COO | None | None |
| Entry | FIX New Order Cross | TCS or FIX Trade Capture | Market Control | Exchange VWAP facility (not FIX order entry; inference) | Web-based, "similar to the VWAP facility" |
| Public print | Normal-market tape (ITCH `C`) | Block list; ITCH `B` | Same | VWAP list | News or announcement |

The VWAP-trade column is from the SEC-approved VWAP rules ([Chapter 6](#/ch/auctions));[^pse-approved-rules-vwap-trading-2024:7] the cross and block columns are from the sections above.

### Execution implications

- Keep Negotiated Trades as a planned, flagged branch of the routing function. Do not route to it before the SEC-approved text and the NTE go-live.
- If approved, it gives small pre-arranged trades a route outside the BBO but within ±5% of a VWAP that is already final when the window opens after the run-off, so the price band is certain at execution (inference).
- Size is unconstrained and prints are reported as news and in end-of-day files: expect more non-order-book value, and keep headline and regular-market volume separate in any liquidity model.

## Routing a pre-arranged trade

<div class="callout infer">
<span class="label">Inference</span>

This is a design built from the rules above, not rule text. Log which leg of the test failed (parties, state, value, band, BBO, session) so a rejected or mis-routed pre-arranged trade can be explained from the log.
</div>

<div class="callout">
<span class="label">Consequence</span>

Venue choice for a pre-arranged trade is rule-driven, not a preference. A deal that qualifies for the Block Sale Market may not be crossed, a deal below the block minimum may be crossed only inside the BBO, and a deal that fits neither has no on-exchange route today.
</div>

| Test | If yes | If no |
|---|---|---|
| 0. Different beneficial owners on the two sides? | Continue | Stop: a same-owner trade is a wash trade |
| 1. Security suspended or halted (a cross is also blocked in a reserved security)? | No cross and no block: blocks adopt halt and suspension states. Wait | Continue |
| 2. Value at least PHP 20m (DDS USD 500k) and price within ±5% of the previous close or LACP, at most 4 decimals? | **Regular block sale**; a cross is prohibited. Apply before the Run-Off Period; approval within 30 minutes; execute within 5 minutes | Go to 3 |
| 3. Value at least PHP 50m (DDS USD 1m), agreed price outside the band, documented underlying agreement? | **Special block sale**: COO approval within 2 working days; Market Control executes | Go to 4 |
| 4. Continuous trading (or run-off at the closing price), agreed price inside the BBO, one TP on both sides? | **Cross order**: FIX New Order Cross (AON, IOC, limit) | Go to 5 |
| 5. Priced at the day's VWAP and at least PHP 500,000? | **VWAP trade**, 15:00-15:15, one TP | No on-exchange route today: work it as ordinary orders, or wait for Negotiated Trades if approved |

```python
def route(deal, now, book, ref_close, closing_price):
    if deal.buyer_owner == deal.seller_owner:        return REJECT("wash trade")
    if deal.security.state in (HALTED, SUSPENDED):   return REJECT("security state")
    in_band = abs(deal.price / ref_close - 1) <= 0.05 and decimals(deal.price) <= 4
    if deal.value >= min_regular_block(deal.security) and in_band:
        return REGULAR_BLOCK            # a cross is not allowed; apply before the run-off
    if deal.value >= min_special_block(deal.security) and deal.has_agreement:
        return SPECIAL_BLOCK            # about 2 working days; COO approval
    crossable = ((continuous(now) and book.bid <= deal.price <= book.offer)
                 or (runoff(now) and deal.price == closing_price))
    if crossable and deal.single_tp:    return CROSS     # touch inclusivity unverified
    if deal.benchmark == "VWAP" and deal.value >= 500_000:  return VWAP_TRADE
    return NO_ONEXCHANGE_ROUTE
```

**Worked arithmetic.** A stock closed at PHP 100.00. The regular-block band is PHP 95.00 to 105.00 and the minimum size is 200,000 shares at 100.00; at the band edges it is 190,477 shares at 105.00 and 210,527 shares at 95.00 (20,000,000 / 105 = 190,476.2 and 20,000,000 / 95 = 210,526.3, rounded up).

**Three cases** (previous close PHP 50.00, BBO 49.95 / 50.05, continuous trading):

| Deal | Route |
|---|---|
| PHP 35m at 50.00 | Value at least PHP 20m and in the band: **regular block**, not a cross, although 50.00 is inside the BBO |
| PHP 12m at 50.00 | Below the block minimum and inside the BBO: **cross** in continuous trading |
| PHP 35m at 53.50 (+7%) | Outside the band, below PHP 50m (so not a special block) and outside the BBO (so not a cross): **no on-exchange route**. A PHP 60m deal at 53.50 with an underlying agreement could be a special block |

### Execution implications

- A natural block above PHP 20m inside the band cannot be crossed even if the cross price is inside the BBO; budget the application and approval timing.
- Timing: blocks may execute from Pre-Open to the run-off, including the recess; crosses only in continuous trading and the run-off. The filing deadline for a regular block is the start of the Run-Off Period, but approval (up to 30 minutes) and execution must still fall inside trading hours, so a late decision usually costs a day (inference).
- If the price is outside the band and the size is below PHP 50m, only a cross inside the spread remains. That is the gap Negotiated Trades is meant to fill.

## Transparency in brief

PSE publishes a full order-by-order book on the ITCH Total View feed and a top-of-book Basic feed; market-data detail is in [Chapter 11](#/ch/market-data).

- The Add Order message has no participant field; broker identifiers appear only on executions and trades, and only when the market does not run "Broker Anonymity ... as announced by the exchange".[^pse-itch-equities-feed-spec-v2-3:14][^pse-itch-equities-feed-spec-v2-3:25] In October 2014 PSE said it would implement anonymity "but not on Go-Live".[^pse-fix-itch-session-week01-2014-10-03:11] No later activation notice was found, so activation is unconfirmed and the working assumption is that executions are broker-identified.
- Crosses, block sales and manual trades carry type flags (`C`, `B`, `M`) in the Trade message, which also has a Printable flag saying whether an execution enters statistics; opening-auction fills arrive as Order Executed With Price messages.[^pse-itch-equities-feed-spec-v2-3:18][^pse-itch-equities-feed-spec-v2-3:27]
- ITCH Basic is top-of-book only: in October 2014 PSE declined a five-level BBO because "the standard for ITCH Basic is that only top of book is published".[^pse-fix-itch-session-week01-2014-10-03:10] Total View is order-by-order but anonymous at order level, so queue position can be inferred from order numbers and counterparty identity is visible only after the trade (inference). Rebuild the book from Total View to estimate queue position.
- Indicative auction price and quantity are broadcast on Total View only, not on Basic ([Chapter 6](#/ch/auctions)).[^pse-itch-equities-feed-spec-v2-3:22][^pse-itch-equities-feed-spec-v2-3:23]
- Block prints appear after the fact in the Daily Quotation Report without broker identities.[^pse-eod-daily-quotation-2026-10-02:11]

## What is not in the public record

- The IG "limitations" that govern a cross price when there is no BBO, and whether "within the BBO" includes the touch prices; whether a cross can print at the touch while resting orders exist at that price.
- How the automatic cross interacts with price priority, and whether a TP's client and proprietary accounts can auto-cross; whether an automatic-cross execution carries the ITCH cross flag (`C`) or prints as an ordinary trade; whether the NTE has any self-trade prevention.
- The current block-sale settlement date and any SCCP guarantee (see the callout above); approval criteria for special blocks beyond "underlying agreement and supporting documents".
- Whether a block can be executed in the 15:00-15:15 Closing VWAP session, and whether block prints reach ITCH in real time as well as the end-of-day report (the specification allows Trade messages flagged `B`; live practice is not documented).
- Any official PSE statistic for the block share of turnover. The shares above are computed from daily reports, and the reference-price analysis uses carried-forward closes without corporate-action adjustment.
- The final approved text of Negotiated Trades and whether it will coexist with the VWAP session on the NTE.
