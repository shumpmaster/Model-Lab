Verdict: FAIL

The Critic's plan review of specs/S-001.md and experiments/E-003.md, on a different model from the writer (brief: docs/briefs/28-critic.md), verbatim. Recorded by the orchestrator. Session session_01QBwHGLd77YbwCSMSPU26vW, 2026-11-04.

## Round 1
Verdict: FAIL

Plan review, round 1 of 3, of S-001 / E-003 (/home/user/wt/ml-definer-s001/specs/S-001.md, /home/user/wt/ml-definer-s001/experiments/E-003.md).

What I could not do: I have no shell tool, so I could not re-run experiments/E-003/sizing.py.
- I re-derived by hand: critical(10)=9 and critical(20)=15, which match the library fact (/home/user/portfolio/library/facts/Q-003-F-i.md:11).
- Plans one-way power: 0.84 at 40 pairs and about 0.99 at 60, both match.
- Research independent-arms power at 60 pairs (0.54) is plausible by a z-approximation.
- Run counts, reserves, token totals and the option A to D sums all re-add correctly: 266+200+266=732; B 490; D 1,040; about 180k a run.
- E-001's per-kind averages (doers about 239k, judges about 160k, about 11% dearer) match src/E-001/RESULT.md:270-283.
- The three change texts have the word counts claimed: 35, 35 and 64.
- The Q-008 tallies match (research check 7 of 14, plans 16 of 18, built material 5 of 16: research/Q-008-memo.md:485-503).
- The line citations I checked in reviews/E-001/reviewer.md, P-001-e002-not-tested.md and docs/PROJECT.md:96,:99,:147 say what is claimed.

Blocking findings

1. **The held-back check is written from S-001, which names the changes.** E-003.md:27 says the Check author writes each check "from … S-001". S-001.md:18-31 (the table of C1 to C3, their causes and their text) is inside S-001. S-001.md:81, E-003.md:11 and AC4 (S-001.md:98) say the Check author never sees the change texts. S-001 describes each change's content (C1: the writer reads the check's role file; C3: the check returns a memo only for a fault it can show). As written, AC4 cannot be met, or is met only by a loophole. Fix: give the Check author only an extract of S-001 that omits the change section, name that extract, and add it to the Check author's pack and to AC4.

2. **The arrival-rate evidence does not say what is claimed.**
   - S-001.md:55 and :122/:136 cite research/Q-008-memo.md §2 for "44 plans, 80 built, 19 research over 5.4 weeks (24 September to 1 November)".
   - Q-008 §2 (lines 181-220 and the tallies) counts returns (148, 82, 40), not pieces, and I find no date window or week count anywhere in the memo.
   - The piece counts 44, 80 and 19 are in docs/PROJECT.md:99, with no dates.
   - The 5.4 weeks and the rates of 8, 15 and 3.5 a week therefore rest on a window no record states. Every "Weeks to collect" figure, the 22 to 79 weeks for option A, and the 16-week limit all depend on it.
   - Fix: cite a record that gives the window, or add the computation as evidence. Also supply evidence for the last-week figures, which cite only git queries.

3. **The time figures contradict the proposed time limit.** S-001.md:78 proposes a 16-week limit per kind, but the table gives plans 10 to 40 weeks, research 7 to 23 and option A 22 to 79 (S-001.md:60, :63, :73).
   - On the slower pace, plans would stop at 16 weeks with about 24 of 60 pairs, and research would stop short as well. The power stated for the recommended option would then be wrong.
   - Fix: restate each option's expected pairs and power at the limit, or drop "recommended" until the limit and size agree.
   - S-001.md:10 ("sees a real 20-point gain about 4 times in 5") is true only if the limit never bites.

4. **The owner's-sample rule leaves results to interpretation.**
   - (a) E-003.md:52-54 draws "pairs" with differing verdicts, but each card shows one "output" and the answer "replaces the judge's verdict for that output". It is not said which output of a pair is shown, or whether both are, so how n10 and n01 are recomputed is undefined.
   - (b) The card question ("should this work have gone back? yes / no / can't tell") is not mapped to PASS and FAIL.
   - (c) "Can't tell" counts as agreement and has no cap, so a judge can be "confirmed" by eight "can't tell" answers.
   - (d) The rule of 3 or more disagreements (E-003.md:88) does not say what happens with fewer than 8 cards. With 2 cards the judge can never fail confirmation; J6 (S-001.md:113) allows this.
   - (e) Cards come only from discordant pairs and from passed outputs. Pairs where both arms fail, the majority for plans at a 5% start, are never examined. Plans may also have no passed outputs to sample. The sample can therefore catch a judge that wrongly passes or splits, not one that wrongly fails everything.
   - (f) How the seed orders the draw is not stated.
   - Fix: define the card, the mapping, the can't-tell treatment (for example, more than N reported and the kind not confirmed) and the minimum number of cards for confirmation.

