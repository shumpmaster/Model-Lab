Verdict: PASS

*The Critic on questions/P-002-two-look-line.md, the owner's card on the line at two looks (P-002, P18): round 1 (FAIL), brief 267, at commit e7569bc; round 2 (PASS), brief 268, at commit 79d8d5a. A fresh session on a different model from the card's writer, started by the Chief of Staff (session_01QBwHGJm2otqFdQxgZQ1fyx), 2026-11-11. Recorded verbatim by the Orchestrator from the helper's return; the round's own verdict line is recorded as "The round's verdict was …" (LL-68). The verdict above is the latest round's. After round 2, its findings 1 to 6 were applied as wording (commit after 79d8d5a).*

## Round 1 (commit e7569bc)

The round's verdict was FAIL.

The card fails on one point, which blocks it. It never says what "the line" is. That is the word the whole choice is about: a newcomer reading "0.097 at each look" cannot tell what the number measures, or why a line set below 1 in 10 still lets a useless method pass more than 1 in 10 of the time. Everything else meets its standard. All 72 figures in the two tables match line-output.txt. So do the two worst cases, the two bands, the ranges of lines and the second-look ceilings over all shares, which are as the Reviewer's round 3 passed them ("about 1 in 100" and "about 4 in 100"). The card makes no recommendation, which the owner's Part 7 answer allows. The risk class, default and timeout match the two earlier value-target cards. Five further findings below do not block. Two of them concern fairness and should be fixed in the same pass.

## Findings

**1. Blocking. "The line" is never defined.**
- Where: WHY (line 5), "Each trial is judged twice on one line". Option headings (lines 44 and 45), "0.097 at each look" and "0.093 at each look". The Words list (lines 7 to 10) has no entry for it.
- Problem: E-004 (Deciding threshold) says a look passes when its "p-value is at most the line". Nothing on the card turns that into plain words. Without it the owner cannot see:
  - how a line of 0.097 fits with "passes at most 0.106";
  - why both lines sit below the 1 in 10 they set (two looks give two chances to pass).
- Fix: add a first Words bullet, for example: "The **line** is how unlikely a difference must be by chance before a look passes it: a look passes the method when chance alone would give a gap this large at most 0.097 of the time (A) or 0.093 of the time (B). A trial has two chances to pass, so the line sits a little below 1 in 10 to keep the overall chance near 1 in 10."

**2. Not blocking. Other words a newcomer needs are not defined.**
- Where:
  - "hold-up checks": lines 12 and 49;
  - "short reads": lines 10 and 49;
  - "30 pieces each way": lines 5 and 10;
  - "trial" and "screened method": line 50.
- Problem: each is defined only on the earlier cards (value-target "Words used below"; trial-gates "Words").
- Fix: add one short bullet each. For example:
  - "**Each way**: with the method and without it."
  - "The **hold-up checks** test that the method's work did no worse at passing its first check and at not being reopened."
  - "A **short read** is one of the pieces you read yourself, picked at random and unlabelled."

**3. Not blocking, fairness. Option A's cost leaves out what the owner was shown before.**
- Where: Option A, line 44, "*Cost:* the 1 in 10 you set for a useless method passing holds at most starting shares, but not at all of them."
- The cost is true. But the owner's part 2 choice read "at most about 1 time in 10". The part 3 option the owner chose promised the stricter line "checked at starting shares of 1 in 2 and 3 in 10" (ml-cards/P-002-value-target.md, lines 46 and 68). Line A meets that check: 0.0933 and 0.0989.
- Only the trial-gates card (line 26) said "passes no more often" with no limit. Leaving out the earlier, narrower promise tilts the card slightly toward B.
- Fix: add to A's cost, or to Context, "It meets the check shown on your value-target card, at starting shares of 1 in 2 and 3 in 10; it breaks the unqualified 'no more often' on the trial-gates card", citing both cards as put.

