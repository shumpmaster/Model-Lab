"""AC5 [trace: V1 -> AC5] -- when a plan or built arm finishes, its deliverable's neutral export is judged
in its own judge session, and when both research checks have returned, the memo's export is judged once in
its own session; each judge runs on a model other than the doers', without the arm's label, hand-back,
commit messages or the check versions' verdicts, and gets its sheet only after the sheet's SHA-256 matches
the recorded fingerprint; for built work the stage's locked checks also run by script; a judge with no
verdict line gets the one fixed follow-up and at most one new session, and a judge whose transcript shows
a read outside its copy, or the web beyond the memo's sources, leaves its pair out; each pair left out is
listed.

Interfaces named (e003_support.py): judge.py next-step | parse-return | followup-text | arm-outcome |
check-model; transcript_check.py check; pair.py locked-checks; fill_judge_brief.py (tested for the
fingerprint gate in test_j4_sheet_route.py).  GAPS: the spec does not say how the locked checks are
invoked for a project, so the command is passed in; and whether the new judge session also gets the
follow-up is not said ("the one fixed follow-up" is read as one in all).
FAILS until the Builder builds src/E-003/judge.py, transcript_check.py and pair.py.
"""
import json
import os

from e003_support import (Base, STAND_IN_MARKERS, STAND_IN_SHEET, commit_files, git, sha256, text_line, tool_line,
                          write_transcript)

FOLLOWUP = "Return your verdict now. First line: `Verdict: PASS` or `Verdict: FAIL`."


class TestAC5Verdicts(Base):
    def step(self, **state):
        base = {"verdict": None, "follow_up_sent": False, "sessions": 1}
        base.update(state)
        return self.decide("judge.py", "next-step", "--state", json.dumps(base))["action"]

    def test_no_verdict_gets_the_one_fixed_follow_up(self):
        self.assertEqual(self.step(), "follow-up")
        p = self.run_script("judge.py", "followup-text")
        self.assertEqual(p.stdout.strip(), FOLLOWUP)

    def test_still_no_verdict_after_the_follow_up_gets_one_new_session(self):
        self.assertEqual(self.step(follow_up_sent=True), "new-session")

    def test_never_a_third_session_and_then_the_pair_is_left_out(self):
        for fu in (False, True):
            self.assertNotEqual(self.step(follow_up_sent=fu, sessions=2), "new-session")
        self.assertEqual(self.step(follow_up_sent=True, sessions=2), "leave-out")

    def test_a_verdict_ends_it(self):
        self.assertEqual(self.step(verdict="PASS"), "done")
        self.assertEqual(self.step(verdict="FAIL", follow_up_sent=True), "done")

    def parse(self, text, *extra):
        f = self.write("ret-%d.txt" % len(os.listdir(self.tmp)), text)
        return self.decide("judge.py", "parse-return", "--text-file", f, *extra)

    def test_first_line_forms(self):
        self.assertEqual(self.parse("Verdict: PASS\n")["verdict"], "PASS")
        self.assertEqual(self.parse("Verdict: FAIL\n2 src/a.py:3\n")["verdict"], "FAIL")
        for text in ("Here is my analysis.\nVerdict: PASS\n", "verdict: pass\n", "Verdict: MAYBE\n", "", "PASS\n",
                     "Verdict:PASS\n"):
            self.assertEqual(self.parse(text)["verdict"], "none", repr(text))

    def test_two_verdict_lines_the_first_counts_and_it_is_reported(self):
        out = self.parse("Verdict: FAIL\n1 src/a.py:2\nVerdict: PASS\n")
        self.assertEqual(out["verdict"], "FAIL")
        self.assertTrue(out["multiple"])
        self.assertFalse(self.parse("Verdict: FAIL\n")["multiple"])

    def test_background_tasks_still_running_means_no_verdict(self):
        self.assertEqual(self.parse("Verdict: PASS\n", "--background-running")["verdict"], "none")

    def test_failed_tests_with_and_without_file_line(self):
        out = self.parse("Verdict: FAIL\n2 src/a.py:3\n3\n")
        self.assertEqual(out["failed"], ["2@src/a.py:3", "3@-"])


