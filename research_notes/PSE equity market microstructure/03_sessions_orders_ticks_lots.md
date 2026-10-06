# PSE equity market microstructure: sessions, calendar, order types, tick sizes and board lots (research notes 03, Chapters 3-4)

**As-of date: 6 October 2026 (Asia/Manila, PHT = UTC+8, no DST).** Venue: The Philippine Stock Exchange, Inc. (PSE), equities only.
Evidence labels used on every bullet: **(P)** primary-sourced (PSE / SEC / SCCP / government text); **(S)** secondary-only (news, broker pages, aggregators); **(I)** my inference from cited facts; **(G)** gap. Citation tags (caret + slug + colon + page) point to archived PDFs, where the number is the PHYSICAL 1-based page; tags with a slug only point to web pages; all slugs are defined in the Source catalog. OCR'd scans are cited by physical page too.

**Reading guide and the ten facts that matter most (preface, not a research section)**

**Evidence-base caveat (P/I).** PSE does not publish a consolidated, current Revised Trading Rules (RTR) or Implementing Guidelines (IG). The posted RTR is the SEC-approved June 2010 text that took effect at the launch of the New Trading System (NTS) on 26 Jul 2010 [^pse-revised-trading-rules:1]; the posted IG is the 22 Jul 2010 issuance [^pse-implementing-guidelines-trading-rules:1]. Later changes live in separate memoranda listed on PSE's "Regulatory Framework" page [^pse-web-regulatory-framework]. Everything labelled "in force" below is therefore a layered reconstruction (2010 base + amendment memos), and rule/part numbers drift (see 1.7). Treat the memo dates and numbers as the stable keys.

1. **Engine:** production is PSEtrade XTS (Nasdaq X-stream), live since 22 Jun 2015 [^pse-web-xts]. Replacement "New Trading Engine" (NTE, Nasdaq Eqlipse Trading) go-live is **Monday 23 Nov 2026**, big-bang, no parallel run; market rehearsals are Saturdays 31 Oct, 7 Nov and 14 Nov 2026 [^pse-nte-broker-forum-2026-07-09:9][^pse-nte-faq-2026-08:1] (P).
2. **Whole-day schedule in force (PHT):** 09:00 Pre-Open, 09:15 Pre-Open No-Cancel, 09:30 Market Open (opening uncross then continuous), 12:00 Market Recess, 13:00 Market Resume, 14:45 Pre-Close, 14:48 Pre-Close No-Cancel, 14:50 Run-off/Trading-at-Last, 15:00 Closing VWAP Session, 15:15 Market Close [^pse-approved-rules-vwap-trading-2024:3][^pse-web-investing-at-pse] (P). Core (to 15:00) since 1 Mar 2022; VWAP session and 15:15 close since 1 Mar 2024.
3. **No extended or after-hours session for ordinary orders.** The only post-run-off segment is the Closing VWAP Session (VWAP-priced, min PHP 500,000, one-firm) [^pse-approved-rules-vwap-trading-2024:7] (P).
4. **Board-lot / tick table (15 bands) is unchanged since 26 Jul 2010** [^pse-revised-trading-rules:21][^pse-cn-2025-0046-board-lot-trading-at-last:4]. "One Lot One Share" (lot = 1 for every security), a 10-band tick table, removal of the Odd Lot Market and a run-off rule change are slated for the NTE; PSE itself said on 4 Jul 2026 and 17 Aug 2026 that the board-lot amendments were "awaiting SEC approval / for SEC approval" [^pse-asm-2026-president-report:22][^pse-analyst-briefing-1h-2026:9]. I found no approval or effectivity circular as of 6 Oct 2026 (G).
5. **NTE Day 1: limit orders only** [^pse-nte-faq-2026-08:1] (P). Market, stop, iceberg, min-qty, MOO/MOC support on the NTE is not stated anywhere public (G).
6. **Order amendments that lose queue priority:** volume increase, limit-price change, trigger-price change; decrease in volume, validity change and account-code change keep priority [^pse-revised-trading-rules:24-25][^pse-implementing-guidelines-trading-rules:18] (P).
7. **No modify/cancel windows:** 09:15-09:30, 14:48-14:50 (no cancel/modify), the 09:30 opening freeze, and the 12:00-13:00 recess (no entry/modify/cancel) [^pse-approved-rules-vwap-trading-2024:5-6][^pse-tpa-2011-0124-amended-implementing-guidelines:3] (P).
8. **Weather rule:** if PAGASA's tropical-cyclone wind signal for NCR is No. 3 or higher at 06:00 of the trading day, the day is cancelled; signals 1-2 mean regular trading [^pse-cn-2025-0037:4-5] (P; SEC-approved, announced and effective immediately by the PSE circular of 20 Aug 2025).
9. **Calendar watch-points:** every weekday holiday or special non-working day in Proclamation 1006 through August 2026 has a PSE "no trading" circular (the EDSA anniversary, 25 Feb, was a special working day); Mon-Wed 16-18 Nov 2026 were declared special non-working days in NCR (Proclamation 1447); on 25 Sep 2026 PSE first announced "regular trading days" for those dates (CN-2026-0043) and then, later the same day, withdrew that and promised a "final advisory" (CN-2026-0044), so the status is open [^pse-cn-2026-0043:1][^pse-trading-day-advisory-2026-11-16-18:1][^lawphil-proc-1447-2026] (P); 24 and 31 Dec 2026 are special non-working days, so no half-day sessions are scheduled.
10. **Price collars define order validity:** an order outside the day's static band (+50%/-30% of reference price since 24 Mar 2020) is invalid, and an order breaching the dynamic threshold (10/15/20% by liquidity cluster) freezes the security pending Market Control action [^pse-cn-2020-0028:1-2][^pse-implementing-guidelines-trading-rules:10-11,25-26][^pse-tpa-2026-0036-dynamic-threshold-review:1] (P; detail covered by another researcher).

**Engine delta table: what a router must switch at the 23 Nov 2026 cut-over (all NTE items are planned or draft, not confirmed in force):**

| Parameter | PSEtrade XTS (until the last session before cut-over) | Nasdaq Eqlipse NTE (planned from 23 Nov 2026) |
|---|---|---|
| Session timetable | 09:00 / 09:15 / 09:30 / 12:00-13:00 / 14:45 / 14:48 / 14:50 / 15:00 / 15:15 (Q1) | no change announced; a negotiated-trades session at 15:00 is proposed |
| Order types | Rule-level: Limit, Market, Market-to-Limit, Stop, Stop-Limit, MOO/MOC; FIX: Market, Limit, Stop, Stop Limit (Q4) | limit orders only on Day 1 |
| Validity / qualifiers | Day, GTC, GTD, GTW, Sliding, FAK (FIX also FOK, Session); min-qty; iceberg | not published; PSETradeX terminal drops GTC and next-day validity |
| Board lot | 15-band table, 5 to 1,000,000 shares | 1 share for PHP and USD securities (awaiting SEC approval) |
| Odd-lot market | separate "O" book, continuous only | abolished |
| Tick table (PHP) | 15 bands, 0.0001 to 5.00 | 10 bands, 0.001 to 5 (draft) |
| Run-off at Closing Price | order rejected if a better-priced passive order exists | accepted and matched at the Closing Price; entry, modification and execution only at the Closing Price |
| Closing VWAP session | 15:00-15:15, VWAP trades >= PHP 500,000, one-firm | same, plus proposed Negotiated Trades (+/-5% of VWAP, no size limit) |
| Cut-over mode | n/a | big bang, no parallel run; rehearsals Sat 31 Oct, 7 Nov, 14 Nov |

