---
number: 2
slug: instruments
title: Instruments, Boards and Listings
summary: Two listing boards, 387 live lines (65 suspended), one ETF; since 11 Aug 2026 a float breach means immediate suspension with no cure period; the odd-lot book ends 23 Nov 2026 if SEC approves.
part: The venue
---

PSE lists everything that trades on its central limit order book under just two listing boards, Main and SME, and the word "board" ends there. The "ETF Board" and "GPDR Board" are labels in rule text, not segments of the engine; there is no foreign board and no buy-in board; the odd-lot market and the block-sale facility are market segments, not boards; and dollar-denominated securities (DDS) are a currency flag. An instrument master for execution should therefore key on (security type, currency, lot regime, state), not on a board code. Figures are as of 6 Oct 2026 unless dated otherwise.

Two behaviours break assumptions carried over from other venues. First, the tradable universe is much smaller than the headline: of 387 live security lines (280 issuers), 65 are suspended, some for a decade, and the one ETF, one warrant series, two PDRs and four US$ lines together averaged about PHP1.3m a day in August 2026 against a market ADV of PHP7.5bn.[^pse-monthly-report-2026-08:1] Second, the minimum-public-ownership (MPO) rule in force since 11 Aug 2026 turns a float breach, usually the by-product of a tender offer, into an immediate suspension of up to six months followed by automatic delisting: there is no cure period during which the stock keeps trading.[^pse-amended-mpo-rule-2026-08:6]

<div class="callout warn">
<span class="label">Scheduled change: 23 Nov 2026, subject to SEC approval</span>

PSE's broker-forum deck of 9 Jul 2026 sets the Nasdaq Eqlipse go-live (big bang, no parallel run) for Monday 23 Nov 2026, with Saturday rehearsals on 31 Oct, 7 Nov and 14 Nov.[^pse-nte-broker-forum-2026-07-09:9] The rule changes tied to it were still "For SEC Approval" on PSE's 17 Aug 2026 status slide, and no approval or effectivity circular had been found by 6 Oct.[^pse-analyst-briefing-1h-2026:9][^pse-asm-2026-president-report:22] If approved: lot size becomes 1 share for PHP and US$ securities, the odd-lot market disappears ("with the standard lot size set at 1, the Odd Lot Market will no longer be available"), and only limit orders are supported on day 1.[^pse-nte-faq-2026-08:1][^pse-nte-broker-forum-2026-07-09:7] This chapter describes the XTS-era rules as in force; the master pipeline is in [Chapter 17](#/ch/reform-timeline).
</div>

## Boards and market segments

### Listing boards

PSE has exactly two listing boards. The First and Second Boards were merged in 2013: the SEC approved the Main and SME listing rules on 20 May 2013, superseding Parts D, E and F of the 2004 rules, and PSE re-cut them on 24 Mar 2021 (Supplemental Rule 12, CN-2021-0021); Article I of the consolidated rules still refers to the First Board, the Second Board and the SME Board.[^pse-listing-disclosure-rules:21][^pse-cn-2021-0021-amended-listing-rules:1] PSE's live directory labels every live security *Main Board* or *SME Board*; the only exceptions are two dormant PLDT convertible-preferred rows (TLII, TLJJ) with a blank board and sector. Its sector filter adds two pseudo-sectors, "SME" and "ETF EQUITY".[^pse-listed-company-directory-frame]

| | Main Board (Art. III Part D) | SME Board (Part E; Part E-1 sponsor model) |
|---|---|---|
| Profit test | cumulative net income of at least PHP75m over the 3 latest fiscal years and at least PHP50m in the latest year; exceptions for issuers operating 10 years or more (PHP75m in 2 of the last 3 years) and for holding companies using a subsidiary's record[^pse-listing-disclosure-rules:50][^pse-listing-disclosure-rules:51] | cumulative EBITDA of at least PHP15m over 3 years, or cumulative revenue of at least PHP150m with average growth of at least 20% over the last 2 years[^pse-listing-disclosure-rules:57] |
| Equity | at least PHP500m | at least PHP25m[^pse-listing-disclosure-rules:58] |
| Operating history | at least 3 years | at least 2 years, plus a 5-year business plan |
| Holders at listing | at least 1,000, each with at least 1 board lot | at least 200, each with at least 1 board lot |
| Lock-up | holders of 10% or more: 180 days from listing (track-record issuers) or 365 days (exempt issuers)[^pse-listing-disclosure-rules:52][^pse-listing-disclosure-rules:53] | non-public holders and related parties: 1 year[^pse-listing-disclosure-rules:60] |
| Annual listing maintenance fee (ALMF) | 1/100 of 1% of market capitalisation, floor PHP250k, cap PHP3.5m since 2 Jan 2025 (was PHP2.0m)[^pse-cn-2024-0068-almf-effectivity:1][^pse-analyst-briefing-1h-2026:12] | PHP100 per PHP1m of market capitalisation, PHP50k to PHP250k |
| Live on 6 Oct 2026 | 271 issuers (276 common lines, 8 of them REITs) | 9 issuers: CTS, HTI, IDC, KPPI, LPC, MFIN, MM, X, XG |

An SME applicant that misses the profit or equity test may list with a PSE-accredited sponsor, which must provide advisory services for at least three full fiscal years; if the sponsorship is terminated and no replacement is found within three months of PSE's approval of the termination, trading is suspended, and at six months the company is automatically delisted.[^pse-listing-disclosure-rules:59][^pse-listing-disclosure-rules:72][^pse-listing-disclosure-rules:74] An SME company may be elevated to the Main Board on written request once it meets the Main criteria; SME issuers may not be portfolio or passive-income companies and may not do a backdoor listing.[^pse-listing-disclosure-rules:61][^pse-listing-disclosure-rules:62] PSE's year-end table shows SME at 11 issuers in 2024 and 10 in 2025.[^pse-listing-statistics-web] PSE rated its sponsor model "Ongoing Review" on 17 Aug 2026: removing the insurance requirement, shortening the sponsor track-record requirement and removing the continuing-sponsorship obligation are under consideration.[^pse-analyst-briefing-1h-2026:16] The 2021 re-cut (SEC approval 4 Feb 2021) came with temporary COVID relief for IPO applications filed in 2021 and 2022: PSE could judge profitability on any two of the three latest fiscal years, excluding the year of impact (2018 and 2019 for a 2021 filing), with added pandemic disclosure; the relief has lapsed.[^pse-cn-2021-0021-amended-listing-rules:1][^pse-cn-2021-0021-amended-listing-rules:2]

Two points that are easy to misread. The Article III Part C sentence "only primary offerings are allowed for listing on the SME Board" is flagged in the rules' own note as superseded: secondary shares in an IPO are barred only for issuers exempt from the track-record test (mining, petroleum, renewable energy and, on the Main Board, holding companies using a subsidiary's record), on both boards.[^pse-listing-disclosure-rules:49][^pse-listing-disclosure-rules:54][^pse-listing-disclosure-rules:62] And no board-specific trading rule was found: Main and SME names use the same Normal-market rules, thresholds and tick and lot tables in every archived trading document (an absence of evidence, not a statement by PSE).

### Labels that are not boards

