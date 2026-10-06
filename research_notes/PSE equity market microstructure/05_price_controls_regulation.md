# PSE price controls, trading halts, market-conduct rules and regulatory constraints on trading (inputs to Chapters 7 and 13) — state as of 6 October 2026

**Reading guide.** Tags: **[P]** primary source (PSE rule/circular, SEC rule, statute); **[S]** secondary-only (news/commentary — corroborates or fills gaps, never the sole basis for a rule); **[I]** my inference. A citation marker made of a caret-bracket with slug, colon and number (written "[^ slug:N ]" here, without the spaces, in the body) = physical page N (what a PDF viewer shows) of `kb/pdfs/<slug>.pdf`; a marker with the slug only = web page. All slugs are listed in the Source catalog. "In force" means *no later superseding instrument found by me*; where that is only an absence-of-evidence statement I say so. Scanned PDFs (Revised Trading Rules, CMIC Rules, DMA Rules, 2011 amendments, 2014-16 halt notices) were read by OCR plus visual check of the key pages.

### Scope note and snapshot

The PSE has **no consolidated current text of its trading rules**. The "regulatory framework" it publishes for Trading Participants (TPs) is the 2010 base (Revised Trading Rules, "RTR", and Implementing Guidelines, "IG", both taking effect on launch of the New Trading System on Mon 26 July 2010) plus a stack of circulars; the PSE's own page lists that stack (base documents plus amending memos, no consolidated edition) ([^pse-web-regulation-trading-participants]). **[P]** [^pse-revised-trading-rules:1][^pse-implementing-guidelines-trading-rules:1]. Consequence for readers: every "current" parameter below is a base rule *plus* amendments, and the PSE's public investor FAQ is stale (it still says a 50% floor and a 3:30 pm close) ([^pse-web-investing-at-pse]) — use the circulars.

Related notes: session/phase clock times and tick rules are in `03_sessions_orders_ticks_lots.md`; short selling, market making and margin financing (SRC Rule 48.1 and its pending 25 Aug 2026 replacement draft) are in `06_market_making_short_selling.md`; foreign-ownership limits, taxes and access are in `09_costs_taxes_foreign_access.md`; the dated reform list is in `11_reform_timeline.md`. This note does not repeat them except where they block or penalise an order.

| Control | In force on 6 Oct 2026 | Effective | Replaced | Key source |
|---|---|---|---|---|
| Static price band | +50% / −30% of Reference Price | Tue 24 Mar 2020 | ±50% (from 26 Jul 2010) | CN-2020-0028 |
| Dynamic threshold (DT) | 20% / 15% / 10% by 6-month trade-count cluster A/B/C; new listings 20%; latest cluster list effective Fri 7 Aug 2026 | clusters since 26 Jul 2010; list refreshed Feb/Aug | — | IG VI; TPA-2026-0036 |
| Freeze → Market Control accept/reject | unchanged | 26 Jul 2010 | — | RTR Art VII §1; IG XIX |
| Market-wide circuit breaker | PSEi −10% / −15% / −20% vs prior close → 15 / 30 / 60-minute halt; each level once per day | Mon 4 May 2020 | single level −10% / 15 min (adopted Sep 2008) | CN-2020-0044 |
| System-failure market halt | TPs with >50% of 6-month ADTV (ex-block sales) unable to trade even via correspondent TP; correspondent TP mandatory; NCR typhoon signal ≥3 → no trading | 20 Aug 2025 (correspondents +2 months) | 1/3 of TP-users unable to connect | CN-2025-0037 |
| Disclosure | material info to PSE within 10 minutes, before the media; EDGE release cut-off 4:00 pm | cut-off 25 May 2026 | 3:30 pm cut-off (1 Mar 2022) | CLDR Art VII; CN-2026-0024 |
| MPO | non-compliance → suspension ≤6 months then automatic delisting; new MPO tiers | 11 Aug 2026 | earlier "Amended MPO Rule" (same suspension wording) | Amended MPO Rule memo |
| Algo / HFT via DMA | prohibited (DMA Rules); "algorithmic trading" article proposed 2023, **no approval found** | DMA Rules, first trading day of 2014 (2 Jan) | — | DMA Rules; CN-2023-0043 |
| VWAP trading | live (Closing VWAP session after run-off) | 1 Mar 2024 | — | CN-2024-0010/-0012 |
| Day schedule | pre-open 9:00, no-cancel 9:15, open 9:30, recess 12:00, resume 13:00, pre-close 14:45, no-cancel 14:48, run-off 14:50, Closing VWAP 15:00, close 15:15 | 1 Mar 2022 (Closing VWAP session from 1 Mar 2024) | Omicron shortened hours (from 14 Jan 2022); the pre-COVID day (2 Jan 2012–Mar 2020) resumed 13:30 and closed 15:30 | CN-2022-0009; VWAP rules |
| New Trading Engine (Nasdaq Eqlipse) | **scheduled go-live Mon 23 Nov 2026**; threshold/circuit-breaker parameters not published in documents I found | — | PSETrade XTS | NTE broker forum 9 Jul 2026 |

---

## 1. Daily price limits ("static thresholds"): values, computation, reference price after corporate actions, special cases

### Takeaway
Since 24 March 2020 every order price must lie within **+50% / −30%** of the Reference Price (previous close, or the Adjusted Closing Price after a corporate action, or the last traded/adjusted price if the stock did not trade the previous day). The band is administered by the Exchange, not hard-coded: it can be lifted case-by-case (post-suspension resumptions, follow-on offerings, listing by introduction), and a breaching order does not simply bounce — it freezes the stock for Market Control (see §2).

### Cited findings
- **[P]** The static band was cut on the downside only: RTR Art. IV §7(b) now reads "upper Static Threshold … fifty percent (50%) above the Reference Price while the lower Static Threshold … thirty percent (30%) below"; IG VI par. 2(b) amended to "fifty percent (50%) above and thirty percent (30%) below the previous day's Reference or Closing Price or the Last Adjusted Closing Price (LACP)". SEC-approved; implemented in PSETrade from Tuesday 24 March 2020; circular dated 21 March 2020 [^pse-cn-2020-0028:1][^pse-cn-2020-0028:2]. CN-2020-0044 states the SEC approved the circuit-breaker rule amendments on 20 March 2020 and refers back to the 30% floor as "another tool to contain the expected high volatility" ([^pse-cn-2020-0044:1]).
- **[P]** PSE press release of 21 March 2020: lower threshold reduced from 50% to 30%; PSE President Monzon: "We benchmarked the adjusted lower static threshold level with what other exchanges in the region currently implement, which is between 10 and 30 percent"; upper threshold "will remain at 50 percent" ([^pse-web-press-2020-03-21-static-threshold]).
- **[P]** What it replaced: the 2010 base RTR Art. IV §7 and IG VI.2(b) set the static threshold at 50% each way ("fifty percent (50%) of the previous day's Reference or Closing Price or the Last Adjusted Closing Price") [^pse-revised-trading-rules:20][^pse-implementing-guidelines-trading-rules:10]; effective with the New Trading System launch Mon 26 July 2010 [^pse-implementing-guidelines-trading-rules:1].
- **[P]** Reference Price (RTR Art. IV §6): (a) previous Trading Day's Closing Price; (b) the Adjusted Closing Price (ACP) "in the event of corporate actions that would result to an adjustment of the Closing Price"; (c) the Last Traded Price or last ACP "in cases where there is no trading activity for the Security in the immediately preceding Trading Day" [^pse-revised-trading-rules:20]. ACP is defined only as "the Closing Price of a Security with adjustments due to corporate events" [^pse-revised-trading-rules:8]. Opening-price tie-breaks use the Reference Price (previous close/LACP); closing-price tie-breaks use the LTP [^pse-implementing-guidelines-trading-rules:16].
- **[P]** Limit orders must carry "a specified limit price within the Security's Static Threshold" (RTR Art. IV §9(a)(i)) [^pse-revised-trading-rules:21]. The static threshold "is not applicable to warrants" [^pse-revised-trading-rules:20][^pse-implementing-guidelines-trading-rules:10].
- **[P]** Corporate actions reset the book: the Exchange cancels (i) orders in a security whose closing price is adjusted by a corporate action, (ii) orders on the ex-date of cash/property dividends, (iii) orders that cross a board lot [^pse-revised-trading-rules:25][^pse-tpa-2011-0110-amended-revised-trading-rules:4]; IG XII.4–5 repeat it for corporate actions and board-lot changes [^pse-implementing-guidelines-trading-rules:18].
- **[P]** Reference-price errors do cause suspensions: on 21 Dec 2023 trading in UnionBank (UBP) was suspended for the day because "the stock's previous closing price was not adjusted to account for UBP's 27 percent stock dividends"; trading resumed 22 Dec "with the adjusted share price" ([^pse-cn-2023-0074-ubp-trading-suspension:1]).
- **[P]** New 2026 rule for declassified dual-class shares: after declassification the adjusted price is "based on the closing price of the Class 'A' shares or Class 'B' shares, whichever is higher" on the last trading day before declassification, and PSE imposes a **two-trading-day suspension** before the delisting of the classified shares (sample timeline: last trading day Thu 10 Sep 2026; suspension from Fri 11 Sep; T+2 completes Mon 14 Sep; declassification, delisting and resumed trading Tue 15 Sep) — circular dated 10 Sep 2026 ([^pse-cn-2026-0041-declassification-price-suspension:1][^pse-cn-2026-0041-declassification-price-suspension:2]).
- **[P]** Lifting the band (RTR Art. VII §6): lifted (a) "on the day of resumption of trading for Securities that have been suspended for at least one year"; (b) "on the listing date of Securities that are listed by way of introduction"; (c) "upon consideration by the Exchange" where an occurrence may change the price drastically or the band would make trading "impractical", announced case-by-case. In (a) and (c) the band stays lifted "until such time that trades have been executed which will eventually be the basis of the ceiling and floor prices on the following day" [^pse-revised-trading-rules:34]. Procedure (IG VI.6): MRD/IRD recommendation → PSE Management Committee approval → Market Control lifts before pre-open; if approval arrives during/after pre-open the lift takes effect next trading day; announced on the PSE website beforehand [^pse-implementing-guidelines-trading-rules:11]. IG VI.5: if a security did not trade on its listing date, next day's static threshold is based on "the indicative reference opening price of the Security provided by the company" [^pse-implementing-guidelines-trading-rules:11].
- **[P]** Case-by-case lifts in practice: SGP (follow-on offering bookbuilt at ₱12.00, below the lower threshold derived from the last traded price before its 31 May 2021 suspension) — only the lower threshold lifted for the 10 Nov 2021 listing date under Art. VII §6(c) [^pse-cn-2021-0055-lift-lower-static-threshold-sgp:1]; KEEPR (₱1.50 offer vs last price before 8 Jul 2021 suspension; lifted for 19 Nov 2021) [^pse-cn-2021-0057-keepr-lower-static-threshold-lift:1]; PHR — static threshold lifted simultaneously with lifting of its suspension on Thu 5 Nov 2020 [^pse-tpa-2020-0052-phr-static-threshold-lift:1].
- **[P]** Listing by way of introduction: "The trading band … shall be lifted on the listing date in order to allow market forces to determine the price … After the listing date, the trading band shall be reinstated" (CLDR Art. III Part G §6) [^pse-listing-disclosure-rules:87].
- **[P]** Tick grid used to round prices (RTR Art. IV §8; unchanged until the NTE): 0.0001–0.0099→0.0001; 0.01–0.049→0.001; 0.05–0.249→0.001; 0.25–0.495→0.005; 0.50–4.99→0.01; 5–9.99→0.01; 10–19.98→0.02; 20–49.95→0.05; 50–99.95→0.05; 100–199.9→0.1; 200–499.8→0.2; 500–999.5→0.5; 1,000–1,999→1; 2,000–4,998→2; ≥5,000→5 [^pse-revised-trading-rules:21]; the NTE will replace this with a one-share lot and a streamlined tick table [^pse-nte-user-group-2026-01-15:9][^pse-nte-user-group-2026-01-15:10].
- **[S]** SuperCity Realty (SRDC) rose from ₱1.20 (18 Dec 2025) to ₱45.95 (7 Jan 2026), "over 3,700%" in nine trading days before a CMIC-requested halt on 8 Jan 2026 ([^insiderph-2026-01-08-srdc-halt][^bw-2026-01-09-srdc-resume]).
- **[S]** New-listing evidence: Medilines (MEDIC) IPO'd on 7 Dec 2021 at ₱2.30 and "tanked 30% on its listing day" ([^philstar-2021-12-07-medilines-debut]) — consistent with the −30% floor being measured from the offer price; PNB Holdings (LTL), a **listing by way of introduction** at ₱1.20 on Fri 25 Sep 2026: a trader quoted by BusinessWorld said it "opened weak at P0.75, swung between P0.70 and P1.24, and closed unchanged at its P1.20 listing price" on about 952.8 million shares (~₱1B) — an open 37.5% below the listing price, i.e. outside the −30% band, which is exactly what the lifted band on a listing-by-introduction date (CLDR Art. III Part G §6) permits ([^bw-2026-10-04-pnbh-debut]).
- **[S]** Resumption after a long suspension — band lifted for one day: Island Information & Technology (IS) resumed on Mon 7 Jul 2025 after a 1,572-day suspension (since 18 Mar 2021, for unfiled 2020–2023 annual and quarterly reports; last trade 17 Mar 2021 at ₱0.144); PSE announced the lifting of its static threshold for the resumption day, after which "+50%/−30%" bands re-attach to that day's close ([^philstar-2025-07-07-island-it-resumption]). Dominion Holdings (DHI), suspended 27 Jan 2020, resumed 20 Aug 2024 ([^philstar-2024-08-22-dominion-resumption]). By contrast, when a suspension lasts less than a year the normal band applies: Villar Land (suspended May 2025, resumed mid-Nov 2025) fell from ₱1,608 to ₱1,126 (14 Nov), ₱790 (17 Nov; the same article later quotes ₱789) and ₱552.20 as printed (18 Nov; the article's own "29.97%" decline from ₱789 implies ₱552.50) — three consecutive sessions of ≈−30% ([^philstar-2025-11-18-vll-plunge]).
- **[P]** PSE's investor FAQ (undated, stale) still describes a 50% ceiling *and* floor, "automatically frozen … unless there is an official announcement from the listed company or the proper government agency" ([^pse-web-investing-at-pse]) — contradicted for the floor by CN-2020-0028.
- **[P]** Block sales sit outside the continuous band: regular block sale ≥₱20M, price within ±5% of the LACP; special block sale ≥₱50M (IG XVIII, 2010 values) [^pse-implementing-guidelines-trading-rules:23][^pse-implementing-guidelines-trading-rules:24]; the NTE "Negotiated Trade" will execute within ±5% of full-day VWAP, 15 minutes after run-off, one-firm only [^pse-nte-broker-forum-2026-07-09:8].

### Inferences
- **[I]** Ceiling/floor are snapped to the tick grid *inward* (ceiling rounded down, floor rounded up, so the band is never exceeded): nine consecutive +50% steps from ₱1.20 with each ceiling rounded *down* to the applicable tick (1.80, 2.70, 4.05, 6.07, 9.10, 13.64, 20.45, 30.65, 45.95) reproduce SRDC's ₱45.95 exactly, whereas rounding to nearest would give about ₱46.1; and Villar Land's first post-resumption close of ₱1,126 from ₱1,608 equals 0.7 × 1,608 = 1,125.6 rounded *up* to the ₱1 tick; a third data point is the 18 Nov close — the report's "29.97%" decline from ₱789 implies ₱552.50, which is exactly 0.7 × 789 = 552.3 rounded up to the ₱0.50 tick used at that price (the article prints ₱552.20, probably a typo) ([^philstar-2025-11-18-vll-plunge]). Together with the nine-trading-day count (Dec 24–25, 30–31 and Jan 1 were non-trading days per [^pse-cn-2025-0043-non-trading-days:1]) this suggests SRDC closed at its ceiling every day — consistent with a +50% daily band compounding until a CMIC intervention (rule trigger: a price that "exceeds or closes at or near the ceiling or floor price based on the approved price trading band", CMIC Art. XI-A §5(a), see §4) [^pse-cmic-rules:113]. A further data point, consistent with the floor rule but not discriminating between rounding conventions: the companion liquidity note (10_empirical_liquidity.md §6, from PSE daily quotation reports) records Asiabest (ABG) closing on 30 Sep 2026 at ₱42.60 with no bid, exactly −30.0% from a ₱60.85 prior close (0.7 × 60.85 = 42.595, i.e. ₱42.60 on the ₱0.05 tick); the 30 Sep report itself shows open 60.00, high 60.85, low and close 42.60 on 545,270 shares [^pse-eod-daily-quotation-2026-09-30:3].
- **[I]** On a long-only unwind the −30% floor compounds as 0.7ⁿ (−51% after two floor days, −66% after three) — liquidation of a large position in a gap-down stock can take several sessions (Villar Land's three floor sessions in Nov 2025 are the live example), and market-wide the circuit breaker (§3) interacts with it. The printed ₱552.20 is off the 2010 tick grid (₱0.50 steps at that price), but the implied ₱552.50 is on it; the three Villar Land prints are therefore consistent with the 2010 tick table still applying in Nov 2025 (weak evidence — a finer grid would fit too).
- **[I]** Because the offer price must act as the "previous close" of an IPO's first day, the system presumably seeds the Reference Price with the offer price (Medilines' −30% from ₱2.30 supports this) — but I found no rule text saying so (RTR Art. IV §6 lists only (a)–(c)). For listings by introduction the first day is effectively unbanded (PNB Holdings), then the ±band is re-seeded from that day's close.

### Gaps
- Formula/procedure for computing the ACP after dividends, stock splits, rights (not in RTR, IG, CLDR; PSE publishes results, not the algorithm).
- IPO-day (and follow-on listing-day) price-limit treatment: no rule text found beyond IG VI.5 and Art. VII §6.
- No ETF-, REIT- or dollar-denominated-security-specific price-limit provisions found (RTR applies to "Securities"; static band exempts only warrants). The ETF/DDS rule PDFs were text-searched without hits, which may reflect scanned images rather than absence.
- No special rule for sub-₱1 ("penny") stocks other than the percentage band and tick grid.
- Whether the post-2020 lower band changes the "static threshold adjusted to 60%" step (see §2) is undocumented.
- NTE (go-live 23 Nov 2026): no document I found states whether static/dynamic thresholds are unchanged.

