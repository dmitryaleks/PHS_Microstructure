# PSE equities: clearing, settlement, depository and corporate-action processing (input to Chapter 10, "Clearing and settlement")

As-of date of these notes: **6 October 2026**. Evidence labels: **[P]** = primary (SCCP, PSE, PDTC/PDS, SEC, BSP or statute text read directly); **[S]** = secondary only (custodian/ICSD market guides, press); **[I]** = my inference. Citation tokens: `[^slug:N]` = physical (1-based) page N of the archived PDF `kb/pdfs/<slug>.pdf`; `[^slug]` = web page (retrieved 6 Oct 2026 unless noted). Times are Philippine time (PHT, UTC+8). SD = settlement date. CM = clearing member (a PSE trading participant approved by SCCP).

**Headline caveat (currency trap).** The "latest" SCCP Rules and Operating Procedures that SCCP itself publishes are still the 13 March 2018 consolidated texts, which still say "rolling T+3" (HTTP Last-Modified of both files on sccp.com.ph = 27 July 2018 and byte sizes equal to the archived copies, 986,937 and 506,062 bytes) [P] [^sccp-clearing-house-operating-procedures-2018:6] [^sccp-web-rules-page]. Everything that changed afterwards (T+2, 12:00 deadline mechanics, collateral haircuts, allocation algorithm, CTGF rules) lives only in dated "Memo for Brokers" amendments. In-force text must therefore be reconstructed from 2018 text + memos (table in 1.5). No consolidated current rulebook is public.

---

## 1. SCCP: legal status, CCP model, risk management, CTGF, rulebook edition

