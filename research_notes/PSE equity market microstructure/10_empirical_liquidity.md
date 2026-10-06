# PSE empirical market quality, liquidity and trading behaviour (inputs for Chapter 15, "Empirical evidence")

*Status: v4, 6 Oct 2026 (all eight sub-topics drafted and reviewed once; v4 adds the 2012-2025 account and active-account series (Table B) and the 2019-2022 retail/foreign shares from PSE's ASM President's Reports; open gaps listed per section). All peso figures are PHP; FX used for rough USD translation is the PSE's own end-of-day rate of PHP 62.775/USD on 2 Oct 2026 [^pse-eod-daily-quotation-2026-10-02:10] (it was 58.13 on 24 May 2024 [^pse-eod-daily-quotation-2024-05-24:11]).*

**Labelling convention.** (P) = primary source (PSE, OECD, SEC/PSE circulars, peer-reviewed paper). (S) = secondary only (news, analyst quote). (I) = my inference or own calculation; own calculations use PSE primary data that I parsed (the PSE Weekly Reports 2019-05-03 to 2026-10-02 = 391 one-page PDFs, and the PSE Daily Quotation Reports for 176 sampled days, 28 consecutive days 2026-08-26 to 2026-10-05, 164 month-end/month-start sessions Jan 2024 - Sep 2026 and 26 event days, 373 distinct reports in all) and are cited to the dataset index [^pse-market-reports-index] (documents.pse.com.ph/market_report/...). Only the individual reports quoted in the text are archived. Where I say "ADVT" I mean the PSE's *average daily value traded* (total market = regular + non-regular, i.e. incl. block sales and odd lots) in PHP.

**Key conventions of PSE statistics (P).**
- "Non-regular market" in the PSE Monthly Report = block sales + odd-lot trades [^pse-monthly-report-sample:11]. "Regular market" = the normal central order book (continuous + auctions).
- PSE's "foreign ratio" = (foreign buying + foreign selling) / (2 x total value traded), i.e. the share of trade *sides* that are foreign (check: 2017: 1,970.23 / (2 x 1,958.36) = 50.3% [^pse-annual-report-2017:17]).
- "Total market capitalisation" includes three foreign-domiciled issuers; "domestic market capitalisation" excludes them [^pse-monthly-report-2025-12:2]. The two diverge strongly (end-2024: total 20.01tn vs domestic 14.57tn).

---

## 1. Headline statistics 2015-2026 (size, turnover, velocity, listings, IPOs, index history)

### Takeaway
The PSE is a ~PHP 13-15tn (domestic) / ~US$230-320bn market that trades only ~PHP 6-9bn (~US$100-150m) a day: ADVT peaked at PHP 9.0bn in 2021, fell to PHP 6.1bn in 2023-24 and recovered to PHP 7.3bn in 2025 (PHP 7.7bn YTD to 2 Oct 2026). Annual turnover velocity (value traded / domestic market cap) has drifted from 19% (2015) to 10-13% (2023-25); the OECD ranks it the lowest among six ASEAN peers (8.8% on total cap in 2023). The index is range-bound (daily closes between ~5.6k and ~7.6k since 2021, the Mar-2020 low being 4,623; ATH 9,058.62 on 29 Jan 2018) and was at 5,629 on 2 Oct 2026 (-7.0% YTD, -15.0% from the 26 Feb 2026 closing high of 6,625.46).

### Cited Findings
**Table A - year-by-year (P unless marked)**

| Year | PSEi close | Total MCAP (PHP tn) | Domestic MCAP (tn) | Value traded (tn) | ADVT (PHP bn; days) | Net foreign (PHP bn) | Foreign ratio | Listed cos. (yr-end) | New IPOs (primary proceeds) |
|---|---|---|---|---|---|---|---|---|---|
| 2013 | 5,889.83 | 11.93 | 9.65 | 2.55 | 10.52 | +15.59 | 51% | 257 | IPO proceeds 60.98bn [^pse-annual-report-2017:17] |
| 2014 | 7,230.57 | 14.25 | 11.71 | 2.13 | 8.80 | +55.45 | 49% | 263 | 11.41bn [^pse-annual-report-2017:17] |
| 2015 | 6,952.08 | 13.47 | 11.19 | 2.15 | 8.96 | -59.76 | 47.9% | 265 | 4 IPOs, 5.20bn [^pse-annual-report-2015:32] |
| 2016 | 6,840.64 | 14.44 | 11.87 | 1.93 | 7.81 | +2.80 | 51.3% | 265 | 4 IPOs, 28.92bn [^pse-annual-report-2016:33] |
| 2017 | 8,558.42 | 17.58 | 14.49 | 1.96 | 8.06 | +56.20 | 50.3% | 267 | 4 IPOs, 22.53bn [^pse-annual-report-2017:16] |
| 2018 | 7,466.02 | 16.15 | 13.54 | 1.74 | 7.15 | -61.01 | 51.3% | 267 | 1 IPO, 8.15bn [^pse-annual-report-2018:9][^pse-annual-report-2018:32] |
| 2019 | 7,815.26 | 16.71 | 13.95 | 1.77 | 7.29 (243) | -14.26 | 55.4% | 268 | 4 IPOs, 13.41bn [^pse-annual-report-2019:5][^pse-annual-report-2019:32] |
| 2020 | 7,139.71 | 15.89 | 13.10 | 1.77 | 7.35 (241) | -128.57 | 45.4% [^pse-asm-2021-presidents-report:5] | n/a | IPO proceeds 44.3bn (count not stated); total capital raised 104bn (2019: 101bn) [^bw-336789][^pse-monthly-report-2020-12:1][^pse-monthly-report-2021-12:2] |
| 2021 | 7,122.63 | 18.08 | 14.56 | 2.23 | 9.00 (248*) | -2.75 | 36.0% | 276 | 8 IPOs; total capital raised 234.48bn (record) [^pse-monthly-report-2021-12:2][^pse-infographic-fy21:1] |
| 2022 | 6,566.39 | 16.56 | 13.28 | 1.79 | 7.30 (245) | -68.05 | 40.7% | 286 | 10 new listings incl. REITs; primary capital raised 99.17bn [^pse-monthly-report-2022-12:2][^pse-infographic-fy22:1] |
| 2023 | 6,450.04 | 16.74 | 13.10 | 1.47 | 6.09 (242) | -53.65 | 43.9% | 283 | 3 listings; primary raised 140.75bn [^pse-monthly-report-2023-12:2][^pse-infographic-fy23:1] |
| 2024 | 6,528.79 | 20.01 | 14.57 | 1.49 | 6.10 (245) | -23.19 | 46.2% | 283 | 3 listings (OGP, CREC, XG); primary 75.78bn [^pse-monthly-report-2024-12:2][^pse-infographic-fy24:1] |
| 2025 | 6,052.92 | 18.73 | 13.65 | 1.78 | 7.33 (243) | -51.20 | 46.3% | 282 | 2 IPOs (TOP, Maynilad "MYNLD"); primary 138.75bn [^pse-monthly-report-2025-12:2][^pse-infographic-fy25:1] |
| 2026 YTD (to 2 Oct) | 5,629.03 | 19.44 (2 Oct) | 13.06 (end-Aug) | 1.43 (own calc: 7.714bn x 186 d) | 7.71 (186) | -31.5 (2 Oct) | 49.03% (PSE YTD) | 280 | none listed in 1Q/2Q26 events; pipeline Vitro REIT (12 Oct), Globe Fintech/"Mynt" IPO ~92.3bn (19 Oct), PNB Holdings by introduction [^pse-weekly-report-2026-10-02:1][^pse-monthly-report-2026-08:1][^pse-asm-2026-president-report:8] |

*Notes to Table A.* (i) 2013-2018 rows come from the PSE annual-report five-year tables [^pse-annual-report-2017:17][^pse-annual-report-2018:32][^pse-annual-report-2019:32]; 2018 domestic MCAP was restated from 13.54tn (AR2018) to 13.55tn (AR2019). (ii) 2020-2025 rows from the December Monthly Reports' "Monthly Review" and the annual infographics. (iii) *2021 day count 248 is from my parse of the weekly reports (ADVT 9.002bn reproduces PSE's 9.00bn); PSE's own day count for 2021 is not in the extracted preview. (iv) The infographic "total capital raised" is *primary shares only* (2024: 75.78bn; 2025: 138.75bn); the press release totals include secondary shares, warrants and private placements (2024: 82.37bn; 2025: 144.14bn) [^pse-infographic-fy24:1][^pse-press-2024-12-27][^pse-press-2025-12-29]. (v) 2025 net foreign selling is 51.20bn in the Monthly Report/infographic but 51.78bn in the 29 Dec 2025 press release (the latter was issued before the last two sessions were final) [^pse-monthly-report-2025-12:2][^pse-press-2025-12-29]. (vi) The 2020 foreign ratio (45.4%) is from PSE's ASM 2021 President's Report [^pse-asm-2021-presidents-report:5] (repeated in [^pse-asm-2022-presidents-report:5]); the 2020 listed-company count is not in any retrieved source.

**Turnover velocity (I; own calculation from Table A).** Value traded / year-end domestic MCAP: 2013 26.4%; 2014 18.2%; 2015 19.2%; 2016 16.3%; 2017 13.5%; 2018 12.8%; 2019 12.7%; 2020 13.5%; 2021 15.3%; 2022 13.5%; 2023 11.2%; 2024 10.2%; 2025 13.0%. On *total* MCAP the ratios are lower (2023 8.8%, 2024 7.4%, 2025 9.5%). ADVT / domestic MCAP in bp per day: 10.9 (2013), 5.2-5.6 (2017-2020), 6.2 (2021), 4.2 (2024), 5.4 (2025). The OECD independently reports a 2023 PSE turnover ratio of 8.8% (lowest of six ASEAN markets; peer mean 49%, range 22-87%), US$24.9bn traded in 2023 (lowest of the six) and a Main Board average turnover ratio of 14% over 2010-2023 [^oecd-capital-market-review-philippines-2024:42][^oecd-capital-market-review-philippines-2024:43].

**Trading days.** 241 (2020), 245 (2022), 242 (2023), 245 (2024), 243 (2025); 162 days to end-Aug 2026 and 186 to 2 Oct 2026 [^pse-monthly-report-2020-12:1][^pse-monthly-report-2022-12:1][^pse-monthly-report-2023-12:1][^pse-monthly-report-2024-12:1][^pse-monthly-report-2025-12:1][^pse-monthly-report-2026-08:1][^pse-weekly-report-2026-10-02:1]. 2025 value traded PHP 1.78tn (+19.1%) [^pse-monthly-report-2025-12:2]; Jan-Aug 2026 PHP 1.22tn (+7.3% y/y) [^pse-monthly-report-2026-08:2]; 1H26 equities trading value PHP 926.54bn vs 809.27bn in 1H25 [^pse-analyst-briefing-1h-2026:7].

**Non-regular (block + odd-lot) share of ADVT (P/I).** 2019 14.2% (1,036.72 of 7,294.56m) [^pse-monthly-report-2019-12:1]; 2020 11.2% [^pse-monthly-report-2020-12:1]; 2022 18.9% (spiked by a single 14 Dec 2022 block, see s.7) [^pse-monthly-report-2022-12:1]; 2023 20.7% [^pse-monthly-report-2023-12:1]; 2024 15.6% [^pse-monthly-report-2024-12:1]; 2025 18.8% (1,374.68 of 7,328.26m) [^pse-monthly-report-2025-12:1]; Jan-Aug 2026 17.4% (1,314.15 of 7,561.17m) [^pse-monthly-report-2026-08:1].

**2026 YTD path.** End-Mar 5,948.94 (-1.7% YTD; ADVT 7.90bn; net foreign BUYING 12.14bn in 1Q) [^pse-infographic-1q26:1]; end-Jun 6,037.17 (ADVT 7.72bn; net foreign selling 11.36bn; MCAP 19.44tn) [^pse-infographic-2q26:1]; 14 Aug 6,297.30 (+4.0% YTD; total MCAP 20.56tn; AVTO 7.57bn; net foreign selling 8.89bn vs 40.18bn at the same date of 2025) [^pse-analyst-briefing-1h-2026:3]; end-Aug 5,956.33 (-1.6% YTD; Aug ADVT 7.53bn; Aug net foreign outflow 16.56bn; YTD foreign ratio 48.3% vs 46.9% a year earlier; total MCAP 19.82tn, domestic 13.06tn) [^pse-monthly-report-2026-08:1][^pse-monthly-report-2026-08:2]; 2 Oct 5,629.03 (week -3.38%; YTD high close 6,625.46, low close 5,629.03; YTD net foreign selling -31.5bn; YTD ADV 7.71bn) [^pse-weekly-report-2026-10-02:1]. Context in the Monthly Report: BSP rate hike, record-low peso and growth-forecast downgrades [^pse-monthly-report-2026-08:2]. The 5 Oct 2026 close of 5,743.21 (+2.03%) is from a Yahoo Finance quote (S; not independently verified).

