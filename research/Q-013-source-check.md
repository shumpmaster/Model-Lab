Verdict: PASS

*The Source checker's check of research/Q-013-memo.md. Each round on a different model from the Researcher; recorded verbatim by the Orchestrator (session_01QBwHGNSLmSrYQgS6BPjV8p) from the helper's return, 2026-11-08; each round's own verdict line is recorded as "The round's verdict was …" (LL-68). The verdict above is the latest round's.*

## Round 1 (brief 159)

The round's verdict was FAIL.

The numbers and most quotes hold. FAIL is for six places where the memo words a claim more strongly than its source, or gets it wrong (list at the end). Dates are 2026-11-08 for all opens. I opened URLs directly, and read the PDFs as text. Sources I could not open at all: the Button reply (nrn3475-c5, login redirect) and the Simmons paper body (403). Rouder 2014 was not opened and was not asked for.

## Finding ids

| id | mark | reason |
|---|---|---|
| F013-1 (Minitab) | confirmed; was assumed | Page says "approximately 0.4, 0.72, and 0.99" for n=10/20/50 at difference 3, and "20 or fewer ... not adequate". No SD is given. SD=5 reproduces it (my inference). Vendor (statistics software). Pingouin d=0.66 stays search-only, but my calculation gives 0.660. |
| F013-2 (Button) | confirmed (quotes exact) | The memo's inflation point is in the page's "overestimates of effect size". The reply dispute could not be opened, so it is not filed as fact. Second source: Gelman & Carlin, same direction. |
| F013-3 (Gelman & Carlin) | confirmed (quote exact) | Read the full PDF. "External" effect sizes is the page's word. |
| F013-4 | confirmed (exact) | The 0.5 and 0.1 thresholds have no second source. |
| F013-5 (dev.to) | confirmed (quotes exact) | Both "order of magnitude" and "roughly a 15-point delta" are on the page. Year not shown. 100 per arm at a 0.78 baseline gives 14 points. Practitioner opinion. |
| F013-6 (2509.24086) | confirmed | Matches the abstract via the arXiv API. The "10 of 12 slices" is measured against the three-run majority, which the memo omits. |
| F013-7 (2512.06710) | confirmed (exact via API) | Affiliations are not shown on arXiv. |
| F013-8 (Henderson) | partly confirmed | Top-N quote exact. "Statistically different distributions" is the page's wording; "looked like different algorithms" is not (same algorithm, TRPO on HalfCheetah-v1, one experiment). No venue on the page. |
| F013-9 (Simmons) | confirmed in substance | Abstract: "flexibility in data collection, analysis, and reporting dramatically increases actual false-positive rates". Only a third-party abstract was opened. Optional stopping is not in the abstract; an APS summary of the paper supports it, but that is not independent. |
| F013-10 (Gelman & Loken) | confirmed (exact) | Read the whole PDF, dated 14 Nov 2013. |
| F013-11 (Miller) | confirmed | 26.1% is for stopping as soon as significance is reached (or at 150 observations, 50% baseline). Stake: his own statistics software and a sample-size calculator. |
| F013-12 (Molas) | confirmed in substance | The 80% figure is the text's summary of peeking every 100 events (threshold 0.95, Beta(1,1) prior). The plot was not seen. |
| F013-13 (Lakens) | confirmed (exact) | 0.142, 0.374 and 0.530 all match. Armitage 1969 not opened. Page undated (2022 edition per the citation). |
| F013-14 (Etz) | confirmed (exact) | Rouder's original not opened. De Heide's abstract independently describes Rouder's claim. |
| F013-15 (de Heide & Grünwald) | partly confirmed | Abstract says "can break down" with default or pragmatic priors, and distinguishes Type 0 priors ("no-problem-at-all") from Type II. Subjective priors: "Bayesian procedures do not depend on the stopping rule" (Appendix A). The memo's "not with default or pragmatic priors" is stronger than the page. |
| F013-16 (Johari) | partly confirmed | "Wholly unreliable" is exact. Type I error control is in the introduction. The abstract says "tradeoff sample size and power efficiently", so the memo's "at some cost in sample size and power" is stronger than the page. Optimizely stake confirmed in the paper's own text. |
| F013-17 (SPRT) | not opened, stays assumed | Search-only. Not filed. |
| F013-18 (Scheel) | confirmed (exact) | 96% against 44%, N=71 against 152. The authors call reduced bias "a plausible factor", not proven. |
| F013-19 (van den Akker) | partly confirmed | 193 preregistered studies against "193 related studies". The abstract does not say "matched pairs". Everything else holds in the page's words. |
| F013-20 | not opened, stays assumed | Search-only. |
| F013-21 (WWC) | partly confirmed | "No formal basis ... conceptual norm" is exact. The four-phase rule is confirmed. AB designs: "difficult to draw valid causal inferences", not "rarely". The memo says "later versions require 5 data points per phase", but the 2010 pilot itself requires at least 5 per phase to meet standards (3 with reservations). |
| F013-22 (Wang & Schork) | confirmed in substance | Table 1: 0.851, 0.126 and 0.681. "40 alternating periods" is 40 periods per intervention (5 observations each, no washout), 80 in all. The abstract has none of these figures. |
| F013-23 (SAS poster) | partly confirmed | "Efficiency is often a mirage" and "nearly useless" are exact. The two-stage tests "seem to have been discredited (Senn)"; the memo says "are discredited". The "nearly useless" sentence is tied to dropouts and period effects. |
| F013-24 (Smid & Winter) | partly confirmed | The default-priors quote is exact, but the setting is Bayesian SEM, which the memo omits. The page allows priors from prior research or from thinking about implausible values, so "real prior information" is stronger than the page. |
| F013-25 (Applied Clinical Trials) | partly confirmed | Article dated 14 Jan 2026 and cites the FDA release of 12 Jan 2026. It says Bayesian methods "may be especially valuable in rare disease and pediatric trials". The prior-data/external-data point is a separate sentence, not "borrowing", which the article never says. FDA text not opened. An agent-directed HTML comment is present and was not followed. |
| F013-26 (Levered) | confirmed (exact) | €500k is team cost per year, €100k tooling, against €500k incremental revenue. The 830k visitors and two months example is hypothetical (400k a month, 1.5% conversion, 5% relative uplift). Vendor stake confirmed. The F013-23 / F013-26 mislabel flag is correct. |
| F013-27 (Larsen et al.) | partly confirmed | "More than 50% of ideas fail" is exact. The 90% is "the failure rate of experiments (due to a combination of bad ideas or buggy implementation)", not ideas alone. |
| F013-28 (Microsoft ExP) | confirmed (exact) | Four products, none in three, 0.002% in one ("1 in 50,000 A/B test pair metrics"). Independent random assignment, so the memo's "randomised overlap" holds. Isolation costs power, and the concession is exact. |
| F013-28b (Collins et al.) | confirmed (exact) | The memo's flagged "(k+1)N/2" is in the text as "(k + 1)(N/2)". The kN and (k+1)(N/2) comparisons are for a simple effect against the factorial's main effect. Table 5 was not seen and was not needed. |
| F013-28c (Braintrust) | confirmed (exact) | "Make one change per experiment." and "A single experiment run can make a bad change look good." Vendor, undated. An agent-directed documentation-index line is present and was not followed. |

