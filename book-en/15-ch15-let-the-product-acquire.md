# Chapter 15 Let the Product Acquire: Free Tools, Trials, and Open Interfaces

Winning a customer used to start with a person moving first: sales made calls, the media buyer bought ads, the writer published content, and the customer was pushed along. Now a share of customers find you themselves — they first run their own numbers through your calculator, or finish one real piece of work inside a trial, and only once it works smoothly do they turn around and ask "which company are you?" Customers like this open with a specific question; nobody exchanges pleasantries and nobody sits through your company introduction from the top.

The customer may have used your thing before ever knowing your company. That is why this chapter gives you 5 methods that bring in leads without a person making a move.

---

## Method 1: Build a small tool so people use it first and leave contact details after

**What to do**: Turn the one question you are asked most often into a free small tool, so the customer gets the result first and you talk about leaving contact details only after that.

**How**

1. From sales and customer-service chat logs, pick the question that is **asked most often and has the most standardized answer** — a quote estimate, a unit conversion, a quota calculation, a compliance check — and choose one. Many people asking means many people searching, so this tool's entry point is naturally open.
2. The tool does one thing only: three or four inputs in, one number or one checklist out. The fewer inputs the better; every extra one drops a cohort of people [our judgment]. Default whatever can be defaulted, and anything the customer can pick from options should not be left for him to type.
3. Fix the order: enter inputs → see the result → want to save the result or see the next layer → only here does the contact-capture box appear. The step of asking for contact details comes **after** the result, not before it.
4. Give an output that can be taken away: a PDF, an image, a conclusion that can be copied. The people willing to save it are the ones genuinely interested.
5. Look at only two numbers each month: how many people used it, and of those who finished, how many left contact details. The second number is this hook's actual score; if the first looks good and the second does not move, the problem is on the results screen.
6. Put the tool on a separate domain or a separate path, not inside a pop-up on your homepage. Its job is to be found by search and shared by people, and a pop-up can do neither [our judgment].

**Example**: HubSpot's Website Grader says officially that it has scored more than 2 million URLs [official]; Ahrefs has turned free tools into a full-page matrix [official]; Shopify's free name generator page says outright, No Sign-Up Required, and only guides you to a trial after you have used it [official].

**Pitfalls**: Turning the tool into a shrunken product-brochure page where the input fields exist only to collect information — the customer fills in half of it, finds there is no result to see, and leaves.

## Method 2: Open up the interface so machines can call your capability

**What to do**: Package your core capability as an interface on an open standard so someone else's AI can call it directly, and the caller becomes one of your lead sources.

**How**

1. Work out, on an open standard, what your capability should be exposed as. Taking MCP as the example, the specification splits the roles into Hosts (the AI application that initiates the connection), Clients (the connector inside the host application), and Servers (the service that provides context and capabilities), and a server offers three kinds of things outward: Resources (data and context), Prompts (templated messages and workflows), and Tools (executable functions) [official]. The question you have to answer is "which tool function my capability is packaged as, how the parameters are filled in, what it returns," not "how my web page is laid out."
2. Write the interface documentation to the standard of "written for a machine": the capability name, the meaning and value range of each parameter, the fields returned, and the message on error. The caller's AI decides whether to use you from this documentation; a usage the documentation does not describe is one it will not guess at.
3. Connecting once is enough. The documentation compares this kind of protocol to the USB-C port of AI applications — connect once and multiple clients can use it [official]. So pick the mainstream standard; do not set up one of your own.
4. Open the read-only part first. Query, calculation, and comparison capabilities that do not touch the other party's data have a low authorization bar and get connected first; write capabilities come later, since the customer side also needs a bit more time before daring to grant you permission.
5. Leave a recognizable identity in the service name and in the returned values. When you are called you do not know who is on the other side, but the other side's people and the later invoice need to be able to recognize you.
6. Keep the version number in the interface address and give old versions a transition period. Change an interface once and everyone already connected breaks outright, and you will receive no complaints at all — they simply stop calling.