**4. Not blocking, fairness. The two option names are not balanced.**
- Where: lines 44 and 45.
- Problem: "A. The line as worked out so far" names a status, while "B. A line held at most 1 in 10 at every starting share" names B's benefit. E-004 uses the same names, so they are not the card's invention, but on the card they lean slightly toward B.
- Fix: give the two options matching names, for example "A. A line of 0.097: 1 in 10 holds at most starting shares, slightly more useful methods pass" and "B. A line of 0.093: 1 in 10 holds at every starting share, slightly fewer pass".

**5. Not blocking. "WHO HAS CHECKED IT" understates the corrections.**
- Where: line 48, "It failed rounds 1 and 2 on how the figures were worded, never on a figure".
- Problem, from the Reviewer's record:
  - Round 2's blocking finding was that a stated ceiling (0.0315) was not the real ceiling (0.0367).
  - Round 2's finding 2 corrected 0.0315 to 0.0314.
  - Round 3 found that round 2 had wrongly accepted 0.0123 (correct: 0.0124).
  - None of these changed a computed result, but "never on a figure" reads as if no figure was ever corrected.
- Fix: "It failed rounds 1 and 2 because figures were stated unfairly (a range too wide, and a ceiling taken over nine shares only); no computed result was wrong, though two gaps were corrected by 0.0001 for rounding. It passed round 3."

**6. Not blocking. Smaller points.**
- **a. The opening paragraph does not lead with failures.** WHY (line 5) mentions the passed third run but not the two failed rounds. AGENTS.md section 4 says the paragraph "starts with anything that failed or was skipped". Fix: open WHY with one clause such as "The Reviewer failed the first two runs on wording and passed the third; the figures have not been worked out for pieces that depend on each other."
- **b. "0.093" means two things.** Option A, line 44, gives "(0.093)" as A's pass chance at 1 in 2, and 0.093 is also B's line. Fix: write "0.0933", as the table does.
- **c. B's cost blurs two figures and leaves out the owner's time.** Option B, line 45, says "It takes the second look up to about 4 in 100 more often, each time with 60 more pieces and 30 more days". The "4 in 100" is for a true halving only (about 1 in 100 for a method that does nothing), and the 5 extra short reads, the owner's own time, are left out. Fix: "...up to about 4 in 100 more often for a true halving (about 1 in 100 for a method that does nothing), each time with 60 more pieces, 30 more days and 5 more short reads for you."

**Checked and found right (no finding):**
- **Pass table** (lines 14 to 25): all 36 figures match line-output.txt lines 13 to 21, and the worst cases match lines 6, 7 and 30 to 32.
- **Second-look table** (lines 29 to 39): all 36 figures match. The card's column order differs from the file's, and each was read across correctly.
- **Second-look summary** (line 41) and the other option figures (lines 44 and 45) match line-output.txt lines 24, 27, 41 to 45 and E-004 lines 122 to 124:
  - line 41: "never ... less often", about 1 in 100 near 0.43 and 0.57 (0.0131), about 4 in 100 near 0.55 (0.0367);
  - bands 0.31 to 0.43 and 0.57 to 0.69 (0.307 to 0.429 and 0.571 to 0.693);
  - 0.106 at about 0.37 and 0.63;
  - 0.098 at about 0.33 and 0.67;
  - "0.0097 at most" (E-004, "0.0000 to 0.0097 less often", which Reviewer round 1 confirmed holds at every share).
- **Second-look cost** (line 10) matches E-004 Step 6 and line 124.
- **Assumptions** (line 49): A1, A3, A5 and A6 are in plain words and match E-004 line 125, including what has not been worked out.
- **Recommendation**: none, with a reason that is not a recommendation. The value-target card's part 2 sets the precedent, and the owner's Part 7 words ("Decide later on checked figures") fit.
- **Risk class, default, timeout**: R3, no default and no timeout, the same as both earlier value-target cards (lines 98 to 99 and 35 to 36), and right for a value target.
- **Context**: each bullet's claim matches its source as far as my manifest reaches (Part 7, verbatim; the Reviewer's rounds; E-004).