### Takeaway
SCCP is a 100% PSE-owned, SEC-registered clearing agency (permanent licence January 2002) that becomes the central counterparty to every PSE-executed equity trade by novation, settling DVP Model 3 (multilateral net, cash and securities) at CM (broker) level, not beneficial-owner level. It is a **limited-recourse CCP**: its obligations are capped at what it receives from CMs plus the Clearing and Trade Guaranty Fund (CTGF, ₱1.77bn at 31 Dec 2025 per PSE's audited statements) plus credit lines arranged for the fund. Risk control is daily mark-to-market collateral (MMCD) with full collateralisation of net negative exposure, early-delivery powers, the CTGF and bank credit lines; there is no initial margin.

### Cited findings

**1.1 Legal status, ownership, membership**
- SCCP is a wholly-owned PSE subsidiary under SEC supervision, incorporated 23 Jan 1996, commercial operations from 3 Jan 2000, permanent licence 17 Jan 2002; the SEC authorises it to impose fines, penalties and sanctions on CMs [P] [^sccp-web-about]. PSE's FY2019 annual report: temporary licence, operations from 3 Jan 2000, SEC approved the permanent-licence request on 15 Jan 2002 subject to compliance with SRC Sec. 42 [P] [^pse-annual-report-2019:39]. (Clearstream says "1 January 2002" [S] [^clearstream-ph-market-infrastructure]; treat 15 vs 17 Jan 2002 as approval vs licence date, and Clearstream's date as unreliable.)
- SCCP's own clearing system, the Central Clearing and Central Settlement (CCCS) system, was launched on 29 May 2006: it applies multilateral netting with novation, "the original parties to the contracts disappear" and SCCP "now stands as the Central Counterparty to all trades transacted in the Exchange" [P] [^pse-audited-fs-2025:39]. (Earlier phases of SCCP's operations from 3 Jan 2000 are not described in the documents I read.)
- PSE's FY2025 annual report still describes SCCP as a wholly owned subsidiary responsible for DVP clearing, the CTGF and Fails Management, and risk monitoring [P] [^pse-annual-report-2025:8]. PSE's President/CEO is also SCCP's President/CEO; SCCP's chairman is PSE's chairman; broker-directors sit on SCCP's board [P] [^pse-annual-report-2025:44-47].
- Statute: SRC Sec. 41 (use of unregistered clearing agency unlawful), Sec. 42 (registration; 42.2(f): rules must provide a guarantee fund to which members contribute based on a relative percentage of the daily exposure of the four largest trading brokers; depositories exempt), Sec. 43-44 (book-entry transfers and clearing-agency records as best evidence), Sec. 47.6 (first priority for a registered clearing agency's claims against a participant on dissolution) [P] [^ra-8799-src:46-48] [^ra-8799-src:50]. 2015 SRC IRR Rule 42 (SEC Form 42-CA; risk-management manual, BCP, insurance plan; duty to notify SEC of participant breaches/difficulties) [P] [^sec-2015-src-irr:158-162]; IRR 36.4.4.5 lets the SEC require uniform settlement systems "including the use of a central counterparty (CCP)" [P] [^sec-2015-src-irr:119]; IRR 28.1.2.5.2(b): ₱100m minimum unimpaired paid-up capital for broker-dealers participating in a registered clearing agency [P] [^sec-2015-src-irr:77].
- Rule changes need SEC approval and take effect 15 days after SEC approval unless the SCCP Board/SEC provides otherwise (Rules 1.4.1, 1.4.3); SCCP has final interpretive authority (Rule 1.2.8) [P] [^sccp-clearing-house-rules-2018:10] [^sccp-clearing-house-rules-2018:12].
- CM eligibility (Rule 2.1.1): SEC-licensed broker-dealer, PSE participant in good standing, depository participant, account holder in good standing with a settlement bank; for equities CMs are limited to PSE trading participants [P] [^sccp-clearing-house-rules-2018:5] [^sccp-clearing-house-rules-2018:18]. SCCP's membership page (6 Oct 2026) lists **125 CMs: 122 "Active", 3 "Suspended"** (EquitiWorld Securities, Jaka Securities, Mount Peak Securities); **118 Local, 7 Foreign** (CLSA Philippines; J.P. Morgan Securities Philippines; Macquarie Capital Securities (Philippines); Maybank ATR Kim Eng Securities; SeedBox Securities; UBS Securities Philippines; UOB Kay Hian Securities (Phil.)) [P] [^sccp-web-membership].
- Settlement banks: SCCP's Partners page shows nine bank logos (Asia United Bank, BDO, China Bank, Deutsche Bank, EastWest, Maybank, Metrobank, RCBC, UnionBank) and states each settlement bank is connected to the C&S System in real time [P] [^sccp-web-partners]; Clearstream lists ten (adds HSBC) [S] [^clearstream-ph-settlement-process] (HSBC unverified/possibly lapsed); membership kit requires automatic-debit-arrangement enrolment with BDO or RCBC [P] [^sccp-web-membership].

**1.2 CCP by novation, with capped recourse**
- Rule 3.1: daily multilateral netting on receipt of trades; "no longer a direct link between the original counter-parties". Rule 3.2: novation occurs and "the SCCP now stands between the original trading parties and becomes the Central Counterparty to each Trade"; each net delivery obligation becomes a contract between the net-delivering CM as seller and SCCP as buyer, each net entitlement a contract between SCCP as seller and the net-receiving CM as buyer. Rule 3.3: contracts mirror the exchange trade's terms and benefit CMs as principals only [P] [^sccp-clearing-house-rules-2018:26]. "Novation" is defined as replacing CM-to-CM rights with rights to/from SCCP as CCP [P] [^sccp-clearing-house-rules-2018:7].
- SCCP's own description: after novation it is "seller to all net buying Clearing Members and buyer to all net selling Clearing Members", taking the buyer's credit risk and the seller's delivery risk; settlement is "Delivery-versus-Payment Model 3 or Multilateral Net Settlement" at CM level, not beneficial-customer level [P] [^sccp-web-services]. So SCCP is a CCP by novation (not a mere trade guarantor); the "guarantee" is limited as below.
- Recourse limit (Rule 3.5): SCCP's obligations are limited exclusively to (a) amounts received from CMs on settlement of any Contract, (b) the amount of the CTGF, (c) credit facilities arranged expressly to support the CTGF; if the CTGF is insufficient, CMs are paid pro rata and SCCP "shall remain liable" with the balance paid only as and when funds become available; no other SCCP assets may be used [P] [^sccp-clearing-house-rules-2018:27-28]. Rule 5.3: for an insolvent CM SCCP satisfies its unsettled-trade obligations from the Clearing Fund, advances being for the insolvent member's account [P] [^sccp-clearing-house-rules-2018:35]. SCCP's website repeats the pro-rata/"as and when funds are available" language [P] [^sccp-web-services].
- Scope: only SCCP-eligible exchange trades; SCCP "does not perform any Clearing and Settlement services for non-Exchange trades" [P] [^sccp-clearing-house-operating-procedures-2018:5]; OP 4.1.1 excludes PSE block transactions and negotiated deals from CTGF/fails/collateral coverage [P] [^sccp-clearing-house-operating-procedures-2018:23]. A Nov 2021 consultation proposed that block sales conforming to the settlement cycle be settled and guaranteed by SCCP and excluded non-conforming blocks from CTGF turnover [P, proposal only] [^sccp-memo-03-1121-proposed-amendments:4] [^sccp-memo-03-1121-proposed-amendments:16-17]; whether adopted is unverified (see Gaps).
- Netting dimension: legacy system netted securities by flag (LP, LC, FP, FC), cash multilaterally [P] [^sccp-clearing-house-operating-procedures-2018:6]; the new C&S System uses account types FC/FH/LC/LH (foreign/local x client/house) with identical flags required for collateral transfers [P] [^sccp-cs-quick-guide:10] [^sccp-cs-quick-guide:13]; RBC: netting per broker, per security, per flag [S] [^rbc-ph-market-profile].
- Allocation algorithm (in force since 21 Jan 2025, Annex 11): when SCCP cannot pay everyone in full, price first (highest buy price and lowest sell price settle first), then smallest quantity first, then pseudo-random; SCCP may make partial securities deliveries. It replaced the old "largest outstanding netted amount first" rule [P] [^sccp-memo-02-0125-sec-approval-rules-3-4-5-1-4-6-2-8-7-6:1] [^sccp-clearing-house-rules-2018:27]; SCCP's stated rationale is cash/securities maximisation during the run [P] [^sccp-memo-01-0524-sec-recommended-revisions:2].
- Finality: once Security and Cash Elements settle the trade is final and irrevocable; unwinding "under any circumstances" not allowed (Rule 4.6) [P] [^sccp-clearing-house-rules-2018:31].

**1.3 Risk management: MMCD, early delivery, monitoring**
- MMCD (Rule 8): SCCP marks every CM's unsettled trades daily to the last closing price; exposure = [Sum(PP x MM) - Sum(PP x CP)] + [Sum(PS x CP) - Sum(PS x MM)] where PP/PS = unsettled buy/sell shares, CP = contract price, MM = market (last traded/closing) price [P] [^sccp-clearing-house-rules-2018:44]. T+2 amendment (effective 24 Aug 2023): window cut from three to two days of unsettled trades ("two days' worth of unsettled Trades"), MM defined as last traded/closing price [P] [^sccp-memo-06-0823-sec-approval-t2-amendments:3-4]. Corporate-action price changes are reflected in the MTM (Rule 8.1.6) [P] [^sccp-clearing-house-rules-2018:44].
- Net negative exposure must be fully collateralised (Rule 8.1.7); CMs can cut it by early delivery of the securities causing it (8.1.3, 8.1.10.3) [P] [^sccp-clearing-house-rules-2018:43] [^sccp-clearing-house-rules-2018:45-46]. Notice via C&S message board by 18:00 on the computation day (8.1.9/OP 6.4); collateral due 12:00 noon next business day (8.1.10; OP 6.5); excess withdrawable 09:00-12:00 next day (OP 6.6) [P] [^sccp-clearing-house-rules-2018:45-46] [^sccp-clearing-house-operating-procedures-2018:32] [^sccp-clearing-house-operating-procedures-2018:34]. Late/missing collateral fine: 1st offence 1/4 of 1% of the required collateral, 2nd 1/2 of 1% plus warning, 3rd 1% plus recommendation for suspension (plus out-of-pocket costs) [P] [^sccp-clearing-house-rules-2018:47] [^sccp-clearing-house-rules-2018:62].
- Eligible collateral (Rule 8.1.8, SEC-approved 13 Dec 2022, effective 20 Feb 2023): cash, or securities that are constituents of the PSEi, PSE MidCap and PSE Dividend Yield indices (25% haircut) and "PSE shares" (35% haircut); valued at last close; list reviewed every six months. Haircuts were aligned with CMIC/SEC RBCA position-risk factors (SEC MC 16-2004 Sch. A) [P] [^sccp-memo-02-0223-collateral-haircut-rates:1] [^sccp-memo-07-0823-sec-approved-amendments:3-4]. Before that increase the haircut was a flat 20% on all eligible securities collateral, imposed from 14 Nov 2008 [P] [^pse-audited-fs-2025:40]. Current list: memo 01-0126 (effective 2 Feb 2026: PSEi adds RCR, drops AGI; DivY adds OGP, URC, drops KEEPR, SECB; MidCap adds AGI, APX, drops DD, RCR) [P] [^sccp-memo-01-0126-eligible-collateral-list:1]; a newer list memo 01-0726 (28 Jul 2026) exists but was not archived [P-web] [^sccp-web-memos-index].
- Risk containment (Rule 7.6, SEC-approved and announced 21 Jan 2025, effective immediately under Rule 1.4.3): SCCP "may, in its discretion, require Early Delivery (i.e., not later than SD-1) of the Cash or Securities obligations from one or more Clearing Members" in five situations: (1) unstable conditions or price fluctuations in one or more securities, in addition to the Rule 8 mark-to-market collateral; (2) exposure larger than the CM's financial condition justifies or that places SCCP at risk; (3) a record of frequent rule violations, unsound management or serious operational defects; (4) market conditions or price fluctuations such that SCCP calls on affected CMs to follow "any of the additional risk containment measures under this Rule as determined by SCCP" (none is itemised); (5) when certain risk levels determined by SCCP have been reached. SCCP "shall lift the early delivery requirement" once the risks are no longer present [P] [^sccp-memo-02-0125-sec-approval-rules-3-4-5-1-4-6-2-8-7-6:3]. The May 2024 consultation draft also allowed SCCP to "require additional margins"; SCCP deleted that option because early delivery "may currently be an adequate protection" [P] [^sccp-memo-01-0524-sec-recommended-revisions:3-4]. The same memo's pp.1-2 carry the other approved amendments (Rule 3.4/Annex 11, Rule 5.1.4(3), Rule 6.2.8) [P] [^sccp-memo-02-0125-sec-approval-rules-3-4-5-1-4-6-2-8-7-6:1-2]. Precedent: SCCP imposed "T+1 early delivery" (two business days ahead of the T+3 cut-off) on six named securities (ACE, FPI, MVC, PHES, WIN, WPI) from 2009 until the Board lifted it effective 20 Jan 2012 [P] [^sccp-memo-03-0112-early-delivery-lifting:1]. OP 5.5.1 (2018 text): CMs at a risk level, or trades with unusual price/volume surges, may be required to settle early [P] [^sccp-clearing-house-operating-procedures-2018:29]. A separate 2012-2013 "Settlement Restrictions" scheme (proposed Rule 7.6.1-7.6.4: SCCP Board/PSE Board may restrict an Identified Security or Identified CM by early delivery of securities by net sellers, early delivery of cash by net buyers, or 100% cash collateral where securities are unavailable; "done-through" trading via another TP prohibited during a restriction; own penalty table approved by the SCCP Board 15 Oct 2012) was circulated for comment (memos 04-0812, 02-0413) but does **not** appear in the 2013 or 2018 consolidated Rules, whose Rule 7 ends at 7.5, and the Nov 2021 draft lists existing Rule 7.6 as "None" [P] [^sccp-memo-04-0812-settlement-restrictions-proposal:1-4] [^sccp-memo-02-0413-settlement-restrictions-revisions:1-5] [^sccp-clearing-house-rules-2018:42] [^pse-sccp-revised-rules:42] [^sccp-memo-03-1121-proposed-amendments:26]; treat it as never adopted (inference) and the 2025 Rule 7.6 as its narrower successor.
- Monitoring: unusual settlement obligations (risk multiple vs 6-month moving average), trade concentration (reported to CMIC), monthly Daily Average Netted Obligation vs Net Liquid Capital, recurring fails (>= 2 within 7 trading days), habitual lates (>= 3 per year) [P] [^sccp-web-services] [^sccp-clearing-house-operating-procedures-2018:29]. No initial margin exists in the rulebook (the margin option was deleted from the 2024 Rule 7.6 draft and is absent from the final text of 21 Jan 2025; an "MMCD Fund/Credit Ring Agreement" section is deleted) [P] [^sccp-memo-01-0524-sec-recommended-revisions:4] [^sccp-memo-02-0125-sec-approval-rules-3-4-5-1-4-6-2-8-7-6:3] [^sccp-clearing-house-operating-procedures-2018:37]; Clearstream's "SCCP has proposed to implement margin requirements ... with the SEC" is stale [S] [^clearstream-ph-settlement-process].
- Client-asset protection rule (Rule 2.3.5, SEC-approved, in force 23 Aug 2023): CMs may deliver only securities of the instructing client; using another client's shares to settle is prohibited unless under a securities-borrowing-and-lending arrangement; violations (found by CMIC) are grounds for suspension/termination under Rule 2.5.1 [P] [^sccp-memo-07-0823-sec-approved-amendments:2] [^sccp-memo-03-0623-client-securities-prohibition:1].

**1.4 CTGF: contributions, formula, size, uses, waterfall**
- Monthly contribution per CM = **1/500 of 1% (0.002%, i.e. 0.2 bp)** of the CM's monthly turnover value net of block sales and cross transactions of the same flag, or another rate set by the SCCP Board and approved by the SEC; billed on the first business day, payable within 7 calendar days (Rule 5.1.4(1); OP 4.3.1.1-4.3.1.2; rate amended effective 1 Aug 2007) [P] [^sccp-clearing-house-rules-2018:33] [^sccp-clearing-house-operating-procedures-2018:24]. PSE's accounts state the same formula [P] [^pse-annual-report-2018:121].
- Initial contribution for new/returning TPs: based on the "Ideal Fund Size" (VaR model), pro-rated over existing TPs; the **high of the range for foreign TPs, the average for local TPs**, rounded up to the next ₱100,000; for new TPs in inactive status 50% is due on admission and the balance before trading starts; reviewed after six months using an effective rate of **11%** applied to the CM's daily average trade value (excess refunded, deficiency collected next business day) [P] [^sccp-clearing-house-rules-2018:33] [^sccp-clearing-house-operating-procedures-2018:24-25]. (Nov 2021 draft: full upfront payment, notarised consent for successor TPs, IFS basis changed to "daily average netted obligation" [P, proposal] [^sccp-memo-03-1121-proposed-amendments:16-17]; adoption unverified.)
- Deficiency collection: if trade value averaged **₱1.5bn/day for two calendar months**, all CMs pay deficiency = 11% x daily average trade value of the preceding six months, outright or amortised over two years at an imputed 12% p.a. [P] [^sccp-clearing-house-rules-2018:34]; since 21 Jan 2025 Rule 5.1.4(3) is replaced by: SCCP may, **with SEC approval**, require supplemental contributions from all active CMs when the CTGF is no longer commensurate with a sustained increase in trade volume [P] [^sccp-memo-02-0125-sec-approval-rules-3-4-5-1-4-6-2-8-7-6:2].
- **Ideal Fund Size (OP 4.4.1, 2018 text)**: reviewed semi-annually; "IFS = [Net Trades_LM x LP x ((SD x RL) + ADV)] / 100 + [Net Trades_LM x LP x FC x 180/360]"; Net Trades_LM = net trade value of the four largest members; LP (liquidation period) = 7 days (T+3 settlement plus an allowance for next-day buy-in/sell-out needing another 3 days); SD = 3.23 ("67% probability level"); ADV = 0.04; FC (financing cost) = 15% p.a.; RL = 2.33 (99% coverage). Computed to cover exposure for one settlement cycle (four-largest-members basis mirrors SRC 42.2(f)) [P] [^sccp-clearing-house-operating-procedures-2018:26] [^sccp-clearing-house-rules-2018:32]. The printed unit conventions are ambiguous and the parameters (LP, cycle) predate T+2; no updated parameters are published [I].
- Composition (Rule 5.1.2): PSE contribution, CM contributions, interest income [P] [^sccp-clearing-house-rules-2018:32]; SCCP's website also lists an "SCCP Reserve Fund" [P] [^sccp-web-services]. Investment: Philippine-government securities or other Board-approved instruments (Rule 5.1.5); additional resources (credit lines from settlement banks, insurance) and use of the fund as collateral for credit lines (Rule 5.1.3) [P] [^sccp-clearing-house-rules-2018:32] [^sccp-clearing-house-rules-2018:34]; SCCP keeps a CTGF account at each settlement bank and credit facilities to minimise actual drawings (OP 2.4.2) [P] [^sccp-clearing-house-operating-procedures-2018:8]. Permitted uses: net money obligations, buy-ins, collateral for credit lines or SBL, insurance premium, SCCP losses/expenses incidental to clearing (Rule 5.1.6) [P] [^sccp-clearing-house-rules-2018:34].
- **Size history (the "Client Monies" note to PSE's audited consolidated statements; the CTGF is off balance sheet and treated as trust monies):** ₱786.3m (31 Dec 2013), ₱838.5m (2014), ₱981.5m (2016), ₱1,064.8m (2017), ₱1,097.7m (2018: TP principal ₱688.7m + PSE ₱80.0m + accumulated income net of unrealised loss ₱329.1m), ₱1,247.7m (2019), ₱1,367.2m (2020), ₱1,429.5m (2021), ₱1,476.4m (2022), ₱1,589.5m (2023), ₱1,627.6m (2024) and **₱1,770.7m at 31 Dec 2025** [P] [^pse-annual-report-2014:130] [^pse-annual-report-2017:67] [^pse-annual-report-2018:121] [^pse-annual-report-2019:66] [^pse-audited-fs-2020:84] [^pse-audited-fs-2022:80] [^pse-annual-report-2024-compiled-17a:148] [^pse-audited-fs-2025:86]. Composition at 31 Dec 2025: TP principal contributions ₱952.7m (up ₱49.2m in 2025 after a net fall of ₱34.0m in 2024, when the note's "Contributions" line was negative, which implies refunds exceeded new contributions [I]), PSE's ₱80.0m, accumulated net interest income ₱730.4m and unrealised gains ₱7.7m [P] [^pse-audited-fs-2025:86]. Assets: government debt securities at FVOCI (face ₱1,436.5m, of which ₱98.0m matures within a year), a time deposit ₱308.8m and cash in banks ₱10.0m; under SCCP's rules the fund may be invested only in securities issued or guaranteed by the Republic or other investments approved by SCCP's board [P] [^pse-audited-fs-2025:87] [^pse-annual-report-2024-compiled-17a:149]. SCCP's management fee is 0.1% of the year-end fund (₱1.77m for 2025) [P] [^pse-audited-fs-2025:87]. Beyond the fund, SCCP "appropriated retained earnings amounting to ₱50.00 million for the settlement of trade obligations of defaulting clearing members should the clearing and trade guarantee fund not be enough" (unchanged at 31 Dec 2024 and 2025) [P] [^pse-audited-fs-2025:65]. Clearstream's "around PHP 1.600 bn ... as of 31 December 2023" [S] [^clearstream-ph-settlement-process] agrees with the audited ₱1,589.5m. Year-end unsettled exposure, for context: ₱8.75bn undelivered (net selling) + ₱3.03bn unpaid purchases at 31 Dec 2019 (T+3) [P] [^pse-annual-report-2019:65]; ₱4.36bn + ₱1.64bn = ₱6.01bn at 31 Dec 2024 and ₱4.62bn + ₱1.72bn = ₱6.33bn at 31 Dec 2025 (dollar-denominated: US$16,240 and nil), all settled in the following January with no failed trades [P] [^pse-audited-fs-2025:82].
- **Default waterfall as written (OP 3.11, alternative cash settlement)**: (1) defaulter's cash entitlement held in escrow, (2) its margin collateral, (3) its MTM collateral, (4) its CTGF contribution, (5) SCCP's reserve appropriated for the CTGF, (6) credit lines availed by SCCP, (7) mutualised CTGF contributions [P] [^sccp-clearing-house-operating-procedures-2018:19]. Cash fails are first bridged by SCCP advances (CTGF or credit lines) so receivers are paid on time [P] [^sccp-clearing-house-operating-procedures-2018:10]. A Nov 2021 draft Rule 5.1.7 would order CTGF application as defaulter's contributions, fund interest, SCCP's contributions, then non-defaulters pro rata, with replenishment in reverse order [P, proposal] [^sccp-memo-03-1121-proposed-amendments:17-19]; adoption unverified.
- Refundability: before 2018 "there shall be no return of cash contributions" [P] [^pse-sccp-revised-rules:35]; Rule 5.2 amended effective 1 Aug 2018 (SEC approval 13 Mar 2018) to refund contributions as trade-related assets on cessation/termination, initially only for TPs/CMs actively operating when the amendment took effect [P] [^sccp-clearing-house-rules-2018:35] [^pse-annual-report-2018:47]; further conditions SEC-approved and effective 8 Jul 2025 (regulatory clearances incl. SEC broker-dealer cancellation order, all liabilities settled, audited proof that the CM absorbed the contributions rather than collecting them from clients, bank details; no cheques to "Cash/Bearer") [P] [^sccp-memo-01-0725-ctgf-refund-sec-approval:1-2] [^sccp-memo-02-0624-ctgf-refund-proposal:1-2].
- Interest on CTGF advances (as amended 21 Jan 2025, Rule 6.2.8): the defaulter bears costs, taxes and lost interest from pre-terminating CTGF investments; credit-line advances bear the lender's rate; until paid, stated in the Demand Notice (replaced "BSP overnight borrowing rate plus spread") [P] [^sccp-memo-02-0125-sec-approval-rules-3-4-5-1-4-6-2-8-7-6:2] [^sccp-memo-01-0524-sec-recommended-revisions:3].
- SCCP fees: initial CM fee ₱5,000; **clearing fee 0.0001 (1 bp), VAT-inclusive, of gross trade value per month** [P] [^sccp-clearing-house-rules-2018:62]. Cross-check: H1-2026 SCCP service fees of ₱165.45m against ₱926.54bn trading value equal 1 bp / 1.12 x 2 sides x value (₱165.5m) [I] [^pse-analyst-briefing-1h-2026:7]; FY2025 SCCP service fees of ₱317.99m (+19.12%, "due to a similar percentage increase in turnover value") against turnover of ₱1,780.77bn (average daily ₱7.33bn; 2024: ₱1,494.90bn) equal the same formula (₱318.0m) [P for the inputs, I for the match] [^pse-annual-report-2025:16]; so the 1 bp VAT-inclusive fee, charged on both sides, appears unchanged.
- SCCP's own capital: SCCP's stand-alone statements were not found; PSE's consolidated notes disclose only the CTGF and the ₱50.00m appropriation above, SCCP's unrecognised deferred tax asset (₱3.65m, which shows SCCP uses the optional standard deduction for tax) and an unfunded retirement plan [P] [^pse-audited-fs-2025:39] [^pse-audited-fs-2025:65] [Gap for equity].

**1.5 Which rulebook is in force (edition table)**

| Date (SEC approval / effect) | Instrument | Change | Status |
|---|---|---|---|
| 28 Jun 2012 (eff. 23 Jul 2012) | Rules 6.1.3, 6.2.2, new 6.2.7; Annex 7 / OP 3.14 | Cash collateral pending delivery; two-tier fines | In force (carried into the 2018 text) [^sccp-memo-01-0812-sec-approval-fails-management:1-3] |
| 21 Feb 2013 (eff. 1 Apr 2013) | Revised Rules/OpProcs | Alternative Cash Settlement etc. | Superseded by 2018 text (archived copy `pse-sccp-revised-rules`, 71 pp; its Alternative Cash Settlement rule is marked "amended effective 01 April 2013, approved by the SEC on 21 February 2013") [P] [^pse-sccp-revised-rules:28] |
| 13 Mar 2018 (Rule 5.2/OP 4.3.1.3 eff. 1 Aug 2018) | Consolidated Rules (71 pp) and OpProcs (39 pp) posted on sccp.com.ph | CTGF refundability | Still the posted text; T+3 wording; partly amended below |
| 24 Nov 2021 | Consultation paper + draft "2022 Revised Clearinghouse Rules" (memo 03-1121) | New C&S System terms, T+2, Rule 7.6, CTGF order of application, fails restructure (renumbering 6.2.x/6.3.x) | Draft; later memos use its numbering, so parts were approved; approved consolidated text not published |
| 13 Dec 2022 (eff. 20 Feb 2023) | Rule 8.1.8 | Index-constituent collateral, 25%/35% haircuts | In force |
| 18 Aug 2023 memo (eff. 24 Aug 2023) | Rules + OpProcs "T+2-related" | See section 2/3 | In force |
| 23 Aug 2023 memo 07-0823 | Rules 2.3.5, 4.7-4.9, 6.2.5, 6.3.5, 8.1.8; OP 2.8-2.10, 3.8.3-3.8.4 | Client-share prohibition; early settlement of BISO trades; holiday/unexpected-event rules; multi-trade-date settlement | In force |
| SEC 9 Jan 2024; eff. 5 Mar 2024 | OP 2.5.3.2 (renumbered) | Early batch run | In force |
| 21 Jan 2025 | Rules 3.4/Annex 11, 5.1.4(3), 6.2.8, 7.6 | Allocation algorithm; supplemental CTGF; costs; risk containment (early delivery only, no margin) | In force (full text of all four in the memo) |
| 8 Jul 2025 | Rule 5.2, OP 4.2.1.3 | CTGF refund conditions | In force |
| after 8 Jul 2025 to 11 Sep 2026 | none | No rule/consultation memo in SCCP memo index | [^sccp-web-memos-index] |

Sources for the table: [^sccp-clearing-house-rules-2018:1] [^sccp-memo-03-1121-proposed-amendments:3-4] [^sccp-memo-02-0223-collateral-haircut-rates:1] [^sccp-memo-06-0823-sec-approval-t2-amendments:1] [^sccp-memo-07-0823-sec-approved-amendments:1] [^sccp-memo-01-0324-early-batch-run-effectivity:1] [^sccp-memo-02-0125-sec-approval-rules-3-4-5-1-4-6-2-8-7-6:3] [^sccp-memo-01-0725-ctgf-refund-sec-approval:2] [^sccp-web-rules-page] [^sccp-web-memos-index].

### Inferences
- [I] SCCP functions as a CCP with a small, mutualised, partly pre-funded default fund and no initial margin. FY2025 turnover averaged ₱7.33bn a day (₱1,780.77bn for the year), so the ₱1.77bn CTGF at end-2025 is about a quarter of one average day's turnover and about 28% of the ₱6.33bn of net obligations outstanding at that year-end (T+2 means roughly two days of trades are always open). That is why the rulebook leans on full MTM collateralisation, early delivery and a 12:00 hard deadline rather than on fund size. The fund has grown about 42% since 2019 (₱1.25bn to ₱1.77bn); average daily value was ₱6.10bn in 2024 and ₱7.33bn in 2025 [^pse-annual-report-2025:16].
- [I] The July 2025 "absorbed, not passed to clients" refund condition implies CTGF contributions are expected to be a broker cost, not a client charge.
- [I] Because the posted PDFs are stale, any implementation spec must treat memo amendments as authoritative and re-check SCCP memos monthly.

### Execution implications
- Your economic exposure is to the CM (broker/custodian chain) first; SCCP absorbs a CM default for trade settlement but is recourse-limited to the CTGF plus credit lines. Prefer clearing brokers with strong net liquid capital; SCCP's DANO/NLC monitoring and RBCA data are not public (inference from the monitoring design).
- Size the tail honestly: the mutualised resources are the CTGF (₱1.77bn at end-2025), SCCP's ₱50m appropriated reserve and bank credit lines whose size is not published, against ₱6.33bn of net obligations open at the 2025 year-end and about ₱7.3bn of daily turnover. A large broker's default is absorbed first by that broker's escrowed entitlements and MMCD collateral, so your practical protection is the broker's collateral position and your own custody and segregation arrangements, not the fund [I].
- Collateral burden sits with the broker (daily MTM, due 12:00 next day); expect brokers to ask for pre-funding or pre-positioned inventory on volatile names, and for SCCP to impose SD-1 early delivery (Rule 7.6) on specific CMs/securities in stress.
- Cost model: SCCP clearing fee 1 bp VAT-inclusive on gross value (each side) and CTGF 0.2 bp of turnover are broker-level costs; whether and how brokers pass them on is in the commission chapter.
- Foreign-client (FC) and local-client (LC) trades net separately; a broker cannot net a foreign client's sell against a local client's buy.
- Allocation algorithm only matters in a partial-settlement event (largest price, then smallest quantity, then random).

### Gaps
- Consolidated, SEC-approved current text of the Rules and Operating Procedures (T+2 version) is not published; text of any adopted Rule 5.1.7 waterfall/Rule 6.1 restructure not located (the final Rule 7.6 is in memo 02-0125 p.3).
- Whether block/negotiated trades are now guaranteed by SCCP (Nov 2021 proposal; PSE negotiated-trade circulars are covered elsewhere).
- SCCP's own equity (only the ₱50.0m appropriation is disclosed in the group notes), its CPMI-IOSCO PFMI self-assessment (none found), and updated Ideal-Fund-Size parameters under T+2.
- HSBC's status as a settlement bank.

---

## 2. Settlement cycle, DVP model and the settlement-day timeline

### Takeaway
Equities settle **T+2** for trades executed from 24 Aug 2023 (first T+2 settlement 29 Aug 2023); the predecessor was a rolling **T+3** with the same 12:00 noon cut-off. Settlement is DVP Model 3 multilateral net per CM in SCCP's C&S System (LSEG Millennium Post Trade, live 27 Mar 2023) with cash settled across nine settlement banks and securities at PDTC. Hard deadline 12:00 noon on SD (11:00 and 14:00 batches on double-settlement days); the batch run may start earlier since 5 Mar 2024. **No T+1 plan, consultation or decision was found as of 6 Oct 2026.**

### Cited findings

**2.1 Cycle history and T+2 migration**
- Predecessor: "Settlement shall be performed on a rolling T+3 cycle ... Settlement Cut-Off shall be at 12:00 NN of Settlement Date" (OP 2.1.5; Rule 8.1.1 "settled three Business Days after Transaction Date") [P] [^sccp-clearing-house-operating-procedures-2018:6] [^sccp-clearing-house-rules-2018:43].
- SCCP Memo 01-0623 (13 Jun 2023): target T+2 effective trade date 24 Aug 2023; last T+3 trades (23 Aug) and first T+2 trades (24 Aug) both settle 29 Aug 2023 because 28 Aug is a holiday; industry-wide testing 29 Jul-7 Aug 2023; revised rules had been submitted to the SEC in December 2021 [P] [^pse-cn-2023-0031-t2-settlement:2-3]. PSE CN-2023-0031 (23 Jun 2023) relayed it [P] [^pse-cn-2023-0031-t2-settlement:1].
- SEC En Banc approved the 24 Aug 2023 go-live on 10 Aug 2023 [P] [^sccp-memo-04-0823-t2-go-live:1] [^sccp-memo-05-0823-settlement-dates-t2-heroes-day:1]; SEC approval of the T+2-related Rules/OP amendments announced 18 Aug 2023, effective on implementation 24 Aug 2023 [P] [^sccp-memo-06-0823-sec-approval-t2-amendments:1]. PSE's releases (15 Aug and 4 Sep 2023) confirm the dates and that the first settlements were completed before deadline [P-web] [^pse-pr-t2-go-live] [^pse-pr-t2-migration-complete].
- Two-week transition (SEC-approved): deadlines +1 hour. 29 Aug 2023: Batch 1 (trade date 23 Aug, T+3) 12:00 PM instead of 11:00 AM; Batch 2 (24 Aug, T+2) 3:00 PM instead of 2:00 PM; 30 Aug-11 Sep 2023: 1:00 PM instead of 12:00 NN; regular 12:00 NN from 12 Sep 2023; during the extension late-settlement penalties applied only from 1:01 PM [P] [^sccp-memo-02-0723-transition-period:1] [^sccp-memo-04-0823-t2-go-live:1-2]. (The June memo had planned 12:30 PM [P] [^pse-cn-2023-0031-t2-settlement:3]; the SEC-approved figure was 1:00 PM [P] [^sccp-memo-02-0723-transition-period:1] [^sccp-memo-04-0823-t2-go-live:1-2].)
- Why T+2 was feasible: the new C&S System supports any cycle, multiple trade dates per settlement date and multi-currency settlement, receives trades from the PSE engine in real time and uses ISO 20022 with banks and depository; SCCP board awarded the project to Millennium IT/LSEG Technology on 15 May 2019; go-live 27 Mar 2023 [P] [^sccp-memo-03-1121-proposed-amendments:3] [P-web] [^pse-pr-sccp-new-cs-system].
- C&S System project record: the project was "put on hold a number of times" in earlier years to give way to the new trading system and the planned PDS Group acquisition, and the board awarded it on 15 May 2019 [P] [^pse-annual-report-2018:47] [^pse-annual-report-2019:27]; SCCP signed the software-licence/maintenance and consultancy agreements with Millennium IT (an LSEG subsidiary) by 4 Dec 2019 [P] [^pse-17c-2019-12-04-sccp-millennium-it-agreements:1-2]; PSE's annual reports then forecast go-live in the first quarter of 2022 (FY2020 report) and the second quarter of 2022 (FY2021 report) [P] [^pse-annual-report-2020:47] [^pse-annual-report-2021:32]; it happened on 27 Mar 2023, about a year after the first forecast, and the T+2 cycle followed five months later [I from the dates].
- What PSE's FY2025 audited statements say about the system and the T+2 move: the system "can accommodate any settlement cycle, unlike the previous system which was hardcoded with settlement cycle T+3", settles two trade dates in one settlement date, "is capable of being connected directly to the PSE trading engine, which will make real time marking to market possible in the future" (so MTM is still end-of-day), and let SCCP "release the cash and securities entitlements of its clearing members at a much earlier time" [P] [^pse-audited-fs-2025:40]. The same note says brokers, custodian banks, PDTC, transfer agents, PSE's Issuer Regulation Division and CMIC took part in working groups, readiness activities and testing over a five-month period before the T+2 migration on 24 Aug 2023, and lists the expected benefits (lower credit and counterparty risk, cash deployment efficiency, more liquidity, lower collateral requirements) [P] [^pse-audited-fs-2025:41].
- **T+1:** no T+1 or shorter-cycle memo, consultation or SEC action appears in SCCP's memo index through 11 Sep 2026 [P-web] [^sccp-web-memos-index]; PSE's 2026 AGM report and 1H-2026 analyst briefing list the integration roadmap (single post-trade system, new depository system, Nasdaq Eqlipse trading engine) without any settlement-cycle change [P] [^pse-asm-2026-president-report:28] [^pse-analyst-briefing-1h-2026:31] [^pse-analyst-briefing-3m-2026:24-25]; Clearstream (updated 5 Jan 2026) still shows equities T+2 [S] [^clearstream-ph-settlement-process], and PSE's own circular of 10 Sep 2026 on dual-class declassification still calls T+2 "the standard" settlement cycle [P] [^pse-cn-2026-0041-declassification-price-suspension:1].
- Dated international comparison: PSE's FY2025 audited statements still say T+2 "aligned the Philippine settlement cycle with major international markets including the U.S., Europe, Canada, Australia, Japan, Hong Kong" [P] [^pse-audited-fs-2025:41]; that sentence is dated, because the US and Canada have settled T+1 since 28 May 2024 (general market knowledge, not a PSE source) [I].
- Fixed income is different: the only T+1 items found are fixed-income conventions at PDEx, not equities: PDEx Trading Convention Sec. 6 already sets the standard fixed-income settlement date at the next trading day (T+1), and a proposal posted on 20 Jul 2026 on PDS's "Rule Proposals for Approval of the SEC" list (text updated as of Dec 2024, earlier version approved by PDEx's Market Governance Board in Mar 2022) would add "spot" settlement up to T+3 and an "extended settlement date" of up to two further trading days for trades with offshore clients that need a longer pre-settlement period to reconcile details with global custodians, against an extension fee of ₱2,500 per day (₱5,000 in the 2022 text), and treat settlement beyond that as a failed trade [P] [^pdex-proposed-settlement-date-conventions-2026:1-2] [^pds-web-rules]. Do not read this as an equities T+1 plan [I].

