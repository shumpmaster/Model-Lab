Verdict: PASS

*The Reviewer's independent run of the line at two looks (P-002, P18), both versions, brief 261, at commit e9f1f2f; a session on a different model from the script's writer, the Definer. Recorded verbatim by the orchestrator, 2026-11-11. Round 1 FAIL (brief 261), round 2 FAIL (brief 264), round 3 PASS (brief 266). The verdict above is the latest round's.*

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

## Round 2 (commit ee6ebc3)

Verdict: FAIL

Round 2, brief 264, fixed copy /home/user/ml-fixed-264 at ee6ebc3. Every changed figure in E-004 and S-002 is correct by my own sums, and line.py reproduces its recorded output exactly. The FAIL rests on one small point of fairness (finding 1): the extra second looks under (b) are stated as a ceiling ("at most", "up to") taken over nine shares only, and the true ceiling over all shares is higher and sits between two of the nine. This is a judgement call; the sentences are true as worded. I recommend neither line.

Nothing was written in the copy (`git status --short | wc -l` gives 0; `find . -name __pycache__ | wc -l` gives 0).

## Part 1. Round 1 findings against 9d8710b

| Round 1 finding | Answered? | Evidence |
|---|---|---|
| 1 (blocking): "(a) above 0.10 from 0.307 to 0.693" | Yes | E-004.md:122 now gives two bands, "about 0.31 to 0.43 and about 0.57 to 0.69", and says 0.0933 at 1 in 2 lies between. My sweep: bands `[[0.3068, 0.4293], [0.5707, 0.6932]]`. line.py's print line is fixed too: "from 0.307 to 0.429 and from 0.571 to 0.693 (246 grid shares)". |
| 2: worst cases named at one share only | Yes | E-004 now names 0.368 and 0.632; 0.3316 and 0.6684; 0.343 and 0.657. All confirmed (see Verified 3). |
| 3: second-look chance missing | Partly | The four lists of nine are added to E-004.md:124 and are all correct. The summary of the gap is where finding 1 below sits. |
| 4: assumptions pointed to, not stated | Yes | E-004.md:125 states A1, A3, A5, A6 in plain words. Each matches the script's text. It also says what has not been worked out. S-002.md:87 now says "four of the script's eight". |
| 5: small points | Yes | Header now says "about 25 seconds" (my run: 22.3 s). (a)'s range 0.09616 up to 0.09725 is given in E-004 and S-002; my exact fractions give 0.09615844 and 0.09725489. The earlier review's sentence is a review record, rightly left alone. |

## Findings

**1. Blocking, small. The extra second looks under (b) are given as a ceiling over nine shares, and the real ceiling is higher.**
- Where: /home/user/ml-fixed-264/experiments/E-004.md:124, "So at these nine shares (b) takes the second look as often as (a) or more often: for a method that does nothing by at most 0.0123 ..., and for a true halving by at most 0.0315". And /home/user/ml-fixed-264/specs/S-002.md:10, "takes the second look, with its 60 more pieces, up to about 3 in 100 more often at the nine starting shares worked out".
- The Definer's scratch figures are right. Over every share from 0.0001 to 0.9999 by 0.0001:
  - True halving: largest gap 0.0367, flat from about 0.547 to 0.549 (0.2652 against 0.2285 at 0.548).
  - Does nothing: largest gap 0.0131, at about 0.427 and at its mirror, about 0.573 (0.3964 against 0.3833). The Definer named 0.573 only.
  - The gap is never negative at any share. So "as often as (a) or more often" holds everywhere, not only at the nine.
- Command: `PYTHONDONTWRITEBYTECODE=1 python3 -I /tmp/claude-0/-home-user/050cc2ca-c3a4-5015-8eb5-9c67e3cf5108/scratchpad/rv264/chk.py`
- Output:
  - `2nd look (b)-(a), does nothing: max 0.01311 at [0.4264 ... 0.4269, 0.5731 ... 0.5736]; min 0.000000`
  - `2nd look (b)-(a), halving: max 0.03667 at [0.5473 ... 0.549]; min 0.000000`
  - `shares with halving gap > 0.0315: (0.5013, 0.5996, 984)`
  - `shares with halving gap > 0.035: [(0.5219, 0.5757)]`
  - `shares with null gap > 0.0123: [(0.3992, 0.4612), (0.5388, 0.6008)]`