**Main open gaps (detail in each section's Gaps list):** (1) no consolidated current RTR/IG and drifting article/part numbers; (2) SEC approval/effectivity of One Lot One Share, the new tick table, odd-lot removal and the run-off change is unpublished as of 6 Oct 2026; (3) the NTE order-entry spec (order types, time-in-force, qualifiers, auction handling) is not public beyond "limit orders only on Day 1"; (4) PSE's final advisory for 16-18 Nov 2026 and the 2027 Eid dates; (5) the Exchange-required per-order value limit, message-rate limits and any cancel-on-disconnect behaviour are undocumented; (6) pre-2010 board-lot/tick tables, whether the Oct 2011 "Phase 1" hours ever ran, and the Feb 2022 extension memo; (7) which of Market-to-Limit, GTW, Sliding Validity, FOK and stop orders XTS actually exposes to external FEOMS clients; (8) odd-lot settlement/price-linkage to the board-lot market is not stated.

---

## 1. What is the PSE session schedule today to the minute, how did it get here, and what is changing?

### Takeaway
The PSE runs a single whole-day session with a 60-minute recess, 30-minute pre-open (15 + 15 no-cancel), a 5-minute closing auction call (3 + 2 no-cancel), a 10-minute run-off at the closing price, and (since 1 Mar 2024) a 15-minute Closing VWAP Session ending at 15:15. The lunch recess only exists in the whole-day schedule (from 2 Jan 2012; before that PSE traded a morning-only 09:30-12:10 session). It was effectively removed under the COVID-era shortened-hours regime (continuous 09:30 to a 12:45 pre-close and 13:00 close, no recess) from 16 Mar 2020 until 3 Dec 2021, restored on 6 Dec 2021, removed again for the Omicron shortened hours 14 Jan-28 Feb 2022 and restored for good on 1 Mar 2022. The close has moved 12:10 (2010-11) to 15:30 (2012-Mar 2020) to 13:00 (shortened hours) to 15:00 (6 Dec 2021) to 15:15 (1 Mar 2024). No hours change is announced for the NTE cut-over, but a "Negotiated Trades" session is proposed at 15:00.

### Cited Findings

#### 1.1 Schedule in force on 6 Oct 2026 (whole-day trading)
| PHT | Phase (PSE name) | What TPs may do | Source |
|---|---|---|---|
| 09:00:00 | Pre-Open | no matching; enter, modify, cancel orders (processed by the pre-opening algorithm) | [^pse-approved-rules-vwap-trading-2024:6] (P) |
| 09:15:00 | Pre-Open No-Cancel | enter only; no cancel/modify | same |
| 09:30:00 | Market Open: Opening, then Continuous | opening price computed and orders matched at it; order book frozen, no entry/modify/cancel; then continuous matching at best price | same |
| 12:00:00 | Market Recess | trading halted; no entry, modify or cancel | same |
| 13:00:00 | Market Resume (continuous) | continuous matching | same |
| 14:45:00 | Pre-Close | same as Pre-Open: enter/modify/cancel (closing-price call) | same |
| 14:48:00 | Pre-Close No-Cancel | enter only | same |
| 14:50:00 | Run-off / Trading-at-Last | orders at the Closing Price only | same |
| 15:00:00 | Closing VWAP Session | only VWAP transactions (see Q2) | [^pse-approved-rules-vwap-trading-2024:7] |
| 15:15:00 | Market Close | no entry/modify/cancel | same |

- The same table is on PSE's own site: "Trading days are from Monday to Friday, 9:00 a.m. to 3:15 p.m." with exactly these phase times (page retrieved 6 Oct 2026) [^pse-web-investing-at-pse] (P). The rule text (RTR Art. II Sec. 2 and IG Part II) restated by SEC-approved CN-2024-0010 dated 1 Feb 2024 [^pse-approved-rules-vwap-trading-2024:1,3,5-6] (P).
- Durations (derived): pre-open 15 + 15 min; continuous AM 150 min (09:30-12:00); recess 60 min; continuous PM 105 min (13:00-14:45); closing call 3 + 2 min; run-off 10 min; Closing VWAP 15 min (I).
- The IG historically listed an 08:45 national-anthem item and Market Control "BOD/EOD actions" around the session [^pse-implementing-guidelines-trading-rules:4-6]; neither appears in the 2024 restatement [^pse-approved-rules-vwap-trading-2024:5-6] (P).
- Rule text says "Unless the Exchange decides otherwise" and "The Exchange may effect changes to the hours and schedule of a Trading Day, as the circumstance warrants" [^pse-approved-rules-vwap-trading-2024:3][^pse-revised-trading-rules:13] (P); this is how the COVID-era and half-day schedules were imposed by memo.

#### 1.2 Phase mechanics
- Pre-Open Period = period when orders are accepted and queued for the opening-price calculation; they do not trade until the market opens. Pre-Close Period is the mirror image for the Closing Price; Run-off/Trading-at-Last = period after Pre-Close when orders are accepted and executed only at the Closing Price [^pse-revised-trading-rules:10-11] (P).
- Auction price algorithm (same for opening and closing): (1) price that maximises matched volume; (2) least unmatched volume; (3) market pressure (side with more volume: highest possible price if buy pressure, lowest if sell pressure); (4) closest to the Reference Price; (5) Reference Price itself if it is among candidates. Reference Price is the previous close or last adjusted close (LACP) for the opening; it is the Last Traded Price for the closing [^pse-implementing-guidelines-trading-rules:12-16][^pse-revised-trading-rules:23-24] (P).
- Cancellation/modification rules by phase: IG XI and XII (2010) say orders may be modified/cancelled from Pre-Open to Trading-at-Last except in the No-Cancel periods; TPA 2011-0124 added Market Recess to the prohibited windows for whole-day trading [^pse-implementing-guidelines-trading-rules:17-18][^pse-tpa-2011-0124-amended-implementing-guidelines:3] (P). Cancelling in Run-off is permitted (IG XII.3, 2010) [^pse-implementing-guidelines-trading-rules:18] (P).
- Run-off content has been restated three times: 2010/2013 text "Limit Orders at the Closing Price only or Market Orders but matching is executed only at the Closing Price" [^pse-implementing-guidelines-trading-rules:4][^pse-tpa-2013-0185-extended-pre-close:5,7]; Dec 2011 text "Limit Orders at the Closing Price only" [^pse-tpa-2011-0124-amended-implementing-guidelines:3]; 2024 text "TPs can enter Orders at the Closing Price only" [^pse-approved-rules-vwap-trading-2024:5-6] (P). RTR Art. IV Sec. 18: all orders in run-off execute only at the Closing Price and "in cases where prices of posted Orders in the Order book are better than the Closing Price, no Orders will be accepted by the Trading System" [^pse-revised-trading-rules:27][^pse-cn-2025-0046-board-lot-trading-at-last:8] (P).

#### 1.3 Half-day trading (rule text vs practice)
- Rule text restated 1 Feb 2024: half-day = 09:00 pre-open, 09:15 no-cancel, 09:30 open, 11:57 pre-close, 11:59 pre-close no-cancel, 12:00 run-off, 12:10 Closing VWAP, 12:25 close [^pse-approved-rules-vwap-trading-2024:3,5] (P).
- Last documented use: 24 and 31 Dec 2021, with a different pre-close timing (11:55 pre-close, 11:58 no-cancel, 12:00 run-off, 12:10 close) [^pse-cn-2021-0063-half-day-trading-2021-12:1] (P). For 2025 and 2026, 24 and 31 Dec are non-trading days (special non-working days) [^pse-cn-2025-0043-non-trading-days:1][^pse-cn-2026-0008:3] (P), so no half-day sessions are scheduled; the half-day table is dormant (I).

#### 1.4 History of schedule changes (effective date, memo, resulting schedule)
| Effective | Change | Resulting PHT schedule | Memo / approval | Source |
|---|---|---|---|---|
| pre-26 Jul 2010 | Maktrade era: morning session only | 09:30-12:00 | n/a (news) | [^philstar-2008-12-04-extended-hours] (S) |
| 26 Jul 2010 | NTS ("PSEtrade", NYSE Euronext NSC) launches; RTR/IG take effect; PSE trades **half-day only** | 08:45 anthem; 09:00 pre-open; 09:15-09:30 no-cancel; 09:30 open; 11:57-11:59 pre-close auction; 11:59-12:00 no-cancel; 12:00 run-off; 12:10 close. Whole-day schedule defined but never used: 09:30-12:00, 14:00-15:45, pre-close 15:45, run-off 15:50, close 16:00 | RTR approved by SEC 1 Jun 2010 (memo 2010-0275, 8 Jun 2010); IG memo 2010-0340 (22 Jul 2010) | [^pse-revised-trading-rules:1-2,13][^pse-implementing-guidelines-trading-rules:1,4-6][^pse-memo-extended-trading-proposal-2011:2] (P) |
| 2008 plan (not implemented) | Board had approved 09:00-12:00 / recess to 14:00 / 14:00-16:00; postponed during the Maktrade-to-PSEtrade transition | n/a | CN-2011-0002 survey memo (28 Jun 2011) | [^pse-cn-2011-0002:1] (P) |
| 28 Jul 2011 (proposal) | Board (13 Jul 2011) approved extension from 09:00-12:10 to 09:00-15:30 in two phases: Phase 1 (1 Oct 2011) 09:00-13:00; Phase 2 (1 Jan 2012) 09:00-12:00 and 13:30-15:30 | proposal only | TPA 2011-0030 | [^pse-memo-extended-trading-proposal-2011:1-2] (P). Whether Phase 1 ever ran is unconfirmed (G); a 2013 PSE memo says pre-2012 trading time was "two hours and forty minutes", i.e. 09:30-12:10, which suggests it did not (I) [^pse-memo-extended-pre-close-consultation-2013:1] |
| **2 Jan 2012** | Whole-day trading begins | 08:45 anthem; 09:00 pre-open (09:15 no-cancel); 09:30 open; 12:00 recess; **13:30** resume; **15:17** pre-close auction (15:17-15:19), no-cancel 15:19-15:20; 15:20 run-off; 15:30 close | TPA 2011-0108 (6 Dec 2011); CN-2011-0025 (26 Dec 2011); SEC approval letter 25 Oct 2011 (TPA 2011-0110, 7 Dec 2011); IG amendments TPA 2011-0124 (28 Dec 2011); SCCP memo 03-1211 (settlement deadline unchanged, CCCS open to 19:00) | [^pse-memo-new-trading-hours-2011:1][^pse-cn-2011-0025:1][^pse-tpa-2011-0110-amended-revised-trading-rules:1-3][^pse-tpa-2011-0124-amended-implementing-guidelines:1-3][^sccp-memo-03-1211-settlement-unchanged-extended-hours:1] (P) |
| **4 Nov 2013** | Extended pre-close: 3 to 5 minutes (Board 10 Jul 2013; peer pre-close lengths cited: Bursa 5, SGX 6, SET 10, IDX 10, HoSE 15 min) | pre-close auction 15:15-15:18; no-cancel 15:18-15:20; run-off 15:20-15:30; close 15:30 | TPA 2013-0107 (consultation 17 Jul 2013), SEC letter 26 Sep 2013, TPA 2013-0165 (14 Oct), TPA 2013-0167 (16 Oct), TPA 2013-0185 (14 Nov; SEC-signed texts 29 Oct 2013) | [^pse-memo-extended-pre-close-consultation-2013:1-5][^pse-memo-extended-pre-close-implementation-2013:1][^pse-memo-pre-close-schedule-2013:1][^pse-tpa-2013-0185-extended-pre-close:2,4-7] (P) |
| 22 Jun 2015 | Migration to PSEtrade XTS (Nasdaq X-stream) | no hours change | n/a | [^pse-web-xts] (P) |
| **16 Mar 2020** | COVID shortened hours (first day only 16 Mar; a 08:30/09:00 variant announced for 17 Mar-14 Apr was never used) | 09:00 pre-open; 09:30 open; 12:45 pre-close; 12:50 run-off; 13:00 close | CN-2020-0017 (15 Mar 2020) | [^pse-cn-2020-0017:1] (P) |
| 17-18 Mar 2020 | Trading suspended (Luzon ECQ) | none | CN-2020-0021 (16 Mar 2020) | [^pse-cn-2020-0021:1] (P) |
| 19 Mar 2020 | Trading resumes; shortened hours; trading floor closed, trading remote | as 16 Mar 2020 | CN-2020-0025 (17 Mar 2020) | [^pse-cn-2020-0025-resumption-of-trading:1] (P) |
| 2020-2021 | Shortened hours extended: to 30 Apr 2020 (CN-2020-0035), to 15 May 2020 (CN-2020-0042), then "until further notice" under MECQ (CN-2020-0046, 14 May 2020) | 09:00 / 09:30 / 12:45 / 12:50 / 13:00 | as listed | [^pse-cn-2020-0035:1][^pse-cn-2020-0042:1][^pse-cn-2020-0046:1] (P) |
| **6 Dec 2021** | "Back to pre-pandemic full day 5-hour schedule" (note: not the 2012-2020 times; afternoon moved 30 min earlier) | 09:00 pre-open; 09:30 open; 12:00 recess; **13:00** resume; **14:45** pre-close; **14:50** run-off; **15:00** close | CN-2021-0059 (22 Nov 2021) | [^pse-cn-2021-0059:1] (P) |
| 24 and 31 Dec 2021 | Half-day trading | 09:00 / 09:15 / 09:30 / 11:55 / 11:58 / 12:00 / 12:10 | CN-2021-0063 (15 Dec 2021) | [^pse-cn-2021-0063-half-day-trading-2021-12:1] (P) |
| 14-31 Jan 2022 | Omicron shortened hours | 09:00 / 09:15 / 09:30 / 12:45 pre-close / 12:48 no-cancel / 12:50 run-off / 13:00 close | CN-2022-0004 (11 Jan 2022) | [^pse-cn-2022-0004:1] (P) |
| Feb 2022 | Shortened hours evidently continued to 28 Feb (no separate extension memo found) | as above | implied by CN-2022-0009 "Further to CN-2022-0004" | (I) |
| **1 Mar 2022** | Full-day schedule restored, no-cancel phases listed | 09:00 / 09:15 / 09:30 / 12:00 / 13:00 / 14:45 / 14:48 / 14:50 / 15:00 | CN-2022-0009 (17 Feb 2022) | [^pse-cn-2022-0009-trading-schedule-mar-2022:1] (P) |
| 3 Jan 2024 (evidence of pre-VWAP close) | Afternoon "from 1:00 to 3:00 p.m." | close 15:00 | CN-2024-0003 | [^pse-cn-2024-0003-update-market-halt:1] (P) |
| **1 Mar 2024** | Closing VWAP Session introduced; market close moves 15:00 to 15:15 (half-day: 12:10 VWAP, 12:25 close) | ... 14:50 run-off; 15:00 Closing VWAP; 15:15 close | SEC-approved Rules on VWAP Trading, CN-2024-0010 (1 Feb 2024, effective immediately, launch to be advised); CN-2024-0012 (15 Feb 2024: launch 1 Mar 2024); ASM 2024 report confirms go-live date | [^pse-approved-rules-vwap-trading-2024:1,3,5-7][^pse-cn-2024-0012-vwap-go-live:1][^pse-asm-2024-presidents-report:24] (P) |

(I) The 2013 RTR text still read "1:30 p.m. resume / 3:15 pre-close / 3:30 close" when CN-2023-0043 was drafted in Sep 2023, i.e. the 2021-22 schedule was run under the "unless the Exchange decides otherwise" clause and the RTR Art. II text was only restated in Feb 2024 [^pse-cn-2023-0043:11].

#### 1.5 Announced / planned changes as of 6 Oct 2026
- **NTE go-live Mon 23 Nov 2026.** Project plan: FEOMS certification 10-23 Sep 2026; pre-production connectivity tests 29 Sep-9 Oct; pre-production testing 12-22 Oct; Saturday market rehearsals 31 Oct, 7 Nov, 14 Nov; go-live 23 Nov [^pse-nte-broker-forum-2026-07-09:9] (P). PSE: "There will be no parallel runs ... big bang approach"; MRs are in the pre-production environment; TPs must use new production links [^pse-nte-faq-2026-08:1] (P). Readiness (9 Jul 2026): of 40 TPs with their own FEOMS, 18 were still analysing/developing FIX, 9 had not started development, 2 had no analysis, 11 had not responded [^pse-nte-broker-forum-2026-07-09:5] (P). Secondary: go-live "by November", 11-hour session capacity, 5 million orders / 450,000 trades capacity [^philstar-2026-07-23-nte-go-live] (S).
- **No change to session times is announced for the NTE.** The only schedule change in the pipeline is a new "Closing VWAP Negotiated Trades Session" at 15:00 (half-day 12:10) with close still 15:15 (half-day 12:25), proposed in CN-2026-0031 (1 Jul 2026; comments to 7 Jul 2026) [^pse-cn-2026-0031-negotiated-trades:1,6,8-10] (P). Status 17 Aug 2026: "Negotiated Trades: Revising per Public Comments" [^pse-analyst-briefing-1h-2026:9] (P).
- **Run-off rule change with NTE:** orders in Run-off "can be entered, modified, and executed only at the Closing Price"; an incoming order at the Closing Price is accepted and matched with a better-priced passive order at the Closing Price (today XTS rejects it) [^pse-cn-2025-0046-board-lot-trading-at-last:5-8][^pse-nte-user-group-2026-01-15:11-15][^pse-nte-broker-forum-2026-07-09:7] (P). The draft section text still carries the legacy sentence "no Orders will be accepted" although the worked examples show acceptance (internal inconsistency in the draft) [^pse-cn-2025-0046-board-lot-trading-at-last:8] (P/I).
- **Nov 16-18, 2026:** see Q3. **GPDR** draft rules allow PSE to "adjust the trading hours of GPDRs" to the underlying's overseas hours (not yet approved) [^pse-cn-2024-0047:23] (P).

#### 1.6 Intraday disruptions to the schedule (rule + practice)
- RTR Art. VIII (2010): Sec. 2 Market Halt; Sec. 3 Suspension of trading in the market (all trades and posted orders for the day remain valid); Sec. 4 Cancellation of trading in the market (President may cancel a scheduled day if announced within one hour after Pre-Open; all trades and posted orders for the day are purged) [^pse-revised-trading-rules:35-36] (P).
- Market-halt trigger changed by the 20 Aug 2025 circular (SEC-approved, effective immediately): from "1/3 of TP users cannot access" to TPs representing more than 50% of average daily trading value (ex block sales, six calendar months) unable to trade directly or via their mandatory Correspondent TP, due solely to Exchange system problems, natural disasters or extraordinary circumstances [^pse-cn-2025-0037:1-3] (P); consultation context [^pse-cn-2022-0020-market-halt-consultation:4-6][^pse-cn-2023-0055:3-4] (P).
- Resumption rules after a halt (amended Dec 2011): for whole-day trading no extension of hours except to complete the remaining phases; if a halt lasts more than two hours or beyond 15:45 (then 15 min after the 15:30 close) the Exchange decides whether to suspend or cancel the day [^pse-tpa-2011-0124-amended-implementing-guidelines:4-6][^pse-tpa-2011-0110-amended-revised-trading-rules:6] (P). Those clock times were never restated for the 15:00/15:15 schedules (G).
- Practice (all P): 3 Jan 2024 technical halt 09:32 to 11:56, afternoon "as scheduled" 13:00-15:00 [^pse-cn-2024-0001-market-halt:1][^pse-cn-2024-0003-update-market-halt:1]; 4 Jan 2022 opening delayed (43 of 125 TPs unable to connect) then trading cancelled for the day (Nasdaq engine / Flextrade front-end connectivity) [^pse-cn-2022-0001-delay-market-opening:1][^pse-cn-2022-0002-cancellation-of-trading-2022-01-04:1]; 4 Jun 2019 halt from 11:45 for a fire drill, resumption 13:30, close 15:30 [^pse-cn-2019-0031-trading-halt-fire-drill:1]; earlier "technical issues" halts at 13:46 on 20 Nov 2014 (resumed 14:30, close still 15:30), 14:05:26 on 24 Aug 2015, 10:02:22 on 25 Aug 2015 and 10:29:18 on 8 Apr 2016 [^pse-cn-2014-0057-trading-halt-2014-11-20:1][^pse-cn-2015-0110-trading-halt-2015-08-24:1][^pse-cn-2015-0112-trading-halt-2015-08-25:1][^pse-cn-2016-0020-trading-halt-2016-04-08:1]. Late-open handling is by same-day "adjusted schedule" circular that re-times only the affected opening phases and keeps the rest: 9 Dec 2024 Pre-Open 09:40, No-Cancel 09:50, Open 09:55 [^pse-cn-2024-0061-adjusted-schedule-2024-12-09:1]; 24 Mar 2025 open delayed for a "system connectivity issue", No-Cancel 11:05, Open 11:10, remaining phases unchanged [^pse-cn-2025-0014:1][^pse-cn-2025-0015-adjusted-schedule-2025-03-24:1]. In none of these did PSE extend the close.
- Market-wide circuit breaker (CN-2020-0044, effective 4 May 2020): PSEi -10% => 15-min halt, -15% => 30 min, -20% => 60 min vs previous close; each level once per day; a breach before the recess includes the recess in the halt; trigger cut-offs published only for the old 15:15 pre-close (L1 until 14:55, L2 14:40, L3 14:10) and the shortened schedule (12:25 / 12:10 / 11:40) [^pse-cn-2020-0044:1-4] (P). For today's 14:45 pre-close the equivalent cut-offs (pre-close minus halt minutes minus 5) would be 14:25 / 14:10 / 13:40, but PSE has not republished them (I/G).

#### 1.7 Stale or inconsistent sources to avoid (important for reconciling broker pages)
- PSE's own "Investing" page prose still says trading runs "9:30 AM to 12:00 NN and 1:30 PM to 3:30 PM" and describes a 50% static band, although the schedule table on the same page shows the current 09:00-15:15 timetable [^pse-web-investing-at-pse] (P, stale prose).
- A First Metro Securities help article (post dated 13 Feb 2015) still shows the 2020-21 shortened hours (09:30-13:00, 12:45 pre-close) [^firstmetrosec-help-34] (S, stale).
- Numbering drift: after VWAP became new RTR Art. VI (Feb 2024), later memos disagree on article numbers (CN-2025-0037 still cites Art. VIII for Market Halt; CN-2026-0031 cites Art. VII for Cross/Block/Negotiated) and on IG part numbers (CN-2020-0044 inserted a new Part XXI Circuit Breaker; CN-2025-0037 calls Technical Contingencies "Part XXI"; VWAP is IG XXV, Negotiated Trades proposed as IG XXVI) [^pse-cn-2020-0044:2][^pse-cn-2025-0037:3,6][^pse-cn-2026-0031-negotiated-trades:7,11] (P/I).

### Inferences
- (I) Total continuous-matching time is 255 minutes (150 + 105); auctions occupy 30 + 5 minutes; run-off 10 minutes.
- (I) With no cross in the closing call, the Closing Price should default to the Last Traded Price because the closing-price algorithm uses LTP as its reference (IG VIII) and the RTR defines Closing Price as "the price determined during the Pre-Close Period"; I found no explicit text for the no-cross case. PSE's end-of-day quote-file spec only says "Day Close: price of a security at market close. If there is no trade for the day, Day Close has no value" and that LTP falls back to the close price when there was no trade that day [^pse-quote-file-eod-spec-2014:1] (P, 2014).
- (I) Phase 1 (1 Oct 2011, to 13:00) was probably never implemented (see table).
- (I) No hours change should be assumed for 23 Nov 2026, but nothing public rules out one; the NTE session/phase spec is not public.

### Gaps
- (G) No consolidated IG/RTR; the IG Part II text is only available via CN-2024-0010 and earlier memos.
- (G) NTE FIX Order Entry/Session spec (v1.1, 8 Jun 2026) and ITCH/MDF specs (v1.2, 17 Jul 2026) are released to participants only ("Please contact ... for the latest version") [^pse-web-nte] so phase-by-phase NTE behaviour (opening freeze length, auction order types) is unverifiable.
- (G) Duration of the 09:30 "Opening" freeze is not stated in any rule.
- (G) Missing memo for the Feb 2022 extension of shortened hours; missing TPA 2011-0052 (26 Sep 2011) on Phase 1.

### Execution implications
- Build the exchange-state machine on the ten PHT phase timestamps above (UTC: 01:00, 01:15, 01:30, 04:00, 05:00, 06:45, 06:48, 06:50, 07:00, 07:15); schedule defensively against PSE memos because the Exchange can change it by circular on days' notice (CN-2021-0059 gave 14 days; CN-2020-0017 gave one day).
- Last cancel/modify is 09:14:59 (pre-open) and 14:47:59 (closing call). After that, auction interest is locked; after 14:50 only closing-price orders exist. Plan closing-benchmark algos to commit before 14:48.
- No normal orders may be sent 15:00-15:15; VWAP-session trades go through a separate exchange VWAP facility. PSE says the future Negotiated Trades platform will be "web-based, similar to the VWAP facility" [^pse-nte-faq-2026-08:1], which implies the VWAP facility is web-based and not reachable over FIX order entry (I).
- Under XTS, a Run-off order priced at the Closing Price is rejected if a better-priced passive order exists; under the NTE it will be accepted and matched. Code both behaviours and switch at cut-over.
- NTE cut-over: freeze router changes before 14 Nov; test on the three Saturdays; expect no fall-back engine (no parallel run); confirm each broker's FEOMS certification status given the July readiness figures; assume non-Day orders do not survive the cut-over unless the broker confirms (G).

---

## 2. When can block sales, odd lots, crosses, VWAP/negotiated trades and short sales be entered, by session?

### Takeaway
Block sales may be executed from Pre-Open to Run-off including the recess; odd lots trade only in continuous sessions in a separate "O"-prefixed book; crosses must be inside the BBO and never in the auctions; VWAP trades happen only in the Closing VWAP Session; short sales are barred in both auctions. Negotiated Trades (proposed) would share the 15:00-15:15 slot.

### Cited Findings
| Facility | 09:00-09:30 pre-open | Continuous AM/PM | Recess 12:00-13:00 | 14:45-14:50 pre-close | 14:50-15:00 run-off | 15:00-15:15 VWAP session |
|---|---|---|---|---|---|---|
| Normal-market orders | enter (modify/cancel until 09:15) | yes | no | enter (modify/cancel until 14:48) | closing-price orders only | no |
| Odd-lot board | no | yes only | no | no | no | no |
| Cross transaction | no | yes, inside BBO | no | no | yes, at Closing Price | no |
| Block sale | yes (approved block can run at pre-open) | yes | yes | yes | yes | not per rule text (I) |
| VWAP trade | no | no | no | no | no | yes |
| Short sell order | no | yes (uptick rule, Day orders) | no | no | yes: the system rejects short sells only in Pre-Open and Pre-Close (since 22 Jan 2019) | no |

Sources by row: normal orders see 1.1; odd lot [^pse-implementing-guidelines-trading-rules:19-20][^pse-revised-trading-rules:26]; cross [^pse-revised-trading-rules:31]; block sale [^pse-revised-trading-rules:32][^pse-tpa-2011-0110-amended-revised-trading-rules:5]; VWAP [^pse-approved-rules-vwap-trading-2024:4,7]; short sale [^pse-short-selling-guidelines-2023-10:2][^pse-revised-trading-rules:18-19][^pse-cn-2019-0004-short-selling-guidelines-amendment:1] (P).

- **Block sales (regular):** value at least PHP 20 million; price within 5% above/below the Last Adjusted Closing Price; price up to 4 decimals; volume may be a non-multiple of the board lot; settlement T+0 (execution date) per the 2010 text, which has not been restated since the equity settlement cycle moved to T+2 [^pse-implementing-guidelines-trading-rules:23-24] (P; current T+0 treatment unverified, G). **Special block sale:** at least PHP 50 million; underlying agreement supplied; PSE Market Control executes it; approval within 2 working days [^pse-implementing-guidelines-trading-rules:24] (P). Both thresholds were restated unchanged in the July 2026 consultation ("regular ... PhP20 million ... 5% ... Reference Price; special ... PhP50 million") [^pse-cn-2026-0031-negotiated-trades:3] (P).
- Process: application to PSE (originally by 12:00 noon; Dec 2011 changed to "before Run-Off Period"); PSE approves/disapproves within 30 minutes; execute within 5 minutes of approval via the Trading Confirmation System with side, security, quantity, price, counterparty member code, client account ID; an unconfirmed two-firm declaration is eliminated after 15 minutes; approvals after hours are executed in the next Pre-Open; pre-dated blocks are announced and run in Pre-Open [^pse-implementing-guidelines-trading-rules:24-25][^pse-tpa-2011-0124-amended-implementing-guidelines:4] (P). Block sales may run "from the Market Pre-Open to the Trading-at-Last/Run-Off period, including Market Recess" [^pse-tpa-2011-0110-amended-revised-trading-rules:5] (P). Block sales respect the trader's value limit [^pse-implementing-guidelines-trading-rules:17] and carry the Normal Market's security states except freezing/reservation [^pse-revised-trading-rules:32] (P).
- 2026 practice examples: PSE posts a trading-participant advisory the day before execution with stock, shares, price, value, e.g. DHI 191,854,123 shares at 1.7032 = PHP 326,765,942.29 on 17 Mar 2026; PAL 464,230,075 shares at 0.4305 = PHP 199,851,047.29 on 29 May 2026; ATI blocks (one the 177,612,478-share tender-offer result) at 3.60 followed by a trading suspension for minimum-public-ownership non-compliance on 13 Mar 2026 [^pse-tpa-2026-0015-block-sale-dhi:1][^pse-tpa-2026-0023-block-sale-pal:1][^pse-tpa-2026-0012-block-sale-ati-tender-offer:1] (P). Note the 4-decimal, off-tick, non-lot quantities.
- DDS block sales: USD 500,000 (regular), USD 1,000,000 (special) [^pse-dds-rules:7] (P).
- FIX (XTS) models block sales as Trade Capture Report (35=AE) with TrdType 0 = Regular Block Sale, 1 = Special Block Sale, one-party and cross workflows [^pse-fix-specification-v2-5:34-40] (P).
- **Cross transactions:** price within BBO (or per IG limits if no BBO); not in Pre-Open/Pre-Close; at the Closing Price in Run-off; pre-arranged trades that qualify as block sales must use the Block Sale Market, not a cross [^pse-revised-trading-rules:31] (P). Sub-threshold pre-arranged trades outside the BBO currently have no execution facility, which is what Negotiated Trades is meant to fix [^pse-cn-2026-0031-negotiated-trades:3] (P). Automatic cross: if a TP has a posted order and posts a counterpart order at the same or better price, the new order matches against its own earlier order regardless of queue position [^pse-revised-trading-rules:31] (P).
- **Odd lots:** orders smaller than the board lot go to a separate Odd Lot Market with an "O" prefix on the symbol (e.g. OBC); only limit and market orders; validities Day/GTW/GTD/GTC/Sliding; partial matching allowed; modification same as normal market; "no Pre-Open, Pre-Close and Run-Off Period in the Odd Lot Market"; accepted only during Continuous Trading; start-of-day reference price = LACP of the Normal Market; closing price = last odd-lot trade or LACP; no dynamic threshold; freezes/reservations do not carry across markets; using the odd-lot board to execute a normal-market transaction is a major violation [^pse-implementing-guidelines-trading-rules:19-20][^pse-revised-trading-rules:26,37] (P). Odd-lot and cross trades are excluded from the VWAP computation [^pse-approved-rules-vwap-trading-2024:7] (P). DDS can trade in the odd-lot market [^pse-dds-rules:7] (P). The Odd Lot Market will no longer exist on the NTE [^pse-nte-faq-2026-08:1][^pse-cn-2025-0046-board-lot-trading-at-last:5] (P).
- **VWAP trading (Closing VWAP Session):** executes only within 15 minutes after Run-off at the full-day VWAP computed by the Exchange (max 4 decimals); minimum value PHP 500,000 (consultation draft said PHP 1,000,000); single-firm only (two-firm option reserved, needs SEC approval); not allowed for suspended/halted securities; trader value limit applies; VWAP excludes block sales, intentional crosses and odd-lot trades; if VWAP display is delayed the session is suspended and cancelled for the day if fewer than 5 minutes remain at resolution [^pse-approved-rules-vwap-trading-2024:2,4,7][^pse-cn-2023-0043:4,17] (P). Launched 1 Mar 2024 [^pse-cn-2024-0012-vwap-go-live:1] (P).
- **Negotiated Trades (proposal, not in force):** one-firm pre-arranged trades between different clients; no volume or value restriction; execution window 15 minutes after Run-off (a "Closing VWAP Negotiated Trades Session"); price within +/-5% of the full-day VWAP (or of previous close/LACP if no trade), at most 4 decimals; suspended securities excluded; if VWAP computation is delayed the session is suspended and cancelled if under 5 minutes remain [^pse-cn-2026-0031-negotiated-trades:3-4,7,11][^pse-nte-broker-forum-2026-07-09:8] (P). PSE says it will not replace block sales, will run on a web-based platform "similar to the VWAP facility", counts toward daily value, is disseminated in the market-data feed as news, and appears in the CTF [^pse-nte-faq-2026-08:1-2] (P). Status: "Revising per Public Comments" [^pse-analyst-briefing-1h-2026:9].
- **Short selling:** program launched 6 Nov 2023 [^pse-cn-2023-0056:1]; the June 2018 guidelines had also barred Run-off, but PSE corrected this on 23 Jan 2019 because the RTR and the trading-system configuration reject short sells only in Pre-Open and Pre-Close [^pse-cn-2019-0004-short-selling-guidelines-amendment:1]; short-sell orders not accepted in Pre-Open or Pre-Close, Day orders only, no aggregation, not accepted in the Odd Lot Market or block sales, uptick rule, flagged as short sells, eligible securities only (PSEi, MidCap and DivY constituents and ETFs; 10% short-interest cap) [^pse-short-selling-guidelines-2023-10:1-3] (P). FIX Side values: 5 = Short Sell, Z = Buy Back [^pse-fix-specification-v2-5:53] (P).
- **Algorithmic trading:** RTR is silent; the DMA Rules bar HFT/algorithmic trading through a DMA Facility; PSE says it has granted exemptions for child orders from conditioned parent orders; the Sep 2023 proposal would permit algo trading if the parent order is manually entered and child orders are limit orders, and keep HFT out of DMA [^pse-dma-rules:2,7][^pse-cn-2023-0043:3-8] (P). Only the VWAP part of CN-2023-0043 was approved (CN-2024-0010); no approval of the algo article found (G).

### Inferences
- (I) Block sales cannot be done in the Closing VWAP Session (rule window ends at Run-off).
- (I) Because odd lots only trade in continuous sessions, a board-lot residual cannot be cleaned up in the closing auction or run-off.
- (I) Short sales are permitted in Run-off, but the uptick rule (price above the last sale, or equal to it only if above the preceding different price) makes them hard to execute at a fixed Closing Price that equals the last auction print.

### Gaps
- (G) How the VWAP facility is accessed technically (web UI vs FIX) is only indirectly described.
- (G) Whether an approved block sale can still be executed in the Closing VWAP Session window is not addressed.

### Execution implications
- For a hedge fund, large pre-arranged prints need broker-side block-sale approval (PHP 20m+, within 5% of LACP) and are announced; do not expect size to be hidden before execution day (TPA announcements).
- Residual odd-lot quantities (today) must be worked in the odd-lot book during continuous trading; there is no auction path. This disappears with the NTE (lot = 1).
- Treat the 15:00-15:15 window as unavailable to a standard FIX order router; VWAP/negotiated prints need broker facilities.
- Short-selling algos must suppress the sell-short flag in pre-open and pre-close and send Day orders only.

---

## 3. What are the trading calendar, weather/emergency suspension rules, half-day practice, and trading-versus-settlement holiday differences?

### Takeaway
Trading days are all weekdays except legal holidays, special holidays, days the BSP is closed and days declared non-trading by the SEC or PSE President; PSE follows the Presidential holiday proclamations and issues a circular per month or event (2026 lead times observed: 4 days to about 4 weeks, e.g. 29 Jan for 17 Feb, 13 Mar for 20 Mar, 8 Jun for 12 Jun, 27 Jul for 21 and 31 Aug; same-day or evening-before for emergencies). Weather closures are governed by an Aug 2025 rule keyed to NCR TCWS 3+ at 06:00. PSE and the SCCP clearing house have always closed together in the examples found.

### Cited Findings
- **Rule (RTR Art. II Sec. 1):** "Every day shall be a Trading Day except for Saturdays, Sundays, legal holidays, special holidays, days when the Bangko Sentral ng Pilipinas (BSP) is closed, and such other days as may otherwise be declared by the SEC or the Exchange, through its President or other duly authorized representative, to be a non-Trading Day" [^pse-revised-trading-rules:13] (P). Aug 2012 reminder: absent an announced suspension, trading proceeds as usual; suspensions are announced via mass media, the website and SMS [^pse-memo-trading-days-suspensions-guidelines-2012:1] (P).
- **2026 non-trading weekdays (PSE circulars):**

| Date (2026) | Reason | Circular | Source |
|---|---|---|---|
| Thu 1 Jan | New Year's Day (the same circular closes 8, 24, 25, 30, 31 Dec 2025; Fri 31 Oct 2025, All Saints' Day Eve, had its own circular CN-2025-0038 [^pse-cn-2025-0038-non-trading-day-2025-10-31:1]) | CN-2025-0043 (24 Nov 2025) | [^pse-cn-2025-0043-non-trading-days:1] |
| Tue 17 Feb | Chinese New Year (special) | CN-2026-0008 | [^pse-cn-2026-0008:1] |
| Fri 20 Mar | Eid'l Fitr (Proclamation 1189, 12 Mar 2026, notice one week ahead) | CN-2026-0010 | [^pse-cn-2026-0010:1] |
| Thu 2, Fri 3, Thu 9 Apr | Maundy Thursday, Good Friday, Araw ng Kagitingan | CN-2026-0011 | [^pse-cn-2026-0011:1] |
| Fri 1 May | Labor Day | CN-2026-0016 | [^pse-cn-2026-0016:1] |
| Wed 27 May | Eid'l Adha (Proclamation 1264, 21 May 2026; PSE circular dated 22 May, five days ahead) | CN-2026-0023 | [^pse-cn-2026-0023:1] |
| Fri 12 Jun | Independence Day | CN-2026-0027 | [^pse-cn-2026-0027:1] |
| Fri 21 Aug, Mon 31 Aug | Ninoy Aquino Day, National Heroes Day | CN-2026-0034B | [^pse-cn-2026-0034b-non-trading-days-aug-2026:1] |
| Mon 2 Nov | All Souls' Day (additional special) | no PSE circular yet; Proclamation 1006 | [^pse-cn-2026-0008:3] |
| Mon 30 Nov | Bonifacio Day | no PSE circular yet; Proclamation 1006 | same |
| Tue 8 Dec; Thu 24 Dec; Fri 25 Dec; Wed 30 Dec; Thu 31 Dec | Immaculate Conception; Christmas Eve; Christmas; Rizal Day; Last Day of the Year | no PSE circular yet; Proclamation 1006 | same |

