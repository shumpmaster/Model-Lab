# Q-010 memo: methods for predicting whether a practice transfers to a new setting, and how well they have predicted (Researcher, 2026-11-08)

*The Researcher's memo for Q-010 on brief 158 (docs/briefs/158-researcher.md), 2026-11-08, recorded verbatim by the Orchestrator (session_01QBwHGNSLmSrYQgS6BPjV8p) from the helper's return; only this italic line is the Orchestrator's. Its B items stay unconfirmed until the Source checker has opened them (research/Q-010-source-check.md).*

**Short answer.** Methods for judging whether a finding will hold elsewhere fall into five families:
- naive extrapolation from similar studies;
- statistical adjustment (reweighting on covariates, bounding, hierarchical pooling);
- formal causal-graph transportability;
- conditions checklists and theory-based methods (Cartwright and Hardie's support factors, realist context-mechanism-outcome, PIET-T, CFIR, DORA's AI Capabilities Model);
- forecasting (prediction markets, expert crowds, machine-learning models, LLMs).

Only the first two families and forecasting have been scored against what then happened, and almost all of those tests come from economics, education, psychology and social science, not from building software with AI. In those tests:
- Naive extrapolation predicted poorly. The first 10 Opower sites overstated the effect at the next 101. One similar study got another's sign right only 61% of the time.
- Covariate adjustment was mixed and often poor, and failed where the programme itself differed between sites. It did better when it used place-level traits, and in one microcredit pooling and one bounding test.
- Forecasting predicted replication or results fairly well. That is a different target from transfer, and forecasters tend to overestimate effects.

In software and AI the record is thin:
- Cross-project defect prediction succeeded in about 3% of pairings (search-only).
- A pre-registered prediction that stronger models would depend less on their scaffold was rejected.
- Benchmark and simulated-user results did not predict what happened with real users.

I found no test of any conditions-checklist or theory-based method in which the check was applied before a transfer and then scored against the outcome, in any field. For three of the question's settings there is nothing at all: team size, degree of human oversight, and product kind beyond benchmark-to-real gaps. For model change there are only the scaffold and prompt-portability studies. All of this rests on one Input reader pass, none of it has been source-checked yet, and several key sources were never opened.

Grades: **B** = the Input reader reports it from a page it opened (unconfirmed until the Source checker opens it). **assumed (search-only)** = seen only in a search extract. Library facts carry their own grade.

---

## Part 1: What methods exist

**1a. Naive extrapolation and similarity.**
- **Fact, B (F010-1):** predictions from the first ten Opower trials' rich microdata "substantially overstate efficacy in the next 101 sites". The causes given are that utilities with stronger effects adopted first and that early trials targeted high-usage households. Allcott, NBER w18373, https://www.nber.org/papers/w18373. The quoted wording is **assumed (search-only)**: the fetch tool confirmed it only as a paraphrase.
- **Fact, B secondhand (F010-2):** across about 600 development evaluations, a similar study predicts another's sign "61% of the time", and a naive effect-size prediction is wrong "by about 249%". Source: Jason Collins quoting Vivalt (JEEA 2020), https://td.jcx.au/interpreting-trial-results/generalisability-effect-sizes.html. Vivalt's paper was not opened. **Stake:** Vivalt founded AidGrade, the data source.
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
- **Cartwright and Hardie, "will it work here" (F010-10):** asks whether the policy plays the same causal role here and whether its support factors are present. Grade **assumed (search-only)**: the book was not opened; secondary pages at https://blogstest.lse.ac.uk/lsereviewofbooks/?p=12790 and https://undsoc.org/2013/06/20/causal-inference-and-random-trials/. Library Q-009-F6-1 (weak C) supports the support-factor idea secondhand.
- **Realist context-mechanism-outcome configurations tested inside trials (F010-11):** **Fact, B.** The authors say whether this works "is ultimately an empirical question" and describe no test of transfer. Bonell et al., Trials 2016, https://pmc.ncbi.nlm.nih.gov/articles/PMC5045599/. **Stake:** the authors run realist trials.
- **PIET-T (F010-12):** **Fact, B.** A systematic review found 44 transferability criteria with "limited empirical support" and says the model's usefulness "must be evaluated". https://pmc.ncbi.nlm.nih.gov/articles/PMC6019740. **Stake:** the authors propose the model.
- **CFIR (F010-13):** **Fact, B.** It was used retrospectively to find constructs linked to implementation at 12 months. The authors call the results exploratory and say "we did not pre-test items or conduct reliability and validity assessments". https://pmc.ncbi.nlm.nih.gov/articles/PMC8496554
- **DORA AI Capabilities Model (F010-30):** **Fact, B.** It names seven conditions said to amplify AI's benefits, drawn from interviews and a survey of about 5,000 people. It says "in the absence of a user-centric focus, AI adoption can have a negative impact on team performance". The Input reader saw no prospective test. https://cloud.google.com/blog/products/ai-machine-learning/introducing-doras-inaugural-ai-capabilities-model (also https://dora.dev/research/2025/ai-capabilities-model). **Stake:** Google sells AI development tools. The data are correlational survey data.
- **Tipton's generalisability index:** seen in search only. No validation was found, and no finding id was assigned.
- **Cross-project defect prediction (F010-21):** **assumed (search-only).** Zimmermann et al. (2009) built decision trees to estimate before trying a prediction whether it would succeed. This is the only software-engineering pre-transfer screen found. Whether the trees were later validated is unknown.

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

