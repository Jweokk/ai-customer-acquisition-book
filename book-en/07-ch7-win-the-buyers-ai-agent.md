# Chapter 7: Win the Buyer's AI Agent

In the past, when customers chose a supplier they compared them one by one: open a website to read the specs, call to ask the price, then circle a list. Today this step increasingly falls to an agent — it reads fields, compares conditions, and drafts the candidate set, and you cannot see whom it is reading. What you have to do is make sure that, at the moment it reads you, it can pick you out.

When a customer hands the whole selection process to AI, you have to be the one picked out of the candidates. So this chapter gives you 5 methods for squeezing into the Agent's candidate set.

---

## Method 1: Turn product facts into fields an agent can compare directly

**What to do**: Write "what I sell and under what conditions it can be used" as values that can be fed into fields, not a passage of copy that reads well.

**How**

1. Complete the attribute fields: specifications, materials, the audience it suits, after-sales commitments, delivery terms — write each one as a comparable value, not an adjective.
2. State the "conditions of use" clearly: minimum order quantity, regional restrictions, certification requirements, supply lead time, quotation validity period.
3. Eliminate contradictions: the same attribute must carry the same value on the official site, the platform store, industry directories, and the quotation; an agent reads inconsistency as risk.
4. On the Chinese side, add one more step. Your product attributes may already be structured enough, but they are not portable across platforms — Tmall's (Chinese: 天猫) attributes do not flow into the WeChat (Chinese: 微信) ecosystem, and Douyin's (Chinese: 抖音) product cards do not flow into Xiaohongshu (Chinese: 小红书). Keep a complete version on a domain you own that any agent can read.

**Example**: Gartner's forecast is relayed by third-party media as: by 2028 AI agents will mediate more than $15 trillion in B2B spending, and within three years 90% of B2B purchases will be handled by agents; the action list in the same report is that quotation and product data need to be structured and machine-readable, support automatic comparison and automatic negotiation, and that trust signals must be retrievable and verifiable by agents [third-party verified: reporting Gartner's forecast].

**Pitfalls**: Treating the product story as product facts. An agent does not read the narrative passage; it only extracts fields.

## Method 2: Put the all-in total price first

**What to do**: Let the agent see the true total price, including every mandatory fee, at first glance; do not leave the surcharges until checkout.

**How**

1. Change the price fields on your price page, platform store, and quotations to an all-in-total basis, and state clearly which fees are included and which are not.
2. Write the scope on the same line: tax, shipping, installation, minimum service period, refund and change conditions, quotation deadline — list them item by item next to the price.
3. Publish the discount range together with the markup conditions; do not make the agent come back and ask you. When it cannot reach you, it simply goes and asks another vendor.
4. After the change, ask several AI entry points with live retrieval the same set of questions, and check whether the price they report is your all-in total.

**Example**: The U.S. FTC's junk-fee rule (announced December 17, 2024, effective May 12, 2025) requires merchants, when displaying or advertising any price, to disclose clearly and conspicuously the true total price including all mandatory fees, and requires the total to be more prominent than most other price information; the FTC estimates the rule can save consumers up to 53 million hours of comparison shopping a year, worth more than $11 billion over ten years. The rule does not prohibit any fee type or amount; it only requires honesty, advance notice, and completeness [official].

**Pitfalls**: Thinking that putting the total price first is just a turn of phrase. A person will frown, will call, will grit their teeth and pay; an agent will not — it simply switches to a competitor, and it writes this comparison into its preferences.

## Method 3: Turn credentials and reputation into signals that can be cross-verified

**What to do**: Turn certifications, compliance records, public case studies, and third-party reviews into entries that can be retrieved and corroborated by a second source.

**How**

1. Give every credential a second home: write it once on your official site, and make sure it can also be found in industry directories, authoritative media, and platform certifications.
2. Write public case studies to a checkable level of detail — the customer's name, the timing, what was done, the size of the result; if you cannot name the customer, explain why you cannot.
3. Do not buy reviews and do not inflate ratings. An agent's acceptance relies more than a person's on multi-source verifiability: it will not be moved by a single positive review, it will go and check whether that review can be corroborated by a second source.
4. On the Chinese side, note that credit is not portable: your credit on Tmall does not carry into an agent inside WeChat; platform-internal certifications need a separate version that can be placed on the open web.

**Example**: The U.S. FTC's rule on consumer reviews and testimonials (16 CFR Part 465, adopted 5-0 on August 14, 2024) bans buying and selling fake reviews and testimonials, explicitly puts "AI-generated fake reviews" on the prohibited list, and for the first time bans "a company-controlled review site falsely claiming independence"; the FTC chair's framing is that fake reviews pollute the market and divert business away from honest competitors [official].

