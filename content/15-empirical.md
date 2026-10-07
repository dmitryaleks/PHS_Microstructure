---
number: 15
slug: empirical
title: Empirical Liquidity and Market Quality
summary: A thin, concentrated, foreign-sensitive market whose closes often print the day's extreme; spreads and depth are not public and PSE-specific microstructure research is almost absent.
part: Evidence and synthesis
---

The Philippine Stock Exchange has a domestic capitalisation of about PHP 13–15tn (roughly US$210–240bn at PHP 62.8/USD) but trades only PHP 6–9bn a day: PHP 7.33bn in 2025 and PHP 7.71bn year-to-date to 2 Oct 2026.[^pse-monthly-report-2025-12:1][^pse-weekly-report-2026-10-02:1] About 5 bp of market value changes hands per day, annual turnover was 10–13% of domestic capitalisation in 2023–2025, and the OECD ranks the PSE's 2023 turnover ratio (8.8%) lowest of six ASEAN peers.[^oecd-capital-market-review-philippines-2024:42] Value is concentrated (the ten most-traded names are about 60% of regular-market value on a median day), foreign-sensitive (foreigners were 46–49% of trade sides in 2024–2026 and have been net sellers in every year since 2022) and lumpy (block sales are 11–21% of headline average daily value, and single prints of PHP 25–110bn have produced days up to 19 times the trailing median).

Three behaviours most often break assumptions carried over from other venues. First, the headline turnover figure includes block sales and odd lots that a participation algorithm cannot trade against. Second, the closing print is not a neutral reference: the PSEi closed on the day's high or low on 38% of sessions in 2019–2026 (a random walk gives about 1–8%), and in the ten most liquid stocks the close or open lands on the day's high or low about five times as often as chance. Third, nothing about the quality of the book is published. Effective spreads, depth, intraday volume and the closing auction's share of volume are in no PSE document, and no study of tick size, price limits, the closing auction, board lots or broker-ID transparency on the PSE has been found. Every spread, impact and intraday figure below is therefore an end-of-day proxy or a statistic **computed from PSE daily reports** (labelled, with its sample period, and never a PSE-published figure) and should be treated as a prior to be replaced by measurements from your own market-data capture. Data run to 2 Oct 2026 (weekly report) and 5 Oct 2026 (daily reports).

## How to read the evidence

| Class | Source | How it is labelled |
|---|---|---|
| PSE-published | Annual reports, Monthly Report previews, the weekly report, infographics, the Stock Market Investor Profile (SMIP), annual-meeting President's Reports, circulars | Cited to document and page |
| Third-party | OECD (2024), academic papers, press | Named in the text; press-only facts say so |
| Computed | Parsed from PSE reports: 391 one-page Weekly Reports (3 May 2019 – 2 Oct 2026; 1,813 daily PSEi rows) and 373 Daily Quotation Reports (176 sampled days, two per month Jun 2019 – Sep 2026; 28 consecutive sessions 26 Aug – 5 Oct 2026; 164 month-end and month-start sessions Jan 2024 – Sep 2026; 26 event days)[^pse-weekly-reports-dataset][^pse-dqr-dataset] | "Computed", with sample period. Only individually cited reports are archived |

Conventions of PSE's own statistics:

- **ADVT** is average daily value traded. The total market is the regular market plus the non-regular market, and non-regular means block sales plus odd-lot trades.[^pse-monthly-report-sample:11]
- **Foreign ratio** is (foreign buying + foreign selling) ÷ (2 × total value traded): the share of trade *sides* that are foreign, not a share of ownership (2017: 1,970.23 ÷ (2 × 1,958.36) = 50.3%).[^pse-annual-report-2017:17]
- **Total market capitalisation** includes three foreign-domiciled issuers; **domestic** excludes them (end-2024: 20.01tn total, 14.57tn domestic).[^pse-monthly-report-2024-12:2]
- Rough USD figures use PSE's own rate of PHP 62.775/USD on 2 Oct 2026.[^pse-eod-daily-quotation-2026-10-02:10]

### Rule regimes inside the sample

Statistics span several rule sets. Read a number against the regime in force on its dates; rule detail is in the chapters linked.

