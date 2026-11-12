# Brief 292 — definer — S-002: the second re-check's findings (P-002, M8)

session: session_01QBwHGHoKws9VC78aWK8zpb
model: the Definer runs in a fresh session. Model names are kept out of this record by this session's standing instructions (LL-70).
start: Model-Lab@df93c61275f141e832571aa6e3417044b991cd3c (branch build/definer/p002-rule-fixes-3, in its own worktree /home/user/wt/ml-definer-292, made from the commit that adds this brief)
manifest: the worktree; reviews/Q-018-rules/_critic-r2-verbatim.md (findings 1 to 7); specs/S-002.md; docs/briefs/290-definer.md; research/Q-018-extract/ (Service-Desk.list.jsonl, github_reads.json); the clones /home/user/Service-Desk and /home/user/Personal-Org-Operating-Model (read only)
recorded: at hand-out, 2026-11-12

## Brief
The Critic's second re-check failed with one blocking finding (reviews/Q-018-rules/_critic-r2-verbatim.md). In specs/S-002.md only, with the same limits as brief 290 (no change to the draw, sample, seed, cut-off or any edge-case filter's text; no rule the findings do not touch):
1. Finding 1 (blocking): a record is RT5's when its own text classes it as a phase gate or a value target, or part of one (Model-Lab's `Asked:` lines, as the Critic cites); the name words stay as the test only where a record gives no class; a record whose text says it is a stop-rule choice is counted whatever its name. Check every record the change moves (trial-gates, two-look-line, build-gate-stop, P-002-target, and any other) against the three repositories, and list them.
2. Finding 2: rework open question 13's reasoning and examples so it does not argue Open question 3; keep its options and give a recommendation.
3. Findings 3(a) to (e), 4, 5(a) to (c), 6 and 7: fix or answer each. For 5(c), say in step 3 how the extract keeps head branch names (they are already in the list files in clear), so the spec and the extract agree; change no extract file.
Return the same table as brief 290. Re-read each changed sentence against the record it states (LL-55). Do not freeze. Run Python as `python3 -I -B` (LL-84). Commit as `definer <definer@agents.invalid>` with the trailers `Agent-Session: session_01QBwHGHoKws9VC78aWK8zpb/definer-292` and `Spec: S-002` in one paragraph; do not push or merge. Run `governance/checks/check_all.sh . <the commit that adds this brief>` and `python3 -I -B governance/checks/surface_guard.py diff --range <that commit>..build/definer/p002-rule-fixes-3 --branch build/definer/p002-rule-fixes-3`. Return the six-part contract.