class TestAC5Outcome(Base):
    def outcome(self, *args):
        return self.decide("judge.py", "arm-outcome", *args)

    def test_built_work_passes_only_if_the_judge_passes_and_the_locked_checks_pass(self):
        self.assertTrue(self.outcome("--verdict", "PASS", "--locked-exit", "0")["pass"])
        self.assertFalse(self.outcome("--verdict", "PASS", "--locked-exit", "1")["pass"])
        self.assertFalse(self.outcome("--verdict", "FAIL", "--locked-exit", "0")["pass"])
        self.assertFalse(self.outcome("--verdict", "FAIL", "--locked-exit", "2")["pass"])

    def test_plans_have_no_locked_checks(self):
        self.assertTrue(self.outcome("--verdict", "PASS")["pass"])
        self.assertFalse(self.outcome("--verdict", "FAIL")["pass"])

    def test_no_verdict_is_neither_pass_nor_fail(self):
        self.assertIsNone(self.outcome("--verdict", "none")["pass"])

    def test_the_judge_runs_on_a_model_other_than_the_doers(self):
        ok = self.decide("judge.py", "check-model", "--doer", "claude-opus-5-5", "--judge", "claude-fable-5-1")
        self.assertTrue(ok["ok"])
        same = self.decide("judge.py", "check-model", "--doer", "claude-opus-5-5", "--judge", "claude-opus-5-5")
        self.assertFalse(same["ok"])

    def test_locked_checks_run_by_script_and_their_exit_status_is_recorded(self):
        for body, want in (("import unittest\nclass T(unittest.TestCase):\n def test_a(self): pass\n", 0),
                           ("import unittest\nclass T(unittest.TestCase):\n def test_a(self): self.fail('x')\n", 1)):
            copy = self.new_repo("copy%d" % want)
            commit_files(copy, {"tests/acceptance/test_x.py": body}, "c")
            out = self.decide("pair.py", "locked-checks", "--copy", copy, "--command",
                              "python3 -m unittest discover -s tests/acceptance")
            self.assertEqual(out["exit"], want)


class TestAC5Brief(Base):
    """The judge's brief carries neither the arm's label, hand-back, commit messages nor a verdict."""

    def test_the_filled_brief_holds_none_of_them(self):
        src = self.new_repo("src")
        start = commit_files(src, {"a.txt": "a\n"}, "start", when="2026-11-01T10:00:00Z")
        final = commit_files(src, {"b.txt": "b\n"}, "HANDBACK-AND-CHANGE-NAMED commit message",
                             when="2026-11-02T10:00:00Z")
        out = os.path.join(self.tmp, "ex")
        os.makedirs(out)
        p = self.run_script("export.py", "make", "--kind", "plans", "--repo", src, "--start", start, "--final", final,
                            "--label", "L5", "--out", out, "--checker-role", "critic",
                            "--role-file", ".claude/agents/critic.md", "--task-statement-text", "Write a plan.")
        self.assertEqual(p.returncode, 0, p.stderr[-300:])
        fill = [os.path.join(d, f) for d, _, fs in os.walk(out) for f in fs if f == "L5.fill.json"][0]
        sheet = self.write("s/holdouts/S-001-plans-1.md", STAND_IN_SHEET)
        outp = os.path.join(self.tmp, "w", "brief.txt")
        os.makedirs(os.path.dirname(outp))
        q = self.run_script("fill_judge_brief.py", "--sheet", sheet, "--fingerprint", sha256(STAND_IN_SHEET),
                            "--fill", fill, "--label", "L5", "--copy-path", os.path.join(self.tmp, "copy"), "--out", outp)
        self.assertEqual(q.returncode, 0, q.stderr[-300:])
        text = open(outp, encoding="utf-8").read()
        for bad in ("HANDBACK-AND-CHANGE-NAMED", start, final, "no-change", "hand-back of"):
            self.assertNotIn(bad, text)


