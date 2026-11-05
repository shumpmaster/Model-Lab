"""Counts, caps and review points (spec S-001, AC8; E-003 Sample).

  python3 -I src/E-003/counts.py cap --kind K --side work|judging|total [--pairs N]
  python3 -I src/E-003/counts.py may-start --kind K --side work|judging --started N [--pairs N]
          [--ruling-file F]
  python3 -I src/E-003/counts.py due --kind K --side work|judging --runs R --run-cards-sent J --weeks W
          --review-cards-sent V
  python3 -I src/E-003/counts.py card --kind K --work FILE --judging FILE --weeks W [--target 60]
  python3 -I src/E-003/counts.py record-ruling --file F --kind K --ruling "go on"|"stop" --date YYYY-MM-DD

cap        Planned runs per side: plans and built work 2 doers and 2 judges a pair, research 2 checks and
           1 judge a memo, plus the sheet's 1 run; the reserve is 10% of the kind's planned runs, rounded
           up, split in proportion to the sides' planned runs with the judging side's share rounded down
           and the rest to the work side.  A side's cap is its planned runs plus its share; the kind's total
           is the planned runs plus the reserve.  At 60 pairs: plans and built work 133 and 132 (266 in
           all), research 133 and 66 (200).
may-start  Whether one more run may start on a side: fewer started than the side's cap (no side borrows
           the other's share) and no "stop" as the kind's latest recorded ruling.
due        A counts card is due at every 20 runs of a side and at every 16 weeks after the kind opened.
card       The owner's counts card: runs and tokens of each side (the work side's from its records, the
           judging side's from the judging lead's latest counts block, S-001 J5), pairs collected and left
           out, the power at the pairs collected under sizing.py's three assumptions (each kind from its
           own starting figure), and the weeks to the target at the pace so far.  It shows no outcome:
           nothing of the work side's file is copied but its runs, tokens and pair counts.
record-ruling  Appends the owner's "go on" or "stop" for a kind, with its date; any other word is refused
           and nothing is written.
"""
import argparse
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import e003lib as L  # noqa: E402

RUN_CHECKPOINT = 20
REVIEW_WEEKS = 16


def planned(kind, pairs):
    work = 2 * pairs
    judging = 2 * pairs if kind in ("plans", "built") else pairs
    return work, judging


def caps(kind, pairs=60):
    work, judging = planned(kind, pairs)
    total_planned = work + judging + 1
    reserve = (total_planned + 9) // 10
    j_share = reserve * judging // (work + judging)
    w_share = reserve - j_share
    return {"work": work + w_share, "judging": judging + j_share, "total": total_planned + reserve,
            "planned": {"work": work, "judging": judging, "sheet": 1}, "reserve": {"work": w_share,
                                                                                   "judging": j_share}}


def latest_ruling(path, kind):
    if not path or not os.path.isfile(path):
        return None
    last = None
    for line in L.read_text(path).split("\n"):
        f = line.split("\t")
        if len(f) == 3 and f[1] == kind and f[2] in ("go on", "stop"):
            last = f[2]
    return last


def nonneg_int(s, name):
    try:
        v = int(s)
    except (TypeError, ValueError):
        raise SystemExit("counts.py: %s is not an integer" % name)
    return v


def cmd_card(a):
    work = L.read_json(a.work)
    w_runs = nonneg_int(work.get("runs"), "work runs")
    w_tokens = nonneg_int(work.get("tokens"), "work tokens")
    collected = nonneg_int(work.get("pairs_collected"), "pairs_collected")
    left = nonneg_int(work.get("pairs_left_out"), "pairs_left_out")
    lines, err = L.split_lines(L.read_text(a.judging))
    if err:
        L.refuse("refused: the judging lead's counts block: %s" % err)
    values, err = L.parse_counts_lines(lines)
    if err:
        L.refuse("refused: the judging lead's counts block: %s" % err)
    s = L.sizing()
    key = L.SIZING_KEY[a.kind]
    power = {name: s.power(collected, *s.cells(s.START[key], name)[1:3]) for name in s.NAMES}
    if collected >= a.target:
        to_target = 0
    elif collected <= 0 or a.weeks <= 0:
        to_target = None
    else:
        to_target = round((a.target - collected) / (collected / a.weeks), 1)
    c = caps(a.kind, a.target)
    words = {"plans": "plans", "built": "built work", "research": "research"}[a.kind]
    text = "\n".join([
        "Counts card: %s, week %s since the kind opened (%s)." % (words, fmt_num(a.weeks), values["counts"]),
        "Work side: %s runs of %s at most, %s tokens." % (fmt_int(w_runs), c["work"], fmt_int(w_tokens)),
        "Judging side: %s runs of %s at most, %s tokens, reserve used %s, as of the INDEX at %s." % (
            fmt_int(int(values["runs"])), c["judging"], fmt_int(int(values["tokens"])), values["reserve-used"],
            values["index-commit"][:12]),
        "Pairs collected: %d; left out: %d." % (collected, left),
        "Power at %d pairs, for a real 20-point difference at 1 in 40: one-way %.2f, middle %.2f, independent %.2f." % (
            collected, power["one-way"], power["middle"], power["independent"]),
        ("Weeks to %d pairs at the pace so far: %s." % (a.target, fmt_num(to_target))) if to_target is not None
        else "Weeks to %d pairs at the pace so far: no pace yet." % a.target,
        "Your ruling: \"go on\" or \"stop this kind\".",
    ])
    first_use = {k: values[k] for k in ("k1-canary", "k2", "k3", "k4", "k5", "k7")}
    L.emit({"kind": a.kind, "weeks": a.weeks, "text": text, "work": {"runs": w_runs, "tokens": w_tokens},
            "judging": {"runs": int(values["runs"]), "tokens": int(values["tokens"]),
                        "reserve_used": int(values["reserve-used"]), "index_commit": values["index-commit"]},
            "pairs_collected": collected, "pairs_left_out": left, "power": power, "weeks_to_target": to_target,
            "caps": {"work": c["work"], "judging": c["judging"]}, "first_use_checks": first_use})


