# Ruling needed: the line each trial is judged on, at its two looks

Milestone: M9

WHY: Each trial is judged twice on one line: after 30 pieces each way, and, if it leaned the right way, after 30 more. You asked to decide this line on its own card, on figures checked by someone other than their writer. Both versions below have now been worked out and checked three times by a Reviewer on a different AI model from their writer, who passed the third run. The choice is between keeping a useless method's pass chance at most 1 in 10 at every starting share (B) and passing more useful methods (A). This card makes no recommendation. Until you rule, the trial plan cannot be fixed and no trial can start. It sets how often a trial can be fooled, so it is part of the value target: yours alone, never defaulted.

**Words.**
- A **piece** is one merged pull request of the kind being tried. The **starting share** is how often pieces of that kind need you today, without the method; it is not known before a trial.
- A **method that does nothing** is one that makes no difference. **Passing** it is a false alarm. A **true halving** is a method whose pieces need you exactly half as often.
- The **second look** happens only if look 1 leaned the right way and did not pass. It costs 60 more pieces (30 each way), a second wait of 30 days and 5 more short reads.

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
  A. **The line as worked out so far: 0.097 at each look.** A method that does nothing passes more than 1 in 10 of the time when the starting share is in two bands, about 0.31 to 0.43 and about 0.57 to 0.69. It passes at most 0.106, at about 0.37 and 0.63. It does not pass more than 1 in 10 at 1 in 2 (0.093) or outside those bands. *Gain:* a true halving passes up to about 1 in 100 more often than under B. It takes the second look as often as B or less often, so slightly fewer trials run the full length. *Cost:* the 1 in 10 you set for a useless method passing holds at most starting shares, but not at all of them. *Reversible:* yes, for trials not yet started.
  B. **A line held at most 1 in 10 at every starting share: 0.093 at each look.** A method that does nothing passes at most 0.098, at about 0.33 and 0.67. *Gain:* the 1 in 10 holds whatever the starting share turns out to be. *Cost:* a true halving passes up to about 1 in 100 less often than under A (0.0097 at most). It takes the second look up to about 4 in 100 more often, each time with 60 more pieces and 30 more days. *Reversible:* yes, for trials not yet started.

RECOMMENDATION: none. You asked to decide this on checked figures, and the difference is a judgement between a firm 1 in 10 and slightly more passes of useful methods.
WHO HAS CHECKED IT: the Reviewer, on a different AI model from the figures' writer (the Definer), ran the script and its own sums three times. It failed rounds 1 and 2 on how the figures were worded, never on a figure, and passed round 3. The Critic checks this card before it is put to you.
WHAT THE FIGURES ASSUME, in plain words: whether a piece needs you does not depend on any other piece, and every piece on one side has the same chance (A1). A true halving is exactly half (A3). The figures come before the hold-up checks, the short reads and any stop, which can only make a method pass less often (A5). The starting share is the same at both looks (A6). They have not been worked out for pieces that depend on each other or for a share that changes between looks.
RISK CLASS: R3 (part of a value target, the owner's own ruling)   REVERSIBILITY: reversible, for trials not yet started   BLAST RADIUS: how often every screened method's trial passes or is fooled, and how many trials run to the second look
DEFAULT: none — value targets are never delegated or defaulted   TIMEOUT: none

## Context
- The owner chose to decide the line on a card of its own during Design, on figures checked by someone other than their writer: "Decide later on checked figures (Recommended)" (source: decisions/questions/P-002-design-gate.md, Part 7)
- Both versions, every figure on this card and assumptions A1, A3, A5 and A6 (source: experiments/E-004.md, "Deciding threshold"; experiments/E-004/line.py and line-output.txt at commit 5448c15)
- The Reviewer's three rounds: round 1 FAIL on the wording of A's bands, round 2 FAIL on the second-look gap given over nine shares only, round 3 PASS, with every figure reproduced by its own sums (source: reviews/P-002-two-look-line/reviewer.md)
- The 1 in 10 line for a useless method passing, from the owner's value-target answers, and the trial with a planned second look (source: git show 3ae1268:questions/P-002-trial-gates.md; git show 964da47:questions/P-002-value-target.md)
- The second look's cost: 60 more pieces, a second wait of 30 days and 5 more short reads (source: experiments/E-004.md; decisions/questions/P-002-design-gate.md, Part 6)
- S-002's stop rule of three rounds for this check, not reached since round 3 passed (source: specs/S-002.md)