| Label | What it is | Finding |
|---|---|---|
| ETF Board | a rule-level construct | SR 11 says an ETF "shall be listed on the Exchange's ETF Board, which is a separate board from the Exchange's existing boards",[^pse-sr11-etf-rules-2026:4] yet the directory shows the only ETF, FMETF, with Listing Board = Main Board and sub-sector "ETF-EQUITY".[^pse-listed-company-directory-frame] No separate tape or engine segment appears in any archived specification (inference). The 16 Jun 2026 consultation draft (CN-2026-0029) would drop the construct: ETF securities "shall be listed on the Exchange's Main Board" and ETFs "shall not be required to maintain a minimum public ownership".[^pse-cn-2026-0029-etf-amend-consult:8] |
| GPDR Board | a draft rule only | "GPDRs shall be listed in the GPDR Board of the Exchange"; trading "generally follows" the equity rules.[^pse-cn-2024-0047:12][^pse-cn-2024-0047:23] No GPDR is listed. |
| Foreign board | does not exist | Foreign versus local is a flag on trades and accounts (House, Foreign/Local, Market Maker, Related Party Local/Foreign, Tax-Exempt Local/Foreign, Foreign/Local Retail and Institutional in the trade-amendment matrix).[^pse-implementing-guidelines-trading-rules:23] The old A/B arrangement under which Class B shares traded on the "regular board" was repealed in 2025 (see Class A/B below). |
| Buy-in board | does not exist | SCCP's buy-in is a procedure, not a market: if by 9:15 am of the business day after settlement date a clearing member still lacks securities, SCCP posts buy-in orders on PSE's trading floor at the prevailing offer or, with none, the lower of last close less two fluctuations, last transaction price or current offer.[^sccp-clearing-house-rules-2018:38][^sccp-clearing-house-rules-2018:39] The rulebook text predates T+2; detail in [Chapter 10](#/ch/clearing-settlement). |
| Odd-lot market | a separate segment inside the engine | Orders below the board lot carry an "O" prefix on the symbol (BC becomes OBC); limit and market orders only; continuous session only (no pre-open, pre-close or run-off); no dynamic threshold; reference price is the last adjusted closing price of the Normal market.[^pse-implementing-guidelines-trading-rules:19][^pse-implementing-guidelines-trading-rules:20] DDS may trade there too.[^pse-dds-rules:7] Ends with the new engine if One Lot One Share is approved. |
| Block-sale and cross facility | a pre-arranged-trade facility | Regular block sale: at least PHP20m with price within ±5% of the reference price; special block sale: at least PHP50m, with prior Chief Operating Officer approval.[^pse-implementing-guidelines-trading-rules:24] PSE restated both thresholds on 1 Jul 2026 and noted that a pre-arranged trade below the block minimum can only be entered as a cross inside the best bid and offer; "there is presently no execution facility" for smaller trades priced outside it.[^pse-cn-2026-0031-negotiated-trades:3] Mechanics, approval timing and settlement: [Chapter 5](#/ch/matching). |
| Dollar-denominated securities (DDS) | a currency flag | See DDS below. Not the same as the 2003 Dollar Denominated Trading facility, which quotes the same peso-listed shares in US dollars.[^pse-dds-page-web] |

### Eligible-broker restriction (REITs and DDS)

Only trading participants (TPs) that attended PSE's training and filed a sworn certification of operational readiness may trade REIT shares (Amended REIT Listing Rules Sec. 14; CN-2020-0066 of 15 Jul 2020) or DDS (DDS Rules Part C Sec. 1, item b); PSE restricts non-compliant TPs from trading them.[^pse-cn-2020-0066-reit-broker-eligibility:1][^pse-sr3-2-reit-listing-amend-2023:10-11][^pse-dds-rules:6] REIT shares must also be held under a Name-on-Central-Depository (NOCD) arrangement so that holders are traceable to their own names.[^pse-sr3-2-reit-listing-amend-2023:10] PSE's REIT and DDS product pages list the same 123 eligible TPs (124 rows, one name duplicated), effectively the whole TP roster.[^pse-reit-page-web][^pse-dds-page-web] For REIT IPOs, eligibility also gates the 20% broker allocation and the 10% local-small-investor (LSI) allocation through PSE EASy; the application must reach PSE at least one day before price setting (1:30 pm cut-off) or before the end of the offer period respectively.[^pse-cn-2020-0066-reit-broker-eligibility:2]

### Execution implications

- Key the instrument master on (security type, currency, lot regime, state). The only board attribute PSE exposes is Main or SME, and it carries no trading rule.
- Hard-code an instrument-state filter. A suspension blocks posting, modification and cancellation of orders, bars every TP from dealing in the security directly or indirectly, and (per the Implementing Guidelines) purges all posted orders on suspension; a trading halt of up to one trading day still allows order entry except cross transactions.[^pse-listing-disclosure-rules:140][^pse-implementing-guidelines-trading-rules:27] The Rules text is softer than the Guidelines: posted orders "may be purged at the end of a Trading Day".[^pse-revised-trading-rules:34] Halt and threshold mechanics are in [Chapter 7](#/ch/price-controls).
- Before a suspension is lifted PSE manually imposes a Reservation state in which orders other than crosses may be posted, modified and cancelled, and announces the resumption time beforehand; on resumption after a suspension of a year or more the static threshold is lifted until trades re-establish a basis, so expect gap behaviour (relevant to the Villar names if they stay suspended past June 2027, and to legacy suspended preferreds).[^pse-implementing-guidelines-trading-rules:26][^pse-revised-trading-rules:34]
- Odd-lot flow is a separate book today. If One Lot One Share is approved there is one book with lot = 1: change lot rounding, minimum-notional rules and tick tables together, and read them from static data rather than hard-coding either regime ([Chapter 4](#/ch/order-types)).
- Confirm with the broker that the account route is on the REIT and DDS eligible lists; DDS done-through trades are allowed only among Eligible Brokers.[^pse-dds-rules:7]

## Instrument types

PSE's directory on 6 Oct 2026 lists 387 live security lines once 11 symbol-less rows for securities already delisted and 8 HTML template rows are dropped; 385 have a live security frame (320 Open, 65 Suspended).[^pse-listed-company-directory-frame][^pse-sec-frames-snapshot] The directory has no security-type field, so the type counts below classify by security name and sector strings are good to about ±2.

| Type | Live lines | Open / suspended | What differs in trading |
|---|---|---|---|
| Common shares | 285 (276 Main incl. 8 REITs; 9 SME) = 280 issuers | 256 / 29 | Baseline. Five issuers carry separate A and B lines until declassification completes. |
| Preferred shares | 98 (29 issuers; includes the 4 US$ lines) | 60 / 36, plus 2 with no frame (PLDT TLII, TLJJ) | Same book and sessions; yield-driven; many sub-series per issuer; excluded from the float computation. |
| REITs (inside common) | 8 | 7 / 1 (VREIT) | Eligible-broker restriction, NOCD, 33.33% float, at least 90% payout. |
| PDRs | 2 (ABSP, GMAP) | 2 / 0 | Halt and suspend with the underlying share; lot 1,000; foreign limit "No Limit". |
| Company warrants | 1 (AGIW) | 1 / 0 | No static price limit; auto-delist at expiry; halt with the underlying share. |
| ETF | 1 (FMETF) | 1 / 0 | The only instrument with market-maker obligations; iNAV; creation and redemption through an Authorized Participant. |
| US$ DDS (inside preferred) | 4 (DMPA1, DMPA2, TCB2A, TCB2B) | 2 / 2 | US$ tick and lot table, Eligible Brokers only, US$ settlement. |
| GPDRs, structured warrants, covered warrants, derivatives | 0 | | Rules or projects, not listed products. |
| Debt | not on the equity book | | Corporate bonds and government securities trade on PDEx. |
| **Total** | **387** | **320 / 65, plus 2 without frames** | |

The status split is common 256 open and 29 suspended, preferred 60 open, 36 suspended and 2 without a frame, and PDR, ETF and warrant all open.[^pse-sec-frames-snapshot] On 5 Oct 2026, 257 securities traded (85 advancing, 95 declining, 77 unchanged).[^pse-composite-sector-frame]

### Common shares and share classes

**Class A/B declassification.** SEC MC 10 s.2025 (issued 7 Aug 2025, effective 9 Aug 2025) discontinues the Class A and Class B classification of listed common shares. The 1973 rules had let Class B shares (open to Filipinos and foreigners) trade on the regular board with buyers obliged to accept either certificate. Affected issuers had until 9 Aug 2026 to amend their Articles; since 11 Aug 2025 buyers on the regular board take delivery of the class they bought and paid for; and a foreign buyer whose trade breaches the foreign-ownership limit must have the excess sold immediately (the same day if discovered in trading hours, otherwise at the next open).[^pse-cn-2025-0035-sec-declassification-mandate:1][^pse-cn-2025-0035-sec-declassification-mandate:2-3][^pse-cn-2025-0036-declassification-effectivity:1] PSE's mechanics (CN-2026-0041 of 10 Sep 2026): the adjusted price of the merged single class is the higher of the Class A and Class B closing prices on the last trading day, and trading is suspended for two trading days before the delisting date of the classified shares so that earlier trades settle on the standard T+2 cycle. The sample timeline is last trading day Thu 10 Sep, suspension from Fri 11 Sep, T+2 settlement Mon 14 Sep, then declassification, delisting of the old classes and resumption on Tue 15 Sep.[^pse-cn-2026-0041-declassification-price-suspension:1][^pse-cn-2026-0041-declassification-price-suspension:2]

<div class="callout warn">
<span class="label">Currency: a pending, issuer-specific event</span>

On 6 Oct 2026 the directory still lists five A/B pairs as separate tickers: ATN/ATNB, FJP/FJPB, LC/LCB, MA/MAB and OPM/OPMB (the A lines show a foreign-ownership limit of 0%, the B lines "No Limit", and both show the same free-float level); Keppel Philippines A and B were delisted in 2025.[^pse-sec-frames-snapshot][^pse-delisted-companies-web] The circulars do not say which issuers remain or when each will cut over, so treat each remaining pair as an issuer-specific event that carries the two-day suspension and the adjusted reference price when it happens.
</div>

**Sector reclassification.** PSE classifies a company by the activity that generates at least 60% of its revenue. CN-2025-0047 (26 Dec 2025) moved 13 companies between sectors and sub-sectors effective Mon 5 Jan 2026 (ATN, DITO, ECVC, ECP, FYN, JAS, LMG, PHR, PRC, PHA, PPC, UNH, WIN); ATN and ATNB moved from Holding Firms to Industrial.[^pse-cn-2025-0047-sector-reclassification:1][^pse-cn-2025-0047-sector-reclassification:2] Index consequences are in [Chapter 11](#/ch/market-data).

### Preferred shares

The 98 preferred lines come from 29 issuers: San Miguel Corp. has 21, Megawide 10, Petron 9, Ayala 6, and Arthaland, EEI, Globe, Phoenix Petroleum and Cirtek 4 each (SMC's sub-series 2-A to 2-D were redeemed on 1 Oct 2025 and survive only as stale directory rows). Directory listing dates show 11 new lines in 2021, 11 in 2023, 12 in 2024, 15 in 2025 and 11 so far in 2026, the latest being Arthaland ALCPG and ALCPH on 2 Oct 2026.[^pse-listed-company-directory-frame] Of the 98 lines, 36 are Suspended, mostly series being retired and illiquid legacy series (for example SMC2E to SMC2K, PRF2A, PRF2B, PRF3A and PRF3B, and the PNX and MWP series); the reason for each was not verified.[^pse-sec-frames-snapshot] Primary-market scale in 2026: SMC raised PHP30bn through Series 2-V, 2-W and 2-X (8.0401%, 8.3570% and 8.6483%, 3.27 times subscribed, listed 3 Aug 2026; PHP146.65bn across 11 sub-series and 5 follow-on offerings in total), and Arthaland raised PHP2.15bn through Series G and H (8.1250% and 8.75%, 1.43 times subscribed, listed 2 Oct 2026).[^pse-press-smc-foo-2026][^pse-press-arthaland-foo]

**Listing route replaced on 12 Aug 2026.** CN-2026-0037 (SEC-approved, effective immediately) replaced Article III Part H (Supplemental Rule 19, effective 24 May 2022):[^pse-cn-2026-0037-preferred-shares-rule-effectivity:1][^pse-listing-disclosure-rules:90][^pse-listing-disclosure-rules:91]

| | Old rule (24 May 2022) | New rule (12 Aug 2026) |
|---|---|---|
| Routes | public offering of preferred shares without listing common shares | IPO, or direct listing without a public offering |
| Minimum offer | PHP1bn or 20% of the preferred's market capitalisation, whichever is higher | IPO route: PHP100m[^pse-cn-2026-0037-preferred-shares-rule-effectivity:4] |
| Holders at listing | at least 1,000, each with at least 1 board lot | at least 100, each with at least 1 board lot |
| Float maintenance | 20% of outstanding and listed preferred shares | no maintenance percentage in the new text |
| Direct listing | not available | private-placement shares (qualified institutional buyers or not) and QIB sales are eligible; tradable immediately; any transfer must go through "the Exchange's facility or system for negotiated transactions", with restrictions if issued in an exempt transaction[^pse-cn-2026-0037-preferred-shares-rule-effectivity:5] |
| Post-listing duty | none | direct listing: distribute at least PHP50m to at least 100 investors within 1 year, else PSE may suspend trading, double the ALMF, or require a buy-back within 90 days and delist[^pse-cn-2026-0037-preferred-shares-rule-effectivity:5][^pse-cn-2026-0037-preferred-shares-rule-effectivity:6] |
| Lock-up and offer period | 365 days for issuances below the offer price in the prior 180 days; 5 trading days public, 3 for LSIs | unchanged for the IPO route[^pse-cn-2026-0037-preferred-shares-rule-effectivity:4] |
| Pricing and shelf | offering price at the issuer's discretion under the general IPO rules[^pse-listing-disclosure-rules:39] | initial price set by a financial-adviser report (yields, spreads, comparables); shelf listing up to 5 years[^pse-cn-2026-0037-preferred-shares-rule-effectivity:3] |
| Disclosure | full continuing-disclosure rules | limited to events affecting the ability to pay dividends;[^pse-cn-2026-0037-preferred-shares-rule-effectivity:1] modified penalty scale (basic penalty PHP5,000 for issuers with under PHP25m of assets up to PHP50,000 at PHP1bn and above, plus a per-day penalty)[^pse-cn-2026-0037-preferred-shares-rule-effectivity:9] |

Preferred shares and treasury shares are excluded from the MPO computation.[^pse-amended-mpo-rule-2026-08:3] The consultation ran from CN-2026-0015 (21 Apr 2026) through a second exposure draft, CN-2026-0028 (10 Jun 2026), to an SEC submission on 25 Jun 2026.[^pse-asm-2026-president-report:22][^pse-circular-index-2025-2026]

<div class="callout infer">
<span class="label">Inference</span>

The direct-listing rule routes every transfer through "the Exchange's facility or system for negotiated transactions" but does not name it. The dedicated Negotiated Trades facility is still a proposal ([Planned products](#/ch/instruments/planned-products-and-rule-changes)), and the only live PSE facility for pre-arranged trades is the block-sale and cross facility. What a holder of a directly listed preferred actually uses today is therefore not stated in the public record; confirm with the broker before assuming any secondary liquidity.
</div>

### Company warrants

CLDR Article V Part E covers subscription warrants (exercise period of 1 to 5 years) and two derivative types: covered warrants, where the issuer owns 100% of the underlying listed shares under a charge to an independent trustee bank, and non-collateralised warrants, issuable only by investment houses and universal banks with an irrevocable guarantee and stand-by letter of credit from a guarantor with at least PHP1.25bn of unimpaired paid-up capital; derivative warrants run 9 to 24 months.[^pse-listing-disclosure-rules:113][^pse-listing-disclosure-rules:116][^pse-listing-disclosure-rules:117][^pse-listing-disclosure-rules:118] All warrants are freely transferable (non-detachable ones only with the host security); listing of warrants issued by listed companies is mandatory; warrants delist automatically at the end of the exercise period; the exercise price may not be below par (PHP5 if no par); and listing is effected 7 trading days after the Notice-of-Approval conditions are met.[^pse-listing-disclosure-rules:121][^pse-listing-disclosure-rules:122][^pse-listing-disclosure-rules:123] The part carries a note that the rules are "subject to revisions … pending final approval by the Commission".[^pse-listing-disclosure-rules:112]

Only one series is listed: **AGIW**, 2.2bn warrants of Alliance Global Group listed 19 Dec 2025 (PHP1.1bn gross proceeds, exercise price PHP12, five-year exercise period, up to PHP26.71bn if fully exercised), which rose 100% on listing day to PHP1.00.[^pse-press-agi-warrants] On 5 Oct 2026 AGIW last traded at PHP1.05 (5,000 warrants, PHP5,270; 52-week range 0.60 to 1.96), with 2,203,548,165 warrants listed, lot 1,000, free float 28.54% and market capitalisation of about PHP2.3bn.[^pse-sec-frames-snapshot] Earlier company warrants were Cirtek TECHW (expired 19 Aug 2024), Leisure & Resorts World LRW (29 Oct 2021) and Megaworld MEGW1 and MEGW2 (2014 to 2015): company-issued warrants are rare and short-lived.[^pse-delisted-companies-web] No derivative or covered warrant is listed, and none appears among the delisted warrants (inference from the directory and the delisted-companies list).

The static price limit does not apply to warrants,[^pse-revised-trading-rules:20][^pse-implementing-guidelines-trading-rules:10] and a halt or suspension of the underlying share also halts or suspends any warrant, PDR or other security that directly derives its value from it, so AGIW stops with AGI.[^pse-revised-trading-rules:34][^pse-implementing-guidelines-trading-rules:27]

### The ETF: FMETF

**Instrument.** FMETF ("ATR FAMI Philippine Equity Exchange Traded Fund, Inc.", listed 2 Dec 2013 as the First Metro Philippine Equity ETF) is the only ETF. It was the country's first, with authorised capital of PHP3bn, PHP750m listed on day one, and the PSEi as benchmark.[^pse-annual-report-2013:22] PSE's ETF page lists First Metro Securities Brokerage Corp. as both Market Maker and Authorized Participant.[^pse-etf-page-web]

| 5 Oct 2026 | Value |
|---|---|
| Last price, volume | PHP97.00; 8,610 shares (PHP835,667); 52-week range 94.80 to 109.50 |
| iNAV on PSE's frame (6 Oct) | 97.3388, so the last price was about 0.35% below iNAV (readings taken at different times, so illustrative)[^pse-etf-frame] |
| Size | 11,891,260 shares outstanding (frame also shows 11,841,260 issued and 30,000,000 listed); par PHP100; lot 10; free float shown 100%; market capitalisation about PHP1.15bn; the day's volume was about 0.07% of shares outstanding[^pse-sec-frames-snapshot] |

The gap between 30,000,000 listed and about 11.9m outstanding looks like a shelf-listing artefact (inference): under SR 11 an ETF may list every share in its registration statement, but trading eligibility starts only on notice that shares were created and issued to or through an Authorized Participant, and unissued shares are removed when the shelf lapses.[^pse-sr11-etf-rules-2026:5]

**Rule set** (SR 11, SEC-approved 18 Mar 2013, with the SEC ETF Rules of MC 10 s.2012 appended; a text comparison of the May 2026 "UPDATED" posting with the 2021 posting shows no difference apart from the appended SEC rules, so no substantive 2026 change is in force).[^pse-sr11-etf-rules-2026:4]

| Item | Rule |
|---|---|
| Structure | open-end investment company issuing and redeeming in Creation Units against a basket of securities; all directors Filipino; minimum authorised and paid-up capital PHP250m[^pse-sr11-etf-rules-2026:3][^pse-sr11-etf-rules-2026:5][^pse-sr11-etf-rules-2026:33] |
| Participants | at least 2 Authorized Participants (registered broker-dealers and active TPs with at least PHP100m paid-up capital) at all times; at least 1 designated Market Maker, drawn from the APs; transfer agent with at least PHP100m paid-in capital; fund manager in operation for at least 2 years[^pse-sr11-etf-rules-2026:3][^pse-sr11-etf-rules-2026:4] |
| Listing | outside the IPO distribution rules (no mandatory 20% TP or 10% LSI allocation); underlying securities must be listed and sufficiently liquid; shelf listing allowed[^pse-sr11-etf-rules-2026:5][^pse-sr11-etf-rules-2026:6] |
| Public ownership | 10% of issued shares, with AP and Market Maker holdings and shares from creation and redemption counted as public[^pse-sr11-etf-rules-2026:7] |
| iNAV | disclosed every 1 minute during trading hours (PSE's frequency; the SEC rules default to 15 seconds unless the Exchange proposes another);[^pse-sr11-etf-rules-2026:8][^pse-sr11-etf-rules-2026:36] NAV, NAV per share, shares outstanding, index and tracking error announced daily, cut-off 4:30 pm, moved to 6:30 pm by Board Resolution 141 of 11 Sep 2013 |
| Creation and redemption | only an AP may submit instructions to the ETF; on PSE's page it "can occur any time during trading hours", initiated by a cross transaction through PSE, with creation done when the ETF price is above iNAV[^pse-sr11-etf-rules-2026:37][^pse-etf-page-web] |
| Notification | within 10 minutes: any creation or redemption (with the resulting shares outstanding), a tracking-error breach, a failure to publish iNAV, loss of the Market Maker; monthly issuance and redemption report within 5 trading days of month-end[^pse-sr11-etf-rules-2026:10][^pse-sr11-etf-rules-2026:11] |
| Suspension | if suspended underlying securities make up 20% or more of the basket, if there is no Market Maker for 1 month, or on SEC order; trading is also suspended if a terminated Market Maker, AP, fund manager, custodian, index provider or transfer agent is not replaced at least 10 trading days before the termination takes effect[^pse-sr11-etf-rules-2026:11][^pse-sr11-etf-rules-2026:12] |
| 1-hour halt (longer if PSE deems it necessary) | on the first day of a tracking-error breach, delisting of an underlying security, a halt in underlying securities worth 20% or more of the index, or late iNAV[^pse-sr11-etf-rules-2026:12][^pse-sr11-etf-rules-2026:13] |
| Fees and penalties | filing PHP50k, listing PHP100k, ALMF 1/200 of 1% of market capitalisation capped at PHP250k; PHP100 a day for too few APs, PHP500 a day with no Market Maker[^pse-sr11-etf-rules-2026:14] |
| Delisting | more than 90% of shares must be purchased or redeemed, with a fairness opinion[^pse-sr11-etf-rules-2026:13-14] |

**Market-maker obligations** (ETF Market Making Rules and Implementing Guidelines Sec. 2; the general regime is in [Chapter 8](#/ch/market-making)). The Market Maker must keep two-way quotes within a maximum spread set by price band:[^pse-sr11-etf-rules-2026:23]

| Price band (PHP) | Maximum spread |
|---|---|
| 0.0001 to 0.4950 | 20 ticks |
| 0.5000 to 19.9800 | 15 ticks |
| 20.0000 to 999.5000 | 10 ticks |
| 1,000 and above | 5 ticks |

Each market-making order must be at least 5 board lots. A *wide spread* (a spread beyond the limit, or a one-sided book) lasting at least 3 continuous minutes must be cured within 90 seconds, and the Market Maker must keep orders in the book for at least 50% of each trading day and 80% of each month.[^pse-sr11-etf-rules-2026:23][^pse-sr11-etf-rules-2026:24][^pse-sr11-etf-rules-2026:25]

At FMETF's PHP97 (tick PHP0.05, lot 10) the cap is 10 ticks, PHP0.50 or 51.5 bp of price against a tick of 5.2 bp, and the minimum quote is 5 lots of 10 shares, 50 shares or PHP4,850 a side (inference from the tables and the lot and tick tables). The obligation is a spread cap, not a depth commitment: the whole day's value on 5 Oct, PHP835,667, equals about 170 minimum-size quotes.

**Pipeline (consultation only).** CN-2026-0029 (16 Jun 2026, comments to 30 Jun; aligned with SEC MC 14 s.2026 on umbrella funds) proposes umbrella ETFs (each sub-fund its own ticker), UITFs and other collective investment schemes as issuers with fund units listable beside shares, actively managed ETFs, minimum paid-up capital cut from PHP250m to PHP50m (PSE's press note adds a floor as low as PHP1m for investment companies with a 5-year record), a single Authorized Participant (deemed Market Maker if alone; otherwise the Market Maker need not be an AP, though only an AP may submit creation and redemption instructions), ETFs tracking foreign-listed or regulated OTC securities, and no public-ownership minimum.[^pse-cn-2026-0029-etf-amend-consult:3][^pse-cn-2026-0029-etf-amend-consult:4][^pse-cn-2026-0029-etf-amend-consult:7][^pse-cn-2026-0029-etf-amend-consult:9][^pse-press-additional-reforms] None is in force: PSE's 17 Aug 2026 status slide shows the ETF amendments "Revising per Public Comments".[^pse-analyst-briefing-1h-2026:16] BSP Circular 1030 (5 Feb 2019) already makes ETFs eligible inward foreign investments, registrable through authorised agent banks ([Chapter 14](#/ch/foreign-access)).[^pse-cn-2019-0037-foreign-investment-etf:1]

### REITs

Eight REITs are listed, all on the Main Board.

| Ticker | Issuer | Listed | Last, 5 Oct | Volume / value, 5 Oct | Frame float | Status |
|---|---|---|---|---|---|---|
| AREIT | AREIT, Inc. (first PH REIT) | 13 Aug 2020 | 36.90 | 439,400 / PHP16.2m | 36.18% | Open; PSEi member |
| DDMPR | DDMP REIT, Inc. | 24 Mar 2021 | 1.03 | 1.86m / PHP1.9m | 33.36% | Open |
| FILRT | Filinvest REIT Corp. | 12 Aug 2021 | 2.74 | 1.43m / PHP3.9m | 35.03% | Open |
| RCR | RL Commercial REIT, Inc. | 14 Sep 2021 | 6.23 | 2.40m / PHP14.8m | 44.18% | Open; PSEi member since 2 Feb 2026 |
| MREIT | MREIT, Inc. | 1 Oct 2021 | 13.42 | 542,500 / PHP7.3m | 44.71% | Open |
| CREIT | Citicore Energy REIT Corp. | 22 Feb 2022 | 2.90 | 2.63m / PHP7.6m | 38.22% | Open |
| VREIT | VistaREIT, Inc. | 15 Jun 2022 | 1.31 (stale) | 0 | 35.29% | **Suspended since about 1 Jun 2026** (Villar group) |
| PREIT | Premiere Island Power REIT Corp. | 15 Dec 2022 | 1.00 | 150,000 / PHP0.15m | 48.90% | Open |

Listing dates come from PSE's new-listings page and prices, volumes and floats from the REIT list and security frames;[^pse-new-listings-ipo-web][^pse-reit-frame][^pse-sec-frames-snapshot] RCR replaced AGI in the PSEi on 2 Feb 2026.[^pse-press-rcr-psei] PSE's new-listings page tags VREIT and PREIT as SME at their 2022 IPOs while the directory shows Main Board for both; no transfer is documented. The PSEi has two REITs, AREIT and RCR.[^pse-cn-2026-0035:2]

**Regime.** The legal frame is RA 9856 (REIT Act of 2009), the SEC implementing rules (MC 1 s.2020, amended by SEC MC 1 s.2026, issued 8 Jan 2026 and effective 25 Jan 2026), BIR RR 3-2020 and PSE's Amended REIT Listing Rules (Supplemental Rule 3; the 2023 amendments are SR 3.2, CN-2023-0010 of 9 Mar 2023, which supersede the 2020 rules and the 13 Jun 2022 amendments).[^pse-regulation-listed-company-web]

| Item | Requirement |
|---|---|
| Distribution | at least 90% of distributable income each year, by the last working day of the 5th month after fiscal year-end[^sec-mc-1-2020-reit-irr:10] |
| Public company | listed, with at least 1,000 public shareholders each holding at least 50 shares and together at least one-third of outstanding capital stock[^sec-mc-1-2020-reit-irr:11][^pse-sr3-2-reit-listing-amend-2023:2] |
| Capital and board | paid-up capital at least PHP300m; stockholders' equity at least PHP500m at filing; at least one-third (minimum 2) independent directors[^sec-mc-1-2020-reit-irr:12][^pse-sr3-2-reit-listing-amend-2023:3] |
| Assets and leverage | at least 75% of deposited property in income-generating real estate, at least 35% in Philippine real estate, at most 40% overseas with SEC authority; borrowings at most 35% of deposited property, up to 70% if publicly rated investment grade[^sec-mc-1-2020-reit-irr:14][^sec-mc-1-2020-reit-irr:16] |
| Sponsor | reinvestment undertaking and plan (proceeds reinvested in Philippine real estate or infrastructure within 1 year); quarterly reinvestment reports; the 3-year same-business track-record test is waived[^pse-sr3-2-reit-listing-amend-2023:2][^pse-sr3-2-reit-listing-amend-2023:3][^pse-sr3-2-reit-listing-amend-2023:6][^pse-sr3-2-reit-listing-amend-2023:8] |
| Lock-up | Main Board: holders of 10% or more locked 180 days from listing (track-record REIT) or 365 days (newly incorporated REIT invoking its assets' record, or exempt issuer); SME: non-public holders and related parties 1 year[^pse-sr3-2-reit-listing-amend-2023:4] |
| Continuing | annual full valuation by an accredited independent valuer (not the same valuer for more than 3 consecutive years); failure to maintain public ownership means suspension of up to 6 months, then automatic delisting; any delisting needs a tender offer[^pse-sr3-2-reit-listing-amend-2023:7][^pse-sr3-2-reit-listing-amend-2023:8][^pse-sr3-2-reit-listing-amend-2023:10] |
| Float under the 2026 MPO rule | 33.33% at IPO and maintained[^pse-amended-mpo-rule-2026-08:2][^pse-amended-mpo-rule-2026-08:3] |

The tax and float rules interlock: under BIR RR 3-2020 a REIT's dividends are deductible only if paid within five months of year-end, the REIT keeps public-company status and follows its reinvestment plan, and before declaring dividends it files a sworn statement that the minimum public ownership was maintained at all times (with quarterly shareholder lists carrying TINs); sales of REIT shares outside the Exchange attract capital gains tax.[^bir-rr-3-2020-reit:4][^bir-rr-3-2020-reit:5] A REIT that slips below its float therefore loses a tax deduction as well as its listing. DDMPR's frame float is 33.36%, 0.03 percentage points above the 33.33% line. PSE's REIT page adds a management fee of at most 1% of NAV and a sponsor sale of at least one-third of the REIT to the public.[^pse-reit-page-web]

**SEC MC 1 s.2026** is known only from a law-firm summary (the SEC text was not retrievable): it widens eligible assets to those "capable of producing recurring and predictable cash flows" (transport, telecom and energy infrastructure, data centres, parking, warehouses), allows indirect holding through SPVs or joint ventures if the REIT owns at least two-thirds of voting capital, defines a public shareholder as one with no sponsor affiliation or "substantial influence" (presumed at 10%), and caps the management fee at 1% of NAV.[^cruzmarcelo-sec-reit-rules-2026] PSE said on 11 Sep 2026 that the framework is "already proving to be a powerful catalyst", cited a VITRO REIT listing application and toll-road interest, and warned that 8%-plus preferred yields may moderate REIT listings.[^pse-press-reit-framework-forum] The Vitro REIT IPO (about PHP24.19bn) is scheduled for 12 Oct 2026.[^pse-asm-2026-president-report:8]

### PDRs

ABSP (ABS-CBN Holdings PDRs, listed 7 Oct 1999) and GMAP (GMA Holdings PDRs, listed 30 Jul 2007) are Services/Media lines on the Main Board.[^pse-listed-company-directory-frame] On 5 Oct 2026 GMAP last traded at PHP3.25, 17.9% below its 25 Sep close of PHP3.96, on 46,000 PDRs (PHP150,190); ABSP last traded at PHP2.32 with no trade since 2 Oct.[^pse-sec-frames-snapshot] Static data: ABSP 91.77m PDRs outstanding (262.5m listed), free float 85.72%, market capitalisation about PHP213m; GMAP 363.5m PDRs, free float 20.80%, about PHP1.44bn; both with lot 1,000 and foreign limit "No Limit" even though the underlying broadcasters carry 0%, consistent with PDRs being the foreigner-accessible wrapper for 100%-Filipino media companies (inference). Underlying shares of PDRs count as public shares in the float guidelines unless otherwise non-public,[^pse-amended-mpo-rule-2026-08:11] and BSP's FX Manual lists onshore-listed PDRs as eligible inward investments.[^pse-cn-2019-0037-foreign-investment-etf:2]

### Dollar-denominated securities (DDS)

PSE describes DDS as "listed, traded and settled in US dollar", a "different asset class than the issuer's existing listed shares".[^pse-dds-page-web] The four live lines are DMPA1 and DMPA2 (Del Monte Pacific US$ Series A-1 and A-2 preference shares) and TCB2A and TCB2B (Cirtek Holdings Preferred B-2 sub-series, quoted in US dollars).[^pse-dds-frame] On 6 Oct 2026 DMPA1 was Suspended (last US$10.00, last data 24 Mar 2022), DMPA2 Suspended (US$9.71, 10 Nov 2022), TCB2A Open (US$0.06 on 1 Oct 2026, zero volume) and TCB2B Open (US$0.36 on 13 Jul 2026).[^pse-sec-frames-snapshot] DDS turnover averaged PHP0.04m a day in August 2026.[^pse-monthly-report-2026-08:1]

The DDS rulebook (Supplemental Rule 13, CN-2016-0078 of 2 Dec 2016) applies to existing listed companies; the issuer must be in good standing and engage at least two Eligible Brokers as a continuing condition.[^pse-dds-rules:2][^pse-dds-rules:4] Reference price, trading threshold and the open and close calculation are the peso-stock rules by reference; DDS may trade in the odd-lot market; trader value limits are applied after converting orders to pesos at the previous day's exchange rate; block sales are US$500,000 (regular) and US$1,000,000 (special).[^pse-dds-rules:7] Settlement is in US dollars through an SCCP-designated bank: TPs need an FCDU account and a separate US$ settlement account, funds must be good cleared funds by the settlement deadline, and collateral for mark-to-market deposits is US$ cash.[^pse-dds-rules:8-9]

| Price (US$) | Tick (US$) | Lot |
|---|---|---|
| to 0.99 | 0.01 | 100 |
| 1.00 to 4.99 | 0.01 | 20 |
| 5.00 to 9.99 | 0.01 | 10 |
| 10.00 to 19.98 | 0.02 | 10 |
| 20.00 to 49.95 | 0.05 | 10 |
| 50.00 to 99.95 | 0.05 | 5 |
| 100.00 to 199.90 | 0.10 | 5 |
| 200.00 to 499.80 | 0.20 | 5 |
| 500.00 to 999.50 | 0.50 | 5 |
| 1,000 and above | 1.00 | 5 |

Source: DDS Rules Part C Sec. 1;[^pse-dds-rules:6] the same table appears as the "current" US$ table in PSE's Jan 2026 engine deck.[^pse-nte-user-group-2026-01-15:10] At US$0.06 a single tick is 16.7% of the price and a lot of 100 is worth US$6; at US$0.36 a tick is 2.8%.

### Not yet listed: GPDRs, structured warrants and derivatives

**GPDRs.** A Global Philippine Depositary Receipt is a peso-denominated instrument giving economic but no voting interest in a foreign-listed security, with an option to convert to the underlying.[^pse-analyst-briefing-1h-2026:10] The draft rules (CN-2024-0047 of 26 Sep 2024) allow Trading Participants, BSP-authorised banks and non-bank financial institutions, and investment companies with a 3-year operating history to issue them, with at least PHP100m of paid-up capital and of equity; the underlying must be listed, traded and in good standing on a member exchange of the World Federation of Exchanges; the ratio is 1:1 or as specified; the issuer must mirror the underlying's material disclosures; trading follows the equity rules but PSE may adjust GPDR trading hours to the overseas market; GPDR trading is suspended if the underlying is suspended or has a corporate action affecting its price or share count; and clearing follows SCCP equity procedures.[^pse-cn-2024-0047:6][^pse-cn-2024-0047:7][^pse-cn-2024-0047:10][^pse-cn-2024-0047:19][^pse-cn-2024-0047:23][^pse-cn-2024-0047:24] Revised rules were submitted to the SEC on 24 Jun 2026, with approval and publication "targeted within the quarter"; no approval or GPDR listing has been found by 6 Oct 2026.[^pse-asm-2026-president-report:24]

**Structured warrants and derivatives.** SEC proposed rules on the registration and trading of structured warrants were circulated by PSE on 30 Apr 2026 (comments to the SEC by 13 May 2026), and PSE is aligning its draft with them.[^pse-cn-2026-0018:1][^pse-asm-2026-president-report:24] PSE is developing derivatives starting with PSEi index futures; no rule, launch date or clearing house is in the public record ([Planned products](#/ch/instruments/planned-products-and-rule-changes)).

### Debt and other funds

PSE's rules allow debt listings (minimum issue PHP100m, at least 100 holders, rated unless national-government paper), but corporate bonds and government securities trade on PDEx (PDS Group).[^pse-listing-disclosure-rules:92-93] PSE owned 94.55% of PDS Holdings (PDEx and PDTC) on 4 Feb 2026 and targets phase 2 of the integration, including fixed-income ETFs and derivatives, for 2027; corporate bond listings were 22 in 2024, 25 in 2025 and 16 in 6M26.[^pse-annual-report-2025:9][^pse-asm-2026-president-report:28][^pse-asm-2026-president-report:9] No fund other than FMETF is exchange-listed; open-end mutual funds and UITFs are not.

### Execution implications

- Treat ETF, PDR, warrant and DDS lines as no-algo instruments. Their August ADV was PHP0.93m (ETF), PHP0.35m (warrants and PDRs together) and PHP0.04m (US$), so any child order sized off ADV exceeds the day's value.[^pse-monthly-report-2026-08:1] FMETF's market-maker obligation (5 lots, 10-tick cap) is the only structural liquidity source.
- ETF arbitrage is a cross transaction against an Authorized Participant, not an open-market trade. PSE's ETF page says each ETF must have at least two Authorized Participants, yet its participants table names one, First Metro Securities (also the Market Maker); whether a second AP exists unlisted is not in the public record.[^pse-etf-page-web][^pse-sr11-etf-rules-2026:4]
- Preferred shares are yield-driven and come in many sub-series per issuer: aggregate by issuer in risk limits, handle series-level suspensions, and expect new series from direct listings with no stated secondary market.
- Check the currency flag. US$ lines use a different lot and tick table, and TCB2A and TCB2B sit at US$0.06 and US$0.36, where one US$0.01 tick is 17% and 3% of the price.
- Linked halts are automatic: a halt or suspension of ABS-CBN or GMA Network shares takes ABSP or GMAP with it, and AGIW stops with AGI.[^pse-revised-trading-rules:34]
- Warrants carry no static price limit and have printed +100% on day one; a down-move is unconstrained too.[^pse-press-agi-warrants]

## Universe statistics

### Counts and the 14 Aug 2026 reconciliation

PSE's own year-end series counts listed companies, not lines (delistings are from PSE's delisted-companies list, and the last row is derived from the directory):[^pse-listing-statistics-web][^pse-delisted-companies-web]

| Year-end | Main | SME | Total | New listings | Delisted (issuers) |
|---|---|---|---|---|---|
| 2021 | 269 | 7 | 276 | 8 | 3 |
| 2022 | 276 | 10 | 286 | 10 (6 Main, 4 SME) | 0 |
| 2023 | 273 | 10 | 283 | 3 | 6 |
| 2024 | 272 | 11 | 283 | 3 | 3 |
| 2025 | 272 | 10 | 282 | 2 | 3 |
| 6 Oct 2026 | 271 | 9 | 280 | 1 (LTL) | 3 (ATI, LAND, RRHI) |

PSE's 17 Aug 2026 analyst briefing (market data as of 14 Aug 2026) reports 280 listed companies, total market capitalisation PHP20.56tn (+9.8% YTD), PSEi 6,297.30 (+4.0% YTD), average daily value PHP7.57bn, capital raised YTD PHP69.43bn and net foreign selling PHP8.89bn.[^pse-analyst-briefing-1h-2026:3] The directory reconciles to that figure: 285 common lines less 5 B-class lines (ATNB, FJPB, LCB, MAB, OPMB) is 280 issuers, which equals PSE's 282 at end-2025 plus 1 listing in 2026 (PNB Holdings, LTL, by introduction on 25 Sep) less 3 delistings (ATI on 3 Apr, LAND on 6 Jul, RRHI on 31 Aug). PSE's 280 at 14 Aug (282 less ATI and LAND) ties because the later RRHI delisting and LTL listing net to zero.[^pse-delisted-companies-web] The Main and SME split also ties (271 and 9 in the directory against 270 and 10 from rolling PSE's table forward) if exactly one company moved from SME to Main; Altus Property (APVI) is the plausible candidate (tagged SME at its Jun 2020 listing by introduction, Main in the directory), but that move is unverified. The three foreign-incorporated issuers (MFC, SLF, DELM) and the 8 REITs are inside the count.

| Sector (common lines) | Lines | Suspended |
|---|---|---|
| Industrial | 75 | 6 |
| Services | 60 | 7 |
| Property (incl. 8 REITs) | 51 | 8 |
| Holding Firms | 32 | 2 |
| Financials | 31 | 3 |
| Mining & Oil | 27 | 2 |
| SME Board (no sector tag) | 9 | 1 |
| **Total** | **285** | **29** |

Sub-sector lines: Banks 17 and Other Financial Institutions 14; Industrial is Food/Beverage/Tobacco 29, Electricity/Energy/Power/Water 25, Construction/Infrastructure/Allied 10, Electrical Components 6, Chemicals 4, Other 1; Mining 22 and Oil 5; Services is Transportation 10, Retail 9, Casinos & Gaming 8, Information Technology 8, Hotel & Leisure 6, Other Services 6, Telecommunications 5, Education 4, Media 4.[^pse-listed-company-directory-frame][^pse-sec-frames-snapshot] The directory's sector strings are inconsistent (VREIT's sub-sector reads "REIT", FILRT's sector field holds the company name), so treat these counts as ±2.

Static data across the 285 common lines: **board lot** 1,000 shares for 116 issues, 100 for 76, 10,000 for 49, 10 for 26, 100,000 for 7, 1,000,000 for 7 and 5 for 4 (current tiers; [Chapter 4](#/ch/order-types)); **foreign ownership limit** 40% for 217 issues, "No Limit" for 51 (including DELM, MFC, SLF, MONDE, OGP, SEVN, JFC, WLCON and the B-class lines), 0% for 15 (mass media, some mining and oil A shares, and others), 60% for Ferronickel and 30% for NRCP ([Chapter 14](#/ch/foreign-access)).[^pse-sec-frames-snapshot]

### Market capitalisation and turnover

| Measure | Value |
|---|---|
| Total market capitalisation | PHP20.01tn (2024), 18.73tn (2025), 19.44tn (6M26); 20.56tn on 14 Aug 2026; 19.82tn at end-Aug (20.14tn at end-Jul)[^pse-asm-2026-president-report:6][^pse-analyst-briefing-1h-2026:3][^pse-monthly-report-2026-08:2] |
| Domestic market capitalisation (excludes three foreign companies) | PHP13.65tn at end-2025 (PHP14.57tn at end-2024); 13.06tn at end-Aug 2026 (13.32tn at end-Jul)[^pse-monthly-report-2025-12:2][^pse-monthly-report-2026-08:2][^pse-press-last-trading-day-2025] |
| Average daily value | PHP6.10bn (2024), 7.33bn (2025), 7.72bn (6M26); 7.57bn on 14 Aug 2026[^pse-asm-2026-president-report:6][^pse-analyst-briefing-1h-2026:3] |
| PSEi | 6,052.92 at end-2025; 5,956.33 at end-Aug 2026; 5,743.21 on 5 Oct 2026[^pse-monthly-report-2026-08:2][^pse-composite-sector-frame] |

The three foreign issuers are Manulife Financial (MFC, PHP2,600 a share, 10 shares traded on 5 Oct), Sun Life Financial (SLF, PHP4,800, 105 shares) and Del Monte Pacific (DELM, PHP3.37, 26,000 shares); foreign issues averaged PHP1.56m a day in August.[^pse-sec-frames-snapshot][^pse-monthly-report-2026-08:1] They make up PHP5.1tn (27%) of "total" capitalisation at end-2025 and PHP6.8tn (34%) at end-Aug 2026, which is why the investable base is the domestic figure. ICT became the first PHP2tn stock (PHP2.01tn close on 14 Jul 2026).[^pse-press-icts-p2t]

| August 2026 average daily value (PHP m) | Aug | Year to date (162 days) |
|---|---|---|
| Total market | 7,525.03 | 7,561.17 |
| Regular market | 5,956.14 | 6,247.02 |
| Non-regular market (block, cross, other off-book) | 1,568.89 (20.8%) | 1,314.15 (17.4%) |
| Common | 7,501.17 | 7,528.79 |
| Preferred | 23.47 | 31.67 |
| Warrants and PDR | 0.35 | 0.65 |
| Dollar-denominated | 0.04 | 0.06 |
| SME Board | 1.41 | 24.35 |
| ETF | 0.93 | 1.33 |

Source: PSE Monthly Report, August 2026.[^pse-monthly-report-2026-08:1] By sector in August, average daily value was Services 2,096.53, Property 1,452.14, Industrial 1,407.98, Holding Firms 1,347.26, Financials 862.81 and Mining & Oil 355.98. The SME Board's year-to-date average sits far above its recent months (0.88 in July, 1.41 in August), so it reflects a few large days rather than a run rate (inference). Foreign participation and net flows are in [Chapter 14](#/ch/foreign-access) and [Chapter 15](#/ch/empirical).

**Concentration.** On 5 Oct 2026 total value was PHP3.74bn, of which ICT alone was PHP873m (23%) and BDO PHP190m; FMETF traded PHP0.84m, PREIT PHP0.15m and AGIW PHP5k.[^pse-composite-sector-frame][^pse-sec-frames-snapshot] That was a quiet day against the PHP7.5bn August average, but the shape is typical. Capitalisation structure, from summing the frames on 6 Oct:[^pse-sec-frames-snapshot]

| Measure | Value |
|---|---|
| All common lines | PHP19.10tn |
| Domestic (excluding MFC, SLF, DELM) | PHP12.12tn, of which PHP4.35tn (36%) is free-float adjusted |
| Top 10 and top 30 names | 45.8% and 72.4% of domestic capitalisation |
| Size bands | 1 stock at least PHP1tn (ICT, PHP1.74tn); 32 at least PHP100bn; 105 at least PHP10bn; 219 at least PHP1bn |
| Domestic by sector, PHP tn (free-float adjusted) | Industrial 2.91 (0.78), Services 2.84 (1.22), Financials 2.08 (0.86), Holding Firms 2.04 (0.79), Property 1.79 (0.57), Mining & Oil 0.44 (0.13), SME 0.016 (0.004) |
| Largest, PHP bn | ICT 1,736, SM 599, BDO 590, BPI 498, MER 469, SMPH 451, AP 328, AC 320, VLC 289 (suspended, stale price), MBT 275 |
| SME Board | about PHP16bn across nine issuers: XG 4.10bn, HTI 3.55bn, MM 3.30bn, CTS 2.27bn, LPC 0.65bn, X 0.56bn, MFIN 0.52bn, IDC 0.41bn, KPPI 0.28bn |

These sums include suspended issues at their last price, so they differ from PSE's published PHP13.06tn. A listing by introduction shows how fast a new line can concentrate flow: PNB Holdings (LTL) traded 73.8m shares (PHP88m, about 2.4% of the day's market value) on 5 Oct in a PHP1.20 stock, ten days after listing.

### Free float

PSE publishes issued, listed and outstanding shares, Free Float Level, market capitalisation (previous close times outstanding shares), board lot, par value and foreign limit in each security frame.[^pse-sec-frames-snapshot] Frame float for the 285 common lines:

| Free float | Lines | Free float | Lines |
|---|---|---|---|
| under 10% | 4 (MFC 0.20, SLF 0.62, MM 1.37, UNH 2.92) | 50 to 60% | 22 |
| 10 to 20% | 52 | 60 to 70% | 8 |
| 20 to 30% | 96 | 70 to 80% | 4 |
| 30 to 40% | 54 | 80 to 90% | 5 |
| 40 to 50% | 38 | 90 to 100% | 2 (SFI 99.71, EG 91.0) |

The median is 28.87% and the mean 32.5% (open-status names only: median 28.99%, with 42 of 256 open names under 20%).

<div class="callout warn">
<span class="label">Vintage of the Free Float Level field</span>

The frame shows no as-of date and no definition for Free Float Level, so it may not match the 2026 Revised Public Ownership Guidelines. Market capitalisation in the same table is current and new listings (MYNLD, LTL, TOP) carry current floats, but a name that has stopped reporting keeps its last value: MGH shows 10.67%, exactly the figure the press reported when it cured its MPO breach in Aug 2024, so floats for suspended or non-reporting names may be up to two years old.[^insiderph-2024-08-05-metro-global-avoids-delisting] The EPS fields in the same frames are stale as well (Dec 2023 on 319 frames, 9M-Sep 2024 on 341 of 387). Do not use the frame float as a time series, and do not infer MPO compliance from it.
</div>

**Float cushion against the in-force MPO** (open names, using the cohort tiers below). All 32 post-1 Dec 2017 listers sit at or above 20% except PNB Holdings (LTL, 15.39%), which is consistent with the 15% tier for a listing above PHP50bn (its market capitalisation is PHP56.3bn; the tier match is an inference because the field is undefined); several are pinned at the line: OGP 20.00, ASLAG 20.01, SPNEC 20.01, DMW 20.04, XG 21.14, REDC 22.31. Of 222 pre-Dec-2017 listers (10% rule), 183 are at or above 20%, and the thinnest are CHP 10.03, BH 10.16, MBC 10.23, PHC 10.40, TFHI 10.57, FDC 10.73, FB 11.23, PSB 11.61, FGEN 11.67 and BCOR 11.74. Suspended names with low floats: UNH 2.92 and MM 1.37 (both could be MPO cases; unverified), AAA 10.12, MGH 10.67, PORT 10.00, STR 10.30 and VLC 11.33. REIT floats are in the REIT table above (33.33% line).

### Execution implications

- Carry these fields per symbol: security type, currency, lot and tick regime (with the cut-over date), status (Open, Suspended, halted, Reservation), foreign-ownership limit and any A/B pairing, linked underlying (for automatic halts), eligible-broker flag (REIT, DDS), cohort MPO and last float cushion, listing date (for lock-up and over-allotment windows), and pending corporate-action flags.
- Build the tradable universe each morning from live status (65 suspended symbols), then filter by float. PSE's index free-float floor of 20% is a workable proxy for investable names ([Chapter 11](#/ch/market-data)).
- Do not build the instrument master from the listed-company directory table alone: on 6 Oct it still carried 11 symbol-less rows for securities already delisted (common ATI, 8990, Keppel Philippines A and B, RRHI, SFA Semicon; preferred CPGP and SMC2A to SMC2D) and 8 HTML template rows. Join it to the delisted-companies list and require a live security frame (status Open or Suspended) before admitting a symbol.[^pse-listed-company-directory-frame][^pse-delisted-companies-web]
- Size participation caps on per-name ADV, not market ADV: ICT alone was 23% of the day's value on 5 Oct, and the top 10 names are 46% of domestic capitalisation.
- Use domestic market capitalisation (PHP13.06tn at end-Aug 2026) as the investable base; MFC, SLF and DELM sit in PSE's "total" but trade almost nothing.
- Compute a float cushion (free float minus the cohort MPO of 10%, 20%, 15% or 33.33%) from POR filings, not from the frame. Names within a few points of the line with a pending tender offer or placement carry a suspension (zero-liquidity) tail risk.

## Listing rules that change how securities trade

### Minimum public ownership: the rule in force since 11 Aug 2026

PSE's memo of 11 Aug 2026 states that the SEC-approved Amended Rule on Minimum Public Ownership and the Revised Guidelines in Determining the Public Ownership of Listed Companies "shall take effect immediately"; the rule implements SEC MC 11 s.2026.[^pse-amended-mpo-rule-2026-08:1][^pse-amended-mpo-rule-2026-08:2]

| Cohort | Initial (IPO) | Maintaining |
|---|---|---|
| Listed before SEC MC 13-2017 (1 Dec 2017) | 10% | 10% |
| Listed after MC 13-2017, before MC 11-2026 | 20% | 20% |
| Listed after MC 11-2026, expected market capitalisation up to PHP500m | 33% | 20% |
| over PHP500m to PHP1bn | 25% (minimum offer PHP165m) | 20% |
| over PHP1bn to PHP50bn | 20% (minimum offer PHP250m) | 20% |
| over PHP50bn | 15% (minimum offer PHP10bn) | 15% |
| REIT | 33.33% | 33.33% |

The maintaining tier is keyed to market capitalisation at the time of listing, not current market capitalisation; the percentage is computed on issued and outstanding common shares, with preferred and treasury shares excluded; and PSE can change a percentage only with prior SEC approval.[^pse-amended-mpo-rule-2026-08:2][^pse-amended-mpo-rule-2026-08:3] **Large-issuer relief:** an issuer with expected market capitalisation of at least PHP200bn at listing may be endorsed for a lower MPO, never below 12% (and the maintaining level may not be lower than the approved initial level), on objective evidence that it would improve distribution and liquidity, full disclosure compliance with enhanced continuing disclosure, and liquidity safeguards.[^pse-amended-mpo-rule-2026-08:3][^pse-amended-mpo-rule-2026-08:4] Companies listed by introduction must show compliance at filing; backdoor-listed companies must comply immediately on completion.[^pse-amended-mpo-rule-2026-08:5][^pse-amended-mpo-rule-2026-08:6]

**Compliance mechanics and sanctions.**[^pse-amended-mpo-rule-2026-08:4][^pse-amended-mpo-rule-2026-08:5][^pse-amended-mpo-rule-2026-08:6][^pse-amended-mpo-rule-2026-08:7]

| Step | Rule |
|---|---|
| Monitoring | monthly internal float computation; immediate disclosure when float falls below the MPO (Art. VII Sec. 4.1, which means within 10 minutes of the issuer becoming aware)[^pse-listing-disclosure-rules:139] |
| Plan and cure | Compliance Plan within 10 days of the breach; restore compliance within 6 months of the breach |
| Reports | Public Ownership Report within 15 calendar days of each quarter-end; an interim report immediately after any transaction that pushes float below the MPO; float statement in the annual report |
| Sanction | immediate suspension of trading for up to 6 months from the date of breach; a Compliance Plan or pending corrective measures does not suspend or defer it; during the suspension the company may restore the float or petition for voluntary delisting |
| Outcome | still non-compliant at the end of the suspension means automatic delisting; the Involuntary Delisting procedure does not apply; the 5-year relisting prohibition applies, and directors and principal officers are disqualified from becoming directors or principal officers of any company applying for initial or additional listing in that period unless they show reasonable measures and due diligence |
| Voluntary route | a petition for voluntary delisting by reason of an MPO breach carries the same 5-year prohibition and officer disqualification; if a timely petition is pending for reasons beyond the company's control, PSE may defer the automatic delisting |
| Transition | companies already under monitoring or corrective action continue under the rules in force when they became non-compliant |

The 2026 text has no monthly-report trigger; the 2012 rule required a monthly report when float fell below 12%, and PSE's Aug 2023 consultation proposed 12%, 24% and 39.996% triggers by cohort that the 2026 text does not carry.[^pse-cn-2023-0041-mpo-delisting-consult:8] The consultation also explains why no grace period exists: BIR rules impose capital gains tax and documentary stamp tax on trading of shares of non-compliant companies, so PSE "is unable to grant a grace period and allow the continued trading" of such shares ([Chapter 12](#/ch/costs)).[^pse-cn-2023-0041-mpo-delisting-consult:9]

**What counts as public** (Revised Guidelines). Non-public: holders of 10% or more of outstanding common shares; any holder with a board seat; directors (including independent directors), principal officers and the chairman emeritus; the parent, subsidiaries, affiliates and associates; controlling shareholders; and employer-plan shares whether paid or not. Public: small individual holdings, Trading Participants (unless non-public), funds including SSS and GSIS **regardless of size unless the fund has a board seat**, shares lodged under the PCD Nominee account (classified as indirect holdings in the report), and underlying shares of PDRs and overseas depositary receipts. Only outstanding common shares count.[^pse-amended-mpo-rule-2026-08:9][^pse-amended-mpo-rule-2026-08:10][^pse-amended-mpo-rule-2026-08:11]

**History.**

| Effective | Rule | Initial | Maintain | Breach |
|---|---|---|---|---|
| 1 Jan 2012 | PSE Amended MPO Rule (SR 6; SEC approval 19 Dec 2011) | 10% | 10% at all times; quarterly report within 15 calendar days | non-compliant on or after 1 Jan 2013: suspension of up to 6 months, then automatic delisting; 5-year relisting ban; Involuntary Delisting Rules do not apply; voluntary delisting needed a tender offer reaching more than 90%[^pse-sr6-mpo-rule-2012:3][^pse-sr6-mpo-rule-2012:6][^pse-sr6-mpo-rule-2012:7] |
| Issued 1 Dec 2017 | SEC MC 13-2017 | 20% | 20% at all times; 12 months to cure | (SEC rule)[^pse-sr6-2-mpo-initial-backdoor-2020:3] |
| 3 Aug 2020 | PSE CN-2020-0076 (SR 6.2) | offer of 33% or PHP50m (to PHP500m), 25% or PHP100m (to PHP1bn), 20% or PHP250m (above), whichever higher; introduction and backdoor listings at least 20% | 20% | 2012 ladder continued[^pse-sr6-2-mpo-initial-backdoor-2020:4] |
| Mar 2025 (reported) | temporary IPO relief from 20% to 15% for 2 years, extendable, with a follow-on or placement within 2 to 3 years | 15% | | reported by the Daily Tribune; no PSE circular found; overtaken by the 2026 tiers[^tribune-pse-eases-float-2025] |
| 11 Aug 2026 | PSE Amended MPO Rule (SEC MC 11 s.2026) | tiers above | 20% (15% above PHP50bn) | immediate suspension, up to 6 months, then automatic delisting |

SEC MC 11 s.2026 was issued 24 Feb 2026 (per a law-firm summary; the SEC text was not retrievable). PSE's route to the final rule: consultation 13 May 2026 (comments to 20 May), submission to the SEC 25 May, SEC letter of 14 Jul approving with revisions, second exposure draft 16 Jul (comments to 21 Jul), effectivity 11 Aug.[^pse-cn-2026-0020-mpo-consult:1][^pse-mpo-second-exposure-2026-07:3][^cruzmarcelo-sec-mc11-2026] The IPO and maintenance tiers on PSE's IPO-requirements web page (20% minimum offering, PHP2m ALMF cap) are stale.[^pse-ipo-listing-requirements-web]

**Live MPO cases.** ATI and RRHI were handled under the pre-2026 text, whose suspend-then-delist ladder is identical (inference).

| Issuer | Event | Suspension | Outcome |
|---|---|---|---|
| ATI (Asian Terminals) | tender-offer results (177,612,478 shares) and a 31,721,200-share block crossed as special block sales at PHP36.00 on 13 Mar 2026 (PHP6.39bn plus PHP1.14bn, PHP7.54bn; the notice prints "3.60", but its transaction values imply 36.00); PSE announced the day before that a suspension would follow[^pse-tpa-2026-0012-block-sale-ati-tender-offer:1] | after the block execution on 13 Mar 2026 | voluntary delisting approved 25 Mar (CN-2026-0013), removed 3 Apr 2026: about 3 weeks suspended[^pse-cn-2026-0013-ati-voluntary-delisting:1] |
| RRHI (Robinsons Retail) | JE Holdings tender offer at PHP48.30, 25 May to 6 Jul 2026, took float to 0.31% (press)[^philstar-rrhi-suspension] | effective 13 Jul 2026; removed from the PSE DivY, MidCap and Services indices on 16 Jul (the DivY and MidCap indices fell to 19 constituents)[^pse-cn-2026-0032-rrhi-index-removal:1] | voluntary delisting approved 20 Aug (CN-2026-0038), delisted 31 Aug 2026: 7 weeks suspended[^pse-cn-2026-0038-rrhi-voluntary-delisting:1] |
| STN (Steniel) | non-compliant; PSE notice of 23 Oct 2023 | from 22 May 2023, automatic delisting due after 6 months[^pse-cn-2023-0058-steniel-mpo-non-compliance:1] | trades again (last PHP1.95, frame float 28.81%): cured[^pse-sec-frames-snapshot] |
| MGH (Metro Global) | non-compliant | from 5 Feb 2024, automatic delisting due 5 Aug 2024 (CN-2024-0037A)[^pse-cn-2024-0037a-metro-global-mpo-non-compliance:1] | its parent transferred 55m shares (about 2% of 2.75bn) to Smart Share Investments, lifting float to 10.67% (press); still Suspended on 6 Oct 2026, reason not verified |

<div class="callout">
<span class="label">Consequence</span>

The MPO rule is a hard liquidity-event generator. Any tender offer, placement or share transfer that pushes a name below its cohort line (10%, 20%, 15% or 33.33%) triggers an immediate suspension, not a cure period, and positions cannot be exited on-exchange until delisting or tender mechanics resolve. In the ATI case the tender-offer results were crossed as special block sales and the suspension was announced in the same PSE notice (block on Fri 13 Mar 2026, suspension straight after); RRHI's tender closed on 6 Jul and the stock was suspended from 13 Jul. The last on-exchange exit is the tender window itself.
</div>

### Lock-ups, stabilisation and IPO distribution

| Route | Who is locked | Period |
|---|---|---|
| Main Board IPO | existing holders of 10% or more | 180 days from listing (track-record issuers), 365 days (exempt: mining, oil, renewable energy, holding companies using a subsidiary's record)[^pse-listing-disclosure-rules:52][^pse-listing-disclosure-rules:53] |
| Main and SME IPO | any shares issued or transferred, or instruments leading to an issuance, within 180 days before the offer period at a price below the offer price | 365 days from full payment (SME: from listing); alternative investment funds exercising instruments held at least 365 days and selling in the IPO are exempt, with unsold shares locked 365 days[^pse-listing-disclosure-rules:53][^pse-listing-disclosure-rules:60] |
| SME IPO | non-public holders and related parties | 1 year from listing[^pse-listing-disclosure-rules:60] |
| REIT | see REIT table | 180 or 365 days (Main), 1 year (SME) |
| Preferred IPO | below-offer-price issuances in the prior 180 days | 365 days from full payment[^pse-cn-2026-0037-preferred-shares-rule-effectivity:4] |
| Listing by introduction where listing or an offer is mandated | holders of 10% or more | escrow from listing until 180 days after the public offering[^pse-listing-disclosure-rules:87] |
| Additional listing with a related-party rights-offer waiver | the subscriber | 180 days after listing of the subscribed shares[^pse-listing-disclosure-rules:104] |

The lock-up must be stated in the Articles. It is implemented by PDTC electronic lock-up or an escrow agreement with an independent institution acceptable to PSE (furnished at least 7 calendar days before the offer period); other arrangements are accepted only if 98% of locked holdings are escrowed and insiders and major holders are escrowed; a company moving from SME to Main gets credit for the SME lock-up served; and the issuer must notify PSE of a voluntary lock-up release not earlier than 15 and not later than 10 trading days before it ends.[^pse-listing-disclosure-rules:41][^pse-listing-disclosure-rules:42][^pse-listing-disclosure-rules:54][^pse-listing-disclosure-rules:148] A newly listed company may not offer additional securities (except stock dividends and employee option plans) within 180 days of listing, and a holding company relying on a subsidiary's track record cannot divest it for 3 years unless a majority of stockholders approve a divestment plan.[^pse-listing-disclosure-rules:54][^pse-listing-disclosure-rules:55]

**Stabilisation.** Article III Part A Sec. 13 (inserted by CN-2023-0022 of 12 May 2023, SEC-approved, effective immediately) requires an applicant conducting a secondary offering to hold a stabilisation fund: 10% to 15% of the base offer for offers up to PHP10bn, 12.5% to 15% for PHP10bn to PHP25bn and 15% above PHP25bn (on a PHP20bn base offer, PHP2.5bn to PHP3.0bn). Stabilisation may not breach the MPO, the stabilising agent reports weekly, and SEC prior approval is required.[^pse-cn-2023-0022-stabilization-fund:1][^pse-cn-2023-0022-stabilization-fund:2][^pse-listing-disclosure-rules:38][^pse-listing-disclosure-rules:39] Over-allotment options appear in recent deals: Maynilad had up to 249.05m primary over-allotment shares, and Mynt (GCASH) has up to 1.20bn secondary ones.[^pse-press-maynilad-greenlight][^pse-press-mynt-ipo-approval]

**Distribution of IPO shares** (Art. III Part F; LSI terms as amended 13 Jun 2022): book-building for up to 60% of the offer with qualified institutional buyers; local small investor (LSI) tranche of at least 10% (subscription up to PHP100,000 per investor, clawed back to 15% when LSI demand is at least five times the allocation, balloted if exceeded); the balance of at least 30% to the general public, of which 20% of the offer shares is sold through Trading Participants; offer period of at least 5 trading days; listing within 10 calendar days of the end of the offer period; LSIs subscribe through PSE EASy.[^pse-listing-disclosure-rules:77][^pse-listing-disclosure-rules:78][^pse-listing-disclosure-rules:79][^pse-listing-disclosure-rules:80]

**First-day price limits.** No IPO-specific limit rule was found. New securities start with the 20% dynamic threshold; if an IPO does not trade on listing day, the next day's static threshold is based on the company's indicative reference opening price; the static band is +50% and −30% of the reference price except for warrants and a listing-by-introduction listing day.[^pse-implementing-guidelines-trading-rules:11][^pse-cn-2020-0028:1][^pse-revised-trading-rules:34] Whether the offer price is the day-1 reference is not stated in the archived text; a press report that Medilines' PHP2.30 IPO "tanked 30%" on its 7 Dec 2021 debut is consistent with the −30% floor measured from the offer price.[^philstar-2021-12-07-medilines-debut] Price-limit detail is in [Chapter 7](#/ch/price-controls).

**Listing by way of introduction (LBWI).** Allowed, for example, where an unlisted issuer's shares are distributed as a property dividend by a listed issuer; the initial price is set with a fairness opinion; the trading band is lifted on the listing date and reinstated afterwards; and mandated or closely held cases must make a public offering within 1 year or face suspension, ALMF doubling, or a buy-back and delisting.[^pse-listing-disclosure-rules:83][^pse-listing-disclosure-rules:84][^pse-listing-disclosure-rules:87][^pse-listing-disclosure-rules:88] PNB Holdings (LTL) listed 46.93bn shares on 25 Sep 2026 at PHP1.20, 23.9bn of them distributed as a property dividend by PNB.[^pse-press-pnb-holdings-lbwi]

### Follow-ons, rights and additional listing

- **Follow-on offerings** (Art. V Part F; amendments of CN-2024-0024, 16 Apr 2024): offer-price range with a floor at or below the market price disclosed at filing; LSI allocation mandatory; offer period at least 5 trading days; shares issued at a discount in the prior 180 days cannot be sold in the offer.[^pse-listing-disclosure-rules:124][^pse-listing-disclosure-rules:125]
- **Stock rights offerings** (Art. V Part B): file within 90 days of board approval with a price range (floor at or below market); an underwriter takes up unexercised rights after the second round; the record date is at least 15 trading days after PSE board approval; the offer period starts within 30 calendar days of the record date.[^pse-listing-disclosure-rules:106][^pse-listing-disclosure-rules:107] Rights are not listed as separate securities: no rights ticker appears in the directory and the rules have no rights-trading provision (absence of evidence). Recent rights offerings include Globe (28 Oct 2022), PBB (31 Mar 2023), UnionBank (31 May 2024) and Phinma (27 Nov 2024).[^pse-new-listings-ipo-web]
- **Additional listing** (Art. V Part A; private placements and swaps of 10% to 35% of resulting capital, single or creeping within 12 months): a **1-hour trading halt** on announcement of the information leading to the transaction and a second 1-hour halt on dissemination of the Comprehensive Corporate Disclosure (due within 5 trading days); subscription by related parties needs a prior rights or public offer unless the price is a premium to the 30-trading-day weighted close, the minority waives by majority vote, or the issuer is in rehabilitation.[^pse-listing-disclosure-rules:98][^pse-listing-disclosure-rules:99][^pse-listing-disclosure-rules:100][^pse-listing-disclosure-rules:101] Live example: on 19 Jan 2026 MRC Allied disclosed approval of 315,000,000 additional shares at PHP1.00 to two named subscribers and PSE halted the stock from 9:30 to 10:30 am.[^pse-cn-2026-0004-2-emergency-disclosures-trading-halt:2] Lodging or trading unlisted shares draws a fine of 15% of market value plus PHP2,000 a day, or PHP5m if higher.[^pse-listing-disclosure-rules:105]
- **Listing deadlines for newly issued shares** (SR 20 = CN-2023-0012 of 21 Mar 2023, SEC-approved, effective on posting): every issued and outstanding share of a listed class, including treasury shares, must be listed; the periods are non-extendible.[^pse-sr20-listing-issued-outstanding-shares-2023:1][^pse-sr20-listing-issued-outstanding-shares-2023:2]

| Transaction | Deadline to file the listing application |
|---|---|
| Private placement and share swap | 60 calendar days from full payment (full payment within 1 year of subscription or closing) |
| Stock dividend | 60 calendar days from stockholders' approval (or SEC approval of the capital increase) |
| Stock rights offering | 90 calendar days from board approval |
| Conversion or exercise of convertibles | 60 calendar days |
| ESOP or ESPP shares | 60 calendar days from issuance and full payment |

Source: SR 20, Annex A.[^pse-sr20-listing-issued-outstanding-shares-2023:2][^pse-sr20-listing-issued-outstanding-shares-2023:3] Penalties per violation in a rolling five-year window are PHP100k, PHP200k, PHP300k and PHP500k, then a **2-month trading suspension** on the fifth and delisting grounds thereafter, plus PHP2,000 per trading day until the application is filed; after approval the issuer has 60 days (extendible by 30) to meet the Notice-of-Approval conditions or the approval lapses.[^pse-sr20-listing-issued-outstanding-shares-2023:3][^pse-sr20-listing-issued-outstanding-shares-2023:4] Shares issued in placements or as stock dividends can therefore stay unlisted, and untradable, for weeks to months after issue, and share-count and float changes show up in PSE data with a lag (inference).

<div class="callout warn">
<span class="label">Currency: ex-date text in the consolidated rules is stale</span>

The January 2025 consolidated rules still say that PSE sets the ex-date "three (3) Trading Days before the announced record date" for rights offerings (T+3-era wording). Since the move to T+2 on trade date 24 Aug 2023, the ex-rights date is **one trading day before the disclosed record date** (CN-2023-0031), and ex-dates of already-announced actions were re-set by amended disclosures.[^pse-listing-disclosure-rules:107][^pse-cn-2023-0031-t2-settlement:1][^pse-cn-2023-0040-t2-go-live:1] Illustration: for a record date of Thu 15 Oct 2026 the ex-date is Wed 14 Oct and the last cum-date is Tue 13 Oct, whereas the stale text would give ex-date Mon 12 Oct (three trading days before). PSE's per-event notice is authoritative; conventions are in [Chapter 10](#/ch/clearing-settlement).
</div>

Dividend disclosure timing sits alongside: a record date must be disclosed at least 10 trading days ahead, payment may not be more than 18 trading days after the record date, and under SEC MC 2 s.2009 the record date of a cash dividend must fall not less than 10 nor more than 30 days after declaration (15 days if unspecified).[^pse-listing-disclosure-rules:146][^pse-listing-disclosure-rules:147][^pse-gn19-sec-mc-2-2009-rights-dividends:1]

### Delisting, tender offers and backdoor listing

**Involuntary delisting** (Supplemental Rule 8). Grounds include non-compliance with the Listing Agreement or rules despite notice, a false market attributable to the issuer, incapacity to continue the business, liquidation or dissolution (an announced or filed insolvency proceeding merits immediate suspension), negative stockholders' equity (on the Main and SME rules, three consecutive years, effective 30 days after Board approval), revoked registration, retirement of an entire listed class, repeated disclosure failures, and not being in commercial operation within 2 years of listing. The issuer may request a hearing within 15 working days of notice, has one motion for reconsideration, and a company delisted this way cannot relist for 5 years; its directors and executive officers are disqualified for the same period.[^pse-sr8-delisting-rules:1][^pse-sr8-delisting-rules:2][^pse-sr8-delisting-rules:3][^pse-sr8-delisting-rules:4][^pse-listing-disclosure-rules:56][^pse-listing-disclosure-rules:63]

**Voluntary delisting** (Supplemental Rule 8.1, effective 21 Dec 2020):[^pse-sr8-1-voluntary-delisting-2020:1][^pse-sr8-1-voluntary-delisting-2020:3][^pse-sr8-1-voluntary-delisting-2020:4]

| Requirement | Rule |
|---|---|
| Eligibility | not available once involuntary proceedings have started |
| Approval | at least two-thirds of the entire board, including a majority (and at least two) of the independent directors, and holders of at least two-thirds of outstanding and listed shares, with votes against not above 10% |
| Timing | petition and tender-offer report filed at least 60 days before the delisting takes effect |
| Tender offer | to all holders of record; minimum price is the higher of the highest valuation in an independent fairness opinion (SRC Rule 19.2.6) and the 1-year VWAP before the board-approval disclosure; if the stock has been suspended for a year or more, the fairness-opinion value only |
| Ownership | proponents must reach at least 95% of issued and outstanding shares (and still tender to the rest if they already hold 95%) |
| Other | no unpaid fees or penalties; voluntary delisting fee equal to one ALMF; a later relisting is a new listing and the involuntary 5-year ban does not apply, **except** that a voluntary delisting approved because of an MPO breach carries the 5-year ban and officer disqualification |

The 2012 MPO rule set a lower tender threshold for MPO-driven voluntary delistings (more than 90% of issued shares, or a level aligned with the minimum float). Which threshold governs MPO petitions today is not stated: the 2026 rule points to "the Amended Voluntary Delisting Rules", and RRHI's float of 0.31% after its tender offer cleared either.[^pse-sr6-mpo-rule-2012:3][^pse-amended-mpo-rule-2026-08:6] PSE proposed changes in Aug 2023 (two-thirds vote on *issued* rather than outstanding-and-listed shares, replacing the 95% test with an MPO-aligned test, a mandatory tender offer); adoption is unconfirmed and PSE's site still shows SR 8.1 as the latest text.[^pse-cn-2023-0041-mpo-delisting-consult:14] ETFs and REITs have their own delisting tender rules (more than 90% for an ETF; a mandatory tender offer for any REIT delisting).[^pse-sr11-etf-rules-2026:13][^pse-sr3-2-reit-listing-amend-2023:10]

**Backdoor listing** (Supplemental Rule 7, CN-2022-0026 of 22 Jun 2022). A backdoor listing is deemed to occur when a listed company acquires shares or assets of an unlisted party (or the reverse) resulting in a change of control (more than 50% of voting power), a change in de facto control (the acquirer becomes the single largest substantial shareholder) or a substantial change in business (acquired business or assets above 50% of total assets). PSE suspends trading immediately after evaluating the disclosure and lifts the suspension one full trading day after it disseminates the comprehensive corporate disclosure (and any SEC confirmations); a one-hour halt accompanies disclosure of the final price of the mandatory follow-on offering; the maintaining MPO must be met immediately on completion of the transaction (20% under the 2020 guidelines).[^pse-sr7-backdoor-listing-2022:3][^pse-sr7-backdoor-listing-2022:4][^pse-amended-mpo-rule-2026-08:6][^pse-sr6-2-mpo-initial-backdoor-2020:4]

### The suspension ladder

| Trigger | Consequence | Source |
|---|---|---|
| Material information not yet disclosed | issuer must disclose within 10 minutes and, if inside trading hours, request a halt; the halt lifts 1 hour after dissemination (next trading day if disseminated within an hour of the close) | CLDR Art. VII Sec. 4.1[^pse-listing-disclosure-rules:139][^pse-listing-disclosure-rules:140] |
| Rumour clarification requested by PSE, no reply | halt until 10:00 am; reply due by 11:00 am or fine of PHP30,000 plus PHP10,000 per 30 minutes | Sec. 4.5[^pse-listing-disclosure-rules:145][^pse-listing-disclosure-rules:146] |
| Acquisition of an unlisted company worth 10% or more of the issuer's book value | suspension until terms are disclosed | Sec. 5[^pse-listing-disclosure-rules:146] |
| Failure to appoint a replacement transfer agent 10 trading days before termination | suspension until a new agent is notified | Sec. 12[^pse-listing-disclosure-rules:148] |
| Annual report (17-A) late; due 105 days after fiscal year-end | basic fine, 15 calendar days of daily fines, a warning, then **automatic suspension for up to 3 months** (no daily fines during it), then delisting procedures | Sec. 17[^pse-listing-disclosure-rules:153][^pse-listing-disclosure-rules:154] |
| Quarterly report (17-Q) late; due 45 days after quarter-end | basic fine, 10 days of daily fines, then **suspension for up to 2 months**, then delisting procedures | Sec. 17[^pse-listing-disclosure-rules:154][^pse-listing-disclosure-rules:155] |
| ALMF unpaid after 15 Feb | automatic 2-month suspension (to 15 Apr), then delisting consideration | PSE IPO page[^pse-ipo-listing-requirements-web] |
| Listing-application deadline missed (SR 20) | fifth violation in 5 years: 2-month suspension | SR 20[^pse-sr20-listing-issued-outstanding-shares-2023:3] |
| Public float below MPO | immediate suspension up to 6 months, then automatic delisting | MPO rule[^pse-amended-mpo-rule-2026-08:6] |
| REIT public-ownership failure | suspension up to 6 months, then automatic delisting | SR 3.2[^pse-sr3-2-reit-listing-amend-2023:7] |
| SME sponsor ends with no replacement | suspension at 3 months, automatic delisting at 6 months | Part E-1[^pse-listing-disclosure-rules:74] |
| Backdoor listing detected | immediate suspension until 1 full trading day after the comprehensive disclosure | SR 7[^pse-sr7-backdoor-listing-2022:4] |
| Direct-listed preferred misses the PHP50m / 100-investor distribution | PSE may suspend, double the ALMF, or require a buy-back within 90 days and delist | CN-2026-0037[^pse-cn-2026-0037-preferred-shares-rule-effectivity:6] |
| ETF: underlying 20% or more suspended, no Market Maker for a month, SEC order | suspension; 1-hour halts for tracking error, delisted underlying, late iNAV | SR 11[^pse-sr11-etf-rules-2026:12][^pse-sr11-etf-rules-2026:13] |
| Class A/B declassification | 2-trading-day suspension before delisting of the classified shares | CN-2026-0041[^pse-cn-2026-0041-declassification-price-suspension:1] |
| Underlying halted or suspended | automatic halt or suspension of warrants, PDRs and other derived securities | Trading Rules Art. VII[^pse-revised-trading-rules:34] |

<div class="callout warn">
<span class="label">Currency: the Villar-group suspensions have outlived the 3-month ceiling</span>

Eleven symbols show last data on 29 May 2026 (INFRA, VLC, VLL2A) or 1 Jun 2026 (ALLDY, HOME, MM, STR, T, VLL, VLL2B, VREIT) and were still Suspended on 6 Oct 2026; Petron PRF3B also stopped on 1 Jun and UNH on 22 May.[^pse-sec-frames-snapshot] The Villar-group attribution is an inference from issuer names, except that PSE removed VLL and VREIT (Property) and ALLDY and HOME (Services) from the sector indices effective 3 Aug 2026.[^pse-cn-2026-0035:1] The press reported six of seven Villar-listed companies (about PHP320bn) suspended for nearly three months over overdue financial filings, with second-quarter reports also late.[^insiderph-villar-frozen] The CLDR's 3-month ceiling would have expired around end-Aug to Sep; more than four months on, the outcome or any extension is not in the public record.
</div>

Other long suspensions on the frames: AAA (since May 2015), PORT (May 2014), FBP (Feb 2015), ACPA (Nov 2013) and SMCP1 (Oct 2012).[^pse-sec-frames-snapshot] A security suspended for a year or more has its static threshold lifted on the resumption day.[^pse-revised-trading-rules:34]

<div class="callout infer">
<span class="label">Inference</span>

Late-filing suspensions cluster in mid and late May. Last-trade dates of today's suspended common names fall on 15 to 16 May (PORT 2014, AAA 2015, MJC 2023, PNX 2024, I-Remit 2025) and 20 May (ROX 2024), and the 2026 stoppages came a little later (UNH 22 May; INFRA and VLC 29 May; the other Villar names 1 Jun). That fits the ladder for December year-ends: a 17-A due on day 105 (15 Apr), 15 days of fines to 30 Apr, a warning circular, then automatic suspension. PSE's per-case suspension notices were not retrieved, so treat mid-May as a risk window for names that have not filed by 15 Apr, not as a rule.
</div>

### Execution implications

- Screen for event risk with the float cushion. Where a tender offer or placement could take a name below its cohort line, assume suspension (zero liquidity) rather than a drift. Resolve positions in names with a live tender offer before the offer expires: tender, hedge through securities lending where borrowable ([Chapter 9](#/ch/short-selling)), or sell.
- Use RD−1 for rights and dividend ex-dates since 24 Aug 2023, and take the actual ex-date from PSE's per-event notice; the last cum-date is two trading days before the record date. Cum and ex adjustments are applied to the reference price (last adjusted closing price).
- A listing by introduction is not bounded by the static band on its listing day, so expect extreme volume and gap risk (LTL traded 73.8m shares on 5 Oct).
- Event feeds: PSE's EDGE disclosure cut-off was 3:30 pm until 22 May 2026 and is **4:00 pm since 25 May 2026** (CN-2026-0024), and the consolidated rules still print 3:30 pm;[^pse-cn-2026-0024-edge-cutoff-4pm:1][^pse-listing-disclosure-rules:139] EDGE itself was unavailable on 6 Oct 2026, with PSE directing the public to pse.com.ph.[^pse-cn-2026-0046-edge-outage-access-to-disclosures:1] Do not rely on a single EDGE scraper for halt and suspension triggers ([Chapter 11](#/ch/market-data), [Chapter 13](#/ch/regulatory-constraints)).
- IPO and placement supply is predictable: put lock-up expiries (listing date plus 180 or 365 days), over-allotment windows and unlisted-share backlogs on the event calendar.

## IPO pipeline, 2020 to 2026

IPO activity fell from 8 to 10 a year (2021 and 2022) to 2 or 3 a year (2023 to 2025), then returned in value terms: Maynilad raised PHP34.34bn on 7 Nov 2025, the second-largest IPO on record, and Mynt (GCASH, about PHP92bn) would be the largest.[^pse-press-maynilad-ipo] The first half of 2026 had no IPO; capital raising was follow-on and preferred led.

| Year | IPOs and listings by introduction (LBWI) | New issuers | Delistings (issuers) |
|---|---|---|---|
| 2020 | Altus Property (APVI, LBWI, SME, 26 Jun); MerryMart (MM, SME, 15 Jun as printed on PSE's page); AREIT (13 Aug; PHP12.34bn);[^pse-press-areit-debut] Converge (CNVRG, 26 Oct; PHP29.08bn incl. over-allotment, then the largest)[^pse-press-converge-ipo] | 4 | 1: Pepsi-Cola Products Philippines (voluntary) |
| 2021 | DDMPR (24 Mar); Monde Nissin (MONDE, 1 Jun; PHP55.89bn, the largest IPO in PSE history);[^pse-press-monde-ipo] FILRT (12 Aug; PHP12.58bn); RCR (14 Sep; PHP23.53bn); MREIT (1 Oct; PHP15.29bn, about 2 times covered); AllDay Marts (ALLDY, 3 Nov; PHP4.5bn, LSI tranche 1.62 times); Medilines (7 Dec); SP New Energy (SPNEC, 17 Dec; PHP2.7bn) | 8 | 3: Primetown and Export & Industry Bank (involuntary), Cebu Property Ventures (merger) |
| 2022 | Haus Talk (HTI, SME, 17 Jan; PHP0.75bn); Figaro (24 Jan); CREIT (22 Feb; PHP6.40bn); Bank of Commerce (BNCOM, 31 Mar; PHP3.36bn); CTS Global (CTS, SME, 13 Apr; PHP1.375bn); Raslag (ASLAG, 6 Jun; PHP0.70bn); VistaREIT (VREIT, 15 Jun; 7.5bn shares, smallest REIT by capital raised); Balai ni Fruitas (30 Jun); LFM Properties (LPC, LBWI, 9 Nov); Premiere Island Power REIT (PREIT, 15 Dec) | 10 | 0 |
| 2023 | Alternergy (24 Mar; PHP1.62bn); Upson (3 Apr; PHP1.50bn plus PHP0.15bn secondary over-allotment); Repower (REDC, 24 Jul; PHP1.05bn) | 3 | 6: Eagle Cement, 2GO, MPIC, Holcim Philippines (voluntary); Unioil, PICOP (involuntary) |
| 2024 | OceanaGold Philippines (OGP, 13 May; PHP6.08bn, secondary); Citicore Renewable (7 Jun; PHP5.30bn incl. US$12.5m from MOBILIST); NexGen Energy (SME, 16 Jul; PHP0.504bn) | 3 | 3: Cebu Holdings (merger); Premium Leisure, SFA Semicon (voluntary) |
| 2025 | Top Line Business Development (TOP, 8 Apr; PHP0.733bn); Maynilad (MYNLD, 7 Nov; PHP34.34bn, primary shares, ADB and IFC US$245m cornerstone, the SEC's first "Philippine Green Equity" label) | 2 | 3: Keppel Philippines A/B, 8990 Holdings (voluntary); Philab (involuntary) |
| 2026 to 6 Oct | PNB Holdings (LTL, LBWI, 25 Sep) | 1 | 3: Asian Terminals (3 Apr), City & Land Developers (merger, 6 Jul), Robinsons Retail (31 Aug) |

Sources: PSE's new-listings page (through 8 Apr 2025), the PSE press releases for each deal, and the delisted-companies list.[^pse-new-listings-ipo-web][^pse-delisted-companies-web] That is 31 new issuers (28 IPOs and 3 LBWIs: APVI, LPC, LTL) against 19 delisted (11 voluntary, 5 involuntary, 3 mergers), and the roll-forward from PSE's 2021 count of 276 ties to 280 on 6 Oct 2026. PSE's statistics table counts 4 SME listings in 2022 while its IPO page tags differently (VREIT and PREIT as SME): the classification differences are unresolved. Preferred and warrant retirements (SMC2A to SMC2D on 1 Oct 2025, CPGP on 11 Jun 2025, ALCPB and ALCPC on 11 Nov 2024, Cirtek TECHW on 19 Aug 2024) are not counted.

| Year | Capital raised (PHP bn) | Composition |
|---|---|---|
| 2020 | 103.76 | not itemised in the releases found |
| 2021 | 234.48 | 1H21 122.46, including Monde Nissin |
| 2022 | 110.29 | nine IPOs, one LBWI, five stock rights offerings and 12 private placements; 1H22 61.92 (eight IPOs, one rights offering, four placements) |
| 2023 | 140.95 | not itemised in the releases found |
| 2024 | 82.37 | IPO 11.91; follow-on 47.08; private placement 12.38; rights 11.00 |
| 2025 | 144.13 | IPO 35.07; follow-on 67.29; private placement 40.67; about 1.1 other (AGI warrants) |
| 6M 2026 | 39.43 | no IPO; follow-on 26.50; private placement 12.93 |

Sources: PSE year-end and half-year releases and the 4 Jul 2026 President's Report.[^pse-asm-2026-president-report:8][^pse-press-1h2021-capital][^pse-press-last-trading-day-2022][^pse-press-psei-6-5k-2024][^pse-press-1h22-ipos][^pse-press-last-trading-day-2025] PSE's own 2025 count was 2 IPOs, 8 follow-ons and 14 private placements, +75.0% year on year.[^pse-press-last-trading-day-2025] The 6M26 totals are exactly the completed follow-on offerings (Globe Telecom PHP25bn on 2 Mar, Top Line PHP1.5bn on 26 Jun) and private placements (Italpinas PHP187.93m on 6 Jan, Citicore Renewable PHP6.70bn on 13 Jan, EEI PHP6bn on 24 Feb, Prime Media PHP44.25m on 11 Mar) on PSE's 13 Aug 2026 list.[^pse-analyst-briefing-1h-2026:13]

**Forthcoming (PSE, 4 Jul and 17 Aug 2026).** The 4 Jul list totalled about PHP164.2bn; the 17 Aug list (as of 13 Aug) about PHP133.70bn: stock rights offering by LFM Properties (about PHP1.2bn, 21 Sep), listing by introduction of PNB Holdings (about PHP56bn of market capitalisation, 25 Sep), IPOs of Vitro REIT (about PHP24.19bn, 12 Oct) and Mynt (about PHP92.31bn, 19 Oct), follow-on offering by Arthaland (about PHP3bn, 25 Sep; completed 2 Oct at PHP2.15bn), and private placements by SteelAsia (about PHP9bn) and EEI (about PHP4bn), dates to be determined.[^pse-asm-2026-president-report:8][^pse-analyst-briefing-1h-2026:13] San Miguel's PHP30bn follow-on listed 3 Aug.

<div class="callout warn">
<span class="label">Conflict: Mynt listing date</span>

PSE's 4 Jul 2026 and 17 Aug 2026 decks give 19 Oct 2026; PSE's 18 Sep 2026 approval release gives a tentative listing of 20 Oct 2026. Use the later, dated PSE release (20 Oct) and re-check against the final prospectus calendar. Terms per the release: up to 1.61bn primary and up to 6.42bn secondary shares (8.03bn) plus an over-allotment of up to 1.20bn secondary shares, at up to PHP10.00 (9.23bn shares at the cap is about PHP92.3bn, which matches the headline size); final price set on 1 Oct after book-building, offer period 6 to 12 Oct, Main Board, symbol GCASH, LSIs through PSE EASy.[^pse-press-mynt-ipo-approval][^pse-asm-2026-president-report:8] The outcome was not known on 6 Oct 2026.
</div>

PSE's Listing Engagement and Assistance Program (LEAP, launched 2020 per PSE's 2026 decks; the FY2025 annual report says 2021) had 24 companies on its roster on 4 Jul and 25 on 17 Aug 2026, four of them "ready and preparing for their IPO next year", and four participants have already listed.[^pse-asm-2026-president-report:20][^pse-analyst-briefing-1h-2026:15][^pse-annual-report-2025:29]

### Execution implications

- IPO weeks carry predictable supply. The LSI tranche, the over-allotment and stabilisation window, and lock-up expiries are all dated from the listing date. Maynilad's 180-day window ended about 6 May 2026 (listed 7 Nov 2025). If a 180-day lock-up applies, Vitro REIT's would end about 10 Apr 2027 (listing 12 Oct 2026) and Mynt's about 18 Apr 2027 (listing 20 Oct 2026); a 365-day case runs to 12 Oct and 20 Oct 2027. Which period binds depends on each prospectus.
- A very large IPO is also an index-inclusion event (Maynilad entered the PSEi on 3 Aug 2026 under the early-inclusion rule); flows are in [Chapter 11](#/ch/market-data).
- Mynt alone, at about PHP92bn, is roughly 64% of the PHP144bn raised in all of 2025 (arithmetic): the market is bimodal, a few large institution-and-cornerstone deals and little mid-cap flow, with retail LSI tranches a design feature of large deals.

## Planned products and rule changes

PSE's own status board (17 Aug 2026 briefing, the latest dated status found) and the 4 Jul 2026 President's Report give the position below.[^pse-analyst-briefing-1h-2026:9][^pse-analyst-briefing-1h-2026:10][^pse-analyst-briefing-1h-2026:16][^pse-asm-2026-president-report:22][^pse-asm-2026-president-report:24] Since January 2026 the in-force changes are rule-level only (REIT framework 25 Jan, MPO 11 Aug, preferred listing 12 Aug, Class A/B declassification); no new tradable product type has launched in 2026. The master pipeline table is in [Chapter 17](#/ch/reform-timeline); hedging through securities lending and short sales is in [Chapter 9](#/ch/short-selling).

| Item | Status (6 Oct 2026) | Detail and slippage |
|---|---|---|
| One Lot One Share (lot = 1, new tick table, odd-lot market removed) | "For SEC Approval"; targeted Q4 2026 with the new engine (go-live planned Mon 23 Nov) | CN-2025-0046 (15 Dec 2025; comments to 31 Dec): one-share lots for PHP and US$ securities; TPs may impose a minimum order value as a condition of accepting orders, provided they do not exceed the maximum commission rate allowed by law.[^pse-cn-2025-0046-board-lot-trading-at-last:3] A 2023 predecessor (CN-2023-0051, 9 Oct 2023) cut the maximum lot from 1,000,000 to 20,000 and the minimum from 5 to 1, to allow a PHP100 minimum investment; PSE reported it "awaiting SEC approval" in Jul 2024 and no approval was ever announced.[^pse-cn-2023-0051:3][^pse-asm-2024-presidents-report:18] |
| Fractional trading | listed as an initiative in 2023; no later phase found | PSE's 2023 President's Report lists "Fractional Trading" in its Pipeline of Initiatives: letting an investor buy partial shares and trade by peso value instead of number of shares, with "Phase 1 to focus on amendment of board lot structure".[^pse-asm-2023-presidents-report:40] The board-lot amendment it describes was first filed in 2023 and is now One Lot One Share, so One Lot One Share is in effect Phase 1 of that initiative (inference from the wording). No later phase, rule draft or date was found in the 2024 to 2026 reports, the 2026 decks or PSE's circular index. |
| Negotiated Trades | "Revising per Public Comments" | CN-2026-0031 (1 Jul 2026; comments to 7 Jul): a variant of the block-sale framework for smaller pre-arranged trades outside the best bid and offer.[^pse-cn-2026-0031-negotiated-trades:3] Design shown to brokers on 9 Jul: price within ±5% of the full-day VWAP (4 decimals), no volume or value limit, execution window 15 minutes after the run-off, one-firm trades only, web-based like the VWAP facility; reported through the feed as news and included in value and the consolidated trade file.[^pse-nte-broker-forum-2026-07-09:8][^pse-nte-faq-2026-08:1][^pse-nte-faq-2026-08:2] |
| New trading engine | big bang 23 Nov 2026; no parallel run | Certification 10 to 23 Sep, pre-production testing 12 to 22 Oct, Saturday rehearsals 31 Oct, 7 Nov and 14 Nov; day 1 limit orders only; 40 TPs run their own front ends and had to certify;[^pse-nte-broker-forum-2026-07-09:5][^pse-nte-broker-forum-2026-07-09:9] press reported a cost of PHP241.03m for the engine and PHP45.83m for the back office.[^philstar-nte-november] The run-off change (all run-off orders entered, modified and executed only at the closing price) is in [Chapter 6](#/ch/auctions).[^pse-nte-user-group-2026-01-15:11] |
| GPDR | revised rules with the SEC since 24 Jun 2026 | Approval "targeted within the quarter" (Q3 2026) has elapsed with no notice found. Slippage: "Target Launch: 2025" (Jul 2024 report), Q1 2025 (BusinessWorld, Oct 2024), rules filed with the SEC Jan 2025, SEC comments 26 May 2025, revised rules filed 24 Jun 2026; the FY2025 annual report aimed for a ready GPDR issuer in 2H 2026.[^pse-asm-2024-presidents-report:25][^bworld-2024-10-23-gpdr-derivatives-targets][^pse-asm-2025-presidents-report:30][^pse-annual-report-2025:38] |
| Market-making framework (GPDR and ETF annexes) | "Revising per Public Comments" | Released 4 Jun 2026, comments to 23 Jun; may extend to stocks later ([Chapter 8](#/ch/market-making)).[^pse-press-market-making][^pse-asm-2026-president-report:23] |
| ETF rule amendments | "Revising per Public Comments" | CN-2026-0029 (see the ETF section). |
| Structured warrants | SEC draft out for comment; PSE aligning its rules and sounding out issuers | SEC comments closed 13 May 2026; no date.[^pse-cn-2026-0018:1] |
| Derivatives (PSEi index futures first) | early exposure draft; vendor RFI issued July 2026; talks with multilaterals on funding | PSE says the new engine will "facilitate the introduction of new financial instruments, such as derivatives".[^pse-nte-page-web] Slipped: "Target Launch: 2026" (Jul 2024 report), "first derivatives in 2026" (FOW, Aug 2024), Q1 2026 (BusinessWorld, Oct 2024); the Q1 2026 target was missed. Groundwork: MOUs with Taiwan exchanges and study visits to TAIFEX, TPEx and TWSE on 15 to 18 Dec 2025. The FY2025 annual report said the derivatives rules were "slated to be finalized" in 2H 2026; no launch date, SEC rule or clearing house is in the sources found.[^pse-analyst-briefing-1h-2026:10][^pse-annual-report-2025:29][^pse-annual-report-2025:38][^fow-pse-derivatives-2026] |
| Preferred-share listing; MPO | **in force** (SEC Approved) | 12 Aug and 11 Aug 2026 (above). |
| SME sponsor model | "Ongoing Review" | An SME sponsor-model consultation of 28 Aug 2026 appears in PSE's announcement index under CN-2026-0041, the same number the 10 Sep 2026 declassification memo carries.[^pse-web-announcements-archive] |
| Revised SBL rules | awaiting SEC approval | Revised rules with directed pooled lending were filed with the SEC on 16 Apr 2026; PDTC's lending agency service went live in Apr and May 2026 ([Chapter 9](#/ch/short-selling)).[^pse-press-additional-reforms][^pse-asm-2026-president-report:22] |

### Execution implications

- Plan for a regime change on 23 Nov 2026 (planned, not confirmed): lot = 1, a new tick table, no odd-lot book, a revised trading-at-last rule and new FIX and ITCH endpoints. Freeze strategy-parameter changes around the cut-over and make lot and tick logic data-driven ([Chapter 16](#/ch/execution-implications)).
- Only limit orders are supported on day 1 and there is no parallel run, so algorithms that rely on market, market-on-open or market-on-close orders need a day-1 fallback.[^pse-nte-faq-2026-08:1]
- Even if One Lot One Share is approved, the smallest tradable unit is one whole share; no peso-amount or fractional-share design has been published, so do not build for sub-share quantities.
- Derivatives, GPDRs and structured warrants are not tradable in 2026 for planning purposes: hedging means securities lending and short sales (subject to the eligibility list) and FMETF only.
- Do not model any pipeline item before a PSE circular and an SEC approval appear: PSE's targets have slipped repeatedly (short selling was SEC-approved in Jun 2018 and went live in Nov 2023).

## What is not in the public record

- Per-instrument terms: preferred par values, dividend rates and call dates; FMETF's creation-unit size and current tracking-index disclosure; PDR conversion terms (issuer prospectuses and EDGE were not accessible).
- The reason for each preferred suspension, and whether the two PLDT convertible-preferred lines (TLII, TLJJ) are still outstanding.
- Whether a second FMETF Authorized Participant exists, and which "facility or system for negotiated transactions" serves directly listed preferreds.
- SEC approval status, after 17 Aug 2026, of One Lot One Share, the ETF and GPDR rules, market making and the SBL rules (the MPO and preferred-listing rules were approved on 11 and 12 Aug 2026).
- Which Class A/B issuers remain and their cut-over dates.
- The definition and as-of date of the frame's "Free Float Level", and any aggregate MPO-compliance list or free-float histogram from PSE.
- Whether the 2023 voluntary-delisting amendments were adopted, and which tender threshold (90% or 95%) governs MPO-driven petitions.
- The outcome or extension of the Villar-group suspensions beyond the 3-month ceiling; why MGH is still suspended two years after curing its MPO breach; a PSE circular for the reported Mar 2025 temporary 15% IPO float relief.
- The IPO day-1 reference price (offer price or not) and any IPO-specific price limit.
- The primary text of SEC MC 11 s.2026 and SEC MC 1 s.2026 (SEC site not retrievable): only PSE's draft annex and law-firm summaries are available.
- The final pricing, allocation and listing date of Mynt (GCASH) and the Vitro REIT outcome.
