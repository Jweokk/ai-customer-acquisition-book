# Chapter 20 How to Know If It's Working: Three Sets of Books and a Holdout Test

It used to be enough to look at one attribution report to judge whether this money was well spent—who brought the click, who brought the conversion, credit goes to them, and the budget follows the number. Now the customer's comparison process on the AI side carries no link, no source, and never enters your backend; the report both misses the real effect and credits some channel with credit that doesn't exist. What you need to do is change the question: stop asking "which conversion should this be credited to" and start asking "what would happen if this money weren't spent," then write that answer as a range you can show your boss and your finance team.

Every method above costs money, and the effect isn't visible on the customer's side—all you have is the books. So this chapter gives you 5 methods to answer to your boss and your finance team with a range.

---

## Method 1: Split one attribution report into four sets of books, each answering only one question

**What to do**: Drop the habit of "using one report to answer every question," split the numbers a decision needs into four sets of books, and state what each set of books is allowed to be used for.

**How**

1. The first set is the attribution report (multi-touch attribution, platform backend). It answers "how do already-happened conversions get allocated"; the data is observational and is only allowed for tactical optimization inside a channel: creative, audience, bids.
2. The second set is self-reported channel research. It answers "how buyers remember they found you"; the data is self-reported and carries systematic bias, so it is only used to see whether the "invisible part's share" is growing or shrinking.
3. The third set is the AI visibility baseline. It answers "do you hold a place at the answer layer"; the data is what you measure yourself, and it is used to judge asset health and decide which sources to fight for first.
4. The fourth set is the incremental experiment. It answers "what would you lose if this money weren't spent"; it is the only one of the four with causal evidence, and only it can decide whether a budget stays or goes.
5. Write down next to the report why attribution fails. First, decisions at the answer layer are digested inside the conversation itself—the user doesn't need to reach your page to get the conclusion. Second, sessions that jump over from AI clients usually carry no usable source information, and land on the page mostly as "direct / no source." Third, conversational research happens entirely outside your analytics system, with no tracking at all. Worse: that small fraction that does carry source information is itself a biased sample—the people willing to click through and the people who take the answer and leave are not the same group. The part that can be measured is often exactly the most biased subset [our judgment].
6. Before every budget meeting, state which set of books this decision uses. The vast majority of misjudgments happen when "the first set of books answers the fourth set's question." Also, label the AI channel's attribution number in the report as "an attribution floor, not the size of the channel," and anyone citing it must also report the self-reported figure.

**Example**: A public analysis from a video infrastructure company (relayed by Derivatex Agency in May 2026) claimed that in one month 27% of new sign-ups self-reported discovering the company through ChatGPT, Perplexity, and Claude, while Google Analytics credited those AI channels with only 0.5% in the same period—a 54-fold gap [third-party verified]. This figure has only been relayed, never traced back to the original analysis, and neither the sample size nor the question wording is known, so read it only as an order of magnitude. On the other side: external media that AI frequently cites get less than 1% of their referral traffic from AI platforms [third-party verified]. Both numbers are right; they aren't answering the same question—27% is "the path the buyer remembers," and 0.5% and 1% are "the path the system can trace."

**Pitfalls**: Reading GA's 0.5% attribution directly as "the AI channel is worth roughly zero," then cutting it in the budget meeting. The conclusion looks data-backed, so no one has to be accountable for it.

## Method 2: Fix the wording of self-reported research so that bias becomes a trend

**What to do**: Run a buyer self-reported channel survey once a month, using fixed wording and a fixed position to lock the bias down, so different months can be compared.

**How**

