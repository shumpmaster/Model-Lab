Verdict: PASS

*The Reviewer on pull request #128 (R1), brief 356 (docs/briefs/356-reviewer.md, written as brief 352 and renumbered after, since 352 to 355 are taken on another open branch), at commit 3f8d1fc; a session on a different model from the work's and the landing's writers (asked claude-fable-5-1, served claude-fable-5-2). Recorded verbatim by the Orchestrator, 2026-11-23. Commits after the reviewed one add only the brief record, its renumbering, this record and session lines.*

## Round 1 (commit 3f8d1fc)

The third weekly landing holds against brief 113 (steps 1, 5, 6, 7), brief 124 (steps 2, 3), S-001 AC2 and E-003 Step 2. No blocking finding; three non-blocking findings and one open question follow the checks.

Reviewed: `/tmp/claude-0/-home-user/9a06fe22-60e0-580d-8926-30c8a46558b9/scratchpad/fix-w3` at 3f8d1fc6903ba333efa4a9294b37c142227e6f8c (parents 44dbc33 and 2a748d0) against main 32f1010910ca0bc3cf60c6689f8770c50a0ae2b6. All Python was run as `python3 -I -B`.

### Checks that tried to refute it and did not

**A. The landing's shape (brief 124, step 3).**
`git log --format='%h %an %s' 32f1010..HEAD` gives 9 commits: 7 by `builder` (03abfa2, caea79b, 4b82493, 974ac2a, 041d95a, 6b5d1c2, 2a748d0), then 44dbc33 and the merge 3f8d1fc by `orchestrator`.
- `git diff --stat 32f1010 HEAD`: 2 files, 31 insertions, 0 deletions.
  - `reviews/E-003/built/sessions.md` +3
  - `src/E-003/records/built/session-session_01QBwHGN9msBbxxLA7UJmFtP.md` +28
- The landing starts from main: 44dbc33's parent is 32f1010, and last week's tip 4473eea is the merge base, already on main.
- The merge is a true two-parent merge, and `git diff --stat HEAD^1 HEAD` shows only the session file (+28).
- Each builder commit has author and committer `builder <builder@agents.invalid>`, with trailers `Agent-Session: session_01QBwHGN9msBbxxLA7UJmFtP/builder-113` and `Spec: S-001`, and no model name or co-author line.
- Both orchestrator commits carry `Agent-Session: session_01QBwHGNPFytF6t2VG6mnugn`.
- `reviews/E-003/built/k1-records.md` already lists the session file, so there is no new path to add.
- No pair, no export: `src/E-003/exports/built` does not exist, so `export.py verify` does not apply. `scan.tsv`, `counts.json`, `opened.md` and `seed.md` are unchanged.

**B. Surface guard.**
`python3 -I -B governance/checks/surface_guard.py diff --range 32f1010910ca0bc3cf60c6689f8770c50a0ae2b6..2a748d02d715f1254f1d20d83775deb992d15552 --branch claude/s-001-built-work-t14hmx`
→ `OK: 7 commit(s) in 32f1010...2a748d0 checked (0 merge(s) skipped, 0 exempt, 0 human)`, exit 0.

**C. Each wake's lines (brief 113, steps 1, 5, 6, 7).**
Per commit, `git diff <c>^ <c>` adds exactly 4 lines to the session file and removes none: `listing:`, `wake:`, `marker:`, `scan:`.
- Listing: `shumpmaster/Service-Desk, shumpmaster/Model-Lab` at all seven wakes; the sheets repository is never listed.
- Wake arrivals, against the 18:40:00Z schedule: 18:40:35, 18:40:43, 18:41:06, 18:40:33, 18:40:46, 18:40:47, 18:40:35. All are within the hour.
- Marker present, both repositories fetched, hook present, at every wake.
- Each commit's committer date equals its last line's time (18:41:10, :23, :48, :11, :16, :20, :11).
- No added line starts `k1-` (grep count 0).
- Step 6: the kind has been open since 2026-11-07T22:52:38Z (`opened.md`), with no pair started and 0 runs, so no `may-start`, checkpoint or 20-run probe was due.

