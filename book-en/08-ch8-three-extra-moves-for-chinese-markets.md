# Chapter 8: Three Extra Moves for Chinese Markets

GEO used to be a matter of bringing the overseas recipe over — hit Reddit, fill in the wiki, turn your official site into a page that can be cited. Now Chinese is a different foundation: your content grows inside the platform's container, and the customer's way of asking, the entry points, and the handoff all sit inside the wall. What you need to do is keep the mechanism and redo the playbook — recognize the terrain first, then decide where the money goes.

The Chinese corpus is another terrain, and how customers ask inside Doubao (Chinese: 豆包), Kimi, and WeChat (Chinese: 微信) is completely different. So this chapter gives you 5 methods for re-landing the points above in Chinese.

---

## Method 1: Start by recognizing that Chinese is walled-garden terrain

**What to do**: Go through the overseas GEO playbook item by item, check whether the raw material is present, and only then decide whether to spend the money.

**How**

1. Write down the difference between the two foundations. On the open web the unit of content is the URL: a public page can be read by anyone, and reputation travels from one page to another through backlinks. In a walled garden the unit of content is the account and the App: WeChat Official Account (Chinese: 公众号) articles, Douyin (Chinese: 抖音) videos, Xiaohongshu (Chinese: 小红书) notes, and Taobao (Chinese: 淘宝) product pages grow inside the platform's container, are invisible across platforms, are not indexed externally by default, and the power of distribution sits with the platform algorithm and in-app search.
2. Take the overseas recipe checklist and compare it item by item against Chinese, asking only one question: "is the raw material here?" Reddit, the wiki, YouTube, backlinks, structured pages. Whichever item's raw material is absent, that item cannot be done.
3. Write the conclusion as a switch: a playbook holds only when its raw material is present. When the raw material is absent, the same money spent on the same actions returns zero.
4. Accept that the closedness of the Chinese internet is a long-term default. On September 13, 2021, at a State Council Information Office press conference, MIIT (Chinese: 工信部) listed "blocking URL links" as one of the key problems in the special rectification of the internet industry, convened administrative guidance meetings with Alibaba (Chinese: 阿里巴巴), Tencent (Chinese: 腾讯), ByteDance (Chinese: 字节跳动), and others, required that blocking be lifted to standard within a deadline, and characterized the matter as harming the user experience, damaging user rights, and disrupting market order [third-party reported]. Having to launch a dedicated special campaign just to require that "links open" is itself proof that links not opening is the default state.

**Example**: Move "hit Reddit + Chinese Wikipedia + listicle articles" into Chinese and all three raw materials are absent — Chinese buyers mostly do not go to Reddit, and Chinese entry points mostly do not cite it; the entry count and update activity of Chinese Wikipedia cannot support the commercial corpus of a category; YouTube's counterpart in Chinese commercial contexts is Douyin and Bilibili (Chinese: 哔哩哔哩), while Douyin's comments and videos are themselves inside the walled garden, not public pages any engine can crawl. The reason that overseas correlation study writes "hit third-party platforms" as the recipe is that it measured the signals most correlated with AI visibility as YouTube mentions and branded web mentions, with brand mentions overall about 3 times traditional backlinks, while the number of content pages is almost irrelevant [vendor claim] — this conclusion holds on the open web, but move it inside the wall and the raw material is gone. **Composite sketch | constructed from common industry patterns, not a named event**: when some Chinese SaaS and consumer-goods companies go overseas, they still lay out content platforms first according to the domestic model, and only when they turn around to ask English entry points do they discover they have never once appeared in the English candidate set — the time was not wasted, it was spent on a stage English buyers do not watch.

**Pitfalls**: Confirm whether the raw material is present before deciding on the recipe. The actions themselves are not wrong; the mistake is assuming that the two foundations are the same.

## Method 2: Run a bilingual entry-point audit with the same set of questions

**What to do**: Take the buyer's real questions, ask them once on each of the Chinese and English entry-point sets, and put the two candidate sets side by side.

**How**

