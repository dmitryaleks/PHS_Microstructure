---
number: 3
slug: sessions
title: Trading Sessions and Calendar
summary: One whole-day session, 09:00-15:15, with two call auctions, hard no-cancel windows, a recess and a VWAP-only last 15 minutes; closures arrive by circular and the engine changes on 23 Nov 2026.
part: Trading mechanics
---

The Philippine Stock Exchange (PSE) trades one session, Monday to Friday: two continuous blocks split by a 60-minute recess, a call auction at each end, and a closing price struck at 14:50, 25 minutes before the official close. Ordinary orders stop at 15:00; the last 15 minutes (15:00-15:15) belong to a VWAP-only facility that a normal order cannot reach.[^pse-approved-rules-vwap-trading-2024:3][^pse-approved-rules-vwap-trading-2024:7] PSE publishes no consolidated rulebook: what follows is the June 2010 Revised Trading Rules (RTR) and Implementing Guidelines (IG) as amended by dated memoranda, so memo numbers and dates are the stable keys.[^pse-web-regulatory-framework]

Three behaviours most often break assumptions carried over from other venues. First, the **close is not the closing price**: the closing price is struck at 14:50, run-off orders execute only at it, and 15:15 only ends the VWAP window; a pipeline that still assumes the 15:30 close that ran until March 2020 is wrong. Second, the day has **hard no-touch windows**: nothing can be cancelled after 09:15:00 or 14:48:00, and nothing at all can be entered, changed or cancelled during the 12:00-13:00 recess. Third, the **calendar is not a published table**: closures arrive by circular days to weeks ahead, a typhoon rule keyed to the NCR wind signal at 06:00 can cancel a day, and PSE's position on 16-18 Nov 2026 is unresolved. A new engine replaces PSEtrade XTS on 23 Nov 2026; no session times are announced to change, but several phase behaviours are slated to ([the cut-over section](#/ch/sessions/the-23-november-2026-engine-cut-over)).

## The trading day

The RTR lets the Exchange "determine the hours and schedule of a Trading Day"; unless it decides otherwise the schedule below applies, and it "may effect changes ... as the circumstance warrants".[^pse-approved-rules-vwap-trading-2024:3] That clause is how the shortened, half-day and late-open schedules since 2020 were imposed, by circular with notice from none (same-day late opens) to 14 days.

| PHT | UTC | Phase (PSE name) | Length | What participants may do |
|---|---|---|---|---|
| 09:00:00 | 01:00 | **Pre-Open** | 15 min | No matching. Enter, modify and cancel orders; they queue for the opening-price calculation |
| 09:15:00 | 01:15 | **Pre-Open No-Cancel** | 15 min | Enter only; no modification, no cancellation |
| 09:30:00 | 01:30 | **Market Open** ("Opening") | not stated | Opening price calculated and orders matched at it; book frozen: no entry, modification or cancellation |
| 09:30 | 01:30 | Continuous trading | 150 min | Orders match automatically at the best price; enter, modify, cancel |
| 12:00:00 | 04:00 | **Market Recess** | 60 min | Trading halted for all securities; no entry, modification or cancellation |
| 13:00:00 | 05:00 | **Market Resume** (continuous) | 105 min | As above |
| 14:45:00 | 06:45 | **Pre-Close** | 3 min | "Same as Pre-Open": enter, modify, cancel; orders queue for the closing-price calculation |
| 14:48:00 | 06:48 | **Pre-Close No-Cancel** | 2 min | Enter only |
| 14:50:00 | 06:50 | **Run-off / Trading-at-Last** | 10 min | Orders at the Closing Price only |
| 15:00:00 | 07:00 | **Closing VWAP Session** | 15 min | VWAP transactions only; no ordinary orders |
| 15:15:00 | 07:15 | **Market Close** | - | End of trading; no entry, modification or cancellation |

Times and phase names are RTR Article II Section 2 as restated on 1 Feb 2024; the phase descriptions are IG Part II.[^pse-approved-rules-vwap-trading-2024:3][^pse-approved-rules-vwap-trading-2024:6] PSE's Investing page shows the same table and "Trading days are from Monday to Friday, 9:00 a.m. to 3:15 p.m." (retrieved 6 Oct 2026).[^pse-web-investing-at-pse] The morning, afternoon and pre-close times have been unchanged since 1 Mar 2022, the VWAP session and 15:15 close since 1 Mar 2024.[^pse-cn-2022-0009-trading-schedule-mar-2022:1][^pse-cn-2024-0012-vwap-go-live:1] UTC is PHT minus eight hours (no daylight saving). Lengths are derived: continuous matching totals 255 minutes (150 + 105); the auctions take 30 minutes at the open and 5 at the close.

### Phase mechanics

