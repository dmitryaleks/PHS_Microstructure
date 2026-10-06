# Chapter 1 — Market architecture of the Philippine Stock Exchange (PSE): institutions, governance, trading technology, participants

> **Currency:** researched 6 Oct 2026. "In force" means in force on 6 Oct 2026 unless a date says otherwise. Evidence labels: **[P]** primary document (PSE/SCCP/PDS/SEC/statute/exchange circular), **[S]** secondary only (press/aggregator), **[I]** my inference. Citations are footnote-style keys: a caret-slug-colon-page key points to physical 1-based page N of the archived PDF `kb/pdfs/<slug>.pdf` (page N is what a PDF viewer shows, not the printed folio); a caret-slug key without a page points to a web page. Every key is defined in the Source catalog at the end (web pages fetched 6 Oct 2026 unless the entry says otherwise).
>
> **State of play on 6 Oct 2026 (one-line each):** PSE is the only stock exchange; engine = PSEtrade XTS (Nasdaq X-stream, live 22 Jun 2015) with a **big-bang cutover to Nasdaq Eqlipse Trading planned for Mon 23 Nov 2026**; 123 trading participants in the public directory (121 active, 2 suspended); PSE owns **94.55%** of PDS Group Holdings (PDEx + PDTC) since 4 Feb 2026; equities settle **T+2** (since trade date 24 Aug 2023); minimum TP unimpaired paid-up capital still **P30M** (increase to P50M/P100M only proposed, 21 Jul 2026); 3,641,067 stock-market accounts at end-2025 (88.6% online); board-lot ("One Lot One Share") and negotiated-trade rules are tied to the new engine and were still awaiting SEC approval on 4 Jul / 17 Aug 2026. Market context: PSEi 5,629.03 at the 2 Oct 2026 close (−3.4% w/w, −7.0% YTD), total market cap P19.44tn.[^pse-weekly-market-watch-2026-10-02:3]

---

## 1. Institutional map: who runs, regulates, clears and settles the Philippine equity market

### Takeaway
The PSE is a demutualised (3 Aug 2001), self-listed (15 Dec 2003), SEC-licensed exchange **and** front-line SRO that now vertically owns its clearing CCP (SCCP, 100%), its market-regulation arm (CMIC, 100%) and — since Dec 2024–Feb 2026 — the depository/registry + fixed-income exchange group (PDS Group, 94.55%). The SEC (Securities Regulation Code, RA 8799, and the 2015 IRR) is the statutory regulator that must pre-approve PSE/CMIC/SCCP rules and can order a TP take-over; BSP matters via settlement banks, PDTC's dual oversight and FX/investment registration. Order → match → CCP novation → DVP at the depository is therefore a single-venue, single-CCP, single-CSD chain.

### Cited findings

#### 1.1 PSE: corporate form, SRO status, ownership caps, board
- **[P]** Incorporated 14 Jul 1992 as a non-stock corporation; became a stock corporation 3 Aug 2001; shares listed by introduction 15 Dec 2003 "pursuant to the demutualization mandate of RA 8799". "The PSE is the only stock exchange that operates and regulates the Philippine equities market"; offers listing, trading, market data, clearing, settlement.[^pse-annual-report-2025:8] Manila SE (1927) and Makati SE (1963) unified 23 Dec 1992; SEC licence to operate as exchange 4 Mar 1994; SEC granted temporary SRO status in 1996 and the SRO certificate on 29 Jun 1998.[^pse-corp-history]
- **[P]** SRC §33.2(a) required an existing exchange to reorganise as a stock corporation within one year under an SEC-approved demutualisation plan; §33.2(b) exchange must be solely in the business of operating an exchange (SEC may exempt a subsidiary of a juridical parent).[^ra-8799-src-lawphil]
- **[P]** Statutory governance constraints (SRC §33.2): no person may own/control >5% of voting rights and no "industry or business group" >20%; brokers may be at most 49% of the board; president + ≥51% of the remaining directors must be independents/representatives of issuers and investors not associated with a broker for 2 years; president/management must not be broker-affiliated for ≥2 years.[^ra-8799-src-lawphil] IRR Rule 33.2(c): brokers and dealers are "one industry group"; SEC may order divestment and bar the excess holder from voting.[^sec-2015-src-irr:110][^sec-2015-src-irr:111]
- **[P]** Compliance history: PSE rights offering (P2.90bn, listed Mar 2018) "brought the PSE closer to complying with the industry ownership limit"; broker shareholdings 19.9% in May 2020.[^pse-corp-history] Litigation: SC decision of 30 Jan 2024 on PASBDI et al. v. PSE/SEC (limits on brokers voting their whole holding) reversed the injunction against the SEC but affirmed it against PSE and PSE Nomelec for the 2010 Nomelec rules.[^pse-annual-report-2025:11]
- **[P]** Shareholders at 31 Mar 2026: 82,062,326 shares, 316 holders of record; PCD Nominee (Filipino) 62.60%; PCD Nominee (Non-Filipino) 10.73%; San Miguel Corp. Retirement Plan 9.21%; SM Investments 4.31%; many broker-TPs hold 240,000 shares (0.29%) each; foreign-owned 12.45%; public float 65.72% (31 Dec 2025).[^pse-annual-report-2025:13][^pse-annual-report-2025:14][^pse-annual-report-2025:62]
- **[P]** Board of 15 (website, Oct 2026): Chair Jose T. Pardo; President & CEO Ramon S. Monzon; independents incl. J. Bautista, T. Leonardo-De Castro, P. Favila, J. Kang, N. J. van Veen; broker-directors per FY2025 17-A bios incl. D. Arroyo, E. Gobing, A. Te, V. Yuchengco (and W. Sy, no longer listed on the website).[^pse-corp-board][^pse-annual-report-2025:42][^pse-annual-report-2025:43] COO Roel A. Refran; Head, Market Operations Division Marvin M. Refuerzo; Head, Technology Division Philip A. Driz.[^pse-annual-report-2025:43]
- **[P]** PSE lists itself on its own board under an MOU with the SEC; the SEC (acting "as the Exchange") posts PSE's own disclosures to PSE EDGE.[^pse-17c-2025-05-22-nasdaq-eqlipse-contract:1]
- **[P]** Group (FY2025 17-A, stake as of 4 Feb 2026): SCCP (100%), CMIC (100%), Premier Software Enterprise Inc. (IT subsidiary incorporated Apr 2019, 100%), PSE Realty Inc. (SEC-approved Jun 2024), PDS Holdings (94.55%).[^pse-annual-report-2025:8][^pse-annual-report-2025:9] 6M2026 revenue mix: trading 34%, listing 23%, depository 20%, market data 7%, technology 3%, other 13%.[^pse-analyst-briefing-1h-2026:5]

#### 1.2 SEC and the statute (RA 8799; 2015 IRR effective 9 Nov 2015)
- **[P]** SRC: §32.1 no broker/dealer may use an unregistered exchange; §32.2 other trading markets only per SEC rules and under an SRO "comparable" to an exchange; §33.1(d) every exchange undertakes to take over an insolvent member on SEC order; §36.1 SEC may summarily suspend trading in a listed security; §36.3 SEC decides "the number, size and location of stock Exchanges... in addition to the existing PSE"; §36.4 SEC rules on clearance/settlement; §36.5 SEC-supervised investor-compensation trust funds; §40.3 SROs need **prior SEC approval** of any rule/amendment (SEC must act within 60 days, else the SRO may make it effective; emergency summary effectivity allowed); §40.4 SEC may alter/abrogate SRO rules on matters incl. hours of trading, minimum units of trading, odd lots, settlement timing; §40.5 SEC may suspend an SRO up to 12 months; §40.6 SRO discipline; §40.7 SEC review of sanctions on appeal/own motion within 30 days; §42.2(f) clearing agency must run a guarantee fund sized on exposure of the four largest trading brokers; §28.4(b) broker-dealers must meet SEC minimum net capital and post a bond.[^ra-8799-src-lawphil]
- **[P]** 2015 SRC IRR took effect 9 Nov 2015.[^sec-2015-src-irr-notice-of-effectivity:1] Rule 28.1.2.5.1: an Exchange Trading Participant (ETP) needs good-standing membership in an Exchange, participation in an SEC-accredited Trust Fund (Rule 36.5.1) and clearing-fund contributions.[^sec-2015-src-irr:77] Rule 33.1(d).3: take-over procedure (suspend, transfer accounts to another TP, liquidate trading right and trade-related assets, notify the accredited trust fund).[^sec-2015-src-irr:109] Rule 36.4.4.5: SEC may require use of a central counterparty; Rule 36.5.1: "Accredited Trust Fund".[^sec-2015-src-irr:119] Rule 39.1.1.5: SRO must run market surveillance; Rule 39.1.3: SROs may file allocation-of-responsibility plans.[^sec-2015-src-irr:126][^sec-2015-src-irr:131]
- **[P]** PSE's own summary of the split: SEC = primary regulator; PSE and CMIC are "licensed as SROs" for front-line regulation; PSE enforces TP admission/trading-right rules and (non-audit) trading rules and listing/disclosure rules (maximum penalty on issuers: involuntary delisting); CMIC halts/suspends securities for trading irregularities and enforces SRC/SRC-IRR/SEC/PSE/CMIC rules against TPs; SEC reviews PSE/CMIC decisions, revokes TP/salesman/associated-person licences, orders take-overs and refers criminal cases to the DOJ. (The web table repeats the "rules that do not require audit of books" sentence in both the PSE and CMIC cells — treat the exact split as per the CMIC Rules.)[^pse-corp-regulatory-framework]
- **[P]** The SEC approves PSE rules by letter (e.g. TP Rules approved 28 May 2009; DMA Rules transmitted 29 Oct 2013; CMIC Rules approved 12–13 Jan 2012).[^pse-rules-trading-rights-trading-participants:3][^pse-dma-rules:1][^pse-cmic-rules:2] Board-lot (One Lot One Share), negotiated-trade and other rule changes in 2026 are explicitly "awaiting SEC approval".[^pse-asm-2026-president-report:22][^pse-analyst-briefing-1h-2026:9]

#### 1.3 CMIC (Capital Markets Integrity Corporation)
- **[P]** Wholly-owned PSE subsidiary; "independent audit, surveillance, and compliance arm of the Exchange"; took over the former PSE Market Regulation Division; SEC granted authority to operate with **provisional SRO status on 2 Feb 2012**; CMIC Rules "took effect in March 2012".[^pse-annual-report-2025:8][^pse-corp-group-structure][^pse-corp-history] SEC resolved on 12 Jan 2012 (letter 13 Jan 2012) to approve the CMIC Rules and operating procedures; on 2 Feb 2012 it approved an appeal-to-CMIC-Board amendment (Art. III Sec. 6: 10 business days, 5 for summary actions).[^pse-cmic-rules:2][^pse-cmic-rules:4] PSE circular dated 23 Feb 2012 announced the approved rules (effectivity "announced later").[^pse-cmic-rules:1]
- **[P]** Mandate (CMIC Rules v1.2, 15 Dec 2011): jurisdiction over all violations of securities laws/CMIC Rules by TPs and over trading-related irregularities/unusual trading involving issuers (Art. II §1); Listing/Disclosure departments keep issuer disclosure and continuing-listing jurisdiction (Art. II §3); TPs must state they are a PSE TP and a member of SCCP and of the SIPF (Art. I §4); **best-execution duty** (Art. VII §31: "reasonable diligence to ascertain the best available price"); TP failure/take-over procedure and SIPF role (Art. VII §30); capital/RBCA monitoring (Art. VIII); involuntary suspension grounds incl. third clearing-house suspension in a year, clearing-agency suspension, RBCA <1.1 or NLC <P5M not cured (Art. X §7); trading irregularities incl. marking the close and wash sales (Art. XI).[^pse-cmic-rules:9][^pse-cmic-rules:11][^pse-cmic-rules:12][^pse-cmic-rules:56][^pse-cmic-rules:58][^pse-cmic-rules:59][^pse-cmic-rules:106][^pse-cmic-rules:117]
- **[P]** Process and sanctions: CMIC decides cases in the first instance (substantial-evidence standard); appeal to the CMIC Board within 10 business days (5 for summary actions); for grave/major violations onward appeal to the **SEC** within 15 calendar days under SEC MC 10 (2010) — PSE itself is not in the appeal chain; decisions become executory once the appeal period lapses, and execution is stayed pending a CMIC-Board appeal except for minor violations and for suspension/expulsion sanctions. Scale (Art. XII §4): grave violations — reprimand + fine P25,000–200,000, then denial of trading-right exercise/exchange access, then bar; major — fines P10,000–30,000 / 30,000–50,000 / 50,000–75,000 / ≥P75,000; minor — reprimand, then P10,000–50,000. Rules took effect 15 days after publication on the Exchange and CMIC websites.[^pse-cmic-rules:17][^pse-cmic-rules:119][^pse-cmic-rules:120][^pse-cmic-rules:124]
- **[P]** CMIC surveillance system "TMS" (acquired from the Korea Exchange) launched 8 May 2012; a **new surveillance system for CMIC** is on PSE's 2026 technology-upgrade list.[^pse-corp-history][^pse-analyst-briefing-3m-2026:24] CMIC President in 2025–26 notices: Gerard B. Sanvictores.[^pse-cn-2025-0027:2]
- **Independence:** only structural evidence found — 100% PSE-owned, separate SEC-approved rulebook, SEC (not PSE) hears appeals. CMIC board composition/funding not found (cmic.com.ph returns HTTP 403 to automated clients).

#### 1.4 SCCP (Securities Clearing Corporation of the Philippines)
- **[P]** Wholly-owned PSE subsidiary (became wholly-owned in 2004); incorporated 1996; commercial operations 3 Jan 2000; permanent licence 17 Jan 2002; "acts as a Central Counterparty to trades executed at the PSE"; SEC-supervised and authorised to fine/sanction clearing members.[^pse-corp-group-structure][^pse-corp-history] Functions: DVP synchronisation, Clearing and Trade Guaranty Fund (CTGF) and Fails Management, risk monitoring.[^pse-annual-report-2025:8]
- **[P]** Mechanics (Clearing House Rules, revised 13 Mar 2018): eligible clearing members are SEC-licensed broker/dealers that are PSE participants, depository participants and account holders at an accredited settlement bank (Rule 2.1);[^sccp-clearing-house-rules-2018:18] daily multilateral netting then **novation** — SCCP becomes buyer to every net seller and seller to every net buyer (Rules 3.1–3.3);[^sccp-clearing-house-rules-2018:26] PSE trade feed sent "immediately after the applicable trading hours" and SCCP gives settlement banks a Cash List by the first business day after trade date (Rule 4.1.1–4.1.2);[^sccp-clearing-house-rules-2018:29] CTGF target ("Ideal Fund Size") = **11% of the clearing member's average trade value over six months**, 50% of the required contribution payable on admission for new TPs;[^sccp-clearing-house-rules-2018:33] clearing is at **clearing-member, not beneficial-customer, level**.[^sccp-web-services] The 2018 Operating Procedures define a late cash payment as one confirmed by the settlement bank after the 12:00 NN cut-off on settlement date (text still says T+3).[^sccp-clearing-house-operating-procedures-2018:13]
- **[P]** **T+2**: SCCP/PSE announced migration (CN-2023-0031, 23 Jun 2023): first T+2 trade date **24 Aug 2023**, settling 29 Aug 2023 (28 Aug holiday); last T+3 trades (23 Aug) also settled 29 Aug; ex-rights dates moved to one trading day before record date.[^pse-cn-2023-0031-t2-settlement:1][^pse-cn-2023-0031-t2-settlement:2] SEC-approved T+2 amendments to the Rules/Operating Procedures (SCCP Memo 06-0823, 18 Aug 2023) effective with T+2: trade amendments in the C&S system by 11:30 on settlement date; sufficiency check by 12:00 NN; late cash/securities 12:00–14:00 fined P1,000 + 1/8 of 1% (0.00125) of value; after 14:00 or not at all P1,000 + 1/4 of 1% (0.0025) compounded daily; preventive suspension if not cured by 09:15 on SD+1; MMCD now covers two days of unsettled trades.[^sccp-memo-06-0823-sec-approval-t2-amendments:2][^sccp-memo-06-0823-sec-approval-t2-amendments:3][^sccp-memo-06-0823-sec-approval-t2-amendments:4] SCCP's own site: DVP multilateral net settlement, cleared funds and securities needed "not later than 12:00 noon of settlement date"; cash via net debits/credits to clearing members' accounts at settlement banks; securities by book-entry at the depository (non-immobilised securities must be lodged first).[^sccp-web-services]
- **[P]** Risk tools: Mark-to-Market Collateral Deposit — collateral due by 12:00 noon T+1; eligible collateral = cash, PSEi/DivY/MidCap constituents and PSE shares with **25% haircut (index stocks) / 35% (PSE shares)**; eligible list refreshed by SCCP memo (latest listed 28 Jul 2026).[^sccp-web-services][^sccp-web-home]
- **[P]** New clearing & settlement system ("Millennium Post Trade") went live 27 Mar 2023 and enabled T+2;[^pse-corp-history] SCCP service fees were P165.45M in 1H2026 (+14.5%) on equity trading value of P926.54bn (vs P809.27bn).[^pse-analyst-briefing-1h-2026:7]
- **[P]** SCCP incorporated 23 Jan 1996; membership kit requires PSE TP accreditation, PDTC membership, a Cash Settlement Account and Cash Collateral Deposit Account with the settlement bank, an initial CTGF contribution, a Clearing Member Information Form and signed Master Agreement.[^sccp-web-about-2026-05-17][^sccp-web-membership-2025-09-14]
- **[P]** **Clearing-member roster (SCCP "Clearing Members" search page, Wayback snapshot 14 Sep 2025):** 124 clearing members — 123 ACTIVE, 1 SUSPENDED (Equitiworld, code 153), **0 INACTIVE**; nationality flag Local 113 / Foreign 11 (Apex Philippines Equities 255, CLSA 323, Deutsche Regis Partners 209, HDI Securities 174, J.P. Morgan 185, Macquarie 121, Maybank ATR-Kim Eng 220, Seedbox 365, UBS 333, UOB Kay Hian 260, Yao & Zialcita 275); the codes match the broker codes in PSE's monthly report (e.g. UBS 333, CLSA 323, J.P. Morgan 185, Macquarie 121) **[I]**.[^sccp-web-membership-2025-09-14][^pse-monthly-report-sample:21]
- **[I]** The rulebook posted on sccp.com.ph is still the 13 Mar 2018 text (T+3 language); the in-force T+2 wording exists only in Memo 06-0823 — a reader of the "rulebook" alone gets stale cut-offs.

