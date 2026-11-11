Verdict: PASS

*The Critic on questions/P-002-trial-gates.md, the question on the owner's two approvals for each screened method (P-002): round 1 (FAIL), round 2 (FAIL), round 3 (PASS); briefs 241, 242 and 243. Each round a fresh session on a different model from the card's writer, started by the Chief of Staff (session_01QBwHGKirN166RhxQTHuAt9), 2026-11-10. Recorded verbatim by the Orchestrator from the helper's return; the round's own verdict line is recorded as "The round's verdict was …" (LL-68). The verdict above is the latest round's. After round 3, its findings 1, 2, 3, 4, 5, 6, 8 and 9 were applied as wording; finding 7 (plainness) stays open.*

## Round 1 (brief 241)

The round's verdict was FAIL.

Card checked: /home/user/ml-critic-241/questions/P-002-trial-gates.md, round 1, read cold. Two findings are blocking and twelve are non-blocking. I hold no command tool, so I ran nothing; figures were checked against the printed output in the odds record. Every Context source was opened.

Self-implication flag (D-050): the Critic passed the value-target card at round 3. Finding 4 below touches wording that card also carried (its part 3 option B, "may come back only with a trial plan that is truly different") and that no earlier round questioned.

## What holds

- **Figures (lines 14, 17, 19, 31).** All match /home/user/ml-critic-241/intake/P-002-value-target-odds-2026-11-10.md at the 1 in 10 line, with fair rounding.

  | Card says | Output |
  |---|---|
  | one look, about 7 and 4 in 10 | 0.71, 0.42 |
  | two looks, about 9 and 7 in 10 | 0.92, 0.70 |
  | about 3 to 5 trials in 10 go on | 0.27 to 0.48 for a real halving (0.38 to 0.39 for no effect) |
  | hold-up checks turn away a harmless method 1 in 7 to 1 in 5 | 0.145 (round 2), up to 0.20 (round 3) |

- **Quotes.** Lines 5 and 7 match the owner's words in /home/user/ml-critic-241/intake/P-002-owner-value-target-answers-2026-11-10.md, each starting mid-sentence after "I think". The desk quote on line 11 matches answer 5 of /home/user/ml-critic-241/decisions/questions/P-002-groundwork-shortlist.md; "no data out" matches answer 6.
- **Sources.** R9, R16 and R18 exist as described in /home/user/ml-critic-241/docs/projects/P-002.md section 7. "No re-running for a better answer" is in the experiment playbook as cited.
- **Form.** Template fields, the Milestone line and Context are present. No default and no timeout is right for a value target. The opening names B's departure first and holds no paths or ids (LL-08, S-026). The recommendation gives its confidence and what would change it.

## Blocking

1. **Lines 9, 12, 17 and 21: the card calls A "your design", but A narrows the owner's second approval, and the owner's stated worry is left out.**
   - The owner's words are that results come "à la the gate of which I approve or reject the final implementation to the model". Nothing in them limits approval to results that cleared the line.
   - Under A and C, on a "not shown" result "you may not adopt it on that result". The owner can only reject or order another trial, so the trial's line still decides, not the owner.
   - Line 14 says "many useful methods will come back 'not shown'". So the narrowing applies to a large share of results.
   - The owner's reason for the gate was "An automated pipeline could end up killing a lot." The card omits that sentence. Line 12's "Nothing is dropped by the pipeline" answers it only in form under A and C.
   - Line 21 gives "It is your design" as a reason for A. The two cards sit under every option, so this does not distinguish A; B gives the owner's approval more force than A does.
   - No option offers the plain reading of the owner's words: approving a "not shown" method into the model. B stops at "use in this project". The card does not say that reading exists or why it is not offered.
   - This is LL-08's cause in a new form: the owner's words read to fit the recommendation.

