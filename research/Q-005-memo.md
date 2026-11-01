# Research memo: Q-005. Written procedures that pass work between people: when they help, when they make no difference, when they harm, and how fields add and retire rules (2026-11-01, revision 1)

**Depth:** 3 (graded memo). **Researcher session:** fresh, blind (D-055).

**Question:** research/Q-005.md. It serves the Discovery of P-001. It asks which principles from other fields transfer to the written instructions passed between agents of the operating model, under which conditions, and what limits they set on adding and retiring instructions.

**Revision 1 (2026-11-01).** This revision changes only what research/Q-005-source-check-2.md found:
- the Sumwalt sentence is dropped from F15;
- the F2 and F22 wordings are marked as paraphrase, and F22 now uses IHI's own words;
- the Urbach PMID is corrected to 24620866;
- F5 is resolved, and P-2 and P-8 (with §1, §3.1, LP-02 and LP-07) are revisited against it;
- the "high baseline quality" remark in F3 is reworded as my own inference;
- LP-03 is reworded;
- LP-06 is marked opinion;
- regrades, filing status and the split of LF-Q005-05 and -06 are recorded as the check lists them (§5 and §8).

No new web pages were opened for this revision (L-0005). Nothing else is changed.

---

## 0. How to read this memo

Every statement is marked **Fact**, **Estimate** or **Opinion**.

**Grades for facts:**
- **A.** A primary record I opened in /home/user/Personal-Org-Operating-Model.
- **B.** A publisher's or agency's own page that I opened. *No B items in this memo* (see access limits).
- **C.** The claim appears in search-result extracts from **two or more independent hosts**, for example a journal or index record and an institution's press release or a trade report. I did not open the page myself. The text is untrusted and reported as a claim, with its URLs.
- **D.** The claim appears in one search-result host only, or only on advocacy, blog or study-guide pages.

**Estimates and opinions** carry my confidence: **(H)** high, **(M)** medium, **(L)** low. They are mine, not the sources'.

**Load-bearing facts** are marked ★. Each ★ fact cites two independent hosts. If it cannot, it says so.

**Access limits in this session:**
- `www.nejm.org` and `www.sciencedirect.com` did not resolve when fetched.
- `pmc.ncbi.nlm.nih.gov` and `psnet.ahrq.gov` were blocked, as the brief warned.
- After the second resolution failure, the environment said to stop trying further hosts. I did, so **no web page was opened directly by me**. Every web claim below is drawn from search-result extracts and is graded C or D.
- The second source check opened many of the primary records (§8). Its results are recorded there. It changed no grades, and I do not mark my own facts as checked.

**No model memory is used as a source.** Where I know of evidence but found no source for it this session, I leave it out or list it as a gap.

**The operating model is the subject, not evidence.** Lines quoted from it (grade A) only say what it currently does, so that each transfer check has something concrete to test against.

---

## 1. Short answer

1. **Opinion (M).** Written procedures improved outcomes where three things held:
   - the failures they targeted were common at baseline;
   - the procedure was actually carried out in full;
   - it came inside a wider package: training, team routines, coaching, measurement and peer pressure.

   The same written instrument showed **no effect** in a mandated province-wide rollout (Ontario).
   - Whether high baseline quality is what removes the effect is **not established**. That reading is my own inference. Against it, a controlled study in six hospitals described as having "high standards of care" found a large effect (F5).

   Procedures caused **harm** where the situation differed from the one the authors assumed, so following the text used up the scarce resource, time. The evidence is in §3.1–§3.3.
2. **Opinion (M).** The strongest evidence in every field comes from *before-after* studies.
   - Some better-controlled studies found smaller effects than the first uncontrolled reports: the randomised mortality result (F3) and the English replication (F9).
   - Not all did: SURPASS, with a concurrent control, found a large fall (F5).

   The lesson is that, without a control, you cannot tell which case you are in. A pipeline that can replay the same task under two instruction versions can measure much more cleanly than any of these fields could. This is the clearest transferable *method* lesson (§3.1, §4 P-8).
3. **Opinion (M).** On adding rules: fields that studied their own response to single incidents found the response was usually the **weakest kind of fix**, meaning training, a policy reminder or a process tweak. The same kinds of event then recurred.

   The stronger fixes were those that do not depend on someone remembering a written rule: forcing functions and engineered controls. Aviation filters incident-driven proposals through a second body that weighs cost. Some proposals are rejected there.

   Benefits of single-incident rules are well documented only as individual cases, such as Knight Capital, Swissair 111 and US Airways 1549. **I found no study measuring the net benefit of incident-driven rules as a class.** This is a gap, not a finding of "no benefit" (§3.4).
4. **Opinion (M).** On growth and retirement: rule sets grow, staff cannot follow them all, and warnings and checklists that multiply get overridden. The literature names this "safety clutter" and "checklist fatigue".
   - Fields that retire rules do it by **scheduled review**, for example reassessing clinical guidelines every 3 years.
   - Monitoring and adapting rules, with the people who use them, is central to Hale & Borys's framework.
   - Evidence that **sunset clauses** work is mixed and comes mostly from advocacy organisations (§3.5).
5. **Opinion (M).** Transfer to AI agents is **partial and condition-specific**, worked through in §4:
   - **Do not transfer:** mechanisms based on fatigue, motivation and social pressure.
   - **Transfer in altered form:** mechanisms based on capacity (too many instructions lower compliance) and on fit (a rule written for one situation misfires in another). Their evidence for agents comes from different literature, which Q-001 marked as assumed.
   - **The incident-fix lesson ("prefer a check or a forcing function over another written rule") transfers strongly.** An agent pipeline can build mechanised checks and tool permissions more cheaply than a hospital can build forcing functions.

---

## 2. Fields chosen, and fields left out

**Chosen**, in order of evidence strength for this question:

1. **Surgical and intensive-care checklists.** There is a stepped-wedge randomised trial, several multi-site before-after studies, a controlled multi-site study, a province-wide natural experiment, systematic reviews, and a qualitative study of *why* one programme worked.
2. **Clinical handover between shifts.** There is a nine-site and a 32-site multi-site study of one bundle, plus a systematic review of a second tool.
3. **Aviation checklists and procedures.** There are NASA field studies, accident investigations where a procedure did not fit, and line audits of non-compliance.
4. **Cross-industry rule management.** This covers safety-science reviews, research on corrective actions after root-cause analysis, guideline obsolescence, organisational rule dynamics and sunset clauses. It is the evidence most directly about *adding and retiring* rules.
5. **Military orders, intent versus detail.** I found one quantitative simulation study plus doctrine and theses. The evidence is weak, but it is the only direct evidence on intent-based orders that I found.
6. **Software runbooks and operations.** I found one vendor claim, one industry incident database and one controlled code-review experiment. The evidence is weak.

**Left out or thinly covered**, so the Source checker and Chief of Staff know what was not scanned:

- **Nuclear power operating procedures**, including the move from event-based to symptom-based emergency procedures. This is relevant to the question of rules that fit the situation, but I did not search it this session. *Gap, see new question Q-a.*
- **Pharmaceutical good-manufacturing SOPs and deviation management, maritime and rail, construction method statements.** Not searched. I expect their evidence on outcomes to be weaker than medicine's (**Opinion, L**).
- **Fire-fighting standard orders and wildland-fire intent.** These appear only incidentally in results, under coloradofirecamp.com. Not used.
- **Law and regulation broadly.** Only the sunset-clause evidence was scanned.

---

## 3. Findings

### 3.1 Surgical and ICU checklists: the same text, different results