Library entries checked in /home/user/portfolio/library. They match the memo: Q-009-F4-2 (2.2–6.0), F4-5 (4 of 115), F8-4 (B, Kiro vendor), F8-5 (B, Statsig vendor), F8-6 (C, CXL), F8-7 (C), F8-8 (B, Google SRE), Q-003-F-i (strong, Calc, with its discordance assumptions), Q-003-F-a (B, single origin), Q-003-P-a (opinion-grade). I did not re-verify Q-003-F-i's "50 against 50 detects about 28 points". My normal approximation gives 26.5 at a 50% baseline.

## Recomputations

Paired t, two-sided alpha 0.05, 80% power, noncentral t, minimum detectable d in SDs of the differences:

| n | exact t | (1.96+0.8416)/√n | memo range |
|---|---|---|---|
| 10 | 0.996 | 0.886 | 0.9–1.0 ✓ |
| 20 | 0.660 | 0.626 | 0.63–0.66 ✓ |
| 30 | 0.529 | 0.511 | 0.51–0.53 ✓ |

- The memo's lower bound is the normal approximation and its upper bound is the exact value.
- Exact power at d=0.9, n=10 is 0.717.
- Minitab consistency: difference 3 with SD 5 gives power 0.40, 0.72 and 0.99 at n=10, 20 and 50.
- Predictive value, alpha 0.05 and power 0.3: if 50% of changes are real, 0.15/(0.15+0.025)=0.857 ✓. If 10% are real, 0.03/(0.03+0.045)=0.400 ✓. The "10% are real" case equates "experiment failed" with "no effect", and F013-27's 90% includes buggy implementations, so it stays illustrative.
- Library McNemar arithmetic: 10 discordant pairs need 9, and 20 need 15 ✓. 50 tasks at 25% against 5% gives power 0.699 (0.768 for exactly 15 discordant tasks). 15% against 5% gives 0.241. 100 per arm at a 0.78 baseline detects 14 points, against the dev.to "roughly 15" ✓.