**Index history and drawdowns (P unless marked).**
- 2013 taper-tantrum year: record close 7,392.20 / intraday 7,403.65 on 15 May 2013 (+27.4% YTD at the time; 31 record highs in 2013); the index then fell on the Fed's taper signals but still closed 2013 at 5,889.83 [^pse-annual-report-2013:6][^pse-annual-report-2013:11]. 2014 closed at 7,230.57 (peak 7,360.75) [^pse-annual-report-2014:32].
- All-time high 9,058.62 on 29 Jan 2018 (intraday per AR); 2017 close 8,558.42 = +25.1% with 14 record highs; 2018 close 7,466.02 (-12.8%) [^pse-annual-report-2018:6][^pse-annual-report-2018:28][^pse-annual-report-2017:16].
- COVID crash (I from PSE weekly data): 2019-07-15 close 8,365.29 -> 2020-03-19 close 4,623.42 = -44.7% (-49.0% from the Jan-2018 ATH); March 2020 monthly low 4,623.42 and month-end 5,321.23 (-21.6% m/m; YTD -31.9%) [^pse-monthly-report-2020-03:1].
- (P) **PSE's own November-2020 snapshot.** At 30 Oct 2020 the PSEi (6,324.00) was 19.1% below the 2019 close (7,815.26 on 27 Dec 2019), 36.8% above the 2020 low close (4,623.42 on 19 Mar 2020) and 30.2% below the all-time high (9,058.62 on 29 Jan 2018); year-to-date ADVT was PHP 6.70bn (-8.2% against 7.29bn in 2019), domestic market cap PHP 11.58tn (-17.0% YTD) and net foreign selling PHP 111.54bn [^pse-asm-2020-presidents-report:3][^pse-asm-2020-presidents-report:4]. By the end of 2020 ADVT had recovered to PHP 7.35bn and domestic market cap to PHP 13.10tn [^pse-asm-2021-presidents-report:4].
- Later troughs (I, closing values): 2022-09-30 5,741.07; 2023-10-27 5,961.99; 2025-11-14 5,584.35; 2026-10-02 5,629.03 (so 2 Oct 2026 was the lowest close since 14 Nov 2025). Year highs: 2024-10-07 7,554.68; 2025-01-06 6,625.17; 2026-02-26 6,625.46 [^pse-weekly-reports-dataset]. 2025: -7.29% (the first annual fall since 2023; 2024's +1.2% was the first y/y gain since 2019 per PSE) [^pse-monthly-report-2025-12:2][^pse-press-2024-12-27]. PSE's CEO attributed 2025's weakness to a corruption scandal, a weak peso and a disappointing Q3 GDP print [^pse-press-2025-12-29].

### Inferences
- (I) Liquidity is a *flow* problem more than a size problem: with domestic MCAP of ~PHP 13-15tn and ADVT of ~PHP 6-9bn, ~5 bp of market cap trades per day; at PHP 62.8/USD the whole market trades only ~US$120m/day.
- (I) One-off block crosses inflate the annual averages: the 16 Dec 2021 block alone (PHP 80.7bn) adds ~PHP 0.33bn to 2021's 9.00bn ADVT (ADVT ex-that block ~8.7bn) and the 14 Dec 2022 Eagle Cement cross (PHP 110.9bn) adds ~PHP 0.45bn to 2022's 7.30bn (ex-block ~6.85bn) [^pse-eod-daily-quotation-2021-12-16:10][^pse-eod-daily-quotation-2022-12-14:11]. The post-2022 decline in ADVT to ~6.1bn coincided with BSP tightening and net foreign selling in every year since 2022 (cumulative 2022-2025: -196.1bn; 2026 YTD another -31.5bn). It also coincided with the unwinding of the retail boom: retail's share of value fell from 31.1% (2021) to 18.4% (2023), and about 56% of the PHP 0.76tn fall in value traded between 2021 and 2023 was retail (own arithmetic, s.3) [^pse-asm-2022-presidents-report:4][^pse-asm-2023-presidents-report:6].
- (I) The PSE's published turnover metrics are inflated by block sales (non-regular share of ADVT 11-21% in 2019-2026), so the *regular-market* ADV that an algorithm can access is ~79-89% of the headline.

### Execution implications
- Budget capacity from regular-market ADV (~PHP 6.2bn YTD 2026, ~US$100m), not from the headline ADVT; block-sale volume is not available to a participation algo.
- Because ADVT swings +-20-30% year to year and has monthly dispersion of 4-5x (e.g. 3.96bn in Nov 2023 vs 12.3bn in Dec 2022 [^pse-monthly-report-2023-12:1][^pse-monthly-report-2022-12:1]), size participation limits on a *trailing 20-60 day median* of regular-market value, not the annual mean.
- A single PHP 1bn parent order is ~13% of average daily total value; at 10% participation it needs >1 full day even in the broad market.

### Gaps
- The 2020 listed-company count and the 2020 IPO count are not in retrieved documents (the 2020 foreign ratio was found in the ASM 2021 President's Report). The FY2020-FY2023 annual reports exist on documents.pse.com.ph (sites/4) but are image-only SEC Form 17-A filings (only the cover pages have a text layer) [^pse-annual-report-2020-17a]; the OCR text of the FY2020 MD&A pages (physical pp. 31-32, 36) covers PSE's own revenue and costs, not market statistics, and the FY2021-FY2023 files were not OCR-read. The FY2024/FY2025 reports are archived by other researchers (pse-annual-report-2024/2025) and are also SEC-form style.
- PSE "Fact Book" not located; the PSE Listing Statistics page is script-rendered and could not be scraped.

---

## 2. Concentration of turnover (top-10/20 names, PSEi constituents, block sales)

### Takeaway
Turnover is highly concentrated: on a typical day the top 10 names account for ~60% and the top 20 for ~79% of regular-market value (median of 176 sampled days 2019-2026), only ~14 names trade >= PHP 100m (~US$1.6m) and ~24 names >= PHP 50m per day, and the PSEi's 30 constituents carried 76.7% of regular-market value in Feb 2020. In Aug-Oct 2026 a single stock (ICTSI) alone was ~25-30% of regular-market value on most days.

### Cited Findings
- (P/I) **Feb 2020 (full Monthly Report):** regular-market value PHP 112.07bn, non-regular (block + odd lot) PHP 20.50bn, total PHP 132.56bn over 19 days [^pse-monthly-report-sample:11]; the 30 PSEi constituents traded PHP 85.90bn of regular-market value [^pse-monthly-report-sample:15] = 76.7% of regular value; the top-10 by value (ALI, SMPH, SM, BDO, AC, BPI, URC, MWC, MBT, JFC) summed to PHP 63.15bn = 56.3%, top-20 PHP 84.99bn = 75.8%, top-25 PHP 90.89bn = 81.1% [^pse-monthly-report-sample:17]. All 25 names with the highest monthly volume-turnover ratios (2.5%-49.6% of shares outstanding in one month, e.g. ISM 49.6%, FRUIT 37.2%, MAH 35.6%, TECH 20.2%) were non-PSEi small/mid caps [^pse-monthly-report-sample:16].
- (I; own calculation from 176 sampled Daily Quotation Reports, 2 days per month, Jun 2019 - Sep 2026 [^pse-dqr-dataset]) **median share of regular-market value, by year:** top-1 12.1% (2019), 13.5 (2020), 10.6 (2021), 11.1 (2022), 11.6 (2023), 13.3 (2024), 16.1 (2025), 22.7 (2026); top-5 39.6 / 37.3 / 34.6 / 37.8 / 41.7 / 43.2 / 47.6 / 49.8; top-10 60.5 / 55.3 / 51.2 / 56.2 / 59.3 / 64.8 / 64.8 / 64.1; top-20 77.5 / 76.2 / 71.2 / 77.9 / 79.4 / 83.6 / 81.3 / 80.5. All-days medians: top-1 13.3%, top-5 41.0%, top-10 59.7%, top-20 79.0%. Concentration has risen since 2021.
- (I; same dataset) **Breadth of the liquid universe (median per day):** names with regular-market value >= PHP 100m: 14 (2019), 16, 16, 16, 10 (2023), 14, 14, 14 (2026); >= PHP 50m: 24, 25, 30, 25, 19, 21, 22, 23; >= PHP 10m: 54, 54, 62, 48, 42, 44, 48, 52; >= PHP 1m: ~91-128. Traded issues per day: 224-254 (of ~280 listed companies plus preferreds/warrants/ETFs).
- (I; 28 consecutive sessions 2026-08-26 to 2026-10-05, main-board only) top-1 27.5%, top-5 52.9%, top-10 66.8%, top-20 81.2% (daily means). ICT (International Container Terminal Services) was in the top-10 on all 28 days and was 21.0% of pooled regular value, SM 15.3% (inflated by 17 Sep when SM printed PHP 16.8bn = 73% of the day's regular value), ALI 6.8%, BDO 5.6%, AC 5.4%, MBT 2.9%, BPI 2.3%, MER 2.1%, SMPH 2.0%, APX 2.0% [^pse-dqr-dataset][^pse-eod-daily-quotation-2026-09-17:11].
- (I; same 28 days) average daily total value PHP 8.77bn of which regular PHP 6.87bn (78%), block sales PHP 1.90bn (pooled 21.7%; mean-of-daily 15.1%), odd-lot ~PHP 1.1m (0.01%), and the new VWAP session PHP 1.05m (0.012%). Block sales were 82% of the 11 Sep 2026 total (PHP 26.9bn of 32.7bn) and 32% on 2 Oct (PHP 2.63bn of 8.18bn) [^pse-eod-daily-quotation-2026-10-02:11].
- (I; 176-day sample) pooled block-sale share of total value by year: 15.2% (2019), 7.7 (2020), 13.0 (2021), 12.1 (2022), 19.8 (2023), 12.6 (2024), 19.5 (2025), 13.4 (2026 YTD sample); all-sample 13.9%. Odd-lot share <= 0.015%. VWAP-session share 0.05% (2024), 0.09% (2025), 0.11% (2026) [^pse-dqr-dataset].
- (P) The PSEi has 30 members; the PSE MidCap Index covers the top 20 mid-sized companies and the DivY Index the top 20 high-yielders [^pse-asm-2026-president-report:5]. RL Commercial REIT replaced Alliance Global in the PSEi in 1Q26 [^pse-infographic-1q26:1].
- (P) **PSEi weights (end-Sep 2025 factsheet):** the PSEi (30 "largest and most active" companies, free-float market-cap weighted, calculated every minute, reviewed semi-annually) had total free-float market cap of PHP 8,588.80bn (largest constituent PHP 952.13bn, smallest 66.99bn, mean 286.29bn, median 166.17bn); the top-5 weights were ICT 14.0%, SM 12.2%, BDO 9.0%, BPI 8.6% and SMPH 6.9% = 50.6%; sector weights Financials 24.6%, Holding Firms 26.1%, Services 20.8%, Industrial 15.4%, Property 13.1%; dividend yield 3.72%, P/E 9.91, P/B 1.25 [^pse-psei-factsheet-2025-09:1][^pse-psei-factsheet-2025-09:2]. The one-minute calculation interval is the basis of the random-walk benchmark used in s.5 (about 270 observations per session).
- (P) Ownership concentration drives low free float: in 2023 half of Main Board companies had free float <28% and only a quarter >40%; corporations hold 47% of listed equity; in 49% of listed companies the largest shareholder owns >50%; the PSE minimum public ownership is 20-33% at listing and 10% thereafter [^oecd-capital-market-review-philippines-2024:43][^oecd-capital-market-review-philippines-2024:121]. Average float of listed companies was 34.32% at end-2013 [^pse-annual-report-2013:28]. The PSE has a proposal (May 2026) for tiered MPO rules awaiting SEC approval [^pse-asm-2026-president-report:22].

### Inferences
- (I) With ~14 names above PHP 100m/day, a book of US$50-100m cannot be built in the "mid-cap" universe without dominating volume; the effective investable universe for institutional size is roughly the ~30-40 index-weight names.
- (I) Rising single-name dominance (ICT) is a *regime* feature of Aug-Oct 2026, not a structural constant (medians for 2019-2025 are 11-16%); it should be treated as a stress case for basket algos that assume diversified volume.
- (I) Block trades are a structural second venue (13-20% of value); the proposed "Negotiated Trades" rule would extend this to smaller pre-arranged deals [^pse-asm-2026-president-report:23].

### Execution implications
- Rank-based participation: use name-specific rolling ADV; for names outside the top ~40, ADV < PHP 10m (~US$160k) means even a PHP 5m order is ~50% of ADV.
- Do not assume a basket is "diversified": top-10 names are ~60% of market-wide value, so a market-neutral basket of 50 names will see highly skewed fill rates (tail names fill late/never).
- Watch for large single-name event days (corporate crosses, index days) when one name takes >50% of regular value: volume-based schedules anchored on trailing volume will under-participate in the other names that day.

### Gaps
- The PSE publishes "Active Companies By Trading Value", broker rankings and block-sale listings only in the full (paid) Monthly Report; the public "preview" has two pages. Only the Feb 2020 full report is archived (by another researcher). No public time series of top-10 share exists; mine is a sampled reconstruction.
- PSEi-constituent share of value was computed only for Feb 2020; constituent histories (index policy PDFs exist in the archive) were not applied to the 176-day sample.

---

## 3. Participation: foreign vs local, retail vs institutional, online share

### Takeaway
Foreigners are ~46-49% of PSE trade *sides* (not of ownership), and have been net sellers in every year since 2022 (2022 -68.05bn; 2023 -53.65bn; 2024 -23.19bn; 2025 -51.20bn; 2026 YTD -31.5bn at 2 Oct); retail has been only ~18-20% of value turnover in 2022-25 (it was 26.9% in 2020 and peaked at 38.9% in Jan-May 2021) even though 99% of the 3.64m accounts are retail and 88.6% are online; ~12% of accounts were active in 2025.

### Cited Findings
**Table B - Stock Market Investor Profile (SMIP): accounts, online accounts and active share, 2012-2025 (P unless marked)**

| Year | Accounts (growth) | Online accounts (share of accounts) | Reporting TPs: all / online | Active share, all accounts | Active share, online accounts | Active share: retail / inst. / local / foreign (%) | Implied active accounts (I) | Sources |
|---|---|---|---|---|---|---|---|---|
| 2012 | 525,850 | 78,216 (14.9%*) | - | 24.3% | - | - | 127,825 (stated) | [^pse-investor-profile-2013:2][^pse-investor-profile-2013:3][^pse-investor-profile-2013:6] |
| 2013 | 585,562 (+11.4%) | 129,255 (22.1%*) | 135 / 14 | 23.9% | 43.4% | 23.7 / 30.9 / 23.7 / 39.7 | 140,145 (stated) | [^pse-investor-profile-2013:2][^pse-investor-profile-2013:3][^pse-investor-profile-2013:6] |
| 2014 | 640,665 (+9.4%) | 174,592 (27.3%*) | 135 / 18 | 33.6% | 64.6% | 34.1 / 22.4 / 33.6 / 30.8 | ~215k | [^pse-investor-profile-2014:2][^pse-investor-profile-2014:3] |
| 2015 | 712,549 (+11.2%) | 236,669 (33.2%*) | 132 / 22 | 32.7% | 66.6% | 33.4 / 18.0 / 32.7 / 29.6 | ~233k | [^pse-investor-profile-2015:2][^pse-investor-profile-2015:3] |
| 2016 | 773,187 (+8.5%) | 302,516 (39.1%*) | 133 / 26 | 33.4% | 61.2% | 33.8 / 24.4 / 33.5 / 28.8 | ~258k | [^pse-investor-profile-2016:2][^pse-investor-profile-2016:3] |
| 2017 | 868,810 (+12.4%) | 388,864 (44.8%*) | 132 / 26 | 34.0% | 57.4% | 34.2 / 28.8 / 34.0 / 33.6 | ~295k | [^pse-investor-profile-2017:2][^pse-investor-profile-2017:3] |
| 2018 | 1,089,413 (+25.4%) | 625,763 (57.4%*) | 131 / 27 | 29.1% | 41.6% | 29.1 / 28.5 / 29.1 / 28.4 | ~317k | [^pse-investor-profile-2018:2][^pse-investor-profile-2018:3] |
| 2019 | 1,228,038 (+12.7%) | 782,118 (63.7%*) | 130 / 32 | 25.2% | 34.2% | 25.2 / 22.2 / 25.2 / 22.7 | ~309k | [^pse-investor-profile-2019:2][^pse-investor-profile-2019:3] |
| 2020 | 1,396,753 (+13.7%) | 936,200 (67.0%*) | 130 / 32 | 30.0% | 37.1% | 30.3 / 17.3 / 30.1 / 24.8 | ~419k | [^pse-investor-profile-2020:2][^pse-investor-profile-2020:3] |
| 2021 | 1,620,017 (+16.0%) | 1,159,034 (71.5%) | 130 / 33 | 31.9% | 39.8% | 32.0 / 22.3 / 31.9 / 27.8 | ~517k | [^pse-investor-profile-2021:2][^pse-investor-profile-2021:3] |
| 2022 | 1,712,734 (+5.7%) | 1,258,907 (73.5%) | 130 / 38 | 20.2% | 22.2% | 20.1 / 23.7 / 20.1 / 24.3 | ~346k | [^pse-smip-2022:2][^pse-smip-2022:3] |
| 2023 | 1,906,019 (+11.3%) | 1,525,768 (80.0%) | 123 / 38 | 17.6% | 19.3% | 17.6 / 20.5 / 17.5 / 22.7 | ~335k | [^pse-smip-2023:2][^pse-smip-2023:3] |
| 2024 | 2,860,234 (+50.1%) | 2,471,860 (86.4%) | 121 / 39 | 23.1% | 24.5% | 23.1 / 19.5 / 22.9 / 36.1 | ~661k | [^pse-smip-2024:2][^pse-smip-2024:3] |
| 2025 | 3,641,067 (+27.3%) | 3,226,616 (88.6%) | 122 / 35 | 11.8% | 12.0% | 11.7 / 14.6 / 11.7 / 20.4 | ~430k | [^pse-investor-profile-2025:2][^pse-investor-profile-2025:3] |

*Notes to Table B.* (i) "Active" = the account traded at least once in the year; the definition is printed only in the 2013 edition [^pse-investor-profile-2013:3] and later editions do not restate it. Active shares for 2013-2025 were read from the rendered infographics (the PDF text layer scrambles the order of the figures). (ii) The 2012 row comes from the 2013 edition (24.3% active; the 127,825 active accounts are the figure revised after six TPs resubmitted); 2012 online accounts (78,216) and 2011 (52,750) are on p6 of that edition. (iii) *Online share is own arithmetic (online / total accounts) for 2012-2020; 2021-2025 shares are as printed. (iv) "Implied active accounts" = published share x accounts (own arithmetic; the shares are rounded to 0.1 pp, i.e. an error of up to about +/-0.5%); the 2012-2013 values are stated by PSE. (v) The 2013 edition says its online data came from 14 TPs offering online trading; the number of TPs supplying online data rose to 38-39 by 2022-24 (35 in 2025), so the early online counts may be incomplete, and the jump in the active share between 2013 (23.9%) and 2014 (33.6%) may reflect a change in coverage or definition (I). (vi) The 2018 edition was reposted in a revised version in July 2020 per the PSE index [^pse-market-reports-index]; the 2022-2025 splits by investor type are on p3 of each edition.

- (P) **Foreign vs local share of transactions:** 2022 40.7% foreign / 59.3% local; 2023 43.9 / 56.1; 1H24 46.1 / 53.9 [^pse-asm-2024-presidents-report:6]; 2024 46.2 / 53.8; 2025 46.3 / 53.7; 1H25 48.3 / 51.7; 1H26 49.5 / 50.5 [^pse-asm-2026-president-report:7]. Half-year net foreign flows: 1H24 -31.12bn (full-year 2024 -23.19bn, i.e. net buying of +7.9bn in 2H24), 1H25 -41.07bn [^pse-asm-2025-presidents-report:7]. Earlier: 2015 47.9%, 2016 51.3%, 2017 50.3%, 2018 51.3%, 2019 55.4%, 2020 45.4% [^pse-asm-2021-presidents-report:5], 2021 36.0%, 2022 40.7%, 2023 43.9% (Table A); within the year the ratio was 32.6% in 1H21 [^pse-asm-2021-presidents-report:5], 32.8% in 7M21 and 42.4% in 7M22 [^pse-asm-2022-presidents-report:5], and 43.6% in 7M23 [^pse-asm-2023-presidents-report:7]. The Aug-2026 report gives YTD 48.3% vs 46.9% a year earlier, and 45.0% for August alone [^pse-monthly-report-2026-08:2]; the PSE weekly report gives 49.03% YTD at 2 Oct 2026 and 55.49% in the week of 28 Sep-2 Oct [^pse-weekly-report-2026-10-02:1].
- (I; data quirk) Summing PSE's own *daily* "Total Foreign" figures over a year gives a foreign ratio 2-3 pp higher than PSE's official annual figure (2025: 49.1% vs 46.3%; 2024: 48.8% vs 46.2%; 2023: 45.9% vs 43.9%; 2021: 37.1% vs 36.0%; 2026 YTD: 52.2% vs 49.03%), so the official YTD ratio is not the sum of the daily numbers (possible netting/exclusion of foreign-to-foreign crosses; PSE does not document this) [^pse-weekly-reports-dataset][^pse-weekly-report-2026-10-02:1].
- (P) **Net foreign flows (PHP bn):** 2013 +15.59; 2014 +55.45; 2015 -59.76; 2016 +2.80; 2017 +56.20; 2018 -61.01; 2019 -14.26; 2020 -128.57; 2021 -2.75; 2022 -68.05; 2023 -53.65; 2024 -23.19; 2025 -51.20 (Table A). Year-to-date marks: 2020 to 30 Oct -111.54bn [^pse-asm-2020-presidents-report:4]; 1H21 -77.76bn [^pse-asm-2021-presidents-report:5]; 7M21 -87.02bn and 7M22 -45.95bn [^pse-asm-2022-presidents-report:5]; 7M23 -6.55bn [^pse-asm-2023-presidents-report:7]. Monthly examples: Dec 2021 +84.88bn (single block/rotation), Dec 2025 -10.67bn after +6.38bn in Nov 2025 [^pse-monthly-report-2021-12:2][^pse-monthly-report-2025-12:2]. 2026: 1Q +12.14bn net buying, 1H -11.36bn, Aug -16.56bn, YTD at 2 Oct -31.5bn [^pse-infographic-1q26:1][^pse-infographic-2q26:1][^pse-monthly-report-2026-08:2][^pse-weekly-report-2026-10-02:1].
- (P) **Retail vs institutional share of value traded:** 2019 18.2% retail / 81.8% institutional; 2020 26.9 / 73.1; Jan-May 2021 38.9 / 61.1 [^pse-asm-2021-presidents-report:4]; full-year 2021 31.1 / 68.9, 7M21 36.8 / 63.2 and 7M22 21.2 / 78.8 [^pse-asm-2022-presidents-report:4]; 2022 20.1 / 79.9 and 7M23 20.4 / 79.6 [^pse-asm-2023-presidents-report:6]; 2023 18.4 / 81.6; 1H24 20.0 / 80.0 [^pse-asm-2024-presidents-report:6]; 2024 18.9 / 81.1; 1H25 17.9 / 82.1 [^pse-asm-2025-presidents-report:7]; 2025 18.2 / 81.8; 5M25 17.2 / 82.8; 5M26 19.1 / 80.9 [^pse-asm-2026-president-report:7]. The retail share therefore doubled from 18% (2019) to 39% in the first five months of 2021 (the pandemic account boom) and then fell back to ~20% from 2022, where it has stayed (17-20%) even though accounts have since more than doubled (Table B). The slides do not define the basis (presumably value traded), and no series earlier than 2019 was found (the 2015-2019 ASM slides checked have no retail/institutional chart in their text layers). In June 2025 PSE's CEO said retail contributes only "16 percent" of value turnover (S for the figure's basis; it is below the 18.9% in the ASM chart, definitions not given) [^pse-press-2025-06-09].
- (P) **Accounts (Stock Market Investor Profile):** 1,089,413 (2018); 1,228,038 (2019); 1,396,753 (2020) [^pse-asm-2025-presidents-report:13]; 1,620,017 (2021); 1,712,734 (2022); 1,906,019 (2023); 2,860,234 (2024, +50.1%, the highest growth since the series began in 2008); 3,641,067 (2025, +27.3%) [^pse-asm-2026-president-report:15][^pse-press-2025-06-09]. 2025: retail 3,611,157 (99.2%), institutional 29,910 (0.8%); local 3,608,358 (99.1%), foreign 32,709 (0.9%); online 3,226,616 = 88.6% of accounts (99.9% retail; 99.3% local) [^pse-investor-profile-2025:2]. Online accounts: 1,525,768 (2023, 80.0%); 2,471,860 (2024, 86.4%, +62%) [^pse-smip-2024:2].
- (P/I) **Account history and the online share (Table B).** Registered accounts grew from 525,850 (2012) to 868,810 (2017) and 1,396,753 (2020), then 3,641,067 (2025). (I; own arithmetic) They compounded at ~13% a year in 2012-20 and ~21% a year in 2020-25 (6.9x over 2012-25); the online share of accounts rose from ~15% (2012) and 22% (2013) to 45% (2017), 57% (2018), 67% (2020) and 89% (2025); and in 2018 online accounts rose by 236,899, more than the whole increase in total accounts (220,603), i.e. non-online accounts fell [^pse-investor-profile-2017:2][^pse-investor-profile-2018:2]. PSE's own chart gives the non-online accounts directly: 479,946 (2017), 463,650 (2018), 445,920 (2019), 460,553 (2020), 460,983 (2021) and 453,827 (2022) [^pse-asm-2023-presidents-report:10]; by subtraction (I) they were 447,634 (2012), 380,251 (2023), 388,374 (2024) and 414,451 (2025). Online accounts rose by 3.15m between 2012 and 2025, slightly more than the 3.12m rise in total accounts, so the entire growth of the account base is online: the offline base was flat at ~0.45-0.48m in 2012-22 and has been ~0.38-0.41m since 2023. The 2016-21 totals and online counts are repeated in PSE's ASM 2022 slides [^pse-asm-2022-presidents-report:8]. Retail accounts were 95.2% of the total in 2015 [^pse-investor-profile-2015:2], 97.5% in 2018 [^pse-investor-profile-2018:2] and 99.2% in 2025 [^pse-investor-profile-2025:2]; foreign accounts were 1.5% (8,917) in 2013 [^pse-investor-profile-2013:2] and 0.9% (32,709) in 2025 [^pse-investor-profile-2025:2]. The number of TPs reporting to the survey fell from 135 (2013-14) to 130 (2019-22), 123 (2023), 121 (2024) and 122 (2025).
- (P) **The account surge is e-wallet onboarding.** PSE says 89% of the >950k increase in accounts in 2024 was due to e-wallets [^pse-asm-2025-presidents-report:13]; the GCash-based GStocks PH (launched Aug 2023) had >1.7m registered users, Maya Stocks >15k, and PSE EASy (IPO subscription app for local small investors) >84k registered users as of March 2026 [^pse-analyst-briefing-3m-2026:21]. This is consistent with a small average online ticket (PHP 50.7k in 2024) and a low active-account share.
- (P) **Active accounts** (Table B). The total active share was 23.9% in 2013, 33-34% in 2014-17, 29.1% (2018), 25.2% (2019), 30.0% (2020) and 31.9% (2021), then 20.2% (2022), 17.6% (2023), 23.1% (2024) and 11.8% (2025), the lowest of the 14 years; for online accounts it was 43.4% (2013), 57-67% (2014-17), 34-42% (2018-21), 22.2% (2022), 19.3% (2023), 24.5% (2024) and 12.0% (2025) [^pse-investor-profile-2013:3][^pse-investor-profile-2013:6][^pse-investor-profile-2014:3][^pse-investor-profile-2015:3][^pse-investor-profile-2016:3][^pse-investor-profile-2017:3][^pse-investor-profile-2018:3][^pse-investor-profile-2019:3][^pse-investor-profile-2020:3][^pse-investor-profile-2021:3][^pse-smip-2022:3][^pse-smip-2023:3][^pse-smip-2024:3][^pse-investor-profile-2025:3]. By type in 2025 (retail 11.7%, institutional 14.6%, local 11.7%, foreign 20.4%) and 2024 (23.1 / 19.5 / 22.9 / 36.1%). Foreign accounts were more active than local ones in 2013 and 2022-2025 but less active in every edition from 2014 to 2021.
- (P) **Trade size:** in 2024 the average value of an online trade was PHP 50,746.82 (+7.9%) vs PHP 99,823.86 for non-online trades (+4.5%) [^pse-press-2025-06-09]. In 2022 the average online ticket was PHP 46,236.40, +33.2% from PHP 34,701.80 in 2021 [^pse-asm-2023-presidents-report:10]. (I) From PSE weekly reports: average value per trade (value/no. of trades) was PHP 87k (2019), 66k (2020), 78k (2021), 96k (2022), 108k (2023), 105k (2024), 105k (2025), 89k (2026 YTD); trades per day 81k, 112k, 116k, 76k, 57k, 58k, 70k, 86k [^pse-weekly-reports-dataset].
- (P) Investor demographics 2025 (retail accounts): aged 18-29 28.2%, 30-44 48.0%, 45-59 17.2%, 60+ 6.6% [^pse-investor-profile-2025:3]; annual income below PHP 500k 36.7%, PHP 500k-1m 53.9%, above PHP 1m 9.4% [^pse-investor-profile-2025:4]. The 2024 report instead had 82.4% of accounts under PHP 500k (the two surveys are not comparable: different numbers of reporting TPs) [^pse-smip-2024:4].
- (P) 121-122 trading participants are active; the OECD notes that "market making" is nominal (121 brokers are formally market makers but match orders and "do not trade on their own account or build inventories"; only about half are active) [^pse-infographic-fy24:1][^oecd-capital-market-review-philippines-2024:47].
- (P/I) **Short selling is effectively unused.** The PSE's Daily Short Selling Report (published since the 6 Nov 2023 launch; 53 eligible securities, 52 from late 2025, incl. the FMETF ETF) shows total short-sale volume 0 and value PHP 0.00, with short-interest ratios "NULL", on **every one of the 710 daily reports from 6 Nov 2023 to 5 Oct 2026** (own parse of all 710 PDFs listed in the PSE market-report index; first and last reports archived) [^pse-short-sell-report-2023-11-06:2][^pse-short-sell-report-2026-10-05:2][^pse-market-reports-index]. This is consistent with the OECD's remark that SBL/short selling "has yet to come into widespread use" [^oecd-capital-market-review-philippines-2024:13] and with the PSE's 2026 work to streamline MSLA clearance and simplify foreign-institution participation in SBL (revised SBL rules awaiting SEC approval) [^pse-asm-2026-president-report:22]. The PSE's index-futures project is still at the exposure-draft/RFI stage [^pse-asm-2026-president-report:24] and the OECD notes the Philippines is the only peer without a public derivatives market, with derivatives offered OTC by banks [^oecd-capital-market-review-philippines-2024:47].
- (P/I) **Broker concentration (Feb 2020, the only full report archived).** The top-25 brokers by value (buying plus selling) were Salisbury BKT PHP 25.27bn, UBS 25.16bn, CLSA 20.70bn, J.P. Morgan 20.17bn, Credit Suisse 15.56bn, Macquarie 13.73bn, COL Financial 13.46bn, BDO Securities 11.35bn, Maybank ATR Kim Eng 11.18bn and Wealth Securities 9.27bn [^pse-monthly-report-sample:21]. Against a two-sided total of 2 x PHP 132.56bn [^pse-monthly-report-sample:11] the top-5 brokers handled 40.3%, the top-10 62.6% and the top-25 89.8% of value (own arithmetic). The online retail broker COL Financial had the most trades (518,390; 16.2% of broker-side trades) but only 5.1% of value (average PHP 26k per trade, versus PHP 191-253k at UBS/Salisbury), i.e. value is institution/foreign-broker-led while trade counts are retail-led. Later broker rankings are only in the paid Monthly Report or the script-rendered PSE 'Broker Ranking' page.

### Inferences
- (I) The foreign activity ratio rose from ~36% (2021) to ~46-49% (2024-26) mainly because *local* turnover collapsed rather than because foreign turnover grew. Summing PSE's own daily series (own calculation): foreign buy+sell value was PHP 1.66tn (2021), 1.51tn (2022), 1.36tn (2023), 1.46tn (2024) and 1.75tn (2025), while local sides (2 x value traded minus foreign) fell from 2.81tn (2021) to 1.53tn (2024), -45%, before recovering to 1.81tn in 2025 [^pse-weekly-reports-dataset].
- (I; own arithmetic: published retail share x value traded in Table A, assuming the share refers to total value traded) Retail value traded was ~PHP 0.32tn (2019), 0.48tn (2020), 0.69tn (2021), 0.36tn (2022), 0.27tn (2023), 0.28tn (2024) and 0.32tn (2025), while institutional value (local and foreign institutions, including crosses) stayed within 1.2-1.5tn. About 56% of the 0.76tn fall in value traded between 2021 and 2023 was therefore retail: the 2021 volume peak was retail-led and its reversal explains much of the collapse in local turnover noted above [^pse-asm-2022-presidents-report:4][^pse-asm-2023-presidents-report:6].
- (I) The ~12% active-account rate in 2025 despite 3.6m accounts implies the retail "wave" is mostly dormant accounts; retail still only contributes ~18% of value, so volume growth is not retail-driven in 2025-26. Multiplying the published shares by the account totals (Table B, own arithmetic) gives ~0.14m active accounts in 2013 (stated), ~0.2-0.3m in 2014-19, ~0.42m (2020), ~0.52m (2021), ~0.35m (2022), ~0.34m (2023), ~0.66m (2024) and ~0.43m (2025): the number of accounts that trade at all has stayed within ~0.3-0.7m since 2020 while registered accounts rose 2.6x (1.40m to 3.64m). The editions differ in reporting-TP coverage and PSE does not document definitions, so the year-to-year changes are not a clean time series.
- (I) Because on-exchange short selling and listed derivatives are absent, price formation is driven by long-only flows and index events; there is no short-covering or hedging flow to dampen moves, and foreign funds must hedge via offshore/OTC instruments (not observable in PSE data).
- (I) Foreign share is highest on index-rebalance days (70-89% foreign activity) and lowest on domestic block days (3-20%), so intraday foreign participation is event-driven.

### Execution implications
- Foreign-heavy flow (46-49% of sides) means daily value is sensitive to EM fund flows and MSCI events; when foreign activity fades, value falls toward PHP 4-5bn a day (e.g. ADVT of PHP 3.96bn in Nov 2023 with ~zero net foreign flow [^pse-monthly-report-2023-12:1]).
- Retail is a small, fragmented liquidity source (average ticket PHP 50k online): do not expect retail flow to absorb institutional size at the open or close.
- Retail's share of turnover is regime-dependent (39% in Jan-May 2021, ~18% in 2023-25): do not assume a constant retail/institutional mix when estimating how much natural two-way flow is in the book, and re-check the published share when the market is retail-led.
- The absence of real market-makers means displayed depth is mostly broker-agency orders; plan for fewer standing quotes than the headline number of participants suggests.
- Plan on no usable on-exchange short capacity (zero reported short sales in 710 sessions) and no listed hedging instrument: strategies needing shorts or index hedges must be implemented through offshore or OTC instruments, and pairs/market-neutral execution cannot be done as a single on-exchange package.

### Gaps
- No public split of value by investor type beyond the ASM chart (retail/institutional, from 2019 only) and the foreign/local ratio; no institutional-local vs foreign-institutional split; no public share of *online* trades in value (only avg ticket sizes); no data on proprietary/HFT/algorithmic share (PSE rules on algorithmic trading were only consulted in Sep 2023 [^pse-cn-2023-0043:1]).

---

## 4. Liquidity and cost metrics (spreads, depth, price impact, tick constraints, trading costs)

### Takeaway
No public intraday spread/depth statistics exist for the PSE; the best primary proxy is the best bid/ask printed in the PSE Daily Quotation Report after the close. On 176 sampled days the *end-of-day* quoted spread was a median ~31 bp for the 10 most active names, ~35 bp for ranks 11-30, ~50 bp for ranks 31-60, ~87 bp for ranks 61-100 and ~227 bp beyond; 33-44% of liquid-name observations are exactly one tick wide, while the median is 2-3 ticks. All-in round-trip trading costs are the highest among ASEAN peers (OECD: buyer 0.30%, seller 0.90% = 1.2% vs 0.66% peer average), and fell by 0.5 pp for sellers when the stock transaction tax was cut from 0.6% to 0.1% on 1 July 2025.

### Cited Findings
- (P) **Tick/board-lot table in force Oct 2023 - Oct 2026** (price band -> tick, board lot): 0.0001-0.0099 -> 0.0001, 1,000,000; 0.01-0.049 -> 0.001, 100,000; 0.05-0.249 -> 0.001, 10,000; 0.25-0.495 -> 0.005, 10,000; 0.50-4.99 -> 0.01, 1,000; 5-9.99 -> 0.01, 100; 10-19.98 -> 0.02, 100; 20-49.95 -> 0.05, 100; 50-99.95 -> 0.05, 10; 100-199.9 -> 0.10, 10; 200-499.8 -> 0.20, 10; 500-999.5 -> 0.50, 10; 1,000-1,999 -> 1, 5; 2,000-4,998 -> 2, 5; >= 5,000 -> 5, 5 [^pse-cn-2023-0051:3][^pse-cn-2023-0051:4]; the same table is on the PSE investing page [^pse-investing-page]. A proposal to cut lot sizes to enable a PHP 100 minimum investment ("One Share, One Lot") is awaiting SEC approval, targeted for Q4 2026 with the new trading engine [^pse-cn-2023-0051:3][^pse-asm-2026-president-report:22].
- (I) **Relative tick size** implied by the table: ~4-10 bp of price for most index stocks (PHP 50-1,000 range), 10-25 bp for PHP 5-50 stocks, up to 200 bp at PHP 0.50 (tick PHP 0.01); the tick is a sawtooth in price, with the relative tick jumping at band edges (e.g. 0.1% at PHP 100, 0.05% at PHP 199.9).
- (I; own calculation from the Daily Quotation Reports; main-board stock-days with a trade) **Distribution of relative tick size (tick / closing price):** in the 176-day sample (42,347 stock-days) 0.6% of stock-days have a relative tick <5 bp, 18.5% 5-10 bp, 33.0% 10-25 bp, 13.0% 25-50 bp, 14.8% 50-100 bp and 20.0% >=100 bp; by *value* the shares are 1.4%, 47.6%, 41.0%, 4.9%, 3.1% and 2.0%. Median relative tick 22.7 bp; value-weighted 16.9 bp. In the 28-session 2026 panel 56.3% of value traded in names with a 5-10 bp tick and 31.6% in 10-25 bp names (value-weighted 13.1 bp) [^pse-dqr-dataset]. So almost half of traded issues (but only ~10% of value) have ticks >= 25 bp of price, i.e. are tick-constrained by construction (sub-PHP 10 stocks with a PHP 0.01 tick).
- (P/I) **A coarser tick table is proposed for the new engine.** PSE's 15 Dec 2025 consultation (CN 2025-0046; comments to 31 Dec 2025) proposes a "One Lot One Share" structure with the Nasdaq Eqlipse engine due in 2026: lot size 1 for all prices and a new tick table - up to PHP 0.099: 0.001; 0.10-0.995: 0.005; 1-9.99: 0.01; 10-99.95: 0.05; 100-199.9: 0.10; 200-499.8: 0.20; 500-999.5: 0.50; 1,000-1,999: 1; 2,000-4,998: 2; >=5,000: 5 - under which the tick for PHP 10-19.98 stocks rises from 0.02 to 0.05, brokers may set minimum order values, and the DDS tick/lot table is aligned [^pse-cn-2025-0046-board-lot-trading-at-last:3][^pse-cn-2025-0046-board-lot-trading-at-last:4]. As of the PSE's July 2026 presentation the board-lot amendment was still awaiting SEC approval with a Q4 2026 target [^pse-asm-2026-president-report:22]. (I; own calculation on the 28-session 2026 panel) if the table were adopted, 16.0% of traded stock-days (17.8% of regular-market value, e.g. ALI, SMPH, APX, PX, EMI, MYNLD, WEB, SCC, LTG, MREIT, all priced PHP 10-20) would face a 2.5x larger tick, the value-weighted relative tick would rise from 13.1 bp to 16.9 bp and the median from 24.1 bp to 32.5 bp [^pse-dqr-dataset]. For example ALI at PHP 15.14 would move from a 13 bp to a 33 bp tick.
- (I; own calculation, 176 sampled Daily Quotation Reports, Jun 2019 - Sep 2026; main-board stocks that traded that day with a two-sided close quote) **End-of-day quoted spread by turnover rank** [^pse-dqr-dataset]:

| Rank by day's value | n obs | median spread (bp) | IQR (bp) | median spread (ticks) | share at exactly 1 tick | share <= 2 ticks | median tick as bp of price | median day value (PHP m) |
|---|---|---|---|---|---|---|---|---|
| 1-10 | 1,758 | 30.9 | 14.8-64.6 | 3 | 33% | 47% | 8.9 | 252 |
| 11-30 | 3,517 | 35.2 | 16.6-75.4 | 2 | 41% | 54% | 12.5 | 66 |
| 31-60 | 5,275 | 50.4 | 23.4-99.4 | 2 | 44% | 60% | 16.7 | 14 |
| 61-100 | 7,036 | 86.6 | 39.5-160.4 | 2 | 42% | 57% | 25.0 | 3 |
| >100 | 24,717 | 227.3 | 111.9-449.4 | 5 | 20% | 33% | 41.2 | 0.4 |

  Sub-period medians for rank 1-10 were 32.2 bp (2019-22), 32.2 bp (2023-24) and 25.8 bp (Jan 2025-Sep 2026, median 2 ticks), i.e. a modest improvement in 2025-26. *Caveat:* the Daily Quotation Report does not define Bid/Ask [^pse-daily-quotation-report-file-spec-2016:1]; the values appear to be the residual book after the closing run-off, so they likely overstate intraday time-weighted spreads (e.g. BDO bid 110.4/ask 110.6 = 2 ticks, 18 bp; BPI 93.9/94.0 = 1 tick, 10.6 bp; ICT 860/862 = 4 ticks, 23 bp on 2 Oct 2026 [^pse-eod-daily-quotation-2026-10-02:1]).
- (I; own calculation, 28 consecutive sessions 26 Aug - 5 Oct 2026, [^pse-dqr-dataset]) **Amihud-type illiquidity** (median across stocks of the median daily |close-to-close return| in % per PHP 100m of that day's regular-market value; stocks ranked by average daily value): top-10: 0.56; ranks 11-30: 2.5; ranks 31-60: 5.8; ranks 61-100: 34; ranks >100: 464 (median average daily value PHP 287m / 70m / 21m / 2.8m / 0.1m). Interpretation: a PHP 100m day in a top-10 name is associated with ~0.6% absolute move, in a rank 61-100 name ~34%.
- (P) **Trading costs.** Per OECD (2024, before the 2025 tax cut): PSE fee 0.005% + 12% VAT, clearing 0.01%, SEC fee 0.005%, broker commission 0.05-1.5% (+12% VAT; the 1.5% minimum was removed by SEC MC 7-2024 of 16 Apr 2024 [^pse-cn-2024-0029-min-commission-removal:1]), seller-only stock transaction tax 0.6%; total buyer 0.30%, seller 0.90% of value, i.e. 1.2% round trip vs a 0.66% peer average and ~3x Indonesia/Singapore/Thailand on the sell side [^oecd-capital-market-review-philippines-2024:45][^oecd-capital-market-review-philippines-2024:46]. The Capital Markets Efficiency Promotion Act (RA 12214) cut the stock transaction tax (STT) from 0.6% to 0.1%: BIR Revenue Regulations 20-2025 (signed 29 Jul, received 5 Aug 2025) set the STT on shares listed and traded on a local exchange at 1/10 of 1% (0.1%) of the gross selling price effective 1 Jul 2025 [^bir-rr-20-2025-stt:2][^bir-rr-20-2025-stt:4]; the PSE confirmed the new rate applies to transactions from 1 Jul 2025 (RA 12214 was published on 4 Jun 2025) [^pse-cn-2025-0028-cmepa-effectivity:1], and its CEO had flagged the cut as "upcoming" in June 2025 [^pse-press-2025-06-09]. (I) With everything else unchanged the seller's cost falls from ~0.90% to ~0.40% and the round trip from ~1.2% to ~0.7%, i.e. about the OECD's 0.66% peer average (ignoring commission changes after the April 2024 removal of the 1.5% minimum).
- (P) **Market making.** 121 brokers are nominal market makers; they "do not trade on their own account"; no incentives for market makers exist; the market-making article of the Revised Trading Rules was still pending SEC approval as of June 2024 [^oecd-capital-market-review-philippines-2024:47]; in 2026 the PSE released amendments to the market-making rules to include a GPDR framework, to be extended later to individual stocks [^pse-asm-2026-president-report:23][^pse-infographic-2q26:1].
- (P) The OECD concluded that the Philippines has "markedly lower liquidity than peer countries", attributing it to low free float, high trading costs (esp. sell-side tax), limited research and no market makers; short selling/SBL launched in 2023 has "yet to come into widespread use" [^oecd-capital-market-review-philippines-2024:13][^oecd-capital-market-review-philippines-2024:48]. PSE launched short selling in 2023 [^pse-infographic-fy23:1].
- (P) Average value of regular-market trades in Feb 2020: PHP 70.3k per trade regular; PHP 2.98m per block/odd-lot print (5.90bn / 83,911 trades; 1.0787bn / 362 trades per day) [^pse-monthly-report-sample:11].
- (P) Block-sale rules in the archived Implementing Guidelines: regular block sale >= PHP 20m, price within +-5% of the last adjusted closing price (undated version) [^pse-implementing-guidelines-trading-rules:23].

### Inferences
- (I) Because 33-44% of liquid-name spreads equal one tick and the relative tick is 5-25 bp, a large fraction of PSE stocks are *tick-constrained* (spread cannot go below ~1 tick); queue priority (price-time) matters more than price improvement.
- (I) Spread-cost per share is small relative to explicit costs: the 0.1% STT (post-2025) + ~0.05-0.25% commission + ~0.02% exchange/clearing dominates the 5-30 bp spread for the top 30 names; pre-2025 the 0.6% sell-side STT dwarfed everything.
- (I) The ~5 ticks median spread beyond rank 100 means ~2-4% round-trip cost for tail names.

### Execution implications
- Treat quoted half-spread as ~5-15 bp for top-10 names and 15-50 bp for ranks 11-60; budget 25-60 bp one-way for ranks 61-100 and >100 bp for the tail, on top of fees.
- Estimated impact scale: ~0.5-2.5% daily |move| per PHP 100m in the top-30 names argues for conservative participation caps and for using the block facility for >PHP 20m prints when a counterparty exists (a judgement, not taken from a cited study; e.g. <=10% of regular-market ADV and <=20% of the volume of any single auction or 5-minute window).
- Regime change: if the Dec-2025 tick proposal is adopted with the new engine (go-live 23 Nov 2026), ALI, SMPH, APX, PX, EMI and other PHP 10-20 names (~18% of value) get a 0.05 tick (25-50 bp of price): expect wider quoted spreads, deeper queues at each price and more reliance on the closing call; re-measure spreads and queue priority behaviour immediately after the change.
- Tick-constrained queues: joining the best bid/ask early matters; pennying is limited by the discrete tick, so "inside-spread" quoting is possible only where spread >= 2 ticks (about 55-65% of liquid names at the close).

### Gaps
- No PSE or academic estimate of *effective* spreads, depth at best/top-5 levels, quoted spread time series, or price impact curves was found; my numbers are end-of-day book proxies. Intraday ITCH data (PSE ITCH spec archived by others) would be needed.
- Post-July-2025 all-in costs are my arithmetic from the OECD cost table and the BIR rate; no published post-reform comparison with peers was found.

---

## 5. Intraday structure, closing auction, end-of-day behaviour, calendar effects

### Takeaway
PSE trades 09:30-12:00 and 13:00-14:45 continuous, with a 5-minute pre-close call (14:45-14:50; orders can be cancelled until 14:48, entered but not cancelled 14:48-14:50), a 10-minute run-off at the closing price (14:50-15:00) and, since 2024, a 15-minute "Closing VWAP session" (15:00-15:15) that is almost unused (0.05-0.11% of value). There is no public intraday volume profile; I found no PSE statistic on the closing auction's share of volume. Daily price data show a *negative* last-trading-day-of-month return (mean -0.52%) and positive first-three-day returns, contradicting the "month-end window dressing rally" narrative of local market reports.

### Cited Findings
- (P) **Session schedule history.** June 2010: pre-close (3 min) introduced with PSEtrade; 2012: trading extended to 15:30 (4h30 vs 2h40) [^pse-memo-extended-pre-close-consultation-2013:1]. 4 Nov 2013: pre-close lengthened to 15:15-15:20 (auction 15:15-15:18, no-cancel 15:18-15:20), run-off 15:20-15:30, close 15:30; rationale given by PSE: (i) PSE had the shortest pre-close in the region (Bursa Malaysia 5 min, SGX 6, SET 10, IDX 10, HoSE 15), (ii) to let TPs "assess and counter a sharp price move at the close", (iii) ETFs and index funds are benchmarked to closing prices so baskets need more time to execute [^pse-memo-extended-pre-close-consultation-2013:1][^pse-memo-extended-pre-close-consultation-2013:2][^pse-memo-extended-pre-close-implementation-2013:1][^pse-memo-pre-close-schedule-2013:1][^pse-annual-report-2013:28]. 2015-2016 schedule: 09:00 pre-open, 09:15 no-cancel, 09:30 open, 12:00 recess, 13:30 resume, 15:15 pre-close, 15:18 no-cancel, 15:20 run-off, 15:30 close [^pse-annual-report-2015:10][^pse-annual-report-2016:10].
- (P) **Origins of the midday recess (2011-2012).** Until 30 Sep 2011 the PSE traded only in the morning (open 09:30, pre-close 11:57, run-off 12:00, close 12:10, i.e. about 2h40 of trading); the Board approved on 13 Jul 2011 a two-phase extension: from 1 Oct 2011 trading until 13:00, and from 2 Jan 2012 a two-session day, 09:30-12:00 and 13:30-15:30 (pre-close 15:17, run-off 15:20, close 15:30, i.e. 4h30), with end-of-day files due at 12:45 (morning session), 16:15 (full day) and the website Daily Quotation Report at 17:00 [^pse-memo-extended-trading-proposal-2011:1][^pse-memo-new-trading-hours-2011:1]. The recess therefore dates only from 2012, and the 2021-24 schedule moved the afternoon session to 13:00 (see below).
- (P) **COVID-era changes.** 16 Mar 2020 shortened hours (close 13:00 with pre-close 12:45, run-off 12:50); the same notice scheduled an 08:30 pre-open/09:00 open to 13:00 for 17 Mar-14 Apr [^pse-cn-2020-0017:1], but trading was suspended from 17 Mar 2020 "until further notice" [^pse-cn-2020-0021:1] and resumed on 19 Mar on a 09:30-13:00 schedule [^bw-284527]; shortened hours (09:30-13:00, pre-close 12:45, run-off 12:50) were extended to 30 Apr, 15 May and, under the modified ECQ, until further notice (trading floor closed, trading done remotely) [^pse-cn-2020-0035:1][^pse-cn-2020-0042:1][^pse-cn-2020-0046:1]; shortened again 14-31 Jan 2022 (Omicron) [^pse-cn-2022-0004:1]; on 6 Dec 2021 PSE "went back to its pre-pandemic" full-day schedule of 09:00 pre-open, 09:30 open, 12:00-13:00 recess, 14:45 pre-close, 14:50 run-off, 15:00 close [^pse-cn-2021-0059:1]; half-day sessions (open 09:30, pre-close 11:55, run-off 12:00, close 12:10) apply on 24 and 31 December [^pse-cn-2021-0063-half-day-trading-2021-12:1]; after the 14-31 Jan 2022 Omicron cut, the full-day schedule resumed on 1 Mar 2022 (CN 2022-0009, the circular cited by the PSE infographics) [^pse-cn-2022-0009-trading-schedule-mar-2022:1].
- (P) **Current schedule (SEC-approved 1 Feb 2024, CN 2024-0010):** pre-open 09:00; pre-open no-cancel 09:15; open 09:30; recess 12:00; resume 13:00; pre-close 14:45; pre-close no-cancel 14:48; run-off/trading-at-last 14:50; Closing VWAP session 15:00; market close 15:15. Run-off: orders only at the closing price. VWAP session: trades only at the VWAP of the day (all trades except block sales, intentional crosses and odd lots), value >= PHP 500,000, single trading participant, reported in the end-of-day report [^pse-approved-rules-vwap-trading-2024:3][^pse-approved-rules-vwap-trading-2024:5][^pse-approved-rules-vwap-trading-2024:6][^pse-approved-rules-vwap-trading-2024:7]; matches the live PSE page [^pse-investing-page]. VWAP trading went live on 1 Mar 2024 [^pse-cn-2024-0012-vwap-go-live:1]. The PSE infographics still describe "9:30AM to 3:00PM" and cite CN 2022-0009, i.e. they omit the 15:00-15:15 VWAP session [^pse-infographic-fy25:1].
- (P) **Closing price mechanics.** The pre-close works like the pre-open call (maximum matched volume; reference price for the closing calculation = last traded price) and the run-off is "trading-at-last" at that price [^pse-implementing-guidelines-trading-rules:4][^pse-implementing-guidelines-trading-rules:12][^pse-implementing-guidelines-trading-rules:16]. Odd-lot closing price = last traded price [^pse-implementing-guidelines-trading-rules:20].
- (P) **A run-off limitation in the current engine and its planned removal.** In the run-off/trading-at-last period the current PSEtrade XTS *rejects* an incoming order if a counterpart passive order in the book is priced better than the closing price (e.g. closing price 10.00, resting sell at 9.00: an incoming buy at 10.00 is refused), so such resting orders cannot be hit at the close; the Nasdaq Eqlipse engine would accept the incoming order and match it with the better-priced passive order *at the closing price* (price improvement to the incoming side, no loss to the resting side relative to its limit). PSE proposed on 15 Dec 2025 to amend Article IV Section 18 accordingly, with the run-off allowing orders to be entered, modified and executed only at the closing price [^pse-cn-2025-0046-board-lot-trading-at-last:5][^pse-cn-2025-0046-board-lot-trading-at-last:6][^pse-cn-2025-0046-board-lot-trading-at-last:8]. Implication: today's run-off liquidity is structurally thinner than the book suggests, and should expand after the engine change.
- (I; 28 sessions + 176 sampled days) **VWAP-session usage:** 6 of the 28 sessions Aug 26 - Oct 5, 2026 had any VWAP trade; examples: 2 Oct 2026 one print of 3,750 GLO shares = PHP 7.29m (0.09% of the day's PHP 8.18bn) [^pse-eod-daily-quotation-2026-10-02:11]; 17 Sep 2026 75,000 shares = PHP 4.35m [^pse-eod-daily-quotation-2026-09-17:11]; 28 Aug 2026 168,000 shares = PHP 2.29m [^pse-dqr-2026-08-28:11]. In the 176-day sample VWAP value was 0.054% (2024), 0.092% (2025), 0.113% (2026) of total value; odd-lots <= 0.015% [^pse-dqr-dataset].
- (P) **Intraday value is not published**; the PSE Weekly Report gives only daily OHLC for the PSEi, total value, number of trades and foreign activity (e.g. week of 28 Sep-2 Oct 2026: daily value PHP 5.19/5.39/9.10/7.54/8.18bn on 85k/83k/101k/90k/76k trades) [^pse-weekly-report-2026-10-02:1].
- (S) **"Window dressing" in local market commentary.** BusinessWorld reports month-end rallies attributed to window dressing (e.g. "PSEi rallies by 0.71% on 'window dressing'", 30 Jun 2017 [^bw-14232]; "PSEi rebounds on month-end window dressing", 27 Jun 2019 [^bw-238977]; "Shares up on window dressing, increased buying", 28 Sep 2023 [^bw-548526]) but also "PSEi drops further on month-end window dressing" on 31 May 2023, an MSCI rebalance day [^bw-526114]. Local desks use the term for the last 1-3 sessions of a month or quarter.
- (I; own calculation, daily PSEi closes from the PSE Weekly Reports, 29 Apr 2019 - 2 Oct 2026, n=1,808 returns [^pse-weekly-reports-dataset]) **Turn-of-month pattern:** last trading day of the month: mean -0.52% (t = -3.3; median -0.64%; only 34% of 89 months positive); first trading day of the month +0.34% (t=2.5); 2nd +0.31% (t=2.4); 3rd +0.23% (t=1.9); other days -0.045% (t=-1.4). Last day of quarter -0.51% (t=-2.0; n=30). Robustness: it is *not* an MSCI artefact - in months whose last session is an MSCI review day (Feb/May/Aug/Nov, n=30) the mean is -0.18% (t=-0.7), whereas in the other 59 months it is -0.70% (t=-3.6, median -0.68%, 68% negative); it appears in both halves of the sample (2019-22: -0.47%, n=44; 2023-26: -0.58%, n=45); excluding Feb-Jun 2020 it is -0.66% (t=-4.6); a permutation test against randomly drawn days gives p=0.0004; the first three sessions of a month average +0.29% (t=4.0, 63% positive, n=267). Caveats: a short sample (89 months) over which the index fell ~30%, daily returns are fat-tailed, and no cross-check against other markets was done; treat as indicative.
- (I; same data) **Day of week** (all days, excl. 15 Feb-30 Jun 2020 in brackets): Mon -0.116% (-0.055), Tue +0.138% (+0.097; t=2.4), Wed +0.048% (+0.032), Thu -0.050% (-0.005), Fri -0.118% (-0.124; t=-2.05). Average value traded by weekday (PHP bn): Mon 6.4, Tue 7.3, Wed 7.3, Thu 7.1, Fri 8.1 (Fridays include many MSCI/month-end days). Intraday decomposition: Friday open-to-close -0.15% vs overnight +0.03%.
- (I; same data) **Month of year:** average daily value (PHP bn): Jan 7.1, Feb 8.2, Mar 8.0, Apr 6.1, May 7.7, Jun 7.1, Jul 6.0, Aug 7.3, Sep 7.3, Oct 6.8, Nov 7.7, Dec 8.5; April and July are the thinnest months.
- (I; same data) **Opening gaps and ranges:** mean |open - previous close| for the PSEi 1.0-1.4% of price over 2019-2026 (2020: 1.8%), and mean high-low range 1.1% (2019), 1.8% (2020), 1.3%, 1.4%, 1.0%, 1.1%, 1.2%, 1.2% (2026). Overnight (close-to-open) mean +0.024% vs open-to-close mean -0.043% per day.
- (I; same data, n=1,813 sessions) **The PSEi closes at an extreme of its daily range far more often than a random walk would imply.** Close = day's high on 21.3% of sessions (30.3% in 2019, 28.5% 2020, 25.0% 2021, 26.9% 2022, 21.1% 2023, 15.1% 2024, 12.8% 2025, 11.8% 2026 YTD) and close = day's low on 16.8% (15.2, 13.8, 13.7, 15.5, 19.8, 20.4, 16.9, 19.4%); the close falls in the top decile of the day's range on 28.4% and in the bottom decile on 23.1% of sessions (benchmark for a Gaussian random walk with 200-5,000 steps: close = high 0.6-4.0%; top/bottom decile 13.3-14.4% each). The open is also at the day's high on 17.0% and at the low on 10.1% of sessions. Mean |close-open| / (high-low) is 0.54-0.61 by year (benchmark 0.47), and 22-32% of sessions are "trend days" with |close-open| >= 80% of the range (benchmark 13%) [^pse-weekly-reports-dataset]. The bias flipped from "close at high" (2019-22, rising/range-bound market) to "close at low" (2023-26, drifting market), so the extremes track the prevailing drift rather than a fixed closing-auction premium; but the sheer frequency says that the final auction print (pre-close call + run-off) very often *sets* the day's high or low.
- (I; own calculation, 176 sampled Daily Quotation Reports, ranks 1-100 by value, 17,600 stock-days) **Individual stocks also open and close at the day's extreme far more often than a tick-discretised random walk implies, most of all in the liquid names.** Close = day's high / day's low: ranks 1-10 13.2% / 14.7% (random-walk benchmark about 2.7% each); ranks 11-30 13.9% / 13.6% (4.4%); 31-60 15.0% / 15.0% (7.7%); 61-100 20.6% / 19.4% (12.7%). Open = day's high / low: 14.8% / 11.0% (ranks 1-10), 18.1% / 14.3% (11-30), 24.0% / 16.6% (31-60), 31.8% / 20.8% (61-100). The benchmark is a driftless Brownian motion whose expected high-low range equals each stock-day's observed range in ticks (mean range 35.6, 25.7, 18.1 and 13.4 ticks by tier); the probability that the close lies within half a tick of the maximum is 2*Phi(0.5*1.596/R)-1. The excess ratio falls from about 5x (top-10) to 1.6x (ranks 61-100) [^pse-dqr-dataset]. Interpretation: the opening call and the closing call/run-off print at a day's high or low about five times more often than chance in the most liquid names, i.e. auction prices carry a discrete jump relative to the continuous-trading path (imbalance-driven), consistent with the sell-side description of index flows concentrating in the closing auction.
- (I; own calculation, 164 Daily Quotation Reports for the last three and first two sessions of each month, Jan 2024 - Sep 2026, top-100 stocks by value) **Month-end closing dislocation, but no systematic mark-up.** On the last session of the month (T-0, 33 months) top-100 stocks close at the day's high on 21.6% and at the day's low on 22.2% of stock-days (43.8% in total), versus 16.7% / 17.3% (34.0%) on baseline mid-month days and 32-36% on T-2, T-1, T+1 and T+2 (tick-discretised random-walk expectation about 9% each side); the last day of a quarter shows 24.1% / 19.2%. The mean position of the close within the day's range is 0.498 on T-0 (baseline 0.493), i.e. there is no upward bias, and the equal-weighted return of stocks trading >= PHP 10m was +0.10% on the last day (+0.11% on T-1; n=1,601) while the PSEi fell on average ~0.5% on those days [^pse-dqr-dataset][^pse-weekly-reports-dataset]. So the month-end close is *noisier* (consistent with index/benchmark and portfolio-rebalancing flows at the close) but there is no evidence in these data of a broad "marking the close" bias; the month-end weakness is concentrated in the large, index-weighted names.
- (I; same data) **Variance decomposition:** overnight (previous close to open) variance is only 8-16% of close-to-close variance in 2019, 2021-2025 (13%, 9%, 14%, 8%, 9%, 16%), but 39% in 2020 and 25% in 2026 YTD; open-to-close accounts for 57-86%. Parkinson (range-based) volatility is 0.70-0.80 of close-to-close volatility. Daily return autocorrelation is ~0 (lag-1 -0.019, lag-2 -0.046), the weekly variance ratio VR(5) is 1.17 [^pse-weekly-reports-dataset]. Camba & Camba (2020) likewise fail to reject a random walk in PSE index data (see s.8).
- (S) **Late-session moves are a staple of local market reports** (headline-level evidence): "PSEi falls to near 7-month low after late selloff" (16 Jan 2025: "despite trading higher for most of the session") [^bw-647194]; "Philippine stocks rebound on last-minute buying" (10 Dec 2024) [^bw-640643]; "PSEi loses steam before close on profit taking" (10 Sep 2024) [^bw-620502]; "last-minute selling trimmed gains" (12 Oct 2023) [^bw-551311]; "PSEi pares early losses to end flat before Fed, BSP" (16 Dec 2024) [^bw-641856].
- (S) **Index-rebalance flows concentrate in the closing auction.** After the MSCI May 2026 review (effective at the close of 29 May 2026; JFC removed from the MSCI Philippines Standard Index) a Globalinks sales trader told BusinessWorld "forced selling is typically concentrated in the closing auction of the rebalancing date, which explains the unusually heavy volumes", and a First Resources trader said the index "was down the whole day due to the rebalancing" [^bw-753259]. A China Bank Capital MD said on 30 May 2023 that foreign institutions were rebalancing ahead of MSCI effectivity and anticipated "a potentially volatile session ... on the back of last-minute window dressing" the next day [^bw-525845].
- (P) Foreign index flows concentrate at the close: e.g. 31 May 2023 (MSCI semi-annual review effective): total value PHP 24.5bn (5.3x the trailing 20-day median), foreign activity 81.3%, net foreign selling PHP 4.15bn; 100,324 trades [^pse-weekly-report-2023-06-02:1].

### Inferences
- (I) Because the VWAP session is effectively unused (<0.12% of value) it should not be counted on as a liquidity pool: price-taking at the "day VWAP" is available only if a counterparty with >= PHP 500k also wants it, and one TP must stand on both sides.
- (I) The close structure (5-minute pre-close call, then a 10-minute trading-at-last run-off) means a closing-auction order can be placed late (modifiable until 14:48; enter-only until 14:50) and re-hedged against the run-off; passive index funds benchmark to this close (PSE's own 2013 rationale), so closing-auction participation is the natural MOC/benchmark venue, but I found no data on its volume share.
- (I) A negative month-end drift together with MSCI days and foreign selling suggests that index/benchmark flows rather than domestic fund "window dressing" dominate month-end price formation in 2019-2026; the narrative should be treated as a headline cliche rather than an exploitable signal.

### Execution implications
- Month-end sessions have ~30% more closing-extreme prints than ordinary days (43.8% vs 34.0% of top-100 stock-days): widen auction-participation tolerance and avoid leaving a large unfilled balance for the closing call on the last session of a month or quarter.
- Auction price risk: in the 10 most liquid names the close (or open) equals the day's high or low on ~28% (~26%) of sessions versus ~5% expected by chance, so a passive limit order resting into the closing call can be run over by an imbalance print; size closing-auction participation conservatively and prefer the run-off (trading-at-last at the already-determined closing price) for the residual.
- Schedule: the continuous session has two halves separated by a 1-hour recess; no public U-shape evidence exists, so calibrate the intraday volume curve from your own ITCH/Level-1 capture. Pre-open (09:00-09:30) and pre-close (14:45-14:50) are auctions: use limit-at-close for benchmark-to-close mandates.
- On MSCI review days (effective at the close of the last business day of Feb/May/Aug/Nov in 2023-2026, see s.7) expect 3-6x normal value, 70-90% foreign sides and heavy closing-auction/block volume: schedule around them, or trade into the closing auction deliberately with a pre-agreed share of the print. Other index providers' dates (FTSE, S&P) were not examined.
- The last-session-of-month drift (mean -0.5%, t about -3, 2019-2026) and the rebound in the first three sessions are in-sample facts on a short, down-trending sample; treat them as a timing prior (e.g. avoid scheduling large buys into the last session) and test on your own data before relying on them.

### Gaps
- No public data on the *share of daily volume in pre-open, continuous, pre-close/run-off, VWAP session*; no lunch-break or intraday U-shape study for the PSE found. The 2013 consultation does not quantify closing volume. The date on which the close moved from 15:30 (2013-2017 reports) to 15:00 (called "pre-pandemic" in CN 2021-0059) was not established from the sources read.

---

## 6. Volatility, price limits and circuit breakers

### Takeaway
PSEi daily-return volatility is moderate: close-to-close annualised 14-21% in normal years (2019 14.6%, 2021 18.7%, 2022 20.7%, 2023 14.3%, 2024 15.5%, 2025 16.9%, 2026 YTD 18.2%) with a 33.9% spike in 2020. Daily moves >= 5% occurred only in 2020 (8 days) and twice in 2026 (-5.0% on 9 Mar and +6.1% on 15 Jun). Single-stock moves >= 10% affect ~2% of stock-days (~4 stocks a day), >= 30% ~0.2% of stock-days; the +50% static threshold was reached once in 28 sessions.

### Cited Findings
- (I; own calculation from daily PSEi closes, PSE Weekly Reports [^pse-weekly-reports-dataset]) **Annual realised volatility and tail days:**

| Year | N returns | Ann. vol (close-close) | mean abs ret | days with abs(r) >= 2% | >=3% | >=5% | worst day | best day |
|---|---|---|---|---|---|---|---|---|
| 2019 (from 29 Apr) | 164 | 14.6% | 0.71% | 6 | 0 | 0 | -3.00% | +2.71% |
| 2020 | 238 | 33.9% | 1.36% | 47 | 19 | 8 | -14.32% (log) | +7.17% |
| 2021 | 247 | 18.7% | 0.89% | 18 | 9 | 0 | -3.67% | +4.98% |
| 2022 | 245 | 20.7% | 1.01% | 26 | 9 | 0 | -4.35% | +3.54% |
| 2023 | 241 | 14.3% | 0.71% | 6 | 1 | 0 | -2.58% | +3.51% |
| 2024 | 245 | 15.5% | 0.78% | 11 | 0 | 0 | -2.98% | +2.50% |
| 2025 | 242 | 16.9% | 0.80% | 13 | 6 | 0 | -4.39% | +3.44% |
| 2026 (to 2 Oct) | 186 | 18.2% | 0.86% | 12 | 2 | 2 | -5.10% | +5.96% |

  Full-sample annualised vol 20.2%. Ten worst days (simple returns): 2020-03-19 -13.34% (first session after the 17-18 Mar closure), 2020-03-12 -9.71%, 2020-03-16 -7.91%, 2020-04-16 -7.07%, 2020-03-09 -6.76%, 2026-03-09 -4.97%, 2020-06-15 -4.82%, 2025-04-07 -4.30%, 2022-03-08 -4.26%, 2022-03-14 -4.15%. Best: 2020-03-26 +7.44%, 2026-06-15 +6.14%, 2020-03-25 +5.31%, 2020-11-10 +5.23%, 2021-05-27 +5.11%.
- (I) **Intraday range:** mean (high-low)/open for the PSEi was 1.08% (2019), 1.82% (2020), 1.31% (2021), 1.38% (2022), 1.03% (2023), 1.13% (2024), 1.19% (2025), 1.23% (2026) [^pse-weekly-reports-dataset].
- (I; 28 consecutive sessions, [^pse-dqr-dataset]) **Single-stock moves** (close vs previous close, stock-days with trades on both days, n=6,060): |ret| >= 5%: 8.4%; >= 10%: 1.96% (119; avg 4.4 stocks/day); >= 15%: 0.81%; >= 20%: 0.40% (24; 0.9 stocks/day); >= 30%: 0.20% (12); >= 50%: 0.02% (1). Extreme movers in the window were illiquid names (e.g. SRDC +50%, +48%, +34% on PHP 0-1m of value; ABG -30% and -23% on PHP 26-31m).
- (P/I) **A static-limit example.** Asiabest Group (ABG) closed at PHP 42.60 on 30 Sep 2026, exactly -30.0% from the previous close of 60.85 (0.7 x 60.85 = 42.595), i.e. at the lower static threshold with *no bid* in the Daily Quotation Report (bid "-", ask 42.60; open 60.00, high 60.85, low = close 42.60; 545k shares, PHP 25.8m) [^pse-eod-daily-quotation-2026-09-30:3]. The surrounding sessions in the same data: +15.6% on 28 Sep (intraday high 76.65), -16.4% on 29 Sep, -22.5% on 1 Oct, -15.5% on 2 Oct (close 27.90; -61.7% in four sessions), +11.1% on 5 Oct, on PHP 10-74m daily value [^pse-dqr-dataset]. SRDC (Supercity Realty) moved +48.3%, +12.8%, +33.6% and +31.9% on days when only PHP 0.1-1.2m traded. No source read explains these moves; they are noted only as live examples of threshold and thin-book behaviour.
- (P) **Static and dynamic thresholds.** Original static threshold +-50% of previous close or last adjusted closing price [^pse-implementing-guidelines-trading-rules:10]; on 21 Mar 2020 (SEC-approved) the *lower* static threshold was cut to 30% below the reference price, upper kept at +50% [^pse-cn-2020-0028:1]. The PSE website still describes a symmetric 50% band and dynamic thresholds of 10%, 15% or 20% depending on trade frequency [^pse-investing-page]. Reaching the static limit freezes the stock unless an announcement justifies the move.
- (P) **Static bands are re-based or lifted ad hoc.** The band is set from the last traded price, so after a long suspension it can be stale: on the follow-on listing dates of Synergy Grid (SGP, 10 Nov 2021) and Keepers Holdings (KEEPR, 19 Nov 2021) the PSE lifted the *lower* static threshold because the bookbuilt prices (PHP 12.00 and PHP 1.50) were below the band implied by the last trade before the suspensions of 31 May and 8 Jul 2021, keeping the upper threshold [^pse-cn-2021-0055-lift-lower-static-threshold-sgp:1][^pse-cn-2021-0057-keepr-lower-static-threshold-lift:1].
- (P) **Market-wide circuit breakers.** Old rule: automatic 15-minute halt of the whole market if the PSEi declines >= 10% (an offshoot of the 2008 crisis); replaced from 4 May 2020 by a three-phase system: PSEi declines of 10%, 15%, 20% trigger halts of 15, 30 and 60 minutes [^pse-cn-2020-0044:1]. The 10% breaker was actually triggered on 12 Mar 2020 (intraday -10.33%; -9.71% close) and again at the open on 19 Mar 2020 [^bw-283531][^bw-284527]; BusinessWorld says the previous use was in October 2008 [^bw-283531].
- (P) PSE's own November-2020 summary of its pandemic measures lists the temporary shortened hours (09:30 open to 13:00 close), the three-level market-wide circuit breaker (PSEi falls of 10%, 15% and 20% giving 15-, 30- and 60-minute halts), the cut of the *lower* static threshold from 50% to 30% (upper threshold kept at 50%) and floorless trading (the IATF allowed PSE to reopen during the ECQ on condition that the trading floor stayed closed and only a skeletal workforce operated; the slide refers to a reopening in June 2020) [^pse-asm-2020-presidents-report:5].
- (P) **Trading suspensions as an event type:** the two-session closure of 17-18 Mar 2020 (trading resumed 19 Mar; March 2020 therefore had 20 trading days) [^pse-cn-2020-0021:1][^pse-monthly-report-2020-03:1][^bw-284527]. In the 20-day March 2020 month ADVT was PHP 6.96bn (non-regular only 0.44bn) and the PSEi traded 4,623.42-6,884.77 [^pse-monthly-report-2020-03:1].

### Inferences
- (I) A 15-20% annualised vol for the benchmark corresponds to a ~1.0-1.3% daily 1-sigma and a 1.1-1.4% average daily range; position-risk systems should be calibrated to 2022-2026 (17-20% annualised) rather than the calm 2023-24 window.
- (I) The +50%/-30% static bands are wide relative to ordinary single-stock moves (only ~0.2% of stock-days move >= 30%), so they bind only in extreme episodes (the ABG floor on 30 Sep 2026); the practical protection against runaway prices is the dynamic threshold and PSE/CMIC suspensions, for which no statistics are published.

### Execution implications
- Use a volatility-scaled slice size. Order of magnitude from the Amihud-type estimates in s.4 (linear scaling, judgement): a PHP 5m child order corresponds to ~0.03% of absolute daily move in top-10 names but ~0.3% in ranks 31-60 and >1.5% in ranks 61-100, against a typical PSEi range of ~1.2% a day.
- Circuit-breaker rules (10/15/20% market-wide, 15/30/60 min) mean orders in the book at the time of a halt are frozen; build order-state recovery for halts and for the new trading engine cut-over (see s.7).

### Gaps
- No public count of static/dynamic-threshold freezes or of market-wide halts (other than 12 Mar 2020 reported by Philstar) found; PSE does not publish surveillance statistics.
- Intraday realised volatility (5-min) and variance ratios cannot be computed from public PSE data; the DLSU papers below use daily/monthly data only.

---

## 7. Notable episodes

### Takeaway
Seven recurring episode types move PSE microstructure: (1) taper/EM outflow shocks (2013), (2) pandemic closure and crash/reopening (Mar 2020), (3) MSCI/FTSE rebalance days (4-6x normal value), (4) block-sale-dominated days (total value PHP 20-116bn), (5) technical outages (Jan 2022, Jan 2024, Mar 2025), (6) manipulation/pump-and-dump cases (Villar Land 2025; BW Resources, Calata historically) and (7) the Sep-Oct 2026 sell-off.

### Cited Findings
- (P) **2013 taper tantrum:** record close 7,392.20 on 15 May 2013 (intraday 7,403.65; +27.4% YTD at the time; 31 record highs that year) [^pse-annual-report-2013:6][^pse-annual-report-2013:11]; the Fed's tapering signals then "derailed" the rally and "concerns over the taper talk dragged on", pulling the PSEi to its 2013 closing low of 5,738.06 on 28 Aug 2013 (-22.4% from the May peak); the Fed announced the first US$10bn QE reduction in December (effective Jan 2014); the PSEi still ended 2013 up 1.3% at 5,889.83 and the peso weakened 7.8% to PHP 44.41/USD [^pse-annual-report-2013:12]. Foreign activity was 51.1% of trades and full-year net foreign buying was +15.59bn, down 85.8% from the record +109.98bn of 2012 (so the foreign pull-back was a flow *slowdown* rather than a full-year net exit) [^pse-annual-report-2013:12][^pse-annual-report-2017:17]. ADVT in 2013 was PHP 10.52bn, the highest of 2013-2025 [^pse-annual-report-2017:17]. In 2014 trading dipped early in the year on Fed-tapering worries and China's slowdown [^pse-annual-report-2014:59], and the PSEi peaked at 7,360.75 just below the May-2013 record close before ending 2014 at 7,230.57 [^pse-annual-report-2014:32].
- (P) **March 2020 (pandemic crash, closure, reopening).** 12 Mar 2020: PSEi -616.99 pts / -9.71% to 5,736.27 (biggest one-day fall since 2008, lowest close since Dec 2012); intraday -10.33% (5,697.13) triggered the 10% market-wide circuit breaker shortly before 3pm and halted trading for 15 minutes until 3:08pm (first use since Oct 2008); value PHP 7.96bn; net foreign selling PHP 0.77bn [^bw-283531]. The finance secretary asked the SSS and GSIS to at least double their daily equity purchases [^bw-283559]. 16 Mar: shortened hours; 17-18 Mar: trading suspended [^pse-cn-2020-0017:1][^pse-cn-2020-0021:1]. 19 Mar (reopening, 09:30-13:00 session): the circuit breaker triggered again right at the open (PSEi -12.4% at the opening bell); the index touched 4,039.15 (-24.29% intraday, "unprecedented"), recovered to 4,751.72 and closed at 4,623.42 (-711.95 pts, -13.34%; all-shares -11.92%); value PHP 9.42bn on 1.25bn shares; net foreign selling PHP 2.40bn [^bw-284527][^pse-monthly-report-2020-03:1]. Rule changes: lower static threshold cut from 50% to 30% (21 Mar) and three-tier circuit breaker (10/15/20% -> 15/30/60-minute halts) from 4 May 2020 [^pse-cn-2020-0028:1][^pse-cn-2020-0044:1]. Rebounds of +5.31% (25 Mar) and +7.44% (26 Mar); the week of 23-27 Mar traded PHP 34.7bn on 644k trades (129k/day vs 75-85k in 2019) [^pse-weekly-reports-dataset]. 2020 net foreign selling was PHP 128.57bn, the largest of the decade [^pse-monthly-report-2021-12:2].
- (I; own calculation from the Daily Quotation Reports of 12, 16, 19 and 25 Mar 2020, main-board stock lines; the 19 Mar report is archived [^pse-eod-daily-quotation-2020-03-19:1], the other three are part of [^pse-dqr-dataset]) **Crash-week breadth.** Value of the common-stock lines was PHP 7.79bn (12 Mar), 6.21bn (16 Mar), 9.00bn (19 Mar) and 7.18bn (25 Mar), plus block sales of 0.16bn, 0.24bn, 0.41bn and 1.12bn (9.00 + 0.41 = 9.41bn reproduces the PHP 9.42bn reported for 19 Mar). The top-5 names took 41%, 46%, 49% and 42% of value and the top-10 59%, 67%, 69% and 61%, against 2020 medians of 37% and 55% on ordinary sampled days (s.2): concentration rises in stress. On 12 Mar, the first circuit-breaker day, 30% of the 100 most-traded stocks closed at the day's low and the mean position of the close within the day's range was 0.19 (0.5 = neutral). On the 19 Mar reopening the median top-100 stock traded in a 17.0% high-low range (SM 509.50-698.00, BDO 75.00-99.80, ALI 19.44-25.20, AC 360.00-475.00), 23% closed at the low, and the stock-level net foreign lines summed to -PHP 2.37bn (BusinessWorld: -2.40bn); by 25 Mar the median top-100 range had narrowed to 5.8% and 20% closed at the high. Block sales were 1.12bn on 25 Mar (143m shares), i.e. 13% of the day's value, and the largest line that day was AGI with PHP 1.08bn and PHP 0.74bn of net foreign selling.
- (I; PSE weekly data) **MSCI/index review days** show up as the highest-value sessions at the end of Feb/May/Aug/Nov: 2019-11-26 PHP 21.2bn; 2020-05-29 20.4bn (+4.82% day); 2020-11-27 27.6bn; 2021-05-27 23.8bn (+5.11%); 2021-11-29 28.0bn; 2022-05-31 35.7bn (foreign 84%); 2022-11-29 23.5bn; 2023-02-28 21.2bn; 2023-05-31 24.5bn (foreign 81%); 2024-05-31 22.7bn; 2025-02-28 20.6bn; 2025-05-30 40.0bn (6.2x median; net foreign -15.3bn); 2026-02-27 19.6bn; 2026-05-29 26.5bn (net foreign -6.6bn); 2026-08-28 18.8bn (ALI PHP 7.2bn = 40% and ICT PHP 4.3bn = 24% of regular value; ALI foreign net selling PHP 1.56bn) [^pse-weekly-reports-dataset][^pse-dqr-2026-08-28:4][^pse-dqr-2026-08-28:5]. Inquirer reported "PSEi sinks to 5,700 level as MSCI reshuffle spark sell-off" on 29 May 2026 (S, headline) [^gnews-inquirer-2026-05-29]; BusinessWorld reported ALI rising on MSCI rebalancing/foreign inflows on 31 Aug 2025 (S, headline) [^gnews-bw-2025-08-31].
- (S/P) **How index events trade (BusinessWorld).** 30 May 2023: "Philippine shares fall ahead of MSCI rebalancing" (PSEi -1.25% to 6,510.67; foreign institutions rebalancing before the MSCI effective date) and 31 May 2023 "PSEi drops further on month-end window dressing" [^bw-525845][^bw-526114]; 2 Jun 2025: JFC fell 8.2% in the week of the 30 May 2025 MSCI review (AEV added to the MSCI Global Small Cap index; Bloomberry and Wilcon removed) [^bw-676401]; 3 Jun 2024: "MSCI rebalancing, foreign selling drop BDO shares" [^bw-598985]; 1 Jun 2026: Ayala Corp. fell after the May 2026 MSCI changes (JFC dropped to small cap, effective at the close of 29 May), with passive-fund forced selling "concentrated in the closing auction" [^bw-753259]. On 30 May 2025 block sales were 61% of the day's value (see below).
- (P/S) **PSE's own index review: the CBC/AREIT inclusion (Jan-Feb 2025).** On 24 Jan 2025 the PSE announced that AREIT and China Banking Corp. (CBC) would enter the PSEi and Nickel Asia (NIKL) and Wilcon Depot (WLCON) leave it, effective Monday 3 Feb 2025 [^pse-cn-2025-0005:1]. On the last session before the change (Fri 31 Jan 2025) CBC traded 62.9m shares = PHP 5.60bn (net foreign buying PHP 0.66bn) and AREIT 65.6m shares = PHP 2.72bn (net foreign buying PHP 0.99bn), against single-name values that are normally below PHP 1bn; total value was PHP 21.6bn (4.6x the trailing median) while the PSEi fell 4.01% into a bear market [^pse-dqr-2025-01-31:1][^pse-dqr-2025-01-31:4][^pse-weekly-reports-dataset]. CBC opened at PHP 66.95 and closed at its high of PHP 93 (+39% from the open); BusinessWorld reported +33.8% on the week and +46.5% YTD, with First Resources attributing the jump to index-tracking funds adjusting portfolios [^pse-dqr-2025-01-31:1][^bw-650452]. (I) An index-inclusion date can therefore move an included mid-cap by 30-40% in one session on two to three times its normal weekly value, and the move is concentrated at the end of the last session before effectivity.
- (P/I) **Block-sale-dominated days** (PHP bn; blocks identified from the PSE Daily Quotation Report block-sale tables): 2022-12-14: total 116.0 (19x the trailing 20-day median), of which block sales 110.9 - Eagle Cement (EAGLE) crosses at PHP 22.02 as a San Miguel unit completed its acquisition/tender offer (572.78m tendered shares = PHP 12.62bn; BusinessWorld puts the whole transaction at ~PHP 97.4bn); foreign activity 3%, PSEi +0.5%; EAGLE was suspended after the cross pending delisting [^pse-eod-daily-quotation-2022-12-14:11][^bw-493205]. 2021-12-16: 87.5 (block 80.7): an Aboitiz Power (AP) block of 1.84bn shares at PHP 40.01 = PHP 73.6bn plus a 146.5m-share print (PHP 5.9bn), with PHP 79.4bn of foreign net buying that day (the counterparty is not identified in the sources read; BusinessWorld's wrap printed the net foreign figure as "P79.44 million", a units error - PSE reports it in PHP thousands) [^pse-eod-daily-quotation-2021-12-16:10][^bw-418099]. 2023-06-16: 53.5 (block 44.8): BPI block of 329.7m shares at PHP 105 = PHP 34.6bn plus PHP 8.0bn more at the same price [^pse-eod-daily-quotation-2023-06-16:11]. 2023-09-26: 35.2 (block 29.3): Metro Pacific Investments (MPI) crosses of 2bn shares at PHP 5.20 (PHP 10.4bn each; MPIC's voluntary-delisting plan was reported on 21 Sep 2023 [^bw-546877]) [^pse-eod-daily-quotation-2023-09-26:12]. 2021-03-03: 34.1 (block 24.7; regular value led by small caps AR, DITO, PHA at PHP 1.1-1.25bn each) [^pse-dqr-dataset]. 2025-05-30 (MSCI day): 40.0 = regular 15.55 + block 24.47 (61%) [^pse-dqr-2025-05-30:12]. 2025-10-24: 26.3 (block 19.3; San Miguel preferred series SMC2J/SMC2K at PHP 75) [^pse-eod-daily-quotation-2025-10-24:12]. 2026-09-11: 32.7 (block 26.9 = 82%; First Gen (FGEN) PHP 25.8bn) [^pse-eod-daily-quotation-2026-09-11:11]. 2026-09-17: SM printed PHP 16.8bn = 73% of regular-market value [^pse-eod-daily-quotation-2026-09-17:11]. Overall, 118 of 1,793 sessions (6.6%) had total value >= 2x the trailing 20-day median and 48 (2.7%) >= 3x [^pse-weekly-reports-dataset]. The December 2022 monthly report records non-regular ADVT of PHP 7,173.64m for the month (Industrial sector ADVT 7,744m) [^pse-monthly-report-2022-12:1].
- (S) **Technical glitches (full BusinessWorld texts read).** (a) 4 Jan 2022: PSE cancelled the whole session after 43 of 125 trading participants could not connect the (Nasdaq) trading engine to the Flextrade front-end; all orders queued from 3:01pm on 3 Jan until 9:05am on 4 Jan were cancelled; the Revised Trading Rules allow a halt if at least one-third of users cannot access the system; the PSEi had closed 7,041.27 (-1.14%) on 3 Jan [^pse-cn-2022-0001-delay-market-opening:1][^pse-cn-2022-0002-cancellation-of-trading-2022-01-04:1][^bw-421693][^bw-421594]. (b) 3 Jan 2024: trading halted at 09:32 and resumed at 11:56 (afternoon session ran 13:00-15:00 as scheduled) [^pse-cn-2024-0001-market-halt:1][^pse-cn-2024-0003-update-market-halt:1], because of a glitch in the mobile trading application's account-authentication process (one of four silos) affecting at least one-third of participants; PSE explained two days later and analysts urged faster disclosure [^bw-567311]. The PSE data for that day show value of only PHP 3.11bn on 27,036 trades (about half the 2024 averages of PHP 6.10bn and 58k trades) and a PSEi close of 6,498.88 (-0.84%) [^pse-weekly-reports-dataset]. (c) 24 Mar 2025: the open was delayed from 09:30 to 11:10 by a "system connectivity issue"; the PSEi closed 6,192.02 (-1.19%) on PHP 4.63bn and 42,853 trades (about 60% of the 2025 averages); analysts noted disruptions "every year since 2022" [^pse-cn-2025-0015-adjusted-schedule-2025-03-24:1][^bw-661247][^bw-661414][^pse-weekly-reports-dataset]. (d) 9 Dec 2024: the open was delayed to 09:55 (pre-open 09:40, pre-open no-cancel 09:50; cause not stated in the notice) [^pse-cn-2024-0061-adjusted-schedule-2024-12-09:1]. Manila Bulletin (20 Aug 2025) reported that PSE can now cancel trading in disasters or glitches (headline only [^gnews-mb-2025-08-20]). PSE is replacing its trading engine ("PSE Trading Engine 2026"): pre-production connectivity testing 29 Sep-9 Oct and testing 12-22 Oct, Saturday market rehearsals on 31 Oct, 7 and 14 Nov, and go-live on 23 Nov 2026 as a "big bang" with no parallel run; the new board-lot table is targeted for Q4 2026 "alongside the new trading engine" [^pse-nte-broker-forum-2026-07-09:9][^pse-nte-faq-2026-08:1][^pse-asm-2026-president-report:22].
- (P) **Weather and administrative non-trading days.** No trading (and no clearing/settlement at SCCP) on 26 Sep 2022 [^pse-cn-2022-0035-trading-suspension-2022-09-26:1] and no trading on 24 Jul 2024 because of "inclement weather and resulting floods" [^pse-cn-2024-0038-trading-suspension-2024-07-24:1]; 31 Oct 2025 was declared a non-trading day by proclamation, and the PSE announced that 8, 24, 25, 30 and 31 Dec 2025 and 1 Jan 2026 would also be non-trading, which is why 29 Dec 2025 was the last session of 2025 [^pse-cn-2025-0038-non-trading-day-2025-10-31:1][^pse-cn-2025-0043-non-trading-days:1].
- (P) **Halt rule changed after the glitches (SEC-approved 20 Aug 2025).** The trigger for a market-wide halt moved from "at least one-third of trading participants cannot access the trading system" to "participants accounting for more than 50% of the average daily trading value (excluding block sales) of the preceding six months cannot access it, directly or through a correspondent TP, due solely to Exchange system problems or natural disasters/unforeseen events"; every TP must now have a correspondent TP as a business-continuity requirement; new guidelines let the Exchange halt, suspend or cancel a scheduled trading day in natural disasters or extraordinary circumstances if its business-continuity plan cannot be implemented [^pse-cn-2025-0037:1]. (The old one-third rule was the one invoked on 4 Jan 2022 [^pse-cn-2022-0001-delay-market-opening:1].)
- (S) **Manipulation / enforcement (allegations, as reported).** The SEC's case against Villar Land Holdings Corp. ("HVN", formerly Golden MV Holdings) is described by a Philstar opinion column (5 Feb 2026) as the largest stock-price manipulation and insider-trading case the government has filed against a listed company and its owners. As quoted from the SEC: in March 2025 the company released unaudited FY2024 results (total assets PHP 1.33tn vs PHP 5.1bn; net income PHP 999.72bn, from revaluation of real estate) before its auditor approved them; HVN trading surged and the PSE suspended trading because audited statements were delayed; the November 2025 audited statements reversed the figures (assets PHP 33bn; net income PHP 1.42bn) and the price fell; the SEC's review found "recurring trading patterns involving a limited group of related individuals and entities whose transactions accounted for a substantial portion of trading activity during periods of price increases", plus director purchases hours before a material disclosure; the SEC filed a criminal complaint with the DOJ (pending initial evaluation); Mr Villar denies wrongdoing [^philstar-2026-02-05-villar]. These are allegations, not findings. Older cases (S, snippets only): BW Resources (2000; SEC recommended charges for insider trading and price manipulation) and Calata Corp (after listing, PHP 4bn traded in two weeks and the price went from PHP 23.95 to PHP 8 in four days) [^inq-biz-buzz-calata].
- (P) **Surveillance.** CMIC (Capital Markets Integrity Corporation) monitors the market with the Korea Exchange-developed "Total Market Surveillance" system and can restrict/halt/suspend securities or participants for unusual trading [^pse-investing-page].
- (I) **Sep-Oct 2026 sell-off:** PSEi 6,625.46 (26 Feb) -> 6,366.64 (Aug high) -> 5,956.33 (31 Aug) -> 5,629.03 (2 Oct), -3.38% in the week of 28 Sep-2 Oct with value PHP 35.4bn and net foreign selling PHP 4.57bn [^pse-weekly-report-2026-10-02:1][^pse-monthly-report-2026-08:1]; commentary cites BSP rate hike, record-low peso, growth downgrades and US-Iran tensions (S headlines: "PSEi falls below 5,800 on renewed US-Iran fears", Inquirer 28 Sep 2026 [^gnews-inquirer-2026-09-28]).

### Inferences
- (I) Three of the PSE's four recent disruptions (2022, 2024, 2025) were connectivity/front-end problems at the opening, not engine matching errors; the new trading engine cut-over (go-live 23 Nov 2026) is the next operational risk.
- (I) Because index-event days (3-6x volume) and block days (up to 19x) are rare and predictable only for MSCI, execution algos need an "event day" regime flag.

### Execution implications
- Pre-trade calendar: MSCI/FTSE/S&P review dates; PSE block-sale announcements; corporate crosses (tender offers, placements) that make one stock >50% of regular value.
- Resilience: confirm order state after outages (2022/2024/2025 halts) and plan for the 23 Nov 2026 engine cut-over (no parallel run; only three Saturday rehearsals): freeze or de-risk algos around go-live, re-certify FIX/ITCH (the PSE reports that only a minority of broker systems had completed connectivity testing by July 2026 [^pse-nte-broker-forum-2026-07-09:5]) and re-estimate any microstructure calibrations after the change.

### Gaps
- SEC and PSE press releases (sec.gov.ph blocks automated access) were not read; the Villar Land account relies on one opinion column quoting the SEC, and the older BW Resources/Calata cases on search snippets. MSCI review dates were inferred from volume spikes and news headlines, not from MSCI's calendar. The counterparties/reasons for the 16 Dec 2021 Aboitiz Power block, the 16 Jun 2023 BPI block, the 24 Oct 2025 San Miguel preferred prints and the 11 Sep 2026 First Gen block were not identified.
- No source found for the exact count of 2022-2026 market-wide halts or per-stock freezes.

---

## 8. Academic and practitioner literature on PSE microstructure

### Takeaway
Direct peer-reviewed microstructure studies of the PSE are almost absent. What exists is (i) calendar-anomaly/efficiency tests on daily or monthly *index* data (Rufino & Delfino 2016; Camba & Camba 2020; Almonares 2019), (ii) event/volatility studies (Calderon 2002; Pinili & Murcia 2023), (iii) one IPO-underpricing study (Sullivan & Unite 1999), (iv) herding studies using daily returns or surveys (Rahman & Ermawati 2020; Pamplona 2023) and (v) policy/consultation documents (PSE 2013, 2023; OECD 2024). I found **no** PSE-specific study of tick size, price limits/circuit breakers, the closing auction, board-lot/odd-lot effects, bid-ask spreads/information asymmetry, or broker-ID transparency; the closing-auction rationale rests on PSE's own 2013 consultation paper.

### Cited Findings
**A. Calendar effects, efficiency and volatility regimes (index data)**
- (P; archived) Rufino & Delfino (2016), DLSU Business & Economics Review 25(2): data = daily closes of the PSEi and six sector indices, 2 Jan 2006 - 7 Jun 2013 (341 Mondays; ~1,700 days); method = Kruskal-Wallis test and pairwise multiple comparisons with a significance-level correction to avoid false positives; finding = no day-of-the-week effect in the PSEi or any sector index in the "modernisation" period, in contrast to pre-2005 studies that found one (Basher & Sadorsky 2006; Choudhry 2000; Brooks & Persand 2001; Almonte 2004); modernisation steps cited: Online Disclosure System (2005) and the surveillance system acquired in 2007 [^paper-rufino-delfino-2016-dow:2][^paper-rufino-delfino-2016-dow:3][^paper-rufino-delfino-2016-dow:4][^paper-rufino-delfino-2016-dow:8]. My own 2019-2026 daily estimates (s.5) agree: Tue +0.14% (t=2.4) and Fri -0.12% (t=-2.05) are the extremes, but neither survives a Bonferroni correction for five weekdays.
- (P; abstract) Camba & Camba (2020), JAFEB 7(10): ADF and Phillips-Perron unit-root tests, Lo-MacKinlay and Chow-Denning variance-ratio tests on PSE data; cannot reject a random walk; attribute weak-form efficiency to liquidity gains from the PSE's modernisation [^paper-camba-camba-2020-random-walk]. Companion paper: robust least squares and VAR show COVID-19 daily infections had a negative, significant effect on the PSEi, the peso and diesel prices [^paper-camba-camba-2020-covid].
- (P; abstract) Pinili & Murcia (2023), Eur. J. Econ. Financ. Res. 7(3): daily PSEi 2 Dec 2019 - 5 May 2022 (T~632); Chow and Bai-Perron tests find four breakpoints linked to COVID-19 events; worst performance in Jan-Apr 2020; OLS suggests random-walk characteristics [^paper-pinili-murcia-2023-covid-breakpoints].
- (P; abstract) Almonares (2019), DLSU BER: Markov-switching model of monthly PSE returns, Jan 2000 - Jul 2017: two regimes (positive mean/low volatility vs negative mean/high volatility); high-volatility regimes coincide with domestic political crises, the Asian financial crisis, currency depreciation and the GFC [^paper-almonares-2019-markov].
- (P; archived) Calderon (2002), DLSU BER 13(2): event study of PHISIX daily returns for 30 days before/after the 8 Aug 2001 demutualisation (27 Jun - 21 Sep 2001, 61 days); F-tests (variance ratio >1) and GARCH(1,1): volatility was higher after demutualisation (GARCH lag coefficient 0.60 before, 0.78 after). Very short window overlapping the Sep-2001 attacks and no anomaly adjustment (authors' own limitation) - low evidentiary weight [^paper-calderon-2002-demutualization:3][^paper-calderon-2002-demutualization:13][^paper-calderon-2002-demutualization:15].
- (P; abstract) Atento et al. (2026), Asian Financial Economics and Policy: Jul 2018 - Jun 2025, annual tercile portfolios by price per share, weekly/monthly equal-weighted returns: no size premium (SML 0.030% weekly, p=0.793; 0.145% monthly, p=0.758) in any of seven annual cohorts or three sub-periods; strong GARCH(1,1) volatility clustering; states Perez (2018) is the only prior published size/value study with PSE firm-level data [^paper-atento-2026-size-premium].
- (P; abstract) Unite (2002), DLSU BER: Johansen cointegration of the PSE with Taiwan, Japan, Hong Kong, Singapore and the US around domestic capital-market liberalisation [^paper-unite-2002-integration].

**B. IPOs**
- (P; abstract) Sullivan & Unite (1999), Rev. Pacific Basin Fin. Markets & Policies: 104 Philippine IPOs 1987-1997, average initial return 22.69%; offer size, firm age and industry do not explain underpricing; authors infer that Philippine underwriters face different regulatory policies, contractual mechanisms and market conditions [^paper-sullivan-unite-1999-ipo]. Institutional context (P): underwriters must allocate at least 20% of an IPO to PSE trading participants and 10% to local retail investors; retail took only 1.4% of IPO shares in 2021 per PSE, improving with the PSE EASy app (2 of 4 IPOs in 2019 using EASy had >9% local-small-investor take-up, versus <2% historically) [^oecd-capital-market-review-philippines-2024:33][^pse-annual-report-2019:5]. IPO counts and proceeds 2015-2025 are in Table A.

**C. Herding and investor behaviour**
- (P; archived) Rahman & Ermawati (2020), Bull. Monetary Econ. & Banking 23(3): daily returns of the most liquid stocks in the ASEAN-5 and the US, 4 Jan 2000 - 28 Dec 2018; CSAD herding regressions with Newey-West errors; the dominant global driver of herding is the US federal funds rate, the dominant regional driver is Singapore's cross-market herding; herding caused by market *up* spikes occurs only in the Philippines (down-market herding only in Malaysia) [^paper-rahman-ermawati-2020-herding:1][^paper-rahman-ermawati-2020-herding:6][^paper-rahman-ermawati-2020-herding:14].
- (P; abstract) Pamplona (2023): survey of 395 Filipino retail investors, structural equation model; low herd bias; self-reflection reduces herding; investor-advisor relationship does not aid learning [^paper-pamplona-2023-herd] (survey evidence, low-tier venue).

**D. Market development and reforms**
- (P; abstract) Briones (2017), J. Philippine Development 41-42: structural and regulatory history (unification of two exchanges, demutualisation, Securities Regulation Code); world ranking by market-cap ratio rose from 44th (2009) to 12th (2014); challenges: narrow investor base, lack of competition, weak governance and legal framework [^paper-briones-2017-stock-market-development].
- (P; abstract) Dioquino (2014) case study of the 2011-2013 PSE turnaround: initiatives sorted into "Liquidity" (raising volume) and "Governance" buckets; index breaks 5,000 [^paper-dioquino-2014-sicat-case]. PSE's 2013 report documents the reforms: minimum 10% public ownership for all listed companies, average float 34.32% at end-2013 (32.28% in 2012), DMA rules approved 29 Oct 2013 (effective first trading day of 2014), extended pre-close from 4 Nov 2013 [^pse-annual-report-2013:28].

**E. Topics for which no PSE-specific study was found** (with the closest primary evidence)
- Tick size / board lot: no study; the PSE's own consultations are the only evidence: Oct 2023 (cut lot sizes so that PHP 100 buys one lot, ticks unchanged) [^pse-cn-2023-0051:3] and Dec 2025 (one-share lots with the new engine and a coarser tick for PHP 10-19.98 stocks, s.4) [^pse-cn-2025-0046-board-lot-trading-at-last:4].
- Price limits / circuit breakers: no study; PSE circulars of March-April 2020 changed the static threshold and circuit breakers (s.6) [^pse-cn-2020-0028:1][^pse-cn-2020-0044:1].
- Closing auction: no study; PSE's 2013 consultation gives the rationale (peer pre-close lengths; MOC/ETF benchmarking) [^pse-memo-extended-pre-close-consultation-2013:1].
- Broker-ID transparency: no study; the PSE's ITCH feed specification (v2.3, OMX X-stream, 2014) defines trade/execution messages with passive and active broker IDs ("e", "c", "p") used when Broker Anonymity is *not* in force and anonymous versions ("E", "C", "P") when it is, "as announced by the exchange"; which mode is live in 2026 is not stated in the documents read [^pse-itch-equities-feed-spec-v2-3:15][^pse-itch-equities-feed-spec-v2-3:25]. The same spec supports indicative price/quantity messages for open, intraday and closing auctions [^pse-itch-equities-feed-spec-v2-3:26].
- Information asymmetry / spreads / price impact: no study; see s.4 for my end-of-day proxies. Algorithmic trading: PSE only consulted on explicit algorithmic-trading rules in Sep 2023 [^pse-cn-2023-0043:1].
- Search log: OpenAlex title/abstract searches combining Philippine/PSE with tick size, price clustering, price limits, circuit breaker, intraday, bid-ask spread, liquidity premium, trading volume, herding, foreign ownership/foreign investors; Crossref bibliographic queries on bid-ask spread, price limits, volume-volatility, foreign-investor behaviour, stock splits; direct Google Scholar/SSRN/ScienceDirect searches were not possible in this session (web-search budget exhausted, DuckDuckGo/Bing blocked), so "none found" is not proof of absence.

**F. Practitioner / policy sources used throughout**
- OECD (2024) Capital Market Review of the Philippines (liquidity, free float, trading costs, market making) [^oecd-capital-market-review-philippines-2024:42]; PSE consultation papers (pre-close 2013, algorithmic/VWAP 2023, board lot 2023); sell-side comments as reported by BusinessWorld (MSCI closing-auction flows, glitch reactions; s.5 and s.7).

### Inferences
- (I) The thinness of the literature means execution research on the PSE must be proprietary: spreads, depth, auction imbalance and intraday curves are not published and have not been studied in public.
- (I) The few findings that exist (random walk at daily frequency, no weekday effect, herding on up-spikes tied to US rates) are consistent with my own daily-data results (no autocorrelation, no robust weekday effect, Fed/EM-flow-driven regimes), but they say nothing about intraday behaviour.

### Execution implications
- Use US/European evidence on tick-size, auction and price-limit effects only as priors; build PSE-specific impact and auction models from your own order/ITCH data.
- Expect regulatory microstructure changes (new trading engine and board-lot table in Q4 2026; negotiated trades; market-making rules; derivatives plans) to invalidate historical calibrations; re-estimate after each change.

### Gaps
- No access to paywalled full texts (Sullivan & Unite 1999; Camba & Camba 2020; Almonares 2019; Unite 2002; Pinili & Murcia 2023 - abstracts only); no PSE-specific paper on spreads/depth/price impact/auctions; SSRN/Google Scholar not searchable here.

---

## Source catalog

```yaml
- slug: pse-annual-report-2013
  title: "The Philippine Stock Exchange, Inc. 2013 Annual Report (\"All The Right Pieces\")"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://ir.pse.com.ph/wp-content/uploads/sites/4/2020/04/2013-PSE-Annual-Report.pdf"
  local_path: pdfs/pse-annual-report-2013.pdf
  edition: historical
  amended_through: undated
  note: "FY2013; taper-tantrum context (p6, p11), extended pre-close (p28), float level."
- slug: pse-annual-report-2014
  title: "PSE 2014 Annual Report (\"Plans In Motion\")"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://ir.pse.com.ph/wp-content/uploads/sites/4/2020/04/2014-PSE-Annual-Report.pdf"
  local_path: pdfs/pse-annual-report-2014.pdf
  edition: historical
  amended_through: undated
  note: "FY2014 index and peak levels (p32)."
- slug: pse-annual-report-2015
  title: "PSE 2015 Annual Report (\"Ready for Bigger Milestones\")"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://ir.pse.com.ph/wp-content/uploads/sites/4/2020/04/2015-PSE-Annual-Report.pdf"
  local_path: pdfs/pse-annual-report-2015.pdf
  edition: historical
  amended_through: undated
  note: "FY2015 turnover, foreign ratio, IPO list (p32), trading schedule (p10)."
- slug: pse-annual-report-2016
  title: "PSE 2016 Annual Report (\"Meeting Challenges\")"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://ir.pse.com.ph/wp-content/uploads/sites/4/2020/04/PSE-2016-FA-Meeting-Challenges.pdf"
  local_path: pdfs/pse-annual-report-2016.pdf
  edition: historical
  amended_through: undated
  note: "FY2016; 4 IPOs (p33), five-year indicators (p35), trading schedule (p10)."
- slug: pse-annual-report-2017
  title: "PSE 2017 Annual Report (\"Evolving into a World Class Stock Exchange\")"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/4/2021/07/2017_PSE_Annual_Report.pdf"
  local_path: pdfs/pse-annual-report-2017.pdf
  edition: historical
  amended_through: undated
  note: "Table 06 five-year market indicators 2013-2017 on p17; narrative p16."
- slug: pse-annual-report-2018
  title: "PSE 2018 Annual Report (\"Geared For Growth\")"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/4/2021/02/2018_PSE_Annual_Report.pdf"
  local_path: pdfs/pse-annual-report-2018.pdf
  edition: historical
  amended_through: undated
  note: "ATH 9,058.62 on 29 Jan 2018 (p6); indicators 2016-2018 (p32)."
- slug: pse-annual-report-2019
  title: "PSE 2019 Annual Report (\"Charting PSE's ESG Roadmap\")"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/4/2021/06/PSE-Annual-Report-2019-1.pdf"
  local_path: pdfs/pse-annual-report-2019.pdf
  edition: historical
  amended_through: undated
  note: "Indicators 2018-2019 (p32); 4 IPOs in 2019 (p5, p31)."
- slug: pse-annual-report-2020-17a
  title: "PSE Annual Report 2020 (SEC Form 17-A)"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/4/2021/06/2020-Annual-Report.pdf"
  local_path: null
  edition: historical
  amended_through: undated
  note: "Not archived (not relied on for data): 80-page image-only SEC Form 17-A; OCR of the MD&A (pp. 31-32, 36) shows corporate financials, not market statistics. The FY2021-FY2023 reports in the same folder (2022/05/2021-Annual-Report.pdf, 2023/05/2022-Annual-Report.pdf, 2024/04/2023-Annual-Report.pdf) have the same image-only format."
- slug: pse-infographic-fy21
  title: "The Philippine Stock Market - End-December 2021 (infographic)"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2022/01/FY21-Infographic.pdf"
  local_path: pdfs/pse-infographic-fy21.pdf
  edition: historical
  amended_through: 2022-01-17
  note: "Year-end indicators; trading hours footnote."
- slug: pse-infographic-fy22
  title: "The Philippine Stock Market - End-December 2022 (infographic)"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2023/01/FY22-Infographic-final.pdf"
  local_path: pdfs/pse-infographic-fy22.pdf
  edition: historical
  amended_through: 2023-01-12
  note: "286 listed companies; primary capital raised 99.17bn."
- slug: pse-infographic-fy23
  title: "The Philippine Stock Market - End-December 2023 (infographic)"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2024/01/FY23-Infographic.pdf"
  local_path: pdfs/pse-infographic-fy23.pdf
  edition: historical
  amended_through: 2024-01-12
  note: "283 listed; short selling launched; T+2 shift."
- slug: pse-infographic-fy24
  title: "The Philippine Stock Market - End-December 2024 (infographic)"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2025/01/FY24-Infographic-v3-clean.pdf"
  local_path: pdfs/pse-infographic-fy24.pdf
  edition: historical
  amended_through: 2025-01-10
  note: "283 listed, 121 active TPs, VWAP trading implemented."
- slug: pse-infographic-fy25
  title: "The Philippine Stock Market - End-December 2025 (infographic)"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2026/01/FY25-Infographic.pdf"
  local_path: pdfs/pse-infographic-fy25.pdf
  edition: historical
  amended_through: 2026-01-08
  note: "282 listed; MCAP 18.73tn; ADVT 7.33bn; net foreign selling 51.20bn."
- slug: pse-infographic-1q26
  title: "The Philippine Stock Market - End-March 2026 (infographic)"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2026/05/1QFY26-Infographic.pdf"
  local_path: pdfs/pse-infographic-1q26.pdf
  edition: in-force
  amended_through: 2026-05-04
  note: "1Q26 indicators; net foreign buying 12.14bn."
- slug: pse-infographic-2q26
  title: "The Philippine Stock Market - End-June 2026 (infographic)"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2026/07/2Q26-Infographic.pdf"
  local_path: pdfs/pse-infographic-2q26.pdf
  edition: in-force
  amended_through: 2026-07-23
  note: "1H26 indicators; market-making rule amendments released."
- slug: pse-monthly-report-2019-12
  title: "PSE Monthly Report December 2019 (public preview, 2 pages)"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/market_report/December 2019-MR.pdf"
  local_path: pdfs/pse-monthly-report-2019-12.pdf
  edition: historical
  amended_through: 2020-02-26
  note: "ADVT regular vs non-regular, 243 days."
- slug: pse-monthly-report-2020-03
  title: "PSE Monthly Report March 2020 (preview)"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/market_report/March 2020-MR.pdf"
  local_path: pdfs/pse-monthly-report-2020-03.pdf
  edition: historical
  amended_through: 2020-05-20
  note: "PSEi low 4,623.42; 20 trading days."
- slug: pse-monthly-report-2020-12
  title: "PSE Monthly Report December 2020 (preview)"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/market_report/December 2020-MR.pdf"
  local_path: pdfs/pse-monthly-report-2020-12.pdf
  edition: historical
  amended_through: 2021-02-01
  note: "ADVT 7,348.13m in 241 days."
- slug: pse-monthly-report-2021-12
  title: "PSE Monthly Report December 2021 (preview)"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2022/01/12-2021_PSE-Monthly-Report_Preview.pdf"
  local_path: pdfs/pse-monthly-report-2021-12.pdf
  edition: historical
  amended_through: 2022-01-31
  note: "2021 and 2020 value/foreign/MCAP; record capital raised."
- slug: pse-monthly-report-2022-12
  title: "PSE Monthly Report December 2022 (preview)"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2023/02/12-2022_PSE-Monthly-Report_Preview.pdf"
  local_path: pdfs/pse-monthly-report-2022-12.pdf
  edition: historical
  amended_through: 2023-02-01
  note: "2022 summary; December non-regular spike."
- slug: pse-monthly-report-2023-12
  title: "PSE Monthly Report December 2023 (preview)"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2024/02/12-2023_PSE-Monthly-Report_Preview.pdf"
  local_path: pdfs/pse-monthly-report-2023-12.pdf
  edition: historical
  amended_through: 2024-02-26
  note: "2023 summary."
- slug: pse-monthly-report-2024-12
  title: "PSE Monthly Report December 2024 (preview)"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2025/02/12-2024_PSE-Monthly-Report_Preview.pdf"
  local_path: pdfs/pse-monthly-report-2024-12.pdf
  edition: historical
  amended_through: 2025-02-04
  note: "2024 summary."
- slug: pse-monthly-report-2025-12
  title: "PSE Monthly Report December 2025 (preview)"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2026/02/12-2025_PSE-Monthly-Report_Preview.pdf"
  local_path: pdfs/pse-monthly-report-2025-12.pdf
  edition: historical
  amended_through: 2026-02-04
  note: "2025 summary; 243 trading days; foreign ratio 46.3%."
- slug: pse-monthly-report-2026-08
  title: "PSE Monthly Report August 2026 (preview)"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2026/09/08-2026_PSE-Monthly-Report_Preview.pdf"
  local_path: pdfs/pse-monthly-report-2026-08.pdf
  edition: in-force
  amended_through: 2026-09-30
  note: "Latest monthly summary used (YTD to end-Aug 2026)."
- slug: pse-monthly-report-sample
  title: "PSE Monthly Report February 2020 (full, 46 pages)"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/market_report/February 2020-MR.pdf"
  local_path: pdfs/pse-monthly-report-sample.pdf
  edition: historical
  amended_through: 2020-04-17
  note: "Archived by another researcher; daily regular/non-regular value, top-25 lists."
- slug: pse-investor-profile-2013
  title: "Stock Market Investor Profile 2013"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2021/05/2013_StockMarketInvestorProfile.pdf"
  local_path: pdfs/pse-investor-profile-2013.pdf
  edition: historical
  amended_through: 2014-07-24
  note: "525,850 (2012) and 585,562 (2013) accounts; online accounts 129,255 (p6); active share 23.9% (p3). Date = posting date in the PSE market-report index."
- slug: pse-investor-profile-2014
  title: "Stock Market Investor Profile 2014"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2021/05/2014_StockMarketInvestorProfile.pdf"
  local_path: pdfs/pse-investor-profile-2014.pdf
  edition: historical
  amended_through: 2015-08-18
  note: "640,665 accounts; 174,592 online (18 reporting TPs); active share 33.6% (p3). Date = posting date in the PSE market-report index."
- slug: pse-investor-profile-2015
  title: "Stock Market Investor Profile 2015"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2021/05/Stock_Market_Investor_Profile_2015_final.pdf"
  local_path: pdfs/pse-investor-profile-2015.pdf
  edition: historical
  amended_through: 2016-08-03
  note: "712,549 accounts; 236,669 online (22 reporting TPs); active share 32.7% (p3). Date = posting date in the PSE market-report index."
- slug: pse-investor-profile-2016
  title: "Stock Market Investor Profile 2016"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2021/05/Stock_Market_Investor_Profile_2016_final.pdf"
  local_path: pdfs/pse-investor-profile-2016.pdf
  edition: historical
  amended_through: 2017-05-29
  note: "773,187 accounts; 302,516 online (26 reporting TPs); active share 33.4% (p3). Date = posting date in the PSE market-report index."
- slug: pse-investor-profile-2017
  title: "Stock Market Investor Profile 2017"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2021/05/Stock_Market_Investor_Profile_2017_final.pdf"
  local_path: pdfs/pse-investor-profile-2017.pdf
  edition: historical
  amended_through: 2018-10-01
  note: "868,810 accounts; 388,864 online (26 reporting TPs); active share 34.0% (p3). Date = posting date in the PSE market-report index."
- slug: pse-investor-profile-2018
  title: "Stock Market Investor Profile 2018"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2021/05/2018_Stock_Market_Investor_Profile_revJul20.pdf"
  local_path: pdfs/pse-investor-profile-2018.pdf
  edition: historical
  amended_through: 2020-07-11
  note: "1,089,413 accounts (+25.4%); 625,763 online (27 reporting TPs); active share 29.1% (p3). The PSE index lists this revised version under July 2020. Date = posting date in the PSE market-report index."
- slug: pse-investor-profile-2019
  title: "Stock Market Investor Profile 2019"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2021/05/Stock_Market_Investor_Profile_2019_final.pdf"
  local_path: pdfs/pse-investor-profile-2019.pdf
  edition: historical
  amended_through: 2020-07-14
  note: "1,228,038 accounts; 782,118 online (32 reporting TPs); active share 25.2% (p3). Date = posting date in the PSE market-report index."
- slug: pse-investor-profile-2020
  title: "Stock Market Investor Profile 2020"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2021/05/Stock-Market-Investor-Profile-2020.pdf"
  local_path: pdfs/pse-investor-profile-2020.pdf
  edition: historical
  amended_through: 2021-06-02
  note: "1,396,753 accounts; 936,200 online (32 reporting TPs); active share 30.0% (p3). Date = posting date in the PSE market-report index."
- slug: pse-investor-profile-2021
  title: "Stock Market Investor Profile 2021"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2023/02/Stock-Market-Investor-Profile-2021-final-v2-1.pdf"
  local_path: pdfs/pse-investor-profile-2021.pdf
  edition: historical
  amended_through: 2022-06-10
  note: "1,620,017 accounts (+16.0%); 1,159,034 online (71.5%); active share 31.9% (p3). Date = posting date in the PSE market-report index."
- slug: pse-smip-2022
  title: "Stock Market Investor Profile 2022"
  publisher: "Philippine Stock Exchange (Corporate Planning and Research Dept.)"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2023/05/Stock-Market-Investor-Profile-2022.pdf"
  local_path: pdfs/pse-smip-2022.pdf
  edition: historical
  amended_through: 2023-06-05
  note: "Active-account share 20.2%."
- slug: pse-smip-2023
  title: "Stock Market Investor Profile 2023"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2024/05/Stock-Market-Investor-Profile-2023.pdf"
  local_path: pdfs/pse-smip-2023.pdf
  edition: historical
  amended_through: 2024-05-29
  note: "1,906,019 accounts; active 17.6%."
- slug: pse-smip-2024
  title: "Stock Market Investor Profile 2024"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2025/06/Stock-Market-Investor-Profile-2024-.pdf"
  local_path: pdfs/pse-smip-2024.pdf
  edition: historical
  amended_through: 2025-06-09
  note: "2,860,234 accounts; online 86.4%."
- slug: pse-investor-profile-2025
  title: "Stock Market Investor Profile 2025 (infographic)"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2026/05/2025-SMIP-Infographic.pdf"
  local_path: pdfs/pse-investor-profile-2025.pdf
  edition: in-force
  amended_through: 2026-05-29
  note: "3,641,067 accounts; online 88.6%; active 11.8%."
- slug: pse-asm-2026-president-report
  title: "PSE Annual Stockholders' Meeting 2026 - President's Report"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/4/2026/07/PSE-ASM-2026-PRESIDENT_S-REPORT.pdf"
  local_path: pdfs/pse-asm-2026-president-report.pdf
  edition: in-force
  amended_through: 2026-07-04
  note: "Local/foreign and retail/institutional shares (p7), accounts (p15), rule pipeline (p22-24)."
- slug: pse-analyst-briefing-1h-2026
  title: "PSE STAR Briefing - 1H 2026 Updates"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/4/2026/08/2026.08.17-PSE-STAR-1H-2026.pdf"
  local_path: pdfs/pse-analyst-briefing-1h-2026.pdf
  edition: in-force
  amended_through: 2026-08-17
  note: "Market highlights to 14 Aug 2026 (p3)."
- slug: oecd-capital-market-review-philippines-2024
  title: "OECD Capital Market Review of the Philippines 2024"
  publisher: "OECD"
  type: pdf
  canonical_url: "https://www.oecd.org/content/dam/oecd/en/publications/reports/2024/12/oecd-capital-market-review-of-the-philippines-2024_7b7ad891/80afb228-en.pdf"
  local_path: pdfs/oecd-capital-market-review-philippines-2024.pdf
  edition: in-force
  amended_through: undated
  note: "Publication date December 2024 (month from URL path; day not stated). Physical pages cited Year: 2024."
- slug: pse-cn-2023-0051
  title: "CN 2023-0051 Proposed Amendments to the PSE Board Lot (consultation)"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2023-0051.pdf"
  local_path: pdfs/pse-cn-2023-0051.pdf
  edition: superseded
  amended_through: 2023-10-09
  note: "Scanned; p3-4 contain the in-force tick/lot table and the proposal."
- slug: pse-cn-2023-0043
  title: "CN 2023-0043 Proposed amendments re Algorithmic Trading and VWAP Trading (consultation)"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2023-0043.pdf"
  local_path: pdfs/pse-cn-2023-0043.pdf
  edition: superseded
  amended_through: 2023-09-05
  note: "Rationale for VWAP trading (p4)."
- slug: pse-approved-rules-vwap-trading-2024
  title: "CN 2024-0010 Approved Rules on VWAP Trading"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2024-0010.pdf"
  local_path: pdfs/pse-approved-rules-vwap-trading-2024.pdf
  edition: in-force
  amended_through: 2024-02-01
  note: "Scanned; trading day schedule (p3, p5-6), VWAP rules (p7)."
- slug: pse-memo-extended-pre-close-consultation-2013
  title: "TPA 2013-0107 Extended Pre-Close Period (public comments)"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "n/a (PSE memorandum archived by another researcher)"
  local_path: pdfs/pse-memo-extended-pre-close-consultation-2013.pdf
  edition: historical
  amended_through: 2013-07-17
  note: "Rationale and peer pre-close durations."
- slug: pse-memo-extended-pre-close-implementation-2013
  title: "TPA 2013-0165 Implementation of Extended Pre-Close Period"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "n/a"
  local_path: pdfs/pse-memo-extended-pre-close-implementation-2013.pdf
  edition: historical
  amended_through: 2013-10-14
  note: "Effective 4 Nov 2013."
- slug: pse-memo-pre-close-schedule-2013
  title: "TPA 2013-0167 Pre-Close Schedule"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "n/a"
  local_path: pdfs/pse-memo-pre-close-schedule-2013.pdf
  edition: historical
  amended_through: 2013-10-16
  note: "15:15-15:18 auction; 15:18-15:20 no-cancel."
- slug: pse-cn-2020-0017
  title: "CN 2020-0017 Shortened Trading Hours"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2020-0017.pdf"
  local_path: pdfs/pse-cn-2020-0017.pdf
  edition: historical
  amended_through: 2020-03-15
  note: "COVID shortened hours."
- slug: pse-cn-2020-0021
  title: "CN 2020-0021 Trading Suspension Starting March 17, 2020"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2020-0021.pdf"
  local_path: pdfs/pse-cn-2020-0021.pdf
  edition: historical
  amended_through: 2020-03-16
  note: "Closure."
- slug: pse-cn-2020-0028
  title: "CN 2020-0028 Amendment of Rule on Static Threshold"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2020-0028.pdf"
  local_path: pdfs/pse-cn-2020-0028.pdf
  edition: in-force
  amended_through: 2020-03-21
  note: "Lower static threshold 50% -> 30%."
- slug: pse-cn-2020-0035
  title: "CN 2020-0035 Extension of Shortened Trading Hours"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2020-0035.pdf"
  local_path: pdfs/pse-cn-2020-0035.pdf
  edition: historical
  amended_through: 2020-04-13
  note: "Hours to 30 Apr 2020."
- slug: pse-cn-2020-0042
  title: "CN 2020-0042 Shortened Trading Hours Extended to May 15, 2020"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2020-0042.pdf"
  local_path: pdfs/pse-cn-2020-0042.pdf
  edition: historical
  amended_through: 2020-04-27
  note: "Hours to 15 May 2020."
- slug: pse-cn-2020-0044
  title: "CN 2020-0044 Amendment of Circuit Breaker Rules"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2020-0044.pdf"
  local_path: pdfs/pse-cn-2020-0044.pdf
  edition: in-force
  amended_through: 2020-04-29
  note: "Three-phase circuit breaker (10/15/20% -> 15/30/60 min) from 4 May 2020."
- slug: pse-cn-2021-0059
  title: "CN 2021-0059 Adjustments in Trading Hours"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2021-0059.pdf"
  local_path: pdfs/pse-cn-2021-0059.pdf
  edition: historical
  amended_through: 2021-11-22
  note: "Return to full-day schedule from 6 Dec 2021."
- slug: pse-cn-2022-0004
  title: "CN 2022-0004 Shortened Trading Hours (Omicron)"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2022-0004.pdf"
  local_path: pdfs/pse-cn-2022-0004.pdf
  edition: historical
  amended_through: 2022-01-11
  note: "14-31 Jan 2022 hours."
- slug: pse-implementing-guidelines-trading-rules
  title: "Implementing Guidelines of the PSE Revised Trading Rules"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://www.pse.com.ph/ (Regulations > Trading Rules)"
  local_path: pdfs/pse-implementing-guidelines-trading-rules.pdf
  edition: superseded
  amended_through: undated
  note: "Archived by another researcher; undated version (pre-2020 thresholds)."
- slug: pse-daily-quotation-report-file-spec-2016
  title: "Daily Quotation Report File Specifications v1.0"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "n/a"
  local_path: pdfs/pse-daily-quotation-report-file-spec-2016.pdf
  edition: historical
  amended_through: 2016-12-21
  note: "Does not define Bid/Ask."
- slug: pse-weekly-report-2023-06-02
  title: "PSE Weekly Report, week ended 2 June 2023 (wk22)"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2023/06/page01_PSEWeeklyReport2023_wk22.pdf (URL pattern; see index)"
  local_path: pdfs/pse-weekly-report-2023-06-02.pdf
  edition: historical
  amended_through: 2023-06-02
  note: "Contains 31 May 2023 MSCI day (PHP 24.5bn, foreign 81%)."
- slug: pse-weekly-report-2026-10-02
  title: "PSE Weekly Report, week ended 2 October 2026 (wk40)"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2026/10/page01_PSEWeeklyReport2026_wk40.pdf"
  local_path: pdfs/pse-weekly-report-2026-10-02.pdf
  edition: in-force
  amended_through: 2026-10-02
  note: "Latest weekly data; YTD high/low, foreign activity."
- slug: pse-eod-daily-quotation-2026-10-02
  title: "PSE Daily Quotation Report, 2 October 2026"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/market_report/October 02, 2026-EOD.pdf"
  local_path: pdfs/pse-eod-daily-quotation-2026-10-02.pdf
  edition: in-force
  amended_through: 2026-10-02
  note: "Archived by another researcher; block-sale and VWAP lines on p11."
- slug: pse-eod-daily-quotation-2024-05-24
  title: "PSE Daily Quotation Report, 24 May 2024"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/market_report/May 24, 2024-EOD.pdf"
  local_path: pdfs/pse-eod-daily-quotation-2024-05-24.pdf
  edition: historical
  amended_through: 2024-05-24
  note: "FX rate and format example."
- slug: pse-market-reports-index
  title: "PSE Market Reports index (Monthly, Weekly, Daily Quotation, Infographic, Investor Profile)"
  publisher: "Philippine Stock Exchange"
  type: dataset
  canonical_url: "https://www.pse.com.ph/market-report/"
  local_path: null
  edition: in-force
  amended_through: undated
  note: "Script-rendered table; enumerated via the site's posts-table AJAX endpoint (1,732 entries). Individual files at documents.pse.com.ph/market_report/."
- slug: pse-weekly-reports-dataset
  title: "PSE Weekly Reports 2019-05-03 to 2026-10-02 (391 one-page PDFs) - parsed daily PSEi OHLC, value, trades, foreign activity"
  publisher: "Philippine Stock Exchange"
  type: dataset
  canonical_url: "https://www.pse.com.ph/market-report/ (category Weekly Report)"
  local_path: null
  edition: in-force
  amended_through: 2026-10-02
  note: "Own parse (1,813 daily rows); reproduces PSE ADVT for 2021-2025 exactly. Only two weeks archived individually."
- slug: pse-dqr-dataset
  title: "PSE Daily Quotation Reports - 373 parsed days: 176 sampled days (2 per month Jun 2019-Sep 2026), 28 consecutive days 26 Aug-5 Oct 2026, 164 month-end/month-start sessions (Jan 2024-Sep 2026) and 26 event days (27 Dec 2019-15 Jun 2026)"
  publisher: "Philippine Stock Exchange"
  type: dataset
  canonical_url: "https://documents.pse.com.ph/market_report/<Month DD, YYYY>-EOD.pdf"
  local_path: null
  edition: in-force
  amended_through: 2026-10-05
  note: "Own parse (per-stock bid/ask/OHLC/volume/value/net foreign; odd-lot, block, VWAP summary). Only the individually cited reports are archived; the rest are described by URL pattern and date."
- slug: pse-press-2025-12-29
  title: "PSE marks last trading day of 2025"
  publisher: "Philippine Stock Exchange (press room)"
  type: web
  canonical_url: "https://corporate.pse.com.ph/?p=17546"
  local_path: null
  edition: historical
  amended_through: 2025-12-29
  note: "Year-end statistics; CEO quote."
- slug: pse-press-2024-12-27
  title: "PSEi closes trading year at 6.5K level"
  publisher: "Philippine Stock Exchange (press room)"
  type: web
  canonical_url: "https://corporate.pse.com.ph/?p=16717"
  local_path: null
  edition: historical
  amended_through: 2024-12-27
  note: "2024 year-end statistics."
- slug: pse-press-2025-06-09
  title: "Stock market accounts breach 2M mark"
  publisher: "Philippine Stock Exchange (press room)"
  type: web
  canonical_url: "https://corporate.pse.com.ph/?p=16996"
  local_path: null
  edition: historical
  amended_through: 2025-06-09
  note: "2024 account statistics, avg trade sizes, 16% retail share quote."
- slug: pse-investing-page
  title: "Investing at PSE (board lot table, trading hours, thresholds, surveillance FAQ)"
  publisher: "Philippine Stock Exchange"
  type: web
  canonical_url: "https://www.pse.com.ph/investing-at-pse/"
  local_path: null
  edition: in-force
  amended_through: undated
  note: "Accessed 6 Oct 2026."
- slug: bw-14232
  title: "PSEi rallies by 0.71% on 'window dressing'"
  publisher: "BusinessWorld"
  type: web
  canonical_url: "https://bworldonline.com/stock-market/2017/07/01/14232/psei-rallies-0-71-window-dressing/"
  local_path: null
  edition: n/a
  amended_through: 2017-07-01
  note: "Secondary; headline/snippet via WP REST API."
- slug: bw-238977
  title: "PSEi rebounds on month-end window dressing"
  publisher: "BusinessWorld"
  type: web
  canonical_url: "https://bworldonline.com/editors-picks/2019/06/27/238977/psei-rebounds-on-month-end-window-dressing/"
  local_path: null
  edition: n/a
  amended_through: 2019-06-27
  note: "Secondary."
- slug: bw-526114
  title: "PSEi drops further on month-end window dressing"
  publisher: "BusinessWorld"
  type: web
  canonical_url: "https://bworldonline.com/stock-market/2023/05/31/526114/psei-drops-further-on-month-end-window-dressing/"
  local_path: null
  edition: n/a
  amended_through: 2023-05-31
  note: "Secondary; 31 May 2023 MSCI day."
- slug: bw-548526
  title: "Shares up on window dressing, increased buying"
  publisher: "BusinessWorld"
  type: web
  canonical_url: "https://bworldonline.com/stock-market/2023/09/28/548526/shares-up-on-window-dressing-increased-buying/"
  local_path: null
  edition: n/a
  amended_through: 2023-09-28
  note: "Secondary."
- slug: bw-421693
  title: "Stock exchange trading halted due to technical glitch"
  publisher: "BusinessWorld"
  type: web
  canonical_url: "https://bworldonline.com/top-stories/2022/01/05/421693/stock-exchange-trading-halted-due-to-technical-glitch/"
  local_path: null
  edition: n/a
  amended_through: 2022-01-05
  note: "Secondary; full text read. 4 Jan 2022 cancellation: 43 of 125 TPs unable to connect."
- slug: bw-421594
  title: "Trading glitch unlikely to shake index - analyst"
  publisher: "BusinessWorld"
  type: web
  canonical_url: "https://bworldonline.com/stock-market/2022/01/04/421594/trading-glitch-unlikely-to-shake-index-analyst/"
  local_path: null
  edition: n/a
  amended_through: 2022-01-04
  note: "Secondary; full text read."
- slug: bw-567311
  title: "PSE told to explain trading halts much sooner"
  publisher: "BusinessWorld"
  type: web
  canonical_url: "https://bworldonline.com/corporate/2024/01/08/567311/pse-told-to-explain-trading-halts-much-sooner/"
  local_path: null
  edition: n/a
  amended_through: 2024-01-08
  note: "Secondary; full text read. 3 Jan 2024 halt 09:32-11:55."
- slug: bw-661247
  title: "Philippine stock market starts trading after delayed open"
  publisher: "BusinessWorld (Bloomberg)"
  type: web
  canonical_url: "https://bworldonline.com/bloomberg/2025/03/24/661247/philippine-stock-market-starts-trading-after-delayed-open/"
  local_path: null
  edition: n/a
  amended_through: 2025-03-24
  note: "Secondary; full text read. 24 Mar 2025 open delayed to 11:10."
- slug: bw-661414
  title: "PHL stock exchange's tech glitches may dent foreign investor confidence"
  publisher: "BusinessWorld"
  type: web
  canonical_url: "https://bworldonline.com/top-stories/2025/03/25/661414/phl-stock-exchanges-tech-glitches-may-dent-foreign-investor-confidence/"
  local_path: null
  edition: n/a
  amended_through: 2025-03-25
  note: "Secondary; full text read."
- slug: gnews-inquirer-2026-05-29
  title: "PSEi sinks to 5,700 level as MSCI reshuffle spark sell-off (headline via Google News RSS)"
  publisher: "Inquirer.net"
  type: web
  canonical_url: "https://news.google.com/rss/search?q=MSCI+rebalancing+PSE+trading+value+record+stocks"
  local_path: null
  edition: n/a
  amended_through: 2026-05-29
  note: "Headline only."
- slug: gnews-bw-2025-08-31
  title: "Ayala Land shares rise on MSCI rebalancing, foreign inflows (headline via Google News RSS)"
  publisher: "BusinessWorld"
  type: web
  canonical_url: "https://news.google.com/rss/search?q=MSCI+rebalancing+PSE+trading+value+record+stocks"
  local_path: null
  edition: n/a
  amended_through: 2025-08-31
  note: "Headline only."
- slug: gnews-mb-2025-08-20
  title: "PSE can now cancel trading due to disasters or glitches (headline via Google News RSS)"
  publisher: "Manila Bulletin"
  type: web
  canonical_url: "https://news.google.com/rss/search?q=PSE+trading+halted+technical+glitch"
  local_path: null
  edition: n/a
  amended_through: 2025-08-20
  note: "Headline only."
- slug: gnews-inquirer-2026-09-28
  title: "PSEi falls below 5,800 on renewed US-Iran fears (headline via Google News RSS)"
  publisher: "Inquirer.net"
  type: web
  canonical_url: "https://news.google.com/rss/search?q=PSEi+plunge+foreign+selling+September+2026"
  local_path: null
  edition: n/a
  amended_through: 2026-09-28
  note: "Headline only."
- slug: philstar-2026-02-05-villar
  title: "Battle royale - SEC vs Manny Villar (opinion)"
  publisher: "Philstar.com"
  type: web
  canonical_url: "https://www.philstar.com/opinion/2026/02/05/2505766/battle-royale-sec-vs-manny-villar"
  local_path: null
  edition: n/a
  amended_through: 2026-02-05
  note: "Secondary; opinion column (Tony Lopez) read in full via direct fetch; relays SEC allegations against Villar Land Holdings (HVN); not a court finding."
- slug: inq-biz-buzz-calata
  title: "Biz Buzz - Probing Calata"
  publisher: "Inquirer"
  type: web
  canonical_url: "https://business.inquirer.net/74459/biz-buzz-probing-calata/amp"
  local_path: null
  edition: n/a
  amended_through: undated
  note: "Secondary; snippet only; date not established."
- slug: paper-rufino-delfino-2016-dow
  title: "Day-of-the-Week Effects in the Philippine Stock Exchange: Do They Exist Amid Modernization?"
  publisher: "DLSU Business & Economics Review 25(2) (Rufino and Delfino)"
  type: paper
  canonical_url: "https://animorepository.dlsu.edu.ph/ber/vol25/iss2/5"
  local_path: pdfs/paper-rufino-delfino-2016-dow.pdf
  edition: n/a
  amended_through: undated
  note: "Archived from the Wayback Machine copy of the DLSU repository PDF (original host returns 403 to scripts). Physical pages cited Year: 2016."
- slug: paper-calderon-2002-demutualization
  title: "A Study of the Demutualization of the Philippine Stock Exchange and its Effect on Stock Return Volatility"
  publisher: "DLSU Business & Economics Review 13(2) (Calderon)"
  type: paper
  canonical_url: "https://animorepository.dlsu.edu.ph/ber/vol13/iss2/2"
  local_path: pdfs/paper-calderon-2002-demutualization.pdf
  edition: n/a
  amended_through: undated
  note: "Archived from Wayback copy; student-level event study, low evidentiary weight Year: 2002."
- slug: paper-almonares-2019-markov
  title: "Markov Switching Model of Philippine Stock Market Volatility"
  publisher: "DLSU Business & Economics Review (Almonares)"
  type: paper
  canonical_url: "https://doi.org/10.59588/2243-786x.1532"
  local_path: null
  edition: n/a
  amended_through: undated
  note: "Abstract only (via OpenAlex); full text not retrievable (repository 403, not in Wayback) Year: 2019."
- slug: paper-camba-camba-2020-random-walk
  title: "The Existence of Random Walk in the Philippine Stock Market: Evidence from Unit Root and Variance-Ratio Tests"
  publisher: "Journal of Asian Finance, Economics and Business 7(10) (Camba and Camba)"
  type: paper
  canonical_url: "https://doi.org/10.13106/jafeb.2020.vol7.no10.523"
  local_path: null
  edition: n/a
  amended_through: 2020-10-01
  note: "Abstract only (via OpenAlex); koreascience PDF host unreachable."
- slug: paper-sullivan-unite-1999-ipo
  title: "The Underpricing of Initial Public Offerings in the Philippines from 1987 to 1997"
  publisher: "Review of Pacific Basin Financial Markets and Policies (Sullivan and Unite)"
  type: paper
  canonical_url: "https://doi.org/10.1142/s0219091599000163"
  local_path: null
  edition: n/a
  amended_through: undated
  note: "Abstract only (via OpenAlex); full text not retrieved Year: 1999."
- slug: paper-rahman-ermawati-2020-herding
  title: "An Analysis of Herding Behavior in the Stock Market: A Case Study of the ASEAN-5 and the United States"
  publisher: "Bulletin of Monetary Economics and Banking 23(3) (Rahman and Ermawati)"
  type: paper
  canonical_url: "https://doi.org/10.21098/bemp.v23i3.1362"
  local_path: pdfs/paper-rahman-ermawati-2020-herding.pdf
  edition: n/a
  amended_through: 2020-10-30
  note: "Open access PDF from bmeb-bi.org."
- slug: paper-pamplona-2023-herd
  title: "Influence of Retail Investors' Learning Behavior on Herd Bias: An Analysis of Philippine Stock Trading"
  publisher: "International Journal of Research Publications (Pamplona)"
  type: paper
  canonical_url: "https://www.ijrp.org/filePermission/fileDownlaod/4/97d5350a91467d0bab16a6fa6d860866/2"
  local_path: null
  edition: n/a
  amended_through: undated
  note: "Abstract only (via OpenAlex); full text not retrieved Year: 2023."
- slug: paper-unite-2002-integration
  title: "The Effect of Capital Market Liberalization Measures on the Integration of the Philippine Stock Market with International Markets"
  publisher: "DLSU Business & Economics Review (Unite)"
  type: paper
  canonical_url: "https://animorepository.dlsu.edu.ph/cgi/viewcontent.cgi?article=1386&context=ber"
  local_path: null
  edition: n/a
  amended_through: undated
  note: "Abstract only (via OpenAlex); full text not retrieved."
- slug: pse-eod-daily-quotation-2026-09-17
  title: "PSE Daily Quotation Report, 17 September 2026"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/market_report/September 17, 2026-EOD.pdf"
  local_path: pdfs/pse-eod-daily-quotation-2026-09-17.pdf
  edition: historical
  amended_through: 2026-09-17
  note: "SM PHP 16.8bn print (73% of regular value); VWAP and block-sale lines on p11."
- slug: pse-dqr-2026-08-28
  title: "PSE Daily Quotation Report, 28 August 2026"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/market_report/August 28, 2026-EOD.pdf"
  local_path: pdfs/pse-dqr-2026-08-28.pdf
  edition: historical
  amended_through: 2026-08-28
  note: "MSCI review day; ALI and ICT dominate; VWAP and block lines on p11."
- slug: pse-eod-daily-quotation-2026-09-11
  title: "PSE Daily Quotation Report, 11 September 2026"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/market_report/September 11, 2026-EOD.pdf"
  local_path: pdfs/pse-eod-daily-quotation-2026-09-11.pdf
  edition: historical
  amended_through: 2026-09-11
  note: "Block sales PHP 26.9bn (First Gen PHP 25.8bn); block table p11."
- slug: pse-eod-daily-quotation-2026-09-30
  title: "PSE Daily Quotation Report, 30 September 2026"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/market_report/September 30, 2026-EOD.pdf"
  local_path: pdfs/pse-eod-daily-quotation-2026-09-30.pdf
  edition: historical
  amended_through: 2026-09-30
  note: "ABG at lower static threshold (-30%, no bid) on p3."
- slug: pse-eod-daily-quotation-2025-10-24
  title: "PSE Daily Quotation Report, 24 October 2025"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/market_report/October 24, 2025-EOD.pdf"
  local_path: pdfs/pse-eod-daily-quotation-2025-10-24.pdf
  edition: historical
  amended_through: 2025-10-24
  note: "Block sales PHP 19.3bn incl. SMC2J/SMC2K prints; block table p12."
- slug: pse-dqr-2025-05-30
  title: "PSE Daily Quotation Report, 30 May 2025"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/market_report/May 30, 2025-EOD.pdf"
  local_path: pdfs/pse-dqr-2025-05-30.pdf
  edition: historical
  amended_through: 2025-05-30
  note: "MSCI day: regular 15.55bn + block 24.47bn; block table p12."
- slug: pse-eod-daily-quotation-2023-09-26
  title: "PSE Daily Quotation Report, 26 September 2023"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/market_report/September 26, 2023-EOD.pdf"
  local_path: pdfs/pse-eod-daily-quotation-2023-09-26.pdf
  edition: historical
  amended_through: 2023-09-26
  note: "Block sales PHP 29.3bn (MPI crosses); block table p12."
- slug: pse-eod-daily-quotation-2023-06-16
  title: "PSE Daily Quotation Report, 16 June 2023"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/market_report/June 16, 2023-EOD.pdf"
  local_path: pdfs/pse-eod-daily-quotation-2023-06-16.pdf
  edition: historical
  amended_through: 2023-06-16
  note: "BPI block PHP 34.6bn+; block table p11."
- slug: pse-eod-daily-quotation-2022-12-14
  title: "PSE Daily Quotation Report, 14 December 2022"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/market_report/December 14, 2022-EOD.pdf"
  local_path: pdfs/pse-eod-daily-quotation-2022-12-14.pdf
  edition: historical
  amended_through: 2022-12-14
  note: "Eagle Cement crosses; block sales PHP 110.9bn; block table p11."
- slug: pse-eod-daily-quotation-2020-03-19
  title: "PSE Daily Quotation Report, 19 March 2020"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/market_report/March 19, 2020-EOD.pdf"
  local_path: pdfs/pse-eod-daily-quotation-2020-03-19.pdf
  edition: historical
  amended_through: 2020-03-19
  note: "Reopening session after the 17-18 Mar closure; per-stock OHLC, value and net foreign (p1-6)."
- slug: pse-eod-daily-quotation-2021-12-16
  title: "PSE Daily Quotation Report, 16 December 2021"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/market_report/December 16, 2021-EOD.pdf"
  local_path: pdfs/pse-eod-daily-quotation-2021-12-16.pdf
  edition: historical
  amended_through: 2021-12-16
  note: "Aboitiz Power block PHP 73.6bn+; block table p10."
- slug: pse-asm-2020-presidents-report
  title: "PSE Annual Stockholders' Meeting 2020 - President's Report (2 November 2020)"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/4/2021/07/ASM2020-Presidents-Report-for-IR-Microsite.pdf"
  local_path: pdfs/pse-asm-2020-presidents-report.pdf
  edition: historical
  amended_through: 2020-11-02
  note: "PSEi and indicators to 30 Oct 2020 (p3-4); pandemic measures (p5). Date printed on slide 1."
- slug: pse-asm-2021-presidents-report
  title: "PSE Annual Stockholders' Meeting 2021 - President's Report (2 July 2021)"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/4/2021/07/Presidents-Report-2.pdf"
  local_path: pdfs/pse-asm-2021-presidents-report.pdf
  edition: historical
  amended_through: 2021-07-02
  note: "FY2020 and 1H21: retail vs institutional (p4), local vs foreign and net foreign (p5), capital raised (p6). Date printed on slide 1."
- slug: pse-asm-2022-presidents-report
  title: "PSE Annual Stockholders' Meeting 2022 - President's Report"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/4/2022/08/PSE-ASM-2022-PRESIDENTS-REPORT-final.pdf"
  local_path: pdfs/pse-asm-2022-presidents-report.pdf
  edition: historical
  amended_through: undated
  note: "FY2021 and 7M22 (data to 31 Jul 2022; capital raised to 3 Aug 2022): ADVT, market cap and retail vs institutional (p4), local vs foreign and net foreign (p5), capital raised (p6), accounts 2016-21 (p8). Image slides; values read from the rendered pages."
- slug: pse-asm-2023-presidents-report
  title: "PSE Annual Stockholders' Meeting 2023 - President's Report"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/4/2023/08/ASM-2023-PRESIDENTS-REPORT-final-v2.pdf"
  local_path: pdfs/pse-asm-2023-presidents-report.pdf
  edition: historical
  amended_through: undated
  note: "FY2022 and 7M23 (data to 31 Jul 2023): retail vs institutional (p6), local vs foreign and net foreign (p7), accounts incl. non-online and average online ticket (p10)."
- slug: pse-asm-2024-presidents-report
  title: "PSE Annual Stockholders' Meeting 2024 - President's Report"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/4/2024/07/FINAL_PSE-ASM-2024-PRESIDENT_S-REPORT.pdf"
  local_path: pdfs/pse-asm-2024-presidents-report.pdf
  edition: historical
  amended_through: 2024-07-06
  note: "Archived by another researcher; local/foreign and retail/institutional shares for 2022-1H24 on p6."
- slug: pse-asm-2025-presidents-report
  title: "PSE Annual Stockholders' Meeting 2025 - President's Report"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/4/2025/07/PSE-ASM-2025-PRESIDENT_S-REPORT-FINAL-v2.pdf"
  local_path: pdfs/pse-asm-2025-presidents-report.pdf
  edition: historical
  amended_through: 2025-07-12
  note: "Archived by another researcher; 2024-1H25 shares and net foreign flows on p7."
- slug: pse-itch-equities-feed-spec-v2-3
  title: "PSE Equities Feed Specification for X-stream (ITCH) v2.3"
  publisher: "Philippine Stock Exchange / OMX Technology AB"
  type: pdf
  canonical_url: "https://www.pse.com.ph/psetrade-xts/ (ITCH tab)"
  local_path: pdfs/pse-itch-equities-feed-spec-v2-3.pdf
  edition: superseded
  amended_through: undated
  note: "Archived by another researcher; copyright 2014. Broker-ID messages (p15), broker anonymity (p25), auction event types (p26)."
- slug: bw-283531
  title: "Stocks plummet on coronavirus fears"
  publisher: "BusinessWorld"
  type: web
  canonical_url: "https://bworldonline.com/editors-picks/2020/03/13/283531/stocks-plummet-on-coronavirus-fears/"
  local_path: null
  edition: n/a
  amended_through: 2020-03-13
  note: "Secondary; full text read via BusinessWorld WP REST API. 12 Mar 2020 -9.71%, circuit breaker."
- slug: bw-283559
  title: "SSS, GSIS directed to prop up PSE with more equities purchases"
  publisher: "BusinessWorld"
  type: web
  canonical_url: "https://bworldonline.com/editors-picks/2020/03/13/283559/sss-gsis-directed-to-prop-up-pse-with-more-equities-purchases/"
  local_path: null
  edition: n/a
  amended_through: 2020-03-13
  note: "Secondary; full text read."
- slug: bw-284527
  title: "Shares plummet as trading resumes after halt"
  publisher: "BusinessWorld"
  type: web
  canonical_url: "https://bworldonline.com/editors-picks/2020/03/19/284527/shares-plummet-as-trading-resumes-after-halt/"
  local_path: null
  edition: n/a
  amended_through: 2020-03-19
  note: "Secondary; full text read. Reopening day 19 Mar 2020: -13.34%, intraday -24.29%."
- slug: bw-418099
  title: "PHL stocks rise on bargain hunting, BSP decision"
  publisher: "BusinessWorld"
  type: web
  canonical_url: "https://bworldonline.com/stock-market/2021/12/16/418099/phl-stocks-rise-on-bargain-hunting-bsp-decision/"
  local_path: null
  edition: n/a
  amended_through: 2021-12-16
  note: "Secondary; full text read. Value PHP 87.52bn; prints net foreign buying as 'P79.44 million' (PSE figure is in PHP thousands = PHP 79.4bn)."
- slug: bw-493205
  title: "San Miguel unit completes tender offer of Eagle Cement"
  publisher: "BusinessWorld"
  type: web
  canonical_url: "https://bworldonline.com/corporate/2022/12/15/493205/san-miguel-unit-completes-tender-offer-of-eagle-cement/"
  local_path: null
  edition: n/a
  amended_through: 2022-12-15
  note: "Secondary; full text read. Special block sale on 14 Dec 2022."
- slug: bw-525845
  title: "Philippine shares fall ahead of MSCI rebalancing"
  publisher: "BusinessWorld"
  type: web
  canonical_url: "https://bworldonline.com/stock-market/2023/05/30/525845/philippine-shares-fall-ahead-of-msci-rebalancing/"
  local_path: null
  edition: n/a
  amended_through: 2023-05-30
  note: "Secondary; full text read."
- slug: bw-546877
  title: "Pangilinan eyes listing of tollways unit, Maynilad"
  publisher: "BusinessWorld"
  type: web
  canonical_url: "https://bworldonline.com/corporate/2023/09/21/546877/pangilinan-eyes-listing-of-tollways-unit-maynilad/"
  local_path: null
  edition: n/a
  amended_through: 2023-09-21
  note: "Secondary; full text read. Mentions MPIC voluntary delisting plan."
- slug: bw-551311
  title: "PSEi inches up on dovish Fed ahead of US data"
  publisher: "BusinessWorld"
  type: web
  canonical_url: "https://bworldonline.com/stock-market/2023/10/12/551311/psei-inches-up-on-dovish-fed-ahead-of-us-data/"
  local_path: null
  edition: n/a
  amended_through: 2023-10-12
  note: "Secondary; headline and lead sentence only ('last-minute selling trimmed gains')."
- slug: bw-598985
  title: "MSCI rebalancing, foreign selling drop BDO shares"
  publisher: "BusinessWorld"
  type: web
  canonical_url: "https://bworldonline.com/corporate/2024/06/03/598985/msci-rebalancing-foreign-selling-drop-bdo-shares/"
  local_path: null
  edition: n/a
  amended_through: 2024-06-03
  note: "Secondary; headline and lead only."
- slug: bw-620502
  title: "PSEi loses steam before close on profit taking"
  publisher: "BusinessWorld"
  type: web
  canonical_url: "https://bworldonline.com/stock-market/2024/09/10/620502/psei-loses-steam-before-close-on-profit-taking/"
  local_path: null
  edition: n/a
  amended_through: 2024-09-10
  note: "Secondary; headline and lead only."
- slug: bw-640643
  title: "Philippine stocks rebound on last-minute buying"
  publisher: "BusinessWorld"
  type: web
  canonical_url: "https://bworldonline.com/stock-market/2024/12/10/640643/philippine-stocks-rebound-on-last-minute-buying/"
  local_path: null
  edition: n/a
  amended_through: 2024-12-10
  note: "Secondary; headline and lead only."
- slug: bw-641856
  title: "PSEi pares early losses to end flat before Fed, BSP"
  publisher: "BusinessWorld"
  type: web
  canonical_url: "https://bworldonline.com/stock-market/2024/12/16/641856/psei-pares-early-losses-to-end-flat-before-fed-bsp/"
  local_path: null
  edition: n/a
  amended_through: 2024-12-16
  note: "Secondary; headline and lead only."
- slug: bw-647194
  title: "PSEi falls to near 7-month low after late selloff"
  publisher: "BusinessWorld"
  type: web
  canonical_url: "https://bworldonline.com/stock-market/2025/01/16/647194/psei-falls-to-near-7-month-low-after-late-selloff/"
  local_path: null
  edition: n/a
  amended_through: 2025-01-16
  note: "Secondary; full text read. 16 Jan 2025: high 6,419.26, closed at session low 6,265.52 after last-minute profit taking."
- slug: bw-676401
  title: "JFC shares fall after divesting stake in C-Joy Poultry Realty, MSCI rebalancing"
  publisher: "BusinessWorld"
  type: web
  canonical_url: "https://bworldonline.com/corporate/2025/06/02/676401/jfc-shares-fall-after-divesting-stake-in-c-joy-poultry-realty-msci-rebalancing/"
  local_path: null
  edition: n/a
  amended_through: 2025-06-02
  note: "Secondary; excerpt read."
- slug: bw-753259
  title: "Ayala Corp. slides after MSCI changes, macro pressures"
  publisher: "BusinessWorld"
  type: web
  canonical_url: "https://bworldonline.com/corporate/2026/06/01/753259/ayala-corp-slides-after-msci-changes-macro-pressures/"
  local_path: null
  edition: n/a
  amended_through: 2026-06-01
  note: "Secondary; excerpt read; sell-side quote that rebalancing selling concentrates in the closing auction."
- slug: paper-camba-camba-2020-covid
  title: "The Effect of COVID-19 Pandemic on the Philippine Stock Exchange, Peso-Dollar Rate and Retail Price of Diesel"
  publisher: "Journal of Asian Finance, Economics and Business 7(10) (Camba and Camba)"
  type: paper
  canonical_url: "https://doi.org/10.13106/jafeb.2020.vol7.no10.543"
  local_path: null
  edition: n/a
  amended_through: 2020-10-01
  note: "Abstract only (via OpenAlex)."
- slug: paper-pinili-murcia-2023-covid-breakpoints
  title: "COVID-19 Pandemic Events and Philippine Stock Market Performance: Testing for Multiple Breakpoints"
  publisher: "European Journal of Economic and Financial Research 7(3) (Pinili and Murcia)"
  type: paper
  canonical_url: "https://doi.org/10.46827/ejefr.v7i3.1543"
  local_path: null
  edition: n/a
  amended_through: undated
  note: "Abstract only (via OpenAlex) Year: 2023."
- slug: paper-atento-2026-size-premium
  title: "Value and Size Premiums in the Philippine Equity Market: Evidence from an Extended Dataset with Volatility Analysis"
  publisher: "Asian Financial Economics and Policy (Atento et al.)"
  type: paper
  canonical_url: "https://doi.org/10.65166/nbsg0j88"
  local_path: null
  edition: n/a
  amended_through: undated
  note: "Abstract only (via OpenAlex); publication date inferred as 2026 from OpenAlex record Year: 2026."
- slug: paper-briones-2017-stock-market-development
  title: "Stock Market Development in the Philippines: Past and Present"
  publisher: "Journal of Philippine Development 41-42 (Briones)"
  type: paper
  canonical_url: "https://doi.org/10.62986/pjd2016.41-42.1-2f"
  local_path: null
  edition: n/a
  amended_through: undated
  note: "Abstract only (via OpenAlex) Year: 2017."
- slug: paper-dioquino-2014-sicat-case
  title: "Hans Sicat and the Transformation at the Philippine Stock Exchange"
  publisher: "Asian Case Research Journal (Dioquino)"
  type: paper
  canonical_url: "https://doi.org/10.1142/s0218927514500163"
  local_path: null
  edition: n/a
  amended_through: undated
  note: "Abstract only (via OpenAlex); paywalled Year: 2014."
- slug: bir-rr-20-2025-stt
  title: "BIR Revenue Regulations No. 20-2025: rate adjustment of the stock transaction tax under RA 12214 (CMEPA)"
  publisher: "Bureau of Internal Revenue / Department of Finance"
  type: pdf
  canonical_url: "https://www.bir.gov.ph/ (Revenue Regulations 2025; exact URL held by archiving researcher)"
  local_path: pdfs/bir-rr-20-2025-stt.pdf
  edition: in-force
  amended_through: 2025-08-05
  note: "Scanned; archived by another researcher. Date = BIR received/issue stamp 5 Aug 2025 (signed by the Finance Secretary 29 Jul 2025). STT 0.1% of gross selling price on p2; effectivity 1 Jul 2025 on p4."
- slug: bw-336789
  title: "Stock market operator targets 3 IPOs this year"
  publisher: "BusinessWorld"
  type: web
  canonical_url: "https://bworldonline.com/editors-picks/2021/01/04/336789/stock-market-operator-targets-3-ipos-this-year/"
  local_path: null
  edition: n/a
  amended_through: 2021-01-04
  note: "Secondary; full text read. Gives 2020 capital raised PHP 104bn (IPOs 44.3bn, follow-ons 41.2bn, SROs 12.8bn, private placements 5.6bn) vs 101bn in 2019."
- slug: pse-analyst-briefing-3m-2026
  title: "PSE Overview - analyst briefing (3M 2026)"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/4/2026/07/3M-2026-PSE-Analyst-Briefing.pdf"
  local_path: pdfs/pse-analyst-briefing-3m-2026.pdf
  edition: in-force
  amended_through: 2026-03-18
  note: "Archived by another researcher; market data to 17 Mar 2026; e-wallet account statistics on p21."
- slug: pse-nte-broker-forum-2026-07-09
  title: "New Trading Engine - Broker Forum (9 July 2026)"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://www.pse.com.ph/pse-new-trading-engine/ (updates tab)"
  local_path: pdfs/pse-nte-broker-forum-2026-07-09.pdf
  edition: in-force
  amended_through: 2026-07-09
  note: "Archived by another researcher; timeline on p9 (rehearsals 31 Oct, 7 and 14 Nov; go-live 23 Nov 2026); readiness counts p5-6."
- slug: pse-nte-faq-2026-08
  title: "Frequently Asked Questions - New Trading Engine (Aug 2026)"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://www.pse.com.ph/pse-new-trading-engine/ (FAQs tab)"
  local_path: pdfs/pse-nte-faq-2026-08.pdf
  edition: in-force
  amended_through: undated
  note: "Archived by another researcher; p1: no parallel run, big-bang implementation. Document month taken from the archived file name; day not stated."
- slug: pse-psei-factsheet-2025-09
  title: "PSE Index (PSEi) factsheet, data as of end-September 2025"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://www.pse.com.ph/indices/ (factsheet download)"
  local_path: pdfs/pse-psei-factsheet-2025-09.pdf
  edition: superseded
  amended_through: undated
  note: "Archived by another researcher. Data as of end-September 2025; publication date not stated. Weights and index statistics on p2; methodology on p1."
- slug: pse-short-sell-report-2023-11-06
  title: "PSE Daily Short Selling Report, 6 November 2023 (first report)"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2023/11/November-06-2023.pdf"
  local_path: pdfs/pse-short-sell-report-2023-11-06.pdf
  edition: historical
  amended_through: 2023-11-06
  note: "Original file is AES-encrypted with an empty password; the archived copy was re-saved without encryption (content unchanged) so that text extraction works. Totals are on p2."
- slug: pse-short-sell-report-2026-10-05
  title: "PSE Daily Short Selling Report, 5 October 2026 (latest at time of research)"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/wp-content/uploads/sites/15/2026/10/October-05-2026.pdf"
  local_path: pdfs/pse-short-sell-report-2026-10-05.pdf
  edition: in-force
  amended_through: 2026-10-05
  note: "Same re-save note as the first report; all 710 reports from 6 Nov 2023 to 5 Oct 2026 show zero short-sale volume (own parse)."
- slug: pse-memo-extended-trading-proposal-2011
  title: "TPA 2011-0030 Proposed amendment of trading rules in relation to extended trading"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "n/a (PSE memorandum archived by another researcher; URL not recorded)"
  local_path: pdfs/pse-memo-extended-trading-proposal-2011.pdf
  edition: historical
  amended_through: 2011-07-28
  note: "Board approval of 13 Jul 2011; pre-2011 schedule 09:00-12:10; two-phase extension on p1."
- slug: pse-memo-new-trading-hours-2011
  title: "TPA 2011-0108 PSE new trading hours (effective 2 Jan 2012)"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "n/a (PSE memorandum archived by another researcher; URL not recorded)"
  local_path: pdfs/pse-memo-new-trading-hours-2011.pdf
  edition: historical
  amended_through: 2011-12-06
  note: "09:30-12:00 / 13:30-15:30 schedule with 15:17 pre-close; EOD report timing."
- slug: pse-cn-2020-0046
  title: "CN 2020-0046 Shortened trading hours under MECQ"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2020-0046.pdf"
  local_path: pdfs/pse-cn-2020-0046.pdf
  edition: historical
  amended_through: 2020-05-14
  note: "Archived by another researcher; hours 09:30-13:00 continue; trading floor closed."
- slug: pse-cn-2021-0063-half-day-trading-2021-12
  title: "CN 2021-0063 Half-day trading on 24 and 31 December 2021"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2021-0063.pdf"
  local_path: pdfs/pse-cn-2021-0063-half-day-trading-2021-12.pdf
  edition: historical
  amended_through: 2021-12-15
  note: "Archived by another researcher; half-day phases."
- slug: pse-cn-2022-0001-delay-market-opening
  title: "CN 2022-0001 Delay in market opening and trading (4 Jan 2022)"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2022-0001.pdf"
  local_path: pdfs/pse-cn-2022-0001-delay-market-opening.pdf
  edition: historical
  amended_through: 2022-01-04
  note: "Archived by another researcher; 43 of 125 TPs unable to connect; one-third halt rule."
- slug: pse-cn-2022-0002-cancellation-of-trading-2022-01-04
  title: "CN 2022-0002 Cancellation of trading (4 January 2022)"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2022-0002.pdf"
  local_path: pdfs/pse-cn-2022-0002-cancellation-of-trading-2022-01-04.pdf
  edition: historical
  amended_through: 2022-01-04
  note: "Archived by another researcher; NASDAQ engine / Flextrade front-end connection failure."
- slug: pse-cn-2022-0009-trading-schedule-mar-2022
  title: "CN 2022-0009 Trading schedule effective 1 March 2022"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2022-0009.pdf"
  local_path: pdfs/pse-cn-2022-0009-trading-schedule-mar-2022.pdf
  edition: historical
  amended_through: 2022-02-17
  note: "Archived by another researcher (a duplicate slug pse-cn-2022-0009-trading-schedule-mar-2022 also exists); full-day schedule 09:30-12:00, 13:00-15:00."
- slug: pse-cn-2022-0035-trading-suspension-2022-09-26
  title: "CN 2022-0035 Trading suspension (26 September 2022)"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2022-0035.pdf"
  local_path: pdfs/pse-cn-2022-0035-trading-suspension-2022-09-26.pdf
  edition: historical
  amended_through: 2022-09-25
  note: "Archived by another researcher; no PSE trading and no SCCP clearing; reason not stated."
- slug: pse-cn-2024-0001-market-halt
  title: "CN 2024-0001 Market halt (3 January 2024)"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2024-0001.pdf"
  local_path: pdfs/pse-cn-2024-0001-market-halt.pdf
  edition: historical
  amended_through: 2024-01-03
  note: "Archived by another researcher."
- slug: pse-cn-2024-0003-update-market-halt
  title: "CN 2024-0003 Update on the market halt (3 January 2024)"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2024-0003.pdf"
  local_path: pdfs/pse-cn-2024-0003-update-market-halt.pdf
  edition: historical
  amended_through: 2024-01-03
  note: "Archived by another researcher; halted 09:32, resumed 11:56."
- slug: pse-cn-2024-0012-vwap-go-live
  title: "CN 2024-0012 VWAP Trading (go live)"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2024-0012.pdf"
  local_path: pdfs/pse-cn-2024-0012-vwap-go-live.pdf
  edition: historical
  amended_through: 2024-02-15
  note: "Archived by another researcher; launch on 1 March 2024."
- slug: pse-cn-2024-0038-trading-suspension-2024-07-24
  title: "CN 2024-0038 Trading suspension (24 July 2024)"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2024-0038.pdf"
  local_path: pdfs/pse-cn-2024-0038-trading-suspension-2024-07-24.pdf
  edition: historical
  amended_through: 2024-07-24
  note: "Archived by another researcher; inclement weather and floods."
- slug: pse-cn-2024-0061-adjusted-schedule-2024-12-09
  title: "CN 2024-0061 Adjusted trading schedule (9 December 2024)"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2024-0061.pdf"
  local_path: pdfs/pse-cn-2024-0061-adjusted-schedule-2024-12-09.pdf
  edition: historical
  amended_through: 2024-12-09
  note: "Archived by another researcher; open delayed to 09:55."
- slug: pse-cn-2025-0015-adjusted-schedule-2025-03-24
  title: "CN 2025-0015 Adjusted trading schedule (24 March 2025)"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2025-0015.pdf"
  local_path: pdfs/pse-cn-2025-0015-adjusted-schedule-2025-03-24.pdf
  edition: historical
  amended_through: 2025-03-24
  note: "Archived by another researcher; open delayed to 11:10."
- slug: pse-cn-2025-0038-non-trading-day-2025-10-31
  title: "CN 2025-0038 Non-trading day (31 October 2025)"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2025-0038.pdf"
  local_path: pdfs/pse-cn-2025-0038-non-trading-day-2025-10-31.pdf
  edition: historical
  amended_through: 2025-09-24
  note: "Archived by another researcher."
- slug: pse-cn-2025-0043-non-trading-days
  title: "CN 2025-0043 Non-trading days (Dec 2025 - 1 Jan 2026)"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2025-0043.pdf"
  local_path: pdfs/pse-cn-2025-0043-non-trading-days.pdf
  edition: historical
  amended_through: 2025-11-24
  note: "Archived by another researcher."
- slug: pse-cn-2025-0046-board-lot-trading-at-last
  title: "CN 2025-0046 Proposed amendments to the PSE board lot and the rule on trading during run-off/trading-at-last (consultation)"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2025-0046.pdf"
  local_path: pdfs/pse-cn-2025-0046-board-lot-trading-at-last.pdf
  edition: superseded
  amended_through: 2025-12-15
  note: "Archived by another researcher. Proposed tick/lot table p3-4; run-off rejection rule and Eqlipse change p5-8. Proposal only; SEC approval pending as of Jul 2026."
- slug: pse-cn-2025-0028-cmepa-effectivity
  title: "CN 2025-0028 Effectivity of RA 12214 (CMEPA)"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2025-0028.pdf"
  local_path: pdfs/pse-cn-2025-0028-cmepa-effectivity.pdf
  edition: in-force
  amended_through: 2025-06-26
  note: "Archived by another researcher. STT 0.6% to 0.1% from 1 Jul 2025."
- slug: pse-cn-2025-0005
  title: "CN 2025-0005 Results of the review of PSE indices (24 Jan 2025)"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2025-0005.pdf"
  local_path: pdfs/pse-cn-2025-0005.pdf
  edition: superseded
  amended_through: 2025-01-24
  note: "Archived by another researcher. PSEi changes (AREIT, CBC in; NIKL, WLCON out) effective 3 Feb 2025."
- slug: pse-cn-2025-0037
  title: "CN 2025-0037 Amendments to the Revised Trading Rules (market halt trigger), correspondent TP guidelines and natural-disaster guidelines"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2025-0037.pdf"
  local_path: pdfs/pse-cn-2025-0037.pdf
  edition: in-force
  amended_through: 2025-08-20
  note: "Archived by another researcher. Halt trigger now >50% of 6-month ADTV (ex blocks)."
- slug: pse-dqr-2025-01-31
  title: "PSE Daily Quotation Report, 31 January 2025"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/market_report/January 31, 2025-EOD.pdf"
  local_path: pdfs/pse-dqr-2025-01-31.pdf
  edition: historical
  amended_through: 2025-01-31
  note: "Last session before the CBC/AREIT PSEi inclusion; CBC row p1, AREIT p4, WLCON p7."
- slug: bw-650452
  title: "Chinabank shares surge before index comeback"
  publisher: "BusinessWorld"
  type: web
  canonical_url: "https://bworldonline.com/corporate/2025/02/03/650452/chinabank-shares-surge-before-index-comeback/"
  local_path: null
  edition: n/a
  amended_through: 2025-02-03
  note: "Secondary; excerpt read. CBC +33.8% on the week to PHP 93; most actively traded stock that week (PHP 6.51bn)."
- slug: pse-cn-2021-0055-lift-lower-static-threshold-sgp
  title: "CN 2021-0055 Synergy Grid (SGP): lifting of lower static threshold"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2021-0055.pdf"
  local_path: pdfs/pse-cn-2021-0055-lift-lower-static-threshold-sgp.pdf
  edition: historical
  amended_through: 2021-10-27
  note: "Archived by another researcher."
- slug: pse-cn-2021-0057-keepr-lower-static-threshold-lift
  title: "CN 2021-0057 The Keepers Holdings (KEEPR): lifting of lower static threshold"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2021-0057.pdf"
  local_path: pdfs/pse-cn-2021-0057-keepr-lower-static-threshold-lift.pdf
  edition: historical
  amended_through: 2021-11-04
  note: "Archived by another researcher."
- slug: pse-cn-2024-0029-min-commission-removal
  title: "CN 2024-0029 Removal of minimum commission charges (SEC MC 7-2024)"
  publisher: "Philippine Stock Exchange"
  type: pdf
  canonical_url: "https://documents.pse.com.ph/CircularOPSPDF/CN-2024-0029.pdf"
  local_path: pdfs/pse-cn-2024-0029-min-commission-removal.pdf
  edition: historical
  amended_through: 2024-05-17
  note: "Archived by another researcher; SEC MC 7-2024 dated 16 Apr 2024."
```
