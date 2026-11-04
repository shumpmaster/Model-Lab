*The gate Critic's return on docs/gates/P-001/build-gate-3-case.md and its proposal (brief: docs/briefs/53-critic-gate.md), on claude-sonnet-5-5, a different model from the case's writer, verbatim. Recorded by the orchestrator. Session session_01QBwHGKs5xh6cq2DgNNozv7, 2026-11-04.*

**The Critic's recommendation:** hold — case 3 fixes most of what the second view found, but it still asks the owner to "answer the terms card" and "choose a size on the gate card" without showing the terms card at all. The only Critic record on the two cards that I hold is a FAIL (reviews/P-001-build-gate/critic.md, round 2, seven blocking findings), and the case is silent on it. None of this needs Design reopened. Re-issued with the terms card described, the cards' check status stated, the milestone block and M2's standing settled, and the points under "Citation check" below fixed, I would expect to proceed.

## The Critic's independent view

Records read: the case, the proposal, docs/gates/_GATE.md and _PROPOSAL.md, the second view, and the cited lines of reviews/S-001/plan.md (:1-3, :583, :711, :897-963), reviews/P-001-build-gate/critic.md in full, reviews/44/reviewer.md in full, docs/PROJECT.md :10-166, specs/S-001.md :225-273, the six rulings the case cites, and design-gate-3-case.md :68-80. I did not read experiments/E-003.md. Claims that rest on the spec only are marked "spec only".

**Fair to the plan.**
- plan.md:1 is a PASS. plan.md:583 re-adds 266+200+266=732 and the weeks 60 to 121 and 32 to 64. The case's sizes and the section 6 baseline (9 sessions, 24 to 27 records, 183 to 366, up to 243 to 487) match critic.md:164 and plan.md:906.
- The cause of the worst case is now right: sessions that "cannot be resumed" (critic.md:94). That was my second-view G2.
- The headline limit is now stated honestly. The case says "about 1 in 2 for built work and research if the two versions often disagree, less if a judge errs". critic.md:17 and :133 support it. Two conditions are still missing: 0.8 holds only under the library's middle assumption, and each kind must reach 60 pieces (spec only).
- The 4-in-5 and 1-in-2 figures sit in a FAIL record's findings (critic.md:14, :17). The spec's "Size" section is the better cite.
- The words I counted for sections 1 to 8 come to about 346 without citations, visuals and captions. That is under 350, but it is my own count and the margin is thin.

**What still fails or is weak.**
1. **Terms card still not shown, and no Critic PASS on either card is in the pack.**
   - The case describes the card only as "the terms card's eleven answers". The only cite is critic.md:166, which maps the plan's nine questions onto the card's terms. It says nothing of "eleven" and does not describe the card.
   - Nothing says whether round 3 passed. Section 4 and section 1 rest on critic.md:164, a line in a record that ends in FAIL.
   - This is my second-view finding 5, not resolved.
2. **Non-A sizes are still thin.**
   - Section 4 now draws A, B, C1 and C2 with runs and weeks, which settles the missing options and the letter clash (G3), as far as I can tell without the gate card itself.
   - Tokens (132 million for A; 48, 88 and 188 million for B, C1 and C2 at critic.md:164), power and the owner's part for B, C1 and C2 are not given.
   - The node "C2: 100, 100 and 60" does not say which kind has 60.
   - This is partly resolved.
3. **Form breaches in section 4.**
   - Section 4 gives no Build milestones (M3 to M6), no who-does-what, and none of the dependency picture the form calls standard.
   - Section 3 does not carry Design's join-up result. It appears only in the appendix.
   - Section 6 gives no token usage, and does not say "not recorded".
4. **Section 1: "the plan freezes".**
   - The cited lines do not say it. plan.md:942 says only that the sign-off is not yet recorded.
   - plan.md:939 ("Open questions 5, 8 and 9 stay with the owner before the freeze") supports it and is not cited.
