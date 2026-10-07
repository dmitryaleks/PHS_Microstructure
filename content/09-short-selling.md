---
number: 9
slug: short-selling
title: Short Selling, Lending, Margin and Hedging
summary: Short selling has been legal in 52 names since 6 Nov 2023 yet every daily report shows zero volume; borrow, margin and hedging routes are partial, pending or offshore.
part: Liquidity and shorting
---

Short selling on the PSE is fully specified, technically live since 6 November 2023, and unused. **Every Daily Short Sell Report from the go-live day to 5 October 2026 (710 index entries, 707 distinct files) shows TOTAL VOLUME 0.** MSCI's June 2026 accessibility review says the programme "is not yet an established market practice".[^pse-dssr-2023-11-06:2][^pse-dssr-2026-10-05:2][^pse-market-reports-dssr][^msci-accessibility-review-2026:43] The exchange rules are not the obstacle: an eligible list of 52 securities, a 10% short-interest cap, an uptick test, day orders, borrow-before-sale and a daily public report are all in force.[^pse-short-selling-guidelines-2023-10:1] What is missing is plumbing: a BIR-registered securities lending agreement for each borrower, a lending pool (PDTC's first participants were onboarded only in April and May 2026), broker back offices built for long-only clients, and, for foreign funds, an offshore lending route that has awaited SEC approval since 16 April 2026.[^pse-cn-2026-0022:1-2][^pse-press-2026-06-15-reforms]

The rest of the chapter follows the same pattern. Margin is a broker product under an SEC rule that caps credit at 50% of market value (a 60% replacement was exposed on 25 August 2026); no derivative on PSE equities is listed; and a foreign investor's index hedge has to be offshore. Three assumptions break on contact with the record: that "legal" means "available at scale", that a foreign lending agreement can be used today, and that a PSEi future exists.

## Status board on 6 October 2026

| Item | Status | Key dates | Evidence |
|---|---|---|---|
| Short-selling programme | **Live in rules and systems; zero volume.** 52 eligible securities (51 stocks plus FMETF) on 5 Oct 2026 | Guidelines effective 2 Oct 2023; go-live 6 Nov 2023 | [^pse-cn-2023-0048:2][^pse-cn-2023-0056:1][^pse-dssr-2026-10-05:1-2] |
| SBL, onshore | **Live.** PDTC lending pool onboarded its first lenders and borrowers (cash collateral) | Rules effective 15 Feb 2007; PDS memo 03-2026 of 22 Apr 2026; PSE circular CN-2026-0022 dated 6 May 2026 (listed elsewhere as 18 May 2026) | [^pse-sbl-short-selling-webinar-2023:3][^pse-cn-2026-0022:1-2] |
| MSLA clearance through PSE (one-stop shop) | **In force**, effective immediately | SEC-approved 15 May 2026; PSE memo 22 May 2026 | [^pse-cn-2026-0025:1-2][^pse-msla-clearance-guidelines-2026:1-4] |
| SBL for foreign lenders and borrowers (offshore GMSLA, "directed pooled lending") | **Pending SEC approval** | Consulted 3-18 Feb 2026; filed with the SEC 16 Apr 2026; PSE still "awaiting approval" 4 Jul and 17 Aug 2026 | [^pse-cn-2026-0009:1][^pse-press-2026-06-15-reforms][^pse-asm-2026-president-report:22][^pse-analyst-briefing-1h-2026:9] |
| Margin, SRC Rule 48.1 | **In force (old text):** credit up to 50%, maintenance 25% long / 30% short. Replacement draft **not adopted** | Draft exposed 25 Aug 2026; comments closed 15 Sep 2026 | [^sec-2015-src-irr:165][^sec-rfq-2026-src-rule-48-1-margin:1] |
| Index futures and any listed derivative | **Not launched; no SEC-approved rules** | Plan slipped from "2026"; RFI Jul 2026; funding talks Aug 2026 | [^pse-asm-2024-presidents-report:25][^pse-analyst-briefing-1h-2026:10] |
| Structured warrants | **SEC draft only** | Exposed 28 Apr 2026; comments to 13 May 2026 | [^pse-cn-2026-0018:2] |
| GPDRs (peso receipts on foreign stocks) | **Pending SEC approval** of revised rules | Submitted 24 Jun 2026, approval "targeted within the quarter" | [^pse-analyst-briefing-1h-2026:10] |
| New trading engine (Nasdaq Eqlipse) | Scheduled; not live | Go-live 23 Nov 2026 | [^pse-nte-broker-forum-2026-07-09:9] |

PSE's press-room feed (ten latest items, newest 2 October 2026) shows nothing on SBL approval, GPDRs or derivatives after 14 August 2026, but circulars CN-2026-0036 to -0042 could not be retrieved, so a later announcement cannot be excluded.[^pse-press-feed]

## The short-selling regime

### Legal stack and dates

| Date | Event |
|---|---|
| 9 Jun 2006 | SEC Memorandum Circular 7, series of 2006: Rules on Securities Borrowing and Lending[^sec-mc-7-2006-sbl-rules:15] |
| 23 Jun 2006 | BIR Revenue Regulations 10-2006, tax treatment of SBL[^bir-rr-10-2006-sbl:1] |
| 16 Nov 2006; 5 Feb 2007; 15 Feb 2007 | SEC approves the PSE SBL Rules; PSE issues SBL Guidelines; both take effect[^pse-sbl-short-selling-webinar-2023:3] |
| 8 Jun 2010 | Revised Trading Rules published with short-selling provisions (Article IV, Section 5); effective with the new trading system on 26 Jul 2010[^pse-sbl-short-selling-webinar-2023:3][^pse-implementing-guidelines-trading-rules:1] |
| 9 Nov 2015 | 2015 SRC IRR effective: Rule 24.2-2 (short sales) and Rule 48.1 (margin)[^sec-2015-src-irr-notice-of-effectivity:1] |
| 5 Jun 2018; 22 Jun 2018 | SEC approves; PSE publishes the Guidelines for Short Selling Transactions (eligible: PSEi plus ETFs)[^pse-sbl-short-selling-webinar-2023:3][^pse-short-selling-guidelines:1] |
| 22-23 Jan 2019 | Short orders barred only in Pre-Open and Pre-Close; run-off removed from the bar (CN-2019-0004 of 23 Jan 2019)[^pse-cn-2019-0004-short-selling-guidelines-amendment:1] |
| 10 / 25 Feb 2020 | CMIC Implementing Guidelines on SBL and Short Selling: memo dated 10 Feb 2020, effective 25 Feb 2020[^cmic-sbl-short-selling-guidelines:1] |
| 24 May 2023 | SEC accepts offshore collateral for SBL with a foreign party[^pse-cn-2023-0048:2] |
| 21 Jul 2023 | PDTC receives the SEC's conditional approval to act as lending agent[^pse-sbl-short-selling-webinar-2023:3] |
| 6 Sep 2023 (BIR letter); 25 Sep 2023 (PSE says it received the confirmation) | BIR confirms it may register a GMSLA[^pse-cn-2023-0048:1][^pse-sbl-short-selling-webinar-2023:3] |
| 2 Oct 2023 | Short Selling Guidelines "take effect immediately"; MidCap and Dividend Yield constituents added to the eligible set (the Guidelines clause is marked "revised October 16, 2023")[^pse-cn-2023-0048:2][^pse-short-selling-guidelines-2023-10:1] |
| 19 Oct 2023 | Go-live moved from 23 Oct to 6 Nov 2023; front-end systems must be re-certified to tag short orders[^pse-cn-2023-0056:1] |
| 6 Nov 2023 | Programme go-live; first Daily Short Sell Report lists 53 eligible securities, all at zero[^pse-dssr-2023-11-06:1-2] |

