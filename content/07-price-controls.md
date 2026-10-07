---
number: 7
slug: price-controls
title: Price Controls, Halts and Circuit Breakers
summary: Static band +50%/−30%, dynamic 10–20% thresholds that freeze the stock instead of auctioning it, PSEi breakers at −10/−15/−20%, and how halts and suspensions treat resting orders.
part: Trading mechanics
---

The Philippine Stock Exchange controls price moves with three layers, none of which behaves like the limit-up/limit-down or volatility-auction regimes of other venues. A **static band** fixes an absolute corridor for the day (+50% / −30% of the reference price). A per-security **dynamic threshold** (10%, 15% or 20% of the last traded price, set by six-month trade count) is a second, tighter corridor. A **market-wide circuit breaker** halts everything when the PSEi falls 10%, 15% or 20% from the previous close. Below those sit discretionary single-stock halts and suspensions imposed for disclosure, surveillance and compliance reasons.

Two behaviours break assumptions carried over from other venues. First, an order that breaches either corridor neither bounces nor queues: it **freezes the security for every participant** (no posting, modifying or cancelling) until PSE Market Control accepts or rejects it, normally within five minutes and by contacting the broker (the Trading Participant, TP) to confirm the order — and there is **no stock-level volatility auction**. Second, **halt and suspension are different states with opposite order handling**: a halt leaves resting orders in place and lets participants manage them, a suspension purges them. The rules are a 2010 base text (the Revised Trading Rules, RTR, and Implementing Guidelines, IG) plus circulars; PSE publishes no consolidated edition,[^pse-web-regulation-trading-participants] and its public FAQ is stale (it still describes a 50% floor and a 3:30 pm close).[^pse-web-investing-at-pse] This chapter describes the PSEtrade XTS rules in force on 6 October 2026; the Nasdaq Eqlipse cut-over scheduled for 23 November 2026 is treated in a warning at the end.

## The control stack on 6 October 2026

| Control | In force | Effective | Replaced |
|---|---|---|---|
| Static price band | Ceiling +50%, floor −30% of the Reference Price[^pse-cn-2020-0028:1-2] | Tue 24 Mar 2020 | ±50% since 26 Jul 2010[^pse-implementing-guidelines-trading-rules:10] |
| Dynamic threshold | 20% / 15% / 10% of last traded price for trade-count Clusters A / B / C; new listings 20%[^pse-implementing-guidelines-trading-rules:10] | Latest list effective Fri 7 Aug 2026[^pse-tpa-2026-0036-dynamic-threshold-review:1] | Previous list, effective Mon 2 Feb 2026[^pse-tpa-2026-0002-dynamic-threshold-review:1] |
| Freeze and Market Control | Breaching order freezes the stock; Market Control accepts or rejects within 5 minutes[^pse-implementing-guidelines-trading-rules:26] | 26 Jul 2010 | — |
| Market-wide circuit breaker | PSEi −10% / −15% / −20% vs previous close → 15 / 30 / 60-minute halt, each level once a day[^pse-cn-2020-0044:2] | Mon 4 May 2020 | Single −10% / 15-minute level[^pse-revised-trading-rules:35] |
| System-failure market halt | TPs holding more than 50% of six-month average daily trading value (ADTV, ex-block) cannot trade, even through a Correspondent TP[^pse-cn-2025-0037:3] | 20 Aug 2025 | At least one-third of TP-users unable to connect[^pse-revised-trading-rules:35] |
| Weather rule | PAGASA (the weather agency) wind signal 3–5 in the National Capital Region (NCR) at 6:00 am → trading day cancelled[^pse-cn-2025-0037:4] | 20 Aug 2025 | Case-by-case declarations |
| Single-stock halts and suspensions | Disclosure halts (lifted one hour after dissemination), restrictions by the Capital Markets Integrity Corporation (CMIC, PSE's surveillance arm), suspensions for late reports, minimum public ownership (MPO) breach and backdoor listing[^pse-listing-disclosure-rules:140][^pse-listing-disclosure-rules:153] | RTR 2010; CMIC from 12 Mar 2012 | — |
| Nasdaq Eqlipse (NTE) | Go-live scheduled Mon 23 Nov 2026; threshold and halt parameters not published[^pse-nte-broker-forum-2026-07-09:9] | Not in force | PSEtrade XTS |

## Static price band

### Rule

Every limit order must carry a price inside the security's Trading Threshold, which is the static and the dynamic threshold together.[^pse-revised-trading-rules:20][^pse-revised-trading-rules:21] The static threshold is an absolute ceiling and floor for the day.[^pse-implementing-guidelines-trading-rules:10] Since **Tue 24 March 2020** the ceiling is 50% above and the floor 30% below the Reference Price: the lower limit was cut from 50% by circular CN-2020-0028 (dated 21 March 2020, with SEC approval; CN-2020-0044 dates the SEC's approval of the companion breaker amendments 20 March), and the upper limit stayed at 50%.[^pse-cn-2020-0028:1-2][^pse-cn-2020-0044:1] PSE's stated rationale was a regional benchmark of 10–30%.[^pse-web-press-2020-03-21-static-threshold] The band does not apply to warrants.[^pse-revised-trading-rules:20] For backtests, use a −50% floor for trade dates before 24 March 2020.

### Reference price and special cases

| Situation | Reference Price used for the band | Evidence |
|---|---|---|
| Normal day | Previous Trading Day's Closing Price | RTR Art. IV §6[^pse-revised-trading-rules:20] |
| Corporate action that adjusts the close | Adjusted Closing Price (ACP), defined only as the closing price "with adjustments due to corporate events"; the formula is not published | Same section and definitions[^pse-revised-trading-rules:20][^pse-revised-trading-rules:8] |
| No trade on the previous day, including a resumption after suspension | Last Traded Price or last ACP, e.g. the last price before the suspension in the SGP and KEEPR circulars below | Same section[^pse-revised-trading-rules:20][^pse-cn-2021-0055-lift-lower-static-threshold-sgp:1] |
| Odd-lot market | Last Adjusted Closing Price of the Normal market | IG XIV[^pse-implementing-guidelines-trading-rules:20] |
| Listing by introduction | Band **lifted** on the listing date, then reinstated | Consolidated Listing and Disclosure Rules (CLDR) Art. III Part G §6[^pse-listing-disclosure-rules:87] |
| Security did not trade on its listing date | Next day's band is based on the issuer's indicative reference opening price | IG VI.5[^pse-implementing-guidelines-trading-rules:11] |
| IPO first day | **Not stated in any rule.** Medilines (IPO ₱2.30, 7 Dec 2021) "tanked 30%" on debut, consistent with the offer price acting as reference[^philstar-2021-12-07-medilines-debut] | Inference |

