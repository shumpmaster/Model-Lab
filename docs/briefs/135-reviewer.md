# Brief 135 — reviewer — the upgrade to model 3.7.2 (pull request #71)

session: session_01QBwHGNSLmSrYQgS6BPjV8p
model: the Reviewer ran on a different model from the change's writer, the Chief of Staff's session (D-056). Model names are kept out of this record by this session's own standing instructions, which bar model identifiers in anything pushed to a repository; they are in the session's transcript (LL-70).
start: Model-Lab@51bc9dce2c0e2736ea796b7dc6acad16469c5d7b (worktree /home/user/ml-sync, branch orch/model-sync-3-7-2); Personal-Org-Operating-Model@a1706c2790108f5d4b1e87c745ab99c013691dce; read live, not from a fixed copy
manifest: none
recorded: after hand-out, 2026-11-08, backfilled from the exact text the session sent, because no record was written at hand-out (LL-70)

## Brief
You are the Reviewer under the AI Build Operating Model. Try to refute one change; never fix it.

The change: the git worktree /home/user/ml-sync, branch orch/model-sync-3-7-2, two commits on top of origin/main (`git -C /home/user/ml-sync log origin/main..HEAD`, `git -C /home/user/ml-sync diff origin/main..HEAD`). It upgrades the Model-Lab repository from operating-model version 3.6.0 to 3.7.2.

What it must do (its standard):
- The owner's ruling: option A of /home/user/Model-Lab/questions/P-002-route.md ("Upgrade now, then start"), as that card describes the upgrade.
- The sizing record it must match: /home/user/Model-Lab/intake/P-002-upgrade-footprint-2026-11-08.md (20 files: 18 changed, 2 added; .claude/agents/critic.md and docs/PROJECT.md kept unchanged).
- Its own ledger entry, L-0008 in docs/LEDGER.md of the worktree.
- The operating model's sources: /home/user/Personal-Org-Operating-Model at commit a1706c2 (tools/ and template-v3/), CHANGELOG.md 3.7.0–3.7.2; the 3.6.0 commit is 3a2606a. A precedent: Service-Desk's L-0022 and L-0023 in /home/user/Service-Desk/docs/LEDGER.md.
- The repository's rules: /home/user/ml-sync/AGENTS.md and governance/SURFACES.md (lanes: governance/**, .github/**, intake/** are the chief-of-staff's; .claude/**, docs/** the orchestrator's).
- It must not disturb the prompt engine (P-001): its plan docs/PROJECT.md, experiments/, specs/, tests/, held-back records (governance/HOLDOUTS.md), and the files experiment E-003 reads (experiments/E-003.md:31; governance/PACKS.toml's S-001-analysis and S-001-holdout roles).

Check at least: every copied file is byte-identical to the model's copy at a1706c2 (`git -C /home/user/Personal-Org-Operating-Model show a1706c2:<path> | cmp - <file>`); PACKS.toml and SURFACES.md hold exactly the model's 3a2606a→a1706c2 change plus this repository's own lines, unchanged; no file outside the sizing record's list changes except the ledger, lessons log and generated digest; critic.md, docs/PROJECT.md, experiments/, specs/, tests/ and governance/HOLDOUTS.md are untouched; file modes are unchanged; each commit's author is in the lane for its files; then run `cd /home/user/ml-sync && python3 -m unittest discover -s tests/acceptance -p 'test_*.py'`, the same for tests/E-003, and `governance/checks/check_all.sh .` (note: an orchestrator commit on the branch's own first-parent line makes `record_checks merges` fail until it is merged; judge it on a simulated merge if you can, read-only, or say so). Also judge whether L-0008 says truly what was done.

Return, first line exactly `Verdict: PASS` or `Verdict: FAIL`, then numbered findings with file and line, each blocking or non-blocking, then what you verified (command + output), then open questions.

## Outcome
PASS (reviews/71/reviewer.md)
