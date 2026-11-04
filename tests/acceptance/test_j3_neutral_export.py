"""join-test: S-001/J3

J3 -- arm -> neutral export -> judge.  For plans and built work, the arm's deliverable as a git bundle of
exactly two commits, the first holding the tree of the piece's start commit and the second, its child,
the arm's final tree, both with one neutral author and committer, one fixed date, and the messages
`start` and `<label>`; for research, a bundle of one commit, the tree at the memo's submission commit,
message `<label>`.  Beside each bundle `<label>.fill.json`, and one INDEX line: label, kind, bundle path,
the bundle's SHA-256, the fill file's SHA-256, tab-separated; when every pair has its exports, a final
line `last`.  A bundle whose SHA-256 differs from its index line gets no judgement.  The test covers it
"on exports made from a test repository: two commits with the neutral fields, the trees equal to the
start and final commits', and no other object reachable."

Interface named (e003_support.py): src/E-003/export.py make | finish | verify | list.
GAPS: the spec names no fixed date, no neutral author, no bundle file name or fill-file keys; the test
requires only that author = committer, the same in both commits and in every export, not the test
repository's, and the date fixed (identical across exports) and not the source commits' date.
FAILS until the Builder builds src/E-003/export.py.
"""
import json
import os
import subprocess

from e003_support import Base, ROOT, commit_files, git, sha256

SECRET_MSG = "CHANGE-PARAGRAPH-NAMED in the arm's own commit message"


class ExportBase(Base):
    def source(self):
        r = self.new_repo("src")
        self.start = commit_files(r, {"README.md": "start tree\n", "dir/a.txt": "a\n"}, "start commit message",
                                  when="2026-11-01T10:00:00Z")
        commit_files(r, {"dir/a.txt": "a changed\n"}, "arm commit one", when="2026-11-02T10:00:00Z")
        self.final = commit_files(r, {"new.txt": "deliverable\n", "dir/b.txt": "b\n"}, SECRET_MSG,
                                  when="2026-11-03T10:00:00Z")
        return r

    def make(self, kind, label, repo, out, **extra):
        args = ["make", "--kind", kind, "--repo", repo, "--label", label, "--out", out,
                "--checker-role", "reviewer", "--role-file", ".claude/agents/reviewer.md"]
        if kind == "research":
            args += ["--memo-commit", self.final, "--memo-path", "research/Q-9-memo.md",
                     "--task-statement-path", "research/Q-9.md"]
        else:
            args += ["--start", self.start, "--final", self.final, "--task-statement-text", "Write the thing.",
                     "--task-statement-path", "specs/S-100.md"]
        p = self.run_script("export.py", *args)
        self.assertEqual(p.returncode, 0, p.stderr[-500:])
        return p

    def index_lines(self, out):
        with open(os.path.join(out, "INDEX"), encoding="utf-8") as fh:
            return fh.read().split("\n")

    def resolve(self, out, rel):
        for base in (out, ROOT):
            p = os.path.join(base, rel)
            if os.path.isfile(p):
                return p
        self.fail("INDEX names a bundle that is not there: %s" % rel)

    def clone(self, bundle, name):
        dest = os.path.join(self.tmp, name)
        p = subprocess.run(["git", "clone", "-q", bundle, dest], capture_output=True, text=True)
        self.assertEqual(p.returncode, 0, p.stderr)
        return dest


