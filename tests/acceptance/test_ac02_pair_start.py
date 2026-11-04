"""AC2 [trace: V1 -> AC2] -- a new piece dispatched in a participating project with its record made at
dispatch (plans and built work: the worker's brief, start commit and model; research: the memo's
submission and the source check's brief, start commit and model): the harness runs both arms from that
start commit in fresh copies, with briefs that differ only by the change paragraph, on the same served
model, starting within the same hour and within 7 days of the dispatch, and records the pair; a piece
with no such record does not enter and is listed.

Interfaces named (e003_support.py): src/E-003/pair.py entry (eligibility) and pair.py plan --no-run
(makes the two copies and returns the arms, starting no session).  GAP: the spec does not say where the
"pair record" lives; the test checks the returned arms only.  FAILS until src/E-003/pair.py is built.
"""
import json
import os
import subprocess

from e003_support import Base, git, commit_files, filled

SD_BRIEF = ("# Brief -- X-1, builder\n\nYou are the builder.\n\nTASK STATEMENT: build stage 2 of specs/S-100.md "
            "in {real}.\n\nReturn a hand-back.\n")


class TestAC2(Base):
    def make_entry(self, kind="built", model="claude-opus-5-5", dispatched="2026-11-05T09:00:00Z"):
        real = self.new_repo("real")
        base = commit_files(real, {"specs/S-100.md": "# Spec\n", ".claude/agents/critic.md": "critic\n",
                                   "a.txt": "start\n"}, "start", when="2026-11-01T10:00:00Z")
        parent = commit_files(real, {"a.txt": "start\nmore\n"}, "second", when="2026-11-02T10:00:00Z")
        later = commit_files(real, {"b.txt": "later\n"}, "after the start", when="2026-11-05T12:00:00Z")
        self.start, self.later = parent, later
        brief = SD_BRIEF.format(real=real)
        entry = {"brief": brief, "start": parent, "repo": "Service-Desk", "kind": kind, "model": model,
                 "dispatched_at": dispatched, "real_path": real}
        if kind == "research":
            entry["memo_commit"] = base   # the memo is submitted before the source check starts
        self.entry_file = self.write("entry.json", json.dumps(entry))
        self.real = real
        self.brief = brief
        return entry

    def plan(self, change, now="2026-11-06T09:00:00Z"):
        out = self.decide("pair.py", "plan", "--entry", self.entry_file, "--repos-root", self.tmp,
                          "--change", change, "--now", now, "--no-run")
        self.assertEqual(len(out["arms"]), 2, out)
        return {a["arm"]: a for a in out["arms"]}

    def check_copies(self, arms):
        self.assertEqual(set(arms), {"control", "change"})
        self.assertNotEqual(arms["control"]["copy"], arms["change"]["copy"], "two fresh copies")
        for a in arms.values():
            c = a["copy"]
            self.assertTrue(os.path.isdir(c))
            self.assertEqual(a["commit"], self.start)
            self.assertEqual(git(c, "rev-parse", "HEAD"), self.start)
            revs = set(git(c, "rev-list", "--all").split())
            ancestors = set(git(self.real, "rev-list", self.start).split())
            self.assertEqual(revs, ancestors, "a copy holds the start commit and its ancestors only")
            self.assertNotIn(self.later, revs)
            self.assertFalse(os.path.exists(os.path.join(c, "b.txt")))

    def test_plans_and_built_work_two_arms_from_the_start_commit(self):
        entry = self.make_entry("built")
        arms = self.plan("C2")
        self.check_copies(arms)
        self.assertEqual(arms["control"]["model"], entry["model"])
        self.assertEqual(arms["change"]["model"], entry["model"], "same served model in both arms")

    def test_briefs_differ_only_by_the_change_paragraph_and_the_copys_path(self):
        self.make_entry("built")
        arms = self.plan("C2")
        ctl, chg = arms["control"]["brief"], arms["change"]["brief"]
        for a, b in ((ctl, arms["control"]["copy"]), (chg, arms["change"]["copy"])):
            self.assertNotIn(self.real, a, "the real repository's absolute path is replaced by the copy's")
            self.assertIn(b, a)
        ctl_c = ctl.replace(arms["control"]["copy"], "<COPY>")
        chg_c = chg.replace(arms["change"]["copy"], "<COPY>")
        expected_ctl = self.brief.replace(self.real, "<COPY>")
        self.assertEqual(ctl_c, expected_ctl, "nothing but the path changed in the no-change brief")
        self.assertNotEqual(chg_c, ctl_c)
        paragraph = [p for p in chg_c.split("\n\n") if p not in ctl_c.split("\n\n")]
        self.assertEqual(len(paragraph), 1, "exactly one paragraph differs")
        self.assertTrue(paragraph[0].startswith("The inputs for this task, by path: "), paragraph[0])
        self.assertEqual("\n\n".join(p for p in chg_c.split("\n\n") if p != paragraph[0]), ctl_c)

    def test_arms_start_within_the_same_hour_and_within_seven_days_of_dispatch(self):
        from datetime import datetime, timedelta
        self.make_entry("built", dispatched="2026-11-05T09:00:00Z")
        arms = self.plan("C2", now="2026-11-06T09:00:00Z")
        t = {k: datetime.fromisoformat(a["start_at"].replace("Z", "+00:00")) for k, a in arms.items()}
        self.assertLessEqual(abs(t["control"] - t["change"]), timedelta(hours=1))
        d0 = datetime.fromisoformat("2026-11-05T09:00:00+00:00")
        for v in t.values():
            self.assertLessEqual(v - d0, timedelta(days=7))

    def test_research_runs_two_source_checks_from_the_checks_start_commit(self):
        self.make_entry("research")
        arms = self.plan("C3")
        self.check_copies(arms)
        paras = [p for p in arms["change"]["brief"].split("\n\n") if p not in arms["control"]["brief"].split("\n\n")]
        self.assertEqual(len(paras), 1)
        self.assertTrue(paras[0].startswith("A source you cannot open is not by itself a fault"), paras[0])

    def test_a_pair_is_refused_when_the_start_is_more_than_seven_days_after_dispatch(self):
        self.make_entry("built", dispatched="2026-10-20T09:00:00Z")
        p = self.run_script("pair.py", "plan", "--entry", self.entry_file, "--repos-root", self.tmp,
                            "--change", "C2", "--now", "2026-11-06T09:00:00Z", "--no-run")
        if p.returncode == 0:
            out = json.loads(p.stdout)
            self.assertFalse(out.get("arms"), "no arm may start 17 days after dispatch")
        else:
            self.assertEqual(p.returncode, 1)

    def test_a_piece_with_no_record_does_not_enter_and_is_listed(self):
        for kind in ("plans", "built", "research"):
            src = self.write("none-%s.md" % kind, "# Brief 99\n\nsession: s\nrecorded: at hand-out, 2026-11-05\n\n"
                             "## Brief\n\nNo model, no start.\n")
            out = self.decide("pair.py", "entry", "--source", src, "--kind", kind, "--repo", "Service-Desk",
                              "--now", "2026-11-06T09:00:00Z")
            self.assertFalse(out["eligible"], kind)
            self.assertRegex(out["reason"].lower(), "model|start|record|memo|check")

    def test_only_public_participating_repositories_enter(self):
        sha = "0123456789abcdef0123456789abcdef01234567"
        rec = ("# Brief 80\n\nsession: s\nmodel: claude-opus-5-5\nstart: X@%s\nrecorded: at hand-out, 2026-11-05\n\n"
               "## Brief\n\nDo it.\n" % sha)
        src = self.write("rec.md", rec)
        for repo, ok in (("Service-Desk", True), ("Model-Lab", True), ("Personal-Org-Operating-Model", False)):
            out = self.decide("pair.py", "entry", "--source", src, "--kind", "built", "--repo", repo,
                              "--now", "2026-11-06T09:00:00Z")
            self.assertEqual(out["eligible"], ok, repo)
