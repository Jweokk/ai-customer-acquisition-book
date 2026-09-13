# Chapter 22 Build the Foundation: First-Party Data, Compliance, and Omnichannel Orchestration

Every move in the previous two parts happens where the customer can see it — in the AI's answers, in the platform's feed, in the message you sent; the subject of this chapter never shows up on the customer's side at all.

This step does not happen on the customer's side, but it decides whether everything you did before can be logged, reviewed, and continued. So this chapter gives you 5 methods to lay the foundation first.

---

## Method 1: Get the customer list back into your own hands

**What to do**: Collect the customer contact details scattered across platform back-ends, sales reps' phones, Excel, and chat logs into one list you can export, contact, and delete person by person.

**How**

1. Settle on four fields first, and do not add a fifth: one reachable identifier (phone number or email), source (which entry point it came from), consent status (when and how it was obtained), and the time of the last touch.
2. Round up all the entry points: website forms, official accounts and WeCom, stores and trade shows, customer-service conversations, trial sign-ups, and closed customers. Assign one person per entry point to enter records as they come in; don't count on catching up at month-end.
3. Consent status must be tied to the individual and must be deletable person by person. Quarantine the segment whose source you cannot explain; it takes part in no marketing action.
4. Clean the list once a quarter: move those who withdrew consent or clearly said they do not accept marketing from the reachable zone to a quarantine zone, keeping one record for the audit trail.
5. Keep it in a system you can export from. A list stuck in a platform account back-end that you cannot export stops being yours the moment the platform changes a rule.

**Example**: The vendor's definition of a CDP (customer data platform) is this: integrate customer data from multiple sources into a unified customer profile, with specific capabilities that include identity resolution — matching and merging records of the same customer across devices and channels — and data activation — sending customer data to systems such as email platforms and ad networks [vendor claim]. Treat this passage only as a definitional reference for “how far you need to consolidate”. It promises no results, and it is not product-selection advice.

**Pitfalls**: Mixing bought or scraped lists into your own. The batch whose source you cannot explain can take down the credibility of the whole list with a single complaint or a single leak — and it never had the consent you claim for it in the first place.

## Method 2: Build “notice, consent, refusal” into the moment of collection

**What to do**: Let customers see how you will use their information before they leave contact details, and let them ask you to stop marketing to them after they do.

**How**

1. Give notice at the moment of collection, covering four things: the name and contact details of the processor; the purpose and method of processing, the types of information, and the retention period; the ways and procedures by which the individual can exercise their rights; and any other matters the law requires you to disclose. State them in a prominent way, in clear and easy-to-understand language, truthfully, accurately, and completely [official]. If these matters change later, tell the individual about the parts that changed.
2. Consent must be voluntary and explicit, and you may not trade it for access — except where the personal information is necessary to provide the product or service [official]. In practice it comes down to one line: make “I agree to receive marketing messages” a separate checkbox, and let the product work normally when it is left unchecked.
3. Provide two ways out: one for withdrawing consent, one for refusing personalized pushes and marketing. The provision on automated decision-making reads, verbatim, that you should also provide an option not targeting the individual's personal characteristics, or provide the individual with a convenient way to refuse [official].
4. Before giving personal information to another processor (a push platform, an ad platform, a data service provider), first disclose the recipient's name, contact details, processing purpose, processing method, and the types of personal information, and obtain separate consent [official].
5. Correction, deletion, and account closure must each have an entry point a user can actually click. These three were named one by one in the four-ministry special campaign of 2025: failing to provide effective functions for correcting and deleting personal information and closing accounts, and providing personalized information pushes without offering a convenient way to refuse [official].

**Example**: The U.S. FTC's “click-to-cancel” rule turned that sentence into a hard requirement — unsubscribing must be as easy as subscribing; the rulemaking drew more than 16,000 public comments, while consumer complaints rose from an average of 42 a day in 2021 to 70 in 2024 [official]. Consent and refusal must cost the same.

**Pitfalls**: Turning “consent” into a checkbox nobody has read, then interpreting it internally as a marketing authorization covering every channel. Consent is per-purpose — marketing, handing information to others, and using it abroad each stand on their own, and each must be withdrawable.

## Method 3: Do the threshold math before data leaves the country

**What to do**: Before customer data flows abroad (an overseas marketing cloud, an overseas ad platform, an overseas customer-service system, reports read by an overseas subsidiary), work out whether you need to file for a security assessment.

**How**