1. Change the question. Don't ask "how did you hear about us"; ask "before contacting us, which of these things did you do." Self-report answers memory and belonging, not causation—the most recent and most face-saving touchpoint is easier to recall, email and offline events are easily forgotten, the more "insider" answer is easier to give, and what position the question sits in the form, single- or multi-select, and whether sales fills it in for them all directly change the answer distribution. Calibration isn't eliminating the bias, it's fixing it in place.
2. Options should be multi-select, open, and non-leading, and must include "asked an AI assistant," split by platform: ChatGPT, Doubao, DeepSeek, Kimi, Yuanbao, Perplexity, WeChat Search.
3. There is a measured reason to split platforms: only 11% of domains are cited by both ChatGPT and Perplexity [third-party verified]. Counting "AI search" as one channel amounts to adding two completely different behaviors together.
4. Account for the three kinds of touchpoints separately and don't force single-touch attribution: the same buyer can be recorded both as "asked AI" and as "read a third-party review"; when analyzing, produce numbers under both a first-touch and a last-touch convention, each labeled.
5. Weight by strata. Survey response rates differ by channel; large accounts almost never fill in forms, so weight by response rate, or at least report numbers by customer stratum rather than merging them into one total percentage.
6. Set two calibration anchors, with fixed frequency and position: the change in branded terms and direct site visits, and the relative change in competitive-term bid cost. If the self-reported AI share is rising while branded direct visits stay flat, it is mostly recall bias; only when the two move in the same direction can it be treated as a trend. Same questions, same position, same order every month; a single month's number does not enter a budget decision.

**Example**: The payments company Fiska built its own attribution with "form self-reported channel + UTM"; reporting says its leads from large models rose from 3 a month to 14, more than 50% of total leads [vendor claim]. The value of this case isn't in the numbers but in the act of "building your own ruler."

**Pitfalls**: Making the survey a single-select dropdown at the end of the form, collapsed by default, with options only "search engine / social media / friend referral / other"—"asked AI" gets filed under "other," the self-reported figure can come out even lower than GA's, and the team concludes from this that "customers themselves don't even remember the AI channel." Survey design alone can create error of more than tenfold, and it never shows up in any data-quality report.

## Method 3: Build your own visibility baseline table and test the core questions monthly

**What to do**: Using a fixed set of buyer questions and fixed entry points, measure for yourself "what AI says about us now"—build the table once, reuse it long term.

**How**

1. First define the question set: the 30–60 questions buyers ask most, in four categories—awareness, comparison, risk, and selection—with 5 fixed "must be mentioned" hard questions.
2. Then define the entry points, setting priority by where your customers are, not chasing full coverage: overseas, ChatGPT, Google AI Overviews, Perplexity; in Chinese, Doubao, DeepSeek, Kimi, Yuanbao.
3. Each record must keep at least these fields: test date, whether the brand was mentioned, what position it ranked, in what context it was mentioned (recommendation / comparison / risk warning), which third-party domains were cited, the share of parameters and credentials described incorrectly, which direct competitors also appeared in the same question, and whether running the same question 3 times produced consistent results.
4. Fix the frequency: test the 10 core questions every month and all the questions every quarter.
5. Fix the test discipline: open a fresh environment with no history, fix the time window and region, copy the questions verbatim without "optimizing" them, and run each one 3 times.
6. Use a set of current-state data to calibrate expectations, only to judge what counts as normal, not as a target: one in-house measurement, an analysis report covering 14,750 buyer questions across four platforms, found an overall brand citation rate of 14.0%, with 53% of brands completely absent on questions in their own category; by industry, finance and insurance 2.1%, legal and professional services 86% never cited [vendor claim]. The gaps between platforms are even more extreme: ChatGPT cites a specific brand in only 0.59% of answers, Perplexity 13.05%, and Grok 27% [third-party verified].

**Example**: Our own measurement used 6 real procurement questions, asked twice through each of 5 model channels (A–E), yielding 51 valid answers: asking the same model twice in a row, the overlap of the lists was only 22%–56%; switching to another model, only 4%–21% [our own measurement]. Another industry analysis notes that 40%–60% of cited sources get swapped out every month [third-party verified]—so a single sample isn't a conclusion; "we got recommended this month" is not an asset, "consistently cited for six straight months" is.

**Pitfalls**: Drawing a rising "we got recommended by ChatGPT" curve in the weekly report. Single platform, single run, single question, paired with a monthly 40–60% turnover, amounts to drawing noise as a trend. Worse is tying visibility to bonuses—a manipulable metric will be manipulated; buying mentions and fake reviews can push the number up short term while pushing the trust asset down, and the part that falls doesn't show up in any report.

