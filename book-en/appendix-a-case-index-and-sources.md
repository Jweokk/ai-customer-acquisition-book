# Appendix A · Case Index and Sources

This appendix is the book's tiered ledger: every source carries its **nature**, its **data point in time** and its **link test status**; every case carries whether it is **named and verifiable**. Any figure whose original source cannot be traced is not written into the book; any passage that uses a composite profile is explicitly flagged, both in the body and in this section.

## A.1 How source tiers are defined

| Source tier | Meaning | Rules for use |
|---|---|---|
| [official] | Official documents, official blogs, financial filings and official releases from an institution or platform | May be cited directly, with the publisher and date noted |
| [third-party verified] | Independent third-party research, academic papers, authoritative media reports | Must be checked against the original report/paper page |
| [vendor claim] | Vendor self-reported data, self-run benchmarks, advertorials and press releases | A lead only, **never to be treated as fact**; the vendor's identity and interest must be disclosed when citing |
| [our judgment] | The authors' inference | Kept in a separate column from fact; readers may challenge it |
| [our own measurement] | Evidence collected by this book itself | Method, sample, time and boundaries must be given; reproducible and falsifiable |

## A.2 Key-figure verification ledger (verified)

| No. | Figure | Original source | Nature |
|---|---|---|---|
| N-01 | US Google zero-click rate 68.01% (Jan–Apr 2026); 60.45% in 2024; about 45% a decade ago | SparkToro, 2026-06-08 (data source Similarweb; Datos for 2024) | [third-party verified] |
| N-02 | AI Mode monthly actives above 1 billion (Gemini 3.5 Flash as the default model) | Google official blog, 2026-05-20 (announced at I/O 2026) | [official] |
| N-03 | With an AI summary present, traditional-result clicks are 8% versus 15% without one; links inside the summary get 1% clicks; 18% of searches contain an AI summary; 88% of summaries cite more than three sources | Pew Research Center, 2025-07-22 (sample: 900 US adults, March 2025 data) | [third-party verified] |
| N-04 | Google bulk-sending requirements: spam-complaint-rate target < 0.1%, never to reach 0.3%; SPF/DKIM/DMARC and one-click unsubscribe required | Gmail official help page | [official] |
| N-05 | FCC declaratory ruling: AI-generated voice counts as "artificial or prerecorded voice" under the TCPA (2024-02-08) — without prior consent it is unlawful | FCC official ruling document (FCC-24-17) | [official] |
| N-06 | FTC final rule on fake reviews and testimonials: announced 2024-08-14, effective 2024-10-21 (16 CFR Part 465) | FTC press release + US Federal Register | [official] |
| N-07 | China generative-AI users 602 million, up 141.7% from the end of 2024, penetration 42.8% (as of 2025-12) | CNNIC 57th Statistical Report on China's Internet Development (published 2026-02-05) | [official] |
| N-08 | 6sense 2025 Buyer Experience Report: 85%–95% of purchases come from the "day-one list"; 80% of won deals go to the vendor preferred before first contact; 61% of evaluation is completed before contact | 6sense Science of B2B | [vendor claim] |
| N-09 | Gartner forecast: traditional search volume down 25% by 2026 (published 2024-02-19; a forecast) | Gartner press release | [official: forecast] |

## A.3 Named case index

| Case | Chapter | Point | Verifiability |
|---|---|---|---|
| Chegg admitted on its earnings call that ChatGPT was hitting new-customer growth; shares fell −48.41% the next day | Ch.2 / Ch.10 | The direct impact of gateway migration on an incumbent acquisition model | Named and verifiable (earnings filing and media reports) |
| Stack Overflow "Code Red": 10% of staff shifted to firefighting; three years later it moved to B2B SaaS | Ch.2 / Ch.10 | An organization-level response after a traffic gateway is drained | Named and verifiable (public interviews) |
| Stereogum ad revenue −70%, move to subscriptions (first-person account signed by the founder) | Ch.1 / Ch.10 | Media survival in the zero-click era | Named and verifiable (signed first-person account) |
| Cursor's support bot invented a "single-device policy"; users publicly cancelled and the founder apologized | Ch.7 / Ch.17 | The cost of AI promises that are not true | Named and verifiable (media reports) |
| Bellingham, US: a staffer used ChatGPT to draft slanted tender conditions; a $2.7 million contract went to a pricier preferred vendor; the city opened an investigation | Ch.7 / Ch.13 | Buy-side AI use equally needs authorization and an audit trail | Named and verifiable (media reports) |
| Moffatt v. Air Canada (2024 BCCRT 149): a company is liable for its chatbot's misstatements | Ch.7 / Ch.17 | "The AI said it" is no defence | Named and verifiable (ruling text) |
| A Chevrolet dealership's AI support agent was induced to agree to "sell a car for $1" | Ch.13 / Ch.17 | A textbook case of missing price authority | Named and verifiable (media reports) |
| CNET used an in-house AI tool to mass-produce personal-finance articles, paused it after corrections | Ch.14 | Industrial-scale content burns through byline credibility | Named and verifiable (media investigation) |
| WeChat (Chinese: 微信) banned the third-party add-on WeTool (2019) | Ch.10 / Ch.11 | Automating personal WeChat is a red line | Named and verifiable (media reports) |

## A.4 Composite-profile list

Any passage in the body that uses a "composite profile" is built from widely observed industry patterns and is **not a named event**; the body flags this explicitly. Current list:

| Location | Profile subject | Label |
|---|---|---|
| Ch.1 | An industrial-equipment maker that treats a single AI-visibility test as a conclusion | Composite profile ｜ Built from widely observed industry patterns, not a named event |

## A.5 Our own measurement archive

| Measurement | Content | Method archive |
|---|---|---|
| Measurement 1 | Multi-model test of the candidate set: 6 questions (3 Chinese–English pairs) × 5 model channels × 2 runs; 51 valid answers | See the repository folder `实测/实测1-候选集多模型/`: test report, raw answers, extraction results, results table, re-run script |

## A.6 Figures not adopted (listed for reference)

The following figures appear in industry discussion but are **not adopted by this book**, either because the original source could not be traced or because the definition does not match. If a reader sees these claims in some article, they can come back to this table to check why the book did not write them: median industry conversion rates for Leads→MQL→SQL, monthly actives and search penetration for the various content platforms (QuestMobile / Xiaohongshu / Douyin official figures), G2 and Forrester surveys of buyers' AI usage, Ahrefs and Seer studies of CTR decline, McKinsey's day-one-list share, and GDPR and EU AI Act fine and timeline details.

## A.7 Industry figures read but not written into the body (listed for reference)

These sources appeared in early drafts as reference points for industry differences; after the formal draft deleted the whole "industry landing table" research device, the body no longer cites them. They are kept here so that readers and later versions can trace the book's choices:

- Bartoli Consulting Group｜B2B Manufacturing SEO Case Study: Electronic Power Design｜https://www.bartoliconsulting.com/case-studies/seo-case-studies-b2b-manufacturing｜[vendor claim]
- Dayu Zhiyuan (Yixunpan) (Chinese: 大鱼致远（易询盘）)｜B2B Foreign-Trade Social-Media Marketing Project Fit Guide｜https://www.rocforever.com/cn/B2B-n6595.html｜[vendor claim]
- CNBC｜Amazon faces a dilemma: fight AI shopping agents or join them｜2025-12-24｜https://www.cnbc.com/2025/12/24/amazon-faces-a-dilemma-fight-ai-shopping-agents-or-join-them.html｜[third-party reported]
- Xiaoman Technology OKKI (Chinese: 小满科技 OKKI)｜Relayed from a Shuzhi Qianxian interview piece (AI overall adoption rate 75%; iResearch 2024 foreign-trade B2B SaaS tools share 14.7%)｜https://mp.m.ofweek.com/ai/a456714443567｜[third-party reported]
- Laigu Pro (Chinese: 来鼓 Pro)｜New Oriental Douyin (Chinese: 抖音) DM AI reception case｜2026-07｜https://laigu.com/blog/教育行业抖音获客用ai私信自动回复30天提升获线/｜[vendor claim]
- 21st Century Business Herald｜Securities-firm digital customer acquisition: the SAC's review of 19 securities firms' wealth-management digitalization cases｜2025-08-08｜https://www.21jingji.com/article/20250808/herald/15e5a6d995898e427b2a6496ee4e820a.html｜[third-party reported]
- eMarketer｜FAQ on GEO and AEO: Where AI search and SEO overlap in 2026｜2026-04｜https://www.emarketer.com/content/faq-on-geo-aeo--where-ai-search-seo-overlap-2026｜[third-party reported]

## A.8 Case pool (named and verifiable, including those not used in the body)

This table is the complete ledger of the case-gathering effort: every entry meets three conditions — **named** (company / product / institution), **URL tested reachable**, and **a sentence supporting the conclusion readable at the source**. Those marked in the "Used in" column have been written into the body; those marked "not used in the body" were collected this round but not used, left for later versions and for readers to check themselves.

