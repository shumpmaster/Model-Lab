Verdict: FAIL

Reason: of the 15 ★ items, 11 are supported with at least one opened primary record. Only F2, F3, F9, F11, F15, F27 and F30 have a second opened source I count as independent. F12 has one only for its 47% figure, F26 could not be opened, and F1, F4, F7, F8, F21 and F22 have only one opened source. Nothing in the proposed entries was found to contradict a source. But one sentence in F15 (Sumwalt) is not in the NTSB report, and two memo quotes are not verbatim (F2 Leape, F22). I upgraded no grades and wrote no repo files; scratch files are in my scratchpad only.

How I read it: the memo and the earlier check were not in the working tree when I started. I read them from git (`orch/p001-research-questions`, commits f37a8ff and be6ac3e) before your note arrived. I did not open /home/user/portfolio, decisions, questions or docs.

How I opened sources: WebFetch still fails with ENOTFOUND for every host. Plain `curl` from Bash through the proxy, with normal TLS checks, worked for:
- pubmed.ncbi.nlm.nih.gov
- pmc.ncbi.nlm.nih.gov
- Europe PMC
- ntsb.gov
- ihi.org
- psnet.ahrq.gov
- flightsafety.org
- ntrs.nasa.gov
- several news and repository hosts

These returned 403 or an error, and I did not work around them:
- nejm.org
- bmj.com
- qualitysafety.bmj.com
- sec.gov
- bst.gc.ca and tsb-bst.gc.ca
- apps.dtic.mil
- ahrq.gov
- reliasmedia.com
- beckersasc.com
- uib.no
- eurekalert.org
- springer.com (429)
- canada.ca (stream error)
- health.state.mn.us (expired certificate)

One request I sent with a browser-style User-Agent was denied by the permission system. I did not retry it.

Two corrections to the earlier check and the memo:
- The earlier check gave PMID 24694806 for Urbach. That PMID is an unrelated Japanese review. Urbach, NEJM 2014 is PMID 24620866.
- The memo's doubt about F5 is resolved (see the F5 row).

