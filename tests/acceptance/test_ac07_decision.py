"""AC7 [trace: V1 -> AC7] -- when the Reviewer analyses a kind, a change is kept only if the judge is
confirmed (6 or more cards answered, at most 2 disagreements) and the exact one-sided test on the
differing pairs clears 1 in 40 (for C3, also the false-pass guard); otherwise the record says "not shown",
with the gain and its 95% range, and "no change helps" stands as an accepted result.

Interface named (e003_support.py): src/E-003/analyse.py run --kind built|plans|research --pairs FILE
--cards FILE -> {"n_pairs","n10","n01","p","gain","ci":[lo,hi],"judge_confirmed","kept","status","record",
"false_pass_guard"}.  Pairs file: JSON list of {"piece","change_pass","control_pass","doer_model",
"judge_model"} (research: {"piece","change_check_pass","control_check_pass","memo_judge_pass", ...}: a
version's pass counts only where the held-back check also passes the memo).  Cards file:
{"answered": n, "disagreements": d} after the owner's answers have replaced the judge's verdicts.
The reference numbers are worked independently in e003_support.py (exact binomial; Newcombe's method 10,
compared to within 0.02).  Anchors from the spec: 10 discordant pairs need 9, 20 need 15.
GAPS: the file shapes are ours; status words are the spec's: "kept", "not shown", "not shown: judge not
confirmed", "too few pieces to test" (fewer than 10 pairs, E-003 Deciding threshold).
FAILS until the Builder builds src/E-003/analyse.py.
"""
import json
import re

from e003_support import Base, binom_p_ge, kept_by_test, newcombe_paired

OK_CARDS = {"answered": 8, "disagreements": 1}


def pairs_of(n10, n01, both=0, neither=0, model="claude-opus-5-5", judge="claude-fable-5-1"):
    out = []
    for kind, count in (("n10", n10), ("n01", n01), ("both", both), ("neither", neither)):
        for i in range(count):
            out.append({"piece": "%s-%d" % (kind, i), "doer_model": model, "judge_model": judge,
                        "change_pass": kind in ("n10", "both"), "control_pass": kind in ("n01", "both")})
    return out


class AnalyseBase(Base):
    def run_kind(self, kind, pairs, cards=OK_CARDS):
        return self.decide("analyse.py", "run", "--kind", kind, "--pairs", self.write("pairs.json", json.dumps(pairs)),
                           "--cards", self.write("cards.json", json.dumps(cards)))