5. **Section 5 citation.**
   - plan.md:935 says the start-commit field is listed under open question 5. It does not say "enter only if the starting point is recorded" (spec AC2 does). The "(terms card)" tag carries no record.
   - "Smaller gains usually read 'not shown'" generalises critic.md:18, which speaks of built work and research only.
   - The risk lines say little of what we would do. For example plan.md:921 gives "keep the word on README's first line, tell the owner not to reuse it".
6. **Section 8 is thin on the set-up and on the ruling that the proposal needs no reader.**
   - The set-up line names the private repository and exclusion. heldback-store:12 also asks the owner to check that the environment does not add the repository to every new session. The case leaves that action out.
   - "No representative reads the proposal, despite its label" cites PROJECT.md:166 (the owner is the user) and the proposal's header line. The option B ruling (/home/user/ml-ask/questions/P-001-gate-citation.md) is not a record in the pack. I took it from the task brief.
7. **Section 6, caption of the owner's-part visual.** It cites "reviews/P-001-build-gate/critic.md" with no line. Cite :164 and :94.
8. **Appendix.**
   - The empty `milestones` block is explained by extending design-gate-3-case.md:75, a Discovery remark, to this gate. No record says the check printed nothing here.
   - Design-4's cite (plan.md:933) covers only the intake, runner and risk-paths citations, not "every fact".
   - Design-6 says "PASS at round 3", and the flowchart draws "Plan review round 1: FAIL, Round 2: FAIL, Round 3: PASS". plan.md:3 shows these are the new draft's rounds. Five earlier rounds (the old draft's rounds 1 and 2 FAIL, then rounds 4 and 5 FAIL) are left out. Label the nodes "New draft, round n" and say the count.
   - "The plan rewritten twice" is not what the rulings say. plan-stop chose one focused confirmation review and plan-stop-2 chose one rewrite (plan.md:3).

**Visuals against the visual rules.**
- Phase flowchart: it matches its text alternative, holds no number, and marks the Build gate. The caption line after the alternative is cosmetic.
- Vision before/after: the figures (2 of 44, 5 of 19, 32 of 80, and the 20 points) match PROJECT.md:111 and :108. "No result exists yet" is stated.
- Sizes flowchart: the numbers match critic.md:164. Tokens and power are unknown for B, C1 and C2 and are not drawn as unknown, but the chart also does not claim them. "C2: 100, 100 and 60" is clearer in the alternative than in the node.
- Owner-part chart: the numbers match critic.md:94, :164 and plan.md:906. It carries no hatched unknown, and the K7 range (wake messages) is absent.
- Plan-review chart: misleading as above.
- Section 3 has no screens, and the case says so (plan.md:927).

**Citation check:**
- Section 1, line 5: "the plan freezes" is not in plan.md:942 or critic.md:164. critic.md:164 does not mention the ruling. Partly resolved from the second view.
- Section 1, line 7: plan.md:1, :583 and worst-work support it. Resolved.
- Section 2, line 18: PROJECT.md:108 and :112 support it. The second view's open point (PROJECT.md:57 and :108 still say "the same past tasks") is not addressed, and the case does not say whether the owner is asked to approve rewording. Spec only.
- Section 3, lines 29 and 30: e002-not-tested:12, :1 and heldback-store:1 support them. Resolved.
- Section 4: the sizes rest on critic.md:164. "C2 ... 60 for plans" is not at :164 and is only in the round-1 finding at critic.md:29. Partly resolved.
- Section 5, line 49: critic.md:14, :17 and :18 support it as a record of the plan, with the condition noted above.
- Section 5, lines 51 and 53: plan.md:897, :963, :913, :916 and :920 support them. "Accepted" is replaced by "to accept". Resolved.
- Section 5, line 54: reviewer.md:17 supports it.
- Section 6: spend-ceiling:10, PROJECT.md:116 and plan.md:899 support it.
- Section 7: PROJECT.md:112 and :113 support it. proposal:24 is AC8. The stale line is resolved. PROJECT.md:114 and :115 (the stop-and-go-to-owner rule) are not mentioned.
- Section 8, line 77: critic.md:166 does not say "eleven" and is not a PASS.
- Section 8, line 79: PROJECT.md:60 and :72 begin the blocks of Build and Launch standard lines. Supported, though the cites are loose.
- Section 8, line 80: see item 6.
- Appendix table: Design-1, 2, 3, 5 and 6 are supported by plan.md:711, :939, :957 and :1. Design-4 is narrower than claimed. The Design-3 and Design-5 "not recorded by the model" labels are correct.
- Appendix, lines 108 and 109: the rulings, and the first and second views, exist. "Rewritten twice" is wrong (item 8).

