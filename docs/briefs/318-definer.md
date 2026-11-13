# Brief 318 — definer — S-002: brief 317's findings, the live coder disclosed (P-002, M8)

session: session_01QBwHGLHPCVt3NpHNqhuahM
model: the Definer runs in a fresh session. Model names are kept out of this record by this session's standing instructions (LL-70).
start: Model-Lab@37f3ff3e2ed03693c2b74677f07b3f380070af81 (branch build/definer/p002-fix-2, in its own worktree /home/user/wt/ml-definer-318, made from the commit that adds this brief)
manifest: the worktree; specs/S-002.md; experiments/E-004.md; reviews/S-002-rulings-2/_critic-verbatim.md (all findings); questions/P-002-live-later-work-check.md (an open card; do not write in any of its options); research/Q-018-extract/ (README.md, sample.jsonl); governance/PACKS.toml; full clones with history at /tmp/claude-0/-home-user/48846bdd-45a4-59bb-b690-7e716cd073d8/scratchpad/hc/<repository> (read only)
recorded: at hand-out, 2026-11-13

## Brief
In specs/S-002.md, and in experiments/E-004.md only where finding 1 names it, with brief 314's limits:
1. Finding 1: disclose that in live trials the Chief of Staff, who knows each piece's side, codes `later_work` unchecked, in each place finding 1 names (the plain-words paragraph, J3, J4, Risks, and E-004's "What this trial cannot catch" and Steps 1 and 8). Add an open question pointing to questions/P-002-live-later-work-check.md, with its three options; write in none of them.
2. Findings 5 (the "until the owner rules" wording), 7 (J1's "reads no record's text"), 8 (POOM #20 and step 6 (q)), 10 (the starting ruling for brief-dispatched pieces, and the step 6 item), 11 (a record asking about the piece and other work: "this piece" when any part asks about the piece under way), 12(3) (a touch-log line with a non-null `record` carries only a code), 13 (the coder's source is the records pack).
3. Finding 9: say whether a ledger entry can be a skip source for another entry. Take "it cannot" (two different approvals stay two), unless the ruling's words require otherwise; say which, and list the case in step 6 (r).
Return a table (finding, fix, lines, sampled results expected to change). Re-read each changed sentence against the record it states (LL-55). Do not freeze. Run Python as `python3 -I -B` (LL-84). Commit as `definer <definer@agents.invalid>` with the trailers `Agent-Session: session_01QBwHGLHPCVt3NpHNqhuahM/definer-318` and `Spec: S-002` in one paragraph; do not push or merge. Run `governance/checks/check_all.sh . <the commit that adds this brief>` and `python3 -I -B governance/checks/surface_guard.py diff --range <that commit>..build/definer/p002-fix-2 --branch build/definer/p002-fix-2`. Return the six-part contract.
