"""AC8 [trace: V1 -> AC8] -- when the test is running, the owner receives, at every 20 runs of each side
and 16 weeks after each kind opens, the runs and tokens used on each side, the pairs collected and left
out, the power at the pairs collected and the weeks to the target at the pace so far, and no outcome; the
owner's "go on" or "stop" is recorded; no side of a kind starts more runs than its planned runs plus its
share of the reserve, so no kind starts more than its planned runs plus reserve.

Interface named (e003_support.py): src/E-003/counts.py
  cap --kind K --side work|judging|total [--pairs N]                   -> {"cap": n}
  may-start --kind K --side work|judging --started N [--ruling-file F]  -> {"allowed": bool}
  due --kind K --side S --runs R --run-cards-sent J --weeks W --review-cards-sent V -> {"due": bool,"reason"}
  card --kind K --work FILE --judging FILE --weeks W [--target 60]    -> {"text", "work":{"runs","tokens"},
        "judging":{"runs","tokens"}, "pairs_collected", "pairs_left_out", "power":{one-way,middle,independent},
        "weeks_to_target"}
  record-ruling --file F --kind K --ruling "go on"|"stop" --date D
The caps are the spec's: with 60 pairs, plans and built work 133 work-side and 132 judging-side runs
(planned 120 + 13 and 120 + 12), research 133 and 66; with the sheet's run, 266 and 200 in all.  Power is
experiments/E-003/sizing.py's, at the pairs collected, for the three assumptions, each kind from its own
starting figure.  FAILS until src/E-003/counts.py is built.
"""
import json
import math
import os
import re

from e003_support import Base, sizing

COUNTS = ["counts: S-001-built-1", "index-commit: " + "0123456789abcdef0123456789abcdef01234567", "judged: 12",
          "runs: 30", "reserve-used: 2", "tokens: 4800000", "left-out: L3,L9", "k1-canary: unseen", "k2: pass",
          "k3: pass", "k4: pass", "k5: pass", "k7: untested"]


class TestAC8Caps(Base):
    def cap(self, kind, side, pairs=None):
        args = ["cap", "--kind", kind, "--side", side]
        if pairs:
            args += ["--pairs", str(pairs)]
        return self.decide("counts.py", *args)["cap"]

    def test_caps_at_60_pairs(self):
        for kind in ("built", "plans"):
            self.assertEqual((self.cap(kind, "work"), self.cap(kind, "judging"), self.cap(kind, "total")), (133, 132, 266))
        self.assertEqual((self.cap("research", "work"), self.cap("research", "judging"), self.cap("research", "total")),
                         (133, 66, 200))

    def test_caps_at_the_other_sizes_in_the_spec_table(self):
        self.assertEqual((self.cap("built", "work", 40), self.cap("built", "judging", 40), self.cap("built", "total", 40)),
                         (89, 88, 178))
        self.assertEqual((self.cap("built", "work", 100), self.cap("built", "judging", 100)), (221, 220))
        self.assertEqual((self.cap("research", "work", 40), self.cap("research", "judging", 40)), (89, 44))
        self.assertEqual((self.cap("research", "work", 100), self.cap("research", "judging", 100)), (221, 110))

    def test_no_kind_starts_more_than_planned_plus_reserve(self):
        for kind in ("built", "plans", "research"):
            self.assertEqual(self.cap(kind, "work") + self.cap(kind, "judging") + 1, self.cap(kind, "total"))

    def may(self, kind, side, started, **extra):
        args = ["may-start", "--kind", kind, "--side", side, "--started", str(started)]
        for k, v in extra.items():
            args += ["--" + k.replace("_", "-"), v]
        return self.decide("counts.py", *args)["allowed"]

    def test_a_side_starts_runs_up_to_its_cap_and_no_more(self):
        self.assertTrue(self.may("built", "work", 132))
        self.assertFalse(self.may("built", "work", 133))
        self.assertTrue(self.may("built", "judging", 131))
        self.assertFalse(self.may("built", "judging", 132))
        self.assertTrue(self.may("research", "judging", 65))
        self.assertFalse(self.may("research", "judging", 66))
        self.assertFalse(self.may("plans", "work", 500))

    def test_a_side_cannot_borrow_the_other_sides_unused_share(self):
        self.assertFalse(self.may("built", "work", 133), "the judging side may be far under its cap")

    def test_a_stop_ruling_stops_further_runs(self):
        f = self.write("rulings.txt", "")
        self.decide("counts.py", "record-ruling", "--file", f, "--kind", "built", "--ruling", "stop",
                    "--date", "2026-12-01")
        self.assertFalse(self.may("built", "work", 10, ruling_file=f))
        self.decide("counts.py", "record-ruling", "--file", f, "--kind", "plans", "--ruling", "go on",
                    "--date", "2026-12-01")
        self.assertTrue(self.may("plans", "work", 10, ruling_file=f))