### Execution implications
- Build the corridor as `ceil = round_down_to_tick(1.5 × RefPx)`, `floor = round_up_to_tick(0.7 × RefPx)` (inward snapping, inferred from SRDC/Villar Land prints; in the legacy ITCH feed the engine's own values are the High Collar / Low Collar fields of message [k] — see §2 — so read those rather than recompute) with RefPx = previous close or ACP, using the tick of the *resulting* price range; re-pull RefPx every morning (corporate-action days, long suspensions) — the UBP episode shows PSE itself can mis-set it.
- Never send a limit outside the corridor: it freezes the stock for everyone (§2) and burns goodwill with the broker.
- Treat the asymmetric floor as a liquidity cliff: model exits as multi-day on gap-down names; for shorts the −30% limit caps single-day cover profit.
- Expect cancel-and-replace on ex-dates/corporate-action days (exchange purges orders) — GTC/GTD logic must re-arm.
- Watch circulars for lifted lower thresholds (follow-on offerings after long suspensions); in those sessions price discovery is unbounded on the downside and ceiling/floor logic must be switched off.

---

## 2. Dynamic thresholds, the "freeze" mechanism, reservation and any volatility interruptions

### Takeaway
Each security carries a Dynamic Threshold of 10%, 15% or 20% (by trade count over the last six months) measured against the **last traded price**. An order whose price breaches the static or dynamic threshold **freezes the security**: nobody can post, modify or cancel; PSE Market Control must act "immediately or no later than five (5) minutes", usually by phoning the TP to confirm; breaching orders are accepted or rejected, with several auto-accept and auto-reject cases. I found no stock-level volatility interruption/auction beyond this.

### Cited findings
- **[P]** Definition: DT is "the maximum allowable price difference between an update in the Last Traded Price (LTP) … and its preceding LTP that is equal to a percentage set by the Exchange"; clusters: **A** traded ≤20 times in past six months → 20%; **B** 21–500 times → 15%; **C** >500 times → 10%; new listings → 20% [^pse-implementing-guidelines-trading-rules:10][^pse-implementing-guidelines-trading-rules:11].
- **[P]** Review cadence: semi-annual, "every second trading week of January and July" on prior-six-month data; a Cluster A security traded 200 times between reviews moves to B's threshold, a Cluster B security traded 1,000 times to C's; PSE may reclassify earlier; results published before effectivity [^pse-implementing-guidelines-trading-rules:11]. Actual circulars: TPA-2026-0002 dated 19 Jan 2026, effective **Mon 2 Feb 2026** (data Jul–Dec 2025); TPA-2026-0036 dated 3 Aug 2026, effective **Fri 7 Aug 2026** (data Jan–Jun 2026) — same 20/15/10 table [^pse-tpa-2026-0002-dynamic-threshold-review:1][^pse-tpa-2026-0036-dynamic-threshold-review:1]. The security→cluster list is an **image** table (Groups A, B, C) on page 2 of the circular [^pse-tpa-2026-0036-dynamic-threshold-review:2].
- **[P]** Freeze rule (RTR Art. VII §1): "Whenever an Order will result in a breach of the Trading Threshold of a Security within a Trading Day, the trading of the Security will be frozen"; orders cannot be posted, modified or cancelled in a frozen security; if an order is partially matched "only the portion … that will result to a breach … will be frozen". If the **static** threshold is breached, the Exchange accepts the order if the price is "within the allowable percentage price difference under the Implementing Guidelines", otherwise rejects it; where accepted, **"the Exchange will adjust the Static Threshold to sixty percent (60%). All Orders breaching the 60% Static Threshold will be rejected."** If the **dynamic** threshold is breached, accept if within the allowable difference, otherwise reject [^pse-revised-trading-rules:33].
- **[P]** IG XIX mechanics: Market Control acts "immediately or no later than five (5) minutes from the time of freezing"; (b) for a partially matched limit order, intermediate trades stand and the remainder is auto-accepted if its price differs from the last intermediate trade by no more than the DT, otherwise Market Control contacts the TP to confirm validity; (c) a limit order priced **at the best bid/offer** but beyond the DT is auto-accepted; (d) a **cross transaction** breaching the DT is auto-accepted; (e) any order breaching the DT **within five minutes before Market Pre-Close is auto-rejected**; (f) if the TP cannot be reached within five minutes the order is auto-rejected and the security "thawed"; (4) breaching the DT in the same security more than three times in a day through different orders by the same TP "shall be deemed a minor violation" [^pse-implementing-guidelines-trading-rules:25][^pse-implementing-guidelines-trading-rules:26]. Order status "Frozen" = order "has caused the freezing of the Security and is waiting for Market Control action"; "Market Eliminated" = cancelled by Market Control or automatically by market rules [^pse-implementing-guidelines-trading-rules:17].
- **[P]** Reservation of a security is triggered by (i) a market-on-opening order with no indicative opening price, (ii) an unfilled market order at open, (iii) an indicative opening price that breaches the static threshold; it is also imposed manually before lifting a suspension; during reservation orders other than crosses can still be posted/modified/cancelled [^pse-revised-trading-rules:33][^pse-implementing-guidelines-trading-rules:26].
- **[P]** How the controls appear in the legacy market-data feed (X-stream ITCH spec v2.3, © 2014; the NTE replaces it at the cut-over, so re-verify after 23 Nov 2026): the per-orderbook Restrictions message [k] carries *Short Sell Eligible*, a **High Collar** and **Low Collar** ("Maximum [Minimum] allowed price via static limit"; 2147483647 means no limit) and **CB Limit Up % / Down %** ("Circuit breaker maximum movement allowed up [down] as a percentage from the Last Traded Price (dynamic limit)"; 0 means no limit; a decimals field scales both) [^pse-itch-equities-feed-spec-v2-3:12][^pse-itch-equities-feed-spec-v2-3:13]. The Trading Action message [H] sets each orderbook's state — T trading or V suspended — with a reason: N normal, S "Suspended by market control", F "Frozen due to circuit breaker (dynamic limit)", H "Halted (intraday auction)"; intraday a suspension is V+S (lifted T+N), a freeze V+F (thawed T+N) and a halt T+H (lifted T+N) [^pse-itch-equities-feed-spec-v2-3:13][^pse-itch-equities-feed-spec-v2-3:14]. "Circuit breaker" in these fields means the stock-level dynamic limit, not the PSEi breaker; the system-event codes (daily phases and the lunch break) include no market-wide halt code [^pse-itch-equities-feed-spec-v2-3:10].
- **[P]** Odd-lot market has no dynamic threshold and freezes in the normal market do not propagate to it (and vice versa) [^pse-implementing-guidelines-trading-rules:20][^pse-revised-trading-rules:26]; the NTE removes the odd-lot market (lot size = 1) [^pse-nte-faq-2026-08:1].
- **[P]** DMA firms must have written procedures for "handling of DMA Orders breaching the trading thresholds and other circumstances which may require confirmation" (DMA Rules §4(c)(ii)(3)) [^pse-memo-sec-approved-dma-rules-2013-11-26:6]; the DMA price-limit filter is "percentage away from the last traded price" or "last adjusted closing price" or ticks (§11(b)(iii)) [^pse-memo-sec-approved-dma-rules-2013-11-26:10].
- **[P]** Session structure that bounds auctions: pre-open 9:00 (enter/modify/cancel; algorithmic opening price), no-cancel from 9:15, open 9:30; pre-close 14:45, no-cancel 14:48, run-off/trading-at-last 14:50 (orders only at the closing price; "in cases where prices of posted Orders in the Order book are better than the Closing Price, no Orders will be accepted"), Closing VWAP 15:00–15:15 [^pse-approved-rules-vwap-trading-2024:3][^pse-approved-rules-vwap-trading-2024:6][^pse-revised-trading-rules:27]. Opening/closing price algorithm: max matched volume → min unmatched → market pressure → closest to Reference Price (opening) or LTP (closing) [^pse-revised-trading-rules:23][^pse-revised-trading-rules:24]. Short-sale orders are not accepted in pre-open/pre-close [^pse-short-selling-guidelines-2023-10:2].
- **[P]** Planned change: the NTE (Nasdaq) will let run-off orders be "entered, modified, and executed only at the Closing Price" (current text allows only execution at the closing price) and, on day 1, supports **limit orders only** [^pse-nte-user-group-2026-01-15:11][^pse-nte-faq-2026-08:1].
- **[I]** The reject path surfaces in FIX as ExecType=Rejected; the 2015 X-stream FIX spec defines OrdRejReason 5 (unknown order), 6 (duplicate) and 99 ("Other — refer to Text (58)"), so threshold/phase rejects will arrive as 99 + free text [^pse-fix-specification-v2-5:52] (spec predates the NTE; the Eqlipse FIX spec was released July 2026 and is not archived here).

### Inferences
- **[I]** The DT anchor is LTP, not the touch: a deep passive limit resting more than DT% from the last trade can itself trip a freeze, whereas orders at the BBO and crosses are exempt — so staged/pegged placement is safer than parking far orders.
- **[I]** A freeze of up to ~5 minutes locks *all* participants' order entry/cancel in that stock; risk systems that rely on cancel-on-disconnect or kill-switch cancels will not work during it.
- **[I]** There is no volatility auction: the stock-specific brakes are (i) the band + freeze, (ii) CMIC restriction/halt/suspension (§4), (iii) disclosure halts (§4). Market-wide brake is the PSEi circuit breaker (§3).
- **[I]** The feed states line up with the rulebook states: V+F is the freeze (no posting, modifying or cancelling), V+S the suspension (orders purged), and T+H the Trading Halt or reservation (orders may be entered, modified and cancelled but nothing matches — what the spec labels an "intraday auction" state); the spec does not say what uncrossing, if any, runs when T+H is lifted. The collar and CB-limit fields let a client read the engine's own corridor instead of re-deriving it, so the §1 snapping rule becomes a cross-check; whether the NTE feed carries equivalents is not documented in what I found.

### Gaps
- The numerical "allowable percentage price difference" for **static** breaches is not in the IG (IG XIX details only the DT cases); whether the 60% step still applies after the 2020 change is undocumented.
- Whether the live PSETrade/PSETradeX stack *rejects locally before sending* vs. freezing the stock: not documented.
- NTE behaviour of thresholds/freeze; cluster list is image-only (no machine-readable feed found).

### Execution implications
- Clip every limit price to the **tighter of** static corridor and DT corridor (±10% for Cluster C around LTP); for sweeps send marketable limits at/inside the BBO and walk them.
- Refresh clusters each Feb/Aug (and watch for intra-period reclassification); preferred-share lines and thin names sit in A/B at 20%/15%.
- Keep per-TP DT-breach count ≤3/day; do not fire breaching orders in the final five minutes before pre-close (auto-reject).
- During a freeze assume no cancels: size passive orders so that a 5-minute inability to cancel is tolerable.
- Add NTE regression tests: lot size 1, limit-only day 1, run-off order entry semantics.

---

## 3. Market-wide circuit breakers, the COVID-19 closure and other market-wide halts

### Takeaway
The PSEi circuit breaker has three levels since **4 May 2020** (−10%/−15%/−20% → 15/30/60-minute market halt, once per level per day). The old single-level breaker (adopted Sept 2008) fired only four times (27 Oct 2008; 12, 13, 19 Mar 2020); I found no report of any trigger since. The exchange closed for two trading days (17–18 Mar 2020) for the Luzon lockdown. System-failure halts are a separate rule (Art. VIII §2) rewritten on 20 Aug 2025; since 2010 there have been repeated outage halts/cancellations (2014, 2015 ×2, 2016, 2022, 2024, 2025 delayed opens).

### Cited findings
- **[P]** Current rule (CN-2020-0044, 29 Apr 2020; effective Mon 4 May 2020; SEC approval 20 Mar 2020): RTR Art. VIII §1 — trading halts if the percentage decrease in PSEi from its previous close reaches an IG level; duration varies by level; "implemented only once in a Trading Day for each level"; "will not be triggered at a specific time prior to the pre-close". new IG section "Circuit Breaker" (numbered XXI in the circular; the 2025 circular numbers *Technical Contingencies* as Part XXI, so the live IG part numbers are uncertain): Level 1 ≥10% → 15 min; Level 2 ≥15% → 30 min; Level 3 ≥20% → 60 min; a higher-level breach imposes the higher level's duration and the lower level then never triggers that day; "In the event that any of the Circuit Breaker levels is breached before Market Recess, market shall be halted for the corresponding halt duration period, which shall include the Market Recess period" [^pse-cn-2020-0044:1][^pse-cn-2020-0044:2][^pse-cn-2020-0044:3][^pse-cn-2020-0044:4].
- **[P]** Cut-offs stated in the circular for a pre-close at 3:15 pm: L1 only up to 2:55 pm, L2 up to 2:40 pm, L3 up to 2:10 pm (pre-close minus 20/35/65 min, i.e. the 15/30/60-minute halt plus five minutes); for the then-shortened day (pre-close 12:45): 12:25 / 12:10 / 11:40 [^pse-cn-2020-0044:2][^pse-cn-2020-0044:4]. The PSE press release gives the rationale — a breaker "will not be triggered if doing so will result in having less than five (5) minutes of continuous trading prior to the pre-close" — and says that the old breaker "tripped four times … on October 27, 2008 and on March 12, 13, and 19, 2020" ([^pse-web-press-2020-04-30-circuit-breaker]).
- **[P]** What it replaced (2010 RTR Art. VIII §1): halt if PSEi falls ≥10% vs previous close; trading "will resume within fifteen (15) minutes"; once per day; no trigger within 30 minutes of market close [^pse-revised-trading-rules:35]. CN-2020-0044 describes it as "an offshoot of the 2008 global financial crisis" [^pse-cn-2020-0044:1].
- **[S]** 12 Mar 2020: PSEi −9.71% at close (5,736.27); intraday low 5,697.13 (−10.33%) triggered a 15-minute halt ([^philstar-2020-03-12-circuit-breaker]). 19 Mar 2020 (first session after reopening): PSEi −13.34% to 4,623.42; breaker tripped at the open when the index was down 12.4%; intraday low 4,039.15 (−24.29%) — the single-level breaker could not fire again ([^bw-2020-03-19-shares-plummet]). "The circuit breaker was triggered three times in four trading days", which prompted the multi-level design ([^bw-2020-05-01-three-level-cb]).
- **[I]** Data check on whether any level has been reached since 4 May 2020: the companion liquidity note (10_empirical_liquidity.md §6, own calculation from PSE Weekly Report daily closes) finds the worst PSEi close-to-close fall after that date was −4.97% (9 Mar 2026; next −4.82% on 15 Jun 2020 and −4.30% on 7 Apr 2025), with annual worst days of −2.6% to −4.4% in 2021–2025, and a mean intraday range of about 1.0–1.4% — far from the −10% Level 1 trigger, although intraday lows were not checked individually.
- **[P]** COVID closure: CN-2020-0017 (15 Mar) announced shortened hours from 16 Mar [^pse-cn-2020-0017:1]; CN-2020-0021 (16 Mar): after the President placed Luzon under enhanced community quarantine, "no trading at [PSE] and no clearing and settlement at [SCCP] starting tomorrow, March 17, 2020 until further notice" [^pse-cn-2020-0021:1]; CN-2020-0025 (17 Mar): trading resumes **Thu 19 Mar 2020** with pre-open 9:00, open 9:30, pre-close 12:45, run-off 12:50, close 1:00 pm, trading floor closed, remote trading from offsite locations [^pse-cn-2020-0025-resumption-of-trading:1]. **[S]** International press framed it as the first national market shutdown over COVID-19 (headline only: "Philippines first country to suspend all financial markets as coronavirus spreads") ([^arabnews-2020-03-16-first-to-suspend]).
- **[P]** Hours since: shortened hours extended to 30 Apr, 15 May and under MECQ [^pse-cn-2020-0035:1][^pse-cn-2020-0042:1][^pse-cn-2020-0046:1]; back from Mon 6 Dec 2021 to what PSE called its "pre-pandemic full day-5-hour trading schedule" (open 9:30, recess 12:00, resume 13:00, pre-close 14:45, run-off 14:50, close 15:00) [^pse-cn-2021-0059:1] — but the schedule actually in force from 2 Jan 2012 to March 2020 resumed at 13:30 and closed at 15:30 (pre-close 15:17, from 4 Nov 2013 15:15) [^pse-memo-new-trading-hours-2011:1][^pse-memo-extended-pre-close-implementation-2013:1], so the afternoon moved 30 minutes earlier; Omicron shortening from 14 Jan 2022 (pre-close 12:45; announced to 31 Jan, evidently extended because the next circular restores the full day only on 1 Mar) [^pse-cn-2022-0004:1]; full-day schedule again from Tue 1 Mar 2022 [^pse-cn-2022-0009-trading-schedule-mar-2022:1]; Closing VWAP session 15:00–15:15 added with the VWAP rules (SEC-approved 1 Feb 2024; live 1 Mar 2024) [^pse-approved-rules-vwap-trading-2024:3][^pse-cn-2024-0012-vwap-go-live:1].
- **[P]** System-failure market halt — history of Art. VIII §2: 2010 base: halt if "at least one-third (1/3) of the Trading Participant-users cannot access the Trading System" [^pse-revised-trading-rules:35]; Jan 2012 amendments (SEC letter 25 Oct 2011): halts ≥30 minutes → extend hours, but "trading extension will no longer be applicable for whole day trading, except for … completing the remaining market phases"; if a halt lasts more than two hours or 15 minutes beyond the run-off, the Exchange has "sole discretion to suspend or cancel the trading for the day" [^pse-tpa-2011-0110-amended-revised-trading-rules:6][^pse-tpa-2011-0124-amended-implementing-guidelines:4][^pse-tpa-2011-0124-amended-implementing-guidelines:6]. The amended IG Part XX adds that the Exchange must tell TPs of the lifting of a market halt at least five minutes before it happens, and compresses the remaining phases on resumption (pre-close and trading-at-last cut to 2 and 5 minutes when less than ten minutes of continuous trading remain; a ten-minute extension if a halt that began in continuous trading ends during trading-at-last, five minutes if it began in pre-close); its clock times are written for the 15:30 close and I found no restatement for the 15:00/15:15 schedules [^pse-tpa-2011-0124-amended-implementing-guidelines:4][^pse-tpa-2011-0124-amended-implementing-guidelines:5][^pse-tpa-2011-0124-amended-implementing-guidelines:6]. The 2010 base IG also halts the market while the Customer Common Gateway (the FEOMS order-routing gateway) is down and for ten minutes after it is fixed; during that halt Market Control acts on active orders only on a CCG client's request and in line with the cancellation rules (the 2012 amendment reprints only part of Part XX, so I cannot say whether this item survived) [^pse-implementing-guidelines-trading-rules:30]. PSE's 2022 consultation proposed the new test because "around 10 brokers (out of a total of 125 active TPs) … account for more than 50% of total trades" and the 1/3 headcount is "not representative" [^pse-cn-2022-0020-market-halt-consultation:4]; final text (CN-2025-0037, 20 Aug 2025, effective immediately): PSE may halt the market if TPs "accounting for more than fifty percent (50%) of the average daily trading value (exclusive of block sales) as of the end of the six calendar month period preceding the date of determination cannot trade, directly or through their Correspondent Trading Participant, due solely to trading system problems attributable to Exchange system issues … natural disasters or extraordinary circumstances"; every TP must designate a Correspondent TP (two months to comply; different FEOMS vendor or separate silo/FIX gateway; done-through account code; no aggregation) [^pse-cn-2025-0037:1][^pse-cn-2025-0037:2][^pse-cn-2025-0037:3][^pse-cn-2025-0037:6][^pse-cn-2025-0037:7].
- **[P]** Natural-disaster guidelines (CN-2025-0037 Annex B): PSE may halt, suspend or cancel a trading day when an emergency prevents staff entering the premises, may disrupt TPs accounting for >50% of ADTV, or other emergencies, and must "immediately notify" the SEC; if PAGASA's tropical-cyclone wind signal in NCR is 1–2 → regular trading, **3–5 → no trading**; if downgraded to 1–2 by 6:00 am the next trading day, no cancellation [^pse-cn-2025-0037:4][^pse-cn-2025-0037:5] ([S] trade-press headline: "Storm Signal No. 3 now enough to shut down PSE trading", [^insiderph-2025-08-20-storm-signal-3], headline only). Base RTR: trading day = every day except weekends, holidays, days BSP is closed, and other days declared by SEC/PSE President [^pse-tpa-2011-0110-amended-revised-trading-rules:3]; absent a declaration "trading shall proceed as usual" [^pse-memo-trading-days-suspensions-guidelines-2012:1]. President may suspend trading in the Market for the rest of the day (trades/orders deemed valid) or cancel the day within one hour after pre-open (trades and orders purged) [^pse-revised-trading-rules:36].
- **[P]** Market-wide non-trading days declared by circular include: 19 Aug 2013, 8 Dec 2014, 12 Sep 2017, 16 Oct 2017 (suspension of banking/clearing or PhilPaSS operations) [^pse-cn-2013-0033-trading-suspension-2013:1][^pse-cn-2014-0059-trading-suspension-2014-12-08:1][^pse-cn-2017-0050-trading-suspension-2017-09-12:1][^pse-cn-2017-0059-trading-suspension-2017-10-16:1]; 13 Jan 2020 (Taal ash emission) [^pse-cn-2020-0002-trading-suspension-2020-01-13:1]; 26 Sep 2022 [^pse-cn-2022-0035-trading-suspension-2022-09-26:1]; 24 Jul 2024 (inclement weather/floods) [^pse-cn-2024-0038-trading-suspension-2024-07-24:1].
- **[P]** Outage episodes: 20 Nov 2014 halt at 1:46 pm, resumed 2:30 pm, close at 3:30 as scheduled [^pse-cn-2014-0057-trading-halt-2014-11-20:1]; 24 Aug 2015 halt 2:05:26 pm (lifted 2:50 pm) and 25 Aug 2015 halt 10:02:22 am (resumed 2:55 pm), cause "market data transmission" overload on PSE front-end terminals, PSE stated the halt "was not imposed to stem the market's drop" [^pse-cn-2015-0110-trading-halt-2015-08-24:1][^pse-cn-2015-0112-trading-halt-2015-08-25:1][^pse-cn-2015-0118-statement-trading-halts-2015:1][^pse-cn-2015-0118-statement-trading-halts-2015:2]; 8 Apr 2016 halt 10:29:18 am, third-party communication line disconnection, resumed 11:10 am [^pse-cn-2016-0020-trading-halt-2016-04-08:1][^pse-cn-2016-0023-statement-trading-halt-2016:1]; 4 Jun 2019 halt 11:45 am for a fire drill, resumed 1:30 pm [^pse-cn-2019-0031-trading-halt-fire-drill:1]; **4 Jan 2022**: opening delayed, "among the 125 trading participants … 43 are unable to connect" (≥1/3), then the day was **cancelled** — connection failure between the Nasdaq engine and the Flextrade front end [^pse-cn-2022-0001-delay-market-opening:1][^pse-cn-2022-0002-cancellation-of-trading-2022-01-04:1]; **3 Jan 2024** technical issue halted trading at 9:32 am, resumed 11:56 am, afternoon "from 1:00 to 3:00 p.m." as scheduled; PSE and "its third party front-end system provider" investigating (root cause not stated) [^pse-cn-2024-0003-update-market-halt:1][^pse-cn-2024-0002:1]; 9 Dec 2024 pre-open/no-cancel/open pushed to 9:40/9:50/9:55 with no reason given ("the remaining market phases will still be followed") [^pse-cn-2024-0061-adjusted-schedule-2024-12-09:1]; **24 Mar 2025** open delayed to 11:10 am for a "system connectivity issue" [^pse-cn-2025-0014:1][^pse-cn-2025-0015-adjusted-schedule-2025-03-24:1]. [S] PSEi closed −1.19% at 6,192.02 that day; analysts warned about investor confidence ([^wealthinsights-2025-03-24-tech-glitches]).

### Inferences
- **[I]** With today's 14:45 pre-close the breaker cut-offs scale to ≈14:25 (L1), 14:10 (L2), 13:40 (L3) (pre-close −20/−35/−65 min per the circular's own examples); the circular's literal clock times (written for a 3:15 pm pre-close, the 2012–2020 schedule) are legacy. Because a halt "includes the Market Recess", a breach at 11:50 would leave only 10 minutes of 15 and effectively resume at 13:00 (my reading).
- **[I]** The three-level design fixes the 19 Mar 2020 problem (index −24% intraday after a single 15-minute pause), but no trigger has been reported since 2020, so the live system's behaviour at re-open (auction vs continuous) is untested in public records.
- **[I]** Outage risk is the dominant "halt" risk: eight documented system halts, cancellations or late opens in 2014–2025 (20 Nov 2014; 24 and 25 Aug 2015; 8 Apr 2016; 4 Jan 2022; 3 Jan 2024; 9 Dec 2024 — late open, cause not stated in the circular; 24 Mar 2025) versus no circuit-breaker trip found since 2020. The 4 Jun 2019 fire-drill halt is excluded.

