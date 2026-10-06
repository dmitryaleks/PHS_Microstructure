# PSE equities: market making, short selling, securities borrowing & lending, margin, and derivatives/hedging (status as of 6 October 2026)

Scope: feeds Chapters 8 ("Market making") and 9 ("Short selling and securities lending"). Equities focus. "Today" = 6 Oct 2026.

**Evidence labels.** `[P]` = primary source (rule text, regulator/exchange document, exchange-published data). `[S]` = secondary-only (news, law-firm note, data aggregator). `[I]` = my inference. Citation format: `[^slug:N]` = archived PDF in `kb/pdfs/<slug>.pdf`, N = physical 1-based page; `[^slug]` = web page (URLs in the Source catalog). Scanned PDFs (no text layer) were read by OCR (Windows OCR); where an OCR reading looked doubtful I say so.

## 0. Status board (what is in force vs pending), as of 6 Oct 2026

| Item | Status on 6 Oct 2026 | Key dates | Evidence |
|---|---|---|---|
| ETF market-making rules (Part C of PSE ETF Rules) | **IN FORCE.** The only exchange market-making regime; covers ETFs only. | SEC-approved 18 Mar 2013 | [P] [^pse-etf-rules:1], [^pse-press-2026-06-04-market-making] |
| Designated market makers | **One**: First Metro Securities Brokerage Corp. for the only ETF, FMETF. No equity (single-stock) market makers. | live PSE ETF page, crawled 6 Oct 2026 | [P] [^pse-etf-page] |
| "Amended PSE Market Making Rules" (general framework + ETF annex + GPDR annex) | **PROPOSED, not in force.** Consultation memo CN-2026-0026; PSE status 17 Aug 2026 "Revising per Public Comments"; not yet shown as submitted to/approved by SEC. | issued 3 Jun 2026; comments to 23 Jun 2026 | [P] [^pse-cn-2026-0026:1], [^pse-analyst-briefing-1h-2026:9] |
| SEC "Rules on Market Making" (umbrella; equities + fixed income) | **PROPOSED (SEC exposure draft).** PSE rules would become SEC-approved implementing guidelines. | SEC En Banc 13 Aug 2026; comments to 28 Aug 2026; PSE memo CN-2026-0039 of 20 Aug 2026 | [P] [^pse-cn-2026-0039-sec-market-making-rfc:1-2] |
| Short selling programme | **LIVE in rules since 2 Oct 2023; went live 6 Nov 2023.** 52 eligible securities (51 stocks + FMETF) on 5 Oct 2026. **Zero short-sale volume reported on every PSE Daily Short Sell Report, 6 Nov 2023 - 5 Oct 2026.** | go-live 6 Nov 2023 | [P] [^pse-cn-2023-0048:2], [^pse-cn-2023-0056:1], [^pse-dssr-2026-10-05:1-2] |
| SBL programme (onshore) | **LIVE.** Rules effective 15 Feb 2007. PDTC lending agent system onboarded first lenders/borrowers (22 Apr 2026); PSE announced readiness 18 May 2026. | 22 Apr / 18 May 2026 | [P] [^pse-sbl-short-selling-intro-presentation:2], [^pse-cn-2026-0022:1-2] |
| SBL: foreign "directed pooled lending" / offshore GMSLA model | **PENDING SEC approval.** Revised PSE SBL Rules submitted 16 Apr 2026; PSE status 17 Aug 2026 "For SEC Approval". | submitted 16 Apr 2026 | [P] [^pse-press-2026-06-15-reforms], [^pse-analyst-briefing-1h-2026:9] |
| SBL: MSLA clearance (PSE one-stop shop) | **IN FORCE** (SEC-approved 15 May 2026, effective immediately). | 15 / 22 May 2026 | [P] [^pse-cn-2026-0025:1-2] |
| Margin: SRC Rule 48.1 | **IN FORCE (old text):** credit <= 50% of market value; maintenance 25% long / 30% short. **Replacement draft exposed** 25 Aug 2026 (60% LTV, 30% maintenance); comments closed 15 Sep 2026; not adopted as far as found. | draft 25 Aug 2026 | [P] [^sec-2015-src-irr:165], [^sec-rfq-2026-src-rule-48-1-margin:1,9] |
| PSEi index futures / any listed derivative | **NOT LAUNCHED, no SEC-approved rules.** PSE drafting; vendor RFI July 2026; seeking multilateral funding (Aug 2026). | 2024 target "2026" has slipped | [P] [^pse-asm-2024-presidents-report:25], [^pse-analyst-briefing-1h-2026:10] |
| Structured (covered) warrants | **SEC DRAFT only** (exposed 28 Apr 2026; comments to 13 May 2026). None listed. | 28-29 Apr 2026 | [P] [^pse-cn-2026-0018:2] |
| GPDR (peso depositary receipts on foreign stocks) | **PENDING SEC approval** of revised rules submitted 24 Jun 2026 (targeted "within the quarter"). | 24 Jun 2026 | [P] [^pse-analyst-briefing-1h-2026:10] |
| New trading engine (Nasdaq Eqlipse) | Scheduled go-live 23 Nov 2026 (PSE broker forum 9 Jul 2026); lot size 1, odd-lot market abolished (PSE FAQ Aug 2026). Not live yet. | 23 Nov 2026 | [P] [^pse-nte-broker-forum-2026-07-09:9], [^pse-nte-faq-2026-08:1] |

**0.1 Dated timeline (primary unless marked)**

| Date | Event | Source |
|---|---|---|
| 9 Jun 2006 | SEC MC 7 s.2006, Rules on SBL | [^sec-mc-7-2006-sbl-rules:15] |
| 23 Jun 2006 | BIR RR 10-2006 (tax treatment of SBL) | [^bir-rr-10-2006-sbl:1] |
| 16 Nov 2006 / 5 Feb 2007 / 15 Feb 2007 | SEC approves PSE SBL Rules / PSE SBL Guidelines issued / both effective | [^pse-sbl-short-selling-intro-presentation:2] |
| 1 Feb 2008; 30 May 2008 | BIR RR 1-2008 (multilateral MSLA); BSP Circular 611 (foreign SBL, special BSRD) | [^bir-rr-1-2008-sbl:1], [^bsp-circular-611] |
| 8 Jun 2010 | Revised Trading Rules published (short-selling provisions) | [^pse-sbl-short-selling-intro-presentation:2] |
| 18 Mar 2013 | SEC-approved PSE ETF Rules incl. ETF Market Making Rules (Supplemental Rule 11) | [^pse-etf-rules:1] |
| 9 Nov 2015 | 2015 SRC IRR effective (Rules 24.2-2, 48.1) | [^sec-2015-src-irr-notice-of-effectivity:1] |
| 5 / 22 Jun 2018 | SEC approves / PSE publishes Short Selling Guidelines | [^pse-sbl-short-selling-intro-presentation:2] |
| 22 Jan 2019 | Short orders barred in Pre-Open and Pre-Close | [^pse-short-selling-guidelines:2] |
| 10 / 25 Feb 2020 | CMIC SBL and short-selling guidelines memo / effective | [^cmic-sbl-short-selling-guidelines:1] |
| 24 May, 21 Jul, 6 Sep 2023 | SEC accepts offshore collateral; PDTC conditional lending-agent approval; BIR accepts GMSLA registration | [^pse-cn-2023-0048:1-2], [^pse-sbl-short-selling-webinar-2023:3] |
| 2 Oct, 16 Oct, 6 Nov 2023 | Short Selling Guidelines effective; eligible list widened; programme go-live | [^pse-cn-2023-0048:2], [^pse-short-selling-guidelines-2023-10:1], [^pse-cn-2023-0056:1] |
| 5 Jun 2024 | BIR RR 10-2024 (MSLA/GMSLA registration, accession agreements) | [^pse-cn-2024-0035:3-4] |
| 1 Jul 2025 | Stock transaction tax cut to 0.1% (CMEPA) | [^bir-rr-20-2025-stt:2] |
| 3 Feb 2026 | PSE consults on revised SBL rules (offshore SBL, directed pooled lending) | [^pse-cn-2026-0009:1] |
| 28 Apr 2026 | SEC exposes structured-warrant rules | [^pse-cn-2026-0018:2] |
| 16 Apr 2026 | Revised PSE SBL Rules submitted to SEC | [^pse-press-2026-06-15-reforms] |
| 22 Apr / 18 May 2026 | PDTC lending pool onboards first lenders and borrowers / PSE announces readiness | [^pse-cn-2026-0022:1-2] |
| 15 May 2026 | SEC approves PSE 2026 MSLA clearance guidelines (PSE one-stop shop) | [^pse-cn-2026-0025:1] |
| 3 Jun 2026 | PSE consults on Amended Market Making Rules | [^pse-cn-2026-0026:1] |
| 24 Jun 2026 | Revised GPDR rules submitted to SEC | [^pse-analyst-briefing-1h-2026:10] |
| 13 Aug 2026 | SEC exposes Rules on Market Making | [^pse-cn-2026-0039-sec-market-making-rfc:2] |
| 17 Aug 2026 | PSE status: SBL rules "For SEC Approval"; market making "Revising per Public Comments" | [^pse-analyst-briefing-1h-2026:9] |
| 25 Aug 2026 | SEC exposes replacement Rule 48.1 (margin) | [^sec-rfq-2026-src-rule-48-1-margin:1] |
| 24 Sep 2026 | SEC exposes higher broker-dealer minimum capital (Rules 28.1/33.1; comments to 14 Oct 2026) | [^pse-memo-2026-10-01-sec-rfc-src-28-1-33-1-capital:2] |
| 23 Nov 2026 (scheduled) | Nasdaq Eqlipse go-live; lot size 1 | [^pse-nte-broker-forum-2026-07-09:9] |

