Verdict: PASS

*The Reviewer on pull request #87 (R3), brief 228 (docs/briefs/228-reviewer.md, written as brief 129 and renumbered after, since 129 was taken on main), at commit cb9882c; a session on a different model from the change's writer (asked claude-fable-5-1, served claude-fable-5-2). Recorded verbatim by the Orchestrator, 2026-11-09. After the pass, on findings 2 and 5, the Orchestrator changed only the check's usage text and the brief record's number and model line; the landing's records and the check's code are as reviewed.*

## Round 1 (commit cb9882c)

Both parts hold: I could not refute the holdouts check fix or the week-1 landing. No finding is blocking; six are carried as risks or open points. The reviewed copy is unchanged (`git status --short` empty, HEAD still cb9882c).

All commands ran in throwaway clones under `/tmp/claude-0/-home-user/9a06fe22-60e0-580d-8926-30c8a46558b9/scratchpad/rv/` (`tm` = test merge of cb9882c onto e1e96d7, `cases` = my synthetic histories), with `PYTHONDONTWRITEBYTECODE=1`.

### What ran

| Check | Result |
| --- | --- |
| `python3 -m unittest discover -s tests/acceptance -p 'test_*.py'` | `Ran 228 tests ... OK (skipped=1)`, exit 0 |
| `python3 -m unittest discover -s tests/E-003 -p 'test_*.py'` | `Ran 25 tests ... OK`, exit 0 |
| `governance/checks/check_all.sh . HEAD^1` on the test merge | exit 0, `OK: all governance checks passed.`; `PASS v3_checks holdouts --base HEAD^1` with `NOTE: governance/HOLDOUTS.md unchanged in HEAD^1..HEAD` |
| `surface_guard.py diff --range e1e96d7..cd30da6 --branch claude/s-001-built-work-t14hmx` | `OK: 6 commit(s) ... checked (0 merge(s) skipped, 0 exempt, 0 human)`, exit 0 |
| `export.py verify` | not run: there is no `src/E-003/exports/` and no INDEX, as brief 124 step 3 allows |

The test merge's tree equals cb9882c's. The landing merge is 06bf9c5; its second parent is cd30da691646f12fc0501be5bf94e0631c96d51c, the tip of `origin/claude/s-001-built-work-t14hmx`.

One set-up point: the source repository is shallow, and a plain local clone drops `.git/shallow`. My first `check_all.sh` run failed in `surface_guard diff` with `error: Could not read 8001049c...`. I copied `/home/user/Model-Lab/.git/shallow` into the throwaway clone's `.git` and reran; that second run is the result above.

### Part 1: the holdouts check, old (e1e96d7) against new (cb9882c)

Each case ran as `python3 <old|new>/governance/checks/v3_checks.py holdouts --base <base> --root .`, script at `/tmp/claude-0/-home-user/9a06fe22-60e0-580d-8926-30c8a46558b9/scratchpad/rv/run_cases.sh`.