**2.2 DVP model and account structure**
- DVP Model 3 (multilateral net for both legs) with SCCP guaranteeing DVP [P] [^sccp-web-services] [^sccp-clearing-house-operating-procedures-2018:5]. Securities move by book-entry at PDTC between CM Securities Settlement Accounts and SCCP's accounts; cash moves between CM Cash Settlement Accounts at settlement banks and SCCP's nostro [P] [^sccp-clearing-house-rules-2018:31] [^sccp-clearing-house-operating-procedures-2018:6-7]. CMs hold a Cash Settlement Account (and a Cash Collateral Deposit Account) at a settlement bank; one account per currency under the new system [P] [^sccp-clearing-house-rules-2018:12-13] [^sccp-memo-03-1121-proposed-amendments:7-8].
- New C&S System operations view: balance types Free / Earmarked (early delivered) / Pending Withdrawal (PDTC confirmation) / Pending Debit / Pending Credit; maker-checker ("dual approval") on early delivery, collateral and share-withdrawal instructions; PHP and USD modules [P] [^sccp-cs-quick-guide:6] [^sccp-cs-quick-guide:9-14]. SCCP also created four PHP and four USD securities collateral accounts per CM in PDTC's eClearSettle (memo 01-0222, Feb 2022) [P] [^sccp-memo-01-0222-collateral-accounts-pdtc:1-2].

**2.3 Settlement-day timeline in force (PHT)**

| Time | Event | Source / status |
|---|---|---|
| T+1 morning | Obligation (and Cash List) available; Cash List to settlement banks by first business day after transaction date | Rule 4.1.2; OP Annex 1 [P] [^sccp-clearing-house-rules-2018:29] [^sccp-clearing-house-operating-procedures-2018:38] (2018 text) |
| SD 08:00-10:00 | "Forecast" netting: forecast cash call and securities obligations viewable | [P] [^sccp-cs-quick-guide:5] [^sccp-cs-quick-guide:7] |
| SD 10:00-12:00 | "Final" netting: cash call and final securities obligations; fund Cash Settlement Account, move securities to the Settlement Account | [P] [^sccp-cs-quick-guide:5] [^sccp-cs-quick-guide:7] |
| SD 11:30 | Latest time PSE-authorised trade amendments/cancellations are reflected in the C&S System | Rule 4.1.3 as amended [P] [^sccp-memo-06-0823-sec-approval-t2-amendments:2] |
| **SD 12:00 noon** | Settlement deadline/cut-off for cash (good cleared funds confirmed by the bank to the C&S System) and securities (credited at PDTC); SCCP verifies sufficiency (Rule 4.1.4); **batch run starts** (DVP; deliveries before receipts) | OP 2.5.4.1; Rule 4.1.4 [P] [^sccp-clearing-house-operating-procedures-2018:9-10] [^sccp-memo-06-0823-sec-approval-t2-amendments:2] |
| SD before 12:00 | **Early batch run** if all CM cash and securities obligations are in; SEC condition: email notice to CMs and settlement banks 10 minutes before the run. Proposed in memo 08-0823 (30 Aug 2023; SCCP Board-approved 16 Aug 2023; comments to 6 Sep 2023) because the old system hard-coded the 12:00 start whereas the new C&S System can start the run as soon as all obligations are delivered; also applies to the 11:00 and 14:00 batches on double-settlement days | Effective 5 Mar 2024 [P] [^sccp-memo-08-0823-early-batch-run-proposal:1-2] [^sccp-memo-01-0324-early-batch-run-effectivity:1-2] |
| Double-settlement days | Batch 1 deadline 11:00 AM, Batch 2 deadline 2:00 PM; max two trade dates per day | Rule 4.9; OP 2.10 [P] [^sccp-memo-07-0823-sec-approved-amendments:7-8] |
| SD 12:00-14:00 / after 14:00 | "Late" window vs "fail": penalty tiers (see 3) | [P] [^sccp-clearing-house-rules-2018:62] |
| SD ~13:15 / 13:30 (2018 text) | Cash shortages funded from CTGF/credit lines by 13:15; "sweep-out" credits Due Broker proceeds to receiving CMs' cash accounts by 13:30 | OP 2.5.4.2; not re-stated in T+2 amendments [P] [^sccp-clearing-house-operating-procedures-2018:10] |
| SD 15:00 | Notice of Securities Default (moved from 13:30 by the T+2 amendment) | [P] [^sccp-memo-06-0823-sec-approval-t2-amendments:6] |
| SD 17:00 | Notices of possible overnight cash/securities fail to CMIC (moved from 15:00); Buy-In/Sell-Out notice and request to PSE; preventive-suspension notice | [P] [^sccp-memo-06-0823-sec-approval-t2-amendments:6-7] |
| SD+1 09:15 / 10:00 / 12:00 | Cure deadline and suspension; buy-in/sell-out executed; Demand Notice | see 3 |
| Trade date 18:00 | MMCD requirement posted; collateral due 12:00 next business day | [P] [^sccp-clearing-house-rules-2018:45] |

- Historical performance (T+3 era, share of CM obligations met by the 12:00 deadline per the annual reports): 2015 cash 99.99% and securities 99.98%; 2016 securities 99.99% and cash 99.98%; 2017 securities 99.98% and cash 99.97%; average time SCCP released Due Broker entitlements 12:34 (2015), 12:28 (2016), 12:31 (2017); "no overnight fails" in 2015 and 2016 [P] [^pse-annual-report-2015:66] [^pse-annual-report-2016:72] [^pse-annual-report-2017:32]. 2018: compliance 99.99% (securities) and 99.96% (cash), average release of entitlements 12:37 p.m.; 2019: 99.99% for both, average release by 12:30 p.m.; no overnight settlement default in either year, so SCCP did not draw its settlement-bank credit facilities [P] [^pse-annual-report-2018:47] [^pse-annual-report-2019:27]. The annual reports for FY2020 onward (all read) no longer print compliance or release-time statistics, so there are no T+2-era figures; the only recent data are year-end snapshots: all trades outstanding at 31 Dec 2024 and 31 Dec 2025 were settled in the following January and "no failed trades occurred from these transactions" [P] [^pse-audited-fs-2025:82].
- Settlement finality: trades settled in SCCP's run are final and irrevocable (Rule 4.6; see 1.2) [P] [^sccp-clearing-house-rules-2018:31]. For the interbank cash leg, BSP's Peso RTGS rules (M-2022-049) make a payment "final and irrevocable" once the paying and receiving participants' settlement accounts are debited and credited, and say the RTGS will settle the money leg of a security transaction "only when the security involved has been delivered or at least earmarked by the concerned FMI" (DvP) [P] [^bsp-m-2022-049-peso-rtgs-rules:8]; the documents do not say whether SCCP's equity cash legs use that DvP interface, so treat the DvP sentence as the BSP's general rule for FMIs, not as a description of SCCP's settlement banks [I].

**2.4 Cash leg: settlement banks and PhilPaSSplus**
- Cash is netted per CM into a Net Money Obligation/Entitlement; CMs fund the Cash Settlement Account with cleared funds; the settlement bank confirms to SCCP online and funds move to SCCP's nostro; Rule 4.1.2's Cash List also tells banks how much each must pay another "for the synchronization of funds between them" [P] [^sccp-clearing-house-rules-2018:29] [^sccp-clearing-house-rules-2018:31]; the 2024 early-run memo refers to the banks' "rebalancing process" [P] [^sccp-memo-01-0324-early-batch-run-effectivity:2].
- Funding modes: cheques with same-day value backed by credit lines/bills-purchase lines, or RTGS; SCCP urges PhilPaSSplus funding; settlement banks guarantee the cash figures uploaded to C&S [S] [^clearstream-ph-settlement-process] [^rbc-ph-market-profile].
- PhilPaSSplus (BSP Peso RTGS): operates Mondays to Fridays 09:00-17:45, with intra- and inter-FI transactions settled 09:00-17:45 on a normal day [P] [^bsp-philpassplus-primer:10] [^bsp-schedule-peso-rtgs:1]. **Not yet changed**: BSP's July 2026 FAQ says the Peso RTGS currently runs "8.75 hours a day, 5 business days a week" and that a **22/7 regime has a target soft launch in November 2026** (22 hours a day, 7 days a week except nationwide regular/special non-working holidays), with windows 00:00-08:59 (before normal hours), 09:00-19:00 (normal hours) and 19:01-22:00 (after hours), a 22:01-23:59 housekeeping gap, weekend transactions value-dated Monday, sending in extended hours optional, and no commitment yet on extending DvP/eDvP/PvP securities windows ("welcomes the potential extension ... subject to market demand, operational readiness and ... arrangements between the BSP and the relevant FMIs") [P] [^bsp-faqs-22x7-peso-rtgs-2026-07:1-4] [^bsp-web-payments-settlements]. SCCP has issued no corresponding memo through 11 Sep 2026 [P-web] [^sccp-web-memos-index].
- Dependency: when government offices including PhilPaSS and PCHC check clearing are closed, SCCP cannot settle (Business Day definition; Rule 4.9) [P] [^sccp-memo-07-0823-sec-approved-amendments:7] [^sccp-memo-03-1121-proposed-amendments:5].

**2.5 Calendar rules (holidays, unexpected closures, double settlement)**
- SCCP posts adjusted settlement dates for nationwide holidays at least two weeks ahead (regular and special non-working holidays in the official list) and, for ad hoc special holidays or calamity/civil-disturbance closures, "no later than 10:00 AM of the next applicable business day"; settlement dates roll on the rolling cycle [P] [^sccp-memo-07-0823-sec-approved-amendments:4-6].
- If a trading day coincides with a day when PhilPaSS/PCHC are closed, its settlement coincides with that of the prior trade date; where more than two consecutive trading days lack settlement, dates are spread so that at most two trade dates settle per day; MTM covers all unsettled trade dates [P] [^sccp-memo-07-0823-sec-approved-amendments:7-8]. Worked example: PhilPaSS suspended 24 Jul 2023 (trading open): trades of 21 and 24 Jul both settled 27 Jul (11:00 AM and 2:00 PM batches), MTM covered four unsettled trade dates [P] [^sccp-memo-01-0723-philpass-suspension:1]. Another: trades of 23 and 24 Aug 2023 both settled 29 Aug [P] [^sccp-memo-05-0823-settlement-dates-t2-heroes-day:1].
- PSE policy (2018 proposal) is to stay open on special non-working days in the NCR and on days when only government work is suspended; SCCP's matching guideline was "trading without settlement" [P] [^pse-cn-2018-0023-trading-without-settlement-proposal:1] [^pse-cn-2018-0023-trading-without-settlement-proposal:3].
- Incident log from the memo index (titles only unless noted): PDTC technical problems 27 Sep 2018 (02-0918), 19-21 Apr 2022 (settlement of 19 Apr trades slipped to 21 Apr: memos 04-0422/06-0422 [P]), 20 May 2022 (03-0522); PhilPaSS(plus) 26 Oct 2020 (03-1020), 11-12 Nov 2020 (suspensions), 10 Feb 2022 (entitlements released after 17:50; last securities 17:24, last cash 17:35 [P]), 23 Aug 2022 (03-0822), 24 Jul 2023 (no settlement); "No clearing and settlement" 24 Jul 2024 and 29 Aug 2025; "C&S System available until 5 PM only" on several days 2024-2026 [^sccp-memo-02-0222-delayed-settlement:1] [^sccp-memo-04-0422-readjustment-apr19-2022:1] [^sccp-memo-06-0422-ongoing-settlement:1] [^sccp-web-memos-index].

### Inferences
- [I] On a normal day cash and securities for exchange trades finish between 12:00 and roughly 13:30; the effective hard stop for upstream funding is therefore the morning of SD, and for custodian-chain funding earlier (see section 6).
- [I] Operational slippage risk is dominated by PhilPaSS/PDTC outages and typhoon closures, not by CM failures; two-day slippage has occurred (Apr 2022).
- [I] The T+2 cycle was designed with SCCP-side flexibility (any cycle supported), so a later shortening is technically cheap, but nothing has been proposed.

### Execution implications
- Compute SD from SCCP's holiday memos, not from a generic T+2 business-day rule: adjusted dates can pair two trade dates on one SD and change collateral timing (MTM covers all unsettled dates).
- For foreign-funded flow, PHP funding must be at the broker/custodian before 12:00 SD; CM-level netting means your fills net against the broker's other clients of the same flag only for SCCP purposes, not for your custodian instruction.
- Assume a 12:00-14:00 receipt window for proceeds (average release historically about 12:30) when planning intraday recycling; same-day turnaround of proceeds is custodian-dependent.
- Keep the calendar feed alive for calamity days (announced by 10:00 AM next business day, i.e. after you may already have traded).
- No T+1 transition work to schedule; monitor SCCP memos.

### Gaps
- Official SCCP T+2 Operating Procedures text (intraday times such as 13:15/13:30 sweep) is not republished; the 2018 times may have changed with the new system.
- Whether SCCP/PDTC/settlement banks will use BSP's extended (22/7) RTGS hours after the targeted November 2026 soft launch; no SCCP statement yet.
- Settlement statistics after 2019 (compliance rates, release times, fail counts); none are published in the annual reports.
- When T+3 itself replaced earlier cycles (not needed for current design).

---

## 3. Fails management, buy-ins and penalties

### Takeaway
SCCP pays the receiving side first (CTGF/credit lines) and holds the defaulter's counter-leg in escrow. If unresolved by **09:15 on SD+1** the defaulter is preventively suspended and SCCP **executes a sell-out (cash fail) or buy-in (securities fail) at 10:00** through a designated PSE trading participant, no commission, at prevailing market prices with a price-setting fallback; costs and price differences go to the defaulter. Buy-in/sell-out trades settle early where practicable. A cash-close-out ("Alternative Cash Settlement": highest regular-lot price + 10%) exists if the buy-in fails. Fines are ₱1,000 + 0.125% (12:00-14:00) or 0.25% compounded daily (after 14:00 or unpaid).

### Cited findings
- **Definitions**: Late Cash Payment/Late Securities Delivery = after the cut-off but before end of business on SD; Overnight Fail = default unresolved at end of business on SD [P] [^sccp-clearing-house-rules-2018:7].
- **Cash fail**: SCCP advances the deficit from the CTGF or credit lines, holds in escrow the defaulter's receivable securities (not less than the fail), charges the Table 3.14 penalty; if unpaid by 09:15 on SD+1 SCCP executes a sell-out of the escrowed securities at 10:00; proceeds first reimburse advances, penalties, taxes and costs; sell-out trade is a normal PSE trade [P] [^sccp-clearing-house-operating-procedures-2018:7] [^sccp-clearing-house-operating-procedures-2018:17] [^sccp-memo-06-0823-sec-approval-t2-amendments:7].
- **Securities fail**: SCCP holds in escrow the defaulter's receivable cash and/or securities (>= the fail); if the net seller has not delivered by 09:15 on SD+1 and a borrowing (SBL) had not been executed, SCCP suspends and executes the buy-in at 10:00 [P] [^sccp-clearing-house-operating-procedures-2018:7] [^sccp-clearing-house-operating-procedures-2018:17] [^sccp-memo-06-0823-sec-approval-t2-amendments:8]. Buy-in costs and price differences are charged to the defaulter on top of penalties [P] [^sccp-clearing-house-operating-procedures-2018:17].
- **Execution mechanics**: SCCP coordinates with the PSE (FTAC) and uses PSE trading participants; BISO trades carry **no brokers' commission**; SCCP is recorded as buyer "acting for and on behalf of the defaulting seller" (or seller for sell-out); contracts are irrevocable; a BISO Order is signed by SCCP's COO and copied to PSE's President [P] [^sccp-clearing-house-operating-procedures-2018:20]. Nov 2021 draft details (adoption unverified): orders posted in the normal market, minimum board-lot execution with excess for the defaulter's account, withdrawal if the defaulter cures before execution, late cure still leaves the defaulter as compulsory counterparty [P, proposal] [^sccp-memo-03-1121-proposed-amendments:21-25]. SEC-approved since 23 Aug 2023: buy-in and sell-out trades settle earlier than the regular cycle "as far as practicable" [P] [^sccp-memo-07-0823-sec-approved-amendments:2-3].
- **Pricing**: buy-in at prevailing offer; if none, below the lowest of three references, sell-out at prevailing bid, else above the highest. **Document conflict**: OP 3.10.5.1 says buy-in reference "last closing price plus two price fluctuations", Rule 6.2.6 says "last closing price less two fluctuations"; sell-out references are "closing price less two fluctuations" in both. If buy-in price < contract price the difference is credited to the CTGF; if higher it is charged to the defaulter (mirror for sell-out) [P] [^sccp-clearing-house-operating-procedures-2018:17-18] [^sccp-clearing-house-rules-2018:37] [^sccp-clearing-house-rules-2018:39].
- **Alternative Cash Settlement (cash close-out)**: if the buy-in fails wholly/partly and the SCCP President/COO decides, receivers are paid cash = highest regular-lot price at execution (or last traded day) **plus a 10% premium**; invocable after failure to buy on SD+1 where the security, trade size relative to CTGF exposure, or the defaulter is deemed risky, otherwise after trading hours on the **second business day after SD** (T+2 amendment; was T+6 / "highly risky") [P] [^sccp-clearing-house-operating-procedures-2018:18-19] [^sccp-memo-06-0823-sec-approval-t2-amendments:2]. The COO bears no liability for the decision [P] [^sccp-clearing-house-rules-2018:28].
- **Cash as collateral in lieu of delivery**: management may accept cash collateral up to 17:00 on SD when the failure is beyond the CM's control, with delivery by 10:00 next trading day or suspension; the cash is then used for the buy-in [P] [^sccp-memo-06-0823-sec-approval-t2-amendments:3]. Clearstream dates this "Revised Fails Management Rules" to July 2012 [S] [^clearstream-ph-settlement-process].
- **Notices and suspension chain (SD, T+2 text)**: 15:00 Notice of Securities Default; 17:00 notices to CMIC, BISO notice/request to PSE and notice of preventive suspension to the defaulter; **09:15 SD+1** new notice (OP 3.7(j)) to CMIC and PSE that the defaulter will be placed under preventive suspension, recommending immediate preventive suspension from trading; 12:00 SD+1 Demand Notice (reimbursement of advances plus penalties, interest, taxes); the suspension is lifted only on full payment, subject to confirmation by the SCCP Risk Management Committee (formerly "Fails Management Committee") or Board; suspension notices are published on SCCP's website (no longer the PSE electronic board/website) [P] [^sccp-memo-06-0823-sec-approval-t2-amendments:6-8]. The 2018 text instead recommended immediate suspension only if the Demand Notice stayed unpaid between 12:00 and 15:00 on SD+1; the T+2 redline struck that sentence [P] [^sccp-clearing-house-operating-procedures-2018:21] [^sccp-memo-06-0823-sec-approval-t2-amendments:8]. Default handling is confidential: no advance announcement of BISO (OP 3.4) [P] [^sccp-clearing-house-operating-procedures-2018:13].
- **No more share borrowing after a buy-in**: the 2018 text had SCCP borrow the bought-in quantity to deliver immediately and charge the defaulter interest until T+3 settlement; the T+2 redline deleted the borrowing sentence (interest/charges now accrue until all obligations are fully paid), and the Nov 2021 rationale says the new system "assigns" the buy-in trade to the defaulting CM so receivers are delivered for the defaulter's account [P] [^sccp-clearing-house-operating-procedures-2018:21] [^sccp-memo-06-0823-sec-approval-t2-amendments:8] [^sccp-memo-03-1121-proposed-amendments:25].
- **Fines (Rules Annex 7 / OP 3.14; unchanged by the T+2 amendment)**: late cash or securities after 12:00 and up to 14:00 on SD: ₱1,000 + 1/8 of 1% (0.125%) of the fail value plus any advance charges and out-of-pocket costs; cash/securities fails after 14:00 or not made: ₱1,000 + 1/4 of 1% (0.25%) of the fail value **compounded daily** until paid/delivered or advances repaid, plus costs, and preventive suspension if not cured by 09:15 SD+1 [P] [^sccp-clearing-house-rules-2018:62] [^sccp-memo-06-0823-sec-approval-t2-amendments:4]. Collateral-default fines in 1.3.
- **When the fine tiers and the cash-collateral rule took effect**: SEC approved on 28 Jun 2012 (letter received 13 Jul) and the amendments took effect **23 Jul 2012**: new Rule 6.2.7 (cash as collateral pending delivery); a lower fee of ₱1,000 + 1/8 of 1% for "Late Settlements" (12:00-14:00) while "Settlement Fails" (after 14:00 or not made) stayed at ₱1,000 + 1/4 of 1% compounded daily; CMs were reminded that repeated fines are grounds for suspension/termination under Rule 2.5.1(b) [P] [^sccp-memo-01-0812-sec-approval-fails-management:1-3].
- **Sanction ladder**: repeated violations, suspension for a third time -> termination (Rule 2.5.1); preventive suspension (2.5.3); appeals to SEC within 10 business days without stay (2.5.5) [P] [^sccp-clearing-house-rules-2018:24-25]. Recurring fails (>= 2 in 7 trading days) are reported to CMIC [P] [^sccp-clearing-house-operating-procedures-2018:29]. Enforcement example: EquitiWorld Securities suspended 25-27 Mar 2024 under Rule 2.5.1(a)/(b) for persistent late cash payments from Feb 2020 to Nov 2023 [P] [^sccp-memo-03-0324-clearing-member-suspension:1]; in Nov 2024 the SEC En Banc ordered CMIC to take over the firm "for the purpose of settling [its] liabilities to its customers, the PSE and other trading participants", CMIC filed a proposed allocation plan in May 2025 and the SEC approved the early release of intact shares to clients in June 2025 [P] [^pse-audited-fs-2025:59] [^pse-audited-fs-2025:89].
- **Custodian-side**: unmatched instructions auto-cancel at the end of the third business day after the first attempted settlement date; penalties are passed through and must be pre-funded by SD-1 14:30 PHT [S] [^clearstream-ph-settlement-services].
- **Short sales and fails**: short selling needs borrowed stock (SBL); a borrowing executed with a lender cures a fail before buy-in (OP 3.10.4) [P] [^sccp-clearing-house-operating-procedures-2018:17]; SBL rules are covered elsewhere.