#### 1.5 PDS Group (PDEx, PDTC) and the PSE take-over
- **[P]** PDS Holdings (PDSHC) owns PDEx (SEC-registered fixed-income securities market and SRO, incorporated 2003), PDTC (depository/registry, incorporated 1995, formerly Philippine Central Depository; **dual SEC + BSP oversight**) and PDS Academy.[^pds-web-company-overview] PDEx has its own Market Governance Board (9 governors incl. 4 independent) and enforcement committee.[^pds-web-market-governance]
- **[P]** **PSE stake timeline:** 2004 PSE invested in PDS Holdings in exchange for its Philippine Central Depository shares;[^pse-corp-history] until Dec 2024 the holding was a 20.98% "associate";[^pse-annual-report-2025:19] an earlier 2017–18 attempt to buy control did not complete — a 16 Apr 2018 Inquirer report (quoted in PSE's 17-C) said the SPA timetable lapsed on 31 Mar 2018 and PSE would stay a ~20% holder **[S]**, which PSE denied having told counterparties (it reaffirmed its aim of unifying fixed income and equities) — and the holding stayed at 20.98%;[^pse-17c-2018-04-16-pds-deal-clarification:3][^pse-annual-report-2025:19] **26 Dec 2024** SPAs/term sheets: BAP 28.8335%, SGX 20%, WTSI 8%, SMC 4%, IHAP 0.65%, Golden Astra 0.3606%, Mizuho 0.08% (board approval 27 Nov 2024; stockholders 6 Jul 2024; SEC 19 Dec 2024), plan "to acquire up to 100%";[^pse-17c-2024-12-26-pdshc-acquisition-agreements:3][^pse-17c-2024-12-26-pdshc-acquisition-agreements:4] the SGX + WTSI + SMC + Golden Astra block (20% + 8% + 4% + 0.36% = 32.36%) closed on 27 Dec 2024 (title of PSE's 17-C list)[^pse-ir-all-disclosures] and the stake (20.98% + 32.36% = 53.34%) was consolidated at end-2024 (goodwill P1,230.90M; P1,213.52M paid for the 32.36%);[^pse-annual-report-2025:19] 78.33% (24 Feb 2025), 79.9% (end-Mar 2025), 91.6% (15 May 2025);[^pse-press-fy2024-results][^pse-press-q1-2025-results] 94.21% after Land Bank's 2.15% (134,372 shares at P600; 22 Dec 2025) **[S]**;[^philstar-pds-landbank-2025-12-24] **94.55% on 4 Feb 2026** after the PDIC purchase (0.34%);[^pse-17c-2026-02-04-pdic-pdshc-shares:3][^pse-annual-report-2025:9] restated 94.55% at 5 Mar 2026.[^pse-analyst-briefing-3m-2026:25] Remaining holder named in the press: DBP (3.08%); PSE says it will pursue the remaining shares in 2026 (target "as high as 97%" **[S]**).[^pse-annual-report-2025:36][^philstar-pds-landbank-2025-12-24] No later stake figure found (1H2026 briefing is silent).
- **[P]** Rationale (17-C): single exchange structure for fixed income + equities; vertical integration of the depository with trading/clearing/settlement; unified venue; risk/ops efficiency; derivatives; integrated surveillance.[^pse-17c-2024-12-26-pdshc-acquisition-agreements:4]
- **[P]** **Integration roadmap** (4 Jul 2026 ASM; 17 Aug 2026 briefing): Phase 1 (ongoing) — 13 systems/platforms identified for consolidation, network/infrastructure consolidation roadmap, working groups, aligned listing/disclosure processes; **Phase 2 (target 2027)** — a *single system for post-trade (clearing & settlement and depository)*, fixed-income assets as acceptable clearing-member collateral, integrated risk/compliance/supervision, broader NoCD coverage.[^pse-asm-2026-president-report:28][^pse-analyst-briefing-1h-2026:31] PDTC is also replacing its depository system ("New Central Depository System for PDTC").[^pse-analyst-briefing-3m-2026:24][^pse-analyst-briefing-3m-2026:25]
- **[P]** Depository stats: assets held in the depository P6.08tn at end-Jun 2026 — equities P5.45tn = **41.9%** of the market value of domestic PSE-listed companies; debt P632bn = 43.0% of debt in the registry; depository revenue 20% of PSE revenue.[^pse-analyst-briefing-1h-2026:18][^pse-analyst-briefing-1h-2026:5] PDS site (PDTC counts dated 1 Oct 2026): 164 registered securities, 42 issuers, 256 depository participants; undated headline values: registry P1.31tn with 282,395 registered holders, P5.59tn of assets in custody with the depository.[^pds-web-home]

#### 1.6 SIPF (Securities Investors Protection Fund, Inc.)
- **[P]** Formally established 2 Oct 1979.[^pse-corp-history] Described by PSE as comparable to the PDIC: protection "automatic upon the opening of an account with a PSE-accredited stockbroker", compensating trade-related obligations of stockbrokers for extraordinary losses from fraud, failure of business or judicial insolvency of a broker.[^pse-web-investing-at-pse] Legal hooks: SRC §36.5 (SEC-supervised trust funds), IRR Rule 36.5 — an "Accredited Trust Fund" compensates customers only for "actual damages" from a broker's business failure/fraud/mismanagement; business failure is determined by the exchange/SRO (or the SEC if they fail to act) without a judicial insolvency declaration (36.5.3); **every broker-dealer must be a member/participant of an Accredited Trust Fund** (36.5.4); the fund keeps a Customer Protection Fund and must have SEC-approved rules on required balance, assessments, borrowing, investment, payout procedure and board composition (36.5.5–36.5.7); IRR Rule 28.1.2.5.1.2 makes participation a registration condition.[^ra-8799-src-lawphil][^sec-2015-src-irr:77][^sec-2015-src-irr:119][^sec-2015-src-irr:120]
- **[P]** In a TP failure the exchange/CMIC notifies the SIPF; SIPF may pay validated claims before the exchange finishes settling the failed TP's liabilities and is subrogated to those claims (CMIC Rules Art. VII §30(c)).[^pse-cmic-rules:56][^pse-cmic-rules:57]
- **Gap:** the per-investor coverage cap and fund size could not be retrieved — sipf.com.ph is a parked domain (ParkLogic redirect) and no PSE/CMIC/SEC document reviewed states the cap.

