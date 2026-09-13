# Chapter 16 Let AI Answer Around the Clock

During the day someone watches the back office and takes the inquiries one by one; after hours the phone goes silent, and a customer who can't reach anyone goes off to the next vendor. At this step the customer has already come to you on their own — if you can't catch them, the visit was wasted. So this chapter gives you 5 methods to turn "those inquiries after hours" into leads.

---

## Method 1: Open the reception desk on official channels first

**What to do**: Don't hire a third-party relay and don't modify the client — use official channels like WeChat Customer Service and WeCom to open a reception point of your own where a link can be attached.

**How**

1. First count how many places you can be found from: the footer of your website, landing pages, the official account menu, business cards, platform store pages. Each of these places is missing a "tap and you can talk" entry point — fill it in.
2. Open the reception point on official channels. WeChat Customer Service has public API documentation that includes interfaces such as "get customer service account link"; once you have the link you can attach it to your website and landing pages [official].
3. On the WeCom side, go through the developer center and first understand the development boundaries clearly — what you can do, what qualifications are required, which step needs enterprise verification — then decide who will configure it [official].
4. For bringing the bot in, use an existing integration path. Alibaba Cloud (Chinese: 阿里云) Intelligent Dialogue Robot (Tongyi edition) has a "WeChat Customer Service Deployment Guide" that describes exactly how a bot connects to this WeChat Customer Service gateway [official].
5. After configuring, act as a customer yourself once. Take a phone that has never followed you, tap in from the landing page, ask three questions, and see whether you were caught, how long it took, and whether the one who caught you was a person or a bot. A cruder acceptance standard works better: within half a minute a person or a bot speaks first [our judgment]. If you can't do that, the link is broken, the hours are misconfigured, or no one has claimed this gate at all.
6. Write down "who watches this gate during which hours." Skip this step and every automation later becomes an auto-reply that no one answers. What is attached at each gate and who maintains it — check them off against this table:

| Reception point | What is attached | Who maintains |
|---|---|---|
| Website footer | Customer service account link + service hours | Marketing |
| Landing page | The same link, with a button labeled "you can ask outside business hours" | Marketing |
| Official account menu | Put the customer service entry on the first level | Operations |
| Business cards and email signatures | QR code | Sales |
| Platform store page | In-platform customer service entry + the same script | Operations |

**Example**: WeChat Customer Service's official documentation lists "get customer service account link" as a separate interface entry [official]. Its practical use is narrow but hard: it lets you attach the reception entry to any page of your own, instead of only inside WeChat.

**Pitfalls**: Opening the reception point on a personal account or on a third-party relay client. The more gates you open the more it looks like a real business, but only official channels survive changes in platform rules, and if something goes wrong you won't lose the account along with it [our judgment].

## Method 2: Build the knowledge base in your own hands first

**What to do**: Write the Q&A the bot will use into a sheet of your own first, then copy a version into the platform back end.

**How**

1. Copy from real conversations of the past three months: the exact words customers asked, the exact words support replied. Copying this way is far better than rewriting your website copy — nobody can finish reading answers rewritten from marketing language. When copying, pick only two kinds of sessions — those where the customer asked and then dropped off, and those where the customer asked and then closed. The first tells you which sentence drove them away, the second tells you which sentence worked.
2. One answer answers only one thing. Split "can you issue an invoice" and "how soon can it ship" into two entries. A bot that answers off-topic is, in the great majority of cases, not a bad model — it's a knowledge base with three things packed into one entry.
3. Behind every answer, attach two things: the source (which page, which clause) and the owner (who reviews it — write a name or a desk, not a department).
4. Start the answer's phrasing from the customer's own words. If a customer asks "can you issue a special VAT invoice for this," the answer starts with "yes" — not with "our company is a general taxpayer." If the customer scans and can't see the two words they want, they'll ask again, or just leave [our judgment].
5. Fill the fields according to this table, one row per entry:

| Field | What to fill in |
|---|---|
| Customer's exact words | The sentence copied from a real conversation |
| Standard answer | Answers only one thing |
| Source | Page / clause / internal document ID |
| Owner | Who reviews |
| Last updated | Date |

