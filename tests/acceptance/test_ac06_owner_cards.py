"""AC6 [trace: V1 -> AC6] -- when every pair of a kind is judged, the owner receives 8 cards, each one
output without arm labels, showing the judge's verdict with the numbers of the failed tests and their
cited lines, drawn by the pre-written seed from the three groups E-003 names; more are drawn, up to 12,
until 6 have a yes or no; the owner's answers replace the judge's verdicts, the pairs are scored again,
and the cards answered and the disagreements are recorded.

Interface named (e003_support.py): src/E-003/cards.py draw --pairs FILE --seed N --set SETID [--answers
FILE] -> {"cards":[{"label","group","order","verdict","failed","open"}...], "answered": n,
"too_few": bool}; cards.py rescore --pairs FILE --answers FILE -> {"classes":{piece: n10|n01|concordant},
"n10","n01","answered","disagreements","by_group"}.  The draw is compared with the reference in
e003_support.py (Python's random.Random(seed): sample(G1,k1), sample(G2,k2), sample(G3,k3), then further
cards one at a time with choice in the order G1, G3, G2).
GAPS: how a shortfall is added to the three sample sizes, and "choice from what is left, in the order
G1, G3, G2", are read as e003_support.ref_allocation / ref_sequence say; the pairs-file shape is ours.
FAILS until the Builder builds src/E-003/cards.py.
"""
import json
import re

from e003_support import (Base, make_pairs, ref_groups, ref_sequence, ref_allocation)

SET = "S-001-built-1"
# 6 deciding pairs (differ), 4 both-pass, 4 both-fail
SPEC = ([("PASS", "FAIL")] * 3 + [("FAIL", "PASS")] * 3 + [("PASS", "PASS")] * 4 + [("FAIL", "FAIL")] * 4)


class TestAC6(Base):
    def draw(self, pairs, seed=20261104, answers=None):
        pf = self.write("pairs.json", json.dumps(pairs))
        args = ["draw", "--pairs", pf, "--seed", str(seed), "--set", SET]
        if answers is not None:
            args += ["--answers", self.write("answers.json", json.dumps(answers))]
        return self.decide("cards.py", *args)

    def test_eight_cards_four_two_two_from_the_three_groups_by_the_seed(self):
        pairs = make_pairs(SPEC)
        out = self.draw(pairs)
        cards = out["cards"]
        self.assertEqual(len(cards), 8)
        self.assertEqual([(c["label"], c["group"]) for c in cards], ref_sequence(pairs, 20261104))
        self.assertEqual([c["group"] for c in cards].count("G1"), 4)
        self.assertEqual([c["group"] for c in cards].count("G2"), 2)
        self.assertEqual([c["group"] for c in cards].count("G3"), 2)
        self.assertEqual([c["order"] for c in cards], list(range(1, 9)))

    def test_the_same_seed_gives_the_same_draw_and_another_seed_a_different_one(self):
        pairs = make_pairs(SPEC)
        a = [c["label"] for c in self.draw(pairs, 7)["cards"]]
        b = [c["label"] for c in self.draw(pairs, 7)["cards"]]
        c = [c["label"] for c in self.draw(pairs, 8)["cards"]]
        self.assertEqual(a, b)
        self.assertEqual(c, [x for x, _ in ref_sequence(pairs, 8)])

    def test_group_membership_follows_e003(self):
        pairs = make_pairs(SPEC)
        g1, g2, g3 = ref_groups(pairs)
        self.assertEqual((len(g1), len(g2), len(g3)), (12, 8, 8))
        groups = {c["label"]: c["group"] for c in self.draw(pairs, 3)["cards"]}
        for lab, g in groups.items():
            self.assertIn(lab, {"G1": g1, "G2": g2, "G3": g3}[g])

    def test_each_card_is_one_output_with_the_verdict_and_failed_lines_and_no_arm_label(self):
        pairs = make_pairs(SPEC)
        v = {l: x for p in pairs for l, x in p["verdicts"].items()}
        f = {l: x for p in pairs for l, x in p["failed"].items()}
        for c in self.draw(pairs)["cards"]:
            self.assertEqual(c["verdict"], v[c["label"]])
            self.assertEqual(c["failed"], f[c["label"]])
            self.assertIn("holdouts/%s.md" % SET, json.dumps(c), "names the sheets repository's sheet to open")
            blob = json.dumps(c).lower()
            for word in ("control", "change", "arm", "piece", '"p0'):
                self.assertNotIn(word, blob, "a card must not reveal the arm or the pair: " + word)
            self.assertFalse(re.search(r"\b[ck]\d\d\b", c["verdict"] + c["failed"]))

    def test_group_too_small_takes_its_shortfall_from_g1_then_g3_then_g2(self):
        # no both-pass pairs: G2 is empty; G1 and G3 are large
        pairs = make_pairs([("PASS", "FAIL")] * 6 + [("FAIL", "FAIL")] * 6)
        self.assertEqual(ref_allocation(*ref_groups(pairs)), [6, 0, 2])
        out = self.draw(pairs)
        self.assertEqual([(c["label"], c["group"]) for c in out["cards"]], ref_sequence(pairs, 20261104))
        # only one deciding pair (G1 = 2 outputs): the shortfall goes to G3
        pairs = make_pairs([("PASS", "FAIL")] + [("PASS", "PASS")] * 4 + [("FAIL", "FAIL")] * 4)
        self.assertEqual(ref_allocation(*ref_groups(pairs)), [2, 2, 4])
        out = self.draw(pairs)
        self.assertEqual([(c["label"], c["group"]) for c in out["cards"]], ref_sequence(pairs, 20261104))

    def test_built_outputs_whose_locked_checks_failed_are_never_drawn(self):
        pairs = make_pairs(SPEC, locked=("c00", "k00", "c03", "k03", "c07", "k07", "c08", "c12"))
        g = ref_groups(pairs)
        for bad in ("c00", "k00", "c03", "c07", "c08", "c12"):
            for grp in g:
                self.assertNotIn(bad, grp)
        for seed in range(1, 12):
            labels = {c["label"] for c in self.draw(pairs, seed, answers={})["cards"]}
            self.assertFalse(labels & {"c00", "k00", "c03", "k03", "c07", "k07", "c08", "c12"})

    def test_more_cards_are_drawn_one_at_a_time_until_six_have_a_yes_or_no(self):
        pairs = make_pairs(SPEC)
        seq = ref_sequence(pairs, 5)[:8]
        # three "can't tell" among the first eight, then yes for everything after
        ans = {lab: "yes" for p in pairs for lab in p["verdicts"]}
        for lab, _ in seq[:3]:
            ans[lab] = "can't tell"
        full = ref_sequence(pairs, 5, ans)
        self.assertEqual(len(full), 9)
        out = self.draw(pairs, 5, answers=ans)
        self.assertEqual([(c["label"], c["group"]) for c in out["cards"]], full)
        self.assertEqual(out["answered"], 6)
        self.assertFalse(out["too_few"])

    def test_at_most_twelve_cards_and_too_few_answered_after_twelve(self):
        pairs = make_pairs(SPEC)
        everything = {lab: "can't tell" for p in pairs for lab in p["verdicts"]}
        out = self.draw(pairs, 5, answers=everything)
        self.assertEqual(len(out["cards"]), 12)
        self.assertEqual(out["answered"], 0)
        self.assertTrue(out["too_few"])
        self.assertEqual([(c["label"], c["group"]) for c in out["cards"]], ref_sequence(pairs, 5, everything))

    def test_eight_answers_stop_at_eight(self):
        pairs = make_pairs(SPEC)
        ans = {lab: "no" for p in pairs for lab in p["verdicts"]}
        self.assertEqual(len(self.draw(pairs, 5, answers=ans)["cards"]), 8)


