---
number: 1
slug: market-architecture
title: Market Architecture
summary: One exchange, one CCP, one depository and no co-location. Who runs and regulates PSE equities, how orders reach the engine, and why the 23 Nov 2026 Eqlipse cut-over is the date to design around.
part: The venue
---

Philippine cash equities run through one exchange, one central counterparty and one depository, and one corporate group now owns the whole chain. The Philippine Stock Exchange (PSE) is the only stock exchange and a front-line self-regulatory organisation (SRO); it owns 100% of its clearing house (SCCP) and of its market-regulation arm (CMIC), and since December 2024 it has bought control of the depository and fixed-income group PDS (94.55% beneficially owned as of 4 Feb 2026).[^pse-annual-report-2025:8][^pse-annual-report-2025:9] There is no venue-selection, routing or cross-venue problem: every optimisation is intraday scheduling, broker selection and counterparty management.

Three features break assumptions carried over from other venues. **Algorithmic access is not a given**: PSE's DMA Rules prohibit high-frequency and algorithmic trading through the DMA facility, a 2023 proposal to allow algorithms has no recorded approval, there is no co-location and no published message-rate limit, so execution algorithms run inside the broker's own system.[^pse-dma-rules:7][^pse-cn-2023-0043:3] **The engine and the rule set are about to change together**: PSEtrade XTS (Nasdaq X-stream, live since 22 Jun 2015) is scheduled to give way to Nasdaq Eqlipse in a no-parallel-run cut-over on Mon 23 Nov 2026, bundled with rule changes still awaiting SEC approval on the latest public status (17 Aug 2026).[^pse-nte-broker-forum-2026-07-09:9][^pse-analyst-briefing-1h-2026:9] **The broker layer is small, concentrated and thinly capitalised**: 123 trading participants are listed, ten of them accounted for 65% of broker-ranked value (buy plus sell) on 5 Oct 2026, grandfathered brokers still need only P30 million of capital, and brokers do fail (Equitiworld, suspended on an SEC order in October 2024, is still being liquidated).[^pse-web-tp-directory][^pse-web-broker-ranking][^pse-rules-trading-rights-trading-participants:9][^pse-cn-2026-0012:2]

## The institutional map

Who does what, from order entry to settlement, who owns whom, and where each rulebook lives.

