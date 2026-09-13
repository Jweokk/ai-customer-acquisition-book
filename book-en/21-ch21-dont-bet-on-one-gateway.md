# Chapter 21 Don't Bet on One Gateway: Dependency Check and Hedging

In the past, customer acquisition meant picking the most effective gateway and stacking budget on it—the higher the position, the more customers, and that lesson held for twenty years. Now buyers have moved to a different place to pick vendors—AI answers, platform recommendations, other people's reviews, buyers' procurement agents—and at every gateway the rules, the price, and the survival are decided unilaterally by someone else; the line that worked best for you yesterday may not count today. What you need to do is this: before any gateway gets rewritten, measure once how dependent you are on it, then give that dependence a few fallbacks.

The gateways where customers live don't belong to you, and the day the platform changes its rules you still have to be alive. So this chapter gives you 5 methods, starting with a dependency check.

---

## Method 1: Answer these twelve questions to measure your own dependency

**What to do**: Use a fixed questionnaire to turn "how dependent am I on a given gateway" into a score you can record and track.

**How**

1. Answer once a quarter, 12 questions, each worth 0–3 points, 36 points total. The person who fills it in is the person being asked—don't hand it to an assistant.

| Group | Question | 0 points | 1 point | 2 points | 3 points |
|---|---|---|---|---|---|
| Gateway structure | What share of first deals does your single largest acquisition gateway contribute (by the signed / payment-received basis, not lead count) | >70% | 50–70% | 30–50% | <30% |
| Gateway structure | If this gateway's rules changed, could you find an equivalent substitute within 30 days | no substitute | substitute exists but the cost is unbearable | substitute exists, cost is bearable | multiple gateways already running in parallel |
| Gateway structure | Does your acquisition chain depend on one platform's sharing / redirect capability | fully dependent | mostly dependent | partly dependent | not dependent at all |
| Gateway structure | If the buyer goes through no platform at all, can they still find you | no | only by remembering the brand name | has its own channel | has its own touchpoint with sustainable return visits |
| Asset ownership | In whose database is your customer relationship record kept | all on the platform | mostly on the platform | mostly your own first-party data | first-party data complete and directly reachable |
| Asset ownership | If the gateway disappears, can your content / data assets still be found by buyers | no | only scattered remnants | yes, but with no third-party support | yes, and with cross-ecosystem third-party source support |
| Asset ownership | Are your third-party sources concentrated within a single platform ecosystem | entirely concentrated | mostly concentrated | somewhat dispersed | dispersed across ecosystems |
| Asset ownership | Does your attribution and measurement depend on a single platform's self-reported data | fully dependent | mostly dependent | has a partly self-built measure | has a self-built incremental-experiment measure |
| Protocols and interfaces | For agent / buyer-system integration, have you implemented only a single protocol or a single vendor's field spec | yes, with no alternative | yes, but with a migration plan | two paths already supported | protocol-neutral structured assets |
| Protocols and interfaces | Do price, inventory, lead time, credentials, and return / exchange terms have an authoritative, verifiable, machine-readable single source of truth | no | yes, but scattered across multiple systems | unified source, but not machine-readable | yes, with version history and a change audit trail |
| Governance | In the last four quarters, have you made an explicit decision about "gateway dependency" (rather than continuing to invest by default) | never discussed | discussed, no conclusion | conclusion reached, not recorded | every quarter has a resolution and a record |
| Governance | In budget / assessment, is there an item that explicitly rewards "reducing the share of any single gateway" | no, only lead counts are assessed | raised but can't be executed | there is a metric, with very low weight | a metric on par with lead counts |

