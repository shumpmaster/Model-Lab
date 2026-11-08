# Brief 132 — critic — round 1 on the re-made route card and its sizing record

session: session_01QBwHGNSLmSrYQgS6BPjV8p
model: the Critic ran on a different model from the card's writer, the Chief of Staff's session (D-056; the dispatch asked for a different model family). Model names are kept out of this record by this session's own standing instructions, which bar model identifiers in anything pushed to a repository; they are in the session's transcript (LL-70).
start: Model-Lab@957dadc plus the uncommitted card and sizing record in the live checkout; read live, not from a fixed copy
manifest: none
recorded: after hand-out, 2026-11-08, backfilled from the exact text the session sent, because no record was written at hand-out (LL-70)

## Brief
You are the Critic under the AI Build Operating Model. Check one owner question card, cold, as a smart non-expert would read it, before it is put to the owner. This is round 1 of a new card; it replaces one that failed three rounds because the change it routes (an upgrade of the repository to a newer model version) had not been sized from the files. It now cites a sizing record.

The card: /home/user/Model-Lab/questions/P-002-route.md
The sizing record it rests on: /home/user/Model-Lab/intake/P-002-upgrade-footprint-2026-11-08.md

The standard: Personal-Org-Operating-Model/OPERATING_MODEL.md §2 (decision cards D-019; Plain English first S-026; Every ask is filed S-033); Model-Lab/AGENTS.md §5 and Model-Lab/questions/_TEMPLATE.md (form); options fairly put; the recommendation not presented as the only reasonable choice.

Open every Context source (under /home/user/: Model-Lab, Personal-Org-Operating-Model, Service-Desk, portfolio) and confirm it says what is claimed. For the sizing record, check what you can against the files: that the listed Model-Lab files exist; that the model's changes between commits 3a2606a and b18259c are what it lists (you can read Personal-Org-Operating-Model/CHANGELOG.md and compare current files in Personal-Org-Operating-Model/tools/ and template-v3/ with Model-Lab's copies by reading them); that the prompt engine's tests read only the functions and pack roles it names (tests/acceptance/e003_support.py, test_j7_analysis_pack.py, test_j8_holdout_pack.py); that docs/PROJECT.md is said to be left unchanged. You have no shell, so the trial's test runs cannot be repeated by you; say so and judge whether the record states its method plainly enough to be repeated.

Return PASS or FAIL, then numbered findings: line, what is wrong, why it matters to the owner, blocking or non-blocking. Do not fix the card.

## Outcome
FAIL (reviews/P-002-route-2/critic.md, round 1)
