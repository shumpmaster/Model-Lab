"""AC9 [trace: V1 -> AC9] -- when the served model of the doers or the judge changes during a kind's
comparison, pairs are grouped by model, the deciding test is run on the larger group only, and the result
says so.  (E-003 Exclusions 7: a pair whose two arms report different served models is a set-up fault.)

Interface named (e003_support.py): analyse.py run (see test_ac07_decision.py); pairs carry "doer_model"
and "judge_model" (and optionally "arm_models": [change arm's, control arm's]).  Output adds "groups"
({group: pairs}), "decided_on" (the larger group) and a "record" that says the split was made.
GAPS: the spec gives no tie rule and no group-name form; the test avoids ties and reads group names as
"<doer model> / <judge model>" only through the output's own "decided_on" being one of the groups' keys.
FAILS until src/E-003/analyse.py is built.
"""
import json

from e003_support import Base, binom_p_ge, kept_by_test

CARDS = {"answered": 8, "disagreements": 0}


def group(n, n10, n01, model, judge):
    out = []
    for i in range(n):
        kind = "n10" if i < n10 else "n01" if i < n10 + n01 else "both"
        out.append({"piece": "%s-%s-%d" % (model, judge, i), "doer_model": model, "judge_model": judge,
                    "change_pass": kind in ("n10", "both"), "control_pass": kind in ("n01", "both")})
    return out


class TestAC9(Base):
    def run_kind(self, pairs, kind="built"):
        return self.decide("analyse.py", "run", "--kind", kind, "--pairs", self.write("p.json", json.dumps(pairs)),
                           "--cards", self.write("c.json", json.dumps(CARDS)))

    def test_pairs_are_grouped_by_doer_model_and_the_test_runs_on_the_larger_group_only(self):
        big = group(40, 20, 0, "claude-opus-5-5", "claude-fable-5-1")      # clears alone
        small = group(20, 0, 10, "claude-opus-5-6", "claude-fable-5-1")    # the other way
        pooled_p = binom_p_ge(20, 30)
        self.assertGreater(pooled_p, 1 / 40, "the fixture is built so that pooling would not clear")
        out = self.run_kind(big + small)
        self.assertEqual((out["n10"], out["n01"]), (20, 0), "only the larger group's pairs are tested")
        self.assertTrue(out["kept"])
        self.assertEqual(out["n_pairs"], 40)
        self.assertEqual(len(out["groups"]), 2)
        self.assertEqual(sorted(out["groups"].values()), [20, 40])
        self.assertIn("claude-opus-5-5", out["decided_on"])
        self.assertNotIn("claude-opus-5-6", out["decided_on"])
        self.assertRegex(out["record"].lower(), r"model")
        self.assertRegex(out["record"].lower(), r"larger group|larger of")

    def test_the_larger_group_may_be_the_one_that_does_not_clear(self):
        small = group(20, 12, 0, "claude-opus-5-5", "claude-fable-5-1")    # clears alone
        big = group(40, 5, 5, "claude-opus-5-6", "claude-fable-5-1")
        out = self.run_kind(small + big)
        self.assertFalse(out["kept"])
        self.assertIn("claude-opus-5-6", out["decided_on"])

    def test_a_change_of_the_judge_model_also_splits(self):
        a = group(30, 12, 0, "claude-opus-5-5", "claude-fable-5-1")
        b = group(12, 0, 6, "claude-opus-5-5", "claude-fable-5-2")
        out = self.run_kind(a + b)
        self.assertEqual(len(out["groups"]), 2)
        self.assertEqual(out["n_pairs"], 30)
        self.assertTrue(kept_by_test(12, 0) == out["kept"])

    def test_a_single_model_is_one_group_and_no_split_is_claimed(self):
        out = self.run_kind(group(30, 12, 0, "claude-opus-5-5", "claude-fable-5-1"))
        self.assertEqual(len(out["groups"]), 1)
        self.assertNotRegex(out["record"].lower(), r"larger group")

    def test_a_pair_whose_arms_report_different_served_models_is_a_set_up_fault_and_left_out(self):
        pairs = group(30, 12, 0, "claude-opus-5-5", "claude-fable-5-1")
        pairs[0]["arm_models"] = ["claude-opus-5-5", "claude-opus-5-6"]
        out = self.run_kind(pairs)
        self.assertEqual(out["n_pairs"], 29)
        self.assertIn(pairs[0]["piece"], json.dumps(out.get("left_out")))
