# Ruling needed: may three open questions stay open into Design and Build?

Milestone: Discovery-8

WHY: Before the brief goes to the Design gate, every unknown the plan depends on must either be answered with evidence or accepted by you as open, with the test that will close it and what happens if it fails. Three cannot be answered in Discovery. Accepting them is yours to decide. If you do not decide, the brief cannot go to the Design gate.

The three, each with its test and fallback (from the brief's section 7):
  1. **Can past tasks be replayed faithfully**, so a change can be tested on the same tasks it would have faced? Test: replay a few past tasks in Design, before the test is fixed. If not: compare new work with and without a change over the same period, which needs more pieces of work.
  2. **Do the checks judge consistently and fairly enough** to be the yardstick? Test: repeat judgements on a sample, and use checkers from a different family of AI models where available, in Design. If not: a held-back set of checks the work never sees, and a sample you look at yourself, decide; the record says how far the checks can be trusted.
  3. **Does any change give a gain the test can see?** Test: the test itself, in Build. If not: the result is that no change helped; you accepted in advance that changing the instructions may not help.

OPTIONS:
  Either way, the replay check uses some of the 100 test runs you allowed through Design (the brief plans no more than 40 for the replay and consistency checks together); the options differ only in when it runs and what you know at the Design gate.
  A. **Accept all three as open into Design and Build**, with the tests and fallbacks above; the replay check runs in Design. *Gain:* the brief can go to the Design gate now. *Cost:* you rule the Design gate without knowing whether the planned test can run on past tasks; if it cannot, Design switches to the slower fallback. *Reversible:* yes.
  B. **Accept 2 and 3, but answer 1 before the Design gate**, by running the replay check now. *Gain:* you rule the Design gate knowing whether the planned test can run. *Cost:* the Design gate waits until the check is done. *Reversible:* yes.

RECOMMENDATION: A, with medium confidence (the Chief of Staff's judgement): each question has a test and a fallback written down, and since the check uses the same runs either way, running it in Design avoids holding up the gate. What would change it: if you want the Design gate ruled only once the test's method is known to work, B.
WHO HAS CHECKED IT: the Critic, on a different AI model from the writer (record: reviews/P-001-open-unknowns/critic.md).
RISK CLASS: R2 (a planning ruling; nothing irreversible)   REVERSIBILITY: reversible   BLAST RADIUS: when the brief goes to the Design gate, and how the test is designed
DEFAULT: none — accepting an unknown as open needs your own recorded ruling, and a default is never read as your ruling   TIMEOUT: none

## Context
- An unknown may stay open into Design (the model calls it Define) only when the project document names the test that closes it and the fallback if it fails, and the owner's ruling accepting it is recorded (source: Personal-Org-Operating-Model OPERATING_MODEL.md §4, definition of ready item 7)
- The three unknowns, their tests and fallbacks (source: docs/PROJECT.md section 7, U2, U3 and U4)
- The owner allowed about 100 test runs through Discovery and Design, with checkpoints on tokens used, and the project goes back to the owner if they run out before the fair test is ready (source: decisions/questions/P-001-test-budget.md; docs/PROJECT.md section 6)
- The owner accepted that changing the instructions may not help (source: decisions/questions/P-001-no-change-result.md)
