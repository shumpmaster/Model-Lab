"""A mechanical reference for E-003's analysis (spec S-001, AC7, AC9 and AC10; E-003 Measure and Deciding
threshold).

THIS IS NOT THE ANALYSIS.  E-003 has the Reviewer, which did not run the test, analyse each kind against
the registered thresholds, and the Orchestrator records the Reviewer's verdict verbatim.  The spec names
no script for it.  This script was added because S-001's locked checks need one; it is a Builder
deliverable of the harness that works out the same arithmetic mechanically, so that the Reviewer's figures
can be compared with a reference.  Its output is not a verdict, not the Reviewer's result, and not a
record of the test's outcome; nothing it prints decides whether a change is kept.

  python3 -I src/E-003/analyse.py run --kind built|plans|research --pairs FILE --cards FILE
  python3 -I src/E-003/analyse.py v2 --kind K --passes N [--pieces 30]

run   Pairs file: a JSON list of {"piece", "change_pass", "control_pass", "doer_model", "judge_model"
      [, "arm_models": [change arm's, control arm's]]}; for research {"piece", "change_check_pass",
      "control_check_pass", "memo_judge_pass", "doer_model", "judge_model"}, a version's pass counting
      only where the held-back check also passes the memo.  Cards file: {"answered": n, "disagreements":
      d}, after the owner's answers replaced the judge's verdicts (cards.py rescore).
      - A pair whose arms report different served models, or with no outcome, is left out and listed.
      - Pairs are grouped by "<doer model> / <judge model>"; if there is more than one group, the test is
        run on the larger group only and the record says so (AC9; a tie takes the group seen first).
      - Judge confirmed: at least 6 cards answered and at most 2 disagreements.
      - The one-sided exact binomial test on the differing pairs: P(X >= n10 | n10 + n01, 1/2) <= 1/40.
      - Research also: the false-pass guard, C3's false passes no more than the unchanged check's plus one.
      - Gain (n10 - n01) / pairs, with its 95% range by Newcombe's method for paired proportions.
      - Status: "too few pieces to test" (fewer than 10 pairs), "not shown: judge not confirmed",
        "kept", "not shown: false-pass guard", or "not shown".
      The `record` text of a kept change carries V2 for its kind and the change's removal test, read from
      experiments/E-003/C<n>-*.md and written out in full.
v2    V2 (docs/PROJECT.md section 6): over the first 30 pieces of the kind checked under the changed
      operating model, the first-time passes needed so that chance alone, at the starting figure (plans 2
      of 44, research 5 of 19, built work 32 of 80), gives it at most 1 time in 25 (exact, one-sided).
"""
import argparse
import math
import os
import re
import sys
from fractions import Fraction

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import e003lib as L  # noqa: E402
import change as C  # noqa: E402

ALPHA = Fraction(1, 40)
V2_ALPHA = Fraction(1, 25)
STARTING = {"plans": (2, 44), "research": (5, 19), "built": (32, 80)}
KIND_WORDS = {"plans": "plans", "built": "built work", "research": "research"}
REVIEW = {"plans": "the plan review", "built": "the build review", "research": "the source check"}
Z = 1.959963984540054


def binom_p_ge(k, d):
    if d == 0:
        return 1.0
    return float(Fraction(sum(math.comb(d, j) for j in range(k, d + 1)), 2 ** d))


def wilson(x, n):
    if n == 0:
        return 0.0, 1.0
    p = x / n
    den = 1 + Z * Z / n
    centre = (p + Z * Z / (2 * n)) / den
    half = Z * math.sqrt(p * (1 - p) / n + Z * Z / (4 * n * n)) / den
    return centre - half, centre + half


def newcombe(a, b, c, d):
    """Newcombe's method 10: (difference, lower, upper) of two paired proportions; b = n10, c = n01."""
    n = a + b + c + d
    p1, p2 = (a + b) / n, (a + c) / n
    l1, u1 = wilson(a + b, n)
    l2, u2 = wilson(a + c, n)
    diff = p1 - p2
    big = (a + b) * (c + d) * (a + c) * (b + d)
    cc = a * d - b * c
    if cc > n / 2:
        cc -= n / 2
    elif cc >= 0:
        cc = 0.0
    else:
        cc += n / 2
    phi = 0.0 if big == 0 else cc / math.sqrt(big)
    lo = diff - math.sqrt(max(0.0, (p1 - l1) ** 2 + (u2 - p2) ** 2 - 2 * phi * (p1 - l1) * (u2 - p2)))
    hi = diff + math.sqrt(max(0.0, (u1 - p1) ** 2 + (p2 - l2) ** 2 - 2 * phi * (u1 - p1) * (p2 - l2)))
    return diff, lo, hi


