"""The judge's steps and its return (spec S-001, AC5 and J5; E-003 Step 4, Sample "Reruns (a)").

  python3 -I src/E-003/judge.py next-step --state JSON
          JSON: {"verdict": "PASS"|"FAIL"|null, "follow_up_sent": bool, "sessions": n}
          -> {"action": "done" | "follow-up" | "new-session" | "leave-out"}
  python3 -I src/E-003/judge.py parse-return --text-file F [--background-running]
          -> {"verdict": "PASS"|"FAIL"|"none", "failed": ["<n>@<path>:<line>" | "<n>@-", ...], "multiple": bool}
  python3 -I src/E-003/judge.py followup-text
  python3 -I src/E-003/judge.py arm-outcome --verdict PASS|FAIL|none [--locked-exit N] -> {"pass": bool|null}
  python3 -I src/E-003/judge.py check-model --doer M --judge M -> {"ok": bool}

next-step     A judge that ends without a verdict line gets, in the same session, the one fixed
              follow-up; if it still gives none, one new judge session with the same brief; if that
              gives none, the pair is left out and listed.  Never a third session.
parse-return  The verdict is the first line only, exactly `Verdict: PASS` or `Verdict: FAIL`; anything
              else, or background tasks still running at the end, is no verdict.  A second verdict line
              is reported (`multiple`) and the first counts.  Each later line that starts with a test
              number gives `<n>@<path>:<line>` when it cites file:line in J5's form, else `<n>@-`; each
              number once.  (The judging lead still checks each cited path against the export's file
              list before it writes the J5 line, and writes `<n>@-` for one that names no file of it.)
arm-outcome   Built work passes only if the judge passes and the locked checks exit 0; plans and research
              have no locked checks; no verdict is neither pass nor fail.
check-model   Every judge runs on a model other than the doers'.
"""
import argparse
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import e003lib as L  # noqa: E402

FOLLOWUP = "Return your verdict now. First line: `Verdict: PASS` or `Verdict: FAIL`."
VERDICT_LINE = re.compile(r"Verdict: (PASS|FAIL)")
TEST_LINE = re.compile(r"^\s*(?:[-*]\s*)?(?:test\s*)?#?(\d{1,4})(?:[.):]|\s|$)(.*)$", re.I)
CITE = re.compile(r"([A-Za-z0-9._/+-]{1,200}):(\d{1,6})(?![\d])")


def next_step(state):
    verdict = state.get("verdict")
    if verdict in ("PASS", "FAIL"):
        return "done"
    sessions = int(state.get("sessions") or 1)
    if sessions >= 2:
        return "leave-out"
    if not state.get("follow_up_sent"):
        return "follow-up"
    return "new-session"


def parse_return(text, background=False):
    lines = text.replace("\r\n", "\n").split("\n")
    first = lines[0].rstrip() if lines else ""
    m = VERDICT_LINE.fullmatch(first)
    verdict = m.group(1) if m and not background else "none"
    failed, seen, multiple = [], set(), False
    if m:
        for line in lines[1:]:
            if VERDICT_LINE.fullmatch(line.strip()):
                multiple = True
                break
            t = TEST_LINE.match(line)
            if not t:
                continue
            n = int(t.group(1))
            if n in seen or n == 0:
                continue
            seen.add(n)
            c = CITE.search(t.group(2))
            if c and L.cited_path_ok(c.group(1)):
                failed.append("%d@%s:%s" % (n, c.group(1), c.group(2)))
            else:
                failed.append("%d@-" % n)
    return {"verdict": verdict, "failed": failed, "multiple": multiple}


def main(argv=None):
    ap = argparse.ArgumentParser(prog="judge.py", description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    n = sub.add_parser("next-step")
    n.add_argument("--state", required=True)
    p = sub.add_parser("parse-return")
    p.add_argument("--text-file", required=True)
    p.add_argument("--background-running", action="store_true")
    sub.add_parser("followup-text")
    o = sub.add_parser("arm-outcome")
    o.add_argument("--verdict", required=True, choices=("PASS", "FAIL", "none"))
    o.add_argument("--locked-exit", type=int)
    c = sub.add_parser("check-model")
    c.add_argument("--doer", required=True)
    c.add_argument("--judge", required=True)
    a = ap.parse_args(argv)
    if a.cmd == "next-step":
        try:
            state = json.loads(a.state)
        except ValueError:
            ap.error("--state is not JSON")
        L.emit({"action": next_step(state)})
    if a.cmd == "parse-return":
        L.emit(parse_return(L.read_text(a.text_file), a.background_running))
    if a.cmd == "followup-text":
        sys.stdout.write(FOLLOWUP + "\n")
        return
    if a.cmd == "arm-outcome":
        if a.verdict == "none":
            L.emit({"pass": None, "reason": "no verdict"})
        ok = a.verdict == "PASS" and (a.locked_exit is None or a.locked_exit == 0)
        L.emit({"pass": ok, "reason": "" if ok else ("the judge failed it" if a.verdict == "FAIL"
                                                       else "the locked checks failed")})
    if a.cmd == "check-model":
        same = a.doer.strip().lower() == a.judge.strip().lower()
        L.emit({"ok": not same and L.full(L.MODEL, a.judge), "reason": "the judge runs on the doers' model" if same
                else ""})


if __name__ == "__main__":
    main()