### Inferences
- [I] The fine is economically a 12.5-25 bp per-event cost on the notional plus daily compounding, but the dominant risk to a defaulting broker's client is the buy-in price, which is "prevailing offer" at 10:00 and can be well above the contract price; the difference is charged to the CM and will be passed to the client.
- [I] Buy-ins and sell-outs put a one-off block of order flow into the failing security at about 10:00 on SD+1; with no commission and a single designated TP, such executions may show up as agency prints under one broker code (unverified).

### Execution implications
- Ensure every sell is covered at the broker's PDTC settlement account (or borrowed) by 12:00 SD; leave no reliance on late-day cure: after 14:00 the fine doubles and 09:15 SD+1 triggers suspension and a market buy-in.
- Treat your broker's financial standing as a fail-risk factor: broker suspension (e.g., 2024 case) can freeze executions and trigger sell-outs of escrowed securities.
- For execution cost models, include the buy-in tail: price difference + 0.25%/day + brokers' pass-through.
- Pre-matching with custodians must finish before the custodian's own cut-offs (section 6) so a custodian-side mismatch does not cause a market fail.

### Gaps
- Whether the 2012-2013 "Settlement Restrictions" penalty table (memos 04-0812, 02-0413) was ever SEC-approved; it is absent from the posted 2018 Rules.
- The T+2-era Operating Procedures renumbering means the section numbers used above (2018 text) are legacy; Rule 6.2/6.3 numbers follow the Nov 2021 draft.
- Final fines for custodian-level failures are custodian-specific and unpublished.

---

## 4. Depository, custody and beneficial-owner visibility

### Takeaway
PDTC (Philippine Depository & Trust Corp.), formerly PCD, is the sole central securities depository for PSE-listed equities. Lodged shares are immobilised in the name of **PCD Nominee Corporation (PCNC)** (separate Filipino and non-Filipino holdings); participants (brokers, custodians) hold book-entry positions and are treated by PDTC as beneficial owners, so beneficial-owner detail exists only at participant level except under the **Name-on-Central-Depository (NoCD)** facility (mandatory for dollar-denominated shares since 2017, offered for REITs, expansion to all stocks planned). A "no-jumbo" rule has required electronic lodgement of all registered securities of listed companies since 1 July 2010. PSE now controls PDTC's parent (beneficial ownership of PDS Group 94.55% at 5 Mar 2026).