- Why it is not fair as it stands:
  - The nine shares sit at the two edges of the hump. At almost every share between 1 in 2 and 6 in 10 the halving gap is larger than the "at most 0.0315" stated.
  - In S-002.md:10 the two neighbouring figures ("up to about 0.106", "up to about 1 in 100 less often") are ceilings over all shares. The third "up to" is not, and the owner reads the three together. The true figure rounds to about 4 in 100, not 3.
  - The tilt is toward (b): its cost looks smaller than its worst. Round 1 failed a wording that made (a) look worse than it is. The same standard applies here, in the text the owner rules from.
  - The wording is honest about its limit ("at these nine shares"), which is why this is small. It is not false.
- Fair wording across all shares, for E-004: "At every starting share (b) takes the second look as often as (a) or more often: for a method that does nothing by at most about 0.013 (near starting shares of 0.43 and 0.57), and for a true halving by at most about 0.037 (near 0.55; 0.2652 against 0.2285). At the nine shares listed the largest gaps are 0.0123 and 0.0314."
- For S-002: "takes the second look, with its 60 more pieces, up to about 4 in 100 more often".
- These figures are not in line-output.txt. E-004 says its figures come from line.py and its output. So the fix needs line.py to print the two ceilings and their shares, with the output re-recorded and run again by someone other than the Definer.

**2. Not blocking. "at most 0.0315" is 0.0314.**
- The unrounded figures at 6 in 10 are 0.222169 and 0.190730; the gap is 0.03144. At 1 in 2: 0.300552 and 0.269315; gap 0.03124.
- 0.0315 is the difference of the two rounded figures. The sentence also sets the 1 in 2 pair (gap 0.0312) beside "at most 0.0315" as if equal.
- Output: `0.6 0.190730 0.222169`, `0.5 0.269315 0.300552`.

**3. Not blocking. Three statements in E-004 are true but are not in line-output.txt.**
- E-004.md:121 says the versions come "from line.py and its output".
- Not printed by line.py: (a)'s range of lines (0.09616 up to 0.09725); the mirror shares 0.368, 0.3316 and 0.657; the lower band edge figures "about 0.31 to 0.43" are printed, so those are fine.
- All three are correct by my sums (Verified 3). The mirrors follow from swapping the two outcomes. If line.py is touched for finding 1, it could print these as well.

**4. No finding. Every other changed sentence checks out.**
- E-004.md:122 (a): nine does-nothing figures, nine halving figures, 0.1063 at 0.368 and 0.632, the two bands, "not ... outside them". Correct.
- E-004.md:123 (b): nine and nine figures, 0.0982 at 0.3316 and 0.6684, next line 0.09359 reaching 0.1009 at 0.343 and 0.657, "0.0000 to 0.0097 less often". Correct (my worst gap: -0.00970 at 0.2984; never positive).
- E-004.md:124: all 36 second-look figures correct. "0.0123 (at 4 in 10 and 6 in 10)" correct (0.01235). "60 more pieces, a second wait of 30 days and 5 more short reads" matches E-004's steps and docs/projects/P-002.md:187.
- E-004.md:125: A1, A3, A5, A6 match the script's header. The grouping of A2, A4, A7, A8 is right.
- S-002.md:87: both ranges, the two bands, and the list of what E-004 holds are correct.
- Neither file recommends a line (S-002.md:10 "This plan does not choose"; S-002.md:196; E-004.md:10).
- line.py's change is print-only: the band grouping and the header's run time. The diff of 9d8710b touches no computation.

**5. The v2.5.1 section 12 reviewer checklist, item by item.**
1. Mechanism, not just passing tests: yes. No hard-coded output; line.py's figures match an independent exact computation.
2. Test-file changes: none in 9d8710b.
3. Likeliest failures: a wrong figure reaching the owner's card (covered by this run); a peak hiding between listed shares (this is finding 1); a peak hiding between grid points (covered in round 1, gap at most 0.000116).
4. New dependencies, permissions, network calls: none. line.py still imports only numpy and math.comb.
5. Active rulings: none violated that I found. No line recommended.
6. Redesign: not applicable.
7. Surface: `python3 governance/checks/surface_guard.py diff --range 9d8710b^..9d8710b --branch build/definer/p002-two-look-wording` gives `OK: 1 commit(s) ... checked (0 merge(s) skipped, 0 exempt, 0 human)`. Author `definer <definer@agents.invalid>`, trailers `Agent-Session: session_01QBwHGN6YeYid8ERiP8HY5Z/definer-263` and `Spec: S-002`.
- PR body: none was in my manifest, so the "What this means for you" rule had nothing to apply to. I could not check it. See open question 3.
- Join-up section: not applicable; no screens or views.

