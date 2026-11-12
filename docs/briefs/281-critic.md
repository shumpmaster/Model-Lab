# Brief 281 — critic — the focused confirmation review the owner chose at the plan stop (P-002, M9)

session: session_01QBwHGNPKhVy6fgoUjKtW6q
model: the Critic runs on a different model from the plan's writer, the Definer (D-056), in a fresh session. Model names are kept out of this record by this session's standing instructions (LL-70).
start: Model-Lab@4a03208bd7d1f757132a4a004766f265f16d5ea4 (the Definer's commit on brief 280, branch build/definer/p002-plan-stop-fix), read from a fixed copy at /home/user/ml-fixed-281
manifest: the fixed copy; the owner's answer, intake/P-002-owner-plan-stop-answer-2026-11-12.md, and the card, questions/P-002-plan-stop.md (option A); reviews/S-002/plan.md (rounds 1 to 3 and the re-check); docs/briefs/280-definer.md; specs/S-002.md; experiments/E-004.md, line.py and line-output.txt; docs/gates/P-002/trial-terms.md
recorded: at hand-out, 2026-11-12

## Brief
You are the Critic (plan review, D-043). Read from the fixed copy only; write nothing. Your return is recorded verbatim in reviews/S-002/plan.md as the focused confirmation review. The owner chose option A at the plan stop: "A: focused fix (Recommended)". This is the one check that option allows; a FAIL goes back to the owner. Check only what the Definer's change on brief 280 (commit 4a03208bd7d1f757132a4a004766f265f16d5ea4) touched:
1. that the re-check's findings 1 to 9 are fixed as option A and the findings state them, in particular the refill of void and duplicate entries from the spare places, the one limit of three a look, "a place left empty", the share-based lean, and the stated limit on sides known ahead;
2. that the change made nothing else false and opened no route to steer a trial or the hand check once the sides are known; re-read the entry, void, withdrawal, reserve, wait and count rules end to end;
3. that S-002 lines 18 to 54 and the table at 76 to 95 are unchanged in content, and no figure from line-output.txt changed;
4. the Definer's two open points: a result that changes with how an empty place is filled stops the trial and goes to the owner (its own design); and the Orchestrator writing void lines itself, re-checked by the judging Reviewer.
A finding about text the change did not touch is out of scope unless the change makes it false. Rate a finding blocking only if it makes the plan wrong or lets a trial or the hand check be steered.

Return first a column-0 line `Verdict: PASS` or `Verdict: FAIL`, then numbered findings each marked blocking or not, each with file, line and a fix, then the six-part contract.
