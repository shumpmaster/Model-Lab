Verdict: PASS

The Critic's plan review of specs/S-001.md and experiments/E-003.md, on a different model from the writer (brief: docs/briefs/28-critic.md), verbatim (FAIL at rounds 1 and 2; PASS at round 3). Round 4 is the join-up review closing Design (brief: docs/briefs/33-critic.md, session session_01QBwHGMBo8kZsMCS2EvKNwd, 2026-11-04, on claude-sonnet-5-5): FAIL, four blocking findings; under the plan stop rule this went to the owner, who chose one focused confirmation review (decisions/questions/P-001-plan-stop.md). Round 5 is that review (brief: docs/briefs/38-critic.md, on claude-sonnet-5-5): FAIL, two new blocking findings; it went back to the owner, who chose to re-specify how the test is run as a new draft reviewed from round one (decisions/questions/P-001-plan-stop-2.md). The new draft's rounds are recorded below as "New draft, round <n>" (brief for round 1: docs/briefs/42-critic.md): round 1 FAIL, four blocking findings; round 2 FAIL, one blocking finding; round 3 PASS, with the join-up review passing. Round 4 (brief: docs/briefs/57-critic.md, session session_01QBwHGKFFgmANWaCNGxCLZd, on claude-sonnet-5-5) is a focused check of the Definer's fix to the order of the kinds and its weeks (commit e504ea0): PASS. Recorded by the orchestrator. Session session_01QBwHGLd77YbwCSMSPU26vW, 2026-11-04.

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

## Round 5 — the focused confirmation review
Verdict: FAIL

Confirmation review of S-001 (plan round 5), on claude-sonnet-5-5, a different model from the Definer. Two blocking findings are new. Both sit in the join between the held-back store and the judges, the part the fixes touched but did not finish. Of the seven earlier findings, five are resolved, one is resolved only on paper, and one is only partly resolved.

**How I worked.** I have no shell, so I could not run `git diff`. I read the files as they stand now (ec29f46) and compared them with the figures recorded in reviews/S-001/plan.md rounds 3 and 4. I read these:
- specs/S-001.md
- experiments/E-003.md
- the extract (experiments/E-003/check-author-extract.md)
- governance/PACKS.toml
- governance/HOLDOUTS.md
- governance/SURFACES.md
- the runner functions in session_runner.py (norm, always_out, _fill, _any, manifest_problems, and the SESSION_ROLES, AGENT_OF and PACK_OF lines)
- glob_to_regex and glob_match in govlib.py
- intake/P-001-environment-2026-11-04.md
- E-002's judge-brief template
- the check-author agent file

I read the docstring of `glob_to_regex` but not `_segment_regex`. I did not read `pack_entry` or the Service Desk's whole files. From the Service Desk I only grepped critic.md line 31, which matches the spec's claim of a one-word difference.

## The seven earlier findings

1. **Pack `S-001-holdout` cannot be selected. Resolved on paper; the proof is partly open (see B1).**
   - The route is now a hand-assembled pack, with no runner change (S-001:114-119, :227-230; E-003:11; PACKS.toml:103-121).
   - SESSION_ROLES, AGENT_OF and PACK_OF are left alone, so the original defect is gone. The spec says openly that `S-001-holdout` is "no role it knows".
   - J8 (S-001:163) now checks a recorded manifest against the pack entry. That shows what was put in a folder, not what the session could read (B1).

2. **No place for the held-back text, no fingerprint rule. Partly resolved.**
   - The author-to-store leg is now consistent in four places:
     - The Check author returns the text to the Orchestrator only (extract :48-52; S-001:122).
     - The Orchestrator places it in one file in the store.
     - The fingerprint is the SHA-256 of that file's bytes, computed by the Orchestrator.
     - The Orchestrator records the set id and fingerprint in HOLDOUTS.md with a ledger entry `holdouts: changed` (S-001:121-125, :159, :231). v3_checks.py:1635-1646 exists as cited.
   - The store-to-judge-brief leg is open (B2).
   - The store's location is the owner's open question 8, which you told me to leave aside.

