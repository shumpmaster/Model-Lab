"""join-test: S-001/J1

J1 -- change text -> arm copy: the change paragraph (experiments/E-003/C<n>-*.md, the fenced block),
with its fill (<path> for C1; <list> for C2), inserted as its own paragraph after the task statement of
the "change" arm's brief (for C3, the source check's brief).  Awkward cases: no separate task statement
(insert after its first paragraph and record it); C1's plan-check role file absent at the start commit
(not eligible); C2's list holds only the spec (eligible); C2's task names no spec (the list is the paths
the task names); C2's list empty (not eligible).

Interfaces named (e003_support.py): src/E-003/change.py apply | remove | fill-c1 | fill-c2.
GAPS: the spec does not say how the harness finds "the task statement" in a brief, so apply takes it as
a file (--task-statement) naming a paragraph of the brief; nor how a cited stage's line range is derived
(the test assumes: from its heading to the next heading of the same or higher level).
These tests FAIL until the Builder builds src/E-003/change.py.
"""
import os
import re

from e003_support import Base, ROOT, CHANGE_TEXT, filled, git, init_repo, commit_files

BRIEF = ("# Brief -- X-1, writer\n\nYou are the writer. Work only from the files in this copy.\n\n"
         "TASK STATEMENT: write the plan for the reminder feature, as specs/S-777.md.\n\n"
         "Return a hand-back with the spec's path.\n")
TASK = "TASK STATEMENT: write the plan for the reminder feature, as specs/S-777.md."


class TestJ1Apply(Base):
    def apply(self, change, brief=BRIEF, task=TASK, fill=""):
        b = self.write("brief.md", brief)
        t = self.write("task.txt", task)
        return self.decide("change.py", "apply", "--change", change, "--brief", b, "--task-statement", t,
                           "--fill", fill)

    def expected(self, change, fill, brief=BRIEF, task=TASK):
        paras = brief.split("\n\n")
        i = [p.strip() for p in paras].index(task.strip())
        return "\n\n".join(paras[:i + 1] + [filled(change, fill)] + paras[i + 1:])

    def test_each_change_is_its_own_paragraph_after_the_task_statement(self):
        for change, fill in (("C1", ".claude/agents/critic.md"),
                             ("C2", "specs/S-777.md:4-9, src/a.py"), ("C3", "")):
            out = self.apply(change, fill=fill)
            self.assertEqual(out["brief"], self.expected(change, fill), change)
            self.assertEqual(out["placement"], "after-task-statement", change)

    def test_the_text_is_the_fenced_block_with_the_fill_and_nothing_else_added(self):
        out = self.apply("C1", fill=".claude/agents/critic.md")["brief"]
        self.assertIn("Before you write, read .claude/agents/critic.md: it is the role file of the agent "
                      "that will check this plan.", out)
        self.assertNotIn("<path>", out)
        self.assertEqual(len(out) - len(BRIEF), len(filled("C1", ".claude/agents/critic.md")) + 2)

    def test_c2_fill_is_the_list(self):
        out = self.apply("C2", fill="specs/S-777.md, src/a.py")["brief"]
        self.assertIn("The inputs for this task, by path: specs/S-777.md, src/a.py. Read these first.", out)
        self.assertNotIn("<list>", out)

    def test_no_separate_task_statement_goes_after_the_first_paragraph_and_is_recorded(self):
        brief = "First paragraph that is the whole task.\n\nSecond paragraph of context.\n\nThird.\n"
        out = self.apply("C1", brief=brief, task="", fill=".claude/agents/critic.md")
        self.assertEqual(out["placement"], "after-first-paragraph")
        self.assertTrue(out["recorded"], "the harness must record that the task statement was not separate")
        paras = brief.split("\n\n")
        self.assertEqual(out["brief"], "\n\n".join([paras[0], filled("C1", ".claude/agents/critic.md")] + paras[1:]))

    def test_change_arm_with_the_paragraph_removed_is_the_no_change_brief_byte_for_byte(self):
        for change, fill in (("C1", ".claude/agents/critic.md"), ("C2", "specs/S-777.md"), ("C3", "")):
            out = self.apply(change, fill=fill)["brief"]
            b = self.write("changed.md", out)
            back = self.decide("change.py", "remove", "--change", change, "--brief", b, "--fill", fill)["brief"]
            self.assertEqual(back, BRIEF, change)

    def test_applying_changes_nothing_live(self):
        before = git(ROOT, "status", "--porcelain")
        self.apply("C1", fill=".claude/agents/critic.md")
        self.assertEqual(git(ROOT, "status", "--porcelain"), before)


