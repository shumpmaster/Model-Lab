"""join-test: S-001/J7

J7 -- result record -> the Reviewer's analysis and M4: read by the Reviewer through the pack folder the
Orchestrator assembles by hand from `[roles.S-001-analysis]` (specs/S-001.md, experiments/E-003.md,
experiments/E-003/sizing.py, reviews/E-003/**, src/E-003/records/**, decisions/questions/E-003-*-cards.md),
plus .claude/agents/reviewer.md and the dispatch's brief, whose manifest it records in the dispatch's
brief record, in the form "How a hand-assembled pack is routed" names.  "A test marked join-test:
S-001/J7 covers it: it reads the `S-001-analysis` entry, fails if it is missing, parses the recorded
manifest in the named form, and checks it against the entry: every path, apart from the agent file,
allowed by must_read and matched by none of its must_not_see; experiments/E-003.md, sizing.py, the kind's
verdict record and the kind's card file present; no path under holdouts/ or named governance/HOLDOUTS.md;
patterns compared case-folded, as session_runner.py's `norm` does."

No Builder code is needed.  The pack-entry tests run against governance/PACKS.toml now.  The
recorded-manifest test checks every `## Pack manifest` section found in docs/briefs/*.md whose files
include experiments/E-003.md (classified by the parsed file lines, not by the record's text, so the blind
dispatch's manifest, which also lists reviewer.md, is not taken for one; or the one named by S001_MANIFEST); it
is skipped, saying so, while no analysis dispatch has recorded one -- the spec says the test is
"meaningful only once ... the manifest is recorded", and the analysis is dispatched last.  The same
checks run on synthetic manifests, good and deliberately broken, so the test is not vacuous.
"""
import os
import re
import unittest

from e003_support import (Base, good_manifest, manifest_violations, norm, parse_manifest, pack_entry,
                          manifest_kind, manifest_markers, recorded_manifests, session_runner)

AGENT = ".claude/agents/reviewer.md"
KIND_FILES = ["experiments/E-003.md", "experiments/E-003/sizing.py", "specs/S-001.md",
              "reviews/E-003/built/verdicts.tsv", "reviews/E-003/built/sheet.md", "reviews/E-003/built/sessions.md",
              "decisions/questions/E-003-built-cards.md", "src/E-003/records/built/pairs.jsonl"]


def analysis_problems(text, kind="built"):
    entry = pack_entry("S-001-analysis")
    if entry is None:
        return ["the S-001-analysis entry is missing from governance/PACKS.toml"]
    files, commit, brief, problems = parse_manifest(text)
    problems = list(problems)
    problems += manifest_violations(entry, files, agent_file=AGENT)
    paths = {p for _, p in files}
    for need in ("experiments/E-003.md", "experiments/E-003/sizing.py", "reviews/E-003/%s/verdicts.tsv" % kind,
                 "decisions/questions/E-003-%s-cards.md" % kind):
        if need not in paths:
            problems.append("%s: required and not in the manifest" % need)
    return problems


class TestJ7Entry(Base):
    def test_the_entry_exists(self):
        self.assertIsNotNone(pack_entry("S-001-analysis"), "no [roles.S-001-analysis] in governance/PACKS.toml: "
                             "no analysis dispatch")

    def test_the_entry_matches_the_spec(self):
        e = pack_entry("S-001-analysis")
        self.assertEqual(sorted(e["must_read"]), sorted([
            "specs/S-001.md", "experiments/E-003.md", "experiments/E-003/sizing.py", "reviews/E-003/**",
            "src/E-003/records/**", "decisions/questions/E-003-*-cards.md"]))
        self.assertIn("docs/reports/**", e["must_not_see"])
        for key in ("{spec}", "{ruling}"):
            self.assertNotIn(key, repr(e))

    def test_no_pattern_of_the_entry_reaches_the_sheets(self):
        e = pack_entry("S-001-analysis")
        for path in ("holdouts/S-001-built-1.md", "governance/HOLDOUTS.md", "governance/holdouts.md"):
            self.assertFalse(any(re.search(r"holdouts", norm(p)) for p in e["must_read"]), path)

    def test_comparison_is_case_folded_as_session_runners_norm(self):
        ref = session_runner().norm
        for s in ("Docs/Reports/X.md", "STRASSE", "straße", "é.md", "é.md", "Governance/HOLDOUTS.md"):
            self.assertEqual(norm(s), ref(s), s)