3. **J7 hands the Reviewer records its pack does not hold. Resolved, with residue (N2, N4, N5).**
   - `[roles.S-001-analysis]` (PACKS.toml:123-130) holds the spec, E-003, reviews/E-003/** and decisions/questions/E-003-*-cards.md. These match S-001:126-129 and :162, and E-003:15.
   - The card path pattern matches the J6 file name. The `*` stays inside one path segment, per the govlib.py docstring (:297-303).

4. **J8's withheld-path list contradicts the pack. Resolved.**
   - `experiments/E-003/C?-*.md` now appears in all of these places: S-001:108, :120, :146, :163; E-003:11; PACKS.toml:119.
   - Case-folded, `c?-*.md` matches `c1-plans-read-the-check.md`. It fails on `check-author-extract.md` at the third character, because "e" is not "-".
   - The extract contains no "arm", no C1 to C3, and no `specs/` or `E-003.md`. I grepped it.

5. **The extract promises sources the pack cannot give. Resolved.**
   - The extract (:12-19) names only Model-Lab's three role files and software.md, and says there is no research playbook.
   - S-001:102 and :132 state the consequence: the Service Desk's pieces are judged by Model-Lab's standard.

6. **Spec and pack disagree; the agent file and brief point at the spec. Resolved.**
   - S-001:108 and J8 now say HOLDOUTS.md is in no pack, which agrees with `always_out`.
   - The extract (:22-29) says the agent file's lines about reading a spec, committing and handing off do not apply, and that a brief's spec line does not apply either.
   - No BRIEFS route is needed, since the pack is hand-assembled.

9. **Judge brief differs from E-002's template without saying so. Resolved.**
   - E-003:53-60 lists seven changes: role and file, piece label, "Judge it against" (per kind, including plans), the added check, the web line for research, the return line, and foreground only.
   - I compared them against E-002:22-36. Nothing else differs, apart from the trivial label in the template's line 24.

## Findings

1. **BLOCKING (B1). The blind dispatch's guarantee is certified by a folder manifest, not by what the session could read.**
   - AC4 (S-001:146) and J8 (:163) rest on a hand-assembled "pack folder" and a recorded manifest of its paths and SHA-256s.
   - The only record of how sessions get repositories (intake/P-001-environment-2026-11-04.md:20-27) says the opposite of confinement: "Subagents you start share this container", and "Helpers … can read every repository that session holds".
   - So /home/user/Model-Lab/specs/S-001.md, experiments/E-003.md and the C-files are readable by the blind Check author whatever its folder holds.
   - The scripted runner would have enforced the pack; this route does not, and no record shows another mechanism.
   - J8 would pass with a manifest that is correct and a session that read the spec. That is the same defect I flagged in round 4 finding 1 ("J8 would pass while the route is broken").
   - The arms get a read-outside-the-copy leak test (E-003 Exclusions 2). The blind Check author gets none.
   - S-001:132 does not list this among the limits.
   - Fix, in the Definer's lane:
     - State that the pack is a convention in a shared container.
     - Add to AC4 and J8 a transcript check that the blind session made no read, search or command on any path outside its pack. A hit voids the held-back check for that kind.
     - Add the limit to S-001:132.

2. **BLOCKING (B2). No named role places the held-back text into each judge's brief and checks its fingerprint, and the only candidate cannot hold the record.**
   - The text:
     - J4 (S-001:159) says "read by the harness from the held-back store, whose SHA-256 … must equal the recorded fingerprint".
     - E-003 Step 4 (:51) puts the full text into every judge's brief.
     - E-003:13 has the Builder build the harness, and it "starts every helper session".
   - The Builder's pack hides both governance/HOLDOUTS.md and holdouts/** (PACKS.toml:70-71, "the hidden holdout checks"). The runner keeps the record out of every pack (session_runner.py:356-358).
   - The recorded fingerprint lives only in HOLDOUTS.md. No record says who hands it, or the store path, to the harness, or who fills the brief.
   - Either the Builder's session gets the text and the record, against its own pack, or the Orchestrator does it, which no line says.
   - A second leak follows. E-003 Exclusions 3 has the harness record each run's full starting context. For judges that context holds the held-back text. If it is saved under reviews/E-003/**, it is written into a repository, against S-001:122 ("never … into any repository"). The new Reviewer pack would then hold it (PACKS.toml:128).
   - Fix, in the Definer's lane, with the Chief of Staff and Orchestrator:
     - Name the role that reads the store, checks the fingerprint, fills the judge brief and starts the judge. The Orchestrator is the only role whose lane (SURFACES.md:52) holds HOLDOUTS.md, so it is the likely candidate.
     - Say how the Builder's harness is tested without the real text, using a stand-in file in J4.
     - Say where the filled judge briefs and transcripts go, and that the held-back text is excised from anything the Reviewer or a repository holds.

3. **Not blocking. Stale "Needed outside" items.**
   - S-001:227-229 still ask for corrections that PACKS.toml:103-130 already makes. The pack uses `C?-*.md`, and its comment already says the Orchestrator adds the agent file and brief.
   - They also say "the Chief of Staff adds" the analysis pack, which is already added.
   - Update them to "done at ec29f46, owner's approval pending (open question 5)".

4. **Not blocking. The manifest has no defined form.**
   - S-001:116, :128, :163 and :231 say "recorded in the dispatch's brief record (docs/briefs/)". The existing records have no manifest field; the grep hits for "manifest" in docs/briefs are only briefs 32, 36 and 38.
   - The check author (b) cannot write a parseable J7 or J8 test without a named heading and line format. Name it.

5. **Not blocking. The Reviewer's pack lacks what J7 asks for.**
   - J7 and E-003 want "power at that size stated" for a kind stopped early. Only sizes 15, 22, 30 and 45 appear in the spec, and the generator experiments/E-003/sizing.py is not in `S-001-analysis`.
   - Add sizing.py, or have the spec state the Reviewer computes it.
   - Also unchanged since round 4 finding 10: reviews/E-003/** is the Orchestrator's lane (SURFACES.md:46), but the Builder's harness produces the results and cannot write there (:65-70). Name the route.

6. **Not blocking. HOLDOUTS.md does not state the fingerprint algorithm.** HOLDOUTS.md:1-10 says only "fingerprints". The algorithm lives in the spec, E-003 and the extract. Add one line there when the Orchestrator makes its first entry.

7. **Not blocking. A return-recording hazard.**
   - The extract (:57-60) has the author return each check's full text.
   - The Orchestrator's habit is to record returns verbatim (CLAUDE.md, this repository's reviews/ practice).
   - Say in S-001:231 that this return is not recorded in any repository.

8. **Not blocking, unchanged. C2 file :15 says "at most 3 of the 16"; S-001:30 says "3 to 5 of 16 … 11 to 19 points".** This was round 4's join-up table, row 1 (e). It is not among the seven findings.

## Did any change alter a threshold, size, option or criterion's meaning?

No change I can see alters one.
- Unchanged against the figures I recorded in rounds 3 and 4 (the repository carries no earlier copy I could diff):
  - 1 in 40
  - 8 cards, split 4/2/2
  - at least 6 answered, at most 2 disagreements, up to 12 cards
  - 16-week review points
  - 10% reserve
  - the tables of weeks, power, runs and tokens
  - options A to D (732, 490, 266 and 1,040 runs)
  - the false-pass guard
- AC4's wording now names the per-task pack and the separate sessions. That ties the criterion to the mechanism in B1 and B2 but does not change what it requires.

## The six-part contract

1. **What I changed:** Nothing. I am read-only and wrote no file.
2. **Why:** To check the Definer's fixes (8df159b) and the Chief of Staff's PACKS.toml change (ec29f46) against the join-up review's findings 1 to 4, 5, 6 and 9, and to read the tools the plan connects to.
3. **What I verified:**
   - The route, store and Reviewer-pack text in the spec, E-003, the extract and PACKS.toml, read side by side.
   - That `C?-*.md` matches the change files and not the extract, by reading the glob rules (`?` and `*` stay within a segment).
   - That the extract holds none of "arm", C1 to C3, `specs/` or `E-003.md`.
   - E-003's list of template changes against E-002:22-36.
   - The runner's role lines, `norm`, `always_out` and `manifest_problems`.
   - SURFACES.md lane lines.
   - The intake's statements on shared repositories.
   - v3_checks.py's `check_holdouts` exists as cited.
4. **What is undone:**
   - I ran no command, so no `git diff` and no test run.
   - I did not read `_segment_regex`, `pack_entry` or RUNNER.toml.
   - I did not read the whole of the Service Desk's files, and checked only critic.md line 31 there.
   - I did not re-check findings 7, 8, 10 and 11 of round 4, which this review did not cover.
5. **Needed outside my lane:**
   - The Definer: B1 and B2, and findings 3 to 8.
   - The Orchestrator: say whether it is the role that fills the judge briefs and checks the fingerprint, and the manifest format.
   - The Chief of Staff: a HOLDOUTS.md line on the algorithm, and a route for results into reviews/E-003/**.
6. **Open questions:**
   - Which role fills the judge brief from the held-back store and checks the fingerprint: the Orchestrator, or a Builder harness run with a text it was not meant to hold?
   - Does the owner accept a convention-only blind pack plus a transcript check, or want the blind author started in a session that holds no Model-Lab repository (the intake says repositories are fixed when a session starts)?

Files: /home/user/Model-Lab/specs/S-001.md, /home/user/Model-Lab/experiments/E-003.md, /home/user/Model-Lab/experiments/E-003/check-author-extract.md, /home/user/Model-Lab/governance/PACKS.toml, /home/user/Model-Lab/governance/HOLDOUTS.md, /home/user/Model-Lab/governance/SURFACES.md, /home/user/Model-Lab/governance/checks/session_runner.py, /home/user/Model-Lab/governance/checks/govlib.py, /home/user/Model-Lab/intake/P-001-environment-2026-11-04.md.

## New draft, round 1 (with the join-up review closing Design)
Verdict: FAIL

# Plan review, round 1 of the new draft of S-001 / E-003 (commit ce860ed)

I am the Critic, on claude-sonnet-5-5. I wrote nothing and ran no command, because I have no shell.

I read:
- specs/S-001.md, experiments/E-003.md, experiments/E-003/check-author-extract.md, docs/design/JOIN_UP_REVIEW.md
- governance/PACKS.toml, HOLDOUTS.md, SURFACES.md
- session_runner.py (`norm` :225, `always_out` :356, `manifest_problems` :708, `PACK_OF` and `SESSION_ROLES` :135-138)
- govlib.py (`glob_to_regex` :297, `glob_match` :331)
- the intake record, src/E-001/RESULT.md (:1-40, :150-180, :286-305)
- the rulings P-001-heldback-store, P-001-plan-stop-2 and P-001-model-lab-public, and P-001-work-repo
- triage round 5, reviews/S-001/plan.md round 4, and PROJECT.md :40-66

I re-did the run, reserve-split, checkpoint and week arithmetic for options A to D and for 40, 60 and 100 pairs. All of it holds: 266 / 266 / 200 runs, 732 in total, 36 checkpoints pooled against 33 split, and the weeks sums of 60 to 121 and 32 to 64.

Not verified:
- The 50,540-byte pack size, since I have no shell.
- Whether the sheets repository really is absent from other sessions. No record shows it.

## Findings

**Blocking**

1. **The central guarantee rests on an unrecorded fact, and K1 does not test it.**
   - specs/S-001.md:130 says a session that never holds the sheets repository "cannot fetch one" because the repository is private.
   - No record shows that. The intake's own listing from the Chief of Staff and Orchestrator session shows the private repository (intake:5-16, :31). That session also has GitHub tools.
   - The only support is that the permission check refused the operating-model repository until the owner allowed it (src/E-001/RESULT.md:161).
   - K1 (S-001:146) lists only the session's own status and its checkouts under /home/user. It never probes what the session's tools or git can reach.
   - K1 also runs at each work session's start, after a sheet may already exist. A leak is then found after exposure.
   - Fix:
     - Add a K1 probe: a read of the sheets repository through the session's GitHub tools, and a `git fetch` of it, must both be refused.
     - Run it before the first sheet is written.
     - Run it in the Orchestrator's session and in every work session.
     - Say what happens if either succeeds.

2. **The work and judging sessions must live for weeks, and nothing says how they are woken. The owner's actions omit it.**
   - Pieces arrive over 7 to 64 weeks per kind (S-001:75-87). A machine is reclaimed after inactivity (intake:28).
   - Nothing says what starts the arms when a piece is dispatched. They must start within the same hour and within 7 days of the real dispatch (S-001:60, E-003:54).
   - Nothing says who wakes the work session, or how often.
   - K5 (S-001:150) and the "not estimated" for lost sessions (:111) treat reclaim as a rare event. With batches spread over weeks it is the normal case. Every batch could need a new judging session, and the owner starts those.
   - So the owner's burden is understated. The "3 sessions, 2 records, at least 1 batch" (:111-113, :119) leaves out a wake-up per piece or batch and a new session per reclaim.
   - Fix:
     - Say what triggers a pair.
     - Give the owner's actions per kind as a range, with reclaim expected.
     - Or name a cadence and put its cost in options A to D.

3. **Required results have no route out of the sheets-side sessions.**
   - The J4 block is exactly ten lines (S-001:224). The J5 closing block is the verdict file plus `sha256` (:225). Any other line is refused.
   - Yet E-003:92 reports the results of K1 to K6, J7 (:227) hands them to the Reviewer, and :310 has them recorded in sessions.md.
   - K2's repository list, K3, K4 and K5 are produced only inside the sheets-side sessions. K2 and K4 are the second line for AC4 and AC5. No fixed-form line carries them.
   - AC8 and E-003:97 need the judging side's runs, tokens and pairs left out on the combined counts card. Only "as its lead last reported them" is said; no form or route.
   - Fix:
     - Add fixed-form lines for the K results (for example `k2: ok`, `k4: ok`) and for the counts, to J4 and J5.
     - Extend J5's test to match.

4. **The milestones header repeats round 4 finding 10.**
   - S-001:7 reads `milestones: M2`. E-003:5 names M2 and M4.
   - AC4 to AC10 deliver the runs and results of M4 ("Each tested change has a result", docs/PROJECT.md:66).
   - Name both milestones in S-001, or say which acceptance criteria belong to which.

**Not blocking**

5. **The "judges in their own sessions" reading is not clearly supported by the ruling's words. It must go to the owner before the freeze.**
   - The words are "the sheet writer and each judging in their own sessions" (P-001-plan-stop-2.md:10) and "the sessions that judge" (P-001-heldback-store.md:1).
   - The plainer reading is each judging in its own session, about 120 sessions a kind (S-001:296).
   - The draft reads it as one judging session per kind, with each judge a helper (:122). That is a departure, and AC5, the session table and the owner's costs all rest on it.
   - The draft does ask the owner (open question 8), and it states the cost. That is the right route.
   - The answer is due "at the Build gate" (:302). Move it before the freeze, because a per-judge answer changes AC5, J5 and the owner's burden.
   - Per-judge sessions would add little isolation, since every session can read public Model-Lab (:197).

6. **A sheets-side session's helpers share its machine, and what that machine holds is not confined.**
   - The sheet session's clone of the sheets repository holds earlier kinds' sheets and verdict files. The blind Check author for a later kind shares that machine (intake:22, :26).
   - Under option "together" it could also see a running kind's partial verdicts. The only guard is the transcript check.
   - The pack folder's location is not stated. A folder under a checkout, or in a directory with an instructions file, brings extra context (src/E-001/RESULT.md:292).
   - State that the pack folder sits outside every clone and outside any directory with an instructions file.
   - Say what the sheet session may hold of earlier kinds.

7. **The K3 fallback is incomplete and contradicts K2 (S-001:148).**
   - It covers briefs, pack files and exports.
   - The Builder's three scripts (the fill script, the transcript check and the export reader) also come from Model-Lab (:185, E-003:14). The fallback does not mention them.
   - The fallback's "second private repository started with the judging session" breaks K2's "sheets repository only" and AC5's "no work repository".

8. **J5's test overclaims (S-001:225).**
   - It says "no other text, a sheet's above all, can be carried".
   - `<path>` in `<n>@<path>:<line>` is free text a judge writes, so a sheet quotation could pass as a path.
   - Require the lead to check that the path names a file in the judged export. Add a length and character limit.

9. **Two lines about governance/PACKS.toml disagree.**
   - S-001:303 says the earlier change was reverted on the default branch.
   - S-001:304 says `[roles.S-001-holdout]` is "today in the file with the earlier text".
   - The file at ce860ed holds it (PACKS.toml:103-120): `C1-*.md`, `C2-*.md` and `C3-*.md` patterns, and no `reviews/E-003/**`.
   - Say which tip is the starting state, so the Chief of Staff's edit starts from the right text.
   - I checked the planned `C?-*.md`:
     - `?` is one non-slash character (govlib.py:290).
     - Matching is case-folded (session_runner.py:225).
     - It does not match check-author-extract.md, and it does match the C-files.
     - Confirmed.

10. **Exports carry whole start trees into public Model-Lab.**
    - J3 (S-001:223) and E-003:57 put the start commit's full tree in every export.
    - For the private operating-model and portfolio repositories that is more than "records" (P-001-model-lab-public.md:10).
    - The spec is silent. Either restrict entry to public repositories, or add this to open question 8 or 5.

11. **K5's fallback misses a lost sheet session (S-001:150).**
    - A sheet session lost before step 4's push loses the Check author's return. It is held nowhere else (:176, :191).
    - Say that a new sheet is written (set id n = 2, 1 run, counted).

12. **The extract and E-003 differ on what a judge is given.**
    - Extract lines 35-36 say the check judges "the piece alone". E-003:68 gives plans the task statement text and research the question file. The plans row (extract:12) does not mention it.
    - Add one sentence to the extract. This is a frozen file, so do it before the freeze.

## Items you asked me to judge

- **Session kinds against the recorded facts.** The start, repositories and helpers are consistent with the intake (:21, :22, :26) and with RESULT.md (:9, :11, :158, :166-175, :299). Gaps are in findings 1, 2, 6 and 7.
- **K1 to K6 and their fallbacks.**
  - K1 is unsound as written (finding 1).
  - K2 is fine.
  - K3's fallback is incomplete (7).
  - K4's fallback is honest: it asks the owner.
  - K5 misses the sheet session and is mis-framed as rare (2, 11).
  - K6 relies on instructions plus a count of calls naming the repository. Arm transcripts are covered; the work session's own transcript is not, as the spec admits (:197).
- **Sheet text in any record.**
  - I found no record that carries a sheet's text.
  - The routes are the fixed blocks, the unrecorded Check author return, the filled briefs that are not stored, and the Reviewer's pack (which holds only the verdict record and numbers).
  - Finding 8 is the weakest point. The rest relies on the transcript checks.
  - HOLDOUTS.md stays out of every pack (`always_out`, session_runner.py:356-358).
  - I found no `arm`, no C1 to C3 and no change-text phrase in the extract.
- **Roles under lane and pack.**
  - PACKS.toml is the Chief of Staff's, who proposes (SURFACES:83).
  - HOLDOUTS.md and reviews/** are the Orchestrator's (:46, :52).
  - Cards go in decisions/**, the Chief of Staff's.
  - Exports and records go in src/**, the Builder's (:65-70).
  - The locked checks go in tests/acceptance/** and checks/**, the Check author's.
  - The leads write to a repository with no surface map; the spec says so and it is acceptable.
  - Every role can do its part, except for the triggers and routes in findings 2 and 3.
- **The owner's actions.** They are stated (:111-119, :302), but not fair or complete until finding 2 is fixed. The sums are right: 9 session starts, 6 records passed and at least 3 batch messages for option A.
- **Repeats from earlier rounds.** The milestones header repeats round 4 f10 (finding 4). The hand-built pack route (round 4 f1 and round 5 B1) is now handled by sessions plus a transcript check. Round 4 f4 (`C*.md` matching the extract) is fixed by `C?-*.md`.

## Join-up review — Design, 2026-11-04 (in the form of docs/design/JOIN_UP_REVIEW.md)

**Screens checked:** none. P-001 has no screens or views. As in round 4, I checked the parts side by side:
- specs/S-001.md (AC1 to AC11, J1 to J8, Needed outside)
- experiments/E-003.md
- experiments/E-003/check-author-extract.md
- governance/PACKS.toml `[roles.S-001-holdout]`
- governance/HOLDOUTS.md
- governance/SURFACES.md
- session_runner.py
- the intake record
- src/E-001/RESULT.md
- the rulings

| Check | Result | Fix |
|---|---|---|
| One meaning per term, threshold and id | Mostly pass. Pairs, runs, reserve (⌈10%⌉, judging side rounded down), 1 in 40, 6 cards and 2 disagreements, 8 to 12 cards, 16 weeks and 7 days agree across the spec and E-003. Differences: milestones M2 against M2 and M4 (blocking, finding 4); "judges in their own sessions" is read two ways (5); "readable only by CI" in HOLDOUTS.md:3 is queued for correction (S-001:307). | 4, 5 |
| One route | Fails at three places. (1) The K2 to K5 results and the counts card have no carrying block (3). (2) The work and judging sessions' wake-up route is missing (2). (3) K1 does not test the fetch route that the guarantee rests on (1). The pack route, the sheet route (J4), the judging route (J5), the card route (J6) and the Reviewer route (J7) match end to end. | 1, 2, 3 |
| Consistent names, paths and ids | Mostly pass. The cited pack lines, runner lines (:135-138, :225-227, :356-358, :464-472), SURFACES lines and intake lines exist and say what is claimed. The state of PACKS.toml is contradicted at S-001:303 and :304 (9). The K3 fallback's second repository contradicts K2 and AC5 (7). | 7, 9 |
| No two parts doing the same job, no job without a part | Pass on duplicates: the two Check author dispatches are separate and kept so. Unowned jobs: waking the work session (2), the counts card's judging side (3), and the K1 probe of tool reach (1). | 1, 2, 3 |
| Every datum available from the records, or listed as a needed change | Fails at three places: the K results and the judging-side counts (3); the start commit in Model-Lab's briefs (listed, owner's order, open question 5); and the privacy of whole-tree exports (10). | 3, 10 |

**Needed changes to the records:**
- Fixed-form lines for the K results and the counts in J4 and J5.
- The K1 probe.
- The starting state of PACKS.toml.
- The start-commit field in Model-Lab's briefs (already listed).

**Blocking differences:** findings 1 to 4. The others are non-blocking and carry to the gate's case as risks.

## Sign-off
The owner's ruling at the gate: decisions/P-001/criteria-<n>.md. Not yet recorded.

## The six-part contract

1. **What I changed:** Nothing. I am read-only and wrote no file.
2. **Why:** To review the new draft of S-001 / E-003 from round one, as the brief asked, and to add the Design join-up review.
3. **What I verified:**
   - I read the files listed above in full or at the cited lines.
   - I recomputed the run, reserve-split and checkpoint arithmetic for options A to D and for 40, 60 and 100 pairs.
   - I read the runner functions, `glob_to_regex`, PACKS.toml and SURFACES.md for lane and pack facts.
   - I grepped the extract for `arm`, C1 to C3 and spec words.
   - I checked the cited intake lines, RESULT.md lines and ruling lines against the text.
4. **What is undone:**
   - I could not run a command, so I did not run `wc -c` on the pack, sizing.py, arrivals.py or any test.
   - I did not read the three role files, the playbook or the C-files.
   - I did not read E-001, E-002, Q-008 or the Service Desk's files.
   - Whether the sheets repository is really absent from other sessions is unknown to every record, so K1 to K6 are checked at first use only.
5. **Needed outside my lane:**
   - The Definer: findings 1 to 12.
   - The owner: question 8 (finding 5) and finding 10, ahead of the freeze.
   - The Chief of Staff: the PACKS.toml starting state (finding 9).
6. **Open questions:**
   - What starts a pair's arms when a piece is dispatched, and who wakes the work session?
   - Does the owner accept the per-kind reading of "each judging in their own sessions"?
   - May exports of private-repository work be placed in public Model-Lab?

Files: /home/user/Model-Lab/specs/S-001.md, /home/user/Model-Lab/experiments/E-003.md, /home/user/Model-Lab/experiments/E-003/check-author-extract.md, /home/user/Model-Lab/docs/design/JOIN_UP_REVIEW.md, /home/user/Model-Lab/governance/PACKS.toml, /home/user/Model-Lab/governance/HOLDOUTS.md, /home/user/Model-Lab/governance/SURFACES.md, /home/user/Model-Lab/governance/checks/session_runner.py, /home/user/Model-Lab/governance/checks/govlib.py, /home/user/Model-Lab/intake/P-001-environment-2026-11-04.md, /home/user/Model-Lab/src/E-001/RESULT.md, /home/user/Model-Lab/decisions/questions/P-001-plan-stop-2.md, /home/user/Model-Lab/decisions/questions/P-001-heldback-store.md, /home/user/Model-Lab/decisions/questions/P-001-model-lab-public.md, /home/user/Model-Lab/docs/PROJECT.md, /home/user/Model-Lab/reviews/S-001/plan.md, /home/user/Model-Lab/triage/P-001-S-001-round-5.md

## New draft, round 2
Verdict: FAIL

# Plan review, round 2 of S-001 / E-003 (branch head after the merge of 0d79ea9)

I am the Critic, on claude-sonnet-5-5. I wrote nothing and ran no command, because I have no shell.

I re-read S-001 (K1 to K7, the session table, J3 to J5, the owner-action tables, open questions 8 and 9, Needed outside), E-003 (lines 14-17, 34, 41, 55, 70, 94, 109), the extract, and the new intake section (lines 35-42).

I re-did the arithmetic for the owner-action tables:
- Blocks: A 24-27, B 17-19, C 8, D 32-37, with review points counted from each kind's weeks.
- Wake messages: 60-121 and 180-363.
- K5-fails sessions: 183-366.
- The per-judging counts: 132 / 132 / 66 = 330, and 9 - 3 + 330 = 336.

All of it holds.

## Round 1 findings, one by one

1. **K1 reach. Partly resolved; see new finding A.** The probe, the before-the-first-sheet timing and the stop rules are added (S-001:166-171).
2. **Wake route and owner's actions. Resolved.**
   - What starts a pair is stated (:156). The cadence is stated (:157-163). K5 now treats reclaim as expected (:175-179).
   - K7 is added (:181). The owner-action ranges are given, with the K7-fails and K5-fails cases (:122-131).
   - The ranges are consistent with the wake counts.
3. **Results with no route. Resolved.** The J4 block carries k2 to k5 (:258), in full, stopped and void forms. The J5 counts block carries k2 to k5 and k7 plus judging-side runs, tokens and left-out labels (:259). The parser and test are specified.
4. **Milestones header. Resolved.** S-001:7 now reads `milestones: M2, M4`, and both are in docs/PROJECT.md (:57, :66).
5. **"Judges in their own sessions". Handled as an owner question.** Open question 8 now quotes both rulings, says the plainer reading may be one session per judging, gives the costs (about 330 sessions for option A) and is ruled before the freeze (:332-336). That is the right route.
6. **Shared machine. Resolved.** The pack folder is in a new empty folder outside every clone and any instructions file (:206). The sheet session holds nothing of earlier kinds (:213). The E-003 mirror is at :34.
7. **K3 fallback. Resolved.** Scripts are now covered, and no second repository is given. The spec stops the test or orders a revision (:173).
8. **J5 overclaim. Resolved.** The path is limited by form (1 to 200 characters), must name a file in the export tree as the export reader lists it, and the test checks that, the test number and the label against the INDEX (:259).
9. **PACKS starting state. Resolved.** The default branch at eb8fe9d is named (:346).
10. **Whole-tree exports. Put to the owner as open question 9.** Both outcomes are stated (:337-339). Acceptable.
11. **Sheet lost before the push. Resolved.** n = 2, 1 run, counted (:178; E-003:41).
12. **Extract and judge inputs. Resolved.** The extract now has the plans row "with the task statement it was written to" (line 12) and the "judge is given beside it" wording (lines 35-42).

## New findings

**A. BLOCKING. K1's probe cannot detect the reach it tests (S-001:168, :344).**
- Each part passes if it is "refused or returns nothing". The probe runs before the first sheet is written, so the sheets repository then holds nothing.
- A readable empty repository also "returns nothing" to a root read through the session's GitHub tools. It also returns nothing to `git ls-remote` and to a `git fetch`.
- So the probe passes whether or not the reach exists. That is the very thing the guarantee at :142 rests on.
- Fix:
  - Have the owner put one harmless canary file in the sheets repository, such as a README with a fixed word, before the probe.
  - Require parts (i) and (ii) to be refused and not to show the canary.
  - Change :344 ("holding `holdouts/` and `verdicts/` only") to allow that file.
  - Have the J4/J5 `k1`/sessions record say which word was or was not seen.
- Part (iii) is fine, since an open sheet session has events.

**B. Not blocking. Probe parts after a sheet exists can expose it (:169, :171).**
- Every later work session runs the probe at its start. A `git fetch` (part ii) or a root read that succeeds after a sheet exists would bring the sheet to that machine.
- After the first sheet, use `git ls-remote` and a directory-name read of the canary only. Do not fetch.

**C. Not blocking. Part (iii) is likely to fail, and the plain words do not say what that means.**
- The Chief of Staff's session holds `list_events`, which reads another session's events (intake:41). The probe is likely to show the reach.
- The recorded fallback is to go on with the sheet kept from the Orchestrator's side by instruction alone (:170, :229). That side includes the Chief of Staff, who writes the cards and the gate case.
- "In plain words" (:9-18) says nothing of open questions 8 and 9 or of this. Add one sentence to the plain words.

**D. Not blocking. The wakes' tokens are not estimated (:115).**
- About 7 work-session turns a week, over 60 to 121 weeks for option A, is about 420 to 850 turns. Each begins with a listing, plus 60 to 121 judging turns and the weekly Orchestrator turn.
- The owner sets the token budget on 132 million (:95). State at least a bound, or say plainly that the budget excludes wakes.

**E. Not blocking. The weekly landing needs an authority statement (:159, :355).**
- The Orchestrator lands the Builder's records and exports by merge commit weekly, from its own scheduled task. CLAUDE.md requires the full suite and the required reviewers before a merge.
- Say that landing the work session's records and exports is exempt, or what review it gets.

**F. Not blocking. Small form gaps.**
- J5's verdict-line `served model` has no character form, while J4 gives one (1 to 64 characters from letters, digits, `.`, `_` and `-`). Give J5 the same.
- J4's awkward cases still describe a void block as "no block but `set`, `scan: void`, and the hit's line" (:258). The void form now has more lines (runs, tokens, the four k lines). Align the two.
- K5 does not cover a reclaim of the Orchestrator's own session, though its weekly wake is a long-lived turn. K7 covers only its wake.

## Join-up review — Design, 2026-11-04 (round 2, in the form of docs/design/JOIN_UP_REVIEW.md)

**Screens checked:** none. P-001 has no screens or views. I checked the same parts side by side as in round 1: S-001, E-003, the extract, PACKS.toml `[roles.S-001-holdout]`, HOLDOUTS.md, SURFACES.md, the runner, and the intake, including the new tools section.

| Check | Result | Fix |
|---|---|---|
| One meaning per term, threshold and id | Pass. Milestones now M2 and M4 in both S-001 and E-003. Sessions per kind (K1 to K7), the 20-run checkpoints and the J4/J5 forms agree. The k lines use the same three words in J4, J5, E-003:94 and :182. Remaining: J4's void awkward-case text against the void form, and the J5 model field (F). | F |
| One route | Pass for pack, sheet, judging, card and Reviewer routes, and now for the K results and the counts: the J4 and J5 blocks carry k2 to k5, k7 and judging-side counts, and the Orchestrator maps labels from the work side's records. The wake route (daily, weekly, weekly) is stated end to end. One route cannot yet be shown to work: the K1 probe (A). | A |
| Consistent names, paths and ids | Pass. The intake lines cited (:37-42) exist and say what is claimed; the cited runner lines still hold; PACKS.toml's starting state is stated consistently (:346); `C?-*.md` still does not match the extract. The set-id form `S-001-<kind>-<n>` agrees with E-003's naming. | none |
| No two parts doing the same job, no job without a part | Pass. Waking (work, Orchestrator, judging), counts card, landing, K lines and the canary-holder (the owner) each have a part, except the canary file (A) and the landing's authority (E). | A, E |
| Every datum available from the records, or listed as a needed change | Pass except: the canary file in the sheets repository (A), and the whole-tree exports (open question 9, with the owner). The start-commit field in Model-Lab's briefs is still listed under open question 5. | A |

**Needed changes to the records:** the canary file in the sheets repository and its use in K1 (A); the start-commit field in Model-Lab's briefs; the PACKS.toml entries as listed at S-001:346-348.

**Blocking differences:** A only. B to F are carried as risks. Open questions 5, 8 and 9 go to the owner before the freeze.

## Sign-off
The owner's ruling at the gate: decisions/P-001/criteria-<n>.md. Not yet recorded.

## The six-part contract

1. **What I changed:** Nothing. I am read-only and wrote no file.
2. **Why:** To judge each round 1 finding against the Definer's answer, review the new K7, the owner-action ranges and the J4/J5 fixed forms, and update the join-up section.
3. **What I verified:**
   - I read S-001's changed sections, E-003, the extract, the intake and the J3 to J5 text.
   - I re-did the arithmetic for the blocks, wake and session counts.
   - I checked the cited intake lines against the text.
4. **What is undone:**
   - I could not run any command, so I did not run sizing.py, arrivals.py or any test.
   - I did not diff the unchanged parts against round 1 line by line.
   - I did not re-read the C-files or the role files.
   - The tools' behaviour (create_trigger, list_events, GitHub tools) is described but untested; K1, K5 and K7 are the first-use checks.
5. **Needed outside my lane:**
   - The Definer: finding A, and B to F.
   - The owner: open questions 5, 8 and 9 before the freeze, and the canary file.
   - The Chief of Staff: the plain-words sentence (C) and the PACKS.toml entries.
6. **Open questions:**
   - Will `list_events` show the reach (K1 iii)? If so, does the owner go on with instruction alone?
   - Is a weekly landing of work-session records exempt from the stage-5 review?

Files: /home/user/Model-Lab/specs/S-001.md, /home/user/Model-Lab/experiments/E-003.md, /home/user/Model-Lab/experiments/E-003/check-author-extract.md, /home/user/Model-Lab/intake/P-001-environment-2026-11-04.md, /home/user/Model-Lab/governance/PACKS.toml, /home/user/Model-Lab/docs/design/JOIN_UP_REVIEW.md

## New draft, round 3
Verdict: PASS

# Plan review, round 3 of S-001 / E-003 (branch head after commit 3077c89)

I am the Critic, on claude-sonnet-5-5. I wrote nothing and ran no command, because I have no shell. I re-read the changed parts of S-001 and the lines they touch. These are the plain words (:16-18), the tables (:111-135), the landing's authority (:165), K1 to K7 (:170-189) and J4/J5 (:266-267). I also checked the new citations against governance/risk-paths.toml and re-did the arithmetic for the new owner-action columns.

## Round 2 findings

**A (blocking). Resolved.**
- The probe now has a canary: a `README.md` that the owner places before any probe. It holds one word, which the owner gives only to each sheet session's lead (S-001:172).
- Before the first sheet, parts (i) and (ii) pass only if each is refused and the canary is not shown. Part (iii) passes only if refused. An empty repository can no longer pass (:174).
- The probing session records one line per part. The sheet lead reads those records and says in `k1-canary:` whether it saw the word (:175-176). The probing session does not know the word, so it cannot judge its own return. That is a sound split.
- The sheet lead starts the Check author only if every part reads `refused` and the canary is shown in neither record. Otherwise it stops with `stopped: k1` (:176; J4 stopped form).
- Needed outside now lists `README.md` in the repository (:353).

**B (not blocking). Resolved.** After the first sheet exists, nothing is fetched or opened. Part (i) lists root names only, part (ii) is `git ls-remote` only, and part (iii) is not run again (:174).

**C (not blocking). Resolved.** The plain words now carry open questions 8 and 9. They also say that part (iii) will likely show the reach because the Chief of Staff's session holds a tool that reads other sessions' transcripts. The consequence is stated: the sheet is then kept from the side that writes the cards and the gate case by instruction alone, unless the owner changes the access or stops the test (:18).

**D (not blocking). Resolved.** The budget is stated to exclude the wakes. The wake counts are given (about 420 to 847 work-session turns, 60 to 121 each for the Orchestrator and judging sessions, 540 to 1,089 in all). No cost per turn is claimed. This is honest (:16, :124).

**E (not blocking). Resolved.** The weekly landing is not exempt from review. Its paths are class R1 (governance/risk-paths.toml:22) and need a Reviewer's verdict (:29). The landing takes the surface guard, the full suite, a Reviewer helper and a merge commit on PASS. A FAIL means nothing lands that week, and AC2's 7 days run to the start of a pair, not to the landing (S-001:165). The risk-paths citations check out. I did not open AGENTS.md §1 and §4.

**F (not blocking). Resolved.**
- J5's served model now has J4's form (1 to 64 characters from letters, digits, `.`, `_` and `-`).
- J4's void awkward case now says "the void form above and no other".
- K5 covers the Orchestrator's own session, and its failure adds a column to the owner-action ranges. I re-did the arithmetic: A 243-487, B 163-327, C 29-61, D 351-695. All correct.
- J4 and J5 gain the `k1-canary` line, with its three words in the parser's form.

## New findings (all non-blocking)

1. **The owner's per-kind relays are not in the owner-action tables (S-001:112-114, :126-135).**
   - K1 asks the owner, per kind, to give the sheet lead the canary word. It also asks for the sheet session's id for part (iii) and the Model-Lab commit of each K1 record (:172, :176). These are about three to four messages a kind.
   - They are small and fixed, but the tables count only starts, blocks and wake messages. Add one line, or say "plus about four short relays a kind".

2. **Detection lag on the judging side (:176).**
   - The judging lead reads the K1 records added since its last block, at the tip of the landing branch. Landing is weekly and reviewed. A `seen` in a work session's record can therefore reach the judging lead a week or more later, during which judging goes on.
   - The sheet is already treated as seen from the moment of the reach, and the kind stops when the lead finds it. The lag is acceptable, but say so in the kind's record limits (:229-237).

3. **The canary word could enter a public record if a probe succeeds (:175).**
   - A `returned <first line>` record carries README's first line into Model-Lab. This happens only on a failed K1, where the kind stops anyway.
   - Keep the word on README's first line only, and tell the owner not to reuse it.

4. **Small: :122 ("Once for the whole test") does not mention the canary.** It does elsewhere (:17, :353). One phrase will fix it.

## Join-up review — Design, 2026-11-04 (round 3, in the form of docs/design/JOIN_UP_REVIEW.md)

**Screens checked:** none. P-001 has no screens or views. I checked the same parts side by side as before: S-001, E-003, the extract, PACKS.toml `[roles.S-001-holdout]`, HOLDOUTS.md, SURFACES.md, risk-paths.toml, the runner and the intake.

| Check | Result | Fix |
|---|---|---|
| One meaning per term, threshold and id | Pass. M2 and M4 agree; K1 to K7, `k<n>` and `k1-canary` words agree across J4, J5 and E-003; the model form is now the same in J4 and J5; the void form agrees with its awkward case. | none |
| One route | Pass. Pack, sheet, judging, card, Reviewer and landing routes match end to end. The wake route (daily, weekly, weekly) is stated. K1 is now able to detect a reach, through the canary read by the sheet lead. The landing route is reviewed under R1. | none |
| Consistent names, paths and ids | Pass. The cited intake lines (:37-42), runner lines and risk-paths lines (:22, :29) exist and say what is claimed. The PACKS.toml starting state is consistent (:346). `C?-*.md` does not match the extract. | none |
| No two parts doing the same job, no job without a part | Pass. The canary has an owner and a reader; the landing has a Reviewer. Small gap: the owner's per-kind relays are uncounted (new finding 1). | 1 |
| Every datum available from the records, or listed as a needed change | Pass. The canary file is now listed (:353). The start-commit field in Model-Lab's briefs is under open question 5. Whole-tree exports of private repositories are with the owner as open question 9. | none |

**Needed changes to the records:** the canary file in the sheets repository; the start-commit field in Model-Lab's briefs; the PACKS.toml entries as listed at S-001:346-348.

**Blocking differences:** none. The non-blocking items above are carried into the gate's case as risks. Open questions 5, 8 and 9 stay with the owner before the freeze.

## Sign-off
The owner's ruling at the gate: decisions/P-001/criteria-<n>.md. Not yet recorded.

## The six-part contract

1. **What I changed:** Nothing. I am read-only and wrote no file.
2. **Why:** To judge whether round 2's findings A to F are resolved and whether the changes introduce anything new, and to update the join-up section.
3. **What I verified:**
   - I read the changed text of S-001 at the lines cited above.
   - I re-did the arithmetic for the new K5-in-the-Orchestrator column.
   - I checked the risk-paths citations against the file.
   - I confirmed that J4 and J5 give the `k1-canary` line in the parser's form.
4. **What is undone:**
   - I ran no command, so I did not run sizing.py, arrivals.py or any test.
   - I did not read AGENTS.md §1 and §4.
   - I did not diff the sections that rounds 1 and 2 passed.
   - The tools' behaviour (create_trigger, list_events, GitHub tools) is still untested; K1, K5 and K7 are the first-use checks.
5. **Needed outside my lane:**
   - The Definer: new findings 1 to 4, optional before the freeze.
   - The owner: open questions 5, 8 and 9 before the freeze, and the canary file.
   - The Chief of Staff: the PACKS.toml entries.
6. **Open questions:**
   - Will the first K1 probe show the `list_events` reach? If so, does the owner go on with instruction alone?

Files: /home/user/Model-Lab/specs/S-001.md, /home/user/Model-Lab/experiments/E-003.md, /home/user/Model-Lab/experiments/E-003/check-author-extract.md, /home/user/Model-Lab/governance/risk-paths.toml, /home/user/Model-Lab/intake/P-001-environment-2026-11-04.md, /home/user/Model-Lab/docs/design/JOIN_UP_REVIEW.md

## New draft, round 4 (commit 9b805dd; brief 57, a fresh session; a focused check of the Definer's fix e504ea0)
Verdict: PASS

Findings:
1. (Not blocking) Every changed sentence is true of experiments/E-003/sizing.py lines 135-149 and experiments/E-003/output.txt lines 89-93.
   - `seq` is the sum of the kinds' weeks, and `par` is the maximum of them.
   - Option A comes out at 60 to 121 weeks one after another (39) and 32 to 64 together (24). Research alone at 60 pairs is 32 to 64 (output.txt line 62), and it is the slowest kind: plans are 21 to 42 and built work is 7 to 15.
   - The option table (S-001 lines 96-99) matches all four options: A 60–121 (39) and 32–64 (24); B 40–81 (26) and 21–43 (16); C 7–15 (6) twice; D 87–173 (59) and 53–107 (39).
   - Line 15 gives 60 to 121 one after another and 32 to 64 if all three collect from the start. Line 317 gives plans 21 to 42 and research 32 to 64. Both are true.
   - Line 308 quotes output.txt's own "together" wording, which is the script's label and is correct there.
2. (Not blocking) Each order in open question 4 (lines 337-341) carries the weeks true of it.
   - Order 1, one kind after another: 60 to 121 weeks of collection, plus waits between kinds that no record measures. Line 338 says this, and it matches the bound at line 120.
   - Order 2, the next kind collecting while the previous is judged: the same 60 to 121 weeks of collection, with only the waits saved. This is the correction the fix was meant to make. Nothing in sizing.py supports a shorter figure for it, and none is claimed.
   - Orders 3 and 4: 32 to 64 weeks, as the slowest kind. Line 341 also says E-003 registers analysis one after another, so order 4 needs that registration revised before any run. That is right, because E-003 line 101 says "kinds are still analysed one after another".
   - The ruling quote in line 337 matches line 1 of decisions/questions/P-001-worst-work.md. The owner's verbatim words there are "I don't care to start, let's just work it incrementally because everything should be touched". The spec states "Follows 'incrementally' literally" as its own reading and puts the question to the owner. That is an honest framing, not a claim about the ruling.
3. (Not blocking) The plan is consistent with itself and with E-003.
   - Line 90's header and line 94's column heading agree with each other and with line 15.
   - Line 126's claim that an overlapping order "does not change these counts, which are per kind-week" holds for order 2 as well. The counts are 7, 1 and 1 a week while a kind runs, and 1 landing review a week, so the totals follow from the kind-weeks (line 16: 540 to 1,090 wakes).
   - Line 221's "if the owner lets kinds overlap" now covers orders 2 to 4 and is still true.
   - The Weeks row at line 120 ("the tables' figures, plus up to 2 weeks before a kind closes") is unchanged and does not contradict anything.
   - E-003.md line 101 matches the spec. "Only the second shortens collection" refers to all three collecting from the start. Under the first, collection takes the one-after-another weeks. "Kinds are still analysed one after another" is consistent with order 4 being excluded from E-003 as registered.
   - The K checks, the AC and J lines and the Risks do not mention the "together" weeks, so nothing else is made false.
4. (Not blocking, out of scope) E-003 line 101 does not name order 4 (everything at once). The spec says order 4 needs a revised registration, so no new falsehood arises.
5. The fix touched only the lines named. I found no change beyond its scope and no figure changed.

Contract:
- changed: nothing. I hold no write tool.
- why: this is the round-4 focused check of the fix in e504ea0, landed by merge b527ed9, with the "together" weeks (32 to 64) no longer tied to the next kind collecting while the previous is judged.
- verified: sizing.py lines 100-149; all of output.txt lines 89-93 and lines 62 and 78; S-001 lines 13-16, 88-126, 219-222, 305-346 and every other line the greps matched; E-003.md lines 94-107; the P-001-worst-work.md ruling.
- undone: I did not read the rest of the spec or re-run earlier rounds' checks. I did not run sizing.py (no shell), so I rely on output.txt matching it. I read the code, which computes the sums and maxima those figures need.
- needed outside your lane: the Orchestrator records this verbatim in reviews/S-001/plan.md as round 4, and notes that a round is counted.
- open questions: none for the Definer. The owner's choice among the four orders stays with open question 4.