**What a hedge fund can actually do on 6 Oct 2026 [I, built on the cited findings below]:**
- *Short PSE stocks onshore:* rules allow it in 52 names; infrastructure for locals exists (PDTC pool, BIR-registered MSLA); no short sale has ever printed; the offshore/GMSLA route foreign funds need is awaiting SEC approval. Treat as unavailable at scale.
- *Borrow stock:* only through PDTC's pool or bilateral MSLAs registered with the BIR via PSE; cash collateral; no public borrow-cost or inventory data.
- *Lever longs:* broker margin under SRC Rule 48.1 (<= 50% credit today; the one broker list documented, First Metro's, has 39 names); MSCI reports no overdraft facilities for foreign investors; the SEC draft raises the cap to 60%.
- *Hedge beta:* no onshore index future, option or covered warrant; offshore alternatives are EPHE, the PLDT ADR and OTC swaps (no listed options on either ETF/ADR found).
- *Rely on market makers:* only FMETF has one.

**Absence-of-news check [I].** PSE's press-room RSS feed (10 latest items, newest 2 Oct 2026) has nothing on SBL approval, market making, GPDR or derivatives after 14 Aug 2026 [^pse-press-feed]; public PSE circulars run to CN-2026-0044 (25 Sep 2026) but CN-2026-0036 to -0042 are not retrievable from the PSE circular store (404), so a late-Aug/Sep announcement cannot be excluded.

---

## 1. Market making (Chapter 8)

### Takeaway
The PSE has only one obligation-based liquidity regime: ETF market making (Part C of the PSE ETF Rules, SEC-approved 18 Mar 2013), and it covers a single ETF (FMETF) with a single market maker (First Metro Securities). There are no designated equity market makers. A new umbrella regime is being drafted twice over: PSE's "Amended Market Making Rules" (consultation 3-23 Jun 2026; keeps the 2013 ETF quoting numbers, adds incentives, a GPDR annex and a P100m capital test) and an SEC "Rules on Market Making" exposure draft (13-28 Aug 2026; capital floor P150m, equity and fixed income, PSE rules become SEC-approved implementing guidelines). Neither is in force; PSE says it is "revising per public comments" (17 Aug 2026).

### Cited findings

**1.1 In force today: ETF Market Making Rules (Part C, PSE ETF Rules, SEC-approved 18 Mar 2013)**
- [P] The document is headed "SEC Approved PSE ETF Rules, March 18, 2013"; Part C = "ETF Market Making Rules" with Implementing Guidelines. It is published by PSE as Supplemental Rule 11 (memo CN-2013-0010). [^pse-etf-rules:1] [^pse-etf-rules:15] [^pse-sr11-etf-rules-2026:1]  No later amendment to Part C was found; the only amendment proposal is the June 2026 consultation (below).
- [P] SEC layer: the SEC ETF Rules (SEC MC No. 10, series of 2012) define a Market Maker as "an Authorized Participant that assumes the obligation of providing two-way quotes following the rules of the Exchange and the Commission" (s.5(14)) and require at least two Authorized Participants, at least one of which acts as market maker (s.8(2)); PSE's Part C implements those sections. [^sec-etf-rules:5] [^sec-etf-rules:8]
- [P] ETF structure: at least two Authorized Participants (broker-dealers/trading participants, each with paid-up capital >= P100m); at least one AP must be designated the ETF Market Maker. [^pse-etf-rules:3]
- [P] Registration of an ETF Market Maker (Implementing Guidelines s.1): licensed broker/dealer; registered trading participant (TP); continuously operating as broker/dealer for the 5 years before application; at least 1 Designated Specialist (a licensed salesman); no violation or serious non-compliance in the last 2 years; processing fee P5,000 per issue. [^pse-etf-rules:21]  Registration and specialist accreditation valid 1 year, renewable; non-transferable. [^pse-etf-rules:15]  The PSE application/renewal checklist adds SEC Form 28-BDA, CMIC compliance certificates, Chinese-wall procedures under SRC 34.1, and a copy of the TP-ETF agreement. [^pse-etf-market-maker-renewal-checklist:1]
- [P] A market-making agreement with the ETF is a precondition: "Only when the ETF has a market making agreement with its Market Maker can its shares be subject of Market Making orders." [^pse-etf-rules:16]
- [P] **Quoting obligations (Implementing Guidelines s.2).** Obligations bite "upon occurrence of Wide Spread". Maximum spread by price band: P0.0001-0.4950 = 20 ticks; P0.5000-19.9800 = 15 ticks; P20.0000-999.5000 = 10 ticks; P1000 and above = 5 ticks. Minimum order quantity per market-making order = 5 board lots. Wide Spread = (a) spread larger than the limit, (b) one-sided quotation, or (c) no quotes on both sides, continuing for at least 3 minutes in Continuous Trading; the MM must enter orders within 90 seconds (not exceeding) to cure. **Presence: active market-making orders for >= 50% of each trading day** (hours/minutes with an active order while the market is open) **and >= 80% of the time over a month**. [^pse-etf-rules:16-17] [^pse-etf-rules:22-23]
- [P] Worked example in the rule: ETF at P25.00, tick 0.05, lot 100 -> 10 ticks = P0.50 maximum spread (2.0% of price) and minimum quote 500 shares; the MM may cure a P0.60 wide book with a single sell of 500 at P25.40 or a single buy of 700 at P25.00 (one-sided cure is enough). [^pse-etf-rules:23-24]
- [P] Segregation/accounts: MM must use its designated ETF Market Making account only for market-making orders and may keep only the market-making and error accounts for that ETF; Designated Specialist may not handle client orders or any other ETF the same day; MM is fully liable for all MM orders. [^pse-etf-rules:17-18]  Holding the ETF in the MM's own proprietary account is a "major violation". [^pse-etf-rules:20]
- [P] Sanctions: major violations include using the MM account for non-MM trades, unauthorized use, holding the ETF proprietary, reporting failures, continuous non-compliance; suspension/termination causes (substantial non-compliance, unpaid dues, SEC/CMIC/SCCP suspension); re-registration only after 3 months. [^pse-etf-rules:19-20]  Issuer-side: the ETF pays P500 per day for absence of an MM [^pse-etf-rules:13]; trading in the ETF is suspended if there is no MM for one month. [^pse-etf-rules:11]
- [P] Voluntary withdrawal needs 30 trading days' notice plus ETF consent; temporary suspension of duties is possible for technical problems, specialist unavailability, or other Exchange-approved reasons. [^pse-etf-rules:18-19]
- [P] Older trading-rule text: the Revised Trading Rules define "Market Maker" as a TP "primarily engaged by the issuer to provide liquidity to a Security, pursuant to an agreement", and "Designated Specialist" as the licensed salesman performing MM duties; Art. V "Market Making" is marked "pending final approval by the SEC" in this edition; Section 22 requires separate traders for proprietary, client and MM accounts and bars a Designated Specialist from client accounts. [^pse-revised-trading-rules:9] [^pse-revised-trading-rules:30] [^pse-revised-trading-rules:28]
- [P] PSE itself: "PSE's existing market making rules are for Exchange Traded Funds" (press release 4 Jun 2026). [^pse-press-2026-06-04-market-making]

**1.2 Pending: PSE "Amended PSE Market Making Rules" (consultation CN-2026-0026)**
- [P] Memo dated 3 Jun 2026 (signed R. S. Monzon), comments by e-mail to the Office of the General Counsel until 23 Jun 2026; attaches Annex "A" (14 sections + product annexes A ETFs and B GPDRs). Disclaimer: draft only, "may differ materially" from final. [^pse-cn-2026-0026:1-2]
- [P] Scope/definitions: general framework for all exchange-traded products; "Market Making" = continuous provision of liquidity through simultaneous two-way quotes; Designated Specialist = licensed salesman accredited by the Exchange. [^pse-cn-2026-0026:3]
- [P] Accreditation (s.3): SEC-registered broker-dealer; PSE TP; **unimpaired paid-up capital >= P100,000,000**; 3 continuous years as PSE TP, **or** at least two key personnel with >= 5 years' securities-trading experience on a local/WFE-member exchange; >= 1 Designated Specialist; clean record 2 years; no restraining orders. Application: letter of intent, board resolution, processing fee of **P5,000 per issue** (checked on the rendered page image; the OCR text had misread it as "25,000"), "or such other amount as may be prescribed"; same fee as the 2013 rule. Accreditation non-transferable, valid until terminated (no 1-year renewal cycle in the draft). [^pse-cn-2026-0026:3-5]
- [P] s.4: an MM may cover more than one product subject to Exchange approval; no MM order without a valid Market Making Agreement with the issuer **or the Exchange**. s.5 incentives: "Exchange and clearing fee concessions, price quoting services, connectivity support, **exemption from short selling restrictions**, and other incentives" via commercial agreements; key arrangements reported to SEC. [^pse-cn-2026-0026:5]
- [P] s.7: the Exchange sets product-specific (i) maximum spread, (ii) minimum order quantity, (iii) presence (minimum duration of two-way quotes); Exchange minima cannot be waived by the issuer agreement. s.8 "Wide Spread" = spread above Exchange limit, one-sided, or no quotes - **no 3-minute/90-second time parameters appear in the draft text**. [^pse-cn-2026-0026:6-7]
- [P] s.10: dedicated MM account only for MM orders; only MM and error accounts; books/records identify the Designated Specialist of the day. s.11 temporary suspension (technical problems, specialist unavailable, other cases) with public disclosure. s.13 withdrawal: 30 trading days' notice + issuer consent, 1-month cooling-off if consent missing. s.14: continuous failure -> PSE briefing -> suspension/revocation. [^pse-cn-2026-0026:8-9]
- [P] Annex A (ETFs): same price-band spread table as 2013 (20/15/10/5 ticks), 5 board lots minimum, presence >= 50% of time per trading day; **the 80% monthly presence test and 3-minute/90-second cure windows are not reproduced**. Annex B (GPDRs): identical numbers. [^pse-cn-2026-0026:10] [^pse-cn-2026-0026:14]
- [P] PSE press release: rules "updated based on global industry standards"; expansion "later" to individual stocks and other products; incentives "not previously available". [^pse-press-2026-06-04-market-making]
- [P] Status: "Market Making - Status: Revising per Public Comments" (PSE STAR briefing, 17 Aug 2026). [^pse-analyst-briefing-1h-2026:9]  After revision the rules go to the SEC for approval (press release). [^pse-press-2026-06-04-market-making]

**1.3 Pending: SEC "Rules on Market Making" exposure draft (PSE memo CN-2026-0039, 20 Aug 2026)**
- [P] SEC En Banc exposed the draft on 13 Aug 2026 (issued 14 Aug); comments to ipsd_msrd@sec.gov.ph until 28 Aug 2026. [^pse-cn-2026-0039-sec-market-making-rfc:1-2]
- [P] Scope: equity and fixed-income securities on an Exchange; Government securities excluded (BTr primary-dealer framework). Existing exchange MM rules continue "to the extent consistent with, and approved by the Commission as implementing guidelines". [^pse-cn-2026-0039-sec-market-making-rfc:3-4]
- [P] Qualification: unimpaired paid-up capital under an SEC risk-based framework, **never less than P150,000,000** (Exchange may calibrate upward); operating track record or key-personnel experience; 2-year clean record; Designated Specialist with >= 5 years' experience. Exchange accredits (no separate SEC process) but must notify SEC within 3 business days and report quarterly. [^pse-cn-2026-0039-sec-market-making-rfc:5-6]
- [P] Exchange designates eligible securities by liquidity/float/trading activity under SEC-approved criteria; **multiple market makers per security allowed** (coordination left to Exchange rules). Market Making Agreement required (issuer, Exchange or other approved party). [^pse-cn-2026-0039-sec-market-making-rfc:6]
- [P] Equity obligations (Rule VII): firm two-sided quotes for an Exchange-set minimum share of the session; maximum spread (price terms) and minimum quote size set by the Exchange, "risk-sensitive and differentiated by liquidity profile, public float and trading activity"; quotes firm/executable except for system failure, market-wide disruption, force majeure; inventory: maintain or have reasonable access to inventory/**securities-borrowing arrangements** ("not required to hold inventory at all times"); reliance on borrowing requires compliance with SBL rules. [^pse-cn-2026-0039-sec-market-making-rfc:8]
- [P] Permissible acts: own-account trading, bona fide hedging, block trades, stabilization; prohibited: wash/matched trades, artificial prices, misuse of MNPI, collusion with issuers, false information. [^pse-cn-2026-0039-sec-market-making-rfc:7]
- [P] Incentives (Rule IX): reduced transaction fees, **liquidity rebates**, simplified onboarding, enhanced trading facilities; must reward quoting performance, guard against excessive cancellations/artificial trading/excess inventory; **subject to prior SEC approval** and periodic review against performance data; general nature publicly disclosed. [^pse-cn-2026-0039-sec-market-making-rfc:9]
- [P] Transparency (Rule X): Exchange must publish names of accredited MMs and their securities, designated securities, obligations/parameters/performance standards, start/end/suspension of arrangements, issuer relationships, and may publish aggregate market-quality indicators (average quoted spread, quote presence, volume, depth); quarterly performance/compliance/incentive-utilisation reports to SEC; MM records (orders, quotes, inventory) kept >= 5 years. [^pse-cn-2026-0039-sec-market-making-rfc:10]
- [P] Rule XIII: surveillance of quoting obligations, inventory, spoofing/layering/wash trades/marking the close; temporary suspension allowed for system failure, force majeure, extraordinary volatility, cyber incidents, halts, "lack of inventory despite reasonable efforts, unavailability of securities lending, settlement disruption, or corporate action/record date restrictions"; sanctions = suspension/revocation, fines, referral. Effectivity 15 days after publication. [^pse-cn-2026-0039-sec-market-making-rfc:12-13]
- [I] The PSE draft's P100m capital test is below the SEC draft's P150m floor, so PSE's text will have to change (or the SEC figure will); the 17 Aug "revising" status is consistent with PSE re-basing on the SEC umbrella rules.
- [I] PSE's ETF proposal that the market maker "need not be" an Authorized Participant conflicts with the SEC ETF Rules definition (market maker = an Authorized Participant), so it needs a matching SEC amendment before it can take effect.

**Parameter comparison for implementers [P, from the cited pages]**

| Parameter | In force: 2013 ETF MM rules | PSE draft (3 Jun 2026) | SEC draft (exposed 13 Aug 2026) |
|---|---|---|---|
| Who qualifies | Authorized Participant of the ETF; licensed broker/dealer and TP; 5 yrs continuous operation; >= 1 Designated Specialist; clean 2 yrs [^pse-etf-rules:21] | SEC-registered broker-dealer and PSE TP; >= P100m unimpaired paid-up capital; 3 yrs as TP or 2 key staff with >= 5 yrs' experience; >= 1 Designated Specialist [^pse-cn-2026-0026:4] | Licensed-exchange TP; capital >= P150m (floor); track record or key personnel; Designated Specialist >= 5 yrs [^pse-cn-2026-0039-sec-market-making-rfc:5-6] |
| Maximum spread | 20 / 15 / 10 / 5 ticks by price band (0.0001-0.495 / 0.50-19.98 / 20-999.5 / >= 1000) [^pse-etf-rules:22] | same table (ETF and GPDR annexes) [^pse-cn-2026-0026:10] | Exchange-set, risk-sensitive by liquidity tier [^pse-cn-2026-0039-sec-market-making-rfc:8] |
| Minimum quote | 5 board lots per MM order [^pse-etf-rules:22] | 5 board lots [^pse-cn-2026-0026:10] | Exchange-set "Minimum Quote Size" [^pse-cn-2026-0039-sec-market-making-rfc:8] |
| Presence | >= 50% of each day; >= 80% of the month [^pse-etf-rules:22-23] | >= 50% of each day only [^pse-cn-2026-0026:10] | Exchange-set minimum duration of firm two-sided quotes [^pse-cn-2026-0039-sec-market-making-rfc:8] |
| Wide-spread timing | 3 min trigger; <= 90 s to cure [^pse-etf-rules:22] | not stated [^pse-cn-2026-0026:7] | not stated; firm quotes required except disruptions [^pse-cn-2026-0039-sec-market-making-rfc:8] |
| Incentives | none documented | fee/clearing concessions, quoting services, connectivity, short-sale exemption (commercial) [^pse-cn-2026-0026:5] | reduced fees, liquidity rebates, onboarding, enhanced facilities; SEC prior approval [^pse-cn-2026-0039-sec-market-making-rfc:9] |
| Registration life | 1 yr, renewable [^pse-etf-rules:15] | valid until terminated [^pse-cn-2026-0026:5] | per Exchange |
| Several MMs per product | ETF needs >= 1 MM (an AP) [^pse-etf-rules:3] | MM may cover several products [^pse-cn-2026-0026:5] | multiple MMs per security allowed [^pse-cn-2026-0039-sec-market-making-rfc:6] |

**1.4 Designated market makers and what they cover; performance data**
- [P] PSE ETF page ("ETF Participants", crawled 6 Oct 2026): FMETF - Market Maker: First Metro Securities Brokerage Corp.; Authorized Participant: First Metro Securities Brokerage Corp. No other ETF is listed in that table. [^pse-etf-page]
- [P] FMETF is on the short-selling eligible list (Oct 2026) and on First Metro's own margin list. [^pse-dssr-2026-10-05:1] [^firstmetrosec-margin-trading-agreement-v072026:6]
- [P] No equity market maker: PSE says existing MM rules are ETF-only [^pse-press-2026-06-04-market-making]; PSE was still "studying the introduction of market makers in the local market" in Mar 2026 and July 2025. [^pse-analyst-briefing-3m-2026:14] [^pse-asm-2025-presidents-report:30]  One broker was planning an information session on market making for new products (GPDRs, ETFs). [^pse-analyst-briefing-3m-2026:14]
- [P] Market-making collaboration agenda: PSE-TPEx MOU (10 Jun 2025) and Dec 2025 TWSE/TPEx/TAIFEX learning sessions. [^pse-analyst-briefing-3m-2026:15] [^pse-annual-report-2025:29]
- [P] GPDR/ETF reform context: ETF rule amendments (consultation CN-2026-0029, 16 Jun 2026, comments to 30 Jun 2026) would let the ETF Market Maker be a non-AP, require only one AP (an only-AP is deemed the MM) and suspend trading after one month without an MM. [^pse-cn-2026-0029-etf-amend-consult:4] [^pse-cn-2026-0029-etf-amend-consult:7] [^pse-cn-2026-0029-etf-amend-consult:18]
- Performance data: [P] no market-maker compliance, spread or presence statistics for FMETF are published in the PSE reports I checked; the SEC draft would oblige PSE to publish such indicators in future. [^pse-cn-2026-0039-sec-market-making-rfc:10]
- One-day proxy [P]: PSE's Daily Quotation Report for 2 Oct 2026 shows FMETF closing **bid 97.00 / ask 97.50**, volume 57,610 shares, value P5,602,625, net foreign selling P188,017; BDO the same day closed 110.40 / 110.60 on 2.87m shares and P317.4m. [^pse-eod-daily-quotation-2026-10-02:9] [^pse-eod-daily-quotation-2026-10-02:1]  With the tick table in the Revised Trading Rules (P0.05 tick for P50.00-99.95, 2010 edition; the ETF rule's own P25/0.05 example is consistent with it), P0.50 = 10 ticks, i.e. FMETF's closing quote sat exactly at the rule's maximum spread (0.52% of price vs 0.18% for BDO). [^pse-revised-trading-rules:21] [I: single closing snapshot, not a compliance test]

**1.5 Are market-maker quotes identifiable in the book?**
- [P] Public ITCH spec (OMX X-stream, v2.3): Add Order [A] carries order number, side, quantity, orderbook, price - **no broker or MM flag**. Executions come as [E]/[C]/[P] (anonymous) or [e]/[c]/[p] with passive and active Broker ID, depending on whether the exchange has "Broker Anonymity" in force. Orderbook Restrictions [k] carries a "Short Sell Eligible" flag. [^pse-itch-equities-feed-spec-v2-3:12] [^pse-itch-equities-feed-spec-v2-3:14-16] [^pse-itch-equities-feed-spec-v2-3:25]
- [P] MM orders are entered through a segregated "Market Making Account" (2013 rule s.17(b); 2026 draft s.10(c)), so PSE can identify them internally. [^pse-etf-rules:17] [^pse-cn-2026-0026:8]
- [I] Public identifiability therefore depends on whether broker IDs are displayed (anonymity setting not stated in the spec); for FMETF, First Metro is the sole MM so its broker code (if shown) would identify the quote.

**1.6 Incentives**
- [P] In force: none documented for the ETF MM (2013 rules list none); proposed PSE s.5 and SEC Rule IX incentives are above. [^pse-etf-rules:15-23] [^pse-cn-2026-0026:5] [^pse-cn-2026-0039-sec-market-making-rfc:9]
- [P] Tax angle: sales by a "dealer in securities" are carved out of the 0.1% stock transaction tax and taxed as ordinary income instead (BIR RR 20-2025, in force since 1 Jul 2025; same carve-out in the statute, RA 12214 amending Tax Code s.127); whether an MM qualifies as a dealer depends on facts. [^bir-rr-20-2025-stt:2-3] [^ra-12214-cmepa:16]
- [P] Short-sale relief: SRC Rule 24.2-2.5 already exempts "bona fide market-making or arbitrage activity executed by a broker dealer authorized to engage in such activities" from the uptick rule ("unless otherwise provided by the Commission"); PSE draft would add "exemption from short selling restrictions" as a negotiable incentive. [^sec-2015-src-irr:71] [^pse-cn-2026-0026:5]

### Inferences
- [I] Any displayed liquidity in PSE single stocks is voluntary (broker prop desks, other participants); no exchange-mandated quote exists for equities and none will before SEC approval of both the SEC umbrella rules and PSE implementing guidelines (earliest: after the SEC draft is finalised and published; effectivity is 15 days after publication).
- [I] For FMETF the obligation envelope is loose: 5 board lots minimum, spread up to 10 ticks (about 2% in the rule's own example), presence only 50% of the day, plus a 3-minute grace before "wide spread" and 90 seconds to cure - so FMETF quotes can be absent or wide for minutes without breach.
- [I] The proposed rules count quote size in "board lots" while PSE is moving to a standard lot of 1 with the new engine (odd-lot market abolished, "One Share, One Lot" targeted Q4 2026), so quote-size units will have to be restated in the final rules. [^pse-nte-faq-2026-08:1] [^pse-asm-2026-president-report:22]

### Execution implications
(All items below are my inferences [I] drawn from the cited rules.)
- Do not model a quoting counterparty in equities; treat FMETF as the only product with an obligated quoter (single MM, 50% presence). Expect gaps and wide spreads at open and in the first minutes after fast moves.
- If trading FMETF as a hedge, the spread you can rely on is the rule maximum (10 ticks = P0.50 at a P97 price, observed at the 2 Oct 2026 close), not typical equity spreads; FMETF trades only about P5-6m a day on that snapshot, and resting size beyond 5 board lots is not guaranteed.
- Watch for: (i) SEC Rules on Market Making finalisation; (ii) PSE implementing guidelines naming Designated Securities (likely PSEi names/ETFs/GPDRs first), spreads and presence per tier; (iii) liquidity-rebate/fee-concession schedules (SEC approval required) - these will change maker-taker economics around market makers' quotes.
- MM short-sale exemption and securities-borrowing preconditions mean a future equity MM will quote both sides from borrowed stock; borrow availability (Section 3) is a hard dependency.
- Feed handling: the book shows no MM tag in ITCH Add Order; do not assume you can filter MM liquidity from public data. Check broker-ID anonymity on the new Eqlipse-based feed after 23 Nov 2026.

### Gaps
- Final text/effective date of the amended PSE rules and the SEC Rules on Market Making (both unadopted as of 6 Oct 2026).
- Actual incentive economics (fee concession amounts) and any FMETF quoting/presence statistics; whether FMETF's MM has ever been sanctioned.
- Broker-anonymity setting in production feeds and whether the Eqlipse feed flags market-making orders.
- Any private liquidity-provider arrangements for individual stocks (e.g. IPO stabilisation/ price-support) outside the ETF rules.

---

## 2. Short selling (Chapter 9, part 1)

### Takeaway
Onshore short selling is legal, rule-complete and technically live: the PSE Short Selling Programme went live on 6 Nov 2023 (Guidelines effective 2 Oct 2023; SEC approved the Guidelines 5 Jun 2018). Eligible: PSEi, MidCap and Dividend-Yield constituents plus ETFs (52 securities on 5 Oct 2026), 10% short-interest cap, uptick/zero-plus price test, day orders only, flagged orders, borrow-before-sale (naked-short ban), daily public report. But PSE's Daily Short Sell Report shows zero volume on every one of its 707 published report files (6 Nov 2023 - 5 Oct 2026), MSCI says the programme "is not yet an established market practice", and PSE is still waiting for SEC approval of the SBL changes it says address "all regulatory hurdles to short selling".

### Cited findings

**2.1 Legal stack and dates**
- [P] SRC IRR (2015) Rule 24.2-2: definition of short sale with a net-long ownership test (24.2-2.1); short orders must be marked on the order and in all records and the broker must determine that the customer "has already borrowed the security" (24.2-2.3); only "qualified securities" (market cap, tradability, liquidity) (24.2-2.4); **uptick rule (24.2-2.5)**: no short sale on an exchange facility unless (1) at a price higher than the last sale or (2) at the last-sale price if that price is above the next preceding different sale price that day; exempt: bona fide market-making or arbitrage by an authorized broker-dealer; failure to deliver (24.2-2.6); **mandatory close-out** by the broker-dealer by the next business day after settlement date (24.2-2.7); directors/officers/principal stockholders may not short their own company (24.2-2.8); ledger of all short sales (24.2-2.9); SEC may prohibit short selling "indefinitely or for such period" or as an emergency measure (24.2-2.10). [^sec-2015-src-irr:70-71]
- [P] Revised Trading Rules Art. IV s.5: only Eligible Securities, principal or client; uptick rule (s.5.2(b)); short order valid for one trading day, not allowed in Pre-Open/Pre-Close; **naked short selling prohibited** (borrow first, or prior SBL agreement ensuring delivery on settlement date, or an exercisable unconditional right to deliver); order must be identified as a short sale at entry; PSE may suspend short selling in a stock, delist it from the eligible list, cap shares sold short, order a participant to stop or liquidate shorts, and require disclosure of open short positions to PSE and SEC (s.5.3). [^pse-revised-trading-rules:18-20] (same text excerpted at [^pse-trading-rules-art-iv-sec-5-short-selling:1-2])
- [P] Timeline: PSE SBL Rules approved by SEC 16 Nov 2006, SBL Guidelines 5 Feb 2007, both effective 15 Feb 2007; Revised Trading Rules (with short-selling provisions) published 8 Jun 2010; SEC approval of Short Selling Guidelines 5 Jun 2018, published 22 Jun 2018. [^pse-sbl-short-selling-intro-presentation:2]  PSE TPA 2023-0031: "The governing laws and rules on short-selling have been in place since 2010. Its implementation, however, awaited the implementation of the PSE's new trading system (PSEtrade) and the SBL program." [^pse-tpa-2023-0031:5]
- [P] CMIC Implementing Guidelines on SBL and Short Selling: SEC-approved, CMIC Memo 2020-005 dated 10 Feb 2020, effective 25 Feb 2020. [^cmic-sbl-short-selling-guidelines:1]  (SEC En Banc date 17 Dec 2019 [S]: [^pnl-law-cmic-guidelines-2020])
- [P] Enabling steps in 2023: SEC accepted offshore collateral for SBL (PSE memo 24 May 2023); PDTC got conditional SEC approval as lending agent 21 Jul 2023; BIR letter of 6 Sep 2023 accepting registration of a Global MSLA; Guidelines effective 2 Oct 2023 with MidCap and Dividend-Yield constituents added; go-live moved from 23 Oct to **6 Nov 2023**, requiring TPs to re-certify front-end order management systems (FEOMS) to tag short-sell orders. [^pse-cn-2023-0048:1-3] [^pse-sbl-short-selling-webinar-2023:3] [^pse-cn-2023-0056:1]

**2.2 Rule parameters (Guidelines, "as of October 2023", revised 16 Oct 2023)**
- [P] Eligible securities: all PSEi members, ETFs, MidCap constituents and Dividend-Yield constituents; Exchange may amend criteria. [^pse-short-selling-guidelines-2023-10:1]  (Jan 2019 text: PSEi + ETFs only [^pse-short-selling-guidelines:1])
- [P] **Short Interest Ratio (SIR) <= 10%** of outstanding shares per security, else the security becomes ineligible until SIR falls back; SIR monitored daily; status changes announced at end of day and effective next trading day; changing the 10% threshold needs prior SEC approval; PSE publishes gross short-sale transactions and outstanding short position daily. [^pse-short-selling-guidelines-2023-10:1]
- [P] Order handling: system rejects short orders in ineligible securities; only TPs may enter short orders (clients route through TPs); TP must determine the client has borrowing arrangements first; DMA clients: TP still enters the order unless the TP can verify the borrow before entry and meets Exchange conditions; **not accepted in Pre-Open and Pre-Close** (revised 22 Jan 2019 per SRC Rule 40.3.3); **day orders only**; no aggregation; **no odd-lot or block-sale short orders**. PSE's FAQ also lists run-off/trading-at-last as barred. [^pse-short-selling-guidelines-2023-10:2] [^pse-sbl-short-selling-page]
- [P] Price test: uptick rule per SRC Rule 24.2-2 and RTR s.5.2(b). PSE FAQ: price must be higher than last sale (e.g. last P1.00 -> P1.01 or higher) or equal to last sale only if that price is above the next preceding different sale price (zero-plus tick). [^pse-short-selling-guidelines-2023-10:2] [^pse-sbl-short-selling-page]  Numbering note [I]: the Guidelines point to "Section 3 of SRC Rule 24.2-2" (pre-2015 numbering) while the 2015 IRR numbers the same test 24.2-2.5, as PSE's FAQ does. [^sec-2015-src-irr:71]
- [P] Flagging: TP must flag short orders; a trade may not be amended from short sale to regular sale or vice versa. Depository transfers for short sales carry "SBL Borrow - Short Selling" / "SBL Return - Short Selling" tags; omnibus intra-account moves reported to PSE; "buyback" = purchase to cover. [^pse-short-selling-guidelines-2023-10:3]
- [P] FIX: tag 54 Side value 5 = "Short Sell" (Z = Buy Back, NASDAQ-defined); Side of an open order may be amended to/from short sell in the FIX session spec (distinct from the post-trade amendment ban above). [^pse-fix-specification-v2-5:53] [^pse-fix-specification-v2-5:26]  ITCH [k] message flags "Short Sell Eligible". [^pse-itch-equities-feed-spec-v2-3:12]
- [P] Penalties: Article IX of the Revised Trading Rules; CMIC treats naked short selling, uptick violations and insider short sales as "major" violations. [^pse-short-selling-guidelines-2023-10:4] [^cmic-sbl-short-selling-guidelines:6-7]
- [P] Client-side paperwork (CMIC guidelines): notarized Affidavit of Undertaking before the first short sale; borrowed-share records in stock debit/credit memos; "short" noted on order tickets and confirmations; short sales booked to the customer ledger, not the error account; MSLA/SLAA/confirmation notice on file; **the undertaking includes using the same trading participant for any buy-back of the shorted shares**. [^cmic-sbl-short-selling-guidelines:2-3] [^cmic-sbl-short-selling-guidelines:10] [^cmic-sbl-short-selling-guidelines:13]
- [P] Position reporting: TPs compute each account's aggregate short position per security as of the **15th and last day of each month** and file a written report with CMIC within 2 days; bi-annual SBL summaries within 15 days of each half-year; daily Depository Participant Report (DDPR) of SBL movements from TPs, custodians and lending agents (v1.7, 11 Jul 2023). [^cmic-sbl-short-selling-guidelines:5-6] [^pse-tpa-2023-0031:5-6]
- [P] Public disclosure: Daily Short Sell Report (DSSR) on pse.com.ph (Market Information > Market Reports) by end of each trading day, with short volume/value and SIR per eligible security; legend Y = short-sell and buy-back eligible, B = buy-back eligible only, IR = index recomposition, SI = SIR > 10%. [^pse-cn-2023-0056:1] [^pse-dssr-2026-10-05:2]

**2.3 Eligible securities today (5 Oct 2026)**
- [P] 52 securities flagged Y: AC, ACEN, AEV, AGI, ALI, APX, AREIT, BDO, BLOOM, BPI, CBC, CNPF, CNVRG, COSCO, CREIT, DMC, DNL, EMI, GLO, GSMI, GTCAP, ICT, JFC, JGS, KEEPR, LTG, MBT, MEG, MER, MONDE, MREIT, MWC, MYNLD, NIKL, OGP, PGOLD, PLUS, PNB, PX, RCR, RLC, SCC, SECB, SEVN, SGP, SM, SMC, SMPH, TEL, URC, WLCON (51 stocks) + FMETF. 9 flagged B (buy-back only, former eligibles after index changes): AUB, CEB, DD, DDMPR, FCG, FILRT, GMA7, PCOR, SHLPH. [^pse-dssr-2026-10-05:1-2]  The same 52 appear on PSE's live eligible-list page. [^pse-short-selling-eligible-list]
- [S] At launch there were 53 eligible securities (52 stocks + 1 ETF). [^gma-2023-10-20-short-selling-nov-6]
- [P] No PSEi-specific carve-outs beyond eligibility/SIR/PSE discretionary powers (suspension, caps, forced cover). PSEi constituents are the core of the list; foreign-ownership-limit (FOL) names carry a return risk for foreign lenders if FOL is breached before the shares are returned. [^pse-revised-trading-rules:19-20] [^pse-sbl-short-selling-page]

**2.4 Actual usage**
- [P] **All 707 distinct DSSR files (710 listed entries; three file names reused), 6 Nov 2023 - 5 Oct 2026, show "TOTAL VOLUME: 0 / TOTAL VALUE: 0.00" and "NULL" short-interest ratios for every security.** Archived samples: first day and latest day. [^pse-dssr-2023-11-06:2] [^pse-dssr-2026-10-05:2] (index of reports: [^pse-market-reports-dssr])
- [S] BusinessWorld, 12 Feb 2024: PSE launched short selling in November 2023 but "the latest daily short selling report ... showed that there have been no developments"; PSE CEO R. Monzon: the product "is really to target the foreign investors so that when the emerging market or the Philippine economy loses favor, instead of selling out, they can hedge"; "I don't expect short selling to take off in a big way right away because the market is down. Brokers have also to adopt their back office." [^bworld-2024-02-12-short-selling-recovery]
- [S] BusinessWorld, 6 Feb 2024 (Bloomberg data): 52 stocks incl. all PSEi shares plus one ETF may be shorted; local brokers' back ends and client systems are "configured for a long-only market"; many investors do not understand the set-up; some local brokerages planned to offer shorting to clients "by June" 2024. [^bworld-2024-02-06-short-selling-demand]  Philstar commentary (Merkado Barkada, 19 Feb 2024): "There have been zero short-selling transactions"; agreements among parties not yet signed. [^philstar-2024-02-19-merkado-barkada]
- [P] MSCI Global Market Accessibility Review, June 2026 (Philippines): "Stock Lending / Short Selling: The PSE Short Selling Program was implemented in November 2023. However, it is not yet an established market practice." Also 40% general foreign ownership limit; overdraft facilities for foreign investors prohibited. [^msci-accessibility-review-2026:43]
- [S] PSE CEO R. Monzon (Philstar, 2 Jul 2026): revised SBL rules "address all regulatory hurdles to short selling and this long-overdue investment strategy". [^philstar-2026-07-02-short-selling]

**2.5 Costs/tax on the short leg**
- [P] The short sale is a sale of listed shares: stock transaction tax of 1/10 of 1% (0.1%) of gross selling price since 1 Jul 2025 under CMEPA (prior rate 0.6% per secondary summaries [S]); DST on sales of listed shares is exempt. [^bir-rr-20-2025-stt:2] [^ra-12214-cmepa:16] [^pse-cn-2025-0032-bir-stt-advisory:1] [^bir-rr-19-2025-dst:3]  Borrow and return are tax-exempt only if the SBL conditions are met (Section 3).
- [P] BSP Circular 611 (30 May 2008): foreign borrowers get special "For SBL Transactions Only" BSRDs, may buy FX with the peso proceeds of the borrowed shares; equivalent shares bought back for return are not eligible for BSRD registration; collateral held under SBL is deducted from BSP-registered investments and cannot be repatriated while pledged; reports to BSP via FPIMS within 2 banking days. [^bsp-circular-611]

### Inferences
- [I] Zero prints in ~3 years = no practical short-selling capacity onshore, even for locals; for foreigners the missing piece is the offshore/GMSLA pathway pending SEC approval. Treat "short PH stocks onshore" as unproven plumbing, not a liquid strategy.
- [I] Even once the pathway opens, supply is limited to what PDTC's lending pool collects (pension funds, index funds, insurers being recruited) and cash collateral; expect scarce borrow in the 52 names and a binding 10% SIR cap on a name only if shorting becomes large.

### Execution implications
- Order entry: Side=5 (Short Sell) on FIX (per the pre-Eqlipse X-stream spec; the new engine's FIX spec is not public - re-check before 23 Nov 2026); only in continuous trading (not pre-open, pre-close, run-off/TAL); DAY orders only; no aggregation, no odd-lot/block; price must satisfy uptick or zero-plus test relative to last sale and the preceding different sale - an algo needs real-time last-sale/last-different-sale state and must reprice passive short orders as the last sale moves; the rules do not say whether the engine rejects a failing short order at entry or at match, so design for rejection at entry and re-validate resting orders after every last-sale change.
- Covering: buy-backs must go through the same TP that executed the short (CMIC undertaking); buy-to-cover remains possible in B-flag names; plan for mandatory close-out the business day after settlement if delivery fails (24.2-2.7).
- Pre-trade checks: SIR per name (DSSR) and eligibility flag changes announced at end of day, effective next day; short orders for ineligible names are rejected by the engine.
- Documents/lead time: BIR-registered MSLA (PSE pre-clearance now ~5 working days, accession 1 day), SLAA/service agreements, notarized undertaking, cash collateral account; lenders recall subject to settlement cycle. Plan weeks, not days, to be operational.
- Cost: 0.1% STT on each short sale leg (sale only; buy-to-cover is a purchase, no STT) plus borrow fee/collateral cost (no public fee data).
- Do not size strategies on short alpha in PH single names; use the offshore/derivative routes in Section 5 for hedging until shorting actually prints.

### Gaps
- No public data on borrow fees, lending-pool size, locate availability or recall experience.
- Whether any short sale has been executed but unreported; DSSR is the only public statistic.
- Exact definition of "last sale" for the uptick test (auction prints, odd-lot, block trades) not stated in the rules located, nor whether the engine applies the test at entry or at match.
- Whether DMA/direct clients can self-enter short orders today (Guideline 2(d) requires TP capability and Exchange-imposed conditions; none found published).
- Status after 5 Oct 2026 of SEC approval of the revised SBL rules.

---

## 3. Securities borrowing and lending (Chapter 9, part 2)

### Takeaway
SBL is regulated by SEC MC 7/2006, the PSE SBL Rules (effective 15 Feb 2007), BIR RR 10-2006 (as amended by RR 1-2008 and RR 10-2024) and BSP Circular 611. Since April-May 2026 the PDTC Lending Agency Service has an operating onshore lending pool (cash-collateralised) with its first lenders and borrowers onboarded; PSE has also become the one-stop shop for MSLA clearance and BIR registration (SEC-approved 15 May 2026). The foreign-participation model (offshore GMSLA/"directed pooled lending") is still awaiting SEC approval. No SBL volume statistics are public.

### Cited findings

**3.1 Framework and participants**
- [P] SEC MC 7 s.2006 (9 Jun 2006): covers brokers, dealers, banks, insurers and other persons; lending agents must register with the SEC (fee P50,000; lending-system requirements); direct lenders limited to banks (incl. foreign bank branches), investment houses, investment companies, insurers, government/BSP-authorised pension funds, securities dealers and others the SEC declares; loanable securities = exchange-listed securities and BTr/BSP securities in electronic form; collateral cash, equity or government securities; marked to market daily and **maintained at >= 102% (cash/government) or >= 105% (equity)**; title passes to borrower; foreigners may not borrow from Filipinos equities of nationalized-activity companies unless a foreign-ownership monitoring mechanism exists; exchanges may adopt SBL programmes approved by the SEC; fines P20,000/P30,000/P50,000 per order/transaction or 2x amount. [^sec-mc-7-2006-sbl-rules:2] [^sec-mc-7-2006-sbl-rules:5-8] [^sec-mc-7-2006-sbl-rules:10-11] [^sec-mc-7-2006-sbl-rules:13-15]
- [P] PSE SBL Rules: cover local/foreign borrowers and lenders; TPs act as principal or "Agent-Facilitator" and **must engage a Lending Agent** (2.01-2.02); bi-annual SBL reports; clients may not lend through the TP if that creates negative RBCA exposure (2.08); Exchange may restrict or prohibit borrowing/lending of any listed share (3.01); SBL may not circumvent manipulation/fraud rules (3.02). [^pse-sbl-rules:2-5]
- [P] Operating models (PSE deck 2023): (1) TP lends its proprietary shares; (2) TP as registered lending agent with a multilateral MSLA; (3) different TPs as intermediaries on the lending and borrowing sides; (4) **foreign client borrowers**: lending agent -> MSLA with the foreign borrower, shares delivered to the borrower's custodian bank via "EQ Trade", borrower gives the executing broker the MSLA and confirmation notice as proof the short is covered. [^pse-sbl-models-2023:1-4]
- [P] **PDTC as lending agent.** SEC conditional approval 21 Jul 2023. [^pse-sbl-short-selling-webinar-2023:3]  Lenders sign an SLAA with their depository participant (SLAA1), which signs SLAA2 with PDTC; the borrowing DP signs an MSLA with PDTC; clients are not MSLA signatories. [^pse-cn-2023-0053:1-2]  PDTC memo 03-2026 (22 Apr 2026): lenders and borrowers with BIR-registered agreements onboarded; lenders input lending instructions into the Lending Pool; borrowers check availability and request loans if cash collateral is sufficient; borrowers open a separate cash-collateral bank account; letters of intent to PDTC (role: lender, borrower or both). [^pse-cn-2026-0022:2]  PSE CN-2026-0022 (18 May 2026) announces readiness. [^pse-cn-2026-0022:1]  PSE/PDTC are engaging pension funds, index funds and insurers to populate the pool. [^pse-press-2026-06-15-reforms]
- [P] PSE SBL Guidelines (operating practice): lender must state in the confirmation notice whether it acts as direct lender or lending agent; TPs file the BIR registration certificate with PSE within 15 days; daily mark-to-market; title to lent shares passes and **voting rights pass with title** unless a written proxy/voting trust is executed (lending a whole holding can cut the lender off from corporate-event information); recall on prior notice within the normal settlement cycle; agent-facilitators must identify principals before each transaction (at least by agreed code). [^pse-sbl-guidelines:2-4]
- [P] Insurers may lend under Insurance Commission rules (circular letter filed by PSE as IC CL 2019-45; printed date legible only as "04 September 20[18/19]"). [^ic-cl-2019-45-sbl:1]
- [P] Who may borrow/lend: BIR RR 10-2006 s.4: no restriction on the status or qualifications of a Borrower (need not be PSE-registered) or a Lender (foreign lenders contemplated); RR 10-2024 qualifies the Lender limb with "except those provided in SEC and PSE regulations". [^bir-rr-10-2006-sbl:3] [^pse-cn-2024-0035:4]

**3.2 Tax treatment**
- [P] RR 10-2006 s.5 as amended by RR 1-2008 s.5 and RR 10-2024 s.4: SBL of PSE-listed shares and delivery/return of collateral and equivalent shares are **not subject to stock transaction tax, capital gains tax or documentary stamp tax** (DST under the cited Tax Code sections) provided (i) a valid MSLA is executed and registered with/approved by the BIR, (ii) the SBL programme complies with SEC rules and (iii) it is administered and supervised by the PSE; all other taxes apply. Approval retroacts to the date of complete submission. [^bir-rr-10-2006-sbl:4] [^bir-rr-1-2008-sbl:4] [^pse-cn-2024-0035:4]
- [P] Permitted purposes (RR 10-2006 s.6(f)): settlement of a sale; settlement of a future sale; replacement of another borrowing; on-lending; financing/collateral pledging; other BIR-authorised purposes; maximum borrowing period 2 years. [^bir-rr-10-2006-sbl:2] [^bir-rr-10-2006-sbl:5-6]
- [P] "Deemed sale" triggers (no stock return at end of period, use outside specified purposes, default, defective MSLA, late/no registration, loans outside the period): taxed as sales (CGT on a deemed off-exchange sale, DST). RR 10-2024: if the borrower fails to return, the lender may buy equivalent shares on the exchange with the collateral, and that purchase bears stock transaction tax. [^bir-rr-10-2006-sbl:9-10] [^pse-cn-2024-0035:8]
- [P] Manufactured dividends are not taxable income of the lender and not deductible by the borrower. [^bir-rr-10-2006-sbl:4]
- [P] Registration mechanics: PSE one-stop shop (SEC-approved 15 May 2026, effective immediately): PSE receives documents and the P5,000 BIR fee, pre-clears within 5 working days (accession agreements: 1 working day), transmits to BIR, SEC no longer pre-clears or certifies (post-audit only); fees P5,000 PSE + P5,000 BIR per MSLA (per borrower for multilateral/accession); BIR registration within 2 weeks if executed in the Philippines, 1 month if executed abroad (from apostille/authentication per RR 10-2024); registration valid until revoked; foreign-executed agreements need not be consularized/apostilled for PSE pre-clearance if parties warrant due execution; margin rate in the MSLA addendum cannot be < 102% (cash/government) or < 105% (equity). [^pse-cn-2026-0025:1-2] [^pse-msla-clearance-guidelines-2026:1-4] [^pse-cn-2024-0035:7]
- [P] GMSLA for foreign parties: BIR may register a GMSLA with a PSE-prescribed supplemental agreement (letter 6 Sep 2023; codified in RR 10-2024); offshore collateral approved by SEC (24 May 2023): cash in USD/EUR/JPY/GBP/AUD, OECD government/agency debt rated at least BBB, and constituents of WFE-member benchmark indices. [^pse-cn-2023-0048:1-2] [^pse-cn-2024-0035:6]
- [S] SEC streamlining reported by Philstar (10 Jun 2026): processing cut from 7 to 5 working days, SEC fee of P5,030 removed. [^philstar-2026-06-10-sbl-framework]

**3.3 Pending: revised PSE SBL Rules ("directed pooled lending", offshore SBL)**
- [P] Consultation CN-2026-0009 (3 Feb 2026; comments to 18 Feb 2026): allow an SEC-registered **onshore Lending Agent** (PDTC) to facilitate the Philippine leg of SBL between foreign lenders and foreign borrowers using offshore collateral under a GMSLA; collateral managed offshore by a third-party collateral manager (non-cash) or the lender/offshore agent (cash); default handled offshore; onshore custodian/TP notifies the lending agent and remits any CGT; reports cut from 9 to 4/3; PSE audit right added. Stated aim: "induce foreign participation". [^pse-cn-2026-0009:3-7] [^pse-cn-2026-0009:9-14]
- [P] PSE's FY2025 annual report frames the friction being removed: the proposal "remov[es] the requirement for offshore lending agents to separately register in the Philippines" (SEC MC 7 s.4 registration) by letting an SEC-registered onshore lending agent handle the Philippine leg; PSE was also working with SEC and BIR to streamline MSLA registration (done 15 May 2026). [^pse-annual-report-2025:37]
- [P] Submitted to the SEC 16 Apr 2026; status 17 Aug 2026 "For SEC Approval". [^pse-press-2026-06-15-reforms] [^pse-analyst-briefing-1h-2026:9]
- [S] SEC comments (meeting 6 May 2026): include onshore custodians' responsibilities, benchmark that brokers are SBL facilitators not lending agents, update the GMSLA supplement/annex. [^philstar-2026-07-02-short-selling]

**3.4 Usage**
- [P] No public SBL volume, lending-pool size or fee data located. The only quantitative signal is the DSSR (zero short volume) and PDTC reporting only that its "first set" of borrowers/lenders were onboarded (Apr-May 2026). [^pse-cn-2026-0022:1] [^pse-dssr-2026-10-05:2]
- [P] SBL "reasons for borrowing" per PSE include avoiding settlement failure, short selling, arbitrage/derivatives support and market making. [^pse-sbl-short-selling-page]

### Inferences
- [I] Onshore SBL exists mainly as plumbing; liquidity in the lending pool will be thin until institutions are signed up, and PSE's pitch to pension/index/insurance funds in June 2026 suggests supply is still being recruited.
- [I] Foreign hedge funds' realistic route is offshore GMSLA with a PH-registered agent, which needs the pending SEC approval; until then foreign borrowers face the older onshore route (BIR-registered MSLA, BSP special BSRD, cash collateral in PH).

### Execution implications
- Treat borrow as a pre-trade dependency with onboarding measured in weeks [I]: PSE pre-clearance up to 5 working days, BIR action within 5 working days of a complete filing (RR 10-2024), plus PDTC systems training, a cash-collateral bank account and client-side SLAA/service agreements; collateral is cash in the pool model (separate cash-collateral bank account) and must stay >= 102%/105%.
- Corporate actions: manufactured dividends/benefits flow to the lender; lender may recall within the settlement cycle (the PSE FAQ still says T+3; PSE announced migration to T+2 on 23 Jun 2023) [^pse-cn-2023-0031-t2-settlement:1]; FOL breaches can block returns to foreign lenders.
- Tax cliff: any failure to meet MSLA/return conditions converts the loan into a taxable sale/purchase (STT 0.1% on exchange repurchase; CGT/DST on a deemed off-exchange sale) - build return-date monitoring (max 2 years) and registration deadlines (2 weeks/1 month) into the operations stack.
- BSP: foreign borrowers should expect special BSRD coding and FX reporting under Circular 611; confirm with a custodian before each programme.

### Gaps
- Fee levels/rebates, utilisation, lendable inventory; PDTC operating guidelines text (referenced in CN-2023-0053 but not archived).
- Whether BSP Circular 611 has been replaced by a later BSP issuance for the offshore model (it is cited by PSE as the operative FX rule in its FAQ; not re-verified in the 2025 FX manual).
- Final SEC decision on the revised PSE SBL Rules.

---

## 4. Margin trading and bank lending against shares (Chapter 9, part 3)

### Takeaway
Margin lending is by broker-dealers under SRC Rule 48.1: currently credit up to 50% of market value, maintenance margin 25% (long) / 30% (short) and a P50,000 minimum equity. The SEC exposed on 25 Aug 2026 a replacement framework (60% maximum credit, 30% maintenance, PSE-run margin rules, interim eligibility limited to PSEi and MSCI Philippines constituents, P150m minimum capital for new margin lenders). Brokers apply stricter house rules (First Metro: P200,000 opening equity, 0.90%/month interest, liquidation below 30% equity).

### Cited findings
- [P] Statute: SRC s.48.1 (RA 8799) tells the SEC to prescribe credit limits "in accordance with the credit and monetary policies that may be promulgated from time to time by the Monetary Board of the Bangko Sentral", with a ceiling standard of the higher of 65% of the current market price or 100% of the lowest price in the preceding 36 months (but not more than 75%); the Monetary Board "may increase or decrease the above percentages". So the BSP's Monetary Board, not the SEC, holds the statutory power to move the margin percentages; the SEC's current 50% rule sits below the statutory ceiling and the draft 60% would too. [^ra-8799-src:50]
- [P] Operative rule: 2015 IRR Rule 48.1: (48.1.1) broker-dealer may not extend credit above **50%** of the current market value at the time of the transaction and no new credit if account equity < **P50,000**; (48.1.2) margin maintained >= **25%** of the market value of long positions and **30%** of short positions; (48.1.3) initial-margin call to be met within 5 business days, maintenance call within 24 hours, no purchase/sell orders on the account until cured; (48.1.4) liquidate before the close of the next trading day if the call is unmet; (48.1.5) 7-day extension for initial margin on application to the Exchange. [^sec-2015-src-irr:165]  Rule 48.2: credit only against securities collateral. [^sec-2015-src-irr:165]
- [P] **Proposed Rule 48.1 replacement** (SEC En Banc 25 Aug 2026; comments to 15 Sep 2026): PSE would write "Exchange Margin Trading Rules" within 90 days of effectivity; interim margin-eligible securities = PSEi and MSCI Philippines Index constituents plus Exchange-designated; interim requirements: **credit <= 60%** of market value, minimum equity P50,000, **maintenance >= 30%**, margin call to be met within 3 trading days, forced liquidation without notice, liquidation notice by next business day, 7-day extension retained; new margin lenders need unimpaired paid-up capital >= **P150,000,000**, RBCA compliance, no major PSE margin-rule penalty in the prior 2 years. [^sec-rfq-2026-src-rule-48-1-margin:1] [^sec-rfq-2026-src-rule-48-1-margin:6-7] [^sec-rfq-2026-src-rule-48-1-margin:9-10]  (Law-firm summary dated 9 Sep 2026 [S]: [^cruzmarcelo-2026-09-09-margin].) Status: proposal only; no adoption found as of 6 Oct 2026. [I]
- [P] Broker practice (First Metro Securities margin agreement v07/2026): opening requirement P200,000 cash/marginable securities; minimum equity P50,000; interest **0.90% per month plus VAT** on daily debit balance; margin alert below 50% equity (buying suspended), margin call below 40% (restore to 50%), forced sale below 30%; 39 marginable securities (38 stocks + FMETF), all with a 100% margin rating (i.e. broker-determined). [^firstmetrosec-margin-trading-agreement-v072026:1-3] [^firstmetrosec-margin-trading-agreement-v072026:6]
- [P] Foreign investors: MSCI notes overdraft facilities for foreign investors are prohibited and FX transactions must be linked to security transactions (June 2026). [^msci-accessibility-review-2026:43]
- [P] BSP: no numeric ceiling on bank lending to finance share purchases was located. BSP Circular 432 (2004) fixes the loan value of "blue chip" stock collateral at 50% of market value (issuer listed, net worth >= P1bn, five consecutive profitable years; not the lender's own shares) in MORB X313.b, X322.2 and X326.1k(5). [^bsp-circular-432]
- [S/I] Prevalence: margin is offered by at least some brokers (First Metro documented); no PSE statistic on margin debt located.

### Inferences
- [I] The proposal raises permitted leverage (50% -> 60% credit, i.e. 40% initial equity) and loosens call timing (24h/5 days -> 3 trading days) while concentrating eligibility on PSEi and MSCI constituents; it also lifts the capital bar for lenders. Not in force yet.
- [I] A hedge fund wanting leverage onshore would normally use prime-broker/swap financing offshore rather than a Philippine margin account; local margin is built for retail/HNW with small tickets (P200k openers).

### Execution implications
- Even under the proposal, margin eligibility is by broker list: model financing capacity per broker house list and haircut, not the SEC maximum.
- Margin liquidation is rules-based and fast (24h maintenance calls today; before next close if unmet): do not assume time to cure in stressed markets.
- Short positions in a margin account carry 30% maintenance today; short sales under the SBL route are collateralised by cash instead.

### Gaps
- Final SEC Rule 48.1; PSE Exchange Margin Trading Rules (not yet written); statistics on margin debt/prevalence; any BSP limit on bank margin or stock-collateralised lending beyond the 2004 circular.

---

## 5. Derivatives and hedging instruments (Chapter 9, part 4)

### Takeaway
There is no listed derivative on PSE equities: no index futures, single-stock futures, options, or covered/structured warrants. PSE plans PSEi index futures first but has slipped from a "2026" target to rule-drafting plus vendor RFI and fund-raising; SEC structured-warrant rules are only a draft. Foreigners must hedge via offshore routes: the US-listed iShares MSCI Philippines ETF (EPHE), PLDT's NYSE ADR, OTC swaps/P-notes (no public PH-specific data), none with listed options found.

### Cited findings
- [P] PSE plan trail: ASM 2024 (6 Jul 2024): Derivatives "Target Launch: 2026", index futures on PSEi [^pse-asm-2024-presidents-report:25]; PSE-TWSE MOU 27 Aug 2024 (derivatives via TAIFEX) [^pse-asm-2025-presidents-report:28]; PSE-Nasdaq Eqlipse upgrade announced 22 May 2025 "enabling new financial instruments such as derivatives" [^pse-asm-2025-presidents-report:25]; ASM 2025 (12 Jul 2025): "set to launch index futures based on the PSEi" [^pse-asm-2025-presidents-report:30]; TAIFEX learning sessions 15-18 Dec 2025 [^pse-annual-report-2025:29]; FY2025 annual report: "PSE's rules for derivatives are slated to be finalized in the second half of 2026" [^pse-annual-report-2025:38]; ASM 2026 (4 Jul 2026): early exposure draft to select institutions, vendor RFI targeted early July [^pse-asm-2026-president-report:24]; PSE STAR briefing (17 Aug 2026): RFI released in July; next step "discussions with multilaterals for possible funding" [^pse-analyst-briefing-1h-2026:10]. The FY2025 annual report adds that Eqlipse's modular design allows "advanced options pricing and index calculations" to be integrated later. [^pse-annual-report-2025:37]
- [P] No SEC derivative-exchange rules/approvals located; SRC IRR Rule 25 only bars exchange members from endorsing/guaranteeing options on listed securities. [^sec-2015-src-irr:72]
- [P] **Structured warrants**: SEC exposure draft (En Banc 28 Apr 2026; comments to 13 May 2026; PSE memo CN-2026-0018 of 30 Apr 2026): issuers = licensed broker-dealers or investment houses with >= P400m unimpaired paid-up capital; underlyings = PH or WFE-member foreign single equities, securities indices, ETFs, debt, baskets; index-linked and foreign-listed warrants cash-settled; issuer discloses whether it will quote or appoint **one** market maker, with disclosed maximum spread, minimum quantity and daily presence; further issues for market-making limited so issuer+MM hold <= 50%. [^pse-cn-2026-0018:2] [^pse-cn-2026-0018:5-6] [^pse-cn-2026-0018:8-9] [^pse-cn-2026-0018:19]  PSE status 17 Aug 2026: aligning its draft rules with the SEC's and gathering issuer feedback. [^pse-analyst-briefing-1h-2026:10]
- [P] GPDRs (peso receipts on foreign-listed securities, economic not voting interest): PSE rules consulted 26 Sep 2024; submitted to SEC Jan 2025; revised rules submitted 24 Jun 2026, approval "targeted within the quarter"; first issuer targeted 2H 2026. [^pse-cn-2024-0047:1] [^pse-annual-report-2025:38] [^pse-analyst-briefing-1h-2026:10]  Not a hedge for PH equities.
- [S] **EPHE** (iShares MSCI Philippines ETF, tracks MSCI Philippines IMI 25/50): AUM about US$132.4m, expense ratio 0.59%, 40 holdings (largest ICT 22.7%, BDO 9.9%), average volume about 140k shares/day, inception 28 Sep 2010 (data page dated 6 Oct 2026). [^stockanalysis-ephe]
- [S] **PLDT ADR** (NYSE: PHI): market cap about US$3.8bn, average volume about 234k shares, close US$18.15 on 5 Oct 2026. [^stockanalysis-phi]
- [S/I] **Listed options**: Cboe's options symbol directory (5,339 lines, downloaded 6 Oct 2026) lists classes for EWH, EWM, EWS, EWT, EWY, THD and EEM but **no EPHE and no PHI**. [^cboe-options-symbol-directory]
- [P] Foreign ownership limits (general 40%) and the FX linkage rule shape any synthetic exposure. [^msci-accessibility-review-2026:43]

### Inferences
- [I] No onshore index future before 2027 at the earliest: rules unfinished, funding being sought, vendor selection after the July RFI, and the Eqlipse engine itself only goes live on 23 Nov 2026.
- [I] Practical hedges today: (a) short EPHE (liquid enough for small books only; ICT concentration 22.7% means it hedges ICT-heavy beta); (b) PHI ADR short/hedge for TEL exposure only; (c) OTC total-return/ index swaps with offshore banks that hedge by buying/selling PSE shares (no public data on P-note/swap size - not verified); (d) onshore SBL short in the 52 eligibles when the pathway opens.

### Execution implications
- Basis/ tracking risk: EPHE holds 40 names with large ICT weight; hedge ratios vs PSEi must be re-estimated; US hours do not overlap PSE hours, so overnight gap risk.
- Synthetic positions via swaps do not touch PSE short-selling rules, but the dealer's hedge trades do (uptick, SIR caps), so dealer capacity can vanish in stress.
- Plan for the SEC structured-warrant regime (issuer P400m capital; one market maker per series) as a future onshore short-ish/hedging channel once adopted.

### Gaps
- Offshore index futures on the Philippines (none verified), EPHE options (none found; absence in Cboe directory only), P-note/swap volumes, other Philippine ADRs/GDRs, historic covered-warrant issuance.
- PSE derivatives launch date/SEC approval; GPDR approval outcome after 17 Aug 2026.

---

## Source catalog

```yaml
- slug: "pse-etf-rules"
  title: "PSE Rules on Exchange Traded Funds, Parts A-C (incl. ETF Market Making Rules and Implementing Guidelines)"
  publisher: "The Philippine Stock Exchange, Inc. (SEC-approved)"
  type: "pdf"
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2021/04/PSE-ETF-RULES-A-B-C-for-Website.pdf"
  local_path: "pdfs/pse-etf-rules.pdf"
  edition: "in-force"
  amended_through: "2013-03-18"
  note: "Cover says \"SEC Approved PSE ETF Rules March 18, 2013\"; proposed 2026 amendments (CN-2026-0029) not adopted as of 6 Oct 2026."
- slug: "pse-cn-2026-0026"
  title: "PSE Memorandum CN-2026-0026 - Invitation to submit comments on amendments to the PSE Market Making Rules (Annex A draft)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: "pdf"
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2026-0026.pdf"
  local_path: "pdfs/pse-cn-2026-0026.pdf"
  edition: "n/a"
  amended_through: "2026-06-03"
  note: "Scanned; OCR-read. Proposed (not in force) rules; comments closed 23 Jun 2026; processing-fee figure ambiguous in OCR."
- slug: "pse-cn-2026-0039-sec-market-making-rfc"
  title: "PSE memo CN-2026-0039 (20 Aug 2026) with SEC notice and draft \"SEC Rules on Market Making\""
  publisher: "The Philippine Stock Exchange, Inc. / Securities and Exchange Commission"
  type: "pdf"
  canonical_url: "https://www.pse.com.ph/ (PSE circular CN-2026-0039; CircularOPSPDF path returned 404; archived copy supplied by another researcher)"
  local_path: "pdfs/pse-cn-2026-0039-sec-market-making-rfc.pdf"
  edition: "n/a"
  amended_through: "2026-08-20"
  note: "SEC exposure draft (En Banc 13 Aug 2026; comments to 28 Aug 2026); not adopted as of 6 Oct 2026."
- slug: "pse-cn-2026-0029-etf-amend-consult"
  title: "PSE CN-2026-0029 - Proposed amendments to PSE Rules on ETFs (consultation paper)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: "pdf"
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2026-0029.pdf"
  local_path: "pdfs/pse-cn-2026-0029-etf-amend-consult.pdf"
  edition: "n/a"
  amended_through: "2026-06-16"
  note: "Scanned; OCR-read. Draft; comments to 30 Jun 2026."
- slug: "pse-sr11-etf-rules-2026"
  title: "PSE Supplemental Rule 11 - Rules on Exchange Traded Funds (CN-2013-0010; includes SEC ETF Rules annex)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: "pdf"
  canonical_url: "https://www.pse.com.ph/ (Supplemental Rules; archived by another researcher)"
  local_path: "pdfs/pse-sr11-etf-rules-2026.pdf"
  edition: "in-force"
  amended_through: "2013-03-18"
  note: "Same text as pse-etf-rules; used only to identify the rule as Supplemental Rule 11."
- slug: "sec-etf-rules"
  title: "SEC Memorandum Circular No. 10, series of 2012 - Rules and Regulations on Exchange Traded Funds"
  publisher: "Securities and Exchange Commission"
  type: "pdf"
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2021/04/SEC-ETF-Rules.pdf"
  local_path: "pdfs/sec-etf-rules.pdf"
  edition: "in-force"
  amended_through: "undated"
  note: "Series of 2012 (exact date not in text layer); s.5(14) market maker definition, s.8(2) two APs / one market maker."
- slug: "pse-eod-daily-quotation-2026-10-02"
  title: "PSE Daily Quotation Report, 2 October 2026"
  publisher: "The Philippine Stock Exchange, Inc."
  type: "pdf"
  canonical_url: "https://www.pse.com.ph/market-report/"
  local_path: "pdfs/pse-eod-daily-quotation-2026-10-02.pdf"
  edition: "historical"
  amended_through: "2026-10-02"
  note: "End-of-day quotes with bid/ask, OHLC, volume, value, net foreign; archived by another researcher; FMETF on p.9, BDO on p.1."
- slug: "ra-8799-src"
  title: "Republic Act No. 8799 - The Securities Regulation Code (full text)"
  publisher: "Republic of the Philippines"
  type: "pdf"
  canonical_url: "https://www.sec.gov.ph/ (SRC text; copy archived by another researcher)"
  local_path: "pdfs/ra-8799-src.pdf"
  edition: "in-force"
  amended_through: "undated"
  note: "Section 48.1 margin credit standard on p.50."
- slug: "pse-etf-market-maker-renewal-checklist"
  title: "ETF Market Maker Application/Renewal Checklist"
  publisher: "The Philippine Stock Exchange, Inc."
  type: "pdf"
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2022/03/ETF-Market-Maker-Application-Renewal-Checklist.pdf"
  local_path: "pdfs/pse-etf-market-maker-renewal-checklist.pdf"
  edition: "in-force"
  amended_through: "undated"
  note: "Posted 2022-03 on PSE site; lists 5-year operating history requirement."
- slug: "pse-revised-trading-rules"
  title: "PSE Revised Trading Rules (memo No. 2010-0275 edition; scanned)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: "pdf"
  canonical_url: "https://www.pse.com.ph/ (Consolidated Rules - Trading; file archived by another researcher)"
  local_path: "pdfs/pse-revised-trading-rules.pdf"
  edition: "historical"
  amended_through: "undated"
  note: "2010 edition (PSE presentation says Revised Trading Rules published 8 Jun 2010); later amended; short-selling s.5 still cross-referenced by the Oct 2023 Guidelines. OCR-read."
- slug: "pse-trading-rules-art-iv-sec-5-short-selling"
  title: "Revised Trading Rules, Article IV Section 5 (Short Selling) excerpt"
  publisher: "The Philippine Stock Exchange, Inc."
  type: "pdf"
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2021/01/Short-Selling_02_RulesRegulations_PSE_Revised-Trading-Rules-Article-IV-Section-5.pdf"
  local_path: "pdfs/pse-trading-rules-art-iv-sec-5-short-selling.pdf"
  edition: "in-force"
  amended_through: "undated"
  note: "Scanned excerpt posted on PSE SBL/Short Selling rules page."
- slug: "pse-short-selling-guidelines-2023-10"
  title: "PSE Guidelines on Short Selling Transactions (as of October 2023)"
  publisher: "The Philippine Stock Exchange, Inc. (with SEC sign-off)"
  type: "pdf"
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2024/05/PSE-Guidelines-on-Short-Selling-Transactions_Oct2023_v3.pdf"
  local_path: "pdfs/pse-short-selling-guidelines-2023-10.pdf"
  edition: "in-force"
  amended_through: "2023-10-16"
  note: "Eligible-securities clause \"revised October 16, 2023\"; archived by another researcher (identical to Oct2023_v3 file)."
- slug: "pse-short-selling-guidelines"
  title: "PSE Guidelines on Short Selling Transactions (as of January 2019)"
  publisher: "The Philippine Stock Exchange, Inc. (with SEC sign-off)"
  type: "pdf"
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2021/01/Short_Selling_02_Rules_Regulations_PSE_Guidelines_for_Short_Selling_Transactions_rev_Jan2019.pdf"
  local_path: "pdfs/pse-short-selling-guidelines.pdf"
  edition: "superseded"
  amended_through: "2019-01-22"
  note: "Eligible = PSEi + ETFs only; superseded by Oct 2023 text."
- slug: "pse-cn-2023-0048"
  title: "PSE CN-2023-0048 - Regulatory framework for SBL and short selling transactions"
  publisher: "The Philippine Stock Exchange, Inc."
  type: "pdf"
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2023-0048.pdf"
  local_path: "pdfs/pse-cn-2023-0048.pdf"
  edition: "n/a"
  amended_through: "2023-10-02"
  note: "Guidelines effective 2 Oct 2023; GMSLA/BIR letter; offshore collateral."
- slug: "pse-cn-2023-0056"
  title: "PSE CN-2023-0056 - Short Selling Program go-live (6 Nov 2023)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: "pdf"
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2023-0056.pdf"
  local_path: "pdfs/pse-cn-2023-0056.pdf"
  edition: "n/a"
  amended_through: "2023-10-19"
  note: "FEOMS re-certification; DSSR publication."
- slug: "pse-cn-2023-0053"
  title: "PSE CN-2023-0053 - Regulatory requirements for SBL (SLAA/MSLA/PDTC lending agency service)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: "pdf"
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2023/11/CN-2023-0053.pdf"
  local_path: "pdfs/pse-cn-2023-0053.pdf"
  edition: "n/a"
  amended_through: "2023-10-11"
  note: "n/a"
- slug: "pse-dssr-2023-11-06"
  title: "PSE Daily Short Selling Report, 6 Nov 2023 (go-live day)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: "pdf"
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2023/11/November-06-2023.pdf"
  local_path: "pdfs/pse-dssr-2023-11-06.pdf"
  edition: "historical"
  amended_through: "2023-11-06"
  note: "Original is AES-encrypted (no password); archived copy is a decrypted re-save, content unchanged."
- slug: "pse-dssr-2026-10-05"
  title: "PSE Daily Short Selling Report, 5 Oct 2026"
  publisher: "The Philippine Stock Exchange, Inc."
  type: "pdf"
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2026/10/October-05-2026.pdf"
  local_path: "pdfs/pse-dssr-2026-10-05.pdf"
  edition: "in-force"
  amended_through: "2026-10-05"
  note: "Decrypted re-save. All 707 distinct DSSR files (6 Nov 2023 - 5 Oct 2026) were parsed in a scratch directory; each reports TOTAL VOLUME 0."
- slug: "pse-market-reports-dssr"
  title: "PSE Market Reports page (index of 710 Daily Short Sell Report entries)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: "web"
  canonical_url: "https://www.pse.com.ph/market-report/"
  local_path: null
  edition: "in-force"
  amended_through: "2026-10-05"
  note: "Table retrieved through the site's own table endpoint; category \"Daily Short Sell Report\"."
- slug: "pse-short-selling-eligible-list"
  title: "List of Short Selling Eligible Securities (live frame, \"As of October 05, 2026\")"
  publisher: "The Philippine Stock Exchange, Inc."
  type: "web"
  canonical_url: "https://frames.pse.com.ph/eligible"
  local_path: null
  edition: "in-force"
  amended_through: "2026-10-05"
  note: "Snapshot fetched 6 Oct 2026; 52 securities."
- slug: "pse-sbl-short-selling-page"
  title: "PSE SBL & Short Selling page (overview, FAQs, document index)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: "web"
  canonical_url: "https://www.pse.com.ph/sbl-short-selling/"
  local_path: null
  edition: "in-force"
  amended_through: "undated"
  note: "FAQ gives uptick-rule example and barred phases (pre-open, pre-close, run-off/TAL); still quotes T+3 recall (outdated)."
- slug: "pse-etf-page"
  title: "PSE Exchange Traded Fund page (ETF Participants table)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: "web"
  canonical_url: "https://www.pse.com.ph/exchange-traded-fund/"
  local_path: null
  edition: "in-force"
  amended_through: "2026-10-06"
  note: "Crawled 6 Oct 2026; FMETF market maker and authorized participant = First Metro Securities Brokerage Corp."
- slug: "pse-press-2026-06-04-market-making"
  title: "PSE releases amendments to market making rules for public comment"
  publisher: "The Philippine Stock Exchange, Inc. (press release)"
  type: "web"
  canonical_url: "https://www.pse.com.ph/pse-releases-amendments-to-market-making-rules-for-public-comment/"
  local_path: null
  edition: "n/a"
  amended_through: "2026-06-04"
  note: "n/a"
- slug: "pse-press-2026-06-15-reforms"
  title: "PSE to introduce additional regulatory reforms"
  publisher: "The Philippine Stock Exchange, Inc. (press release)"
  type: "web"
  canonical_url: "https://www.pse.com.ph/pse-to-introduce-additional-regulatory-reforms/"
  local_path: null
  edition: "n/a"
  amended_through: "2026-06-15"
  note: "States SBL directed-pooled-lending rules submitted to SEC 16 Apr 2026."
- slug: "pse-press-feed"
  title: "PSE press-room RSS feed (10 latest items, newest 2 Oct 2026)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: "web"
  canonical_url: "https://www.pse.com.ph/feed/"
  local_path: null
  edition: "in-force"
  amended_through: "2026-10-02"
  note: "Used for the absence-of-news check."
- slug: "pse-cn-2026-0009"
  title: "PSE CN-2026-0009 - Proposed amendments to PSE Rules on SBL and rationalization of SBL reports"
  publisher: "The Philippine Stock Exchange, Inc."
  type: "pdf"
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2026-0009.pdf"
  local_path: "pdfs/pse-cn-2026-0009.pdf"
  edition: "n/a"
  amended_through: "2026-02-03"
  note: "Consultation paper + Annex B revised SBL rules (draft); comments to 18 Feb 2026."
- slug: "pse-cn-2026-0022"
  title: "PSE CN-2026-0022 - Updates on PDTC Lending Agency Service for the PSE SBL Program (with PDS memo 03-2026)"
  publisher: "The Philippine Stock Exchange, Inc. / PDS Group"
  type: "pdf"
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2026-0022.pdf"
  local_path: "pdfs/pse-cn-2026-0022.pdf"
  edition: "in-force"
  amended_through: "2026-05-18"
  note: "Scanned; OCR-read. PDS memo dated 22 Apr 2026."
- slug: "pse-cn-2026-0025"
  title: "PSE CN-2026-0025 - 2026 Revised Guidelines for MSLA Clearance (SEC-approved 15 May 2026)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: "pdf"
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2026-0025.pdf"
  local_path: "pdfs/pse-cn-2026-0025.pdf"
  edition: "in-force"
  amended_through: "2026-05-22"
  note: "Scanned; OCR-read."
- slug: "pse-msla-clearance-guidelines-2026"
  title: "PSE 2026 Revised Guidelines for MSLA Clearance"
  publisher: "The Philippine Stock Exchange, Inc."
  type: "pdf"
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2026/05/2026-Revised-Guidelines-for-MSLA-Clearance_SEC-approved.pdf"
  local_path: "pdfs/pse-msla-clearance-guidelines-2026.pdf"
  edition: "in-force"
  amended_through: "2026-05-15"
  note: "SEC-approved date from CN-2026-0025."
- slug: "pse-cn-2024-0035"
  title: "PSE CN-2024-0035 - Amendments to BIR Revenue Regulations on SBL (attaches BIR RR 10-2024 dated 5 Jun 2024)"
  publisher: "The Philippine Stock Exchange, Inc. / Bureau of Internal Revenue"
  type: "pdf"
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2024-0035.pdf"
  local_path: "pdfs/pse-cn-2024-0035.pdf"
  edition: "in-force"
  amended_through: "2024-06-05"
  note: "Annex A (pp.3-9) is scanned RR 10-2024; OCR-read."
- slug: "bir-rr-10-2006-sbl"
  title: "BIR Revenue Regulations No. 10-2006 - Tax treatment of SBL transactions"
  publisher: "Bureau of Internal Revenue / Department of Finance"
  type: "pdf"
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2021/01/SBL_02_RulesRegulations_BIR_RR-No.-10-2006.pdf"
  local_path: "pdfs/bir-rr-10-2006-sbl.pdf"
  edition: "in-force"
  amended_through: "2006-06-23"
  note: "As amended by RR 1-2008 and RR 10-2024."
- slug: "bir-rr-1-2008-sbl"
  title: "BIR Revenue Regulations No. 1-2008 - amending RR 10-2006 (multilateral MSLA, registration)"
  publisher: "Bureau of Internal Revenue / Department of Finance"
  type: "pdf"
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2021/01/SBL_02_RulesRegulations_BIR_RR-No.-1-2008.pdf"
  local_path: "pdfs/bir-rr-1-2008-sbl.pdf"
  edition: "in-force"
  amended_through: "2008-02-01"
  note: "n/a"
- slug: "bir-rr-20-2025-stt"
  title: "BIR Revenue Regulations No. 20-2025 - Stock transaction tax rate (0.1%) under CMEPA"
  publisher: "Bureau of Internal Revenue"
  type: "pdf"
  canonical_url: "https://www.bir.gov.ph/ (RR 20-2025; archived by another researcher)"
  local_path: "pdfs/bir-rr-20-2025-stt.pdf"
  edition: "in-force"
  amended_through: "2025-08-05"
  note: "Scanned; OCR-read. Effective for sales from 1 Jul 2025."
- slug: "bir-rr-19-2025-dst"
  title: "BIR Revenue Regulations No. 19-2025 - Documentary stamp tax under CMEPA"
  publisher: "Bureau of Internal Revenue"
  type: "pdf"
  canonical_url: "https://www.bir.gov.ph/ (RR 19-2025; archived by another researcher)"
  local_path: "pdfs/bir-rr-19-2025-dst.pdf"
  edition: "in-force"
  amended_through: "2025-08-05"
  note: "Scanned; OCR-read. s.199(e) exempts sale of listed shares."
- slug: "sec-mc-7-2006-sbl-rules"
  title: "SEC Memorandum Circular No. 7, s.2006 - Rules on Securities Borrowing and Lending"
  publisher: "Securities and Exchange Commission"
  type: "pdf"
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2021/01/SBL_02_RulesRegulations_SEC_MC-No.-7-2006-SBL-Rules.pdf"
  local_path: "pdfs/sec-mc-7-2006-sbl-rules.pdf"
  edition: "in-force"
  amended_through: "2006-06-09"
  note: "n/a"
- slug: "pse-sbl-rules"
  title: "PSE Rules on Securities Borrowing and Lending (Part 1 of PSE Rules and Guidelines on SBL)"
  publisher: "The Philippine Stock Exchange, Inc. (SEC-approved)"
  type: "pdf"
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2021/01/SBL_02_RulesRegulations_PSE_SBL-Rules.pdf"
  local_path: "pdfs/pse-sbl-rules.pdf"
  edition: "in-force"
  amended_through: "2006-11-16"
  note: "Scanned; OCR-read. Date from PSE milestones slide (SEC approval 16 Nov 2006; effective 15 Feb 2007). Revised draft pending (CN-2026-0009)."
- slug: "pse-sbl-guidelines"
  title: "PSE Guidelines on Securities Borrowing & Lending"
  publisher: "The Philippine Stock Exchange, Inc."
  type: "pdf"
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2021/01/SBL_02_RulesRegulations_PSE_SBL-Guidelines.pdf"
  local_path: "pdfs/pse-sbl-guidelines.pdf"
  edition: "in-force"
  amended_through: "undated"
  note: "Companion to the PSE SBL Rules (issued 5 Feb 2007 per PSE milestones slide); text layer present."
- slug: "ra-12214-cmepa"
  title: "Republic Act No. 12214 - Capital Markets Efficiency Promotion Act (CMEPA)"
  publisher: "Republic of the Philippines"
  type: "pdf"
  canonical_url: "https://www.officialgazette.gov.ph/ (RA 12214; copy archived by another researcher)"
  local_path: "pdfs/ra-12214-cmepa.pdf"
  edition: "in-force"
  amended_through: "undated"
  note: "p.16 amends Tax Code s.127 (STT 1/10 of 1%, dealer-in-securities carve-out); effective 1 Jul 2025 per BIR RR 20-2025."
- slug: "pse-sbl-models-2023"
  title: "Securities Borrowing and Lending Models (domestic process flows)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: "pdf"
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2023/08/SBL-Models-2023-FINAL-jgg-mvv.pdf"
  local_path: "pdfs/pse-sbl-models-2023.pdf"
  edition: "in-force"
  amended_through: "2023-08"
  note: "Date from upload path."
- slug: "pse-sbl-short-selling-intro-presentation"
  title: "An Introduction to the PSE SBL and Short Selling Programs (Nov 2018)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: "pdf"
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2021/01/Presentation_Introduction-to-the-PSE-SBL-and-Short-Selling-Programs.pdf"
  local_path: "pdfs/pse-sbl-short-selling-intro-presentation.pdf"
  edition: "historical"
  amended_through: "2018-11"
  note: "Source of the 2006-2018 milestone dates."
- slug: "pse-sbl-short-selling-webinar-2023"
  title: "PSE's SBL and Short Selling Programs - webinar deck for retail investors (Oct 2023)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: "pdf"
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2023/10/SBL-and-Short-Selling-Webinar-for-Retail-Investors-jgg.pdf"
  local_path: "pdfs/pse-sbl-short-selling-webinar-2023.pdf"
  edition: "historical"
  amended_through: "2023-10-06"
  note: "Contains 21 Jul 2023 PDTC conditional approval."
- slug: "pse-tpa-2023-0031"
  title: "PSE TPA 2023-0031 - Updated reporting of SBL transactions for short-selling (DDPR v1.7)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: "pdf"
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2023/11/TPA_2023-0031.pdf"
  local_path: "pdfs/pse-tpa-2023-0031.pdf"
  edition: "in-force"
  amended_through: "2023-07-14"
  note: "n/a"
- slug: "cmic-sbl-short-selling-guidelines"
  title: "CMIC Implementing Guidelines on SBL and Short Selling (Memo 2020-005)"
  publisher: "Capital Markets Integrity Corporation (SEC-approved)"
  type: "pdf"
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2021/01/SBL_02_RulesRegulations_CMIC_Guidelines-on-SBL-and-Short-Selling.pdf"
  local_path: "pdfs/cmic-sbl-short-selling-guidelines.pdf"
  edition: "in-force"
  amended_through: "2020-02-10"
  note: "Effective 25 Feb 2020; scanned; OCR-read. Eligible-securities clause there (PSEi + ETFs) predates Oct 2023 expansion."
- slug: "ic-cl-2019-45-sbl"
  title: "Insurance Commission Circular Letter - Amended guidelines for SBL transactions of insurers"
  publisher: "Insurance Commission"
  type: "pdf"
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2021/01/SBL_02_Rules_Regulations_IC_CL_No_2019-45.pdf"
  local_path: "pdfs/ic-cl-2019-45-sbl.pdf"
  edition: "in-force"
  amended_through: "undated"
  note: "Printed date in the file reads \"04 September 20[18/19]\" (text-layer OCR); number per PSE file name."
- slug: "sec-2015-src-irr"
  title: "2015 Implementing Rules and Regulations of the Securities Regulation Code (full text)"
  publisher: "Securities and Exchange Commission"
  type: "pdf"
  canonical_url: "https://appointment.sec.gov.ph/wp-content/uploads/2019/11/2015IRR_RA9799.pdf"
  local_path: "pdfs/sec-2015-src-irr.pdf"
  edition: "in-force"
  amended_through: "2015-11-09"
  note: "Effectivity 9 Nov 2015; Rules 24.2-2 (pp.70-71), 25 (p.72), 48.1 (p.165). Pending SEC amendments (Rule 48.1 draft; Rules 28.1/33.1 draft of 24 Sep 2026) not yet adopted."
- slug: "sec-rfq-2026-src-rule-48-1-margin"
  title: "SEC Notice and draft MC - Proposed amendments to Rule 48.1 (Margin), 2015 SRC Rules"
  publisher: "Securities and Exchange Commission"
  type: "pdf"
  canonical_url: "https://cruzmarcelo.com/wp-content/uploads/2026/09/2026RFQ_Proposed-Amendments-to-SRC-Rule-48.1.pdf"
  local_path: "pdfs/sec-rfq-2026-src-rule-48-1-margin.pdf"
  edition: "n/a"
  amended_through: "2026-08-25"
  note: "Exposure draft; comments to 15 Sep 2026; copy hosted by Cruz Marcelo & Tenefrancia."
- slug: "cruzmarcelo-2026-09-09-margin"
  title: "SEC Proposes New Margin Financing Framework For Broker-Dealers"
  publisher: "Cruz Marcelo & Tenefrancia"
  type: "web"
  canonical_url: "https://cruzmarcelo.com/?p=23121"
  local_path: null
  edition: "n/a"
  amended_through: "2026-09-09"
  note: "Secondary summary of the draft."
- slug: "firstmetrosec-margin-trading-agreement-v072026"
  title: "First Metro Securities Brokerage Corp. - Margin Trading Agreement (v072026) with Annex A marginable securities"
  publisher: "First Metro Securities Brokerage Corporation"
  type: "pdf"
  canonical_url: "https://help.firstmetrosec.com.ph/hc/article_attachments/60732981574425"
  local_path: "pdfs/firstmetrosec-margin-trading-agreement-v072026.pdf"
  edition: "in-force"
  amended_through: "2026-07"
  note: "Broker house terms; version tag v072026."
- slug: "pse-analyst-briefing-1h-2026"
  title: "PSE STAR Briefing - 1H 2026 Updates (17 Aug 2026)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: "pdf"
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/4/2026/08/2026.08.17-PSE-STAR-1H-2026.pdf"
  local_path: "pdfs/pse-analyst-briefing-1h-2026.pdf"
  edition: "in-force"
  amended_through: "2026-08-17"
  note: "Latest PSE status on SBL, market making, GPDR, derivatives, structured warrants."
- slug: "pse-analyst-briefing-3m-2026"
  title: "PSE Overview / 3M 2026 Analyst Briefing (18 Mar 2026)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: "pdf"
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/4/2026/07/3M-2026-PSE-Analyst-Briefing.pdf"
  local_path: "pdfs/pse-analyst-briefing-3m-2026.pdf"
  edition: "historical"
  amended_through: "2026-03-18"
  note: "n/a"
- slug: "pse-asm-2026-president-report"
  title: "President's Report, Annual Stockholders' Meeting (4 Jul 2026)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: "pdf"
  canonical_url: "https://documents.pse.com.ph/ (ASM 2026 President's Report; archived by another researcher)"
  local_path: "pdfs/pse-asm-2026-president-report.pdf"
  edition: "in-force"
  amended_through: "2026-07-04"
  note: "n/a"
- slug: "pse-asm-2025-presidents-report"
  title: "President's Report, Annual Stockholders' Meeting 2025"
  publisher: "The Philippine Stock Exchange, Inc."
  type: "pdf"
  canonical_url: "https://documents.pse.com.ph/ (archived by another researcher)"
  local_path: "pdfs/pse-asm-2025-presidents-report.pdf"
  edition: "historical"
  amended_through: "2025-07-12"
  note: "n/a"
- slug: "pse-asm-2024-presidents-report"
  title: "President's Report, Annual Stockholders' Meeting 2024"
  publisher: "The Philippine Stock Exchange, Inc."
  type: "pdf"
  canonical_url: "https://documents.pse.com.ph/ (archived by another researcher)"
  local_path: "pdfs/pse-asm-2024-presidents-report.pdf"
  edition: "historical"
  amended_through: "2024-07-06"
  note: "Source of \"Derivatives - Target launch 2026\"."
- slug: "pse-annual-report-2025"
  title: "PSE Annual Report 2025"
  publisher: "The Philippine Stock Exchange, Inc."
  type: "pdf"
  canonical_url: "https://documents.pse.com.ph/ (archived by another researcher)"
  local_path: "pdfs/pse-annual-report-2025.pdf"
  edition: "in-force"
  amended_through: "undated"
  note: "States derivatives rules \"slated to be finalized in 2H 2026\"."
- slug: "pse-cn-2026-0018"
  title: "PSE CN-2026-0018 - Request for comments on SEC's proposed regulations for structured warrants"
  publisher: "The Philippine Stock Exchange, Inc. / SEC"
  type: "pdf"
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2026-0018.pdf"
  local_path: "pdfs/pse-cn-2026-0018.pdf"
  edition: "n/a"
  amended_through: "2026-04-30"
  note: "Scanned; OCR-read. SEC draft (En Banc 28 Apr 2026)."
- slug: "pse-cn-2024-0047"
  title: "PSE CN-2024-0047 - Proposed rules for Global Philippine Depositary Receipts"
  publisher: "The Philippine Stock Exchange, Inc."
  type: "pdf"
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2024-0047.pdf"
  local_path: "pdfs/pse-cn-2024-0047.pdf"
  edition: "historical"
  amended_through: "2024-09-26"
  note: "Consultation draft."
- slug: "pse-nte-broker-forum-2026-07-09"
  title: "PSE new trading engine - Broker Forum (9 Jul 2026)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: "pdf"
  canonical_url: "https://documents.pse.com.ph/ (archived by another researcher)"
  local_path: "pdfs/pse-nte-broker-forum-2026-07-09.pdf"
  edition: "in-force"
  amended_through: "2026-07-09"
  note: "Go-live 23 Nov 2026."
- slug: "pse-nte-faq-2026-08"
  title: "PSE New Trading Engine FAQ (Aug 2026)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: "pdf"
  canonical_url: "https://documents.pse.com.ph/ (archived by another researcher)"
  local_path: "pdfs/pse-nte-faq-2026-08.pdf"
  edition: "in-force"
  amended_through: "2026-08"
  note: "Odd-lot market abolished with lot size 1."
- slug: "sec-2015-src-irr-notice-of-effectivity"
  title: "SEC Notice - Effectivity of the 2015 SRC Rules on 9 November 2015"
  publisher: "Securities and Exchange Commission"
  type: "pdf"
  canonical_url: "https://appointment.sec.gov.ph/wp-content/uploads/2019/11/2015-SRC-Rules-Notice-of-Effectivity-of-SRC-IRR-Nov-09-2015.pdf"
  local_path: "pdfs/sec-2015-src-irr-notice-of-effectivity.pdf"
  edition: "in-force"
  amended_through: "2015-11-05"
  note: "Notice dated 5 Nov 2015; rules effective 9 Nov 2015 after publication on 25 Oct 2015; archived by another researcher."
- slug: "pse-memo-2026-10-01-sec-rfc-src-28-1-33-1-capital"
  title: "PSE memo (1 Oct 2026) - SEC request for comments on Rules 28.1 and 33.1 (broker-dealer minimum capital, surety bond)"
  publisher: "The Philippine Stock Exchange, Inc. / Securities and Exchange Commission"
  type: "pdf"
  canonical_url: "https://www.pse.com.ph/ (PSE memo dated 1 Oct 2026; archived by another researcher)"
  local_path: "pdfs/pse-memo-2026-10-01-sec-rfc-src-28-1-33-1-capital.pdf"
  edition: "n/a"
  amended_through: "2026-10-01"
  note: "SEC En Banc exposure draft of 24 Sep 2026; comments to 14 Oct 2026; context for market-maker and margin-lender capital tests (existing broker-dealer capital P100m)."
- slug: "pse-cn-2025-0032-bir-stt-advisory"
  title: "PSE CN-2025-0032 - BIR tax advisory on manual payment of the revised stock transaction tax (CMEPA)"
  publisher: "The Philippine Stock Exchange, Inc."
  type: "pdf"
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2025-0032.pdf"
  local_path: "pdfs/pse-cn-2025-0032-bir-stt-advisory.pdf"
  edition: "in-force"
  amended_through: "2025-07-15"
  note: "Archived by another researcher; confirms revised STT = 1/10 of 1%."
- slug: "pse-cn-2023-0031-t2-settlement"
  title: "PSE CN-2023-0031 - T+2 settlement"
  publisher: "The Philippine Stock Exchange, Inc."
  type: "pdf"
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2023-0031.pdf"
  local_path: "pdfs/pse-cn-2023-0031-t2-settlement.pdf"
  edition: "in-force"
  amended_through: "undated"
  note: "Archived by another researcher; used only to note the T+2 cycle."
- slug: "pse-itch-equities-feed-spec-v2-3"
  title: "PSE Equities Feed Specification for X-stream (ITCH) v2.3"
  publisher: "The Philippine Stock Exchange, Inc. / OMX"
  type: "pdf"
  canonical_url: "https://documents.pse.com.ph/ (archived by another researcher)"
  local_path: "pdfs/pse-itch-equities-feed-spec-v2-3.pdf"
  edition: "historical"
  amended_through: "2015-03"
  note: "Pre-Eqlipse feed; broker-anonymity switch and Short Sell Eligible flag."
- slug: "pse-fix-specification-v2-5"
  title: "PSE FIX Specification for X-stream v2.5"
  publisher: "The Philippine Stock Exchange, Inc. / OMX"
  type: "pdf"
  canonical_url: "https://documents.pse.com.ph/ (archived by another researcher)"
  local_path: "pdfs/pse-fix-specification-v2-5.pdf"
  edition: "historical"
  amended_through: "2015-08-10"
  note: "Pre-Eqlipse order-entry spec; Side 5 = Short Sell."
- slug: "msci-accessibility-review-2026"
  title: "MSCI 2026 Global Market Accessibility Review (June 2026)"
  publisher: "MSCI Inc."
  type: "pdf"
  canonical_url: "https://www.msci.com/ (archived by another researcher)"
  local_path: "pdfs/msci-accessibility-review-2026.pdf"
  edition: "in-force"
  amended_through: "2026-06"
  note: "Philippines section on p.43."
- slug: "bsp-circular-611"
  title: "BSP Circular No. 611 (30 May 2008) - SBL involving foreign borrowers of PSE-listed shares"
  publisher: "Bangko Sentral ng Pilipinas (text via Supreme Court E-Library)"
  type: "web"
  canonical_url: "https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/10/54361"
  local_path: null
  edition: "in-force"
  amended_through: "2008-05-30"
  note: "Still referenced by PSE as the FX rule for foreign SBL participants; later BSP changes not checked."
- slug: "bsp-circular-432"
  title: "BSP Circular No. 432 (14 May 2004) - blue-chip stock collateral and own-share acceptance by banks"
  publisher: "Bangko Sentral ng Pilipinas (text via Supreme Court E-Library)"
  type: "web"
  canonical_url: "https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/10/45890"
  local_path: null
  edition: "in-force"
  amended_through: "2004-05-14"
  note: "Amends MORB X313.b, X322.2, X326.1k(5)."
- slug: "philstar-2026-07-02-short-selling"
  title: "PSE clears regulatory hurdles to short selling"
  publisher: "The Philippine Star"
  type: "web"
  canonical_url: "https://www.philstar.com/business/2026/07/02/2539152/pse-clears-regulatory-hurdles-short-selling"
  local_path: null
  edition: "n/a"
  amended_through: "2026-07-02"
  note: "Secondary; SEC 6 May 2026 comments on revised SBL rules."
- slug: "philstar-2026-06-10-sbl-framework"
  title: "SEC streamlines securities borrowing, lending framework"
  publisher: "The Philippine Star"
  type: "web"
  canonical_url: "https://www.philstar.com/business/2026/06/10/2534005/sec-streamlines-securities-borrowing-lending-framework"
  local_path: null
  edition: "n/a"
  amended_through: "2026-06-10"
  note: "Secondary."
- slug: "gma-2023-10-20-short-selling-nov-6"
  title: "PSE to launch short selling program on Nov. 6"
  publisher: "GMA News"
  type: "web"
  canonical_url: "https://www.gmanetwork.com/news/money/companies/885794/pse-to-launch-short-selling-program-on-nov-6/story"
  local_path: null
  edition: "n/a"
  amended_through: "2023-10-20"
  note: "Secondary; 53 initial eligible securities."
- slug: "bworld-2024-02-06-short-selling-demand"
  title: "Philippine short selling in short demand 3 months after its launch"
  publisher: "BusinessWorld"
  type: "web"
  canonical_url: "https://www.bworldonline.com/top-stories/2024/02/06/573730/philippine-short-selling-in-short-demand-3-months-after-its-launch/"
  local_path: null
  edition: "n/a"
  amended_through: "2024-02-06"
  note: "Secondary (Bloomberg data); body retrieved via curl on 6 Oct 2026."
- slug: "bworld-2024-02-12-short-selling-recovery"
  title: "PSE: Short selling progress hinges on market recovery"
  publisher: "BusinessWorld"
  type: "web"
  canonical_url: "https://bworldonline.com/corporate/2024/02/12/574940/pse-short-selling-progress-hinges-on-market-recovery/"
  local_path: null
  edition: "n/a"
  amended_through: "2024-02-12"
  note: "Secondary; Monzon quotes on slow take-up."
- slug: "philstar-2024-02-19-merkado-barkada"
  title: "So can people do short-selling or not? (Merkado Barkada)"
  publisher: "The Philippine Star"
  type: "web"
  canonical_url: "https://www.philstar.com/business/stock-commentary/2024/02/19/2334314/so-can-people-do-short-selling-or-not"
  local_path: null
  edition: "n/a"
  amended_through: "2024-02-19"
  note: "Secondary commentary; points readers to the Daily Short Sell Report."
- slug: "pnl-law-cmic-guidelines-2020"
  title: "Securities Borrowing and Lending (SBL) and Short Selling in the Philippines: Implementing Guidelines"
  publisher: "PNL law blog"
  type: "web"
  canonical_url: "https://pnl-law.com/blog/?p=5701"
  local_path: null
  edition: "n/a"
  amended_through: "2020-05-03"
  note: "Secondary; gives SEC En Banc date 17 Dec 2019."
- slug: "stockanalysis-ephe"
  title: "iShares MSCI Philippines ETF (EPHE) data page"
  publisher: "StockAnalysis.com"
  type: "web"
  canonical_url: "https://stockanalysis.com/etf/ephe/"
  local_path: null
  edition: "n/a"
  amended_through: "2026-10-06"
  note: "Secondary data aggregator; AUM/holdings as shown on 6 Oct 2026."
- slug: "stockanalysis-phi"
  title: "PLDT Inc. ADR (NYSE: PHI) data page"
  publisher: "StockAnalysis.com"
  type: "web"
  canonical_url: "https://stockanalysis.com/stocks/phi/"
  local_path: null
  edition: "n/a"
  amended_through: "2026-10-06"
  note: "Secondary data aggregator."
- slug: "cboe-options-symbol-directory"
  title: "Cboe Options Symbol Directory (CSV download)"
  publisher: "Cboe Global Markets"
  type: "dataset"
  canonical_url: "https://www.cboe.com/us/options/symboldir/?download=csv"
  local_path: null
  edition: "in-force"
  amended_through: "2026-10-06"
  note: "5,339 lines retrieved 6 Oct 2026; no EPHE or PHI option class."
```
