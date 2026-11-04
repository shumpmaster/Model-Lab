"""Sizing for the fair test (experiments/E-003.md, spec S-001). Standard library only.

Exact power of the paired test E-003 registers: over N pairs, a change is kept when the
one-sided exact binomial test on the discordant pairs (n10 = change passes, no change fails;
n01 = the reverse) gives P(X >= n10 | n10 + n01, 1/2) <= 1/40 (docs/PROJECT.md section 6, V1).
Each pair falls in n10 with probability p10 and in n01 with p01; the gain is p10 - p01 = 0.20.

Three assumptions about how often the two arms disagree, because no record measures it:
  one-way      p10 = 0.20, p01 = 0       the change only ever helps (the most favourable)
  middle       p10 = 0.25, p01 = 0.05    the library's assumption (portfolio library Q-003-F-i)
  independent  p10 = p1(1-p0), p01 = p0(1-p1): the arms agree no more than chance (the least
               favourable here), from each kind's starting figure p0 and p1 = p0 + 0.20

Run: python3 experiments/E-003/sizing.py
"""
import math
from math import comb

ALPHA = 1 / 40
START = {"plans": 0.05, "research": 0.26, "built work": 0.40}  # docs/PROJECT.md section 6
TOKENS_PER_RUN = 2_526_069 / 14  # E-001's 14 runs (src/E-001/RESULT.md, Step 2: cost)
RUNS_PER_PAIR = {"plans": 4, "research": 3, "built work": 4}  # E-003, Sample


def critical(d):
    """Smallest n10 that clears 1/40 among d discordant pairs, or None."""
    for k in range(d + 1):
        if sum(comb(d, j) for j in range(k, d + 1)) / 2 ** d <= ALPHA:
            return k
    return None


def power(n, p10, p01):
    pd = p10 + p01
    q = p10 / pd
    total = 0.0
    for d in range(n + 1):
        k = critical(d)
        if k is None:
            continue
        p_d = comb(n, d) * pd ** d * (1 - pd) ** (n - d)
        total += p_d * sum(comb(d, j) * q ** j * (1 - q) ** (d - j) for j in range(k, d + 1))
    return total


def scenarios(p0):
    p1 = p0 + 0.20
    return {"one-way": (0.20, 0.0), "middle": (0.25, 0.05),
            "independent": (p1 * (1 - p0), p0 * (1 - p1))}


if __name__ == "__main__":
    print("critical n10 for 10, 15, 20 discordant pairs:", critical(10), critical(15), critical(20))
    for kind, p0 in START.items():
        print(f"\n{kind} (starting figure {p0:.0%})")
        for n in (40, 60, 100):
            runs = RUNS_PER_PAIR[kind] * n + 1  # + the Check author's held-back check
            reserve = math.ceil(runs * 0.10)
            pw = ", ".join(f"{s} {power(n, *pp):.2f}" for s, pp in scenarios(p0).items())
            print(f"  {n} pairs: {runs} runs + {reserve} reserve = {runs + reserve} runs, "
                  f"about {(runs + reserve) * TOKENS_PER_RUN / 1e6:.0f} million tokens; power: {pw}")