## Method 4: Run one holdout test, and first work out how big a difference you can detect

**What to do**: Artificially create a control group where "this money isn't spent," and use the difference to answer the causal question—but work out the resolution first, then decide the design.

**How**

1. Pick a design by your market structure. Geographic control: split markets into test and control groups and pause or halve the spend in the test group, provided the markets can be operated independently with no cross-region spillover. Time-based on/off: instead of splitting geographically, rotate on/off weekly nationwide and compare each market's on-weeks against its off-weeks, which naturally absorbs regional differences but costs more weeks. Dose ladder: don't go to zero; run three levels of −50% / flat / +50%, which is more noise-resistant than "on/off" and easier for the business side to accept.
2. Work out the resolution first—this step decides whether the experiment succeeds. Suppose there are 20 markets with 500 qualified leads per market per month, estimate the standard deviation of month-to-month variation across markets at three levels—75 / 150 / 250 leads—and with 10 test markets against 10 control markets, at 95% confidence and 80% power, the smallest detectable difference is about 94 / 188 / 313 leads per market per month, i.e. 19% / 38% / 63% relative. The implication is direct: what a geographic control can reliably answer is "is this channel actually worth nothing," not "did a 5% lift do anything."
3. Work the observation window the other way. Suppose 10,000 qualified leads a month and you want to verify a real increment of about 5% for an AI channel; take half the markets as test: detecting a 20% relative change needs about 6,700 leads per group, roughly 1.3 months; detecting 10% needs about 28,400 per group, roughly 5.7 months; detecting 50% needs only about 900 per group, roughly 0.2 months. In one sentence: small effects need long windows; what can be confirmed quickly is a large effect.
4. So set the first round's goal as "ruling out catastrophic misjudgment"—is this channel completely ineffective, and will things collapse if the budget is moved away. To measure a small effect there are only two paths: switch the unit of observation to revenue or contract value (a larger single value), or accept a two-quarter window.
5. Get five things right, or seasonality and natural variation will contaminate the conclusion: the test and control groups must be compared in the same week and under the same promotion cadence, never against the same period last year; also look at the same group's data for the 4–8 weeks before the experiment as a before-and-after baseline, to offset the gap the two groups already had; the smallest observation unit is a whole week, and any window under 7 days doesn't count; before the experiment, write down the hypothesis, the primary metric, the observation window, and the stopping rule, and don't peek mid-way; when reporting, give the effect size, not just the direction.
6. Set the stopping rule before you start. Looking at the results halfway and deciding when to stop based on them will lift a nominal 5% false-positive rate to over 30%; you also have to handle multiple comparisons, the novelty effect, and proxy metrics failing—you optimized form submissions but the deals didn't move.

**Example**: Experimentation itself can be built up—Booking.com runs more than 25,000 experiments a year, and its head of experimentation says there were as many as 1,000 online at once [third-party verified: citing an official statement]. A holdout test is not a special case; it is the crudest one in that system.

**Pitfalls**: Treating "it didn't collapse when I paused it" as "the channel is useless." A holdout test is good at answering whether a channel has failed wholesale; it cannot answer whether a small increment exists. When the interval crosses 0, the right move is to extend the window, not to pick a prettier number.

## Method 5: Split the budget into three buckets, hard-code the keep-or-cut rules, and report ranges not point estimates

**What to do**: Split the budget into three buckets and state the thresholds, hard-code the keep-or-cut conditions; when reporting, give both the attribution number and the experiment number, plus an interval.

**How**

