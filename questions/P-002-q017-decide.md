# Ruling needed: the count's deciding check failed on how the checking rounds were coded

Milestone: Discovery-2

The one deciding check you ruled for the count of our own records failed, so the next step is yours. You will choose whether to count without the checking rounds, fix their coding, or set the target without starting figures. Nothing here is irreversible.

The count reads extracts: files I had the Orchestrator (the role that keeps records) build from the repositories, with no text from your records in them. What the check found: the count question is now blind to what anyone hopes it shows, and neutral. It did not check the commit and pull-request extracts for accuracy; an earlier round judged the counts workable from them.

What failed is the rounds extract, which codes every round of checking from the review records. Those records come in many formats, and the Orchestrator's script got several wrong. It counted reviewers' briefs and README files as passing verdicts, read headings such as "Round 2 findings" as rounds, split one check into several pieces, and dated some final verdicts before the failures that came before them. So the figures for work passing its check at the first try, and for work failing three checks in a row, would be wrong. The script's output was not checked against a sample of the files first; that slip is in the lessons log (LL-73).

WHY: your ruling sends a failure back to you, and your choice of how success is measured waits on starting figures (one of the ways the project could fail, listed in its plan, is a measure with no starting figure).
OPTIONS:
  A. Count without the checking rounds.
     The rounds files, their script and the README's text on them are removed from the extract, and the question is narrowed to: who made and merged changes, how often you were asked, and how often merged changes were changed again. The two remaining extracts are checked by hand against a sample of the records first (LL-73). One short check of the narrowed question and those extracts then decides; a failure comes back to you.
     Gain: three of the four figures, from the extracts the earlier round found workable, once checked.
     Cost: a check that can fail again, since the two extracts have not yet been hand-checked; and no fresh count of checking rounds. The earlier counts stand in: they are dated 2026-11-01, the dispatch log the first of them read stops on 2026-10-08, and they count by item checked, not by pull request.
     Undo: the rounds can be counted later.
  B. Fix the rounds coding, then one more check.
     The Orchestrator recodes the rounds from the Critic's list: drop briefs and READMEs; split only on real round headings; group one check's files into one piece; date a verdict by the last change to its verdict line, or mark it overwritten; mark dispatch lines from roles that are not checkers. The question gains a tie-break for rounds on the same date, and a rule for a first round with no recorded verdict. The output is checked by hand against a sample of each file format, and one more check decides; a failure comes back to you.
     Gain: all four figures.
     Cost: the most work, and a check that can fail again; the records' many formats are the cause, and some may still be coded wrong.
     Undo: nothing changes until the count is on record.
  C. Set the value target without starting figures.
     Drop the count. The target is set from the measure's definition, and a starting figure is measured from new work before any trial.
     Gain: no more checks; your choice comes sooner.
     Cost: the target's size is chosen without knowing today's level; the first trials wait for the new-work figure.
     Undo: the target can be re-set by a later ruling once figures exist.
RECOMMENDATION: A, with moderate confidence (the Chief of Staff's judgement): it keeps the figures closest to how much work agents carry and how often you step in, and avoids the records that are least uniform. What would change it: wanting the rounds figure fresh (then B), or wanting no more checks (then C).
WHO HAS CHECKED IT: the Critic's three rounds and the deciding check on the count question; the Critic on this card, PASS at round 2 (reviews/P-002-q017-decide/critic.md).
RISK CLASS: R0, a question only   REVERSIBILITY: reversible   BLAST RADIUS: one research question of the screening project, and the starting figures for its value target
DEFAULT: none, deliberately: the ruling sends the next step to you; until you choose, the count and the target wait   TIMEOUT: none

## Context
- The owner ruled extracts only and one deciding check, a failure coming back to the owner (source: decisions/questions/P-002-q017-stop.md)
- The deciding check failed on the rounds coding, found the question blind and neutral, and found round 3's blocking finding answered (source: reviews/P-002-research-q017/critic.md, deciding check)
- Round 3 judged the counts from the commit and pull-request extracts workable (source: reviews/P-002-research-q017/critic.md, round 3, finding 7)
- The earlier counts are dated 2026-11-01 (source: research/Q-006-memo.md, research/Q-008-memo.md); the dispatch log the first read stops on 2026-10-08 (source: research/Q-006-memo.md)
- The risk of a measure with no starting figure is R12 of the pre-mortem (source: docs/projects/P-002.md, section 7)
- The slip is recorded (source: docs/LESSONS.md, LL-73)
- At the stop rule the owner chooses from fixed options: re-specify, re-scope, drop, or one focused confirmation review; accepting work despite a failed check is never an option (source: Personal-Org-Operating-Model OPERATING_MODEL.md §4 "Stop rule")
