# Q-014 memo: what organisations that scan outside practice found when judging, approving, declining, retiring and stopping (2026-11-08)

*The Researcher's memo for Q-014, round 4, the focused confirmation round the owner ruled (decisions/questions/P-002-research-stop.md; brief 186, docs/briefs/186-researcher.md), revised after the Source checker's round 3 (research/Q-014-source-check.md); rounds 1 to 3 (briefs 162, 170, 178) are in this file's history. Recorded verbatim by the Orchestrator (session_01QBwHGNSLmSrYQgS6BPjV8p), 2026-11-09, from the helper's return; only this italic line is the Orchestrator's. The helper's return opened with a note to the Orchestrator before the memo, which is not recorded here; its three points are answered in the source-check brief (docs/briefs/188-source-checker.md).*

*Researcher, 2026-11-09, revised after source-check rounds 1, 2 and 3 (focused confirmation round). Sources: the Input reader's findings (research/Q-014-input.md), which are untrusted, the Source checker's round 1 to 3 findings (research/Q-014-source-check.md), and the portfolio library. I did not use the web, and model memory is not used as a source. In the summary parts, every sentence names the finding ids (F014-n) or library entries it rests on; sentences with no recorded finding behind them are marked as my opinion.*

The evidence does not show whether scanning and adopting outside practice brings benefit, no benefit or harm. No source compares organisations that scan with ones that do not (Input reader's gap statement; §1). What the evidence does record, across process safety, health technology assessment, standards bodies and software, is a few problems. Each comes from one case, one study, or attributed opinion:

- **Retiring may be harder than adopting. This is my opinion, drawn from scattered cases; no source compares the two directly.**
  - One RFC records that the IETF's procedure for reviewing immature standards "has never been followed" (F014-24).
  - In medicine, the authors of one paper assert that an established ineffective practice is hard to get practitioners to abandon. This is their assertion, not a measured rate (library Q-009-F13-3).
  - "Do not do" reminders showed no association with practice change in one study included in a scoping review (F014-17).
  - Of 7 low-value services flagged by the Choosing Wisely campaign, 2 declined slightly, 3 stayed flat and 2 rose (F014-18; insurer data).
  - An NIHR researcher argues that a "do not recommend" ruling needs more certainty than leaving a treatment to clinical discretion (F014-16, opinion).
- **In one scheme, re-appraisal after provisional funding almost always ended in a recommendation.**
  - Under the reformed Cancer Drugs Fund, 19 of 20 technologies were recommended at exit. The abstract excludes one terminated evaluation.
  - 12 of the 20 exit evaluations (60%) did not fully resolve the original uncertainty (F014-12; one consultancy conference abstract).
  - This is one scheme. Whether it holds elsewhere is untested.
- **Missing change processes show up in inspection citations and incident reports. That a heavy process invites bypassing is a stated concern, not a finding.**
  - In OSHA's refinery inspections (2007–2011), 39 of 92 MOC citations (42%) were for having no MOC system established or in use (F014-4; secondary figures, consultancy author).
  - In the EU's eMARS database, 4 of 891 reports were explicitly MOC-related, and all four showed no MOC used. The author calls the data's quality very poor (F014-5).
  - These are citations and reports, not a count of change failures.
  - In one study's typology of MOC failures, temporary changes were 10.1% and requested (planned) changes the largest share, 45.6% (F014-2, F014-3).
  - One consultancy author states a concern that MOC systems seen as overly bureaucratic may be bypassed (F014-6). A process-safety writer argues that shortcuts follow when MOC takes longer than the change (F014-8, opinion). Neither gives a measured rate.
- **In the one software case recorded, a radar with no formal process faded.**
  - Zalando reports that its first radar was "easy to ignore due to lack of a formal process" and relied on volunteer contributions that fell off (F014-26; self-report).
  - This is one case.

Some fixes are described. No finding measures the outcome of any of them:
- time limits and formal close-out for temporary changes, and routine review of all open changes (recommendations from two named audits, F014-7);
- scheduled review by member vote (ISO, F014-22), and loss of status if a standard is not revised or reaffirmed within 10 years (ANSI, as summarised in a 2016 ASME slide, F014-23);
- a one-off IETF experiment that defaulted old standards to "retire" (F014-24);
- tiered stability levels, each with its own removal notice (one project's policy, Kubernetes, F014-30);
- named heads accountable for removing failed trials (one company's self-report, Zalando, F014-26);
- keeping a record of rejected proposals (PEP 1, F014-25), and keeping reversed decisions marked superseded (one practitioner's practice, library Q-009-F7-6).

The cost of adopting is quantified only in health: the Cancer Drugs Fund's £968m (F014-9), and a modelled York estimate of the health that one adoption would have displaced (F014-13).

The cost of declining appears in only one account, by a partisan author: a standards body turned away work, and the people doing it left to work outside it (F014-35). One official review's finding of slow action on harm (F014-33) counts as a cost of declining only on my reading. No source quantifies the cost of declining (Input reader's gap statement).

No organisation was found that stopped scanning on purpose and said why (Input reader's gap statement; §6).

**Opinion (mine).** Most findings come from process safety and health, not from AI build practice (see "Thin, absent or from a different field"). So in my opinion they transfer at most as analogy, not as measured effect.

**Grading key.**
- **B:** the Input reader reports opening the page, or the Source checker opened it in round 1 (said where it applies). B items stay unconfirmed until the Source checker confirms them. "(fetch)" means the quote came through a fetch tool and the reader did not see the raw text. Exact-text PDFs are F014-1 to -3, -19 and -32; the reader also lists the Laughland PDF (F014-4 to -7) as exact text.
- **assumed (search-only):** seen only in a search extract.
- **Unconfirmed claim:** the Source checker opened the source and did not find the claim, or could not open it. It is not relied on anywhere.
- **Library entries:** carry their own grade.

**Fact / estimate / opinion:** marked on each item.

---

## 1. Benefit, no benefit or harm

**No controlled comparison exists.**
- **Fact, B (reader's own gap statement).** The evidence is audits, case series and before/after counts.
- **Opinion (mine, from the reader's gap statement).** The findings below are therefore observational or descriptive. None tests a cause.

**Process-safety records link accidents and citations to absent or weak change control (MOC). They do not show that MOC helps.**
- **Fact, B (F014-1, exact).** Across 630 chemical-industry accidents from 1990 to 2015, MOC failure made up 9.1% of the cause attributions (149 of 1,633 attributions, since accidents had multiple causes). It is not 9.1% of the 630 accidents.
  - **Opinion (the authors' assertion, B, F014-1).** The authors state that MOC-related accidents did not decrease over the period; they give no trend figures.
  - *Disagreement:* the same paper cites a study (Gambetti 2013, not opened) putting 80% of large incidents down to MOC failure. A separate search (F014-5, B) found only 4 of 891 eMARS reports explicitly MOC-related, and its author doubts the data's quality. The figures differ by an order of magnitude and use different bases (cause attributions, large incidents, reports). The Input reader suggests this is possibly because incidents are coded differently.
- **Fact, B (F014-4).** In OSHA's refinery inspections (2007–2011), MOC was 9% of process-safety citations, and 42% of those were for having no MOC system established or in use.
  - The OSHA figures are secondary.
  - *Stake:* ABB Consulting sells MOC audits.
- **Fact, library, moderate (B) (Q-009-F13-10).** A 2002 survey cited by CSB staff found only 44% of firms' MOC programmes assessed organisational change.

**Health: an adoption route that bypassed full assessment cost a lot and could not be shown to help.**
- **Fact, B (fetch) (F014-9).** England's Cancer Drugs Fund cost £968m (October 2010 – March 2015) and overspent. The NAO said its impact on patient outcomes could not be evaluated.
  - The NAO report also says its work "was not designed to assess the value for money of the Fund". The Source checker confirmed this from the report PDF, not from the web page.
- **Fact, B (primary paper opened at abstract level by the Source checker) (F014-10).** Aggarwal et al. (Annals of Oncology 28(8)) report that of 47 indications in the fund, 18% met ESMO clinical-benefit criteria and 55% had been rejected by NICE as not cost-effective.
  - The abstract gives 9 of 47 for the ESMO figure. That is 19.1%, but the paper says 18%.
  - The news page the Input reader opened does not name the authors.
  - *Disagreement, assumed (search-only):* a patient charity's chief executive called the fund "totally transformational" for breast cancer patients. This is not on the news page.
- **Fact, library, moderate (B) (Q-009-F13-2).** A review of more than 3,000 trials found 396 medical reversals.
- **Fact, library, moderate (B) (Q-009-F13-3).** Established ineffective practice is hard to dislodge. This is the authors' assertion.

**Software: one company reports costs from too broad an adoption policy.**
- **Fact, B (fetch) (F014-26).** Zalando reports that too-broad technology choice raised tooling, maintenance and duplication costs.
  - *Stake:* self-report.
- **Fact, library, moderate (B) (Q-009-F13-9 / F7-7).** DORA found no evidence that formal external change approval lowers change failure rates.
  - *Stake:* Google. The data are from 2019.

**Where the evidence is thin.**
- No source measures the net benefit of a scanning programme (Input reader's gap statement).
- **Opinion (mine).** Library Q-009-F13-12 (weak (C); a glossary summary of Rogers, and Rogers was not opened) describes a pro-innovation bias: diffusion research gives too little consideration to rejection or discontinuance. That suggests to me that published accounts may under-report rejection and discontinuance.

## 2. How proposals were judged, including changes to something already in use

**Health horizon scanning: in one network survey, filtering used common criteria and removing obsolete technology was a minority aim.**
- **Fact, B (exact) (F014-19).** In the EuroScan agencies, filtering used burden, benefit, cost and timing. Only 5 of 15 agencies named removal of obsolete technologies as a purpose.
  - *Stake:* the authors work at a member agency.

**Reassessment of technologies already in use: one survey documents the barriers and a pragmatic selection.**
- **Fact, B (fetch) (F014-14).** Reported barriers were political push-back, clinician resistance, poor evidence, lack of expertise, and a lot of work for small savings. Prioritisation is "often based on some combination of utilization rates, ease of reassessment".
  - **Assumed (search-only):** a companion systematic review calls reassessment "in its infancy".

**Disinvestment candidates largely dissolved on inspection.**
- **Fact, B (fetch) (F014-15).** Of 65 "cannot recommend" Cochrane reviews screened, 43% gave candidates. Many interventions were no longer in use, or the evidence could not rule out benefit. That challenged the assumption of large savings.
  - *Stake:* NICE and Cochrane ran the work.

**One researcher argues that stopping needs more certainty than starting.**
- **Opinion, B (fetch) (F014-16).** An NIHR researcher writes that a "do not recommend" ruling needs more certainty than leaving a treatment to clinical discretion, partly because of legal challenge.

**Changes to plant in use.**
- **Fact, B (exact) (F014-2, F014-3).**
  - The Flixborough inquiry recommended that temporary changes get the same formal safety review as permanent ones.
  - Temporary changes were 10.1% of MOC failures and are linked to time pressure.
  - Requested (planned) changes were the largest share of MOC failures (45.6%).
  - Under urgency, breakdown changes saw bypassing and simplified risk assessment.
- **Opinion, B (F014-6, F014-7).**
  - The author states a concern that MOC systems seen as overly bureaucratic may be bypassed, or that shortcuts are created. No rate is given.
  - The author says signatories may have been added to cover competence gaps.
  - The author asks whether a short and long form could be used. This is posed as a question, not a recommendation.
  - *Stake:* consultancy.
- **Opinion, B (fetch) (F014-8).** A process-safety writer argues that shortcuts follow when MOC takes longer than the change itself. He says a repeat change may skip full MOC only if the earlier one was properly documented.
  - *Stake:* none stated on the page.
- **Fact, B (exact) (F014-32).** ICH says the envisioned post-approval "operational flexibility" for medicines has not been achieved. It puts this down to a lack of harmonised approaches to lifecycle management, which "can hinder innovation and continual improvement".
  - *Stake:* industry gains from lighter change control.

**Software proposal criteria.**
- **Fact, B (fetch) (F014-25).** Python's PEP 1 sets minimum criteria for accepting a proposal (net improvement, solid implementation).
- **Fact, library (Q-009-F13-1, moderate (B)).** Thoughtworks' Trial ring requires seeing the technology deployed in production.
- **Fact, library (Q-009-F13-8, moderate (B)).** RFC 7282 judges consensus by open issues, not head counts.

**Gap.** No source measures whether stricter judging criteria produce better adoptions (Input reader's gap statement).

## 3. How proposals were approved

**Only descriptions exist; nothing compares approval models (Input reader's gap statement).**
- **Fact, B (fetch) (F014-22).** ISO members vote to confirm, revise or withdraw, usually by simple majority. Withdrawal needs a further 8-week ballot. The page says this guidance is not binding.
- **Fact, B (fetch) (F014-25).** Python's Steering Council, or a delegate, has final authority.
- **Fact, B (fetch) (F014-27).** By 2024, Zalando took radar proposals as GitHub-issue pitches, a principal-engineer panel voted on ring changes, and bigger changes were discussed quarterly.
- **Opinion, B (fetch) (F014-27).** Zalando's lead said good discussions take a lot of time and that incentives fail without the right culture.
- **Fact, library (Q-009-F13-1, moderate (B)).** Thoughtworks uses votes by a senior advisory board at a four-day meeting.

**When the scanner only advises, uptake is reported only in one interviewee's estimate and one critic's commentary.**
- **Fact, B (fetch) (F014-14).** Many reassessment programmes were only advisory.
- **Estimate, B (fetch) (F014-14).** One interviewee estimated that the decision-making body accepted the programme's recommendations about half the time. In the same account, the government almost always acted on the Board's advice. This is one person's estimate, not a measured rate.
- **Opinion, B (fetch) (F014-34).** This is commentary on Australia's MBS review. The page gives more than 5,700 items on the MBS and more than 1,400 recommendations made (fact). A critic says only about 200 have been changed (her understanding) and that the minister watered advice down under clinician pressure.
  - *Stake:* advocacy viewpoint.

**One paper says approval responsibility for planned changes should be defined.**
- **Opinion, B (exact) (F014-3): the Han Siong authors' own recommendation, not a named guidance document.** Writing about planned (requested) changes, the paper says the responsibility for approving them should be carefully defined, and approval given after review by competent personnel.

**Where sources pull different ways.**
- **Fact, library (Q-009-F13-9 / F7-7).** DORA found no evidence that formal external approval was associated with lower change failure rates (Google stake; 2019 data).
- **Fact, B (F014-1, -3, -4, -5).** The MOC sources record absent, failed or bypassed change processes in a cause typology, inspection citations and incident reports.
- **Opinion (mine).** These two are not strictly contradictory. They come from fields with very different consequences of failure. Neither tests an approval model directly.

## 4. What adopting, and what declining, cost

**Cost of adopting.**
- **Fact, B (fetch) (F014-9).** £968m for the Cancer Drugs Fund (above).
- **Estimate, B (fetch) (F014-13).** The York researchers' estimate (Claxton et al., via a university release) puts the NHS threshold at £18,317 per QALY, based on 2008 spending.
  - In their modelled hypothetical, ranibizumab for diabetic macular oedema "would have displaced" 4,367 QALYs, or 295 deaths.
  - The release says the threshold NICE uses is probably too high.
  - **Opinion (mine, inferred from F014-13; not stated on the page).** On that estimate, adopting above the threshold would displace more health than it gains. This frames the cost of adopting as the value of whatever it displaces. It is the only quantified argument in the set that declining can have a benefit, and it is modelled, not observed.
- **Fact, B (fetch) (F014-26).** Zalando reports tooling, maintenance and duplication costs from broad adoption.

**Cost of declining.**
- **Fact, B (fetch); opinion-laden (F014-35).** In 2004 the W3C "told them that work wasn't welcome" (continuing HTML work), and individuals from Apple, Mozilla and Opera founded WHATWG outside W3C. W3C later "changed its mind" and let XHTML2's charter expire at the end of 2009.
  - *Stake:* the author says "I get paid for it"; no payer is named.
- **Fact, B (fetch, secondary on the official review) (F014-33).** The Cumberlege review found a system that failed to listen to patients and, when it acted, "too often moved glacially".
  - **Opinion (mine).** I read this as a cost of slow retirement. The review itself is about slow action on harm, not about retirement.
  - The report itself was not opened.
- **Gap.** No source quantifies the cost of a rejected proposal. The UK Accelerated Access Review's slow-adoption figures could not be confirmed (Input reader's gap statement).

## 5. How adopted practices were reviewed and retired

**Scheduled review with automatic lapse (described, outcome unmeasured).**
- **Fact, B (fetch) (F014-22).** ISO reviews an International Standard every 5 years and a Technical Specification every 3. The page recommends confirming a TS only once.
- **Fact, B (ASME 2016 slide, opened by the Source checker) (F014-23).** An American National Standard under continuous or periodic maintenance that is not revised or reaffirmed within 10 years loses its status. "Stabilized maintenance" takes mature, non-safety standards out of the regular revision cycle, but they still need a status review every 10 years.
  - The current ANSI text was not opened.
- **Fact, library (Q-009-F5-8, weak (C)).** Thoughtworks fades an entry when its opinion has not changed for two successive Radars.
- **Fact, library (Q-005-LF-Q005-15, weak (C)).** Half of 17 AHRQ guidelines were outdated after 5.8 years.

**A review rule that, per one RFC, had never been followed.**
- **Fact, B (fetch) (F014-24).** The IETF's RFC 2026 procedure for reviewing immature standards "has never been followed". A 2004–05 experiment reviewed about 125 old Proposed Standards, defaulted each to "retire", and proposed dozens for Historic status.
  - The RFC's own counts are inconsistent (61 vs 44).
  - The Source checker records the RFC's stated purpose as "to determine how many Proposed Standards could be considered obsolete" (round 3).
- **Opinion (mine).** The experiment is an instance of "retire unless someone objects" being used as a default. Clearing a backlog was not the RFC's stated purpose.

**In one scheme, re-appraisal after provisional funding almost always ended in a recommendation.**
- **Fact, B (fetch) (F014-12).** Under the reformed Cancer Drugs Fund, 19 of 20 exits were recommended. The abstract excludes one terminated evaluation. Yet 12 of 20 (60%) did not fully resolve the original uncertainty.
  - *Stake:* the authors' consultancy serves pharmaceutical clients.
  - **Assumed (search-only):** a 2025 abstract reports 23 of 24 re-appraisals positive.
- **Opinion (mine, on F014-12 only).** In this one scheme (20 technologies, one consultancy abstract), provisionally funded technologies were mostly recommended at exit. Whether provisional approvals elsewhere behave the same way is untested.

**Tiered lifetimes by maturity.**
- **Fact, B (fetch; page truncated) (F014-30).** Kubernetes does not remove GA APIs within a major version. Beta APIs are served at least 9 months or 3 releases after deprecation. Alpha APIs can be removed without notice.

**Deprecation without removal (unconfirmed).**
- **Unconfirmed claim, search-only (F014-31).** In 50 Java APIs across 297,254 projects, consumers mostly did not react to deprecation.
  - The Source checker could not open it (login redirect). It is not relied on.
- **Unconfirmed claim, search-only; the authors' argument (F014-31).** The authors argue that never removing deprecated features has cheapened deprecation.

**Telling people to stop: little change in the two recorded cases.**
- **Fact, B (fetch) (F014-17).** A scoping review of 109 papers found active change interventions "associated with the greatest likelihood of de-adoption". In one included study (two NICE topics), "do not do" reminders showed no association with practice change. That is not a finding of the review as a whole.
- **Opinion, B (fetch) (F014-17).** The authors argue that without a sustainability plan, clinicians revert.
- **Fact, B (fetch, via news) (F014-18).** Of 7 Choosing Wisely low-value services, 2 declined slightly, 3 stayed flat and 2 rose.
  - *Stake:* the data and lead author are from Anthem, an insurer.

**Two audits recommended reviewing open items.**
- **Opinion, B (F014-7).** These are recommendations from two named audits, not a general finding:
  - from a Seveso III refinery audit: formal close-out of MOCs and time limits on temporary changes;
  - from a Middle East chemical-plant audit: a routine review process for all open MOCs.
  - *Stake:* consultancy.

**Accountable retirement in software.**
- **Fact, B (fetch) (F014-26).** Zalando made heads accountable for removing failed trials, archived Hold entries, and phased out Clojure, Haskell and Rust for new applications.
  - *Stake:* self-report; no outcome measured.
- **Fact, B (fetch; opened by the Source checker; page undated) (F014-29).** Thoughtworks staff call the Hold ring ambiguous: it can mean "not ready yet" or "please stop".
- **Opinion, B (fetch); unreliable (F014-28).** A post claims radar governance is a "one-way valve" and that Thoughtworks has demoted only two technologies into Hold.
  - The source may be machine-generated or satirical. Its statistics have no links and are not corroborated.
  - I give it no weight beyond noting the claim. **Not proposed for the library.**

**Keeping records of what was rejected or retired.**
- **Fact, B (fetch) (F014-25).** PEP 1 gives proposals statuses including Rejected, Withdrawn, Deferred and Superseded. Of a rejected PEP it says "It is still important to have a record of this fact". The page does not say that Rejected or Withdrawn PEPs stay in the index.
  - Avoiding repeat proposals is the purpose of a separate PEP 1 item, a PEP's "Rejected Ideas" section, not of the status record.
  - The page shows "last modified 2026-11-08", so it is a moving page.
- **Opinion, library (Q-009-F7-6, moderate (B)).** Architecture decision records keep a reversed decision and mark it superseded.

**Gap.** No study tracks over years whether retired practices come back (Input reader's gap statement).

## 6. When, if ever, organisations stopped scanning, and why

**No organisation was found that publicly stopped scanning and gave reasons.**
- **Fact, B (exact) (F014-20).** Australia's medicines industry body stated in 2022 that there was no nationally coordinated horizon-scanning process. The paper does not say one existed earlier or that anything stopped, so it is not evidence of stopping.
  - *Stake:* the industry body wants faster access for its members' products.
  - **Assumed (search-only):** a 2023 government communique says the same.

**One recorded case of weakening; no recorded case of stopping.**
- **Fact, B (fetch) (F014-26).** Zalando's first radar was "easy to ignore due to lack of a formal process" and depended on fading volunteer effort.
- **Unconfirmed claim (F014-21).**
  - The Input reader's search extract said Austria's oncology horizon-scanning programme "lacks customers actively requesting assessments", and that its effect on practice and costs was not evaluated.
  - The Source checker opened the abstract (rounds 1 and 3) and found neither statement in it. The abstract reports users satisfied with the outputs.
  - It is not relied on.
  - *Stake:* the authors run the programme.
- **Fact, B (exact) (F014-19).** Almost half of EuroScan agencies had fewer than 2 full-time staff. This is context only: it shows the agencies are small, not that any of them weakened.
- **Opinion (mine).**
  - In the one recorded case, Zalando's first radar (F014-26, self-report), a scanner weakened through neglect, not through a decision to stop. It had no formal process and relied on fading volunteer contributions.
  - EuroScan staffing (F014-19) is not used as support. F014-21 is unconfirmed and not relied on.
  - No decision to stop scanning was found (Input reader's gap statement).

**Not found.** Whether AHRQ's horizon scanning or HealthPACT closed, and any company that announced dropping its tech radar.

---

## Thin, absent or from a different field

**Thin or absent:**
- controlled outcomes of scanning (Input reader's gap statement; §1);
- comparisons of approval models (Input reader's gap statement; §3);
- quantified costs of declining (Input reader's gap statement; §4);
- long-term follow-up on retirement (Input reader's gap statement; §5);
- any reasoned decision to stop scanning (Input reader's gap statement; §6).

**From a different field.** By my count of the 35 findings:
- 8 are from process safety (F014-1 to -8);
- 15 are from health (F014-9 to -21, -33, -34);
- 5 are from standards bodies or medicines regulation (F014-22 to -24, -32, -35);
- 7 are from software (F014-25 to -31).

**Opinion (mine).** Several of these are not quite "scanning outside practice":
- MOC is internal change control (F014-1 to -8);
- the Cancer Drugs Fund is a funding route (F014-9 to -12);
- standards review is maintenance (F014-22 to -24).

**How far it transfers. Opinion (mine).**
- Structural features may transfer to a small AI-build organisation: time limits (F014-7), review of open items (F014-7), records of rejection (F014-25), and the scattered signs that retiring is harder than adopting (opening bullet 1).
- In my opinion, effect sizes should not be carried over.
- The software sources are closer in kind but have no outcome data: Zalando is a self-report (F014-26, -27), and Kubernetes (F014-30) and PEP 1 (F014-25) are project policies.

## Stakes summary

| Source | Stake |
|---|---|
| ABB / Laughland (F014-4 to -7) | sells MOC audits |
| Costello Medical (F014-12) | serves pharmaceutical clients |
| Anthem (F014-18) | insurer, own data and lead author |
| NICE / Cochrane (F014-15) | ran the work |
| Packer (F014-19) | works at a member agency |
| Ludwig Boltzmann Institute (F014-21) | runs the programme |
| Medicines Australia (F014-20) | industry body |
| Sivonen (F014-35) | partisan; says he is paid for the work, payer not named |
| Zalando (F014-26, -27) | self-report |
| Thoughtworks (library entries, F014-29) | consultancy |
| ICH (F014-32) | industry benefits from lighter change control |
| Peter Clark (F014-11) | chaired the Cancer Drugs Fund |

## Sources needed that the Input reader did not open (gaps)

1. Aggarwal et al., Annals of Oncology 28(8): the full paper. The Source checker opened the abstract only.
2. The IMMDS (Cumberlege) report itself.
3. The OSHA refinery National Emphasis Program documents.
4. Gambetti 2013.
5. Current ANSI Essential Requirements text.
6. The 2012 Leggett systematic review.
7. The MBS Review Taskforce final and obsolete-items reports.
8. The 2015 AHRQ horizon-scanning evaluation (the PDF came back empty).
9. Accelerated Access Review figures.
10. Sawant et al. full text.
11. The Nachtnebel et al. 2016 full text (the Source checker opened the abstract only).
12. The 2025 ISPOR Cancer Drugs Fund re-appraisal abstract.
13. W3C records of the 2004 workshop.
14. A Thoughtworks Radar archive, to count moves into Hold.
15. Any record of whether Australia ever had a national horizon-scanning unit and, if so, whether and why it closed.

None of these needs a paid source or a level-5 expert as far as I can tell. The Aggarwal paper and Sawant et al. may be paywalled.

**Questions I add (neutral, for whoever triages):**
- (a) Across fields, how often are provisional or conditional approvals reversed at re-appraisal, and what predicts reversal?
- (b) What happened to scanning programmes that lapsed, and to the decisions they used to feed?

---

## What each possible answer would change (as the question frames it)

- **Patterns that held up elsewhere become candidates.** None has outcome evidence, so each would enter as an opinion-grade pattern (my opinion). The described candidates are:
  - time limits and formal close-out for temporary changes, and routine review of all open changes (recommendations from two named audits, F014-7);
  - the same safety review for temporary as for permanent changes (the Flixborough recommendation, as quoted in F014-2);
  - scheduled review by member vote (ISO, F014-22);
  - loss of status after 10 years without revision or reaffirmation (ANSI, per a 2016 ASME slide, F014-23);
  - a one-off default-to-retire experiment (F014-24);
  - fading unchanged entries (library Q-009-F5-8, weak (C));
  - tiered stability with stated removal notice (one project's policy, F014-30);
  - named, accountable heads for removing failed trials (one company's self-report, F014-26);
  - records of rejected and superseded proposals (F014-25), and reversed decisions kept and marked superseded (one practitioner's practice, library Q-009-F7-6);
  - short and long forms of review (F014-6, posed there only as a question).
- **Documented harms become things to avoid.** Recorded, each from few sources:
  - no change process in place: 39 of 92 OSHA refinery MOC citations (42%; F014-4, secondary), and 4 of 891 eMARS reports, all with no MOC used (F014-5, data quality called very poor). These are citations and reports, not counts of failures.
  - MOC failure was 9.1% of cause attributions in one study of 630 accidents (F014-1);
  - bypassing and simplified risk assessment for breakdown changes under urgency (F014-3);
  - temporary changes were 10.1% of MOC failures in one study's typology, linked to time pressure (F014-2);
  - adoption whose effect on outcomes could not be evaluated (one fund, F014-9);
  - in one scheme, provisional funding recommended at exit without fully resolving the original uncertainty in 12 of 20 cases (F014-12);
  - slow action on harm, from one official review read through a secondary blog (F014-33).
- **Stated concerns and commentary, not documented harms:**
  - a heavy process inviting bypassing: one consultancy author's stated concern (F014-6) and one writer's opinion (F014-8);
  - advisory scanning whose advice is watered down: one critic's commentary (F014-34). F014-14 does not show override. In one interviewee's estimate, the decision-making body accepted the advice about half the time, and government almost always followed the Board.
  - Deprecation without removal (F014-31) is unconfirmed and is not counted.
- **Finding no benefit, or a high cost of declining.**
  - No net-benefit evidence was found either way (Input reader's gap statement).
  - The cost of declining is documented only anecdotally (F014-35; F014-33 on my reading only).
  - The cost of adopting is quantified only in health (F014-9, and the modelled F014-13).
  - How much this weighs on whether and how to scan is for the owner to judge.
- **Retirement and stopping rules that worked or failed.**
  - *Little change:* "do not do" reminders, in one study included in a scoping review (F014-17). Also the Choosing Wisely campaign (a campaign, not a reminders trial): 2 of 7 flagged services declined slightly (F014-18; insurer data).
  - *Not applied:* a review rule that one RFC says was never followed (F014-24).
  - *Active de-adoption:* active change interventions were associated with the greatest likelihood of de-adoption, in one scoping review (F014-17).
  - *Automatic lapse:* exists (F014-23, per a 2016 slide), with no outcome measured.
  - *Stopping rules:* none with any record of working or failing were found (Input reader's gap statement). F014-20 shows only that no coordinated process existed in 2022. F014-26 is one case of neglect, not a rule. F014-21 is unconfirmed and not relied on.

---

## Proposed library entries
*(statement | type | grade | proposed shelf life; all grades pending the source check)*

1. Han Siong et al. 2017: across 630 chemical-industry accidents (1990–2015), MOC failure made up 9.1% of cause attributions (149 of 1,633); the authors assert no decrease over the period, without trend figures; they cite Gambetti's 80% as a disagreeing figure | fact | B | 5 years
2. Han Siong et al.: temporary changes were 10.1% of MOC failures, linked to time pressure; Flixborough recommended the same review as for permanent changes | fact | B | 5 years
3. Laughland (ABB, consultancy stake): OSHA refinery inspections 2007–2011, MOC was 9% of citations and 42% of those were for no MOC system (secondary figures) | fact | B | 5 years
4. Laughland: two named audits (a Seveso III refinery, a Middle East chemical plant) recommended formal close-out, time limits on temporary MOCs and a routine review of all open MOCs; these are recommendations, not general findings | opinion | B | 5 years
5. Laughland: states a concern that MOC systems seen as overly bureaucratic may be bypassed; asks whether a short and long form could be used | opinion | B | 5 years
6. NAO 2015: Cancer Drugs Fund cost £968m (Oct 2010 – Mar 2015), overspent, and its effect on outcomes could not be evaluated; the work was not designed to assess value for money (report PDF) | fact | B | 10 years
7. Aggarwal et al., Annals of Oncology 28(8) (abstract opened): of 47 fund indications, 18% met ESMO benefit criteria (9 of 47, which is 19.1%) and 55% (26) had been rejected by NICE; a patient charity disagreed (search-only) | fact | B (abstract only) | 10 years
8. Haycock et al. (ISPOR 2022, pharma-consultancy stake): 19 of 20 Cancer Drugs Fund exits recommended (excluding one terminated evaluation); 60% did not fully resolve the original uncertainty | fact | B | 3 years
9. Claxton et al. (York release): NHS threshold estimated at £18,317 per QALY (2008 spending); in a modelled hypothetical, ranibizumab for DMO would have displaced 4,367 QALYs; the release says the threshold in use is probably too high | estimate | B | 5 years
10. Leggett et al. 2012: barriers to health-technology reassessment; many programmes advisory; one interviewee estimated the decision-making body accepted recommendations about half the time, with government almost always following the Board | fact | B | 5 years
11. Docherty et al. 2011: of 65 "cannot recommend" Cochrane reviews, 43% gave disinvestment candidates; many interventions were already out of use | fact | B | 10 years
12. Niven et al. 2015: active change interventions were associated with the greatest likelihood of de-adoption; in one included study, "do not do" reminders not associated with change; the authors argue clinicians revert without a sustainability plan | fact (the reversion point is the authors' argument) | B | 5 years
13. Rosenberg et al. (via AJMC; Anthem stake): of 7 Choosing Wisely services, 2 declined, 3 stayed flat, 2 rose (data to 2013) | fact | B | 5 years
14. Packer et al. 2015 (authors at a member agency): of 15 EuroScan agencies, 5 named removing obsolete technology as a purpose; almost half had under 2 FTE | fact | B | 5 years
15. ISO/TC 211: IS reviewed every 5 years, TS every 3; confirm, revise or withdraw by vote; withdrawal needs a further 8-week ballot | fact | B | 3 years
16. RFC 4450: the RFC 2026 review procedure had never been followed; the 2004–05 experiment, whose stated purpose was to determine how many Proposed Standards could be considered obsolete, defaulted about 125 old standards to "retire" | fact | B | 10 years
17. PEP 1: proposals carry statuses including Rejected, Withdrawn, Deferred and Superseded, and a rejection should be on record; a separate "Rejected Ideas" section records turned-down ideas; final authority with the Steering Council or a delegate | fact | B | 2 years
18. Zalando 2020: the first radar was easy to ignore; broad choice raised costs; gave decision rights to Principal Engineers and accountability for removing failed trials (self-report) | fact | B | 3 years
19. Kubernetes deprecation policy: GA not removed within a major version; beta at least 9 months or 3 releases after deprecation; alpha removable without notice | fact | B | 2 years
20. ICH Q12 concept paper 2014: the envisioned post-approval operational flexibility had not been achieved; lack of harmonised lifecycle approaches can hinder innovation and continual improvement | fact | B | 10 years
21. Medicines Australia 2022: no nationally coordinated horizon-scanning process in Australia (not evidence that one existed or stopped) | fact | B | 2 years
22. Pattern: give every temporary change a time limit, close changes out formally, and review all open items routinely. Origin: two audits' recommendations and Flixborough (items 2, 4). Effect unmeasured | pattern | opinion built on B | 3 years
23. Pattern: pair any "stop doing" ruling with active change work, not a list alone. Origin: item 12 (one scoping review's association for active interventions; one included study for the reminders result) and item 13 (one campaign, 2 of 7 services declined; insurer data). Effect of the pattern itself unmeasured | pattern | opinion built on B | 3 years
24. Pattern: in the one scheme studied (the reformed Cancer Drugs Fund), provisionally funded technologies were mostly recommended at exit; state in advance what evidence would reverse one. Origin: item 8. The second clause is my opinion and is not in the source (the filed P24 omits it) | pattern | opinion built on B | 3 years

Not proposed:
- F014-28 (unreliable source).
- F014-21 (opened at abstract level by the Source checker; the claim was not found) and F014-31 (search-only; the Source checker could not open it). Both are unconfirmed claims.
- F014-23 (a 2016 slide; current ANSI text not opened) and F014-29 (attributed staff opinion, undated page). Both are now opened by the Source checker but not proposed in this round.
- F014-11, -16, -27, -33, -34, -35 (attributed opinion or secondary; fileable only as attributed opinion if the checker wishes).

## Finding ids relied on, for the Source checker

- **Input reader:** F014-1 to F014-35.
  - F014-28 is noted but given no weight.
  - The unconfirmed claims, not relied on, are F014-21 (abstract opened, claim not found) and F014-31 (could not open).
  - Search-only sub-claims sit in -10, -12, -14 and -20.
  - F014-23 and F014-29 were opened by the Source checker in round 1.
- **Library entries cited:** Q-009-F13-1, F13-2, F13-3, F13-8, F13-9, F13-10, F13-12, F7-6, F7-7, F5-8, and Q-005-LF-Q005-15. The source check says the Q-009 entries are on the unmerged branches build/source-checker/q009-a and q009-b, not on portfolio main. They were present in the working tree read at /home/user/portfolio/library/.
- **Library files read** (all under /home/user/portfolio/library/):
  - /home/user/portfolio/library/README.md
  - /home/user/portfolio/library/facts/Q-009-F13-1.md
  - /home/user/portfolio/library/facts/Q-009-F13-2.md
  - /home/user/portfolio/library/facts/Q-009-F13-3.md
  - /home/user/portfolio/library/facts/Q-009-F13-8.md
  - /home/user/portfolio/library/facts/Q-009-F13-9.md
  - /home/user/portfolio/library/facts/Q-009-F13-10.md
  - /home/user/portfolio/library/facts/Q-009-F13-12.md
  - /home/user/portfolio/library/facts/Q-009-F5-8.md
  - /home/user/portfolio/library/facts/Q-009-F7-6.md
  - /home/user/portfolio/library/facts/Q-009-F7-7.md
  - /home/user/portfolio/library/facts/Q-005-LF-Q005-15.md

## Tokens

I cannot see my total tokens.

---

# Change list (this round, answering source-check round 3 and the summary-sentence check)

**Round 3 corrections**

| # | Item | What changed | Answers |
|---|---|---|---|
| 1 | Opening bullet 3; "Documented harms" list; §2 F014-6 line; entry 5 | "Heavy, one-size-fits-all approval invites bypassing" is gone. Bypassing is now attributed as Laughland's stated concern (F014-6) and Sutton's opinion (F014-8), with no rate. In "What each answer would change" it moves out of "Documented" into a new "Stated concerns and commentary" list. "Heavy, uniform" became "seen as overly bureaucratic". | R3 correction 1 |
| 2 | Opening bullet 3 | "Many change failures trace to having no change process" became 39 of 92 OSHA MOC citations (42%) and 4 of 891 eMARS reports, and it says these are citations and reports, not failures. | R3 correction 2 |
| 3 | §3 approval-responsibility item; §2 F014-6 signatories | §3 is now an Opinion: the Han Siong authors' own recommendation about planned changes, not a named guidance. Its heading is scoped to one paper. "Signatories pile up" became "signatories may have been added". | R3 correction 3 |
| 4 | Opening bullets 1 and 4 | Bullet 1 is now my opinion from scattered cases, listing each case (F014-24, F13-3 as an assertion, F014-17 one included study, F014-18 2 of 7, F014-16 opinion), and says no source compares the two directly. Bullet 4 is now "the one software case", quoting "lack of a formal process"; "not tied to a decision" and "tends to" are dropped. | R3 correction 4 |
| 5 | §6 closing opinion | Now "one recorded case" (Zalando, F014-26). F014-19 is dropped as support and marked context only. | R3 correction 5 |
| 6 | §6 F014-21 | Relabelled "Unconfirmed claim". It notes the abstract reports users satisfied with the outputs. | R3 correction 6 |
| 7a | §5 F014-12; entry 8; opening bullet 2 | Added "the abstract excludes one terminated evaluation". | R3 correction 7 |
| 7b | §5 CDF opinion; pattern 24 | "Provisional recommendations mostly became full ones" became "mostly recommended at exit". | R3 correction 7 |
| 7c | §5 F014-17; entry 12; "what each answer would change" | "Most likely to produce" became "associated with the greatest likelihood of". | R3 correction 7 |
| 7d | "What each answer would change", retirement rules | "Failed: reminders (F014-17; F014-18)" became "Little change". Choosing Wisely is described as a campaign, not a reminders trial. The never-followed RFC rule is now "Not applied". | R3 correction 7 |
| 7e | §5 RFC 4450 opinion; entry 16 | "Used to clear a backlog" is dropped. The stated purpose is given as the Source checker recorded it (round 3), and the remaining reading is marked as my opinion. | R3 correction 7 |
| 8 | §1 F014-1 disagreement | "Probably" became "possibly", attributed to the Input reader. | R3 correction 8 |

Rounds 1 and 2: round 3 records all of their corrections as applied, so none was open.

**Summary-sentence check**

| # | Item | What changed |
|---|---|---|
| 9 | Opening paragraph | "A set of failure patterns that keep recurring" became "a few problems … each from one case, one study, or attributed opinion". The no-comparison sentence now cites the reader's gap statement. |
| 10 | Opening bullet 2 | Now cites F014-12 and says "technologies" and "exit evaluations", in place of "drugs" and "reviews". |
| 11 | Opening fixes list | Each fix now names its source and how strong it is. "Automatic lapse / retire unless renewed" is split into the ISO, ANSI and IETF items, since ISO is a scheduled vote, not a lapse. |
| 12 | Opening paragraphs on costs, stopping and transfer | Each now cites its findings (F014-9, -13, -35, -33 on my reading, and the gap statement). The transfer sentence is marked as my opinion. |
| 13 | Body headings that stated general rules | These are scoped to their base: §1 MOC and software; §2 EuroScan, reassessment and F014-16; §3 advisory uptake and approval responsibility; §5 RFC, F014-31, "telling people to stop" and "open items"; §6 weakening. You can revert these. |
| 14 | §1 Opinions | "Every finding is observational" now cites the gap statement. The pro-innovation-bias line is marked as mine and cites F13-12 as a glossary summary. |
| 15 | §3 "Where sources pull different ways" | "DORA: heavy approval did not help" and "missing approval causes accidents" were stronger than the findings. They are now split into the DORA library fact (no evidence of association) and what the MOC findings record, followed by my opinion. |
| 16 | §4 F014-13 opinion | "Clearest" became "only quantified argument", and it says it is inferred from F014-13. |
| 17 | F014-31 (§5, "Documented harms", "Not proposed", ids list) | Relabelled "Unconfirmed claim" and removed from the documented-harms list. This is the same rule as correction 6: a claim the checks left unconfirmed supports nothing. |
| 18 | "Thin, absent or from a different field" | Each absence now cites the gap statement and its section. "Most of the evidence" became my count by field (8, 15, 5 and 7 of 35 findings). "Not quite scanning" and "effect sizes do not transfer" are marked as my opinion. The software sources are cited by id. |
| 19 | "What each answer would change", candidates list | Each candidate now names its source and how strong it is. F014-2 is limited to the Flixborough same-review recommendation, since the time limits come from F014-7. The ISO, ANSI and IETF items are split, and F5-8 is added because it is already cited in §5. |
| 20 | "What each answer would change", documented harms | Each harm now has its base and qualifier. Concerns and commentary (F014-6, -8, -34) are separated out, and F014-31 is excluded. |
| 21 | Patterns 23 and 24 | Pattern 23's origins are stated at their actual strength. Pattern 24's "state in advance" clause is marked as my opinion, not in the source, and it notes the filed P24 omits it. |
| 22 | Researcher italic line; grading key; gaps list item 11 | The italic line is updated for this round. The key adds the "Unconfirmed claim" label. Gap 11 now says the Nachtnebel full text, since the abstract was opened. |

No new outside claims were added. The F014-24 stated-purpose quote is taken from the Source checker's round 3 record.

# Finding ids for the Source checker to re-check

- **Body wording changed:** F014-1, F014-3, F014-6, F014-12, F014-17, F014-21, F014-24, F014-31.
- **Summary citations to check against the recorded findings:** F014-2, -4, -5, -7, -8, -9, -13, -14, -16, -18, -19, -20, -22, -23, -25, -26, -30, -33, -34, -35.
- **Library entries:** Q-009-F13-3, F13-9 / F7-7, F13-12, F7-6, F5-8.
- **Filed Q-014 entries whose memo wording changed:** 5, 8, 12 and 16, and patterns P23 and P24.

# Tokens

I cannot see my total tokens.
