# Chapter 9: Advertising: From "Selecting an Audience" to "Giving a Target"

Advertising used to mean nailing the audience precisely: pick the region, pick the age, pick the interests, pick the keywords — the finer your targeting, the better your economics. Now the platform has taken this step back — you give it a target and a budget, and it goes off into the big pool to find people itself. Audience targeting is turning from your job into the system's job.

Customers are still pushed along by the feed; only the way you buy has changed. So this chapter gives you 6 methods, switching from "picking audiences" to "giving targets".

---

## Method 1: Change "selecting an audience" into "giving a target"

**What to do**: Stop fine-tuning targeting; give the system a target cost per conversion and let it find people on its own.

**How**

1. First pick one conversion event in the account that **can report back reliably** — an order, a lead capture, or an add on WeCom (Chinese: 企微); pick one, do not hang five on at once. This one is what the system needs to learn; hang too many and it does not know what to learn toward.
2. Set the target cost per conversion near your historical cost. Read this number as "I want people at roughly this price point"; it is not a "cheaper is always better" knob.
3. Give the system a learning period, and during it do not repeatedly change the bidding strategy. With too few conversion samples on hand, the system cannot tell who your people are, and the more often you change things now, the less it learns.
4. Change only one thing at a time: either the budget or the target cost, never both on the same day. After a change, watch for a sufficient stretch of time before judging.
5. Test the bidding strategy and the creative separately. Strategy is "whom to find"; creative is "what words to find them with"; change the two together and even when a result comes you cannot tell which one earned it.

**Example**: Baidu's (Chinese: 百度) official help pages describe oCPC's use very plainly — set a target cost per conversion, and the system optimizes toward that cost [official]. Ocean Engine's (Chinese: 巨量引擎) official product manual describes automated delivery as "pooling human delivery experience and system optimization capability to cover the entire delivery chain" [official]. As for the learning period, that Ocean Engine scaling material explains it in detail: at the start of a campaign the system has little conversion data on hand, so it can only try users in large numbers to feel its way; accumulate enough and it moves into stable delivery, fall short and the exploration fails [vendor claim]. **This passage directly explains why "it just will not run when you first turn it on" is normal.**

**Pitfalls**: Squeezing the target cost clearly below the historical value. The lower you set the target, the most common outcome is that volume simply will not run — you think you are saving money, but you are actually tying the system's hands.

## Method 2: Give the system a direction; do not expect it to fence people in

**What to do**: Use a seed list or audience signals to tell the system which direction to search in, while knowing clearly that it is only a hint.

**How**

1. Hand over the people who most resemble your customers: your existing closed-customer list, high-intent visitors, and people who added you on WeCom but did not order. These three resemble customers to different degrees; submit them separately and look at them separately.
2. Give an asset group only one clearly themed seed. Cramming industry terms, competitor terms, and behavioral audiences all into one group points in no direction at all.
3. Once a week, look at the audience the system actually ran to and compare it with your seed. If it drifted, change the seed rather than going back to add targeting and weld the opening shut.
4. Reserve a small slice of budget to run a "no seed" control group. Without this control, you can never say whether the seed did the work or the system would have found these people anyway.

**Example**: The Google Ads API documentation says in so many words: the audience signal in Performance Max (Asset Group Signal) is a "hint" to the system about user intent and preferences, used to "find new customer segments you might not have anticipated", and it is not itself hard targeting [official]. The documentation also explains that one asset group can carry multiple signals, but each must be added separately [official].

**Pitfalls**: Setting an audience signal as if it were hard targeting, then finding the system running outside the signal and concluding "the system is disobedient". It was never designed to fence people in — **what you actually want is not to fence things in, but to avoid pointing in the wrong direction**.

## Method 3: Turn one piece of creative into a batch of creative

**What to do**: The unit of competition in delivery changes from "one good ad" to "a batch of creative the system can freely combine".

**How**

