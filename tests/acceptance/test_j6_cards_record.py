"""join-test: S-001/J6

J6 -- owner's card -> result record: the card's output label, its group (G1, G2 or G3), the order it was
drawn in, and the owner's answer (yes, no, can't tell) in the owner's words, filed under decisions/
questions/ as an owner's answer is, in one file per kind, decisions/questions/E-003-<kind>-cards.md, so
the Reviewer's pack can name it (J7); then the pair's class worked out again.  The card shows the verdict,
the failed test numbers and their cited lines from J5, and names the sheets repository's
`holdouts/<set id>.md` for the owner to open; neither the card nor the file holds the sheet's text.
Awkward cases: a group too small; fewer than 6 answered after 8 cards (more drawn, up to 12); fewer than 6
after 12 ("too few answered"); a built output whose locked checks failed (never drawn); the owner answers
"no" in a pair the other arm also passed (the pair stays concordant); the owner quotes a test's text in an
answer (the Chief of Staff files the answer with that quotation replaced by the test's number, and says
so in the file).

Interface named (e003_support.py): src/E-003/cards.py file --kind K --set SETID --cards FILE --answers
FILE --out ROOT [--sheet FILE] -> writes ROOT/decisions/questions/E-003-<kind>-cards.md.  The draw, the
group-size, the 8-to-12 and the locked-checks cases, and the re-scoring, are exercised in
test_ac06_owner_cards.py.  GAPS: the file's layout is not given; the test looks for each card's label,
group, order and answer text, and for the sheet-text and arm-label absences.  FAILS until built.
"""
import json
import os
import re

from e003_support import Base, STAND_IN_SHEET, STAND_IN_MARKERS

SET = "S-001-built-1"
CARDS = {"cards": [
    {"label": "m81", "group": "G1", "order": 1, "verdict": "FAIL", "failed": "2@src/a.py:3", "open": "holdouts/%s.md" % SET},
    {"label": "m17", "group": "G2", "order": 2, "verdict": "PASS", "failed": "-", "open": "holdouts/%s.md" % SET},
    {"label": "m40", "group": "G3", "order": 3, "verdict": "FAIL", "failed": "1@src/b.py:9,3@src/c.py:2",
     "open": "holdouts/%s.md" % SET},
]}
ANSWERS = {"m81": "Yes, this should have gone back, the second test is plainly right.",
           "m17": "no",
           "m40": "can't tell without reading the whole thing"}


class TestJ6(Base):
    def file(self, kind="built", answers=None, sheet=True):
        cards = self.write("cards.json", json.dumps(CARDS))
        ans = self.write("answers.json", json.dumps(answers or ANSWERS))
        sh = self.write("sheet.md", STAND_IN_SHEET)
        args = ["file", "--kind", kind, "--set", SET, "--cards", cards, "--answers", ans, "--out", self.tmp]
        if sheet:
            args += ["--sheet", sh]
        p = self.run_script("cards.py", *args)
        self.assertEqual(p.returncode, 0, p.stderr[-400:])
        path = os.path.join(self.tmp, "decisions", "questions", "E-003-%s-cards.md" % kind)
        self.assertTrue(os.path.isfile(path), "one file per kind: decisions/questions/E-003-<kind>-cards.md")
        return open(path, encoding="utf-8").read()

    def test_the_file_holds_label_group_order_and_the_owners_words(self):
        text = self.file()
        for c in CARDS["cards"]:
            self.assertIn(c["label"], text)
        for words in ANSWERS.values():
            self.assertIn(words, text, "the owner's answer in the owner's words")
        for lab, group, order in (("m81", "G1", 1), ("m17", "G2", 2), ("m40", "G3", 3)):
            row = [l for l in text.splitlines() if lab in l]
            self.assertTrue(row, lab)
            self.assertIn(group, "\n".join(row))
            self.assertRegex("\n".join(row), r"\b%d\b" % order)

    def test_the_file_names_the_sheet_to_open_but_holds_none_of_its_text(self):
        text = self.file()
        self.assertIn("holdouts/%s.md" % SET, text)
        for m in STAND_IN_MARKERS:
            self.assertNotIn(m, text)
        for line in STAND_IN_SHEET.splitlines()[1:]:
            self.assertNotIn(line.split(": ", 1)[-1], text)

    def test_a_quoted_test_text_is_replaced_by_its_number_and_the_file_says_so(self):
        quoted = dict(ANSWERS)
        quoted["m81"] = ('Yes. "STANDIN-T2: the piece contradicts the task it was set." is true of it, '
                         'and the rest is fine.')
        text = self.file(answers=quoted)
        for m in STAND_IN_MARKERS:
            self.assertNotIn(m, text)
        self.assertNotIn("contradicts the task it was set", text)
        self.assertRegex(text, r"(?i)test\s*2|\(2\)|\[2\]")
        self.assertRegex(text, r"(?i)replaced")
        self.assertIn("the rest is fine", text, "the rest of the owner's words stays")

    def test_one_file_per_kind_and_no_arm_labels(self):
        a = self.file("built")
        b = self.file("plans")
        self.assertTrue(os.path.isfile(os.path.join(self.tmp, "decisions/questions/E-003-built-cards.md")))
        self.assertTrue(os.path.isfile(os.path.join(self.tmp, "decisions/questions/E-003-plans-cards.md")))
        for t in (a, b):
            self.assertIsNone(re.search(r"(?i)\b(control|change arm|no-change arm)\b", t))
