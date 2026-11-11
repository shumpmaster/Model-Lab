# Ruling needed: the line each trial is judged on, at its two looks

Milestone: M9

WHY: The independent check of these figures failed twice before it passed: the Reviewer, on a different AI model from their writer, failed the first two runs because figures were stated unfairly, and passed the third. The figures have not been worked out for pieces that depend on each other. You asked to decide this line on a card of its own, on checked figures. The choice is between keeping a useless method's chance of passing at most 1 in 10 whatever today's share turns out to be (B), and passing slightly more useful methods with slightly fewer second looks (A). This card makes no recommendation. Until you rule, the trial plan cannot be fixed and no trial can start. It sets how often a trial can be fooled, so it is part of the value target: yours alone, never defaulted. Either choice can be changed for trials not yet started.

**Words.**
- A **trial** tries one screened method (an idea for working better, found by the screening) on new pieces of work. A **piece** is one merged pull request of the kind being tried. **Each way** means with the method and without it.
- The **line** is how unlikely a difference must be by chance before a look passes the method: a look passes it when chance alone would give a gap this large at most 0.097 of the time (A) or 0.093 of the time (B). A trial has two chances to pass, so the line sits a little below 1 in 10, to keep the overall chance of passing a useless method near 1 in 10.
- The **starting share** is how often pieces of that kind need you today, without the method; it is not known before a trial, and how often a useless method passes depends a little on it.
- A **method that does nothing** makes no difference; passing it is a false alarm. A **true halving** is a method whose pieces need you exactly half as often.
- The **second look** happens only if look 1, at 30 pieces each way, leaned the right way and did not pass. It costs 60 more pieces (30 each way), a second wait of 30 days and 5 more short reads.
- A **short read** is one of the pieces you read yourself, picked at random and shown to you unlabelled; 5 per look.
- The **hold-up checks** test that the method's work did no worse at passing its first independent check and at not being reopened for a fault. They can only lower the figures below.

**How often each version passes** (before the hold-up checks, which can only lower these):

| Starting share | A: does nothing | B: does nothing | A: true halving | B: true halving |
|---|---|---|---|---|
| 1 in 10 | 0.0677 | 0.0677 | 0.2753 | 0.2753 |
| 2 in 10 | 0.0908 | 0.0882 | 0.5192 | 0.5183 |
| 3 in 10 | 0.0989 | 0.0963 | 0.7009 | 0.6913 |
| 4 in 10 | 0.1043 | 0.0908 | 0.8325 | 0.8295 |
| 5 in 10 | 0.0933 | 0.0842 | 0.9231 | 0.9159 |
| 6 in 10 | 0.1043 | 0.0908 | 0.9671 | 0.9647 |
| 7 in 10 | 0.0989 | 0.0963 | 0.9910 | 0.9906 |
| 8 in 10 | 0.0908 | 0.0882 | 0.9989 | 0.9988 |
| 9 in 10 | 0.0677 | 0.0677 | 1.0000 | 1.0000 |
| Worst at any share | 0.1063 (at 0.368 and 0.632) | 0.0982 (at 0.3316 and 0.6684) | | |

**How often each version takes the second look:**

| Starting share | A: does nothing | B: does nothing | A: true halving | B: true halving |
|---|---|---|---|---|
| 1 in 10 | 0.3800 | 0.3800 | 0.5800 | 0.5800 |
| 2 in 10 | 0.3824 | 0.3824 | 0.5431 | 0.5431 |
| 3 in 10 | 0.3827 | 0.3850 | 0.4779 | 0.4782 |
| 4 in 10 | 0.3808 | 0.3931 | 0.3793 | 0.3863 |
| 5 in 10 | 0.3890 | 0.4005 | 0.2693 | 0.3006 |
| 6 in 10 | 0.3808 | 0.3931 | 0.1907 | 0.2222 |
| 7 in 10 | 0.3827 | 0.3850 | 0.1082 | 0.1273 |
| 8 in 10 | 0.3824 | 0.3824 | 0.0354 | 0.0447 |
| 9 in 10 | 0.3800 | 0.3800 | 0.0066 | 0.0068 |

Over every starting share, B never takes the second look less often than A. It takes it at most about 1 in 100 more often for a method that does nothing (near 0.43 and 0.57), and at most about 4 in 100 more often for a true halving (near 0.55).

