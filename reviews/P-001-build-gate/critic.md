Verdict: FAIL

The Critic's check of questions/P-001-build-gate.md and questions/P-001-build-gate-terms.md (brief: docs/briefs/47-critic.md), on claude-sonnet-5-5, a different model from the questions' writer, verbatim. Recorded by the orchestrator. Session session_01QBwHGMBo8kZsMCS2EvKNwd, 2026-11-04.

## Round 1
Both cards need changes before they go to the owner. I read the gate card, the terms card, specs/S-001.md (all except lines 195-324, which I did not read), the question template, AGENTS.md §5 and "Plain English first", and the owner's rulings in decisions/questions/. I did not open E-003, so I could not check term 6's false-pass tolerance against it. I did not re-derive the sizing figures. The ones I compared match the plan: runs, tokens and weeks for options A to D, 266 against 732 giving "about a third", the 9 and 336 sessions, and the 32 to 64 against 60 to 121 weeks.

**Findings, gate card (questions/P-001-build-gate.md)**

1. BLOCKING. The opening does not lead with what failed or was skipped (AGENTS.md "Plain English first").
   - It starts "Design is done ... passed".
   - It omits that the check of the judges was never run (decisions/questions/P-001-e002-not-tested.md; spec "In plain words").
   - It omits that the replay check failed for every kind, which is why the test uses new work.
   - So the owner is not told the judges' accuracy is unknown, and a judge wrong 1 time in 10 cuts the chance of seeing a real 20-point gain to about 1 in 2 or less.

2. BLOCKING. The recommendation states "sees a 20-point gain about 4 times in 5 for every kind" as plain fact.
   - The plan gives 0.8 only under the library's middle assumption. Built work and research fall to about 0.51 and 0.54 if the two versions disagree as often as chance allows, and everything halves with a noisy judge (spec "Size"; sizing table).
   - The card also omits the plan's "Smaller gains" warning: for the changes tested on built work and research, "not shown" is the usual result even if they help by as much as their cause allows. The owner should know this before spending 132 million tokens.
   - The recommendation leans beyond the records without these.

3. BLOCKING. The budget is put as 132 million tokens, with no mention that the wakes are outside it.
   - The plan says about 540 to 1,089 session wakes and 60 to 121 landing reviews are "not estimated", outside the runs and tokens, and outside the budget (spec "The budget excludes the wakes").
   - The owner's own part is also unstated in the options: 9 sessions to start and 24 to 27 blocks to pass, up to 183 to 366 session starts if K5 fails. The Context line only says the part "grows".

4. Non-blocking. Option A's cost line ("before anything shows whether the sessions wake and keep the secrets") sits oddly with the recommendation. The recommendation says built work goes first and tries the untested running, stopping if its first checks fail.
   - Option B's gain ("untested parts tried on the fastest kind first") is also true of A, so the options are not fairly separated.
   - "Each kind stops if those first checks fail" is too strong. K1, K3, K4 and K5 failures go to the owner as a question: go on with a stated limit, or stop (spec K1, K4, K5).

5. Non-blocking. Option C gives no tokens, weeks or power for 40 pieces a kind (88 million, 40 to 81 weeks) or for the 100-piece plan (188 million, 87 to 173 weeks), so the owner can't weigh it. It also drops the plan option D's "60 for plans".

6. Non-blocking. The risk class is R2 and the reversibility is "irreversible" (because of option F), with no default and no timeout. That fits AGENTS.md §5, since irreversible questions never default, and the card explains why. The template wants a letter and hours, so say "none (irreversible)". The milestone line (Design-6) is fine.

7. Checked and true: the Design-6 milestone line; the ruling "every kind, incrementally"; option B saying it goes against that ruling (it does, LL-08); the figures for A and B; the plan review at round 3 and the join-up review.

**Findings, terms card (questions/P-001-build-gate-terms.md)**

8. BLOCKING. The card says "eight terms", but the plan's nine open questions are not all carried over.
   - Plan question 5 also asks the owner to approve, as a rule change, the PACKS.toml entries for the per-task packs `S-001-holdout` and `S-001-analysis`. Without the first, "AC4 cannot be met and the test does not start". Term 4 carries only the recording half. The "eight" count is never reconciled with the nine, although the Context line says nine.
   - Plan question 3 also asks whether research should be tested at all, or left until the built-work and plan results are in, given what the test can show for C3. Term 3 carries only the time limit.
   - Plan question 8 also asks the owner to accept the owner's part and the K3, K5 and K7 fallbacks. Term 7 gives only the session counts.