**Milestones:**
- The fenced milestone block is still empty and the appendix does not say why for this gate.
- M2 is shown ("plan passed review; yours to accept at this gate"). The case does not say whether a merged pull request or research item exists for it, so I cannot say whether a missing sprint is a finding. Its standing should be stated. Reviews/44 shows a Reviewer PASS on PR #44 (the pack entries), but it does not show M2's merge.
- M3 to M6 are Build milestones and need no sprint before this gate. They are not listed, which is part of item 3.
- The six Design standard rows read as achievements, not tasks. Design-3 and Design-5 are "not recorded", which is never a finding and is not claimed reached. Design-6 is claimed reached and plan.md:1 supports it. Design-1 and Design-2 are shown without a reached claim, which is fine.
- Build and Launch standard lines are "all taken on", and none is claimed reached. No project milestone is dropped, and none is wrongly claimed.

**Findings of the second view, one by one.**
- Failure 1 (only A described): partly resolved, see item 2.
- Failure 2 (headline limit): resolved in substance. The missing conditions are noted above.
- Failure 3 ("Accepted"): resolved.
- Failure 4 (no baseline): resolved.
- Failure 5 (terms card not shown): not resolved.
- Failure 6 (set-up half): partly resolved.
- Failure 7 (stale kill line): resolved, with the PROJECT.md:114-115 omission noted.
- Failure 8 (plain words): mostly resolved, since the appendix now defines the terms. They are defined after their first use in sections 1 to 8, and the "terms card" definition cites a record that does not define it.
- Failure 9 (standard visuals): partly resolved. The vision and check-outcomes visuals are added and "no screens" is stated. The dependency picture is still missing.
- Appendix rows (the old-draft cites): resolved with the new draft's lines.
- Milestone block and M2 standing: not resolved.

## The proposal's copy

1. **The eleven scenarios are whole.** I compared AC1 to AC11 (proposal lines 17 to 27) word for word with specs/S-001.md lines 250 to 260, including the "AC<n> [trace: …] —" prefix. Each is the full text of its line, ends where the spec's does, and carries the right `[specs/S-001.md:250..260]` citation. None is cut short. The long clauses of AC4 and AC5 are complete.
2. **The second view's form breaches are fixed.**
   - The proposal no longer cites the Critic's plan review or anything under decisions/.
   - Section 5 now cites PROJECT.md:99 for the spend ceiling.
   - Section 2 now says "no instruction changes".
