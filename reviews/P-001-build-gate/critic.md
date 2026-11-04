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

## Round 3 (commit ea0aaac; brief 54, a fresh session; the last round allowed)

Verdict: FAIL

Round 3 check of questions/P-001-build-gate.md (the gate card) and questions/P-001-build-gate-terms.md (the terms card). I read both from /home/user/ml-gate at ea0aaac, and I am on claude-sonnet-5-5, a different model from the cards' writer. Round 2's findings G1 to G3, T1 to T4 and most of N1 to N9 are resolved. Two new errors keep the verdict at FAIL: finding 1 on the gate card and finding 2 on both cards. Each is a one-line fix.

**Round 2 findings, resolved**
- G1: option C now has gain, cost, chance and the owner's part for both sizes. The figures are right for C1 (0.57 / 0.30, 17 to 19 records, 40 to 81 wake messages, 123 to 246 session starts). C2 has an error (finding 1).
- G2: the 243 to 487 worst case, the K7 ranges (60 to 121, 180 to 363) and the ranges for B and C all match "The owner's actions per option".
- G3: the case now uses the card's letters (A, B, C1, C2) and its figures.
- T1: the quoted V1 and M2 texts are word for word the plan's open questions 1 and 2.
- T2: 9B no longer overstates the gain; it says little isolation is gained and that AC5 and J5 change.
- T3: term 10 now lists the K7, K5 and K3 fallbacks, including the K3 choice of stopping the test or ordering a new plan through review.
- T4: the conversation-started research source-check record is in term 5.
- N1, N2, N3, N5, N7 and N8 are fixed. N6 is fixed apart from one open item (see the note after finding 4).
- All nine of the plan's questions map to terms 1 to 11, and nothing is left out.
- The opening of each card is plain, with no ids or paths.
- Checked true:
  - The gate card's figures match the plan for A, B, C1 and C2: runs, tokens, weeks, sessions, records, wake messages and session starts.
  - 9B's 336 sessions, 7B's cost, the 16-week review points, and the quoted lines 1 and 10 of the plan-stop-2 ruling all match.
  - The Reviewer's note on the thin analysis comment (reviews/44/reviewer.md, finding 5) is carried correctly.
  - The model-lab-public and spend-ceiling rulings are used correctly in 11 and 7.
  - Options that go against a ruling are flagged: gate B; terms 2A, 2C and 9A, and 11B as going beyond the ruling.

**Findings**

1. Gate card, option C2 (BLOCKING). "Chance: about 24 in 25, or about 7 in 10 with judge error" is stated for the whole option. The option is 100 pieces for research and built work and 60 for plans.
   - Those figures are the plan's for 100 pieces (0.96 / 0.71).
   - Plans stay at 60 pieces, which is 0.80 / 0.45 (the plan's 60-piece rows).
   - So the figure is false for plans.
   - Fix: say "for research and built work; plans stay at about 4 in 5, or 9 in 20 with judge error".

2. Both cards, "comes to you first" (BLOCKING, LL-46 and LL-50: a claim about what a system will do that no record holds).
   - Terms 10A's gain says "every failure that would change your part comes to you first". The gate card's recommendation says "a failed first check there comes to you before more is spent".
   - Only K1, K3, K4 and K5 at its first check are put to the owner as a question.
   - K7 has no question. The Orchestrator tries first, then the owner just sends wake messages. The owner is not offered a go-on-or-stop choice, and the card says so itself in term 10.
   - K5 in the Orchestrator's own session after the first check is also no question; it is just one more session a week.
   - Fix: name the checks that do come as a question (K1, K3, K4, K5 at its first check), and say the wake-message duty simply falls to the owner.

3. Gate card, options B, C1 and C2 (not blocking). A says built work and research fall to about 1 in 2 if the two versions disagree as often as chance allows. B, C1 and C2 omit this, although B is built work only. Under that assumption B is 0.51 and C1 is 0.34 for built work, 0.37 for research and 0.62 for plans. The line defining "Chance" implies the middle assumption only, so the figures are true. But B's "about 4 in 5" reads better than the record supports. Add the caveat to B at least.

4. Terms card, term 2 and the gate card's "side by side" (not blocking).
   - 32 to 64 weeks is the longest single kind (research), so it holds only if all three kinds collect from the start. That is 2C, "all at once".
   - The plan (line 90, and open question 4) ties it to 2A, the next kind starting while the previous is judged, and the card repeats the plan.
   - Collecting one kind after another gives about the sum, 60 to 121. The card is true of its cited record, but a smart owner could pick 2A expecting 32 to 64.
   - Say "up to 32 to 64, only if the kinds overlap fully", or flag it back to the plan.

Note on N6 (the one open item): 4B ("leave research until the built-work and plan results are in; research may never be tested") is not marked as going against "every kind" or "everything should be touched". It also does not say how it fits with gate options A and C, which include research.

5. Gate card (not blocking). The plan's "one likely limit" (K1: the secret check kept from the cards' writer by instruction alone, because the Chief of Staff's session holds a tool that reads other sessions' transcripts) is in the case (section 5) and the plan's "In plain words", but in neither card. The gate card says "Your part assumes every first check passes". Add a line pointing to case section 5.