1. First list every segment where data leaves: overseas CRM and marketing clouds, overseas email and ad platforms, overseas customer-service ticketing systems, and reports read by overseas teams or agents.
2. Filing is required in four situations — providing important data abroad; operators of critical information infrastructure and processors of personal information on more than 1 million people providing personal information abroad; providing personal information on 100,000 people or sensitive personal information on 10,000 people abroad on a cumulative basis since January 1 of the previous year; and other situations requiring filing as prescribed by the national cyberspace administration [official].
3. Carry out a self-assessment of risk before filing: assess the legality, legitimacy, and necessity of the purpose, scope, and method of the outbound transfer; the scale, scope, types, and sensitivity of the data transferred; the protection capacity of the overseas recipient; and whether the contract you plan to sign spells out the security responsibilities in full [official].
4. Build the timing into your schedule: the assessment is completed within 45 working days of acceptance, extendable when the case is complex or supplementary materials are needed; a passed assessment is valid for 2 years, and if you still need to transfer data abroad when it expires, file again 60 working days before expiry [official].
5. The legal documents must spell out at least six things: the purpose, method, and data scope of the outbound transfer, and the use and method of the overseas recipient; the overseas storage location, the retention period, and the measures for handling the data after the period ends; the binding requirements for further transfers to other organizations or individuals; the security measures to be taken when actual control or the local legal environment changes; remedies for breach, liability for breach, and the dispute-resolution method; and the requirements for emergency handling and the channels for protecting rights when data is tampered with, leaked, or illegally obtained [official].

**Example**: The most expensive lesson on the cross-border line comes with a price tag: the Irish Data Protection Commission fined Meta €1.2 billion for continuing to transfer EU user data back to the United States, finding it in breach of Article 46(1) of the GDPR [official].

**Pitfalls**: Assuming that “we use overseas SaaS, so it counts as a transfer abroad”. Look at where the data actually lands, not where the vendor is registered or which party signed the contract [our judgment]. And treating the types and scale of personal information as a vague impression ends with the filing threshold miscalculated.

## Method 4: Label AI-generated content before you publish it

**What to do**: For text, images, audio, video, and virtual scenes generated or synthesized with AI, declare identity as required at every link of publishing and distribution, and make sure the label is still there after the file is exported.

**How**

1. First tell the two kinds of label apart: an explicit label is added to generated or synthesized content or to the interaction interface and is clearly perceivable by users, in the form of text, sound, or graphics; an implicit label is written into the file data by technical means and is not easily perceived by users [official].
2. Apply it per medium: for images, add a prominent notice in an appropriate position; for video, add it in the opening frames and around the playback area, and it may also be added at the end and in the middle; for virtual scenes, add it in the opening frames; for text, add a text or symbol notice in an appropriate position at the start, end, or middle, or add a prominent notice in the interface or around the text [official].
3. Write the implicit label into the file metadata, covering at least the attribute information of the generated or synthesized content, the service provider's name or code, the content number, and other production element information [official].
4. Where download, copy, or export functions exist, make sure the file contains an explicit label that meets the requirements — a label that only sits in the back-end and drops off on export does not count as done [official].
5. If you distribute through an app store, the labeling materials will be checked at listing or launch review; when publishing generated or synthesized content, declare it proactively and use the labeling function the platform provides; no organization or individual may maliciously delete, tamper with, forge, or conceal these labels [official].
6. Remember the date: the measures took effect on September 1, 2025 [official].

**Example**: Article 9 of the Measures for Labeling AI-Generated and Synthesized Content gives teams making ad creative the most practical reading: when a user requests generated or synthesized content without an explicit label, the service provider may supply it after making the user's labeling obligations and usage responsibilities clear through the user agreement, and must keep logs of the recipient and related information for no less than six months in accordance with the law [official]. The moment you get “clean” material, the labeling obligation and usage responsibility shift to your side — and the logs still have to be kept.

**Pitfalls**: Assuming only face-swaps and digital humans need labeling. The scope is “text, images, audio, video, and virtual scenes generated or synthesized using AI technology” [official] — mass-generated product images, AI-voiced talking-head videos, and AI-written scripts and copy all fall inside it.

## Method 5: Link your touchpoints into a chain that reports back

**What to do**: Connect “which channel a list segment is pushed to, what that channel brings, and how the result is read back” into a single line, one line one set of definitions, reviewed channel by channel.

**How**

1. One push line per channel: cut a segment from the list, push it to that channel, and give the line its own name so it does not blend into organic traffic.
2. Fix the report-back fields, these six and no more: spend, impressions, cost per thousand impressions, clicks, click-through rate, and cost per click [official]. Read only these for every line; do not swap definitions on the fly.
3. When the same group is pushed to two channels, look at the two sides separately. Different channels have different cost structures, and blending them into one average will wrongly convict one and wrongly acquit the other at the same time.
4. The read-back must land on “the group you pushed out”. The vendor's own documentation locks the definition down: it analyzes only the advertising and marketing performance of ads served to the audience pushed from its own platform to that ad platform [official]. Your table must lock down the same limitation.
5. Reconcile the six fields with closed deals in the CRM once a quarter. If the channel report claims conversions and you cannot find the corresponding people in the CRM, fix the definitions first, then talk about adding budget.
6. Omnichannel orchestration has no authoritative official definition; just follow the practice [our judgment]. The deliverable you hand in is one table: channel × pushed list × six fields × quarterly trend.

