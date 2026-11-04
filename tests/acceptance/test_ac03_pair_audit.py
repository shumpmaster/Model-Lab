"""AC3 [trace: V1 -> AC3] -- when a piece's named inputs change between its start commit and its real
round-1 submission, or an arm leaks, or the arms' starting contexts differ beyond the change text, then
the pair is not judged as it stands: it is left out or rerun as E-003 says, listed with its reason, and
never run again for a better answer.

E-003 Exclusions 1-3 and Sample "Reruns (b)": in-flight inputs and leaks leave the pair out; a set-up
fault (including a context that differs) is rerun once, both arms; a second fault leaves it out.

Interfaces named (e003_support.py): src/E-003/pair.py audit | context-compare | rerun-decision, and
src/E-003/transcript_check.py check (tested fully in test_j3/ac05; here its use on an arm).
GAPS: the spec says "decided mechanically from git" but not how "before the real work's round-1
submission" is cut; the test cuts it at the submission commit's committer date.  FAILS until built.
"""
import json
import os

from e003_support import (Base, commit_files, git, text_line, tool_line, write_transcript)

START_T, MAIN1_T, SUB_T, MAIN2_T = ("2026-11-01T10:00:00Z", "2026-11-02T10:00:00Z", "2026-11-03T10:00:00Z",
                                    "2026-11-04T10:00:00Z")


class TestAC3Audit(Base):
    def fixture(self, main_edits, merge_main=False):
        """main: start, then each (when, files) of main_edits; work branch from start with its own commit."""
        r = self.new_repo()
        start = commit_files(r, {"specs/S-100.md": "spec\n", "src/x.py": "x\n", "other.txt": "o\n"}, "start",
                             when=START_T)
        main_commits = []
        for when, files in main_edits:
            main_commits.append(commit_files(r, files, "main edit", when=when))
        git(r, "checkout", "-q", "-b", "work", start)
        sub = commit_files(r, {"src/x.py": "x work\n"}, "round 1", when=SUB_T)
        if merge_main:
            git(r, "merge", "-q", "--no-ff", "-m", "takes in main", main_commits[0],
                env={"GIT_AUTHOR_DATE": SUB_T, "GIT_COMMITTER_DATE": SUB_T})
            sub = git(r, "rev-parse", "HEAD")
        git(r, "checkout", "-q", "main")
        return r, start, sub

    def audit(self, r, start, sub, *named):
        args = ["audit", "--repo", r, "--start", start, "--submission", sub, "--default-branch", "main"]
        for n in named:
            args += ["--named-input", n]
        return self.decide("pair.py", *args)

    def test_unrelated_default_branch_change_leaves_the_pair_in(self):
        r, s, sub = self.fixture([(MAIN1_T, {"other.txt": "changed\n"})])
        out = self.audit(r, s, sub, "specs/S-100.md")
        self.assertTrue(out["include"], out)

    def test_named_input_changed_before_the_submission_leaves_the_pair_out_with_a_reason(self):
        r, s, sub = self.fixture([(MAIN1_T, {"specs/S-100.md": "spec changed\n"})])
        out = self.audit(r, s, sub, "specs/S-100.md")
        self.assertFalse(out["include"])
        self.assertIn("specs/S-100.md", out["reason"])

    def test_named_input_changed_only_after_the_submission_does_not_count(self):
        r, s, sub = self.fixture([(MAIN2_T, {"specs/S-100.md": "spec changed late\n"})])
        self.assertTrue(self.audit(r, s, sub, "specs/S-100.md")["include"])

    def test_branch_that_takes_in_a_foreign_commit_leaves_the_pair_out(self):
        r, s, sub = self.fixture([(MAIN1_T, {"other.txt": "changed\n"})], merge_main=True)
        out = self.audit(r, s, sub, "specs/S-100.md")
        self.assertFalse(out["include"])
        self.assertTrue(out["reason"])

    def test_a_directory_named_input_counts_its_files(self):
        r, s, sub = self.fixture([(MAIN1_T, {"src/y.py": "new file in a named directory\n"})])
        self.assertFalse(self.audit(r, s, sub, "src/")["include"])


def start_lines(path, change=None):
    brief = "You are the builder in %s.\n\nTASK: do it.\n" % path
    if change:
        brief += "\n" + change + "\n"
    return [json.dumps({"type": "system", "subtype": "init", "cwd": path, "model": "claude-opus-5-5"}),
            json.dumps({"type": "user", "message": {"role": "user", "content": brief}})]


