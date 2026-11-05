"""join-test: S-001/J8

J8 -- extract -> the blind Check author (dispatch (a)).  "A test marked join-test: S-001/J8 covers it,
written in dispatch (b).  It reads the `S-001-holdout` entry of governance/PACKS.toml and fails if the
entry is missing or carries `{spec}`, `{ruling}`, may_read or include_feedback.  It parses the dispatch's
recorded manifest in the named form and fails unless every path in it, apart from .claude/agents/
check-author.md, is allowed by the entry's must_read and matched by none of its must_not_see, the extract
is present, and no path matches a withheld path of this spec (those under must_not_see in "Two Check
author jobs") or is governance/HOLDOUTS.md or under holdouts/.  Patterns are compared case-folded, as
session_runner.py's `norm` does.  It also fails if the extract names a withheld path, a change id (C1,
C2, C3) or "arm", or holds a sentence of a change text.  It is meaningful only once the pack entry exists
and the manifest is recorded, so it runs before each blind dispatch."

No Builder code is needed.  The entry and extract tests run now.  The recorded-manifest test checks every
`## Pack manifest` section in docs/briefs/*.md whose parsed file lines include the extract or
.claude/agents/check-author.md; it is skipped, saying so, while no blind dispatch has recorded one.  Before
each blind dispatch run it as
    S001_BLIND_MANIFEST=<the dispatch's brief record> python3 -m unittest discover -s tests/acceptance -p 'test_j8*.py'
With that setting the test checks that record, whatever it holds (no file lines, either kind's files,
neither), and never skips it; it ignores S001_ANALYSIS_MANIFEST and S001_MANIFEST.  The same checks run on synthetic
manifests, good and deliberately broken.
"""
import os
import re
import unittest

from e003_support import (Base, CHANGE_FILE, CHANGE_TEXT, ROOT, good_manifest, manifest_violations, norm,
                          manifest_kind, parse_manifest, pack_entry, pattern_matches, recorded_manifests)

AGENT = ".claude/agents/check-author.md"
EXTRACT = "experiments/E-003/check-author-extract.md"
WITHHELD = ["specs/S-001.md", "experiments/E-003.md", "experiments/E-003/C?-*.md", "tests/acceptance/**",
            "checks/**", "reviews/S-001/**", "reviews/E-003/**", "docs/briefs/**", "docs/gates/**",
            "decisions/**", "src/**"]
GOOD = [EXTRACT, ".claude/agents/critic.md", ".claude/agents/reviewer.md", ".claude/agents/source-checker.md",
        "docs/playbooks/software.md", AGENT]


def holdout_problems(text):
    entry = pack_entry("S-001-holdout")
    if entry is None:
        return ["the S-001-holdout entry is missing from governance/PACKS.toml"]
    files, commit, brief, problems = parse_manifest(text)
    problems = list(problems)
    problems += manifest_violations(entry, files, withheld=WITHHELD, agent_file=AGENT)
    if EXTRACT not in {p for _, p in files}:
        problems.append("the extract is not in the manifest")
    return problems


class TestJ8Entry(Base):
    def test_the_entry_exists_and_carries_none_of_the_forbidden_keys(self):
        e = pack_entry("S-001-holdout")
        self.assertIsNotNone(e, "no [roles.S-001-holdout] in governance/PACKS.toml: no blind dispatch")
        for key in ("may_read", "include_feedback"):
            self.assertNotIn(key, e)
        for placeholder in ("{spec}", "{ruling}"):
            self.assertNotIn(placeholder, repr(e))

    def test_must_read_is_the_extract_the_three_role_files_and_the_playbooks(self):
        e = pack_entry("S-001-holdout")
        self.assertEqual(sorted(e["must_read"]), sorted([
            EXTRACT, ".claude/agents/critic.md", ".claude/agents/reviewer.md", ".claude/agents/source-checker.md",
            "docs/playbooks/**"]))

    def test_must_not_see_lists_every_withheld_path(self):
        e = pack_entry("S-001-holdout")
        self.assertEqual(sorted(e["must_not_see"]), sorted(WITHHELD))

    def test_the_change_texts_are_withheld_and_the_extract_is_not(self):
        e = pack_entry("S-001-holdout")
        for rel in CHANGE_FILE.values():
            self.assertTrue(any(pattern_matches(p, rel) for p in e["must_not_see"]), rel)
            self.assertTrue(any(pattern_matches(p, rel.upper()) for p in e["must_not_see"]), "case-folded: " + rel)
        self.assertFalse(any(pattern_matches(p, EXTRACT) for p in e["must_not_see"]),
                         "the extract must not be withheld ('C*.md' would hide it)")
        self.assertTrue(any(pattern_matches(p, EXTRACT) for p in e["must_read"]))

    def test_no_pattern_of_the_entry_names_the_holdout_record(self):
        e = pack_entry("S-001-holdout")
        for p in e["must_read"]:
            self.assertNotIn("holdouts", norm(p))


