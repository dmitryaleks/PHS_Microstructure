# PSE Equity Market Microstructure — Chapter 2: Instruments, Boards and Listing Landscape (research notes)

**Status of this file:** COMPLETE DRAFT v2, last revised 6 Oct 2026 (all six key questions covered; unresolved items are listed under each section's Gaps and in the closing summary). "Today" = 6 Oct 2026. Evidence tags: **[P]** primary-sourced (PSE/SEC/statute text or PSE live data pages), **[S]** secondary-only (news / law-firm), **[I]** my inference or my own computation from primary data. Citation form: `[^slug:N]` = physical 1-based PDF page N of `kb/pdfs/<slug>.pdf`; `[^slug]` = web page/dataset (see Source catalog). "CLDR" = PSE Consolidated Listing and Disclosure Rules, edition published as of January 2025 (the edition in force today per PSE's regulation page; see Q4).

---

## 1. Board / market structure: which instruments trade where, and how the rules differ

### Takeaway
PSE has exactly **two listing boards, Main and SME** (First/Second boards were merged in 2013, rules re-cut on 24 Mar 2021). Everything else people call a "board" is either (a) a rule-level label that does not appear in PSE's live security data (ETF Board), (b) a market segment inside the trading engine (Normal/board-lot market, Odd-Lot market, Block Sale/cross facility), (c) a currency/instrument flag (US$-denominated securities, "DDS"), or (d) a clearing remedy rather than a market (SCCP buy-in). There is **no "foreign board"** (foreign/local is a trade flag), and **no persistent "buy-in board"**. The Odd-Lot market is scheduled to disappear when the new trading engine (Nasdaq Eqlipse) goes live (**planned Mon 23 Nov 2026**, big-bang, no parallel run per PSE's 9 Jul 2026 broker-forum deck; SEC approval of One Lot One Share was still pending at 4 Jul) because lot size becomes 1 share [P] [^pse-nte-broker-forum-2026-07-09:9] [^pse-nte-faq-2026-08:1] [^pse-asm-2026-president-report:22].

### Cited findings
**Listing boards**
- CLDR Art. I Part A Sec. 4 (still worded "First Board, Second Board and SME Board") carries the note that on 20 May 2013 the SEC approved the Main and SME Board listing rules which superseded Parts D, E, F of the 2004 Revised Listing Rules, and that these were further amended on 24 Mar 2021 (Supplemental Rule 12) [P] [^pse-listing-disclosure-rules:21]. Art. III Part D = Main Board, Part E = SME Board, Part E-1 = SME under Sponsor Model [P] [^pse-listing-disclosure-rules:5].
- PSE directory (live, 6 Oct 2026) labels every live security with a "Listing Board" of *Main Board* or *SME Board* (exceptions: two dormant PLDT convertible-preferred rows, TLII/TLJJ, with blank board and sector); its sector filter has the six PSE sectors plus two pseudo-sectors, "SME" and "ETF EQUITY" [P] [^pse-listed-company-directory-frame].
- SME Board today holds 9 common-share issuers (CTS, HTI, IDC, KPPI, LPC, MFIN, MM, X, XG); PSE's own year-end table shows SME = 10 at end-2025 and 11 at end-2024 [P/I] [^pse-listed-company-directory-frame] [^pse-listing-statistics-web].
- Main vs SME listing criteria (CLDR): Main: 3-yr track record, cumulative net income ≥ PHP75m over 3 FYs and ≥ PHP50m in latest FY, stockholders' equity ≥ PHP500m, ≥3-yr operating history, ≥1,000 holders each ≥ 1 board lot [P] [^pse-listing-disclosure-rules:50] [^pse-listing-disclosure-rules:51]. SME: either cumulative EBITDA ≥ PHP15m (3 FYs) or cumulative revenue ≥ PHP150m with ≥20% average growth over the last 2 FYs; equity ≥ PHP25m; ≥2-yr operating history; ≥200 holders each ≥ 1 board lot; 5-yr business plan [P] [^pse-listing-disclosure-rules:57] [^pse-listing-disclosure-rules:58]. SME companies that miss the profit/equity test may list with a PSE-accredited sponsor for ≥3 full fiscal years of continuing sponsorship; if a sponsor is terminated and no replacement is found within 3 months trading is suspended, and at 6 months the company is automatically delisted [P] [^pse-listing-disclosure-rules:59] [^pse-listing-disclosure-rules:72] [^pse-listing-disclosure-rules:74]. PSE is reviewing the sponsor model (status "Ongoing Review" on 17 Aug 2026): removal of the insurance requirement, a shorter sponsor track-record requirement and removal of the continuing-sponsorship obligation are under consideration [P] [^pse-analyst-briefing-1h-2026:16]. An SME-listed company may be elevated to the Main Board on written request once it meets Main criteria [P] [^pse-listing-disclosure-rules:62]. SME IPOs may offer primary shares only (Art. III Part C Sec. 4 as superseded: companies exempt from track-record rules cannot offer secondary shares) [P] [^pse-listing-disclosure-rules:48] [^pse-listing-disclosure-rules:62].
- PSE web summary of the same criteria and fees (Main ALMF 1/100 of 1% of market cap, floor PHP250k, cap PHP2m; SME ALMF PHP100 per PHP1m, PHP50k–250k; ALMF unpaid by 15 Feb => automatic 2-month suspension) [P] [^pse-ipo-listing-requirements-web]. The Main-Board ALMF upper limit was raised from PHP2.0m to **PHP3.5m** effective 2 Jan 2025 (CN-2024-0068 of 19 Dec 2024, SEC-approved, amending Art. VI Part C Sec. 2; floor PHP250k and the SME scale of PHP100 per PHP1m, PHP50k–250k, unchanged; the CLDR table of contents lists it as Supplemental Rule 24) [P] [^pse-cn-2024-0068-almf-effectivity:1] [^pse-listing-disclosure-rules:15]. PSE's IPO-requirements web page has not been updated and still shows the PHP2m cap [P]; PSE's 1H-2026 briefing confirms the increase (upper fee limit from PHP2m to PHP3.5m) as a driver of higher listing-maintenance revenue [P] [^pse-analyst-briefing-1h-2026:12].
- No board-specific *trading* differences between Main and SME were found in the archived trading rules (same Normal-market rules, thresholds, tick/lot tables) [I; absence-of-evidence] — see Gaps.

**ETF "board"**
- SR 11 (SEC-approved ETF rules of 18 Mar 2013): "An ETF shall be listed on the Exchange's ETF Board, which is a separate board from the Exchange's existing boards." The rules re-apply only some listing rules (excludes IPO distribution rules, additional-listing rules, board-specific criteria) [P] [^pse-sr11-etf-rules-2026:4] [^pse-sr11-etf-rules-2026:5].
- But PSE's live directory shows the only ETF, FMETF, with *Listing Board = Main Board* and sub-sector "ETF-EQUITY" [P] [^pse-listed-company-directory-frame]. => the "ETF Board" is a rule-level construct; there is no separate ETF tape or trading-engine segment visible in any archived spec [I]. The June 2026 consultation draft would drop the construct: proposed Section 5 says ETF shares/units "shall be listed on the Exchange's Main Board" and proposed Section 6 says ETFs "shall not be required to maintain a minimum public ownership" (today: 10%, AP/MM holdings count as public) [P, draft] [^pse-cn-2026-0029-etf-amend-consult:8].
- The May 2026 "UPDATED" posting of SR 11 on PSE's site is text-identical (by my diff) to the 2021 posting of the ETF rules plus an appended copy of SEC MC 10-2012 (SEC ETF Rules); i.e. no substantive 2026 change to the in-force ETF rules [I; diff of `pse-etf-rules` vs `pse-sr11-etf-rules-2026`]. Proposed amendments are only at consultation stage (CN-2026-0029, 16 Jun 2026; comments to 30 Jun 2026) [P] [^pse-cn-2026-0029-etf-amend-consult:1].

**Eligible-broker restriction (REITs and DDS)**: only trading participants that attended PSE's REIT/DDS training and filed a sworn certification of operational readiness may trade REIT shares (Amended REIT Listing Rules Sec. 14; CN-2020-0066, 15 Jul 2020) or DDS (DDS Rules Part C Sec. 1(b)); PSE restricts non-compliant TPs, REIT shares must also be held under a **Name-on-Central-Depository (NOCD)** arrangement so that holders are traceable (Sec. 13). PSE's REIT and DDS product pages today list the *same* 123 eligible trading participants (124 rows, one duplicated name), i.e. effectively the whole TP roster [P] [^pse-cn-2020-0066-reit-broker-eligibility:1] [^pse-dds-rules:6] [^pse-reit-page-web] [^pse-dds-page-web]. For REIT IPOs eligibility also gates participation in the 20% broker allocation and the 10% LSI allocation via PSE EASy [P] [^pse-cn-2020-0066-reit-broker-eligibility:2].

**REITs, PDRs, preferred, warrants** — no separate board: all list on Main Board (REITs additionally governed by SR 3 / SEC REIT IRR; see Q2). PSE's new-listings table shows VREIT and PREIT as *SME* at IPO (2022) whereas the directory today shows Main Board for both (transfer or relabel not documented) [P/I] [^pse-new-listings-ipo-web] [^pse-listed-company-directory-frame].

