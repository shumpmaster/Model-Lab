Verdict: FAIL

*The Critic's cold read of questions/P-002-plan-stop.md, the owner's card on the plan stop (P-002, M9), in a fresh session on a different model from the writer, the Chief of Staff's session. Round 1: brief docs/briefs/278-critic.md, FAIL, two blocking findings. Recorded verbatim by the orchestrator, session session_01QBwHGNPKhVy6fgoUjKtW6q, 2026-11-12.*

## Round 1
Verdict: FAIL

Brief 278: Critic's cold read of questions/P-002-plan-stop.md, read only from /home/user/ml-fixed-278. I wrote nothing. This is a first check of this card, so no finding implicates an earlier check of mine (D-050). Findings 2, 4 and 9 below reflect on earlier Critic checks, because the records they rest on came from them. I read the card, questions/_TEMPLATE.md, AGENTS.md section 5, reviews/S-002/plan.md (rounds 1 to 3 and the re-check), docs/briefs/276-definer.md, experiments/E-004.md (Exclusions, lines 119 to 130), reviews/S-001/plan.md, decisions/questions/P-001-plan-stop.md, and docs/projects/P-002.md section 6.

What holds:
- The story in the opening paragraph matches the record. The plan passed at round 3 with nine non-blocking findings. Finding 3 was the piece and pull request mismatch. The Definer's answer counted a merged pull request once on the first entry's side and left the later place empty. The re-check failed on two blocking points: the second-look rule becomes undefined with an empty place, and a session that knows the sides can empty a place it chooses. All of this agrees with reviews/S-002/plan.md and E-004:123 to 129.
- Context lines 31 to 35 match the records. Line 35 matches P-001's plan stop precedent.
- "Nothing is frozen and no trial has started" is consistent with E-004 and S-002 still carrying draft placeholders.
- Option A's mechanism is real. E-004:120 gives reserve places 61 to 63 and a cap of 3 withdrawals per look. The re-check's own fix for finding 1 was the reserve place, with voids and withdrawals counted toward one cap.
- "Seven smaller points" is correct: re-check findings 3 to 9.
- Option C's "the part that has needed fixing in every round" is fair. Rounds 1, 2 and 3 and the re-check all had findings on withdrawal and entry.

Findings

1. BLOCKING. Card lines 8 to 23 (OPTIONS) and 36 (Context). The options are not the stop rule's fixed ones, and the card does not say why. The Context line itself lists the fixed choices as "re-specify, re-scope, drop, or one focused confirmation review". The card offers A (one focused confirmation review), C (re-specify), and B ("undo the late fix and keep the plan as it passed"). B is not on the list. Re-scope and drop are absent with no reason given. B also leaves the piece and pull request question open, so it reads close to "accept despite a failed check", which line 36 says is never an option. The passed plan is a legitimate state, but the card must say how B fits the rule.
   Fix: either (a) state in one plain sentence why re-scope and drop do not apply here, and show B as a form of the focused-confirmation family (undo the failed change and confirm only the reverted text), or (b) replace B with a listed option. If B stays, say plainly that its open question is carried and not accepted as settled, and where it will be decided.

2. BLOCKING. Whole card (lines 5, 10, 13, 15, 20; compare AGENTS.md section 5 and LL-80). Words a newcomer needs are not defined. The card never says what the trial is trying to show, or what "piece", "side", "place", "second look" or "entering a piece twice" mean. The unexplained terms are:
   - "piece": a merged pull request.
   - "side" and "place": which arm of the trial a piece sits on, and one of its 60 slots per look.
   - "the second look": a second round of 30 more each way.
   - "the hand check" and "the scenario card".
   Terms like "the rule for whether the second look runs is written for 30 each way" mean nothing to a newcomer. Only "scenario card" is glossed, and only in option B.
   Fix: add two plain sentences at the top, for example: "A trial gives 30 pieces (merged pull requests) to a method and 30 without it, each in a numbered place drawn by shuffle, and may add 30 more each way at a second look." Gloss "hand check" ("a check by hand of the counting rules on 60 past pieces") and "withdrawn/dropped" ("left out and replaced").

3. Not blocking. Option A, Gain line (line 12): "no new route lets a piece be dropped by choice" overclaims. A refill under the cap of 3 still lets a dispatcher who knows the sides use up to three void or duplicate entries a look, and refilled places are chosen by the same people. The re-check's own fix says to add "merging ... or entering a brief twice" to the plan's stated limit on sides known ahead. The card says it adds these routes to the limits, but the Gain line says no route exists.
   Fix: "no new uncapped route: at most three pieces a look can be dropped this way, and the plan states that as a limit."