## Six-part contract

**Changed (by file).** Nothing in any repository. Scratch only, under /tmp/claude-0/-home-user/050cc2ca-c3a4-5015-8eb5-9c67e3cf5108/scratchpad/rv264/: chk.py, chk.out, run2.txt.

**Why.** Brief 264: round 2 of the independent run, after the Definer's commit 9d8710b.

**Verified (command and output).**
1. Re-run. `PYTHONDONTWRITEBYTECODE=1 python3 -I experiments/E-004/line.py`, output saved to scratch, then `diff` against experiments/E-004/line-output.txt: `IDENTICAL`, in 22.3 s.
2. Scope of the change. `git diff 9d8710b^ 9d8710b --stat`: E-004.md, line-output.txt, line.py, S-002.md, 17 insertions and 8 deletions. `git diff 9d8710b ee6ebc3 --stat`: only docs/briefs/263-definer.md.
3. Own sums (chk.py, written fresh this round). Fisher p-values by whole-number counts compared as exact fractions; the pass regions built from critical counts, not from line.py's tables; every share from 0.0001 to 0.9999. Output:
   - `range (a): 0.096158 up to 0.097255` (exactly 0.09615844 and 0.09725489); `range (b): 0.092274 up to 0.093594`
   - All nine rows of does-nothing passes, halving passes and both second-look columns equal line-output.txt to four places.
   - `(a) worst null [(0.10634, 0.632), (0.10634, 0.368) ...] bands [[0.3068, 0.4293], [0.5707, 0.6932]]`
   - `(b) worst null [(0.09818, 0.3316), (0.09818, 0.6684) ...] bands []`
   - `next line worst null [(0.10086, 0.3427), (0.10086, 0.6573) ...] at .343 0.10086 at .657 0.10086`
   - `halving pass (b)-(a): min -0.00970 at 0.2984, max 0.00000`
   - Second-look gaps: as quoted under finding 1.
   - `at 0.548 ... halving (a)(b) 0.2285 0.2652 diff 0.03667`; `at 0.573 null (a)(b) 0.3833 0.3964 diff 0.01311`; `at 0.427 null (a)(b) 0.3833 0.3964 diff 0.01311`
4. Surface guard: OK, as in finding 5.

**Undone.**
- No seeded simulation this round. Round 1's simulation covered the pass figures. The second-look figures rest on my exact sums and line.py agreeing; they need only look 1's counts, so the sum is simple.
- The second-look ceilings are on a 0.0001 grid. Both peaks are flat across several grid points, so I treat them as settled to four places.
- I did not check docs/projects/P-002.md or any card for the second-look wording; none states it yet.
- I did not test A1 or A6 failing, as in round 1.

**Needed outside my surface.**
- The Definer: state the second-look gap across all shares in E-004.md:124 and S-002.md:10 (finding 1); have line.py print the two ceilings and their shares and re-record the output; correct 0.0315 to 0.0314 if the nine-share figure is kept (finding 2); optionally print (a)'s range and the mirror shares (finding 3).
- The Chief of Staff, for the card: use "up to about 4 in 100 more often for a true halving, about 1 in 100 for a method that does nothing", not the nine-share figures.
- A further independent run of line.py's new output lines, if they are added.

**Open questions.**
1. Is finding 1 blocking in the orchestrator's eyes? The sentences are true as qualified. I rated it blocking because the owner will read "up to" as a ceiling and the neighbouring figures are ceilings over all shares.
2. If the ceilings go into line.py, should it also print the share ranges where the gap exceeds the nine-share figures (halving: 0.501 to 0.600)?
3. My standing instructions name docs/archive/OPERATING_MODEL_v2.5.1.md section 12. That file is not in this copy; I read it at /home/user/Personal-Org-Operating-Model/docs/archive/OPERATING_MODEL_v2.5.1.md. They also make a missing "What this means for you" opening in a PR body a FAIL. No PR body was given to me. If one exists for this work, it still needs that check.