1. What you submit at one time is multiple headlines, multiple images, multiple short videos — not one set polished to perfection.
2. Creative and landing page must say the same thing. If the headline talks low price and the landing page is a premium line, conversion will definitely collapse — this has nothing to do with how smart the system is.
3. Refresh the whole batch after a while. Creative has a lifespan; run the same batch too long and performance decays on its own — do not wait until the drop is visible to the naked eye to top it up.
4. Prepare creative according to delivery scale. That Ocean Engine material gave a rough rule of thumb: the number of ads is roughly daily spend divided by 100, and the number of creative assets roughly daily spend divided by 1000 [vendor claim]. This ratio need not be copied, but you can use it to check whether your own creative volume is obviously too low.

**Example**: The Google Ads Help Center defines Ad Strength as real-time feedback on the "relevance, quality, and diversity" of the creative, used to judge whether an asset group is "set up well and can maximize performance" [official]. Tencent Ads (Chinese: 腾讯广告), for its part, talks about automatic placements by pairing "diverse creative adaptation" with "intelligent optimization strategy" [official].

**Pitfalls**: Thinking that writing pretty copy is enough. What the system rates is **diversity** — the same meaning phrased ten ways is still one set of creative in its eyes.

## Method 4: Feed your own list back into delivery

**What to do**: Connect your own data into delivery, then read the results back — do not just keep spending on strangers.

**How**

1. Push first-party audiences (your own list, website behavior) to the ad platform. Most cloud vendors' marketing products provide this channel; you do not have to build it yourself.
2. After pushing, separately collect the metrics for **this batch of people**: spend, impressions, CPM, clicks, CTR, and cost per click.
3. Look only at this batch's performance; do not evaluate it with whole-account averages. The whole account mixes in people the system found on its own, and with the two blended together you cannot tell whether the list is useful.
4. The list itself must iterate: feed the traits of the best-performing segment back into the seed pool for the next round, forming a loop. This step is done on a rolling basis, not once.
5. Align definitions before pushing the list. What "closed customer" means in your CRM and what "conversion" means on the platform — if the two do not line up, the numbers you read back are wrong, and the same customer may count as two people across the two sides. If the list contains people who have unsubscribed or explicitly refused marketing, remove them first.
6. Do not expect the list size to be right in one go. A small list is not necessarily useless, but with a small sample the swings are large — look at the trend, not a single day.

**Example**: The Alibaba Cloud (Chinese: 阿里云) help documentation gives the path: after an audience is pushed to the platform, you can review spend, impressions, CPM, clicks, CTR, and cost per click for a specified account, audience, and order [official].

**Pitfalls**: Pushing without reading back. Sending the list out and not looking at what comes back is handing over your customer data for free and getting no conclusion in return.

## Method 5: Label AI-generated creative

**What to do**: For AI-generated images, videos, and copy, declare their identity according to the rules before publishing.

**How**

1. Distinguish the two kinds of marking: an **explicit label** is a notice the user can see; an **implicit label** is written into the file data and is not easily perceived. Both are required — you do not choose one.
2. Add a prominent notice in an appropriate place on images; add notices on the opening frame and around playback for videos, and optionally at the end and in the middle; for virtual scenes, add one on the opening frame.
3. The marking must still be there after the creative file is downloaded, copied, or exported — it cannot hang only in the delivery backend and vanish once exported.
4. If you go through an app distribution platform (a mini program, an app listing), the review step verifies the marking materials, so prepare this in advance.

**Example**: The Measures for the Labeling of AI-Generated and Synthesized Content set out explicit-labeling requirements separately for text, audio, images, videos, and virtual scenes, and state clearly that "when functions such as download, copy, and export are provided, it shall be ensured that the file contains an explicit label meeting the requirements"; Article 7 also provides that internet application distribution platforms must verify the labeling materials during listing review. The Measures took effect on September 1, 2025 [official].

**Pitfalls**: Thinking that only face-swaps and digital humans need labeling. The rule covers "text, images, audio, video, and virtual scenes generated or synthesized using AI technology" — **the creative images you use in delivery count too**.

## Method 6: Do not misstate yourself in your ads

**What to do**: Every claim must have an internally verifiable source, and factor the cost of platform review in advance.

**How**

