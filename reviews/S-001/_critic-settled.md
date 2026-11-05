Verdict: PASS

*The Critic on S-001 and E-003 as settled with the Build-gate rulings, before the freeze lands. Brief 69 (docs/briefs/69-critic.md) for round 1 and brief 71 (docs/briefs/71-critic.md) for round 2; each a fresh session on a different model from the settled text's writer. Recorded verbatim by the Orchestrator, 2026-11-04. The first line is the latest round's verdict; round 1's was FAIL. In round 2's contract, item 3's word "Verdict", which the return followed with a colon, is written "(Verdict)". The Orchestrator compared the two copies byte for byte after round 2 (`git diff 3edcc54 9fd48c9`): only the lines the Definer reported differ.*

## Round 1 (commit 3edcc54)

The settled text carries every ruling as the owner gave it. One defect is blocking: four evidence pointers to docs/PROJECT.md in S-001 are now wrong. Correct them before anything is locked.

Findings

1. BLOCKING. Four line pointers into docs/PROJECT.md in specs/S-001.md no longer point at what the spec says they do.
   - "Facts relied on" says V1 is at "docs/PROJECT.md:96". Line 96 is now the heading "## 5. Limits"; V1 is at :108. Ruling 1 in the same spec correctly cites :108.
   - It gives the starting figures and piece counts (plans 2 of 44 and so on) at ":99". Line 99 is now the spend-ceiling bullet; "2 of 44" is at :111. The same ":99" is cited in "How fast new work arrives" (Q-008 counts pieces ... docs/PROJECT.md:99).
   - It gives the "different provider needs the owner's override" fact at ":147". Line 147 is now blank or risk text; the override wording is at :99 and :159.
   - The same pointers are in the text before the freeze (480fb62), so the freeze did not introduce them. PROJECT.md moved when the Chief of Staff carried out term 1, and the settled text updated only the ruling-1 and ruling-2 pointers (:108, :57). A frozen spec cannot be corrected later. Fix: change :96 to :108, and :99 to :111 where it cites the counts and starting figures (two places). For the override fact, change :147 to :99 (or :159, which also mentions it).

2. Non-blocking. Two spots still read as if the per-task packs are pending.
   - S-001's "The Reviewer's reach" says the pack is one "which the Chief of Staff adds to governance/PACKS.toml (Needed outside)".
   - E-003's "Who does what" (Reviewer entry) says "which the Chief of Staff adds to governance/PACKS.toml".
   - Both entries are in place: PACKS.toml lines 103-131 hold `[roles.S-001-holdout]` and `[roles.S-001-analysis]`, and reviews/44/owner.md reads "Verdict: PASS".
   - The settled "Two Check author jobs" paragraph says "so it is in place". The wording is a loose end, not a contradiction of a ruling. "Facts relied on" keeps "starting state ... `[roles.S-001-analysis]` does not exist". That is labelled as the starting state and stays true as history.

3. Non-blocking. S-001's "How fast new work arrives" still says "as run for this draft" for output.txt. The spec is now frozen, so the word is stale.

4. Non-blocking. The freeze added line-level evidence tags to "Facts relied on", which no ruling required.
   - Verified true: Q-008-memo.md:367 (§4 heading), :481 (Tallies heading), output.txt:38 ("critical n10 ... 9 12 15"), and design-environment-check.md:16 ("Judge models").
   - Not verifiable here, because the portfolio library is not in any copy: Q-003-F-i.md:11, Q-002-F-h.md:10, Q-003-F-f.md:10, Q-002-F-g.md:10, Q-002-F-c.md:10 and Q-003-F-c.md:10.
   - They change no figure or method step.

5. Non-blocking. E-003 Exclusions 6 ("Not eligible at entry") does not list a piece from a private repository, which Step 2 now excludes by term 7. Step 2 is explicit and governs, so nothing is lost.

Check 1: each changed sentence against the rulings and records

- The twelve points below are true of the cards as asked (2350130) and the answer records. None says more or less than the owner ruled.
  - Rulings 1 and 2: the V1 text equals PROJECT.md:108 and the proposed text in the plan's questions 1 and 2. M2's "done when" equals PROJECT.md:57. "Stands once the Critic has checked it" matches the carry-out line, and the 300-runs line was restated (PROJECT.md:157).
  - Ruling 3: size A, 732 runs, about 132 million tokens; research tested last (term 3 A); no fixed limit with review points at 16 weeks and each token checkpoint (term 8).
  - Ruling 4: one kind after another, no overlap, not all collecting from the start. The owner answered "All as recommended", not "A with overlap", so this stands.
  - Ruling 5: the Service Desk and Model-Lab take part; the Chief of Staff records brief, start and model at hand-out until M3; Model-Lab's brief records gain `start:` (term 9). The packs are approved by the owner's verdict and merge on PR #44 (term 4); owner.md and PACKS.toml bear this out.
  - Ruling 6: the judges stay within the owner's AI plan, on Fable 5.1.
  - Ruling 7: false-pass tolerance is the unchanged check's plus one (term 10).
  - Ruling 8: one judging session per kind, each judge a helper inside it (term 6); the owner's part and fallbacks accepted (term 11).
  - Ruling 9: only public repositories' pieces enter (term 7). The headline weeks do not change, and the bracketed figures overstate and are not recomputed. This matches the card's "headline weeks do not change".