OPTIONS:
  A. **A line of 0.097: 1 in 10 holds at most starting shares; slightly more useful methods pass.** This is the line worked out so far. A method that does nothing passes more than 1 in 10 of the time when the starting share is in two bands, about 0.31 to 0.43 and about 0.57 to 0.69; at most 0.1063, at 0.368 and 0.632. At 1 in 2 it passes 0.0933, and outside the bands at most 1 in 10. *Gain:* a true halving passes up to about 1 in 100 more often than under B, and the second look is taken as often as under B or less often. *Cost:* the 1 in 10 you set for a useless method passing does not hold at every starting share. It meets the check shown on your value-target card, at starting shares of 1 in 2 and 3 in 10 (0.0933 and 0.0989); it does not meet the trial-gates card's unqualified "passes no more often". *Reversible:* yes, for trials not yet started.
  B. **A line of 0.093: 1 in 10 holds at every starting share; slightly fewer useful methods pass.** A method that does nothing passes at most 0.0982, at 0.3316 and 0.6684. *Gain:* the 1 in 10 holds whatever the starting share turns out to be, as the trial-gates card worded it. *Cost:* a true halving passes up to about 1 in 100 less often than under A (0.0097 at most). The second look is taken up to about 4 in 100 more often for a true halving (about 1 in 100 for a method that does nothing), each time with 60 more pieces, 30 more days and 5 more short reads for you. *Reversible:* yes, for trials not yet started.

RECOMMENDATION: none. You asked to decide this on checked figures, and the difference is a judgement between a firm 1 in 10 and slightly more passes of useful methods.
WHO HAS CHECKED IT: the Reviewer, on a different AI model from the figures' writer (the Definer), ran the script and its own sums three times. It failed rounds 1 and 2 because figures were stated unfairly (a range given too wide, and a ceiling taken over nine shares only); no computed result was wrong, though two gaps were corrected by 0.0001 for rounding. It passed round 3. The Critic checked this card: round 1 failed it for leaving "the line" undefined.
WHAT THE FIGURES ASSUME, in plain words: whether a piece needs you does not depend on any other piece, and every piece on one side has the same chance (A1). A true halving is exactly half (A3). The figures come before the hold-up checks, the short reads and any stop, which can only make a method pass less often (A5). The starting share is the same at both looks (A6). They have not been worked out for pieces that depend on each other or for a share that changes between looks.
RISK CLASS: R3 (part of a value target, the owner's own ruling)   REVERSIBILITY: reversible (for trials not yet started)   BLAST RADIUS: how often every screened method's trial passes or is fooled, and how many trials run to the second look
DEFAULT: none — value targets are never delegated or defaulted   TIMEOUT: none

## Context
- The owner chose to decide the line on a card of its own during Design, on figures checked by someone other than their writer: "Decide later on checked figures (Recommended)" (source: decisions/questions/P-002-design-gate.md, Part 7)
- Both versions, every figure on this card and assumptions A1, A3, A5 and A6 (source: experiments/E-004.md, "Deciding threshold"; experiments/E-004/line.py and line-output.txt at commit 5448c15)
- The Reviewer's three rounds: round 1 FAIL on the wording of A's bands, round 2 FAIL on the second-look gap given over nine shares only, round 3 PASS, with every figure reproduced by its own sums (source: reviews/P-002-two-look-line/reviewer.md)
- The owner chose 1 in 10: "A useless method is kept at most about 1 time in 10"; the planned second look was put as "a little stricter than the part 2 line so that a useless method is still kept no more often than that line (checked at starting shares of 1 in 2 and 3 in 10)" (source: git show 964da47:questions/P-002-value-target.md, parts 2 and 3)
- The trial-gates card put the second look as "judged together on a slightly stricter line so a useless method passes no more often" (source: git show 3ae1268:questions/P-002-trial-gates.md)
- E-004 names the two versions "the line as worked out so far" and "a line held at most 1 in 10 at every starting share"; this card names both by their line, after the Critic's round 1 (source: experiments/E-004.md; reviews/P-002-two-look-line/critic.md)
- The second look's cost: 60 more pieces, a second wait of 30 days and 5 more short reads (source: experiments/E-004.md; decisions/questions/P-002-design-gate.md, Part 6)
- S-002's stop rule of three rounds for this check, not reached since round 3 passed (source: specs/S-002.md)
- The Critic's round 1 on this card (source: reviews/P-002-two-look-line/critic.md)
