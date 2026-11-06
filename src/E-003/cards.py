"""The owner's cards: draw, re-score and file (spec S-001, AC6 and J6; E-003 Step 5).

  python3 -I src/E-003/cards.py draw --pairs FILE --seed N --set SETID [--answers FILE]
  python3 -I src/E-003/cards.py rescore --pairs FILE --answers FILE
  python3 -I src/E-003/cards.py file --kind K --set SETID --cards FILE --answers FILE --out ROOT [--sheet FILE]

The pairs file is a JSON list in the dispatch order of the pieces.  Plans and built work:
  {"piece", "change": <label>, "control": <label>, "verdicts": {<label>: PASS|FAIL},
   "failed": {<label>: "<J5 failed tests>"}, "locked_failed": {<label>: bool}}   (built work only)
Research, one memo a card:
  {"piece", "label", "verdict": PASS|FAIL, "failed", "change_check_pass": bool, "control_check_pass": bool}
The answers file maps a label to the owner's answer in the owner's words; an answer that starts with
"yes" is FAIL, one that starts with "no" is PASS, anything else (can't tell) is no answer.

draw     Groups (E-003 Step 5): G1 the outputs that decide (both outputs of each pair whose verdicts
         differ; research: memos on which the two versions' counted verdicts differ), G2 outputs the
         judge passed in pairs both arms passed, G3 outputs it failed in pairs both failed; built
         outputs whose locked checks failed are in none.  Each group in dispatch order, within a pair
         by label.  One `random.Random(seed)`: sample(G1, 4), sample(G2, 2), sample(G3, 2), a group's
         shortfall taken from G1, then G3, then G2; then, while fewer than 6 cards hold a yes or no and
         fewer than 12 are shown, one more card at a time with choice() from what is left, in the order
         G1, G3, G2.  Without --answers only the first eight are drawn.  A card shows the label, its
         group and order, the judge's verdict, the failed tests' numbers with their cited lines, and
         the sheet to open (holdouts/<set id>.md in the sheets repository); never which arm or piece it is.
rescore  Each answer replaces the judge's verdict on its output (a built output whose locked checks
         failed stays failed); each pair's class (n10, n01, concordant) is worked out again.  Records the
         cards answered and the disagreements, overall and by group.
file     Writes ROOT/decisions/questions/E-003-<kind>-cards.md: each card's label, group, order, verdict,
         failed tests and the owner's answer in the owner's words, the sheet named but none of its text.
         With --sheet, any quotation of a test's text in an answer is replaced by that test's number, and
         the file says so (J6).
"""
import argparse
import json
import os
import random
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import e003lib as L  # noqa: E402

TOTAL, MAX_CARDS, NEED = 8, 12, 6
TARGET = (4, 2, 2)


def answer_of(words):
    """yes | no | None (can't tell, or no answer)."""
    if not isinstance(words, str):
        return None
    m = re.match(r"\s*(yes|no)\b", words.strip().lower())
    return m.group(1) if m else None


def owner_verdict(words):
    a = answer_of(words)
    return {"yes": "FAIL", "no": "PASS"}.get(a)


def is_research(pairs):
    return bool(pairs) and "label" in pairs[0] and "change_check_pass" in pairs[0]


def outputs(pairs):
    """{label: {"verdict", "failed", "locked_failed"}}"""
    out = {}
    for p in pairs:
        if "label" in p:
            out[p["label"]] = {"verdict": p["verdict"], "failed": p.get("failed", "-"), "locked_failed": False}
        else:
            for lab in (p["change"], p["control"]):
                out[lab] = {"verdict": p["verdicts"][lab], "failed": p.get("failed", {}).get(lab, "-"),
                            "locked_failed": bool(p.get("locked_failed", {}).get(lab))}
    return out


def counted(p, verdict):
    """Research: each version's counted pass, given the verdict on the memo."""
    ok = verdict == "PASS"
    return bool(p["change_check_pass"]) and ok, bool(p["control_check_pass"]) and ok


def groups(pairs):
    g1, g2, g3 = [], [], []
    for p in pairs:
        if "label" in p:
            ch, co = counted(p, p["verdict"])
            lab = p["label"]
            if ch != co:
                g1.append(lab)
            elif ch:
                g2.append(lab)
            else:
                g3.append(lab)
            continue
        v = p["verdicts"]
        locked = p.get("locked_failed", {})
        for lab in sorted([p["change"], p["control"]]):
            if locked.get(lab):
                continue
            if v[p["change"]] != v[p["control"]]:
                g1.append(lab)
            elif v[lab] == "PASS":
                g2.append(lab)
            else:
                g3.append(lab)
    return [g1, g2, g3]


