"""join-test: S-001/J5

J5 -- judge -> verdict record -> the Orchestrator's side.  "A test marked join-test: S-001/J5 covers it:
given the kind's INDEX and each export's file list as the export reader prints it, it fails on any line
of the verdict file, the counts block or the closing block whose fields are not exactly these, in these
forms and this order; on a cited path that is not in its export's file list; on a test number outside
the sheet's count; and on a label not in the INDEX.  So what can be carried is ids, numbers, the fixed
words, and paths of files already in the exports; no other text, a sheet's above all."

Interface named (e003_support.py): src/E-003/verdicts.py check --index FILE --filelists DIR --tests N
--set SETID (--verdicts FILE | --counts FILE | --closing FILE); exit 0 accepted, exit 1 refused with a
first line naming the offending line.  DIR holds `<label>.files`, one path per line, as the export reader
prints it.
GAPS: (1) the closing block's layout between its three parts is not given; the test lays it out as the 13
counts lines, then the verdict file's lines, then `sha256: <hex>` (the SHA-256 of the verdict file's
bytes), no separators; (2) "tokens, tool uses, seconds" are taken as decimal integers; (3) the judging
lead's own check "writes `<n>@-` for a citation outside these forms" is the lead's act; this check
accepts `<n>@-`.  FAILS until the Builder builds src/E-003/verdicts.py.
"""
import os

from e003_support import Base, sha256

SET = "S-001-built-1"
H = "cd" * 32
H2 = "ef" * 32
COMMIT = "0123456789abcdef0123456789abcdef01234567"
INDEX = ["L1\tbuilt\tsrc/E-003/exports/built/L1.bundle\t" + H + "\t" + H2,
         "L2\tbuilt\tsrc/E-003/exports/built/L2.bundle\t" + H + "\t" + H2,
         "L3\tbuilt\tsrc/E-003/exports/built/L3.bundle\t" + H + "\t" + H2, "last"]
FILES = {"L1": ["src/app.py", "README.md", "docs/a+b.md"], "L2": ["src/app.py"], "L3": ["x.txt"]}
TESTS = 4


def vline(label="L1", set_id=SET, sheet=H, brief=H2, model="claude-fable-5-1", verdict="FAIL",
          failed="2@src/app.py:14,3@README.md:1", follow="no", new="no", first="match", tr="clean",
          tokens="1200", tools="14", secs="88"):
    return "\t".join([label, set_id, sheet, brief, model, verdict, failed, follow, new, first, tr, tokens, tools, secs])


def counts(**kw):
    d = {"counts": SET, "index-commit": COMMIT, "judged": "3", "runs": "7", "reserve-used": "1",
         "tokens": "5000", "left-out": "L2,L3", "k1-canary": "unseen", "k2": "pass", "k3": "pass",
         "k4": "pass", "k5": "pass", "k7": "untested"}
    d.update(kw)
    return ["%s: %s" % (k, v) for k, v in d.items()]


class J5Base(Base):
    def setUp(self):
        super().setUp()
        self.index = self.write("INDEX", "\n".join(INDEX) + "\n")
        for lab, files in FILES.items():
            self.write("files/%s.files" % lab, "\n".join(files) + "\n")
        self.filedir = os.path.join(self.tmp, "files")

    def check(self, kind, text):
        f = self.write("in-%s.txt" % kind, text)
        return self.run_script("verdicts.py", "check", "--index", self.index, "--filelists", self.filedir,
                               "--tests", str(TESTS), "--set", SET, "--" + kind, f)

    def ok(self, kind, text, msg=""):
        p = self.check(kind, text)
        self.assertEqual(p.returncode, 0, "refused what it must accept (%s): %s" % (msg, (p.stdout + p.stderr)[:300]))

    def bad(self, kind, text, msg=""):
        p = self.check(kind, text)
        self.assertEqual(p.returncode, 1, "accepted what it must refuse: " + msg)
        return p