1. For numbers and performance claims in ads, find the source internally before writing; if you cannot find a source, delete it.
2. Run creative through the platform's pre-review and rules first; do not wait until it is rejected after going live to change it. Every platform has a creative review step, with checks as fine-grained as the proportion of text on the outer image and whether a celebrity or artist is used.
3. Keep "money spent on delivery" and "money paid for violations" in separate books. The cost of violations should not be carried by the delivery budget, or you will take risks you should not take just to "spend the budget down".
4. Keep a record when a platform rejects you: which creative, on what grounds, and how it was changed. The same type of rejection recurring means there is a systemic flaw in your creative workflow.

**Example**: Tencent Ads' official materials list the "ad creative pre-review tool" as a capability that can detect violations in images and copy, with checks including the proportion of text on the outer image and celebrity or artist use [official].

**Pitfalls**: Treating advertising as a free creative zone nobody polices. There is review on the platform side and labeling requirements on the regulatory side, and both are tightening.

---

## Notes for this chapter

- This chapter **cites no performance multipliers**. The multipliers that can be found in the materials (for example, "automated bidding raises spend 500% over manual bidding", "ROI exceeds the channel average by 30%") all come from vendor-selected case materials, can only be tagged [vendor claim], and cannot serve as budget assumptions — the treatment here is consistent with Chapter 2.
- Conversely, the **operational rules of thumb** in vendor materials (the learning-period mechanism, "ads ≈ daily spend/100, creative assets ≈ daily spend/1000") can be referenced, but are likewise tagged [vendor claim] — do not treat them as industry standards.
- The official entries for the three Chinese platforms (Ocean Engine, Tencent Ads, Baidu Marketing) currently have only one or two help-center pages each; the mechanisms make sense, but **there is no item-by-item source text for "how to configure a specific product"** — this is the clearest gap in this chapter.
- The original texts of China's Advertising Law and the Measures for the Administration of Internet Advertising were not obtained this round (only the Measures for the Labeling of AI-Generated and Synthesized Content), so this chapter's statements on ad identifiability reach only the platform-rule level, not the level of legal provisions.
- Method 2 cites the Google Ads API documentation, which is **a description of product mechanics, not a performance promise** — it says how the signal is used, not that using it will be cheaper.

## Sources for this chapter

[1] Baidu Marketing | How to use OCPC smart bidding | https://tg.baidu.com/m/wiki/feed/11630.html | [official]
[2] Baidu Marketing | What is OCPC | https://pd.baidu.com/Knowledge/20568.html | [official]
[3] Juliangxue | [Automated delivery] product manual | https://school.oceanengine.com/product_help/content/668400000007/115216 | [official]
[4] Ocean Engine | Introduction to new scaling products and outstanding cases (PDF, includes the learning-period definition and delivery-volume rules of thumb) | http://vos.vipstatic.com/school/wp-content/uploads/2021/08/11183442/ | [vendor claim]
[5] Tencent Ads | Help Center · Automatic placements | https://e.qq.com/ads/helpcenter/detail?cid=3160&pid=9376 | [official]
[6] Google Ads API | Asset Group Signals | https://developers.google.com/google-ads/api/performance-max/asset-group-signals | [official]
[7] Google Ads Help | About Ad Strength | https://support.google.com/google-ads/answer/9142254?hl=en | [official]
[8] Google Ads Help | Creative and asset requirements | https://support.google.com/google-ads/answer/6167118?hl=en | [official]
[9] Cyberspace Administration of China and three other departments | Measures for the Labeling of AI-Generated and Synthesized Content | issued 2025-03-14, effective 2025-09-01 | https://www.cac.gov.cn/2025-03/14/c_1743654684782215.htm | [official]
[10] People's Daily Online | Notice on issuing the Measures for the Labeling of AI-Generated and Synthesized Content (corroborating the same text) | http://politics.people.com.cn/n1/2025/0314/c1001-40439288.html | [official]
[11] Alibaba Cloud | Ocean Engine performance analysis (Quick Audience) | https://help.aliyun.com/zh/document_detail/170392.html | [official]
