"""The Builder's own tests of the E-003 harness (src/E-003/), beyond S-001's locked checks.

Run from the repository root:
    python3 -m unittest discover -s tests/E-003 -p 'test_*.py'
Python standard library only.  Each script is run as the locked checks run it, `python3 -I`.
"""
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SRC = os.path.join(ROOT, "src", "E-003")
ENV = {"GIT_AUTHOR_NAME": "T", "GIT_AUTHOR_EMAIL": "t@t.invalid", "GIT_COMMITTER_NAME": "T",
       "GIT_COMMITTER_EMAIL": "t@t.invalid", "GIT_CONFIG_GLOBAL": os.devnull, "GIT_CONFIG_NOSYSTEM": "1"}


def run(name, *args, stdin=None):
    return subprocess.run([sys.executable, "-I", os.path.join(SRC, name)] + [str(a) for a in args], input=stdin,
                          capture_output=True, text=True, cwd=ROOT, timeout=120)


def git(repo, *args):
    e = dict(os.environ)
    e.update(ENV)
    return subprocess.run(["git", "-C", repo] + list(args), capture_output=True, text=True, env=e,
                          check=True).stdout.strip()


def tool(name, **inp):
    return json.dumps({"type": "assistant", "message": {"content": [{"type": "tool_use", "name": name, "input": inp}]}})


class Tmp(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp(prefix="e003-own-")
        self.addCleanup(shutil.rmtree, self.tmp, True)
        base = None
        for cand in ("/var/tmp", os.path.expanduser("~")):
            if os.path.isdir(cand) and os.access(cand, os.W_OK):
                base = tempfile.mkdtemp(prefix="e003-copy-", dir=cand)
                break
        self.addCleanup(shutil.rmtree, base, True)
        self.cwd = os.path.join(base, "copy")
        os.makedirs(self.cwd)

    def write(self, rel, text):
        p = os.path.join(self.tmp, rel)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "w", encoding="utf-8", newline="") as fh:
            fh.write(text)
        return p

    def tcheck(self, *lines, extra=()):
        t = self.write("t%d.jsonl" % len(os.listdir(self.tmp)), "\n".join(lines) + "\n")
        p = run("transcript_check.py", "check", "--cwd", self.cwd, *extra, t)
        return p.returncode, p.stdout.strip()


class TestTranscriptCheckReadings(Tmp):
    def test_sed_awk_and_grep_scripts_are_not_paths(self):
        self.assertEqual(self.tcheck(tool("Bash", command="sed -n '/^## 12/,/^## 13/p' a.md; awk '/^x/,/^y/' a.md"),
                                     tool("Bash", command="for f in a b; do sed -i -E '/^import x$/d' $f.py; done")),
                         (0, "clean"))

    def test_a_file_named_after_a_sed_script_is_still_checked(self):
        self.assertEqual(self.tcheck(tool("Bash", command="sed -n '1p' /home/user/x.md")), (1, "leak@1"))

    def test_cd_is_followed_within_a_command(self):
        self.assertEqual(self.tcheck(tool("Bash", command="cd sub && cat ../a.txt")), (0, "clean"))
        self.assertEqual(self.tcheck(tool("Bash", command="cd sub && cat ../../a.txt")), (1, "leak@1"))

    def test_dev_null_is_a_redirection_target_and_etc_is_read_only(self):
        self.assertEqual(self.tcheck(tool("Bash", command="ls x 2>/dev/null; cat /etc/hosts")), (0, "clean"))
        self.assertEqual(self.tcheck(tool("Write", file_path="/etc/x", content="y")), (1, "leak@1"))
        self.assertEqual(self.tcheck(tool("Bash", command="echo x > /etc/x")), (1, "leak@1"))

    def test_a_folder_made_by_mkdir_holds_created_paths(self):
        self.assertEqual(self.tcheck(tool("Bash", command="mkdir -p /tmp/e003-own-dir"),
                                     tool("Read", file_path="/tmp/e003-own-dir/f.txt")), (0, "clean"))
        self.assertEqual(self.tcheck(tool("Read", file_path="/tmp/e003-own-dir2/f.txt"),
                                     tool("Bash", command="mkdir /tmp/e003-own-dir2")), (1, "leak@1"))

    def test_touch_creates_and_a_read_on_the_same_line_is_clean(self):
        self.assertEqual(self.tcheck(tool("Bash", command="touch /tmp/e003-t.txt && cat /tmp/e003-t.txt")),
                         (0, "clean"))

    def test_unknown_tools_and_helpers_leak_and_the_handback_does_not(self):
        self.assertEqual(self.tcheck(tool("Agent", prompt="x")), (1, "leak@1"))
        self.assertEqual(self.tcheck(tool("mcp__github__get_me")), (1, "leak@1"))
        self.assertEqual(self.tcheck(tool("TodoWrite", todos=[]), tool("SubagentHandback", message="m")), (0, "clean"))

    def test_a_url_in_text_a_script_writes_is_data_but_a_fetch_is_not(self):
        self.assertEqual(self.tcheck(tool("Bash", command="python3 - <<'EOF'\nprint('see https://x.example/a')\nEOF")),
                         (0, "clean"))
        self.assertEqual(self.tcheck(tool("Bash", command="python3 -c \"import urllib.request as u; "
                                                           "u.urlopen('https://x.example/a')\"")), (1, "leak@1"))
        self.assertEqual(self.tcheck(tool("Bash", command="pip install requests")), (1, "leak@1"))

    def test_a_working_directory_outside_the_copy_leaks(self):
        line = json.dumps({"type": "user", "cwd": "/home/user/Model-Lab", "message": {"content": "x"}})
        self.assertEqual(self.tcheck(line), (1, "leak@1"))

    def test_a_missing_transcript_fails_by_rule(self):
        p = run("transcript_check.py", "check", "--cwd", self.cwd, os.path.join(self.tmp, "none.jsonl"))
        self.assertEqual((p.returncode, p.stdout.strip()), (1, "missing"))