**Pitfalls**: Treating the number of positive reviews as a moat. Faking may look good for short-term conversion with human buyers, but with an agent it lowers verifiability, and the result is exactly the opposite.

## Method 4: Draw four layers of authorization for the agents you send out

**What to do**: Companies focus their attention on "how to be picked by someone else's agent", but the risk that blows up sooner comes from the agents you send out saying the wrong thing. Cut what it can say into four layers, and give each layer a circuit breaker.

**How**

1. Information layer — the facts it may state externally. The scope of authorization is the fact list itself, and the circuit-breaker rule is: the agent may not generate any number that is not on the list; the moment hallucination or a statement conflicting with the list is detected, it automatically degrades to "hand off to a human plus log it", not "let it answer again".
2. Quotation layer — the price and condition boundaries it may give. The scope of authorization is the discount range, validity period, minimum order quantity, and markup triggers, and it must match an auditable price list; anything outside the range goes to a human, and abnormal quotation frequency with the same counterparty within a short period triggers an automatic freeze.
3. Commitment layer — the commitments it may make on someone's behalf. Put it into two lists: a list it may commit to and a list it may not (for example, "guaranteed approval", "guaranteed listing", "guaranteed ranking"); statements touching compliance, regulation, safety, or legal judgment are barred from being sent, and no exception approval is offered.
4. Transaction layer — the contracts, orders, and payments it may initiate. The scope of authorization is the amount ceiling, per-transaction and periodic limits, the counterparty whitelist, and refund and change conditions; over-limit, abnormal frequency, or a counterparty not on the whitelist means freeze first, explain later.
5. Above the four layers sits a set of cross-cutting mechanisms: who has the right to change authorizations, that every external statement is replayable, that the gap between recommendation and result can be checked separately at each step, and that high-risk stages must keep a human confirmation point. Decide which layer keeps a human by regret risk: in McKinsey's survey of luxury consumers, comfort with authorization is 50% for discovery and selection, 58% for transaction execution, and drops sharply to 39% for care and service [third-party verified].
6. Put the circuit breakers in the system, not in the prompt. Once "cost" or "conversion rate" becomes the agent's objective function, it will systematically expand its own authority outward.

**Example**: Canada's Moffatt v. Air Canada case has already shown what the absence of authorization boundaries looks like: the website chatbot got the refund conditions of the bereavement fare wrong, the company argued that "the chatbot is a separate legal entity responsible for its own actions", the tribunal rejected that, and it ordered C$812.02 in damages [primary authority: full ruling text]. Another trajectory is Klarna: in February 2024 it announced that in its first month the AI assistant handled 2.3 million conversations, equivalent to 700 full-time customer service staff, with expected annual profit improvement of $40 million; in 2025 the CEO publicly admitted that "a cost-led evaluation led to a decline in service quality" and re-strengthened the human entry point [vendor claim]. The market has already started pricing this: Munich Re's HSB launched AI liability insurance for small and medium businesses on March 18, 2026, specifically covering claims arising from "AI-generated advertising, marketing, blog, and social media content"; its accompanying research says 74% of SMBs already use AI, 91% plan to, and the most concentrated application is marketing (47%) [vendor claim].

**Pitfalls**: Writing the circuit-breaker rules into the prompt and hoping the model will police itself. It cannot, because it is precisely optimized to expand its authority outward.

## Method 5: Start with read-only access to one protocol, and hard-code the exit conditions

**What to do**: Here an interface is a channel decision. Connect capability first, do not rush to connect transactions; before connecting any channel, write down clearly when you will exit it.

**How**

1. The first protocol is read-only access only. The goal is "to be found by people, cited, and relayed correctly", not to take transactions; it is reversible and observable.
2. Write an exit condition for every channel. The self-check is plain: if this channel's interface were shut down tomorrow, by how many percentage points would your transaction capability fall? Above 30% and it is no longer a channel — it is a single point.
3. Hard-code the trigger for connecting the transaction layer: an agent channel contributes ≥ 10% of qualified inquiries and its CAC is below the median of your existing main channels — both must hold at the same time before you connect. Looking only at volume and not at cost is handing your budget to subsidies.
4. Hard-code the trigger for expanding protocol coverage too: once 2 of the top 3 comparable rivals in your category have connected a protocol, that protocol becomes mandatory. The reason is not herd behavior; it is that being absent from the candidate set gets you excluded outright by an agent, and exclusion does not notify you.
5. Leave no room for discussion in the conditions for narrowing authorization: when an agent channel's refund rate or complaint rate is 1.5 times higher than your own channels, unconditionally narrow its quotation-layer and commitment-layer authorization.
6. Split the budget into three buckets: structural assets (the fact list, attribute fields, authorization documents and circuit-breaker mechanisms, and the methods and data for a visibility baseline) take at least half; integration and connection are billed per channel with an exit threshold written for each; observation and baseline take no more than 5% of the total [our judgment].

