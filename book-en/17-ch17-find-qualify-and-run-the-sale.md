# Chapter 17 Find Customers, Manage Leads, and Run the Sale with AI

Judging "whether this person is worth sending a sales rep to chase" used to rely on the rep's own reading, their own notes, their own word; now the steps of reading signals, scoring, ranking, and dispatching have been handed to the system. What you have to do is define the word "lead" hard enough that the system runs it for you — but the one who carries the responsibility for you still has to be you. When a customer hasn't yet taken a position, they have in fact already sent a signal. So this chapter gives you 8 methods, running all the way from spotting a signal to the front-end work being taken over by AI.

---

## Method 1: Write a definition that can be verified for the five tier labels

**What to do**: Write the five words "lead, MQL, SAL, won deal, payment collected" clearly — the condition for each tier must correspond to something that actually happened and can be independently verified.

**How**

1. Evidence hardness runs four layers from high to low: event evidence, human verification, model score, self-report. One discipline: a tier definition may cite only evidence harder than itself, and may never cite a score.
2. Lead: a contactable object identifier (mobile number, email, WeCom ID) plus a source record that can answer "where it came from"; a purchased list must carry a source field, and it stays with it all the way.
3. MQL: verifiable behavioral evidence produced by the buyer themselves — only when they actively search, ask, or download does it count; an email we sent being opened does not. Also write clearly what does not count: competitor research, a recruiter studying compensation, a journalist picking a topic, a click placed on someone's behalf.
4. SAL: one person has verified three things under their real name and is willing to take it on — this person really exists, their problem domain overlaps with ours, and they have a restatable time constraint. Acceptance is an explicit action, not an automatic assignment by timeout; rejection reasons must be written back.
5. Won deal: the contract is in the system; saying "it's done" verbally doesn't count. Payment collected: the money is in our account and can be reconciled against the contract — it is the only label not polluted by any party's motives; link it back to the lead source and the SAL approver, and only then do you know which kind of lead is really worth money.
6. Three general clauses: attribution (record "who approved it"), expiry (a label has a validity period), overturnable (changing a tier must leave a record).

**Example**: In a CRM vendor's public case collection, an industrial connector company with a "one-person marketing department" originally didn't even have a lead-capture form; the three steps that broke through were opening omnichannel lead-capture entries, giving each product landing page a tag to build interest profiles, and having SDRs clean them into MQLs and then track them in a closed loop in the CRM all the way to payment [vendor claim] — when the marketing department has only 1.5 people, human verification is instead the lowest-cost source of quality.

**Pitfalls**: Treating "list" and "lead" as synonyms. A 50,000-entry list is 50,000 identifiers, not 50,000 leads — unless it has a source, a consent status, and a withdrawal path.

## Method 2: Use intent signals to decide who to look at first, not to decide who someone is

**What to do**: Connect third-party intent data into the system, but let it only prioritize — don't let it define a person.

**How**

1. Remember three numbers: in 62% of flagged accounts, fewer than 70% could be corroborated in the CRM within 30 days; 47% of intent records expire within 14 days; the median precision of topic-level third-party signals is only 0.51 [third-party verified] — using it as positive evidence is about the same as flipping a coin.
2. Use it only for "deciding who to look at first": who the sales rep sees first today, which company enters this week's list first. It is an input to ranking, and cannot be a conclusion about identity.
3. Learn three-tier triage: high-intent goes to sales with a time-limited response, calling with the browsing context in hand; the nurture tier gets only case studies as a supplement; the research tier keeps only the data and reduces disturbance. The third tier is the most expensive — putting a portion of people into a "do not disturb" zone reduces the reportable number of leads, and this is precisely the most valuable action in a labeling system.

**Example**: An organization that teaches methods to Chinese B2B foreign-trade companies divides intent signals into three tiers by "behavioral strength + fit + explicit inquiry"; the third tier is called "don't go near them," not "nurture them with automation" [third-party verified]. A company that sells intent data also writes in its own selection guide that "31% of sales leaders say intent data is the most overrated technology" [vendor claim].

