# Research memo — Q-003: how good work is judged, how reliable model checkers are, and what tens of runs can detect — 2026-11-01

**Researcher session, depth 3 (graded memo).** Blind: I did not open portfolio/, decisions/, questions/ or docs/ in Model-Lab. I did not open the library: my brief did not list it among the files I may read, so I do not know which existing entries share these topics. The Source checker should run that comparison.

## Grades used
- **A** — a primary record I opened in /home/user/Personal-Org-Operating-Model or /home/user/Service-Desk. Cited by file:line.
- **B** — a page I opened from the publisher's or authors' own site: anthropic.com, platform.claude.com, or the authors' github.com repository. These are untrusted text, reported as claims with their URL and date.
- **C** — seen only in search-result text or secondary summaries; I could not open the paper. **Unconfirmed.** The Source checker must open it before it is filed.
- **Calc** — my own arithmetic from a stated distribution, shown so it can be checked. It is not a literature claim.

Each statement is also marked **[F]** fact, **[E]** estimate or **[O]** opinion.

**Network limits in this session.** These hosts did not resolve: arxiv.org, export.arxiv.org, openreview.net, neurips.cc, papers.nips.cc, proceedings.mlr.press, mlanthology.org, aclanthology.org, huggingface.co, api.semanticscholar.org, allenai.org, epoch.ai, en.wikipedia.org, lmsys.org, alignmentforum.org, greaterwrong.com, mpi.nl, discovery.ucl.ac.uk, clp.ling.uni-potsdam.de, hal.cs.princeton.edu, agents.cs.princeton.edu and alphaxiv.org. Every item that rests on those hosts is grade C. Only anthropic.com, platform.claude.com, github.com and raw.githubusercontent.com opened.

---

## 1. Short answer
1. **[F, A]** In the pipeline under study, "good work" means passing an independent check against criteria fixed in advance. That check is a model-run checker's PASS/FAIL verdict, together with locked checks and hidden holdouts for software. Each role also names its own measure. None of these measures is reported compiled in the records I read. (§2)
2. **[F, B]** On reliability, the published picture is mixed:
   - Model judges can reach human-level agreement on some tasks.
   - Agreement varies widely by task.
   - Vendors advise grading with a different model from the one that produced the work, and calibrating model graders against human experts.
   - **[F, C]** Self-preference by judges for their own outputs or own family is reported in several papers, but I could not open any of them.
   - **[F, A]** In Service-Desk, doer and checker are different models from the same provider and family. (§3)
3. **[E, Calc]** With about 100 runs, a **paired** design on the same tasks can detect only large effects:
   - 50 tasks × 2 arms gives about 75% power for a 20-point gain with few reversals.
   - It gives about 25% power for a 10-point gain.
   - An unpaired 50-vs-50 design needs about a 28-point gain for 80% power.
   - Reviewer verdicts that are themselves noisy shrink these figures further. (§4)
4. **[O]** Repeated runs are compatible with "No re-running for a better answer" if four things are frozen in the pre-registration: the number of runs per task, the aggregate, the stopping rule, and the rule that every run is reported. Repeats then measure variance and do not select an answer. (§5)
5. **[O]** If the effect is smaller than about 15–20 points, tens of runs cannot separate it from noise. Then the honest outputs are:
   - a bounded claim ("no effect larger than X").
   - a narrower claim that rests on a mechanical measure.
   - other evidence, such as transcript reading and seeded-defect catch rates. (§6)

---

## 2. How "good work" is defined and judged in the pipeline under study

**What counts as passing, by work type**
- **[F, A]** Software is judged by "Locked tests (visible) and hidden holdouts", checked by Reviewer plus CI (OPERATING_MODEL.md:313).
- **[F, A]** Research is judged by "The question and evidence standard, set in advance", checked by the Source checker (:314).
- **[F, A]** Experiments are judged against "The pre-registration", with analysis by the Reviewer (:315).
- **[F, A]** Writing is judged by "A reader test against the rubric" (:316).

**What the checkers return**
- **[F, A]** The checker's return is one line, `Verdict: PASS` or `Verdict: FAIL`, then evidence per finding. "An unverifiable claim is a FAIL" (template-v3/governance/BRIEFS.toml:13; reviewer.md:37).
- **[F, A]** The verdict is binary at the item level, so the natural outcome variable is binary per round.