(P). Proclamation 1006 (3 Sep 2025) also lists 25 Feb 2026 (Wed, EDSA anniversary) as a special **working** day and 4 Apr (Black Saturday), 1 Nov (Sunday) as weekend dates [^pse-cn-2026-0008:3]; PSE issued no non-trading memo for 25 Feb 2026, consistent with trading (I). PSE's site notes Eid'l Fitr/Eid'l Adha closures are announced only after the government notice [^pse-web-investing-at-pse] (P).
- **2027 (government, not yet PSE):** Proclamation 1427 (issued 8 Sep 2026): regular holidays 1 Jan (Fri), 25 Mar (Thu), 26 Mar (Fri), 9 Apr (Fri), 1 May (Sat), 12 Jun (Sat), 30 Aug (Mon), 30 Nov (Tue), 25 Dec (Sat), 30 Dec (Thu); special non-working 21 Aug (Sat), 1 Nov (Mon), 8 Dec (Wed), 31 Dec (Fri); additional special 6 Feb (Sat, Chinese New Year), 27 Mar (Sat), 2 Nov (Tue), 24 Dec (Fri); 25 Feb (Thu) special working day; Eid'l Fitr and Eid'l Adha to be proclaimed later [^lawphil-proc-1427-2026][^bworld-2026-09-30-dole-2027-holidays] (S for the transcription, corroborated by a DOLE advisory report). Likely weekday PSE closures (I): 1 Jan, 25 Mar, 26 Mar, 9 Apr, 30 Aug, 1 Nov, 2 Nov, 30 Nov, 8 Dec, 24 Dec, 30 Dec, 31 Dec plus the two Eid dates.
- **16-18 Nov 2026 (ASEAN Summit):** Proclamation 1447 (17 Sep 2026) declares Mon-Wed 16-18 Nov 2026 special (non-working) days in NCR [^lawphil-proc-1447-2026]; DOLE Labor Advisory 16 (2026) confirms the pay rules [^bworld-2026-09-30-dole-2027-holidays] (S). PSE then issued two circulars on 25 Sep 2026: CN-2026-0043 said "November 16 - 18, 2026 shall be regular trading days at The Philippine Stock Exchange" [^pse-cn-2026-0043:1], and CN-2026-0044, issued later the same day, said PSE "will be releasing an updated and final advisory ... with regard to the Exchange operations on November 16-18, 2026" and that it "supersedes the aforementioned PSE circular" [^pse-trading-day-advisory-2026-11-16-18:1] (P). The first reading (open, as a regular trading day, despite the NCR proclamation) has therefore been explicitly withdrawn, not confirmed. As of 6 Oct 2026 the open/closed decision is unresolved (G); PSE's announcements archive (entries through 6 Oct 2026) shows the 25 Sep 2026 advisory as the latest word on trading days [^pse-web-announcements-archive][^pse-web-circulars-index] (P).
- **Weather and other emergencies (Guidelines on Natural Disasters or Extraordinary Circumstances, Annex B of CN-2025-0037, SEC-approved, effective immediately 20 Aug 2025):** the Exchange may halt, suspend or cancel a scheduled Trading Day when it is unable to implement its Business Continuity Plan and (a) an emergency (fire, earthquake, eruption, flood, heavy rainfall, civil commotion, terrorist attack) forces evacuation or prevents staff re-entering PSE premises, (b) an emergency may disrupt TPs accounting for more than 50% of average daily trading value (ex-blocks, six months), or (c) other emergency posing risk to staff, on MOD recommendation with the President's approval; SEC is notified immediately [^pse-cn-2025-0037:1-2,4] (P). **PAGASA TCWS in NCR:** Signal 1 or 2 => regular trading; Signal 3, 4 or 5 => no trading; if PAGASA downgrades NCR to Signal 1-2 by 06:00 of the following trading day there is no cancellation, if NCR stays at Signal 3+ at 06:00 the day is cancelled [^pse-cn-2025-0037:4-5] (P). The 2023 draft used the older "Public Storm Warning Signal" wording [^pse-cn-2023-0055:6-7] (P). Rule behind it: RTR Art. VIII Sec. 4 (cancellation announced within one hour after Pre-Open; trades and orders purged) [^pse-revised-trading-rules:36] (P).
- **Precedents (PSE circulars):** 7 Aug 2012 no trading (weather + BSP/PCHC clearing suspended) [^pse-memo-trading-suspension-2012-08-07:1]; 12 Sep 2017 no trading (clearing suspended in banking system) [^pse-cn-2017-0050-trading-suspension-2017-09-12:1]; 16 Oct 2017 no trading (PhilPaSS operations suspended) [^pse-cn-2017-0059-trading-suspension-2017-10-16:1]; 26 Dec 2017 and 2 Jan 2018 extra no-trading days (Malacanang MC 37) [^pse-cn-2017-0078-non-trading-days-dec-2017:1]; 13 Jan 2020 Taal ash, no trading and no settlement [^pse-cn-2020-0002-trading-suspension-2020-01-13:1]; 17-18 Mar 2020 ECQ [^pse-cn-2020-0021:1]; 26 Sep 2022 no trading and no SCCP settlement (announced the evening before) [^pse-cn-2022-0035-trading-suspension-2022-09-26:1]; 24 Jul 2024 no trading "today" because of inclement weather and floods (announced same day) [^pse-cn-2024-0038-trading-suspension-2024-07-24:1]; 22 Jun 2016 regular hours maintained during the Metro Manila shake drill [^pse-cn-2016-0040-shake-drill-regular-hours:1] (P).
- **Security-level halts:** e.g. one-hour halt 09:30-10:30 on MRC on 19 Jan 2026 after a material disclosure [^pse-cn-2026-0004-2-emergency-disclosures-trading-halt:1-2] (P).
- **Trading vs settlement holidays:** SCCP "Business Day" excludes holidays and days on which PSE trading or BSP/PCHC clearing is cancelled [^sccp-clearing-house-rules-2018:4] (P); equity settlement is T+2 clearing days with payment/delivery deadline 12 noon [^pse-web-investing-at-pse] (P). Every PSE weather/emergency closure above was paired with an SCCP no-clearing notice or a BSP/PhilPaSS outage. In Oct 2017 PSE consulted on adding "the policy of the Exchange is to continue to operate ... even on days when the clearing activities of the BSP or PCHC are suspended" [^pse-cn-2017-0060-proposed-amendments-trading-rules:1-2] and held a forum on a "trading day without clearing and settlement" [^pse-memo-trading-day-without-clearing-settlement-forum-2017:1]; I found no adoption (G). Settlement-day arithmetic therefore follows BSP business days, not the PSE's own calendar (I).

