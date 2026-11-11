Verdict: FAIL

*The Critic on questions/P-002-two-look-line.md, the owner's card on the line at two looks (P-002, P18): round 1 (FAIL), brief 267, at commit e7569bc. A fresh session on a different model from the card's writer, started by the Chief of Staff (session_01QBwHGJm2otqFdQxgZQ1fyx), 2026-11-11. Recorded verbatim by the Orchestrator from the helper's return; the round's own verdict line is recorded as "The round's verdict was …" (LL-68). The verdict above is the latest round's.*

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