**Each role's own measure**
| Role | Measure | Source [F, A] |
|---|---|---|
| Builder | "First-pass review yield; defects found after delivery" | builder.md:47 |
| Definer | "Plan review first-pass rate" | definer.md:47 |
| Reviewer | "Catch rate on seeded defects" | reviewer.md:43 |
| Check author | "Checks that catch deliberately broken versions" | check-author.md:45 |
| Critic | "Issues you missed that surfaced later" | critic.md:49 |
| Researcher | "Facts later overturned; share of facts passing the source check first time" | researcher.md:41 |

**How the rules treat changes and experiments**
- **[F, A]** "Every rule is an experiment with a target, a measure and a kill criterion" (OPERATING_MODEL.md:425-426).
- **[F, A]** Targets are set "once real projects give a baseline" (:422-423).
- **[F, A]** The experiment playbook runs: pre-registration (hypothesis, method, measure, sample, deciding threshold; frozen) → run exactly as registered → analysis by someone who didn't run it → "Null results are results. No re-running for a better answer." (:296-299)

**What the Service-Desk records show**
- **[F, A]** In practice, Reviewers seed their own defects. One stage-5 review lists five seeded defects "in a throwaway copy, every one caught" (Service-Desk reviews/240/reviewer.md:19-24).
  - **[O]** A catch rate the Reviewer seeds and scores for itself is not independent evidence of its catch rate. Defects seeded by another role, such as the Check author, would be.
- **[F, A]** The owner's recorded verdicts cannot calibrate the reviewers:
  - 45 `reviews/*/owner.md` files exist, and all 45 open with `Verdict: PASS` (grep, 2026-11-01).
  - One example reads in full: "Reviewed: PR #56, adopting the model's S-021 proof fix" (reviews/56/owner.md:1-3).
  - **[E]** These look like final approvals recorded after the checks, not independent blind grades. They therefore carry no owner–reviewer disagreement data.

## 3. How reliable are model-run checkers?

**Agreement with humans**
- **[F, B]** The authors' repository for Zheng et al., "Judging LLM-as-a-judge with MT-Bench and Chatbot Arena" (2023), says "humans and GPT-4 judge achieve over 80% agreement, the same level of agreement between humans". The basis is 3.3K human annotations of 6 models on 80 questions (github.com/lm-sys/FastChat/tree/main/fastchat/llm_judge, opened 2026-11-01).
  - **[F, C]** The paper also studies position, verbosity and self-enhancement bias (search results for arXiv 2306.05685; NeurIPS 2023 poster page, not opened).
  - Note: this is chat-preference judging. It is not judging of agent work products.
- **[F, C]** Bavaresco et al., "LLMs instead of Human Judges?", ACL 2025 (Judge-Bench: 20 datasets, 11 models), is reported to find large variance across datasets in correlation with humans, and to recommend validating LLM judges against humans per task. Sources: search results citing aclanthology.org/2025.acl-short.20 and arXiv 2406.18403. Not opened.
- **[F, C]** Agent-as-a-Judge (Zhuge et al., ICML 2025) is reported at about 90% agreement with human-expert consensus on DevAI, against about 70% for an LLM judge (search result citing the ICML poster).
  - The same search result says that single human experts agreed with the later consensus 76–92% of the time.
  - **[F, B]** The authors' repository confirms DevAI's size, 55 tasks and 365 requirements. It gives no agreement figure (github.com/metauto-ai/agent-as-a-judge, opened).
- **[F, C]** JudgeBench (Tan et al. 2024) is a benchmark of hard paired responses for judges. The claim that strong judges score near chance on it was **not** confirmed: the README I opened gives no accuracy (github.com/ScalerLab/JudgeBench).