def fmt_int(n):
    return "{:,}".format(n)


def fmt_num(x):
    return str(int(x)) if float(x).is_integer() else "%.1f" % x


def main(argv=None):
    ap = argparse.ArgumentParser(prog="counts.py", description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("cap")
    c.add_argument("--kind", required=True, choices=L.KINDS)
    c.add_argument("--side", required=True, choices=("work", "judging", "total"))
    c.add_argument("--pairs", type=int, default=60)
    m = sub.add_parser("may-start")
    m.add_argument("--kind", required=True, choices=L.KINDS)
    m.add_argument("--side", required=True, choices=("work", "judging"))
    m.add_argument("--started", required=True, type=int)
    m.add_argument("--pairs", type=int, default=60)
    m.add_argument("--ruling-file")
    d = sub.add_parser("due")
    d.add_argument("--kind", required=True, choices=L.KINDS)
    d.add_argument("--side", required=True, choices=("work", "judging"))
    d.add_argument("--runs", required=True, type=int)
    d.add_argument("--run-cards-sent", required=True, type=int)
    d.add_argument("--weeks", required=True, type=float)
    d.add_argument("--review-cards-sent", required=True, type=int)
    k = sub.add_parser("card")
    k.add_argument("--kind", required=True, choices=L.KINDS)
    k.add_argument("--work", required=True)
    k.add_argument("--judging", required=True)
    k.add_argument("--weeks", required=True, type=float)
    k.add_argument("--target", type=int, default=60)
    r = sub.add_parser("record-ruling")
    r.add_argument("--file", required=True)
    r.add_argument("--kind", required=True, choices=L.KINDS)
    r.add_argument("--ruling", required=True)
    r.add_argument("--date", required=True)
    a = ap.parse_args(argv)

    if a.cmd == "cap":
        L.emit({"cap": caps(a.kind, a.pairs)[a.side], "kind": a.kind, "side": a.side, "pairs": a.pairs})
    if a.cmd == "may-start":
        cap = caps(a.kind, a.pairs)[a.side]
        ruling = latest_ruling(a.ruling_file, a.kind)
        if ruling == "stop":
            L.emit({"allowed": False, "reason": "the owner ruled \"stop\" for this kind"})
        if a.started >= cap:
            L.emit({"allowed": False, "reason": "the %s side has started its cap of %d runs" % (a.side, cap)})
        L.emit({"allowed": True, "reason": "", "cap": cap})
    if a.cmd == "due":
        by_runs = a.runs // RUN_CHECKPOINT > a.run_cards_sent
        by_weeks = int(a.weeks // REVIEW_WEEKS) > a.review_cards_sent
        reasons = []
        if by_runs:
            reasons.append("%d runs of the %s side" % (a.runs, a.side))
        if by_weeks:
            reasons.append("%s weeks since the kind opened" % fmt_num(a.weeks))
        L.emit({"due": by_runs or by_weeks, "reason": "; ".join(reasons)})
    if a.cmd == "card":
        cmd_card(a)
    if a.ruling not in ("go on", "stop"):
        L.refuse("refused: a ruling is \"go on\" or \"stop\"")
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", a.date):
        L.refuse("refused: the date is not YYYY-MM-DD")
    with open(a.file, "a", encoding="utf-8", newline="") as fh:
        fh.write("%s\t%s\t%s\n" % (a.date, a.kind, a.ruling))
    L.emit({"recorded": True, "kind": a.kind, "ruling": a.ruling, "date": a.date})


if __name__ == "__main__":
    main()
