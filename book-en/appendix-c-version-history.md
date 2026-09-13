# Appendix C · Version History and Update Notes

This book is a "living book": continuous gathering → scheduled merging → version increments. This appendix records the substantive changes in each version; the detailed commit record is in the repository [CHANGELOG](https://github.com/Jweokk/ai-customer-acquisition-book/blob/main/CHANGELOG.md).

## v0.3.0 — 2026-09-13 (English edition)

- **First complete English edition**: 31 files under `book-en/` — preface, 4 part openers, 24 chapters, Appendix A (case index and both ledgers) and Appendix C — mapped one-to-one onto the Chinese edition.
- Translation rules live in `book-en/README.md`; terminology and source-tier mapping live in `assets/glossary-en.md`.
- `llms.txt` now pairs every chapter with both its Chinese site page and its English file on GitHub.
- The English PDF is published at the repository root as `ai-customer-acquisition-en.pdf` (GitHub distribution only).
- The Chinese content is unchanged in this release; the version number moves with it.

## v0.1.0 — 2026-09-13

**First edition (in progress).**

- Published the preface and the skeleton and first draft of the four parts and seventeen chapters;
- The book's proposition and boundaries: customer acquisition = earning the qualification to enter the buyer's decision process; the finish line is drawn at the first completed transaction / signed contract;
- Dual-track perspective: the Chinese ecosystem and overseas ecosystems written side by side;
- Four sourcing disciplines (trace to the original publisher, label the source tier, present differences in official figures side by side, delete what cannot be verified);
- **Added the book's own measurements**: the multi-model candidate-set measurement (6 questions × 5 model channels × 2 runs, 51 valid answers), concluding that a candidate set is a distribution rather than a list, that Chinese and English gateways return two candidate sets that barely intersect, and that the bare model layer carries no citations;
- Established Appendix A's tier ledger (source tier, data date, verifiability).

## v0.2.0 — 2026-09-13 (structure edition)

- **Established the book's main line**: buyers have changed where they pick vendors. Part 3 was reordered around the buyer's four steps (Find → Shortlist → Close → Bring the next one), and the second sentence of every chapter opening now returns to the main line; the preface carries the main line in one sentence, the reader-positioning table and that formula.
- **Chapter list changed to 24 chapters**: expanded from 17 chapters to 24 (adding eight chapters — advertising, in-platform acquisition, letting partners sell for you, the content factory and matrix distribution, product-led acquisition, AI answering customers around the clock, word-of-mouth referral and virality, and building the foundation first; the dark funnel merged into Chapter 1); chapter names changed to plain language you can grasp at a glance.
- **Numbering migration**: all chapter-number references, navigation and indexes synced to the 24-chapter numbering; appendices moved to the 90–93 prefix.
- **Writing style settled as the method format**: the tactic name is the subsection name, each method has four blocks (what to do / how / example / pitfalls to avoid), and each chapter ends with two items (Notes for this chapter, Sources for this chapter);
- **Sourcing discipline unchanged**: numbers that cannot be traced to the original publisher do not go into the body; effect multiples reported by vendors are marked only [vendor claim] and are not treated as budget assumptions.

## v0.2.1 — 2026-09-13 (case round)

- 16 methods that previously could only say "no publicly verifiable case available" were replaced with named, verifiable cases; every case URL was tested one by one and confirmed reachable, and the verifiable original sentence is kept in the sources;
- Added A.8, the case pool, registering the cases gathered this round but not written into the body, for reference;
- Vendor-reported effect figures are still marked only [vendor claim] / [vendor self-reported], and are not treated as fact.

## v0.2.2 — 2026-09-13 (sourcing and title round)

- Subtitle changed to "Buyers are asking AI — are you in the answer?"; the part opener subsection renamed "Chapters in This Part";
- The self-test channels no longer write specific model vendors and version numbers, and instead use capability tiers A–E (reasoning / general-purpose / lightweight / open-weight / spot-check), with the raw data and scripts anonymized accordingly.

## v0.2.3 — 2026-09-13

- Subtitle fixed as "Use AI to Acquire Customers: Find, Shortlist, Close, Bring the Next One";
- Added Appendix E · References for the Whole Book: all the book's sources merged and de-duplicated into 299 entries, uniformly numbered with the citing chapters listed against each one; the body carries no numeric superscripts (the tier stays at the end of the sentence), and the end-of-chapter lists are kept.

## v0.2.5 — 2026-09-13

- One round of salvaging from the earlier growth-hacking material library: 90 candidates, 24 written into the body (Chapters 10, 11, 12, 13, 16, 18, 19, 20, 21, 22, 23), with a new A.9 ledger; Appendix E updated to 314 entries.

## Version Plan

- v0.2.x: chapter-by-chapter consolidation (unified terminology, sources merged into Appendix A and numbered, every chapter's unverified items brought to zero or deleted);
- v0.3.x: complete the in-house measurements for Chapter 8 and Chapter 20; add concrete cases to the industry difference matrix;
- v1.0.0: whole-book consolidation complete, Appendices A–D complete, PDF finalized.

## How Updates Work

New content is merged into existing chapters in the normal chapter structure, so readers cannot see "which paragraph was added in which version"; version notes appear only in this appendix and the CHANGELOG. The body carries no version markers.
