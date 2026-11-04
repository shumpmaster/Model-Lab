"""join-test: S-001/J4

J4 -- held-back check -> the sheets repository -> judge.  "A test marked join-test: S-001/J4 covers it,
in Model-Lab, with a stand-in sheet that is no real check: the fill script puts the stand-in's text in
the brief only when its SHA-256 matches the given fingerprint, refuses on a mismatch, and writes nothing
but the J5 line; and the block parser accepts exactly the three forms above, each line in its form and
order (counts as decimal integers, the commit as 40 lowercase hex digits, the fingerprint as 64, the set
id as `S-001-<built, plans or research>-<n>`, the served model as 1 to 64 characters from letters,
digits, `.`, `_` and `-`, each k result one of the three words, and `k1-canary` one of `unseen`, `seen`
and `unread`), and refuses any other line, form or order."

Interfaces named (e003_support.py): src/E-003/fill_judge_brief.py (--sheet --fingerprint --fill --label
--copy-path --out) and src/E-003/block.py parse (stdin block; exit 0 + JSON with "form", or exit 1).
Uses export.py make to produce a real fill file.
GAPS: (1) the fill script's command line and the keys of <label>.fill.json are not given; (2) "writes
nothing but the J5 line" is read as: the only file it creates is --out and its stdout, if any, holds no
sheet text; (3) the spec says both that k1-canary may be unseen/seen/unread and that "in the full form it
is `unseen`": the test accepts `unseen` in the full form and does not test `seen`/`unread` there;
(4) it fixes no cross-line rule (e.g. which `stopped:` goes with which `pack:`), so none is tested.
FAILS until the Builder builds both scripts.
"""
import os
import re

from e003_support import Base, STAND_IN_SHEET, STAND_IN_MARKERS, sha256, commit_files, git

SET = "S-001-built-1"
COMMIT = "0123456789abcdef0123456789abcdef01234567"
FP = "ab" * 32

FULL = ["set: " + SET, "repository-commit: " + COMMIT, "path: holdouts/%s.md" % SET, "fingerprint: " + FP,
        "tests: 3", "pack: match", "scan: clean", "model: claude-fable-5-1", "runs: 1", "tokens: 41234",
        "k1-canary: unseen", "k2: pass", "k3: pass", "k4: pass", "k5: untested"]
STOPPED = ["set: " + SET, "pack: differs", "stopped: pack", "runs: 0", "tokens: 120",
           "k1-canary: unread", "k2: untested", "k3: untested", "k4: untested", "k5: untested"]
VOID = ["set: " + SET, "scan: void", "hit: 57", "runs: 1", "tokens: 9000",
        "k1-canary: unseen", "k2: pass", "k3: pass", "k4: fail", "k5: pass"]


def block(lines):
    return "\n".join(lines) + "\n"