- **F1 ★ Fact (C).** In the WHO 19-item Surgical Safety Checklist study (Haynes et al., NEJM 2009;360:491-9), eight hospitals in eight cities were measured before and after, with no concurrent control. Inpatient deaths fell from 1.5% to 0.8% and complications from 11% to 7%. The sample was 7,688 patients, 3,733 before and 3,955 after.
  - Sources: https://news.harvard.edu/gazette/story/2009/01/surgical-safety-checklist-drops-deaths-and-complications-by-more-than-one-third/ ; https://www.hsph.harvard.edu/news/press-releases/hospital-sites-demonstrate-surgical-safety-checklist-drops-deaths-and-complications/ (both press releases from the authors' institution, so not fully independent of the authors); https://www.reliasmedia.com/articles/112170-study-safety-checklist-reduces-mortality .
- **F2 ★ Fact (C).** After mandatory adoption in 101 Ontario hospitals (Urbach et al., NEJM 2014;370:1029-38, PMID 24620866, administrative data, before-after), there was no significant change:
  - operative mortality went from 0.71% to 0.65%;
  - complications went from 3.86% to 3.82%;
  - no hospital changed significantly, and no subgroup benefited.

  Leape's editorial argued, *in my paraphrase*, that the checklist was not actually used. These are not his words.
  - Sources: https://www.fiercehealthcare.com/healthcare/surgical-safety-checklists-may-not-improve-patient-outcomes-after-all ; https://mdedge.com/content/surgical-checklists-failed-improve-outcomes ; https://theincidentaleconomist.com/wordpress/?p=54007 .
- **F3 ★ Fact (C).** A stepped-wedge cluster-randomised trial in 2 Norwegian hospitals and 5 surgical specialties (Haugen et al., Ann Surg 2015;261(5):821-8) found:
  - complications fell from 19.9% to 11.5% (P<0.001);
  - length of stay fell by 0.8 days;
  - overall mortality went from 1.6% to 1.0%, which was not significant. One hospital alone fell from 1.9% to 0.2%.

  Commentary raised "checklist fatigue".
  - **Opinion (L), my own inference, not found in any opened source:** checklists may do little where baseline quality is already high. F5 cuts against it.
  - Sources: https://bora.uib.no/handle/1956/8501 ; https://www.uib.no/en/node/79979 ; https://www.patientsafetysolutions.com/docs/May_2015_The_Great_Checklist_Debate.htm .
- **F4 ★ Fact (C).** In a 25,513-patient cohort at one Dutch hospital (van Klei et al., Ann Surg 2012;255(1):44-9):
  - adjusted mortality fell (OR 0.85, 95% CI 0.73-0.98), while crude mortality did not (3.13%→2.85%, P=0.19);
  - **full checklist completion** was associated with OR 0.44 (0.28-0.70);
  - partial completion (OR 1.09) and non-completion (OR 1.16) showed no significant association;
  - the authors wrote that the effect "depended crucially upon checklist compliance".

  This is observational. Sicker emergency patients were less often fully checked, which is a possible confounder.
  - Sources: https://pubmed.ncbi.nlm.nih.gov/22123159/ (index record, from search extract) ; https://beckersasc.com/asc-quality-infection-control/who-surgery-checklist-may-yield-varying-results-depending-on-level-of-compliance.html .
- **F5 Fact (C).** The SURPASS multi-step checklist in six Dutch hospitals (de Vries et al., NEJM 2010;363:1928-37) reduced complications from 27.3 to 16.7 per 100 patients. **Resolved by source check 2** (PubMed 21067384):
  - in-hospital mortality fell from 1.5% to 0.8%, and these are SURPASS's own figures; they coincide with the WHO study's;
  - there was a concurrent control of 5 hospitals, where outcomes did not change;
  - the six intervention hospitals had "high standards of care".
  - Sources: https://hcplive.com/view/more-evidence-supports-the-use-of-surgical-checklists ; https://www.patientsafetysolutions.com/docs/February_2011_SURPASS_Checklist_Reduces_Malpractice_Claims.htm ; PubMed 21067384 (opened by source check 2).
- **F6 Fact (C).** Two later syntheses:
  - A 2016 review of 25 studies (de Jager et al.) judged them too heterogeneous for meta-analysis. It found complications fell in resource-poor settings but the checklist "did not appear to be effective in developed nations".
  - A 2024 quality assessment rated confidence in the pooled checklist meta-analyses "critically low".
  - Sources: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4943979/ ; https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11060208/ (both as search extracts; pmc host blocked). Bergs et al. 2014 meta-analysis (doi:10.1002/bjs.9381): scope confirmed, pooled estimates not retrieved.
- **F7 ★ Fact (C).** In the Michigan Keystone ICU programme (Pronovost et al., NEJM 2006;355:2725-32; 103 ICUs), catheter bloodstream infections fell by up to 66%. The median went from 2.7 per 1,000 catheter-days to 0 at 3 months, and the mean from 7.7 to 1.4 at 16-18 months.

  Pronovost himself said "greater focus on the issue" may have contributed.
  - Sources: https://www.itnonline.com/content/program-cuts-catheter-infections ; https://psnet.ahrq.gov/issue/intervention-decrease-catheter-related-bloodstream-infections-icu (extract only) ; https://scholars.duke.edu/publication/1113942 .
- **F8 ★ Fact (C).** "Explaining Michigan" (Dixon-Woods et al., Milbank Q 2011;89(2):167-205) argues three points:
  - popular accounts perpetuate "the myth" that the results came from "a 'simple checklist' rather than a complex social intervention";
  - the effects worked through pressure to conform, a networked community of practitioners, and other interventions that built a culture;
  - copying only the checklist risks "the cargo cult problem".
  - Sources: https://www.milbank.org/quarterly/articles/explaining-michigan-developing-an-ex-post-theory-of-a-quality-improvement-program/ ; https://www.health.org.uk/journal-articles/explaining-michigan-developing-ex-post-theory-quality-improvement-programme ; https://courses.ucsf.edu/pluginfile.php/174490/mod_resource/content/1/Lyndon%20Explaining%20Michigan%20Dixon-Woods.pdf .
- **F9 ★ Fact (C).** Matching Michigan, a replication in English ICUs (Bion et al., BMJ Qual Saf 2013;22:110-23, stepped and non-randomised), found that adult infection rates fell from 3.7 to 1.48 per 1,000 catheter-days. However, rates fell "just as fast" in ICUs still waiting to join. The authors attributed most of the fall to a wider secular trend.
  - Sources: https://qualitysafety.bmj.com/content/22/2/110 (extract) ; https://www.infectioncontroltoday.com/view/rates-icu-infections-fall-england ; https://eurekalert.org/news-releases/580017 .
- **F10 Fact (D).** Bosk, Dixon-Woods, Goeschel & Pronovost ("Reality check for checklists", Lancet 2009;374:444-5) warned against spreading checklists without understanding how they work. Bosk is reported as saying a checklist "on its own, [does] not much".
  - Sources: https://pgfi.sas.upenn.edu/home/SASFrontiers/bosk.html ; https://www.sciencedaily.com/releases/2009/09/090916092657.htm . These are two hosts, but both are secondary summaries, so I grade this D for the quote.

**Opinions on §3.1:**

- **Opinion (M).** Taken together, F1–F10 show that the *written checklist* is neither sufficient nor reliably effective.
  - Large effects came with uncontrolled designs, low-resource settings, wide social programmes, and in one controlled study (F1, F5, F6, F7, F8).
  - Effects shrank or vanished with mandated rollout (F2), with concurrent comparison in one replication (F9), and with randomisation for mortality (F3).
  - Within-site effects followed actual, full completion (F4).
  - That baseline quality is the moderator is my own inference, and F5 cuts against it.
- **Opinion (M).** The mechanisms named by the field, namely team communication, culture and peer pressure, are *social*. An agent has none of them. That reading is mine, not the sources'.

