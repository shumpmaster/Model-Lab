"""AC1 [trace: V1 -> AC1] -- the owner opens experiments/E-003/ and finds C1, C2 and C3 as the exact
text the harness will insert, with kind, cause aimed at, how it is applied and its removal test; and
every brief and role file in every repository is as it was, since the changes exist only as these texts.

Needs no Builder code: file checks only.  Should PASS now.
"""
import os
import re
import subprocess
import unittest

from e003_support import (CHANGE_FILE, CHANGE_TEXT, FROZEN, ROOT, C1_TEXT, C2_TEXT, C3_TEXT)


def read(rel):
    with open(os.path.join(ROOT, rel), encoding="utf-8") as fh:
        return fh.read()


def fenced_blocks(section):
    return re.findall(r"^```[^\n]*\n(.*?)^```[ \t]*$", section, re.S | re.M)


def section_of(text, heading):
    m = re.search(r"^## %s[^\n]*\n(.*?)(?=^## |\Z)" % re.escape(heading), text, re.S | re.M)
    return m.group(1) if m else None


class TestAC1(unittest.TestCase):
    def test_each_change_file_holds_the_four_things(self):
        for cid, rel in CHANGE_FILE.items():
            text = read(rel)
            self.assertRegex(text, r"kind of work: ", cid + ": no kind")
            self.assertRegex(text, r"cause aimed at: ", cid + ": no cause aimed at")
            self.assertIsNotNone(section_of(text, "The text"), cid + ": no 'The text' section")
            self.assertIsNotNone(section_of(text, "Application rule"), cid + ": no application rule")
            removal = section_of(text, "Removal test")
            self.assertIsNotNone(removal, cid + ": no removal test")
            self.assertGreaterEqual(len(re.findall(r"^\d\. ", removal, re.M)), 3,
                                    cid + ": removal test lists fewer than three conditions")

    def test_kind_and_cause_are_the_registered_ones(self):
        want = {"C1": ("plans", "instructions"), "C2": ("built work", "material handed over"),
                "C3": ("research", "the check itself")}
        for cid, (kind, cause) in want.items():
            text = " ".join(read(CHANGE_FILE[cid]).split())
            self.assertIn("kind of work: " + kind, text, cid)
            self.assertIn("cause aimed at: " + cause, text, cid)

    def test_text_is_one_exact_fenced_block(self):
        for cid, rel in CHANGE_FILE.items():
            blocks = fenced_blocks(section_of(read(rel), "The text"))
            self.assertEqual(len(blocks), 1, cid + ": 'The text' must hold exactly one fenced block")
            self.assertEqual(blocks[0].rstrip("\n"), CHANGE_TEXT[cid], cid + ": the text differs from the frozen one")

    def test_word_counts_stated_in_the_files(self):
        self.assertEqual(len(C1_TEXT.split()), 35)   # "two sentences, 35 words"
        self.assertEqual(len(C2_TEXT.split()), 11)   # "10 fixed words ... 11 counting <list> as one word"
        self.assertEqual(len(C3_TEXT.split()), 64)   # "three sentences, 64 words"
        self.assertLess(max(len(t.split()) for t in CHANGE_TEXT.values()), 70)  # "each is under 70 words"

    def test_application_rules_say_change_arm_only_and_clean_removal(self):
        for cid, rel in CHANGE_FILE.items():
            text = read(rel)
            self.assertIn("byte for byte", section_of(text, "Removal test"), cid)
            app = section_of(text, "Application rule")
            if cid in ("C1", "C2"):
                self.assertIn("change\" arm", app, cid)
            else:
                self.assertIn("added", app, cid)

    def test_no_role_file_or_playbook_carries_a_change_text(self):
        """The changes exist only as these texts: no live role file holds a sentence of them."""
        needles = ["it is the role file of the agent that will check this plan",
                   "The inputs for this task, by path",
                   "A source you cannot open is not by itself a fault in the memo",
                   "Return the memo only for a fault you can show"]
        for base in (".claude/agents", "docs/playbooks"):
            for d, _, files in os.walk(os.path.join(ROOT, base)):
                for f in files:
                    with open(os.path.join(d, f), encoding="utf-8", errors="replace") as fh:
                        body = fh.read()
                    for n in needles:
                        self.assertNotIn(n, body, "%s/%s holds a change text" % (base, f))

    def test_no_existing_brief_record_was_altered_since_the_freeze(self):
        """AC1's "every brief ... is as it was": a brief record that existed at the freeze is not modified or
        deleted (new records may be added; docs/briefs/README.md is the folder's own text).  Reading of
        "every brief and role file in every repository": this repository's role files are covered by the
        test above (no change text is in any of them); a later, unrelated role-file update is legitimate and
        is not failed here; other repositories are outside what a Model-Lab file test can reach."""
        p = subprocess.run(["git", "-C", ROOT, "diff", "--name-status", "--diff-filter=MD", FROZEN, "HEAD", "--",
                            "docs/briefs", ":(exclude)docs/briefs/README.md"], capture_output=True, text=True)
        self.assertEqual(p.returncode, 0, p.stderr)
        self.assertEqual(p.stdout.strip(), "", "a brief record changed since the freeze:\n" + p.stdout)

    def test_no_brief_record_holds_a_change_text_as_a_paragraph_for_the_real_work(self):
        needles = ["Before you write, read <path>", "Before you write, read .claude/agents/",
                   "A source you cannot open is not by itself a fault in the memo"]
        d = os.path.join(ROOT, "docs", "briefs")
        for f in sorted(os.listdir(d)):
            if f.endswith(".md") and f != "README.md":
                with open(os.path.join(d, f), encoding="utf-8", errors="replace") as fh:
                    body = fh.read()
                for n in needles:
                    self.assertNotIn(n, body, "docs/briefs/%s holds a change text" % f)

    def test_the_freeze_covers_the_change_files(self):
        """The change texts are frozen with the spec: unchanged since the freeze commit."""
        p = subprocess.run(["git", "-C", ROOT, "diff", "--name-status", FROZEN, "HEAD", "--",
                            "experiments/E-003/C1-plans-read-the-check.md",
                            "experiments/E-003/C2-built-named-inputs.md",
                            "experiments/E-003/C3-research-check-what-it-can-open.md"],
                           capture_output=True, text=True)
        self.assertEqual(p.stdout.strip(), "", "a frozen change text changed:\n" + p.stdout)


if __name__ == "__main__":
    unittest.main()