class TestJ7Validation(Base):
    def test_a_good_manifest_has_no_problem(self):
        self.assertEqual(analysis_problems(good_manifest(KIND_FILES + [AGENT])), [])

    def test_a_good_manifest_with_the_agent_file_only_exempt_from_must_read(self):
        self.assertEqual(analysis_problems(good_manifest(KIND_FILES + [AGENT])), [])
        probs = analysis_problems(good_manifest(KIND_FILES + [AGENT, ".claude/agents/critic.md"]))
        self.assertTrue(any("critic.md" in p for p in probs))

    def broken(self, extra=(), drop=(), text=None):
        paths = [p for p in KIND_FILES + [AGENT] if p not in drop] + list(extra)
        return analysis_problems(text or good_manifest(paths))

    def test_paths_outside_must_read_are_refused(self):
        for p in ("docs/PROJECT.md", "experiments/E-003/C1-plans-read-the-check.md", "tests/acceptance/x.py",
                  "BRIEF.md", "src/E-003/harness.py"):
            self.assertTrue(any(p in x for x in self.broken(extra=[p])), p)

    def test_paths_matched_by_must_not_see_are_refused_even_when_case_differs(self):
        for p in ("docs/reports/a.md", "Docs/Reports/a.md", "DOCS/REPORTS/deep/a.md"):
            probs = self.broken(extra=[p])
            self.assertTrue(any(p in x for x in probs), p)

    def test_holdout_paths_are_refused(self):
        for p in ("holdouts/S-001-built-1.md", "Holdouts/S-001-built-1.md", "governance/HOLDOUTS.md",
                  "governance/holdouts.md"):
            self.assertTrue(any(p in x for x in self.broken(extra=[p])), p)

    def test_required_files_must_be_present(self):
        for p in ("experiments/E-003.md", "experiments/E-003/sizing.py", "reviews/E-003/built/verdicts.tsv",
                  "decisions/questions/E-003-built-cards.md"):
            self.assertTrue(any(p in x and "required" in x for x in self.broken(drop=[p])), p)

    def test_the_kinds_files_are_the_kinds(self):
        probs = analysis_problems(good_manifest(KIND_FILES + [AGENT]), kind="plans")
        self.assertTrue(any("plans" in p for p in probs))

    def test_form_defects_are_found(self):
        good = good_manifest(KIND_FILES + [AGENT])
        cases = {
            "uppercase sha": re.sub(r"^[0-9a-f]{64}", "A" * 64, good, count=1, flags=re.M),
            "one space": good.replace("  .claude", " .claude", 1),
            "no commit": re.sub(r"^commit: .*\n", "", good, flags=re.M),
            "no brief line": re.sub(r"^brief: .*\n", "", good, flags=re.M),
            "short commit": re.sub(r"^commit: .*$", "commit: 0123456", good, flags=re.M),
            "wrong heading": good.replace("## Pack manifest", "## Pack Manifest"),
            "wrong info string": good.replace("```manifest", "```text"),
            "two blocks": good.replace("## Helper brief", "```manifest\n```\n\n## Helper brief"),
        }
        lines = good.split("```manifest\n")[1].split("\n")
        file_lines = [l for l in lines if re.match(r"^[0-9a-f]{64}  ", l)]
        unsorted = good.replace("\n".join(file_lines), "\n".join(reversed(file_lines)))
        cases["not sorted"] = unsorted
        for name, text in cases.items():
            self.assertTrue(analysis_problems(text), "form defect not found: " + name)


class TestJ7Classify(Base):
    def test_the_blind_dispatchs_manifest_is_not_taken_for_an_analysis_manifest(self):
        blind = good_manifest(["experiments/E-003/check-author-extract.md", ".claude/agents/critic.md",
                               ".claude/agents/reviewer.md", ".claude/agents/source-checker.md",
                               "docs/playbooks/software.md", ".claude/agents/check-author.md"])
        self.assertEqual(manifest_kind(blind), "blind")
        self.assertEqual(manifest_kind(good_manifest(KIND_FILES + [AGENT])), "analysis")
        self.assertIsNone(manifest_kind("no manifest here"))


class TestJ7Recorded(Base):
    def test_every_recorded_analysis_manifest_conforms(self):
        named = bool(os.environ.get("S001_MANIFEST"))
        # A record named by S001_MANIFEST is checked here if its files include experiments/E-003.md or it
        # has no file lines; a record carrying both kinds' files is checked, and failed, by J7 and J8 alike.
        def mine(t):
            has_files, blind, analysis = manifest_markers(t)
            return analysis or not has_files
        found = [(rel, t) for rel, t in recorded_manifests()
                 if (mine(t) if named else manifest_kind(t) == "analysis")]
        if not found:
            self.skipTest("S001_MANIFEST names a manifest of the other kind (J8's); this test checks analysis "
                          "manifests" if named else
                          "no analysis dispatch has recorded a manifest yet (J7 runs before each analysis dispatch)")
        for rel, text in found:
            kind = (re.search(r"reviews/E-003/(built|plans|research)/", text) or [None, "built"])[1]
            self.assertEqual(analysis_problems(text, kind), [], rel)


if __name__ == "__main__":
    unittest.main()
