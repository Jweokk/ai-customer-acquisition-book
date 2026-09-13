# Chapter 24 Don't Cross These Lines: Six Failure Files

Every earlier chapter was about how to do things; this one is the reverse: it collects only the ways to die that have a name, a date, and a number. Someone has crossed the line and paid the price at every step above. So this chapter gives you 7 methods — one for each of the six files, plus a closing one — starting with how others went down.

A risk checklist gets read, nodded at, and put in a drawer; a failure file does not — someone really paid for each of them.

---

## Method 1: Don't amplify a claim you can't back

**What to do**: Cross “a position in AI answers” off the purchase order, and don't use fake reviews to amplify an unsupported claim.

**How**

1. Name every customer logo on the wall, every award list, every five-star rating, and every review piece, one by one, and each must point to a real contract or authorization; take down first anything that cannot.
2. Get written authorization for names and logos before they go live, spelling out the use and how it can be revoked; a trial customer cannot be displayed as a customer.
3. For every performance claim, find the internal source first, and delete it if there is none; write “who signed off” into the creative ledger.
4. Don't buy services that fake orders, fake reviews, or buy award lists, and don't sell them either: both directions are on the enforcement list.

**Example**: The “customers” on 11x's website logo wall, including ZoomInfo and Airtable, were found by a media investigation not to be real customers (only about a one-month trial); ZoomInfo sent a letter alleging false advertising and trademark infringement, and the report said total customer retention was below 50% [third-party verified]; Artisan was banned by LinkedIn at the end of 2025 and reinstated about two weeks later in January 2026, with its lead pipeline cut off outright during the suspension [third-party verified]; the U.S. FTC passed the Consumer Reviews and Testimonials Rule (16 CFR Part 465) 5-0 on August 14, 2024, and the April 2026 TruHeight case settled for $4 million, with each violation of a consent order carrying a civil penalty of up to $53,088 [official]. AI selling points from the same period have also been priced: the SEC's first “AI washing” enforcement in March 2024 brought a $400,000 fine, and DoNotPay settled for $193,000 in one of the five FTC Operation AI Comply cases [official].

**Pitfalls**: Don't use “everyone is faking it” as a reason — the first round of pushback hurts the honest sellers in the trade. A single fabricated review can influence a model output within 72 hours [to verify: 1].

## Method 2: Don't mistake “can do” for “should do”

**What to do**: Take personalization only as far as the granularity of consent, and don't use the anxiety you found to push up the ticket size.

**How**

1. Write the purpose of the data as one sentence that can be read aloud: data collected for purpose A is not used for purpose B, and a change of purpose requires fresh consent.
2. Record consent by “for what, at what frequency, on what channel”; carry out a personal information protection impact assessment before automated decision-making, and provide a convenient way to refuse.
3. Self-test before reaching out: if this message were screenshotted and posted in a public community, would you still be okay with it?
4. Every touch by AI outbound calling and AI customer service must be traceable to a consent chain; anything that cannot be traced, stop first.

**Example**: Qualtrics's October 2025 survey (14 countries, 20,000+ consumers): 53% of consumers worry about data misuse in automated AI interactions (up 8 percentage points year over year), and after a bad experience only 29% give feedback directly while 47% cut spending [vendor claim]; Usercentrics's “State of Digital Trust 2026” (7 countries, 11,000 people): 52% of consumers trust AI with personal data less, and in Sweden 77% find AI personalization intrusive [official claim]. On the Chinese side: Shenzhen Zhenai (Chinese: 珍爱网) used “virtual humans” and age anxiety to push the ticket size to tens of thousands of yuan, and got a 1.7 million yuan fine in return [third-party verified]; a central-media investigative report described AI outbound calling at 800–1,500 calls per machine per day and costs as low as a little over one jiao (0.1 yuan) per minute, grounded in Article 24 of the Regulations for the Implementation of the Law on the Protection of Consumer Rights and Interests, which bans commercial calls without consent [official].

**Pitfalls**: The currency of personalization is trust, and the credit limit is held by the user — technology decides how accurately you can speak, tolerance decides how close you can get.

## Method 3: Don't let AI promise where you have no facts

**What to do**: Write the cost of “AI saying the wrong thing” into the process, not into an apology letter: for price, terms, delivery time, payment terms, and qualifications, AI produces drafts only.

**How**

