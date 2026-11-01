Verdict: PASS

The Critic's check of questions/P-001-after-the-count.md and the brief's updated sections 5, 6 and 7, on a different model from their writer (brief: docs/briefs/15-critic.md), verbatim: round 1 (FAIL), round 2 (PASS). Recorded by the orchestrator. Session session_01QBwHGHrHnEvMNYgKDoaH8w, 2026-11-01.

## Round 1
Verdict: FAIL

I could not run `git diff` because I have no shell tool. I read sections 5, 6 and 7 of /home/user/wt/ml-cos/docs/PROJECT.md directly and judged those lines as they stand now. I made no check against the diff itself.

1. Blocking. The "gain counts at" thresholds and power figures in section 6 use a 5% cutoff, not the owner's 1 in 25.
   - The same sentence says "chance alone at most 1 time in 25" and then "one-sided at 5%". Those are different cutoffs, and the figures follow the 5% one.
   - I recomputed the exact binomial at 30 pieces:
     - Plans (starting rate 2/44): stated threshold 4, chance of reaching it about 4.5%; threshold at 1 in 25 is 5.
     - Built work (40%): stated threshold 17, chance about 4.8%; threshold at 1 in 25 is 18.
     - Critic (1/20): stated threshold 5, chance about 1.6%; it holds at 5.
     - Research (5/19): stated threshold 13; not computed exactly (a normal approximation is borderline), so not confirmed.
   - Plans at 4 and built work at 17 therefore break the owner's ruling (decisions/questions/P-001-value-target.md).
   - The power figures go with them. At thresholds 5 and 18, a real 20-point gain shows roughly 90 and 57 times in 100, not the stated 96 and 71. I checked these approximately, not exactly.
   - The research and Critic power figures (69, 90) are consistent with the 5% calculation. Re-derive all four under the ruled cutoff.

2. Blocking. The options tilt towards A, and A's cost is incomplete.
   - A is the longest option. It is the only one with a bolded sub-clause and two supporting sentences.
   - A takes credit for "every agent's brief and AI model is recorded". The owner already ruled that across the model (P-001-session-records.md), and option C also keeps it. It is no reason to prefer A.
   - A's cost never mentions the run and token cost. PROJECT.md section 6 says the testing budget is "about 300 runs". Option C's gain, by contrast, is stated as "no more effort or tokens".
   - A's cost also omits that if the test finds nothing, the project closes under the owner's earlier ruling (P-001-no-change-result.md). That is the same end state as C, reached after spending the runs.
   - A also says the test "does not need past causes". That is stated as settled. In fact whether past tasks can be replayed (U2) and whether any change shows a visible gain (U4) are both still open.

3. Blocking. The question uses the research one-sidedly.
   - The option A text says the research "found instructions matter most for vague hand-overs and missing requirements". That is an estimate, and the Researcher gave it with qualifications.
   - The question leaves out what the same memo concludes: instructions are "one lever among several, not the main one", and model and context are the largest levers on capability-limited tasks (Q-002 memo §1 items 4 and 7).
   - The "estimate" label appears only in the Context list. It is missing from the body the owner reads, where it supports the recommended option.

4. Non-blocking, but fix before the question is put. The count is described as bigger and firmer than it was.
   - "Of 84 sent-back pieces" should say returns, not pieces. A piece can be sent back several times.
   - The 84 come from 125 returns classified out of 315 found. Most of the plan, built and other-work returns were drawn from samples.
   - The question omits that 41 more returns have no findings recorded at all.
   - "None names the AI model" reads as "the model is not a cause". The memo's own search found the model is almost never recorded (3 SD hits, 2 POOM, 0 Model-Lab, none a cause). The honest wording is that the model is not recorded, so the count cannot say.
   - "Instructions 1" is the primary cause only. The brief was unseen by the checkers, so the records cannot assess instructions either way. The question says this only in part.

5. Non-blocking. The pooled starting figures reproduce, but the choices behind them are not disclosed.
   - Plans: 1/17 + 1/23 + 0/3 + 0/1 = 2/44 (reproduces). S-004 is excluded.
   - Research: 2/12 + 3/7 = 5/19 (reproduces). It takes the Model-Lab "original check" figure. Counting the later-added check gives 0 of 7, so 2/19 (about 11%). The Q-014 and Q-015 variant gives 3/14 for Service Desk.
   - Built work: 15/51 + 17/29 = 32/80 (reproduces). The 17/29 includes 5 single-PASS PR files that record no earlier round. Without them POOM is 12/24, and the pool is 27/75 (36%), not 40%.
   - Critic: 1/20 (reproduces).
   - Section 6 treats these as exact baselines, though 2 of 44 is very uncertain. It should say so, and say which variant was chosen.

6. Non-blocking. The Critic starting figure has no V2 line. The Critic's 1 of 20 is listed and given a threshold, but V2 covers only plans, research and built work.

