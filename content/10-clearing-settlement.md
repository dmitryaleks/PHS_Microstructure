---
number: 10
slug: clearing-settlement
title: Clearing, Settlement and Corporate Actions
summary: One CCP with no initial margin and a capped PHP 1.77bn fund, T+2 with a noon deadline, ex-date one trading day before record date with resting orders cancelled, and a stale posted rulebook.
part: Post-trade and information
---

Philippine equity post-trade is one chain under one group. Matched trades pass from the Exchange to the Securities Clearing Corporation of the Philippines (SCCP), which becomes the central counterparty to each **clearing member** (a broker, not the end investor), settles multilaterally net on **T+2** against a hard **12:00 noon** deadline, and moves securities in the depository (PDTC) while cash moves across settlement banks. With one CCP, one depository and one venue there is nothing to route; the post-trade problem is a calendar, funding and counterparty problem.

Four behaviours break assumptions carried over from other venues. First, **the downloadable rulebook is stale**: SCCP still posts the 13 March 2018 text, which says rolling T+3, and everything since (T+2, haircuts, the allocation algorithm, early delivery, fund refunds) exists only as dated memos, so the in-force rule set must be reconstructed ([below](#/ch/clearing-settlement/the-rulebook-currency-trap-and-the-in-force-rule-set)). Second, **risk is collateralised daily but never margined**: there is no initial margin, the guaranty fund was PHP 1.77bn at end-2025, and SCCP's liability is capped by Rule 3.5. Third, **the ex-date is one trading day before the record date** (since 24 Aug 2023), and the Exchange **cancels resting orders on the ex-date of a cash or property dividend and whenever a corporate action adjusts the closing price**. Fourth, foreign flow runs through custodians whose cut-offs fall before SCCP's noon deadline, and the fail statistics that would size that risk stop in 2019.

## Key parameters

SD is the settlement date; SD-1 and SD+1 are the adjacent business days. Each row is sourced where it is developed below.

| Parameter | Value | In force since |
|---|---|---|
| Settlement cycle | **T+2**, settlement date adjusted by SCCP holiday memos | 24 Aug 2023 (T+3 before) |
| Deadline | **12:00 noon on SD** for cash and securities; 11:00 and 14:00 batches on double-settlement days; batch may start early | 24 Aug 2023; 5 Mar 2024 |
| Model | Novation to SCCP; DVP model 3, multilateral net per clearing member and flag | CCCS 29 May 2006; new C&S System 27 Mar 2023 |
| Late and fail fines | PHP 1,000 + 0.125% of the fail (12:00-14:00); PHP 1,000 + 0.25% compounded daily (after 14:00) | 23 Jul 2012 |
| Fail ladder | Cure by 09:15 SD+1; buy-in or sell-out at 10:00 SD+1; cash close-out at highest regular-lot price + 10% | 23 Jul 2012; T+2 timings 24 Aug 2023 |
| Collateral | Mark-to-market on two days of unsettled trades, due 12:00 next business day; haircut 25% (PSEi, MidCap, Dividend Yield) or 35% (other eligible, incl. PSE's own shares) | 20 Feb 2023; 24 Aug 2023 |
| Early delivery | SCCP may require delivery by SD-1 in five situations; **no initial margin** | 21 Jan 2025 |
| Guaranty fund | PHP 1,770.7m at 31 Dec 2025; members pay 0.2 bp of turnover; SCCP liability capped (Rule 3.5) | Rule text 2018 |
| Ex-date | One trading day before the record date | 24 Aug 2023 (RD-3 before) |
| Resting orders | Exchange **cancels** orders on cash or property dividend ex-dates and on closing-price adjustments | Art. IV Sec. 14\(c\), text of Jan 2012 |
| Dividends | Record date disclosed at least 10 trading days ahead; paid within 18 trading days of it | Listing rules |
| Depository | PDTC; PCD Nominee holds legal title; no-jumbo rule | 1 Jul 2010 |
| Pending | BSP 22/7 RTGS soft launch Nov 2026; Nasdaq Eqlipse 23 Nov 2026; single post-trade system target 2027; **no T+1 plan found** | Not in force |

## The post-trade chain

| Step | Entity | What it does |
|---|---|---|
| Match | PSE (PSEtrade XTS; Nasdaq Eqlipse scheduled 23 Nov 2026, see [Chapter 17](#/ch/reform-timeline)) | Matches orders; sends the trade feed to SCCP "immediately after the applicable trading hours"[^sccp-clearing-house-rules-2018:29] |
| Clear | SCCP | Novation, netting per clearing member and flag, mark-to-market collateral, fails management, guaranty fund[^sccp-clearing-house-rules-2018:11] |
| Cash | Settlement banks | Hold each clearing member's Cash Settlement Account; confirm funds to SCCP; credit proceeds[^sccp-clearing-house-rules-2018:31] |
| Securities | PDTC (depository) and transfer agents | Book-entry delivery between settlement accounts; legal title in PCD Nominee's name[^pdtc-depository-rules-1997:27] |
| Supervise | SEC, CMIC | SEC approves SCCP rule changes and hears appeals;[^sccp-clearing-house-rules-2018:12][^sccp-clearing-house-rules-2018:25] CMIC receives overnight-fail notices[^sccp-memo-06-0823-sec-approval-t2-amendments:2] |

Who the clearing members are depends on which list and date you read, and the lists are not merged here. SCCP's membership page on 6 Oct 2026 shows **125 clearing members: 122 active and 3 suspended** (EquitiWorld Securities, Jaka Securities, Mount Peak Securities), **118 local and 7 foreign** (CLSA Philippines, J.P. Morgan Securities Philippines, Macquarie Capital Securities (Philippines), Maybank ATR Kim Eng Securities, SeedBox Securities, UBS Securities Philippines, UOB Kay Hian Securities (Phil.)); the page prints no total, so the counts come from its directory table.[^sccp-web-membership] An archived snapshot of 14 Sep 2025 showed 124 (123 active, 1 suspended).[^sccp-web-membership-2025-09-14] PSE's directory of 20 Jul 2026 lists 123 trading participants, 121 active and 2 suspended (EquitiWorld, Mount Peak); Jaka Securities appears in neither section of it although SCCP lists it as suspended ([Chapter 1](#/ch/market-architecture) holds the participant record).[^pse-active-tp-summary-2026-07-20] Equity clearing members are limited to PSE trading participants.[^sccp-clearing-house-rules-2018:5]

## SCCP: status, novation and the recourse cap

### Legal status and ownership

| Item | Fact |
|---|---|
| Ownership | 100% PSE-owned, SEC-registered clearing agency; the SEC authorises it to fine and sanction clearing members[^sccp-web-about] |
| Dates | Incorporated 23 Jan 1996; commercial operations 3 Jan 2000; permanent licence 17 Jan 2002.[^sccp-web-about] PSE's FY2019 report records SEC approval of the permanent licence on 15 Jan 2002, so the two dates are most likely approval and licence (inference);[^pse-annual-report-2019:39] Clearstream's "1 January 2002" is unreliable[^clearstream-ph-market-infrastructure] |
| Systems | CCCS launched 29 May 2006;[^pse-audited-fs-2025:39] replaced by LSEG Millennium Post Trade on 27 Mar 2023[^pse-audited-fs-2025:40] |
| Governance | PSE's President and CEO is also SCCP's; SCCP's chairman is PSE's chairman; broker-directors sit on SCCP's board[^pse-annual-report-2025:44-47] |
| Statute | Securities Regulation Code Sec. 41 (using an unregistered clearing agency is unlawful), Sec. 42 (registration; 42.2(f) guarantee fund sized on volume and the daily exposure of the four largest brokers), Secs. 43-44 (book entries and clearing-agency records as best evidence), Sec. 47.6 (first priority for the clearing agency's claims against a failing participant)[^ra-8799-src:46-48][^ra-8799-src:50]; 2015 IRR Rule 42, and Rule 36.4.4.5 under which the SEC may require a CCP[^sec-2015-src-irr:158-162][^sec-2015-src-irr:119] |
| Rule changes | SEC approval required; effective 15 days after approval unless the SCCP Board or SEC provides otherwise; SCCP interprets its Rules where they are silent or ambiguous[^sccp-clearing-house-rules-2018:12][^sccp-clearing-house-rules-2018:10] |
| Membership test | SEC-licensed broker-dealer, PSE participant in good standing, depository participant, account holder with a settlement bank[^sccp-clearing-house-rules-2018:18] |

**Settlement banks.** SCCP's Partners page shows nine bank logos (Asia United Bank, BDO, China Bank, Deutsche Bank, EastWest, Maybank, Metrobank, RCBC, UnionBank), each connected to the C&S System in real time.[^sccp-web-partners] Clearstream lists ten, adding HSBC, whose current status is unverified;[^clearstream-ph-settlement-process] the membership kit requires automatic-debit enrolment with BDO or RCBC.[^sccp-web-membership]

### Novation, netting and finality

After daily multilateral netting "there will no longer be a direct link between the original counter-parties"; novation follows, SCCP "becomes the Central Counterparty to each Trade", each net delivery obligation becomes a contract between the net-delivering clearing member as seller and SCCP as buyer, and each net entitlement a contract between SCCP as seller and the net-receiving member as buyer, with clearing members as principals only.[^sccp-clearing-house-rules-2018:26] SCCP describes itself as "seller to all net buying Clearing Members and buyer to all net selling Clearing Members" in Delivery-versus-Payment Model 3 (multilateral net) at clearing-member, not beneficial-owner, level.[^sccp-web-services] Securities are netted per security and per flag: the 2018 flags were LP, LC, FP and FC,[^sccp-clearing-house-operating-procedures-2018:6] and the C&S System screens use account types FC, FH, LC and LH (read as foreign or local, client or house).[^sccp-cs-quick-guide:9] A foreign-client sale therefore does not net against a local-client purchase. Once the securities and cash elements settle the trade is "final and irrevocable" and cannot be unwound "under any circumstances" (Rule 4.6).[^sccp-clearing-house-rules-2018:31]

<div class="callout">
<span class="label">Consequence</span>

SCCP is a CCP by novation but a **limited-recourse** one. Rule 3.5 caps its obligations to (a) amounts it receives from clearing members on settling the contract, (b) the guaranty fund (CTGF) and \(c\) credit facilities arranged expressly to support the CTGF. If the CTGF is insufficient members are paid pro rata (or as SCCP considers fair), SCCP "shall, however, remain liable" for the balance but pays it only "as and when" funds become available, and "no other assets of the SCCP shall be made available".[^sccp-clearing-house-rules-2018:27-28] Rule 5.3 separately says SCCP shall be responsible for ensuring eligible trades are fully settled, sourcing an insolvent member's obligations from the Clearing Fund as advances for that member's account.[^sccp-clearing-house-rules-2018:35] The guarantee is only as large as the fund plus the credit lines (see [the fund section](#/ch/clearing-settlement/the-clearing-and-trade-guaranty-fund-ctgf)).
</div>

### What SCCP does not clear

SCCP clears SCCP-eligible exchange trades only and "does not perform any Clearing and Settlement services for non-Exchange trades".[^sccp-clearing-house-operating-procedures-2018:5] The 2018 procedures exclude "PSE block transactions and negotiated deals" from the guaranty-fund, fails-management and collateral coverage.[^sccp-clearing-house-operating-procedures-2018:23] The settlement status of block sales is unresolved (see [block and negotiated trades](#/ch/clearing-settlement/block-and-negotiated-trades-unresolved-settlement-and-guarantee-status)).

### Execution implications

- Your credit exposure runs first to the **clearing member** (broker or custodian chain) and only then to SCCP, whose cover is capped; prefer clearing members with strong net liquid capital. SCCP monitors each member's daily average netted obligation against its net liquid capital, but the data are not public.[^sccp-web-services]
- Check each broker's status on SCCP's membership page before routing: three members were suspended on 6 Oct 2026.[^sccp-web-membership]
- Keep foreign-flag and local-flag flow in the right accounts end to end; netting, collateral transfers and foreign-room counts all key off the flag.[^sccp-cs-quick-guide:9]
- Treat any block, cross or negotiated execution as outside the SCCP guarantee until SCCP or PSE states otherwise.

## Risk management: collateral, early delivery and no initial margin

SCCP controls its exposure with a daily mark-to-market collateral deposit (MMCD), early-delivery powers, the fund and bank credit lines. It does not take initial margin.

### Mark-to-market collateral deposit

| Parameter | Rule | Source |
|---|---|---|
| Marking | Every clearing member's unsettled trades are marked daily at end of session to the last closing price; price changes from corporate actions are included | Rules 8.1.4, 8.1.6[^sccp-clearing-house-rules-2018:44] |
| Window | **Two days** of unsettled trades since 24 Aug 2023 (three under T+3) | Memo 06-0823[^sccp-memo-06-0823-sec-approval-t2-amendments:3-4] |
| Exposure | [Sum(PP x MM) - Sum(PP x CP)] + [Sum(PS x CP) - Sum(PS x MM)]; PP, PS = unsettled buy and sell shares, CP = contract price, MM = last traded or closing price | Rule 8.1.5[^sccp-clearing-house-rules-2018:44] |
| Coverage | Net negative exposure must be **fully collateralised**; the previous day's deposits are blocked automatically | Rule 8.1.7[^sccp-clearing-house-rules-2018:45] |
| Notice | C&S message board by **18:00** on the computation day | Rule 8.1.9[^sccp-clearing-house-rules-2018:45] |
| Due | Cash or securities collateral by **12:00 noon** the next business day | Rule 8.1.10[^sccp-clearing-house-rules-2018:46] |
| Release | Excess withdrawable 09:00-12:00 the following business day | Rule 8.1.11[^sccp-clearing-house-rules-2018:46] |
| Early delivery | Delivering the securities (or cash) behind the exposure reduces the requirement; the C&S System earmarks them under maker-checker approval | Rules 8.1.3, 8.1.10.3[^sccp-clearing-house-rules-2018:43][^sccp-cs-quick-guide:9-11] |
| Late collateral | 1st offence 0.25% of required collateral; 2nd 0.5% plus warning; 3rd 1% plus suspension recommendation; plus out-of-pocket costs; billed by 15:00 | Rule 8.1.12[^sccp-clearing-house-rules-2018:47] |

**Worked example.** A member has unsettled buys of 200,000 shares at PHP 50.00 and unsettled sells of 50,000 at PHP 52.00 in the same stock; the close is PHP 47.00. Exposure = (200,000 x 47 - 200,000 x 50) + (50,000 x 52 - 50,000 x 47) = -600,000 + 250,000 = **-PHP 350,000**, so PHP 350,000 must be covered by 12:00 the next business day. In cash that is PHP 350,000; in a PSEi constituent (25% haircut) it takes PHP 350,000 / 0.75 = **PHP 466,667** of market value at last close; in a 35%-haircut share, PHP 350,000 / 0.65 = **PHP 538,462**. Securities collateral is valued at the last close.[^sccp-memo-07-0823-sec-approved-amendments:3-4]

### Eligible collateral and haircuts

| From | Eligible securities | Haircut | Source |
|---|---|---|---|
| 14 Nov 2008 | Securities comprising the PSE index, including PSE's own shares | 20% flat | PSE FY2025 statements[^pse-audited-fs-2025:40] |
| 20 Feb 2023 (SEC approval 13 Dec 2022) | Constituents of the PSEi, PSE MidCap and PSE Dividend Yield indices | 25% | Memos 02-0223, 07-0823[^sccp-memo-02-0223-collateral-haircut-rates:1][^sccp-memo-07-0823-sec-approved-amendments:3-4] |
| 20 Feb 2023 | "PSE" shares (the Exchange's own stock) and all other shares SCCP accepts | 35% | Memos 07-0823, 01-0126[^sccp-memo-07-0823-sec-approved-amendments:4][^sccp-memo-01-0126-eligible-collateral-list:1] |

Rule 8.1.8 limits acceptable securities, unless the SCCP Board prescribes otherwise, to constituents of those three indices and PSE's own shares; cash is always acceptable.[^sccp-memo-07-0823-sec-approved-amendments:3-4] Haircuts were aligned with the position-risk factors in the CMIC rules and SEC MC 16-2004 Schedule A; MidCap and Dividend Yield shares were admitted at 25% because they meet PSE's liquidity standards.[^sccp-memo-02-0223-collateral-haircut-rates:1] The list is reviewed every six months and follows PSE's index reviews. The latest archived list (memo 01-0126, effective 2 Feb 2026) added RCR to the PSEi and dropped AGI; added OGP and URC to Dividend Yield and dropped KEEPR and SECB; added AGI and APX to MidCap and dropped DD and RCR.[^sccp-memo-01-0126-eligible-collateral-list:1] SCCP's memo index lists a newer collateral memo, 01-0726 of 28 Jul 2026, that is not archived here;[^sccp-web-memos-index] take the current list from SCCP. SCCP's own Services page still shows a list "effective 1 Feb 2024".[^sccp-web-services]

### Early delivery (Rule 7.6) and the absence of initial margin

Since 21 Jan 2025 (SEC-approved, effective immediately under Rule 1.4.3) SCCP "may, in its discretion, require Early Delivery (i.e., not later than SD-1) of the Cash or Securities obligations from one or more Clearing Members" in five situations, and must lift the requirement when the risk is gone:[^sccp-memo-02-0125-sec-approval-rules-3-4-5-1-4-6-2-8-7-6:3]

| # | Trigger |
|---|---|
| 1 | Unstable conditions or price fluctuations in one or more securities, in addition to the Rule 8 collateral |
| 2 | Exposure larger than the member's financial condition justifies, or that puts SCCP at risk |
| 3 | A record of frequent rule violations, unsound management or serious operational defects |
| 4 | Market conditions such that SCCP calls on affected members to follow "any of the additional risk containment measures under this Rule as determined by SCCP" (none is itemised) |
| 5 | Risk levels determined by SCCP have been reached by a particular member |

The May 2024 consultation draft also let SCCP "require additional margins"; SCCP deleted that because early delivery "may currently be an adequate protection", and the final text has no margin.[^sccp-memo-01-0524-sec-recommended-revisions:4] **There is no initial margin in the rulebook**; Clearstream's statement that SCCP "has proposed to implement margin requirements" is stale.[^clearstream-ph-settlement-process]

The only precedent for a security-specific regime is the 2009-2012 early-delivery requirement on six stocks (ACE, FPI, MVC, PHES, WIN, WPI), imposed by the joint PSE and SCCP boards on 5 Feb 2009 and lifted effective 20 Jan 2012. On T+0 a selling broker had to hold the shares in its PDTC house account before posting any sell order and a buying broker had to hold 100% upfront cash before posting any buy; on T+1 by 12:00 noon net sellers had to early-deliver (or post 100% cash collateral) and net buyers had to early-deliver 100% of the cash value, whether or not they were net Due Brokers.[^sccp-memo-03-0112-early-delivery-lifting:1-3] In 2012 SCCP's Board also approved a "Settlement Restrictions" Rule 7.6 (early delivery of securities by net sellers, early delivery of cash by net buyers, 100% cash collateral, and a ban on "done-through" trading during a restriction) and the deletion of Operating Procedures 5.5.1.1 and 5.5.1.2, and circulated it for comment.[^sccp-memo-04-0812-settlement-restrictions-proposal:1-2][^sccp-memo-02-0413-settlement-restrictions-revisions:1-5] It never reached the consolidated text: the 2013 and 2018 Rules end Rule 7 at 7.5 and the 2018 procedures still carry 5.5.1.1 and 5.5.1.2.[^sccp-clearing-house-rules-2018:42][^sccp-clearing-house-operating-procedures-2018:29] Read it as not adopted (inference), with the 2025 Rule 7.6 as its narrower successor.

**Monitoring.** SCCP watches the adequacy of each member's fund contribution against its pending trades, large concentrations in one issue (referred to CMIC) and recurring fails (at least two within seven trading days, reported to CMIC);[^sccp-clearing-house-operating-procedures-2018:28-29] its website adds unusual settlement obligations against a six-month moving average, monthly daily average netted obligation against net liquid capital and habitual lates (three or more a year).[^sccp-web-services]

**Client-asset rule (Rule 2.3.5, in force since 23 Aug 2023).** A clearing member may deliver only the securities of the instructing client and may not use another client's shares to settle a different client's obligation unless under a securities borrowing and lending arrangement; CMIC findings of violation are grounds for suspension or termination under Rule 2.5.1.[^sccp-memo-07-0823-sec-approved-amendments:2] Omnibus and prime-broker set-ups should be checked against it ([Chapter 9](#/ch/short-selling) covers borrowing).

### Execution implications

- Collateral is a **broker** cost and constraint: expect brokers to ask for pre-funding or pre-positioned inventory in volatile names, and expect the two-day window and the 25% / 35% haircuts to set how much of a position a broker will carry unfunded.
- Collateral eligibility is index-driven. A stock that drops out of the PSEi, MidCap and Dividend Yield indices at a February or August review is no longer eligible collateral from the effective date, which can change a broker's financing appetite for it.[^sccp-memo-01-0126-eligible-collateral-list:1]
- If SCCP invokes Rule 7.6 on a name or member, assume the 2009 pattern: shares pre-positioned before selling, cash pre-funded before buying, deliveries due by 12:00 on SD-1. No notice period or channel is specified beyond SCCP memos.
- Early delivery is also the client's tool: delivering the securities behind a negative exposure removes the collateral charge.

## The Clearing and Trade Guaranty Fund (CTGF)

### Contributions and sizing

| Item | Rule |
|---|---|
| Monthly contribution | **1/500 of 1% (0.002%, 0.2 bp)** of the member's monthly turnover net of block sales and cross transactions of the same flag, or another rate set by the SCCP Board and approved by the SEC; billed on the first business day, payable within seven calendar days; rate set effective 1 Aug 2007 and restated in PSE's FY2025 accounts[^sccp-clearing-house-rules-2018:33][^sccp-clearing-house-operating-procedures-2018:24][^pse-audited-fs-2025:86] |
| Initial contribution | New or returning participants pay on the Ideal Fund Size (VaR model) pro-rated over existing participants: the **high of the range for foreign participants, the average for local**, rounded up to the next PHP 100,000; inactive new participants pay 50% on admission, the balance before trading[^sccp-clearing-house-rules-2018:33][^sccp-clearing-house-operating-procedures-2018:24-25] |
| Six-month true-up | Effective rate of **11%** on the member's daily average trade value; excess refunded, deficiency collected the next business day[^sccp-clearing-house-rules-2018:33] |
| Deficiency call (2018 text) | If market trade value averaged PHP 1.5bn a day for two calendar months, all members pay 11% of their six-month daily average trade value, outright or amortised over two years at an imputed 12%[^sccp-clearing-house-rules-2018:34] |
| Supplemental call (since 21 Jan 2025) | Replaces the PHP 1.5bn trigger, which SCCP's Nov 2021 paper called outdated: SCCP may, **with SEC approval**, require all active members to contribute more when the fund is "no longer commensurate to a sustained increase in trade volume"[^sccp-memo-02-0125-sec-approval-rules-3-4-5-1-4-6-2-8-7-6:2][^sccp-memo-03-1121-proposed-amendments:17] |
| Composition | PSE's seed contribution, members' contributions and interest income; invested in Philippine government securities or Board-approved instruments[^sccp-clearing-house-rules-2018:32][^sccp-clearing-house-rules-2018:34] |

The Ideal Fund Size is reviewed semi-annually: IFS = [Net Trades(LM) x LP x ((SD x RL) + ADV)] / 100 + [Net Trades(LM) x LP x FC x 180/360], where Net Trades(LM) is the net trade value of the **four largest members**, and the T+2 amendment set it on a two-day cycle and cut the liquidation period LP to **5 days (from 7)**.[^sccp-memo-06-0823-sec-approval-t2-amendments:9] The other 2018 parameters, which the T+2 memo does not restate, are SD 3.23 (a 67% probability level), ADV 0.04, FC 15% a year and RL 2.33 (99% coverage).[^sccp-clearing-house-operating-procedures-2018:26] The printed unit conventions are ambiguous and no current IFS output is published.

### Size history

| Year-end | CTGF (PHP m) | Trading-participant principal | PSE seed | Income and unrealised | Source |
|---|---|---|---|---|---|
| 2013 | 786.3 | 434.4 | 80.0 | 271.9 | [^pse-annual-report-2014:130] |
| 2014 | 838.5 | 471.5 | 80.0 | 287.0 | [^pse-annual-report-2014:130] |
| 2016 | 981.5 | 584.1 | 80.0 | 317.4 | [^pse-annual-report-2017:67] |
| 2017 | 1,064.8 | 645.7 | 80.0 | 339.0 | [^pse-annual-report-2017:67] |
| 2018 | 1,097.7 | 688.7 | 80.0 | 329.1 | [^pse-annual-report-2018:121] |
| 2019 | 1,247.7 | 737.1 | 80.0 | 430.6 | [^pse-annual-report-2019:66] |
| 2020 | 1,367.2 | 788.0 | 80.0 | 499.1 | [^pse-audited-fs-2020:84] |
| 2021 | 1,429.5 | 849.3 | 80.0 | 500.2 | [^pse-audited-fs-2022:80] |
| 2022 | 1,476.4 | 899.0 | 80.0 | 497.3 | [^pse-audited-fs-2022:80] |
| 2023 | 1,589.5 | 937.5 | 80.0 | 572.0 | [^pse-annual-report-2024-compiled-17a:148] |
| 2024 | 1,627.6 | 903.5 | 80.0 | 644.2 | [^pse-annual-report-2024-compiled-17a:148] |
| 2025 | **1,770.7** | 952.7 | 80.0 | 738.1 | [^pse-audited-fs-2025:86] |

The fund is off balance sheet and held as trust money; 2015 is omitted because that year's note was not read. In 2024 the "Contributions" line was negative (PHP -34.0m), which implies refunds exceeded new contributions (inference); it recovered by PHP 49.2m in 2025.[^pse-audited-fs-2025:86] At 31 Dec 2025 the assets were government debt at fair value (face PHP 1,436.5m, of which PHP 98.0m matures within a year), a PHP 308.8m time deposit and PHP 10.0m cash; SCCP charges a management fee of 0.1% of the year-end fund (PHP 1.77m for 2025).[^pse-audited-fs-2025:87] Beyond the fund, SCCP has appropriated **PHP 50.00m of retained earnings** to settle a defaulting member's trade obligations "should the clearing and trade guarantee fund not be enough" (unchanged at 31 Dec 2024 and 2025).[^pse-audited-fs-2025:65]

<div class="callout infer">
<span class="label">Inference</span>

Against FY2025 turnover of PHP 1,780.77bn (an average PHP 7.33bn a day)[^pse-annual-report-2025:16] the PHP 1,770.7m fund is about **24% of one average day's turnover**, and about **28%** of the PHP 6.33bn of net obligations open at the 2025 year-end (PHP 4.62bn undelivered plus PHP 1.72bn unpaid; PHP 6.01bn a year earlier),[^pse-audited-fs-2025:82] with roughly two days of trades always open under T+2. That is why the rulebook leans on full daily collateralisation, early delivery and a 12:00 hard stop rather than on fund size. The fund has grown about 42% since 2019, while average daily turnover rose from PHP 6.10bn (2024) to PHP 7.33bn (2025).
</div>

### Uses, waterfall, refunds and fees

- **Uses (Rule 5.1.6):** net money obligations of a failed trade, buy-ins, collateral for settlement-bank credit lines or securities borrowing, insurance premiums, and SCCP's incidental losses; SCCP must notify the SEC when the fund is used, and a member whose contribution is applied must replenish it.[^sccp-clearing-house-rules-2018:34][^sccp-clearing-house-rules-2018:35] SCCP keeps a CTGF account and credit facilities at each settlement bank to limit actual drawings.[^sccp-clearing-house-operating-procedures-2018:8]
- **Waterfall as written** (procedure for cash close-out): (1) the defaulter's cash entitlement held in escrow, (2) its margin collateral, (3) its mark-to-market collateral, (4) its CTGF contribution, (5) SCCP's reserve appropriated for the CTGF, (6) credit lines availed by SCCP, (7) the mutualised CTGF contributions.[^sccp-clearing-house-operating-procedures-2018:19] The "margin collateral" step has no counterpart in the current rulebook, which has no margin regime (inference: legacy drafting). A November 2021 draft would order the application as the defaulter's contributions, fund interest, SCCP's contributions, then non-defaulters pro rata; its adoption is unverified.[^sccp-memo-03-1121-proposed-amendments:17-18]
- **Interest on advances (Rule 6.2.8, since 21 Jan 2025):** the defaulter bears the costs, taxes and lost interest of pre-terminating CTGF investments; credit-line advances bear the lender's rate; both run until paid and are stated in the Demand Notice. This replaced "BSP overnight borrowing rate plus spread".[^sccp-memo-02-0125-sec-approval-rules-3-4-5-1-4-6-2-8-7-6:2]
- **Refunds (Rule 5.2):** before 2018 there was no return of cash contributions;[^pse-sccp-revised-rules:35] refunds as trade-related assets on cessation or termination took effect on 1 Aug 2018 (SEC approval 13 Mar 2018).[^pse-audited-fs-2025:86-87] Since 8 Jul 2025 the member must also show regulatory clearances including the SEC's broker-dealer cancellation order, that all liabilities are settled, and audited evidence that it **shouldered** the contributions rather than collecting them from clients (refund only to the extent proved); no cheque is issued payable to "Cash" or "Bearer".[^sccp-memo-01-0725-ctgf-refund-sec-approval:1-2] That implies contributions are meant to be a broker cost, not a client charge (inference).
- **SCCP fees:** clearing fee **1 bp, VAT-inclusive, of gross trade value** per month (initial membership fee PHP 5,000).[^sccp-clearing-house-rules-2018:62] FY2025 service fees of PHP 317.99m (+19.12%, in line with turnover)[^pse-annual-report-2025:16] and H1-2026 fees of PHP 165.45m on PHP 926.54bn of trading value[^pse-analyst-briefing-1h-2026:7] match 1 bp charged on both sides divided by 1.12 (inference), so the rate appears unchanged. The cost stack is in [Chapter 12](#/ch/costs).

### Allocation algorithm when SCCP cannot pay everyone

If SCCP cannot pay every receiving member in full during a settlement run, Rule 3.4 and Annex 11 (in force since 21 Jan 2025) settle **price first** (the highest buy price and the lowest sell price), then the **lowest quantity**, then a **pseudo-random** process; SCCP may make partial securities deliveries.[^sccp-memo-02-0125-sec-approval-rules-3-4-5-1-4-6-2-8-7-6:1] SCCP's rationale is that the highest buying price brings in the most cash to pay sellers, the lowest selling price brings in the most securities to deliver to buyers, and the lowest quantity settles the most trades in a given time.[^sccp-memo-01-0524-sec-recommended-revisions:2] It replaced "largest outstanding netted amounts first".[^sccp-clearing-house-rules-2018:27]

<div class="callout warn">
<span class="label">Read the rendered page, not the text layer</span>

SCCP amendment memos are redlines. The PDF text layer prints struck-through and inserted wording side by side, so the old "largest outstanding netted amounts first" rule sits next to the new Annex 11 with nothing marking which is current. The T+2 memo mixes deletions and insertions the same way (for example "third second business day (T+6)"). Read the page image before quoting a time, fine or rule number from any memo.[^sccp-memo-02-0125-sec-approval-rules-3-4-5-1-4-6-2-8-7-6:1][^sccp-memo-06-0823-sec-approval-t2-amendments:2]
</div>

### Execution implications

- Size the tail honestly: the mutualised resources are the fund, SCCP's PHP 50m reserve and credit lines whose size is not published, against about PHP 7.3bn of daily turnover. A large broker's default is absorbed first by that broker's escrowed entitlements and collateral, so your practical protection is the broker's collateral position and your own custody and segregation, not the fund (inference).
- The allocation algorithm only matters in a partial-settlement event; no such event is on the public record.
- Fund contributions (0.2 bp of turnover) and the 1 bp clearing fee are broker-level costs; whether they pass through is in [Chapter 12](#/ch/costs).

## The rulebook-currency trap and the in-force rule set

<div class="callout warn">
<span class="label">Currency trap</span>

SCCP's "Rules & Regulations" page lists only the 13 Mar 2018 Rules (71 pages) and Operating Procedures (39 pages); both files carry a 27 Jul 2018 last-modified date and are the same size as the archived 2018 copies, and both still say "rolling T+3".[^sccp-web-rules-page][^sccp-clearing-house-operating-procedures-2018:6] Everything that changed afterwards lives only in dated "Memo for Brokers" amendments (2022 to 8 Jul 2025). **No consolidated, current rulebook is public**, and SCCP's memo index shows no rule or consultation memo after 8 Jul 2025 through 11 Sep 2026.[^sccp-web-memos-index] Treat the memos as authoritative and re-check the index monthly.
</div>

### Edition history

| Date (SEC approval / effect) | Instrument | Change | Status |
|---|---|---|---|
| 28 Jun 2012 (eff. 23 Jul 2012) | Rules 6.1.3, 6.2.2, new 6.2.7; Annex 7 | Cash collateral pending delivery; two-tier fines | Carried into the 2018 text[^sccp-memo-01-0812-sec-approval-fails-management:1-3] |
| 21 Feb 2013 (eff. 1 Apr 2013) | Revised Rules and Procedures | Alternative Cash Settlement | Superseded by the 2018 text[^pse-sccp-revised-rules:28] |
| 13 Mar 2018 (Rule 5.2 eff. 1 Aug 2018) | Consolidated Rules and OP | CTGF refundability | The posted text, T+3 wording[^sccp-clearing-house-rules-2018:1] |
| 24 Nov 2021 | Memo 03-1121 consultation, draft "2022 Revised Clearinghouse Rules" | New C&S terms, T+2, Rule 7.6, CTGF order, fails restructure | Draft; later memos use its numbering, so parts were approved[^sccp-memo-03-1121-proposed-amendments:3-4] |
| 13 Dec 2022 (eff. 20 Feb 2023) | Rule 8.1.8 | Index-constituent collateral; 25% / 35% | In force[^sccp-memo-02-0223-collateral-haircut-rates:1] |
| 18 Aug 2023 (eff. 24 Aug 2023) | T+2 Rules and OP amendments | See below | In force[^sccp-memo-06-0823-sec-approval-t2-amendments:1] |
| 23 Aug 2023 | Memo 07-0823: Rules 2.3.5, 4.7-4.9, 6.2.5, 6.3.5, 8.1.8; OP 2.8-2.10, 3.8.3-3.8.4 | Client-share ban; early BISO settlement; holiday and closure rules; multiple trade dates | In force[^sccp-memo-07-0823-sec-approved-amendments:1] |
| 9 Jan 2024 (eff. 5 Mar 2024) | OP 2.5.3.2 | Early batch run | In force[^sccp-memo-01-0324-early-batch-run-effectivity:1] |
| 21 Jan 2025 | Rules 3.4 / Annex 11, 5.1.4(3), 6.2.8, 7.6 | Allocation; supplemental CTGF; costs; early delivery | In force[^sccp-memo-02-0125-sec-approval-rules-3-4-5-1-4-6-2-8-7-6:3] |
| 8 Jul 2025 | Rule 5.2, OP 4.2.1.3 | CTGF refund conditions | In force[^sccp-memo-01-0725-ctgf-refund-sec-approval:2] |

### Posted text versus in-force text

| Provision | Posted 2018 text | In force | Since |
|---|---|---|---|
| Settlement cycle | Rolling T+3, cut-off 12:00 NN | **T+2**, cut-off 12:00 NN; batch run may start earlier if all obligations are in | 24 Aug 2023; 5 Mar 2024 |
| Trade amendments | Reflected in C&S by 11:30 on T+3 | By **11:30 on settlement date**; sufficiency check by 12:00 | 24 Aug 2023 |
| MMCD window | Three days of unsettled trades | **Two days**; all unsettled trade dates when settlement dates are paired (four in the Jul 2023 example) | 24 Aug 2023 |
| Collateral | Flat 20% haircut | 25% (index shares) / 35% (other eligible) | 20 Feb 2023 |
| Allocation | Largest netted amounts first | Price, lowest quantity, pseudo-random | 21 Jan 2025 |
| Early delivery | Option within T+0 to T+2; OP 5.5.1 risk-level call | Option any time before settlement date; Rule 7.6 call **by SD-1** | 24 Aug 2023; 21 Jan 2025 |
| Fund top-up | PHP 1.5bn/day for two months triggers a deficiency call | Supplemental contributions with SEC approval | 21 Jan 2025 |
| IFS liquidation period | 7 days, three-day cycle | **5 days**, two-day cycle | 24 Aug 2023 |
| Fails notices | Securities-default notice 13:30; overnight-fail notices to CMIC 15:00 | **15:00** and **17:00** | 24 Aug 2023 |
| Cash close-out trigger | SD+1 if "highly risky"; otherwise after trading hours on the third business day (T+6) | SD+1 if "risky"; otherwise after trading hours on the **second business day after SD** | 24 Aug 2023 |
| After a buy-in | SCCP borrows the bought-in shares to deliver at once | Deleted; buy-in and sell-out trades settle early "as far as practicable" | 23-24 Aug 2023 |
| Advance interest | BSP overnight rate plus spread | Defaulter bears costs, taxes, lost interest | 21 Jan 2025 |
| Fund refund | None before 2018; trade-related assets from 1 Aug 2018 | Plus clearance and no-pass-through proof | 8 Jul 2025 |

Sources for the changed items: the T+2 redline[^sccp-memo-06-0823-sec-approval-t2-amendments:2][^sccp-memo-06-0823-sec-approval-t2-amendments:6-9] and memos 07-0823 and 02-0125.[^sccp-memo-07-0823-sec-approved-amendments:2-3] Section numbers in the memos follow the new numbering (sell-out rules 6.2.x for 2018's 6.1.x; securities-fail rules 6.3.x for 2018's 6.2.x; OP 3.7 for 3.9 notices; OP 3.8.3-3.8.4 for 3.10.3-3.10.4; OP 3.12 for 3.14 sanction table; OP 4.3.1 for 4.4.1 IFS).[^sccp-memo-06-0823-sec-approval-t2-amendments:2][^sccp-memo-06-0823-sec-approval-t2-amendments:7-9]

### Execution implications

- Version-gate any model of settlement, collateral or fails on the dates above: a backtest that spans 24 Aug 2023 needs T+3 before and T+2 after, a three-day and a two-day MMCD window, and the 20% and 25%/35% haircut regimes either side of 20 Feb 2023.
- Never implement from the PDFs on sccp.com.ph alone. Pull every memo since 2022 and read the redlines from the page image.
- Re-check SCCP's memo index at least monthly (latest entry 01-0926, 11 Sep 2026).[^sccp-web-memos-index]

## Settlement cycle, DVP and the settlement day

### T+2 since 24 Aug 2023

Equity trades executed from **24 Aug 2023** settle on T+2 (first T+2 settlement 29 Aug 2023); the predecessor was a rolling T+3 with the same 12:00 noon cut-off.[^sccp-clearing-house-operating-procedures-2018:6][^pse-cn-2023-0031-t2-settlement:2] The migration record:

| Date | Event |
|---|---|
| 13 Jun 2023 | SCCP memo 01-0623 targets T+2 for trade date 24 Aug 2023; revised rules had been submitted to the SEC in Dec 2021[^pse-cn-2023-0031-t2-settlement:2-3] |
| 23 Jun 2023 | PSE CN-2023-0031 relays it and sets the ex-date at one trading day before record date[^pse-cn-2023-0031-t2-settlement:1] |
| 29 Jul-7 Aug 2023 | Industry-wide testing[^pse-cn-2023-0031-t2-settlement:2] |
| 10 Aug 2023 | SEC En Banc approves the go-live[^sccp-memo-04-0823-t2-go-live:1] |
| 18 Aug 2023 | SEC approval of the T+2 Rules and OP amendments announced, effective 24 Aug[^sccp-memo-06-0823-sec-approval-t2-amendments:1] |
| 23-24 Aug 2023 | Last T+3 trade date and first T+2 trade date both settle on 29 Aug (28 Aug was a holiday); transition deadlines: Batch 1 (23 Aug trades) 12:00 PM instead of 11:00 AM, Batch 2 (24 Aug trades) 3:00 PM instead of 2:00 PM[^sccp-memo-02-0723-transition-period:1][^sccp-memo-05-0823-settlement-dates-t2-heroes-day:1] |
| 30 Aug-11 Sep 2023 | Deadline 1:00 PM instead of 12:00 NN (penalties from 1:01 PM); the June memo had planned 12:30 PM, the SEC-approved figure was 1:00 PM[^pse-cn-2023-0031-t2-settlement:3][^sccp-memo-04-0823-t2-go-live:1-2] |
| From 12 Sep 2023 | Regular 12:00 NN deadline[^sccp-memo-04-0823-t2-go-live:2] |

T+2 was feasible because the new C&S System supports any settlement cycle, settles two trade dates on one settlement date, handles multiple currencies and uses ISO 20022 with banks and the depository; the old system hard-coded T+3. PSE's accounts say it can connect directly to the trading engine to make real-time marking possible "in the future", so marking is still end-of-day.[^pse-audited-fs-2025:40]

<div class="callout warn">
<span class="label">Stale statements</span>

PSE's FY2025 audited statements still say T+2 "aligned the Philippine settlement cycle with major international markets including the U.S., Europe, Canada, Australia, Japan, Hong Kong".[^pse-audited-fs-2025:41] That sentence is dated: the US and Canada have settled **T+1 since 28 May 2024** (general market knowledge, not a PSE source). **No T+1 or shorter-cycle plan, consultation or SEC action for equities was found** as of 6 Oct 2026: SCCP's memo index has none through 11 Sep 2026,[^sccp-web-memos-index] PSE's 2026 roadmap lists a single post-trade system and a new depository system without a cycle change,[^pse-asm-2026-president-report:28][^pse-analyst-briefing-3m-2026:24] and PSE's circular of 10 Sep 2026 still calls T+2 "the standard" cycle.[^pse-cn-2026-0041-declassification-price-suspension:1] The only T+1 items found are fixed-income conventions: PDEx's standard fixed-income settlement is already T+1, and a pending proposal would add longer spot and extended dates for offshore clients.[^pdex-proposed-settlement-date-conventions-2026:1-2]
</div>

### DVP model and accounts

SCCP guarantees DVP and runs a DVP net settlement system.[^sccp-clearing-house-operating-procedures-2018:5] Securities move by book entry at PDTC between clearing members' Securities Settlement Accounts and SCCP's accounts; cash moves between members' Cash Settlement Accounts at settlement banks and SCCP's nostro.[^sccp-clearing-house-rules-2018:31] Each member also keeps a Cash Collateral Deposit Account.[^sccp-clearing-house-rules-2018:13] The C&S System shows balances as Free, Earmarked (early delivered), Pending Withdrawal (awaiting PDTC confirmation), Pending Debit and Pending Credit, with maker-checker approval on early delivery, collateral and share-withdrawal instructions, and PHP and USD modules.[^sccp-cs-quick-guide:6][^sccp-cs-quick-guide:9] "Cash" means good cleared funds in any denomination held by the settlement bank.[^sccp-clearing-house-rules-2018:4]

### Settlement-day timeline (Philippine time)

| Time | Event | Source |
|---|---|---|
| T, end of session | Trade feed to SCCP; Daily Transaction and Obligation reports; clearing members reconcile against PSE's DTR and report errors at once | Rule 4.1.1; OP 2.5.1 (2018 text)[^sccp-clearing-house-rules-2018:29][^sccp-clearing-house-operating-procedures-2018:8] |
| T, 18:00 | MMCD requirement posted | Rule 8.1.9[^sccp-clearing-house-rules-2018:45] |
| SD-1 | Cash List to settlement banks by the first business day after trade date; collateral due 12:00 noon | Rules 4.1.2, 8.1.10[^sccp-clearing-house-rules-2018:29][^sccp-clearing-house-rules-2018:46] |
| SD 08:00-10:00 | "Forecast" netting: forecast cash call and securities obligations viewable | C&S Quick Guide[^sccp-cs-quick-guide:5][^sccp-cs-quick-guide:7] |
| SD 10:00-12:00 | "Final" netting: cash call and final securities obligations; fund the Cash Settlement Account, move securities to the settlement account | C&S Quick Guide[^sccp-cs-quick-guide:5][^sccp-cs-quick-guide:7] |
| SD 11:30 | Last time for PSE-authorised trade amendments and cancellations to reach the C&S System | Rule 4.1.3 as amended[^sccp-memo-06-0823-sec-approval-t2-amendments:2] |
| **SD 12:00** | Settlement cut-off for cash (confirmed by the bank) and securities (credited at PDTC); SCCP verifies sufficiency; **batch run** starts, deliveries before receipts. It may start earlier if every obligation is in, after an email notice to members and banks 10 minutes before (since 5 Mar 2024) | Rule 4.1.4; OP 2.5.3.2[^sccp-memo-06-0823-sec-approval-t2-amendments:2][^sccp-memo-01-0324-early-batch-run-effectivity:1] |
| Double-settlement day | Batch 1 deadline **11:00**, Batch 2 **14:00**; at most two trade dates per day | Rule 4.9; OP 2.10[^sccp-memo-07-0823-sec-approved-amendments:7-8] |
| SD 12:00-14:00 | "Late" cash or securities: fine PHP 1,000 + 0.125% of the fail | Annex 7[^sccp-memo-06-0823-sec-approval-t2-amendments:4] |
| SD about 13:15 / 13:30 | Cash shortages funded from the CTGF or credit lines by 13:15; sweep-out credits Due Broker proceeds by 13:30 (2018 text, not restated under T+2) | OP 2.5.4.2[^sccp-clearing-house-operating-procedures-2018:10] |
| SD after 14:00 | Fail: PHP 1,000 + 0.25% compounded daily | Annex 7[^sccp-memo-06-0823-sec-approval-t2-amendments:4] |
| SD 15:00 | Notice of Securities Default (was 13:30) | OP 3.7(a)[^sccp-memo-06-0823-sec-approval-t2-amendments:6] |
| SD 17:00 | Notices of possible overnight cash and securities fail to CMIC (was 15:00); buy-in/sell-out notice, request to PSE and preventive-suspension notice; last time for cash collateral in lieu of delivery | OP 3.7(e)-(i); Rule 6.3.8[^sccp-memo-06-0823-sec-approval-t2-amendments:6-7][^sccp-memo-06-0823-sec-approval-t2-amendments:3] |
| SD+1 08:00 | Failed Exchange Trades Report | OP 2.6(d)[^sccp-memo-06-0823-sec-approval-t2-amendments:5] |
| SD+1 09:15 | Cure deadline; notice to CMIC and PSE recommending immediate preventive suspension | OP 3.7(j)[^sccp-memo-06-0823-sec-approval-t2-amendments:7] |
| SD+1 10:00 | Buy-in or sell-out executed as a normal PSE trade | OP 3.8.3-3.8.4[^sccp-memo-06-0823-sec-approval-t2-amendments:7-8] |
| SD+1 12:00 | Demand Notice for advances, penalties, interest and taxes | OP 3.7(k)[^sccp-memo-06-0823-sec-approval-t2-amendments:7] |

The 2018 intraday times that the T+2 redline did not touch (13:15, 13:30) may have changed with the new system; the official T+2 Operating Procedures text has not been republished.

### Cash leg: settlement banks and the BSP payment system

Cash is netted per member into a Net Money Obligation or Entitlement; members fund the Cash Settlement Account with cleared funds, the bank confirms to SCCP online and the funds move to SCCP's nostro; the Cash List also tells banks how much each must pay another "for the synchronization of funds between them", which the 2024 memo calls the banks' "rebalancing process".[^sccp-clearing-house-rules-2018:29][^sccp-clearing-house-rules-2018:31][^sccp-memo-01-0324-early-batch-run-effectivity:2] Custodian guides describe funding by same-day cheque against credit lines or by RTGS and say SCCP urges PhilPaSSplus funding (secondary).[^clearstream-ph-settlement-process][^rbc-ph-market-profile]

BSP's Peso RTGS (PhilPaSSplus) runs Monday to Friday **09:00-17:45**, with intra- and inter-institution payments settled in that window.[^bsp-philpassplus-primer:10][^bsp-schedule-peso-rtgs:1] A payment is final and irrevocable once the paying and receiving participants' settlement accounts are debited and credited; BSP's rules say the RTGS settles the money leg of a securities transaction only after the security is delivered or earmarked, which is BSP's general DvP rule for market infrastructures, not a description of SCCP's own settlement banks (inference).[^bsp-m-2022-049-peso-rtgs-rules:8] SCCP **cannot settle on any day government offices, PhilPaSS and PCHC check clearing are closed**.[^sccp-memo-07-0823-sec-approved-amendments:7]

<div class="callout warn">
<span class="label">Scheduled change: BSP 22/7 RTGS, November 2026</span>

BSP's July 2026 FAQ says the Peso RTGS runs 8.75 hours a day, five days a week today and targets a **soft launch in November 2026** of 22 hours a day, seven days a week except nationwide holidays: windows 00:00-08:59, 09:00-19:00 and 19:01-22:00, a 22:01-23:59 housekeeping gap, weekend transactions value-dated Monday, sending in extended hours optional, and participation expected to grow progressively. BSP "welcomes the potential extension" of DvP settlement windows only "subject to market demand, operational readiness" and arrangements with the infrastructures concerned.[^bsp-faqs-22x7-peso-rtgs-2026-07:1-4] SCCP has issued no corresponding memo through 11 Sep 2026.[^sccp-web-memos-index] SCCP's noon deadline is its own rule, so extended RTGS hours do not by themselves move it (inference).
</div>

### Holidays, closures and double-settlement days

SCCP posts adjusted settlement dates for nationwide holidays at least two weeks ahead; for special holidays outside the official list and for calamity or civil-disturbance closures it posts "no later than 10:00 AM of the next applicable business day"; dates roll on the rolling cycle.[^sccp-memo-07-0823-sec-approved-amendments:4-6] If a trading day falls on a day PhilPaSS and PCHC are closed, its trades settle with the previous trade date's; if more than two consecutive trading days lack settlement, dates are spread so at most two trade dates settle per day, and MMCD covers all unsettled trade dates.[^sccp-memo-07-0823-sec-approved-amendments:7-8] In practice the 2026 memos came 10 to 17 days before the fixed holidays (Holy Week and Araw ng Kagitingan on 16 Mar; Labor Day 21 Apr; Independence Day 1 Jun; Ninoy Aquino Day 11 Aug; National Heroes Day 17 Aug) and 7 and 5 days before Eid'l Fitr (13 Mar) and Eid'l Adha (22 May), so the two-week notice is not reliably met; the 2027 holiday adjustments (Proclamation 1427) were posted on 11 Sep 2026.[^sccp-web-home]

- **T+2 example:** 23 and 24 Aug 2023 both settled on 29 Aug because 28 Aug was a holiday.[^sccp-memo-05-0823-settlement-dates-t2-heroes-day:1]
- **T+3-era example:** with PhilPaSS suspended on Mon 24 Jul 2023 and trading open, trades of 21 and 24 Jul both settled on Thu 27 Jul (11:00 and 14:00 batches) and MMCD covered four unsettled trade dates.[^sccp-memo-01-0723-philpass-suspension:1]
- **Slippage examples:** a PDTC end-of-day delay moved the settlement of 19 Apr 2022 trades first to 20 Apr and then to 21 Apr.[^sccp-memo-04-0422-readjustment-apr19-2022:1][^sccp-memo-06-0422-ongoing-settlement:1] On 10 Feb 2022 PhilPaSSplus started processing that day's value-dated transactions only at about 15:24, the last securities reached SCCP at 17:24 and the last cash at 17:35, and entitlements were released after 17:50.[^sccp-memo-02-0222-delayed-settlement:1] SCCP's memo index also lists PDTC problems on 27 Sep 2018 and 20 May 2022, PhilPaSS(plus) problems on 26 Oct and 11-12 Nov 2020 and 23 Aug 2022, "no clearing and settlement" on 24 Jul 2024 and 29 Aug 2025, and several days from 2024 to 2026 on which the C&S System was available until 5 PM only (titles only).[^sccp-web-memos-index]

### Settlement performance on the public record

| Year | Securities met by 12:00 | Cash met by 12:00 | Average release of Due Broker entitlements |
|---|---|---|---|
| 2015 | 99.98% | 99.99% | 12:34[^pse-annual-report-2015:66] |
| 2016 | 99.99% | 99.98% | 12:28[^pse-annual-report-2016:72] |
| 2017 | 99.98% | 99.97% | 12:31[^pse-annual-report-2017:32] |
| 2018 | 99.99% | 99.96% | 12:37[^pse-annual-report-2018:47] |
| 2019 | 99.99% | 99.99% | 12:30[^pse-annual-report-2019:27] |

These are T+3 figures (no overnight fails in 2015 and 2016; no overnight settlement default in 2018 and 2019). **Reports from FY2020 onward print no compliance or release-time statistics**, so there are no T+2-era figures; the only recent data are year-end snapshots: every trade open at 31 Dec 2024 and 31 Dec 2025 settled in the following January with "no failed trades".[^pse-audited-fs-2025:82]

<div class="callout warn">
<span class="label">Scheduled change: 23 Nov 2026, subject to SEC approval</span>

The Nasdaq Eqlipse engine is scheduled for a big-bang go-live on 23 Nov 2026.[^pse-nte-broker-forum-2026-07-09:9] SCCP's procedures tell members to reconcile against PSE's Daily Transaction Report; PSE's January 2026 deck says the DTR "will no longer be available" once end-of-day files move to the new back-office portal (ABC, CTF, Quote and Price.lis remain), and the August FAQ says the CTF and ABC specifications are unchanged and negotiated trades will be in the CTF.[^pse-nte-user-group-2026-01-15:19][^pse-nte-faq-2026-08:2] The portal also carries trade amendment and trade unbundling modules.[^pse-nte-broker-forum-2026-07-09:13] The deck does not date the DTR's removal, so tying it to the cut-over is an inference, and no SCCP memo on the new engine's trade-feed interface was found. Version-gate post-trade file ingestion on the cut-over date; the master pipeline table is in [Chapter 17](#/ch/reform-timeline).
</div>

### Execution implications

- Compute the settlement date from SCCP's holiday and closure memos, not a generic T+2 calendar: adjusted dates can pair two trade dates on one date and change collateral timing. Model SD as the second SCCP Business Day after the trade date, where a Business Day excludes holidays and days on which PSE trading or BSP and PCHC clearing are cancelled;[^sccp-clearing-house-rules-2018:4] a trading day that is not a settlement day takes the previous trade date's SD (Rule 4.9).
- PHP funding for foreign-funded flow must be at the broker or custodian before 12:00 on SD (earlier through custodians, see [below](#/ch/clearing-settlement/foreign-investors-custodians-and-special-cases)). A member's fills net against its other clients of the same flag only for SCCP purposes, not for your custodian instruction.
- Plan proceeds on a 12:00-14:00 receipt window (historical average release about 12:30); same-day recycling of proceeds depends on the custodian.
- Keep the calendar feed alive for calamity days: closures are announced by 10:00 the next business day, which may be after you have traded.
- There is no T+1 migration work to schedule; monitor SCCP memos.

## Fails, buy-ins and penalties

A **Late** cash payment or securities delivery arrives after the cut-off but before the end of business on SD; an **Overnight Fail** is a default unresolved at the end of business on SD.[^sccp-clearing-house-rules-2018:7] SCCP pays the receiving side first and holds the defaulter's counter-leg in escrow.

| Stage | Cash fail | Securities fail |
|---|---|---|
| Receivers | SCCP advances the deficit from the CTGF or credit lines so receivers are paid on time[^sccp-clearing-house-operating-procedures-2018:16] | Receivers wait for the buy-in |
| Escrow | The defaulter's receivable securities, not less than the fail | The defaulter's receivable cash and/or securities, not less than the fail[^sccp-clearing-house-operating-procedures-2018:16] |
| Cure | Payment by **09:15 SD+1** | Delivery by **09:15 SD+1**, or a borrowing executed with a lender before the buy-in[^sccp-memo-06-0823-sec-approval-t2-amendments:8] |
| If uncured | Preventive suspension; **sell-out of the escrowed securities at 10:00**; proceeds reimburse advances, penalties, taxes and costs[^sccp-memo-06-0823-sec-approval-t2-amendments:7] | Preventive suspension; **buy-in at 10:00** at prevailing market prices; costs and price differences go to the defaulter[^sccp-memo-06-0823-sec-approval-t2-amendments:8] |
| Last resort | Demand Notice 12:00 SD+1 | Cash close-out (below) if the buy-in fails |

**Execution of a buy-in or sell-out.** SCCP coordinates with PSE's Floor Trading and Arbitration Committee and trades through trading participants; the trades carry **no brokers' commission**, SCCP is recorded as buyer "acting for and on behalf of the defaulting seller" (or as seller), the contracts are irrevocable, and the order is signed by SCCP's COO with a copy to PSE's President.[^sccp-clearing-house-operating-procedures-2018:20] Defaults are handled confidentially, with no advance announcement.[^sccp-clearing-house-operating-procedures-2018:13] The trades are entered as normal PSE trades and settle early "as far as practicable".[^sccp-memo-07-0823-sec-approved-amendments:2-3] SCCP no longer borrows the bought-in shares to deliver at once; interest and charges now accrue until all obligations are paid.[^sccp-memo-06-0823-sec-approval-t2-amendments:8]

**Prices.** The buy-in price is the prevailing offer (the sell-out price the prevailing bid). If there is no offer, the 2018 procedures price the buy-in below the lowest of three references, and if no bid the sell-out above the highest. If the buy-in price is below the contract price the difference is credited to the CTGF; if higher it is charged to the defaulter (mirror for sell-outs).[^sccp-clearing-house-operating-procedures-2018:17-18]

<div class="callout warn">
<span class="label">Conflicting documents</span>

For a buy-in with no offer, Operating Procedure 3.10.5.1 lists the reference "last closing price **plus** two price fluctuations", while Rule 6.2.6 says the lower of "the last closing price **less** two fluctuations", the last transaction price or the current offer; both texts use closing price less two price fluctuations as the sell-out reference.[^sccp-clearing-house-operating-procedures-2018:17-18][^sccp-clearing-house-rules-2018:39][^sccp-clearing-house-rules-2018:37] The conflict is unresolved in the public text; the procedure's "plus" reads as an upward cap (inference). Design for the worst case: a buy-in at the prevailing offer, with no ceiling you can rely on.
</div>

**Alternative Cash Settlement (cash close-out).** If the buy-in fails wholly or partly, the SCCP President or COO may pay receivers cash equal to the highest regular-lot price at execution (or on the last traded day) **plus a 10% premium**. It can be invoked on SD+1 where the security, the trade's size against the fund's exposure, or the defaulter is deemed "risky", otherwise after trading hours on the **second business day after SD** (previously the third, T+6); the COO bears no liability for the decision.[^sccp-clearing-house-rules-2018:27-28][^sccp-memo-06-0823-sec-approval-t2-amendments:2] Management may instead accept cash as collateral until 17:00 on SD when the failure is beyond the member's control, with delivery due by 10:00 the next trading day or suspension, the cash then funding the buy-in.[^sccp-memo-06-0823-sec-approval-t2-amendments:3]

### Fines

| Offence | Fine |
|---|---|
| Cash or securities late after 12:00 and up to 14:00 on SD | PHP 1,000 + **1/8 of 1% (0.125%)** of the fail value, plus advance charges and out-of-pocket costs |
| Cash or securities fail after 14:00 or not made | PHP 1,000 + **1/4 of 1% (0.25%) compounded daily** until paid or delivered, plus costs; preventive suspension if not cured by 09:15 SD+1 |

Both tiers took effect on 23 Jul 2012 and the T+2 amendment left the amounts unchanged.[^sccp-memo-06-0823-sec-approval-t2-amendments:9][^sccp-clearing-house-rules-2018:62] Collateral-default fines are in the collateral section. The rule gives no day-count convention for "compounded daily"; read it as a 0.25% daily rate (interpretation).

**Worked example.** A seller fails to deliver 500,000 shares bought at PHP 50.00 (PHP 25.0m). The fine is PHP 1,000 + 0.125% x 25m = **PHP 32,250** if delivered by 14:00, or PHP 1,000 + 0.25% x 25m = **PHP 63,500** on SD after 14:00. A buy-in at 10:00 on SD+1 at PHP 52.50 (+5%) charges the defaulter 500,000 x 2.50 = **PHP 1.25m**, about 20 times the fine. The price move, not the fine, is the cost.

### Sanctions and the EquitiWorld precedent

Suspension or termination grounds include material or persistent breach and repeated fined violations; a third suspension means termination; SCCP may order preventive suspension at once; appeals go to the SEC within 10 business days without a stay.[^sccp-clearing-house-rules-2018:24-25]

| Date | Event |
|---|---|
| Feb 2020-Nov 2023 | Persistent or repeated late cash payments by EquitiWorld Securities[^sccp-memo-03-0324-clearing-member-suspension:1] |
| 25-27 Mar 2024 | SCCP suspends EquitiWorld as a clearing member under Rule 2.5.1(a)/(b)[^sccp-memo-03-0324-clearing-member-suspension:1] |
| 9-10 Oct 2024 | SEC involuntary suspension and preservation order; CMIC special audit[^pse-cn-2024-0053-equitiworld-involuntary-suspension:1] |
| Nov 2024 | SEC En Banc orders CMIC to take over the firm to settle liabilities to customers, PSE and other participants[^pse-audited-fs-2025:59] |
| May-Jun 2025 | CMIC files an allocation plan; SEC approves early release of intact shares (9 Jun 2025)[^pse-cn-2025-0027:2][^pse-audited-fs-2025:89] |
| 17 Mar 2026 | SEC approves the multi-tranche allocation plan and the release of available cash dividends[^pse-cn-2026-0012:2] |

The SEC approved release of intact shares about eight months after the suspension order and the full allocation plan about 17 months after it (arithmetic from the dates). Mount Peak Securities, also on SCCP's suspended list, has been under CMIC involuntary suspension since 13 Aug 2025: its access to PSE's trading system, PDTC's online system and SCCP's clearing facilities is restricted, clients may ask to transfer their securities to another broker or to execute done-through sells with CMIC's approval, and trades by related parties and proprietary trading are barred.[^pse-tpa-2025-0050-mount-peak-involuntary-suspension:2-3] [Chapter 1](#/ch/market-architecture) holds the broker-failure record. Custodians' own penalties for unmatched instructions are custodian-specific and unpublished; one custodian guide says unmatched instructions auto-cancel at the end of the third business day after the first attempted settlement date and penalties are passed through.[^clearstream-ph-settlement-services]

### Execution implications

- Cover every sell at the broker's PDTC settlement account (or borrow) by 12:00 on SD; do not rely on late-day cure. After 14:00 the fine doubles and 09:15 on SD+1 triggers suspension and a market buy-in.
- In a cost model include the buy-in tail: price difference plus 0.25% a day plus broker pass-through (inference that the broker passes it on).
- Expect buy-in and sell-out flow at about 10:00 on SD+1 in the failing name, entered through one designated participant with no commission; whether it prints as agency flow under one broker code is unverified.
- Treat your broker's standing as fail risk: a suspension freezes executions and can trigger sell-outs of escrowed securities.
- Pre-matching with custodians must finish before the custodian's own cut-offs so a custodian-side mismatch does not become a market fail.

## The depository: PDTC and PCD Nominee

PDTC (Philippine Depository & Trust Corp., formerly the Philippine Central Depository) is the central securities depository for PSE-listed equities. PDS Holdings holds 97.72% of PDTC,[^pse-17c-2024-12-26-pdshc-acquisition-agreements:5] and PSE beneficially owned **94.55% of the PDS group on 5 Mar 2026** (92.06% at 30 May 2025);[^pse-analyst-briefing-3m-2026:25][^pse-asm-2025-presidents-report:32] the acquisition trail and group structure are in [Chapter 1](#/ch/market-architecture). Depository assets were PHP 6.08tn at end-June 2026 (equities PHP 5.45tn, 41.9% of domestic listed market value).[^pse-analyst-briefing-1h-2026:18]

### Legal title and accounts

| Topic | Rule |
|---|---|
| Legal title | Lodged securities are immobilised by transferring legal title to **PCD Nominee**, a wholly owned subsidiary whose single purpose is holding legal (not beneficial) title; PDTC is not a fiduciary and treats each participant as beneficial owner of everything in its accounts[^pdtc-depository-rules-1997:8][^pdtc-depository-rules-1997:27] |
| Settlement | Book-entry delivery is final and irrevocable and constitutes constructive delivery; only the Settlement Sub-Account is eligible for transactions; securities are fungible[^pdtc-depository-rules-1997:15] |
| Accounts | Principal-Local or Principal-Foreign, Client-Local and Client-Foreign accounts; foreign clients' holdings must be segregated in a Client-Foreign sub-account[^pdtc-depository-rules-1997:14] |
| Nationality split | Transfer agents confirm PCNC balances daily and send the Filipino and foreign balances to PDTC by 12:00 noon the next business day[^pse-memo-2010-0203-lodgment:4-5][^pse-memo-2010-0203-lodgment:9] |
| Participants | **192 equities depository participants** (brokers, bank trust departments, insurers, SSS, GSIS and the global custodian banks Citibank N.A., Deutsche Bank AG Manila Branch, HSBC and Standard Chartered; SCCP itself) and 63 fixed-income participants as of 30 Sep 2026; BNP Paribas, State Street and Northern Trust are not direct participants[^pds-web-depository-participants] |

The Filipino and non-Filipino PCNC split is the depository-level mechanism that lets PDTC and transfer agents police foreign-ownership limits without beneficial-owner names (inference). Global custodians without a direct PDTC account reach the market through a sub-custodian that is a participant, for example Clearstream through Standard Chartered Bank Philippines in an omnibus account.[^clearstream-ph-market-link-guide]

### No-jumbo rule, lodgement and upliftment

As a condition of listing and trading every issuer must electronically lodge its registered securities with PDTC "without any jumbo or mother certificate" (Listing Rules Art. III Part A Sec. 16, SRC Sec. 43); existing listed companies were mandated from **1 Jul 2010**, with conversion of existing jumbo certificates in at most 30 business days.[^pse-memo-2010-0203-lodgment:1-2][^pse-memo-2010-0203-lodgment:4] To lodge, a participant prepares a direct transfer to PCD Nominee with the nationality indicated, enters a lodgement report and delivers the documents to the transfer agent, which verifies within three business days (defects corrected within one).[^pse-memo-2010-0203-lodgment:7] **Upliftment** freezes the shares: the request is earmarked, goes to the transfer agent on a published weekly schedule, and the shares are ineligible for settlement until certificates are issued, with elapsed times of two to four weeks reported by custodians (secondary).[^pse-memo-2010-0203-lodgment:8][^pdtc-depository-rules-1997:32][^rbc-ph-market-profile]

### Beneficial-owner visibility and NoCD

PDTC's records stop at the participant. **Name-on-Central-Depository (NoCD)** records holdings at beneficial-owner level in sub-accounts under an omnibus broker account. A 6 Apr 2017 SEC directive stresses that NoCD is "mandatory for all DDS transactions" under the SEC-approved PSE DDS Rules (Part A Sec. 3, approved 10 Nov 2016). For the Del Monte Pacific offer it allowed an interim omnibus account with segregated coded sub-accounts, required client consents within two months of listing and a sealed master list for the SEC, and said SRC Rule 52.1.6.7 (no numbered accounts) applies fully once that period lapses.[^sec-dds-directive-2017:1-2] For REITs brokers assign each client an 11-character NoCD ID (3-character PSE broker code, "R", 7 broker characters) under two broker accounts, one "omnibus with client" and one "omnibus without client" that is flat at end of day; clients with custodians need no NoCD sub-account.[^pdtc-nocd-reit-faq:1-3][^pdtc-nocd-reit-faq:6] For ordinary peso shares NoCD is not required; PSE's 2025-2026 materials list "expansion of NoCD coverage to include all stock securities" as planned, with no timetable.[^pse-asm-2025-presidents-report:32][^pse-analyst-briefing-3m-2026:25]

<div class="callout warn">
<span class="label">Pending change: single post-trade system, target 2027</span>

PSE's roadmap (4 Jul and 17 Aug 2026) plans a "single system for post-trade activities (clearing and settlement, and depository)", fixed-income assets as clearing collateral and wider NoCD coverage as Phase 2, targeted for 2027, and PDTC is implementing a new central depository system.[^pse-asm-2026-president-report:28][^pse-analyst-briefing-1h-2026:31][^pse-analyst-briefing-3m-2026:24-25] Cut-offs, interfaces and NoCD coverage may change; none has been announced. See [Chapter 17](#/ch/reform-timeline).
</div>

The only public PDTC rule text is the November 1997 "Rules of the Philippine Central Depository"; later amendments, the 2021 Registry Rules and PDTC's fee schedule are not publicly accessible.[^pds-web-rules]

### Execution implications

- Choose the settlement route deliberately: a local broker's own PDTC accounts (omnibus), a global custodian's sub-custodian (off-exchange broker-to-custodian trade settled at PDTC), or NoCD-segregated sub-accounts for DDS and REITs.
- Your legal protection rests on custodian and broker segregation and the participant's records, not on PDTC's.
- Send the nationality flag end to end; mis-flagging affects the PCNC split and foreign-room counts.
- Do not plan on upliftment; it freezes the stock for weeks.

## Corporate actions

### Ex-date: record date minus one trading day

Since the target effective date of **24 Aug 2023** the Exchange sets the ex-date "one (1) trading day prior to the disclosed record date"; ex-dates already disclosed for earlier actions were adjusted through amended disclosures.[^pse-cn-2023-0031-t2-settlement:1] The convention follows from the cycle: under T+2 a buyer on the ex-date settles after the record date and is not on the register, while a buyer on record date minus 2 settles on the record date and is.

**Worked example (June 2026 calendar; Fri 12 Jun was a non-trading day).**[^pse-cn-2026-0027:1] Record date Mon 15 Jun. The ex-date is Thu 11 Jun. A buyer on Wed 10 Jun settles Mon 15 Jun (Thu 11 is T+1, Fri 12 is a holiday, Mon 15 is T+2) and is entitled; a buyer on Thu 11 Jun settles Tue 16 Jun and is not. Under the old rule (ex-date three trading days before record date, T+3) the ex-date would have been Tue 9 Jun. Moving to RD-1 shifted the last cum-entitlement trade date from **RD-4 to RD-2**; backtests and corporate-action calendars that span 24 Aug 2023 need the convention switched at that date.

**Evidence from PSE EDGE.** A scan of the EDGE dividends list on 7 Oct 2026 (515 records, 499 with both an ex-date and a record date) against a PSE closure calendar built from PSE's non-trading-day circulars and Proclamation 1006 finds that **all 493 records with ex-dates from 20 Oct 2023 to 8 Feb 2027 put the ex-date on the last trading day before the record date**, with no trading day in between.[^pse-edge-dividends-rights] Only 12 of the 493 pairs straddle a closure, and every intervening weekday is a PSE closure: 21 Aug 2025 (Ninoy Aquino Day); 8, 24, 25, 30 and 31 Dec 2025 and 1 Jan 2026;[^pse-cn-2025-0043-non-trading-days:1] 17 Feb, 20 Mar, 2, 3 and 9 Apr, 1 May, 27 May, 12 Jun and 31 Aug 2026.[^pse-cn-2026-0008:1][^pse-cn-2026-0010:1][^pse-cn-2026-0011:1][^pse-cn-2026-0016:1][^pse-cn-2026-0023:1][^pse-cn-2026-0027:1][^pse-cn-2026-0034b-non-trading-days-aug-2026:1] The six rows that do not fit are stale entries with 2018-2023 ex-dates: five show the old RD-3 pattern (two trading days between) and one spans the 2018 year-end closures. Data oddities: one record date on a Sunday (Central Azucarera de Tarlac, 15 Mar 2026) and 14 record dates on PSE non-trading days, mostly foreign-listed issuers (Manulife, Sun Life) and San Miguel's 20 Mar 2026 record date (Eid'l Fitr), where the ex-date remains the last trading day before. The market-calendar page marks cash and stock ex-dates by day.[^pse-edge-market-calendar]

**Data source.** The EDGE list loads from an unauthenticated POST to `/disclosureData/dividends_and_rights_info_list.ax?DividendsOrRights=Dividends` (or `Rights`) with form fields `pageNum`, `sortMode`, `dateSortType` and `cmpySortType`; the page itself renders empty to scrapers. On 7 Oct 2026 it returned 11 pages and 515 dividend rows (485 cash, 5 stock, 3 property among the 493 post-T+2 rows with both dates) with columns for company, security, dividend type, rate, ex-dividend date, record date, payment date and circular number (rights add entitlement ratio, offer price, ex-rights date and offer-period start and end). It holds stale rows from 2018 onward and "TBA" dates, so filter on ex-date and on populated dates before use.[^pse-edge-dividends-rights]

<div class="callout warn">
<span class="label">Stale text in the rulebook</span>

PSE's Consolidated Listing and Disclosure Rules (January 2025 compilation) still print "the Exchange shall automatically determine the ex-date ... three (3) Trading Days before the announced record date" under the rights-offering article, and one custodian profile repeats "three working days".[^pse-listing-disclosure-rules:107][^clearstream-ph-securities-administration] Use RD-1: PSE's circular of 23 Jun 2023 and the EDGE data override the compilation. See also [Chapter 2](#/ch/instruments).
</div>

<div class="callout">
<span class="label">Consequence: resting orders do not survive an ex-date</span>

Revised Trading Rules Art. IV Sec. 14\(c\) says "The Exchange **shall cancel** the following Orders which are deemed invalid: (i) Orders for a certain Security in the event of corporate actions resulting to an adjustment in the Closing Price; (ii) **Orders on the ex-date for Securities with cash and/or property dividends**; or (iii) Orders for Securities that cross a Board Lot."[^pse-revised-trading-rules:25][^pse-tpa-2011-0110-amended-revised-trading-rules:4] The Implementing Guidelines say the Exchange "may cancel all active Orders when corporate actions result in adjustment of the Closing Price".[^pse-implementing-guidelines-trading-rules:18] The Rules are mandatory ("shall") where the Guidelines say "may", and the text carves out no multi-day validity (GTC, GTD, GTW, sliding), so assume **every resting order, whatever its validity, is purged** in a stock with a cash or property dividend on its ex-date and in any stock whose closing price is adjusted, and resubmit after the reference price is set (inference from the rule text; PSE has issued no statement on multi-day orders). No later amendment of this section was found. See [Chapter 4](#/ch/order-types) for validity types.
</div>

<div class="callout warn">
<span class="label">Scheduled change: 23 Nov 2026, subject to SEC approval</span>

PSE's January 2026 deck for the new engine lists, among the PSETradeX terminal changes, removal of Good Till Cancel and Next Day validity and a new Good Till 3 Months validity for the cloud version; the cloud migration has since been deferred.[^pse-nte-user-group-2026-01-15:17][^pse-nte-broker-forum-2026-07-09:11] PSE has not said whether the Eqlipse engine keeps the GTC, GTD, GTW and sliding validities of the 2010 rules or carries Sec. 14\(c\) over. Treat any multi-day order as lost at the 23 Nov 2026 cut-over (inference) and see [Chapter 17](#/ch/reform-timeline).
</div>

### Reference-price adjustment

The Reference Price is the previous trading day's closing price, or the **Adjusted Closing Price (ACP)** "in the event of corporate actions that would result to an adjustment of the Closing Price", or the last traded price or last ACP if there was no trading; the ACP is "the Closing Price of a Security with adjustments due to corporate events".[^pse-revised-trading-rules:20][^pse-revised-trading-rules:8] The opening reference is the previous close or the Last Adjusted Closing Price (LACP).[^pse-implementing-guidelines-trading-rules:16] Market Control broadcasts dividends and rights before the pre-open.[^pse-implementing-guidelines-trading-rules:5-6] The index methodology adjusts the previous price and free-float factor for stock dividends, rights and splits.[^pse-index-policy-2024:14] PSE's **exact ACP formulas were not found** in the documents read; the feed hooks are the `lacp` field of the securities static-data file, "Adjusted Previous" in the end-of-day quote file and the start-of-day reference-price message (see [Chapter 11](#/ch/market-data)).[^pse-securities-static-data-file:4][^pse-quote-file-eod-spec-2014:2][^pse-itch-equities-feed-spec-v2-3:27]

<div class="callout infer">
<span class="label">Inference</span>

Standard conventions (not published by PSE): a cash dividend of D lowers the ACP to close minus D; a stock dividend of x% divides the close by (1 + x). On that basis UBP's 27% stock dividend implied an ACP of close / 1.27, a 21.3% drop. Validate against the published LACP before relying on your own adjustment.
</div>

PSE can get it wrong. On 21 Dec 2023 it suspended Union Bank (UBP) for the day because "the stock's previous closing price was not adjusted to account for UBP's 27 percent stock dividends", and resumed on 22 Dec "with the adjusted share price".[^pse-cn-2023-0074-ubp-trading-suspension:1] For a Class A/B declassification the adjusted price is the **higher** of the two classes' closes on the last trading day, preceded by a two-trading-day suspension so earlier trades settle "through the standard T+2 settlement cycle": last trading day Thu 10 Sep, suspension from Fri 11 Sep, T+2 settlement completed Mon 14 Sep, then effectivity, delisting and resumed trading on Tue 15 Sep (sample timeline, circular of 10 Sep 2026).[^pse-cn-2026-0041-declassification-price-suspension:1-2]

### Dividends, stock dividends and rights

| Event | Rule |
|---|---|
| Declaration and record date | Disclosed to the Exchange; record date set per SEC (and BSP) rules and **disclosed at least 10 trading days before the record date**[^pse-listing-disclosure-rules:146-147] |
| Payment date | **At most 18 trading days after the record date**; for PDTC-lodged shares cash and stock dividends go to PDTC within 18 trading days; one declaration may cover several dividends if dates are explicit[^pse-listing-disclosure-rules:147] |
| PDTC credit | After PDTC verifies good funds from the issuer at least one business day before payment date; participants distribute net of withholding tax; entitlements computed from PCD Nominee holdings at record date as confirmed by the transfer agent, rounded down[^pdtc-depository-rules-1997:31] |
| Stock dividends | Credited after the transfer agent confirms the listing or payment date and a new certificate in PCNC's name[^pdtc-depository-rules-1997:31] |
| Rights: filing | Listing and SEC registration applications within 90 days of board approval; price range (floor and cap) disclosed at filing[^pse-listing-disclosure-rules:106] |
| Rights: record date | At least **15 trading days** after approval; offering period starts within **30 calendar days** of the record date; offering memorandum at least 7 calendar days earlier[^pse-listing-disclosure-rules:107] |
| Rights: allocation | Underwriter takes shares not subscribed after the second round; unexercised rights go first to holders who exercised; extra shares must be indicated and paid in round one[^pse-listing-disclosure-rules:106-107] |
| Rights: close-out | Certification and new stockholder list within 15 days of the offering's last day; delay penalty is a 25% surcharge on listing fees plus 1% a day[^pse-listing-disclosure-rules:107-108] |
| Rights: mechanics | Participants distribute subscription forms to beneficial owners and return them to the transfer agent; new shares are lodgeable after full payment[^pdtc-depository-rules-1997:32] |

On payment timing, 467 of the 474 EDGE records with a payment date pay within 18 trading days of the record date (median gap 15 calendar days); the seven that do not are foreign-listed cash dividends (Manulife and four Sun Life payments, 20-23 trading days), a stock dividend (Makati Finance, 35) and a property dividend paid 350 trading days after its record date (Liberty Flour Mills). The EDGE rights list held 12 records, every one with ex-rights and offer dates still "TBA" and several dating from 2014-2015.[^pse-edge-dividends-rights] Custodian guides report cash reaching clients 30-40 calendar days after the record date, so the custody chain adds time beyond the issuer's payment date (inference); they also report rights as **not tradable** (exercise or lapse, subscription at least two days before the offer closes, new shares 15-60 days after payment) and non-resident dividend tax of 25% (15% with tax sparing or treaty relief).[^clearstream-ph-asset-servicing][^rbc-ph-market-profile] No PSE rule on trading rights was found in the rulebooks read, so non-tradability rests on custodian statements and silence (inference); tax detail is in [Chapter 12](#/ch/costs) and [Chapter 14](#/ch/foreign-access).

**Clearing interplay.** SCCP's mark-to-market reflects corporate-action price changes (Rule 8.1.6).[^sccp-clearing-house-rules-2018:44] Custodians file market claims from record date + 1 for trades that settle across the record date or fail.[^rbc-ph-market-profile] The Equitiworld case shows what happens to entitlements at a failed broker: PDTC paid accumulated cash dividends of its clients to a CMIC account (PHP 8.76m at 31 Dec 2025).[^pse-audited-fs-2025:89]

### Execution implications

- Pull ex-, record and payment dates from the EDGE "Dividends and Rights" list and the market calendar and test entitlement as trade date earlier than ex-date; never use the legacy RD-3 convention. Model the ex-date as the last PSE trading day before the record date, including when the record date is itself a non-trading day.
- On the ex-date re-seed reference and limit prices from the LACP or ACP, expect resting orders to be cancelled and avoid carrying GTC or other multi-day orders across ex-dates; cross-check the published reference price against your own adjustment because PSE once opened a day unadjusted (UBP, 21 Dec 2023).
- Rights appear not to be tradable (custodian statements; no PSE rule found): if the strategy cannot subscribe, avoid holding through the rights record date or accept dilution, and check custodian availability and early internal deadlines.
- Dividend withholding on non-residents is taken at source through PDTC participants; arrange relief paperwork with the custodian before the pay date. Proceeds arrive after the payment date plus bank clearing.

## Foreign investors, custodians and special cases

### Custodian settlement

Foreign institutions trade through a local broker (foreign-client flag), and the broker-to-custodian leg is a separate **off-exchange, gross, trade-by-trade settlement at PDTC**: custodian guides say it does not follow DVP, securities to be sold must be in the broker's account by 12:00 on SD, and same-day turnaround is possible but constrained by cheque clearing.[^clearstream-ph-settlement-process][^rbc-ph-market-profile] This evidence is **secondary only** (Clearstream, RBC); market guides from the other global custodians were not available, so their cut-offs are unknown. Clearstream's published cut-offs for listed equities:

| Time (PHT) | Step |
|---|---|
| SD-1 09:00 | Manual pre-matching by telephone starts[^clearstream-ph-settlement-services] |
| SD-1 14:30 | Funding for third-party-bank cash must be credited; a MT210 is no guarantee[^clearstream-ph-settlement-services] |
| SD 09:30 | Mismatches advised[^clearstream-ph-settlement-services] |
| SD 09:35 | Deadline for valid instructions for PDTC-eligible securities: "10:00 SD-1 to 09:35 SD" on Clearstream's year-round PHT table (03:35 on its summer CET table); deliveries expected to settle 13:30-14:30[^clearstream-ph-settlement-times] |
| SD 10:00 | Cancel and re-instruct a mismatched instruction; no amendment, no countervalue tolerance, no partial settlement[^clearstream-ph-settlement-services] |
| SD 12:00 | SCCP deadline |

Standing instructions: deliver to Standard Chartered Bank Philippines (BIC SCBLPHMM) for the account of CBL in favour of the client; cash by MT202 with `REC/RTGS` in field 72; manager's cheques not accepted; and only securities with a valid BSP registration are accepted for receipt.[^clearstream-ph-settlement-services][^clearstream-ph-cash-services][^clearstream-ph-investment-regulation]

<div class="callout infer">
<span class="label">Inference</span>

For a Clearstream-type route the working cut-offs are: instruct and pre-match by SD-1 09:00, fund PHP by SD-1 14:30, valid instruction by 09:35 on SD, SCCP deadline 12:00, with broker-side settlement finishing about 12:30-13:30. Most foreign-flow fails will originate in the custodian segment (manual pre-matching, cut-offs, BSP registration), not at SCCP. Other custodians' formats and cut-offs are unknown.
</div>

### BSP registration

Under the BSP FX Manual (updated May 2025; the live file was byte-identical when checked on 6 Oct 2026), inward investments need not be registered unless repatriation in pesos is to be funded with FX from authorised agent banks; a BSRD is no longer issued for onshore-listed equities. Equity of residents listed at an onshore exchange such as PSE, ETFs and PDRs are registered when the **registering AAB** (an FCDU bank the investor designates) reports them to BSP; inward FX must be converted to pesos through an AAB unless the investment must be funded in FX, and the investor signs an "Authority to Disclose Information" covering all registered investments.[^bsp-fx-manual-morfxt-2025-05:42][^bsp-fx-manual-morfxt-2025-05:46] Registration mechanics and ownership limits are in [Chapter 14](#/ch/foreign-access).

### Dollar-denominated securities

DDS (rules SEC-approved 10 Nov 2016) settle in **USD** through a settlement bank designated by SCCP; participants need an FCDU account and a separate USD cash settlement account, and funds must be good cleared funds by the deadline (same-day USD notes may not clear). Fund contributions are paid in pesos at the PDEx closing USD rate; MMCD is computed separately with **USD cash collateral only**; fails management is the same.[^pse-dds-rules:8-10] SCCP's December 2016 training deck described the old regime (BDO as settlement bank, 12:00 on T+3, USD transfers the day before settlement); the new C&S System handles PHP and USD settlement and collateral, with four PHP and four USD securities collateral accounts per member at PDTC.[^sccp-dds-clearing-settlement-2016:3-5][^sccp-cs-quick-guide:5][^sccp-memo-01-0222-collateral-accounts-pdtc:2] No separate DDS cycle announcement was found, so DDS are assumed to follow T+2 and the noon deadline (inference); the 2016 procedures are partly historical. NoCD is mandatory for DDS.[^sec-dds-directive-2017:1]

### Give-up/take-up

Under the Revised Trading Rules a trading participant may assign an outstanding client order to another participant for clearing and settlement; the Settling Participant assumes liability by agreement but the Assigning Participant stays solidarily liable, and proprietary orders cannot be given up.[^pse-revised-trading-rules:27-28] SCCP's give-up/take-up facility was proposed in January 2011 and revised in May 2011 (secondary summary only);[^digest-ph-sccp-gutu-2011] a word search of the 2018 SCCP rules finds no such provision, so the operative mechanics are not in the published rulebook and current status is unverified.

### Class A/B shares and foreign-ownership breaches

SEC Memorandum Circular 10 s.2025 (PSE CN-2025-0035) discontinues the Class A/B split of listed common shares, gives companies one year to amend their articles and, meanwhile, obliges regular-board buyers to "accept the delivery of the specific class of shares that they have purchased and paid for"; its preamble calls the split "a source of administrative inefficiencies for the trading participants and the Securities Clearing Corporation of the Philippines (SCCP)".[^pse-cn-2025-0035-sec-declassification-mandate:2-3] The circular took effect on 9 Aug 2025, articles had to be amended by 9 Aug 2026 and the delivery rule applies from 11 Aug 2025.[^pse-cn-2025-0036-declassification-effectivity:1] If a trade breaches a foreign-ownership limit, the foreign buyer's broker must dispose of the excess at the prevailing market price immediately (the same day if found in trading hours, otherwise at the next open) and return the proceeds.[^pse-cn-2025-0035-sec-declassification-mandate:3] Check foreign-room headroom before order entry, not at settlement.

### Block and negotiated trades: unresolved settlement and guarantee status

<div class="callout warn">
<span class="label">Unresolved</span>

The Implementing Guidelines say regular block sales settle "within the execution date (T+0)" and special blocks settle on execution date unless the parties' agreement says otherwise.[^pse-implementing-guidelines-trading-rules:23-24] Regular trades moved to T+2 in Aug 2023 and **no block-specific amendment was found**, so whether T+0 block settlement still applies is unverified. The 2018 SCCP procedures exclude block and negotiated trades from guaranty-fund, fails and collateral coverage.[^sccp-clearing-house-operating-procedures-2018:23] SCCP's Board approved, on 29 Mar 2021, that block sales conforming to the settlement cycle be settled and guaranteed by SCCP, and the Nov 2021 consultation proposed the rule change;[^sccp-memo-03-1121-proposed-amendments:4][^sccp-memo-03-1121-proposed-amendments:17] no adoption is on record and the 2018 Rules still show the exclusion. Treat blocks as outside the SCCP guarantee and confirm settlement terms with the executing broker. Block mechanics are in [Chapter 5](#/ch/matching).
</div>

### Execution implications

- Hold standing settlement instructions and FX arrangements with every custodian, confirm each broker's PDTC participant IDs, and allocate at the close of trade date so custodian matching can start at 09:00 on SD-1.
- Exchange deadlines come first. Unbundling of aggregated client orders and trade amendments must be done by 14:00 on T+1 where the nationality flag changes and 17:00 on T+1 where it does not on a whole trading day (17:00 on T+0 and 12:00 on T+1 on a half day), per the December 2011 amendments to the Implementing Guidelines; SCCP then only reflects PSE-authorised changes up to 11:30 on SD ([Chapter 13](#/ch/regulatory-constraints)).[^pse-tpa-2011-0124-amended-implementing-guidelines:3-4]
- Avoid late partial fills with different counter-values: no tolerance and no partial settlement at the custodian.
- DDS: keep USD liquidity at the designated settlement bank the day before SD and complete NoCD consent and KYC steps.
- For stocks near a foreign-ownership cap, a breaching buy is unwound at market, so headroom checks belong before order entry.

## What is not in the public record

- A consolidated, SEC-approved T+2 text of SCCP's Rules and Operating Procedures; the text of any adopted Rule 5.1.7 waterfall or Rule 6 restructure from the Nov 2021 draft.
- Settlement compliance, release-time and fail statistics after 2019; SCCP's own capital, the size of its credit lines, a PFMI self-assessment and updated Ideal Fund Size parameters.
- Whether blocks and negotiated trades are now guaranteed or settle T+0 or T+2.
- Which buy-in reference price applies (OP "plus" or Rule "less") when no offer exists.
- Whether SCCP, PDTC and the settlement banks will use BSP's extended RTGS hours after the November 2026 soft launch, and how SCCP will interface with the new engine on 23 Nov 2026.
- PDTC's current rules and fee schedule, the Filipino and foreign PCNC balances, the NoCD expansion timetable and the go-live date of the new depository system.
- PSE's ACP formulas, stock-dividend record-date mechanics and any rule on rights tradability.
- Other custodians' cut-offs and SSI formats, PDTC pre-matching cut-offs, and whether HSBC is still a settlement bank.
- Primary confirmation that give-up/take-up is in force.
- A reconciliation of SCCP's clearing-member list with PSE's participant directory (Jaka Securities).
