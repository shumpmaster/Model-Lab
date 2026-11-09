# Ruling needed: two research write-ups failed their last check; keep only their single checked facts, drop them, or rewrite their summaries in a fixed form

Milestone: Discovery-5

Which way should the screening project (the work on finding and adopting outside AI practice) take two of its research subjects: how often to look at outside practice and who does the reading, and how others judge, retire and stop changes? You ruled one more round on each write-up, with one check deciding it and a failure coming back to you. Both failed.

Every fix the round asked for was made, and nothing unconfirmed is relied on. What failed is again wording: summary lines and section headings that say more than their sources. One example: the first write-up says reviews "went without an update" where its source says they were updated late. Its list of fixes is now 9 items; the second's is 11.

Beside each write-up, the checker filed short single facts in the shared library of checked facts (a separate repository): 27 facts and 2 patterns for the first, 21 facts and 3 patterns for the second. Each was checked against its source when filed. The last round found nine that needed correcting and corrected them, but it compared the rest only with the write-up, some quickly, and no check has passed the facts as a set. Nothing here is irreversible.

WHY: the rule sends a failure back to you, and the rest of this first phase (Discovery) waits on knowing which research on these two subjects it can use.
OPTIONS:
  A. Keep only the single facts, after one check of them.
     Set both write-ups aside. A fresh source checker (a helper that opens each source) re-checks every filed fact for the two subjects against its source, once, and removes or rewords any that fail; that check decides, and a failure comes back to you. The facts that pass reach the shared library only through a pull request (a proposed change) you approve.
     Gain: no more rounds on the write-ups; what the plan uses has passed a check as a set.
     Cost: one check of 53 entries; the project's plan reads these subjects from separate facts, not a summary; and one more pull request for you.
     Undo: after the library change is merged, entries can be withdrawn by a later change.
  B. Drop both subjects from this phase.
     Use only the three write-ups that passed; the filed facts for these two stay unmerged and are not used.
     Gain: no more rounds, and nothing more to approve.
     Cost: how often to look, and how to judge and retire changes, go into the plan with no research behind them.
     Undo: the write-ups and facts stay on record and can be taken up later.
  C. Rewrite only the summaries, in a fixed form.
     A fresh researcher replaces each write-up's summary lines with short lines that each quote the checked wording of the fact they rest on, and nothing more; one check then decides each, and a failure comes back to you a third time. The filed facts wait until then, and are kept or dropped by what you rule after that check.
     Gain: both subjects keep a summary.
     Cost: one more round each, with a form not yet tried; the last two rounds failed on the same cause.
     Undo: the earlier versions stay in the record.
RECOMMENDATION: A, with moderate confidence (the Chief of Staff's judgement): the single facts held up better than the summaries, and four rounds show the summaries keep saying more than them. What would change it: wanting a summary of these two subjects in the plan (then C), or judging them unimportant for this phase, or not wanting another check and pull request (then B).
WHO HAS CHECKED IT: the source checker's four rounds on each write-up; the Critic on this card (reviews/P-002-research-stop-2/critic.md).
RISK CLASS: R0, a question only   REVERSIBILITY: reversible   BLAST RADIUS: two research write-ups of the screening project, their filed facts, and the plan that draws on them
DEFAULT: none, deliberately: the stop rule leaves the next step to you   TIMEOUT: none

## Context
- The owner ruled one more focused round, one check deciding each memo, a failure coming back to the owner (source: decisions/questions/P-002-research-stop.md)
- The first write-up (research Q-012) failed its deciding check: the round 3 fixes held, nothing unconfirmed is relied on, and summary sentences and headings were still worded more strongly than their findings; 9 items listed; three entries corrected and "the rest" read against the memo (source: research/Q-012-source-check.md, round 4)
- The second write-up (research Q-014) failed its deciding check on the same kind of wording; 11 items listed; six entries corrected and the other facts "skimmed against the memo" (source: research/Q-014-source-check.md, round 4)
- The lists of fixes asked for ran 14, 11, 4 and 9 for the first, and 15, 5, 8 and 11 for the second (source: research/Q-012-source-check.md and research/Q-014-source-check.md, rounds 1 to 4)
- The other three write-ups passed their source checks (source: research/Q-010-source-check.md, round 3; research/Q-011-source-check.md, round 2; research/Q-013-source-check.md, round 2)
- At the stop rule the owner chooses from fixed options: re-specify, re-scope, drop, or one focused confirmation review; accepting work despite a failed check is never an option (source: Personal-Org-Operating-Model OPERATING_MODEL.md §4 "Stop rule")
- The cause is recorded, and recurred in the focused round (source: docs/LESSONS.md, LL-71)
- The filed facts are on two local branches of the portfolio library, build/source-checker/q-012 (27 facts, 2 patterns) and build/source-checker/q-014 (21 facts, 3 patterns), not yet in a pull request (source: worktrees /home/user/lib-q-012 and /home/user/lib-q-014)