3. **Section 1, line 7.** PROJECT.md:13 supports "role files, each task's brief, and what each is given to read". It does not say "three candidate changes". That comes from the spec's AC1 (C1, C2, C3). It is true of the records and a fair summary, but it is cited to the wrong line. C2 also changes the inputs a brief names and C3 changes a check's brief, so "written instructions" is a fair summary rather than exact.
4. **Section 1, line 8.** "At most 1 time in 40" is true of PROJECT.md:108. It omits that AC7 also needs the owner's cards to confirm the judge. "Only if" keeps it true.
5. **Section 2.** Both lines are true of PROJECT.md:109 and :112.
6. **Section 4.** "No screens: the fair test has no screens or views; the owner sees records and short cards" is in the form and is true. It carries no cite, which the form does not require.
7. **Section 5.** The two lines are true of PROJECT.md:99 and :116. The section holds nothing of the owner's setup or effort, which the form asks for "as the records hold them": the private repository, the cards, and the sessions to start. The case carries these. Add them here, citing heldback-store:12 or plan.md:906. Decisions/ citations are barred in a proposal by the form, so use the spec or PROJECT.md instead.
8. **Header line.** "Shown to the user representative, a simulation of the target user, not real users" is the form's fixed text, but by the owner's option B no user representative reads this proposal. The case says so (section 8). The proposal's own line still says otherwise. I leave the fix to the Chief of Staff, per the second view's question 1.
9. **Readability.** AC4 and AC5 use terms never defined in the proposal (sheets repository, fingerprint, K4, locked checks). The owner ruled for the full text, so I do not fail the copy.
10. **Word count.** Sections 1, 2 and 5 are about 140 counted words, under the 200 cap.
11. **Fairness to the plan.** Beyond the criteria themselves, the proposal's other lines (the 1-in-40 chance and the 20-point gain) are true of PROJECT.md. The case's claim that the proposal holds nothing but the form's sections is true.

## The six-part contract

1. **What I changed:** nothing. I hold no write tool.
2. **Why:** to give the Build gate's third case its Critic section, to say for each second-view finding whether case 3 resolves it, and to check the proposal's copy.
3. **What I verified:**
   - Read in /home/user/ml-gate (commit ea0aaac): the case, the proposal, _GATE.md and _PROPOSAL.md, the second view, specs/S-001.md :225-273 (AC1 to AC11 word for word), docs/PROJECT.md :10-166, reviews/S-001/plan.md at :1-15, :575-595, :706-714, :840-966, reviews/P-001-build-gate/critic.md in full, reviews/44/reviewer.md in full, the rulings spend-ceiling, e002-not-tested, heldback-store, worst-work and design-gate, and design-gate-3-case.md :68-80.
   - My own word counts: the case about 346, the proposal about 140.
4. **What is undone:**
   - I did not read the gate card (questions/P-001-build-gate.md), the terms card, experiments/E-003.md, the whole spec, or most of plan.md. I did not read the old draft's rounds.
   - I did not read the ml-ask question or the owner's option B ruling. I took it from the task brief.
   - I did not run sizing.py or `v3_checks gates`.
   - Claims marked "spec only" rest on the spec alone.
5. **Needed outside my lane:**
   - The Chief of Staff, for the case:
     - Describe the terms card, or say where the owner sees its eleven terms.
     - State the cards' check status, citing a round that passed, or say none exists.
     - Give tokens, power and owner's part for B, C1 and C2.
     - Add the Build milestones and who does what to section 4.
     - Fix the "rewritten twice" claim and label the plan-review visual as the new draft's rounds.
     - Add the environment-check half of the set-up.
     - State M2's standing and the reason for the empty milestone block.
     - Cite plan.md:939 for the freeze.
   - The Chief of Staff, for the proposal: fix the PROJECT.md:13 cite for "three candidate changes", add the owner's setup to section 5, and settle the header line.
   - The owner: the criteria, the size and the terms card.
6. **Open questions:**
   - Did the gate card and the terms card pass a round 3? The pack holds only the round 1 and round 2 FAILs.
   - Should the "Shown to the user representative" header stay in a proposal the owner ruled no representative reads?

Files: /home/user/ml-gate/docs/gates/P-001/build-gate-3-case.md, /home/user/ml-gate/docs/gates/P-001/build-gate-3-proposal.md, /home/user/ml-gate/specs/S-001.md, /home/user/ml-gate/reviews/S-001/plan.md, /home/user/ml-gate/reviews/P-001-build-gate/critic.md, /home/user/ml-gate/reviews/P-001/_build-gate-2-critic.md