| Case (named) | Source tier | Source | Used in |
|---|---|---|---|
| Amazon**：Customer Obsession + Working Ba | [official] (codes) + [third-party: former Amazon executive | https://www.amazon.jobs/content/en/our-workplace/leadership-principles ; https://workingbackward | not used in the body |
| Microsoft**：Customer Connection Program ( | [official] | https://techcommunity.microsoft.com/blog/microsoftintuneblog/announcing-the-microsoft-management | Ch.1, Method 4 |
| Intuit**：Design for Delight — Follow-Me- | [official] (Intuit Inc. copyright doc | https://static1.squarespace.com/static/62726b549e95bf2087fc2759/t/62ffb171b5c6f01e0ed15a5a/16609 | not used in the body |
| Superhuman**：Product-Market Fit Engine (putting | [third-party: first-person account signed by the founder] | https://review.firstround.com/how-superhuman-built-an-engine-to-find-product-market-fit/ | Ch.1, Method 4 |
| Cloudflare**：block AI crawlers by default + Pay Per Crawl | [official] | https://www.cloudflare.com/press/press-releases/2025/cloudflare-just-changed-how-ai-crawlers-scr | not used in the body |
| Google × Reddit** content licensing (reported at about $60M/year) | [official] (scope of the partnership); the amount is [third-party reported | https://blog.google/company-news/inside-google/company-announcements/expanded-reddit-partnership | not used in the body |
| The Atlantic × OpenAI** content and product partnership | [official] | https://www.theatlantic.com/press-releases/archive/2024/05/atlantic-product-content-partnership- | not used in the body |
| News Corp × OpenAI** multi-year global partnership | [third-party verified: authoritative media] | https://www.cnbc.com/2024/05/22/newscorp-and-openai-strike-multi-year-partnership-deal-to-use-jo | not used in the body |
| OpenAI ChatGPT Instant Checkout** (buyer age | [third-party verified: authoritative media] | https://www.cnbc.com/2025/09/29/chatgpt-instant-checkout-etsy-shopify.html | not used in the body |
| Amazon Rufus** (in-site AI shopping assistant) | [vendor claim] (Amazon self-reported) | https://www.aboutamazon.com/news/retail/amazon-rufus-ai-assistant-personalized-shopping-features | not used in the body |
| Estée Lauder × OpenAI**：240+ custom GPT | [third-party reported] (official customer story at openai | https://www.ciodive.com/news/Estee-Lauder-ELC-generative-AI-OpenAI-partnership-ChatGPT/733005 | not used in the body |
| Duolingo**：'AI-first' memo and the reputational backlash | [third-party verified: authoritative media] | https://fortune.com/2025/06/09/duolingo-ceo-surprised-backlash-ai-first-company-announcement | not used in the body |
| Shopify**：'prove AI can't do it, then add people' | [third-party verified: authoritative media] (memo text on X | https://www.cnbc.com/2025/04/07/shopify-ceo-prove-ai-cant-do-jobs-before-asking-for-more-headcou | not used in the body |
| Shopify**：orders from AI search up 15× in a year (positive case) | [third-party compilation: relayed from an earnings call] (original source at | https://detailed.com/public | not used in the body |
| IAC / People Inc.** (formerly Dotdash Meredith)： | [third-party verified: authoritative media] | https://digiday.com/media/publishers-swap-traffic-angst-for-strategy-in-q3-earnings | not used in the body |
| Penske Media v. Google**：the first publisher suit over AI summaries | [third-party verified: authoritative media] | https://techcrunch.com/2025/09/14/rolling-stone-owner-penske-media-sues-google-over-ai-summaries | not used in the body |
| Encyclopaedia Britannica v. Perplexity** | [official] (plaintiff press release) | https://www.prnewswire.com/news-releases/britannica-files-copyright-and-trademark-infringement-l | not used in the body |
| Epic Games 'Fortnite' | [authoritative media: citing an Apple official statement] | https://www.cnbc.com/2020/08/13/apple-kicks-fortnite-out-of-app-store-for-challenging-payment-ru | Ch.10, Method 1 |
| Valve 'Steam Link' (iOS version) | [authoritative media: citing a Valve statement] | https://www.cnet.com/tech/mobile/valve-accuses-apple-of-rejecting-steam-link-mobile-streaming-ap | not used in the body |
| Apple (App Store, China region) | [authoritative media] | https://xinwen.bjd.com.cn/content/s5f2624fee4b0d7d5fee65d92.html | Ch.10, Method 1 |
| Apple (corroborating item in the same case · The Paper) | [authoritative media] | https://www.thepaper.cn/newsDetail_forward_8420791 | not used in the body |
| Patuoxun (Chinese: 帕拓逊) (main brand Mpow) | [authoritative media] | https://m.bjnews.com.cn/detail/162969795414530.html | Ch.10, Method 5 |
| Sunvalley (Chinese: 泽宝) (parent Xinghui Co.; brands RAVPower / Taotr | [authoritative media] | https://m.bjnews.com.cn/detail/162969795414530.html / https://m.caixin.com/m/2021-07-21/10174347 | Ch.10, Method 5 |
| Aukey (Chinese: 傲基) (a different company from Sunvalley above) | [authoritative media] | https://m.bjnews.com.cn/detail/162969795414530.html | not used in the body |
| Youshu (Chinese: 有棵树) (a subsidiary of Tianze Information) | [authoritative media: citing a listed-company announcement] | http://www.nbd.com.cn/rss/toutiao/articles/1853164.html | not used in the body |
| Tongtuo Technology (Chinese: 通拓科技) (a subsidiary of Huading Co.) | [authoritative media: citing a listed-company announcement] | https://m.bjnews.com.cn/detail/162969795414530.html | not used in the body |
| Winona (Chinese: 薇诺娜) (domestic beauty brand) | [official: Tencent Marketing Academy (platform-reported results)] | https://eschool.qq.com/Solution/ListDetail/pd-7788 | Ch.10, Method 3 |
| Sephora | [official: Tencent Marketing Academy (platform-reported results)] | https://eschool.qq.com/Solution/ListDetail/pd-7788 | not used in the body |
| OMEGA | [official: Tencent Marketing Academy (platform-reported results)] | https://eschool.qq.com/Solution/ListDetail/pd-7788 | not used in the body |
| HP | [vendor claim: Amazon Ads official case library] | https://advertising.amazon.com/solutions/products/sponsored-brands | Ch.10, Method 4 |
| Taobao listings (Chinese: 淘宝宝贝) (Zhitongche / keyword bidding, Alimama official figures) | [official: Alimama] | https://www.alimama.com/news_detail.htm?contentId=430 | Ch.10, Method 4 |
| Zynga | [authoritative media: citing a Zynga SEC filing] | https://www.cnet.com/home/smart-home/zynga-shares-soar-on-facebook-ipo | Ch.10, Method 5 |
| Facebook (2018 News Feed algorithm overhaul) | [authoritative media: citing a Facebook official statement ( | https://www.theguardian.com/technology/2018/jan/11/facebook-news-feed-algorithm-overhaul-mark-zu | not used in the body |
| WeChat Open Docs 'Mini Program Search Optimization Guide' | [official] | https://developers.weixin.qq.com/miniprogram/dev/framework/search/seo.html | not used in the body |
| WeChat Open Docs 'Service Providers Receiving Mini Program Violation Penalties on Behalf of Developers' | [official] | https://developers.weixin.qq.com/doc/oplatform/Third-party_Platforms/2.0/product/illegalEvent.ht | not used in the body |
| WeChat Open Class PRO 2023 (reprinted by Xinhuanet) | [official: platform-reported] | https://www3.xinhuanet.com/tech/20230111/b4286147d13f4bb6a444666b31f8a4d4/c.html | not used in the body |
| Amazon seller success-story library (official Amazon) | [vendor claim] | https://sell.amazon.de/informationen/verkaufer-geschichten?mons_sel_locale=zh_CN | not used in the body |
| Gary Vaynerchuk / VaynerMedia** (personal brand + team) | [first-person account] | https://garyvaynerchuk.com/the-garyvee-content-strategy-how-to-grow-and-distribute-your-brands-s | Ch.12, Method 1 |
| Moz** (Whiteboard Friday series) | [institutional methodology] | https://moz.com/blog/repurpose-content-with-ai-whiteboard-friday | not used in the body |
| East Buy (Chinese: 东方甄选)** (Dong Yuhui clip licensing) | [authoritative media: Sohu Tech] | https://www.bianews.com/news/details?id=165035 | Ch.12, Method 1 |
| WeChat Official Accounts Platform (Chinese: 微信公众平台)** first case of its 'content-laundering complaint panel' (the account **Jingyingshuo** (Chinese: 精英说) accused of laundering from * | [official reprint: National Copyright Administration site] | https://www.ncac.gov.cn/xxfb/yjdt/201901/t20190107_49426.html | not used in the body |
| Douyin** (copyright-infringement governance, first half of 2021) | [authoritative media: China Securities Journal] | https://cs.com.cn/sylm/jsbd/202106/t20210624_6178255.html | not used in the body |
| Douyin** 'Code of Conduct for Misbehavior by Matrix Accounts' | [authoritative media: Xinhuanet (relaying an official new rule)] | http://www.xinhuanet.com/tech/20231130/c932193c6db34a079588421d9706516c/c.html | Ch.12, Method 4 |
| YouTube** (channel monetization policies: | [official rules] | https://support.google.com/youtube/answer/1311392?hl=en | Ch.12, Method 4 |
| WeChat Official Accounts Platform** (new rule against 'non-human automated creation') | [authoritative media + official response] | https://www.yicai.com/news/103125654.html | not used in the body |
| Gong** (Gong Labs) | [vendor self-reported] | https://www.gong.io/blog/taking-the-guesswork-out-of-sales-call-effectiveness | Ch.12, Method 5 |
| Ahrefs** (study of its own logs + traffic data) | [vendor self-reported] | https://ahrefs.com/blog/llmstxt-study | not used in the body |
| Strava** (Year in Sport: Trend Report) | [vendor self-reported: official press release] | https://press.strava.com/articles/strava-releases-12th-annual-year-in-sport-trend-report-2025 | Ch.12, Method 5 |
| Spotify** (annual Wrapped campaign) | [official] | https://newsroom.spotify.com/2025-12-03/2025-wrapped-user-experience/ | not used in the body |
| Cyberspace Administration of China (Chinese: 中央网信办)** notice on cases of 'self-media' failing to label properly (named accounts: Douyin's 'Qingqing Guoji' and 'Jike Kepuguan | [official notice] | https://www.cac.gov.cn/2026-05/03/c_1779492291101867.htm | not used in the body |
| WeChat Channels (Chinese: 微信视频号)** 'Announcement on Strengthening the Governance of AI-Generated Content' | [state media reprint of an official announcement: Qingdao Daily (source: WeChat Channels | https://www.dailyqd.com/guanhai/438720_1.html | not used in the body |
| Xiaohongshu** 'AI Governance Rules Announcement' | [authoritative media relay: ITHome / Sina Tech] | https://finance.sina.com.cn/tech/digi/2026-08-07/doc-inimnram0019917.shtml | not used in the body |
| CAC** first phase of the 'Qinglang · Cracking Down on AI Technology Abuse' campaign (involving Tencent, Weibo, Douyin, Ali | [official notice] | https://www.cac.gov.cn/2025-06/20/c_1752129980667315.htm | not used in the body |
| HubSpot Website Grader | [official] (HubSpot official press release) | https://www.hubspot.com/blog/bid/5539/website-grader-analyzes-over-2-million-sites | Ch.15, Method 1 |
| Shopify Free Business Name Generator | [official] | https://www.shopify.com/tools/business-name-generator | Ch.15, Method 5 |
| Ahrefs Free Backlink Checker | [official] | https://ahrefs.com/backlink-checker | Ch.15, Method 1 |
| Heroku free plan discontinued | [official] | https://help.heroku.com/RSBRUH58/removal-of-heroku-free-product-plans-faq | Ch.15, Method 4 |
| Railway free allowance: first shut down, then reopened and hard-coded | [vendor claim] (vendor self-reported, including self-reported unit-economics figures) | https://blog.railway.com/p/free-plan | not used in the body |
| Figma pricing, seat and billing revamp | [official] | https://www.figma.com/blog/billing-experience-update-2025 | not used in the body |
| Supabase Free plan limits | [official] | https://supabase.com/pricing | not used in the body |
| Cloudflare Workers Free daily limits | [official] | https://developers.cloudflare.com/workers/platform/limits | not used in the body |
| Stripe MCP server | [official] | https://docs.stripe.com/mcp | not used in the body |
| Linear MCP server | [official] | https://linear.app/docs/mcp | not used in the body |
| GitHub MCP Server | [official] | https://github.com/github/github-mcp-server | not used in the body |
| MCP Registry (the official MCP registry) | [official] | https://blog.modelcontextprotocol.io/posts/2025-09-08-mcp-registry-preview | not used in the body |
| GitHub MCP Registry | [official] (GitHub official blog) | https://github.blog/ai-and-ml/github-copilot/meet-the-github-mcp-registry-the-fastest-way-to-dis | not used in the body |
| Stripe Directory | [official] | https://docs.stripe.com/directory | not used in the body |
| CoSchedule Headline Analyzer | [vendor claim] ('#1' is self-assessed) | https://coschedule.com/headline-analyzer | Ch.12, Method 4 |
| Zapier MCP | [vendor claim] (9,000+ / SOC 2 are self- | https://github.com/zapier/zapier-mcp | not used in the body |
| Sentry MCP | [official] | https://github.com/getsentry/sentry-mcp | not used in the body |
| Cloudflare remote MCP server capability launch | [official] | https://blog.cloudflare.com/remote-model-context-protocol-servers-mcp | not used in the body |
| Cloudflare MCP Server Portals | [official] | https://blog.cloudflare.com/zero-trust-mcp-server-portals | not used in the body |
| Claude Connectors directory | [official] | https://claude.com/connectors | not used in the body |
| MCP Registry publishing guide (quickstart) | [official] | https://modelcontextprotocol.io/registry/quickstart | not used in the body |
| Heroku new low-cost plans Eco / Mini | [official] | https://blog.heroku.com/new-low-cost-plans | not used in the body |
| Ahrefs Free SEO Tools (tools collection page) | [official] | https://ahrefs.com/free-seo-tools | Ch.15, Method 1 |
| Australia's Robodebt (automated debt collection) Royal Commission report | [authoritative media investigation] (Guardian relaying the royal | https://www.theguardian.com/australia-news/2023/jul/07/robodebt-royal-commission-final-report-re | Ch.17, Method 5 |
| Zillow Offers (automated home buying / automated offers) shutdown post-mortem | [company's public post-mortem] (earnings press release filed with the SEC) | https://www.prnewswire.com/news-releases/zillow-group-reports-third-quarter-2021-financial-resul | Ch.17, Method 5 |
| 11x.ai (AI SDR / automated outreach) metrics independently disproven | [authoritative media investigation] (TechCrunch, multiple | https://techcrunch.com/2025/03/24/a16z-and-benchmark-backed-11x-has-been-claiming-customers-it-d | Ch.17, Method 5 |
| Air Canada support bot misstated bereavement fares (Moffatt v. Air Ca | [institution/law-firm analysis] (law firm quoting the ruling text paragraph by paragraph; ru | https://fosterandcompany.com/air-canada-found-liable-for-negligent-misrepresentation-by-chatbot | Ch.17, Method 7 |
| Netherlands' SyRI welfare-fraud risk system (NJCM et al. v. the Dutch State) | [regulator document] (official judgment publication by the Dutch judiciary, | https://uitspraken.rechtspraak.nl/details?id=ECLI%3ANL%3ARBDHA%3A2020%3A1878 | Ch.17, Method 7 |
| Budapest Bank emotion AI analyzing support calls (Hungarian DPA: NAIH-85-3/202 | [regulator document relay] (decision collected by GDPRhub | https://gdprhub.eu/NAIH_(Hungary)_-_NAIH-85-3/2022 | not used in the body |
| Dutch childcare-benefits scandal (Toeslagenaffaire) | [authoritative media investigation] (CNBC) | https://www.cnbc.com/2021/01/15/dutch-government-resigns-after-childcare-benefits-scandal-.html | not used in the body |
| iTutorGroup hiring software automatically rejected applicants aged 55/60+ (EEOC v. | [regulator document] (EEOC press release) | https://www.eeoc.gov/newsroom/itutorgroup-pay-365000-settle-eeoc-discriminatory-hiring-suit | Ch.17, Method 8 |
| Rite Aid store AI facial-recognition false alerts (FTC v. Rite Aid, 2 | [regulator document] (FTC case file + press release) | https://www.ftc.gov/legal-library/browse/cases-proceedings/2023190-rite-aid-corporation-ftc-v | not used in the body |
| RealPage rental algorithmic pricing (DOJ et al. v. RealPage, 2 | [institution/law-firm analysis] (Paul Weiss paragraph-by- | https://www.paulweiss.com/insights/client-memos/practical-takeaways-from-the-doj-s-algorithmic-p | not used in the body |
| DoNotPay 'robot lawyer' + FTC 'Operation AI Comply | [regulator document] (FTC press release + case file) | https://www.ftc.gov/news-events/news/press-releases/2024/09/ftc-announces-crackdown-deceptive-ai | not used in the body |
| FCC penalty over AI-faked Biden voice robocalls (Steve Kramer; Lin | [authoritative media investigation] (NH Public Rad | https://www.nhpr.org/nh-news/2025-06-13/political-operative-fake-biden-robocalls-nh-primary-foun | not used in the body |
| Amazon experimental hiring algorithm discriminated against women | [authoritative media investigation] (Guardian relaying a Reuters investig | https://www.theguardian.com/technology/2018/oct/10/amazon-hiring-ai-gender-bias-recruiting-engin | not used in the body |
| Cursor / Anysphere support bot invented company policy | [institution database] (AI Incident Da | https://incidentdatabase.ai/cite/1039 | not used in the body |
| Klarna AI support 'equal to 700 full-time agents' | [vendor claim] (Klarna official press release) | https://www.klarna.com/international/press/klarna-ai-assistant-handles-two-thirds-of-customer-se | not used in the body |
| DPD support bot went off the rails and was shut down | [authoritative media investigation] (BBC) | https://www.bbc.com/news/technology-68025677 | Ch.17, Method 8 |
| New York City's MyCity official business Q&A bot gave unlawful advice | [institution database] (OECD.AI incident database, index | https://oecd.ai/en/incidents/2024-03-29-3dce | not used in the body |
| FTC 6(b) inquiry into eight 'surveillance pricing' companies | [regulator document] (FTC press release) | https://www.ftc.gov/news-events/news/press-releases/2024/07/ftc-issues-orders-eight-companies-se | not used in the body |
| Luckin Coffee (Chinese: 瑞幸咖啡) | [company filing: SEC prospectus] | https://www.sec.gov/Archives/edgar/data/1767582/000091205719000058/filename1.htm | not used in the body |
| Pinduoduo (Chinese: 拼多多) (PDD Holdings, formerly Pinduoduo) | [company filing: SEC annual report] | https://www.sec.gov/Archives/edgar/data/1737806/000110465922049283/pdd-20211231x20f.htm | not used in the body |
| Dropbox | [company website / official help center] | https://www.dropbox.com/refer | not used in the body |
| Airbnb (Chinese: 爱彼迎) | [company official help center] | https://www.airbnb.com/help/article/3622 | not used in the body |
| Robinhood | [company filing: SEC] | https://www.sec.gov/Archives/edgar/data/1783879/000162828021013318/robinhoods-1.htm | Ch.19, Method 1 |
| Monzo (UK digital bank) | [company annual report] | https://monzo.com/annual-report/2026/Monzo-Annual-Report-2026.pdf | Ch.19, Method 1 |
| HONOR (Chinese: 荣耀) | [company website campaign rules] | https://www.honor.com/cn/msale/yqylhdgz.html | Ch.19, Method 4 |
| Amazon Associates | [company official help center] | https://affiliate-program.amazon.com/help/node/topic/GS4DGSRUYG5BX8E3 | Ch.19, Method 4 |
| Taobaoke / Alimama (Chinese: 淘宝客 / 阿里妈妈) (Alibaba) | [company official developer documentation] | https://open.alitrip.com/docs/api.htm?apiId=62201 | Ch.10, Method 4 |
| Fashion Nova (US fast fashion) | [enforcement action: FTC press release] | https://www.ftc.gov/news-events/news/press-releases/2022/01/fashion-nova-will-pay-42-million-par | not used in the body |
| Sunday Riley Modern Skincare + Devumi | [enforcement action: FTC press release] | https://www.ftc.gov/news-events/news/press-releases/2019/10/devumi-owner-ceo-settle-ftc-charges- | not used in the body |
| The Bountiful Company (parent of Nature's Bounty | [enforcement action: FTC press release] | https://www.ftc.gov/news-events/news/press-releases/2023/02/ftc-charges-supplement-marketer-hija | not used in the body |
| Rytr (AI writing tool) | [enforcement action: FTC press release] | https://www.ftc.gov/news-events/news/press-releases/2024/09/ftc-announces-crackdown-deceptive-ai | not used in the body |
| Sitejabber (GGL Projects, Inc.) | [enforcement action: FTC press release (final order)] | https://www.ftc.gov/news-events/news/press-releases/2025/01/ftc-approves-final-order-against-sit | not used in the body |
| Roomster and its operators + Jonathan Martinez (d/b/a | [enforcement action: FTC press release] | https://www.ftc.gov/news-events/news/press-releases/2022/08/ftc-states-sue-rental-listing-platfo | not used in the body |
| Amazon sues AppSally and Rebatest (two fake-review brokers) | [company official press release: platform enforcement] | https://press.aboutamazon.com/2022/2/amazon-sues-fake-review-brokers-who-attempt-to-profit-from- | not used in the body |
| Amazon + the US Better Business Bureau (BBB) sue Skitsolutionbd; Am | [company official press release: platform enforcement] | https://www.aboutamazon.com/news/policy-news-views/amazons-latest-actions-against-fake-review-br | not used in the body |
| Tripadvisor (Chinese: 猫途鹰) | [company official report / platform enforcement] | https://tripadvisor.mediaroom.com/2025-03-18-Tripadvisors-2025-Transparency-Report-reveals-stron | not used in the body |
| Beijing Haipu Advertising Co., Ltd. (Chinese: 北京嗨噗广告有限公司) | [enforcement action: SAMR official site] | https://www.samr.gov.cn/jjj/sjdt/gzdt/art/2023/art_885915ef69c94901bd4ce6b44d9029bc.html | not used in the body |
| Baoji Haisheng Modern Agriculture Co., Ltd. (Chinese: 宝鸡海升现代农业有限公司) | [enforcement action: Shaanxi Provincial Administration for Market Regulation official site] | https://snamr.shaanxi.gov.cn/sy/sjyw/202309/t20230919_2604145.html | not used in the body |
| Hangzhou Dongtian Technology Co., Ltd. (Chinese: 杭州东田科技有限公司) | [enforcement action: SAMR release, reprinted on a government site] | https://www.qinshui.gov.cn/ztzl_369/cxxcjy_25/bgsx_36/202309/t20230901_1847663.shtml | not used in the body |
| FTC 'Rule on the Use of Consumer Reviews and Testimonials' (16 CFR Part 465) | [regulatory rule text + FTC press release] | https://www.ecfr.gov/current/title-16/chapter-I/subchapter-D/part-465 | not used in the body |

## A.9 Second-round material-mining ledger (growth-hacking material library)

In the second round I swept the growth-hacking material library gathered earlier (`~/wiki/topics/growth-hacking/raw/articles/`, 339 pieces, of which 286 had not previously been cited by this book), section by section, yielding **90** candidates in total. The table below is the complete ledger: items marked "Ch.X, Method N" have been written into the body; those marked "not used in the body" were collected this round but not used, kept for later versions and for readers to check themselves.

Collection discipline: a material summary is a lead only; every item requires fetching the original page at `source_url` and pulling the sentence that supports the conclusion from that page; every URL is tested for reachability one by one; figures whose original publisher cannot be traced are not collected.

| Case (named) | Source tier | Source | Used in |
|---|---|---|---|
| Sage and Paige** (US women's-wear DTC brand) × **Polar Ana | [vendor claim] (the vendor's own case page; the client is named and includes a client-side signed | https://www.polaranalytics.com/case-studies/how-sage-and-paige-transformed-their-digital | not used in the body |
| Apple ATT / Meta** (AdLibrary five-year retrospective) | [third-party verified: industry retrospective] (AdLibrary independent ana | https://adlibrary.com/posts/ios-14-att (**200**) | not used in the body |
| Focus Digital** (digital-marketing agency, 2026 CAC Trends R | [third-party verified: agency's own data report, methodology and definitions public | https://focus-digital.co/customer-acquisition-cost-trends/ (**200**) | not used in the body |
| Digital Applied** (consultancy, CAC Benchmarks 2026 | [third-party verified: compiles 8 sets of public benchmarks, each source labeled] ( | https://www.digitalapplied.com/blog/customer-acquisition-cost-benchmarks-2026-industry ( | not used in the body |
| Jungle** (AI study app, founders Julian / David) × ** | [third-party reported: founder interview] (Superwall | https://superwall.com/blog/this-ai-study-app-makes-usd100k-mo-heres-how-no-code (**200** | Ch.13, Method 3 |
| Recurly** (subscription-billing infrastructure vendor, 2025-12-03 win-back guide) | [vendor claim: including industry data] (Recurly is a billing product | https://recurly.com/blog/customer-winback-strategies-for-subscriptions/ (**200**) | not used in the body |
| N26** (German digital bank) × **Sacra** (company-research firm) | [third-party verified: firm estimate] (Sacra company research, some | https://sacra.com/research/n26 (**200**) | not used in the body |
| Antenna** (US subscription data firm, 2024 year-end roundup) | [third-party verified: data-firm estimate] (Antenna is a third | https://www.antenna.live/insights/antennas-2024-top-subscription-insights-net-churn (**2 | not used in the body |
| Benchmarkit** (2026 B2B SaaS & AI-Native Me | [third-party verified: citing a Benchmarkit report] (ori | https://www.thesaascfo.com/saas-grr-benchmark-2026/ (**200**) | not used in the body |
| Recurly** (subscription-billing platform network data, 2026-07) | [vendor claim: vendor network data] (Recurly is a billing | https://recurly.com/research/churn-rate-benchmarks/ (**200**) | not used in the body |
| ChartMogul** (SaaS retention report, 2,500+ SaaS companies) | [third-party verified] (based on ChartMogul's own platform | https://chartmogul.com/reports/saas-retention-the-new-normal/ (**200**) | not used in the body |
| Booking.com** (experimentation culture) × **Airbnb** (photography experiment) / **Ob | [third-party reported: media] (Observer column, B | https://observer.com/2026/01/why-experimentation-drives-high-performing-companies/ (**20 | Ch.20, Method 4 |
| Case name (named) |  |  | not used in the body |
| SaaS Capital** 2025 private-SaaS retention benchmarks | [third-party verified] (its own annual survey running over a decade, sample = ARR> | https://www.saas-capital.com/blog-posts/what-is-a-good-retention-rate-for-a-private-saas | not used in the body |
| Lenny's Newsletter** GOOD/GREAT retention benchmarks | [third-party verified] (compiles public data with 20 practitioners) | https://www.lennysnewsletter.com/p/what-is-good-retention-issue-29 (200) | not used in the body |
| Duolingo** seven-state growth model | [official] (Duolingo official blog, by Er | https://blog.duolingo.com/growth-model-duolingo (200) | Ch.19, Method 2 |
| Remery** 17 pricing experiments (12 losses, 5 wins) | [third-party reported: the company's own account of its experimental data] | https://remery.ai/blog/saas-pricing-experiments-17-tests-results (200) | not used in the body |
| Tsinghua Business Review A/B testing** (including iQIYI / China Mobile) | [third-party verified: academic journal] (Tsinghua SEM's Tsinghua Business Review 2 | https://www.sem.tsinghua.edu.cn/info/1171/35965.htm (200) | not used in the body |
| MarketerHire** paid-acquisition framework | [third-party verified: industry content] | https://marketerhire.com/blog/paid-acquisition-strategy (200) | not used in the body |
| Zylo** 2026 SaaS pricing trends | [third-party verified] (survey of Zylo's customer network; Gartne | https://zylo.com/blog/saas-pricing-trends (200) | not used in the body |
| Polytraffic** CAC benchmarks by channel | [third-party verified: compilation] (aggregating HubSpot/Prof | https://polytraffic.com/articles/customer-acquisition-cost-by-channel (200) | not used in the body |
| Yueshengshi (Chinese: 粤省事)** (Guangdong provincial government / Digital Guangdong, WeChat mini program + App) | [official] (Digital Guangdong website) + [third-party verified] (Tencent Cloud do | https://www.secrss.com/articles/14012 (200); https://www.digitalgd.com.cn/szgd/yss/ywly_y | Ch.10, Method 3 |
| Shanghai "One-Stop Online Service" / "Suishenban" (Chinese: 上海"一网通办" / "随申办")** (Shanghai municipal government) | [third-party verified] (Jiemian News, citing the deputy director of the Shanghai Big Data Center at | https://m.jiemian.com/article/11828626.html (200) | not used in the body |
| Zheliban (Chinese: 浙里办)** (mobile end of the Zhejiang government service portal) | [official (relayed by official media)] (Xinhuanet relaying Zhejiang Daily, with offici | https://www.news.cn/government/20240625/74eca00cd3bb49129d0318b909d6b1f6/c.html (200) | not used in the body |
| Lalamove (Chinese: 货拉拉)** (intra-city freight platform, prospectus figures) | [third-party verified: citing the prospectus] (Huxiu Miaotou based on a 2025-04 | https://pro.huxiu.com/article/4215577.html (200) | Ch.10, Method 4 |
| Full Truck Alliance / "Yunmanman" (Chinese: 满帮集团 / "运满满")** (digital freight platform, YMM.US) | [third-party verified: citing financial filings] (Securities Daily = relayed from filings; Sina Tech | http://www.zqrb.cn/gscy/qiyexinxi/2025-03-06/A1741232211313.html (200); https://finance.s | not used in the body |
| Temu** (PDD, parent of Pinduoduo, going global) | [third-party verified] (Harvard Business School Working Know | https://www.library.hbs.edu/working-knowledge/how-shein-and-temu-conquered-fast-fashion- | Ch.19, Method 1 |
| Airbnb** (acquiring customers via the Craigslist platform) | [third-party reported: single source, **second-hand relay**, used with caution] | https://growthexpertz.com/growth-hacking-case-studies (200) | not used in the body |
| Shopify partner ecosystem** (App Store + referral partners) | [third-party reported: single source, **second-hand relay**, used with caution] | https://partnerinsight.io/insights/what-does-it-take-to-build-a-thriving-saas-marketplac | Ch.11, Method 1 |
| Fastenal** (US industrial distributor/fastener supplier) | [third-party verified: citing the company annual report] (Dorn Group/M | https://www.dorngroup.com/fastenal-investments-line-extensions-digital-growth/ (200; **requires with | not used in the body |
| Kuaidi100 "Baidiyun" × Langsheng Group (Chinese: 快递100「百递云」 × 朗生集团)** (logistics-SaaS customer case) | [vendor claim: platform self-reported] (a case from Kuaidi100's own official site | https://www.kuaidi100.com/enterprise/customer/langsheng.shtml (200) | not used in the body |
| Sunnystep × SHOPLINE** (footwear brand, Singapore / overseas DTC) | [third-party reported: citing a vendor client, used with caution] (Xiaguangshe report | https://mp.ofweek.com/digitaleconomy/a256714077547 (200) | not used in the body |
| Hotmail** ("PS: I Love You" email signature) | [third-party verified: book excerpt] (TechCrunch book excerpt, fig | https://techcrunch.com/2009/10/18/ps-i-love-you-get-your-free-email-at-hotmail/ (200) | not used in the body |
| Amazon third-party seller marketplace | [third-party reported: single source, second-hand relay] | https://zetetikos.substack.com/p/case-study-how-amazons-flywheel-effect (200)/`.../2026- | not used in the body |
| "Qinwuyuan" (Chinese: "秦务员") (Shaanxi integrated government-services platform) | [official] (published by People's Daily Online; contributing unit = the platform's operations department) | http://politics.people.com.cn/BIG5/n1/2025/1223/c458474-40630249.html (200)/`.../2026-08 | Ch.10, Method 3 |
| Fan Deng Reading (Chinese: 樊登读书) | [third-party verified: self-media relay, figures are the company's own, used with caution] | https://www.sohu.com/a/684937054_121716213 (200) | Ch.12, Method 1 |
| Substack recommendation network | [third-party verified: Chinese second-hand relay (Runwise → Maimai), | https://maimai.cn/article/detail?fid=1797931979&efid=sZR2w6WLVHbUNk2W33BGVQ (200) | not used in the body |
| a16z 'Top 100 Gen AI Consumer Apps' 6th edition (Ca | [third-party verified] (a16z based on SimilarWeb | https://a16z.com/100-gen-ai-apps-6/ (200) | not used in the body |
| Guixingren Pro (Chinese: 硅星人 Pro) 'The 10,000 wild ways to growth-hack an AI product' (Wordware | [third-party verified: media case compilation, each case's data is a media relay, downgr | https://www.woshipm.com/ai/6299942.html (200) | not used in the body |
| Spotify · Discover Weekly | [third-party verified: product data citing Time/Fast Co | https://www.markhub24.com/post/spotify-s-discover-weekly-how-personalization-became-a-co | not used in the body |
| Netflix · recommendation engine (NRE) | [vendor claim: an e-commerce tool vendor's blog relaying Netflix | https://www.rebuyengine.com/blog/netflix (200) | not used in the body |
| 1ClickReport: the May 2026 core update and "the death of programmatic SEO" | [vendor claim: an SEO tool vendor's first-hand client observation, a single firm's 6 | https://www.1clickreport.com/blog/google-may-2026-core-update-programmatic-seo-dead (200 | not used in the body |
| Luckin Coffee (CGO Yang Fei) | [official: financial-filing data] + [first-person account: CGO interview] | https://www.centurium.com/press/…(Centurium Capital interview) (200) | Ch.18, Method 4 |
| Intercom · Fin AI support | [vendor claim: Intercom engineering team's own account (via Ho | https://www.honeycomb.io/resources/case-studies/how-honeycomb-helped-intercom-observe-an | not used in the body |
| Reforge 'growth loops replace the funnel' · Pinterest content loop | [third-party verified] (Balfour / Winters | https://www.reforge.com/blog/growth-loops (200) | not used in the body |
| Notion (disclosed by the company to CNBC) | [third-party verified: disclosed by the company to CNBC] | https://www.cnbc.com/2025/09/18/notion-launches-ai-agent-as-it-crosses-500-million-in-an | not used in the body |
| Zoom | [third-party verified] (revenue and customer counts traceable to Zoom's filings; | https://www.getmonetizely.com/articles/case-study-how-zoom-scaled-pricing-strategy-durin | not used in the body |
| Remery** (B2B workflow-automation SaaS) | [vendor claim] (the company's own account of its A/B experimental data; full pre- | https://remery.ai/blog/saas-pricing-experiments-17-tests-results | not used in the body |
| Shopify App Store (+ partner ecosystem) | [third-party verified] (Partner Insight's | https://partnerinsight.io/insights/what-does-it-take-to-build-a-thriving-saas-marketplac | Ch.11, Method 1 |
| Duolingo** (soft-wall signup page A/B) | [third-party reported] (NoGood post-mortem, citing Duolin | https://nogood.io/blog/duolingo-case-study/ | Ch.19, Method 2 |
| Duolingo** (economics of organic acquisition) | [official] (HBR podcast / case figures; the $2.5 is | https://hbr.org/podcast/2025/04/how-duolingo-aims-to-diversify-beyond-language-learning | Ch.19, Method 2 |
| Hotmail | [third-party relay] (TechCrunch publishing 'Vira | https://techcrunch.com/2009/10/18/ps-i-love-you-get-your-free-email-at-hotmail/ | not used in the body |
| Slack | [third-party reported] (First Round Review | https://review.firstround.com/from-0-to-1b-slacks-founder-shares-their-epic-launch-strat | not used in the body |
| Decagon × Duolingo (Duolingo English Test) | [vendor claim] (Decagon official case page, the client is D | https://www.decagon.ai/case-studies/duolingo | Ch.19, Method 2 |
| Decagon × Chime | [vendor claim] (Decagon official case page; the page notes its own figures | https://www.decagon.ai/case-studies/chime | not used in the body |
| UC Berkeley 'California Management Review' ( | [third-party verified] (UC Berkeley academic journal I | https://cmr.berkeley.edu/2026/04/chatbot-frustration-is-real-hidden-costs-and-best-pract | Ch.16, Method 4 |
| Braintrust 'Best AI customer service agents | [third-party reported] (Braintrust platform comparison report; | https://www.braintrust.dev/articles/best-ai-customer-service-agents-2026 | not used in the body |
| NetEase Zhigi · Yunshang (NetEase Yunshang) (Chinese: 网易智企·云商（网易云商）) AI support / AI private domain | [vendor claim] (NetEase Zhigi · Yunshang official content; case clients are anonymous, | https://grow.163.com/cms/ai-si-yu-wang-yi-zhi-qi-2026-YcKhIBbi.html | not used in the body |
| Luckin Coffee** (co-founder and CGO Yang Fei interviewed, Centurium Capital · Founder Talk) | [vendor claim: a company executive's own interview account, single source] (the publisher is an investor | https://www.centurium.com/press/%E7%91%9E%E5%B9%B8%E5%92%96%E5%95%A1%E6%9D%A8%E9%A3%9E%E | Ch.18, Method 4 |
| Watsons (Chinese: 屈臣氏)** (a full teardown in the Woshipm private-domain operations column) | [third-party reported: column teardown, relaying the company's figures] | https://www.woshipm.com/operate/5298724.html(200) | not used in the body |
| MINISO (Chinese: 名创优品)** (teardown in the Woshipm private-domain operations column) | [third-party reported: column teardown, relaying the company's figures] | https://www.woshipm.com/operate/5288035.html(200) | not used in the body |
| Perfect Diary (Chinese: 完美日记)** (Growth Box OSINT teardown, reprinted by CBNData) | [third-party reported: OSINT estimate, single source, used with caution] | https://www.cbndata.com/information/40929(200) | not used in the body |
| Soochow Securities Digital Intelligence Branch (Chinese: 东吴证券数智分公司)** (Securities Daily report, reprinted by Securities Times online) | [third-party reported: authoritative industry media] (Securities Daily, citing the company | https://www.stcn.com/article/detail/3588663.html(200) | not used in the body |
| Runwise post-mortem ｜ SMS win-back frequency experiment** (a Runwise innovation-community method post-mortem) | [third-party reported: method post-mortem] (Runwise's own media | https://runwise.co/digital-growth/growth-hacking/5455/(200) | not used in the body |
| Revolut** (2025 annual report + company press release published with it) | [official: company press release (published with the 2025 annual report)]* | https://www.revolut.com/en-US/news/revolut_reports_record_profit_of_2_3bn_for_2025_as_re | not used in the body |
| Airbnb** ｜ Referrals 2.0 rebuild (teardown by referral-marketing vendor Extole | [vendor claim: referral-marketing vendor relaying Airbnb's growth team | https://www.extole.com/blog/how-airbnbs-marketing-strategy-attracted-referrals-with-the- | Ch.23, Method 3 |
| Dropbox** ｜ two-sided referral reward (post-mortem on a sweepstakes/referral SaaS blog) | [vendor claim: referral SaaS blog, second-hand relay, single source] — | https://www.viraloo.org/blog/dropbox-referral-program-case-study-3900-growth(200) | not used in the body |
| Pinduoduo** (in-depth teardown by Jiemian News / Huanfan Caijing) | [third-party reported: authoritative media] (Jiemian News / Huanfan Caijing; " | https://www.jiemian.com/article/2317958.html(200) | Ch.19, Method 1 |
| MINISO** ｜ referral acquisition (coupon referrals + invite-a-friend-for-cash) | [third-party reported: column teardown, relaying the company's figures]** + note | https://www.woshipm.com/operate/5288035.html(200) | not used in the body |
| Three Youzan (Chinese: 有赞) customer-referral cases**: Huanglaowu Foods / Liangjiangren / Chunke CENO (Youzan New Retail Encyclopedia, blog | [vendor claim] (promotional material from customers of Youzan's own toolchain, not third-party | https://www.cnblogs.com/youzan/articles/19099271(200) | not used in the body |
| Starbucks Rewards | [third-party reported: loyalty SaaS compilation, relaying the company's disclos | https://www.rivo.io/blog/best-rewards-programs-dtc-brands(200) | not used in the body |
| Sephora Beauty Insider |  |  | not used in the body |
| N26 (Contrary Research report) | [third-party reported: research firm] | https://research.contrary.com/company/n26(200) | not used in the body |
| Groupon / LivingSocial** (Wharton professor Eric C | [third-party reported] (Wharton official publication, citing the professor | https://knowledge.wharton.upenn.edu/article/death-daily-deal/ | Ch.21, Method 3 |
| Casey Winters** (former head of growth at Pinterest / Grubhub | [third-party reported] (a signed article by a named practitioner) | https://www.caseyaccidental.com/p/when-growth-plateaus-how-and-when | not used in the body |
| Allbirds** (NASDAQ: BIRD, IPO 2021-11) | [official] (transaction amounts, recorded by the SEC) + [third-party reported |  | not used in the body |
| FTC "click-to-cancel" rule** (Click-to-Cancel, amending the 1973 N | [official] (FTC press release text) | https://www.ftc.gov/news-events/news/press-releases/2024/10/federal-trade-commission-ann | Ch.22, Method 2 |
| Meta (Meta Platforms Ireland)** cross-border data transfer case | [official] (DPC official press release text) | http://www.dataprotection.ie/en/news-media/press-releases/Data-Protection-Commission-ann | Ch.22, Method 3 |
| N26 / Germany's BaFin** growth cap and anti-money-laundering penalty | [third-party reported] (Banking Dive named repo | https://www.bankingdive.com/news/n26-bafin-growth-cap-aml-compliance-sar-stalf-tayenthal | not used in the body |
| Growth Engineering / Pragmatic Engineer × | [third-party reported] (in-depth interview with a named expert, author Gerg | https://newsletter.pragmaticengineer.com/p/what-is-growth-engineering | Ch.23, Method 3 |
| PostHog growth-engineer team | [vendor claim] (PostHog self-reported, and it is a product-analytics ven | https://posthog.com/blog/what-is-a-growth-engineer | not used in the body |
| Atlassian product growth engineer** (official blog) | [official] (Atlassian official blog; Atla | https://www.atlassian.com/blog/how-we-build/what-does-a-product-growth-engineer-work-on | Ch.23, Method 3 |
| Quibi** (Jeffrey Katzenberg + Meg Whitman) | [third-party reported] (Babson College official publication, with named | https://entrepreneurship.babson.edu/lessons-from-billion-dollar-failure/ | not used in the body |
| Dark Patterns** (ACM 'Communications o | [third-party reported] (peer-reviewed journal article; a textbook-level reference | https://cacm.acm.org/practice/dark-patterns/ | not used in the body |
| Robinhood / FINRA $26 million fine | [official] (FINRA press release text) | https://www.finra.org/media-center/newsreleases/2025/finra-orders-robinhood-financial-pa | not used in the body |
| Case/study (named) |  |  | not used in the body |
| Bain 'AI Is Transforming Productivity, but | [third-party reported] (Bain official research report) | https://www.bain.com/insights/ai-transforming-productivity-sales-remains-new-frontier-te | not used in the body |
| Salesforce 'State of Sales' 2026** (7th edition, 23 | [vendor claim] (Salesforce's own annual survey) | https://www.salesforce.com/news/stories/state-of-sales-report-announcement-2026/ | not used in the body |
| UC Berkeley 'California Management Review'* | [third-party reported] (academic journal Insights; of which | https://cmr.berkeley.edu/2025/02/balancing-personalized-marketing-and-data-privacy-in-th | Ch.22, Method 3 |
| Osano '2025 Marketing Data Privacy Compliance Guide' | [vendor claim] (practical guide from a privacy-compliance SaaS vendor) | https://www.osano.com/articles/marketing-data-privacy-guide | not used in the body |