class TestAC7(AnalyseBase):
    def test_spec_anchors(self):
        self.assertFalse(kept_by_test(8, 2))
        self.assertTrue(kept_by_test(9, 1))
        self.assertFalse(kept_by_test(14, 6))
        self.assertTrue(kept_by_test(15, 5))

    def test_the_one_sided_exact_test_on_the_differing_pairs(self):
        for n10, n01 in ((9, 1), (8, 2), (15, 5), (14, 6), (12, 3), (11, 3), (10, 0), (9, 0), (20, 0), (5, 5), (0, 9),
                         (7, 1), (6, 0), (13, 2)):
            out = self.run_kind("built", pairs_of(n10, n01, both=20, neither=10))
            self.assertEqual((out["n10"], out["n01"]), (n10, n01))
            self.assertAlmostEqual(out["p"], binom_p_ge(n10, n10 + n01), places=9)
            self.assertEqual(out["kept"], kept_by_test(n10, n01), "n10=%d n01=%d" % (n10, n01))
            self.assertEqual(out["status"], "kept" if kept_by_test(n10, n01) else "not shown")

    def test_concordant_pairs_do_not_enter_the_test(self):
        a = self.run_kind("plans", pairs_of(9, 1, both=0, neither=0))
        b = self.run_kind("plans", pairs_of(9, 1, both=40, neither=40))
        self.assertEqual((a["p"], a["kept"]), (b["p"], b["kept"]))

    def test_judge_confirmation_needs_six_answered_and_at_most_two_disagreements(self):
        clearing = pairs_of(15, 3, both=20, neither=22)
        for answered, dis, want in ((6, 2, True), (6, 3, False), (5, 0, False), (8, 2, True), (8, 3, False),
                                    (12, 2, True), (12, 0, True), (4, 0, False), (0, 0, False), (6, 0, True)):
            out = self.run_kind("built", clearing, {"answered": answered, "disagreements": dis})
            self.assertEqual(out["judge_confirmed"], want, (answered, dis))
            self.assertEqual(out["kept"], want, (answered, dis))
            if not want:
                self.assertIn("judge not confirmed", out["status"])

    def test_not_shown_carries_the_gain_and_its_95_percent_range(self):
        pairs = pairs_of(8, 3, both=20, neither=29)   # 60 pairs, gain 5/60, not cleared
        out = self.run_kind("built", pairs)
        self.assertFalse(out["kept"])
        diff, lo, hi = newcombe_paired(20, 8, 3, 29)
        self.assertAlmostEqual(out["gain"], diff, places=6)
        self.assertAlmostEqual(out["gain"], 5 / 60, places=6)
        self.assertAlmostEqual(out["ci"][0], lo, delta=0.02)
        self.assertAlmostEqual(out["ci"][1], hi, delta=0.02)
        rec = out["record"]
        self.assertIn("not shown", rec)
        self.assertIn("95%", rec)
        self.assertNotRegex(rec.lower(), r"no effect|does not help|doesn't help")

    def test_newcombe_range_for_other_tables(self):
        for tbl in ((30, 12, 4, 14), (10, 5, 5, 40), (25, 0, 0, 35), (5, 10, 0, 45)):
            a, b, c, d = tbl
            pairs = pairs_of(b, c, both=a, neither=d)
            out = self.run_kind("plans", pairs)
            diff, lo, hi = newcombe_paired(a, b, c, d)
            self.assertAlmostEqual(out["gain"], diff, places=6)
            self.assertAlmostEqual(out["ci"][0], lo, delta=0.02, msg=str(tbl))
            self.assertAlmostEqual(out["ci"][1], hi, delta=0.02, msg=str(tbl))

    def test_no_change_helps_is_an_accepted_result(self):
        out = self.run_kind("built", pairs_of(4, 6, both=30, neither=20))
        self.assertFalse(out["kept"])
        self.assertEqual(out["status"], "not shown")
        self.assertLess(out["gain"], 0)

    def test_fewer_than_ten_pairs_is_too_few_pieces_to_test(self):
        out = self.run_kind("built", pairs_of(9, 0))
        self.assertEqual(out["status"], "too few pieces to test")
        self.assertFalse(out["kept"])
        ten = self.run_kind("built", pairs_of(10, 0))
        self.assertTrue(ten["kept"])

    def test_the_record_for_a_kept_change_says_kept(self):
        out = self.run_kind("built", pairs_of(16, 2, both=20, neither=22))
        self.assertTrue(out["kept"])
        self.assertIn("kept", out["record"].lower())
        self.assertNotIn("not shown", out["record"])


class TestAC7Research(AnalyseBase):
    def memo(self, i, change, control, judge):
        return {"piece": "m%d" % i, "doer_model": "claude-sonnet-5-5", "judge_model": "claude-fable-5-1",
                "change_check_pass": change, "control_check_pass": control, "memo_judge_pass": judge}

    def table(self, rows):
        """rows: (change_check_pass, control_check_pass, memo_judge_pass, count)"""
        out, i = [], 0
        for ch, co, j, n in rows:
            for _ in range(n):
                out.append(self.memo(i, ch, co, j))
                i += 1
        return out

    def test_a_version_passes_only_where_the_held_back_check_also_passes_the_memo(self):
        # Raw verdicts would give n10 = 12 against n01 = 0 (kept); counted, the judge fails 8 of those 12.
        rows = [(True, False, True, 4), (True, False, False, 8), (False, False, True, 20), (True, True, True, 28)]
        out = self.run_kind("research", self.table(rows))
        self.assertEqual((out["n10"], out["n01"]), (4, 0))
        self.assertFalse(out["kept"])

    def test_false_pass_guard_allows_the_unchanged_checks_false_passes_plus_one(self):
        # a clearing result (n10 = 12, n01 = 0) with C3's false passes at control's + 1, then + 2
        base = [(True, False, True, 12), (True, True, True, 30), (False, False, True, 18)]
        ok = self.table(base + [(True, False, False, 1)])      # change false passes 1, control 0 -> +1
        out = self.run_kind("research", ok)
        self.assertTrue(out["false_pass_guard"], out)
        self.assertTrue(out["kept"])
        bad = self.table(base + [(True, False, False, 2)])     # +2
        out = self.run_kind("research", bad)
        self.assertFalse(out["false_pass_guard"])
        self.assertFalse(out["kept"], "a clearing test is not enough when the guard fails")
        both = self.table(base + [(True, True, False, 3), (True, False, False, 1)])   # 4 vs 3 -> +1 again
        self.assertTrue(self.run_kind("research", both)["false_pass_guard"])

    def test_the_guard_applies_to_research_only(self):
        out = self.run_kind("built", pairs_of(12, 0, both=20, neither=28))
        self.assertIn(out.get("false_pass_guard"), (None, True))
        self.assertTrue(out["kept"])
