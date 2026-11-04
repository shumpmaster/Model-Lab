# Ruling needed: record the judging-consistency check as "not tested" without running it?

Milestone: M2, Design-3

WHY: Two checks come before the fair test. The first (the replay check) asked whether past tasks can be re-run faithfully; the Reviewer found they cannot, under its rules. The second (the judging-consistency check) asks whether the AI judges agree with themselves and each other, using only replays that passed the first. Three qualify and it needs four, so by its own rule its outcome is "not tested" whatever the judges say, and its fallback applies: checks the work never sees, plus a sample you look at yourself, decide. Skipping a registered check is yours to decide; if you do not, nothing runs.
OPTIONS:
  A. record the judging check as "not tested" without running it — the fallback applies to the judges. *Gain:* no runs or tokens spent on an outcome already fixed. *Cost:* no measure of judge consistency now; it comes later from the held-back checks and your sample. *Reversible:* yes; a new registration can test it later.
  B. run it as registered — up to 20 runs; the whole check's outcome is "not tested" by its own rule. It would report, as readings only that change nothing in the fair test, how the two judges differ on the three replays and how often the test judge agrees with itself. *Gain:* those readings. *Cost:* up to 20 runs, an estimated 3 to 4 million tokens (the replay check's six judge runs cost 143,000 to 194,000 each); the replays' copies must be rebuilt first, and one of the three (S-014) is not comparable with its original. *Reversible:* the runs used cannot be taken back.
  C. amend the replay check's rule on reads outside the copy and re-register the judging check — the Reviewer found two replays failed only on reading their own saved command output; allowing that would give five replays to judge. This reopens the replay check's result through a new registration, never by reinterpreting the old one. *Gain:* the consistency question gets a chance to be tested (it can still come out "not tested" if too few pieces pass). *Cost:* a new registration and its review, then up to 20 runs (about 3 to 4 million tokens). *Reversible:* yes until it runs.
  All three stay within the 40 runs set for the two checks (14 used).
RECOMMENDATION: A, with medium confidence (the Chief of Staff's judgement): the result is fixed in advance, and the fallback already exists for this case. What would change it: if you want the judges measured before the fair test is designed, C.
WHO HAS CHECKED IT: the Critic, on a different AI model from the writer (record: reviews/P-001-e002-not-tested/critic.md, PASS).
RISK CLASS: R0 (computed from the paths it touches)   REVERSIBILITY: costly   BLAST RADIUS: the Design checks and the fair test's judging
DEFAULT: none — dropping registered work is the owner's ruling   TIMEOUT: none

## Context
- The Reviewer's analysis of the replay check: every kind goes to the fallback, and three replays qualify for E-002, which needs four (source: reviews/E-001/reviewer.md)
- E-002's pass gate and its "not tested" rule (source: experiments/E-002.md)
- The owner accepted U3 as open into Design and Build with its fallback (source: decisions/questions/P-001-open-unknowns.md)
- The replay check's 14 runs used about 2.5 million tokens (source: src/E-001/RESULT.md)