class TestAC6Rescore(Base):
    def rescore(self, pairs, answers):
        return self.decide("cards.py", "rescore", "--pairs", self.write("p.json", json.dumps(pairs)),
                           "--answers", self.write("a.json", json.dumps(answers)))

    def test_the_owners_answer_replaces_the_judges_verdict_and_the_pair_class_is_worked_out_again(self):
        pairs = make_pairs([("PASS", "FAIL"), ("FAIL", "PASS"), ("PASS", "PASS"), ("FAIL", "FAIL")])
        base = self.rescore(pairs, {})
        self.assertEqual((base["n10"], base["n01"]), (1, 1))
        self.assertEqual(base["classes"], {"p00": "n10", "p01": "n01", "p02": "concordant", "p03": "concordant"})
        # yes = FAIL, no = PASS: the owner fails the change arm of p00 (so p00 becomes concordant) and
        # passes the control arm of p01 (so p01 becomes concordant)
        out = self.rescore(pairs, {"c00": "yes", "k01": "no"})
        self.assertEqual(out["classes"]["p00"], "concordant")
        self.assertEqual(out["classes"]["p01"], "concordant")
        self.assertEqual((out["n10"], out["n01"]), (0, 0))

    def test_can_not_tell_and_undrawn_outputs_keep_the_judges_verdict(self):
        pairs = make_pairs([("PASS", "FAIL")])
        out = self.rescore(pairs, {"c00": "can't tell"})
        self.assertEqual(out["classes"]["p00"], "n10")
        self.assertEqual(out["answered"], 0)

    def test_a_no_on_an_output_in_a_pair_both_arms_passed_leaves_the_pair_concordant(self):
        pairs = make_pairs([("PASS", "PASS")])
        self.assertEqual(self.rescore(pairs, {"c00": "no"})["classes"]["p00"], "concordant")

    def test_answered_and_disagreements_are_recorded(self):
        pairs = make_pairs([("PASS", "FAIL"), ("FAIL", "FAIL"), ("PASS", "PASS")])
        # c00 PASS: owner no (agrees); k00 FAIL: owner no (disagrees); c01 FAIL: owner yes (agrees);
        # c02 PASS: owner can't tell
        out = self.rescore(pairs, {"c00": "no", "k00": "no", "c01": "yes", "c02": "can't tell"})
        self.assertEqual(out["answered"], 3)
        self.assertEqual(out["disagreements"], 1)
