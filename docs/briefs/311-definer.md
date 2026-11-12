# Brief 311 — definer — S-002: the clauses and list items step 5 on memo 4 asked for (P-002, M8)

session: session_01QBwHGLHPCVt3NpHNqhuahM
model: the Definer runs in a fresh session. Model names are kept out of this record by this session's standing instructions (LL-70).
start: Model-Lab@0631a7b828c7ad862beb7bd0dd63fcaaae1fcb14 (branch build/definer/p002-rule-fixes-8, in its own worktree /home/user/wt/ml-definer-311, made from the commit that adds this brief)
manifest: the worktree; specs/S-002.md; reviews/Q-018-recode-3/_critic-verbatim.md (findings 1, 7, 8 and 9); research/Q-018-memo-4.md; research/Q-018-extract/ (README.md, sample.jsonl); full clones with history at /tmp/claude-0/-home-user/48846bdd-45a4-59bb-b690-7e716cd073d8/scratchpad/hc/<repository> (read only)
recorded: at hand-out, 2026-11-12

## Brief
In specs/S-002.md only, with the same limits as briefs 300, 305 and 309 (no change to the draw, sample, seed, cut-off or any edge-case filter's text; no rule a finding does not touch):
1. Finding 7(a): K3's "changed lines" are added plus removed lines; say so in one clause.
2. Finding 7(b): a paired record's event times a question only when that record itself names the piece (the memo's reading for Model-Lab #29); say so in RT1(a).
3. Finding 9(b): RT1(a) pairs a question file with an answer record's first add that names its id, as well as with an append.
4. Finding 9(a): bare `Q-<nnn>` pairing can cross repositories (Personal-Org-Operating-Model #25's Q-013 append); add it to step 6's list, or, if a clause can make the pairing same-repository only without reading text, add that and say which.
5. Finding 8: step 6(m)'s reason for Personal-Org-Operating-Model #49, in the Critic's words.
6. Finding 1: open question 10's line that "the Critic checked both sets" holds only once the new tenth piece under reading (a) is opened; the Orchestrator's computation with the draw's seed gives Model-Lab #93 (after Service-Desk #148, with #237 out). Reword that line so it stays true until the Critic's next check, and name #93.
For each of 1 to 3, say whether any sampled count or time changes. Return a table (finding, fix, lines, sampled results changed). Re-read each changed sentence against the record it states (LL-55). Do not freeze. Run Python as `python3 -I -B` (LL-84). Commit as `definer <definer@agents.invalid>` with the trailers `Agent-Session: session_01QBwHGLHPCVt3NpHNqhuahM/definer-311` and `Spec: S-002` in one paragraph; do not push or merge. Run `governance/checks/check_all.sh . <the commit that adds this brief>` and `python3 -I -B governance/checks/surface_guard.py diff --range <that commit>..build/definer/p002-rule-fixes-8 --branch build/definer/p002-rule-fixes-8`. Return the six-part contract.