2. Work out the total first, then pick the three lowest-scoring questions—those are the only direction you touch this quarter. 0–12 is high risk, 13–24 moderate, 25–36 relatively healthy.
3. Put this table into an existing quarterly meeting, no more than one page, answering only three things: how much the largest gateway's share changed (using the first-deal basis, not the lead basis), what the rule-change log updated (mark each one "affected / not affected / watching"), and what the exit plan updated.
4. Carve out a fixed proportion of the total acquisition budget, allowed to go to only two places: non-largest gateways, and building your own assets. This proportion has no universal number—it is determined by your cost structure—and cannot be raided mid-quarter.
5. List "share of any single gateway's contribution" and "own-asset increment" (net increase in the first-party list, net increase in case-library entries, third-party source coverage) as metrics on a par with lead counts. Set no absolute target, only a direction.
6. Write a one-page plan: if this gateway disappears tomorrow, what do I do in week one. Put it somewhere others can find it.

**Example**: In its FY2018 10-K, Zynga stated itself: 51% of revenue and bookings came from Apple, 38% from Google, and 9% from Facebook, the three totaling 98%; in 2017 it was 51%/33%/12%, barely moving over two years. This is a sample of a company writing "the gateway doesn't belong to me" into a regulatory filing in its own words—a dependency structure doesn't improve just because you know it exists [official: verbatim from SEC filing].

**Pitfalls**: Handing the 12 questions down as a KPI. The team will prop up the most useless channels to score points, putting a little spend on three platforms with almost no customers, turning "multiple gateways" into a formality. Broad but same-source is still the same risk.

## Method 2: Turn rented position into assets you can take with you

**What to do**: Build a first-party identity so buyers can reach you directly, with no platform in between.

**How**

1. In the Chinese ecosystem this has a mature form: WeCom contacts, communities, official accounts / service accounts, mini programs, and SMS form a direct channel that doesn't depend on any single platform's algorithm. In the overseas ecosystem the counterpart is the email list, communities, and your own app.
2. Fit this into the actions you were going to take anyway, without adding a project: after each delivery, casually ask for a publishable customer testimonial; at each trade show, event, or support conversation, casually collect first-party contact details; give every content asset its own "can be contacted" entry point, and don't hide contact details behind a form. The acceptance standard changes from "the immediate effect of this touch" to "what this touch left behind."
3. The form of an asset can be a relationship, or it can be data. Turning content assets into data licensing is another path.
4. There is only one test: on the day the gateway disappears, can this asset call the customer back? If it can't, it doesn't count as an asset.
5. State the boundary clearly. A platform's compliance promise is not your asset: on 2025-04-22 Privacy Sandbox announced it would keep Chrome's existing third-party-cookie user-choice scheme and would not launch a new standalone third-party-cookie consent prompt, and a batch of companies that had already rebuilt their attribution systems around "the death of the cookie" took the sunk cost [official]. First-party data doesn't depend on whether the platform keeps its word, which is why it is the asset.

**Example**: Watsons (Chinese: 屈臣氏) has 4,100+ stores and 65 million members across more than 490 cities in mainland China; in 2020 it launched full-chain private-domain operations, using "store staff adding contacts + WeCom / official account / mini program / community / livestream" to run layered member operations [third-party reported]; Luckin Coffee (Chinese: 瑞幸) built a super CDP system with over 20 million members and private-domain users and 35,000+ communities [third-party reported]. Stack Overflow took another path: licensing its community Q&A data to AI companies and pivoting to enterprise internal-knowledge solutions [third-party reported]. Same mechanism, two forms.

**Pitfalls**: Treating "how much private domain can grow" as the conclusion. These samples show the structural fact that "these kinds of companies treat first-party members as a hedging asset"; the multiples in them cannot be taken as an effectiveness promise.

## Method 3: Look at the failure correlation between gateways before deciding how many to spread across

**What to do**: Change "multiple gateways" from broad coverage into low failure correlation.

**How**

