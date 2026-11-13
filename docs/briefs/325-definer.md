# Brief 325 — definer — S-002 and E-004: brief 324's findings fixed (P-002, M8, M9)

session: session_01QBwHGNX4HWBSkreQEL7zEL
model: the Definer runs in a fresh session. Model names are kept out of this record by this session's standing instructions (LL-70).
start: Model-Lab@cadda95f8aa89fe1ac5340e3ca752f06ad623d9a (branch build/definer/p002-fix-6, in its own worktree /home/user/wt/ml-definer-325, made from the commit that adds this brief)
manifest: the worktree; specs/S-002.md; experiments/E-004.md; reviews/S-002-rulings-5/_critic-verbatim.md (brief 324's findings); decisions/questions/P-002-touch-log-check.md; docs/briefs/323-definer.md
recorded: at hand-out, 2026-11-13

## Brief
In specs/S-002.md and experiments/E-004.md only, with brief 314's limits, fix brief 324's findings:
1. Finding 5 (blocking for the freeze): replace the time-based cut-off with one rule, written the same way in E-004 Step 5 and Exclusions and S-002 AC9 and J9: once the desk keeps its record, a look counts the lines the desk's record says it showed that are put against the look's pieces, with each change the record holds applied as the record gives it; every other difference between the log and the record (a line not shown, a removal or change the record does not hold, a change logged differently) is listed by side outside the deciding result, with the logged version reported beside it. Keep the stated fallback until the record exists.
2. Finding 7: the "without late lines" result is the log as it stood at each piece's merge, from git history (additions out, corrections as first logged, a removed line back in if committed before its piece merged).
3. Finding 8: make AC5's record clause conditional ("once the desk keeps its record").
4. Finding 9: in the plain words, separate the owner's choice ("confirm or add to") from this plan's design (taking a line out, the desk's record), and add "or corrects onto the wrong piece" to the plain-words misses.
Do not make any look wait for the desk's record (finding 6). Return a table (place, change, lines). Re-read each changed sentence against the record it states (LL-55). Do not freeze. Run Python as `python3 -I -B` (LL-84). Commit as `definer <definer@agents.invalid>` with the trailers `Agent-Session: session_01QBwHGNX4HWBSkreQEL7zEL/definer-325` and `Spec: S-002` in one paragraph; do not push or merge. Run `governance/checks/check_all.sh . <the commit that adds this brief>` and `python3 -I -B governance/checks/surface_guard.py diff --range <that commit>..build/definer/p002-fix-6 --branch build/definer/p002-fix-6`. Return the six-part contract.