1. Build a bilingual question set. Take 10–20 real buyer questions and write them in both Chinese and English. Note: this is not translation — the Chinese version is written the way a Chinese buyer asks ("a 50-person SaaS company buying CRM"), and the English version the way an English buyer asks ("50-person SaaS company, under $300/month").
2. Weight the two sides of entry points equally. Chinese side: Doubao, DeepSeek, Kimi, Yuanbao (Chinese: 元宝), plus WeChat Search (Chinese: 微信搜一搜), Douyin Search (Chinese: 抖音搜索), and Xiaohongshu Search (Chinese: 小红书搜索); overseas side: ChatGPT, Google (including AI Overviews / AI Mode), Gemini, and Perplexity, plus Google organic search as the control baseline. Rank priority by "where your customers are", but both sides must be tested at the same time — testing only one side is no audit at all.
3. Fix the sampling discipline: run every question on every entry point at least 3 times; record the date, model / product version, whether it was online, and whether it was logged in each time; extract the lists with model extraction, not keyword regexes (a regex will treat a sentence fragment like "suitable for a 50-person company" as an entity name); where a channel is missing, mark it as missing honestly and do not substitute another model's results; open a fresh environment with no history, copy the questions verbatim, and do not "optimize".
4. Compute only three numbers: the mention rate (the share of samples in which you are mentioned — the denominator is the number of samples, not the number of questions), stability (the overlap of lists from repeated asks on the same entry point), and cross-entry / cross-ecosystem overlap (the overlap of candidate sets between different entry points and between Chinese and English).
5. For products with retrieval, record the cited domains that appear in each answer and invert them into a "list of sources to win over" — this list is the real allocation table for your content budget over the next six months.

**Example**: The book's editorial team ran one round of our own measurement (2026-09-13): 6 real procurement questions (3 Chinese-English pairs, covering CRM, MES, and study-abroad agencies) × 5 model channels × 2 repeats per question, yielding 51 valid answers. Asking the same question twice in a row on the same model, the list overlap was only 22%–56%; switching to another model, the pairwise overlap was only 4%–21%, and the union of four models' lists reached 43 entities; the cross-language overlap of the Chinese and English list pairs was 8%–26%; the study-abroad agency group was the only one with an entity present in both languages (IDP) [our own measurement]. One more detail: the English phrasing kept the geographic anchor "East China", and the English entry points also brought in Yonyou (Chinese: 用友), Kingdee (Chinese: 金蝶), and Digiwin (Chinese: 鼎捷) — the anchor itself is a variable.

**Pitfalls**: Testing only one side. Test only the Chinese side and you see the distribution inside the wall; test only the English side and you know nothing about the Chinese battlefield.

## Method 3: First build the public assets that can be read outside the wall

**What to do**: Externalize the facts with the most value inside the wall into content that can be publicly crawled — this step is 0 to 1, not optimization.

**How**

1. Distinguish the nature of the two problems. Overseas is "you already have a pile of pages; optimize the probability that they get cited" — a probability problem that can be A/B tested and iterated; Chinese may be "you have no assets readable outside the wall at all; you must first externalize the facts with the most value inside it into public content" — an asset problem, from 0 to 1. Confusing the two is the most common strategic error Chinese teams make with GEO.
2. Split content inside the wall into two layers, "facts" and "container": parameters, specifications, data, and cases are facts; Official Account layouts, short-video edits, and DM scripts are the container. Facts can be redone outside the wall; the container cannot be moved out.
3. Prioritize externalizing three things: press releases, encyclopedia entries, content that industry sites can republish, and your own official-site pages — these are the raw material that Chinese entry points can still read today.
4. Do not expect platform content to be read outside the wall. Official Accounts built up over years, tens of thousands of Xiaohongshu notes, and hundreds or thousands of short videos are not externally indexed by default; the more carefully you cultivate content inside the wall, the more likely it is that "the description of you outside the wall is not written by you" [our judgment].

**Example**: A marketing vendor's self-run measurement (as of September 2026, 14,750 buyer questions × four platforms ChatGPT / Perplexity / Claude / Gemini) reports: 51.7% of AI citations point to brands' own official-site pages, guides and blogs account for 14.3%, and the rest flows to third-party editorial content [vendor claim]. This figure was measured on the open web and can only indicate an order of magnitude; but the mechanism it points to is clear — as long as your site can be read, it is your biggest lever. Where official sites are indexed, "official site first" leads to redoing pages; where official sites are not indexed, the same sentence leads to moving the facts outside the wall first.

**Pitfalls**: Treating "raise the probability of being cited" as the first step. You are doing probability optimization while what you lack is assets — the budget is spent and there is still nothing to cite.