## Filed

Worktree /home/user/lib-q-013, branch build/source-checker/q-013, one commit (not pushed) by source-checker with the exact trailer paragraph.
- Facts: /home/user/lib-q-013/library/facts/Q-013-1.md to Q-013-14.md (memo entries 1–14, each reworded to the page).
- Patterns: /home/user/lib-q-013/library/patterns/Q-013-P15.md and Q-013-P16.md (memo entries 15 and 16, opinion-grade; P16 records that the sources disagree).
- 16 index rows appended at the end of /home/user/lib-q-013/library/README.md.
- Nothing was written outside library/.
- Left out of the entries: the Button reply dispute (unopened), "rarely" for AB designs, "looked like different algorithms", "real prior information", "at some cost in power", "matched pairs", and "largest gain available" for pairing.

## What the memo must correct

1. Answer paragraph: "the sources disagree only for purely subjective priors" is wrong. They agree for purely subjective priors (updating does not depend on the stopping rule), and disagree for default or pragmatic priors. Even there it is "can break down", and Type 0 default priors are fine.
2. "Pairing each run with its own control is the largest gain available" has no source. Mark it opinion, or cite the library Q-003-F-a (variance reduction) only.
3. F013-21: the 5-data-points-per-phase rule is in the 2010 pilot itself, not only in later versions. AB designs make causal inference "difficult", not "rarely" supported. The crossover poster's "discredited" is "seem to have been discredited".
4. F013-8: remove "looked like different algorithms". The page says "statistically different distributions" from seed alone, in one TRPO/HalfCheetah experiment. Henderson also measures no false-positive rate.
5. Larsen: the 90%-or-more is experiment failure including buggy implementation, not "ideas fail". The 10% PPV case needs that caveat.
6. Wording softened to the page: Johari ("trade off", not "cost"); F013-24 (Bayesian SEM setting; priors need not be "real prior information"); F013-25 (Bayesian methods in general, not "borrowing"); F013-19 ("related studies", not "matched pairs"); F013-22 ("40 periods per intervention").
7. Answer paragraph: the 0.70–0.77 and 0.25 McNemar power figures rest on assumed discordance rates (25% and 5%, or 15% and 5%). Say so there, not only in section 1.
8. Still open: F013-1 pingouin, F013-17, F013-20, the Button reply, the Simmons body (optional stopping), Rouder 2014, Armitage 1969 and the FDA text.

Tokens: I cannot see my token count.

## Round 2 (brief 173)

The round's verdict was PASS.

All eleven findings listed for re-check hold, and so do the answer-paragraph items and the reworded entries. Nothing round 1 marked not confirmed is relied on as fact. The memo has five minor wording points left (below), none of them blocking. Round 1's record was enough for most items. I re-opened two pages: Miller (evanmiller.org) and the SAS crossover poster.

