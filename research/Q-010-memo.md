# Q-010 memo: methods for predicting whether a practice transfers to a new setting, and how well they have predicted (Researcher, 2026-11-08, revised after source check round 1)

*The Researcher's memo for Q-010, round 2 (brief 168, docs/briefs/168-researcher.md), revised after the Source checker's round 1 (research/Q-010-source-check.md); round 1 was brief 158, in this file's history. Recorded verbatim by the Orchestrator (session_01QBwHGNSLmSrYQgS6BPjV8p), 2026-11-08, from the helper's return; only this italic line is the Orchestrator's, replacing round 1's.*

**Short answer.** Methods for judging whether a finding will hold elsewhere fall into five families:
- naive extrapolation from similar studies;
- statistical adjustment (reweighting on covariates, bounding, hierarchical pooling);
- formal causal-graph transportability;
- conditions checklists and theory-based methods (Cartwright and Hardie's support factors, realist context-mechanism-outcome, PIET-T, CFIR, DORA's AI Capabilities Model);
- forecasting (prediction markets, expert crowds, machine-learning models, LLMs).

Only the first two families and forecasting have been scored against what then happened, and almost all of those tests come from economics, education, psychology and social science, not from building software with AI. Each claim below rests on a single source; none has the two sources a load-bearing fact needs. In those tests:
- Naive extrapolation predicted poorly. The first 10 Opower sites overstated the effect at the next 101 (one source, analysed after the fact). One similar study got another's sign right only 61% of the time (one secondary page paraphrasing Vivalt; weak, C).
- Covariate adjustment was mixed and often poor. Low bias held only on one benchmark, and in one set of simulations no method performed reliably. Where the programme itself differed between sites, adjustment removed most of the differences between control groups but trainee outcomes still did not match; the authors surmise the programme differences are the cause. Adjustment did better when it used place-level traits, and in one microcredit pooling and one bounding test.
- Forecasting predicted replication or results fairly well. That is a different target from transfer, and forecasters tend to overestimate effects.

In software and AI the record is thin:
- Cross-project defect prediction succeeded in about 3% of pairings, where success meant recall, precision and accuracy all above 0.75. This comes from a secondary mapping study; the primary paper was not opened.
- In one scaffold-comparison study, a pre-registered prediction that stronger models would depend less on their scaffold was rejected in direction, though tier-scaling held at one level.
- Benchmark and simulated-user results did not predict what happened with real users.

I found no test of any conditions-checklist or theory-based method in which the check was applied before a transfer and then scored against the outcome, in any field. For three of the question's settings there is nothing at all: team size, degree of human oversight, and product kind beyond benchmark-to-real gaps. For model change there are only the scaffold and prompt-portability studies. All of this rests on one Input reader pass and one Source checker round, and several key sources were never opened.

Grades: **B** = the Input reader reports it from a page it opened (unconfirmed until the Source checker opens it). **C** = weak (for example, one secondary page). **assumed (search-only)** = seen only in a search extract. Library facts carry their own grade. Unless noted, each fact rests on a single source.

---

## Part 1: What methods exist

**1a. Naive extrapolation and similarity.**
- **Fact, B (F010-1):** "Predictions based on rich microdata from the first ten replications substantially overstate efficacy in the next 101 sites". The causes given are that utilities in environmentalist areas "are more likely to adopt" and that early trials targeted high-usage households. Allcott, NBER w18373, https://www.nber.org/papers/w18373.
- **Fact, C, secondhand (F010-2):** across 635 papers (15,024 estimates) of development evaluations, a similar study "will have the correct sign 61% of the time", and a naive effect-size prediction is "wrong by about 249%". Source: Jason Collins, paraphrasing Vivalt (JEEA 2020) rather than quoting her, https://td.jcx.au/interpreting-trial-results/generalisability-effect-sizes.html. Vivalt's paper was not opened. This is a single secondary source.
- **Fact, library Q-009-F6-1, weak (C):** a World Bank blog review of Cartwright and Hardie says Tennessee class-size results did not carry to California because the "support factors weren't in place". It also says similarity thinking can "invite you to stop thinking".

