*The gate Critic's return on docs/gates/P-001/build-gate-1-case.md (brief: docs/briefs/46-critic-gate.md), on claude-sonnet-5-5, a different model from the case's writer, verbatim. Recorded by the orchestrator. Session session_01QBwHGMBo8kZsMCS2EvKNwd, 2026-11-04.*

**The Critic's recommendation:** hold — the plan itself is sound and I would not send it back to Design, but the case cannot yet support the owner's ruling. Its ask is to approve the criteria as scenarios, set a budget and answer open questions. The case shows the owner none of the three, it states a cost claim that no record supports, and it drops several risks that the plan review says must be carried. The fixes are small. Re-issue the case and it can go to the owner.

## The Critic's independent view

I read the case (docs/gates/P-001/build-gate-1-case.md), the gate form, docs/PROJECT.md and reviews/S-001/plan.md. I read lines 1-30, 240-264, 570-594 and 890-965 of the plan review. I also read all five P-001 rulings the case cites (gate-record, spend-ceiling, heldback-store, e002-not-tested, plan-stop-2) and, as allowed, specs/S-001.md (header, lines 9-19, 326-355). Claims that rest only on the spec are marked "spec only".

**What is fair to the plan**
- The case is right that the plan passed review and that the join-up review has no blocking difference (plan.md:1, :939).
- The case is right about the run arithmetic: 732 = 266 + 200 + 266 (plan.md:14, :583).
- The weeks figures, 60-121 one kind after another and 32-64 together, match plan.md:253. They are quoted at the Service Desk's pace, and only the bracketed three-project figures need the other projects to resume.
- The case is also right that secrecy from the card-writing side rests on instruction alone (plan.md:897).

**What the case leaves out that the owner needs**
1. **No scenario is shown.** Section 1 asks the owner to "approve the fair test's criteria as scenarios", and section 8 says they are "frozen after this ruling". The case quotes none of AC1 to AC11. They exist only in the spec (spec only, S-001.md:250-260), which the case cannot cite. The owner cannot approve what the case does not show.
2. **No budget options are shown.** The case asks the owner to "set its budget" and gives one number, option A. The plan's options A to D (490, 732 and 1,040 runs, plus option C) are in plan.md:253-256. Neither the cost nor the time of the other options appears. The owner's earlier ruling covers only about 100 runs through Design, and PROJECT.md:117 says "about 300 runs". The case never says that 732 is more than twice that figure.
3. **The open questions are not listed.** Section 8 says "Your answers to the open questions". It does not say what they are. They are 9 questions (spec only, S-001.md:333-348), and they include real rulings. They cover rewording V1 and M2's "done when" because past tasks cannot be replayed, one kind at a time versus all at once, a firm time limit, the judge model, whether to keep one judging session per kind or one per judging, and whether whole exports of private repositories may sit in public Model-Lab.
4. **The headline limit on what the test can show is missing.** The spec says a real 20-point gain is seen about 4 times in 5 at best. For research and built work it is about 1 in 2 if the two versions disagree as often as chance allows. A judge that is wrong 1 time in 10 lowers that further. Smaller gains will usually read "not shown" (spec only, S-001.md:13-14). This is the biggest risk to the owner's V1 target and section 5 does not carry it.
5. **Section 5 does not carry what the plan review said it must.** plan.md:939 says "The non-blocking items above are carried into the gate's case as risks". The case carries none of these:
   - the owner's per-kind relays are uncounted (plan.md:911-913);
   - judging lag of a week or more (plan.md:915-917);
   - the canary word could enter a public record (plan.md:919-921);
   - the missing start-commit field in Model-Lab's briefs, which means plans and built work cannot enter at all until it is recorded (plan.md:935, :960; spec only, S-001.md:338).

   The form also asks of each risk what we would do and where it stands now. Section 5 says neither for any risk.
6. **The ownership of the rule changes is blurred.** The spec says the governance/PACKS.toml entries are reviewed, approved by the owner as a rule change and merged before this gate, and that the Orchestrator confirms them in the case (spec only, S-001.md:355). The case says only that "reading lists ... are proposed beside this case". The owner's one-time set-up tasks are also not named in section 8. These are creating the private sheets repository and the canary file, and checking that the environment does not add it to every session (heldback-store:12; spec only).
7. **Owner-facing wording.** Words such as "marking sheets", "kind", "the side writing your cards" and "secret sessions" are not defined for a non-expert. "Sheet writer" is also unexplained.

**Form.**
- The standard visuals for sections 2, 3, 4 and 6 and the research and check outcomes visual in the appendix are absent. Section 3 has no screens, so the thumbnails do not apply.
- The word count of sections 1-8 is about 320, under the 350 cap.
- Section 7's kill criteria omit the project's own "stop and go to the owner" rule (PROJECT.md:115).

