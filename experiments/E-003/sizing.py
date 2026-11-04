"""Sizing for the fair test (experiments/E-003.md, spec S-001). Standard library only.

Exact power of the paired test E-003 registers: over N pairs, a change is kept when the
one-sided exact binomial test on the discordant pairs (n10 = change passes, no change fails;
n01 = the reverse) gives P(X >= n10 | n10 + n01, 1/2) <= 1/40 (docs/PROJECT.md section 6, V1).
Each pair falls in n10 with probability p10 and in n01 with p01; the gain is p10 - p01.

Three assumptions about how often the two arms disagree, because no record measures it:
  one-way      p10 = 0.20, p01 = 0       the change only ever helps (the most favourable)
  middle       p10 = 0.25, p01 = 0.05    the library's assumption (portfolio library Q-003-F-i)
  independent  p10 = p1(1-p0), p01 = p0(1-p1): the arms agree no more than chance (the least
               favourable here), from each kind's starting figure p0 and p1 = p0 + 0.20

Also printed: the same with a judge that gets one verdict in ten wrong at random (judge noise,
never measured: E-002 was not run); the power for a real gain of 10 points; and, from the arrival
rates experiments/E-003/arrivals.py derives, the weeks each size takes, the pairs expected at the
16-week review point, and the power at that number.

Pace. The Service Desk's own pace is the expected case: the operating model repository has had no
commit since 24 October and Model-Lab's research was this project's own Discovery, so the pooled
pace of all three projects returns only if the other projects resume. Weeks are therefore given at
the Service Desk's pace, from the whole of each piece on record at dispatch (share 3/4) to half of
them (3/8), and separately at the pooled pace with share 3/4, labelled "only if the other projects
resume".

Run: python3 experiments/E-003/sizing.py
"""
import math
from math import comb

ALPHA = 1 / 40
START = {"plans": 0.05, "research": 0.26, "built work": 0.40}  # docs/PROJECT.md section 6
TOKENS_PER_RUN = 2_526_069 / 14  # E-001's 14 runs (src/E-001/RESULT.md, Step 2: cost)
RUNS_PER_PAIR = {"plans": 4, "research": 3, "built work": 4}  # E-003, Sample
SIZES = (40, 60, 100)
JUDGE_ERROR = 0.10  # an assumption for illustration, not a measured figure
REVIEW_WEEKS = 16  # E-003, Sample: the owner's review point for each kind

# Pieces a week reaching their check (python3 experiments/E-003/arrivals.py, part 2):
# (Service Desk alone over Q-008's window, all three projects over it).
PACE = {"plans": (3.8, 7.9), "research": (2.5, 3.4), "built work": (10.8, 14.4)}
# Share of arriving pieces that enter: on record at dispatch (1 in 2 to all; arrivals.py part 4
# finds 4 of 6 recent research items with the source check on record, rounded down to 1 in 2 for
# the low end, and plans and built work none until the owner orders recording, S-001 open
# question 5) times staying in after the in-flight rule (3 in 4: E-001 found mid-round inputs in
# 4 of the 16 plan and built pieces it audited).
SHARE = (0.5 * 0.75, 1.0 * 0.75)


def critical(d):
    """Smallest n10 that clears 1/40 among d discordant pairs, or None."""
    for k in range(d + 1):
        if sum(comb(d, j) for j in range(k, d + 1)) / 2 ** d <= ALPHA:
            return k
    return None


def power(n, p10, p01):
    pd = p10 + p01
    if n <= 0 or pd <= 0:
        return 0.0
    q = p10 / pd
    total = 0.0
    for d in range(n + 1):
        k = critical(d)
        if k is None:
            continue
        p_d = comb(n, d) * pd ** d * (1 - pd) ** (n - d)
        total += p_d * sum(comb(d, j) * q ** j * (1 - q) ** (d - j) for j in range(k, d + 1))
    return total


def cells(p0, name, gain=0.20):
    """(p11, p10, p01, p00) for one assumption."""
    p1 = p0 + gain
    if name == "one-way":
        p10, p01 = gain, 0.0
    elif name == "middle":
        p10, p01 = gain + 0.05, 0.05
    else:
        p10, p01 = p1 * (1 - p0), p0 * (1 - p1)
    p11 = p1 - p10
    return p11, p10, p01, 1 - p11 - p10 - p01