1. First build a counterexample on yourself: distribute the same piece of content to ten platforms, and if those ten platforms all depend on the same "content to click" logic, the same algorithm family, and the same regulatory jurisdiction, then it is still the same risk exposure across ten accounts—one classifier adjustment and ten places drop at once.
2. Compare on at least three dimensions: regulatory jurisdiction (are these gateways governed by the same law and the same regulator), medium (are they the same kind of distribution logic—search / recommendation / social / IM / offline), and buyer path (buyers researching on their own, peer referrals, or agent procurement).
3. Log each channel's "share of organic traffic" and "sensitivity to platform rule changes" in the same table, compute a concentration index, and look at its direction every quarter. The trend matters more than the absolute value.
4. Prepare for only the most likely way you would die. If your category is one AI can answer directly (question banks, news, tools, common Q&A), you are more likely to die from being replaced, so prioritize relationships and subscriptions; if distribution must pass through one big platform's sharing / payment / account system, you are more likely to die from being revoked, so prioritize multiple channels and your own touchpoints. Doing one thing well for the most likely death beats doing 10% on each of four lines.

**Example**: The daily-deal pair wrote "the correlation of gateway failure" most clearly: LivingSocial's valuation once reached $6 billion and it was ultimately sold for $0; Groupon's share price fell from $28 to around $4 [third-party verified: academic]. Two lives that looked like two gateways actually shared the same set of premises.

**Pitfalls**: Computing concentration as a number you have to hit. This book gives no threshold for "a single channel should not exceed X%"—industries differ too much; use your own four consecutive quarters of data as the baseline and look only at the direction of the trend.

## Method 4: Turn the buyer's session into a relationship you can take with you

**What to do**: Beyond the session logs held by the buyer and the model, hold a relationship with the buyer yourself.

**How**

1. Be directly contactable: a clear brand name, plus a way to reach you that doesn't depend on a platform redirect. The brand name matters especially—after agents collapse the source away, a name the buyer can say out loud and search is the only thing that can still pass through the collapse. In the Chinese ecosystem this step is often just adding a contact; overseas it is subscribing to a newsletter.
2. Be directly returnable to: your own site, your own app, your own community, offline—the buyer can come back without going through any intermediary layer.
3. Evidence that can be remembered: the case library and third-party sources are the external form of "relationship" on the buyer's side, letting the buyer confirm you even when your salesperson isn't present.
4. There is only one acceptance standard: in the week the gateway disappears, how many customers can find you on their own. "How many contacts added, how many subscribers" is a vanity metric; this one is a structural metric.
5. Minimum-threshold action: every time before sending an outreach email, ask one question—"does this letter make the brand name clear?"

**Example**: Chegg's CEO said on the 2023-05-01 earnings call that students' interest in ChatGPT had surged since March and was affecting the new-customer growth rate; the next day the stock closed down 48.41% at $9.08 [third-party reported]. Stack Overflow's CEO, looking back, said ChatGPT put the company into an "existential moment," that he triggered an internal "Code Red," and that he reassigned about 10% of staff to tackle it [third-party reported]. Neither of these two was penalized by a platform; the buyers changed gateways themselves.

**Pitfalls**: Understanding "relationship" as having added a contact or pulled people into a group. An agent won't maintain the relationship for you—its goal is to maximize buyer utility and it has no need to remember whether you are reliable, so the relationship must be held by you.

## Method 5: Don't bet on a single agent protocol; make facts into protocol-neutral assets

**What to do**: Make verifiable facts into structured assets that aren't tied to any one protocol.

**How**

1. Price, inventory, lead time, credentials, return / exchange terms, and liability boundaries—these facts need an authoritative, verifiable, machine-readable single source of truth, with version history and a change audit trail. Such an asset can be verified under any protocol.
2. Treat integration implementations as replaceable parts, not long-term investments. Customize only for one vendor's field spec and you will have to redo it at the next protocol turnover, and with shorter notice.
3. Remember the division of labor: structuring and verifiability are protocol-neutral; integration implementation is protocol-bound. Put resources into the former.
4. Keep two agent-facing integration routes; don't pick a side.
5. Treat the scope of authorization as a variable that changes. Today the buyer lets an agent "look only, don't buy"; tomorrow it lets it "close deals automatically within budget"—when the scope of authorization changes, your acquisition strategy has to change with it, and you won't get advance notice.