### 3.2 Clinical handover

- **F11 ★ Fact (C).** I-PASS in nine paediatric residency programmes (Starmer et al., NEJM 2014, before-after) reported:
  - medical errors fell from 24.5 to 18.8 per 100 admissions, a 23% fall;
  - preventable adverse events fell from 4.7 to 3.3, a 30% fall;
  - no added handoff time.

  The bundle was more than a written form. It also included:
  - a mnemonic;
  - a 2-hour workshop and a 1-hour role-play;
  - a computer module;
  - EHR (electronic health record) tools;
  - verbal and written handoff.
  - Sources: https://www.hospimedica.com/critical-care/articles/294755789/improved-patient-handoffs-reduce-hospital-errors.html ; https://intermountainhealthcare.org/news/2014/12/multicenter-patientsafety-study-reduces-medical-error-injuries-by-30 ; https://mdedge.com/content/inpatient-handoff-program-reduced-errors .
- **F12 ★ Fact (C).** A mentored I-PASS implementation in 32 hospitals (Starmer et al., J Hosp Med 2023;18(1):5-14) reported:
  - handoff-related adverse events fell by 47%;
  - the share of verbal handoffs holding all five key elements rose from 20% to 66%;
  - the share of written handoffs holding them rose from 10% to 74%;
  - external coaching over 18 months, with monthly metric reviews.
  - Sources: https://hms.harvard.edu/news/improved-hospital-handoffs-cut-adverse-events-almost-half ; https://hcinnovationgroup.com/clinical-it/patient-safety/news/21286309/study-ipass-handoff-program-helps-reduce-patient-harm ; https://www.ahrq.gov/sites/default/files/2024-01/landrigan-report.pdf .
  - **Fact (C), from the Q-001 map:** the study authors have a stake in the method. Not re-checked this session.
- **F13 Fact (C).** A systematic review of SBAR (Situation, Background, Assessment, Recommendation; Müller et al., BMJ Open 2018;8:e022202) found "moderate evidence" of better patient safety, especially for phone communication. It also found a "lack of high-quality research".
  - Of 26 outcomes, 8 improved significantly, 11 were reported as improved without statistical tests, and 6 did not change.
  - Sources: https://bmjopen.bmj.com/content/8/8/e022202 (extract) ; https://boris.unibe.ch/125569 ; https://read.qxmd.com/doi/10.1136/bmjopen-2018-022202 .
- **F14 Fact (D).** A 2021 review of reviews (Desmedt et al.) found no single handover tool emerges as best for any specialty. The Cochrane nursing-handover review (CD009979) searched only to March 2013.
  - Sources: https://documentserver.uhasselt.be/bitstream/1942/33259/1/Desmedt-2021.pdf ; https://cochranelibrary.com/cdsr/doi/10.1002/14651858.CD009979 .

**Opinions on §3.2:**

- **Opinion (M).** Handover evidence fits the checklist evidence. The structured *form* raised the completeness of what was handed over sharply (F12: from 10% to 74% written), which is the part closest to an agent brief. The outcome effect came as part of a bundle with training and coaching. No study I found separates the written form's own effect from the rest.

### 3.3 Aviation: procedures that did not fit, and procedures not followed

- **F15 ★ Fact (C).** For US Airways 1549 (Hudson River, 2009), the NTSB found the dual-engine-failure procedure had been designed for a failure at cruise altitude above 20,000 ft, where there is time to complete it. At low altitude the first officer completed only a fraction of it before the ditching.
  - The NTSB recommended a low-altitude dual-engine checklist.
  - In 2016, 6 of 35 recommendations were completed. The low-altitude checklist recommendation was marked closed-unacceptable.
  - Sources: https://www.faa.gov/sites/faa.gov/files/2025-04/usairways1549_recommendations.pdf ; https://amp.insurancejournal.com/news/national/2016/09/19/426808.htm ; https://globalnews.ca/news/2941901/miracle-on-the-hudson-only-6-of-35-safety-recommendations-implemented-after-2009-crash/amp/ .
  - *Shelf life is short on the implementation status: no update after 2016 was found.*
- **F16 Fact (C).** For Swissair 111 (1998), the TSB (report A98H0003) found the crew had no procedures or training directing them to aggressively locate and eliminate the source of the smoke.
  - Its recommendation A00-19 asked that smoke/odour checklists be designed for completion in a time that reduces the chance of a fire taking hold.
  - Press coverage reported the crew could have headed straight for Halifax rather than "follow a lengthy checklist".
  - Sources: https://bst.gc.ca/eng/medias-media/fiches-facts/A98H0003/sum_a98h0003.html ; https://tsb-bst.gc.ca/eng/recommandations-recommendations/aviation/2000/rec-a0019.pdf ; https://www.tampabay.com/archive/1999/01/22/before-crash-swissair-pilots-disagreed-over-what-to-do/ . The exact report passage on timing was not retrieved.
- **F17 Fact (C).** NASA's field study of normal checklists (Degani & Wiener, NASA CR-177549, 1990; Human Factors 35(2), 1993) found checklists had "escaped the scrutiny of the human factors profession". It studied function, format, length and use, and ended with design guidelines.
  - A 1969 NTSB recommendation after a no-flap take-off crash called for checklists to be reviewed.
  - Specific quantitative findings were not retrieved.
  - Sources: https://ntrs.nasa.gov/citations/19910017830 ; https://trid.trb.org/View/342238 ; https://ntrs.nasa.gov/citations/19930068509 .
- **F18 Fact (C).** In line operations safety audits (LOSA):
  - 49% of flights in the LOSA Collaborative archive had at least one intentional non-compliance error. The most common were checklists done from memory and omitted callouts.
  - Flights with no intentional non-compliance averaged 2.1 unintentional errors. Flights with one averaged 3.9, and flights with two or more averaged 7.5.
  - A separate analysis of 700 Air Mobility Command observations found 40% of flights with at least one intentional non-compliance error, mostly checklist-related.
  - Sources: https://flightsafety.org/asw-article/intentionally-noncompliant/ ; https://themobilityforum.net/2024/05/30/what-intentional-non-compliance-tells-us-about-system-safety/ . These are different organisations and methods, so do not compare the figures directly.
- **F19 Fact (D).** Dekker (Applied Ergonomics 2003;34:233-8) describes a double bind:
  - operators can fail to adapt a procedure when adapting is needed;
  - or they can attempt adaptations that fail.

  He argues that organisations should study the gap between procedure and practice rather than press harder for compliance.
  - Sources: https://humanfactors.lth.se/fileadmin/lusa/Sidney_Dekker/articles/2003_and_before/DekkerProcedures.pdf (extract) ; https://ferd.ca/notes/paper-failure-to-adapt-or-adaptations-that-fail.html (third-party notes).
- **F20 Fact (D).** "Work-as-imagined versus work-as-done" (Hollnagel and colleagues) names the assumption that work can be completely prescribed, so that the procedure matches practice, and rejects it. The gap becomes "safety drift" when workarounds become normal while procedures stay unchanged.
  - Sources: secondary only: https://www.ecoonline.com/en-nz/blog/hop-safety-in-practice-work-as-imagined-vs-work-as-done/ ; https://www.skybrary.aero/sites/default/files/bookshelf/3934.pdf .

**Opinions on §3.3:**

- **Opinion (H).** F15 and F16 are the clearest documented cases of a written procedure *contributing to harm*. In both, the procedure was built for an assumed situation, and following it consumed time the real situation did not have.
- **Opinion (M).** F18 suggests that in a mature procedural culture, non-compliance travels with other errors. It does not show which causes which.

### 3.4 Rules added after single incidents: what fields found