class TestRefusalsCarryNoText(Tmp):
    def test_block_refusal_does_not_echo_a_refused_line(self):
        p = run("block.py", "parse", stdin="set: S-001-built-1\n1. SECRET-WORDS of a test\n")
        self.assertEqual(p.returncode, 1)
        self.assertNotIn("SECRET-WORDS", p.stdout + p.stderr)

    def test_verdict_refusal_does_not_echo_a_refused_line(self):
        idx = self.write("INDEX", "L1\tbuilt\tL1.bundle\t%s\t%s\nlast\n" % ("a" * 64, "b" * 64))
        os.makedirs(os.path.join(self.tmp, "files"))
        self.write("files/L1.files", "a.py\n")
        v = self.write("v.tsv", "SECRET-WORDS here\n")
        p = run("verdicts.py", "check", "--index", idx, "--filelists", os.path.join(self.tmp, "files"), "--tests", "3",
                "--set", "S-001-built-1", "--verdicts", v)
        self.assertEqual(p.returncode, 1)
        self.assertNotIn("SECRET-WORDS", p.stdout + p.stderr)


class TestFillBrief(Tmp):
    def fill(self, kind, extra):
        values = {"label": "R1", "kind": kind, "checker_role": "source-checker",
                  "role_file": ".claude/agents/source-checker.md", "review": "source check", "judged": "research/Q-9-memo.md"}
        values.update(extra)
        f = self.write("R1.fill.json", json.dumps(values))
        sheet = self.write("sheet.md", "1. A test.\n")
        import hashlib
        fp = hashlib.sha256(open(sheet, "rb").read()).hexdigest()
        out = os.path.join(self.tmp, "brief.txt")
        p = run("fill_judge_brief.py", "--sheet", sheet, "--fingerprint", fp, "--fill", f, "--label", "R1",
                "--copy-path", "/c", "--out", out)
        self.assertEqual(p.returncode, 0, p.stdout + p.stderr)
        return " ".join(open(out, encoding="utf-8").read().split())

    def test_research_may_open_only_the_memos_sources(self):
        text = self.fill("research", {"task_statement_path": "research/Q-9.md"})
        self.assertIn("use the web only to open the sources the memo cites", text)
        self.assertNotIn("do not use the web", text)
        self.assertIn("The work to judge: research/Q-9-memo.md.", text)
        self.assertIn("against: research/Q-9.md.", text)

    def test_plans_keep_the_bar_on_the_web(self):
        text = self.fill("plans", {"judged": "start..R1", "task_statement_text": "Write the plan."})
        self.assertIn("do not use the web, and do not run git commands", text)
        self.assertIn("the commit range start..R1 in the copy", text)

    def test_a_label_that_is_not_the_fill_files_is_refused(self):
        f = self.write("x.fill.json", json.dumps({"label": "OTHER"}))
        sheet = self.write("s.md", "x\n")
        import hashlib
        fp = hashlib.sha256(b"x\n").hexdigest()
        p = run("fill_judge_brief.py", "--sheet", sheet, "--fingerprint", fp, "--fill", f, "--label", "R1",
                "--copy-path", "/c", "--out", os.path.join(self.tmp, "o.txt"))
        self.assertEqual(p.returncode, 1)
        self.assertFalse(os.path.exists(os.path.join(self.tmp, "o.txt")))