### Cited findings
- **Role and ownership**: PDTC provides depository services for equities (and fixed-income registry); PDSHC holds 97.72% of PDTC and 100% of PDEx [P] [^pse-17c-2024-12-26-pdshc-acquisition-agreements:5]. PSE signed agreements on 26 Dec 2024 to acquire up to 61.92% of PDSHC (SEC approval 19 Dec 2024; ₱600/share, ₱2.32bn total, enterprise value ₱3.75bn) to vertically integrate the depository with trading, clearing and settlement [P] [^pse-17c-2024-12-26-pdshc-acquisition-agreements:3-5]. PSE beneficially owned **92.06% of PDS at 30 May 2025 and 94.55% at 5 Mar 2026** [P] [^pse-asm-2025-presidents-report:32] [^pse-analyst-briefing-3m-2026:25]. PSE's consolidated statements show PDSHC owned 94.21% at 31 Dec 2025 (53.34% at 31 Dec 2024; PDSHC's income statement is consolidated only from 1 Jan 2025), and 94.21% plus the 0.34% bought from PDIC on 4 Feb 2026 equals the 94.55% above [P for the inputs, I for the arithmetic] [^pse-audited-fs-2025:16] [^pse-annual-report-2025:16]. The amended 17-C of 4 Feb 2026 (closing of the PDIC sale, 0.34%) gives the closing trail: PSE's existing 20.98% plus purchases of 4,603,217 PDSHC shares (73.65% of the company; ₱2.76bn at ₱600) from SGX, Whistler, SMC, Golden Astra (32.36%, closed 27 Dec 2024), FINEX and IHAP (2.19%, by 17 Jan 2025), AIA (4%, 31 Jan 2025), BAP and member banks (18.80%, 24 Feb 2025), SSS and Insular (2 Apr 2025), Citicorp, TCS, Mizuho, MUFG, LandBank and PDIC, leaving PSE "beneficially" owning **94.55%**, "subject to customary post-closing conditions" [P] [^pse-17c-2026-02-04-pdic-pdshc-shares:3-5] [^pse-17c-2026-02-04-pdic-pdshc-shares:9]; the remaining ~5.45% is therefore held by holders that had not sold at that date [I]. (That filing prints the SEC approval date as 19 Dec 2023, whereas the original 26 Dec 2024 filing says 19 Dec 2024 [^pse-17c-2024-12-26-pdshc-acquisition-agreements:3]; I treat 2023 as a typo [I].) Integration roadmap: "single system for post-trade activities (clearing and settlement, and depository)", acceptance of fixed-income assets as collateral, NoCD expansion; Phase 2 target 2027; a new central depository system for PDTC is in implementation [P] [^pse-asm-2026-president-report:28] [^pse-analyst-briefing-3m-2026:24-25]. Assets in the depository at end-June 2026: ₱6.08tn (equities ₱5.45tn = 41.9% of domestic listed market value) [P] [^pse-analyst-briefing-1h-2026:18].
- **Scale of PDTC's charges**: in FY2025, the first year PDSHC is consolidated, PSE reports "depository-related fees" of ₱714.36m (25.13% of group operating revenue), made up of securities-account fees and registry-maintenance fees charged by PDTC, and ₱447.96m of transaction fees from PDEx and PDTC combined within trading-related fees [P] [^pse-annual-report-2025:16]. [I] PDTC bills its participants (brokers, custodians), so depository charges reach you through your broker's or custodian's fee schedule; no PDTC tariff was read, so the per-security or per-transfer rates are unknown.
- **Who the participants are**: PDS's "Depository Participants as of 30 September 2026" page lists **192 equities depository participants** (stockbrokers, bank trust departments, insurers, pension funds such as SSS and GSIS, and the global custodian banks Citibank N.A., Deutsche Bank AG Manila Branch (clients' account), The Hongkong and Shanghai Banking Corporation (two accounts) and Standard Chartered Bank; SCCP itself is also a participant) and **63 fixed-income depository participants**; BNP Paribas, State Street and Northern Trust do not appear as direct participants [P-web] [^pds-web-depository-participants]. [I] Global custodians without a direct PDTC account reach the market through one of these sub-custodians (consistent with Clearstream's use of Standard Chartered).
- **Legal title and nominee**: securities lodged are immobilised by transferring legal title to PCD Nominee; PCD acts as depository and, through PCD Nominee, as nominee/trustee of participants, is not a fiduciary, and treats participants as beneficial owners of everything in their accounts; PCD Nominee is a wholly owned subsidiary with the single purpose of holding legal title, not beneficial ownership [P] [^pdtc-depository-rules-1997:8] [^pdtc-depository-rules-1997:27]. Securities are fungible; book-entry delivery is final and irrevocable and constitutes constructive delivery (Rules 1.7.7-1.7.9) [P] [^pdtc-depository-rules-1997:15]. (The PDS website still posts the November 1997 "Rules of the Philippine Central Depository" as "PDTC Depository Rules"; later amendments are not visible. The PDTC Registry Rules (April 2021) and the PDS list of foreign-currency securities accepted in NoCD (30 Sep 2026) are password-protected on the PDS bucket and could not be read [P-web] [^pds-web-rules].)
- **Account structure and nationality**: participants maintain Principal-Local/Foreign, Client-Local and Client-Foreign accounts; foreign clients' holdings must be segregated in a Client-Foreign sub-account; only the Settlement Sub-Account is eligible for transactions [P] [^pdtc-depository-rules-1997:14-15]; transfer agents reconcile PCNC balances separately for Filipino and foreign holdings daily by 12:00 noon next business day [P] [^pse-memo-2010-0203-lodgment:5] [^pse-memo-2010-0203-lodgment:9]. Clearstream: local and foreign investors cannot be commingled in one PDTC account (Rule 1.7) [S] [^clearstream-ph-investment-regulation].
- **Scripless vs certificated; no-jumbo rule**: as a condition of listing and trading every issuer must electronically lodge its registered securities with PDTC "without any jumbo or mother certificate" (CLDR Art. III Pt A Sec. 16, SRC Sec. 43), existing listed companies mandated from **1 July 2010**; PDTC conversion of existing jumbo certificates within a maximum of 30 business days; daily TA confirmation of PCNC balances [P] [^pse-memo-2010-0203-lodgment:1-2] [^pse-memo-2010-0203-lodgment:4-5]. Physical certificates remain possible (re-materialisation) [S] [^rbc-ph-market-profile].
- **Lodgement**: participant prepares a direct transfer to PCD Nominee (nationality indicated), enters a Lodgement Report, delivers transfer, report and certificates to the transfer agent (TA) with cancellation/issuance fees; TA verifies within 3 business days; defects corrected within 1 business day; online TAs confirm directly into PDTC [P] [^pse-memo-2010-0203-lodgment:7]. Defective lodgements may be uplifted and PDTC may buy in [P] [^pdtc-depository-rules-1997:28].
- **Upliftment**: participant enters an Uplift Request (kind, class, quantity, registrant details); shares are frozen/earmarked and ineligible for settlement; request goes to the TA per a weekly schedule; TA issues certificates; PDTC holds them until claimed [P] [^pse-memo-2010-0203-lodgment:8] [^pdtc-depository-rules-1997:32]. Elapsed time 2-4 weeks (RBC, Clearstream 1-3 weeks for the reverse conversion) [S] [^rbc-ph-market-profile] [^clearstream-ph-settlement-services].
- **Corporate-action role (Rule 3.2.4)**: PDTC advises record/payment dates; entitlements are computed from PCD Nominee holdings at record date as confirmed by the TA, rounded down; cash dividends are paid to participants after PDTC verifies good funds from the issuer at least one business day before payment date (net of tax); stock dividends credited after TA confirms listing/payment date; for rights offerings participants distribute subscription forms to beneficial owners and return them to the TA; PCD Nominee does not vote but executes proxies in favour of participants [P] [^pdtc-depository-rules-1997:31-32].
- **Transfer agents**: issuers must engage an SEC-registered TA (CLDR Art. III Pt A Secs. 6-7); TAs confirm validity of delivered certificates within two trading days; SRC IRR 36.4 requires TAs and registered clearing agencies to agree written procedures for lodgement, reconciliation, etc. [P] [^pse-listing-disclosure-rules:37] [^sec-2015-src-irr:117]. PASTRA is the TAs' self-regulatory association [S] [^clearstream-ph-market-infrastructure].
- **Beneficial-owner visibility and NoCD**: SEC directive of 6 Apr 2017: NoCD (sub-accounts under PDTC rules recording holdings at beneficial-owner level) is "mandatory for all DDS transactions" under the SEC-approved PSE DDS Rules (approved 10 Nov 2016, released 2 Dec 2016); interim: omnibus account with segregated coded sub-accounts; clients' consent within two months; sealed master list of names accessible to the SEC on request; numbered accounts barred (SRC Rule 52.1.6.7) [P, scanned] [^sec-dds-directive-2017:1-2]. PDTC DDS guidelines: broker-participants open segregated client sub-accounts under NoCD; only PSE-accredited eligible brokers [P] [^pdtc-dds-operating-guidelines-2017:2]; interim procedure for Del Monte DDS [P] [^pdtc-nocd-delmonte-dds-interim-2017:1]. NoCD for REITs: brokers keep client holdings in a segregated set-up under an omnibus broker account; each client gets a unique 11-character NoCD ID assigned by the broker (XXX = PSE broker code, R = REIT, 7 characters); two broker accounts ("omnibus with client" linking NoCD sub-accounts; "omnibus without client", flat at end-of-day); reports can go directly to clients; clients with custodians need no NoCD sub-account [P] [^pdtc-nocd-reit-faq:1-3] [^pdtc-nocd-reit-faq:6]. For ordinary peso shares NoCD is not required: PSE's 2025-2026 materials list "expansion of NoCD coverage to include all stock securities ... investors receive reports directly from the securities depository" as a planned item [P] [^pse-asm-2025-presidents-report:32] [^pse-analyst-briefing-1h-2026:31].
- **Disclosure to issuers/regulators**: beneficial ownership > 5% and >= 10% reporting (SRC Rules 18/23) and bank-share ultimate-owner disclosure by the corporate secretary for shares held under PCNC (BSP circulars) [S] [^rbc-ph-market-profile]; issuers file top-100 stockholder lists quarterly (CLDR 17.12) [P] [^pse-listing-disclosure-rules:156].
- **Foreign custodians**: a global custodian/ICSD holds through a Philippine sub-custodian that is a PDTC participant, e.g. Clearstream via Standard Chartered Bank Philippines in an omnibus sub-account (securities registered in PCNC's name and "held to the order of SCB FAO Clearstream Banking S.A."); Philippine law recognises the nominee concept, requires CSD segregation, finality of transfers in insolvency, with a legal opinion dated 11 Sep 2025 [S] [^clearstream-ph-market-link-guide]. Foreign ownership limit generally 40%; shares exceeding the limit cannot be registered [S] [^clearstream-ph-investment-regulation].

### Inferences
- [I] The Filipino/non-Filipino PCNC split is the depository-level mechanism that lets PDTC/TAs police foreign-ownership limits without beneficial-owner names.
- [I] Because PDTC treats the participant as owner, your legal protection depends on custodian/broker segregation and the participant's records, not on PDTC's records; NoCD is the exception for DDS/REIT and a likely future standard.
- [I] With PSE now majority owner of PDS, the "single post-trade system" is the main structural change to watch (new depository system plus integrated C&S); it may change cut-offs, interfaces and NoCD coverage in 2027.

### Execution implications
- Choose settlement route deliberately: via a local broker's own PDTC accounts (omnibus), via a global custodian's sub-custodian (off-exchange broker-to-custodian trade settled at PDTC), or, for DDS/REITs, NoCD-segregated sub-accounts.
- Foreign-flag instructions need the foreign nationality indicator end to end; mis-flagging (Filipino vs foreign) affects the PCNC split and foreign-room counts.
- Corporate-action rights (voting, subscription forms) pass from PCNC to the participant, then to you; expect custodian timelines to be shorter than company deadlines.
- Do not plan on upliftment; it freezes the stock for 2-4 weeks.

### Gaps
- PDTC's current rules/operating procedures (post-1997) and registry rules are not accessible; no PDTC fee schedule read.
- Beneficial-owner visibility for ordinary shares beyond participant level is not documented in a primary rule (inference only); NoCD expansion timetable not published.
- PCNC's holdings split numbers (Filipino vs foreign) not found.
- The new PDTC depository system's go-live date and its impact on cut-offs.

---

## 5. Corporate actions: ex-date, dividends, stock dividends, rights, price adjustment

### Takeaway
Since **24 Aug 2023 the PSE sets the ex-date at one trading day before the record date (RD-1)**; before that the convention was three trading days before the record date. Issuers must disclose a record date at least 10 trading days ahead and pay within 18 trading days of the record date; PDTC pays participants after receiving good funds. Rights offerings are non-tradable, subscribe-or-lapse with a record date at least 15 trading days after board approval. On ex-date the reference price becomes the exchange's adjusted closing price and, under Revised Trading Rules Art. IV Sec. 14(c), the Exchange cancels resting orders on cash/property-dividend ex-dates and whenever a corporate action adjusts the closing price.

### Cited findings
- **Ex-date convention**: PSE CN-2023-0031 (23 Jun 2023): "the determination of the ex-rights date for corporate actions beginning the target effective date of August 24, 2023 will be one (1) trading day prior to the disclosed record date"; ex-dates of previously disclosed actions were adjusted via amended disclosures [P] [^pse-cn-2023-0031-t2-settlement:1]. The prior rule (still printed in the January 2025 compilation of the Consolidated Listing and Disclosure Rules): "the Exchange shall automatically determine the ex-date ... three (3) Trading Days before the announced record date" [P] [^pse-listing-disclosure-rules:107]. Custodian guides confirm RD-1 under T+2 and entitlement by trade date vs ex-date (receive trades entitled only if trade date is before ex-date; deliver trades entitled if trade date is on or after ex-date) [S] [^clearstream-ph-securities-administration] [^rbc-ph-market-profile]. Conflict: Clearstream's page also still states "three working days before record date" (legacy text) [S] [^clearstream-ph-securities-administration]. Dates are announced via PSE EDGE disclosures (SEC-posted), and the Exchange broadcasts dividends/rights to trading terminals in start-of-day actions [P] [^pse-listing-disclosure-rules:102] [^pse-implementing-guidelines-trading-rules:5-6].
- **Empirical check on PSE EDGE (6 Oct 2026)**: EDGE's "Dividends and Rights" page loads its table from `POST /disclosureData/dividends_and_rights_info_list.ax?DividendsOrRights=Dividends|Rights` (form fields `pageNum`, `sortMode`, `dateSortType`, `cmpySortType`; works with plain HTTP, the page itself renders empty to scrapers). Dividend columns: Company, Type of Security, Type of Dividend, Dividend Rate, **Ex-Dividend Date, Record Date, Payment Date**, Circular Number; rights columns: Entitlement Ratio, Offer Price, Ex-Rights Date, Start/End of Offer Period. The list held 518 dividend records (502 with both dates; ex-dates 2025-2026 except a handful of older stale rows, latest ex-date 8 Feb 2027) and 12 rights records, all with dates "TBA" [P-web] [^pse-edge-dividends-rights]. In the 502 dated records the record date falls exactly **one weekday after the ex-date in 457 (91%)**; the other 45 show 2-5 weekdays, and the cases I checked coincide with public holidays or long weekends falling between the two dates (e.g. ex 11 Jun 2026 -> record 15 Jun after the 12 Jun holiday; ex 28 Aug -> 1 Sep 2026 after National Heroes Day on 31 Aug; ex 1 Apr -> 6 Apr 2026 over Holy Week; ex 29 Dec 2025 -> 2 Jan 2026 over the year-end holidays) so they are consistent with **one trading day** [I, no full holiday calendar loaded]; one record has a record date on a Sunday (data error). Median record-to-payment gap is 16 calendar days (about 11 weekdays; 54 of 478 exceed 18 weekdays, mostly holiday-affected or foreign-listed issuers, so compliance with the 18-trading-day limit cannot be tested without a trading calendar). The market-calendar page marks "Cash Ex-Date" and "Stock Ex-Date" events by day [P-web] [^pse-edge-market-calendar].
- **Cash dividends**: dividend declaration disclosed to the Exchange; record date set per SEC (and BSP where applicable) rules and **disclosed not less than 10 trading days before the record date** (CLDR Art. VII Secs. 6, 6.1); payment date set per SEC/BSP rules and **not more than 18 trading days from the record date**, with cash for PDTC-lodged shares remitted to PDTC within 18 trading days; single declaration for several dividends allowed if dates are explicit (Guidance Notes 16-19) [P] [^pse-listing-disclosure-rules:146-147]. PDTC credits participants once issuer funds are good (at least one business day before payment date) and participants distribute net of withholding tax [P] [^pdtc-depository-rules-1997:31]. Custodian guides: typical payment 30-40 calendar days after record date; cheques from issuers to the CSD need one day to clear; non-resident dividend tax 25% (15% with tax sparing/treaty relief) [S] [^clearstream-ph-asset-servicing] [^clearstream-ph-settlement-services] [^rbc-ph-market-profile].
- **Stock dividends**: credited through PDTC to participants after TA confirms the listing/payment date and a new jumbo certificate in PCNC's name; dividends on lodged shares "whether from unissued capital or resulting from an increase in capital stock" go to PDTC within 18 trading days of the record date **set by the SEC** [P] [^pdtc-depository-rules-1997:31] [^pse-listing-disclosure-rules:147]. Stock dividends are tax-exempt for non-residents [S] [^rbc-ph-market-profile].
- **Stock rights offerings** (CLDR Art. V Pt B): listing and SEC registration applications within 90 days of board approval, price range (floor/cap) disclosed at filing (Sec. 1); underwriter must take up shares not subscribed after the second round; unexercised rights first go to holders who exercised, and holders seeking extra shares must indicate and pay in round one (Secs. 3-4); **record date at least 15 trading days after approval** (Sec. 7); **offering period starts within 30 calendar days of the record date**, offering memorandum to the Exchange at least 7 calendar days earlier (Sec. 8); post-offer certification of subscription and new stockholder list within 15 days (Sec. 5); delay penalties include a 25% surcharge on listing fees plus 1% a day (Sec. 9) [P] [^pse-listing-disclosure-rules:106-108]. Mechanics at PDTC: participants forward subscription forms to beneficial owners and return them to the TA; new shares are lodgeable after full payment [P] [^pdtc-depository-rules-1997:31-32]. Custodian guides: rights are **not tradable** (exercise or lapse), subscription must be made at least two days (payment two business days) before the offer closes, new shares arrive 15-45 days (RBC) or 30-60 days after payment (Clearstream), pari passu with parent shares; rights events are offered to foreign holders "subject to availability" [S] [^clearstream-ph-securities-administration] [^rbc-ph-market-profile] [^clearstream-ph-asset-servicing]. No PSE rule on trading rights exists in the rulebooks read (inference of non-tradability from silence plus custodians' statements).
- **Reference-price adjustment on ex-date**: Reference Price = previous day's closing price, or the **Adjusted Closing Price (ACP)** "in the event of corporate actions that would result to an adjustment of the Closing Price", or last traded/last ACP if no trade; ACP is "the Closing Price of a Security with adjustments due to corporate events" (Revised Trading Rules Art. IV Sec. 6; Art. I Sec. 1) [P] [^pse-revised-trading-rules:20] [^pse-revised-trading-rules:8]. The static threshold is +/-50% of the reference price (including the Last Adjusted Closing Price, LACP); the opening reference price is the previous close or LACP; **the Exchange may cancel all active orders when corporate actions result in adjustment of the Closing Price** [P] [^pse-implementing-guidelines-trading-rules:10] [^pse-implementing-guidelines-trading-rules:16] [^pse-implementing-guidelines-trading-rules:18]. The Revised Trading Rules are mandatory where the Implementing Guidelines say "may": Art. IV Sec. 14(c) provides that "the Exchange shall cancel" as invalid (i) orders for a security "in the event of corporate actions resulting to an adjustment in the Closing Price", (ii) "orders on the ex-date for Securities with cash and/or property dividends" and (iii) orders that cross a board lot; I read the same wording on the scanned 2010 base text and in the SEC-approved amendment effective January 2012 [P] [^pse-revised-trading-rules:25] [^pse-tpa-2011-0110-amended-revised-trading-rules:4]. PSE can get the adjustment wrong: on 21 Dec 2023 it suspended UnionBank (UBP) for the whole day because "the stock's previous closing price was not adjusted to account for UBP's 27 percent stock dividends", and resumed on 22 Dec "with the adjusted share price" [P] [^pse-cn-2023-0074-ubp-trading-suspension:1]. For a dual-class declassification the adjusted price is "the closing price of the Class A shares or Class B shares, whichever is higher" on the last trading day before declassification, preceded by a two-trading-day suspension so that earlier trades settle "through the standard T+2 settlement cycle" (circular of 10 Sep 2026; worked example: last trading day Thu 10 Sep, suspension from Fri 11 Sep, T+2 settlement completed Mon 14 Sep, declassification, delisting and resumed trading Tue 15 Sep) [P] [^pse-cn-2026-0041-declassification-price-suspension:1-2]. PSE's index methodology confirms stock dividends, rights, splits and other actions adjust the previous day's last traded price and/or free-float factor [P] [^pse-index-policy-2024:14]. Exact ACP formulas (cash dividend deduction, stock-dividend ratio, rights TERP) were **not found** in the primary documents read. Data-feed hooks for the adjusted price: the securities static-data file carries `lacp` (last adjusted close price); the end-of-day quote file carries "Adjusted Previous" (previous close adjusted to corporate actions); the ITCH feed sends the (adjusted) reference price at start of day as an Add Order [A] message with order number and quantity zero (Total View) or a BBO [O] message with sizes set to 0x7FFFFFFFFFFFFFFF (Basic), and a manual intraday reference-price update generates the same messages [P] [^pse-securities-static-data-file:4] [^pse-quote-file-eod-spec-2014:2] [^pse-itch-equities-feed-spec-v2-3:27]. (Specs are the X-stream-era documents; the Nasdaq Eqlipse migration may change message formats.)
- **Clearing interplay**: SCCP's MTM reflects price changes from corporate actions (Rule 8.1.6) [P] [^sccp-clearing-house-rules-2018:44]; market claims: custodians can file claims from record date +1 for trades that settle across the record date or fail; "protection of rights" notices go out from ex-date +2 trading days [S] [^rbc-ph-market-profile].
- **Taxes touching flows**: stock transaction tax reduced from 0.6% to **0.1%** of gross selling price for exchange transactions from 1 Jul 2025 (RA 12214/CMEPA) [P] [^pse-cn-2025-0026-stt-decrease-advisory:1] [^pse-cn-2025-0028-cmepa-effectivity:1]; Clearstream reflects 0.1% [S] [^clearstream-ph-settlement-process]; RBC (Sep 2023) still shows 0.6% (stale) [S] [^rbc-ph-market-profile].

### Inferences
- [I] Under T+2 a buyer on the ex-date settles on RD+1 and so is not on the register at RD; a buyer on RD-2 settles on RD and is. Under T+3 the arithmetic ex-date would have been RD-2, so the old RD-3 convention carried a one-day safety buffer. Moving to RD-1 therefore shifted the ex-date two trading days closer to the record date (one day from the shorter cycle, one from dropping the buffer): shares now trade cum-entitlement until RD-2 instead of RD-4. Backtests and corporate-action calendars spanning 24 Aug 2023 need the convention switched at that date.
- [I] Under RTR Art. IV Sec. 14(c) resting orders in a stock with a cash or property dividend are cancelled on its ex-date, and all orders in a stock whose closing price is adjusted are cancelled; the rule text does not carve out multi-day validities (GTC/GTW/GTD), so assume they are purged too and that strategies must resubmit after the open's reference price is set.

### Execution implications
- Pull ex-dates, record dates and payment dates from the EDGE "Dividends and Rights" list (POST endpoint above) and the market calendar, and recompute entitlement with trade date < ex-date; do not use the legacy "3 trading days before record date" convention (still present in the PSE rulebook compilation).
- On ex-date, re-seed reference/limit prices from the ACP/LACP (static-data `lacp`, EOD "Adjusted Previous", SOD reference-price message), expect the Exchange to cancel resting orders (RTR Art. IV Sec. 14(c)), and avoid carrying GTC/resting orders across ex-dates; cross-check the published reference price against your own adjustment because PSE itself once opened a day with an unadjusted price (UBP, 21 Dec 2023).
- Rights cannot be sold: if the strategy cannot subscribe, avoid holding through the rights record date or accept dilution; check custodian availability and early internal deadlines (custodian cut-offs precede the company's).
- Withholding tax on dividends to non-residents is at source via PDTC participants: plan relief-at-source paperwork (treaty/tax sparing) with the custodian before pay date.
- Dividend proceeds arrive after the payment date plus bank/cheque clearing (days), not on pay date.

### Gaps
- PSE ACP formulas; whether the PSE changed the rights-offering "3 trading days" text after CN-2023-0031 (the January 2025 compilation was not amended).
- No standing machine-readable ex-date feed other than the EDGE list/calendar was found, and no trading-day calendar was loaded to prove RD-1 record by record; the live EDGE table is not archived here (only summarised).
- Stock-dividend record-date mechanics (SEC-set) and timelines for new shares not independently confirmed in primary sources.
- Rights tradability: no primary-rule confirmation.

---

## 6. Foreign investors: global-custodian settlement, SSI conventions, dollar securities

### Takeaway
Foreign institutions trade through a local broker (foreign-client flag), and the broker-to-custodian leg is a separate **off-exchange, gross, trade-by-trade settlement at PDTC**; the custodian chain therefore needs earlier cut-offs than SCCP's 12:00 SD deadline. Evidence here is almost entirely secondary (Clearstream, RBC); no HSBC/Citi/Deutsche/Standard Chartered market guides could be retrieved. Dollar-denominated securities (DDS) settle in USD through a designated USD settlement bank under SCCP rules, with NoCD mandatory.

### Cited findings
- **Settlement flow for foreign investors (Clearstream, updated 5 Jan 2026)**: matched trades go to SCCP; the broker-to-custodian leg settles at PDTC (BaNCS v6), not DVP in the SCCP sense: "movements of cash and securities for off-exchange transactions do not adhere to DVP principles", it is a two-step payment then delivery; securities to be sold must be in the broker's account by 12:00 SD; for purchases custodians pay brokers when securities arrive after the SCCP window; pre-matching facility exists; delivery trades are not on automatic release; the system is available 07:00-18:00 [S] [^clearstream-ph-settlement-process]. RBC: broker-to-custodian settlement is gross trade-for-trade; deadline strictly 12:00 noon for deliveries/receipts; pre-matching still by file exchange and phone; finality when both delivery and receipt orders are executed in PDTC; funds via RTGS or direct entry (some counterparties still use manager's cheques) [S] [^rbc-ph-market-profile].
- **Pre-matching and cut-offs at Clearstream (CBL), listed equities**: pre-matching manual via telephone starting 09:00 on SD-1; mismatches advised by 09:30 on SD; no amendment of a mismatched instruction - cancel and re-instruct by 10:00 on SD; no countervalue tolerance; no partial settlement; funding for third-party-bank cash must be credited by SD-1 14:30 PHT (MT210 is no guarantee); CBL deadline for receipt of valid instructions for PDTC-eligible securities is **03:35 CET/CEST on SD in both seasons, i.e. 09:35 PHT** (CBL's own expected settlement-result windows are 07:30-08:30 for deliveries and 10:30-11:30 for receipts on its summer-2026 table, i.e. 13:30-14:30 and 16:30-17:30 PHT by my conversion) [S] [^clearstream-ph-settlement-services] [^clearstream-ph-settlement-times]. Conversion PHT = CEST + 6h (summer 29 Mar-24 Oct 2026) or CET + 7h (winter 25 Oct 2025-27 Mar 2026) [I].
- **SSI conventions (Clearstream)**: counterparty delivers to "SCB (BIC SCBLPHMM) for account of CBL (BIC CEDELULL) in favour of [client name and account]" and receives from the same; cash via MT202 with `REC/RTGS` in :72: and beneficiary bank BIC in :58D:; manager's cheques not accepted; remittances to SCB with purpose "Securities Transaction" in :70:; CBL accepts only securities with a valid BSP registration (BSRD/BSP reference number) for receipts; turnaround/back-to-back processing available (POOL ID, SETR//TURN) [S] [^clearstream-ph-settlement-services] [^clearstream-ph-cash-services] [^clearstream-ph-investment-regulation].
- **BSP registration (FX Manual, "Updated as of May 2025"; Secs. 32.2 and 37 last amended by Circular 1192 of 11 Apr 2024; the live file on bsp.gov.ph fetched on 6 Oct 2026 is byte-identical to the archived copy, so this is still the current edition)**: Sec. 32.2: inward foreign investments need not be registered with the BSP unless repatriation of capital/earnings in pesos is to be funded with FX resources of authorised agent banks (AABs); a BSRD evidences registration, "except those covered by Section 37 for which a BSRD shall no longer be issued" [P] [^bsp-fx-manual-morfxt-2025-05:42]. Sec. 37: equity securities of residents listed on an onshore exchange (e.g., PSE), ETFs, PDRs and others are registered by a **registering AAB** (an FCDU bank designated by the investor) reporting to the BSP; inward FX must be converted to pesos via an AAB/AAB forex corp unless the investment must be funded in FX; the investor signs an "Authority to Disclose Information" covering all registered investments [P] [^bsp-fx-manual-morfxt-2025-05:46]. Clearstream's custodian view: BSP registration is needed for repatriation, BSRD replaced by a BSP reference number, and CBL accepts only registered securities for receipt [S] [^clearstream-ph-investment-regulation] [^clearstream-ph-settlement-services].
- **Same-day turnaround** allowed for foreign investors but constrained by cheque clearing; instructions on both legs must arrive together [S] [^clearstream-ph-settlement-process].
- **Give-up/Take-up (GUTU)**: under the Revised Trading Rules (2010) a trading participant may assign an outstanding client order to another TP for clearing and settlement; the Settling TP assumes liability by agreement but the Assigning TP stays solidarily liable; proprietary orders cannot be given up [P] [^pse-revised-trading-rules:27-28] [^pse-revised-trading-rules:9]. SCCP's give-up/take-up facility was proposed in January 2011 (SCCP Board 19 Jan 2011; PSE proposed rules 21 Jan 2011) and revised by the SCCP Board on 18 May 2011, per PSE Memo for Brokers 03-0511 of 24 May 2011 [S, paywalled summary] [^digest-ph-sccp-gutu-2011]; a word search of the posted 2018 SCCP Rules and OpProcs finds no give-up/take-up provision, so the operative mechanics are not in the published rulebook (inference), and current status is unverified.
- **Class A/B share declassification (delivery of the class bought)**: SEC Memorandum Circular No. 10, s. 2025 (PSE CN-2025-0035 of 11 Aug 2025; the SEC text attached to that circular has a blank number and date, the PSE circular names it MC 10 of 7 Aug 2025) repeals the 1973 rules that let "B" shares trade on the regular board and made buyers accept either "A" or "B" certificates, discontinues the Class A/B split of listed common shares, gives affected companies one year to amend their articles, and in the meantime obliges regular-board buyers to "accept the delivery of the specific class of shares that they have purchased and paid for"; its preamble says the split "has been a source of administrative inefficiencies for the trading participants and the SCCP"; Sec. 4 requires a foreign buyer whose trade breaches a foreign-ownership limit, through its broker, to dispose of the excess at the prevailing market price immediately (same day if found during trading hours, otherwise at the next open) and return the proceeds [P] [^pse-cn-2025-0035-sec-declassification-mandate:1-3]. PSE CN-2025-0036 (15 Aug 2025): the circular took effect on 9 Aug 2025, affected companies have until 9 Aug 2026 to amend their articles, and the buyer-receives-the-class-bought rule applies from 11 Aug 2025 [P] [^pse-cn-2025-0036-declassification-effectivity:1]. Per-issuer completion is by PSE circular (price adjustment and two-day suspension before delisting; see 5) [P] [^pse-cn-2026-0041-declassification-price-suspension:1-2]. [I] For a foreign holder this removes one source of delivery mismatches for the listed names still dual-class, but the foreign-ownership accounting that follows the PCD Nominee (Filipino/foreign) split and the FOL-breach unwind (Sec. 4 of the SEC circular) remain.
- **Dollar-denominated securities (DDS)**: PSE DDS Rules (SEC-approved 10 Nov 2016) Part D: settlement in USD; TPs need an FCDU account and a separate USD cash settlement account at the SCCP-designated settlement bank; USD cash list to the bank; funds must be good cleared funds by the deadline (same-day USD notes may not clear); no CCCS cash instruction needed (cash handled outside CCCS under the old system); same fails management; CTGF contributions paid in pesos using the PDEx closing USD rate; separate USD MTM collateral (cash USD, or early delivery up to settlement date), USD cash collateral deposit accounts [P] [^pse-dds-rules:8-10]. SCCP's Dec 2016 TP training: settlement bank BDO, deadline 12:00 NN of T+3 then, USD fund transfers via PDDTS the day before settlement, penalties in PHP at the PDEx close [P] [^sccp-dds-clearing-settlement-2016:3-5] [^sccp-dds-clearing-settlement-2016:11-14]. The new C&S System handles PHP and USD settlement and collateral (four PHP and four USD collateral accounts per CM) [P] [^sccp-cs-quick-guide:5] [^sccp-memo-01-0222-collateral-accounts-pdtc:2]; no separate DDS cycle announcement was found, so I infer DDS follow the T+2 cycle with the same 12:00 deadline [I]. SCCP's 2016 deck also covers BSP FX rule changes (Circular 925) letting residents buy FX through the banking system, and PSE's FY2016 report records the BSP Monetary Board approval (8 Sep 2016) of FX amendments including purchases to fund SCCP settlement fails [P] [^sccp-dds-clearing-settlement-2016:6-10] [^pse-annual-report-2016:72]. NoCD mandatory for DDS [P] [^sec-dds-directive-2017:1].
- **FX/price conventions**: peso settlement; FX typically arranged on T+1 by the investor with the custodian (standing instructions or embedded FX in MT54x); local exchange rate conventions not set by SCCP [S] [^rbc-ph-market-profile].

### Inferences
- [I] For a foreign hedge fund, effective cut-offs are: instruct and pre-match by SD-1 (09:00 PHT start), fund PHP by SD-1 14:30 PHT with CBL-type custodians, valid instruction at 09:35 PHT on SD, market deadline 12:00 SD; SCCP-side broker-to-broker settlement then finishes about 12:30-13:30.
- [I] The custodian segment is where most foreign-flow fails will originate (manual pre-matching, cut-offs, BSP registration), not SCCP.

### Execution implications
- Standing SSIs and FX instructions with every custodian; confirm each broker's PDTC participant IDs; use the allocation/confirmation at trade date close so custodian matching can start 09:00 SD-1.
- Avoid late partial fills with different counter-values: no tolerance, no partial settlement at CBL.
- Using a clearing broker via give-up/take-up can centralise settlement but check with the exchange rule status and your broker's agreement.
- DDS: keep USD liquidity at the designated settlement bank the day before SD; accept NoCD consent/KYC steps.
- FOL-capped names: a buy that breaches the foreign ownership limit is unwound by the foreign buyer's broker at market the same day or at the next open (SEC MC 10-2025 Sec. 4), so FOL headroom checks belong before order entry, not at settlement.

### Gaps
- No HSBC, Citi, Deutsche Bank, Standard Chartered, BNP or J.P. Morgan Philippines market guides retrieved (Euroclear/SC URLs returned 403; others not found); other custodians' SSI formats and cut-offs are unknown.
- PDTC pre-matching and instruction cut-offs from PDTC primary documents not accessible.
- Whether DDS beyond Del Monte Pacific are currently listed (PDS list encrypted).
- Primary confirmation of GUTU rules in force.

---

## Source catalog

```yaml
- slug: sccp-clearing-house-rules-2018
  title: "Revised Clearinghouse Rules of the Securities Clearing Corporation of the Philippines (approved by SEC, revised 13 March 2018)"
  publisher: Securities Clearing Corporation of the Philippines (SCCP)
  type: pdf
  canonical_url: https://sccp.com.ph/SCCP/resources/files/rules/SCCP_Revised_Rules_-_Approved_by_the_SEC_031318.pdf
  local_path: pdfs/sccp-clearing-house-rules-2018.pdf
  edition: in-force
  amended_through: 2018-03-13
  note: "Latest consolidated Rules posted by SCCP (HTTP Last-Modified 27 Jul 2018; live file size in Oct 2026 equals the archived copy, 986,937 bytes) but still T+3 text; amended in part by memos of 2022-2025 (see 1.5). Rule 5.2 amended eff. 1 Aug 2018. Physical page numbers equal printed folios."
- slug: sccp-clearing-house-operating-procedures-2018
  title: "Revised Clearinghouse Operating Procedures of SCCP (approved by SEC, revised 13 March 2018)"
  publisher: Securities Clearing Corporation of the Philippines (SCCP)
  type: pdf
  canonical_url: https://sccp.com.ph/SCCP/resources/files/rules/SCCP_Revised_OpProcs_-_Approved_by_the_SEC_031318.pdf
  local_path: pdfs/sccp-clearing-house-operating-procedures-2018.pdf
  edition: in-force
  amended_through: 2018-03-13
  note: "Posted OpProcs still say rolling T+3; section numbers have since been renumbered by later amendments (T+2 memo cites 3.7, 3.8.3, 3.11.6). Obtained from Wayback capture of 10 Feb 2026 of the live file."
- slug: pse-sccp-revised-rules
  title: "Revised Clearinghouse Rules of the Securities Clearing Corporation of the Philippines (approved by SEC, revised 21 February 2013; 71 pp)"
  publisher: Securities Clearing Corporation of the Philippines (SCCP)
  type: pdf
  canonical_url: http://www.sccp.com.ph/resources/files/rules/SCCP_Revised_Rules.pdf
  local_path: pdfs/pse-sccp-revised-rules.pdf
  edition: superseded
  amended_through: 2013-02-21
  note: "Slug already listed in another researcher's catalog but the file was absent from kb/pdfs; re-archived by me from the Wayback Machine capture of 18 Jul 2016 of the URL shown (PDF created 26 Mar 2013; cover: revised 21 Feb 2013; individual rules show SEC approvals of 28 Jun 2012 and 21 Feb 2013). Used only to show Rule 5.2 before 2018 (no return of cash contributions, p.35) and the Rule 6.2.6 buy-in price wording (p.39)."
- slug: sccp-cs-quick-guide
  title: "SCCP New Clearing & Settlement Quick Guide, v1.0"
  publisher: Securities Clearing Corporation of the Philippines (SCCP)
  type: pdf
  canonical_url: https://sccp.com.ph/SCCP/resources/files/rules/New_CS_System_Quick_Guide.pdf
  local_path: pdfs/sccp-cs-quick-guide.pdf
  edition: in-force
  amended_through: 2023-03-31
  note: "Release date March 2023 (file created 11 May 2023; server Last-Modified 24 Sep 2024). Source of forecast/final netting windows, account types FC/FH/LC/LH, early delivery, collateral screens."
- slug: sccp-memo-03-1121-proposed-amendments
  title: "SCCP Memo 03-1121 (24 Nov 2021): Consultation Paper and draft 2022 Revised Clearinghouse Rules"
  publisher: SCCP
  type: pdf
  canonical_url: https://sccp.com.ph/resources/files/memos/2021/03-1121%20Proposed%20Amendments%20to%20the%20SCCP%20Rules.pdf
  local_path: pdfs/sccp-memo-03-1121-proposed-amendments.pdf
  edition: historical
  amended_through: 2021-11-24
  note: "Consultation draft; later approved memos use its numbering but adoption of each provision (CTGF order of application, block-sale guarantee, fails detail) is unverified."
- slug: sccp-memo-01-0222-collateral-accounts-pdtc
  title: "SCCP Memo 01-0222 (8 Feb 2022): Creation of Collateral Accounts in PDTC eCS for the new C&S System"
  publisher: SCCP
  type: pdf
  canonical_url: https://sccp.com.ph/resources/files/memos/2022/01-0222%20Creation%20of%20Collateral%20Accounts%20in%20PDTC%20eCS.pdf
  local_path: pdfs/sccp-memo-01-0222-collateral-accounts-pdtc.pdf
  edition: n/a
  amended_through: 2022-02-08
  note: "Four PHP and four USD securities collateral accounts per CM."
- slug: sccp-memo-02-0222-delayed-settlement
  title: "SCCP Memo 02-0222 (10 Feb 2022): Delayed settlement processing due to PhilPaSSplus technical problem"
  publisher: SCCP
  type: pdf
  canonical_url: https://sccp.com.ph/resources/files/memos/2022/02-0222%20Delayed%20Settlement%20Processing.pdf
  local_path: pdfs/sccp-memo-02-0222-delayed-settlement.pdf
  edition: n/a
  amended_through: 2022-02-10
  note: "Incident record."
- slug: sccp-memo-04-0422-readjustment-apr19-2022
  title: "SCCP Memo 04-0422 (20 Apr 2022): Readjustment of settlement date of trades due 19 April 2022"
  publisher: SCCP
  type: pdf
  canonical_url: https://sccp.com.ph/resources/files/memos/2022/04-0422%20Readjustment%20of%20Settlement%20Date%20of%20Trades%20Due%20for%20Settlement%20on%20April%2019,%202022.pdf
  local_path: pdfs/sccp-memo-04-0422-readjustment-apr19-2022.pdf
  edition: n/a
  amended_through: 2022-04-20
  note: "PDTC end-of-day processing delay; settlement moved to 21 Apr (superseded the 20 Apr plan)."
- slug: sccp-memo-06-0422-ongoing-settlement
  title: "SCCP Memo 06-0422 (21 Apr 2022): Ongoing settlement of trades originally due 19 April 2022"
  publisher: SCCP
  type: pdf
  canonical_url: https://sccp.com.ph/resources/files/memos/2022/06-0422%20-%20Ongoing%20Settlement%20of%20Trades%20Originally%20Due%20for%20Settlement%20April%2019%202022%20(clean).pdf
  local_path: pdfs/sccp-memo-06-0422-ongoing-settlement.pdf
  edition: n/a
  amended_through: 2022-04-21
  note: "Incident record."
- slug: sccp-memo-02-0223-collateral-haircut-rates
  title: "SCCP Memo 02-0223 (10 Feb 2023): New Eligible Securities Collateral and Haircut Rates"
  publisher: SCCP
  type: pdf
  canonical_url: https://sccp.com.ph/resources/files/memos/2023/02-0223%20New%20Eligible%20Securities%20Collateral%20and%20Haircut%20Rates.pdf
  local_path: pdfs/sccp-memo-02-0223-collateral-haircut-rates.pdf
  edition: in-force
  amended_through: 2023-02-10
  note: "SEC approval 13 Dec 2022 of Rule 8.1.8; effective 20 Feb 2023; 25%/35% haircuts."
- slug: sccp-memo-03-0623-client-securities-prohibition
  title: "SCCP Memo 03-0623 (22 Jun 2023): Proposed Rule 2.3.5, prohibition on use of other clients' shares"
  publisher: SCCP
  type: pdf
  canonical_url: https://sccp.com.ph/resources/files/memos/2023/03-0623%20Public%20Consultation%20Notice%20on%20Unauthorized%20Use%20of%20Client%20Securities.pdf
  local_path: pdfs/sccp-memo-03-0623-client-securities-prohibition.pdf
  edition: superseded
  amended_through: 2023-06-22
  note: "Consultation; approved text in memo 07-0823."
- slug: sccp-memo-01-0723-philpass-suspension
  title: "SCCP Memo 01-0723 (23 Jul 2023): Revision of settlement dates due to suspension of PhilPaSS operations"
  publisher: SCCP
  type: pdf
  canonical_url: https://sccp.com.ph/resources/files/memos/2023/01-0723%20AdjustmentOfSettlementDates%20-%20No%20Settlement%20(July%2024%202023).pdf
  local_path: pdfs/sccp-memo-01-0723-philpass-suspension.pdf
  edition: n/a
  amended_through: 2023-07-23
  note: "Worked example of double-settlement day (Batch 1 11:00, Batch 2 14:00)."
- slug: sccp-memo-02-0723-transition-period
  title: "SCCP Memo 02-0723 (25 Jul 2023): Two-week transition period of extended settlement deadlines"
  publisher: SCCP
  type: pdf
  canonical_url: https://sccp.com.ph/resources/files/memos/2023/02-0723%20Two-Week%20Transition%20Period%20of%20Extended%20Settlement%20Deadlines.pdf
  local_path: pdfs/sccp-memo-02-0723-transition-period.pdf
  edition: historical
  amended_through: 2023-07-25
  note: "Transition ended 11 Sep 2023."
- slug: sccp-memo-04-0823-t2-go-live
  title: "SCCP Memo 04-0823 (11 Aug 2023): Go-live of migration to T+2 on 24 Aug 2023"
  publisher: SCCP
  type: pdf
  canonical_url: https://sccp.com.ph/resources/files/memos/2023/04-0823%20Approval%20of%20the%20August%2024%202023%20T+2%20Launch%20Date.pdf
  local_path: pdfs/sccp-memo-04-0823-t2-go-live.pdf
  edition: n/a
  amended_through: 2023-08-11
  note: "SEC En Banc approval 10 Aug 2023."
- slug: sccp-memo-05-0823-settlement-dates-t2-heroes-day
  title: "SCCP Memo 05-0823 (11 Aug 2023): Revision of settlement dates (T+2 SEC approval; National Heroes Day)"
  publisher: SCCP
  type: pdf
  canonical_url: https://sccp.com.ph/resources/files/memos/2023/05-0823%20AdjustmentOfSettlementDates%20-National%20Heroes%20and%20T+2.pdf
  local_path: pdfs/sccp-memo-05-0823-settlement-dates-t2-heroes-day.pdf
  edition: n/a
  amended_through: 2023-08-11
  note: "Settlement schedule for 23-25 Aug 2023."
- slug: sccp-memo-06-0823-sec-approval-t2-amendments
  title: "SCCP Memo 06-0823 (18 Aug 2023): SEC approval of T+2-related amendments to the SCCP Rules and Operating Procedures (redline)"
  publisher: SCCP
  type: pdf
  canonical_url: https://sccp.com.ph/resources/files/memos/2023/06-0823%20Announcement%20of%20SEC%20Approval%20of%20T+2-Related%20Amendments%20to%20the%20SCCP%20Rules%20and%20Operating%20Procedures.pdf
  local_path: pdfs/sccp-memo-06-0823-sec-approval-t2-amendments.pdf
  edition: in-force
  amended_through: 2023-08-18
  note: "Memo dated 18 Aug 2023; amendments effective on T+2 implementation 24 Aug 2023. Redline: strikethrough = deleted, bold-underline = inserted (text extraction interleaves both; read visually)."
- slug: sccp-memo-07-0823-sec-approved-amendments
  title: "SCCP Memo 07-0823 (23 Aug 2023): SEC-approved amendments (Rule 2.3.5, buy-in/sell-out, collateral, holidays, multiple settlement)"
  publisher: SCCP
  type: pdf
  canonical_url: https://sccp.com.ph/resources/files/memos/2023/07-0823%20SEC%20Approval%20of%20Amendments%20to%20the%20SCCP%20Rules%20and%20Operating%20Procedures.pdf
  local_path: pdfs/sccp-memo-07-0823-sec-approved-amendments.pdf
  edition: in-force
  amended_through: 2023-08-23
  note: "States amendments are 'now in force and effect'."
- slug: sccp-memo-08-0823-early-batch-run-proposal
  title: "SCCP Memo 08-0823 (30 Aug 2023): Proposed amendment on early commencement of batch run"
  publisher: SCCP
  type: pdf
  canonical_url: https://sccp.com.ph/resources/files/memos/2023/08-0823%20Public%20Consultation%20Notice%20on%20Early%20Commencement%20of%20Batch%20Run.pdf
  local_path: pdfs/sccp-memo-08-0823-early-batch-run-proposal.pdf
  edition: superseded
  amended_through: 2023-08-30
  note: "Consultation; adopted via memo 01-0324."
- slug: sccp-memo-01-0324-early-batch-run-effectivity
  title: "SCCP Memo 01-0324 (5 Mar 2024): Effectivity of OP amendment on early commencement of batch run"
  publisher: SCCP
  type: pdf
  canonical_url: https://sccp.com.ph/resources/files/memos/2024/01-0324%20Announcement%20of%20SEC%20Approval%20of%20Early%20Batch%20Run.pdf
  local_path: pdfs/sccp-memo-01-0324-early-batch-run-effectivity.pdf
  edition: in-force
  amended_through: 2024-03-05
  note: "SEC approved 9 Jan 2024; 10-minute email notice condition."
- slug: sccp-memo-03-0324-clearing-member-suspension
  title: "SCCP Memo 03-0324 (22 Mar 2024): Suspension of Clearing Member (EquitiWorld Securities)"
  publisher: SCCP
  type: pdf
  canonical_url: https://sccp.com.ph/resources/files/memos/2024/03-0324%20Announcement%20of%20EquitiWorld%20Suspension.pdf
  local_path: pdfs/sccp-memo-03-0324-clearing-member-suspension.pdf
  edition: n/a
  amended_through: 2024-03-22
  note: "Enforcement example under Rule 2.5.1(a)/(b)."
- slug: sccp-memo-01-0524-sec-recommended-revisions
  title: "SCCP Memo 01-0524 (8 May 2024): Proposed amendments recommended by the SEC (Rules 3.4, 5.1.4(3), 6.2.8, 7.6)"
  publisher: SCCP
  type: pdf
  canonical_url: https://sccp.com.ph/resources/files/memos/2024/01-0524%20Public%20Consultation%20Notice%20on%20SEC-Recommended%20Revisions%20to%20the%20SCCP%20Rules.pdf
  local_path: pdfs/sccp-memo-01-0524-sec-recommended-revisions.pdf
  edition: superseded
  amended_through: 2024-05-08
  note: "Consultation text of Rule 7.6 and Annex 11; approved 21 Jan 2025."
- slug: sccp-memo-02-0624-ctgf-refund-proposal
  title: "SCCP Memo 02-0624 (26 Jun 2024): Proposed amendments on CTGF refund requirements"
  publisher: SCCP
  type: pdf
  canonical_url: https://sccp.com.ph/resources/files/memos/2024/02-0624%20Proposed%20Amendments%20to%20the%20SCCP%20Rules%20on%20the%20Requirements%20for%20a%20Refund%20of%20CTGF%20Contributions.pdf
  local_path: pdfs/sccp-memo-02-0624-ctgf-refund-proposal.pdf
  edition: superseded
  amended_through: 2024-06-26
  note: "Consultation; approved 8 Jul 2025."
- slug: sccp-memo-02-0125-sec-approval-rules-3-4-5-1-4-6-2-8-7-6
  title: "SCCP Memo 02-0125 (21 Jan 2025): SEC approval of amendments to Rules 3.4, 5.1.4, 6.2.8 and 7.6 (redline)"
  publisher: SCCP
  type: pdf
  canonical_url: https://sccp.com.ph/SCCP/resources/files/memos/2025/02-0125%20Announcement%20of%20SEC%20Approval%20of%20Amendments%20to%20the%20SCCP%20Rules%20(Rules%203.4_%205.1.4_%206.2.8%20and%207.6).pdf
  local_path: pdfs/sccp-memo-02-0125-sec-approval-rules-3-4-5-1-4-6-2-8-7-6.pdf
  edition: in-force
  amended_through: 2025-01-21
  note: "Effective immediately under Rule 1.4.3; pp.1-2 show Rule 3.4/Annex 11, 5.1.4(3) and 6.2.8; p.3 shows the full new Rule 7.6 text in a boxed block above the signature (the PDF text layer places it after the signature)."
- slug: sccp-memo-01-0725-ctgf-refund-sec-approval
  title: "SCCP Memo 01-0725 (8 Jul 2025): SEC approval of amendments on refund of CTGF contributions"
  publisher: SCCP
  type: pdf
  canonical_url: https://sccp.com.ph/SCCP/resources/files/memos/2025/01-0725%20SEC%20Approval%20of%20Amendments%20Related%20to%20the%20Refund%20of%20CTGF%20Contributions.pdf
  local_path: pdfs/sccp-memo-01-0725-ctgf-refund-sec-approval.pdf
  edition: in-force
  amended_through: 2025-07-08
  note: "Latest rule-amendment memo in the SCCP index as of 11 Sep 2026."
- slug: sccp-memo-01-0126-eligible-collateral-list
  title: "SCCP Memo 01-0126 (28 Jan 2026): List of Securities Eligible as Collateral (effective 2 Feb 2026)"
  publisher: SCCP
  type: pdf
  canonical_url: https://sccp.com.ph/SCCP/resources/files/memos/2026/01-0126%20List%20of%20Securities%20Eligible%20as%20Collateral.pdf
  local_path: pdfs/sccp-memo-01-0126-eligible-collateral-list.pdf
  edition: superseded
  amended_through: 2026-01-28
  note: "Superseded by memo 01-0726 (28 Jul 2026, not archived)."
- slug: sccp-memo-01-0812-sec-approval-fails-management
  title: "SCCP Memo 01-0812 (2 Aug 2012): SEC approval of revisions to the Fails Management System rules and operating procedures"
  publisher: SCCP
  type: pdf
  canonical_url: https://sccp.com.ph/SCCP/resources/files/memos/2012/01-0812%20SEC%20Approval%20for%20%20Revisions%20to%20The%20Fails%20Mgmt%20%20Rules%20and%20Op%20Procs.pdf
  local_path: pdfs/sccp-memo-01-0812-sec-approval-fails-management.pdf
  edition: in-force
  amended_through: 2012-07-23
  note: "SEC approval 28 Jun 2012; effective 23 Jul 2012; introduced Rule 6.2.7 and the two-tier penalty. Scanned OCR text."
- slug: sccp-memo-04-0812-settlement-restrictions-proposal
  title: "SCCP Memo 04-0812 (31 Aug 2012): New Rules and Operating Procedures on Settlement Restrictions (proposed Rule 7.6)"
  publisher: SCCP
  type: pdf
  canonical_url: https://sccp.com.ph/SCCP/resources/files/memos/2012/04-0812%20Rules%20and%20Operating%20Procedures%20for%20Settlement%20Restrictions.pdf
  local_path: pdfs/sccp-memo-04-0812-settlement-restrictions-proposal.pdf
  edition: historical
  amended_through: 2012-08-31
  note: "Consultation draft; not found in the 2018 consolidated Rules."
- slug: sccp-memo-02-0413-settlement-restrictions-revisions
  title: "SCCP Memo 02-0413 (24 Apr 2013): Revisions to the Rules and Operating Procedures on Settlement Restrictions and new penalty table"
  publisher: SCCP
  type: pdf
  canonical_url: https://sccp.com.ph/SCCP/resources/files/memos/2013/02-0413%20%20Revisions%20to%20the%20Rules%20and%20Operating%20Procedures%20on%20Settlement%20Restrictions.pdf
  local_path: pdfs/sccp-memo-02-0413-settlement-restrictions-revisions.pdf
  edition: historical
  amended_through: 2013-04-24
  note: "Consultation until 10 May 2013 before SEC submission; adoption unverified."
- slug: sccp-memo-03-0112-early-delivery-lifting
  title: "SCCP Memo 03-0112 (19 Jan 2012): Lifting of the imposition of T+1 early delivery on identified securities (ACE, FPI, MVC, PHES, WIN, WPI)"
  publisher: SCCP
  type: pdf
  canonical_url: https://sccp.com.ph/SCCP/resources/files/memos/2012/03-0112%20Lifting%20of%20Early%20Delivery%20of%20Identified%20Securities.pdf
  local_path: pdfs/sccp-memo-03-0112-early-delivery-lifting.pdf
  edition: historical
  amended_through: 2012-01-19
  note: "Precedent for security-specific early-delivery restrictions; references memo 01-0209 (5 Feb 2009). Scanned OCR text."
- slug: digest-ph-sccp-gutu-2011
  title: "digest.ph: Update on the SCCP Give-up/Take-up Facility (PSE Memo for Brokers No. 03-0511, 24 May 2011)"
  publisher: digest.ph (summary of a PSE memorandum)
  type: web
  canonical_url: https://www.digest.ph/corporate/update-on-the-sccp-give-up-take-up-facility
  local_path: null
  edition: historical
  amended_through: 2011-05-24
  note: "Secondary and truncated (login wall); only the dates were readable."
- slug: sccp-dds-clearing-settlement-2016
  title: "Clearing and Settlement of Dollar Denominated Securities (TP training, December 2016)"
  publisher: SCCP via PSE
  type: pdf
  canonical_url: https://documents.pse.com.ph/wp-content/uploads/sites/15/2021/01/DDS-Presentation-Clearing-and-Settlement.pdf
  local_path: pdfs/sccp-dds-clearing-settlement-2016.pdf
  edition: historical
  amended_through: 2016-12-31
  note: "Pre-T+2/new-system DDS settlement details (BDO, T+3 12:00)."
- slug: pse-cn-2023-0031-t2-settlement
  title: "PSE CN-2023-0031 (23 Jun 2023): Migration to the T+2 settlement cycle (with SCCP Memo 01-0623)"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: https://documents.pse.com.ph/CircularOPSPDF/CN-2023-0031.pdf
  local_path: pdfs/pse-cn-2023-0031-t2-settlement.pdf
  edition: in-force
  amended_through: 2023-06-23
  note: "Source of the RD-1 ex-date rule from 24 Aug 2023."
- slug: pse-memo-2010-0203-lodgment
  title: "PSE Memo 2010-0203 (4 May 2010): Amended rule on lodgment of securities (no-jumbo) with PDTC procedures"
  publisher: The Philippine Stock Exchange, Inc. / PDS Group
  type: pdf
  canonical_url: https://documents.pse.com.ph/wp-content/uploads/sites/15/2022/08/Supplemental-Rule-4-Memo-No.-2010-0203-1.pdf
  local_path: pdfs/pse-memo-2010-0203-lodgment.pdf
  edition: in-force
  amended_through: 2010-05-04
  note: "Supplemental Rule 4; PDTC annexes dated Jul/Sep 2009; scanned OCR text."
- slug: pdtc-depository-rules-1997
  title: "The Rules of the Philippine Central Depository (November 1997), posted as 'PDTC Depository Rules'"
  publisher: Philippine Dealing System Group / PDTC
  type: pdf
  canonical_url: https://pdswordpressbucket.s3.ap-southeast-1.amazonaws.com/wp-content/uploads/2025/03/PDTC-Depository-Rules.pdf
  local_path: pdfs/pdtc-depository-rules-1997.pdf
  edition: in-force
  amended_through: 1997-11-30
  note: "Posted version carries the 1997 date; later amendments not visible. Treat as the latest publicly posted PDTC rule text."
- slug: pdtc-dds-operating-guidelines-2017
  title: "Operating Guidelines and Procedures for Depository Participants holding Dollar Denominated Securities in the Depository (4 April 2017)"
  publisher: PDTC
  type: pdf
  canonical_url: https://pdswordpressbucket.s3.ap-southeast-1.amazonaws.com/wp-content/uploads/2025/09/PDTC-DDS-Operating-Guidelines-Procedures-as-of-04-April-2017.pdf
  local_path: pdfs/pdtc-dds-operating-guidelines-2017.pdf
  edition: in-force
  amended_through: 2017-04-04
  note: "NoCD for DDS."
- slug: sec-dds-directive-2017
  title: "SEC Markets and Securities Regulation Department: Directives on Dollar Denominated Securities (6 April 2017)"
  publisher: Securities and Exchange Commission (Philippines)
  type: pdf
  canonical_url: https://pdswordpressbucket.s3.ap-southeast-1.amazonaws.com/wp-content/uploads/2025/09/SEC-DDS-Directive.pdf
  local_path: pdfs/sec-dds-directive-2017.pdf
  edition: in-force
  amended_through: 2017-04-06
  note: "Scanned image only (read by extracting the embedded JPEGs)."
- slug: pdtc-nocd-reit-faq
  title: "Name-On-Central-Depository (NoCD) Facility for REIT: Frequently Asked Questions"
  publisher: PDS Group / PDTC
  type: pdf
  canonical_url: https://pdswordpressbucket.s3.ap-southeast-1.amazonaws.com/wp-content/uploads/2025/09/PDTC-NoCD-for-REIT-FAQ_final.pdf
  local_path: pdfs/pdtc-nocd-reit-faq.pdf
  edition: in-force
  amended_through: undated
  note: "Uploaded to the PDS site Sep 2025."
- slug: pdtc-nocd-delmonte-dds-interim-2017
  title: "Proposed operating procedures on the interim implementation of NoCD for Del Monte Pacific DDS (5 April 2017)"
  publisher: PDTC
  type: pdf
  canonical_url: https://pdswordpressbucket.s3.ap-southeast-1.amazonaws.com/wp-content/uploads/2025/09/Operating-Procedures-on-the-Interim-Implementation-of-NoCD-for-Del-Monte-DDS-as-of-05-April-2017.pdf
  local_path: pdfs/pdtc-nocd-delmonte-dds-interim-2017.pdf
  edition: historical
  amended_through: 2017-04-05
  note: "Interim, two-month consent window."
- slug: pse-listing-disclosure-rules
  title: "PSE Consolidated Listing and Disclosure Rules (published as of January 2025)"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: https://documents.pse.com.ph/wp-content/uploads/sites/15/2025/01/Consolidated-Listing-and-Disclosure-Rules-Updated-011025.pdf
  local_path: pdfs/pse-listing-disclosure-rules.pdf
  edition: in-force
  amended_through: 2025-01-31
  note: "Contains the stale 3-trading-day ex-date note (p.107) superseded by CN-2023-0031 for actions from 24 Aug 2023."
- slug: pse-revised-trading-rules
  title: "PSE Revised Trading Rules (SEC-approved; PSE memo 2010-0275, 8 Jun 2010)"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: https://documents.pse.com.ph/wp-content/uploads/sites/15/2021/04/Revised-Trading-Rules.pdf
  local_path: pdfs/pse-revised-trading-rules.pdf
  edition: in-force
  amended_through: 2010-06-08
  note: "Scanned images; later amendments (e.g. 2011) exist in other slugs. Pages cited: 8-9 (definitions), 20 (reference price), 27-28 (give-up/take-up)."
- slug: pse-implementing-guidelines-trading-rules
  title: "Implementing Guidelines of the Revised Trading Rules (PSE memo 2010-0340, 22 Jul 2010)"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: https://documents.pse.com.ph/wp-content/uploads/sites/15/2021/04/Implementing-Guidelines-of-the-Revised-Trading-Rules.pdf
  local_path: pdfs/pse-implementing-guidelines-trading-rules.pdf
  edition: in-force
  amended_through: 2010-07-22
  note: "LACP, static threshold, order cancellation on corporate actions."
- slug: pse-annual-report-2014
  title: "PSE Annual Report 2014 (with consolidated FS)"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: https://ir.pse.com.ph/wp-content/uploads/sites/4/2020/04/2014-PSE-Annual-Report.pdf
  local_path: pdfs/pse-annual-report-2014.pdf
  edition: historical
  amended_through: 2014-12-31
  note: "CTGF size 2013-2014 (p.130)."
- slug: pse-annual-report-2015
  title: "PSE Annual Report 2015"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: https://ir.pse.com.ph/wp-content/uploads/sites/4/2020/04/2015-PSE-Annual-Report.pdf
  local_path: pdfs/pse-annual-report-2015.pdf
  edition: historical
  amended_through: 2015-12-31
  note: "SCCP settlement compliance and release-time statistics (p.66)."
- slug: pse-annual-report-2016
  title: "PSE Annual Report 2016"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: https://ir.pse.com.ph/wp-content/uploads/sites/4/2020/04/PSE-2016-FA-Meeting-Challenges.pdf
  local_path: pdfs/pse-annual-report-2016.pdf
  edition: historical
  amended_through: 2016-12-31
  note: "SCCP statistics (p.72)."
- slug: pse-annual-report-2017
  title: "PSE Annual Report 2017"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: https://documents.pse.com.ph/wp-content/uploads/sites/4/2021/07/2017_PSE_Annual_Report.pdf
  local_path: pdfs/pse-annual-report-2017.pdf
  edition: historical
  amended_through: 2017-12-31
  note: "SCCP statistics (p.32); CTGF 2016-2017 (p.67)."
- slug: pse-annual-report-2018
  title: "PSE Annual Report 2018"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: https://documents.pse.com.ph/wp-content/uploads/sites/4/2021/02/2018_PSE_Annual_Report.pdf
  local_path: pdfs/pse-annual-report-2018.pdf
  edition: historical
  amended_through: 2018-12-31
  note: "CTGF composition (p.121); 2018 clearing and settlement statistics, Rule 5.2 refund approval and C&S project history (p.47)."
- slug: pse-annual-report-2019
  title: "PSE Annual Report 2019"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: https://documents.pse.com.ph/wp-content/uploads/sites/4/2021/06/PSE-Annual-Report-2019-1.pdf
  local_path: pdfs/pse-annual-report-2019.pdf
  edition: historical
  amended_through: 2019-12-31
  note: "SCCP licence history (p.39); 2019 clearing and settlement statistics and the 15 May 2019 award of the new C&S system (p.27); year-end exposure (p.65); CTGF P1.248bn (p.66)."
- slug: pse-annual-report-2020
  title: "PSE Annual Report 2020 (SEC Form 17-A for FY2020)"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: https://documents.pse.com.ph/wp-content/uploads/sites/4/2021/06/2020-Annual-Report.pdf
  local_path: pdfs/pse-annual-report-2020.pdf
  edition: historical
  amended_through: 2020-12-31
  note: "I archived this file. Image-only scan except the cover page (80 pages; I read p.47 from a rendered image): Dec 2019 Millennium IT agreements and the forecast Q1 2022 go-live of the new clearing and settlement system."
- slug: pse-annual-report-2021
  title: "PSE Annual Report 2021 (SEC Form 17-A for FY2021)"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: https://documents.pse.com.ph/wp-content/uploads/sites/4/2022/05/2021-Annual-Report.pdf
  local_path: pdfs/pse-annual-report-2021.pdf
  edition: historical
  amended_through: 2021-12-31
  note: "I archived this file. Image-only scan except the cover page (63 pages; I read p.32 from a rendered image): forecast Q2 2022 go-live of the new clearing and settlement system."
- slug: pse-17c-2019-12-04-sccp-millennium-it-agreements
  title: "PSE SEC Form 17-C (4 Dec 2019): SCCP agreements with Millennium IT Software (Private) Limited for Millennium Post Trade and Millennium Risk"
  publisher: The Philippine Stock Exchange, Inc. (via PSE EDGE)
  type: pdf
  canonical_url: https://documents.pse.com.ph/wp-content/uploads/sites/4/2021/02/17-C-04-December-2019-%E2%80%93-Agreements-between-SCCP-subsidiary-and-Millennium-IT-Software-Private-Limited.pdf
  local_path: pdfs/pse-17c-2019-12-04-sccp-millennium-it-agreements.pdf
  edition: historical
  amended_through: 2019-12-04
  note: "I archived this file. Scope only (software licence and maintenance; consultancy); no contract value stated. Pages 4-6 are blank."
- slug: pse-annual-report-2025
  title: "PSE Annual Report 2025"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: https://documents.pse.com.ph/wp-content/uploads/sites/4/2026/04/2025-Annual-Report.pdf
  local_path: pdfs/pse-annual-report-2025.pdf
  edition: in-force
  amended_through: 2025-12-31
  note: "SCCP description and governance (pp.8, 44-47)."
- slug: pse-audited-fs-2020
  title: "PSE and Subsidiaries: Audited Consolidated Financial Statements for the year ended 31 December 2020 (Annex B to the FY2020 SEC Form 17-A)"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: https://documents.pse.com.ph/wp-content/uploads/sites/4/2021/05/Annex-B-Audited-Consolidated-Financial-Statements.pdf
  local_path: pdfs/pse-audited-fs-2020.pdf
  edition: historical
  amended_through: 2020-12-31
  note: "I archived this file. CTGF note (Note 34) on pp.84-85 gives the CTGF size and composition for 2020 and 2019; text layer present."
- slug: pse-audited-fs-2022
  title: "PSE and Subsidiaries: Audited Consolidated Financial Statements for the year ended 31 December 2022 (Annex B to the FY2022 SEC Form 17-A)"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: https://documents.pse.com.ph/wp-content/uploads/sites/4/2023/05/Annex-B-%E2%80%93-Audited-Consolidated-Financial-Statements.pdf
  local_path: pdfs/pse-audited-fs-2022.pdf
  edition: historical
  amended_through: 2022-12-31
  note: "I archived this file. Image-only scan (no text layer); I read the CTGF note (Note 34, printed page 69) on physical p.80 from a rendered image: CTGF size and composition for 2022 and 2021."
- slug: pse-annual-report-2024-compiled-17a
  title: "PSE SEC Form 17-A for FY2024 compiled with annexes (includes the audited consolidated financial statements)"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: https://documents.pse.com.ph/wp-content/uploads/sites/4/2025/04/Annual-Report-Compiled-17-A-with-Annexes_compressed-1.pdf
  local_path: pdfs/pse-annual-report-2024-compiled-17a.pdf
  edition: historical
  amended_through: 2024-12-31
  note: "I archived this file. 290 pages, image-only scan; I read the CTGF note (Note 36, printed pp.71-73) on physical pp.148-150 from rendered images: CTGF size and composition for 2024 and 2023, asset breakdown and the paragraph on the SEC's 13 Mar 2018 approval of the Rule 5.2 refund amendment."
- slug: pse-audited-fs-2025
  title: "PSE and Subsidiaries: Audited Consolidated Financial Statements for the year ended 31 December 2025 (Annex B to the FY2025 SEC Form 17-A)"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: https://documents.pse.com.ph/wp-content/uploads/sites/4/2026/04/Annex-B-%E2%80%93-Audited-Consolidated-Financial-Statements.pdf
  local_path: pdfs/pse-audited-fs-2025.pdf
  edition: in-force
  amended_through: 2025-12-31
  note: "I archived this file (106 pages, text layer). Cited: p.16 (PDSHC ownership 94.21%), p.39 (CCCS launch 29 May 2006, SCCP deferred tax), p.40-41 (SCCP risk note: MMCD, 20% haircut since 14 Nov 2008, new C&S System, T+2), p.59 and p.89 (Equitiworld takeover), p.65 (SCCP 50.00m appropriation), p.82 (outstanding trades at year-end), p.86-87 (CTGF size, composition, assets)."
- slug: pse-asm-2025-presidents-report
  title: "PSE 2025 Annual Stockholders' Meeting: President's Report"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: https://documents.pse.com.ph/wp-content/uploads/sites/4/2025/07/PSE-ASM-2025-PRESIDENT_S-REPORT-FINAL-v2.pdf
  local_path: pdfs/pse-asm-2025-presidents-report.pdf
  edition: historical
  amended_through: 2025-07-12
  note: "Cover: President's Report, July 12, 2025. PSE owns 92.06% of PDS at 30 May 2025 (p.32)."
- slug: pse-asm-2026-president-report
  title: "PSE 2026 Annual Stockholders' Meeting: President's Report"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: https://documents.pse.com.ph/wp-content/uploads/sites/4/2026/07/PSE-ASM-2026-PRESIDENT_S-REPORT.pdf
  local_path: pdfs/pse-asm-2026-president-report.pdf
  edition: in-force
  amended_through: 2026-07-04
  note: "Cover: President's Report, July 4, 2026. PDS integration roadmap incl. single post-trade system, Phase 2 target 2027 (p.28); NoCD expansion (p.28)."
- slug: pse-analyst-briefing-3m-2026
  title: "PSE Analyst Briefing, 3M 2026"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: https://documents.pse.com.ph/wp-content/uploads/sites/4/2026/07/3M-2026-PSE-Analyst-Briefing.pdf
  local_path: pdfs/pse-analyst-briefing-3m-2026.pdf
  edition: historical
  amended_through: 2026-03-18
  note: "PSE owns 94.55% of PDS at 5 Mar 2026; new central depository system (pp.24-25). Cover date March 18, 2026."
- slug: pse-analyst-briefing-1h-2026
  title: "PSE Analyst Briefing, 1H 2026"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: https://documents.pse.com.ph/wp-content/uploads/sites/4/2026/08/2026.08.17-PSE-STAR-1H-2026.pdf
  local_path: pdfs/pse-analyst-briefing-1h-2026.pdf
  edition: in-force
  amended_through: 2026-08-17
  note: "SCCP service fees (p.7), depository assets (p.18), PDS roadmap (p.31). Cover: PSE STAR Briefing, August 17, 2026; data to 30 Jun 2026."
- slug: pse-17c-2024-12-26-pdshc-acquisition-agreements
  title: "PSE SEC Form 17-C (26 Dec 2024): Agreements for the acquisition of PDSHC shares"
  publisher: The Philippine Stock Exchange, Inc. (via PSE EDGE)
  type: pdf
  canonical_url: https://documents.pse.com.ph/wp-content/uploads/sites/4/2025/01/17-C-December-26-2024-%E2%80%93-Signing-of-Agreements-for-the-Acquisition-of-Philippine-Dealing-System-Holdings-Corp.pdf
  local_path: pdfs/pse-17c-2024-12-26-pdshc-acquisition-agreements.pdf
  edition: historical
  amended_through: 2024-12-26
  note: "Terms, SEC approval 19 Dec 2024, PDTC ownership 97.72% by PDSHC."
- slug: pse-17c-2026-02-04-pdic-pdshc-shares
  title: "PSE SEC Form 17-C (4 Feb 2026, amended): Signing and closing of the PDIC sale of PDSHC shares, with PDSHC shareholder list and closing timeline"
  publisher: The Philippine Stock Exchange, Inc. (via PSE EDGE)
  type: pdf
  canonical_url: https://edge.pse.com.ph/downloadHtml.do?file_id=1866581
  local_path: pdfs/pse-17c-2026-02-04-pdic-pdshc-shares.pdf
  edition: historical
  amended_through: 2026-02-04
  note: "Archived by another researcher (browser print of the EDGE page, file_id 1866581; the same filing is also at documents.pse.com.ph under sites/4/2026/03). I cite pp.3-9 for PSE's 94.55% beneficial ownership of PDSHC, the aggregate 73.65% purchase and the closing trail. Pages 11-69 (attached PDSHC financial statements) have no text layer."
- slug: pse-tpa-2011-0110-amended-revised-trading-rules
  title: "PSE TPA 2011-0110 (7 Dec 2011): SEC-approved amendments to the Revised Trading Rules, effective January 2012"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: https://documents.pse.com.ph/wp-content/uploads/sites/15/2024/08/1_Amended-Revised-Trading-Rules_TPA_2011-0110.pdf
  local_path: pdfs/pse-tpa-2011-0110-amended-revised-trading-rules.pdf
  edition: in-force
  amended_through: 2011-12-07
  note: "Archived by another researcher; scanned (pages 2-6 have no text layer; I read p.4 as an image). I cite only Art. IV Sec. 14(c) (order cancellation on corporate actions and ex-dates); other articles in it have since been amended (trading hours, 2013-2025)."
- slug: pse-cn-2023-0074-ubp-trading-suspension
  title: "PSE CN-2023-0074 (21 Dec 2023): Trading suspension of Union Bank of the Philippines shares"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: https://documents.pse.com.ph/CircularOPSPDF/CN-2023-0074.pdf
  local_path: pdfs/pse-cn-2023-0074-ubp-trading-suspension.pdf
  edition: n/a
  amended_through: 2023-12-21
  note: "Archived by another researcher. Previous close not adjusted for UBP's 27% stock dividend; trading resumed 22 Dec 2023 at the adjusted price."
- slug: pse-cn-2025-0035-sec-declassification-mandate
  title: "PSE CN-2025-0035 (11 Aug 2025): SEC mandate to declassify Class A and Class B shares (SEC MC 10 s.2025 attached, pp.2-3)"
  publisher: The Philippine Stock Exchange, Inc. / Securities and Exchange Commission
  type: pdf
  canonical_url: https://documents.pse.com.ph/CircularOPSPDF/CN-2025-0035.pdf
  local_path: pdfs/pse-cn-2025-0035-sec-declassification-mandate.pdf
  edition: in-force
  amended_through: 2025-08-11
  note: "Archived by another researcher. The attached SEC circular text has a blank number and date; PSE's cover page names it MC 10 s.2025 issued 7 Aug 2025."
- slug: pse-cn-2025-0036-declassification-effectivity
  title: "PSE CN-2025-0036 (15 Aug 2025): Effectivity of the SEC circular mandating declassification of Class A and Class B shares"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: https://documents.pse.com.ph/CircularOPSPDF/CN-2025-0036.pdf
  local_path: pdfs/pse-cn-2025-0036-declassification-effectivity.pdf
  edition: in-force
  amended_through: 2025-08-15
  note: "Archived by another researcher. Effective 9 Aug 2025; articles to be amended by 9 Aug 2026; buyers receive the class bought from 11 Aug 2025."
- slug: pse-cn-2026-0041-declassification-price-suspension
  title: "PSE circular of 10 Sep 2026 (filed as 2026-0041): Price adjustment upon declassification of shares and trade suspension prior to delisting"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: https://documents.pse.com.ph/wp-content/uploads/sites/15/2026/09/2026-0041-Declassification-Price-Adjustment-and-Trading-Suspension-Mechanics.pdf
  local_path: pdfs/pse-cn-2026-0041-declassification-price-suspension.pdf
  edition: in-force
  amended_through: 2026-09-10
  note: "Archived by another researcher. Adjusted price = higher of Class A/B closes; two-trading-day suspension so trades settle on the standard T+2 cycle; sample timeline on p.2."
- slug: ra-8799-src
  title: "Republic Act No. 8799, The Securities Regulation Code"
  publisher: Republic of the Philippines
  type: pdf
  canonical_url: https://documents.pse.com.ph/wp-content/uploads/sites/15/2021/04/Securities-Regulation-Code-1.pdf
  local_path: pdfs/ra-8799-src.pdf
  edition: in-force
  amended_through: 2000-07-19
  note: "Archived by another researcher; the archived file is the PSE-hosted copy (249,135 bytes, same as the URL shown). Approved 19 Jul 2000 per the last page."
- slug: sec-2015-src-irr
  title: "2015 Implementing Rules and Regulations of the Securities Regulation Code"
  publisher: Securities and Exchange Commission (Philippines)
  type: pdf
  canonical_url: https://appointment.sec.gov.ph/wp-content/uploads/2019/11/2015IRR_RA9799.pdf
  local_path: pdfs/sec-2015-src-irr.pdf
  edition: in-force
  amended_through: 2015-08-04
  note: "Signed 4 August 2015 (SEC Resolution No. 494, s.2015); effective 15 days after the last newspaper publication (publication date not in the document). Rule 42 (clearing agencies), 36.4.4.5 (CCP), 28.1.2.5.2(b)."
- slug: pse-dds-rules
  title: "PSE Rules on Dollar Denominated Securities (SEC-approved 10 Nov 2016)"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: https://documents.pse.com.ph/wp-content/uploads/sites/15/2021/01/Approved_DDS_Rules.pdf
  local_path: pdfs/pse-dds-rules.pdf
  edition: in-force
  amended_through: 2016-11-10
  note: "Part D clearing and settlement (pp.8-10)."
- slug: pse-cn-2018-0023-trading-without-settlement-proposal
  title: "PSE CN-2018-0023 (10 Apr 2018): Proposed rule amendment and guidelines for trading without settlement"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: https://documents.pse.com.ph/CircularOPSPDF/CN-2018-0023.pdf
  local_path: pdfs/pse-cn-2018-0023-trading-without-settlement-proposal.pdf
  edition: historical
  amended_through: 2018-04-10
  note: "T+3-era SCCP guideline; formalised later as Rule 4.9."
- slug: pse-cn-2025-0026-stt-decrease-advisory
  title: "PSE CN-2025-0026 (11 Jun 2025): Advisory on decrease of stock transaction tax"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: https://documents.pse.com.ph/CircularOPSPDF/CN-2025-0026.pdf
  local_path: pdfs/pse-cn-2025-0026-stt-decrease-advisory.pdf
  edition: in-force
  amended_through: 2025-06-11
  note: "STT 0.6% to 0.1% from 1 Jul 2025."
- slug: pse-cn-2025-0028-cmepa-effectivity
  title: "PSE CN-2025-0028 (26 Jun 2025): Effectivity of RA 12214 (CMEPA)"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: https://documents.pse.com.ph/CircularOPSPDF/CN-2025-0028.pdf
  local_path: pdfs/pse-cn-2025-0028-cmepa-effectivity.pdf
  edition: in-force
  amended_through: 2025-06-26
  note: "Publication dates and 1 Jul 2025 application."
- slug: pse-index-policy-2024
  title: "PSE Policy on Index Management (2024)"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: https://documents.pse.com.ph/wp-content/uploads/sites/15/2024/01/Policy-on-Index-Management-ver-2024.pdf
  local_path: pdfs/pse-index-policy-2024.pdf
  edition: in-force
  amended_through: 2024-01-31
  note: "Cover says only 'January 2024' (month precision; month end used). Corporate-action adjustment language (p.14)."
- slug: pse-itch-equities-feed-spec-v2-3
  title: "PSE ITCH Equities Feed Specification v2.3 (X-stream)"
  publisher: The Philippine Stock Exchange, Inc. / OMX Technology
  type: pdf
  canonical_url: https://documents.pse.com.ph/wp-content/uploads/sites/15/2024/03/PSE_Equities_Feed_Specification_v2.3.pdf
  local_path: pdfs/pse-itch-equities-feed-spec-v2-3.pdf
  edition: in-force
  amended_through: 2018-10-05
  note: "Cover: Version 2.3, 5 October 2018 (revision history from 2014). X-stream feed, live until the Nasdaq Eqlipse cutover planned for 23 Nov 2026 (per the market-architecture chapter). Reference-price message mechanics (p.27)."
- slug: pse-securities-static-data-file
  title: "PSE Securities Static Data File specification"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: https://documents.pse.com.ph/wp-content/uploads/sites/15/2026/07/PSE_Securities-Static-Data_File_v1.0-1.pdf
  local_path: pdfs/pse-securities-static-data-file.pdf
  edition: in-force
  amended_through: 2026-06-22
  note: "Cover: 'As of 22 June 2026 Version 1.0'. Field lacp = last adjusted close price (p.4)."
- slug: pse-quote-file-eod-spec-2014
  title: "PSE Quote File (EOD) specification (2014)"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: https://documents.pse.com.ph/wp-content/uploads/sites/15/2021/01/Quote-File-for-End-of-Dat-Security-Prices-updated-as-of-November-04-2014.pdf
  local_path: pdfs/pse-quote-file-eod-spec-2014.pdf
  edition: historical
  amended_through: 2014-11-04
  note: "Cover: 'As of 11/4/2014 v2.0' (day/month order ambiguous). Field 'Adjusted Previous' (p.2)."
- slug: bsp-schedule-peso-rtgs
  title: "BSP: Schedule of Peso Real-Time Gross Settlements"
  publisher: Bangko Sentral ng Pilipinas
  type: pdf
  canonical_url: https://www.bsp.gov.ph/PaymentAndSettlement/ScheduleofPesoRTGS.pdf
  local_path: pdfs/bsp-schedule-peso-rtgs.pdf
  edition: in-force
  amended_through: undated
  note: No date printed on the document. Obtained from Wayback capture 2025-06-21 (BSP blocks curl). Possibly superseded by the 22/7 operations regime; unverified.
- slug: bsp-philpassplus-primer
  title: "The PhilPaSSplus Primer"
  publisher: Bangko Sentral ng Pilipinas
  type: pdf
  canonical_url: https://www.bsp.gov.ph/PaymentAndSettlement/PhilPaSSplus_primer.pdf
  local_path: pdfs/bsp-philpassplus-primer.pdf
  edition: in-force
  amended_through: undated
  note: "No date printed on the document. Wayback capture 2025-10-14; operating hours 9:00-17:45 Mon-Fri (p.10)."
- slug: bsp-faqs-22x7-peso-rtgs-2026-07
  title: "BSP Payments and Settlements Department: Frequently Asked Questions on the 22/7 Peso Real-Time Gross Settlement Operations (July 2026)"
  publisher: Bangko Sentral ng Pilipinas
  type: pdf
  canonical_url: https://www.bsp.gov.ph/PaymentAndSettlement/FAQs-22x7-Peso-RTGS-Operations.pdf
  local_path: pdfs/bsp-faqs-22x7-peso-rtgs-2026-07.pdf
  edition: in-force
  amended_through: 2026-07-31
  note: "Dated 'July 2026' on every page (day not given; 2026-07-31 used as month end). Soft launch targeted Nov 2026; current RTGS 8.75 hours x 5 days. Fetched through WebFetch's local binary save."
- slug: bsp-m-2022-049-peso-rtgs-rules
  title: "BSP Memorandum No. M-2022-049: Peso Real-Time Gross Settlement (RTGS) Rules"
  publisher: Bangko Sentral ng Pilipinas
  type: pdf
  canonical_url: https://www.bsp.gov.ph/Regulations/Issuances/2022/M-2022-049.pdf
  local_path: pdfs/bsp-m-2022-049-peso-rtgs-rules.pdf
  edition: in-force
  amended_through: 2022-11-17
  note: Approved by Monetary Board Resolution No. 1680 dated 17 Nov 2022 (memo issuance date not stated). Wayback capture 2025-04-15; OCR-noisy scan; payment finality and DvP (p.8).
- slug: bsp-fx-manual-morfxt-2025-05
  title: "BSP Manual of Regulations on Foreign Exchange Transactions (May 2025)"
  publisher: Bangko Sentral ng Pilipinas
  type: pdf
  canonical_url: https://www.bsp.gov.ph/Regulations/MORFXT/MORFXT.pdf
  local_path: pdfs/bsp-fx-manual-morfxt-2025-05.pdf
  edition: in-force
  amended_through: 2025-05-31
  note: "Cover: 'Updated as of May 2025' (month precision; month end used). Sec. 32.2 (p.42) and Sec. 37 (p.46) on registration of inward investments. The live file at the URL shown, fetched through WebFetch's local binary save on 6 Oct 2026, is byte-identical to the archived copy; BSP blocks curl."
- slug: sccp-web-about
  title: "SCCP website: About Us"
  publisher: SCCP
  type: web
  canonical_url: https://sccp.com.ph/main/aboutUs.html
  local_path: null
  edition: in-force
  amended_through: undated
  note: "Retrieved 6 Oct 2026 (non-www host; www host returns 403 to curl)."
- slug: sccp-web-services
  title: "SCCP website: Services (clearing, CCP, CTGF, risk management)"
  publisher: SCCP
  type: web
  canonical_url: https://sccp.com.ph/main/services.html
  local_path: null
  edition: in-force
  amended_through: undated
  note: "Retrieved 6 Oct 2026; its collateral list shows 'effective 1 Feb 2024' (stale vs memo 01-0126) and cites CTGF use under 'Rule 5.1.5' (differs from 2018 numbering 5.1.6)."
- slug: sccp-web-membership
  title: "SCCP website: Membership (requirements and clearing-member directory)"
  publisher: SCCP
  type: web
  canonical_url: https://sccp.com.ph/main/membership.html
  local_path: null
  edition: in-force
  amended_through: undated
  note: "Retrieved 6 Oct 2026; counts derived by parsing the table (125 rows: 122 active, 3 suspended; 118 local, 7 foreign)."
- slug: sccp-web-partners
  title: "SCCP website: Partners (settlement banks image SBanks.png, depository)"
  publisher: SCCP
  type: web
  canonical_url: https://sccp.com.ph/main/partners.html
  local_path: null
  edition: in-force
  amended_through: undated
  note: "Nine bank logos read from https://sccp.com.ph/resources/images/SBanks.png."
- slug: sccp-web-memos-index
  title: "SCCP website: Memos index (2012-2026)"
  publisher: SCCP
  type: web
  canonical_url: https://sccp.com.ph/main/memos.html
  local_path: null
  edition: in-force
  amended_through: 2026-09-11
  note: "Latest entry memo 01-0926 (11 Sep 2026); no T+1/margin/rule memo after 8 Jul 2025."
- slug: sccp-web-rules-page
  title: "SCCP website: Rules & Regulations page"
  publisher: SCCP
  type: web
  canonical_url: https://sccp.com.ph/main/rulesAndRegulations.html
  local_path: null
  edition: in-force
  amended_through: undated
  note: "Lists only the 031318 Rules and OpProcs and the two quick guides."
- slug: pse-edge-dividends-rights
  title: "PSE EDGE: Dividends and Rights (dividend/rights information list)"
  publisher: The Philippine Stock Exchange, Inc.
  type: web
  canonical_url: https://edge.pse.com.ph/disclosureData/dividends_and_rights_info_form.do
  local_path: null
  edition: in-force
  amended_through: 2026-10-06
  note: "Live list retrieved 6 Oct 2026 via POST to /disclosureData/dividends_and_rights_info_list.ax; 518 dividend rows, 12 rights rows. My parse, not archived."
- slug: pse-edge-market-calendar
  title: "PSE EDGE: Market Calendar (cash/stock ex-dates, meetings, listings)"
  publisher: The Philippine Stock Exchange, Inc.
  type: web
  canonical_url: https://edge.pse.com.ph/companyPage/marketCalendar.do
  local_path: null
  edition: in-force
  amended_through: 2026-10-06
  note: "Read through a summarising fetch tool (October 2026 view)."
- slug: pse-pr-t2-go-live
  title: "PSE press release: SCCP's T+2 settlement cycle goes live on August 24 (15 Aug 2023)"
  publisher: The Philippine Stock Exchange, Inc.
  type: web
  canonical_url: https://www.pse.com.ph/sccps-t2-settlement-cycle-goes-live-on-august-24/
  local_path: null
  edition: historical
  amended_through: 2023-08-15
  note: "Read through a summarising fetch tool, not verbatim."
- slug: pse-pr-t2-migration-complete
  title: "PSE press release: SCCP marks successful migration to the T+2 settlement cycle (4 Sep 2023)"
  publisher: The Philippine Stock Exchange, Inc.
  type: web
  canonical_url: https://www.pse.com.ph/sccp-marks-successful-migration-to-the-t2-settlement-cycle/
  local_path: null
  edition: historical
  amended_through: 2023-09-04
  note: "Read through a summarising fetch tool."
- slug: pse-pr-sccp-new-cs-system
  title: "PSE press release: SCCP migrates to new clearing and settlement technology (31 Mar 2023)"
  publisher: The Philippine Stock Exchange, Inc.
  type: web
  canonical_url: https://www.pse.com.ph/sccp-migrates-to-new-clearing-and-settlement-technology/
  local_path: null
  edition: historical
  amended_through: 2023-03-31
  note: "LSEG Millennium Post Trade live 27 Mar 2023; read through a summarising fetch tool."
- slug: pds-web-rules
  title: "PDS Group website: Rules and PDTC Guidelines document lists"
  publisher: Philippine Dealing System Group
  type: web
  canonical_url: https://www.pds.com.ph/rules/
  local_path: null
  edition: in-force
  amended_through: 2026-08-27
  note: "Rules page: latest dated items are a 27 Aug 2026 comment proposal and a 20 Jul 2026 PDEx settlement-date proposal for SEC approval; PDTC Registry Rules (May 2021). The FCY-securities NoCD list (30 Sep 2026) and the Registry Rules PDF are password-protected and sit on the companion page https://www.pds.com.ph/pdtc-guidelines/."
- slug: pdex-proposed-settlement-date-conventions-2026
  title: "PDEx: Proposed amendments to the Trading Conventions on Settlement Date (fixed income; revived Nov 2024, updated Dec 2024)"
  publisher: Philippine Dealing & Exchange Corp. (PDS Group)
  type: pdf
  canonical_url: https://pdswordpressbucket.s3.ap-southeast-1.amazonaws.com/wp-content/uploads/2026/07/Proposed-Amendments-to-the-Trading-Conventions-on-Settlement-Date.pdf
  local_path: pdfs/pdex-proposed-settlement-date-conventions-2026.pdf
  edition: n/a
  amended_through: 2024-12-31
  note: "Fixed-income market, not equities; listed on https://www.pds.com.ph/rules/ under rule proposals for SEC approval with posting date 20 Jul 2026. The document itself says only 'Updated as of December 2024' (month precision; month end used)."
- slug: pds-web-depository-participants
  title: "PDS Group website: Depository Participants (as of 30 September 2026)"
  publisher: Philippine Dealing System Group
  type: web
  canonical_url: https://www.pds.com.ph/depository-participants/
  local_path: null
  edition: in-force
  amended_through: 2026-09-30
  note: "Counts (192 equities, 63 fixed-income) are my parse of the page's numbered tables."
- slug: bsp-web-payments-settlements
  title: "BSP website: Payments and Settlements (Peso RTGS/PhilPaSSplus; 22/7 operations)"
  publisher: Bangko Sentral ng Pilipinas
  type: web
  canonical_url: https://www.bsp.gov.ph/SitePages/PaymentsAndSettlements/PaymentsAndSettlements.aspx
  local_path: null
  edition: in-force
  amended_through: undated
  note: "Read through a summarising fetch tool (BSP blocks curl); lists M-2022-049, Circular 1181 (ISF), M-2025-039 and 22/7 FAQs."
- slug: clearstream-ph-settlement-process
  title: "Clearstream market profile: Settlement process - Philippines"
  publisher: Clearstream Banking (Deutsche Boerse Group)
  type: web
  canonical_url: https://www.clearstream.com/clearstream-en/res-library/market-coverage/settlement-process-philippines-1280470
  local_path: null
  edition: in-force
  amended_through: 2026-01-05
  note: "Secondary. Contains stale items (margin proposal, T+1 for batch run wording)."
- slug: clearstream-ph-market-infrastructure
  title: "Clearstream market profile: Market infrastructure - Philippines"
  publisher: Clearstream Banking
  type: web
  canonical_url: https://www.clearstream.com/clearstream-en/res-library/market-coverage/market-infrastructure-philippines-1280424
  local_path: null
  edition: in-force
  amended_through: 2024-02-21
  note: "Secondary."
- slug: clearstream-ph-market-link-guide
  title: "Clearstream Market Link Guide - Philippines"
  publisher: Clearstream Banking
  type: web
  canonical_url: https://www.clearstream.com/clearstream-en/res-library/market-coverage/market-link-guide-philippines-1279272
  local_path: null
  edition: in-force
  amended_through: 2025-12-05
  note: "Secondary; legal opinion dated 11 Sep 2025."
- slug: clearstream-ph-settlement-times
  title: "Clearstream settlement times - Philippines"
  publisher: Clearstream Banking
  type: web
  canonical_url: https://www.clearstream.com/clearstream-en/res-library/market-coverage/settlement-times-philippines-1279298
  local_path: null
  edition: in-force
  amended_through: 2026-03-12
  note: "Secondary; CET-labelled deadlines for 29 Mar-24 Oct 2026 and 25 Oct 2025-27 Mar 2026."
- slug: clearstream-ph-settlement-services
  title: "Clearstream settlement services - Philippines (pre-matching, SSI, funding, dematerialisation)"
  publisher: Clearstream Banking
  type: web
  canonical_url: https://www.clearstream.com/clearstream-en/res-library/market-coverage/settlement-services-philippines--1279314
  local_path: null
  edition: in-force
  amended_through: 2024-02-27
  note: "Secondary."
- slug: clearstream-ph-cash-services
  title: "Clearstream cash services - Philippines"
  publisher: Clearstream Banking
  type: web
  canonical_url: https://www.clearstream.com/clearstream-en/res-library/market-coverage/cash-services-philippines-1279332
  local_path: null
  edition: in-force
  amended_through: 2024-02-27
  note: "Secondary."
- slug: clearstream-ph-asset-servicing
  title: "Clearstream asset servicing - Philippines"
  publisher: Clearstream Banking
  type: web
  canonical_url: https://www.clearstream.com/clearstream-en/res-library/market-coverage/asset-servicing-philippines-1279324
  local_path: null
  edition: in-force
  amended_through: 2024-02-27
  note: "Secondary."
- slug: clearstream-ph-securities-administration
  title: "Clearstream market profile: Securities administration - Philippines"
  publisher: Clearstream Banking
  type: web
  canonical_url: https://www.clearstream.com/clearstream-en/res-library/market-coverage/securities-administration-philippines-1280486
  local_path: null
  edition: in-force
  amended_through: 2024-02-21
  note: "Secondary; internally inconsistent on ex-date (RD-1 vs three working days)."
- slug: clearstream-ph-investment-regulation
  title: "Clearstream market profile: Investment regulation - Philippines"
  publisher: Clearstream Banking
  type: web
  canonical_url: https://www.clearstream.com/clearstream-en/res-library/market-coverage/investment-regulation-philippines-1280438
  local_path: null
  edition: in-force
  amended_through: 2026-01-13
  note: "Secondary; BSP registration, 40% foreign ownership limit, PDTC account segregation."
- slug: rbc-ph-market-profile
  title: "RBC Investor Services Market Profile: Philippines"
  publisher: RBC Investor Services
  type: web
  canonical_url: https://www.rbcis.com/en/gmi/global-custody/market-profiles/market.page?dcr=templatedata/globalcustody/marketprofiles/data/philippines
  local_path: null
  edition: in-force
  amended_through: 2023-09-15
  note: "Secondary; 'updated as at September 15, 2023' (pre-dates STT cut, mixes T+2 and T+3 wording)."
```