| Item | Claim | Source opened | Result | Note |
|---|---|---|---|---|
| F1 ★ | WHO checklist: 8 hospitals, 3,733 before and 3,955 after, deaths 1.5% to 0.8%, complications 11% to 7% | PubMed 19144931 (NEJM abstract) | Supports | Abstract gives 1.5% to 0.8% (P=0.003) and 11.0% to 7.0% (P<0.001). "No concurrent control" is true of the design and is not stated in the abstract. The Harvard releases are the authors' institution and I did not open them. reliasmedia returned 403. Only one independent source opened. |
| F2 ★ | Ontario, 101 hospitals: mortality 0.71% to 0.65%, complications 3.86% to 3.82%, not significant | PubMed 24620866; mdedge.com/content/surgical-checklists-failed-improve-outcomes; theincidentaleconomist.com ?p=54007 | Supports (figures) | Abstract: adjusted 0.71 to 0.65 (OR 0.91, P=0.13) and 3.86 to 3.82 (OR 0.97, P=0.29). mdedge confirms the figures and "no subgroup benefited". "No hospital changed significantly" is not in anything I opened. Leape's editorial says the benefit comes from performing the actions, and the blog adds that surgeons "rolled their eyes". The memo's quoted words "was not actually used" appear nowhere I opened, so treat them as a paraphrase. |
| F3 ★ | Norway stepped-wedge trial: complications 19.9% to 11.5%; length of stay down 0.8 days; mortality 1.6% to 1.0% not significant; one hospital 1.9% to 0.2% | Europe PMC record of PMID 24824415 (full abstract); patientsafetysolutions.com May 2015 page | Supports | All figures match: 2,212 control vs 2,263 checklist procedures; length-of-stay 95% CI 0.11 to 1.43. The secondary page repeats the 19.9% to 11.5% and 1.6% to 1.0% figures and discusses "checklist fatigue" (Stock and Sundt). The memo's remark that checklists may do little where baseline quality is high is not in what I opened. |
| F4 ★ | Dutch cohort of 25,513: adjusted OR 0.85; full completion OR 0.44; partial 1.09; none 1.16; "depended crucially upon checklist compliance" | PubMed 22123159 | Supports | Every figure and the quote match. beckersasc returned 403, so only one source is opened. The abstract does not mention sicker emergency patients being checked less often, so that confounder remark is the memo's own. |
| F5 | SURPASS: complications 27.3 to 16.7 per 100; mortality 1.5% to 0.8% | PubMed 21067384 (NEJM 2010) | Supports | The mortality figures are genuinely the SURPASS ones (1.5% to 0.8%, absolute risk reduction 0.7). They coincide with the WHO study's figures. There was a control arm of 5 hospitals, and outcomes did not change there. The checklist was tested in six hospitals "with high standards of care". This cuts against P-2 and P-8 (see the transfer checks). |
| F6 | De Jager 2016 review of 25 studies; 2024 critically-low confidence assessment | none | Unreachable | Not tried beyond the PMC list. |
| F7 ★ | Keystone: 103 ICUs; median 2.7 to 0 at 3 months; mean 7.7 to 1.4 at 16 to 18 months; up to 66% | PubMed 17192537; scholars.duke.edu/publication/1113942; itnonline.com | Supports | PubMed abstract matches. Duke repeats the same abstract, so it is not independent. The ITN article is independent but confirms only a median of zero, not the other figures. Pronovost's "greater focus on the issue" quote is not in what I opened. |
| F8 ★ | Dixon-Woods, Milbank Q 2011: the "simple checklist" myth, social intervention, "cargo cult problem" | PMC3142336 full text (via pmc.ncbi); PubMed 21676020; milbank.org page (abstract only) | Supports | Verbatim: "perpetuated the myth that the program's achievements can be traced to a 'simple checklist' rather than a complex social intervention", and "cargo cult problem". The abstract lists isomorphic pressures, a networked community with normative pressures, and culture-shaping interventions. All of this is one paper in three renderings, so there is no independent second source. |
| F9 ★ | Matching Michigan: adult rate 3.7 to 1.48 per 1,000 catheter-days; falls in not-yet-enrolled ICUs; secular trend | PubMed 22996571; PMC3585494 full text; infectioncontroltoday.com; PubMed 23786847 | Supports | The paper states 3.7 to 1.48, "did not accelerate following interventions training", and "likely part of a wider secular trend". Infection Control Today has the "just as fast in ICUs waiting to join" wording, which is a press paraphrase, not the paper's words. Dixon-Woods's separate ethnography (PubMed 23786847) names the "failure to outperform the secular trend". Two independent sources. |
| F10 | Bosk et al. Lancet 2009 | none | Unreachable | Graded D by the memo. |
| F11 ★ | I-PASS, 9 sites: errors 24.5 to 18.8 per 100, preventable adverse events 4.7 to 3.3, no added handoff time | PubMed 25372088 (NEJM 2014); mdedge.com/content/inpatient-handoff-program-reduced-errors | Supports | Figures match, 10,740 admissions. Oral handoff duration 2.4 vs 2.5 minutes, P=0.55. The abstract lists a mnemonic, training, faculty development and a sustainability campaign. mdedge adds the 2-hour workshop, 1-hour role-play, computer module and direct-observation tools. Two sources. |
| F12 ★ | I-PASS, 32 hospitals: events down 47%; verbal elements 20% to 66%; written 10% to 74%; 18 months of coaching | PubMed 36326255 and PMC10964397 (JHM 2023); hcinnovationgroup.com | Supports | Paper: major events 1.7 to 0.9 per person-year, minor 17.5 to 9.3, a 47% fall. Verbal 20% to 66% (n=4,812), written 10% to 74% (n=1,787). The news article confirms only 47%. The 20/66 and 10/74 figures rest on the paper alone. The HMS page returned an empty response. The authors have a stake in the method (a Q-001 point), which I did not re-check. |
| F13 | SBAR review: "moderate evidence"; 26 outcomes, 8 significant, 11 improved without tests, 6 unchanged | PubMed 30139905 (BMJ Open 2018) | Supports | Matches exactly, including "lack of high-quality research". |
| F15 ★ | US Airways 1549: procedure designed for failure above 20,000 ft; low-altitude checklist recommended; Sumwalt suggested a remembered procedure; 6 of 35 done by 2016 | NTSB AAR-10/03 full report (ntsb.gov); insurancejournal.com AP story (2016) | Partly supports | NTSB: the checklist was "designed assuming that a dual-engine failure occurred at a high altitude (above 20,000 feet)". The crew finished "most of part 1" and could not start parts 2 and 3. Recommendation A-10-66 asks for a low-altitude checklist. The AP story says "only six" of 35 recommendations were heeded and that the low-altitude checklist recommendation is "closed-unacceptable". The Sumwalt claim is NOT supported: in the report he is "Member", and his concurrence supports the staff report and says nothing about a single remembered procedure. I also did not find it in the AP story. The faa.gov PDF is only an excerpt of the NTSB recommendations section and has no status information. The AP story is carried twice (insurancejournal and globalnews), which counts as one source. |
| F16 | Swissair 111: TSB found no procedures for smoke source; recommendation A00-19 | none | Unreachable | bst.gc.ca and tsb-bst.gc.ca returned 403. |
| F17 | NASA CR-177549: checklists "escaped the scrutiny of the human factors profession" | ntrs.nasa.gov/citations/19910017830 | Supports | The abstract has the exact phrase and the "improper use, or the non-use" line. |
| F18 | LOSA: 49% of flights with intentional non-compliance; 2.1, 3.9 and 7.5 unintentional errors | flightsafety.org/asw-article/intentionally-noncompliant/ | Supports | All four figures match. This is a Flight Safety Foundation article reporting Klinect's presentation, not the LOSA data itself. The Air Mobility Command 40% figure is unchecked. |
| F21 ★ | 302 RCAs, 106 with solutions, 731 solutions; training 20%, process change 19.6%, policy reinforcement 15.2%; event types repeated | PubMed 27940638; researchers.mq.edu.au; psnet.ahrq.gov page | Supports | The abstract matches and the authors conclude the commonest solutions were weaker actions. The Macquarie record is a repository copy. The PSNet page is a summary without the numbers. So there is no independent second source with the figures. |
| F22 ★ | VA action hierarchy, as adapted by IHI/AHRQ/state health departments, with three tiers and the stated reason; 10.3% of 78 action plans stronger; Hughes 2006 found 30% never implemented | IHI RCA2 report (ihi.org PDF, Figure 3); IHI Action Hierarchy toolkit PDF | Partly supports | Tiers as in the memo, with two differences. Stronger: forcing functions, simplify, standardise on equipment or process. Intermediate: checklists and cognitive aids, software enhancements, standardised communication tools, redundancy, staffing. Weaker: new procedure or policy, training, warnings, double checks. The memo's quoted "rely less on people's actions and memories" is not verbatim. IHI says stronger actions "require less reliance on humans to remember to perform the task correctly". The 10.3% and Hughes 30% figures are unreachable. The AHRQ copy returned 403, the Minnesota copy has an expired certificate, and the VA copy 404ed. This is one source. |
| F23 | Peerally et al., eight problems with RCA | PubMed 27340202 | Unreachable | The PubMed record has no abstract. |
| F25 | Knight Capital SEC order: no second technician; "no written procedures that required such a review" | wilmerhale.com client alert; jrvarma.in blog | Supports | Both quote SEC order paragraph 15. The sec.gov primary returned 403. The memo does not mark F25 ★. |
| F26 ★ | Carthey et al. BMJ 2011: 192 to 457 policy documents per trust | PubMed 21914756 (no abstract); psnet.ahrq.gov | Unreachable | bmj.com returned 403. The PSNet summary says only that the paper recommends a human factors approach. The numbers appear nowhere I could open. |
| F27 ★ | Drug alerts overridden in 49% to 96% of cases (17 papers) | PubMed 16357358 (JAMIA 2006); repub.eur.nl/pub/60465; textbookofdigitalhealth.com | Supports | The abstract states 49% to 96% and says overriding may often be justified. The repository page is a copy of the abstract. The textbook page is a third-party restatement and is weak. The "91% in a later Dutch study" is unverified. |
| F30 ★ | Shekelle JAMA 2001: 17 guidelines; half outdated at 5.8 years (CI 5.0 to 6.6); 10% at 3.6 years; reassess every 3 years | PubMed 11572738; rti.org page; Tonelli slide deck (kdigo.org) | Supports | The abstract has all figures and "reassessed for validity every 3 years". The 3.6-year CI is 2.6 to 4.6. The slide deck independently lists "Shekelle JAMA 2001 ... 5.8 (5.0, 6.6)". The memo's 17 guidelines is correct; the "more than three quarters need updating" line is also in the abstract. |
| F28 | Safety clutter definition | none read | Unreachable | I downloaded the RMIT PDF but did not read it. |
| F35 | Shattuck: 34% of 32 episodes | none | Unreachable | DTIC returned 403 and canada.ca failed. |
| F37, F38 | "3x MTTR" playbook claim; VOID reports | sre.google/sre-book/being-on-call/; csoonline.com | Unreachable | The SRE page I opened has no "MTTR" or "3x". The CSO article is a different page from the one the memo cites for those numbers. |
| F39 | Code-review checklist experiment | none | Unreachable | Springer returned 429. |
| F14, F19, F20, F24, F29, F31–F34, F36 | as stated in the memo | none | Unreachable | I did not get to these. F24 has no figures in what I read from fox10tv. All were graded D or not ★ except F24, which is graded C. |