| id | Result | Reason |
|---|---|---|
| F013-1 | holds | Minitab is now B, as round 1 confirmed. The pingouin d≈0.66 stays labelled assumed (search-only). "The page does not give the SD" matches round 1. |
| F013-8 | holds | Now "statistically different distributions", in one TRPO/HalfCheetah-v1 experiment, with no false-positive rate measured. The answer paragraph keeps Henderson out of the "far above 5%" claim. |
| F013-15 | holds | Now "can break down", with the subjective-prior quote and the Type 0 distinction. The answer paragraph, entry 5 and the last "What each answer would change" point agree with it. |
| F013-16 | holds | "Trade off sample size and power efficiently" matches the abstract. Entry 4 matches. |
| F013-19 | holds | "193 related studies"; "matched" is gone. Entry 7 matches. |
| F013-21 | holds | The 5-per-phase rule (3 with reservations) is now placed in the 2010 pilot. AB designs make causal inference "difficult". The no-formal-basis quote is kept. The CEC dispute is still labelled search-only. Entry 11 matches. |
| F013-22 | holds | Now "40 periods per intervention (80 in all)". Entry 10 matches Table 1 (0.851, 0.126, 0.681). |
| F013-23 | holds | "Seem to have been discredited (Senn)" is verbatim from the poster, as are "efficiency is often a mirage" and "nearly useless". |
| F013-24 | holds | The Bayesian SEM setting is named. Priors can come from previous research or from thinking about implausible values. The transfer to simpler comparisons is marked as opinion. Entry 6 matches. |
| F013-25 | holds | The "may be especially valuable in rare disease and pediatric trials" wording and the 14 Jan 2026 date are right. Prior or external data is a separate sentence, and "borrowing" is gone. The FDA text is still marked unopened. |
| F013-27 | holds | The 90% is now experiment failure from "bad ideas or buggy implementation". The PPV 10% case carries the caveat and stays "Estimate (Calc, illustrative)". My recompute from round 1 stands (0.857 and 0.400). |
| Answer: Bayesian wording | holds | Agrees for subjective priors, disagrees for default or pragmatic priors, "can break down", Type 0 fine. |
| Answer: pairing sentence | holds | It cites Q-003-F-a (B, single origin) for variance reduction only. "Largest gain available" is marked as opinion. |
| Answer: McNemar assumptions | holds | The 25%/5% and 15%/5% discordance rates are now stated in the answer. Round 1 reproduced the figures (power 0.699 to 0.768, and 0.241). |
| Entries 4, 5, 6, 7, 9, 10, 11, 15 | hold | All match the corrected memo and the filed library entries. |

**Entry changed.** I made one commit, 9a1f004 on build/source-checker/q-013, not pushed. It changes only `/home/user/lib-q-013/library/patterns/Q-013-P15.md`: the Grade line now names Q-003-F-a alongside Q-003-P-a and Q-003-F-i, as the revised memo's entry 15 does. I checked all the Q-013 fact and pattern entries and the README rows. None of them uses the wording round 1 corrected. The commit's last paragraph is exactly the required two lines, `Agent-Session: session_01QBwHGNSLmSrYQgS6BPjV8p/source-checker-173` and `Spec: none (library filing from research Q-013, P-002)`.

**What the memo must still correct.** These are minor, and no library entry carries them.
1. Section 3 (F013-23): "Carryover, period effects and dropouts can make the data 'nearly useless'" is slightly broader than the poster. The "nearly useless" sentence names dropouts and the unbalanced period effect. Carryover is a separate problem the poster lists as one of the biggest.
2. Section 4 (Bayesian monitoring): "Miller's page (F013-11) and Etz … say optional stopping does not affect the interpretation of posterior odds." That wording is Etz's. Miller's sentence is "With Bayesian experiment design you can stop your experiment at any time and make perfectly valid inferences." The substance is the same, but the memo should not quote Etz's wording for Miller.
3. Answer paragraph: "SPRT … control it" relies on F013-17, which is search-only and was never opened. F013-17 is about average sample number, not error control. Mark it or drop SPRT from that list.
4. Answer paragraph: "especially where most changes fail" is looser than F013-27, which says more than 50% of ideas fail. The Button reply dispute on prevalence is also not filed. Say "ideas" or mark it as inference.
5. Section 1 (F013-6): "a single run reversed at least one pairwise ranking in 10 of 12 slices" is measured against the three-run majority. The memo omits this, and it was already omitted in round 1.

Tokens: I cannot see my token count.