def v2_cutoff(kind, pieces=30):
    x, n0 = STARTING[kind]
    p = Fraction(x, n0)
    for k in range(pieces + 1):
        tail = sum(math.comb(pieces, j) * p ** j * (1 - p) ** (pieces - j) for j in range(k, pieces + 1))
        if tail <= V2_ALPHA:
            return k
    return None


def removal_items(change):
    text = L.read_text(os.path.join(L.ROOT, "experiments", "E-003", C.CHANGE_FILES[change]))
    removal = text.split("## Removal test", 1)[1] if "## Removal test" in text else ""
    return re.findall(r"^\d\. (.+)$", removal, re.M)


def outcome(p, research):
    if research:
        vals = (p.get("change_check_pass"), p.get("control_check_pass"), p.get("memo_judge_pass"))
        if any(v is None for v in vals):
            return None
        ch, co, judge = (bool(v) for v in vals)
        return ch and judge, co and judge, ch and not judge, co and not judge
    vals = (p.get("change_pass"), p.get("control_pass"))
    if any(v is None for v in vals):
        return None
    return bool(vals[0]), bool(vals[1]), False, False


def fmt(x):
    return "%.3f" % x


def kept_record(kind, change, n, n10, n01, p, gain, lo, hi):
    cutoff = v2_cutoff(kind)
    x, n0 = STARTING[kind]
    items = removal_items(change)
    words = KIND_WORDS[kind]
    lines = [
        "Kept: %s for %s. Over %d pairs, n10 = %d and n01 = %d; the one-sided exact test on the %d pairs that "
        "differ gives P = %s, at or below 1 in 40; the gain is %s (95%% range %s to %s, Newcombe's method for "
        "paired proportions), and the judge is confirmed by the owner's cards." % (
            change, words, n, n10, n01, n10 + n01, fmt(p), fmt(gain), fmt(lo), fmt(hi)),
        "",
        "V2, the measure the operating model carries after M5: the first-time pass rate of %s over the first 30 "
        "pieces checked under the changed operating model, against the starting figure of %d of %d (%.0f%%). V2 is "
        "met when at least %d of those 30 pass first time, a rate that chance alone at the starting figure would "
        "give at most 1 in 25 (exact one-sided binomial)." % (words, x, n0, 100.0 * x / n0, cutoff),
        "",
        "How the pieces are counted from the review records: a piece is one unit of %s put to its independent "
        "check (%s); the 30 are the first 30 whose round-1 check is recorded after the change enters the "
        "operating model, in the order those review records were made; a piece is a first-time pass when its "
        "review record shows PASS in its first round (round 1), and anything else (FAIL, or no round-1 verdict) "
        "is not." % (words, REVIEW[kind]),
        "",
        "Removal test for %s: it comes out, and the brief or role file returns byte for byte to its text "
        "without the paragraph, when any of these holds:" % change,
    ] + ["%d. %s" % (i, t) for i, t in enumerate(items, 1)]
    return "\n".join(lines)