- Ruling numbers match the question numbers, and all nine questions are covered by terms 1 to 11.
- The statement in "What the test can and cannot show" that research is tested, last, "with this stated" is a fair reading of term 3, whose card text states the "not shown" likelihood.

Check 2: acceptance criteria, joins, figures and method steps

- AC1 to AC11, J1 to J8, every table figure, and the method and sizing text are unchanged between the two copies, as far as I read side by side. The old and new J-lines and the K1 to K7 text are identical.
- What did change beyond wording:
  - E-003 Order is now fixed as no overlap and not all collecting from the start (ruling 4).
  - E-003 Step 2 gains the public-repository condition (term 7) and the `start:` qualification of the Chief of Staff's records (term 9).
  - E-003 "Pairs per kind" is now 60, and the "Kept" rationale and the review-point text are settled to the terms.
  - S-001's "What the sheet session holds" now reads "if it runs while an earlier kind is still being judged". It used to say "if the owner lets kinds overlap". This is still true under no overlap, because the next kind's sheet is written before that kind opens. It is a consequence of ruling 4, not a new design step.
  - "Areas touched" drops "If the owner declines that change, AC4 cannot be met"; the owner approved the packs.

Check 3: lines that still offer a ruled choice or call a ruled matter open

- None found. No "open question" references remain apart from the heading "The owner's rulings on the open questions" and the intended mention in the "Needed outside" section ("open questions 5, 8 and 9 were answered at the Build gate").
- The remaining owner choices are the future ones the cards left in place: the K1, K3, K4, K5 and K7 failures, review-point "go on" or "stop", and options B, C and D shown in the table as unchosen. Option A is marked "(recommended; ruled)".

Check 4: consistency with the rest of S-001 and E-003, and with PROJECT.md V1 and M2

- The V1 and M2 text, the 60 pairs, the 732 runs and 132 million tokens, the order, and the review points agree across S-001, E-003 and PROJECT.md. The pointer defect is finding 1.

Check 5: freeze lines

- S-001 line 3 reads `status: frozen   frozen_at: 75ad74fba46688ccc1d7c0b53875ad9ce03f222e`.
- The brief reads `spec: specs/S-001.md (frozen @ 75ad74fba46688ccc1d7c0b53875ad9ce03f222e)`.
- E-003 line 132 reads `frozen: 75ad74fba46688ccc1d7c0b53875ad9ce03f222e`.
- All three agree and name the settled-text commit (75ad74f), not the freeze commit (3edcc54). E-001's line is a bare `frozen:` followed by one full 40-hex commit (4e2cb12cf6e12244a1d22e88dca56f79f9decbe8), also on E-002. The form matches.
- I cannot confirm from a copy without git history that 4e2cb12 played the same "settled-text commit" role for E-001. The form and placement are identical.

Six-part contract

1. Task: check the Definer's settled and frozen S-001 and E-003 (3edcc54) against the ruling cards, the answer records and E-001's freeze form, comparing with 480fb62.
2. Result: FAIL, on the one blocking finding (four stale PROJECT.md line pointers in S-001). Every ruling is carried as given. Nothing else is blocking.
3. Evidence:
   - Files read: specs/S-001.md and experiments/E-003.md in fix-freeze and fix-terms; decisions/questions/P-001-build-gate.md and P-001-build-gate-terms.md; both cards in fix-cards; docs/PROJECT.md lines 55-58, 94-110 and 145-148; reviews/44/owner.md; governance/PACKS.toml lines 103-131; experiments/E-001.md, E-002.md and E-003.md freeze lines; research/Q-008-memo.md lines 365-368 and 479-482; experiments/E-003/output.txt line 38; docs/reports/2026-11-03-design-environment-check.md line 16.
   - Search results: PROJECT.md "past tasks" (lines 31, 129, 134, 141, 153, 158) and "300 runs".
4. Not done: no shell and no git history, so I could not diff mechanically. I compared the two copies by reading. I did not read the portfolio library, the Service Desk records, or the unchanged remainder of PROJECT.md. I did not judge whether the Critic has yet checked the reworded M2 line, which the spec says only "stands once" checked.
5. Risks: if the pointers go into the freeze uncorrected, the evidence trail for V1, the counts and the override rule points at the wrong lines for the life of the spec. Items 2 to 5 are wording only.
6. Next: the Definer corrects the pointers in finding 1 (and, if wished, items 2, 3 and 5), then re-sets the three freeze lines to the new settled commit, since correcting the pointers changes the text the commit names. The Critic should check that correction.

