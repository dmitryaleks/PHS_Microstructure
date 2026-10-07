---
number: 13
slug: regulatory-constraints
title: Regulatory Constraints and Market Conduct
summary: Orders count whether or not executed, issuers disclose within 10 minutes, ownership triggers sit at 5/10/15/35/50%, foreign-limit breaches are unwound at once, and DMA rules ban algorithmic flow.
part: Costs, rules and access
---

Market conduct on the PSE sits in three layers that a fund meets through its broker and as a shareholder: the Securities Regulation Code (SRC, RA 8799) and its 2015 implementing rules and regulations (IRR), enforced by the SEC; the exchange's own trading rules, with fines and suspensions; and the rules of the Capital Markets Integrity Corporation (CMIC), the exchange's independent surveillance and audit arm. A fourth set, the listing and disclosure rules, binds issuers and their directors but shapes what a trader can do around news.

Three features are most likely to break assumptions carried over from other venues. First, the manipulation rules attach to **orders**, not only trades: the SEC's rules state that a broker's obligations "apply in respect of all orders, irrespective of the trading system used and whether executed or not", and CMIC's marking-the-close text covers bids and offers "whether matched/executed or not". Second, **no PSE rule permits algorithmic or high-frequency trading through direct market access**: the DMA Rules prohibit it, and the 2023 proposal to allow algorithmic trading has no approval on record. Third, ownership law is mechanical and unforgiving: filings at 5% and 10%, a mandatory-tender trigger at 35% or board control, and a foreign-limit breach that must be sold out at market the same day.

## The regime in four layers

| Layer | Instrument | In force | Enforced by | Reaches |
|---|---|---|---|---|
| Statute and SEC rules | SRC §§18, 19, 23, 24, 26, 27, 54; 2015 IRR[^sec-2015-src-irr-notice-of-effectivity:1] | IRR from 9 Nov 2015 | SEC | Any person; extra duties on registered brokers |
| Exchange trading rules | Revised Trading Rules (RTR) and Implementing Guidelines (IG), 2010 base plus circulars; DMA Rules[^pse-revised-trading-rules:1] | RTR and IG from 26 Jul 2010; DMA Rules from the first trading day of 2014 | PSE | Trading Participants (TPs), traders, DMA clients through their TP |
| CMIC Rules | Version 1.2 of 15 Dec 2011[^pse-cmic-rules:112] | SEC-approved 12 Jan 2012;[^pse-cmic-rules:2] operating since 12 Mar 2012[^pse-tpa-2012-0049-cmic-authority-to-commence:1][^pse-tpa-2012-0005-cmic-commencement:1] | CMIC (provisional self-regulatory organisation, SRO, status from 2 Feb 2012) | TPs; unusual trading by issuers |
| Listing and disclosure rules | Consolidated Listing and Disclosure Rules (CLDR), January 2025 compilation[^pse-listing-disclosure-rules:138] | See below | PSE Disclosure Department | Issuers, directors, principal officers |

There is no consolidated current edition of the trading rules; the operative text is the 2010 base plus circulars, so each rule below carries its source and date.[^pse-web-regulation-trading-participants]

## Market manipulation

### What is prohibited

SRC §24.1 makes it unlawful, for anyone "acting for himself or through a dealer or broker", to create a false or misleading appearance of active trading (including by entering an order "with the knowledge that a simultaneous order or orders of substantially the same size, time and price" will be entered "by or for the same or different parties"), to run series of transactions that raise, depress or create activity in a price through devices "such as marking the close, painting the tape, squeezing the float, hype and dump", to circulate price-move information from manipulative operations, to make false statements to induce trades, and to peg, fix or stabilise a price unless allowed.[^ra-8799-src:24][^ra-8799-src:25] §24.2 bars manipulative devices and subjects short sales and stop-loss orders to SEC rules; §26 is the general fraud provision.[^ra-8799-src:25][^ra-8799-src:26]

| Conduct | SEC IRR | CMIC Rules (Art. XI-B) |
|---|---|---|
| Wash sales ("no change in beneficial ownership") | 24.1.1.1 and 24.1.5.5[^sec-2015-src-irr:67][^sec-2015-src-irr:68] | §9, wash sales[^pse-cmic-rules:117] |
| Improper matched orders (colluding parties, same time, price and quantity) | 24.1.5.3[^sec-2015-src-irr:68] | §9, improper matched orders[^pse-cmic-rules:117] |
| **Marking the close** | 24.1.5.2: "buying and selling securities at the close of the market in an effort to alter the closing price"[^sec-2015-src-irr:68] | §9: "posting actual or fictitious bid or offer at or near the close of the market, **whether matched/executed or not**"[^pse-cmic-rules:117] |
| Painting the tape, hype and dump, squeezing the float, false market information, temporary funds | 24.1.5.1, .4, .6, .7, .8[^sec-2015-src-irr:68] | §9 (examples are non-exclusive)[^pse-cmic-rules:117] |
| Price fixing or pegging | Rule 24.1(e)[^sec-2015-src-irr:70] | — |
| Conduct whose "sole or main purpose is to move the price of a listed security or the level of any index which includes said listed security" | — | §1(e)[^pse-cmic-rules:114] |
| Fictitious transaction or false price; dealing at a price unreasonably away from a displayed firm price; conduct likely to damage market fairness | — | §1, items b, c and d[^pse-cmic-rules:114] |