1. Split the buckets and state the thresholds: the attributable bucket, recommended at no more than 50% of the total budget, used for tactical optimization within the bucket; the proven-increment bucket, whose keep-or-cut is decided by the interval from the incremental experiment; the under-validation bucket, recommended at 5%–10%, treated as experiment cost, carrying no KPI except "finishing the design."
2. Hard-code three keep-or-cut rules. Add budget only after ruling out the "increment = 0" hypothesis and only when the incremental ROAS is higher than the marginal ROAS of the next-best channel; when the interval crosses 0, hold and extend the window; asset investments don't take part in this round of trimming—they serve search, AI entry points, sales, and existing-customer referrals all at once, and cutting them is cutting the pass to the whole chain.
3. For strategic judgment, look at the "water level," not the "share." AI arms every seller at once, so an unchanged industry-wide share is the norm and isn't itself evidence of "useless"; the standard changes from "how much did this channel grow" to "how long until this moat expires."
4. Write decision outputs always as intervals. Reference format: a company has an annual paid budget of 1 million yuan; GA credits the AI channel with 0.5% attribution, i.e. 5,000 yuan; self-reported research shows 27% of new customers remember asking an AI. Run one 8-week on/off experiment, and after 4 weeks on and 4 weeks off the output looks like this—"pause investment in this channel; the incremental qualified leads point estimate is −5%, interval −1% to −9%; corresponding annualized revenue impact X to Y ten-thousand yuan."
5. Tie the decision to that output: if the interval is entirely negative and the lower bound exceeds the next channel's marginal ROAS, add budget; if it crosses 0, extend the window to 12 weeks; if the point estimate is near 0 and the upper bound is small, taper per the under-validation bucket.
6. Two reporting disciplines. Report the attribution number and the experiment number to management at the same time, and label the model source—merging the two into one "blended attribution number" is the fastest way for a marketing department to lose credibility [third-party verified]; every budget change must carry an evidence grade—changes backed by an incremental experiment can be executed directly, while changes backed only by an attribution report may only be adjusted within the bucket, not moved across buckets.

**Example**: One industry measurement guide notes that multi-touch attribution models over-attribute digital channels by more than 30% [third-party verified]; another attribution guide cites a CMO survey saying 62% of CMOs listed "proving ROI to finance" as their biggest challenge [third-party verified]. There are ready tools to lower the bar too: Google open-sourced the aggregated-data modeling framework Meridian in March 2024 and opened it to all marketing teams starting January 2025 [official].

**Pitfalls**: Having a direction for budget migration but no rule. The typical move is to cut 20% of the paid-media budget and add it to content and GEO, on the reasoning that "paid-media ROAS is falling and AI is the trend"—the part that was cut was never incrementally validated, the part added in has no observation window either, and a year later you still can't say what that money brought; you have just switched to a different story for the report.

---

## Notes for this chapter

- Attribution numbers and experiment numbers cannot substitute for each other, and cannot be merged into one number. The former answers "how do things that already happened get allocated"; the latter answers "what would be lost if this money weren't spent"; a holdout with no control group cannot answer a causal question [our judgment].
- Reporting an interval means showing the decision maker uncertainty itself, not offering a more conservative point estimate; when the interval crosses 0, don't force a direction—that just shifts the cost of judgment onto the person who has to decide [our judgment].
- Several key numbers in this chapter currently exist only as relays and have not been traced back to their original source: the 54-fold gap between 27% and 0.5%, Boring Marketing's visibility status quo, the 40%–60% monthly turnover, and Leapd's 680-million-citation analysis. Use them only to judge orders of magnitude; don't put them in a budget table, and don't write them into external materials [our judgment].
- The resolution and sample-size formulas are demonstrations: the month-to-month variation uses three assumed levels—75 / 150 / 250—and doesn't include design effects or the variance inflation of stratified sampling; before going live, first estimate real variation from your own market-level data for the last 12 months, then work the window backward [our judgment].
- Some situations aren't suited to a straight holdout: regulated industries should switch to a dose ladder and document beforehand that this is an experiment, not a reduction of service; for consumer businesses with small ticket sizes and short cycles, switch the primary metric to a more sensitive proxy such as branded search volume and direct visits, and move the budget in small 10%–20% steps [our judgment].

## Sources for this chapter