5. **The research arm's eligibility ignores the brief the change acts on.**
   - C3 changes the source check's brief. E-003.md:34 requires the recorded brief, start commit and model of the memo's task, not of the check.
   - Step 3 (E-003.md:42) says each check runs with "its recorded brief", but no eligibility rule requires that the check's brief and model be on record, nor J2 (S-001.md:109). Only Model-Lab's docs/briefs are shown to hold briefs.
   - Open question 5 raises recording for conversation-started work but not this gap.
   - Fix: add the check's brief, check commit and model to eligibility and J2.

Non-blocking findings

6. **C2 adds a rule, so it is two changes and breaks R6.**
   - The text (C2 file, lines 19-21) adds both the list and "If two of them disagree, build to the frozen spec … and name each disagreement". That is a new rule to follow, contradicting S-001.md:146 ("none adds a rule to follow").
   - The effect cannot be attributed to the list alone.
   - It is three sentences, not "two" as the C2 file says (line 6).
   - "Build to the frozen spec" may contradict an owner ruling that outranks it; the harness list orders the spec first.
   - The example `specs/S-001.md:3727-3741` is a line range that does not exist.
   - The mechanical fill rules need a case for a task that names no spec: J1 covers "list holds only the spec", not "no spec".

7. **The sizing assumes a 20-point gain the cited causes cannot supply for C3 and C2.**
   - C3 reaches at most 2 to 3 of the 14 research returns (C3 file, lines 11-12), roughly 16 points of 19 memos at best.
   - C2 reaches 5 of 16, and S-001.md says part is unreachable by text.
   - Say plainly that a true effect below 20 points will usually read "not shown", and that this is a test of the owner's target and not of whether the change helps. R2 (S-001.md:141) does not say it.

8. **The judging limits section omits some points.**
   - The sizing counts no judge noise, though judge consistency was not run.
   - The decision uses a proxy pass (judge against held-back check), while V1 is the first-time pass at the real independent check. The real round-1 verdict is "reported, not deciding" (E-003.md:60). Say that the link between the proxy rate and the real rate is untested.
   - Every held-back check is written by the same model line from the same standard that C1 shows the writer (this is partly stated).
   - The held-back check is "used once" (E-003.md:94) yet read by every judge on every pair; define "once" as once per kind.
   - The section otherwise states its limits well: same provider, consistency unmeasured, C1 teaching to the check, and 8 cards.

9. **Arrival and eligibility rates are optimistic.**
   - Last week's 12 research pieces include Model-Lab Q-001 to Q-008, that is, this project's own Discovery research, which is ending. Service Desk alone gave 4 (S-001.md:55).
   - Q-008 says the records are "mostly conversation-started work", which would not enter without the brief record (open question 5), yet the time table assumes only the 3-in-4 mid-round loss.
   - The operating model repository has had no commits since 24 October, so it contributes no pieces.
   - State a range for the share of pieces that are eligible.

10. **AC5 does not fit research.** It says each arm's deliverable is judged in its own session, but E-003.md:48 has one judge session per memo, and the arms are two check verdicts. Align AC5 and J3.

11. **The false-pass guard "no more than the unchanged check's plus one" (E-003.md:89) has no stated reason.** Record why it is the right tolerance.

12. **The open questions are mostly complete and fairly stated.** Missing items:
    - the 16-week limit and the sequential order against the owner's "no fixed timeline" and "incrementally" rulings (P-001-time-and-limit.md, P-001-worst-work.md). Questions 3 and 4 touch this but do not name the rulings.
    - the item 5 gap above.
    - the owner's "about 100 runs" ruling (P-001-test-budget.md) covers Discovery and Design only, so the 732-run ask is rightly a Build-gate item. Say so in question 3.
    - Question 1's proposed V1 wording is faithful to the ruling's 20 points and 1-in-40 (P-001-value-target.md:1).

13. **Form.**
    - Spec form is followed. The milestone header names M2.
    - `frozen_at` and `design_id` are placeholders, which is acceptable for a draft.
    - E-003 has all the template headings. Its "Holdout use" names no set ids, which is acceptable until the Check author writes the checks. governance/HOLDOUTS.md is empty, as expected.
    - Join sheets J1 to J7 each have awkward cases and tests. Add the C2-no-spec case (finding 6) and the research check-brief case (finding 5).
    - The criteria all trace to V1 or V2, but AC1 is about files, not a scenario the owner can judge outcomes from. The owner can still approve it.

Two checks came out clean and need no change.
- Replay lessons: S-001.md:86-92 correctly follows reviews/E-001/reviewer.md findings 4, 5 and 8 and ruling 1.
- Consistency with the rulings: the fallbacks for U2 and U3 are applied as P-001-open-unknowns.md:11-12 and P-001-e002-not-tested.md:10-12 say. The spend ceiling is respected, and S-001.md:84 is honest that Fable 5.1 may not be a different family (docs/reports/2026-11-03-design-environment-check.md:16).

Please resubmit with findings 1 to 5 addressed.