### Inferences
- (I) In the 2026 circulars reviewed (and the late-2025 ones) PSE closed on every nationwide Presidential holiday and special non-working day. NCR-only declarations are different: for the Manila-hosted ASEAN Summit of 13-15 Nov 2017, PSE's October 2017 non-trading circular listed only 1 and 30 Nov [^pse-cn-2017-0062-non-trading-days-nov-2017:1], I found no later non-trading circular, and PSE sent trading-floor personnel road-closure notices for 13-15 Nov [^pse-tpa-2017-0146-asean-road-closures:1], which suggests the Exchange stayed open (it had consulted on trading without clearing a month earlier, Q3 above); and on 25 Sep 2026 PSE's first circular for 16-18 Nov 2026 said "regular trading days". Both readings (open, as in 2017; closed, as for nationwide holidays) remain live for 16-18 Nov 2026 until the final advisory.
- (I) The two Eid holidays are announced late (one day to one week), so any forward calendar will have two unknown weekdays each year.

### Gaps
- (G) PSE's EDGE/"Market Calendar" page was not retrievable; the PSE site's holiday table is JavaScript-loaded and was not captured, so the weekday list is built from circulars plus Proclamation 1006.
- (G) Final PSE decision for 16-18 Nov 2026; Eid dates for 2027; PSE circulars for Nov-Dec 2026.
- (G) Intraday escalation rule (signal raised after the open) is not specified beyond Art. VIII Sec. 3-4.

### Execution implications
- Hard-code a calendar service fed by (1) Presidential proclamations and (2) the PSE circular index; model 16-18 Nov 2026 as "status unknown" (PSE first said regular trading days, then withdrew that) and make the router able to flip either way on the final advisory; if PSE opens while the BSP/PhilPaSS is closed, expect no settlement on those days and shift T+2 arithmetic accordingly (I).
- Check PAGASA NCR TCWS at 18:00 the night before and 06:00 on the day; PSE will publish a circular; implement a kill-switch for "market not open" overrides.
- Settlement date math should use the BSP/SCCP calendar; do not assume PSE trading days equal clearing days in outage events.
- No half-day sessions are expected in 2026; keep the half-day timetable parameterised (9:00-12:25) in case.

---

## 4. Which order types, validities and qualifiers exist; how do amendments, cancellations and priority work?

### Takeaway
The rulebook (2010, still the base text) defines Limit, Market, Market-to-Limit, Stop (stop-limit, stop-loss), Market-on-Opening/Closing and Cross orders; validities Day, GTC, GTD, GTW (7 calendar days), Sliding (1 year) and Fill-and-Kill; qualifiers Minimum Quantity and Iceberg (disclosed quantity). Queue priority is price-time with market orders first. Changes that increase size, change price or change a trigger price lose priority. The new engine will support only limit orders on Day 1.

### Cited Findings
#### 4.1 Order types (RTR Art. IV Sec. 9, 2010)
- **Limit:** entered Pre-Open to Trading-at-Last with a limit price within the Static Threshold; executes at limit or better; remainder queues [^pse-revised-trading-rules:21] (P).
- **Market:** no price; executes at the better of BBO and LTP; entered from Pre-Open to continuous trading; any unexecuted remainder is queued "for immediate execution" [^pse-revised-trading-rules:21-22] (P). An unfilled market order at the open triggers "reservation" of the security [^pse-revised-trading-rules:33] (P).
- **Market-to-Limit:** continuous phase only; executes at the best price between BBO and LTP, remainder becomes a limit order at the executed price; eliminated if no counterpart on entry [^pse-revised-trading-rules:22] (P).
- **Stop orders (exchange-side):** inactive until a trade occurs at the trigger price or better; trigger must be better than LTP (buy trigger above, sell trigger below). Stop-Limit has trigger price and limit price; Stop-Loss has only a trigger and becomes a market order [^pse-revised-trading-rules:22] (P). XTS FIX exposes OrdType 3 = Stop, 4 = Stop Limit with a TriggeringInstruction block (TriggerPriceType 2 = Last Trade) and an order status "X" for an untriggered order [^pse-fix-specification-v2-5:48-49,52] (P).
- **Market-on-Opening / Market-on-Closing:** entered in Pre-Open/Pre-Close, executable only at the indicative opening/closing price; if unmatched at the end of the call it becomes a limit order at that price [^pse-revised-trading-rules:22] (P).
- **Cross Order:** buy and sell by the same TP executed at agreed quantity and price within the BBO [^pse-revised-trading-rules:22] (P). FIX: New Order Cross (35=s), CrossType 1 = Cross AON, TIF IOC, limit only [^pse-fix-specification-v2-5:16-17,50] (P).
- **Order type priority:** Market Order, then MOO/MOC, then Limit; same-type market orders by time; limit orders by price then time [^pse-implementing-guidelines-trading-rules:12] (P).
- XTS FIX OrdType enumeration is 1 Market, 2 Limit, 3 Stop, 4 Stop Limit only (no Market-to-Limit or MOO/MOC value) [^pse-fix-specification-v2-5:52] (P); the 2010 rule text may therefore describe NSC-era types that XTS maps differently (I).
- **Private order book / "Unplaced" orders (XTS):** orders can be stored un-released (ExecInst S suspend, q unsuspend; OrdStatus Z) and non-Day (GTC/GTD) orders outside the day's static floor/ceiling get status "Unplaced", are invisible, and activate on a later day if inside the new thresholds [^pse-web-xts][^pse-fix-specification-v2-5:50,52] (P).

