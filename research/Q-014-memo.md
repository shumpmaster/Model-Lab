# Q-014 memo: what organisations that scan outside practice found when judging, approving, declining, retiring and stopping (2026-11-08)

*The Researcher's memo for Q-014, round 3 (brief 178, docs/briefs/178-researcher.md), revised after the Source checker's round 2 (research/Q-014-source-check.md); rounds 1 (brief 162) and 2 (brief 170) are in this file's history. Recorded verbatim by the Orchestrator (session_01QBwHGNSLmSrYQgS6BPjV8p), 2026-11-08, from the helper's return; only this italic line is the Orchestrator's.*

*Researcher, 2026-11-08, revised after source-check rounds 1 and 2. Sources: the Input reader's findings (research/Q-014-input.md), which are untrusted, the Source checker's round-1 and round-2 findings (research/Q-014-source-check.md), and the portfolio library. I did not use the web, and model memory is not used as a source.*

The evidence does not show whether scanning and adopting outside practice brings benefit, no benefit or harm. No source compares organisations that scan with ones that do not. What it does show, across process safety, health technology assessment, standards bodies and software, is a set of failure patterns that keep recurring:

- **Adopting is easier than retiring.** Practices stay in place after their evidence goes. Rules to stop doing something either go unapplied or barely change practice.
- **In one scheme, "adopt now, review later" almost always ended in a recommendation.** Under the reformed Cancer Drugs Fund, 19 of 20 provisional drugs were later recommended, even though 60% of the reviews had not fully resolved the original doubt. This is one scheme of 20 technologies; whether it holds elsewhere is untested.
- **Heavy, one-size-fits-all approval invites bypassing.** Many change failures trace to having no change process at all. Temporary changes are one share of MOC failures (10.1%); planned changes are the largest share (45.6%).
- **A scanner that is not tied to a decision tends to fade.** In the one software case, a radar with no formal process was easy to ignore and depended on fading volunteer effort.

Some fixes are described, but none has had its outcome measured:
- routine review of every open change, with time limits;
- automatic lapse, or "retire unless renewed";
- tiered stability levels, each with its own removal notice;
- named decision-makers who are accountable for removing failed trials;
- keeping a record of rejected proposals.

The cost of adopting is quantified in a few health cases. The cost of declining appears only as anecdote. No organisation was found that stopped scanning on purpose and said why. Most of this evidence comes from medicine, chemical plants and standards bodies, not from AI build practice, so it transfers as analogy, not as measured effect.

**Grading key.**
- **B:** the Input reader reports opening the page, or the Source checker opened it in round 1 (said where it applies). B items stay unconfirmed until the Source checker confirms them. "(fetch)" means the quote came through a fetch tool and the reader did not see the raw text. Exact-text PDFs are F014-1 to -3, -19 and -32; the reader also lists the Laughland PDF (F014-4 to -7) as exact text.
- **assumed (search-only):** seen only in a search extract.
- **Library entries:** carry their own grade.

**Fact / estimate / opinion:** marked on each item.

---

## 1. Benefit, no benefit or harm

