"""AC10 [trace: V2 -> AC10] -- when a change is kept, its result record gives the V2 measure for its kind
(first-time pass rate over the first 30 pieces checked under the changed operating model, against the
starting figure, at 1 in 25), how those pieces are counted from the review records, and its removal test,
so the operating model can carry, monitor and remove it after M5 without Model-Lab.

Interface named (e003_support.py): analyse.py run (see test_ac07_decision.py) -> "record" text for a kept
change; analyse.py v2 --kind K --passes N -> {"meets_v2": bool, "cutoff": n}.
V2 (docs/PROJECT.md section 6): over the first 30 pieces of the kind, above the starting figure (plans 2 of
44, research 5 of 19, built work 32 of 80) by so much that chance alone would produce it at most 1 time in
25; the section works the cutoffs out as 5, 13 and 18 first-time passes (exact binomial, one-sided).
The record must carry the removal test's three conditions as experiments/E-003/C<n>-*.md states them.
GAP: the spec does not say what "how those pieces are counted from the review records" contains; the test
asks that the record name the review records and say how a piece is counted (first-time = passed in its
first review round).  FAILS until src/E-003/analyse.py is built.
"""
import json
import os
import re
from math import comb

from e003_support import Base, CHANGE_FILE, ROOT

KINDS = {"plans": ("C1", 2 / 44, 5), "research": ("C3", 5 / 19, 13), "built": ("C2", 32 / 80, 18)}


def cutoff(p, n=30, alpha=1 / 25):
    for k in range(n + 1):
        if sum(comb(n, j) * p ** j * (1 - p) ** (n - j) for j in range(k, n + 1)) <= alpha:
            return k


def kept_pairs(kind):
    if kind == "research":
        return [{"piece": "m%d" % i, "doer_model": "m", "judge_model": "j", "change_check_pass": True,
                 "control_check_pass": i >= 14, "memo_judge_pass": True} for i in range(28)] + \
               [{"piece": "n%d" % i, "doer_model": "m", "judge_model": "j", "change_check_pass": False,
                 "control_check_pass": False, "memo_judge_pass": True} for i in range(20)]
    return [{"piece": "p%d" % i, "doer_model": "m", "judge_model": "j", "change_pass": True,
             "control_pass": i >= 14} for i in range(28)] + \
           [{"piece": "n%d" % i, "doer_model": "m", "judge_model": "j", "change_pass": False,
             "control_pass": False} for i in range(20)]


class TestAC10(Base):
    def test_the_cutoffs_in_project_md_are_what_the_binomial_gives(self):
        for kind, (cid, p0, want) in KINDS.items():
            self.assertEqual(cutoff(p0), want, kind)

    def test_v2_meets_at_the_cutoff_and_not_below(self):
        for kind, (cid, p0, want) in KINDS.items():
            for passes in range(0, 31):
                out = self.decide("analyse.py", "v2", "--kind", kind, "--passes", str(passes))
                self.assertEqual(out["meets_v2"], passes >= want, "%s %d" % (kind, passes))
            self.assertEqual(out["cutoff"], want)

    def record(self, kind):
        out = self.decide("analyse.py", "run", "--kind", kind,
                          "--pairs", self.write("p.json", json.dumps(kept_pairs(kind))),
                          "--cards", self.write("c.json", json.dumps({"answered": 8, "disagreements": 0})))
        self.assertTrue(out["kept"], out)
        return out["record"]

    def test_a_kept_changes_record_gives_v2_and_how_pieces_are_counted_and_the_removal_test(self):
        for kind, (cid, p0, want) in KINDS.items():
            rec = self.record(kind)
            flat = " ".join(rec.split())
            self.assertRegex(flat, r"first 30", kind)
            self.assertRegex(flat, r"1 in 25", kind)
            self.assertRegex(flat, r"(?i)starting figure", kind)
            self.assertRegex(flat, r"(?<!\d)%d(?!\d)" % want, "the cutoff for %s" % kind)
            self.assertRegex(flat, r"(?i)review record", kind)
            self.assertRegex(flat, r"(?i)first[- ]time|first round|round 1", kind)
            self.assertRegex(flat, r"(?i)removal test", kind)
            self.assertIn(cid, flat)

    def test_the_removal_conditions_of_the_change_file_are_carried(self):
        for kind, (cid, p0, want) in KINDS.items():
            rec = " ".join(self.record(kind).split())
            text = open(os.path.join(ROOT, CHANGE_FILE[cid]), encoding="utf-8").read()
            removal = text.split("## Removal test", 1)[1]
            items = re.findall(r"^\d\. (.+)$", removal, re.M)
            self.assertGreaterEqual(len(items), 3)
            for key in ("does not clear V1", "next scheduled review", "AI model that runs"):
                self.assertTrue(any(key in i for i in items), key)
                self.assertIn(key, rec, "%s: removal condition %r missing from the record" % (kind, key))

    def test_the_record_stands_without_model_lab(self):
        rec = self.record("built")
        self.assertRegex(rec, r"(?i)M5|operating model")
        self.assertNotRegex(rec, r"(?i)\bsee (src|experiments)/E-003\b", "must not rest on Model-Lab paths to be read")