**D. The scans' "0 new records", checked independently.**
- Model-Lab main: `git diff --name-status 76871f0 32f1010 -- docs/briefs` (76871f0 is main's first-parent tip before the 2026-11-16T18:41:20Z scan) adds only 345-reviewer, 346/347/348-critic and 349/350/351-critic-gate. No `<n>-builder*.md` was added.
- Main holds 7 builder briefs (04, 24, 25, 90, 92, 97, 103), all added 2026-11-03 to 2026-11-06 and all already in `scan.tsv`.
- Service-Desk origin/main (d0bcd6a, read only): `git log --since=2026-11-14 origin/main -- 'reviews/*/_control/*.json'` is empty. The last control file added is `reviews/Q-028/_control/0-54b3043f4cd7.json` on 2026-11-13T05:59:00Z.
- `git diff --name-status 02e5c96 origin/main -- reviews` shows no `_control` path.
- So 0 new records of either form over 2026-11-16 to 2026-11-23 is true.

**E. The Orchestrator's wake (brief 124, step 2).**
44dbc33 adds three lines at 2026-11-23T20:44:58Z:
- the listing, with four repositories and `shumpmaster/secret-marking absent`;
- `wake: scheduled for 2026-11-23T20:43:00Z, queued 20:44:05Z, this turn ran`;
- `marker: present (machine not new); fetched Model-Lab`.

It is within the hour and in the brief's order. `python3 -I -B src/E-003/counts.py due --kind built --side work --runs 0 --run-cards-sent 0 --weeks 2.3 --review-cards-sent 0` → `{"due": false, "reason": ""}`, so no card was owed.

**F. Full suite and check_all on a test merge.**
The throwaway clone is `/tmp/claude-0/-home-user/9a06fe22-60e0-580d-8926-30c8a46558b9/scratchpad/rev-w3-throwaway`, with `.git/shallow` copied in. It holds a `--no-ff` merge of 3f8d1fc onto 32f1010 (e86f8fb), whose tree equals the landing HEAD.
- `python3 -I -B -m unittest discover -s tests/acceptance -p 'test_*.py'` → `Ran 228 tests in 72.448s`, `OK (skipped=1)`, exit 0.
- `python3 -I -B -m unittest discover -s tests/E-003 -p 'test_*.py'` → `Ran 25 tests in 7.552s`, `OK`, exit 0.
- `GOV_BRANCH=claude/s-001-built-work-t14hmx governance/checks/check_all.sh . HEAD^1` (with `PYTHON` set to a wrapper running `python3 -I -B`) → exit 0, all 25 steps PASS, `OK: all governance checks passed.` Its range walk reports `OK: 10 commit(s) in HEAD^1..HEAD checked (2 merge(s) skipped, 0 exempt, 0 human)`. There are no WARN, FAIL or ERROR lines.
- `git status --short` is empty in both the fixed copy and the throwaway; nothing was changed in fix-w3.

### Findings

1. **Non-blocking (a risk to carry, not a defect in this landing's diff): Service-Desk built work this week has no dispatch record of either scanned form, and AC2 says such a piece "does not enter and is listed".**
   - `git -C /home/user/Service-Desk log --format='%h %an %cI %s' --since=2026-11-16T18:41:20Z origin/main` shows six `builder` commits on 2026-11-22:
     - 26001c2 "the baseline adapter"
     - 3085351 "one rule holds or shows each decision card…"
     - cb807a2
     - 9633e9a
     - c67094e
     - 0f9c4bd "the card fix's handover package"
   - They landed as "P-003: the card fix built (S-014), reviewed PASS" (2783b48, #465) and #464.
   - Over the same window no `reviews/*/_control/*.json` and no `docs/briefs` file was added there, and the `dispatch-log/2026-11.jsonl` additions are definer and critic only.
   - The scan as brief 113 step 7 defines it correctly found 0 records, so the work session did what its brief says.
   - The gap is that `scan.tsv` lists no such piece, and nothing in this landing lists it elsewhere.
   - I did not check whether some other record (for example the Chief of Staff's session lines) qualifies under E-003 Step 2's "a brief record by the Chief of Staff that holds all three".

2. **Non-blocking (outside the landing's diff): this review's brief number is already taken on an unmerged branch.**
   - `git -C /home/user/Model-Lab log --all --diff-filter=A --name-only -- 'docs/briefs/35[2-9]*'` shows `docs/briefs/352-reviewer.md` (0d70a39, 2026-11-23T20:45:52Z, on claude/p-001-model-lab-continue-ohykg9).
   - It also shows `docs/briefs/352-definer.md`, `353-definer.md`, `354-critic.md` and `355-definer.md` (613cf45 to dea5479, 2026-11-23T15:11 to 15:21Z) on origin/claude/epic-fermi-f3ehsf, which is 16 commits ahead of main.
   - 352 is the next number on main, but two briefs numbered 352 will meet when both branches land.

3. **Non-blocking: the served Reviewer model differs from the one recorded.**
   - Brief 124 and `docs/briefs/352-reviewer.md` say `claude-fable-5-1` asked; this session's model id is `claude-fable-5-2`.
   - D-056 is still met, since it differs from the builder line's claude-opus-5-5.
   - The verdict record should state the served model.

### Six-part contract

- **Changed (by file):** nothing in the fixed copy or in any repository. In the scratchpad only: the throwaway clone `/tmp/claude-0/-home-user/9a06fe22-60e0-580d-8926-30c8a46558b9/scratchpad/rev-w3-throwaway`, the wrapper `/tmp/claude-0/-home-user/9a06fe22-60e0-580d-8926-30c8a46558b9/scratchpad/rev-bin/py`, and the check output `/tmp/claude-0/-home-user/9a06fe22-60e0-580d-8926-30c8a46558b9/scratchpad/rev-checkall.txt`.
- **Why:** brief 124 step 3's Reviewer on the third weekly landing (R1 paths under src/**).
- **Verified (command + output):** sections A to F above.
- **Undone:**
  - Service-Desk's `main` was read as `origin/main` (d0bcd6a, 2026-11-23T09:15:46-06:00); the local branch `main` there is stale at e0ea284 (2026-11-07). I did not fetch, so anything pushed after the clone's last fetch is unseen.
  - The same holds for Model-Lab's origin/main, which equals 32f1010.
  - Wake arrival times, marker and hook states are the work session's own claims. They are consistent with commit times but cannot be verified from the repository.
- **Needed outside its surface:**
  - The Orchestrator records this return verbatim as `reviews/<PR number>/reviewer.md`.
  - The owner or Orchestrator decides finding 1.
  - The brief number in finding 2 is settled before both branches land.
- **Open questions:**
  1. Who lists a piece that has no dispatch record at all (finding 1): the work session's `scan.tsv`, or a record of the Orchestrator's? And were the 2026-11-22 Service-Desk builder pieces (the S-014 card fix, the baseline adapter) dispatched with any record that qualifies under E-003 Step 2?
  2. Should the Reviewer brief's number be taken from main alone, or from all open branches?