[1] Pew Research Center｜"Google users are less likely to click on links when an AI summary appears in the results" (with an AI summary, traditional results get 8% clicks and without one 15%; links inside the summary get 1%; 18% of searches contain an AI summary)｜2025-07-22｜https://www.pewresearch.org/short-reads/2025/07/22/google-users-are-less-likely-to-click-on-links-when-an-ai-summary-appears-in-the-results/｜[third-party verified]
[2] SparkToro｜"In 2026, Less than One Third of Google Searches Still Send a Click" (US zero-click rate 68.01% in the first four months of 2026; 60.45% in 2024, data source Datos; about 45% ten years ago, data source Jumpshot)｜2026-06-08｜https://sparktoro.com/blog/in-2026-less-than-one-third-of-google-searches-still-send-a-click/｜[third-party verified]
[3] Google official blog｜"Everything announced at Google I/O 2026" (AI Mode tops 1 billion monthly actives; Gemini 3.5 Flash is the default model)｜2026-05-20｜https://blog.google/innovation-and-ai/technology/ai/google-io-2026-all-our-announcements/｜[official]
[4] Gmail official help page｜Bulk senders: spam complaint rate target below 0.1%, must never reach 0.3%｜https://support.google.com/mail/answer/14229414｜[official]
[5] Blake, Nosko & Tadelis (eBay)｜NBER Working Paper 20171 (large-scale field experiment: for existing customers of an already-known brand, brand keyword ads have very little incremental effect)｜https://www.nber.org/papers/w20171｜[third-party verified]
[6] Kohavi, Tang & Xu｜"Trustworthy Online Controlled Experiments"｜2019, Cambridge University Press (standards for pre-registration, observation windows, and multiple comparisons)｜[third-party verified]
[7] Google Meridian｜open-source MMM framework (open-sourced 2024-03, opened to all marketing teams from 2025-01)｜https://developers.google.com/meridian｜[official]
[8] Meta Robyn｜open-source MMM tool｜https://github.com/facebookexperimental/Robyn｜[official]
[9] Our own measurement 1｜candidate-set multi-model measurement (2026-09-13: sampling and stability of the visibility baseline; 22%–56% overlap across two runs of the same question, 4%–21% across models)｜repository `实测/实测1-候选集多模型/`｜[our own measurement]
[10] Video infrastructure company Gumlet｜the 54-fold gap between the self-reported channel and GA attribution (relayed by Derivatex Agency 2026-05, not traced to the original analysis)｜[third-party verified]
[11] Similarweb｜2026 generative AI brand visibility index (external media frequently cited by AI get less than 1% of their referral traffic from AI platforms, relayed through a third-party summary)｜[third-party verified]
[12] Leapd｜680-million-citation analysis (only 11% of domains are cited by both ChatGPT and Perplexity)｜[third-party verified]
[13] Fiska｜form self-reported channel + UTM self-built attribution (leads from large models rose from 3 to 14 a month, over 50% of total leads)｜[vendor claim]
[14] Boring Marketing｜in-house visibility study (14,750 buyer questions × four platforms; overall brand citation rate 14.0%; 53% of brands wiped out in their own category; finance and insurance 2.1%; legal and professional services 86% never cited)｜[vendor claim]
[15] Brand citation rate comparison (34,234 AI answers: ChatGPT 0.59% / Perplexity 13.05% / Grok 27%, relayed through a third-party summary)｜[third-party verified]
[16] eMarketer｜cited sources turn over 40%–60% monthly｜2026-04｜[third-party verified]
[17] CXL / Peep Laja｜12 A/B testing mistakes (the same test showed a 10%–20% lift in November and was completely ineffective in April)｜[third-party verified]
[18] House of MarTech｜2026 measurement guide (multi-touch attribution over-attributes digital channels by more than 30%; where measurement programs fail points to organization, not technology)｜[third-party verified]
[19] TapClicks｜2026 attribution guide (citing NIQ 2026 CMO Outlook: 62% of CMOs listed "proving ROI to finance" as their biggest challenge)｜[third-party verified]
[20] Observer｜"Why experimentation drives high-performing companies" (citing Booking.com head of experimentation Lukas Vermeer: 25,000+ experiments a year, 1,000+ concurrent)｜https://observer.com/2026/01/why-experimentation-drives-high-performing-companies/｜[third-party verified: citing an official statement]
