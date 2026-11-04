*The gate Critic's return on docs/gates/P-001/build-gate-4-case.md and its proposal (brief: docs/briefs/65-critic-gate.md), on claude-sonnet-5-5, a different model from the case's writer, verbatim. Recorded by the orchestrator. Session session_01QBwHGKFFgmANWaCNGxCLZd, 2026-11-04.*

**The Critic's recommendation:** proceed. Case 4 settles the third view's central finding (the cards' check status), and the terms card is still described only in the appendix. I found no claim the records contradict, and the eleven criteria are copied whole. The Chief of Staff should still correct four small things (listed below), most of all the missing cost of size A.

## The Critic's independent view

Read from /home/user/ml-gate4 (225ca26): the case, the proposal, docs/gates/_GATE.md and _PROPOSAL.md, and the third view. Also read: docs/PROJECT.md (all of Part 1), reviews/S-001/plan.md (:1-3, :248-257, :530-535, :580-583, :708-714 and :893-1026), reviews/P-001-build-gate/critic.md (:12-19, :90-97, :160-189 and :265-438), reviews/44/reviewer.md in full, reviews/P-001-standard-lines/critic.md in full, the rulings heldback-store and e002-not-tested, and specs/S-001.md :225-273. I did not read experiments/E-003.md, the Chief of Staff's notes, docs/briefs/** or docs/reports/**. I could not read the owner's cut-down ruling (/home/user/ml-ans/decisions/questions/P-001-build-gate-stop.md), which was outside the fixed copy. The case cites the cut-down only through critic.md:360, and I took it from that record.

**Fair to the plan.**
- The plan passed (plan.md:1). The new draft's round 3 passed, and the two focused corrections passed at rounds 4 and 5 (plan.md:3, :967-1026).
- The sizes in section 4 are supported by plan.md:253-256 and :583: A 732 runs and 60 to 121 weeks; B 490 and 40 to 81; C 7 to 15; D 1,040 and 87 to 173. Section 6's worst cases (240 to 484 wake messages, 243 to 487 new sessions, presented as alternatives) match plan.md:1019 and critic.md:164.
- The round-5 pass confirms the 4w and 4w+3 arithmetic. The cause of each worst case is now the right one (wake failure against resume failure).
- The visual of the plan's review rounds is now right. plan.md:3 gives the first draft FAIL, FAIL, PASS, FAIL, FAIL, then the new draft FAIL, FAIL, PASS, then PASS and PASS for the two corrections, which is ten rounds.
- The "rewritten twice" error is gone. The rulings line says one focused review and then one rewrite (plan-stop and plan-stop-2).
- My count of sections 1 to 8, without citations, visuals, captions and headings, is about 349 words. That is under 350 with no margin, and it is my own count.

**Still weak.**
1. **The cost of the recommended size is not in the case's words.**
   - Size A's 132 million tokens appear nowhere in sections 1 to 8. critic.md:164 and :368 hold the figure.
   - The caption of the sizes visual says "Tokens and chances for sizes other than A are on the gate card", which implies A's are given. A's chance is in section 5, but its tokens are not.
   - The cards' own round-2 check judged that the headline cost should not be left as a pointer (critic.md:357, :268-269).
   - The owner is asked to "proceed at size A, 732 runs" and sees runs and weeks only. The worst-case sessions are drawn as alternatives that are not summed.
   - Unknown values are named but not hatched. These are the wakes' cost ("outside the budget") and the owner's usage ("not recorded"), which is fair as text.
2. **"It tests every kind in turn" is the plan's reading, stated as settled.**
   - Section 1 cites worst-work. The round-4 review says "in turn" is the spec's own reading, that the ruling's words are "work it incrementally because everything should be touched", and that the order is the owner's open question 4 (plan.md:981).
   - critic.md:389 already asked for "as the plan reads your ruling".
   - The 60 to 121 weeks hold only for one kind after another (plan.md:973-979).
3. **The terms card is still described only in the appendix (line 113).** Its status is now stated and it passed (critic.md:360-364). Section 8 still says only "the terms card's answers". The owner's deadline-bearing action is not described, and the non-blocking findings 1 to 10 of the round-2 check (critic.md:383-410, "fix in the same pass") are not said to be fixed. This is the part of the second and third views' finding 5 that stays open.
4. **Section 4 has no dependency picture.** The form's standard visual is "how the deliverables depend on each other". Section 4 draws sizes instead. The text at PROJECT.md:37 would support such a picture.
5. **The empty `milestones` block.** The reason is still borrowed from design-gate-3-case.md:75. That line says "the timeline prints no milestone lines... whose Discovery ran from a conversation", which is a Discovery remark. No record says the gate check printed nothing here. The form says to copy the check's block and never write lines by hand.
6. **The section 7 stop rule is partial.**
   - PROJECT.md:114 (too few pieces) is not mentioned, and neither is :115.
   - "At every token checkpoint and 16-week review point" cites proposal:24 (AC8). AC8 says "every 20 runs of each side and 16 weeks after each kind opens"; "token checkpoint" is the PROJECT.md:99 and :115 term for the earlier 100-run allowance.
7. **The risk lines say little of what we would do.** Only the secret word (plan.md:921) and the reading-list note carry an action.

**Citation check** (by section and line of the case):
- Line 5 and line 7: supported (critic.md:360-362, plan.md:939, :535, worst-move ruling). Plan.md:1 is only the PASS line and does not carry "tests every kind in turn" (see 2 above).
- Line 18 (section 2): supported (PROJECT.md:108, :112).
- Line 22 (the vision visual): supported (PROJECT.md:111, :108). The alternative figures (27 of 75 for built work, 2 of 19 for research) are not drawn. This is non-blocking, because the stated figures are the ones PROJECT.md leads with.
- Lines 29 to 32 (section 3): supported (e002-not-tested:1 and :12, heldback-store:1, plan.md:939 and :927).
- Lines 36 and 37 (section 4): supported (PROJECT.md:65, :66, :68, :69, :89, :90).
- Section 4's Size D wording, "100 research and built work, 60 plans": plan.md:253-256 and :535 give runs and weeks only. The composition is not at the cited lines. It is consistent with plan.md:248-250 (plans 21 to 42 at 60 pieces, research 53 to 107 at 100) but not cited.
- Section 5, lines 51 to 55: supported (critic.md:17, :386, :272; plan.md:897, :963, :913, :916, :921; reviewer.md:17). "Less if a judge errs" rests on critic.md:14 and :17, which are not both cited. The 0.8 holds only under the library's middle assumption and only if each kind reaches 60 pieces (spec only).
- Section 6, lines 59 and 60: supported (spend-ceiling:10, PROJECT.md:116, plan.md:899). The chart numbers match critic.md:164 and plan.md:1019.
- Section 7, line 73: see weak 6.
- Section 8, line 78: "the terms card's answers... [critic.md:373]" cites the mapping of the plan's questions to terms. The words "seven argued and four listed" (appendix line 113, same cite) are at critic.md:364, not :373. Reviewer.md:28 supports the "owner's approval and merge" of PR #44.
- Section 8, line 79: heldback-store:12 supports the private repository, but not "kept out of other sessions" verbatim. It says the owner "checks that the environment's settings do not add it to every new session". Close enough.
- Section 8, line 81: PROJECT.md:166 and proposal:3 support the reason. The ruling that no representative reads the proposal (decisions/questions/P-001-gate-citation.md, option B) is a record in the pack but is not cited. Cite it.
- Line 90 and the appendix flowchart note: see weak 5.
- Appendix, lines 108 to 110: critic.md:360 and :178 (round 3 FAIL), the standard-lines PASS, and the rulings exist and say what is claimed. "Three failed rounds" matches rounds 1 to 3 (critic.md:180).
- Appendix table: Design-1, 2, 3, 5 and 6 are supported (plan.md:711, :957, :939, :1, :3, :942). Design-4's cite (plan.md:933) covers only the plan's cited intake, runner and risk-paths lines, not "every fact"; it is narrow, and it was flagged in the third view (item 8).
- M2's row says "its pull request is open, so no sprint has merged". No cited record says the pull request is open. reviews/44 concerns the PACKS pull request, which is not M2's.
- Case form: sections 1 to 8 are in the form. The proposal is the owner's version of the criteria by ruling, so no user representative read it. Nothing in the case reports what a user representative said.

**Visuals against the visual rules.**
- Phase flowchart: the drawing matches its alternative, and it holds no number. The Build gate is marked.
- Vision chart: the drawing matches the alternative (2 of 44, 5 of 19, 32 of 80, 20 points). "No result exists yet" is stated.
- Sizes chart: the drawing matches the alternative and the numbers match plan.md:253-256. The caption implies A's tokens are on the case; they are not (weak 1).
- Owner's-part chart: the drawing and the alternative match critic.md:164 and plan.md:1019. The two worst cases are alternatives, not a sum, and that is stated.
- Plan-review chart: matches plan.md:3 and its alternative (ten rounds).
- No chart holds a trend, rating or number the records lack. No screen is drawn, and "no screens" is stated (plan.md:927).

**Milestones.**
- The fenced block is empty. See weak 5.
- M2 is "yours to accept at this gate". Its pull request being open is uncited (see the citation check), so I cannot say a missing sprint is not a finding. If a merged pull request for M2 exists, the Chief of Staff should say so.
- Design-1 to Design-6 read as achievements, not tasks. Design-3 and Design-5 are "not recorded", so they are never a finding and are not claimed reached. Design-6 is claimed reached and plan.md:1, :3 support it.
- Build and Launch standard lines are "all taken on". None is claimed reached, and the reworded lines passed (reviews/P-001-standard-lines/critic.md).
- M3 to M6 are Build milestones, and no sprint could exist before this gate. Section 4 names them as achievements, not tasks.
- No project milestone is dropped.

**The third view's findings, one by one.**
- Terms card not shown / no PASS in the pack: partly resolved. The round-2 PASS is cited (critic.md:360-364), and the rounds 1 to 3 history is stated. The card is still not described outside the appendix, and the non-blocking items outstanding are not mentioned.
- Non-A sizes thin: resolved in form. The sizes are drawn with runs and weeks, but the caption's "other than A" leaves A's own tokens out.
- Form breaches in section 4 (milestones, who does what): resolved. The dependency picture is missing.
- Section 3 without the join-up result: resolved (line 31).
- Section 6 without "not recorded": resolved (line 60).
- "The plan freezes" (item 4): resolved with plan.md:939.
- Section 5 citations and generalisations: mostly resolved. "Not shown" is now limited to built work and research (critic.md:272), and "to accept" replaces "accepted".
- Section 8 set-up and the ruling that the proposal needs no reader: the environment half is resolved (line 79). The ruling is still not cited (line 81).
- Owner's-part visual cite: resolved (critic.md:164 and plan.md:1019).
- Appendix: empty milestone block unresolved. Design-4 unresolved. "Rewritten twice" resolved. Visual labelling resolved. Defined terms are now in the appendix, after their first use in sections 1 to 8; the "terms card" definition cites :373, which does not hold the words (they are at :364).
- M2's standing: partly resolved (stated, uncited).

## The proposal's copy

1. **The eleven scenario lines are whole.** I compared AC1 to AC11 (proposal lines 17 to 27) with specs/S-001.md lines 250 to 260, including the prefix and the long clauses of AC2, AC4 and AC5. Each is the full text of its line and none is cut short. Each carries the right line number, [specs/S-001.md:250] to [specs/S-001.md:260]. This rests on the spec only (not E-003). I did not read E-003.
2. **Section 1.** Line 7 now names "candidate changes" with no count, so the third view's misplaced "three" is gone; PROJECT.md:13 supports it. Line 8 is true of PROJECT.md:108. It omits AC7's second condition (the owner's cards confirming the judge). "Only if" keeps it true.
3. **Section 2.** True of PROJECT.md:109 and :112.
4. **Section 4.** "No screens" is in the form and is true. It has no citation, which the form does not require.
5. **Section 5.** The two lines are true of PROJECT.md:99 and :116. The owner's own set-up (the private repository, the cards, the sessions to start) is still not in the proposal. The third view asked for it (item 7 of that view). The case carries it. Non-blocking.
6. **Header line 3.** "Shown to the user representative, a simulation of the target user, not real users" is the form's fixed text. By the owner's option B nobody reads the proposal in that role. The case says so in section 8 but cites no ruling (see citation check). The third view's question stays open: whether the header should stay.
7. **Readability.** AC4 and AC5 use terms the proposal never defines (sheets repository, held-back check, fingerprint, K4, locked checks). The owner ruled for the full text, so I do not fail the copy.
8. **No other line of the proposal cites a decision record or the Critic's plan review.** The form's bar on those cites is respected.

## Six-part contract

1. **Changed:** nothing. I hold no write tool.
2. **Why:** to give the Build gate's fourth case its Critic section, to say for each third-view finding whether case 4 resolves it, and to check the proposal's copy against specs/S-001.md.
3. **Verified:**
   - Read from /home/user/ml-gate4 (225ca26): the case, the proposal, _GATE.md, _PROPOSAL.md, reviews/P-001/_build-gate-3-critic.md, docs/PROJECT.md, reviews/S-001/plan.md at :1-3, :248-257, :530-535, :580-583, :708-714, :893-1026, reviews/P-001-build-gate/critic.md at :12-19, :90-97, :160-189, :265-438, reviews/44/reviewer.md, reviews/P-001-standard-lines/critic.md, the rulings heldback-store and e002-not-tested (and found gate-citation, worst-work, spend-ceiling, design-gate and plan-stop(-2) in the pack), design-gate-3-case.md :66-81, specs/S-001.md :225-273.
   - AC1 to AC11 against spec lines 250 to 260.
   - My own word count for sections 1 to 8 (about 349) and the arithmetic of sizes and worst cases against plan.md.
4. **Undone:**
   - I did not read the gate card or the terms card (outside my pack), experiments/E-003.md, the sizing tables, or most of plan.md.
   - I did not read the owner's cut-down ruling in /home/user/ml-ans (outside the fixed copy). I took the cut-down from critic.md:360.
   - I did not check whether the cards' round-2 non-blocking findings were fixed, or whether M2 has a merged pull request or whether PR #44 is merged.
   - I did not run `v3_checks gates` or sizing.py.
   - The claims about the criteria (the copy) rest on the spec only.
5. **Needed outside your lane:** the Chief of Staff, for the case:
   - Give size A's token cost in sections 1 to 8, or drop the caption's implication that A's are given.
   - Say "as the plan reads your ruling" about the order, and that the order is an owner's question.
   - Describe the terms card in one line in section 8.
   - Say whether the round-2 non-blocking findings were fixed.
   - Add the dependency picture to section 4.
   - Fix the cite for "seven argued and four listed" (critic.md:364, not :373).
   - Cite P-001-gate-citation.md for the "no representative" line.
   - Cite a record for M2's open pull request, or say none exists.
   - Settle the empty milestone block with a record showing what the check printed.
   - Reword the AC8 reference in section 7 ("every 20 runs of each side").
   - For the proposal: add the owner's set-up to section 5 and settle the header line.
6. **Open questions:**
   - Should a proposal the owner ruled no representative reads keep the form's "Shown to the user representative" header? This was the third view's open question.
   - Is the milestone block empty because the gate check printed nothing, or because it was not run?
   - Did the cards' round-2 non-blocking findings get fixed in a later commit?
