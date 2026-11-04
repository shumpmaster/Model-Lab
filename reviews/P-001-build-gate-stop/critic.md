Verdict: FAIL

The Critic's check of questions/P-001-build-gate-stop.md (brief: docs/briefs/60-critic.md, on PR #44's branch), on claude-sonnet-5-5, a different model from the question's writer, verbatim. Recorded by the orchestrator. Session session_01QBwHGKFFgmANWaCNGxCLZd, 2026-11-04.

## Round 1 (commit 85e8c0a; brief 60, a fresh session)

I read the question cold, then checked it against the cited records. The facts about the three failed rounds, the trace and the plan's rounds 4 and 5 are true of those records. The failures are in how the options and the stop rule are put.

**Findings**

1. BLOCKING. The card first says the rule binds, then says it may not.
   - The opening says the cards failed "for the third time, the last allowed". WHY says the choice is yours under the stop rule. DEFAULT says "the stop rule requires the owner's own choice".
   - The recommendation line then admits "the rules limit plan and build checks to three rounds and name no limit for cards". That matches the sources: OPERATING_MODEL §4 and AGENTS.md "Plan stop rule" name plan and build rounds only, and the trace says whether the rule covers cards is "not checked".
   - So "the last allowed" is the Orchestrator's reading by analogy (the trace says brief 54 treats round 3 that way). It is stated as fact in the opening and reversed only at the end of the recommendation.
   - The plain fourth round is the real alternative to A, B and C. It is not in OPTIONS and has no gain, cost, what happens or what it rules out. An owner choosing among A, B and C is not told that a fourth option exists until the last sentence of the recommendation. That is the unfairness to the owner you asked about (LL-05, LL-08).
   - The sentence "the last session applied the limit to the cards, as you asked this one to" is untraced. No cited record shows you asking anything. The trace says only that brief 54 applied it. Delete it or cite it.
   - Fix: open by saying plainly that no rule counts card checks, that three rounds were treated as the limit, and that you may rule it does not apply. Put a plain fourth round in OPTIONS with all four parts.

2. BLOCKING. The recommendation's reason does not match option A's own contents (LL-05).
   - RECOMMENDATION says "the two remaining faults are one-line fixes".
   - Option A is not that. It rewrites term 2 to the plan's corrected question with each order's true weeks (round 4 gives order 1 as 60 to 121, order 2 as the same 60 to 121, and orders 3 and 4 as 32 to 64). It also "looks again" at term 2's recommendation. It also adds the Orchestrator fallback to term 10, a new claim.
   - The trace says the term 2 fix is "a content judgement for the Chief of Staff and the owner, not a wording fix". It also says the check must be strictly diff-limited and any new claim must fail. A rewritten term 2 is exactly new claims. The card does not say that A's gain ("the fewest changes") and its own fail-on-any-new-claim test pull against each other.
   - The cost line should say A may change term 2's recommended answer, and that the new text is the part most likely to fail the check.

3. BLOCKING. Rule effects for B and C are asserted with no record behind them (LL-46, LL-50).
   - B and C both say the cards are "checked as new cards, from the first round". B adds "up to three more rounds of checks".
   - The trace, under Re-specify, says it found no card equivalent of the "starts again at round one" clause and marks it "not checked". Under Re-scope it says whether a re-scoped card starts again at round one is "not checked".
   - Say that the restart and the three-round count for new cards are the Orchestrator's assumption, or cite a rule. The same gap sits behind finding 1.

4. Not blocking. A's gain "to cards whose other points passed three checks" overstates.
   - Round 3 left non-blocking findings open: 3 (the "1 in 2" caveat missing on B, C1 and C2), 5 (the K1 limit not on the gate card, which the trace says should be there), 6 (the opening's "how accurate the judges are", and the "little over half" reading), and 8 (the check record on both cards, and the plan's lettering "plan question n").
   - A touches none of these. The card should say they stay open.

5. Not blocking. The gate card's own "32 to 64 if the kinds collect side by side", on the recommended option A, is not in A's fix list.
   - The trace calls it true as full overlap.
   - After the plan's correction, full overlap is orders 3 or 4, which the plan says go beyond your ruling. Order 4 also needs E-003's registration revised.
   - If term 2's recommendation changes, that headline on the gate card may need a flag. Say whether it stays.