2. **Lines 5 and 18: the first line says B goes outside two rules, but the card only shows how it breaks one.**
   - Line 5 says B would go outside "Killed, not tuned" and "No re-running for a better answer".
   - Line 18's cost names only "Killed, not tuned". Nothing on the card says how B is a re-run.
   - If the "review after its next 30 pieces" is the re-run, the card should say so; if it is not, the first line overstates B's departure and leans against it.
   - The gloss on line 5 ("a change that misses its pre-set mark is removed, not kept or adjusted") is not at the cited place. OPERATING_MODEL.md §1 item 4 reads only "Unchanged. A test that was itself wrong is not a strike". The rule's words are in /home/user/Personal-Org-Operating-Model/docs/archive/OPERATING_MODEL_v2.5.1.md line 33: "A design that fails its predeclared gate dies. It may be replaced by a genuinely different design (§5), never adjusted until it passes."
   - The gloss is a fair paraphrase, but LL-08 asks for the rule quoted, and Context line 32 cites a place that does not hold it.

## Non-blocking

3. **Lines 10 and 11: several items under "as you described" are the writer's additions.**
   - The owner did not describe "the trial's plan, fixed from then on", "the Critic's view, and a recommendation", or the list in brackets on line 10.
   - Each is reasonable, and the frozen plan is the playbook's rule. They should be marked as added, not as the owner's.

4. **Lines 5, 17 and 19: "A and C stay inside them" is not fully shown for the new trial after a "not shown" result.**
   - The playbook's "new, genuinely different registration" clause sits under "When the test itself was wrong". For a sound trial it says "Null results are results. No re-running for a better answer."
   - v2.5.1's rule allows replacing a failed design with "a genuinely different design", not re-testing the same one.
   - The card sets no limit on fresh trials of one method, though the playbook says "repeated reframing goes back to Discovery".
   - It does not say who checks that a new trial is "truly different"; that check is the Critic's (D-047).

5. **Line 17: the card does not say why the planned second look is not a re-run.** The earlier card did ("one trial planned whole before it starts"). "Leans the right way" is also undefined here.

6. **Lines 17 and 21: "the most useful methods found" is equally true of B.** B is "As A", so its odds are the same 9 and 7 in 10. Two of A's three reasons on line 21 do not separate it from B.

7. **Line 18: B does not say what happens at the review after the next 30 pieces.** The earlier card's version said "removed if it still shows nothing". Without it, B reads as weaker than it was and its way back is unclear.

8. **Lines 17 to 19 and 23: reversibility is given once for the card, not per option (D-019).** For B in particular, the card does not say whether a method adopted on faith can be removed.

9. **Lines 14 and 18: a trial whose gain cleared the line but whose hold-up checks failed is covered by no option.**
   - "Not shown" is defined only as the gain not clearing the line.
   - A harmless method fails the hold-up checks by chance 1 time in 7 to 1 in 5. The card does not say whether the owner may adopt such a method.

10. **Line 26: the proposals on the owner's time understate the load and leave gaps.**
    - "Two cards per method" does not hold under A's fresh trial, which adds an entry card and a results card.
    - The card does not say whether a second look adds another 5 short reads.
    - The cap of 3 covers entry cards only. Results cards are uncapped, and the card does not say what happens to a fourth method.
    - The card gives no sense of how many methods the screening may bring, though one-source entry lets more in.
    - R18's plan says "the owner's hours are counted with the spend"; the card does not carry that.
    - The figure 3 and "two weeks" have no source; they are rightly labelled as proposals.

11. **Line 22: the check record named does not exist yet, and the caveat on the odds is dropped.** The earlier card said the figures are the Chief of Staff's own and that no one else has run the scripts. This card reuses them without saying so.

12. **Line 18 and Context line 34: B's "risk of adopting what is popular rather than what helps" is R1.** Context lists R9, R16 and R18 only.

13. **Line 14: the hold-up range mixes two cases.** 1 in 7 is the one-look figure and 1 in 5 the two-look upper bound. A's "about 9 and 7 in 10" on line 17 is repeated without "before the hold-up checks".