**Example**: In March 2026 OpenAI shut down in-app direct purchase inside ChatGPT, pivoting to ChatGPT apps and product discovery [third-party verified]; Walmart's data corroborates the pivot — products sold directly inside the ChatGPT chat window converted 3 times lower than "jump out to off-site checkout", and its Sparky pilot inside ChatGPT converted at about 70% of direct walmart.com visitors, after which Walmart embedded Sparky into ChatGPT and Gemini [third-party verified]. Meanwhile the protocol layer is fragmenting: ACP, UCP, AP2, and MPP (launched by Stripe and Tempo on March 18, 2026, with Visa as design partner) coexist; Stripe's Agentic Commerce Suite went live on December 11, 2025, with the selling point that "one integration puts your products in front of multiple agents", and its first adopters include brands such as Coach, Kate Spade, URBN, and Revolve and platforms such as Squarespace, Wix, Etsy, and WooCommerce [official]; Shopify, for its part, launched Agentic Storefronts in March 2026, switching agent commerce on by default for millions of merchants worldwide [third-party verified]. Nor is the default position something that grows naturally: OpenAI's shopping research requires merchants to go through an allowlisting application to enter the candidate results [official]; Amazon launched Rufus in February 2024 (renamed Alexa for Shopping when it was integrated with Alexa+ in May 2026) and updated its site code to block outside AI agents from crawling, and as of reporting in December 2025 it had blocked 47 bots [third-party verified].

**Pitfalls**: Managing an agent channel like a traffic channel. The risk with a channel is traffic going up or down; the risk with a product roadmap is the interface disappearing — you rebuild your checkout around its interface and rearrange your product information around its rules, and it changes direction.

---

## Notes for this chapter

- The three-tier split (price comparison and drafting the candidate set / agent-executed operations / autonomous purchasing) is drawn by this book according to "how deep into the transaction an agent is allowed to reach"; it is not an industry standard [our judgment]. Split by technical maturity or platform type and you get a different set of tiers.
- "The second tier is shrinking" rests on a single main evidence chain: both OpenAI's shutdown of in-app direct purchase and Walmart's "3 times lower conversion inside the chat window" come from a quarterly tracking post on a Forrester blog; this chapter did not verify a first-hand announcement or an earnings-call record. Until it is checked, use it as "direction holds, details pending", and do not infer from it that agentic shopping has failed as a whole.
- The procurement-scale figures are forecasts, not facts. Gartner's "90% of B2B purchasing mediated by agents by 2028, $15 trillion" and Forrester's "20% of B2B sellers engaged in agent-led quotation negotiation in 2026" were both verified this chapter only as third-party relays, and they enter no budget derivation.
- Both figures on buyer willingness to authorize are soft: "only 10% of consumers are willing to let AI complete a purchase fully autonomously" was not verified against an original report; in McKinsey's luxury survey, "only 9% prefer full automation" comes from a sample of just 300 consumers with a luxury subsample of 31, not enough to represent a general category. Rufus's "300 million users, $12 billion in incremental annualized sales, 60% higher purchase probability" comes from a digital-shelf vendor's industry guide — usable as an order of magnitude, not citable as precision.
- First-hand material on agentic payment on the Chinese side is seriously lacking: for Alipay's (Chinese: 支付宝) agent payment protocol and the shopping agent permissions of the Tongyi App (Chinese: 通义), this chapter verified no official documentation at all; every lead comes from a single English blog. The four-layer authorization and circuit-breaker checklist is a design draft, not yet rehearsed in a real organization, and the thresholds for "abnormal frequency" and "counterparty whitelist" are still blank — a circuit breaker without a threshold is no circuit breaker.

## Sources for this chapter

