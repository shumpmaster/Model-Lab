*The gate Critic's return on docs/gates/P-001/build-gate-2-case.md and its proposal (brief: docs/briefs/51-critic-gate.md), on claude-sonnet-5-5, a different model from the case's writer, verbatim. Recorded by the orchestrator. Session session_01QBwHGKs5xh6cq2DgNNozv7, 2026-11-04.*

**The Critic's recommendation:** hold — case 2 fixes the biggest gap in the first view: the eleven criteria are now in the proposal, and each is a word-for-word copy of S-001. The case still cannot support the owner's ruling, for four reasons:
- It asks the owner to "choose a budget" but describes only option A.
- It understates the headline limit on what the test can show, against a record it cites.
- Several cited lines do not say what they are cited for, and some come from the superseded old draft of the plan review.
- It still lists no project milestone and draws none of the standard visuals except the phase flowchart.

None of this needs Design reopened. Re-issue the case with these fixed and I would expect to proceed.

## The Critic's independent view

I read the case, the form (docs/gates/_GATE.md and _PROPOSAL.md), the proposal, docs/PROJECT.md in full, and the first view (reviews/P-001/_build-gate-1-critic.md). I also read every cited record: reviews/S-001/plan.md at the cited lines, reviews/P-001-build-gate/critic.md, reviews/44/reviewer.md, reviews/E-001/reviewer.md:1-33, reviews/P-001-standard-lines/critic.md, the design-gate-3 case line 75, and six rulings (design-gate, worst-work, spend-ceiling, heldback-store, e002-not-tested, plan-stop-2). Claims that rest on specs/S-001.md only are marked "spec only".

**Fair to the plan.**
- plan.md:1 is a PASS, and plan.md:939 says "Blocking differences: none". The case is right on both.
- The run sums and weeks are right: 732 = 266+200+266, A is 60–121 and 32–64 weeks, B 490, D 1,040. Round 1 of the new draft re-adds them (plan.md:583).
- The flowchart text alternative is correct, and the Discovery and Design nodes now cite the Design-gate ruling (design-gate:1) and plan.md:1.
- Section 6 now says "whether 732 runs fit is not known; work waits for the reset", which spend-ceiling:10 and PROJECT.md:116 support. Section 7 now carries the "stop and ask" rule.
- The sections 1 to 8 word count is about 342 without citations, under the 350 cap. This is my own count and sits close to the limit.

**What still fails.**
1. **Only option A is described.** The ask is "choose a budget". Section 4 gives B 490, C 266 and D 1,040 as bare run counts.
   - It does not say what B, C or D test, what each costs in tokens, or what each can show.
   - "Built work only" for C is not in the cited lines (plan.md:255 says only "C: 7–15"). It is spec only.
   - The 300-run estimate now sits beside 732, which is good.
2. **The headline limit is understated against the record it cites.** Section 5 line 32 says "about 4 in 5 at best, 1 in 2 if a judge errs".
   - reviews/P-001-build-gate/critic.md:17, which the case cites, says built work and research fall to about 0.51 and 0.54 even with a perfect judge, if the versions disagree as often as chance allows. Spec :13 says the same.
   - A judge wrong 1 time in 10 takes it to "about 1 in 2 or less" for the best case. A reader of the case would think the 1-in-2 case arises only from judge error.
   - The 4-in-5 figure holds only if each kind reaches 60 pieces (spec :13). The case omits that condition.
3. **"Accepted" in section 5 line 36 is not an acceptance.** Nobody has accepted these. The Critic rated them non-blocking, and plan.md:939 says they are "carried into the gate's case as risks". They should be presented as risks the owner is asked to accept.
   - The "word public only on a failed check" phrase is cryptic. plan.md:920 is about the canary word entering a public record.
   - The risk lines still do not say what we would do and where it stands, apart from "first-use checks show it".
4. **Line 34 gives only the failure case.** The "243 to 487" figure is the K5-in-the-Orchestrator column at plan.md:906, not every case of sessions failing to wake. The ordinary figure (180 to 360, spec only) and the nine sessions are missing, so "rise to" has no baseline.
5. **The terms card is not shown.** The open questions are not listed, and the only Critic record the case cites for the card (critic.md:35) is a heading in a round-1 FAIL.
   - The pack holds no later check of it.
   - Section 8 asks the owner to agree to a card the case does not describe and whose only Critic record is a FAIL.