def allocation(g):
    k = list(TARGET)
    have = [len(x) for x in g]
    short = 0
    for i in range(3):
        if have[i] < k[i]:
            short += k[i] - have[i]
            k[i] = have[i]
    for i in (0, 2, 1):
        take = min(short, have[i] - k[i])
        k[i] += take
        short -= take
    return k


def draw(pairs, seed, answers=None):
    g = groups(pairs)
    k = allocation(g)
    rng = random.Random(seed)
    seq = []
    for i in range(3):
        for lab in rng.sample(g[i], k[i]):
            seq.append((lab, "G%d" % (i + 1)))
    if answers is not None:
        shown = {s[0] for s in seq}
        left = {i: [x for x in g[i] if x not in shown] for i in range(3)}
        while True:
            answered = sum(1 for lab, _ in seq if answer_of(answers.get(lab)) is not None)
            if answered >= NEED or len(seq) >= MAX_CARDS:
                break
            for i in (0, 2, 1):
                if left[i]:
                    lab = rng.choice(left[i])
                    left[i].remove(lab)
                    seq.append((lab, "G%d" % (i + 1)))
                    break
            else:
                break
    return seq


def cmd_draw(a):
    pairs = L.read_json(a.pairs)
    answers = L.read_json(a.answers) if a.answers else None
    outs = outputs(pairs)
    seq = draw(pairs, a.seed, answers)
    cards = [{"label": lab, "group": grp, "order": i, "verdict": outs[lab]["verdict"], "failed": outs[lab]["failed"],
              "open": "holdouts/%s.md" % a.set} for i, (lab, grp) in enumerate(seq, 1)]
    answered = sum(1 for lab, _ in seq if answers and answer_of(answers.get(lab)) is not None)
    L.emit({"cards": cards, "answered": answered, "too_few": answered < NEED if answers is not None else None})


def rescore(pairs, answers):
    g = groups(pairs)
    group_of = {lab: "G%d" % (i + 1) for i in range(3) for lab in g[i]}
    by_group = {k: {"answered": 0, "disagreements": 0} for k in ("G1", "G2", "G3")}
    answered = disagreements = 0
    for lab, out in outputs(pairs).items():
        v = owner_verdict(answers.get(lab))
        if v is None:
            continue
        answered += 1
        dis = v != out["verdict"]
        disagreements += dis
        grp = group_of.get(lab)
        if grp:
            by_group[grp]["answered"] += 1
            by_group[grp]["disagreements"] += dis
    classes, n10, n01 = {}, 0, 0
    for p in pairs:
        if "label" in p:
            v = owner_verdict(answers.get(p["label"])) or p["verdict"]
            ch, co = counted(p, v)
        else:
            def final(lab):
                if p.get("locked_failed", {}).get(lab):
                    return False
                return (owner_verdict(answers.get(lab)) or p["verdicts"][lab]) == "PASS"
            ch, co = final(p["change"]), final(p["control"])
        cls = "n10" if ch and not co else "n01" if co and not ch else "concordant"
        n10 += cls == "n10"
        n01 += cls == "n01"
        classes[p["piece"]] = cls
    return {"classes": classes, "n10": n10, "n01": n01, "answered": answered, "disagreements": disagreements,
            "by_group": by_group}


def cmd_rescore(a):
    L.emit(rescore(L.read_json(a.pairs), L.read_json(a.answers)))


# ---------------------------------------------------------------------------------------------
# file

def sheet_tests(sheet_text):
    """[(number, text)] of the sheet's numbered tests."""
    out = []
    for line in sheet_text.split("\n"):
        m = re.match(r"^\s*(\d+)[.)]\s+(.*\S)\s*$", line)
        if m:
            out.append((int(m.group(1)), m.group(2)))
    return out


