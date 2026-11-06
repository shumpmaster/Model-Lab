Verdict: PASS

*The Reviewer on pull request #60 (R1), brief 104 (docs/briefs/104-reviewer.md, on branch claude/chief-of-staff-p001-build-5m9j1d) for round 1 and brief 105 for round 2: the confirmation the owner's ruling A requires (decisions/questions/P-001-harness-landing.md), that the re-signed harness is byte for byte what passed at round 3 (reviews/S-001/_reviewer-build.md); a resumed session on a different model from the Builder. Recorded verbatim by the Orchestrator, 2026-11-06. The first line is the latest round's verdict; round 1's was FAIL.*

## Round 1 (commit c39ca7b)

Reviewed: the copy /tmp/claude-0/-home-user/743e981a-6eb1-53c9-aeeb-160d58f19e05/scratchpad/fix-land at c39ca7b (branch orch/p001-e003-harness: the merge of build/builder/e003-harness-signed onto the default branch at 691ec04). Nothing in it was changed (PYTHONDONTWRITEBYTECODE=1; `git status` clean). The content is byte for byte what I passed at round 3, and the three re-signed commits are exactly what the ruling asked for; the one defect is in the landing merge commit's own record form, which a governance check the landing route runs refuses. It is reparable without touching any content.

### 1. The three pairs

| Original | Re-signed | Tree | Parent | Message |
|---|---|---|---|---|
| 3861b38 | 87a9a0c | same, 01f886c4946a46fc4f9ff4944e5fb69c9097e0c6 | both ed35668 | differs only at its `Agent-Session:` line |
| a42c2df | 9c16256 | same, 79db2976062b929898acccf9d2bab11534279620 | 3861b38 → 87a9a0c | differs only at its `Agent-Session:` line |
| 9caff21 | f7071b0 | same, fc62be78a5b4384cbdf644f4940425b1bffae356 | a42c2df → 9c16256 | differs only at its `Agent-Session:` line |

In each pair `git rev-parse <old>^{tree}` equals `<new>^{tree}`, so every file is byte for byte the same; `git diff --stat 9caff21 f7071b0` is empty. The chain is 87a9a0c (parent ed35668) → 9c16256 → f7071b0, in that order, and ed35668 is an ancestor of 87a9a0c. Each re-signed commit is by `builder <builder@agents.invalid>` as author and committer, and `diff` of the two messages shows one line changed per pair: `Agent-Session: session_01QBwHGNGKXFwvVVdzkei5aT` → `Agent-Session: session_01QBwHGNGKXFwvVVdzkei5aT/builder-90`; the `Spec: S-001` trailer and every other line are unchanged.

### 2. The landing merge

