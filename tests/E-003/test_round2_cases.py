"""Case tables for build round 2 (reviews/S-001/_reviewer-build.md, round 1, findings 1 to 4 and 6).

Every row runs.  Run from the repository root:
    python3 -m unittest discover -s tests/E-003 -p 'test_*.py'

Where the strict reading of E-001's F4 leaves a row open, the row's expected result is the one that reads as
a leak, and its note says "chosen".  `{C}` is the copy (--cwd), outside /tmp; each row is its own transcript,
one Bash call per line.
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
CLEAN, LEAK1, LEAK2 = "clean", "leak@1", "leak@2"

# ---------------------------------------------------------------------------------------------
# Finding 1: paths inside quoted arguments of wrapper commands and inline code.
# (row id, [commands, one transcript line each], expected, note)
FINDING_1 = [
    # shell wrappers: the quoted script is checked as a command of its own
    ("W1", ['bash -c "cat {C}/a.txt"'], CLEAN, "inside the copy"),
    ("W2", ['bash -c "cat /home/user/Model-Lab/specs/S-001.md"'], LEAK1, "outside"),
    ("W3", ["sh -c 'cat /home/user/Model-Lab/specs/S-001.md'"], LEAK1, "single-quoted"),
    ("W4", ['bash -lc "cat /home/user/x"'], LEAK1, "combined flags ending in c"),
    ("W5", ['zsh -c "ls ../../x"'], LEAK1, "relative path leaving the copy"),
    ("W6", ["bash -c 'echo x > /tmp/e003-w1.txt && cat /tmp/e003-w1.txt'"], CLEAN, "/tmp created inside, same line"),
    ("W7", ["bash -c 'cat /tmp/e003-w2.txt'"], LEAK1, "/tmp never created"),
    ("W8", ["bash -c 'cat /tmp/e003-w3.txt'", "echo x > /tmp/e003-w3.txt"], LEAK1, "/tmp read before creation"),
    ("W9", ["echo x > /tmp/e003-w4.txt", 'bash -c "cat /tmp/e003-w4.txt"'], CLEAN, "/tmp read after creation"),
    ("W10", ["cat /tmp/e003-w5.txt; bash -c 'echo x > /tmp/e003-w5.txt'"], CLEAN,
     "created inside a wrapper on the same line"),
    ("W11", ['eval "cat /root/.claude/settings.json"'], LEAK1, "eval"),
    ("W12", ['eval "ls {C}"'], CLEAN, "eval inside the copy"),
    ("W13", ['sudo sh -c "cat /etc/hosts"'], CLEAN, "a system path read by a shell command (F4 allows it)"),
    ("W14", ["find . -name '*.py' -exec sh -c 'cat \"$1\"' _ {} \\;"], CLEAN, "positional argument only"),
    ("W15", ["bash -c \"bash -c 'cat /home/user/x'\""], LEAK1, "nested wrappers"),
    ("W16", ['bash -c "curl https://example.com"'], LEAK1, "network inside a wrapper"),
    # inline code: python -c, heredocs, node -e, perl -e, ruby -e, awk programs
    ("I1", ["python3 -c \"print(open('{C}/a.txt').read())\""], CLEAN, "inside the copy"),
    ("I2", ["python3 -c \"print(open('/home/user/Model-Lab/specs/S-001.md').read())\""], LEAK1, "outside"),
    ("I3", ["python3 -c 'print(open(\"/home/user/x\").read())'"], LEAK1, "inner double quotes"),
    ("I4", ["python3 -c \"import os; os.chdir('/home/user'); print(os.listdir('.'))\""], LEAK1, "chdir outside"),
    ("I5", ["python3 -c \"open('../../x').read()\""], LEAK1, "relative path leaving the copy"),
    ("I6", ["python3 -c \"open('sub/a.txt').read()\""], CLEAN, "relative, inside"),
    ("I7", ["python3 -c \"open('/etc/hosts').read()\""], LEAK1,
     "chosen: a system path in inline code may be read or written, which cannot be told"),
    ("I8", ["python3 -c \"open('/tmp/e003-p1.txt', 'w').write('x')\""], LEAK1,
     "chosen: code writing /tmp is not one of the creation forms"),
    ("I9", ["echo x > /tmp/e003-p2.txt", "python3 -c \"print(open('/tmp/e003-p2.txt').read())\""], CLEAN,
     "/tmp created earlier by a redirect, read in code"),
    ("I10", ["python3 - <<'EOF'\nprint(open('/home/user/x').read())\nEOF"], LEAK1, "heredoc"),
    ("I11", ["python3 - <<'EOF'\nimport os\nos.system('cat /home/user/x')\nEOF"], LEAK1, "heredoc, path in a string"),
    ("I12", ["python3 - <<'EOF'\nprint(open('sub/a.txt').read())\nEOF"], CLEAN, "heredoc, inside"),
    ("I12a", ["python3 - <<'EOF'\nold = '''it's \"$HERE/x.py\"'''\nprint(open('/home/user/x').read())\nEOF"], LEAK1,
     "unbalanced shell quotes in the body (shlex falls back to plain words): the heredoc is still code"),
    ("H1", ["cat > {C}/hook.sh <<'EOF'\ncheck=\"$top/governance/check_all.sh\"\nEOF"], CLEAN,
     "a heredoc given to cat is data written into the copy: `$top/` there is text (E-001's real form)"),
    ("H2", ["cat > {C}/hook.sh <<'EOF'\ncat /home/user/x\nEOF"], LEAK1,
     "chosen: an outside path in a heredoc given to cat is read as a path, as Q1"),
    ("H3", ["cat > {C}/hook.sh <<'EOF'\n#!/usr/bin/env bash\nEOF"], CLEAN, "a system path in data"),
    ("H5", ["git commit -q -F - <<'EOF'\nfalls back to refs/remotes/<remote>/HEAD\nEOF"], CLEAN,
     "a `<name>` placeholder makes the path after it relative (E-001's real form)"),
    ("H4", ["bash <<'EOF'\ncat /home/user/x\nEOF"], LEAK1, "a heredoc given to a shell is checked as commands"),
    ("H6", ["bash <<'EOF'\necho x > /tmp/e003-h6.txt\nEOF", "cat /tmp/e003-h6.txt"], CLEAN,
     "/tmp created inside a heredoc given to a shell, read on a later line"),
    ("I12b", ["python3 - <<'EOF'\nold = '''it's \"$HERE/x.py\"'''\nEOF"], CLEAN,
     "as I12a with no outside path: the form of E-001's real transcripts"),
    ("I13", ["node -e \"require('fs').readFileSync('/home/user/x')\""], LEAK1, "node -e"),
    ("I14", ["node -e \"console.log(1 + 1)\""], CLEAN, "no path"),
    ("I15", ["perl -e 'open(F,\"/home/user/Model-Lab/specs/S-001.md\");print <F>'"], LEAK1, "perl -e"),
    ("I16", ["perl -ne 'print if /foo/' a.txt"], LEAK1,
     "chosen: in code a /word/ pattern cannot be told from a path"),
    ("I17", ["ruby -e \"puts File.read('/home/user/x')\""], LEAK1, "ruby -e"),
    ("I18", ["awk '{print}' /home/user/x"], LEAK1, "awk file argument"),
    ("I19", ["awk 'BEGIN{while((getline l < \"/home/user/x\")>0) print l}'"], LEAK1, "awk program reads a file"),
    ("I20", ["awk '/^## 3/,/^## 4/' a.md"], CLEAN, "awk range patterns starting with ^"),
    ("I21", ["python3 -c \"import urllib.request as u; u.urlopen('https://x.example/a')\""], LEAK1, "network in code"),
    ("I22", ["python3 -c \"import socket; socket.create_connection(('x', 80))\""], LEAK1, "socket in code"),
    ("I23", ["python3 - <<'EOF'\ns = 'run \"$HERE/x.py\"'\nEOF"], CLEAN,
     "in Python code `$HERE/` is text (a file being edited), not a variable; E-001's transcripts hold this form"),
    ("I24", ["python3 - <<'EOF'\ns = '$D/../x'\nEOF"], LEAK1, "a `$NAME` path with a .. segment in code still leaks"),
    ("I25", ["perl -e 'open(F, \"$d/x\")'"], LEAK1, "chosen: in perl `$d/` is a variable, which may lie anywhere"),
    # strings that only look like paths, and patterns
    ("Q1", ['echo "/home/user"'], LEAK1, "chosen: a quoted string that looks like a path is read as one"),
    ("Q2", ['echo "see /api/route"'], LEAK1, "chosen: as Q1"),
    ("Q3", ['git commit -m "fix ../x handling"'], LEAK1, "chosen: a .. path in any argument"),
    ("Q4", ['echo "a/b and c.txt"'], CLEAN, "no absolute path and no .."),
    ("Q5", ['grep -n "/home/user" a.txt'], CLEAN, "a grep pattern is never opened"),
    ("Q6", ["sed -n '/^x/p' a.md"], CLEAN, "a sed address"),
    ("Q7", ["sed 'r /home/user/x' a.md"], LEAK1, "sed's r command reads a file"),
    ("Q8", ["sed 'w /tmp/e003-s.txt' a.md"], LEAK1, "chosen: sed's w is not one of the creation forms"),
    ("Q9", ['echo hi > "/tmp/e003-q1.txt" && cat /tmp/e003-q1.txt'], CLEAN, "quoted redirect target"),
    ("Q11", ["find / -name x"], LEAK1, "the root folder, a bare /"),
    ("Q12", ["python3 -c \"print(4 / 2)\""], CLEAN, "in code a lone / is division"),
    ("Q10", ["cat '{C}/sub dir/a.txt'"], CLEAN, "quoted path with a space, inside"),
]

# Finding 2: git naming another repository, $VAR paths with .., network listeners; beside existing forms.
FINDING_2 = [
    ("G1", ["git remote add o https://github.com/o/r.git"], LEAK1, "new: URL in git remote add"),
    ("G2", ["git remote add o ../other"], LEAK1, "new: a repository path outside the copy"),
    ("G3", ["git remote set-url origin git@github.com:o/r.git"], LEAK1, "new: scp-like address"),
    ("G4", ["git remote add o other"], LEAK1, "new, chosen: git remote add names a repository whatever its form"),
    ("G5", ["git config remote.o.url https://x.example/r"], LEAK1, "new: URL in any git subcommand"),
    ("G6", ["git submodule add https://x.example/r"], LEAK1, "existing"),
    ("G7", ["git fetch"], LEAK1, "existing"),
    ("G8", ["git log --oneline"], CLEAN, "existing"),
    ("G9", ["git -C /home/user/x status"], LEAK1, "existing"),
    ("G10", ["git remote -v"], CLEAN, "lists remotes, names none"),
    ("V1", ["cat $PWD/../x"], LEAK1, "new: $PWD is the working directory; .. leaves the copy"),
    ("V2", ["cat ${D}/../x"], LEAK1, "new: an unknown variable with a .. segment"),
    ("V3", ["cat $(pwd)/../x"], LEAK1, "new: $(pwd) as $PWD"),
    ("V4", ["cat $PWD/src/x"], CLEAN, "new: $PWD inside the copy"),
    ("V5", ['cat "$D/x"'], LEAK1, "new, chosen: a path rooted in an unknown variable may be anywhere"),
    ("V6", ["cat $HOME/x"], LEAK1, "existing"),
    ("V7", ["for f in *.py; do cat $f; done"], CLEAN, "a variable with no path part"),
    ("N1", ["python3 -m http.server 8000"], LEAK1, "new: a network listener"),
    ("N2", ["php -S localhost:8000"], LEAK1, "new: a network listener"),
    ("N3", ["socat TCP-LISTEN:8080 -"], LEAK1, "new: a network listener"),
    ("N4", ["nc -l 8080"], LEAK1, "existing (nc)"),
    ("N5", ["curl https://x.example"], LEAK1, "existing"),
    ("N6", ['echo "https://x.example/a"'], CLEAN, "existing: a URL as data, no network tool"),
]

# Finding 3: pair.py audit, E-003 Exclusions 1.  (row id, fixture, expected include, note)
FINDING_3 = [
    ("A1", "unrelated-main-change", True, "AC3: an unnamed file changes on main"),
    ("A2", "named-input-before", False, "AC3: a named input changes on main before the submission"),
    ("A3", "named-input-after", True, "AC3: it changes only after the submission"),
    ("A4", "merge-main", False, "AC3: the work branch takes in a commit of main"),
    ("A5", "named-directory", False, "AC3: a file is added in a named folder"),
    ("A6", "merge-other", False, "review case 5: the work branch merges another branch"),
    ("A7", "linear-own", True, "the work's own commits only"),
    ("A8", "fast-forward-main", False, "the work branch fast-forwards to a main commit, then commits"),
    ("A9", "merge-own-side-branch", False,
     "chosen: a second-parent commit cannot be shown to be the work's own, even from its own side branch"),
    ("A10", "not-descendant", False, "the submission does not descend from the start commit"),
]


def run(name, *args):
    return subprocess.run([sys.executable, "-I", os.path.join(SRC, name)] + [str(a) for a in args],
                          capture_output=True, text=True, cwd=ROOT, timeout=120)


def bash_line(cmd):
    return json.dumps({"type": "assistant", "message": {"content": [
        {"type": "tool_use", "name": "Bash", "input": {"command": cmd}}]}})


class TranscriptTable(unittest.TestCase):
    TABLE = ()

    def setUp(self):
        self.tmp = tempfile.mkdtemp(prefix="e003-r2-")
        self.addCleanup(shutil.rmtree, self.tmp, True)
        base = None
        for cand in ("/var/tmp", os.path.expanduser("~")):
            if os.path.isdir(cand) and os.access(cand, os.W_OK):
                base = tempfile.mkdtemp(prefix="e003-r2-copy-", dir=cand)
                break
        self.addCleanup(shutil.rmtree, base, True)
        self.cwd = os.path.join(base, "copy")
        os.makedirs(self.cwd)

    def check_rows(self):
        for rid, cmds, want, note in self.TABLE:
            with self.subTest(row=rid, note=note):
                t = os.path.join(self.tmp, rid + ".jsonl")
                with open(t, "w", encoding="utf-8") as fh:
                    fh.write("\n".join(bash_line(c.replace("{C}", self.cwd)) for c in cmds) + "\n")
                p = run("transcript_check.py", "check", "--cwd", self.cwd, t)
                self.assertEqual(p.stdout.strip(), want, "%s (%s): %s" % (rid, note, p.stderr.strip()))
                self.assertEqual(p.returncode, 0 if want == CLEAN else 1)


class TestFinding1(TranscriptTable):
    TABLE = FINDING_1

    def test_rows(self):
        self.check_rows()


class TestFinding2(TranscriptTable):
    TABLE = FINDING_2

    def test_rows(self):
        self.check_rows()


class TestFinding3(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp(prefix="e003-r2a-")
        self.addCleanup(shutil.rmtree, self.tmp, True)

    def git(self, repo, *args, when=None):
        e = dict(os.environ)
        e.update(ENV)
        if when:
            e.update({"GIT_AUTHOR_DATE": when, "GIT_COMMITTER_DATE": when})
        return subprocess.run(["git", "-C", repo] + list(args), capture_output=True, text=True, env=e,
                              check=True).stdout.strip()

    def commit(self, repo, files, msg, when):
        for rel, text in files.items():
            p = os.path.join(repo, rel)
            os.makedirs(os.path.dirname(p), exist_ok=True)
            with open(p, "w") as fh:
                fh.write(text)
        self.git(repo, "add", "-A")
        self.git(repo, "commit", "-q", "-m", msg, when=when)
        return self.git(repo, "rev-parse", "HEAD")

    def fixture(self, name):
        T0, T1, T2, T3 = ("2026-11-01T10:00:00Z", "2026-11-02T10:00:00Z", "2026-11-03T10:00:00Z",
                          "2026-11-04T10:00:00Z")
        r = os.path.join(self.tmp, name)
        os.makedirs(r)
        self.git(r, "init", "-q", "-b", "main")
        start = self.commit(r, {"specs/S-100.md": "spec\n", "src/x.py": "x\n", "other.txt": "o\n"}, "start", T0)
        named = ["specs/S-100.md"]
        if name == "unrelated-main-change":
            self.commit(r, {"other.txt": "changed\n"}, "main", T1)
        elif name == "named-input-before":
            self.commit(r, {"specs/S-100.md": "changed\n"}, "main", T1)
        elif name == "named-input-after":
            self.commit(r, {"specs/S-100.md": "changed\n"}, "main", T3)
        elif name == "named-directory":
            self.commit(r, {"src/y.py": "y\n"}, "main", T1)
            named = ["src/"]
        main1 = self.git(r, "rev-parse", "HEAD")
        if name == "merge-other":
            self.git(r, "checkout", "-q", "-b", "other", start)
            self.commit(r, {"src/o.py": "o\n"}, "other", T1)
        if name == "fast-forward-main":
            self.commit(r, {"other.txt": "changed\n"}, "main", T1)
            main1 = self.git(r, "rev-parse", "HEAD")
        self.git(r, "checkout", "-q", "-b", "work", start)
        if name == "fast-forward-main":
            self.git(r, "merge", "-q", "--ff-only", main1)
        if name == "merge-own-side-branch":
            self.git(r, "checkout", "-q", "-b", "side")
            self.commit(r, {"src/side.py": "s\n"}, "side", T1)
            self.git(r, "checkout", "-q", "work")
        sub = self.commit(r, {"src/x.py": "x work\n"}, "round 1", T2)
        if name == "merge-main":
            self.git(r, "checkout", "-q", "main")
            m = self.commit(r, {"other.txt": "changed\n"}, "main", T1)
            self.git(r, "checkout", "-q", "work")
            self.git(r, "merge", "-q", "--no-ff", "-m", "takes in main", m, when=T2)
            sub = self.git(r, "rev-parse", "HEAD")
        if name == "merge-other":
            self.git(r, "merge", "-q", "--no-ff", "-m", "takes in other", "other", when=T2)
            sub = self.git(r, "rev-parse", "HEAD")
        if name == "merge-own-side-branch":
            self.git(r, "merge", "-q", "--no-ff", "-m", "takes in side", "side", when=T2)
            sub = self.git(r, "rev-parse", "HEAD")
        if name == "not-descendant":
            self.git(r, "checkout", "-q", "--orphan", "lone")
            sub = self.commit(r, {"z.txt": "z\n"}, "unrelated", T2)
        self.git(r, "checkout", "-q", "main")
        return r, start, sub, named

    def test_rows(self):
        for rid, name, want, note in FINDING_3:
            with self.subTest(row=rid, note=note):
                r, start, sub, named = self.fixture(name)
                args = ["audit", "--repo", r, "--start", start, "--submission", sub, "--default-branch", "main"]
                for n in named:
                    args += ["--named-input", n]
                p = run("pair.py", *args)
                self.assertEqual(p.returncode, 0, p.stdout + p.stderr)
                out = json.loads(p.stdout)
                self.assertEqual(out["include"], want, "%s (%s): %s" % (rid, note, out))
                if not want:
                    self.assertTrue(out["reason"])


# ---------------------------------------------------------------------------------------------
# Findings 4 and 6.

class TestFinding4(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp(prefix="e003-r2p-")
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.real = os.path.join(self.tmp, "Service-Desk")
        os.makedirs(os.path.join(self.real, "specs"))
        with open(os.path.join(self.real, "specs", "S-100.md"), "w") as fh:
            fh.write("# Spec\n")
        e = dict(os.environ)
        e.update(ENV)
        for args in (["init", "-q"], ["add", "-A"], ["commit", "-q", "-m", "s"]):
            subprocess.run(["git", "-C", self.real] + args, env=e, check=True, capture_output=True)
        self.start = subprocess.run(["git", "-C", self.real, "rev-parse", "HEAD"], capture_output=True,
                                    text=True).stdout.strip()

    def plan(self, brief, real_path=None):
        entry = {"brief": brief, "start": self.start, "repo": "Service-Desk", "kind": "built", "model": "m",
                 "dispatched_at": "2026-11-05T09:00:00Z"}
        if real_path:
            entry["real_path"] = real_path
        f = os.path.join(self.tmp, "e.json")
        with open(f, "w") as fh:
            json.dump(entry, fh)
        return run("pair.py", "plan", "--entry", f, "--repos-root", self.tmp, "--change", "C2",
                   "--now", "2026-11-05T10:00:00Z", "--no-run")

    def test_rows(self):
        rows = [
            ("P1", "Intro.\n\nTask: build specs/S-100.md in /home/user/Service-Desk.\n\nReturn.\n", None, 1,
             "no real_path and an absolute path in the brief: refused"),
            ("P2", "Intro.\n\nTask: build specs/S-100.md.\n\nReturn.\n", None, 0, "no real_path, no absolute path"),
            ("P3", "Intro.\n\nTask: build specs/S-100.md in {R}.\n\nReturn.\n", "{R}", 0, "the real path replaced"),
            ("P4", "Intro.\n\nTask: build specs/S-100.md in {R}, see /home/user/other.\n\nReturn.\n", "{R}", 1,
             "another absolute path left: refused"),
            ("P5", "Intro.\n\nTask: build specs/S-100.md with /usr/bin/python3.\n\nReturn.\n", None, 0,
             "a system path F4 allows"),
            ("P6", "Intro.\n\nTask: build specs/S-100.md, scratch in /tmp/work.\n\nReturn.\n", None, 1,
             "a /tmp path the run did not create: refused"),
        ]
        for rid, brief, real, code, note in rows:
            with self.subTest(row=rid, note=note):
                p = self.plan(brief.replace("{R}", self.real), real and real.replace("{R}", self.real))
                self.assertEqual(p.returncode, code, "%s (%s): %s" % (rid, note, p.stdout + p.stderr))
                if code == 0:
                    for a in json.loads(p.stdout)["arms"]:
                        self.assertNotIn("/home/user", a["brief"])
                        self.assertNotIn(self.real, a["brief"])


class TestFinding6(unittest.TestCase):
    def test_built_and_research_need_the_task_statements_path(self):
        tmp = tempfile.mkdtemp(prefix="e003-r2e-")
        self.addCleanup(shutil.rmtree, tmp, True)
        r = os.path.join(tmp, "r")
        os.makedirs(r)
        e = dict(os.environ)
        e.update(ENV)
        for args in (["init", "-q"], ["commit", "-q", "--allow-empty", "-m", "s"]):
            subprocess.run(["git", "-C", r] + args, env=e, check=True, capture_output=True)
        s = subprocess.run(["git", "-C", r, "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
        out = os.path.join(tmp, "out")
        base = ["make", "--repo", r, "--out", out, "--checker-role", "reviewer", "--role-file", "x.md"]
        built = base + ["--kind", "built", "--start", s, "--final", s]
        research = base + ["--kind", "research", "--memo-commit", s, "--memo-path", "m.md"]
        self.assertEqual(run("export.py", *built, "--label", "B1").returncode, 1)
        self.assertEqual(run("export.py", *research, "--label", "R1").returncode, 1)
        self.assertFalse(os.path.exists(os.path.join(out, "INDEX")), "nothing written on a refusal")
        self.assertEqual(run("export.py", *built, "--label", "B2", "--task-statement-path", "specs/S.md").returncode, 0)
        self.assertEqual(run("export.py", *research, "--label", "R2", "--task-statement-path", "q.md").returncode, 0)


if __name__ == "__main__":
    unittest.main()