**Transfer checks and their dependence on failed items**

- **P-1:** F4 is supported but single-source. The F2 Leape support is a paraphrase, not a quote. F18 is fine. P-1 stands, resting on F4 and F18 and on the unopened D4.
- **P-2 (baseline matters):** this is weakened. F5 (SURPASS) found a large drop against a concurrent control in six hospitals described as having "high standards of care". The memo's remark about high baseline quality and checklists is not in anything I opened. F6 is unopened. P-2 should not rest on F2, F3 and F6 alone.
- **P-3:** F8 is verified verbatim. F10 is unopened. The F12 effect size rests on one paper.
- **P-4:** F15 supports the design assumption. F16 is unreachable, F19 and F20 unopened. LP-04's "harm" claim for Swissair rests on an unopened source.
- **P-6:** F26 is unreachable, so the 192 to 457 figure has no support. F27 is supported. F28, F29 and F34 are unopened.
- **P-7:** F21 and F22 are each supported by one source only. The 10.3% and Hughes 30% claims are unreachable.
- **P-8:** F1, F2, F3 and F9 are all supported. SURPASS (F5) is a controlled design with a large effect, which complicates the memo's blanket "concurrent controls shrink effects".
- **P-11:** F30 is supported.
- **P-5, P-9, P-12, P-13, P-14:** F35, F24, F31 to F34 are unopened, so I cannot confirm these.