The "effective" date (2 October 2023), the "go-live" date (6 November 2023, first announced as 23 October) and the SEC approval (5 June 2018) are three different dates; PSE's announcement index misdates the 2018 memo as 22 July when the memo itself is dated 22 June 2018.[^pse-cn-2018-0035-short-selling-guidelines-sec-approved:1] PSE's own staff note that "the governing laws and rules on short-selling have been in place since 2010" and that implementation awaited the new trading system and the SBL programme.[^pse-tpa-2023-0031:5]

### Rules in force

| Rule | Parameter |
|---|---|
| Eligible securities | All PSEi member companies, ETFs, MidCap Index constituents and Dividend Yield Index constituents; the Exchange may amend the criteria[^pse-short-selling-guidelines-2023-10:1] |
| Eligible-list size | 52 on 5 Oct 2026 (51 stocks plus FMETF); 53 at launch (52 stocks plus FMETF); nine more names flagged "B", buy-back only[^pse-dssr-2026-10-05:1-2][^pse-dssr-2023-11-06:1] |
| Short-interest cap | Short Interest Ratio **at or below 10%** of outstanding shares; above it the security is ineligible until the ratio falls back; monitored daily; changes announced at end of day and effective the next trading day; changing the 10% needs prior SEC approval[^pse-short-selling-guidelines-2023-10:1] |
| Price test | Uptick or zero-plus rule, SRC Rule 24.2-2.5 and Revised Trading Rules Art. IV s.5.2(b): the sale must be at a price higher than the last sale, or at the last-sale price if that price is above the next preceding different sale price that day[^sec-2015-src-irr:71][^pse-short-selling-guidelines-2023-10:2][^pse-revised-trading-rules:18-20] |
| Exemption from the price test | A sale "due to a bona fide market-making or arbitrage activity executed by a broker dealer authorized to engage in such activities", unless the SEC provides otherwise[^sec-2015-src-irr:71] |
| Order validity | **Day orders only**; no aggregation of short orders[^pse-short-selling-guidelines-2023-10:2] |
| Phases | Not accepted in **Pre-Open** and **Pre-Close**: the Revised Trading Rules say a short order "is valid only for one (1) Trading Day" and short sales "are not allowed during the Pre-Open and Pre-Close Periods"; the Guidelines carry the same bar since 22 Jan 2019 (SRC Rule 40.3.3); see the run-off conflict below[^pse-revised-trading-rules:19][^pse-short-selling-guidelines-2023-10:2][^pse-cn-2019-0004-short-selling-guidelines-amendment:1] |
| Venues and sizes | **No orders for the odd-lot market or for block sales**[^pse-short-selling-guidelines-2023-10:2] |
| Who enters | Only trading participants enter short orders; clients route through them; a DMA client may enter its own only if the participant can verify the borrow before entry and the Exchange's conditions are met[^pse-short-selling-guidelines-2023-10:2] |
| Flagging | The participant must flag every short order; the system rejects short orders in ineligible securities; **FIX tag 54 Side = 5 (Short Sell)**; a trade may not be amended from a short sale to a regular sale or back[^pse-short-selling-guidelines-2023-10:2][^pse-short-selling-guidelines-2023-10:3][^pse-fix-specification-v2-5:53] |
| Borrow before sale ("naked-short ban") | The Trading Rules bar a participant from placing a short order, for principal or client, without (a) borrowing the securities before the sale, (b) a prior SBL agreement ensuring the securities are available for delivery on settlement date, or (c) an exercisable and unconditional right to vest the securities in the purchaser on settlement date; the Guidelines add that the participant must determine before entry that the client has entered into the necessary borrowing arrangements and that SEC and PSE SBL compliance is how the prohibition is met; the SRC rule is stricter in wording and requires a determination that the customer "has already borrowed the security"[^pse-revised-trading-rules:19][^pse-short-selling-guidelines-2023-10:2][^pse-short-selling-guidelines-2023-10:3][^sec-2015-src-irr:70] |
| Client paperwork and records | Before a short sale the customer executes a notarised undertaking acknowledging the short-selling rules and the naked-short ban; short sales are booked to the customer's ledger, not the error account; orders and confirmations are marked "short"; an authorisation letter from a lending client is not enough to prove compliance; borrow and return are recorded with stock credit and debit memos[^cmic-sbl-short-selling-guidelines:2][^cmic-sbl-short-selling-guidelines:3] |
| Same-broker buy-back | The affidavit of undertaking (individual and company forms) commits the client to use **the same trading participant** that executed the short for any buy-back of those shares, and to give that participant the MSLA, the SLAA (lending client and agent-lender participant), service agreements (borrowing client and agent-borrower participant) and a confirmation notice for every short sale[^cmic-sbl-short-selling-guidelines:10][^cmic-sbl-short-selling-guidelines:13] |
| Mandatory close-out | A short sale not delivered within the settlement period must be closed by the broker-dealer, by purchase, on the next business day after the settlement date (written notice to the Exchange and SEC if justifiably impossible)[^sec-2015-src-irr:71] |
| Insiders | Directors, officers and principal stockholders may not short their own company[^sec-2015-src-irr:71] |
| Daily disclosure | The Exchange publishes the Daily Short Sell Report by the end of each trading day, with short volume, value and Short Interest Ratio for each eligible security; depository participants file daily SBL movement reports[^pse-cn-2023-0056:1][^pse-short-selling-guidelines-2023-10:1][^pse-tpa-2023-0031:5] |
| Position reporting | Participants compute each account's aggregate short position per security as of the 15th and last day of each month and file it with CMIC within two days[^cmic-sbl-short-selling-guidelines:5] |
| Exchange and SEC powers | PSE may restrict or prohibit short selling "indefinitely or for such period as it may deem necessary or advisable", with due notice to the SEC; suspend short selling in a particular security (participants duly notified), remove it from the eligible list, limit the number of shares that may be sold short, require a participant to cease shorting (temporarily or permanently) or to liquidate open short positions, and require disclosure to PSE and the SEC of open short positions or the value of borrowed securities sold short; the SEC may itself prohibit short selling "indefinitely or for such period as it may deem proper"[^pse-revised-trading-rules:19][^pse-revised-trading-rules:20][^sec-2015-src-irr:71] |
| Penalties | Article IX of the Revised Trading Rules; CMIC treats naked short selling, uptick violations and insider short sales as major violations[^pse-short-selling-guidelines-2023-10:4][^cmic-sbl-short-selling-guidelines:6-7] |

