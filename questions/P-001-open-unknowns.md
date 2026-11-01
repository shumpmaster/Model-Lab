# Ruling needed: may three open questions stay open into Design?

Milestone: Discovery-8

WHY: Before the brief goes to the Design gate, every load-bearing unknown must either be answered with evidence or accepted by you as open, with the test that will close it and what happens if it fails. Three cannot be answered in Discovery. Accepting them is yours to decide. If you do not decide, the brief cannot go to the Design gate.

The three, each with its test and fallback (from the brief's section 7):
  1. **Can past tasks be replayed faithfully**, so a change can be tested on the same tasks it would have faced? Test: replay a few past tasks in Design, before the test is fixed. If not: compare new work with and without a change over the same period, which needs more pieces of work.
  2. **Do the checks judge consistently and fairly enough** to be the yardstick? Test: judge a sample twice, and use checkers from a different family of AI models where available, in Design. If not: a held-back set of checks the work never sees, and a sample you look at yourself, decide; the record says how far the checks can be trusted.
  3. **Does any change give a gain the test can see?** Test: the test itself, in Build. If not: "no change helps", the result you accepted in advance.

OPTIONS:
  A. **Accept all three as open into Design**, with the tests and fallbacks above. *Gain:* the brief can go to the Design gate now; each question is answered where it can be. *Cost:* if replay fails (1), the test becomes slower and needs more work to show anything. *Reversible:* yes.
  B. **Accept 2 and 3, but answer 1 before the Design gate**, by replaying a few past tasks now. *Gain:* the Design gate is ruled knowing whether the planned test can run. *Cost:* the gate waits for that check, which uses some of the 100 test runs you allowed (the brief plans no more than 40 for this check and the consistency check together). *Reversible:* yes.

RECOMMENDATION: A, with medium confidence: each question has a test and a fallback, and testing replay in Design costs the same runs as testing it now, without holding up the gate. What would change it: if you want the Design gate ruled only once the test's method is known to work, B.
WHO HAS CHECKED IT: the Critic, on a different AI model from the writer (record: reviews/P-001-open-unknowns/critic.md).
RISK CLASS: R2 (a planning ruling; nothing irreversible)   REVERSIBILITY: reversible   BLAST RADIUS: when the brief goes to the Design gate, and how the test is designed
DEFAULT: none — accepting an unknown as open needs the owner's recorded ruling   TIMEOUT: none

## Context
- An unknown may stay open into Define only when the project document names the test that closes it and the fallback if it fails, and the owner's ruling accepting it is recorded (source: Personal-Org-Operating-Model OPERATING_MODEL.md §4, definition of ready item 7)
- The three unknowns, their tests and fallbacks (source: docs/PROJECT.md section 7, U2, U3 and U4)
- The owner allowed about 100 test runs through Discovery and Design (source: decisions/questions/P-001-test-budget.md)
- The owner accepted "no change helps" as a result (source: decisions/questions/P-001-no-change-result.md)