**Naive extrapolation: poor in the tests found.**
- Opower (F010-1): the first-ten-sites prediction overstated the effect at the next 101 sites. The structure is close to prospective: the earlier sites predicted, the later sites were the outcome.
- Vivalt (F010-2): one similar study got another's sign right 61% of the time. That is a baseline for "it worked there", and it is secondhand.

**Covariate reweighting and adjustment: mixed, often poor.**
- **Fact, B (F010-3):** in 56 pairings of 8 sites, average bias was small but accuracy varied widely by method. "The methods with by far the worst performance with regard to RSMSE are the Doubly Robust (DR) approaches." The test was retrospective, and only the first 100k characters were read. **Stake:** the authors developed some of these methods.
- **Fact, B (F010-4):** adjustment made control groups comparable across four US job-training sites, but trainee outcomes still did not match. "differences in treatment components across training programs are the likely cause". So adjustment cannot capture differences in what each programme delivered.
- **Fact, B (F010-5):** across 166 country-year censuses, prediction error grew with how different the two places were, and "macro covariates dominate over micro covariates". The claim that naive extrapolation does not converge is **assumed (search-only)**. The abstract only was read.
- **Fact, B (F010-7):** non-random site selection "can have a substantial influence". The Reading First impact in the selected districts would have been 0.10 SD lower than in the population. Bell et al. 2016, which this cites, was not opened.

**Bounding: one success.**
- **Fact, B (F010-6):** "the bounds are able to recover average treatment effects in one location using results from the other", where a benchmark method did not. It is one test with two Indian sites, abstract only. **Stake:** the author proposes the method.

**Hierarchical pooling: one favourable case.**
- **Fact, B (F010-8):** in seven microcredit trials, about 60% of the variation across sites was sampling noise. The author finds "reasonable external validity", and economic features predicted variation better than study protocols did.
- **Sources disagree:** F010-8 (reasonable transfer for microcredit) against F010-2 (poor transfer across many development fields). **Opinion:** they are probably compatible, since one is a single intervention class and the other a cross-field average, but this has not been checked.

**Formal transportability (F010-9):** no test of its predictions found.

**Conditions checklists (F010-10 to F010-13, F010-30):** no test found in which the check was applied before a transfer and scored against the outcome. CFIR has only exploratory, after-the-fact links (F010-13). PIET-T's own authors say it must be evaluated (F010-12). Bonell (F010-11) proposes a test and does not run one. **Estimate:** this is an absence in one search, not proof that no test exists.

**Forecasting: tested and fairly good, but of replication or results, not transfer.**
- **Fact, B (F010-14):** prediction markets "correctly predicted the outcomes for 18 of the 21 replications". The source is a University of Pennsylvania press release; the Nature Human Behaviour paper could not be opened. **Stake:** a university press office.
- **Fact, B (F010-15):** a machine-learning model was right on 70% of replications in cross-validation and "71% (AUC of 0.73)" in a pre-registered out-of-sample test.
- **Fact, B (F010-16):** averaged expert forecasts of 15 treatments beat 96% of individual forecasts, but "not if accuracy is defined as rank ordering treatments". Credentials did not predict accuracy.
- **Fact, B (F010-17):** across 100 projects, the average forecast predicted treatment effects well, but "forecasters, on average, over-estimate treatment effects". Field expertise did not raise accuracy, and confidence went with lower accuracy. **Stake:** the authors run the platform.
- **Fact, B (F010-18):** GPT-4's predictions of 70 survey experiments correlated strongly with the actual effects, including studies published after its training cutoff, but it "systematically overestimated effect sizes". The r=0.85 figure is **assumed (search-only)**, and the experiment counts differ between versions. https://www.gsb.stanford.edu/faculty-research/publications/large-language-models-can-predict-results-social-science-experiments
- **Opinion:** forecasting asks whether a result is real or how large it is, not whether it holds in a different setting. It transfers to the transfer question only partly. The repeated finding that forecasters overestimate effects (F010-17, F010-18) may bear on judging outside practices.