- **F21 ★ Fact (C).** At a large academic medical centre, 302 root-cause analyses over 8 years were reviewed (Kellogg et al., BMJ Qual Saf 2017;26:381-7). Solutions were proposed in 106 of them, 731 solutions in all. The commonest kinds were:
  - training, 20%;
  - process change, 19.6%;
  - policy reinforcement, 15.2%.

  "Multiple event types were repeated in the study period, despite repeated RCAs." The authors judged most solutions weak.
  - Sources: https://qualitysafety.bmj.com/content/26/5/381 (extract) ; https://researchers.mq.edu.au/en/publications/our-current-approach-to-root-cause-analysis-is-it-contributing-to/ ; https://psnet.ahrq.gov/issue/our-current-approach-root-cause-analysis-it-contributing-our-failure-improve-patient-safety (extract).
- **F22 ★ Fact (C).** The VA's action hierarchy, as adapted by IHI, AHRQ and state health departments, ranks corrective actions in three tiers:
  - **stronger:** forcing functions, engineering controls, standardisation;
  - **intermediate:** checklists, cognitive aids, software changes, staffing;
  - **weaker:** retraining, policy updates.

  In my paraphrase, the stated reason is that stronger actions depend less on people remembering. IHI's own words: stronger actions "require less reliance on humans to remember to perform the task correctly" (IHI RCA2 report, as quoted by source check 2).

  In one study of 20 children's-hospital RCAs, 10.3% of 78 action plans were stronger. A VA study (Hughes 2006) is reported as finding 30% of RCA actions were never implemented.
  - Sources: https://health.state.mn.us/facilities/patientsafety/adverseevents/toolkit/docs/safetytoolkit_actionhierarchy.pdf ; https://www.ahrq.gov/patient-safety/settings/hospital/candor/modules/guide4/aph.html ; https://stg.ihi.org/sites/default/files/SafetyToolkit_ActionHierarchy.pdf .
- **F23 Fact (C).** Peerally, Carr, Waring & Dixon-Woods (BMJ Qual Saf 2017;26:417-22) argue that the name "root cause analysis" wrongly implies one cause or a few. They set out eight problems with RCA in healthcare, including single-point causation, poor analysis quality and weak feedback.
  - Sources: https://eprints.nottingham.ac.uk/37589 ; https://research.birmingham.ac.uk/files/70608217/Peerally_et_al_The_problem_with_BMJ_Qual_Saf_2016.pdf .
- **F24 Fact (C).** Aviation filters rules proposed after incidents through two bodies: the NTSB recommends and the FAA decides.
  - Around 2008 the NTSB chairman reported an acceptance rate of 81.6% across about 4,700 recommendations to the FAA.
  - A 2025 investigative analysis found nearly 25% of recommendations to the FAA since 2000 were closed as unacceptable or superseded. It linked delays to cost and competing priorities.
  - Sources: https://corpora.tika.apache.org/base/docs/govdocs1/320/320039.html ; https://arnoltcenter.org/?p=1621 ; https://www.fox10tv.com/2025/02/24/critical-aviation-safety-improvements-left-limbo-years-over-costs-competing-priorities/ . The two figures use different definitions.
- **F25 Fact (C), an example of a benefit from one incident.** The SEC order on Knight Capital's 2012 failure (Release 34-70694, 2013) found:
  - a technician missed one of eight servers during a deployment;
  - no second technician reviewed the deployment;
  - Knight "had no written procedures that required such a review".

  The order required an independent review of controls and procedures.
  - Sources: https://www.jrvarma.in/blog/Y2013/Knight-Capital.html ; https://www.wilmerhale.com/en/insights/client-alerts/knight-capital-settles-rule-15c3-5-violations-with-sec-agrees-to-pay-12-million ; https://www.sec.gov/news/press-release/2013-222 .

**Opinions and estimates on §3.4:**

- **Opinion (M).** F15, F16 and F25 show that a *single* severe incident can expose a real, general gap: a missing two-person review, or a procedure with no low-altitude variant. A blanket ban on rules from one incident would miss these.
- **Estimate (M).** I found **no study measuring the net effect of incident-driven rules as a class**, weighing benefits against added burden. The evidence on benefits is case by case. The evidence on costs is indirect: weak fixes, recurrence, clutter.

### 3.5 How rules grow, and how they are retired

- **F26 ★ Fact (C).** Carthey et al. (BMJ 2011;343:d5283) counted **192 to 457 policy documents** on each of three London NHS trust intranets. They judged full compliance unrealistic, and noted that outdated versions stay in circulation.
  - Sources: https://psnet.ahrq.gov/issue/breaking-rules-understanding-non-compliance-policies-and-guidelines (extract) ; https://bmjopen.bmj.com/lookup/ijlink/… (BMJ citation link, extract) ; https://qualitysafety.bmj.com/content/19/4/327 (related, extract).
- **F27 ★ Fact (C).** Clinicians override computerised drug-safety alerts in **49% to 96%** of cases (van der Sijs et al., JAMIA 2006;13:138-47, review of 17 papers). A later Dutch study found 91% of alerts overridden. The authors note that many overrides are justified.
  - Sources: https://repub.eur.nl/pub/60465 ; https://www.textbookofdigitalhealth.com/references/h2006overriding.html ; https://psnet.ahrq.gov/issue/overriding-drug-safety-alerts-computerized-physician-order-entry (extract).
- **F28 Fact (C).** "Safety clutter" (Rae, Provan and colleagues, Safety Science 2018) is defined as "the accumulation of safety procedures, documents, roles, and activities that are performed in the name of safety but do not contribute to the safety of operations". The full author list was not confirmed.
  - Sources: https://www.rmit.edu.au/assets/au/en/about/schools-colleges/property-construction/shine/shine-safety-clutter-position-paper-final.pdf ; https://www.worksafe.qld.gov.au/resources/campaigns/safe-work-month-2024-archive/safe-work-month-resources/safe-work-month-and-mental-health-week-2020/safety-clutter-and-what-to-do-about-it-archive .
- **F29 Fact (D).** "Checklist fatigue" is a recognised term. Pronovost is quoted as saying "we do not know how many checklists are too many". I found no study that quantifies the burden as a function of the number of checklists.
  - Sources: https://www.beckershospitalreview.com/quality/patient-safety-outcomes/john-hopkins-study-safety-checklists-important-but-no-magic-wand/ ; https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10941831/ (extract).
- **F30 ★ Fact (C).** Shekelle et al. (JAMA 2001;286:1461-7) studied 17 AHRQ guidelines:
  - half were outdated by **5.8 years** (95% CI 5.0-6.6);
  - 10% were outdated by 3.6 years;
  - the authors recommended reassessing every 3 years.
  - Sources: https://www.rti.org/publication/validity-agency-healthcare-research-and-quality-clinical-practice-guidelines-how-quickly-do ; https://kdigo.org/wp-content/uploads/2017/02/13-Guideline-Revision-or-Not-Criteria-for-Decision-Making-M.-Tonelli.pdf .
- **F31 Fact (C).** Hale & Borys (Safety Science 2013;55:207-21, with a Part 2) review rule management from 1986 onward and contrast two paradigms:
  - top-down rules written by experts and imposed;
  - bottom-up rules that grow from practice.

  Their framework puts *monitoring and adapting rules* at the centre, with rule users involved. The IOSH guidance built on it argues against ever-growing rule sets.
  - Sources: https://vnniosh.vn/?p=18480 ; https://vnniosh.vn/?p=18481 ; https://www.hsmsearch.com/?p=3533 ; https://iosh.com/resources/research-library/safety-rules-and-procedures .