7. Non-blocking. The question's "who has checked it" cites reviews/P-001-after-the-count/critic.md, which does not exist yet. It should be filed before the question is put. The line is otherwise accurate, and the Source checker's round 2 PASS is a real record.

8. Non-blocking. The question has no explicit "if you don't decide" line. "DEFAULT: none ... TIMEOUT: none" with the WHY sentence nearly covers it. Add one plain line: nothing moves, and no test is designed.

9. Non-blocking. Some terms in the question are not plain. "R3" and "Source checker" need a few words each, and "stop rule", "candidates" and "fair test" are used without explanation.

10. Section 5 and the 21/2/61 split in U1 and U5 check out.
    - Spend ceiling: matches P-001-spend-ceiling.md. The owner's "Plan, with option to override" is carried faithfully, and the weekly-limit handling matches the ruling.
    - The "about 100 test runs" figure cites P-001-test-budget.md, which I was not given, so I did not verify it.
    - U1: 10 + 8 + 1 + 1 + 1 = 21, plus 2 worker slips, plus 61 residual = 84. This matches memo bottom lines 3-4.
    - U5: "61 of 84" and "41 more" match memo §5.
    - Nothing in these lines is attributed to the owner without a record.

## Round 2
Verdict: PASS

Round 2. I re-read the rewritten question and the "Starting figures" line in PROJECT.md section 6. I re-derived the thresholds and odds myself.

Round-1 findings

1. Resolved. The thresholds and power figures now use the ruled 1-in-25 cutoff.
   - My exact binomial at n = 30 gives plans 5 at about 1.1%, which matches your figure. The power at the 20-point gain comes to about 0.89-0.90, which matches.
   - Built work at 18 gives about 2.1%, which matches. The alternative 27/75 -> 16 at about 3.9% is consistent with my approximation (about 3.7%).
   - Research 13 and the alternative 2/19 -> 7 are consistent with my normal approximation, but I did not compute them exactly. The 5-of-19 threshold of 13 is the one I flagged as unconfirmed in round 1. I now accept it as plausible, not verified.
   - The sentence no longer says "5%". The Critic line is stated as outside V2's three kinds.
2. Resolved. The options are now even.
   - A's cost now names the roughly 300 runs, the open replay question, the open "can the test see a gain" question, and the accepted "no change helps" closure.
   - The brief-and-model record is stated once, as common to all options and already ruled.
   - A, B and C are each about the same length. Each has a gain, a cost and a reversibility line.
3. Resolved. The research is now cited in full.
   - "One lever among several, not the main one" is quoted. The model and context points appear alongside the instruction point.
   - Option C and the "what would change it" line now give the research as a reason to stop.
4. Resolved. The count's limits are now stated.
   - The question says 315 returns, 125 classified (many by sampling), 41 with no findings, and 84 with findings.
   - It says the model is almost never recorded.
5. Resolved. The starting figures now disclose the alternatives.
   - Research is given as 5 of 19 or 2 of 19, and built work as 32 of 80 or 27 of 75.
   - Both alternatives carry their own thresholds and power.
   - The small-count uncertainty is stated.
6. Resolved. The Critic figure is explained as "recorded for reference" and not one of V2's kinds.
7. Resolved. The record reviews/P-001-after-the-count/critic.md exists at /home/user/wt/ml-orch.
8. Resolved. The question now says "If you do not decide, nothing moves and no test is designed."
9. Partly resolved.
   - "Source checker" is now explained.
   - "Stop rule", "candidates" and "fair test" are explained in place.
   - "R3" in the risk line is still unexplained. That is the form's field, so it is acceptable.
10. Still holds.
    - decisions/questions/P-001-test-budget.md confirms the roughly 100 runs through Discovery and Design, with checkpoints.
    - The section 5 spend ceiling and the U1 and U5 figures are unchanged and still match.

New findings, all non-blocking

11. The question says "no checker saw the brief the worker was given". The memo supports less than that. It says only that the M3C Triage, which blamed a brief, could not see it, and that worker briefs are not recorded for conversational work. Suggested wording: "the briefs workers were given are mostly not recorded".
12. The WHY line says the stop rule "is reached". The rule fires only if the count shows instructions are not a meaningful cause, and the same paragraph says the count could not show that. PROJECT.md U1's fallback sends the case to the owner anyway, so the route is sound. Suggested wording: "the count could not settle the question your stop rule asks, so it comes back to you".
13. The quoted "one lever among several, not the main one" is the memo's bottom line 7, tagged [opinion]. The question calls it "the researcher's estimate". Say "opinion", or cite items 4 and 5 for the estimate.
14. The question's recommendation confidence is "low-to-medium", while the PROJECT.md and earlier text said "medium". This is fine, as the question is the live record.

Files read:
- /home/user/wt/ml-cos/questions/P-001-after-the-count.md
- /home/user/wt/ml-cos/docs/PROJECT.md (line 97)
- /home/user/Model-Lab/decisions/questions/P-001-test-budget.md