**Field-level track records.**
- **Fact, B (F010-19):** "effects found in social psychology laboratories most frequently changed signs in the field". Industrial-organisational psychology transferred most reliably, and small lab effects transferred worst. The figures (r≈.7 overall; .53 against .89; 30 of 217) are **assumed (search-only)**. Abstract only.
- **Fact, B (F010-20):** in Many Labs 2, "variability in observed effect sizes was more attributable to the effect being studied than the sample or setting". The 54% replication rate is **assumed (search-only)**.
- **Sources disagree in emphasis:** F010-20 (setting matters little) against F010-5 and F010-19 (setting distance and field matter). **Opinion:** Many Labs 2 varied samples, not the programme delivered or the institution, so the two may be measuring different kinds of setting change.
- **Software engineering:**
  - Cross-project defect prediction (F010-21, **assumed (search-only)**): 21 of 622 cross-project predictions (3.4%) succeeded, and a same-domain or same-process partner did not reliably help. **Stake:** Microsoft authors studying Microsoft and open-source systems.
  - Pair programming (F010-22, **Fact, B**, abstract only): effects varied between studies and depended on task complexity.
  - Context in software-engineering findings (F010-23, **assumed (search-only)**): Dybå et al. argue findings must be "contextualized". It is a position paper and was not opened.
- **ML distribution shift: the sources disagree.**
  - F010-24 (**Fact, B**, Miller et al., ICML 2021): "out-of-distribution performance is strongly correlated with in-distribution performance", with named exceptions.
  - F010-25 (**Fact, B**, Salaudeen et al., NeurIPS 2025): the pattern is often an artifact of pooling mixed data. On some subsets, sometimes over half the set, "higher ID accuracy predicts lower OOD accuracy".
  - The later paper directly challenges the earlier one; neither has been source-checked.

**AI and agent settings, by the question's dimensions.**
- **Model change.**
  - **Fact, B (F010-26):** on GAIA, a pre-registered prediction that more capable models would be less sensitive to scaffolding was rejected. "elicitation gap is not guaranteed to shrink as models improve". Model family, not capability tier, decided whether the multi-agent advantage held, and scaffold choice alone moved accuracy by up to 28 points. This is the one pre-registered transfer prediction in AI found, and it failed. It is a single-author preprint, abstract only. https://arxiv.org/abs/2606.08529
  - **Fact, B (F010-27):** coding models fine-tuned under OpenHands "score well under OpenHands but degrade substantially" under other scaffolds; untrained base models do not. A workshop paper says the leaderboard assumption of a constant scaffold "breaks down empirically". The 52.6%→8.4% figure is **assumed (search-only)**, from a blog. **Stake:** the DCAS authors propose their own fix.
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
- **Copying an organisational practice (not AI):** **Fact, B, practitioner (F010-31).** A former Spotify employee says the squad model was not really practised even at Spotify and failed when others copied it. He quotes its co-author: "It worries me when people look at what we do and think it's a framework they can just copy and implement." https://www.jeremiahlee.com/posts/failed-squad-goals/ This is one anecdote with a former-employee perspective.

**How far the evidence carries over (opinion).** Most of the tested evidence is about carrying an intervention's average effect between populations in social programmes. Adopting an AI-building practice in a different team, model or oversight regime is analogous in structure, but none of the tested methods has been applied there. The AI-specific evidence (F010-26 to F010-29) shows that transfer across model, scaffold and benchmark-to-real fails often. It does not test any method for predicting when transfer will fail. Thin areas: oversight (none), team size (none), conditions checklists (untested anywhere).

---

## What each possible answer would change (from the question; not chosen here)

- **"A method shown to predict transfer well becomes a candidate check."** The only methods with good scored records are forecasting methods (markets, expert crowds, machine-learning and LLM forecasts), and their target is replication or results, not transfer. One bounding test (F010-6) and one pooling case (F010-8) did well within economics. Whether any of these counts as "shown to predict transfer well" for this purpose is the decision-maker's call.
- **"A method shown to predict poorly weighs against using it."** Naive extrapolation from earlier sites or similar studies (F010-1, F010-2), and covariate-only adjustment where the programme differs (F010-4, F010-3 for doubly robust methods), have scored records that are poor. In AI, the capability-predicts-transfer assumption (F010-26), benchmark-predicts-use (F010-28, F010-29) and in-distribution-predicts-OOD (F010-25 against F010-24) also performed poorly.
- **"A method that predicts well only in some settings is a candidate for those settings."** Some evidence suggests accuracy depends on the field and on how far apart the settings are: industrial-organisational lab results transferred better than social psychology (F010-19), place-level traits mattered more (F010-5), and the effect mattered more than the sample (F010-20). None of these settings is an AI-building setting.
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
- any study of transfer across team size or degree of human oversight in AI-assisted development.