- **Pre-Open and Pre-Close** are periods in which orders "accepted and queued are considered in the determination of" the opening or closing price and do not trade until the market opens or moves to run-off. **Run-off / Trading-at-Last** is "the period after the Pre-Close when Orders are accepted and executed only at the Closing Price".[^pse-revised-trading-rules:10-11] The uncross rules are in [Chapter 6](#/ch/auctions).
- **Run-off.** RTR Article IV Section 18: all run-off orders execute only at the Closing Price and "in cases where prices of posted Orders in the Order book are better than the Closing Price, no Orders will be accepted".[^pse-revised-trading-rules:27] The IG wording of what may be entered changed: limit orders "or Market Orders" at the Closing Price (2010, restated Nov 2013); limit orders only (Dec 2011); "Orders at the Closing Price only" (2024).[^pse-implementing-guidelines-trading-rules:4][^pse-tpa-2013-0185-extended-pre-close:7][^pse-tpa-2011-0124-amended-implementing-guidelines:3][^pse-approved-rules-vwap-trading-2024:6] Whether run-off orders may be amended or cancelled is contradicted between the IG and the ITCH state table; design for no cancel ([Chapter 4](#/ch/order-types/cancellation-mass-cancel-and-disconnects)).
- **The 09:30 freeze.** No rule states how long the book stays frozen while the opening price is computed.[^pse-approved-rules-vwap-trading-2024:6] A July 2026 draft restatement adds that orders "are matched at the Opening Price" in that step.[^pse-cn-2026-0031-negotiated-trades:8]
- **Dropped items.** The 2010 IG also listed an 08:45 national-anthem item and Market Control start-of-day and end-of-day actions; neither is in the 2024 restatement.[^pse-implementing-guidelines-trading-rules:4-6][^pse-approved-rules-vwap-trading-2024:5-6]
- **No extended session.** Nothing follows run-off except the Closing VWAP Session, and no extended-hours session for ordinary orders is proposed in any PSE or SEC document found ([Chapter 17](#/ch/reform-timeline)).

<div class="callout">
<span class="label">Consequence</span>

The last second to cancel or modify is 09:14:59 for the open and 14:47:59 for the close (derived from the phase start times). After 14:48:00 closing-auction interest is locked; after 14:50:00 only closing-price orders exist, and because they execute at a price already fixed, run-off flow cannot move the official close.[^pse-revised-trading-rules:27] A closing-benchmark algorithm must commit before 14:48:00 and treat anything sent 14:48-14:50 as irrevocable.
</div>

### Half-day schedule (dormant)

The RTR carries a half-day timetable, restated on 1 Feb 2024: 09:00 Pre-Open, 09:15 No-Cancel, 09:30 Open, 11:57 Pre-Close, 11:59 Pre-Close No-Cancel, 12:00 Run-off, 12:10 Closing VWAP Session, 12:25 Market Close.[^pse-approved-rules-vwap-trading-2024:3][^pse-approved-rules-vwap-trading-2024:5] Its last documented use was 24 and 31 Dec 2021, with different pre-close timings (11:55, 11:58, 12:00, close 12:10, no VWAP session yet).[^pse-cn-2021-0063-half-day-trading-2021-12:1] PSE closed on both dates in 2025 outright, and 24 and 31 Dec 2026 are special non-working days under Proclamation 1006, so no half-day session is scheduled and the table is dormant (inference); keep it parameterised.[^pse-cn-2025-0043-non-trading-days:1][^pse-cn-2026-0008:3]

### Disruptions and late opens

A late open is handled by a same-day "adjusted schedule" circular that re-times only the affected opening phases and keeps the rest of the day: on 9 Dec 2024 Pre-Open moved to 09:40, No-Cancel to 09:50 and Open to 09:55; on 24 Mar 2025 No-Cancel moved to 11:05 and Open to 11:10 with later phases unchanged.[^pse-cn-2024-0061-adjusted-schedule-2024-12-09:1][^pse-cn-2025-0014:1][^pse-cn-2025-0015-adjusted-schedule-2025-03-24:1] Where the circular says so the close was not extended: 20 Nov 2014 (halt 13:46, resumed 14:30, close 15:30 as scheduled), 4 Jun 2019 (fire-drill halt from 11:45, resumed 13:30, "no changes in the remaining market phases") and 3 Jan 2024 (halt 09:32 to 11:56, afternoon "as scheduled").[^pse-cn-2014-0057-trading-halt-2014-11-20:1][^pse-cn-2019-0031-trading-halt-fire-drill:1][^pse-cn-2024-0001-market-halt:1][^pse-cn-2024-0003-update-market-halt:1] The one day lost to a technical failure was 4 Jan 2022, when the open was delayed (43 of 125 TPs could not connect) and trading was then cancelled.[^pse-cn-2022-0001-delay-market-opening:1][^pse-cn-2022-0002-cancellation-of-trading-2022-01-04:1] The full incident record is in [Chapter 1](#/ch/market-architecture) and [Chapter 7](#/ch/price-controls).

The base rules distinguish a market halt, a suspension (all trades and posted orders for the day stay valid) and a **cancellation of a scheduled day**, which the President may impose if announced within one hour after the Pre-Open Period and under which all trades and posted orders for the day are purged.[^pse-revised-trading-rules:35-36] On a whole-day schedule a halt gets no extension of hours except to complete the remaining phases, and the Exchange has sole discretion to suspend or cancel the day if a halt lasts more than two hours or 15 minutes beyond the Run-Off Period; the IG states that limit as 15:45, written for the old 15:30 close and never restated.[^pse-tpa-2011-0110-amended-revised-trading-rules:6][^pse-tpa-2011-0124-amended-implementing-guidelines:4-6] The market-wide halt trigger and the index circuit breaker, whose clock cut-offs were also written for the old 15:15 pre-close and not republished, are in [Chapter 7](#/ch/price-controls).

### Execution implications

- **Drive the state machine from the feed, not only a clock.** The XTS-era ITCH feed publishes phase events and a Trading Schedule message giving each event's scheduled time in seconds after midnight ([Chapter 6](#/ch/auctions)).[^pse-itch-equities-feed-spec-v2-3:10-11] A clock-only model breaks on 9 Dec 2024 (open 09:55) and 24 Mar 2025 (open 11:10). The NTE feed specification is not public.
- **Schedule defensively against circulars.** CN-2021-0059 gave 14 days' notice; CN-2020-0017 gave one.[^pse-cn-2021-0059:1][^pse-cn-2020-0017:1] Hold the ten timestamps as configuration with an override channel.
- **Commit closing-benchmark orders before 14:48.** There is no ordinary-order path from 15:00 to 15:15; VWAP prints use a separate facility. PSE says Negotiated Trades will run on "a web-based platform, similar to the VWAP facility",[^pse-nte-faq-2026-08:1] which implies the VWAP facility is not reachable over FIX order entry (inference).
- **Treat the recess as a hard stop.** Resting day orders stay in the book, but anything that must change has to change before 12:00:00.

## Special trades by session

Which facilities run in which phase decides what can be done outside the central order book. Blocks and crosses are detailed in [Chapter 5](#/ch/matching), short selling in [Chapter 9](#/ch/short-selling).

| Facility | Pre-Open 09:00-09:30 | Continuous | Recess 12:00-13:00 | Pre-Close 14:45-14:50 | Run-off 14:50-15:00 | VWAP session 15:00-15:15 |
|---|---|---|---|---|---|---|
| Normal-market orders | Enter; modify/cancel until 09:15 | Yes | No | Enter; modify/cancel until 14:48 | Closing-price orders only | No |
| Odd-lot board | No | Yes, only here | No | No | No | No |
| Cross | No | Yes, inside the BBO | No | No | Yes, at the Closing Price | No |
| Block sale | Yes (approval after hours executes in the next Pre-Open) | Yes | Yes | Yes | Yes | Not per the rule text (inference) |
| VWAP trade | No | No | No | No | No | Yes |
| Short-sell order | No (rejected) | Yes (uptick rule, Day orders) | No | No (rejected) | Yes | No |

Sources: odd lots;[^pse-revised-trading-rules:26][^pse-implementing-guidelines-trading-rules:19-20] crosses;[^pse-revised-trading-rules:31] block sales;[^pse-tpa-2011-0110-amended-revised-trading-rules:5][^pse-implementing-guidelines-trading-rules:25] VWAP;[^pse-approved-rules-vwap-trading-2024:4][^pse-approved-rules-vwap-trading-2024:7] short sales.[^pse-short-selling-guidelines-2023-10:2][^pse-cn-2019-0004-short-selling-guidelines-amendment:1]

- **Block sales** run "from the Market Pre-Open to the Trading-at-Last/Run-Off period, including Market Recess", the only way to print between 12:00 and 13:00. The application must be filed before the Run-Off Period (the 2010 text said by 12 noon) and needs prior Exchange approval; thresholds and process are in [Chapter 5](#/ch/matching).[^pse-tpa-2011-0110-amended-revised-trading-rules:5][^pse-tpa-2011-0124-amended-implementing-guidelines:4]
- **Odd lots** have "no Pre-Open, Pre-Close and Run-Off/Trading-at-Last Period".[^pse-implementing-guidelines-trading-rules:20] A board-lot residual therefore cannot be cleaned up in the closing auction or run-off (inference).
- **Short sales.** The system rejects short-sell orders only in Pre-Open and Pre-Close; PSE corrected its June 2018 guidelines (which had also barred run-off) on 23 Jan 2019 to match the RTR. Orders must be Day orders, cannot be aggregated, and are not accepted in the odd-lot market or for block sales.[^pse-short-selling-guidelines-2023-10:2][^pse-cn-2019-0004-short-selling-guidelines-amendment:1] The uptick test makes run-off short sales hard to execute at a fixed closing price (inference).

### The Closing VWAP Session

| Parameter | Rule |
|---|---|
| Window | Within 15 minutes after run-off: 15:00-15:15 (half-day 12:10-12:25)[^pse-approved-rules-vwap-trading-2024:7] |
| Price | The full-day VWAP computed by the Exchange, at most four decimals; all transactions are "executed only at the VWAP computed by the Exchange"[^pse-approved-rules-vwap-trading-2024:4][^pse-approved-rules-vwap-trading-2024:7] |
| Minimum value | PHP 500,000 (the Sep 2023 consultation draft proposed PHP 1 million)[^pse-approved-rules-vwap-trading-2024:7][^pse-cn-2023-0043:17] |
| Counterparty | One trading participant only; a two-firm facility is reserved to the Exchange, subject to prior SEC approval[^pse-approved-rules-vwap-trading-2024:7] |
| VWAP population | All trades except block sales, intentional crosses and odd-lot trades[^pse-approved-rules-vwap-trading-2024:7] |
| Not allowed | Suspended or halted securities[^pse-approved-rules-vwap-trading-2024:4] |
| Delay rule | If the VWAP display is delayed the session is suspended; it resumes if at least five minutes remain, otherwise VWAP trading is cancelled for the day[^pse-approved-rules-vwap-trading-2024:7] |
| Controls | Authorised salesmen/traders only; the per-trader order value limit applies; reported in end-of-day reports[^pse-approved-rules-vwap-trading-2024:4][^pse-approved-rules-vwap-trading-2024:7] |
| Status | SEC-approved, effective immediately on 1 Feb 2024 (CN-2024-0010); launched 1 Mar 2024 (CN-2024-0012)[^pse-approved-rules-vwap-trading-2024:1][^pse-cn-2024-0012-vwap-go-live:1] |

### Execution implications

- Large pre-arranged prints need broker-side block approval, and a block with a pre-set execution date is announced on PSE's website with security, size, price and date; do not expect size to stay hidden until execution day ([Chapter 5](#/ch/matching)).[^pse-implementing-guidelines-trading-rules:25]
- Work odd-lot residuals in the odd-lot book during continuous trading; there is no auction path. This disappears if One Lot One Share is approved ([Chapter 4](#/ch/order-types)).
- Use the VWAP session for benchmark-VWAP mandates, not to influence a close that is already fixed; treat 15:00-15:15 as unavailable to a standard FIX router.
- Short-selling algorithms must suppress the sell-short flag in the pre-open and pre-close and send Day orders only.

## Schedule history since 2010

| Effective | Change | Resulting PHT schedule | Memo / approval |
|---|---|---|---|
| Before 26 Jul 2010 | Maktrade era: morning session only (secondary source); a 2008 Board plan for 09:00-12:00 and 14:00-16:00 was postponed | 09:30-12:00[^philstar-2008-12-04-extended-hours] | CN-2011-0002 (28 Jun 2011)[^pse-cn-2011-0002:1] |
| 26 Jul 2010 | New trading system launches; RTR and IG take effect; half-day trading only | 08:45 anthem; 09:00 pre-open; 09:15-09:30 no-cancel; 09:30 open; 11:57-11:59 pre-close; 11:59-12:00 no-cancel; 12:00 run-off; 12:10 close. A whole-day schedule was defined (resume 14:00, pre-close 15:45, run-off 15:50, close 16:00) but never used | RTR approved by the SEC 1 Jun 2010 (PSE memo 8 Jun); IG memo 22 Jul 2010[^pse-revised-trading-rules:1-2][^pse-revised-trading-rules:13][^pse-implementing-guidelines-trading-rules:1][^pse-implementing-guidelines-trading-rules:4-6] |
| 28 Jul 2011 (proposal) | Board (13 Jul) approves extension to 15:30 in two phases: 1 Oct 2011 (09:00-13:00) and 1 Jan 2012 (09:00-12:00, 13:30-15:30) | Proposal only | TPA 2011-0030.[^pse-memo-extended-trading-proposal-2011:1-2] Whether Phase 1 ran is unconfirmed; PSE's 2013 memo gives pre-2012 trading time as 2 h 40 min (09:30-12:10), which suggests it did not (inference)[^pse-memo-extended-pre-close-consultation-2013:1] |
| **2 Jan 2012** | Whole-day trading begins | 08:45 anthem; 09:00 pre-open (09:15 no-cancel); 09:30 open; 12:00 recess; **13:30** resume; **15:17** pre-close auction (15:17-15:19), no-cancel 15:19-15:20; 15:20 run-off; 15:30 close | TPA 2011-0108 (6 Dec 2011); CN-2011-0025 (26 Dec); rule amendments TPA 2011-0110 (7 Dec); IG amendments TPA 2011-0124 (28 Dec); SCCP memo 03-1211 (settlement deadline stayed at noon)[^pse-memo-new-trading-hours-2011:1][^pse-cn-2011-0025:1][^pse-tpa-2011-0110-amended-revised-trading-rules:1][^pse-tpa-2011-0124-amended-implementing-guidelines:2-3][^sccp-memo-03-1211-settlement-unchanged-extended-hours:1] |
| **4 Nov 2013** | Pre-close lengthened from 3 to 5 minutes (peers cited: Bursa 5, SGX 6, SET 10, IDX 10, HoSE 15) | Pre-close 15:15-15:18; no-cancel 15:18-15:20; run-off 15:20-15:30; close 15:30 | Board 10 Jul; TPA 2013-0107 (17 Jul); SEC letter 26 Sep; TPA 2013-0165 (14 Oct), 2013-0167 (16 Oct), 2013-0185 (14 Nov)[^pse-memo-extended-pre-close-consultation-2013:1-2][^pse-memo-extended-pre-close-implementation-2013:1][^pse-memo-pre-close-schedule-2013:1][^pse-tpa-2013-0185-extended-pre-close:1] |
| 22 Jun 2015 | Migration to PSEtrade XTS (Nasdaq X-stream) | No hours change | PSE annual report 2015[^pse-annual-report-2015:42] |
| **16 Mar 2020** | COVID shortened hours (a 08:30/09:00 variant announced for 17 Mar-14 Apr was never used); no trading 17-18 Mar (Luzon ECQ); resumed 19 Mar with the trading floor closed; extended to 30 Apr, 15 May, then "until further notice" under MECQ | 09:00 pre-open; 09:30 open; 12:45 pre-close; 12:50 run-off; 13:00 close; no recess | CN-2020-0017 (15 Mar), 0021 (16 Mar), 0025 (17 Mar), 0035 (13 Apr), 0042 (27 Apr), 0046 (14 May)[^pse-cn-2020-0017:1][^pse-cn-2020-0021:1][^pse-cn-2020-0025-resumption-of-trading:1][^pse-cn-2020-0035:1][^pse-cn-2020-0042:1][^pse-cn-2020-0046:1] |
| **6 Dec 2021** | New full-day schedule | 09:00 pre-open; 09:30 open; 12:00 recess; **13:00** resume; **14:45** pre-close; **14:50** run-off; **15:00** close (no-cancel phases not listed) | CN-2021-0059 (22 Nov 2021)[^pse-cn-2021-0059:1] |
| 24, 31 Dec 2021 | Half-day trading | 09:00 / 09:15 / 09:30 / 11:55 pre-close / 11:58 no-cancel / 12:00 run-off / 12:10 close | CN-2021-0063 (15 Dec)[^pse-cn-2021-0063-half-day-trading-2021-12:1] |
| 14 Jan-28 Feb 2022 | Omicron shortened hours | 09:00 / 09:15 / 09:30 / 12:45 pre-close / 12:48 no-cancel / 12:50 run-off / 13:00 close | CN-2022-0004 (11 Jan) covers 14-31 Jan[^pse-cn-2022-0004:1]; the run to 28 Feb is implied by CN-2022-0009 ("Further to CN-2022-0004"); no extension memo found (inference) |
| **1 Mar 2022** | Full-day schedule restored, no-cancel phases listed | 09:00 / 09:15 / 09:30 / 12:00 / 13:00 / 14:45 / 14:48 / 14:50 / 15:00 | CN-2022-0009 (17 Feb)[^pse-cn-2022-0009-trading-schedule-mar-2022:1] |
| **1 Mar 2024** | Closing VWAP Session introduced; close moves from 15:00 to 15:15 (half-day 12:25) | ... 14:50 run-off; 15:00 Closing VWAP; 15:15 close | CN-2024-0010 (1 Feb 2024), CN-2024-0012 (15 Feb)[^pse-approved-rules-vwap-trading-2024:1][^pse-approved-rules-vwap-trading-2024:3][^pse-cn-2024-0012-vwap-go-live:1] |
| 23 Nov 2026 (scheduled) | Engine change; session times not announced to change | See [the cut-over section](#/ch/sessions/the-23-november-2026-engine-cut-over) | Broker forum, 9 Jul 2026[^pse-nte-broker-forum-2026-07-09:9] |

<div class="callout infer">
<span class="label">Inference</span>

PSE's CN-2021-0059 says that from 6 Dec 2021 it "will go back to its pre-pandemic full day-5-hour trading schedule". It was not a return: the schedule that ran from 2 Jan 2012 to 13 Mar 2020 resumed at 13:30, entered pre-close at 15:15 and closed at 15:30.[^pse-cn-2021-0059:1][^pse-memo-pre-close-schedule-2013:1] The afternoon moved 30 minutes earlier and the last print from 15:30 to 15:00. This chapter gives the dated schedules and does not use PSE's label. The RTR Article II text still read 13:30 / 15:15 / 15:30 when PSE drafted its September 2023 consultation, so the 2021-22 schedules ran under the "unless the Exchange decides otherwise" clause and the article was restated only on 1 Feb 2024.[^pse-cn-2023-0043:11][^pse-approved-rules-vwap-trading-2024:3]
</div>

<div class="callout warn">
<span class="label">Stale sources and drifting article numbers</span>

PSE's Investing page prose still says trading runs "9:30 AM to 12:00 NN and 1:30 PM to 3:30 PM" next to a schedule table showing the current timetable, and a First Metro Securities help article (post dated 13 Feb 2015) still shows the 2020-21 shortened hours; such prose is the likeliest source of wrong "15:30 close" assumptions in post-2021 data (inference).[^pse-web-investing-at-pse][^firstmetrosec-help-34] Article numbers also drift: after VWAP became RTR Article VI (Feb 2024), CN-2025-0037 still cites Article VIII for Market Halt and CN-2026-0031 cites Article VII for crosses, blocks and negotiated trades.[^pse-cn-2025-0037:3][^pse-cn-2026-0031-negotiated-trades:7] Cite memo numbers and dates, not article numbers.
</div>

### Execution implications

- **Version-gate every history-dependent parameter by date.** The official close was 15:30 until 13 Mar 2020; 13:00 from 16 Mar 2020 to 3 Dec 2021 and again 14 Jan-28 Feb 2022; 15:00 from 6 Dec 2021 to 29 Feb 2024 (except that window); 15:15 since 1 Mar 2024. The last continuous print is never the official close.
- Pre-close started at 15:17 (2 Jan 2012 to 1 Nov 2013), 15:15 (4 Nov 2013 to 13 Mar 2020), 12:45 (shortened hours) and 14:45 (from 6 Dec 2021); the closing no-cancel window was one minute until 1 Nov 2013 and two minutes since where listed. Any closing-auction study spanning these dates needs the regime for each trade date.
- Do not read a close time off PSE's website prose or a broker help page; use the circular for the date in question.

## Trading calendar

### Rule and announcement practice

RTR Article II Section 1: "Every day shall be a Trading Day except for Saturdays, Sundays, legal holidays, special holidays, days when the Bangko Sentral ng Pilipinas (BSP) is closed, and such other days as may otherwise be declared by the SEC or the Exchange, through its President or other duly authorized representative, to be a non-Trading Day."[^pse-revised-trading-rules:13] Absent an announced suspension, trading proceeds as usual; suspensions are announced through mass media, the website and SMS.[^pse-memo-trading-days-suspensions-guidelines-2012:1]

PSE follows the Presidential proclamations and issues one circular per month or event. In 2026 the lead time has run from 4 days (12 Jun, announced 8 Jun) to 25 days (21 and 31 Aug, announced 27 Jul); emergency closures are announced the evening before or the same day. Eid'l Fitr and Eid'l Adha are proclaimed only once the dates are determined: Proclamation 1189 (12 Mar) gave eight days for 20 Mar and Proclamation 1264 (21 May) six days for 27 May.[^pse-cn-2026-0008:3][^pse-cn-2026-0010:1][^pse-cn-2026-0023:1]

### 2026 closures

| Date (2026) | Day | Reason | PSE circular (date) |
|---|---|---|---|
| 1 Jan | Thu | New Year's Day | CN-2025-0043 (24 Nov 2025; also closed 8, 24, 25, 30, 31 Dec 2025)[^pse-cn-2025-0043-non-trading-days:1] |
| 17 Feb | Tue | Chinese New Year | CN-2026-0008 (29 Jan)[^pse-cn-2026-0008:1] |
| 20 Mar | Fri | Eid'l Fitr | CN-2026-0010 (13 Mar)[^pse-cn-2026-0010:1] |
| 2, 3, 9 Apr | Thu, Fri, Thu | Maundy Thursday, Good Friday, Araw ng Kagitingan | CN-2026-0011 (24 Mar)[^pse-cn-2026-0011:1] |
| 1 May | Fri | Labor Day | CN-2026-0016 (24 Apr)[^pse-cn-2026-0016:1] |
| 27 May | Wed | Eid'l Adha | CN-2026-0023 (22 May)[^pse-cn-2026-0023:1] |
| 12 Jun | Fri | Independence Day | CN-2026-0027 (8 Jun)[^pse-cn-2026-0027:1] |
| 21, 31 Aug | Fri, Mon | Ninoy Aquino Day, National Heroes Day | CN-2026-0034B (27 Jul)[^pse-cn-2026-0034b-non-trading-days-aug-2026:1] |
| 2, 30 Nov | Mon, Mon | All Souls' Day, Bonifacio Day | None yet; Proclamation 1006[^pse-cn-2026-0008:3] |
| 8, 24, 25, 30, 31 Dec | Tue, Thu, Fri, Wed, Thu | Immaculate Conception, Christmas Eve, Christmas Day, Rizal Day, Last Day of the Year | None yet; Proclamation 1006[^pse-cn-2026-0008:3] |
| **16-18 Nov** | Mon-Wed | Special non-working days in NCR (Proclamation 1447) | **Unresolved** (below) |

Proclamation 1006 lists 25 Feb 2026 (EDSA anniversary) as a special **working** day, and PSE issued no non-trading memo for it (consistent with trading; inference); 4 Apr (Black Saturday) and 1 Nov (All Saints' Day) fall on weekends.[^pse-cn-2026-0008:3] Eighteen weekdays are listed closures, so 2026 has 243 weekday sessions if 16-18 Nov are regular trading days and 240 if not (derived: 261 weekdays less closures), before any weather or emergency closure.

### 16-18 November 2026

<div class="callout warn">
<span class="label">Status open as of 6 October 2026</span>

Proclamation 1447 (17 Sep 2026) declares Monday to Wednesday 16-18 Nov 2026 special non-working days in NCR for the ASEAN Summit (secondary transcription via LawPhil; verify against the Official Gazette); a DOLE advisory confirms the pay rules.[^lawphil-proc-1447-2026][^bworld-2026-09-30-dole-2027-holidays] On 25 Sep 2026 PSE issued CN-2026-0043: "November 16 - 18, 2026 shall be regular trading days".[^pse-cn-2026-0043:1] Later that day CN-2026-0044 said PSE "will be releasing an updated and final advisory ... with regard to the Exchange operations on November 16-18, 2026" and that it "supersedes the aforementioned PSE circular".[^pse-trading-day-advisory-2026-11-16-18:1] The first reading is therefore withdrawn, not reversed, and PSE's announcements archive through 6 Oct 2026 shows no final advisory.[^pse-web-announcements-archive][^pse-web-circulars-index]

Precedent points both ways (inference). For the ASEAN Summit of 13-15 Nov 2017, PSE's October circular listed only 1 and 30 Nov as non-trading days, no later closure circular was found, and PSE sent road-closure notices to trading-floor staff for 13-15 Nov, which suggests it stayed open.[^pse-cn-2017-0062-non-trading-days-nov-2017:1][^pse-tpa-2017-0146-asean-road-closures:1] Against that, PSE closed on every nationwide Presidential holiday and special non-working day in the 2025-26 circulars reviewed. The three days fall between the last Saturday rehearsal (14 Nov) and go-live (23 Nov).
</div>

### Weather and emergency closures

The Guidelines on Natural Disasters or Extraordinary Circumstances (Annex B of CN-2025-0037; SEC-approved; effective 20 Aug 2025) let the Exchange halt, suspend or cancel a scheduled Trading Day when it cannot implement its Business Continuity Plan and an emergency forces evacuation of (or prevents staff re-entering) the premises, may disrupt participants accounting for more than 50% of average daily trading value (ex-block sales, six calendar months), or otherwise threatens staff; the SEC is notified immediately.[^pse-cn-2025-0037:1][^pse-cn-2025-0037:4] For tropical cyclones the rule is keyed to the PAGASA tropical cyclone wind signal (TCWS) in the National Capital Region: **Signal 1 or 2 means regular trading; Signal 3, 4 or 5 means no trading.** If PAGASA downgrades NCR to Signal 1 or 2 by 06:00 on the trading day the day is not cancelled; if NCR is still at Signal 3 or higher at 06:00 the day is cancelled.[^pse-cn-2025-0037:4-5] (The text says "6:00 A.M. of the following Trading Day": the status is evaluated at 06:00 on the day in question.) The 2023 draft used older "Public Storm Warning Signal" wording.[^pse-cn-2023-0055:6-7] The rule rests on RTR Article VIII Section 4 (above) and does not say what happens if a signal is raised after the open.

Closures found: 7 Aug 2012 (weather; BSP/PCHC clearing suspended);[^pse-memo-trading-suspension-2012-08-07:1] 12 Sep 2017 (banking-system clearing suspended);[^pse-cn-2017-0050-trading-suspension-2017-09-12:1] 16 Oct 2017 (PhilPaSS suspended);[^pse-cn-2017-0059-trading-suspension-2017-10-16:1] 26 Dec 2017 and 2 Jan 2018 (government work suspension, Malacanang MC 37);[^pse-cn-2017-0078-non-trading-days-dec-2017:1] 13 Jan 2020 (Taal ash);[^pse-cn-2020-0002-trading-suspension-2020-01-13:1] 17-18 Mar 2020 (Luzon ECQ);[^pse-cn-2020-0021:1] 26 Sep 2022 (announced the evening before; the circular gives no reason);[^pse-cn-2022-0035-trading-suspension-2022-09-26:1] 24 Jul 2024 (weather and floods, announced the same day).[^pse-cn-2024-0038-trading-suspension-2024-07-24:1] Every circular except the December 2017 and July 2024 ones also announces no clearing or settlement at SCCP.

### Trading versus settlement holidays

SCCP's "Business Day" excludes holidays and days on which PSE trading, or BSP/PCHC clearing, is cancelled; equity settlement is T+2 clearing days with a 12 noon payment and delivery deadline ([Chapter 10](#/ch/clearing-settlement)).[^sccp-clearing-house-rules-2018:4][^pse-web-investing-at-pse] In October 2017 PSE consulted on a rule that "the policy of the Exchange is to continue to operate ... even on days when the clearing activities of the BSP or PCHC are suspended" and held a forum on a "trading day without clearing and settlement"; no adoption was found.[^pse-cn-2017-0060-proposed-amendments-trading-rules:1-2][^pse-memo-trading-day-without-clearing-settlement-forum-2017:1] Settlement-day arithmetic therefore follows the BSP calendar, not PSE's trading calendar (inference); whether BSP and PCHC operate on 16-18 Nov 2026 is not in the public record.

### 2027 holidays (government list, not yet PSE closures)

Proclamation 1427 (8 Sep 2026) sets the 2027 holidays; the transcription is secondary, cross-checked against a DOLE advisory report.[^lawphil-proc-1427-2026][^bworld-2026-09-30-dole-2027-holidays] Weekday dates: 1 Jan, 25 and 26 Mar, 9 Apr, 30 Aug, 1 and 2 Nov, 30 Nov, 8, 24, 30 and 31 Dec; 25 Feb is a special working day, and the two Eid dates will be proclaimed later. PSE will close on these only by circular (inference), so expect two unknown weekdays a year.

### Execution implications

- **Calendar service.** Feed it from Presidential proclamations and PSE's circular index; model 16-18 Nov 2026 as "status unknown" and let the router flip either way on the final advisory.
- **Typhoon days.** Check the PAGASA NCR signal at 18:00 the evening before and at 06:00 on the day. A cancelled day purges posted orders, so implement a "market not open" override and re-arm resting interest the next day.
- **Settlement dates.** Use the BSP/SCCP calendar; if PSE opens while BSP or PhilPaSS is closed, expect no settlement that day and shift T+2 arithmetic (inference).
- **Half-days.** None is scheduled for 2026; keep the 09:00-12:25 timetable parameterised.

## The 23 November 2026 engine cut-over

<div class="callout warn">
<span class="label">Scheduled change: 23 Nov 2026, subject to SEC approval</span>

PSEtrade XTS (live since 22 Jun 2015) is to be replaced by Nasdaq Eqlipse Trading ("NTE") in a **big-bang** go-live on Monday 23 Nov 2026, with no parallel run. Saturday market rehearsals are on 31 Oct, 7 Nov and 14 Nov in pre-production; FEOMS certification ran 10-23 Sep but stays open, and in July 18 of the 40 participants with their own front end were still developing to the FIX specification, 9 had not started, 2 had no analysis and 11 had not responded.[^pse-nte-broker-forum-2026-07-09:5][^pse-nte-broker-forum-2026-07-09:9][^pse-nte-faq-2026-08:1] Everything below is planned or draft, not in force; treat 23 Nov as a target with execution risk ([Chapter 17](#/ch/reform-timeline)).

- **Session times: no change announced.** The only schedule change in the pipeline renames the 15:00-15:15 slot the "Closing VWAP Negotiated Trades Session" (half-day 12:10-12:25), with the close still 15:15 (CN-2026-0031, 1 Jul 2026; status on 17 Aug: "Revising per Public Comments").[^pse-cn-2026-0031-negotiated-trades:6][^pse-cn-2026-0031-negotiated-trades:8-10][^pse-analyst-briefing-1h-2026:9]
- **Negotiated Trades** (proposed): one-firm pre-arranged trades between different clients, no volume or value limit, price within +/-5% of the full-day VWAP (or of the previous or last adjusted close if there was no trade), at most four decimals, in the 15 minutes after run-off on a web-based platform; a variant of, not a replacement for, block sales.[^pse-cn-2026-0031-negotiated-trades:3][^pse-cn-2026-0031-negotiated-trades:11][^pse-nte-faq-2026-08:1]
- **Run-off:** orders "can be entered, modified, and executed only at the Closing Price", and an incoming order at the Closing Price is accepted and matched against a better-priced passive order (XTS rejects it today); the draft text still carries the legacy sentence "no Orders will be accepted", contradicting PSE's own examples.[^pse-cn-2025-0046-board-lot-trading-at-last:5][^pse-cn-2025-0046-board-lot-trading-at-last:8][^pse-nte-broker-forum-2026-07-09:7]
- **Day 1 supports limit orders only**; the odd-lot market is abolished and the lot becomes one share if the board-lot amendments are approved ([Chapter 4](#/ch/order-types)).[^pse-nte-faq-2026-08:1]
- **No SEC approval or effectivity circular** for the run-off, board-lot or negotiated-trade changes appears in PSE's archive through 6 Oct 2026.[^pse-web-announcements-archive][^pse-web-circulars-index]
- **Draft GPDR rules** (not approved) would let PSE "adjust the trading hours of GPDRs" to the underlying's overseas hours.[^pse-cn-2024-0047:23]
</div>

### Execution implications

- Run two rule sets behind a date switch (XTS until the last session before 23 Nov; NTE after) and keep a third "NTE as approved" configuration to flip when PSE publishes the SEC-approved text. Freeze router changes before 14 Nov, test on the three Saturdays, and expect no fall-back engine.
- Under XTS a run-off order at the Closing Price is rejected if a better-priced passive order exists; under the NTE it will be accepted and matched. Code both.
- Assume resting multi-day orders do not survive the cut-over unless the broker confirms otherwise (the PSETradeX terminal is also dropping GTC and next-day validity).[^pse-nte-user-group-2026-01-15:17]

## What is not in the public record

- A consolidated, current RTR or IG; IG Part II exists only through CN-2024-0010 and earlier memos.
- The NTE FIX order-entry and market-data specifications (FIX v1.1 of 8 Jun 2026; ITCH and MDF v1.2 of 17 Jul 2026) are released to participants only, so NTE phase behaviour (freeze length, auction order types) is unverifiable.[^pse-web-nte]
- The duration of the 09:30 freeze; the closing price when the pre-close does not cross ([Chapter 6](#/ch/auctions)).
- Whether Phase 1 of the 2011 extension ran; memo TPA 2011-0052 (26 Sep 2011) and the February 2022 extension memo are not archived.
- Halt-resumption clock times for the 15:00/15:15 schedules and circuit-breaker cut-offs for the 14:45 pre-close.
- PSE's final advisory for 16-18 Nov 2026, the 2027 Eid dates, and PSE circulars for Nov-Dec 2026; PSE's "Market Calendar" page and holiday table were not retrievable.
- What a typhoon signal raised after the open does to the day.
- How the VWAP facility is accessed (web or FIX), and whether an approved block sale can execute inside the VWAP window.