6. Keep the master file in your own document; the one in the platform back end is a duplicate. When you change tools or platforms later, the master file doesn't need to be rewritten. Update once a month, adding the Q&A that newly emerged that month; it's fine if it's incomplete — anything not written automatically falls into the human category.

**Example**: That Alibaba Cloud deployment guide gives the official path for connecting a bot to the WeChat Customer Service channel [official]. What's worth noting here is that the bot and the channel are two separate things — the channel belongs to the platform, the Q&A belongs to you.

**Pitfalls**: Treating the knowledge base as a configuration item inside the platform back end. The back end stores only a copy; the master file is in your hands. This one point determines how many days you'll spend redoing it on the day you change tools [our judgment].

## Method 3: Sort intent into three tiers, then decide who answers

**What to do**: Give the bot a set of tiering rules, so that it decides when to answer on its own and when to hand over to a human immediately.

**How**

1. Sort questions into three tiers, write the rules into the configuration, don't leave them in people's heads:

| What the customer is asking | Who answers | What to record |
|---|---|---|
| Price, whether they can order now, how the contract is signed | Hand over to a human immediately | Exact words + contact info |
| Specs, whether it can integrate with existing systems, how it differs from others | The bot answers | Contact info + intent tier |
| Looking at materials, looking at cases, simply comparing prices | The bot answers | Record only, don't chase |

2. Write out clearly the hours for "hand over to a human immediately": during the day to whom, at night to whom, on weekends to whom. A single on-duty phone number or a group message is fine — the point is that this rule doesn't depend on some person remembering it.
3. When the bot hands over to a human, carry the customer's exact words over with it. Making someone repeat a question they just asked is the fastest way to lose a lead.
4. Look at the handover list once a day and look for two kinds of problem: cases that should have been handed over but weren't, and cases handed over in the middle of the night that no one picked up.
5. Unify the nighttime fallback script into one sentence: "I'm an automated receptionist; I've noted what you said, and someone will contact you tomorrow morning." Someone must actually contact them afterward, otherwise it's a pit you dug for yourself [our judgment].
6. When changing the tiering rules, change only one tier at a time, and watch it for a week. Change all three at once and even after you see the result you can't tell which tier did the work.

**Example**: Intercom's Fin AI Agent FAQ is a page where the vendor describes its own product [vendor claim]. It belongs to the kind of material Chapter 9 dealt with: the product's claims can be read, but its performance numbers can't be used as your own budgeting assumptions. The third tier's "record only, don't chase" action is the same idea as Chapter 17 placing a portion of people explicitly into a do-not-disturb zone.

**Pitfalls**: Letting the bot force an answer all the way through. When a customer asks the same thing twice, it means they no longer trust that answer; to keep circling at this point is to hold your own customer back for your competitor [our judgment].

## Method 4: Give AI a list of things it may not say

**What to do**: Write down as a list the things the bot must absolutely not decide on its own, and post it at the top of the knowledge base.

**How**

1. Three kinds of statement are not given to the bot: discounts and price concessions; delivery time, capacity, whether to squeeze in an order; compliance, certification, performance guarantees.
2. Behind each forbidden phrase, pair a replacement line, so the bot has something to say. When a customer pushes on price, reply "I can't decide the price myself; I'll arrange the person in charge and get back to you within ten minutes."
3. For answers involving commitments, add one sentence at the end: "subject to written confirmation."
4. Write the fallback rule in stone: when a customer asks the same thing twice in a row, hand over to a human directly, no more circling.
5. Each time you add a batch of new Q&A, read through it yourself first and pick out the newly emerged commitment-type statements to add to the list.

The list should be written so it can be posted directly at the top, with a replacement script after each line:

- Don't discuss discounts, don't discuss payment terms, don't discuss free gifts → "I can't decide the price; I'll arrange the person in charge and get back to you within ten minutes."
- Don't quote delivery time, don't quote capacity, don't promise to squeeze in an order → "The exact schedule has to be confirmed by production planning; I'll ask for you today."
- Don't make certification or performance guarantees on the product's behalf → "I'll have a technical colleague handle this with you; send me your requirements."