6. Not blocking. B's rule for what the terms card argues does not match the trace.
   - The trace's list of terms the owner must rule before the freeze is Q1, Q2, Q4, Q5, Q8 and Q9 (S-001:353 and :358; the trace cites 5, 8 and 9 as needing the owner).
   - The card's criterion is "touch your earlier rulings, the value target or anything that cannot be undone". That would push Q5 (a rule-change approval, which is only the owner's) and Q8 into the "accept the plan's answer" list.
   - Say that B's list is still answered by you, not delegated.

7. Not blocking. The opening is one dense paragraph.
   - It leads with the failure and has no ids or paths, so it passes that test.
   - "Shortest time ... tied to an order of collecting that cannot give it", "your own part" and "the 100-piece size" are not explained to a cold reader.
   - "Last allowed" is one of two flat statements that need softening (finding 1).

8. Not blocking. The card form is not met on several small points.
   - Context has 7 bullets against a background of at most 5 lines (OPERATING_MODEL §2).
   - DEFAULT "none" is justified. But "what happens if the owner doesn't decide" is not said: the Build gate does not reach you, and nothing else moves.
   - WHO HAS CHECKED IT names a record that does not exist yet. It should cite the round and result once recorded.
   - "Nothing here cannot be undone" is fine.

**Checked and true**
- Trace and Critic round 3:
  - The failed rounds 1 to 3 and the "round 3 had two blocking findings" claim are true.
  - "One a misreading, the other a one-line fix" is a fair paraphrase of the trace: C2's chance is refuted as a clarity point, and "comes to you first" is confirmed with an in-card fix.
  - The 32 to 64 weeks being a plan fault is true. The trace rates it a fault in the plan and calls it under-rated at non-blocking.
- Plan corrections:
  - Round 4 PASS covers the order of the kinds and its weeks. Round 5 PASS covers line 17's worst case (240 to 484 wake messages, 243 to 487 session starts) and the Orchestrator's weekly-landing ask.
  - "Each correction passed its check" holds.
  - Option A's "four checks that put a question to you" is K1 before the first sheet, K3, K4, and K5 at its first check (S-001:177, :180, :181, :187). The statement that the wake messages simply fall to you matches K7 (:189).
- Delegation and stop rule:
  - The ledger holds only L-0001 to L-0005, none a delegation, so "no grant stands" is true.
  - OPERATING_MODEL §2 lets a grant cover choosing a focused review, and only a grant does.
  - "Accepting despite a failed check is never an option" matches §4. The fixed options match. The same-way failure route matches AGENTS.md and the earlier plan-stop ruling.
- Leaving out "drop" is justified:
  - The trace finds it cannot move the gate.
  - S-001:358 sends questions 5, 8 and 9 to the owner at the gate.
  - Dropping the test is the gate's own kill, which is never delegable.
  - The card could add that kill stays available on the gate card whatever you choose.
- Risk and timing:
  - R0 for questions/** and "reversible" are consistent. The blast radius is right.
  - "None" for default and timeout is consistent with the earlier plan-stop ruling ("never a default").
  - It departs from Model-Lab's §5 default for reversible questions, but the reason is given.

**Six-part contract**
- Changed: nothing. I hold no write tool.
- Why: to check the stop-rule question P-001-build-gate-stop as a smart non-expert owner would read it, against the records it cites.
- Verified: I read the card, the Triage record, the three Critic rounds, the plan review's rounds 4 and 5 (reviews/S-001/plan.md, lines 967 to 1034), both Build-gate cards, S-001 lines 171 to 189 and 333 to 374, the ledger, OPERATING_MODEL §2 and §4, AGENTS.md line 38, the earlier plan-stop ruling, the question template, Model-Lab's AGENTS.md §5, and lessons LL-05, 08, 46, 50, 52 and 53. I read only the fixed copies.
- Undone: I did not re-derive the sizing or read sizing.py or output.txt; I relied on the plan reviews' recomputation. I did not read the case, the proposal, or the Chief of Staff's notes. I did not read the full LL-50 context line, which was elided in the grep output. I did not check whether brief 54 or any ruling shows you telling an earlier session to apply the limit to cards.
- Needed outside my lane: the Chief of Staff must fix findings 1 to 3, and should fix 4 to 8. A fresh Critic session on a different model then re-checks. I flag no self-implication for this session (D-050); it is a first check of this card.
- Open questions: Did you ever ask a session to apply the three-round limit to cards? If so, where is it recorded? Does the owner want a plain fourth round offered as option D? Does the gate card's "32 to 64 side by side" line stay under A once term 2's recommendation is looked at again?