<div class="callout warn">
<span class="label">Conflict: is the run-off phase barred?</span>

The 2018 Guidelines barred short orders in Pre-Open, Pre-Close **and Run-Off/Trading-at-Last**. CN-2019-0004 (23 January 2019) removed run-off "to match system configuration" and SRC Rule 40.3.3, stating that the trading system rejects short orders only in Pre-Open and Pre-Close, and the October 2023 text carries that wording.[^pse-cn-2019-0004-short-selling-guidelines-amendment:1][^pse-short-selling-guidelines-2023-10:2] PSE's undated SBL and Short Selling web page, however, still lists run-off (trading-at-last) among the barred phases.[^pse-sbl-short-selling-page] The primary text, latest dated, says pre-open and pre-close only; the conflict is unresolved. Design for no short orders in run-off unless a broker confirms otherwise. The same web page also shows a stale eligibility FAQ (PSEi and ETFs only) and still quotes a T+3 recall cycle; the settlement cycle has been T+2 since 24 August 2023.[^pse-cn-2023-0031-t2-settlement:1]
</div>

A numbering note: the Guidelines point to "Section 3 of SRC Rule 24.2-2", the pre-2015 numbering, while the 2015 IRR numbers the same test 24.2-2.5, as PSE's FAQ does.[^sec-2015-src-irr:71]

### The price test, worked

Define the last sale L and the next preceding different sale price D (both for the same day). A short sale at price p is allowed if p > L, or if p = L and L > D.

| Sales that day, in order | L | D | Short allowed at |
|---|---|---|---|
| 99.90, then 100.00 (plus tick) | 100.00 | 99.90 | 100.00 or higher (p = L and L > D) |
| 99.90, 100.00, 100.00 (zero-plus tick) | 100.00 | 99.90 | 100.00 or higher |
| 100.00, then 99.90 (minus tick) | 99.90 | 100.00 | 99.95 or higher (one tick above L); not at 99.90 |
| 100.00, 99.90, 99.90 (zero-minus tick) | 99.90 | 100.00 | 99.95 or higher; not at 99.90 |

PSE's FAQ gives the plus-tick case in words: after a last sale of PHP 1.00, a short sale must be at 1.01 or higher.[^pse-sbl-short-selling-page] The rules do not define "last sale" for auction prints, odd-lot trades or block trades, nor say whether the engine applies the test when the order is entered or when it matches.

### Eligible securities on 5 October 2026

Fifty-two securities carry the flag "Y" (short sale and buy-back eligible): AC, ACEN, AEV, AGI, ALI, APX, AREIT, BDO, BLOOM, BPI, CBC, CNPF, CNVRG, COSCO, CREIT, DMC, DNL, EMI, GLO, GSMI, GTCAP, ICT, JFC, JGS, KEEPR, LTG, MBT, MEG, MER, MONDE, MREIT, MWC, MYNLD, NIKL, OGP, PGOLD, PLUS, PNB, PX, RCR, RLC, SCC, SECB, SEVN, SGP, SM, SMC, SMPH, TEL, URC and WLCON (51 stocks) plus the ETF FMETF. Nine former eligibles are flagged "B" (buy-back only): AUB, CEB, DD, DDMPR, FCG, FILRT, GMA7, PCOR and SHLPH.[^pse-dssr-2026-10-05:1-2] The same 52 appear on PSE's live eligible-list page.[^pse-short-selling-eligible-list] The list follows index membership, which changes at the February and August reviews ([Chapter 11](#/ch/market-data)); a name that leaves the indices can be moved to buy-back only on the next trading day. The orderbook-restrictions message in the legacy ITCH specification carries a Short Sell Eligible flag per book.[^pse-itch-equities-feed-spec-v2-3:12]

### Actual usage: none

<div class="callout">
<span class="label">Consequence</span>

**No short sale has ever been reported.** PSE's report index lists 710 Daily Short Sell Report entries (707 distinct files, three file names reused) from 6 November 2023 to 5 October 2026, and every one of the 707 files retrieved shows "TOTAL VOLUME: 0 / TOTAL VALUE: 0.00" and a "NULL" short-interest ratio for every security.[^pse-market-reports-dssr] Only the first and the latest reports are archived in this knowledge base.[^pse-dssr-2023-11-06:2][^pse-dssr-2026-10-05:2] Treat shorting PSE stocks onshore as unproven plumbing, not a tradable strategy.
</div>

| Date | Evidence |
|---|---|
| 6 Nov 2023 | First Daily Short Sell Report: 53 eligible names, volume 0[^pse-dssr-2023-11-06:1-2] |
| 6 Feb 2024 | BusinessWorld (citing Bloomberg data): local brokers' back ends and client systems are "configured for a long-only market", many investors do not understand the set-up, and some local brokerages planned to offer shorting "by June" 2024; reported by BusinessWorld, no PSE document[^bworld-2024-02-06-short-selling-demand] |
| 12 Feb 2024 | BusinessWorld: PSE's CEO said the product "is really to target the foreign investors so that when the emerging market or the Philippine economy loses favor, instead of selling out, they can hedge" and "I don't expect short selling to take off in a big way right away because the market is down. Brokers have also to adopt their back office"[^bworld-2024-02-12-short-selling-recovery] |
| 19 Feb 2024 | Philstar commentary: "There have been zero short-selling transactions"; agreements among the parties not yet signed[^philstar-2024-02-19-merkado-barkada] |
| Jun 2026 | MSCI Global Market Accessibility Review: the programme "was implemented in November 2023. However, it is not yet an established market practice"[^msci-accessibility-review-2026:43] |
| 2 Jul 2026 | PSE's CEO (Philstar): the revised SBL rules "address all regulatory hurdles to short selling"[^philstar-2026-07-02-short-selling] |
| 5 Oct 2026 | Latest report: total volume 0, 52 eligible names[^pse-dssr-2026-10-05:2] |

The daily report is the only public statistic, so an unreported short sale cannot be excluded.

### Execution implications

