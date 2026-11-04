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

## Round 2
Verdict: FAIL

Plan review, round 2 of 3, of S-001 / E-003 at commit e0c9717.

I have no shell, so I did not run sizing.py or arrivals.py. I read both, read the records they read, and re-did the arithmetic by hand. I could not check git add dates (24 Sept, 30 Sept, 1 Nov).

Round-1 findings

1. **Resolved in substance, with one gap (see new finding 1).**
   - The Check author is now given only experiments/E-003/check-author-extract.md (S-001.md:99, AC4 at :116, J8 at :133, E-003.md:11, :27).
   - I read the extract (check-author-extract.md:1-44). It names the kinds, the existing check files to write from, the held-back check form, the J5 answer form and the rules. It says nothing of the changes' content.
   - J8's test checks that the pack lists no withheld file and that no change-text sentence appears in the extract.
   - The held-back checks stay correlated with C1 and C3, because they are written from the same role files the changes touch. S-001.md:102 and :41 now state this.

2. **Mostly resolved, with conditions (see new findings 3 and 4).**
   - arrivals.py gives the window, the rates and the recording share.
   - My re-derivation matches S-001.md:69.
     - 24 Sept to 1 Nov, both days counted, is 39 days = 5.57 weeks.
     - 44, 80 and 19 over 5.57 weeks give 7.9, 14.4 and 3.4 a week.
     - The Service Desk (SD) alone is 33 days = 4.71 weeks, giving 18/4.71 = 3.8, 51/4.71 = 10.8 and 12/4.71 = 2.5.
   - The hard-coded SD denominators (arrivals.py:33) match Q-008: 1+17 plans, 51 built, 12 research (research/Q-008-memo.md:73-79).
   - The recording claims check out against the records.
     - SD has `_control` folders only for Q-items.
     - My glob found no control files under any other reviews folder, so "no plan or built piece has a record" holds.
     - SD's recent research dispatches (dispatch-log/2026-11.jsonl) cover Q-016 to Q-021 (6 items).
     - Source-checker control files with `brief`, `model` and `source_tip` exist for Q-016, Q-018, Q-020 and Q-021. That is 4 of 6, as S-001.md:71 says.

3. **Resolved.**
   - Review points replace the calendar limit (S-001.md:85, E-003.md:76).
   - I re-derived every "Weeks" figure from the pace and share used in sizing.py.
     - Built 60 is 5.6 to 14.8 weeks.
     - Plans 60 is 10.1 to 42.1.
     - Research 60 is 23.5 to 64.
     - Option A one after another is 39 to 121.
     - Option A together is 24 to 64.
     - B, C and D match.
   - Pairs at the 16-week slow-pace review point: plans 22, research 15 (built exceeds 60).
   - The power quoted at those sizes is plausible. One-way research at 15 pairs is 0.06; one-way plans at 22 is about 0.27.
   - Runs, tokens and the power table are unchanged and correct.

4. **Resolved.**
   - A card is one output (E-003.md:55).
   - Yes is FAIL, and "can't tell" has a defined treatment (E-003.md:62).
   - Groups G1/G2/G3 are 4/2/2, so wrongly-failing judges are now sampled.
   - The seeded draw is specified (E-003.md:61).
   - Confirmation needs at least 6 answered and at most 2 disagreements. S-001.md:101, AC6, AC7 and J6 agree with E-003.

5. **Resolved on paper.**
   - The research check's brief, start commit and model are required at entry (E-003.md:35, Exclusions 6, S-001.md:46, J2, open question 5).
   - See new finding 5: Model-Lab's briefs do not record the model.

6. **Resolved.**
   - The disagreement rule is dropped from C2.
   - C2 now has the no-spec and empty-list cases (C2 file, lines 30-33).
   - The bogus line range is gone.
   - See finding 8 for a word-count nit.

7. **Resolved.** The "Most it could reach" column (S-001.md:27-31) and "What the test can and cannot show" (S-001.md:39-43) state the point plainly, and R2 repeats it.

8. **Resolved.**
   - Judge noise is added to the sizing: the `noisy()` formula is right, and the table column agrees with S-001.md:42.
   - The stand-in measure is stated (E-003.md:70).
   - "Used once" now means once per kind (E-003.md:106).

9. **Partly resolved (see new finding 3).**

10. **Resolved.** AC5, J3 and E-003.md:50-51 now agree for research.

11. **Resolved.** E-003.md:101 gives the reason and open question 7 hands it to the owner. The argument is thin but honestly labelled as a judgment.