class TestJ8Extract(Base):
    def setUp(self):
        super().setUp()
        with open(os.path.join(ROOT, EXTRACT), encoding="utf-8") as fh:
            self.text = fh.read()

    def test_the_extract_names_no_withheld_path(self):
        low = norm(self.text)
        for frag in ("specs/s-001", "experiments/e-003", "tests/acceptance", "checks/", "reviews/s-001",
                     "reviews/e-003", "docs/briefs", "docs/gates", "decisions/", "src/", "holdouts.md",
                     "c?-*.md"):
            self.assertNotIn(frag, low, "the extract names a withheld path: " + frag)

    def test_the_extract_names_no_change_id_and_not_the_word_arm(self):
        self.assertIsNone(re.search(r"\bC[123]\b", self.text), "a change id appears in the extract")
        self.assertIsNone(re.search(r"(?i)\barms?\b", self.text), 'the word "arm" appears in the extract')

    def test_the_extract_holds_no_sentence_of_a_change_text(self):
        flat = " ".join(norm(self.text).split())
        for cid, text in CHANGE_TEXT.items():
            for sentence in re.split(r"(?<=[.:;])\s+", " ".join(text.split())):
                s = " ".join(norm(re.sub(r"<[^>]*>", "", sentence)).split()).strip(" .:;")
                if len(s.split()) >= 4:
                    self.assertNotIn(s, flat, "the extract holds a sentence of %s: %r" % (cid, s))

    def test_the_extract_is_as_frozen(self):
        """J8 awkward case: the extract edited after the freeze is a revision, and the Check author is not
        dispatched on it."""
        import subprocess
        from e003_support import FROZEN
        p = subprocess.run(["git", "-C", ROOT, "diff", "--name-status", FROZEN, "HEAD", "--", EXTRACT],
                           capture_output=True, text=True)
        self.assertEqual(p.returncode, 0, p.stderr)
        self.assertEqual(p.stdout.strip(), "", "the extract changed since the freeze:\n" + p.stdout)

    def test_the_extract_says_the_check_goes_to_the_lead_only(self):
        self.assertRegex(self.text, r"(?i)agent that started you")
        self.assertRegex(self.text, r"(?i)nowhere else")


class TestJ8Validation(Base):
    def problems(self, extra=(), drop=(), text=None):
        return holdout_problems(text or good_manifest([p for p in GOOD if p not in drop] + list(extra)))

    def test_a_good_manifest_has_no_problem(self):
        self.assertEqual(self.problems(), [])

    def test_the_agent_file_is_the_only_path_exempt_from_must_read(self):
        self.assertEqual(self.problems(), [])
        self.assertTrue(self.problems(extra=[".claude/agents/builder.md"]))
        self.assertTrue(self.problems(extra=["BRIEF.md"]), "the brief is the `brief:` line, not a file line")

    def test_withheld_paths_are_refused_each(self):
        for p in ("specs/S-001.md", "experiments/E-003.md", "experiments/E-003/C1-plans-read-the-check.md",
                  "experiments/E-003/C2-built-named-inputs.md", "experiments/E-003/c3-research-check-what-it-can-open.md",
                  "tests/acceptance/test_x.py", "checks/y.py", "reviews/S-001/plan.md", "reviews/E-003/built/sheet.md",
                  "docs/briefs/80-x.md", "docs/gates/g.md", "decisions/questions/z.md", "src/E-003/x.py",
                  "SPECS/S-001.MD", "Experiments/E-003/C1-Plans.md"):
            self.assertTrue(any(p.lower() in x.lower() for x in self.problems(extra=[p])), p)

    def test_holdout_paths_are_refused(self):
        for p in ("governance/HOLDOUTS.md", "governance/holdouts.md", "holdouts/S-001-built-1.md"):
            self.assertTrue(any(p in x for x in self.problems(extra=[p])), p)

    def test_the_extract_must_be_present(self):
        self.assertTrue(any("extract" in p for p in self.problems(drop=[EXTRACT])))

    def test_form_defects_are_found(self):
        good = good_manifest(GOOD)
        for name, text in {"one space": good.replace("  .claude", " .claude", 1),
                           "no commit": re.sub(r"^commit: .*\n", "", good, flags=re.M),
                           "no brief": re.sub(r"^brief: .*\n", "", good, flags=re.M),
                           "wrong heading": good.replace("## Pack manifest", "## Manifest"),
                           "wrong info string": good.replace("```manifest", "```")}.items():
            self.assertTrue(holdout_problems(text), name)


class TestJ8Recorded(Base):
    def test_every_recorded_blind_dispatch_manifest_conforms(self):
        named = bool(os.environ.get("S001_BLIND_MANIFEST"))
        # S001_BLIND_MANIFEST names the blind dispatch's record: checked whatever it holds, never skipped
        # (S-001 J8: the pack holds "never ... experiments/E-003.md", and the extract must be present).
        # Unset: the scan of docs/briefs, taking records whose parsed files include the extract or
        # check-author.md.
        found = [(rel, t) for rel, t in recorded_manifests("S001_BLIND_MANIFEST")
                 if named or manifest_kind(t) == "blind"]
        if not found:
            self.skipTest("no blind dispatch has recorded a manifest yet (J8 runs before each blind dispatch; "
                          "set S001_BLIND_MANIFEST=<brief record> to check one)")
        for rel, text in found:
            self.assertEqual(holdout_problems(text), [], rel)


if __name__ == "__main__":
    unittest.main()
