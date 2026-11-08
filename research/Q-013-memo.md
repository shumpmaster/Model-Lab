# Q-013 memo: what few-run trials of a process change can show (Researcher, 2026-11-08; revised after source check round 1)

*The Researcher's memo for Q-013, round 2 (brief 169, docs/briefs/169-researcher.md), revised after the Source checker's round 1 (research/Q-013-source-check.md); round 1 was brief 156, in this file's history. Recorded verbatim by the Orchestrator (session_01QBwHGNSLmSrYQgS6BPjV8p), 2026-11-08, from the helper's return; only this italic line is the Orchestrator's, replacing round 1's.*

**Answer as far as the evidence goes.** With one to a few tens of runs, a trial can reliably find only large effects. Two things are done under my own stated assumptions (Calc, below): a paired comparison of 10 runs detects, at 80% power, a difference of roughly one standard deviation of the run-to-run differences, and 20 runs detect about two-thirds of one. For pass/fail work, the library's McNemar arithmetic (Q-003-F-i) gives two figures, both resting on assumed discordance rates:
- about 0.70–0.77 power for a 20-point gain at 50 paired tasks, assuming 25% of tasks pass only under the new arm and 5% only under the old;
- about 0.25 for a 10-point gain, assuming 15% and 5%.

Below that level the trouble goes beyond missing real effects. The results that do come out significant often overstate the effect and sometimes have the wrong sign (Gelman & Carlin). A significant result is also less likely to be real (Button et al.), especially where most changes fail. Larsen et al. report that more than half of ideas fail, and that in some domains 90% or more of experiments fail, counting bad ideas and buggy implementations together.

Pairing each run with its own control reduces the variance of the difference (library Q-003-F-a, B, single origin). That it is the largest gain available is my opinion. Two practices keep the nominal false-result rate honest:
- **A frozen plan.** Undisclosed flexibility, including choosing measures or re-running, raises false positives far above 5% (Simmons et al.; Gelman & Loken). In one experiment, random seed alone produced statistically different distributions of results (Henderson et al., who measure no false-positive rate).
- **Either no repeated looks or a pre-declared sequential rule.** Five uncorrected looks raise 5% to 14% (Lakens). Pocock, O'Brien-Fleming, SPRT or always-valid p-values control it.

On Bayesian methods and peeking, the sources agree about purely subjective priors: Bayesian updating then does not depend on the stopping rule. They disagree about default or pragmatic priors. There, the resilience to optional stopping "can break down" (de Heide & Grünwald), though not for every default prior: their "Type 0" priors are fine. A blogger's simulation of a fixed posterior threshold with peeking gave 80% false positives. In small-sample Bayesian SEM, default priors can also act as highly informative priors. Single-case and crossover designs can work, but serial correlation and carryover cut their power sharply.

On whether trials may run at the same time, the evidence is thin and comes from huge-scale web A/B testing. There, interactions were rare, but they could not have been found at few-run scale. Factorial designs are a deliberate way to run several changes at once. An eval vendor advises one change at a time.

I found no evidence on what a trial costs, other than one vendor's illustrative figures. I also found no evidence specific to process trials in organisations or agent workflows. Nearly everything transfers from psychology, medicine, web A/B testing and ML benchmarking.

---

## 1. What size of effect few runs can detect, and the chance of a false result

- **Paired t-test power.** One example gives about 0.4 power at n=10 and 0.72 at n=20 for its stated difference; it judges 20 or fewer runs inadequate for that difference. A pingouin example detects d≈0.66 at n=20 with 80% power.
  - Minitab example: Fact. Grade B. F013-1, https://support.minitab.com/minitab/help-and-how-to/statistics/power-and-sample-size/how-to/hypothesis-tests/power-and-sample-size-for-paired-t/interpret-the-results/key-results
  - Pingouin example: Fact. Grade: assumed (search-only).
  - Stake: Minitab sells statistics software.
  - The raw-unit figure needs the example's SD before it means anything, and the page does not give it.
