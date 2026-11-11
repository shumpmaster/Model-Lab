Verdict: FAIL

*The Reviewer's independent run of the odds behind P-002's value target (intake/P-002-value-target-odds-2026-11-10.md): round 1 (FAIL), brief 244. A fresh session on a different model from the Chief of Staff's sessions that wrote the scripts, started by the Chief of Staff (session_01QBwHGJRsdA6DND96m5Z9xE), 2026-11-11, on the fixed copy Model-Lab@565aa90. Recorded verbatim by the Orchestrator from the helper's return; the round's own verdict line is recorded as "The round's verdict was …" (LL-68). The verdict above is the latest round's. Its scripts and outputs were in the session's scratch folder and are not kept here; the second-way script is in the return below. The return's two second-level headings are recorded one level lower, and the last heading's full scratch path is shortened to S/second.py, so the record nests under its round.*

## Round 1 (brief 244)

The round's verdict was FAIL.

The scripts reproduce every recorded line, and my second way agrees with all the figures I checked. The FAIL rests on one code-against-words mismatch in round3.py (finding 2) and on one quoted figure that is rounded down at the ruled line (finding 4).

Working directory for everything: /tmp/claude-0/-home-user/3632fc02-3869-5237-84a8-30f3cf85b850/scratchpad/odds-244/ (called S below). Nothing was written under /home/user/ml-odds-244/.

