# E-004, the line at two looks (P18): both versions the owner's ruling left open
# (decisions/questions/P-002-design-gate.md, Part 7, C), computed for a card of the owner's own.
# Run: python3 -I experiments/E-004/line.py   (reads nothing; needs numpy; about a minute)
#
# The trial, as registered in experiments/E-004.md: each new piece of one kind is drawn to "with the
# method" or "without"; look 1 at 30 pieces each way; if the method is not passed there and its pieces
# needed the owner less often than the others ("leaned the right way"), 30 more each way, and all 60 each
# way are tested together. The test at each look: Fisher's exact test, one-sided (the with-method pieces
# need the owner less often), passed when its p-value is at most the line. The same line at both looks.
#
# Version (a): the line as worked out so far, 0.097 at each look (intake/P-002-value-target-odds-
#   2026-11-10.md, twolook2.py; reviews/P-002-value-target-odds/reviewer.md, rounds 1 to 3).
# Version (b): the largest line at which a method that does nothing passes at most 1 time in 10 at
#   every starting share (searched below, over the shares on GRID).
#
# For each, at starting shares 1 in 10 to 9 in 10 (the share of pieces of the kind that need the owner
# without the method): the overall chance a method that does nothing passes, and how often a method that
# truly halves that share passes; both before the hold-up checks.
#
# Assumptions (each one a choice of this calculation, not a finding):
#  A1 Pieces are independent of each other, and within an arm each needs the owner with one fixed chance.
#  A2 Exactly 30 pieces each way at look 1 and 30 more each way at look 2 (the shuffled draws fill both).
#  A3 "A true halving" means the with-method share is exactly half the without-method share.
#  A4 "Leaned the right way" means strictly fewer with-method pieces needed the owner than without (x < y);
#     a tie does not go on.
#  A5 The figures are before the hold-up checks, the short reads and any stop (P6, P7, P8); those can only
#     lower how often a method passes.
#  A6 The starting share is the same at both looks (nothing else changes how often pieces need the owner
#     between the two looks).
#  A7 "At every starting share" is read as every share on GRID below (0.001 to 0.999 in steps of 0.001),
#     with the largest found refined in steps of 0.0001 around it; version (b)'s line is then checked
#     again at every share from 0.0001 to 0.9999 in steps of 0.0001.
#  A8 Fisher's p-values take finitely many values, so a range of lines gives the same decisions; version
#     (b) is reported as the lowest and highest line of that range.
import numpy as np
from math import comb

N1, N2 = 30, 60
GRID = [i / 1000 for i in range(1, 1000)]
SHARES = [i / 10 for i in range(1, 10)]


def cdf_table(n):
    """T[x][k] = P(with-method count <= x | k needing the owner in all, n each way), fixed margins."""
    T = np.ones((n + 1, 2 * n + 1))
    for k in range(2 * n + 1):
        tot = comb(2 * n, k)
        run = 0
        for x in range(0, n + 1):
            if 0 <= k - x <= n:
                run += comb(n, x) * comb(n, k - x)
            T[x][k] = run / tot
    return T


C1, C2 = cdf_table(N1), cdf_table(N2)
X, Y, U, V = np.meshgrid(*(np.arange(N1 + 1),) * 4, indexing="ij")
ROW, COL = X + U, X + Y + U + V          # look 2 counts, all 60 each way
GO_ON = (X < Y)[:, :, 0, 0]               # leaned the right way (A4)


def rules(line):
    """The pass regions for a line: look 1 (31 x 31) and look 2 given look 1 (31 x 31 x 31 x 31)."""
    r1 = C1 <= line
    R1 = r1[np.arange(N1 + 1)[:, None], np.arange(N1 + 1)[:, None] + np.arange(N1 + 1)[None, :]]
    R2 = (C2 <= line)[ROW, COL]
    return R1, R2


def pmf(n, p):
    return np.array([comb(n, x) * p ** x * (1 - p) ** (n - x) for x in range(n + 1)])


def passes(R1, R2, p_with, p_without):
    """(chance the method passes, chance the trial takes its second look)."""
    Pw, Po = pmf(N1, p_with), pmf(N1, p_without)
    W = np.outer(Pw, Po)                                   # look 1 counts (x with, y without)
    S = np.einsum("xyuv,u,v->xy", R2, Pw, Po)              # look 2 passes, given look 1's counts
    second = (~R1) & GO_ON
    return float((W * R1).sum() + (W * second * S).sum()), float((W * second).sum())


def worst_null(R1, R2, grid):
    vals = [(passes(R1, R2, p, p)[0], p) for p in grid]
    return max(vals)