**1b. Statistical adjustment, bounding and pooling.**
- Reweighting and doubly robust extrapolation: F010-3 (Kern et al., 2016, https://pmc.ncbi.nlm.nih.gov/articles/PMC5030077).
- Covariate adjustment across job-training sites: F010-4 (Hotz, Imbens and Mortimer, https://www.nber.org/papers/t0238).
- Macro- versus micro-level covariates: F010-5 (Dehejia, Pop-Eleches and Samii, https://arxiv.org/abs/1906.08096).
- Bounds: F010-6 (Gechter, JBES 2024, https://ideas.repec.org/a/taf/jnlbes/v42y2024i2p801-811.html).
- Site-selection bias: F010-7 (Stuart et al., https://pmc.ncbi.nlm.nih.gov/articles/PMC5739324).
- Bayesian hierarchical pooling: F010-8 (Meager, https://researchonline.lse.ac.uk/id/eprint/88190/).
- All are **Fact, B** as descriptions of the methods. Their results are under Part 2.

**1c. Formal transportability.**
- **Fact, B (F010-9):** Pearl and Bareinboim give "graph-based procedures for deciding, prior to observing any data, whether causal effects" can be carried to a new population. The abstract reports no test against real outcomes. https://arxiv.org/abs/1503.01603

**1d. Conditions checklists and theory-based methods.**
- **Cartwright and Hardie, "will it work here" (F010-10):** asks whether the policy plays the same causal role here and whether its support factors are present. Grade **B, secondary only**: the book was not opened. Daniel Little's 2013 post quotes the book on causal role and support factors, https://undsoc.org/2013/06/20/causal-inference-and-random-trials/. The LSE page (https://blogstest.lse.ac.uk/lsereviewofbooks/?p=12790) did not resolve. Library Q-009-F6-1 (weak C) supports the support-factor idea secondhand.
- **Realist context-mechanism-outcome configurations tested inside trials (F010-11):** **Fact, B.** The authors say whether this works "is ultimately an empirical question" and describe no test of transfer. Bonell et al., Trials 2016, https://pmc.ncbi.nlm.nih.gov/articles/PMC5045599/. **Stake:** the authors run realist trials.
- **PIET-T (F010-12):** **Fact, B.** A systematic review found 44 transferability criteria with "limited empirical support" and says the model's usefulness "must be evaluated". https://pmc.ncbi.nlm.nih.gov/articles/PMC6019740. **Stake:** the authors propose the model.
- **CFIR (F010-13):** **Fact, B.** The study "was designed a priori to apply the CFIR throughout" to find constructs linked to implementation at 12 months. The authors call the results exploratory rather than confirmatory and say "we did not pre-test items or conduct reliability and validity assessments". It is not a test of transfer. https://pmc.ncbi.nlm.nih.gov/articles/PMC8496554
- **DORA AI Capabilities Model (F010-30):** **Fact, B.** It names seven conditions said to amplify AI's benefits, drawn from interviews and a survey of about 5,000 people. It says "in the absence of a user-centric focus, AI adoption can have a negative impact on team performance". The Input reader saw no prospective test. https://cloud.google.com/blog/products/ai-machine-learning/introducing-doras-inaugural-ai-capabilities-model (also https://dora.dev/research/2025/ai-capabilities-model). **Stake:** Google sells AI development tools. The data are correlational survey data.
- **Tipton's generalisability index:** seen in search only. No validation was found, and no finding id was assigned.
- **Cross-project defect prediction (F010-21):** **B, secondary.** Zimmermann et al. (2009) built decision trees to estimate before trying a prediction whether it would succeed. This is the only software-engineering pre-transfer screen found. Whether the trees were later validated is unknown. The primary paper was not opened.

**1e. Forecasting results or replication.** Prediction markets (F010-14), a machine-learning replication model (F010-15), expert crowds (F010-16, F010-17) and GPT-4 (F010-18). All are **Fact, B**; results are under Part 2.

**1f. Field-level track records.** These describe how often findings carried in a field; they are not methods applied case by case.
- Lab-to-field psychology: F010-19.
- Many Labs 2: F010-20.
- Software-engineering meta-analysis moderators: F010-22, F010-23.
- ML distribution shift: F010-24, F010-25.
- AI benchmark or scaffold to other settings: F010-26 to F010-29, plus library Q-004-F-Q004-6 and Q-009-F2-3.

**Opinion:** I found no method built for AI practices. **Estimate:** this rests on one search pass, so a method may exist unseen.

---

## Part 2: How well the methods predicted transfer

**Naive extrapolation: poor in the tests found (each from a single source).**
- Opower (F010-1): the first-ten-sites prediction overstated the effect at the next 101 sites. The trials were analysed after the fact, not predicted ahead.
- Vivalt (F010-2): one similar study got another's sign right 61% of the time. That is a baseline for "it worked there". It is secondhand, on one secondary page (C).

**Covariate reweighting and adjustment: mixed, often poor.**
- **Fact, B (F010-3):** in 56 pairings of 8 sites, average bias was small on the IHDP benchmark only. In the SDDAP simulations "none of the methods performs reliably". Accuracy varied widely by method: "The methods with by far the worst performance with regard to RSMSE are the Doubly Robust (DR) approaches." The test was retrospective, and only the first 100k characters were read. **Stake:** the authors developed some of these methods.
- **Fact, B (F010-4):** across four US job-training sites, adjustment "removes most of the differences between control units", but trainee outcomes still did not match. The authors surmise that "differences in treatment components across training programs are the likely cause". **Estimate:** so adjustment may not capture differences in what each programme delivered.
- **Fact, B (F010-5):** across country-year census samples, prediction error "increases with increasing differences in education levels" and is small when covariate differences are small (from the Source checker's full-text reading; the Input reader read the abstract only). Also, "macro covariates dominate over micro covariates".
- **Fact, B (F010-7):** non-random site selection "can have a substantial influence". The Reading First impact in the selected districts would have been 0.10 SD lower than in the population. Bell et al. 2016, which this cites, was not opened.

**Bounding: one success.**
- **Fact, B (F010-6):** "the bounds are able to recover average treatment effects in one location using results from the other", where a benchmark method did not. It is one test with two Indian sites, abstract only. **Stake:** the author proposes the method.

**Hierarchical pooling: one favourable case.**
- **Fact, B (F010-8):** in seven microcredit trials, about 60% of the variation across sites was sampling noise. The author finds "reasonable external validity", and economic features predicted variation better than study protocols did.
- **Sources disagree:** F010-8 (reasonable transfer for microcredit) against F010-2 (poor transfer across many development fields). **Opinion:** they are probably compatible, since one is a single intervention class and the other a cross-field average, but this has not been checked.

**Formal transportability (F010-9):** no test of its predictions found.

**Conditions checklists (F010-10 to F010-13, F010-30):** no test found in which the check was applied before a transfer and scored against the outcome. CFIR was applied a priori, but its links to implementation are exploratory and do not test transfer (F010-13). PIET-T's own authors say it must be evaluated (F010-12). Bonell (F010-11) proposes a test and does not run one. **Estimate:** this is an absence in one search, not proof that no test exists.

**Forecasting: tested and fairly good, but of replication or results, not transfer.**
- **Fact, B (F010-14):** prediction markets "correctly predicted the outcomes for 18 of the 21 replications". The source is a University of Pennsylvania press release; the Nature Human Behaviour paper could not be opened. **Stake:** a university press office.
- **Fact, B (F010-15):** a machine-learning model was right on 70% of replications in cross-validation and "71% (AUC of 0.73)" in a pre-registered out-of-sample test.
- **Fact, B (F010-16):** averaged expert forecasts of 15 treatments beat 96% of individual forecasts, but "not if accuracy is defined as rank ordering treatments". Credentials did not predict accuracy.
- **Fact, B (F010-17):** of 100 forecast projects, 66 have results. On those, the average forecast predicted treatment effects well, but "forecasters, on average, over-estimate treatment effects". Field expertise did not raise accuracy, but academics had higher accuracy than non-academics, and confidence was "perversely associated with lower accuracy".
- **Fact, B (F010-18):** GPT-4's predictions of 70 survey experiments correlated strongly with the actual effects, including studies published after its training cutoff, but it "systematically overestimated effect sizes". The experiment counts differ between versions. https://www.gsb.stanford.edu/faculty-research/publications/large-language-models-can-predict-results-social-science-experiments
- **Opinion:** forecasting asks whether a result is real or how large it is, not whether it holds in a different setting. It transfers to the transfer question only partly. The repeated finding that forecasters overestimate effects (F010-17, F010-18) may bear on judging outside practices.

**Field-level track records.**
- **Fact, B (F010-19):** "effects found in social psychology laboratories most frequently changed signs in the field". Industrial-organisational psychology transferred most reliably, and small lab effects transferred worst. Abstract only.
- **Fact, B (F010-20):** in Many Labs 2, "variability in observed effect sizes was more attributable to the effect being studied than the sample or setting". 54% of effects replicated (p < .05).
- **Sources disagree in emphasis:** F010-20 (setting matters little) against F010-5 and F010-19 (setting distance and field matter). **Opinion:** Many Labs 2 varied samples, not the programme delivered or the institution, so the two may be measuring different kinds of setting change.
- **Software engineering:**
  - Cross-project defect prediction (F010-21, **B, secondary**: Herbold's 2017 mapping study, arXiv 1705.06429): 21 of 622 cross-project predictions (3.4%) succeeded, where success meant recall, precision and accuracy all above 0.75. The primary Zimmermann paper was not opened.
  - Pair programming (F010-22, **Fact, B**, abstract only): effects varied between studies and depended on task complexity.
  - Context in software-engineering findings (F010-23, **assumed (search-only)**): Dybå et al. argue findings must be "contextualized". It is a position paper and was not opened.
- **ML distribution shift: the sources disagree.**
  - F010-24 (**Fact, B**, Miller et al., 2021): "out-of-distribution performance is strongly correlated with in-distribution performance", with named exceptions (CIFAR-10-C, Camelyon17-WILDS).
  - F010-25 (**Fact, B**, Salaudeen et al., NeurIPS 2025): the pattern is "often an artifact of aggregating heterogeneous OOD examples". On some subsets, "sometimes over half of the standard OOD set", "higher ID accuracy predicts lower OOD accuracy".
  - The later paper challenges the accuracy-on-the-line pattern that the earlier one reports, though it does not name Miller et al.

**AI and agent settings, by the question's dimensions.**
- **Model change.**
  - **Fact, B (F010-26):** in a study comparing scaffolds on GAIA, a pre-registered prediction that more capable models would be less sensitive to scaffolding was rejected in direction, although tier-scaling held at Level 1. Other pre-registered predictions in the same study held or were falsified. "the elicitation gap is not guaranteed to shrink as models improve". Model family rather than capability tier decided whether the multi-agent advantage held, and scaffold choice alone moved accuracy by up to 28 points. It is a single-author preprint, abstract only. https://arxiv.org/abs/2606.08529
  - **Fact, B (F010-27):** coding models fine-tuned under OpenHands "score well under OpenHands but degrade substantially" under other scaffolds; untrained base models do not. A workshop paper (Vats and Golev, "Deep Learning for Code" workshop) says of the leaderboard assumption of a constant scaffold, "We show this assumption breaks down empirically." **Stake:** the DCAS authors propose their own fix.
  - **Library Q-004-F-Q004-6, weak (C\*):** prompts optimised for one model do not reliably generalise to other models.
- **Product kind (benchmark to real use).**
  - **Fact, B (F010-28):** METR says automatic scoring "may overestimate AI agent real-world performance". Test-passing pull requests still needed substantial work. One model, small sample. https://metr.org/blog/2025-08-12-research-update-towards-reconciling-slowdown-with-time-horizons
  - **Library Q-009-F2-3, moderate (B):** maintainers would not merge about half of test-passing agent pull requests.
  - **Fact, B (F010-29):** in a pre-registered randomised study of 1,298 people, medical benchmarks and simulated users "do not predict the failures we find with human participants". https://pmc.ncbi.nlm.nih.gov/articles/PMC12920132/
- **Team size and developer population.** No test of a transfer method. The library has statements only:
  - Q-009-F6-3 (moderate B): less experienced developers had greater gains. **Stake:** Microsoft.
  - Q-009-F6-4 (moderate B): Google's authors say they cannot assume their effect size applies more broadly.
  - Q-009-F6-5 (moderate B): METR says its developers and repositories are not representative.
  - Q-009-F6-6 (moderate B): context files are useful for specifying non-standard coding practices.
- **Degree of human oversight:** no source found.
- **Copying an organisational practice (not AI):** **Fact, B, practitioner (F010-31).** A former Spotify employee says the squad model was not really practised even at Spotify and failed when others copied it. He quotes Anders Ivarsson, a co-author of the Spotify whitepaper: "It worries me when people look at what we do and think it's a framework they can just copy and implement." https://www.jeremiahlee.com/posts/failed-squad-goals/ This is one anecdote with a former-employee perspective.

**How far the evidence carries over (opinion).** Most of the tested evidence is about carrying an intervention's average effect between populations in social programmes. Adopting an AI-building practice in a different team, model or oversight regime is analogous in structure, but none of the tested methods has been applied there. The AI-specific evidence (F010-26 to F010-29) shows that transfer across model, scaffold and benchmark-to-real often fails. It does not test any method for predicting when transfer will fail. Thin areas: oversight (none), team size (none), conditions checklists (untested anywhere).

---

## What each possible answer would change (from the question; not chosen here)

- **"A method shown to predict transfer well becomes a candidate check."** The only methods with good scored records are forecasting methods (markets, expert crowds, machine-learning and LLM forecasts), and their target is replication or results, not transfer. One bounding test (F010-6) and one pooling case (F010-8) did well within economics. Each rests on one source. Whether any of these counts as "shown to predict transfer well" for this purpose is the decision-maker's call.
- **"A method shown to predict poorly weighs against using it."** These have scored records that are poor, each from a single source:
  - naive extrapolation from earlier sites or similar studies (F010-1, F010-2; the 61% figure rests on one secondary page, C);
  - covariate-only adjustment where the programme differs (F010-4, where the cause is only surmised);
  - doubly robust methods, and all methods in the SDDAP simulations (F010-3).

  In AI, three things performed poorly or are disputed:
  - in one scaffold-comparison study, the prediction that stronger models are less scaffold-sensitive was rejected in direction, though it held at Level 1 (F010-26);
  - benchmark-predicts-use performed poorly (F010-28, F010-29);
  - in-distribution-predicts-OOD is disputed (F010-25 against the pattern in F010-24).
- **"A method that predicts well only in some settings is a candidate for those settings."** Some evidence suggests accuracy depends on the field and on how far apart the settings are:
  - industrial-organisational lab results transferred better than social psychology (F010-19);
  - error grew with covariate distance, and place-level traits mattered more (F010-5);
  - the effect mattered more than the sample (F010-20).

  None of these settings is an AI-building setting.
- **"If no method has been tested, the choice of check rests on other grounds."** This describes the conditions-checklist family as found: Cartwright and Hardie, realist evaluation, PIET-T, CFIR, DORA's model and Pearl and Bareinboim's formal method. No prospective scored test was found for any of them.

**Gaps (sources I need that the Input reader did not open):**
- Cartwright and Hardie's book;
- Vivalt (JEEA 2020) itself;
- Camerer et al. (Nature Human Behaviour 2018) itself;
- Zimmermann et al. (ESEC/FSE 2009) and any later validation of its decision trees;
- Dybå, Sjøberg and Cruzes (ESEM 2012);
- the Tipton generalisability-index paper and any validation of it;
- Bell et al. 2016;
- full texts of Mitchell (2012), Many Labs 2, Gechter and Starace;
- any study of transfer across team size or degree of human oversight in AI-assisted development;
- a second independent source for each load-bearing fact, especially the short-answer claims on naive extrapolation (F010-1, F010-2), covariate adjustment (F010-3, F010-4) and the AI items (F010-26, F010-28, F010-29).

**Questions I propose adding (neutral form):**
- Has any conditions-based transferability check (support factors, realist configurations, CFIR, PIET-T) been applied before an intervention was introduced at a new site and then scored against the outcome there? If so, with what accuracy?
- Has the Zimmermann et al. decision-tree pre-screen for cross-project prediction, or a successor, been validated on new project pairs?

**Possible inconsistency for the Source checker:** the input opens by saying "27 findings" but lists 31 numbered entries (F010-1 to F010-31). It also states that 28 rest on opened pages.

---

## Proposed library entries (statement | type | grade | shelf life proposed)

1. Predictions from the first ten Opower trials' microdata overstated efficacy at the next 101 sites (site selection: utilities in environmentalist areas more likely to adopt; analysed after the fact) | fact | B | 5 years
2. Across 635 development-evaluation papers (15,024 estimates), a similar study had the correct sign 61% of the time (secondhand, a paraphrase of Vivalt by Collins; single secondary source) | fact | C | 5 years
3. In 56 site pairings, extrapolation methods had small average bias on the IHDP benchmark only, with widely varying accuracy; doubly robust methods were worst on RSMSE; in the SDDAP simulations none performed reliably | fact | B | 5 years
4. Across four job-training sites, covariate adjustment removed most differences between control groups but did not equalise trainee outcomes; the authors surmise programme differences as the cause | fact | B | 5 years
5. Across country-year census samples, extrapolation error grew with covariate differences (such as education levels); macro covariates mattered more than micro | fact | B | 5 years
6. In one two-site Indian test, a bounding method recovered the other site's effect where a benchmark did not (the author proposes the method) | fact | B | 5 years
7. In seven microcredit trials about 60% of cross-site heterogeneity was sampling variation; the author finds reasonable external validity | fact | B | 5 years
8. PIET-T review: 44 transferability criteria with limited empirical support; usefulness still to be evaluated | fact | B | 3 years
9. A statewide study designed a priori around CFIR found exploratory links to implementation, with no validity testing of its items; not a test of transfer | fact | B | 3 years
10. Prediction markets predicted 18 of 21 Nature/Science replications (press release; paper not opened) | fact | B | 5 years
11. A machine-learning model predicted 71% of replications (AUC 0.73) in a pre-registered out-of-sample test | fact | B | 5 years
12. Across the 66 of 100 forecast projects with results, the average forecast predicted effects well but overestimated them; expertise did not raise accuracy, though academics beat non-academics | fact | B | 3 years
13. GPT-4 predictions of survey-experiment effects correlated strongly with actual effects but systematically overestimated effect sizes | fact | B | 18 months
14. Across 217 lab-field comparisons, social-psychology lab effects most often changed sign in the field; industrial-organisational psychology transferred best | fact | B | 5 years
15. Many Labs 2: effect-size variation was more attributable to the effect than to the sample or setting | fact | B | 5 years
16. Out-of-distribution accuracy tracks in-distribution accuracy across many models (Miller et al. 2021); a 2025 paper calls this accuracy-on-the-line pattern often an artifact of aggregating heterogeneous OOD data (Salaudeen 2025) | fact with disagreement stated | B | 2 years
17. In a GAIA scaffold-comparison study, a pre-registered prediction that stronger models are less scaffold-sensitive was rejected in direction (tier-scaling held at Level 1); scaffold choice moved accuracy by up to 28 points | fact | B (single-author preprint) | 12 months
18. Coding models fine-tuned under one scaffold degrade substantially under others; base models do not | fact | B | 12 months
19. Medical benchmarks and simulated users did not predict failures with real participants (pre-registered RCT, n=1,298) | fact | B | 18 months
20. METR: automatic scoring may overestimate agents' real-world performance (one model, small sample) | fact | B | 12 months
21. DORA's AI Capabilities Model names seven amplifying conditions from survey and interviews; no prospective test seen (Google has a stake) | fact | B | 12 months
22. No prospective scored test found of any conditions-checklist transferability method (Cartwright, realist evaluation, PIET-T, CFIR, DORA model) | opinion (absence in one search) | n/a (opinion) | 12 months
23. Before adopting an outside practice, treat "it worked there" as a weak predictor (sign right about 61% in one cross-field dataset, from one secondary source), and expect forecasts of effects to run high | pattern | opinion built on B and C sources | 2 years

---

## Finding ids relied on (for the Source checker)

F010-1 to F010-31, every numbered entry. Search-only: F010-23. Secondary only: F010-10 (Little's post), F010-21 (Herbold 2017). Removed as unconfirmed: the F010-5 convergence claim and "166"; the F010-18 r=0.85 figure; the F010-19 figures; the F010-27 52.6%→8.4% figure; the F010-21 same-domain claim and Microsoft stake; the F010-2 AidGrade stake; the F010-17 platform stake.

Library entries cited: Q-009-F6-1, Q-009-F6-3, Q-009-F6-4, Q-009-F6-5, Q-009-F6-6, Q-004-F-Q004-6, Q-009-F2-3.

Files read: /home/user/Model-Lab/research/Q-010.md, /home/user/Model-Lab/research/Q-010-input.md, /home/user/portfolio/library/README.md, and the seven library fact files above. For this revision: /home/user/Model-Lab/research/Q-010-memo.md and /home/user/Model-Lab/research/Q-010-source-check.md.

**Tokens:** I cannot see my token total.

---

## Change list (item | what changed | correction answered)

1. **F010-13, Part 2 checklists paragraph, entry 9:** "used retrospectively" is now "designed a priori to apply the CFIR". "after-the-fact links" is now "exploratory links… do not test transfer". Entry 9 says it is not a transfer test. (Correction 1)
2. **F010-5, Part 2 bullet, entry 5, "some settings" bullet:** dropped "166" and the convergence claim. Added that error rises with covariate differences, cited to the checker's full-text reading. (Correction 2)
3. **F010-2, short answer, Part 2, entry 2, entry 23:** "about 600" is now 635 papers (15,024 estimates). "quoting" is now "paraphrasing". Dropped the AidGrade stake. Grade B is now C. Entry 23's grade basis is now "B and C". (Correction 3)
4. **F010-1, Part 2 Opower bullet, entry 1:** the quote is now exact and its search-only caveat is lifted. "adopted first" is now "more likely to adopt". "close to prospective" is now "analysed after the fact". (Correction 4)
5. **F010-26, short answer, "poorly" bullet, entry 17:** removed "the one pre-registered transfer prediction in AI… failed". It is now a scaffold-comparison study whose prediction was "rejected in direction", with tier-scaling holding at Level 1. "capability-predicts-transfer assumption" is reworded. (Correction 5)
6. **F010-17, entry 12:** added 66 of 100 with results and that academics beat non-academics. Dropped the platform stake. (Correction 6)
7. **F010-3, F010-4, short answer covariate bullet, "poorly" bullet, entries 3 and 4:** low bias holds for IHDP only. Added the SDDAP "none of the methods performs reliably". "made comparable" is now "removes most of the differences". The cause is now "surmise", and "blamed" is gone. My inference from F010-4 is now marked as an estimate. (Correction 7)
8. **F010-18, F010-19, F010-27, entry 14:** deleted r=0.85, the F010-19 figures and 52.6%→8.4%. Entry 14 grade is now plain B. (Correction 8)
9. **F010-21, F010-31, short answer:** added the success definition. Dropped the same-domain claim and the Microsoft stake. Grade is now B secondary (Herbold 2017), following the check's mark. The quote is credited to Anders Ivarsson. (Correction 9)
10. **F010-24, F010-25, entry 16, "poorly" bullet:** dropped "ICML 2021" and added the named exceptions. "directly challenges the earlier one" is now "challenges the accuracy-on-the-line pattern… does not name Miller". OOD in the "poorly" bullet is now "disputed", not "performed poorly". (Correction 10)
11. **Short answer, grade legend, "what each answer" section, Gaps:** each claim is marked as resting on one source. Added "a second independent source for each load-bearing fact" to Gaps. I could add no sources, since the web is barred. (Correction 11)
12. **F010-10:** "assumed (search-only)" is now "B, secondary only", following the check's mark (move between assumed and B).
13. **Short answer last sentence, Finding-ids section:** "none of it has been source-checked yet" now names the one Source checker round. The lists of search-only and removed items are updated. (Consequence of the round)

Marks I left unchanged because "What the memo must correct" does not list them:
- F010-3 "retrospective" (memo's word);
- F010-21's description of the decision trees (the check says they select a training project);
- F010-30 omitting "unlock", and "correlational" being the reader's reading;
- F010-28 page dated 2025-08-13;
- F010-15 body AUC 0.72;
- F010-29 medical setting;
- the checker's weak-C filings for entries 10, 17 and 18.

## Finding ids to re-check
F010-1, F010-2, F010-3, F010-4, F010-5, F010-10, F010-13, F010-17, F010-18, F010-19, F010-21, F010-24, F010-25, F010-26, F010-27, F010-31. Also the short answer, the "what each answer would change" section, and proposed entries 1–5, 9, 12, 14, 16, 17 and 23.

## Tokens
I cannot see my token total.