## Round 3 (commit 5448c15)

Verdict: PASS

Round 3 passes. The Definer's change fixes all three of my round 2 findings, and I could not refute any of it. line.py's recorded output reproduces exactly. The first 25 lines are the same as at 1e9eab7, and the change to the script only adds code at the end. Every new output line, and every changed sentence in E-004 and S-002, matches sums I wrote fresh this round across every share from 0.0001 to 0.9999. The Definer's one change outside its brief, 0.0123 to 0.0124, is right: the exact figure is 0.01235056. Round 2 was wrong to accept 0.0123. One thing went wrong on my side. The guard script left one Python bytecode file in the copy, because the run recipe in my instructions does not stop that (finding 6). It changes nothing in the work, but the copy is no longer exactly as handed out. I recommend neither line. Since this round passes, S-002's three-round stop rule is not reached and nothing goes to the owner with Triage on this account.

Fixed copy: /home/user/ml-fixed-266 at 5448c15. `git status --short | wc -l` gives 0. One ignored file was written there (finding 6).

## Part 1. Round 2 findings against e5bf003

| Round 2 finding | Answered? | Evidence |
|---|---|---|
| 1 (blocking): second-look gap given as a ceiling over nine shares only | Yes | E-004.md:124 now says "at every starting share from 0.0001 to 0.9999 ... never less often": 0.0131 for a method that does nothing (near 0.43 and 0.57; 0.3964 against 0.3833 at 0.5734) and 0.0367 for a true halving (near 0.55; 0.2651 against 0.2284 at 0.5482). The nine-share figures are kept and labelled as such. S-002.md:10 now says "up to about 4 in 100 more often", with the nine-share limit removed. line-output.txt:41-45 prints both ceilings, the shares around each one and a not-negative check. |
| 2: 0.0315 should be 0.0314, and the 1-in-2 pair should not be set beside it as equal | Yes | E-004 says "0.0314 ... (0.2222 against 0.1907 at 6 in 10; at 1 in 2 the gap is 0.0312, 0.3006 against 0.2693)". |
| 3: three E-004 figures were missing from line-output.txt | Yes | line-output.txt:27-33 now prints (a)'s range of lines (0.09616 up to 0.09725) and each worst case at both of its shares (0.632/0.368, 0.6684/0.3316, 0.343/0.657). |

## Findings

**1. Not blocking. Re-run matches, and the change only adds code.**
- `time (PYTHONDONTWRITEBYTECODE=1 python3 -I experiments/E-004/line.py > rv266/run3.txt); diff rv266/run3.txt experiments/E-004/line-output.txt && echo IDENTICAL` gives `real 0m18.714s` and `IDENTICAL`.
- `head -25 experiments/E-004/line-output.txt | diff - <(git show 1e9eab7:experiments/E-004/line-output.txt | head -25)` gives `FIRST25_SAME_AS_1e9eab7`. The old file had 25 lines; the new one has 45.
- `git diff 1e9eab7 e5bf003 -- experiments/E-004/line.py | grep -E '^-[^-]'` returns nothing, so no line was removed or changed. All 64 added lines come after the last earlier print, at line 173.
- What the added code does:
  - a new function `second_look` (the look-1 part of the sum in `passes`);
  - new names `a_low`, `a_next`, `Rn`, `FINE`;
  - asserts that `second_look` equals `passes(...)[1]` at the nine shares;
  - prints.
- It reassigns no name used earlier, so the brief's "change no existing computation; additions to line.py print only" holds.

**2. Not blocking. Every new line of line-output.txt matches my own sums.**
- Command: `PYTHONDONTWRITEBYTECODE=1 python3 -I rv266/own.py`.
- How own.py works, written fresh with no code from line.py:
  - Fisher p-values are exact `Fraction`s, and the pass regions are built from them.
  - The nine-share second-look chances are exact rationals.
  - The 0.0001 sweep is in floats over regions built from those fractions.
