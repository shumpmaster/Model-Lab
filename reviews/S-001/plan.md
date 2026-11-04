Verdict: FAIL

The Critic's plan review of specs/S-001.md and experiments/E-003.md, on a different model from the writer (brief: docs/briefs/28-critic.md), verbatim (FAIL at rounds 1 and 2; PASS at round 3). Round 4 is the join-up review closing Design (brief: docs/briefs/33-critic.md, session session_01QBwHGMBo8kZsMCS2EvKNwd, 2026-11-04, on claude-sonnet-5-5): FAIL, four blocking findings; under the plan stop rule this goes to the owner before any further round. Recorded by the orchestrator. Session session_01QBwHGLd77YbwCSMSPU26vW, 2026-11-04.

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

## Round 3
Verdict: PASS

Plan review, round 3 of S-001 / E-003 at commit da1d44f. I read the spec, E-003, the extract, both scripts and experiments/E-003/output.txt. I checked the figures against the output rather than running the scripts, since I have no shell.

Round-2 new findings

1. **Resolved (was blocking).**
   - S-001.md:103-113 sets up two separate Check author dispatches.
     - (a) is blind, on a per-task pack `S-001-holdout`, which holds the extract and the role files and playbooks it names, and nothing else. No `{spec}`, no `{ruling}`, and the withheld paths are listed under `must_not_see`.
     - (b) writes S-001's locked checks on the standing pack, with the spec.
   - AC4 (S-001.md:130) requires that the two sessions never overlap and that (b) never sees a held-back check.
   - J8 (S-001.md:147) gives a testable check on the pack entry. It fails if the entry is missing, if a withheld path matches, if the entry carries `{spec}`, `{ruling}`, may_read or include_feedback, or if the extract holds a change id, the word "arm" or a change-text sentence.
   - E-003.md:12 and :29 agree: no blind dispatch until the pack is in place and J8 passes.
   - "Needed outside this spec's lane" (S-001.md:204-205) names the owners.
   - The soundness of this fix depends on the pack entry actually being merged (see new finding 3).

2. **Resolved.**
   - The extract (check-author-extract.md:3-4, :37-38) no longer says anything about what the test changes. It says only "Files not listed in your pack are not yours to read."
   - It names no change and no arm. I checked the text and found no "arm" and no C-ids.

3. **Resolved.**
   - Weeks are now quoted at the Service Desk's pace, with the three-project pace in brackets and labelled "only if the other projects resume" (S-001.md:15, :70, :74, :90, :94).
   - The headline ranges no longer rely on POOM or Model-Lab.

4. **Resolved.**
   - experiments/E-003/output.txt holds the saved output of both scripts.
   - I checked every figure in the spec against it, line by line. All agree.
     - The weeks columns match (output lines 42-93).
       - Built work 40/60/100 is 5–10 (4), 7–15 (6) and 12–25 (9).
       - Plans is 14–28 (7), 21–42 (10) and 35–70 (17).
       - Research is 21–43 (16), 32–64 (24) and 53–107 (39).
     - The powers match: 0.84/0.57/0.34 and the rest, plus the judge-noise column.
     - The runs and tokens match (178, 266, 442; 134, 200, 332).
     - The options match.
       - A: 732 runs, 60–121 (39) and 32–64 (24).
       - B: 490 runs, 40–81 and 21–43.
       - C: 7–15.
       - D: 1,040 runs, 87–173 and 53–107.
     - The review points match: 22 to 45 plan pairs, 15 to 30 research pairs, and built work reaching its 60.
     - The eligible-per-week figures match (1.4 to 2.9, 4.1 to 8.1, 0.9 to 1.9).
     - Part 3's recent-pace counts match, including "13 built stages on 25 October" (I counted 13 in output line 24).
     - Part 4's "4 of 6", "0 of 6", "0 of 8" and "29 of 29 have a model line, none a start-commit line" match.
   - I also read the code that prints them. Part 4's new Model-Lab brief line is implemented at arrivals.py:167-171, and the briefs do carry `model:` lines (for example docs/briefs/01-critic.md:4).
   - The cross-check lines (SD 30 Sept to 1 Nov, POOM 24 Sept to 24 Oct, ML 1 Nov) show no counted record falls outside the 24 Sept to 1 Nov window.

5. **Resolved.** S-001.md:15, :47, :48 and open question 5 (:197) now say that Model-Lab's briefs carry the brief and the model but not the start commit.