6. Gate card, opening (not blocking). It says the check of "how accurate the judges are" was skipped. The ruling and the plan call it the judging-consistency check, and the sizing's "wrong one time in ten" is a noise model. Use "how consistent and reliable".
   - Also, "a little over half of what it would be otherwise" is right for the middle assumption (0.80 to 0.45). It is about two-thirds under independent arms (0.51 to 0.34).

7. Terms card, term 10 (not blocking). It lists the K7 fallbacks for the work and judging sessions but not the one for the Orchestrator's session: the owner asks for the weekly landing. The plan's ranges do not count it either. Say so, or carry it back to the plan.

8. Both cards (not blocking). N4 and N9 are only partly fixed.
   - "WHO HAS CHECKED IT" on both cards names the Critic's check of the card but not the round or result. Cite "round 3, PASS" once the Orchestrator records that.
   - "Plan question n" in terms 1, 2, 3, 5 to 11 still uses the plan's lettering; give the question's name instead.

9. Both cards (not blocking). R0 is now given with its basis. The cards state "irreversible" and give the reason (option F, term 11B), though the template says reversibility is computed from the class. DEFAULT and TIMEOUT "none" are right for irreversible questions.

Case and cards agree on letters, sizes, the 24 to 27 records, 183 to 366 and 243 to 487 session starts, and the 4 in 5 and 1 in 2 chances.

**Six-part contract**
- Changed: nothing; I hold no write tool.
- Why: round 3 cold read of the two Build-gate cards as a non-expert owner, against round 2's findings and the cited records.
- Verified, by reading in /home/user/ml-gate:
  - Both cards, and reviews/P-001-build-gate/critic.md (rounds 1 and 2).
  - specs/S-001.md in full (lines 1 to 373).
  - docs/gates/P-001/build-gate-3-case.md, and the proposal for V1.
  - reviews/44/reviewer.md, questions/_TEMPLATE.md, AGENTS.md §5, and the rulings on e002-not-tested, plan-stop-2, worst-work, model-lab-public and spend-ceiling.
  - The risk-paths class lines.
  - The gate-citation ruling exists at /home/user/ml-ask/decisions/questions/P-001-gate-citation.md; I did not open it.
- Undone:
  - I did not re-derive the sizing.
  - I did not open E-003's false-pass text this round (round 2 did).
  - I did not open reviews/S-001/plan.md, so I did not re-check the cards' cited lines in it.
  - I did not read the Chief of Staff's notes or the full proposal text.
- Needed outside my lane: the Chief of Staff must fix findings 1 and 2, which are blocking. It should fix 3 to 9 in the same pass. The Orchestrator should treat the rounds as exhausted (round 3 was the last allowed), so the cards go to the owner only after the fix, or the owner is told they failed their last check (D-044).
- Open questions: should finding 4's figure go back to the plan, since the plan itself ties 32 to 64 weeks to 2A? Who owns the Orchestrator-session K7 ask in finding 7?

