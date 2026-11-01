# Brief 13 — source-checker — check the Q-008 memo

session: session_01QBwHGHrHnEvMNYgKDoaH8w
model: claude-sonnet-5-5 (the Researcher on Q-008 ran on claude-opus-5-5; D-056)
recorded: at dispatch, 2026-11-01 (LL-04, LL-24)

## Brief

You are the Source checker (your role file: /home/user/Model-Lab/.claude/agents/source-checker.md). Today is 2026-11-01. Check the research memo /home/user/wt/ml-orch/research/Q-008-memo.md against its question /home/user/Model-Lab/research/Q-008.md and its sources. Its sources are local records only: /home/user/Service-Desk, /home/user/Model-Lab and /home/user/Personal-Org-Operating-Model (paths as the memo gives them). No web is needed.

1. Re-derive the counts that bear the most weight, with your shell, from the same records and the memo's stated searches and rules: the returns per kind (bottom line 1), the first-try figures (bottom line 2), the 117 classified and the primary-cause table (bottom line 4), and the per-kind tallies in §4. Say where your figure differs and which record decides it.
2. For a sample of at least 12 classified returns across the kinds (include every one whose primary cause is not "capability, residual", and at least 4 that are), open the cited record lines and confirm the record supports the avoidability mark and the causes given. Judge whether the memo applied its own rules in §1.3 and §1.4 as written.
3. Check that the sampling rule in §1.2 was applied as stated (positions and k), by listing the populations yourself.
4. Check each proposed library entry in §7 against the memo body and the records, and say per entry: fileable, fileable with a change (name it), or hold.
5. Check the memo answers each of the question's five items.

Do not open /home/user/Model-Lab/docs/PROJECT.md, /home/user/Model-Lab/decisions/, /home/user/Model-Lab/docs/handoff/, /home/user/Model-Lab/questions/ or /home/user/portfolio/ideas (the project's leanings). Write no files; do not file library entries yet (they are filed after the check passes). Return as your final message a record whose first line, in column 0, is exactly `Verdict: PASS` (the counts and classifications hold, allowing for slips you list) or `Verdict: FAIL` (any load-bearing figure or classification fails), then your findings by item.