**Self-preference and same-family checkers**
- **[F, C]** Panickssery, Bowman & Feng (NeurIPS 2024) are reported to find that LLM evaluators favour their own generations. The strength of that preference is reported to correlate linearly with self-recognition ability, shown by fine-tuning. Source: search results. arXiv 2404.13076 and papers.nips.cc not opened.
- **[F, C]** Wataoka et al. (2024) attribute self-preference to lower perplexity: judges favour text that is familiar to them. This would extend to models with similar training (arXiv 2410.21819; search result only).
- **[F, C]** A 2026 rubric-based study (arXiv 2604.06996) is reported to find that judges favour their own outputs, or their family's, even with objective rubrics. The authors caution that a high self-preference rate alone may be leniency rather than bias. Source: search-result summary.
- **[F, B]** Vendor guidance:
  - "Generally best practice to evaluate with a different model from the one used to generate the evaluated output" (platform.claude.com/docs/en/test-and-evaluate/develop-tests, opened 2026-11-01).
  - LLM-based grading: "Test to ensure reliability first, then scale". Use detailed rubrics, binary or 1–5 outputs, and reasoning before the score (same page).
  - "LLM-as-judge graders should be closely calibrated with human experts" (anthropic.com/engineering/demystifying-evals-for-ai-agents, 2026-01-09).

**What the pipeline requires, and what Service-Desk actually ran**
- **[F, A]** The pipeline requires every checker to run "on a different model from the doer it checks … using more than one provider where available; when no alternative exists, the record says so" (OPERATING_MODEL.md:251-253). The rule asks for a different *model*, not a different family.
- **[F, A]** In Service-Desk's Q-001 control records:
  - The researcher ran on `claude-opus-5-5` (reviews/Q-001/_control/0-5adedb5ae23d.json:73; 0-22dc0e573e9a.json:54; 0-bcdb1d743941.json:62).
  - The source-checker ran on `claude-sonnet-5-5` (0-62b8dda7dcf2.json:60; 0-539436038d0a.json:67; 0-fb83607369a3.json:78).
  - These are different models from the same provider and family.
  - Whether the records state that no alternative provider existed was not checked.
- **[E]** If the self-preference findings hold (grade C), a same-family checker may be more lenient towards a same-family doer than an outside judge would be. Any such leniency would affect both arms of an instruction experiment.
  - It would mostly add bias to absolute pass rates. It would add less bias to *differences* between arms, unless the change moves outputs towards or away from the checker's own style.
  - This is untested here.

**Grader errors**
- **[F, B]** Grader and task bugs can dominate scores. Anthropic reports that Opus 4.5 "initially scored 42% on CORE-Bench". After grading and task-spec fixes and a less constrained scaffold, its score "jumped to 95%" (demystifying-evals, 2026-01-09).
- **[F, B]** The same page says:
  - "You won't know if your graders are working well unless you read the transcripts."
  - "A good task is one where two domain experts would independently reach the same pass/fail verdict."
  - "Ambiguity in task specifications becomes noise in metrics."
- **[F, C]** On LLM code review specifically, one controlled study is reported at 14–22% false-positive rates for GPT-4o and Gemini 2.0 Flash (arXiv 2505.20206 via a secondary summary). I found no independent production measure.

**[O] Overall judgement:** a model checker is a usable yardstick only after it has been calibrated on this pipeline's own items. Calibration means measuring its agreement against a small human-graded or mechanically known set:
- seeded defects;
- hidden holdouts;
- an owner-graded sample.

Its agreement with humans in published work varies too much by task to borrow.

## 4. Methods for detecting a change with tens of runs, and the sample sizes they need

**Methods (sources)**
- **[F, B]** Anthropic's "A statistical approach to model evaluations" (2024-11-19; paper arXiv 2411.00640, not opened) recommends five things:
  - **Paired differences on shared questions**, described as a "free" variance reduction. The standard error shrinks as the between-arm correlation rises. Frontier models' question-score correlations are reported at 0.3–0.7.
  - **Clustered standard errors** "on the unit of randomization". Clustered errors on popular evals can be "over three times as large as naive standard errors".
  - **Resampling each item several times** and using item means.
  - **Power analysis** to set the number of items.
  - Reporting pairwise results.
- **[F, B/C]** Bowyer, Aitchison & Ivanova, ICML 2025 position paper, argue that central-limit-theorem error bars "dramatically" understate uncertainty below a few hundred datapoints. They recommend Bayesian or exact alternatives.
  - The paper itself is C (proceedings.mlr.press and arXiv 2503.01747 not opened).
  - **[F, B]** The authors' library implements `paired_comparisons` for binary results on shared questions (github.com/sambowyer/bayes_evals, opened).