1. List what AI may not state as settled: price, terms, delivery time, payment terms, qualifications, and compensation.
2. Add a “who signs off on this sentence” field to every customer-facing AI channel; with no signer, it does not go out.
3. The first action after a hallucination is to clarify proactively and trace back the people affected.
4. Flag AI's limits on the welcome page and in prominent places in the interface, and route key answers through retrieval-augmented generation (look up the material first, then answer).

**Example**: In April 2025, Cursor's support bot invented a new policy that “one subscription only covers one device”, Reddit and Hacker News took it as an official change, and users publicly announced they were cancelling their subscriptions; co-founder Michael Truell apologized afterward, attributing it to hallucination and “non-deterministic output” [third-party verified]. The Air Canada chatbot promised Jake Moffatt he could buy a ticket at the original price and apply for a bereavement discount refund within 90 days; after the company refused the refund it argued that “the chatbot is a separate legal entity responsible for its own actions”, was rebuked by the British Columbia Civil Resolution Tribunal as “remarkable” and dismissed, and was ordered to pay about 650 Canadian dollars [third-party verified] [to verify: 2]. In December 2025, the Hangzhou Internet Court issued a first-instance ruling in the country's first generative AI “hallucination” tort case: AI does not have the standing of a civil subject, and a commitment it generates on its own does not constitute a declaration of intent by the service provider; because the defendant had prominently flagged the limitations and used retrieval-augmented generation, the court found no fault and dismissed the claims [third-party verified].

**Pitfalls**: Hangzhou's case won an exemption from liability, and the price was that a customer's mistaken belief had already occurred and public credibility had been tested in open litigation: an exemption saves money, not trust.

## Method 4: Don't buy an amplifier with no signal

**What to do**: Justify the project by “how many hours a week a job eats”, not by “what this AI can do”.

**How**

1. Run a time audit first: have the people who will use it report the hours a week they spend on preparatory work, and sort by hours.
2. Before buying, ask “who will change which habit because of it”; if you cannot name the person and the habit, don't spend the budget yet.
3. After launch, measure adoption speed, not capability breadth — a simple agent at 90% adoption beats a complex agent at 10%.
4. Design for deletion: with every tool you add, kill one manual task at the same time.

**Example**: Boomi's Luke Hagstrand has a post-mortem that includes negative data: the team built a multi-agent chatbot for the customer success department that “could answer any CSM question”, with a beautiful demo and a high-profile launch, adoption under 20%, and they finally decided to kill it: it had become “one more thing to stuff into the daily workflow” [vendor claim]. After deconstructing it, they rebuilt it as a set of small, specialized, nearly invisible agents that automatically aggregate and push signals from Salesforce, Gong, and Gainsight every week; 30 days after 2.0 launched, adoption hit 85%, saving each CSM 4–6 hours a week [vendor claim]. The post-mortem also relays two numbers: MIT says 95% of organizations get zero return on generative AI, and the industry line is that “73% of companies are stuck in PoC purgatory” [vendor claim] [to verify: 3].

**Pitfalls**: Adoption rate measures behavior change and has nothing to do with how much the system can do. A purchase that cannot report an adoption rate bought a subscription invoice.

## Method 5: Don't stare at a number that doesn't mean a deal

**What to do**: Write the “definition contract” first, then turn on AI scoring: what counts as a qualified lead, written in buyer language as a definition a system can read.

**How**

1. The definition contract must answer at least three things: what counts as a qualified lead; what counts as a mismatch and who adjudicates it; and who signs off on the conversion rate from one tier to the next.
2. Run intent data as a “candidate set”: what you buy is a ranking, and handing it straight to sales means letting AI replicate an uncalibrated assumption many times over.
3. Once a quarter, pull lead counts, MQL counts, reply rate, and meeting counts back against the closed-deal denominator; if the metrics are up and deals are flat, check the definitions first.
4. Write a one-sentence definition for each of the five labels, with the signer and the review date noted.

**Example**: A B2B marketing agency's benchmark library (including an operations audit of 47 ABM deployments): intent-prioritized accounts converted to opportunities at 21.3% versus 8.4% for non-prioritized ones, and median sales cycle shortened by 28 days; the same document's “quality warning”: 62% of buyers reported that fewer than 70% of flagged accounts showed CRM-documented activity within 30 days, 47% of intent records expired within 14 days, and 29% still had no two-way CRM integration 6 months after deployment [third-party verified]. A cohort study of 14 B2B SaaS sales organizations: AI-SDR outreach reply rates decayed by more than 60% within 18 months, from 11.2% at launch → 6.1% at month 12 → 4.4% at month 18 [third-party verified]. On the Chinese side, Hangzhou Shantao Technology (Chinese: 杭州杉淘科技) faked 589,000 orders on a “shoot A, ship B” scheme and was fined 725,000 yuan [third-party verified].

