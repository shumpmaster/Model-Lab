"""AC11 [trace: V2 -> AC11] -- when a kept change is removed, by its removal test or at the operating
model's scheduled review, the brief or role file returns byte for byte to its text without the change.

Interface named (e003_support.py): src/E-003/change.py apply | remove | verify-removal --change Cn
--control FILE --changed FILE --fill TEXT -> {"clean": bool}.  Removal takes out the change paragraph and
its blank line and nothing else.  FAILS until src/E-003/change.py is built.
The role files in this repository are also checked unchanged in test_ac01_change_texts.py.
"""
import json
import os

from e003_support import Base, ROOT, filled

TEXTS = {
    "plain": "Intro.\n\nTASK STATEMENT: do it.\n\nReturn it.\n",
    "no trailing newline": "Intro.\n\nTASK STATEMENT: do it.\n\nReturn it.",
    "crlf": "Intro.\r\n\r\nTASK STATEMENT: do it.\r\n\r\nReturn it.\r\n",
    "extra blank lines": "Intro.\n\n\n\nTASK STATEMENT: do it.\n\n\nReturn it.\n\n",
    "unicode": "Intro é中.\n\nTASK STATEMENT: do it — now.\n\nReturn ✓.\n",
    "task last": "Intro.\n\nTASK STATEMENT: do it.\n",
    "single paragraph": "TASK STATEMENT: do it.\n",
}
FILLS = {"C1": ".claude/agents/critic.md", "C2": "specs/S-1.md:3-9, src/a.py", "C3": ""}


class TestAC11(Base):
    def apply(self, change, text):
        b = self.write("b.md", text)
        t = self.write("t.txt", "TASK STATEMENT: do it.")
        with open(b, "rb") as fh:
            self.assertEqual(fh.read(), text.encode("utf-8"))
        return self.decide("change.py", "apply", "--change", change, "--brief", b, "--task-statement", t,
                           "--fill", FILLS[change])["brief"]

    def remove(self, change, text):
        b = self.write("changed.md", text)
        return self.decide("change.py", "remove", "--change", change, "--brief", b, "--fill", FILLS[change])["brief"]

    def test_apply_then_remove_returns_the_text_byte_for_byte(self):
        for change in ("C1", "C2", "C3"):
            for name, text in TEXTS.items():
                if "\r" in text:
                    continue          # CRLF handled below: bytes in, bytes out
                changed = self.apply(change, text)
                self.assertNotEqual(changed, text, "%s/%s: the change must change the brief" % (change, name))
                self.assertEqual(self.remove(change, changed), text, "%s/%s" % (change, name))

    def test_crlf_briefs_come_back_byte_for_byte(self):
        text = TEXTS["crlf"]
        b = self.write("crlf.md", text)
        with open(b, "wb") as fh:
            fh.write(text.encode("utf-8"))
        t = self.write("t.txt", "TASK STATEMENT: do it.")
        p = self.run_script("change.py", "apply", "--change", "C3", "--brief", b, "--task-statement", t, "--fill", "")
        self.assertEqual(p.returncode, 0, p.stderr[-300:])
        changed = json.loads(p.stdout)["brief"]
        c = os.path.join(self.tmp, "crlf-changed.md")
        with open(c, "wb") as fh:
            fh.write(changed.encode("utf-8"))
        back = self.decide("change.py", "remove", "--change", "C3", "--brief", c, "--fill", "")["brief"]
        self.assertEqual(back.encode("utf-8"), text.encode("utf-8"))

    def test_removal_takes_out_only_the_paragraph(self):
        text = TEXTS["plain"]
        changed = self.apply("C1", text)
        tampered = changed.replace("Return it.", "Return it, please.")
        self.assertEqual(self.remove("C1", tampered), text.replace("Return it.", "Return it, please."))

    def test_removing_where_the_paragraph_is_absent_changes_nothing(self):
        text = TEXTS["plain"]
        self.assertEqual(self.remove("C2", text), text)

    def test_the_per_pair_clean_removal_check(self):
        text = TEXTS["plain"]
        changed = self.apply("C2", text)
        control, chg = self.write("control.md", text), self.write("chg.md", changed)
        ok = self.decide("change.py", "verify-removal", "--change", "C2", "--control", control, "--changed", chg,
                         "--fill", FILLS["C2"])
        self.assertTrue(ok["clean"])
        other = self.write("chg2.md", changed.replace("Intro.", "Introduction."))
        bad = self.decide("change.py", "verify-removal", "--change", "C2", "--control", control, "--changed", other,
                          "--fill", FILLS["C2"])
        self.assertFalse(bad["clean"], "a second difference is a set-up fault")

    def test_a_role_file_with_the_paragraph_inserted_comes_back(self):
        role = open(os.path.join(ROOT, ".claude", "agents", "critic.md"), encoding="utf-8", newline="").read()
        first_para_end = role.index("\n\n") + 2
        changed = role[:first_para_end] + filled("C3", "") + "\n\n" + role[first_para_end:]
        self.assertEqual(self.remove("C3", changed), role)