- **My own calculation.** Paired t-test, two-sided alpha 0.05, 80% power. The minimum detectable effect, in SDs of the paired differences, is about (1.96+0.84)/√n, plus a small-sample t correction:
  - n=10: about 0.9–1.0
  - n=20: about 0.63–0.66
  - n=30: about 0.51–0.53
  - Estimate (Calc). It assumes independent runs and normal differences. The n=20 figure agrees with the pingouin extract (F013-1). The Source checker should recompute it.
- **Pass/fail work (library, not re-researched).** 10 discordant pairs need 9 in one direction to be significant, and 20 need 15. At 50 paired tasks, power is about 0.70–0.77 for a 20-point gain (assuming 25% and 5% discordance) and about 0.24–0.25 for a 10-point gain (assuming 15% and 5%). Unpaired 50 against 50 detects about 28 points.
  - Fact. Library Q-003-F-i, strong (Calc), with the discordance rates as assumptions.
- **A practitioner's pass-rate calculation.** A 100-example eval detects about a 15-point difference, and a paired (McNemar) design needs "an order of magnitude fewer examples" than two independent arms.
  - Fact (practitioner calculation). Grade B. F013-5, https://dev.to/gabrielanhaia/eval-set-sizing-the-statistical-power-math-behind-llm-ab-tests-4gpc
  - The quote came through a fetch tool and the year is not shown. "Order of magnitude" depends on how correlated the arms are, so I treat it as an opinion on magnitude.
  - The direction agrees with library Q-003-F-a (B, single origin).
- **Low power has two costs.** It lowers the chance of finding a real effect, and it lowers the chance that a significant result is real; it also inflates effect estimates.
  - Fact. Grade B. F013-2, Button et al. 2013, https://research-information.bris.ac.uk/en/publications/power-failure-why-small-sample-size-undermines-the-reliability-of/
  - **Disagreement:** a published reply argues that the size of the reliability loss depends on the unknown share of true effects (search-only, nrn3475-c5).
- **Wrong sign and exaggeration.** In small, noisy studies a significant estimate can have the wrong sign (Type S) or exaggerate the effect (Type M). Exaggeration becomes a problem below 0.5 power, and wrong signs below 0.1. The paper recommends design calculations based on effect sizes from outside the study.
  - Fact. Grade B. F013-3 and F013-4, https://sites.stat.columbia.edu/gelman/research/published/PPS551642_REV2.pdf (only pages 1–4 were opened).