class TestAC3Context(Base):
    def compare(self, a_lines, b_lines, pa="/tmp/copyA", pb="/tmp/copyB"):
        a = write_transcript(self.tmp, "a.jsonl", a_lines)
        b = write_transcript(self.tmp, "b.jsonl", b_lines)
        ct = self.write("change.txt", "THE CHANGE PARAGRAPH")
        return self.decide("pair.py", "context-compare", "--a", a, "--b", b, "--change-text", ct,
                           "--path-a", pa, "--path-b", pb)

    def test_contexts_that_differ_only_by_the_change_and_the_path_match(self):
        out = self.compare(start_lines("/tmp/copyA"), start_lines("/tmp/copyB", "THE CHANGE PARAGRAPH"))
        self.assertTrue(out["same"], out)

    def test_an_extra_context_line_is_a_difference(self):
        extra = start_lines("/tmp/copyB", "THE CHANGE PARAGRAPH") + []
        extra.insert(1, text_line("attribution: Co-authored by someone", role="system"))
        out = self.compare(start_lines("/tmp/copyA"), extra)
        self.assertFalse(out["same"])
        self.assertTrue(out["reason"])

    def test_a_different_model_is_a_difference(self):
        b = start_lines("/tmp/copyB", "THE CHANGE PARAGRAPH")
        b[0] = b[0].replace("claude-opus-5-5", "claude-sonnet-5-5")
        self.assertFalse(self.compare(start_lines("/tmp/copyA"), b)["same"])

    def test_a_second_changed_sentence_is_a_difference(self):
        b = start_lines("/tmp/copyB", "THE CHANGE PARAGRAPH")
        b[1] = b[1].replace("TASK: do it.", "TASK: do it twice.")
        self.assertFalse(self.compare(start_lines("/tmp/copyA"), b)["same"])


class TestAC3Reruns(Base):
    def decision(self, *events):
        h = self.write("h%d.json" % len(os.listdir(self.tmp)), json.dumps([{"event": e} for e in events]))
        return self.decide("pair.py", "rerun-decision", "--history", h)

    def test_a_first_set_up_fault_is_rerun_once(self):
        self.assertEqual(self.decision("set-up-fault")["action"], "rerun")

    def test_a_context_difference_is_a_set_up_fault_and_is_rerun_once(self):
        self.assertEqual(self.decision("context-differs")["action"], "rerun")

    def test_a_second_set_up_fault_leaves_the_pair_out_with_a_reason(self):
        out = self.decision("set-up-fault", "set-up-fault")
        self.assertEqual(out["action"], "leave-out")
        self.assertTrue(out["reason"])
        self.assertEqual(self.decision("set-up-fault", "context-differs")["action"], "leave-out")

    def test_in_flight_inputs_and_leaks_are_never_rerun(self):
        for ev in ("in-flight-inputs", "leak"):
            out = self.decision(ev)
            self.assertEqual(out["action"], "leave-out", ev)
            self.assertTrue(out["reason"], ev)

    def test_a_completed_pair_is_never_rerun_for_a_better_answer(self):
        self.assertNotEqual(self.decision("completed")["action"], "rerun")
        self.assertNotEqual(self.decision("completed", "set-up-fault")["action"], "rerun")


class TestAC3ArmLeak(Base):
    def check(self, lines, *extra):
        cwd = os.path.join(self.tmp, "copy")
        os.makedirs(cwd, exist_ok=True)
        t = write_transcript(self.tmp, "arm.jsonl", lines)
        return self.run_script("transcript_check.py", "check", "--cwd", cwd, *extra, t), cwd

    def test_an_arm_that_reads_outside_its_copy_leaks(self):
        cwd = os.path.join(self.tmp, "copy")
        p, _ = self.check([text_line("start"), tool_line("Read", file_path="/home/user/Service-Desk/CLAUDE.md")])
        self.assertEqual(p.returncode, 1)
        self.assertEqual(p.stdout.strip(), "leak@2")

    def test_an_arm_calling_the_sheets_repository_leaks(self):
        p, cwd = self.check([tool_line("Bash", command="git ls-remote https://github.com/someone/secret-marking")],
                            "--sheets-repo", "secret-marking")
        self.assertEqual(p.returncode, 1)
        self.assertEqual(p.stdout.strip(), "leak@1")

    def test_an_arm_that_stays_in_its_copy_is_clean(self):
        cwd = os.path.join(self.tmp, "copy")
        p, _ = self.check([tool_line("Read", file_path=cwd + "/src/x.py"), tool_line("Bash", command="ls"),
                           tool_line("Grep", pattern="x", path=cwd)])
        self.assertEqual((p.returncode, p.stdout.strip()), (0, "clean"))