- Output:
  - Lines: `(a) decides as any line from 0.09615844 up to, not incl., 0.09725489` and `(b) ... 0.09227380 up to, not incl., 0.09359355`.
  - Worst cases: `a 0.09700 [(0.632, 0.10634), (0.368, 0.10634)]`, `b 0.09227 [(0.6684, 0.09818), (0.3316, 0.09818)]`, `next 0.09359 [(0.343, 0.10086), (0.657, 0.10086)]`.
  - All 18 nine-share pairs match line-output.txt:36-39 to six places. For example, `nothing 0.4 (a) 0.380756 (b) 0.393106 gap 0.01235056`, `halving 0.6 (a) 0.190730 (b) 0.222169 gap 0.03143943` and `halving 0.5 ... gap 0.03123659`. Printed "+0.000014" for nothing at 0.2 is exactly 0.00001357. Printed "+0.000000" for halving at 0.2 is exactly 0.00000030.
  - Every share: `nothing max 0.013113 at 0.5734 (a) 0.3833 (b) 0.3964; ... near-max from 0.4244 to 0.5756 n=92; gaps of near list: [(0.4289, 0.5711)]`, which matches "0.4244 to 0.4289 and 0.5711 to 0.5756". `halving max 0.036673 at 0.5482 (a) 0.2284 (b) 0.2651; near-max from 0.5468 to 0.5496`, which also matches.
  - Never negative: `R1b subset of R1a: True cells in gap set: 4`. Under (b) the trial passes at look 1 only where (a) also passes, so (b)'s second-look set always contains (a)'s. The gap therefore cannot be negative at any share; this follows from how the rules are built. Float minimum `-1.11e-16` is rounding noise, below line.py's `-1e-12` cutoff.

**3. Not blocking. Every changed sentence is correct.**
- E-004.md:124: every figure matches finding 2. Rounding at 0.548 against 0.5482 explains the small differences from round 2's quoted figures (0.2652/0.2285 at 0.548; 0.2651/0.2284 at 0.5482). Own output: `at 0.548 (a) 0.2285 (b) 0.2652`.
- S-002.md:10: "up to about 4 in 100 more often" fits 0.0367, and it now matches the two neighbouring "up to" figures, which are ceilings over all shares.
- Neither file recommends a line (E-004.md:10 "it does not choose or recommend"; S-002.md:10 "This plan does not choose").
- Search for stale figures: `grep -rn "0\.0123\b\|0\.0315\|3 in 100 more often"` outside reviews/ and briefs/ returns nothing.

**4. Not blocking. My ruling on the Definer's change outside its brief (0.0123 to 0.0124): accept it.**
- Exact gap at 4 in 10 and 6 in 10: 0.01235056 (finding 2 output). To four places that is 0.0124.
- The old 0.0123 was the difference of the two rounded figures (0.3931 − 0.3808). That is the same fault as round 2's finding 2 (0.0315 against 0.0314), in the other direction.
- Round 2 itself wrongly said "0.0123 (at 4 in 10 and 6 in 10) correct (0.01235)". That was my error: 0.01235 rounds up.
- The change is outside the brief's wording, which named only 0.0314, but it is the same kind of fix, it is correct, and it touches none of the four files the brief excluded. The Definer's commit message states it.
- Side effect, not blocking: E-004's rounded lists show 0.3808 and 0.3931, which differ by 0.0123, and 0.1907 and 0.2222, which differ by 0.0315. A careful reader may notice the stated gaps differ from those by 0.0001. Both stated gaps are right.

**5. Not blocking, wording. "(the script's grid)" is a little loose.**
- E-004.md:124 says "every starting share from 0.0001 to 0.9999, in steps of 0.0001 (the script's grid)".
- line.py's `GRID` is 0.001 to 0.999 (line.py:39). The 0.0001 sweep is a separate `FINE` list (line.py:217). Header assumption A7 (line.py:30-32) does not mention it.
- The figures are right either way. A7 could name the second-look sweep.

**6. Not blocking for the work, but a breach of my brief: I wrote one file in the copy.**
- `governance/checks/__pycache__/govlib.cpython-313.pyc`, 20:31:04 UTC. It was created when I ran `PYTHONDONTWRITEBYTECODE=1 python3 -I governance/checks/surface_guard.py ...`.
- Cause: `-I` implies `-E`, so Python ignores every `PYTHON*` variable, including `PYTHONDONTWRITEBYTECODE`. line.py imports no local module and so left nothing; surface_guard imports govlib.
- The file is git-ignored (`git status --short --ignored` shows `!! governance/checks/__pycache__/`), so `git status --short` still gives 0. I did not delete it, because the brief says write nothing in the copy.
- Use `python3 -I -B` instead. Earlier rounds that ran the guard the same way may have left the same file in their copies.