**Pitfalls**: Early decay is often misattributed to seasonality, ICP drift, or product changes, and most teams only notice after month 12 — the very period when the metrics were rising is the period when mismatch was accumulating.

## Method 6: Don't leave compliance until after launch

**What to do**: Treat compliance as the title registration of your acquisition assets, done before launch — content states clearly who generated it, and data states clearly where it came from.

**How**

1. Do explicit and implicit labeling together: explicit is the notice users can see (text at the start, end, or middle; a spoken notice added to audio; prominent placement for images and video); implicit is written into the metadata, covering generation attributes, the service provider's name or code, and the content number, with digital watermarks encouraged.
2. The label must still be there after material is downloaded, copied, or exported; when a user requests content without an explicit label, logs must be kept for no less than six months in accordance with the law.
3. Lock down one internal rule: no maliciously deleting, tampering with, forging, or concealing labels, and no providing such tools or services to outsiders.
4. For EU customers, four categories — AI interacting directly with people, generating synthesized content, emotion recognition or biometric categorization, and deepfakes — must be disclosed to a “clearly discernible” standard; fine print in the footer and a label that flashes by do not qualify.

**Example**: The four-ministry Measures for Labeling AI-Generated and Synthesized Content (CAC General Office Document [2025] No. 2) took effect on September 1, 2025, and platforms must verify implicit labels [official]; the transparency obligations in Article 50 of the EU AI Act (Regulation (EU) 2024/1689, published in the Official Journal on July 12, 2024) apply from August 2, 2026 [official] [to verify: 4]; on the data side, the practical reading of the Personal Information Protection Law requires a personal information protection impact assessment before profiling-based automated decision-making [third-party verified] [to verify: 5].

**Pitfalls**: Material without a label cannot be distributed compliantly, and what cannot be distributed is worth zero; “deleting the label” itself turns a violation from “forgot” into “on purpose”.

## Method 7: Don't automate a funnel that doesn't hold

**What to do**: Validate the funnel before doing any AI transformation; if any one of the three questions cannot be answered, work may not start.

**How**

1. Ask: does this funnel already hold in the segment where “the buyer has not contacted you yet”? Or is it waiting for a customer who is no longer present to walk in?
2. Ask: can every tier be traced to a closed deal? For a tier that cannot, what justifies keeping it in the process?
3. Ask: with all the AI switched off, does this funnel still turn? Run it manually on a small sample; if it does not run, it does not hold.
4. On the project charter, write “is the entry point still valid” as the first checkpoint.

**Example**: At Chegg's earnings call on the evening of May 1, 2023, CEO Dan Rosensweig said that student interest in ChatGPT had surged since March and was affecting new customer growth; the stock closed down 48.41% at $9.08 the next day, quarterly revenue guidance of $175–178 million came in far below analysts' expected $193.6 million, and yet Q1 revenue and earnings per share both beat expectations [third-party verified]. On the content side: Charleston Crafted (a home-improvement blog) lost 70% of its traffic and 65% of its ad revenue from March to May 2024; The Planet D (a travel blog founded in 2008) first lost half its traffic, then fell another 90% after layoffs, and closed in 2025; Stereogum's founder said in his own account that ad revenue was cut by 70%; Business Insider's organic search traffic fell 55% from April 2022 to April 2025 and it cut 21% of staff in May 2025 [third-party verified]. Pew, July 2025: when an AI summary appears, only 1% click the cited link inside the summary and 8% click the organic results below (15% when there is no summary) [third-party reported]. Stack Overflow's CEO in post-mortem: ChatGPT put the company through an “existential moment” and triggered a “Code Red”, and three years later it transformed into a SaaS business aimed mainly at enterprises; more than 80% of users want to use or already use AI for code, but only 29% truly trust AI with valuable work [third-party verified]. On the buyer side, tender records published by the City of Bellingham in January 2026 show that an employee asked ChatGPT to write tender requirements “more favorable to a certain vendor”, and at least 16 passages of the model's wording went verbatim into the final 350 requirements, with a five-year, $2.7 million contract awarded to the higher bidder (about $2.5 million versus about $1.45 million for the runner-up) [third-party verified].