def phrases(text):
    """The parts of a test's text that count as a quotation of it: the whole, the part after an id and a
    colon, and every run of five or more of its words."""
    out = {text}
    if ": " in text:
        out.add(text.split(": ", 1)[1])
        out.add(text.split(": ", 1)[0])
    words = text.split()
    for n in range(len(words), 4, -1):
        for i in range(len(words) - n + 1):
            out.add(" ".join(words[i:i + n]))
    return sorted((p.strip(" .") for p in out if len(p.strip(" .")) >= 6), key=len, reverse=True)


def scrub_answer(words, tests):
    replaced = []
    for num, text in tests:
        for ph in phrases(text):
            rx = re.compile(r"[\"'“‘]?\s*" + r"\s+".join(re.escape(w) for w in ph.split()) + r"[.]?\s*[\"'”’]?",
                            re.I)
            if rx.search(words):
                words = rx.sub("[test %d] " % num, words)
                replaced.append(num)
    words = re.sub(r"\[test (\d+)\] (\s*\[test \1\] )+", r"[test \1] ", words)
    return words.replace("  ", " ").strip(), sorted(set(replaced))


def md_cell(s):
    return str(s).replace("|", "\\|").replace("\n", " ")


def cmd_file(a):
    cards = L.read_json(a.cards)
    cards = cards.get("cards", cards) if isinstance(cards, dict) else cards
    answers = L.read_json(a.answers)
    tests = sheet_tests(L.read_text(a.sheet)) if a.sheet else []
    rows, notes, n_answered = [], [], 0
    for c in sorted(cards, key=lambda c: c["order"]):
        words = answers.get(c["label"])
        reading = answer_of(words)
        n_answered += reading is not None
        shown = "(no answer)" if words is None else words
        if words is not None and tests:
            shown, nums = scrub_answer(words, tests)
            if nums:
                notes.append("Card %d (%s): the owner quoted the text of test %s; the Chief of Staff filed the answer "
                             "with that quotation replaced by the test's number." % (
                                 c["order"], c["label"], ", ".join(str(n) for n in nums)))
        rows.append("| %d | %s | %s | %s | %s | %s | %s |" % (
            c["order"], md_cell(c["label"]), c["group"], c["verdict"], md_cell(c["failed"]), md_cell(shown),
            {"yes": "yes (FAIL)", "no": "no (PASS)"}.get(reading, "can't tell")))
    sheet = "holdouts/%s.md" % a.set
    lines = [
        "Ruling: the owner's answers on the %s cards of E-003 (set %s)" % (a.kind, a.set),
        "",
        "Each card is one output, shown with the judge's verdict and the numbers of the failed tests with their "
        "cited lines; the sheet is %s in the sheets repository, for the owner to open, and none of its text is "
        "here (specs/S-001.md, J6)." % sheet,
        "",
        "## The owner's words, verbatim",
        "",
        "| Order | Output | Group | Judge's verdict | Failed tests | The owner's answer | Reading |",
        "|---|---|---|---|---|---|---|",
    ] + rows + [
        "",
        "Cards shown: %d; answered yes or no: %d." % (len(rows), n_answered),
    ]
    if notes:
        lines += ["", "## Quotations replaced", ""] + ["- " + n for n in notes]
    path = os.path.join(a.out, "decisions", "questions", "E-003-%s-cards.md" % a.kind)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write("\n".join(lines) + "\n")
    L.emit({"written": path, "cards": len(rows), "answered": n_answered, "quotations_replaced": len(notes)})


def main(argv=None):
    ap = argparse.ArgumentParser(prog="cards.py", description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    d = sub.add_parser("draw")
    d.add_argument("--pairs", required=True)
    d.add_argument("--seed", required=True, type=int)
    d.add_argument("--set", required=True)
    d.add_argument("--answers")
    r = sub.add_parser("rescore")
    r.add_argument("--pairs", required=True)
    r.add_argument("--answers", required=True)
    f = sub.add_parser("file")
    f.add_argument("--kind", required=True, choices=L.KINDS)
    f.add_argument("--set", required=True)
    f.add_argument("--cards", required=True)
    f.add_argument("--answers", required=True)
    f.add_argument("--out", required=True)
    f.add_argument("--sheet")
    a = ap.parse_args(argv)
    if not L.full(L.SET_ID, a.set if a.cmd != "rescore" else "S-001-built-1"):
        ap.error("--set is not a set id")
    {"draw": cmd_draw, "rescore": cmd_rescore, "file": cmd_file}[a.cmd](a)


if __name__ == "__main__":
    main()