#### 4.2 Validity and qualifiers
- **Validity:** Day (to end of Trading Day); GTC (until cancelled or the security's expiry); GTD (until date); GTW (7 calendar days from posting); Sliding Validity (1 calendar year); Fill-and-Kill (in auctions fills as much as possible at the end of the call, in continuous/run-off executes immediately; remainder eliminated) [^pse-revised-trading-rules:22-23] (P).
- **Qualifiers:** Minimum-quantity (limit or market-to-limit only; executes at least the minimum immediately or is eliminated); Iceberg ("disclosed quantity"; limit or stop-limit only; disclosed quantity not less than 10% of the order and in multiples of the board lot) [^pse-revised-trading-rules:23] (P). Compatibility table (IG VII): FAK standard allowed in auctions, continuous and run-off; min-qty not allowed in auctions; disclosed quantity never allowed with FAK; Day/GTD/GTC/Sliding: standard allowed everywhere, min-qty not in auctions, disclosed qty allowed everywhere [^pse-implementing-guidelines-trading-rules:12] (P).
- **XTS FIX enumerations (v2.5, 10 Aug 2015):** TimeInForce 0 Day (default if absent), 1 GTC, 3 IOC/FaK, 4 FOK (added in v2.5), 6 GTD (ExpireDate 432), 8 Session; MinQty 110; DisplayQty 1138 ("hidden/iceberg"); ExecInst S/q [^pse-fix-specification-v2-5:3,16,50,53] (P). GTW and Sliding have no FIX value (client must use GTD-style dates) and FOK/AON are not mentioned in the RTR or IG, so whether FOK is enabled for PSE equities is undocumented (G/I).
- No fully hidden (non-displayed) order type, pegged order or stand-alone All-or-None (AON) order is described in the RTR/IG (P by absence; I); AON appears only as the FIX CrossType "Cross AON" for same-firm crosses [^pse-fix-specification-v2-5:16,50] (P).
- Pre-2010 context: the Maktrade-era PSE site (archived Jan 2009) says GTC orders on the regular board expired on the seventh calendar day after posting while GTC odd-lot orders stayed until cancelled, and that the system supported main-board, block, cross and odd-lot transactions [^pse-oldweb-trading-system-2009] (S/historical, PSE's own old page via Wayback); the NTS rulebook later split this into GTC (until cancelled/expiry), GTW (7 days) and Sliding (1 year).

#### 4.3 Modification and priority (RTR Art. IV Sec. 13; IG XI)
- Modification is allowed Pre-Open to Trading-at-Last except in the No-Cancel periods and (whole-day) the recess [^pse-implementing-guidelines-trading-rules:17][^pse-tpa-2011-0124-amended-implementing-guidelines:3][^pse-tpa-2011-0110-amended-revised-trading-rules:4] (P).
- **Keeps priority:** decrease in volume; change of validity type; change of client account code. **Loses priority:** increase in volume; change of limit price; change of trigger price. Modification between client and proprietary account is not allowed; a PC Trader cannot modify others' orders without taking ownership [^pse-revised-trading-rules:24-25][^pse-implementing-guidelines-trading-rules:18] (P). XTS FIX confirms: "Any change to the price or trigger price of an order, or increasing quantities will result in the order losing its priority", amendable fields include quantity, display qty, price, OrdType, TIF, ExpireDate, account, MinQty, trigger price, ExecInst and side (buy to buy-in, sell to short sell); the exchange may change OrderID after amendment [^pse-fix-specification-v2-5:25-26] (P).
- Priority across participants is price-time; there is no broker-priority rule, but an automatic same-TP cross lets a TP's new order match its own earlier order ahead of the queue [^pse-revised-trading-rules:31] (P).

#### 4.4 Cancellation
- Allowed in Pre-Open/Pre-Close except No-Cancel, in continuous trading (including the unmatched remainder of a partial fill), and in Run-off [^pse-implementing-guidelines-trading-rules:18] (P). Not allowed in Opening, Market Recess or Close.
- The Exchange cancels: all orders on corporate actions that adjust the closing price, **orders on the ex-date of cash/property dividends**, and orders that cross a board lot (board-lot change) [^pse-revised-trading-rules:25][^pse-implementing-guidelines-trading-rules:18] (P). A suspended security's posted orders are purged [^pse-implementing-guidelines-trading-rules:27] (P).
- Mass cancel: a TP "can only direct the Exchange to execute a cancellation of all the Orders already posted" after a failure of its FEOMS or the Exchange's Common Customer Gateway [^pse-revised-trading-rules:25][^pse-implementing-guidelines-trading-rules:18] (P). No automatic cancel-on-disconnect is documented; XTS FIX only drops a silent session after 2 x HeartBtInt + 6 seconds (66 s for a 30 s interval) [^pse-fix-specification-v2-5:14] (P/G).
- Order status vocabulary (IG X): Active, Cancelled, Error, Executed, Frozen, Market Eliminated, Modified, Scheduled, Sent, Sending, Waiting [^pse-implementing-guidelines-trading-rules:17] (P).

#### 4.5 NTE (Nasdaq Eqlipse) changes known as of Oct 2026
- "On Day 1 of the New Trading Engine, only limit order will be supported" [^pse-nte-faq-2026-08:1] (P). Odd Lot Market removed; lot size 1; Run-off orders entered/modified/executed only at the Closing Price [^pse-nte-broker-forum-2026-07-09:7] (P).
- PSETradeX (PSE's broker terminal) updates announced 15 Jan 2026: remove GTC and Next-Day validity, new "Good Till 3 Months (GT3)" for PSETradeX on-cloud, 2FA, 5,000 client-account cap per broker [^pse-nte-user-group-2026-01-15:17]; by 9 Jul 2026 the PSETradeX TP cloud migration "has been deferred" [^pse-nte-broker-forum-2026-07-09:11] (P). It is not stated whether these terminal changes reflect engine-level validity limits (G).
- Broker-side conditional orders: FEOMS may process other order types internally but only types offered by the PSE trading system may be forwarded [^pse-implementing-guidelines-trading-rules:31] (P).

### Inferences
- (I) On the NTE, market-order behaviour must be emulated with marketable limit orders; stop, iceberg and min-qty must be router-side or avoided until PSE publishes the NTE order-entry spec.
- (I) Because GTC/GTD orders are cancelled on every ex-date and corporate action, and PSE's NTE cut-over is big-bang, resting multi-day orders should be assumed lost at the cut-over.

### Gaps
- (G) NTE FIX Order Entry spec not public; no public list of NTE validities/qualifiers.
- (G) Whether XTS today actually offers Market-to-Limit, Sliding, FOK, or stop orders to external FEOMS clients (RTR/IG vs FIX enumerations differ).
- (G) No public statement on iceberg replenishment priority.
- (G) How retail brokers implement stop/trailing or other conditional orders (exchange-side stop orders exist in the rules, but FEOMS may also hold conditions internally) is not documented in PSE sources; no PSE-published broker order-type matrix was found.
- (G) Whether PSE has a published per-session order-rate/message throttle: IG XXII only says the PSE "reserves the right to impose message flow controls for the FEOMS" [^pse-implementing-guidelines-trading-rules:31].

### Execution implications
- Treat limit-Day as the lowest common denominator for the router across XTS and NTE Day 1.
- To keep time priority when scaling down, use quantity reductions; never re-price or upsize an order you want to keep in queue.
- Re-enter all GTC/GTD interest on ex-dates, after corporate actions and at the NTE cut-over.
- Do not rely on exchange-side cancel-on-disconnect; build router-side kill-switch plus a broker/Market Control mass-cancel request procedure (only allowed for FEOMS/CCG failures).
- Foreign buyers: the system earmarks foreign buy orders against the foreign-ownership room; posting buy orders to block other foreigners is a major violation, so cancel stale foreign buy orders quickly in limit-constrained names [^pse-revised-trading-rules:17,37] (P).

---

## 5. What is the board-lot table, how has it changed, and how do odd lots and the One-Lot-One-Share reform work?

### Takeaway
The PHP board-lot table has 15 price bands from 1,000,000 shares (price below PHP 0.01) to 5 shares (PHP 1,000 and above) and has not changed since the NTS launch on 26 Jul 2010. A 2023 reduction proposal (PHP 100 minimum investment) was not adopted. PSE plans to set the lot to 1 share for all securities (PHP and USD) with the NTE on 23 Nov 2026, subject to SEC approval that I could not confirm.

### Cited Findings
#### 5.1 Table in force (RTR Art. IV Sec. 8, 2010; effective 26 Jul 2010)
| Reference-price band (PHP) | Tick (PHP) | Board lot (shares) | Min notional low/high edge (PHP, derived) |
|---|---|---|---|
| 0.0001 - 0.0099 | 0.0001 | 1,000,000 | 100 / 9,900 |
| 0.0100 - 0.0490 | 0.001 | 100,000 | 1,000 / 4,900 |
| 0.0500 - 0.2490 | 0.001 | 10,000 | 500 / 2,490 |
| 0.2500 - 0.4950 | 0.005 | 10,000 | 2,500 / 4,950 |
| 0.5000 - 4.9900 | 0.01 | 1,000 | 500 / 4,990 |
| 5.0000 - 9.9900 | 0.01 | 100 | 500 / 999 |
| 10.0000 - 19.9800 | 0.02 | 100 | 1,000 / 1,998 |
| 20.0000 - 49.9500 | 0.05 | 100 | 2,000 / 4,995 |
| 50.0000 - 99.9500 | 0.05 | 10 | 500 / 999.50 |
| 100.0000 - 199.9000 | 0.10 | 10 | 1,000 / 1,999 |
| 200.0000 - 499.8000 | 0.20 | 10 | 2,000 / 4,998 |
| 500.0000 - 999.5000 | 0.50 | 10 | 5,000 / 9,995 |
| 1,000 - 1,999 | 1.00 | 5 | 5,000 / 9,995 |
| 2,000 - 4,998 | 2.00 | 5 | 10,000 / 24,990 |
| 5,000 and up | 5.00 | 5 | 25,000+ |

(P) Primary table: [^pse-revised-trading-rules:21] (scan, verified visually against the image); identical in the Oct 2023 and Dec 2025 consultations' "Existing" columns [^pse-cn-2023-0051:3-4][^pse-cn-2025-0046-board-lot-trading-at-last:4], on PSE's site [^pse-web-investing-at-pse] and in the 15 Jan 2026 NTE deck "Current Board Lot" [^pse-nte-user-group-2026-01-15:9]. Secondary corroboration from a broker FAQ [^firstmetrosec-faqs-681] (S). Derived notional column is my arithmetic (I).
Machine-readable copies (keyed on the day's Reference Price; "UP" = no upper bound):
```text
# PHP table in force 6 Oct 2026 (RTR Art. IV Sec. 8, effective 26 Jul 2010): from,to,tick,lot
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
# PHP table PROPOSED for the NTE (CN-2025-0046; NTE deck 15 Jan 2026) - not approved as of 6 Oct 2026
0.0001,0.099,0.001,1
0.10,0.995,0.005,1
1,9.99,0.01,1
10,99.95,0.05,1
100,199.90,0.10,1
200,499.80,0.20,1
500,999.50,0.50,1
1000,1999,1,1
2000,4998,2,1
5000,UP,5,1
# USD (DDS) table in force: from,to,tick,lot
0.01,0.99,0.01,100
1.00,4.99,0.01,20
5.00,9.99,0.01,10
10.00,19.98,0.02,10
20.00,49.95,0.05,10
50.00,99.95,0.05,5
100.00,199.90,0.10,5
200.00,499.80,0.20,5
500.00,999.50,0.50,5
1000.00,UP,1.00,5
# USD (DDS) table PROPOSED for the NTE
0.01,9.99,0.01,1
10,19.98,0.02,1
20,99.95,0.05,1
100,199.90,0.10,1
200,499.80,0.20,1
500,999.50,0.50,1
1000,UP,1,1
```
Sources: PHP in force [^pse-revised-trading-rules:21]; PHP proposed [^pse-cn-2025-0046-board-lot-trading-at-last:4][^pse-nte-user-group-2026-01-15:9]; USD in force [^pse-dds-rules:6] (the rule's first USD band is written "DOWN 0.99", so the 0.01 lower bound in the CSV is my floor); USD proposed [^pse-cn-2025-0046-board-lot-trading-at-last:4-5][^pse-nte-user-group-2026-01-15:10] (P).
- **Rule mechanics:** "The Board Lot and Price Fluctuation of a Security for any Trading Day shall be based on the Security's Reference Price" (previous close, adjusted close after corporate actions, or the last traded/adjusted price if the stock did not trade) [^pse-revised-trading-rules:20-21] (P). Hence lot and tick are fixed for the whole day by the reference-price band even if price crosses a band edge intraday (I). Orders for securities that cross to a different board lot are cancelled by the Exchange [^pse-revised-trading-rules:25][^pse-implementing-guidelines-trading-rules:18] (P). Normal-market orders must be whole board lots; block sales may be non-multiples [^pse-implementing-guidelines-trading-rules:24] (P).
- **Dollar-denominated securities (DDS)** (PSE DDS Rules, Part C Sec. 1): USD 0.99 and below tick 0.01 lot 100; 1.00-4.99 tick 0.01 lot 20; 5.00-9.99 tick 0.01 lot 10; 10.00-19.98 tick 0.02 lot 10; 20.00-49.95 tick 0.05 lot 10; 50.00-99.95 tick 0.05 lot 5; 100.00-199.90 tick 0.10 lot 5; 200.00-499.80 tick 0.20 lot 5; 500.00-999.50 tick 0.50 lot 5; 1,000.00 and up tick 1.00 lot 5 [^pse-dds-rules:6][^pse-dds-rules-presentation-2017:6] (P). DDS value limits are converted to pesos at the previous day's exchange rate [^pse-dds-rules:7] (P).

#### 5.2 History and reform proposals
- Pre-2010 (Maktrade) tables were not retrievable (G). The NTS rulebook (SEC-approved 1 Jun 2010) is the earliest primary table found [^pse-revised-trading-rules:2,21] (P).
- **CN-2023-0051 (9 Oct 2023; comments to 23 Oct 2023), not adopted:** to "accommodate a Php100 minimum investment", proposed lot sizes 20,000 / 5,000 / 2,000 / 400 / 100 / 20 / 10 / 5 / 2 / 1 / 1 / 1 / 1 / 1 / 1 down the 15 bands, with the 4th band stretched to 0.2500-0.9950 (tick 0.005) and the 5th band starting at 1.0000 (tick 0.01), so ticks for 0.50-0.995 would have changed from 0.01 to 0.005; all other ticks unchanged [^pse-cn-2023-0051:3-4] (P, table verified from the page image). The Dec 2025 paper treats the 2010 table as "Existing", showing it was never adopted [^pse-cn-2025-0046-board-lot-trading-at-last:3-4] (P/I).
- **CN-2025-0046 (15 Dec 2025; comments to 31 Dec 2025): "One Lot One Share"** in line with the NTE: lot size 1 share for all securities regardless of price; TPs may impose a minimum order value provided commission does not exceed the legal maximum; Odd Lot Market removed ("all references ... will be removed"); DDS table harmonised [^pse-cn-2025-0046-board-lot-trading-at-last:3-5] (P). New PHP table (price from-to / tick / lot): up to 0.099 / 0.001 / 1; 0.10-0.995 / 0.005 / 1; 1-9.99 / 0.01 / 1; 10-99.95 / 0.05 / 1; 100-199.90 / 0.10 / 1; 200-499.80 / 0.20 / 1; 500-999.50 / 0.50 / 1; 1,000-1,999 / 1 / 1; 2,000-4,998 / 2 / 1; 5,000 and up / 5 / 1 [^pse-cn-2025-0046-board-lot-trading-at-last:4][^pse-nte-user-group-2026-01-15:9] (P). New USD table: up to 9.99 / 0.01 / 1; 10-19.98 / 0.02 / 1; 20-99.95 / 0.05 / 1; 100-199.90 / 0.10 / 1; 200-499.80 / 0.20 / 1; 500-999.50 / 0.50 / 1; 1,000 and up / 1 / 1 [^pse-cn-2025-0046-board-lot-trading-at-last:4-5][^pse-nte-user-group-2026-01-15:10] (P).
- **Status:** "Targeted for implementation in Q4 2026 alongside the new trading engine"; "PSE is awaiting SEC approval of the proposed Board Lot amendments" (4 Jul 2026) and "Status: For SEC Approval" (17 Aug 2026) [^pse-asm-2026-president-report:22][^pse-analyst-briefing-1h-2026:9] (P). 9 Jul 2026 Broker Forum lists "Lot sizes will be standardized at 1 share for both DDS and PHP securities" among the major NTE trading-rule changes, and the Aug 2026 FAQ confirms "Odd Lot Market will no longer be available in the New Trading Engine" [^pse-nte-broker-forum-2026-07-09:7][^pse-nte-faq-2026-08:1] (P). PSE's NTE page still lists CN-2025-0046 as the only "Update" [^pse-web-nte], and PSE's announcements archive, which runs through 6 Oct 2026, shows no approval or effectivity circular for the board-lot amendments (the only board-lot items are the 15 Dec 2025 request for comments and the Oct 2023 proposal) [^pse-web-announcements-archive][^pse-web-circulars-index] (P by absence/G).

#### 5.3 Odd-lot market mechanics (until the NTE)
- Orders below the board lot trade only in the Odd Lot Market, symbol prefix "O"; limit and market orders; validities Day/GTW/GTD/GTC/Sliding; partial matching; Continuous Trading only; no auctions, no run-off; independent reference price (LACP) and closing price (last odd-lot trade); no dynamic threshold; commissions at TP discretion; settlement through the normal clearing path (I) [^pse-implementing-guidelines-trading-rules:19-20][^pse-revised-trading-rules:26] (P). The rule does not tie odd-lot prices to the board-lot BBO; they form in a separate order book (I).

### Inferences
- (I) The smallest economic unit under the current table is PHP 100-25,000+ per lot; the 5-share top bands mean stocks priced above PHP 1,000 trade in lots worth 5,000 to 25,000+.
- (I) Under One Lot One Share, "board lot multiples" no longer constrain child-order sizing; TPs' own minimum order values and commissions do.

### Gaps
- (G) SEC approval/effectivity date of the One-Lot-One-Share rule and the new tick table is not published as of 6 Oct 2026.
- (G) Pre-2010 board-lot tables; whether any corporate-action-specific board-lot exceptions exist.
- (G) How the NTE treats existing GTC/GTD orders when the lot changes.

### Execution implications
- Quantity rounding: floor to board-lot multiple of the day's reference-price band; keep a table keyed on reference price, not on live price.
- For stocks near band edges, tomorrow's lot can change (e.g. reference 49.95 vs 50.00 moves lot 100 to 10): GTC orders are cancelled when the lot changes.
- Minimum child size equals one lot: PHP 500-5,000 for most names below PHP 1,000, but up to PHP 25,000+ above PHP 5,000.
- On the NTE, lot = 1; retain a separate "broker minimum order value" parameter per TP.

---

## 6. What are the tick sizes (price fluctuation) by band, their history, and instrument-class exceptions?

### Takeaway
Ticks are set by the same 15-band table (see Q5) and are determined by the reference price, giving a relative tick of roughly 4-25 basis points for prices above PHP 5 but 20-10,000 bps below PHP 5. The NTE table (10 bands) will coarsen ticks in several bands (notably PHP 10-19.98: 0.02 to 0.05) and refine others (0.50-0.995: 0.01 to 0.005).

### Cited Findings
- Tick table: same rows as 5.1 (Tick column) [^pse-revised-trading-rules:21] (P). RTR definition: "Price Fluctuation or Tick Size shall mean the allowed price step based on a given price range for a Security" [^pse-revised-trading-rules:10] (P).
- Valid prices step from the band's "From" in tick increments up to the "To" value (e.g. 10.00, 10.02 ... 19.98; 20.00, 20.05 ... 49.95) (I); block sales, VWAP and negotiated prices are not tick-constrained (up to 4 decimals) [^pse-implementing-guidelines-trading-rules:23][^pse-approved-rules-vwap-trading-2024:7] (P).
- **Relative tick (bps) at band edges, current table (derived):**

| Band (PHP) | Tick | bps at low edge | bps at high edge | Ticks in band |
|---|---|---|---|---|
| 0.0001-0.0099 | 0.0001 | 10,000 | 101 | 99 |
| 0.0100-0.0490 | 0.001 | 1,000 | 204 | 40 |
| 0.0500-0.2490 | 0.001 | 200 | 40 | 200 |
| 0.2500-0.4950 | 0.005 | 200 | 101 | 50 |
| 0.5000-4.9900 | 0.01 | 200 | 20 | 450 |
| 5.0000-9.9900 | 0.01 | 20 | 10 | 500 |
| 10.0000-19.9800 | 0.02 | 20 | 10 | 500 |
| 20.0000-49.9500 | 0.05 | 25 | 10 | 600 |
| 50.0000-99.9500 | 0.05 | 10 | 5 | 1,000 |
| 100.0000-199.9000 | 0.10 | 10 | 5 | 1,000 |
| 200.0000-499.8000 | 0.20 | 10 | 4 | 1,500 |
| 500.0000-999.5000 | 0.50 | 10 | 5 | 1,000 |
| 1,000-1,999 | 1.00 | 10 | 5 | 1,000 |
| 2,000-4,998 | 2.00 | 10 | 4 | 1,500 |
| 5,000 and up | 5.00 | 10 | toward 0 | n/a |

(I) Cliffs: tick doubles from 0.01 to 0.02 at PHP 10 (10 to 20 bps), jumps 0.02 to 0.05 at PHP 20 (10 to 25 bps, the coarsest relative tick above PHP 5), and doubles or more at each boundary from PHP 100 upward (5 to 10 bps; 4 to 10 bps at PHP 500 and PHP 5,000).
- **Proposed NTE table** (see 5.2): relative tick under the new table (derived): up to 0.099: 0.001 (about 101 bps at 0.099); 0.10-0.995: 0.005 (500 bps at 0.10, 50 bps at 0.995); 1-9.99: 0.01 (100 to 10 bps); 10-99.95: 0.05 (50 bps at PHP 10, 25 bps at 19.95, 10 bps at 49.95, 5 bps at 99.95); 100+ unchanged. Tick changes versus today (I): sub-0.01 prices 0.0001 to 0.001 (coarser); 0.10-0.249 from 0.001 to 0.005 (coarser); 0.50-0.995 from 0.01 to 0.005 (finer); 10.00-19.98 from 0.02 to 0.05 (coarser); all other bands unchanged. Draft rule text keeps tick/lot "based on the given price range for the Security's Reference Price" [^pse-cn-2025-0046-board-lot-trading-at-last:3] (P).
- **Instrument classes:** ETFs use the ordinary table (PSE's ETF Rules illustrate an ETF at PHP 25.00 with tick 0.05 and lot 100 and set market-maker maximum spreads of 20 ticks up to 0.4950, 15 ticks 0.50-19.98, 10 ticks 20-999.50, 5 ticks 1,000+, minimum 5 board lots) [^pse-etf-rules:22-23] (P). DDS use the USD table (5.1). Warrants are exempt from the static threshold [^pse-revised-trading-rules:20] but no separate tick/lot table was found for warrants, preferred shares or REITs (G; I: same table). GPDRs (draft) "shall generally follow the rules and procedures of trading of equity securities" [^pse-cn-2024-0047:23] (P).
- **History:** the 15-band tick table is identical in the 2010 rulebook, 2023 proposal baseline and 2025 proposal baseline; no tick change has been adopted since 26 Jul 2010 [^pse-revised-trading-rules:21][^pse-cn-2023-0051:3][^pse-cn-2025-0046-board-lot-trading-at-last:4] (P). The NTE securities static-data file carries LACP but no tick/lot fields, so participants compute tick/lot from the table and LACP [^pse-securities-static-data-file:4] (P).

### Inferences
- (I) PSEi-type liquid stocks priced PHP 20-50 sit in the band with the largest relative tick (25 bps at PHP 20.00): spreads are tick-constrained there, so queue position dominates; between PHP 100 and 1,000 relative ticks are 4-10 bps.
- (I) The proposed NTE ticks will raise the minimum spread for PHP 10-20 stocks from 10-20 bps to 25-50 bps.

### Gaps
- (G) Whether the SEC-approved NTE tick table equals the Dec 2025 draft; no final text public.
- (G) No separate tick/lot for preferred shares, warrants or REITs was found (assumed same table).

### Execution implications
- Price rounding must use the day's reference-price band, not the live price; implement as a lookup on LACP at 08:45-09:00.
- Quote improvement costs one tick: at PHP 20.00 that is 25 bps; at PHP 499.80 it is 4 bps. Use tick-aware "join vs improve" thresholds per band.
- At the NTE cut-over, switch the price grid per the new table; band-edge logic changes at PHP 0.10, 0.50-0.995 and 10-20.

---

## 7. What order size/value limits, price collars, fat-finger controls and pre-trade risk checks apply to order entry?

### Takeaway
There is no exchange-published maximum order quantity; the exchange control is a per-order **value limit** that each TP sets per trader (capped by an undisclosed exchange-required limit), plus price validity via static/dynamic thresholds that freeze a security on breach. DMA clients additionally pass TP-defined automated pre-trade filters (exposure, order size, price limit). Foreign buy orders are earmarked against foreign-ownership room.

### Cited Findings
- **Value limit of orders (RTR Art. IV Sec. 12; IG IX):** a TP sets its own value limit per order for each Trader, not exceeding the Exchange-required limit; deviations need Exchange approval; the limit applies per order, not cumulatively per day; temporary raises by form at least one day ahead; Block Sale/TCS and VWAP also observe the limit; DDS orders are converted at the prior day's rate [^pse-revised-trading-rules:24][^pse-implementing-guidelines-trading-rules:17][^pse-approved-rules-vwap-trading-2024:4][^pse-dds-rules:7] (P). The numeric exchange-required limit is not published (G).
- **Static threshold:** order price must be within the Trading Threshold; static band originally +/-50% of Reference Price, changed to +50% / -30% from 24 Mar 2020 (CN-2020-0028) [^pse-revised-trading-rules:20][^pse-cn-2020-0028:1-2] (P); not applicable to warrants.
- **Dynamic threshold (per last-trade-to-last-trade move):** Cluster A (traded 20 times or less in six months) 20%, B (21-500 trades) 15%, C (more than 500) 10%; reviewed semi-annually (latest effective 7 Aug 2026); new listings 20% [^pse-implementing-guidelines-trading-rules:10-11][^pse-tpa-2026-0036-dynamic-threshold-review:1] (P).
- **Freeze on breach (IG XIX / RTR Art. VII Sec. 1):** an order whose price breaches the Trading Threshold freezes the security; during the freeze orders cannot be posted, modified or cancelled; Market Control acts immediately or within 5 minutes; partially matched limit orders keep intermediate trades; a breach within 5 minutes before Pre-Close is auto-rejected; unreachable TP => reject and thaw; breaching the dynamic threshold more than three times in a day with different orders is a minor violation; static breaches may be accepted within the allowed percentage and the static band stretched (RTR: to 60%) [^pse-implementing-guidelines-trading-rules:25-26][^pse-revised-trading-rules:33] (P).
- **Reservation** (market order unfilled at open, no IOP with MOO, IOP breaching the static band): orders may still be posted/modified/cancelled except crosses [^pse-implementing-guidelines-trading-rules:26][^pse-revised-trading-rules:33] (P).
- **DMA pre-trade filters (DMA Rules, SEC-approved 29 Oct 2013):** DMA TPs must have an automated risk system before the order reaches PSEtrade and define filters before a client gets access: trade exposure (gross or net), order size (PHP value and/or share volume), price limit (% or ticks from last traded price or LACP); reviewed daily; changes logged; built-in wash-sale prevention; no simultaneous multi-login; session time-out after at least 10 minutes' inactivity; logs kept five years; designated and alternate SEC-licensed traders; Sponsored Access only for QIBs; DMA facility not for HFT/algorithmic trading [^pse-dma-rules:5,7-10] (P). Customer-facing FEOMS must be PSE-certified, one CCG log-in per TP, and PSE may impose message-flow controls [^pse-implementing-guidelines-trading-rules:30-31] (P).
- **Business-continuity controls:** every TP must designate a Correspondent TP (different FEOMS vendor or a separate silo and FIX gateway) and execute via a done-through account code; two-month compliance window from 20 Aug 2025 [^pse-cn-2025-0037:2,6-7] (P).
- **Foreign ownership earmarking:** valid foreign buy orders are earmarked and reduce the volume available to later foreign buys; posting orders to block foreign buyers is a major violation [^pse-revised-trading-rules:17,37] (P). Account codes carry a Local/Foreign nationality flag; bundled orders mixing local and foreign clients must use the foreign bundled account [^pse-implementing-guidelines-trading-rules:21-22] (P).
- **Trade amendments/cancellation (post-trade):** trade cancellation form by 17:00 on T+0; amendments subject to approval; mistakes must be "evident and material" [^pse-implementing-guidelines-trading-rules:18-19,22][^pse-revised-trading-rules:26] (P).
- **Penalty exposure for order-entry misconduct:** major violations include naked/uptick short-sale breaches, odd-lot board abuse and blocking foreign buyers; first major offence PHP 100,000-199,999, second PHP 200,000-299,999, third at least PHP 300,000 plus five-day suspension [^pse-revised-trading-rules:37-39] (P, 2010 amounts).

### Inferences
- (I) The only exchange-side "fat-finger" guard is the price collar (static and dynamic). A fat-finger order inside the dynamic threshold is accepted; one outside freezes the security for up to five minutes and counts against the TP.
- (I) Quantity fat-finger limits live in TP and broker systems (value limit per trader and DMA filters), not in PSE rules.

### Gaps
- (G) Exchange-required value limit per order not published; no public per-second order/message rate limits or self-trade-prevention flags (only DMA wash-sale prevention duty).
- (G) NTE risk-control features (FIX 'Order Entry' spec) not public.

### Execution implications
- Keep marketable limit prices inside the dynamic threshold (10% for the most liquid, cluster C) of the last traded price; an order beyond it freezes the stock and is reviewable by Market Control.
- Apply a pre-trade value check per order below the trader/TP limit; ask the broker for the limit before sizing algorithm slices.
- Do not route algorithmic child orders through a pure DMA facility without broker clarity; the DMA Rules prohibit algorithmic/HFT use except where PSE has granted exemptions.
- Keep separate account codes/nationality flags correct; foreign buy orders reduce others' FOL room.

---

## Source catalog

```yaml
- slug: pse-revised-trading-rules
  title: "Revised Trading Rules (Annex B to PSE memorandum 2010-0275, SEC-approved 1 Jun 2010; effective at NTS launch 26 Jul 2010)"
  publisher: "The Philippine Stock Exchange, Inc. / SEC Market Regulation Department"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2021/04/Revised-Trading-Rules.pdf"
  local_path: "pdfs/pse-revised-trading-rules.pdf"
  edition: in-force
  amended_through: "2010-06-08"
  note: "Scanned image PDF (no text layer; OCR'd; physical pages cited). Base text only; amended piecemeal by TPA 2011-0110, TPA 2013-0185, CN-2020-0028, CN-2020-0044, CN-2024-0010, CN-2025-0037 etc. PSE posts no consolidated version."
- slug: pse-implementing-guidelines-trading-rules
  title: "Implementing Guidelines of the Revised Trading Rules (memo 2010-0340, 22 Jul 2010)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2021/04/Implementing-Guidelines-of-the-Revised-Trading-Rules.pdf"
  local_path: "pdfs/pse-implementing-guidelines-trading-rules.pdf"
  edition: in-force
  amended_through: "2010-07-22"
  note: "Original issuance effective 26 Jul 2010. Part II (hours), XI, XII, XVI-XVIII, XX since amended (TPA 2011-0124, TPA 2013-0185, CN-2020-0044, CN-2024-0010, CN-2025-0037). Used as the baseline for modification/cancellation, thresholds, odd lots, block sales."
- slug: pse-tpa-2011-0110-amended-revised-trading-rules
  title: "SEC Approved Amendments to PSE Revised Trading Rules (TPA 2011-0110, 7 Dec 2011; SEC letter 25 Oct 2011)"
  publisher: "PSE / SEC"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2024/08/1_Amended-Revised-Trading-Rules_TPA_2011-0110.pdf"
  local_path: "pdfs/pse-tpa-2011-0110-amended-revised-trading-rules.pdf"
  edition: superseded
  amended_through: "2011-12-07"
  note: "Scan; whole-day schedule (13:30 resume, 15:17 pre-close), recess added to no-modify/no-cancel, block sales incl. recess, market-halt resumption text."
- slug: pse-tpa-2011-0124-amended-implementing-guidelines
  title: "Amended Sections of the Implementing Guidelines (TPA 2011-0124, 28 Dec 2011)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2024/08/2_Amended-IRR_TPA_2011-0124.pdf"
  local_path: "pdfs/pse-tpa-2011-0124-amended-implementing-guidelines.pdf"
  edition: superseded
  amended_through: "2011-12-28"
  note: "IG hours for 2012 whole-day trading, modification/cancellation except recess, block sale application 'before Run-Off', market-halt phase tables."
- slug: pse-tpa-2013-0185-extended-pre-close
  title: "Approved Amendment to the Revised Trading Rules Regarding the Extended Pre-Close Period (TPA 2013-0185, 14 Nov 2013; with TPA 2013-0165/0167)"
  publisher: "PSE / SEC"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2024/08/4_Extended-Pre-Close_TPA_2013-0185.pdf"
  local_path: "pdfs/pse-tpa-2013-0185-extended-pre-close.pdf"
  edition: superseded
  amended_through: "2013-11-14"
  note: "Scan (OCR'd). SEC letter 29 Oct 2013; pre-close 15:15-15:18, no-cancel 15:18-15:20, effective 4 Nov 2013."
- slug: pse-memo-new-trading-hours-2011
  title: "PSE New Trading Hours (TPA 2011-0108, 6 Dec 2011)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/AnnouncementOPSPDF/PSE%20New%20Trading%20Hours.pdf"
  local_path: "pdfs/pse-memo-new-trading-hours-2011.pdf"
  edition: superseded
  amended_through: "2011-12-06"
  note: "Whole-day schedule effective 2 Jan 2012."
- slug: pse-cn-2011-0025
  title: "Public Advisory: new trading schedule effective 2 Jan 2012 (CN-2011-0025, 26 Dec 2011)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2011-0025.pdf"
  local_path: "pdfs/pse-cn-2011-0025.pdf"
  edition: superseded
  amended_through: "2011-12-26"
  note: "Image-only; OCR'd."
- slug: pse-cn-2011-0002
  title: "Survey on Extended Trading Hours (CN-2011-0002, 28 Jun 2011)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2011-0002.pdf"
  local_path: "pdfs/pse-cn-2011-0002.pdf"
  edition: historical
  amended_through: "2011-06-28"
  note: "Documents 2008 Board-approved 09:00-12:00 / 14:00-16:00 plan that was postponed."
- slug: pse-memo-extended-trading-proposal-2011
  title: "Proposed amendment of Trading Rules in relation to Extended Trading (TPA 2011-0030, 28 Jul 2011)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/AnnouncementOPSPDF/Proposed%20amendment%20of%20Trading%20Rules%20in%20relation%20to%20Extended%20Trading.pdf"
  local_path: "pdfs/pse-memo-extended-trading-proposal-2011.pdf"
  edition: historical
  amended_through: "2011-07-28"
  note: "Phase 1 (1 Oct 2011) / Phase 2 (1 Jan 2012); shows the 2010 whole-day text (14:00 / 15:45 / 15:50 / 16:00)."
- slug: sccp-memo-03-1211-settlement-unchanged-extended-hours
  title: "SCCP Memo for Brokers 03-1211: settlement deadline unchanged after extension of trading hours (16 Dec 2011)"
  publisher: "Securities Clearing Corporation of the Philippines"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/AnnouncementOPSPDF/SCCP%20Memo%20for%20Brokers%2003-1211%3A%20Settlement%20and%20Mark-to-Market%20Collateral%20Deadline%20Remain%20Unchanged%20after%20Extension%20of%20Trading%20Hours.pdf"
  local_path: "pdfs/sccp-memo-03-1211-settlement-unchanged-extended-hours.pdf"
  edition: historical
  amended_through: "2011-12-16"
  note: "OCR-style text layer; T+3 era."
- slug: pse-memo-extended-pre-close-consultation-2013
  title: "For Public Comments: Extended Pre-Close Period (TPA 2013-0107, 17 Jul 2013)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/AnnouncementOPSPDF/For%20Public%20Comments%3A%20Extended%20Pre-Close%20Period.pdf"
  local_path: "pdfs/pse-memo-extended-pre-close-consultation-2013.pdf"
  edition: superseded
  amended_through: "2013-07-17"
  note: "Peer pre-close lengths; 'previous 2h40m' trading time."
- slug: pse-memo-extended-pre-close-implementation-2013
  title: "Implementation of Extended Pre-Close Period (TPA 2013-0165, 14 Oct 2013)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/AnnouncementOPSPDF/Implementation%20of%20Extended%20Pre-Close%20Period.pdf"
  local_path: "pdfs/pse-memo-extended-pre-close-implementation-2013.pdf"
  edition: superseded
  amended_through: "2013-10-14"
  note: "Effective 4 Nov 2013."
- slug: pse-memo-pre-close-schedule-2013
  title: "Pre-Close Schedule (TPA 2013-0167, 16 Oct 2013)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/AnnouncementOPSPDF/Pre-Close%20Schedule.pdf"
  local_path: "pdfs/pse-memo-pre-close-schedule-2013.pdf"
  edition: superseded
  amended_through: "2013-10-16"
  note: "15:15-15:18 auction, 15:18-15:20 no-cancel."
- slug: pse-memo-trading-days-suspensions-guidelines-2012
  title: "Trading days and suspensions guidelines (TPA 2012-0122, 9 Aug 2012)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/AnnouncementOPSPDF/Trading%20Days%20and%20Suspensions%20Guidelines.pdf"
  local_path: "pdfs/pse-memo-trading-days-suspensions-guidelines-2012.pdf"
  edition: historical
  amended_through: "2012-08-09"
  note: "Restates RTR Art. II Sec. 1 and announcement channels."
- slug: pse-memo-trading-suspension-2012-08-07
  title: "Trading suspension 7 Aug 2012 (TPA 2012-0119)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/AnnouncementOPSPDF/TRADING%20SUSPENSION%20-%20AUGUST%207%2C%202012.pdf"
  local_path: "pdfs/pse-memo-trading-suspension-2012-08-07.pdf"
  edition: historical
  amended_through: "2012-08-07"
  note: "Weather plus BSP/PCHC clearing suspension."
- slug: pse-cn-2017-0060-proposed-amendments-trading-rules
  title: "Proposed amendments to the Trading Rules (trading when clearing suspended) (CN-2017-0060, 16 Oct 2017)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2017-0060.pdf"
  local_path: "pdfs/pse-cn-2017-0060-proposed-amendments-trading-rules.pdf"
  edition: historical
  amended_through: "2017-10-16"
  note: "Proposal only; adoption not found."
- slug: pse-memo-trading-day-without-clearing-settlement-forum-2017
  title: "Forum on Trading Day without Clearing and Settlement (TPA 2017-0138, 16 Oct 2017)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/AnnouncementOPSPDF/Forum%20on%20Trading%20Day%20without%20Clearing%20and%20Settlement.pdf"
  local_path: "pdfs/pse-memo-trading-day-without-clearing-settlement-forum-2017.pdf"
  edition: historical
  amended_through: "2017-10-16"
  note: "Invitation only."
- slug: pse-cn-2017-0050-trading-suspension-2017-09-12
  title: "Trading Suspension 12 Sep 2017 (CN-2017-0050)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2017-0050.pdf"
  local_path: "pdfs/pse-cn-2017-0050-trading-suspension-2017-09-12.pdf"
  edition: historical
  amended_through: "2017-09-12"
  note: "Clearing suspension in banking system."
- slug: pse-cn-2017-0059-trading-suspension-2017-10-16
  title: "Trading Suspension 16 Oct 2017 (CN-2017-0059, 15 Oct 2017)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2017-0059.pdf"
  local_path: "pdfs/pse-cn-2017-0059-trading-suspension-2017-10-16.pdf"
  edition: historical
  amended_through: "2017-10-15"
  note: "PhilPaSS suspension."
- slug: pse-cn-2017-0062-non-trading-days-nov-2017
  title: "Non-Trading Days (November 2017): 1 and 30 Nov (CN-2017-0062, 23 Oct 2017)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2017-0062.pdf"
  local_path: "pdfs/pse-cn-2017-0062-non-trading-days-nov-2017.pdf"
  edition: historical
  amended_through: "2017-10-23"
  note: "Used for the absence of any 13-15 Nov 2017 closure."
- slug: pse-tpa-2017-0146-asean-road-closures
  title: "Road Closures during the ASEAN Summit, 13-15 Nov 2017 (TPA 2017-0146, 8 Nov 2017)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/AnnouncementOPSPDF/Road%20Closure%20During%20The%20ASEAN%20Summit.pdf"
  local_path: "pdfs/pse-tpa-2017-0146-asean-road-closures.pdf"
  edition: historical
  amended_through: "2017-11-08"
  note: "Notice to trading-floor personnel; circumstantial evidence that PSE operated during the 2017 ASEAN Summit."
- slug: pse-cn-2017-0078-non-trading-days-dec-2017
  title: "Non-Trading Days (updated) 26 Dec 2017 and 2 Jan 2018 (CN-2017-0078, 19 Dec 2017)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2017-0078.pdf"
  local_path: "pdfs/pse-cn-2017-0078-non-trading-days-dec-2017.pdf"
  edition: historical
  amended_through: "2017-12-19"
  note: "Government work-suspension days treated as non-trading."
- slug: pse-cn-2016-0040-shake-drill-regular-hours
  title: "Regular trading hours during Metro Manila shake drill on 22 Jun 2016 (CN-2016-0040)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2016-0040.pdf"
  local_path: "pdfs/pse-cn-2016-0040-shake-drill-regular-hours.pdf"
  edition: historical
  amended_through: "2016-06-21"
  note: "Image-only; OCR'd."
- slug: pse-cn-2019-0031-trading-halt-fire-drill
  title: "Trading halt due to fire drill, 4 Jun 2019 (CN-2019-0031)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2019-0031.pdf"
  local_path: "pdfs/pse-cn-2019-0031-trading-halt-fire-drill.pdf"
  edition: historical
  amended_through: "2019-06-04"
  note: "Halt 11:45, resume 13:30, close 15:30 (then-current schedule)."
- slug: pse-cn-2020-0002-trading-suspension-2020-01-13
  title: "Trading Suspension 13 Jan 2020 (Taal) (CN-2020-0002)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2020-0002.pdf"
  local_path: "pdfs/pse-cn-2020-0002-trading-suspension-2020-01-13.pdf"
  edition: historical
  amended_through: "2020-01-13"
  note: ""
- slug: pse-cn-2020-0017
  title: "Shortened Trading Hours (CN-2020-0017, 15 Mar 2020)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2020-0017.pdf"
  local_path: "pdfs/pse-cn-2020-0017.pdf"
  edition: historical
  amended_through: "2020-03-15"
  note: ""
- slug: pse-cn-2020-0021
  title: "Trading suspension starting 17 Mar 2020 (CN-2020-0021, 16 Mar 2020)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2020-0021.pdf"
  local_path: "pdfs/pse-cn-2020-0021.pdf"
  edition: historical
  amended_through: "2020-03-16"
  note: ""
- slug: pse-cn-2020-0025-resumption-of-trading
  title: "Resumption of Trading and Settlement 19 Mar 2020 (CN-2020-0025, 17 Mar 2020)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2020-0025.pdf"
  local_path: "pdfs/pse-cn-2020-0025-resumption-of-trading.pdf"
  edition: historical
  amended_through: "2020-03-17"
  note: "Duplicate also archived by another researcher as pse-cn-2020-0025-resumption-of-trading-2020-03-19."
- slug: pse-cn-2020-0028
  title: "Amendment of Rule on Static Threshold (CN-2020-0028, 21 Mar 2020)"
  publisher: "The Philippine Stock Exchange, Inc. (SEC-approved)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2020-0028.pdf"
  local_path: "pdfs/pse-cn-2020-0028.pdf"
  edition: in-force
  amended_through: "2020-03-21"
  note: "Lower static threshold 30%, effective 24 Mar 2020."
- slug: pse-cn-2020-0035
  title: "Extension of Shortened Trading Hours to 30 Apr 2020 (CN-2020-0035)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2020-0035.pdf"
  local_path: "pdfs/pse-cn-2020-0035.pdf"
  edition: historical
  amended_through: "2020-04-13"
  note: ""
- slug: pse-cn-2020-0042
  title: "Shortened Trading Hours extended to 15 May 2020 (CN-2020-0042)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2020-0042.pdf"
  local_path: "pdfs/pse-cn-2020-0042.pdf"
  edition: historical
  amended_through: "2020-04-27"
  note: ""
- slug: pse-cn-2020-0044
  title: "Amendment of Circuit Breaker Rules (CN-2020-0044, 29 Apr 2020)"
  publisher: "The Philippine Stock Exchange, Inc. (SEC-approved 20 Mar 2020)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2020-0044.pdf"
  local_path: "pdfs/pse-cn-2020-0044.pdf"
  edition: in-force
  amended_through: "2020-04-29"
  note: "Three-level circuit breaker effective 4 May 2020."
- slug: pse-cn-2020-0046
  title: "Shortened Trading Hours under MECQ (CN-2020-0046, 14 May 2020)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2020-0046.pdf"
  local_path: "pdfs/pse-cn-2020-0046.pdf"
  edition: historical
  amended_through: "2020-05-14"
  note: ""
- slug: pse-cn-2021-0059
  title: "Adjustments in Trading Hours (CN-2021-0059, 22 Nov 2021)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2021-0059.pdf"
  local_path: "pdfs/pse-cn-2021-0059.pdf"
  edition: superseded
  amended_through: "2021-11-22"
  note: "Effective 6 Dec 2021."
- slug: pse-cn-2021-0063-half-day-trading-2021-12
  title: "Half-day trading on 24 and 31 Dec 2021 (CN-2021-0063, 15 Dec 2021)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2021-0063.pdf"
  local_path: "pdfs/pse-cn-2021-0063-half-day-trading-2021-12.pdf"
  edition: historical
  amended_through: "2021-12-15"
  note: "Last documented half-day schedule."
- slug: pse-cn-2022-0002-cancellation-of-trading-2022-01-04
  title: "Cancellation of Trading 4 Jan 2022 (CN-2022-0002)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2022-0002.pdf"
  local_path: "pdfs/pse-cn-2022-0002-cancellation-of-trading-2022-01-04.pdf"
  edition: historical
  amended_through: "2022-01-04"
  note: ""
- slug: pse-cn-2022-0001-delay-market-opening
  title: "Delay in Market Opening and Trading 4 Jan 2022 (CN-2022-0001)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2022-0001.pdf"
  local_path: "pdfs/pse-cn-2022-0001-delay-market-opening.pdf"
  edition: historical
  amended_through: "2022-01-04"
  note: "43 of 125 TPs unable to connect."
- slug: pse-cn-2022-0004
  title: "Shortened Trading Hours 14-31 Jan 2022 (CN-2022-0004, 11 Jan 2022)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2022-0004.pdf"
  local_path: "pdfs/pse-cn-2022-0004.pdf"
  edition: historical
  amended_through: "2022-01-11"
  note: ""
- slug: pse-cn-2022-0009-trading-schedule-mar-2022
  title: "Trading Schedule effective 1 Mar 2022 (CN-2022-0009, 17 Feb 2022)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2022-0009.pdf"
  local_path: "pdfs/pse-cn-2022-0009-trading-schedule-mar-2022.pdf"
  edition: in-force
  amended_through: "2022-02-17"
  note: "Core schedule still in force (VWAP session added 2024)."
- slug: pse-cn-2022-0020-market-halt-consultation
  title: "Proposed amendments to RTR and Consolidated Listing and Disclosure Rules (CN-2022-0020, 11 May 2022)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2022/05/CN_2022-0020.pdf"
  local_path: "pdfs/pse-cn-2022-0020-market-halt-consultation.pdf"
  edition: superseded
  amended_through: "2022-05-11"
  note: "Market-halt trigger proposal; final form in CN-2025-0037. Another researcher archived the same file as pse-cn-2022-0020-consultation-market-halt-and-disclosure-penalties."
- slug: pse-cn-2022-0035-trading-suspension-2022-09-26
  title: "Trading Suspension 26 Sep 2022 (CN-2022-0035)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2022-0035.pdf"
  local_path: "pdfs/pse-cn-2022-0035-trading-suspension-2022-09-26.pdf"
  edition: historical
  amended_through: "2022-09-25"
  note: ""
- slug: pse-cn-2023-0043
  title: "Proposed amendments re Algorithmic Trading and VWAP Trading (CN-2023-0043, 5 Sep 2023)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2023-0043.pdf"
  local_path: "pdfs/pse-cn-2023-0043.pdf"
  edition: superseded
  amended_through: "2023-09-05"
  note: "VWAP part approved (min value cut to PHP 500k); algo-trading part approval not found."
- slug: pse-cn-2023-0051
  title: "Proposed Amendments to the PSE Board Lot (CN-2023-0051, 9 Oct 2023)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2023-0051.pdf"
  local_path: "pdfs/pse-cn-2023-0051.pdf"
  edition: historical
  amended_through: "2023-10-09"
  note: "Image-only; table verified from page image; proposal not adopted."
- slug: pse-cn-2023-0055
  title: "Proposed Guidelines on Natural Disasters and Part XXI amendments (CN-2023-0055, 17 Oct 2023)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2023-0055.pdf"
  local_path: "pdfs/pse-cn-2023-0055.pdf"
  edition: superseded
  amended_through: "2023-10-17"
  note: "Final form in CN-2025-0037."
- slug: pse-cn-2023-0056
  title: "Short Selling Program Go Live (CN-2023-0056, 19 Oct 2023)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2023-0056.pdf"
  local_path: "pdfs/pse-cn-2023-0056.pdf"
  edition: in-force
  amended_through: "2023-10-19"
  note: "Archived by another researcher; launch date 6 Nov 2023."
- slug: pse-cn-2024-0001-market-halt
  title: "Market Halt 3 Jan 2024 (CN-2024-0001)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2024-0001.pdf"
  local_path: "pdfs/pse-cn-2024-0001-market-halt.pdf"
  edition: historical
  amended_through: "2024-01-03"
  note: ""
- slug: pse-cn-2024-0003-update-market-halt
  title: "Update on the Market Halt (CN-2024-0003, 3 Jan 2024)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2024-0003.pdf"
  local_path: "pdfs/pse-cn-2024-0003-update-market-halt.pdf"
  edition: historical
  amended_through: "2024-01-03"
  note: "Halt 09:32-11:56; afternoon 1:00-3:00 pm."
- slug: pse-approved-rules-vwap-trading-2024
  title: "Approved Rules on VWAP Trading (CN-2024-0010, 1 Feb 2024)"
  publisher: "The Philippine Stock Exchange, Inc. / SEC Markets and Securities Regulation Department"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2024/05/Approved-Rules-on-VWAP-Trading.pdf"
  local_path: "pdfs/pse-approved-rules-vwap-trading-2024.pdf"
  edition: in-force
  amended_through: "2024-02-01"
  note: "Scan (OCR'd). Latest SEC-approved restatement of RTR Art. II Sec. 2 and IG Part II; VWAP Art. VI; IG VWAP parameters (min PHP 500,000)."
- slug: pse-cn-2024-0012-vwap-go-live
  title: "VWAP Trading (Go Live) (CN-2024-0012, 15 Feb 2024)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2024-0012.pdf"
  local_path: "pdfs/pse-cn-2024-0012-vwap-go-live.pdf"
  edition: in-force
  amended_through: "2024-02-15"
  note: "Archived by another researcher; launch 1 Mar 2024."
- slug: pse-asm-2024-presidents-report
  title: "President's Report, 2024 Annual Stockholders' Meeting"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/4/"
  local_path: "pdfs/pse-asm-2024-presidents-report.pdf"
  edition: historical
  amended_through: "undated"
  note: "Archived by another researcher (exact file URL in that researcher's catalog). p.24 lists VWAP go-live 1 Mar 2024 and Short Selling launch 6 Nov 2023."
- slug: pse-cn-2024-0038-trading-suspension-2024-07-24
  title: "Trading Suspension 24 Jul 2024 (CN-2024-0038)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2024/09/CN-2024-0038.pdf"
  local_path: "pdfs/pse-cn-2024-0038-trading-suspension-2024-07-24.pdf"
  edition: historical
  amended_through: "2024-07-24"
  note: ""
- slug: pse-cn-2024-0047
  title: "Proposed Rules for Global Philippine Depositary Receipts (CN-2024-0047, 26 Sep 2024)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2024-0047.pdf"
  local_path: "pdfs/pse-cn-2024-0047.pdf"
  edition: superseded
  amended_through: "2024-09-26"
  note: "Archived by another researcher; draft; revised version awaiting SEC approval per 2026 PSE reports."
- slug: pse-cn-2025-0037
  title: "Amendments to RTR Art. VIII Sec. 2(a), Guidelines on Correspondent TP and on Natural Disasters (CN-2025-0037, 20 Aug 2025)"
  publisher: "The Philippine Stock Exchange, Inc. / SEC"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2025-0037.pdf"
  local_path: "pdfs/pse-cn-2025-0037.pdf"
  edition: in-force
  amended_through: "2025-08-20"
  note: "TCWS rule, market-halt 50% trigger, correspondent TP."
- slug: pse-cn-2025-0038-non-trading-day-2025-10-31
  title: "Non-Trading Day 31 Oct 2025 (CN-2025-0038)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2025-0038.pdf"
  local_path: "pdfs/pse-cn-2025-0038-non-trading-day-2025-10-31.pdf"
  edition: historical
  amended_through: "2025-09-24"
  note: "Not cited in text; shows PSE follows special non-working days."
- slug: pse-cn-2025-0043-non-trading-days
  title: "Non-Trading Days Dec 2025-1 Jan 2026 (CN-2025-0043, 24 Nov 2025)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2025-0043.pdf"
  local_path: "pdfs/pse-cn-2025-0043-non-trading-days.pdf"
  edition: historical
  amended_through: "2025-11-24"
  note: ""
- slug: pse-cn-2025-0046-board-lot-trading-at-last
  title: "Proposed Amendments to the PSE Board Lot and Rule on Trading during Run-Off/Trading-at-Last (CN-2025-0046, 15 Dec 2025)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2025-0046.pdf"
  local_path: "pdfs/pse-cn-2025-0046-board-lot-trading-at-last.pdf"
  edition: in-force
  amended_through: "2025-12-15"
  note: "Consultation paper (proposal; SEC approval not confirmed). Archived by another researcher."
- slug: pse-cn-2026-0004-2-emergency-disclosures-trading-halt
  title: "Emergency Disclosures and Trading Halt: MRC Allied (CN-2026-0004-2, 19 Jan 2026)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2026/01/CN-2026-0004-2.pdf"
  local_path: "pdfs/pse-cn-2026-0004-2-emergency-disclosures-trading-halt.pdf"
  edition: historical
  amended_through: "2026-01-19"
  note: "Security-level one-hour halt example."
- slug: pse-cn-2026-0008
  title: "Non-Trading Day 17 Feb 2026 with attached Proclamation No. 1006 (CN-2026-0008, 29 Jan 2026)"
  publisher: "The Philippine Stock Exchange, Inc. / Office of the President"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2026-0008.pdf"
  local_path: "pdfs/pse-cn-2026-0008.pdf"
  edition: in-force
  amended_through: "2026-01-29"
  note: "Pages 2-4 are the image copy of Proclamation 1006 (2026 holiday list)."
- slug: pse-cn-2026-0010
  title: "Non-Trading Day 20 Mar 2026 (Eid'l Fitr) (CN-2026-0010)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2026-0010.pdf"
  local_path: "pdfs/pse-cn-2026-0010.pdf"
  edition: in-force
  amended_through: "2026-03-13"
  note: ""
- slug: pse-cn-2026-0011
  title: "Non-Trading Days Apr 2026 (CN-2026-0011)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2026-0011.pdf"
  local_path: "pdfs/pse-cn-2026-0011.pdf"
  edition: in-force
  amended_through: "2026-03-24"
  note: ""
- slug: pse-cn-2026-0016
  title: "Non-Trading Day 1 May 2026 (CN-2026-0016)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2026-0016.pdf"
  local_path: "pdfs/pse-cn-2026-0016.pdf"
  edition: in-force
  amended_through: "2026-04-24"
  note: ""
- slug: pse-cn-2026-0023
  title: "Non-Trading Day 27 May 2026 (Eid'l Adha) (CN-2026-0023)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2026-0023.pdf"
  local_path: "pdfs/pse-cn-2026-0023.pdf"
  edition: in-force
  amended_through: "2026-05-22"
  note: ""
- slug: pse-cn-2026-0027
  title: "Non-Trading Day 12 Jun 2026 (CN-2026-0027)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2026-0027.pdf"
  local_path: "pdfs/pse-cn-2026-0027.pdf"
  edition: in-force
  amended_through: "2026-06-08"
  note: ""
- slug: pse-cn-2026-0034b-non-trading-days-aug-2026
  title: "Non-Trading Days Aug 2026 (CN-2026-0034B, 27 Jul 2026)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2026/07/CN-2026-0034B.pdf"
  local_path: "pdfs/pse-cn-2026-0034b-non-trading-days-aug-2026.pdf"
  edition: in-force
  amended_through: "2026-07-27"
  note: ""
- slug: pse-cn-2026-0031-negotiated-trades
  title: "Invitation to Submit Comments on Proposed Rules on Negotiated Trades (CN-2026-0031, 1 Jul 2026)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2026-0031.pdf"
  local_path: "pdfs/pse-cn-2026-0031-negotiated-trades.pdf"
  edition: in-force
  amended_through: "2026-07-01"
  note: "Consultation draft; not in force. Status 'Revising per Public Comments' (17 Aug 2026)."
- slug: pse-cn-2026-0043
  title: "Regular Trading Days (November 16-18, 2026) (CN-2026-0043, 25 Sep 2026; superseded the same day by CN-2026-0044)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2026-0043.pdf"
  local_path: "pdfs/pse-cn-2026-0043.pdf"
  edition: superseded
  amended_through: "2026-09-25"
  note: "Archived by another researcher; superseded the same day by CN-2026-0044. (PSE's circular index separately lists a dividends circular under a similar CN-2026-0043 label; the regular-trading-days memo is the CircularOPSPDF file.)"
- slug: pse-trading-day-advisory-2026-11-16-18
  title: "Trading Day Advisory (November 16-18, 2026) (CN-2026-0044, 25 Sep 2026)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2026/09/November-16-18_Trading-Days_hold_updated.pdf"
  local_path: "pdfs/pse-trading-day-advisory-2026-11-16-18.pdf"
  edition: in-force
  amended_through: "2026-09-25"
  note: "Same advisory also archived by another researcher as pse-cn-2026-0044."
- slug: pse-tpa-2026-0036-dynamic-threshold-review
  title: "Dynamic Threshold Semi-Annual Review (TPA 2026-0036, 3 Aug 2026)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/TPA-2026-0036.pdf"
  local_path: "pdfs/pse-tpa-2026-0036-dynamic-threshold-review.pdf"
  edition: in-force
  amended_through: "2026-08-03"
  note: "Effective 7 Aug 2026."
- slug: pse-tpa-2026-0015-block-sale-dhi
  title: "Execution of Block Sale for DHI Shares (TPA 2026-0015, 16 Mar 2026)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/TPA-2026-0015.pdf"
  local_path: "pdfs/pse-tpa-2026-0015-block-sale-dhi.pdf"
  edition: historical
  amended_through: "2026-03-16"
  note: ""
- slug: pse-tpa-2026-0023-block-sale-pal
  title: "Execution of Block Sale for PAL Shares (TPA 2026-0023, 28 May 2026)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/TPA-2026-0023.pdf"
  local_path: "pdfs/pse-tpa-2026-0023-block-sale-pal.pdf"
  edition: historical
  amended_through: "2026-05-28"
  note: ""
- slug: pse-tpa-2026-0012-block-sale-ati-tender-offer
  title: "Execution of Block Sales for ATI Shares (TPA 2026-0012, 12 Mar 2026)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/TPA-2026-0012.pdf"
  local_path: "pdfs/pse-tpa-2026-0012-block-sale-ati-tender-offer.pdf"
  edition: historical
  amended_through: "2026-03-12"
  note: "Archived by another researcher."
- slug: pse-nte-user-group-2026-01-15
  title: "New Trading Engine, PSETradeX, PSE Back-office Updates: Broker Forum (15 Jan 2026)"
  publisher: "The Philippine Stock Exchange, Inc. (Market Operations Division)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2026/07/NTE-User-Group.pdf"
  local_path: "pdfs/pse-nte-user-group-2026-01-15.pdf"
  edition: in-force
  amended_through: "2026-01-15"
  note: "Archived by another researcher; identical bytes to the file I downloaded. Lot/tick tables p.9-10; run-off p.11-15; PSETradeX p.17."
- slug: pse-nte-broker-forum-2026-07-09
  title: "New Trading Engine, PSETradeX, PSE Back-office Updates: Broker Forum (9 Jul 2026)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2026/07/PSE-New-Trading-Engine-TradeX-Back-office_Broker-Forum_07092026-1.pdf"
  local_path: "pdfs/pse-nte-broker-forum-2026-07-09.pdf"
  edition: in-force
  amended_through: "2026-07-09"
  note: "Go-live 23 Nov 2026; MR dates; TP readiness; Negotiated Trade salient features."
- slug: pse-nte-faq-2026-08
  title: "New Trading Engine FAQ (Aug 2026)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2026/08/Frequent-Asked-Questions.pdf"
  local_path: "pdfs/pse-nte-faq-2026-08.pdf"
  edition: in-force
  amended_through: "undated"
  note: "Date inferred from content (specs released 23 Jul 2026; data from 3 Aug 2026)."
- slug: pse-analyst-briefing-1h-2026
  title: "PSE STAR 1H 2026 analyst briefing (17 Aug 2026)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/4/2026/08/2026.08.17-PSE-STAR-1H-2026.pdf"
  local_path: "pdfs/pse-analyst-briefing-1h-2026.pdf"
  edition: in-force
  amended_through: "2026-08-17"
  note: "Archived by another researcher. p.9: One Share One Lot 'For SEC Approval' (Q4 2026 target); Negotiated Trades 'Revising per Public Comments'."
- slug: pse-asm-2026-president-report
  title: "President's Report, 2026 Annual Stockholders' Meeting (4 Jul 2026)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/4/"
  local_path: "pdfs/pse-asm-2026-president-report.pdf"
  edition: in-force
  amended_through: "2026-07-04"
  note: "Archived by another researcher (exact URL in that researcher's catalog). p.22: awaiting SEC approval of Board Lot amendments."
- slug: pse-securities-static-data-file
  title: "PSE Securities Static Data Specifications v1.0 (22 Jun 2026)"
  publisher: "The Philippine Stock Exchange, Inc. (CMDD Market Data Department)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2026/07/PSE_Securities-Static-Data_File_v1.0-1.pdf"
  local_path: "pdfs/pse-securities-static-data-file.pdf"
  edition: in-force
  amended_through: "2026-06-22"
  note: "Archived by another researcher; fields: LACP, short-sell eligibility, no tick/lot field."
- slug: pse-fix-specification-v2-5
  title: "PSE FIX Specification for X-stream v2.5 (10 Aug 2015)"
  publisher: "The Philippine Stock Exchange, Inc. / OMX Technology AB"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2021/01/PSE_FIX_Specification_v2_5-10-August-2015.pdf"
  local_path: "pdfs/pse-fix-specification-v2-5.pdf"
  edition: in-force
  amended_through: "2015-08-10"
  note: "Archived by another researcher. Legacy XTS FIX spec still posted; NTE FIX specs v0.1/v1.1 not public."
- slug: pse-dma-rules
  title: "PSE Rules on Direct Market Access (SEC-approved 29 Oct 2013)"
  publisher: "The Philippine Stock Exchange, Inc. / SEC"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2021/04/SEC-Approved-DMA-Rules.pdf"
  local_path: "pdfs/pse-dma-rules.pdf"
  edition: in-force
  amended_through: "2013-10-29"
  note: "Archived by another researcher; scan (OCR'd). Sec. 9 restrictions, Sec. 11 pre-trade risk filters."
- slug: pse-dds-rules
  title: "PSE Rules on Dollar Denominated Securities (DDS)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2021/01/Approved_DDS_Rules.pdf"
  local_path: "pdfs/pse-dds-rules.pdf"
  edition: in-force
  amended_through: "undated"
  note: "Part C Sec. 1 USD board lot/tick table and block-sale thresholds."
- slug: pse-dds-rules-presentation-2017
  title: "DDS Rules training presentation (July 2017)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2021/01/DDS_Presentation_PSE_DDS_Rules_July2017-1.pdf"
  local_path: "pdfs/pse-dds-rules-presentation-2017.pdf"
  edition: historical
  amended_through: "2017-07-18"
  note: "Corroborates USD table."
- slug: pse-etf-rules
  title: "SEC Approved PSE ETF Rules (18 Mar 2013)"
  publisher: "The Philippine Stock Exchange, Inc. / SEC"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2021/04/PSE-ETF-RULES-A-B-C-for-Website.pdf"
  local_path: "pdfs/pse-etf-rules.pdf"
  edition: in-force
  amended_through: "2013-03-18"
  note: "Archived by another researcher; amendments proposed 16 Jun 2026 (CN-2026-0029) not in force."
- slug: pse-cn-2014-0057-trading-halt-2014-11-20
  title: "Trading Halt due to Technical Issues, 20 Nov 2014 (CN-2014-0057)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2014-0057.pdf"
  local_path: "pdfs/pse-cn-2014-0057-trading-halt-2014-11-20.pdf"
  edition: historical
  amended_through: "2014-11-20"
  note: "Archived by another researcher; image-only (OCR'd). Halt 13:46, resumed 14:30, close 15:30."
- slug: pse-cn-2015-0110-trading-halt-2015-08-24
  title: "Trading Halt 24 Aug 2015 (CN-2015-0110)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2015-0110.pdf"
  local_path: "pdfs/pse-cn-2015-0110-trading-halt-2015-08-24.pdf"
  edition: historical
  amended_through: "2015-08-24"
  note: "Archived by another researcher; image-only (OCR'd). Halt at 14:05:26."
- slug: pse-cn-2015-0112-trading-halt-2015-08-25
  title: "Trading Halt 25 Aug 2015 (CN-2015-0112)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2015-0112.pdf"
  local_path: "pdfs/pse-cn-2015-0112-trading-halt-2015-08-25.pdf"
  edition: historical
  amended_through: "2015-08-25"
  note: "Archived by another researcher; image-only (OCR'd). Halt at 10:02:22."
- slug: pse-cn-2016-0020-trading-halt-2016-04-08
  title: "Trading Halt 8 Apr 2016 (CN-2016-0020)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2016-0020.pdf"
  local_path: "pdfs/pse-cn-2016-0020-trading-halt-2016-04-08.pdf"
  edition: historical
  amended_through: "2016-04-08"
  note: "Archived by another researcher; image-only (OCR'd). Halt at 10:29:18."
- slug: pse-cn-2024-0061-adjusted-schedule-2024-12-09
  title: "Adjusted Trading Schedule for Today, 9 Dec 2024 (CN-2024-0061)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2024-0061.pdf"
  local_path: "pdfs/pse-cn-2024-0061-adjusted-schedule-2024-12-09.pdf"
  edition: historical
  amended_through: "2024-12-09"
  note: "Archived by another researcher. Pre-Open 09:40, Pre-Open No Cancel 09:50, Market Open 09:55."
- slug: pse-cn-2025-0014
  title: "Delay in Market Open, 24 Mar 2025 (CN-2025-0014)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2025-0014.pdf"
  local_path: "pdfs/pse-cn-2025-0014.pdf"
  edition: historical
  amended_through: "2025-03-24"
  note: "Archived by another researcher."
- slug: pse-cn-2025-0015-adjusted-schedule-2025-03-24
  title: "Adjusted Trading Schedule for Today, 24 Mar 2025 (CN-2025-0015)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2025-0015.pdf"
  local_path: "pdfs/pse-cn-2025-0015-adjusted-schedule-2025-03-24.pdf"
  edition: historical
  amended_through: "2025-03-24"
  note: "Archived by another researcher. Pre-Open No Cancel 11:05, Market Open 11:10."
- slug: pse-cn-2019-0004-short-selling-guidelines-amendment
  title: "Amendments to the PSE Guidelines for Short Selling Transactions (CN-2019-0004, 23 Jan 2019)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2019-0004.pdf"
  local_path: "pdfs/pse-cn-2019-0004-short-selling-guidelines-amendment.pdf"
  edition: historical
  amended_through: "2019-01-23"
  note: "Archived by another researcher; short-sell orders rejected only in Pre-Open and Pre-Close."
- slug: pse-short-selling-guidelines-2023-10
  title: "PSE Guidelines on Short Selling Transactions (as of Oct 2023)"
  publisher: "The Philippine Stock Exchange, Inc. / SEC"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2024/05/PSE-Guidelines-on-Short-Selling-Transactions_Oct2023_v3.pdf"
  local_path: "pdfs/pse-short-selling-guidelines-2023-10.pdf"
  edition: in-force
  amended_through: "2023-10-16"
  note: "Archived by another researcher."
- slug: sccp-clearing-house-rules-2018
  title: "Rules of the Securities Clearing Corporation of the Philippines (2018 edition)"
  publisher: "Securities Clearing Corporation of the Philippines"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2021/04/SCCP_Revised_Rules.pdf"
  local_path: "pdfs/sccp-clearing-house-rules-2018.pdf"
  edition: superseded
  amended_through: "2018-01-01"
  note: "Archived by another researcher; T+3 era text; cited only for the Business Day definition (p.4). Date inferred from file name; treat as undated."
- slug: pse-web-investing-at-pse
  title: "PSE website: Investing at PSE (Trading Hours & Holidays; Board Lot Table; settlement)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: web
  canonical_url: "https://www.pse.com.ph/investing-at-pse/"
  local_path: null
  edition: in-force
  amended_through: "undated"
  note: "Retrieved 6 Oct 2026. Schedule table current; FAQ prose stale (09:30-12:00 / 13:30-15:30; 50% band). Holiday table is JavaScript-loaded and was not captured."
- slug: pse-web-xts
  title: "PSE website: PSEtrade XTS overview and system features"
  publisher: "The Philippine Stock Exchange, Inc."
  type: web
  canonical_url: "https://www.pse.com.ph/psetrade-xts/"
  local_path: null
  edition: in-force
  amended_through: "undated"
  note: "Retrieved 6 Oct 2026; migration 22 Jun 2015; private order book; unplaced orders."
- slug: pse-web-nte
  title: "PSE website: PSE Trading Engine 2026 (system features, FIX gateway, updates tabs)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: web
  canonical_url: "https://www.pse.com.ph/pse-new-trading-engine/"
  local_path: null
  edition: in-force
  amended_through: "undated"
  note: "Retrieved 6 Oct 2026. Lists FIX/ITCH/MDF spec versions (not downloadable) and CN-2025-0046 as only Update."
- slug: pse-web-regulatory-framework
  title: "PSE website: Regulations - Trading Participants - Regulatory Framework"
  publisher: "The Philippine Stock Exchange, Inc."
  type: web
  canonical_url: "https://www.pse.com.ph/regulation-trading-participants/"
  local_path: null
  edition: in-force
  amended_through: "undated"
  note: "Retrieved 6 Oct 2026. Index of RTR, IG and posted amendments (no consolidated text)."
- slug: pse-oldweb-trading-system-2009
  title: "PSE old website: Trading Mechanism / MakTrade system description (Wayback snapshot 6 Jan 2009)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: web
  canonical_url: "https://web.archive.org/web/20090106041916/http://www.pse.com.ph/html/AboutPSE/trading_system.html"
  local_path: null
  edition: historical
  amended_through: "2009-01-06"
  note: "Historical Maktrade-era description; GTC 7-day expiry for regular board orders."
- slug: pse-web-announcements-archive
  title: "PSE website: News and Announcement Archive (circulars, trading-participant advisories)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: web
  canonical_url: "https://www.pse.com.ph/news-and-announcement-archive/"
  local_path: null
  edition: in-force
  amended_through: "undated"
  note: "Retrieved 6 Oct 2026; entries run through 6 Oct 2026. Used for absence evidence (no board-lot approval circular; no final Nov 16-18 advisory)."
- slug: pse-quote-file-eod-spec-2014
  title: "Quote File for End-of-Day Security Prices (updated 4 Nov 2014)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2021/01/Quote-File-for-End-of-Dat-Security-Prices-updated-as-of-November-04-2014.pdf"
  local_path: "pdfs/pse-quote-file-eod-spec-2014.pdf"
  edition: historical
  amended_through: "2014-11-04"
  note: "Archived by another researcher; defines Day Close and Last Traded Price fallback; EOD file carries a Board Lot field."
- slug: pse-web-circulars-index
  title: "PSE website: circulars and announcements index"
  publisher: "The Philippine Stock Exchange, Inc."
  type: web
  canonical_url: "https://www.pse.com.ph/?p=279"
  local_path: null
  edition: in-force
  amended_through: "undated"
  note: "Retrieved 6 Oct 2026; used to establish absence of an approval circular for One Lot One Share and of a final Nov 16-18 advisory."
- slug: lawphil-proc-1447-2026
  title: "Proclamation No. 1447 (17 Sep 2026): special non-working days 16-18 Nov 2026 in NCR"
  publisher: "Office of the President of the Philippines (via LawPhil)"
  type: web
  canonical_url: "https://lawphil.net/executive/proc/proc2026/proc_1447_2026.html"
  local_path: null
  edition: in-force
  amended_through: "2026-09-17"
  note: "Summarised via fetch tool; verify wording against the original."
- slug: lawphil-proc-1427-2026
  title: "Proclamation No. 1427 (8 Sep 2026): 2027 regular holidays and special days"
  publisher: "Office of the President of the Philippines (via LawPhil)"
  type: web
  canonical_url: "https://lawphil.net/executive/proc/proc2026/proc_1427_2026.html"
  local_path: null
  edition: in-force
  amended_through: "2026-09-08"
  note: "Fetch-tool summary mislabels some categories; dates cross-checked with DOLE advisory report."
- slug: bworld-2026-09-30-dole-2027-holidays
  title: "DoLE sets pay rules for ASEAN Summit, 2027 holidays"
  publisher: "BusinessWorld"
  type: web
  canonical_url: "https://bworldonline.com/the-nation/2026/09/30/783394/dole-sets-pay-rules-for-asean-summit-2027-holidays"
  local_path: null
  edition: n/a
  amended_through: "2026-09-30"
  note: "Secondary; cites Labor Advisory 16 and 17 (2026), Proclamations 1447 and 1427."
- slug: philstar-2026-07-23-nte-go-live
  title: "New PSE trading engine goes live by November"
  publisher: "The Philippine Star"
  type: web
  canonical_url: "https://www.philstar.com/business/2026/07/23/2543942/new-pse-trading-engine-goes-live-november"
  local_path: null
  edition: n/a
  amended_through: "2026-07-23"
  note: "Secondary; capacity figures (11-hour session, 5m orders, 450k trades)."
- slug: philstar-2008-12-04-extended-hours
  title: "PSE drafts new rules to allow extended trading hours"
  publisher: "The Philippine Star"
  type: web
  canonical_url: "https://www.philstar.com/business/2008/12/04/420521/pse-drafts-new-rules-allow-extended-trading-hours/amp/"
  local_path: null
  edition: n/a
  amended_through: "2008-12-04"
  note: "Secondary; 2008 hours 9:30-noon and proposed 14:00-16:00 afternoon session."
- slug: firstmetrosec-help-34
  title: "First Metro Securities help: Can I enter an order anytime during the day?"
  publisher: "First Metro Securities Brokerage Corporation"
  type: web
  canonical_url: "https://www.firstmetrosec.com.ph/fmsec/article/34-"
  local_path: null
  edition: superseded
  amended_through: "2015-02-13"
  note: "Stale (shows 2020-21 shortened hours); cited as a stale-data warning only."
- slug: firstmetrosec-faqs-681
  title: "First Metro Securities FAQs (board lots and price fluctuations)"
  publisher: "First Metro Securities Brokerage Corporation"
  type: web
  canonical_url: "https://www.firstmetrosec.com.ph/fmsec/article/681-faqs"
  local_path: null
  edition: n/a
  amended_through: "2018-04-26"
  note: "Secondary; reproduces the 15-band table (matches PSE)."
```