class TestJ1Fills(Base):
    def repo(self):
        r = self.new_repo()
        commit_files(r, {".claude/agents/critic.md": "critic\n", "README.md": "x\n"}, "base")
        return r

    def test_c1_path_is_the_plan_check_role_file_at_the_start_commit(self):
        r = self.repo()
        start = git(r, "rev-parse", "HEAD")
        out = self.decide("change.py", "fill-c1", "--repo", r, "--commit", start)
        self.assertTrue(out["eligible"])
        self.assertEqual(out["fill"], ".claude/agents/critic.md")

    def test_c1_without_the_role_file_at_the_start_commit_is_not_eligible(self):
        r = self.new_repo()
        start = commit_files(r, {"README.md": "x\n"}, "no role file yet")
        commit_files(r, {".claude/agents/critic.md": "later\n"}, "role file added after the start")
        out = self.decide("change.py", "fill-c1", "--repo", r, "--commit", start)
        self.assertFalse(out["eligible"])
        self.assertTrue(out["reason"])

    def c2_repo(self):
        r = self.new_repo()
        spec = "# Spec S-009\n\n### Stage 1\nalpha\nbeta\n\n### Stage 2\ngamma\ndelta\nepsilon\n\n### Stage 3\nzeta\n"
        commit_files(r, {
            "specs/S-009.md": spec,
            "decisions/questions/P-009-ruling.md": "Stage 2 is ruled in decisions/questions/P-009-ruling.md\n",
            "decisions/questions/P-010-other.md": "unrelated\n",
            "tests/acceptance/test_s009.py": "# join-test: S-009/J1\n",
            "tests/acceptance/test_other.py": "# nothing\n",
            "checks/s009_check.py": "# the S-009 check\n",
            "src/lib/a.py": "a\n", "src/lib/b.py": "b\n", "src/app.py": "app\n",
        }, "start")
        start = git(r, "rev-parse", "HEAD")
        commit_files(r, {"src/lib/late.py": "added after the start commit\n"}, "later")
        return r, start

    def fill_c2(self, r, start, task):
        t = self.write("task-%d.txt" % len(os.listdir(self.tmp)), task)
        return self.decide("change.py", "fill-c2", "--repo", r, "--commit", start, "--task-file", t)

    def items(self, out):
        return [x.strip() for x in out["fill"].split(",") if x.strip()]

    def test_c2_list_order_and_content(self):
        r, start = self.c2_repo()
        out = self.fill_c2(r, start, "Build Stage 2 of specs/S-009.md. Edit src/lib/ and src/app.py.")
        self.assertTrue(out["eligible"], out)
        items = self.items(out)
        self.assertRegex(items[0], r"^specs/S-009\.md:\d+-\d+$", "first item is the spec with the stage's line range")
        lo, hi = map(int, items[0].split(":")[1].split("-"))
        self.assertTrue(lo <= 7 <= hi, "range must cover the Stage 2 heading (line 7)")
        self.assertLess(hi, 12, "the range stops before the Stage 3 heading (line 12)")
        rest = items[1:]
        self.assertIn("src/lib/a.py", rest)
        self.assertIn("src/lib/b.py", rest)
        self.assertIn("src/app.py", rest)
        self.assertNotIn("src/lib/late.py", rest, "files are read at the start commit only")
        self.assertIn("decisions/questions/P-009-ruling.md", rest)
        self.assertNotIn("decisions/questions/P-010-other.md", rest)
        self.assertIn("tests/acceptance/test_s009.py", rest)
        self.assertIn("checks/s009_check.py", rest)
        self.assertNotIn("tests/acceptance/test_other.py", rest)
        self.assertEqual(len(items), len(set(items)), "each once")
        order = [rest.index(x) for x in ("src/lib/a.py", "decisions/questions/P-009-ruling.md",
                                          "tests/acceptance/test_s009.py")]
        self.assertEqual(order, sorted(order), "order: named paths, then rulings, then locked checks")

    def test_c2_task_citing_no_stage_lists_the_whole_spec_without_a_range(self):
        r, start = self.c2_repo()
        out = self.fill_c2(r, start, "Review specs/S-009.md as a whole.")
        self.assertIn("specs/S-009.md", self.items(out))
        self.assertNotRegex(out["fill"], r"specs/S-009\.md:\d")

    def test_c2_list_holding_only_the_spec_is_eligible(self):
        r = self.new_repo()
        start = commit_files(r, {"specs/S-001.md": "# Spec\n"}, "start")
        out = self.fill_c2(r, start, "Do the work of specs/S-001.md.")
        self.assertTrue(out["eligible"])
        self.assertEqual(self.items(out), ["specs/S-001.md"])

    def test_c2_task_naming_no_spec_lists_the_paths_it_names(self):
        r, start = self.c2_repo()
        out = self.fill_c2(r, start, "Tidy src/app.py and src/lib/b.py.")
        self.assertTrue(out["eligible"])
        self.assertEqual(sorted(self.items(out)), ["src/app.py", "src/lib/b.py"])

    def test_c2_empty_list_is_not_eligible(self):
        r, start = self.c2_repo()
        out = self.fill_c2(r, start, "Do something sensible.")
        self.assertFalse(out["eligible"])
        self.assertTrue(out["reason"])
