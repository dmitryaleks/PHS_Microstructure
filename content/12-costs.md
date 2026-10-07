---
number: 12
slug: costs
title: Trading Costs and Taxes
summary: Explicit PSE costs per side, the sell-only 0.1% stock transaction tax since 1 Jul 2025 (was 0.6%), a PHP 10m round trip at 70.12 bp, and the dividend and capital-gains tax matrix for non-residents.
part: Costs, rules and access
---

A PSE equity trade carries a short, mostly fixed explicit-cost stack: exchange, clearing and (probably) regulator fees of about 2 bp per side, a negotiated broker commission plus 12% VAT, and one tax that dominates everything else, the **stock transaction tax (STT)** charged to the seller. Since 1 July 2025 that tax is 0.1% of the gross selling price. For the seven and a half years before that it was 0.6%, and it is still 0.6% on some broker fee pages and in any backtest that switches parameters by calendar year instead of by trade date.[^ra-12214-cmepa:16]

Two behaviours break assumptions carried over from other venues. First, the cost is **asymmetric and gross-value based**: a sale costs 10 bp more than a purchase before any commission, and the tax is not netted for intraday round trips. Second, there has been **no regulatory minimum commission since 18 April 2024** and there is no public institutional rate card, so the one input a cost model cannot source is the one that moves the round trip most (2.24 bp of round-trip cost per bp of commission). Investor-level taxes decide what a non-resident fund keeps: listed shares carry no capital-gains tax, but cash dividends to a non-resident corporation are withheld at 25% (15% on a conditional route), and the exchange's own fee page still prints the pre-2021 figure of 30%.[^pse-investing-at-pse]

## The explicit fee stack

### Fee schedule per side

Rates are percentages of gross value (price times quantity). "Both" means the charge applies to the buy and to the sell.

| Component | Rate | Payer | Basis |
|---|---|---|---|
| Broker commission | Negotiated; maximum 1.5% of transaction value; **no regulatory minimum since 18 Apr 2024** | Both | SEC MC 7-2024;[^pse-cn-2024-0029-min-commission-removal:3] exchange statement[^pse-investing-at-pse] |
| VAT on commission | 12% of the commission, so all-in commission is 1.12c | Both | PSE ticket: PHP 28.00 on a 0.25% commission over PHP 10,000[^pse-investing-at-pse] |
| PSE transaction fee | 0.005% (0.5 bp) plus 12% VAT = **0.56 bp** | Both | Exchange page;[^pse-investing-at-pse] OECD reproduction of the same illustration[^oecd-capital-market-review-philippines-2024:45] |
| SCCP clearing and settlement fee | 0.01% (**1.00 bp**), VAT-inclusive | Both | Exchange page;[^pse-investing-at-pse] SCCP Clearing House Rules 2018, Annex 7[^sccp-clearing-house-rules-2018:62] |
| SEC "SRC fee" | 0.005% (**0.5 bp**) of transaction value | Both, per the PSE illustration | Listed by the PSE and OECD; no primary rate document; see the warning below |
| SIPF contribution | 0.001% (0.1 bp), listed only for block sales | Both | One broker FAQ only[^bpi-trade-fees-faq] |
| **Stock transaction tax** | **0.1% (10 bp)** of gross selling price | **Seller only** | NIRC Sec. 127(A) as amended by RA 12214 Sec. 17, from 1 Jul 2025;[^ra-12214-cmepa:16] RR 20-2025[^bir-rr-20-2025-stt:2] |

The PSE's own worked tickets reproduce the stack on a PHP 10,000 trade at a 0.25% commission. The purchase costs PHP 10,030.06: commission with VAT 28.00, SRC fee 0.50, PSE fee 0.56 (VAT included) and SCCP fee 1.00. The sale nets PHP 9,959.94 after the same four items plus STT of 10.00.[^pse-investing-at-pse] Settlement is T+2 (see [Chapter 10](#/ch/clearing-settlement)).

<div class="callout warn">
<span class="label">The SRC fee is a secondary-only parameter</span>

The PSE's illustration charges an "SRC Fee (Transaction Value x 0.005%)" on both sides and cites Section 35 of the Securities Regulation Code, and the OECD's 2024 table lists it as "SRC fee" for the buyer and "SEC fee" for the seller.[^pse-investing-at-pse][^oecd-capital-market-review-philippines-2024:45] But Section 35 only obliges each **Exchange** to pay the SEC a semestral fee of "not more than one-hundredth of one per centum" of the aggregate sales transacted on it, so the 0.005% rate and its pass-through to investors are not in the statute.[^ra-8799-src:36] The PSE's own "Table 2" schedule omits the fee even though both illustrations charge it, and three retail broker pages (COL Financial, First Metro, BPI Trade for regular trades) do not itemise it.[^pse-investing-at-pse][^colfinancial-fees-faq][^firstmetrosec-fees-and-charges][^bpi-trade-fees-faq]

Treat it as a +0.5 bp per-side parameter, **default ON for institutional flow unless the broker's contract note shows otherwise**, and show every cost figure with and without it. The SIPF line (0.001%, block sales only) comes from a single broker page and no SIPF contribution schedule was found in a primary source.
</div>

<div class="callout infer">
<span class="label">Inference</span>

Two 0.005% legs add up to 0.01% of a trade's value, which equals the statutory ceiling in SRC Section 35 (0.01% of aggregate sales, and each trade is one sale). The PSE page may simply be passing the ceiling through, split between buyer and seller. No document says so. A 2014 trade-press report already listed an SEC fee of 0.005% in the standard stack beside the PSE fee (0.005%), the SCCP fee (0.01%) and the 1.5% commission maximum, so the stack apart from the seller tax looks unchanged for at least twelve years (secondary).[^oxford-business-group-2014-trading-tariffs]
</div>

Other notes on the stack:

- **VAT on the PSE fee.** Brokers date the pass-through of 12% VAT on the PSE fee to **4 Sep 2025** (First Metro's tables are headed "Effective September 4, 2025"); the COL Financial FAQ, last modified 10 Jul 2025, shows no VAT on that fee.[^firstmetrosec-fees-and-charges][^colfinancial-fees-faq][^pinoymoneytalk-fees] The OECD's 2024 copy of the PSE illustration already showed VAT-inclusive PHP 0.56,[^oecd-capital-market-review-philippines-2024:45] so what changed on 4 Sep 2025 is probably broker pass-through, not the exchange charge. The originating notice was not found.
- **Rounding.** COL states that every computed charge is rounded to hundredths (symmetric arithmetic rounding) before totalling.[^colfinancial-fees-faq]
- **Clearing-fund contributions** (1/500 of 1%, about 0.2 bp, of a clearing member's monthly turnover) are a broker-level cost and appear in no client fee itemisation found.[^sccp-clearing-house-rules-2018:33] A member that leaves the market is refunded its contributions only to the extent it proves it "shouldered" them rather than collecting them from clients (SCCP memo of 8 Jul 2025), which implies they are meant to be broker overhead (inference); see [Chapter 10](#/ch/clearing-settlement).[^sccp-memo-01-0725-ctgf-refund-sec-approval:1]
- **Scrip charges** are irrelevant to scripless institutional flow: PDTC upliftment PHP 50 per certificate request, transfer-agent direct transfer PHP 100 plus VAT and cancellation PHP 20 plus VAT.[^pse-investing-at-pse]
- **Not in any figure here:** bid-ask spread and market impact ([Chapter 15](#/ch/empirical)), PHP/USD conversion spread, custody and safekeeping, bank transfer charges, withholding taxes on dividends and interest, and securities-lending fees.[^firstmetrosec-fees-and-charges]

### Commission: cap, abolished minimum and what brokers publish

The statutory frame is old. Presidential Decree 154 (14 Mar 1973) capped stockbroker commission at 1% of the value of each transaction, with a PHP 20 minimum per transaction; the SEC raised the cap to **1.5%** on 14 Dec 1977.[^pse-cn-2024-0029-min-commission-removal:2] Separately, the PSE's *Amended Rule on Minimum Commission Rates* prescribed a size-graded minimum. SEC Memorandum Circular 7 of 2024 (dated 16 Apr 2024, effective on publication in two newspapers on 18 Apr 2024) "resolves to remove the minimum amount of commission charged by stockbrokers", and PSE CN-2024-0029 (17 May 2024) confirms the PSE rule and its interpretative guidelines "ceased to be in force upon the effectivity of SEC MC 7-2024 on April 18, 2024".[^pse-cn-2024-0029-min-commission-removal:1][^pse-cn-2024-0029-min-commission-removal:3] The exchange now states: "There is no prescribed minimum commission. A stock brokerage firm may set its own commission schedule."[^pse-investing-at-pse]

**The superseded schedule (history only).** PSE Memo for Brokers 2008-0467, effective 6 Oct 2008, set these minimums, exclusive of VAT:[^pse-memo-2008-0467-minimum-commission-rates:2]

| Transaction value (PHP) | Minimum commission | Floor (PHP) |
|---|---|---|
| Up to 100m | 0.25% | none |
| Over 100m to 500m | 0.15% | 250,000 |
| Over 500m to 1bn | 0.125% | 750,000 |
| Over 1bn to 5bn | 0.10% | 1.25m |
| Over 5bn to 10bn | 0.075% | 5m |
| Over 10bn | 0.05% | 7.5m |

The rate applied to the whole transaction and the PHP floors stopped the fee falling when a trade crossed into a cheaper bracket. The schedule did not apply to broker-to-broker or odd-lot transactions, PD 154 prevailed over it, and trading participants of government entities required to withhold VAT could charge less. Breaches were fined up to PHP 2.5m (first offence), PHP 5m and PHP 10m, with suspensions of up to 5, 10 and 15 business days.[^pse-memo-2008-0467-minimum-commission-rates:2][^pse-memo-2008-0467-minimum-commission-rates:3] A 2014 report gives the same endpoints and the 1.5% maximum.[^oxford-business-group-2014-trading-tariffs] The OECD's 2024 review mislabels the removed floor as a "1.5% minimum"; 1.5% is the maximum, as the SEC circular and the exchange both state.[^oecd-capital-market-review-philippines-2024:45]

<div class="callout infer">
<span class="label">Inference</span>

Before 18 Apr 2024 a PHP 10m institutional trade could not be priced below 0.25% (PHP 25,000 plus VAT). That floor is almost certainly the origin of today's 0.25% headline rate on online retail platforms. Whether institutional rates have since fallen below 25 bp is plausible but undocumented.
</div>

**What brokers publish (secondary sources, not rate documents).**

| Broker | Published commission | Page date |
|---|---|---|
| First Metro Securities | Online 0.25% of gross value; broker-assisted 0.75% (peso account) or 0.50% (dollar-denominated account)[^firstmetrosec-fees-and-charges] | "updated March 19, 2026" |
| COL Financial | 0.25% of gross value[^colfinancial-fees-faq] | modified 10 Jul 2025 |
| BPI Trade | "0.25% or Php 20.00 whichever is higher"[^bpi-trade-fees-faq] | undated |

The PHP 20 in the BPI row is a broker-set floor, not a regulatory one. (The SEC circular's operative wording, "the minimum amount of commission charged by stockbrokers ... for each transaction", matches PD 154's own PHP 20-per-transaction floor, and the exchange says no minimum is prescribed, so the PD floor is treated as removed; that reading is inference.) A consumer blog adds that phone-assisted trades cost 1% to 1.5% before April 2024.[^pinoymoneytalk-fees] **Institutional and global-broker commission rates have no public source**; they are negotiated bilaterally.

<div class="callout warn">
<span class="label">Do not trust broker fee pages for tax rates</span>

Broker pages lag the law: the COL page (10 Jul 2025) predates VAT on the PSE fee, and some pages still show a 0.6% STT. Source rates from the statute, the BIR regulation and the exchange's own page, and version them with effective dates (1 Jul 2025 for STT; 4 Sep 2025 for broker pass-through of VAT on the PSE fee).
</div>

### Execution implications

- Model the explicit cost as `fee(side) = gross x [1.12c + 0.56 bp + 1.00 bp + 0.50 bp (SRC toggle)] + 10 bp x gross x 1[sell]`, with the fee components and the STT as separate, dated parameters. They change by statute or notice; commission changes by contract.
- Only the 2.24c term of the round trip is negotiable. At c = 10 bp the broker-independent part (14.12 bp, of which STT is 10 bp) is 39% of the round trip; at c = 25 bp it is 20%.
- Ask the broker for the contract-note itemisation (SRC fee, SIPF, any per-ticket floor) before fixing the parameter set. A per-ticket floor such as BPI's PHP 20 matters only for very small child orders.
- Whether charges are computed per execution or per order is not documented. If a broker rounds per fill, a heavily sliced parent order can drift by a few centavos per fill; reconcile against contract notes, not against the formula.

## Stock transaction tax

### Rate history

| Period | Rate on gross selling price | Authority |
|---|---|---|
| 1 Jan 1998 to 31 Dec 2017 | 0.5% (1/2 of 1%) | NIRC Sec. 127(A) as enacted (RA 8424)[^ra-8424-nirc-1997:165] |
| 1 Jan 2018 to 30 Jun 2025 | 0.6% (6/10 of 1%) | RA 10963 (TRAIN), approved 19 Dec 2017[^ra-10963-train:24][^ra-10963-train:54] |
| **From 1 Jul 2025** | **0.1% (1/10 of 1%)** | RA 12214 (CMEPA) Sec. 17, approved 29 May 2025;[^ra-12214-cmepa:16] RR 20-2025[^bir-rr-20-2025-stt:2] |

PSE applied the 0.1% rate to transactions through the Exchange made on Tuesday 1 July 2025 onwards; its notice of 11 Jun 2025 assumed publication would be completed before that date, and its notice of 26 Jun 2025 confirms the Act was published in the Manila Bulletin on 4 Jun 2025 and in the physical Official Gazette on 9 Jun 2025.[^pse-cn-2025-0026-stt-decrease-advisory:1][^pse-cn-2025-0028-cmepa-effectivity:1] The 1 Jul 2025 cut is the single largest discontinuity in explicit cost in the whole record: the sell-side tax fell from 60 bp to 10 bp, so any cost model or backtest spanning that date must switch rates by **trade date**.

<div class="callout warn">
<span class="label">Effectivity wording conflicts between copies of the Act</span>

The lawphil HTML transcription of RA 12214 Sec. 29 reads "after fifteen (15) days following the completion of its publication".[^ra-12214-lawphil-html] The signed copy reads "shall take effect on July 1, 2025, following its complete publication",[^ra-12214-cmepa:25] and BIR RMC 60-2025 and RR 20-2025 (Sec. 10) both use 1 July 2025.[^bir-rmc-60-2025-cmepa-circular:1][^bir-rr-20-2025-stt:4] **Use 1 Jul 2025.** The HTML text is a transcription discrepancy.
</div>

### Mechanics: who pays, collects and files

- **Incidence.** The seller or transferor pays. The statute reaches "every sale, exchange, or other disposition of shares of stock and other securities listed and traded through a local stock exchange", other than a sale by a dealer in securities, in lieu of capital gains tax.[^ra-12214-cmepa:16] "Shares of stock" includes warrants, options and mutual fund certificates, and "securities" is defined broadly.[^bir-rr-20-2025-stt:1][^bir-rr-20-2025-stt:2]
- **New scope.** CMEPA added the same 0.1% for shares of a domestic corporation listed and traded on a **foreign** exchange (Sec. 127(B)); RR 20-2025 Sec. 4 implements it, with remittance by the selling shareholder or the broker within 10 banking days.[^ra-12214-cmepa:16][^bir-rr-20-2025-stt:3]
- **Dealers.** A "dealer in securities" is a merchant with an established place of business regularly buying and re-selling securities to customers; dealer gains are ordinary income, not STT (RR 20-2025 Secs. 2(d) and 5).[^bir-rr-20-2025-stt:2][^bir-rr-20-2025-stt:3] A non-resident fund trading for its own account is not a dealer on that definition (inference), so STT, not income tax, applies; whether a market maker qualifies as a dealer depends on facts (see [Chapter 8](#/ch/market-making)).
- **Collection.** The stock broker who effected the sale collects the tax, remits it to the BIR within five banking days of collection and submits a weekly return on Mondays to the exchange secretary.[^ra-12214-cmepa:16][^ra-12214-cmepa:17]
- **Transfer bar.** No transfer is registered unless proof of payment is filed with the transfer agent or corporate secretary (RR 20-2025 Sec. 7).[^bir-rr-20-2025-stt:3][^bir-rr-20-2025-stt:4]
- **Launch-day filing.** The BIR Tax Advisory of 4 Jul 2025, relayed by PSE CN-2025-0032 on 15 Jul 2025, said the revised rate and the foreign-exchange transaction type were not yet in BIR Form 2552 on eBIRForms and eFPS; taxpayers were to file Form 2552 manually and pay at any authorised agent bank "regardless of jurisdiction" (citing RR 4-2024 and RMC 87-2024), using ATC "PT 203" for foreign-exchange transactions. A revenue issuance was to follow once the new rate and ATC were available electronically; it was not located.[^pse-cn-2025-0032-bir-stt-advisory:1][^pse-cn-2025-0032-bir-stt-advisory:2]
- **Account class.** PSE's account-code scheme includes a "Tax-Exempt Client" class for corporate accounts exempt from STT, so STT-exempt status is visible to the trading system at account level.[^pse-implementing-guidelines-trading-rules:21]

### Execution implications

- Look the rate up by **trade date**, not settlement date or calendar year: trades executed on or after 1 Jul 2025 bear 0.1% even though they settle on T+2.
- STT is collected by the executing broker from the seller's proceeds, so it appears on the contract note (the PSE's own sale ticket shows it); no separate filing duty for the seller of an on-exchange sale is stated (inference), but the sale of a foreign-listed domestic share is remitted by the selling shareholder, or through a broker, within 10 banking days.
- Use the account-code classification ("Tax-Exempt Client") only where the account genuinely holds STT-exempt status; the flag is set by the trading participant and the status must be documented.

## Worked example: a PHP 10m round trip

Buy PHP 10,000,000 and sell the same value at the same price, at a 25 bp commission (the retail-online headline rate), full stack including the SRC fee.[^pse-investing-at-pse]

| Component | Buy (PHP) | Sell (PHP) |
|---|---|---|
| Gross value | 10,000,000.00 | 10,000,000.00 |
| Commission at 0.25% | 25,000.00 | 25,000.00 |
| VAT 12% on commission | 3,000.00 | 3,000.00 |
| PSE fee 0.005% | 500.00 | 500.00 |
| VAT 12% on PSE fee | 60.00 | 60.00 |
| SCCP fee 0.01% (VAT-inclusive) | 1,000.00 | 1,000.00 |
| SEC "SRC fee" 0.005% | 500.00 | 500.00 |
| STT 0.1% (seller only) | n/a | 10,000.00 |
| **Total** | **30,060.00 (30.06 bp)** | **40,060.00 (40.06 bp)** |
| Without the SRC fee | 29,560.00 | 39,560.00 |

- **Round trip, full stack: PHP 70,120 = 70.12 bp.** Buy cash out is PHP 10,030,060.00 and sell net proceeds are PHP 9,959,940.00. This is the PSE's own PHP 10,000 ticket scaled by 1,000.[^pse-investing-at-pse]
- **Without the SRC fee: PHP 69,120 = 69.12 bp** (buy 10,029,560.00; sell net 9,960,440.00), which is what a retail-broker stack that omits the fee implies.[^colfinancial-fees-faq][^firstmetrosec-fees-and-charges]

### Closed form and sensitivity

With commission c in basis points, each side costs 1.12c + 0.56 + 1.00 + 0.50 = 1.12c + 2.06 bp, and the sale adds 10 bp of STT:

`RT_bp = 2.24c + 14.12` (full stack), or `2.24c + 13.12` without the SRC fee.

| Commission c (bp) | RT full stack (bp) | RT without SRC (bp) | PHP per PHP 10m round trip (full stack) |
|---|---|---|---|
| 0 | 14.12 | 13.12 | 14,120 |
| 2 | 18.60 | 17.60 | 18,600 |
| 5 | 25.32 | 24.32 | 25,320 |
| 10 | 36.52 | 35.52 | 36,520 |
| 15 | 47.72 | 46.72 | 47,720 |
| 25 | **70.12** | 69.12 | 70,120 |
| 50 | 126.12 | 125.12 | 126,120 |
| 75 | 182.12 | 181.12 | 182,120 |
| 150 (the 1.5% cap) | 350.12 | 349.12 | 350,120 |

Institutional commission levels are assumptions, not sourced.

<div class="callout">
<span class="label">Consequence</span>

The broker-independent part of the round trip is **14.12 bp**, and 10 bp of it is a tax that no negotiation moves. The tax is charged on the gross value of every sale and is not netted for intraday round trips, so a strategy that turns its capital N times a year pays about 10 bp x N in STT alone: 20 turns a year is 200 bp (2%) of capital before commission, spread or impact. Hurdle rates for high-turnover signals must be set net of this tax.
</div>

### Regime comparison and peers

| Regime (c = 25 bp, same full-stack assumptions) | Buy | Sell | Round trip |
|---|---|---|---|
| Before 1 Jul 2025 (STT 0.6%), 2018 to 30 Jun 2025 | PHP 30,060 | PHP 90,060 | **PHP 120,120 (120.12 bp)** |
| From 1 Jul 2025 (STT 0.1%) | PHP 30,060 | PHP 40,060 | **PHP 70,120 (70.12 bp)** |

The saving is exactly the STT cut: 50 bp, or PHP 50,000 per PHP 10m round trip. The pre-CMEPA figure matches the OECD's 2024 illustration of 0.3% for a buyer and 0.9% for a seller, and on a retail-broker stack that omits both the SRC fee and VAT on the PSE fee the pre-CMEPA round trip was PHP 119,000.[^oecd-capital-market-review-philippines-2024:45]

The OECD (published before CMEPA) put total buy-plus-sell trading costs in the Philippines at 1.2% of traded value against a 0.66% peer average, and recommended assessing an STT reduction.[^oecd-capital-market-review-philippines-2024:46] On the OECD's own assumptions (0.25% commission, PHP 10,000 ticket):[^oecd-capital-market-review-philippines-2024:46]

| Market | Buyer | Seller | Round trip |
|---|---|---|---|
| Thailand | 0.27% | 0.27% | 0.54% |
| Singapore | 0.32% | 0.32% | 0.64% |
| Indonesia | 0.32% | 0.32% | 0.64% |
| Malaysia | 0.41% | 0.41% | 0.82% |
| Philippines, OECD 2024 (STT 0.6%) | 0.30% | 0.90% | 1.20% |
| Philippines from 1 Jul 2025 (STT 0.1%; my arithmetic) | 0.30% | 0.40% | 0.70% |

The OECD also notes that the Philippines and Thailand are the two jurisdictions in its comparison where the securities regulator charges an additional fee, and that exchange fees (0.005%) are at the low end of the peer range.[^oecd-capital-market-review-philippines-2024:45]

<div class="callout infer">
<span class="label">Inference</span>

At those assumptions the post-CMEPA Philippine round trip (0.70%) sits about 4 bp above the OECD's 2024 peer average (0.66%), against 54 bp above before the cut. The peer figures were not refreshed after 2024. FTSE Russell still rates the Philippines "Not Met" on "transaction costs (implicit and explicit)" in its March 2026 table, and that rating covers implicit as well as explicit costs.[^ftse-quality-of-markets-asia-pacific-2026-03:1]
</div>

### Execution implications

- STT makes every exit 10 bp more expensive than every entry. A signal must clear the round-trip hurdle, and a sell-then-rebuy rebalance pays the tax again on the same capital.
- For shorts the tax falls on the opening short sale; the buy-to-cover is a purchase and carries no STT.
- Quote hurdles in round-trip bp (2.24c + 14.12), not per side, when comparing with spread and impact estimates from [Chapter 15](#/ch/empirical).
- Apply the STT regime by trade date. A backtest crossing 1 Jul 2025 that uses a single rate overstates or understates sell costs by 50 bp.

## Special cases

### Blocks, crosses and off-exchange transfers

- **Block sales and crosses executed through the exchange are not a tax shelter.** PSE rules require the applicant to certify that the block-sale facility "is not being used to circumvent the provisions of the National Internal Revenue Code of 1997".[^pse-implementing-guidelines-trading-rules:24] The REIT Act says in terms that a sale through the Exchange, "including block sales or cross sales with prior approval from the Exchange", bears the STT;[^ra-9856-reit-act:21] for other stocks the same follows from the statute's reach to any sale "listed and traded through a local stock exchange" (inference).
- **Thresholds, approval and settlement** of block sales are in [Chapter 5](#/ch/matching); the unresolved conflict over their settlement cycle is flagged in [Chapter 10](#/ch/clearing-settlement). Nothing there changes the tax: an exchange-executed block bears STT like any other sale.
- **Block add-ons.** One broker FAQ lists SEC 0.005% and SIPF 0.001% as additional charges on block sales, about +0.6 bp per side if they apply (secondary).[^bpi-trade-fees-faq]
- **Off-exchange transfers of listed shares** are not "traded through a local stock exchange", so Sec. 127 does not apply; the 15% final tax on net capital gains from shares not traded on an exchange and documentary stamp tax apply instead (inference from the statute's wording and the regime tables below).[^bir-rr-21-2025-cmepa-income:4]
- **Negotiated trades under the new engine** (pre-arranged, one firm, within 5% of the full-day VWAP, 15-minute window after the run-off) execute through the exchange's facility; no document states their tax treatment, and the exchange-execution reasoning above is the only guide.[^pse-nte-broker-forum-2026-07-09:8]

### ETFs

No PSE or BIR text on exchange-traded fund STT was found. The statutory definition of "shares of stock" includes "mutual fund certificates" and Sec. 127 reaches "shares of stock and other securities listed and traded", so PSE-listed ETF shares should bear 0.1% on sale (inference).[^ra-12214-cmepa:2][^ra-12214-cmepa:16] On the issuance side, CMEPA exempts from documentary stamp tax the original issuance and redemption of shares in a mutual fund company and the issuance of fund-participation certificates.[^ra-12214-cmepa:20] The equity ETF universe is one fund (see [Chapter 2](#/ch/instruments)).

### REITs

Sales of listed REIT securities through the Exchange bear the STT (the Act names Sec. 127(a)) and are exempt from documentary stamp tax; the Act also exempted REIT offerings from the old IPO tax.[^ra-9856-reit-act:21] A sale of REIT securities **outside** the Exchange bears capital gains tax.[^bir-rr-3-2020-reit:4] REIT dividends carry a 10% final tax even for non-residents (see below). A REIT that owns Philippine land must comply with foreign-ownership limits, which is why all listed REITs show a 40% limit ([Chapter 14](#/ch/foreign-access)).[^ra-9856-reit-act:9]

### IPO tax repeal and primary issuance

The original Code charged an **IPO tax** of 4%, 2% or 1% of the gross selling price, by the share of outstanding stock sold (up to 25%; over 25% to 33 1/3%; over 33 1/3%), paid by the issuer on primary shares or by the seller on secondary shares.[^ra-8424-nirc-1997:165-166] Bayanihan II (RA 11494, approved 11 Sep 2020, effective on publication) repealed Sec. 127(B).[^ra-11494-bayanihan-ii:20][^ra-11494-bayanihan-ii:25] Bayanihan II's Sec. 18 limits the Act's life to the 18th Congress "except as otherwise specifically provided"; the repeal is read as permanent, and CMEPA's rewrite of Sec. 127 (local-exchange sales in (A), foreign-listed shares in (B)) contains no IPO-tax subsection, so the current Code has no IPO tax.[^ra-11494-bayanihan-ii:25][^ra-12214-cmepa:16] Primary issuance still bears issuer-side documentary stamp tax (below). A selling-shareholder tranche sold "through IPO" before listing is no longer covered by the old carve-outs, because Sec. 199(e) now exempts only shares "listed and traded"; its treatment is **not addressed in any source found**, and 15% capital gains tax plus stamp tax is likely (inference).[^ra-12214-cmepa:20]

### Securities borrowing and lending

Borrowing and lending of PSE-listed shares, and the delivery and return of collateral and "Equivalent Shares", are outside STT, capital gains tax and documentary stamp tax **only if** a valid Master Securities Lending Agreement (MSLA) is registered with and approved by the BIR, the programme complies with SEC rules and it is administered and supervised by the PSE.[^bir-rr-10-2006-sbl:4][^bir-rr-1-2008-sbl:4] The conditions, registration steps and programme rules are in [Chapter 9](#/ch/short-selling). The points a cost model needs:

- The **short sale itself is an ordinary sale and bears STT** (10 bp on the opening leg); the buy-to-cover is a purchase and carries none. The PSE FAQ says the subsequent sale of the borrowed securities is "subject to the regular taxes".[^pse-sbl-short-selling-page]
- **A failed condition is a tax event, not only a compliance breach.** If shares are not returned, are used outside the specified purposes, the borrower defaults, the MSLA is invalid or registration is missing or late, the loan is a deemed sale, which "is necessarily consummated outside the PSE" and so bears capital gains tax (tax base: the higher of the prior-day closing price and the amount realised, less cost) and documentary stamp tax under Sec. 175, not STT.[^bir-rr-10-2006-sbl:9][^bir-rr-10-2006-sbl:10] Under RR 10-2024 (5 Jun 2024), where the borrower fails to return at the end of the borrowing period the lender may buy equivalent shares on the exchange with the borrower's collateral, "which purchase is subject to the stock transaction tax under Section 127(a)".[^pse-cn-2024-0035:8]
- **Registration and tenor:** the borrower registers the MSLA with the BIR (PHP 5,000 fee) within two weeks if it was executed in the Philippines and within one month if abroad, and an unregistered MSLA makes each loan a sale and purchase outside the PSE; the maximum borrowing period is two years.[^bir-rr-10-2006-sbl:7][^bir-rr-10-2006-sbl:8][^pse-msla-clearance-guidelines-2026:2][^bir-rr-1-2008-sbl:5]

<div class="callout warn">
<span class="label">Conflict on manufactured dividends</span>

BIR RR 10-2006 as amended by RR 1-2008 says receipt of manufactured dividends "shall not be a taxable income of the Lender" and that the borrower's payment is not deductible.[^bir-rr-10-2006-sbl:4][^bir-rr-1-2008-sbl:5] The PSE's SBL FAQ says manufactured dividends and substitute payments "shall be taxed as other income in the hands of the Lender".[^pse-sbl-short-selling-page] No later BIR issuance reconciling the two was found, and no post-CMEPA SBL-specific BIR issuance was found. Take the regulation as the rule and confirm with tax counsel before a lending programme is priced.
</div>

### Documentary stamp tax

| Transaction | NIRC section | Before 1 Jul 2025 | From 1 Jul 2025 |
|---|---|---|---|
| Original issue of shares | Sec. 174 | PHP 2.00 per PHP 200 of par (1%)[^ra-10963-train:37] | 75% of 1% of par; of actual consideration for no-par shares; of actual value for stock dividends[^ra-12214-cmepa:18][^bir-rr-19-2025-dst:2] |
| Transfer of shares (off-exchange) | Sec. 175 | PHP 1.50 per PHP 200 of **par** (0.75% of par, not of price); no-par: 50% of the stamp tax paid on original issue[^ra-10963-train:38] | Unchanged: CMEPA amended Secs. 174, 176, 179, 190 and 199 only (inferred from the Act's list of amended sections)[^ra-12214-cmepa:1] |
| Sale of shares listed and traded on a local **or foreign** exchange | Sec. 199(e) exemption | Exempt (earlier wording also covered shares sold through an IPO) | Exempt; "redemption" and the foreign-exchange limb are new, the IPO wording is gone[^ra-12214-cmepa:20][^bir-rr-19-2025-dst:3] |
| Foreign-issued certificates of stock | Sec. 176 | n/a | 75% of 1% of transaction value, paid by the seller or transferor[^ra-12214-cmepa:18] |

BIR RR 19-2025 (signed 29 Jul 2025, stamped received 5 Aug 2025) implements the rate changes and the Sec. 199 amendments for transactions made on or after 1 Jul 2025.[^bir-rr-19-2025-dst:1][^bir-rr-19-2025-dst:3] The exchange's own page says sales of PSE-listed shares are exempt from documentary stamp tax.[^pse-investing-at-pse]

### Execution implications

- Anything that moves listed shares off the exchange (a privately negotiated purchase, a transfer between accounts that is a change of beneficial owner) can create 15% capital-gains and stamp-tax exposure; route such trades through the exchange facility and confirm the tax treatment in advance.
- For SBL, build return-date monitoring (two-year maximum) and MSLA registration deadlines (two weeks or one month) into operations: a missed condition converts a loan into a taxable sale.
- Do not model an IPO-allocation selling-shareholder tranche as tax-free without an opinion.

## Investor-level taxes

### Dividends, gains and interest by payee

Rates in force from 1 Jul 2025 per BIR RR 21-2025; "treaty" means a lower treaty rate if one applies.[^bir-rr-21-2025-cmepa-income:4][^bir-rr-21-2025-cmepa-income:5][^bir-rr-21-2025-cmepa-income:7][^bir-rr-21-2025-cmepa-income:8]

| Payee | Gain on listed shares sold on the PSE | Gain on unlisted or off-exchange shares | Cash dividends from a domestic corporation | REIT dividends | Bank and deposit interest |
|---|---|---|---|---|---|
| Resident citizen or resident alien | STT 0.1% on gross (seller) | 15% final on net gain | 10% final | 10% final | 20% final |
| Non-resident alien engaged in trade or business (more than 180 days in a calendar year is "doing business")[^ra-12214-cmepa:6] | STT 0.1% | 15% | 20% | 10% | 20% |
| Non-resident alien not engaged | STT 0.1% | 15% (or treaty) | 25% final (or treaty) | 10% (or lower treaty) | 25% (or treaty) |
| Domestic or resident foreign corporation | STT 0.1% (dealers: ordinary income) | 15% | Exempt | Exempt | 20% |
| **Non-resident foreign corporation (typical fund vehicle)** | STT 0.1% | 15% (or treaty) | **25%; 15% if the home-country condition is met; or treaty** | 10% (or lower treaty) | 25% (or treaty) |

REIT dividends: RA 9856 Sec. 14 imposes a final tax of 10% unless a non-resident alien or non-resident foreign corporation is entitled to a treaty rate below 10%, or the recipient is a domestic or resident foreign corporation (exempt); overseas Filipino investors are exempt for seven years from the effectivity of the implementing tax regulations.[^ra-9856-reit-act:21] A non-resident foreign corporation therefore pays 10% on REIT dividends, not 15% or 25%. Non-resident investment in REIT securities is registrable with the BSP through registering banks (full repatriation of capital and earnings).[^pse-cn-2020-0052-nonresident-reit-investment:1]

What CMEPA did and did not change for investor-level tax: it left the dividend rates untouched (the NRFC move from 30% to 25% came from CREATE, not CMEPA), unified the final tax on bank interest, deposit substitutes and trust funds at 20%, extended the 15% unlisted-share gains tax to shares of foreign corporations not traded on any exchange, introduced STT on domestic shares listed abroad and widened STT to "other securities".[^ra-12214-cmepa:4][^ra-12214-cmepa:5][^ra-12214-cmepa:7][^ra-12214-cmepa:8][^ra-12214-cmepa:16][^pwc-tax-summaries-ph-income-determination]

### Non-resident corporate funds: 25%, 15% and treaties

- **General rule.** A non-resident foreign corporation (NRFC) pays 25% of gross Philippine-source income (NIRC Sec. 28(B)(1), "effective January 1, 2021", CREATE).[^ra-11534-create:11][^ra-12214-cmepa:9]
- **Dividends specifically.** A final withholding tax of **15%** applies "subject to the condition that the country in which the nonresident foreign corporation is domiciled shall allow a credit" for taxes deemed paid in the Philippines equal to the difference between the regular rate and 15% (10 points since the 25% rate).[^ra-11534-create:12] CMEPA left Sec. 28(B)(5)(b) untouched.[^ra-12214-cmepa:9]
- **BIR's restatement (RR 21-2025, from 1 Jul 2025).** NRFC dividends from a domestic corporation: 15% "subject to the condition that the country of residence of the corporate shareholder allows a credit of 10% tax deemed to have been paid in the Philippines **or that the country of residence ... does not impose any tax on the dividends** (or the tax treaty rate)".[^bir-rr-21-2025-cmepa-income:7][^bir-rr-21-2025-cmepa-income:8] The CREATE-amended statute quoted above states only the credit condition; the "no home-country tax" limb comes from the BIR's restatement, PwC and the PSE's older table (an administrative reading).
- **The "tax-sparing" route in practice.** The 15% rate needs either a deemed-paid credit of 10 points in the holder's home country or no home-country tax on the dividend. PwC describes the NRFC rule identically.[^pwc-tax-summaries-ph-income-determination]

<div class="callout warn">
<span class="label">The PSE's own withholding table is stale</span>

The "Investing at PSE" page shows **30%** for non-resident foreign corporations, with a 15% route "equivalent to 15%" credit. That is the pre-CREATE regime; CREATE cut the NRFC rate to 25% and the credit is now 10 points.[^pse-investing-at-pse][^ra-11534-create:12] The statute and RR 21-2025 govern. The same page's individual rates (10%, 20%, 25%) are current.
</div>

**Treaty ceilings** on dividends (maximum withholding; lower rate for a substantial holding, higher rate otherwise; ownership thresholds are 10% or 25% depending on the treaty). Secondary source, PwC, last reviewed 1 Aug 2026:[^pwc-tax-summaries-ph-wht]

| Treaty partner | Dividend ceiling (lower / higher) |
|---|---|
| United States | 20 / 25 |
| United Kingdom, Singapore, Canada, Australia, Malaysia | 15 / 25 |
| Japan, Netherlands, Switzerland, France, Thailand, UAE | 10 / 15 |
| Korea | 10 / 25 |
| Germany | 5 / 10 / 15 |
| No treaty | 15 / 25 (the domestic 15% still needs the home-country condition) |

Ireland, Luxembourg, Hong Kong and the Cayman Islands did not appear in the extract taken; check them directly.

**Worked dividend illustration** (gross cash dividend PHP 1,000,000; arithmetic from the rates above):

| Holder | Withholding | Net |
|---|---|---|
| NRFC at 25% | PHP 250,000 | PHP 750,000 |
| NRFC at 15% (home-country condition met) | PHP 150,000 | PHP 850,000 |
| US-resident corporation holding at least 10% of the voting stock (treaty 20%) | PHP 200,000 | PHP 800,000 |
| REIT dividend to an NRFC | PHP 100,000 | PHP 900,000 |

<div class="callout infer">
<span class="label">Inference</span>

A Cayman- or BVI-domiciled corporate fund (home country imposes no tax on the dividend) should qualify for 15% on RR 21-2025's wording. A US-domiciled corporate holder (taxes foreign dividends, no tax-sparing credit) is more likely at 25%, or 20% at 10% ownership. A treaty ceiling at or above the domestic rate adds nothing, since treaties cap domestic tax and do not raise it. Entity classification (partnership, trust, UCITS or ICAV vehicle) and beneficial-ownership look-through are fact-specific.
</div>

### Capital gains, unlisted shares and treaty hooks

- **Listed shares sold through the exchange:** "in lieu of capital gains tax", so STT only.[^ra-12214-cmepa:16]
- **Shares not traded on a local or foreign exchange:** 15% final on **net** capital gains for individuals (Sec. 24(B)(3)), domestic corporations (Sec. 27(D)(4)), non-resident aliens not in business (through Sec. 25(B)) and NRFCs (Sec. 28(B)(5)\(c)); a return within 30 days of each transaction and a final consolidated return by 15 April for individuals (corporations by the 15th day of the fourth month after year-end).[^ra-12214-cmepa:5][^ra-12214-cmepa:8][^ra-12214-cmepa:10][^ra-12214-cmepa:14][^bir-rr-21-2025-cmepa-income:4][^bir-rr-21-2025-cmepa-income:5][^bir-rr-21-2025-cmepa-income:8] TRAIN already fixed the unlisted-share rate at a flat 15% from 1 Jan 2018.[^ra-10963-train-html]
- **Treaty hook.** Under NIRC Sec. 56(A)(3) as amended, if the seller "submits proof of the intention to avail of the benefit of exemption of capital gains under existing special laws or tax treaties", no payment is required at filing; if the seller later fails to qualify, the tax becomes immediately due with penalties.[^ra-12214-cmepa:15] PwC notes that treaties are explicitly recognised as a basis for capital-gains exemption.[^pwc-tax-summaries-ph-other-taxes] Whether the STT itself, a transaction tax "in lieu of" capital gains tax, can be displaced by a treaty capital-gains article is **not answered by any source retrieved**.
- **Interest on PHP balances** is taxed at 25% for an NRFC (20% for domestic corporations and resident individuals), so keep PHP cash to settlement needs.[^bir-rr-21-2025-cmepa-income:5][^bir-rr-21-2025-cmepa-income:6][^bir-rr-21-2025-cmepa-income:7]

### Execution implications

- Carry a per-account, per-vehicle withholding parameter (10, 15, 20 or 25%; 10% for REIT dividends) into ex-dividend and index-event logic. Dividend capture by a non-resident pays 15% to 25% withholding (REIT 10%) against a 10 bp STT on exit, so it is rarely attractive; ex-date arithmetic is in [Chapter 10](#/ch/clearing-settlement).
- Capital-gains tax is irrelevant for on-exchange trading, and STT is the only transaction tax. Off-exchange or privately negotiated purchases of listed shares create 15% gain-tax and stamp-tax exposure.
- A foreign fund's entitlement to the 15% dividend rate depends on its home-country treatment, not on the PSE; settle the position with the custodian and tax adviser before the first ex-date. The BIR treaty-relief procedure (certificate of residence, application forms, relief at source versus refund) was not retrieved.

## Cost parameters to version by trade date

| Parameter | Regime | In force |
|---|---|---|
| STT on listed shares | 0.5% | to 31 Dec 2017 |
| | 0.6% | 1 Jan 2018 to 30 Jun 2025 |
| | **0.1%** (also domestic shares listed abroad) | from 1 Jul 2025 |
| IPO tax (Sec. 127(B)) | 4% / 2% / 1% | 1 Jan 1998 to Sep 2020 |
| | repealed | from Sep 2020 |
| Minimum broker commission | sliding 0.25% to 0.05% with PHP floors | to 17 Apr 2024 |
| | none (1.5% cap unchanged) | from 18 Apr 2024 |
| Stamp tax on original issue | 1% of par | 1 Jan 2018 to 30 Jun 2025 |
| | 0.75% of par | from 1 Jul 2025 |
| NRFC dividend withholding | 30% (15% with a 15-point credit) | to 31 Dec 2020 |
| | 25% (15% with a 10-point credit or no home-country tax) | from 1 Jan 2021 |
| Broker pass-through of VAT on the PSE fee | not charged on some pages | to 3 Sep 2025 |
| | charged | from 4 Sep 2025 (secondary) |

The NRFC rows rest on CREATE: the 25% rate "effective January 1, 2021" and, for the dividend condition, a credit equal to the difference between the regular rate and 15% from 1 Jul 2020.[^ra-11534-create:11][^ra-11534-create:12] The other rows are sourced where they are explained above.

A minimal per-side cost function that applies the regimes above by trade date (basis points of gross value; excludes spread, impact, FX and custody):

```python
from datetime import date

def explicit_cost_bp(side, commission_bp, trade_date, src_fee=True):
    cost = 1.12 * commission_bp          # commission plus 12% VAT
    cost += 0.56 + 1.00                  # PSE fee incl. VAT, SCCP fee (VAT-inclusive)
    cost += 0.50 if src_fee else 0.0     # SEC "SRC fee": toggle, secondary-only
    if side == "sell":                   # STT is seller-only and set by trade date
        if trade_date >= date(2025, 7, 1):
            cost += 10.0
        elif trade_date >= date(2018, 1, 1):
            cost += 60.0
        else:
            cost += 50.0
    return cost
```

The fee components are the 2025-2026 values; a 2014 report lists the same per-side fees, but the pre-2018 components were not checked against primary documents.[^oxford-business-group-2014-trading-tariffs]

<div class="callout warn">
<span class="label">Scheduled change: 23 Nov 2026, subject to SEC approval</span>

PSE's new trading engine (Nasdaq Eqlipse) is scheduled to go live on 23 Nov 2026.[^pse-nte-broker-forum-2026-07-09:9] The accompanying rule package would introduce **One Lot One Share** (lot size 1) and allow trading participants, "at their discretion", to "impose a minimum order value as a condition to accepting orders" without exceeding the maximum commission rate under applicable laws.[^pse-cn-2025-0046-board-lot-trading-at-last:3][^pse-nte-user-group-2026-01-15:9] That would make broker-set minimum order values, not a regulatory minimum commission, the practical floor for small child orders. The package was labelled "For SEC Approval" on PSE's 17 Aug 2026 status slide and no approval was found as of 6 Oct 2026. The new back-office portal lists a "Weekly Tax Report" module.[^pse-nte-broker-forum-2026-07-09:13] Whether the new engine changes any fee mechanics is not in the public record. Do not model any of this as current; see [Chapter 17](#/ch/reform-timeline).
</div>

## Implicit costs

Spread, market impact, slippage against arrival and closing-auction cost are measured in [Chapter 15](#/ch/empirical); tick-size economics are in [Chapter 4](#/ch/order-types). This chapter covers explicit charges only, which is why it can state them to the centavo.

## What is not in the public record

- **Institutional and global-broker commission rates** after the April 2024 deregulation. No public survey exists; the pre-2024 floor was 0.25% for any trade up to PHP 100m.
- **The primary basis for the 0.005% SRC fee**, the SIPF contribution rate (0.001% appears only on one broker page, for block sales), and the notice behind broker pass-through of VAT on the PSE fee on 4 Sep 2025.
- **BIR positions not found:** the treaty-relief procedure for dividends and capital gains; whether a treaty capital-gains article can displace STT; STT on ETFs; the selling-shareholder tranche of an IPO since the IPO-tax repeal; post-CMEPA SBL guidance; reconciliation of the manufactured-dividend rule.
- **Treatment of stock dividends, rights and other corporate-action taxes** for non-residents was not researched.
- **Whether the new trading engine changes any fee mechanics**, and the follow-up BIR issuance on electronic STT filing.
- **The 2018 SCCP fee level** and any SCCP or PSE fee waivers or incentive schemes.