**Dollar-denominated securities (DDS)**
- PSE: DDS are "listed, traded and settled in US dollar"; a DDS "shall be a different asset class than the issuer's existing listed shares"; distinct from the Dollar Denominated Trading (DDT) facility launched 2003 where the *same* peso-listed shares are quoted in USD [P] [^pse-dds-page-web].
- Live DDS list: DMPA1, DMPA2 (Del Monte Pacific US$ Series A-1/A-2 preference shares), TCB2A, TCB2B (Cirtek Holdings Preferred B-2 subseries A/B, quoted in USD) [P] [^pse-dds-frame] [^pse-sec-frames-snapshot]. Status 6 Oct 2026: DMPA1 *Suspended* (last price US$10.00, last data 24 Mar 2022); DMPA2 *Suspended* (US$9.71, 10 Nov 2022); TCB2A Open, last US$0.06 (1 Oct 2026, zero volume); TCB2B Open, US$0.36 (13 Jul 2026) [P] [^pse-sec-frames-snapshot].
- USD board-lot/tick table in the 15 Jan 2026 NTE user-group deck (current vs "One Lot One Share"): <=0.99: lot 100/tick 0.01; 1–4.99: 20/0.01; 5–9.99: 10/0.01; 10–19.98: 10/0.02; 20–49.95: 10/0.05; 50–99.95: 5/0.05; 100–199.90: 5/0.10; 200–499.80: 5/0.20; 500–999.50: 5/0.50; >=1,000: 5/1 [P] [^pse-nte-user-group-2026-01-15:10].
- **DDS rulebook (SR 13, PSE CN-2016-0078 of 2 Dec 2016)** [P] [^pse-dds-rules:2] [^pse-dds-rules:4] [^pse-dds-rules:6] [^pse-dds-rules:7] [^pse-dds-rules:8] [^pse-listing-disclosure-rules:14]: applies to **existing listed companies** that issue DDS (DDS IPOs need further rules); issuer must be in good standing (no suspension/penalties/investigations) and engage **at least two Eligible Brokers** (TPs trained and certified ready for USD trading) — a continuing-listing condition, breach may suspend DDS trading; same Reference Price, Trading Threshold and open/close calculation as peso stocks (the 2016 text applies the Revised Trading Rules by reference, so today's +50%/-30% static band and the dynamic thresholds follow); USD lot/tick table as above; **DDS may trade in the Odd-Lot Market**; trader value limits applied after converting to pesos at the *previous day's* exchange rate; done-through trades only among Eligible Brokers; **Block Sales: USD500,000 (regular) / USD1,000,000 (special)**; settlement in **USD** via an SCCP-designated settlement bank, TPs need FCDU accounts and a separate USD settlement account, good cleared funds by the settlement deadline; separate DDS section in TP end-of-day reports. SCCP/PDTC DDS operating guidelines also archived by others (`sccp-dds-clearing-settlement-2016`, `pdtc-dds-operating-guidelines-2017`, `sec-dds-directive-2017`) [P].

**Trading-engine segments (as documented in the archived 2010 Implementing Guidelines; later amendments are another chapter's scope)**
- Odd-Lot market = "separate market segment"; odd-lot orders carry an "O" prefix (e.g., OBC); only Limit/Market orders; continuous session only (no pre-open, pre-close or run-off/trading-at-last); no dynamic threshold in the odd-lot market; reference price = last adjusted closing price of the Normal market [P] [^pse-implementing-guidelines-trading-rules:19] [^pse-implementing-guidelines-trading-rules:20]. Under the new engine "with the standard lot size set at 1, the Odd Lot Market will no longer be available" [P] [^pse-nte-faq-2026-08:1].
- Block Sale: Regular Block Sale >= PHP20m, price within +/-5% of LACP, T+0; Special Block Sale >= PHP50m, COO approval, needs supporting agreement; both may be non-multiples of board lot (2010 Implementing Guidelines) [P] [^pse-implementing-guidelines-trading-rules:23] [^pse-implementing-guidelines-trading-rules:24]. **PSE itself restated the same thresholds on 1 Jul 2026**: regular block = minimum PHP20m with price within +/-5% of the Reference Price (previous close, or LACP after corporate actions); special block = minimum PHP50m; a pre-arranged trade below the block minimum can only be entered as a cross transaction inside the BBO, and "there is presently no execution facility" for smaller pre-arranged trades priced outside the BBO (the gap Negotiated Trades would fill) [P] [^pse-cn-2026-0031-negotiated-trades:3]. Whether regular blocks still settle T+0 after the 24 Aug 2023 T+2 migration is unverified (see chapter 04). "Negotiated Trades" proposed as a *variant of* (not replacement for) Block Sale, executed via a web-based facility [P] [^pse-nte-faq-2026-08:1]; consultation 1–7 Jul 2026 (CN-2026-0031) [P] [^pse-asm-2026-president-report:23].
- "Buy-in": SCCP rules provide a buy-in *procedure* for failed trades: if by 9:15 am of the business day after settlement date a clearing member still lacks securities, SCCP posts buy-in orders on the PSE trading floor; priced at the prevailing offer, else the lower of last close less two fluctuations / last transaction price / current offer (SCCP Clearing House Rules 2018 edition; the T+3 wording in that text pre-dates the migration to **T+2 effective trade date 24 Aug 2023**, CN-2023-0031/0040) [P] [^sccp-clearing-house-rules-2018:38] [^sccp-clearing-house-rules-2018:39] [^pse-cn-2023-0040-t2-go-live:1]. No separate buy-in board exists in the archived rules [I].
- "Foreign board": none found. Foreign vs local is carried as trade/account flags (House, Foreign/Local, Market Maker, Related Party Local/Foreign, Tax-Exempt Local/Foreign, Foreign/Local Retail and Institutional) in the trade-amendment matrix [P] [^pse-implementing-guidelines-trading-rules:23]; SCCP determines a clearing member's securities delivery obligations "on a flag-netting basis in accordance with the SCCP Operating Procedures" (2018 Clearing House Rules; the Operating Procedures themselves were not retrieved) [P] [^sccp-clearing-house-rules-2018:30]. **Historical "A/B" regular-board rule**: SEC's 1973 rules let "B" shares (open to Filipinos and aliens) trade on the *regular board* and obliged buyers to accept either A or B certificates; **SEC MC 10 s. 2025 (7 Aug 2025; effective 9 Aug 2025) repealed it and mandates declassification of Class A/B common shares**: affected issuers must amend their Articles within one year (**by 9 Aug 2026**); from 11 Aug 2025 buyers on the regular board accept delivery of the class they bought; a foreign buyer whose trade breaches the foreign-ownership limit must dispose of the excess immediately (same day if discovered intraday, else at next open) [P] [^pse-cn-2025-0035-sec-declassification-mandate:1] [^pse-cn-2025-0035-sec-declassification-mandate:3] [^pse-cn-2025-0036-declassification-effectivity:1]. Mechanics per CN-2026-0041 (10 Sep 2026): adjusted price of the merged single class = the **higher of the Class A and Class B closing prices on the last trading day**; **two-trading-day trading suspension** before the delisting date of the classified shares so that trades settle T+2 (sample: last trading day Thu 10 Sep, suspension from Fri 11 Sep, T+2 settlement Mon 14 Sep, declassification + delisting of old classes + resumption on Tue 15 Sep 2026) [P] [^pse-cn-2026-0041-declassification-price-suspension:1] [^pse-cn-2026-0041-declassification-price-suspension:2]. On 6 Oct 2026 the directory still lists **five A/B pairs as separate tickers**: ATN/ATNB, FJP/FJPB, LC/LCB, MA/MAB, OPM/OPMB (A = foreign-ownership limit 0%, B = "No Limit"; both lines display the same free-float level), so those mergers/suspensions had not yet been executed (Keppel Philippines A/B was delisted in Jul 2025) [I from P] [^pse-sec-frames-snapshot] [^pse-delisted-companies-web]. The circulars do not say which issuers remain or their cut-over dates [gap].
- **GPDR Board (rule-level, not yet live)**: PSE's draft GPDR rules (consultation 26 Sep 2024) say "GPDRs shall be listed in the GPDR Board of the Exchange"; trading "generally follows the rules and procedures of trading of equity securities", with PSE able to adjust GPDR trading hours to the overseas market's hours; clearing via SCCP equity procedures [P] [^pse-cn-2024-0047:12] [^pse-cn-2024-0047:23] [^pse-cn-2024-0047:24].

**Price-limit/threshold regime relevant to instrument types** (base text is the 2010 rulebook; the trading chapter owns the current state)
- Static threshold: **upper +50% / lower -30% of the reference price since 24 Mar 2020** (CN-2020-0028; the 2010 text had +/-50%); *not applicable to warrants* [P] [^pse-cn-2020-0028:1] [^pse-revised-trading-rules:20] [^pse-implementing-guidelines-trading-rules:10]. Dynamic threshold clusters A/B/C = 20%/15%/10% by trade frequency; **new securities start at 20%** [P] [^pse-implementing-guidelines-trading-rules:10] [^pse-implementing-guidelines-trading-rules:11].
- Static threshold is lifted (a) on the resumption day of securities suspended >= 1 year, (b) on the listing date of securities listed **by way of introduction**, (c) at the Exchange's discretion [P] [^pse-revised-trading-rules:34]; CLDR Art. III Part G Sec. 6 repeats that the trading band is lifted on the LBWI listing date and reinstated afterwards [P] [^pse-listing-disclosure-rules:87]. Market-wide circuit breaker: PSEi down >= 10% vs previous close halts the market, resume within 15 minutes (2010 text) [P] [^pse-revised-trading-rules:35].
- Board-lot/tick table (current, PHP), and the "One Lot One Share" replacement: current lot 1,000,000 (<0.01) / 100,000 / 10,000 / 1,000 (0.50–4.99) / 100 (5–49.95) / 10 (50–999.5) / 5 (>=1,000); proposed lot 1 for all prices with tick table 0.001/0.005/0.01/0.05/0.1/0.2/0.5/1/2/5 [P] [^pse-nte-user-group-2026-01-15:9].

### Inferences
- A model of "boards" for execution should key on **(security type, currency, lot regime, suspension/halt state)**, not on a board code; the only board attribute exposed publicly is Main/SME.
- ETF/REIT/preferred/warrant/PDR/DDS all trade in the same central limit order book with the same session phases; the differences are lot/tick table (PHP vs USD), threshold exemptions (warrants), and market-maker presence (ETF only).

### Gaps
- No primary statement found that SME vs Main shares differ in trading rules; trading-chapter researchers should confirm.
- ETF Board vs Main Board label tension (rule vs directory) is unexplained.
- Block-sale thresholds are confirmed unchanged by PSE's own 1 Jul 2026 restatement; the block settlement date after the T+2 migration and the current odd-lot parameters were not re-verified here (the odd-lot book disappears at the new-engine cut-over).

### Execution implications
- Hard-code **instrument-state filters**: 65 of the 385 securities with live frames are in "Suspended" status today (29 common, 36 preferred — including 2 of the 4 US$ DDS lines, DMPA1/DMPA2). Never route to a suspended symbol; orders cannot be posted/modified/cancelled while suspended and all posted orders are purged upon suspension, whereas a *trading halt* (<= 1 trading day) still allows order entry except cross transactions [P] [^pse-listing-disclosure-rules:140] [^pse-implementing-guidelines-trading-rules:27].
- On resumption after >= 1 year suspension the static threshold (+50%/-30%) is lifted until the first trades re-establish a basis [P] [^pse-revised-trading-rules:34] — expect gap/limit behaviour on resumption days (relevant to Villar-group names, see Q4). When a suspension is to be lifted PSE manually imposes a "Reservation" state (orders other than crosses may be posted, modified and cancelled) and announces the resumption time beforehand [P] [^pse-implementing-guidelines-trading-rules:26] [^pse-implementing-guidelines-trading-rules:27].
- Odd-lot flow ("O"-prefix symbols) is a separate book today; after cut-over (Q4 2026) there is one book with lot = 1 — update lot-rounding logic, min-notional rules and tick tables at the same time.
- Warrants (AGIW) have no static price limit; first-day move was +100%.
- **Universe hygiene**: do not build the instrument master from PSE's listed-company directory table alone — on 6 Oct 2026 it still carried 11 symbol-less rows for securities already delisted (common ATI, 8990, Keppel Philippines A and B, RRHI, SFA Semicon; preferred CPGP and SMC2A–2D) and 8 HTML template rows. Join it to the delisted-companies list and require a live security frame (status Open/Suspended) before admitting a symbol.
- Static band is asymmetric (+50% / -30%): downside limit-down moves are capped at 30% for ordinary stocks, but unconstrained for warrants and on LBWI listing days.

---

## 2. Instrument types: what exists, how many, liquidity and rule hooks

### Takeaway
PSE-listed securities (live directory, 6 Oct 2026, after dropping 11 stale rows of already-delisted securities): **387 securities** = 285 common-share lines (276 Main incl. 8 REITs + 9 SME; 280 issuers because five issuers carry separate A and B lines), **98 preferred** lines (29 issuers; San Miguel alone 21), **2 PDRs** (ABSP, GMAP), **1 warrant series** (AGIW), **1 ETF** (FMETF, tiny turnover), plus **4 US$ DDS** (inside the preferred count). Covered/structured warrants, index futures and GPDRs are *rules or projects, not listed products*. The practical tradable universe is far smaller than the headline: 65 symbols are suspended (some for 10+ years) and daily turnover is dominated by a handful of names.

### Cited findings
**Counts (my classification of PSE's directory by security name; sector fields have data-quality glitches)** [I, from P data] [^pse-listed-company-directory-frame]
| Type | Lines | Notes |
|---|---|---|
| Common shares | 285 | Main 276 (incl. 8 REITs), SME 9; = 280 issuers (A/B pairs ATN, FJP, LC, MA, OPM carry two lines each) |
| Preferred / preference | 98 | 29 issuers; 96 Main, 2 with blank board (PLDT TLII/TLJJ, no live frame = likely dormant); includes the 4 US$ DDS lines |
| PDR | 2 | ABSP, GMAP (Services/Media) |
| Warrants | 1 | AGIW (Holding Firms) |
| ETF | 1 | FMETF (sub-sector ETF-EQUITY) |
| **Total live** | **387** | 385 have a live security frame (320 Open, 65 Suspended) |
| *(excluded)* stale rows of delisted securities | 11 | symbol-less rows still in the directory table: common ATI, 8990, Keppel Philippines "A" and "B", RRHI, SFA; preferred CPGP, SMC2A, 2B, 2C, 2D — all appear on PSE's delisted-companies list (2024–2026) [^pse-delisted-companies-web] |
| *(excluded)* template rows in the HTML | 8 | |
Status snapshot (PSE security frames, 6 Oct 2026; "Open" vs "Suspended"): common 256 open / 29 suspended; preferred 60 open / 36 suspended / 2 without live data (TLII, TLJJ); PDR 2 open; ETF open; warrant open [I, from P frames] [^pse-sec-frames-snapshot]. 257 securities show a trade on 5 Oct 2026 (consistent with the market summary: 85 advances + 95 declines + 77 unchanged = 257) [P] [^pse-composite-sector-frame].

**Common shares**
- Share classes: SEC MC 10 s. 2025 (issued 7 Aug 2025, effective 9 Aug 2025) discontinues the Class "A"/"B" classification of listed common shares; PSE CN-2025-0035 (11 Aug 2025) and CN-2025-0036 (15 Aug 2025) relay it, with Articles amendments due by 9 Aug 2026 [P] [^pse-cn-2025-0035-sec-declassification-mandate:1] [^pse-cn-2025-0035-sec-declassification-mandate:3] [^pse-cn-2025-0036-declassification-effectivity:1]. Five A/B pairs are still listed as separate lines (ATN/ATNB, FJP/FJPB, LC/LCB, MA/MAB, OPM/OPMB); the price/suspension mechanics (adjusted price = higher of the A and B closes, 2-day suspension) are in Q1 [P/I] [^pse-sec-frames-snapshot].
- Sector reclassification: CN-2025-0047 (26 Dec 2025) moved 13 companies between PSE sectors/sub-sectors effective Mon 5 Jan 2026 (ATN, DITO, ECVC, ECP, FYN, JAS, LMG, PHR, PRC, PHA, PPC, UNH, WIN) under the PSE Sector Classification Guide rule that a company is classified by the activity generating >= 60% of its revenue; ATN and ATNB move from the Holding Firms to the Industrial index [P] [^pse-cn-2025-0047-sector-reclassification:1] [^pse-cn-2025-0047-sector-reclassification:2].

**Preferred shares**
- 98 lines / 29 issuers; top issuers: San Miguel Corp 21 lines (Series "2" sub-series 2-E..2-X plus the legacy Series 1, SMCP1; sub-series 2-A..2-D were redeemed on 1 Oct 2025 and survive only as stale directory rows), Megawide 10, Petron 9, Ayala 6, Arthaland 4, EEI 4, Globe 4, Phoenix Petroleum 4, Cirtek 4 [I] [^pse-listed-company-directory-frame]. Listing dates in directory by year: 2021: 11; 2023: 11; 2024: 12; 2025: 15; 2026 YTD: 11 (latest: Arthaland ALCPG/ALCPH on 2 Oct 2026; EEI EEIPE 14 Sep 2026; SMC2V/W/X 3 Aug 2026; TOPA1/A2 26 Jun 2026) [I] [^pse-listed-company-directory-frame].
- 36 of 98 preferred lines are *Suspended* (mostly series being retired/redeemed or illiquid legacy series, e.g., SMC2E–2K, PRF2A/B/3A/3B, PNX series, MWP series) [I; reason not verified] [^pse-sec-frames-snapshot].
- Primary-market scale in 2026: SMC raised PHP30bn via Series 2-V/2-W/2-X (dividend rates 8.0401/8.3570/8.6483%, oversubscribed 3.27x, listed 3 Aug 2026; SMC total PHP146.65bn across 11 sub-series/5 FOOs) [P] [^pse-press-smc-foo-2026]; Arthaland Series G/H raised PHP2.15bn (8.1250%/8.75%, 1.43x oversubscribed, listed 2 Oct 2026) [P] [^pse-press-arthaland-foo].
- **Listing through a preferred-share offering — rule replaced on 12 Aug 2026.** The Jan-2025 CLDR Art. III Part H (SR 19, effective 24 May 2022) required a minimum offering of PHP1bn or 20% of the preferred's market cap, >= 1,000 holders and 20% public ownership [P] [^pse-listing-disclosure-rules:90] [^pse-listing-disclosure-rules:91]. **CN-2026-0037 (12 Aug 2026; SEC-approved; effective immediately)** replaces it with "Listing through IPO or Direct Listing of Preferred Shares": (i) IPO route — minimum offer **PHP100m**, >= **100** stockholders each holding >= 1 board lot, same 365-day lock-up for below-offer-price issuances in the prior 180 days, LSI offering window 3 trading days (public offer 5 trading days); (ii) **Direct listing route** (no public offering; shares from QIB/non-QIB private placements and QIB sales are eligible) — tradable immediately, but any transfer must go through "the Exchange's facility or system for negotiated transactions" and transfer restrictions apply if the shares were issued in an exempt transaction; the issuer must distribute >= **PHP50m** of the series to >= **100 investors within 1 year** of listing, else PSE may suspend trading, double the ALMF, or require a buy-back within 90 days and delist; (iii) initial listing price set by a financial-adviser report (market yields/spreads/comparables); shelf listing for up to 5 years; disclosure limited to events affecting ability to pay dividends; modified penalty scale (basic PHP5,000–, per-day, by total assets) [P] [^pse-cn-2026-0037-preferred-shares-rule-effectivity:1] [^pse-cn-2026-0037-preferred-shares-rule-effectivity:3] [^pse-cn-2026-0037-preferred-shares-rule-effectivity:4] [^pse-cn-2026-0037-preferred-shares-rule-effectivity:5] [^pse-cn-2026-0037-preferred-shares-rule-effectivity:6] [^pse-cn-2026-0037-preferred-shares-rule-effectivity:9]. Consultation history: CN-2026-0015 (21 Apr 2026), second exposure draft CN-2026-0028 (10 Jun 2026), SEC submission 25 Jun 2026 [P] [^pse-asm-2026-president-report:22] [^pse-circular-index-2025-2026]. Dependency [I]: directly listed preferreds can only change hands through a negotiated-transaction facility, which PSE is still consulting on (Negotiated Trades, CN-2026-0031) — whether that facility is live today is unverified.
- Preferred shares and treasury shares are *excluded* from the public-float computation under the new MPO rule [P] [^pse-amended-mpo-rule-2026-08:3] [^pse-amended-mpo-rule-2026-08:10].

**Warrants (company-issued) and covered/derivative warrants**
- CLDR Art. V Part E (warrants) [P]: *Subscription warrants* — exercise period >= 1 yr and <= 5 yrs [^pse-listing-disclosure-rules:116]; *Derivative Covered Warrants* — issuer holds 100% of underlying listed shares, charge in favour of an independent trustee bank, exercise period 9–24 months [^pse-listing-disclosure-rules:117]; *Derivative Non-Collateralized Warrants* — only investment houses/universal banks, irrevocable guarantee + stand-by LC from a guarantor with unimpaired paid-up capital >= PHP1.25bn, 9–24 months [^pse-listing-disclosure-rules:113] [^pse-listing-disclosure-rules:118]; all warrants freely transferable (non-detachable only with host security), listing of warrants issued by listed companies is mandatory, warrants auto-delist at end of exercise period [^pse-listing-disclosure-rules:122]; exercise price >= par (or PHP5 if no-par) [^pse-listing-disclosure-rules:121]; listing effected 7 trading days after compliance with notice-of-approval conditions [^pse-listing-disclosure-rules:123]. The part carries a note that the warrant rules are "subject to revisions … pending final approval by the Commission" [^pse-listing-disclosure-rules:112].
- Only one warrant series is listed: **AGIW** — 2.2bn warrants of Alliance Global Group, listed 19 Dec 2025, PHP1.1bn gross proceeds, exercise price PHP12, five-year exercise period, potential PHP26.71bn if exercised; +100% on listing day to PHP1.00 [P] [^pse-press-agi-warrants]. 5 Oct 2026: last PHP1.05, 5,000 warrants traded (PHP5,270), 52-wk 0.60–1.96; 2,203,548,165 warrants listed, board lot 1,000, free float 28.54%, market cap ~PHP2.3bn [P] [^pse-sec-frames-snapshot]. PSE's delisted list shows earlier company warrants: Cirtek TECHW (expired 19 Aug 2024), Leisure & Resorts World LRW (29 Oct 2021), Megaworld MEGW1/2 (2014–15) — i.e. company-issued warrants are rare and short-lived [P] [^pse-delisted-companies-web].
- No derivative/covered warrant has ever appeared in the directory [I]; PSE now plans *structured warrants* (SEC proposed rules circulated 30 Apr 2026, comments to SEC until 13 May 2026) [P] [^pse-cn-2026-0018:1]; PSE "aligning its draft rules with the SEC's and gathering feedback from potential issuers" [P] [^pse-asm-2026-president-report:24].

**ETF — FMETF only**
- Live: "ATR FAMI Philippine Equity Exchange Traded Fund, Inc." (FMETF), listed 2 Dec 2013; 5 Oct 2026 last PHP97.00, volume 8,610 shares (PHP835,667), 52-wk 94.80–109.50; iNAV shown by PSE 97.3388 [P] [^pse-sec-frames-snapshot] [^pse-etf-frame] [^pse-listed-company-directory-frame]. PSE's ETF page lists FMETF as the only ETF, with First Metro Securities Brokerage Corp. as both Market Maker and Authorized Participant [P] [^pse-etf-page-web]. Fund size: 11,891,260 shares outstanding (11,841,260 issued; 30,000,000 listed), par PHP100, board lot 10, free float shown 100%, **market cap ~PHP1.15bn** (i.e. ~0.07% of its shares changed hands on 5 Oct) [I from P] [^pse-sec-frames-snapshot]. Origin: listed 2 Dec 2013 as the Philippines' first ETF by shelf listing, authorised capitalisation PHP3bn with an initial PHP750m listed on day one, tracking the PSEi [P] [^pse-annual-report-2013:22].
- Mechanics per PSE/SEC rules [P]: open-end investment company issuing/redeeming in *Creation Units* against a basket; >= 2 Authorized Participants (broker-dealers, TPs, paid-up >= PHP100m) and one designated Market Maker; min authorized capital and paid-up capital PHP250m; all-Filipino board; transfer agent paid-in >= PHP100m [^pse-sr11-etf-rules-2026:4] [^pse-sr11-etf-rules-2026:5] [^pse-etf-page-web]. The fund manager needs >= 2 years' operating experience; the underlying securities must be listed and traded on a registered exchange and be sufficiently liquid (criteria disclosed in the prospectus); an ETF offering is outside the IPO distribution rules (no mandatory 20% trading-participant or 10% LSI allocation); and under **shelf listing** the ETF may list every share covered by its registration statement, but trading eligibility starts only when the Exchange is notified that shares have been created and issued to or through an AP, with unissued shares removed from the registry when the shelf registration lapses [^pse-sr11-etf-rules-2026:4] [^pse-sr11-etf-rules-2026:5] [^pse-sr11-etf-rules-2026:6] — so FMETF's 30,000,000 listed versus 11,891,260 outstanding shares look like a shelf artefact [I]. **iNAV published every 1 minute** during trading hours (by the fund, manager or third party; the SEC ETF Rules appended to the same file default to every 15 seconds unless the Exchange proposes another frequency, which PSE did [^pse-sr11-etf-rules-2026:36]); NAV/NAVps, shares outstanding, index and tracking error announced daily (cut-off 4:30 pm, amended by Board Resolution 141 of 2013 to 6:30 pm) [^pse-sr11-etf-rules-2026:8]. Creation/redemption "can occur any time during trading hours", initiated by cross transaction through PSE; creation done when iNAV < ETF price, i.e. arbitrage is intraday [^pse-etf-page-web]. Public-ownership floor 10%, with AP/MM-held shares counted as public [^pse-sr11-etf-rules-2026:7].
- Suspension/halt triggers [P]: suspended if suspended underlying securities >= 20% of the basket, or no Market Maker for 1 month, or SEC order; 1-hour halt on tracking-error breach, delisting of an underlying, halt of underlying >= 20% of index value, or late iNAV [^pse-sr11-etf-rules-2026:12] [^pse-sr11-etf-rules-2026:13]. Fees: filing PHP50k, listing PHP100k, ALMF 1/200 of 1% of market cap (max PHP250k); penalties PHP100/day (<2 APs), PHP500/day (no MM) [^pse-sr11-etf-rules-2026:14]. Creation/redemption transparency [P]: the ETF must notify PSE within 10 minutes of any creation or redemption (with the resulting shares outstanding), a tracking-error breach or a failure to publish the iNAV, and file a monthly issuance/redemption report within 5 trading days of month-end; trading in the ETF is suspended if a terminated market maker, AP, fund manager, custodian, index provider or transfer agent is not replaced at least 10 trading days before the termination takes effect [^pse-sr11-etf-rules-2026:10] [^pse-sr11-etf-rules-2026:11] [^pse-sr11-etf-rules-2026:12].
- **Market-maker quoting obligations** (ETF MM rules, Implementing Guidelines Sec. 2) [P] [^pse-sr11-etf-rules-2026:23] [^pse-sr11-etf-rules-2026:24]: max spread 20 ticks (price 0.0001–0.495), 15 ticks (0.50–19.98), 10 ticks (20–999.50), 5 ticks (>=1,000); min order size 5 board lots; "wide spread" if spread exceeds the limit, one-sided or no quotes for >= 3 continuous minutes; MM must restore within 90 seconds; presence >= 50% of each day and >= 80% of each month. For FMETF at ~PHP97 (tick 0.05) the limit is 10 ticks = PHP0.50 and the quote must be >= 5 lots x 10 shares = 50 shares [I, from the table + lot/tick tables].
- **Reform pipeline** (consultation only): CN-2026-0029 (16 Jun 2026; comments to 30 Jun; aligned with SEC MC 14 s. 2026 on umbrella funds) — (1) umbrella ETFs: multiple portfolios/sub-funds under one issuer, each with its own NAV, basket and listed securities; (2) UITFs and other collective investment schemes as eligible issuers, fund *units* listable alongside shares; (3) actively managed ETFs; (4) minimum paid-up capital PHP250m -> PHP50m (PSE's press note adds a floor as low as PHP1m for investment companies with >= 5-year record); (5) >= 1 Authorized Participant (if only one, it is deemed the Market Maker; otherwise the MM need not be an AP, but only an AP can submit creation/redemption instructions); (6) ETFs tracking securities listed on foreign exchanges or regulated OTC markets; (7) no minimum public-ownership requirement [P, draft] [^pse-cn-2026-0029-etf-amend-consult:3] [^pse-cn-2026-0029-etf-amend-consult:4] [^pse-cn-2026-0029-etf-amend-consult:7] [^pse-cn-2026-0029-etf-amend-consult:8] [^pse-cn-2026-0029-etf-amend-consult:9]; separate market-making framework (consultation to 23 Jun 2026; includes GPDRs, could extend to stocks) [P] [^pse-press-additional-reforms] [^pse-press-market-making] [^pse-asm-2026-president-report:23]. Not in force: PSE's 17 Aug 2026 briefing still lists the ETF rule amendments as "Revising per Public Comments" [P] [^pse-analyst-briefing-1h-2026:16]; no SEC approval has been announced [gap].

**REITs (8 listed)** [P] [^pse-new-listings-ipo-web] [^pse-reit-frame] [^pse-sec-frames-snapshot]
| Ticker | Issuer | Listing date | Last (5 Oct 2026) | Volume / value (5 Oct) | Status |
|---|---|---|---|---|---|
| AREIT | AREIT, Inc. (first PH REIT) | 13 Aug 2020 | 36.90 | 439,400 / PHP16.2m | Open; PSEi member |
| DDMPR | DDMP REIT, Inc. | 24 Mar 2021 | 1.03 | 1.86m / PHP1.9m | Open |
| FILRT | Filinvest REIT Corp. | 12 Aug 2021 | 2.74 | 1.43m / PHP3.9m | Open |
| RCR | RL Commercial REIT, Inc. | 14 Sep 2021 | 6.23 | 2.40m / PHP14.8m | Open; PSEi member since 2 Feb 2026 |
| MREIT | MREIT, Inc. | 1 Oct 2021 | 13.42 | 542,500 / PHP7.3m | Open |
| CREIT | Citicore Energy REIT Corp. | 22 Feb 2022 | 2.90 | 2.63m / PHP7.6m | Open |
| VREIT | VistaREIT, Inc. | 15 Jun 2022 | 1.31 (stale) | 0 | **Suspended since ~1 Jun 2026** (Villar group) |
| PREIT | Premiere Island Power REIT Corp. | 15 Dec 2022 | 1.00 | 150,000 / PHP0.15m | Open |
- Legal frame: RA 9856 (REIT Act of 2009), SEC IRR (MC 1 s. 2020; amended by **SEC MC 1 s. 2026**, issued 8 Jan 2026, effective 25 Jan 2026 [S]), BIR RR 3-2020, PSE Amended REIT Listing Rules (SR 3: CN 2020-0005, MEA 2022-0001, CN 2023-0010) [P] [^pse-regulation-listed-company-web]. IRR (2020) requirements [P]: distribute >= 90% of Distributable Income annually by the last working day of the 5th month after FY-end [^sec-mc-1-2020-reit-irr:10]; minimum public ownership — listed, with >= 1,000 public shareholders each holding >= 50 shares and in aggregate >= 1/3 of outstanding capital stock [^sec-mc-1-2020-reit-irr:11]; min paid-up capital PHP300m, >= 1/3 (min 2) independent directors [^sec-mc-1-2020-reit-irr:12]; >= 35% of deposited property in Philippine real estate, <= 40% overseas [^sec-mc-1-2020-reit-irr:14]; leverage <= 35% of deposited property, up to 70% if publicly rated investment grade [^sec-mc-1-2020-reit-irr:16]. PSE REIT page: management fee <= 1% of NAV; sponsor must sell >= 1/3 of the REIT to the public (IRR 5.1.a) [P] [^pse-reit-page-web]. **Tax link to MPO**: under BIR RR 3-2020 a REIT's dividends are deductible from taxable income only if paid within 5 months of year-end, the REIT keeps public-company status and complies with its reinvestment plan, and — before declaring dividends — it files a sworn statement that the minimum public ownership was maintained at all times (plus quarterly shareholder lists with TINs); sales of REIT shares outside the Exchange attract capital gains tax [P] [^bir-rr-3-2020-reit:4] [^bir-rr-3-2020-reit:5]. New PSE MPO rule: **REIT MPO 33.33%** at IPO and maintenance [P] [^pse-amended-mpo-rule-2026-08:2] [^pse-amended-mpo-rule-2026-08:3].
- **PSE REIT Listing Rules, 2023 amendments (SR 3.2 = CN-2023-0010 of 9 Mar 2023; supersede 2020 rules and the 13 Jun 2022 MEA-2022-0001 amendments)** [P]: REIT must have a 90% dividend policy; be a public company upon and after listing (>= 1,000 public shareholders each >= 50 shares owning in aggregate >= 1/3); paid-up capital >= PHP300m; stockholders' equity >= PHP500m at filing; >= 75% of deposited property in income-generating real estate (<= 40% overseas, with SEC authority); >= 1/3 (min 2) independent directors; sponsors must give a reinvestment undertaking and plan; the 3-year "same business" track-record test is waived [^pse-sr3-2-reit-listing-amend-2023:2] [^pse-sr3-2-reit-listing-amend-2023:3]. **Lock-up**: Main Board REIT — holders of >= 10% locked 180 days after listing (track-record REIT) or 365 days (newly incorporated REIT invoking the track record of its assets, or exempt issuer); SME REIT — non-public holders and related parties 1 year [^pse-sr3-2-reit-listing-amend-2023:4]. **Continuing**: REIT must comply with the REIT-Act public-ownership requirement; failure => trading suspension of <= 6 months then automatic delisting; annual independent full valuation; quarterly/annual REIT-specific reports incl. reinvestment-plan progress [^pse-sr3-2-reit-listing-amend-2023:6] [^pse-sr3-2-reit-listing-amend-2023:7] [^pse-sr3-2-reit-listing-amend-2023:8].
- **SEC MC 1 s. 2026 (REIT IRR amendments; issued 8 Jan 2026, effective 25 Jan 2026)** [S, law-firm page fetched]: eligible assets widened to "assets capable of producing recurring and predictable cash flows" (transport, telecom and energy infrastructure, data centres, parking, warehouses); indirect holding via SPV/JV allowed if the REIT owns >= 2/3 of outstanding voting capital; public shareholder = no sponsor affiliation and no "substantial influence" (presumed at >= 10%); >= 90% of distributable income distributed by the REIT and by SPVs/JVs to the REIT; management fee <= 1% of NAV with no duplicate fees on SPV assets; sponsor reinvestment of proceeds within one to two years [^cruzmarcelo-sec-reit-rules-2026]. PSE said the framework "implemented in January" is "already proving to be a powerful catalyst", cited a **VITRO REIT listing application** and toll-road IPO interest, and warned that high rates (8%+ preferred yields) may moderate REIT listings [P] [^pse-press-reit-framework-forum]. Vitro REIT IPO ~PHP24.19bn scheduled 12 Oct 2026 [P] [^pse-asm-2026-president-report:8].

**PDRs**
- ABSP: ABS-CBN Holdings Corporation PDRs (listed 7 Oct 1999); GMAP: GMA Holdings, Inc. PDRs (listed 30 Jul 2007); both Services/Media, Main Board [P] [^pse-listed-company-directory-frame]. 5 Oct 2026: GMAP last PHP3.25 (-17.93% vs prior close of 25 Sep: 3.96), 46,000 PDRs (PHP150,190), 52-wk 3.25–6.25; ABSP last PHP2.32, no trade since 2 Oct, 52-wk 1.35–4.50, P/E shown negative [P] [^pse-sec-frames-snapshot]. Static data: ABSP — 91.77m PDRs issued/outstanding (262.5m listed), free float 85.72%, market cap ~PHP213m, lot 1,000; GMAP — 363.5m PDRs, free float 20.80%, market cap ~PHP1.44bn, lot 1,000; both with FOL "No Limit" [I from P] [^pse-sec-frames-snapshot]. BSP's FX Manual (Circular 1030 of 5 Feb 2019) lists PDRs listed onshore as eligible inward foreign investments registrable via authorised agent banks [P] [^pse-cn-2019-0037-foreign-investment-etf:1] [^pse-cn-2019-0037-foreign-investment-etf:2]. Underlying shares of PDRs count as *public* shares in the public-float guidelines unless otherwise non-public [P] [^pse-amended-mpo-rule-2026-08:11].
- **GPDR** (Global Philippine Depositary Receipts): peso-denominated instrument giving economic but no voting interest in foreign-listed securities with an option to convert to the underlying; PSE proposed rules 26 Sep 2024 (CN-2024-0047, checklist CN-2024-0054); revised rules submitted to SEC 24 Jun 2026; approval/publication "targeted within the quarter" (Q3 2026) as of 4 Jul 2026 [P] [^pse-asm-2026-president-report:24] [^pse-circular-index-2025-2026]. No GPDR is listed today [I]. Slippage: in Oct 2024 PSE targeted GPDR implementation by **Q1 2025** [S] [^bworld-pse-gpdr-derivatives-2024]; as of Oct 2026 the rules are still awaiting SEC approval.

**Investment companies / funds other than the ETF** — no separate category appears in the directory (only ETF-EQUITY); open-end mutual funds/UITFs are not exchange-listed [I; absence]. Under the proposed ETF reforms UITF/umbrella funds could list as ETFs [P] [^pse-press-additional-reforms].

**Fixed income (context only)** — PSE's CLDR Art. IV allows debt listing (min issue PHP100m, >= 100 holders, rated) but corporate bonds and government securities trade on PDEx (PDS Group); PSE now owns 94.55% of PDS Holdings (PDEx + PDTC; stake as of 4 Feb 2026, from a 20.98% associate holding until Dec 2024) and is integrating systems (phase 2 target 2027, incl. fixed-income ETFs/derivatives) [P] [^pse-listing-disclosure-rules:93] [^pse-annual-report-2025:8] [^pse-annual-report-2025:9] [^pse-asm-2026-president-report:28]; ASM slide: corporate bond listings 22 (2024), 25 (2025), 16 (6M26) [P] [^pse-asm-2026-president-report:9].

### Inferences
- Liquidity is extremely concentrated: on 5 Oct 2026 total market value was PHP3.74bn, of which ICT alone traded PHP873m (23%), BDO PHP190m; FMETF PHP0.84m; PREIT PHP0.15m; AGIW PHP5k [I from P] [^pse-composite-sector-frame] [^pse-sec-frames-snapshot]. The ETF/warrant/PDR/DDS universe is, for execution purposes, untradeable at size.
- PNB Holdings (LTL), listed by introduction on 25 Sep 2026, traded 73.8m shares (PHP88m) on 5 Oct, i.e. ~2.4% of market value in a PHP1.20 stock [I from P] [^pse-sec-frames-snapshot].

### Gaps
- Per-instrument terms (par values, dividend rates, call dates for preferreds), FMETF creation-unit size and tracking index, and PDR conversion terms were not retrieved (issuer prospectuses/EDGE not accessible; edge.pse.com.ph errors).
- Reason for each preferred suspension not verified; whether the two PLDT convertible-preferred lines (TLII, TLJJ), which show no live data, are still outstanding.
- Whether SEC has approved ETF, GPDR, preferred-listing and board-lot amendments since the dates above: unknown.

### Execution implications
- Treat ETF/PDR/warrant/DDS lines as **no-algo instruments**: single-digit-percent-of-day volumes in the tens of thousands of pesos; any child order sized off ADV will exceed the day's value. FMETF's MM obligation (5 lots, 10-tick spread cap) is the only structural liquidity source.
- For ETF arbitrage the creation/redemption is a PSE cross transaction against an AP (First Metro Securities is the sole AP/MM), not an open market; no second AP is publicly listed.
- Preferred shares: yield-driven instruments (8%+ coupons in 2026) with multiple sub-series per issuer; keep issuer-level aggregation in risk limits and handle series-level suspensions.
- Check symbol currency flag: USD DDS use a different lot/tick table; TCB2A/B quote in dollars with sub-cent prices.
- **Linked halts**: under the Revised Trading Rules a halt or suspension of a security also halts or suspends any warrant, PDR or other security that directly derives its value from it (Art. VII Secs. 3(c) and 4(c)) — so AGIW stops with AGI, and a halt in ABS-CBN or GMA Network shares would take the ABSP/GMAP PDRs with it; orders in a suspended security cannot be posted, modified or cancelled, and the Implementing Guidelines purge all posted orders upon suspension (the Rules text says they "may be purged at the end of a Trading Day") [P] [^pse-revised-trading-rules:34] [^pse-implementing-guidelines-trading-rules:27].

---

## 3. Universe statistics (latest available)

### Takeaway
PSE's own table: **282 listed companies at end-2025** (272 Main + 10 SME), down from 286 in 2022; only 2 IPOs in 2025. The live directory today shows 285 common-share lines = 280 issuers (276 Main lines incl. 8 REITs + 9 SME; five issuers have separate A and B lines), of which 29 lines are suspended — this reconciles with PSE's 282 at end-2025 (see the reconciliation below). Total market cap PHP19.44tn (6M26) vs PHP18.73tn (2025); domestic market cap PHP13.65tn at end-2025 (PSEi 6,052.92); PSEi was 5,743.21 on 5 Oct 2026.

### Cited findings
**PSE headline table (listing statistics page)** [P] [^pse-listing-statistics-web]
| Year-end | Main | SME | Total | New listings (Main/SME/Total) |
|---|---|---|---|---|
| 2021 | 269 | 7 | 276 | 8 / – / 8 |
| 2022 | 276 | 10 | 286 | 6 / 4 / 10 |
| 2023 | 273 | 10 | 283 | 3 / – / 3 |
| 2024 | 272 | 11 | 283 | 2 / 1 / 3 |
| 2025 | 272 | 10 | 282 | 2 / – / 2 |

PSE's 17 Aug 2026 analyst briefing (data as of 14 Aug 2026) reports **280 listed companies**, total market cap PHP20.56tn (+9.8% YTD), PSEi 6,297.30 (+4.0% YTD), average daily value PHP7.57bn, capital raised YTD PHP69.43bn (-2.0% y/y) and net foreign selling PHP8.89bn [P] [^pse-analyst-briefing-1h-2026:3].

**Directory-derived counts, live common-share lines only (285), 6 Oct 2026** [I from P] [^pse-listed-company-directory-frame] [^pse-sec-frames-snapshot]
| Sector | Rows | of which suspended |
|---|---|---|
| Industrial | 75 | 6 |
| Services | 60 | 7 |
| Property | 51 (incl. 8 REITs) | 8 |
| Holding Firms | 32 | 2 |
| Financials | 31 | 3 |
| Mining & Oil | 27 | 2 |
| SME Board (no sector tag) | 9 | 1 |
| **Total** | **285** | **29** |
Sub-sectors (lines): Banks 17, Other Financial Institutions 14; Holding Firms 32; Industrial — Food/Beverage/Tobacco 29, Electricity/Energy/Power/Water 25, Construction/Infrastructure/Allied 10, Electrical Components & Equipment 6, Chemicals 4, Other Industrials 1; Mining 22, Oil 5; Property 51; Services — Transportation 10, Retail 9, Casinos & Gaming 8, Information Technology 8, Hotel & Leisure 6, Other Services 6, Telecommunications 5, Education 4, Media 4 [I]. (Directory sector strings are inconsistent — e.g., VREIT sub-sector "REIT", FILRT sector field holds the company name, CNPF blank — I normalised by hand; treat as +/-2.) **Reconciliation with PSE's own series (resolved) [I from P]**: PSE counts companies, not lines. 285 common lines − 5 'B' lines (ATNB, FJPB, LCB, MAB, OPMB) = 280 issuers = PSE's 282 at end-2025 + 1 listing in 2026 (LTL, PNB Holdings, LBWI 25 Sep) − 3 delistings in 2026 (ATI 3 Apr, LAND 6 Jul, RRHI 31 Aug). The Main/SME split also ties (271 Main / 9 SME in the directory vs 270 / 10 from rolling PSE's table forward) if exactly one company moved from SME to Main — plausibly Altus Property Ventures (APVI), which PSE's new-listings table tags SME at its Jun 2020 listing by introduction but the directory shows as Main Board; that move itself is unverified. REITs (8) and the three foreign-incorporated issuers (MFC, SLF, DELM) are inside the count. Cross-check: PSE's own briefing counts 280 listed companies on 14 Aug 2026 (= 282 less ATI and LAND), and the later RRHI delisting (31 Aug) and LTL listing (25 Sep) net to zero, which matches the 280 issuers derived from the directory on 6 Oct [P/I] [^pse-analyst-briefing-1h-2026:3].
- PSE sector indices on 5 Oct 2026: PSEi 5,743.21 (+114.18, +2.03%), All Shares 3,198.26, Financials 1,758.11, Industrial 7,428.99, Holding Firms 4,129.61, Property 1,765.72, Services 3,136.05, Mining & Oil 19,566.95, PSE DivY 1,721.63, MidCap 1,750.91; day's volume 414,323,178 shares, 70,275 trades, value PHP3,742,813,171.58 [P] [^pse-composite-sector-frame].
- PSEi composition from 3 Aug 2026 (30 names; MYNLD replaced CNVRG; 2 REITs: AREIT, RCR) [P] [^pse-cn-2026-0035:1] [^pse-cn-2026-0035:2]. Index eligibility needs free float >= 20% of outstanding shares; revised index policy (applies to the next, Jan–Dec 2026 review) uses Median Trading Activity Ratio >= 15% (10% for incumbents) and top-25% monthly ADV rank in >= 9 of 12 months for major indices (7% MTAR, top 50%, 8 of 12 for sector indices) [P] [^pse-press-rcr-psei] [^pse-press-mynld-psei].
- Market size/turnover: total market capitalisation PHP20.01tn (2024), PHP18.73tn (2025), PHP19.44tn (6M26); ADV PHP6.10bn (2024), 7.33bn (2025), 7.72bn (6M26) [P] [^pse-asm-2026-president-report:6]. PSE press (29 Dec 2025): *domestic* market cap PHP13.65tn vs PHP14.57tn (-6.29%), PSEi 6,052.92 (-7.29% YTD), net foreign selling PHP51.78bn, ADV PHP7.33bn [P] [^pse-press-last-trading-day-2025]. ICT became the first PHP2tn stock (PHP2.01tn close on 14 Jul 2026) [P] [^pse-press-icts-p2t]. **Definition of "total" vs "domestic" MCAP (PSE monthly reports): "Domestic MCAP … excludes three foreign companies"** — Dec 2025: total PHP18.73tn vs domestic PHP13.65tn; Aug 2026: total PHP19.82tn (Jul: 20.14tn) vs domestic PHP13.06tn (Jul: 13.32tn), i.e. ~PHP5.1–6.8tn (26–34%) of "total" MCAP is foreign-incorporated issuers [P] [^pse-monthly-report-2025-12:2] [^pse-monthly-report-2026-08:2]. The three foreign issuers are, by name in the directory, Manulife Financial Corp (MFC, PHP2,600/share, **10 shares traded on 5 Oct**), Sun Life Financial Inc. (SLF, PHP4,800, 105 shares) and Del Monte Pacific Ltd (DELM, PHP3.37, 26,000 shares) [I from P] [^pse-sec-frames-snapshot]; PSE ADV for "foreign issues" is ~PHP1.3–1.9m/day [P] [^pse-monthly-report-2026-08:1]. **Use domestic MCAP (PHP13.06tn, Aug 2026) as the investable base.** End-Aug 2026 PSEi 5,956.33 (-4.49% m/m, -1.60% YTD); by 5 Oct it was 5,743.21 [P] [^pse-monthly-report-2026-08:1] [^pse-composite-sector-frame].
- **Turnover by market segment and instrument type (PSE Aug 2026 monthly report; ADV in PHP m)** [P] [^pse-monthly-report-2026-08:1]: total 7,525.03 (Aug; 19 days) / 7,561.17 (YTD, 162 days); *regular market* 5,956.14 / 6,247.02 vs *non-regular market* (block/cross/other off-book) 1,568.89 / 1,314.15 (= 20.8% of Aug value; 17.4% YTD); domestic issues 7,523.47, foreign issues 1.56; **common 7,501.17, preferred 23.47 (31.67 YTD), warrants & PDR 0.35 (0.65 YTD), dollar-denominated 0.04 (0.06 YTD), SME Board 1.41 (24.35 YTD), ETF 0.93 (1.33 YTD)**; sector ADV (Aug): Services 2,096.53, Property 1,452.14, Industrial 1,407.98, Holding Firms 1,347.26, Financials 862.81, Mining & Oil 355.98. Foreign share of Aug trading 45.0% (YTD 48.3%); net foreign selling PHP16.56bn in Aug, PHP20.86bn YTD [P] [^pse-monthly-report-2026-08:2].
- Participation: foreign share of value 46.3% (2025), 49.5% (6M26) vs 46.2% (2024); retail 18.2% of value (2025) vs institutional 81.8%; 3,641,067 stock-market accounts at end-2025 (88.6% online) [P] [^pse-asm-2026-president-report:7] [^pse-asm-2026-president-report:15].

**Free-float distribution (PSE security frames, "Free Float Level", 6 Oct 2026; my tabulation)** [I from P] [^pse-sec-frames-snapshot]. PSE publishes per-security issued/listed/outstanding shares, Free Float Level, Market Capitalization (= previous close x outstanding shares), board lot, par value and Foreign Ownership Limit in each security frame. Static EPS fields in the same frames are stale (year-end Dec 2023 on 319 frames; interim 9M-Sep 2024 on 341 of 387) and are not used. **Vintage caveat**: the frame shows no as-of date for "Free Float Level"; market capitalisation in the same table is current (previous close x shares) and new listings (MYNLD, LTL, TOP) carry current floats, but a name that has stopped reporting keeps its last value — e.g. MGH shows 10.67%, exactly the figure press reported when it cured its MPO breach in Aug 2024 [S] [^insiderph-2024-08-05-metro-global-avoids-delisting] — so floats for suspended or non-reporting names may be up to ~2 years old.
| Free float of common shares | # (285 common with data) |
|---|---|
| < 10% | 4 (MFC 0.20, SLF 0.62, MM 1.37, UNH 2.92) |
| 10–20% | 52 |
| 20–30% | 96 |
| 30–40% | 54 |
| 40–50% | 38 |
| 50–60% | 22 |
| 60–70% | 8 |
| 70–80% | 4 |
| 80–90% | 5 |
| 90–100% | 2 (SFI 99.71, EG 91.0) |
Median 28.87%, mean 32.5% (open-status names only: median 28.99%; 42 of 256 open names < 20%). **Cohort cushions versus the in-force MPO** (open names): the 32 post-1 Dec 2017 listers all sit at or above 20% except PNB Holdings (LTL, 15.39% — consistent with the 15% tier now applicable to a > PHP50bn market-cap listing; LTL's market cap is PHP56.3bn), but several are pinned at the line: OGP 20.00, ASLAG 20.01, SPNEC 20.01, DMW 20.04, XG 21.14, REDC 22.31; of 222 pre-Dec-2017 listers (10% rule) 183 are >= 20% and the thinnest are CHP 10.03, BH 10.16, MBC 10.23, PHC 10.40, TFHI 10.57, FDC 10.73, FB 11.23, PSB 11.61, FGEN 11.67, BCOR 11.74. Suspended names with low float: UNH 2.92, MM 1.37 (both could be MPO cases — **unverified**), AAA 10.12, MGH 10.67 (cured an MPO breach in Aug 2024 per press; still suspended), PORT 10.00, STR 10.30, VLC 11.33. REIT floats (REIT MPO 33.33%): DDMPR 33.36, FILRT 35.03, VREIT 35.29, AREIT 36.18, CREIT 38.22, RCR 44.18, MREIT 44.71, PREIT 48.90.
**Market-cap structure (sum of frame market caps, 6 Oct)**: all common PHP19.10tn; domestic (ex MFC/SLF/DELM) PHP12.12tn; free-float-adjusted domestic PHP4.35tn (36% of domestic); top-10 names 45.8% and top-30 72.4% of domestic market cap; 1 stock >= PHP1tn (ICT PHP1.74tn), 32 >= PHP100bn, 105 >= PHP10bn, 219 >= PHP1bn. Domestic market cap by sector (PHP tn; free-float-adjusted in brackets): Industrial 2.91 (0.78), Services 2.84 (1.22), Financials 2.08 (0.86), Holding Firms 2.04 (0.79), Property 1.79 (0.57), Mining & Oil 0.44 (0.13), SME Board 0.016 (0.004). Largest: ICT 1,736bn, SM 599, BDO 590, BPI 498, MER 469, SMPH 451, AP 328, AC 320, VLC 289 (suspended, stale price), MBT 275. (Totals include suspended issues at their last price and will differ from PSE's published PHP13.06tn domestic MCAP for end-Aug 2026 because of price moves and scope.) SME Board: 9 issuers, aggregate market cap ~PHP16bn (XG 4.10bn, HTI 3.55bn, MM 3.30bn, CTS 2.27bn, LPC 0.65bn, MFIN 0.52bn, X 0.56bn, IDC 0.41bn, KPPI 0.28bn) [I].
**Foreign Ownership Limit (FOL) field**: 40% for 217 common issues, "No Limit" for 51 (incl. DELM, MFC, SLF, MONDE, OGP, SEVN, JFC, WLCON and the B-class lines), **0% for 15** (mass media: ABS-CBN, GMA Network, Manila Broadcasting, Prime Media, Manila Bulletin; mining/oil: Benguet, Lepanto A, Manila Mining A, Oriental Petroleum A; plus ATN A, F&J Prince A, Concrete Aggregates, Filsyn, Metro Alliance, Panasonic Manufacturing), 60% (Ferronickel), 30% (NRCP) [I from P]. The PDRs (ABSP, GMAP) carry "No Limit" while the underlying broadcasters are 0% — consistent with PDRs being the foreigner-accessible wrapper for 100%-Filipino media companies [I]. **Board lot (common, current price tiers)**: 1,000 shares for 116 issues, 100 for 76, 10,000 for 49, 10 for 26, 100,000 for 7, 1,000,000 for 7, 5 for 4; **par value** PHP1 for 183 issues, PHP0.10 for 25, PHP10 for 26, PHP0.01 for 13, and 38 others (PHP0.50: 8; PHP0.25: 5; PHP0.05 and PHP5: 3 each; par shown as 0 for 2 no-par issues; 17 other values) [I from P].

### Inferences
- Roughly 10% of listed common-share lines (29/285) and 37% of preferred lines (36/98) are suspended (non-tradable) at any time; index and ETF constituents need to exclude them.
- The six-sector taxonomy is stable but two micro-boards exist (SME, ETF-EQUITY) in directory filters; sector indices exclude SME names.

### Gaps
- PSE publishes no aggregate free-float histogram, MPO-compliance list or per-sector market-cap table in the sources reached; the distributions above are my tabulation of per-security frame fields. The frame's "Free Float Level" definition (which holders are excluded, as-of date) is not documented on the frame and may differ from the 2026 Revised Public Ownership Guidelines [gap].
- PSE "Capital Raised" tab of the listing-statistics page is dynamic and did not render.

### Execution implications
- Build the tradable universe from live status each morning (65 suspended symbols), then filter by float: use PSE index free-float rules (>= 20%) as a proxy for investable names.
- Use turnover concentration: top names (ICT, BDO, ...) carry the market; participation caps should use per-name ADV not market ADV.

---

## 4. Listing rules that change how securities trade

### Takeaway
The in-force minimum-public-ownership (MPO) rule is the **SEC-approved Amended MPO Rule effective 11 Aug 2026** (implementing SEC MC 11 s. 2026): tiered IPO float of 33%/25%/20%/15% by expected market cap with minimum offer sizes, 20% (15% above PHP50bn) maintenance for post-2026 listers, 20% for post-Dec-2017 listers, 10% for older listers, 33.33% for REITs; breach => **immediate trading suspension for up to 6 months, then automatic delisting** (5-year relisting ban). The suspension/delisting ladder for late filings (17-A: 3-month suspension; 17-Q: 2 months; unpaid ALMF: 2 months) explains many of today's ~65 suspended symbols (the rest are MPO cases and legacy preferred series).

### Cited findings
**4.1 Minimum public ownership — history and current rule**
- 2012: SEC approved PSE's Amended MPO Rule on 19 Dec 2011; effective 1 Jan 2012: 10% of issued/outstanding shares (ex-treasury), POR quarterly within 15 calendar days; grace periods ended 31 Dec 2012; companies non-compliant on/after 1 Jan 2013 are suspended up to 6 months then automatically delisted; Involuntary Delisting Rules do not apply but the 5-year relisting prohibition does; voluntary delisting for MPO breach needs a tender offer that yields > 90% ownership [P] [^pse-sr6-mpo-rule-2012:1] [^pse-sr6-mpo-rule-2012:3] [^pse-sr6-mpo-rule-2012:6] [^pse-sr6-mpo-rule-2012:7] [^pse-sr6-mpo-rule-2012:8].
- 1 Dec 2017: SEC MC 13 s. 2017 raised IPO MPO to 20% (maintain at all times, 12 months to cure) [P] [^pse-sr6-2-mpo-initial-backdoor-2020:3]. 3 Aug 2020 (CN-2020-0076, effective immediately): IPO offer size 33%/PHP50m (mcap <= PHP500m), 25%/PHP100m (PHP500m–1bn), 20%/PHP250m (> PHP1bn), maintain >= 20%; LBWI and backdoor listings need >= 20% float upon and after listing [P] [^pse-sr6-2-mpo-initial-backdoor-2020:1] [^pse-sr6-2-mpo-initial-backdoor-2020:4]. CLDR Main-Board note: floor 10% generally, 20% for companies under the 2020 guidelines [P] [^pse-listing-disclosure-rules:51].
- Aug 2023 consultation (CN-2023-0041, comments to 8 Sep 2023): codify tiers (10% / 20% / REIT 33.33%); monthly-POR triggers 12% / 24% / REIT 39.996%; delete 2012 grace provisions; state that BIR rules impose capital-gains and documentary-stamp tax on trading of shares of non-MPO-compliant companies (reason no grace is possible) [P] [^pse-cn-2023-0041-mpo-delisting-consult:7] [^pse-cn-2023-0041-mpo-delisting-consult:8] [^pse-cn-2023-0041-mpo-delisting-consult:9].
- Mar 2025 (secondary): SEC approved temporary reduction of the IPO public float requirement from 20% to 15% for an initial 2-year period (extendable), with follow-on/private placement within 2–3 years to reach 20%; PSE did not publicise widely [S] [^tribune-pse-eases-float-2025]. No PSE circular for this relief was found [gap]. PSE CEO on 29 Dec 2025: "looming changes in REIT rules and IPO float requirements should result in more listings" [P] [^pse-press-last-trading-day-2025].
- **2026**: SEC MC 11 s. 2026 (issued 24 Feb 2026 [S]; effective after publication in two newspapers; PSE given 3 months to conform — draft text in CN-2026-0020 Annex A) [P] [^pse-cn-2026-0020-mpo-consult:10] [^cruzmarcelo-sec-mc11-2026]. Timeline: PSE consultation 13 May 2026 (comments to 20 May) -> submitted to SEC 25 May -> SEC letter 14 Jul approving with revisions -> second exposure draft 16 Jul (comments to 21 Jul) -> **PSE memo 11 Aug 2026: SEC-approved Amended MPO Rule and Revised Public Ownership Guidelines "take effect immediately"** [P] [^pse-cn-2026-0020-mpo-consult:1] [^pse-mpo-second-exposure-2026-07:3] [^pse-amended-mpo-rule-2026-08:1].
- **In-force MPO table (11 Aug 2026)** [P] [^pse-amended-mpo-rule-2026-08:2] [^pse-amended-mpo-rule-2026-08:3]:
  | Cohort | Initial (IPO) | Maintaining |
  |---|---|---|
  | Listed before SEC MC 13-2017 (1 Dec 2017) | 10% | 10% |
  | Listed after MC 13-2017, before MC 11-2026 | 20% | 20% |
  | Listed after MC 11-2026, expected mcap <= PHP500m | 33% | 20% |
  | … PHP500m–1bn | 25% (min offer PHP165m) | 20% |
  | … PHP1bn–50bn | 20% (min offer PHP250m) | 20% |
  | … > PHP50bn | 15% (min offer PHP10bn) | 15% |
  | REIT | 33.33% | 33.33% |
  Preferred and treasury shares excluded from the computation; the maintaining tier is keyed to market capitalisation *at the time of listing*, not to current market cap. Large-issuer relief: expected mcap >= PHP200bn may get a lower initial MPO, never below 12%, and the maintaining MPO may not be lower than the approved initial MPO; conditions: evidence of better distribution/liquidity, full disclosure compliance and enhanced disclosures, liquidity safeguards (Section 2(c)) [^pse-amended-mpo-rule-2026-08:3] [^pse-amended-mpo-rule-2026-08:4].
- **Compliance mechanics** [P] [^pse-amended-mpo-rule-2026-08:5] [^pse-amended-mpo-rule-2026-08:6]: immediate disclosure when float falls below MPO (Art. VII 4.1); monthly internal float computation; cure within max 6 months from the breach; Compliance Plan due within 10 days of breach; quarterly POR within 15 calendar days of quarter-end; **interim POR immediately** after any transaction that pushes float below MPO; LBWI companies must show MPO compliance at filing; backdoor-listed companies must comply immediately; sanctions: **immediate suspension of trading for up to 6 months from the date of breach** (a Compliance Plan does not defer it), during which the company may restore float or petition for voluntary delisting; if still non-compliant => **automatic delisting** (Involuntary Delisting procedure does not apply; **5-year relisting prohibition** and director/principal-officer disqualification apply unless the person shows reasonable measures/due diligence); if a timely voluntary-delisting petition is pending, PSE may defer automatic delisting; transitional: pre-effectivity cases stay under old rules [^pse-amended-mpo-rule-2026-08:6] [^pse-amended-mpo-rule-2026-08:7].
- **Revised Public Ownership Guidelines (2026)**: non-public = >= 10% holders; holders with a board seat; directors, principal officers, chairman emeritus; parent/subsidiary/affiliate/associate; controlling shareholders; employer-plan shares (even unpaid). Public = small individual holdings, trading participants (unless non-public), **funds incl. SSS/GSIS regardless of size unless they hold a board seat**, **shares in the PCD Nominee account**, and **underlying shares of PDRs and of overseas depositary receipts**; only outstanding common shares count (directors include independent directors; PCD-Nominee shares are classified as indirect holdings in the POR) [^pse-amended-mpo-rule-2026-08:9] [^pse-amended-mpo-rule-2026-08:10] [^pse-amended-mpo-rule-2026-08:11].
- **Live example**: Robinsons Retail Holdings (RRHI) — tender offer by JE Holdings (Gokongwei family vehicle) at PHP48.30, 25 May–6 Jul 2026, took float to 0.31% [S]; PSE **suspended trading effective 13 Jul 2026** and removed RRHI from PSE DivY/MidCap/Services indices from 16 Jul (index counts fell to 19) [P]; company sought voluntary delisting targeted 28 Jul 2026 [S]; **PSE approved the voluntary delisting on 20 Aug 2026 (CN-2026-0038) and RRHI left the official registry effective 31 Aug 2026** — i.e. 7 weeks of suspension before removal [P] [^pse-cn-2026-0038-rrhi-voluntary-delisting:1] [^pse-delisted-companies-web]; RRHI is absent from the 6 Oct directory [I] [^pse-cn-2026-0032-rrhi-index-removal:1] [^philstar-rrhi-suspension] [^pse-listed-company-directory-frame]. This happened *before* the 11 Aug rule but under the 2012 rule's identical suspend-then-delist ladder (see SR 6 above) [I].
- **Other live MPO cases (pre-2026 rule text, same ladder)**: (i) *ATI (Asian Terminals)* — tender-offer results (177,612,478 shares) and a 31,721,200-share block were crossed as **special block sales at PHP3.60 on 13 Mar 2026** (PHP6.39bn + PHP1.14bn = PHP7.54bn); PSE announced beforehand that it would suspend ATI after execution for MPO non-compliance (TPA-2026-0012, 12 Mar), approved the voluntary-delisting petition on 25 Mar (CN-2026-0013) and removed it from the registry on 3 Apr 2026, i.e. about three weeks suspended [P] [^pse-tpa-2026-0012-block-sale-ati-tender-offer:1] [^pse-cn-2026-0013-ati-voluntary-delisting:1]; (ii) *Steniel (STN)* — non-compliant and suspended from 22 May 2023 with automatic delisting due after six months (CN-2023-0058 of 23 Oct 2023); it trades again today (last PHP1.95, frame float 28.81%), i.e. it cured [P/I] [^pse-cn-2023-0058-steniel-mpo-non-compliance:1] [^pse-sec-frames-snapshot]; (iii) *Metro Global Holdings (MGH)* — suspended from 5 Feb 2024, automatic delisting due 5 Aug 2024 (CN-2024-0037A of 16 Jul 2024); it avoided delisting when its parent FEMI transferred 55m shares (~2% of the 2.75bn outstanding) to Smart Share Investments Ltd, lifting the public float to 10.67% [P/S] [^pse-cn-2024-0037a-metro-global-mpo-non-compliance:1] [^insiderph-2024-08-05-metro-global-avoids-delisting] — yet MGH still shows *Suspended* on 6 Oct 2026 (reason not verified) [P] [^pse-sec-frames-snapshot].

**4.2 IPO lock-ups and listing-day mechanics (CLDR, Jan 2025 edition)**
- **Main Board lock-up** (Art. III Part D Sec. 2, as amended by MEA 2022-0003, 13 Jun 2022): existing holders of >= 10% must not dispose for **180 days** from listing if the issuer meets the track-record test, **365 days** if exempt from track record (mining, oil, renewable, holding companies using subsidiary track record); shares issued/transferred in the 180 days before the offer at a price below the IPO price are locked for **365 days from full payment**; carve-out for alternative-investment-fund holders exercising instruments held >= 365 days and selling in the IPO; must be stated in Articles; lock-up of Main-Board transferees from SME counted [P] [^pse-listing-disclosure-rules:52] [^pse-listing-disclosure-rules:53] [^pse-listing-disclosure-rules:54]. **SME**: non-public holders and related parties locked up 1 year after listing (shares issued below IPO price in prior 180 days: 365 days) [P] [^pse-listing-disclosure-rules:60] [^pse-listing-disclosure-rules:61]. Implementation by PDTC electronic lock-up or escrow; PSE needs the escrow agreement >= 7 calendar days before the offer; alternative arrangements allowed only if 98% is escrowed and insiders are escrowed [P] [^pse-listing-disclosure-rules:41] [^pse-listing-disclosure-rules:42]. Voluntary lock-up release must be notified 10–15 trading days before expiry (Art. VII Sec. 11) [P] [^pse-listing-disclosure-rules:148].
- **2021 re-cut of Main/SME criteria (what it replaced)**: SEC approved on 4 Feb 2021 the amended Art. III Parts D and E and the new Part E-1 (sponsor model); PSE CN-2021-0021 (24 Mar 2021, effective immediately) replaced the 2013 Main/SME rules (CN-2013-0023). Alongside, SEC granted **temporary COVID relief for IPO applications filed in 2021 and 2022**: PSE may judge profitability on any two of the three most recent fiscal years excluding the COVID-impact year (e.g., 2018–19 for a 2021 filing), with extra prospectus disclosure on the pandemic [P] [^pse-cn-2021-0021-amended-listing-rules:1] [^pse-cn-2021-0021-amended-listing-rules:2]. Pre-2021 (2013) thresholds as reported by press: Main Board needed authorised capital >= PHP500m, 3-year history and cumulative EBITDA >= PHP50m; SME Board authorised capital >= PHP100m with >= 25% subscribed and paid-up [S, from a search-result summary of Inquirer's 2013 report; page itself returned HTTP 403, so unverified] [^inquirer-sec-revamps-boards-2013]. The 2021 text instead tests net income (Main) or cumulative EBITDA/revenue growth (SME) plus stockholders' equity (PHP500m Main / PHP25m SME), not authorised capital [^pse-listing-disclosure-rules:50] [^pse-listing-disclosure-rules:57].
- **Post-IPO restrictions**: a newly listed company may not offer additional securities (except stock dividends/ESOP) within 180 days of listing [P] [^pse-listing-disclosure-rules:55]. Holding companies relying on a subsidiary's track record cannot divest it for 3 years [^pse-listing-disclosure-rules:54].
- **Stabilisation / greenshoe**: Art. III Part A Sec. 13 (stabilisation fund required for secondary offerings): fund of 10–15% of base offer (offers <= PHP10bn), 12.5–15% (PHP10–25bn), 15% (> PHP25bn); stabilisation may not breach MPO; weekly report to PSE; SEC prior approval required [P] [^pse-listing-disclosure-rules:38] [^pse-listing-disclosure-rules:39]. Over-allotment options appear in recent deals (MYNLD: up to 249.05m primary OA shares; GCASH: up to 1.20bn secondary OA shares) [P] [^pse-press-maynilad-greenlight] [^pse-press-mynt-ipo-approval]. The stabilisation-fund section was inserted as new Art. III Part A Sec. 13 by **CN-2023-0022 (12 May 2023; SEC-approved; effective immediately)** [P] [^pse-cn-2023-0022-stabilization-fund:1] [^pse-cn-2023-0022-stabilization-fund:2].
- **Distribution**: book-building for up to 60% to QIBs; **Local Small Investor (LSI) tranche >= 10%** of the IPO (subscription <= PHP100,000 per investor; clawback to 15% if LSI demand >= 5x; balloting if exceeded); balance >= 30% to the general public, of which 20% of offer shares sold through Trading Participants; offer period >= 5 trading days; listing within 10 calendar days after the offer period; LSIs subscribe through PSE EASy [P] [^pse-listing-disclosure-rules:77] [^pse-listing-disclosure-rules:78] [^pse-listing-disclosure-rules:79] [^pse-listing-disclosure-rules:80] [^pse-press-maynilad-greenlight].
- **First-day price limits**: no IPO-specific rule found. New securities start at the 20% dynamic threshold [^pse-implementing-guidelines-trading-rules:11]; if an IPO does not trade on listing day the next-day static threshold is based on the company's indicative reference opening price [^pse-implementing-guidelines-trading-rules:11]; the static band is +50%/-30% of the reference price (since 24 Mar 2020) except for warrants and on an LBWI listing day (lifted) [^pse-cn-2020-0028:1] [^pse-revised-trading-rules:34]. Whether the IPO reference price on day 1 is the offer price is **not stated** in the archived rule text [gap]; press evidence in the price-controls chapter is consistent with it (Medilines IPO at PHP2.30 "tanked 30%" on its 7 Dec 2021 debut, i.e. the -30% floor measured from the offer price) [S] [^philstar-2021-12-07-medilines-debut]. Observed: AGIW (+100% on day 1); LTL (LBWI) listed at PHP1.20 initial listing price [P] [^pse-press-agi-warrants] [^pse-press-pnb-holdings-lbwi].
- **Listing by way of introduction (LBWI)**: allowed e.g. where an unlisted issuer's shares are distributed as a property dividend by a listed issuer; initial price set with a fairness opinion; trading band lifted on listing date; lock-up per board rules (or 180 days from listing/offer for mandated-listing cases); mandatory public offering within 1 year for mandated/closely-held cases, else suspension/ALMF doubling/buy-back and delisting [P] [^pse-listing-disclosure-rules:83] [^pse-listing-disclosure-rules:84] [^pse-listing-disclosure-rules:87] [^pse-listing-disclosure-rules:88]. Example: PNB Holdings (LTL) listed 46.93bn shares on 25 Sep 2026 (23.9bn distributed as property dividend by PNB) at PHP1.20 [P] [^pse-press-pnb-holdings-lbwi].

**4.3 Follow-ons, rights, additional listing**
- **Follow-on offerings** (Art. V Part F): offer-price range disclosed at filing with a floor <= market price; LSI allocation mandatory; offer period >= 5 trading days; shares issued at a discount in the prior 180 days cannot be sold in the offer (amendments effective 16 Apr 2024, CN-2024-0024) [P] [^pse-listing-disclosure-rules:124] [^pse-listing-disclosure-rules:125].
- **Stock rights offerings** (Art. V Part B): file within 90 days of board approval, price range (floor/cap) disclosed; underwriter takes up unexercised rights after second round; **record date >= 15 trading days after PSE board approval**; the CLDR note says the Exchange sets the ex-date automatically at 3 trading days before the record date (T+3-era wording, never updated), but since the T+2 migration the ex-rights date is **1 trading day before the disclosed record date** (CN-2023-0031); offer period starts <= 30 calendar days after record date [P] [^pse-listing-disclosure-rules:106] [^pse-listing-disclosure-rules:107] [^pse-cn-2023-0031-t2-settlement:1]. **Rights are not listed as separate securities**: no rights ticker appears in the directory and the CLDR has no rights-trading provision (rights = entitlement of holders of record) [I; absence of evidence]. Examples: Globe SRO 28 Oct 2022; PBB 31 Mar 2023; UnionBank 31 May 2024; Phinma 27 Nov 2024 [P] [^pse-new-listings-ipo-web].
- **Additional listing rule** (private placements/swaps of 10%–35%): triggers a **1-hour trading halt on announcement and another 1-hour halt on dissemination of the comprehensive corporate disclosure**; related-party subscriptions need a rights/public offer or minority waiver (180-day lock-up); price at a premium to the 30-day weighted close exempts [P]; live example: on 19 Jan 2026 MRC Allied (MRC) disclosed approval of 315,000,000 additional shares at PHP1.00 to two named subscribers (treated as covered by the Additional Listing Rule via a 2017 up-to-PHP1bn issuance) and PSE imposed a one-hour halt, 9:30–10:30 a.m. [P] [^pse-cn-2026-0004-2-emergency-disclosures-trading-halt:2] [^pse-listing-disclosure-rules:98] [^pse-listing-disclosure-rules:99] [^pse-listing-disclosure-rules:100] [^pse-listing-disclosure-rules:101] [^pse-listing-disclosure-rules:104]. Fine for lodging/trading unlisted shares: 15% of market value + PHP2,000/day or PHP5m (higher) [P] [^pse-listing-disclosure-rules:105].
- **Listing deadlines for newly issued shares (SR 20 = CN-2023-0012 of 21 Mar 2023; SEC-approved; effective on posting to PSE's website)** [P] [^pse-sr20-listing-issued-outstanding-shares-2023:1] [^pse-sr20-listing-issued-outstanding-shares-2023:2] [^pse-sr20-listing-issued-outstanding-shares-2023:3] [^pse-sr20-listing-issued-outstanding-shares-2023:4]: all issued and outstanding securities of a listed company of the same class, including treasury shares, must be listed. The listing application is due within **60 calendar days of full payment** for private placements and share swaps (full payment itself within 1 year of subscription or closing), **60 calendar days of stockholders' approval** (or of SEC approval of the capital increase) for stock dividends, **90 calendar days of board approval** for rights offerings, 60 days from conversion/exercise of convertibles and 60 days from issuance/full payment for ESOP/ESPP shares; the periods are non-extendible. Penalties per violation in a rolling five-year window: PHP100k, 200k, 300k, 500k, then a **2-month trading suspension** on the fifth and delisting grounds thereafter, plus PHP2,000 per trading day until the application is filed. After approval the issuer has 60 days (extendible by 30) to satisfy the Notice-of-Approval conditions or the approval lapses. Execution relevance [I]: shares issued in placements or as stock dividends can stay unlisted, hence untradable, for weeks to months after issue, so share-count and float changes show up in PSE data with a lag.
- **Dividends/splits**: record date must be disclosed >= 10 trading days ahead; payment date <= 18 trading days after record date (cash and stock dividends lodged with PDTC remitted within 18 trading days) [P] [^pse-listing-disclosure-rules:146] [^pse-listing-disclosure-rules:147]; splits/reverse splits, stock dividends and capitalisation issues are Art. VII 4.4 disclosure events [P] [^pse-listing-disclosure-rules:143]. SEC MC 2-2009 (via Guidance Note 19): cash-dividend record date must be **not less than 10 nor more than 30 days** after declaration (default 15 days if unspecified); one declaration may cover several dividends in a year if record and payment dates are given [P] [^pse-gn19-sec-mc-2-2009-rights-dividends:1]. T+2 settlement started on trade date 24 Aug 2023 (SEC en banc approval 10 Aug 2023); for corporate actions from that date the **ex-rights date is one trading day before the disclosed record date**, and ex-dates of already-disclosed actions were re-set via amended disclosures (CN-2023-0031 of 23 Jun 2023) [P] [^pse-cn-2023-0031-t2-settlement:1] [^pse-cn-2023-0040-t2-go-live:1]; the Jan-2025 CLDR Note to Art. V Part B Sec. 7 still prints the old 3-trading-day rule [^pse-listing-disclosure-rules:107] — PSE's per-event notice is authoritative. **ALMF**: upper limit raised from PHP2.0m to **PHP3.5m** per listed company (floor PHP250k; SME unchanged PHP50k–250k) effective 2 Jan 2025 (CN-2024-0068) — PSE's IPO page still shows the old PHP2m cap [P] [^pse-cn-2024-0068-almf-effectivity:1] [^pse-ipo-listing-requirements-web]. **Sector classification rule**: a company is classified where >= 60% of revenue arises; 13 companies were reclassified effective 5 Jan 2026 (e.g., DITO: IT -> Telecommunications; ECVC -> Mining; ATN: Holding -> Industrial/Construction; UNH -> Property; WIN: Holding -> Property; PHA, JAS -> Property) [P] [^pse-cn-2025-0047-sector-reclassification:1] [^pse-cn-2025-0047-sector-reclassification:2].

**4.4 Delisting and tender offers**
- **Involuntary delisting** (SR 8): grounds include non-compliance with listing agreement/rules, false market, negative stockholders' equity (Main/SME rules: delisting after 3 consecutive years of negative equity, effective 30 days after Board approval), registration revoked, repeated disclosure failures, not in commercial operation within 2 years of listing; hearing right (request within 15 working days), one motion for reconsideration; **5-year relisting ban** [P] [^pse-sr8-delisting-rules:1] [^pse-sr8-delisting-rules:2] [^pse-sr8-delisting-rules:3] [^pse-sr8-delisting-rules:4] [^pse-listing-disclosure-rules:56] [^pse-listing-disclosure-rules:63].
- **Voluntary delisting (in force since 21 Dec 2020, SR 8.1)** [P] [^pse-sr8-1-voluntary-delisting-2020:1] [^pse-sr8-1-voluntary-delisting-2020:3] [^pse-sr8-1-voluntary-delisting-2020:4]: approval by >= 2/3 of the entire board incl. a majority (and >= 2) of independent directors **and** holders of >= 2/3 of outstanding-and-listed shares, with votes against <= 10%; petition + tender-offer report >= 60 days before delisting; tender offer to all holders of record; **minimum tender price = higher of (i) highest valuation in an independent fairness opinion (SRC Rule 19.2.6) and (ii) 1-year VWAP before the board-approval disclosure** (fairness-opinion value only if suspended >= 1 year); proponents must end with >= **95%** of issued and outstanding shares; no unpaid fees; voluntary delisting fee = one ALMF; relisting treated as new listing (no 5-year ban for an ordinary voluntary delisting) — **except** that under the 11 Aug 2026 MPO rule a voluntary delisting approved *because of an MPO breach* (the typical post-tender-offer case such as ATI or RRHI) also carries the 5-year relisting prohibition and the director/principal-officer disqualification (Sec. 6(d)) [P] [^pse-amended-mpo-rule-2026-08:6]. Proposed in Aug 2023 (CN-2023-0041): 2/3 vote on *issued* and outstanding shares, replace the 95% test by an MPO-aligned test, mandatory tender offer [P] [^pse-cn-2023-0041-mpo-delisting-consult:14]; adoption status **unconfirmed** (2026 MPO rule refers to "Amended Voluntary Delisting Rules") [gap]. Recent approvals: Eagle Cement (Feb 2023), 2GO (Jun 2023), MPIC (Sep 2023), Premium Leisure (Jun 2024), SFA Semicon (Dec 2024), Keppel Philippines (Jun 2025), 8990 Holdings (Oct 2025), Asian Terminals (Mar 2026); involuntary: Unioil, PICOP (May 2023), Philab (Jun 2025) [P] [^pse-circular-index-2025-2026] [^pse-delisted-companies-web].
- **Backdoor listing** (SR 7 = Revised Rules on Backdoor Listing, CN-2022-0026 of 22 Jun 2022, amending CN-2022-0024 of 26 May 2022) [P] [^pse-sr7-backdoor-listing-2022:1] [^pse-sr7-backdoor-listing-2022:3] [^pse-sr7-backdoor-listing-2022:4]: deemed to occur when a listed company acquires shares/assets of an unlisted party (or vice versa) resulting in **change of control (> 50% voting power)**, change of de facto control (acquirer becomes single largest holder) or a **substantial change in business (acquired business/assets > 50% of total assets)**; PSE **suspends trading immediately after evaluating the disclosure** and lifts it one full trading day after the comprehensive corporate disclosure (and SEC confirmations) are disseminated; a one-hour halt accompanies disclosure of the final price of the mandatory follow-on offering; 20% public float required immediately [^pse-sr6-2-mpo-initial-backdoor-2020:4] [^pse-amended-mpo-rule-2026-08:6].

**4.5 Trading suspensions and halts for non-compliance (CLDR)**
- *Disclosure halts*: issuer must disclose material information within **10 minutes**; during trading hours it must request a halt; the halt lifts **1 hour after dissemination** (next trading day if disseminated <= 1 hour before close); halt allows order entry except crosses; **suspension** blocks posting/modification/cancellation and any TP action [P] [^pse-listing-disclosure-rules:139] [^pse-listing-disclosure-rules:140]. PSE's EDGE disclosure cut-off was 3:30 pm (CN-2022-0010, from 1 Mar 2022) and was **moved to 4:00 pm effective 25 May 2026 (CN-2026-0024)**; filings after the cut-off are posted on the next trading day [P] [^pse-cn-2026-0024-edge-cutoff-4pm:1] [^pse-cn-2022-0010-edge-cutoff-330pm:1] [^pse-listing-disclosure-rules:139]. PSE-requested clarification of market rumours: if no reply, halt until 10:00 am; reply due by 11:00 am else fines PHP30,000 + PHP10,000 per 30 minutes [^pse-listing-disclosure-rules:145] [^pse-listing-disclosure-rules:146]. Substantial acquisition of an unlisted company >= 10% of the issuer's book value => suspension until terms disclosed [^pse-listing-disclosure-rules:146]. Failure to appoint a replacement transfer agent => suspension [^pse-listing-disclosure-rules:148].
- *Late reports*: **17-A (annual) due 105 days after FY-end**; after basic fine and 15 days of daily fines PSE warns, then **automatic suspension for a maximum of 3 months** (no daily fines during suspension), then delisting procedures; **17-Q due 45 days** after quarter-end; 10 days of fines then **2-month suspension**, then delisting procedures [P] [^pse-listing-disclosure-rules:153] [^pse-listing-disclosure-rules:154] [^pse-listing-disclosure-rules:155].
- *Fees*: ALMF unpaid after 15 Feb => automatic 2-month suspension (to 15 Apr), then delisting consideration [P] [^pse-ipo-listing-requirements-web].
- **Live case — Villar group (late-filing suspensions, May–Jun 2026)**: eleven symbols show last data on 29 May 2026 (INFRA, VLC, VLL2A) or 1 Jun 2026 (ALLDY, HOME, MM, STR, T, VLL, VLL2B, VREIT) and are still *Suspended* on 6 Oct 2026 (Petron PRF3B also stopped on 1 Jun and UNH on 22 May; the Villar-group attribution is my inference from names, except VLL, VREIT, ALLDY and HOME, which PSE's index-review circular names) [P/I] [^pse-sec-frames-snapshot]; press: six of seven Villar-listed companies (~PHP320bn) suspended for nearly three months due to overdue financial filings (24 Aug 2026), Q2 reports also late [S] [^insiderph-villar-frozen]; PSE removed VLL/VREIT (Property) and ALLDY/HOME (Services) from the sector indices on 3 Aug 2026 [P] [^pse-cn-2026-0035:1]. The CLDR 3-month ceiling would have expired ~end Aug–Sep 2026; the shares are still suspended >4 months on — outcome/extension **unverified** [gap].
- DDS suspension example: DMPA1/DMPA2 suspended since 2022 (see Q1). Long-dated suspensions: AAA (since May 2015), PORT (May 2014), FBP (Feb 2015), ACPA (Nov 2013), SMCP1 (Oct 2012) [P] [^pse-sec-frames-snapshot].

### Inferences
- The MPO rule is now a *hard* liquidity-event generator: any tender offer/placement that pushes a 10%/20%/33.33% name below its cohort threshold triggers an immediate suspension, not a cure period — ATI (Mar 2026) and RRHI (Jul 2026; the first mega-cap) are the 2026 examples. Orders in the name stop; positions cannot be exited on-exchange until delisting/tender mechanics.
- Late-filing suspensions cluster in mid/late May: last-trade dates of today's suspended common names fall on 15–16 May (PORT 2014, AAA 2015, MJC 2023, PNX 2024, I-Remit 2025) and 20 May (ROX 2024); the 2026 stoppages came later (UNH 22 May; INFRA, VLC 29 May; the other Villar names 1 Jun) [I from P frames; consistent with the Art. VII 17.8 ladder — 17-A due on day 105, then fines, warning and automatic suspension — but PSE's per-case suspension notices were not retrieved].

### Gaps
- Primary text of SEC MC 11-2026 and SEC MC 1-2026 (sec.gov.ph 403 to curl/WebFetch; Wayback 429) — only draft annex (in CN-2026-0020) and secondary summaries.
- IPO day-1 limit mechanics (is the offer price the day-1 reference price?); whether the voluntary-delisting amendments proposed in 2023 were adopted; outcome or extension of the Villar-group suspensions beyond the CLDR 3-month ceiling; a PSE circular for the Mar 2025 temporary 15% IPO float relief; why MGH is still suspended two years after curing its MPO breach.

### Execution implications
- For event risk screening use a "float cushion" measure: free float minus cohort MPO (10/20/33.33/15%); names within a few percentage points of the threshold with a pending tender offer/placement carry suspension (zero-liquidity) tail risk.
- Tender offers that take a name below its MPO have been settled as **special block sales** with the suspension announced in the same PSE notice (ATI: block execution Fri 13 Mar 2026, suspension straight after; RRHI: tender offer closed 6 Jul, suspended effective 13 Jul) — the last on-exchange exit is the tender window itself, so positions in names with a live tender offer should be resolved (tender, hedge via SBL where borrowable, or sell) before the offer expires [P/S] [^pse-tpa-2026-0012-block-sale-ati-tender-offer:1] [^philstar-rrhi-suspension].
- Rights/stock-dividend/cash-dividend ex-dates: ex-date = record date minus 1 trading day since 24 Aug 2023 (CN-2023-0031), not the 3 days still printed in the Jan-2025 CLDR; the last cum-date is therefore two trading days before the record date; cum/ex adjustments are applied to the reference price (Last Adjusted Closing Price) [P] [^pse-cn-2023-0031-t2-settlement:1] [^pse-cn-2026-0031-negotiated-trades:3].
- LBWI listing-day price is unconstrained by the static band; expect extreme volume (LTL: 73.8m shares on day 6).
- Event feeds: the EDGE disclosure cut-off is 4:00 pm since 25 May 2026 (earlier: 3:30 pm), and the EDGE portal itself was unavailable on 6 Oct 2026 with PSE directing the public to pse.com.ph for disclosures — do not rely on a single EDGE scraper for halt/suspension triggers [P] [^pse-cn-2026-0024-edge-cutoff-4pm:1] [^pse-cn-2026-0046-edge-outage-access-to-disclosures:1].
- Resumption after a suspension of >= 1 year lifts the static threshold on the resumption day (Q1) — relevant to the Villar names if they stay suspended past June 2027 and to legacy suspended preferreds.

---

## 5. IPO pipeline and listing trends 2020–2026

### Takeaway
IPO activity collapsed from 8–10 per year (2021–22) to 2–3 per year (2023–25), then came back in value terms: **Maynilad PHP34.34bn (7 Nov 2025, 2nd largest ever)**; **Mynt/GCash (GCASH) ~PHP92bn pricing 1 Oct, offer 6–12 Oct, listing ~19–20 Oct 2026 — would be the largest**; Vitro REIT ~PHP24bn (listing ~12 Oct 2026). 1H-2026 had no IPOs; capital raising was FOO/preferred-led.

### Cited findings
- **IPO and LBWI list from PSE's "New Listings/IPO" page (through 8 Apr 2025)** [P] [^pse-new-listings-ipo-web]: 2020: Altus Property (APVI, LBWI, SME, 26 Jun), MerryMart (MM, SME, 15 Jun [sic]), AREIT (13 Aug), Converge (CNVRG, 26 Oct); 2021: DDMPR (24 Mar), Monde Nissin (MONDE, 1 Jun), FILRT (12 Aug), RCR (14 Sep), MREIT (1 Oct), AllDay Marts (3 Nov), Medilines (7 Dec), SP New Energy (SPNEC, 17 Dec); 2022: Haus Talk (SME 17 Jan), Figaro (24 Jan), CREIT (22 Feb), Bank of Commerce (31 Mar), CTS Global (SME 13 Apr), Raslag (6 Jun), VistaREIT (15 Jun), Balai ni Fruitas (30 Jun), LFM Properties (LBWI 9 Nov), Premiere Island Power REIT (15 Dec); 2023: Alternergy (24 Mar), Upson (3 Apr), Repower (24 Jul); 2024: OceanaGold Philippines (13 May), Citicore Renewable (7 Jun), NexGen Energy (SME 16 Jul); 2025: Top Line Business Development (TOP, 8 Apr), Maynilad (MYNLD, 7 Nov — from directory/PSE press); 2026: PNB Holdings (LTL, **LBWI**, 25 Sep).
- PSE annual counts (new listings): 8 (2021), 10 (2022), 3 (2023), 3 (2024), 2 (2025) [P] [^pse-listing-statistics-web]. (The IPO-page list shows more SME-tagged 2022 names than the statistics table's "SME 4" — classification differences, unresolved.)
- **IPO proceeds by deal (PSE press releases; PHP)** [P]: 2020 — AREIT 12.34bn [^pse-press-areit-debut]; Converge 29.08bn incl. OA (then the biggest IPO) [^pse-press-converge-ipo]. 2021 — **Monde Nissin 55.89bn (largest IPO in PSE history; June 2021)** [^pse-press-monde-ipo]; FILRT 12.58bn [^pse-press-filrt-listing]; RCR 23.53bn [^pse-press-rcr-listing]; MREIT 15.29bn (~2x covered) [^pse-press-mreit-listing]; AllDay Marts 4.5bn (LSI tranche 1.62x) [^pse-press-allday-listing]; SP New Energy 2.7bn [^pse-press-spnec-ipo]; DDMPR offer up to 5.94bn secondary shares at up to PHP2.25 [^pse-press-ddmpr-approval]. 2022 — Haus Talk 0.75bn [^pse-press-haus-talk]; CREIT 6.40bn [^pse-press-creit-listing]; Bank of Commerce 3.36bn [^pse-press-bncom-listing]; CTS Global (SME) 1.375bn [^pse-press-cts-listing]; Raslag 0.70bn [^pse-press-raslag-listing]; VREIT 7.5bn shares listed, "smallest REIT" by capital raised [^pse-press-vreit-listing]. 2023 — Alternergy 1.62bn [^pse-press-alter-listing]; Upson 1.50bn + 0.15bn secondary OA [^pse-press-upson-listing]; Repower 1.05bn [^pse-press-redc-listing]. 2024 — OceanaGold Philippines 6.08bn (secondary) [^pse-press-ogp-listing]; Citicore Renewable 5.30bn (incl. US$12.5m from MOBILIST) [^pse-press-crec-listing]; NexGen (SME) 0.504bn [^pse-press-nexgen-listing]. 2025 — Top Line 0.733bn [^pse-press-top-listing]; Maynilad 34.34bn [^pse-press-maynilad-ipo]. Cross-check: 2024 deals sum to 11.88bn vs PSE's 11.91bn IPO bar; 2025 deals sum to 35.07bn = PSE's 35.07bn IPO bar [I from P] [^pse-asm-2026-president-report:8].
- **Total capital raised via primary + secondary shares (PSE year-end/half-year releases)** [P]: 2020 PHP103.76bn; 2021 PHP234.48bn; 2022 PHP110.29bn (nine IPOs — most since 2007 — plus one LBWI, five SROs, 12 private placements; domestic market cap PHP16.56tn, -8.4%); 2023 PHP140.95bn; 2024 PHP82.37bn; 2025 PHP144.14bn; 1H21 PHP122.46bn (incl. Monde Nissin) and 1H22 PHP61.92bn (eight IPOs, one SRO, four placements) [^pse-press-1h2021-capital] [^pse-press-last-trading-day-2022] [^pse-press-psei-6-5k-2024] [^pse-press-1h22-ipos] [^pse-press-last-trading-day-2025]. 2020 year-end: PSEi 7,139.71; ADV PHP7.35bn; net foreign selling PHP128.65bn [^pse-press-psei-ends-2020].
- **Delistings 2020–Oct 2026 (PSE delisted-company list; issuers, excluding preferred/warrant retirements)** [P] [^pse-delisted-companies-web]: 2020: 1 (Pepsi-Cola Products Philippines, voluntary); 2021: 3 (Primetown, Export & Industry Bank A/B — involuntary; Cebu Property Ventures A/B — merger); 2022: 0; 2023: 6 (Eagle Cement, 2GO, MPIC, Holcim Philippines — voluntary; Unioil, PICOP — involuntary); 2024: 3 (Cebu Holdings merger; Premium Leisure, SFA Semicon voluntary); 2025: 3 (Keppel Philippines A/B, 8990 Holdings voluntary; Philab involuntary); 2026 YTD: 3 (Asian Terminals voluntary 3 Apr [CN-2026-0013 of 25 Mar 2026: petition approved, delisting effective 3 Apr] [^pse-cn-2026-0013-ati-voluntary-delisting:1]; City & Land Developers merger 6 Jul; Robinsons Retail voluntary 31 Aug [^pse-cn-2026-0038-rrhi-voluntary-delisting:1]). Preferred/warrant retirements: SMC2A–2D (redemption 1 Oct 2025), CPGP (11 Jun 2025), ALCPB/ALCPC (11 Nov 2024), Cirtek TECHW warrants (expired 19 Aug 2024). So 2020–Oct 2026: 31 new issuer listings (28 IPOs + 3 listings by way of introduction: APVI 2020, LPC 2022, LTL 2026; counted from PSE's new-listings page plus Maynilad and LTL) vs 19 issuers delisted [I from P] [^pse-new-listings-ipo-web]. Voluntary delistings dominate (11 of 19), and most were controlling-holder take-privates.
- **Capital raised (PHP bn)** [P] [^pse-asm-2026-president-report:8]: 2024 = 82.37 (IPO 11.91, FOO 47.08, private placement 12.38, SRO 11.00); 2025 = 144.13 (IPO 35.07, FOO 67.29, PP 40.67, ~1.1 other = AGI warrants); 6M2026 = 39.43 (FOO 26.50, PP 12.93, **no IPO**). PSE also reports 2025: 2 IPOs, 8 follow-ons, 14 private placements; +75.0% y/y [P] [^pse-press-last-trading-day-2025]. Earlier years are in the two bullets above (total capital raised PHP103.76bn in 2020 through PHP140.95bn in 2023); Monde Nissin (June 2021) remains the largest IPO to date and PSE ranks Maynilad second [P] [^pse-press-maynilad-ipo].
- **Notable large listings**: Maynilad — 7 Nov 2025, PHP34.34bn, primary shares, ADB/IFC US$245m cornerstone, SEC's first "Philippine Green Equity" label, President Marcos rang the bell; offer 23–29 Oct 2025, up to 1.66bn primary shares + 24.9m preferential to First Pacific + 249.05m OA + 354.70m upsize secondary [P] [^pse-press-maynilad-ipo] [^pse-press-maynilad-greenlight]; entered PSEi 3 Aug 2026 [P] [^pse-press-mynld-psei]. MYNLD last PHP16.16 (52-wk 14.02–24.45) [P] [^pse-sec-frames-snapshot]. Top Line (TOP): IPO 8 Apr 2025, later FOO listing; TOP last PHP1.64 [P] [^pse-sec-frames-snapshot].
- **Pipeline (as of 4 Jul 2026 ASM report; ~PHP164.2bn forthcoming)**: IPO Vitro REIT ~PHP24.19bn (12 Oct 2026); IPO Globe Fintech Innovations ("Mynt") ~PHP92.31bn (19 Oct 2026); FOO SMC ~PHP30bn (31 Jul — listed 3 Aug), Arthaland ~PHP3bn (listed 2 Oct: PHP2.15bn raised); SRO LFM Properties ~PHP1.7bn (10 Aug 2026); private placements SteelAsia ~PHP9bn and EEI ~PHP4bn (TBD); LBWI PNB Holdings (~PHP56bn market cap) [P] [^pse-asm-2026-president-report:8]. PSE's 17 Aug 2026 briefing (data as of 13 Aug) updates the list to ~PHP133.70bn forthcoming: SRO LFM Properties ~PHP1.2bn (21 Sep), LBWI PNB Holdings (25 Sep), IPOs Vitro REIT ~PHP24.19bn (12 Oct) and Mynt ~PHP92.31bn (19 Oct), FOO Arthaland ~PHP3bn (25 Sep), private placements SteelAsia ~PHP9bn and EEI ~PHP4bn (dates TBD); completed in 2026: FOOs Globe Telecom PHP25bn (2 Mar), Top Line PHP1.5bn (26 Jun) and SMC PHP30bn (3 Aug), and private placements Italpinas PHP187.93m (6 Jan), Citicore Renewable PHP6.70bn (13 Jan), EEI PHP6bn (24 Feb) and Prime Media PHP44.25m (11 Mar) — the 6M26 totals of FOO 26.50 and private placement 12.93 (PHP bn) are exactly these items [P/I] [^pse-analyst-briefing-1h-2026:13]. Mynt detail (PSE approval 18 Sep 2026): 8.03bn shares = 1.61bn primary + 6.42bn secondary + OA up to 1.20bn secondary; price up to PHP10.00; book-building price set 1 Oct; offer 6–12 Oct; tentative listing 20 Oct 2026; symbol GCASH; LSIs via PSE EASy and GStocks [P] [^pse-press-mynt-ipo-approval]. LEAP programme (launched 2020): 24 companies on the roster in the July ASM report and 25 in the 17 Aug 2026 briefing, four of them "ready and preparing for their IPO next year" (the same wording appears in both; read against the August 2026 date it most plausibly means 2027 [I]), and four LEAP participants have already listed [P] [^pse-asm-2026-president-report:20] [^pse-analyst-briefing-1h-2026:15].
- Policy drivers: MPO tiers (Aug 2026), REIT framework (Jan 2026), preferred-listing relaxations (in force 12 Aug 2026), ETF reforms (pending) — see Q4/Q6. Pandemic relief for 2021–22 IPO applicants (PSE may, case by case, judge profitability on the two fiscal years before the COVID-affected year, e.g. 2018–19 for a 2021 filing, with added pandemic disclosure) took effect with the 24 Mar 2021 rule re-cut [P] [^pse-cn-2021-0021-amended-listing-rules:1] [^pse-cn-2021-0021-amended-listing-rules:2].

### Inferences
- The IPO market is now bimodal: a few very large, cornerstone/institution-driven deals (Maynilad, Mynt) vs. near-zero mid-cap flow; retail participation (LSI tranche via PSE EASy/GStocks) is a design feature of big deals.
- The Mynt deal alone (PHP92bn) is ~64% of PHP144bn raised in all of 2025.

### Gaps
- SME-board IPO counts differ between PSE's statistics table and its new-listings page; the final pricing/allocation of Mynt (GCASH) and the Vitro REIT outcome are not yet known (offer period opened 6 Oct 2026); PSE's 'Capital Raised' tab did not render, so 2020–2023 totals come from press releases.

### Execution implications
- IPO weeks: LSI tranche, OA/stabilisation fund, 180/365-day lock-up expiry dates are predictable supply events (from listing date + 180 days). Add them to the event calendar: MYNLD (7 Nov 2025) 180-day window ended ~6 May 2026; TOP, OGP etc. likewise.
- Expect index-inclusion pressure: "early inclusion" rule (MYNLD qualified; "only the third since 2021") — a post-IPO index-demand event.

---

## 6. Planned/new products as of Oct 2026

### Takeaway
Since January 2026 the *in-force* changes are rule-level only: the SEC REIT framework (MC 1-2026, 25 Jan), the tiered MPO rule (11 Aug), the preferred-share IPO/direct-listing rule (12 Aug) and the Class A/B declassification (SEC deadline 9 Aug 2026; PSE price/suspension mechanics 10 Sep). No new tradable product type has launched in 2026. Pipeline (PSE's own status, 4 Jul and 17 Aug 2026): **index futures on the PSEi** (early exposure draft, vendor RFI, consultants — no launch date), **structured warrants** (SEC rules in consultation), **GPDRs** (rules awaiting SEC), **ETF reform**, **negotiated trades**, **One Lot One Share + new Nasdaq Eqlipse engine ("by November" 2026)**. No fractional-share plan found.

### Cited findings
- **Status board in PSE's 17 Aug 2026 analyst briefing (the latest dated PSE status found)** [P] [^pse-analyst-briefing-1h-2026:9] [^pse-analyst-briefing-1h-2026:10] [^pse-analyst-briefing-1h-2026:16]: One Share One Lot — "For SEC Approval", targeted for Q4 2026 with the new engine; Market Making (GPDR framework) and Negotiated Trades — "Revising per Public Comments"; ETF rule amendments — "Revising per Public Comments"; revised SBL rules — awaiting SEC approval (SEC has already approved the updated MSLA-clearance guidelines); GPDR rules — revised draft submitted 24 Jun, approval and publication "targeted within the quarter"; derivatives — early exposure draft and vendor RFI out, PSE "in discussions with multilaterals for possible funding"; structured warrants — PSE aligning its draft with the SEC's and sounding out potential issuers; MPO and preferred-share rules — "SEC Approved"; sponsor model — "Ongoing Review".
- **Derivatives**: "PSE is developing the Philippine Derivatives market, starting with Index Futures based on the PSEi"; early exposure draft sent to selected institutions; RFI to technology vendors targeted July 2026 (PSE's 17 Aug briefing says it was released in July); third-party consultancy under consideration [P] [^pse-asm-2026-president-report:24] [^pse-analyst-briefing-1h-2026:10]. The new engine "facilitate[s] the introduction of new financial instruments, such as derivatives" [P] [^pse-nte-page-web]. Earlier public targets: derivatives (PSEi index futures first) by **Q1 2026**, conditional on SEC and BIR frameworks, with PSE preparing via exchange visits (HK, Taiwan) and bank sessions [S] [^bworld-pse-gpdr-derivatives-2024]; FOW (29 Aug 2024) headline "plans first derivatives in 2026" after an MOU with a Taiwan exchange group [S, paywalled] [^fow-pse-derivatives-2026]; PSE/SCCP/PDS/SEC delegates studied TAIFEX derivatives lifecycle/clearing and TWSE structured warrants, SBL and market making on 15–18 Dec 2025 [P] [^pse-annual-report-2025:29]. The Q1 2026 target was **missed** (ASM report of 4 Jul 2026 and the 17 Aug 2026 briefing are still at 'early exposure draft' plus vendor RFI, with funding talks under way). **No launch date, no SEC rule, no clearing house designated in sources found** [gap].
- **Structured warrants**: SEC proposed rules on registration/trading (PSE circular 30 Apr 2026; comments to SEC by 13 May 2026); PSE aligning draft rules with SEC's [P] [^pse-cn-2026-0018:1] [^pse-asm-2026-president-report:24]. Existing CLDR "derivative covered/non-collateralized warrant" rules are older and unused (Q2).
- **GPDRs** (see Q2): peso-denominated receipts on foreign-listed securities, listed on a **GPDR Board**, trading hours adjustable to the overseas session, suspension when the underlying is suspended or has a price/number-affecting corporate action, mirror disclosure of the underlying's material information; issuers = TPs, BSP-authorised banks/NBFIs, investment companies (min paid-up capital and equity PHP100m); underlying must be listed on a WFE-member exchange; ratio 1:1 or as specified [P, **draft** of 26 Sep 2024] [^pse-cn-2024-0047:6] [^pse-cn-2024-0047:7] [^pse-cn-2024-0047:10] [^pse-cn-2024-0047:12] [^pse-cn-2024-0047:19] [^pse-cn-2024-0047:23]. Revised rules were submitted to SEC on 24 Jun 2026, with approval/publication "targeted within the quarter" (Q3 2026) [P] [^pse-asm-2026-president-report:24]; a market-making framework covering GPDRs was released 4 Jun 2026 [P] [^pse-press-market-making]. **No evidence of SEC approval or any GPDR listing as of 6 Oct 2026** [I].
- **ETF/market-making reforms** (June 2026 consultations): see Q2 [P].
- **Negotiated Trade Reporting Facility / Negotiated Trades** (consultation to 7 Jul 2026): variant of Block Sale for smaller pre-arranged trades [P] [^pse-asm-2026-president-report:23] [^pse-nte-faq-2026-08:1].
- **One Lot One Share** (CN-2025-0046, 15 Dec 2025): lot = 1 share for all prices, tick table streamlined, trading-at-last (run-off) rule changed so that orders at the closing price are accepted even when better-priced orders rest; awaiting SEC approval as of 4 Jul 2026 and still "For SEC Approval" on 17 Aug 2026, targeted Q4 2026 with the new engine (planned go-live **Mon 23 Nov 2026**; "goes live by November" per press; cost PHP241.03m engine + PHP45.83m back office) [P/S] [^pse-nte-broker-forum-2026-07-09:9] [^pse-asm-2026-president-report:22] [^pse-nte-page-web] [^philstar-nte-november]. NTE FAQ (Aug 2026): odd-lot market ends [P] [^pse-nte-faq-2026-08:1].
- **SBL**: PSE/PDTC lending agency live (22 Apr/18 May 2026); amended SBL rules with directed pooled lending submitted to SEC 16 Apr 2026 [P] [^pse-press-additional-reforms] [^pse-asm-2026-president-report:22].
- **Fractional shares**: no PSE or SEC initiative found; "One Lot One Share" (min 1 share) is the closest and removes the odd-lot concept [I; absence].

### Gaps
- Dates for derivatives; SEC approvals after PSE's 17 Aug 2026 status board for board lot, ETF, GPDR, market-making and SBL rules (the preferred-listing and MPO rules *were* approved: 12 Aug and 11 Aug 2026); NTE exact cut-over date and parallel-run calendar (see trading chapter).

### Execution implications
- Plan for a **regime change on 23 Nov 2026 (planned)**: lot=1, new tick table, no odd-lot book, revised trading-at-last, new FIX/ITCH endpoints (leased-line UAT from May 2026) — freeze strategy parameter changes around cut-over.
- Derivatives/structured warrants are not tradable in 2026 for planning purposes; hedging must use SBL/short-sale and the ETF only.
- Per PSE's NTE FAQ, only limit orders will be supported on day 1 of the new engine and there is no parallel run (big-bang cut-over) — algos that depend on market, market-on-open/close or other order types need a day-1 fallback [P] [^pse-nte-faq-2026-08:1].

---

## Source catalog

```yaml
# Entries are limited to sources cited in the body above. PDF entries are archived under kb/pdfs/<slug>.pdf (citations use physical 1-based page numbers);
# web/dataset entries have local_path null. edition: in-force = current operative or live text; superseded = replaced by a later edition;
# historical = consultation or event record never or no longer operative; n/a = not a rule edition (press, news, data).
# amended_through for live pages is the content date where the page shows one, otherwise undated (the retrieval date is then in the note).
- slug: bir-rr-3-2020-reit
  title: "BIR Revenue Regulations No. 3-2020 (REIT taxation)"
  publisher: "Bureau of Internal Revenue"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2021/03/RR_No._3_2020.pdf"
  local_path: pdfs/bir-rr-3-2020-reit.pdf
  edition: in-force
  amended_through: undated
  note: "Dividend-deduction conditions tied to public-company status and sworn MPO statement (p.5); issuing date not captured."
- slug: pse-amended-mpo-rule-2026-08
  title: "Effectivity of the PSE Amended Rule on Minimum Public Ownership and Revised Guidelines in Determining the Public Ownership of Listed Companies"
  publisher: "The Philippine Stock Exchange, Inc. (SEC-approved)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2026/08/Memo-to-Public_Effectivity-of-the-Amended-MPO-Rule-Rvsd-PO-Guidelines-v2.pdf"
  local_path: pdfs/pse-amended-mpo-rule-2026-08.pdf
  edition: in-force
  amended_through: 2026-08-11
  note: "Memo dated 11 Aug 2026, rule effective immediately. Implements SEC MC 11 s.2026."
- slug: pse-analyst-briefing-1h-2026
  title: "Philippine Stock Exchange: 1H 2026 Updates (PSE STAR Briefing)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/4/2026/08/2026.08.17-PSE-STAR-1H-2026.pdf"
  local_path: pdfs/pse-analyst-briefing-1h-2026.pdf
  edition: in-force
  amended_through: 2026-08-17
  note: "PSE STAR analysts' briefing of 17 Aug 2026 (market data as of 14 Aug 2026; capital-raising list as of 13 Aug). Cited for: 280 listed companies and headline market figures (p.3); rule-amendment status boards (pp.9-10 trading and products, p.16 listing: MPO and preferred rules SEC Approved, ETF rules Revising per Public Comments, sponsor model Ongoing Review); upper ALMF limit raised from PHP2m to PHP3.5m (p.12); 2026 capital-raising pipeline and completed deals (p.13); LEAP (p.15)."
- slug: pse-annual-report-2013
  title: "PSE Annual Report 2013 (CMIC section with surveillance case counts)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://ir.pse.com.ph/wp-content/uploads/sites/4/2020/04/2013-PSE-Annual-Report.pdf"
  local_path: pdfs/pse-annual-report-2013.pdf
  edition: n/a
  amended_through: 2013-12-31
  note: "Cited for the FMETF listing history (p.22). URL verified byte-identical to the archived file on 6 Oct 2026; fiscal-year-end date used because the report states no publication date."
- slug: pse-annual-report-2025
  title: "SEC Form 17-A / Annual Report FY2025 (The Philippine Stock Exchange, Inc.)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/4/2026/04/2025-Annual-Report.pdf"
  local_path: pdfs/pse-annual-report-2025.pdf
  edition: in-force
  amended_through: 2026-03-31
  note: "FY ended 2025-12-31; shareholder data as of 2026-03-31; PDS stake as of 2026-02-04."
- slug: pse-asm-2026-president-report
  title: "President's Report, Annual Stockholders' Meeting"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/4/2026/07/PSE-ASM-2026-PRESIDENT_S-REPORT.pdf"
  local_path: pdfs/pse-asm-2026-president-report.pdf
  edition: in-force
  amended_through: 2026-07-04
  note: "Cover date 4 Jul 2026; accounts, value shares, rule-amendment status, PDS integration roadmap."
- slug: pse-cn-2019-0037-foreign-investment-etf
  title: "PSE Circular - Foreign investment into Philippine ETFs (BSP Circular 1030)"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2019-0037.pdf"
  local_path: pdfs/pse-cn-2019-0037-foreign-investment-etf.pdf
  edition: in-force
  amended_through: 2019-07-08
  note: "Relays BSP Circular 1030 (5 Feb 2019) FX Manual amendments: ETFs and onshore-listed PDRs are eligible inward foreign investments (FX Manual Sec. 33.3.c and 33.3.e); cited here for PDR eligibility (pp.1-2). URL verified byte-identical to the archived file on 6 Oct 2026."
- slug: pse-cn-2020-0028
  title: "Amendment of Rule on Static Threshold (CN-2020-0028, 21 Mar 2020)"
  publisher: "The Philippine Stock Exchange, Inc. (SEC-approved)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2020-0028.pdf"
  local_path: pdfs/pse-cn-2020-0028.pdf
  edition: in-force
  amended_through: 2020-03-21
  note: "Lower static threshold 30%, effective 24 Mar 2020."
- slug: pse-cn-2020-0066-reit-broker-eligibility
  title: "PSE Memorandum CN-No. 2020-0066: Broker eligibility guidelines to trade REIT securities"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2020-0066.pdf"
  local_path: pdfs/pse-cn-2020-0066-reit-broker-eligibility.pdf
  edition: in-force
  amended_through: 2020-07-15
  note: "Dated 15 Jul 2020. Broker-eligibility guidelines for trading REIT securities (training attendance and sworn operational-readiness certification); p.2 covers eligible-broker participation in REIT IPO allocations."
- slug: pse-cn-2021-0021-amended-listing-rules
  title: "PSE CN-2021-0021 - Amended Listing Rules (Main/SME Board criteria, Part E-1 sponsor model; COVID IPO relief)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2021/05/CN_2021-0021.pdf"
  local_path: pdfs/pse-cn-2021-0021-amended-listing-rules.pdf
  edition: in-force
  amended_through: 2021-03-24
  note: "SEC approval 4 Feb 2021; effective immediately; temporary COVID relief for IPO applications filed in 2021-2022 (now lapsed)."
- slug: pse-cn-2022-0010-edge-cutoff-330pm
  title: "CN-2022-0010 - Cut-off for posting disclosures on PSE EDGE (3:30 pm)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2022-0010.pdf"
  local_path: pdfs/pse-cn-2022-0010-edge-cutoff-330pm.pdf
  edition: superseded
  amended_through: 2022-02-24
  note: "Superseded by CN-2026-0024 (4:00 pm)."
- slug: pse-cn-2023-0022-stabilization-fund
  title: "PSE CN-2023-0022 - Amendments to Article III Part A (new Sec. 13 Stabilization Fund)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2023-0022.pdf"
  local_path: pdfs/pse-cn-2023-0022-stabilization-fund.pdf
  edition: in-force
  amended_through: 2023-05-12
  note: "Scanned; OCR used. Effective immediately."
- slug: pse-cn-2023-0031-t2-settlement
  title: "CN-2023-0031 Migration to the T+2 settlement cycle (with SCCP Memo 01-0623)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2023-0031.pdf"
  local_path: pdfs/pse-cn-2023-0031-t2-settlement.pdf
  edition: historical
  amended_through: 2023-06-23
  note: "CN-2023-0031 of 23 Jun 2023 with SCCP Memo 01-0623: T+2 migration targeted for trade date 24 Aug 2023; for corporate actions from that date the ex-rights date is one trading day before the disclosed record date (p.1)."
- slug: pse-cn-2023-0040-t2-go-live
  title: "PSE Memorandum CN-No. 2023-0040: Go-live of the migration to T+2 on 24 Aug 2023 (with SCCP Memo 04-0823)"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2023/08/CN_2023-0040-1.pdf"
  local_path: pdfs/pse-cn-2023-0040-t2-go-live.pdf
  edition: historical
  amended_through: 2023-08-15
  note: "SEC en banc approved the T+2 go-live on 10 Aug 2023; first T+2 trade date 24 Aug 2023 (settles 29 Aug 2023, 28 Aug being a holiday); attaches SCCP Memo 04-0823."
- slug: pse-cn-2023-0041-mpo-delisting-consult
  title: "PSE CN-2023-0041 - Proposed amendments to the Public Ownership Guidelines, Amended MPO Rule and Amended Voluntary Delisting Rules (consultation)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2023-0041.pdf"
  local_path: pdfs/pse-cn-2023-0041-mpo-delisting-consult.pdf
  edition: historical
  amended_through: 2023-08-25
  note: "Consultation only (comments to 8 Sep 2023); shows pre-2026 MPO rule text (paras (a)-(m)) and the voluntary-delisting changes proposed; adoption of the voluntary-delisting changes unconfirmed."
- slug: pse-cn-2023-0058-steniel-mpo-non-compliance
  title: "CN-2023-0058 - Steniel Manufacturing: non-compliance with Amended MPO Rule"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2023/10/CN_2023-0058.pdf"
  local_path: pdfs/pse-cn-2023-0058-steniel-mpo-non-compliance.pdf
  edition: n/a
  amended_through: 2023-10-23
  note: "Quotes the pre-2026 'Amended MPO Rule' suspension wording."
- slug: pse-cn-2024-0037a-metro-global-mpo-non-compliance
  title: "CN-2024-0037A - Metro Global Holdings: non-compliance with Amended MPO Rule"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2024/09/CN-2024-0037A.pdf"
  local_path: pdfs/pse-cn-2024-0037a-metro-global-mpo-non-compliance.pdf
  edition: n/a
  amended_through: 2024-07-16
  note: "Quotes the pre-2026 MPO suspension wording."
- slug: pse-cn-2024-0047
  title: "Proposed Rules for Global Philippine Depositary Receipts (CN-2024-0047, 26 Sep 2024)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2024-0047.pdf"
  local_path: pdfs/pse-cn-2024-0047.pdf
  edition: superseded
  amended_through: 2024-09-26
  note: "Archived by another researcher; draft; revised version awaiting SEC approval per 2026 PSE reports."
- slug: pse-cn-2024-0068-almf-effectivity
  title: "PSE CN-2024-0068 - Effectivity of ALMF (upper limit raised to PHP3.5m)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2024-0068.pdf"
  local_path: pdfs/pse-cn-2024-0068-almf-effectivity.pdf
  edition: in-force
  amended_through: 2024-12-19
  note: "SEC-approved; effective 2 Jan 2025."
- slug: pse-cn-2025-0035-sec-declassification-mandate
  title: "PSE Circular CN-2025-0035 - SEC MC 10 s.2025 mandating declassification of Class A/B shares"
  publisher: "Philippine Stock Exchange / SEC"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2025-0035.pdf"
  local_path: pdfs/pse-cn-2025-0035-sec-declassification-mandate.pdf
  edition: in-force
  amended_through: 2025-08-11
  note: "Archived by another researcher; SEC text at pp. 2-3."
- slug: pse-cn-2025-0036-declassification-effectivity
  title: "PSE Circular CN-2025-0036 - Effectivity of SEC MC 10 s.2025"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2025-0036.pdf"
  local_path: pdfs/pse-cn-2025-0036-declassification-effectivity.pdf
  edition: in-force
  amended_through: 2025-08-15
  note: "Effective 9 Aug 2025; articles to be amended by 9 Aug 2026."
- slug: pse-cn-2025-0047-sector-reclassification
  title: "PSE CN-2025-0047 - Sector reclassification of 13 companies (effective 5 Jan 2026)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2025-0047.pdf"
  local_path: pdfs/pse-cn-2025-0047-sector-reclassification.pdf
  edition: in-force
  amended_through: 2025-12-26
  note: "States the PSE Sector Classification Guide rule (>= 60% of revenue)."
- slug: pse-cn-2026-0004-2-emergency-disclosures-trading-halt
  title: "Emergency Disclosures and Trading Halt: MRC Allied (CN-2026-0004-2, 19 Jan 2026)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2026/01/CN-2026-0004-2.pdf"
  local_path: pdfs/pse-cn-2026-0004-2-emergency-disclosures-trading-halt.pdf
  edition: historical
  amended_through: 2026-01-19
  note: "Notice of 19 Jan 2026: one-hour halt (9:30-10:30 a.m.) on MRC Allied after disclosure of a 315,000,000-share issuance at PHP1.00 treated as covered by the Additional Listing Rule (notice on p.2)."
- slug: pse-cn-2026-0013-ati-voluntary-delisting
  title: "PSE Memorandum CN-No. 2026-0013: Asian Terminals, Inc.: approval of petition for voluntary delisting (effective 3 Apr 2026)"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2026-0013.pdf"
  local_path: pdfs/pse-cn-2026-0013-ati-voluntary-delisting.pdf
  edition: historical
  amended_through: 2026-03-25
  note: "CN-2026-0013 of 25 Mar 2026: PSE approved Asian Terminals' voluntary-delisting petition; removal from the official registry effective 3 Apr 2026."
- slug: pse-cn-2026-0018
  title: "PSE CN-2026-0018 - Request for comments on SEC's proposed regulations for structured warrants"
  publisher: "The Philippine Stock Exchange, Inc. / SEC"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2026-0018.pdf"
  local_path: pdfs/pse-cn-2026-0018.pdf
  edition: n/a
  amended_through: 2026-04-30
  note: "Scanned; OCR-read. SEC draft (En Banc 28 Apr 2026)."
- slug: pse-cn-2026-0020-mpo-consult
  title: "PSE CN-2026-0020 - 2026 Proposed Revisions to the Amended Rule on Minimum Public Ownership (consultation paper; Annex A = SEC MC 11-2026 draft text; Annex B = draft PSE rule)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2026-0020.pdf"
  local_path: pdfs/pse-cn-2026-0020-mpo-consult.pdf
  edition: historical
  amended_through: 2026-05-13
  note: "Consultation draft, superseded by the 11 Aug 2026 rule. Annex A reproduces the SEC circular in draft ('Done this __ February 2026'); the final SEC MC 11 s.2026 PDF could not be retrieved (sec.gov.ph 403)."
- slug: pse-cn-2026-0024-edge-cutoff-4pm
  title: "CN-2026-0024 - Cut-off for posting disclosures on EDGE portal (4:00 pm)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2026/05/CN-No.-2026-0024.pdf"
  local_path: pdfs/pse-cn-2026-0024-edge-cutoff-4pm.pdf
  edition: in-force
  amended_through: 2026-05-22
  note: "Effective 25 May 2026."
- slug: pse-cn-2026-0029-etf-amend-consult
  title: "PSE CN-2026-0029 - Proposed Amendments to PSE Rules on Exchange Traded Funds (consultation paper and draft rules)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2026-0029.pdf"
  local_path: pdfs/pse-cn-2026-0029-etf-amend-consult.pdf
  edition: historical
  amended_through: 2026-06-16
  note: "Scanned; OCR used. Comments to 30 Jun 2026; draft only - approval status unknown. Also cited by other chapters under this slug."
- slug: pse-cn-2026-0031-negotiated-trades
  title: "Invitation to Submit Comments on Proposed Rules on Negotiated Trades (CN-2026-0031, 1 Jul 2026)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2026-0031.pdf"
  local_path: pdfs/pse-cn-2026-0031-negotiated-trades.pdf
  edition: historical
  amended_through: 2026-07-01
  note: "CN-2026-0031 of 1 Jul 2026: consultation on Negotiated Trades as a variant of the block-sale framework (comments to 7 Jul 2026; PSE status 'Revising per Public Comments' as of 17 Aug 2026). Not in force; cited here only for PSE's own restatement of the existing block-sale thresholds (p.3)."
- slug: pse-cn-2026-0032-rrhi-index-removal
  title: "PSE CN-2026-0032 - Removal of Robinsons Retail Holdings from PSE DivY, MidCap and Services indices (trading suspension effective 13 Jul 2026)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2026-0032.pdf"
  local_path: pdfs/pse-cn-2026-0032-rrhi-index-removal.pdf
  edition: historical
  amended_through: 2026-07-14
  note: "Primary source for the RRHI suspension date."
- slug: pse-cn-2026-0035
  title: "CN-2026-0035: Results of the Review of PSE Indices (Jul 2025-Jun 2026)"
  publisher: "The Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2026-0035.pdf"
  local_path: pdfs/pse-cn-2026-0035.pdf
  edition: in-force
  amended_through: 2026-07-27
  note: "Effective 3 Aug 2026; lists the 30 PSEi members now in force."
- slug: pse-cn-2026-0037-preferred-shares-rule-effectivity
  title: "PSE Memorandum CN-No. 2026-0037: Effectivity of the PSE rule on listing through IPO or direct listing of preferred shares"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2026/08/CN-No.-2026-0037.pdf"
  local_path: pdfs/pse-cn-2026-0037-preferred-shares-rule-effectivity.pdf
  edition: in-force
  amended_through: 2026-08-12
  note: "CN-2026-0037 of 12 Aug 2026: SEC-approved rule on listing of preferred shares by IPO or direct listing, effective immediately; replaces CLDR Art. III Part H (SR 19, 24 May 2022). Cited pages: 1, 3-6, 9."
- slug: pse-cn-2026-0038-rrhi-voluntary-delisting
  title: "PSE Memorandum CN-No. 2026-0038: Approval of the voluntary delisting of Robinsons Retail Holdings, Inc. (effective 31 Aug 2026)"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2026/08/CN-No.-2026-0038.pdf"
  local_path: pdfs/pse-cn-2026-0038-rrhi-voluntary-delisting.pdf
  edition: historical
  amended_through: 2026-08-20
  note: "CN-2026-0038 of 20 Aug 2026: PSE approved Robinsons Retail Holdings' voluntary-delisting petition; removal from the official registry effective 31 Aug 2026."
- slug: pse-cn-2026-0041-declassification-price-suspension
  title: "Declassification of shares - price adjustment and trading suspension mechanics (circular of 10 Sep 2026)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2026/09/2026-0041-Declassification-Price-Adjustment-and-Trading-Suspension-Mechanics.pdf"
  local_path: pdfs/pse-cn-2026-0041-declassification-price-suspension.pdf
  edition: in-force
  amended_through: 2026-09-10
  note: "Follows SEC mandate on Class A/B declassification (CN-2025-0035/0036)."
- slug: pse-cn-2026-0046-edge-outage-access-to-disclosures
  title: "PSE EDGE announcement CN-No. 2026-0046: Access to disclosures via PSE website (EDGE portal unavailable, 6 Oct 2026)"
  publisher: "The Philippine Stock Exchange, Inc. (PSE)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2026/10/Access-to-Disclosures-via-PSE-Website.pdf"
  local_path: pdfs/pse-cn-2026-0046-edge-outage-access-to-disclosures.pdf
  edition: historical
  amended_through: 2026-10-06
  note: "CN number taken from the follow-up batches that cite it; the memo itself shows no number."
- slug: pse-dds-rules
  title: "PSE Rules on Dollar Denominated Securities (DDS)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2021/01/Approved_DDS_Rules.pdf"
  local_path: pdfs/pse-dds-rules.pdf
  edition: in-force
  amended_through: 2016-12-02
  note: "Supplemental Rule 13 (CN-2016-0078); the date comes from PSE's regulation-page label for SR 13, the PDF itself is undated. Part C Sec. 1: USD board-lot/tick table, eligible brokers, block-sale thresholds; Part D: USD settlement."
- slug: pse-gn19-sec-mc-2-2009-rights-dividends
  title: "Guidance Note 19 - PSE Memo 2009-0272 re SEC MC No. 2 s.2009 (record date of cash dividends)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2022/08/Guidance-Note-19-SEC-Memo-Circular-No.-2-2009.pdf"
  local_path: pdfs/pse-gn19-sec-mc-2-2009-rights-dividends.pdf
  edition: in-force
  amended_through: 2009-05-13
  note: "Record date 10-30 days after declaration (default 15 days)."
- slug: pse-implementing-guidelines-trading-rules
  title: "Implementing Guidelines of the Revised Trading Rules (memo 2010-0340, 22 Jul 2010)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2021/04/Implementing-Guidelines-of-the-Revised-Trading-Rules.pdf"
  local_path: pdfs/pse-implementing-guidelines-trading-rules.pdf
  edition: superseded
  amended_through: 2010-07-22
  note: "Original text effective with NTS launch 2010-07-26; later amended (2011, 2025 Part XXI). Saved by another researcher."
- slug: pse-listing-disclosure-rules
  title: "Consolidated Listing and Disclosure Rules (published as of January 2025)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2025/01/Consolidated-Listing-and-Disclosure-Rules-Updated-011025.pdf"
  local_path: pdfs/pse-listing-disclosure-rules.pdf
  edition: in-force
  amended_through: 2025-01-10
  note: "Cover: 'Published as of January 2025'; PSE's regulation page labels the file 'Updated 01/10/25' and the latest dated item in its own index is CN 2025-0002 of 8 Jan 2025 (SR 1.4) with SR 24 (CN 2024-0068, ALMF). Superseded or modified since by separate memoranda not consolidated in this file: ALMF cap (CN-2024-0068, 2 Jan 2025, already in SR 24), EDGE cut-off 4:00 pm (CN-2026-0024, 25 May 2026), preferred-share listing rule (CN-2026-0037, 12 Aug 2026), MPO rule (11 Aug 2026), A/B declassification (SEC MC 10 s.2025). Page n of Article VII = physical n+137; Article VIII page n = physical n+158 (per another researcher)."
- slug: pse-monthly-report-2025-12
  title: "PSE Monthly Report December 2025 (preview)"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2026/02/12-2025_PSE-Monthly-Report_Preview.pdf"
  local_path: pdfs/pse-monthly-report-2025-12.pdf
  edition: historical
  amended_through: 2026-02-04
  note: "2025 summary; 243 trading days; foreign ratio 46.3%."
- slug: pse-monthly-report-2026-08
  title: "PSE Monthly Report, August 2026 (preview)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2026/09/08-2026_PSE-Monthly-Report_Preview.pdf"
  local_path: pdfs/pse-monthly-report-2026-08.pdf
  edition: in-force
  amended_through: 2026-08-31
  note: "Preview; posted 2026-09-30."
- slug: pse-mpo-second-exposure-2026-07
  title: "Second Exposure Draft of 2026 Proposed Revisions to the Amended Rule on MPO (PSE memo of 16 Jul 2026)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2026/07/Invitation-to-Comment-Second-Exposure-Draft-of-Proposed-Revisions-to-the-Amended-MPO-Rule.pdf"
  local_path: pdfs/pse-mpo-second-exposure-2026-07.pdf
  edition: historical
  amended_through: 2026-07-16
  note: "Timeline source: PSE submission to SEC 25 May 2026; SEC letter of 14 Jul 2026 approving with revisions; comments to 21 Jul 2026."
- slug: pse-nte-broker-forum-2026-07-09
  title: "New Trading Engine, PSETradeX, PSE Back-office Updates - Broker Forum (9 Jul 2026)"
  publisher: "The Philippine Stock Exchange, Inc. (Market Operations Division)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2026/07/PSE-New-Trading-Engine-TradeX-Back-office_Broker-Forum_07092026-1.pdf"
  local_path: pdfs/pse-nte-broker-forum-2026-07-09.pdf
  edition: in-force
  amended_through: 2026-07-09
  note: "Project schedule, readiness counts, negotiated-trade features, PSETradeX charges."
- slug: pse-nte-faq-2026-08
  title: "Frequently Asked Questions - New Trading Engine / PSE Back-Office / PSETradeX / Market Data"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2026/08/Frequent-Asked-Questions.pdf"
  local_path: pdfs/pse-nte-faq-2026-08.pdf
  edition: in-force
  amended_through: undated
  note: "Published Aug 2026 per upload path; refers to data from 3 Aug 2026 and to specs released 23 Jul 2026."
- slug: pse-nte-user-group-2026-01-15
  title: "New Trading Engine, PSETradeX, PSE Back-office Updates - Broker Forum (15 Jan 2026)"
  publisher: "The Philippine Stock Exchange, Inc. (Market Operations Division)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2026/06/NTE-User-Group.pdf"
  local_path: pdfs/pse-nte-user-group-2026-01-15.pdf
  edition: in-force
  amended_through: 2026-01-15
  note: "Date from the PSE page listing (deck itself undated); lot/tick tables are proposals."
- slug: pse-revised-trading-rules
  title: "Revised Trading Rules (2010; scanned)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2021/04/Revised-Trading-Rules.pdf"
  local_path: pdfs/pse-revised-trading-rules.pdf
  edition: superseded
  amended_through: undated
  note: "Image-only PDF (memo 2010-0275); Art. VIII s.2 halt trigger amended 20 Aug 2025. Saved by another researcher; pages cited from my OCR."
- slug: pse-sr11-etf-rules-2026
  title: "Supplemental Rule 11 - PSE Rules on Exchange Traded Funds (CN-2013-0010; 'UPDATED' posting of May 2026) with SEC ETF Rules (SEC MC 10 s.2012) appended"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2026/05/Supplemental-Rule-11-Memo-No.-2013-0010-1-UPDATED-1.pdf"
  local_path: pdfs/pse-sr11-etf-rules-2026.pdf
  edition: in-force
  amended_through: 2013-09-11
  note: "Cover text 'SEC Approved PSE ETF Rules, March 18, 2013'; latest dated amendment inside is Board Resolution 141 s.2013 (11 Sep 2013). By my text diff identical to the 2021 posting (pdfs/pse-etf-rules.pdf) apart from the appended SEC rules. Another researcher's catalog entry for this slug gives amended_through 2013-03-18 (SEC approval date); the later 11 Sep 2013 date is Board Resolution 141 s.2013 appearing inside the file."
- slug: pse-sr20-listing-issued-outstanding-shares-2023
  title: "Supplemental Rule 20 - PSE CN-2023-0012, Implementing Guidelines for the Listing of Issued and Outstanding Shares (with amended checklists for stock rights, ESOP/ESPP and stock dividend listings)"
  publisher: "The Philippine Stock Exchange, Inc. / SEC"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2023/03/Supplemental-Rule-20-Implementing-Guidelines-for-the-Listing-of-Issued-and-Outstanding-Shares.pdf"
  local_path: pdfs/pse-sr20-listing-issued-outstanding-shares-2023.pdf
  edition: in-force
  amended_through: 2023-03-21
  note: "SEC-approved; effective on posting to PSE's website. Guidelines on pp.2-4, checklists pp.5-16. Text hash-identical to documents.pse.com.ph/CircularOPSPDF/CN-2023-0012.pdf (checked 6 Oct 2026)."
- slug: pse-sr3-2-reit-listing-amend-2023
  title: "Supplemental Rule 3.2 - PSE Amended Listing Rules for REITs (2023 amendments; CN-2023-0010 of 9 Mar 2023)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2023/03/Supplemental-Rule-3.2-Amended-REIT-Listing-Rules-2023.pdf"
  local_path: pdfs/pse-sr3-2-reit-listing-amend-2023.pdf
  edition: in-force
  amended_through: 2023-03-09
  note: "Supersedes the 2020 amended REIT listing rules and the 13 Jun 2022 MEA-2022-0001 amendments (lock-up exemption, stockholders' equity)."
- slug: pse-sr6-2-mpo-initial-backdoor-2020
  title: "Supplemental Rule 6.2 - PSE CN-2020-0076, Guidelines on MPO Requirement for Initial and Backdoor Listings"
  publisher: "The Philippine Stock Exchange, Inc. / SEC"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2022/07/Supplemental-Rule-6.2-Guidelines-on-MPO-Requirements-for-Initial-and-Backdoor-Listings.pdf"
  local_path: pdfs/pse-sr6-2-mpo-initial-backdoor-2020.pdf
  edition: superseded
  amended_through: 2020-08-03
  note: "Scanned; OCR used. IPO tiers (PHP50m/100m/250m offer sizes) superseded by the Aug 2026 tiers."
- slug: pse-sr6-mpo-rule-2012
  title: "Supplemental Rule 6 - PSE CN-2012-0003, Amended Rule on Minimum Public Ownership (with SEC letters of 22 Dec 2011 and 2 Jan 2012)"
  publisher: "The Philippine Stock Exchange, Inc. / SEC"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2022/08/Supplemental-Rule-6-Amended-MPO-Rule.pdf"
  local_path: pdfs/pse-sr6-mpo-rule-2012.pdf
  edition: superseded
  amended_through: 2012-01-03
  note: "Scanned; OCR used for reading. Effective 1 Jan 2012; superseded by the 11 Aug 2026 rule (the suspend-up-to-6-months-then-automatic-delist ladder and 5-year relisting ban are carried forward)."
- slug: pse-sr7-backdoor-listing-2022
  title: "Supplemental Rule 7 - PSE CN-2022-0026, Revised Rules on Backdoor Listing"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2022/07/Supplemental-Rule-7-Revised-Rules-on-Backdoor-Listing.pdf"
  local_path: pdfs/pse-sr7-backdoor-listing-2022.pdf
  edition: in-force
  amended_through: 2022-06-22
  note: "Amends CN-2022-0024 of 26 May 2022; text read pp.1-4 only (change-of-control/business-change tests, suspension mechanics)."
- slug: pse-sr8-1-voluntary-delisting-2020
  title: "Supplemental Rule 8.1 - PSE CN-2020-0104, Amendments to the Voluntary Delisting Rules"
  publisher: "The Philippine Stock Exchange, Inc. / SEC"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2022/07/Supplemental-Rule-8.1-Amendments-to-the-Voluntary-Delisting-Rules.pdf"
  local_path: pdfs/pse-sr8-1-voluntary-delisting-2020.pdf
  edition: in-force
  amended_through: 2020-12-21
  note: "Scanned; OCR used. Latest voluntary-delisting text published on PSE's site (6 Oct 2026); 2023 proposals in CN-2023-0041 not confirmed adopted."
- slug: pse-sr8-delisting-rules
  title: "Supplemental Rule 8 - Rules on Delisting (involuntary delisting; original voluntary-delisting text)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2022/08/Supplemental-Rule-8.pdf"
  local_path: pdfs/pse-sr8-delisting-rules.pdf
  edition: in-force
  amended_through: undated
  note: "Involuntary delisting criteria, procedure and 5-year relisting ban remain in force; the voluntary-delisting section here (95% test, 60 days) is amended by SR 8.1."
- slug: pse-tpa-2026-0012-block-sale-ati-tender-offer
  title: "Execution of Block Sales for ATI Shares (TPA 2026-0012, 12 Mar 2026)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/TPA-2026-0012.pdf"
  local_path: pdfs/pse-tpa-2026-0012-block-sale-ati-tender-offer.pdf
  edition: historical
  amended_through: 2026-03-12
  note: "TPA-2026-0012 of 12 Mar 2026: special block sales of Asian Terminals (ATI) shares, including tender-offer results of 177,612,478 shares, executed 13 Mar 2026 at PHP3.60, with a trading suspension to follow for non-compliance with the MPO requirement."
- slug: sccp-clearing-house-rules-2018
  title: "Revised Clearinghouse Rules of the Securities Clearing Corporation of the Philippines (revised 13 Mar 2018)"
  publisher: "Securities Clearing Corporation of the Philippines"
  type: pdf
  canonical_url: "https://www.sccp.com.ph/resources/files/rules/SCCP_Revised_Rules_-_Approved_by_the_SEC_031318.pdf"
  local_path: pdfs/sccp-clearing-house-rules-2018.pdf
  edition: superseded
  amended_through: 2018-03-13
  note: "Still the version on sccp.com.ph; T+3 text superseded by SEC-approved T+2 amendments (memo 06-0823)."
- slug: sec-mc-1-2020-reit-irr
  title: "SEC MC No. 1 s.2020 - Revised Implementing Rules and Regulations of RA 9856 (REIT Act of 2009)"
  publisher: "Securities and Exchange Commission (Philippines)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2021/03/2020MCNo01_1.pdf"
  local_path: pdfs/sec-mc-1-2020-reit-irr.pdf
  edition: in-force
  amended_through: 2020-02-07
  note: "Revised IRR of RA 9856; effectivity 7 Feb 2020 per its p.1 (per another researcher). Amended in part by SEC MC 1 s.2026 (issued 8 Jan 2026, effective 25 Jan 2026): the 2026 text was NOT retrieved (sec.gov.ph 403) and is known only from a law-firm summary (cruzmarcelo-sec-reit-rules-2026), so page cites here describe the 2020 text."
- slug: bworld-pse-gpdr-derivatives-2024
  title: "BusinessWorld (via Metrobank Wealth Insights) - PSE eyes Q1 2025 for GPDR launch, derivatives by 2026 (23 Oct 2024)"
  publisher: "BusinessWorld (via Metrobank Wealth Insights)"
  type: web
  canonical_url: "https://wealthinsights.metrobank.com.ph/bworldonline/pse-eyes-q1-2025-for-gpdr-launch-derivatives-by-2026"
  local_path: null
  edition: n/a
  amended_through: 2024-10-23
  note: "Secondary-only; GPDR target Q1 2025; derivatives (PSEi futures) target Q1 2026; SEC and BIR frameworks required."
- slug: cruzmarcelo-sec-mc11-2026
  title: "Cruz Marcelo & Tan - SEC issues minimum public ownership rules for IPO applicants (SEC MC 11 s.2026)"
  publisher: "Cruz Marcelo & Tan"
  type: web
  canonical_url: "https://cruzmarcelo.com/sec-issues-minimum-public-ownership-rules-for-ipo-applicants/"
  local_path: null
  edition: n/a
  amended_through: undated
  note: "Law-firm page; its own publication date was not captured (SEC MC 11 s.2026 is dated 24 Feb 2026). Secondary-only; gives MC date 24 Feb 2026 and tier table (consistent with PSE rule); page publication date not captured (date shown is the MC date)."
- slug: cruzmarcelo-sec-reit-rules-2026
  title: "Cruz Marcelo & Tan - SEC amends REIT rules to expand eligible assets (SEC MC 1 s.2026)"
  publisher: "Cruz Marcelo & Tan"
  type: web
  canonical_url: "https://cruzmarcelo.com/sec-amends-reit-rules-to-expand-eligible-assets-and-strengthen-regulatory-framework/"
  local_path: null
  edition: n/a
  amended_through: undated
  note: "Law-firm page fetched 6 Oct 2026; its own publication date was not captured (SEC MC 1 s.2026 issued 8 Jan 2026, effective 25 Jan 2026). Secondary-only; page fetched 6 Oct 2026; MC issued 8 Jan 2026, effective 25 Jan 2026 (date shown is the MC date)."
- slug: fow-pse-derivatives-2026
  title: "FOW - Philippine Stock Exchange plans first derivatives in 2026 (29 Aug 2024)"
  publisher: "FOW (Financial Times Ltd)"
  type: web
  canonical_url: "https://www.fow.com/insights/3702078-philippine-stock-exchange-plans-first-derivatives-in-2026"
  local_path: null
  edition: n/a
  amended_through: 2024-08-29
  note: "Secondary-only; paywalled - only headline and first lines visible (MOU with a Taiwan exchange group)."
- slug: inquirer-sec-revamps-boards-2013
  title: "Philippine Daily Inquirer - SEC revamps listing board structure (2013)"
  publisher: "Philippine Daily Inquirer"
  type: web
  canonical_url: "https://business.inquirer.net/125871/sec-revamps-listing-board-structure/amp"
  local_path: null
  edition: n/a
  amended_through: undated
  note: "NOT FETCHED (HTTP 403); content known only from a search-result summary (two boards replacing three; Main: authorised capital >= PHP500m, 3 yrs, cumulative EBITDA >= PHP50m; SME: authorised capital >= PHP100m, 25% subscribed/paid). Treat as unverified."
- slug: insiderph-2024-08-05-metro-global-avoids-delisting
  title: "Close Call: Sobrepeña's Metro Global Holdings avoids automatic delisting"
  publisher: "InsiderPH"
  type: web
  canonical_url: "https://insiderph.com/close-call-sobrepenas-metro-global-holdings-avoids-automatic-delisting"
  local_path: null
  edition: n/a
  amended_through: 2024-08-05
  note: "Secondary-only; page content obtained through a WebFetch summary on 6 Oct 2026 (not raw text). Reports that FEMI transferred 55m MGH shares (~2% of outstanding) to Smart Share Investments Ltd, lifting MGH's public float to 10.67%, and PSE's statement that MGH would no longer be automatically delisted on 5 Aug 2024."
- slug: insiderph-villar-frozen
  title: "InsiderPH - Villar empire fights to regain footing as P320-B in stocks stay frozen (24 Aug 2026)"
  publisher: "InsiderPH"
  type: web
  canonical_url: "https://insiderph.com/villar-empire-fights-to-regain-footing-as-p320-b-in-stocks-stay-frozen"
  local_path: null
  edition: n/a
  amended_through: 2026-08-24
  note: "Secondary-only; overdue financial filings; six of seven Villar-listed firms (~PHP320bn) suspended ~3 months."
- slug: philstar-2021-12-07-medilines-debut
  title: "Medilines shares tank in volatile stock market debut"
  publisher: "Philstar.com"
  type: web
  canonical_url: "https://www.philstar.com/business/2021/12/07/2146329/medilines-shares-tank-volatile-stock-market-debut"
  local_path: null
  edition: n/a
  amended_through: 2021-12-07
  note: "Secondary; full text read."
- slug: philstar-nte-november
  title: "The Philippine Star - New PSE trading engine goes live by November (23 Jul 2026)"
  publisher: "The Philippine Star"
  type: web
  canonical_url: "https://www.philstar.com/business/business-as-usual/2026/07/23/2543942/new-pse-trading-engine-goes-live-november"
  local_path: null
  edition: n/a
  amended_through: 2026-07-23
  note: "Secondary-only; engine PHP241.03m, back office PHP45.83m."
- slug: philstar-rrhi-suspension
  title: "The Philippine Star - RRHI trading suspended as PSE exit looms (14 Jul 2026)"
  publisher: "The Philippine Star"
  type: web
  canonical_url: "https://www.philstar.com/business/2026/07/14/2541905/rrhi-trading-suspended-pse-exit-looms/amp/"
  local_path: null
  edition: n/a
  amended_through: 2026-07-14
  note: "Secondary-only; tender offer terms (JE Holdings, PHP48.30, 25 May-6 Jul), float 0.31%. Article dates suspension 14 Jul; PSE circular says effective 13 Jul (PSE used)."
- slug: pse-circular-index-2025-2026
  title: "PSE circulars CN-2023-xxxx to CN-2026-xxxx (subject-line index compiled by me from documents.pse.com.ph/CircularOPSPDF first pages)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: dataset
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/"
  local_path: null
  edition: in-force
  amended_through: 2026-09-25
  note: "Working index of 204 circular PDFs retrieved between CN-2023-0001 and CN-2026-0044 (25 Sep 2026); numbers returning HTTP 404 were skipped; first-page subject lines read by text extraction, scanned circulars by OCR or visual reading. The index file itself is not archived in kb."
- slug: pse-composite-sector-frame
  title: "PSE composite and sector indices frame (market summary for 5 Oct 2026)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: dataset
  canonical_url: "https://frames.pse.com.ph/compositeSector"
  local_path: null
  edition: in-force
  amended_through: 2026-10-05
  note: "PSEi 5,743.21; volume 414,323,178; value PHP3,742,813,171.58; advances/declines/unchanged 85/95/77."
- slug: pse-dds-frame
  title: "PSE Dollar Denominated Securities list frame"
  publisher: "The Philippine Stock Exchange, Inc."
  type: dataset
  canonical_url: "https://frames.pse.com.ph/dds"
  local_path: null
  edition: in-force
  amended_through: 2026-10-05
  note: "DMPA1, DMPA2, TCB2A, TCB2B."
- slug: pse-dds-page-web
  title: "PSE Dollar Denominated Securities product page"
  publisher: "The Philippine Stock Exchange, Inc."
  type: web
  canonical_url: "https://www.pse.com.ph/dollar-denominated-securities/"
  local_path: null
  edition: in-force
  amended_through: undated
  note: "Retrieved 6 Oct 2026. DDS vs the 2003 DDT facility; eligible-broker list (same 123 names)."
- slug: pse-delisted-companies-web
  title: "PSE Delisted Companies list (1980-present, with reason and effectivity date)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: web
  canonical_url: "https://www.pse.com.ph/delisted-companies/"
  local_path: null
  edition: in-force
  amended_through: 2026-08-31
  note: "Latest entry when retrieved 6 Oct 2026: RRHI, effective 31 Aug 2026. Used for delisting counts 2020-2026 and the RRHI 31 Aug 2026 date."
- slug: pse-etf-frame
  title: "PSE ETF list frame (FMETF iNAV)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: dataset
  canonical_url: "https://frames.pse.com.ph/etf"
  local_path: null
  edition: in-force
  amended_through: 2026-10-06
  note: "Shows FMETF only; iNAV 97.3388."
- slug: pse-etf-page-web
  title: "PSE Exchange Traded Fund product page"
  publisher: "The Philippine Stock Exchange, Inc."
  type: web
  canonical_url: "https://www.pse.com.ph/exchange-traded-fund/"
  local_path: null
  edition: in-force
  amended_through: undated
  note: "Retrieved 6 Oct 2026. Definition, creation/redemption steps, key parties, participants table (FMETF; First Metro Securities Brokerage Corp.)."
- slug: pse-ipo-listing-requirements-web
  title: "PSE IPO Listing Requirements (Main, SME, sponsor model; fees)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: web
  canonical_url: "https://www.pse.com.ph/ipo-listing-requirements/"
  local_path: null
  edition: in-force
  amended_through: undated
  note: "Retrieved 6 Oct 2026. Summary of CLDR criteria; still shows 20% minimum offering and the old PHP2m ALMF cap (stale vs Aug 2026 MPO rule and CN-2024-0068)."
- slug: pse-listed-company-directory-frame
  title: "PSE Listed Company Directory (frames.pse.com.ph/listedCompany) - all listed securities with sector, sub-sector, listing date and board"
  publisher: "The Philippine Stock Exchange, Inc."
  type: dataset
  canonical_url: "https://frames.pse.com.ph/listedCompany"
  local_path: null
  edition: in-force
  amended_through: 2026-10-06
  note: "Live table retrieved 6 Oct 2026: 406 HTML rows = 387 live securities + 11 symbol-less rows of already-delisted securities (ATI, 8990, Keppel Philippines A and B, RRHI, SFA; CPGP, SMC2A-2D) + 8 template rows. Security-type counts in these notes are my own classification by security name; sector strings are inconsistent (hand-normalised, +/-2)."
- slug: pse-listing-statistics-web
  title: "PSE Listing Statistics (new listings and number of listed companies 2021-2025)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: web
  canonical_url: "https://www.pse.com.ph/listing-statistics/"
  local_path: null
  edition: in-force
  amended_through: 2025-12-31
  note: "Table covers year-ends 2021-2025 (listed companies by board, new listings); page itself undated; retrieved 6 Oct 2026; the 'Capital Raised' tab did not render."
- slug: pse-new-listings-ipo-web
  title: "PSE New Listings / IPO page (IPOs, LBWIs, follow-ons, SROs)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: web
  canonical_url: "https://www.pse.com.ph/new-listings-ipo/"
  local_path: null
  edition: in-force
  amended_through: 2025-04-08
  note: "Latest entry on the page when retrieved 6 Oct 2026 was the TOP listing of 8 Apr 2025 (Maynilad, PNB Holdings and the 2026 follow-ons are not on it); page itself undated."
- slug: pse-nte-page-web
  title: "PSE Trading Engine 2026 overview page"
  publisher: "The Philippine Stock Exchange, Inc."
  type: web
  canonical_url: "https://www.pse.com.ph/pse-new-trading-engine/"
  local_path: null
  edition: in-force
  amended_through: undated
  note: "Retrieved 6 Oct 2026. One Lot One Share; derivatives enablement; CN-2025-0046 reference."
- slug: pse-press-1h2021-capital
  title: "PSE press release - Capital raising, trading activity up in 1H2021 (1 Jul 2021)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: web
  canonical_url: "https://www.pse.com.ph/capital-raising-trading-activity-up-in-1h2021/"
  local_path: null
  edition: n/a
  amended_through: 2021-07-01
  note: "1H21 PHP122.46bn; 2020 full-year PHP103.76bn."
- slug: pse-press-1h22-ipos
  title: "PSE press release - 1H22 IPOs match FY21 maiden offerings (1 Jul 2022)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: web
  canonical_url: "https://www.pse.com.ph/1h22-ipos-match-fy21-maiden-offerings/"
  local_path: null
  edition: n/a
  amended_through: 2022-07-01
  note: "1H22 PHP61.92bn."
- slug: pse-press-additional-reforms
  title: "PSE press release - PSE to introduce additional regulatory reforms (15 Jun 2026)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: web
  canonical_url: "https://www.pse.com.ph/pse-to-introduce-additional-regulatory-reforms/"
  local_path: null
  edition: n/a
  amended_through: 2026-06-15
  note: "ETF rule reform highlights; negotiated-trade facility; SBL directed pooled lending."
- slug: pse-press-agi-warrants
  title: "PSE press release - Alliance Global Group marks warrants listing (22 Dec 2025)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: web
  canonical_url: "https://www.pse.com.ph/alliance-global-group-inc-marks-warrants-listing/"
  local_path: null
  edition: n/a
  amended_through: 2025-12-22
  note: "AGIW terms and first-day move."
- slug: pse-press-allday-listing
  title: "PSE press release - AllDay Marts joins PSE's roster of listed firms (3 Nov 2021)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: web
  canonical_url: "https://www.pse.com.ph/allday-marts-inc-joins-pses-roster-of-listed-firms/"
  local_path: null
  edition: n/a
  amended_through: 2021-11-03
  note: "PHP4.5bn; LSI tranche 1.62x."
- slug: pse-press-alter-listing
  title: "PSE press release - Alternergy Holdings kicks off 2023 IPO listings (24 Mar 2023)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: web
  canonical_url: "https://www.pse.com.ph/alternergy-holdings-kicks-off-2023-ipo-listings-at-the-pse/"
  local_path: null
  edition: n/a
  amended_through: 2023-03-24
  note: "PHP1.62bn."
- slug: pse-press-areit-debut
  title: "PSE press release - AREIT debuts as the first REIT in the PSE (13 Aug 2020)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: web
  canonical_url: "https://www.pse.com.ph/areit-debuts-as-the-first-real-estate-investment-trust-in-the-pse/"
  local_path: null
  edition: n/a
  amended_through: 2020-08-13
  note: "PHP12.34bn raised."
- slug: pse-press-arthaland-foo
  title: "PSE press release - Arthaland concludes follow-on offering (2 Oct 2026)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: web
  canonical_url: "https://www.pse.com.ph/arthaland-corporation-concludes-follow-on-offering/"
  local_path: null
  edition: n/a
  amended_through: 2026-10-02
  note: "ALCPG/ALCPH."
- slug: pse-press-bncom-listing
  title: "PSE press release - Bank of Commerce lists maiden shares (31 Mar 2022)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: web
  canonical_url: "https://www.pse.com.ph/bank-of-commerce-lists-maiden-shares/"
  local_path: null
  edition: n/a
  amended_through: 2022-03-31
  note: "PHP3.36bn."
- slug: pse-press-converge-ipo
  title: "PSE press release - Converge debuts as biggest IPO in PSE (26 Oct 2020)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: web
  canonical_url: "https://www.pse.com.ph/converge-debuts-as-biggest-ipo-in-pse/"
  local_path: null
  edition: n/a
  amended_through: 2020-10-26
  note: "PHP29.08bn incl. overallotment."
- slug: pse-press-crec-listing
  title: "PSE press release - Citicore Renewable Energy Corp. lists P5.3B IPO shares (7 Jun 2024)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: web
  canonical_url: "https://www.pse.com.ph/citicore-renewable-energy-corp-lists-p5-3b-ipo-shares/"
  local_path: null
  edition: n/a
  amended_through: 2024-06-07
  note: "PHP5.30bn incl. US$12.5m MOBILIST."
- slug: pse-press-creit-listing
  title: "PSE press release - Citicore Energy REIT conducts IPO listing at the PSE (22 Feb 2022)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: web
  canonical_url: "https://www.pse.com.ph/citicore-energy-reit-corp-conducts-ipo-listing-at-the-pse/"
  local_path: null
  edition: n/a
  amended_through: 2022-02-22
  note: "PHP6.40bn."
- slug: pse-press-cts-listing
  title: "PSE press release - CTS Global Equity Group debuts as listed firm on SME Board (13 Apr 2022)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: web
  canonical_url: "https://www.pse.com.ph/cts-global-equity-group-debuts-as-listed-firm-on-sme-board/"
  local_path: null
  edition: n/a
  amended_through: 2022-04-13
  note: "PHP1.375bn."
- slug: pse-press-ddmpr-approval
  title: "PSE press release - PSE green-lights DDMPR IPO (26 Feb 2021)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: web
  canonical_url: "https://www.pse.com.ph/pse-green-lights-ddmpr-ipo/"
  local_path: null
  edition: n/a
  amended_through: 2021-02-26
  note: "Offer up to 5.94bn secondary shares at up to PHP2.25."
- slug: pse-press-filrt-listing
  title: "PSE press release - PSE welcomes FILRT in its roster of listed REIT companies (12 Aug 2021)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: web
  canonical_url: "https://www.pse.com.ph/pse-welcomes-filreit-in-its-roster-of-listed-reit-companies/"
  local_path: null
  edition: n/a
  amended_through: 2021-08-12
  note: "PHP12.58bn."
- slug: pse-press-haus-talk
  title: "PSE press release - Haus Talk starts off 2022 IPO listings in PSE (17 Jan 2022)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: web
  canonical_url: "https://www.pse.com.ph/haus-talk-starts-off-2022-ipo-listings-in-pse/"
  local_path: null
  edition: n/a
  amended_through: 2022-01-17
  note: "PHP750m."
- slug: pse-press-icts-p2t
  title: "PSE press release - International Container Terminal Services becomes PSE's first P2T company (15 Jul 2026)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: web
  canonical_url: "https://www.pse.com.ph/international-container-terminal-services-inc-becomes-pses-first-p2t-company/"
  local_path: null
  edition: n/a
  amended_through: 2026-07-15
  note: "ICT market cap PHP2.01tn."
- slug: pse-press-last-trading-day-2022
  title: "PSE press release - PSE marks last trading day of 2022 (29 Dec 2022)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: web
  canonical_url: "https://www.pse.com.ph/pse-marks-last-trading-day-of-2022/"
  local_path: null
  edition: n/a
  amended_through: 2022-12-29
  note: "2022 PHP110.29bn; 2021 PHP234.48bn; nine IPOs."
- slug: pse-press-last-trading-day-2025
  title: "PSE press release - PSE marks last trading day of 2025 (29 Dec 2025)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: web
  canonical_url: "https://www.pse.com.ph/pse-marks-last-trading-day-of-2025/"
  local_path: null
  edition: n/a
  amended_through: 2025-12-29
  note: "2025 capital raised, IPO count, domestic market cap."
- slug: pse-press-market-making
  title: "PSE press release - PSE releases amendments to market making rules for public comment (4 Jun 2026)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: web
  canonical_url: "https://www.pse.com.ph/pse-releases-amendments-to-market-making-rules-for-public-comment/"
  local_path: null
  edition: n/a
  amended_through: 2026-06-04
  note: "General market-making framework incl. GPDRs; comments to 23 Jun 2026."
- slug: pse-press-maynilad-greenlight
  title: "PSE press release - Maynilad gets PSE greenlight for IPO listing (6 Oct 2025)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: web
  canonical_url: "https://www.pse.com.ph/maynilad-water-services-inc-gets-pse-greenlight-for-ipo-listin/"
  local_path: null
  edition: n/a
  amended_through: 2025-10-06
  note: "Offer terms, overallotment and upsize options; LSI via PSE EASy."
- slug: pse-press-maynilad-ipo
  title: "PSE press release - Maynilad raises P34B on its stock market debut (7 Nov 2025)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: web
  canonical_url: "https://www.pse.com.ph/maynilad-water-services-inc-raises-p34b-on-its-stock-market-debut/"
  local_path: null
  edition: n/a
  amended_through: 2025-11-07
  note: "Second-largest IPO in PSE history."
- slug: pse-press-monde-ipo
  title: "PSE press release - PSE, government and private sector laud Monde Nissin on biggest IPO in Philippine stock market history (1 Jun 2021)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: web
  canonical_url: "https://www.pse.com.ph/pse-government-and-private-sector-laud-monde-nissin-on-biggest-ipo-in-philippine-stock-market-history/"
  local_path: null
  edition: n/a
  amended_through: 2021-06-01
  note: "PHP55.89bn."
- slug: pse-press-mreit-listing
  title: "PSE press release - MREIT marks IPO listing with bell ringing at four locations (1 Oct 2021)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: web
  canonical_url: "https://www.pse.com.ph/mreit-marks-ipo-listing-with-bell-ringing-at-four-locations/"
  local_path: null
  edition: n/a
  amended_through: 2021-10-01
  note: "PHP15.29bn; ~2x oversubscribed."
- slug: pse-press-mynld-psei
  title: "PSE press release - MYNLD to join PSEi, replacing CNVRG (27 Jul 2026)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: web
  canonical_url: "https://www.pse.com.ph/mynld-to-join-psei-replacing-cnvrg/"
  local_path: null
  edition: n/a
  amended_through: 2026-07-27
  note: "Early inclusion; revised index liquidity criteria (MTAR/MADV)."
- slug: pse-press-mynt-ipo-approval
  title: "PSE press release - PSE clears Mynt, Inc. for IPO (18 Sep 2026)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: web
  canonical_url: "https://www.pse.com.ph/pse-clears-mynt-inc-for-ipo/"
  local_path: null
  edition: n/a
  amended_through: 2026-09-18
  note: "GCASH IPO terms and timetable."
- slug: pse-press-nexgen-listing
  title: "PSE press release - PSE welcomes Nexgen Energy Corp.'s listing on SME Board (16 Jul 2024)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: web
  canonical_url: "https://www.pse.com.ph/pse-welcomes-nexgen-energy-corp-s-listing-on-sme-board/"
  local_path: null
  edition: n/a
  amended_through: 2024-07-16
  note: "PHP504m."
- slug: pse-press-ogp-listing
  title: "PSE press release - OceanaGold (Philippines) debuts on the PSE (13 May 2024)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: web
  canonical_url: "https://www.pse.com.ph/oceanagold-philippines-inc-debuts-on-the-pse/"
  local_path: null
  edition: n/a
  amended_through: 2024-05-13
  note: "PHP6.08bn secondary shares."
- slug: pse-press-pnb-holdings-lbwi
  title: "PSE press release - PNB Holdings Corporation lists shares on PSE (25 Sep 2026)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: web
  canonical_url: "https://www.pse.com.ph/pnb-holdings-corporation-lists-shares-on-pse/"
  local_path: null
  edition: n/a
  amended_through: 2026-09-25
  note: "LBWI, 46.93bn shares, PHP1.20."
- slug: pse-press-psei-6-5k-2024
  title: "PSE press release - PSEi closes trading year at 6.5K level (27 Dec 2024)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: web
  canonical_url: "https://www.pse.com.ph/psei-closes-trading-year-at-6-5k-level/"
  local_path: null
  edition: n/a
  amended_through: 2024-12-27
  note: "2024 PHP82.37bn vs 2023 PHP140.95bn; domestic market cap PHP14.57tn."
- slug: pse-press-psei-ends-2020
  title: "PSE press release - PSEi ends 2020 above 7,100 level (29 Dec 2020)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: web
  canonical_url: "https://www.pse.com.ph/psei-ends-2020-above-7100-level/"
  local_path: null
  edition: n/a
  amended_through: 2020-12-29
  note: "PSEi 7,139.71; ADV PHP7.35bn; net foreign selling PHP128.65bn."
- slug: pse-press-raslag-listing
  title: "PSE press release - Raslag Corp. holds maiden share listing (6 Jun 2022)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: web
  canonical_url: "https://www.pse.com.ph/raslag-corp-holds-maiden-share-listing/"
  local_path: null
  edition: n/a
  amended_through: 2022-06-06
  note: "PHP700m."
- slug: pse-press-rcr-listing
  title: "PSE press release - PSE welcomes RL Commercial REIT (14 Sep 2021)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: web
  canonical_url: "https://www.pse.com.ph/pse-welcomes-rl-commercial-reit-inc-to-its-roster-of-listed-firms/"
  local_path: null
  edition: n/a
  amended_through: 2021-09-14
  note: "PHP23.53bn."
- slug: pse-press-rcr-psei
  title: "PSE press release - RCR replaces AGI in PSE index (27 Jan 2026)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: web
  canonical_url: "https://www.pse.com.ph/rcr-replaces-agi-in-pse-index/"
  local_path: null
  edition: n/a
  amended_through: 2026-01-27
  note: "Index free-float >= 20% criterion."
- slug: pse-press-redc-listing
  title: "PSE press release - Repower Energy Development Corp. joins the ranks of publicly-listed companies (24 Jul 2023)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: web
  canonical_url: "https://www.pse.com.ph/repower-energy-development-corp-joins-the-ranks-of-publicly-listed-companies/"
  local_path: null
  edition: n/a
  amended_through: 2023-07-24
  note: "PHP1.05bn."
- slug: pse-press-reit-framework-forum
  title: "PSE press release - PSE, IHAP, FINEX hold forum on new Philippine REIT framework (11 Sep 2026)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: web
  canonical_url: "https://www.pse.com.ph/pse-ihap-finex-hold-forum-on-new-philippine-reit-framework/"
  local_path: null
  edition: n/a
  amended_through: 2026-09-11
  note: "SEC MC 1 s.2026 context; VITRO REIT application."
- slug: pse-press-smc-foo-2026
  title: "PSE press release - San Miguel Corporation raises P30B from follow-on offering (3 Aug 2026)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: web
  canonical_url: "https://www.pse.com.ph/san-miguel-corporation-raises-p30b-from-follow-on-offering/"
  local_path: null
  edition: n/a
  amended_through: 2026-08-03
  note: "SMC2V/W/X."
- slug: pse-press-spnec-ipo
  title: "PSE press release - Solar Philippines Nueva Ecija concludes IPO (17 Dec 2021)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: web
  canonical_url: "https://www.pse.com.ph/solar-philippines-nueva-ecija-concludes-ipo/"
  local_path: null
  edition: n/a
  amended_through: 2021-12-17
  note: "PHP2.7bn primary."
- slug: pse-press-top-listing
  title: "PSE press release - Top Line Business Development Corp. begins trading on PSE (8 Apr 2025)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: web
  canonical_url: "https://www.pse.com.ph/top-line-business-development-corp-begins-trading-on-pse/"
  local_path: null
  edition: n/a
  amended_through: 2025-04-08
  note: "PHP732.62m."
- slug: pse-press-upson-listing
  title: "PSE press release - Upson International holds maiden listing (3 Apr 2023)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: web
  canonical_url: "https://www.pse.com.ph/upson-international-corp-holds-maiden-listing/"
  local_path: null
  edition: n/a
  amended_through: 2023-04-03
  note: "PHP1.50bn primary + PHP150m secondary OA."
- slug: pse-press-vreit-listing
  title: "PSE press release - VistaREIT joins the ranks of PSE-listed firms (15 Jun 2022)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: web
  canonical_url: "https://www.pse.com.ph/vistareit-inc-joins-the-ranks-of-pse-listed-firms/"
  local_path: null
  edition: n/a
  amended_through: 2022-06-15
  note: "7.5bn shares listed; smallest REIT by capital raised."
- slug: pse-regulation-listed-company-web
  title: "PSE Regulations - Listed Companies (consolidated rules, supplemental rules, guidance notes index)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: web
  canonical_url: "https://www.pse.com.ph/regulation-listed-company/"
  local_path: null
  edition: in-force
  amended_through: undated
  note: "Retrieved 6 Oct 2026. Index of rule documents incl. SR 1-23 and May 2026 updates to SR 11 and SR 21."
- slug: pse-reit-frame
  title: "PSE REIT list frame"
  publisher: "The Philippine Stock Exchange, Inc."
  type: dataset
  canonical_url: "https://frames.pse.com.ph/reit"
  local_path: null
  edition: in-force
  amended_through: 2026-10-05
  note: "Eight REITs; the frame's volume columns read 0 (security frames used instead)."
- slug: pse-reit-page-web
  title: "PSE Real Estate Investment Trust product page"
  publisher: "The Philippine Stock Exchange, Inc."
  type: web
  canonical_url: "https://www.pse.com.ph/real-estate-investment-trust/"
  local_path: null
  edition: in-force
  amended_through: undated
  note: "Retrieved 6 Oct 2026. 1/3 public sale and <=1% NAV management-fee statements; eligible-broker list (123 names)."
- slug: pse-sec-frames-snapshot
  title: "PSE security information frames (frames.pse.com.ph/security/<symbol>): status, last price, volume, value, 52-week range, issued/listed/outstanding shares, Free Float Level, market cap, board lot, par value, FOL"
  publisher: "The Philippine Stock Exchange, Inc."
  type: dataset
  canonical_url: "https://frames.pse.com.ph/security/FMETF"
  local_path: null
  edition: in-force
  amended_through: 2026-10-05
  note: "387 live symbols fetched 6 Oct 2026 (15-minute delayed; 'As of' mostly the 5 Oct 2026 close): 385 with a status (320 Open, 65 Suspended), 2 PLDT preferred frames empty. The static block is partly stale: EPS fields are Dec-2023/9M-Sep-2024 and 'Free Float Level' carries no as-of date (see the vintage caveat in section 3). Parsed tabulations are mine."
- slug: tribune-pse-eases-float-2025
  title: "Daily Tribune - PSE eases public float level to 15%"
  publisher: "Daily Tribune"
  type: web
  canonical_url: "https://tribune.net.ph/2025/03/19/pse-eases-public-float-level-to-15"
  local_path: null
  edition: n/a
  amended_through: 2025-03-19
  note: "Secondary-only source for the temporary 20% -> 15% IPO float relief (2-year, extendable)."
```