## Method 4: Redo one piece of material per platform, and catch the customer inside the wall

**What to do**: The Chinese ecosystem's conversion loop is designed to "close inside the platform", so content, search, the handoff, and lead capture have to run end to end within one platform.

**How**

1. Accept the redo cost: the same material must be redone per platform as image-and-text posts, short videos, livestreams, and DM scripts, and one production run is valid for only one platform.
2. Move the handoff point forward into the content: say it clearly in the video — "DM me", "tap here to leave your details" — and do not leave the handoff to an official site outside the wall, because platforms actively block external links.
3. Treat "diverting traffic off-platform is strictly prohibited" as a design premise, not a prohibition: if the customer is seeded on Xiaohongshu, complete the DM or the lead capture on Xiaohongshu and do not pull them off-platform.
4. Run on a fixed cadence: image-and-text posts weekly, short videos weekly, livestreams per campaign, and DMs answered 24/7 by a person or by AI. Content inside the platform, search inside the platform, handoff inside the platform, and the transaction back inside the platform — drop one of the four steps and customers leak away.

**Example**: A channel review from the education-and-training industry sets out a Chinese division of labor: ground promotion and outbound calls suit community-based and newly opened campuses, Douyin suits institutions with content capability to amplify exposure, Dianping (Chinese: 大众点评) catches price-comparing users with intent to visit, the WeChat ecosystem handles private-domain retention, and Xiaohongshu is treated as the key platform for cold-start new growth; the article cites platform data saying Xiaohongshu has 300 million monthly active users, a monthly search penetration of 70%, and about 200 million users a month actively seeking purchase-decision advice, and notes that Xiaohongshu strictly prohibits diverting traffic off-platform [third-party reported: platform data relayed]. An education institution uses a multi-model hybrid Agent for 24/7 automated reception and tiered follower follow-up on Douyin DMs, aggregating more than 100 accounts, claiming it independently handles over 85% of professional inquiries at night, a 580.6% increase in DM lead capture, and a 4.6× overall ROI improvement [vendor claim]. On the private-domain side, a retail white paper states that its platform data shows WeCom (Chinese: 企微) private-domain users have a repurchase rate 2.8 times higher than public-domain users and more than 45% higher value per customer [vendor claim].

**Pitfalls**: Treating platform content as an asset you can just carry away. In-platform content cannot get out, and off-platform traffic platforms will not let you in — both ends must be redone according to platform rules.

## Method 5: Rank entry points by where the customer is, and look at each platform's own AI separately

**What to do**: Chinese entry points are fragmented; first rank them by "where your customers are", then measure each entry point's citation sources one by one.

**How**

1. List the Chinese entry points: Doubao, DeepSeek, Kimi, Tencent Yuanbao, Tongyi (Chinese: 通义) / Quark (Chinese: 夸克), and Ernie (Chinese: 文心), plus the three in-platform search entry points WeChat Search, Douyin Search, and Xiaohongshu Search.
2. Ask each entry point the same batch of questions once, record the cited domains that appear in the answers, and only after forming a distribution decide the content budget. For the composition of citation sources across Chinese entry points, this book currently has no cross-entry measured data; use it as a hypothesis pending verification.
3. Look separately at the AI entry points that "grow inside the body of a walled-garden company": Doubao grows inside the ByteDance ecosystem, Yuanbao inside the Tencent ecosystem. For such an entry point, what can it read first — content inside its own wall, or content outside it? For now there is only a hypothesis, no data [our judgment].
4. Do not treat AI assistants as the whole of Chinese entry points. Chinese B2B buyer research falls heavily on trade shows, acquaintances, industry WeChat groups, and Baidu (Chinese: 百度) / Zhihu (Chinese: 知乎), and this is especially true for buyers at industrial-belt companies — **its buyer does not ask inside AI; it asks in the group chat.**

**Example**: A Chinese GEO industry research report states that Doubao, DeepSeek, Tencent Yuanbao, and Qwen (Chinese: 千问) grow explosively and contribute the main increment through ecosystem advantages or vertical scenarios, with users concentrating toward top Apps; more than 40% of users have shifted the center of gravity of their searching from traditional search engines to AI search, and more than half use both; the misconception the report singles out is "understanding AI brand strategy with the mindset of traditional search engines and performance advertising" [third-party secondary: quantitative conclusions not item-by-item verifiable]. CNNIC's 56th Statistical Report on Internet Development in China says that 80.9% of generative AI users use it for answering questions, and that as of March 2025 a total of 346 generative AI services had completed filing [official].