### Orders count whether or not executed

Rule 24.1.2 is addressed to any person and reaches a "bid or offer", not only a deal, that has or is likely to have the effect of creating a false or misleading appearance of active trading. Rule 24.1.3 forbids a broker to place an order for another person where it is aware, or reasonably suspects, that the order creates such an appearance; 24.1.4 lists what the broker must weigh (market impact, timing, related-party interest, unusual settlement, series of orders, commercial reason) and says failure to consider these factors "shall raise a presumption that the transaction/s is/are manipulative"; and **24.1.6** applies the registered-person obligations "in respect of all orders, irrespective of the trading system used and whether executed or not".[^sec-2015-src-irr:67][^sec-2015-src-irr:68] CMIC's version adds a reporting duty: a TP that knows or suspects a client's transaction is unusual or manipulative must report in writing **within 24 hours of receipt of the order**, and failure raises a presumption that the TP itself is involved.[^pse-cmic-rules:114][^pse-cmic-rules:116] PSE reminded TPs of this in 2012.[^pse-tpa-2012-0099-cmic-reminder-art-xib-sec-8-manipulation:1]

<div class="callout">
<span class="label">Consequence</span>

A fund's exposure does not need a fill. Rule 24.1.2 and the CMIC close-of-market language reach resting and cancelled orders, and the broker is the first filter: it must consider the order's market impact, timing and commercial rationale, and must report suspicion to CMIC within 24 hours. Child-order logic that places and pulls size near the close, or trades against accounts under common control, produces the patterns those broker factors (market impact, timing, related parties, series of orders) are designed to catch.
</div>

<div class="callout infer">
<span class="label">Inference</span>

There is no named prohibition of spoofing or layering. The basis for pursuing it is the combination of Rule 24.1.2, 24.1.6, the CMIC marking-the-close text and CMIC §1(e) (conduct aimed at moving price or an index level). Closing-price manipulation is the best-documented abuse in the public record, and the closing auction and run-off concentrate that risk; the Closing VWAP session gives a separate incentive to move the day's VWAP. These are readings of the rule text, not enforcement history. The structural limits on closing-price manipulation (call auction, no-cancel window, a run-off that cannot move the price) are in [Chapter 6](#/ch/auctions/marking-the-close).
</div>

### Front-running and client priority

A registered person "shall not deal in any securities for himself or for any account in which he has an interest based upon advance knowledge he possesses of pending transactions for or with clients", and client orders have priority over house orders and are handled "in the order in which they are received".[^sec-2015-src-irr:94] Rule 34.1 ("Customer First") requires a TP to execute a customer order "immediately upon receipt", gives customers priority over the TP's own trades, treats orders of directors, officers, associated persons and affiliates as proprietary, and allows each trader one dealing account, treated as proprietary.[^sec-2015-src-irr:111] PSE adds the Best Execution Rule: "reasonable diligence to ascertain the best available price … so that the resultant price to the client is as favorable as possible under the prevailing market conditions"; breach is a **major** violation.[^pse-revised-trading-rules:29][^pse-revised-trading-rules:37] Short-selling conduct rules (uptick, borrow, close-out) are in [Chapter 9](#/ch/short-selling).

### Execution implications

- Keep an auditable order-intent log for every child order, including cancelled ones, and be ready for a broker's 24-hour suspicious-order inquiry. DMA firms must keep system logs for at least five years.[^pse-memo-sec-approved-dma-rules-2013-11-26:11]
- Avoid offsetting orders in the book across funds or accounts under common control, and avoid order patterns whose only effect is to move the close or an index level.
- Treat the final minutes and the run-off as the highest-scrutiny window; justify any size placed or withdrawn there by an execution rationale that can be written down.

## Insider trading and the blackout rule

SRC §27.1 makes it unlawful for an insider to buy or sell while in possession of material non-public information; trades by an insider or the insider's spouse or relatives within the second degree between the information coming into existence and its absorption by the market are **presumed** to be made with it, rebuttable by showing unawareness; §27.2 defines material non-public information (not generally disclosed and likely to affect price, or important to a reasonable person); §27.3 bars tipping; and §27.4 bars trading on non-public information about a commenced or imminent tender offer.[^ra-8799-src:26][^ra-8799-src:27] IRR Rule 27 repeats these; IRR 19.10 adds that anyone aware of a potential tender offer may not trade the target until it is announced, which "shall constitute insider trading under Section 27.4".[^sec-2015-src-irr:73][^sec-2015-src-irr:74][^sec-2015-src-irr:52] CMIC Art. XI-B §§3–6 mirror the insider definition, the presumption and the materiality test.[^pse-cmic-rules:114][^pse-cmic-rules:115]

