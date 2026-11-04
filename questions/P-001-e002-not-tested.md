# Ruling needed: record the judging-consistency check as "not tested" without running it?

Milestone: M2, Design-3

WHY: The judging-consistency check (E-002) judges only replays that passed the replay check. Under the Reviewer's reading of the replay check's frozen rules, three replays qualify, and E-002 needs at least four; with three, its own rules make the result "not tested" whatever the judges say, and the brief's fallback applies (held-back checks and a sample you look at decide, and the record states how far the checks can be trusted). Running it would spend up to 20 test runs, several million tokens on the replay check's evidence, to reach a result already fixed. Not running a registered check is a change to the plan, so it is yours to decide. If you do not decide, nothing runs.
OPTIONS:
  A. record E-002 as "not tested" without running it — the fallback applies to the judges; the 20 runs stay unspent. *Gain:* no runs or tokens spent on a fixed result. *Cost:* no measure of judge consistency now; it is measured later from the held-back checks and your sample. *Reversible:* yes; a new registration can test it later.
  B. run E-002 as registered — up to 20 runs; its consistency result is "not tested" by its own rule, but its self-preference and first-time-pass readings are recorded. *Gain:* those readings, for what they are worth. *Cost:* up to 20 runs and their tokens. *Reversible:* the runs used cannot be taken back.
  C. amend the replay check's rule on reads outside the copy and re-register E-002 — the Reviewer found two replays failed only on reading their own saved command output; a new registration could allow that, giving five replays to judge. *Gain:* the consistency question gets tested. *Cost:* a new registration, its review and up to 20 runs; a rule changed after seeing the result must be a new registration, never a reinterpretation. *Reversible:* yes until it runs.
RECOMMENDATION: A, with medium confidence (the Chief of Staff's judgement): the result is fixed in advance, and the fallback already exists for this case. What would change it: if you want the judges measured before the fair test is designed, C.
WHO HAS CHECKED IT: not yet; the Critic reads it cold before it is put.
RISK CLASS: R0 (computed from the paths it touches)   REVERSIBILITY: costly   BLAST RADIUS: the Design checks and the fair test's judging
DEFAULT: none — dropping registered work is the owner's ruling   TIMEOUT: none

## Context
- The Reviewer's analysis of the replay check: every kind goes to the fallback, and three replays qualify for E-002, which needs four (source: reviews/E-001/reviewer.md)
- E-002's pass gate and its "not tested" rule (source: experiments/E-002.md)
- The owner accepted U3 as open into Design and Build with its fallback (source: decisions/questions/P-001-open-unknowns.md)
- The replay check's 14 runs used about 2.5 million tokens (source: src/E-001/RESULT.md)
