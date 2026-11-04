"""join-test: S-001/J2

J2 -- dispatch record -> pair: the recorded brief text, the start commit (full id), the repository, the
kind of work and the model, as one entry per piece; for research, those of the source check, plus the
memo's submission commit.  Awkward cases: a record written after the dispatch or after the round-1
verdict (not eligible); a research item whose researcher is on record but whose source check is not
(not eligible); a Service Desk control file holding several roles (the entry whose `role` is the
dispatched one); a piece the work session first finds more than 7 days after its dispatch (not
eligible, listed).  (The brief with the real repository's absolute path is covered in AC2's test of
the copies; the two-lane case needs a record format the spec does not give: see the return.)

Interface named (e003_support.py): src/E-003/pair.py entry --source FILE [--role R] [--kind K]
[--repo NAME] [--memo-commit SHA] --now ISO -> {"eligible","reason","entry":{brief,start,repo,kind,model,
dispatched_at[,memo_commit]}}.  Sources: a Model-Lab brief record (docs/briefs/README.md fields
`session:`, `model:`, `start:`, `recorded:`, then a `## Brief` section) or a Service Desk control file
(JSON with `brief`, `model`, `source_tip`, `role`, `dispatched_at`, as reviews/<item>/_control/*.json).
GAP: how a control file "holding several roles" is laid out is not given; the test uses a JSON list of
entry objects.  FAILS until the Builder builds src/E-003/pair.py.
"""
import json

from e003_support import Base

SHA = "0123456789abcdef0123456789abcdef01234567"
SHA2 = "fedcba9876543210fedcba9876543210fedcba98"

RECORD = """# Brief 80 -- builder -- stage 3 of S-100

session: session_01ABC
model: claude-opus-5-5 (a fresh session)
start: Model-Lab@%s
recorded: at hand-out, 2026-11-05

## Brief

You are the builder. Build stage 3 of specs/S-100.md.

Return a hand-back.
"""


def control(role, **kw):
    d = {"role": role, "agent": role, "brief": "# Brief -- %s\n\nCheck memo Q-9.\n" % role, "model": "claude-opus-5-5",
         "source_tip": SHA, "dispatched_at": "2026-11-05T09:00:00Z"}
    d.update(kw)
    return d


class TestJ2(Base):
    def entry(self, text, name="rec.md", now="2026-11-06T09:00:00Z", **opts):
        src = self.write(name, text)
        args = ["entry", "--source", src, "--now", now]
        for k, v in opts.items():
            args += ["--" + k.replace("_", "-"), v]
        return self.decide("pair.py", *args)

    def test_brief_record_gives_the_entry(self):
        out = self.entry(RECORD % SHA, kind="built", repo="Model-Lab")
        self.assertTrue(out["eligible"], out)
        e = out["entry"]
        self.assertEqual(e["start"], SHA)
        self.assertEqual(e["model"], "claude-opus-5-5")
        self.assertEqual(e["repo"], "Model-Lab")
        self.assertEqual(e["kind"], "built")
        self.assertIn("Build stage 3 of specs/S-100.md.", e["brief"])
        self.assertIn("Return a hand-back.", e["brief"])
        self.assertNotIn("session: session_01ABC", e["brief"], "the recorded brief is the Brief section only")

    def test_record_without_a_full_start_commit_is_not_eligible(self):
        for start in ("Model-Lab@0123456", "", "Model-Lab@" + SHA.upper()):
            out = self.entry((RECORD % SHA).replace("start: Model-Lab@%s" % SHA, "start: " + start),
                             kind="built", repo="Model-Lab")
            self.assertFalse(out["eligible"], start)
            self.assertTrue(out["reason"])

    def test_record_without_a_model_is_not_eligible(self):
        out = self.entry((RECORD % SHA).replace("model: claude-opus-5-5 (a fresh session)\n", ""),
                         kind="built", repo="Model-Lab")
        self.assertFalse(out["eligible"])

    def test_record_written_after_the_dispatch_is_not_eligible(self):
        late = (RECORD % SHA).replace("recorded: at hand-out, 2026-11-05",
                                      "recorded: after hand-out, 2026-11-06, because the start was not noted")
        self.assertFalse(self.entry(late, kind="built", repo="Model-Lab")["eligible"])

    def test_record_made_after_the_round_1_verdict_is_not_eligible(self):
        out = self.entry(RECORD % SHA, kind="built", repo="Model-Lab", round_1_verdict_at="2026-11-04T00:00:00Z")
        self.assertFalse(out["eligible"], "record dated 2026-11-05 follows a verdict of 2026-11-04")

    def test_control_file_with_several_roles_gives_the_dispatched_roles_entry(self):
        both = [control("researcher", brief="RESEARCHER BRIEF", source_tip=None, model="claude-sonnet-5-5"),
                control("source-checker", brief="CHECKER BRIEF", source_tip=SHA2)]
        out = self.entry(json.dumps(both), name="c.json", kind="research", repo="Service-Desk",
                         role="source-checker", memo_commit=SHA)
        self.assertTrue(out["eligible"], out)
        e = out["entry"]
        self.assertEqual(e["brief"], "CHECKER BRIEF")
        self.assertEqual(e["start"], SHA2)
        self.assertEqual(e["memo_commit"], SHA)
        self.assertEqual(e["model"], "claude-opus-5-5")

    def test_research_with_researcher_on_record_but_not_the_source_check_is_not_eligible(self):
        only = [control("researcher", source_tip=None)]
        out = self.entry(json.dumps(only), name="c.json", kind="research", repo="Service-Desk",
                         role="source-checker", memo_commit=SHA)
        self.assertFalse(out["eligible"])
        self.assertTrue(out["reason"])

    def test_research_needs_the_memo_submission_commit(self):
        one = control("source-checker")
        out = self.entry(json.dumps(one), name="c.json", kind="research", repo="Service-Desk", role="source-checker")
        self.assertFalse(out["eligible"])

    def test_more_than_seven_days_after_dispatch_is_not_eligible_and_exactly_seven_is(self):
        rec = RECORD % SHA
        self.assertTrue(self.entry(rec, kind="built", repo="Model-Lab", dispatched_at="2026-11-01T00:00:00Z",
                                   now="2026-11-08T00:00:00Z")["eligible"])
        late = self.entry(rec, kind="built", repo="Model-Lab", dispatched_at="2026-11-01T00:00:00Z",
                          now="2026-11-08T00:00:01Z")
        self.assertFalse(late["eligible"])
        self.assertRegex(late["reason"].lower(), "7 days|seven|late")