| From | Change | Reading consequence | Chapter |
|---|---|---|---|
| 4 Nov 2013 | Pre-close 15:15–15:20, run-off 15:20–15:30, close 15:30[^pse-memo-pre-close-schedule-2013:1][^pse-memo-extended-pre-close-implementation-2013:1] | Close at 15:30 until the March 2020 cut | [3](#/ch/sessions), [6](#/ch/auctions) |
| 16–19 Mar 2020 | Shortened hours (close 13:00); no trading 17–18 Mar; trading resumed 19 Mar[^pse-cn-2020-0017:1][^pse-cn-2020-0021:1][^pse-cn-2020-0025-resumption-of-trading:1] | A morning-only session, pre-close 12:45, run-off 12:50, until 3 Dec 2021 | [3](#/ch/sessions) |
| 24 Mar 2020 | Lower static threshold cut from 50% to 30% below the reference price; upper stays +50% (circular dated 21 Mar)[^pse-cn-2020-0028:1] | Floor hits are 30% moves, not 50% | [7](#/ch/price-controls) |
| 4 May 2020 | Single 10% index breaker replaced by 10/15/20% levels (15/30/60-minute halts)[^pse-cn-2020-0044:1] | Pre-May-2020 breaker history is a different rule | [7](#/ch/price-controls) |
| 6 Dec 2021 | Full-day schedule with 13:00 resume and 15:00 close; shortened again to a 13:00 close from 14 Jan 2022 (announced to 31 Jan; the end on 28 Feb is implied by the 1 Mar restoration)[^pse-cn-2021-0059:1][^pse-cn-2022-0004:1][^pse-cn-2022-0009-trading-schedule-mar-2022:1] | PSE's circular calls this schedule "pre-pandemic", but the pre-March-2020 market resumed at 13:30 and closed at 15:30; do not repeat the label | [3](#/ch/sessions) |
| 6 Nov 2023 | Short-selling programme live; Daily Short Sell Report starts[^pse-short-sell-report-2023-11-06:2] | Short volume is zero throughout (below) | [9](#/ch/short-selling) |
| 1 Mar 2024 | Closing VWAP session 15:00–15:15; official close 15:15[^pse-approved-rules-vwap-trading-2024:3][^pse-cn-2024-0012-vwap-go-live:1] | The pre-close call and run-off still end at 15:00 | [3](#/ch/sessions) |
| 1 Jul 2025 | Stock transaction tax 0.6% to 0.1% of the seller's gross value[^pse-cn-2025-0028-cmepa-effectivity:1][^bir-rr-20-2025-stt:4] | Cost-sensitive turnover before and after is not comparable | [12](#/ch/costs) |
| 20 Aug 2025 | Market-halt trigger changed from one-third of trading participants to participants above 50% of six-month ADTV[^pse-cn-2025-0037:1] | Outage-halt history before and after differs | [7](#/ch/price-controls) |
| 11 Aug 2026 | SEC-approved tiered minimum-public-ownership rule effective immediately[^pse-amended-mpo-rule-2026-08:1] | Float statistics below pre-date it | [2](#/ch/instruments), [13](#/ch/regulatory-constraints) |
| 23 Nov 2026 (scheduled) | Nasdaq Eqlipse engine go-live; see the warning callouts below[^pse-nte-broker-forum-2026-07-09:9] | Every calibration here needs re-estimating | [17](#/ch/reform-timeline) |

## Headline statistics, 2013–2026

**Market size and turnover.** PSE-published figures except the velocity column, which is computed here as value traded ÷ year-end domestic capitalisation.

| Year | PSEi close (change) | Total MCAP (PHP tn) | Domestic MCAP (PHP tn) | Value traded (PHP tn) | ADVT (PHP bn; days) | Velocity (computed) | Source |
|---|---|---|---|---|---|---|---|
| 2013 | 5,889.83 (+1.3%) | 11.93 | 9.65 | 2.55 | 10.52 | 26.4% | [^pse-annual-report-2017:17] |
| 2014 | 7,230.57 (+22.8%) | 14.25 | 11.71 | 2.13 | 8.80 | 18.2% | [^pse-annual-report-2017:17] |
| 2015 | 6,952.08 (-3.9%) | 13.47 | 11.19 | 2.15 | 8.96 | 19.2% | [^pse-annual-report-2017:17] |
| 2016 | 6,840.64 (-1.6%) | 14.44 | 11.87 | 1.93 | 7.81 | 16.3% | [^pse-annual-report-2017:17] |
| 2017 | 8,558.42 (+25.1%) | 17.58 | 14.49 | 1.96 | 8.06 | 13.5% | [^pse-annual-report-2017:17] |
| 2018 | 7,466.02 (-12.8%) | 16.15 | 13.54 | 1.74 | 7.15 | 12.8% | [^pse-annual-report-2018:32] |
| 2019 | 7,815.26 (+4.7%) | 16.71 | 13.95 | 1.77 | 7.29 (243) | 12.7% | [^pse-annual-report-2019:32][^pse-monthly-report-2019-12:1] |
| 2020 | 7,139.71 (-8.6%) | 15.89 | 13.10 | 1.77 | 7.35 (241) | 13.5% | [^pse-monthly-report-2020-12:1][^pse-monthly-report-2020-12:2] |
| 2021 | 7,122.63 (-0.2%) | 18.08 | 14.56 | 2.23 | 9.00 (248) | 15.3% | [^pse-monthly-report-2021-12:1][^pse-monthly-report-2021-12:2] |
| 2022 | 6,566.39 (-7.8%) | 16.56 | 13.28 | 1.79 | 7.30 (245) | 13.5% | [^pse-monthly-report-2022-12:1][^pse-monthly-report-2022-12:2] |
| 2023 | 6,450.04 (-1.8%) | 16.74 | 13.10 | 1.47 | 6.09 (242) | 11.2% | [^pse-monthly-report-2023-12:1][^pse-monthly-report-2023-12:2] |
| 2024 | 6,528.79 (+1.2%) | 20.01 | 14.57 | 1.49 | 6.10 (245) | 10.2% | [^pse-monthly-report-2024-12:1][^pse-monthly-report-2024-12:2] |
| 2025 | 6,052.92 (-7.3%) | 18.73 | 13.65 | 1.78 | 7.33 (243) | 13.0% | [^pse-monthly-report-2025-12:1][^pse-monthly-report-2025-12:2] |
| 2026 to 2 Oct | 5,629.03 (-7.0%) | 19.44 | 13.06 (end-Aug) | 1.43 (computed: 7.714bn × 186) | 7.71 (186) | n/a | [^pse-weekly-report-2026-10-02:1][^pse-monthly-report-2026-08:1] |

Index changes for 2014–2016 are computed from year-end closes; the others are as printed. The 2018 domestic figure was restated from 13.54tn to 13.55tn.[^pse-annual-report-2019:32] On total capitalisation velocity is lower (2023 8.8%, 2024 7.4%, 2025 9.5%, computed). ADVT as basis points of domestic capitalisation per day (computed) was 10.9 (2013), 5.2–5.6 (2017–2020), 6.2 (2021), 4.2 (2024) and 5.4 (2025). The OECD independently reports a 2023 PSE turnover ratio of 8.8% (peer mean 49%, range 22–87%), US$24.9bn traded in 2023 (lowest of the six) and a Main Board turnover ratio averaging 14% over 2010–2023.[^oecd-capital-market-review-philippines-2024:42] Value traded rose 19.1% in 2025 and was PHP 1.22tn in January–August 2026 (+7.3% year on year) and PHP 926.54bn of equities in 1H26 against 809.27bn in 1H25.[^pse-monthly-report-2026-08:2][^pse-analyst-briefing-1h-2026:7]

**Regular versus non-regular value.** Block sales and odd lots are 11–21% of headline ADVT, so the regular-market ADV an algorithm can reach is 79–89% of the headline.

| Period | Non-regular share of ADVT | Source |
|---|---|---|
| 2019 | 14.2% (1,036.72 of 7,294.56m) | [^pse-monthly-report-2019-12:1] |
| 2020 | 11.2% | [^pse-monthly-report-2020-12:1] |
| 2021 | 18.0% (1,619.65 of 9,002.10m; computed from PSE figures) | [^pse-monthly-report-2021-12:1] |
| 2022 | 18.9% (one 14 Dec block lifted December's non-regular ADVT to PHP 7,173.64m) | [^pse-monthly-report-2022-12:1] |
| 2023 | 20.7% | [^pse-monthly-report-2023-12:1] |
| 2024 | 15.6% | [^pse-monthly-report-2024-12:1] |
| 2025 | 18.8% (1,374.68 of 7,328.26m) | [^pse-monthly-report-2025-12:1] |
| Jan–Aug 2026 | 17.4% (1,314.15 of 7,561.17m); regular ADV PHP 6.25bn | [^pse-monthly-report-2026-08:1] |

**Trading days:** 243 (2019), 241 (2020), 248 (2021), 245 (2022), 242 (2023), 245 (2024), 243 (2025); 162 to end-August 2026 and 186 to 2 Oct 2026.[^pse-monthly-report-2019-12:1][^pse-monthly-report-2020-12:1][^pse-monthly-report-2021-12:1][^pse-monthly-report-2022-12:1][^pse-monthly-report-2023-12:1][^pse-monthly-report-2024-12:1][^pse-monthly-report-2025-12:1][^pse-monthly-report-2026-08:1][^pse-weekly-report-2026-10-02:1]

**Listings and capital raised.**

| Year | Listed companies (year-end) | IPOs (count; primary proceeds PHP bn) | Capital raised, PSE basis (PHP bn) | Source |
|---|---|---|---|---|
| 2013 | 257 | count not recorded; 60.98 | 175.07 | [^pse-annual-report-2017:17] |
| 2014 | 263 | count not recorded; 11.41 | 153.08 | [^pse-annual-report-2017:17] |
| 2015 | 265 | 4; 5.20 | 184.60 | [^pse-annual-report-2015:32] |
| 2016 | 265 | 4; 28.92 | 176.80 | [^pse-annual-report-2016:33] |
| 2017 | 267 | 4; 22.53 | 164.76 | [^pse-annual-report-2017:16] |
| 2018 | 267 | 1; 8.15 | 187.84 | [^pse-annual-report-2018:9][^pse-annual-report-2018:32] |
| 2019 | 268 | 4; 13.41 | 94.48 | [^pse-annual-report-2019:31][^pse-annual-report-2019:32] |
| 2020 | not found | count not stated; 44.3 | about 104 (press basis; 2019 about 101 on the same basis) | [^bw-336789][^pse-monthly-report-2020-12:1] |
| 2021 | 276 | 8; proceeds not extracted | 234.48 (record; previous high 228.33 in 2012) | [^pse-monthly-report-2021-12:2][^pse-infographic-fy21:1] |
| 2022 | 286 | 10 new listings including REITs | 99.17 (primary) | [^pse-monthly-report-2022-12:2][^pse-infographic-fy22:1] |
| 2023 | 283 | 3 listings | 140.75 (primary) | [^pse-monthly-report-2023-12:2][^pse-infographic-fy23:1] |
| 2024 | 283 | 3 (OGP, CREC, XG) | 75.78 (primary; 82.37 on the press basis) | [^pse-monthly-report-2024-12:2][^pse-infographic-fy24:1][^pse-press-2024-12-27] |
| 2025 | 282 | 2 (TOP, Maynilad "MYNLD") | 138.75 (primary; 144.14 on the press basis) | [^pse-monthly-report-2025-12:2][^pse-infographic-fy25:1][^pse-press-2025-12-29] |
| 2026 to 2 Oct | 280 | no IPO priced; PNB Holdings listed by introduction on 25 Sep[^bw-2026-10-04-pnbh-debut] | 69.43 to 14 Aug (-2.0% year on year) | [^pse-weekly-report-2026-10-02:1][^pse-analyst-briefing-1h-2026:3] |

Capital-raised totals depend on the basis: annual-report and infographic figures count primary shares, while PSE's year-end press totals add secondary shares, warrants and private placements (2024: 82.37bn against 75.78bn; 2025: 144.14bn against 138.75bn), and the 2019 and 2020 "about 101" and "about 104" come from a press compilation rather than the annual-report table. Two large offers are scheduled: Vitro REIT (about PHP 24.19bn, 12 Oct 2026) and Mynt (Globe Fintech, about PHP 92.31bn; PSE's 18 Sep 2026 release gives a tentative 20 Oct listing, whereas the 4 Jul annual-meeting deck lists 19 Oct, so the later release is used).[^pse-asm-2026-president-report:8][^pse-press-mynt-ipo-approval] The 2020 listed-company and IPO counts were not found in any text-searchable PSE document (the FY2020–FY2023 annual reports are image-only SEC filings).

### PSEi history and drawdowns

| Episode | Peak (close) | Trough (close) | Move | Source |
|---|---|---|---|---|
| 2013 taper tantrum | 7,392.20 (15 May 2013; intraday 7,403.65) | 5,738.06 (28 Aug 2013) | -22.4% (computed) | [^pse-annual-report-2013:6][^pse-annual-report-2013:12] |
| 2014 | 7,360.75 peak | 7,230.57 year-end | peak just below the 2013 record close | [^pse-annual-report-2014:32] |
| All-time high to the 2020 low | 9,058.62 (29 Jan 2018) | 4,623.42 (19 Mar 2020) | -49.0% (computed); 2018 itself closed at 7,466.02, -12.8% for the year | [^pse-annual-report-2018:6][^pse-annual-report-2018:28] |
| COVID crash | 8,365.29 (15 Jul 2019, computed from weekly data) | 4,623.42 (19 Mar 2020) | -44.7% (computed); March 2020 range 4,623.42–6,884.77, month-end 5,321.23 (-21.6% m/m, -31.9% YTD) | [^pse-weekly-reports-dataset][^pse-monthly-report-2020-03:1] |
| 2022–2025 drift | 7,554.68 (7 Oct 2024) | 5,584.35 (14 Nov 2025) | -26.1% (computed); earlier lows 5,741.07 (30 Sep 2022) and 5,961.99 (27 Oct 2023) | [^pse-weekly-reports-dataset] |
| 2026 | 6,625.46 (26 Feb 2026) | 5,629.03 (2 Oct 2026) | -15.0%, -7.0% YTD (computed); the lowest close since 14 Nov 2025 | [^pse-weekly-report-2026-10-02:1] |

Year-high closes (computed) were 7,554.68 (7 Oct 2024), 6,625.17 (6 Jan 2025) and 6,625.46 (26 Feb 2026).[^pse-weekly-reports-dataset] In PSE's own November 2020 snapshot the PSEi (6,324.00 at 30 Oct 2020) was 19.1% below the 2019 close, 36.8% above the 2020 low close and 30.2% below the all-time high, with year-to-date ADVT of PHP 6.70bn (-8.2% on 2019), domestic capitalisation of PHP 11.58tn (-17.0% YTD) and net foreign selling of PHP 111.54bn.[^pse-asm-2020-presidents-report:3][^pse-asm-2020-presidents-report:4] The index fell 7.3% in 2025 after 2024's +1.2%, which PSE described as the first annual gain since 2019 (2020–2023 were all negative).[^pse-monthly-report-2025-12:2][^pse-press-2024-12-27] PSE's CEO attributed the 2025 weakness to a corruption scandal, a weak peso and a disappointing third-quarter GDP print.[^pse-press-2025-12-29]

**The 2026 path.**

| Date | PSEi | Value, flows and other marks | Source |
|---|---|---|---|
| End-Mar 2026 | 5,948.94 (-1.7% YTD) | ADVT 7.90bn; net foreign buying +12.14bn in 1Q | [^pse-infographic-1q26:1] |
| End-Jun 2026 | 6,037.17 | ADVT 7.72bn; net foreign selling 11.36bn in 1H; total MCAP 19.44tn | [^pse-infographic-2q26:1] |
| 14 Aug 2026 | 6,297.30 (+4.0% YTD) | Total MCAP 20.56tn; ADVT 7.57bn; net foreign selling 8.89bn against 40.18bn at the same date of 2025 | [^pse-analyst-briefing-1h-2026:3] |
| End-Aug 2026 | 5,956.33 (-1.6% YTD) | August ADVT 7.53bn; August net foreign outflow 16.56bn; YTD net foreign selling 20.86bn (45.43bn a year earlier); YTD foreign ratio 48.3% (46.9%); total MCAP 19.82tn, domestic 13.06tn; BSP rate hike, record-low peso and growth downgrades cited | [^pse-monthly-report-2026-08:1][^pse-monthly-report-2026-08:2] |
| 2 Oct 2026 | 5,629.03 (week -3.38%) | YTD high close 6,625.46; YTD net foreign selling 31.5bn; YTD ADV 7.71bn; foreign ratio 49.03% YTD and 55.49% in the week | [^pse-weekly-report-2026-10-02:1] |
| 5 Oct 2026 | 5,743.21 (+2.03%) | PSE market page; the end-of-day report is not archived | [^pse-composite-sector-frame] |

### Execution implications

- **Budget capacity from regular-market ADV, not the headline.** Regular ADV was PHP 5.95bn in 2025 and PHP 6.25bn in January–August 2026;[^pse-monthly-report-2025-12:1][^pse-monthly-report-2026-08:1] block volume is not available to a participation algorithm.
- **Size participation on a trailing 20–60-day median of regular-market value, not the annual mean.** Annual ADVT moved -18.9% (2022), -16.5% (2023) and +20.1% (2025) year on year, and monthly ADVT has ranged from PHP 3.96bn (Nov 2023) to PHP 12.66bn (Nov 2020), about 3×.[^pse-monthly-report-2022-12:1][^pse-monthly-report-2023-12:1][^pse-monthly-report-2025-12:1][^pse-monthly-report-2020-12:1]
- **A PHP 1bn parent order is about 13% of average daily total value (PHP 7.71bn) and 16% of regular ADV (PHP 6.25bn).** At 10% of regular ADV it needs about 1.6 days even if it could be spread over the entire market (computed arithmetic on the figures above).
- **One-off crosses inflate annual averages.** The 16 Dec 2021 block alone adds about PHP 0.33bn to 2021's 9.00bn ADVT (about 8.7bn without it) and the 14 Dec 2022 Eagle Cement cross adds about PHP 0.45bn to 2022's 7.30bn (about 6.85bn without it; computed).[^pse-eod-daily-quotation-2021-12-16:10][^pse-eod-daily-quotation-2022-12-14:11]

<div class="callout infer">
<span class="label">Inference</span>

Liquidity here is a *flow* problem more than a size problem: at about 5 bp of capitalisation a day, the whole market trades roughly US$120m. The post-2022 fall in ADVT to about PHP 6.1bn coincided with net foreign selling in every year since 2022 (cumulative 2022–2025 of PHP -196.1bn) and the unwinding of the 2021 retail boom (retail's share of value fell from 31.1% to 18.4% between 2021 and 2023; see Participation).
</div>

## Concentration of turnover

### Official data: February 2020

The only full Monthly Report in the archive (February 2020, 19 trading days) shows regular-market value of PHP 112.07bn, non-regular PHP 20.50bn and total PHP 132.56bn.[^pse-monthly-report-sample:11] The 30 PSEi constituents traded PHP 85.90bn of regular-market value, 76.7% of the regular total.[^pse-monthly-report-sample:34] Summing the report's ranked lines (own arithmetic), the top ten names by regular-market value (ALI, SMPH, SM, BDO, AC, BPI, URC, MWC, MBT, JFC) traded PHP 63.15bn (56.3%), the top 20 PHP 84.99bn (75.8%) and the top 25 PHP 90.89bn (81.1%).[^pse-monthly-report-sample:17] The 25 names with the highest monthly volume-turnover ratios (2.5%–49.6% of shares outstanding in one month, for example ISM 49.6%, FRUIT 37.2%, MAH 35.6%, TECH 20.2%) were all non-PSEi small and mid caps.[^pse-monthly-report-sample:16]

### Computed series

**Median share of regular-market value, computed from 176 sampled Daily Quotation Reports (two per month, Jun 2019 – Sep 2026).**[^pse-dqr-dataset]

| Year | Top-1 | Top-5 | Top-10 | Top-20 |
|---|---|---|---|---|
| 2019 | 12.1% | 39.6% | 60.5% | 77.5% |
| 2020 | 13.5% | 37.3% | 55.3% | 76.2% |
| 2021 | 10.6% | 34.6% | 51.2% | 71.2% |
| 2022 | 11.1% | 37.8% | 56.2% | 77.9% |
| 2023 | 11.6% | 41.7% | 59.3% | 79.4% |
| 2024 | 13.3% | 43.2% | 64.8% | 83.6% |
| 2025 | 16.1% | 47.6% | 64.8% | 81.3% |
| 2026 to Sep | 22.7% | 49.8% | 64.1% | 80.5% |
| All days | 13.3% | 41.0% | 59.7% | 79.0% |

**Breadth of the liquid universe, median names per day with regular-market value at or above a threshold (same sample).**[^pse-dqr-dataset]

| Year | ≥ PHP 100m | ≥ PHP 50m | ≥ PHP 10m |
|---|---|---|---|
| 2019 | 14 | 24 | 54 |
| 2020 | 16 | 25 | 54 |
| 2021 | 16 | 30 | 62 |
| 2022 | 16 | 25 | 48 |
| 2023 | 10 | 19 | 42 |
| 2024 | 14 | 21 | 44 |
| 2025 | 14 | 22 | 48 |
| 2026 to Sep | 14 | 23 | 52 |

About 91–128 names trade at least PHP 1m a day, and 224–254 issues trade at all on a day (of about 280 listed companies plus preferreds, warrants and ETFs). PHP 100m is about US$1.6m.

**Twenty-eight consecutive sessions, 26 Aug – 5 Oct 2026, main board only (computed).**[^pse-dqr-dataset] Daily means were: top-1 27.5%, top-5 52.9%, top-10 66.8%, top-20 81.2% of regular-market value. ICTSI (ICT) was in the top ten on all 28 days and was 21.0% of pooled regular value; SM was 15.3% (inflated by 17 Sep, when SM printed PHP 16.8bn, 73% of that day's regular value of about PHP 23.1bn[^pse-eod-daily-quotation-2026-09-17:4][^pse-eod-daily-quotation-2026-09-17:11-12]); then ALI 6.8%, BDO 5.6%, AC 5.4%, MBT 2.9%, BPI 2.3%, MER 2.1%, SMPH 2.0% and APX 2.0%. Average daily total value was PHP 8.77bn, of which regular PHP 6.87bn (78%), block sales PHP 1.90bn (21.7% pooled; 15.1% mean of daily shares), odd lots about PHP 1.1m (0.01%) and the new VWAP session PHP 1.05m (0.012%). Block sales were 82% of the 11 Sep total (PHP 26.9bn of 32.7bn) and 32% on 2 Oct (PHP 2.63bn of 8.18bn).[^pse-eod-daily-quotation-2026-09-11:11][^pse-eod-daily-quotation-2026-10-02:11]

**Block-sale share of total value, pooled, by year (computed, 176-day sample):** 15.2% (2019), 7.7% (2020), 13.0% (2021), 12.1% (2022), 19.8% (2023), 12.6% (2024), 19.5% (2025) and 13.4% (2026 sample); 13.9% over the whole sample. Odd lots are at most 0.015% of value.[^pse-dqr-dataset] The sample share differs from the official non-regular share above because it samples two days a month and blocks are lumpy. Block-sale rules are in [Chapter 5](#/ch/matching).

### Index weights and free float

- **PSEi weights (latest factsheet found, end-Sep 2025).** The PSEi (30 largest and most active companies, free-float market-cap weighted, calculated every minute, reviewed semi-annually) had a free-float market capitalisation of PHP 8,588.80bn (largest constituent 952.13bn, smallest 66.99bn, mean 286.29bn, median 166.17bn). The top five weights were ICT 14.0%, SM 12.2%, BDO 9.0%, BPI 8.6% and SMPH 6.9% (50.6% together); sector weights were Holding Firms 26.1%, Financials 24.6%, Services 20.8%, Industrial 15.4% and Property 13.1%.[^pse-psei-factsheet-2025-09:1][^pse-psei-factsheet-2025-09:2] Constituents have changed since (RCR replaced AGI in 1Q26 and MYNLD replaced CNVRG on 3 Aug 2026); index mechanics are in [Chapter 11](#/ch/market-data).[^pse-infographic-1q26:1][^pse-cn-2026-0035:1] The PSE MidCap Index covers the top 20 mid-sized companies and the Dividend Yield Index the top 20 high-yielders.[^pse-asm-2026-president-report:5] At 30 Sep 2026 the MSCI Philippines Index held only nine constituents with ICTSI at 44.73%.[^msci-philippines-index-factsheet-2026-09:1]
- **Ownership concentration (OECD, 2023 data).** Half of Main Board companies had free float below 28% and only a quarter above 40%; corporations hold 47% of listed equity; in 49% of listed companies the largest shareholder owns more than half (ASEAN 37%, Asia 22%).[^oecd-capital-market-review-philippines-2024:43][^oecd-capital-market-review-philippines-2024:121] The OECD reports listing minimums of 20–33% and a 10% maintenance floor. Average float of listed companies was 34.32% at end-2013 (32.28% in 2012).[^pse-annual-report-2013:28]

<div class="callout warn">
<span class="label">Currency: public-ownership rule changed on 11 Aug 2026</span>

The OECD's 20–33% listing and 10% maintenance figures describe the earlier regime. PSE's Amended Rule on Minimum Public Ownership, which the SEC approved, took effect immediately on 11 Aug 2026: IPO float of 33%, 25%, 20% or 15% by expected market capitalisation (each with a minimum offer size) and 33.33% for REITs;[^pse-amended-mpo-rule-2026-08:1][^pse-amended-mpo-rule-2026-08:2] maintenance at 20% (15% for issuers above PHP 50bn at listing) and 33.33% for REITs, and a possible lower requirement, never below 12%, for issuers expecting a market capitalisation of at least PHP 200bn at listing.[^pse-amended-mpo-rule-2026-08:3] Issuers listed before SEC MC 13 of 2017 keep 10%, and those listed between that circular and SEC MC 11 of 2026 keep 20%.[^pse-amended-mpo-rule-2026-08:2] PSE's 4 Jul 2026 annual-meeting report still described the tiered proposal as "awaiting SEC approval"; the 11 Aug 2026 memo supersedes it.[^pse-asm-2026-president-report:22] Detail is in [Chapter 2](#/ch/instruments) and [Chapter 13](#/ch/regulatory-constraints).
</div>

<div class="callout infer">
<span class="label">Inference</span>

With about 14 names above PHP 100m a day, a US$50–100m book cannot be built outside the roughly 30–40 index-weight names without dominating volume. ICT's share in August–October 2026 is a regime feature, not a constant (2019–2025 medians for the top name are 11–16%); treat it as a stress case for basket algorithms that assume diversified volume. Blocks are a structural second venue (13–20% of value), and the proposed Negotiated Trades rule would extend that to smaller pre-arranged deals.[^pse-asm-2026-president-report:23]
</div>

### Execution implications

- Use name-specific rolling ADV and rank-based participation. Beyond roughly the top 40–60 names daily value is below about PHP 10m (US$160k), so even a PHP 5m order is about half of ADV.
- Do not treat a basket as diversified. The top ten names are about 60% of market-wide value, so a market-neutral basket of 50 names will see highly skewed fill rates, with tail names filling late or not at all.
- Flag days on which one name exceeds half of regular value (corporate crosses, index days); volume schedules anchored on trailing volume under-participate in the other names that day.

## Participation

### Accounts, online share and activity

**Stock Market Investor Profile (PSE-published; "active" means the account traded at least once in the year, a definition printed only in the 2013 edition).** Implied active accounts are published share × accounts (computed; shares are rounded to 0.1 pp).

| Year | Accounts (growth) | Online accounts (share of accounts) | Active share, all | Active share, online | Retail / institutional / local / foreign active | Implied active accounts | Source |
|---|---|---|---|---|---|---|---|
| 2012 | 525,850 | 78,216 (14.9%) | 24.3% | n/a | n/a | 127,825 (stated) | [^pse-investor-profile-2013:2-6] |
| 2013 | 585,562 (+11.4%) | 129,255 (22.1%) | 23.9% | 43.4% | 23.7 / 30.9 / 23.7 / 39.7 | 140,145 (stated) | [^pse-investor-profile-2013:2-6] |
| 2014 | 640,665 (+9.4%) | 174,592 (27.3%) | 33.6% | 64.6% | 34.1 / 22.4 / 33.6 / 30.8 | about 215k | [^pse-investor-profile-2014:2-3] |
| 2015 | 712,549 (+11.2%) | 236,669 (33.2%) | 32.7% | 66.6% | 33.4 / 18.0 / 32.7 / 29.6 | about 233k | [^pse-investor-profile-2015:2-3] |
| 2016 | 773,187 (+8.5%) | 302,516 (39.1%) | 33.4% | 61.2% | 33.8 / 24.4 / 33.5 / 28.8 | about 258k | [^pse-investor-profile-2016:2-3] |
| 2017 | 868,810 (+12.4%) | 388,864 (44.8%) | 34.0% | 57.4% | 34.2 / 28.8 / 34.0 / 33.6 | about 295k | [^pse-investor-profile-2017:2-3] |
| 2018 | 1,089,413 (+25.4%) | 625,763 (57.4%) | 29.1% | 41.6% | 29.1 / 28.5 / 29.1 / 28.4 | about 317k | [^pse-investor-profile-2018:2-3] |
| 2019 | 1,228,038 (+12.7%) | 782,118 (63.7%) | 25.2% | 34.2% | 25.2 / 22.2 / 25.2 / 22.7 | about 309k | [^pse-investor-profile-2019:2-3] |
| 2020 | 1,396,753 (+13.7%) | 936,200 (67.0%) | 30.0% | 37.1% | 30.3 / 17.3 / 30.1 / 24.8 | about 419k | [^pse-investor-profile-2020:2-3] |
| 2021 | 1,620,017 (+16.0%) | 1,159,034 (71.5%) | 31.9% | 39.8% | 32.0 / 22.3 / 31.9 / 27.8 | about 517k | [^pse-investor-profile-2021:2-3] |
| 2022 | 1,712,734 (+5.7%) | 1,258,907 (73.5%) | 20.2% | 22.2% | 20.1 / 23.7 / 20.1 / 24.3 | about 346k | [^pse-smip-2022:2-3] |
| 2023 | 1,906,019 (+11.3%) | 1,525,768 (80.0%) | 17.6% | 19.3% | 17.6 / 20.5 / 17.5 / 22.7 | about 335k | [^pse-smip-2023:2-3] |
| 2024 | 2,860,234 (+50.1%) | 2,471,860 (86.4%) | 23.1% | 24.5% | 23.1 / 19.5 / 22.9 / 36.1 | about 661k | [^pse-smip-2024:2-3] |
| 2025 | 3,641,067 (+27.3%) | 3,226,616 (88.6%) | 11.8% | 12.0% | 11.7 / 14.6 / 11.7 / 20.4 | about 430k | [^pse-investor-profile-2025:2-3] |

Online shares for 2012–2020 are own arithmetic (online ÷ total); 2021–2025 are as printed. Coverage changes between editions: reporting trading participants fell from 135 (2013–2014) to 130 (2019), 123 (2023), 121 (2024) and 122 (2025), while the number supplying online data rose from 14 (2013) to 38–39 (2022–2024) and 35 (2025),[^pse-investor-profile-2013:2-6][^pse-smip-2022:2-3][^pse-smip-2024:2-3][^pse-investor-profile-2025:2-3] so early online counts may be incomplete and the 2013–2014 jump in the active share (23.9% to 33.6%) may reflect coverage or definition rather than behaviour. Foreign accounts were more active than local ones in 2013 and 2022–2025 but less active in every edition from 2014 to 2021.

- **The account base is online and e-wallet driven.** Accounts compounded about 13% a year in 2012–2020 and about 21% a year in 2020–2025 (6.9× over 2012–2025; computed). The online share rose from about 15% (2012) to 45% (2017), 67% (2020) and 89% (2025). Non-online accounts were flat at 0.45–0.48m through 2022 (479,946 in 2017 to 453,827 in 2022[^pse-asm-2023-presidents-report:10]) and are about 0.38–0.41m since 2023 (by subtraction), so the whole increase of the account base since 2012 is online.
- PSE says 89% of the increase of more than 950k accounts in 2024 was due to e-wallets.[^pse-asm-2025-presidents-report:13] GStocks PH (GCash, live Aug 2023) had more than 1.7m registered users, Maya Stocks more than 15k and the IPO app PSE EASy more than 84k as of March 2026.[^pse-analyst-briefing-3m-2026:21] 2024's +50.1% was the highest growth since the series began in 2008.[^pse-asm-2026-president-report:15][^pse-press-2025-06-09]
- 2025 composition: retail 3,611,157 (99.2%), institutional 29,910 (0.8%); local 3,608,358 (99.1%), foreign 32,709 (0.9%); online accounts 88.6% of the total, 99.9% retail and 99.3% local.[^pse-investor-profile-2025:2] Foreign accounts were 1.5% (8,917) of the total in 2013, and retail accounts 95.2% in 2015 and 97.5% in 2018.[^pse-investor-profile-2013:2][^pse-investor-profile-2015:2][^pse-investor-profile-2018:2]

<div class="callout infer">
<span class="label">Inference</span>

An 11.8% active rate on 3.64m accounts means the retail wave is mostly dormant accounts. Implied active accounts have stayed within roughly 0.3–0.7m since 2020 while registered accounts rose 2.6× (1.40m to 3.64m), and retail still contributes only about 18% of value. The editions differ in coverage and PSE does not document definitions, so year-to-year changes are not a clean time series. Separately, with no on-exchange shorting and no listed derivatives, price formation is driven by long-only flows and index events: there is no short-covering or hedging flow to dampen moves, and foreign funds hedge offshore or over the counter, which PSE data do not show.

</div>

### Who trades the value

**Foreign share, net foreign flows and retail share, by year.** Trade size columns are computed from the Weekly Reports (value ÷ number of trades; trades per day; 2019 from 3 May).

| Year | Foreign / local share of value | Net foreign (PHP bn) | Retail / institutional share of value | Avg value per trade (PHP k) | Trades per day (k) |
|---|---|---|---|---|---|
| 2013 | 51% / 49% | +15.59 | n/a | n/a | n/a |
| 2014 | 49% / 51% | +55.45 | n/a | n/a | n/a |
| 2015 | 47.9% / 52.1% | -59.76 | n/a | n/a | n/a |
| 2016 | 51.3% / 48.7% | +2.80 | n/a | n/a | n/a |
| 2017 | 50.3% / 49.7% | +56.20 | n/a | n/a | n/a |
| 2018 | 51.3% / 48.7% | -61.01 | n/a | n/a | n/a |
| 2019 | 55.4% / 44.6% | -14.26 | 18.2% / 81.8% | 87 | 81 |
| 2020 | 45.4% / 54.6% | -128.57 | 26.9% / 73.1% | 66 | 112 |
| 2021 | 36.0% / 64.0% | -2.75 | 31.1% / 68.9% | 78 | 116 |
| 2022 | 40.7% / 59.3% | -68.05 | 20.1% / 79.9% | 96 | 76 |
| 2023 | 43.9% / 56.1% | -53.65 | 18.4% / 81.6% | 108 | 57 |
| 2024 | 46.2% / 53.8% | -23.19 | 18.9% / 81.1% | 105 | 58 |
| 2025 | 46.3% / 53.7% | -51.20 | 18.2% / 81.8% | 105 | 70 |
| 2026 to 2 Oct | 49.03% / 50.97% | -31.5 | 19.1% / 80.9% (5M26) | 89 | 86 |

Sources: foreign ratio and net foreign flows for 2013–2017,[^pse-annual-report-2017:17] 2015 (47.9%),[^pse-annual-report-2015:32] 2018,[^pse-annual-report-2018:32] 2019,[^pse-annual-report-2019:32] 2020,[^pse-monthly-report-2020-12:2] 2021,[^pse-monthly-report-2021-12:2] 2022,[^pse-monthly-report-2022-12:2] 2023,[^pse-monthly-report-2023-12:2] 2024,[^pse-monthly-report-2024-12:2] 2025[^pse-monthly-report-2025-12:2] and 2026;[^pse-weekly-report-2026-10-02:1] retail share for 2019–2020,[^pse-asm-2021-presidents-report:4] 2021,[^pse-asm-2022-presidents-report:4] 2022,[^pse-asm-2023-presidents-report:6] 2023,[^pse-asm-2024-presidents-report:6] 2024,[^pse-asm-2025-presidents-report:7] and 2025 and 5M26;[^pse-asm-2026-president-report:7] trade size and trades per day computed from the Weekly Reports.[^pse-weekly-reports-dataset] The slides do not define the basis of the retail share (presumably value traded) and no series before 2019 was found. The 2025 net foreign figure is 51.20bn in the Monthly Report and infographic; the 29 Dec 2025 press release's 51.78bn was issued before the last two sessions were final.[^pse-press-2025-12-29]

- **Retail share.** Jan–May 2021 38.9%; 7M21 36.8%; 7M22 21.2%; 7M23 20.4%; 1H24 20.0%; 1H25 17.9%; 5M25 17.2%.[^pse-asm-2021-presidents-report:4][^pse-asm-2022-presidents-report:4][^pse-asm-2023-presidents-report:6][^pse-asm-2024-presidents-report:6][^pse-asm-2025-presidents-report:7][^pse-asm-2026-president-report:7] The share roughly doubled from 18% (2019) to 39% (Jan–May 2021) and then fell back to 17–20% from 2022, even though accounts more than doubled. In June 2025 PSE's CEO said retail contributes only "16 percent" of value turnover (a figure whose basis is not given and which is below the 18.9% in the annual-meeting chart).[^pse-press-2025-06-09]
- **Foreign share within years.** 1H21 32.6%; 7M21 32.8%; 7M22 42.4%; 7M23 43.6%; 1H24 46.1%; 1H25 48.3%; 1H26 49.5%; YTD to end-Aug 2026 48.3%;[^pse-asm-2021-presidents-report:5][^pse-asm-2022-presidents-report:5][^pse-asm-2023-presidents-report:7][^pse-asm-2024-presidents-report:6][^pse-asm-2025-presidents-report:7][^pse-asm-2026-president-report:7][^pse-monthly-report-2026-08:2] year-to-date net foreign flows were -87.02bn (7M21), -45.95bn (7M22) and -6.55bn (7M23), and half-year flows -77.76bn (1H21), -31.12bn (1H24; full-year 2024 -23.19bn, so net buying of about +7.9bn in 2H24) and -41.07bn (1H25).[^pse-asm-2021-presidents-report:5][^pse-asm-2022-presidents-report:5][^pse-asm-2023-presidents-report:7][^pse-asm-2025-presidents-report:7] Monthly examples: December 2021 +84.88bn (one block and rotation), December 2025 -10.67bn after +6.38bn in November 2025.[^pse-monthly-report-2021-12:2][^pse-monthly-report-2025-12:2]
- **Data quirk (computed).** Summing PSE's own daily "total foreign" figures gives a foreign ratio 2–3 pp above PSE's official figure (2025: 49.1% against 46.3%; 2024: 48.8% against 46.2%; 2023: 45.9% against 43.9%; 2021: 37.1% against 36.0%; 2026 YTD: 52.2% against 49.03%), so the official figure is not the sum of the daily numbers; PSE does not document the difference.[^pse-weekly-reports-dataset][^pse-weekly-report-2026-10-02:1]
- **Foreign activity is event-driven (inference).** Foreign share is highest on index-rebalance days (70–89%) and lowest on domestic block days (3–20%); the 31 May 2023 MSCI session had 81.3% foreign activity.[^pse-weekly-report-2023-06-02:1]

<div class="callout infer">
<span class="label">Inference</span>

The foreign ratio rose from about 36% (2021) to 46–49% (2024–2026) mainly because *local* turnover collapsed. Summing PSE's daily series (computed), foreign buy-plus-sell value was PHP 1.66tn (2021), 1.51tn (2022), 1.36tn (2023), 1.46tn (2024) and 1.75tn (2025), while local sides (twice value traded minus foreign) fell from 2.81tn (2021) to 1.53tn (2024), down 45%, before recovering to 1.81tn in 2025.[^pse-weekly-reports-dataset] Retail value (published share × value traded; computed, assuming the share refers to total value) was about PHP 0.32tn (2019), 0.48tn (2020), 0.69tn (2021), 0.36tn (2022), 0.27tn (2023), 0.28tn (2024) and 0.32tn (2025), while institutional value stayed within 1.2–1.5tn. About 56% of the 0.76tn fall in value traded between 2021 and 2023 was therefore retail.
</div>

### Trade size, IPO allocation and brokers

- **Trade size.** In 2024 the average online trade was PHP 50,746.82 (+7.9%) against PHP 99,823.86 for non-online trades (+4.5%);[^pse-press-2025-06-09] in 2022 the average online ticket was PHP 46,236.40, up 33.2% from PHP 34,701.80 in 2021.[^pse-asm-2023-presidents-report:10] In February 2020 the average regular-market trade was PHP 70.3k against PHP 2.98m per block or odd-lot print.[^pse-monthly-report-sample:11]
- **IPO allocation.** Underwriters must allocate at least 20% of an IPO to PSE trading participants and 10% to local retail investors. PSE reported in 2021 that retail investors subscribed to only 1.4% of shares against the 10% assigned; the OECD adds that PSE now says the retail allocation has generally been well subscribed through the PSE EASy app.[^oecd-capital-market-review-philippines-2024:33] After EASy launched in June 2019, two of the four 2019 IPOs that used it exceeded 9.0% take-up in the local-small-investor tranche, against under 2.0% in earlier IPOs.[^pse-annual-report-2019:5]
- **Market makers are nominal.** The OECD reports 121 brokers formally acting as market makers who match orders but "do not trade on their own account or build inventories", with only about half active, and the OECD found no market-maker incentives.[^oecd-capital-market-review-philippines-2024:47] PSE's 2026 proposed amendments to its Market Making Rules (a framework for GPDRs, possibly expanded later to individual stocks) are not in force.[^pse-asm-2026-president-report:23] Inference: displayed depth is therefore mostly broker-agency orders ([Chapter 8](#/ch/market-making)).
- **Short selling is unused.** The Daily Short Selling Report shows zero short-sale volume and value, and "NULL" short-interest ratios, on every one of the 710 daily reports from 6 Nov 2023 to 5 Oct 2026 (computed: own parse of all 710 PDFs; first and last archived). Eligible securities numbered 53 on the first report (incl. the FMETF ETF) and 52 on 5 Oct 2026.[^pse-short-sell-report-2023-11-06:2][^pse-short-sell-report-2026-10-05:2][^pse-market-reports-index] The OECD says short selling and securities lending "has yet to come into widespread use", and there is no public derivatives market.[^oecd-capital-market-review-philippines-2024:13][^oecd-capital-market-review-philippines-2024:47] See [Chapter 9](#/ch/short-selling).
- **Broker concentration, February 2020 (the only full report archived; ranked by buying plus selling value).** Against two-sided value of 2 × PHP 132.56bn the top five brokers handled 40.3%, the top ten 62.6% and the top 25 89.8% (computed).[^pse-monthly-report-sample:11][^pse-monthly-report-sample:21]

| Rank | Broker | Value (PHP bn) | Trades |
|---|---|---|---|
| 1 | Salisbury BKT Securities | 25.27 | 99,892 |
| 2 | UBS Securities Philippines | 25.16 | 131,926 |
| 3 | CLSA Philippines | 20.70 | 221,125 |
| 4 | J.P. Morgan Securities Philippines | 20.17 | 76,508 |
| 5 | Credit Suisse Securities (Philippines) | 15.56 | 466,514 |
| 6 | Macquarie Capital Securities | 13.73 | 69,047 |
| 7 | COL Financial Group | 13.46 | 518,390 |
| 8 | BDO Securities | 11.35 | 20,636 |
| 9 | Maybank ATR Kim Eng | 11.18 | 146,830 |
| 10 | Wealth Securities | 9.27 | 27,374 |

COL Financial, the online retail broker, had the most trades (518,390; 16.2% of broker-side trades) but only 5.1% of value (about PHP 26k per trade against PHP 191–253k at UBS and Salisbury): value is institution- and foreign-broker-led while trade counts are retail-led.[^pse-monthly-report-sample:21] The broker mix is dated: the ranking is from February 2020, full rankings sit in the paid Monthly Report, and PSE's website shows only a top-10 snapshot ([Chapter 1](#/ch/market-architecture) reproduces the 5 Oct 2026 frame). Concentration persisted: in its 2022 consultation PSE said around 10 of 125 active trading participants account for more than 50% of total trades.[^pse-cn-2022-0020-market-halt-consultation:4]

### Execution implications

- Foreign-heavy flow (46–49% of sides) makes daily value sensitive to EM fund flows and index events; when foreign activity fades value falls toward PHP 4–5bn a day (ADVT PHP 3.96bn in Nov 2023 with near-zero net foreign flow).[^pse-monthly-report-2023-12:1]
- Retail is a small, fragmented liquidity source (average online ticket about PHP 50k); do not expect it to absorb institutional size at the open or close, and do not assume a constant retail/institutional mix (39% in Jan–May 2021, 17–20% since 2022).
- Plan on no usable on-exchange short capacity (zero reported short sales in 710 sessions) and no listed hedging instrument: market-neutral or pairs strategies cannot be executed as a single on-exchange package, and hedges must go through offshore or OTC instruments.
- Plan for fewer standing quotes than the number of participants suggests (inference: displayed depth is mostly broker-agency orders).

## Liquidity and cost evidence

<div class="callout">
<span class="label">What is and is not public</span>

No public PSE document or academic paper gives effective spreads, depth at the best or top-five levels, a quoted-spread time series or price-impact curves. The best primary proxy is the best bid and ask printed in the Daily Quotation Report after the close, and PSE's file specification does not define them.[^pse-daily-quotation-report-file-spec-2016:1] They appear to be the residual book after the closing run-off, so they probably overstate time-weighted intraday spreads (2 Oct 2026: BDO 110.4/110.6 is 2 ticks or 18 bp; BPI 93.9/94.0 is 1 tick or 10.6 bp; ICT 860/862 is 4 ticks or 23 bp).[^pse-eod-daily-quotation-2026-10-02:1][^pse-eod-daily-quotation-2026-10-02:5] Everything in the spread, depth and impact tables below is such a proxy.
</div>

### Tick size and the relative tick

The 15-band tick and board-lot table in force is set out in [Chapter 4](#/ch/order-types); PSE's December 2025 consultation shows the same table as "existing".[^pse-cn-2025-0046-board-lot-trading-at-last:4] Because the tick is fixed in pesos per price band, the relative tick (tick ÷ price) is a sawtooth: it jumps at each band edge and falls as price rises within the band.

| Price band (PHP) | Tick (PHP) | Relative tick at band floor | Relative tick at band ceiling |
|---|---|---|---|
| 0.01–0.049 | 0.001 | 1,000 bp | 204 bp |
| 0.05–0.249 | 0.001 | 200 bp | 40 bp |
| 0.25–0.495 | 0.005 | 200 bp | 101 bp |
| 0.50–4.99 | 0.01 | 200 bp | 20 bp |
| 5–9.99 | 0.01 | 20 bp | 10 bp |
| 10–19.98 | 0.02 | 20 bp | 10 bp |
| 20–49.95 | 0.05 | 25 bp | 10 bp |
| 50–99.95 | 0.05 | 10 bp | 5 bp |
| 100–199.9 | 0.10 | 10 bp | 5 bp |
| 200–499.8 | 0.20 | 10 bp | 4 bp |
| 500–999.5 | 0.50 | 10 bp | 5 bp |
| 1,000–1,999 | 1 | 10 bp | 5 bp |
| 2,000–4,998 | 2 | 10 bp | 4 bp |
| 5,000 and above | 5 | 10 bp | n/a |

Tick values from PSE's consultation table;[^pse-cn-2025-0046-board-lot-trading-at-last:4] the relative-tick columns are computed arithmetic. Most index stocks (PHP 50–1,000) therefore carry a 4–10 bp tick, PHP 5–50 stocks 10–25 bp, and sub-PHP 1 stocks up to 200 bp.

**Distribution of the relative tick (computed from 176 sampled Daily Quotation Reports; 42,347 main-board stock-days with a trade).**[^pse-dqr-dataset]

| Relative tick | Share of stock-days | Share of value |
|---|---|---|
| under 5 bp | 0.6% | 1.4% |
| 5–10 bp | 18.5% | 47.6% |
| 10–25 bp | 33.0% | 41.0% |
| 25–50 bp | 13.0% | 4.9% |
| 50–100 bp | 14.8% | 3.1% |
| 100 bp and above | 20.0% | 2.0% |

The median relative tick is 22.7 bp and the value-weighted figure 16.9 bp. In the 28-session 2026 panel 56.3% of value traded in names with a 5–10 bp tick and 31.6% in 10–25 bp names (value-weighted 13.1 bp). Almost half of traded issues, but only about 10% of value, have ticks of 25 bp or more and are tick-constrained by construction (sub-PHP 10 stocks with a PHP 0.01 tick).

### End-of-day quoted spreads and price impact

**End-of-day quoted spread by turnover rank (computed from 176 sampled Daily Quotation Reports, Jun 2019 – Sep 2026; main-board stocks that traded with a two-sided close quote).**[^pse-dqr-dataset]

| Rank by day's value | Observations | Median spread (bp) | IQR (bp) | Median spread (ticks) | At exactly 1 tick | At 2 ticks or less | Median tick (bp of price) | Median day value (PHP m) |
|---|---|---|---|---|---|---|---|---|
| 1–10 | 1,758 | 30.9 | 14.8–64.6 | 3 | 33% | 47% | 8.9 | 252 |
| 11–30 | 3,517 | 35.2 | 16.6–75.4 | 2 | 41% | 54% | 12.5 | 66 |
| 31–60 | 5,275 | 50.4 | 23.4–99.4 | 2 | 44% | 60% | 16.7 | 14 |
| 61–100 | 7,036 | 86.6 | 39.5–160.4 | 2 | 42% | 57% | 25.0 | 3 |
| over 100 | 24,717 | 227.3 | 111.9–449.4 | 5 | 20% | 33% | 41.2 | 0.4 |

For the ten most active names the median end-of-day spread was 32.2 bp in 2019–2022, 32.2 bp in 2023–2024 and 25.8 bp from January 2025 to September 2026 (median two ticks), a modest improvement.[^pse-dqr-dataset]

**Amihud-type illiquidity (computed, 28 consecutive sessions 26 Aug – 5 Oct 2026):** the median across stocks of the median daily absolute close-to-close return, in % per PHP 100m of that day's regular-market value, with stocks ranked by average daily value.[^pse-dqr-dataset]

| Rank | Illiquidity (% per PHP 100m) | Median average daily value (PHP m) |
|---|---|---|
| Top 10 | 0.56 | 287 |
| 11–30 | 2.5 | 70 |
| 31–60 | 5.8 | 21 |
| 61–100 | 34 | 2.8 |
| Over 100 | 464 | 0.1 |

Read it as an association, not a clean impact estimate: absolute moves include news-driven moves. A PHP 100m day is associated with about 0.6% absolute movement in a top-ten name and about 34% in a rank 61–100 name.

### Costs

Per the OECD (2024, before the 2025 tax cut), the PSE fee was 0.005% plus 12% VAT, clearing 0.01%, the SEC fee 0.005%, and broker commission 0.05–1.5% plus VAT, with a seller-only stock transaction tax of 0.6%: a total of 0.30% for the buyer and 0.90% for the seller, 1.2% round trip against a 0.66% peer average and about three times Indonesia, Singapore and Thailand on the sell side.[^oecd-capital-market-review-philippines-2024:45][^oecd-capital-market-review-philippines-2024:46] The stock transaction tax fell from 0.6% to 0.1% on trades from 1 Jul 2025;[^pse-cn-2025-0028-cmepa-effectivity:1][^bir-rr-20-2025-stt:4] on the same stack the seller's cost falls from about 0.90% to about 0.40% and the round trip from about 1.2% to about 0.70% (computed, at a 0.25% commission), roughly the OECD's peer average. The OECD's sentence that "the SEC removed the 1.5% minimum broker commission fee in April 2024" mislabels the change: what was removed (effective 18 Apr 2024) was the sliding *minimum* commission of 0.25% to 0.05%, and the 1.5% *maximum* remains.[^pse-cn-2024-0029-min-commission-removal:1] The OECD's 0.30% and 0.90% reproduce at a 0.25% commission ([Chapter 12](#/ch/costs)). The fee stack, the SEC "SRC fee" caveat and worked round trips are in [Chapter 12](#/ch/costs); spread and impact are not in these cost figures.

The OECD concluded the Philippines has "markedly lower liquidity than peer countries", attributing it to low free float, high trading costs (especially the sell-side tax), limited research and the absence of market makers.[^oecd-capital-market-review-philippines-2024:13][^oecd-capital-market-review-philippines-2024:48]

<div class="callout warn">
<span class="label">Scheduled change: 23 Nov 2026, subject to SEC approval</span>

PSE's 15 Dec 2025 consultation (CN 2025-0046) proposes One Lot One Share and a new tick table with the Nasdaq Eqlipse engine: for PHP 10–99.95 a single 0.05 tick, so stocks priced PHP 10–19.98 move from a 0.02 tick to 0.05.[^pse-cn-2025-0046-board-lot-trading-at-last:3][^pse-cn-2025-0046-board-lot-trading-at-last:4] PSE's 4 Jul 2026 annual-meeting report says it is "awaiting SEC approval" of the board-lot amendments, targeted for Q4 2026 alongside the new engine, and the 17 Aug 2026 status board still lists them as pending; no approval or effectivity circular was found by 6 Oct 2026.[^pse-asm-2026-president-report:22][^pse-analyst-briefing-1h-2026:9] PSE's earlier October 2023 proposal to cut lot sizes so that PHP 100 buys a lot (CN 2023-0051, ticks unchanged) was reported "awaiting SEC approval" in July 2024; no approval was ever announced and the December 2025 paper shows the old table as "existing" (inference: the 2023 proposal lapsed).[^pse-cn-2023-0051:3][^pse-asm-2024-presidents-report:18] If the new table is adopted, computed on the 28-session 2026 panel, 16.0% of traded stock-days (17.8% of regular-market value; ALI, SMPH, APX, PX, EMI, MYNLD, WEB, SCC, LTG and MREIT, all priced PHP 10–20) would face a 2.5× larger tick; the value-weighted relative tick would rise from 13.1 bp to 16.9 bp and the median from 24.1 bp to 32.5 bp (ALI at PHP 15.14: 13 bp to 33 bp).[^pse-dqr-dataset] Re-measure spreads and queue behaviour immediately after any change. Do not hard-code either regime ([Chapter 17](#/ch/reform-timeline)).
</div>

### Execution implications

- **Quoted half-spread budget (judgement from the proxies above):** about 5–15 bp for the top ten names and 15–50 bp for ranks 11–60; 25–60 bp one way for ranks 61–100 and more than 100 bp for the tail, on top of fees. The roughly 5-tick median beyond rank 100 implies a 2–4% round trip.
- **Tick-constrained queues.** 33–44% of liquid-name spreads equal one tick, so price-time priority matters more than price improvement; joining the best bid or ask early matters, and pennying inside the spread is possible only where the spread is at least two ticks (about 55–65% of liquid names at the close).
- **Impact scale (linear scaling of the Amihud-type figures; judgement, not from a cited study):** a PHP 5m child order is associated with about 0.03% of absolute daily move in the top ten names, about 0.3% in ranks 31–60 and above 1.5% in ranks 61–100, against a typical PSEi daily range of about 1.2%. Cap participation conservatively (for example at most 10% of regular-market ADV and at most 20% of any single auction or five-minute window) and use the block facility (regular block sale of at least PHP 20m, within ±5% of the reference price;[^pse-cn-2026-0031-negotiated-trades:3] see [Chapter 5](#/ch/matching)) when a counterparty exists.
- **Explicit costs dominate spread for the top 30 names after 1 Jul 2025:** a 0.1% tax plus commission and about 0.02% of exchange and clearing fees against a 5–30 bp spread; before July 2025 the 0.6% sell-side tax dwarfed everything. Backtests must switch the tax by trade date.

## Intraday and calendar behaviour

### What is public and the closing regimes

PSE publishes no intraday volume profile and no statistic on the share of volume in the pre-open, continuous session, pre-close call, run-off or VWAP session. The Weekly Report gives only daily PSEi open, high, low and close, total value, number of trades and foreign activity (week of 28 Sep – 2 Oct 2026: daily value PHP 5.19, 5.39, 9.10, 7.54 and 8.18bn on 85k, 83k, 101k, 90k and 76k trades).[^pse-weekly-report-2026-10-02:1] PSE's 2013 consultation on the extended pre-close gives the rationale (peer pre-close lengths; ETF and index funds benchmarked to the close, so baskets need time) but does not quantify closing volume.[^pse-memo-extended-pre-close-consultation-2013:1][^pse-memo-extended-pre-close-consultation-2013:2]

The closing price is set by a pre-close call (maximum matched volume; reference price the last traded price) followed by a run-off at that price.[^pse-implementing-guidelines-trading-rules:4][^pse-implementing-guidelines-trading-rules:12][^pse-implementing-guidelines-trading-rules:16] Mechanics are in [Chapter 6](#/ch/auctions). Close-of-day statistics below were measured across four timetables:

| Period | Pre-close | Run-off | Close |
|---|---|---|---|
| 4 Nov 2013 – 13 Mar 2020 | 15:15–15:20 | 15:20–15:30 | 15:30 |
| 16 Mar 2020 – 3 Dec 2021 (no trading 17–18 Mar) | 12:45 | 12:50 | 13:00 |
| 6 Dec 2021 – 29 Feb 2024 (13:00 close from 14 Jan to 28 Feb 2022, end date implied) | 14:45 (no-cancel 14:48 from 1 Mar 2022) | 14:50 | 15:00 |
| from 1 Mar 2024 | 14:45 (no-cancel 14:48) | 14:50, then Closing VWAP 15:00–15:15 | 15:15 |

Sources: [^pse-memo-pre-close-schedule-2013:1][^pse-cn-2020-0025-resumption-of-trading:1][^pse-cn-2021-0059:1][^pse-cn-2022-0004:1][^pse-cn-2022-0009-trading-schedule-mar-2022:1][^pse-approved-rules-vwap-trading-2024:3]. PSE's infographics still print "9:30AM to 3:00PM" and cite CN 2022-0009, omitting the VWAP session,[^pse-infographic-fy25:1] and the "Investing at PSE" web page still carries a 15:30-close table and FAQ text that are stale.[^pse-investing-page]

**Closing VWAP session usage (computed, 176 sampled days and the 28-session panel).** Six of the 28 sessions from 26 Aug to 5 Oct 2026 had any VWAP trade (examples: 2 Oct, one print of 3,750 GLO shares for PHP 7.29m, 0.09% of the day's PHP 8.18bn; 17 Sep, 75,000 shares for PHP 4.35m; 28 Aug, 168,000 shares for PHP 2.29m).[^pse-eod-daily-quotation-2026-10-02:11][^pse-eod-daily-quotation-2026-09-17:11][^pse-dqr-2026-08-28:11] VWAP value was 0.054% (2024), 0.092% (2025) and 0.113% (2026) of total value, and odd lots at most 0.015%.[^pse-dqr-dataset] A VWAP trade needs value of at least PHP 500,000 and a single trading participant on both sides,[^pse-approved-rules-vwap-trading-2024:7] so the session should not be counted on as a liquidity pool.

### The PSEi closes at an extreme of the day's range

**PSEi close and open at the day's high or low (computed from daily PSEi OHLC in the Weekly Reports; 1,813 sessions, 29 Apr 2019 – 2 Oct 2026).**[^pse-weekly-reports-dataset]

| Year | Close = high | Close = low |
|---|---|---|
| 2019 | 30.3% | 15.2% |
| 2020 | 28.5% | 13.8% |
| 2021 | 25.0% | 13.7% |
| 2022 | 26.9% | 15.5% |
| 2023 | 21.1% | 19.8% |
| 2024 | 15.1% | 20.4% |
| 2025 | 12.8% | 16.9% |
| 2026 to 2 Oct | 11.8% | 19.4% |
| All sessions | 21.3% | 16.8% |

The close falls in the top decile of the day's range on 28.4% of sessions and in the bottom decile on 23.1%; the open is the day's high on 17.0% and low on 10.1%. A Gaussian random walk with 200–5,000 steps gives close = high on 0.6–4.0% of sessions and 13.3–14.4% in each decile. Mean |close − open| ÷ range is 0.54–0.61 by year (benchmark 0.47) and 22–32% of sessions are "trend days" with |close − open| of at least 80% of the range (benchmark 13%). The bias flipped from "close at high" in 2019–2022 (rising or range-bound market) to "close at low" in 2023–2026 (drifting market), so the extremes track prevailing drift rather than a fixed closing-auction premium. The yearly figures also straddle the timetables above: 2019 and early 2020 were measured on a 15:30 close, March 2020 to November 2021 on a 13:00 close and later years on a 15:00 close, so year-to-year changes mix drift with schedule changes.

**Individual stocks, ranks 1–100 by value (computed from 176 sampled Daily Quotation Reports; 17,600 stock-days).** The benchmark is a driftless Brownian motion whose expected high-low range equals each stock-day's observed range in ticks.[^pse-dqr-dataset]

| Rank tier | Close = high / low | Random-walk benchmark | Open = high / low |
|---|---|---|---|
| 1–10 | 13.2% / 14.7% | about 2.7% each | 14.8% / 11.0% |
| 11–30 | 13.9% / 13.6% | 4.4% | 18.1% / 14.3% |
| 31–60 | 15.0% / 15.0% | 7.7% | 24.0% / 16.6% |
| 61–100 | 20.6% / 19.4% | 12.7% | 31.8% / 20.8% |

The excess ratio falls from about 5× in the top ten to 1.6× in ranks 61–100.

<div class="callout infer">
<span class="label">Inference</span>

The opening call and the closing call and run-off print at a day's high or low about five times more often than chance in the most liquid names. That is consistent with auction prices carrying a discrete, imbalance-driven jump relative to the continuous path, and with sell-side descriptions of index flows concentrating in the closing auction (below). It is not proof: drift, tick discretisation and thin continuous trading also push the close to extremes. There is no public data on the closing auction's volume share.
</div>

### Index and benchmark flows at the close

- **Press and sell-side (secondary only; no PSE document).** After the May 2026 MSCI review (effective at the close of 29 May 2026; JFC moved to small cap) a Globalinks sales trader told BusinessWorld forced selling "is typically concentrated in the closing auction of the rebalancing date".[^bw-753259] On 30 May 2023 a China Bank Capital managing director said foreign institutions were rebalancing ahead of MSCI effectivity and expected "a potentially volatile session ... on the back of last-minute window dressing".[^bw-525845]
- **Primary data on an index day.** 31 May 2023 (MSCI semi-annual review effective): total value PHP 24.5bn (5.3× the trailing 20-day median), foreign activity 81.3%, net foreign selling PHP 4.15bn and 100,324 trades.[^pse-weekly-report-2023-06-02:1]
- **Late-session headlines (secondary).** BusinessWorld reported "PSEi falls to near 7-month low after late selloff" on 16 Jan 2025 despite trading higher for most of the session, "last-minute buying" on 10 Dec 2024, "loses steam before close on profit taking" on 10 Sep 2024 and "last-minute selling trimmed gains" on 12 Oct 2023.[^bw-647194][^bw-640643][^bw-620502][^bw-551311]

### Month-end, day-of-week and seasonal patterns

**Turn of the month, PSEi (computed from daily closes in the Weekly Reports; 29 Apr 2019 – 2 Oct 2026; 1,808 returns, 89 months).**[^pse-weekly-reports-dataset]

| Session | Mean return | Note |
|---|---|---|
| Last trading day of the month | -0.52% (t = -3.3) | median -0.64%; only 34% of 89 months positive |
| Last day of a quarter | -0.51% (t = -2.0) | n = 30 |
| 1st trading day | +0.34% (t = 2.5) | |
| 2nd trading day | +0.31% (t = 2.4) | |
| 3rd trading day | +0.23% (t = 1.9) | first three sessions average +0.29% (t = 4.0; 63% positive; n = 267) |
| All other days | -0.045% (t = -1.4) | |

The last-day effect is not an MSCI artefact: in months whose last session is an MSCI review day (Feb, May, Aug, Nov; n = 30) the mean is -0.18% (t = -0.7), whereas in the other 59 months it is -0.70% (t = -3.6; median -0.68%; 68% negative). It appears in both halves of the sample (2019–2022 -0.47%, n = 44; 2023–2026 -0.58%, n = 45), is -0.66% (t = -4.6) excluding February–June 2020, and a permutation test against randomly drawn days gives p = 0.0004. Caveats: 89 months over which the index fell about 30%, fat-tailed daily returns and no cross-check against other markets, so treat it as indicative. Local market reports attribute month-end rallies to "window dressing" (for example 30 Jun 2017, 27 Jun 2019, 28 Sep 2023) and also describe a fall on "month-end window dressing" on 31 May 2023, an MSCI day.[^bw-14232][^bw-238977][^bw-548526][^bw-526114] In these data the narrative is a headline cliché rather than an exploitable signal.

**Month-end closing dislocation, top-100 stocks (computed from 164 Daily Quotation Reports for the last three and first two sessions of each month, Jan 2024 – Sep 2026).**[^pse-dqr-dataset][^pse-weekly-reports-dataset]

| Session | Close = high | Close = low | Both |
|---|---|---|---|
| Last session of the month (33 months) | 21.6% | 22.2% | 43.8% |
| Baseline mid-month days | 16.7% | 17.3% | 34.0% |
| T-2, T-1, T+1, T+2 | | | 32–36% |
| Last day of a quarter | 24.1% | 19.2% | 43.3% |

A tick-discretised random walk gives about 9% on each side. The mean position of the close within the day's range is 0.498 on the last day (baseline 0.493), so there is no upward bias, and the equal-weighted return of stocks trading at least PHP 10m was +0.10% on the last day (+0.11% on T-1; n = 1,601) while the PSEi fell on average about 0.5% on those days. The month-end close is noisier, consistent with index and rebalancing flows at the close, but there is no evidence of a broad "marking the close" bias; the month-end weakness is concentrated in the large, index-weighted names.

**Day of week, PSEi (computed, same data; figures in brackets exclude 15 Feb – 30 Jun 2020).**[^pse-weekly-reports-dataset]

| Day | Mean return | Average value traded (PHP bn) |
|---|---|---|
| Monday | -0.116% (-0.055%) | 6.4 |
| Tuesday | +0.138% (+0.097%; t = 2.4) | 7.3 |
| Wednesday | +0.048% (+0.032%) | 7.3 |
| Thursday | -0.050% (-0.005%) | 7.1 |
| Friday | -0.118% (-0.124%; t = -2.05) | 8.1 |

Neither extreme survives a Bonferroni correction for five weekdays; Friday's value includes many MSCI and month-end days; Friday open-to-close was -0.15% against an overnight +0.03%. Rufino and Delfino (2016) likewise found no day-of-week effect in the PSEi or any sector index over 2006–2013 (see Literature).

**Month of year, average daily value (computed, PHP bn):** Jan 7.1, Feb 8.2, Mar 8.0, Apr 6.1, May 7.7, Jun 7.1, Jul 6.0, Aug 7.3, Sep 7.3, Oct 6.8, Nov 7.7, Dec 8.5; April and July are the thinnest months, and March includes the 2020 crash.[^pse-weekly-reports-dataset]

**Overnight versus intraday variance (computed).** Overnight (previous close to open) variance is only 8–16% of close-to-close variance in 2019 and 2021–2025 (13%, 9%, 14%, 8%, 9%, 16%) but 39% in 2020 and 25% in 2026 to date; open-to-close accounts for 57–86%. Mean overnight return is +0.024% a day against -0.043% open-to-close. Parkinson (range-based) volatility is 0.70–0.80 of close-to-close volatility; daily autocorrelation is near zero (lag 1 -0.019, lag 2 -0.046) and the weekly variance ratio VR(5) is 1.17; no significance test was recorded, and a ratio above 1 does not rule out some multi-day dependence.[^pse-weekly-reports-dataset] In the one weekly report archived with daily open and close (28 Sep – 2 Oct 2026) the open differed from the previous close by 0.20–0.52% (mean absolute 0.38%; arithmetic on the report).[^pse-weekly-report-2026-10-02:1]

<div class="callout warn">
<span class="label">Scheduled change: 23 Nov 2026, subject to SEC approval</span>

Today's Nasdaq X-stream run-off *rejects* an incoming order at the closing price if a resting counter-order is priced better than the close (closing price 10.00, resting sell at 9.00: an incoming buy at 10.00 is refused), so such resting orders cannot be hit at the close. Under the Nasdaq Eqlipse engine the incoming order would be accepted and matched with the better-priced resting order at the closing price, and run-off orders could be entered, modified and executed only at the closing price. PSE proposed the rule change on 15 Dec 2025; its separate SEC status is not stated.[^pse-cn-2025-0046-board-lot-trading-at-last:5][^pse-cn-2025-0046-board-lot-trading-at-last:6][^pse-cn-2025-0046-board-lot-trading-at-last:8] Run-off liquidity today is therefore structurally thinner than the book suggests, and the closing statistics above should be re-estimated after the cut-over. Negotiated Trades (±5% of VWAP, one firm, a 15-minute window after the run-off) are proposed alongside.[^pse-nte-broker-forum-2026-07-09:8]
</div>

### Execution implications

- **Closing-auction price risk is large in the liquid names.** In the ten most liquid names the close (or open) equals the day's high or low on about 28% (26%) of sessions against about 5% by chance. A passive limit resting into the closing call can be run over by an imbalance print; size closing-auction participation conservatively and prefer the run-off (trading at the already-determined closing price) for the residual.
- **Month-end sessions have about 30% more closing-extreme prints than ordinary days** (43.8% against 34.0% of top-100 stock-days). Widen auction-participation tolerance and avoid leaving a large unfilled balance for the closing call on the last session of a month or quarter.
- **The last-session drift (about -0.5%, t about -3) and the early-month rebound are in-sample facts on a short, down-trending sample.** Use them as a timing prior (for example, avoid scheduling large buys into the last session) and test them on your own data.
- **MSCI review days** (effective at the close of the last business day of Feb, May, Aug and Nov in 2023–2026) mean 3–6× normal value, 70–90% foreign sides and heavy closing-auction and block volume: schedule around them, or enter the closing auction deliberately with a pre-agreed share of the print. FTSE and S&P dates were not examined.
- **News can follow the close.** Company disclosures can be released the same day after the close ([Chapter 13](#/ch/regulatory-constraints)), so a closing print can pre-date same-day news; none of the closing statistics above controls for it.
- **There is no public U-shape evidence.** Calibrate the intraday volume curve from your own ITCH or Level-1 capture. A closing order can be placed late (modifiable until 14:48 and enter-only until 14:50) and hedged against the run-off; passive index funds benchmark to this close, so the closing auction is the natural MOC venue, but its volume share is unknown.

## Volatility, limit hits and circuit breakers

**Annual realised volatility and tail days, PSEi (computed from daily closes in the Weekly Reports; 29 Apr 2019 – 2 Oct 2026; worst and best days are log returns and the day counts use absolute log returns).**[^pse-weekly-reports-dataset]

| Year | Returns | Annualised volatility (close-close) | Mean absolute return | Days with absolute move ≥ 2% | ≥ 3% | ≥ 5% | Worst day (log) | Best day (log) |
|---|---|---|---|---|---|---|---|---|
| 2019 (from 29 Apr) | 164 | 14.6% | 0.71% | 6 | 0 | 0 | -3.00% | +2.71% |
| 2020 | 238 | 33.9% | 1.36% | 47 | 19 | 8 | -14.32% | +7.17% |
| 2021 | 247 | 18.7% | 0.89% | 18 | 9 | 0 | -3.67% | +4.98% |
| 2022 | 245 | 20.7% | 1.01% | 26 | 9 | 0 | -4.35% | +3.54% |
| 2023 | 241 | 14.3% | 0.71% | 6 | 1 | 0 | -2.58% | +3.51% |
| 2024 | 245 | 15.5% | 0.78% | 11 | 0 | 0 | -2.98% | +2.50% |
| 2025 | 242 | 16.9% | 0.80% | 13 | 6 | 0 | -4.39% | +3.44% |
| 2026 to 2 Oct | 186 | 18.2% | 0.86% | 12 | 2 | 2 | -5.10% | +5.96% |

Full-sample annualised volatility is 20.2%. In simple returns the ten worst days were 19 Mar 2020 -13.34% (first session after the 17–18 Mar closure), 12 Mar 2020 -9.71%, 16 Mar 2020 -7.91%, 16 Apr 2020 -7.07%, 9 Mar 2020 -6.76%, 9 Mar 2026 -4.97%, 15 Jun 2020 -4.82%, 7 Apr 2025 -4.30%, 8 Mar 2022 -4.26% and 14 Mar 2022 -4.15%; the best were 26 Mar 2020 +7.44%, 15 Jun 2026 +6.14%, 25 Mar 2020 +5.31%, 10 Nov 2020 +5.23% and 27 May 2021 +5.11%. Mean (high − low) ÷ open for the PSEi was 1.08% (2019), 1.82% (2020), 1.31% (2021), 1.38% (2022), 1.03% (2023), 1.13% (2024), 1.19% (2025) and 1.23% (2026).[^pse-weekly-reports-dataset] Daily moves of 5% or more occurred only in 2020 (eight days) and twice in 2026 (9 Mar and 15 Jun).

**Single-stock moves (computed, 28 consecutive sessions 26 Aug – 5 Oct 2026; close against previous close, stock-days with trades on both days, n = 6,060).**[^pse-dqr-dataset]

| Absolute move | Share of stock-days | Count / per day |
|---|---|---|
| ≥ 5% | 8.4% | |
| ≥ 10% | 1.96% | 119; 4.4 stocks a day |
| ≥ 15% | 0.81% | |
| ≥ 20% | 0.40% | 24; 0.9 stocks a day |
| ≥ 30% | 0.20% | 12 |
| ≥ 50% | 0.02% | 1 |

Extreme movers were illiquid names (for example SRDC +50%, +48% and +34% on PHP 0–1m of value; ABG -30% and -23% on PHP 26–31m).

- **A floor hit.** Asiabest Group (ABG) closed at PHP 42.60 on 30 Sep 2026, exactly -30.0% from the previous close of 60.85 (0.7 × 60.85 = 42.595), with no bid in the report (bid "-", ask 42.60; open 60.00, high 60.85, low and close 42.60; 545,270 shares, PHP 25.8m).[^pse-eod-daily-quotation-2026-09-30:3] The surrounding sessions were +15.6% on 28 Sep (intraday high 76.65), -16.4% on 29 Sep, -22.5% on 1 Oct and -15.5% on 2 Oct (close 27.90; -61.7% in four sessions), then +11.1% on 5 Oct, on PHP 10–74m of daily value.[^pse-dqr-dataset] SRDC (Supercity Realty) moved +48.3%, +12.8%, +33.6% and +31.9% on days when only PHP 0.1–1.2m traded. No source found explains these moves; they are live examples of threshold and thin-book behaviour. The Villar Land floor sequence in November 2025 is similar: after a suspension of under a year the normal band applied and the stock fell from PHP 1,608 to 1,126, 790 and 552 in three consecutive sessions (press report).[^philstar-2025-11-18-vll-plunge]
- **Static and dynamic thresholds.** The static band was ±50% of the previous close or last adjusted closing price; since 24 Mar 2020 it is +50%/-30%.[^pse-implementing-guidelines-trading-rules:10][^pse-cn-2020-0028:1] Dynamic thresholds of 10%, 15% or 20% depend on trade frequency.[^pse-investing-page] The mechanism (a breaching order freezes the stock for Market Control) and lifting rules are in [Chapter 7](#/ch/price-controls); no count of threshold freezes is published.
- **Market-wide breaker history.** The old rule was an automatic 15-minute halt if the PSEi fell 10%, an offshoot of the 2008 crisis; PSE's 30 Apr 2020 release says it tripped four times: 27 Oct 2008 and 12, 13 and 19 Mar 2020.[^pse-web-press-2020-04-30-circuit-breaker][^pse-cn-2020-0044:1] The press accounts used here describe the 12 Mar (intraday -10.33% to 5,697.13; close -9.71%) and 19 Mar triggers; PSE's count adds 13 Mar, for which no intraday detail was read.[^bw-283531][^bw-284527] The three-level breaker (10%, 15%, 20% = 15, 30, 60 minutes) has run since 4 May 2020. Computed: the worst close-to-close fall since 4 May 2020 was -4.97% (9 Mar 2026), so no level can have been reached on a close; intraday lows were not checked individually and no trigger has been reported. Clock cut-offs in the circular were written against the old 15:15 pre-close; no updated statement exists ([Chapter 7](#/ch/price-controls)).
- **PSE's own summary of its pandemic measures** (November 2020) lists the shortened 09:30–13:00 hours, the three-level breaker, the cut of the lower static threshold from 50% to 30% and floorless trading.[^pse-asm-2020-presidents-report:5]

<div class="callout infer">
<span class="label">Inference</span>

A 15–20% annualised benchmark volatility is a 1.0–1.3% daily one-sigma and a 1.1–1.4% average daily range, so position-risk systems should be calibrated to 2022–2026 (17–20% annualised) rather than the calm 2023–2024 window. The +50%/-30% static bands are wide relative to ordinary single-stock moves (about 0.2% of stock-days move 30% or more), so they bind only in extreme episodes such as the ABG floor; practical protection against runaway prices is the dynamic threshold and PSE or CMIC halts, for which no statistics are published. Intraday (five-minute) realised volatility and variance ratios cannot be computed from public PSE data.
</div>

### Execution implications

- Use a volatility-scaled slice size. From the Amihud-type figures, a PHP 5m child order is about 0.03% of an absolute daily move in the top ten names, about 0.3% in ranks 31–60 and above 1.5% in ranks 61–100 (linear scaling, judgement).
- Orders in the book at a market-wide halt are frozen; build order-state recovery for halts and for the new-engine cut-over (see Episodes). Detect breaker states defensively; queue state during a breaker halt is unknown ([Chapter 7](#/ch/price-controls)).
- On a long-only unwind the -30% floor compounds (-51% after two floor days, -66% after three), so liquidating a large position in a gap-down name can take several sessions.

## Episodes

| Episode | Date | Key numbers |
|---|---|---|
| Taper tantrum | May–Dec 2013 | Record close 7,392.20 (15 May), low 5,738.06 (28 Aug), year-end 5,889.83 |
| Pandemic crash and closure | 9–26 Mar 2020 | -9.71% on 12 Mar; closed 17–18 Mar; -13.34% on 19 Mar; +7.44% on 26 Mar |
| Index-review days | End Feb/May/Aug/Nov | PHP 19–40bn a day, 3–6× the trailing median, 70–90% foreign |
| PSEi inclusion day | 31 Jan 2025 | CBC +38.9% on PHP 5.60bn; AREIT PHP 2.72bn |
| Block-dominated days | 2021–2026 | Total value PHP 26–116bn, blocks 61–96% |
| Technical outages | Jan 2022, Jan 2024, Dec 2024, Mar 2025 | Cancelled day; halt 09:32–11:56; late opens 09:55 and 11:10 |
| Manipulation cases | 2025–2026 | Villar Land allegations; SRDC halt |
| Sell-off | Sep–Oct 2026 | PSEi 5,629.03 on 2 Oct, -15.0% from 26 Feb |

### 2013 taper tantrum

The PSEi's record close of 7,392.20 on 15 May 2013 (intraday 7,403.65, +27.4% year to date; 31 record highs in the year) was followed by Fed tapering signals that "derailed" the rally, to a 2013 closing low of 5,738.06 on 28 Aug (-22.4%); the Fed announced the first US$10bn QE reduction in December (effective January 2014), the PSEi still ended 2013 up 1.3% at 5,889.83, and the peso weakened 7.8% to PHP 44.41/USD.[^pse-annual-report-2013:6][^pse-annual-report-2013:11][^pse-annual-report-2013:12] Foreign activity was 51.1% of trades, and full-year net foreign buying was +15.59bn, down 85.8% from the record +109.98bn of 2012, so the foreign pull-back was a slowdown rather than a full-year exit.[^pse-annual-report-2013:12][^pse-annual-report-2017:17] ADVT of PHP 10.52bn in 2013 was the highest of 2013–2025. In 2014 trading dipped early on Fed-tapering worries and China's slowdown.[^pse-annual-report-2014:59]

### March 2020: crash, closure and reopening

- **12 Mar.** The PSEi fell 616.99 points (-9.71%) to 5,736.27, the biggest one-day fall since 2008 and lowest close since December 2012; intraday -10.33% (5,697.13) triggered the 10% breaker shortly before 3 pm and halted trading for 15 minutes until 3:08 pm (the first use since October 2008, per BusinessWorld); value PHP 7.96bn; net foreign selling PHP 0.77bn.[^bw-283531] The finance secretary asked the SSS and GSIS to at least double their daily equity purchases.[^bw-283559]
- **16–19 Mar.** Shortened hours from 16 Mar; no trading 17–18 Mar.[^pse-cn-2020-0017:1][^pse-cn-2020-0021:1] On the 19 Mar reopening (09:30–13:00) the breaker triggered at the open (PSEi -12.4%); the index touched 4,039.15 (-24.29% intraday, "unprecedented"), recovered to 4,751.72 and closed at 4,623.42 (-711.95 points, -13.34%; all-shares -11.92%) on PHP 9.42bn and 1.25bn shares, with net foreign selling of PHP 2.40bn.[^bw-284527][^pse-monthly-report-2020-03:1]
- **Rule changes.** Lower static threshold 50% to 30% (24 Mar) and the three-level breaker (4 May).[^pse-cn-2020-0028:1][^pse-cn-2020-0044:1]
- **Rebound and flows.** +5.31% (25 Mar) and +7.44% (26 Mar); the week of 23–27 Mar traded PHP 34.7bn on 644k trades (129k a day against 75–85k in 2019; computed).[^pse-weekly-reports-dataset] 2020 net foreign selling was PHP 128.57bn, the largest of the decade.[^pse-monthly-report-2021-12:2] March 2020 had 20 trading days, ADVT of PHP 6.96bn (non-regular 0.44bn) and a PSEi range of 4,623.42–6,884.77.[^pse-monthly-report-2020-03:1]

**Crash-week breadth (computed from the Daily Quotation Reports of 12, 16, 19 and 25 Mar 2020, main-board stock lines).** The 19 Mar report is archived;[^pse-eod-daily-quotation-2020-03-19:1] the other three are part of the dataset.[^pse-dqr-dataset]

| Date | Common-stock value (PHP bn) | Block sales (PHP bn) | Top-5 share | Top-10 share |
|---|---|---|---|---|
| 12 Mar | 7.79 | 0.16 | 41% | 59% |
| 16 Mar | 6.21 | 0.24 | 46% | 67% |
| 19 Mar | 9.00 | 0.41 | 49% | 69% |
| 25 Mar | 7.18 | 1.12 | 42% | 61% |

Against 2020 medians of 37% and 55% on ordinary sampled days, concentration rises in stress. On 12 Mar, 30% of the 100 most-traded stocks closed at the day's low and the mean position of the close within the range was 0.19 (0.5 is neutral). On 19 Mar the median top-100 stock traded in a 17.0% high-low range (SM 509.50–698.00, BDO 75.00–99.80, ALI 19.44–25.20, AC 360.00–475.00), 23% closed at the low and stock-level net foreign lines summed to -PHP 2.37bn (BusinessWorld: -2.40bn). By 25 Mar the median range had narrowed to 5.8% and 20% closed at the high; block sales were PHP 1.12bn (143m shares), 13% of the day's value, and the largest line was AGI with PHP 1.08bn of value and PHP 0.74bn of net foreign selling.

### Index-review days

MSCI and index-review days are the highest-value sessions of the year (computed from the Weekly Reports unless noted):[^pse-weekly-reports-dataset]

| Date | Total value (PHP bn) | Detail |
|---|---|---|
| 26 Nov 2019 | 21.2 | |
| 29 May 2020 | 20.4 | |
| 27 Nov 2020 | 27.6 | |
| 27 May 2021 | 23.8 | PSEi +5.11% |
| 29 Nov 2021 | 28.0 | |
| 31 May 2022 | 35.7 | foreign 84% |
| 29 Nov 2022 | 23.5 | |
| 28 Feb 2023 | 21.2 | |
| 31 May 2023 | 24.5 | foreign 81%; 5.3× the trailing 20-day median[^pse-weekly-report-2023-06-02:1] |
| 31 May 2024 | 22.7 | |
| 28 Feb 2025 | 20.6 | |
| 30 May 2025 | 40.0 | 6.2× the median; net foreign -15.3bn; blocks 61% (regular 15.55 + block 24.47)[^pse-dqr-2025-05-30:12] |
| 27 Feb 2026 | 19.6 | |
| 29 May 2026 | 26.5 | net foreign -6.6bn |
| 28 Aug 2026 | 18.8 | ALI PHP 7.2bn (40% of regular value) and ICT PHP 4.3bn (24%); ALI net foreign selling PHP 1.56bn[^pse-dqr-2026-08-28:4][^pse-dqr-2026-08-28:5] |

Press attributions (secondary): "Philippine shares fall ahead of MSCI rebalancing" (30 May 2023, PSEi -1.25% to 6,510.67);[^bw-525845] JFC fell 8.2% in the week of the 30 May 2025 review (AEV added to the MSCI Global Small Cap index, Bloomberry and Wilcon removed);[^bw-676401] "MSCI rebalancing, foreign selling drop BDO shares" (3 Jun 2024);[^bw-598985] Ayala Corp. fell after the May 2026 changes.[^bw-753259] The dates above were inferred from volume spikes and headlines, not from MSCI's calendar.

**PSE's own index review: CBC and AREIT (Jan–Feb 2025).** On 24 Jan 2025 PSE announced that AREIT and China Banking Corp. (CBC) would join the PSEi and Nickel Asia and Wilcon Depot would leave, effective Mon 3 Feb 2025.[^pse-cn-2025-0005:1] On the last session before the change (Fri 31 Jan 2025) CBC traded 62.9m shares for PHP 5.60bn (net foreign buying PHP 0.66bn) and AREIT 65.6m shares for PHP 2.72bn (net foreign buying PHP 0.99bn), against single-name values normally below PHP 1bn; total value was PHP 21.6bn (4.6× the trailing median) while the PSEi fell 4.01% into a bear market.[^pse-dqr-2025-01-31:1][^pse-dqr-2025-01-31:4][^pse-weekly-reports-dataset] CBC opened at PHP 66.95 and closed at its high of PHP 93 (+39% from the open) with a bid at 93 and no offer in the report; BusinessWorld reported +33.8% on the week and +46.5% year to date, with First Resources attributing the jump to index-tracking funds adjusting portfolios.[^pse-dqr-2025-01-31:1][^bw-650452]

<div class="callout infer">
<span class="label">Inference</span>

An index-inclusion date can move an included mid-cap by 30–40% in one session on two to three times its normal weekly value, concentrated at the end of the last session before effectivity. Because index-event days (3–6× volume) and block days (up to 19×) are rare and predictable only for scheduled reviews, execution algorithms need an event-day regime flag.
</div>

### Block-dominated days

| Date | Total value (PHP bn) | Of which block (PHP bn) | Detail |
|---|---|---|---|
| 14 Dec 2022 | 116.0 (19× the trailing 20-day median) | 110.9 | Eagle Cement crosses at PHP 22.02 as a San Miguel unit completed its acquisition and tender offer (572.78m tendered shares, PHP 12.62bn; BusinessWorld puts the whole transaction at about PHP 97.4bn); foreign activity 3%, PSEi +0.5%; EAGLE suspended after the cross pending delisting[^pse-eod-daily-quotation-2022-12-14:11][^bw-493205] |
| 16 Dec 2021 | 87.5 | 80.7 | Aboitiz Power block of 1.84bn shares at PHP 40.01 (PHP 73.6bn) plus a 146.5m-share print (PHP 5.9bn); PHP 79.4bn of foreign net buying (counterparty not identified; BusinessWorld printed the figure as "P79.44 million", a units error because PSE reports in PHP thousands)[^pse-eod-daily-quotation-2021-12-16:10][^bw-418099] |
| 16 Jun 2023 | 53.5 | 44.8 | BPI block of 329.7m shares at PHP 105 (PHP 34.6bn) plus PHP 8.0bn more at the same price[^pse-eod-daily-quotation-2023-06-16:11] |
| 30 May 2025 | 40.0 | 24.47 | MSCI day (above)[^pse-dqr-2025-05-30:12] |
| 26 Sep 2023 | 35.2 | 29.3 | Metro Pacific Investments crosses of 2bn shares at PHP 5.20 (PHP 10.4bn each); voluntary-delisting plan reported 21 Sep 2023[^pse-eod-daily-quotation-2023-09-26:12][^bw-546877] |
| 3 Mar 2021 | 34.1 | 24.7 | Regular value led by small caps AR, DITO and PHA at PHP 1.1–1.25bn each[^pse-dqr-dataset] |
| 11 Sep 2026 | 32.7 | 26.9 (82%) | First Gen PHP 25.8bn[^pse-eod-daily-quotation-2026-09-11:11] |
| 24 Oct 2025 | 26.3 | 19.3 | San Miguel preferred series SMC2J and SMC2K at PHP 75[^pse-eod-daily-quotation-2025-10-24:12] |

A regular-market print can dominate a day too: on 17 Sep 2026 SM alone traded PHP 16.8bn, 73% of regular-market value, with blocks only PHP 2.36bn of PHP 25.5bn.[^pse-eod-daily-quotation-2026-09-17:4][^pse-eod-daily-quotation-2026-09-17:11-12] Overall, 118 of 1,793 sessions (6.6%) had total value of at least twice the trailing 20-day median and 48 (2.7%) at least three times (computed).[^pse-weekly-reports-dataset] The counterparties and reasons for the 16 Dec 2021, 16 Jun 2023, 24 Oct 2025 and 11 Sep 2026 blocks were not identified.

### Technical outages and halts

- **4 Jan 2022.** PSE cancelled the whole session after 43 of 125 trading participants could not connect the Nasdaq trading engine to the Flextrade front end; orders queued from 3:01 pm on 3 Jan until 9:05 am on 4 Jan were cancelled. The PSEi had closed at 7,041.27 (-1.14%) on 3 Jan.[^pse-cn-2022-0001-delay-market-opening:1][^pse-cn-2022-0002-cancellation-of-trading-2022-01-04:1][^bw-421693][^bw-421594]
- **3 Jan 2024.** Trading halted at 09:32 and resumed at 11:56 (the afternoon ran 13:00–15:00 as scheduled) after a glitch in the mobile application's account-authentication process affected at least one-third of participants; PSE explained two days later and analysts urged faster disclosure.[^pse-cn-2024-0001-market-halt:1][^pse-cn-2024-0003-update-market-halt:1][^bw-567311] Value was only PHP 3.11bn on 27,036 trades (about half the 2024 averages of PHP 6.10bn and 58k trades) and the PSEi closed at 6,498.88 (-0.84%; computed).[^pse-weekly-reports-dataset]
- **9 Dec 2024.** The open was delayed to 09:55 (pre-open 09:40, no-cancel 09:50); the notice states no cause.[^pse-cn-2024-0061-adjusted-schedule-2024-12-09:1]
- **24 Mar 2025.** The open was delayed from 09:30 to 11:10 by a "system connectivity issue"; the PSEi closed at 6,192.02 (-1.19%) on PHP 4.63bn and 42,853 trades, about 60% of the 2025 averages (computed), and analysts noted disruptions "every year since 2022".[^pse-cn-2025-0015-adjusted-schedule-2025-03-24:1][^bw-661247][^bw-661414][^pse-weekly-reports-dataset]
- **Closures.** No trading (and no clearing and settlement) on 26 Sep 2022 and on 24 Jul 2024 for weather and flooding; 31 Oct 2025 was declared a non-trading day, and 8, 24, 25, 30 and 31 Dec 2025 and 1 Jan 2026 were also non-trading, so 29 Dec 2025 was the last session of 2025.[^pse-cn-2022-0035-trading-suspension-2022-09-26:1][^pse-cn-2024-0038-trading-suspension-2024-07-24:1][^pse-cn-2025-0038-non-trading-day-2025-10-31:1][^pse-cn-2025-0043-non-trading-days:1]
- **Rule change after the glitches.** SEC-approved on 20 Aug 2025: a market-wide halt now needs participants accounting for more than 50% of the average daily trading value (excluding block sales) of the preceding six months to be unable to trade because of Exchange system problems or natural disasters; every participant must have a correspondent participant.[^pse-cn-2025-0037:1] The old one-third rule was the one invoked on 4 Jan 2022.

<div class="callout warn">
<span class="label">Scheduled change: 23 Nov 2026, subject to SEC approval</span>

PSE is replacing its trading engine ("PSE Trading Engine 2026", Nasdaq Eqlipse): pre-production connectivity testing 29 Sep – 9 Oct, testing 12–22 Oct, Saturday market rehearsals on 31 Oct, 7 Nov and 14 Nov, and a "big bang" go-live on 23 Nov 2026 with no parallel run; Day 1 is limit orders only. The PSE reported in July 2026 that only a minority of broker systems had completed connectivity testing; no later change notice was found by 6 Oct 2026.[^pse-nte-broker-forum-2026-07-09:9][^pse-nte-broker-forum-2026-07-09:5][^pse-nte-faq-2026-08:1] The One Lot One Share, tick-table, run-off and Negotiated Trades changes tied to it are not in force and no SEC approval was found. Three of the four recent disruptions (2022, 2024, 2025) were connectivity or front-end problems at the open rather than engine matching errors, so the cut-over is the next operational risk. Freeze or de-risk algorithms around go-live, re-certify FIX and ITCH, and re-estimate every calibration in this chapter afterwards.
</div>

### Manipulation and enforcement (allegations, as reported)

The SEC's case against Villar Land Holdings (HVN) is described by a *Philstar* opinion column (5 Feb 2026) as the largest stock-price manipulation and insider-trading case the government has filed against a listed company and its owners. As quoted from the SEC: in March 2025 the company released unaudited FY2024 results (total assets PHP 1.33tn against PHP 5.1bn; net income PHP 999.72bn from revaluation of real estate) before its auditor approved them; trading surged and PSE suspended it because audited statements were delayed; the November 2025 audited statements reversed the figures (assets PHP 33bn; net income PHP 1.42bn) and the price fell; the SEC found "recurring trading patterns involving a limited group of related individuals and entities", plus director purchases hours before a material disclosure, and filed a criminal complaint with the DOJ (pending initial evaluation). Mr Villar denies wrongdoing.[^philstar-2026-02-05-villar] These are allegations, not findings. Older cases rest on search snippets only: BW Resources (2000; the SEC recommended charges for insider trading and price manipulation) and Calata Corp (after listing, PHP 4bn traded in two weeks and the price went from PHP 23.95 to PHP 8 in four days).[^inq-biz-buzz-calata] CMIC monitors the market with the Korea Exchange-developed Total Market Surveillance system and can restrict, halt or suspend securities or participants.[^pse-investing-page] The SRDC case (PHP 1.20 to 45.95 in nine trading days before a CMIC-requested halt on 8 Jan 2026) is in [Chapter 7](#/ch/price-controls).[^insiderph-2026-01-08-srdc-halt][^bw-2026-01-09-srdc-resume]

### September–October 2026 sell-off

The PSEi fell from 6,625.46 (26 Feb) to a 6,366.64 August high, 5,956.33 (31 Aug) and 5,629.03 (2 Oct), -3.38% in the week of 28 Sep – 2 Oct on value of PHP 35.4bn and net foreign selling of PHP 4.57bn.[^pse-weekly-report-2026-10-02:1][^pse-monthly-report-2026-08:1] Commentary cites the BSP rate hike, a record-low peso, growth downgrades and US–Iran tensions (headline: "PSEi falls below 5,800 on renewed US-Iran fears", 28 Sep 2026).[^pse-monthly-report-2026-08:2][^gnews-inquirer-2026-09-28]

### Execution implications

- **Pre-trade calendar:** MSCI, FTSE and S&P review dates; PSE block-sale announcements; corporate crosses (tender offers, placements) that make one stock more than half of regular value.
- **Resilience:** confirm order state after outages (2022, 2024 and 2025 events) and plan the 23 Nov 2026 cut-over; do not rely on the closing auction on an outage day, because remaining market phases are compressed.
- Keep a second broker or correspondent route; the 2025 rule makes correspondents mandatory for trading participants, but a buy-side firm still needs its own fallback.

## Literature on PSE microstructure

Direct peer-reviewed microstructure studies of the PSE are almost absent. What exists is calendar-anomaly and efficiency tests on daily or monthly *index* data, event and volatility-regime studies, one IPO-underpricing study, herding studies and policy documents.

| Study | Period and data | Method | Finding | Weight |
|---|---|---|---|---|
| Rufino and Delfino (2016), DLSU Bus. & Econ. Rev. 25(2) | PSEi and six sector indices, daily, 2 Jan 2006 – 7 Jun 2013 (about 1,700 days) | Kruskal-Wallis and pairwise comparisons with a significance correction | No day-of-week effect in the "modernisation" period, unlike pre-2005 studies[^paper-rufino-delfino-2016-dow:2][^paper-rufino-delfino-2016-dow:3][^paper-rufino-delfino-2016-dow:4][^paper-rufino-delfino-2016-dow:8] | Index data only |
| Camba and Camba (2020), JAFEB 7(10) | PSE index data | ADF and Phillips-Perron unit-root, Lo-MacKinlay and Chow-Denning variance-ratio tests | Cannot reject a random walk; weak-form efficiency attributed to modernisation[^paper-camba-camba-2020-random-walk] | Abstract only |
| Camba and Camba (2020), COVID companion | Daily, COVID period | Robust least squares, VAR | COVID infections had a negative, significant effect on the PSEi, the peso and diesel prices[^paper-camba-camba-2020-covid] | Abstract only |
| Pinili and Murcia (2023), Eur. J. Econ. Financ. Res. 7(3) | PSEi daily, 2 Dec 2019 – 5 May 2022 (T about 632) | Chow and Bai-Perron breakpoint tests | Four breakpoints tied to COVID events; worst performance Jan–Apr 2020; random-walk characteristics[^paper-pinili-murcia-2023-covid-breakpoints] | Abstract only |
| Almonares (2019), DLSU Bus. & Econ. Rev. | Monthly PSE returns, Jan 2000 – Jul 2017 | Markov-switching | Two regimes; the high-volatility regime coincides with political crises, the Asian crisis, depreciation and the GFC[^paper-almonares-2019-markov] | Abstract only |
| Calderon (2002), DLSU Bus. & Econ. Rev. 13(2) | PHISIX daily, 61 days around the 8 Aug 2001 demutualisation | Event study, F-tests, GARCH(1,1) | Volatility higher after (GARCH lag coefficient 0.60 before, 0.78 after); the window overlaps the Sep 2001 attacks and has no anomaly adjustment[^paper-calderon-2002-demutualization:3][^paper-calderon-2002-demutualization:13][^paper-calderon-2002-demutualization:15] | Low |
| Atento et al. (2026), Asian Fin. Econ. & Policy | Jul 2018 – Jun 2025; annual price-per-share terciles | Weekly and monthly equal-weighted portfolio returns | No size premium (0.030% weekly, p = 0.793; 0.145% monthly, p = 0.758); strong GARCH(1,1) clustering; Perez (2018) is the only earlier published size or value study with PSE firm-level data[^paper-atento-2026-size-premium] | Abstract only |
| Unite (2002), DLSU Bus. & Econ. Rev. | PSE against Taiwan, Japan, Hong Kong, Singapore, US | Johansen cointegration | Integration around domestic capital-market liberalisation[^paper-unite-2002-integration] | Abstract only |
| Sullivan and Unite (1999) | 104 Philippine IPOs, 1987–1997 | IPO underpricing regressions | Average initial return 22.69%; offer size, firm age and industry do not explain it[^paper-sullivan-unite-1999-ipo] | Abstract only |
| Rahman and Ermawati (2020), Bull. Monetary Econ. & Banking 23(3) | Daily returns of the most liquid ASEAN-5 and US stocks, 4 Jan 2000 – 28 Dec 2018 | CSAD herding regressions, Newey-West errors | US federal funds rate is the dominant global driver of herding; herding on market *up* spikes occurs only in the Philippines[^paper-rahman-ermawati-2020-herding:1][^paper-rahman-ermawati-2020-herding:6][^paper-rahman-ermawati-2020-herding:14] | Daily data |
| Pamplona (2023) | Survey of 395 Filipino retail investors | Structural equation model | Low herd bias; self-reflection reduces herding[^paper-pamplona-2023-herd] | Survey, low-tier venue |
| Briones (2017), J. Philippine Development 41–42 | Structural and regulatory history | Narrative | World ranking by market-cap ratio rose from 44th (2009) to 12th (2014); narrow investor base, weak competition and governance[^paper-briones-2017-stock-market-development] | Abstract only |
| Dioquino (2014) | 2011–2013 PSE turnaround | Case study | Initiatives sorted into "Liquidity" and "Governance"[^paper-dioquino-2014-sicat-case] | Case study |

PSE's own 2013 report documents the reforms of that period: a 10% minimum public ownership for all listed companies, average float of 34.32% at end-2013 (32.28% in 2012), Direct Market Access rules approved on 29 Oct 2013 and an extended pre-close from 4 Nov 2013.[^pse-annual-report-2013:28] The OECD (2024) review covers liquidity, free float, trading costs and market making.[^oecd-capital-market-review-philippines-2024:42]

### Topics with no PSE-specific study found

| Topic | Finding | Closest primary evidence |
|---|---|---|
| Tick size and board lot | No study | PSE consultations: Oct 2023 (cut lot sizes so PHP 100 buys one lot, ticks unchanged) and Dec 2025 (one-share lots and a coarser tick for PHP 10–19.98 stocks)[^pse-cn-2023-0051:3][^pse-cn-2025-0046-board-lot-trading-at-last:4] |
| Price limits and circuit breakers | No study | PSE circulars of March–April 2020[^pse-cn-2020-0028:1][^pse-cn-2020-0044:1] |
| Closing auction | No study | PSE's 2013 consultation (peer pre-close lengths; closing-benchmarked funds)[^pse-memo-extended-pre-close-consultation-2013:1] |
| Broker-ID transparency | No study | The ITCH specification (v2.3, 2014) defines trade messages with passive and active broker IDs when Broker Anonymity is not in force and anonymous versions when it is, "as announced by the exchange"; which mode is live in 2026 is not stated in any PSE document found ([Chapter 11](#/ch/market-data))[^pse-itch-equities-feed-spec-v2-3:15][^pse-itch-equities-feed-spec-v2-3:25] |
| Spreads, information asymmetry, price impact | No study | The end-of-day proxies above |
| Algorithmic trading | No study | PSE consulted on explicit algorithmic-trading rules in Sep 2023; no approval was found[^pse-cn-2023-0043:1] |

"None found" is not proof of absence: the search covered OpenAlex and Crossref queries combining Philippine or PSE with tick size, price clustering, price limits, circuit breaker, intraday, bid-ask spread, liquidity premium, trading volume, herding and foreign ownership, but not Google Scholar, SSRN or ScienceDirect. Several papers are paywalled and are summarised from abstracts only.

<div class="callout infer">
<span class="label">Inference</span>

Execution research on the PSE must be proprietary: spreads, depth, auction imbalance and intraday curves are not published and have not been studied in public. The few published findings (a random walk at daily frequency, no weekday effect, herding on up-spikes tied to US rates) are broadly consistent with the computed daily results here (near-zero daily autocorrelation, no robust weekday effect, regimes driven by Fed and EM flows) but say nothing about intraday behaviour.
</div>

### Execution implications

- Use US and European evidence on tick-size, auction and price-limit effects only as priors; build PSE-specific impact and auction models from your own order and ITCH data.
- Expect regulatory microstructure changes (new engine, board-lot table, negotiated trades, market-making rules, derivatives plans) to invalidate historical calibrations; re-estimate after each change ([Chapter 16](#/ch/execution-implications), [Chapter 17](#/ch/reform-timeline)).

## What is not in the public record

- **Effective spreads, depth at best or top-five levels, quoted-spread time series and price-impact curves.** Only end-of-day proxies exist; intraday ITCH or Level-1 capture is needed.
- **Intraday volume curve and the share of volume** in the pre-open, continuous session, pre-close and run-off, and Closing VWAP session; auction imbalance data; the closing auction's share of volume. No lunch-break or U-shape study exists.
- **A public time series of the top-ten share.** "Active Companies by Trading Value", full broker rankings and block-sale listings appear only in the paid full Monthly Report, of which only February 2020 is archived (the website shows a top-10 broker snapshot only); the series above are sampled reconstructions.
- **Investor-type splits.** Nothing beyond the retail/institutional chart (from 2019) and the foreign/local ratio: no local-institution against foreign-institution split, no online share of value, and no proprietary, high-frequency or algorithmic share.
- **Threshold freezes and market-wide halts.** PSE publishes no surveillance statistics or counts of dynamic-threshold or static-threshold freezes.
- **SMIP definitions.** "Active" is defined only in the 2013 edition and coverage changes between editions, so the series is indicative.
- **Post-July-2025 all-in costs against peers.** The figures here are arithmetic on the OECD table and the BIR rate; no published post-reform comparison was found.
- **Counterparties of the large block days** and the unexplained moves in ABG and SRDC.
- **Recalibration after 23 Nov 2026.** Every spread, tick-constraint, closing and concentration statistic here pre-dates the new engine and any One Lot One Share or tick-table change.