## Six-part contract

**Changed (by file).** Nothing. I hold no write tool and wrote nothing in /home/user/ml-fixed-267 or /home/user/ml-cards.

**Why.** Brief 267 (/home/user/Model-Lab/docs/briefs/267-critic.md): check the owner's card on the line at two looks, before it is put to the owner.

**Verified.**
- I read in full:
  - /home/user/ml-fixed-267/questions/P-002-two-look-line.md
  - /home/user/ml-fixed-267/questions/_TEMPLATE.md
  - /home/user/ml-fixed-267/AGENTS.md (sections 4 and 5)
  - /home/user/ml-fixed-267/experiments/E-004.md
  - /home/user/ml-fixed-267/experiments/E-004/line-output.txt
  - /home/user/ml-fixed-267/reviews/P-002-two-look-line/reviewer.md (rounds 1 to 3)
  - /home/user/ml-fixed-267/decisions/questions/P-002-design-gate.md (Part 7 and "How it is carried out")
  - /home/user/ml-cards/P-002-value-target.md
  - /home/user/ml-cards/P-002-trial-gates.md
- I compared every figure on the card by hand against line-output.txt and E-004.md.
- I have no shell, so I ran no command and did not re-run line.py. The figures rest on the Reviewer's round 3 reproduction.

**Undone.**
- I did not re-run or re-derive any figure.
- I could not confirm that the cards in /home/user/ml-cards are the ones at commits 964da47 and 3ae1268, which the card's Context cites; I took them as the brief describes them.
- I did not check specs/S-002.md, which the Context cites for the stop rule; it was not in my manifest.

**Needed outside my surface.**
- Chief of Staff: fix finding 1 (blocking) and, ideally, findings 3 to 6 in the same pass. Then hand the card back for a fresh Critic round.
- Orchestrator: record this return verbatim in reviews/P-002-two-look-line/critic.md.

**Open questions.**
1. Option names (finding 4): E-004 uses the same names. Should the Definer rename them in E-004 too, so the card and the plan agree, or may the card use its own names?
2. Finding 3 rests on what the owner was shown on two earlier cards. If the owner already read "passes no more often" as the firm 1 in 10, the card may need to say plainly that line A departs from that earlier wording.

## Round 2 (commit 79d8d5a)

The round's verdict was PASS.

*The Critic on questions/P-002-two-look-line.md, the owner's card on the line at two looks (P-002, P18). This is round 2, brief 268, read from the fixed copy /home/user/ml-fixed-268 at 79d8d5a. It is a fresh session on a different model from the card's writer.*

The card passes. It now says what "the line" is, and that was round 1's only blocking finding. The five findings that did not block are also answered. I checked every changed sentence and figure against line-output.txt, E-004.md and the two cards as put, and all of them match. I checked all 72 table figures again and they still match. Six small findings remain and none of them blocks. One of them (finding 1) is a point that round 1 passed and should not have, so I flag it under D-050.

## Part 1. Round 1's findings against this card