- **F32 Fact (C).** Schulz (ASQ 1998;43(4):845-76) studied rules at a large US research university. The **rate of new rules fell as the number of existing rules grew**, which supports learning theory over "rules breed rules without limit". March, Schulz & Zhou (*The Dynamics of Rules*, Stanford UP 2000) study what prompts rules to be created, changed and suspended. Their specific findings on rule age were not retrieved.
  - Sources: https://katalog.lib.cas.cz/KNAV/EdsRecord/edb,1544734 ; https://ideas.repec.org/a/cup/apsrev/v96y2002i04p827-828_51.html .
- **F33 Fact (D).** The evidence on sunset clauses and rule reviews is mixed:
  - agency sunsets show the most consistent gains;
  - rule-level sunsets have limited evidence;
  - any gain may be a one-off clearing of stock;
  - a Bertelsmann study found termination clauses make no substantial difference.

  Most sources are advocacy organisations.
  - Sources: https://www.archbridgeinstitute.org/the-economic-effects-of-sunset-laws/ ; https://ciceroinstitute.org/blog/new-research-do-sunset-laws-actually-work-the-evidence-is-in/ ; https://bertelsmann-stiftung.de/fileadmin/files/BSt/Presse/imported/downloads/xcms_bst_dms_16216_16217_2.pdf .
- **F34 Fact (D).** Amalberti (Safety Science 2001;37:109-26) is reported to argue that in ultra-safe systems, extending existing measures, including more rules, does little.
  - Source: secondary only, https://toi.brage.unit.no/toi-xmlui/bitstream/11250/2602682/1/Elvik_10.1016_j.ssci.2013.10.024.pdf .

### 3.6 Military orders: intent versus detail

- **F35 Fact (C).** In Shattuck's simulation with four US Army battalions, company commanders' actions matched their battalion commander's intent in **34% of 32 episodes**. This happened despite a prescribed method for stating intent. Shattuck blamed poor written communication and argued for "imparting presence", meaning trust and personal knowledge, beyond the written intent.
  - Sources: https://coloradofirecamp.com/safety-drill/commanders-intent-study.htm ; https://www.canada.ca/en/army/services/canadian-army-journal/articles/2025/short-bursts-rolls-commanders-intent-redux.html ; https://apps.dtic.mil/sti/pdfs/ADA301158.pdf (not opened).
  - Venue: Military Review, March-April 2000, is reported but not confirmed.
- **F36 Fact (D).** I found **no controlled comparison** of intent-based orders against detailed orders. The available work is:
  - a historical comparison of two Afghanistan battles;
  - a staff college thesis finding mission orders "not effective at the tactical level";
  - a dissertation finding advantages mainly in units with high team experience;
  - a 2021 survey of Swedish officers listing obstacles.
  - Sources: https://www.ausa.org/news/study-weighs-mission-command-effectiveness ; https://apps.dtic.mil/sti/pdfs/ADA242667.pdf ; https://stars.library.ucf.edu/etd2023/45 ; https://doaj.org/article/db2b98553a49468ebc212f5c6666d818 .

**Opinion on §3.6:**

- **Opinion (M).** The military evidence does not settle "intent versus procedure". What it does suggest is that written intent alone is often misread, and that intent works best where the parties share experience. Agents in this pipeline share none: every session is fresh.

### 3.7 Software runbooks and operations

- **F37 Fact (C).** Google's SRE book states that recording best practice ahead of time in a "playbook" gives "roughly a 3x improvement in MTTR" (mean time to repair) compared with "winging it". No study behind the figure was found.
  - Sources: https://www.goodreads.com/quotes/10158819-when-humans-are-necessary-we-have-found-that-thinking-through ; https://raw.githack.com/mm-k8s-ug/kubecon-slides/master/slides/2018-kubecon-eu/Stories%20from%20the%20Playbook%20-%20Tina%20Zhang%20&%20Fred%20van%20den%20Driessche,%20Google%20%28Any%20Skill%20Level%29%20-%20Stories%20from%20the%20Playbook.pdf .
- **F38 Fact (C).** Verica's VOID reports cover about 10,000 incidents from about 600 companies. They found no relationship between incident length and severity, and argued that MTTR is an unreliable measure. This weakens any claim measured in MTTR, including F37.
  - Sources: https://www.businesswire.com/news/home/20221213005501/en/Verica-Announces-the-Second-Annual-Verica-Open-Incident-Database-VOID-Report-to-Make-the-Internet-More-Resilient ; https://www.csoonline.com/article/3683508/mttr-not-a-viable-metric-for-complex-software-system-reliability-and-security.html ; https://www.usenix.org/conference/srecon22americas/presentation/nash .
- **F39 Fact (C).** In a controlled experiment with 70 developers (Gonçalves et al., Empir Softw Eng 2022;27:99), mostly novices at code review:
  - a guided checklist helped on a simple review;
  - an ordinary checklist helped on a complex one;
  - the guided version limited the reviewer's own approach on complex tasks;
  - there was no strong link between the amount of guidance and performance.
  - Sources: https://link.springer.com/10.1007/s10664-022-10123-8 ; https://www.zora.uzh.ch/entities/publication/12e91b80-1a51-4659-bfaf-47727928286e ; https://metrics.blogg.gu.se/?p=747 .

---

## 4. Principles, their conditions, and the transfer check against AI agents

**Facts about the subject, for the checks (grade A, opened):**

- **S1.** Every rule is "an experiment with a target, a measure and a kill criterion". A regular review "keeps, changes or retires each rule", and how often is **[open]** (OPERATING_MODEL.md:425-428).
- **S2.** The v2.5.1 generalisation gate is kept (OPERATING_MODEL.md:426). Its steps, as written in docs/archive/OPERATING_MODEL_v2.5.1.md:639-645:
  - classify the failure; an "execution failure" is fixed by making the existing rule checkable, not by adding a rule (:639);
  - apply the rule of two, or give a severity argument; otherwise put the item on a candidate list "with an expiry", where it lapses if it does not recur (:642);
  - use the "smallest layer that fixes it" (:643);
  - have a fresh-context generality review "without reading the incident story first" (:645).

  The stated reason: "a rule written in response to one surprise tends to fit that surprise" (:647).
- **S3.** The v2.5.1 rule-experiment text says to alternate a rule on and off "rather than comparing before and after". A rule that "didn't move its metric while cost rose is removed" (docs/archive/OPERATING_MODEL_v2.5.1.md:633).
- **S4.** Route briefs are one line, with ids only. Changing them is R3 (governance/BRIEFS.toml:1-2, :17-36).
- **S5.** Role-file duties have grown into long paragraphs carrying version-dated exceptions, for example "unless the owner approved it before the project took model 3.4.0" (template-v3/.claude/agents/critic.md:14).

**Conditions in which agents differ from human workers.** All are **Opinion (M)** unless marked. None is evidence that a given principle works for agents.