**Pitfalls**: “The product didn't break, the execution wasn't wrong, the buyer changed entry points” — that line is the mechanism itself.

---

## Notes for this chapter

- **The background, amounts, dates, and regulatory document numbers of the six files follow the original manuscript, unchanged, with no new facts or cases added.** Phenomena for which named, checkable evidence was not obtained are left blank by preference.
- **Vendor self-reported data is always read at a discount**: the performance numbers from Qualtrics, Usercentrics, Boomi, The Starr Conspiracy, and Digital Applied are vendor readings and have not been reproduced by an independent third party; the denominator behind “a X-fold / X% improvement” is defined by the publisher.
- **The 12 questions at the end of the chapter, the three principles, and the three questions in Method 7 are all [our judgment]**; they are a question order, not a scoring standard; each company should first run a quarter under its own definitions before setting thresholds.
- **Items still to be verified** (original sources not traced; do not cite them alone): ① the 2026 CCTV 3·15 “AI poisoning” item is relayed only from a vendor press release, and “generating a dozen or more articles in minutes” and “making a nonexistent product a top recommendation in 72 hours” were not obtained from CCTV's original program or CCTV.com's original reporting [to verify: 1 / 6]; ② the Air Canada award has two readings (about 650 Canadian dollars / 812 Canadian dollars), and the original decision text was not checked [to verify: 2 / 8]; ③ “MIT says 95% zero return” and “73% of companies stuck in PoC purgatory” in the Boomi post-mortem are secondhand relays [to verify: 3 / 7]; ④ “applies from 2026-08-02” for Article 50 of the EU AI Act was not checked sentence by sentence against the original text of Article 113 [to verify: 4 / 9]; ⑤ the PIPL article numbers and 11x's “retention below 50%” (about 24 sources; whether it is logo, contract, or revenue retention is unclear) have only a single secondary source [to verify: 5 / 10].

## Appendix: 12-question self-check

Use it as a red-light checklist. If any single light is on, do not scale up yet — because what scales is the mistake.

| # | Question (the red-light signal is in parentheses) |
|---|---|
| 1 | Have we run this funnel manually on a small sample **without AI**? (never ran it / ran it and didn't look at the data) |
| 2 | Can we make mainstream models **accurately restate** who we are, what we do, and **who we are not for**? (cannot produce an accuracy baseline) |
| 3 | How many third-party sources are **not under our control** (editorial media, review sites, communities, podcasts)? (our own sites are more than half) |
| 4 | Can we explain clearly why “this lead is qualified” — in **buyer language** rather than a score range? (all we can give is a score and a model name) |
| 5 | For the five tiers — lead / prospect / opportunity / win / payment — the **definition contract**: who signs, how often is it reviewed? (nobody signs / the definition is stuck in an old deck) |
| 6 | For our AI outreach, can we state for each person **at what granularity they consented to which purpose**? (using “signing up means consent” to cover everything) |
| 7 | For every AI-generated piece aimed at buyers, **who signs off, who can pull it, how often is it reviewed**? (there is a publishing process but no retraction process) |
| 8 | Do our AI-generated materials have both **explicit and implicit labels**? Whose service-provider code is in the metadata? (explicit only, with metadata set by the outsourcing vendor) |
| 9 | Do our customer-facing chatbots and voice agents meet disclosure obligations **where the user is located** (including frequency and protection of minors)? (compliant only by place of registration) |
| 10 | In our most recent “**turn AI off for a week**” controlled experiment, which metrics did we look at? (never done, or only activity volume) |
| 11 | What is the **adoption rate** of the AI tools and agents we have bought? Why don't the non-adopters use them? (cannot give an adoption rate, only renewal records) |
| 12 | If a platform changed its rules or a model changed version tomorrow, which of our acquisition assets **would go to zero overnight**? (cannot list them, let alone hedge) |

Questions 8 and 9 are the ones Chinese companies most often miss: **labeling is about distribution eligibility, not aesthetics**; question 12 maps to the book's hedging logic — **dependency cannot be eliminated, but it can be inventoried, priced, and spread**.

## Three principles

Six files, one closing method, twelve red lights, distilled into three sentences.

### Principle One: Pushback always arrives

Wherever **a signal that can be faked at scale** is used for acquisition, pushback will certainly arrive — only the timing and the form are unknown. This book has seen four ways it shows up: platform rules (the LinkedIn ban), regulatory process (FTC fines, typical cases from the State Administration for Market Regulation), buyer detection and filtering (recipients spotting AI templates, buyers using AI to rewrite tender requirements), and rivals' retaliatory imitation (once the technique is copied, the signal's value goes to zero).