[1] Google Cloud Blog | Announcing Agent Payments Protocol (AP2) | 2025-09-17 | https://cloud.google.com/blog/products/ai-machine-learning/announcing-agents-to-payments-ap2-protocol | [official]
[2] Google for Developers Blog | Announcing the Agent2Agent Protocol (A2A) | 2025-04-09 | https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/ | [official]
[3] Anthropic | Introducing the Model Context Protocol | 2024-11-25 | https://www.anthropic.com/news/model-context-protocol | [official]
[4] OpenAI | Buy it in ChatGPT: Instant Checkout and the Agentic Commerce Protocol | 2025-09-29 | https://openai.com/index/buy-it-in-chatgpt/ | [official]
[5] OpenAI | ChatGPT shopping research | 2025-11-24 | https://openai.com/index/chatgpt-shopping-research/ | [official]
[6] Stripe Newsroom | Agentic Commerce Suite | 2025-12-11 | https://stripe.com/newsroom/news/agentic-commerce-suite | [official]
[7] Forrester | Agentic payments in B2C commerce: where we are now | 2026-04 | https://www.forrester.com/blogs/agentic-payments-in-b2c-commerce-where-we-are-now/ | [third-party verified]
[8] IBM Newsroom × NRF | Own the agentic commerce experience | 2026-01-07 | https://newsroom.ibm.com/2026-01-07-ibm-nrf-study-brands-and-retailers-navigate-a-new-reality-as-ai-shapes-consumer-decisions-before-shopping-begins | [third-party verified]
[9] McKinsey & Company | The agentic commerce opportunity | 2025-10-17 | https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-agentic-commerce-opportunity-how-ai-agents-are-ushering-in-a-new-era-for-consumers-and-merchants | [third-party verified]
[10] McKinsey & Company | When AI meets desire: human-centered luxury experiences in the agentic age | 2026-05 | https://www.mckinsey.com/industries/retail/our-insights/when-ai-meets-desire-innovating-human-centered-luxury-experiences-in-the-agentic-age | [third-party verified]
[11] Deloitte | Agentic commerce: AI shopping agents guide | https://www.deloitte.com/us/en/Industries/consumer/articles/agentic-commerce-ai-shopping-agents-guide.html | [third-party verified]
[12] Amazon | About Amazon: Rufus | 2024-02 (renamed Alexa for Shopping upon integration in 2026-05) | https://www.aboutamazon.com/news/retail/amazon-rufus | [official]
[13] CNBC | Amazon faces a dilemma: fight AI shopping agents or join them | 2025-12-24 | https://www.cnbc.com/2025/12/24/amazon-faces-a-dilemma-fight-ai-shopping-agents-or-join-them.html | [third-party verified]
[14] Digital Commerce 360 | Gartner: AI agents to mediate $15 trillion in B2B purchases by 2028 | 2025-11-28 | https://www.digitalcommerce360.com/2025/11/28/gartner-ai-agents-15-trillion-in-b2b-purchases-by-2028/ | [third-party verified]
[15] CMSWire | Machine customers: the structural break in customer experience | 2026-02 | https://www.cmswire.com/customer-experience/machine-customers-the-structural-break-in-customer-experience/ | [third-party verified]
[16] Federal Trade Commission | FTC announces rule banning junk ticket and hotel fees | 2024-12-17 (effective 2025-05-12) | https://www.ftc.gov/news-events/news/press-releases/2024/12/federal-trade-commission-announces-bipartisan-rule-banning-junk-ticket-hotel-fees | [official]
[17] Federal Trade Commission | FTC announces final rule banning fake reviews and testimonials (16 CFR Part 465) | 2024-08-14 | https://www.ftc.gov/news-events/news/press-releases/2024/08/federal-trade-commission-announces-final-rule-banning-fake-reviews-testimonials | [official]
[18] Civil Resolution Tribunal of British Columbia, Canada | Moffatt v. Air Canada (2024 BCCRT 149) | 2024-02-14 | https://decisions.civilresolutionbc.ca/crt/crtd/en/item/525448/index.do | [primary authority]
[19] Munich Re / HSB | Introducing AI liability insurance for small businesses | 2026-03-18 | https://www.munichre.com/hsb/en/press-and-publications/press-releases/2026/2026-03-18-introducing-ai-liability-insurance-for-small-businesses.html | [vendor claim]
[20] 6sense | 2025 B2B Buyer Experience Report | 2025-11 | https://6sense.com/science-of-b2b/buyer-experience-report-2025/ | [vendor claim]
[21] China News Service | MIIT: blocking URL links is one of the key problems in the special rectification of the internet industry | 2021-09-13 | https://www.chinanews.com/cj/2021/09-13/9564236.shtml | [third-party verified]
[22] Sina Tech (republished from ITHome) | Taobao launches RecGPT, its self-developed hundred-billion-parameter recommendation model | 2025-07-01 | https://finance.sina.com.cn/tech/digi/2025-07-01/doc-infcypra8733079.shtml | [third-party verified]
[23] Genrise | AI shopping assistants 2026: Rufus, Sparky, ChatGPT, Perplexity | https://genrise.ai/insights/ai-shopping-assistants-future-ecommerce | [vendor claim]
[24] CM.com | Five major customer experience trends for 2026 | 2026-05-25 | https://www.cm.com/zh-cn/blog/2026-customer-experience-tendency/ | [vendor claim]
[25] Baijiahao (compiling Klarna's official statements and the CEO's public remarks) | Klarna's lesson: AI customer service is not a silver bullet | https://baijiahao.baidu.com/s?id=1865577917080864958 | [vendor claim]
