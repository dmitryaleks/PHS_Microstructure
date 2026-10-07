---
number: 14
slug: foreign-access
title: Foreign Access and Ownership Limits
summary: Which PSE stocks foreigners may own (218 of 281 capped at 40%, 15 at 0%), how the cap is policed order by order, and the BSP registration, FX and index-provider facts that gate foreign flow.
part: Costs, rules and access
---

Foreign ownership on the PSE is limited **per company, in aggregate**, not per investor, and the binding quantity for a trading algorithm is not the statutory percentage but the **foreign room left** in each stock: the company's limit minus what foreigners already hold, minus what other foreign buyers have already earmarked. The archived Revised Trading Rules say the trading system "will earmark all valid foreign buying Orders", so a resting foreign bid consumes room when it is entered, not when it fills.[^pse-revised-trading-rules:17] A breach that does get through must be unwound the same day (or at the next open) at the prevailing market price, an execution risk with no price cap.[^pse-cn-2025-0035-sec-declassification-mandate:3]

Two facts break assumptions carried over from other venues. The 40% limit is the norm, not the exception: on PSE EDGE on 6 October 2026, 218 of 281 listed companies, holding about 93.5% of the market capitalisation shown, carry a 40% limit, including banks, telecoms and REITs, not just land-rich developers and utilities.[^pse-edge-stock-data] And there is **no separate foreign board or foreign price**: the old Class A / Class B share lines that once priced foreign access separately are being abolished by SEC rule, so access to a capped name is a single order book with a shares-available counter.[^pse-cn-2025-0035-sec-declassification-mandate:2]

## Legal framework

### The Constitution and the 60/40 rule

Foreign equity caps come from the 1987 Constitution and from statutes and executive orders layered on top of it.[^constitution-1987-lawphil]

| Provision | Rule |
|---|---|
| Art. XII Sec. 2 | Natural resources: co-production, joint-venture or production-sharing agreements only with Filipino citizens or corporations at least 60% Filipino-owned; large-scale minerals and petroleum through technical or financial assistance agreements with the President |
| Art. XII Sec. 7 | Private lands transferable only to those qualified to hold public-domain lands |
| Art. XII Sec. 10 | Congress may reserve investment areas to citizens or to corporations at least 60% Filipino-owned |
| Art. XII Sec. 11 | Public-utility franchises only to corporations at least 60% Filipino-owned; foreign participation in the governing body limited to its proportionate share of capital; executive and managing officers must be citizens |
| Art. XIV Sec. 4(2) | Schools at least 60% Filipino-owned, with control vested in citizens |
| Art. XVI Sec. 11 | Mass media wholly owned and managed by citizens; advertising at least 70% Filipino |

"Capital" in the 60/40 rule was settled by the Supreme Court in *Gamboa v. Teves*. The decision of 28 June 2011 read "capital" as shares entitled to vote in the election of directors; the resolution of 9 October 2012 denied the motions for reconsideration with finality and made the test stricter: the 60-40 requirement applies to each class of shares, voting or non-voting, mere legal title is insufficient, and "full beneficial ownership of 60 percent of the outstanding capital stock, coupled with 60 percent of the voting rights, is required".[^gamboa-v-teves-2012-lawphil] An issuer subject to Art. XII Sec. 11 therefore has to test each class of shares separately (inference from the ruling).

### RA 11647 and RA 11659 (2022)

- **RA 11647** (amending the Foreign Investments Act; approved 2 Mar 2022; effective 15 days after publication): non-Philippine nationals may invest up to **100%** of a domestic enterprise unless a law or the negative list limits it.[^ra-11647-foreign-investments-act-amendments:5] Micro and small domestic market enterprises with paid-in equity below US$200,000 are reserved to Philippine nationals; the threshold is US$100,000 if the enterprise involves advanced technology (DOST), is an endorsed startup or enabler, or directly employs at least 15 Filipinos. List B may be amended no more often than every two years.[^ra-11647-foreign-investments-act-amendments:6][^ra-11647-foreign-investments-act-amendments:8]
- **RA 11659** (amending the Public Service Act; approved 21 Mar 2022; effective 15 days after publication): "public utility" now means only distribution of electricity, transmission of electricity, petroleum and petroleum-product pipeline transmission systems, water pipeline distribution and wastewater (including sewerage) pipeline systems, seaports, and public utility vehicles, and "no other person shall be deemed a public utility unless otherwise subsequently provided by law".[^ra-11659-public-service-act-amendments:4] Section 25 adds a reciprocity clause: foreign nationals may not own more than **50%** of the capital of entities operating critical infrastructure unless their country grants reciprocity.[^ra-11659-public-service-act-amendments:13] Section 34 amends the foreign-ownership limits in the laws on BOT projects, domestic shipping, civil aviation, toll operation, transport network vehicles and the telecom public-utility classification (RA 7925), so telecoms, airlines, shipping and toll operators are no longer constitutional "public utilities".[^ra-11659-public-service-act-amendments:14] Two further provisions bear on institutional foreign holders: Sec. 23 lets the President, on national-security grounds, suspend or prohibit a merger, acquisition or investment in a public service that would give a foreigner control; and Sec. 24 bars entities controlled by or acting for a foreign government, or foreign state-owned enterprises, from owning capital in a public utility or critical infrastructure (for investments made after the Act), except that sovereign wealth funds and independent pension funds of each state may collectively own up to **30%** of the capital of such public services.[^ra-11659-public-service-act-amendments:12][^ra-11659-public-service-act-amendments:13]

### The 13th Regular Foreign Investment Negative List (EO 113, 13 April 2026)