| Case | Old exit | New exit |
| --- | --- | --- |
| A1 test merge of the whole branch, base main | 1 | 0 (unchanged) |
| A2 the landing merge 06bf9c5 alone, base its first parent | 1 | 0 |
| B #69's merge 3b3e4cb, base its first parent | 0 (recorded by L-0007) | 0 (same) |
| C direct change, no ledger entry | 1 | 1 |
| D change on a side branch, merged `--no-ff`, no ledger entry | 1 | 1 |
| E as D, plus a ledger entry `holdouts: changed` | 0 | 0 |
| F change then revert, both on the first-parent line | 1 | 1 |
| **G change then revert on a side branch, merged** | **1** | **0** |
| H the merge commit itself edits the file | 1 | 1 |
| I changed branch is the first parent, main merged into it | 1 | 1 |
| J stale branch (pre-#69) merges main into itself, base main | 1 | 1 |
| J2 that branch then landed on main by merge | 1 | 0 |
| L stale branch (pre-#69) edits the file, landed by merge | 1 | 1 |
| M landing merge resolved to the stale side's file (drops the S-001-built-1 line) | 1 | 1 |
| N mode change only | 1 | 1 |
| O file deleted | 1 | 1 |
| P renamed away and back in two commits | 1 | 1 |
| Q stale branch tip, base main tip, no merge | 1 | 1 |
| R octopus merge, change on the third parent | 1 | 1 |
| T change two merges deep, landed | 1 | 1 |

- **Your four cases reproduce** (A, B, C, D).
- **Why no net change can be missed:** if no first-parent commit differs from its first parent, HEAD's file equals the file at an ancestor of the base, and the kept base-against-HEAD blob comparison covers that remainder (cases J and Q).
- **CI fits:** `.github/workflows/governance.yml` uses a base that is the first parent of the merge it checks.
- **The differences from the old check** are A1, A2 and J2 (the intended ones) and G (finding 1).

### Part 2: the landing

- **Commits:** all 6 are by `builder <builder@agents.invalid>`, each with `Agent-Session: session_01QBwHGN9msBbxxLA7UJmFtP/builder-113` and `Spec: S-001`, no model name or co-author line. They touch only five files under `src/E-003/records/built/`, and `git diff 06bf9c5^1 06bf9c5` shows exactly those five.
- **K1 lines:** listing first (22:21:25Z, sheets repository absent); `k1-i: refused`, `k1-ii: refused`, `k1-iii: returned 1 events` with no event text; `k1: fail`; then the limit line, which matches brief 113's text byte for byte. The ruling file it names is on main. No other line starts `k1-`, every line is `<UTC time> <line>`, and times are in order.
- **Seed before the opening:** `seed.md` is `2026-11-07T22:22:37Z seed: 4076695088` (below 2^32), committed in 6514023 at 22:22:43Z. The opening is 22:52:38Z.
- **Opening time:** I reran `kind.py can-open` at each commit of `git log --reverse e1e96d7 -- reviews/E-003/built/sheet.md governance/HOLDOUTS.md`. 82177da is not eligible; 98d2d93 (committer date 2026-11-07T22:52:38+00:00) is the first eligible one, with set S-001-built-1 and fingerprint ee47900c... `opened.md` matches.
- **Scan:** main at each of the three scan times (32ef018, 3154dc5, 81cecc5) holds the same 7 `docs/briefs/<n>-builder.md` files, so "7 found" and "0 new" twice hold. Rerunning `pair.py entry` gives the recorded reasons for 04, 24 and 25. It gives `eligible` for 103, 90, 92 and 97 with the recorded dispatch times; each names S-001 or E-003, so brief 113's stricter reason applies. `scan.tsv` has six tab-separated fields per line.
- **Service-Desk:** all 85 control files at e0ea284 have roles researcher, source-checker or critic-triage, none builder. A fresh fetch of its main into a scratch repository shows 0 control files added up to 2026-11-09T18:41:11Z.
- **counts.json:** `{"runs": 0, "tokens": 0, "pairs_collected": 0, "pairs_left_out": 0}`, the keys `counts.py` reads. No pair or helper was started.
- **S-001 AC2, AC3, J3 and E-003:** records without a brief or start commit are listed and do not enter (AC2; Exclusions 6). There are no pairs, so AC3, Exclusions 1 to 5 and 7, and Sample's run counts have nothing to test. There are no exports, so J3 has nothing to test.
- **sessions.md against brief 124 steps 1 and 2:** the weekly task id and next fire time are recorded. The wake was queued 20:43:20Z for 20:43:00Z, so `k7: pass` holds. Listing, fetch and marker are recorded; the marker was present, so no `k5` line is due. No K1 probe is due (no review point, no analysis dispatch).
- **k1-records.md against step 3:** it gains exactly the one `session-*.md` path the landing brings.
- **Join-up review:** this project has no screens or views. The parts working together are covered by the test merge runs above.

### Findings

1. **Non-blocking, carried as a risk: a change made and undone on a merged side branch no longer fails.** Case G:
   ```
   G change+revert on a side branch, merged   old exit 1 | governance/HOLDOUTS.md changed in 8307ea6..HEAD, but no ledger entry ...
   G change+revert on a side branch, merged   new exit 0 | NOTE: governance/HOLDOUTS.md unchanged in 8307ea6..HEAD
   ```
   `git rev-list --first-parent 8307ea6..HEAD -- ./governance/HOLDOUTS.md` lists nothing; `--full-history` lists 2d9c127 and 322861a. This is within the ruling record's wording ("each commit on the first-parent line is compared with its first parent"), and the file never differs on the landing line. But on a pull-request run HEAD is the merge commit, so every commit of the pull request is on the side: there the check now sees only the net effect. The owner should know the ruling carries this.

2. **Non-blocking: the check's usage text is now out of step.** `governance/checks/v3_checks.py:70-72` still says "any commit touches it, or it differs between REF and HEAD". Case G is a commit that touches it and passes.

3. **Non-blocking: no test covers `check_holdouts`.** `grep -rn "check_holdouts\|v3_checks.*holdouts" tests/` finds nothing, before or after the change. The first-parent behaviour on this R3 path rests on the four recorded cases and mine, not on a locked check.

4. **Non-blocking: two work-session turns have no `listing:` line.** Brief 113 step 5 says "Every turn (every wake), in this order: step 1's listing". The turns at 2026-11-08T19:16:36Z and 19:16:52Z (commits 565dde8, a4a1aa2) record only `hook:` lines. Both were owner-message turns, not wakes; S-001 requires the listing at every wake, and every wake has one. K6's "no listing has shown the sheets repository attached" still holds on the listings recorded.

5. **Non-blocking: no Reviewer brief record for this review is in the copy.** Brief 124 step 3 says "Write a Reviewer brief (docs/briefs/, the next number)". `ls docs/briefs | sort -n | tail -1` gives `227-critic.md`, and the copy's tree is clean. Also, brief 124's model line names claude-fable-5-1 for its Reviewer helpers; this session is served claude-fable-5-2. That is still a different model from the builder's (D-056), but the record should say what ran.

6. **Non-blocking: the landing merge and the k1-records line are committed before this verdict.** Brief 124 step 3 puts both "On PASS". Commits 06bf9c5 and cce423e already exist; they are not pushed (`origin/claude/p-001-model-lab-continue-ohykg9` is at 7ea573a), so nothing has landed ahead of review. They should be pushed only with this return recorded.

### Six-part contract

- **Changed (by file):** nothing. No file in the reviewed copy or any repository was edited. Throwaway clones and one script exist only under `/tmp/claude-0/-home-user/9a06fe22-60e0-580d-8926-30c8a46558b9/scratchpad/rv/`.
- **Why:** reviewer role; refute the check fix against the owner's ruling (decisions/questions/P-001-holdouts-check-merges.md, L-0009) and the week-1 landing against brief 113, S-001 AC2, AC3 and J3, E-003 Steps 2 and 3, Exclusions and Sample, and brief 124 steps 2 and 3.
- **Verified (command + output):** as in "What ran" and the two parts above.
- **Undone:**
  - `review_check` with a pull request number was not run, as no pull request exists yet. The check path is R3, so the owner's verdict file is still needed (governance/risk-paths.toml).
  - No pull request body was given, so its Tasks section was not read.
  - The work session's hook, its trigger and its `list_events` call are outside any repository and cannot be checked from here.
- **Needed outside my surface:**
  - Record this return verbatim in reviews/<PR>/reviewer.md.
  - Add the Reviewer brief record (finding 5).
  - Decide whether to correct the usage text and add a test for the check (findings 2 and 3).
  - Report the first-parent change for the operating model's own copy, as the ruling record says.
- **Open questions:**
  1. Does the owner accept finding 1's narrowing on pull-request runs, or should the check also walk the commits a merge brings in when the merge base's file equals the first parent's? That would keep case G failing and still pass the weekly landing.
  2. Should brief 113's "every turn" listing bind owner-message turns, or only wakes (finding 4)?
  3. `opened.md` gives the opening as 98d2d93's committer date (22:52:38Z), as brief 113 step 6 words it; that commit reached main with #69 at 23:09:09Z. No piece was dispatched in between, so nothing turns on it now. Do the judging brief's review points use the same time?