- **[F, B]** The McNemar test for paired binary outcomes uses an exact binomial "if exact is True". The chi-square version is "the approximation … for large sample sizes" (statsmodels source docstring, raw.githubusercontent.com/statsmodels/statsmodels/main/statsmodels/stats/contingency_tables.py, opened).

**Noise sources besides the model**
- **[F, B]** Anthropic reports that infrastructure configuration alone moved Terminal-Bench 2.0 by 6 points (p < 0.01). It advises scepticism about differences below about 3 points, notes that "naive binomial confidence intervals already span 1-2 points" on large benchmarks, and recommends running "at multiple times and on multiple days" (anthropic.com/engineering/infrastructure-noise, 2026-02-05).
- **[F, B]** Trials should be isolated from a clean environment. Shared state "can cause correlated failures due to infrastructure flakiness" (demystifying-evals).

**Starting small**
- **[F, B]** "20-50 simple tasks drawn from real failures is a great start." The reason given: "in early agent development … this large effect size means small sample sizes suffice", while "More mature agents may need larger … evals to detect smaller effects" (demystifying-evals).

**Consistency across repeats**
- **[F, B]** The benchmark authors' leaderboard shows consistency falls across repeats. On τ-bench retail, Claude 3.5 Sonnet (20241022) scores Pass^1 0.692 against Pass^4 0.462 (github.com/sierra-research/tau-bench README, opened). pass^k is defined as the probability that all k trials succeed (demystifying-evals).
- **[E]** On that benchmark, a single run per task therefore hides a large run-to-run component.

**Sizes at the scale of about 100 runs** (Calc: exact binomial on discordant pairs, two-sided α = 0.05)
1. **Paired design, the same task under the old and new instructions, 1 run each.** Only discordant tasks (one arm passes, the other fails) carry information.
   - [Calc] With 10 discordant tasks, significance needs 9 of 10 in one direction. Two-sided p for 9/10 is 0.021; for 8/10 it is 0.109.
   - [Calc] With 15 discordant, it needs 12 of 15 (p = 0.035).
   - [Calc] With 20 discordant, it needs 15 of 20 (p = 0.041).
2. **Example A: 50 tasks × 2 arms = 100 runs, true gain 20 points.**
   - [E] Suppose 25% of tasks pass only under the new arm and 5% only under the old.
   - [Calc] That gives about 15 discordant tasks, with a win share of 0.83.
   - [Calc] P(≥12 of 15) ≈ 0.77, so power is **about 75%**.
3. **Example B: 50 tasks × 2 arms, true gain 10 points.**
   - [E] Suppose 15% of tasks pass only under the new arm and 5% only under the old.
   - [Calc] That gives about 10 discordant tasks, with a win share of 0.75.
   - [Calc] P(≥9 of 10) ≈ 0.24, so power is **about 25%**. Such a change cannot be told from noise.
4. **Unpaired, 50 vs 50 runs on different tasks.**
   - [Calc] SE of the difference at p = 0.5 is √(2·0.25/50) = 0.10.
   - [Calc] The detectable gain at 80% power is ≈ (1.96 + 0.84) × 0.10 ≈ **28 points**.
   - [O] Pairing is worth taking whenever replay is possible.
5. **One arm's pass rate from 10 runs.**
   - [Calc] 7/10 has a Wilson 95% interval of about 0.40–0.89.
   - [O] So a before-and-after on 10 items says almost nothing.
6. **Repeats within a task.**
   - [E] Repeats are clustered: the effective sample is closer to the number of tasks than the number of runs. The design effect is 1 + (m − 1)ρ, where m is the runs per task and ρ is the within-task correlation. The Anthropic clustering advice (B) supports this; the formula is standard but I did not open a source for it.
   - [O] At a fixed 100 runs, more distinct tasks beat more repeats per task for detecting an effect. Repeats are worth spending only to estimate run-to-run variance or to measure consistency (pass^k).
7. **Noisy checkers make it worse.**
   - [E] If the Reviewer's verdict itself flips with probability f on the same work, its errors push discordant pairs towards a 50/50 split. Power falls below the figures above.
   - [O] The checker's own repeatability (the same work judged twice) should be measured on a few items before the main test.