**Example**: Alibaba Cloud's (Chinese: 阿里云) help documentation gives a very concrete path: an audience-push task pushes an audience to Ocean Engine (Chinese: 巨量引擎), then on the performance analysis page you select the time range, the Ocean Engine account, the ad audience, and the ad order to look back at spend, impressions, cost per thousand impressions, clicks, click-through rate, and cost per click, and the bottom of the page lists key metrics order by order [official]. The same document limits it: it analyzes only ads served to the audience pushed from it to that platform [official].

**Pitfalls**: Pushing without reading back — or reading back only against your own last week. Without a control, you cannot tell whether the list did the work or the channel would have produced volume anyway.

---

When the foundation is weak, every method above gets discounted. If the list cannot be gathered, the results of all your visibility, content, and outreach work never settle; if consent status is unclear, leads coming back from channels to the CRM dare not be touched again; if the outbound threshold is uncalculated, the overseas set of moves can be halted at any time; if labels are missing, shipping creative is accumulating risk; if read-back definitions are not unified, not one set of books will hold. None of these five things happen on the customer's side; they do one thing only — let what you did before be logged, reviewed, and continued.

## Notes for this chapter

- This chapter describes the “notice–consent” requirement itself and gives no article numbers. Using customer data “for marketing” is not something a single clause of the Personal Information Protection Law covers; it is assembled from the requirements on notice, consent, separate consent, and convenient refusal, and pinning one article number on it would compress several provisions into one. If you need an article number, go back to the original text, check it clause by clause, and only then cite it.
- For automated decision-making, this chapter quotes the original wording — where it is used for information pushes and commercial marketing, an option not targeting the individual's personal characteristics should also be provided, or the individual should be given a convenient way to refuse; the original text also states that unreasonable differential treatment of individuals in transaction prices and other transaction terms is prohibited [official]. This chapter does not interpret the enforcement intensity of this provision, nor does it expand on the definitions for algorithm filing and algorithm recommendation management.
- “Omnichannel orchestration” has no authoritative official definition. It is neither a legal concept nor was a unified definition ever given by a regulator or standards body. This chapter writes it as a practice — cut a list segment and push it out, report back six fields, review channel by channel, reconcile with the CRM once a quarter — naming no products and not presenting it as an industry standard [our judgment].
- The first-party data section cites Microsoft's definition of a CDP; that is a vendor's reading, to be used only as a definitional reference for “how far you need to consolidate”, not as a product capability or a promise of results [vendor claim]. The Alibaba Cloud document cited in Method 5 is an operational definition that explains how the fields are read; it is likewise not a promise of results [official].
- The numbers in the outbound threshold (1 million people, 100,000 people, 10,000 people, 45 working days, 2 years, 60 working days) all come from the original text of the Measures for the Security Assessment of Data Cross-Border Transfer, which took effect on September 1, 2022 [official]. Before actually filing, go by the currently effective text and the reading of the cyberspace administration authority where you are located.

## Sources for this chapter

[1] Personal Information Protection Law of the People's Republic of China (adopted August 20, 2021; effective November 1, 2021) | full text on the Cyberspace Administration of China website | https://www.cac.gov.cn/2021-08/20/c_1631050028355286.htm | [official]
[2] Cyberspace Administration of China Order No. 11, Measures for the Security Assessment of Data Cross-Border Transfer (effective September 1, 2022) | full text on the Cyberspace Administration of China website | https://www.cac.gov.cn/2022-07/07/c_1658811536396503.htm | [official]
[3] Measures for Labeling AI-Generated and Synthesized Content (issued March 7, 2025; effective September 1, 2025) | full text on the Cyberspace Administration of China website | https://www.cac.gov.cn/2025-03/14/c_1743654684782215.htm | [official]
[4] Office of the Central Cyberspace Affairs Commission, Ministry of Industry and Information Technology, Ministry of Public Security, State Administration for Market Regulation | Announcement on Carrying Out the 2025 Special Campaign on Personal Information Protection (March 28, 2025) | full text on the Cyberspace Administration of China website | https://www.cac.gov.cn/2025-03/28/c_1744867353112759.htm | [official]
[5] Alibaba Cloud | Ocean Engine performance analysis (the fields and limiting definition for reading back results after a Quick Audience audience push) | https://help.aliyun.com/zh/document_detail/170392.html | [official]
[6] Microsoft | What is a CDP? (the customer data platform definition, identity resolution, and data activation capabilities) | https://www.microsoft.com/zh-cn/dynamics-365/resources/what-is-a-cdp | [vendor claim]
[7] U.S. FTC | Final Click-to-Cancel Rule (unsubscribing must be as easy as subscribing; 16,000+ public comments) | 2024-10 | https://www.ftc.gov/news-events/news/press-releases/2024/10/federal-trade-commission-announces-final-click-cancel-rule-making-it-easier-consumers-end-recurring | [official]
[8] Irish Data Protection Commission (DPC) | decision against Meta Ireland: €1.2 billion (breach of Article 46(1) of the GDPR) | http://www.dataprotection.ie/en/news-media/press-releases/Data-Protection-Commission-announces-conclusion-of-inquiry-into-Meta-Ireland | [official]