**Example**: On 2025-09-17, Google released the Agent Payments Protocol (AP2), advanced jointly with more than 60 payments and technology companies. Its definition of the problem is blunt: existing payment systems assume "a human clicks buy on a trusted interface," and autonomous agents initiating payments break that assumption, so it has to solve three things—authorization, authenticity, and accountability—through Mandate, a tamper-proof encrypted contract the user signs with a verifiable credential signature, forming a non-repudiable audit chain; the text explicitly points to the B2B scenario, where enterprises can use it to "autonomously procure partner solutions through Google Cloud Marketplace" [official]. AP2 and OpenAI's and Stripe's ACP are two parallel routes [official].

**Pitfalls**: Treating protocol integration as "get on early for first-mover advantage." Protocols will turn over, and the notice period at turnover only gets shorter.

---

## Notes for this chapter

- The two ways a single gateway dies are not decided by the quality of your operation. Being replaced is "the gateway is still there, you're not" (Chegg, Stack Overflow, Stereogum and the like); being revoked is "you're still there, the gateway is gone" (ATT, WeChat's external-link blocking, the TikTok divestiture law). There is only one way to diagnose replacement: see whether exposure-type metrics diverge from real acquisition metrics—in a case PPA submitted to the UK Competition and Markets Authority, an automotive content publisher's top-ranked article saw traffic fall 25%, while over the same period search visibility rose 7% and CTR fell from 2.75% to 1.71% [third-party reported]. If the divergence is confirmed for two consecutive quarters, it is not an optimization problem, it is a gateway problem.
- The "predictability" of platform policy is itself a source of risk. Privacy Sandbox, from launch to U-turn, is the best evidence: you can't make long-term investment decisions on "my judgment is this policy will land." That is why the hedging allocation in Method 1 can't follow the current-period ROI ranking—the pressure to raid it always shows up when the largest gateway is performing best, which is exactly when it should least be raided.
- Ownership and survival of the gateway are not in your hands. On 2025-09-02, the US Department of Justice won remedies in the Google search monopoly case; the court banned exclusive contracts and required opening part of the search index and user-interaction data, on the factual basis that Google had long held about 90% of all US search queries and the court had earlier issued a 277-page opinion finding monopoly [official]; on 2025-01-17, the US Supreme Court upheld the constitutionality of the TikTok divestiture law, and the distribution channel for 170 million US users faced "divest or shut down" [official: verbatim from the opinion]. Both can only be covered by multiple channels and your own assets; operational optimization can't cover them.
- The scoring tiers of the twelve questions and the four-part split of the hedge kit (assets / channels / relationships / protocols) are both [our judgment]; this is a work checklist, not a validity-tested measurement instrument. The 0/1/2/3 cut points are set by mechanism intuition; recalibrate them to your own industry structure and compare only against yourself.
- The figures in the Chinese-side private-domain samples (Watsons, Luckin, Perfect Diary, LYFEN, NetEase Zhiqi) are all media, vendor, or agency figures, and mostly self-reported single cases. This book uses them to illustrate the structural fact that "these kinds of companies treat first-party members as a hedging asset," and does not use the multiples in them as an effectiveness promise. Meta's own estimate of the ATT hit, about $10 billion, is used only for magnitude—management said on the same call that "we can't be precise, this is an estimate" [management statement, verified through third-party reporting].

## Sources for this chapter

[1] Google｜"Introducing AI Overviews"｜2024-05-14｜https://blog.google/products/search/generative-ai-google-search-may-2024/｜[official]
[2] Google｜"Everything announced at Google I/O 2026" (AI Mode tops 1 billion monthly actives)｜2026-05-20｜https://blog.google/innovation-and-ai/technology/ai/google-io-2026-all-our-announcements/｜[official]
[3] CNNIC (China Internet Network Information Center)｜the 57th "Statistical Report on China's Internet Development" (602 million generative AI users, 42.8% penetration)｜published 2026-02-05｜https://www.cnnic.com.cn/IDR/ReportDownloads/｜[official] (consistent across authoritative reprints such as Xinhua)
[4] U.S. DOJ｜"Department of Justice Wins Significant Remedies Against Google"｜2025-09-02｜https://www.justice.gov/opa/pr/department-justice-wins-significant-remedies-against-google｜[official]
[5] Google Cloud｜"Powering AI commerce with the new Agent Payments Protocol (AP2)"｜2025-09-17｜https://cloud.google.com/blog/products/ai-machine-learning/announcing-agents-to-payments-ap2-protocol｜[official]
[6] American Bar Association (Business Law Today)｜"BC Tribunal Confirms Companies Remain Liable for Information Provided by AI Chatbot (Moffatt v. Air Canada)"｜2024-02-14｜https://www.americanbar.org/groups/business_law/resources/business-law-today/2024-february/bc-tribunal-confirms-companies-remain-liable-information-provided-ai-chatbot/｜[third-party reported]
[7] Ars Technica｜"Company apologizes after AI support agent invents policy that causes user uproar" (Cursor)｜2025-04-17｜https://arstechnica.com/ai/2025/04/cursor-ai-support-bot-invents-fake-policy-and-triggers-user-uproar/｜[third-party reported]
[8] FTC｜"Trade Regulation Rule on Unfair or Deceptive Fees"｜2024-12-17｜https://www.ftc.gov/news-events/news/press-releases/2024/12/federal-trade-commission-announces-bipartisan-rule-banning-junk-ticket-hotel-fees｜[official] (effective 2025-05-12)
[9] arXiv:2507.05301 (Kai-Cheng Yang)｜citations in AI search answers are highly concentrated｜2025-07-07｜https://arxiv.org/html/2507.05301v1｜[academic preprint, before peer review]
[10] Our own measurement 1 · candidate-set multi-model measurement｜2026-09-13｜method and raw data at `实测/实测1-候选集多模型/`｜[our own measurement]
[11] CNBC (Lauren Feiner)｜"Facebook says Apple iOS privacy change will result in $10 billion revenue hit this year"｜2022-02-02｜https://www.cnbc.com/2022/02/02/facebook-says-apple-ios-privacy-change-will-cost-10-billion-this-year.html｜[management statement, verified through third-party reporting]
[12] Google Privacy Sandbox Blog (Anthony Chavez)｜"Next steps for Privacy Sandbox and tracking protections in Chrome"｜2025-04-22｜https://privacysandbox.google.com/blog/privacy-sandbox-next-steps｜[official]
[13] Digiday (Ivy Liu)｜"Google AI Overviews linked to 25% drop in publisher referral traffic"｜2025-08-15｜https://digiday.com/media/google-ai-overviews-linked-to-25-drop-in-publisher-referral-traffic-new-data-shows/｜[third-party reported]
[14] AdExchanger (Anthony Vargas)｜"The AI Search Reckoning Is Dismantling Open Web Traffic"｜2026-01-06｜https://www.adexchanger.com/publishers/the-ai-search-reckoning-is-dismantling-open-web-traffic-and-publishers-may-never-recover/｜[third-party reported]
[15] Stereogum (Scott Lapatine)｜"Getting Killed By AI"｜2025-11-10｜https://stereogum.com/2478838/stereogum-relaunch/news｜[official: founder's own account]
[16] Zynga Inc.｜Form 10-K (FY2018), platform concentration disclosure (Apple 51% + Google 38% + Facebook 9% = 98%)｜filed 2019-02-27｜https://www.sec.gov/Archives/edgar/data/1439404/000156459019005098/znga-10k_20181231.htm｜[official: verbatim from SEC filing]
[17] CNBC (Sarah Min)｜"Chegg shares drop more than 40% after company says ChatGPT is killing its business"｜2023-05-02｜https://www.cnbc.com/2023/05/02/chegg-drops-more-than-40percent-after-saying-chatgpt-is-killing-its-business.html｜[third-party reported]
[18] The Verge《Decoder》｜"Stack Overflow users don't trust AI. They're using it anyway"｜2025-12-15｜https://www.theverge.com/podcast/844073/stack-overflow-ceo-ai-coding-chatgpt-code-red-interview｜[third-party reported]
[19] China News Service (Chinese: 中国新闻网)｜"MIIT: Blocking website links is one of the key problems in the special rectification of the internet industry" (State Council Information Office press conference)｜2021-09-13｜https://www.chinanews.com/cj/2021/09-13/9564236.shtml｜[third-party reported]
[20] European Commission｜"Commission provides guidance under Digital Markets Act to facilitate development of innovative products on Apple's platforms"｜2025-03-19｜https://digital-markets-act.ec.europa.eu/commission-provides-guidance-under-digital-markets-act-facilitate-development-innovative-products-2025-03-19_en｜[official]
[21] Supreme Court of the United States｜"TikTok Inc. v. Garland, 604 U.S. ___ (2025)"｜2025-01-17｜https://www.supremecourt.gov/opinions/24pdf/24-656_ca7d.pdf｜[official: verbatim from the opinion]
[22] FTC｜"FTC Announces Final Rule Banning Fake Reviews and Testimonials" (16 CFR Part 465)｜2024-08-14｜https://www.ftc.gov/news-events/news/press-releases/2024/08/federal-trade-commission-announces-final-rule-banning-fake-reviews-testimonials｜[official] (effective 2024-10-21)
[23] FTC｜"FTC Takes Action Against TruHeight" (thousands of employee-written five-star reviews + bot accounts; $4 million judgment)｜2026-04-13｜https://www.ftc.gov/news-events/news/press-releases/2026/04/ftc-takes-action-against-truheight-deceptive-unsubstantiated-advertising-supposed-height-enhancing｜[official]
[24] Google｜"New Gmail protections for a safer, less spammy inbox"｜2023-10-03｜https://blog.google/products-and-platforms/products/gmail/gmail-security-authentication-spam-protection/｜[official]
[25] Everyone Is a Product Manager (Chinese: 人人都是产品经理, Yan Tao Sanshou column)｜"A full teardown of Watsons' private domain" (65 million members, 4,100+ stores, 5,000+ communities)｜2022｜https://www.woshipm.com/operate/5452718.html｜[third-party reported]
[26] Jazzyear (Chinese: 甲子光年, interview with Luckin senior technical director Zhao Xu)｜"Luckin reshapes the coffee business with AI" (super CDP, over 20 million members / private-domain users, 35,000+ communities)｜2025-05｜https://www.jazzyear.com/article_info.html?id=1496｜[third-party reported]
[27] Aike SCRM (Chinese: 艾客 SCRM)｜"A teardown of Perfect Diary's private-domain community operations"｜2023-01｜http://www.ikscrm.com/school/syll/1493.html｜[third-party reported: vendor perspective]
[28] Southern Metropolis Daily (Chinese: 南方都市报; republished by NetEase News)｜"As the traffic dividend peaks, how to do marketing and customer service" (Tencent Qidian + LYFEN: 3,700+ stores, 45 million+ user records)｜2024-01｜https://www.163.com/dy/article/IOTLLO6Q05129QAF.html｜[third-party reported]
[29] NetEase Zhiqi (Chinese: 网易智企; reposted by Weiyangx)｜"AI private-domain operations solution" (four-layer stratification; insurance customer case)｜2025｜https://www.weiyangx.com/441234.html｜[vendor claim]
[30] Wharton Knowledge｜"The Death of the Daily Deal" (LivingSocial's $6 billion valuation → sold for $0; Groupon's share price $28 → $4)｜https://knowledge.wharton.upenn.edu/article/death-daily-deal/｜[third-party verified: academic]