14. **Plainness on a phone.**
    - Lines 5, 10 and 14 each run to about 90 to 110 words; line 14 carries eight figures.
    - "About 9 and 7 in 10" makes the reader hold the two starting shares in mind.
    - "Pieces", "your touches", "the 5 short reads" and "the checks that work holds up" are defined only on the earlier card.
    - The letters have changed meaning: the earlier part 3's B was "drop at once" and C "keep on promise"; here B is "adopt on faith" and C "one look only". An owner who read both today could mix them up.

## Files read

- /home/user/ml-critic-241/questions/P-002-trial-gates.md
- /home/user/ml-critic-241/questions/P-002-value-target.md
- /home/user/ml-critic-241/questions/_TEMPLATE.md
- /home/user/ml-critic-241/reviews/P-002-value-target/critic.md
- /home/user/ml-critic-241/intake/P-002-owner-value-target-answers-2026-11-10.md
- /home/user/ml-critic-241/intake/P-002-value-target-odds-2026-11-10.md
- /home/user/ml-critic-241/decisions/questions/P-002-groundwork-shortlist.md
- /home/user/ml-critic-241/decisions/questions/P-002-target.md (searched for the owner's "faith" words)
- /home/user/ml-critic-241/docs/projects/P-002.md (section 7)
- /home/user/ml-critic-241/docs/LESSONS.md (LL-08)
- /home/user/ml-critic-241/AGENTS.md (§5)
- /home/user/Personal-Org-Operating-Model/OPERATING_MODEL.md (§1, §2, definition of ready, experiment playbook)
- /home/user/Personal-Org-Operating-Model/docs/archive/OPERATING_MODEL_v2.5.1.md (line 33, by search)

## Round 2 (brief 242)

The round's verdict was FAIL.

Card checked: /home/user/ml-critic-242/questions/P-002-trial-gates.md, round 2, read cold. Two findings are blocking and eleven are non-blocking; both blocking ones sit in the recommended option B and its recommendation. I hold no command tool, so I ran nothing; figures were checked against the printed output in the odds record. Every Context source was opened.

Self-implication flag (D-050): round 1 of this card and round 3 of the value-target card were Critic checks.
- Finding 1 below concerns B's "reviewed after its next 30 pieces", wording the value-target card's part 3 option C also carried and which passed at round 3 without its relation to "No re-running" being asked.
- Round 1 raised that relation only conditionally (its finding 2) and asked for the removal clause to be restored (its finding 7).
- Finding 5 below repeats round 1's finding 4, which also touches wording the value-target card carried.

## What holds

- **The owner's design.**
  - Lines 5 and 7 quote the owner word for word from /home/user/ml-critic-242/intake/P-002-owner-value-target-answers-2026-11-10.md, now including the reason ("An automated pipeline could end up killing a lot...").
  - Option A is the plain reading of "approve or reject the final implementation to the model", put first, with its cost stated fairly.
  - The writer's additions on lines 12 and 13 are marked "Added". LL-76's correction is met for the options.
- **"Killed, not tuned".**
  - Line 5 quotes it exactly from /home/user/Personal-Org-Operating-Model/docs/archive/OPERATING_MODEL_v2.5.1.md line 33.
  - Context line 41 cites that place, and correctly says OPERATING_MODEL.md §1 item 4 keeps it "Unchanged".
  - The first line names A and B as departures, and the recommended option is one of them (LL-08).
- **Figures.** All match /home/user/ml-critic-242/intake/P-002-value-target-odds-2026-11-10.md at the 1 in 10 line, with fair rounding.

  | Card says | Output |
  |---|---|
  | one look, about 7 and 4 in 10 | 0.71, 0.42 |
  | two looks, about 9 and 7 in 10 | 0.92, 0.70 |
  | line "slightly stricter" | 0.097 at each look |
  | about 3 to 5 trials in 10 run twice as long | 0.27 to 0.48 for a real halving (0.38 to 0.39 for no effect) |
  | harmless method turned away 1 in 7 with one look, up to 1 in 5 with two | 0.145 (round 2); up to 0.20 (round 3) |

- **Sources.**
  - R1, R9, R16 and R18 are in /home/user/ml-critic-242/docs/projects/P-002.md section 7 as described; R1 is the first risk.
  - The desk line matches answer 5 of /home/user/ml-critic-242/decisions/questions/P-002-groundwork-shortlist.md.
  - "No re-running for a better answer" and "repeated reframing goes back to Discovery" are in the experiment playbook.
  - The owner chose "1 in 10 (catch more)", as line 9 says.
- **Form.** Template fields, the Milestone line and Context are present. No default and no timeout is right for a value target. Reversibility is given per option.

## Round 1 findings

| # | Round 1 finding | Status |
|---|---|---|
| 1 | A called "your design" but narrowed it; the owner's reason left out (blocking) | Answered in the options. The same fault returns in the recommendation: finding 2 below. |
| 2 | First line named two rules for B, showed one; rule glossed and miscited (blocking) | Answered in form: one rule named, quoted exactly, cited where its words are. The second rule's relation to B is now simply unsaid: finding 1 below. |
| 3 | Writer's additions under "as you described" | Answered. |
| 4 | "Inside the rules" not shown for a fresh trial after "not shown" | Partly. A limit and the Critic's check were added; the core point stands: finding 5 below. |
| 5 | Why the second look is not a re-run; "leans the right way" | Answered (lines 16 and 21). |
| 6 | "Most useful methods found" equally true of B | Answered; the reason is gone. |
| 7 | What happens at B's review | Answered in words ("removed then if it still is not shown"); what the review tests is still undefined: finding 1 below. |
| 8 | Reversibility per option | Answered. |
| 9 | Shown but did not hold up, covered by no option | Answered by line 24, which opens a new gap under B: finding 1 below. |
| 10 | Proposals on the owner's time | Mostly answered: fresh-design cards, second-look reads, a cap on both kinds, the queue, the unknown number and the hours are all there. Left over: finding 7 below. |
| 11 | Check record missing; odds caveat dropped | Answered; one residue in finding 10 below. |
| 12 | R1 missing from Context | Answered. |
| 13 | Hold-up range mixed two cases | Answered. |
| 14 | Plainness on a phone | Partly: words are defined and the letters are flagged; long lines remain: finding 11 below. |

## Blocking

1. **Lines 5, 20 and 24: the recommended option's relation to the two rules is not stated accurately.**
   - **The review reads as a re-run.**
     - Line 20: a "not shown" method is "reviewed after its next 30 pieces and removed then if it still is not shown", and "enters the operating model only once a trial shows it".
     - Read plainly, the same method is tested again after a null result, and a pass opens the way into the model.
     - The playbook says "Null results are results. No re-running for a better answer."
     - The card explains why C's second look is not a re-run (line 21) but says nothing either way for B's review. Line 5 names only "Killed, not tuned".
     - Round 1's finding 2 asked for exactly this: "If the 'review after its next 30 pieces' is the re-run, the card should say so".
   - **The review is not defined.**
     - "Shown" (line 9) needs 30 pieces with the method and 30 without, by coin toss. The card does not say what the "next 30 pieces" are compared with, or how a method "in use" still has "without" pieces.
     - It does not say whether a pass at the review counts as "a trial shows it".
     - The odds record holds no figure for this extra look. The stricter line (0.097) was set for two looks only, so a useless method gets one more chance than the 1 in 10 the owner chose.
   - **Line 24 gives B a departure at the model level that its cost omits.**
     - Under B the owner decides on a method that was shown but did not hold up, and B's own rule lets a shown method into the model.
     - The value-target card's part 2 says a method is kept when the gain clears the line "and the work holds up". So a method that failed that gate could enter the model under B.
     - Line 20's cost says only "the same departure as A within this project", and line 26 says under B "the model stays something that can be trusted".
   - **Why it blocks:** LL-08 asks that a recommended departure be stated in the first line; the task asks for each option's relation to both rules to be accurate. For the recommended option it is not.

2. **Line 26 (and line 20's title): the recommendation says B "gives your approval the last word on every result, which is what you asked for". It does not.**
   - The owner's words are "approve or reject the final implementation to the model". Under B, the owner's approval cannot put a "not shown" method into the model, which is the thing they named.
   - B lets the owner approve only "a 'not shown' result that held up". A result that was not shown and did not hold up is covered by no line of B.
   - At B's review the method is "removed then if it still is not shown", with no approval.
   - The second half of the sentence does disclose the model limit, and A is offered. But "what you asked for" is attached to the narrower option, in the line most read on a phone.
   - This is LL-76's own case in a milder form: there, the recommended option was called "your design" though it "barred the owner from adopting any method a trial did not show".
   - B's title, "You decide every result", carries the same overstatement.

## Non-blocking

3. **Lines 19 to 22: the card does not say whether A and B use one look or two.**
   - C says the second look is on the entry card; D says one look only. A and B say neither.
   - The cost "about 3 to 5 trials in 10 run twice as long" is charged to C alone. If A and B also take the second look, that leans against C; if they do not, their odds are the lower 7 and 4 in 10 and the card does not say so.

4. **Line 5: the card does not say what going outside the rule does to the rule.**
   - The value-target card said its lighter standard "also sends the standard to the model as a proposal".
   - Here, under A, methods enter the operating model, which every project uses. The card does not say whether choosing A or B is an exception for this project or a proposed change to the model.
   - Rule changes are the owner's (§2), so the owner may choose it; they should know which they are choosing.

5. **Line 21: "stays inside the rules" is still not fully shown for C's fresh trial design** (round 1 finding 4).
   - The playbook's "new, genuinely different registration" sits under "When the test itself was wrong". For a sound trial it says null results are results.
   - The archived rule lets a failed design be "replaced by a genuinely different design"; C keeps the same method and changes only the trial.
   - The added limit (fails twice, goes back) and the Critic's check narrow the gap but do not close it. D inherits it through "As C".

6. **Line 9: two definitions are loose.**
   - "Not shown is any other result" can be read as "other than shown" or "other than shown and holding up". Lines 20 and 24 use the first; the card should not leave it to inference.
   - "Holds up when its work does no worse" drops "by more than chance at 1 in 10" from the value-target card's definition. With it gone, line 16's "turn away a harmless method about 1 time in 7" has no stated cause.
   - "Chosen by coin toss" is the odds record's wording; the value-target card says "shuffled draws so each side gets 30". Harmless, but the two differ.

7. **Lines 32 to 35: what is left on the owner's time.**
   - B's review after the next 30 pieces is not counted. It is presumably a third card, and possibly 5 more reads.
   - No estimate of time per card or per read is given. Counting cards in place of hours is said honestly, but R18's plan was "the owner's hours are counted with the spend".
   - The cap of 3 and the two-week promise can collide: a results card held in the queue may pass two weeks. The card does not say which gives way.
   - The figures 3 and "two weeks" have no source; they are rightly labelled proposals.

8. **Line 19: A's way back rests on a review date the owner has not ruled.** "Comes out by a model change, at its review date" relies on the six-month review date, which was a proposal on the value-target card. The owner's recorded answers cover parts 1 to 4 only.

9. **D-019 form.**
   - The card has four options against "2–3". D is a variant of C, so the load is small.
   - It does not say what waits while the question is unruled. The value-target card did: "the plan cannot say how a method is tried and kept, and the brief cannot go to you for the Design gate". The template's WHY asks for "the cost of leaving it unruled".

10. **Line 27: "the Critic ... from its first round" does not give that round's outcome.**
    - Round 1 failed the card. The line reads as a clean check.
    - The value-target card's note that "an independent run is proposed before the Design gate" is dropped.

11. **Plainness on a phone.**
    - Line 5 runs to about 105 words, line 16 to about 120 with eight figures, and line 19 to about 95.
    - "About 9 in 10 and 7 in 10" and D's "about 7 and 4 in 10, against 9 and 7" make the reader carry the two starting shares; D also drops "before the hold-up checks".
    - "One-source entry" (lines 12 and 19) is not explained on this card.
    - "The 5 short reads of unlabelled pieces" is clearer than before, but why the owner reads them is said only on the earlier card.

12. **Line 14: "Nothing is dropped by the pipeline" holds only in form under C and D.** There, on a "not shown" result the owner may only reject or order one new design, so the trial's line still decides. C's cost says so plainly ("your approval cannot keep a 'not shown' method"), which is why this does not block.

13. **Context line 39 cites a question file that is due to be deleted.** questions/P-002-value-target.md goes when its answer record lands (AGENTS.md §5); the definitions this card relies on would then have no live source.

## Files read

- /home/user/ml-critic-242/questions/P-002-trial-gates.md
- /home/user/ml-critic-242/reviews/P-002-trial-gates/critic.md
- /home/user/ml-critic-242/questions/P-002-value-target.md
- /home/user/ml-critic-242/reviews/P-002-value-target/critic.md (round 3)
- /home/user/ml-critic-242/intake/P-002-owner-value-target-answers-2026-11-10.md
- /home/user/ml-critic-242/intake/P-002-value-target-odds-2026-11-10.md
- /home/user/ml-critic-242/questions/_TEMPLATE.md
- /home/user/ml-critic-242/decisions/questions/P-002-groundwork-shortlist.md
- /home/user/ml-critic-242/docs/projects/P-002.md (section 7)
- /home/user/ml-critic-242/docs/LESSONS.md (LL-08, LL-76)
- /home/user/ml-critic-242/AGENTS.md (§5)
- /home/user/Personal-Org-Operating-Model/OPERATING_MODEL.md (§1, §2, the experiment playbook)
- /home/user/Personal-Org-Operating-Model/docs/archive/OPERATING_MODEL_v2.5.1.md (line 33)

## Round 3 (brief 243)

The round's verdict was PASS.

Card checked: /home/user/ml-critic-243/questions/P-002-trial-gates.md, round 3, read cold. No finding blocks; nine are non-blocking, and findings 1 and 2 are the ones most worth fixing before the card is put. I hold no command tool, so I ran nothing; figures were checked against the printed output in the odds record. Every Context source was opened; one citation (the commit id on line 45) I could not confirm.

Self-implication flag (D-050): rounds 1 and 2 of this card and round 3 of the value-target card were Critic checks. Finding 2 below repeats round 1's finding 4 and round 2's finding 5, and touches wording the value-target card also carried ("may come back only with a trial plan that is truly different") and passed with.

## What holds

- **The owner's design.**
  - Lines 5 and 7 quote the owner word for word from /home/user/ml-critic-243/intake/P-002-owner-value-target-answers-2026-11-10.md, including the reason.
  - Option A is the plain reading of "approve or reject the final implementation to the model", put first, and the narrower options follow it (LL-76).
  - The writer's additions on lines 15 and 16 are marked "Added"; the time proposals are labelled proposals.
- **The rules.**
  - Line 5 quotes "Killed, not tuned" exactly from /home/user/Personal-Org-Operating-Model/docs/archive/OPERATING_MODEL_v2.5.1.md line 33; OPERATING_MODEL.md §1 item 4 does read "Unchanged".
  - The recommended option's departure is in the first sentence, with the rule quoted (LL-08).
  - Line 26 says why the planned second look is not a re-run.
  - "Sends that change to the model as a proposal, as your part 4 answer did" matches part 4 option A of the value-target card and /home/user/ml-critic-243/decisions/questions/P-002-target.md line 17.
- **Figures.** All match /home/user/ml-critic-243/intake/P-002-value-target-odds-2026-11-10.md at the 1 in 10 line, with fair rounding.

  | Card says | Output |
  |---|---|
  | one look, about 7 in 10 and 4 in 10 | 0.71, 0.42 |
  | two looks, about 9 in 10 and 7 in 10 | 0.92, 0.70 |
  | "slightly stricter line" | 0.097 at each look |
  | about 3 to 5 trials in 10 run twice as long | 0.27 to 0.48 for a real halving (0.38 to 0.39 for no effect) |
  | harmless method turned away about 1 in 7 with one look, up to 1 in 5 with two | 1 - 0.92 x 0.93 = 0.145 (round 2); up to 0.20 (round 3) |

- **Sources.**
  - R1, R9, R16 and R18 are in /home/user/ml-critic-243/docs/projects/P-002.md section 7 as described; R1 is the first risk.
  - The desk line matches answer 5 of /home/user/ml-critic-243/decisions/questions/P-002-groundwork-shortlist.md.
  - "Null results are results. No re-running for a better answer" and "repeated reframing goes back to Discovery" are in the experiment playbook; "Never delegable: … rule changes" is in §2.
  - The value-target Critic's round 3 does say it read the scripts and re-did the arithmetic by hand, and that no one else has run them.
- **Form.** Template fields, the Milestone line and Context are present. There are three options, each with gain, cost and reversibility. No default and no timeout is right for a value target. The cost of leaving it unruled is stated. The recommendation gives its confidence and what would change it.

## Round 2 findings

| # | Round 2 finding | Status |
|---|---|---|
| 1 | Recommended option's relation to the two rules not accurate; undefined review after 30 more pieces (blocking) | Answered. The review is gone; "passed" now includes holding up, so only a passed method enters the model under B and C; the recommended option is now the one named as the departure. |
| 2 | Recommendation claimed "what you asked for" for the narrower option (blocking) | Answered. The phrase now sits on A, which is the owner's wording; B's title says what B does. |
| 3 | One look or two not said for each option | Partly. Each option now says. The cost of longer trials is charged to B alone: finding 1 below. |
| 4 | What going outside the rule does to the rule | Answered (line 5). |
| 5 | "Inside the rules" not shown for a fresh trial design | Partly. B's cost now gives both readings of "Killed, not tuned" and what follows from the stricter one; the playbook rule is still unsaid: finding 2 below. |
| 6 | Loose definitions | Answered (line 11; "shuffled draws"). |
| 7 | Owner's time: review uncounted, no time per card, cap against two weeks | Answered. The review is gone, time per card is said to be unknown, and results cards are never held back. One gap: finding 5 below. |
| 8 | A's way back rested on an unruled review date | Answered: "by a model change, which you rule". |
| 9 | Four options; cost of leaving it unruled | Answered. |
| 10 | Round 1's outcome not given; independent run dropped | Answered (line 34). The line will need round 3's outcome when recorded. |
| 11 | Plainness on a phone | Partly: finding 7 below. |
| 12 | "Nothing is dropped by the pipeline" holds only in form under the narrower options | Stands as before, and is still disclosed by B's cost ("your approval cannot keep a 'not passed' method"). |
| 13 | Context cites a question file due to be deleted | Answered in form; the commit id is unconfirmed: finding 8 below. |

Round 1 findings left partly answered at round 2: 1 and 2 are answered (as round 2's 2 and 1 above); 7 and 9 are moot or answered by the new definition of "passed"; 10 and 11 are answered; 4 and 14 remain partly answered (findings 2 and 7 below).

## Non-blocking

1. **Lines 29 and 30: the cost of longer trials is charged to B but not to A, which has the same two looks.**
   - A reads "Two looks planned" and its cost names only the rule and the first risk. B's cost adds "about 3 to 5 trials in 10 run twice as long".
   - Both options run the same trial, so the cost is equal. A reader weighing A against B sees it under B only.
   - This is round 2's finding 3 turned round: there the cost sat on one option and leaned against it; here it leans, mildly, toward the recommended one.
   - It does not block because A says "Two looks planned", line 26 says what a second look adds, and line 33 says "if shorter trials matter more, C".

2. **Lines 5 and 30: B's relation to "No re-running for a better answer" is still not said.**
   - Line 5 says "B and C stay inside it", meaning "Killed, not tuned". B's own cost says that holds only on one reading; on the stricter one B "can only reject". So the flat first-line statement is conditional, and the card does not say who settles the reading.
   - The playbook says "Null results are results. No re-running for a better answer." Its "new, genuinely different registration" sits under "When the test itself was wrong". B's new trial design follows a sound trial that came back "not passed".
   - Line 26 says the second look is "not a re-run after seeing results". B's new design is drawn up after seeing results, and the card says nothing either way.
   - Context line 48 cites the playbook, but no line in the card body uses it for B.
   - It does not block: B is not recommended, the consequence of the stricter reading is on the card, and the limit ("fails twice goes back") and the Critic's check are there.

3. **Line 29: A's cost does not say that "not passed" includes a method whose work held up worse.**
   - Line 11 defines "not passed" as anything else, so it covers a trial where the method's pieces did worse on a check by more than chance.
   - A's cost says "methods with no passed trial can enter the model" and names only "what is popular rather than what helps". It does not name harm.
   - The owner said missing a helpful method and adopting a harmful one worry them "Both equally" (groundwork answer 3). The hold-up checks are the plan's guard against the second.
   - It does not block: line 29 says the results card "says plainly when it was not passed and why", and the owner decides with that in front of them.

4. **Lines 29 and 33: A makes the keep line the owner has just chosen advisory, and the card does not say so.**
   - The owner chose "1 in 10 (catch more)" for part 2, which reads "A method is kept when … and the work holds up".
   - Under A the line still judges the trial but no longer decides what is kept. The value-target card's "Kept methods stay only on their own results" would no longer hold either.
   - "A small trial is weak evidence either way" is fair against the figures: a real halving is missed 1 to 3 times in 10 before the hold-up checks, and a useless method passes up to 1 time in 10.

5. **Lines 38 to 41: one gap on the owner's time.**
   - Under A, the card does not say whether approving the results card is itself the change to the operating model, or whether a separate model change follows for the owner to rule (R16: "lands through the model's own change process").
   - Results cards are uncapped. That is bounded by the entry cards the owner approves, but the card does not say so.
   - The figures 3 and "two weeks" have no source; they are rightly labelled proposals.

6. **Line 30: "goes back to the screening" is not explained.** The playbook's words are "goes back to Discovery". The card does not say what it means for the method: dropped, or queued for a later entry card.

7. **Plainness on a phone.**
   - Line 5 runs to about 135 words, longer than at round 2. It carries the departure, the proposal to the model, the card's history, the owner's reason and the cost of waiting in one paragraph.
   - Line 30 runs to about 120 words, and its last sentence (the two readings of the rule) is the hardest on the card.
   - Line 19 is a heading with a 25-word bracket holding two figures before the table it introduces.
   - The table itself is clear and answers the earlier "9 and 7 in 10" point.

8. **Context line 45: "at commit 5995412" could not be confirmed.** I hold no command tool, and the id appears nowhere else in the records I can search. The question file itself is present and says what the line claims.

9. **Line 15: "carries the trial's plan, which is then fixed" does not mention that the second look stops if the first look's hold-up checks fail.** The value-target card said so ("the second look stops and the method is dropped"). Under "Nothing is dropped by the pipeline" that result would now come to the owner; the card leaves it to inference.

## Files read

- /home/user/ml-critic-243/questions/P-002-trial-gates.md
- /home/user/ml-critic-243/reviews/P-002-trial-gates/critic.md
- /home/user/ml-critic-243/questions/P-002-value-target.md
- /home/user/ml-critic-243/reviews/P-002-value-target/critic.md (round 3, by search)
- /home/user/ml-critic-243/intake/P-002-owner-value-target-answers-2026-11-10.md
- /home/user/ml-critic-243/intake/P-002-value-target-odds-2026-11-10.md
- /home/user/ml-critic-243/questions/_TEMPLATE.md
- /home/user/ml-critic-243/decisions/questions/P-002-groundwork-shortlist.md
- /home/user/ml-critic-243/decisions/questions/P-002-target.md (line 17, by search)
- /home/user/ml-critic-243/docs/projects/P-002.md (section 7)
- /home/user/ml-critic-243/docs/LESSONS.md (LL-08, LL-76)
- /home/user/ml-critic-243/AGENTS.md (§5)
- /home/user/Personal-Org-Operating-Model/OPERATING_MODEL.md (§1, §2, the experiment playbook)
- /home/user/Personal-Org-Operating-Model/docs/archive/OPERATING_MODEL_v2.5.1.md (line 33)
