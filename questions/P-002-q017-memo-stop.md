# Ruling needed: the count's memo failed its last source check on one sentence

Milestone: Discovery-2

The memo that reports the count of our own records failed its third and last check by the source checker (the helper that confirms a memo against its sources). The model's stop rule allows no fourth check without you, so you choose: fix the one sentence and check it once more, or set the memo aside and use its figures alone. Nothing here is irreversible.

What the checks found: round 1 reran the memo's script, recounted the main figures with its own code, and tested a sample against git; the figures held, but the round failed on how they were marked and worded. Round 2 failed on one figure wrong, one sentence too broad, and file names left in the memo, all since fixed. Round 3 reran the script and confirmed every figure in the current memo, and found every earlier correction held. What failed at round 3 is one sentence describing a spread of figures: it says one to three pull requests sit at "each count from 5 to 22", but six of those counts have none.

WHY: the figures are the starting point for your choice of how the project's success is measured (its value target), which waits on them.
OPTIONS:
  A. Fix the one sentence, then one focused check (the stop rule's "one focused confirmation review").
     The sentence is replaced by the counts that occur, and one focused check confirms that change and nothing else. The script's label words stay as they are, as round 3 treated them as rule terms, not reported figures.
     Gain: the memo is used whole: its figures, each figure's mark (supported, supported in part, or not supported), and its stated limits.
     Cost: one more short check, which could fail; if it did, you would choose again from re-specify, re-scope or drop.
     Undo: nothing changes until the check is on record.
  B. Set the memo aside and use its figures alone (a re-scope).
     The plan uses the figures round 3 confirmed, with the marks the memo gives them, and not the memo's sentences.
     Gain: no more checks on the memo.
     Cost: the figures were confirmed as part of the memo, and their limits live in its sentences. The plan would restate those limits in new words, which would need their own check, since wording stronger than the figures is what failed earlier rounds.
     Undo: the memo stays on record and can be checked later.
RECOMMENDATION: A, with high confidence (the Chief of Staff's judgement): the fault is one sentence, the fix is mechanical, and it keeps the memo's checked limits with its figures. What would change it: wanting no further check on the memo at all (then B).
WHO HAS CHECKED IT: the source checker's three rounds on the memo; the Critic on this card, FAIL at round 1 and PASS at round 2 on this revision (reviews/P-002-q017-memo-stop/critic.md).
RISK CLASS: R0, a question only   REVERSIBILITY: reversible   BLAST RADIUS: the count memo of the screening project and the figures its value target draws on
DEFAULT: none, deliberately, as a departure from the usual form: the stop rule leaves the next step to you; until you choose, the value target waits   TIMEOUT: none

## Context
- Round 3 confirmed every figure in the current memo and found the round 1 and round 2 corrections held; it failed on one sentence in the section on questions put to the owner (source: research/Q-017-source-check.md, round 3)
- Round 2 found one figure wrong and one sentence too broad (source: research/Q-017-source-check.md, round 2)
- Round 1 recounted the main figures independently and sampled against git (source: research/Q-017-source-check.md, round 1)
- At the stop rule the owner chooses from fixed options: re-specify, re-scope, drop, or one focused confirmation review; accepting work despite a failed check is never an option (source: Personal-Org-Operating-Model OPERATING_MODEL.md §4 "Stop rule")