6. **Resolved.** sizing.py:43 now says 4 of 6.

7. **Resolved.** S-001.md:69 states that the two window ends are the Definer's reading of Q-008, with the cross-check as the safeguard.

8. **Resolved.**
   - C2 is now stated as 10 fixed words, 11 with the list (S-001.md:30, C2 file line 7).
   - The "year" wording is replaced by the actual weeks (S-001.md:178).

New material, all non-blocking

1. **The extract tells the blind author to write the built-work check from "the frozen spec the stage builds"** (check-author-extract.md:13). The check is written once per kind before the kind opens, and the pack holds no `{spec}` (S-001.md:108). A future stage's spec cannot be in it. Reword it to a generic standard from the build-review role file, with the spec supplied to the judge at judging time through the task statement ("Judge it against" in E-003.md:50).

2. **Adding governance/PACKS.toml to Areas touched (S-001.md:150) sits uneasily with the spec's own text.**
   - S-001.md:164 and :204 say governance/** is the Chief of Staff's lane, and "proposes" is that role's authority; the change needs the owner's approval as a rule change.
   - No builder lane may edit it, so listing it does not give the Builder rights. It only lets the Chief of Staff's change pass an areas check.
   - Say that plainly in the Areas note.
   - The owner's approval of the rule change is not among the open questions (S-001.md:192-199). Add it as a line to open question 5 or 6, or name it in the gate case.
   - If the owner declines the pack change, AC4 cannot be met. Say that the test then does not start.

3. **A small overstatement in S-001.md:86.** "Research stopped there would almost certainly read 'not shown'" holds for 15 pairs (0.06 to 0.10) but not for 30 pairs (0.57 / 0.40 / 0.26, output line 71). Say "at 15; likely at 30".

4. **The Orchestrator confirms the pack in the gate case.** That is a good control. Make sure the Chief of Staff's gate document includes it, and that the Critic's gate check can verify it. This is a note for the gate stage, not for the spec.

Everything else that I checked in rounds 1 and 2 stands as resolved. The plan can be frozen once these non-blocking points are handled or accepted. None of them changes a threshold, a size or an option.

## Round 4 — the join-up review closing Design
Verdict: FAIL

## Join-up review — Design, 2026-11-04

*Required before Design can be marked done, and again before Launch (OPERATING_MODEL §4 "Phase gates", S-024). A step inside the phase, not a phase of its own. Reviewed: P-001 at commit 5bb3727. The plan review of specs/S-001.md passed at round 3 and is not re-run here.*

**Screens checked:** none. P-001 has no screens or views. Its design is a set of parts, checked side by side in place of screens:
- specs/S-001.md (criteria, J1 to J8, Needed outside, Areas touched)
- experiments/E-003.md
- experiments/E-003/check-author-extract.md
- C1, C2 and C3
- `[roles.S-001-holdout]` and `[roles.check-author]` in governance/PACKS.toml
- governance/HOLDOUTS.md
- .claude/agents/critic.md, reviewer.md and source-checker.md
- docs/playbooks/
- docs/PROJECT.md, M2 to M4 and section 6
- governance/checks/session_runner.py and governance/RUNNER.toml

| Check | Result (pass, or what differs and where) | Fix |
|---|---|---|
| One meaning per term, threshold and id | **Mostly pass.** These agree across the parts: pair, run, kind, the 1-in-40 and 6-card/2-disagreement thresholds, 8 to 12 cards, 7 days, 16 weeks, 10% reserve, and every run, token and option total I recomputed. The C1 to C3 word counts (35, 11, 64) also hold. These differ: (a) the deciding pass is not defined the same way for built work and research. (b) The model "the same model" refers to differs between plans/built work and research (finding 8). (c) "Held-back" (spec, E-003, PROJECT) and "holdout" (pack name, HOLDOUTS.md) are used for one thing. HOLDOUTS.md calls its sets "readable only by CI", but J4 puts the text in every judge's brief. (d) E-003 "Holdout use" says "used once means once per kind", against _REGISTRATION.md:12 "At most once". (e) C2 says its reachable share is "at most 3 of the 16" (C2 line 15). The spec says "3 to 5 of 16 … 11 to 19 points" (S-001:30). (f) The extract judges built work against "the spec the stage builds" (extract line 28). E-003:51 says the task statement. (g) The held-back check is a PACKS "holdout" in name only. | Findings 6, 7, 8, 9 |
| One route (work and records pass by one path; both ends of each join say the same) | **Fails at four places.** (1) The blind dispatch cannot be routed to the new pack (finding 1). (2) The held-back text has no route from its author to the harness (finding 2). (3) J7's reader, the Reviewer, cannot open the records J7 hands it (finding 3). (4) J8's withheld-path list and the pack's list differ (finding 4). J1, J2, J3, J5 and J6 have matching ends, apart from findings 7, 10 and 11. | Findings 1 to 4 |
| Consistent names, paths and ids (every path or id named exists in the part it points to) | **Mostly pass.** Every cited record exists: the C1 to C3 files, E-001/E-002 records, Q-008, the decisions and the environment report. The pack paths exist. These do not: (a) the extract names "the research playbook" and "the playbook for the spec's work type", and docs/playbooks/ holds only software.md. (b) The extract names the Service Desk's role files, which no Model-Lab pack can hold. (c) S-001:108 and J8 say the pack holds governance/HOLDOUTS.md, and the pack and runner leave it out. (d) E-003 Step 4 says "E-002's judge-brief template" with a "Judge it against" slot, and the template is in E-002 line 21 onward. | Findings 5, 9 |
| No two parts doing the same job, and no job without a part | **Pass on duplicates.** The two Check author dispatches are deliberately separate, and the judge and the locked-check script are deliberately both decisive for built work. **Unowned jobs:** the card draw by seed, re-scoring after the owner's answers, and the Newcombe range. E-003 names no part for them (the Builder runs the harness, the Chief of Staff prepares cards, the Reviewer analyses). Which part writes the result record is also unnamed. Neither is blocking: all can be assigned at Build, but they are carried as a risk. | Finding 10 |
| Every datum the design needs is available from the records, or listed as a needed change | **Fails at two places.** (a) The store location and fingerprint method for the held-back checks are in no record. (b) The runner change and the Reviewer-pack change (findings 1 and 3) are not in "Needed outside this spec's lane" (S-001:205-208). The start-commit field for Model-Lab's briefs is named in open question 5 but not listed there. | Findings 1, 2, 3, 11 |

**Needed changes to the records:**
- A runner and role change so a dispatch can select `S-001-holdout` (finding 1).
- A named store and a fingerprint rule for the held-back checks (finding 2).
- Reviewer pack entries for experiments/E-003.md, reviews/E-003/** and the owner's card answers (finding 3).
- A start-commit field in Model-Lab's docs/briefs/ (S-001:15, :47; open question 5).

## Sign-off
The owner's ruling at the gate: <the gate's decision record: decisions/<item>/criteria-<n>.md at the Build gate, for Design's review; decisions/<item>/launch-<n>.md at the Launch gate, for Build's>

## Findings

1. **BLOCKING. The per-task pack `[roles.S-001-holdout]` cannot be selected by any dispatch.**
   - governance/PACKS.toml:103-120 adds a role table named for a task. session_runner.py:464-472 builds a pack from `PACK_OF.get(role, role)`, where `role` is the plan entry's `role`.
   - SESSION_ROLES (session_runner.py:135) has no such role, so a dispatch naming it is refused as "unknown role" (:782-783).
   - `AGENT_OF` and `PACK_OF` (:137-138) map only `definer-freeze` and `critic-gate`/`critic-triage`. RUNNER.toml:36 has no `[tools]` row for it. The SURFACES.md roster (:19-30) has no row for it.
   - ENTRY_KEYS (:132) has no task field, so "task `S-001-holdout`" (S-001:108) cannot be written. A dispatch as `check-author` gets the standing `[roles.check-author]`, whose `must_read` is `specs/{spec}.md` (PACKS.toml:45). The blind author would then read S-001.
   - J8's test (S-001:147) reads only the TOML text, so it would pass while the route is broken. "Needed outside" (S-001:206) allows "a separate role table" but lists no runner, RUNNER.toml or roster change. The pack comment (PACKS.toml:105-106) says as much.
   - Fix: list the runner change as a needed change (an `AGENT_OF` and `PACK_OF` mapping and the `[tools]` row), or key the pack to an entry field. Make J8 also prove that a dispatch resolves to this pack.

2. **BLOCKING. No route or place for the held-back text, and no fingerprint rule.**
   - The extract (lines 36-38) tells the author to "store it outside every repository, as governance/HOLDOUTS.md says".
   - HOLDOUTS.md (lines 1-10) names no location and no fingerprint method. The runner keeps that file out of every pack (session_runner.py:357-358), so the author cannot read it. The pack comment (PACKS.toml:110) says "the extract carries its storage rule", but the extract gives only the sentence above.
   - The author's session is confined to its pack folder (BRIEFS.toml:9). Its write lane is tests/acceptance/** and checks/** (SURFACES.md:60-63). Its agent file says commit to build/check-author/<task> (check-author.md:20).
   - J4 (S-001:143) has the harness read the text "from outside the repositories" and check it against HOLDOUTS.md. The author side and the harness side agree on no path and no algorithm. S-001:207 has the Orchestrator record the fingerprint "from the Check author's return", so the author computes it.
   - Fix: name the store, who moves the text there, and the fingerprint (for example SHA-256 of the file's bytes, computed by the Orchestrator). Add it to the extract and to J4. Also note that a HOLDOUTS.md change needs a ledger entry with `holdouts: changed` (v3_checks.py:1635-1647).

3. **BLOCKING. J7 hands the Reviewer records its pack does not hold.**
   - E-003:15 and J7 (S-001:146) have the Reviewer analyse each kind against the thresholds in E-003. The result records go to reviews/E-003/** (Areas touched, S-001:150), and the owner's card answers go to decisions/questions/ (J6).
   - The Reviewer's pack (PACKS.toml:53-58) holds specs, tests/acceptance, checks, src, tests, docs/handover and `reviews/{spec}/checks.txt` only. It has no experiments/E-003.md, no reviews/E-003/** and no decisions/questions/**.
   - The thresholds are only partly in the spec (AC7). The Exclusions, Newcombe, false-pass guard and card rules live in E-003.
   - Fix: add to "Needed outside" a Reviewer pack entry for those three, or name where the harness puts the results (docs/handover or tests) and copy the thresholds into the spec.

4. **BLOCKING. J8's withheld-path list contradicts the pack, and as written would fail the extract.**
   - S-001:108, AC4 (:130) and J8 (:147) withhold `experiments/E-003/C*.md`. The pack withholds `C1-*.md`, `C2-*.md` and `C3-*.md` (PACKS.toml:118) because paths are casefolded (session_runner.py:225-227, :681), so `c*.md` also matches `check-author-extract.md`. The pack comment (PACKS.toml:108-109) says so.
   - J8's test "resolves its patterns and fails if any withheld path matches". Written from the spec's list, it fails on the extract, which is in the pack's `must_read`. It can never pass, and the blind dispatch is gated on it.
   - Fix: rewrite the spec, AC4, E-003 line 11 and J8 with `C1-*.md`, `C2-*.md`, `C3-*.md`, or have J8 read the pack's own `must_not_see`.

5. **Not blocking. The extract promises sources the pack cannot give.**
   - Lines 12-14 and 16-17 name "the research playbook", "the playbook for the spec's work type", and the Service Desk's role files "where two projects' standards differ". docs/playbooks/ has only software.md.
   - The pack is a Model-Lab source tree, so the Service Desk's files cannot be in it.
   - Today every eligible piece comes from the Service Desk (S-001:47), so Model-Lab's standard would judge the Service Desk's work.
   - Carry as a risk for the Build gate. Fix: say the check is written from Model-Lab's files only, or add the Service Desk's files to the pack as a needed change.

6. **Not blocking. Spec and pack disagree on what the pack holds, and the blind author's own role file and brief point at the spec.**
   - S-001:108 lists governance/HOLDOUTS.md in the pack. The runner removes it from all packs (session_runner.py:357-358), and the pack leaves it out.
   - The check-author agent file (check-author.md:11, :23-24) and the brief (BRIEFS.toml:9, :17) tell the author to read the frozen spec ("spec S-001"). Both come with every pack (session_runner.py:822-823).
   - Fix: add a BRIEFS route and a note in the extract that these lines do not apply.

7. **Not blocking. J3 says the judge never sees commit messages, yet a "fresh copy of its final commit" holds them.**
   - J3 (S-001:142) says "never the hand-back or commit messages". E-002:37 and E-001 step 2.1 copies hold the commit and its ancestors, so the arm's commit messages are in the history.
   - The judge template (E-002:30-32) bars other repositories but not `git log`.
   - Fix: squash the deliverable into one neutral commit, or add the bar to the judge brief.

8. **Not blocking. Plans and built work use a different model than the recorded one.**
   - E-003:44 runs both arms on "the model the operating model uses for that role when the kind's comparison opens". AC2 and S-001:59 say "the same served model", and J2 (:141) records the dispatch model. For research, E-003:45 uses the check's recorded model.
   - The recorded model is a required field for eligibility but is not used for plans or built work.
   - Fix: say which one governs.
   - A related gap: AC5 requires a judge on a model other than the doers'. If a recorded source-check model were Fable 5.1, no awkward case covers it.

9. **Not blocking. Judge brief text differs from E-002's template without saying so.**
   - E-003:52 and Exclusions 2 let the research judge use the web. The template (E-002:30-32) says "do not use the web".
   - E-003:53 adds the foreground-only lines only. The template's "Judge it against" slot (E-002:28) is a spec or request, but plans have nothing in J3 for it.
   - Fix: list every change to the template.

10. **Not blocking. Jobs with no named part, and the milestone header.**
    - No part is named for the card draw, the re-scoring, the Newcombe range, or writing the result record (E-003 steps 3 to 5; J5 to J7; Areas touched has reviews/E-003/** in the Orchestrator's lane). The Builder cannot write there (SURFACES.md:65-70).
    - Fix: name the Builder's harness for the first three and the Orchestrator's recording route for the record.
    - E-003:5 names milestones M2 and M4. S-001:7 names M2 only, yet AC4 to AC9 deliver M4's test. PROJECT.md:66 gives M4 to the Builder.
    - PROJECT.md:57 and :108 still read "on the same past tasks" and "about 300 runs" (:117), against the spec's 732. Open questions 1 and 2 cover these for the owner, so they stand as carried risks.
    - M3 "lands with M5" (PROJECT.md:37), after M4, yet the test needs recording from the start. S-001:48 and open question 5 give the fallback (the Chief of Staff records).

11. **Not blocking. Result and sample data have a small mismatch.**
    - Model-Lab's briefs hold no start commit (S-001:15, :47), and "Needed outside" (S-001:208) lists recording only "if the owner orders it".
    - The "Holdout use" line of E-003 (:107) names no held-back set, but _REGISTRATION.md:12 asks for one. The ids will exist only after dispatch.
    - Fix: list the field and set ids as needed changes at the Build gate.

## The six-part contract

1. **What I changed:** Nothing. I am read-only and wrote no file.
2. **Why:** To check the Design parts side by side, as the brief asked, and give the Design part of docs/design/JOIN_UP_REVIEW.md.
3. **What I verified:**
   - I read all the files the brief lists, plus the cited records by existence.
   - I recomputed the run and token totals for options A to D.
   - I counted the words in C1, C2 and C3.
   - I traced the runner's role-to-pack lookup (session_runner.py:135-142, :464-472, :807-812), the pack contents and the tool rows in RUNNER.toml.
   - I did not run any command.
4. **What is undone:** I did not read the Service Desk's files, the operating model repository, or the full list of records the spec cites. I did not run the J8 test or the harness, since neither exists yet.
5. **Needed outside my lane:**
   - The Chief of Staff and Orchestrator: the runner and roster change for `S-001-holdout` (finding 1), the store and fingerprint rule (finding 2), and the Reviewer pack (finding 3).
   - The Definer: findings 4 to 11.
6. **Open questions:**
   - Should dispatch (a) get its own role name in the runner, or a task field in the entry?
   - Where is the held-back store, and who moves the text there?
   - Does the owner want findings 5 to 11 fixed before the Build gate, or carried as risks?

Files: /home/user/Model-Lab/specs/S-001.md, /home/user/Model-Lab/experiments/E-003.md, /home/user/Model-Lab/experiments/E-003/check-author-extract.md, /home/user/Model-Lab/governance/PACKS.toml, /home/user/Model-Lab/governance/HOLDOUTS.md, /home/user/Model-Lab/governance/checks/session_runner.py, /home/user/Model-Lab/governance/RUNNER.toml, /home/user/Model-Lab/governance/BRIEFS.toml, /home/user/Model-Lab/governance/SURFACES.md, /home/user/Model-Lab/docs/design/JOIN_UP_REVIEW.md.