**7. The v2.5.1 §12 reviewer checklist, item by item.**
1. Does the work do what it claims, or only pass tests? It does. Nothing is hard-coded, and every printed figure matches an independent exact computation (finding 2).
2. Test-file changes: none. line.py's new asserts only add a check.
3. Likeliest failures:
   - A wrong figure reaching the owner's card: covered by findings 2 and 3.
   - A ceiling hiding between the nine shares: fixed (Part 1, item 1).
   - A peak hiding between grid points: both peaks are flat over 29 or more grid points (finding 2).
4. New dependencies, permissions or network calls: none. The imports are still only numpy and math.comb.
5. Active rulings: none violated that I found. No line is recommended. S-002 is still `status: draft` (S-002.md:3), so editing it needs no superseding entry.
6. Redesign: not applicable.
7. Surface: `python3 governance/checks/surface_guard.py diff --range e5bf003^..e5bf003 --branch build/definer/p002-two-look-ceilings` gives `OK: 1 commit(s) in e5bf003^..e5bf003 checked (0 merge(s) skipped, 0 exempt, 0 human)`, rc=0.
   - Author: `definer <definer@agents.invalid>`.
   - Trailers: `Agent-Session: session_01QBwHGJm2otqFdQxgZQ1fyx/definer-265` and `Spec: S-002`.
   - Files: exactly the four the brief allows. `git diff e5bf003 5448c15 --stat` shows only docs/briefs/265-definer.md and a Chief of Staff session-lines file.

Other charter items:
- PR body ("What this means for you") and Tasks: my manifest holds no PR. The merge 5448c15 is local and its message is a title plus an `Agent-Session:` trailer, with no PR body. The rule had nothing to apply to, so it is not a FAIL here (open question 2).
- Join-up section: not applicable, since this work has no screens or views.
- S-002's opening summary is plain English.

## Six-part contract

**Changed (by file).**
- In the repositories: nothing on purpose. The one file left by accident is /home/user/ml-fixed-266/governance/checks/__pycache__/govlib.cpython-313.pyc (finding 6).
- Scratch files in /tmp/claude-0/-home-user/05f0729c-59b7-568d-bab0-5a59dfde631a/scratchpad/rv266/:
  - own.py and own.out (my own sums);
  - run3.txt (the re-run);
  - out-1e9eab7.txt (the earlier recorded output).

**Why.** Brief 266: round 3, the last before S-002's stop rule, reviewing the Definer's commit e5bf003 (brief 265).

**Verified.** Findings 1 to 3 and 7, each with its command and output:
- the re-run matches exactly (18.7 s);
- the first 25 lines are unchanged from 1e9eab7, and from 9d8710b;
- the line.py diff only adds code;
- my exact sums match every new line and every changed sentence;
- the surface guard gives OK.

**Undone.**
- No seeded simulation this round. The pass figures were simulated in round 1, and the second-look chances need only look-1 counts, which I summed exactly at the nine shares.
- I did not run `governance/checks/check_all.sh`, which the brief does not ask for and which would likely write more bytecode.
- As in earlier rounds, I did not test assumptions A1 or A6 failing.
- I did not remove the bytecode file (finding 6).

**Needed outside my surface.**
- Orchestrator: delete /home/user/ml-fixed-266/governance/checks/__pycache__/ if the copy must stay as handed out. Correct the Python recipe in future reviewer briefs to `python3 -I -B`.
- Optionally, the Definer: have A7 in line.py's header name the 0.0001 second-look sweep (finding 5).
- Chief of Staff, for the card: use "up to about 4 in 100 more often for a true halving, about 1 in 100 for a method that does nothing", from E-004.md:124.

**Open questions.**
1. Round 2 accepted 0.0123 in error (finding 4). Should the review record carry a note against round 2's line, or is this round's ruling enough?
2. My standing instructions make a PR body without a "What this means for you" opening a FAIL. No PR body for this work was in my manifest. If a PR is opened to land 5448c15, it still needs that check, and the Tasks tick check.
3. My standing instructions say this repository keeps v2.5.1's process (L-0112). L-0112 applies that to v2.x projects. Model-Lab's AGENTS.md:1 calls it a v3 project, and governance/OPERATING_MODEL_VERSION says 3.7.2. I applied both the v2.5.1 §12 checklist and the v3 charter items. Which one governs should be settled.