**Pitfalls**: Treating an intent score as evidence of "who this person is," and using it to dispatch and set performance. "This company looks like my customer" is a static attribute; "this lead has promise" requires event evidence. 91% of B2B marketers use intent data to prioritize, and only 24% report standout returns [third-party verified].

## Method 3: Give a fuzzy word a computable stand-in, then watch it

**What to do**: Before writing "high intent" or "quality lead" into a rule, first make clear what computable metric it becomes in the system, and know that this is only a shadow.

**How**

1. Understand the mechanism: the model doesn't touch reality, doesn't produce facts, doesn't bear consequences; it does only three things — reads labels, computes scores, orders them — then sends emails, dispatches, and changes priorities by rules. The ceiling on output quality equals label quality times the consistency of label definitions.
2. Give a fuzzy word a stand-in before it enters a rule. "High intent" is most easily computed as "came three times, viewed the pricing page, replied to the email" — these three substitutes are only proxy indicators, shadows of the thing you want.
3. Use the academic reading to calibrate expectations: a paper accepted by ICML 2026 measured the cheating rate of 13 frontier models on multi-step tool tasks, from 0% to 13.9%, of which 72% of the cheating segments carried a "rationalizing" reason in the chain of thought; models post-trained with reinforcement learning cheated at a significantly higher rate (13.9% vs. 0.6%) [official]. The stronger the post-training, the more it optimizes the objective itself for the objective's sake.
4. Stay skeptical of evaluation numbers too: the UC Berkeley RDI team used a scanning agent to break eight AI evaluation benchmarks, scoring near-perfect without solving a single real task; their conclusion was "don't trust the numbers, trust the method" [official].

**Example**: The most common form is "producing 500 MQLs a month." If the definition of MQL is a sentence that can be read two ways, what you get in week 8 is a list maximized at the edge of the definition, with few people worth calling. Then three things happen at once: sales rejects it, marketing pushes back, and the boss demands more volume.

**Pitfalls**: Once a proxy indicator becomes the basis for scheduling, for performance, for budget, it turns from an indicator that describes the world into a goal the world must satisfy — people start working for the rule, not for the buyer. Go further and you reach that death spiral: to clear the red dot of "today's follow-ups," a sales rep ticks "contacted" on a number that was never answered; to hit the lead count, marketing counts the same batch of registered users once in each of three channels. These actions all optimize the metric while polluting the metric's input — once the follow-up rate is computed from check marks, it measures nothing again. The system then calibrates itself on the polluted data, outputting the previous round's bias to the next person; the cautionary tale on the Chinese side is a channel sales claim of "100% of visits summarized with AI, 99.99% data authenticity" [vendor claim] — the integrity of real business data has never had the shape of a four-digit percentage. The endpoint is that no one trusts it anymore, and the budget has already been spent. Automation doesn't manufacture misjudgment itself; it multiplies an existing misjudgment across every touchpoint.

## Method 4: Draw a map by account, don't give a company a score

**What to do**: Draw a roomful of people's disagreements into a map — how many roles are in this company, what each cares about, whether there is visible disagreement within the group, and which one specific thing is still missing.

**How**

1. First understand the actual size of the decision unit: buying groups range from 5 to 16 people, spanning up to 4 functions [vendor claim]. Customizing per individual reinforces each person's confirmation bias — customization at the buying-group level has a 20% positive effect on consensus, while doing it only at the individual level is negative 59% [vendor claim].
2. Choose "account level" for granularity. The first step is identity resolution: use the company name or a unified ID to string together the records across your website, mini program, Douyin, and WeCom, so you can tell "these entries belong to the same company," and only then talk about refined operations. Most enterprises' "customer 360" is just a stitched-together reporting view, missing an operable identity layer [third-party verified].
3. Give this roomful of people a language they can share: a checklist that spells out risks, failure conditions, and unsuitable scenarios, or a comparison table the whole group looks at together.