| Round 1 finding | Answered? | Evidence |
|---|---|---|
| 1 (blocking): "the line" not defined | Yes | Line 9 adds a Words entry. It says a look passes "when chance alone would give a gap this large at most 0.097 of the time (A) or 0.093 of the time (B)" and explains why the line sits below 1 in 10 (two chances to pass). This fits E-004 line 120 ("p-value is at most the line"). |
| 2: other words not defined | Yes | Line 8 defines trial, screened method, piece and each way. Line 13 defines short read and line 14 defines hold-up checks. Line 12 gives the second look's cost. |
| 3: A's cost left out the value-target promise | Yes | Line 48: "It meets the check shown on your value-target card, at starting shares of 1 in 2 and 3 in 10 (0.0933 and 0.0989); it does not meet the trial-gates card's unqualified 'passes no more often'." Context line 61 quotes ml-cards/P-002-value-target.md lines 46 and 68 word for word. Context line 62 quotes ml-cards/P-002-trial-gates.md line 26 word for word. |
| 4: unequal option names | Yes | Lines 48 and 49 now use matching names ("A line of 0.097: ... slightly more useful methods pass" and "A line of 0.093: ... slightly fewer useful methods pass"). Context line 63 records the change from E-004's names (E-004 lines 122 and 123, quoted correctly). |
| 5: WHO HAS CHECKED IT understated the corrections | Yes | Line 52 uses the wording I proposed. The "two gaps corrected by 0.0001" are 0.0315 to 0.0314 (Reviewer round 2, finding 2) and 0.0123 to 0.0124 (Reviewer round 3, finding 4). |
| 6a: WHY did not lead with failures | Yes | Line 5 now opens with "failed twice before it passed" and with the dependent-pieces gap. It has no paths or ids. |
| 6b: "0.093" meant two things | Yes | Line 48 writes "0.0933". |
| 6c: B's cost blurred two figures and left out the owner's time | Yes | Line 49: "up to about 4 in 100 more often for a true halving (about 1 in 100 for a method that does nothing), each time with 60 more pieces, 30 more days and 5 more short reads for you." |

## Part 2. Changed sentences and figures

- **Pass table** (lines 18 to 29): all 36 figures match line-output.txt lines 13 to 21. The worst-case row, 0.1063 at 0.368 and 0.632 and 0.0982 at 0.3316 and 0.6684, matches lines 31 and 32.
- **Second-look table** (lines 33 to 43): all 36 figures match lines 13 to 21. The card's column order differs from the file's, and each row was read across correctly.
- **Line 45**: "never ... less often", about 1 in 100 near 0.43 and 0.57 (0.0131) and about 4 in 100 near 0.55 (0.0367). These match lines 41 to 45 and E-004 line 124.
- **Option A** (line 48):
  - the bands 0.31 to 0.43 and 0.57 to 0.69 (0.307 to 0.429 and 0.571 to 0.693, line 24);
  - 0.1063 at 0.368 and 0.632;
  - 0.0933 at 1 in 2, and at most 1 in 10 outside the bands;
  - a gain of up to about 1 in 100 (0.0097).
  - All are correct.
- **Option B** (line 49): 0.0982 at 0.3316 and 0.6684; 0.0097 at most (E-004 line 123). Both correct.
- **Line 12**: 60 more pieces, 30 days and 5 short reads match E-004 line 124 and Step 6.
- **Assumptions** (line 53): A1, A3, A5 and A6 are unchanged and still match E-004 line 125.
- **Fairness**: The headings, gains and costs are now balanced. Each option's cost sits next to the earlier promise it meets or breaks. There is no recommendation.
- **Risk class R3, reversible for trials not yet started, no default, no timeout**: These match both cards as put (value-target lines 98 and 99, trial-gates lines 35 and 36) and fit a value target.

## Findings

**1. Not blocking. The words "on a card of its own" and "checked by someone other than their writer" are not the owner's words in Part 7. Self-implication flag (D-050): round 1 checked this bullet and passed it as "Part 7, verbatim".**
- Where: Context, line 58, "The owner chose to decide the line on a card of its own during Design, on figures checked by someone other than their writer: 'Decide later on checked figures (Recommended)' (source: decisions/questions/P-002-design-gate.md, Part 7)". WHY, line 5, "You asked to decide this line on a card of its own, on checked figures."
- Problem: Part 7 (design-gate record, line 16) holds only "Decide later on checked figures (Recommended)". The card of its own and the check by someone else come from the record's "How it is carried out", P18 bullet (line 27): "run by someone other than their writer, then put to the owner on a card of their own before the design freezes". That bullet is how the ruling is carried out, written by the Chief of Staff, not the owner's words.
- Fix: in line 58, cite "Part 7, and 'How it is carried out', P18". In WHY, write "You chose to decide this line later, on checked figures; it comes to you on a card of its own, as recorded with your ruling."