HEAD c39ca7b: two parents, first 691ec04 (the default branch), second f7071b0; author and committer `orchestrator <orchestrator@agents.invalid>`; message "Land Build-2, the fair test's harness scripts, re-signed on the owner's ruling A, after the Reviewer's pass at round 3" with an `Agent-Session:` trailer. `git log 691ec04..HEAD` holds exactly four commits: the merge and 87a9a0c, 9c16256, f7071b0; nothing else. The tree: `git diff --name-only 691ec04 HEAD` lists 16 files, all under src/E-003/ (13) and tests/E-003/ (3), 3,845 insertions, no deletions; `HEAD:src/E-003` and `HEAD:tests/E-003` are the same tree objects as `9caff21:src/E-003` (5c5da622...) and `9caff21:tests/E-003` (2e2fcc6c...); 691ec04 holds neither folder; `git diff --quiet 691ec04 HEAD -- . ':!src/E-003' ':!tests/E-003'` reports no other difference. So the tree is the default branch's with 9caff21's src/E-003/** and tests/E-003/** added, and nothing more.

### 3. The suites and checks on the copy

- Locked suite: `python3 -m unittest discover -s tests/acceptance -p 'test_*.py'` → Ran 228, OK (skipped=2, the J7/J8 recorded-manifest tests, by design). This is the corrected AC2 research test (landed at 284008b, PR #57) against the re-signed harness: the whole suite passes.
- Builder's tests: `python3 -m unittest discover -s tests/E-003 -p 'test_*.py'` → Ran 25, OK.
- `python3 governance/checks/surface_guard.py diff --range 691ec04..HEAD` → "OK: 4 commit(s) in 691ec04..HEAD checked (1 merge(s) skipped, 0 exempt, 0 human)". The session-id finding of Brief 100 (one session writing both checks and code) does not arise here: the Builder's commits now carry the `/builder-90` label and the Check author's commit is in the base.
- `bash governance/checks/check_all.sh . 691ec04` → 24 steps PASS, 1 FAIL: `record_checks merges --base 691ec04` (exit 1); "Governance checks FAILED." Detail: "commit c39ca7ba875f by orchestrator (no Item: trailer) changes src/E-003/analyse.py, src/E-003/block.py, ... outside status/**, dispatch-log/** and queue/**". The same with `--branch orch/p001-e003-harness` (the skip applies only to item/ and build/ branches).

### Findings

1. BLOCKING — the landing merge commit c39ca7b is not in the form the merges check accepts, so the landing's own check run fails. governance/checks/record_checks.py:26-33 (record-merges, D-067): each first-parent commit by `orchestrator` either carries an `Item:` trailer, and then has two parents, its second parent being its `Item-Tip:` commit, with the item's required reviews bound to that tip, or touches only status/**, dispatch-log/** and queue/**; :525-541 (the check), :544-550 (`merge_problems`). c39ca7b carries only `Agent-Session:`, no `Item:` or `Item-Tip:`, and changes src/E-003/** and tests/E-003/**. Reproducing case: `python3 governance/checks/record_checks.py merges --base 691ec04 --root .` on the copy → "FAIL: 1 violation(s)". AGENTS.md §4 has a change merge only after the full suite and the checks, and the check is enforced (the step prints FAIL, not WARN). The repair touches no content: remake the merge commit with the same two parents and tree, adding `Item: <the item id>` and `Item-Tip: f7071b0265f68c0b953479e7051c3c00f54505ec` (`orch.ITEM_RE` form), with this review recorded against that tip; the earlier landing of the AC2 correction (284008b, by orchestrator, no `Item:` trailer, changing tests/acceptance/**) has the same form, so how landings are to carry D-067's trailers is a standing question for the Orchestrator, not one this pull request introduced. Nothing else in this review changes once the merge commit is remade; only this finding needs re-checking.

No finding on the content. The round-3 PASS on 9caff21 stands for 87a9a0c, 9c16256 and f7071b0: their trees are the trees I reviewed, the locked suite and the Builder's suites pass on the landed tree, and the surface guard passes the range. It does not yet stand for the landing as a whole, since item 3's check run does not hold.

### Six-part contract

- Changed (by file): nothing; the Reviewer holds no write lane. No fixture was needed; every check ran read-only on the copy.
- Why: confirmation that the re-signed harness is byte for byte what passed at round 3, and review of its landing merge, as Brief 104 dispatched under the owner's ruling A on decisions/questions/P-001-harness-landing.md.
- Verified (command + output): tree ids, parents, authors and message diffs for the three pairs; the merge's parents, commit list (`git log 691ec04..HEAD`, 4 commits), path list and per-folder tree ids against 9caff21 and the default branch; the locked suite (228 OK, 2 skips); tests/E-003 (25 OK); the surface guard on 691ec04..HEAD (OK); check_all.sh (24 PASS, 1 FAIL) and the failed step rerun alone with its detail and with `--branch`.
- Undone: nothing the brief asked. The `Item:` form a landing should carry was read from the check's text, not tried, since remaking the merge is the Orchestrator's lane.
- Needed outside this surface: the Orchestrator remakes c39ca7b with `Item:` and `Item-Tip:` trailers (same parents, same tree) and binds this review to f7071b0, or records why record-merges does not apply to a Builder landing (governance/enforcement.toml is the place a warn-only reading would have to live; the step is enforced today).
- Open questions: how 284008b (PR #57's landing, the same form) passed its landing checks, and whether the `Agent-Session: <session>/builder-90` label should be the standing form for every helper's commits (the Check author's daa44a3 still carries the bare session id).

## Round 2 (commit c39ca7b, the merges check read as CI reads it)

Reviewed again: the same fixed copy /tmp/claude-0/-home-user/743e981a-6eb1-53c9-aeeb-160d58f19e05/scratchpad/fix-land at c39ca7b, unchanged; the CI-style run was made in a fresh clone under /tmp/claude-0/-home-user/743e981a-6eb1-53c9-aeeb-160d58f19e05/scratchpad/review-cases/r5/ci.

### 1. The merges check read the way CI reads it

- .github/workflows/governance.yml:79-84: on a `pull_request` event HEAD is GitHub's merge ref, and when it has two parents the base is set to `HEAD^1`, so check_all.sh runs with the base equal to the commit the pull request was merged onto. governance/checks/record_checks.py:519 walks `rev-list --first-parent --reverse <base>..HEAD` and judges only those commits; :528-541 apply the `Item:` rule only to a commit whose author id is `orchestrator` (`agent_id()`, govlib.py:760-765, which is None for a GitHub-authored merge).
- Reproduction: in a new clone of the copy, checked out at 691ec04, `git -c user.name=GitHub -c user.email=noreply@github.com merge --no-ff c39ca7b` → merge f7fef82 with parents 691ec04 and c39ca7b (first parent 691ec04, as GitHub's merge ref has), its tree the same as c39ca7b's (f23576b7...). `git rev-list --first-parent HEAD^1..HEAD` holds only f7fef82; c39ca7b sits on the second parent. `python3 governance/checks/record_checks.py merges --base 691ec04f6028bd6a4bae208301c439a526efdad5 --root .` → "NOTE: 1 first-parent commit(s) in 691ec04...HEAD, 0 item merge(s), 0 asks-merge merge(s)"; "OK: every merge and Orchestrator commit on the first-parent line holds"; exit 0. `bash governance/checks/check_all.sh . 691ec04f...` on that clone → "OK: all governance checks passed." This matches pull request #60's CI run as reported, and explains #57's landing (284008b) passing in the same form.

### 2. Whether brief 104's finding 1 stands

It does not stand as a blocking finding against this landing. My run applied the merges check to the landing branch's own first-parent line, on which c39ca7b is the first-parent commit; the check's text (record_checks.py:26-34) says it judges the default branch's first-parent line, and the owner merges pull requests on GitHub, so the commit that reaches the default branch's first-parent line is GitHub's merge, authored by GitHub, which the check does not judge; c39ca7b lands on a second parent, where the check never reads. The check as CI runs it passes on this landing, and so does check_all.sh in full. Finding 1 is withdrawn as blocking and restated below as an observation about the check's reach, not about this pull request. Nothing else in the brief 104 return changes: the three re-signed commits are byte for byte the trees I passed at round 3 (87a9a0c, 9c16256, f7071b0, chained on ed35668, messages differing only at `Agent-Session:`), the landing brings in exactly those three and nothing else beside 691ec04, its tree is the default branch's with 9caff21's src/E-003/** and tests/E-003/** added, the locked suite (228, OK, 2 by-design skips) and tests/E-003 (25, OK) pass on it, and `surface_guard diff --range 691ec04..HEAD` is OK. My round 3 PASS on 9caff21 stands for this landing.

### Findings

1. Not blocking (an observation on the check, withdrawn as a finding against the landing) — D-067's `Item:`/`Item-Tip:` binding of reviews to the merged tip is not exercised by a landing in this form: the Orchestrator's landing merge c39ca7b sits on the second parent of GitHub's merge, where record_checks.py:519 never looks, and GitHub's merge itself has no agent id, so the only binding of this review to the landed tip is `review_check pr 60` (reviews/60/reviewer.md). A local run of `record_checks merges` on an `orch/` branch gives a FAIL the default branch will not (the skip at :513 covers `item/` and `build/` branches only); the Orchestrator's local use of check_all.sh on an `orch/` landing branch should expect that, or the skip should name `orch/` too. Open question for the Chief of Staff, outside this pull request.

### Six-part contract

- Changed (by file): nothing; the Reviewer holds no write lane. The CI-style clone and merge are under /tmp/claude-0/-home-user/743e981a-6eb1-53c9-aeeb-160d58f19e05/scratchpad/review-cases/r5/ci only.
- Why: round 2 of brief 104, rerunning the merges check as CI runs it, as Brief 105 dispatched.
- Verified (command + output): governance.yml:79-84 and record_checks.py:511-541 read; a GitHub-style merge of c39ca7b onto 691ec04 made in a fresh clone (parents and tree checked); `record_checks.py merges --base <HEAD^1>` on it (OK, exit 0) and `check_all.sh . <HEAD^1>` (all PASS); brief 104's content, suite and surface-guard results unchanged on the same copy.
- Undone: nothing the brief asked.
- Needed outside this surface: the Orchestrator records this return beside brief 104's in reviews/60/reviewer.md so `review_check pr 60` finds the verdict; the Chief of Staff considers whether record-merges should skip `orch/` branches or whether landings should carry `Item:`/`Item-Tip:` on the second-parent merge so D-067's binding is read (finding 1).
- Open questions: whether the `Agent-Session: <session>/builder-90` label becomes the standing form for every helper's commits (the Check author's daa44a3 still carries the bare session id), as noted in brief 104.