class TestTranscriptCheck(Base):
    """Used on arms (AC3), on the blind Check author (AC4) and on judges (here)."""

    def setUp(self):
        super().setUp()
        self.cwd = os.path.join(self.tmp, "copy")
        os.makedirs(self.cwd)

    def check(self, lines, *extra):
        t = write_transcript(self.tmp, "t%d.jsonl" % len(os.listdir(self.tmp)), lines)
        return self.run_script("transcript_check.py", "check", "--cwd", self.cwd, *extra, t)

    def clean(self, lines, *extra):
        p = self.check(lines, *extra)
        self.assertEqual((p.returncode, p.stdout.strip()), (0, "clean"), p.stdout + p.stderr[-200:])

    def leak(self, lines, at, *extra):
        p = self.check(lines, *extra)
        self.assertEqual((p.returncode, p.stdout.strip()), (1, "leak@%d" % at), p.stdout + p.stderr[-200:])

    def test_reads_inside_the_copy_are_clean(self):
        self.clean([text_line("hello"), tool_line("Read", file_path=self.cwd + "/a.txt"),
                    tool_line("Read", file_path="sub/b.txt"), tool_line("Grep", pattern="x"),
                    tool_line("Glob", pattern="**/*.py"), tool_line("Bash", command="ls -la && git log --oneline")])

    def test_a_read_search_or_command_outside_the_copy_is_a_leak_at_its_line(self):
        self.leak([text_line("a"), tool_line("Read", file_path="/etc/hostname")], 2)
        self.leak([tool_line("Grep", pattern="x", path="/home/user")], 1)
        self.leak([text_line("a"), text_line("b"), tool_line("Glob", pattern="*.md", path="/tmp/other")], 3)
        self.leak([tool_line("Bash", command="cat /root/.bashrc")], 1)
        self.leak([tool_line("Bash", command="cd /tmp && ls")], 1)

    def test_parent_directory_escape_and_sibling_prefix_are_leaks(self):
        self.leak([tool_line("Read", file_path="../secret.txt")], 1)
        self.leak([tool_line("Read", file_path=self.cwd + "/../other/x")], 1)
        self.leak([tool_line("Read", file_path=self.cwd + "-evil/x")], 1)

    def test_the_first_of_two_leaks_is_reported(self):
        self.leak([tool_line("Read", file_path="/etc/a"), tool_line("Read", file_path="/etc/b")], 1)

    def test_web_use_is_a_leak_unless_allowed(self):
        self.leak([tool_line("WebFetch", url="https://example.com/x", prompt="p")], 1)
        self.leak([tool_line("WebSearch", query="q")], 1)
        self.leak([tool_line("Bash", command="curl -s https://example.com")], 1)
        self.leak([tool_line("Bash", command="git fetch https://github.com/x/y")], 1)

    def test_the_research_judge_may_open_only_the_memos_sources(self):
        src = self.write("sources.txt", "https://example.org/paper\nhttps://example.net/data\n")
        self.clean([tool_line("WebFetch", url="https://example.org/paper", prompt="p")], "--web-sources", src)
        self.leak([tool_line("WebFetch", url="https://elsewhere.example/page", prompt="p")], 1, "--web-sources", src)
        self.leak([tool_line("WebSearch", query="more")], 1, "--web-sources", src)
        self.leak([tool_line("Read", file_path="/etc/hosts")], 1, "--web-sources", src)

    def test_a_file_the_harness_saved_of_the_runs_own_output_may_be_read_at_its_named_path(self):
        saved = os.path.join(self.tmp, "saved-output.txt")
        self.clean([tool_line("Read", file_path=saved)], "--allow-path", saved)
        self.leak([tool_line("Read", file_path=saved + ".other")], 1, "--allow-path", saved)

    def test_a_call_naming_the_sheets_repository_is_a_leak(self):
        self.leak([tool_line("Bash", command="git ls-remote https://github.com/owner/secret-marking")], 1,
                  "--sheets-repo", "secret-marking")
        self.leak([tool_line("mcp__github__get_file_contents", owner="owner", repo="secret-marking", path="README.md")],
                  1, "--sheets-repo", "secret-marking")

    def test_the_blind_check_authors_pack_folder_is_its_only_working_directory(self):
        self.clean([tool_line("Read", file_path=self.cwd + "/experiments/E-003/check-author-extract.md"),
                    tool_line("Read", file_path=self.cwd + "/BRIEF.md")])
        self.leak([tool_line("Read", file_path="/home/user/Model-Lab/specs/S-001.md")], 1)
        self.leak([tool_line("Bash", command="grep -r Verdict /home/user/Model-Lab")], 1)
