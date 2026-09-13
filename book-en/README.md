# English edition — file map and rules

This directory holds the English edition of 《AI 获客》 (AI Customer Acquisition). The Chinese edition under `book/` is the source of truth; every update lands here too, in the same commit.

## File map (Chinese → English)

| Chinese (`book/`) | English (`book-en/`) |
|---|---|
| `00-序-客户找供应商的方式变了.md` | `00-preface-how-buyers-find-vendors.md` |
| `00z-篇一-先看清战场.md` | `part1-see-the-battlefield.md` |
| `01z-篇二-AI时代的新方法.md` | `part2-new-methods-for-the-ai-era.md` |
| `08z-篇三-用AI改造老办法.md` | `part3-upgrading-the-old-methods.md` |
| `19z-篇四-别白花钱别把地基打歪.md` | `part4-dont-waste-money-or-build-on-sand.md` |
| `01-第1章-先看清战场.md` | `01-ch1-see-the-battlefield.md` |
| `02-第2章-让AI在回答里提到你.md` | `02-ch2-get-mentioned-in-ai-answers.md` |
| `03-第3章-挤进客户的第一份名单.md` | `03-ch3-get-onto-the-first-shortlist.md` |
| `04-第4章-让第三方替你说话.md` | `04-ch4-let-third-parties-speak-for-you.md` |
| `05-第5章-先讲自己的坑.md` | `05-ch5-lead-with-your-own-pitfalls.md` |
| `06-第6章-让机器读懂你.md` | `06-ch6-be-readable-by-machines.md` |
| `07-第7章-让买家的AI代理选中你.md` | `07-ch7-win-the-buyers-ai-agent.md` |
| `08-第8章-中文市场要多做三件事.md` | `08-ch8-three-extra-moves-for-chinese-markets.md` |
| `09-第9章-投广告.md` | `09-ch9-advertising-from-audiences-to-targets.md` |
| `10-第10章-在别人的平台上获客.md` | `10-ch10-acquire-on-other-peoples-platforms.md` |
| `11-第11章-让别人替你卖.md` | `11-ch11-let-partners-sell-for-you.md` |
| `12-第12章-把一次内容拆成三十条.md` | `12-ch12-turn-one-piece-into-thirty.md` |
| `13-第13章-外联-从发得多到发得准.md` | `13-ch13-outreach-from-volume-to-precision.md` |
| `14-第14章-做出别人抄不走的内容.md` | `14-ch14-content-others-cannot-copy.md` |
| `15-第15章-让产品自己拉客.md` | `15-ch15-let-the-product-acquire.md` |
| `16-第16章-让AI24小时替你接客户.md` | `16-ch16-let-ai-answer-around-the-clock.md` |
| `17-第17章-用AI找客户管线索跑销售.md` | `17-ch17-find-qualify-and-run-the-sale.md` |
| `18-第18章-电话和私域.md` | `18-ch18-phone-and-private-domains.md` |
| `19-第19章-让客户替你带客户.md` | `19-ch19-let-customers-bring-customers.md` |
| `20-第20章-怎么知道有没有用.md` | `20-ch20-how-to-know-its-working.md` |
| `21-第21章-别把命押在一个入口.md` | `21-ch21-dont-bet-on-one-gateway.md` |
| `22-第22章-先打地基.md` | `22-ch22-build-the-foundation.md` |
| `23-第23章-谁来干花多少钱.md` | `23-ch23-who-does-it-and-what-it-costs.md` |
| `24-第24章-别踩这些线-六份失败档案.md` | `24-ch24-red-lines-six-failure-files.md` |
| `90-附录A-案例索引与资料出处.md` | `appendix-a-case-index-and-sources.md` |
| `92-附录C-版本历史与更新说明.md` | `appendix-c-version-history.md` |

## Rules for the English edition

1. **Same structure as the Chinese.** A chapter keeps its opening two sentences, its numbered methods in the same order, and the same four blocks per method: **What to do / How / Example / Pitfalls**.
2. **Numbers, dates, URLs and company names are copied verbatim.** Never round, never re-source, never re-derive. A number that cannot be traced in the Chinese edition does not appear here either.
3. **Source tiers are carried over 1:1**, using the mapping in [`assets/glossary-en.md`](../assets/glossary-en.md) (`【官方口径】` → `[official]`, and so on). A chapter keeps its own source list at the end, with the same URLs.
4. **No `fly2ai.top` links anywhere in the English edition.** Reading/download links point at GitHub only.
5. **A Chinese company's first mention reads `English name (Chinese: 中文名)`** on first occurrence.
6. **The body stays clean**: no version markers, no "added in vX", no process words (word counts, gathering plans). Version history lives in `appendix-c-version-history.md` and the repository `CHANGELOG.md`.
7. **No numeric superscripts in the body** (same convention as the Chinese edition — the tier rides at the end of the sentence).