**Pitfalls**: Treating "AI search" as a single channel. The same analysis of 680 million citations says only 11% of domains are cited by both ChatGPT and Perplexity [vendor claim] — even inside one ecosystem, AI search is not a single channel; across ecosystems, even less so.

---

## Notes for this chapter

- The bilingual audit measures the model-memory layer of a bare API, not consumer AI search products with live retrieval (ChatGPT Search, Perplexity, AI Overviews, Chinese assistants with retrieval). It answers "how the model-memory layer organizes the candidate set" and cannot be extrapolated to "the citation behavior of AI search products". [our own measurement]
- The cross-language overlap of 8%–26% is sensitive to definition: recomputing the raw data with two other algorithms gives a range of 2.3%–31.2%. The difference comes entirely from the definition of "overlap" (whether models are merged, whether brand names are normalized). The direction (the two lists barely intersect) is usable; the specific percentages are not citable as precise values. [our own measurement]
- The two points "Chinese entry points rely mainly on publicly crawlable second-hand information" and "platform content cannot be read outside the wall" are currently mechanism hypotheses, not measured conclusions; this book still has no measurement of the citation-source composition of Chinese entry points. [our judgment]
- The 51.7% item comes from a tool vendor's self-run study and its sample basis has not been independently verified; the 680-million-citation analysis likewise comes from a tool vendor's self-run study, with neither sample nor method independently verified. Both are used only to judge order of magnitude. [vendor claim]
- Xiaohongshu's 300 million monthly active users, 70% search penetration, and about 200 million users a month seeking purchase-decision advice come from a third-party article relaying Qiangua Data's (Chinese: 千瓜数据) 2025 Active User Research Report; this round saw only the relay, not the original report. [third-party secondary]

## Sources for this chapter

[1] China News Service | MIIT: blocking URL links is one of the key problems in the special rectification of the internet industry (2021-09-13, State Council Information Office press conference) | https://www.chinanews.com/cj/2021/09-13/9564236.shtml | [third-party reported]
[2] China Internet Network Information Center (CNNIC) | 56th Statistical Report on Internet Development in China (2025-07-21, data as of June 2025) | https://www.cnnic.net.cn/n4/2025/0721/c88-11328.html | [official]
[3] Boring Marketing | AI brand visibility statistics (14,750 buyer questions × four platforms, data page updated in real time) | as of 2026-09 | https://boringmarketing.com/ai-visibility-statistics | [vendor claim]
[4] Leapd | Analysis of 680 million AI citations: ChatGPT, Google AI Overviews, and Perplexity source information differently | 2026-04 | https://www.leapd.ai/blog/ai-visibility/how-chatgpt-google-ai-overviews-and-perplexity-source-information-in-2026 | [vendor claim]
[5] Ahrefs | Studying 75,000 brands: what determines whether a brand is recommended in AI answers | 2025-12 | https://ahrefs.com/blog/ai-brand-visibility-correlations/ | [vendor claim]
[6] Chinese GEO industry research report (republished on Zhihu / Sina Finance) | 2026 | https://zhuanlan.zhihu.com/p/2012459780288046392 | [third-party secondary: mostly image-and-text, quantitative conclusions not item-by-item verifiable]
[7] Jiaoyujie | Why is Xiaohongshu the next customer-acquisition battlefield for tutoring institutions? | 2026 | https://www.jiaoyujie365.com/N/2411.html | [third-party reported: platform data relayed from Qiangua Data's 2025 Active User Research Report]
[8] Laigu Pro | Case study: AI DM automation for Douyin customer acquisition in the education industry | 2026-07 | https://laigu.com/blog/教育行业抖音获客用ai私信自动回复30天提升获线/ | [vendor claim]
[9] 36Kr Research Institute / Tencent Smart Retail | 2024 White Paper on Private-Domain Operations and Omnichannel Growth in China | https://36kr.com/p/2684930182745348 | [vendor claim: data self-reported by the report's authors]
[10] Our own measurement 1 | Multi-model measurement of the candidate set | 2026-09-13 | Methods and raw data: `实测/实测1-候选集多模型/` (`实测报告.md`, `结果.csv`, `raw_with_vendors.json`, `问题集.json`) | [our own measurement]