**Visual (the only one, the flowchart in section 1)**
- The drawing matches its text alternative, and it holds no number, rating or trend.
- "Discovery: done" and "Design: done" cite docs/PROJECT.md, which does not say either phase is done. The record that says so is the Design gate ruling (decisions/questions/P-001-design-gate.md), which is not cited.
- There is nothing drawn as unknown, and no unknown value is hidden.

**Citation check:**
- **Section 1, line 5.** plan.md:960 is a list of owner tasks, "open questions 5, 8 and 9 before the freeze, and the canary file". It does not say the owner approves scenarios, sets a budget, or that "the plan then freezes". The sign-off at plan.md:942 says the criteria ruling is "Not yet recorded". Cite :942 and :960 together, and name the scenarios.
- **Section 1, line 7.** plan.md:583 is the Critic's arithmetic check inside the new draft's round 1. It does not say "the plan passed review". The PASS is at plan.md:1-3 and the join-up pass is at :939. "60 pieces a kind" and "recommended A" are not at plan.md:253, which holds the weeks and run totals. That rests on the spec only (S-001.md:331).
- **Section 3, line 23.** e002-not-tested says the replay check was not run and that U2's fallback applies, which means comparing new work done both ways over the same period. The words "cannot be re-run faithfully" are in the spec only (S-001.md:10, :334), and the case does not cite the spec.
- **Section 3, line 24.** plan-stop-2 (the ruling) says to rewrite with separate sessions. It does not say "instruction alone was not enough". heldback-store gives the owner's reasoning for a separate repository, but that is a different sentence. Section 5 line 37 then says secrecy from the card side does rest on instruction, so the two lines sit awkwardly together.
- **Section 4, line 30.** plan.md:932 is the wake route "daily, weekly, weekly". It does not say "You start three sessions a kind and pass short records". That is in the spec only (S-001.md:17). "Checked at first use" is supported at plan.md:957 (:932 does not say it).
- **Section 5, line 36.** plan.md:899 is wake counts ("540 to 1,089 in all") and says no cost per turn is claimed. It does not say "your part grows to hundreds of messages". The owner-action ranges are at plan.md:906 (A 243-487, with the K5-in-the-Orchestrator column), and spec only S-001.md:17 says 180 to 360. Cite :906.
- **Section 6, line 41.** "within your AI plan unless you override it" is not supported as a statement about 732 runs. plan.md:14 gives 732 runs and spend-ceiling gives only the ceiling. PROJECT.md:116 says the plan's remaining allowance cannot be read from a session, and spend-ceiling:10 says work waits for the weekly reset if the limit is hit. No record says 732 runs (about 130 million tokens, spec only S-001.md:16) fit in the plan. Restate it as "the ceiling is your plan; whether 732 runs fit is not known; work waits for the reset if it does not".
- **Section 8, line 52.** The same as section 1 line 5: plan.md:960 does not say "criteria as scenarios, frozen after this ruling".
- **Section 8, line 54.** "Build's and Launch's standard lines, all taken on [docs/PROJECT.md]" is supported at PROJECT.md:60-64 and :72-76. See the Standard lines section for findings on whether those lines are true of the records.
- **Appendix, line 64.** The statement that the timeline "prints no milestone lines for this project" cites P-001-gate-record.md. That record says only "Ruling: A" and "Milestone: M1, M2, M3, M4, M5, M6". The question file (questions/P-001-gate-record.md) is not in my pack. The case's claim is therefore unsupported by the record as I hold it. The form says to copy `v3_checks gates` output exactly, and the block in the case is empty.
- **Appendix, line 76.** plan.md:960 says "the canary file" and the PACKS entries at :961. It does not say "reading lists". The case should cite :961 and say what is proposed.
- **Appendix table, line 68-73.** Rows 1, 2 and 4 cite plan.md as a whole with no line number. Row 6, "The plan review passed", cites :583, which is the arithmetic check, and not the PASS at :1.
- **Other lines that cite properly:** line 35 (plan.md:253), line 37 (plan.md:897), line 42 (plan.md:899), line 14-15, line 18-19 (PROJECT.md section 2, the intent), line 47 (no-change-result).

**Milestones:**
- The block is empty, so the case lists no project milestone at all. M1 to M6 are not listed with their status. M1, the count, is a Discovery milestone and M2, the fair test, is a Design milestone. M3 to M6 are Build milestones, which the owner is about to rule on at this gate. The gate-record ruling lists M1 to M6, but the case does not say what it ruled.
- I cannot judge "reached", "sprint pending" or "dropped" for any project milestone from this case. I cannot confirm that the empty block is what `v3_checks gates` printed.
- The table lists only the six Design standard milestones. Rows saying "Not recorded by the model" (Design-3, Design-5) are not findings and neither is claimed reached, which is correct. Design-1, 2, 4 and 6 are claimed as met by a "reviewed" plan, with no line cited for Design-1, 2 and 4, and Design-6 cites the wrong line (above).
- Every name in the table reads as an achievement, not a task. None of the project milestone names M2 to M6 appears in the case, so I cannot check their wording here.
- Section 8 and the appendix say Build's and Launch's standard lines are "all taken on". That is a statement about PROJECT.md lines that I check below.