12. **Resolved.** Open questions 3, 4, 5 and 7 now carry the rulings and the research question.

13. **Resolved.** J1, J2 and J6 carry the added awkward cases.

New findings

1. **BLOCKING: the blind Check author cannot also write S-001's locked checks.**
   - S-001.md:187 says the Check author's pack must hold the extract "in place of `specs/{spec}.md`".
   - S-001.md:191 names the Check author only for held-back checks.
   - But S-001's own acceptance tests and join-tests (J1 to J8, `tests/acceptance/**`, `checks/**`) are normally written by the Check author from the spec, at stage 4 (OPERATING_MODEL.md "Tests written before the work", line 165; PACKS.toml:44-45 gives that role the spec).
   - As written, either the locked checks have no author, or the same role both reads the spec and is the blind author. The second breaks AC4.
   - Fix: state two separate Check author dispatches. (a) A blind one, whose per-task pack holds the extract, not the spec. (b) A normal one for the locked checks, with the spec. Say who dispatches each and that (b) never writes or sees the held-back checks. Say that the PACKS change is a per-task pack, not a replacement of the role's standing pack.
   - Also name who makes the PACKS change and when (it is outside the spec's areas, and the Orchestrator must confirm it before the Build gate). J8's test is only meaningful once it is in place.

2. **Non-blocking: the extract's header tells the Check author that the test varies something.** The extract says what "the test changes" and that files `C*.md` are withheld (check-author-extract.md:3-7, :40). That is a hint, though a mild one. Reword it to "files not listed in your pack are not yours to read". Also J8's check that no change-text sentence appears in the extract does not catch this.

3. **Non-blocking: the "fast pace" is not reachable as described.**
   - Fast is "all three projects" (S-001.md:69). But the same paragraph says the operating model repository has stopped and Model-Lab's research was this project's own Discovery.
   - POOM supplied 26 of the 44 plans and 29 of the 80 built pieces (Q-008.md:73-78). So the fast pace for plans (7.9 a week) and built work (14.4) cannot come back unless POOM resumes.
   - Label the fast end "only if the other projects resume", or drop it from the headline ranges (nine months in the "Time" bullet, S-001.md:15).
   - The slow pace of the SD alone (3.8 and 10.8) is the honest central case.

4. **Non-blocking: the evidence is a command, not command plus output.**
   - S-001.md:151-152 cites `python3 …` without the printed output (template form: "command + output").
   - I could not run either script.
   - Before the freeze, the Orchestrator should run sizing.py and arrivals.py, attach the output (for example experiments/E-003/output.txt), and confirm it matches the figures in the spec.
   - Confirm especially the three dates, the cross-check lines (arrivals.py:129-131, which the spec does not quote) and "6 recent research items".

5. **Non-blocking: Model-Lab's briefs do not record model or start commit.**
   - S-001.md:15 and E-003.md:36 say Model-Lab's docs/briefs/ holds the record today.
   - docs/briefs/README.md:1-4 says only that it records "what the agent was told", the brief text. No model, no start commit.
   - So Model-Lab's plans and built work are no more eligible today than the SD's. Correct the claim, or add Model-Lab to open question 5.

6. **Non-blocking: sizing.py's comment contradicts the spec.** sizing.py:36 says "3 of 6 recent research items on record". S-001.md:71 says 4 of 6, and the control files confirm 4 of 6. Fix the comment. The share is not computed from it (SHARE is hard-coded at sizing.py:39), but the evidence should agree.

7. **Non-blocking: arrivals.py's window start is an inference.** The first and last records (POOM reviews/1/reviewer.md; ML Q-002-to-Q-007-corrections-confirmation.md) are the Definer's choice. Q-008 mentions both (Q-008.md:213, :447) but does not say they are the earliest and latest. The cross-check lines are the safeguard (finding 4).

8. **Non-blocking nits.**
   - C2's fixed text is 11 words, not 10 (S-001.md:30, C2 file line 7).
   - S-001.md:161 says "plans and research could take most of a year each", while research at 60 pairs is up to 64 weeks.

9. **Non-blocking: the judging limits are honestly stated.** The same-provider, unmeasured-consistency, C1-teaching-to-the-check and 8-cards limits are all present (S-001.md:102). Owner cards from G2 and G3 now address a judge that wrongly passes or fails. Plans may have few G2 outputs at a 5% start. E-003.md:60 handles this by moving the cards to other groups.

Please resubmit with finding 1 fixed. Findings 2 to 8 can be fixed in the same pass.