class TestJ3(ExportBase):
    def one(self, kind="built", label="L1"):
        r = self.source()
        out = os.path.join(self.tmp, "exports", kind)
        os.makedirs(out)
        self.make(kind, label, r, out)
        rows = [l for l in self.index_lines(out) if l and l != "last"]
        self.assertEqual(len(rows), 1, rows)
        f = rows[0].split("\t")
        self.assertEqual(len(f), 5, "INDEX line: label, kind, bundle path, bundle SHA-256, fill SHA-256")
        self.assertEqual((f[0], f[1]), (label, kind))
        return r, out, f

    def test_two_commits_neutral_fields_trees_equal_and_nothing_else_reachable(self):
        r, out, f = self.one("built", "L1")
        bundle = self.resolve(out, f[2])
        c = self.clone(bundle, "cl")
        revs = git(c, "rev-list", "--reverse", "--all").split()
        self.assertEqual(len(revs), 2, "exactly two commits")
        first, second = revs
        self.assertEqual(git(c, "rev-list", "--parents", "-n1", second).split(), [second, first])
        self.assertEqual(git(c, "rev-list", "--parents", "-n1", first).split(), [first], "first has no parent")
        self.assertEqual(git(c, "rev-parse", first + "^{tree}"), git(r, "rev-parse", self.start + "^{tree}"))
        self.assertEqual(git(c, "rev-parse", second + "^{tree}"), git(r, "rev-parse", self.final + "^{tree}"))
        self.assertEqual(git(c, "log", "-1", "--format=%B", first).strip(), "start")
        self.assertEqual(git(c, "log", "-1", "--format=%B", second).strip(), "L1")
        fmt = "%an|%ae|%ad|%cn|%ce|%cd"
        a, b = (git(c, "log", "-1", "--format=" + fmt, "--date=raw", x) for x in (first, second))
        self.assertEqual(a, b, "one neutral author and committer and one fixed date in both commits")
        an, ae, ad, cn, ce, cd = a.split("|")
        self.assertEqual((an, ae, ad), (cn, ce, cd))
        self.assertNotIn("Fixture", an + ae)
        self.assertNotIn(ad.split()[0], {git(r, "log", "-1", "--format=%at", x) for x in (self.start, self.final)})
        # no other object is reachable
        want = set(revs)
        for t in (first, second):
            want |= set(l.split()[2] for l in git(c, "ls-tree", "-r", "-t", t).splitlines())
            want.add(git(c, "rev-parse", t + "^{tree}"))
        got = set(l.split()[0] for l in git(c, "rev-list", "--objects", "--all").splitlines())
        self.assertEqual(got, want)
        for secret in (self.start, self.final):
            self.assertNotEqual(subprocess.run(["git", "-C", c, "cat-file", "-e", secret],
                                               capture_output=True).returncode, 0, "source commit reachable")
        self.assertNotIn(SECRET_MSG, git(c, "log", "--all", "--format=%B"))

    def test_fixed_date_and_author_are_the_same_in_every_export(self):
        r, out, f = self.one("built", "L1")
        self.make("built", "L2", r, out)
        rows = [l.split("\t") for l in self.index_lines(out) if l and l != "last"]
        ids = []
        for row in rows:
            c = self.clone(self.resolve(out, row[2]), "c" + row[0])
            ids.append(git(c, "log", "-1", "--format=%an|%ae|%ad|%cd", "--date=raw", "--all"))
        self.assertEqual(len(set(ids)), 1, ids)

    def test_fill_file_beside_the_bundle_and_index_hashes(self):
        r, out, f = self.one("built", "L1")
        bundle = self.resolve(out, f[2])
        fill = os.path.join(os.path.dirname(bundle), "L1.fill.json")
        self.assertTrue(os.path.isfile(fill), "<label>.fill.json beside the bundle")
        self.assertEqual(sha256(open(bundle, "rb").read()), f[3])
        self.assertEqual(sha256(open(fill, "rb").read()), f[4])
        blob = open(fill, encoding="utf-8").read()
        data = json.loads(blob)
        self.assertIsInstance(data, dict)
        for needle in ("reviewer", ".claude/agents/reviewer.md", "L1", "specs/S-100.md"):
            self.assertIn(needle, blob)
        self.assertNotIn("Fixture", blob)
        self.assertNotIn(SECRET_MSG, blob)
        self.assertNotIn(self.final, blob)
        self.assertNotIn(self.start, blob)

    def test_plans_fill_carries_the_task_statement_text(self):
        r, out, f = self.one("plans", "P1")
        fill = os.path.join(os.path.dirname(self.resolve(out, f[2])), "P1.fill.json")
        self.assertIn("Write the thing.", open(fill, encoding="utf-8").read())

    def test_research_export_is_one_commit_with_the_memos_tree(self):
        r, out, f = self.one("research", "R1")
        c = self.clone(self.resolve(out, f[2]), "cr")
        revs = git(c, "rev-list", "--all").split()
        self.assertEqual(len(revs), 1)
        self.assertEqual(git(c, "rev-parse", revs[0] + "^{tree}"), git(r, "rev-parse", self.final + "^{tree}"))
        self.assertEqual(git(c, "log", "-1", "--format=%B", revs[0]).strip(), "R1")

    def test_no_deliverable_means_that_arm_fails_and_no_export_is_made(self):
        r = self.source()
        out = os.path.join(self.tmp, "exports", "none")
        os.makedirs(out)
        before = set(os.listdir(out))
        p = self.run_script("export.py", "make", "--kind", "built", "--repo", r, "--label", "L8", "--out", out,
                            "--checker-role", "reviewer", "--role-file", ".claude/agents/reviewer.md",
                            "--start", self.start, "--final", self.final, "--no-deliverable")
        self.assertEqual(p.returncode, 0, p.stderr[-300:])
        res = json.loads(p.stdout)
        self.assertFalse(res["exported"])
        self.assertEqual(res["arm_result"], "FAIL")
        self.assertEqual(set(os.listdir(out)), before, "no bundle, fill file or INDEX line for it")

    def test_final_line_last_when_every_pair_has_its_exports(self):
        r, out, f = self.one("built", "L1")
        self.assertNotIn("last", self.index_lines(out))
        p = self.run_script("export.py", "finish", "--out", out, "--kind", "built")
        self.assertEqual(p.returncode, 0, p.stderr)
        lines = [l for l in self.index_lines(out) if l != ""]
        self.assertEqual(lines[-1], "last")
        self.assertEqual(lines.count("last"), 1)

    def test_a_bundle_whose_sha256_differs_from_its_index_line_is_refused(self):
        r, out, f = self.one("built", "L1")
        ok = self.run_script("export.py", "verify", "--out", out, "--kind", "built")
        self.assertEqual(ok.returncode, 0, ok.stderr)
        with open(self.resolve(out, f[2]), "ab") as fh:
            fh.write(b"\0")
        bad = self.run_script("export.py", "verify", "--out", out, "--kind", "built")
        self.assertEqual(bad.returncode, 1)

    def test_export_reader_lists_the_files_of_the_final_tree(self):
        r, out, f = self.one("built", "L1")
        p = self.run_script("export.py", "list", self.resolve(out, f[2]))
        self.assertEqual(p.returncode, 0, p.stderr)
        self.assertEqual(sorted(p.stdout.split("\n")[:-1] if p.stdout.endswith("\n") else p.stdout.split("\n")),
                         sorted(git(r, "ls-tree", "-r", "--name-only", self.final).split()))
