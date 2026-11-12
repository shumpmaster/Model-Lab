# Ruling needed: how to judge a piece whose only independent check was of another kind

Milestone: M8

The counting rules judge each piece by the first round of its first independent check: a plan by its plan review, built work by its build review. A few past pieces have only a check of the other kind. Service-Desk #148, a plan, had only build-style review rounds, the first of which failed. Model-Lab #93, a plan, had no plan review, and its only review came after it merged. Today the rules call such a piece "undecided" and list it. In a trial the kind is fixed when the work is handed out, so this affects only the hand check and the starting figure. Nothing is frozen, so nothing here is irreversible.

WHY: the starting figure for how often first checks pass needs a rule for these pieces; the plan does not change until you choose (specs/S-002.md, open question 12).
OPTIONS:
  A. Strict: only a check of the piece's own kind counts; the rest are undecided and listed, as the rules read today.
     Gain: every counted result answers the same question, the first independent check you ruled on (T25).
     Cost: a few past pieces drop out of the starting figure.
  B. Fallback: when no check of the piece's kind exists, its only independent check before merging counts. Service-Desk #148 becomes a FAIL; Model-Lab #93 stays undecided.
     Gain: fewer pieces left out.
     Cost: some counted results then test something other than the piece's own kind of check.
RECOMMENDATION: A, with fair confidence (the Definer's and the Chief of Staff's judgement): a check of another kind tests something else, and the list keeps each such piece in view. What would change it: the list growing large enough to bias the starting figure (then B).
WHO HAS CHECKED IT: the Critic's re-checks of the corrected rules (reviews/Q-018-rules/_critic-verbatim.md, section 3(b); reviews/Q-018-rules/_critic-r2-verbatim.md).
RISK CLASS: R0, a question only   REVERSIBILITY: reversible   BLAST RADIUS: the hand check's first-check results and the starting figure; not trials
DEFAULT: none: the counting rules change only on your answer (specs/S-002.md, open question 12)   TIMEOUT: none

## Context
- Service-Desk #148's only check records are the Reviewer's rounds on the design reviewer's setup, classed as build reviews by their file names (source: reviews/Q-018-rules/_critic-r2-verbatim.md, section 1)
- Model-Lab #93 has no plan review; its build review was made after its merge (source: reviews/Q-018-rules/_critic-verbatim.md, section 1)
- You ruled that a trial's work holds up when its pieces do no worse at passing their first independent check (source: docs/gates/P-002/trial-terms.md, T25)