The Exchange cancels resting orders in a security whose close is adjusted by a corporate action, on the ex-date of cash or property dividends, and for orders that cross a board lot,[^pse-revised-trading-rules:25][^pse-implementing-guidelines-trading-rules:18] so GTC and GTD logic must re-arm on those days ([Chapter 10](#/ch/clearing-settlement/corporate-actions) has the corporate-action calendar, [Chapter 4](#/ch/order-types) order validity). PSE can also get the reference wrong: on 21 December 2023 UnionBank (UBP) was suspended for the day because "the stock's previous closing price was not adjusted to account for UBP's 27 percent stock dividends", and resumed on 22 December at the adjusted price.[^pse-cn-2023-0074-ubp-trading-suspension:1] Class A/B share mergers under SEC MC 10-2025 use the higher of the two classes' last closes as the adjusted price, with a two-trading-day suspension before the classified shares are delisted (CN-2026-0041, 10 Sep 2026).[^pse-cn-2026-0041-declassification-price-suspension:1-2] Block sales are priced within ±5% of the last adjusted close under their own rule rather than the band ([Chapter 5](#/ch/matching/block-sales)).[^pse-implementing-guidelines-trading-rules:23]

### Ceiling and floor arithmetic

The rules say the static threshold is an absolute value but do not say how it is snapped to the tick grid ([Chapter 4](#/ch/order-types/board-lots-and-tick-sizes)). Four dated price prints constrain the answer:

| Print | Reference | Raw limit | Snapped inward | Nearest tick | Snapped outward | Observed |
|---|---|---|---|---|---|---|
| SRDC, nine consecutive ceilings, 19 Dec 2025 to 7 Jan 2026 | ₱1.20 | 1.20 × 1.5⁹ | **45.95** | 46.15 | 46.30 | **45.95** (7 Jan 2026) |
| Villar Land floor, 14 Nov 2025 | ₱1,608 | 1,125.6 | 1,126 (₱1 tick) | 1,126 | 1,125 | 1,126 |
| Villar Land floor, 18 Nov 2025 | ₱789 | 552.3 | 552.50 (₱0.50 tick) | 552.50 | 552.00 | ₱552.20 as printed; the article's own −29.97% implies 552.50 |
| Asiabest (ABG) floor, 30 Sep 2026 | ₱60.85 (previous close in PSE daily quotation data)[^pse-dqr-dataset] | 42.595 | 42.60 (₱0.05 tick) | 42.60 | 42.55 | 42.60, no bid |

The SRDC chain is the discriminating point: rounding each day's ceiling **down** (1.80, 2.70, 4.05, 6.07, 9.10, 13.64, 20.45, 30.65, 45.95) reproduces the reported ₱45.95 exactly, while rounding to the nearest tick does not.[^insiderph-2026-01-08-srdc-halt][^bw-2026-01-09-srdc-resume] The nine trading days follow from CN-2025-0043, which closed the market on 24, 25, 30 and 31 December 2025 and 1 January 2026.[^pse-cn-2025-0043-non-trading-days:1] The three floor prints exclude outward snapping but cannot separate "round up" from "nearest".[^philstar-2025-11-18-vll-plunge][^pse-eod-daily-quotation-2026-09-30:3]

<div class="callout infer">
<span class="label">Inference</span>

Ceiling and floor are snapped **inward** — ceiling rounded down, floor rounded up — so the band is never exceeded: `ceil = round_down_to_tick(1.5 × RefPx)`, `floor = round_up_to_tick(0.7 × RefPx)`, using the tick of the resulting price. This is inferred from four data points, not stated in any PSE document. The legacy ITCH feed publishes the engine's own High Collar and Low Collar for each order book (see [the feed section](#/ch/price-controls/how-states-and-collars-appear-in-the-feed)); read those instead of recomputing and use the formula as a cross-check.
</div>

Compounding matters on a gap-down name: a long-only unwind faces 0.7ⁿ of the reference after n floor sessions — 70.0%, 49.0%, 34.3%, 24.0% and 16.8% for n = 1 to 5 — and Villar Land printed three consecutive floor-limit sessions in November 2025 (₱1,608 to ₱1,126, ₱790 and about ₱552).[^philstar-2025-11-18-vll-plunge] On the upside, nine ceiling sessions multiply price by 1.5⁹ ≈ 38.4, which is how SRDC went from ₱1.20 to ₱45.95 before a CMIC-requested halt.[^bw-2026-01-09-srdc-resume]

### When the band is lifted

RTR Art. VII §6 lifts the static threshold in three cases: on the resumption day of a security suspended for at least one year; on the listing date of a listing by way of introduction; and "upon consideration by the Exchange" where an event may move the price drastically or the band would make trading impractical, announced case by case. In the first and third cases the band stays lifted until trades establish the basis of the next day's ceiling and floor.[^pse-revised-trading-rules:34] Procedure: the Market Regulation or Issuer Regulation Division recommends, the Management Committee approves, Market Control lifts before pre-open; approval arriving during or after pre-open takes effect the next trading day; PSE announces it on its website beforehand.[^pse-implementing-guidelines-trading-rules:11]

| Date | Security | What happened |
|---|---|---|
| 5 Nov 2020 | PHR | Static threshold lifted on the day its suspension was lifted.[^pse-tpa-2020-0052-phr-static-threshold-lift:1] |
| 10 Nov 2021 | SGP | Follow-on bookbuilt at ₱12.00, below the floor derived from the last trade before the 31 May 2021 suspension; only the **lower** threshold lifted.[^pse-cn-2021-0055-lift-lower-static-threshold-sgp:1] |
| 19 Nov 2021 | KEEPR | ₱1.50 offer versus the pre-suspension (8 Jul 2021) price; lower threshold lifted.[^pse-cn-2021-0057-keepr-lower-static-threshold-lift:1] |
| 20 Aug 2024 | DHI | Resumed after suspension since 27 Jan 2020 (reported by press).[^philstar-2024-08-22-dominion-resumption] |
| 7 Jul 2025 | Island IT (IS) | Resumed after 1,572 days; PSE announced the lift for the resumption day, after which +50%/−30% re-attached to that day's close (press).[^philstar-2025-07-07-island-it-resumption] |
| 14–18 Nov 2025 | Villar Land | Suspended less than a year, so **no lift**: three consecutive sessions of about −30%.[^philstar-2025-11-18-vll-plunge] |
| 25 Sep 2026 | PNB Holdings (LTL) | Listing by introduction at ₱1.20: opened ₱0.75 (−37.5%), ranged ₱0.70–1.24, closed ₱1.20 on about 952.8 million shares (press).[^bw-2026-10-04-pnbh-debut] |

### Execution implications

- Clip every limit to the tighter of the static and dynamic corridors, using the feed's collars when available. A price outside the corridor does not reject politely; it freezes the stock for everyone (next section).
- The −30% floor is a liquidity cliff on gap-down names: plan exits as multi-day, and note that the floor caps a short's single-day cover profit at 30% of the reference.
- Re-pull the reference price every morning (corporate-action days, resumptions). Switch ceiling and floor logic off on listing-by-introduction days and on announced lifts, and expect unbounded downside on those sessions.
- GTC and GTD orders do not survive ex-dates and adjusted-close days; re-arm them after the purge.

## Dynamic thresholds and the freeze

### Clusters

The dynamic threshold (DT) is the maximum allowed difference between a new last traded price (LTP) and the preceding LTP.[^pse-implementing-guidelines-trading-rules:10]

| Cluster | Trades in the past six months | DT | Securities on the 7 Aug 2026 list (my count) |
|---|---|---|---|
| A | 20 or fewer | 20% | 62 |
| B | 21 to 500 | 15% | 88 |
| C | More than 500 | 10% | 235 |
| New listing | — | 20% | — |

The list is published only as an image on page 2 of the circular, so there is no machine-readable feed;[^pse-tpa-2026-0036-dynamic-threshold-review:2] the counts above are read from that image and total 385 securities, the same as the number of securities with live frames on PSE's site.[^pse-sec-frames-snapshot] Names such as SM, BDO, ICT and the FMETF ETF sit in Cluster C. The IG schedules reviews for "every second trading week of January and July" on the preceding six months' data,[^pse-implementing-guidelines-trading-rules:11] but the new lists take effect in early February and August: TPA-2026-0002 (dated 19 Jan 2026) from Mon 2 Feb 2026 on July–December 2025 data, and TPA-2026-0036 (dated 3 Aug 2026) from Fri 7 Aug 2026 on January–June 2026 data.[^pse-tpa-2026-0002-dynamic-threshold-review:1][^pse-tpa-2026-0036-dynamic-threshold-review:1] A Cluster A security traded 200 times between reviews moves to B's threshold and a Cluster B security traded 1,000 times moves to C's; PSE may reclassify earlier.[^pse-implementing-guidelines-trading-rules:11] The next reset is expected around February 2027 (inference from the cadence).

### What happens on a breach

RTR Art. VII §1: "Whenever an Order will result in a breach of the Trading Threshold of a Security within a Trading Day, the trading of the Security will be frozen." Orders cannot be posted, modified or cancelled while frozen; if an order is partly matched, only the portion that breaches is frozen. A static breach is accepted if the price is within the "allowable percentage price difference under the Implementing Guidelines", otherwise rejected, and an accepted static breach widens the static threshold to 60% (orders beyond 60% are rejected). A DT breach is accepted if within the allowable difference, otherwise rejected.[^pse-revised-trading-rules:33]

| Case | Outcome (IG XIX)[^pse-implementing-guidelines-trading-rules:25-26] |
|---|---|
| Any breach | Market Control acts "immediately or no later than five (5) minutes" after the freeze.[^pse-implementing-guidelines-trading-rules:26] |
| Partly matched limit order whose remainder breaches the DT | Intermediate trades stand. The remainder is auto-accepted if its price differs from the last intermediate trade by no more than the DT; otherwise Market Control calls the TP to confirm. |
| Limit order priced at the best bid or offer (BBO) but beyond the DT | Auto-accepted. |
| Cross transaction beyond the DT | Auto-accepted. |
| Any order breaching the DT in the five minutes before pre-close | Auto-**rejected**. |
| TP cannot be reached within five minutes | Order auto-rejected and the security "thawed". |
| More than three DT breaches by one TP in one day through different orders | Minor violation. |

Order status shows "Frozen" while the order awaits Market Control and "Market Eliminated" once cancelled by Market Control or by market rules.[^pse-implementing-guidelines-trading-rules:17] Reservation is a separate state: the engine imposes it when a market-on-opening order has no indicative opening price, a market order is unfilled at the open, or the indicative opening price breaches the static band ([Chapter 6](#/ch/auctions/reservation)), and PSE imposes it manually before lifting a suspension; during reservation orders other than crosses can still be posted, modified and cancelled.[^pse-revised-trading-rules:33][^pse-implementing-guidelines-trading-rules:26] The odd-lot market has no DT, and freezes in the Normal market do not carry across to it.[^pse-implementing-guidelines-trading-rules:20] Direct market access (DMA) firms must have written procedures for DMA orders that breach the thresholds, and their price-limit filter is expressed as a percentage or ticks from the LTP or last adjusted close ([Chapter 13](#/ch/regulatory-constraints)).[^pse-memo-sec-approved-dma-rules-2013-11-26:6][^pse-memo-sec-approved-dma-rules-2013-11-26:10]

Worked example (rule arithmetic, not engine output): a Cluster C stock last traded at ₱50.00 has a DT corridor of ₱45.00–55.00 around the LTP. With the best offer at ₱52.00, a buy limit at ₱56.00 is beyond the DT and not at the BBO, so the stock freezes until Market Control confirms or rejects it. A buy at ₱52.00 is inside the corridor and trades. If the best offer is itself ₱56.00, a buy at ₱56.00 is beyond the DT but at the BBO and is auto-accepted.

<div class="callout warn">
<span class="label">Gaps in the freeze rule</span>

The numerical "allowable percentage price difference" for a **static** breach is not in the IG, which details only the DT cases. The 60% step was written for a ±50% band; whether it applies to the −30% floor after March 2020 is undocumented. Whether the PSETrade stack rejects locally before freezing the stock, and whether the engine tests the order's limit price or the resulting trade price, are also undocumented; the IG's wording ("the price of any Order breaches the Trading Threshold") points to the limit price.
</div>

<div class="callout infer">
<span class="label">Inference</span>

There is no volatility auction ([Chapter 6](#/ch/auctions/no-volatility-auction) says the same). The stock-specific brakes are the band plus freeze, CMIC restriction, halt or suspension, and disclosure halts. A freeze of up to five minutes locks every participant's entry and cancel in that stock, so cancel-on-disconnect and kill-switch cancels cannot work during it. The DT anchor is the LTP, not the touch, so a deep passive limit more than DT% away from the last trade can itself trip a freeze, while orders at the best bid or offer and crosses are auto-accepted instead of waiting for a call.

The DT limits the jump between successive last-traded prices, not the day's move. A Cluster C name can still walk to the static floor through successive prints: Asiabest (ABG, read as Cluster C from the image-only list) fell 16.4% on 29 Sep 2026, closed at its −30% floor on 30 Sep, then fell 22.5% and 15.5% — 61.7% in four sessions — on ₱10–74 million of daily value.[^pse-dqr-dataset] The static band, not the DT, bounds the day.
</div>

### Execution implications

- Cap child-order prices at the tighter of the static corridor and the DT corridor (±10% around LTP for Cluster C). To sweep, send marketable limits at or inside the BBO and walk them.
- Refresh the cluster map each February and August from the circular's image and re-run it when PSE reclassifies mid-period. Thin names and preferreds sit in A or B (15–20% DT).
- Keep per-TP DT breaches at three a day or fewer, and send nothing that can breach the DT in the last five minutes before pre-close.
- Size passive orders so that a five-minute inability to cancel is tolerable.

## Market-wide circuit breaker

### Levels and mechanics

Since **Mon 4 May 2020** (CN-2020-0044 of 29 Apr 2020, SEC-approved 20 March 2020) trading halts when the PSEi falls at least 10%, 15% or 20% from its previous close.[^pse-cn-2020-0044:1-2]

| Level | PSEi decline | Halt | Last trigger time under the circular (pre-close 15:15) | Scaled to today's 14:45 pre-close (inference) | Shortened day (pre-close 12:45) |
|---|---|---|---|---|---|
| 1 | 10% | 15 minutes | 14:55 | 14:25 | 12:25 |
| 2 | 15% | 30 minutes | 14:40 | 14:10 | 12:10 |
| 3 | 20% | 60 minutes | 14:10 | 13:40 | 11:40 |

The circular's rules: each level triggers **once per trading day**; a breach of a higher level imposes that level's halt and the lower level never triggers that day; and a breach before the recess halts the market "for the corresponding halt duration period, which shall include the Market Recess period".[^pse-cn-2020-0044:2-4] Its own examples: PSEi down 11% at 10:00 halts the market until 10:15, and at 10:20, with the index again 10.28% below the previous close, there is no second halt; down 15% at the open halts 30 minutes, and after the 10:00 resume a reading of −10.02% at 10:30 does not halt because the higher level has already been breached.[^pse-cn-2020-0044:3] PSE's press release gives the rationale for the cut-offs: a breaker will not trigger if it would leave less than five minutes of continuous trading before pre-close.[^pse-web-press-2020-04-30-circuit-breaker]

Worked example: with a previous PSEi close of 6,000, Level 1 is at 5,400, Level 2 at 5,100 and Level 3 at 4,800. A Level 1 breach at 11:50 would use 10 of its 15 minutes before the 12:00 recess and, on this reading of the "includes the Market Recess" rule, the market would resume at 13:00 (inference).

<div class="callout warn">
<span class="label">Cut-off times after the 14:45 pre-close</span>

The circular's clock times were written for the 15:15 pre-close that applied until March 2020 (14:55, 14:40 and 14:10); the day now has a 14:45 pre-close.[^pse-cn-2022-0009-trading-schedule-mar-2022:1] No updated statement was found. Taken literally, the Level 1 and 2 times (14:55 and 14:40) fall after the 14:45 pre-close, so they cannot be literal; the cut-offs presumably scale to pre-close minus 20, 35 and 65 minutes (14:25, 14:10 and 13:40), but this is inference. The circular also labels the new text "Section XXI" of the IG, whereas the 2025 circular uses Part XXI for Technical Contingencies, so the live IG numbering is uncertain.[^pse-cn-2025-0037:6]
</div>

The single-level breaker it replaced (RTR Art. VIII §1, 2010 text) halted the market if the PSEi fell at least 10%, resumed within 15 minutes, applied once a day and did not trigger within 30 minutes of the close;[^pse-revised-trading-rules:35] the circular calls it an offshoot of the 2008 global financial crisis.[^pse-cn-2020-0044:1]

### Trigger record

| Date | PSEi | Outcome |
|---|---|---|
| 27 Oct 2008 | — | Old single-level breaker tripped[^pse-web-press-2020-04-30-circuit-breaker] |
| 12 Mar 2020 | Intraday low 5,697.13 (−10.33%); close 5,736.27 (−9.71%) | 15-minute halt[^philstar-2020-03-12-circuit-breaker] |
| 13 Mar 2020 | — | Tripped again (PSE count)[^pse-web-press-2020-04-30-circuit-breaker] |
| 19 Mar 2020 | Close 4,623.42 (−13.34%); tripped at the open at −12.4%; intraday low 4,039.15 (−24.29%) | First session after the COVID closure; the single level could not fire twice, which prompted the three-level design[^bw-2020-03-19-shares-plummet][^bw-2020-05-01-three-level-cb] |
| Since 4 May 2020 | Worst close-to-close fall −4.97% (9 Mar 2026), then −4.82% (15 Jun 2020) and −4.30% (7 Apr 2025)[^pse-weekly-reports-dataset] | No trigger found; intraday lows not individually checked ([Chapter 15](#/ch/empirical/volatility-limit-hits-and-circuit-breakers)) |

### Execution implications

- Hard-code the 10/15/20% triggers and the scaled cut-offs, and treat the cut-off clock times as unconfirmed.
- Detect a breaker halt defensively: the feed has no market-wide halt message, so combine PSEi drawdown against the previous close with simultaneous halt or freeze states across constituents (inference).
- Queue state during a breaker halt is **unknown** (see the end of the chapter). Do not assume orders survive, and do not assume they are purged; design for both and re-validate after resumption.

## System-failure halts, calamities and closures

### The system-failure halt

RTR Art. VIII §2(a), as amended on **20 Aug 2025** (CN-2025-0037, SEC-approved, effective immediately): the Exchange may halt the market if Trading Participants accounting for more than 50% of average daily trading value (exclusive of block sales) over the six calendar months before the date of determination cannot trade, directly or through their Correspondent TP, "due solely to trading system problems attributable to Exchange system issues" or natural disasters or extraordinary circumstances.[^pse-cn-2025-0037:1][^pse-cn-2025-0037:3] The old test was one-third of TP-users unable to connect.[^pse-revised-trading-rules:35] PSE's 2022 consultation argued that about 10 of 125 active brokers account for over 50% of trades, so a headcount is "not representative", and that a market-wide halt "should only be a last option".[^pse-cn-2022-0020-market-halt-consultation:4]

The 2011 amendments (clock times written for the then 15:30 close; no restatement was found) set the halt mechanics: PSE gives TPs at least five minutes' notice before lifting a halt; a halt of 30 minutes or more extends hours, but for whole-day trading only to complete the remaining phases; with less than ten minutes of continuous trading left, pre-close and trading-at-last shrink to two and five minutes; a halt that ends during trading-at-last brings a ten-minute extension (five if it began in pre-close); and a halt of more than two hours, or one running 15 minutes past the run-off, lets the Exchange decide whether to suspend or cancel the day.[^pse-tpa-2011-0124-amended-implementing-guidelines:4][^pse-tpa-2011-0124-amended-implementing-guidelines:5][^pse-tpa-2011-0124-amended-implementing-guidelines:6] The 2010 IG also halts the market while the Customer Common Gateway is down and for ten minutes after it is fixed.[^pse-implementing-guidelines-trading-rules:30] The President may suspend trading in the Market for the rest of the day (trades and posted orders stay valid) or cancel the day by announcement within one hour after pre-open (trades and orders are purged).[^pse-revised-trading-rules:36]

### Correspondent Trading Participants

Every TP must designate a Correspondent TP, with two months from posting (to about 20 Oct 2025) to comply. The correspondent must use a front-end order management system (FEOMS) from a different vendor, or sit in a different silo and FIX gateway; PSE confirms the selection at least three trading days before it takes effect; trades go through a done-through account code and may not be aggregated; PSE keeps a registry.[^pse-cn-2025-0037:2][^pse-cn-2025-0037:6][^pse-cn-2025-0037:7] The correspondent rule protects the broker's flow, not yours: a buy-side firm still needs its own second broker and FIX or DMA fallback.

### Weather rule and closures

Under CN-2025-0037 Annex B the Exchange may halt, suspend or cancel a trading day when it cannot implement its business continuity plan and an emergency stops staff entering the premises, may disrupt TPs holding more than 50% of ADTV, or otherwise threatens a fair and orderly market; it must notify the SEC immediately. For tropical cyclones, PAGASA wind signals 1–2 in NCR mean regular trading and 3–5 mean no trading, judged at 6:00 am on the trading day concerned: a downgrade to 1–2 by then avoids cancellation, and a signal still at 3 or higher cancels the day.[^pse-cn-2025-0037:4][^pse-cn-2025-0037:5] Absent a declaration, "trading shall proceed as usual".[^pse-memo-trading-days-suspensions-guidelines-2012:1] The dated list of weather, volcanic, banking-system and pandemic closures (13 Jan 2020, 17–18 Mar 2020, 26 Sep 2022, 24 Jul 2024 and earlier) and the calendar treatment are in [Chapter 3](#/ch/sessions/weather-and-emergency-closures).

### Outage record

| Date | Event | Stated cause | Outcome |
|---|---|---|---|
| 20 Nov 2014 | Halt 13:46, resumed 14:30 | Technical issues | Close 15:30 as scheduled[^pse-cn-2014-0057-trading-halt-2014-11-20:1] |
| 24 Aug 2015 | Halt 14:05:26, lifted 14:50 | Market data transmission to PSE front-end terminals (servers at full load); direct ITCH users unaffected | Statement: not imposed "to stem the market's drop"[^pse-cn-2015-0110-trading-halt-2015-08-24:1][^pse-cn-2015-0118-statement-trading-halts-2015:1-2] |
| 25 Aug 2015 | Halt 10:02:22, resumed 14:55 | Same | Halt lasted most of the day[^pse-cn-2015-0112-trading-halt-2015-08-25:1] |
| 8 Apr 2016 | Halt 10:29:18, resumed 11:10 | Third-party communication line disconnection | Not linked to 2015[^pse-cn-2016-0020-trading-halt-2016-04-08:1][^pse-cn-2016-0023-statement-trading-halt-2016:1] |
| 4 Jan 2022 | Open delayed, then day **cancelled** | 43 of 125 TPs could not connect; Nasdaq engine to Flextrade front-end link | No trading[^pse-cn-2022-0001-delay-market-opening:1][^pse-cn-2022-0002-cancellation-of-trading-2022-01-04:1] |
| 3 Jan 2024 | Halt 09:32, resumed 11:56 | Third-party front-end provider; root cause not stated | Afternoon on schedule[^pse-cn-2024-0003-update-market-halt:1][^pse-cn-2024-0002:1] |
| 9 Dec 2024 | Pre-open, no-cancel and open moved to 09:40, 09:50, 09:55 | No reason given | Later phases unchanged[^pse-cn-2024-0061-adjusted-schedule-2024-12-09:1] |
| 24 Mar 2025 | Open delayed to 11:10 (no-cancel 11:05) | "System connectivity issue" | PSEi closed −1.19% at 6,192.02 (press)[^pse-cn-2025-0014:1][^pse-cn-2025-0015-adjusted-schedule-2025-03-24:1][^wealthinsights-2025-03-24-tech-glitches] |

[Chapter 1](#/ch/market-architecture/outage-and-incident-record) lists the 2022–2025 incidents with circular numbers. That is eight system halts, cancellations or late opens in 2014–2025 against no breaker trigger since 2020 (the 4 Jun 2019 fire-drill halt, 11:45 to 13:30, was planned).[^pse-cn-2019-0031-trading-halt-fire-drill:1] Outage risk, not price risk, is the dominant halt risk.

### Execution implications

- Outage playbook: day cancelled (2022), halt and resume (2024), late open (2025). Do not rely on the closing auction on any day; expect "remaining market phases" to be compressed.
- When PSE announces the lifting of a system-failure halt it must do so at least five minutes ahead; use that window to re-validate resting orders. No such notice is specified for a breaker halt.
- Assume no trading when a PAGASA signal of 3 or higher is in force for NCR at 6:00 am, and when the central bank (BSP) or the PhilPaSS payment system suspends settlement operations.

## Single-stock halts and suspensions

### Halt, suspension, reservation and freeze compared

| State | Imposed by | Post / modify / cancel | Matching | Posted orders | ITCH state |
|---|---|---|---|---|---|
| Freeze | A breaching order | No | No | Held until Market Control acts | V + F |
| Reservation | Engine triggers, or manually before lifting a suspension | Yes, except crosses | No | Kept | Not separately documented |
| **Halt** | Exchange or SEC; issuer-requested | **Yes**, except crosses | No | **Kept** | T + H |
| **Suspension** | Exchange or SEC; CMIC | **No**; no TP may deal "directly or indirectly" | No | **Purged upon suspension** | V + S |

A halt is a "temporary stoppage … not lasting longer than one Trading Day"; the trading of any warrant, Philippine depositary receipt or other security deriving its value from the security is halted or suspended with it.[^pse-implementing-guidelines-trading-rules:26][^pse-implementing-guidelines-trading-rules:27][^pse-revised-trading-rules:34] The RTR text on purging is softer ("may be purged at the end of a Trading Day, as set out in the Implementing Guidelines"); the IG says "all posted Orders … shall be purged upon suspension", so the IG controls the timing (inference).[^pse-revised-trading-rules:34][^pse-implementing-guidelines-trading-rules:27] PSE executes the action and notifies the market simultaneously, and announces the resumption time before lifting.[^pse-implementing-guidelines-trading-rules:27] The Exchange or the SEC may halt or suspend, and either is lifted "upon compliance by the Issuer".[^pse-revised-trading-rules:33][^pse-revised-trading-rules:34]

### Lifting and resumption

The IG's Security Halt and Suspension Matrix sets the sequence:[^pse-implementing-guidelines-trading-rules:28]

| Case | Day 1 | Day 2 | Day 3 |
|---|---|---|---|
| 1 | Halted at the start or middle of the day, no compliance by end of day | Still no compliance: suspended | Compliance before 4 pm: resumes in pre-open. After 4 pm: 50 minutes suspended, then 10 minutes reserved |
| 2 | Halted; compliance within the day | Trading resumes | — |
| 3 | Voluntary or Exchange-initiated suspension | Compliance before 4 pm: resumes in pre-open. After 4 pm: 50 minutes suspended, 10 minutes reserved | — |

Counted from the 9:30 open, 50 plus 10 minutes is a **10:30 am** resumption. SuperCity Realty (SRDC) resumed at 10:30 on Fri 9 Jan 2026 and Xurpas at 10:30 on Tue 21 Jul 2026, and PSE's one-hour disclosure halt in MRC Allied ran 9:30–10:30 on 19 Jan 2026.[^bw-2026-01-09-srdc-resume][^insiderph-2026-07-20-xurpas-resumes][^pse-cn-2026-0004-2-emergency-disclosures-trading-halt:1-2] The link between the 10:30 resumptions and the matrix is my inference.

### Disclosure halts

Issuers must disclose material information to PSE within ten minutes, before it reaches the media. If the event occurs in trading hours, the issuer "must request a halt" (also when an after-hours event cannot be disclosed before pre-open). The halt is lifted one hour after dissemination, or on the next trading day if dissemination is within the last hour before the close; soft information and legally barred disclosures are exempt.[^pse-listing-disclosure-rules:139][^pse-listing-disclosure-rules:140] PSE can impose a halt itself: on 19 Jan 2026 it halted MRC Allied for one hour on a 315,000,000-share placement at ₱1.00 to two named subscribers, disclosed that morning after a 16 Jan board approval.[^pse-cn-2026-0004-2-emergency-disclosures-trading-halt:1-2] If PSE asks an issuer to confirm or deny a market rumour and gets no answer, it "shall impose a trading halt", lifted at 10:00 am even without a reply; the reply is due by 11:00 am or the issuer is fined ₱30,000 plus ₱10,000 for each further 30 minutes.[^pse-listing-disclosure-rules:145][^pse-listing-disclosure-rules:146] Other disclosure-driven suspensions (a substantial acquisition of an unlisted company, a transfer agent terminated without a replacement, a backdoor listing, which PSE suspends immediately after evaluating the disclosure and lifts one full trading day after the comprehensive disclosure) are in the ladder in [Chapter 2](#/ch/instruments/the-suspension-ladder).[^pse-listing-disclosure-rules:146][^pse-listing-disclosure-rules:148][^pse-sr7-backdoor-listing-2022:4]

<div class="callout warn">
<span class="label">Proposed, not found adopted</span>

PSE's November 2022 consultation (CN-2022-0045) proposed making disclosure halts voluntary ("may request") with PSE able to impose them, and dropping the automatic halt for unanswered rumour clarifications in favour of penalties.[^pse-cn-2022-0045-consultation-2022-part-ii:4][^pse-cn-2022-0045-consultation-2022-part-ii:30] The January 2025 consolidated rules still carry the old wording and no effectivity circular was found.[^pse-listing-disclosure-rules:139]
</div>

### Surveillance halts (CMIC)

CMIC monitors trading daily and, with the PSE President's approval, may restrict, halt or suspend a listed security, or trading by one TP in it, "upon breach of pre-established price and/or volume benchmarks or when CMIC deems it necessary". The benchmarks are not public. An order lasts until lifted, and only once the information is adequate; the SEC is told within 15 minutes if the market is open, or by 4:00 pm for next-day orders. When a price "exceeds or closes at or near the ceiling or floor price based on the approved price trading band", CMIC checks for prior disclosure and directs the issuer to file a sworn statement by **4:00 pm** on whether undisclosed information exists; non-compliance lets CMIC, without obliging it, issue an order, and an order is lifted no earlier than one hour after the statement is circulated and posted.[^pse-cmic-rules:112][^pse-cmic-rules:113]

SRDC shows the sequence (press reports): CMIC asked for an explanation on 7 Jan 2026 after the rise from ₱1.20 (18 Dec 2025) to ₱45.95 (7 Jan 2026); the company missed the deadline; PSE suspended trading at 9:00 am on Thu 8 Jan; SRDC filed a "not aware of any material information" statement late that day; trading resumed at 10:30 am on Fri 9 Jan.[^insiderph-2026-01-08-srdc-halt][^bw-2026-01-09-srdc-resume] Treat a name that sits at ceiling or floor for several sessions with no disclosure as a halt candidate.

### Compliance suspensions

| Trigger | Ladder under the Consolidated Listing and Disclosure Rules |
|---|---|
| Annual report (SEC Form 17-A) not filed | Due 105 days after fiscal year-end (+15 calendar days on PSE's extension format). Basic fine plus daily fines for 15 calendar days, a warning, then **automatic suspension for up to three months** (daily fines stop), then delisting procedures.[^pse-listing-disclosure-rules:151][^pse-listing-disclosure-rules:153] |
| Quarterly report (Form 17-Q) not filed | Due 45 days after quarter-end (+5 days). Fines for 10 days, then suspension of up to two months, then delisting procedures.[^pse-listing-disclosure-rules:151][^pse-listing-disclosure-rules:154] |
| Report filed but fines unpaid | Daily fines for 15 (17-A) or 10 (17-Q) days, then suspension of up to three or two months.[^pse-listing-disclosure-rules:153][^pse-listing-disclosure-rules:155] |
| Unstructured-disclosure fine unpaid for one month | Suspension of trading.[^pse-listing-disclosure-rules:160] |
| Minimum public ownership (MPO) breached | **Immediate** suspension for up to six months from the breach, then automatic delisting; a Compliance Plan does not defer the suspension.[^pse-amended-mpo-rule-2026-08:6] |

In practice the "maximum three months" is not a cap: Island IT stayed suspended 1,572 days (18 Mar 2021 to 7 Jul 2025) before filing.[^philstar-2025-07-07-island-it-resumption] Del Monte Pacific (September 2025) and Xurpas (2 Jun to 21 Jul 2026) were suspended for missed filings,[^bw-2025-09-17-delmonte-suspended][^insiderph-2026-07-20-xurpas-resumes] and on 24 Aug 2026 six of the seven Villar-group companies (about ₱320 billion of market value) had been suspended for nearly three months over overdue filings.[^insiderph-2026-08-24-villar-frozen] PSE's data on 6 Oct 2026 still marked eleven symbols, most of them Villar-group names, as Suspended with last trades on 29 May or 1 Jun 2026, beyond the three-month ceiling (outcome unverified), and listed 65 of 385 securities with live frames as suspended (29 common, 36 preferred), so a suspended-state filter is a live requirement.[^pse-sec-frames-snapshot]

The full ladder (including unpaid listing fees, missed listing-application deadlines and sponsor failures) and the MPO tiers and cases (ATI, RRHI, Steniel, Metro Global) are in [Chapter 2](#/ch/instruments/the-suspension-ladder); holder-side duties are in [Chapter 13](#/ch/regulatory-constraints/minimum-public-ownership-the-holders-view). One MPO point belongs here because it is a liquidity event: after the JE Holdings tender offer for Robinsons Retail (RRHI) closed on 6 Jul 2026, PSE suspended the stock from 13 Jul and removed it on 31 Aug, so the tender window was the last on-exchange exit.[^insiderph-2026-07-13-rrhi-suspension][^philstar-rrhi-suspension][^pse-cn-2026-0038-rrhi-voluntary-delisting:1]

### Broker-level stoppages

CMIC can suspend a Trading Participant, voluntarily or involuntarily (grounds include an SEC take-over order, clearing-agency suspension, failure to restore a risk-based capital ratio of 1.1 or net liquid capital of ₱5 million, an unimpaired paid-up capital shortfall, and "grave violation" of the securities laws). The suspension automatically suspends the Trading Right, deactivates the broker's access to the trading system, and freezes its accounts at the clearing agency and the depository; clients may transfer or sell only with CMIC approval, as in the Mount Peak (13 Aug 2025) and Benjamin Co Ca (31 Jul 2026) notices.[^pse-cmic-rules:106][^pse-cmic-rules:107][^pse-cmic-rules:108][^pse-tpa-2025-0050-mount-peak-involuntary-suspension:2][^pse-tpa-2026-0035-benjamin-co-ca-involuntary-suspension:2] The case record is in [Chapter 1](#/ch/market-architecture/broker-failure-and-the-safety-net). A suspended individual trader can be reinstated only if at least one hour remains before the close.[^pse-implementing-guidelines-trading-rules:10]

### Execution implications

- Build a per-security state machine: trading, frozen, reserved, halted (orders kept, no matching), suspended (orders purged), with resumption at pre-open or 10:30, and drive it from circulars, PSE's EDGE disclosure system and the feed together. EDGE itself has been unavailable on 19 Jan and 6 Oct 2026 ([Chapter 11](#/ch/market-data/corporate-disclosure-dissemination-pse-edge)), so do not rely on a single scraper.
- Pre-trade screens: late-filing calendar (17-A day 105 or 120, 17-Q day 45 or 50), float cushion against the MPO tier, sustained limit-up or limit-down without disclosure, and live tender offers (the tender window can be the last on-exchange exit before a suspension).
- Orders resting through a suspension are gone; resting orders through a halt remain. Re-enter after resumption and expect the first print to be unbounded if the band was lifted.
- Spread flow across brokers: a broker suspension restricts clients to CMIC-approved transfers.

## How states and collars appear in the feed

The legacy X-stream ITCH specification (v2.3, copyright 2014) carries the controls in two per-order-book messages.[^pse-itch-equities-feed-spec-v2-3:12][^pse-itch-equities-feed-spec-v2-3:13]

| Field or state | Meaning |
|---|---|
| Restrictions [k]: Short Sell Eligible | Y or N (a further "B" value was added in spec v2.1; see [Chapter 9](#/ch/short-selling)) |
| Restrictions [k]: High Collar, Low Collar | "Maximum / minimum allowed price via static limit"; 2147483647 means no limit |
| Restrictions [k]: CB Limit Up %, Down % | "Circuit breaker" maximum movement as a percentage from the LTP (the dynamic limit); 0 means no limit; a decimals field scales both |
| Trading Action [H]: T + N | Trading, normal |
| [H]: V + S | Suspended by market control; lifted with T + N |
| [H]: V + F | Frozen due to the dynamic limit; thawed with T + N |
| [H]: T + H | Halted ("intraday auction"); lifted with T + N |

"Circuit breaker" in these fields means the stock-level dynamic limit, not the PSEi breaker, and the system event codes (pre-open, no-cancel, break, pre-close, trading at last) contain no market-wide halt code.[^pse-itch-equities-feed-spec-v2-3:10][^pse-itch-equities-feed-spec-v2-3:14] Other points from the spec: [k] is sent at the start of the day and may be re-sent intraday; a group-wide suspension is signalled by an [H] message for every order book in the group; the reference price arrives as an Add Order [A] message with order number and quantity zero (Total View) or a BBO message [O] with size fields at 0x7FFFFFFFFFFFFFFF (Basic feed); a halt generates indicative price messages with auction type "I" (intraday auction); and an order that executes on thawing after a freeze may arrive as an Order Executed With Price [C] message.[^pse-itch-equities-feed-spec-v2-3:25][^pse-itch-equities-feed-spec-v2-3:26][^pse-itch-equities-feed-spec-v2-3:27][^pse-itch-equities-feed-spec-v2-3:28] Rejections surface in FIX as ExecType Rejected; the 2015 FIX spec defines only OrdRejReason 5, 6 and 99 ("Other — refer to Text"), so threshold and phase rejects will probably arrive as 99 with free text (inference; the Eqlipse FIX specification of July 2026 is not archived here).[^pse-fix-specification-v2-5:52]

<div class="callout infer">
<span class="label">Inference</span>

The feed states line up with the rulebook: V + F is the freeze, V + S the suspension (orders purged) and T + H the halt or reservation (orders can be entered, modified and cancelled but nothing matches). The spec does not say whether an uncross runs when a T + H state is lifted. A security with no band (a warrant) or a lifted band should publish the no-limit collar value (inference). Because a market-wide halt would be a group suspension, expect a burst of [H] messages across constituents rather than a single event.
</div>

### Execution implications

- Drive the per-security state machine from [H] (state and reason) and the system events, and take ceiling, floor and DT corridor from [k] each day and on any intraday re-send, instead of recomputing them.
- Do not infer a PSEi breaker from a single order book: look for [H] changes across the group together with the index drawdown from the Index feed.
- Treat every field above as XTS-era; re-map them when the NTE ITCH and market-data specifications are certified.

## Scheduled change: Nasdaq Eqlipse (23 Nov 2026)

<div class="callout warn">
<span class="label">Scheduled change: 23 Nov 2026 (not in force)</span>

PSE's broker forum of 9 Jul 2026 set a big-bang go-live of the Nasdaq Eqlipse engine for Mon 23 Nov 2026 after Saturday rehearsals on 31 Oct, 7 Nov and 14 Nov, with no parallel run.[^pse-nte-broker-forum-2026-07-09:9][^pse-nte-faq-2026-08:1] Day 1 supports only limit orders, so the market-order reservation triggers cannot fire (inference); lot size becomes one share and the odd-lot market disappears; run-off orders may be entered, modified and executed only at the closing price.[^pse-nte-faq-2026-08:1][^pse-nte-broker-forum-2026-07-09:7] None of the archived NTE documents states whether the static band, dynamic thresholds, freeze process, reservation, circuit breakers or ITCH collar fields change; the NTE ITCH and market-data specifications (v1.2, July 2026) are not archived here. Version-gate every rule in this chapter by engine, and regression-test collars, freeze states, halt codes and reject reasons on the first day.
</div>

## What is not in the public record

- The numerical "allowable percentage price difference" for static breaches, and whether the 60% step survives the 2020 change.
- How the ACP is computed after dividends, splits and rights, and the IPO and follow-on first-day price-limit rule.
- ETF-, REIT- and dollar-denominated-security-specific price-limit provisions (none found; the ETF and DDS rule PDFs may be scanned images). DDS rules apply the Revised Trading Rules by reference, so today's band follows (see [Chapter 2](#/ch/instruments)).
- Order treatment at a PSEi breaker halt (kept or purged), re-opening mechanism (auction or continuous), how a breaker halt is broadcast, and updated cut-off clock times for the 14:45 pre-close.
- CMIC's price and volume benchmarks; annual statistics of halts and suspensions; any SEC-ordered halt in recent years.
- Whether the 2022 disclosure-halt proposals were adopted after January 2025.
- Root causes of the 3 Jan 2024, 9 Dec 2024 and 24 Mar 2025 incidents, and any NTE failover or halt procedure.