**No controlled comparison exists.**
- **Fact, B (reader's own gap statement).** The evidence is audits, case series and before/after counts.
- **Opinion.** Every finding below is therefore observational.

**Process-safety change control (MOC) shows harm when the process is absent or weak, not proof that it helps.**
- **Fact, B (F014-1, exact).** Across 630 chemical-industry accidents from 1990 to 2015, MOC failure made up 9.1% of the cause attributions (149 of 1,633 attributions, since accidents had multiple causes). It is not 9.1% of the 630 accidents.
  - **Opinion (the authors' assertion, B, F014-1).** The authors state that MOC-related accidents did not decrease over the period; they give no trend figures.
  - *Disagreement:* the same paper cites a study (Gambetti 2013, not opened) putting 80% of large incidents down to MOC failure. A separate search (F014-5, B) found only 4 of 891 eMARS reports explicitly MOC-related, and its author doubts the data's quality. The figures differ by an order of magnitude and use different bases (cause attributions, large incidents, reports), probably because incidents are coded differently.
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

**Software: too broad an adoption policy had costs.**
- **Fact, B (fetch) (F014-26).** Zalando reports that too-broad technology choice raised tooling, maintenance and duplication costs.
  - *Stake:* self-report.
- **Fact, library, moderate (B) (Q-009-F13-9 / F7-7).** DORA found no evidence that formal external change approval lowers change failure rates.
  - *Stake:* Google. The data are from 2019.

**Where the evidence is thin.**
- No source measures the net benefit of a scanning programme.
- **Opinion.** Pro-innovation bias in diffusion research (library Q-009-F13-12, weak (C)) suggests that what has been published may under-report rejection and discontinuance.

## 2. How proposals were judged, including changes to something already in use

**Health horizon scanning filters on common criteria; removing obsolete technology is a minority aim.**
- **Fact, B (exact) (F014-19).** In the EuroScan agencies, filtering used burden, benefit, cost and timing. Only 5 of 15 agencies named removal of obsolete technologies as a purpose.
  - *Stake:* the authors work at a member agency.

**Reassessment of technologies already in use: the barriers are documented and the selection is pragmatic.**
- **Fact, B (fetch) (F014-14).** Reported barriers were political push-back, clinician resistance, poor evidence, lack of expertise, and a lot of work for small savings. Prioritisation is "often based on some combination of utilization rates, ease of reassessment".
  - **Assumed (search-only):** a companion systematic review calls reassessment "in its infancy".

**Disinvestment candidates largely dissolved on inspection.**
- **Fact, B (fetch) (F014-15).** Of 65 "cannot recommend" Cochrane reviews screened, 43% gave candidates. Many interventions were no longer in use, or the evidence could not rule out benefit. That challenged the assumption of large savings.
  - *Stake:* NICE and Cochrane ran the work.

**Stopping something needs more certainty than starting it.**
- **Opinion, B (fetch) (F014-16).** An NIHR researcher writes that a "do not recommend" ruling needs more certainty than leaving a treatment to clinical discretion, partly because of legal challenge.

**Changes to plant in use.**
- **Fact, B (exact) (F014-2, F014-3).**
  - The Flixborough inquiry recommended that temporary changes get the same formal safety review as permanent ones.
  - Temporary changes were 10.1% of MOC failures and are linked to time pressure.
  - Requested (planned) changes were the largest share of MOC failures (45.6%).
  - Under urgency, breakdown changes saw bypassing and simplified risk assessment.
- **Opinion, B (F014-6, F014-7).** Heavy, uniform MOC is seen as bureaucratic and invites bypassing. Signatories pile up to cover competence gaps. The author asks whether a short and long form could be used; this is posed as a question, not a recommendation.
  - *Stake:* consultancy.
- **Opinion, B (fetch) (F014-8).** Shortcuts follow when MOC takes longer than the change itself. A repeat change may skip full MOC only if the earlier one was properly documented.
  - *Stake:* none stated on the page.
- **Fact, B (exact) (F014-32).** ICH says the envisioned post-approval "operational flexibility" for medicines has not been achieved. It puts this down to a lack of harmonised approaches to lifecycle management, which "can hinder innovation and continual improvement".
  - *Stake:* industry gains from lighter change control.

**Software proposal criteria.**
- **Fact, B (fetch) (F014-25).** Python's PEP 1 sets minimum criteria for accepting a proposal (net improvement, solid implementation).
- **Fact, library (Q-009-F13-1, moderate (B)).** Thoughtworks' Trial ring requires seeing the technology deployed in production.
- **Fact, library (Q-009-F13-8, moderate (B)).** RFC 7282 judges consensus by open issues, not head counts.

**Gap.** No source measures whether stricter judging criteria produce better adoptions.

## 3. How proposals were approved

**Only descriptions exist; nothing compares approval models.**
- **Fact, B (fetch) (F014-22).** ISO members vote to confirm, revise or withdraw, usually by simple majority. Withdrawal needs a further 8-week ballot. The page says this guidance is not binding.
- **Fact, B (fetch) (F014-25).** Python's Steering Council, or a delegate, has final authority.
- **Fact, B (fetch) (F014-27).** By 2024, Zalando took radar proposals as GitHub-issue pitches, a principal-engineer panel voted on ring changes, and bigger changes were discussed quarterly.
- **Opinion, B (fetch) (F014-27).** Zalando's lead said good discussions take a lot of time and that incentives fail without the right culture.
- **Fact, library (Q-009-F13-1, moderate (B)).** Thoughtworks uses votes by a senior advisory board at a four-day meeting.

**When the scanner only advises, how far its advice is taken up is mixed.**
- **Fact, B (fetch) (F014-14).** Many reassessment programmes were only advisory.
- **Estimate, B (fetch) (F014-14).** One interviewee estimated that the decision-making body accepted the programme's recommendations about half the time. In the same account, the government almost always acted on the Board's advice. This is one person's estimate, not a measured rate.
- **Opinion, B (fetch) (F014-34).** This is commentary on Australia's MBS review. The page gives more than 5,700 items on the MBS and more than 1,400 recommendations made (fact). A critic says only about 200 have been changed (her understanding) and that the minister watered advice down under clinician pressure.
  - *Stake:* advocacy viewpoint.

**Approval responsibility should be defined.**
- **Fact, B (exact) (F014-3).** Process-safety guidance calls for carefully defined approval responsibility and review by competent personnel.

**Where sources pull different ways.**
- **Opinion.** DORA (heavy external approval did not help) and the MOC literature (missing or bypassed approval causes accidents) are not strictly contradictory. They come from fields with very different consequences of failure. Neither tests an approval model directly.

## 4. What adopting, and what declining, cost

**Cost of adopting.**
- **Fact, B (fetch) (F014-9).** £968m for the Cancer Drugs Fund (above).
- **Estimate, B (fetch) (F014-13).** The York researchers' estimate (Claxton et al., via a university release) puts the NHS threshold at £18,317 per QALY, based on 2008 spending.
  - In their modelled hypothetical, ranibizumab for diabetic macular oedema "would have displaced" 4,367 QALYs, or 295 deaths.
  - The release says the threshold NICE uses is probably too high.
  - **Opinion (mine, not stated on the page).** Adopting above the threshold displaces more health than it gains. This frames the cost of adopting as the value of whatever it displaces. It is the clearest quantified argument in the set that declining has a benefit, but it is modelled, not observed.
- **Fact, B (fetch) (F014-26).** Zalando reports tooling, maintenance and duplication costs from broad adoption.

**Cost of declining.**
- **Fact, B (fetch); opinion-laden (F014-35).** In 2004 the W3C "told them that work wasn't welcome" (continuing HTML work), and individuals from Apple, Mozilla and Opera founded WHATWG outside W3C. W3C later "changed its mind" and let XHTML2's charter expire at the end of 2009.
  - *Stake:* the author says "I get paid for it"; no payer is named.
- **Fact, B (fetch, secondary on the official review) (F014-33).** The Cumberlege review found a system that failed to listen to patients and, when it acted, "too often moved glacially".
  - **Opinion (mine).** I read this as a cost of slow retirement. The review itself is about slow action on harm, not about retirement.
  - The report itself was not opened.
- **Gap.** No source quantifies the cost of a rejected proposal. The UK Accelerated Access Review's slow-adoption figures could not be confirmed.

## 5. How adopted practices were reviewed and retired

**Scheduled review with automatic lapse (described, outcome unmeasured).**
- **Fact, B (fetch) (F014-22).** ISO reviews an International Standard every 5 years and a Technical Specification every 3. The page recommends confirming a TS only once.
- **Fact, B (ASME 2016 slide, opened by the Source checker) (F014-23).** An American National Standard under continuous or periodic maintenance that is not revised or reaffirmed within 10 years loses its status. "Stabilized maintenance" takes mature, non-safety standards out of the regular revision cycle, but they still need a status review every 10 years.
  - The current ANSI text was not opened.
- **Fact, library (Q-009-F5-8, weak (C)).** Thoughtworks fades an entry when its opinion has not changed for two successive Radars.
- **Fact, library (Q-005-LF-Q005-15, weak (C)).** Half of 17 AHRQ guidelines were outdated after 5.8 years.

**A review rule that is never applied.**
- **Fact, B (fetch) (F014-24).** The IETF's RFC 2026 procedure for reviewing immature standards "has never been followed". A 2004–05 experiment reviewed about 125 old Proposed Standards, defaulted each to "retire", and proposed dozens for Historic status.
  - The RFC's own counts are inconsistent (61 vs 44).
- **Opinion.** "Retire unless someone speaks up" was used there to clear a backlog.

**In one scheme, provisional adoption with re-appraisal almost always ended in a recommendation.**
- **Fact, B (fetch) (F014-12).** Under the reformed Cancer Drugs Fund, 19 of 20 exits were recommended, yet 12 of 20 (60%) did not fully resolve the original uncertainty.
  - *Stake:* the authors' consultancy serves pharmaceutical clients.
  - **Assumed (search-only):** a 2025 abstract reports 23 of 24 re-appraisals positive.
- **Opinion.** In this one scheme (20 technologies, one consultancy abstract), provisional recommendations mostly became full ones. Whether provisional approvals elsewhere behave the same way is untested.

**Tiered lifetimes by maturity.**
- **Fact, B (fetch; page truncated) (F014-30).** Kubernetes does not remove GA APIs within a major version. Beta APIs are served at least 9 months or 3 releases after deprecation. Alpha APIs can be removed without notice.

**Deprecation without removal loses force.**
- **Fact, assumed (search-only) (F014-31).** In 50 Java APIs across 297,254 projects, consumers mostly did not react to deprecation.
  - The Source checker could not open it (login redirect).
- **Opinion, assumed (search-only) (F014-31).** The authors argue that never removing deprecated features has cheapened deprecation.

**Telling people to stop rarely works alone.**
- **Fact, B (fetch) (F014-17).** A scoping review of 109 papers found active change interventions most likely to produce de-adoption. In one included study (two NICE topics), "do not do" reminders showed no association with practice change. That is not a finding of the review as a whole.
- **Opinion, B (fetch) (F014-17).** The authors argue that without a sustainability plan, clinicians revert.
- **Fact, B (fetch, via news) (F014-18).** Of 7 Choosing Wisely low-value services, 2 declined slightly, 3 stayed flat and 2 rose.
  - *Stake:* the data and lead author are from Anthem, an insurer.

**Open items need their own review.**
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

**Gap.** No study tracks over years whether retired practices come back.

## 6. When, if ever, organisations stopped scanning, and why

**No organisation was found that publicly stopped scanning and gave reasons.**
- **Fact, B (exact) (F014-20).** Australia's medicines industry body stated in 2022 that there was no nationally coordinated horizon-scanning process. The paper does not say one existed earlier or that anything stopped, so it is not evidence of stopping.
  - *Stake:* the industry body wants faster access for its members' products.
  - **Assumed (search-only):** a 2023 government communique says the same.

**Weakening rather than stopping.**
- **Fact, B (fetch) (F014-26).** Zalando's first radar was "easy to ignore due to lack of a formal process" and depended on fading volunteer effort.
- **Fact, assumed (search-only) (F014-21).** Austria's oncology horizon-scanning programme "lacks customers actively requesting assessments". Its effect on practice and costs was not evaluated.
  - The Source checker opened the abstract and did not find either statement in it. This stays unconfirmed.
  - *Stake:* the authors run the programme.
- **Fact, B (exact) (F014-19).** Almost half of EuroScan agencies had fewer than 2 full-time staff.
- **Opinion.** The recorded way scanning weakens is neglect, not a decision to stop. This rests on Zalando's radar, which had no formal process and faded (F014-26), and on thin EuroScan staffing (F014-19) only. F014-21 is unconfirmed and is not relied on. A decision to stop has not been recorded.

**Not found.** Whether AHRQ's horizon scanning or HealthPACT closed, and any company that announced dropping its tech radar.

---

## Thin, absent or from a different field

**Thin or absent:**
- controlled outcomes of scanning;
- comparisons of approval models;
- quantified costs of declining;
- long-term follow-up on retirement;
- any reasoned decision to stop scanning.

**From a different field.** Most of the evidence comes from regulated, high-consequence fields (chemical plants, national health budgets) or from standards bodies with formal membership votes. Several of these are not quite "scanning outside practice":
- MOC is internal change control;
- the Cancer Drugs Fund is a funding route;
- standards review is maintenance.

**How far it transfers (opinion).** Structural lessons may transfer to a small AI-build organisation: time limits, review of open items, records of rejection, the gap between adopting and retiring. Effect sizes do not transfer. The software sources (Zalando, Kubernetes, PEP 1) are closer in kind but are self-descriptions with no outcome data.

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
11. The Nachtnebel et al. 2016 page.
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

- **Patterns that held up elsewhere become candidates.** Described but unmeasured candidates:
  - time limits, close-out and routine review of open or temporary changes (F014-2; two audits' recommendations, F014-7);
  - automatic lapse or default-to-retire (F014-22, -23, -24);
  - tiered stability with stated removal notice (F014-30);
  - named, accountable decision-makers for retirement (F014-26);
  - records of rejected and superseded proposals (F014-25; library F7-6);
  - short and long forms of review (F014-6, posed there only as a question).

  None has outcome evidence, so each would enter as an opinion-grade pattern.
- **Documented harms become things to avoid.** Documented:
  - no change process, or a bypassed one (F014-1, -4, -5);
  - temporary changes (F014-2);
  - heavy uniform process that invites bypassing (F014-6, -8);
  - adoption without an evaluable outcome (F014-9);
  - provisional approval that, in one scheme, was recommended without fully resolving doubt (F014-12);
  - advisory scanning whose advice is watered down (F014-34, commentary only). F014-14 does not show override: in one interviewee's estimate, advice was accepted about half the time by the decision-making body, and government almost always followed the Board;
  - slow action on harm (F014-33);
  - deprecation without removal (F014-31, search-only).
- **Finding no benefit, or a high cost of declining.** No net-benefit evidence was found either way. The cost of declining is documented only anecdotally (F014-35; F014-33 on my reading only). The cost of adopting is quantified only in health (F014-9, and the modelled F014-13). How much this weighs on whether and how to scan is for the owner to judge.
- **Retirement and stopping rules that worked or failed.**
  - *Failed:* passive "do not do" reminders (one included study in F014-17; F014-18) and a review rule never applied (F014-24).
  - *Active de-adoption:* associated with change, in one scoping review (F014-17).
  - *Automatic lapse:* exists, with no outcome measured.
  - *Stopping rules:* none with any record of working or failing were found. F014-20 shows only that no coordinated process existed in 2022. F014-26 shows neglect, not rules; F014-21 is search-only and unconfirmed, so it is not relied on.

---

## Proposed library entries
*(statement | type | grade | proposed shelf life; all grades pending the source check)*

1. Han Siong et al. 2017: across 630 chemical-industry accidents (1990–2015), MOC failure made up 9.1% of cause attributions (149 of 1,633); the authors assert no decrease over the period, without trend figures; they cite Gambetti's 80% as a disagreeing figure | fact | B | 5 years
2. Han Siong et al.: temporary changes were 10.1% of MOC failures, linked to time pressure; Flixborough recommended the same review as for permanent changes | fact | B | 5 years
3. Laughland (ABB, consultancy stake): OSHA refinery inspections 2007–2011, MOC was 9% of citations and 42% of those were for no MOC system (secondary figures) | fact | B | 5 years
4. Laughland: two named audits (a Seveso III refinery, a Middle East chemical plant) recommended formal close-out, time limits on temporary MOCs and a routine review of all open MOCs; these are recommendations, not general findings | opinion | B | 5 years
5. Laughland: MOC seen as bureaucratic risks bypassing; asks whether a short and long form could be used | opinion | B | 5 years
6. NAO 2015: Cancer Drugs Fund cost £968m (Oct 2010 – Mar 2015), overspent, and its effect on outcomes could not be evaluated; the work was not designed to assess value for money (report PDF) | fact | B | 10 years
7. Aggarwal et al., Annals of Oncology 28(8) (abstract opened): of 47 fund indications, 18% met ESMO benefit criteria (9 of 47, which is 19.1%) and 55% (26) had been rejected by NICE; a patient charity disagreed (search-only) | fact | B (abstract only) | 10 years
8. Haycock et al. (ISPOR 2022, pharma-consultancy stake): 19 of 20 Cancer Drugs Fund exits recommended; 60% did not fully resolve the original uncertainty | fact | B | 3 years
9. Claxton et al. (York release): NHS threshold estimated at £18,317 per QALY (2008 spending); in a modelled hypothetical, ranibizumab for DMO would have displaced 4,367 QALYs; the release says the threshold in use is probably too high | estimate | B | 5 years
10. Leggett et al. 2012: barriers to health-technology reassessment; many programmes advisory; one interviewee estimated the decision-making body accepted recommendations about half the time, with government almost always following the Board | fact | B | 5 years
11. Docherty et al. 2011: of 65 "cannot recommend" Cochrane reviews, 43% gave disinvestment candidates; many interventions were already out of use | fact | B | 10 years
12. Niven et al. 2015: active change interventions most likely to produce de-adoption; in one included study, "do not do" reminders not associated with change; the authors argue clinicians revert without a sustainability plan | fact (the reversion point is the authors' argument) | B | 5 years
13. Rosenberg et al. (via AJMC; Anthem stake): of 7 Choosing Wisely services, 2 declined, 3 stayed flat, 2 rose (data to 2013) | fact | B | 5 years
14. Packer et al. 2015 (authors at a member agency): of 15 EuroScan agencies, 5 named removing obsolete technology as a purpose; almost half had under 2 FTE | fact | B | 5 years
15. ISO/TC 211: IS reviewed every 5 years, TS every 3; confirm, revise or withdraw by vote; withdrawal needs a further 8-week ballot | fact | B | 3 years
16. RFC 4450: the RFC 2026 review procedure had never been followed; the 2004–05 experiment defaulted about 125 old standards to "retire" | fact | B | 10 years
17. PEP 1: proposals carry statuses including Rejected, Withdrawn, Deferred and Superseded, and a rejection should be on record; a separate "Rejected Ideas" section records turned-down ideas; final authority with the Steering Council or a delegate | fact | B | 2 years
18. Zalando 2020: the first radar was easy to ignore; broad choice raised costs; gave decision rights to Principal Engineers and accountability for removing failed trials (self-report) | fact | B | 3 years
19. Kubernetes deprecation policy: GA not removed within a major version; beta at least 9 months or 3 releases after deprecation; alpha removable without notice | fact | B | 2 years
20. ICH Q12 concept paper 2014: the envisioned post-approval operational flexibility had not been achieved; lack of harmonised lifecycle approaches can hinder innovation and continual improvement | fact | B | 10 years
21. Medicines Australia 2022: no nationally coordinated horizon-scanning process in Australia (not evidence that one existed or stopped) | fact | B | 2 years
22. Pattern: give every temporary change a time limit, close changes out formally, and review all open items routinely. Origin: two audits' recommendations and Flixborough (items 2, 4). Effect unmeasured | pattern | opinion built on B | 3 years
23. Pattern: pair any "stop doing" ruling with active change work, not a list alone. Origin: items 12 (one included study for the reminders result) and 13 (medicine) | pattern | opinion built on B | 3 years
24. Pattern: in the one scheme studied (the reformed Cancer Drugs Fund), provisional approvals mostly ended recommended; state in advance what evidence would reverse one. Origin: item 8 | pattern | opinion built on B | 3 years

Not proposed: F014-28 (unreliable source); search-only items F014-21 and -31 until opened (-21 was opened at abstract level and not confirmed); F014-23 (a 2016 slide; current ANSI text not opened) and F014-29 (attributed staff opinion, undated page), both now opened by the Source checker but not proposed in this round; F014-11, -16, -27, -33, -34, -35 (attributed opinion or secondary; fileable only as attributed opinion if the checker wishes).

## Finding ids relied on, for the Source checker

- **Input reader:** F014-1 to F014-35. F014-28 is noted but given no weight. The search-only items are F014-21 and -31, plus sub-claims in -10, -12, -14 and -20. F014-23 and F014-29 were opened by the Source checker in round 1.
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

# Change list (this round, answering source-check round 2)

| # | Item | What changed | Correction (round 2) |
|---|---|---|---|
| 1 | Opening bullet 2 | "Tends to become permanent" became "In one scheme … almost always ended in a recommendation". "Approved" became "recommended", and "had not resolved" became "had not fully resolved". I added that this is one scheme of 20 technologies and is untested elsewhere. | 1 |
| 2 | §5 CDF heading and closing line; harms list; pattern 24 | The heading is now scoped to one scheme. "Estimate. Provisional approvals mostly become permanent" became an opinion limited to this scheme (20 technologies, one consultancy abstract), and it says the general case is untested. The harms-list line and pattern 24 are narrowed to the one scheme, to match the library's P24 title. | 1 |
| 3 | §5 F014-17; entry 12 | "Without a sustainability plan, clinicians revert" is moved out of Fact into a separate Opinion, attributed to the authors. Entry 12 now attributes it as the authors' argument. | 2 |
| 4 | §2 F014-6; "what each answer would change" patterns list; entry 5 | "The author suggests short and long forms" became "the author asks whether a short and long form could be used", posed as a question. "Short and long forms of review by risk" became "short and long forms of review (posed there only as a question)". "By risk" is dropped. Entry 5 is reworded to match. | 3 |
| 5 | §4 F014-33; "Finding no benefit" bullet | "This is a cost of slow retirement" is now marked as my opinion, and it notes the review is about slow action on harm. The F014-33 citation as a cost of declining is marked "on my reading only". | 4 |
| 6 | §6 closing opinion; "stopping rules" bullet | "Weak links to the people who decide" is dropped. The opinion now rests on Zalando (F014-26) and EuroScan staffing (F014-19) only, and says F014-21 is not relied on. The stopping-rules bullet no longer cites F014-21 as showing neglect. | 5 |
| 7 | §1 F014-1; entry 1 | "MOC-related accidents did not decrease" moved out of Fact. It is now an opinion: the authors' assertion, with no trend figures. Entry 1 is reworded to match. | optional point 1 |
| 8 | Opening bullet 3 | "Or to temporary changes" became: temporary changes are one share (10.1%), and planned changes are the largest share (45.6%). | optional point 2 |
| 9 | Researcher italic line | Now says the memo is revised after source-check rounds 1 and 2. | consequence |

The rest of the opening answer stands. Nothing else was changed, and no new outside claims were added.

# Finding ids for the Source checker to re-check

F014-1, F014-2, F014-3, F014-6, F014-12, F014-17, F014-19, F014-21, F014-26, F014-33.

Library entries to re-check: Q-014 entries 1, 5, 12 and pattern 24, whose filed versions may now differ from the memo's wording.

# Notes for the Orchestrator

- **Header line.** I left the first italic line, which is yours, verbatim. It still describes round 2 (brief 170), so you may want to update it for this round's brief.
- **Earlier change list.** The previous round's change list, re-check list and notes are replaced by the ones above.

# Tokens

I cannot see my total tokens.
