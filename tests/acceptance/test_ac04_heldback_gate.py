"""AC4 [trace: V1 -> AC4] -- when a kind's comparison opens, its held-back check already exists, written
by a blind Check author that ran as a helper of a sheet session the owner started with the sheets
repository only, from a pack folder matching the manifest recorded from `S-001-holdout`, and whose
transcript shows no read, search or command outside that folder and no web or network use; that session
is not the one that wrote S-001's locked checks, and the session that wrote them never held a held-back
check; the check is in the sheets repository with its fingerprint recorded in governance/HOLDOUTS.md, and
no session that does or starts the work, and no arm's copy, brief or export, has held it.

What a file-level check can show is tested here; the rest (which repositories a session was started with,
the owner's choices) is shown by the first-use checks K1 to K7 in the kind's record, not by a test.
 - The gate: src/E-003/kind.py can-open --kind K --holdouts governance/HOLDOUTS.md --sheet-record FILE
   -> {"eligible": bool, "reason": str} (FAILS until built).
 - governance/HOLDOUTS.md holds only `<set id>  <fingerprint>` lines, no sheet text, and the repository
   holds no holdouts/ tree (PASSES now).
 - The locked checks' author session is not recorded anywhere on the held-back side (PASSES now).
 - The transcript check on the blind Check author is tested in test_ac05_judging.py (TestTranscriptCheck).
GAP: the spec gives no command for "the kind opens"; kind.py can-open is the smallest gate a test can call.
"""
import os
import re
import subprocess

from e003_support import Base, ROOT, FROZEN, git

FP = "ab" * 32
FULL = ["set: S-001-built-1", "repository-commit: " + "0123456789abcdef0123456789abcdef01234567",
        "path: holdouts/S-001-built-1.md", "fingerprint: " + FP, "tests: 5", "pack: match", "scan: clean",
        "model: claude-sonnet-5-5", "runs: 1", "tokens: 41000", "k1-canary: unseen", "k2: pass", "k3: pass",
        "k4: pass", "k5: pass"]
HOLD = "# Hidden holdout sets\n\n```holdouts\n# <set id>  <fingerprint>\n%s\n```\n"


class TestAC4Gate(Base):
    def can_open(self, kind="built", holdout_lines=("S-001-built-1  " + FP,), block=FULL):
        h = self.write("HOLDOUTS.md", HOLD % "\n".join(holdout_lines))
        b = self.write("sheet.md", "\n".join(block) + "\n")
        return self.decide("kind.py", "can-open", "--kind", kind, "--holdouts", h, "--sheet-record", b)

    def test_the_kind_opens_when_its_sheet_is_placed_and_recorded(self):
        out = self.can_open()
        self.assertTrue(out["eligible"], out)

    def test_no_held_back_check_for_the_kind_means_it_does_not_open(self):
        out = self.can_open(holdout_lines=())
        self.assertFalse(out["eligible"])
        self.assertRegex(out["reason"].lower(), "held-back|holdout|sheet|fingerprint")
        self.assertFalse(self.can_open(kind="plans")["eligible"], "built's set is not plans'")

    def test_a_void_sheet_means_it_does_not_open(self):
        void = ["set: S-001-built-1", "scan: void", "hit: 57", "runs: 1", "tokens: 9000", "k1-canary: unseen",
                "k2: pass", "k3: pass", "k4: pass", "k5: pass"]
        self.assertFalse(self.can_open(block=void)["eligible"])

    def test_a_stopped_sheet_means_it_does_not_open(self):
        stopped = ["set: S-001-built-1", "pack: differs", "stopped: pack", "runs: 0", "tokens: 10", "k1-canary: unread",
                   "k2: untested", "k3: untested", "k4: untested", "k5: untested"]
        self.assertFalse(self.can_open(block=stopped)["eligible"])

    def test_the_recorded_fingerprint_must_be_the_blocks(self):
        self.assertFalse(self.can_open(holdout_lines=("S-001-built-1  " + "cd" * 32,))["eligible"])

    def test_a_malformed_holdouts_line_does_not_count(self):
        for line in ("S-001-built-1 " + FP, "S-001-built-1  " + FP[:60], "S-001-built-1  " + FP.upper(),
                     "S-001-built-1\t" + FP):
            self.assertFalse(self.can_open(holdout_lines=(line,))["eligible"], line)

    def test_a_block_with_a_line_that_is_not_one_of_the_forms_is_not_recorded(self):
        self.assertFalse(self.can_open(block=FULL + ["1. a line of the sheet"])["eligible"])

    def test_the_sheet_must_have_been_placed_under_the_kinds_set_id(self):
        wrong = [l.replace("S-001-built-1", "S-001-plans-1") for l in FULL]
        self.assertFalse(self.can_open(block=wrong)["eligible"], "plans' block does not open built")


class TestAC4Repository(Base):
    def test_holdouts_md_holds_only_set_lines_and_no_sheet_text(self):
        text = open(os.path.join(ROOT, "governance", "HOLDOUTS.md"), encoding="utf-8").read()
        body = re.search(r"```holdouts\n(.*?)```", text, re.S).group(1)
        for line in body.splitlines():
            if not line.strip() or line.startswith("#"):
                continue
            self.assertRegex(line, r"^S-001-(built|plans|research)-\d+  [0-9a-f]{64}$", line)

    def test_no_holdouts_tree_is_tracked_in_model_lab(self):
        tracked = git(ROOT, "ls-files", "holdouts")
        self.assertEqual(tracked, "")
        self.assertFalse(os.path.exists(os.path.join(ROOT, "holdouts")))

    def test_no_tracked_file_outside_the_spec_family_and_records_names_a_sheet_path(self):
        out = git(ROOT, "grep", "-l", "-E", r"holdouts/S-001-(built|plans|research)-[0-9]+\.md", "--", ".",
                  check=False)
        allowed = {"specs/S-001.md", "experiments/E-003.md"}
        extra = {f for f in out.split() if f not in allowed and not f.startswith(("reviews/", "docs/", "decisions/",
                                                                                      "tests/acceptance/"))}
        self.assertEqual(extra, set(), "paths that name a sheet outside the spec family and records")

    def test_the_session_that_wrote_the_locked_checks_is_not_a_sheets_side_session(self):
        """Every commit touching the locked checks carries an Agent-Session trailer, and none of those ids
        appears in any record of the held-back side (reviews/E-003/**) or in governance/HOLDOUTS.md."""
        log = git(ROOT, "log", "--format=%H%x00%B%x01", "%s..HEAD" % FROZEN, "--", "tests/acceptance", "checks")
        sessions = set()
        for rec in [r for r in log.split("\x01") if r.strip()]:
            h, body = rec.strip().split("\x00", 1)
            m = re.search(r"^Agent-Session: (\S+)$", body, re.M)
            self.assertIsNotNone(m, "commit %s touches the locked checks without an Agent-Session trailer" % h[:8])
            sessions.add(m.group(1))
        held_side = [os.path.join(ROOT, "governance", "HOLDOUTS.md")]
        for d, _, fs in os.walk(os.path.join(ROOT, "reviews", "E-003")):
            held_side += [os.path.join(d, f) for f in fs]
        for path in held_side:
            if os.path.isfile(path):
                body = open(path, encoding="utf-8", errors="replace").read()
                for s in sessions:
                    self.assertNotIn(s, body, "%s names the locked checks' author session" % path)