The operational meaning is not “don't use fakeable signals”, but: **while the signal still has value, move part of the budget to producing the unfakeable part** — first-hand data, real customer testimonials, a verifiable operating process, professional judgment someone is willing to put their name to. What they share is this: **the cost of faking them is higher than the faker is willing to pay.**

### Principle Two: An amplifier has no direction

AI does not produce direction; it multiplies the slope of an existing direction by a larger number. **A negative number times a large number gives a more negative number.** This explains four of the six files in this chapter: when the funnel does not hold, automation makes it fail to hold faster; when the lead definition is fuzzy, scoring makes it fuzzy many times over; when the script has no factual foundation, generation makes it fabricate more loudly; when compliance is not done, scale makes it break the rules more expensively.

The order is therefore fixed: **establish that the slope is positive first, then talk about amplification.** The way to judge the sign of the slope is crude, and that is exactly why so few people do it — run it manually on a small sample and see whether it actually closes.

### Principle Three: Closing the loop comes before scale

Scale is a multiplier on the loop, not a substitute for it. A minimum viable loop must answer four questions and leave checkable evidence: **who was reached → why him → who closed → why he closed.** When you cannot answer, the larger the scale the further you are from the answer — the first effect of scale is to worsen the signal-to-noise ratio.

One sentence you can put into a quarterly goal: **move only one thing per quarter, and it must be the broken link inside the loop, not a new tool outside it.**

---

## Sources for this chapter

**Regulatory documents and statutes ([official])**
- U.S. FTC | Final Rule Banning Fake Reviews and Testimonials (16 CFR Part 465) | 2024-08-14 | https://www.ftc.gov/news-events/news/press-releases/2024/08/federal-trade-commission-announces-final-rule-banning-fake-reviews-testimonials; FTC v. TruHeight ($4 million judgment) | 2026-04-13 | https://www.ftc.gov/news-events/news/press-releases/2026/04/ftc-takes-action-against-truheight-deceptive-unsubstantiated-advertising-supposed-height-enhancing
- U.S. FTC | Operation AI Comply (including Rytr, DoNotPay) | 2024-09-25 | https://www.ftc.gov/news-events/news/press-releases/2024/09/ftc-announces-crackdown-deceptive-ai-claims-schemes | see also https://www.ftc.gov/legal-library/browse/cases-proceedings/donotpay; U.S. SEC | AI washing enforcement ($400,000) | 2024-03-18 | https://www.sec.gov/newsroom/press-releases/2024-36
- Cyberspace Administration of China and three other departments | Measures for Labeling AI-Generated and Synthesized Content (CAC General Office Document [2025] No. 2, effective 2025-09-01) | https://www.cac.gov.cn/2025-03/14/c_1743654684782215.htm
- European Union | Regulation (EU) 2024/1689 (AI Act), OJ L, 2024/1689, 12.7.2024 | https://eur-lex.europa.eu/eli/reg/2024/1689/oj
- State Council | Article 24 of the Regulations for the Implementation of the Law on the Protection of Consumer Rights and Interests | effective 2024-07-01 | https://www.gov.cn/zhengce/content/202403/content_6940158.htm
- Standing Committee of the National People's Congress | Personal Information Protection Law of the People's Republic of China | effective 2021-11-01 | https://www.cac.gov.cn/2021-08/20/c_1631050028355286.htm

**Court judgments and regulatory cases ([third-party verified])**
- Moffatt v. Air Canada, 2024 BCCRT 149 | American Bar Association analysis | 2024-02-14 | https://www.americanbar.org/groups/business_law/resources/business-law-today/2024-february/bc-tribunal-confirms-companies-remain-liable-information-provided-ai-chatbot/
- Hangzhou Internet Court | first-instance judgment in the country's first generative AI “hallucination” tort case | People.cn (People's Court Daily) | 2026-01-26 | http://society.people.com.cn/n1/2026/0126/c1008-40652440.html
- State Administration for Market Regulation | seven typical cases of online unfair competition | Xinhua Net | 2024-12-31 | http://www.news.cn/food/20241231/ceec0fa0841345fb872ed48b07dd3748/c.html