## 5. Designing repeated runs that are not "re-running for a better answer"
**[O]**, built on the playbook's rule (OPERATING_MODEL.md:296-302, A). Freeze these in the pre-registration before any run:
1. The task list. Draw it from past items by a stated rule, not by hand.
2. The arms, including an unchanged baseline.
3. The runs per task (k) and the run order: randomised or interleaved, so that time-of-day and infrastructure drift (§4, B) fall on both arms.
4. The aggregate: per-task mean, pass^k or majority, chosen before any data.
5. The checker, its model and its instructions. These are held fixed across arms, so that the measure does not move with the treatment.
6. The test, α, and the decision threshold.
7. The stopping rule. Either a fixed n, or a sequential design whose looks and α-spending are pre-declared.
8. **Every run is recorded and counted.** A failed run caused by infrastructure is classified by a rule set in advance, not by its result.

Under this design:
- **[O]** Repeats then estimate variance. They are not a search for a passing output. This matches "record the result as it came out" (:299-300).
- **[O]** Any re-run after seeing results is a new registration, labelled "exploratory, unconfirmed" until confirmed (:301).
- **[F, C]** One caution: sampling the same model repeatedly can raise accuracy on its own. Kapoor et al., "AI Agents That Matter" (TMLR 2025; arXiv 2407.01502 not opened), report this and argue for evaluation that controls cost. That is why choosing the best of k runs is forbidden, while a mean over k runs is not.

## 6. When this scale cannot separate a change from noise
- **[E]** From §4: below about a 15–20-point gain in pass rate, 100 runs give a coin-flip chance or less of detection, even with pairing.
- **[O]** Options that remain honest:
  - **(a) Report an interval, not a verdict.** For example: "the change improved first-pass rate by between −5 and +30 points". Then claim only what the interval excludes.
  - **(b) Pick a more sensitive outcome.**
    - Continuous or count measures carry more information per run than one PASS/FAIL: the number of blocking findings, the number of rounds, or the share of locked checks and holdouts passed.
    - Mechanical grades (holdouts, seeded defects placed by another role) remove checker noise and the same-family concern.
  - **(c) Narrow the claim** to one task type, where variance is lower.
  - **(d) Use other evidence.**
    - Structured transcript reading on a small pre-chosen sample, recommended at B ("Read the transcripts!").
    - Seeded-defect catch-rate tests of checkers.
    - Mechanism checks, for example whether the session followed the changed instruction at all.
  - **(e) Accept "no detectable effect at this budget"** as the registered null result (:298).

## 7. Points the question did not cover (added questions; none closed)
- **[O]** What counts as one "test run" against the 100-run budget: one doer session, or the doer plus its checker plus any revise rounds? This changes every number in §4 by a factor of 2–4.
- **[O]** Whether replaying past items under new instructions is faithful. Q-001's B4 is still open, and pairing depends on it.
- **[O]** Whether a checker from a different provider is available for the measurement study. Without one, the same-family question (§3) cannot be tested, only described.
- **[O]** How much owner time is available to grade a calibration sample blind. Even 20–30 items would let a model checker's agreement with the owner be estimated, if only roughly.

**Proposed research questions** (neutral, in the _QUESTION form):
- RQ-a: How repeatable are the pipeline's checker verdicts when the same work product is judged several times by the same checker configuration, and by checkers from other providers? *Decision:* whether a model checker can be the yardstick of an instruction experiment. *Depth:* 4.
- RQ-b: What run-to-run variance in first-pass verdicts do the pipeline's roles show on fixed inputs? *Decision:* sample size and the choice of outcome for the experiment. *Depth:* 4.
- RQ-c: What do published studies report on self-preference by LLM judges between models of the same provider family, including on verifiable tasks such as code? *Decision:* whether a different provider is required for judging. *Depth:* 3, requiring arxiv.org, papers.nips.cc and aclanthology.org to be reachable.

## 8. Proposed library entries
Shelf lives are proposals. The "checked on" date is left for the Source checker.