class TestExport(Tmp):
    def test_a_label_twice_and_after_last_is_refused(self):
        r = os.path.join(self.tmp, "r")
        os.makedirs(r)
        git(r, "init", "-q")
        git(r, "commit", "-q", "--allow-empty", "-m", "s")
        s = git(r, "rev-parse", "HEAD")
        out = os.path.join(self.tmp, "out")
        args = ["make", "--kind", "built", "--repo", r, "--out", out, "--checker-role", "reviewer",
                "--role-file", ".claude/agents/reviewer.md", "--start", s, "--final", s]
        self.assertEqual(run("export.py", *args, "--label", "A1").returncode, 0)
        self.assertEqual(run("export.py", *args, "--label", "A1").returncode, 1)
        self.assertEqual(run("export.py", *args, "--label", "start").returncode, 1)
        self.assertEqual(run("export.py", "finish", "--out", out, "--kind", "built").returncode, 0)
        self.assertEqual(run("export.py", "finish", "--out", out, "--kind", "built").returncode, 1)
        self.assertEqual(run("export.py", *args, "--label", "A2").returncode, 1)
        self.assertEqual(run("export.py", "verify", "--out", out, "--kind", "built").returncode, 0)


class TestPlanPrompt(Tmp):
    def test_each_arm_gets_e001s_confinement_with_its_own_copy_path(self):
        r = os.path.join(self.tmp, "real")
        os.makedirs(r)
        git(r, "init", "-q")
        os.makedirs(os.path.join(r, "specs"))
        with open(os.path.join(r, "specs", "S-1.md"), "w") as fh:
            fh.write("# S\n")
        git(r, "add", "-A")
        git(r, "commit", "-q", "-m", "s")
        s = git(r, "rev-parse", "HEAD")
        entry = self.write("e.json", json.dumps({
            "brief": "Intro.\n\nTask: build specs/S-1.md in %s.\n\nReturn.\n" % r, "start": s, "repo": "Model-Lab",
            "kind": "built", "model": "m", "dispatched_at": "2026-11-05T09:00:00Z", "real_path": r}))
        p = run("pair.py", "plan", "--entry", entry, "--repos-root", self.tmp, "--change", "C2",
                "--now", "2026-11-05T10:00:00Z", "--no-run")
        self.assertEqual(p.returncode, 0, p.stdout + p.stderr)
        arms = {a["arm"]: a for a in json.loads(p.stdout)["arms"]}
        for a in arms.values():
            self.assertTrue(a["prompt"].startswith(a["brief"].rstrip("\n")))
            self.assertIn("Work only in %s. Do not read" % a["copy"], a["prompt"])
            self.assertNotIn(r, a["prompt"])
        self.assertIn("The inputs for this task, by path: specs/S-1.md. Read these first.", arms["change"]["brief"])

    def test_the_wrong_change_for_the_kind_is_refused(self):
        entry = self.write("e.json", json.dumps({"brief": "x", "start": "a" * 40, "repo": "Model-Lab", "kind": "plans",
                                                 "model": "m", "dispatched_at": "2026-11-05T09:00:00Z"}))
        p = run("pair.py", "plan", "--entry", entry, "--repos-root", self.tmp, "--change", "C2",
                "--now", "2026-11-05T10:00:00Z", "--no-run")
        self.assertEqual(p.returncode, 1)


class TestAnalyseIsAReference(unittest.TestCase):
    def test_the_help_says_it_is_not_the_reviewers_analysis(self):
        p = run("analyse.py", "--help")
        self.assertEqual(p.returncode, 0)
        flat = " ".join(p.stdout.split())
        self.assertIn("THIS IS NOT THE ANALYSIS", flat)
        self.assertIn("not the Reviewer's result", flat)


if __name__ == "__main__":
    unittest.main()
