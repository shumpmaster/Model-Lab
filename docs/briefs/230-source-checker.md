# Brief 230 — source-checker — the Q-017 count memo

session: session_01QBwHGNSLmSrYQgS6BPjV8p
model: the Source checker runs on a different model from the Researcher whose memo it checks (D-056). Model names are kept out of this record by this session's standing instructions (LL-70).
start: Model-Lab@21279c8df1087103eab591fb1d2b555189007f8e plus research/Q-017-memo.md in the live checkout
manifest: research/Q-017.md, Q-017-memo.md, Q-017-extract/**; the three repositories, read-only, to sample
recorded: at hand-out, 2026-11-09

## Brief
You are the Source checker under the AI Build Operating Model. Check one research memo that counts an organisation's own records, and confirm its figures. You run on a different model from the Researcher who wrote it.

The memo: /home/user/Model-Lab/research/Q-017-memo.md. The question: /home/user/Model-Lab/research/Q-017.md. The extract it counted: /home/user/Model-Lab/research/Q-017-extract/ (README.md first). The memo ends with the script that made its figures.

Check:
1. Rerun the memo's script over the extract (python3 -I, writing only under /tmp/q017-check/) and confirm every figure the memo states matches the script's output. List any that do not.
2. Recount the main figures independently with your own code, not the memo's: merged pull requests per repository and month; pull requests with and without a commit under the owner's identity; the merging accounts; commits by author class; files first added with a question label and with a decision label; and the 14-day named and file-overlap counts.
3. Test the extract against the repositories themselves on a sample of your own choosing (/home/user/Service-Desk, /home/user/Model-Lab, /home/user/Personal-Org-Operating-Model, default branch, read-only: git log, git show, git rev-list on origin/main), including at least one workflow-bot merge, one commit under the owner's identity, and one file first added under questions/ (by its path in git; do not open the file's contents).
4. Check that every rule the memo states is the rule its script applies, that each figure is marked as the question asks, and that no sentence is worded more strongly than its figure (lesson LL-71).

Do not read docs/projects/, docs/PROJECT.md, ideas/, sessions/chief-of-staff/, or the contents of anything under questions/ or decisions/; do not use the web.

Return: first line exactly `Verdict: PASS` (every figure confirmed, every rule as stated) or `Verdict: FAIL`; then a table of each figure or rule checked with confirmed / does not hold and a one-line reason; then your independent recounts; then your sample against git; then what the memo must correct. Report your total tokens if you can see them.
