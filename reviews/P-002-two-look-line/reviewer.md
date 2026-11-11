Verdict: FAIL

*The Reviewer's independent run of the line at two looks (P-002, P18), both versions, brief 261, at commit e9f1f2f; a session on a different model from the script's writer, the Definer. Recorded verbatim by the orchestrator, 2026-11-11.*

## Round 1 (commit e9f1f2f)

Verdict: FAIL

Every figure in line-output.txt reproduces, and each agrees with my own exact sums and my own seeded simulation. The FAIL rests on one small wording fault in experiments/E-004.md (finding 1). It misstates version (a) in the text the owner's card will draw on. I recommend neither line.

Fixed copy: /home/user/ml-fixed-261 at e9f1f2f. Nothing was written in it (`git status --short | wc -l` gives 0, no `__pycache__`).

## Findings

**1. Blocking, small. E-004 says version (a) is "above 0.10 from 0.307 to 0.693". It is not above 0.10 across that whole range.**
- Where: /home/user/ml-fixed-261/experiments/E-004.md:122, "at most 0.1063, near a starting share of 0.632 (and above 0.10 from 0.307 to 0.693)".
- The truth is two bands with a gap between them. A do-nothing method passes above 0.10 from about 0.307 to 0.429 and from about 0.571 to 0.693. From about 0.430 to 0.570 it is below 0.10 (0.0933 at 1 in 2).
- Command: `python3 -I /tmp/claude-0/-home-user/050cc2ca-c3a4-5015-8eb5-9c67e3cf5108/scratchpad/rv261/sweep.py`
- Output: `(a) 0.097: ... shares above 0.10 (step 0.0001): 2452; runs: [(0.3068, 0.4293), (0.5707, 0.6932)]` and `0.5 0.09329`.
- line-output.txt carries the hint ("246 grid shares", where a full range would be 387). E-004 drops it.
- The same sentence in E-004 gives 0.0933 at 5 in 10, so it contradicts itself.
- Why blocking: it makes (a) look worse than it is, in the text the owner rules from. An earlier round treated a wrong range in the same place as blocking (reviews/P-002-value-target-odds/reviewer.md:263).
- A fair wording: "above 0.10 at starting shares from about 0.31 to 0.43 and from about 0.57 to 0.69".
- line.py's own print line ("above 0.10 from 0.307 to 0.693 (246 grid shares)") has the same weakness, less sharply.

**2. Not blocking. The worst cases are each named at one share only; each has a mirror.**
- (a): 0.10634 at 0.632 and also at 0.368. (b): 0.09818 at 0.6684 and also at 0.3316. Next line up: 0.10086 at 0.343 and also at 0.657.
- Output: `(a) 0.097: worst does-nothing pass 0.10634 at share 0.632; mirror share 0.3680 gives 0.10634`.
- E-004 says "near 0.632" and "near 0.668" only. docs/projects/P-002.md section 6 says "near 4 in 10 and 6 in 10", which is the fairer form.

**3. Not blocking. The chance of a second look is in line-output.txt but nowhere in E-004 or S-002.**
- The figures reproduce (see Verified). Under (b) the second look is taken a little more often than under (a). For a do-nothing method: 0.4005 against 0.3890 at 1 in 2. For a true halving: 0.3006 against 0.2693 at 1 in 2, and 0.2222 against 0.1907 at 6 in 10. At 1 in 10 and 2 in 10 there is no difference to four places.
- A second look means 60 more pieces, a second 30-day wait and 5 more short reads. That is a cost difference between the lines which the card's source text does not state.
- Command: `grep -n "second look taken\|0\.3006\|0\.2693" experiments/E-004.md specs/S-002.md` returns nothing.

