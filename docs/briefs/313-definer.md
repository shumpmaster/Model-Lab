# Brief 313 — definer — S-002: brief 312's three wording points (P-002, M8)

session: session_01QBwHGLHPCVt3NpHNqhuahM
model: the Definer runs in a fresh session. Model names are kept out of this record by this session's standing instructions (LL-70).
start: Model-Lab@26c8534cc3d11cb2e27682cf3fef132acd900c33 (branch build/definer/p002-rule-fixes-9, in its own worktree /home/user/wt/ml-definer-313, made from the commit that adds this brief)
manifest: the worktree; specs/S-002.md; reviews/Q-018-recode-4/_critic-verbatim.md (findings 1, 2 and 3); research/Q-018-extract/README.md (its last paragraph)
recorded: at hand-out, 2026-11-12

## Brief
In specs/S-002.md only, with the same limits as brief 311, and in the Critic's words where it gives them; no counting result may change:
1. Finding 1: open question 10's line (:253) now reads that the Critic checked both sets as the sample stands after Service-Desk #237 stopped being a piece (set (a) with Model-Lab #93, brief 312; set (b) with Service-Desk #341, brief 310).
2. Finding 2: step 3 (:109) gives the ids for an answer record's first add and each append, as RT1(a) and the extract do.
3. Finding 3: "What a touch is" (:46): "the commit that first adds it to the default branch" becomes the reachable commit with the earliest commit time that adds it, which is what the extract does. Say whether Model-Lab #29's example in RT1(a) stays (the Critic says it may, as an illustration).
Return a table (finding, fix, lines). Do not freeze. Run Python as `python3 -I -B` (LL-84). Commit as `definer <definer@agents.invalid>` with the trailers `Agent-Session: session_01QBwHGLHPCVt3NpHNqhuahM/definer-313` and `Spec: S-002` in one paragraph; do not push or merge. Run `governance/checks/check_all.sh . <the commit that adds this brief>` and `python3 -I -B governance/checks/surface_guard.py diff --range <that commit>..build/definer/p002-rule-fixes-9 --branch build/definer/p002-rule-fixes-9`. Return the six-part contract.
