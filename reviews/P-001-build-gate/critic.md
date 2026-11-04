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