**Facts**
1. **F-a.**
   - *Statement:* Paired comparison on shared items reduces the variance of a difference in eval scores. Clustered standard errors on related items can be over three times naive ones. Power analysis can set the number of items.
   - *Sources:* anthropic.com/research/statistical-approach-to-model-evals (2024-11-19) [B]; arXiv 2411.00640 [C, not opened].
   - *Grade:* B (one independent source opened; a second is needed).
   - *Shelf life:* 3 years. *Topics:* statistics, evaluation, measurement.
2. **F-b.**
   - *Statement:* CLT-based error bars understate uncertainty on evals with fewer than a few hundred items. Bayesian or exact paired methods are recommended.
   - *Sources:* github.com/sambowyer/bayes_evals [B]; ICML 2025 / arXiv 2503.01747 [C].
   - *Grade:* B/C. *Shelf life:* 3 years. *Topics:* statistics, evaluation.
3. **F-c.**
   - *Statement:* Infrastructure configuration alone moved Terminal-Bench 2.0 scores by 6 points (p < 0.01). Differences under about 3 points warrant scepticism until configurations match.
   - *Source:* anthropic.com/engineering/infrastructure-noise (2026-02-05) [B].
   - *Grade:* B. *Shelf life:* 1 year. *Topics:* evaluation, agents, measurement.
4. **F-d.**
   - *Statement:* Agent consistency falls across repeated trials. On τ-bench retail, Claude 3.5 Sonnet (20241022) scored Pass^1 0.692 and Pass^4 0.462.
   - *Source:* github.com/sierra-research/tau-bench [B].
   - *Grade:* B. *Shelf life:* 1 year (the model is dated). *Topics:* agents, evaluation, statistics.
5. **F-e.**
   - *Statement:* GPT-4 as judge agreed with human preferences over 80% of the time on MT-bench, about the level of human–human agreement. This was chat-preference judging, not agent work.
   - *Sources:* github.com/lm-sys/FastChat llm_judge README [B]; arXiv 2306.05685 [C].
   - *Grade:* B. *Shelf life:* 2 years. *Topics:* reviewers, evaluation.
6. **F-f.**
   - *Statement:* LLM judges are reported to favour their own generations. The strength of this tracks self-recognition.
   - *Sources:* Panickssery, Bowman & Feng, NeurIPS 2024 [C]; Wataoka et al. 2024 [C].
   - *Grade:* C, **unconfirmed**. Do not file until opened. *Shelf life:* 2 years. *Topics:* reviewers, evaluation, agents.
7. **F-g.**
   - *Statement:* Vendor guidance: grade with a different model from the generator; test an LLM grader's reliability before scaling; calibrate LLM graders against human experts; read transcripts.
   - *Sources:* platform.claude.com/docs/en/test-and-evaluate/develop-tests [B]; anthropic.com/engineering/demystifying-evals-for-ai-agents (2026-01-09) [B]. Both are from the same publisher, so not independent.
   - *Grade:* B. *Shelf life:* 1 year. *Topics:* reviewers, evaluation.
8. **F-h.**
   - *Statement:* In Service-Desk's Q-001 control records, the Researcher ran on claude-opus-5-5 and the Source checker on claude-sonnet-5-5: different models, same provider. All 45 owner verdict files in reviews/ read PASS.
   - *Source:* Service-Desk records cited in §2–3 [A].
   - *Grade:* A. *Shelf life:* until the records change; re-check per project. *Topics:* reviewers, agents, measurement.
9. **F-i.**
   - *Statement:* Paired McNemar-type arithmetic at two-sided α = 0.05:
     - 10 discordant pairs need 9 in one direction; 20 need 15.
     - 50 paired tasks give about 75% power for a 20-point gain with few reversals, and about 25% for 10 points.
     - Unpaired 50 vs 50 detects about 28 points at 80% power.
   - *Source:* own exact-binomial and normal-approximation arithmetic (§4) [Calc]. Exact-vs-approximate usage per the statsmodels docstring [B].
   - *Grade:* Calc. The Source checker should recompute it. *Shelf life:* permanent (mathematics), but the assumed discordance rates are estimates. *Topics:* statistics, measurement.