## The cut-down cards, round 1 (commit ddc3429; brief 63, a fresh session; new cards under the owner's ruling, decisions/questions/P-001-build-gate-stop.md)

Verdict: FAIL

Both cards follow the ruling's shape: they are short, they point to the plan's tables, and the terms card argues seven terms and lists four. Each card has one blocking problem. These are new cards, round 1. Neither card is yet fit for the owner, because the gate card hides the cost of the recommended spend and the terms card leaves out parts of the plan's open questions.

Findings

1. Gate card, BLOCKING. Option A states no cost. It says "Cost: the runs you set", and the card gives no run, token or week figure for the size it recommends.
   - The ruling allows pointing to the plan's tables instead of copying them. It does not allow leaving the owner with no headline number.
   - OPERATING_MODEL §2 requires gain and cost per option.
   - The card says "In plain words" holds "the chance, the weeks, the runs, what you would do". It omits two things that section holds and that earlier rounds found decisive: "Smaller gains" and "The budget excludes the wakes".
   - "Smaller gains": two of the three changes can reach at most about 11 to 19 points, so "not shown" is the usual result even if they help (spec "What the test can and cannot show").
   - "The budget excludes the wakes": the budget the owner sets counts runs only. The plan puts about 540 to 1,089 wakes and 60 to 121 landing reviews outside it, not estimated (spec "The budget excludes the wakes").
   - The recommendation rests on "about 4 in 5 for every kind under the library's assumption". It is qualified, so it is not false. But built work, the first kind, is also the one whose change is expected to read "not shown", and that is not said anywhere. This is LL-05 leaning, which round 1 of the old cards already found.
   - Fix: add one line for A giving 732 runs, about 132 million tokens, and 60 to 121 weeks one after another (32 to 64 if the kinds collect together). Say the wakes are outside it, and that "not shown" is likely for built work and research.

2. Terms card, BLOCKING. The ruling's test is that nothing is left out, and some parts of the plan's open questions are missing.
   - Question 5 (recording at dispatch) has two gaps.
     - It asks which projects take part. Term 9 does not carry this; term 7 only covers the public/private cut.
     - It says Model-Lab's brief records lack the start-commit field, so the field must be added (spec open question 5; "Needed outside", last bullet). Term 9 omits this.
   - Question 3 asks about research "given what the test can show for C3 (and C2)". The plan says the owner "may prefer to test C1 and C2 only". Term 3 carries only research and C3, and drops C2 and that alternative.
   - Fix: add these to terms 3, 7 and 9.

