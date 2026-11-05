Verdict: PASS

*The Reviewer on pull request #57 (R3), brief 100 (docs/briefs/100-reviewer.md, on branch claude/chief-of-staff-p001-build-5m9j1d): the one review the owner's ruling A requires, running every case of the corrected AC2 research test (decisions/questions/P-001-ac2-research-test.md); a resumed session on a different model from the test's writer and from the build's. Recorded verbatim by the Orchestrator, 2026-11-05.*

Reviewed: the Check author's commit daa44a3 on f517937, read in the fixed copy /tmp/claude-0/-home-user/743e981a-6eb1-53c9-aeeb-160d58f19e05/scratchpad/combo at 6a958b6 (that commit with the Builder's branch 9caff21 merged in locally so the test can run against the build). Fixtures and broken copies are under /tmp/claude-0/-home-user/743e981a-6eb1-53c9-aeeb-160d58f19e05/scratchpad/review-cases/r4/ (base/: a `git archive` export of 6a958b6; one folder per broken case; break.py: the one-line breakages). Nothing in the fixed copy was changed (PYTHONDONTWRITEBYTECODE=1; `git status` clean).

## 1. The corrected test and the whole locked suite against the real build

- `python3 -m unittest discover -s tests/acceptance -p 'test_ac02*.py' -k test_research_runs` → Ran 1 test, OK.
- `python3 -m unittest discover -s tests/acceptance -p 'test_*.py'` → Ran 228 tests, OK (skipped=2: the J7/J8 recorded-manifest tests, skipped by design while no manifest is recorded; test_j7_analysis_pack.py:149-153, test_j8_holdout_pack.py:165-172). The locked suite passes in full against 9caff21 for the first time; rounds 1 to 3 had this one test failing for the fault the owner's ruling names.

## 2. Broken copies of src/E-003/pair.py, one per case, the corrected test against each

Each copy is the full working tree with one breakage in `cmd_plan` (break.py; the diff per case is one or two lines). "Fails at" names the assertion in the corrected test (tests/acceptance/test_ac02_pair_start.py as of daa44a3).

| Case | Breakage | Corrected test | Fails at |
|---|---|---|---|
| a. C3's paragraph missing | the change arm gets the control brief | FAILS | :106 `assertNotEqual(chg_c, ctl_c)`: the two briefs equal once the copy paths are set aside |
| b. two paragraphs added | C3 plus a second paragraph | FAILS | :108 "exactly one paragraph differs": 3 != 1 |
| c. C3 altered in its first words | "Any source you cannot open..." | FAILS | :109 `startswith("A source you cannot open is not by itself a fault")` |
| d. altered after the first words, inside the asserted prefix | "...is not a fault in the memo" | FAILS | :109 the same `startswith` |
| e. another paragraph changed in the change arm only | "Return a hand-back now." in the change arm | FAILS | :108 "exactly one paragraph differs": 2 != 1 |
| f. changed identically in both arms | "Return a hand-back now." in both | FAILS | :105 "nothing but the path changed in the no-change brief": ctl_c != expected_ctl |
| g. the real path left in both briefs (stray-path refusal disabled, so the comparison is reached) | no replacement | FAILS | :100 `assertNotIn(self.real, a)`: the real path found in the control brief |
| h. left in one (the change arm) | replacement for the control arm only | FAILS | :100 `assertNotIn(self.real, a)`: the real path found in the change brief |
| g2. as g with the build's own stray-path refusal left on | no replacement | FAILS | e003_support.py:96 (`decide`: pair.py plan exited 1, the build's own set-up-fault refusal from round 2) |

Every case the brief names fails the corrected test, as it must. Cases f, g and h fail only through the lines the correction added beyond the `<COPY>` substitution (:100-102, :105): with the substitution alone and the old one-paragraph count, g would pass (both briefs hold the real path, so they still differ by exactly C3) and f would pass; so those added lines carry weight.