**Blackout.** CLDR Art. VII §13.2: a director or principal officer "must not deal in the Issuer's securities during the period within which a material non-public information is obtained and up to two (2) full Trading Days after the price sensitive information is disclosed"; breach is a Level 2 offence.[^pse-listing-disclosure-rules:149][^pse-listing-disclosure-rules:160] §13.1 separately requires the issuer to disclose directors' and principal officers' holdings within five trading days of admission, appointment or any change, in addition to SEC Forms 23-A and 23-B.[^pse-listing-disclosure-rules:149] Unusual trading without an apparent reason "gives rise to the presumption that there is insider trading or a rumor or report", and the issuer must answer PSE inquiries or state that no undisclosed development explains it.[^pse-listing-disclosure-rules:149][^pse-listing-disclosure-rules:150]

<div class="callout warn">
<span class="label">Proposed, not found adopted</span>

PSE consultation CN-2024-0048 (30 Sep 2024) proposed extending the blackout to the **issuer itself** (no sale or buy-back) and fixing an earnings blackout from 30 calendar days before the earlier of the earnings pre-announcement or the 17-A or 17-Q submission until two full trading days after disclosure.[^pse-cn-2024-0048-consultation-blackout-rule:4][^pse-cn-2024-0048-consultation-blackout-rule:5] The January 2025 CLDR still shows the old text and no effectivity circular was found as of 6 Oct 2026.
</div>

One surveillance trigger is easy to miss: executing TPs must disclose to PSE, within five trading days of a block sale, the identity of all clients who traded the security from the time the block-sale request was filed.[^pse-implementing-guidelines-trading-rules:25] CMIC sanctioned six TPs in 2013 for breaching that provision (Section XVIII, paragraph 13 of the IG): written reprimands for UBS, Lucky, BDO Securities and Credit Suisse, and a reprimand plus monetary penalty each for BPI Securities and Tower Securities.[^pse-cmic-memo-2014-004-disciplinary-actions-2014-01-10:30][^pse-cmic-memo-2014-004-disciplinary-actions-2014-01-10:31]

### Execution implications

- Run a restricted list with wall-crossing records. CMIC's insider definition covers the issuer, its directors, officers and controlling persons, anyone whose relationship gives access to material information, and anyone who learns it from them, so a board nominee, a role in a pending tender offer or an advisory mandate can put a fund on the list.[^pse-cmic-rules:115]
- No dealing from receipt of material non-public information until two full trading days after disclosure for insider-linked funds. Count the two days from the release on PSE's EDGE disclosure system, which is the next trading day if the filing missed the cut-off (inference; see the disclosure section).
- Expect trading around a block-sale application to be reviewed.

## Surveillance, sanctions and enforcement

### CMIC

CMIC was incorporated on 14 March 2011, was granted SRO status on 2 February 2012 (the 2025 annual report says provisional status) and is PSE's "independent audit, surveillance, and compliance unit", having taken over the former Market Regulation Division; it investigates SRC and CMIC Rule violations by TPs and trading-related irregularities and unusual trading by issuers.[^pse-annual-report-2013:57][^pse-annual-report-2025:8] Its three departments are Surveillance, Audit and Compliance, and Investigation and Enforcement. PSE describes its surveillance system as Total Market Surveillance, developed by the Korea Exchange, with real-time price and volume alerts.[^pse-web-investing-at-pse] Its halt powers are in [Chapter 7](#/ch/price-controls).

### Sanction schedules

| Source | Violation | Sanction |
|---|---|---|
| **CMIC Art. XII**, grave (includes **trading-related irregularities**, unauthorised use of client funds or securities, failure to comply with a final order) | 1st / 2nd / 3rd and later | Written reprimand plus fine of ₱25,000–200,000 / denial of the Trading Right and access to exchange systems / bar from the Exchange and other TPs[^pse-cmic-rules:118][^pse-cmic-rules:119] |
| CMIC, major (capitalisation, ethics, customer-protection reserves, untrue statements to CMIC) | 1st / 2nd / 3rd / 4th and later | Fine of ₱10,000–30,000 / ₱30,000–50,000 / ₱50,000–75,000 / at least ₱75,000[^pse-cmic-rules:119][^pse-cmic-rules:120] |
| CMIC, minor | 1st / later | Written reprimand / fine of ₱10,000–50,000[^pse-cmic-rules:120] |
| **PSE RTR Art. IX**, major (best-execution breach, naked or uptick short-sale breach, insider short sale, odd-lot abuse, error-account abuse pattern, malicious foreign-buy orders) | 1st / 2nd / 3rd and later, within a rolling 12 months | ₱100,000–199,999 / ₱200,000–299,999 / at least ₱300,000 **and** suspension of at least five consecutive trading days, published[^pse-revised-trading-rules:37][^pse-revised-trading-rules:39] |
| PSE RTR Art. IX, minor | 1st / 2nd / 3rd and later | Written reprimand / ₱10,000 / at least ₱50,000[^pse-revised-trading-rules:39][^pse-revised-trading-rules:40] |
| **SEC administrative** (SRC §54.1) | Violations of the Code, rules or orders | Suspension or revocation of registration; fine of ₱10,000–1,000,000 plus up to ₱2,000 a day; disqualification as officer or director for violations of §§19.2, 20, 24, 26 and 27; fine of up to three times profit gained or loss avoided (the printed text cross-refers to "Section 34")[^ra-8799-src:55][^ra-8799-src:56] |
| **Criminal** (SRC §73) | Any violation | Fine of ₱50,000–5,000,000 or 7–21 years' imprisonment, or both; also on responsible officers of a juridical entity[^ra-8799-src:66] |
| **Civil** | Manipulation (§59); insider trading (§61) | Damages to counterparties before the Regional Trial Court[^ra-8799-src:59][^ra-8799-src:60] |

