Verdict: FAIL

*The Critic on questions/P-002-trial-gates.md, the question on the owner's two approvals for each screened method (P-002): round 1 (FAIL), round 2 (FAIL); briefs 241 and 242. Each round a fresh session on a different model from the card's writer, started by the Chief of Staff (session_01QBwHGKirN166RhxQTHuAt9), 2026-11-10. Recorded verbatim by the Orchestrator from the helper's return; the round's own verdict line is recorded as "The round's verdict was …" (LL-68). The verdict above is the latest round's.*

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