**Questions I propose adding (neutral form):**
- Has any conditions-based transferability check (support factors, realist configurations, CFIR, PIET-T) been applied before an intervention was introduced at a new site and then scored against the outcome there? If so, with what accuracy?
- Has the Zimmermann et al. decision-tree pre-screen for cross-project prediction, or a successor, been validated on new project pairs?

**Possible inconsistency for the Source checker:** the input opens by saying "27 findings" but lists 31 numbered entries (F010-1 to F010-31). It also states that 28 rest on opened pages.

---

## Proposed library entries (statement | type | grade | shelf life proposed)

1. Predictions from the first ten Opower trials' microdata overstated efficacy at the next 101 sites (site-selection bias) | fact | B (quote wording search-only) | 5 years
2. Across about 600 development evaluations, a similar study predicted another's sign 61% of the time (secondhand, via Collins; Vivalt has a stake as AidGrade founder) | fact | B secondhand | 5 years
3. In 56 site pairings, extrapolation methods had small average bias but widely varying accuracy; doubly robust methods were worst on RSMSE | fact | B | 5 years
4. Across four job-training sites, covariate adjustment equalised control groups but not trainee outcomes; programme differences were blamed | fact | B | 5 years
5. Across 166 censuses, extrapolation error grew with how different the places were; macro covariates mattered more than micro | fact | B | 5 years
6. In one two-site Indian test, a bounding method recovered the other site's effect where a benchmark did not (the author proposes the method) | fact | B | 5 years
7. In seven microcredit trials about 60% of cross-site heterogeneity was sampling variation; the author finds reasonable external validity | fact | B | 5 years
8. PIET-T review: 44 transferability criteria with limited empirical support; usefulness still to be evaluated | fact | B | 3 years
9. A statewide CFIR study found exploratory links to implementation, with no validity testing of its items | fact | B | 3 years
10. Prediction markets predicted 18 of 21 Nature/Science replications (press release; paper not opened) | fact | B | 5 years
11. A machine-learning model predicted 71% of replications (AUC 0.73) in a pre-registered out-of-sample test | fact | B | 5 years
12. Across 100 forecast projects, the average forecast predicted effects well but overestimated them; expertise did not raise accuracy (the authors run the platform) | fact | B | 3 years
13. GPT-4 predictions of survey-experiment effects correlated strongly with actual effects but systematically overestimated effect sizes | fact | B | 18 months
14. Across 217 lab-field comparisons, social-psychology lab effects most often changed sign in the field; industrial-organisational psychology transferred best | fact | B (figures search-only) | 5 years
15. Many Labs 2: effect-size variation was more attributable to the effect than to the sample or setting | fact | B | 5 years
16. Out-of-distribution accuracy tracks in-distribution accuracy across many models (Miller 2021), disputed as a pooling artifact (Salaudeen 2025) | fact with disagreement stated | B | 2 years
17. On GAIA a pre-registered prediction that stronger models are less scaffold-sensitive was rejected; scaffold choice moved accuracy by up to 28 points | fact | B (single-author preprint) | 12 months
18. Coding models fine-tuned under one scaffold degrade substantially under others; base models do not | fact | B | 12 months
19. Medical benchmarks and simulated users did not predict failures with real participants (pre-registered RCT, n=1,298) | fact | B | 18 months
20. METR: automatic scoring may overestimate agents' real-world performance (one model, small sample) | fact | B | 12 months
21. DORA's AI Capabilities Model names seven amplifying conditions from survey and interviews; no prospective test seen (Google has a stake) | fact | B | 12 months
22. No prospective scored test found of any conditions-checklist transferability method (Cartwright, realist evaluation, PIET-T, CFIR, DORA model) | opinion (absence in one search) | n/a (opinion) | 12 months
23. Before adopting an outside practice, treat "it worked there" as a weak predictor (sign right about 61% in one cross-field dataset), and expect forecasts of effects to run high | pattern | opinion built on B sources | 2 years

---

## Finding ids relied on (for the Source checker)

F010-1 to F010-31, every numbered entry. The search-only ones are F010-10, F010-21 and F010-23. Search-only parts of others: the F010-1 quote wording; the F010-5 convergence claim; the F010-18 r=0.85 figure; the F010-19 figures; the F010-20 54% figure; the F010-27 52.6%→8.4% figure.

Library entries cited: Q-009-F6-1, Q-009-F6-3, Q-009-F6-4, Q-009-F6-5, Q-009-F6-6, Q-004-F-Q004-6, Q-009-F2-3.

Files read: /home/user/Model-Lab/research/Q-010.md, /home/user/Model-Lab/research/Q-010-input.md, /home/user/portfolio/library/README.md, and the seven library fact files above.

**Tokens:** I cannot see my token total.