def noisy(c, e):
    """Discordant probabilities when each verdict is flipped at random with probability e."""
    p11, p10, p01, p00 = c
    k = 1 - e
    return (p11 * k * e + p10 * k * k + p01 * e * e + p00 * e * k,
            p11 * e * k + p10 * e * e + p01 * k * k + p00 * k * e)


NAMES = ("one-way", "middle", "independent")


def runs_for(kind, n):
    runs = RUNS_PER_PAIR[kind] * n + 1  # + the Check author's held-back check
    return runs + math.ceil(runs * 0.10)  # + the 10% reserve


def weeks_for(kind, n):
    """(Service Desk pace, all on record; Service Desk pace, half on record; pooled pace, all on record)."""
    slow, fast = PACE[kind]
    return n / (slow * SHARE[1]), n / (slow * SHARE[0]), n / (fast * SHARE[1])


def fmt(ps):
    return " / ".join(f"{p:.2f}" for p in ps)


if __name__ == "__main__":
    print("critical n10 for 10, 15, 20 discordant pairs:", critical(10), critical(15), critical(20))
    print(f"eligible pieces a week = pace x share; share {SHARE[0]:.3f} (half on record) to {SHARE[1]:.3f} (all)")
    for kind, p0 in START.items():
        slow, fast = PACE[kind]
        print(f"\n{kind} (starting figure {p0:.0%}); eligible a week at the Service Desk's pace "
              f"{slow * SHARE[0]:.2f} to {slow * SHARE[1]:.2f}; {fast * SHARE[1]:.2f} only if the other projects resume")
        for n in SIZES:
            r = runs_for(kind, n)
            hi, lo, fa = weeks_for(kind, n)
            print(f"  {n} pairs: {r} runs with reserve, about {r * TOKENS_PER_RUN / 1e6:.0f} million tokens; "
                  f"{hi:.0f} to {lo:.0f} weeks at the Service Desk's pace ({fa:.0f} only if the other projects resume)")
            print(f"    power, 20-point gain, one-way / middle / independent: "
                  f"{fmt(power(n, *cells(p0, s)[1:3]) for s in NAMES)}")
            print(f"    same, judge wrong 1 verdict in {round(1 / JUDGE_ERROR)}: "
                  f"{fmt(power(n, *noisy(cells(p0, s), JUDGE_ERROR)) for s in NAMES)}")
            print(f"    power, 10-point gain, one-way / middle / independent: "
                  f"{fmt(power(n, *cells(p0, s, 0.10)[1:3]) for s in NAMES)}")
        for label, share in (("half on record", SHARE[0]), ("all on record", SHARE[1])):
            at = math.floor(REVIEW_WEEKS * slow * share)
            print(f"  at the {REVIEW_WEEKS}-week review point, Service Desk's pace, {label}: about {at} pairs; "
                  f"power at {at}, one-way / middle / independent: {fmt(power(at, *cells(p0, s)[1:3]) for s in NAMES)}")

    print("\nOptions (runs with reserve; weeks at the Service Desk's pace, all to half on record, one kind after"
          " another / collected together; in brackets, only if the other projects resume)")
    options = {
        "A: 60 each": {"built work": 60, "plans": 60, "research": 60},
        "B: 40 each": {"built work": 40, "plans": 40, "research": 40},
        "C: built work 60 only": {"built work": 60},
        "D: 100 research and built, 60 plans": {"built work": 100, "plans": 60, "research": 100},
    }
    for name, plan in options.items():
        runs = sum(runs_for(k, n) for k, n in plan.items())
        seq = [sum(weeks_for(k, n)[i] for k, n in plan.items()) for i in (0, 1, 2)]
        par = [max(weeks_for(k, n)[i] for k, n in plan.items()) for i in (0, 1, 2)]
        print(f"  {name}: {runs} runs, about {runs * TOKENS_PER_RUN / 1e6:.0f} million tokens; "
              f"{seq[0]:.0f} to {seq[1]:.0f} weeks one after another ({seq[2]:.0f}), "
              f"{par[0]:.0f} to {par[1]:.0f} together ({par[2]:.0f})")