class TestAC8Due(Base):
    def due(self, **kw):
        base = {"kind": "built", "side": "work", "runs": 0, "run_cards_sent": 0, "weeks": 0, "review_cards_sent": 0}
        base.update(kw)
        args = ["due"]
        for k, v in base.items():
            args += ["--" + k.replace("_", "-"), str(v)]
        return self.decide("counts.py", *args)

    def test_every_20_runs_of_each_side(self):
        for side in ("work", "judging"):
            self.assertFalse(self.due(side=side, runs=19)["due"])
            self.assertTrue(self.due(side=side, runs=20)["due"])
            self.assertFalse(self.due(side=side, runs=39, run_cards_sent=1)["due"])
            self.assertTrue(self.due(side=side, runs=40, run_cards_sent=1)["due"])
            self.assertFalse(self.due(side=side, runs=40, run_cards_sent=2)["due"])

    def test_16_weeks_after_the_kind_opens_and_every_16_weeks_after(self):
        self.assertFalse(self.due(weeks=15)["due"])
        self.assertTrue(self.due(weeks=16)["due"])
        self.assertFalse(self.due(weeks=16, review_cards_sent=1)["due"])
        self.assertTrue(self.due(weeks=32, review_cards_sent=1)["due"])


class TestAC8Card(Base):
    def card(self, kind="built", weeks=10, collected=15, left=3, work_extra=None):
        work = {"runs": 62, "tokens": 11_200_000, "pairs_collected": collected, "pairs_left_out": left}
        work.update(work_extra or {})
        w = self.write("work.json", json.dumps(work))
        j = self.write("judging.txt", "\n".join(COUNTS) + "\n")
        return self.decide("counts.py", "card", "--kind", kind, "--work", w, "--judging", j, "--weeks", str(weeks))

    def test_the_card_carries_runs_and_tokens_of_each_side_and_the_pairs(self):
        out = self.card()
        self.assertEqual((out["work"]["runs"], out["work"]["tokens"]), (62, 11_200_000))
        self.assertEqual((out["judging"]["runs"], out["judging"]["tokens"]), (30, 4_800_000))
        self.assertEqual((out["pairs_collected"], out["pairs_left_out"]), (15, 3))
        text = out["text"].replace(",", "")
        for n in ("62", "11200000", "30", "4800000", "15", "3"):
            self.assertRegex(text, r"(?<!\d)%s(?!\d)" % n)

    def test_power_at_the_pairs_collected_is_sizing_pys_for_the_three_assumptions(self):
        s = sizing()
        for kind, key in (("built", "built work"), ("plans", "plans"), ("research", "research")):
            for n in (15, 30, 45):
                out = self.card(kind=kind, collected=n)
                for name in s.NAMES:
                    want = s.power(n, *s.cells(s.START[key], name)[1:3])
                    self.assertAlmostEqual(out["power"][name], want, places=3, msg="%s n=%d %s" % (kind, n, name))

    def test_weeks_to_target_at_the_pace_so_far(self):
        out = self.card(weeks=10, collected=15)          # 1.5 pairs a week; 45 to go
        self.assertAlmostEqual(out["weeks_to_target"], 30.0, delta=0.5)
        out = self.card(weeks=8, collected=60)
        self.assertEqual(out["weeks_to_target"], 0)
        self.assertIsNone(self.card(weeks=8, collected=0)["weeks_to_target"], "no pace yet")

    def test_the_card_shows_no_outcome(self):
        out = self.card(work_extra={"n10": 7, "n01": 1, "gain": 0.21, "outcomes": ["PASS", "FAIL"],
                                    "pair_results": [{"change": "PASS", "control": "FAIL"}]})
        text = out["text"]
        self.assertIsNone(re.search(r"(?i)\b(n10|n01|gain|pass|fail|verdict|kept|helps|better|worse)\b", text), text)
        blob = json.dumps(out).lower()
        for word in ("n10", "n01", '"gain"', "verdict", "outcomes", "pair_results"):
            self.assertNotIn(word, blob)

    def test_the_owners_ruling_is_recorded(self):
        f = self.write("rulings.txt", "")
        p = self.run_script("counts.py", "record-ruling", "--file", f, "--kind", "built", "--ruling", "go on",
                            "--date", "2026-12-01")
        self.assertEqual(p.returncode, 0, p.stderr)
        text = open(f, encoding="utf-8").read()
        for needle in ("built", "go on", "2026-12-01"):
            self.assertIn(needle, text)
        q = self.run_script("counts.py", "record-ruling", "--file", f, "--kind", "built", "--ruling", "maybe",
                            "--date", "2026-12-02")
        self.assertEqual(q.returncode, 1, "only 'go on' or 'stop' is a ruling")
        self.assertNotIn("maybe", open(f, encoding="utf-8").read())