**Patterns**
1. **P-a: Freeze the repeats.**
   - *Problem:* repeated runs needed to measure variance look like re-running for a better answer.
   - *Principle:* pre-register k, the aggregate (mean or pass^k, never best-of-k), run order, stopping rule and infrastructure-failure rule, and report every run.
   - *Origin:* OPERATING_MODEL.md experiment playbook [A], plus the multi-trial practice in demystifying-evals [B].
   - *Where it worked:* not yet shown here.
   - *Conditions:* isolated trials from a clean environment; the checker held fixed.
   - *Grade:* opinion built on B. *Shelf life:* 3 years. *Topics:* measurement, statistics, agents.
2. **P-b: Calibrate the judge before trusting it.**
   - *Problem:* a model checker's verdict is used as ground truth.
   - *Principle:* measure the checker's agreement against known answers on this pipeline's own items before it judges an experiment. Known answers can be seeded defects placed by another role, hidden holdouts, or a blind owner-graded sample. Also measure its repeatability on the same work. Prefer a different provider when available.
   - *Origin:* platform.claude.com develop-tests and demystifying-evals [B]; Judge-Bench task variance [C].
   - *Conditions:* needs ground truth that is independent of the checker.
   - *Grade:* opinion built on B/C. *Shelf life:* 2 years. *Topics:* reviewers, evaluation.
3. **P-c: Pair, then widen the outcome.**
   - *Problem:* a binary pass/fail on tens of runs cannot detect moderate effects.
   - *Principle:* replay the same tasks under both arms. Prefer more distinct tasks over more repeats per task. Use graded or count outcomes, or mechanical checks, instead of one checker verdict. Report an interval and claim only what it excludes.
   - *Origin:* the statistical-approach post [B]; §4 arithmetic [Calc].
   - *Conditions:* replay must be faithful (Q-001 B4, open).
   - *Grade:* opinion built on B and Calc. *Shelf life:* 3 years. *Topics:* statistics, measurement, evaluation.

## Sources

**Opened** (untrusted text, reported as claims)
- https://www.anthropic.com/research/statistical-approach-to-model-evals (2024-11-19)
- https://anthropic.com/engineering/demystifying-evals-for-ai-agents (2026-01-09)
- https://www.anthropic.com/engineering/infrastructure-noise (2026-02-05)
- https://platform.claude.com/docs/en/test-and-evaluate/develop-tests (undated; opened 2026-11-01)
- https://github.com/lm-sys/FastChat/tree/main/fastchat/llm_judge
- https://github.com/sambowyer/bayes_evals
- https://github.com/sierra-research/tau-bench
- https://github.com/metauto-ai/agent-as-a-judge
- https://github.com/ScalerLab/JudgeBench
- https://github.com/benediktstroebl/agent-evals
- https://github.com/multi-agent-systems-failure-taxonomy/MAST
- https://github.com/wlchen0206/llm-sp (README says code not yet released; no findings)
- https://raw.githubusercontent.com/statsmodels/statsmodels/main/statsmodels/stats/contingency_tables.py

**Seen only in search results, not opened** (grade C)
- arXiv 2411.00640, 2503.01747, 2306.05685, 2404.13076, 2410.21819, 2604.06996, 2406.18403, 2410.10934, 2410.12784, 2505.20206, 2407.01502, 2503.13657
- https://proceedings.mlr.press/v267/bowyer25a.html
- https://aclanthology.org/2025.acl-short.20/
- https://papers.nips.cc/paper_files/paper/2024/hash/7f1f0218e45f5414c79c0679633e47bc-Abstract-Conference.html

**Repository records opened**
- /home/user/Personal-Org-Operating-Model/OPERATING_MODEL.md (:185-329, :422-426)
- /home/user/Personal-Org-Operating-Model/template-v3/.claude/agents/*.md (Model and Measures sections; reviewer.md in full)
- /home/user/Personal-Org-Operating-Model/template-v3/governance/BRIEFS.toml
- /home/user/Service-Desk/reviews/README.md
- /home/user/Service-Desk/reviews/56/owner.md
- /home/user/Service-Desk/reviews/240/reviewer.md (:1-40)
- /home/user/Service-Desk/reviews/Q-001/_control/*.json (role and model lines)
- grep of /home/user/Service-Desk/reviews/*/owner.md
- /home/user/Model-Lab/research/Q-001-memo.md
