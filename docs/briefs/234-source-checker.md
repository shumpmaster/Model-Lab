# Brief 234 — source-checker — round 3 (last before the stop rule) on the revised Q-017 memo

session: session_01QBwHGNSLmSrYQgS6BPjV8p
model: the Source checker runs on a different model from the Researcher whose memo it checks (D-056). Model names are kept out of this record by this session's standing instructions (LL-70).
start: Model-Lab@8655f650263b77a4ef2f78a3925e6f613a4bb6ce plus the revised research/Q-017-memo.md in the live checkout
manifest: research/Q-017.md, Q-017-memo.md, Q-017-source-check.md, Q-017-extract/**; the three repositories, read-only
recorded: at hand-out, 2026-11-09

## Brief
You are the Source checker under the AI Build Operating Model. Round 3, the last before the stop rule: re-check a revised research memo against round 2's corrections. You run on a different model from the Researcher.

The revised memo: /home/user/Model-Lab/research/Q-017-memo.md (round 3; its change list is at the end). Rounds 1 and 2 of the check, with "What the memo must correct": /home/user/Model-Lab/research/Q-017-source-check.md. The question: /home/user/Model-Lab/research/Q-017.md. The extract: /home/user/Model-Lab/research/Q-017-extract/.

Check:
1. Rerun the memo's revised script over the extract (python3 -I, writing only under /tmp/q017-check3/) and confirm every figure the memo states matches its output, and that the figures rounds 1 and 2 confirmed are unchanged or the change is explained.
2. For each correction round 2 asked for, confirm it is made, and that round 1's corrections still hold.
3. Read every sentence of the opening paragraph and each item's summary, and confirm each is worded no more strongly than its figure and carries the question's mark (supported, in part, not supported) (lesson LL-71).
4. Confirm the memo and its script report no path or file name.
You may re-test against the repositories read-only (/home/user/Service-Desk, /home/user/Model-Lab, /home/user/Personal-Org-Operating-Model, origin/main) where the earlier rounds' record is not enough. Do not read docs/projects/, docs/PROJECT.md, ideas/, sessions/chief-of-staff/, or the contents of anything under questions/ or decisions/; do not use the web.

Return: first line exactly `Verdict: PASS` or `Verdict: FAIL`; then a table of each correction and each figure you re-checked, holds / does not hold, with a one-line reason; then what, if anything, the memo must still correct. Report your total tokens if you can see them.
