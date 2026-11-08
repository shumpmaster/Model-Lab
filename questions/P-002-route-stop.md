# Ruling needed: the route card for starting the screening failed its check three times; size the upgrade first, have one focused last check, or hold

Milestone: none (the screening is not yet a project item here; this ruling decides how its route is settled)

The card asking you how the screening of cutting-edge practice starts failed the Critic's check three times, so by the model's stop rule it stops and comes to you. Each failure was the same: the card described the needed upgrade of this repository's rules and checks from its change notes, not from the files, and so kept understating what it touches, including two of the prompt engine's test files and a list of files those tests read. Nothing has been changed in the repository: no upgrade, no project filed, and nothing of the prompt engine's touched. You choose how to settle the route; nothing here is irreversible. If you rule nothing, nothing starts.

WHY: the screening cannot be filed until its route is settled, and the stop rule leaves the next step to you.
OPTIONS:
  A. Size it first, then a new card — the Chief of Staff writes down every file the upgrade would change, from a file-by-file comparison, and which of the prompt engine's tests, file lists and checks each one reaches; a fresh Critic checks the new card against that record. Gain: the route rests on a measured footprint, which is what all three failures lacked. Cost: an estimated half day more before the route reaches you, and the Critic's usage for new rounds. Reversible: yes.
  B. One focused last check — the card is reworded once to fix the round-3 findings and one Critic round decides it; if it fails, it comes back here. Gain: faster, if it passes. Cost: the footprint still comes from the change notes, the gap behind every failure so far. Reversible: yes.
  C. Hold the screening — nothing more is done until you say. Gain: no further usage, and no change beside the prompt engine. Cost: the second idea waits with no date. Reversible: yes.
RECOMMENDATION: A, with high confidence (the Chief of Staff's judgement): it fixes the one cause behind all three failures, and the footprint is needed for the upgrade's own review whichever way the route goes. What would change it: wanting the screening started sooner at the risk of a fourth failure (then B), or wanting nothing beside the prompt engine for now (then C).
WHO HAS CHECKED IT: the Critic failed the route card in three rounds (reviews/P-002-route/critic.md); stop cards go to the owner without a further round, as the stop rule says.
RISK CLASS: R0 (questions/**)   REVERSIBILITY: reversible   BLAST RADIUS: the screening's start only
DEFAULT: none, since starting a project is yours to rule; undecided, nothing starts   TIMEOUT: none

## Context
- The route card failed the Critic in rounds 1, 2 and 3, each time on the upgrade's reach (source: reviews/P-002-route/critic.md)
- At three plan rounds the owner gets one summary and, if needed, a card with fixed options: re-specify, re-scope, drop, or one focused confirmation review (source: Personal-Org-Operating-Model OPERATING_MODEL.md §4 "Stop rule")
- The cause is recorded as the route being put before the change was sized, the same cause as the Service Desk launch plan's failed rounds (source: docs/LESSONS.md, LL-69)
- The prompt engine's tests in test_j7_analysis_pack.py and test_j8_holdout_pack.py read governance/checks/session_runner.py, govlib.py and governance/PACKS.toml, which an upgrade would change (source: reviews/P-002-route/critic.md, round 3; tests/acceptance/e003_support.py)
- The round-3 wording of the route card is kept for reuse (source: intake/P-002-route-card-r3-2026-11-08.md)