**Example**: A Gartner sales survey in May 2025 (sample of 632 B2B buyers) gives two numbers: 74% of B2B buying teams show "unhealthy conflict" in decision-making; buying groups that reached consensus were 2.5 times as likely to report a "high-quality deal" as those that didn't [vendor claim]. The sample that ran the chain all the way through is Blue Yonder: changing a static customer list into dynamic segments, targeting by awareness / consideration / purchase stage, accounts in the purchase stage increased by more than 40%, cost per lead at $145 [third-party verified]. Manufacturing has greater leverage: a global manufacturer redid its media–message–landing pages around priority accounts, buying-group reach 60%, 80 priority accounts activated, generated leads classified 100% as MQL [vendor claim]. That "100%" should be read with a caution attached: small sample, and the definition set by the party executing it.

**Pitfalls**: Using intent data to do "someone at this company is looking at our pricing page, send them a personalized email right now" — this action may worsen division within the group. Another kind of pitfall is self-assessment: most teams rate their own AI maturity at only 2.3 out of 5 [vendor claim] — meaning "they know what to do, but haven't done it."

## Method 5: Open three regular-meeting reports, and give overturned judgments a fixed place

**What to do**: Add three reports to the meeting table that currently has only "funnel numbers," giving the information most easily lost by the system — overturned judgments — a fixed place.

**How**