- **Order entry.** FIX Side = 5 on the legacy XTS specification (v2.5); the Eqlipse FIX specification is not public, so re-check before 23 November 2026. The legacy specification also lets an open order's side be amended to or from short sell, which is separate from the ban on amending an executed trade.[^pse-fix-specification-v2-5:26][^pse-nte-faq-2026-08:1]
- **Phases and validity.** Short orders only in continuous trading, as day orders, unaggregated, never in the odd-lot market or a block sale; treat run-off as barred.
- **Price test state.** An algorithm needs real-time last sale and last different sale and must reprice or cancel passive short offers as the last sale moves. Because the engine's entry-versus-match behaviour is unstated, design for rejection at entry and re-validate resting orders after every print.
- **Pre-trade checks.** Eligibility flag (ITCH orderbook restrictions, the daily report) and the "B" status; eligibility changes are announced at the end of the day and apply the next day; the engine rejects shorts in ineligible names.
- **Cover.** Buy-backs must go through the same trading participant; plan for the mandatory close-out the business day after settlement if delivery fails.
- **Cost.** 0.1% stock transaction tax on each short sale (sale leg only) plus the borrow fee and collateral cost; no public borrow-fee data exists ([Chapter 12](#/ch/costs)).
- **Lead time.** Plan weeks, not days: BIR-registered lending agreement, cash-collateral account, client undertakings and broker readiness.
- **Sizing.** Do not size strategies on short alpha in Philippine single names; use the routes in the derivatives section until shorts actually print.

## Securities borrowing and lending

### Framework

| Instrument | What it does |
|---|---|
| SEC Memorandum Circular 7, series of 2006 | Covers brokers, dealers, banks, insurers and others; lending agents must register with the SEC (fee PHP 50,000); direct lenders are limited to banks (including foreign-bank branches), investment houses, investment companies, insurers, government or BSP-authorised pension funds, securities dealers and others the SEC declares; loanable securities are exchange-listed securities and BTr/BSP securities in electronic form; foreigners may not borrow equities of nationalised-activity companies unless foreign ownership can be monitored; exchanges may adopt SEC-approved SBL programmes; fines of PHP 20,000, 30,000 and 50,000 per order or transaction, or twice the amount[^sec-mc-7-2006-sbl-rules:5][^sec-mc-7-2006-sbl-rules:6-7][^sec-mc-7-2006-sbl-rules:8][^sec-mc-7-2006-sbl-rules:13][^sec-mc-7-2006-sbl-rules:14-15] |
| PSE Rules on SBL (SEC-approved 16 Nov 2006, effective 15 Feb 2007) | Cover local and foreign borrowers and lenders; a trading participant, as principal or as "Agent-Facilitator", **must engage a Lending Agent** (2.01-2.02); a participant may not let a client lend if that creates negative risk-based-capital exposure (2.08); the Exchange may restrict or prohibit borrowing and lending of any listed share (3.01); for 12 months from effectivity participants could lend directly or through an agent, after which the SBL programme's requirements applied in full (6.01-6.03)[^pse-sbl-rules:2][^pse-sbl-rules:3][^pse-sbl-rules:4][^pse-sbl-rules:5] |
| PSE SBL Guidelines (issued 5 Feb 2007) | The confirmation notice states whether the lender is a direct lender or lending agent; participants file the BIR registration certificate with PSE within 15 days; daily marking to market; title and **voting rights pass to the borrower** unless a written proxy is executed; recall on prior notice within the normal settlement cycle; agent-facilitators identify principals before each transaction[^pse-sbl-guidelines:2][^pse-sbl-guidelines:3] |
| BIR RR 10-2006, as amended by RR 1-2008 (1 Feb 2008) and RR 10-2024 (5 Jun 2024) | Tax treatment and MSLA registration (below)[^bir-rr-10-2006-sbl:4][^bir-rr-1-2008-sbl:4][^pse-cn-2024-0035:1-2] |
| BSP Circular 611 (30 May 2008) | Foreign-exchange treatment of foreign borrowers (below)[^bsp-circular-611] |
| CMIC Implementing Guidelines (effective 25 Feb 2020) | Ledgers, ratios, position reports (15th and month-end) and penalties[^cmic-sbl-short-selling-guidelines:3][^cmic-sbl-short-selling-guidelines:5] |
| PSE 2026 Revised Guidelines for MSLA Clearance | Documents and timetable (below)[^pse-msla-clearance-guidelines-2026:1-4] |

Insurers may lend under an Insurance Commission circular letter (filed by PSE as IC CL 2019-45; its printed date is legible only as "04 September 20[18/19]").[^ic-cl-2019-45-sbl:1]

### Operating models

| Model | Structure |
|---|---|
| 1 | The trading participant lends its own proprietary shares to its client under an MSLA[^pse-sbl-models-2023:1] |
| 2 | The participant is a registered lending agent: SLAA with each client lender, one multilateral MSLA with client borrowers[^pse-sbl-models-2023:2] |
| 3 | Different participants on each side: an Agent-Facilitator signs an SLAA with its client and with the Lending Agent; the borrowing participant signs a service agreement with its client and an MSLA with the Lending Agent[^pse-sbl-models-2023:3] |
| 4 (foreign client borrowers) | The Lending Agent signs the MSLA with the foreign borrower; shares go to the borrower's custodian bank through EQ Trade; the borrower gives the selling broker the MSLA and confirmation notice as proof the short is covered; the custodian delivers the sold shares to that broker for settlement[^pse-sbl-models-2023:4] |

### Collateral, marking and recall

Eligible collateral is cash, equity or government securities, or a combination, in electronic form and free of liens.[^sec-mc-7-2006-sbl-rules:9] Collateral is marked to market at least daily and must be maintained at not less than **102%** of the market value of the borrowed securities when it is cash or government securities and not less than **105%** when it is equity; a margin call follows any shortfall and excess may be released.[^sec-mc-7-2006-sbl-rules:10][^sec-mc-7-2006-sbl-rules:11] A lender may recall on notice "in accordance with the standard settlement cycle", and a borrower may return at any time.[^sec-mc-7-2006-sbl-rules:12] The maximum borrowing period is two years.[^bir-rr-10-2006-sbl:2] On a default, the lender may dispose of the collateral and offset it against the shares not returned.[^pse-sbl-rules:3] Foreign-ownership limits matter: the lending system must monitor foreign ownership, and PSE warns that a foreign-limit breach before return can block returns to foreign lenders ([Chapter 14](#/ch/foreign-access)).[^sec-mc-7-2006-sbl-rules:6][^pse-sbl-short-selling-page]

### The PDTC lending pool

PDTC (the depository, part of the PDS Group) acts as lending agent. The SEC gave conditional approval on 21 July 2023 (PSE's 2024 President's Report calls it "approval"; the conditions were not found).[^pse-sbl-short-selling-webinar-2023:3][^pse-asm-2024-presidents-report:24] Documentation runs through depository participants: a lender signs an SLAA with its participant (SLAA1), the participant signs SLAA2 with PDTC, and the borrowing participant signs the MSLA with PDTC; the lending and borrowing clients are not MSLA signatories.[^pse-cn-2023-0053:1-2] PDS memo 03-2026 (22 April 2026) onboarded lenders and borrowers that hold BIR-registered agreements: lenders enter lending instructions into the Lending Pool, borrowers check availability and request loans if their **cash** collateral is sufficient, borrowers open a separate cash-collateral bank account, and participants send letters of intent naming their role.[^pse-cn-2026-0022:2] PSE's circular CN-2026-0022 announcing PDTC's readiness is dated 6 May 2026 on its face; it is listed elsewhere under 18 May 2026, probably a posting date (inference), and the document's own date governs.[^pse-cn-2026-0022:1] It describes PDTC's "first set of borrowers and lenders", and PSE is engaging pension funds, index funds and insurers to populate the pool.[^pse-press-2026-06-15-reforms] No pool size, inventory, fee or utilisation data is public.

### MSLA registration through PSE (since 15 May 2026)

The SEC approved the 2026 Revised Guidelines for MSLA Clearance on 15 May 2026, effective immediately; PSE circulated them on 22 May 2026 and became the one-stop shop, ending separate SEC and BIR approvals for each agreement.[^pse-cn-2026-0025:1-2][^pse-analyst-briefing-1h-2026:9] The press reported a cut in processing from 7 to 5 working days and removal of the SEC's PHP 5,030 fee (reported by Philstar; no PSE document found).[^philstar-2026-06-10-sbl-framework]

| Item | Rule |
|---|---|
| Filing | To PSE's Capital Markets Development Division. Bilateral MSLA (borrower files): letter-request, three notarised copies each of the MSLA and its Addendum, forms MSLA1a and MSLA1b, charter documents and BIR registration, PSE fee PHP 5,000 and BIR fee PHP 5,000. GMSLA: the executed GMSLA plus any supplemental agreement and the same items. Multilateral MSLA (lending agent files): PHP 5,000 PSE and PHP 5,000 BIR **per borrower**. Accession agreement: PHP 5,000 plus PHP 5,000 per additional borrower[^pse-msla-clearance-guidelines-2026:1][^pse-msla-clearance-guidelines-2026:2] |
| BIR deadline | Register within **two weeks** of execution if executed in the Philippines and **one month** if executed abroad; RR 10-2024 counts the month **from authentication or apostille**, and the BIR must act within **five working days** of a complete filing; the guidelines quote RR 1-2008 s.8(c)[^pse-msla-clearance-guidelines-2026:2][^pse-cn-2023-0053:2][^pse-cn-2024-0035:7] |
| Foreign execution | Agreements executed abroad need not be consularised or apostilled if the parties warrant due execution; agreements executed in the Philippines must be notarised[^pse-msla-clearance-guidelines-2026:3] |
| Margin rate in the Addendum | Not less than 102% (cash or government collateral) or 105% (equity)[^pse-msla-clearance-guidelines-2026:3] |
| PSE review | Five working days from complete documents and payment; **accession agreements one working day**[^pse-msla-clearance-guidelines-2026:3] |
| Transmission | PSE issues a Pre-Clearance Certificate with an MSLA reference number, sends the documents to the BIR (copy to the SEC) and remits the BIR fee; accession agreements go to the BIR weekly on Mondays (documents due by Wednesday noon)[^pse-msla-clearance-guidelines-2026:4] |
| After registration | The BIR certificate is released through PSE; a copy goes to CMIC within 15 days; the SEC may post-audit any registered agreement[^pse-msla-clearance-guidelines-2026:4] |
| Caveat | The guidelines are "[n]othing ... final approval by the Commission of the GMSLA framework, pro-forma GMSLA, Supplemental Agreement ... or the Philippine Annex"[^pse-msla-clearance-guidelines-2026:2] |

<div class="callout warn">
<span class="label">Documentary tension: apostille</span>

RR 10-2024 (s.8(c)) says an MSLA executed abroad is registered with an "authenticated or apostilled version" pre-cleared by PSE, while PSE's 2026 guidelines say foreign-executed agreements "do not need to be consularized or apostilled" for PSE pre-clearance if the parties warrant due execution, and the BIR's September 2023 position accepted a photocopy of a foreign-executed GMSLA with a notarised deed of undertaking to supply the apostilled copy within 30 days, failing which the application is deemed withdrawn.[^pse-cn-2024-0035:7][^pse-msla-clearance-guidelines-2026:3][^pse-cn-2023-0048:2][^pse-cn-2023-0048:4] Whether the BIR still accepts the undertaking route after RR 10-2024 is not stated in the documents read; confirm before relying on a one-month clock that starts at execution.
</div>

RR 10-2024 added that approval retroacts to the date of complete submission, registration lasts until revoked, a multilateral MSLA is registered once and extended by accession agreements, parties may switch between lender and borrower roles if the confirmation notice states the capacity, and the borrower gives PSE the BIR-stamped copy within 15 days.[^pse-cn-2024-0035:1-2]

### Tax treatment

| Item | Rule |
|---|---|
| Exemption | SBL of PSE-listed shares and the delivery of collateral are **not subject to stock transaction tax, capital gains tax or documentary stamp tax**, provided a valid MSLA is executed and registered with and approved by the BIR, the programme complies with SEC rules, and it is administered and supervised by PSE; all other taxes apply[^bir-rr-10-2006-sbl:4][^pse-cn-2024-0035:4] |
| If conditions fail | The borrowing is treated as a disposal by the lender and the return as an acquisition by the lender, and the applicable taxes apply; an unregistered MSLA makes the loan a sale and purchase outside the exchange subject to capital gains tax and DST[^bir-rr-10-2006-sbl:4][^pse-cn-2023-0053:2] |
| Permitted purposes | Settlement of a sale; settlement of a future sale; replacement of another borrowing; on-lending; financing and collateral pledging; other BIR-authorised purposes[^bir-rr-10-2006-sbl:5-6] |
| Manufactured dividends | Not taxable income of the lender and not deductible by the borrower[^bir-rr-10-2006-sbl:4] |
| Deemed sale (RR 10-2006 s.9, restated by RR 10-2024) | The loan is treated as a sale and purchase when any of these occurs: no stock return, in whole or part, at the end of the borrowing period (a partial return is allowed; the balance is deemed bought and sold); the shares are used for anything other than the specified purposes; the borrower defaults on a return; the agreement lacks the essential features of a valid MSLA; registration fails or is late; or loans are made outside the borrowing period[^bir-rr-10-2006-sbl:9][^pse-cn-2024-0035:8] |
| Tax if deemed sold | The deemed sale is off-exchange: capital gains tax (return within 30 days of each sale; base is the higher of the closing price on the day before the "Specified Day" and the amount realised) plus documentary stamp tax; the gain is exempt from regular income tax and the tax is not deductible; late payment penalties can follow. The Specified Day is the day after the borrowing period ends (no return), the day the shares were delivered (other use), or the day after a failed recall demand[^bir-rr-10-2006-sbl:9-10][^bir-rr-10-2006-sbl:10-11] |
| Failure to return, lender's remedy | RR 10-2024: the lender may buy equivalent shares on the exchange with the borrower's collateral, and that purchase bears stock transaction tax[^pse-cn-2024-0035:8] |
| GMSLA with a foreign party | The BIR may register a GMSLA with a PSE-prescribed supplemental agreement if it is filed within one month of execution; a foreign-executed GMSLA needs apostille or a notarised deed of undertaking to supply it within 30 days, failing which the application is deemed withdrawn[^pse-cn-2023-0048:1][^pse-cn-2023-0048:2][^pse-cn-2023-0048:4] |
| Offshore collateral (SEC, 24 May 2023) | Cash in USD, EUR, JPY, GBP or AUD; OECD government or agency debt rated at least BBB; constituents of benchmark indices of World Federation of Exchanges members[^pse-cn-2023-0048:2] |
| The short sale itself | A sale of listed shares: 0.1% stock transaction tax on the gross selling price since 1 July 2025 (previously 0.6%); no tax on the buy-to-cover purchase ([Chapter 12](#/ch/costs))[^ra-12214-cmepa:16][^bir-rr-20-2025-stt:2] |

Two dates are cited for the BIR's GMSLA confirmation: PSE's October 2023 circular cites the BIR's letter of 6 September 2023, while PSE's retail webinar deck says PSE received the confirmation on 25 September 2023 (and repeats 6 September elsewhere); read 6 September as the letter date and 25 September as when PSE says it received it.[^pse-cn-2023-0048:1][^pse-sbl-short-selling-webinar-2023:3]

### Pending: revised PSE SBL Rules ("directed pooled lending")

<div class="callout warn">
<span class="label">Pending SEC approval</span>

PSE consulted from 3 to 18 February 2026 (CN-2026-0009) and submitted the revised rules to the SEC on 16 April 2026; PSE said on 4 July and 17 August 2026 that it was "awaiting approval of SEC".[^pse-cn-2026-0009:1][^pse-press-2026-06-15-reforms][^pse-asm-2026-president-report:22][^pse-analyst-briefing-1h-2026:9] (The "For SEC Approval" badge in the 17 August slide text attaches to the neighbouring "One Share, One Lot" item on the rendered slide; both are pending.) No approval, expected date or effectivity notice was found.
</div>

The proposal lets an SEC-registered **onshore** lending agent (PDTC) run only the Philippine leg of a loan between a foreign lender and a foreign borrower executed under a GMSLA with offshore collateral: the lender or its offshore agent authorises an onshore custodian or participant to enter the lending instruction; the onshore agent pools the securities and moves them to the borrower's onshore custodian or participant; collateral is delivered to and managed offshore (by a third-party collateral manager for non-cash collateral, or the lender or offshore agent for cash); on a default the non-defaulting party notifies the onshore agent through its onshore representative and any capital gains tax is remitted by the onshore custodian or participant; the onshore agent files the bi-annual report; and PSE gains a right to inspect.[^pse-cn-2026-0009:3][^pse-cn-2026-0009:4][^pse-cn-2026-0009:5] The nine SBL reports would be merged into four (no lending agent) or three (with one).[^pse-cn-2026-0009:5][^pse-cn-2026-0009:6][^pse-cn-2026-0009:7] The annual report frames the friction removed: offshore lending agents would no longer need to register separately in the Philippines.[^pse-annual-report-2025:37] Philstar reported SEC comments of 6 May 2026 on custodians' responsibilities, on brokers being facilitators rather than lending agents, and on the GMSLA supplement (secondary).[^philstar-2026-07-02-short-selling]

<div class="callout warn">
<span class="label">Currency risk: BSP Circular 611</span>

PSE's FAQ still cites BSP Circular 611 (30 May 2008) as the foreign-exchange rule for foreign borrowers: special "For SBL Transactions Only" registration documents (BSRDs), permission to buy FX with the peso proceeds of borrowed shares, no BSRD eligibility for shares bought back for return, and collateral under SBL deducted from registered investments and not repatriable while pledged.[^bsp-circular-611][^pse-sbl-short-selling-page] BSP's FX Manual updated to May 2025 says a BSRD "shall no longer be issued" for certain onshore-listed investments covered by its Section 37.[^bsp-fx-manual-morfxt-2025-05:42] Whether Circular 611 survives unchanged for the offshore model was not verified; confirm with a custodian before each programme ([Chapter 14](#/ch/foreign-access)).
</div>

### Execution implications

- **Treat borrow as a pre-trade dependency measured in weeks.** PSE pre-clearance takes up to five working days (accession agreements one), then BIR action, plus PDTC systems onboarding, a cash-collateral bank account and client-side service agreements; collateral in the pool model is cash and must stay at or above 102% (105% for equity).
- **Calendar the tax cliff.** Failing the MSLA or return conditions turns a loan into a taxable sale or purchase. Monitor the two-year maximum and the two-week or one-month registration deadlines in operations.
- **Corporate actions.** Manufactured dividends flow to the lender; voting rights pass with title; the lender may recall within the T+2 settlement cycle; foreign-limit breaches can block returns.
- **Foreign funds.** Until the revised rules are approved, foreign borrowers face the older onshore route (BIR-registered MSLA, special BSP documentation, cash collateral in the Philippines).

<div class="callout infer">
<span class="label">Inference</span>

Onshore SBL exists mainly as plumbing. Lendable supply is limited to what the PDTC pool recruits (pension funds, index funds and insurers are being approached), so expect scarce borrow in the 52 names and a binding 10% cap on a name only if shorting ever becomes large. The realistic route for foreign hedge funds is the offshore GMSLA with an onshore agent, which needs the pending approval.
</div>

## Margin trading and lending against shares

### SRC Rule 48.1 in force

The statute tells the SEC to set credit limits "in accordance with the credit and monetary policies" of the BSP's Monetary Board, with a ceiling standard of the higher of 65% of the current market price or 100% of the lowest price in the preceding 36 months (never above 75%); the Monetary Board may move the percentages.[^ra-8799-src:50] The operative rule (2015 IRR, effective 9 November 2015) is stricter:[^sec-2015-src-irr:165]

| Item | Rule 48.1 now |
|---|---|
| Maximum credit | 50% of current market value at the time of the transaction (48.1.1) |
| Minimum equity | No new credit if account equity is below PHP 50,000 (48.1.1) |
| Maintenance margin | At least 25% of the market value of long positions and 30% of short positions (48.1.2) |
| Margin calls | Initial-margin call met within five business days; maintenance call within 24 hours; no purchase or sale order executes on the account until cured (48.1.3) |
| Liquidation | If a call is unmet, liquidate before the close of the next trading day (48.1.4) |
| Extension | Seven days for an initial-margin call on application to the Exchange (48.1.5) |
| Collateral | Credit only against securities collateral (Rule 48.2) |

### The draft replacement (exposed 25 August 2026)

<div class="callout warn">
<span class="label">Pending, not adopted</span>

The SEC En Banc exposed a replacement for Rule 48.1 on 25 August 2026 (comments to 15 September 2026); no adoption was found as of 6 October 2026. It would take effect 15 days after publication.[^sec-rfq-2026-src-rule-48-1-margin:1][^sec-rfq-2026-src-rule-48-1-margin:11]
</div>

| Item | Draft (interim rules) |
|---|---|
| Framework | PSE writes "Exchange Margin Trading Rules" within 90 calendar days of effectivity, subject to SEC approval[^sec-rfq-2026-src-rule-48-1-margin:6] |
| Eligible securities (interim) | Constituents of the PSEi and the MSCI Philippines Index, plus securities the Exchange designates (48.1.10.1)[^sec-rfq-2026-src-rule-48-1-margin:9] |
| Maximum credit | **60%** of current market value; minimum equity PHP 50,000 (48.1.11.1)[^sec-rfq-2026-src-rule-48-1-margin:9] |
| Maintenance | At least **30%** of current market value of margin-eligible securities (48.1.11.2); the separate 25% long and 30% short figures are not repeated[^sec-rfq-2026-src-rule-48-1-margin:9] |
| Margin call | Met within **three trading days** unless the agreement or house rules set shorter; failure allows liquidation without further notice, with notice to the customer by the next business day; written forbearance allowed; 7-day extension retained (48.1.12)[^sec-rfq-2026-src-rule-48-1-margin:9][^sec-rfq-2026-src-rule-48-1-margin:10] |
| Lenders | New or increased margin financing needs unimpaired paid-up capital of at least PHP 150m, compliance with risk-based capital adequacy, and no major PSE penalty in the prior two years (48.1.7.1)[^sec-rfq-2026-src-rule-48-1-margin:7] |
| House rules | Brokers may be stricter (48.1.11.3, 48.1.13); existing accounts continue (48.1.14)[^sec-rfq-2026-src-rule-48-1-margin:9][^sec-rfq-2026-src-rule-48-1-margin:11] |

A law-firm summary dated 9 September 2026 describes the draft (secondary).[^cruzmarcelo-2026-09-09-margin]

**Worked example (arithmetic from the rule text).** Buy PHP 10m of stock at maximum leverage. Now: debt PHP 5.0m (50%); maintenance 25% means a call when equity falls below 25% of market value, which happens when the position falls to PHP 5.0m / 0.75 = PHP 6.67m, a **33.3%** fall. Draft: debt PHP 6.0m (60%); maintenance 30% triggers at PHP 6.0m / 0.70 = PHP 8.57m, a **14.3%** fall, and the call must then be met within three trading days instead of 24 hours. The draft therefore allows more leverage with a much thinner price cushion.

### Broker house terms

Brokers apply stricter terms. First Metro Securities' margin agreement (version 072026) requires PHP 200,000 in cash or marginable securities to open and keeps a minimum net equity of PHP 50,000; interest is **0.90% per month plus VAT** on the daily debit balance, changeable without notice; buying is suspended below 50% equity ("margin alert"), a margin call below 40% requires restoring 50%, and securities are sold without notice below 30%; the broker may cut or cancel the line "at FMSBC's sole and absolute discretion"; and its Annex A lists 39 marginable securities (38 stocks and FMETF), all at a 100% rating.[^firstmetrosec-margin-trading-agreement-v072026:1][^firstmetrosec-margin-trading-agreement-v072026:2][^firstmetrosec-margin-trading-agreement-v072026:3][^firstmetrosec-margin-trading-agreement-v072026:6] That is the only broker's list documented here. All 38 of its marginable stocks are on the 5 October 2026 short-eligible list; the 13 eligible names it does not margin are BLOOM, COSCO, CREIT, DNL, GSMI, KEEPR, MREIT, NIKL, OGP, PX, SECB, SEVN and WLCON (a comparison of the two lists, not a PSE statement). No PSE statistic on margin debt was found.

### Foreign investors and banks

MSCI notes that overdraft facilities for foreign investors are prohibited and that foreign-exchange transactions must be linked to security transactions.[^msci-accessibility-review-2026:43] No numeric BSP ceiling on bank lending to finance share purchases was found; BSP Circular 432 (14 May 2004) fixes the loan value of "blue chip" share collateral at 50% of market value (issuer listed, net worth of at least PHP 1bn, five consecutive profitable years, not the lender's own shares).[^bsp-circular-432]

### Execution implications

- **Model financing by broker list and house haircut, not by the SEC maximum.** Eligibility is a broker list (39 names at First Metro).
- **Liquidation is fast and rules-based.** Today a maintenance call gives 24 hours and unmet calls are liquidated before the next close; do not assume time to cure in a stressed market.
- **Shorts in a margin account** carry 30% maintenance today; short sales under the SBL route are collateralised by cash instead.
- **Hedge funds** would normally finance through offshore prime-broker or swap lines; local margin is built for retail and high-net-worth tickets starting at PHP 200,000.

## Derivatives and hedging instruments

### Onshore: nothing is listed

| Product | Status | Evidence |
|---|---|---|
| PSEi index futures (first planned) | **Not launched; no SEC-approved rules.** Target "2026" (Jul 2024 report); learning sessions with TAIFEX, TPEx and TWSE (15-18 Dec 2025); rules "slated to be finalized in the second half of 2026"; early exposure draft to select institutions; RFI to technology vendors in July 2026; "discussions with multilaterals for possible funding" (17 Aug 2026); no launch date | [^pse-asm-2024-presidents-report:25][^pse-annual-report-2025:29][^pse-annual-report-2025:38][^pse-asm-2026-president-report:24][^pse-analyst-briefing-1h-2026:10] |
| Single-stock futures, options | None; SRC Rule 25 only bars exchange members from endorsing or guaranteeing options on listed securities; no derivative-exchange rules found | [^sec-2015-src-irr:72] |
| Structured (covered) warrants | **SEC draft only** (En Banc 28 Apr 2026; issued 29 Apr; comments to 13 May 2026; PSE memo CN-2026-0018 of 30 Apr). None listed. PSE is aligning its draft with the SEC's and gathering issuer feedback | [^pse-cn-2026-0018:2][^pse-analyst-briefing-1h-2026:10] |
| GPDRs | **Pending SEC approval** of revised rules submitted 24 Jun 2026; PSE aimed for approval and publication "within the quarter" (to 30 Sep 2026) and a ready issuer in 2H 2026; consulted Sep 2024, filed Jan 2025, SEC comments 26 May 2025. They give economic, not voting, interest in foreign securities, so they are not a hedge for Philippine equities | [^pse-analyst-briefing-1h-2026:10][^pse-cn-2024-0047:1][^pse-annual-report-2025:38][^pse-asm-2025-presidents-report:30] |
| Company warrants | One series, AGIW (Alliance Global Group), listed 19 Dec 2025: an issuer's own warrant, not a structured warrant (it closed at 1.05 with 5,000 warrants traded on 2 Oct 2026) | [^pse-press-agi-warrants][^pse-eod-daily-quotation-2026-10-02:9] |

<div class="callout warn">
<span class="label">Slipping targets</span>

PSE's derivatives and GPDR dates have slipped repeatedly: derivatives "Target Launch: 2026" (July 2024), "Q1 2026" (October 2024), "set to launch index futures" (July 2025), then an RFI and fund-raising with no date in August 2026; GPDRs "Target Launch: 2025" (July 2024), "Q1 2025" (October 2024), revised rules filed June 2026.[^pse-asm-2024-presidents-report:25][^pse-asm-2025-presidents-report:30][^pse-analyst-briefing-1h-2026:10] Do not model any of them before PSE circulars and SEC approvals appear. The Eqlipse engine's modular design is said to allow later integration of "advanced options pricing and index calculations".[^pse-annual-report-2025:37] See [Chapter 17](#/ch/reform-timeline).
</div>

The SEC's structured-warrant draft sets the terms of a future onshore channel. Issuers would be licensed broker-dealers or investment houses with at least **PHP 400m** unimpaired paid-up capital (non-collateralised issuers also need an investment-grade rating or a guarantee).[^pse-cn-2026-0018:5][^pse-cn-2026-0018:6] Underlyings would be single equities on a Philippine or foreign exchange, securities indices, ETFs, debt securities and baskets; foreign underlyings must trade on a World Federation of Exchanges member; series over an index, over foreign-listed instruments or over a non-collateralised basket (and any series where physical delivery would breach foreign-ownership limits) would be restricted to cash settlement; and all structured warrants outstanding over one local underlying would be capped at **50%** of its issued shares excluding treasury shares (the underlying company's own warrants do not count toward the cap).[^pse-cn-2026-0018:8][^pse-cn-2026-0018:9] On liquidity, the issuer discloses whether it will meet a spread requirement, provide liquidity through market making, or both; if it uses market making it appoints **only one** maker, discloses the maximum spread, minimum quantity and daily presence, announces a replacement at least two weeks before the old maker's obligations end, and may make a further issue to facilitate market making only if issuer and maker together hold no more than 50% of the existing issue.[^pse-cn-2026-0018:19] The draft would thus create the first series-level market-making obligation outside ETFs ([Chapter 8](#/ch/market-making)).

### Offshore hedges: status as found

| Instrument | What was found | Evidence |
|---|---|---|
| iShares MSCI Philippines ETF (EPHE, US-listed) | Tracks the MSCI Philippines IMI 25/50; about US$132.4m assets, 0.59% expense ratio, 40 holdings (largest ICT 22.7%, BDO 9.9%), average volume about 140,000 shares a day, inception 28 Sep 2010 (data page of 6 Oct 2026; secondary aggregator) | [^stockanalysis-ephe] |
| PLDT ADR (NYSE: PHI) | Market capitalisation about US$3.8bn, average volume about 234,000 shares, close US$18.15 on 5 Oct 2026; hedges TEL exposure only (secondary aggregator) | [^stockanalysis-phi] |
| SGX-PSE MSCI Philippines Index Futures | The only Philippine-equity index derivative mentioned in PSE's own materials: listed on the Singapore Exchange on 25 November 2013 (PSE history page) and shown as a "new product" in PSE's January 2015 roadshow. **Whether it still trades, and how actively, was not verified**; no SGX contract data was retrieved | [^pse-corp-history][^pse-tokyo-roadshow-2015-01:7] |
| Listed options on EPHE or PHI | None found: Cboe's options symbol directory (5,339 lines, downloaded 6 Oct 2026) lists classes for other country ETFs but no EPHE or PHI; absence in that directory only | [^cboe-options-symbol-directory] |
| OTC index or total-return swaps, P-notes | Inference: available from offshore banks, which would hedge by trading PSE shares; no public Philippines-specific size or pricing data was found and none of this was verified | none found |

The MSCI Philippines Index itself had only nine constituents at 30 September 2026, with ICTSI near 45%, so a future referencing it would hedge mostly ICT and the largest banks.[^msci-philippines-index-factsheet-2026-09:1] Foreign ownership limits (a general 40% limit, per MSCI) and the rule that foreign-exchange transactions be linked to security transactions shape any synthetic exposure ([Chapter 14](#/ch/foreign-access)).[^msci-accessibility-review-2026:43]

### Execution implications

- **Basis and timing.** EPHE holds 40 names with heavy ICT weight, so hedge ratios against the PSEi must be re-estimated, and US hours do not overlap PSE hours, so overnight gap risk is unhedged during the Manila session.
- **Swaps skip the short-selling rules but the dealer's hedge does not.** A dealer hedging a swap by selling PSE shares meets the uptick test, eligibility and the short-interest cap, so dealer capacity can vanish in stress.
- **No onshore index future before 2027 is the base case** (inference): rules unfinished, funding sought, vendor selection pending after the July RFI, and the engine itself goes live only on 23 November 2026.
- **Plan for the structured-warrant regime** as a future onshore hedging channel once adopted.

## What is not in the public record

- Borrow fees, lending-pool size, lendable inventory, locate availability and recall experience; PDTC's operating guidelines (referenced by PSE but not archived).
- Whether any short sale has been executed but unreported; the Daily Short Sell Report is the only public statistic.
- The exact definition of "last sale" for the uptick test (auction prints, odd-lot and block trades) and whether the engine applies the test at entry or at match; whether DMA clients can self-enter short orders today (no Exchange conditions were found published).
- Whether the engine accepts short orders in the run-off phase.
- The status after 5 October 2026 of the SEC's decision on the revised SBL rules; whether BSP Circular 611 is still the operative foreign-exchange rule for foreign borrowers.
- The final text of SRC Rule 48.1 and the PSE Exchange Margin Trading Rules (not yet written); margin-debt statistics; any BSP limit on bank lending against shares beyond the 2004 circular.
- The launch date and rules of any PSE derivative; the GPDR approval outcome after 17 August 2026; the trading status of the SGX MSCI Philippines futures; Philippines-specific swap and P-note volumes.