**Example**: The current version of the MCP specification is 2026-07-28; the specification defines the protocol as an open standard between AI applications and external data sources and tools, with messages carried over JSON-RPC, and the three kinds of capability a server exposes are data, prompt templates, and tool functions [official]. The getting-started documentation compares it to "the USB-C interface of AI applications" and lists the clients that already support it — Claude, ChatGPT, Visual Studio Code, Cursor, and others — so you write it once and can connect in many places [official].

**Pitfalls**: Reading "opening an interface" as "putting up an API document." A document left sitting there is read by nobody; it only counts once it can actually be called.

## Method 3: Publish the service into official directories so agents find you on their own

**What to do**: Publish the service into official registries and platform app directories, so the buyer's agent and the platforms pull you up when they choose vendors.

**How**

1. Keep the two kinds of directory apart. One is a **protocol-level registry** (such as MCP's official registry), where what gets published is metadata, so that clients and aggregators can discover which services are available; the other is a **platform app directory** (the app marketplaces of payment platforms and collaboration platforms), which catalogs individual app entries, and that is where customers go to choose. Get into both; they do different jobs.
2. Prepare the metadata the publication requires: the service's unique name, its install location (package name or remote address), start-up and configuration instructions (command-line arguments, environment variables), and a capability description. These are the fields you cannot get around at registration; miss one and you cannot publish.
3. Take a name in reverse-domain-name form, and be able to prove that the namespace is yours — verify ownership with your domain or your code-hosting account. The review clears only when the name and the ownership match; if they do not, you are holding a place for someone else.
4. The bar for publication is usually "the install method is publicly installable" or "the service itself is publicly reachable." Private services open only to the inside are generally outside the scope of what gets cataloged.
5. Do not stop once you have published: **the downstream aggregators and marketplaces are where customers actually look.** A registry gives unsorted metadata; a marketplace adds ratings and recommendations on top, so the material has to be filled in one mainstream marketplace at a time.
6. Write the blurb in the directory entry in the words a customer would actually type, not your internal phrasing. How well this paragraph is written directly decides whether you show up in that search.

**Example**: MCP's official registry is that central directory: publicly reachable services can publish their metadata into it, and clients and aggregators discover which services are available through its interface [official]. Stripe's Directory documentation is the most direct: it lets developers and AI agents find the external service provider best suited to a given task, and what it indexes includes apps listed in app marketplaces, providers that can be switched on with a single command, and a directory of interfaces that support pay-per-call, with search results carrying structured fields such as the provider's identity and interface address [official]; the documentation also gives the way to write — use in the blurb the words a customer would actually type, so "help freelancers invoice and get paid faster" is more findable than "next-generation financial operations platform"; use complete phrases rather than pulling the words apart and scattering them; and the display name and account name must match what customers call you, or someone searching your name directly will not find you either [official].

**Pitfalls**: Assuming that having your name listed in a registry equals leads. A directory gives you one chance to be found; whether you are chosen depends on the description in the entry and the reputation outside the directory [our judgment].

## Method 4: Write the boundaries of the trial and the free tier in stone

**What to do**: How far free goes, when charging starts, and how the allowance is calculated all get fixed in advance, so the trial period does the filtering itself.

**How**

1. Give free on one dimension only: either time or count. Give both and the customer cannot work out how much is left, and starts using it timidly.
2. Write out "what happens when you run out" before the first use: how much allowance remains, whether running out stops the service or auto-charges, and how much it charges. What customers fear most is receiving an unexpected bill as the trial nears its end, and that kind of dispute is more expensive than no conversion [our judgment].
3. Get the customer to accomplish one real thing inside the trial rather than clicking through every feature. The test is "has he run his own data through it once" — clear that step and paying becomes possible; not before.
4. Follow up on two separate tracks. Those who used it but did not hit the allowance and those who ran out and stopped need entirely different messages: the first lack a reason to use it, the second lack a budget.
5. During the trial, log the nodes — activation, drop-off, hitting the allowance — and see which screen people stick on. When you are adjusting the product, the sticking points are more useful than a vague conversion rate.
6. Converge the free-tier terms and the discount policy into one place. If the same company presents two sets of trial rules, customers will screenshot them and compare, and sales cannot explain which one actually applies.

**Example**: On 2022-11-28 Heroku took down free dynos, free Postgres, and the free Key-Value Store all at once [official]; Railway first shut down its free plan to stop the bleeding, then reopened it in the form of 5 USD / 30 days + 1 USD / month [vendor claim].

**Pitfalls**: Setting the free allowance to "just short of finishing one thing." After the trial the customer remembers exactly one thing — you cannot get anything done there.

## Method 5: Turn the tool's result page into a lead-capture page

**What to do**: Let the result the tool calculates go find the next customer on its own, and catch the new visitor along the way.

**How**

1. The result page gives three things: the conclusion, the basis, and the next step. The basis is "how this number was calculated," and tools that can explain the algorithm and the parameter ranges clearly get shared the most [our judgment].
2. Make the result takeable: a conclusion that can be copied, an image, a PDF. When the customer takes it away, his own inputs go with it, and your name goes with it too.
3. Make the result pages findable by search and readable by AI. Generate a static page for each common input combination, with the title being the question the customer would search and the body laying out the input conditions and the calculated conclusion. When someone searches the same conditions, what they find is your page, not someone else's tool.
4. Leave an entry point on the sharing path: whoever receives the image or the link can open it and run the calculation again with their own conditions. The person who calculates a second time is the new lead you just won.
5. Leave one spot at the bottom of each result page for "see the detailed version," and ask for contact details only there, once — do not reach out from every corner of the page.
6. Do not put a pile of navigation on the results page. The customer arrived with one specific question; this page answers only that question and leaves one exit.

**Example**: Shopify's free name generator strings "generate a result — pick a domain — start a trial" into a single path, so the results page is itself the lead-capture page [official]; HubSpot's results page gives a score plus item-by-item advice plus a competitor comparison, then guides to the next step [official].

**Pitfalls**: A results page with nothing but a line saying "congratulations on completing the assessment" and a QR code. If the customer gets nothing he can take away, the page was made for nothing.

---

## Notes for this chapter

- This chapter **cites no conversion percentages for trials or free tools**. Every such number that could be found in the materials (free-trial-to-paid rates and the like) came from aggregation blogs with no original source, so none is used, which is why methods 1, 4, and 5 give the how and not the result. To find out whether it works, keep your own books the way Chapter 20 does.
- The open-capability directories of domestic platforms (WeChat Mini Programs (Chinese: 微信小程序), the Feishu app marketplace (Chinese: 飞书应用市场), the DingTalk open platform (Chinese: 钉钉开放平台), the Coze store (Chinese: 扣子商店)) were not captured this round, and neither was Build with the Apps SDK in OpenAI's help center (curl returned 403). So the practice in method 3 follows the public documentation of MCP and Stripe; moving to another platform means walking through its own listing rules again.
- There is currently no authoritative standard for designing a tool hook. Methods 1 and 5 are written as workable practice, not as the standard answer.
- Methods 2 and 3 cite official documentation and describe **mechanisms**, not promised results. They say how something gets called and how something gets listed; they do not say how many leads doing it will bring.
- Think through the authorization boundary before opening your capability up. The MCP specification writes user consent, data access control, and authorization before tool invocation as principles the implementer must handle, not as options [official] — opening an interface carries a compliance cost.

## Sources for this chapter

[1] Model Context Protocol | Specification (2026-07-28 version) | https://modelcontextprotocol.io/specification/2026-07-28 | [official]
[2] Model Context Protocol | Official registry documentation | https://registry.modelcontextprotocol.io/docs | [official]
[3] Model Context Protocol | Getting-started documentation | https://modelcontextprotocol.io/docs/2026-07-28/getting-started/intro | [official]
[4] Stripe | Directory documentation | https://docs.stripe.com/directory | [official]
[5] HubSpot | Website Grader has scored 2 million+ URLs | https://www.hubspot.com/blog/bid/5539/website-grader-analyzes-over-2-million-websites | [official]
[6] Ahrefs | Free SEO Tools (free-tool matrix) | https://ahrefs.com/free-seo-tools | [official]
[7] Heroku | Removal of Heroku Free Product Plans (effective 2022-11-28) | https://help.heroku.com/RSBRUH58/removal-of-heroku-free-product-plans-faq | [official]
[8] Shopify | Free Business Name Generator (results page to trial) | https://www.shopify.com/tools/business-name-generator | [official]