### Gaps
- Rules on order treatment at a circuit-breaker halt (retained vs purged; whether pre-open-style auction at re-open) — not found; Art. VII (single-stock halts) preserves orders, Art. VIII §3–4 (market suspension/cancellation) states trades/orders valid/purged, but nothing specific to breaker halts.
- How a PSEi breaker halt is broadcast: the legacy ITCH spec has per-orderbook states and phase events but no market-wide halt code [^pse-itch-equities-feed-spec-v2-3:10][^pse-itch-equities-feed-spec-v2-3:14].
- Whether any breaker tripped after 19 Mar 2020 — I found none in the news or circulars, and the daily-close data above make a trigger very unlikely, but intraday lows were not checked.
- Root causes of 3 Jan 2024, 9 Dec 2024 and 24 Mar 2025 events not published.
- NTE failover/halt procedures.

### Execution implications
- Hard-code the 10/15/20% PSEi triggers and scaled cut-offs; during a halt, queue state (orders retained?) is **unknown** — design for both.
- Detect a breaker halt defensively, because the 2014 feed spec has no market-wide halt event: combine the index drawdown against the prior close (−10/−15/−20%) with simultaneous halt or freeze states across constituents **[I]**.
- Outage playbook: day cancelled (2022) vs halt-and-resume (2024) vs late open (2025); do not rely on the closing auction; expect the "remaining market phases" to be compressed. For a system-failure halt PSE must announce the lifting at least five minutes ahead (IG XX.2) — use that window to re-validate working orders; no such notice is specified for a breaker halt.
- Maintain a second broker (correspondent TP logic) — the 2025 rule makes correspondents mandatory for TPs, but a buy-side firm still needs its own FIX/DMA fallback.
- Typhoon signal ≥3 in NCR by 6:00 am ⇒ assume no trading; also BSP/PhilPaSS closures suspend trading.

---

## 4. Single-stock halts and suspensions

### Takeaway
Single-stock stoppages come from (i) the disclosure rules (halt around material news; clarification requests), (ii) CMIC's surveillance power (restrict/halt/suspend on unusual price/volume), (iii) compliance failures (late 17-A/17-Q, unpaid fines, no stock transfer agent, MPO breach), (iv) corporate-action/market-structure events, and (v) suspension of the *broker* (TP) itself. A **halt** (≤1 trading day) leaves order entry/cancel open; a **suspension** blocks all order activity and purges posted orders. Typical resumption is at 10:30 am after a 50-minute suspension + 10-minute reservation.

### Cited findings
- **[P]** Definitions: Trading Halt = "temporary stoppage … not lasting longer than one Trading Day"; orders other than crosses can be posted/modified/cancelled during a halt; derivative securities (warrants, PDRs) are halted too. Suspension: orders cannot be posted/modified/cancelled; no TP may "directly or indirectly" deal; "all posted Orders for such Security shall be purged upon suspension" (the RTR itself is softer: orders "may be purged at the end of a Trading Day, as set out in the Implementing Guidelines", so the IG's purge-on-suspension controls the timing — my reading **[I]**); PSE executes the action and notifies the market simultaneously and announces the resumption time [^pse-implementing-guidelines-trading-rules:26][^pse-implementing-guidelines-trading-rules:27][^pse-revised-trading-rules:34]; RTR Art. VII §3–5: Exchange **or the SEC** may halt/suspend; lifted "upon compliance by the Issuer" [^pse-revised-trading-rules:33][^pse-revised-trading-rules:34].
- **[P]** Lifting matrix (IG, Security Halt and Suspension Matrix): Case 1 — halted at start/middle of day with no compliance at EOD → Day 2 suspended; if the issuer complies before 4 pm, trading resumes in the market pre-open; if after 4 pm, "Trading will be suspended for fifty (50) minutes, and will be reserved ten (10) minutes thereafter". Case 2 — compliance within the day → resumption. Case 3 — voluntary or Exchange-initiated suspension, same 4 pm split on Day 2 [^pse-implementing-guidelines-trading-rules:28].
- **[P]** Disclosure halt (CLDR Art. VII §4.1): issuers must disclose material information "within ten (10) minutes from the receipt of such information or the happening … prior to its release to the news media"; if it occurs in trading hours the issuer "must request a halt" (also if after hours and disclosure cannot be made before pre-open); "the trading halt shall be lifted one (1) hour after the information has been disseminated … If the information is disseminated one (1) hour or less prior to the close of market, the trading halt shall be lifted on the subsequent Trading Day"; soft information and legally barred disclosures are exempt [^pse-listing-disclosure-rules:139][^pse-listing-disclosure-rules:140]. PSE can impose it itself: on Mon 19 Jan 2026 PSE imposed a **one-hour halt in MRC Allied (9:30–10:30)** "in view of the materiality" of a 16 Jan 2026 board approval of a 315,000,000-share private placement at ₱1.00 per share (₱315M) to two individuals [^pse-cn-2026-0004-2-emergency-disclosures-trading-halt:1][^pse-cn-2026-0004-2-emergency-disclosures-trading-halt:2].
- **[P]** Clarification of news/rumours (Art. VII §4.5): on a PSE request the issuer must confirm or deny before the next pre-open (or, if asked after hours, before the next pre-open); "The Exchange shall impose a trading halt … if it fails to confirm or deny"; the halt "shall be lifted at 10:00 a.m. even in the absence of any reply"; reply required by 11:00 am or a ₱30,000 fine plus ₱10,000 per further 30 minutes [^pse-listing-disclosure-rules:145][^pse-listing-disclosure-rules:146]. Related rules: issuers must respond to PSE inquiries on unusual trading activity and, if the cause is unknown, disclose that no undisclosed development explains it (§15) [^pse-listing-disclosure-rules:149][^pse-listing-disclosure-rules:150]; unusual activity "gives rise to the presumption that there is insider trading or a rumor or report".
- **[P]** Not yet adopted (as far as the Jan 2025 compilation shows): the Nov 2022 consultation proposed making disclosure halts voluntary ("may request") with PSE able to impose them, deleting the hard-copy filing, and dropping the automatic halt in §4.5 in favour of penalties; the January 2025 text still has the old wording [^pse-cn-2022-0045-consultation-2022-part-ii:4][^pse-cn-2022-0045-consultation-2022-part-ii:30][^pse-cn-2022-0045-consultation-2022-part-ii:31][^pse-cn-2022-0045-consultation-2022-part-ii:32][^pse-listing-disclosure-rules:139][^pse-listing-disclosure-rules:145].
- **[P]** Substantial acquisitions/reverse takeovers (§5): where an acquired interest in an unlisted company is ≥10% of the issuer's book value, "the trading of the securities of the Issuer shall be suspended until the terms and conditions … are actually disclosed" [^pse-listing-disclosure-rules:146]; stock-transfer-agent termination without a replacement ≥10 trading days before effectivity → suspension until notice (§12) [^pse-listing-disclosure-rules:148].
- **[P]** CMIC surveillance halts (CMIC Rules Art. XI-A): CMIC "shall monitor daily the trading activity" and, with the PSE President's approval, may "issue restriction, halt or suspension orders against trading of a listed security, or against trading by a Trading Participant of a particular listed security upon breach of pre-established price and/or volume benchmarks or when CMIC deems it necessary" (§1–2); orders last until lifted, only after the information is adequate (§3); SEC is notified immediately if the market is open, else by 4:00 pm for next-day orders, with written notice by 11:00 am next day (§4); procedure (§5): upon detecting unusual activity "including instances when the price of a listed security exceeds or closes at or near the ceiling or floor price based on the approved price trading band", CMIC checks prior disclosure with the SEC/Disclosure Dept, directs the issuer (or TP) to file by **4:00 pm** a written statement confirming the existence/absence of undisclosed information; non-compliance → CMIC "may, but is not obliged to" halt; once the statement is circulated and posted the order is lifted "not earlier than one (1) hour" later [^pse-cmic-rules:112][^pse-cmic-rules:113].
- **[S]** Worked example (Jan 2026): CMIC told SuperCity Realty (SRDC) on 7 Jan to explain a surge from ₱1.20 to ₱45.95 over nine trading days; SRDC missed the deadline; PSE suspended trading at 9:00 am on Thu 8 Jan; SRDC filed a "not aware of any material information" statement late Thursday; trading resumed 10:30 am Fri 9 Jan [^bw-2026-01-09-srdc-resume][^insiderph-2026-01-08-srdc-halt]. Another example: the SEC asked PSE/CMIC for reports on the PLDT sell-off before its 19 Dec 2022 capex-overrun disclosure (stock −19.35% that day) [^philstar-2022-12-20-sec-pldt-inquiry].
- **[P]** Non-filing suspensions (CLDR Art. VII §17.2/§17.8): annual report (SEC Form 17-A) due 105 days after fiscal year-end, 17-Q due 45 days after quarter-end, extensions only on PSE's format (+15 calendar days for 17-A, +5 for 17-Q) [^pse-listing-disclosure-rules:150][^pse-listing-disclosure-rules:151]; for 17-A non-filing: basic fine plus daily fine for 15 calendar days, warning, then "automatic suspension of the trading of the company's shares for a maximum period of three (3) months", then delisting procedures; for 17-Q: 10 days of daily fines then suspension up to two months; unpaid fines also lead to suspension (3 months / 2 months) [^pse-listing-disclosure-rules:153][^pse-listing-disclosure-rules:154][^pse-listing-disclosure-rules:155]. Fine schedules: structured-report scale by total assets (₱5,000 basic + ₱500/day for <₱25M … ₱50,000 + ₱5,000/day for ≥₱1B; annual cap 10× basic); unstructured violations: Level 1 (reprimand, ₱50,000, ₱75,000, ₱100,000) and Level 2 (₱100,000 → ₱300,000 and discretion to suspend/delist; includes breaches of the blackout rule), plus ₱1,000/trading day until rectified; failure to pay within one month → suspension [^pse-listing-disclosure-rules:159][^pse-listing-disclosure-rules:160]. In practice the "maximum three months" is not a hard cap: Island IT stayed suspended 1,572 days (18 Mar 2021 → 7 Jul 2025) before curing its filings [^philstar-2025-07-07-island-it-resumption] **[S]**. Examples: Del Monte Pacific missed the extended 28 Aug 2025 17-A deadline, PSE warned on 9 Sep and suspended it that week (BusinessWorld says Tuesday 16 Sep) [^bw-2025-09-17-delmonte-suspended][^insiderph-2025-09-09-delmonte-warning]; Xurpas suspended 2 Jun 2026 for missing its 2025 annual and Q1-2026 reports, resumed Tue 21 Jul 2026 at 10:30 am [^insiderph-2026-07-20-xurpas-resumes]; 11 listed firms (six Villar-controlled) sanctioned for late Q2-2026 filings due by the extended 19 Aug deadline, penalties undisclosed in PSE's 20 Aug notice [^bilyonaryo-2026-08-23-villar-late-q2]; as of 24 Aug 2026 six of the seven Villar-group listed companies (~₱320B market value) had been suspended "for nearly three months" over overdue financial filings, with SSS and GSIS among the stuck holders ([^insiderph-2026-08-24-villar-frozen]) — the group had also been suspended in May 2025 for late annual reports: Vista Land and Vistamalls were reinstated in May–June 2025 after filing (headlines only: [^rappler-2025-05-19-vista-land-lifted], [^philstar-2025-06-05-vistamalls-lifted]) while Villar Land stayed suspended until mid-November 2025 ([^philstar-2025-11-18-vll-plunge]).
- **[P]** Minimum public ownership (MPO): the 11 Aug 2026 Amended MPO Rule (SEC MC No. 11 s. 2026; "take effect immediately") sets IPO public-float tiers (33% ≤₱500M; 25% >₱500M–₱1B with ₱165M minimum offer; 20% >₱1B–₱50B with ₱250M minimum offer; 15% >₱50B with ₱10B minimum offer; REIT 33.33%; lower floor ≥12% for issuers ≥₱200B) and maintenance levels (10% for companies listed before SEC MC 13 s. 2017; 20% after; for post-MC 11 listings 20% up to ₱50B, 15% above; REIT 33.33%) [^pse-amended-mpo-rule-2026-08:2][^pse-amended-mpo-rule-2026-08:3]. A company that falls below MPO "shall be **immediately suspended** from trading for a period of not more than six (6) months from the date of breach", with a compliance plan due within ten days, and "shall be automatically delisted" if still non-compliant; a compliance plan or pending corrective measures do not defer the suspension; 5-year relisting ban applies [^pse-amended-mpo-rule-2026-08:5][^pse-amended-mpo-rule-2026-08:6]. Live example (**[S]**): after the Gokongwei family's tender offer for Robinsons Retail Holdings (RRHI) left public ownership at 0.31% against a 10% minimum, PSE halted RRHI at 9:13 am on Mon 13 Jul 2026 once the tender-offer block sale was completed, with voluntary delisting expected by 28 Jul 2026; the stock had hit its daily limit on unusual trading in the preceding days ([^insiderph-2026-07-13-rrhi-suspension]). The previous "Amended MPO Rule" already used the same suspension/automatic-delisting wording (Steniel: breach 22 May 2023; Metro Global: breach 5 Feb 2024; six-month clocks run from the breach date) [^pse-cn-2023-0058-steniel-mpo-non-compliance:1][^pse-cn-2024-0037a-metro-global-mpo-non-compliance:1]. Non-public shares include holdings ≥10% of the common shares, board-represented holders, directors/principal officers, controlling shareholders and affiliates; holdings of "Funds" (mutual funds, UITFs, asset managers) are public "regardless of the amount … unless the Fund has a Board seat" [^pse-amended-mpo-rule-2026-08:10][^pse-amended-mpo-rule-2026-08:11].
- **[P]** Broker-level (TP) stoppages — CMIC Rules Art. X: voluntary vs involuntary suspension; grounds include SEC take-over order, clearing-agency suspension, failure to restore RBCA ≥1.1 / net liquid capital ≥₱5M, unimpaired paid-up capital shortfall, and "grave violation of the Securities Laws … inimical to the interest of the Exchange, the investors and the public" (§7); suspension automatically suspends the Trading Right and cuts access to PSE, PDTC and SCCP systems (§9) [^pse-cmic-rules:106][^pse-cmic-rules:107]. Recent notices: Mount Peak Securities suspended 13 Aug 2025 (capitalization), clients may transfer or sell only with CMIC approval; proprietary and related-party trades barred [^pse-tpa-2025-0050-mount-peak-involuntary-suspension:2]; Benjamin Co Ca & Co. suspended 31 Jul 2026 on the same terms [^pse-tpa-2026-0035-benjamin-co-ca-involuntary-suspension:2]; Globalinks suspended 9 Jul 2025 (lifted Oct 2025) and Equitiworld taken over in 2024 [S] ([^insiderph-2025-08-13-mount-peak-cmic]); SEC approved CMIC's Equitiworld liquidation/allocation plan on 17 Mar 2026 [^pse-cn-2026-0012:2]; one-day denial of access for Meridian Securities on 5 Oct 2018 at CMIC's request [^pse-cn-2018-0048-cmic-denial-of-access-meridian:1]. Earlier cases in the PSE annual reports: CMIC suspended I. Ackerman & Co. in 2014 (SEC take-over order 2015) [^pse-annual-report-2017:33]; after client complaints of possible trading-related irregularities on their accounts, CMIC suspended DW Capital, Inc.'s trading of all listed securities on 10 Aug 2017 (petition to the SEC for a take-over order on 18 Aug; the suspension was lifted on 5 Dec 2017 pursuant to a court writ) [^pse-annual-report-2017:33]. A suspended individual TP/Trader is blocked from the trading system and may be reinstated only if ≥1 hour remains before close (IG V.15–17) [^pse-implementing-guidelines-trading-rules:10].

### Inferences
- **[I]** The 10:30 am re-opening seen for SRDC, Xurpas and MRC equals the IG matrix's "50 minutes suspension + 10 minutes reservation" counted from the 9:30 open.
- **[I]** A hedge fund's *position-level* triggers: (a) price at/near ceiling/floor for several sessions (CMIC trigger), (b) approaching MPO floor on holdings made non-public by ≥10% stakes, (c) filing-calendar risk (17-A day 105/120; 17-Q day 45/50) for small caps, (d) broker suspensions that strand client orders.
- **[I]** For large caps the bigger practical risk is the disclosure halt: it is issuer-requested/PSE-imposed on news and lasts ≥1 hour; orders remain enterable during halts but cannot be matched.

### Gaps
- CMIC's *pre-established price/volume benchmarks* are not public.
- No consolidated statistics of halts/suspensions per year (PSE circulars searched individually only).
- Whether the 2022 halt/clarification proposals were adopted after Jan 2025: no effectivity circular found.
- SEC-ordered halts (RTR gives the SEC the same power) — no recent example found.

### Execution implications
- Subscribe to PSE circulars/EDGE feeds and build an automated "halt/suspension" state machine for: halt (orders accepted, no matching), suspension (orders purged), reservation, resume at pre-open vs 10:30.
- Pre-trade checks for names with late filings, MPO proximity or surge-to-ceiling patterns; treat sustained limit-up with no disclosure as a CMIC-halt risk (trade smaller, avoid being the last buyer).
- Maintain broker diversification: TP suspensions restrict client activity to CMIC-approved transfers.

---

## 5. Market-conduct rules: manipulation, insider trading, front-running; surveillance, enforcement and penalties

### Takeaway
The conduct regime has three layers: the SRC (RA 8799) and its 2015 IRR (SEC-enforced, criminal and administrative); PSE's RTR (fines/suspensions for rule breaches); and the CMIC Rules (CMIC, the PSE's independent audit/surveillance unit, operating since 12 Mar 2012). The IRR lists "marking the close", painting the tape, wash sales and matched orders by name; CMIC's text goes further (quotes "whether matched/executed or not" near the close) and obliges brokers to report suspected manipulation within 24 hours. Enforcement is visible mainly through CMIC broker sanctions and a few high-profile SEC complaints.