class TestJ4Parser(Base):
    def parse(self, lines):
        return self.run_script("block.py", "parse", stdin=block(lines) if isinstance(lines, list) else lines)

    def accepted(self, lines, form=None):
        p = self.parse(lines)
        self.assertEqual(p.returncode, 0, "refused a block it must accept: %s" % p.stdout[:200] + p.stderr[:200])
        if form:
            import json
            self.assertEqual(json.loads(p.stdout)["form"], form)

    def refused(self, lines, why=""):
        p = self.parse(lines)
        self.assertEqual(p.returncode, 1, "accepted a block it must refuse (%s)" % why)

    def test_the_three_forms_are_accepted(self):
        self.accepted(FULL, "full")
        self.accepted(STOPPED, "stopped")
        self.accepted(VOID, "void")

    def test_scan_unread_and_each_stopped_value_and_k_words(self):
        self.accepted([l.replace("scan: clean", "scan: unread") for l in FULL], "full")
        for s in ("k1", "k2", "k3", "k4", "pack"):
            self.accepted([l.replace("stopped: pack", "stopped: " + s) for l in STOPPED], "stopped")
        for w in ("pass", "fail", "untested"):
            self.accepted([l.replace("k2: pass", "k2: " + w) for l in FULL], "full")
        for c in ("unseen", "seen", "unread"):
            self.accepted([l.replace("k1-canary: unread", "k1-canary: " + c) for l in STOPPED], "stopped")
            self.accepted([l.replace("k1-canary: unseen", "k1-canary: " + c) for l in VOID], "void")

    def test_set_id_forms(self):
        for good in ("S-001-built-1", "S-001-plans-2", "S-001-research-10"):
            self.accepted([l.replace(SET, good) for l in FULL], "full")
        for bad in ("S-001-other-1", "S-002-built-1", "S-001-built-", "S-001-built-x", "s-001-built-1",
                    "S-001-built-1-2", "S-001-Built-1"):
            self.refused([l.replace(SET, bad) for l in FULL], bad)

    def test_commit_must_be_40_lowercase_hex(self):
        for bad in (COMMIT[:39], COMMIT + "0", COMMIT.upper(), "g" * 40, "abc1234"):
            self.refused([l.replace(COMMIT, bad) for l in FULL], bad)

    def test_fingerprint_must_be_64_lowercase_hex(self):
        for bad in (FP[:63], FP + "0", FP.upper(), "z" * 64):
            self.refused([l.replace("fingerprint: " + FP, "fingerprint: " + bad) for l in FULL], bad)

    def test_counts_are_decimal_integers(self):
        for key in ("tests", "tokens"):
            for bad in ("three", "3.5", "-1", "", "0x10", "1,000"):
                self.refused([re.sub(r"^%s: .*" % key, "%s: %s" % (key, bad), l) for l in FULL], key + " " + bad)
        for bad in ("one", "1.0", "-1"):
            self.refused([l.replace("hit: 57", "hit: " + bad) for l in VOID], "hit " + bad)

    def test_runs_values_by_form(self):
        self.refused([l.replace("runs: 1", "runs: 0") for l in FULL], "full form has runs: 1")
        self.refused([l.replace("runs: 1", "runs: 2") for l in FULL])
        self.refused([l.replace("runs: 0", "runs: 2") for l in STOPPED], "stopped: 0 or 1")
        self.accepted([l.replace("runs: 0", "runs: 1") for l in STOPPED], "stopped")
        self.refused([l.replace("runs: 1", "runs: 0") for l in VOID], "void has runs: 1")

    def test_served_model_is_1_to_64_characters_of_the_allowed_set(self):
        self.accepted([l.replace("claude-fable-5-1", "a") for l in FULL])
        self.accepted([l.replace("claude-fable-5-1", "A.b_c-9" * 9 + "x") for l in FULL])  # 64
        for bad in ("", "x" * 65, "has space", "slash/x", "colon:x", "semi;x"):
            self.refused([re.sub(r"^model: .*", "model: " + bad, l) for l in FULL], repr(bad))

    def test_k_results_and_canary_words_are_closed_sets(self):
        for bad in ("ok", "PASS", "passed", ""):
            self.refused([l.replace("k3: pass", "k3: " + bad) for l in FULL], bad)
        for bad in ("saw", "SEEN", "none", ""):
            self.refused([l.replace("k1-canary: unseen", "k1-canary: " + bad) for l in FULL], bad)

    def test_pack_scan_path_lines(self):
        self.refused([l.replace("pack: match", "pack: maybe") for l in FULL])
        self.refused([l.replace("scan: clean", "scan: dirty") for l in FULL])
        self.refused([l.replace("path: holdouts/%s.md" % SET, "path: holdouts/other.md") for l in FULL])
        self.refused([l.replace("path: holdouts/%s.md" % SET, "path: ../holdouts/%s.md" % SET) for l in FULL])
        self.refused([l.replace("scan: void", "scan: clean") for l in VOID], "void form keeps scan: void")

    def test_any_other_line_form_or_order_is_refused(self):
        self.refused(FULL + ["notes: free text"], "extra line")
        self.refused(FULL + ["1. a stolen test line from a sheet"], "sheet text")
        self.refused(FULL[:-1], "missing k5")
        self.refused(FULL[1:], "missing set")
        swapped = list(FULL)
        swapped[4], swapped[5] = swapped[5], swapped[4]
        self.refused(swapped, "order")
        self.refused(FULL + FULL, "doubled")
        self.refused(VOID[:2] + [STOPPED[2]] + VOID[3:], "mixed forms")
        self.refused([FULL[0], VOID[1]] + FULL[1:], "mixed forms 2")
        self.refused([""] + FULL, "leading blank line")
        self.refused(FULL[:3] + [""] + FULL[3:], "blank line inside")
        self.refused("", "empty")

    def test_space_after_colon_is_exact(self):
        self.refused([l.replace("tests: 3", "tests:3") for l in FULL])
        self.refused([l.replace("tests: 3", "tests:  3") for l in FULL])
        self.refused([l + " " if l.startswith("runs") else l for l in FULL], "trailing space")