## Standard lines

Lines: FAIL

1. **Build-1** (PROJECT.md:60) says the held-back checks are written "by a Check author who never sees the work". The plan review (plan.md:22) and the spec say the Check author never sees the change texts. It writes the sheets for the pieces. "The work" is the wrong object, and a reader would take it to mean the Check author never sees the piece. Reword it to say the Check author never sees the changes.
2. **Build-3** (PROJECT.md:62) says the harness and the record "touch how every project's agents are started and judged". The spec and PROJECT.md:88 say the harness runs only as copies inside Model-Lab (experiments/**, nothing live changes). Only the brief-and-model record (M3) lands in the operating model's own tools (PROJECT.md:90). The reason is true of the record but not of the harness. Reword it to say only the record touches every project, or drop the harness from the clause.
3. **Build-2** and **Build-5**: the reasons are true of the records (PROJECT.md:65, :86, :89). "Harness" is jargon for the owner. I would say "the test's scripts" instead, but it is not a failure.
4. **Build-4** is plain and true of the records (M4, PROJECT.md:66).
5. **Launch-1 to Launch-4** are true of the records (PROJECT.md:68, :90, :93; V2 at :109). Launch-4 is project-specific and good.
6. **Launch-5** gives "the owner passes the Launch gate" as the reason. Every project has that gate, so it does not say why this project needs the milestone. The lessons-for-the-operating-model half (lessons log, PROJECT.md:13, :92) is the real reason. Reword it to lead with that.
7. All ten lines have a why, none has " · " inside the reason, and all ten are present with the correct form `- <Phase>-<n> (standard) · taken on · why: <reason>`. The failures are accuracy and plainness only: findings 1, 2 and 6.

## The six-part contract

1. **What I changed:** nothing. I am read-only and wrote no file.
2. **Why:** the brief asked for the Critic section of the Build gate case for P-001 and a check of PROJECT.md section 3 lines Build-1 to Build-5 and Launch-1 to Launch-5.
3. **What I verified:**
   - the case line by line against plan.md lines 1-3, 14, 22, 240-264, 570-594, 897-965;
   - decisions/questions/P-001-gate-record, spend-ceiling, heldback-store, e002-not-tested and plan-stop-2;
   - PROJECT.md in full;
   - the spec's header, plain words, open questions 1-9 and its stop rule (S-001.md:1-19, 326-355);
   - a word-count estimate of sections 1-8 (about 320).
4. **What is undone:**
   - I did not read the Chief of Staff's notes, docs/briefs/** or docs/reports/**, as the brief said.
   - I did not read experiments/E-003.md, the whole spec or all 960 lines of the plan review.
   - I did not see questions/P-001-gate-record.md, which is not in my pack. I did not see OPERATING_MODEL §4's table of standard milestones, so I judged the standard lines against PROJECT.md and the records, not against the table's wording.
   - I could not run `v3_checks gates`, so I cannot say what the milestone block should print.
   - I did not verify the 50,540-byte pack size or whether the sheets repository exists.
5. **Needed outside my lane:**
   - The Chief of Staff, for the case: show the scenarios, show the budget options with the 300-run figure beside 732, list the open questions, carry the plan review's non-blocking items and the power limit as risks, fix the citations above, and have the milestone block printed by `v3_checks gates`.
   - The Chief of Staff, for the standard lines: reword Build-1, Build-3 and Launch-5, then have a Critic check the reworded lines before commit (PROJECT.md:35).
   - The Chief of Staff, for the PACKS.toml entries: confirm they are merged and approved before this gate, as the spec says.
   - The owner: open questions 1-9 in the spec, the sheets repository, and the budget.
6. **Open questions:**
   - Does the question file for the gate-record ruling say that an empty milestone block is the intended form for this project? If so the case should cite it with a line.
   - Is the owner meant to see the nine open questions in the case itself, or on a card beside it?

Files: /home/user/Model-Lab/docs/gates/P-001/build-gate-1-case.md, /home/user/Model-Lab/docs/PROJECT.md, /home/user/Model-Lab/reviews/S-001/plan.md, /home/user/Model-Lab/specs/S-001.md, /home/user/Model-Lab/decisions/questions/P-001-gate-record.md, /home/user/Model-Lab/decisions/questions/P-001-spend-ceiling.md, /home/user/Model-Lab/decisions/questions/P-001-heldback-store.md, /home/user/Model-Lab/decisions/questions/P-001-e002-not-tested.md, /home/user/Model-Lab/decisions/questions/P-001-plan-stop-2.md