**2. Not blocking. "Leaned the right way" is not defined.**
- Where: line 12, "only if look 1 ... leaned the right way and did not pass".
- Fix: add "(fewer of the method's 30 pieces needed you than of the other 30; a tie does not go on)". This is E-004 Step 5, item 3.

**3. Not blocking. The rule for the second look leaves out the hold-up checks.**
- Where: line 12.
- Problem: E-004 Step 5 item 4 and P6 say look 1 does not go on if its hold-up checks fail. Line 14 says those checks only lower the figures, and that is true. But line 12 reads as the full rule, and it is not.
- Fix: write "leaned the right way, did not pass, and its work held up".

**4. Not blocking, fairness. The reason given for making no recommendation names only one of A's gains.**
- Where: line 51, "a judgement between a firm 1 in 10 and slightly more passes of useful methods".
- Problem: A's other gain is fewer second looks, which saves the owner's time. It is left out, and "firm" set against "slightly" leans a little toward B.
- Fix: "a judgement between 1 in 10 held at every starting share and slightly more passes of useful methods with slightly fewer second looks."

**5. Not blocking. WHO HAS CHECKED IT stops at round 1.**
- Where: line 52, "The Critic checked this card: round 1 failed it for leaving 'the line' undefined."
- Fix: before the card is put, add "and passed it at round 2".

**6. Not blocking. The stop-rule bullet cites a record that does not name this check.**
- Where: Context, line 65, "S-002's stop rule of three rounds for this check ... (source: specs/S-002.md)".
- Problem: S-002 line 193 says "plan rounds and build rounds, three each". It does not say this check counts as one of them. The Reviewer's round 3 is the record that applies the rule here ("S-002's three-round stop rule is not reached").
- Fix: add reviews/P-002-two-look-line/reviewer.md, round 3, to the bullet's source.

## Six-part contract

**Changed (by file).** Nothing. I hold no write tool, and I wrote nothing in /home/user/ml-fixed-268 or /home/user/ml-cards.

**Why.** Brief 268 (/home/user/Model-Lab/docs/briefs/268-critic.md) asks for round 2 on the card after its change in commit ce7556d.

**Verified.**
- I read in full:
  - /home/user/ml-fixed-268/questions/P-002-two-look-line.md
  - /home/user/ml-fixed-268/reviews/P-002-two-look-line/critic.md (round 1)
  - /home/user/ml-fixed-268/reviews/P-002-two-look-line/reviewer.md (rounds 1 to 3)
  - /home/user/ml-fixed-268/experiments/E-004/line-output.txt
  - /home/user/ml-fixed-268/experiments/E-004.md, lines 60 to 135
  - /home/user/ml-fixed-268/questions/_TEMPLATE.md
  - /home/user/ml-fixed-268/decisions/questions/P-002-design-gate.md
  - /home/user/ml-cards/P-002-value-target.md
  - /home/user/ml-cards/P-002-trial-gates.md
  - /home/user/Model-Lab/docs/briefs/267-critic.md
- I searched /home/user/ml-fixed-268/specs/S-002.md for its stop rule (line 193).
- I compared every figure on the card by hand with line-output.txt and E-004.md.
- I have no shell, so I ran no command.

**Undone.**
- I did not run `git show ce7556d`. I compared the card with round 1's quotations instead, as the brief allows.
- I did not re-derive any figure; they rest on the Reviewer's round 3.
- I took the copies in /home/user/ml-cards to be the cards at 964da47 and 3ae1268, as the brief describes them.

**Needed outside my surface.**
- Chief of Staff: findings 1 to 6, ideally before the card is put. At least finding 5, so that the card records this round.
- Orchestrator: record this return verbatim in reviews/P-002-two-look-line/critic.md as round 2.
- Triage: note the D-050 flag on finding 1. Round 1 accepted the Part 7 bullet as verbatim when part of it is not.

**Open questions.**
1. Finding 1: should the card say plainly that "a card of its own" is how the ruling was carried out, not the owner's own words? Or is citing the P18 bullet enough?
