# Handoff — the prompt engine (P-001), 5 November 2026, tenth stopping point

*Written by the Chief of Staff (session_01QBwHGNGKXFwvVVdzkei5aT). It follows docs/handoff/2026-11-04-chief-of-staff-9.md.*

## Where it stands
- **PRs #51 and #53 are merged** (13:25); main's questions/ held only the template (LL-30). The full governance check on main passes once the clone has full history (LL-63: run `git fetch --unshallow origin` in Model-Lab too).
- **Build-2 is built and its review passes, but it cannot land yet.** The Builder (claude-opus-5-5; briefs 90, 92, 97) built the harness scripts under src/E-003/ on build/builder/e003-harness: 3861b38, a42c2df, 9caff21 (pushed as-is to origin to keep it; not merged anywhere). The Reviewer (claude-fable-5-1; briefs 91, 96, 98) failed rounds 1 and 2 and passed round 3, the last build round (reviews/S-001/_reviewer-build.md). The Builder's returns are in docs/reports/2026-11-05-e003-harness-return*.md, outside the Reviewer's pack.
- **One locked check fails a correct build**: the research case in tests/acceptance/test_ac02_pair_start.py:94-100 compares the briefs without setting each copy's path aside. The Builder found it and the Reviewer confirmed it in all three rounds. **PR #54** (branch cos/p001-ask-ac2-test) files the question; the Critic (claude-sonnet-5-5; briefs 93-95) passed it at round 3. No default: correcting a locked check sets aside the owner's own words (intake/P-001-owner-instruction-2026-11-05.md). 228 locked tests: 225 pass, this one fails, J7 and J8's recorded-manifest tests skip by design.

## Next, in order
1. Check the live state of #54 (LL-11). Once it merges, open the answer pull request recording the owner's exact words (AGENTS.md §5); then act on the ruling (A or B: brief the Check author with the full case table first, LL-61, and one review that runs every case, LL-60; C: brief the Definer for a superseding spec).
2. **File the trade-offs question** the Reviewer left for the owner, once #54 is answered or beside it. Its items, with the costs the Reviewer measured (reviews/S-001/_reviewer-build.md, round 2 findings 2 to 5, round 3 findings 1 to 3):
   - over-strict readings that cost a pair per hit: path-like text in echo, printf or commit messages; `echo /`; regex literals and `/`-tokens in inline code (4 lines in one of E-001's 14 transcripts); code reading /etc or writing /tmp; a merge of the worker's own side branch; a brief naming /tmp/work;
   - gaps, to close or record as limits: `ls //`; `/.` and `/..` inside quoted text read as leaks; scripts written with Write or Edit are not scanned; paths built in code (HOME lookups, concatenation, variables) are not resolved;
   - the brief record form: pair.py admits a record only when its `recorded:` line starts "at hand-out" (round 1, finding 5); every brief this project writes already does.
   Any change to the build after round 3 needs the owner's ruling, since the stop rule gives no fourth round.
3. Land Build-2 only after the AC2 test is corrected and the full suite passes: merge build/builder/e003-harness into the push branch with `git merge --no-ff`, after `surface_guard.py diff --range` and the suite, in a separate worktree at the exact commit.
4. As before: every brief that records a pack manifest names the setting its check reads (S001_BLIND_MANIFEST for J8, S001_ANALYSIS_MANIFEST for J7) and the Orchestrator confirms the run checked the record, not skipped. The three non-blocking points on the locked checks stay for a later superseding change, by the owner's instruction, unless the owner rules B on #54.
5. The sheets repository: still unconfirmed that the environment does not add shumpmaster/secret-marking to new sessions; the K1 probe settles it before the first sheet.

## Token checkpoint
This session's own usage is not read here. Helpers this session, as reported (resumed helpers' increases only, LL-34): Builder 355,075, 474,630 and 510,540; Reviewer 245,508, 347,728 and 371,399; Critic 62,113, 73,565 and 80,377; 2,520,935 in all. No test runs have been used: the fair test's 732 runs start with the first kind.