- **D1.** Agents have no fatigue, motivation, habit or social pressure. Peer culture and "being watched" do not exist for them.
- **D2.** Every session is fresh, with no shared experience between sender and receiver (S-010 header in every agent file, grade A, e.g. critic.md:9).
- **D3.** An agent reads its whole instruction text at the start of every session. "Was the checklist used?" becomes "was the instruction followed?".
- **D4.** **Assumed, from Q-001 A5 and A3; not opened here.** Instruction-following falls as the number of instructions grows, and recall falls as context fills.
- **D5.** Transcripts give a full record of work-as-done. Human fields rarely have this.
- **D6.** Paired replay of the same task under two instruction versions may be possible (Q-001 B4, grade A for the records' existence).
- **D7.** Checks and permissions can be enforced by tools, not text: for example tool lists and surface guards.

| # | Principle (origin) | Conditions it depends on | Transfer check against AI agents | Verdict (Opinion) |
|---|---|---|---|---|
| P-1 | **A written procedure helps only when actually carried out in full** (F4, F2 editorial in paraphrase, F18) | The effect runs through execution. Partial or nominal use gives no benefit. Compliance is observable. | It holds in form: an agent can skip or misread instructions (D4). It differs in cause: there is no motivated non-compliance (D1). Full execution can be *checked* from the transcript (D5). | **Transfers (M).** Measure whether each instruction was followed before judging its effect. |
| P-2 | **Benefit depends on the baseline rate of the targeted failure** (F2, F3). Revised against F5. | The targeted failure must be common. SURPASS (F5) found a large controlled effect in hospitals with "high standards of care" and a baseline of 27.3 complications per 100. So a high *quality label* does not remove the effect. Whether a low *measured rate of the targeted failure* does is untested. That is my own inference (L). F6 is not relied on. | Holds logically for any system, as a reason to measure before adding a rule. Requires knowing the base rate of the failure class in this pipeline, which is not known (Q-001 L1). | **Transfers (M), weakened from H** as a condition. Measure the base rate before adding a rule; do not treat "already good" as a reason to skip measuring. |
| P-3 | **The checklist was a vehicle for a social intervention; copying the text is a "cargo cult"** (F8, F10, F11, F12) | The effect works through culture, team communication, coaching and peer networks. | Those mechanisms are absent (D1, D2). For agents the text plus the checks *is* nearly the whole intervention. The lesson that survives is the inverse: do not assume human-field effect sizes carry over, because their causes were not textual. | **Does not transfer as a mechanism (M).** As a caution, transfer human effect sizes only with care. |
| P-4 | **A procedure designed for an assumed situation misfires, and can harm, when the situation differs** (F15, F16, F19, F20) | The procedure's authors assumed conditions such as altitude, time or fire spread. Following it consumed the scarce resource. | Holds plausibly. An agent follows text literally (D3), and its scarce resources are turns, time and context (Q-001 G4). Rules carrying exceptions dated to old versions (S5) are a sign that rules are bound to a situation. Untested here. | **Transfers (M).** State each rule's intended conditions; prefer short rules that fit the situation. |
| P-5 | **Written intent is often misread; intent works with shared experience** (F35, F36) | Shared training and trust between sender and receiver. | No shared experience (D2). Written intent would then be *more* at risk of misreading, but an agent can be asked cheaply to restate intent before acting, which can be tested. | **Transfers partly (L).** The evidence is one simulation; test it before relying on it. |
| P-6 | **Rule sets accumulate past the point of usability; warnings multiply and get overridden** (F26–F29, F34) | Human attention, memory and fatigue limits; override as a coping behaviour. | Fatigue does not apply (D1). An analogue does: compliance falls with instruction count and context size (D4, assumed). The mechanism differs, so the threshold will differ. | **Transfers in altered form (M).** Set a size or count budget per role file, tested against compliance in this pipeline. |
| P-7 | **Fixes after incidents are mostly weak (training, policy reminders); events recur. Prefer fixes that don't rely on memory** (F21–F23) | Weak fixes depend on people remembering. Stronger fixes engineer the failure out. | "Training" does not exist for agents; "policy" equals instruction text. "Forcing functions" have direct equivalents: tool permissions, mechanised checks, schema validation (D7). The gate already says an execution failure is fixed by making the rule checkable (S2). | **Transfers strongly (H).** Prefer a check or permission over another sentence of instruction. |
| P-8 | **Uncontrolled before-after studies can mislead in either direction; only a concurrent control tells which.** Some controlled designs found smaller effects (F3 mortality, F9). One found a large effect (F5). Revised against F5. | Secular trends, Hawthorne effects and selection. | Holds. Model or version changes act like secular trends (Q-001 C4, F1). Paired replay (D6) and the on/off alternation already written in S3 are the remedy. | **Transfers (H).** The need for a control holds whichever way the controlled result falls. |
| P-9 | **Rules proposed after an incident are filtered by a second body weighing cost** (F24) | A separate body with authority and cost analysis; some proposals rejected. | The pipeline has an analogue: the Critic checks and the owner decides by card (S1), and the generality review reads the proposal without the incident story (S2). Whether the filter rejects anything is not known. | **Transfers (M).** Record the rejection rate as a health measure. |
| P-10 | **One severe incident can expose a real general gap** (F15, F16, F25) | High severity; the gap is general, not specific to the case. | Holds plausibly. The rule of two already allows a severity argument (S2). | **Transfers (M).** Keep the severity route, with the same experiment and kill criterion. |
| P-11 | **Rules go stale on a measurable clock; review on a schedule** (F30, F31) | The underlying knowledge changes. Clinical guidelines: half outdated by 5.8 years. | Agent instructions are tied to model versions, which change much faster than clinical evidence (Q-001 F1, assumed). The clock will be shorter; its length is unknown. | **Transfers (M)** as a principle. The interval must be set from this pipeline's own data. |
| P-12 | **Involve the people who follow the rules in monitoring and revising them** (F31, F19, F20) | Rule users notice misfit and report it. | Agents can be asked to report rules that conflicted or did not fit, but they may comply with their instructions rather than report misfit. Transcripts (D5) give work-as-done directly. | **Transfers partly (L–M).** |
| P-13 | **Sunset clauses retire rules** (F33) | Automatic expiry with review; mixed evidence. | Expiry is cheap to implement for agent instructions. S2 already uses expiry for candidates, not for adopted rules. | **Evidence too weak to rely on (L).** |
| P-14 | **Rule birth rate slows as rules accumulate** (F32) | Organisational learning in one university. | Single setting; unclear analogue. | **Not used (L).** Noted only to temper the "rules always breed rules" claim. |

---

## 5. Proposed library entries

Each entry gives source, grade, shelf life and topics. Every pattern also states its origin, conditions and transfer check. Grades are proposals for the Source checker. **None is self-checked.**

The **Filing** column records source check 2's ruling as it lists it (research/Q-005-source-check-2.md). The check changed no grades.

### Fact entries

| Id (proposed) | Statement | Sources | Grade | Shelf life | Topics | Filing (source check 2) |
|---|---|---|---|---|---|---|
| LF-Q005-01 | The WHO surgical checklist study (8 hospitals, before-after, no concurrent control) reported deaths falling from 1.5% to 0.8% and complications from 11% to 7%. | F1 URLs; NEJM 2009;360:491 | C | 10 years | checklists, procedures | **Hold**: second independent source not opened |
| LF-Q005-02 | Mandatory checklist adoption in 101 Ontario hospitals showed no significant change in adjusted mortality (0.71%→0.65%) or adjusted complications (3.86%→3.82%). | F2 URLs; PMID 24620866 | C | 10 years | checklists, rules | **Fileable** (with "adjusted") |
| LF-Q005-03 | A stepped-wedge randomised trial (2 hospitals) found complications falling from 19.9% to 11.5%; overall mortality (1.6%→1.0%) was not significant. | F3 URLs | C | 10 years | checklists | **Fileable** |
| LF-Q005-04 | In one hospital cohort, the mortality association held for full checklist completion (OR 0.44) but not for partial or no completion. | F4 URLs | C | 10 years | checklists, procedures | **Hold**: one source only |
| LF-Q005-05a | In the English replication of Michigan, the adult ICU infection rate fell from 3.7 to 1.48 per 1,000 catheter-days, equally in units not yet enrolled; the authors attributed this to a secular trend. | F9 URLs | C | 10 years | checklists, process-improvement | **Fileable** (split from LF-Q005-05) |
| LF-Q005-05b | An ex-post study attributed Michigan's ICU infection results to a complex social intervention, not "a simple checklist". | F8 URLs | C | 10 years | checklists, process-improvement | **Hold**: one paper only (split from LF-Q005-05) |
| LF-Q005-06a | I-PASS handover bundle (9 sites) reported a 23% fall in medical errors and a 30% fall in preventable adverse events, with no added handoff time; the bundle included training. | F11 URLs | C | 8 years | handoffs | **Fileable** (split from LF-Q005-06) |
| LF-Q005-06b | Mentored I-PASS implementation (32 hospitals, 18 months of coaching) reported a 47% fall in handoff-related adverse events. | F12 URLs | C | 8 years | handoffs | **Fileable** (split from LF-Q005-06) |
| LF-Q005-06c | In the same 32-hospital study, written handoffs with all key elements rose from 10% to 74%. | F12 URLs | C | 8 years | handoffs | **Hold**: one source only (split from LF-Q005-06) |
| LF-Q005-07 | SBAR: moderate evidence and a lack of high-quality research (systematic review, 2018). | F13 URLs | C | 5 years | handoffs | **Fileable** |
| LF-Q005-08 | US Airways 1549: the NTSB found the dual-engine checklist was designed assuming a dual-engine failure at high altitude (above 20,000 ft), and could not be completed at low altitude. | F15 URLs; NTSB AAR-10/03 | C | 10 years for the finding; 2 years for implementation status | procedures, checklists | **Fileable** (restated as the NTSB finding; no Sumwalt sentence) |
| LF-Q005-09 | Swissair 111: TSB asked that smoke checklists be designed for completion in a time that limits fire development. | F16 URLs | C | 10 years | procedures, checklists | **Hold**: unreachable |
| LF-Q005-10 | LOSA: intentional non-compliance was reported on 49% of archived flights and travelled with more unintentional errors. | F18 URLs | C | 5 years | procedures | **Fileable** |
| LF-Q005-11 | Of 731 solutions from 302 hospital RCAs, the commonest were training (20%), process change (19.6%) and policy reinforcement (15.2%). Event types recurred. | F21 URLs | C | 8 years | rules, process-improvement | **Hold**: one source only |
| LF-Q005-12 | The action hierarchy ranks forcing functions above checklists, and checklists above retraining and policy updates. | F22 URLs | C | 10 years | rules, process-improvement | **Hold**: one source only |
| LF-Q005-13 | Three NHS trusts each held 192–457 policy documents. | F26 URLs | C | 10 years | rules | **Hold**: unreachable |
| LF-Q005-14 | Drug-safety alerts are overridden in 49–96% of cases (review, 2006). | F27 URLs | C | 10 years | rules | **Fileable** (without the 91% figure; second source weak) |
| LF-Q005-15 | Half of 17 AHRQ guidelines were outdated by 5.8 years; reassessment every 3 years was recommended. | F30 URLs | C | 10 years | rules | **Fileable** |
| LF-Q005-16 | In a simulation, company commanders matched battalion intent in 34% of 32 episodes. | F35 URLs | C | 10 years | handoffs, procedures | **Hold**: unreachable |
| LF-Q005-17 | No controlled comparison of intent-based against detailed orders was found (as of 2026-11-01). | F36 URLs | D | 2 years | procedures | **Hold**: absence claim, needs a search record |
| LF-Q005-18 | The "3x MTTR" playbook claim is a practitioner assertion with no study found; MTTR itself is reported to be unreliable. | F37, F38 URLs | C | 3 years | procedures, process-improvement | **Hold**: unreachable |
| LF-Q005-19 | NTSB recommendations to the FAA: about 82% accepted (around 2008); about 25% closed unacceptable or superseded (since 2000, 2025 analysis). | F24 URLs | C | 3 years | rules | **Hold**: unopened |
| LF-Q005-20 | No study measuring the net effect of incident-driven rules as a class was found (as of 2026-11-01). | absence across §3.4 searches | D | 2 years | rules, process-improvement | **Hold**: absence claim, needs a search record |

### Pattern entries (borrowed principles)

**LP-Q005-01: Check execution before judging a rule.** *Filing: hold, because an origin fact (LF-04) is held.*
- **Statement:** a written procedure's effect is conditional on full execution. Measure whether it was followed before judging it.
- **Origin:** surgical checklists (LF-04, LF-02), aviation LOSA (LF-10).
- **Conditions:** execution varies and is observable.
- **Transfer check:** agents can skip instructions through capacity limits (assumed, Q-001 A5), not motivation. Transcripts make execution observable. *Transfers (M).*
- **Grade:** C (sources) / Opinion M (transfer).
- **Shelf life:** 3 years. **Topics:** procedures, checklists.

**LP-Q005-02: Measure the base rate before adding a rule.** *Filing, per the check: its origin facts LF-02 and LF-03 are fileable; drop F6 and check against F5 first. Done in this revision.*
- **Statement:** an added procedure pays off only where the failure it targets is common enough to measure a fall. A high quality *label* is not evidence that the failure is rare: SURPASS (F5) found a large controlled effect in hospitals with "high standards of care".
- **Origin:** checklist results across settings (LF-02, LF-03), tested against F5. F6 dropped.
- **Conditions:** a measurable base rate of the targeted failure.
- **Transfer check:** holds logically. The pipeline's base rates are unknown. *Transfers (M), weakened from H.*
- **Grade:** C / Opinion M.
- **Shelf life:** 5 years. **Topics:** rules, process-improvement.

**LP-Q005-03: Do not assume effect sizes whose mechanism was social carry over.** *Filing: hold (F8 single paper, F10 unopened).*
- **Statement:** do not assume that effects in human fields that ran through culture, coaching or peer pressure carry over to agents.
- **Origin:** Explaining Michigan (LF-05b), I-PASS bundles (LF-06a, LF-06b).
- **Conditions:** a social mechanism.
- **Transfer check:** agents lack it (no fatigue, no peers, fresh sessions). *The mechanism does not transfer; the caution does (M).*
- **Grade:** C / Opinion M.
- **Shelf life:** 3 years. **Topics:** checklists, handoffs.

**LP-Q005-04: State the conditions a rule assumes.** *Filing: hold (F16 unreachable, F19 unopened).*
- **Statement:** write down the situation each rule is designed for. A rule followed outside its designed situation can consume the scarce resource and do harm.
- **Origin:** NTSB 1549, TSB Swissair 111 (LF-08, LF-09); Dekker (F19).
- **Conditions:** the situation varies, and the procedure costs time.
- **Transfer check:** agents follow text literally, and their scarce resource is turns, time and context. Exceptions dated to old versions in role files (critic.md:14, grade A) are a sign of rules bound to a situation. *Transfers (M), untested here.*
- **Grade:** C / Opinion M.
- **Shelf life:** 3 years. **Topics:** procedures, rules.

**LP-Q005-05: Prefer a check or permission over another written rule.** *Filing: hold (LF-11, LF-12 single source).*
- **Statement:** weak fixes depend on memory and fail to stop recurrence. Prefer a mechanised check or tool permission to another instruction sentence.
- **Origin:** RCA corrective-action research and the VA action hierarchy (LF-11, LF-12).
- **Conditions:** a stronger, engineered option exists.
- **Transfer check:** agent pipelines have cheap engineered options (tool lists, guards, schema checks). The subject's gate already says this for execution failures (OPERATING_MODEL_v2.5.1.md:639, grade A). *Transfers strongly (H).*
- **Grade:** C / Opinion H.
- **Shelf life:** 5 years. **Topics:** rules, process-improvement.

**LP-Q005-06: Give each role file a size budget.** *This is an opinion, not a fact. Filing: hold (LF-13 unreachable; F28, F29 unopened).*
- **Statement (Opinion, M):** rule and warning sets accumulate past usability. Set an explicit budget, and retire a rule when adding one.
- **Origin:** NHS policy counts, alert override, safety clutter, checklist fatigue (LF-13, LF-14; F28, F29).
- **Conditions:** a limit on attention.
- **Transfer check:** human fatigue does not apply. Agent compliance and recall limits (Q-001 A3, A5, assumed) are the analogue, with an unknown threshold. *Transfers in altered form (M).* The budget must be set from this pipeline's data.
- **Grade:** C (origin facts) / Opinion M.
- **Shelf life:** 2 years. **Topics:** rules, procedures.

**LP-Q005-07: Use concurrent controls, not before-after comparisons.** *Filing: hold (LF-01 held).*
- **Statement:** uncontrolled before-after comparisons can over- or understate procedure effects. Use concurrent controls, randomised or paired. In this literature some controlled studies found smaller effects (LF-03 mortality, LF-05a) and one found a large effect (F5). Only a control tells which.
- **Origin:** checklist literature (LF-01, LF-02, LF-03, LF-05a, F5).
- **Conditions:** secular trends and confounding.
- **Transfer check:** model and version changes act like secular trends. Paired replay (Q-001 B4) and the on/off alternation (OPERATING_MODEL_v2.5.1.md:633, grade A) apply. *Transfers (H).*
- **Grade:** C / Opinion H.
- **Shelf life:** 5 years. **Topics:** process-improvement.

**LP-Q005-08: Keep a severity route through a separate filter.** *Filing: hold (LF-19 unopened).*
- **Statement:** a single severe incident may justify a rule, provided it passes a separate filter that weighs cost and can reject it.
- **Origin:** NTSB/FAA (LF-19), Knight Capital (F25), Hudson (LF-08).
- **Conditions:** the filter is independent and has power to reject.
- **Transfer check:** the pipeline's Critic plus owner card, and the generality review that reads without the incident story (v2.5.1:645, grade A), are analogues. The rejection rate is unknown. *Transfers (M).*
- **Grade:** C / Opinion M.
- **Shelf life:** 3 years. **Topics:** rules.

**LP-Q005-09: Review rules on a schedule set from data.** *Filing: fileable on LF-15 only; F31 is unopened.*
- **Statement:** rules go stale on a measurable clock. Review them on a schedule set from data.
- **Origin:** clinical guidelines (LF-15); Hale & Borys (F31).
- **Conditions:** the underlying knowledge changes over time.
- **Transfer check:** model versions change faster than clinical evidence, so the interval is likely shorter. Its length is unknown. *Transfers (M).*
- **Grade:** C / Opinion M.
- **Shelf life:** 3 years. **Topics:** rules.

**LP-Q005-10: Test that written intent was understood.** *Filing: hold (LF-16 unreachable).*
- **Statement:** written intent is often misread. Test understanding, for example by having the receiver restate the intent, rather than assuming it.
- **Origin:** military intent simulation (LF-16).
- **Conditions:** no shared experience.
- **Transfer check:** agents share none (fresh sessions), and a restatement check is cheap. The evidence is one study. *Transfers partly (L).*
- **Grade:** C / Opinion L.
- **Shelf life:** 3 years. **Topics:** handoffs.

---

## 6. Questions added (none closed)

- **Q-a.** What did nuclear power find when it moved from event-based to symptom-based emergency procedures, and what evidence is there on outcomes? *Decision:* whether "rules that fit the situation" have a stronger evidence base than §3.3. *Depth:* 3.
- **Q-b.** In this pipeline, how does compliance with role-file instructions change with the number and length of instructions, measured by paired replay? *Decision:* the size budget in LP-06. *Depth:* 3, with experiment.
- **Q-c.** Of past changes to role files and briefs in this repository, how many followed one incident, how many passed the rule of two or a severity argument, and how many were later retired? *Decision:* whether the existing gate is used, and whether its filter ever rejects anything (LP-08). *Depth:* 3.
- **Q-d.** Is there any controlled study, in any field, of the *net* effect of rules added after single incidents, weighing benefit against added burden? *Decision:* LF-20 is an absence of evidence. *Depth:* 3.
- **Q-e.** Do agents report rules that misfit when asked to, or do they comply silently? *Decision:* whether P-12 can work through agent reports or only through transcript review. *Depth:* 3.

---

## 7. Gaps, and what the Source checker needs

1. **No page was opened directly by me** (§0). Every web item is C or D. Source check 2 opened many primary records (§8), but held several ★ items for lack of a second independent opened source.
2. **Specific values not confirmed:**
   - the Shattuck venue (F35);
   - the full Rae et al. author list (F28);
   - Bergs 2014 pooled estimates (F6).

   The SURPASS question (F5) is resolved by source check 2.
3. **Agent-side conditions D4 and D6** rest on the Q-001 map's *assumed* items (IFScale, context-recall guidance, replay records). Transfer verdicts that use them are only as strong as those items.
4. **The pipeline's own evidence** (Q-001 L1, rounds, first-pass rates) was not used. It is outside this question's scope, and §4 judges transfer only, not effect.
5. **The two absence claims** (LF-17, LF-20) need a search record before they can be filed.

---

## 8. Source check 2: results as recorded

Taken from research/Q-005-source-check-2.md. **Regrades: none.** The check upgraded no grade, so every grade above stands as proposed. I do not mark my own facts as checked.

**Per item:**
- **Supported, two independent opened sources:** F2 (figures), F3, F9, F11, F15 (NTSB finding and AP status; the Sumwalt sentence was *not* supported and is dropped), F27, F30.
- **Supported, one opened source only:**
  - F1, F4, F7, F8, F21;
  - F22, partly: the tier contents differ in detail, and the quote was not verbatim, now fixed;
  - F12: the 47% figure has two sources, but the 20%→66% and 10%→74% figures have one.
- **Supported, not ★:** F5 (resolved: own figures, 5-hospital concurrent control, "high standards of care"), F13, F17, F18, F25.
- **Corrections recorded:**
  - the Urbach PMID is 24620866;
  - the F2 Leape wording and the F22 wording are paraphrase;
  - the F3 "high baseline quality" remark is my own inference;
  - the F2 clause "no hospital changed significantly" and the F4 confounder remark were not found in what the check opened. The confounder remark is mine.
- **Unreachable or unopened:** F6, F10, F14, F16, F19, F20, F23, F24, F26, F28, F29, F31–F39.

**Filing status:**
- **Fileable:** LF-Q005-02 (with "adjusted"), -03, -05a, -06a, -06b, -07, -08 (as the NTSB finding), -10, -14 (without 91%), -15; LP-Q005-02 (after the F5 revision above) and LP-Q005-09 (on LF-15 only).
- **Held:** LF-Q005-01, -04, -05b, -06c, -09, -11, -12, -13, -16, -17, -18, -19, -20; LP-Q005-01, -03, -04, -05, -06, -07, -08, -10.
- **Splits:**
  - LF-Q005-05 becomes 05a (English replication, fileable) and 05b (Explaining Michigan, held);
  - LF-Q005-06 becomes 06a (9-site, fileable), 06b (47%, fileable) and 06c (written handoff 10%→74%, held).

---

**Sources opened in the repository (grade A):**
- /home/user/Model-Lab/research/Q-005.md
- /home/user/Model-Lab/research/Q-001-memo.md
- /home/user/Personal-Org-Operating-Model/OPERATING_MODEL.md (§10, :415-429)
- /home/user/Personal-Org-Operating-Model/docs/archive/OPERATING_MODEL_v2.5.1.md (:633-647)
- /home/user/Personal-Org-Operating-Model/template-v3/governance/BRIEFS.toml
- /home/user/Personal-Org-Operating-Model/template-v3/.claude/agents/critic.md
- /home/user/ml-lessons/research/Q-005-source-check-2.md (for revision 1)

**Web sources:** all are cited inline above. They were seen only as search-result extracts on 2026-11-01, not opened by me. No new web pages were opened for revision 1.
