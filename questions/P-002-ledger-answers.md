# Ruling needed: whether Personal-Org-Operating-Model's ledger entries that quote you count as your answers

Milestone: M8

Personal-Org-Operating-Model records your rulings in its ledger, each entry quoting your words. Until 11 October that ledger is the only record of most of them. After that, it repeats answers that the repository's answer files also hold. The counting rules don't read the ledger today. In the sample, such entries fall while two pieces were under way (#20 and #22) that have no other touch, so your choice decides whether those two pieces count as needing you. Nothing is frozen, so nothing here is irreversible.

WHY: the starting count of how often pieces need you misses rulings that this repository kept only in its ledger; the plan does not change until you choose (specs/S-002.md, open question 15).
OPTIONS:
  A. Leave ledger entries out, and list them, as the rules read today.
     Gain: no new record type to read.
     Cost: it misses your rulings from before 11 October, which that repository kept only in its ledger.
  B. Count an entry that quotes you as a decision record of its own, timed by the commit that adds it. Skip it when an answer record already counted on the piece holds the same words, so that one answer counts once.
     Gain: it catches the early rulings without counting any answer twice.
     Cost: one more record type, and a same-words check.
  C. Count every entry that quotes you, even when an answer file holds the same answer.
     Gain: simple.
     Cost: after 11 October it counts one answer twice.
RECOMMENDATION: B, with fair confidence (the Definer's and the Chief of Staff's judgement): before 11 October the ledger is where that repository kept your rulings, so A misses real touches, and C double-counts after. What would change it: wanting the count to read only question and answer records (then A).
WHO HAS CHECKED IT: the Critic's step 5 on the re-coding raised it (reviews/Q-018-recode/_critic-verbatim.md, finding 2 and open questions); the Definer wrote the options (docs/briefs/300-definer.md).
RISK CLASS: R0, a question only   REVERSIBILITY: reversible   BLAST RADIUS: the hand check's touch count and the starting figure, in Personal-Org-Operating-Model
DEFAULT: none: the counting rules change only on your answer (specs/S-002.md, open question 15)   TIMEOUT: none

## Context
- Personal-Org-Operating-Model's ledger entries quote the owner in a `decided_by:` line; its answer files began on 2026-10-11 (source: specs/S-002.md, open question 15; Personal-Org-Operating-Model reviews/S-022/_owner-answers-2026-10.md)
- Inside the sample, such entries were added in the windows of #20, #22, #25, #27, #30, #35, #49 and #50 (source: specs/S-002.md, open question 15)
- Personal-Org-Operating-Model #20 and #22 have no other touch under the rules (source: research/Q-018-memo-2.md)