One case of my own passes the corrected test and nothing else in the suite catches it: C3's text altered after the asserted prefix (case d2, "Return the memo only for a fault you can show" → "Return the memo for a fault you can show", pair.py after `C.apply`). The corrected test → OK (the prefix at :109 still holds and exactly one paragraph differs); the whole suite on that copy shows only four failures that are artefacts of my copies having no `.git` (test_ac04 `git ls-files`, test_j1 `git status`, test_ac01 and test_j8 `git diff`: all four fail the same way on the unbroken base copy, "fatal: not a git repository"), so no locked test catches a C3 paragraph whose tail is altered in pair.py. This is a limit the research test shares with the built-work test (:81 checks only the prefix "The inputs for this task, by path: "; :82 reconstructs the control brief, not the paragraph's text) and that predates the correction (the old research test's :100 was the same `startswith`); test_j1's text checks cover change.py's output, not pair.py's handling of it. Not a finding against this change, whose scope the ruling fixed to the comparison; recorded as an open question for a later change to the locked checks (comparing the differing paragraph to the frozen change text in full, e003_support.py's C3_TEXT).

## 3. The change against the ruling

- `git diff --name-only f517937 daa44a3` → tests/acceptance/test_ac02_pair_start.py only; the diff is 11 insertions, 2 deletions, all inside test_research_runs_two_source_checks_from_the_checks_start_commit (:94-109). No other test, file or line.
- The replaced two lines (the raw two-brief paragraph comparison, `assertEqual(len(paras), 1)`) become the built-work test's comparison block, lines 71-80 of the same file, transplanted word for word with its variable names (`ctl`, `chg`, `ctl_c`, `chg_c`, `expected_ctl`); the C3 `startswith` line is kept. Line 82 of the built-work test (the reconstruction equality) is not copied. So the change matches ruling A on decisions/questions/P-001-ac2-research-test.md ("its writer changes only the comparison, so it sets each copy's location aside first, as the same file's built-work test already does") and Brief 100's reading of it ("the comparison only, as the same file's built-work test at lines 72-80 does").
- What it adds beyond setting the copy paths aside: the two path assertions (:100-102, the real path absent and the copy path present in each brief) and the control-brief equality (:103-105) and `assertNotEqual` (:106). All four are lines 72-78 of the block the ruling names, so they do not go past it; each checks a requirement the spec sets for every kind (specs/S-001.md:251 AC2, "briefs that differ only by the change paragraph"; :264 J2, the real path "replaced by the copy's path, nothing else changed"; experiments/E-001.md:102), and they are what make cases f, g and h fail. Nothing added is outside lines 72-80 or outside AC2/J2.
- Author and committer `check-author <check-author@agents.invalid>`; the message ends with `Agent-Session: session_01QBwHGNGKXFwvVVdzkei5aT` and `Spec: S-001`. No model names or co-author lines.

## 4. Governance checks

`bash governance/checks/check_all.sh . f517937` on the copy: 23 steps PASS, 2 FAIL, "Governance checks FAILED." Both failures come from the local, unpushed merge 6a958b6 the copy carries so the test can run against the build, not from daa44a3:
- `surface_guard diff --range f517937..HEAD`: "spec S-001: session session_01QBwHGNGKXFwvVVdzkei5aT wrote both checks (check-author) and code (builder)". The range holds the Check author's commit and the Builder's three, and both carry the same `Agent-Session` trailer. On the pull request's own range the guard passes: `python3 governance/checks/surface_guard.py diff --range f517937..daa44a3 --root .` → "OK: 1 commit(s) in f517937..daa44a3 checked (0 merge(s) skipped, 0 exempt, 0 human)". See finding 1.
- `record_checks merges --base f517937`: "commit 6a958b617444 by orchestrator (no Item: trailer) changes src/E-003/analyse.py, ... outside status/**, dispatch-log/** and queue/**". The local merge commit has no `Item:` trailer; the real landing of the Builder's branch will carry one. Not about daa44a3.
Every other step passes (surface_guard check, ledger_check append-only against f517937, digest, governance_checks all, review_check lint, spec_check status/frozen/predates/facts, v3_checks scope/freeze/holdouts/milestones/gates/ready/trace/joins/sessions, record_checks decisions/routing/build-cap/grants, surface_guard charters).

## Findings

1. Not blocking — the Check author's and the Builder's commits carry the same `Agent-Session: session_01QBwHGNGKXFwvVVdzkei5aT` trailer (daa44a3; 3861b38, a42c2df, 9caff21), the top-level session's id rather than each helper's own, so the surface guard reads any range holding both as one session that "wrote both checks and code" for S-001 (governance/checks/surface_guard.py, the session rule; the output above). Case: `python3 governance/checks/surface_guard.py diff --range f517937..HEAD --root .` on the copy → FAIL; `--range f517937..daa44a3` → OK. Not a fault of this change (the trailer form is CLAUDE.md's, and the pull request's own range passes), but the record as written cannot show the Check author and the Builder were different sessions, which is what the guard exists to check (D-006). Open question for the Orchestrator: land the two ranges separately so each guard run holds one role's commits, and consider recording the helper's own id in `Agent-Session`.

2. Not blocking (limit, predates the change) — a build that alters C3's paragraph after its first words passes the corrected test and every other locked test (case d2 above; test_ac02_pair_start.py:109 checks a prefix only, as :81 does for C2). Carried as an open question for a later change to the locked checks, outside ruling A's scope.

No finding against the change itself: it does what the ruling allows and no more, the corrected test passes the real build, fails every broken copy the brief names at a specific assertion, and the pull request's own range passes the surface guard.

## Six-part contract

- Changed (by file): nothing; the Reviewer holds no write lane. Fixtures, broken copies and break.py are under /tmp/claude-0/-home-user/743e981a-6eb1-53c9-aeeb-160d58f19e05/scratchpad/review-cases/r4/ only.
- Why: the review ruling A requires of the corrected AC2 research test (decisions/questions/P-001-ac2-research-test.md), run against the real build and against broken copies, as Brief 100 dispatched.
- Verified (command + output): the corrected test alone (OK) and the whole locked suite (228, OK, 2 by-design skips) on the combo copy; nine broken copies of pair.py each failing the corrected test at the assertion named above, plus one tail-alteration copy it passes, with the whole suite run on it and on the unbroken base to separate real catches from no-`.git` artefacts; `git diff f517937 daa44a3` (one file, one test, lines 71-80's block); the commit's identity and trailers; check_all.sh (23 PASS, 2 FAIL both from the local merge) and the surface guard on f517937..daa44a3 (OK).
- Undone: nothing the brief asked. The locked suite was not rerun with the broken copies inside a git repository, so the four `.git`-dependent tests were judged by their identical failure on the unbroken base rather than by a pass.
- Needed outside this surface: the Orchestrator's landing order and `Item:` trailer for the Builder's branch, so the combined ranges pass the surface guard and the merges check (finding 1); a later locked-check change, with the owner's approval as this one had, if the prefix-only text checks of :81 and :109 are to be tightened (finding 2).
- Open questions: (a) whether `Agent-Session` should carry each helper's own session id so the record itself shows the Check author and the Builder apart; (b) whether the precedent of correcting a locked test under an owner's ruling should name, as this ruling does, that one review must run every case rather than read the change.
