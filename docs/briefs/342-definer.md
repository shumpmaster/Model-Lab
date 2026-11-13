# Brief 342 — definer — S-002 and E-004: stale citations, two wording matches, and memo 5's results out of the quoted rule line (P-002, M8, M9)

session: session_01QBwHGLKYvyVZk199qdegcJ
model: the Definer runs in a fresh session, apart from the Definers of briefs 321 to 341. Model names are kept out of this record by this session's standing instructions (LL-70).
start: Model-Lab@e83c854b9b50b3ecbf6aeb413a44287244d38f6a (branch build/definer/p002-fix-11, in its own worktree /home/user/wt/ml-definer-342, made from the commit that adds this brief)
manifest: the worktree; specs/S-002.md; experiments/E-004.md; decisions/questions/P-002-plan-stop-2.md and P-002-plan-written-by-piece.md (now on the default branch); docs/briefs/341-definer.md; reviews/S-002/plan.md, section "Focused confirmation review, at the second plan stop"
recorded: at hand-out, 2026-11-13

## Brief
In specs/S-002.md and experiments/E-004.md only, change nothing a rule means:
1. Citations: where the text cites questions/P-002-plan-stop-2.md or questions/P-002-plan-written-by-piece.md, or says the decision record "follows" (S-002 :46, :109, :267, :268, and any other place a search finds), cite decisions/questions/P-002-plan-stop-2.md and P-002-plan-written-by-piece.md, keeping the quoted option words.
2. Wording: S-002 :10's "handed out" and :267's summary of how option A was written in, brought to brief 341's wording (one boundary, "dispatch"; the first-commit listing).
3. The rule line at S-002 :46 is quoted verbatim to the Researcher (step 4), so it must carry no results: move the hand check's results it now holds (Model-Lab #98's brief times, sample lines, "no count of memo 5 changes" and the like) out of :46 into a sentence or note outside the lines step 4 quotes (for example step 6 or the hand check's order of work), keeping each fact and its source. Keep the rule itself word for word.
Do not freeze. Return a table (place, change, lines). Re-read each changed sentence against the record it states (LL-55). Run Python as `python3 -I -B` (LL-84). Commit as `definer <definer@agents.invalid>` with the trailers `Agent-Session: session_01QBwHGLKYvyVZk199qdegcJ/definer-342` and `Spec: S-002` in one paragraph; do not push or merge. Run `governance/checks/check_all.sh . <the commit that adds this brief>` (`review_check lint` is red on main from reviews/87/owner.md, outside this lane: say so if it is) and `python3 -I -B governance/checks/surface_guard.py diff --range <that commit>..build/definer/p002-fix-11 --branch build/definer/p002-fix-11`. Return the six-part contract.