**4. Not blocking. E-004 and S-002 point to the eight assumptions but do not state them.**
- E-004.md:121 says "at the assumptions listed in the script"; S-002.md:87 says "with the script's eight assumptions". S-002.md:181 states A1 as a known limit.
- I found no assumption that contradicts E-004 or section 6. Per assumption:
  - A1 (independent pieces, one fixed chance per arm): a modelling choice; S-002:181 names it as a limit.
  - A2 (exactly 30 each way per look): matches E-004 Step 4 and Exclusions (a withdrawn piece's place goes back).
  - A3 (halving is exactly half): matches section 6 and the earlier run.
  - A4 (strictly fewer, a tie does not go on): matches E-004 Step 5 item 3 and twolook.py's `x<y`.
  - A5 (before hold-up checks, reads and stops, which can only lower passes): matches E-004 Step 5 item 4 and Step 6; the direction is right.
  - A6 (same starting share at both looks): stated only in the script.
  - A7 (grid of shares): checked; my 0.0001 grid finds the same worst cases, and neighbouring grid values differ by at most 0.000116, so no peak hides between grid points.
  - A8 (a range of lines decides the same): confirmed exactly, see Verified.
- The owner's card should carry A1, A3, A5 and A6 in plain words, since E-004 does not.

**5. Not blocking. Small points.**
- line.py's header says "about a minute". It ran in 22.5 seconds.
- The 0.097 line also sits in a range: any line from 0.09616 up to, not including, 0.09725 decides the same. E-004 gives this range for (b) only.
- The earlier review's sentence "Every share from about 0.32 to 0.68 exceeds 0.10" (reviews/P-002-value-target-odds/reviewer.md:265) has the same fault as finding 1. Its figures are right.

**6. Version (a) agrees with the earlier independent run. No finding.**
- Earlier: 0.0933 at 1 in 2, 0.0989 at 3 in 10, 0.1043 at 4 in 10 and 6 in 10, 0.0908 at 2 in 10 and 8 in 10, maximum 0.1062 at 0.36 and 0.64 on a 2% grid; halving 0.9231 and 0.7009.
- Now: the same to four places. My simulation at 0.36 gives 0.1061; the finer grid puts the peak at 0.368 and 0.632, at 0.1063.
- Section 6 of docs/projects/P-002.md ("0.093 and 0.099 ... up to about 0.106 at starting shares near 4 in 10 and 6 in 10") is fair.

**7. Fairness of the other statements. No finding.**
- E-004's two lists of nine do-nothing figures and nine halving figures for (a) and (b): all correct.
- "(b) ... 0.093 (any line from 0.09227 up to, not including, 0.09359 decides the same)": correct. These are the exact neighbouring attainable p-values.
- "0.0000 to 0.0097 less often than under (a)": correct, and it holds at every share, not only the nine (largest gap 0.00970 at a share of 0.298).
- S-002.md:10 "up to about 0.106" and "up to about 1 in 100 less often": fair.
- "the next line up reaches 0.1009 near 0.343": correct (0.10086).
- Neither E-004 nor S-002 recommends a line.

**8. The charter's PR and handover items.** My manifest holds no pull request body, no Tasks section and no handover package, so the "What this means for you" rule and the tick check had nothing to apply to. S-002's opening summary is plain. No join-up section applies: this work has no screens or views. `surface_guard.py` was not run: the brief gave no range (see Undone).

## Six-part contract

**Changed (by file).** Nothing in any repository. Scratch only, under /tmp/claude-0/-home-user/050cc2ca-c3a4-5015-8eb5-9c67e3cf5108/scratchpad/rv261/: exact.py, sweep.py, sim.py and their outputs exact.out, sweep.out, sim.out, run1.txt.

**Why.** Brief 261: the independent run of both lines, by someone other than the Definer who wrote line.py (commit bf54505, author `definer`).

**Verified (command and output).**

1. Reproduction. `PYTHONDONTWRITEBYTECODE=1 python3 -I experiments/E-004/line.py`, then `diff` against experiments/E-004/line-output.txt: `IDENTICAL`, in 22.5 s.

2. Exact sums (`python3 -I exact.py`). Written from scratch: whole-number arithmetic, Fisher p-values as exact fractions, lines as exact fractions, no numpy, no code from line.py. Version (b)'s bounds come out as exact fractions: `largest attainable p <= 0.093: 0.0922738` (look 2, counts 18 against 26 or 34 against 42) and `smallest attainable p > 0.093: 0.0935936` (look 1, 9 against 15 or 15 against 21). Results, which match line-output.txt to every printed place:

| Share | Does nothing passes (a) / (b) | True halving passes (a) / (b) | Second look, halving (a) / (b) | Second look, does nothing (a) / (b) |
|---|---|---|---|---|
| 0.1 | 0.0677 / 0.0677 | 0.2753 / 0.2753 | 0.5800 / 0.5800 | 0.3800 / 0.3800 |
| 0.2 | 0.0908 / 0.0882 | 0.5192 / 0.5183 | 0.5431 / 0.5431 | 0.3824 / 0.3824 |
| 0.3 | 0.0989 / 0.0963 | 0.7009 / 0.6913 | 0.4779 / 0.4782 | 0.3827 / 0.3850 |
| 0.4 | 0.1043 / 0.0908 | 0.8325 / 0.8295 | 0.3793 / 0.3863 | 0.3808 / 0.3931 |
| 0.5 | 0.0933 / 0.0842 | 0.9231 / 0.9159 | 0.2693 / 0.3006 | 0.3890 / 0.4005 |
| 0.6 | 0.1043 / 0.0908 | 0.9671 / 0.9647 | 0.1907 / 0.2222 | 0.3808 / 0.3931 |
| 0.7 | 0.0989 / 0.0963 | 0.9910 / 0.9906 | 0.1082 / 0.1273 | 0.3827 / 0.3850 |
| 0.8 | 0.0908 / 0.0882 | 0.9989 / 0.9988 | 0.0354 / 0.0447 | 0.3824 / 0.3824 |
| 0.9 | 0.0677 / 0.0677 | 1.0000 / 1.0000 | 0.0066 / 0.0068 | 0.3800 / 0.3800 |

The "1.0000" entries are 0.99995, rounded.

3. Sweep (`python3 -I sweep.py`). Pass regions built from the exact fractions; every share from 0.0001 to 0.9999 by 0.0001.
   - `(a) 0.097: worst does-nothing pass 0.10634 at share 0.632`
   - `(b) 0.09227: worst does-nothing pass 0.09818 at share 0.6684 ... shares above 0.10: 0`
   - `next up 0.09359: worst does-nothing pass 0.10086 at share 0.6573` (the same 0.10086 at 0.343)
   - `halving pass, (b) minus (a), over shares 0.001..0.999: most negative -0.00970 at 0.298`
   - All 62 attainable lines from 0.05 to 0.10: `worst does-nothing pass non-decreasing in the line: True`. So line.py's halving search is sound, and 0.09227 is the largest line that holds. The next, 0.09359, gives 0.10085; the one after, 0.09425, gives 0.10252.

4. Simulation (`python3 -I sim.py`). Seed 261, 2,000,000 trials per row, lines 0.097 and 0.093. Every row is within about 0.0004 (two standard errors) of the exact figure. Worst cases:
   - `line 0.0970 share 0.632: pass 0.1061`, `share 0.368: pass 0.1063`
   - `line 0.0930 share 0.6684: pass 0.0980`, `share 0.3316: pass 0.0979`
   - `line 0.0936 share 0.343: pass 0.1013`, `share 0.657: pass 0.1009`

5. line.py reads nothing and reaches no network: its only imports are numpy and math.comb.

**Undone.**
- `surface_guard.py diff` was not run; the brief names no range or branch.
- I ran exact.py's full output once and did not re-time it. Its printed run time (0.4 s) looks too short for the work, so I do not rely on that timing. Its figures are confirmed independently by sweep.py and sim.py.
- I did not test what happens when A1 or A6 fail (pieces that are not independent, or a share that drifts between looks). Those are stated assumptions, not figures to reproduce.

**Needed outside my surface.**
- The Definer: reword E-004.md:122 to the two bands (finding 1). Optionally name the mirror shares, and add the second-look figures or a line pointing to them (findings 2 and 3).
- The Chief of Staff, for the card: state the two bands for (a); state that (b) takes the second look slightly more often; carry A1, A3, A5 and A6 in plain words.

**Open questions.**
1. Should the card show the second-look chance for both lines, since it is a cost to the owner that differs between them?
2. Should line.py's print line be reworded and its output re-recorded, or is fixing E-004's wording alone enough, leaving the output as run?
3. "At every starting share" is read as a 0.0001 grid (A7). My check bounds the gap between grid points at 0.000116 against a margin of 0.0018, so I treat it as settled. Does the owner's card need to say so?