### Cited findings
- **[P]** Statute: SRC §24.1 prohibits (a) creating a false/misleading appearance of active trading (no change in beneficial ownership; simultaneous orders of substantially the same size, time and price), (b) series of transactions that raise/depress price or create active trading "through manipulative devices such as marking the close, painting the tape, squeezing the float, hype and dump, boiler room operations", (c) circulating price-move information from manipulative operations, (d) false/misleading statements, (e) pegging/fixing/stabilizing prices; §24.2 bars manipulative devices and makes short sales and "stop-loss order[s]" subject to SEC rules [^ra-8799-src:24][^ra-8799-src:25]. §26 fraud [^ra-8799-src:26]; **§27.1** insider trading (presumption for insiders and relatives within the 2nd degree trading between information and its absorption), §27.2 definition of material non-public information, §27.3 tipping, §27.4 tender-offer insider trading [^ra-8799-src:26][^ra-8799-src:27].
- **[P]** 2015 IRR (effective 9 Nov 2015 after 25 Oct 2015 publication [^sec-2015-src-irr-notice-of-effectivity:1]): Rule 24.1.1–24.1.4 repeat and extend §24 — brokers must refuse orders they "reasonably suspect" create a false appearance and must weigh market impact, timing, related-party interest, unusual settlement, series of orders, commercial reason; failure to consider these factors "shall raise a presumption that the transaction/s is/are manipulative" (24.1.4); **24.1.5 examples**: painting the tape; "buying and selling securities at the close of the market in an effort to alter the closing price (marking the close)" (24.1.5.2); improper matched orders; hype and dump; wash sales; squeezing the float; false market information; creating temporary funds for manipulation; **24.1.6: obligations "apply in respect of all orders, irrespective of the trading system used and whether executed or not"** [^sec-2015-src-irr:67][^sec-2015-src-irr:68]. Rule 24.1(e) price fixing [^sec-2015-src-irr:70]. Rule 27 insider trading [^sec-2015-src-irr:73][^sec-2015-src-irr:74].
- **[P]** Front-running and client priority: IRR 30.2.1.2.6.1.3 — a registered person "shall not deal in any securities for himself or for any account in which he has an interest based upon advance knowledge he possesses of pending transactions for or with clients or any other non-public information" (SRC §27); client orders have priority over house orders and are handled "in the order in which they are received" ("Customer First", Rule 34.1: execute customer orders "immediately upon receipt", house/affiliate orders treated as proprietary, one dealing account per trader) [^sec-2015-src-irr:94][^sec-2015-src-irr:111]. PSE adds the Best Execution Rule (RTR Art. IV §23) and strict account-code identification/trade-amendment limits (Art. IV §15, §19) [^pse-revised-trading-rules:29][^pse-revised-trading-rules:25][^pse-revised-trading-rules:27].
- **[P]** Short selling (SRC §24.2, IRR 24.2-2): uptick rule ("at a price higher than the last sale" or at the last-sale price if above the preceding different price); delivery/borrow pre-condition; mandatory close-out; no short sales by directors, officers or principal stockholders; SEC may prohibit short selling at any time (24.2-2.10) [^sec-2015-src-irr:70][^sec-2015-src-irr:71]. PSE Guidelines (Oct 2023, v3): eligible = PSEi members, ETFs, MidCap and Dividend-Yield index constituents; short-interest ratio ≤10% else ineligible (announced end-day, effective next day); no short orders in pre-open/pre-close, day orders only, no aggregation, none in odd-lot or block sales, TP must enter the order (DMA clients only under conditions); daily publication of gross short sales and short positions; penalties under RTR Art. IX [^pse-short-selling-guidelines-2023-10:1][^pse-short-selling-guidelines-2023-10:2][^pse-short-selling-guidelines-2023-10:3][^pse-short-selling-guidelines-2023-10:4]; RTR Art. IV §5 (uptick rule, naked-short prohibition, PSE powers to suspend shorting or cap short positions) [^pse-revised-trading-rules:18][^pse-revised-trading-rules:19][^pse-revised-trading-rules:20].
- **[P]** CMIC Rules (V1.2, 15 Dec 2011; SEC approved 12 Jan 2012; amended Art. III §6 on 2 Feb 2012; effective 12 Mar 2012 when the SEC order of 9 Mar 2012 let CMIC start) [^pse-cmic-rules:2][^pse-cmic-rules:4][^pse-tpa-2012-0049-cmic-authority-to-commence:1][^pse-tpa-2012-0005-cmic-commencement:1]: Art. XI-B §1 — TPs shall not create a false/misleading appearance as to the market, price or value of a listed security; input a fictitious transaction or false price; deal "at any price which differs to an unreasonable extent from any firm price … displayed"; engage in conduct "whose sole or main purpose is to move the price of a listed security or the level of any index which includes said listed security"; cause another's rule violation [^pse-cmic-rules:113][^pse-cmic-rules:114]. §2: a TP that knows or suspects a client's transactions are unusual/manipulative must report to CMIC **within 24 hours of receipt of the order**; failure creates a presumption of involvement [^pse-cmic-rules:114]; §8 repeats IRR 24.1.3–24.1.4 and the 24-hour notice [^pse-cmic-rules:115][^pse-cmic-rules:116][^pse-tpa-2012-0099-cmic-reminder-art-xib-sec-8-manipulation:1]; §9 manipulative schemes include "(b) Posting actual or fictitious bid or offer at or near the close of the market, **whether matched/executed or not**, in an effort to alter or … likely … to alter the closing price (marking the close)" [^pse-cmic-rules:117]; §3–6 insider trading/insider definition [^pse-cmic-rules:114][^pse-cmic-rules:115]; §10 civil liability via SRC §59 [^pse-cmic-rules:117].
- **[P]** CMIC sanctions (Art. XII): violations are grave, major or minor; **"Trading-related Irregularities" are grave** — 1st: written reprimand + fine ₱25,000–₱200,000; 2nd: denial of the Trading Right and access to Exchange facilities; 3rd+: bar from the industry; major: ₱10,000–₱75,000+ escalating; minor: reprimand then ₱10,000–₱50,000; previous violations within six years count; sanctions are published once affirmed by the CMIC Board or unappealed; SEC may review/reclassify [^pse-cmic-rules:118][^pse-cmic-rules:119][^pse-cmic-rules:120][^pse-cmic-rules:122]. PSE's own penal sanctions for trading-rule breaches (RTR Art. IX; offences are counted within any rolling twelve-month period): major violations (incl. shorting by insiders, best-execution breach, naked short selling, uptick violations, odd-lot abuse, error-account abuse, malicious foreign-buy orders) — ₱100,000–₱199,999 (1st), ₱200,000–₱299,999 (2nd), ≥₱300,000 **and** ≥5 consecutive trading days' suspension (3rd+, published); minor — reprimand, ₱10,000, ≥₱50,000 [^pse-revised-trading-rules:37][^pse-revised-trading-rules:39][^pse-revised-trading-rules:40].
- **[P]** Statutory penalties: SEC administrative sanctions (SRC §54.1) — suspension/revocation of registration, fine ₱10,000–₱1,000,000 plus up to ₱2,000/day, disqualification from being an officer/director for violations of §§19.2, 20, 24, 26, 27, and a fine of up to three times the profit gained/loss avoided (cross-referenced as "Section 34" in the printed text); criminal penalty (SRC §73): fine ₱50,000–₱5,000,000 or imprisonment of 7–21 years, or both, imposed also on responsible officers of a juridical entity; civil liability for manipulation (§59) and insider trading (§61) before the RTC [^ra-8799-src:55][^ra-8799-src:56][^ra-8799-src:59][^ra-8799-src:60][^ra-8799-src:66].
- **[P]** Surveillance: CMIC functions as the "independent audit, surveillance, and compliance unit of the PSE, having taken over the functions of the former Market Regulation Division of the PSE"; it may investigate violations of the SRC and CMIC Rules by TPs and "trading-related irregularities and unusual trading activities" by issuers; SEC gave provisional SRO status on 2 Feb 2012 [^pse-annual-report-2025:8]. PSE says CMIC's surveillance system is "Total Market Surveillance (TMS)", developed by the Korea Exchange, with real-time alerts on price/volume movements ([^pse-web-investing-at-pse]).
- **[P]** Published enforcement (CMIC): 19 Oct 2012 compilation of investigation sanctions — Nieves Securities, Tower Securities and HDI Securities each reprimanded and fined **₱200,000** for failing to report in writing client transactions "which possibly constitute Unusual Trading Activities" (Art. XI-B §§2, 8; SRC Rule 24.1(b)-1), plus smaller fines for KYC/best-execution lapses [^pse-tpa-2012-0177-cmic-disciplinary-actions-2012-10-19:17][^pse-tpa-2012-0177-cmic-disciplinary-actions-2012-10-19:18]; 10 Jan 2014 compilation: five investigation sanctions for 2012, four for 2013 (incl. one SRC 24.1(b)-1 case, Angping & Associates, appealed to the SEC) and four 2013 "Surveillance Department" sanctions (UBS, Lucky, BDO, Credit Suisse — written reprimands for breach of "Section XVIII, Paragraph 13" of the Implementing Guidelines) [^pse-cmic-memo-2014-004-disciplinary-actions-2014-01-10:29][^pse-cmic-memo-2014-004-disciplinary-actions-2014-01-10:30][^pse-cmic-memo-2014-004-disciplinary-actions-2014-01-10:31]; **[I]** IG XVIII.13 is the duty to disclose to PSE, within five trading days of a block sale, the identity of all clients who traded the security since the block-sale request was filed [^pse-implementing-guidelines-trading-rules:25]. [S] Headline-level corroboration: "4 brokers fined for 'suspicious' trading of stocks" (Inquirer, 22 Oct 2012) ([^inquirer-2012-10-22-four-brokers-fined]).
- **[P]** CMIC surveillance statistics reported in PSE annual reports (surveillance cases "investigated"/"evaluated" per year, and how many were referred to the Investigation and Enforcement Department, IED): 2013 — 117, referred 26 (IED resolved 6 investor complaints and 28 surveillance cases; 7 cases on investors/beneficial owners endorsed to the SEC; 13 of 133 audited TPs, i.e. 10%, sanctioned vs 59 or 44% at end-2012) [^pse-annual-report-2013:57]; 2014 — 87, referred 16 (14 cases endorsed to the SEC) [^pse-annual-report-2014:63]; 2015 — 66, referred 20 (six SD-endorsed cases forwarded to the SEC) [^pse-annual-report-2015:68]; 2016 — 167, referred 24 (IED endorsed 8 cases to the SEC and 6 possible PSE-disclosure-rule matters to the Exchange; 10 more cases still under investigation) [^pse-annual-report-2016:74]; 2017 — 149, referred 43 (26 beneficial-owner cases endorsed to the SEC; 12 disclosure-rule matters forwarded to the PSE) [^pse-annual-report-2017:33]; 2018 — 94, referred 23 (7 under investigation; 24 cases endorsed to the SEC and 19 disclosure-rule matters forwarded to the PSE; one IED resolution led to a temporary denial of a TP's trading right and access to PSE systems) [^pse-annual-report-2018:49]; 2019 — 94, referred 11 (4 under preliminary investigation; 10 cases endorsed to the SEC and 5 disclosure-rule matters forwarded to the PSE) [^pse-annual-report-2019:28]. Total market surveillance (TMS, Korea Exchange) trained analysts in Seoul [^pse-annual-report-2013:57][^pse-annual-report-2014:63]. I found no comparable figures for 2020–2025 (the FY2025 report describes CMIC but gives no case counts [^pse-annual-report-2025:8]).
- **[S]** SEC/judicial cases: **BW Resources (1999–2000)** — SEC complaint alleged wash sales, matched orders and "making the close" by named brokers as the price rose from ₱2 to ₱107 in a year; DOJ initially dismissed ([^philstar-2001-01-24-bw-charges]); a broker was convicted and sentenced to 14 years in May 2021 (headline only; article not retrievable) ([^inquirer-2021-05-22-bw-conviction]). **Villar Land Holdings (formerly Golden MV Holdings)** — SEC filed criminal complaints with the DOJ on 30 Jan 2026 against the company, Manuel Villar Jr. and family/directors alleging false/misleading statements (SRC §24.1(d), §26.3: unaudited 2024 total assets ₱1.33 trillion vs ₱35.7 billion audited), related-entity trading that "created artificial demand", and insider trading by director Camille Villar (Dec 2017 purchases); respondents denied wrongdoing (20 Apr 2026); as of 23 Aug 2026 still at preliminary investigation, no charges filed ([^politiko-2026-01-31-sec-villar-land][^bw-2026-04-21-villar-land-dismissal][^bilyonaryo-2026-08-23-villar-late-q2]). **PLDT (Dec 2022)** — SEC inquiry into the sell-off preceding the capex-overrun disclosure ([^philstar-2022-12-20-sec-pldt-inquiry]).

### Inferences
- **[I]** For spoofing/layering there is no named prohibition, but CMIC §9(b) (bids/offers near the close "whether matched or not"), IRR 24.1.6 (orders "whether executed or not") and CMIC §1(e) (conduct whose main purpose is to move the price) give regulators a basis; the TP-reporting duty (24 hours) makes brokers the first filter.
- **[I]** Closing-price manipulation is the best-documented abuse (BW case; CMIC §9(b)); the closing auction (14:45–15:00) plus run-off (orders only at the closing price) concentrates that risk, and the Closing VWAP session (VWAP computed from the day's trades, excluding blocks/crosses/odd lots) gives an incentive to move the day's VWAP.
- **[I]** Published enforcement is sparse and aggregate: CMIC's detailed sanction lists I could retrieve are 2012–2014, and the only case-count series is the 2013–2019 annual-report paragraphs (≈66–167 surveillance cases a year, of which 11–43 reach the enforcement department; 6–26 beneficial-owner cases a year are endorsed to the SEC — 7, 14, 6, 8, 26, 24 and 10 in 2013–2019 — and 5–19 disclosure-rule matters a year went to the PSE in 2016–2019). Neither names the manipulated issuers, so market-conduct risk is best read from the rules and the few SEC cases.

### Gaps
- CMIC's own annual reports and post-2014 disciplinary publications: cmic.com.ph returns 403 to automated clients; the Wayback index lists only front pages and forms. PSE annual reports for 2020–2024 were not available in the archive (2025 has no CMIC case counts).
- Whether the CMIC Rules were amended after 2012 (sanction amounts; Article XI) — the PSE still posts the 2012 text.
- SEC enforcement statistics; the SEC's reported May 2026 "annotated consolidated reference" of the 2015 IRR (seen only in a search-engine summary) was not retrieved, so post-2015 IRR amendments are not reconciled.
- No retrievable report of a closing-price-manipulation sanction after 2013.

### Execution implications
- Treat orders as regulated even when cancelled: quote-stuffing/layering near the close or around the auctions creates exposure under IRR 24.1.6 and CMIC §9(b).
- Keep an auditable order-intent log per child order (5-year log retention is required of DMA TPs [^pse-memo-sec-approved-dma-rules-2013-11-26:11]) and be ready for a broker's 24-hour suspicious-order report.
- Avoid same-beneficial-owner crosses and offsetting orders in the book (wash/matched-order definitions), including across funds/accounts under common control.
- Short-selling algos must obey the uptick rule, borrow-before-short, no short in pre-open/pre-close, and short-interest eligibility (≤10%).

---

## 6. Disclosure and ownership rules that bind traders

### Takeaway
Issuers must disclose material information to the PSE within 10 minutes and before the media (EDGE; release cut-off 4:00 pm since 25 May 2026). Investors must report ≥5% (SEC Form 18-A, 5 business days) and, as director/officer/≥10% holder, Forms 23-A/23-B (10 calendar days; PSE copy within 5 calendar days); directors/principal officers are barred from dealing from receipt of material non-public information until two full trading days after disclosure; mandatory tender offers start at 35% (or board control) and above 50%; issuer buy-backs need unrestricted retained earnings and PSE disclosure; a trade that breaches a foreign-ownership limit must be unwound at market the same trading day (or at the next open) under SEC MC 10 s.2025.

### Cited findings
- **[P]** Timing: SRC IRR 17.1.1.1.3(b): disclosure "promptly to the public through the news media" and, if listed, "to that Exchange and to the Commission within ten (10) minutes after the occurrence of the event and prior to its release to the public through the news media" [^sec-2015-src-irr:39]; PSE CLDR Art. VII §4.1 same 10 minutes; §4.2 bars selective disclosure of MNPI unless simultaneously disclosed to PSE (exceptions for persons bound by confidentiality); §4.3 standards; §4.4 list of mandatory events (change of control, ≥10% asset transactions, dividends, resignations, ±10% YoY revenue change, etc.); §16 corrections within ten minutes; §14 analyst/investor briefings notified ≥3 trading days ahead [^pse-listing-disclosure-rules:139][^pse-listing-disclosure-rules:140][^pse-listing-disclosure-rules:141][^pse-listing-disclosure-rules:142][^pse-listing-disclosure-rules:143][^pse-listing-disclosure-rules:144][^pse-listing-disclosure-rules:145][^pse-listing-disclosure-rules:149][^pse-listing-disclosure-rules:150].
- **[P]** EDGE release cut-off: **4:00 pm** for disclosures received on or before; later submissions are posted next trading day; the submission system stays open after 4 pm — CN-2026-0024 (22 May 2026), effective Mon 25 May 2026 [^pse-cn-2026-0024-edge-cutoff-4pm:1]; superseded cut-off 3:30 pm effective 1 Mar 2022 (CN-2022-0010; still printed in the Jan 2025 CLDR note) [^pse-cn-2022-0010-edge-cutoff-330pm:1][^pse-listing-disclosure-rules:139]; EDGE has been the filing channel since 27 Dec 2013 [^pse-listing-disclosure-rules:138]. Outage precedent: on 19 Jan 2026 the PSE disclosure system was unavailable; issuers were told to e-mail "Emergency Disclosure [symbol] – [template]" to PSE; EDGE accessible again the same day [^pse-cn-2026-0003-1-edge-unavailable:1][^pse-cn-2026-0006-edge-accessible:1].
- **[P]** Beneficial ownership (SRC §18 / IRR Rule 18): any person acquiring beneficial ownership of **5%** of a class of equity securities of a public/listed company files a sworn **SEC Form 18-A** with the issuer, the Exchange and the SEC — statute: within 10 days; **IRR 18.1.2: within five (5) business days** after acquisition; amendments on any change (18.2); groups acting together are deemed to acquire as of the agreement date (18.1.5.3); short-form **Form 18-AS** within 45 days after year-end only for passive holders that are brokers/dealers, BSP-regulated banks, insurers, investment houses, registered investment companies or pension plans [^ra-8799-src:18][^ra-8799-src:19][^sec-2015-src-irr:42][^sec-2015-src-irr:43][^sec-2015-src-irr:44].
- **[P]** Directors, officers and ≥10% holders (SRC §23 / IRR Rule 23): **Form 23-A** within 10 calendar days of becoming such an owner/director/officer; **Form 23-B** within 10 calendar days after each calendar month-end with a change; for listed securities the report goes to the Exchange "not more than five (5) calendar days after such person became beneficial owner"; statute uses "more than ten per centum", IRR "ten percent (10%) or more"; **short-swing profits** from any purchase and sale within <6 months are recoverable by the issuer (§23.2) and such persons may not short (§23.3) [^sec-2015-src-irr:65][^sec-2015-src-irr:66][^ra-8799-src:22][^ra-8799-src:23]. PSE separately requires issuers to disclose directors'/principal officers' direct and indirect holdings within **five trading days** of admission, election/appointment or any change (CLDR §13.1) — "separate and distinct from the reportorial requirements under SRC Rule 23" (SEC Forms 23-A/23-B must still be filed) — and requires 18/23 reports to be furnished to the Exchange (§17.5) [^pse-listing-disclosure-rules:149][^pse-listing-disclosure-rules:152].
- **[P]** Insider blackout (CLDR Art. VII §13.2): "A Director or a Principal Officer of an Issuer must not deal in the Issuer's securities during the period within which a material non-public information is obtained and up to two (2) full Trading Days after the price sensitive information is disclosed" — violation is a Level 2 offence [^pse-listing-disclosure-rules:149][^pse-listing-disclosure-rules:160]. Proposed (CN-2024-0048, 30 Sep 2024): extend the rule to the **issuer itself (no sale or buy-back)** and fix an earnings blackout from **30 calendar days** before the earlier of earnings pre-announcement or 17-A/17-Q submission until two full trading days after disclosure [^pse-cn-2024-0048-consultation-blackout-rule:4][^pse-cn-2024-0048-consultation-blackout-rule:5]; the Jan 2025 CLDR text still shows the old rule and I found no effectivity circular.
- **[P]** Mandatory tender offers (SRC §19.1; IRR Rule 19): statute — a person/group intending to acquire ≥15% (or ≥30% over twelve months) of a listed class must file a declaration/tender offer; **IRR 19.2.1**: ≥15% in a 12-month period → file a declaration; **19.2.2**: intending to acquire **35%** of voting shares "or such outstanding voting shares that are sufficient to gain control of the board" within 12 months → disclose and make a tender offer for that percentage; **19.2.5**: any acquisition resulting in **>50%** of total outstanding equity → tender offer for all remaining shares at a price supported by a fairness opinion, accepting all tendered; 19.2.3: acquisitions through the exchange trading system need no tender offer if the 35%/control target is not reached (even if the remainder is acquired by block sale); 19.2.4: direct purchases from holders → tender offer, closing after the offer; exemptions include purchases from unissued/increased capital (unless it yields ≥50%/control), foreclosure, privatization, rehabilitation, **"purchases in the open market at the prevailing market price"**, mergers (19.3); offer open ≥20 business days; mandatory offer at the highest price paid in the prior six months (19.9.2); anyone aware of a pending offer may not trade the target until announced (19.10 = insider trading under §27.4); SEC may nullify non-compliant purchases and order a tender offer (19.13); Form 19-1 filing (19.6) [^ra-8799-src:20][^ra-8799-src:21][^sec-2015-src-irr:45][^sec-2015-src-irr:46][^sec-2015-src-irr:48][^sec-2015-src-irr:50][^sec-2015-src-irr:51][^sec-2015-src-irr:52][^sec-2015-src-irr:53]. [S] Holcim PH tender offer (Holderfin, 2023) and its tax treatment appear in trade press ([^mb-2023-07-24-holcim-tender-offer-taxes], headline-level only).
- **[P]** Issuer buy-backs: IRR 19.4.1 — an issuer may repurchase its own shares "only … if such Issuer has unrestricted retained earnings in its books to cover the amount of shares to be purchased" and for stock-option/purchase plans, short-term obligations settled by re-issuance, paying dissenting/withdrawing stockholders, or other legitimate purpose; widespread solicitation triggers the issuer tender-offer procedure; no repurchase outside the offer for 10 business days after termination (19.4.4) [^sec-2015-src-irr:48][^sec-2015-src-irr:49]; PSE Art. VII §9: planned acquisitions/dispositions of treasury shares disclosed promptly and each execution (number, price) before the next pre-open [^pse-listing-disclosure-rules:148]. No SEC safe-harbour for volume/timing found; blackout expansion proposed (above).
- **[P]** Foreign-ownership limits (FOL) as an order-level constraint: the Trading System "will earmark all valid foreign buying Orders" and PSE can sanction foreign buy orders posted "for the malicious purpose of limiting the available volume for foreign buyers" (RTR Art. IV §2(d)) [^pse-revised-trading-rules:17]; every order carries a local/foreign flag in its account code (see §7); issuers with limits must file a monthly foreign-ownership report (CLDR §17.13) [^pse-listing-disclosure-rules:157]. Since **9 Aug 2025** (SEC MC 10 s.2025, circulated as PSE CN-2025-0035/-0036) a trade that breaches a foreign-ownership limit — called a "remote event" because "the PSE maintains a system that strictly monitors and enforces foreign ownership limits" (recital) — obliges the foreign buyer, through its broker, to dispose of the excess shares "at the prevailing market price" and return the proceeds: immediately and within the same trading day if discovered in trading hours, otherwise at the next day's open; violations are punishable under SRC §54 [^pse-cn-2025-0035-sec-declassification-mandate:2][^pse-cn-2025-0035-sec-declassification-mandate:3][^pse-cn-2025-0036-declassification-effectivity:1]. The engine-side check that stops foreign buying at the limit is not described in the rule documents I found; the companion foreign-access note (09_costs_taxes_foreign_access.md, §3) documents the live "Foreign Shares Available" market-data message and infers that foreign-flagged buys are rejected once availability reaches zero **[I]**.

### Inferences
- **[I]** A foreign hedge fund is not among the Rule 18.1.3 passive-filer categories, so it must file the full Form 18-A within five business days of crossing 5% (and again on changes); crossing 10% adds Form 23-A/23-B duties and §23.2 short-swing exposure, and ≥10% holdings are "non-public" for MPO purposes (the Funds carve-out suggests asset-manager vehicles may be treated as public; classification is for PSE).
- **[I]** The open-market exemption (19.3.1.6) is what lets an on-exchange accumulator pass 35% without a tender offer; 19.2.3/19.13 limit what happens if part of the stake is bought off-market, so structure matters.
- **[I]** The 10-minute/pre-media rule means most price-sensitive news is released intraday after a halt request; the 4:00 pm release cut-off creates a window (4:00–open) where disclosures filed after cut-off appear next trading day pre-open.

### Gaps
- Exact amendment history of IRR Rules 18/19/23 after 2015 (e.g., SEC memorandum circulars) not reconciled.
- Whether CN-2024-0048 (blackout/earnings window) or the 2022 halt-voluntariness proposals took effect after Jan 2025.
- SEC rules on buy-back programme mechanics (volume/price/timing) — none found beyond IRR 19.4 and PSE disclosure.

### Execution implications
- Position-limit monitors at 5% (file 18-A within 5 business days), 10% (23-A/23-B; short-swing), 15% (declaration), 35%/board control and 50% (tender offer) — per class of equity, aggregating persons acting in concert.
- Blackout compliance for insider-linked funds: no dealing from MNPI receipt until T+2 full trading days after disclosure.
- Event-driven strategies: the 10-minute rule and 1-hour halt after disclosure make first-minute execution a regulated, halt-constrained event; EDGE cut-off at 4:00 pm.
- Foreign-flagged buys in FOL-constrained names (a 40% cap on most listed companies per the foreign-access note): size against the live foreign-shares-available figure; an executed breach is a forced market sale at the same-day or next-open price, an uncapped execution-risk event.

---

## 7. Algorithmic trading, DMA, HFT and mandated order controls

### Takeaway
The PSE has **no rule expressly permitting algorithmic or high-frequency trading**. The DMA Rules (SEC-approved Oct 2013, effective on the first trading day of 2014, i.e. 2 Jan) prohibit using the DMA facility for "High-Frequency and/or Algorithmic trading"; PSE has granted exemptions for child orders of conditioned parent orders and in Sept 2023 proposed an "Algorithmic Trading" article (parent order manual, child orders limit orders, PSE can suspend) — still "pending approval by the SEC" in Jan 2024 and not in the Feb 2024 SEC-approved VWAP package. Order flow is constrained by TP-level value limits, FEOMS certification and message-flow controls, DMA pre-trade risk filters, and surveillance duties.

### Cited findings
- **[P]** DMA Rules (SEC letter 29 Oct 2013; PSE memo 26 Nov 2013: effective first trading day of 2014; 6-month transition for existing DMA TPs): definitions — "Algorithmic Trading" (platform entry of orders with an algorithm deciding timing, price or quantity "or in many cases initiating the order without human intervention") and "High-Frequency Trading" ("computer-driven process of entering or cancelling orders … over sub-second intervals"); DMA services = Automatic Order Routing (internet/STP) and **Sponsored Access (QIBs only)**; **§9(e): "The DMA Facility shall not be used for High-Frequency and/or Algorithmic trading"**; §9(c) no simultaneous multiple log-ins on one user ID; §10(h) facility must have built-in measures to prevent wash sales; §10(a) the TP is "ultimately responsible for all DMA Orders"; §11 automated **pre-trade risk filters** before access — trade exposure (gross/net), order size (value, volume) and **price limit** (% or ticks from LTP or last adjusted close), reviewed daily; §12 system logs kept ≥5 years; §14 PSE may disconnect "without prior notice" and suspend/revoke on SEC/CMIC/SCCP recommendation; §19 RTR penalties apply to DMA flow [^pse-memo-sec-approved-dma-rules-2013-11-26:1][^pse-memo-sec-approved-dma-rules-2013-11-26:3][^pse-memo-sec-approved-dma-rules-2013-11-26:4][^pse-memo-sec-approved-dma-rules-2013-11-26:8][^pse-memo-sec-approved-dma-rules-2013-11-26:9][^pse-memo-sec-approved-dma-rules-2013-11-26:10][^pse-memo-sec-approved-dma-rules-2013-11-26:11][^pse-memo-sec-approved-dma-rules-2013-11-26:12].
- **[P]** Sept 2023 consultation (CN-2023-0043, 5 Sep 2023): PSE says the DMA Rules "expressly prohibit" algo trading but that it "has granted exemptions … in respect of child orders originating from conditioned parent orders"; proposes new RTR Art. V: "Algorithmic Trading is allowed by the Exchange"; **no programmed/automated entry of a Parent Order**; **child orders must be limit orders**; TP must satisfy IG requirements before activating algos in its FEOMS or DMA facility; PSE may suspend algorithmic trading that slows or disrupts the Trading System (unusual order volume/behaviour); DMA TPs must risk-check child orders, "shall not be engaged in, and will not accept any Orders arising from or intended for, High Frequency Trading", submit the list/behaviour of each algo order type and wait for PSE's written no-objection, and tag parent–child identifiers; HFT stays banned [^pse-cn-2023-0043:3][^pse-cn-2023-0043:5][^pse-cn-2023-0043:6][^pse-cn-2023-0043:7][^pse-cn-2023-0043:8][^pse-cn-2023-0043:9][^pse-cn-2023-0043:20][^pse-cn-2023-0043:25].
- **[S]** Status: PSE said on 4 Jan 2024 it was "proposing to provide provisions that will expressly allow algorithmic trading in the Revised Trading Rules, which are also pending approval by the SEC" while the SEC had already approved VWAP trading ([^philstar-2024-01-04-pse-new-products]). **[P]** The SEC-approved package of 1 Feb 2024 contains only the VWAP rules (Art. I definition, Art. II schedule, Art. VI, IG XXV) — no algorithmic-trading article [^pse-approved-rules-vwap-trading-2024:1][^pse-approved-rules-vwap-trading-2024:2][^pse-approved-rules-vwap-trading-2024:4]; PSE's trading-participant rules page lists no algorithmic-trading rule among its 2024–25 uploads ([^pse-web-regulation-trading-participants]).
- **[P]** VWAP trading (approved 1 Feb 2024, live 1 Mar 2024): executed only in the Closing VWAP session at the day's VWAP (excluding block sales, intentional crosses and odd lots), minimum value ₱500,000, one TP per trade (two-firm later subject to SEC approval), not allowed in suspended/halted securities; if the VWAP display is delayed the session is suspended and cancelled for the day if <5 minutes remain [^pse-approved-rules-vwap-trading-2024:4][^pse-approved-rules-vwap-trading-2024:7][^pse-cn-2024-0012-vwap-go-live:1].
- **[P]** Mandated order controls at TP level: **value limit per order per trader** (TP-set but ≤ the Exchange limit; temporary changes by form one day ahead) (RTR Art. IV §12; IG IX) [^pse-revised-trading-rules:24][^pse-implementing-guidelines-trading-rules:17]; trader IDs only for SEC-licensed, PAM-certified traders, classed proprietary/client/PC (max two PC traders), with separate traders for house and client books and Chinese walls (RTR Art. IV §22; IG V) [^pse-implementing-guidelines-trading-rules:8][^pse-implementing-guidelines-trading-rules:9][^pse-revised-trading-rules:28]; every order carries an account code (type and local/foreign flag) and trades unbundled/amended within set deadlines [^pse-implementing-guidelines-trading-rules:21][^pse-implementing-guidelines-trading-rules:22]; **FEOMS** must be PSE-certified and recertified for each release, one FEOMS login per TP to the CCG, and "The PSE reserves the right to impose message flow controls for the FEOMS"; PSE may disconnect a FEOMS link that causes problems; TP must supply client lists and risk-management procedures for clients using its FEOMS terminals [^pse-implementing-guidelines-trading-rules:30][^pse-implementing-guidelines-trading-rules:31][^pse-implementing-guidelines-trading-rules:32][^pse-implementing-guidelines-trading-rules:33]; TPs must keep a backup terminal connected to the PSE disaster-recovery site (IG XXI, 2010) [^pse-implementing-guidelines-trading-rules:30]; SEC IRR 52.1.6.18: DMA clients must carry unique client codes [^sec-2015-src-irr:193]; TP is "solely and fully liable" for all orders entered via onsite, offsite, third-party order-routing, DMA or any other system (RTR Art. IV §2(a)) [^pse-revised-trading-rules:17].
- **[P]** Order/trade reversals that can undo an algo's fills: trade cancellation only for (a) TP mistake agreed by both parties (form by 5 pm T+0), (b) computer/system error confirmed by PSE, or (c) Board resolution with SEC notice at least three trading days before; fee per cancelled trade; error account must be used and positions liquidated within a month (2024 proposal to drop the one-month limit pending) [^pse-revised-trading-rules:26][^pse-implementing-guidelines-trading-rules:18][^pse-implementing-guidelines-trading-rules:19][^pse-revised-trading-rules:27][^pse-cn-2024-0048-consultation-blackout-rule:9][^pse-cn-2024-0048-consultation-blackout-rule:10].
- **[P]** Broker-side duties that shape algos: TPs must report suspected manipulation within 24 hours (CMIC XI-B §2), observe Customer First/Best Execution (IRR 34.1; RTR Art. IV §23), keep order tickets time-stamped and synchronized to the Exchange clock (IRR 52.1.7) [^pse-cmic-rules:114][^sec-2015-src-irr:111][^pse-revised-trading-rules:29][^sec-2015-src-irr:194][^sec-2015-src-irr:195].
- **[P]** Pending changes: SEC draft **Rules on Market Making** exposed 13/14 Aug 2026 (comments to 28 Aug) [^pse-cn-2026-0039-sec-market-making-rfc:2]; NTE go-live **23 Nov 2026** after market rehearsals 31 Oct, 7 Nov and 14 Nov; FEOMS certification window 10–23 Sep 2026; day-1 limit orders only; lot size one share; negotiated-trade facility; run-off order entry change [^pse-nte-broker-forum-2026-07-09:7][^pse-nte-broker-forum-2026-07-09:8][^pse-nte-broker-forum-2026-07-09:9][^pse-nte-faq-2026-08:1].

### Inferences
- **[I]** Practically, institutional "algos" at the PSE run in two ways: (i) broker-side algorithms operated by the TP under its own FEOMS/trader IDs (parent order entered by a human trader; child orders limit-only is what PSE's 2023 text would codify), and (ii) buy-side parent orders sliced manually or via broker-provided tools. Direct sub-second client-controlled strategies through DMA/Sponsored Access are contractually barred.
- **[I]** The SEC may not have approved the algorithmic-trading article yet (no document found either way), so any fund relying on client-side algos through DMA should obtain written PSE no-objection via its broker; unapproved HFT remains prohibited.
- **[I]** Message-flow controls exist in the IG but no numeric message-rate limit is public; the NTE FIX/ITCH specs (released July 2026) probably carry throttles.

### Gaps
- Final status of the algorithmic-trading article (approval date/text) — not found after Jan 2024.
- Numeric message-rate/ratio limits and pre-trade limits imposed by PSE on FEOMS (not public).
- NTE order types beyond limit orders, price-collar and self-trade-prevention features (not in the documents I retrieved).
- CN-2023-0043 Annex pages describing the IG-level algo requirements were read only in summary.

### Execution implications
- Do not plan on client-controlled sub-second DMA strategies; run through a broker's certified FEOMS with human-entered parent orders and **limit-only child orders**; keep parent-child tagging ready for the proposed rule.
- Embed pre-trade controls mirroring DMA §11: exposure, order value/volume, and price-band (% from LTP/ACP) per child order — and the PSE's own value limit per trader.
- Design for trade-cancellation/amendment risk (system error cancellations, TP mistakes) and error-account liquidation.
- Re-certify FIX/ITCH connectivity for Eqlipse before 23 Nov 2026; assume new reject semantics.

---

## Source catalog

```yaml
- slug: arabnews-2020-03-16-first-to-suspend
  title: "Philippines first country to suspend all financial markets as coronavirus spreads (headline only)"
  publisher: "Arab News"
  type: web
  canonical_url: "https://www.arabnews.com/node/1642536"
  local_path: null
  edition: n/a
  amended_through: "2020-03-16"
  note: "Headline/snippet only; page not read."
- slug: bilyonaryo-2026-08-23-villar-late-q2
  title: "Six Villar firms face PSE sanctions over late Q2 financial reports"
  publisher: "Bilyonaryo"
  type: web
  canonical_url: "https://bilyonaryo.com/2026/08/23/six-villar-firms-face-pse-sanctions-over-late-q2-financial-reports/business/"
  local_path: null
  edition: n/a
  amended_through: "2026-08-23"
  note: "Secondary; full text read."
- slug: bw-2020-03-19-shares-plummet
  title: "Shares plummet as trading resumes after halt"
  publisher: "BusinessWorld"
  type: web
  canonical_url: "https://bworldonline.com/editors-picks/2020/03/19/284527/shares-plummet-as-trading-resumes-after-halt/"
  local_path: null
  edition: n/a
  amended_through: "2020-03-19"
  note: "Secondary."
- slug: bw-2020-05-01-three-level-cb
  title: "Amid volatility, PSE to implement 3-level circuit breaker system"
  publisher: "BusinessWorld"
  type: web
  canonical_url: "https://bworldonline.com/editors-picks/2020/05/01/292270/amid-volatility-pse-to-implement-3-level-circuit-breaker-system/"
  local_path: null
  edition: n/a
  amended_through: "2020-05-01"
  note: "Secondary."
- slug: bw-2025-09-17-delmonte-suspended
  title: "Del Monte Pacific suspended from trading on report filing lapse"
  publisher: "BusinessWorld"
  type: web
  canonical_url: "https://bworldonline.com/corporate/2025/09/17/698880/del-monte-pacific-suspended-from-trading-on-report-filing-lapse/"
  local_path: null
  edition: n/a
  amended_through: "2025-09-17"
  note: "Secondary; full text read."
- slug: bw-2026-01-09-srdc-resume
  title: "SRDC to resume trading on Jan. 9 after halt (Reuters via BusinessWorld)"
  publisher: "BusinessWorld"
  type: web
  canonical_url: "https://bworldonline.com/corporate/2026/01/09/723274/srdc-to-resume-trading-on-jan-9-after-halt/"
  local_path: null
  edition: n/a
  amended_through: "2026-01-09"
  note: "Secondary; full text read."
- slug: bw-2026-04-21-villar-land-dismissal
  title: "Villar Land seeks dismissal of SEC complaint"
  publisher: "BusinessWorld"
  type: web
  canonical_url: "https://bworldonline.com/corporate/2026/04/21/744267/villar-land-seeks-dismissal-of-sec-complaint/"
  local_path: null
  edition: n/a
  amended_through: "2026-04-21"
  note: "Secondary; full text read."
- slug: bw-2026-10-04-pnbh-debut
  title: "PNB Holdings flat after market debut amid heavy turnover"
  publisher: "BusinessWorld"
  type: web
  canonical_url: "https://bworldonline.com/corporate/2026/10/04/784202/pnb-holdings-flat-after-market-debut-amid-heavy-turnover/"
  local_path: null
  edition: n/a
  amended_through: "2026-10-04"
  note: "Secondary; full text read; first-day range for a listing by way of introduction (25 Sep 2026)."
- slug: inquirer-2012-10-22-four-brokers-fined
  title: "4 brokers fined for 'suspicious' trading of stocks (headline only)"
  publisher: "Inquirer.net"
  type: web
  canonical_url: "https://business.inquirer.net/88546/4-brokers-fined-for-suspicious-trading-of-stocks"
  local_path: null
  edition: n/a
  amended_through: "2012-10-22"
  note: "Headline only (not read)."
- slug: inquirer-2021-05-22-bw-conviction
  title: "Stock broker gets 14 years jail time for BW stock price manipulation (headline only)"
  publisher: "Inquirer.net"
  type: web
  canonical_url: "https://business.inquirer.net/323382/stock-broker-gets-14-years-jail-time-for-bw-stock-price-manipulation"
  local_path: null
  edition: n/a
  amended_through: "2021-05-22"
  note: "Headline from a news index only; the site blocks automated access, so the article was not read."
- slug: insiderph-2025-08-13-mount-peak-cmic
  title: "CMIC suspends 50-year-old stock broker Mount Peak over serious violations"
  publisher: "InsiderPH"
  type: web
  canonical_url: "https://insiderph.com/cmic-suspends-50-year-old-stock-broker-mount-peak-over-serious-violations-clients-may-sell-or-transfer-funds-with-approval"
  local_path: null
  edition: n/a
  amended_through: "2025-08-13"
  note: "Secondary; mentions Globalinks (9 Jul 2025; lifted Oct 2025) and Equitiworld (2024)."
- slug: insiderph-2025-08-20-storm-signal-3
  title: "Storm Signal No. 3 now enough to shut down PSE trading (headline only)"
  publisher: "InsiderPH"
  type: web
  canonical_url: "https://insiderph.com/storm-signal-no-3-now-enough-to-shut-down-pse-trading"
  local_path: null
  edition: n/a
  amended_through: "2025-08-20"
  note: "Headline only (not read); corroborates CN-2025-0037 Annex B."
- slug: insiderph-2025-09-09-delmonte-warning
  title: "Del Monte Pacific faces trading suspension on Sept. 15 over report delay"
  publisher: "InsiderPH"
  type: web
  canonical_url: "https://insiderph.com/del-monte-pacific-faces-trading-suspension-on-sept-15-over-report-delay"
  local_path: null
  edition: n/a
  amended_through: "2025-09-09"
  note: "Secondary; full text read. Differs by a day from BusinessWorld on the suspension date."
- slug: insiderph-2026-01-08-srdc-halt
  title: "Dormant SuperCity stock adds P5-B in unexplained surge, PSE halts trading"
  publisher: "InsiderPH"
  type: web
  canonical_url: "https://insiderph.com/dormant-supercity-stock-adds-p5-b-in-unexplained-surge-pse-halts-trading"
  local_path: null
  edition: n/a
  amended_through: "2026-01-08"
  note: "Secondary; read via fetch-tool summary."
- slug: insiderph-2026-07-13-rrhi-suspension
  title: "Robinsons Retail trading suspended as delisting enters final stage"
  publisher: "InsiderPH"
  type: web
  canonical_url: "https://insiderph.com/robinsons-retail-trading-suspended-as-delisting-enters-final-stage"
  local_path: null
  edition: n/a
  amended_through: "2026-07-13"
  note: "Secondary; full text read."
- slug: insiderph-2026-07-20-xurpas-resumes
  title: "Xurpas resumes trading after suspension over late filings"
  publisher: "InsiderPH"
  type: web
  canonical_url: "https://insiderph.com/xurpas-resumes-trading-after-suspension-over-late-filings"
  local_path: null
  edition: n/a
  amended_through: "2026-07-20"
  note: "Secondary; full text read."
- slug: insiderph-2026-08-24-villar-frozen
  title: "Villar empire fights to regain footing as P320-B in stocks stay frozen"
  publisher: "InsiderPH"
  type: web
  canonical_url: "https://insiderph.com/villar-empire-fights-to-regain-footing-as-p320-b-in-stocks-stay-frozen"
  local_path: null
  edition: n/a
  amended_through: "2026-08-24"
  note: "Secondary; opening paragraphs read."
- slug: mb-2023-07-24-holcim-tender-offer-taxes
  title: "Holcim tender offer now subject to hefty taxes (headline only)"
  publisher: "Manila Bulletin"
  type: web
  canonical_url: "https://mb.com.ph/2023/7/24/holcim-tender-offer-now-subject-to-hefty-taxes"
  local_path: null
  edition: n/a
  amended_through: "2023-07-24"
  note: "Headline only (not read)."
- slug: philstar-2001-01-24-bw-charges
  title: "SEC presses charges vs BW stock manipulators"
  publisher: "Philstar.com"
  type: web
  canonical_url: "https://www.philstar.com/business/2001/01/24/96832/sec-presses-charges-vs-bw-stock-manipulators"
  local_path: null
  edition: n/a
  amended_through: "2001-01-24"
  note: "Secondary; full text read."
- slug: philstar-2020-03-12-circuit-breaker
  title: "Worst PSEi crash since 2012 triggers 'circuit breakers'"
  publisher: "Philstar.com"
  type: web
  canonical_url: "https://www.philstar.com/business/2020/03/12/2000197/philippine-stocks-crash-noon-break"
  local_path: null
  edition: n/a
  amended_through: "2020-03-12"
  note: "Secondary; read via fetch-tool summary."
- slug: philstar-2021-12-07-medilines-debut
  title: "Medilines shares tank in volatile stock market debut"
  publisher: "Philstar.com"
  type: web
  canonical_url: "https://www.philstar.com/business/2021/12/07/2146329/medilines-shares-tank-volatile-stock-market-debut"
  local_path: null
  edition: n/a
  amended_through: "2021-12-07"
  note: "Secondary; full text read."
- slug: philstar-2022-12-20-sec-pldt-inquiry
  title: "SEC starts inquiry into PLDT sell-off"
  publisher: "Philstar.com"
  type: web
  canonical_url: "https://www.philstar.com/business/2022/12/20/2231896/sec-starts-inquiry-pldt-sell-off"
  local_path: null
  edition: n/a
  amended_through: "2022-12-20"
  note: "Secondary; full text read."
- slug: philstar-2024-01-04-pse-new-products
  title: "PSE to introduce more products"
  publisher: "Philstar.com"
  type: web
  canonical_url: "https://www.philstar.com/business/2024/01/04/2323215/pse-introduce-more-products"
  local_path: null
  edition: n/a
  amended_through: "2024-01-04"
  note: "Secondary; full text read; source for 'algorithmic trading pending SEC approval' (Jan 2024)."
- slug: philstar-2024-08-22-dominion-resumption
  title: "PSE lifts trading suspension on Dominion Holdings shares"
  publisher: "Philstar.com"
  type: web
  canonical_url: "https://www.philstar.com/business/2024/08/22/2379558/pse-lifts-trading-suspension-dominion-holdings-shares"
  local_path: null
  edition: n/a
  amended_through: "2024-08-22"
  note: "Secondary; full text read."
- slug: philstar-2025-06-05-vistamalls-lifted
  title: "Vistamalls suspension lifted after reporting failures cured (headline only)"
  publisher: "Philstar.com"
  type: web
  canonical_url: "https://www.philstar.com/business/stock-commentary/2025/06/05/2448404/vistamalls-suspension-lifted-after-reporting-failures-cured"
  local_path: null
  edition: n/a
  amended_through: "2025-06-05"
  note: "Headline only (not read)."
- slug: philstar-2025-07-07-island-it-resumption
  title: "Island IT open for trading today after 1,572-day suspension (Merkado Barkada)"
  publisher: "Philstar.com"
  type: web
  canonical_url: "https://www.philstar.com/business/stock-commentary/2025/07/07/2456175/island-it-open-trading-today-after-1572-day-suspension"
  local_path: null
  edition: n/a
  amended_through: "2025-07-07"
  note: "Secondary (commentary column); full text read."
- slug: philstar-2025-11-18-vll-plunge
  title: "Villar Land shares plunge 76% days after suspension lifted"
  publisher: "Philstar.com"
  type: web
  canonical_url: "https://www.philstar.com/business/2025/11/18/2488238/villar-land-shares-plunge-76-days-after-suspension-lifted"
  local_path: null
  edition: n/a
  amended_through: "2025-11-18"
  note: "Secondary; full text read (Bloomberg-sourced figures)."
- slug: politiko-2026-01-31-sec-villar-land
  title: "SEC files criminal raps vs. Villar Land, Manny Villar and family for insider trading, market manipulation"
  publisher: "Politiko"
  type: web
  canonical_url: "https://politiko.com.ph/sec-files-criminal-raps-vs-villar-land-manny-villar-and-family-for-insider-trading-market-manipulation/"
  local_path: null
  edition: n/a
  amended_through: "2026-01-31"
  note: "Secondary (reproduces SEC statement); full text read."
- slug: pse-amended-mpo-rule-2026-08
  title: "Effectivity of the PSE Amended Rule on Minimum Public Ownership and Revised Guidelines in Determining Public Ownership"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2026/08/Memo-to-Public_Effectivity-of-the-Amended-MPO-Rule-Rvsd-PO-Guidelines-v2.pdf"
  local_path: "pdfs/pse-amended-mpo-rule-2026-08.pdf"
  edition: in-force
  amended_through: "2026-08-11"
  note: "Implements SEC MC No. 11 s.2026; effective immediately."
- slug: pse-annual-report-2013
  title: "PSE Annual Report 2013 (CMIC section with surveillance case counts)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://www.pse.com.ph/%20(annual%20report;%20direct%20PDF%20URL%20not%20captured)"
  local_path: "pdfs/pse-annual-report-2013.pdf"
  edition: n/a
  amended_through: "2013-12-31"
  note: "Fiscal-year-end date; publication date not stated. Archived by a parallel researcher."
- slug: pse-annual-report-2014
  title: "PSE Annual Report 2014 (CMIC section with surveillance case counts)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://www.pse.com.ph/%20(annual%20report;%20direct%20PDF%20URL%20not%20captured)"
  local_path: "pdfs/pse-annual-report-2014.pdf"
  edition: n/a
  amended_through: "2014-12-31"
  note: "Fiscal-year-end date; publication date not stated. Archived by a parallel researcher."
- slug: pse-annual-report-2015
  title: "PSE Annual Report 2015 (CMIC section with surveillance case counts)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://www.pse.com.ph/%20(annual%20report;%20direct%20PDF%20URL%20not%20captured)"
  local_path: "pdfs/pse-annual-report-2015.pdf"
  edition: n/a
  amended_through: "2015-12-31"
  note: "Fiscal-year-end date; publication date not stated. Archived by a parallel researcher."
- slug: pse-annual-report-2016
  title: "PSE Annual Report 2016 (CMIC section with surveillance case counts)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://www.pse.com.ph/%20(annual%20report;%20direct%20PDF%20URL%20not%20captured)"
  local_path: "pdfs/pse-annual-report-2016.pdf"
  edition: n/a
  amended_through: "2016-12-31"
  note: "Fiscal-year-end date; publication date not stated. Archived by a parallel researcher."
- slug: pse-annual-report-2017
  title: "PSE Annual Report 2017 (CMIC section with surveillance case counts)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://www.pse.com.ph/%20(annual%20report;%20direct%20PDF%20URL%20not%20captured)"
  local_path: "pdfs/pse-annual-report-2017.pdf"
  edition: n/a
  amended_through: "2017-12-31"
  note: "Fiscal-year-end date; publication date not stated. Archived by a parallel researcher."
- slug: pse-annual-report-2018
  title: "PSE Annual Report 2018 (CMIC section with surveillance case counts)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://www.pse.com.ph/%20(annual%20report;%20direct%20PDF%20URL%20not%20captured)"
  local_path: "pdfs/pse-annual-report-2018.pdf"
  edition: n/a
  amended_through: "2018-12-31"
  note: "Fiscal-year-end date; publication date not stated. Archived by a parallel researcher."
- slug: pse-annual-report-2019
  title: "PSE Annual Report 2019 (CMIC section with surveillance case counts)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://www.pse.com.ph/%20(annual%20report;%20direct%20PDF%20URL%20not%20captured)"
  local_path: "pdfs/pse-annual-report-2019.pdf"
  edition: n/a
  amended_through: "2019-12-31"
  note: "Fiscal-year-end date; publication date not stated. Archived by a parallel researcher."
- slug: pse-annual-report-2025
  title: "PSE Integrated Annual Report FY2025 (CMIC description at p.8)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://www.pse.com.ph/%20(annual%20report;%20direct%20PDF%20URL%20not%20captured)"
  local_path: "pdfs/pse-annual-report-2025.pdf"
  edition: in-force
  amended_through: "2025-12-31"
  note: "Fiscal-year-end date; publication date not stated. Archived by a parallel researcher."
- slug: pse-approved-rules-vwap-trading-2024
  title: "CN-2024-0010 - SEC-approved PSE Rules on VWAP Trading (Annex A: Art. I, II, VI; IG II, XXV)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2024/02/CN-2024-0010.pdf"
  local_path: "pdfs/pse-approved-rules-vwap-trading-2024.pdf"
  edition: in-force
  amended_through: "2024-02-01"
  note: "Pages 2-7 are images (read by OCR). Gives the current day schedule incl. Closing VWAP session."
- slug: pse-cmic-memo-2014-004-disciplinary-actions-2014-01-10
  title: "CMIC Memorandum 2014-004 - Publication of disciplinary actions (10 Jan 2014)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/AnnouncementOPSPDF/Publication%20of%20Disciplinary%20Actions.pdf"
  local_path: "pdfs/pse-cmic-memo-2014-004-disciplinary-actions-2014-01-10.pdf"
  edition: n/a
  amended_through: "2014-01-10"
  note: "Scanned (OCR); Annexes I-K = investigation/surveillance sanctions 2012-13."
- slug: pse-cmic-rules
  title: "Capital Markets Integrity Corporation (CMIC) Rules V1.2 with SEC approval letters and CMIC memo"
  publisher: "Capital Markets Integrity Corporation / PSE"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2021/04/Approved-CMIC-Rules-2.pdf"
  local_path: "pdfs/pse-cmic-rules.pdf"
  edition: in-force
  amended_through: "2012-02-02"
  note: "Scanned 124-page file (read by OCR for pp.2-8, 27-37, 100-124). SEC approval 12/13 Jan 2012; Art. III s6 amended 2 Feb 2012; effective 12 Mar 2012. Later amendments (sanction amounts etc.) not located - gap."
- slug: pse-cn-2013-0033-trading-suspension-2013
  title: "CN-2013-0033 - Trading suspension, 19 Aug 2013 (banking-system clearing suspension)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2013-0033.pdf"
  local_path: "pdfs/pse-cn-2013-0033-trading-suspension-2013.pdf"
  edition: n/a
  amended_through: "2013-08-19"
  note: "Event notice."
- slug: pse-cn-2014-0057-trading-halt-2014-11-20
  title: "CN-2014-0057 - Trading halt due to technical issues, 20 Nov 2014"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2014-0057.pdf"
  local_path: "pdfs/pse-cn-2014-0057-trading-halt-2014-11-20.pdf"
  edition: n/a
  amended_through: "2014-11-20"
  note: "Scanned notice (read by OCR)."
- slug: pse-cn-2014-0059-trading-suspension-2014-12-08
  title: "CN-2014-0059 - Trading suspension, 8 Dec 2014"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2014-0059.pdf"
  local_path: "pdfs/pse-cn-2014-0059-trading-suspension-2014-12-08.pdf"
  edition: n/a
  amended_through: "2014-12-08"
  note: "Event notice."
- slug: pse-cn-2015-0110-trading-halt-2015-08-24
  title: "CN-2015-0110 - Trading halt, 24 Aug 2015"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2015-0110.pdf"
  local_path: "pdfs/pse-cn-2015-0110-trading-halt-2015-08-24.pdf"
  edition: n/a
  amended_through: "2015-08-24"
  note: "Scanned notice (OCR)."
- slug: pse-cn-2015-0112-trading-halt-2015-08-25
  title: "CN-2015-0112 - Trading halt, 25 Aug 2015"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2015-0112.pdf"
  local_path: "pdfs/pse-cn-2015-0112-trading-halt-2015-08-25.pdf"
  edition: n/a
  amended_through: "2015-08-25"
  note: "Scanned notice (OCR)."
- slug: pse-cn-2015-0118-statement-trading-halts-2015
  title: "CN-2015-0118 - PSE Statement on the trading halts (24-25 Aug 2015)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2015-0118.pdf"
  local_path: "pdfs/pse-cn-2015-0118-statement-trading-halts-2015.pdf"
  edition: n/a
  amended_through: "2015-09-04"
  note: "Root-cause statement."
- slug: pse-cn-2016-0020-trading-halt-2016-04-08
  title: "CN-2016-0020 - Trading halt, 8 Apr 2016"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2016-0020.pdf"
  local_path: "pdfs/pse-cn-2016-0020-trading-halt-2016-04-08.pdf"
  edition: n/a
  amended_through: "2016-04-08"
  note: "Scanned notice (OCR)."
- slug: pse-cn-2016-0023-statement-trading-halt-2016
  title: "CN-2016-0023 - PSE Statement on Trading Halt, 8 Apr 2016"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2016-0023.pdf"
  local_path: "pdfs/pse-cn-2016-0023-statement-trading-halt-2016.pdf"
  edition: n/a
  amended_through: "2016-04-08"
  note: "Root-cause statement."
- slug: pse-cn-2017-0050-trading-suspension-2017-09-12
  title: "CN-2017-0050 - Trading suspension, 12 Sep 2017"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2017-0050.pdf"
  local_path: "pdfs/pse-cn-2017-0050-trading-suspension-2017-09-12.pdf"
  edition: n/a
  amended_through: "2017-09-12"
  note: "Event notice."
- slug: pse-cn-2017-0059-trading-suspension-2017-10-16
  title: "CN-2017-0059 - Trading suspension, 16 Oct 2017 (PhilPaSS)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2017-0059.pdf"
  local_path: "pdfs/pse-cn-2017-0059-trading-suspension-2017-10-16.pdf"
  edition: n/a
  amended_through: "2017-10-15"
  note: "Event notice."
- slug: pse-cn-2018-0048-cmic-denial-of-access-meridian
  title: "CN-2018-0048 - Implementation of CMIC action on Meridian Securities, Inc."
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2018-0048.pdf"
  local_path: "pdfs/pse-cn-2018-0048-cmic-denial-of-access-meridian.pdf"
  edition: n/a
  amended_through: "2018-10-05"
  note: "One-day denial of trading access at CMIC's request."
- slug: pse-cn-2019-0031-trading-halt-fire-drill
  title: "CN-2019-0031 - Trading halt due to fire drill, 4 Jun 2019"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2019-0031.pdf"
  local_path: "pdfs/pse-cn-2019-0031-trading-halt-fire-drill.pdf"
  edition: n/a
  amended_through: "2019-06-04"
  note: "Event notice."
- slug: pse-cn-2020-0002-trading-suspension-2020-01-13
  title: "CN-2020-0002 - Trading suspension, 13 Jan 2020 (Taal)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2020-0002.pdf"
  local_path: "pdfs/pse-cn-2020-0002-trading-suspension-2020-01-13.pdf"
  edition: n/a
  amended_through: "2020-01-13"
  note: "Event notice."
- slug: pse-cn-2020-0017
  title: "CN-2020-0017 - Shortened trading hours (15 Mar 2020)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2020-0017.pdf"
  local_path: "pdfs/pse-cn-2020-0017.pdf"
  edition: superseded
  amended_through: "2020-03-15"
  note: "COVID-19 schedule; superseded by CN-2020-0025 and later."
- slug: pse-cn-2020-0021
  title: "CN-2020-0021 - Trading suspension starting 17 Mar 2020"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2020-0021.pdf"
  local_path: "pdfs/pse-cn-2020-0021.pdf"
  edition: n/a
  amended_through: "2020-03-16"
  note: "COVID-19 market closure notice."
- slug: pse-cn-2020-0025-resumption-of-trading
  title: "CN-2020-0025 - Resumption of trading and settlement (19 Mar 2020)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2020-0025.pdf"
  local_path: "pdfs/pse-cn-2020-0025-resumption-of-trading.pdf"
  edition: n/a
  amended_through: "2020-03-17"
  note: "Resumption with shortened hours; floor closed."
- slug: pse-cn-2020-0028
  title: "CN-2020-0028 - Amendment of rule on static threshold (lower band 30%)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2020-0028.pdf"
  local_path: "pdfs/pse-cn-2020-0028.pdf"
  edition: in-force
  amended_through: "2020-03-21"
  note: "Amends RTR Art. IV s7(b) and IG VI.2(b); effective 24 Mar 2020."
- slug: pse-cn-2020-0035
  title: "CN-2020-0035 - Extension of shortened trading hours (to 30 Apr 2020)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2020-0035.pdf"
  local_path: "pdfs/pse-cn-2020-0035.pdf"
  edition: superseded
  amended_through: "2020-04-13"
  note: "COVID-19 schedule."
- slug: pse-cn-2020-0042
  title: "CN-2020-0042 - Shortened trading hours extended to 15 May 2020"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2020-0042.pdf"
  local_path: "pdfs/pse-cn-2020-0042.pdf"
  edition: superseded
  amended_through: "2020-04-27"
  note: "COVID-19 schedule."
- slug: pse-cn-2020-0044
  title: "CN-2020-0044 - Amendment of circuit breaker rules (three levels)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2020-0044.pdf"
  local_path: "pdfs/pse-cn-2020-0044.pdf"
  edition: in-force
  amended_through: "2020-04-29"
  note: "RTR Art. VIII s1 and new IG part on circuit breakers; effective 4 May 2020; SEC approval 20 Mar 2020."
- slug: pse-cn-2020-0046
  title: "CN-2020-0046 - Shortened trading hours under MECQ"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2020-0046.pdf"
  local_path: "pdfs/pse-cn-2020-0046.pdf"
  edition: superseded
  amended_through: "2020-05-14"
  note: "COVID-19 schedule."
- slug: pse-cn-2021-0055-lift-lower-static-threshold-sgp
  title: "CN-2021-0055 - SGP: lifting of lower static threshold"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2021-0055.pdf"
  local_path: "pdfs/pse-cn-2021-0055-lift-lower-static-threshold-sgp.pdf"
  edition: n/a
  amended_through: "2021-10-27"
  note: "Example of RTR Art. VII s6(c) lift."
- slug: pse-cn-2021-0057-keepr-lower-static-threshold-lift
  title: "CN-2021-0057 - KEEPR: lifting of lower static threshold"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2021-0057.pdf"
  local_path: "pdfs/pse-cn-2021-0057-keepr-lower-static-threshold-lift.pdf"
  edition: n/a
  amended_through: "2021-11-04"
  note: "Example of RTR Art. VII s6(c) lift."
- slug: pse-cn-2021-0059
  title: "CN-2021-0059 - Adjustments in trading hours (back to five-hour day, 6 Dec 2021)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2021-0059.pdf"
  local_path: "pdfs/pse-cn-2021-0059.pdf"
  edition: superseded
  amended_through: "2021-11-22"
  note: "Superseded by CN-2022-0004 (Omicron) then CN-2022-0009."
- slug: pse-cn-2022-0001-delay-market-opening
  title: "CN-2022-0001 - Advisory: delay in market opening and trading, 4 Jan 2022"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2022-0001.pdf"
  local_path: "pdfs/pse-cn-2022-0001-delay-market-opening.pdf"
  edition: n/a
  amended_through: "2022-01-04"
  note: "43 of 125 TPs unable to connect."
- slug: pse-cn-2022-0002-cancellation-of-trading-2022-01-04
  title: "CN-2022-0002 - Cancellation of trading, 4 Jan 2022"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2022-0002.pdf"
  local_path: "pdfs/pse-cn-2022-0002-cancellation-of-trading-2022-01-04.pdf"
  edition: n/a
  amended_through: "2022-01-04"
  note: "Whole trading day cancelled."
- slug: pse-cn-2022-0004
  title: "CN-2022-0004 - Shortened trading hours 14-31 Jan 2022"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2022-0004.pdf"
  local_path: "pdfs/pse-cn-2022-0004.pdf"
  edition: historical
  amended_through: "2022-01-11"
  note: "Omicron-era schedule."
- slug: pse-cn-2022-0009-trading-schedule-mar-2022
  title: "CN-2022-0009 - Trading schedule effective 1 Mar 2022"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2022-0009.pdf"
  local_path: "pdfs/pse-cn-2022-0009-trading-schedule-mar-2022.pdf"
  edition: in-force
  amended_through: "2022-02-17"
  note: "Full-day schedule (pre-close 14:45, close 15:00); extended by 15:00-15:15 Closing VWAP session from 2024."
- slug: pse-cn-2022-0010-edge-cutoff-330pm
  title: "CN-2022-0010 - Cut-off for posting disclosures on PSE EDGE (3:30 pm)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2022-0010.pdf"
  local_path: "pdfs/pse-cn-2022-0010-edge-cutoff-330pm.pdf"
  edition: superseded
  amended_through: "2022-02-24"
  note: "Superseded by CN-2026-0024 (4:00 pm)."
- slug: pse-cn-2022-0020-market-halt-consultation
  title: "CN-2022-0020 - Consultation: proposed amendments to Revised Trading Rules and Consolidated Listing and Disclosure Rules (market halt trigger etc.)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2022/05/CN_2022-0020.pdf"
  local_path: "pdfs/pse-cn-2022-0020-market-halt-consultation.pdf"
  edition: historical
  amended_through: "2022-05-11"
  note: "Proposal; market-halt part adopted in changed form by CN-2025-0037 (six-month ADTV window); Level 1/Level 2 disclosure penalties appear in the 2025 CLDR."
- slug: pse-cn-2022-0035-trading-suspension-2022-09-26
  title: "CN-2022-0035 - Trading suspension, 26 Sep 2022"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2022-0035.pdf"
  local_path: "pdfs/pse-cn-2022-0035-trading-suspension-2022-09-26.pdf"
  edition: n/a
  amended_through: "2022-09-25"
  note: "Event notice."
- slug: pse-cn-2022-0045-consultation-2022-part-ii
  title: "CN-2022-0045 - Consultation: 2022 amendments Part II (incl. voluntary disclosure halts, s4.5 halt removal)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2022-0045.pdf"
  local_path: "pdfs/pse-cn-2022-0045-consultation-2022-part-ii.pdf"
  edition: historical
  amended_through: "2022-11-16"
  note: "Proposal; adoption status of items 20-21 not confirmed (Jan 2025 CLDR text unchanged)."
- slug: pse-cn-2023-0043
  title: "CN-2023-0043 - Consultation: Algorithmic Trading and VWAP Trading amendments"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2023-0043.pdf"
  local_path: "pdfs/pse-cn-2023-0043.pdf"
  edition: historical
  amended_through: "2023-09-05"
  note: "VWAP portion adopted Feb 2024; algorithmic-trading article not found approved."
- slug: pse-cn-2023-0058-steniel-mpo-non-compliance
  title: "CN-2023-0058 - Steniel Manufacturing: non-compliance with Amended MPO Rule"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2023/10/CN_2023-0058.pdf"
  local_path: "pdfs/pse-cn-2023-0058-steniel-mpo-non-compliance.pdf"
  edition: n/a
  amended_through: "2023-10-23"
  note: "Quotes the pre-2026 'Amended MPO Rule' suspension wording."
- slug: pse-cn-2023-0074-ubp-trading-suspension
  title: "CN-2023-0074 - Trading suspension of Union Bank of the Philippines shares"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2023-0074.pdf"
  local_path: "pdfs/pse-cn-2023-0074-ubp-trading-suspension.pdf"
  edition: n/a
  amended_through: "2023-12-21"
  note: "Reference price not adjusted for 27% stock dividend."
- slug: pse-cn-2024-0002
  title: "CN-2024-0002 - Market resumption, 3 Jan 2024"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2024-0002.pdf"
  local_path: "pdfs/pse-cn-2024-0002.pdf"
  edition: n/a
  amended_through: "2024-01-03"
  note: "Event notice."
- slug: pse-cn-2024-0003-update-market-halt
  title: "CN-2024-0003 - Update on the market halt, 3 Jan 2024"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2024-0003.pdf"
  local_path: "pdfs/pse-cn-2024-0003-update-market-halt.pdf"
  edition: n/a
  amended_through: "2024-01-03"
  note: "Event notice."
- slug: pse-cn-2024-0012-vwap-go-live
  title: "CN-2024-0012 - VWAP Trading go-live (1 Mar 2024)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2024-0012.pdf"
  local_path: "pdfs/pse-cn-2024-0012-vwap-go-live.pdf"
  edition: in-force
  amended_through: "2024-02-15"
  note: "Launch notice."
- slug: pse-cn-2024-0037a-metro-global-mpo-non-compliance
  title: "CN-2024-0037A - Metro Global Holdings: non-compliance with Amended MPO Rule"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2024/09/CN-2024-0037A.pdf"
  local_path: "pdfs/pse-cn-2024-0037a-metro-global-mpo-non-compliance.pdf"
  edition: n/a
  amended_through: "2024-07-16"
  note: "Quotes the pre-2026 MPO suspension wording."
- slug: pse-cn-2024-0038-trading-suspension-2024-07-24
  title: "CN-2024-0038 - Trading suspension, 24 Jul 2024 (inclement weather)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2024/09/CN-2024-0038.pdf"
  local_path: "pdfs/pse-cn-2024-0038-trading-suspension-2024-07-24.pdf"
  edition: n/a
  amended_through: "2024-07-24"
  note: "Event notice."
- slug: pse-cn-2024-0048-consultation-blackout-rule
  title: "CN-2024-0048 - Consultation: expand black-out rule (Art. VII s13.2), error-account liquidation etc."
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2024-0048.pdf"
  local_path: "pdfs/pse-cn-2024-0048-consultation-blackout-rule.pdf"
  edition: historical
  amended_through: "2024-09-30"
  note: "Proposal; effectivity not found."
- slug: pse-cn-2024-0061-adjusted-schedule-2024-12-09
  title: "CN-2024-0061 - Adjusted trading schedule for 9 Dec 2024"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2024-0061.pdf"
  local_path: "pdfs/pse-cn-2024-0061-adjusted-schedule-2024-12-09.pdf"
  edition: n/a
  amended_through: "2024-12-09"
  note: "Delayed opening."
- slug: pse-cn-2025-0014
  title: "CN-2025-0014 - Delay in market open, 24 Mar 2025 (system connectivity issue)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2025-0014.pdf"
  local_path: "pdfs/pse-cn-2025-0014.pdf"
  edition: n/a
  amended_through: "2025-03-24"
  note: "Event notice."
- slug: pse-cn-2025-0015-adjusted-schedule-2025-03-24
  title: "CN-2025-0015 - Adjusted trading schedule for 24 Mar 2025"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2025-0015.pdf"
  local_path: "pdfs/pse-cn-2025-0015-adjusted-schedule-2025-03-24.pdf"
  edition: n/a
  amended_through: "2025-03-24"
  note: "Open at 11:10."
- slug: pse-cn-2025-0035-sec-declassification-mandate
  title: "CN-2025-0035 - SEC MC 10 s.2025 mandating declassification of Class A/B shares (SEC text at pp.2-3; s.4 foreign-ownership breach unwind)"
  publisher: "Philippine Stock Exchange / SEC"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2025-0035.pdf"
  local_path: "pdfs/pse-cn-2025-0035-sec-declassification-mandate.pdf"
  edition: in-force
  amended_through: "2025-08-11"
  note: "Archived by another researcher. SEC MC 10 s.2025 s.4: trades that breach foreign ownership limits must be disposed of at market the same trading day (or next open); s.5 penalties under SRC s.54."
- slug: pse-cn-2025-0036-declassification-effectivity
  title: "CN-2025-0036 - Effectivity of SEC MC 10 s.2025 (took effect 9 Aug 2025; articles to be amended by 9 Aug 2026)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2025-0036.pdf"
  local_path: "pdfs/pse-cn-2025-0036-declassification-effectivity.pdf"
  edition: in-force
  amended_through: "2025-08-15"
  note: "Archived by another researcher."
- slug: pse-cn-2025-0037
  title: "CN-2025-0037 - Amendments to Revised Trading Rules (market halt), correspondent TP guidelines, natural-disaster guidelines"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2025-0037.pdf"
  local_path: "pdfs/pse-cn-2025-0037.pdf"
  edition: in-force
  amended_through: "2025-08-20"
  note: "SEC-approved; effective immediately (correspondent requirement +2 months)."
- slug: pse-cn-2025-0043-non-trading-days
  title: "CN-2025-0043 - Non-trading days (Dec 2025 - 1 Jan 2026)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2025-0043.pdf"
  local_path: "pdfs/pse-cn-2025-0043-non-trading-days.pdf"
  edition: n/a
  amended_through: "2025-11-24"
  note: "Used for trading-day counting."
- slug: pse-cn-2026-0003-1-edge-unavailable
  title: "CN-2026-0003 - Access to disclosures via PSE website and filing of emergency disclosures (19 Jan 2026)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2026/01/CN-2026-0003-1.pdf"
  local_path: "pdfs/pse-cn-2026-0003-1-edge-unavailable.pdf"
  edition: n/a
  amended_through: "2026-01-19"
  note: "EDGE outage notice."
- slug: pse-cn-2026-0004-2-emergency-disclosures-trading-halt
  title: "CN-2026-0004 - Emergency disclosures and trading halt (MRC Allied), 19 Jan 2026"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2026/01/CN-2026-0004-2.pdf"
  local_path: "pdfs/pse-cn-2026-0004-2-emergency-disclosures-trading-halt.pdf"
  edition: n/a
  amended_through: "2026-01-19"
  note: "Includes PSE disclosure notice and MRC 17-C."
- slug: pse-cn-2026-0006-edge-accessible
  title: "CN-2026-0006 - EDGE systems now accessible (19 Jan 2026)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2026/01/CN-2026-0006.pdf"
  local_path: "pdfs/pse-cn-2026-0006-edge-accessible.pdf"
  edition: n/a
  amended_through: "2026-01-19"
  note: "Event notice."
- slug: pse-cn-2026-0012
  title: "CN-2026-0012 - Updates on Equitiworld Securities, Inc. (CMIC memo 2026-006)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2026-0012.pdf"
  local_path: "pdfs/pse-cn-2026-0012.pdf"
  edition: n/a
  amended_through: "2026-03-19"
  note: "SEC approval of CMIC liquidation/allocation plan."
- slug: pse-cn-2026-0024-edge-cutoff-4pm
  title: "CN-2026-0024 - Cut-off for posting disclosures on EDGE portal (4:00 pm)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2026/05/CN-No.-2026-0024.pdf"
  local_path: "pdfs/pse-cn-2026-0024-edge-cutoff-4pm.pdf"
  edition: in-force
  amended_through: "2026-05-22"
  note: "Effective 25 May 2026."
- slug: pse-cn-2026-0039-sec-market-making-rfc
  title: "CN-2026-0039 - Request for comments on SEC's proposed Rules on Market Making (SEC notice 14 Aug 2026)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2026/08/CN-No.-2026-0039.pdf"
  local_path: "pdfs/pse-cn-2026-0039-sec-market-making-rfc.pdf"
  edition: historical
  amended_through: "2026-08-20"
  note: "Draft only; comments due 28 Aug 2026."
- slug: pse-cn-2026-0041-declassification-price-suspension
  title: "Declassification of shares - price adjustment and trading suspension mechanics (circular of 10 Sep 2026)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2026/09/2026-0041-Declassification-Price-Adjustment-and-Trading-Suspension-Mechanics.pdf"
  local_path: "pdfs/pse-cn-2026-0041-declassification-price-suspension.pdf"
  edition: in-force
  amended_through: "2026-09-10"
  note: "Follows SEC mandate on Class A/B declassification (CN-2025-0035/0036)."
- slug: pse-eod-daily-quotation-2026-09-30
  title: "PSE Daily Quotation Report, 30 September 2026"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/market_report/September%2030,%202026-EOD.pdf"
  local_path: "pdfs/pse-eod-daily-quotation-2026-09-30.pdf"
  edition: historical
  amended_through: "2026-09-30"
  note: "Archived by another researcher. Page 3: ABG (Asiabest) open 60.00, high 60.85, low/close 42.60, no bid, 545,270 shares (a -30% floor close)."
- slug: pse-fix-specification-v2-5
  title: "PSE FIX Specification for X-stream, v2.5 (OMX Technology AB)"
  publisher: "OMX Technology AB / PSE"
  type: pdf
  canonical_url: "https://www.pse.com.ph/%20(PSEtrade%20XTS%20-%20Fix%20Gateway%20page;%20direct%20PDF%20URL%20not%20captured)"
  local_path: "pdfs/pse-fix-specification-v2-5.pdf"
  edition: superseded
  amended_through: "2015-08-10"
  note: "Legacy X-stream spec; the NTE Eqlipse FIX spec (released Jul 2026) is not archived here."
- slug: pse-implementing-guidelines-trading-rules
  title: "Implementing Guidelines of the Revised Trading Rules (Annex A to PSE Memo No. 2010-0340)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2021/04/Implementing-Guidelines-of-the-Revised-Trading-Rules.pdf"
  local_path: "pdfs/pse-implementing-guidelines-trading-rules.pdf"
  edition: in-force
  amended_through: "2010-07-22"
  note: "Base text effective 26 Jul 2010; Part II hours, Part VI.2(b), Part XX and others amended by TPA-2011-0124, CN-2020-0028, CN-2020-0044 (new circuit-breaker part), CN-2025-0037 (Part XXI), VWAP rules (Part XXV). Security Halt and Suspension Matrix on p.28 is an image."
- slug: pse-itch-equities-feed-spec-v2-3
  title: "PSE Equities Feed Specification v2.3 (ITCH, for X-stream)"
  publisher: "The Philippine Stock Exchange (content copyright OMX Technology AB 2014)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2024/03/PSE_Equities_Feed_Specification_v2.3.pdf"
  local_path: "pdfs/pse-itch-equities-feed-spec-v2-3.pdf"
  edition: in-force
  amended_through: "2018-10-05"
  note: "Legacy PSEtrade XTS feed spec (content copyright OMX Technology AB 2014); valid until the NTE cut-over scheduled for 23 Nov 2026 (the Eqlipse feed spec is not public). Archived by another researcher. Message [k] (collars, CB limits) p.12-13; Trading Action [H] and reasons p.13-14; system events p.10."
- slug: pse-listing-disclosure-rules
  title: "Consolidated Listing and Disclosure Rules (Article VII Disclosure Rules; Article VIII Penalties; Art. III Part G)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2025/01/Consolidated-Listing-and-Disclosure-Rules-Updated-011025.pdf"
  local_path: "pdfs/pse-listing-disclosure-rules.pdf"
  edition: in-force
  amended_through: "2025-01-10"
  note: "Cover says 'Published as of January 2025'; PSE listing page titles it 'Updated 01/10/25'. Later changes not systematically checked; known superseding item: EDGE cut-off now 4:00 pm (CN-2026-0024). Article VII page n = physical n+137; Article VIII page n = physical n+158."
- slug: pse-memo-extended-pre-close-implementation-2013
  title: "Implementation of Extended Pre-Close Period (TPA 2013-0165, 14 Oct 2013)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/AnnouncementOPSPDF/Implementation%20of%20Extended%20Pre-Close%20Period.pdf"
  local_path: "pdfs/pse-memo-extended-pre-close-implementation-2013.pdf"
  edition: superseded
  amended_through: "2013-10-14"
  note: "Effective 4 Nov 2013: pre-close 15:15, run-off 15:20, close 15:30 (the pre-pandemic schedule). Archived by another researcher."
- slug: pse-memo-new-trading-hours-2011
  title: "PSE New Trading Hours (TPA 2011-0108, 6 Dec 2011)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/AnnouncementOPSPDF/PSE%20New%20Trading%20Hours.pdf"
  local_path: "pdfs/pse-memo-new-trading-hours-2011.pdf"
  edition: superseded
  amended_through: "2011-12-06"
  note: "Whole-day schedule effective 2 Jan 2012: resume 13:30, pre-close 15:17, close 15:30. Archived by another researcher."
- slug: pse-memo-sec-approved-dma-rules-2013-11-26
  title: "PSE Rules on Direct Market Access (DMA) with PSE memo of 26 Nov 2013 and SEC letter of 29 Oct 2013"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/AnnouncementOPSPDF/SEC-Approved%20Direct%20Market%20Access%20(DMA)%20Rules.pdf"
  local_path: "pdfs/pse-memo-sec-approved-dma-rules-2013-11-26.pdf"
  edition: in-force
  amended_through: "2013-11-26"
  note: "Scanned (read by OCR). Effective first trading day of 2014; this 14-page copy has the cover memo as p.1, so rule pages = pse-dma-rules page + 1."
- slug: pse-memo-trading-days-suspensions-guidelines-2012
  title: "TPA 2012-0122 - Trading days and suspensions guidelines (9 Aug 2012)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/AnnouncementOPSPDF/Trading%20Days%20and%20Suspensions%20Guidelines.pdf"
  local_path: "pdfs/pse-memo-trading-days-suspensions-guidelines-2012.pdf"
  edition: in-force
  amended_through: "2012-08-09"
  note: "Quotes RTR Art. II s1."
- slug: pse-nte-broker-forum-2026-07-09
  title: "New Trading Engine, PSETradeX, back-office - Broker Forum (9 Jul 2026)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2026/07/PSE-New-Trading-Engine-TradeX-Back-office_Broker-Forum_07092026-1.pdf"
  local_path: "pdfs/pse-nte-broker-forum-2026-07-09.pdf"
  edition: in-force
  amended_through: "2026-07-09"
  note: "Go-live 23 Nov 2026; negotiated trades."
- slug: pse-nte-faq-2026-08
  title: "New Trading Engine FAQs (Aug 2026)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://www.pse.com.ph/pse-new-trading-engine/?tab=faqs"
  local_path: "pdfs/pse-nte-faq-2026-08.pdf"
  edition: in-force
  amended_through: undated
  note: "Published on the PSE NTE FAQs tab; direct PDF URL not captured; archived by a parallel researcher."
- slug: pse-nte-user-group-2026-01-15
  title: "New Trading Engine user group deck (15 Jan 2026; PSE re-upload June 2026)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2026/06/NTE-User-Group.pdf"
  local_path: "pdfs/pse-nte-user-group-2026-01-15.pdf"
  edition: in-force
  amended_through: "2026-01-15"
  note: "Run-off rule change; lot/tick tables."
- slug: pse-revised-trading-rules
  title: "Revised Trading Rules (Annex B to PSE Memorandum No. 2010-0275)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2021/04/Revised-Trading-Rules.pdf"
  local_path: "pdfs/pse-revised-trading-rules.pdf"
  edition: in-force
  amended_through: "2010-06-08"
  note: "Scanned base text (SEC approval letter 1 Jun 2010; effective on launch of the New Trading System, 26 Jul 2010). Partly superseded: Art. II/IV s13-14/VI s3/VIII s2 by TPA-2011-0110 (Jan 2012), Art. IV s7(b) by CN-2020-0028, Art. VIII s1 by CN-2020-0044, Art. VIII s2(a) by CN-2025-0037. Read by OCR + visual check."
- slug: pse-short-selling-guidelines-2023-10
  title: "PSE Guidelines on Short Selling Transactions (as of October 2023, v3)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2024/05/PSE-Guidelines-on-Short-Selling-Transactions_Oct2023_v3.pdf"
  local_path: "pdfs/pse-short-selling-guidelines-2023-10.pdf"
  edition: in-force
  amended_through: "2023-10-16"
  note: "Supersedes the Jan 2019 version (kb: pse-short-selling-guidelines). Eligible-security criteria revised 16 Oct 2023."
- slug: pse-tpa-2011-0110-amended-revised-trading-rules
  title: "TPA 2011-0110 - SEC-approved amendments to the Revised Trading Rules (Art. II, IV s13-14, VI s3, VIII s2)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/AnnouncementOPSPDF/SEC%20Approved%20Amendments%20to%20PSE%20Revised%20Trading%20Rules.pdf"
  local_path: "pdfs/pse-tpa-2011-0110-amended-revised-trading-rules.pdf"
  edition: in-force
  amended_through: "2011-12-07"
  note: "Scanned; SEC letter 25 Oct 2011; effective Jan 2012. Read by OCR. Partly superseded (hours changed 2013, 2021-22, 2024; Art. VIII s2(a) 2025)."
- slug: pse-tpa-2011-0124-amended-implementing-guidelines
  title: "TPA 2011-0124 - Amended sections of the Implementing Guidelines (hours, Part XX Market Halt)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/AnnouncementOPSPDF/Amended%20Sections%20of%20the%20Implementing%20Guidelines%20of%20the%20Revised%20trading%20Rules.pdf"
  local_path: "pdfs/pse-tpa-2011-0124-amended-implementing-guidelines.pdf"
  edition: in-force
  amended_through: "2011-12-28"
  note: "Scanned; effective with the Jan 2012 hours. Read by OCR and visual check of p.4."
- slug: pse-tpa-2012-0005-cmic-commencement
  title: "TPA 2012-005 - Commencement of operations of the Capital Markets Integrity Corporation"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/AnnouncementOPSPDF/Commencement%20of%20Operations%20of%20the%20Capital%20Markets%20Integrity%20Corporation.pdf"
  local_path: "pdfs/pse-tpa-2012-0005-cmic-commencement.pdf"
  edition: n/a
  amended_through: "2012-03-15"
  note: "Scanned (OCR)."
- slug: pse-tpa-2012-0049-cmic-authority-to-commence
  title: "TPA 2012-0049 - Authority to commence operations granted to CMIC and effectivity of CMIC Rules"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/AnnouncementOPSPDF/Authority%20to%20commence%20operations%20granted%20to%20CMIC%20and%20effectivity%20of%20CMIC%20Rules.pdf"
  local_path: "pdfs/pse-tpa-2012-0049-cmic-authority-to-commence.pdf"
  edition: n/a
  amended_through: "2012-03-13"
  note: "Scanned (OCR)."
- slug: pse-tpa-2012-0099-cmic-reminder-art-xib-sec-8-manipulation
  title: "TPA 2012-0099 - CMIC reminder on Art. XI-B s8 (executing orders to avoid manipulation)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/AnnouncementOPSPDF/Reminder%20on%20compliance%20with%20CMIC%20Rules%20Article%20XI-B,%20Section%208.pdf"
  local_path: "pdfs/pse-tpa-2012-0099-cmic-reminder-art-xib-sec-8-manipulation.pdf"
  edition: n/a
  amended_through: "2012-06-20"
  note: "Scanned (OCR)."
- slug: pse-tpa-2012-0177-cmic-disciplinary-actions-2012-10-19
  title: "TPA 2012-0177 - Publication of CMIC disciplinary actions (19 Oct 2012)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/AnnouncementOPSPDF/Publication%20of%20CMIC%20Disciplinary%20Actions%20.pdf"
  local_path: "pdfs/pse-tpa-2012-0177-cmic-disciplinary-actions-2012-10-19.pdf"
  edition: n/a
  amended_through: "2012-10-19"
  note: "Scanned (OCR); Annex C = investigation sanctions."
- slug: pse-tpa-2020-0052-phr-static-threshold-lift
  title: "TPA 2020-0052 - PH Resorts Group Holdings: lifting of static threshold"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2023/02/TPA_2020-0052.pdf"
  local_path: "pdfs/pse-tpa-2020-0052-phr-static-threshold-lift.pdf"
  edition: n/a
  amended_through: "2020-10-30"
  note: "Example of RTR Art. VII s6."
- slug: pse-tpa-2025-0050-mount-peak-involuntary-suspension
  title: "TPA 2025-0050 - Mount Peak Securities, Inc. - involuntary suspension (CMIC memo 2025-024)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/TPA-2025-0050.pdf"
  local_path: "pdfs/pse-tpa-2025-0050-mount-peak-involuntary-suspension.pdf"
  edition: n/a
  amended_through: "2025-08-13"
  note: "CMIC Rules Art. X s7 action."
- slug: pse-tpa-2026-0002-dynamic-threshold-review
  title: "TPA 2026-0002 - Dynamic threshold semi-annual review (effective 2 Feb 2026)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2026/01/TPA-2026-0002.pdf"
  local_path: "pdfs/pse-tpa-2026-0002-dynamic-threshold-review.pdf"
  edition: superseded
  amended_through: "2026-01-19"
  note: "Superseded by TPA-2026-0036."
- slug: pse-tpa-2026-0035-benjamin-co-ca-involuntary-suspension
  title: "TPA 2026-0035 - Benjamin Co Ca & Company, Inc. - involuntary suspension (CMIC memo 2026-015)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/TPA-2026-0035.pdf"
  local_path: "pdfs/pse-tpa-2026-0035-benjamin-co-ca-involuntary-suspension.pdf"
  edition: n/a
  amended_through: "2026-07-31"
  note: "CMIC Rules Art. X s7 action."
- slug: pse-tpa-2026-0036-dynamic-threshold-review
  title: "TPA 2026-0036 - Dynamic threshold semi-annual review (effective 7 Aug 2026)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/TPA-2026-0036.pdf"
  local_path: "pdfs/pse-tpa-2026-0036-dynamic-threshold-review.pdf"
  edition: in-force
  amended_through: "2026-08-03"
  note: "Cluster list on p.2 is an image."
- slug: pse-web-investing-at-pse
  title: "PSE web page 'Investing at PSE' (investor FAQ)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: web
  canonical_url: "https://www.pse.com.ph/investing-at-pse/"
  local_path: null
  edition: n/a
  amended_through: undated
  note: "Undated and stale (50% floor; 3:30 pm close) but describes CMIC/TMS surveillance; accessed 2026-10-06."
- slug: pse-web-press-2020-03-21-static-threshold
  title: "PSE press release: lower static threshold reduced from 50% to 30% (21 Mar 2020)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: web
  canonical_url: "https://www.pse.com.ph/?p=9405"
  local_path: null
  edition: n/a
  amended_through: "2020-03-21"
  note: "Primary (PSE press room)."
- slug: pse-web-press-2020-04-30-circuit-breaker
  title: "PSE press release: new three-level circuit breaker operational 4 May 2020 (30 Apr 2020)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: web
  canonical_url: "https://www.pse.com.ph/?p=9409"
  local_path: null
  edition: n/a
  amended_through: "2020-04-30"
  note: "Primary (PSE press room); states the old breaker's trip dates."
- slug: pse-web-regulation-trading-participants
  title: "PSE web page 'Regulation - Trading Participants' (list of trading rules documents)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: web
  canonical_url: "https://www.pse.com.ph/regulation-trading-participants/"
  local_path: null
  edition: n/a
  amended_through: undated
  note: "Lists the 2010 base rules plus amending memos; accessed 2026-10-06 (no algorithmic-trading rule listed)."
- slug: ra-8799-src
  title: "Republic Act No. 8799, The Securities Regulation Code (PSE-hosted PDF)"
  publisher: "Republic of the Philippines (copy hosted by PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2021/04/Securities-Regulation-Code-1.pdf"
  local_path: "pdfs/ra-8799-src.pdf"
  edition: in-force
  amended_through: undated
  note: "Enacted 19 Jul 2000; hosted copy undated; later statutory amendments not checked."
- slug: rappler-2025-05-19-vista-land-lifted
  title: "PSE lifts trading suspension on 2 Villar firms following annual report submission (headline only)"
  publisher: "Rappler"
  type: web
  canonical_url: "https://www.rappler.com/business/vista-land-trading-suspension-lifted-philippine-stock-exchange-may-19-2025/"
  local_path: null
  edition: n/a
  amended_through: "2025-05-19"
  note: "Headline only; site blocks automated access."
- slug: sec-2015-src-irr
  title: "2015 Implementing Rules and Regulations of the Securities Regulation Code (2015 SRC Rules)"
  publisher: "Securities and Exchange Commission (Philippines)"
  type: pdf
  canonical_url: "https://appointment.sec.gov.ph/wp-content/uploads/2019/11/2015IRR_RA9799.pdf"
  local_path: "pdfs/sec-2015-src-irr.pdf"
  edition: in-force
  amended_through: "2015-11-09"
  note: "As issued, effective 9 Nov 2015; post-2015 SEC amendments not reconciled (SEC reportedly issued an annotated consolidated reference in May 2026 - not retrieved)."
- slug: sec-2015-src-irr-notice-of-effectivity
  title: "SEC Notice - Effectivity of the 2015 SRC Rules on 9 November 2015"
  publisher: "Securities and Exchange Commission (Philippines)"
  type: pdf
  canonical_url: "https://appointment.sec.gov.ph/wp-content/uploads/2019/11/2015-SRC-Rules-Notice-of-Effectivity-of-SRC-IRR-Nov-09-2015.pdf"
  local_path: "pdfs/sec-2015-src-irr-notice-of-effectivity.pdf"
  edition: n/a
  amended_through: "2015-11-05"
  note: "Publication 25 Oct 2015 (Manila Bulletin, Philippine Star)."
- slug: wealthinsights-2025-03-24-tech-glitches
  title: "Philippine stock exchange's tech glitches may dent foreign investor confidence (BusinessWorld syndication)"
  publisher: "Metrobank Wealth Insights / BusinessWorld"
  type: web
  canonical_url: "https://wealthinsights.metrobank.com.ph/bworldonline/phl-stock-exchanges-tech-glitches-may-dent-foreign-investor-confidence/"
  local_path: null
  edition: n/a
  amended_through: "2025-03-24"
  note: "Secondary; read via fetch-tool summary."
```