class TestJ5VerdictFile(J5Base):
    def file(self, *lines):
        return "\n".join(lines) + "\n"

    def test_good_lines_are_accepted(self):
        self.ok("verdicts", self.file(vline(), vline("L2", verdict="PASS", failed="-"),
                                      vline("L3", verdict="none", failed="-", follow="yes", new="yes", first="differs",
                                            tr="leak@41")))
        self.ok("verdicts", self.file(vline(failed="1@-,2@src/app.py:1")), "n@- is the lead's own outside-citation form")
        self.ok("verdicts", self.file(vline(failed="4@docs/a+b.md:999999")))

    def test_label_not_in_the_index(self):
        self.bad("verdicts", self.file(vline("L9")), "label")

    def test_wrong_set_id(self):
        self.bad("verdicts", self.file(vline(set_id="S-001-plans-1")))

    def test_hashes_are_64_lowercase_hex(self):
        for bad in (H[:63], H.upper(), "g" * 64, H + "0", ""):
            self.bad("verdicts", self.file(vline(sheet=bad)), "sheet " + bad)
            self.bad("verdicts", self.file(vline(brief=bad)), "brief " + bad)

    def test_served_model_form(self):
        for bad in ("", "has space", "x" * 65, "a/b"):
            self.bad("verdicts", self.file(vline(model=bad)), repr(bad))

    def test_verdict_words(self):
        for bad in ("Pass", "FAIL ", "MAYBE", "", "Verdict: PASS"):
            self.bad("verdicts", self.file(vline(verdict=bad)), repr(bad))

    def test_failed_test_number_must_be_within_the_sheets_count_and_unique(self):
        for bad in ("0@src/app.py:1", "5@src/app.py:1", "99@src/app.py:1", "2@src/app.py:1,2@src/app.py:2",
                    "-1@src/app.py:1", "a@src/app.py:1"):
            self.bad("verdicts", self.file(vline(failed=bad)), bad)

    def test_cited_path_must_be_in_the_exports_file_list(self):
        self.bad("verdicts", self.file(vline(failed="1@not/in/export.py:3")), "unlisted path")
        self.bad("verdicts", self.file(vline("L2", failed="1@README.md:1")), "path of another export")

    def test_cited_path_and_line_forms(self):
        for bad in ("1@../etc/passwd:1", "1@/src/app.py:1", "1@src/../src/app.py:1", "1@src/app.py:",
                    "1@src/app.py:x", "1@src/app.py:1234567", "1@src/ app.py:1", "1@src/app.py", "1@src/app.py:1;",
                    "1@" + "a" * 201 + ":1", "1@:1", "1 src/app.py:1"):
            self.bad("verdicts", self.file(vline(failed=bad)), bad)

    def test_followup_session_firstmessage_transcript_words(self):
        for kw, bad in (("follow", "maybe"), ("follow", "Yes"), ("new", "1"), ("first", "equal"),
                        ("tr", "leak"), ("tr", "leak@"), ("tr", "leak@x"), ("tr", "dirty"), ("tr", "leak@-1")):
            self.bad("verdicts", self.file(vline(**{kw: bad})), "%s=%s" % (kw, bad))

    def test_numbers_are_decimal_integers(self):
        for kw in ("tokens", "tools", "secs"):
            for bad in ("", "x", "1.5", "-3", "1e3"):
                self.bad("verdicts", self.file(vline(**{kw: bad})), "%s=%r" % (kw, bad))

    def test_field_count_separator_and_free_text(self):
        good = vline()
        self.bad("verdicts", self.file(good + "\textra"), "15 fields")
        self.bad("verdicts", self.file("\t".join(good.split("\t")[:-1])), "13 fields")
        self.bad("verdicts", self.file(good.replace("\t", " ")), "spaces for tabs")
        self.bad("verdicts", self.file(good, "a line of free text that is not a record"), "stray line")
        self.bad("verdicts", self.file(good, ""), "blank line")
        self.bad("verdicts", self.file(vline(failed="1@src/app.py:1 STANDIN-T1: the piece cites a file")), "sheet text")

    def test_the_refusal_names_the_offending_line(self):
        p = self.bad("verdicts", self.file(vline(), vline("L9")))
        self.assertRegex((p.stdout + p.stderr).splitlines()[0], r"\b2\b")


class TestJ5Counts(J5Base):
    def text(self, lines):
        return "\n".join(lines) + "\n"

    def test_good_counts_block(self):
        self.ok("counts", self.text(counts()))
        self.ok("counts", self.text(counts(**{"left-out": "-"})))
        self.ok("counts", self.text(counts(**{"k1-canary": "seen", "k7": "fail"})))

    def test_bad_values(self):
        for k, v in (("counts", "S-001-other-1"), ("index-commit", COMMIT[:39]), ("index-commit", COMMIT.upper()),
                     ("judged", "x"), ("runs", "-1"), ("reserve-used", "1.5"), ("tokens", ""),
                     ("left-out", "L9"), ("left-out", "L1;L2"), ("left-out", "L1, L2"), ("left-out", ""),
                     ("k1-canary", "maybe"), ("k2", "ok"), ("k7", "PASS")):
            self.bad("counts", self.text(counts(**{k: v})), "%s=%r" % (k, v))

    def test_bad_shape(self):
        lines = counts()
        self.bad("counts", self.text(lines + ["note: free text"]), "extra line")
        self.bad("counts", self.text(lines[:-1]), "missing k7")
        self.bad("counts", self.text(lines[:2] + lines[3:]), "missing judged")
        swapped = list(lines)
        swapped[3], swapped[4] = swapped[4], swapped[3]
        self.bad("counts", self.text(swapped), "order")
        self.bad("counts", self.text(lines[:-1] + ["k6: pass", lines[-1]]), "k6 line")
        self.bad("counts", self.text(lines + lines), "doubled")


class TestJ5Closing(J5Base):
    def closing(self, verdict_lines, sha=None, counts_lines=None):
        vf = "\n".join(verdict_lines) + "\n"
        return "\n".join(counts_lines or counts()) + "\n" + vf + "sha256: %s\n" % (sha or sha256(vf))

    def test_good_closing_block(self):
        self.ok("closing", self.closing([vline(), vline("L2", verdict="PASS", failed="-")]))

    def test_sha256_must_equal_the_verdict_files(self):
        self.bad("closing", self.closing([vline()], sha=H), "wrong sha256")
        self.bad("closing", self.closing([vline()], sha=sha256("x").upper()), "uppercase sha256")

    def test_a_bad_verdict_line_inside_is_refused(self):
        self.bad("closing", self.closing([vline(), vline("L9")]), "label not in INDEX")
        self.bad("closing", self.closing([vline(failed="9@src/app.py:1")]), "test number out of count")
        self.bad("closing", self.closing([vline(failed="1@nope.py:1")]), "path not in export")

    def test_a_bad_counts_part_is_refused(self):
        self.bad("closing", self.closing([vline()], counts_lines=counts(judged="x")))

    def test_text_after_the_sha_line_is_refused(self):
        self.bad("closing", self.closing([vline()]) + "and some prose\n")