4. Not blocking. Option A, Cost line (line 12). The cost is understated. Beyond one more change and check:
   - Voids now share the cap of 3 with real withdrawals, so a trial can stop sooner and come back to the owner.
   - Each refill adds a wait, because a reserve piece must be dispatched and merged after the withdrawal (E-004:121).
   - The precedent on line 35 shows a focused fix failing again. In S-001 the owner chose a focused fix, it failed, and the owner then chose to re-specify (reviews/S-001/plan.md header).
   Fix: add these to the Cost line, and say in the RECOMMENDATION that the S-001 precedent is why the confidence is only moderate.

5. Not blocking. Option B, Cost (line 17): "The Critic judged that mostly harmless at round 3, but not settled." Round 3 finding 3 said "The effect is mostly conservative, so it is not blocking". The re-check then found that merging a later touch-heavy "with" piece under an earlier "without" entry widens the gap in the method's favour (finding 2). "Harmless" overstates. Fix: quote the round 3 word ("mostly conservative") and add the re-check's finding that it can favour the method. Also add the plan's stated limit about entries steered by someone who knows the sides.

6. Not blocking. Line 10 and option A: "three spare places a trial already holds". E-004:120 gives three reserve places per look and a cap of 3 per look, so a trial holds up to six over two looks. Context line 34 says "a look". Fix: say "each look holds three spare places".

7. Not blocking. Line 7 (WHY): "the trial's fairness rests on no one being able to choose which pieces drop out after the sides are known (docs/projects/P-002.md, section 6)". P-002 section 6 (line 184) says only "shuffled draws before work starts"; it does not say the dropped-pieces point. The point is in reviews/S-002/plan.md round 1 finding 7 and the re-check finding 2. Fix: cite those, or quote section 6's actual words.

8. Not blocking. Line 27 (DEFAULT none, TIMEOUT none) against AGENTS.md section 5 ("Reversible questions adopt the recommendation at timeout"). The card marks the question reversible and gives no default, which departs from section 5. The reason offered is "the stop rule leaves the next step to you". The stop rule is cited to Personal-Org-Operating-Model OPERATING_MODEL.md §4, a file that is not in this copy, so I could not verify the text. P-001's card record uses the same wording ("never a default"), so the choice is consistent with precedent. Fix: cite the exact rule line that forbids a default, or put the AGENTS.md exception in the card in words. R0 is consistent with risk-paths.toml (questions/** is R0). "Reversible" and the blast radius fit a pre-freeze plan choice.

9. Not blocking. Line 25 (WHO HAS CHECKED IT). It names only the Critic's plan review. The recommendation (A) was written by the Chief of Staff, and the options come from the Critic's own findings, so the card has had no independent check beyond this one. Fix: say so, or add "this card: Critic cold read, reviews/P-002-plan-stop/critic.md".

10. Not blocking. Line 24 (RECOMMENDATION). "A, with moderate confidence" is honest. The "what would change it" lines are fine, but add a third: "or the check fails again, which sends it back to you", since A can itself fail (as the card admits at line 12).

Six-part contract
- Changed: nothing. I wrote no file.
- Why: brief 278 asked for a cold reading of the owner's card on the plan stop (P-002, M9), against AGENTS.md section 5 and questions/_TEMPLATE.md.
- Verified:
  - Every statement in the card against reviews/S-002/plan.md (rounds 1 to 3 and the re-check), docs/briefs/276-definer.md, and E-004 Exclusions lines 119 to 130.
  - The P-001 precedent against decisions/questions/P-001-plan-stop.md and reviews/S-001/plan.md.
  - The risk class against risk-paths.toml.
  - The template's fields. The card carries WHY, OPTIONS, RECOMMENDATION, RISK CLASS, REVERSIBILITY, BLAST RADIUS, DEFAULT, TIMEOUT and a sourced Context list.
- Undone:
  - I could not open Personal-Org-Operating-Model OPERATING_MODEL.md §4. The stop rule's list of fixed options and its no-default rule are checked only through the card's own Context line 36, reviews/S-001/plan.md and decisions/questions/P-001-plan-stop.md.
  - I did not open the Definer's diff, so I cannot say that no other change was made on brief 276.
  - I did not open docs/projects/P-002.md beyond section 6.
- Needed outside your surface:
  - The Orchestrator records this return verbatim in reviews/P-002-plan-stop/critic.md.
  - The Chief of Staff fixes findings 1 and 2, and ideally 3 to 10, and brings the card back for a re-check before it goes to the owner.
- Open questions:
  1. Does the stop rule allow "restore the passed plan and carry the open question" as a fixed option, or is it a form of one focused confirmation review? The Chief of Staff should cite the rule line.
  2. Is no default for a reversible R0 stop-rule choice an agreed exception to AGENTS.md section 5? If so, cite it.