| Step | Institution | Role | Ownership, status, key dates | Rulebook |
|---|---|---|---|---|
| Order and order entry | **Trading participants (TPs)** | Licensed broker-dealers holding PSE trading rights; the only route to the book. The TP applies risk checks and per-trader order-value limits (per order, not per day), then sends orders from its PSE-certified FEOMS or a PSETradeX terminal to the Common Customer Gateway (FIX 5.0 SP1); one FEOMS log-in per TP.[^pse-implementing-guidelines-trading-rules:17][^pse-implementing-guidelines-trading-rules:31] | 123 listed on 6 Oct 2026; for equities, clearing membership is limited to TPs.[^pse-web-tp-directory][^sccp-clearing-house-rules-2018:18] | TP Rules (SEC-approved 28 May 2009);[^pse-rules-trading-rights-trading-participants:3] Implementing Guidelines |
| Matching | **PSE** | The only stock exchange and a front-line SRO: engine (XTS; Eqlipse planned 23 Nov 2026), listing, market data, clearing and settlement services; trade feed to SCCP, ITCH feed to vendors.[^pse-annual-report-2025:8][^pse-web-psetrade-xts] | Stock corporation since 3 Aug 2001; listed by introduction 15 Dec 2003; exchange licence 4 Mar 1994, SRO certificate 29 Jun 1998.[^pse-annual-report-2025:8][^pse-corp-history] | Revised Trading Rules, DMA Rules, circulars (CN-yyyy-nnnn, TPA-yyyy-nnnn);[^pse-web-reg-trading-participants] [Chapter 3](#/ch/sessions) to [Chapter 7](#/ch/price-controls) |
| Surveillance and discipline | **CMIC** | Independent audit, surveillance and compliance arm; disciplines TPs; halts and suspends securities and failing TPs.[^pse-corp-regulatory-framework] | 100% PSE; provisional SRO status from 2 Feb 2012.[^pse-annual-report-2025:8][^pse-corp-history] | CMIC Rules v1.2, SEC-approved 12 Jan 2012[^pse-cmic-rules:2] |
| Clearing | **SCCP** | Central counterparty by novation at clearing-member (not beneficial-customer) level; DVP; Clearing and Trade Guaranty Fund (CTGF); fails management.[^sccp-web-services][^sccp-clearing-house-rules-2018:26] | 100% PSE (since 2004); incorporated 23 Jan 1996; operating 3 Jan 2000; permanent licence 17 Jan 2002.[^sccp-web-about-2026-05-17][^pse-corp-history] | Clearing House Rules (the 13 Mar 2018 text is still the one posted; T+2 amendments are in memo 06-0823):[^sccp-memo-06-0823-sec-approval-t2-amendments:2] [Chapter 10](#/ch/clearing-settlement) |
| Cash leg | **Settlement banks; BSP** | Each clearing member holds a Cash Settlement Account and a Cash Collateral Deposit Account (PHP, and USD for dollar-denominated securities) with a settlement bank that confirms cash to SCCP online; SCCP cannot settle when PhilPaSSplus (BSP's RTGS) or Philippine Clearing House Corp. clearing is closed.[^sccp-clearing-house-rules-2018:13][^sccp-cs-quick-guide:5][^sccp-memo-07-0823-sec-approved-amendments:7] | SCCP's Partners page shows nine bank logos (Asia United, BDO, China Bank, Deutsche Bank, EastWest, Maybank, Metrobank, RCBC, UnionBank); automatic-debit enrolment is with BDO or RCBC.[^sccp-web-partners][^sccp-web-membership] | SCCP rules; BSP FX Manual ([Chapter 14](#/ch/foreign-access)) |
| Settlement (T+2) and registry | **PDTC** (PDS Group) | Depository and registry with dual SEC and BSP oversight; securities leg by book entry. Funds and securities are due by 12:00 noon on settlement date (late-delivery fines from 12:00; preventive suspension if uncured by 09:15 on SD+1); shares not lodged stay with issuers or transfer agents.[^pds-web-company-overview][^sccp-memo-06-0823-sec-approval-t2-amendments:2][^pse-analyst-briefing-1h-2026:18] | PSE beneficially owns **94.55%** of PDS Holdings (4 Feb 2026), up from 20.98%.[^pse-17c-2026-02-04-pdic-pdshc-shares:3][^pse-annual-report-2025:9] | PDTC rules; [Chapter 10](#/ch/clearing-settlement) |
| Safety net | **SIPF** | Securities Investors Protection Fund: compensates customers for broker fraud, business failure or insolvency; automatic on opening an account with a PSE-accredited broker.[^pse-web-investing-at-pse] | Established 2 Oct 1979;[^pse-corp-history] coverage cap not public | SRC §36.5 |
| Oversight | **SEC** | Pre-approves every PSE, CMIC and SCCP rule; licenses brokers; orders the take-over of a failed TP; may suspend trading in a listed security.[^ra-8799-src-lawphil][^sec-2015-src-irr:154] | RA 8799 (Securities Regulation Code, SRC); the 2015 IRR took effect 9 Nov 2015.[^sec-2015-src-irr-notice-of-effectivity:1] | SRC, IRR, memorandum circulars |

### PSE: form, ownership and governance

PSE lists itself on its own board under a memorandum of understanding with the SEC, which posts PSE's disclosures to PSE EDGE.[^pse-17c-2025-05-22-nasdaq-eqlipse-contract:1] Statute caps control: no person may hold more than 5% of the voting rights and no industry group more than 20% (brokers and dealers count as one group); brokers may fill at most 49% of the board; the president and at least 51% of the other directors must be independents or issuer and investor representatives not broker-affiliated for two years; the SEC may order divestment.[^ra-8799-src-lawphil][^sec-2015-src-irr:110][^sec-2015-src-irr:111] A 2018 rights offering (P2.90 billion) moved broker holdings towards the cap (19.9% in May 2020), and on 30 Jan 2024 the Supreme Court ruled on the 2010 Nomelec broker-voting rules (injunction against the SEC reversed, against PSE and PSE Nomelec affirmed).[^pse-corp-history][^pse-annual-report-2025:11] At 31 Mar 2026 PSE had 316 holders of record; PCD Nominee accounts held 62.60% (Filipino) and 10.73% (non-Filipino), foreign ownership was 12.45% and the public float 65.72%; the 15-member board is chaired by Jose T. Pardo, with Ramon S. Monzon as President and CEO.[^pse-annual-report-2025:13][^pse-annual-report-2025:62][^pse-corp-board]

### The SEC and the rule-approval channel

PSE, CMIC and SCCP rules take effect only through the SEC, which may also alter or abrogate SRO rules on hours of trading, minimum units of trading, odd lots and settlement timing (SRC §40.4); lot size, tick size and the odd-lot market are therefore SEC-level matters.[^ra-8799-src-lawphil]

| Provision | Content |
|---|---|
| SRC §33.1(d); IRR Rule 33.1(d).3 | Every exchange must take over an insolvent member on SEC order: suspend it, transfer its accounts to another TP, liquidate its trading right and trade-related assets, notify the accredited trust fund.[^sec-2015-src-irr:109] |
| SRC §36.1, §36.4, §36.5; IRR Rules 36.4.4.5, 36.5 | Summary suspension of a listed security; SEC rules on clearance and settlement, which may require a central counterparty; every broker-dealer must belong to an SEC-accredited trust fund, and business failure is determined without a judicial insolvency declaration.[^ra-8799-src-lawphil][^sec-2015-src-irr:119][^sec-2015-src-irr:120] |
| SRC §28.4(b); IRR Rule 28.1.2.5.1; SRC §42.2(f) | Minimum net capital and bond; a TP needs good-standing exchange membership, trust-fund participation and clearing-fund contributions; a clearing agency's guarantee fund is sized on the exposure of the four largest trading brokers.[^ra-8799-src-lawphil][^sec-2015-src-irr:77] |
| **IRR Rule 40.3** | Prior SEC approval of any SRO rule or amendment. A proposal of major significance is published at least 30 days before approval (comment period at most 20 days). Within 60 days of submission the SEC must approve by order or institute proceedings; if it does not, the SRO may declare the proposal effective; if proceedings are not concluded within 90 days of commencement, the SRO makes it effective. Purely administrative matters take effect after 10 business days; emergency summary effectivity is allowed.[^sec-2015-src-irr:154] |

<div class="callout infer">
<span class="label">Inference</span>

"Awaiting SEC approval" is not a public yes or no. Rule 40.3 gives an SRO a route to effectiveness when the SEC neither approves nor opens proceedings within the windows, so a rule could take effect without a published approval letter. No filing dates were found for the lot-size, run-off or negotiated-trade amendments, so the clocks cannot be dated. Treat PSE's effectivity circular, not an SEC letter, as the trigger for version-gating, and expect rule and engine changes to be announced together.
</div>

### CMIC: surveillance and enforcement

CMIC took over PSE's former Market Regulation Division; its surveillance system (TMS, acquired from the Korea Exchange) launched on 8 May 2012 and a replacement is on PSE's 2026 technology list.[^pse-corp-group-structure][^pse-corp-history][^pse-analyst-briefing-3m-2026:24] Its jurisdiction covers TP violations of securities laws and CMIC rules and trading irregularities involving issuers; issuer disclosure and listing duties stay with PSE.[^pse-cmic-rules:9][^pse-cmic-rules:11] TPs owe a best-execution duty, "reasonable diligence to ascertain the best available price" (Art. VII §31); CMIC monitors capital (Art. VIII), may impose involuntary suspension (Art. X §7) and treats marking the close and wash sales as irregularities (Art. XI).[^pse-cmic-rules:58][^pse-cmic-rules:59][^pse-cmic-rules:106][^pse-cmic-rules:117] CMIC decides at first instance; appeal lies to the CMIC Board within 10 business days (5 for summary actions) and, for grave or major violations, to the SEC within 15 calendar days (SEC MC 10 of 2010), so PSE is not in the appeal chain.[^pse-cmic-rules:17] Sanctions escalate from reprimand and fines (grave: P25,000 to P200,000 first; major: P10,000 up to at least P75,000) to denial of the trading right and a bar (Art. XII §4).[^pse-cmic-rules:119][^pse-cmic-rules:120] Independence rests on structure only (100% PSE ownership, a separate SEC-approved rulebook, SEC appeals); board composition and funding were not found.

### PDS Group: PSE's depository and fixed-income arm

PDS Holdings (PDSHC) owns PDEx (SEC-registered fixed-income exchange and SRO, incorporated 2003), PDTC (depository and registry, incorporated 1995) and PDS Academy.[^pds-web-company-overview]

| Date | Event | PSE stake |
|---|---|---|
| 2004 to Dec 2024 | PSE invests in PDS Holdings in exchange for its Philippine Central Depository shares; a 2017–18 attempt to buy control lapses (the Inquirer reported the SPA timetable ended 31 Mar 2018; PSE's 17-C denied saying it would stay a minority holder).[^pse-corp-history][^pse-17c-2018-04-16-pds-deal-clarification:3] | 20.98% (associate)[^pse-annual-report-2025:19] |
| 26 Dec 2024 | SPAs for a further 61.92%: BAP 28.8335%, SGX 20%, WTSI 8%, SMC 4%, IHAP 0.65%, Golden Astra 0.3606%, Mizuho 0.08%; plan to acquire up to 100%.[^pse-17c-2024-12-26-pdshc-acquisition-agreements:3][^pse-infographic-fy24:1] | |
| 27 Dec 2024 | The SGX, WTSI, SMC and Golden Astra block (32.36%) closes; consolidated at end-2024.[^pse-ir-all-disclosures][^pse-annual-report-2025:19] | 53.34% |
| 24 Feb 2025; end-Mar 2025; 15 May 2025; 30 May 2025 | PSE press releases and the 2025 annual-meeting report.[^pse-press-fy2024-results][^pse-press-q1-2025-results][^pse-asm-2025-presidents-report:32] | 78.33%; 79.9%; 91.6%; 92.06% |
| 22 Dec 2025 | Land Bank sells 2.15% (134,372 shares at P600); reported by The Philippine Star only.[^philstar-pds-landbank-2025-12-24] | 94.21% (secondary) |
| **4 Feb 2026** | PDIC sells 0.34%; closed the same day.[^pse-17c-2026-02-04-pdic-pdshc-shares:3] | **94.55%** |
| 5 Mar 2026 | Restated in PSE's 3M2026 briefing.[^pse-analyst-briefing-3m-2026:25] | 94.55% |

No later figure was found; the press names DBP (3.08%) as the remaining holder and PSE says it will pursue the rest in 2026.[^philstar-pds-landbank-2025-12-24][^pse-annual-report-2025:36] PSE's stated rationale is a single exchange for fixed income and equities, vertical integration of the depository with trading and clearing, and derivatives.[^pse-17c-2024-12-26-pdshc-acquisition-agreements:4] The integration roadmap (4 Jul and 17 Aug 2026): phase 1 (ongoing) consolidates 13 systems; **phase 2, targeted for 2027, is a single post-trade system for clearing, settlement and depository**, with fixed-income assets accepted as clearing-member collateral and wider Name-on-Central-Depository coverage; PDTC is also replacing its depository system.[^pse-asm-2026-president-report:28][^pse-analyst-briefing-1h-2026:31][^pse-analyst-briefing-3m-2026:24] Depository assets were P6.08 trillion at end-Jun 2026, of which equities P5.45 trillion, only **41.9%** of the market value of domestic listed companies, and debt P632 billion (43.0% of debt in the registry); PDTC shows 164 registered securities, 42 issuers and 256 depository participants (1 Oct 2026).[^pse-analyst-briefing-1h-2026:18][^pds-web-home]

### SIPF

In a TP failure the exchange or CMIC notifies the SIPF, which may pay validated claims before the exchange finishes settling the failed TP's liabilities and is then subrogated to them (CMIC Rules, Art. VII §30, para. c).[^pse-cmic-rules:57] An accredited trust fund compensates customers only for "actual damages" and must have SEC-approved rules on required balance, assessments, borrowing, payout and board composition (IRR Rule 36.5).[^sec-2015-src-irr:120] The per-investor cap and the fund's size could not be found: sipf.com.ph is a parked domain and no PSE, CMIC or SEC document reviewed states them.

### Execution implications

- There is no routing problem: optimise intraday scheduling, broker selection and counterparty risk. After novation your counterparty is SCCP at **clearing-member** level; exposure to the broker, its custodian and its settlement bank remains, so custody belongs with a clearing member that is not a thinly capitalised TP and the broker-failure process belongs in your operational-risk file.
- Rule changes arrive as PSE circulars and SCCP memos, often tied to SEC approval and the engine cut-over: monitor both and version every parameter by effective date.
- Only 41.9% of domestic equity value sits in the depository, so scrip eligibility checks belong in the order workflow ([Chapter 10](#/ch/clearing-settlement)); BSP and PhilPaSS closures stop settlement even when PSE trades ([Chapter 3](#/ch/sessions)). The 2027 single post-trade system may change SCCP-PDTC interfaces and collateral rules (inference; no rule text yet).

## Trading system

### Lineage

| Date | System | Note |
|---|---|---|
| 1993 to 1995 | Manila SE Stratus/Equicom (4 Jan 1993); Makati SE "MakTrade" (15 Jun 1993); Unified Trading System on MakTrade software (13 Nov 1995) | The two floors unified on 23 Dec 1992.[^pse-corp-history] |
| 26 Jul 2010 | "PSEtrade" New Trading System (NTS) | NYSE Euronext Technologies SAS (NSC platform); migration took about two years; Implementing Guidelines (memo 2010-0340) effective on launch.[^pse-annual-report-2015:42][^pse-implementing-guidelines-trading-rules:1] |
| 29 Oct 2013 | SEC-approved DMA Rules | Effective the first trading day of 2014.[^pse-dma-rules:1][^pse-memo-sec-approved-dma-rules-2013-11-26:1] |
| 22 Jun 2015 | **PSEtrade XTS** (Nasdaq X-stream, OMX Technology AB) | Selection announced 1 Jul 2014 (press reprint); planned go-live 1 Jun 2015 slipped three weeks, reason not documented.[^mondovisione-nasdaq-omx-selected-2014][^pse-annual-report-2015:42][^pse-fix-itch-session-week21-2015-05-22:3] |
| 27 Jun 2022 | Floorless trading | Floors closed 24 Jun 2022.[^pse-corp-history] |
| 22 May 2025 | Contract with Nasdaq Technology AB for **Nasdaq Eqlipse Trading** | Multi-asset "fourth generation" platform.[^pse-17c-2025-05-22-nasdaq-eqlipse-contract:2][^pse-corp-eqlipse-press-release] |
| **23 Nov 2026** | **Planned Eqlipse go-live** | Big bang, no parallel run.[^pse-nte-broker-forum-2026-07-09:9][^pse-nte-faq-2026-08:1] |

<div class="callout warn">
<span class="label">Scheduled change: 23 Nov 2026, subject to SEC approval</span>

XTS is current until Nasdaq Eqlipse ("NTE", PSE's new trading engine) goes live on **Monday 23 Nov 2026**, after Saturday rehearsals on 31 Oct, 7 Nov and 14 Nov; there is no parallel run, and on Day 1 only limit orders are supported.[^pse-nte-broker-forum-2026-07-09:9][^pse-nte-faq-2026-08:1] New FIX (Session Gateway, Order Entry, Drop Copy), ITCH and market-data-feed specifications replace the XTS ones. Rule changes tied to the engine, and their status on PSE's 17 Aug 2026 slide: **One Lot One Share** (1-share lots for PHP and USD securities, odd-lot market abolished, TPs may set a minimum order value) with a 10-band tick table in place of today's 15 bands, "For SEC Approval", targeted Q4 2026; run-off orders entered, modified and executed only at the closing price, proposed with the lot rule; **Negotiated Trades**, "Revising per Public Comments".[^pse-analyst-briefing-1h-2026:9][^pse-asm-2026-president-report:22][^pse-nte-user-group-2026-01-15:9] No SEC approval or effectivity circular had been found by 6 Oct 2026, and no PSE notice on the project after 25 Sep. Never present NTE parameters as current. The master pipeline is in [Chapter 17](#/ch/reform-timeline), tick and lot tables in [Chapter 4](#/ch/order-types), and the version-gated design in [Chapter 16](#/ch/execution-implications).
</div>

### PSEtrade XTS in production

PSE stated in 2015 that "PSEtrade-XTS Trading Engine can handle 10,000 orders per second"; the engine was built with "three times more capacity" than its predecessor and average trades per day rose 39.0% from a little over 38,000 (2014) to 53,000 (2015); for scale, 5 Oct 2026 saw 70,275 trades and 414.3 million shares worth P3.743 billion.[^pse-fix-itch-session-week21-2015-05-22:13][^pse-annual-report-2015:6][^pse-annual-report-2015:8][^sccp-web-home] **No latency figure is published**; the ITCH specification says only that the protocol suits "low latency messaging".[^pse-itch-equities-feed-spec-v2-3:7] XTS runs PROD and DR sites with same-day recovery (the previous platform needed the next trading day); every TP must keep a back-up terminal connected to the DR site, and broker gateways fail over to DR addresses only if the TP has a leased line to DR.[^pse-annual-report-2015:42][^pse-implementing-guidelines-trading-rules:30][^pse-broker-failover-fallback-plan:3] A private order book holds orders off-market for later release, and GTC or GTD orders outside the static threshold take an "unplaced" status and re-activate next day if inside the new thresholds.[^pse-web-psetrade-xts]

### Protocols

**Order entry: FIX 5.0 SP1** through the Common Customer Gateway (specification v2.5, 10 Aug 2015, OMX Technology AB).

| Topic | Rule |
|---|---|
| Session | DefaultApplVerID 8 only; Logon first and nothing sent before the response; **no encryption or compression** (use private lines or VPN); username up to 30 and password up to 10 characters. Test Request after HeartBtInt plus up to 6 s; session dropped after 2 x HeartBtInt + 6 s (HeartBtInt 30 gives 66 s).[^pse-fix-specification-v2-5:8][^pse-fix-specification-v2-5:11][^pse-fix-specification-v2-5:14] |
| Messages | Inbound: New Order Single (D), New Order Cross (s; CrossType must be 1, all-or-none), Cancel (F), Cancel/Replace (G), Trade Capture Report (AE, block and privately negotiated trades). Outbound: Execution Report (8), Cancel Reject (9), TCR Ack (AR).[^pse-fix-specification-v2-5:10][^pse-fix-specification-v2-5:16] |
| Identity | Account up to 14 characters; ExecutingTrader party (role 12); optional give-up clearing firm (role 14); SecuritySubType N normal, O odd-lot, I index board.[^pse-fix-specification-v2-5:15][^pse-fix-specification-v2-5:47][^pse-fix-specification-v2-5:48] |
| Enumerations | OrdType 1 Market, 2 Limit, 3 Stop, 4 Stop-Limit; TimeInForce 0 Day, 1 GTC, 3 IOC, 4 FOK, 6 GTD, 8 Session; Side 1, 2, 5 Short Sell, Z Buy Back; ExecInst S and q move an order to and from the private book; MinQty (110) and DisplayQty (1138) are defined. Which of these the rules enable is a [Chapter 4](#/ch/order-types) question.[^pse-fix-specification-v2-5:50][^pse-fix-specification-v2-5:52][^pse-fix-specification-v2-5:53] |
| Identifiers | ClOrdID up to 20 characters, unique per trading day and across all of a firm's FIX connections (X-stream may not check); OrderID can change after an amendment, so track ClOrdID chains.[^pse-fix-specification-v2-5:15][^pse-fix-specification-v2-5:25] |
| Amendment | Quantity, display quantity, price, order type, time in force, expiry, give-up firm, account, MinQty, text, trigger price, ExecInst and side (buy to buy-in, sell to short sell) may change; **a price or trigger-price change or a quantity increase loses priority**.[^pse-fix-specification-v2-5:25][^pse-fix-specification-v2-5:26] |
| Start of day | Open GT orders are restated by unsolicited Execution Reports even while you are disconnected, so the outbound sequence number may be higher at logon: recover with ResendRequest.[^pse-fix-specification-v2-5:9] |

**Market data: ITCH over SoupBinTCP.** Point-to-point ITCH uses SoupBinTCP v3.0 with case-sensitive credentials; MoldUDP64 multicast is specified, but nothing reviewed says PSE uses it; the XTS-era specification is v2.3 (5 Oct 2018; v1.0 was 19 May 2014).[^pse-itch-equities-feed-spec-v2-3:2][^pse-itch-equities-feed-spec-v2-3:7] Products are ITCH Total View (every order at every price level), Basic (best bid and offer plus last sale), News, and an ETF iNAV every minute.[^pse-annual-report-2015:44] Broker anonymity is switchable "as announced by the exchange": if it is not in force, Order Executed [e], Order Executed with Price [c] and Trade [p] carry the Broker ID; if in force, the anonymous variants [E], [C], [P] are sent.[^pse-itch-equities-feed-spec-v2-3:25] PSE said on 3 Oct 2014 it would implement anonymity "but not on Go-Live" and no activation was found, so broker IDs on executions are probably visible but unconfirmed ([Chapter 11](#/ch/market-data) holds the evidence).[^pse-fix-itch-session-week01-2014-10-03:11] Eqlipse keeps separate dedicated TCP connections for ITCH and for the new market-data feed (MDF), both over SoupBinTCP.[^pse-nte-faq-2026-08:3]

### Access channels

| Channel | What it is | Facts |
|---|---|---|
| **FEOMS** | Broker-operated front end, PSE-certified, on the Common Customer Gateway | 2015: about 15 FEOMS certified and 33 TPs launched their own; 2026: **40 TPs** run their own (plus 7 data vendors and 21 TPs on market data). One log-in per TP; PSE may impose message-flow controls; bureau-service operation of a TP's FEOMS is prohibited.[^pse-annual-report-2015:44][^pse-nte-broker-forum-2026-07-09:5][^pse-implementing-guidelines-trading-rules:31][^pse-implementing-guidelines-trading-rules:32] |
| **PSETradeX** | PSE-hosted service bureau, introduced 2012 (FlexTrade "Mottai" front end since the 2017 switch from N2N; Check Point VPN or leased line; four broker silos) | P10,400 per account for the first three and P7,800 from the fourth (unit not stated); **5,000 accounts per broker**; 2FA replaces the RSA token; GTC and next-day validity being removed; cloud migration deferred (9 Jul 2026); terminal needs Windows 10 Pro 64-bit and Internet Explorer 11.[^pse-annual-report-2025:55][^pse-nte-broker-forum-2026-07-09:11][^pse-nte-user-group-2026-01-15:17][^pse-psetradex-installation-guidelines:9][^pse-web-new-trading-engine] |
| **DMA** | Client orders go straight to the matching system: Automatic Order Routing, or Sponsored Access (QIBs only) | Below; algorithmic and high-frequency use prohibited.[^pse-dma-rules:7] Five TPs launched DMA in 2015.[^pse-annual-report-2015:44] |
| **Online brokers** | 22 TPs are listed as online brokers (among them COL Financial, First Metro, BDO Securities, BPI Securities, AB Capital, DragonFi) | 35 TPs supplied online-account data for 2025.[^pse-web-tp-directory][^pse-investor-profile-2025:2] |

**Connectivity.** Leased lines from PLDT, ETPI or Globe with Ethernet hand-over; a 100 Mbps drop-wire exists for PSE Tower (BGC) tenants only; the website lists 1 Mbps minimum and 2 Mbps recommended, and the January 2026 deck sets 2 Mbps minimum for the new parallel UAT lines; each TP needs at least two leased lines (PROD and UAT or DR).[^pse-web-new-trading-engine][^pse-nte-user-group-2026-01-15:7][^pse-nte-faq-2026-08:2] **There is no co-location or proximity hosting** in any PSE, XTS or NTE document; the drop-wire is the only proximity feature.[^pse-web-psetrade-xts][^pse-web-new-trading-engine] Access to Eqlipse interfaces and documentation needs a sub-licence agreement with PSE (Nasdaq a third-party beneficiary, no Nasdaq liability), a leased line to test and production, and FEOMS re-certification; the FIX specifications (Session Gateway, Order Entry, Drop Copy: v0.1 30 Jan, v1.1 8 Jun 2026) and ITCH and MDF specifications (v1.0 29 Jan, v1.1 8 Jun, v1.2 17 Jul 2026) are released on e-mail request only.[^pse-nte-user-group-2026-01-15:4][^pse-nte-user-group-2026-01-15:5][^pse-web-new-trading-engine]

### DMA rules and algorithmic trading

| Item | Rule |
|---|---|
| Definitions | **DMA**: a client enters orders, modifications and cancellations directly into the PSE matching system for automatic execution without TP intervention. **Algorithmic trading**: an algorithm decides timing, price or quantity, or initiates the order without human intervention. **High-frequency trading**: algorithmic trading entering or cancelling orders over **sub-second intervals**.[^pse-dma-rules:2] |
| Services | Automatic Order Routing (internet trading or straight-through processing) and Sponsored Access (QIB clients only, orders reaching the engine without passing through the TP's infrastructure).[^pse-dma-rules:3] |
| **Restriction** | **Section 9(e): "The DMA Facility shall not be used for High-Frequency and/or Algorithmic trading."**[^pse-dma-rules:7] |
| Requirements | Certification (and re-certification on significant changes); designated and alternate SEC-licensed trader; five trading days' notice; pre-trade filters set before access and reviewed daily (trade exposure, order size by value or volume, price limit in percent or ticks from the last traded or adjusted close); wash-sale prevention; daily reconciliation; 5-year logs; annual DR test and third-party stress and penetration tests.[^pse-dma-rules:5][^pse-dma-rules:6][^pse-dma-rules:8][^pse-dma-rules:9][^pse-dma-rules:10] |
| Fees (excluding VAT) | P10,000 installation; P2,500 certification or re-certification; P10,000 monthly; P5,000 development testing.[^pse-dma-rules:6] |
| Sanctions, effectivity | PSE may disconnect without notice and suspend or revoke on SCCP, CMIC or SEC recommendation; the DMA Rules take precedence over the Common Customer Gateway guidelines. SEC transmittal 29 Oct 2013; effective the first trading day of 2014 with a six-month transition.[^pse-dma-rules:10][^pse-dma-rules:11][^pse-memo-sec-approved-dma-rules-2013-11-26:1] |

**The unapproved 2023 proposal.** CN-2023-0043 (5 Sep 2023; comments to 19 Sep 2023) proposed folding the DMA Rules into the Revised Trading Rules and adding "Algorithmic Trading is allowed by the Exchange": programmed entry of a **Parent Order** would not be allowed and **Child Orders must be limit orders**; each algorithmic order type on DMA would need a letter to PSE and PSE's written no-objection, child orders would pass the DMA TP's risk checks, HFT would stay barred, a parent-child identifier would be required, and PSE could suspend algorithms or cancel all DMA orders. The paper records that PSE had already granted exemptions for child orders of conditioned parent orders.[^pse-cn-2023-0043:3][^pse-cn-2023-0043:6][^pse-cn-2023-0043:8][^pse-cn-2023-0043:9] Only the VWAP part was adopted (Closing VWAP session live 1 Mar 2024); no approval circular for the algorithmic amendments was found, and PSE's regulatory-framework page lists only the 2013 DMA Rules and the VWAP rules.[^pse-cn-2024-0012-vwap-go-live:1][^pse-web-reg-trading-participants]

<div class="callout">
<span class="label">Consequence</span>

A third-party execution algorithm cannot be hosted on a client's DMA connection under the rules in force. Algorithms live where the broker's own system generates the child orders, and the only public statement of what is tolerated is the 2023 paper's note on exemptions for child orders of conditioned parent orders. Inference: that means broker-side conditioned orders with limit-order children, HFT excluded everywhere; the exemptions are unpublished, so their scope and any message-rate conditions must be established with the broker before building.
</div>

### Throttles, message limits and capacity

No numeric order-rate or message-rate limit is published. What exists: PSE's reserved right to impose message-flow controls on a FEOMS; one FEOMS session per TP; a per-trader **value limit per order** set by the TP within the Exchange's cap (temporary raises need a form a day ahead; per order, not per day); DMA pre-trade filters; and PSETradeX's 5,000-account cap.[^pse-implementing-guidelines-trading-rules:17][^pse-implementing-guidelines-trading-rules:31][^pse-nte-user-group-2026-01-15:17] The only Eqlipse capacity figures come from The Philippine Star (23 Jul 2026), not PSE: "five million orders and 450,000 trades", an 11-hour session, up to 10,000 securities, 15 million client accounts, 1,000 brokers and 1,200 market-data connections, at P241.03 million (engine) plus P45.83 million (back office).[^philstar-nte-2026-07-23]

### Outage and incident record

| Date | Event | Stated cause | Notice |
|---|---|---|---|
| 4 Jan 2022 | Opening delayed, then **trading cancelled for the day**; 43 of 125 TPs could not connect | Connection between the Nasdaq trading engine and the FlexTrade front end | CN-2022-0001, -0002[^pse-cn-2022-0001-delay-market-opening:1][^pse-cn-2022-0002-cancellation-of-trading-2022-01-04:1] |
| 3 Jan 2024 | Halted 09:32, resumed 11:56 (2 h 24 m); afternoon 13:00 to 15:00 as scheduled | "Technical issue"; third-party front-end provider investigating; no root cause published | CN-2024-0001 to -0003[^pse-cn-2024-0001-market-halt:1][^pse-cn-2024-0003-update-market-halt:1] |
| 9 Dec 2024 | Pre-open 09:40, no-cancel 09:50, open **09:55** (25 minutes late) | None stated | CN-2024-0061[^pse-cn-2024-0061-adjusted-schedule-2024-12-09:1] |
| 24 Mar 2025 | Open **11:10** (no-cancel 11:05), about 1 h 40 m late | "System connectivity issue" | CN-2025-0014, -0015[^pse-cn-2025-0014:1][^pse-cn-2025-0015-adjusted-schedule-2025-03-24:1] |
| 19 Jan, 6 Oct 2026 | PSE EDGE disclosure systems unavailable (disclosure, not trading); emergency-disclosure procedure; no trading halt noted | Not stated | CN-2026-0003, -0046[^pse-cn-2026-0003:1][^pse-cn-2026-0046-edge-outage-access-to-disclosures:1] |

Non-technical closures also stop the chain: 13 Jan 2020 (Taal ash) and 26 Sep 2022 (typhoon) halted trading and SCCP clearing and settlement; 24 Jul 2024 (floods) halted trading.[^pse-cn-2020-0002-trading-suspension-2020-01-13:1][^pse-cn-2022-0035-trading-suspension-2022-09-26:1][^pse-cn-2024-0038-trading-suspension-2024-07-24:1] The 4 Jan 2022 failure (43 of 125 TPs, 34%) met the old market-halt trigger of one-third of TPs unable to connect.[^pse-cn-2022-0001-delay-market-opening:1] **Since 20 Aug 2025** the trigger is that TPs accounting for more than 50% of six-month average daily value (excluding block sales) cannot trade, directly or through their correspondent TP; every TP must have a **Correspondent TP** as business continuity (two months' grace); and PSE may halt, suspend or cancel a day for natural disasters if its continuity plan fails (PAGASA signal 3 to 5 in the National Capital Region means no trading).[^pse-cn-2025-0037:1][^pse-cn-2025-0037:2][^pse-cn-2025-0037:4] Under the 2010 Implementing Guidelines a Common Customer Gateway failure halts the market for its duration plus ten minutes, and a TP may direct a mass cancel only after a FEOMS or Gateway failure.[^pse-implementing-guidelines-trading-rules:18][^pse-implementing-guidelines-trading-rules:30] Halt mechanics: [Chapter 7](#/ch/price-controls).

<div class="callout infer">
<span class="label">Inference</span>

Where a cause is stated (4 Jan 2022, 3 Jan 2024, 24 Mar 2025) it is the connectivity or front-end layer, not matching logic, and two of the three name the third-party front-end provider. The PSE-hosted gateway and front-end stack is the weak point, and the Eqlipse cut-over replaces both it and the engine, so expect elevated incident risk in the first weeks.
</div>

### Replacement project: Nasdaq Eqlipse Trading

PSE's 22 May 2025 agreement covers a modular multi-asset platform (pre-trade risk, index calculation and options-pricing modules; flexible deployment including cloud); the stated purposes are a single lot size, derivatives, new market-data products and real-time index feeds.[^pse-corp-eqlipse-press-release][^pse-web-new-trading-engine]

| Date | Milestone |
|---|---|
| Jun to Jul 2026 | Customer-test connectivity; credentials 6 to 10 Jul (same FIX credentials, new market-data credentials, ports and IPs); TEST from 13 Jul; final FIX, ITCH and MDF specifications 23 Jul per the August FAQ (PSE's page dates ITCH and MDF v1.2 17 Jul).[^pse-nte-broker-forum-2026-07-09:4][^pse-nte-faq-2026-08:2] |
| 10 to 23 Sep 2026 | FEOMS certification (earlier on request, later allowed).[^pse-nte-broker-forum-2026-07-09:9][^pse-nte-faq-2026-08:2] |
| 29 Sep to 22 Oct 2026 | Pre-production connectivity testing (to 9 Oct), then testing (12 to 22 Oct).[^pse-nte-broker-forum-2026-07-09:9] |
| Sat 31 Oct, 7 Nov, 14 Nov | Market rehearsals in pre-production over the new production links, with PSE scripts.[^pse-nte-broker-forum-2026-07-09:9][^pse-nte-faq-2026-08:1] |
| **Mon 23 Nov 2026** | **Go-live, big bang** |

Readiness on 9 Jul 2026: of 40 TPs with their own FEOMS, 18 were analysing and developing FIX, 9 analysing only, 2 had not started and 11 had not responded; for UAT links 1 had completed connectivity testing, 3 were testing, 3 in telco installation, 17 in telco talks, 5 not started and 11 silent; of 28 market-data parties 10 were developing, 12 had not started and 6 were silent.[^pse-nte-broker-forum-2026-07-09:5][^pse-nte-broker-forum-2026-07-09:6] The August FAQ is inconsistent on whether new server IPs exist (supplied with credentials since 10 Jul, or "not yet available; only point-to-point testing completed").[^pse-nte-faq-2026-08:3] Also scheduled with the engine: removal of PSETradeX GTC and next-day validity, retirement of the DTR end-of-day file for the new PSE Portal (live 3 Aug 2026), and inclusion of Negotiated Trades in value and the consolidated trade file.[^pse-nte-user-group-2026-01-15:19][^pse-nte-faq-2026-08:2] Derivatives (PSEi index futures) remain at exposure-draft and funding-talks stage.[^pse-analyst-briefing-1h-2026:10]

<div class="callout warn">
<span class="label">Currency: slippage prior and an unresolved calendar</span>

PSE targets have slipped before: XTS moved from 1 Jun to 22 Jun 2015, and a 2023 board-lot cut was filed with the SEC and never approved ([Chapter 17](#/ch/reform-timeline) holds the slippage record).[^pse-fix-itch-session-week21-2015-05-22:3] On 25 Sep 2026 PSE issued CN-2026-0043 declaring 16 to 18 Nov regular trading days and the same day CN-2026-0044 superseded it, promising a final advisory; the last rehearsal (Sat 14 Nov) falls just before that calendar settles.[^pse-cn-2026-0043:1][^pse-cn-2026-0044:1] No postponement notice existed on 6 Oct 2026.
</div>

### Execution implications

- **Order tracking and recovery:** key on ClOrdID chains, not OrderID; a price or trigger change or quantity increase loses priority ([Chapter 5](#/ch/matching)); expect a burst of GT restatements and a sequence gap at logon (ResendRequest); there is no wire encryption, so private lines or VPN only.
- **Kill procedures:** cancel-on-disconnect is not documented for XTS (orders stay live; mass cancel only on request after a FEOMS or Gateway failure), so the broker's kill switch and your own cancel-all path are the control; whether Eqlipse adds cancel-on-disconnect is unknown (inference).
- **Shared gateway and algorithm hosting:** one FEOMS session per TP and a reserved right to throttle mean your flow shares a pipe with the broker's other clients; get message-rate, order-value and position limits in writing (none is published) and assume algorithms run in the broker's system (conditioned parent, limit children), not on DMA; establish its exemption status.
- **Cut-over:** avoid large programmes around 23 Nov 2026 and the three rehearsal Saturdays; confirm the broker's FEOMS certification and UAT status (1 of 40 FEOMS TPs had finished connectivity testing by 9 Jul); parameterise lot, tick and odd-lot logic per security and engine version; Day 1 is limit-only, so slicers must not rely on market or stop orders or GTC.
- **No co-location:** the latency edge is leased-line quality and the broker gateway; do not invest in proximity infrastructure. Against about 70,000 trades a day and a published 10,000 orders per second, the broker gateway and 1 to 2 Mbps lines, not the engine, set practical limits (inference). Market-data access needs a sub-licence or vendor ([Chapter 11](#/ch/market-data)).
- **Incident prior:** four technical disruptions in 2022 to 2025 (one full-day cancellation, one 2.4-hour halt, two late opens) justify standing resume logic and a manual fallback.

## Trading participants

### Counts and status

| Date | Count | Source |
|---|---|---|
| At demutualisation | Cap of 184 trading rights ("no more than 184") | TP Rules[^pse-rules-trading-rights-trading-participants:7] |
| Feb 2018; 4 Jan 2022 | 132 active TPs; 125 TPs | PSE release; CN-2022-0001[^pse-pr-trading-floor-closed-2022-06-24][^pse-cn-2022-0001-delay-market-opening:1] |
| 2022 to 2025 | Annual-survey respondents 130, 123, 121 (active), 122: survey coverage, not rosters | Investor profiles[^pse-smip-2022:2][^pse-smip-2023:2][^pse-smip-2024:2][^pse-investor-profile-2025:2] |
| End-2024, end-2025, end-Jun 2026 | **121 active TPs** | PSE infographics[^pse-infographic-fy24:1][^pse-infographic-fy25:1][^pse-infographic-2q26:1] |
| 2 Jun, 20 Jul 2026 | 123 entries each, including two suspended firms | Directory PDFs[^pse-active-tp-summary-2026-06-02:1][^pse-active-tp-summary-2026-07-20:1] |
| 6 Oct 2026 | **123 TPs: 121 active (114 local, 7 foreign), 2 suspended** (Equitiworld, Mount Peak) | PSE web directory, no as-of stamp[^pse-web-tp-directory] |
| 6 Oct 2026 | **125 clearing members: 122 active, 3 suspended** (EquitiWorld, Jaka, Mount Peak); 118 local, 7 foreign | SCCP membership page[^sccp-web-membership] |
| 14 Sep 2025 | 124 clearing members: 123 active, 1 suspended; 113 local, 11 foreign | SCCP page, Wayback snapshot[^sccp-web-membership-2025-09-14] |

<div class="callout warn">
<span class="label">Conflicting rosters: report each, do not merge</span>

The registries differ in population and date. SCCP lists 125 clearing members against 123 TPs in PSE's directory; one named difference is Jaka Securities, a suspended clearing member absent from PSE's directory. CMIC suspended Benjamin Co Ca and Co., Inc. on 31 Jul 2026, yet the firm is in neither 2026 directory PDF and was not recorded among the two suspended firms on the 6 Oct web directory, so its status is unconfirmed.[^pse-tpa-2026-0035-benjamin-co-ca-involuntary-suspension:1] "Foreign" is 7 on both 6 Oct 2026 lists but was 11 on SCCP's archived list (adding Apex Philippines Equities, HDI Securities, Yao and Zialcita and Deutsche Regis Partners); the flag is undefined. Firms rename (HDI to CNN Securities, Deutsche Regis Partners to Regis Partners, Maybank ATR Kim Eng to Maybank Securities, MVG to Caballes-Go, among others), so key brokers on broker code, not name.[^sccp-web-membership-2025-09-14][^pse-web-tp-directory][^pse-active-tp-summary-2026-07-20:1]
</div>

The directory's "Type" field (123 rows): Retail 63, Institutional/Retail 29, Institutional 17, and fourteen other combinations; "minimum investment" runs from P0 to P1 million (BDO Securities P500,000; Maybank, Regis Partners, Century, David Go and East West Capital P1 million).[^pse-web-tp-directory] Seven TPs are flagged foreign: CLSA Philippines, J.P. Morgan Securities Philippines, Macquarie Capital Securities (Philippines), Maybank Securities, UBS Securities Philippines, UOB-Kay Hian Securities (Philippines) and Seedbox Securities; four are typed institutional and one institutional/retail.[^pse-web-tp-directory]

### The trading-right model

Rules Governing Trading Rights and Trading Participants (SEC approval 28 May 2009; PSE memo 2009-0316).

| Feature | Rule |
|---|---|
| Nature | Each of the 184 members at demutualisation received a trading right ("the right to operate as a broker/dealer of securities in the Exchange"), evidenced by a certificate that is not a shareholding: one per TP, **no vote at PSE meetings and no share of PSE's assets**.[^pse-rules-trading-rights-trading-participants:6] |
| Form and admission | A domestic corporation licensed by the SEC (foreign brokers operate as local subsidiaries) and not connected with another TP; admitted by at least 8 Board votes; entrance fee at least P200,000; a transfer of 51% or more of shares within 12 months needs Board approval; a Board-approved Nominee (at least 21, resident; fee P50,000) is ultimately responsible.[^pse-rules-trading-rights-trading-participants:8][^pse-rules-trading-rights-trading-participants:9][^pse-rules-trading-rights-trading-participants:10][^pse-rules-trading-rights-trading-participants:12] |
| Pledge | Each TP pledges its trading right (full value) to secure client, government, Exchange, SCCP and other-TP claims, unless it posts an acceptable guarantee (standby letter of credit, surety bond, pledge of PSE or index shares, or government securities).[^pse-rules-trading-rights-trading-participants:7] |
| Transfer | Sale with Board approval, SEC, SCCP, PDTC and PSE clearances, newspaper publication, a 30-day claims window and escrow with PSE; a ceased TP's right reverts to the Board.[^pse-rules-trading-rights-trading-participants:13][^pse-rules-trading-rights-trading-participants:14] |
| Start of operations | SEC licence; broker code and "trading cap" from Market Operations; stock-broker bond P5 million and dealer bond P1 million "or such other amount as may be prescribed by the SEC"; at least one licensed associated person and salesman; trading within a year of approval.[^pse-rules-trading-rights-trading-participants:14][^pse-rules-trading-rights-trading-participants:15] |

### Capital and prudential rules

| Item | In force on 6 Oct 2026 | PSE proposal (21 Jul 2026) | SEC exposure draft (24 Sep 2026) |
|---|---|---|---|
| Unimpaired paid-up capital (UPUC), first-time registrants or acquirers joining a clearing agency | P100 million[^sec-2015-src-irr:77] | Unchanged, "or such higher amount as may be required by law"[^pse-memo-tp-paid-up-capital-increase-2026-07:4] | **P120 million for all broker-dealers**[^pse-memo-2026-10-01-sec-rfc-src-28-1-33-1-capital:4] |
| UPUC, existing TPs that deferred compliance with P100 million | **P30 million** (P20 million from 31 Dec 2009, P30 million from 31 Dec 2010); SEC letter: applies "only to TPs who opted to defer"[^pse-rules-trading-rights-trading-participants:4][^pse-rules-trading-rights-trading-participants:9] | At least P50 million by 31 Dec 2027; P100 million by 31 Dec 2029[^pse-memo-tp-paid-up-capital-increase-2026-07:3] | P30 million route deleted; at least P100 million by 31 Dec 2029 and P120 million by 31 Dec 2030[^pse-memo-2026-10-01-sec-rfc-src-28-1-33-1-capital:5] |
| Surety bond | P12 million (PSE's July 2026 paper); IRR floor P10 million (brokers), P2 million (dealers)[^pse-memo-tp-paid-up-capital-increase-2026-07:3][^sec-2015-src-irr:87] | P12 million to P20 million by 31 Dec 2028 for TPs not at P100 million | At least P20 million from 31 Dec 2028 for TPs still on the P30 million route; fixed IRR amounts replaced by exchange-rule amounts[^pse-memo-2026-10-01-sec-rfc-src-28-1-33-1-capital:5] |
| Proprietary-only dealers with no client securities | P2.5 million[^sec-2015-src-irr:78] | Not addressed | Retained[^pse-memo-2026-10-01-sec-rfc-src-28-1-33-1-capital:4] |
| Effectivity | Current | None; no SEC approval or final circular found | On complete publication[^pse-memo-2026-10-01-sec-rfc-src-28-1-33-1-capital:6] |

<div class="callout warn">
<span class="label">Pending change: capital increases, not in force</span>

Two proposals exist and neither is in force. PSE's consultation (comments to 31 Jul 2026) lifts existing TPs to P50 million by 2027 and P100 million by 2029.[^pse-memo-tp-paid-up-capital-increase-2026-07:1] The SEC's own exposure draft (En Banc 24 Sep 2026, relayed by PSE on 1 Oct, comments to 14 Oct 2026) sets P120 million for every broker-dealer and abolishes the P30 million route; it cites inflation (P100 million in 2004 equals about P230.5 million in 2026 prices).[^pse-memo-2026-10-01-sec-rfc-src-28-1-33-1-capital:1][^pse-memo-2026-10-01-sec-rfc-src-28-1-33-1-capital:3] The SEC rule is the senior instrument; the end-dates align at 31 Dec 2028 (bond) and 31 Dec 2029 (P100 million), but the SEC draft goes further.
</div>

**Risk-based capital** (SEC MC 16 of 2004, restated in IRR Rule 49.1): RBCA ratio at least 1.1; net liquid capital (NLC) at least the higher of P5 million and 5% of aggregate indebtedness (P2.5 million and 2.5% for proprietary-only dealers without custody); indebtedness at most 2,000% of NLC; SEC notice within 24 hours above 1,700% or below a 1.2 ratio; equity withdrawals barred if NLC would fall below 120% of the minimum or indebtedness exceed 1,500% of net capital; the firm must stop business at once if the ratio falls below 1.1 or NLC below the minimum; computation daily, reports due the 20th and the 5th.[^pse-rbca-rules:19][^pse-rbca-rules:20][^sec-2015-src-irr:166][^sec-2015-src-irr:167] CMIC applies the same thresholds and can suspend a TP for uncured breaches; reports are not public.[^pse-cmic-rules:106]

### Proprietary activity and commissions

SRC §34.1 generally bars a member-broker from trading for its own or associated accounts except as market maker, in odd lots, to offset errors or as the SEC defines; IRR Rule 34.1 replaces the flat ban with the **"Customer First" policy**: customer orders are executed immediately on receipt, take priority over the TP's own, have their receipt time recorded and are executed by the assigned trader; staff and insider accounts count as proprietary.[^ra-8799-src-lawphil][^sec-2015-src-irr:111][^sec-2015-src-irr:112] PSE classes trader IDs as proprietary, client or "PC" (at most two PC traders per TP, only one handling both on a day); a market-making TP may not hold a proprietary account in its stock.[^pse-implementing-guidelines-trading-rules:8][^pse-implementing-guidelines-trading-rules:9] No figure exists for the proprietary share of turnover. **Commissions:** SEC MC 7 of 2024 (16 Apr 2024) removed PSE's minimum-commission schedule (0.25% to 0.05% of trade value) with effect from 18 Apr 2024; PD 154's 1.5% ceiling remains ([Chapter 12](#/ch/costs)).[^pse-cn-2024-0029-min-commission-removal:1][^pse-cn-2024-0029-min-commission-removal:2]

### Concentration

Broker ranking, 5 Oct 2026 15:00 (PSE top-10 frame, share of value traded; foreign-owned in bold):

| Rank | Broker | Share | Rank | Broker | Share |
|---|---|---|---|---|---|
| 1 | Mandarin Securities | 11.46% | 6 | **Maybank ATR Kim Eng** | 6.00% |
| 2 | **UBS Securities Philippines** | 8.90% | 7 | COL Financial | 5.80% |
| 3 | **Macquarie Capital Securities** | 7.88% | 8 | First Metro Securities | 5.04% |
| 4 | SB Equities | 6.51% | 9 | Philippine Equity Partners | 3.74% |
| 5 | **CLSA Philippines** | 6.25% | 10 | Regis Partners | 3.41% |

Top 5: 41.0%; **top 10: 64.99%**; the four foreign-owned firms 29.03%; COL Financial led by volume (78.8 million shares). The day's value was P3.743 billion on 414.3 million shares and 70,275 trades, so broker values are two-sided (inference from the ranking's construction).[^pse-web-broker-ranking][^sccp-web-home] The only full report archived (February 2020) gave a top 5 near 40%, a top 10 near 63% and six foreign-owned firms near 40% of two-sided value (own computation).[^pse-monthly-report-sample:1][^pse-monthly-report-sample:21] Broker codes in market data (February 2020): Mandarin 200, UBS 333, CLSA 323, J.P. Morgan 185, Macquarie 121, COL 203, BDO Securities 279, Maybank 220, SB Equities 115, Philippine Equity Partners 338, Regis 209, First Metro 267.[^pse-monthly-report-sample:21] The non-regular market (blocks and similar) is about 17% of value: year to August 2026 average daily value P7,561 million, regular P6,247 million, non-regular P1,314 million.[^pse-monthly-report-2026-08:1] PSE sells a TP Ranking Report (P40 an issue, P80 a quarter, January to March 2026 rate).[^pse-cn-2026-0001:1] Longer series: [Chapter 15](#/ch/empirical).

### Broker failure and the safety net

| Firm | Event | Status |
|---|---|---|
| DW Capital, Inc. | SEC order of 5 Dec 2017 directing PSE to take over its operations | Court of Appeals affirmed 8 Oct 2018 (final 4 Jul 2019); Supreme Court petition (G.R. 245845) pending per the FY2025 report[^pse-annual-report-2025:11][^pse-annual-report-2025:12] |
| R&L Investments | CMIC allocation and liquidation plan for trade-related assets (April 2023) | Historical[^pse-cn-2023-0017:1] |
| Equitiworld Securities | SCCP suspended it as a clearing member 25 to 27 Mar 2024 for repeated late cash payments (Feb 2020 to Nov 2023); SEC involuntary suspension and preservation order (CMIC notified 9 Oct 2024); SEC approved early release of "intact" shares on 9 Jun 2025 and a multi-tranche allocation plan on 17 Mar 2026, with CMIC to coordinate with the SIPF | Still suspended in the 6 Oct 2026 directory[^sccp-memo-03-0324-clearing-member-suspension:1][^pse-cn-2024-0053-equitiworld-involuntary-suspension:1][^pse-cn-2025-0027:2][^pse-cn-2026-0012:2] |
| Globalinks Securities and Stocks | CMIC involuntary suspension from 9 Jul 2025 for continuing capitalisation breaches | Lifted 14 Oct 2025 after a capital infusion[^pse-tpa-2025-0040-globalinks-involuntary-suspension:1][^pse-tpa-2025-0061-globalinks-lifting-of-suspension:1] |
| Mount Peak Securities | CMIC involuntary suspension from 13 Aug 2025 (investigations over capitalisation and other securities-law compliance) | Still suspended in the directory[^pse-tpa-2025-0050-mount-peak-involuntary-suspension:1] |
| Benjamin Co Ca and Co. | CMIC involuntary suspension from 31 Jul 2026 | Directory status unconfirmed[^pse-tpa-2026-0035-benjamin-co-ca-involuntary-suspension:1] |

During an involuntary suspension the firm's access to the PSE trading system, PDTC's online system and SCCP's clearing facilities is restricted; client transfers and done-through sells may be allowed with CMIC approval; proprietary and related-party trades are barred or may be.[^pse-tpa-2025-0040-globalinks-involuntary-suspension:1] Clients re-open accounts at active TPs while the SIPF process runs in parallel.[^pse-cn-2025-0027:2]

### Execution implications

- Institutional flow runs through roughly 6 to 9 TPs (foreign-owned institutional firms held 4 of the top 6 on 5 Oct 2026) while about 110 mostly retail-typed firms carry most accounts (inference): use at least two institutional brokers and benchmark them with the TP Ranking Report; commissions are negotiable (no minimum, 1.5% cap).
- Ask each broker for FEOMS certification and Eqlipse UAT status, RBCA and NLC headroom (not public) and its stance on the capital proposals; a P30 million cushion is thin against P7.5 billion of daily value (inference), which favours clearing members with bank or foreign parents.
- "Customer First" and CMIC's best-execution duty put clients ahead of the broker's book but promise no price improvement: run your own cost analysis against VWAP.
- Key rosters on broker code and refresh them from both PSE and SCCP (a suspension can appear on SCCP's list or in a CMIC notice first); rehearse the failure path, where asset release can take years.

## Investor base

| Year (reporting TPs) | Total accounts | Online | Local / foreign | Retail / institutional | Active share |
|---|---|---|---|---|---|
| 2018 | 1,089,413 | n/a | n/a | n/a | n/a |
| 2021 | 1,620,017 | n/a | n/a | 1,589,507 / 30,510 | n/a |
| 2022 (130) | 1,712,734 | 1,258,907 (73.5%) | 1,684,167 / 28,567 (1.7%) | 1,680,572 / 32,162 (1.9%) | 20.2% |
| 2023 (123) | 1,906,019 | 1,525,768 (80.0%) | 1,878,304 / 27,715 (1.5%) | 1,877,213 / 28,806 (1.5%) | 17.6% |
| 2024 (121) | 2,860,234 | 2,471,860 (86.4%) | 2,830,358 / 29,876 (1.0%) | 2,827,950 / 32,284 (1.1%) | 23.1% |
| 2025 (122) | **3,641,067** | 3,226,616 (**88.6%**) | 3,608,358 / 32,709 (0.9%) | 3,611,157 / 29,910 (0.8%) | **11.8%** |

Sources: 2018;[^pse-asm-2024-presidents-report:12] 2021 and 2022;[^pse-smip-2022:2][^pse-smip-2022:3] 2023;[^pse-smip-2023:2][^pse-smip-2023:3] 2024;[^pse-smip-2024:2][^pse-smip-2024:3] 2025.[^pse-investor-profile-2025:2][^pse-investor-profile-2025:3] The 2025 total is +27.3% on 2024 (5-year CAGR 21.1%) and online accounts are 99.9% retail.[^pse-asm-2026-president-report:15][^pse-smip-2024:2] The infographics do not define "active" (the one definition found, "traded at least once in the year", is in the 2013 edition; see [Chapter 15](#/ch/empirical)); 35 TPs reported online data in 2025 against 38 or 39 earlier.[^pse-investor-profile-2025:2] Growth drivers: the stock transaction tax cut from 0.6% to 0.1% on 1 Jul 2025 ([Chapter 12](#/ch/costs)), GCash "G-Stocks" with AB Capital (September 2022) and other app brokers, and the PERA promotion.[^pse-annual-report-2025:39][^pse-corp-history]

Share of value traded (PSE annual stockholders' meeting report):[^pse-asm-2026-president-report:7]

| | 2024 | 2025 | 6M2025 | 6M2026 |
|---|---|---|---|---|
| Local / foreign | 53.8 / 46.2 | 53.7 / 46.3 | 51.7 / 48.3 | 50.5 / **49.5** |
| Retail / institutional (5M2025 and 5M2026 in the last two columns) | 18.9 / 81.1 | 18.2 / 81.8 | 17.2 / 82.8 | 19.1 / 80.9 |

The foreign share was 45.0% in August 2026 and 48.3% year to date (46.9% a year earlier); PSE's weekly statistics show 55% for 28 Sep to 2 Oct and 49% year to 2 Oct (mean of foreign buying and selling over total value).[^pse-monthly-report-2026-08:2][^pse-weekly-market-watch-2026-10-02:3] Net foreign selling was P51.20 billion in 2025, P11.36 billion in H1 2026 and P20.86 billion in January to August 2026 (P45.43 billion a year earlier), reaching P31.53 billion by 2 Oct.[^pse-infographic-fy25:1][^pse-infographic-2q26:1][^pse-monthly-report-2026-08:2][^pse-weekly-market-watch-2026-10-02:3] Summed daily foreign figures run 2 to 3 points above the official annual ratio ([Chapter 15](#/ch/empirical)).

| Scale | End-2024 | End-2025 | End-Jun 2026 | Latest |
|---|---|---|---|---|
| Average daily value (P billion) | 6.10 | 7.33 | 7.72 | 7.56 (Jan to Aug); 7.71 (to 2 Oct 2026) |
| Market capitalisation (P trillion) | 20.01 | 18.73 | 19.44 | 19.82 (end-Aug); 19.44 (2 Oct 2026; domestic issues 12.46) |
| Listed companies | 283 | 282 | 281 | 280 (14 Aug 2026) |

Sources:[^pse-asm-2026-president-report:6][^pse-infographic-fy24:1][^pse-infographic-fy25:1][^pse-infographic-2q26:1][^pse-analyst-briefing-1h-2026:3][^pse-monthly-report-2026-08:2][^pse-weekly-market-watch-2026-10-02:3] The PSEi closed at 5,629.03 on 2 Oct 2026 (-3.4% on the week, -7.0% year to date). Common shares are 99.7% of value (August 2026); preferred shares, warrants and PDRs, dollar-denominated issues, ETFs and the SME board together average under P30 million a day.[^pse-monthly-report-2026-08:1]

### Execution implications

- Model about half of value as foreign and about 80% as institutional; retail is a small, noisy residual, not a source of liquidity for size. The 3.6 million accounts are an account-count story: if "active" means traded in the year, active accounts fell from about 661,000 (23.1% of 2,860,234) in 2024 to about 430,000 in 2025 despite 27% account growth (inference).
- Net foreign flow, published daily and monthly, is a core signal and risk factor (foreign share 46.2% in 2024, 49.5% in 6M2026). One Lot One Share would lower the minimum ticket and may raise small-order message traffic, but not institutional liquidity (inference).

## Regional links

| Link | Status |
|---|---|
| ASEAN Exchanges | Bursa Malaysia, Indonesia Stock Exchange, PSE, SGX, SET and Vietnam Exchange (VNX joined; 39th CEOs Meeting in Vietnam, 2026); PSE hosted the 38th on 21 Feb 2025; ASEAN-ISE sustainability-data RFI February 2025; **depositary-receipt MOU 21 Nov 2024**; the stated aim is "linkages that would allow investors to trade across borders easily".[^aseanexchanges-web-about][^pse-annual-report-2025:28][^pse-asm-2025-presidents-report:28][^pse-corp-global-alliances] |
| ASEAN Trading Link | Launched 18 Sep 2012 with Bursa Malaysia and SGX, SET joining 15 Oct 2012 (secondary source). No PSE report or briefing reviewed (2015, 2024 to 2026) mentions it and none lists PSE as a participant.[^wikipedia-asean-exchanges] |
| SGX-PSE MSCI Philippines Index Futures | Co-branded, listed on SGX on 25 Nov 2013; whether it still trades, and how actively, was not checked.[^pse-corp-history] |
| Other | FTSE/ASEAN index MoA (2005); MOUs with Shenzhen SE (Jan 2023), Taiwan SE (Aug 2024) and Taipei Exchange (10 Jun 2025).[^pse-corp-history][^pse-asm-2025-presidents-report:28] |
| PSE derivatives | PSEi index futures first: early exposure draft to selected institutions, an RFI to technology vendors "last July", funding talks with multilaterals; no launch date.[^pse-analyst-briefing-1h-2026:10] |

### Execution implications

- The SGX-listed MSCI Philippines futures are the only exchange-traded index hedge in PSE's materials (liquidity unchecked); there is no onshore index future yet. Otherwise the hedge is a basket of constituents, since PSE-listed ETFs trade only about P0.93 million a day (August 2026), which keeps hedging on the same venue and T+2 cycle (inference; see [Chapter 9](#/ch/short-selling)).
- There is no cross-venue arbitrage or Trading Link routing for PSE equities; foreign institutions reach the market through locally incorporated foreign broker subsidiaries or global brokers' local TPs (inference).

## What is not in the public record

- SIPF coverage cap and fund size; CMIC board composition, and why its SRO status is still called provisional.
- Any latency figure, engine or DR site location, numeric message-rate limit or cancel-on-disconnect behaviour; the field-level Eqlipse specifications (sub-licence needed) and whether GTC, GTD, stop and market orders return after Day 1.
- The amended Implementing Guidelines for the Gateway and message controls: the posted text is the 22 Jul 2010 edition and amendments exist (TPA 2011-0124; Part XXI in 2025).[^pse-tpa-2011-0124-amended-implementing-guidelines:1]
- Root causes of the 3 Jan 2024, 9 Dec 2024 and 24 Mar 2025 incidents.
- Whether PSE has re-confirmed 23 Nov 2026 since the September readiness window; the SEC's decision on the board-lot, run-off and negotiated-trade amendments; whether the 2023 algorithmic-trading amendments were ever approved and what exemptions PSE has granted.
- The proprietary share of turnover, broker market shares for 2024 to 2026, the Exchange's own order-value limit, the current broker-code list and the second firm behind the 125 versus 123 roster gap.
- The definition of an "active" account since 2022, the online share of value, the local and foreign split of institutions, and whether "retail" includes foreign retail.
- Primary confirmation of PSE's non-participation in the ASEAN Trading Link, activity in the SGX-PSE MSCI Philippines futures, and PSE's PDS stake after 4 Feb 2026.