def worst_null_refined(line):
    R1, R2 = rules(line)
    v, p = worst_null(R1, R2, GRID)
    fine = [round(p + d / 10000, 4) for d in range(-10, 11) if 0 < p + d / 10000 < 1]
    return max(worst_null(R1, R2, fine), (v, p))


# --- Self-check against the recorded odds (version (a) at 1 in 2 and 3 in 10) by the loops of the
#     recorded twolook.py, written out again here in plain Python.
def two_look_loops(p0, p1, a):
    P1, P0 = pmf(N1, p1), pmf(N1, p0)
    keep = 0.0
    for x in range(N1 + 1):
        for y in range(N1 + 1):
            w = P1[x] * P0[y]
            if C1[x][x + y] <= a:
                keep += w
            elif x < y:
                keep += w * sum(P1[u] * P0[v] for u in range(N1 + 1) for v in range(N1 + 1)
                                if C2[x + u][x + y + u + v] <= a)
    return keep


print("SELF-CHECK, line 0.097, plain loops against the vectorised code")
Ra = rules(0.097)
for p0 in (0.5, 0.3):
    loops = two_look_loops(p0, p0, 0.097)
    vec = passes(*Ra, p0, p0)[0]
    print(f" start {p0:.1f}: does-nothing passes {loops:.4f} (loops) {vec:.4f} (vectorised)")
    assert abs(loops - vec) < 1e-9

# --- Version (b): the largest line with the worst does-nothing chance at most 0.10 over GRID.
cands = sorted({float(v) for v in np.concatenate([C1.ravel(), C2.ravel()]) if 0.05 <= v <= 0.10})
lo, hi = 0, len(cands) - 1                 # invariant: cands[lo] holds (checked below), cands[hi+1] fails
assert worst_null(*rules(cands[lo]), GRID)[0] <= 0.10
while lo < hi:
    mid = (lo + hi + 1) // 2
    if worst_null(*rules(cands[mid]), GRID)[0] <= 0.10:
        lo = mid
    else:
        hi = mid - 1
b_low = cands[lo]
b_next = cands[lo + 1] if lo + 1 < len(cands) else None
b_worst, b_at = worst_null_refined(b_low)
if b_worst > 0.10:
    raise SystemExit(f"refined grid breaks version (b): {b_worst:.5f} at {b_at}")
fine_all = worst_null(*rules(b_low), [i / 10000 for i in range(1, 10000)])
if fine_all[0] > 0.10:
    raise SystemExit(f"fine grid breaks version (b): {fine_all[0]:.5f} at {fine_all[1]}")
n_worst, n_at = worst_null(*rules(b_next), GRID) if b_next is not None else (None, None)
a_worst, a_at = worst_null_refined(0.097)

print()
print("THE TWO LINES")
print(f" (a) as worked out so far: 0.097 at each look; worst does-nothing pass {a_worst:.4f}, at a starting share of {a_at}")
print(f" (b) at most 1 in 10 at every starting share: any line from {b_low:.5f} up to, not including, {b_next:.5f}"
      f" gives the same decisions; worst does-nothing pass {b_worst:.4f}, at a starting share of {b_at}")
print(f"     checked at every share from 0.0001 to 0.9999 by 0.0001: worst {fine_all[0]:.4f}, at {fine_all[1]}")
if b_next is not None:
    print(f"     the next line up, {b_next:.5f}, gives a worst does-nothing pass of {n_worst:.4f}, at {n_at}, so it is out")
Rb = rules(b_low)

print()
print("BY STARTING SHARE, before the hold-up checks")
print(" share | does nothing passes (a) (b) | true halving passes (a) (b) (b)-(a) | second look taken, halving (a) (b) | does nothing (a) (b)")
for p in SHARES:
    na, sa0 = passes(*Ra, p, p)
    nb, sb0 = passes(*Rb, p, p)
    ha, sa1 = passes(*Ra, p / 2, p)
    hb, sb1 = passes(*Rb, p / 2, p)
    print(f"  {p:.1f}  |   {na:.4f}  {nb:.4f}         |   {ha:.4f}  {hb:.4f}  {hb - ha:+.4f}     |   {sa1:.4f}  {sb1:.4f}            |   {sa0:.4f}  {sb0:.4f}")

print()
print("WORST DOES-NOTHING PASS OVER EVERY SHARE ON THE GRID (0.001 to 0.999), refined by 0.0001")
for name, R, line in (("(a)", Ra, 0.097), ("(b)", Rb, b_low)):
    over = [p for p in GRID if passes(*R, p, p)[0] > 0.10]
    span = f"above 0.10 from {min(over)} to {max(over)} ({len(over)} grid shares)" if over else "never above 0.10"
    w, at = worst_null_refined(line)
    print(f" {name} worst {w:.4f} at {at}; {span}")
