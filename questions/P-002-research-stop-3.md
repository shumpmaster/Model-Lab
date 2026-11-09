# Ruling needed: two research write-ups on agent teams failed their last check

Milestone: Discovery-5

How should the screening project (the work on finding and adopting outside AI practice) use two research subjects: how teams of AI agents under one or a few people are run, and how the share of work agents do, people's trust in it and whether it holds up are measured? Both write-ups failed their third and last check against their sources. The model's stop rule allows no fourth round without you.

Each round found fewer things to correct:
- the first write-up (how agent teams are run): 20, then 6, then 1;
- the second (how their work is measured): 16, then 4, then 3.

At round 2, three of the first write-up's corrections had not held; at round 3, every correction from round 2 held. What failed at round 3 was wording that said more than its source. One table cell said a vendor's feature is "in use", where the source is a dated post announcing it. One line credited a Google figure to its chief executive by name, where the article says only "the company says".

Beside the write-ups, the checker filed short entries in the shared library of checked facts (a separate repository): 22 facts and 2 patterns (general practices drawn from the facts) for the first, 23 facts and 2 patterns for the second, 49 entries in all. The first check opened most entries' sources before filing; a few could not be opened, and some rest on abstracts or press reports, so they are graded weak. The next two checks re-read the entries against the write-ups and corrected several, the last of them at round 3. No check has passed the entries as a set. Nothing here is irreversible.

WHY: the project's next step, your choices on how success is measured, needs a measure the research on the second subject was asked for: the pre-mortem's risks R3 and R12 turn on how the share of work and its quality are measured (docs/projects/P-002.md, section 7). Unruled, it waits.
OPTIONS:
  A. Keep only the library entries, after one check of them.
     Set both write-ups aside. A fresh source checker (a helper that opens each source) re-checks all 49 entries against their sources, once, and rewords or removes any that fail. That check decides; if it fails, a new question like this one comes to you. The entries that pass come to you in one library pull request (a proposed change) holding both branches, to approve.
     Gain: what the plan uses has passed a check as a set. This is the route you chose for the last two write-ups; that check passed, rewording 12 of 29 and 12 of 24 entries (research/Q-012-entries-check.md, Q-014-entries-check.md).
     Cost: one check of 49 entries, which can itself fail; one more pull request for you; the plan reads these subjects from separate entries, not a summary.
     Undo: once in the shared library, an entry can be withdrawn by a later change, but another project may have relied on it by then.
  B. One focused round on both write-ups.
     The researcher fixes the four remaining items and re-reads every summary line; one check of each write-up, covering its entries too, then decides, and a failure brings a new question like this one. The entries that pass come with them in one pull request.
     Gain: both subjects keep a summary.
     Cost: one more round each; the same kind of fault has reappeared each round (docs/LESSONS.md, LL-71).
     Undo: the earlier versions stay on record; once in the shared library, an entry can be withdrawn by a later change, but another project may have relied on it by then.
  C. Drop both subjects from this phase (Discovery, the project's first phase).
     The entries for these two stay unmerged and unused. The plan relies on the research that passed (Q-010, Q-011, Q-013) and the entries already in the library, which touch these subjects only in part.
     Gain: no more rounds, and nothing more to approve.
     Cost: how agent teams are run, and how their work is measured, go into the plan with thin research, though they are what you said the project is for (decisions/questions/P-002-target.md).
     Undo: the write-ups and entries stay on record and can be taken up later.
RECOMMENDATION: A, with moderate confidence (the Chief of Staff's judgement): the entries have been corrected each round, and one check of them as a set makes them safe to rely on, as it did last time. What would change it: wanting a summary of these subjects in the plan (then B), or deciding they can wait (then C).
WHO HAS CHECKED IT: the source checker's three rounds on each write-up; the Critic on this card, PASS at round 2 (reviews/P-002-research-stop-3/critic.md).
RISK CLASS: R0, a question only   REVERSIBILITY: reversible   BLAST RADIUS: two research write-ups of the screening project, their filed entries, and the plan that draws on them
DEFAULT: none, deliberately: the stop rule leaves the next step to you   TIMEOUT: none

## Context
- The first write-up (research Q-015) failed round 3 on one table cell; every round 2 correction held (source: research/Q-015-source-check.md, round 3)
- At round 2, 17 of the first write-up's 20 round 1 corrections held and 3 did not (source: research/Q-015-source-check.md, round 2)
- The second write-up (research Q-016) failed round 3 on three wordings; every round 2 correction held (source: research/Q-016-source-check.md, round 3)
- The lists of corrections ran 20, 6 and 1 for the first, and 16, 4 and 3 for the second (source: research/Q-015-source-check.md and research/Q-016-source-check.md, rounds 1 to 3)
- Filed entries were corrected in rounds 2 and 3, including Q-015-18, Q-015-23, Q-016-2 and pattern Q-016-P25 at round 3 (source: the same files, the "Entries changed" part of each round)
- For the last two write-ups that reached the stop rule, the owner chose to keep only their entries after one check, and that check passed (source: decisions/questions/P-002-research-stop-2.md; research/Q-012-entries-check.md; research/Q-014-entries-check.md)
- The owner's aim for the project is how multi-agent systems are run and optimised (source: decisions/questions/P-002-target.md)
- The pre-mortem's risks R3 and R12 turn on how the share of work and its quality are measured (source: docs/projects/P-002.md, section 7)
- At the stop rule the owner chooses from fixed options: re-specify, re-scope, drop, or one focused confirmation review; accepting work despite a failed check is never an option (source: Personal-Org-Operating-Model OPERATING_MODEL.md §4 "Stop rule")
- The recurring cause is recorded (source: docs/LESSONS.md, LL-71)
- The filed entries are on two local branches of the portfolio library, build/source-checker/q-015 (22 facts, 2 patterns) and build/source-checker/q-016 (23 facts, 2 patterns), not yet in a pull request (source: worktrees /home/user/lib-q-015 and /home/user/lib-q-016)