CMIC treats each count as a separate violation, looks back six years for similar violations, publishes sanctions once the CMIC Board affirms them or the appeal period lapses, requires payment within 15 calendar days (then a 25% surcharge plus 1% interest a day), and the SEC may review and reclassify.[^pse-cmic-rules:120][^pse-cmic-rules:121] CMIC §10 gives injured persons the SRC §59 remedy against a TP that willfully participates in manipulation.[^pse-cmic-rules:117] Issuer-side disclosure fines are in the CLDR: a structured-report scale by total assets (from ₱5,000 plus ₱500 a day for assets under ₱25 million to ₱50,000 plus ₱5,000 a day for ₱1 billion and above, with a per-year cap of ten times the basic fine), and for unstructured disclosures Level 1 (reprimand, ₱50,000, ₱75,000, ₱100,000) and Level 2, which includes blackout breaches (₱100,000, ₱150,000, ₱200,000, then ₱300,000 with discretion to suspend or delist), plus ₱1,000 for each trading day until rectified.[^pse-listing-disclosure-rules:159][^pse-listing-disclosure-rules:160]

### Published enforcement and statistics

CMIC's published case counts exist only as annual-report paragraphs for 2013–2019:

| Year | Surveillance cases (investigated or evaluated) | Referred to enforcement dept | Endorsed to the SEC | Disclosure-rule matters sent to PSE |
|---|---|---|---|---|
| 2013 | 117 | 26 | 7 | — |
| 2014 | 87 | 16 | 14 | — |
| 2015 | 66 | 20 | 6 | — |
| 2016 | 167 | 24 | 8 | 6 |
| 2017 | 149 | 43 | 26 | 12 |
| 2018 | 94 | 23 | 24 | 19 |
| 2019 | 94 | 11 | 10 | 5 |

Sources by year: 2013,[^pse-annual-report-2013:57] 2014,[^pse-annual-report-2014:63] 2015,[^pse-annual-report-2015:68] 2016,[^pse-annual-report-2016:74] 2017,[^pse-annual-report-2017:33] 2018,[^pse-annual-report-2018:49] 2019.[^pse-annual-report-2019:28] In 2013, 13 of 133 audited TPs (10%) were sanctioned against 59 (44%) at the end of 2012; in 2018 one enforcement resolution led to the temporary denial of a TP's trading right. No comparable figures were found for 2020–2025: the FY2025 report describes CMIC but gives no case counts.[^pse-annual-report-2025:8] Named sanctions are older still. On 19 Oct 2012 CMIC reprimanded and fined three brokers (Nieves, Tower and HDI Securities) ₱200,000 each for failing to report client transactions that "possibly constitute Unusual Trading Activities", with ₱20,000–30,000 fines for know-your-customer and best-execution lapses; a press headline put the number of fined brokers at four.[^pse-tpa-2012-0177-cmic-disciplinary-actions-2012-10-19:17][^pse-tpa-2012-0177-cmic-disciplinary-actions-2012-10-19:18][^inquirer-2012-10-22-four-brokers-fined] A 10 Jan 2014 compilation lists five investigation sanctions for 2012, four for 2013 (one SRC 24.1(b)-1 case appealed to the SEC) and four 2013 surveillance sanctions.[^pse-cmic-memo-2014-004-disciplinary-actions-2014-01-10:29][^pse-cmic-memo-2014-004-disciplinary-actions-2014-01-10:30]

Court and SEC cases appear only in press reports. BW Resources (1999–2000): the SEC alleged wash sales, matched orders and "making the close" by named brokers as the price rose from ₱2 to ₱107 in a year, and a broker was reported sentenced to 14 years in May 2021 (headline only).[^philstar-2001-01-24-bw-charges][^inquirer-2021-05-22-bw-conviction] Villar Land Holdings: the SEC filed criminal complaints with the DOJ on 30 Jan 2026 alleging false or misleading statements (SRC §24.1(d), §26.3), artificial demand from related-entity trading and insider trading by a director; the respondents denied wrongdoing and the matter was still at preliminary investigation on 23 Aug 2026.[^politiko-2026-01-31-sec-villar-land][^bw-2026-04-21-villar-land-dismissal][^bilyonaryo-2026-08-23-villar-late-q2] PLDT: the SEC inquired into the sell-off before the company's 19 Dec 2022 capex-overrun disclosure.[^philstar-2022-12-20-sec-pldt-inquiry]

