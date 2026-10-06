# PSE equities: trading costs, taxes and foreign-investor access (inputs to Chapters 12 "Costs" and 14 "Foreign access")

Status date: 6 October 2026 (all "in force" statements are as of this date unless stated). Draft v2 — all four key questions covered; open gaps are listed per section and in the closing summary of gaps below the timeline.

Conventions
- Citations: `[^slug:N]` = archived PDF in `kb/pdfs/<slug>.pdf`, N = physical 1-based page. `[^slug]` = web page (no PDF archived). Full list in "Source catalog" at the end.
- Evidence labels at the end of a finding: **P** = primary source (law, regulation, regulator/exchange document); **S** = secondary only (law-firm/broker/press/blog page); **I** = my inference (stated reasoning, not found in a source).
- PHP = Philippine peso; bp = basis point (0.01%).
- Tooling constraint: the shared web-search budget ran out mid-session, so some gaps below are "not searched" rather than "not public"; later work used direct fetches of known URLs, the shared KB archive, OCR of scanned PDFs (Windows OCR; page images re-read visually where it mattered) and the PSE EDGE portal (edge.pse.com.ph answered direct requests on 6 Oct 2026).

---

## 1. Explicit per-trade costs on the PSE (commission, exchange/clearing fees, STT, DST) and a worked PHP 10 million round trip

### Takeaway
As of 6 Oct 2026 a PSE cash-equity trade carries: negotiable broker commission (+12% VAT; no regulatory minimum since 18 Apr 2024; ceiling 1.5%), PSE fee 0.005% (+12% VAT), SCCP clearing fee 0.01% (VAT-inclusive), an SEC "SRC fee" of 0.005% (listed by the PSE and the OECD for both sides; several retail brokers do not itemise it), and on the **sell side only** the stock transaction tax (STT) of **0.1%** of gross value (cut from 0.6% on 1 Jul 2025 by RA 12214/CMEPA). Round-trip explicit cost is `2.24·c + 14.12` bp (c = commission in bp; `+13.12` if the SRC fee is not charged): **70.12 bp** at the 0.25% retail-online headline rate (69.12 bp on a retail-broker stack), ~36.5 bp at a 10 bp commission, versus 120.12 bp under the pre-CMEPA regime at 0.25%. Many broker fee pages are stale (some still show 0.6% STT or omit VAT on the PSE fee), so reconcile against the statute, the BIR regulation and the exchange's own page.

### Cited findings

**A. Commission rules**
- Presidential Decree 154 (14 Mar 1973) capped broker commission at 1% of transaction value with a PHP 20 minimum per transaction; on 14 Dec 1977 the SEC raised the cap to 1.5% — both recited in the SEC's own circular. [^pse-cn-2024-0029-min-commission-removal:2] — P
- Until April 2024 the PSE "Amended Rule on Minimum Commission Rates" (and its Interpretative Guidelines) prescribed a size-graded minimum "ranging from 0.25% to 0.05% of the value of the trade". [^pse-cn-2024-0029-min-commission-removal:2] — P. The full schedule (PSE Memo for Brokers No. 2008-0467, effective 6 Oct 2008, Annex A "Amended Rules on the Minimum Commission Rates", exclusive of VAT; as amended by PSE Board Resolution 69 s.2006) was: transaction value up to PHP 100m → 0.25%; over PHP 100m to 500m → 0.15% but not less than PHP 250,000; over 500m to 1bn → 0.125% but not less than PHP 750,000; over 1bn to 5bn → 0.10% but not less than PHP 1.25m; over 5bn to 10bn → 0.075% but not less than PHP 5m; over 10bn → 0.05% but not less than PHP 7.5m. The rate applied to the whole transaction (the PHP floors stop the fee falling when a trade crosses a bracket); it did not apply to broker-to-broker or odd-lot transactions; PD 154 prevailed; TPs of government entities that must withhold VAT could charge less; fines for breach ran from PHP 2.5m (first offence) to PHP 10m. [^pse-memo-2008-0467-minimum-commission-rates:2] [^pse-memo-2008-0467-minimum-commission-rates:3] — P (read from the image; scanned memo). Hence a PHP 10m institutional trade could not be priced below 0.25% (PHP 25,000 + VAT) before 18 Apr 2024 — the origin of today's 0.25% retail-online headline rate (I). A 2014 report gives the same endpoints (0.25% below PHP 100m, 0.05% above PHP 10bn) with a 1.5% maximum. [^oxford-business-group-2014-trading-tariffs] — S
- SEC Memorandum Circular 7, s. 2024, dated 16 Apr 2024, "resolves to remove the minimum amount of commission charged by stockbrokers to its customers for each transaction"; effective on publication in two newspapers (published 18 Apr 2024; filed with UP Law Center 17 Apr 2024). PSE CN-2024-0029 (17 May 2024) confirms the PSE rule and guidelines "ceased to be in force upon the effectivity of SEC MC 7-2024 on April 18, 2024". [^pse-cn-2024-0029-min-commission-removal:1] [^pse-cn-2024-0029-min-commission-removal:3] — P
- Current exchange statement: "maximum commission rate of 1.5% of the total transaction cost plus 12% VAT. There is no prescribed minimum commission. A stock brokerage firm may set its own commission schedule." [^pse-investing-at-pse] — P (exchange web page, undated).
- PSE proposed on 15 Dec 2025 (consultation) letting TPs impose a minimum order value "provided the TP shall not exceed the maximum commission rate under applicable laws and regulations"; the same wording appears in the new-trading-engine (NTE) user-group deck of 15 Jan 2026 alongside "One Lot One Share" (lot size standardised at 1 share). [^pse-cn-2025-0046-board-lot-trading-at-last:3] [^pse-nte-user-group-2026-01-15:9] — P. The NTE broker forum of 9 Jul 2026 schedules **go-live for 23 Nov 2026** (market rehearsals 31 Oct, 7 Nov, 14 Nov), so the legacy engine and its rules remain in force today and these changes are not yet live. [^pse-nte-broker-forum-2026-07-09:9] — P
- Published retail rates (all S, broker pages): First Metro Securities (page "updated March 19, 2026"): online 0.25% of gross value; broker-assisted 0.75% (peso account) / 0.50% (dollar-denominated account). [^firstmetrosec-fees-and-charges] COL Financial (modified 10 Jul 2025): 0.25% of gross. [^colfinancial-fees-faq] BPI Trade: "0.25% or Php 20.00 whichever is higher" (a broker-set floor, not a regulatory one). [^bpi-trade-fees-faq] A consumer blog adds that before April 2024 phone-assisted trades cost 1%–1.5%. [^pinoymoneytalk-fees] — S
- Institutional/global-broker commission rates: **no public source found** (negotiated, bilateral). See Gaps.