**Example**: This "pitfall" has been measured: multiple surveys show 53%–77% of respondents have had a bad or frustrating chatbot experience; in another survey covering 5,728 customers, 64% would rather companies didn't use AI customer service at all [third-party verified: academic / institutional research]. This is precisely why the "things you may not say" list exists.

**Pitfalls**: Thinking you can just change your wording later if you said something wrong. The customer took a screenshot; the sentence you said becomes your obligation, and changing your wording later can't erase the screenshot already sent [our judgment].

## Method 5: Keep the reception process as a record you can go back to

**What to do**: Record the reception process according to rules, and say clearly on the very first message that "this is a bot answering."

**How**

1. In the first opening message, state the identity clearly: this is automated reception, and you can switch to a human at any time. Don't hide this sentence on the third level of a menu.
2. Keep the conversation record entry by entry, with the fields fixed at these five — don't let each person record their own way:

| Field | What to record |
|---|---|
| Time | Time of entry, time of handover to human |
| Source | Which gate the customer came in through |
| What was asked | The customer's exact words |
| Who answered | Bot / human name |
| Outcome | Closed / went silent / to follow up |

3. How long to keep it and who can see it — write it as an internal rule, don't rely on system defaults.
4. For fields involving personal information, collect only the few that are needed on the spot during reception, and explain the purpose when collecting.
5. After a human takes over, write the outcome back into the same record: closed, went silent, or still needs follow-up. Without writing it back, at month's end you can't know what this link actually brought in.
6. For the specific compliance boundaries — how to notify, how to keep recordings and records, which step must be handed back to a human — go back to the original regulations in Chapter 22 and check. This chapter does only two things: there is notification, and there is a record.

**Example**: The official documentation on both the WeChat Customer Service and WeCom sides gives the supported interfaces and development boundaries [official]; reception records can be retrieved from these gates into your own table, without relying on screenshots taken by hand by support staff.

**Pitfalls**: Storing every conversation indiscriminately. The more fields you collect and the longer you keep them, the greater your custodial responsibility — what to collect and how long to keep it: check with legal before you start [our judgment].

---

## Notes for this chapter

- Numbers like "what proportion of inquiries come after hours" — this chapter gives none of them. There is currently no source that can be verified; filling one in by hand just to have it in the plan will only make you get the on-duty schedule wrong.
- The compliance boundaries of the reception link (notification wording, retention of recordings and records, when a human must be handed back to) — this chapter only flags them. The specific provisions must be checked against the original regulations in Chapter 22; this chapter cannot be used as a basis for compliance.
- The overseas channel (WhatsApp Business Platform) — this time its official documentation's original text could not be verified, so this chapter writes none of its specific practices.
- Intercom's Fin AI Agent FAQ is the vendor's own statement and can only be marked [vendor claim]; it describes what capabilities the product has, and does not constitute a performance promise — handled the same way as Chapter 9.
- All methods in this chapter are done only within official channels and do not involve any way of bypassing the platform.

## Sources for this chapter

[1] WeChat Customer Service｜API documentation｜https://kf.weixin.qq.com/api/doc/path/94745｜[official]
[2] WeChat Customer Service｜Get customer service account link｜https://kf.weixin.qq.com/api/doc/path/94751｜[official]
[3] WeCom｜Developer center · overview｜https://developer.work.weixin.qq.com/document/path/94638｜[official]
[4] Alibaba Cloud (Chinese: 阿里云)｜Intelligent Dialogue Robot (Tongyi edition) · WeChat Customer Service deployment guide｜https://help.aliyun.com/zh/beebot/intelligent-dialogue-robot-tongyi-version/wechat-customer-service-deployment｜[official]
[5] Intercom｜Fin AI Agent FAQs｜https://www.intercom.com/help/en/articles/7837535-fin-ai-agent-faqs｜[vendor claim]
[6] UC Berkeley CMR｜Chatbot Frustration Is Real: Hidden Costs and Best Practices (53–77% had bad experiences; in a Gartner survey of 5,728 customers, 64% would rather companies didn't use AI customer service)｜https://cmr.berkeley.edu/2026/04/chatbot-frustration-is-real-hidden-costs-and-best-practices/｜[third-party verified: academic / institutional research]