3. Terms card, term 4, non-blocking but must be corrected. The rules of the operating model say a rule change is approved by the owner's own GitHub action, or a recorded proxy action (OPERATING_MODEL §2 "Approvals").
   - "Approve them by your verdict and merge on the pull request" blurs this. Say plainly that the approval is the owner's own action on that pull request.
   - The plan says the entries are "merged before the Build gate". The card does not say whether that has happened.
   - Neither card names the pull request (#44). That branch is the one the cards sit on, so a reader cannot tell whether merging it also lands the gate documents. I could not check this, so I raise it as an open question.
   - "Passed with one minor note" is true of reviews/44/reviewer.md finding 5. That review was of commit 09dfa20, and the reviewer did not re-run the suite on the later head. It also recorded one red check in the local suite, the expected LL-29 case. Say this.

4. Gate card, non-blocking. Option A's gain, "the test starts", overstates.
   - Plans and built work cannot enter until recording at dispatch exists (spec "Recording is a precondition"). That is term 9.
   - The recommendation reason "built work, which comes first … the fastest kind" holds only once term 9 is ordered. Say so (LL-46, LL-50).
   - Also point to the plan's first-use checks, such as K1, as the condition on the secret check.

5. Gate card, non-blocking. Its letters clash with the plan's.
   - The card's options A to D include the plan's sizes A to D.
   - "C" could mean Recycle or size C, and an answer to a gate must be unambiguous. Name the sizes "size A", "size B" and so on everywhere, including the answer line.
   - The opening is also well over the "≤ 5 lines" background of §2.
   - The card does not link the case or the Critic's view, which §2 requires at a phase gate.

6. Gate card, non-blocking.
   - Option D (kill) says "the lessons log still goes to the operating model". PROJECT.md records that the brief-and-model record goes in on a V1 miss (line 112), and M6 corrects the lessons log at the end of a cycle. No record says what happens on a kill at this gate. Cite one or drop the clause.
   - Context bullet 2 says "by the owner's ruling" for both facts. Only the judge-consistency skip is the owner's (P-001-e002-not-tested). The failed replay is E-001's result (reviews/E-001/reviewer.md). Split them (LL-05).
   - Option C (size C) is said to go against the ruling "no single kind first". The plan does not say this of its own option C; it is the Chief of Staff's reading. The owner's words were "I don't care to start… work it incrementally because everything should be touched". Say "reads as going against".
   - The same applies to term 2B and 2C "goes beyond your ruling", where the plan does say it, so attribute it to the plan.
   - The "likely limit" (K1) is worded "may be" on the card. The plan says "likely", with its reason: the Chief of Staff's session holds a tool that reads other sessions' transcripts.

7. Terms card, non-blocking.
   - Context bullet 2 says the owner "ruled the value target with the words 'the same past tasks'". The ruling is the owner's choice of option A, "+20 pts". The words are in the question as put and in PROJECT.md V1, not in the owner's own words (LL-05).
   - Term 1 should say plainly that A rewrites text the owner approved.
   - Term 7A's cost, "the operating model's own work is not tested", omits that the repository has had no commit since 24 October (spec); the loss today is small.
   - Term 5B says "override your ceiling", but the ruling asks for an override "at the time" of spending. Say that the answer must be given at the time.
   - Term 11 gives no figure for the owner's part, though the plan's ranges are large: for size A, up to 240 to 484 wake messages, or 243 to 487 new sessions. It also omits the 8 to 12 cards per kind that the owner answers. State the worst case in one line.
   - Term 2A gives "60 to 121 weeks" without the pace it assumes, the Service Desk's pace, or the recording precondition.
   - Term 2B's "up to three times as large" is a derivation, not in the record. Mark it as the writer's arithmetic.
   - Terms 9 (a new standing duty for the Chief of Staff) and 8 arguably touch the rules and the earlier no-fixed-length ruling (P-001-time-and-limit). They are only listed. Confirm that is acceptable under the ruling.
   - Terms 8 to 11 use K3, K5 and K7 in the options, which a non-expert cannot read.

8. Both cards, non-blocking. "WHO HAS CHECKED IT" lists "its check of this card" before this check has a result. After a PASS, cite the round and the record, as P-001-gate-citation does.

9. Both cards, non-blocking. The risk class R0 (questions/** is R0 in risk-paths.toml), reversibility "irreversible" with its reason given, default none and timeout none are right. AGENTS.md §5 says irreversible questions never default, and the template's computed reversibility is overridden with the reason stated. The milestone line Design-6 is accepted as before.

Checked and true
- Gate card, opening: it leads with the skipped checks. The claim "wrong 1 in 10 lowers it to about 1 in 2 or less" matches the plan.
- Gate card, Context: the plan passed at round 3, with the join-up review having no blocking difference, and rounds 4 and 5 passed.
- Gate card, recommendation: 60 pairs is the smallest size giving 0.80 under the middle assumption for every kind; 40 pairs gives 0.57.
- Gate card, Context: the 100-run allowance covered only Discovery and Design, and the ruling "no single kind first; every kind, incrementally" is cited correctly.
- Terms card, term 1: it is true that the plan gives the two texts word for word.
- Terms card, term 2: 60 to 121 versus 32 to 64 weeks match.
- Terms card, term 3: the 11 to 16 points, 200 runs and "not shown is likely" match.
- Terms card, term 5: the judges are Fable 5.1 and share the work's provider (spec "What this cannot rule out"). Option B's cost is "not estimated" in the plan.
- Terms card, term 6: both quotes match lines 1 and 10 of the plan-stop-2 record. Line 10 is the Chief of Staff's carry-out text. The counts of 9 and about 336 match. The card says the A reading "may not be what you meant". The two changes (one criterion and one join line) are AC5 and J5.
- Terms card, term 7: the "beyond a record" reading matches P-001-model-lab-public.
- Terms card, term 10: the plus-one false-pass rule matches E-003 "Kept".
- Terms card, term 11: the K3 fallback (stop, or order a revision) is accurate.
- Terms card, opening: seven terms plus four makes eleven, which maps onto the nine questions apart from the gaps in finding 2.
- Neither opening has ids or paths. No option states what a system will do without a record, apart from findings 4 and 6.

Six-part contract
- Changed: nothing. I hold no write tool.
- Why: to check the two redrafted Build-gate cards cold against the owner's ruling (B) and the records they cite.
- Verified:
  - I read both cards, the ruling, and S-001 (lines 1 to 237 and 330 to 377, plus a grep of the headings).
  - I read the question template, the lessons LL-05, 08, 46, 50, 52 and 53, and the earlier three rounds in reviews/P-001-build-gate/critic.md.
  - I read the rulings plan-stop-2, worst-work, model-lab-public, spend-ceiling, test-budget, e002-not-tested and value-target, reviews/44/reviewer.md, the join-up review and the round 4 and 5 headings in reviews/S-001/plan.md.
  - I checked E-003 "Kept", PROJECT.md for the kill and miss lines, risk-paths.toml and AGENTS.md §5.
  - I confirmed that docs/gates/P-001 holds the earlier cases.
- Undone:
  - I did not re-derive the sizing figures.
  - I did not read S-001 lines 238 to 329 in full (the acceptance criteria and join sheets, facts relied on, and risks). I did read the risks and stop rule.
  - I did not open the build-gate cases or the proposals.
  - I did not check whether PR #44 is merged or what else it carries, and I did not check that PACKS.toml still equals what the Reviewer read.
  - I did not open E-003 beyond "Kept", or read the time-and-limit ruling.
- Needed outside my lane: the Chief of Staff fixes findings 1 and 2, and should fix 3 to 8 in the same pass. The redraft goes to a round 2 check. The Orchestrator records this verbatim in reviews/P-001-build-gate/critic.md as round 1 of the new cards.
- Open questions:
  - (1) Does merging the pull request that adds the reading lists also land the cards and the gate case?
  - (2) Should the headline cost of the recommended size be allowed to stay as a pointer? I judge not.
  - (3) The plan frames 2B and 2C as going beyond the ruling. Is that the owner's reading, or only the plan's?

## The cut-down cards, round 2 (commit 595d439; brief 64, a fresh session)

Verdict: PASS

Both cards follow the owner's ruling (B). They are short, they point to the plan's tables instead of copying them, and the terms card argues seven terms and lists four. Round 1's two blocking findings are resolved. I found no new blocking error, but several non-blocking points should be fixed in the same pass. The most important are findings 1 to 3.

Round 1, finding by finding
- **Finding 1 (gate A had no cost): resolved.**
  - Option A now gives 732 runs, about 132 million tokens, and 60 to 121 weeks one after another (32 to 64 if all three collect from the start). These match "Budget options by kind and order".
  - It says the wakes and landing reviews are outside the budget and not estimated ("The budget excludes the wakes").
  - It says "not shown" is the usual result for built work and research ("What the test can and cannot show").
  - The recording precondition is stated and tied to term 9.
- **Finding 2 (terms left out of the plan's questions): resolved.** I mapped terms 1 to 11 to the plan's nine open questions, and everything except budget and size is carried.
  - Q1 and Q2 are term 1. Q3's research question, with C2 and the "test only plans and built work" alternative, is term 3. Q3's time limit is term 8.
  - Q4 is term 2, including the overlap variant. Q5 is term 9 (projects, start-commit field, research started in a conversation) and term 4 (packs).
  - Q6 is term 5. Q7 is term 10. Q8 is terms 6 and 11. Q9 is term 7.
- **Findings 3 to 9: resolved**, except where noted in the numbered findings below.
  - Term 4 now names PR #44, says the lists are not yet merged, quotes the minor note (reviews/44/reviewer.md finding 5) and the expected local failure (finding 6), and says approval is the owner's own action.
  - The sizes are named "size A" and so on, option D's unsupported clause is gone, and the contexts are split.
  - The "reads as going against" attributions are in place, and K1 now says "likely".
  - Terms 1, 2, 5, 7 and 11 are fixed as asked, and "K" jargon is gone from the options.
  - WHO HAS CHECKED IT now cites the round and the record.

Findings (all non-blocking)
1. **Gate card, non-blocking: still no link to the case and the Critic's view.** The opening says they "come with this card", but OPERATING_MODEL §2 says that at a phase gate the card links them. This was round 1 finding 5 and is only half fixed. The files are docs/gates/P-001/build-gate-3-case.md and reviews/P-001/_build-gate-3-critic.md. Add the pointer in WHO HAS CHECKED IT or Context.
2. **Gate card, non-blocking: the recommendation's "about 4 in 5 for every kind" is the library's middle assumption only.**
   - The plan's "In plain words" also says about 1 time in 2 for research and built work if the two versions disagree as often as chance allows (0.51 and 0.54 in the table).
   - The card names the assumption and gives the judge-noise figure and the "not shown" cost, so it is not false. But built work, the first kind, is the case at 1 in 2.
   - Add that one clause, or the pointer to "Size, runs and time" next to the 4 in 5.
   - "Works every kind in turn as you ruled" states the plan's reading of "incrementally" as the owner's ruling. The terms card calls it the plan's "literal reading" and offers B and C that go beyond it. Say "as the plan reads your ruling".
3. **Terms card, term 8, non-blocking: it touches an earlier ruling but is only listed, and states the ruling's scope as fact.**
   - "Your ruling of no fixed length covered Discovery only" is the plan's reading (spec Q3: "does not cover Build").
   - The ruling's record (P-001-time-and-limit.md) also says "no cap on the owner's time", unscoped, and the owner's words are "I want it to be done right. This is my current project and all of my effort will go into it".
   - The proposed answer, no limit, agrees with the ruling, so nothing goes against it. But the card should say it is the plan's reading and quote the ruling. It should also pose the plan's question "does the owner want a firm limit instead?".
4. **Terms card, term 4, non-blocking: the sequence is not explained.**
   - The plan says the packs are "merged before the Build gate" (spec, "Needed outside"). The card says "not yet merged" and approval is by PR #44, which also carries these cards and the gate case. It does not say the plan's condition is unmet as sequenced.
   - The reviewer checked commit 09dfa20. The brief says the PACKS.toml diff to the head f667d4c is empty. The suite was not re-run there. The card says "an earlier commit" and could say that.
   - The plan says only the first list (the blind check) is needed for the test to start. B's cost is stated for "them", both lists.
5. **Terms card, terms 6A, 7B and 2A, non-blocking: whose reading is not always said (LL-05, LL-08).**
   - 6A: "it reads these as one judging session per kind" is the plan's draft reading. B's "the plainer reading" is the plan's "may be". Say whose.
   - 7: "a whole copy is more than a record, so B goes beyond it" is the plan's judgement, unattributed. The model-lab-public ruling (P-001-model-lab-public.md) rests on Model-Lab being "temporary", and covered replay records that included patches and transcripts from the private repository. The card omits that premise.
   - The opening says "one recommended answer" reads an earlier ruling in a way the owner may not have meant. 2A also reads "incrementally" as strictly one after another (attributed to the plan, but it is also a reading).
6. **Terms card, term 2, non-blocking: the overlap variant has no letter.** "You may also let the next kind start collecting while the previous is judged" sits inside A, so the owner's answer "A" is ambiguous. Give it a letter or say how to answer it.
7. **Terms card, term 3, non-blocking: A and B barely differ under the recommended order.** Research already comes last under 2A. State that B means deciding later with research's 200 runs not committed now.
8. **Terms card, term 11, non-blocking: "The first leaves you only stopping the test or ordering a revision" is too broad.**
   - It is true only for the judging session. K3 lets the sheet session's files go in a message.
   - The sentence also does not say which of the three fallbacks "the first" is.
9. **Terms card opening and WHY, non-blocking.**
   - The opening does not lead with what failed or was skipped (AGENTS.md "Plain English first"). Term 1's "the test cannot use past tasks" is the natural lead.
   - "The plan cannot freeze until every term is answered" and "the plan's open questions must be ruled before the freeze" overstate the plan. The plan says that only for questions 8 and 9, with 5 at the gate. The ruling still requires every term answered, so this is a wording point.
10. **Gate card, non-blocking: reversibility is explained inconsistently.** The opening lists kill, runs spent and the frozen plan as irreversible. BLAST RADIUS says option D is why. Hold and recycle give no gain or cost line, which §2 asks for, though the ruling's cut-down allows brevity.

Checked and true
- **Gate card:**
  - The opening leads with the skipped checks and has no ids or paths. The 1-in-2-or-less figure matches the plan.
  - Sizes A to D match the table (732 runs, 132 million tokens, 60–121 and 32–64 weeks).
  - Every pointer leads to a heading that holds what is claimed. Those headings are "Budget options by kind and order", "Size, runs and time", "The owner's actions per option", "The budget excludes the wakes", "Recording is a precondition for plans and built work", "What the test can and cannot show" and "In plain words" with "Still open, and one likely limit".
  - Context: the plan passed at round 3 with the join-up review, and rounds 4 and 5 passed. The 100-run allowance was for Discovery and Design. The size-C and likely-limit attributions are correct.
- **Terms card:**
  - Term 6's two quotes match lines 1 and 10 of plan-stop-2; 9 and about 336 sessions match. The term 7 weeks and the "no commit since 24 October" claim match the spec.
  - Term 10 matches E-003 "Kept". Term 11's 240–484 wake messages and 243–487 new sessions match the table.
  - Term 5's spend-ceiling "at the time" matches that ruling. Term 3's 11–16, 11–19 and 200 runs match.
- **Both cards:** R0 (questions/**), irreversible, default none and timeout none are right for a phase gate and for a term that includes an irreversible step.
- **No unsourced option effects.** Nothing states what a system will do without a record (LL-46, LL-50, LL-52). Term 6B flags its untested tools. Term 2B's "three times" is marked as the Chief of Staff's arithmetic. Term 9's Chief of Staff duty is flagged as a standing duty.

Six-part contract
- **Changed:** nothing. I hold no write tool.
- **Why:** to check round 2 of the cut-down Build-gate cards against the owner's ruling (B) and the records they cite, and to confirm round 1's findings are resolved.
- **Verified:**
  - Both cards, the ruling, round 1 of reviews/P-001-build-gate/critic.md, and S-001.md lines 1–250 and 310–378.
  - The rulings plan-stop-2, time-and-limit, worst-work, model-lab-public, spend-ceiling, test-budget and value-target.
  - reviews/44/reviewer.md, the plan.md round headings and the round 3 section, E-003 "Kept", the question template, OPERATING_MODEL §2, LL-05 and LL-08.
  - The existence of the gate case files and the Critic gate views, and PROJECT.md lines 108, 117 and 158.
- **Undone:**
  - I did not re-derive the sizing or arrival figures.
  - I did not read S-001 lines 251–309 (acceptance criteria, join sheets and facts).
  - I did not open E-003 beyond "Kept", the gate case beyond its recommendation line, or reviews/E-001/reviewer.md.
  - I could not check whether PR #44 is merged or what it carries beyond this branch's contents.
  - I did not re-check AGENTS.md §5 or the lessons LL-46, LL-50 and LL-52 text beyond their headings.
- **Needed outside my lane:** the Chief of Staff should fix findings 1 to 9 in one pass. Findings 1 to 3 matter most for the owner. The Orchestrator records this verbatim in reviews/P-001-build-gate/critic.md as round 2 of the cut-down cards.
- **Open questions:**
  - (1) Does the owner treat term 4's approval-by-merge of PR #44 as satisfying "merged before the Build gate", given that PR also carries the gate case?
  - (2) Are terms 8 and 9 properly "listed" under the ruling, or does the standing duty and the new brief field make term 9 a rule change that must be argued? I judge listing acceptable because the card says so openly.