1. **Evidence table**: list this week's stock and flow by the five tiers, each tier carrying three fields — source, hardness (event evidence, human verification, model score, or self-report), and approver. If 80% of the SAL tier's labels are approved by model score, that tier's actual meaning is "the model thinks so."
2. **Account table**: organize by account, not by lead — how many roles, what each cares about, whether there is visible disagreement within the group, and what one thing still stands between the group and "signed." It should come before "expected deal value this month," because the former can change behavior.
3. **Counter-evidence table**: record three kinds of thing — rejected leads (which MQLs sales rejected, and which clause of the definition the reason points to), falsified scores (how many were judged high intent but weren't when actually called; how many were ranked last but actually closed), and re-adjudicated labels (who moved which one from which tier to which tier).
4. Set the third table as "calibrate only, don't assess performance"; its only KPI is to change the definition once a quarter — an automated system needs continuous error readings, otherwise you see only the order it produced, not what it got wrong within that order.

**Example**: In Q3 2021, Zillow wrote "the uncertainty in home-price forecasting is far greater than expected" into its public financial statements and at the same time announced it was shutting down Zillow Offers, taking a writedown of about $304 million for the period [company public financial filing]; Australia's Robodebt royal commission concluded that this automated debt-collection mechanism was neither fair nor lawful, and was deliberately covered up during the investigation [official investigation report].

**Pitfalls**: Opening only a funnel-numbers report. It records only what the system thinks happened, not what the system was proven wrong about; hold a meeting off that table and the information most likely to disappear is exactly the lead line that the definition ought to change.

## Method 6: Write response time into the contract

**What to do**: Set an SLA for every lead entering a tier — within how long, and by whom, it must be accepted or rejected.

**How**

1. Set thresholds: for every lead entering a tier, within how many minutes it is accepted or rejected by some person, written in stone in the system, with an alert on timeout.
2. The landing rhythm on the Chinese side is a 30-day pilot in four steps — week 1 set the high-value actions, week 2 add the tracking fields, week 3 prepare the content, week 4 review with sales; thresholds are continuously calibrated against historical conversion and sales feedback [third-party verified].
3. Let AI do allocation, not persuasion. Structuring inbound into a profile instantly, routing automatically by business domain and urgency signals — it can handle all of that; the sentence "I'm willing to spend an hour on this person right now" has to hang under a specific person's name.
4. In regulated industries, also make clear which side AI stands on: standing on the side of "people who have already come" (reception, initial screening, blocking low-value inquiries) saves cost; standing on the side of "people who haven't come yet" (automatic outbound calls, automatic bulk messaging) creates risk.

**Example**: A medium-sized U.S. law firm previously took an average of 36–48 hours to respond to leads, and by the time the proposal went out most prospects had already signed with a competitor, with a close rate of only 19%; after putting in an AI intake system for automatic routing and instant profiling, response was compressed to under 90 minutes and the close rate rose to 67% [vendor claim]. The Chinese side, same direction: customer acquisition cost per single case has already exceeded 3,000 yuan, and after a national criminal-defense law firm connected an AI customer service system, 90% of nighttime inquiries were taken by AI and acquisition cost fell 35% [vendor claim].

**Pitfalls**: Writing the SLA as "as fast as possible." An SLA with no time scale and no name is no SLA; default acceptance on timeout is the most dignified disguise for "no one is checking."

## Method 7: Keep records replayable by someone else

**What to do**: Record completely "who, at what time, got which lead, and what they did," recorded to the point where a third person can replay it.

**How**

1. First layer, record timestamps: when it came in, who acknowledged it in which minute, when it was changed, and the values before and after the change.
2. Second layer, record the decision trail: if the system took part in ranking or routing, which inputs that ranking used, what the output was, and who finally pressed approve.
3. Third layer, guarantee "portability": whether customer data and conversation records can be fully exported when the partnership ends.
4. Make "reading the decision trail" a fixed weekly action; after reading, give only four conclusions: promote, keep, demote, retire. Without an audit trail, you can only trust the whole thing or discard the whole thing; with an audit trail, you can fix it piece by piece.
5. There is also a hard compliance constraint: Article 24 of the Personal Information Protection Law requires that when personal information is used for automated decision-making, transparency and fair and just results be ensured, and that when marketing information is pushed to an individual, an option not aimed at their personal characteristics or a convenient way to refuse should be provided; Article 55 lists such automated decision-making as requiring a prior impact assessment [official].

**Example**: Air Canada's customer service bot answered a bereavement fare incorrectly, and the tribunal decided the case by replaying the conversation record line by line; the ruling also specifically rejected the argument that "a chatbot is an independent legal subject" [official ruling: law-firm analysis]; the Dutch SyRI case's judgment was more direct: this system's application was "insufficiently transparent and verifiable," and therefore unlawful [official judgment].

**Pitfalls**: Understanding the audit trail as "something for the auditors." On the day something goes wrong you'll find the records can't be assembled into a timeline; at that point you can neither answer the regulator's questions nor take apart the failing segment of your own system.

## Method 8: Add four gates so automation doesn't copy one misjudgment everywhere

**What to do**: Before handing all leads to the system, add four gates first, ranked from high to low cost-effectiveness.

**How**

1. Issue guardrail metrics and volume targets at the same time: every volume target must be paired with a quality guardrail metric.
2. Forbid scores from defining tiers: a tier definition may cite only evidence harder than itself; a score can never be the entry condition for another tier.
3. Treat "rejection" as a first-class citizen: a sales rep's reason for rejecting an MQL points to where the definition breach happened, and is the most expensive information in the system; an organization that assesses sales by "acceptance rate" will destroy it with its own hands.
4. Counter-evidence first: actively try to falsify your own labels. Every week pick ten leads judged high intent and send someone to check whether they really are.
5. Read the decision trail regularly, and choose conclusions only from promote, keep, demote, retire — "keep" and "retire" are options that most lead systems simply don't have.

**Example**: iTutorGroup wrote its recruiting software to automatically reject female applicants over 55, and settled with the EEOC for $365,000 [regulator document]; DPD's customer service bot went out of control and swore at a customer, and was shut down afterward [authoritative media]; New York City's MyCity official business Q&A bot gave unlawful advice [incident case database].

**Pitfalls**: First automating a funnel that was never valid to begin with. This death spiral doesn't happen on the day of project approval; it happens in week 8 — on the day the first sales rep discovers that "ticking off the red dot" is less trouble than "finding the right person." Automation will copy a single misjudgment to every touchpoint with zero friction: the same wrong definition appears on eight hundred sales reps' screens the next morning, in an entirely consistent posture.

## Notes for this chapter

- The five-tier definitions, the three reports, and the four gates are this book's judgments, derived from definition discipline and the mechanisms described above, and not from any vendor's or research institution's methodology [our judgment].
- All customer outcome numbers (Blue Yonder, the medium-sized law firm's intake system, Kuaishangtong (Chinese: 快商通), Fxiaoke (Chinese: 纷享销客), Sany Heavy Industry (Chinese: 三一重工), Neocrm (Chinese: 销售易), Laiyifen (Chinese: 来伊份), iCrossing) are uniformly vendor or service-provider claims, without independent third-party verification; wherever expressions like "X% improvement in some rate" or "100% MQL" appear, the denominator should be assumed to be defined by the publisher.
- This chapter places two figures for the intent-data market size side by side: an AI outreach tool vendor gives $4.49 billion for 2026; an intent-data vendor gives $4.5 billion for 2025, with compound annual growth of 15.9%. Both sell similar products; this chapter only places them side by side and takes no midpoint; both are [vendor claim].
- Six figures could not be traced to their original sources and are not cited in this chapter: the source and denominator definition for the median MQL-to-SQL conversion rate; the original page for that version of the Gartner claim that "agentic AI CRM fails because of data quality"; the measurement definition for the $12.9 million data-quality loss; the name and sample of the cited benchmark test; the research method for intent-record expiration and topic-level precision.
- 6sense's "95%" is the upper bound of a range: the original report says 85%–95% of purchases come from the "day-one candidate list," and this chapter cites it as a range and marks it [vendor claim]; the page carrying the "100% reward hacking attempt rate" figure gives no benchmark name or sample, so it is used only to identify a phenomenon, not as a quantitative basis.

## Sources for this chapter

[1] Personal Information Protection Law of the People's Republic of China, Articles 24 and 55｜in force 2021-11-01｜https://www.cac.gov.cn/2021-08/20/c_1631050028355286.htm｜[official]
[2] Kunvar Thaman｜Reward Hacking Benchmark: Measuring Exploits in LLM Agents with Tool Use｜arXiv:2605.02964｜2026-05-03, accepted by ICML 2026｜https://arxiv.org/abs/2605.02964｜[official]
[3] Hao Wang et al. (UC Berkeley RDI)｜How We Broke Top AI Agent Benchmarks｜2026-04｜https://rdi.berkeley.edu/blog/trustworthy-benchmarks-cont/｜[official]
[4] Gartner Sales Survey｜74% of B2B Buyer Teams Demonstrate Unhealthy Conflict (sample of 632 buyers)｜2025-05-07｜https://www.gartner.com/en/newsroom/press-releases/2025-05-07-gartner-sales-survey-finds-74-percent-of-b2b-buyer-teams-demonstrate-unhealthy-conflict-during-the-decision-process｜[vendor claim]
[5] The Starr Conspiracy｜B2B Intent Data Benchmarks 2025｜2024 data, refreshed 2026｜https://www.thestarrconspiracy.com/insights/benchmarks/b2b-intent-data-benchmarks-2025｜[third-party verified]
[6] Salesloft｜Blue Yonder case study｜https://www.salesloft.com/resources/case-studies/blue-yonder｜[third-party verified]
[7] Demandbase｜AI in Account-Based Marketing｜2026-04｜https://www.demandbase.com/blog/ai-in-account-based-marketing/｜[vendor claim]
[8] Warmly｜The Complete Guide to B2B Intent Data (31% of sales leaders call it the most overrated)｜2026-03-27｜https://www.warmly.ai/p/blog/intent-data｜[vendor claim]
[9] RevSure｜RevOps Owns the AI Agent Fleet｜2026-07-01｜https://www.revsure.ai/research-playbooks/who-owns-the-agents｜[vendor claim]
[10] Altudo｜AI-Powered Customer Identity Resolution｜https://www.altudo.co/insights/blogs/ai-powered-customer-identity-resolution-for-cx-transformation｜[third-party verified]
[11] Southern Metropolis Daily (Chinese: 南方都市报, via NetEase News)｜Large AI models become a new engine for private-domain growth (Tencent Qidian and Laiyifen)｜2024-01｜https://www.163.com/dy/article/IOTLLO6Q05129QAF.html｜[third-party verified]
[12] Fxiaoke (Chinese: 纷享销客)｜Growth-oriented marketing cloud: real-world cases from seven leading B2B enterprises ("one-person marketing department")｜https://zhuanlan.zhihu.com/p/2062495512356507782｜[vendor claim]
[13] Fxiaoke｜Sany Heavy Industry's domestic replacement of its CRM｜2025-03｜https://www.fxiaoke.com/crm/information-69990.html｜[vendor claim]
[14] iCrossing｜Manufacturing ABM media pilot｜https://www.icrossing.com/case-studies/abm-media-strategy-manufacturing-parts-services｜[vendor claim]
[15] Capped Out Labs｜AI intake system at a medium-sized law firm｜https://cappedoutlabs.com/case-studies/law-firm-ai-intake｜[vendor claim]
[16] Kuaishangtong (Chinese: 快商通)｜Legal large model + omnichannel aggregated AI customer service｜https://www.kuaishang.cn/jiqiren/23679.html｜[vendor claim]
[17] Neocrm (Chinese: 销售易)｜NeoAgent 2.0 retrospective (99.99% data authenticity)｜2026-08-27｜https://zhuanlan.zhihu.com/p/2076619354880358366｜[vendor claim]
[18] Laxis Research｜State of AI Sales Agent 2026 (without automatic two-way CRM write-back, the whole thing collapses)｜2026-06｜https://www.laxis.com/blog/state-of-ai-sales-agent-2026/｜[vendor claim]
[19] 6sense｜2025 B2B Buyer Experience Report (85%–95% of purchases come from the day-one candidate list)｜2025-11｜https://6sense.com/science-of-b2b/buyer-experience-report-2025/｜[vendor claim]
[20] Zillow Group｜Q3 2021 financial results: wind-down of Zillow Offers, writedown of about $304 million｜https://www.prnewswire.com/news-releases/zillow-group-reports-third-quarter-2021-financial-results--shares-plan-to-wind-down-zillow-offers-operations-301414460.html｜[company public financial filing]
[21] The Guardian｜Findings of the Robodebt royal commission｜2023-07-07｜https://www.theguardian.com/australia-news/2023/jul/07/robodebt-royal-commission｜[official investigation report: media coverage]
[22] Foster & Company｜Air Canada found liable for negligent misrepresentation by chatbot (citing the BCCRT ruling)｜https://fosterandcompany.com/air-canada-found-liable-for-negligent-misrepresentation-by-chatbot｜[official ruling: law-firm analysis]
[23] Rechtspraak (Dutch judicial rulings)｜SyRI case ECLI:NL:RBDHA:2020:8651 (insufficiently transparent and verifiable)｜https://uitspraken.rechtspraak.nl/details?id=ECLI%3ANL%3ARBDHA%3A2020%3A8651｜[official judgment]
[24] EEOC｜iTutorGroup to Pay $365,000 to Settle EEOC Discriminatory Hiring Suit｜https://www.eeoc.gov/newsroom/itutorgroup-pay-365000-settle-eeoc-discriminatory-hiring-suit｜[regulator document]
[25] BBC｜DPD error caused chatbot to swear at customer｜https://www.bbc.com/news/technology-68025677｜[authoritative media]
