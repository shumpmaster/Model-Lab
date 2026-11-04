Verdict: FAIL

*The Critic on S-001 and E-003 as settled with the Build-gate rulings, before the freeze lands. Brief 69 (docs/briefs/69-critic.md); a fresh session on a different model from the settled text's writer. Recorded verbatim by the Orchestrator, 2026-11-04. The first line is the latest round's verdict.*

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