**Library entries: may it be filed?**

Rule used: a load-bearing (★) fact needs two independent sources I opened. A third-party restatement of the paper's figures counts. A repository copy of the same abstract, or the authors' own institution, does not. Grades are the memo's, unchanged.

Fileable now:
- LF-Q005-02 (Ontario, F2). Say "adjusted" in the statement.
- LF-Q005-03 (Norway trial, F3).
- LF-Q005-07 (SBAR, F13). Not ★, one primary opened.
- LF-Q005-08 (US Airways 1549, F15). Restate it as the NTSB finding. Do not file the Sumwalt sentence.
- LF-Q005-10 (LOSA, F18). Not ★, one source opened.
- LF-Q005-14 (alert override, F27). The second source is weak (a restatement); drop the 91% figure.
- LF-Q005-15 (guideline obsolescence, F30).

Fileable only if restated:
- LF-Q005-05 (Michigan and Matching Michigan). Split it. The English replication half (F9) is fileable. The Explaining Michigan half (F8) has only one paper, so hold it.
- LF-Q005-06 (I-PASS). File the 9-site (F11) and the 47% (F12) clauses. The written handoff 10% to 74% clause is one source, so hold it.

Hold (do not file):
- LF-Q005-01 (F1): the second independent source was not opened.
- LF-Q005-04 (F4): one source only.
- LF-Q005-09 (F16): unreachable.
- LF-Q005-11 (F21): one source only.
- LF-Q005-12 (F22): one source only.
- LF-Q005-13 (F26): unreachable.
- LF-Q005-16 (F35), LF-Q005-18 (F37, F38), LF-Q005-19 (F24): unreachable or unopened.
- LF-Q005-17 and LF-Q005-20: absence claims, and I made no search record. They need one.

Patterns:
- LP-Q005-02: its origin facts LF-02 and LF-03 are fileable. Drop F6 and check it against the F5 counter-evidence first.
- LP-Q005-09: fileable on LF-15 only. Hale and Borys (F31) is unopened.
- LP-Q005-01, 03, 04, 05, 06, 07, 08, 10: hold, because at least one origin fact is held or unopened.

Files read: /home/user/Model-Lab/research/Q-005.md and the memo and earlier check from git (`orch/p001-research-questions`, commits f37a8ff and be6ac3e).