Files: /tmp/claude-0/-home-user/a9cd8a0a-147c-550f-94b8-72427d1045fd/scratchpad/fix-freeze/specs/S-001.md (lines 71, 281, 282, 285 for finding 1; line 234 and line 70 for items 2 and 3) and /tmp/claude-0/-home-user/a9cd8a0a-147c-550f-94b8-72427d1045fd/scratchpad/fix-freeze/experiments/E-003.md (line 18).

## Round 2 (commit 9fd48c9)

Round 2 of the Critic's check of the settled S-001 and E-003. I found no blocking finding.

Findings:

1. Not blocking. The four line pointers (round 1, finding 1) now name the right PROJECT.md lines. I read docs/PROJECT.md in the fix-freeze2 copy for each one.
   - S-001 line 71, "plans 44, built work 80, research 19; docs/PROJECT.md:111". Line 111 is the "Starting figures" bullet with plans 2 of 44, research 5 of 19 and built work 32 of 80.
   - S-001 line 281, "plans 2 of 44, research 5 of 19, built work 32 of 80". Line 111 holds exactly these figures.
   - S-001 line 282, the V1 20-point gain kept at 1 in 40. PROJECT.md:108 is V1. Ruling 1 on line 335 already cited :108.
   - S-001 line 285, "A different provider needs the owner's override". PROJECT.md:99 is the spend ceiling in section 5, which allows an override "in their own words at the time". PROJECT.md:159 is the section 8 constraint that says the same.
   - Every `PROJECT.md:<n>` pointer left in either file is now correct. The remaining ones are line 335 (:108) and line 336 (:57, the M2 line).

2. Not blocking. Item 2, the Reviewer's-reach lines, now state a ruling already in the text. The two lines are S-001 234 and E-003 18. Both change "which the Chief of Staff adds" to "added ... with the owner's approval (reviews/44/owner.md; ruling 5 ...)". S-001 lines 205, 275, 339 and 350 already say the owner approved both per-task packs by verdict and merge on PR 44. reviews/44/owner.md exists and reads `Verdict: PASS`. This adds no new claim.

3. Not blocking. Item 3, S-001 line 70, now says the output was "as run for S-001's round-3 draft on 2026-11-04". The first line of experiments/E-003/output.txt says the same ("as run for S-001's round-3 draft on 2026-11-04"). This removes the stale "this draft" and adds no new claim.

4. Not blocking. Item 5, E-003 line 118 (Exclusions 6), gains "the piece is from a repository that is not public". Step 2 (E-003 line 45) and ruling 9 already require a public repository. This only makes the exclusions list match the entry rule. It adds no new claim.

5. Not blocking. The three freeze lines agree. S-001 line 3 and S-001 line 365 both read `f4298cdf19a5abf17e34d7979846252819c2b14b`, and so does E-003 line 132. In fix-freeze all three read `75ad74fba46688ccc1d7c0b53875ad9ce03f222e`. The old hash is gone from fix-freeze2.

6. Not blocking. I found no other change between the two copies. I read both copies of S-001 (367 lines against 367) and E-003 (132 lines against 132) in full and compared them by reading. The only differing lines I found are the ones the Definer reported. I have no shell, so this is a reading comparison, not a byte diff. One small tidy-up, for the next revision only. S-001 lines 293 and 352 still say `[roles.S-001-analysis]` "does not exist" or is "added (it is not in the file)". These describe the starting state, and line 293 labels it as such, so the text is not wrong or in conflict. Nothing here needs changing now.

The six-part contract:

1. **Task.** Check that the Definer's fix for round 1 is correct and complete. That means the four PROJECT.md pointers, the stale-claim edits, anything else changed between the two copies, and the three freeze lines.
2. **What I did.** I read S-001 and E-003 in full in both copies and compared them. I checked each pointer against docs/PROJECT.md in fix-freeze2 (lines 57, 99, 108, 111, 159). I grepped both files for every remaining `PROJECT.md:<n>` pointer. I read reviews/44/owner.md and the first line of experiments/E-003/output.txt.
3. **Result.** (Verdict) PASS. Findings 1 to 6 are all non-blocking, and all of them confirm the fix.
4. **Evidence.** The files and lines are quoted in findings 1 to 5. The copies are `/tmp/claude-0/-home-user/a9cd8a0a-147c-550f-94b8-72427d1045fd/scratchpad/fix-freeze/` (round 1) and `/tmp/claude-0/-home-user/a9cd8a0a-147c-550f-94b8-72427d1045fd/scratchpad/fix-freeze2/` (new), each with specs/S-001.md and experiments/E-003.md. The pointers were checked against fix-freeze2/docs/PROJECT.md.
5. **Limits and risks.** The comparison between the copies was by reading, not a byte diff. The values in output.txt were not re-run. I did not re-check that each ruling was carried as the owner gave it, because round 1 found that and nothing in these changes touches it.
6. **Self-implication and next step.** Nothing here implicates my own round 1 check. Round 1 had already named the pointers in finding 1 and items 2, 3 and 5, and this round only confirms they were fixed. The settled S-001 and E-003, with the freeze at `f4298cdf19a5abf17e34d7979846252819c2b14b`, are fit to be recorded as settled.
