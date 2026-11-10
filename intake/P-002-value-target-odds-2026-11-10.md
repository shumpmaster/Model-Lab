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

## Routed to stage
2 Shape (Discovery): evidence for the value-target question (Discovery-2).