#### 1.7 BSP and the cash leg
- **[P]** Cash settlement runs through SCCP-accredited **settlement banks** (each clearing member keeps a Cash Settlement Account and a Cash Collateral Deposit Account with one); the SCCP "Business Day" excludes days on which BSP or Philippine Clearing House Corp. clearing is cancelled.[^sccp-clearing-house-rules-2018:4][^sccp-clearing-house-rules-2018:12][^sccp-clearing-house-rules-2018:13] The 2023 C&S system handles PHP and USD cash accounts (USD for dollar-denominated securities) with SWIFT withdrawals.[^sccp-cs-quick-guide:5][^sccp-cs-quick-guide:14] The membership forms in the (2018) rulebook still name RCBC and Equitable-PCI Bank (EPCIB, a legacy name) as the two settlement banks;[^sccp-clearing-house-rules-2018:50][^sccp-clearing-house-rules-2018:60] SCCP's current membership-kit page (archived 14 Sep 2025) lists "Automatic Debit Arrangement (ADA) Enrolment with **BDO or RCBC**", i.e. BDO Unibank and RCBC are the settlement banks today (each bank is connected to the C&S system online in real time; "Partners" page: any depository recognised by SCCP is directly connected).[^sccp-web-membership-2025-09-14][^sccp-web-partners-2025-09-14]
- **[P]** BSP's other roles: dual oversight of PDTC;[^pds-web-company-overview] FX/inward-investment rules for foreign portfolio investors (BSP FX Manual Chapter II: Sections 32–38, 41 — registration with the BSP/BSRD via authorised agent banks, servicing, deposit of peso divestment proceeds).[^bsp-fx-manual-morfxt-2025-05:5]
- **Gap:** no PSE/SCCP document reviewed names **PhilPaSS** (BSP's RTGS) as the inter-bank leg of equity cash settlement. **[I]** settlement banks very likely square positions across banks on PhilPaSS/PCHC, but this is unverified.

#### 1.8 Who does what, order entry → settlement (as in force 6 Oct 2026)
| Step | Actor | What happens | Source |
|---|---|---|---|
| Client order | Client → TP (broker/dealer) | order via TP desk, online front-end (PSETradeX service bureau or own platform) or DMA; TP's own risk checks, per-trader order value limits | [^pse-implementing-guidelines-trading-rules:17][^pse-dma-rules:9] |
| Order entry | TP's PSE-certified FEOMS or PSETradeX terminal → PSE Common Customer Gateway (FIX 5.0 SP1) | one FEOMS log-in per TP; PSE can impose message-flow controls | [^pse-implementing-guidelines-trading-rules:31][^pse-fix-specification-v2-5:7] |
| Matching | PSE trading engine (XTS; Eqlipse planned 23 Nov 2026) | continuous + auction phases; trade feed to SCCP and ITCH feed to vendors | [^pse-web-psetrade-xts][^pse-nte-broker-forum-2026-07-09:9] |
| Surveillance | CMIC (TMS), PSE Market Operations | real-time surveillance; halts; trade amendments/cancellations per rules | [^pse-corp-history][^pse-cmic-rules:11] |
| Clearing | SCCP (CCP) | trade feed after close; netting + novation per clearing member; CTGF/MMCD | [^sccp-clearing-house-rules-2018:26][^sccp-clearing-house-rules-2018:29] |
| Cash instruction | SCCP → settlement banks | Cash List by T+1 business day | [^sccp-clearing-house-rules-2018:29] |
| Settlement (SD = T+2) | PDTC (securities, book-entry) + settlement banks (cash) via SCCP | DVP; funds/securities needed by 12:00 NN; late fines after 12:00; preventive suspension if uncured 09:15 SD+1 | [^sccp-web-services][^sccp-memo-06-0823-sec-approval-t2-amendments:2] |
| Registry/records | PDTC / transfer agents | shares not lodged remain in issuer/transfer-agent books | [^pse-analyst-briefing-1h-2026:18] |
| Oversight/enforcement | SEC > PSE/CMIC/SCCP; SIPF on broker failure; BSP on banks/FX | rule pre-approval, discipline, take-over, compensation | [^pse-corp-regulatory-framework] |

#### 1.9 TP-failure precedents (how the chain behaves under stress)
- **[P]** DW Capital, Inc.: SEC order of 5 Dec 2017 directed PSE to take over its operations; Court of Appeals affirmed 8 Oct 2018 (final 4 Jul 2019); petition pending at the Supreme Court (G.R. 245845) as of FY2025 report.[^pse-annual-report-2025:11][^pse-annual-report-2025:12]
- **[P]** R&L Investments (2023) and **Equitiworld Securities** (suspended; still listed in the directory): CMIC prepares an allocation/liquidation plan for trade-related assets under SEC supervision; SEC approved Equitiworld's multi-tranche allocation plan on 17 Mar 2026 and earlier (9 Jun 2025) approved early release of "intact" shares to clients; clients re-open accounts at active TPs; SIPF claims run in parallel.[^pse-cn-2023-0017:1][^pse-cn-2025-0027:2][^pse-cn-2026-0012:2] Mount Peak Securities is also shown as suspended (no circular found).[^pse-web-tp-directory]

### Inferences
- **[I]** PSE has moved from "exchange + CCP" to a full-stack market infrastructure group; the 2027 single post-trade system will probably change the SCCP–PDTC interfaces, collateral rules (fixed income as collateral) and possibly settlement-bank arrangements; the T+2 rulebook staleness suggests rule-text maintenance lags operational change.
- **[I]** Because rule changes (lot size, tick size, odd-lot, hours, settlement) require SEC prior approval and PSE ties them to the engine cutover, the go-live date is also the effective date of several microstructure changes only if SEC approval arrives first; approval status is the key watch item.

### Gaps
- SIPF coverage cap/fund size; CMIC board composition and independence safeguards; PhilPaSS role in the inter-bank cash leg; whether PCC approvals were needed for the PDS stake; current stake after 4 Feb 2026; the "provisional" qualifier on CMIC's SRO status (FY2025 17-A still says provisional); live (not archived) SCCP settlement-bank/clearing-member lists (sccp.com.ph subpages return 403; Wayback copy of 14 Sep 2025 used).

### Execution implications
- One venue, one CCP, one CSD: there is no venue selection or smart-order routing problem on the Philippine cash equity market; all optimisation is intra-day scheduling and broker selection.
- Your counterparty after novation is SCCP at **clearing-member** level; your exposure to the executing broker/custodian (and its settlement bank) remains — keep assets with a custodian/clearing member that is not a thinly-capitalised TP (see §3) and know the broker-failure process (CMIC/SEC allocation plan; multi-year asset release in the Equitiworld case).
- T+2 cut-offs (12:00 NN on SD for cash/securities, fines from 12:00) and the 41.9% depository coverage of market value mean securities in registry form must be lodged/immobilised before they can be delivered — pre-trade eligibility checks belong in the order workflow.
- Rule-change channel = PSE circulars (CN-yyyy-nnnn) and SCCP memos; effectivity is frequently tied to SEC approval and to the engine cutover — monitor both.

---

## 2. Trading system: product, vendor lineage, architecture, protocols, access, limits, outages, replacement project

### Takeaway
Production engine on 6 Oct 2026 is **PSEtrade XTS = Nasdaq (OMX) X-stream Trading**, live since 22 Jun 2015 (replacing the NYSE Euronext NSC-based "PSEtrade" of 26 Jul 2010), with FIX 5.0 SP1 order entry via a Common Customer Gateway, ITCH-over-SoupBinTCP market data, a PROD+DR pair, PSE-certified broker front-ends (40 TPs run their own) or the PSE-hosted FlexTrade-based PSETradeX service bureau. It is being replaced by **Nasdaq Eqlipse Trading** (contract 22 May 2025) in a big-bang cutover scheduled **Mon 23 Nov 2026**, bundled with One Lot One Share, a negotiated-trade facility and new FIX/ITCH/MDF specifications. No co-location, no published latency, no numeric message-rate limit.

### Cited findings

#### 2.1 Technology lineage
| Date | System | Vendor / note | Source |
|---|---|---|---|
| 4 Jan 1993 | MSE "Stratus Trading System with Equicom" | MSE floor | [^pse-corp-history] |
| 15 Jun 1993 | "MakTrade" (MkSE); 13 Nov 1995 Unified Trading System, single order book on MakTrade software | | [^pse-corp-history] |
| 26 Jul 2010 | "PSEtrade" New Trading System (NTS) — NSC platform | NYSE Euronext Technologies SAS; migration took ~2 years; Implementing Guidelines memo 2010-0340 effective on launch | [^pse-annual-report-2015:42][^pse-implementing-guidelines-trading-rules:1] |
| 2012–13 (vendor change 2017) | **PSETradex** online service bureau/terminal for TPs (introduced 2012 per AR; "launched" Apr 2013 per history) | vendor N2N → **FlexTrade** ("Mottai" terminal) in 2017 (month not stated) | [^pse-annual-report-2025:55][^pse-corp-history][^pse-psetradex-installation-guidelines:9] |
| 29 Oct 2013 | SEC-approved DMA Rules | | [^pse-dma-rules:1] |
| 1 Jul 2014 → 22 Jun 2015 | **PSEtrade XTS** selected (X-stream, "mid-2015") and live | Nasdaq OMX / OMX Technology AB | [^mondovisione-nasdaq-omx-selected-2014] **[S]**; [^pse-annual-report-2015:42] |
| 27 Jun 2022 | trading floors closed 24 Jun 2022; floorless trading from 27 Jun | | [^pse-corp-history] |
| 22 May 2025 | contract with Nasdaq Technology AB for "Nasdaq Eqlipse Trading" (multi-asset engine) | | [^pse-17c-2025-05-22-nasdaq-eqlipse-contract:2] |
| **23 Nov 2026** | planned Eqlipse go-live | big bang, no parallel run | [^pse-nte-broker-forum-2026-07-09:9][^pse-nte-faq-2026-08:1] |

#### 2.2 PSEtrade XTS (in force until cutover)
- **[P]** Go-live 22 Jun 2015 on "NASDAQ's X-stream Trading technology"; replaced the NSC platform of NYSE Euronext Technologies SAS; preparation 11 months vs two years for the previous migration; built with "three times more capacity" than the previous engine; same-day recovery after a failure (previous platform: next trading day).[^pse-annual-report-2015:42][^pse-annual-report-2015:6][^pse-web-psetrade-xts] X-stream was also used by Bursa Malaysia, SGX and the Indonesia exchange.[^pse-annual-report-2015:42] Planned go-live was 1 Jun 2015 (final smoke test 30 May; 6th market rehearsal 23 May) and slipped to 22 Jun; the primary documents reviewed do not give the reason.[^pse-fix-itch-session-week21-2015-05-22:3]
- **[P]** Published capacity: "PSEtrade-XTS Trading Engine can handle **10,000 orders per second**" (PSE session of 22 May 2015); average trades/day rose 39.0% from ~38,000 (2014) to ~53,000 (2015).[^pse-fix-itch-session-week21-2015-05-22:13][^pse-annual-report-2015:8] **No latency figure** is published anywhere reviewed (the ITCH spec only says the protocol suits "low latency messaging").[^pse-itch-equities-feed-spec-v2-3:7]
- **[P]** Features: private order book (orders held off-market and released later) and "unplaced" status for non-day (GTC/GTD) orders outside the static threshold, re-activated next day if inside the new thresholds.[^pse-web-psetrade-xts]
- **[P]** DR: XTS PROD and XTS DR sites; during the 2015 cutover the legacy NSC suite (PAM, CCG, WEP) stayed up in parallel as a fallback with connections disabled; market rehearsals tested the DR site; broker OMS gateways could fail over to the DR addresses only if the TP had a leased line to DR, and the Implementing Guidelines require every TP to keep a back-up terminal connected to the DR site.[^pse-broker-failover-fallback-plan:2][^pse-broker-failover-fallback-plan:3][^pse-broker-failover-fallback-plan:5][^pse-annual-report-2015:44][^pse-implementing-guidelines-trading-rules:30] Leap-second handling in 2015: NTP disabled on trading servers 30 Jun 2015, clock set at 00:00 Manila 1 Jul.[^pse-fix-itch-session-week21-2015-05-22:14]

#### 2.3 Order entry (FIX) — XTS-era specification (PSE FIX Specification v2.5, 10 Aug 2015, OMX Technology AB)
- **[P]** X-stream FIX supports **FIX 5.0 SP1** (DefaultApplVerID=8); first message must be Logon; **no encryption or compression**; password field max 10 chars, username 30.[^pse-fix-specification-v2-5:7][^pse-fix-specification-v2-5:8][^pse-fix-specification-v2-5:11] Heartbeat: Test Request after HeartBtInt + "reasonable time" (≤6 s) and session dropped after 2×HeartBtInt+6 s (HeartBtInt=30 → 66 s); HeartBtInt range is set by the exchange.[^pse-fix-specification-v2-5:11][^pse-fix-specification-v2-5:14]
- **[P]** Messages: New Order Single (D), New Order Cross (s; CrossType must be 1 = AON, limit, IOC), Cancel (F), Cancel/Replace (G), Trade Capture Report (AE) for block/privately negotiated trades; outbound Execution Report (8), Cancel Reject (9), TCR Ack (AR), News (B).[^pse-fix-specification-v2-5:10][^pse-fix-specification-v2-5:16][^pse-fix-specification-v2-5:17] Required fields incl. Account (≤14 chars), ExecutingTrader party (role 12); optional give-up clearing firm (role 14); SecuritySubType: N normal board / O odd-lot board / I index board.[^pse-fix-specification-v2-5:15][^pse-fix-specification-v2-5:47][^pse-fix-specification-v2-5:48]
- **[P]** Enumerations: OrdType 1 Market, 2 Limit, 3 Stop, 4 Stop-Limit; TimeInForce 0 Day, 1 GTC, 3 IOC, 4 FOK, 6 GTD, 8 Session; Side 1 Buy, 2 Sell, 5 Short Sell, Z Buy Back; ExecInst S/q = suspend to / release from private book; MinQty (110) and DisplayQty (1138, hidden/iceberg) exist in the message definition.[^pse-fix-specification-v2-5:16][^pse-fix-specification-v2-5:50][^pse-fix-specification-v2-5:52][^pse-fix-specification-v2-5:53] (Which of these PSE's trading rules actually enable is a trading-rules question — not verified here.)
- **[P]** Order management: ClOrdID ≤20 chars, unique per day and across a firm's FIX connections (X-stream may not check uniqueness); OrderID can change after an amendment; amendable attributes include qty, price, display qty, TIF, account, side (buy↔buy-in, sell↔short-sell); **any price/trigger change or quantity increase loses time priority**; GT orders are restated by unsolicited Execution Reports at start of day, so sequence numbers can jump on logon (use ResendRequest).[^pse-fix-specification-v2-5:9][^pse-fix-specification-v2-5:25][^pse-fix-specification-v2-5:26]
- **[P]** The 2010 Implementing Guidelines add: only one FEOMS log-in per TP; "PSE reserves the right to impose message flow controls for the FEOMS"; only order types offered by the PSE system may be forwarded; PSE may disconnect a FEOMS that harms the system; client list and risk-management procedures must be given to PSE; bureau-service operation of a TP's FEOMS is prohibited; the TP may direct the exchange to cancel all posted orders only after a FEOMS/CCG failure.[^pse-implementing-guidelines-trading-rules:31][^pse-implementing-guidelines-trading-rules:32][^pse-implementing-guidelines-trading-rules:18] (Edition caveat: this posted text is dated 22 Jul 2010; later amendments exist, e.g. TPA 2011-0124 of 28 Dec 2011 for the whole-day trading hours that started in 2012, and the 2025 Part XXI correspondent-TP rules.)[^pse-tpa-2011-0124-amended-implementing-guidelines:1][^pse-annual-report-2025:40]

#### 2.4 Market-data protocols (XTS)
- **[P]** ITCH ("INET ITCH") over **SoupBinTCP v3.0** for point-to-point; MoldUDP64 is specified for one-to-many multicast; usernames/passwords case-sensitive; spec v2.3 dated 5 Oct 2018 (v1.0 19 May 2014); broker anonymity is switchable "as announced by the exchange": if not in force, Order Executed [e], Order Executed with Price [c] and Trade [p] carry the **Broker ID**; if in force, the anonymous variants [E], [C], [P] are sent (the spec does not say which mode PSE runs; PSE publishes broker codes/rankings, so non-anonymous is the likely mode **[I]**).[^pse-itch-equities-feed-spec-v2-3:2][^pse-itch-equities-feed-spec-v2-3:7][^pse-itch-equities-feed-spec-v2-3:22][^pse-itch-equities-feed-spec-v2-3:25] Products: ITCH Total View (every order at every price level), ITCH Basic (best bid/offer + last sale), ITCH News (disclosures/notices), ETF iNAV every minute; more than half of data vendors upgraded to Total View in 2015.[^pse-annual-report-2015:44] The NTE FAQ confirms the current implementation uses separate dedicated TCP connections per feed.[^pse-nte-faq-2026-08:3]

#### 2.5 Access channels
- **FEOMS (broker order-management gateways):** In 2015 ~15 FEOMS were system-certified and 33 TPs launched their own; 5 TPs launched DMA.[^pse-annual-report-2015:44] **40 TPs** have their own FEOMS in the 2026 migration (+ 7 data vendors and 21 TPs consuming market data).[^pse-nte-broker-forum-2026-07-09:5][^pse-nte-broker-forum-2026-07-09:6]
- **PSETradeX** (PSE-hosted service bureau; FlexTrade "Mottai" front-end; Check Point VPN or leased line/drop wire; four "broker silo" servers; white-label web fronts at `*.psetradex.ph`): charges P10,400 per account for the first three and P7,800 for the fourth onward (unit and billing period not stated); **cap of 5,000 accounts per broker**; 2FA replaces RSA token; GTC and next-day validity removed, "GT3 (3 months)" proposed for the cloud version, whose migration "has been deferred"; "VIP accounts" for clients posting their own orders (new price P22,500 on commitments).[^pse-psetradex-installation-guidelines:9][^pse-psetradex-installation-guidelines:17][^pse-nte-broker-forum-2026-07-09:11][^pse-nte-user-group-2026-01-15:17][^pse-active-tp-summary-2026-07-20:1] Terminal minimum: Windows 10 Pro 64-bit, Core i5/8 GB (rec. i7/16 GB), Internet Explorer 11.[^pse-web-new-trading-engine]
- **DMA** (PSE Rules on DMA; SEC letter 29 Oct 2013): Automatic Order Routing (internet or STP) and **Sponsored Access (QIBs only)**; DMA TP must pass PSE system certification (re-certification on significant changes), have a designated + alternate SEC-licensed trader, automated pre-trade risk filters (trade exposure gross/net; order size by value/volume; price limits in % or ticks vs last/adjusted close), 5-year system logs, annual DR test and third-party capacity/penetration test, wash-sale prevention; fees P10,000 setup, P2,500 (re)certification, P10,000 monthly, P5,000 dev-testing (ex-VAT); PSE may disconnect without notice. **§9(e): "The DMA Facility shall not be used for High-Frequency and/or Algorithmic trading"** (HFT defined as sub-second order/cancel intervals).[^pse-dma-rules:2][^pse-dma-rules:3][^pse-dma-rules:5][^pse-dma-rules:6][^pse-dma-rules:7][^pse-dma-rules:8][^pse-dma-rules:9][^pse-dma-rules:10][^pse-dma-sop-guidelines:1]
- **Algorithmic trading status:** CN-2023-0043 (5 Sep 2023, comments to 19 Sep 2023) proposed to move DMA rules into the Revised Trading Rules and allow algo trading: "Programmed or automated Order entry of a Parent Order shall not be allowed" and child orders must be limit orders; TPs must comply before activating algos in the FEOMS or DMA facility; PSE may suspend algos that disrupt the system; the paper records that PSE had already granted exemptions for child orders of conditioned parent orders. I found **no SEC-approval circular** for these algo amendments in the 2023–2026 circulars I could search (only the VWAP part was approved: CN-2024-0010 of 1 Feb 2024; VWAP trading 15:00–15:15 live 1 Mar 2024) and PSE's regulatory-framework page still lists only the 2013 DMA Rules and the VWAP rules.[^pse-cn-2023-0043:3][^pse-cn-2023-0043:6][^pse-cn-2023-0043:7][^pse-cn-2023-0043:8][^pse-asm-2024-presidents-report:24][^pse-corp-history][^pse-web-reg-trading-participants]
- **Online brokers:** PSE lists 22 TPs as "Online Brokers" (AAA Southeast, AB Capital, Abacus, AP Securities, BDO Securities, BPI Securities, China Bank Securities, COL Financial, DragonFi, F. Yap, First Metro, Globalinks, Investors Securities, Landbank Securities, Luna, Mercantile, Philstocks, RCBC Securities, Timson, Unicapital, VC Securities, Wealth Securities); 35 TPs supplied online-account data for 2025.[^pse-web-tp-directory][^pse-smip-2025-infographic:2]
- **Connectivity:** leased lines (PLDT, ETPI, Globe) with Ethernet copper hand-over; drop-wire 100 Mbps for PSE Tower BGC tenants only; leased-line 1 Mbps minimum/2 Mbps recommended (2026 website) and **2 Mbps minimum** for new parallel UAT lines (Jan 2026 deck, lines due May 2026); at least two leased lines (PROD and UAT/DR) per TP; existing PSETradeX lines unchanged.[^pse-web-new-trading-engine][^pse-nte-user-group-2026-01-15:7][^pse-nte-faq-2026-08:2]
- **Co-location/proximity hosting:** none documented in any PSE/XTS/NTE connectivity document; the only proximity feature is the drop-wire for tenants of the PSE building (in 2015: "Ayala Tower 1 tenants").[^pse-web-psetrade-xts][^pse-web-new-trading-engine]
- **Sub-licensing:** access to Eqlipse applications/interfaces and documentation by data vendors and TPs with their own FEOMS requires a sub-licence agreement with PSE (Nasdaq a third-party beneficiary, no Nasdaq liability), a leased line to test and production, and FEOMS re-certification.[^pse-nte-user-group-2026-01-15:4][^pse-nte-user-group-2026-01-15:5] The new FIX specs (Session Gateway, Order Entry, **Drop Copy** — v0.1 30 Jan 2026, v1.1 8 Jun 2026) and ITCH/MDF specs (v1.0 29 Jan, v1.1 8 Jun, **v1.2 17 Jul 2026**) are released only on request by e-mail;[^pse-web-new-trading-engine] "the final specs [were] released last July 23, 2026".[^pse-nte-faq-2026-08:2]

#### 2.6 Throttles / message limits
- **[P]** No numeric order-rate or message-rate limit is published. What exists: PSE's reserved right to impose message-flow controls on a FEOMS (IG XXII.1(h)); one FEOMS session per TP; HeartBtInt bounds set by the exchange; per-trader **value limit per order** (set by the TP, may not exceed the Exchange limit; temporary raises need a form one day ahead; applies per order, not per day); trading cap/trading-floor requirements assigned at broker-code issuance; DMA pre-trade filters; PSETradeX account cap (5,000/broker).[^pse-implementing-guidelines-trading-rules:17][^pse-implementing-guidelines-trading-rules:31][^pse-revised-trading-rules:24][^pse-rules-trading-rights-trading-participants:14][^pse-nte-user-group-2026-01-15:17] Engine capacity claims: 10,000 orders/s (XTS, 2015).[^pse-fix-itch-session-week21-2015-05-22:13]

#### 2.7 Outages and glitches (PSE circulars)
| Date | Event | Source |
|---|---|---|
| 3 Jan 2024 | "Technical issue": market halted 09:32, resumed 11:56 (≈2 h 24 m); afternoon session ran 13:00–15:00 as scheduled; PSE and its "third party front-end system provider" investigating root cause (none published in the circulars reviewed) | [^pse-cn-2024-0001-market-halt:1][^pse-cn-2024-0002:1][^pse-cn-2024-0003-update-market-halt:1] |
| 24 Mar 2025 | Market open delayed by a "system connectivity issue"; adjusted phases: Pre-Open No-Cancel 11:05, Market Open 11:10 (≈1 h 40 m late) | [^pse-cn-2025-0014:1][^pse-cn-2025-0015-adjusted-schedule-2025-03-24:1] |
| 19 Jan 2026 | PSE EDGE disclosure systems inaccessible; "emergency disclosure" procedure, then restored (disclosure system, not trading) | [^pse-cn-2026-0003:1] |
| 19 Mar–29 May 2020 | trading floor closed, off-site trading (COVID quarantine); three-level circuit breaker introduced May 2020 | [^pse-corp-history] |
- **[P]** Rule change after these events: from 20 Aug 2025 the market-wide-halt trigger changed from "at least one-third of TP users cannot access the trading system" to "TPs accounting for >50% of average daily trading value (ex-block sales, prior 6 months) cannot access it", and **every TP must have a Correspondent TP** as business-continuity (Part XXI, IG); new guidelines let PSE halt/suspend/cancel a trading day for natural disasters if the BCP cannot be implemented.[^pse-annual-report-2025:40][^pse-revised-trading-rules:35] Trading-hour extension on a halt of ≥30 min: +30 min (30–50 min halt), +1 h (>50 min) under the original rule.[^pse-revised-trading-rules:35]

#### 2.8 Replacement project: Nasdaq Eqlipse Trading ("PSE Trading Engine 2026")
- **[P]** 22 May 2025 joint press release/17-C: upgrade to Nasdaq's "fourth generation" modular multi-asset platform (pre-trade risk, index calculation, options pricing modules; flexible deployment incl. cloud); PSE "opted to renew its partnership with Nasdaq".[^pse-corp-eqlipse-press-release][^pse-17c-2025-05-22-nasdaq-eqlipse-contract:2] Purposes: single lot size, derivatives, new market-data products and real-time index feeds for fund managers.[^pse-web-new-trading-engine]
- **[S]** Cost P241.03M (engine) + P45.83M (back office); capacity "five million orders and 450,000 trades", 11-hour session, up to 10,000 securities, 15 million client trading accounts, 1,000 brokers, 1,200 market-data connections.[^philstar-nte-2026-07-23]
- **[P]** **Schedule (9 Jul 2026 deck):** customer-test connectivity Jun–Jul 2026; credentials 6–10 Jul (same FIX credentials, different market-data credentials, different ports/IPs; TEST available from 13 Jul); final FIX/ITCH/MDF specs (deck: "3rd week of July"; FAQ: released 23 Jul 2026); **FEOMS certification 10–23 Sep 2026** (earlier on request; later allowed); pre-production connectivity testing 29 Sep–9 Oct; pre-production testing 12–22 Oct; **Saturday market rehearsals 31 Oct, 7 Nov, 14 Nov 2026**; **go-live Mon 23 Nov 2026**; no parallel run ("big bang"); rehearsals in pre-production over new production links with PSE-provided scripts.[^pse-nte-broker-forum-2026-07-09:4][^pse-nte-broker-forum-2026-07-09:9][^pse-nte-faq-2026-08:1][^pse-nte-faq-2026-08:2] The August FAQ adds that the new server IP addresses were "not yet available" and only point-to-point link tests had been completed.[^pse-nte-faq-2026-08:3]
- **[P]** **Readiness at 9 Jul 2026:** of 40 TPs with own FEOMS — 18 analysing/developing FIX, 9 analysing but not developing, 2 no analysis, 11 no response; UAT links: 1 completed, 3 connectivity testing, 3 telco installation, 17 telco discussions, 5 not started, 11 no response. Market data (7 DVs + 21 TPs = 28): spec analysis 19 ongoing/3 not started/6 no response; development 10 ongoing/12 not started/6 no response; UAT connection 2 complete/13 ongoing/7 not started/6 no response.[^pse-nte-broker-forum-2026-07-09:5][^pse-nte-broker-forum-2026-07-09:6]
- **[P]** **Rule/behaviour changes bundled with cutover:** lot size 1 for PHP and USD (DDS) securities, odd-lot market abolished; streamlined tick-size tables (consultation-stage; table below); TPs may impose minimum order values (within the maximum commission); run-off/Trading-at-Last orders may be entered, modified and executed only at the closing price (orders better than the close are now accepted); **Negotiated Trades** (pre-arranged between different clients, price within ±5% of full-day VWAP, 4 decimals, no size limit, 15-minute window after run-off, one-firm trades only, web-based like the VWAP facility, counted in value/CTF and published on the market-data feed as news); **Day-1 order types: limit only**; GTC/next-day validity removed for PSETradeX; DTR end-of-day file removed; new PSE Portal for EOD files (price file, weekly tax report, RBCA), TAGen, trade amendment and unbundling.[^pse-nte-broker-forum-2026-07-09:7][^pse-nte-broker-forum-2026-07-09:8][^pse-nte-broker-forum-2026-07-09:13][^pse-nte-user-group-2026-01-15:9][^pse-nte-user-group-2026-01-15:10][^pse-nte-user-group-2026-01-15:11][^pse-nte-user-group-2026-01-15:17][^pse-nte-user-group-2026-01-15:19][^pse-cn-2025-0046-board-lot-trading-at-last:3][^pse-nte-faq-2026-08:1] SEC approval of the board-lot amendments was still pending on 4 Jul and 17 Aug 2026 ("targeted for Q4 2026 alongside the new trading engine").[^pse-asm-2026-president-report:22][^pse-analyst-briefing-1h-2026:9]
- **[P]** **Board-lot / tick-size change proposed for the cutover (PSE Jan 2026 broker-forum deck; SEC approval pending as of Aug 2026; PHP securities, price ranges in PHP):**

| Price range (PHP) | Current lot | Current tick | Proposed lot | Proposed tick |
|---|---|---|---|---|
| 0.0001–0.0099 | 1,000,000 | 0.0001 | 1 | 0.001 (range "up to 0.099") |
| 0.0100–0.0490 | 100,000 | 0.001 | 1 | 0.001 |
| 0.0500–0.0990 | 10,000 | 0.001 | 1 | 0.001 |
| 0.10–0.2490 | 10,000 | 0.001 | 1 | 0.005 (range 0.10–0.995) |
| 0.2500–0.4950 | 10,000 | 0.005 | 1 | 0.005 |
| 0.50–0.995 | 1,000 | 0.01 | 1 | 0.005 |
| 1–4.99 | 1,000 (to 4.99) | 0.01 | 1 | 0.01 (range 1–9.99) |
| 5–9.99 | 100 | 0.01 | 1 | 0.01 |
| 10–19.98 | 100 | 0.02 | 1 | 0.05 (range 10–99.95) |
| 20–49.95 | 100 | 0.05 | 1 | 0.05 |
| 50–99.95 | 10 | 0.05 | 1 | 0.05 |
| 100–199.90 | 10 | 0.1 | 1 | 0.1 |
| 200–499.80 | 10 | 0.2 | 1 | 0.2 |
| 500–999.50 | 10 | 0.5 | 1 | 0.5 |
| 1,000–1,999 | 5 | 1 | 1 | 1 |
| 2,000–4,998 | 5 | 2 | 1 | 2 |
| ≥5,000 | 5 | 5 | 1 | 5 |

USD (DDS) current: ≤0.99 lot 100/tick 0.01; 1–4.99 lot 20/0.01; 5–9.99 lot 10/0.01; 10–19.98 lot 10/0.02; 20–49.95 lot 10/0.05; 50–99.95 lot 5/0.05; 100–199.90 lot 5/0.10; 200–499.80 lot 5/0.20; 500–999.50 lot 5/0.50; ≥1,000 lot 5/1; proposed lot 1 everywhere with ticks 0.01 (≤9.99), 0.02 (10–19.98), 0.05 (20–99.95), 0.10, 0.20, 0.50, 1.[^pse-nte-user-group-2026-01-15:9][^pse-nte-user-group-2026-01-15:10] (The deck's range boundaries differ between its "current" and "proposed" columns, so rows above merge the two; the boundary rows 0.0500–0.0990 and 0.50–0.995 are my alignment — verify against the final SEC-approved table.)
- **[P]** Other IT projects on the 2026 list: PDTC depository system, CMIC surveillance system, XBRL disclosure platform, SCCP/PDTC post-trade integration (2027); derivatives (PSEi index futures) still at RFI/consultation stage with funding talks.[^pse-analyst-briefing-3m-2026:24][^pse-analyst-briefing-1h-2026:10]
- **Watch item (calendar):** on 25 Sep 2026 PSE issued CN-2026-0043 ("Nov 16–18, 2026 shall be regular trading days") and the same day CN-2026-0044 superseded it, promising a "final advisory" on operations for 16–18 Nov — i.e. the last rehearsal Saturday (14 Nov) falls right before a calendar still being finalised.[^pse-cn-2026-0043:1][^pse-cn-2026-0044:1]

### Inferences
- **[I]** Readiness data (1 of 40 FEOMS TPs had finished connectivity testing by 9 Jul; 11 silent) plus a no-parallel-run big bang make slippage or a phased broker onboarding a live possibility; no PSE postponement notice existed on 6 Oct 2026.
- **[I]** With a single FEOMS session per TP, an exchange-side right to throttle and a 2015 capacity of 10,000 orders/s, practical limits are set by the broker's gateway and 1–2 Mbps leased lines, not by the engine.
- **[I]** DMA §9(e) plus the 2023 algo paper (no approval found) imply that third-party algorithms are tolerated only as broker-side conditioned orders; HFT is excluded.
- **[I]** Cancel-on-disconnect is not documented for XTS (orders remain live; IG allows a mass cancel on request only after FEOMS/CCG failure); whether Eqlipse's Session/Order-Entry gateways add cancel-on-disconnect or kill-switch functions is unknown until the specs are obtained.

### Gaps
- Latency figures; engine/DR site locations; Eqlipse FIX/ITCH/MDF field-level specs (sub-licence required); whether GTC/GTD/stop/market orders return after Day 1; the amended Implementing Guidelines text for CCG/message controls under XTS; root cause of 3 Jan 2024 and 24 Mar 2025 incidents; whether PSE has formally re-confirmed 23 Nov 2026 after the Sept readiness window; SEC decision on board lot/negotiated trades.

### Execution implications
- Build order tracking on **ClOrdID chains** (OrderID may change); every price/trigger change or size-up loses priority; plan replace logic accordingly; expect no encryption on the wire (private lines/VPN only).
- Hard-code nothing about lot/tick/odd-lot: parameterise board-lot and tick tables per security and per engine version; the odd-lot board disappears and One Lot One Share changes minimum order sizes and tick ladders at cutover.
- On Day 1 of Eqlipse only **limit orders** are supported — slicers must not rely on market/stop orders or GTC; use negotiated trades (±5% of VWAP, one-firm) for pre-arranged blocks.
- Do not schedule large programmes around 23 Nov 2026 and the three Saturday rehearsals; confirm your broker's FEOMS certification status and UAT results; expect staggered broker readiness.
- Algorithmic access: assume algos must live in the broker's FEOMS/EMS (conditioned parent, limit child orders) rather than on DMA; ask the broker for its exemption status and PSE's algo-suspension powers.
- Market data: direct subscription requires PSE sub-licence/vendor; ITCH and MDF are separate TCP (SoupBinTCP) sessions per PSE's FAQ (the XTS ITCH spec also defines MoldUDP64 multicast, but nothing reviewed says PSE uses it).
- Stale-order risk: PSE outages in Jan 2024 (≈2.4 h) and Mar 2025 (≈1.7 h late open) show multi-hour interruptions are possible; keep broker-level kill procedures and resume logic (SOD restatement of GT orders, sequence jumps).
- No co-location product exists: latency edge is limited to leased-line quality/broker gateway; do not invest in proximity infrastructure.

---

## 3. Trading Participants (brokers)

### Takeaway
PSE's TP population is small and concentrated: **123 firms** in the public directory (121 active, 2 suspended; all trading rights derive from the original 184 members at demutualisation), 7 flagged foreign-owned, about 22 offering online trading. The on-day top-10 share of turnover is ~65% (5 Oct 2026) and foreign-owned institutional brokers (UBS, Macquarie, CLSA, Maybank) are 4 of the top 6. Legal minimum capital is still **P30M** for grandfathered TPs (P100M for new entrants) and an RBCA/NLC regime; proprietary trading is allowed only under the SEC's "Customer First" policy.

### Cited findings

#### 3.1 Count, status and categories
- **[P]** PSE directory (fetched 6 Oct 2026, no "as of" stamp): 123 TPs — Active 121 (114 local + 7 foreign), Suspended 2 (Equitiworld Securities; Mount Peak Securities); the Public Directory PDFs of 2 Jun and 20 Jul 2026 each list 123 entries including those two.[^pse-web-tp-directory][^pse-active-tp-summary-2026-07-20:1][^pse-active-tp-summary-2026-06-02:1] PSE infographics: **121 active TPs** at end-2024, end-2025 and end-Jun 2026.[^pse-infographic-fy24:1][^pse-infographic-fy25:1][^pse-infographic-2q26:1]
- **[P]** Directory "Type" tally (my count of the 123 rows): Retail 63; Institutional/Retail 29; Institutional 17; Individual/Corporation 2; Individual 2; Foreign/Institutional/Retail 2; Retail/Institutional 1; Retail/Institutional/Online 1; Institutional/Online 1; Individual/Corporate 1; Individual/Institutional/Retail 1; Corporate 1; Retail/Traditional 1; Broker/Dealer 1. "Minimum investment" ranges P0–P1,000,000 (e.g. BDO Securities P500,000; Maybank, Regis Partners, Century, David Go, East West Capital P1M).[^pse-web-tp-directory]
- **[I]** **Churn Sep 2025 → Oct 2026** (comparing SCCP's clearing-member roster archived 14 Sep 2025 — 124 members, 123 active — with the PSE directory of 6 Oct 2026 after renames): exits J.M. Barcelon & Co. (code 188) and JAKA Securities (125); entrant Caballes-Go Securities (typed "Broker/Dealer"); Mount Peak Securities moved from active to suspended; name changes HDI Securities → CNN Securities, Yu & Company → Meta Capital Securities, Deutsche Regis Partners → Regis Partners, Maybank ATR-Kim Eng → Maybank Securities, Salisbury BKT → Salisbury Securities.[^sccp-web-membership-2025-09-14][^pse-web-tp-directory] Net: 124 → 123 firms; SCCP's roster showed zero "INACTIVE" members.
- **[P]** TPs reporting to PSE's annual investor survey: 130 (2022), 123 (2023), 121 active (2024), 122 (2025).[^pse-smip-2022:2][^pse-smip-2023:2][^pse-smip-2024:2][^pse-smip-2025-infographic:2] Original cap: "only one class of Trading Participants... no more than 184".[^pse-rules-trading-rights-trading-participants:7] The directory has no "inactive" status; the rules provide a fee on non-operating trading rights and voluntary suspension/cessation procedures.[^pse-rules-trading-rights-trading-participants:13]

#### 3.2 Trading-right model (Rules Governing Trading Rights and Trading Participants; SEC-approved 28 May 2009, PSE memo 2009-0316 of 18 Jun 2009)
- **[P]** At demutualisation the exchange conferred on each of the 184 members a **trading right** (right to operate as broker/dealer on the Exchange) evidenced by a certificate, "not... a shareholding"; one trading right per TP; **no vote or asset participation**; modifications/new rights need majority TP concurrence; TP must be a domestic corporation licensed by the SEC; admission by ≥8 board votes; entrance fee ≥P200,000; control change ≥51% within 12 months needs Board approval (fee ≥P200,000); each TP appoints a Nominee (≥21, Philippine resident, approved by the Board; fee P50,000; TP liable for nominee) and may not be connected with another TP.[^pse-rules-trading-rights-trading-participants:6][^pse-rules-trading-rights-trading-participants:7][^pse-rules-trading-rights-trading-participants:8][^pse-rules-trading-rights-trading-participants:10][^pse-rules-trading-rights-trading-participants:11][^pse-rules-trading-rights-trading-participants:12]
- **[P]** Trading rights are **transferable by sale** with Board approval, escrow with the Exchange (escrow fee ≥P50,000), SEC/SCCP/PDTC/PSE clearances, 3-newspaper publication and a 30-day claims window; a right of a TP that ceases becomes vacant and reverts to the Board; each TP must **pledge its trading right** (full value) to secure client/government/exchange/SCCP/other-TP claims unless it posts an acceptable guarantee (standby L/C, surety bond, pledge of PSE/index shares or government securities).[^pse-rules-trading-rights-trading-participants:7][^pse-rules-trading-rights-trading-participants:13][^pse-rules-trading-rights-trading-participants:14]
- **[P]** Start of operations needs SEC broker/dealer licence, broker's code and "trading cap" from PSE Market Operations, a **stock-broker bond of P5M and dealer bond of P1M "or such other amount as SEC prescribes"**, ≥1 SEC-licensed associated person and salesman, and trading must start within one year of approval.[^pse-rules-trading-rights-trading-participants:13][^pse-rules-trading-rights-trading-participants:14][^pse-rules-trading-rights-trading-participants:15]

#### 3.3 Capital and prudential rules
- **[P]** Rules text: minimum unimpaired paid-up capital (UPUC) P20M from 31 Dec 2009 and **P30M from 31 Dec 2010 "and onwards"** (Art. III §8(c), as amended by SEC), and the SEC's approval letter (3 Jun 2009) says this "applies only to TPs who opted to defer compliance with the P100 million unimpaired capital requirement"; PSE's July 2026 paper describes the same structure ("an entity applying to be a TP which does not meet the P100 Million... requirement shall have a minimum UPUC of P20M... P30M").[^pse-rules-trading-rights-trading-participants:3][^pse-rules-trading-rights-trading-participants:4][^pse-rules-trading-rights-trading-participants:9][^pse-memo-tp-paid-up-capital-increase-2026-07:3] SEC IRR 28.1.2.5.2(b): P100M for first-time registrants joining a registered clearing agency; deferring existing broker-dealers keep P30M plus a surety bond (Rule 28.1.6: ≥P10M for brokers, ≥P2M for dealers, or SEC-prescribed amount; PSE's July 2026 paper says the current surety bond is P12M).[^sec-2015-src-irr:77][^sec-2015-src-irr:87][^pse-memo-tp-paid-up-capital-increase-2026-07:3]
- **[P]** **Proposal (not in force):** PSE consultation paper CN of 21 Jul 2026 (comments to 31 Jul 2026): ≥P50M UPUC by 31 Dec 2027; surety bond P12M→P20M for TPs not at P100M by 31 Dec 2028; **P100M by 31 Dec 2029**; draft amendment of Art. III §8. No SEC approval or final circular found by 6 Oct 2026.[^pse-memo-tp-paid-up-capital-increase-2026-07:1][^pse-memo-tp-paid-up-capital-increase-2026-07:3][^pse-memo-tp-paid-up-capital-increase-2026-07:4]
- **[P]** RBCA/NLC (SEC MC 16-2004; restated in IRR Rule 49.1): RBCA ratio ≥1.1; **NLC ≥P5M or 5% of aggregate indebtedness, whichever is higher** (P2.5M/2.5% for dealers dealing only in proprietary shares without custody); aggregate indebtedness ≤2,000% of NLC (24-hour notice if >1,700% or RBCA <1.2; dividend/withdrawal limits when NLC <120% of minimum); firm must stop business if RBCA <1.1 or NLC below minimum; daily computation, semi-monthly reports (due the 20th and the 5th); core equity must exceed operational-risk requirement.[^pse-rbca-rules:18][^pse-rbca-rules:19][^pse-rbca-rules:20][^sec-2015-src-irr:166][^sec-2015-src-irr:167] CMIC applies the same thresholds and can place a TP under involuntary suspension for uncured breaches.[^pse-cmic-rules:59][^pse-cmic-rules:106]

#### 3.4 Broker vs dealer, proprietary activity
- **[P]** SRC §34.1 generally bars a member-broker from trading for its own/associated accounts on the exchange except as market maker, odd-lot, error offsets or other cases the SEC defines; IRR Rule 34.1 replaces the flat ban with the **"Customer First" policy**: customer orders executed immediately on receipt, priority over the TP's own orders, order receipt time recorded, all orders executed by the assigned trader on assigned terminals; insiders'/staff accounts are treated as proprietary; a trader may keep one dealing account with the employing TP; "done-through" accounts follow the same policy (34.3).[^ra-8799-src-lawphil][^sec-2015-src-irr:111][^sec-2015-src-irr:112] PSE trader IDs are classified proprietary / client / PC; a market-making TP may not hold a proprietary account in the stock it makes a market in.[^pse-implementing-guidelines-trading-rules:8][^pse-implementing-guidelines-trading-rules:9] CMIC Rules define a "Done Through Account" as an account a TP keeps with another TP to effect transactions for its customers or for its own proprietary account.[^pse-cmic-rules:7]
- **[P]** Directory shows a single firm typed "Broker/Dealer" (Caballes-Go Securities) and the SEC licence distinguishes brokers and dealers (separate bond amounts and NLC floor).[^pse-web-tp-directory][^sec-2015-src-irr:87]
- **Gap:** no published figure for the share of value turnover that is TP proprietary/dealer flow.

#### 3.5 Foreign-owned brokers, online brokers, commissions
- **[P]** Directory "Foreign" flags (7): CLSA Philippines (institutional), J.P. Morgan Securities Philippines (institutional), Macquarie Capital Securities (Philippines) (institutional), Maybank Securities (institutional/retail; the broker-ranking page still shows "Maybank ATR Kim Eng Securities"), UBS Securities Philippines (institutional), UOB-Kay Hian Securities (Philippines) (retail), Seedbox Securities (corporate).[^pse-web-tp-directory] SCCP's roster (Sep 2025) flags **11** members "Foreign" — the same seven plus Apex Philippines Equities, HDI Securities (now CNN Securities), Yao & Zialcita and Deutsche Regis Partners (now Regis Partners, shown Local by PSE) — so the foreign-owned count is 7–11 depending on list, date and ownership definition.[^sccp-web-membership-2025-09-14] TPs must be **domestic corporations** (foreign brokers operate as locally-incorporated subsidiaries); a foreign national may be a Nominee with permits.[^pse-rules-trading-rights-trading-participants:9][^pse-rules-trading-rights-trading-participants:11]
- **[P]** Commissions: SEC MC 7-2024 (16 Apr 2024, effective 18 Apr 2024) removed the PSE minimum-commission schedule (previously 0.25%–0.05% of value) — PD 154's 1.5% ceiling remains; PSE's rule and interpretive guidelines "ceased to be in force" on 18 Apr 2024.[^pse-cn-2024-0029-min-commission-removal:1][^pse-cn-2024-0029-min-commission-removal:2][^pse-cn-2024-0029-min-commission-removal:3] PSE sells a "TP Ranking Report" (P40/issue, P80/quarter, Jan–Mar 2026 rate) alongside weekly/monthly reports.[^pse-cn-2026-0001:1]

#### 3.6 Concentration (value traded, buy + sell)
- **[P]** Single-day snapshot "As of 5 Oct 2026, 15:00" (PSE broker-ranking frame, top-10 only; **[I]** each broker's value counts its buys + sells, so "% to total" is its share of two-sided turnover and all brokers sum to 100%, confirmed by the SCCP one-sided market value below): Mandarin Securities 11.46%; UBS Securities Philippines 8.90%; Macquarie Capital Securities 7.88%; SB Equities 6.51%; CLSA Philippines 6.25%; Maybank ATR Kim Eng 6.00%; COL Financial 5.80% (and 78.8M shares — largest by volume); First Metro Securities 5.04%; Philippine Equity Partners 3.74%; Regis Partners 3.41% → **top-5 41.0%, top-10 64.99%; foreign-owned UBS+Macquarie+CLSA+Maybank = 29.03%**. Market value that day (SCCP site): P3.743bn, 414.3M shares, 70,275 trades (so broker values in the ranking are two-sided).[^pse-web-broker-ranking][^sccp-web-home]
- **[I]** Feb 2020 monthly report (top-25 by value, buy+sell): Salisbury BKT 25.27bn, UBS 25.16bn, CLSA 20.70bn, J.P. Morgan 20.17bn, Credit Suisse 15.56bn, Macquarie 13.73bn, COL 13.46bn, BDO Securities 11.35bn, Maybank ATR Kim Eng 11.18bn, Wealth 9.27bn; with total market value of ≈P132.6bn (6,976.9M ADVT × 19 days) the top-5 ≈40% and top-10 ≈63% of two-sided value; the six foreign-owned firms in the top 10 ≈40%.[^pse-monthly-report-sample:1][^pse-monthly-report-sample:21] (Credit Suisse and the DBP-Daiwa/BDO Nomura JVs no longer appear in the 2026 directory.)
- **[P]** Broker codes appear in market data/monthly reports (examples Feb 2020: Mandarin 200, UBS 333, CLSA 323, J.P. Morgan 185, Macquarie 121, COL 203, BDO Securities 279, Maybank ATR 220, SB Equities 115, Philippine Equity Partners 338, Regis 209, First Metro 267); PSETradeX silo table lists ~130 broker codes (vintage ~2017–19).[^pse-monthly-report-sample:21][^pse-psetradex-installation-guidelines:17][^pse-psetradex-installation-guidelines:18]
- **[P]** Non-regular (block/negotiated etc.) market is ~17% of value: YTD Aug 2026 ADVT P7,561M, of which regular P6,247M and non-regular P1,314M.[^pse-monthly-report-2026-08:1]

### Inferences
- **[I]** Institutional/foreign flow is intermediated by ~6–9 TPs; the long tail of ~110 mostly "Retail"-typed firms handles little value but most accounts. Because ranking is by two-sided value, a block cross between two top brokers counts twice in their shares.
- **[I]** The P100M-by-2029 proposal is aimed at the weakest tail; at P30M the TP capital cushion is small relative to P7.5bn average daily value — a reason to prefer clearing members with large parents (bank-owned or foreign).

### Gaps
- Proprietary/dealer share of turnover; broker-level market-share series for 2024–26 (PSE sells the TP Ranking Report; only a one-day free snapshot found); exact Exchange "value limit per order"; number of non-operating trading rights; current broker-code list.

### Execution implications
- Institutional access is concentrated in a handful of foreign and local-institutional TPs; use at least two and benchmark them with the PSE TP Ranking Report. Retail-oriented online TPs (e.g. COL Financial, First Metro) dominate share-count and trade count but not value.
- Negotiate commissions: minimum commission was abolished 18 Apr 2024 (cap remains 1.5% under PD 154).
- Check the TP's FEOMS certification and Eqlipse UAT status, its RBCA/NLC headroom (SEC reports are not public), and whether it will be affected by the proposed capital increase.
- "Customer First" and CMIC best-execution duty (Art. VII §31) give clients priority over the broker's own book but are not a guarantee of price improvement — document your own TCA against VWAP.

---

## 4. Investor base

### Takeaway
Stock-market accounts have grown from 1.09M (2018) to **3,641,067 (2025)**, 88.6% online and 99.2% retail/99.1% local — yet foreign investors generate ~46–50% of value and institutions ~81% of value; only ~12% of accounts were "active" in 2025. Liquidity is institution- and foreign-driven; retail growth is an account-count story.

### Cited findings
- **[P]** Accounts (PSE Stock Market Investor Profile, year-end; reporting TPs in brackets):

| Year | Total accounts | Online | Online % | Local / Foreign | Retail / Institutional | "Active" % of total accounts | Source |
|---|---|---|---|---|---|---|---|
| 2018 | 1,089,443 | n/a | n/a | n/a | n/a | n/a | [^pse-corp-history] |
| 2021 | 1,620,017 | (>1M online investors) | n/a | n/a | 1,589,507 / 30,510 | n/a | [^pse-smip-2022:2] |
| 2022 [130] | 1,712,734 | 1,258,907 | 73.5% | 1,684,167 / 28,567 (1.7%) | 1,680,572 / 32,162 (1.9%) | 20.2% | [^pse-smip-2022:2][^pse-smip-2022:3] |
| 2023 [123] | 1,906,019 | 1,525,768 | 80.0% | 1,878,304 / 27,715 (1.5%) | 1,877,213 / 28,806 (1.5%) | 17.6% | [^pse-smip-2023:2][^pse-smip-2023:3] |
| 2024 [121] | 2,860,234 | 2,471,860 | 86.4% | 2,830,358 / 29,876 (1.0%) | 2,827,950 / 32,284 (1.1%) | 22.9% | [^pse-smip-2024:2][^pse-smip-2024:3] |
| 2025 [122] | 3,641,067 | 3,226,616 | 88.6% | 3,608,358 / 32,709 (0.9%) | 3,611,157 / 29,910 (0.8%) | 11.8% | [^pse-smip-2025-infographic:2][^pse-smip-2025-infographic:3] |
(2025 figures also in the ASM report: +27.3% y/y; 5-year CAGR 21.1%; online 88.6% = 3,226,616.)[^pse-asm-2026-president-report:15][^pse-analyst-briefing-1h-2026:8] Online accounts were 99.9% retail in 2022–24; 35 TPs reported online data in 2025 (38–39 in 2022–24).[^pse-smip-2025-infographic:2][^pse-smip-2024:2] The infographics do not define "active account".
- **[P]** Retail profile 2024: 50.7% female; ages 18–29 26.5%, 30–44 48.8%, 45–59 17.4%, 60+ 7.3%; Metro Manila 49.3% of total retail accounts; foreign retail nationalities led by Japanese 29.9%, Chinese 19.8%, American 13.0%.[^pse-smip-2024:3][^pse-smip-2024:6][^pse-smip-2024:7]
- **[P]** Value-turnover shares (PSE ASM 2026): **local vs foreign** — 2024 53.8%/46.2%; 2025 53.7%/46.3%; 6M2025 51.7%/48.3%; 6M2026 50.5%/**49.5%**; **retail vs institutional** — 2024 18.9%/81.1%; 2025 18.2%/81.8%; 5M2025 17.2%/82.8%; 5M2026 19.1%/80.9%.[^pse-asm-2026-president-report:7] Monthly report: foreign share 45.0% in Aug 2026, 48.3% YTD vs 46.9% a year earlier.[^pse-monthly-report-2026-08:2] Net foreign selling: P51.20bn (2025), P11.36bn (H1 2026), P20.86bn (Jan–Aug 2026 vs P45.43bn).[^pse-infographic-fy25:1][^pse-infographic-2q26:1][^pse-monthly-report-2026-08:2]
- **[P]** Market scale: average daily value P6.10bn (2024), P7.33bn (2025), P7.72bn (6M2026), P7.56bn (Jan–Aug 2026); market cap P20.01tn / P18.73tn / P19.44tn; listed companies 283 / 282 / 281 (Jun 2026) / 280 (14 Aug 2026).[^pse-asm-2026-president-report:6][^pse-infographic-fy24:1][^pse-infographic-2q26:1][^pse-analyst-briefing-1h-2026:3] Trading days Mon–Fri 09:30–15:00.[^pse-infographic-2q26:1] 2022 avg value per online transaction: P46,236.[^pse-press-smip-2022]
- **[P]** Composition of value, Aug 2026 (average daily, P million): common 7,501.17 of total 7,525.03 (99.7%); preferred 23.47; warrants & PDRs 0.35; dollar-denominated 0.04; ETFs 0.93; SME board 1.41; foreign-incorporated issues 1.56; regular market 5,956.14 vs non-regular 1,568.89 (YTD: 6,247.02 vs 1,314.15).[^pse-monthly-report-2026-08:1]
- **[P]** Drivers: CMEPA (RA 12214) cut the stock transaction tax from 0.6% to 0.1% from 1 Jul 2025; GCash "G-Stocks" with AB Capital (Sep 2022) and other e-wallet/app brokers; PSE's PERA promotion.[^pse-annual-report-2025:39][^pse-corp-history]

### Inferences
- **[I]** If "active" means traded in the year (undefined), active accounts fell from ≈655k (22.9% × 2.86M) in 2024 to ≈430k (11.8% × 3.64M) in 2025 despite +27% account growth: new accounts (largely app/e-wallet) are dormant; retail participation in value stayed ~18–19%.
- **[I]** Foreign accounts (0.9% of accounts) account for ~half of value, so price discovery and index moves are driven by ~33k foreign and ~30k institutional accounts.

### Gaps
- Online vs traditional share of **value** turnover; definition of "active"; institutional split between local/foreign; foreign-investor trading by broker; whether "retail" in the value split includes foreign retail.

### Execution implications
- Participation-rate and impact models should treat roughly half of value as foreign/institutional flow (rising in 2026) and ~80% as institutional; retail flow is a small, noisy residual with intraday seasonality — not a reliable liquidity source for size.
- Net foreign flow (published daily/monthly) is a core alpha/risk factor; foreign share trended up from 46.2% (2024) to 49.5% (6M2026).
- One Lot One Share will lower the minimum ticket and may raise small-order message traffic in expensive stocks (inference), but not institutional liquidity.

---

## 5. Regional links

### Takeaway
PSE is a member of the six-exchange **ASEAN Exchanges** collaboration (Bursa Malaysia, IDX, PSE, SGX, SET, Vietnam Exchange). The **ASEAN Trading Link** (Bursa–SGX from 18 Sep 2012, SET from 15 Oct 2012) never included PSE as far as any PSE document shows; current regional work is sustainability data (ASEAN-ISE), depositary receipts and MOUs — no cross-border order routing for PSE equities.

### Cited findings
- **[P]** ASEAN Exchanges (site, Oct 2026): collaboration of Bursa Malaysia, Indonesia Stock Exchange, Philippine Stock Exchange, SGX, SET and Vietnam Exchange (VNX joined; 39th CEOs Meeting in Vietnam in 2026); PSE hosted the 38th CEOs Meeting on 21 Feb 2025 (Boracay); ASEAN-ISE RFI Feb 2025 (sustainability data infrastructure); **depositary-receipt MOU 21 Nov 2024** (following the SET–SGX DR link).[^aseanexchanges-web-about][^pse-infographic-2q26:1][^pse-annual-report-2025:28][^pse-annual-report-2025:29][^pse-asm-2025-presidents-report:28] PSE's own description: ASEAN Exchanges aims to "develop linkages that would allow investors to trade across borders easily".[^pse-corp-global-alliances]
- **[S]** ASEAN Trading Link launched 18 Sep 2012 with Bursa Malaysia and SGX; SET joined 15 Oct 2012; Wikipedia's account does not mention PSE.[^wikipedia-asean-exchanges] No PSE annual report/ASM deck reviewed (2015, 2024–2026) mentions the ATL.
- **[P]** Other links: FTSE/ASEAN index MoA (2005); the co-branded **SGX-PSE MSCI Philippines Index Futures** was listed on SGX on 25 Nov 2013 (the only Philippine-equity index derivative that PSE's history page or its 2026 briefings mention; whether it still trades, and how actively, was not checked); MOUs with Shenzhen SE (Jan 2023), Taiwan SE (Aug 2024), Taipei Exchange (10 Jun 2025).[^pse-corp-history][^pse-asm-2025-presidents-report:28] PSE's own derivatives market (PSEi index futures first) is still in development: per the 17 Aug 2026 briefing an early exposure draft went to selected institutions, an RFI went to technology vendors "last July" (year not stated), and PSE is "in discussions with multilaterals for possible funding"; no launch date is published.[^pse-analyst-briefing-1h-2026:10]

### Inferences
- **[I]** PSE is not connected to ATL; foreign institutions access PSE through Philippine-incorporated foreign broker subsidiaries or global brokers' local TPs, not through a regional link.

### Gaps
- Primary confirmation (ASEAN Exchanges/ATL documents) of PSE's non-participation or any planned join date.

### Execution implications
- Index-risk hedging: the SGX-listed MSCI Philippines futures are the only exchange-traded route mentioned in PSE's materials (liquidity unchecked); there is no onshore index future until PSE launches one (no date published; project at exposure-draft/RFI/funding stage in Aug 2026) — **[I]** otherwise the onshore hedge is a basket of index constituents (PSE-listed ETFs trade only ~P0.93M a day, Aug 2026, §4), which keeps hedging on the same single venue and T+2 cycle.
- No cross-venue arbitrage or ATL routing exists; DR (depositary receipt) programmes are the only emerging cross-listing channel.

---

## Source catalog

```yaml
- slug: pse-annual-report-2025
  title: "SEC Form 17-A / Annual Report FY2025 (The Philippine Stock Exchange, Inc.)"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: https://documents.pse.com.ph/wp-content/uploads/sites/4/2026/04/2025-Annual-Report.pdf
  local_path: pdfs/pse-annual-report-2025.pdf
  edition: in-force
  amended_through: 2026-03-31
  note: "FY ended 2025-12-31; shareholder data as of 2026-03-31; PDS stake as of 2026-02-04."
- slug: pse-annual-report-2015
  title: "PSE Annual Report 2015 - Ready for Bigger Milestones"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: https://ir.pse.com.ph/wp-content/uploads/sites/4/2020/04/2015-PSE-Annual-Report.pdf
  local_path: pdfs/pse-annual-report-2015.pdf
  edition: historical
  amended_through: undated
  note: "FY2015 report; PSEtrade XTS launch description. File saved by another researcher."
- slug: pse-asm-2026-president-report
  title: "President's Report, Annual Stockholders' Meeting"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: https://documents.pse.com.ph/wp-content/uploads/sites/4/2026/07/PSE-ASM-2026-PRESIDENT_S-REPORT.pdf
  local_path: pdfs/pse-asm-2026-president-report.pdf
  edition: in-force
  amended_through: 2026-07-04
  note: "Cover date 4 Jul 2026; accounts, value shares, rule-amendment status, PDS integration roadmap."
- slug: pse-asm-2025-presidents-report
  title: "President's Report, Annual Stockholders' Meeting 2025"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: https://documents.pse.com.ph/wp-content/uploads/sites/4/2025/07/PSE-ASM-2025-PRESIDENT_S-REPORT-FINAL-v2.pdf
  local_path: pdfs/pse-asm-2025-presidents-report.pdf
  edition: historical
  amended_through: 2025-07-12
  note: "Eqlipse announcement; ASEAN DR collaboration (21 Nov 2024)."
- slug: pse-asm-2024-presidents-report
  title: "President's Report, Annual Stockholders' Meeting 2024"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: https://documents.pse.com.ph/wp-content/uploads/sites/4/2024/07/FINAL_PSE-ASM-2024-PRESIDENT_S-REPORT.pdf
  local_path: pdfs/pse-asm-2024-presidents-report.pdf
  edition: historical
  amended_through: 2024-07-06
  note: "VWAP trading go-live 1 Mar 2024; short-selling programme."
- slug: pse-analyst-briefing-1h-2026
  title: "Philippine Stock Exchange: 1H 2026 Updates (PSE STAR Briefing)"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: https://documents.pse.com.ph/wp-content/uploads/sites/4/2026/08/2026.08.17-PSE-STAR-1H-2026.pdf
  local_path: pdfs/pse-analyst-briefing-1h-2026.pdf
  edition: in-force
  amended_through: 2026-08-17
  note: "Market highlights as of 2026-08-14; depository stats; PDS roadmap."
- slug: pse-analyst-briefing-3m-2026
  title: "PSE Overview / 3M 2026 Analysts' Briefing"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: https://documents.pse.com.ph/wp-content/uploads/sites/4/2026/07/3M-2026-PSE-Analyst-Briefing.pdf
  local_path: pdfs/pse-analyst-briefing-3m-2026.pdf
  edition: in-force
  amended_through: 2026-03-18
  note: "Cover date 18 Mar 2026; PDS stake 94.55% as of 5 Mar 2026; technology upgrades. File saved by another researcher."
- slug: pse-17c-2025-05-22-nasdaq-eqlipse-contract
  title: "SEC Form 17-C: Contract Signing with Nasdaq (Nasdaq Eqlipse Trading)"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: https://documents.pse.com.ph/wp-content/uploads/sites/4/2026/01/17-C-22-May-2025-Contract-Singing-with-Nasdaq-for-Nasdaq-Eqlipse-Trading.pdf
  local_path: pdfs/pse-17c-2025-05-22-nasdaq-eqlipse-contract.pdf
  edition: in-force
  amended_through: 2025-05-22
  note: "Agreement with Nasdaq Technology AB, Inc.; SEC MOU remark on self-listing."
- slug: pse-17c-2024-12-26-pdshc-acquisition-agreements
  title: "SEC Form 17-C: Signing of agreements for the acquisition of Philippine Dealing System Holdings Corp."
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/4/2025/01/17-C-December-26-2024-%E2%80%93-Signing-of-Agreements-for-the-Acquisition-of-Philippine-Dealing-System-Holdings-Corp.pdf"
  local_path: pdfs/pse-17c-2024-12-26-pdshc-acquisition-agreements.pdf
  edition: historical
  amended_through: 2024-12-26
  note: "SPAs/term sheets with BAP, SGX, WTSI, SMC, IHAP, Golden Astra, Mizuho; SEC approval 2024-12-19."
- slug: pse-17c-2026-02-04-pdic-pdshc-shares
  title: "SEC Form 17-C: Agreement with PDIC to purchase PDSHC shares (PSE to beneficially own 94.55%)"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/4/2026/03/17-C-04-February-2026-Signing-of-Agreement-to-purchase-8146-PDSHC-shares-owned-by-PDIC-and-13146-shares-held-by-PDIC-in-trust-for-Export-and-Industry-Bank-Inc.pdf"
  local_path: pdfs/pse-17c-2026-02-04-pdic-pdshc-shares.pdf
  edition: in-force
  amended_through: 2026-02-04
  note: "Browser-printed PDF; p.3 states 94.55%; the filing's regulator-approval line shows a typo (2023)."
- slug: pse-17c-2018-04-16-pds-deal-clarification
  title: "SEC Form 17-C (16 Apr 2018): Clarification of news article 'Bourse backs out of PDS deal'"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: https://documents.pse.com.ph/wp-content/uploads/sites/4/2021/02/17-C-16-April-2018-Clarification-of-news-article-on-PDS-deal.pdf
  local_path: pdfs/pse-17c-2018-04-16-pds-deal-clarification.pdf
  edition: historical
  amended_through: 2018-04-16
  note: "Quotes the Inquirer report (lapse of SPA timetable 31 Mar 2018) and PSE's denial; used for the failed 2017-18 control attempt."
- slug: pse-ir-all-disclosures
  title: "PSE Investor Relations - All Disclosures (SEC 17-A/17-C listing)"
  publisher: The Philippine Stock Exchange, Inc.
  type: web
  canonical_url: https://ir.pse.com.ph/investor-relations/reports-and-disclosures/all-disclosures/
  local_path: null
  edition: in-force
  amended_through: undated
  note: "Fetched 2026-10-06; used only for the titles/dates of 17-C filings (e.g. 27 Dec 2024 closing of SPAs with SGX, WTSI, SMC, Golden Astra)."
- slug: pse-web-reg-trading-participants
  title: "Regulations > Trading Participants (regulatory framework document list)"
  publisher: The Philippine Stock Exchange, Inc.
  type: web
  canonical_url: https://www.pse.com.ph/regulation-trading-participants/
  local_path: null
  edition: in-force
  amended_through: undated
  note: "Fetched 2026-10-06; lists Revised Trading Rules, DMA Rules (2013), TP Rules (2009), SCCP/CMIC rules, VWAP rules (2024), RBCA rules, min-commission removal (CN-2024-0029); no algorithmic-trading rule."
- slug: pse-nte-broker-forum-2026-07-09
  title: "New Trading Engine, PSETradeX, PSE Back-office Updates - Broker Forum (9 Jul 2026)"
  publisher: The Philippine Stock Exchange, Inc. (Market Operations Division)
  type: pdf
  canonical_url: https://documents.pse.com.ph/wp-content/uploads/sites/15/2026/07/PSE-New-Trading-Engine-TradeX-Back-office_Broker-Forum_07092026-1.pdf
  local_path: pdfs/pse-nte-broker-forum-2026-07-09.pdf
  edition: in-force
  amended_through: 2026-07-09
  note: "Project schedule, readiness counts, negotiated-trade features, PSETradeX charges."
- slug: pse-nte-user-group-2026-01-15
  title: "New Trading Engine, PSETradeX, PSE Back-office Updates - Broker Forum (15 Jan 2026)"
  publisher: The Philippine Stock Exchange, Inc. (Market Operations Division)
  type: pdf
  canonical_url: https://documents.pse.com.ph/wp-content/uploads/sites/15/2026/06/NTE-User-Group.pdf
  local_path: pdfs/pse-nte-user-group-2026-01-15.pdf
  edition: in-force
  amended_through: 2026-01-15
  note: "Date from the PSE page listing (deck itself undated); lot/tick tables are proposals."
- slug: pse-nte-faq-2026-08
  title: "Frequently Asked Questions - New Trading Engine / PSE Back-Office / PSETradeX / Market Data"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: https://documents.pse.com.ph/wp-content/uploads/sites/15/2026/08/Frequent-Asked-Questions.pdf
  local_path: pdfs/pse-nte-faq-2026-08.pdf
  edition: in-force
  amended_through: undated
  note: "Published Aug 2026 per upload path; refers to data from 3 Aug 2026 and to specs released 23 Jul 2026."
- slug: pse-cn-2025-0046-board-lot-trading-at-last
  title: "CN-2025-0046 Proposed amendments to the PSE Board Lot and rule on Trading during Run-Off/Trading-at-Last (consultation paper)"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: https://documents.pse.com.ph/CircularOPSPDF/CN-2025-0046.pdf
  local_path: pdfs/pse-cn-2025-0046-board-lot-trading-at-last.pdf
  edition: n/a
  amended_through: 2025-12-15
  note: "Consultation paper (comments to 2025-12-31); not rule text in force."
- slug: pse-fix-specification-v2-5
  title: "PSE FIX Specification for X-stream v2.5 (FIX 5.0 SP1)"
  publisher: OMX Technology AB (Nasdaq OMX) for PSE
  type: pdf
  canonical_url: https://documents.pse.com.ph/wp-content/uploads/sites/15/2021/01/PSE_FIX_Specification_v2_5-10-August-2015.pdf
  local_path: pdfs/pse-fix-specification-v2-5.pdf
  edition: in-force
  amended_through: 2015-08-10
  note: "Specification for PSEtrade XTS; in force until the Eqlipse cutover (planned 2026-11-23). New-engine FIX specs are not public."
- slug: pse-itch-equities-feed-spec-v2-3
  title: "PSE Equities Feed (ITCH) Specification for X-stream v2.3"
  publisher: OMX Technology AB (Nasdaq OMX) for PSE
  type: pdf
  canonical_url: https://www.pse.com.ph/psetrade-xts/
  local_path: pdfs/pse-itch-equities-feed-spec-v2-3.pdf
  edition: in-force
  amended_through: 2018-10-05
  note: "XTS-era ITCH spec saved by another researcher; PSE's XTS page (landing page given) lists versions only up to v2.2 (19 Mar 2015), so the v2.3 file URL was not recorded."
- slug: pse-fix-itch-session-week21-2015-05-22
  title: "Session on FIX and ITCH - Week 21 (22 May 2015)"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: https://documents.pse.com.ph/wp-content/uploads/sites/15/2021/01/Session-on-FIX-and-ITCH-week21.pdf
  local_path: pdfs/pse-fix-itch-session-week21-2015-05-22.pdf
  edition: historical
  amended_through: 2015-05-22
  note: "States XTS engine capacity of 10,000 orders per second; planned 1 Jun go-live."
- slug: pse-broker-failover-fallback-plan
  title: "PSE Failover and Fallback Plan (XTS cutover)"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: https://documents.pse.com.ph/wp-content/uploads/sites/15/2021/01/Broker-Fail-over-and-Fall-back-Plan.pdf
  local_path: pdfs/pse-broker-failover-fallback-plan.pdf
  edition: historical
  amended_through: undated
  note: "2015 cutover plan: XTS PROD/DR and NSC fallback. Contains private IP addresses (not reproduced)."
- slug: pse-psetradex-installation-guidelines
  title: "PSETradex Installation Guidelines (FlexTrade/Mottai terminal; broker silo distribution)"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: https://documents.pse.com.ph/wp-content/uploads/sites/15/2021/01/PSETradex-Installation-Guidelines8536.pdf
  local_path: pdfs/pse-psetradex-installation-guidelines.pdf
  edition: in-force
  amended_through: undated
  note: "Listed on the PSE trading-engine pages as current; broker table vintage ~2017-19."
- slug: pse-implementing-guidelines-trading-rules
  title: "Implementing Guidelines of the Revised Trading Rules (memo 2010-0340, 22 Jul 2010)"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: https://documents.pse.com.ph/wp-content/uploads/sites/15/2021/04/Implementing-Guidelines-of-the-Revised-Trading-Rules.pdf
  local_path: pdfs/pse-implementing-guidelines-trading-rules.pdf
  edition: superseded
  amended_through: 2010-07-22
  note: "Original text effective with NTS launch 2010-07-26; later amended (2011, 2025 Part XXI). Saved by another researcher."
- slug: pse-revised-trading-rules
  title: "Revised Trading Rules (2010; scanned)"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: https://documents.pse.com.ph/wp-content/uploads/sites/15/2021/04/Revised-Trading-Rules.pdf
  local_path: pdfs/pse-revised-trading-rules.pdf
  edition: superseded
  amended_through: undated
  note: "Image-only PDF (memo 2010-0275); Art. VIII s.2 halt trigger amended 20 Aug 2025. Saved by another researcher; pages cited from my OCR."
- slug: pse-tpa-2011-0124-amended-implementing-guidelines
  title: "Amended sections of the Implementing Guidelines of the Revised Trading Rules (TPA 2011-0124)"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: https://documents.pse.com.ph/wp-content/uploads/sites/15/2024/08/2_Amended-IRR_TPA_2011-0124.pdf
  local_path: pdfs/pse-tpa-2011-0124-amended-implementing-guidelines.pdf
  edition: in-force
  amended_through: undated
  note: "Existence of 2011 amendments to the Implementing Guidelines (not read in detail for this chapter)."
- slug: pse-rules-trading-rights-trading-participants
  title: "Rules Governing Trading Rights and Trading Participants (PSE memo 2009-0316; SEC approval 28 May 2009; scanned)"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: https://documents.pse.com.ph/wp-content/uploads/sites/15/2021/04/Rules-Governing-Trading-Rights-and-Trading-Participants.pdf
  local_path: pdfs/pse-rules-trading-rights-trading-participants.pdf
  edition: in-force
  amended_through: 2009-06-18
  note: "Image-only PDF; text read via OCR. Capital article amendment proposed 2026-07-21 (not in force)."
- slug: pse-memo-tp-paid-up-capital-increase-2026-07
  title: "Proposed increase in the minimum unimpaired paid-up capital of PSE Trading Participants (consultation paper)"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: https://documents.pse.com.ph/wp-content/uploads/sites/15/2026/07/Memo-to-Public_Proposed-Increase-in-the-Unimpaired-Paid-Up-Capital-of-TP-1.pdf
  local_path: pdfs/pse-memo-tp-paid-up-capital-increase-2026-07.pdf
  edition: n/a
  amended_through: 2026-07-21
  note: "Proposal only; comments to 2026-07-31; no approval found by 2026-10-06."
- slug: pse-dma-rules
  title: "PSE Rules on Direct Market Access (DMA) with SEC transmittal of 29 Oct 2013 (scanned)"
  publisher: The Philippine Stock Exchange, Inc. / SEC
  type: pdf
  canonical_url: https://documents.pse.com.ph/wp-content/uploads/sites/15/2021/04/SEC-Approved-DMA-Rules.pdf
  local_path: pdfs/pse-dma-rules.pdf
  edition: in-force
  amended_through: 2013-10-29
  note: "Image-only PDF read visually; s.9(e) prohibits HFT/algorithmic trading via DMA Facility. 2023 proposal to amend not found approved."
- slug: pse-dma-sop-guidelines
  title: "DMA Rules Annex A: Guidelines on Written Policies and Procedures for DMA TPs"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: https://documents.pse.com.ph/wp-content/uploads/sites/15/2021/04/Annex-A_Guidelines-on-Written-SOPs-for-DMATPs.pdf
  local_path: pdfs/pse-dma-sop-guidelines.pdf
  edition: in-force
  amended_through: undated
  note: "Two-page annex; certification by Nominee of DMA SOPs."
- slug: pse-cn-2023-0043
  title: "CN-2023-0043 Proposed amendments to the Revised Trading Rules re algorithmic trading and VWAP trading (consultation paper)"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: https://documents.pse.com.ph/CircularOPSPDF/CN-2023-0043.pdf
  local_path: pdfs/pse-cn-2023-0043.pdf
  edition: n/a
  amended_through: 2023-09-05
  note: "Consultation; VWAP part later approved (CN-2024-0010); algo part approval not found. Saved by another researcher."
- slug: pse-rbca-rules
  title: "SEC Memorandum Circular No. 16 s.2004 - Risk Based Capital Adequacy requirement for broker dealers (scanned)"
  publisher: Securities and Exchange Commission (posted by PSE)
  type: pdf
  canonical_url: https://documents.pse.com.ph/wp-content/uploads/sites/15/2021/04/RBCA-Rules.pdf
  local_path: pdfs/pse-rbca-rules.pdf
  edition: in-force
  amended_through: 2004-12-31
  note: "Image-only PDF; year from circular series; restated in 2015 SRC IRR Rule 49.1."
- slug: pse-cmic-rules
  title: "Capital Markets Integrity Corporation Rules v1.2 (15 Dec 2011) with SEC approval letters (scanned)"
  publisher: Capital Markets Integrity Corporation / PSE
  type: pdf
  canonical_url: https://documents.pse.com.ph/wp-content/uploads/sites/15/2021/04/Approved-CMIC-Rules-2.pdf
  local_path: pdfs/pse-cmic-rules.pdf
  edition: in-force
  amended_through: 2012-02-23
  note: "Image-only PDF read via OCR; PSE memo 23 Feb 2012; later amendments not located."
- slug: sccp-clearing-house-rules-2018
  title: "Revised Clearinghouse Rules of the Securities Clearing Corporation of the Philippines (revised 13 Mar 2018)"
  publisher: Securities Clearing Corporation of the Philippines
  type: pdf
  canonical_url: https://www.sccp.com.ph/resources/files/rules/SCCP_Revised_Rules_-_Approved_by_the_SEC_031318.pdf
  local_path: pdfs/sccp-clearing-house-rules-2018.pdf
  edition: superseded
  amended_through: 2018-03-13
  note: "Still the version on sccp.com.ph; T+3 text superseded by SEC-approved T+2 amendments (memo 06-0823)."
- slug: sccp-clearing-house-operating-procedures-2018
  title: "Revised Clearinghouse Operating Procedures of SCCP (revised 13 Mar 2018)"
  publisher: Securities Clearing Corporation of the Philippines
  type: pdf
  canonical_url: https://www.sccp.com.ph/resources/files/rules/SCCP_Revised_OpProcs_-_Approved_by_the_SEC_031318.pdf
  local_path: pdfs/sccp-clearing-house-operating-procedures-2018.pdf
  edition: superseded
  amended_through: 2018-03-13
  note: "Saved by another researcher."
- slug: sccp-memo-06-0823-sec-approval-t2-amendments
  title: "SCCP Memo 06-0823: SEC approval of T+2-related amendments to SCCP Rules and Operating Procedures"
  publisher: Securities Clearing Corporation of the Philippines
  type: pdf
  canonical_url: "https://sccp.com.ph/resources/files/memos/2023/06-0823%20Announcement%20of%20SEC%20Approval%20of%20T+2-Related%20Amendments%20to%20the%20SCCP%20Rules%20and%20Operating%20Procedures.pdf"
  local_path: pdfs/sccp-memo-06-0823-sec-approval-t2-amendments.pdf
  edition: in-force
  amended_through: 2023-08-18
  note: "Effective 2023-08-24 (T+2). Copy archived from the Wayback snapshot of 2023-11-29 (live sccp.com.ph memos page returns 403)."
- slug: pse-cn-2023-0031-t2-settlement
  title: "CN-2023-0031 Migration to the T+2 settlement cycle (with SCCP Memo 01-0623)"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: https://documents.pse.com.ph/CircularOPSPDF/CN-2023-0031.pdf
  local_path: pdfs/pse-cn-2023-0031-t2-settlement.pdf
  edition: historical
  amended_through: 2023-06-23
  note: "Saved by another researcher."
- slug: sccp-cs-quick-guide
  title: "SCCP Clearing & Settlement Quick Guide v1.0 (new C&S system)"
  publisher: Securities Clearing Corporation of the Philippines
  type: pdf
  canonical_url: https://www.sccp.com.ph/resources/files/rules/New_CS_System_Quick_Guide.pdf
  local_path: pdfs/sccp-cs-quick-guide.pdf
  edition: in-force
  amended_through: 2023-03-31
  note: "Release date March 2023 (day not stated)."
- slug: sec-2015-src-irr
  title: "2015 Implementing Rules and Regulations of the Securities Regulation Code"
  publisher: Securities and Exchange Commission
  type: pdf
  canonical_url: https://www.sec.gov.ph/
  local_path: pdfs/sec-2015-src-irr.pdf
  edition: in-force
  amended_through: 2015-11-09
  note: "Effective 9 Nov 2015 per SEC notice; the archived copy was saved by another researcher and its exact file URL was not recorded (sec.gov.ph blocks automated clients); landing page given."
- slug: sec-2015-src-irr-notice-of-effectivity
  title: "SEC Notice: Effectivity of the 2015 SRC Rules on 9 Nov 2015"
  publisher: Securities and Exchange Commission
  type: pdf
  canonical_url: https://appointment.sec.gov.ph/wp-content/uploads/2019/11/2015-SRC-Rules-Notice-of-Effectivity-of-SRC-IRR-Nov-09-2015.pdf
  local_path: pdfs/sec-2015-src-irr-notice-of-effectivity.pdf
  edition: in-force
  amended_through: 2015-11-05
  note: "Notice dated 5 Nov 2015."
- slug: ra-8799-src-lawphil
  title: "Republic Act No. 8799 - The Securities Regulation Code"
  publisher: Lawphil Project (Arellano Law Foundation)
  type: web
  canonical_url: https://lawphil.net/statutes/repacts/ra2000/ra_8799_2000.html
  local_path: null
  edition: in-force
  amended_through: undated
  note: "Statute text as published on lawphil (signed 19 Jul 2000, effective 8 Aug 2000 per PSE history); amendments not tracked."
- slug: pse-cn-2024-0029-min-commission-removal
  title: "CN-2024-0029 Removal of minimum commission charges (with SEC MC 7 s.2024)"
  publisher: The Philippine Stock Exchange, Inc. / SEC
  type: pdf
  canonical_url: https://documents.pse.com.ph/wp-content/uploads/sites/15/2024/09/Removal-of-Minimum-Commission-Chanrges_CN-2024-0029.pdf
  local_path: pdfs/pse-cn-2024-0029-min-commission-removal.pdf
  edition: in-force
  amended_through: 2024-05-17
  note: "SEC MC 7-2024 dated 2024-04-16, effective 2024-04-18 (annex)."
- slug: pse-cn-2024-0001-market-halt
  title: "CN-2024-0001 Market halt (3 Jan 2024)"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: https://documents.pse.com.ph/CircularOPSPDF/CN-2024-0001.pdf
  local_path: pdfs/pse-cn-2024-0001-market-halt.pdf
  edition: historical
  amended_through: 2024-01-03
  note: "Saved by another researcher."
- slug: pse-cn-2024-0002
  title: "CN-2024-0002 Market resumption (3 Jan 2024, 11:56)"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: https://documents.pse.com.ph/CircularOPSPDF/CN-2024-0002.pdf
  local_path: pdfs/pse-cn-2024-0002.pdf
  edition: historical
  amended_through: 2024-01-03
  note: ""
- slug: pse-cn-2024-0003-update-market-halt
  title: "CN-2024-0003 Update on the market halt (3 Jan 2024)"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: https://documents.pse.com.ph/CircularOPSPDF/CN-2024-0003.pdf
  local_path: pdfs/pse-cn-2024-0003-update-market-halt.pdf
  edition: historical
  amended_through: 2024-01-03
  note: "Saved by another researcher."
- slug: pse-cn-2025-0014
  title: "CN-2025-0014 Delay in market open (24 Mar 2025, system connectivity issue)"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: https://documents.pse.com.ph/CircularOPSPDF/CN-2025-0014.pdf
  local_path: pdfs/pse-cn-2025-0014.pdf
  edition: historical
  amended_through: 2025-03-24
  note: ""
- slug: pse-cn-2025-0015-adjusted-schedule-2025-03-24
  title: "CN-2025-0015 Adjusted trading schedule for 24 Mar 2025"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: https://documents.pse.com.ph/CircularOPSPDF/CN-2025-0015.pdf
  local_path: pdfs/pse-cn-2025-0015-adjusted-schedule-2025-03-24.pdf
  edition: historical
  amended_through: 2025-03-24
  note: "Saved by another researcher."
- slug: pse-cn-2026-0003
  title: "CN-2026-0003 PSE EDGE systems now accessible (19 Jan 2026)"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: https://documents.pse.com.ph/CircularOPSPDF/CN-2026-0003.pdf
  local_path: pdfs/pse-cn-2026-0003.pdf
  edition: historical
  amended_through: 2026-01-19
  note: "Disclosure-system outage, not trading engine."
- slug: pse-cn-2023-0017
  title: "CN-2023-0017 R&L Investments, Inc. allocation plan (CMIC notice)"
  publisher: The Philippine Stock Exchange, Inc. / CMIC
  type: pdf
  canonical_url: https://documents.pse.com.ph/CircularOPSPDF/CN-2023-0017.pdf
  local_path: pdfs/pse-cn-2023-0017.pdf
  edition: historical
  amended_through: 2023-04-04
  note: ""
- slug: pse-cn-2025-0027
  title: "CN-2025-0027 Updates on Equitiworld Securities, Inc. (CMIC Memorandum 2025-019)"
  publisher: The Philippine Stock Exchange, Inc. / CMIC
  type: pdf
  canonical_url: https://documents.pse.com.ph/CircularOPSPDF/CN-2025-0027.pdf
  local_path: pdfs/pse-cn-2025-0027.pdf
  edition: historical
  amended_through: 2025-06-11
  note: ""
- slug: pse-cn-2026-0012
  title: "CN-2026-0012 Updates on Equitiworld Securities, Inc. (CMIC Memorandum 2026-006)"
  publisher: The Philippine Stock Exchange, Inc. / CMIC
  type: pdf
  canonical_url: https://documents.pse.com.ph/CircularOPSPDF/CN-2026-0012.pdf
  local_path: pdfs/pse-cn-2026-0012.pdf
  edition: in-force
  amended_through: 2026-03-19
  note: "SEC approved the allocation plan on 2026-03-17."
- slug: pse-cn-2026-0001
  title: "CN-2026-0001 Subscription to PSE Reports for 2026 (incl. TP Ranking Report prices)"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: https://documents.pse.com.ph/CircularOPSPDF/CN-2026-0001.pdf
  local_path: pdfs/pse-cn-2026-0001.pdf
  edition: in-force
  amended_through: 2026-01-08
  note: ""
- slug: pse-cn-2026-0043
  title: "CN-2026-0043 Regular trading days (16-18 Nov 2026)"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: https://documents.pse.com.ph/CircularOPSPDF/CN-2026-0043.pdf
  local_path: pdfs/pse-cn-2026-0043.pdf
  edition: superseded
  amended_through: 2026-09-25
  note: "Superseded the same day by CN-2026-0044."
- slug: pse-cn-2026-0044
  title: "CN-2026-0044 Trading day advisory (16-18 Nov 2026)"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: https://documents.pse.com.ph/CircularOPSPDF/CN-2026-0044.pdf
  local_path: pdfs/pse-cn-2026-0044.pdf
  edition: in-force
  amended_through: 2026-09-25
  note: "Promises an updated final advisory on 16-18 Nov operations."
- slug: pse-smip-2025-infographic
  title: "Stock Market Investor Profile 2025 (infographic)"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: https://documents.pse.com.ph/wp-content/uploads/sites/15/2026/05/2025-SMIP-Infographic.pdf
  local_path: pdfs/pse-smip-2025-infographic.pdf
  edition: in-force
  amended_through: 2026-05-29
  note: "Upload date per PSE Market Reports list."
- slug: pse-smip-2024
  title: "Stock Market Investor Profile 2024"
  publisher: The Philippine Stock Exchange, Inc. (Corporate Planning and Research Dept.)
  type: pdf
  canonical_url: https://documents.pse.com.ph/wp-content/uploads/sites/15/2025/06/Stock-Market-Investor-Profile-2024-.pdf
  local_path: pdfs/pse-smip-2024.pdf
  edition: historical
  amended_through: 2025-05-31
  note: "Cover 'May 2025' (day not stated); PSE list shows posting 2025-06-09."
- slug: pse-smip-2023
  title: "Stock Market Investor Profile 2023"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: https://documents.pse.com.ph/wp-content/uploads/sites/15/2024/05/Stock-Market-Investor-Profile-2023.pdf
  local_path: pdfs/pse-smip-2023.pdf
  edition: historical
  amended_through: 2024-05-31
  note: "Cover 'May 2024'."
- slug: pse-smip-2022
  title: "Stock Market Investor Profile 2022"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: https://documents.pse.com.ph/wp-content/uploads/sites/15/2023/05/Stock-Market-Investor-Profile-2022.pdf
  local_path: pdfs/pse-smip-2022.pdf
  edition: historical
  amended_through: 2023-05-31
  note: "Cover 'May 2023'."
- slug: pse-active-tp-summary-2026-07-20
  title: "Active Trading Participants - Public Directory as of July 20, 2026"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: https://documents.pse.com.ph/wp-content/uploads/sites/15/2026/07/Active-TP-Summary-Website_July-20_-2026.pdf
  local_path: pdfs/pse-active-tp-summary-2026-07-20.pdf
  edition: in-force
  amended_through: 2026-07-20
  note: "123 entries incl. two suspended firms."
- slug: pse-active-tp-summary-2026-06-02
  title: "Active Trading Participants - Public Directory as of June 2, 2026"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: https://documents.pse.com.ph/wp-content/uploads/sites/15/2026/06/Active-TP-Summary-Website_June-2_-2026.pdf
  local_path: pdfs/pse-active-tp-summary-2026-06-02.pdf
  edition: superseded
  amended_through: 2026-06-02
  note: "123 entries."
- slug: pse-monthly-report-sample
  title: "PSE Monthly Report, February 2020"
  publisher: The Philippine Stock Exchange, Inc. (Market Data Department)
  type: pdf
  canonical_url: "https://documents.pse.com.ph/market_report/February%202020-MR.pdf"
  local_path: pdfs/pse-monthly-report-sample.pdf
  edition: historical
  amended_through: 2020-02-29
  note: "Full 46-page report incl. top-25 brokers (saved by another researcher; URL taken from PSE's Market Reports list). Monthly reports from 2021 onward are 2-page previews only."
- slug: pse-monthly-report-2026-08
  title: "PSE Monthly Report, August 2026 (preview)"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: https://documents.pse.com.ph/wp-content/uploads/sites/15/2026/09/08-2026_PSE-Monthly-Report_Preview.pdf
  local_path: pdfs/pse-monthly-report-2026-08.pdf
  edition: in-force
  amended_through: 2026-08-31
  note: "Preview; posted 2026-09-30."
- slug: pse-infographic-fy24
  title: "PSE FY2024 Stock Market Infographic"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: https://documents.pse.com.ph/wp-content/uploads/sites/15/2025/01/FY24-Infographic-v3-clean.pdf
  local_path: pdfs/pse-infographic-fy24.pdf
  edition: historical
  amended_through: 2024-12-31
  note: "URL as listed by PSE search result; saved by another researcher."
- slug: pse-infographic-fy25
  title: "PSE FY2025 Stock Market Infographic"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: https://documents.pse.com.ph/wp-content/uploads/sites/15/2026/01/FY25-Infographic.pdf
  local_path: pdfs/pse-infographic-fy25.pdf
  edition: historical
  amended_through: 2025-12-31
  note: ""
- slug: pse-infographic-2q26
  title: "PSE 2Q26 Stock Market Infographic (end-June 2026)"
  publisher: The Philippine Stock Exchange, Inc.
  type: pdf
  canonical_url: https://documents.pse.com.ph/wp-content/uploads/sites/15/2026/07/2Q26-Infographic.pdf
  local_path: pdfs/pse-infographic-2q26.pdf
  edition: in-force
  amended_through: 2026-06-30
  note: ""
- slug: pse-weekly-market-watch-2026-10-02
  title: "PSE Weekly Market Watch, 28 Sep - 2 Oct 2026 (Vol. XVI No. 40)"
  publisher: The Philippine Stock Exchange, Inc. (Market Data Department)
  type: pdf
  canonical_url: https://documents.pse.com.ph/wp-content/uploads/sites/15/2026/10/wk40_oct2026mktwatch.pdf
  local_path: pdfs/pse-weekly-market-watch-2026-10-02.pdf
  edition: in-force
  amended_through: 2026-10-02
  note: "Used only for the 2 Oct 2026 PSEi close/YTD and market capitalisation."
- slug: bsp-fx-manual-morfxt-2025-05
  title: "BSP Manual of Regulations on Foreign Exchange Transactions (MORFXT), May 2025"
  publisher: Bangko Sentral ng Pilipinas
  type: pdf
  canonical_url: https://www.bsp.gov.ph/
  local_path: pdfs/bsp-fx-manual-morfxt-2025-05.pdf
  edition: in-force
  amended_through: 2025-05-31
  note: "Saved by another researcher (file URL not recorded; bsp.gov.ph blocks automated clients); only the table of contents (Chapter II inward investments) used here."
- slug: pse-web-new-trading-engine
  title: "PSE New Trading Engine (Trading > PSE Trading Engine 2026)"
  publisher: The Philippine Stock Exchange, Inc.
  type: web
  canonical_url: https://www.pse.com.ph/pse-new-trading-engine/
  local_path: null
  edition: in-force
  amended_through: undated
  note: "Fetched 2026-10-06; lists FIX/ITCH/MDF spec release dates, connectivity requirements, PSETradeX hardware; specs themselves by e-mail request."
- slug: pse-web-psetrade-xts
  title: "PSEtrade XTS (Trading > PSEtrade XTS)"
  publisher: The Philippine Stock Exchange, Inc.
  type: web
  canonical_url: https://www.pse.com.ph/psetrade-xts/
  local_path: null
  edition: in-force
  amended_through: undated
  note: "Fetched 2026-10-06."
- slug: pse-web-tp-directory
  title: "Trading Participants directory and Online Brokers list"
  publisher: The Philippine Stock Exchange, Inc.
  type: web
  canonical_url: https://www.pse.com.ph/directory/
  local_path: null
  edition: in-force
  amended_through: undated
  note: "Fetched 2026-10-06; 123 rows (121 Active, 2 Suspended); no as-of stamp."
- slug: pse-web-broker-ranking
  title: "Broker Ranking (top 10 TPs by value, last trading day)"
  publisher: The Philippine Stock Exchange, Inc.
  type: web
  canonical_url: https://frames.pse.com.ph/brokerRankings
  local_path: null
  edition: in-force
  amended_through: 2026-10-05
  note: "Snapshot 'As of October 05, 2026 15:00:00'; no history available."
- slug: pse-web-investing-at-pse
  title: "Investing at PSE (FAQ incl. SIPF description)"
  publisher: The Philippine Stock Exchange, Inc.
  type: web
  canonical_url: https://www.pse.com.ph/investing-at-pse/
  local_path: null
  edition: in-force
  amended_through: undated
  note: "Fetched 2026-10-06."
- slug: pse-corp-history
  title: "PSE corporate history (timeline 1927-2025)"
  publisher: The Philippine Stock Exchange, Inc.
  type: web
  canonical_url: https://corporate.pse.com.ph/about-pse/corporate-profile/history/
  local_path: null
  edition: in-force
  amended_through: undated
  note: "Fetched 2026-10-06; timeline runs to July 2025."
- slug: pse-corp-group-structure
  title: "PSE Group Corporate Structure (CMIC, SCCP, Premier, PDS)"
  publisher: The Philippine Stock Exchange, Inc.
  type: web
  canonical_url: https://corporate.pse.com.ph/about-pse/the-organization/group-corporate-structure/
  local_path: null
  edition: in-force
  amended_through: undated
  note: "Fetched 2026-10-06; states PDS 94.55% owned."
- slug: pse-corp-regulatory-framework
  title: "Stock Market Regulatory Framework (PSE / CMIC / SEC scope table)"
  publisher: The Philippine Stock Exchange, Inc.
  type: web
  canonical_url: https://corporate.pse.com.ph/about-pse/corporate-profile/stock-market-regulatory-framework/
  local_path: null
  edition: in-force
  amended_through: undated
  note: "Fetched 2026-10-06."
- slug: pse-corp-board
  title: "PSE Board of Directors"
  publisher: The Philippine Stock Exchange, Inc.
  type: web
  canonical_url: https://corporate.pse.com.ph/about-pse/the-organization/board-of-directors/
  local_path: null
  edition: in-force
  amended_through: undated
  note: "Fetched 2026-10-06."
- slug: pse-corp-global-alliances
  title: "PSE Global Alliances (WFE, ASEAN Exchanges, SSE, AOSEF)"
  publisher: The Philippine Stock Exchange, Inc.
  type: web
  canonical_url: https://corporate.pse.com.ph/about-pse/corporate-profile/global-alliances/
  local_path: null
  edition: in-force
  amended_through: undated
  note: "Fetched 2026-10-06."
- slug: pse-corp-eqlipse-press-release
  title: "Philippine Stock Exchange Adopts Nasdaq Eqlipse Trading to Enhance Market Infrastructure (press release, 22 May 2025)"
  publisher: Nasdaq / The Philippine Stock Exchange, Inc.
  type: web
  canonical_url: https://corporate.pse.com.ph/philippine-stock-exchange-adopts-nasdaq-eqlipse-trading-to-enhance-market-infrastructure/
  local_path: null
  edition: historical
  amended_through: 2025-05-22
  note: "Joint press release (GlobeNewswire)."
- slug: pse-press-fy2024-results
  title: "PSE posts P1.2B net income in 2024 (press release, 3 Mar 2025)"
  publisher: The Philippine Stock Exchange, Inc.
  type: web
  canonical_url: https://www.pse.com.ph/pse-posts-p1-2b-net-income-in-2024/
  local_path: null
  edition: historical
  amended_through: 2025-03-03
  note: "Stake in PDS 78.33% as of 2025-02-24."
- slug: pse-press-q1-2025-results
  title: "PSE net earnings rise 5 percent in Q1 2025 (press release, 16 May 2025)"
  publisher: The Philippine Stock Exchange, Inc.
  type: web
  canonical_url: https://www.pse.com.ph/pse-net-earnings-rise-5-percent-in-q1-2025/
  local_path: null
  edition: historical
  amended_through: 2025-05-16
  note: "PDS stake 79.9% at end-Mar 2025; 91.6% as of 2025-05-15."
- slug: pse-press-smip-2022
  title: "Online stock market accounts reach 1.26M in 2022 (press release, 5 Jun 2023)"
  publisher: The Philippine Stock Exchange, Inc.
  type: web
  canonical_url: https://www.pse.com.ph/online-stock-market-accounts-reach-1-26m-in-2022/
  local_path: null
  edition: historical
  amended_through: 2023-06-05
  note: ""
- slug: sccp-web-services
  title: "SCCP Services (CCP, DVP, CTGF, MMCD)"
  publisher: Securities Clearing Corporation of the Philippines
  type: web
  canonical_url: https://www.sccp.com.ph/main/services.html
  local_path: null
  edition: in-force
  amended_through: undated
  note: "Fetched 2026-10-06; states T+2, 12:00 noon settlement deadline, collateral haircuts."
- slug: sccp-web-home
  title: "SCCP home page (market summary and memos list)"
  publisher: Securities Clearing Corporation of the Philippines
  type: web
  canonical_url: https://www.sccp.com.ph/main/home.html
  local_path: null
  edition: in-force
  amended_through: 2026-10-05
  note: "Market summary as of 2026-10-05; memo list to 2026-09-11."
- slug: sccp-web-membership-2025-09-14
  title: "SCCP Membership page - membership kit and Clearing Members search list (Wayback snapshot 14 Sep 2025)"
  publisher: Securities Clearing Corporation of the Philippines
  type: web
  canonical_url: https://web.archive.org/web/20250914052222id_/https://sccp.com.ph/main/membership.html
  local_path: null
  edition: superseded
  amended_through: 2025-09-14
  note: "Live page returns 403 to automated clients; archived copy used. 124 clearing members (123 active, 1 suspended); ADA enrolment 'with BDO or RCBC'."
- slug: sccp-web-partners-2025-09-14
  title: "SCCP Partners page - Settlement Banks and Depository (Wayback snapshot 14 Sep 2025)"
  publisher: Securities Clearing Corporation of the Philippines
  type: web
  canonical_url: https://web.archive.org/web/20250914055356id_/https://sccp.com.ph/main/partners.html
  local_path: null
  edition: superseded
  amended_through: 2025-09-14
  note: "Definitions of settlement bank/depository; bank names not listed in text."
- slug: sccp-web-about-2026-05-17
  title: "SCCP About Us (Wayback snapshot 17 May 2026)"
  publisher: Securities Clearing Corporation of the Philippines
  type: web
  canonical_url: https://web.archive.org/web/20260517023553id_/https://sccp.com.ph/main/aboutUs.html
  local_path: null
  edition: in-force
  amended_through: 2026-05-17
  note: "Incorporated 23 Jan 1996; operations 3 Jan 2000; permanent licence 17 Jan 2002."
- slug: pds-web-company-overview
  title: "PDS Group company overview (PDEx, PDTC, PDS Academy)"
  publisher: PDS Group
  type: web
  canonical_url: https://www.pds.com.ph/company-overview/
  local_path: null
  edition: in-force
  amended_through: undated
  note: "Fetched 2026-10-06."
- slug: pds-web-market-governance
  title: "PDEx Market Governance Structure"
  publisher: PDS Group
  type: web
  canonical_url: https://www.pds.com.ph/market-governance-structure/
  local_path: null
  edition: in-force
  amended_through: undated
  note: "Fetched 2026-10-06."
- slug: pds-web-home
  title: "PDS Group home page (PDTC/PDEx statistics as of 1 Oct 2026)"
  publisher: PDS Group
  type: web
  canonical_url: https://www.pds.com.ph/
  local_path: null
  edition: in-force
  amended_through: 2026-10-01
  note: "Fetched 2026-10-06."
- slug: aseanexchanges-web-about
  title: "ASEAN Exchanges - About us"
  publisher: ASEAN Exchanges
  type: web
  canonical_url: https://www.aseanexchanges.org/about-us/
  local_path: null
  edition: in-force
  amended_through: undated
  note: "Fetched 2026-10-06; six member exchanges."
- slug: wikipedia-asean-exchanges
  title: "ASEAN Exchanges (Wikipedia) - ASEAN Trading Link section"
  publisher: Wikipedia
  type: web
  canonical_url: https://en.wikipedia.org/wiki/ASEAN_Exchanges
  local_path: null
  edition: n/a
  amended_through: undated
  note: "Secondary; used only for ATL launch dates (18 Sep 2012; SET 15 Oct 2012) via page-summary tool."
- slug: philstar-nte-2026-07-23
  title: "New PSE trading engine goes live by November (The Philippine Star, 23 Jul 2026)"
  publisher: The Philippine Star
  type: web
  canonical_url: https://www.philstar.com/business/business-as-usual/2026/07/23/2543942/new-pse-trading-engine-goes-live-november
  local_path: null
  edition: n/a
  amended_through: 2026-07-23
  note: "Secondary-only source of Eqlipse capacity figures and cost."
- slug: philstar-pds-landbank-2025-12-24
  title: "PSE hikes stake in PDS via acquisition of Landbank shares (The Philippine Star, 24 Dec 2025)"
  publisher: The Philippine Star
  type: web
  canonical_url: https://www.philstar.com/business/2025/12/24/2496342/pse-hikes-stake-pds-acquisition-landbank-shares
  local_path: null
  edition: n/a
  amended_through: 2025-12-24
  note: "Secondary; read through a page-summary tool (94.21%; DBP 3.08% outstanding; target 97%; P2.75bn total)."
- slug: mondovisione-nasdaq-omx-selected-2014
  title: "Philippine Stock Exchange selects NASDAQ OMX's X-stream Trading technology (1 Jul 2014)"
  publisher: Mondo Visione (press release reprint)
  type: web
  canonical_url: https://mondovisione.com/media-and-resources/news/philippine-stock-exchange-selects-nasdaq-omxs-x-stream-trading-technology-one-201471/
  local_path: null
  edition: historical
  amended_through: 2014-07-01
  note: "Secondary reprint; planned go-live mid-2015."
```