class TestJ4Fill(Base):
    def setUp(self):
        super().setUp()
        src = self.new_repo("src")
        start = commit_files(src, {"a.txt": "a\n"}, "s", when="2026-11-01T10:00:00Z")
        final = commit_files(src, {"b.txt": "b\n"}, "f", when="2026-11-02T10:00:00Z")
        out = os.path.join(self.tmp, "exports")
        os.makedirs(out)
        p = self.run_script("export.py", "make", "--kind", "built", "--repo", src, "--start", start,
                            "--final", final, "--label", "L7", "--out", out, "--checker-role", "reviewer",
                            "--role-file", ".claude/agents/reviewer.md", "--task-statement-path", "specs/S-100.md")
        self.assertEqual(p.returncode, 0, p.stderr[-300:])
        self.fill = os.path.join(out, "L7.fill.json")
        if not os.path.isfile(self.fill):
            for d, _, fs in os.walk(out):
                for f in fs:
                    if f == "L7.fill.json":
                        self.fill = os.path.join(d, f)
        self.sheet = self.write("sheet/holdouts/%s.md" % SET, STAND_IN_SHEET)
        self.fp = sha256(STAND_IN_SHEET)

    def fillrun(self, sheet=None, fp=None, out="brief.txt"):
        outp = os.path.join(self.tmp, "work", out)
        os.makedirs(os.path.dirname(outp), exist_ok=True)
        return self.run_script("fill_judge_brief.py", "--sheet", sheet or self.sheet, "--fingerprint", fp or self.fp,
                               "--fill", self.fill, "--label", "L7", "--copy-path", os.path.join(self.tmp, "copy"),
                               "--out", outp), outp

    def test_a_matching_fingerprint_puts_the_sheet_in_the_brief(self):
        p, outp = self.fillrun()
        self.assertEqual(p.returncode, 0, p.stderr[-400:])
        # E-002's template breaks lines inside phrases ("Judge it\nagainst:") and E-003 changes nothing else
        # in it, so every phrase is matched with whitespace collapsed.
        text = " ".join(open(outp, encoding="utf-8").read().split())
        self.assertIn(" ".join(STAND_IN_SHEET.split()), text, "the check in full")
        a, b, c = text.find("Judge it against"), text.find("Apply this check:"), text.find("The work fails if any test of this check fails.")
        self.assertTrue(0 <= a < b < c, "E-003 Step 4 change 4: after 'Judge it against', then the check, then the failing rule")
        self.assertLess(b, text.find("STANDIN-T1"))
        self.assertLess(text.find("STANDIN-T3"), c)
        self.assertIn("Do not start background tasks", text)
        self.assertIn("the numbers of the tests of the check that failed, each citing file:line", text)
        self.assertIn("L7", text)
        self.assertNotRegex(text, r"(?i)\barm\b")

    def test_the_same_inputs_give_the_same_brief_byte_for_byte(self):
        _, a = self.fillrun(out="a.txt")
        _, b = self.fillrun(out="b.txt")
        self.assertEqual(open(a, "rb").read(), open(b, "rb").read())

    def test_a_mismatching_fingerprint_is_refused_and_nothing_is_written(self):
        wrong = [sha256("another sheet"), self.fp[:-1] + ("0" if self.fp[-1] != "0" else "1"), self.fp.upper(), self.fp[:63]]
        for fp in wrong:
            p, outp = self.fillrun(fp=fp)
            self.assertEqual(p.returncode, 1, fp)
            self.assertFalse(os.path.exists(outp), "no brief may be written on a mismatch")
            for m in STAND_IN_MARKERS:
                self.assertNotIn(m, p.stdout + p.stderr, "a refusal must not echo the sheet")

    def test_a_sheet_changed_by_one_byte_is_refused(self):
        changed = self.write("sheet2/holdouts/%s.md" % SET, STAND_IN_SHEET.replace("not a real", "not a rea1"))
        p, outp = self.fillrun(sheet=changed)
        self.assertEqual(p.returncode, 1)
        self.assertFalse(os.path.exists(outp))

    def test_it_writes_nothing_but_its_brief_and_prints_no_sheet_text(self):
        def snap():
            return {os.path.join(d, f) for d, _, fs in os.walk(self.tmp) for f in fs}
        before = snap()
        p, outp = self.fillrun()
        self.assertEqual(p.returncode, 0, p.stderr[-300:])
        after = snap()
        self.assertEqual(after - before, {outp}, "the only new file is the brief")
        for m in STAND_IN_MARKERS:
            self.assertNotIn(m, p.stdout + p.stderr)
        self.assertLessEqual(len([l for l in p.stdout.splitlines() if l.strip()]), 1, "at most the one J5 line")