**Media, companies, and third-party research** [third-party verified] unless otherwise noted
- CNBC | Chegg stock falls 48.41% | 2023-05-02 | https://www.cnbc.com/2023/05/02/chegg-drops-more-than-40percent-after-saying-chatgpt-is-killing-its-business.html
- The Verge | Decoder interview with Stack Overflow's CEO | 2025-12-15 | https://www.theverge.com/podcast/844073/stack-overflow-ceo-ai-coding-chatgpt-code-red-interview
- AdExchanger | The AI search traffic collapse | 2026-01-06 | https://www.adexchanger.com/publishers/the-ai-search-reckoning-is-dismantling-open-web-traffic-and-publishers-may-never-recover/
- Stereogum (Scott Lapatine) | Getting Killed By AI | 2025-11-10 | https://stereogum.com/2478838/stereogum-relaunch/news | [official: founder's own account]
- KNKX / Cascade PBS | City of Bellingham employee used ChatGPT to exclude bidders | 2026-01-05 | https://www.knkx.org/government/2026-01-05/city-of-bellingham-chatgpt-ai-contract-vendor
- Ars Technica | Cursor's support bot invents a policy | 2025-04-17 | https://arstechnica.com/ai/2025/04/cursor-ai-support-bot-invents-fake-policy-and-triggers-user-uproar/
- TechCrunch | 11x claims customers it does not have | 2025-03-24 | https://techcrunch.com/2025/03/24/a16z-and-benchmark-backed-11x-has-been-claiming-customers-it-doesnt-have/
- TechCrunch | Artisan raises $25 million; CEO admits early hallucinations | 2025-04-09 | https://techcrunch.com/2025/04/09/artisan-the-stop-hiring-humans-ai-agent-startup-raises-25m-and-is-still-hiring-humans/
- TechCrunch | LinkedIn bans and reinstates Artisan | 2026-01-07 | https://techcrunch.com/2026/01/07/yes-linkedin-banned-ai-agent-startup-artisan-but-now-its-back/
- Boomi (Luke Hagstrand) | Built an AI agent nobody used | 2025-10-01 | https://boomi.com/blog/customer-success-ai-agent/ | [vendor claim: includes negative data]
- Qualtrics | AI customer service fails at 4 times the rate of other uses (14 countries) | 2025-10 | https://www.qualtrics.com/news/ai-powered-customer-service-fails-at-four-times-the-rate-of-other-tasks/ | [vendor claim]
- Usercentrics (Sapio Research) | State of Digital Trust 2026 (7 countries, 11,000 people) | 2026-03 | https://usercentrics.com/resources/state-of-digital-trust-report-2026/ | [official claim]
- The Starr Conspiracy | B2B intent data benchmarks 2025 (refreshed 2026-05) | https://www.thestarrconspiracy.com/insights/benchmarks/b2b-intent-data-benchmarks-2025
- Digital Applied | The case against AI SDRs 2026 (cohort study of 14 companies) | 2026-05 | https://www.digitalapplied.com/blog/case-against-ai-sdrs-contrarian-analysis-2026
- China.com.cn | AI outbound calls at a thousand a day (including a Shanghai Consumer Council survey) | 2026-07-28 | http://news.china.com.cn/2026-07/28/content_118621717.shtml
- China Economic Net | AI-generated content must carry labels (over 490 large models filed) | 2025-09-01 | http://www.ce.cn/xwzx/gnsz/gdxw/202509/t20250901_2460291.shtml
- King & Wood Mallesons (Chinese: 金杜律师事务所) | Retail marketing data compliance | 2023-06 | https://www.kingandwood.com/cn/zh/insights/latest-thinking/uni-marketing-data-compliance-in-retail-marketing-in-era-of-digitalization.html
- Sohu (Chinese: 搜狐) (vendor press release, relaying the 2026 CCTV 3·15 “AI poisoning” item) | 2026-08-31 | https://www.sohu.com/a/1068667519_100119123 | [vendor press release: quoted secondhand]
- Pew Research Center | Study of click behavior when an AI summary appears (1% / 8% / 15%) | 2025-07-22 | https://www.pewresearch.org/short-reads/2025/07/22/google-users-are-less-likely-to-click-on-links-when-an-ai-summary-appears-in-the-results/