9. BLOCKING. Term 7 option A does not say it departs from the owner's own wording.
   - The owner ruled "each judging in their own sessions" (decisions/questions/P-001-plan-stop-2.md:10).
   - The plan itself says that A is a reading of this and that "the plainer reading may be one session per judging".
   - The card hides this in the "what would change it" line. Option A, which is recommended, should say it reads the ruling as one session per kind (LL-08).
   - Likewise term 2 option C (all three at once) goes against "no single kind first, incrementally" and the "one kind after another" order. It is not flagged, and option A is not placed against the ruling either.

10. Non-blocking. Several options have a gain but no cost.
    - Term 5 option B gives no cost for the outside judge, though it spends past the ceiling.
    - Term 6 never says in plain words what a "false pass" is, and option B ("a stricter one you name") gives no gain or cost.
    - Term 1 option B is fairly put, since the plan's replay result rules out the wording.

11. Non-blocking. Terms 1 and 4 use M2 and M3 as bare ids. The opening is plain.
    - The risk class is R0 (questions/**) yet the reversibility reads "irreversible". AGENTS.md §5 says reversibility is computed from the class, so the card should say the irreversibility comes from option 8B and not from the file path.
    - Setting the owner's value-target wording is arguably above R0, so the Chief of Staff should confirm the class.

12. Checked and true: 2A's 32 to 64 against 60 to 121 weeks; 3A's review points at 16 weeks and at each token checkpoint; 7's 9 against about 336 sessions; 8's "Service Desk and Model-Lab today"; and 8B's "for good". I found no option that states what a system will do without a cited record (LL-46, LL-50), apart from the "stops" wording in finding 4.

**Six-part contract**
- Changed: nothing. I hold no write tool.
- Why: to check the two Build-gate cards cold against the plan and the owner's rulings.
- Verified: by reading the files named above. I ran no commands. I compared the figures by eye with the plan's tables and did not re-run sizing.py.
- Undone: the sizing figures were not re-derived; the E-003 text and the Chief of Staff's notes were not read; the spec's lines 195-324 were not read.
- Needed outside my lane: the Chief of Staff must fix findings 1, 2, 3, 8 and 9 and re-submit for a second Critic round. Findings 4, 5, 6, 10 and 11 should be fixed in the same pass.
- Open questions: should the PACKS.toml pack approval and the "test research at all?" question go on the terms card, or on a third card? That is the Chief of Staff's call. If the answer is a third card, the "eight terms" wording must still say which of the plan's nine each card carries.

## Round 2 (commit b9540eb; brief 52, a fresh session)

Verdict: FAIL

Round 2 check of questions/P-001-build-gate.md (the gate card) and questions/P-001-build-gate-terms.md (the terms card), read from /home/user/ml-gate at b9540eb. I am on claude-sonnet-5-5, a different model from the cards' writer.

Round 1's blocking findings 1, 2, 3, 8 and 9 are resolved in substance. The redrafts add errors, listed below. Seven of the findings are blocking: G1 and G2 on the gate card, T1 to T4 on the terms card, and G3, which is the case's fault.

**Round 1 findings**
- Resolved: 1 (the opening leads with the skipped checks), 2 (power is conditional and the smaller-gains warning is in), 4, 6 and 9. The terms card now flags 2A, 2C and 9A against your rulings.
- Finding 3 is resolved except that the owner's worst range is wrong (see G2).
- Finding 5 is partly resolved: tokens and weeks are now given for option C, but not power, gain or cost (see G1).
- Finding 8 is mostly resolved: the packs, "test research at all" and the owner's part are now carried. Two gaps remain (T2 and T4).
- Finding 10 is partly resolved. Terms 6B and 7B now have gain and cost. 10A, 10B and 11 are thin (see N6).
- Finding 11 is resolved on ids and on the basis for "irreversible". The class question is open (see N9).

**Blocking findings**

*Gate card*

G1. BLOCKING, gate card. Option C is not fairly put.
- It is a live ask ("Say which") with no gain, cost, what it rules out, power or owner's part.
- The plan's figures are in S-001: 40 pairs a kind gives 0.57 under the middle assumption, or 0.30 if the judge errs one time in ten. 100 pairs gives 0.96, or 0.71 with judge error.
- The owner's part is 9 sessions and 17 to 19 records for 40 pieces, and 9 sessions and 32 to 37 records for the 100-piece plan.
- Without these, the owner cannot weigh C against A, and A's recommendation ("the smallest size that gives about 4 in 5") is the only guide to C.

G2. BLOCKING, gate card. Option A says "up to about 183 to 366 session starts", and the plan's worst case is higher.
- The plan's table gives 183 to 366 if K5 fails. It gives 243 to 487 for A if K5 also fails in the Orchestrator's own session ("The owner's actions per option", specs/S-001.md:135).
- "Up to" is therefore false of the record. The case (section 5) gives 243 to 487 but labels it "if sessions cannot wake themselves". That is the wrong cause: it is resume failure, whereas a wake failure (K7) costs 60 to 121 wake messages, or 180 to 363.
- The card and the case disagree, and neither card gives the K7 range.
- Option B has the same gap: the plan has 163 to 327 for B (its option C: 29 to 61).

G3. BLOCKING for the case, which is not under my review, but the owner will read it beside the card. Its budget lettering clashes with the card's.
- The case (section 4) says "B 490; C 266, built work only; D 1,040", using the plan's letters.
- The card's letters are B = built work only, C = 40 or 100 pieces, D = hold.
- An owner who answers "C" from the case's words would be ruling something else.
- Fix one side. The card does say "the plan's option C" for its B, but the case does not say "plan's".

*Terms card*

T1. BLOCKING, term 1. The reworded value target is shown in quotation marks but is not the plan's wording.
- The plan proposes two different texts. V1 is the longer one (S-001 open question 1: "…each new piece done or checked both with and without the change…", plus the 1-in-40 clause and the 20-point clause). M2's "done when" is another text altogether (open question 2).
- The card quotes one fragment, drops "new", and says "reword both to" it.
- You alone may change the value target, so the card should show the exact V1 and M2 wording it asks you to approve, or say that it is a summary.

T2. BLOCKING, term 9B. "Gain: each judge fully apart" is untrue of the plan.
- S-001 open question 8 says "Little isolation is gained, since every session can read public Model-Lab", and that each judge would hold a clone of the whole sheets repository, with the other kinds' sheets and verdicts. Isolation there depends on the transcript check, as it does now.
- The cost line also omits that AC5 and J5 must change before the freeze.
- B's pitch is therefore overstated (LL-05).

T3. BLOCKING, term 10. It asks you to accept fallbacks without telling you what they are.
- Plan question 8 asks you to accept "the fallbacks K3, K5 and K7 name". The term says only "the plan's fallbacks bring it to you, and your part can grow to the ranges the gate card gives".
- The gate card covers K5 only, and wrongly (G2). It omits K7 (you send wake messages) and K3 (if the judging session cannot read Model-Lab, your only choices are to stop the test or order a revised spec, which changes K2 and AC5).
- K3 is the one fallback that can end the test, and it is not said anywhere.
- "Bring it to you" is also wrong for K7 in the work session, where the Orchestrator tries first.

T4. BLOCKING, term 5. It leaves out a part of plan question 5, so the claim "carry every part of the nine except budget and size" is false.
- The plan also says research started in a conversation needs the same record for its source check, not only for the researcher.
- 5B ("only research can enter") is true only of the Service Desk's scripted research.

**Non-blocking findings**

N1. Gate card, opening. "Nothing here is irreversible except closing the project" understates two things.
- Runs and tokens already spent are not recovered.
- A frozen spec is not changed (a revision is a new spec through plan review).
- Say so, or soften the line.
- The "roughly halves" is right for the middle assumption (0.80 to 0.45). Under the independent arms it is 0.51 to 0.34.

N2. Gate card, option A. Its order (built work, then plans, then research) is not set against "no single kind first".
- The owner's words in P-001-worst-work.md were "I don't care to start… incrementally". They support an order, so this is probably fine, but A should say that it reads the ruling this way.
- Only B is flagged.

N3. Gate card. The weeks it gives for A, B and C assume plans and built work are recorded at dispatch (terms 5A) and the Service Desk's pace.
- The card does not say that 5B or 11B changes the answer.
- It also omits what the case's section 6 says: whether 132 million tokens fit your AI plan is not known, and work waits for the reset (P-001-spend-ceiling.md).

N4. Gate card, "WHO HAS CHECKED IT". It lists "its check of this card" before that check has a result. After PASS it should cite the record and round, as P-001-gate-citation.md does.

N5. Risk classes differ without explanation. The gate card says R2, the terms card says R0, and the path rule puts questions/** at R0 (governance/risk-paths.toml:23).
- The gate card should give the basis for R2.
- The terms card should confirm the class for term 1, since it changes the value target's wording.

N6. Terms card, thin options and unsupported claims.
- 10A and 10B have no gain or cost, and 10B ("the plan would then be revised before it freezes") is not in a record.
- 2C's "Gain: the shortest wait" is unsupported. The plan gives one "together" figure, 32 to 64, which is the same figure the card gives 2A.
- Term 2A's gain and the gate card's "side by side" describe slightly different things.
- Term 6 does not carry the Reviewer's non-blocking note that the analysis pack's comment is thin (reviews/44/reviewer.md, finding 5). The case does.

N7. Terms card, term 9. The quotation "the sheet writer and each judging in their own sessions" is spliced.
- The ruling's own headline reads "the sheet writer and the judges in their own sessions". "Each judging" is the carry-out line, written by the Chief of Staff (decisions/questions/P-001-plan-stop-2.md:1 and :10).
- Your words were "A: rewrite, full review (Recommended)". Attribute the phrase to the ruling's record, not to you (LL-05).

N8. Terms card, term 11. The option does not mention that your Model-Lab ruling already allowed records from private repositories, including the replay transcripts, in public Model-Lab (P-001-model-lab-public.md). The ruling appears only in Context. Say whether 11B goes against it, or sits within it, in the option itself. It could also say the operating-model repository has had no commit since 24 October.

N9. Plain English. Both openings are plain. "Plan's option C", "the plan's options B and D" and "plan question n" use the plan's lettering, which you may not have read. Giving the plan's names or sizes instead would be clearer.

**Checked and true**
- Gate card: the Design-6 milestone line, and the figures for A (732 runs, 132 million tokens, 60 to 121 / 32 to 64 weeks, 9 sessions, 24 to 27 records, 540 to 1,090 wakes, 60 to 121 reviews). Also the figures for its B (266, 48 million, 7 to 15, 3 sessions, 8 records, 22 to 46), for C (490 / 88 million / 40 to 81; 1,040 / 188 million / 87 to 173) and the ruling quotes. The power statements (0.80, about 0.51 and 0.54, 11 to 19 points) and "the budget counts runs only" also hold.
- Terms card: 3A's 16-week review points, and 4's "200 runs, 32 to 64 weeks, 11 to 16 points". Also 7B's cost (spend beyond the plan, not estimated), 8 against E-003 (the false-pass guard is "no more than the unchanged check's plus one"), and 9's "9 against about 336".
- Terms card: mapping of the plan's nine questions. Q1 and Q2 are in term 1, Q3 in terms 3 and 4, Q4 in 2, Q5 in 5 and 6, Q6 in 7, Q7 in 8, Q8 in 9 and 10, and Q9 in 11.
- The sorted-out reversibility reasons, and DEFAULT/TIMEOUT "none" on both cards, are right for irreversible questions.
- I found no option stating what a system will do without a record (LL-46, LL-50), apart from the items above. The first-use "stop to the owner" wording is now accurate.

**Six-part contract**
- Changed: nothing. I hold no write tool.
- Why: round 2 cold check of the two Build-gate cards against S-001, the owner's rulings, the case and the template.
- Verified: by reading the files named above, in /home/user/ml-gate. They are S-001 lines 1 to 373 in full, both cards, the round 1 critic record, the case, the template, reviews/44/reviewer.md, the rulings (worst-work, plan-stop-2, heldback-store, model-lab-public, test-budget, e002-not-tested, spend-ceiling), E-003's false-pass lines, risk-paths.toml's class lines, AGENTS.md §5, the lessons LL-05, 08, 46 and 50, and P-001-gate-citation.md.
- Undone: the sizing figures were not re-derived. I did not open the proposal file, the full text of E-003, the PROJECT.md sections on V1 and M2 (so I could not compare the "same past tasks" wording), plan.md beyond the lines cited, or the question files' original wording for the plan-stop-2 option text.
- Needed outside my lane: the Chief of Staff must fix G1 to G3 and T1 to T4, and should fix N1 to N9. It must then re-submit for round 3, the last round allowed.
- Open questions: should the case's lettering follow the card, or the card's the plan's? That is the Chief of Staff's call, but they must match. Does the owner intend "up to" on the owner's part to cover the 243 to 487 worst case, or only the K5-alone range?