6. **The owner's set-up is incomplete.** heldback-store:12 also asks the owner to check that the environment does not add the sheets repository to every new session. Section 8 line 54 omits that half.
7. **Section 7 line 48 is stale.** PROJECT.md:115 is about the 100 runs allowed through Design being used up before the test is ready. The test is now ready (plan passed), so the line misdescribes the stop rule that applies in Build. The owner's go-on or stop rule is the review points in AC8, and the line does not mention them.
8. **Plain words.** "Terms card", "kinds", "relays", "reading lists", "first-use checks" and "the side writing your cards" are still undefined for a non-expert.
9. **Standard visuals.** The case has only the phase flowchart. Section 2's before-and-after, section 4's dependency picture, section 6's owner-time picture and the appendix's check-outcomes visual are absent, as in the first view. Section 3's thumbnails do not apply, since the project has no screens, but the case does not say so. This is a form finding.

**Visual (the flowchart).**
- It matches its text alternative, holds no number, rating or trend, and no unknown is drawn as known.
- Its nodes now cite correctly (design-gate:1, plan.md:1).
- The caption line "Where the project stands" comes after the text alternative with its citations. That is cosmetic.

**Citation check:**
- **Section 1, line 5.**
  - plan.md:942 supports that the owner's criteria ruling is not yet recorded. plan.md:960 lists open questions 5, 8, 9 and the canary file.
  - Neither says "the plan then freezes", mentions a budget, or mentions the terms card.
  - Partly resolved from the first view.