def run(kind, pairs, cards):
    research = kind == "research"
    change = L.CHANGE_OF_KIND[kind]
    left_out, kept_pairs = [], []
    for p in pairs:
        am = p.get("arm_models")
        if isinstance(am, list) and len(set(am)) > 1:
            left_out.append({"piece": p.get("piece"), "reason": "the two arms report different served models "
                             "(a set-up fault still mixed after its rerun)"})
            continue
        o = outcome(p, research)
        if o is None:
            left_out.append({"piece": p.get("piece"), "reason": "no outcome for one arm (no verdict after the reruns)"})
            continue
        kept_pairs.append((p, o))
    groups, order = {}, []
    for p, o in kept_pairs:
        g = "%s / %s" % (p.get("doer_model"), p.get("judge_model"))
        if g not in groups:
            groups[g] = []
            order.append(g)
        groups[g].append(o)
    if not order:
        decided, chosen = None, []
    else:
        decided = max(order, key=lambda g: (len(groups[g]), -order.index(g)))
        chosen = groups[decided]
    n = len(chosen)
    n10 = sum(1 for ch, co, _, _ in chosen if ch and not co)
    n01 = sum(1 for ch, co, _, _ in chosen if co and not ch)
    both = sum(1 for ch, co, _, _ in chosen if ch and co)
    neither = n - n10 - n01 - both
    p_value = binom_p_ge(n10, n10 + n01)
    clears = n10 + n01 > 0 and Fraction(sum(math.comb(n10 + n01, j) for j in range(n10, n10 + n01 + 1)),
                                        2 ** (n10 + n01)) <= ALPHA
    if n:
        gain, lo, hi = newcombe(both, n10, n01, neither)
    else:
        gain, lo, hi = 0.0, -1.0, 1.0
    answered, dis = int(cards.get("answered", 0)), int(cards.get("disagreements", 0))
    confirmed = answered >= 6 and dis <= 2
    guard = None
    fp = None
    if research:
        fp = {"change": sum(1 for _, _, a, _ in chosen if a), "control": sum(1 for _, _, _, b in chosen if b)}
        guard = fp["change"] <= fp["control"] + 1
    if n < 10:
        status = "too few pieces to test"
    elif not confirmed:
        status = "not shown: judge not confirmed"
    elif clears and guard is not False:
        status = "kept"
    elif clears:
        status = "not shown: false-pass guard"
    else:
        status = "not shown"
    kept = status == "kept"
    words = KIND_WORDS[kind]
    if kept:
        record = kept_record(kind, change, n, n10, n01, p_value, gain, lo, hi)
    elif status == "too few pieces to test":
        record = ("Too few pieces to test: %s for %s closed with %d pairs, fewer than 10; it is reported, not "
                  "dropped." % (change, words, n))
    else:
        why = {"not shown: judge not confirmed":
               "the judge is not confirmed (%d cards answered, %d disagreements; it needs at least 6 answered and "
               "at most 2 disagreements), so no change is kept for this kind from this run" % (answered, dis),
               "not shown: false-pass guard":
               "the test clears, but C3's false passes (%s) are more than the unchanged check's (%s) plus one" % (
                   fp and fp["change"], fp and fp["control"]),
               "not shown": "the one-sided exact test on the %d pairs that differ (n10 = %d, n01 = %d) gives P = %s, "
               "above 1 in 40" % (n10 + n01, n10, n01, fmt(p_value))}[status]
        record = ("Not shown: %s for %s. Over %d pairs, %s. The gain is %s (95%% range %s to %s, Newcombe's method "
                  "for paired proportions). A result that does not clear is reported as not shown: the change did "
                  "not meet the owner's 20-point target in this test, and \"no change helps\" stands as an accepted "
                  "result." % (change, words, n, why, fmt(gain), fmt(lo), fmt(hi)))
    if len(order) > 1:
        record += ("\n\nThe served model changed during the comparison: pairs were grouped by model (doers / judge): "
                   "%s. The deciding test is run on the larger group only, %s (%d pairs)%s." % (
                       "; ".join("%s: %d" % (g, len(groups[g])) for g in order), decided, n,
                       ", the first seen of groups of equal size" if sum(
                           1 for g in order if len(groups[g]) == n) > 1 else ""))
    if left_out:
        record += "\n\nLeft out: %s." % "; ".join("%s (%s)" % (x["piece"], x["reason"]) for x in left_out)
    out = {"kind": kind, "change": change, "n_pairs": n, "n10": n10, "n01": n01, "p": p_value, "gain": gain,
           "ci": [lo, hi], "judge_confirmed": confirmed, "kept": kept, "status": status,
           "false_pass_guard": guard, "groups": {g: len(groups[g]) for g in order}, "decided_on": decided,
           "left_out": left_out, "record": record,
           "note": "a mechanical reference only; the analysis is the Reviewer's (E-003, Who does what)"}
    if fp is not None:
        out["false_passes"] = fp
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(prog="analyse.py", description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("run", help="the reference arithmetic for one kind (not the Reviewer's analysis)")
    r.add_argument("--kind", required=True, choices=L.KINDS)
    r.add_argument("--pairs", required=True)
    r.add_argument("--cards", required=True)
    v = sub.add_parser("v2", help="V2's cutoff for a kind")
    v.add_argument("--kind", required=True, choices=L.KINDS)
    v.add_argument("--passes", required=True, type=int)
    v.add_argument("--pieces", type=int, default=30)
    a = ap.parse_args(argv)
    if a.cmd == "run":
        L.emit(run(a.kind, L.read_json(a.pairs), L.read_json(a.cards)))
    cutoff = v2_cutoff(a.kind, a.pieces)
    x, n0 = STARTING[a.kind]
    L.emit({"kind": a.kind, "pieces": a.pieces, "passes": a.passes, "cutoff": cutoff,
            "starting_figure": "%d of %d" % (x, n0), "meets_v2": cutoff is not None and a.passes >= cutoff})


if __name__ == "__main__":
    main()