### Execution implications

- Published enforcement is sparse and aggregate; read conduct risk from the rules and the few SEC cases, not from the sanctions list.
- A third grave violation bars a broker, and a second denies its trading right: a broker's compliance record is a counterparty risk, so keep more than one execution route.

## Disclosure duties that bind traders

Issuers must disclose material information to PSE **within ten minutes** of receiving it or of the event, and before it reaches the news media; SRC IRR 17.1.1.1.3(b) says the same for the SEC.[^pse-listing-disclosure-rules:139][^sec-2015-src-irr:39] Selective disclosure of material non-public information is prohibited unless made simultaneously to PSE (confidants bound by duty or written confidentiality are exempt); the mandatory-event list includes change of control, losses or transactions of 10% or more of assets, dividends, director resignations and a 10% year-on-year revenue change; corrections are due within ten minutes; and analyst or investor briefings must be notified three trading days ahead.[^pse-listing-disclosure-rules:140][^pse-listing-disclosure-rules:141][^pse-listing-disclosure-rules:142][^pse-listing-disclosure-rules:143][^pse-listing-disclosure-rules:145][^pse-listing-disclosure-rules:149][^pse-listing-disclosure-rules:150] Halts that accompany disclosure are in [Chapter 7](#/ch/price-controls/disclosure-halts).

<div class="callout warn">
<span class="label">EDGE cut-off: 4:00 pm since 25 May 2026</span>

The same-day release cut-off was 3:30 pm from 1 Mar 2022 (CN-2022-0010) and is **4:00 pm from Mon 25 May 2026** (CN-2026-0024 of 22 May 2026); later filings are released on the next trading day, and the submission system stays open after the cut-off.[^pse-cn-2022-0010-edge-cutoff-330pm:1][^pse-cn-2026-0024-edge-cutoff-4pm:1] The January 2025 consolidated rules still print 3:30 pm.[^pse-listing-disclosure-rules:139] With the market closing at 15:15, news filed between 15:15 and 16:00 can now be released the same day after the close (inference). EDGE has been the filing channel since 27 Dec 2013;[^pse-listing-disclosure-rules:138] the release path, feed products and the outages of 19 Jan and 6 Oct 2026 are in [Chapter 11](#/ch/market-data/corporate-disclosure-dissemination-pse-edge).
</div>

### Execution implications

- Event strategies are regulated, halt-constrained events: a halt request follows in-hours disclosure and lasts at least one hour, so first-minute execution is not available.
- Do not run halt or news triggers off a single EDGE scraper; add the PSE website and the circular feed.

## Ownership reporting, tender offers and buy-backs

| Level | Trigger | Filing or action | Deadline |
|---|---|---|---|
| **5%** of a class | Acquiring beneficial ownership of a class of equity in a listed or public company (the statute says "more than 5%")[^ra-8799-src:18][^sec-2015-src-irr:42] | Sworn **SEC Form 18-A** to the issuer, the Exchange and the SEC; amendment on any change; a group is deemed to acquire on the date of agreement[^sec-2015-src-irr:44] | **Five business days** after acquisition under IRR 18.1.2 (the statute says 10 days or the period the SEC fixes)[^sec-2015-src-irr:42] |
| 5%, passive institutions | Brokers, banks, insurers, investment houses, registered investment companies, pension plans, not seeking control | Short-form **Form 18-AS** | 45 days after year-end; Form 18-A within three business days of ceasing to qualify[^sec-2015-src-irr:43] |
| **10%** or director or officer | Beneficial ownership of 10% or more (statute: "more than 10%"), or becoming a director or officer | **Form 23-A**; then **Form 23-B** for each month with a change | 10 calendar days; 10 calendar days after month-end; for listed securities the Exchange copy "not more than five (5) calendar days after" becoming an owner[^sec-2015-src-irr:65][^sec-2015-src-irr:66] |
| 10%, short-swing | Any purchase and sale, or sale and purchase, within less than six months | Profit recoverable by the issuer; no short sales by such holders[^ra-8799-src:22][^ra-8799-src:23] | Suit within two years |
| **15%** | Intending to acquire 15% in one or more transactions within 12 months | Declaration filed with the SEC[^sec-2015-src-irr:45] | On forming the intention; no period stated |
| **35%** or board control | Intending to acquire 35% of voting shares, or enough to control the board, within 12 months | Disclose the intention and contemporaneously tender for the percentage sought[^sec-2015-src-irr:45] | With the disclosure |
| **Over 50%** | Any acquisition taking ownership above 50% of total equity | Tender offer for all remaining shares at a price supported by an independent fairness opinion; accept all tendered[^sec-2015-src-irr:46] | With the acquisition |

The statute words the trigger differently: SRC §19.1 requires anyone intending to acquire at least 15% of a listed company's class of equity, or at least 30% over twelve months, to make a tender offer by filing a declaration with the SEC; the IRR splits this into the 15% declaration, the 35% or board-control tender offer and the 50% tender offer above, and the IRR is the text that brokers apply (inference).[^ra-8799-src:20] Mechanics: direct purchases from holders that would reach 35% or board control require a tender offer for all voting shares, and the private sale cannot complete before the offer closes; acquisitions **through the exchange trading system** need no tender offer if the 35% or control target is not reached, even if the rest is bought as a block (19.2.3, 19.2.4); exemptions include purchases from unissued or increased capital (unless reaching 50% or board control), foreclosure, privatisation, court-supervised rehabilitation, mergers, and **"purchases in the open market at the prevailing market price"** (19.3.1.6), though the Rule 18 and 23 disclosures still apply.[^sec-2015-src-irr:45][^sec-2015-src-irr:48] An offer stays open at least 20 business days, a mandatory offer must be at the highest price paid in the previous six months, tendered shares can be withdrawn while the offer is open, and the SEC may nullify non-compliant purchases and order a tender offer.[^sec-2015-src-irr:51][^sec-2015-src-irr:52][^sec-2015-src-irr:53] A hedge-fund vehicle is not among the 18-AS categories (inference), so it files the full Form 18-A, and again on changes.

<div class="callout infer">
<span class="label">Inference</span>

The open-market exemption is what lets an on-exchange accumulator pass 35% without a tender offer; how much of the stake is bought off-market determines whether the exemption holds, so structure matters. Percentages run per class of equity and aggregate persons acting in concert; the position-limit monitor must do the same.
</div>

**Tender offers meet the minimum public ownership (MPO) rule.** A tender offer that leaves public float below the issuer's minimum ends in an immediate trading suspension, and both 2026 cases ended in voluntary delisting: Robinsons Retail (tender closed 6 Jul 2026, suspended 13 Jul, delisted 31 Aug) and Asian Terminals (block crossed 13 Mar 2026, delisted 3 Apr) are the 2026 cases ([Chapter 2](#/ch/instruments/minimum-public-ownership-the-rule-in-force-since-11-aug-2026)).[^pse-cn-2026-0038-rrhi-voluntary-delisting:1][^pse-cn-2026-0013-ati-voluntary-delisting:1] The Holcim Philippines tender offer of 2023 and its tax treatment are covered in trade press.[^mb-2023-07-24-holcim-tender-offer-taxes]

### Issuer buy-backs

An issuer may repurchase its shares only if it has **unrestricted retained earnings** to cover the purchase and the purpose is a stock option or purchase plan, short-term obligations settled by re-issuance, paying dissenting stockholders, or another legitimate corporate purpose; active, widespread solicitation triggers the issuer tender-offer procedure, and no repurchase outside the offer is allowed for ten business days after it ends.[^sec-2015-src-irr:48][^sec-2015-src-irr:49] PSE requires prompt disclosure of planned acquisitions or dispositions of treasury shares and of each execution (number and price) before the next pre-open.[^pse-listing-disclosure-rules:148] No SEC safe harbour for buy-back volume or timing was found; the 2024 blackout proposal would bar buy-backs inside blackout windows.

### Foreign-ownership breaches

Valid foreign buy orders are earmarked against the foreign-ownership limit, and posting foreign buy orders "for the malicious purpose of limiting the available volume for foreign buyers" is a major violation.[^pse-revised-trading-rules:17][^pse-revised-trading-rules:37] Since **9 Aug 2025**, SEC MC 10-2025 (circulated as CN-2025-0035 and -0036) requires that, in the "remote event" that a trade breaches the limit, the foreign buyer, through its broker, "immediately cause the disposition" of the excess "at the prevailing market price" and return the proceeds: **within the same trading day if the breach is found in trading hours, otherwise at the next day's opening**; violations are punishable under SRC §54.[^pse-cn-2025-0035-sec-declassification-mandate:3][^pse-cn-2025-0036-declassification-effectivity:1] The circular's recital says PSE "strictly monitors and enforces" the limits in its system.[^pse-cn-2025-0035-sec-declassification-mandate:2] The SEC text archived with CN-2025-0035 is an unsigned copy with the number and date left blank; PSE's notices give 7 Aug 2025 as its date and 9 Aug 2025 as its effect.[^pse-cn-2025-0035-sec-declassification-mandate:1] Foreign-room data, the Class A/B declassification and engine behaviour at the limit are in [Chapter 14](#/ch/foreign-access/behaviour-at-the-limit).

### Execution implications

- Monitor 5% (Form 18-A within five business days), 10% (Forms 23-A and 23-B, short-swing exposure), 15% (declaration), 35% or board control and 50% (tender offer), per class and across persons acting in concert.
- In foreign-limit-constrained names, size foreign-flagged buys against the live foreign-shares-available figure. An executed breach is a forced market sale at the same-day price or the next open, with proceeds returned to the investor: an uncapped execution-risk event.
- Where a live tender offer exists, resolve the position (tender, hedge, sell) before it closes if the offer can take public float below the MPO.

## Algorithmic trading, HFT and direct market access

The PSE has **no rule that expressly permits algorithmic or high-frequency trading**. The DMA Rules, approved by the SEC (letter of 29 Oct 2013) and effective on the first trading day of 2014, with six months for existing DMA providers to comply, define algorithmic trading (an algorithm deciding timing, price or quantity "or in many cases initiating the order without human intervention") and high-frequency trading ("entering or cancelling orders … over sub-second intervals"), and §9(e) states: "The DMA Facility shall not be used for High-Frequency and/or Algorithmic trading."[^pse-memo-sec-approved-dma-rules-2013-11-26:1][^pse-memo-sec-approved-dma-rules-2013-11-26:2][^pse-memo-sec-approved-dma-rules-2013-11-26:3][^pse-memo-sec-approved-dma-rules-2013-11-26:8] The services covered are Automatic Order Routing and Sponsored Access (qualified institutional buyers, QIBs, only); the TP is "ultimately responsible for all DMA Orders", with or without its knowledge, and the facility must have built-in wash-sale prevention; PSE may disconnect a DMA facility "without prior notice" and suspend or revoke on SEC, CMIC or Securities Clearing Corporation of the Philippines (SCCP) recommendation; and the RTR's penal sanctions apply to DMA flow.[^pse-memo-sec-approved-dma-rules-2013-11-26:4][^pse-memo-sec-approved-dma-rules-2013-11-26:9][^pse-memo-sec-approved-dma-rules-2013-11-26:11][^pse-memo-sec-approved-dma-rules-2013-11-26:12] The requirements, fees and pre-trade filters are in [Chapter 1](#/ch/market-architecture/dma-rules-and-algorithmic-trading) and [Chapter 4](#/ch/order-types/risk-controls-at-order-entry).

PSE said in September 2023 that the DMA Rules "expressly prohibit" algorithmic trading but that it "has granted exemptions … in respect of child orders originating from conditioned parent orders".[^pse-cn-2023-0043:3] Its consultation CN-2023-0043 proposed a new RTR Article V: "Algorithmic Trading is allowed by the Exchange"; no programmed or automated entry of a **parent** order; child orders must be **limit orders**; TPs must satisfy the IG before activating algorithms; PSE may suspend algorithmic trading that slows or disrupts the system; DMA TPs must risk-check child orders, "shall not be engaged in, and will not accept any Orders arising from or intended for, High Frequency Trading", submit each algorithmic order type and wait for PSE's written no-objection, and tag parent–child identifiers.[^pse-cn-2023-0043:5][^pse-cn-2023-0043:6][^pse-cn-2023-0043:7][^pse-cn-2023-0043:8][^pse-cn-2023-0043:9]

<div class="callout warn">
<span class="label">Algorithmic trading is not approved</span>

On 4 Jan 2024 PSE said its proposed algorithmic-trading provisions were "pending approval by the SEC".[^philstar-2024-01-04-pse-new-products] The SEC-approved package of 1 Feb 2024 contains only the VWAP trading rules, and PSE's trading-participant rules page lists no algorithmic-trading rule among its 2024–25 uploads.[^pse-approved-rules-vwap-trading-2024:1][^pse-web-regulation-trading-participants] No approval was found as of 6 Oct 2026, and HFT stays prohibited even under the proposal.
</div>

<div class="callout infer">
<span class="label">Inference</span>

In practice institutional algorithms run in two ways: broker-side algorithms operated by the TP under its own certified front-end system, with a human-entered parent order and limit-only child orders (what the 2023 text would codify), and buy-side parent orders sliced manually or with broker tools. Client-controlled sub-second strategies through DMA or Sponsored Access are contractually barred. A fund relying on client-side algorithms through DMA should obtain written PSE no-objection through its broker.
</div>

### Mandated controls at TP level

Per-trader value limits, certification of the front-end order management system (FEOMS), message-flow controls and the DMA pre-trade filters are in [Chapter 4](#/ch/order-types/risk-controls-at-order-entry). The conduct-side points are these: each order carries an account code (client or proprietary, local or foreign flag); trader IDs go only to SEC-licensed, PAM-certified traders; house and client desks are separated by Chinese walls; a TP is "solely and fully liable" for all orders entered by any route including DMA; DMA clients carry unique client codes; and order tickets are time-stamped and synchronised to the Exchange clock.[^pse-implementing-guidelines-trading-rules:8][^pse-revised-trading-rules:17][^pse-revised-trading-rules:27][^pse-revised-trading-rules:28][^sec-2015-src-irr:193][^sec-2015-src-irr:194][^sec-2015-src-irr:195] No numeric message-rate limit is public.

### Execution implications

- Do not plan on client-controlled sub-second DMA strategies: use a broker's certified front end with human-entered parent orders and limit-only children, and keep parent–child tags ready for the proposed rule.
- Mirror the DMA §11 filters and the broker's per-trader value limit in your own risk layer.
- Re-certify FIX and ITCH connectivity for Eqlipse (FEOMS certification window 10–23 Sep 2026, still open to later requests); day 1 is limit orders only.[^pse-nte-broker-forum-2026-07-09:9][^pse-nte-faq-2026-08:1]

## Trading-participant duties that reach a fund

| Duty | Rule | What it means for a client |
|---|---|---|
| Best execution | RTR Art. IV §23; breach is a major violation[^pse-revised-trading-rules:29][^pse-revised-trading-rules:37] | Ask how the broker evidences "reasonable diligence" for algorithmic slices |
| Client priority | IRR 34.1 and 30.2.1.2.6.1[^sec-2015-src-irr:111][^sec-2015-src-irr:94] | Your order is not behind the house's; aggregated orders must satisfy clients first |
| Aggregation | RTR Art. IV §4: a foreign aggregated order unbundles into foreign, local or error accounts; a local one only to local clients or error; matched orders allocated "fair and reasonable"[^pse-revised-trading-rules:17][^pse-revised-trading-rules:18] | Know your broker's allocation procedure; it must tell you |
| Order ticket and records | Time stamp on receipt and transmission; solicited or unsolicited flag; short-sale marking[^sec-2015-src-irr:194][^sec-2015-src-irr:195] | Order handling is auditable to the second |
| Suspicion reports | CMIC Art. XI-B §2 and §8 (24 hours); AML reporting by broker-dealers[^pse-cmic-rules:114][^sec-2015-src-irr:193] | Your broker may report you without telling you |
| Account identification | Every order carries an account code; amendments only between permitted codes[^pse-revised-trading-rules:25][^pse-revised-trading-rules:27] | Foreign-flag and local-flag handling is enforced at order level |
| Error accounts | Designated account; errors reflected within two trading days; positions liquidated within one month; a pattern of abuse is a major violation[^pse-revised-trading-rules:27][^pse-revised-trading-rules:37] | Error trades become the TP's proprietary position |

Trade cancellation is limited to a TP mistake agreed by both parties (form by 5 pm on T+0), a computer or system error confirmed by PSE, or a Board resolution with SEC notice at least three trading days before; a fee is charged per cancelled trade, and the fourth cancelled block sale is a major violation.[^pse-revised-trading-rules:26][^pse-implementing-guidelines-trading-rules:18][^pse-implementing-guidelines-trading-rules:19][^pse-revised-trading-rules:39] A 2024 proposal to drop the one-month limit on error-account liquidation is pending.[^pse-cn-2024-0048-consultation-blackout-rule:9][^pse-cn-2024-0048-consultation-blackout-rule:10] Unbundling deadlines are stated differently by the SEC (noon on T+1, IRR 52.1.6.18) and PSE's 2011 guidelines (2:00 pm or 5:00 pm on T+1 for whole-day trading); confirm the operative deadline with the broker.[^sec-2015-src-irr:194][^pse-tpa-2011-0124-amended-implementing-guidelines:3]

### Execution implications

- Obtain from each broker its written best-execution, aggregation and allocation, and error-account policies, and its stance on algorithmic child orders, before routing.
- Build reconciliation for the narrow cases in which a trade can be cancelled or an account code amended, and for error trades that end up in the broker's own book.

## Minimum public ownership: the holder's view

The tiers, the public-float classification and the live cases are in [Chapter 2](#/ch/instruments/minimum-public-ownership-the-rule-in-force-since-11-aug-2026), and the suspension state in [Chapter 7](#/ch/price-controls/compliance-suspensions). The enforcement points that matter to a holder: a breach brings **immediate** suspension for up to six months and automatic delisting if uncured; a Compliance Plan (due within ten days) or pending corrective measures do not defer the suspension; and automatic delisting, or a voluntary delisting approved because of the breach, carries a five-year relisting bar and disqualifies directors and principal officers unless they show reasonable measures and due diligence.[^pse-amended-mpo-rule-2026-08:5][^pse-amended-mpo-rule-2026-08:6] Holdings of 10% or more, board-represented holders, directors, officers, controlling shareholders and affiliates are non-public, so a large holder shrinks the float the rule counts; funds are public "regardless of the amount of shareholdings, unless the Fund has a Board seat", and whether an asset-manager vehicle holding 10% or more is treated as public is for PSE to classify (inference).[^pse-amended-mpo-rule-2026-08:10][^pse-amended-mpo-rule-2026-08:11] Screen on the float cushion, the free float minus the issuer's cohort minimum, and treat names within a few points of the line with a pending tender offer or placement as suspension risks.

## What is not in the public record

- Final status of the algorithmic-trading article (approval date or text) after January 2024; numeric message-rate and pre-trade limits imposed on FEOMS.
- CMIC's price and volume benchmarks, its own annual reports and post-2014 disciplinary publications (cmic.com.ph blocks automated access), and PSE annual reports for 2020–2024; any CMIC case counts after 2019.
- Whether the CMIC Rules were amended after 2012 (sanction amounts, Article XI), and SEC enforcement statistics.
- Any closing-price manipulation sanction after 2013.
- Whether CN-2024-0048 (blackout and error-account changes) or the 2022 halt proposals took effect after January 2025; post-2015 amendments to IRR Rules 18, 19 and 23 are not reconciled.
- SEC rules on buy-back programme volume, price and timing.
- Order types beyond limit orders, price collars and self-trade prevention on the Nasdaq Eqlipse engine (NTE).
