# Brief 129 — reviewer — the holdouts check fix and the first weekly landing (R3)

session: session_01QBwHGNPFytF6t2VG6mnugn
model: claude-fable-5-1 (the change's writer, the Chief of Staff and Orchestrator in the Chief of Staff's session, runs on claude-opus-5-5; the work session's builder too; D-056). A new Reviewer session.
start: Model-Lab@cb9882c86c167674aea3ce1044e38403d67c43bb (fixed copy /tmp/claude-0/-home-user/9a06fe22-60e0-580d-8926-30c8a46558b9/scratchpad/fix-71, branch claude/p-001-model-lab-continue-ohykg9), against main at e1e96d74272f84cb1a83e0ed9896816a9c00075c
manifest: none. This brief records no pack manifest of its own, so neither S001_BLIND_MANIFEST (J8) nor S001_ANALYSIS_MANIFEST (J7) is set for it.
recorded: at hand-out, 2026-11-09 (LL-04, LL-24)

## Brief

Review the change in /tmp/claude-0/-home-user/9a06fe22-60e0-580d-8926-30c8a46558b9/scratchpad/fix-71 against main (e1e96d74272f84cb1a83e0ed9896816a9c00075c): `git diff e1e96d74272f84cb1a83e0ed9896816a9c00075c HEAD` and `git log --format='%h %an %s' e1e96d74272f84cb1a83e0ed9896816a9c00075c..HEAD`. It holds two things.
1. **The holdouts check fix**, on the owner's ruling (decisions/questions/P-001-holdouts-check-merges.md; ledger L-0009): in governance/checks/v3_checks.py, `check_holdouts` follows `--first-parent` in place of `--full-history`. Try to refute that it still catches every change to governance/HOLDOUTS.md that reaches the branch, on a merge or not, and only stops reading a merge as a change when the file is unchanged against its first parent. The Orchestrator ran four cases (the landing passes; #69's merge, recorded by L-0007, passes; a change with no ledger entry fails; the same change on a merged side branch fails); run your own.
2. **The first weekly landing** under docs/briefs/124-orchestrator-landing.md, step 3: the merge of the work session's branch claude/s-001-built-work-t14hmx (brief 113), its records only, no exports yet. Try to refute it against brief 113, S-001 AC2, AC3 and J3, and E-003 Steps 2 and 3, Exclusions and Sample: `python3 governance/checks/surface_guard.py diff --range e1e96d74272f84cb1a83e0ed9896816a9c00075c..<the merge's second parent> --branch claude/s-001-built-work-t14hmx`, each record's content against brief 113's steps (the K1 lines and limit line, the seed before the opening, the opening time, the scan and its reasons, counts.json's form), reviews/E-003/built/sessions.md and k1-records.md against brief 124 steps 2 and 3.
Run the full suite and `governance/checks/check_all.sh . HEAD^1` on a test merge of the branch onto main, outside this copy. Change nothing in the copy (PYTHONDONTWRITEBYTECODE=1).

Return: first line `Verdict: PASS` or `Verdict: FAIL`; numbered findings, each blocking or not, with the command and output that shows each; the six-part contract.