EO 113 promulgates the **13th Regular Foreign Investment Negative List**, replacing the 12th (EO 175, 27 Jun 2022), which had replaced the 11th (EO 65, 29 Oct 2018).[^eo-113-2026-13th-finl:1][^eo-175-2022-12th-finl:1][^lawphil-eo-65-2018] Negative List A (limits set by the Constitution and specific laws) may be amended at any time; List B (security, health, morals and small enterprises) no more often than once every two years.[^eo-113-2026-13th-finl:1] The order takes effect 15 days after publication.[^eo-113-2026-13th-finl:2]

<div class="callout warn">
<span class="label">Effective date not verified</span>

The archived copy does not show the publication date. KPMG reports an effective date of 1 May 2026 (from a 16 April publication) and another report gives 2 May 2026.[^kpmg-2026-04-13th-finl] Treat the list as in force since early May 2026; the earlier 12th list governed until then. KPMG also reports the telecom, architecture, retail and materiel items as changes from the 12th list (secondary).
</div>

| Maximum foreign equity | Activities (13th list) | Basis cited in the order |
|---|---|---|
| **0%** | Mass media except recording; internet business; corporate practice of architecture; cooperatives; private security agencies; small-scale mining; marine resources; cockpits; nuclear, biological, chemical and radiological weapons and anti-personnel mines; firecrackers (List A items 1 to 10)[^eo-113-2026-13th-finl:3] | Const. Art. XVI Sec. 11(1); specific laws |
| **25%** | Private recruitment; defence-related construction contracts (items 11 and 12)[^eo-113-2026-13th-finl:3] | Labor Code Art. 27; CA 541 |
| **30%** | Advertising (item 13)[^eo-113-2026-13th-finl:4] | Const. Art. XVI Sec. 11(2) |
| **40%** | Retail trade below PHP 25m paid-up capital; natural resources (large-scale minerals and petroleum under President-signed agreements, and renewable energy, are excepted and open); ownership of private lands; **public utilities (the six categories)**; educational institutions (with exceptions); rice and corn; government procurement of goods, infrastructure (up to 75% where Filipino entities lack the technology) and consulting services; commercial fishing vessels; condominium units (items 14 to 24)[^eo-113-2026-13th-finl:4][^eo-113-2026-13th-finl:5] | Const. Art. XII Secs. 2, 7, 11 and Art. XIV Sec. 4(2); RA 11659 Sec. 4; RA 11595 |
| **40% (List B)** | PNP-regulated products; military materiel; dangerous drugs; sauna and massage; gambling; micro and small domestic market enterprises below US$200,000 paid-in (US$100,000 with exceptions)[^eo-113-2026-13th-finl:6][^eo-113-2026-13th-finl:7] | RA 7042 as amended by RA 11647; RA 12024 |
| **Up to 100%** (50% without reciprocity) | Operation and management of telecommunications (item 25)[^eo-113-2026-13th-finl:5] | RA 11659 Sec. 25; IRR Sec. 45 |

Foreign retailers are allowed with at least PHP 25m paid-up capital and PHP 10m per store, subject to reciprocity (RA 11595).[^eo-113-2026-13th-finl:4] Footnote 10 of the order restates the public-utility rule that foreign participation in the governing body is limited to its proportionate share of capital and that all executive and managing officers must be citizens.[^eo-113-2026-13th-finl:4] The list does not name banks or insurers; sector statutes govern them and were not retrieved, although EDGE shows 40% for listed banks (below). REITs that own Philippine land must observe foreign-ownership limits (RA 9856 Sec. 6).[^ra-9856-reit-act:9]

The negative list is the legal ceiling for a sector; what binds a trade is the **limit in each issuer's articles**, which can sit below the legal ceiling, and the practical record is the per-company data below.

### Execution implications

- Do not derive a stock's limit from the negative list. Take it from the issuer-level data below and re-pull it when an issuer amends its articles (telecoms and the Class A/B issuers are the live cases).
- For state-owned and sovereign investors, the public-utility and critical-infrastructure holdings are capped by the RA 11659 Sec. 24 regime (30% collectively for sovereign wealth and pension funds) in addition to the issuer's own limit; confirm the position with counsel before sizing in issuers in the six public-utility categories (electricity distribution and transmission, water and sewerage pipelines, petroleum pipelines, seaports and public utility vehicles).
- Check the effective date of any new negative list or amendment: List A may change at any time, List B no more often than every two years.

## The per-company limit in practice