Limit on item 4: the question cards (questions/P-002-value-target.md and questions/P-002-trial-gates.md, in PRs #90 and #91) are not in the fixed copy. I could read only what quotes them: the two decisions files, docs/projects/P-002.md section 6, and the Critic's figure tables in reviews/P-002-value-target/critic.md and reviews/P-002-trial-gates/critic.md. The two decisions files quote almost no odds figures. The figures sit in section 6 and on the cards.

### Findings

1. **Re-run (non-blocking, clean).**
   - Command: I extracted the five python blocks from the intake item by regex, with no retyping, into S/run/. twolook_lib.py is twolook.py's text up to and including `return keep,second`. I ran each as `python3 -I <name>.py` from S/run and compared line by line against the item's recorded output.
   - Result: power 12/12, twolook 15/15, twolook2 8/8, holdup 12/12, round3 15/15 lines. All IDENTICAL, with zero differing lines.
   - The scripts ran as written, with no change. twolook2, holdup and round3 use `sys.path.insert(0,'.')`, so they must be run from the directory holding twolook_lib.py. This is not stated in the item.
   - Timings: twolook.py took about 5s and the others under 0.4s.

2. **Code against words (LL-54): one mismatch, blocking by the stated rule, small in size.**
   - round3.py, the comment at part 3 and the printed line "HOLD-UP, two looks ... up to 0.20", say "worst shares from holdup.py: 0.118 (60% fault) and 0.095 (20%)".
   - The worst two figures in holdup.py's output are 0.118 (60%) and 0.115 (50%). `1-(1-0.118)*(1-0.115)` = 0.219, which is about 0.22, not 0.20. The 0.095 row is not the worst.
   - The Critic noted this ("0.22") at round 3, but the script and its output were not changed.
   - Part 3 prints a hard-coded figure and is not computed from holdup.py. Only a "worst" label that does not match the code is wrong. If one check really sits at 20% and the other at 60%, then 0.20 is the right figure for that pairing, but the code does not say so.
   - Effect on five drops: round3.py uses H=0.80. At H=0.78 the five-drop figures move by 0.00 to 0.01 in every row (S/sweep.py: 0.07 becomes 0.08, 0.47 becomes 0.48, 0.15 becomes 0.16, and so on). The rounded figures in section 6 ("1 to 4 in 10; 5 to 8 in 10") do not change.
   - Everything else matches its words:
     - power.py: `hyper_p(x1,n,n,x1+x0) <= alpha` is P(method count ≤ observed), so one-sided and the method needing the owner less often. The false-keep arm uses p0 for both arms, as it should.
     - two_look: it goes on only when `x<y` (method arm count lower) and the check at look 1 did not clear. The same `a` is used at both looks. The second test pools x+u against y+v at 60 per arm.
     - The line-selection loop in twolook.py takes the largest a in steps of 0.001 with false keep at most the target. The 1-in-40 target gives 0.022 at the 50% start.
     - twolook.py's printed 0.45 for 1 in 40 at the 30% start (line 0.025) against twolook2.py's 0.43 (line 0.022) is two different lines, not a discrepancy.
     - holdup.py calls one_look on the fault-free shares (1-f0, 1-f1), so the harm direction is correct. Its two-look guard function does fail-at-look-1 or (pass and then fail at 60). That is a valid upper bound for "every trial goes on".
     - round3.py target_met is `2*x<=y and cdf<=a` with x the latest count and y the starting count, which is the rule in words. The five-drops code is `(1-H*(pi*real+(1-pi)*null))**5`, which matches.

3. **Second way (non-blocking, agrees).**
   - Command: `python3 -I S/second.py`. Written from the words, in exact integer and Fraction arithmetic with the line compared as an integer ratio, plus seeded simulations of N=300,000 runs per figure. The margins below are 95% (1.96 SE). The full script is under "Second-way script" below. It took 42s.
   - One look at 30 per arm, exact against simulation:

     | Start | Line | Real halving kept (exact / sim ±margin) | No-effect kept (exact / sim ±margin) |
     |---|---|---|---|
     | 50% | 1 in 10 | 0.7120 / 0.7112 ±0.0016 | 0.0775 / 0.0779 ±0.0010 |
     | 50% | 1 in 40 | 0.4132 / 0.4139 ±0.0018 | 0.0137 / 0.0135 ±0.0004 |
     | 30% | 1 in 10 | 0.4204 / 0.4205 ±0.0018 | 0.0615 / 0.0620 ±0.0009 |
     | 30% | 1 in 40 | 0.1917 / 0.1921 ±0.0014 | 0.0131 / 0.0132 ±0.0004 |

     The item records 0.71/0.078, 0.41/0.014, 0.42/0.061, 0.19/0.013, so these agree.
   - Two looks at line 0.097, exact against simulation:

     | Start | No-effect kept (exact / sim ±margin) | Real halving kept (exact / sim ±margin) |
     |---|---|---|
     | 50% | 0.0933 / 0.0929 ±0.0010 | 0.9231 / 0.9232 ±0.0010 |
     | 30% | 0.0989 / 0.0988 ±0.0011 | 0.7009 / 0.7012 ±0.0016 |

     Second trial run: real 0.269 and 0.478, no-effect 0.389 and 0.383, all matching the item (0.27, 0.48, 0.39, 0.38).
   - Two looks at line 0.022:

     | Start | No-effect kept (exact / sim ±margin) | Real halving kept (exact / sim ±margin) |
     |---|---|---|
     | 50% | 0.0242 / 0.0239 ±0.0005 | 0.7703 / 0.7693 ±0.0015 |
     | 30% | 0.0215 / 0.0213 ±0.0005 | 0.4290 / 0.4292 ±0.0018 |

     These agree with the item (0.024, 0.77, 0.021, 0.43).
   - Target, 60 pieces each period:

     | Start | Line | Real halving met (exact / sim ±margin) | No change met (exact) |
     |---|---|---|---|
     | 50% | 1 in 10 | 0.5321 / 0.5319 ±0.0018 | 0.0003 |
     | 50% | 1 in 40 | 0.5319 | 0.0003 |
     | 30% | 1 in 10 | 0.5362 / 0.5364 ±0.0018 | 0.0119 |
     | 30% | 1 in 40 | 0.4122 / 0.4121 ±0.0018 | 0.0099 |

     The item records 0.53, 0.53, 0.54, 0.41 for real halving and 0.000, 0.000, 0.012, 0.010 for no change. All agree. The no-change 0.0003 prints as "0.000", which is fine.
   - Hold-up rows, from my own code with the same tests:
     - Harm caught at 30 per arm, 10% to 20%: exact 0.3023, simulation 0.3017 ±0.0016 (item 0.30).
     - Harm caught at 60 per arm, 10% to 20%: 0.4935 (item 0.49).
     - Harmless, 50% fault share, one look: 0.0775 (item 0.078).
     - Harmless two-look upper bound: 0.1183 at 60% and 0.0804 at 10% (item 0.118 and 0.080).
   - Beyond the item's wording, I swept the two-look false keep across starting shares (S/sweep.py), with the line fixed at 0.097 and 0.022:

     | Start share | False keep at 0.097 | False keep at 0.022 |
     |---|---|---|
     | 0.05 | 0.041 | 0.0056 |
     | 0.1 | 0.0677 | 0.0138 |
     | 0.2 | 0.0908 | 0.0202 |
     | 0.3 | 0.0989 | 0.0215 |
     | 0.4 | **0.1043** | 0.0238 |
     | 0.5 | 0.0933 | 0.0242 |
     | 0.6 | **0.1043** | 0.0238 |
     | 0.7 | 0.0989 | 0.0215 |
     | 0.8 | 0.0908 | 0.0202 |
     | 0.9 | 0.0677 | 0.0138 |

     So the 1-in-10 two-look line is not "at most 1 in 10" at every start. It reaches 0.104 at starts of 40% and 60%. The item scoped its claim to "either starting share shown", so the item is accurate. The wider "stays at 1 in 10" in section 6 holds only as "about 1 in 10". The 1-in-40 line holds at every start (maximum 0.0242).

4. **Quoted figures at the ruled 1 in 10 line.**
   - **Blocking, small: "A real halving shows on the count only about 4 to 5 times in 10" (section 6, Miss).**
     - At the ruled 1 in 10 line the figures are 0.53 and 0.54 (exact 0.5321 and 0.5362), which is "about 5 in 10". The 0.41 that makes it "4" is the 1-in-40 line at a 30% start, which the owner did not rule.
     - The rounding is down, which makes a miss look like weaker evidence than it is at the ruled line.
     - The figure also covers only the count test. V1 also requires the work to hold up, which would lower the chance of meeting V1 as a whole. That is not modelled, and the item says "on the count".
     - Fair wording: "about 5 times in 10 (0.53 to 0.54 at a line of 1 in 10)".
   - **Non-blocking: "up to 1 in 5" with two looks for the hold-up checks.**
     - The honest bound is 0.22, which is about 1 in 4.5, and that is on the owner-facing side of the rounding. This is finding 2 again. "1 in 7" for one look is fair (0.145 = 1 in 6.9).
   - **Non-blocking: "the overall chance stays at 1 in 10" (section 6 and the card).**
     - It is 0.093 to 0.099 at the two shares shown and 0.104 at 40% or 60%, so it should read "about 1 in 10". The starting share is unknown until counted.
   - **Fair as quoted.**
     - 0.71 and 0.42 are "about 7 and 4 in 10".
     - 0.92 and 0.70 are "9 and 7".
     - 0.27 to 0.48 are "3 to 5 in 10 go on".
     - Harm caught 0.30 to 0.71 and 0.49 to 0.93 are "3 to 7 in 10" and "5 to 9".
     - The errors-per-10 table: 0.08 and 0.30; 9 x 0.093 = 0.84 and 9 x 0.099 = 0.89; 0.23 and 0.57; 0.19 and 0.22; 0.40 and 1.50; 0.47 and 0.50; 1.15 and 2.85; 0.11 and 0.12. All match twolook2's output to rounding.
     - Five drops: "1 to 4 in 10" (0.07 to 0.37) and "5 to 8 in 10" (0.47 to 0.77).
   - The five-drops figures include a hold-up pass rate of 0.80 for harmless or helpful methods. This is a separate guess, not a measured value (see assumptions).

5. **Assumptions the figures rest on, and which would move a ruled figure.**
   1. **Randomised assignment (coin toss or shuffle) with Fisher's exact test.** The false-keep figures then hold whether or not pieces are independent. The power, target and hold-up figures do assume independent pieces and a fixed per-piece chance.
      - If pieces vary in difficulty (they cluster by kind, repo or week), the counts become over-dispersed, so detect figures (0.71, 0.92, and so on) fall. The false-keep figures stay valid for randomised trials.
      - The target test compares two non-randomised periods as independent samples, so drift between periods, and any difference in pieces over time, is not modelled. This could raise or lower the chance of meeting the target, and could produce a spurious pass.
   2. **A halving to exactly half, with the starting share known.** The target figures use true starting shares of 50% and 30%. At lower starts they fall (the Critic's 6-of-60 case). The stop rule at a starting count under 6 of 60 is the guard, but the figure the owner ruled on is higher than the true figure at low starts. The direction is lower.
   3. **Detect figures assume the method is a full halving.** A smaller real effect gives lower detect rates.
   4. **The two-look line was tuned at 50% and 30% starts only.** It exceeds 1 in 10 at 40% and 60% (0.104). If the real start sits there, the false keep is slightly higher, by 0.004.
   5. **The two hold-up checks are independent.** Positively correlated checks would lower the chance that a harmless method fails at least one (so "1 in 7 to 1 in 5" is too high). Negatively correlated would raise it.
   6. **The hold-up fault shares are assumed (10% to 60%).** The real shares are unknown, and the true share could be higher or lower. The figures of 0.095 to 0.118 per check drive H=0.80.
   7. **H=0.80, and that the hold-up pass is independent of the keep result.** A lower H (0.78 if the worst shares apply) raises five-drops slightly. A helpful method that also does worse on a check would be a correlation not modelled.
   8. **Trials are independent for the five-drops figure, with fixed shares of real methods.** The shares of real methods are unknown illustrations (50% and 10%). The real share of methods that help could be much lower, which raises the chance of five drops.
   9. **Sampling the pieces without weighting.** A "piece" is a merged pull request, treated as exchangeable. Any rule that lets the owner's attention vary by piece, or lets the log of touches be unreliable, would bias the starting figure.

6. **Contract (non-findings).**
   - **Changed:** nothing in any repository. I wrote only S/run/ (the extracted scripts and outputs), S/second.py and S/sweep.py.
   - **Why:** to re-run the item's scripts, check them a second way, and check quoted figures.
   - **Verified:** items 1 and 3 above, by command. Item 2 by reading the code against the item's words. Item 4 by comparing quoted figures to my output and the item's output.
   - **Undone:** the question cards (questions/P-002-*.md, PRs #90 and #91) were not in the copy, so I could not check their own wording. I checked the Critic's quoted figures from them instead.
   - **Needed outside my surface:** the intake item's round3.py hold-up line (or its comment) needs correcting by its owner, and section 6's "4 to 5 times in 10" needs rewording by its owner. I cannot fix either.
   - **Open questions:** (a) was "up to 0.20" meant to pair 60% with 20% on purpose, or to be the worst case? (b) Should the target figure be restated with the hold-up half of V1 included? (c) Should the two-look line be re-set so the false keep stays at most 1 in 10 at every starting share, rather than at two?

### Second-way script (full text of S/second.py)

```python
# Second way: written from the item's words. Exact integer arithmetic (no floats in the
# probabilities or the line comparison) + seeded simulation of the same rules.
# Rules: 2 arms (with method M, without W) of n pieces; each piece "needs owner" w.p. pM / pW.
# Test: Fisher exact one-sided; p-value = P(M's count <= observed | total count, margins fixed);
# keep when p-value <= line. Two looks: look 1 at 30/arm; if not kept and M's count < W's count,
# add 30/arm and test all 60/arm at the same line; keep if that clears. Target: 60 vs 60, latest
# count <= half of starting count AND the fall clears the line.
import random, math
from fractions import Fraction as F
from math import comb

_rej={}
def rejtab(n,line):           # line = Fraction. rej[a][k] True if P(X<=a | k total, n per arm) <= line
    key=(n,line)
    if key in _rej: return _rej[key]
    tab=[[False]*(2*n+1) for _ in range(n+1)]
    for k in range(2*n+1):
        tot=comb(2*n,k); run=0
        for a in range(0,min(n,k)+1):
            if 0<=k-a<=n: run+=comb(n,a)*comb(n,k-a)
            tab[a][k]= (run*line.denominator <= line.numerator*tot)
        for a in range(min(n,k)+1,n+1): tab[a][k]=True
    _rej[key]=tab; return tab

def wts(n,p):                 # exact Fractions
    return [comb(n,x)*p**x*(1-p)**(n-x) for x in range(n+1)]

def one(n,pM,pW,line):
    t=rejtab(n,line); A=wts(n,pM); B=wts(n,pW)
    return sum(A[x]*B[y] for x in range(n+1) for y in range(n+1) if t[x][x+y])

def two(n,pM,pW,line):
    t1=rejtab(n,line); t2=rejtab(2*n,line); A=wts(n,pM); B=wts(n,pW)
    keep=F(0); second=F(0)
    for x in range(n+1):
        for y in range(n+1):
            w=A[x]*B[y]
            if t1[x][x+y]: keep+=w
            elif x<y:
                second+=w
                s=sum(A[u]*B[v] for u in range(n+1) for v in range(n+1) if t2[x+u][x+y+u+v])
                keep+=w*s
    return keep,second

def target(n,pNew,pOld,line):
    t=rejtab(n,line); A=wts(n,pNew); B=wts(n,pOld)
    return sum(A[x]*B[y] for x in range(n+1) for y in range(n+1) if 2*x<=y and t[x][x+y])

def sim_two(n,pM,pW,line,N,seed):
    r=random.Random(seed); t1=rejtab(n,line); t2=rejtab(2*n,line); k=0
    for _ in range(N):
        x=sum(r.random()<pM for _ in range(n)); y=sum(r.random()<pW for _ in range(n))
        if t1[x][x+y]: k+=1
        elif x<y:
            u=sum(r.random()<pM for _ in range(n)); v=sum(r.random()<pW for _ in range(n))
            if t2[x+u][x+y+u+v]: k+=1
    return k/N
def sim_one(n,pM,pW,line,N,seed):
    r=random.Random(seed); t=rejtab(n,line); k=0
    for _ in range(N):
        x=sum(r.random()<pM for _ in range(n)); y=sum(r.random()<pW for _ in range(n))
        k+=t[x][x+y]
    return k/N
def sim_target(n,pNew,pOld,line,N,seed):
    r=random.Random(seed); t=rejtab(n,line); k=0
    for _ in range(N):
        x=sum(r.random()<pNew for _ in range(n)); y=sum(r.random()<pOld for _ in range(n))
        k+= (2*x<=y and t[x][x+y])
    return k/N
def moe(p,N): return 1.96*math.sqrt(max(p,1e-9)*(1-p)/N)

N=300000
L10=F(1,10); L40=F(1,40)
print("ONE LOOK n=30")
for p0 in (F(1,2),F(3,10)):
  for nm,L in (("1/10",L10),("1/40",L40)):
    re_=float(one(30,p0/2,p0,L)); nu=float(one(30,p0,p0,L))
    sr=sim_one(30,float(p0/2),float(p0),L,N,1); sn=sim_one(30,float(p0),float(p0),L,N,2)
    print(f" start {float(p0):.0%} line {nm}: exact real {re_:.4f} (sim {sr:.4f} +-{moe(re_,N):.4f}); exact null {nu:.4f} (sim {sn:.4f} +-{moe(nu,N):.4f})")
print("TWO LOOKS n=30 then 60, line 0.097 (and 0.022)")
for L,nm in ((F(97,1000),"0.097"),(F(22,1000),"0.022")):
  for p0 in (F(1,2),F(3,10)):
    nu,s0=two(30,p0,p0,L); re_,s1=two(30,p0/2,p0,L)
    sn=sim_two(30,float(p0),float(p0),L,N,3); sr=sim_two(30,float(p0/2),float(p0),L,N,4)
    print(f" line {nm} start {float(p0):.0%}: exact null {float(nu):.4f} (sim {sn:.4f} +-{moe(float(nu),N):.4f}); exact real {float(re_):.4f} (sim {sr:.4f} +-{moe(float(re_),N):.4f}); 2nd trial real {float(s1):.3f} null {float(s0):.3f}")
print("TARGET 60 vs 60")
for p0 in (F(1,2),F(3,10)):
  for nm,L in (("1/10",L10),("1/40",L40)):
    a=float(target(60,p0/2,p0,L)); b=float(target(60,p0,p0,L))
    sa=sim_target(60,float(p0/2),float(p0),L,N,5); sb=sim_target(60,float(p0),float(p0),L,N,6)
    print(f" start {float(p0):.0%} line {nm}: exact met {a:.4f} (sim {sa:.4f} +-{moe(a,N):.4f}); no change {b:.4f} (sim {sb:.4f} +-{moe(b,N):.4f})")
print("HOLD-UP rows (harm direction: M has MORE faults; fault-free count of M fewer)")
# caught 30/arm, faults 10% -> 20%: M fault-free share 0.8, W 0.9
c=float(one(30,F(8,10),F(9,10),L10)); sc=sim_one(30,0.8,0.9,L10,N,7)
print(f" caught 30/arm 10%->20%: exact {c:.4f} (sim {sc:.4f} +-{moe(c,N):.4f})")
# harmless, fault 50% either way, one look: tested by faults directly (M faults > W faults) via mirror
h=float(one(30,F(1,2),F(1,2),L10))
print(f" harmless fault share 50% one look: {h:.4f}")
# harmless two-look guard 60% fault share, upper bound as in item (go on every time): own coding
def guard2(f,n,line):
    t1=rejtab(n,line); t2=rejtab(2*n,line); A=wts(n,f); tot=F(0)
    for x in range(n+1):
      for y in range(n+1):
        w=A[x]*A[y]
        if t1[x][x+y]: tot+=w
        else: tot+=w*sum(A[u]*A[v] for u in range(n+1) for v in range(n+1) if t2[x+u][x+y+u+v])
    return tot
# fault share 60% => fault-free share 0.4 for the M-fewer-fault-free test
print(f" harmless two-look (go on every time) fault 60%: {float(guard2(F(2,5),30,L10)):.4f}; fault 10%: {float(guard2(F(9,10),30,L10)):.4f}")
# harm caught 60/arm 10->20
print(f" caught 60/arm 10%->20%: {float(one(60,F(8,10),F(9,10),L10)):.4f}")
```

Other files: S/run/*.py and S/run/*.out (the extracted item scripts and their outputs), and S/sweep.py (the starting-share sweep and the H sensitivity).