- **Section 1, line 7.** plan.md:1 (PASS), plan.md:14 (732) and worst-work (every kind, incrementally) are all supported. "A tests every kind" is the proposer's reading and is fine.
- **Section 2, line 18.** PROJECT.md:108 and :112 are supported. Note that PROJECT.md:108 and the M2 line (PROJECT.md:57) still say "the same past tasks", while the plan tests new work. The case does not say whether the owner is asked to approve rewording them (the first view's finding 3, spec only).
- **Section 3, line 22.** reviews/E-001/reviewer.md:23 (plans) and :32 (built work) both say "go to the fallback". Neither covers research. e002-not-tested:12 says U2's fallback applies for every kind and would be the better cite.
- **Section 3, line 23.** e002-not-tested:1 and heldback-store:1 are supported. The "own sessions" half is at heldback-store:13. Resolved from the first view.
- **Section 4, line 27.**
  - plan.md:535, :253 and :255 say the numbers, but they sit in Round 5 and Round 3 of the old draft, which the owner replaced (plan-stop-2). The new draft's own statement is plan.md:583.
  - The lines do not say "one kind after another" or "together" for the two week ranges, or "built work only" for C (spec only).
- **Section 4, line 28.** PROJECT.md:115 ("100 test runs") and :117 ("about 300 runs") are supported.
- **Section 5, line 32.**
  - plan.md:34 is an old-draft finding that says "4 times in 5" is "true only if the limit never bites"; it does not give the figure.
  - critic.md:14 and :18 support "judge errs" and "not shown".
  - critic.md:17 contradicts the case's "1 in 2 if a judge errs" (see failure 2).
- **Section 5, lines 33 and 37.** plan.md:897 and :963, and reviews/44/reviewer.md:17, are supported.
- **Section 5, line 34.** plan.md:906 is supported for 243–487 only as the K5 column. plan.md:957 says the first-use checks are untested. Neither gives a baseline.
- **Section 5, line 35.** plan.md:935 says the start-commit field is under open question 5. It does not say "enter only once".
- **Section 5, line 36.** plan.md:913, :916 and :920 are supported as facts. "Accepted" is not supported (failure 3).
- **Section 6.** spend-ceiling:10 and PROJECT.md:116 support "waits for the reset" and "no cap on your time". plan.md:899 supports the wake-ups being outside the budget.
- **Section 7.** PROJECT.md:112 and :113 are supported. Line 48 is misapplied (failure 7).
- **Section 8, line 53.** critic.md:35 only names the terms card in a heading and does not show the owner agrees to it. reviews/44/reviewer.md:28 supports the owner's approval of the reading lists.
- **Section 8, line 54.** heldback-store:12 supports the private repository. "A word you choose" is at plan.md:960 only as "the canary file", so the owner choosing the word is spec only.
- **Section 8, line 55.** PROJECT.md:60 and :72 are the first lines of the two blocks of ten, so they are cited loosely. The standard-lines Critic PASS (reviews/P-001-standard-lines/critic.md) covers the reworded ones.
- **Section 8, line 56.** PROJECT.md:166 says "The owner is the user." The second half ("the proposal serves only as a record the check opens") is the owner's option B ruling, which the case does not cite. I read it only from the task brief.
- **Appendix, line 65.** design-gate-3-case.md:75 says the timeline printed no milestone lines for Discovery. The case applies it to the Build gate without a record. I could not run `v3_checks gates`, so I cannot confirm the empty block is what it printed.
- **Appendix table.**
  - Design-1 (plan.md:94) is Round 1's FAIL of the superseded draft. It says "AC1 is about files, not a scenario … The owner can still approve it", which does not establish the criteria were reviewed.
  - Design-2 (plan.md:93) is also Round 1. It asks to "Add the C2-no-spec case", and does not say the join sheets were mapped or reviewed.
  - Design-4 (plan.md:314) is in the old Round 4 join-up. It says "Mostly pass … These do not", and does not say every cited record was checked to exist.
  - Design-3 cites :957, which says the tools are untested, and the "reviewed" label is a stretch.
  - Design-5 (plan.md:939) and Design-6 (plan.md:1, :942) are supported. Better cites for the others are the new draft's rounds 2 and 3 (plan.md:837, :925).
- **Appendix lines 76–77.** The rulings and the first-view and standard-lines Critic records exist and say what is claimed.

**Milestones:**
- The fenced milestone block is still empty, and no project milestone is listed.
  - M2 (a fair test is ready, Design) is not shown with any status, sprint or reason.
  - M3 to M6 are Build milestones and need no sprint before this gate.
  - I cannot tell whether a merged pull request or research item exists for M2, so I cannot say whether its missing sprint is a finding. The case should state M2's standing.
  - The Design-gate ruling (design-gate:1) approved M1 to M6 as written.
- The six Design standard rows read as achievements, not tasks. Design-3 and Design-5 are "Not recorded by the model", which is never a finding and is not claimed reached. Design-6 is claimed reached, and the record supports that.
- The Build and Launch standard lines are "all taken on", with the reworded Build-1, Build-3 and Launch-5 PASSed. No Build or Launch standard milestone is claimed reached, which is correct. Nothing is claimed that the records do not hold.

**First view's findings, one by one.**
- **1, no scenario shown.** Resolved. The proposal holds all eleven, which I checked below.
- **2, budget options.** Partly resolved. The 300-run comparison is added, but B, C and D are bare counts (failure 1).
- **3, open questions not listed.** Not resolved. The case now says "the terms card" and gives it no content (failure 5).
- **4, headline limit.** Added, but misstated (failure 2).
- **5, risks carried.** Mostly resolved. All four items are present, plus the reading-list note. "Accepted" misdescribes them and the form's "what we would do / where it stands" is thin (failures 3 and 4).
- **6, rule-change ownership and set-up.** Partly resolved. The reading lists are in section 8 with the Reviewer PASS, but the environment check is missing (failure 6).
- **7, wording.** Partly resolved (failure 8).
- **Form.** Standard visuals are not resolved (failure 9). The kill-criteria omission is resolved, but the line is stale (failure 7).
- **Flowchart citations.** Resolved.
- **Citation items.**
  - Resolved: section 1 line 7, section 3 line 23 (plan-stop-2 claim removed), section 6, section 8 line 54, appendix line 76 and table row 6.
  - Partly: section 1 line 5, section 3 line 22 and appendix line 65.
  - Table rows 1, 2 and 4 now carry line numbers, but the lines do not say what is claimed.
- **Milestones.** Not resolved.

## The proposal's copy

I compared specs/S-001.md:250–260 to the proposal's eleven scenario lines, word for word, including the "AC<n> [trace: …] —" prefix and each clause through to the final full stop.

1. **The eleven scenarios are whole.** AC1 to AC11 in the proposal (lines 17–27) are each the full text of the spec's line 250 to 260 respectively. Each ends where the spec's does, and none is cut short. Each ends with the right `[specs/S-001.md:<line>]`, which is the form's own line citation.
2. **Form breach, Critic record cited.** `_PROPOSAL.md` bars citing any "case, Critic or User representative record or anything under decisions/". Proposal lines 7, 35 and 36 cite reviews/S-001/plan.md, which is the Critic's plan review. Sections 1 and 5 would need other records (the spec or PROJECT.md).
3. **Header line.** "Shown to the user representative, a simulation of the target user" is the form's fixed text. By the owner's ruling no user representative reads this proposal. The case (line 56) says so, but the line states otherwise. Flag it as inaccurate for this case. Delete it or add a note, depending on the form's rules.
4. **Section 1, line 7.** "Three candidate changes … written instructions" cites plan.md:22, an old-draft finding that merely mentions C1 to C3. It is true of the records (PROJECT.md:13 for instructions), but C2 changes the inputs a brief names and C3 changes a check's brief. "Written instructions" is a fair summary, not an exact one.
5. **Section 1, line 8.** "Kept only if it raises the share … at most 1 time in 40" is true of PROJECT.md:108. It omits that AC7 also requires the judge to be confirmed by the owner's cards, though "only if" keeps it true.
6. **Section 2, lines 12–13.** PROJECT.md:109 (V2) and :112 are supported. "Nothing in the operating model changes, and the record … still goes in" reads as self-contradictory. The brief-and-model record is a change to the operating model (PROJECT.md:90, :112). Reword to "no instruction changes".
7. **Section 5, line 38.** "AI usage within your existing plan" cites PROJECT.md:116, which is about the owner's time and tokens. The spend ceiling is at PROJECT.md:99 and spend-ceiling:1.
8. **Section 5, lines 35 and 37.** plan.md:960 says "the canary file" and open questions 5, 8 and 9. It does not say "a private repository" or that the owner chooses the word, and heldback-store:12 holds the repository half. plan.md:913 supports "about four short relays a kind" but not "Sessions to start … and short records to pass on". The weeks (60–121) and the owner-action counts, which are the time and effort the form asks for, are absent from section 5. They could be cited to the new-draft round 3 (plan.md:906) or to spec :17.
9. **Readability, not a copy fault.** AC4 and AC5 are long and use terms the proposal never defines (sheets repository, fingerprint, K4, locked checks). The owner ruled for the full text, so I do not fail the copy.
10. **Word count.** Sections 1, 2 and 5 are about 175 counted words, under the 200 cap.
11. **Screens.** Section 4 "No screens: …" is in the form. It carries no citation, but the form's screen line does not require one.

## The six-part contract

1. **What I changed:** nothing. I hold no write tool.
2. **Why:** to give the Build gate's second case its Critic section, check the eleven scenario lines against specs/S-001.md:250–260, and judge whether case 2 resolves the first view.
3. **What I verified:**
   - the case, the proposal, docs/gates/_GATE.md and _PROPOSAL.md, docs/PROJECT.md in full, and the first view;
   - every cited record at its cited lines: reviews/S-001/plan.md (lines 1–3, 14, 22, 34, 93–94, 250–257, 314, 535, 567–600, 895–964 and the heading map), reviews/P-001-build-gate/critic.md, reviews/44/reviewer.md, reviews/E-001/reviewer.md:1–33, reviews/P-001-standard-lines/critic.md, design-gate-3-case.md:68–80, and the rulings design-gate, worst-work, spend-ceiling, heldback-store, e002-not-tested, plan-stop-2 and gate-record;
   - specs/S-001.md lines 230–279, including the eleven criteria, word for word against the proposal;
   - the section 1 to 8 word count of about 342 (my own count).
4. **What is undone:**
   - I did not read the whole spec, E-003, or the whole of the 960-line plan review (I did not read lines 100–250 or 327–560, apart from the lines cited).
   - I did not run sizing.py or `v3_checks gates`.
   - I did not see the owner's option B ruling or the terms card, which are outside the pack. I took the ruling from the task brief.
   - I did not read the research section of reviews/E-001/reviewer.md.
   - Claims marked "spec only" rest on the spec alone.
5. **Needed outside my lane:**
   - The Chief of Staff, for the case:
     - Describe options B, C and D with cost and what each can show.
     - Fix the 1-in-2 wording and the "Accepted" label.
     - Name the terms card's questions, or say where the owner sees them.
     - Add the environment-check half of the owner's set-up.
     - Update the stale stop-rule line.
     - Cite the new draft's rounds for the Design standard rows.
     - State M2's standing and print the milestone block with `v3_checks gates`.
     - Add the standard visuals, or say why they do not apply.
   - The Chief of Staff, for the proposal: drop the Critic-record citations, fix the PROJECT.md:116 cite, and reword or remove the user-representative header line.
   - The owner: the budget, the terms card, the sheets repository and the set-up.
6. **Open questions:**
   - Is the "Shown to the user representative" line meant to stay in a proposal the owner ruled no user representative reads?
   - Does the terms card now have a passing Critic round? The pack holds only the round-1 FAIL.

Files: /home/user/ml-gate/docs/gates/P-001/build-gate-2-case.md, /home/user/ml-gate/docs/gates/P-001/build-gate-2-proposal.md, /home/user/ml-gate/specs/S-001.md, /home/user/ml-gate/reviews/S-001/plan.md, /home/user/ml-gate/reviews/P-001/_build-gate-1-critic.md, /home/user/ml-gate/docs/PROJECT.md
