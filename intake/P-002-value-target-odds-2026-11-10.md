# Intake item — P-002 value-target odds, 2026-11-10

source: other (the Chief of Staff's own calculation, session_01QBwHGKirN166RhxQTHuAt9)
date: 2026-11-10

## What was reported
The detection odds quoted in questions/P-002-value-target.md, "How a trial decides". They are illustrations: the starting share of work that needs the owner is not known until the new log has counted it, so two starting shares are shown, 1 in 2 and 3 in 10, each halved by the method.

Method: each trial compares n pieces done with the method against the n pieces done just before it (unpaired). The test is Fisher's exact test, one-sided (the method's pieces need the owner less often), at a cutoff of 1 in 10 (alpha 0.10) or 1 in 40 (alpha 0.025, the prompt engine's line, docs/PROJECT.md section 6, V1). "Detect" is the chance the test clears the cutoff when the method truly halves the share; "false keep" is the chance it clears the cutoff when the method does nothing. Every outcome pair is enumerated exactly; nothing is simulated. Fisher's test is conservative, so the false-keep chance is below the cutoff.

Output (python3 -I power.py):

```
n=20/arm start=50% halved=25% alpha=1in10: detect 0.53, false keep 0.047
n=20/arm start=50% halved=25% alpha=1in40: detect 0.27, false keep 0.010
n=20/arm start=30% halved=15% alpha=1in10: detect 0.31, false keep 0.058
n=20/arm start=30% halved=15% alpha=1in40: detect 0.12, false keep 0.012
n=30/arm start=50% halved=25% alpha=1in10: detect 0.71, false keep 0.078
n=30/arm start=50% halved=25% alpha=1in40: detect 0.41, false keep 0.014
n=30/arm start=30% halved=15% alpha=1in10: detect 0.42, false keep 0.061
n=30/arm start=30% halved=15% alpha=1in40: detect 0.19, false keep 0.013
n=50/arm start=50% halved=25% alpha=1in10: detect 0.86, false keep 0.067
n=50/arm start=50% halved=25% alpha=1in40: detect 0.67, false keep 0.018
n=50/arm start=30% halved=15% alpha=1in10: detect 0.62, false keep 0.069
n=50/arm start=30% halved=15% alpha=1in40: detect 0.35, false keep 0.015
```

Script:

```python
# Exact power of a one-sided Fisher exact test (method arm needs the owner less often),
# n pieces per arm, unpaired: method pieces vs the same number before the trial.
from math import comb
def hyper_p(a,n1,n2,k):  # P(X<=a) for X ~ hypergeom: successes in arm1 given total k
    tot=comb(n1+n2,k); return sum(comb(n1,x)*comb(n2,k-x) for x in range(max(0,k-n2),a+1))/tot
def power(p0,p1,n,alpha):
    pw=0;fa=0
    for x1 in range(n+1):          # touches in method arm
        for x0 in range(n+1):      # touches in baseline arm
            sig = hyper_p(x1,n,n,x1+x0) <= alpha
            pr1=comb(n,x1)*p1**x1*(1-p1)**(n-x1); pr0=comb(n,x0)*p0**x0*(1-p0)**(n-x0)
            if sig: pw+=pr1*pr0
            q=comb(n,x1)*p0**x1*(1-p0)**(n-x1)
            if sig: fa+=q*pr0
    return pw,fa
for n in (20,30,50):
  for p0 in (0.5,0.3):
    for a in (0.10,0.025):
      pw,fa=power(p0,p0/2,n,a)
      print(f"n={n}/arm start={p0:.0%} halved={p0/2:.0%} alpha=1in{round(1/a)}: detect {pw:.2f}, false keep {fa:.3f}")
```

## Round 2 (2026-11-10, after the Critic's round 1)

The round 1 design compared each trial with the pieces done just before it; the Critic found that design lets anything else that changed between the two periods count as the method (reviews/P-002-value-target/critic.md, finding 2). Round 2 assigns each new piece of the kind by coin toss, recorded before work on it starts, to "with the method" or "without", in the same weeks. The arithmetic is the same unpaired one-sided Fisher test, enumerated exactly, at 30 pieces per arm; it assumes pieces are independent of each other.

It adds:
- **Two looks** (the card's part 3, option A). Look 1 at 30 pieces per arm. If the method is not kept there and its pieces needed the owner less often than the others ("leans the right way"), 30 more per arm are assigned and all 60 per arm are tested together. One line is used at both looks, fixed before the first piece, set so that a method that does nothing is kept at most 1 time in 10 (or 1 in 40) across both looks at either starting share shown: 0.097 for 1 in 10, 0.022 for 1 in 40.
- **The hold-up guard.** A method fails it when its pieces do worse on a check (first-time pass at the independent check, or reopened for a fault) by enough that chance alone would produce the difference at most 1 time in 10, the same test in the harm direction. The figure is how often a method that changes nothing on that check fails it by chance. With two checks, assuming they are independent, a harmless method fails at least one about 1 time in 7 (1 - 0.92 x 0.93, at the worst shares shown); the card's keep odds are before that.
- **The share of kept methods that do nothing**, if 1 method in 10 tried is real (one look).
- **Errors per 10 methods tried** (the card's part 2), from the two-look figures: with 1 in 10 tried real, at a line of 1 in 10, real ones missed 0.08 to 0.30 and useless ones kept 0.84 to 0.89 (9 x 0.093 to 9 x 0.099); at 1 in 40, missed 0.23 to 0.57, kept 0.19 to 0.22. With 5 in 10 real, at 1 in 10, missed 0.4 to 1.5, kept 0.47 to 0.50; at 1 in 40, missed 1.15 to 2.85, kept 0.11 to 0.12.

Output (python3 -I twolook.py):

```
ONE LOOK, 30 per arm
 start 50%, line 1 in 10: real halving kept 0.71; no-effect kept 0.078
 start 50%, line 1 in 40: real halving kept 0.41; no-effect kept 0.014
 start 30%, line 1 in 10: real halving kept 0.42; no-effect kept 0.061
 start 30%, line 1 in 40: real halving kept 0.19; no-effect kept 0.013
TWO LOOKS, 30 then 60 per arm, one line at both looks, chosen so no-effect kept <= target
 overall target 0.1, start 50%: line at each look 0.097; no-effect kept 0.093; real halving kept 0.92; second trial run for real 0.27, for no-effect 0.39
 overall target 0.1, start 30%: line at each look 0.1; no-effect kept 0.099; real halving kept 0.70; second trial run for real 0.48, for no-effect 0.38
 overall target 0.025, start 50%: line at each look 0.022; no-effect kept 0.024; real halving kept 0.77; second trial run for real 0.57, for no-effect 0.44
 overall target 0.025, start 30%: line at each look 0.025; no-effect kept 0.024; real halving kept 0.45; second trial run for real 0.70, for no-effect 0.43
SHARE OF KEPT METHODS THAT DO NOTHING, one look, if 1 in 10 methods tried is real
 start 50%, line 1 in 10: 0.49
 start 50%, line 1 in 40: 0.23
 start 30%, line 1 in 10: 0.57
 start 30%, line 1 in 40: 0.38
```

Output (python3 -I twolook2.py; it imports the functions above from twolook_lib.py, the first part of twolook.py):

```
1 in 10 overall, line 0.097 at each look, start 50%: no-effect kept 0.093; real halving kept 0.92; second trial: real 0.27, no-effect 0.39
1 in 10 overall, line 0.097 at each look, start 30%: no-effect kept 0.099; real halving kept 0.70; second trial: real 0.48, no-effect 0.38
1 in 40 overall, line 0.022 at each look, start 50%: no-effect kept 0.024; real halving kept 0.77; second trial: real 0.57, no-effect 0.44
1 in 40 overall, line 0.022 at each look, start 30%: no-effect kept 0.021; real halving kept 0.43; second trial: real 0.71, no-effect 0.43
hold-up guard, check failed by 60% of pieces either way: method with no effect fails it 0.073
hold-up guard, check failed by 50% of pieces either way: method with no effect fails it 0.078
hold-up guard, check failed by 20% of pieces either way: method with no effect fails it 0.055
hold-up guard, check failed by 10% of pieces either way: method with no effect fails it 0.048
```

Script twolook.py:

```python
# Exact odds for the value-target card, round 2. Pieces of one kind are assigned by coin toss to
# "with the method" or "without" in the same weeks. A piece "needs the owner" with chance p0 without
# the method and p1 with it. Test: Fisher's exact test, one-sided (with-method pieces need the owner
# less often). Every outcome is enumerated; nothing is simulated.
from math import comb
from functools import lru_cache
@lru_cache(None)
def cdf(a,n1,n2,k):  # P(X<=a), X = with-method count in a 2x2 table with fixed margins
    t=comb(n1+n2,k); return sum(comb(n1,x)*comb(n2,k-x) for x in range(max(0,k-n2),a+1))/t
def pmf(n,p): return [comb(n,x)*p**x*(1-p)**(n-x) for x in range(n+1)]
def one_look(p0,p1,n,a):
    P1,P0=pmf(n,p1),pmf(n,p0)
    return sum(P1[x]*P0[y] for x in range(n+1) for y in range(n+1) if cdf(x,n,n,x+y)<=a)
def two_look(p0,p1,n,a):
    # look 1 at n per arm; if not kept and the method arm had fewer pieces needing the owner,
    # go on to 2n per arm and test all pieces together at the same line a.
    P1,P0=pmf(n,p1),pmf(n,p0); keep=0; second=0
    for x in range(n+1):
        for y in range(n+1):
            w=P1[x]*P0[y]
            if cdf(x,n,n,x+y)<=a: keep+=w
            elif x<y:
                second+=w
                keep+=w*sum(P1[u]*P0[v] for u in range(n+1) for v in range(n+1) if cdf(x+u,2*n,2*n,x+y+u+v)<=a)
    return keep,second
n=30
print("ONE LOOK, 30 per arm")
for p0 in (0.5,0.3):
  for L,a in (("1 in 10",0.10),("1 in 40",0.025)):
    print(f" start {p0:.0%}, line {L}: real halving kept {one_look(p0,p0/2,n,a):.2f}; no-effect kept {one_look(p0,p0,n,a):.3f}")
print("TWO LOOKS, 30 then 60 per arm, one line at both looks, chosen so no-effect kept <= target")
for target in (0.10,0.025):
  for p0 in (0.5,0.3):
    best=None
    for a in [x/1000 for x in range(5,int(target*1000)+1)]:
      fk,_=two_look(p0,p0,n,a)
      if fk<=target: best=(a,fk)
    a,fk=best; pw,sec=two_look(p0,p0/2,n,a); _,sec0=two_look(p0,p0,n,a)
    print(f" overall target {target}, start {p0:.0%}: line at each look {a}; no-effect kept {fk:.3f}; real halving kept {pw:.2f}; second trial run for real {sec:.2f}, for no-effect {sec0:.2f}")
print("SHARE OF KEPT METHODS THAT DO NOTHING, one look, if 1 in 10 methods tried is real")
for p0 in (0.5,0.3):
  for L,a in (("1 in 10",0.10),("1 in 40",0.025)):
    t=0.1*one_look(p0,p0/2,n,a); f=0.9*one_look(p0,p0,n,a)
    print(f" start {p0:.0%}, line {L}: {f/(t+f):.2f}")
```

Script twolook2.py:

```python
# Round 2 additions: fixed lines checked at both starting shares, and the hold-up guard's false-fail
# chance. Same tools as twolook.py.
import sys; sys.path.insert(0,'.')
from twolook_lib import *
n=30
for a,label in ((0.097,"1 in 10 overall"),(0.022,"1 in 40 overall")):
  for p0 in (0.5,0.3):
    fk,s0=two_look(p0,p0,n,a); pw,s1=two_look(p0,p0/2,n,a)
    print(f"{label}, line {a} at each look, start {p0:.0%}: no-effect kept {fk:.3f}; real halving kept {pw:.2f}; second trial: real {s1:.2f}, no-effect {s0:.2f}")
# Hold-up guard: a method fails it when its pieces do worse on a check by enough that chance alone
# would produce it at most 1 time in 10 (one-sided Fisher, the harm direction), at 30 pieces per arm.
for share in (0.6,0.5,0.2,0.1):
    print(f"hold-up guard, check failed by {share:.0%} of pieces either way: method with no effect fails it {one_look(1-share,1-share,n,0.10):.3f}")
```

## Routed to stage
2 Shape (Discovery): evidence for the value-target question (Discovery-2).