PSE EDGE publishes a "Foreign Ownership Limit(%)" on each company's Stock Data page. Of the 284 company pages parsed on 6 Oct 2026 (each stamped "As of Oct 06, 2026"), 281 are used: the two foreign secondary listings (Manulife and Sun Life, limit 100%) and one page with no data (Asian Terminals, delisted in April 2026) are excluded. The counts and weights are computed from those pages, with market capitalisation as shown on EDGE (about PHP 12.3 trillion in total).[^pse-edge-stock-data] The EDGE page set is not PSE's listed-company count (280 issuers, [Chapter 2](#/ch/instruments)): it differs in date and coverage, so the two totals are not expected to tie.

| Foreign ownership limit | Companies | Share of market cap shown | Examples |
|---|---|---|---|
| **40%** | **218** | **about 93.5%** | ICTSI, SM Investments, BDO, BPI, Meralco, SM Prime, PLDT, Globe, Ayala Land, all eight REITs |
| 100% | 46 | about 6.2% | Jollibee, Century Pacific Food, Monde Nissin, OceanaGold Philippines, Philippine Seven, D&L Industries, Wilcon Depot, Shell Pilipinas, IMI, SSI Group, Del Monte Pacific, GMA Holdings PDR, ABS-CBN Holdings PDR |
| 0% | 15 | about 0.3% | Media: GMA Network, ABS-CBN, Manila Broadcasting, Prime Media, Manila Bulletin Publishing. Mining: Lepanto Consolidated, Benguet, Oriental Petroleum and Minerals, Manila Mining. Other: Concrete Aggregates, ATN Holdings, F&J Prince, Panasonic Manufacturing Philippines, Filsyn, Metro Alliance |
| 30% | 1 | negligible | National Reinsurance Corp. of the Philippines |
| 60% | 1 | negligible | Ferronoux Holdings |

The largest 40%-limit companies by market capitalisation (PHP billion, EDGE, 6 Oct 2026; 23 of the 218 are suspended securities valued at their last price, Villar Land Holdings among them):[^pse-edge-stock-data]

| Band | Companies (symbol, PHP bn) |
|---|---|
| Above PHP 400bn | ICT 1,827; SM 601; BDO 590; BPI 495; MER 478; SMPH 471 |
| PHP 200 to 400bn | AP 335; AC 326; VLC 289 (suspended); MBT 276; FB 260; EMI 257; **TEL 238; GLO 224**; ALI 220; AEV 217 |
| PHP 100 to 200bn | LTG 168; AREIT 153; SMC 140; JGS 135; CBC 135; RCR 130; MYNLD 120; URC 120; PNB 116; SGP 115; PGOLD 114; APX 110; ACEN 105; DMC 101 |
| Below PHP 100bn | PAL 95; GTCAP 90; MWC 89; PTC 89; MREIT 85; AGI 78; RLC 75; UBP 70; MEG 69; AUB 68 |

- **Banks, REITs, food and beverage groups, telecoms and holding companies are all at 40%.** The one equity ETF page found by name (FMETF) and all eight REITs found by name (AREIT, DDMPR, FILRT, RCR, MREIT, CREIT, VREIT, PREIT) show a 40% limit, so ETF and REIT access does not bypass the limit.[^pse-edge-stock-data]
- **Telecoms still show 40%** on EDGE even though RA 11659 removed telecoms from the public-utility list and the 13th list allows up to 50% or 100%. The issuers' articles evidently have not moved (inference).
- **MSCI's description matches the data.** MSCI says "All industries are in general subject to a 40 percent foreign ownership limit. These limitations affect more than ten percent of the Philippine equity market."[^msci-accessibility-review-2026:43] The 13th list is narrower than that sentence, but the land-ownership rule (nearly every operating company holds land) puts about 94% of capitalisation at 40% in practice (inference).
- **Limits cap the aggregate of all foreign holders.** EDGE shows the limit but **not the current foreign-ownership level**; the issuer-filed data and the live shares-available counter do (next section). Suspended names (for example Villar Land and AllHome) still display a limit.
- **A 0% reading is not always "no foreign access".** Five of the 15 zero-limit pages (ATN Holdings, F&J Prince, Lepanto, Manila Mining, Oriental Petroleum) list a Class B symbol next to the A symbol. The A line is Filipino-only and the B line is open to aliens under the SEC's 1973 rule, and issuers already split into A and B shares are exempt from the foreign-ownership reporting rule, so EDGE's 0% for these pages is best read as the A line (inference); see the Class A and Class B section below. That leaves about ten companies, the five media names and Benguet, Concrete Aggregates, Panasonic Manufacturing, Filsyn and Metro Alliance, with no foreign route except through a PDR where one exists.[^pse-edge-stock-data][^pse-listing-disclosure-rules:157]
- **0% names are reachable only through PDRs.** The two broadcasters with Philippine Deposit Receipt lines, GMA Holdings PDR (GMAP) and ABS-CBN Holdings PDR (ABSP), show a 100% limit on the PDR against 0% on the underlying common shares, consistent with the Constitution's mass-media rule.[^pse-edge-stock-data] A PDR gives the holder the right to the delivery or sale of the underlying share and to adjustments on cash dividends, rights and similar events; it is not evidence of ownership of the issuer.[^pse-investing-at-pse] Both lines are almost untradeable (see [Chapter 2](#/ch/instruments)), and PDR conversion terms were not retrieved. Listed PDRs are registrable through a registering bank (below).[^bsp-fx-manual-morfxt-2025-05:46]

### Execution implications

- Build the foreign universe from two tables: a static limit per security (EDGE Stock Data or the PSE security frames, which also carry the limit)[^pse-sec-frames-snapshot] and the live room from the feed. Treat **0%-limit names as untradeable for foreign accounts** (use the PDR line where one exists) and **100%-limit names as unconstrained**; for the 40% group the foreign room, not 40%, is the quantity that matters.
- With about 94% of capitalisation under a 40% cap, an index-driven foreign bid can run into the cap in a heavily held name. Expect foreign demand to stop at the limit and restart when room recovers (inference).

## Monitoring the limit

The limit is policed at five levels, from the issuer's filing down to the individual order.

| Level | Mechanism | Frequency |
|---|---|---|
| Issuer report | Issuers with unclassified shares and foreign ownership limits file a monthly report (last working day of the first week of the month) so that the Exchange can show foreign holdings "on a real time basis"; since 2 Jul 2007 they must also update foreign and local holdings, including unlisted shares, through the PSE disclosure system (ODiSy, now EDGE) by **4:00 pm of each trading day on which foreign holdings change**, and the figures are "as of 4:00 pm" and approved by PSE before public viewing; issuers already split into Class A and B shares, or wholly foreign-ownable or non-ownable, are exempt[^pse-listing-disclosure-rules:157][^pse-listing-guidance-notes:68][^pse-listing-guidance-notes:72] | Monthly, and daily on change |
| FOL file | Monthly Excel file `FOL_yyyymm.xls`, e-mailed on the 8th day of the following month: company limit, company foreign-owned shares, outstanding shares, and per-security class (C common, P preferred, U unlisted); effective 18 Jun 2008, specification v1.1 of Sept 2019[^pse-fol-spec-v1-1:2][^pse-fol-spec-v1-1:3] | Monthly |
| Account flag | Each trading-participant account code carries a **Nationality Flag (Local or Foreign)**; any change in account type or nationality flag creates a new account code; requests by 4 pm take effect the next trading day[^pse-implementing-guidelines-trading-rules:21][^pse-implementing-guidelines-trading-rules:22] | Per order |
| Order entry | The trading system earmarks every valid foreign buying order against the foreign room[^pse-revised-trading-rules:17] | Per order |
| Depository | Participants with foreign clients keep separate Client-Foreign securities accounts and sub-accounts; transfers must respect the nationality segregation[^pdtc-depository-rules-1997:14][^pdtc-depository-rules-1997:15] | Continuous |

The same account-code classification governs aggregation. A bundled account is classified local or foreign, and "for purposes of foreign ownership monitoring, when posting an Order of combined local and foreign client Orders, the foreign bundled account shall be used". A foreign bundle may be unbundled to foreign clients, local clients and the error account; a local bundle only to local clients and the error account. Unbundling deadlines follow the December 2011 amendments to the Implementing Guidelines: on a whole trading day, 14:00 on T+1 where the nationality flag changes and 17:00 on T+1 where it does not; on a half day, 17:00 on T+0 and 12:00 on T+1.[^pse-tpa-2011-0124-amended-implementing-guidelines:3-4] The 2010 text carried only the half-day limbs (noon T+1, or 5 pm T+0 if the nationality flag changes),[^pse-implementing-guidelines-trading-rules:22] and the SEC's IRR states noon on T+1; chapters [10](#/ch/clearing-settlement) and [13](#/ch/regulatory-constraints) set out the conflict. The error account must carry the trading participant's own nationality.[^pse-implementing-guidelines-trading-rules:21]

<div class="callout warn">
<span class="label">Edition caveat</span>

The Revised Trading Rules and Implementing Guidelines archived here are the **2010** base texts (effective 26 Jul 2010, with piecemeal amendments since and no consolidated version published). The earmarking rule and the nationality-flag mechanics are quoted from them; no later amendment touching them was found, but the current in-force text could not be checked.[^pse-implementing-guidelines-trading-rules:1]
</div>

### The Foreign Shares Available message

The ITCH feed carries a **Foreign Shares Available message [f]** per product code: reference data at the start of the day, then dynamic updates; product codes that do not allow foreign ownership send no [f] message.[^pse-itch-equities-feed-spec-v2-3:22][^pse-itch-equities-feed-spec-v2-3:25] The feed itself is described in [Chapter 11](#/ch/market-data). Layout in the legacy X-stream specification v2.3: type "f" (1 byte), timestamp (4), product code (8), ownership rule ID (2), sign (1, "+" or "-") and foreign shares available (8, integer, "the number of shares currently available for foreign ownership").[^pse-itch-equities-feed-spec-v2-3:19][^pse-itch-equities-feed-spec-v2-3:20] The sign byte allows a **negative** value; the specification does not say when it occurs (foreign holdings above the limit is the natural reading, inference), so decode the field as signed. The absence of an [f] message cannot tell a 0% name from a name whose limit is not tracked; combine it with the static limit.

**Worked example (fictitious data from PSE's file specification).** The sample row in the FOL specification shows "XYZ Land Inc." with a 40% limit, 1,898,121,199 outstanding shares and 75,925,216 foreign-owned shares; the values are fictitious and only illustrate the format.[^pse-fol-spec-v1-1:2] On those figures the limit is 759.2m shares, foreign holdings are 4.0% of outstanding, and room is 683.3m shares (36.0% of outstanding). FTSE's "foreign headroom" definition, (FOL minus foreign holdings) divided by FOL, gives (40% - 4.0%) / 40% = 90%.[^ftse-geis-ground-rules-2026-09:13] The arithmetic is computed here, not published by PSE; the engine's exact basis (per company or per class, net or gross of earmarks) is not documented.

<div class="callout warn">
<span class="label">Scheduled change: 23 Nov 2026, subject to SEC approval</span>

The legacy feed specification is valid until the new trading engine's scheduled go-live on 23 Nov 2026.[^pse-nte-broker-forum-2026-07-09:9] PSE's NTE page lists new ITCH and market-data specifications (v1.2 dated 17 Jul 2026), but they were not retrieved, so **whether and how a foreign-shares-available field is carried after cutover is unverified**.[^pse-web-nte-page] The new back-office portal lists "Trading Account Generator" and "Trade Unbundling" modules, which are where the nationality flag and unbundling will live.[^pse-nte-broker-forum-2026-07-09:13] Engine behaviour at the limit under the new engine is not public.
</div>

### Execution implications

- Subscribe to [f] (or its successor) and gate every foreign-account buy on `foreign_shares_available >= order size`, counting your own working orders. Treat zero or negative as "no foreign bid" and expect only local liquidity on the bid in constrained names, with potentially wider spreads and more impact for foreign flow (inference).
- Because valid foreign buy orders are earmarked, **a resting foreign bid consumes room before it fills**, and other foreign buyers' orders reduce the room you see. Cancel unneeded resting quantity in tight names; PSE can sanction a trading participant that posts foreign buy orders "for the malicious purpose of limiting the available volume for foreign buyers".[^pse-revised-trading-rules:17]
- Keep account codes cleanly flagged. Any foreign component in an aggregated order forces the foreign bundle, so avoid mixing local and foreign flow in one bundle and keep unbundling deadlines simple.

## Behaviour at the limit

### What the rules say

1. **At order entry:** valid foreign buying orders are earmarked and limit "the available volume for succeeding foreign buying Orders within the applicable foreign ownership limits"; posting such orders for the malicious purpose of limiting the room is a **major violation** (first offence PHP 100,000 to 199,999, second PHP 200,000 to 299,999, third and later at least PHP 300,000 and a suspension of at least five trading days; 2010 amounts).[^pse-revised-trading-rules:17][^pse-revised-trading-rules:37][^pse-revised-trading-rules:39]
   Illustration of the rule (my arithmetic; how the engine handles an order larger than the remaining room is not documented): with 5.0m shares of room, a valid foreign bid for 4.0m shares leaves 1.0m available to succeeding foreign buy orders, whether or not the 4.0m ever trades.
2. **After a breaching trade:** SEC Memorandum Circular 10 of 2025 (Sec. 4): "In the remote event that a trade is executed and the same results in a breach of allowable foreign ownership limits, the foreign buyer, through its broker, shall immediately cause the disposition of such number of shares that caused the breach ... at the prevailing market price and shall return the proceeds to the foreign investor." If the breach is discovered during trading hours, disposal is immediate and within the same trading day; otherwise at the opening of the next trading day. Penalties follow SRC Section 54 after due notice and hearing.[^pse-cn-2025-0035-sec-declassification-mandate:3]
3. **The Circular's recital** states that "the PSE maintains a system that strictly monitors and enforces foreign ownership limits given the current technological advances in its trading system".[^pse-cn-2025-0035-sec-declassification-mandate:2]

<div class="callout">
<span class="label">Consequence</span>

Foreign room is a shared, first-come resource that **resting orders consume, not only fills**. In a constrained name a large passive foreign bid reduces, and can exhaust, the volume available to later foreign buyers (by the rule's own wording), and a breach that does execute is a forced market sale of the excess with no price limit. Size every foreign buy against live room, release resting quantity you do not need, and treat zero room as the absence of a foreign bid.
</div>

### What the rules do not say

<div class="callout infer">
<span class="label">Inference</span>

When a security's foreign shares available reach zero, the engine should reject or cap foreign-flagged buy orders while foreign sells and local trades continue. This follows from the earmarking rule, the [f] message and the account flag, but no rule text states the rejection logic. Foreign-to-foreign transfers do not change the foreign total, so a cross between two foreign accounts should remain possible at the limit, but no rule confirms it. **No separate foreign board or alternative foreign price appears in any PSE rule, circular or feed specification read**: the feed has one order book per product code with a shares-available counter. FTSE's eligible-exchange table lists a "Foreign board" for Thailand but only the "Main board" for the Philippines, which is consistent with that.[^ftse-geis-ground-rules-2026-09:32]
</div>

Absence from the sources read is a finding, not proof. The mechanics that matter most for an algorithm (whether a partially acceptable foreign order is cut back or rejected whole, whether earmarks release on cancel and expiry, whether the engine counts hidden quantity) are not public.

### Class A and Class B shares are being abolished

Under SEC guidelines of 7 Sep 1973, Class A common shares could be issued only to Filipino citizens and Class B shares to Filipinos and aliens alike; Class B traded on the regular board and buyers there had to accept either class.[^pse-cn-2025-0035-sec-declassification-mandate:2] The SEC now cites an "unfair disparity in price between Class A and Class B shares", "unwarranted arbitrage for holders of class B" and administrative inefficiency for brokers and SCCP, and has repealed the rule.[^pse-cn-2025-0035-sec-declassification-mandate:2]

| Date | Event |
|---|---|
| 7 Aug 2025 | SEC MC 10 s.2025 issued; discontinues the A/B classification of common shares of listed companies[^pse-cn-2025-0035-sec-declassification-mandate:1][^pse-cn-2025-0035-sec-declassification-mandate:3] |
| 9 Aug 2025 | Circular effective on publication in two newspapers[^pse-cn-2025-0036-declassification-effectivity:1] |
| 11 Aug 2025 | First trading day: buyers on the regular board receive the class they bought and paid for, not an alternative class[^pse-cn-2025-0036-declassification-effectivity:1] |
| **9 Aug 2026** | Deadline for companies to amend their articles of incorporation[^pse-cn-2025-0036-declassification-effectivity:1] |
| 10 Sep 2026 | PSE sets the mechanics for each merger: the single class is priced at the higher of the Class A and Class B closes on the last trading day, after a **two-trading-day** suspension before the classified shares are delisted[^pse-cn-2026-0041-declassification-price-suspension:1] |

The price adjustment, the suspension and PSE's sample timeline (last trading day Thursday 10 Sep 2026, resumption of the single class on Tuesday 15 Sep) are set out with the other corporate-action mechanics in [Chapter 2](#/ch/instruments) and [Chapter 10](#/ch/clearing-settlement).

<div class="callout warn">
<span class="label">Migration is not finished</span>

PSE's listed-company directory on 6 Oct 2026, two months after the articles deadline, still lists five A/B pairs separately: ATN/ATNB, FJP/FJPB, LC/LCB, MA/MAB and OPM/OPMB.[^pse-listed-company-directory-frame] Whether each company has amended its articles, and when each pair will merge under the 10 Sep mechanics, was not checked. Until a pair merges, the A and B lines are still separate securities with separate prices; check each name's articles before relying on historic A/B spreads.
</div>

### Execution implications

- Treat a foreign breach as an uncapped execution-risk event: forced disposal at market, same day or at the next open, with proceeds returned. A pre-trade guard that sizes against live room is cheaper than any post-trade cure.
- For lenders, a foreign-ownership breach before the return of lent shares can block the return to a foreign lender, so the PSE's SBL FAQ makes the lender responsible for monitoring foreign-ownership levels (programme detail in [Chapter 9](#/ch/short-selling)).[^pse-sbl-short-selling-page]
- Watch the A/B collapse: lines that traded at a premium or discount may re-rate on merger, and the price adjustment uses the higher close of the two classes.

## BSP registration, FX and repatriation

### Registration through a registering bank

The BSP's *Manual of Regulations on Foreign Exchange Transactions* (updated May 2025, amended through Circular 1212 of 11 Apr 2025) governs foreign investment in PSE equities.[^bsp-fx-manual-morfxt-2025-05:42] Inward investments by non-residents "need not be registered with the BSP unless the repatriation of capital and/or the remittance of related earnings in pesos thereon shall be funded with FX resources of AABs/AAB forex corps" (authorised agent banks). A Bangko Sentral Registration Document (BSRD) evidences registration, "except those covered by Section 37 for which a BSRD shall no longer be issued".[^bsp-fx-manual-morfxt-2025-05:42]

| Route | Covers | How |
|---|---|---|
| Sec. 36: direct BSP registration | Unlisted equity; onshore investment funds (mutual funds, UITFs) whether listed or not; unlisted PDRs; direct investment items such as branch capital and condominium units[^bsp-fx-manual-morfxt-2025-05:44][^bsp-fx-manual-morfxt-2025-05:45] | Online BSP system, free of charge, within one year of the applicable reckoning date; BSRD issued |
| **Sec. 37: through a registering AAB** | **Equity securities issued onshore by residents and listed at an onshore exchange (e.g. PSE)**; ETFs; listed PDRs; onshore-listed debt; peso time deposits of at least 90 days; government debt; equity of non-residents listed onshore[^bsp-fx-manual-morfxt-2025-05:46] | "Registered upon reporting thereof by the registering AAB to the BSP"; **no BSRD** |

- **The registering AAB** is a bank with an FCDU designated by the non-resident investor to report and monitor the investments; the investor gives each registering AAB an "Authority to Disclose Information" (Appendix 10.4) covering all registered investments.[^bsp-fx-manual-morfxt-2025-05:46]
- **Funding.** FX remitted to fund Sec. 37 investments "must be converted to pesos with AABs/AAB forex corps except if investment is required to be funded by FX" (Sec. 37.3); Sec. 36 investments need not be converted.[^bsp-fx-manual-morfxt-2025-05:45][^bsp-fx-manual-morfxt-2025-05:46]
- **Classification.** Onshore-listed equities, ETFs and PDRs count as foreign direct or portfolio investment depending on control (more than 50% of voting power is control; at least 10% is "significant influence").[^bsp-fx-manual-morfxt-2025-05:43]
- **Servicing (Sec. 38).** Registered investments are "entitled to full and immediate repatriation of capital and remittance of related earnings" using AAB FX, on an Application to Purchase FX (Annex A) with the Appendix 1.4 documents; FX sold is remitted directly to the investor's onshore or offshore account on the date of FX sale.[^bsp-fx-manual-morfxt-2025-05:47] Peso divestment proceeds may sit temporarily in the investor's peso account with any AAB (Sec. 41) and may be reinvested (Sec. 42).[^bsp-fx-manual-morfxt-2025-05:48][^bsp-fx-manual-morfxt-2025-05:49]
- **Peso accounts.** Non-resident peso accounts may be funded only by listed sources (conversion of inward FX, proceeds of BSP-registered investments, services, trade, and **cash collateral for securities borrowing and lending**, among others), and FX can be bought back up to the balance of eligible-source pesos.[^bsp-fx-manual-morfxt-2025-05:19][^bsp-fx-manual-morfxt-2025-05:20]
- **Timeline.** BSP Circular 1030 (5 Feb 2019) added ETFs and onshore-listed PDRs (PSE notice 8 Jul 2019); the BSP confirmed non-resident REIT investment as registrable (PSE notice 26 May 2020); Circular 1192 (11 Apr 2024) amended the registration sections and Circular 1212 (11 Apr 2025) the latest provisions. The May 2025 manual reflects the AAB-only route for listed securities, but the circulars themselves were not retrieved, so which one introduced it is not established.[^pse-cn-2019-0037-foreign-investment-etf:1][^pse-cn-2020-0052-nonresident-reit-investment:1][^bsp-fx-manual-morfxt-2025-05:46]

MSCI describes the practical consequence: "There is no offshore currency market and there are constraints on the onshore currency market (e.g., foreign exchange transactions must be linked to security transactions)", and "overdraft facilities for foreign investors are prohibited".[^msci-accessibility-review-2026:43]

### Hedging the peso exposure

Customers, including non-residents other than regulated financial institutions authorised to deal in FX derivatives, may hedge FX exposure through derivatives with AABs only if the underlying is eligible for servicing with AAB FX, and the notional may not exceed the underlying exposure at any time. Customers can no longer buy FX from AABs for exposures fully covered by deliverable derivatives; AABs may deal non-deliverable derivatives, and NDFs may be used for a sell-side non-deliverable derivative with a non-resident counterparty.[^bsp-fx-manual-morfxt-2025-05:73][^bsp-fx-manual-morfxt-2025-05:74]

### Securities lending and short selling by foreign funds

The SEC approved (PSE circular of 24 May 2023) **offshore collateral** in SBL transactions involving at least one foreign party, provided the participants are Qualified Buyers under the 2015 SRC IRR as amended by SEC MC 6 of 2021; a foreign entity that would qualify if Philippine-established is itself a Qualified Buyer, and a prime-brokered client must itself be a Qualified Buyer.[^pse-cn-2023-0027-offshore-collateral-sbl:1][^pse-cn-2023-0027-offshore-collateral-sbl:2] Allowed offshore collateral is cash in USD, EUR, JPY, GBP or AUD, government and agency debt of OECD members rated at least BBB, and constituents of benchmark indices of World Federation of Exchanges members.[^pse-cn-2023-0027-offshore-collateral-sbl:1] The BIR tax conditions and the pending revision of the SBL rules for foreign lenders are in [Chapter 9](#/ch/short-selling) and [Chapter 12](#/ch/costs). MSCI rates stock lending and short selling "improvements needed" (see the MSCI table below); the programme has not yet become established market practice, and expect thin borrow.

### Execution implications

- Sequence: appoint a PDTC-participant broker or global custodian; designate an FCDU registering AAB and sign the Authority to Disclose Information; convert FX to PHP through AABs **before** trading (no overdraft) and let the AAB report the investment; at exit, buy back FX against the Annex A application (inference from the manual).
- Pre-fund PHP and convert early in the day; a single registering AAB simplifies repatriation reporting. See [Chapter 10](#/ch/clearing-settlement) for the T+2 funding deadlines.
- Hedge notional must stay at or below the registered exposure; NDFs with a non-resident dealer are the fallback. Unregistered exposures cannot be hedged on the same basis (inference).
- Keep PHP balances to settlement needs: interest on them is taxed at 25% for a non-resident corporation ([Chapter 12](#/ch/costs)).

## Custody, omnibus structures and disclosure

The depository, settlement and custodian-chain mechanics (PCD Nominee, the Filipino and non-Filipino balance split, netting by flag, the broker-to-custodian leg, funding deadlines) are in [Chapter 10](#/ch/clearing-settlement). The foreign-access points are these.

- **Account opening.** Trading participants are PSE-accredited brokers; after the account-opening documents "the TP will do its Know Your Customer (KYC) procedure"; online accounts must be pre-funded for buys; settlement is T+2.[^pse-investing-at-pse] Detailed KYC and tax-identification documentation for non-resident institutions was not found, and no global-custodian market guide was retrieved.
- **Nationality is carried end to end.** The trading account code, the bundled-account rule and the depository's Client-Foreign accounts all key off the same Local or Foreign flag, and a transfer between depository accounts must respect the nationality segregation.[^pse-implementing-guidelines-trading-rules:21][^pdtc-depository-rules-1997:15] A mis-flagged instruction is therefore likely to corrupt the foreign-room count, not only the settlement (inference).
- **Omnibus and NoCD.** For ordinary shares the depository sees only the participant (inference; no primary rule found), and MSCI's only custody-related complaint is the overdraft prohibition.[^msci-accessibility-review-2026:43] PDTC's Name-on-Central-Depository facility segregates client holdings under a broker's omnibus account; it is mandatory for dollar-denominated securities and offered for REITs, where the broker's sales report to the transfer agent must break out free accounts "for each nationality/tax status", the information the REIT dividend withholding needs ([Chapter 12](#/ch/costs)). Clients with their own custodians need no NoCD sub-account.[^pdtc-nocd-reit-faq:1][^pdtc-nocd-reit-faq:5][^pdtc-nocd-reit-faq:6]
- **Beneficial-ownership reports.** Any person acquiring 5% beneficial ownership of a class of listed equity must file SEC Form 18-A within five business days with the issuer, the exchange and the SEC; the full threshold ladder (10%, 15%, 35%, 50%) is in [Chapter 13](#/ch/regulatory-constraints).[^sec-2015-src-irr:42]

### Execution implications

- Settle through a single registering bank and a single custody chain per fund where possible, so that the nationality flag, the Authority to Disclose Information and the repatriation reporting all describe the same beneficial owner.
- Put a 5% watch on every capped name in the foreign portfolio: crossing it starts a five-business-day filing clock, and foreign room is also the scarcest in the names where foreign funds are largest.

## Index-provider status and foreign participation

### MSCI

The MSCI 2026 Global Market Accessibility Review (June 2026) keeps the Philippines in the Emerging Markets group, and the Philippines column is **identical to the 2025 review** (all 18 ratings unchanged).[^msci-accessibility-comparison-2026:5][^msci-accessibility-comparison-2025:5] The MSCI Emerging Markets index factsheet of September 2026 lists the Philippines among constituent countries.[^msci-em-index-factsheet-2026-09:1]

| Criterion | Rating |
|---|---|
| Foreign ownership limit (FOL) level | **-** |
| Foreign room level | **-** |
| Foreign exchange market liberalization level | **-** |
| Stock lending | **-** |
| Short selling | **-** |
| Equal rights to foreign investors | + |
| Clearing and settlement | + |
| Stability of institutional framework | + |
| Investor qualification requirement; capital flow restriction level; investor registration and account set-up; market regulations; information flow; custody; registry and depository; trading; transferability; availability of investment instruments | ++ |

Legend: ++ no issues; + no major issues, improvements possible; - improvements needed.[^msci-accessibility-review-2026:71] MSCI's text: foreign room "More than one percent of the MSCI Philippines IMI is impacted by low foreign room"; equal rights "limited as a result of the stringent foreign ownership limits".[^msci-accessibility-review-2026:43]

### FTSE Russell

FTSE Russell classifies the Philippines as **Secondary Emerging**: in the September 2025 annual review (published 7 Oct 2025), in the March 2026 interim review (published 7 Apr 2026) and in the September 2026 ground rules.[^ftse-country-classification-annual-2025-09:5][^ftse-country-classification-interim-2026-03:6][^ftse-geis-ground-rules-2026-09:45] The watch list after September 2025 held Egypt and Nigeria; after March 2026 only Egypt. The Philippines was on neither.[^ftse-country-classification-interim-2026-03:2][^ftse-country-classification-interim-2026-03:5]

<div class="callout warn">
<span class="label">FTSE 2026 announcement: outcome unknown</span>

The 2026 annual country-classification announcement was scheduled for **Tuesday 6 Oct 2026**.[^ftse-country-classification-interim-2026-03:5] It had not been published when the sources were checked, so the outcome is unknown; FTSE "will normally give at least six months' notice before changing the classification of any country", and the Philippines was on no watch list, so no change was signalled.[^ftse-geis-ground-rules-2026-09:9]
</div>

FTSE's Quality of Markets table for Asia Pacific as at March 2026 (Philippines column, read from the rendered table; the full table is in [Chapter 11](#/ch/market-data)) rates, for access purposes: **Not Met** on transaction costs (implicit and explicit), on a developed foreign exchange market (the cell is boxed, which the legend reads as a rating change since September 2025; the prior rating was not checked) and on a developed derivatives market; **Restricted** on the incidence of foreign ownership restrictions, stock lending, short sales, free-delivery settlement, account structure at custodian level and minority-shareholder treatment; **Pass** on capital and income repatriation and on registration of foreign investors, with a T+2 DvP cycle.[^ftse-quality-of-markets-asia-pacific-2026-03:1] The Philippines is the only Developed, Advanced Emerging or Secondary Emerging market in that Asia Pacific table rated "Not Met" on transaction costs (read from the table). The rating was recorded after the 0.1% STT took effect and covers implicit as well as explicit costs; see [Chapter 12](#/ch/costs) and [Chapter 15](#/ch/empirical).

FTSE index construction adjusts constituents for foreign-ownership limits: its Global Equity Index Series ground rules (v14.4, Sept 2026) apply an investability weighting for free float and foreign ownership limits and define "foreign headroom" as (FOL - foreign holdings) / FOL (FOL 49% with 39% held by foreigners gives 20.41%), with a minimum foreign-headroom requirement set out in a linked document whose title refers to 5%; the document itself was not retrieved.[^ftse-geis-ground-rules-2026-09:13]

### Foreign participation: flow-heavy, stock-light

| Measure | Value |
|---|---|
| Foreign share of PSE trades, Aug 2026 | 45.0% |
| Foreign share, year to date 2026 | 48.3% (46.9% in the same period of 2025) |
| Net foreign flow, Aug 2026 | outflow PHP 16.56bn (after a PHP 7.05bn inflow in July) |
| Net foreign selling, year to date | PHP 20.86bn (PHP 45.43bn a year earlier) |
| Foreign accounts, 2025 | 32,709 of 3,641,067 stock market accounts (0.9%); 0.7% of online accounts[^pse-investor-profile-2025:2] |
| Foreign share of listed equity held, end-2023 (OECD) | about 10% (domestic investors 62%) |

The first four rows are from PSE's August 2026 monthly report.[^pse-monthly-report-2026-08:2] The OECD (end-2023, before CMEPA) found foreign ownership of Philippine listed equity the lowest in ASEAN (13% to 26%) and below Asia (18%) and the world (20%); institutional investors are 6% of the total and foreign corporations 3%; in 49% of listed companies the largest shareholder owns more than half the equity.[^oecd-capital-market-review-philippines-2024:122][^oecd-capital-market-review-philippines-2024:121]

<div class="callout infer">
<span class="label">Inference</span>

Foreign participation is **flow-heavy and stock-light**: nearly half of trades but a small slice of holdings, so a foreign seller is mostly selling to a domestic holder. The OECD's roughly 10% counts disclosed holders only; the remainder after domestic (62%) and foreign (10%) sits in an "other free-float" category of investors that do not have to disclose, so 10% is a floor on foreign holdings, not a measure. The series and definition of PSE's foreign ratio are in [Chapter 15](#/ch/empirical).
</div>

### Execution implications

- FTSE underweights or excludes names with insufficient foreign headroom: expect index-driven foreign demand to stop at the limit and restart when headroom recovers, a flow regime an algorithm can anticipate (inference).
- MSCI's accessibility review and market classification review are annual (June 2026 for both; the press report of the 2026 classification result does not name the Philippines), and an FTSE reclassification would come with at least six months' notice, so neither is a near-term trading signal; both determine how much passive foreign money can reach capped names.[^ladige-2026-06-msci-mcr] Index-event volume on the PSE (MSCI's May and November index reviews, FTSE's quarterly reviews) is in [Chapter 11](#/ch/market-data).

## Pending changes

- **New trading engine, 23 Nov 2026** (subject to SEC approval of the accompanying rules): feed and engine behaviour at the foreign limit unverified; see the warning above and [Chapter 17](#/ch/reform-timeline).
- **Revised SBL rules for foreign lenders and borrowers** (an SEC-registered onshore lending agent for the Philippine leg): filed with the SEC on 16 Apr 2026 and "awaiting approval" in July and August 2026 per PSE (see [Chapter 9](#/ch/short-selling)).
- **FTSE's 2026 annual announcement** (scheduled 6 Oct 2026): outcome not known as of 6 Oct 2026. MSCI's next index review is in November 2026 (constituent changes; date not retrieved).
- **A/B declassification**: five pairs unmerged on 6 Oct 2026.

## What is not in the public record

- **Current foreign-ownership levels and room per company.** EDGE shows only the limit; the monthly FOL file, issuer filings and the live shares-available counter are not public in what was retrieved (the EDGE disclosure search returned no "Foreign Ownership" template for PLDT, only a Public Ownership Report).
- **Engine behaviour at the limit** on either engine: rejection logic, treatment of partial room, release of earmarks, hidden quantity, and any foreign-to-foreign crossing rule.
- **Whether the new engine's feed keeps the foreign-shares-available field**, and the status of the A/B pairs after the 9 Aug 2026 deadline.
- **EO 113's publication and effectivity date**, the SEC's nationality-test guidelines (control test, grandfather rule) and the sector statutes behind the 40% limit on banks, insurance and lending companies.
- **Institutional custody practice:** global-custodian market guides, omnibus-account practice, KYC and tax-identification requirements for non-resident institutions, and the BSP appendices (10.A, 10.B, 1.4, Annex A).
- **FTSE's minimum-foreign-headroom document**, the FTSE September 2026 decision, and MSCI's 2026 annual market classification review text for the Philippines (only the accessibility review was read).
