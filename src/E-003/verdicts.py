"""The verdict record checker (spec S-001, J5).

  python3 -I src/E-003/verdicts.py check --index FILE --filelists DIR --tests N --set SETID
          (--verdicts FILE | --counts FILE | --closing FILE)

--index is the kind's INDEX (J3); --filelists holds `<label>.files`, each export's file list as the
export reader prints it (`export.py list`); --tests is the sheet's `tests:` count; --set its set id.
Accepted: exit 0 and {"ok": true, ...}.  Refused: exit 1, the first line naming the offending line by its
number, never repeating its text.

The verdict file (`verdicts/<set id>.tsv`): one line per judgement, 14 tab-separated fields: label (in the
INDEX), set id, the sheet's SHA-256 as checked, the filled brief's SHA-256, served model (1 to 64 of
letters, digits, `.`, `_`, `-`), verdict (PASS, FAIL or none), failed tests (`<n>@<path>:<line>` joined
by commas, or `-`; `<n>` from 1 to the sheet's count, each once; `<path>` 1 to 200 of letters, digits,
`.`, `_`, `-`, `/`, `+`, no `..` segment, no leading `/`, a file of the judged export; `<line>` 1 to 6
digits; or `<n>@-`), follow-up sent (yes/no), new session (yes/no), first message equal to the brief
(match/differs), transcript check (clean/leak@<line>), tokens, tool uses, seconds.
The counts block: exactly `counts`, `index-commit`, `judged`, `runs`, `reserve-used`, `tokens`,
`left-out` (INDEX labels joined by commas, or `-`), `k1-canary`, `k2`, `k3`, `k4`, `k5`, `k7`, in order.
The closing block: a counts block, then the verdict file's lines, then `sha256: <hex>` of the verdict
file's bytes (its lines, each ending in a newline), and nothing after it.
"""
import argparse
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import e003lib as L  # noqa: E402

CITATION = re.compile(r"([1-9][0-9]*)@(?:-|(.+):([1-9][0-9]{0,5}|0))")


class Refused(Exception):
    pass


class Checker:
    def __init__(self, index, filelists, tests, set_id):
        rows, _ = L.read_index(index)
        self.labels = {r["label"] for r in rows}
        self.filelists = filelists
        self.tests = tests
        self.set_id = set_id
        self._files = {}

    def files(self, label):
        if label not in self._files:
            path = os.path.join(self.filelists, label + ".files")
            if not os.path.isfile(path):
                self._files[label] = None
            else:
                self._files[label] = set(p for p in L.read_text(path).split("\n") if p)
        return self._files[label]

    def verdict_line(self, line, n):
        f = line.split("\t")
        if len(f) != 14:
            raise Refused("line %d: %d tab-separated fields, not 14" % (n, len(f)))
        label, set_id, sheet, brief, model, verdict, failed, follow, new, first, tr, tokens, tools, secs = f
        if label not in self.labels:
            raise Refused("line %d: the label is not in the INDEX" % n)
        if set_id != self.set_id:
            raise Refused("line %d: the set id is not %s" % (n, self.set_id))
        if not L.full(L.SHA64, sheet) or not L.full(L.SHA64, brief):
            raise Refused("line %d: a SHA-256 is not 64 lowercase hex digits" % n)
        if not L.full(L.MODEL, model):
            raise Refused("line %d: the served model is not in its form" % n)
        if verdict not in ("PASS", "FAIL", "none"):
            raise Refused("line %d: the verdict is not PASS, FAIL or none" % n)
        if failed != "-":
            seen = set()
            for item in failed.split(","):
                m = CITATION.fullmatch(item)
                if not m:
                    raise Refused("line %d: a failed test is not `<n>@<path>:<line>` or `<n>@-`" % n)
                num = int(m.group(1))
                if num > self.tests:
                    raise Refused("line %d: test number %d is outside the sheet's %d" % (n, num, self.tests))
                if num in seen:
                    raise Refused("line %d: test number %d appears twice" % (n, num))
                seen.add(num)
                path = m.group(2)
                if path is not None:
                    if m.group(3) == "0" or not L.cited_path_ok(path):
                        raise Refused("line %d: a cited path or line is not in its form" % n)
                    files = self.files(label)
                    if files is None:
                        raise Refused("line %d: no file list for the export" % n)
                    if path not in files:
                        raise Refused("line %d: a cited path is not in the export's file list" % n)
        if follow not in ("yes", "no") or new not in ("yes", "no"):
            raise Refused("line %d: follow-up and new session are yes or no" % n)
        if first not in ("match", "differs"):
            raise Refused("line %d: first message is match or differs" % n)
        if not (tr == "clean" or re.fullmatch(r"leak@[1-9][0-9]*", tr)):
            raise Refused("line %d: the transcript check is clean or leak@<line>" % n)
        for v in (tokens, tools, secs):
            if not L.full(L.INT, v):
                raise Refused("line %d: tokens, tool uses and seconds are decimal integers" % n)

    def verdict_lines(self, lines, first=1):
        for i, line in enumerate(lines, first):
            self.verdict_line(line, i)

    def counts(self, lines, first=1):
        values, err = L.parse_counts_lines(lines, self.set_id, self.labels, first)
        if err:
            raise Refused(err)
        return values


def lines_of(path):
    text = L.read_text(path)
    lines, err = L.split_lines(text)
    if err:
        raise Refused(err)
    return lines


def main(argv=None):
    ap = argparse.ArgumentParser(prog="verdicts.py", description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("check")
    c.add_argument("--index", required=True)
    c.add_argument("--filelists", required=True)
    c.add_argument("--tests", required=True, type=int)
    c.add_argument("--set", required=True)
    g = c.add_mutually_exclusive_group(required=True)
    g.add_argument("--verdicts")
    g.add_argument("--counts")
    g.add_argument("--closing")
    a = ap.parse_args(argv)
    if not L.full(L.SET_ID, a.set):
        ap.error("--set is not a set id")
    try:
        ck = Checker(a.index, a.filelists, a.tests, a.set)
    except (OSError, ValueError) as exc:
        L.refuse("refused: the INDEX: %s" % exc)
    try:
        if a.verdicts:
            lines = lines_of(a.verdicts)
            ck.verdict_lines(lines)
            L.emit({"ok": True, "form": "verdicts", "lines": len(lines)})
        if a.counts:
            values = ck.counts(lines_of(a.counts))
            L.emit({"ok": True, "form": "counts", "counts": values})
        lines = lines_of(a.closing)
        n = len(L.COUNTS_KEYS)
        values = ck.counts(lines[:n])
        rest = lines[n:]
        if not rest or not rest[-1].startswith("sha256: "):
            raise Refused("line %d: the closing block must end with `sha256: <hex>`" % len(lines))
        for i, line in enumerate(rest[:-1], n + 1):
            if line.startswith("sha256: "):
                raise Refused("line %d: text after the sha256 line" % (i + 1))
        vlines = rest[:-1]
        ck.verdict_lines(vlines, n + 1)
        sha = rest[-1][len("sha256: "):]
        if not L.full(L.SHA64, sha):
            raise Refused("line %d: the sha256 is not 64 lowercase hex digits" % len(lines))
        body = "".join(l + "\n" for l in vlines).encode("utf-8")
        if L.sha256_bytes(body) != sha:
            raise Refused("line %d: the sha256 is not the verdict file's" % len(lines))
        L.emit({"ok": True, "form": "closing", "counts": values, "lines": len(vlines), "sha256": sha})
    except Refused as exc:
        L.refuse("refused: %s" % exc)


if __name__ == "__main__":
    main()