- **Illustration of the false-result chance (my calculation, using Button et al.'s logic).** Take alpha 0.05 and power 0.3, which is typical of a few-run trial of a moderate effect.
  - If half the tried changes are real, about 86% of significant results are true.
  - If 10% are real, about 40% are true.
  - Estimate (Calc, illustrative). The 10% case uses the "90% or more" rate from F013-27 (B). That rate is for experiments that failed, from a combination of bad ideas and buggy implementation, not for ideas with no real effect. Reading it as "90% of changes have no real effect" is therefore an assumption. The rate also comes from web-scale experiment programmes, and whether it holds for process changes is unknown.
- **Run-to-run noise in agent and model evaluation.**
  - In 8 models with 3 runs each, a single run reversed at least one pairwise ranking in 10 of 12 slices. Two runs removed about 83% of those reversals, and pairwise significance conclusions never flipped.
    - Fact. Grade B. F013-6, https://arxiv.org/abs/2509.24086 (preprint; the figures come from the fetch tool's summary).
  - Agent run-to-run consistency (ICC) varies with the type of task. Estimates settle after 8–16 trials for structured tasks and 32 or more for complex reasoning.
    - Fact. Grade B. F013-7, https://arxiv.org/abs/2512.06710 (preprint; affiliations not checked).
  - Library Q-009-F4-2 (B): single-run agent benchmark results vary by 2.2–6.0 points depending on which run is selected.
  - Transfer: these are model evaluations, not process changes on an organisation's own work. They do show that noise from a single run is large in agent work.
- **Gap.** No study measures how often few-run trials of organisational process changes give wrong answers.

## 2. What a trial costs

- **The only figures found are a vendor's illustration.** A team of about €500k a year plus €100k of tooling barely pays back. One example test needs 830k visitors and two months.
  - Fact (a vendor's illustrative figures). Grade B. F013-26, https://www.levered.dev/blog/why-ab-testing-fails-for-smbs-and-what-to-do-instead
  - **Stake:** Levered sells the alternative it recommends.
  - **Disagreement:** practitioners say low-traffic sites can still test bigger changes (search-only).
  - Transfer: web traffic economics, not staff-time trials. Very weak transfer.
  - Note for the Source checker: the Input reader's cost gap note calls this finding "F013-23". The finding that holds the euro figures is F013-26.
- **Indirect evidence on the value side.** More than 50% of ideas fail in general. In some domains, 90% or more of experiments fail, from a combination of bad ideas and buggy implementation. Most positive changes are small, so experiments struggle for adequate power.
  - Fact. Grade B. F013-27, https://ar5iv.labs.arxiv.org/html/2212.11366
  - Stake: some authors are industry experimentation practitioners.
- **Sequential designs can lower the expected cost.** They need fewer participants on average (Lakens, F013-13, B). The SPRT has the smallest average sample number for its error rates (F013-17, assumed search-only). The "40–60% saving" figure comes from a vendor calculator (search-only) and should not be used.
- **Opinion.** The per-run cost of a trial on an organisation's own work is mostly the work itself, done k times under each arm, plus checker time. None of the sources measure this.
- **Gap.** There is no independent costing of staff time, delay or compute. The question is answered only by inference, and the cost of the organisation's own runs would have to be measured, not researched.

## 3. Designs available for so few runs

- **Paired, crossover and N-of-1 designs.**
  - Crossover designs need fewer subjects when within-subject variation is small. Carryover, period effects and dropouts can make the data "nearly useless". Two-stage carryover tests "seem to have been discredited" (Senn), and "efficiency is often a mirage".
    - Opinion and fact from a practitioner poster. Grade B. F013-23, https://support.sas.com/resources/papers/proceedings/proceedings/sugi24/Posters/p221-24.pdf (1999; pages 1–2 opened).
  - An N-of-1 crossover simulation with 400 observations and a 0.3 SD effect gave 0.85 power with no serial correlation. With serial correlation 0.75, a single-period design fell to 0.13 power. 40 periods per intervention (80 in all) recovered it to 0.68. Power to detect carryover was weak.
    - Fact. Grade B. F013-22, https://pmc.ncbi.nlm.nih.gov/articles/PMC6787650/
    - Transfer: consecutive pieces of an organisation's work done by the same people or agents are plausibly serially correlated, so alternating arms often matters. This transfer is an opinion.
- **Single-case designs (WWC standards).**
  - A case acts as its own control. The 2010 pilot standard requires three demonstrations of the effect, at least four A/B phases, and at least 5 data points per phase to meet standards (3 to meet them with reservations). With a basic AB design, valid causal inference is "difficult". The panel itself says the three-demonstrations rule has "no formal basis" and is a conceptual norm.
    - Fact. Grade B. F013-21, https://ies.ed.gov/ncee/WWC/Docs/ReferenceResources/wwc_scd.pdf (2010 pilot version; pages 1–6).
  - CEC's research division disputes the 5-data-point minimum (search-only).
  - Library Q-009-F4-5 (B): only 4 of 115 medical N-of-1 studies met WWC standards.
- **Sequential and adaptive designs.**
  - Pocock and O'Brien-Fleming boundaries or alpha spending control error across looks and need fewer participants on average. Estimates from a trial that stops early overstate the effect.
    - Fact (an established method). Grade B. F013-13, https://lakens.github.io/statistical_inferences/10-sequential.html
  - Always-valid p-values (mSPRT) allow stopping at any time while controlling Type I error, and let users trade off sample size and power efficiently.
    - Fact. Grade B. F013-16, https://arxiv.org/abs/1512.04922
    - Stake: authors are linked to Optimizely (search-only).
  - SPRT optimality: F013-17, assumed (search-only).
- **Small-sample Bayesian methods.**
  - These are not a quick fix. In Bayesian structural equation modelling (SEM) with small samples, default priors can act as highly informative priors. The paper advises priors drawn from previous research or from thought about which values are implausible, together with a sensitivity analysis.
    - Fact and opinion. Grade B. F013-24, https://www.frontiersin.org/articles/10.3389/fpsyg.2020.611963/full
    - The same point is attributed to McNeish 2016 (search-only).
    - Transfer: the source's setting is SEM. Applying it to simpler few-run comparisons is my opinion.
  - A trade press summary (14 January 2026) of FDA draft guidance says Bayesian methods "may be especially valuable in rare disease and pediatric trials". It makes the point about using prior or external data in a separate sentence.
    - Fact about a summary. Grade B. F013-25, https://appliedclinicaltrialsonline.com/view/fda-issues-draft-guidance-advance-bayesian-methods-clinical-trials
    - The FDA text was not opened, and it is a draft.
    - Transfer: where the gain comes from prior or external data, it depends on having trustworthy prior data, which for a new process change an organisation usually lacks. This is an opinion.
- **Gap.** No head-to-head comparison of these designs at n of 1–30 was found. The comparison above is put together from separate sources (opinion).

## 4. Frozen plan, re-running until a better answer, and repeated looks

- **Re-running and selection.**
  - In one experiment (TRPO on HalfCheetah-v1), ten RL runs that differed only in random seed were split into two groups of five, and the groups gave "statistically different distributions". Selecting the top-N trials, or averaging fewer than 5 runs, was common and misleading. The paper measures no false-positive rate.
    - Fact. Grade B. F013-8, https://ar5iv.labs.arxiv.org/html/1709.06560
  - Undisclosed flexibility, including optional stopping and choice of measures, raises real false-positive rates far above 5%.
    - Fact. Grade B. F013-9, https://stafforini.com/works/simmons-2011-falsepositive-psychology-undisclosed/
    - Only a third-party copy of the abstract was opened.
  - A multiple-comparisons problem arises even with a single analysis if the analysis choices depend on the data.
    - Fact (argument). Grade B. F013-10, https://sites.stat.columbia.edu/gelman/research/unpublished/p_hacking.pdf (working paper; page 1 opened).
  - Library Q-003-P-a (opinion-grade pattern): pre-register k, the aggregate (never best-of-k), the run order and the stopping rule, and report every run.
- **Does a frozen plan help in practice? The sources disagree.**
  - Registered Reports, whose plans are peer-reviewed before data, had 44% positive results against 96% in standard reports (71 against 152 papers).
    - Fact. Grade B. F013-18, https://www.psychologicalscience.org/journals/ampps/25152459211007467/
    - A search extract says the authors do not claim this proves the format reduces bias.
  - 193 preregistered studies, compared with 193 related studies, did not have fewer positive results, smaller effects or fewer errors. They had more power analyses and larger samples, and there was no robust evidence that preregistration prevents p-hacking.
    - Fact. Grade B. F013-19, https://research-portal.uu.nl/en/publications/preregistration-in-practice-a-comparison-of-preregistered-and-non/
  - Reconciliation (opinion): a plan that is reviewed and binding (F013-18) may differ from a plan that is only filed (F013-19).
  - Critics argue that preregistration does not fix the underlying problems.
    - Opinion. Assumed (search-only). F013-20.
  - Transfer: all from psychology. There is no evidence specific to software or agent work.
- **Repeated looks.**
  - Stopping at the first significant result gave 26.1% false positives in one example, against a nominal 5%; a fixed sample size avoids this.
    - Fact. Grade B. F013-11, https://www.evanmiller.org/how-not-to-run-an-ab-test.html
    - The author's link to A/B tools was not checked.
  - Uncorrected looks raise alpha to 0.142 after 5 looks, 0.374 after 100 and 0.530 after 1000.
    - Fact. Grade B. F013-13, citing Armitage et al. 1969.
    - Transfer: for a few-run trial, even 3–5 informal looks matter.
- **Bayesian monitoring: the sources disagree.**
  - Miller's page (F013-11) and Etz summarising Rouder (F013-14, B) say optional stopping does not affect the interpretation of posterior odds. https://alexanderetz.com/2016/03/06/sunday-bayes-optional-stopping-is-no-problem-for-bayesians/ ; Rouder's original was not opened.
  - De Heide & Grünwald agree for purely subjective priors: Bayesian procedures then "do not depend on the stopping rule". They say the resilience "can break down" with default or pragmatic priors, and they separate default priors that are "no-problem-at-all" (Type 0) from those that are not.
    - Fact. Grade B. F013-15, https://ar5iv.labs.arxiv.org/html/1708.08278 (read in part).
  - A blogger's simulation found that a fixed posterior threshold with peeking gave 80% false positives.
    - Fact (practitioner simulation). Grade B. F013-12, https://www.alexmolas.com/2025/10/30/bayesian-ab-test-peeking.html
  - Reading (opinion): the two sides answer different questions. One is the coherence of the posterior; the other is the frequency of false decisions.

## 5. Other changes made to the same work at the same time

- **Interactions at huge scale were rare.** Microsoft ExP found interactions between concurrent tests in 0.002% of test-pair metrics in one of four products, and none in three. It isolates tests only when it suspects an interaction, because isolation costs power, and it concedes that some interactions may have gone undetected for lack of power.
  - Fact. Grade B. F013-28, https://www.microsoft.com/en-us/research/articles/a-b-interactions-a-call-to-relax/
  - **Stake:** Microsoft runs this platform.
  - **Transfer is poor:** the setting is hundreds of tests on millions of users with randomised overlap. A few-run trial has neither the randomisation of overlap nor the power to see an interaction.
- **Library (not re-researched).**
  - Q-009-F8-5 (B, vendor): overlapping tests rarely collide.
  - Q-009-F8-6 (C, CXL): avoid overlapping traffic when judging a single test.
  - Q-009-F8-7 (C): parallel experiments can interact negatively.
  - Q-009-F8-8 (B, Google SRE): simultaneous overlapping canaries risk contaminating each other's signal.
  - Q-009-F8-4 (B, vendor): small prompt cohorts are only directional.
  - These already disagree among themselves.
- **Factorial designs vary several changes at once on purpose.** They need fewer subjects than one experiment per factor (about k times fewer) and can estimate interactions.
  - Fact (an established method). Grade B. F013-28b, https://pmc.ncbi.nlm.nih.gov/articles/PMC2796056
  - The PDF was read in part, and the Table 5 figures were not seen directly. The "(k+1)N/2" comparison in the Input reader's note should be re-checked against the paper.
  - Transfer: behavioural science. It requires that each run be randomly assigned to a combination of changes. Changes that are simply rolled out together are confounded.
- **One change per experiment.** An eval vendor advises this because simultaneous changes cannot be attributed. It also says a single run can make a bad change look good.
  - Opinion (vendor guidance). Grade B. F013-28c, https://docs.braintrust.dev/evaluate/best-practices.md
  - Stake: Braintrust sells eval tooling.
  - **It disagrees with F013-28b** unless the simultaneous changes are crossed by design.
  - Frey & Jugulum report that one-factor-at-a-time designs sometimes exploit interactions better than orthogonal arrays (search-only).
- **Opinion.** Overlapping trials fall into two kinds that the sources treat differently:
  - **Crossed by design:** each run randomly assigned to each change. This is a factorial; it is valid and can be efficient.
  - **Uncontrolled:** two changes land on the same work over the same period. This confounds both.
- **Gap.** No evidence on concurrent trials in agent or organisational workflows.

## What each answer would change (as Q-013 puts it; not a recommendation)

- **If few-run trials cannot separate real effects from noise,** adoption rests on whatever other evidence there is. The evidence fits this reading for small effects: below roughly 0.5 SD at 20–30 paired runs, or below about 20 points on pass/fail work at tens of tasks (under the assumed discordance rates). Significant results there are also likely to be exaggerated.
- **If they can separate only large effects, or only in some designs,** a trial can gate only changes expected to matter that much. The evidence fits this reading best:
  - effects of about 1 SD at about 10 paired runs, or about 0.65 SD at 20;
  - paired or alternating designs with a frozen plan;
  - a fixed number of runs or a pre-declared sequential rule.
  - Outside this reading fall: single-period or AB designs, uncorrected peeking, and Bayesian stopping with default or pragmatic priors, where the resilience to optional stopping can break down.
- **If they can,** a trial can serve as the gate. No source shows this for effects of ordinary size at few runs.
- **On simultaneous changes,** the evidence separates two cases:
  - Changes crossed by randomised design may run together (factorial, F013-28b).
  - Uncontrolled overlapping changes on the same work confound each other (F013-28c; library F8-6 and F8-8).
  - Evidence that interactions are rare comes only from web scale (F013-28) and does not show they are rare at few runs.
  - Which policy follows is for the decision-maker.

## Proposed library entries (statement | type | grade | proposed shelf life)

1. Small, noisy studies give significant estimates of exaggerated size (power below 0.5) or the wrong sign (power below 0.1); design calculations should use effect sizes from outside the study (Gelman & Carlin 2014) | fact | B | 10 years
2. Low power lowers both the chance of detecting a real effect and the chance that a significant result is real (Button et al. 2013); disputed on dependence on prevalence | fact | B | 10 years
3. Uncorrected repeated looks raise a nominal 0.05 alpha to 0.142 after 5 looks; group-sequential boundaries or alpha spending control it, and early-stop estimates overstate effects (Lakens, citing Armitage 1969) | fact | B | permanent (mathematics)
4. Always-valid p-values (mSPRT) permit continuous monitoring with Type I error control and let users trade off sample size and power efficiently (Johari, Pekelis & Walsh); stake: Optimizely | fact | B | 10 years
5. With purely subjective priors, Bayesian procedures do not depend on the stopping rule. With default or pragmatic priors, resilience to optional stopping can break down, though "Type 0" default priors are fine (de Heide & Grünwald). Rouder, via Etz, says optional stopping is no problem | fact | B | 10 years
6. In small-sample Bayesian SEM, default priors can act as highly informative priors; use priors from previous research or from thought about implausible values, with a sensitivity analysis (Smid & Winter 2020) | fact | B | 10 years
7. Registered Reports had 44% positive results against 96% in standard reports (Scheel et al. 2021), but preregistered studies compared with related studies showed no fewer positive results (van den Akker et al. 2024): the sources disagree | fact | B | 5 years
8. Undisclosed analytic flexibility, including optional stopping, raises false-positive rates far above 5% (Simmons et al. 2011) | fact | B | 10 years
9. In one RL experiment (TRPO, HalfCheetah-v1), two groups of five runs that differed only in random seed gave statistically different distributions; top-N selection is misleading (Henderson et al.) | fact | B | 5 years
10. In N-of-1 crossover designs, serial correlation sharply cuts power (0.85 to 0.13 at r=0.75), and 40 periods per intervention partly recover it (0.68) (Wang & Schork 2019) | fact | B | 10 years
11. The WWC single-case "three demonstrations" rule has no formal basis by the panel's own account; the 2010 pilot requires at least 5 data points per phase (3 with reservations), and basic AB designs make valid causal inference difficult (Kratochwill et al. 2010) | fact | B | 10 years
12. Microsoft ExP found interactions between concurrent A/B tests rare (0.002% of pair-metrics in one of four products) at web scale, with possible undetected interactions; stake: own platform; not for few-run settings | fact | B | 3 years
13. Factorial designs need fewer subjects than one experiment per factor and can estimate interactions (Collins, Dziak & Li 2009) | fact | B | permanent (method)
14. Minimum detectable paired effect at alpha 0.05 and 80% power is about 0.9–1.0 SD of differences at n=10, 0.63–0.66 at n=20 and 0.51–0.53 at n=30, assuming independent, normal differences | fact (calculation) | Calc, to be recomputed by the Source checker | permanent for the mathematics
15. Pattern: gate a change by a few-run trial only if the expected effect is at least the design's minimum detectable effect; pair or alternate the runs, freeze k, the measure and the stopping rule (fixed, or a declared sequential boundary), and report every run | pattern | opinion built on B sources plus library Q-003-P-a, Q-003-F-a and Q-003-F-i | 3 years
16. Pattern: let trials overlap only when crossed by randomised (factorial) assignment; otherwise run them in turn | pattern | opinion built on B sources (F013-28b, F013-28c) plus library F8-6 and F8-8; the sources disagree | 3 years

## Finding ids relied on (for the Source checker)

- **Opened by the Input reader:** F013-2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 21, 22, 23, 24, 25, 26, 27, 28, 28b, 28c
- **Opened by the Source checker, round 1:** F013-1 (the Minitab page; now B)
- **Search-only, so assumed:** the F013-1 pingouin extract, F013-17, F013-20, and the sub-notes under F013-2, 11, 17, 21, 24, 26, 27, 28c
- **Library:** Q-003-F-a, Q-003-F-i, Q-003-P-a, Q-009-F4-2, F4-5, F8-4, F8-5, F8-6, F8-7, F8-8
- **Calc items to recompute:** minimum detectable effect by n (section 1); the PPV illustration (section 1)
- **Flags:**
  - The Input reader's cost gap note says "F013-23" where the euro figures are in F013-26.
  - F013-21 has no stake field.
  - Fetch-tool quotes need exact re-checking: F013-5, F013-6, F013-15, and the Table 5 figures in F013-28b.
- **Sources needed but not gathered:** Rouder 2014 (original); the FDA draft guidance text; the CEC position paper; any independent costing of trials; any study of few-run trials or concurrent changes in software or agent workflows. No level-5 expert or paid source is requested.

## Tokens
I cannot see my token count.

---

## Change list

| # | Item | What changed | Answers correction |
|---|---|---|---|
| 1 | Answer, Bayesian paragraph | The old line, "disagree only for purely subjective priors", was wrong. It now says the sources agree for purely subjective priors and disagree for default or pragmatic priors. It uses "can break down" and says Type 0 default priors are fine. | 1 |
| 2 | Section 4, F013-15 | "Breaks down" became "can break down". Added the subjective-prior quote and the Type 0 distinction. | 1 (and the F013-15 row) |
| 3 | Entry 5 | Restated the same way as item 2. | 1 |
| 4 | "What each answer would change", last point of the second reading | "Default-prior Bayesian stopping" became "default or pragmatic priors, where the resilience can break down". | 1 |
| 5 | Answer, pairing sentence | Now cites Q-003-F-a (B, single origin) for variance reduction only. "Largest gain available" is marked as my opinion. Q-003-F-a added to entry 15's basis. | 2 |
| 6 | Section 3, F013-21 | The 5-points-per-phase rule (3 with reservations) is now in the 2010 pilot itself. "Later versions" was removed. AB designs: "rarely supports" became "difficult". The CEC dispute is kept, still search-only. | 3 |
| 7 | Entry 11 | Restated the same way as item 6. | 3 |
| 8 | Section 3, F013-23 | "Are discredited" became "seem to have been discredited (Senn)". | 3 |
| 9 | Section 4, F013-8 | Removed "looked like different algorithms". Now: "statistically different distributions", in one TRPO/HalfCheetah-v1 experiment. Added that the paper measures no false-positive rate. | 4 |
| 10 | Answer, frozen-plan bullet | Henderson moved out of the "false positives far above 5%" claim into its own sentence, with the same caveat as item 9. | 4 |
| 11 | Entry 9 | Restated the same way as item 9. | 4 |
| 12 | Answer, Button/Larsen sentence | "Most ideas fail" became "most changes fail". The 90% is now experiment failure counting bad ideas and buggy implementations. | 5 |
| 13 | Section 1, PPV illustration | Added the caveat that the 90% includes buggy implementations, so reading it as a 90% no-effect share is an assumption. Still Estimate (Calc, illustrative). | 5 |
| 14 | Section 2, F013-27 | 90% reworded as experiment failure from bad ideas plus buggy implementation. | 5 |
| 15 | Section 3, F013-16, and entry 4 | "At some cost in sample size and power" became "trade off sample size and power efficiently". | 6 |
| 16 | Section 3, F013-24 | Bayesian SEM setting named. "Real prior information" became priors from previous research or from thought about implausible values. Transfer to simpler comparisons added, marked opinion. | 6 |
| 17 | Answer, F013-24 sentence, and entry 6 | Restated the same way as item 16. | 6 |
| 18 | Section 3, F013-25 | "Borrowing of prior data" replaced. The article's wording is Bayesian methods "may be especially valuable in rare disease and pediatric trials", with prior or external data in a separate sentence. Article date added. The transfer opinion is now conditional on the gain coming from prior data. | 6 |
| 19 | Section 4, F013-19, and entry 7 | "Matched pairs" / "matched preregistered studies" became 193 preregistered studies "compared with 193 related studies". | 6 |
| 20 | Section 3, F013-22, and entry 10 | "40 alternating periods" became "40 periods per intervention (80 in all)". | 6 |
| 21 | Answer, McNemar figures | The assumed discordance rates (25%/5% and 15%/5%) are now stated in the answer. Also added to section 1 and to the first reading in "What each answer would change". | 7 |
| 22 | Section 1, F013-1, and the "Finding ids relied on" lists | The Minitab page moved from assumed to B (the check confirmed it). The pingouin extract stays assumed. "I do not have the SD" became "the page does not give it". | 8 and the F013-1 row (move from assumed to B) |
| 23 | F013-17, F013-20, Button reply, Simmons body (optional stopping), Rouder 2014, Armitage 1969, FDA text | Unchanged. All still assumed or open. | 8 |

- **Stake notes:** the check marked none as unconfirmed, so none were dropped. The Optimizely link (F013-16) stays labelled search-only, as before.
- **Fact/estimate/opinion marks:** only the pairing claim (now opinion) and the F013-1 grade changed. The PPV illustration stays an illustrative estimate, with a stronger caveat.

## Finding ids for the Source checker to re-check

- **Findings:** F013-1 (the Minitab grade move), F013-8, F013-15, F013-16, F013-19, F013-21, F013-22, F013-23, F013-24, F013-25, F013-27.
- **Answer paragraph:** the Bayesian wording, the pairing sentence and the McNemar assumptions.
- **Library entries now cited in the answer:** Q-003-F-a and Q-003-F-i.
- **Proposed entries reworded:** 4, 5, 6, 7, 9, 10, 11 and 15.
- **Calc:** the PPV illustration's caveat.

## Tokens
I cannot see my token count.