**B. Exchange, clearing and regulatory fees (per side, buy and sell)**
- PSE transaction fee: "1/200 of 1% (0.5 basis points) on gross value for every buy and sell transaction executed. The fee is exclusive of 12% value added tax." [^pse-investing-at-pse] — P. Worked ticket on the same page shows "0.56 (VAT included)" on a PHP 10,000 trade. [^pse-investing-at-pse] — P
- VAT on the PSE fee: broker/blog pages date its pass-through to clients from **4 Sep 2025** ("Effective September 4, 2025" header on First Metro's purchase and sale tables). [^firstmetrosec-fees-and-charges] [^pinoymoneytalk-fees] — S. COL's FAQ (modified 10 Jul 2025) predates it and shows no VAT on the PSE fee (stale for this item). [^colfinancial-fees-faq] — S. However, the OECD's 2024 reproduction of the PSE's illustration already showed "0.005% of the transaction value + 12% VAT = PHP 0.56". [^oecd-capital-market-review-philippines-2024:45] — P/S. So VAT existed on the exchange fee at the exchange level before Sep 2025; what changed on 4 Sep 2025 is probably broker pass-through (my inference — I). I did not find the originating PSE/BIR notice (see Gaps).
- SCCP clearing fee: "1 basis point on gross value ... inclusive of 12% VAT" [^pse-investing-at-pse] — P; SCCP Clearing House Rules Annex 7: "ad-valorem rate of 0.0001 or 1 basis point (VAT-inclusive) based on gross trade value (per month)"; initial clearing membership fee PHP 5,000. [^sccp-clearing-house-rules-2018:62] — P (2018 edition).
- SEC "SRC fee": the PSE's illustration charges "SRC Fee (Transaction Value x 0.005%)" on both a buy and a sell, citing SRC Section 35. [^pse-investing-at-pse] — P. SRC Sec. 35 only says each Exchange pays the SEC a semestral fee "not more than one-hundredth of one per centum (1%)" [sic — the words denote 0.01%, the parenthesis says 1%] of the aggregate sales transacted on it; the 0.005% rate is not in the statute. [^ra-8799-src:36] — P. COL, First Metro and BPI Trade (regular trades) do not list it; BPI lists "SEC 0.005%" only for block sales. [^colfinancial-fees-faq] [^firstmetrosec-fees-and-charges] [^bpi-trade-fees-faq] — S. Independent corroboration that it is a standing charge: the OECD (2024) says "the SEC collects the equivalent of 0.005% of the traded value from sellers and buyers" and labels it "SRC fee" (buy) / "SEC fee" (sell) in its table; a 2014 report listed an SEC 0.005% fee in the normal stack. [^oecd-capital-market-review-philippines-2024:45] [^oxford-business-group-2014-trading-tariffs] — P/S. **Conflict flagged**: exchange/OECD include it, three retail broker pages do not itemise it (possibly absorbed or netted); model it as a +0.5 bp per-side parameter, default ON for institutional flow unless the broker's contract note shows otherwise (I).
- SIPF: BPI Trade lists "SIPF 0.001% of gross trade amount" and "SEC 0.005%" as "additional for block sale transactions" (PHP 20m regular block sale; PHP 50m special block sale). [^bpi-trade-fees-faq] — S. SRC IRR Rule 36.5 requires broker-dealers to be members of an "Accredited Trust Fund" that maintains a Customer Protection Fund. [^sec-2015-src-irr:120] — P. The SIPF contribution schedule itself was not found in a primary source.
- Rounding: COL states every computed charge is rounded to hundredths using symmetric arithmetic rounding before totalling. [^colfinancial-fees-faq] — S
- Scrip-related fees (irrelevant to scripless institutional flow): PDTC upliftment PHP 50 per certificate request; transfer-agent direct-transfer PHP 100 + VAT and cancellation PHP 20 + VAT. [^pse-investing-at-pse] — P. First Metro: upliftment PHP 250 per certificate (from 1 Jul 2024). [^firstmetrosec-fees-and-charges] — S
- Settlement cycle: T+2 (clearing days) per the exchange page; the SEC approved the T+2 go-live for 24 Aug 2023 (first T+2 trading day; its trades settled 29 Aug 2023). [^pse-investing-at-pse] [^sccp-memo-04-0823-t2-go-live:1] — P

**C. Stock transaction tax (STT) — rate history and rules**
- Original NIRC (RA 8424, effective 1 Jan 1998): 1/2 of 1% (0.5%) of gross selling price on listed shares sold through the local exchange, paid by the seller; plus an IPO tax of 4% / 2% / 1% of gross selling price (≤25%; >25% to 33 1/3%; >33 1/3% of outstanding shares sold), paid by the issuer (primary) or the seller (secondary). [^ra-8424-nirc-1997:165] [^ra-8424-nirc-1997:166] [^ra-8424-nirc-1997:270] — P (as originally enacted)
- TRAIN (RA 10963, approved 19 Dec 2017, effective 1 Jan 2018): Sec. 127(A) raised to 6/10 of 1% (0.6%). [^ra-10963-train:24] [^ra-10963-train:54] — P
- Bayanihan II (RA 11494, approved 11 Sep 2020; effective on publication): "Section 127(B) of the NIRC ... is hereby repealed" — the IPO tax. [^ra-11494-bayanihan-ii:20] [^ra-11494-bayanihan-ii:25] — P. CMEPA later re-used subsection (B) for foreign-listed shares, so the current Code text has no IPO tax. [^ra-12214-cmepa:16] — P (the repeal-is-permanent reading is partly I: Bayanihan II Sec. 18 limits the Act's life to the 18th Congress "except as otherwise specifically provided").
- **CMEPA (RA 12214, approved 29 May 2025; effective 1 July 2025)**: Sec. 17 rewrites NIRC Sec. 127: "(A) ... every sale, exchange, or other disposition of shares of stock and other securities listed and traded through a local stock exchange, other than the sale by a dealer in securities, in lieu of capital gains tax, a tax at the rate of one-tenths of one percent (1/10 of 1%) of the gross selling price or gross value in money ... paid by the seller or transferor"; dealer gains are ordinary income; "(B)" same 1/10 of 1% for shares of a domestic corporation listed and traded through a **foreign** stock exchange. [^ra-12214-cmepa:16] — P
- Effectivity: Sec. 29 of the signed Act: "shall take effect on July 1, 2025, following its complete publication". [^ra-12214-cmepa:25] — P. BIR RMC 60-2025 (11 Jun 2025) circularizes the Act and the President's veto message and says the Act "will take effect on July 1, 2025". [^bir-rmc-60-2025-cmepa-circular:1] — P. **Discrepancy**: the lawphil HTML transcription of Sec. 29 reads "after fifteen (15) days following the completion of its publication"; the official signed PDF and the BIR say 1 July 2025 — rely on the PDF. [^ra-12214-lawphil-html] — S
- BIR RR 20-2025 (signed by the Finance Secretary 29 Jul 2025; received/issued 5 Aug 2025): STT = 1/10 of 1% (0.1%) of gross selling price/gross value in money, effectivity 1 Jul 2025, for local-exchange sales (Sec. 3) and for domestic-company shares listed abroad (Sec. 4); dealer gains = ordinary income (Sec. 5). [^bir-rr-20-2025-stt:1] [^bir-rr-20-2025-stt:2] [^bir-rr-20-2025-stt:3] [^bir-rr-20-2025-stt:4] — P
- Who pays/collects: seller pays; the stock broker who effected the sale collects and remits to the BIR "within five (5) banking days from the date of collection" and files a weekly return on Mondays with the exchange secretary; for foreign-exchange-listed shares the selling shareholder (or broker/representative) remits within 10 banking days. [^ra-12214-cmepa:16] [^ra-12214-cmepa:17] [^bir-rr-20-2025-stt:3] — P. Transfer-registration bar: no transfer is registered unless proof of tax payment is filed with the transfer agent/corporate secretary (RR 20-2025 Sec. 7). [^bir-rr-20-2025-stt:3] [^bir-rr-20-2025-stt:4] — P
- Filing mechanics at launch: the BIR Tax Advisory of 4 Jul 2025 (Commissioner Lumagui; attached to PSE CN-2025-0032 of 15 Jul 2025) confirms the 1/10 of 1% rate for local-exchange sales and the new coverage of domestic-company shares listed abroad, says the revised rate (and the foreign-exchange transaction type) was not yet in BIR Form 2552 on eBIRForms/eFPS, and advises manual filing and payment at any authorized agent bank (citing RR 4-2024 and RMC 87-2024); foreign-exchange transactions are to use ATC "PT 203" on Form 2552; a revenue issuance would follow once the rate and ATC are available electronically (that follow-up issuance was not located). [^pse-cn-2025-0032-bir-stt-advisory:1] [^pse-cn-2025-0032-bir-stt-advisory:2] — P. PSE's new back-office portal (NTE) lists a "Weekly Tax Report" module. [^pse-nte-broker-forum-2026-07-09:13] — P
- Definitions used by the regulation: "dealer in securities" = a merchant with an established place of business regularly buying and re-selling to customers; "shares of stock" includes mutual fund certificates; "securities" is broad. [^bir-rr-20-2025-stt:2] [^ra-12214-cmepa:2] — P

**D. Special cases for STT**
- Block sales / crosses: PSE regular block sale = at least PHP 20m, price within ±5% of the last adjusted closing price, T+0 settlement; special block sale at least PHP 50m; the applicant must certify the facility "is not being used to circumvent the provisions of the National Internal Revenue Code". [^pse-implementing-guidelines-trading-rules:23] [^pse-implementing-guidelines-trading-rules:24] — P (guidelines edition in KB, undated; the new trading engine, go-live scheduled 23 Nov 2026, adds a "Negotiated Trade" — a pre-arranged transaction between different clients at a price within ±5% of the full-day VWAP, no volume/value restriction, executed in a 15-minute window after run-off/trading-at-last [^pse-nte-broker-forum-2026-07-09:8] [^pse-nte-broker-forum-2026-07-09:9] — P). For REIT securities the REIT Act says "any sale ... through the Exchange, including block sales or cross sales with prior approval from the Exchange, shall be subject to the stock transaction tax" and exempt from DST. [^ra-9856-reit-act:21] — P. For non-REIT stocks I infer the same (statute reaches any sale "listed and traded through a local stock exchange") — I. Off-exchange sales of listed shares are not "traded through" the exchange and fall to the 15% net capital gains tax regime plus DST (below) — I.
- ETFs: no PSE/BIR text found. The statutory definition of "shares of stock" includes "mutual fund certificates" and Sec. 127 reaches "shares of stock and other securities listed and traded", so PSE-listed ETF shares should bear 0.1% STT on sale. [^ra-12214-cmepa:2] [^ra-12214-cmepa:16] — I. DST: CMEPA exempts original issuance/redemption of shares in a mutual fund company and issuance of fund-participation certificates. [^ra-12214-cmepa:20] — P
- REITs: STT on sale of listed REIT securities through the exchange (the statute names Sec. 127(a)); exempt from DST on exchange sales; exempt from the (now repealed) IPO tax. [^ra-9856-reit-act:21] — P. Dividend tax is in Section 2.
- IPO shares: no IPO tax since Sep 2020 (above). Issuer pays DST on primary issuance at 0.75% of par (or of consideration if no-par). A selling-shareholder tranche sold "through IPO" before listing is no longer covered by the old IPO-tax/DST carve-outs (CMEPA's Sec. 199(e) now exempts only shares "listed and traded"). Treatment of that tranche is **not addressed in any source I found**; likely 15% capital gains tax + DST — I.
- Securities borrowing and lending (SBL): borrowing/lending of PSE-listed shares and delivery/return of collateral or "Equivalent Shares" are not subject to STT (Sec. 127), capital gains tax or DST **provided** a valid Master Securities Lending Agreement (MSLA) is executed, registered with and approved by the BIR, and the SBL program is SEC-compliant and PSE-supervised. [^bir-rr-10-2006-sbl:4] [^bir-rr-1-2008-sbl:4] — P. The borrower registers the MSLA (PHP 5,000; within 2 weeks if executed in the Philippines, 1 month if abroad); borrowing period max 2 years. [^bir-rr-10-2006-sbl:7] [^bir-rr-10-2006-sbl:8] — P. "Deemed sale" (CGT 15% + DST, no STT because it is outside the exchange) if shares are not returned, used outside specified purposes, borrower defaults, MSLA invalid, or registration missing/late. [^bir-rr-10-2006-sbl:9] [^bir-rr-10-2006-sbl:10] — P. The actual short sale is an ordinary sale and bears STT (PSE FAQ: "The subsequent sale of the borrowed securities (short sale) ... shall be subject to the regular taxes"). [^pse-sbl-short-selling-page] — P/S (exchange FAQ).
- **Conflict on manufactured dividends**: RR 10-2006 as amended by RR 1-2008 says receipt of manufactured dividends "shall not be a taxable income of the Lender" and payment is not deductible for the borrower. [^bir-rr-10-2006-sbl:4] [^bir-rr-1-2008-sbl:5] — P. The PSE's SBL FAQ says manufactured dividends/substitute payments "shall be taxed as other income in the hands of the Lender". [^pse-sbl-short-selling-page] — S/P (exchange FAQ). No later BIR issuance reconciling the two was found; no post-CMEPA SBL-specific BIR issuance was found.

**E. Documentary stamp tax (DST)**
- Original issue of shares (NIRC Sec. 174): TRAIN PHP 2.00 per PHP 200 of par (1%); CMEPA lowers to "seventy-five percent of one percent (75% of 1%)" of par, or of actual consideration for no-par shares, or actual value for stock dividends; applies to documents/transactions on or after 1 Jul 2025. [^ra-10963-train:37] [^ra-12214-cmepa:17] [^ra-12214-cmepa:18] [^bir-rr-19-2025-dst:1] [^bir-rr-19-2025-dst:2] — P
- Transfers of shares (Sec. 175): PHP 1.50 per PHP 200 of par value (0.75% of **par**, not price); no-par: 50% of the DST paid on original issue. [^ra-10963-train:38] — P. CMEPA amended Secs. 174, 176, 179, 190, 199 only, so Sec. 175 is unchanged (my reading of the amended-sections list on [^ra-12214-cmepa:1]) — I.
- Exemption (Sec. 199(e)): "Sale, exchange, redemption, or other disposition of shares of stock listed and traded through a local or foreign stock exchange" — foreign-exchange limb and "redemption" are new; the old "or through initial public offering" wording is gone. [^ra-12214-cmepa:20] [^bir-rr-19-2025-dst:3] — P
- Foreign-issued certificates (Sec. 176): 75% of 1% of transaction value, paid by seller/transferor. [^ra-12214-cmepa:18] — P

**F. Worked example: PHP 10,000,000 bought then sold at the same price (settlement T+2, no price change)**

Per-side components (basis points of gross value): commission `c`; VAT on commission `0.12c`; PSE fee 0.50; VAT on PSE fee 0.06; SCCP 1.00 (VAT-inclusive); SEC "SRC fee" 0.50 (listed by the PSE and by the OECD's 2024 table as charged to buyer and seller; several retail brokers do not pass it through). Sell side adds STT 10.00. "Full stack" below follows the PSE's own illustration; the "retail-broker stack" omits the SRC fee.

| Component | Buy (PHP) | Sell (PHP) |
|---|---|---|
| Gross value | 10,000,000.00 | 10,000,000.00 |
| Commission @0.25% (headline retail-online rate) | 25,000.00 | 25,000.00 |
| VAT 12% on commission | 3,000.00 | 3,000.00 |
| PSE fee 0.005% | 500.00 | 500.00 |
| VAT 12% on PSE fee | 60.00 | 60.00 |
| SCCP clearing fee 0.01% (VAT-incl.) | 1,000.00 | 1,000.00 |
| SEC "SRC fee" 0.005% | 500.00 | 500.00 |
| STT 0.1% (seller only) | – | 10,000.00 |
| **Full-stack total** | **30,060.00** (30.06 bp) | **40,060.00** (40.06 bp) |
| *Retail-broker stack (no SRC fee) total* | *29,560.00* | *39,560.00* |

- Round trip at c = 25 bp, full stack: **PHP 70,120.00 = 70.12 bp** (buy cash out 10,030,060.00; sell net proceeds 9,959,940.00). This reproduces the PSE's own PHP 10,000 ticket scaled x1,000 (buy outlay 10,030.06; sell net 9,959.94). [^pse-investing-at-pse] — arithmetic from P inputs. Retail-broker stack (no SRC fee): **PHP 69,120.00 = 69.12 bp** (buy 10,029,560.00; sell net 9,960,440.00). [^colfinancial-fees-faq] [^firstmetrosec-fees-and-charges] — S
- Closed form (full stack): `RT_bp = 2.24c + 14.12` (`2.24c + 13.12` without the SRC fee), c in bp. Commission sensitivity, full stack: c = 15 bp → PHP 47,720 (47.72 bp); c = 10 bp → PHP 36,520 (36.52 bp); c = 5 bp → PHP 25,320 (25.32 bp). Institutional commission levels are assumptions, not sourced; the fixed part (14.12 bp, of which STT 10 bp) is broker-independent.
- Regime comparison at c = 25 bp, same full-stack assumptions: **pre-CMEPA (STT 0.6%)**: buy 30,060, sell 90,060, RT **PHP 120,120 (120.12 bp)** — matching the OECD's 2024 PHP 10,000 illustration of 0.3% buyer / 0.9% seller cost. [^oecd-capital-market-review-philippines-2024:45] — P/S (OECD, pre-CMEPA). **Post-CMEPA (STT 0.1%)**: RT 70,120 (70.12 bp). The CMEPA saving is exactly the STT cut, 50 bp = PHP 50,000 per PHP 10m round trip; on the retail-broker stack the comparison is PHP 119,000 (COL-style fee page before the 4 Sep 2025 VAT change) to PHP 69,120.
- OECD context (published before CMEPA): total buy+sell trading costs in the Philippines were 1.2% of traded value vs a 0.66% peer average, driven by the 0.6% seller tax; OECD recommended assessing an STT reduction. [^oecd-capital-market-review-philippines-2024:46] — P/S. FTSE still rates "transaction costs" as Not Met in March 2026 (Section 4).
- Block/cross add-on per BPI Trade: SEC 0.005% + SIPF 0.001% = +0.6 bp per side if applicable. [^bpi-trade-fees-faq] — S
- Not in the figure: bid-ask spread and impact, PHP/USD conversion spread, custody/safekeeping, bank transfer charges (First Metro lists PDDTS charges as "actual fees varies per bank"), withholding taxes on dividends/interest, SBL fees. [^firstmetrosec-fees-and-charges] — S

### Inferences
- Because STT is levied on the gross value of every sale and is not netted for intraday round trips, a strategy turning over capital N times a year pays about 10 bp x N in STT alone; the fixed component of the round trip (14.12 bp full stack, 13.12 bp without the SRC fee) is independent of broker.
- A non-resident fund trading for its own account through brokers is not a "dealer in securities" under the RR 20-2025 definition (no established place of business reselling to customers), so STT, not ordinary income tax, applies. [^bir-rr-20-2025-stt:2]
- VAT on commission and on the PSE fee is likely a sunk cost for a non-resident investor (no Philippine VAT registration to credit it against).

### Gaps
- Institutional/global broker commission rates after the 18 Apr 2024 deregulation (no public survey found; the pre-2024 floor was 0.25% for any trade up to PHP 100m, so post-2024 negotiated rates below that are plausible but undocumented).
- Primary notice for VAT on the PSE fee (4 Sep 2025) and the primary basis/pass-through of the 0.005% SRC fee and the SIPF contribution rate.
- Whether the BIR has ruled on ETF STT, selling-shareholder IPO tranches, and post-CMEPA SBL; content of the President's veto message (annex of RMC 60-2025 not in the 1-page archive).
- Whether the new Nasdaq Eqlipse engine (2026) changes any fee mechanics.

### Execution implications
- Model explicit cost as `fee(side) = gross·[1.12c + 0.56bp + 1.00bp + 0.50bp(SRC, toggle)] + 10bp·gross·1[sell]`; keep STT and exchange fees as separate, dated parameters (they change by statute/notice; commission by contract).
- STT makes sells 10 bp more expensive than buys: asymmetric hurdle for signals; avoid sell-then-rebuy churn; for shorts the STT hits on the opening short sale (SBL borrow/return is outside STT only under a BIR-registered MSLA).
- Block/negotiated trades are not a tax shelter: STT still applies when executed through the exchange; off-exchange transfers trigger 15% capital gains tax and DST.
- Do not trust broker fee pages for tax rates (COL page dated 10 Jul 2025 predates VAT on the PSE fee; some pages still show 0.6%); source rates from the statute/RR and the exchange page, and version them with effective dates (1 Jul 2025; 4 Sep 2025).
- Tick/board-lot effects are out of scope here; commission minimums (e.g., BPI PHP 20) matter only for very small child orders.

---

## 2. Investor-level taxes (dividends, capital gains, REIT dividends, treaty/tax-sparing route)

### Takeaway
Listed shares: no capital-gains tax, only the 0.1% seller-side STT. Cash dividends from a domestic corporation: 10% final for residents; **20%** for non-resident aliens engaged in business; **25%** for non-resident aliens not engaged in business; for non-resident foreign corporations (the typical fund vehicle) **25%**, reducible to **15%** final if the home country grants a deemed-paid credit of 10 points or imposes no tax on the dividend (BIR's reading in RR 21-2025), or to a treaty rate. REIT dividends: **10%** final even for non-residents (unless a treaty gives less). Unlisted/off-exchange share gains: 15% of net gain. CMEPA did not change the dividend rates; the PSE's own "Investing at PSE" page still shows the pre-2021 figure of 30% for non-resident corporations.

### Cited findings
Quick matrix (rates in force from 1 Jul 2025 per RR 21-2025; "treaty" = lower rate if a treaty applies; sources in the bullets below):

| Payee | Gain on listed shares sold on the PSE | Gain on unlisted / off-exchange shares | Cash dividends from a domestic corporation | REIT dividends | Bank/deposit interest |
|---|---|---|---|---|---|
| Resident citizen / resident alien | STT 0.1% on gross (seller) | 15% final on net gain | 10% final | 10% final | 20% final |
| Non-resident alien engaged in trade/business (>180 days in a year) | STT 0.1% | 15% | 20% | 10% | 20% |
| Non-resident alien not engaged | STT 0.1% | 15% (or treaty) | 25% final (or treaty) | 10% (or lower treaty) | 25% (or treaty) |
| Domestic / resident foreign corporation | STT 0.1% (dealers: ordinary income) | 15% | exempt | exempt | 20% |
| **Non-resident foreign corporation (typical fund vehicle)** | STT 0.1% | 15% (or treaty) | **25%; 15% if home-country credit/no-tax condition met; or treaty** | 10% (or lower treaty) | 25% (or treaty) |

- What CMEPA changed and did not change for investor-level tax: it left the dividend rates untouched (the 10% / 20% / 25% individual rates and the NRFC provisions pre-date it — the PSE's older table shows the same 10/20/25 for individuals; the NRFC move from 30% to 25% came from CREATE, not CMEPA), unified the final tax on bank interest/deposit substitutes/trust funds at 20% (Sec. 24(B)(1), 27(D)(1)), extended the 15% unlisted-share gains tax to shares of foreign corporations not traded on any exchange, introduced STT on domestic shares listed abroad and widened STT to "other securities". [^ra-12214-cmepa:5] [^ra-12214-cmepa:6] [^ra-12214-cmepa:8] [^ra-12214-cmepa:16] [^bir-rr-21-2025-cmepa-income:3] [^bir-rr-21-2025-cmepa-income:4] [^pwc-tax-summaries-ph-income-determination] — P/S (the "pre-dates it" comparison relies on the PSE page [^pse-investing-at-pse] — I).
- Individuals — cash/property dividends from a domestic corporation: 10% final (citizens and resident aliens); non-resident alien engaged in trade or business (more than 180 days in a calendar year = "doing business"): 20% (Sec. 25(A)(2)); non-resident alien not engaged in trade or business: 25% final (Sec. 25(B)). [^ra-12214-cmepa:5] [^ra-12214-cmepa:6] [^bir-rr-21-2025-cmepa-income:4] [^bir-rr-21-2025-cmepa-income:5] — P
- Domestic and resident foreign corporations: intercorporate dividends from a domestic corporation exempt. [^bir-rr-21-2025-cmepa-income:7] — P
- Non-resident foreign corporation (NRFC): general 25% of gross income from Philippine sources (Sec. 28(B)(1), "effective January 1, 2021" 25%); dividends specifically: final withholding tax 15% (Sec. 28(B)(5)(b), CREATE RA 11534) "subject to the condition that the country in which the nonresident foreign corporation is domiciled shall allow a credit against the tax due ... taxes deemed to have been paid in the Philippines" equal to the difference between the regular rate in Sec. 28(B)(1) and 15% (i.e., 10 points since the 25% rate). [^ra-12214-cmepa:9] [^ra-11534-create:11] [^ra-11534-create:12] — P. CMEPA left Sec. 28(B)(5)(b) untouched ("XXX"). [^ra-12214-cmepa:9] — P
- BIR's restatement (RR 21-2025, effective 1 Jul 2025): NRFC dividends from a domestic corporation: 15% "subject to the condition that the country of residence of the corporate shareholder allows a credit of 10% tax deemed to have been paid in the Philippines **or that the country of residence ... does not impose any tax on the dividends** (or the tax treaty rate)". [^bir-rr-21-2025-cmepa-income:7] [^bir-rr-21-2025-cmepa-income:8] — P. NRFC interest income and other fixed/determinable income: 25% (or treaty rate). [^bir-rr-21-2025-cmepa-income:7] — P
- Treaty ceilings on dividends (maximum WHT, lower/higher rate by ownership threshold; "last reviewed 01 August 2026"): United States 20/25; United Kingdom 15/25; Singapore 15/25; Japan 10/15; Netherlands 10/15; Switzerland 10/15; France 10/15; Germany 5/10/15; Canada 15/25; Australia 15/25; Korea 10/25; Malaysia 15/25; Thailand 10/15; UAE 10/15; non-treaty 15/25 (the domestic 15% needs the home-country condition above). Substantial-ownership thresholds are 10% or 25% depending on treaty. [^pwc-tax-summaries-ph-wht] — S. Ireland, Luxembourg, Hong Kong and Cayman Islands did not appear in the table extract I took (no row captured) — check.
- Capital gains: shares sold through the exchange are "in lieu of capital gains tax" (STT only). [^ra-12214-cmepa:16] — P. Shares **not** traded on a local/foreign exchange: 15% final on **net** capital gains for individuals (Sec. 24(B)(3)), domestic corporations (Sec. 27(D)(4)), non-resident aliens not in business (via Sec. 25(B)) and NRFCs (Sec. 28(B)(5)(c)); return within 30 days of each transaction and a final consolidated return by 15 April (individuals; corporations by the 15th day of the 4th month after year-end). [^ra-12214-cmepa:5] [^ra-12214-cmepa:10] [^ra-12214-cmepa:14] [^bir-rr-21-2025-cmepa-income:4] [^bir-rr-21-2025-cmepa-income:5] [^bir-rr-21-2025-cmepa-income:8] — P. TRAIN (from 1 Jan 2018) already fixed the unlisted-share rate at a flat 15%. [^ra-10963-train-html] — S (HTML copy)
- Treaty hook for unlisted-share gains: NIRC Sec. 56(A)(3) as amended by CMEPA — if the seller "submits proof of the intention to avail of the benefit of exemption of capital gains under existing special laws or tax treaties, no such payments shall be required" at filing, but if the seller later fails to qualify the tax becomes immediately due with penalties. [^ra-12214-cmepa:15] — P. PwC separately notes that "Tax treaties are explicitly recognised as a basis for capital gains tax exemption" and describes the NRFC dividend rule identically to RR 21-2025 (25% general; 15% if the home country either does not tax such dividends or allows a deemed-paid credit of 10 points), and confirms Sec. 175 DST (PHP 1.50 per PHP 200 par) and STT 0.1% including "other securities" and foreign-listed domestic shares. [^pwc-tax-summaries-ph-income-determination] [^pwc-tax-summaries-ph-other-taxes] — S. Whether STT itself (a transaction tax "in lieu of" capital gains tax) can be displaced by a treaty capital-gains article is **not answered** by any source retrieved.
- REIT dividends (RA 9856 Sec. 14): "final tax of ten percent (10%), unless" received by a non-resident alien or non-resident foreign corporation entitled to a treaty rate below 10%, or by a domestic/resident foreign corporation (exempt); overseas Filipino investors are exempt for seven years from the effectivity of the implementing tax regulations (reckoning date not settled in the sources; irrelevant for foreign funds). [^ra-9856-reit-act:21] — P. So an NRFC pays 10% on REIT dividends, not 15%/25%.
- Non-resident REIT investment is BSP-registrable through registering AABs (full repatriation of capital and earnings). [^pse-cn-2020-0052-nonresident-reit-investment:1] — P
- The exchange's own "Investing at PSE" withholding table is stale: it shows 30% for non-resident foreign corporations with a 15% route "equivalent to 15%" credit — the pre-CREATE regime (CREATE cut the rate to 25%; credit now 10 points). [^pse-investing-at-pse] [^ra-11534-create:12] — P vs P (conflict; statute prevails).
- Wash-sale and capital-loss limits were also touched by CMEPA (Secs. 38, 39) but only matter for taxpayers with income-tax capital gains; listed-share sales on the PSE are outside them. [^ra-12214-cmepa:2] — I

Worked dividend illustration (gross cash dividend PHP 1,000,000): NRFC at 25% → tax 250,000, net 750,000; NRFC at 15% → 150,000 / 850,000; US-resident corporation holding at least 10% voting (treaty 20%) → 200,000 / 800,000; REIT dividend to an NRFC → 100,000 / 900,000. [rates above; arithmetic] — I

### Inferences
- A Cayman/BVI-domiciled corporate fund (home country imposes no tax on dividends) should, on RR 21-2025's wording, qualify for 15% rather than 25%; a US-domiciled corporate holder (taxes foreign dividends, no tax-sparing credit) is more likely stuck with 25% (or 20% at 10%+ ownership). Entity classification of the fund vehicle (partnership, trust, UCITS/ICAV) and beneficial-ownership look-through are fact-specific. — I
- Dividend capture for non-residents is expensive: withholding of 15–25% (REIT 10%) versus 10 bp STT on exit.

### Gaps
- BIR treaty-relief procedure (certificate of residence/CORTT and application forms, relief-at-source vs refund) was not retrieved; I only have a recollection (RMO 14-2021) which I have **not** verified. Whether STT is treated as a percentage tax outside treaty capital-gains articles: not resolved (KPMG article could not be read).
- Treaty rows for Ireland/Luxembourg/Hong Kong not captured.
- Treatment of stock dividends, rights, and corporate-action taxes for non-residents not researched.

### Execution implications
- Bake a dividend-withholding parameter per account/vehicle (10/15/20/25%) into ex-dividend and index-event trading; REIT names carry a lower rate.
- Capital-gains tax is irrelevant for on-exchange trading; STT is the only transaction tax. Off-exchange/privately negotiated purchases of listed shares create 15% gain tax and DST exposure.
- Cash held in PHP earns interest taxed at 25% (NRFC) — keep PHP balances to settlement needs.

---

## 3. Foreign-ownership limits (constitutional/statutory caps, RA 11659, RA 11647, current negative list, monitoring, behaviour at the limit)

### Takeaway
The in-force negative list is the **13th Regular Foreign Investment Negative List (EO 113, signed 13 Apr 2026)**, replacing the 12th (EO 175, 27 Jun 2022) and the 11th (EO 65, 29 Oct 2018). Hard caps: 0% mass media (except recording) and several other activities; 25% private recruitment/defence-construction; 30% advertising; 40% for land ownership, public utilities (now a six-item list after RA 11659), natural resources, educational institutions, certain retail, etc. Foreign ownership of listed stocks is policed by the PSE trading system using an account-level Local/Foreign flag, daily issuer reporting, and a real-time "foreign shares available" market-data field; breaches must be unwound the same or next day. Two-tier Class A/B share lines are being abolished by SEC MC 10-2025. In practice the **40% limit is the norm**: on PSE EDGE (6 Oct 2026) 218 of 281 listed companies — about 93.5% of the market capitalisation shown — carry a 40% foreign ownership limit (including banks, telecoms, REITs and holding companies, not just land developers and utilities); 46 carry 100% (e.g. Jollibee, Century Pacific, Monde Nissin) and 15 carry 0% (broadcasters, some mining). MSCI rates the Philippine FOL level and foreign room "-"; FTSE rates foreign-ownership restrictions "Restricted" and classifies the market as Secondary Emerging.

### Cited findings
**A. Legal framework**
- Constitution Art. XII: Sec. 2 (natural resources; co-production/joint-venture/production-sharing only with Filipino citizens or corporations at least 60% Filipino-owned; large-scale minerals/petroleum technical or financial assistance agreements with the President); Sec. 7 (private lands transferable only to those qualified to hold public-domain lands); Sec. 10 (Congress may reserve investment areas to at least 60% Filipino); Sec. 11 (public-utility franchises only to corporations at least 60% Filipino-owned; foreign participation in the governing body limited to its proportionate share of capital; executive/managing officers must be citizens). Art. XIV Sec. 4(2): schools at least 60% Filipino-owned and control with citizens. Art. XVI Sec. 11: mass media "wholly-owned and managed" by citizens; advertising at least 70% Filipino. [^constitution-1987-lawphil] — P
- "Capital" for the 60/40 rule: Supreme Court in *Gamboa v. Teves* (28 Jun 2011; MR denied with finality 9 Oct 2012): "Full beneficial ownership of 60 percent of the outstanding capital stock, coupled with 60 percent of the voting rights, is required", applied to voting and non-voting shares. [^gamboa-v-teves-2012-lawphil] — P
- RA 11647 (FIA amendments; approved 2 Mar 2022; effective 15 days after publication): foreign investors may own 100% of "domestic market enterprises" outside the negative list; micro/small domestic market enterprises with paid-in equity below US$200,000 are reserved to Philippine nationals; the threshold drops to US$100,000 if the enterprise involves advanced technology (DOST), is an endorsed startup/enabler, or directly employs at least 15 Filipinos; List B amendments no more often than every two years. [^ra-11647-foreign-investments-act-amendments:6] [^ra-11647-foreign-investments-act-amendments:8] — P
- RA 11659 (Public Service Act amendments; approved 21 Mar 2022; effective 15 days after publication): "public utility" now means only distribution of electricity, transmission of electricity, petroleum/petroleum-product pipeline transmission systems, water and wastewater/sewerage pipeline systems, seaports, and public utility vehicles; "No other person shall be deemed a public utility unless otherwise subsequently provided by law". [^ra-11659-public-service-act-amendments:4] — P. Declared aim: "rationalizing foreign equity restrictions by clearly defining the term 'public utilities'". [^ra-11659-public-service-act-amendments:1] — P. Sec. 25 reciprocity: foreign nationals may not own more than 50% of entities operating "critical infrastructure" unless their country gives reciprocity. [^ra-11659-public-service-act-amendments:13] — P. The repealing clause amends the foreign-ownership limits in the BOT law, domestic shipping, civil aviation/aeronautics, toll operation, TNC classification and the telecom public-utility classification (RA 7925). [^ra-11659-public-service-act-amendments:14] [^ra-11659-public-service-act-amendments:15] — P
- **13th RFINL (EO 113, 13 Apr 2026; effective 15 days after publication in the Official Gazette or a newspaper — publication date not verified)**: List A — no foreign equity: mass media except recording, internet business (DOJ Op. 40 s.1998), corporate practice of architecture, cooperatives, private security agencies, small-scale mining, marine resources, cockpits, nuclear/biological/chemical weapons, firecrackers; up to 25%: private recruitment, defence-related construction; up to 30%: advertising; up to 40%: retail trade below the paid-up-capital threshold, natural resources (with exceptions for FTAA and renewable energy), ownership of private lands, public utilities (the six-item list), educational institutions, rice/corn, government procurement categories, commercial fishing vessels, condominium units; up to 100% (50% without reciprocity): operation and management of telecommunications (Sec. 25 RA 11659). List B (security/health/morals/SMEs) up to 40%: PNP-regulated items, materiel, dangerous drugs, sauna/massage, gambling, micro/small domestic enterprises below US$200,000 (US$100,000 with the exceptions). Retail: foreign retailers allowed with at least PHP 25m paid-up capital and PHP 10m per store (RA 11595). [^eo-113-2026-13th-finl:1] [^eo-113-2026-13th-finl:3] [^eo-113-2026-13th-finl:4] [^eo-113-2026-13th-finl:5] [^eo-113-2026-13th-finl:6] [^eo-113-2026-13th-finl:7] — P
- Superseded list for audit trail: 12th RFINL, EO 175 (27 Jun 2022), "replacing the Eleventh". [^eo-175-2022-12th-finl:1] — P
- REITs that own Philippine land must observe foreign-ownership limits (RA 9856 Sec. 6). [^ra-9856-reit-act:9] — P
- The negative list does not name banks or insurers; sector statutes (not retrieved) govern them. — I/gap

**A2. Quick reference — maximum foreign equity under the 13th RFINL (EO 113) and its legal basis** [^eo-113-2026-13th-finl:3] [^eo-113-2026-13th-finl:4] [^eo-113-2026-13th-finl:5] [^eo-113-2026-13th-finl:6] [^eo-113-2026-13th-finl:7] — P

| Max foreign equity | Activities (List) | Basis cited in the order |
|---|---|---|
| 0% | Mass media except recording; internet business; corporate practice of architecture; cooperatives; private security agencies; small-scale mining; marine resources; cockpits; nuclear, biological, chemical, radiological weapons and anti-personnel mines; firecrackers (List A) | Const. Art. XVI Sec. 11(1); special laws |
| 25% | Private recruitment; defence-related construction contracts (List A) | Labor Code Art. 27; CA 541 |
| 30% | Advertising (List A) | Const. Art. XVI Sec. 11(2) |
| 40% | Land ownership; public utilities (six categories); natural resources (large-scale minerals/petroleum under President-signed financial/technical agreements and renewable energy excepted); educational institutions (with exceptions); retail trade below the paid-up-capital threshold; rice and corn; government procurement; commercial fishing vessels; condominium units (List A). Also List B items: PNP-regulated products, materiel, dangerous drugs, sauna/massage, gambling, micro/small domestic-market enterprises below US$200,000 (US$100,000 with exceptions) | Const. Art. XII Secs. 2, 7, 11; Art. XIV Sec. 4(2); RA 11659 Sec. 4; RA 11595; RA 11647 |
| up to 100% (50% without reciprocity) | Operation and management of telecommunications (List A item 25) | RA 11659 Sec. 25 and IRR Sec. 45 |

(Item numbers/exceptions are from my OCR of the scanned order; the grouping of items 19–24 under the 40% heading follows the page layout and should be re-checked against the Official Gazette text before quoting individual items.)

**B. Monitoring at the listed-company and market level**
- PSE Consolidated Listing and Disclosure Rules, Art. VII Sec. 17.13: issuers with unclassified shares and foreign ownership limits must report foreign holdings monthly (last working day of the first week) and "on a real time basis" — in practice a daily update by 4:00 pm whenever foreign shareholdings change, including unlisted shares, via the PSE disclosure system (ODISY, now EDGE); issuers already split into Class A/B shares, or wholly foreign-ownable/non-ownable, are exempt. [^pse-listing-disclosure-rules:157] [^pse-listing-guidance-notes:67] [^pse-listing-guidance-notes:68] [^pse-listing-guidance-notes:72] — P
- PSE Foreign Ownership Level (FOL) report specification v1.1 (Sept 2019): monthly Excel file `FOL_yyyymm.xls` emailed every 8th day of the following month with company FOL (e.g. 40%), company foreign-owned shares, outstanding shares, and per-security class (C/P/U) data; effective 18 Jun 2008. [^pse-fol-spec-v1-1:2] [^pse-fol-spec-v1-1:3] — P
- Order-level flag: each TP account code carries a Nationality Flag (Local/Foreign); changing it creates a new account code; aggregated/bundled accounts must be classified local or foreign and "for purposes of foreign ownership monitoring, when posting an Order of combined local and foreign client Orders, the foreign bundled account shall be used"; unbundling by 12 noon T+1 (or 5 pm T+0 if the nationality flag changes). [^pse-implementing-guidelines-trading-rules:21] [^pse-implementing-guidelines-trading-rules:22] — P
- Depository level: participants with foreign clients must keep Client-Foreign securities accounts/sub-accounts, segregating non-Filipino holdings. [^pdtc-depository-rules-1997:14] [^pdtc-depository-rules-1997:15] — P (1997 rules)
- Real-time feed: the ITCH market-data feed carries a **"Foreign Shares Available" [f]** message per product code, with an Ownership Rule ID, a sign (+/–) and the number of shares currently available for foreign ownership; sent at start of day and dynamically; products that do not allow foreign ownership send no [f] message. [^pse-itch-equities-feed-spec-v2-3:19] [^pse-itch-equities-feed-spec-v2-3:20] [^pse-itch-equities-feed-spec-v2-3:22] [^pse-itch-equities-feed-spec-v2-3:25] — P (legacy X-stream feed spec v2.3, valid until the new trading engine's scheduled 23 Nov 2026 go-live [^pse-nte-broker-forum-2026-07-09:9]; the successor Nasdaq Eqlipse feed spec was not found, so whether and how the foreign-shares-available field is carried after cutover is unverified).
- SEC MC 10 s. 2025 (7 Aug 2025; effective 9 Aug 2025): recital — "the PSE maintains a system that strictly monitors and enforces foreign ownership limits given the current technological advances in its trading system". [^pse-cn-2025-0035-sec-declassification-mandate:2] [^pse-cn-2025-0036-declassification-effectivity:1] — P
- Beneficial-ownership disclosure: any person acquiring 5% beneficial ownership of a class of listed equity must file SEC Form 18-A within five business days with the issuer, the exchange and the SEC. [^sec-2015-src-irr:42] — P

**C. What happens at the limit**
- SEC MC 10-2025 Sec. 4: "In the remote event that a trade is executed and the same results in a breach of allowable foreign ownership limits, the foreign buyer, through its broker, shall immediately cause the disposition of such number of shares that caused the breach ... at the prevailing market price and shall return the proceeds to the foreign investor"; if discovered in trading hours, same day, otherwise at the next opening. Penalties under SRC Sec. 54. [^pse-cn-2025-0035-sec-declassification-mandate:3] — P
- Two-line (A/B) structure: the SEC's 1973 rules let Class B shares (open to aliens) trade on the regular board with buyers accepting A or B certificates; the SEC now cites "unfair disparity in price between Class A and Class B shares" and "unwarranted arbitrage for holders of Class B", and directs the end of A/B classification: listed companies must amend their articles within one year of effectivity — by **9 Aug 2026** — and in the interim buyers on the regular board receive the class they paid for. [^pse-cn-2025-0035-sec-declassification-mandate:2] [^pse-cn-2025-0035-sec-declassification-mandate:3] [^pse-cn-2025-0036-declassification-effectivity:1] — P
- No separate "foreign board" or alternative foreign price was found in any PSE rule, circular or feed spec (the feed has one order book per product code with a shares-available counter). — I (absence in the sources read)
- MSCI (June 2026): "All industries are in general subject to a 40 percent foreign ownership limit. These limitations affect more than ten percent of the Philippine equity market"; "More than one percent of the MSCI Philippines IMI is impacted by low foreign room". [^msci-accessibility-review-2026:43] — P/S (index-provider opinion; the "all industries" wording is MSCI's characterization and is broader than the 13th RFINL).

**D. FOL-constrained names (PSE EDGE "Stock Data" pages, each stamped "As of Oct 06, 2026"; counts and shares below are my computation from 284 pages parsed, source field "Foreign Ownership Limit(%)")** [^pse-edge-stock-data] — P for each limit; aggregates are I
- Distribution (281 company pages after excluding two foreign secondary listings, Manulife and Sun Life, whose limit is 100%): **218 companies at 40%**, 46 at 100%, 15 at 0%, one at 30% (National Reinsurance Corp. of the Philippines) and one at 60% (Ferronoux Holdings). Weighted by the market capitalisation shown on EDGE (about PHP 12.3 trillion in total), roughly **93.5% sits in 40%-limit companies**, 6.2% in 100%-limit companies and 0.3% in 0%-limit companies. This is consistent with MSCI's statement that "all industries are in general subject to a 40 percent foreign ownership limit" affecting "more than ten percent" of the market (the practical cause is the land-ownership rule: nearly every operating company holds land). [^msci-accessibility-review-2026:43] — P/I
- Largest 40%-limit companies (EDGE symbol; market cap PHP bn as of 6 Oct 2026): ICTSI (ICT, 1,827); SM Investments (SM, 601); BDO Unibank (BDO, 590); Bank of the Philippine Islands (BPI, 495); Manila Electric (MER, 478); SM Prime (SMPH, 471); Aboitiz Power (AP, 335); Ayala Corp (AC, 326); Metrobank (MBT, 276); San Miguel Food & Beverage (FB, 260); Emperador (EMI, 257); **PLDT (TEL, 238)**; **Globe (GLO, 224)**; Ayala Land (ALI, 220); Aboitiz Equity Ventures (AEV, 217); LT Group (LTG, 168); AREIT (153); San Miguel Corp (SMC, 140); JG Summit (JGS, 135); China Banking (CBC, 135); RL Commercial REIT (RCR, 130); Maynilad (MYNLD, 120); Universal Robina (URC, 120); PNB (116); Synergy Grid (SGP, 115); Puregold (PGOLD, 114); Apex Mining (APX, 110); ACEN (105); DMCI (DMC, 101); PAL Holdings (95); GT Capital (GTCAP, 90); Manila Water (MWC, 89); MREIT (85); Robinsons Land (RLC, 75); Union Bank (UBP, 70); Megaworld (MEG, 69). So banks, REITs, food/beverage conglomerates, telecoms and holding companies are all at 40%, not only land developers and utilities. Telecoms (TEL, GLO) still show 40% on EDGE even though RA 11659 removed telecoms from the public-utility list and the 13th RFINL allows up to 50%/100% — the issuers' articles evidently have not moved (I).
- 100%-limit companies include Jollibee (JFC), Century Pacific Food (CNPF), Monde Nissin (MONDE), OceanaGold Philippines (OGP), Philippine Seven (SEVN), D&L Industries (DNL), Wilcon Depot (WLCON), Shell Pilipinas (SHLPH), IMI, SSI Group, Del Monte Pacific (DELM) and two **Philippine Deposit Receipt** lines: GMA Holdings PDR (GMAP) and ABS-CBN Holdings PDR (ABSP).
- 0%-limit companies: GMA Network (GMA7), ABS-CBN (ABS), Manila Broadcasting (MBC), Prime Media (PRIM), Manila Bulletin Publishing (MB), Lepanto Consolidated Mining (LC), Benguet (BC), Oriental Petroleum & Minerals (OPM), Manila Mining (MA), Concrete Aggregates (CA), ATN Holdings (ATN), F&J Prince (FJP), Panasonic Manufacturing Philippines (PMPC), Filsyn (FYN), Metro Alliance (MAH). Foreign access to the broadcasters is therefore only through their PDR lines (GMAP, ABSP: 100% limit on the PDR; 0% on the underlying common), consistent with the Constitution's mass-media rule. The PSE FOL-spec sample row ("XYZ Land Inc.", 40%) is fictitious and only illustrates the format. [^pse-fol-spec-v1-1:2] — P/I
- Funds: the one equity ETF page found by a name search (ATR FAMI Philippine Equity ETF, FMETF) and all eight listed REITs found by name (AREIT, DDMPR, FILRT, RCR, MREIT, CREIT, VREIT, PREIT) show a 40% limit — so ETF/REIT access does not bypass FOL. [^pse-edge-stock-data] — P
- Limits are per company, not per investor: they cap the aggregate of all foreign holders. EDGE's page does not show the current foreign-ownership level (the issuer-filed foreign ownership data and the live "foreign shares available" counter do); suspended names (e.g. Villar Land, AllHome) still display a limit.

### Inferences
- When a security's foreign shares available reach zero the exchange engine will reject foreign-flagged buy orders; foreign sells and local trades continue (not stated in the sources read; inferred from the SEC recital, the [f] message and the order flag). — I
- Foreign-to-foreign transfers do not change the foreign holding total, so crossing between two foreign accounts should remain possible at the limit, but no rule text confirms this. — I
- With A/B lines collapsing into one line, previous A/B price differentials should converge; the status of companies' articles after the 9 Aug 2026 deadline is unchecked.

### Gaps
- Current foreign-ownership levels per company (EDGE shows only the limit; the monthly FOL file/issuer filings and the live shares-available counter are not public in what I retrieved — the EDGE disclosure search returned no "Foreign Ownership" template for PLDT, only a Public Ownership Report); engine behaviour at the limit on the new trading engine; any foreign-foreign crossing rule; status of A/B declassification after 9 Aug 2026; publication/effectivity date of EO 113; SEC nationality-test guidelines (control test/grandfather rule); sector laws for banks, insurance, lending companies (EDGE shows 40% for listed banks, but the legal basis was not retrieved).

### Execution implications
- Subscribe to the [f] message (or its successor) and gate every foreign-account buy on `foreign_shares_available ≥ order size`; treat zero as "no foreign bid"; for constrained names expect only local liquidity on the bid and potentially wider spreads/impact for foreign flow — I.
- Keep account codes cleanly flagged: any foreign component in an aggregated order forces the foreign bundle; avoid mixing to keep unbundling deadlines simple.
- Pre-trade guard against FOL-breaching executions: a breach forces same-day (or next-open) disposal at market with proceeds returned — an uncapped execution-risk event.
- Watch the Class A/B collapse: lines that traded at a premium/discount may re-rate; check each name's articles before relying on historic spreads.
- Universe handling: with 40% limits on ~94% of market cap, "foreign room" (limit minus current foreign holdings) rather than the statutory limit is the binding quantity; maintain a per-security table {limit from EDGE Stock Data, live shares available from the feed}, treat 0%-limit names as untradable for foreign accounts (use the PDR line where one exists: GMAP, ABSP) and 100%-limit names as unconstrained.
- FTSE excludes/underweights names with insufficient foreign headroom (rule 6.2); expect index-driven foreign demand to stop at the limit and re-start when headroom recovers — a flow regime that an execution algorithm can anticipate (I).

---

## 4. Operational access for foreign investors (KYC, custody, BSP registration, FX, omnibus accounts, MSCI/FTSE status)

### Takeaway
Account opening is through a PSE trading participant (TP) that performs KYC; custody sits in PDTC with segregated foreign accounts. For repatriation through the banking system, a non-resident should register the investment — for PSE-listed equity, ETFs and REITs this is now done by a **registering authorized agent bank (AAB)** reporting to the BSP, and the BSP states a BSRD is **no longer issued** for these categories (BSP FX Manual, as updated May 2025). Registered investments get full and immediate repatriation using banking-system FX; FX must be linked to eligible securities flows (no overdrafts; no offshore PHP market per MSCI). MSCI's June 2026 review leaves the Philippines' 18 accessibility ratings unchanged from 2025 (weak spots: FOL level, foreign room, FX liberalization, stock lending, short selling); MSCI classifies the Philippines as Emerging; FTSE Russell classifies it as Secondary Emerging (Sept 2025 annual review; confirmed in the March 2026 interim).

### Cited findings
**A. Account opening, custody, omnibus**
- TPs are PSE-accredited traditional or online brokers; after account opening documents "the TP will do its Know Your Customer (KYC) procedure"; online accounts must be pre-funded for buys; settlement T+2. [^pse-investing-at-pse] — P
- MSCI rates the Philippines "++" (no issues) on investor qualification requirement, investor registration and account set-up, custody, registry/depository and trading; "+" on clearing and settlement ("Overdraft facilities for foreign investors are prohibited"); "-" on foreign-exchange market liberalization, stock lending and short selling. [^msci-accessibility-comparison-2026:5] [^msci-accessibility-review-2026:43] [^msci-accessibility-review-2026:71] — P/S (index-provider assessment). Philippines column identical in the 2025 and 2026 comparison tables (all 18 ratings unchanged). [^msci-accessibility-comparison-2025:5] [^msci-accessibility-comparison-2026:5] — P/I
- Aggregation/omnibus-type handling at the exchange: bundled accounts classified local/foreign and unbundled by T+1 noon (above). [^pse-implementing-guidelines-trading-rules:22] — P. At the depository, foreign client holdings are kept in separate Client-Foreign accounts. [^pdtc-depository-rules-1997:14] — P
- PDTC's Name-on-Central-Depository ("NoCD") facility lets a broker keep client holdings under its omnibus broker account "in a segregated set-up": PDTC creates Account 1 "Omnibus with Client" (NoCD client sub-accounts, each with a unique NoCD ID) and Account 2 "Omnibus without Client" (operational pass-through); for REIT allocations the broker's sales report to the transfer agent must break out free accounts "for each nationality/tax status". [^pdtc-nocd-reit-faq:1] [^pdtc-nocd-reit-faq:2] [^pdtc-nocd-reit-faq:5] [^pdtc-dds-operating-guidelines-2017:6] [^pdtc-dds-operating-guidelines-2017:8] — P. MSCI names omnibus-structure deficiencies for many other markets but, for the Philippines, only the overdraft prohibition. [^msci-accessibility-review-2026:43] — I (absence of a complaint; not an explicit endorsement of omnibus practice).
- Global-custodian market guides for the Philippines were **not retrieved** (search budget). MSCI's custody rating "++" is the only independent indication. — gap

**B. BSP registration and FX (Manual of Regulations on Foreign Exchange Transactions, "FX Manual", updated May 2025, amended through Circular 1212 of 11 Apr 2025)**
- Inward investments by non-residents "need not be registered with the BSP unless the repatriation of capital and/or the remittance of related earnings in pesos thereon shall be funded with FX resources of AABs/AAB forex corps"; a BSRD evidences registration, "except those covered by Section 37 for which a BSRD shall no longer be issued". [^bsp-fx-manual-morfxt-2025-05:42] — P
- Classification: equity securities listed at an onshore exchange (PSE), ETFs, investment funds, PDRs are FDI or portfolio investment depending on control (>50% voting = control; ≥10% = significant influence). [^bsp-fx-manual-morfxt-2025-05:42] [^bsp-fx-manual-morfxt-2025-05:43] — P
- Sec. 37 (registration through AABs): equity securities issued onshore by residents and listed at an onshore exchange (e.g. PSE), ETFs, listed PDRs, listed debt, peso time deposits of at least 90 days, etc. are "registered upon reporting thereof by the registering AAB to the BSP"; the registering AAB is an FCDU bank designated by the investor; the investor gives an "Authority to Disclose Information" (Appendix 10.4); FX remitted to fund these investments "must be converted to pesos with AABs/AAB forex corps except if investment is required to be funded by FX". [^bsp-fx-manual-morfxt-2025-05:46] — P
- Sec. 36 (direct BSP registration, free of charge via BSP online system, within one year of the applicable reckoning date) covers unlisted equity, investment funds created onshore, and similar. [^bsp-fx-manual-morfxt-2025-05:44] [^bsp-fx-manual-morfxt-2025-05:45] — P
- Sec. 38: BSP-registered investments are "entitled to full and immediate repatriation of capital and remittance of related earnings" using AAB FX, on an Application to Purchase FX (Annex A) with Appendix 1.4 documents; FX sold is remitted directly to the investor's onshore/offshore account on the date of FX sale; Sec. 41: peso divestment proceeds may sit temporarily in the investor's peso account with any AAB; Sec. 42: reinvestment allowed. [^bsp-fx-manual-morfxt-2025-05:47] [^bsp-fx-manual-morfxt-2025-05:48] [^bsp-fx-manual-morfxt-2025-05:49] — P
- Non-resident peso accounts may be funded only by listed sources (conversion of inward FX; proceeds of BSP-registered investments; services; trade; **cash collateral for securities borrowing and lending**, etc.), and FX can be bought back up to the balance of eligible-source pesos. [^bsp-fx-manual-morfxt-2025-05:19] [^bsp-fx-manual-morfxt-2025-05:20] — P
- FX hedging: customers (including non-residents) may hedge FX exposure with AABs only if the underlying is eligible for servicing with AAB FX; notional may not exceed the underlying exposure; AABs may deal non-deliverable derivatives, and NDFs may be used for a sell-side non-deliverable derivative with a non-resident counterparty. [^bsp-fx-manual-morfxt-2025-05:73] [^bsp-fx-manual-morfxt-2025-05:74] — P
- PSE circulars confirm the registration route for REITs (May 2020) and ETFs (BSP Circular 1030 of 5 Feb 2019, PSE note 8 Jul 2019). [^pse-cn-2020-0052-nonresident-reit-investment:1] [^pse-cn-2019-0037-foreign-investment-etf:1] — P
- MSCI: "There is no offshore currency market and there are constraints on the onshore currency market (e.g., foreign exchange transactions must be linked to security transactions)". [^msci-accessibility-review-2026:43] — P/S
- Not retrieved: BSP appendices (10.A/10.B/1.4) — the forms/annex zip exceeds the 10 MB fetch limit.
- SBL/short selling for foreign funds: the SEC approved (PSE circular of 24 May 2023) **offshore collateral** in SBL transactions "involving at least one foreign party", provided the participants are Qualified Buyers under the 2015 SRC IRR (as amended by SEC MC 6 s.2021 to Rule 10.1.3; a foreign entity that would qualify if Philippine-established is itself a Qualified Buyer; a prime-brokered client must be a Qualified Buyer apprised of the risks). Allowed offshore collateral: cash in GBP and AUD; government/agency debt of OECD members rated at least BBB; constituents of benchmark indices of World Federation of Exchanges member exchanges. [^pse-cn-2023-0027-offshore-collateral-sbl:1] [^pse-cn-2023-0027-offshore-collateral-sbl:2] — P (read via my OCR of the scanned circular). BIR treatment of the MSLA/borrow is in Section 1D; PHP cash collateral held by a non-resident is an eligible source for its peso account (above). The PSE Short Selling Program began in Nov 2023 but "is not yet an established market practice" (MSCI). [^msci-accessibility-review-2026:43] — P/S
- PSE's revised MSLA clearance guidelines (SEC-approved, 2026 edition) keep the BIR registration deadlines of RR 1-2008 Sec. 8(c) (two weeks if executed in the Philippines; one month if executed abroad) and refer to GMSLA/multilateral MSLA structures. [^pse-msla-clearance-guidelines-2026:2] — P

**C. Index-provider status**
- MSCI 2026 Global Market Accessibility Review (June 2026): Philippines in the Emerging Markets (Asia Pacific) group; ratings as above. [^msci-accessibility-review-2026:43] [^msci-accessibility-comparison-2026:5] — P. MSCI EM factsheet (Sept 2026) lists the Philippines among constituent countries. [^msci-em-index-factsheet-2026-09:1] — P
- FTSE Russell: the September 2025 annual review (published 7 Oct 2025) lists the Philippines under **Secondary Emerging** (columns Developed / Advanced Emerging / Secondary Emerging / Frontier); the March 2026 interim (published 7 Apr 2026) keeps it there; the watch list then contained Egypt and Nigeria, not the Philippines. [^ftse-country-classification-annual-2025-09:1] [^ftse-country-classification-annual-2025-09:5] [^ftse-country-classification-interim-2026-03:1] [^ftse-country-classification-interim-2026-03:2] [^ftse-country-classification-interim-2026-03:6] — P. The FTSE September 2026 annual announcement had not yet appeared in the archive (last year's came out 7 Oct 2025). — gap
- FTSE "Quality of Markets" criteria, Asia Pacific, as at March 2026 (Philippines column, read from the rendered table; the legend says boxed cells mark a rating change from September 2025): Pass on regulatory authorities, capital/income repatriation, foreign-investor registration, brokerage competition, tax comparability (domestic vs non-domestic), off-exchange transactions, efficient trading mechanism, transparency, failed-trade settlement costs, CSD, CCP, custody competition; **Restricted** on minority-shareholder treatment, **foreign ownership restrictions**, stock lending, short sales, free-delivery settlement, and account structure at custodian level (securities and cash); **Not Met** on **transaction costs** (implicit and explicit), **developed FX market** (cell appears boxed, i.e. possibly changed since Sept 2025; prior rating not checked) and developed derivatives market; DvP settlement cycle T+2. Lower-middle income, investment-grade credit. [^ftse-quality-of-markets-asia-pacific-2026-03:1] — P (FTSE's own assessment; the "Not Met" on transaction costs was recorded after the 0.1% STT took effect).
- FTSE index construction adjusts constituents for foreign ownership limits: the Global Equity Index Series ground rules (v14.4, Sept 2026) apply an investability weighting for free float and FOLs and define "foreign headroom" = (FOL − foreign holdings)/FOL (e.g. FOL 49%, foreign 39% → 20.41%), with a minimum-foreign-headroom requirement set out in a linked document (title indicates 5%; the document itself was not retrieved). [^ftse-geis-ground-rules-2026-09:13] — P

**D. Market-participation context**
- Foreign transactions were 45.0% of PSE turnover in Aug 2026 and 48.3% year-to-date (46.9% in the same period of 2025); net foreign selling PHP 20.86bn YTD vs PHP 45.43bn a year earlier; ADV PHP 7.53bn (Aug 2026). [^pse-monthly-report-2026-08:2] — P
- Foreign accounts are 0.9% of online stock-market accounts surveyed in 2025 (32,709 of 3.64m). [^pse-investor-profile-2025:2] — P
- Ownership (OECD, end-2023, pre-CMEPA): domestic investors own 62% of Philippine listed equity; foreign investors about 10% — the lowest in ASEAN (13%–26%) and below Asia (18%) and the world (20%); institutional investors are 6% of the total, foreign corporations 3%. In 49% of listed companies the largest shareholder holds more than half the equity. [^oecd-capital-market-review-philippines-2024:122] [^oecd-capital-market-review-philippines-2024:121] — P/S. Together with the 45–48% foreign share of turnover above, foreign participation is a flow-heavy, stock-light presence (I).

### Inferences
- Practical onboarding sequence: (1) appoint a PDTC-participant broker/global custodian; (2) designate an FCDU "registering AAB" and sign the Authority to Disclose Information; (3) convert FX to PHP through AABs before trading (no overdraft) and let the AAB report the investment; (4) at exit, buy back FX the same day against the Annex A application. Under the May 2025 manual the BSRD concept survives mainly for unlisted/direct registrations. — I
- Hedging PHP exposure of registered listed holdings through AAB-intermediated deliverable or non-deliverable derivatives is permitted; unregistered exposures cannot be hedged on the same basis. — I

### Gaps
- Global-custodian profiles/omnibus-account practice at institutional level; detailed KYC/TIN documentation for non-resident institutions; BSP appendix text (10.A/10.B/1.4, Annex A); FTSE September 2026 annual decision (due about early October); MSCI 2026 Annual Market Classification Review text for the Philippines (only the accessibility review was read); the FTSE "foreign headroom" threshold document.

### Execution implications
- Funding/settlement: pre-fund PHP, T+2, no overdraft; sequence FX conversion early in the day; single registering AAB simplifies repatriation reporting.
- FX hedge sizing must stay at or below the registered exposure; NDF with non-resident dealers is the fallback.
- Ownership reporting: 5% crossing triggers SEC Form 18-A within five business days.
- Short selling/SBL exist (since Nov 2023) but MSCI and FTSE rate stock lending and short selling "-"/"Restricted": expect thin borrow; SBL needs a BIR-registered MSLA before the first loan or the transfer is a taxable deemed sale; foreign funds can post offshore collateral (GBP/AUD cash, OECD BBB+ government debt, WFE-index equities) only if they are Qualified Buyers.
- Cost headroom: FTSE still marks Philippine transaction costs "Not Met" and the OECD found trading costs about twice the peer average before CMEPA; the 50 bp STT cut narrows but does not remove the gap, so further STT/fee reforms remain a live policy variable to monitor (I).

### Timeline of rule changes relevant to explicit costs and access (what replaced what)

| Date | Change | Replaced | Source |
|---|---|---|---|
| 14 Mar 1973 / 14 Dec 1977 | PD 154: commission cap 1% (min PHP 20); SEC raises cap to 1.5% | none | [^pse-cn-2024-0029-min-commission-removal:2] |
| 1 Jan 1998 | NIRC (RA 8424): STT 0.5%; IPO tax 4/2/1% | earlier regime | [^ra-8424-nirc-1997:165] [^ra-8424-nirc-1997:270] |
| 6 Oct 2008 | PSE Memo 2008-0467: graded minimum commission schedule 0.25% (to PHP 100m) down to 0.05% (above PHP 10bn) | earlier schedule (as amended 2006) | [^pse-memo-2008-0467-minimum-commission-rates:2] |
| 1 Jan 2018 | TRAIN: STT 0.6%; DST issue PHP 2/200, transfer PHP 1.50/200 | STT 0.5% | [^ra-10963-train:24] [^ra-10963-train:54] |
| 1 Jul 2020 / 1 Jan 2021 | CREATE (approved 26 Mar 2021): dividend-credit condition becomes "regular rate minus 15%" from 1 Jul 2020; NRFC regular rate 25% "effective January 1, 2021" | 30% NRFC rate; 15%-with-15-point-credit condition | [^ra-11534-create:11] [^ra-11534-create:12] [^ra-12214-cmepa:9] |
| Sep 2020 (approved 11 Sep; effective on publication) | Bayanihan II repeals IPO tax (Sec. 127(B)) | 4/2/1% IPO tax | [^ra-11494-bayanihan-ii:20] |
| 2 Mar 2022 | RA 11647: min paid-in capital US$200k / US$100k for domestic-market enterprises; List B changes at most every 2 years | higher thresholds | [^ra-11647-foreign-investments-act-amendments:6] |
| 21 Mar 2022 | RA 11659: "public utility" narrowed to six categories; reciprocity clause for critical infrastructure | broad public-utility definition | [^ra-11659-public-service-act-amendments:4] [^ra-11659-public-service-act-amendments:13] |
| 24 May 2023 | SEC approves offshore collateral for SBL with a foreign party (Qualified Buyers) | onshore-only collateral | [^pse-cn-2023-0027-offshore-collateral-sbl:1] |
| 24 Aug 2023 | T+2 settlement cycle go-live | T+3 | [^sccp-memo-04-0823-t2-go-live:1] |
| 11 Apr 2024 | BSP Circular 1192 amends FX Manual (AAB-based registration for listed securities; no BSRD for Sec. 37 categories - as reflected in the May 2025 manual) | BSRD-based registration | [^bsp-fx-manual-morfxt-2025-05:46] |
| 18 Apr 2024 | SEC MC 7-2024 removes minimum commission (1.5% cap stays) | PSE 0.25%-0.05% minimum schedule; PHP 20 floor | [^pse-cn-2024-0029-min-commission-removal:1] |
| 11 Apr 2025 | BSP Circular 1212 (latest amendment cited in the FX Manual; FX derivatives and registration provisions) | earlier text | [^bsp-fx-manual-morfxt-2025-05:45] |
| 1 Jul 2025 | CMEPA: STT 0.1% (local and foreign-listed shares; "other securities"); DST on issue 0.75%; Sec. 199(e) widened; unlisted-share CGT 15% extended to foreign-corporation shares | STT 0.6%; DST 1% | [^ra-12214-cmepa:16] [^ra-12214-cmepa:17] [^ra-12214-cmepa:20] |
| 9 Aug 2025 (deadline 9 Aug 2026) | SEC MC 10-2025 effective: Class A/B declassification; FOL-breach unwind rule | A/B dual lines | [^pse-cn-2025-0036-declassification-effectivity:1] [^pse-cn-2025-0035-sec-declassification-mandate:3] |
| 4 Sep 2025 | Brokers begin passing 12% VAT on the PSE transaction fee to clients (secondary-sourced; the PSE's own illustration already showed VAT-inclusive 0.56 in 2024) | broker pages showing PSE fee without VAT | [^firstmetrosec-fees-and-charges] [^oecd-capital-market-review-philippines-2024:45] |
| 13 Apr 2026 | EO 113: 13th RFINL | 12th (EO 175) | [^eo-113-2026-13th-finl:1] |
| Jun 2026 | MSCI 2026 accessibility review (Philippines ratings unchanged) | 2025 review | [^msci-accessibility-comparison-2026:5] |
| 23 Nov 2026 (scheduled) | New trading engine go-live (one lot one share; negotiated trade; new back-office portal) | legacy engine/rules | [^pse-nte-broker-forum-2026-07-09:9] |

(CREATE was approved 26 Mar 2021 [^ra-11534-create:77]; its dividend-credit proviso is dated "effective July 1, 2020" in the text, and the 25% NRFC rate is dated "effective January 1, 2021" in the Sec. 28(B)(1) text reproduced in CMEPA. The BSP Circular rows rely on the amendment footnotes of the May 2025 manual; the pre-2024 BSRD practice is inferred from the manual's footnote 62, not from the earlier circular text, which was not retrieved. "T+3" before Aug 2023 is from my background knowledge, not from a retrieved source.)

---

### Consolidated open gaps and source conflicts (for the report writer)

Open gaps (absence of public information is itself a finding where noted):
1. Post-April-2024 institutional/global-broker commission rates: no public source (negotiated; the pre-2024 floor was 0.25% up to PHP 100m, so sub-25 bp deals are plausible but undocumented).
2. Primary basis for the 0.005% SEC "SRC fee" rate, the SIPF contribution rate (0.001% appears only on one broker page for block sales), and the notice behind VAT on the PSE fee.
3. BIR positions not found: treaty-relief procedure for dividends/capital gains; whether treaty capital-gains articles can displace STT; STT on ETFs; selling-shareholder tranche of an IPO since the IPO-tax repeal; post-CMEPA SBL guidance; reconciliation of the manufactured-dividend rule (RR 10-2006/1-2008 vs the PSE FAQ).
4. Foreign ownership: current foreign-ownership levels/headroom per stock (EDGE shows limits only); behaviour of the engine at the limit and any foreign-to-foreign crossing rule; whether the new trading engine feed (go-live scheduled 23 Nov 2026) keeps the foreign-shares-available field; status of Class A/B declassification after the 9 Aug 2026 deadline; EO 113 publication/effectivity date; SEC nationality-test guidelines; sector statutes behind the 40% limit on banks.
5. Operational: global-custodian market guides and institutional omnibus practice; KYC/TIN documentation for non-resident institutions; BSP appendices 10.A/10.B/1.4 and Annex A; FTSE September 2026 annual announcement (expected about early October); MSCI 2026 annual market classification review text for the Philippines; FTSE minimum-foreign-headroom document.
6. Tooling: the shared web-search budget was exhausted mid-session, so items 3-5 were probed only through direct fetches of known URLs, the archived KB and the PSE EDGE portal; "not found" there does not prove non-existence.

Source conflicts and staleness flagged in the notes:
- PSE "Investing at PSE" page: current on STT (0.1%), PSE-fee VAT and SRC fee, but its withholding-tax table is pre-CREATE (30% for non-resident corporations); the statute (RA 11534 / RR 21-2025) governs.
- Broker pages: COL (modified 10 Jul 2025) omits VAT on the PSE fee; several omit the SRC fee that the PSE and the OECD list.
- RA 12214 effectivity wording: lawphil HTML ("15 days after publication") vs signed PDF and BIR ("1 July 2025") — PDF governs.
- OECD 2024 review calls the removed commission floor a "1.5% minimum"; 1.5% is the maximum (SEC MC 7-2024 text).
- MSCI says "all industries ... 40 percent" foreign ownership limit; the 13th RFINL is narrower, but EDGE data show 40% on about 94% of market capitalisation (land-ownership rule), so MSCI's description matches practice.

## Source catalog

```yaml
- slug: ra-12214-cmepa
  title: "Republic Act No. 12214, Capital Markets Efficiency Promotion Act (enrolled/signed copy)"
  publisher: "Republic of the Philippines (Congress; copy via Lawphil Project)"
  type: pdf
  canonical_url: "https://lawphil.net/statutes/repacts/ra2025/pdf/ra_12214_2025.pdf"
  local_path: pdfs/ra-12214-cmepa.pdf
  edition: in-force
  amended_through: "2025-05-29"
  note: "Approved 29 May 2025; Sec. 29 effectivity 1 Jul 2025. Lawphil HTML transcription differs on effectivity wording (15 days after publication) - PDF governs."
- slug: ra-12214-lawphil-html
  title: "Republic Act No. 12214 (HTML transcription)"
  publisher: "Lawphil Project (Arellano Law Foundation)"
  type: web
  canonical_url: "https://lawphil.net/statutes/repacts/ra2025/ra_12214_2025.html"
  local_path: null
  edition: in-force
  amended_through: "2025-05-29"
  note: "Used only to flag the effectivity-wording discrepancy; contains OCR/transcription slips (e.g. Sec. 176 \"seventy percent\")."
- slug: bir-rr-20-2025-stt
  title: "BIR Revenue Regulations No. 20-2025 - STT rate adjustment and STT on domestic shares listed abroad"
  publisher: "Bureau of Internal Revenue / Department of Finance"
  type: pdf
  canonical_url: "https://bir-cdn.bir.gov.ph/BIR/pdf/RR%20NO.%2020-2025.pdf"
  local_path: pdfs/bir-rr-20-2025-stt.pdf
  edition: in-force
  amended_through: "2025-08-05"
  note: "Signed by Finance Secretary 29 Jul 2025; BIR records stamp 5 Aug 2025; effective 1 Jul 2025. Scanned image PDF (no text layer)."
- slug: bir-rr-19-2025-dst
  title: "BIR Revenue Regulations No. 19-2025 - DST rate adjustments and exempt documents under CMEPA"
  publisher: "Bureau of Internal Revenue / Department of Finance"
  type: pdf
  canonical_url: "https://bir-cdn.bir.gov.ph/BIR/pdf/RR%20NO.%2019-2025.pdf"
  local_path: pdfs/bir-rr-19-2025-dst.pdf
  edition: in-force
  amended_through: "2025-08-05"
  note: "Scanned image PDF; covers Secs. 174, 176, 179 and 199."
- slug: bir-rr-21-2025-cmepa-income
  title: "BIR Revenue Regulations No. 21-2025 - CMEPA amendments to NIRC Secs. 22, 24, 25, 27, 28, 32, 34, 38, 39, 42"
  publisher: "Bureau of Internal Revenue / Department of Finance"
  type: pdf
  canonical_url: "https://bir-cdn.bir.gov.ph/BIR/pdf/RR%20NO.%2021-2025.pdf"
  local_path: pdfs/bir-rr-21-2025-cmepa-income.pdf
  edition: in-force
  amended_through: "2025-08-05"
  note: "Scanned image PDF; rate tables on pp. 3-8."
- slug: bir-rmc-60-2025-cmepa-circular
  title: "BIR Revenue Memorandum Circular No. 60-2025 circularizing RA 12214 and the veto message"
  publisher: "Bureau of Internal Revenue"
  type: pdf
  canonical_url: "https://bir-cdn.bir.gov.ph/BIR/pdf/RMC%20NO.%2060-2025.pdf"
  local_path: pdfs/bir-rmc-60-2025-cmepa-circular.pdf
  edition: in-force
  amended_through: "2025-06-11"
  note: "One-page cover only; annexes (Act and veto message) not in the archived copy."
- slug: ra-8424-nirc-1997
  title: "Republic Act No. 8424, National Internal Revenue Code of 1997 (as originally enacted)"
  publisher: "Republic of the Philippines (copy via Lawphil Project)"
  type: pdf
  canonical_url: "https://lawphil.net/statutes/repacts/ra1997/pdf/ra_8424_1997.pdf"
  local_path: pdfs/ra-8424-nirc-1997.pdf
  edition: historical
  amended_through: "1997-12-11"
  note: "Used for original Sec. 127 (STT 1/2 of 1%; IPO tax). Not the current consolidated Code."
- slug: ra-10963-train
  title: "Republic Act No. 10963, TRAIN Law"
  publisher: "Republic of the Philippines (copy via Lawphil Project)"
  type: pdf
  canonical_url: "https://lawphil.net/statutes/repacts/ra2017/pdf/ra_10963_2017.pdf"
  local_path: pdfs/ra-10963-train.pdf
  edition: superseded
  amended_through: "2017-12-19"
  note: "STT 6/10 of 1% (superseded by CMEPA for Sec. 127); DST Secs. 174-175 (Sec. 175 still current). Scanned image PDF, 29 MB."
- slug: ra-10963-train-html
  title: "Republic Act No. 10963 (HTML)"
  publisher: "Lawphil Project"
  type: web
  canonical_url: "https://lawphil.net/statutes/repacts/ra2017/ra_10963_2017.html"
  local_path: null
  edition: superseded
  amended_through: "2017-12-19"
  note: "Used for the 15% unlisted-share capital gains tax text (Sec. 24(C)/27(D)(2)); page not located in the scanned PDF."
- slug: ra-11494-bayanihan-ii
  title: "Republic Act No. 11494, Bayanihan to Recover as One Act (Sec. 6 repeals IPO tax)"
  publisher: "Republic of the Philippines (copy via Lawphil Project)"
  type: pdf
  canonical_url: "https://lawphil.net/statutes/repacts/ra2020/pdf/ra_11494_2020.pdf"
  local_path: pdfs/ra-11494-bayanihan-ii.pdf
  edition: in-force
  amended_through: "2020-09-11"
  note: "Scanned image PDF; Sec. 6 on p. 20."
- slug: ra-11534-create
  title: "Republic Act No. 11534, CREATE Act (NRFC dividend and capital-gains provisions)"
  publisher: "Republic of the Philippines (copy via Lawphil Project)"
  type: pdf
  canonical_url: "https://lawphil.net/statutes/repacts/ra2021/pdf/ra_11534_2021.pdf"
  local_path: pdfs/ra-11534-create.pdf
  edition: in-force
  amended_through: "2021-03-26"
  note: "Sec. 28(B)(5)(b) on pp. 11-12."
- slug: ra-9856-reit-act
  title: "Republic Act No. 9856, Real Estate Investment Trust Act of 2009"
  publisher: "Republic of the Philippines (copy via Lawphil Project)"
  type: pdf
  canonical_url: "https://lawphil.net/statutes/repacts/ra2009/pdf/ra_9856_2009.pdf"
  local_path: pdfs/ra-9856-reit-act.pdf
  edition: in-force
  amended_through: "2009-12-17"
  note: "Secs. 6, 13, 14 (nationality, STT/DST/IPO treatment, 10% dividend tax). Scanned image PDF. Final page shows a 17 Dec 2009 date stamp and what appears to be a lapsed-into-law notice (no presidential signature) - read from the page image."
- slug: ra-8799-src
  title: "Republic Act No. 8799, Securities Regulation Code"
  publisher: "Republic of the Philippines (copy archived by another researcher)"
  type: pdf
  canonical_url: "https://lawphil.net/statutes/repacts/ra2000/pdf/ra_8799_2000.pdf"
  local_path: pdfs/ra-8799-src.pdf
  edition: in-force
  amended_through: "undated"
  note: "Enacted 2000; Sec. 35 on p. 36. Canonical URL assumed from the lawphil pattern - not verified for this copy."
- slug: sec-2015-src-irr
  title: "2015 Implementing Rules and Regulations of the Securities Regulation Code"
  publisher: "Securities and Exchange Commission"
  type: pdf
  canonical_url: "n/a (archived by another researcher; source URL not recorded here)"
  local_path: pdfs/sec-2015-src-irr.pdf
  edition: in-force
  amended_through: "undated"
  note: "Used for Rule 18.1 (5% beneficial ownership report, p. 42), Rule 35 (p. 113), Rule 36.5 (p. 120)."
- slug: bir-rr-10-2006-sbl
  title: "BIR Revenue Regulations No. 10-2006 - tax treatment of securities borrowing and lending"
  publisher: "Bureau of Internal Revenue"
  type: pdf
  canonical_url: "n/a (archived by another researcher; source URL not recorded here)"
  local_path: pdfs/bir-rr-10-2006-sbl.pdf
  edition: superseded
  amended_through: "2006-06-23"
  note: "Amended by RR 1-2008 (Secs. 2-6, 9, 12(a)); pp. 4, 7-10 used."
- slug: bir-rr-1-2008-sbl
  title: "BIR Revenue Regulations No. 1-2008 amending RR 10-2006 (SBL)"
  publisher: "Bureau of Internal Revenue"
  type: pdf
  canonical_url: "https://bir-cdn.bir.gov.ph/BIR/pdf/RR%20No.%201-2008.pdf"
  local_path: pdfs/bir-rr-1-2008-sbl.pdf
  edition: in-force
  amended_through: "2008-02-01"
  note: "Archived independently by another researcher and by me (byte-identical; my duplicate deleted). Secs. 5 and 6(a) on pp. 4-5."
- slug: eo-113-2026-13th-finl
  title: "Executive Order No. 113 - Thirteenth (13th) Regular Foreign Investment Negative List"
  publisher: "Office of the President (copy via Lawphil Project)"
  type: pdf
  canonical_url: "https://lawphil.net/executive/execord/eo2026/pdf/eo_113_2026.pdf"
  local_path: pdfs/eo-113-2026-13th-finl.pdf
  edition: in-force
  amended_through: "2026-04-13"
  note: "Scanned image PDF (7 pp.); effective 15 days after publication (publication date not verified). OCR by me for page mapping."
- slug: eo-175-2022-12th-finl
  title: "Executive Order No. 175 - Twelfth Regular Foreign Investment Negative List"
  publisher: "Office of the President (copy via Lawphil Project)"
  type: pdf
  canonical_url: "https://lawphil.net/executive/execord/eo2022/pdf/eo_175_2022.pdf"
  local_path: pdfs/eo-175-2022-12th-finl.pdf
  edition: superseded
  amended_through: "2022-06-27"
  note: "Replaced by EO 113 (2026)."
- slug: ra-11659-public-service-act-amendments
  title: "Republic Act No. 11659, amending the Public Service Act"
  publisher: "Republic of the Philippines (copy via Lawphil Project)"
  type: pdf
  canonical_url: "https://lawphil.net/statutes/repacts/ra2022/pdf/ra_11659_2022.pdf"
  local_path: pdfs/ra-11659-public-service-act-amendments.pdf
  edition: in-force
  amended_through: "2022-03-21"
  note: "Scanned image PDF (15 pp.)."
- slug: ra-11647-foreign-investments-act-amendments
  title: "Republic Act No. 11647, amending the Foreign Investments Act of 1991"
  publisher: "Republic of the Philippines (copy via Lawphil Project)"
  type: pdf
  canonical_url: "https://lawphil.net/statutes/repacts/ra2022/pdf/ra_11647_2022.pdf"
  local_path: pdfs/ra-11647-foreign-investments-act-amendments.pdf
  edition: in-force
  amended_through: "2022-03-02"
  note: "Scanned image PDF (8 pp.)."
- slug: constitution-1987-lawphil
  title: "1987 Constitution of the Republic of the Philippines"
  publisher: "Lawphil Project"
  type: web
  canonical_url: "https://lawphil.net/consti/cons1987.html"
  local_path: null
  edition: in-force
  amended_through: "undated"
  note: "Art. XII Secs. 2, 7, 10, 11; Art. XIV Sec. 4(2); Art. XVI Sec. 11. Not archived (HTML only)."
- slug: gamboa-v-teves-2012-lawphil
  title: "Gamboa v. Teves, G.R. No. 176579, Resolution of 9 October 2012 (and Decision of 28 June 2011)"
  publisher: "Supreme Court of the Philippines (via Lawphil)"
  type: web
  canonical_url: "https://lawphil.net/judjuris/juri2012/oct2012/gr_176579_2012.html"
  local_path: null
  edition: in-force
  amended_through: "2012-10-09"
  note: "Defines \"capital\" in Art. XII Sec. 11; 2011 Decision at https://lawphil.net/judjuris/juri2011/jun2011/gr_176579_2011.html."
- slug: bsp-fx-manual-morfxt-2025-05
  title: "Manual of Regulations on Foreign Exchange Transactions (FX Manual / MORFXT)"
  publisher: "Bangko Sentral ng Pilipinas"
  type: pdf
  canonical_url: "https://www.bsp.gov.ph/Regulations/MORFXT/MORFXT.pdf"
  local_path: pdfs/bsp-fx-manual-morfxt-2025-05.pdf
  edition: in-force
  amended_through: "2025-04-11"
  note: "Cover says \"Updated as of May 2025\"; latest amending circular cited in text is No. 1212 of 11 Apr 2025. Appendices/annexes are in a separate zip not retrieved."
- slug: msci-accessibility-review-2026
  title: "MSCI 2026 Global Market Accessibility Review (report)"
  publisher: "MSCI Inc."
  type: pdf
  canonical_url: "https://www.msci.com/downloads/web/msci-com/indexes/index-resources/market-classification/MSCI%202026%20GLOBAL%20MARKET%20ACCESSIBILITY%20REVIEW%20REPORT.pdf"
  local_path: pdfs/msci-accessibility-review-2026.pdf
  edition: in-force
  amended_through: "2026-06-18"
  note: "Cover says June 2026; date is the MSCI press-release date. Philippines text p. 43; table p. 71."
- slug: msci-accessibility-comparison-2026
  title: "MSCI 2026 Global Market Accessibility Review - country comparison"
  publisher: "MSCI Inc."
  type: pdf
  canonical_url: "https://www.msci.com/downloads/web/msci-com/indexes/index-resources/market-classification/MSCI%202026%20GLOBAL%20MARKET%20ACCESSIBILITY%20COUNTRY%20COMPARISON%20REPORT.pdf"
  local_path: pdfs/msci-accessibility-comparison-2026.pdf
  edition: in-force
  amended_through: "2026-06-18"
  note: "Emerging-markets table p. 5; Philippines column read visually against the rendered page."
- slug: msci-accessibility-comparison-2025
  title: "MSCI 2025 Global Market Accessibility Review - country comparison"
  publisher: "MSCI Inc."
  type: pdf
  canonical_url: "https://www.msci.com/downloads/web/msci-com/indexes/index-resources/market-classification/MSCI%202025%20GLOBAL%20MARKET%20ACCESSIBILITY%20COUNTRY%20COMPARISON%20REPORT.pdf"
  local_path: pdfs/msci-accessibility-comparison-2025.pdf
  edition: superseded
  amended_through: "undated"
  note: "Cover says June 2025; used only for the year-on-year comparison."
- slug: msci-em-index-factsheet-2026-09
  title: "MSCI Emerging Markets Index factsheet (Sept 2026)"
  publisher: "MSCI Inc."
  type: pdf
  canonical_url: "n/a (archived by another researcher; source URL not recorded here)"
  local_path: pdfs/msci-em-index-factsheet-2026-09.pdf
  edition: in-force
  amended_through: "undated"
  note: "Lists the Philippines among EM country constituents (p. 1)."
- slug: ftse-country-classification-annual-2025-09
  title: "FTSE Equity Country Classification - September 2025 annual announcement"
  publisher: "FTSE Russell (LSEG)"
  type: pdf
  canonical_url: "n/a (archived by another researcher; source URL not recorded here)"
  local_path: pdfs/ftse-country-classification-annual-2025-09.pdf
  edition: in-force
  amended_through: "2025-10-07"
  note: "Philippines = Secondary Emerging (p. 5)."
- slug: ftse-country-classification-interim-2026-03
  title: "FTSE Equity Country Classification - March 2026 interim announcement"
  publisher: "FTSE Russell (LSEG)"
  type: pdf
  canonical_url: "n/a (archived by another researcher; source URL not recorded here)"
  local_path: pdfs/ftse-country-classification-interim-2026-03.pdf
  edition: in-force
  amended_through: "2026-04-07"
  note: "Philippines unchanged (p. 6); watch list = Egypt, Nigeria (p. 2)."
- slug: ftse-quality-of-markets-asia-pacific-2026-03
  title: "FTSE Quality of Markets - Asia Pacific (March 2026)"
  publisher: "FTSE Russell (LSEG)"
  type: pdf
  canonical_url: "n/a (archived by another researcher; source URL not recorded here)"
  local_path: pdfs/ftse-quality-of-markets-asia-pacific-2026-03.pdf
  edition: in-force
  amended_through: "undated"
  note: "One-page criteria table; Philippines column read from the rendered image (Secondary Emerging group); boxed cells mark changes since Sept 2025."
- slug: pse-cn-2024-0029-min-commission-removal
  title: "PSE Circular CN-2024-0029 - Removal of Minimum Commission Charges (attaches SEC MC 7-2024)"
  publisher: "Philippine Stock Exchange / SEC"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2024-0029.pdf"
  local_path: pdfs/pse-cn-2024-0029-min-commission-removal.pdf
  edition: in-force
  amended_through: "2024-05-17"
  note: "SEC MC 7-2024 dated 16 Apr 2024 at pp. 2-3."
- slug: pse-memo-2008-0467-minimum-commission-rates
  title: "PSE Memo for Brokers No. 2008-0467 - Minimum Commission Rates & Policy on Commissions in a Tender Offer (Annex A schedule)"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2021/04/Minimum-Commission-Rates-and-Policy-on-Commisions-in-a-Tender-Offer.pdf"
  local_path: pdfs/pse-memo-2008-0467-minimum-commission-rates.pdf
  edition: superseded
  amended_through: "2008-10-06"
  note: "Scanned image PDF (3 pp.; no text layer). Effective 6 Oct 2008; repealed from 18 Apr 2024 by SEC MC 7-2024. Annex A on p. 2, penalties/tender-offer policy on pp. 2-3."
- slug: pse-cn-2025-0032-bir-stt-advisory
  title: "PSE Circular CN-2025-0032 - BIR tax advisory on manual payment of revised STT"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2025-0032.pdf"
  local_path: pdfs/pse-cn-2025-0032-bir-stt-advisory.pdf
  edition: in-force
  amended_through: "2025-07-15"
  note: "Page 1 = PSE circular; page 2 = BIR Tax Advisory of 4 Jul 2025 (low-resolution image, read visually; ATC PT 203 for foreign-exchange STT)."
- slug: pse-cn-2025-0035-sec-declassification-mandate
  title: "PSE Circular CN-2025-0035 - SEC MC 10 s.2025 mandating declassification of Class A/B shares"
  publisher: "Philippine Stock Exchange / SEC"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2025-0035.pdf"
  local_path: pdfs/pse-cn-2025-0035-sec-declassification-mandate.pdf
  edition: in-force
  amended_through: "2025-08-11"
  note: "Archived by another researcher; SEC text at pp. 2-3."
- slug: pse-cn-2025-0036-declassification-effectivity
  title: "PSE Circular CN-2025-0036 - Effectivity of SEC MC 10 s.2025"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2025-0036.pdf"
  local_path: pdfs/pse-cn-2025-0036-declassification-effectivity.pdf
  edition: in-force
  amended_through: "2025-08-15"
  note: "Effective 9 Aug 2025; articles to be amended by 9 Aug 2026."
- slug: pse-cn-2025-0046-board-lot-trading-at-last
  title: "PSE Circular CN-2025-0046 - proposed board lot and trading-at-last amendments"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "n/a (archived by another researcher; source URL not recorded here)"
  local_path: pdfs/pse-cn-2025-0046-board-lot-trading-at-last.pdf
  edition: n/a
  amended_through: "2025-12-15"
  note: "Consultation draft only; minimum order value proposal at p. 3."
- slug: pse-cn-2020-0052-nonresident-reit-investment
  title: "PSE Circular - Non-resident investment into Philippine REITs"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "n/a (archived by another researcher; source URL not recorded here)"
  local_path: pdfs/pse-cn-2020-0052-nonresident-reit-investment.pdf
  edition: in-force
  amended_through: "2020-05-26"
  note: "Cites then-current Sec. 37.2 of the FX Manual."
- slug: pse-cn-2019-0037-foreign-investment-etf
  title: "PSE Circular - Foreign investment into Philippine ETFs (BSP Circular 1030)"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "n/a (archived by another researcher; source URL not recorded here)"
  local_path: pdfs/pse-cn-2019-0037-foreign-investment-etf.pdf
  edition: in-force
  amended_through: "2019-07-08"
  note: "Sec. 33.3.c of the FX Manual covers ETFs."
- slug: pse-implementing-guidelines-trading-rules
  title: "Implementing Guidelines of the PSE Revised Trading Rules"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "n/a (archived by another researcher; source URL not recorded here)"
  local_path: pdfs/pse-implementing-guidelines-trading-rules.pdf
  edition: in-force
  amended_through: "undated"
  note: "Account nationality flag/bundling pp. 21-22; block sales pp. 23-24. Edition predates the 2026 new trading engine changes."
- slug: pse-listing-disclosure-rules
  title: "PSE Consolidated Listing and Disclosure Rules"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "n/a (archived by another researcher; source URL not recorded here)"
  local_path: pdfs/pse-listing-disclosure-rules.pdf
  edition: in-force
  amended_through: "undated"
  note: "Art. VII Sec. 17.13 on p. 157."
- slug: pse-listing-guidance-notes
  title: "PSE listing and disclosure guidance notes (incl. foreign ownership memos 2007)"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "n/a (archived by another researcher; source URL not recorded here)"
  local_path: pdfs/pse-listing-guidance-notes.pdf
  edition: in-force
  amended_through: "undated"
  note: "Memos of 15 Jun 2007 and 8 Nov 2007 at pp. 67-68, 72."
- slug: pse-fol-spec-v1-1
  title: "PSE Foreign Ownership Level (FOL) Report Specifications v1.1"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "n/a (archived by another researcher; source URL not recorded here)"
  local_path: pdfs/pse-fol-spec-v1-1.pdf
  edition: in-force
  amended_through: "undated"
  note: "Version 1.1 dated September 2019."
- slug: pse-itch-equities-feed-spec-v2-3
  title: "PSE Equities Feed Specification for X-stream (ITCH) v2.3"
  publisher: "Philippine Stock Exchange / OMX"
  type: pdf
  canonical_url: "n/a (archived by another researcher; source URL not recorded here)"
  local_path: pdfs/pse-itch-equities-feed-spec-v2-3.pdf
  edition: superseded
  amended_through: "undated"
  note: "Legacy engine feed; [f] Foreign Shares Available message on pp. 19-20, 22, 25. 2026 engine (Nasdaq Eqlipse) spec not checked."
- slug: pdtc-depository-rules-1997
  title: "Rules of the Philippine Central Depository (Nov 1997)"
  publisher: "Philippine Central Depository / PDTC"
  type: pdf
  canonical_url: "n/a (archived by another researcher; source URL not recorded here)"
  local_path: pdfs/pdtc-depository-rules-1997.pdf
  edition: historical
  amended_through: "1997-11-30"
  note: "Date is month-level only (November 1997). Foreign accounts pp. 14-15."
- slug: sccp-clearing-house-rules-2018
  title: "SCCP Clearing House Rules (2018) - Annex 7 schedule of fees"
  publisher: "Securities Clearing Corporation of the Philippines"
  type: pdf
  canonical_url: "n/a (archived by another researcher; source URL not recorded here)"
  local_path: pdfs/sccp-clearing-house-rules-2018.pdf
  edition: in-force
  amended_through: "undated"
  note: "Clearing fee 1 bp VAT-inclusive (p. 62); later SCCP memos may have amended rules."
- slug: sccp-memo-04-0823-t2-go-live
  title: "SCCP Memo for Brokers No. 04-0823 - Go-live of the migration to the T+2 settlement cycle on 24 Aug 2023"
  publisher: "Securities Clearing Corporation of the Philippines"
  type: pdf
  canonical_url: "n/a (archived by another researcher; source URL not recorded here)"
  local_path: pdfs/sccp-memo-04-0823-t2-go-live.pdf
  edition: in-force
  amended_through: "2023-08-11"
  note: "SEC En Banc approval 10 Aug 2023; first T+2 trading day 24 Aug 2023."
- slug: pse-nte-user-group-2026-01-15
  title: "PSE new trading engine - user group (15 Jan 2026)"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "n/a (archived by another researcher; source URL not recorded here)"
  local_path: pdfs/pse-nte-user-group-2026-01-15.pdf
  edition: in-force
  amended_through: "2026-01-15"
  note: "One Lot One Share and TP minimum order value language (pp. 9-10)."
- slug: pse-nte-broker-forum-2026-07-09
  title: "PSE new trading engine - broker forum (9 Jul 2026)"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "n/a (archived by another researcher; source URL not recorded here)"
  local_path: pdfs/pse-nte-broker-forum-2026-07-09.pdf
  edition: in-force
  amended_through: "2026-07-09"
  note: "Negotiated Trade (p. 8); portal modules incl. Weekly Tax Report (p. 13)."
- slug: pse-monthly-report-2026-08
  title: "PSE Monthly Report, August 2026"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "n/a (archived by another researcher; source URL not recorded here)"
  local_path: pdfs/pse-monthly-report-2026-08.pdf
  edition: in-force
  amended_through: "undated"
  note: "Foreign transactions share and net foreign flows (p. 2)."
- slug: pse-investor-profile-2025
  title: "PSE Stock Market Investor Profile 2025"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "n/a (archived by another researcher; source URL not recorded here)"
  local_path: pdfs/pse-investor-profile-2025.pdf
  edition: in-force
  amended_through: "undated"
  note: "Foreign vs local account counts (p. 2)."
- slug: pse-investing-at-pse
  title: "PSE - \"Investing at PSE\" (trading cycle, transaction fees & taxes)"
  publisher: "Philippine Stock Exchange"
  type: web
  canonical_url: "https://www.pse.com.ph/investing-at-pse/"
  local_path: null
  edition: in-force
  amended_through: "undated"
  note: "Retrieved 6 Oct 2026. Shows STT 0.1%, VAT on PSE fee, SRC fee 0.005%, T+2; its withholding-tax table is stale (30% NRFC). Wayback snapshots (to date the page) were rate-limited."
- slug: pse-edge-stock-data
  title: "PSE EDGE - Company \"Stock Data\" pages (Foreign Ownership Limit(%) field)"
  publisher: "Philippine Stock Exchange (EDGE disclosure portal)"
  type: web
  canonical_url: "https://edge.pse.com.ph/companyPage/stockData.do?cmpy_id={id}"
  local_path: null
  edition: in-force
  amended_through: "2026-10-06"
  note: "Pages fetched 6 Oct 2026 (stamped \"As of Oct 06, 2026\"); ids 1-760 scanned, 284 company pages parsed. Examples - id 6 PLDT 40%, id 69 Globe 40%, id 260 BDO 40%, id 86 Jollibee 100%, id 610 GMA Network 0%, id 611 GMA Holdings PDR 100%. Aggregates in the notes are my computation."
- slug: pse-sbl-short-selling-page
  title: "PSE - Securities Borrowing & Lending and Short Selling page (tax FAQ)"
  publisher: "Philippine Stock Exchange"
  type: web
  canonical_url: "https://www.pse.com.ph/sbl-short-selling/"
  local_path: null
  edition: in-force
  amended_through: "undated"
  note: "Retrieved 6 Oct 2026; cites BIR Ruling 168-98, RR 10-2006 as amended by RR 1-2008."
- slug: firstmetrosec-fees-and-charges
  title: "First Metro Securities - Fees and Charges"
  publisher: "First Metro Securities Brokerage Corp."
  type: web
  canonical_url: "https://help.firstmetrosec.com.ph/hc/en-us/articles/55429528585369-Fees-and-Charges"
  local_path: null
  edition: in-force
  amended_through: "2026-03-19"
  note: "Broker page; \"Effective September 4, 2025\" tables; STT 0.1%."
- slug: colfinancial-fees-faq
  title: "COL Financial - fees charged for executing trades (FAQ)"
  publisher: "COL Financial Group"
  type: web
  canonical_url: "https://colfinancial.freshdesk.com/support/solutions/articles/6000073098-what-are-the-fees-charged-for-executing-trades-buy-and-sell-"
  local_path: null
  edition: superseded
  amended_through: "2025-07-10"
  note: "Modified 10 Jul 2025; predates VAT on the PSE fee."
- slug: bpi-trade-fees-faq
  title: "BPI Trade - applicable trading fees (FAQ)"
  publisher: "BPI Securities"
  type: web
  canonical_url: "https://new.bpitrade.com/faq/what-are-the-applicable-trading-fees/"
  local_path: null
  edition: in-force
  amended_through: "undated"
  note: "Block-sale add-ons SIPF 0.001% and SEC 0.005%."
- slug: pinoymoneytalk-fees
  title: "PSE Stock Trading Fees & Sample Computations (with CMEPA, 12% VAT update)"
  publisher: "Pinoy Money Talk (blog)"
  type: web
  canonical_url: "https://www.pinoymoneytalk.com/fees-computation-buying-selling-stocks/"
  local_path: null
  edition: in-force
  amended_through: "undated"
  note: "Consumer blog; secondary only; corroborates 4 Sep 2025 VAT on PSE fee."
- slug: oxford-business-group-2014-trading-tariffs
  title: "Trading tariffs: commission structures and taxes on stock trades (The Report: Philippines 2014)"
  publisher: "Oxford Business Group"
  type: web
  canonical_url: "https://oxfordbusinessgroup.com/reports/philippines/2014-report/economy/trading-tariffs-commission-structures-and-taxes-on-stock-trades"
  local_path: null
  edition: historical
  amended_through: "undated"
  note: "2014 snapshot of the old PSE minimum-commission scale and fees; secondary."
- slug: pwc-tax-summaries-ph-wht
  title: "Philippines - Corporate - Withholding taxes (Worldwide Tax Summaries)"
  publisher: "PwC"
  type: web
  canonical_url: "https://taxsummaries.pwc.com/philippines/corporate/withholding-taxes"
  local_path: null
  edition: in-force
  amended_through: "2026-08-01"
  note: "\"Last reviewed 01 August 2026\"; secondary source for treaty dividend ceilings."
- slug: pwc-tax-summaries-ph-income-determination
  title: "Philippines - Corporate - Income determination (Worldwide Tax Summaries)"
  publisher: "PwC"
  type: web
  canonical_url: "https://taxsummaries.pwc.com/philippines/corporate/income-determination"
  local_path: null
  edition: in-force
  amended_through: "2026-08-01"
  note: "Dividend-income section (NRFC 25%/15% conditions). Secondary corroboration only."
- slug: pwc-tax-summaries-ph-other-taxes
  title: "Philippines - Corporate - Other taxes (Worldwide Tax Summaries)"
  publisher: "PwC"
  type: web
  canonical_url: "https://taxsummaries.pwc.com/philippines/corporate/other-taxes"
  local_path: null
  edition: in-force
  amended_through: "2026-08-01"
  note: "STT 0.1% scope, DST table, capital gains tax. Page carries its own \"Last reviewed - 01 August 2026\" stamp."
- slug: ftse-geis-ground-rules-2026-09
  title: "FTSE Global Equity Index Series Ground Rules v14.4 (September 2026)"
  publisher: "FTSE Russell (LSEG)"
  type: pdf
  canonical_url: "n/a (archived by another researcher; source URL not recorded here)"
  local_path: pdfs/ftse-geis-ground-rules-2026-09.pdf
  edition: in-force
  amended_through: "undated"
  note: "Rule 6.2 investability weightings, foreign ownership restrictions and foreign headroom (p. 13)."
- slug: oecd-capital-market-review-philippines-2024
  title: "OECD Capital Market Review of the Philippines 2024"
  publisher: "OECD"
  type: pdf
  canonical_url: "n/a (archived by another researcher; source URL not recorded here)"
  local_path: pdfs/oecd-capital-market-review-philippines-2024.pdf
  edition: historical
  amended_through: "undated"
  note: "Pre-CMEPA (STT still 0.6%, SEC minimum-commission removal of Apr 2024 mentioned). Trading-cost tables pp. 45-46; ownership structure pp. 121-122. The text mislabels the removed commission floor as \"1.5% minimum\" (1.5% is the maximum)."
- slug: pdtc-nocd-reit-faq
  title: "PDTC NoCD facility FAQ (REIT allocations)"
  publisher: "Philippine Depository & Trust Corp. (PDTC)"
  type: pdf
  canonical_url: "n/a (archived by another researcher; source URL not recorded here)"
  local_path: pdfs/pdtc-nocd-reit-faq.pdf
  edition: in-force
  amended_through: "undated"
  note: "Omnibus-with-client sub-account structure (pp. 1-2) and nationality/tax-status allocation report (p. 5)."
- slug: pdtc-dds-operating-guidelines-2017
  title: "Operating Guidelines and Procedures for Depository Participants holding Dollar Denominated Securities in the Depository (incl. NoCD facility)"
  publisher: "Philippine Depository & Trust Corp. (PDTC) / PDS Group"
  type: pdf
  canonical_url: "n/a (archived by another researcher; source URL not recorded here)"
  local_path: pdfs/pdtc-dds-operating-guidelines-2017.pdf
  edition: in-force
  amended_through: "2017-01-01"
  note: "Year-level date only (2017) - treat as undated within the year. NoCD features pp. 6, 8-9."
- slug: pse-cn-2023-0027-offshore-collateral-sbl
  title: "PSE Memorandum CN-2023-0027 - SEC approval of offshore collateral in SBL transactions with a foreign party"
  publisher: "Philippine Stock Exchange / SEC"
  type: pdf
  canonical_url: "n/a (archived by another researcher; source URL not recorded here)"
  local_path: pdfs/pse-cn-2023-0027-offshore-collateral-sbl.pdf
  edition: in-force
  amended_through: "2023-05-24"
  note: "Scanned image PDF (no text layer); read via my OCR. Allowed collateral and Qualified Buyer list at pp. 1-2."
- slug: pse-msla-clearance-guidelines-2026
  title: "PSE Revised Guidelines for MSLA Clearance (SEC-approved, 2026)"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2026/05/2026-Revised-Guidelines-for-MSLA-Clearance_SEC-approved.pdf"
  local_path: pdfs/pse-msla-clearance-guidelines-2026.pdf
  edition: in-force
  amended_through: "undated"
  note: "URL taken from the PSE SBL page link list; file archived by another researcher. RR 1-2008 Sec. 8(c) registration deadlines cited at p. 2."
```
