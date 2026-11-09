Verdict: FAIL

*The Source checker's check of research/Q-017-memo.md. Each round on a different model from the Researcher; recorded verbatim by the Orchestrator (session_01QBwHGNSLmSrYQgS6BPjV8p) from the helper's return, 2026-11-09; each round's own verdict line is recorded as "The round's verdict was …" (LL-68). The verdict above is the latest round's.*

## Round 1 (brief 230)

The round's verdict was FAIL.

All the memo's figures hold. The failure is on check 4: how figures are marked, one rule description, and wording stronger than the figures (LL-71). Those are listed under "What the memo must correct".

I could not see my token total.

## 1. Rerun of the memo's script
- I extracted the script from the memo to /tmp/q017-check/q017.py and ran `python3 -I q017.py /home/user/Model-Lab/research/Q-017-extract`. It exited cleanly, and everything I wrote went under /tmp/q017-check/.
- Two runs differ only in the order of keys in one printed dict ("plain-in-no-PR commits touching each kind"); every number is identical.

| Figure or rule | Result |
|---|---|
| Lead: 447 PRs (312 / 85 / 50) and lines (322,755 / 87,968 / 109,461) | confirmed |
| Lead: plain commits by agent identity 94.2 / 98.9 / 97.8%, owner 5.8 / 1.1 / 2.2% | confirmed |
| Lead: no co-author trailer; no commit marked revert | confirmed (checked on all commits, not just PR lines) |
| Lead: merging account 226 / 86 in Service-Desk; Model-Lab 85 and POOM 50 all by the owner's account | confirmed |
| Lead: PRs with an owner-identity commit 48/312, 6/85, 16/50 | confirmed |
| Lead: question-label first adds 540 / 82 / 29; decision-label 78 / 1 / 1 | confirmed |
| Lead: 14-day file overlap 202 / 42 / 33; 14-day named 37 / 17 / 6 | confirmed |
| Lead: all 447 merged within 60 days of 2026-11-09 | confirmed |
| §1 PRs per month and lines, the kind table, the 175 / 50 / 38 flagged counts | confirmed |
| §1 commit table (1,648 / 844 / 827 plain in PRs; 434 / 4 / 1 outside; other-merge 291 / 38 / 70 inside, 73 / 0 / 0 outside) and the 375 / 59 split | confirmed |
| §1 29 Service-Desk and 1 POOM PR numbers with no merged line; 525 binary entries | confirmed |
| §2 names and counts per class; committer "Claude" on 684 / 6 / 25 agent commits | confirmed |
| §2 all 147 owner plain commits are single-file with GitHub as committer, split by kind as stated | confirmed |
| §2 per-PR table, line splits by author group, merging account against owner commit | confirmed |
| §2 commit-level shares (plain only, all commits, excluding merge-pr commits) | confirmed |
| §2 first agents.invalid dates (2026-09-30T19:04:45Z, 2026-11-01T16:58:40Z, 2026-09-24T14:59:13Z) and owner plain commits after (119 / 8 / 17) | confirmed |
| §2 "exactly one non-agent commit comes first, under the owner's identity" | confirmed |
| §3 all rows of both tables (months, re-additions, deletions, still present, via PR or outside, agent/owner split, PR distributions, matching rows, moves 7 / 0 / 1) | confirmed |
| §4 left-out files (71/2,622; 51/685; 8/575, by kind) and PRs with no file left (14 / 9 / 11) | confirmed |
| §4 table rows for 14, 30 and 60 days, complete and incomplete groups, including the direct-commit column | confirmed |
| §4 mentions_prs 148/148, 44/44, 52/53 | confirmed |
| §5 author date differs from commit date on 86 / 43 / 18 commits | confirmed |
| §5 "Model-Lab records contain earlier versions of this extract" | confirmed; git shows 16 paths under that extract folder in Model-Lab |
| Rule: month by merged_at UTC; share and window definitions as scripted | holds |
| Rule: kind classification, "first match wins" | holds in substance, with two small gaps (see corrections) |
| Rule: windows (strictly later, up to and including +N days; complete if merged_at + N ≤ 2026-11-09T00:00Z) | holds |
| Rule: matching test and move test in §3 | holds, and the memo marks them as estimates |

## 2. Independent recounts
I wrote my own code at /tmp/q017-check/own/recount.py, r2.py and the git sample. It agrees on every main figure:
- **PRs per repository and month:** Service-Desk 1 / 245 / 66 (Sep / Oct / Nov), Model-Lab 85 (all Nov), POOM 10 / 28 / 12.
- **PRs with an owner-identity commit:** 48, 6 and 16. The `commit_author_classes` field and the commits file give the same answer.
- **Merging accounts:** Service-Desk shumpmaster 226 and github-actions[bot] 86; Model-Lab shumpmaster 85; POOM shumpmaster 50.
- **Plain commits by class:** agent 1,962 / 839 / 810, owner 120 / 9 / 18. There are no co-author trailers and no revert flags. No commit sits in two PRs, and every PR's merge commit is in the commits file.
- **Files first added with a label (earliest commit_date):** questions 540 / 82 / 29, decisions 78 / 1 / 1.
- **14-day counts:** file overlap with a later merged PR 202 / 42 / 33, named 37 / 17 / 6. My independent run also gives the same 30- and 60-day counts: Service-Desk 203 overlap / 41 named, Model-Lab 42 / 17, POOM 33 / 6.

## 3. Sample against git (default branch, origin/main, read-only)
- **Commit counts agree.** Total, merge and non-merge commits match the extract: 2,758 / 676 / 2,082 in Service-Desk, 971 / 123 / 848 in Model-Lab, 948 / 120 / 828 in POOM.
- **Author counts agree.** Non-merge commits with an agents.invalid address are 1,962 / 839 / 810, and non-merge commits by author shumpmaster are 120 / 9 / 18.
- **Merge authors and committers agree.** For example, Service-Desk shows 226 shumpmaster/GitHub and 86 github-actions[bot]/GitHub.
- **No revert subjects.** `git log` finds no subject starting "Revert" in any repository.
- **Workflow-bot merge.** Service-Desk PR 234 (b8e29e97…) has two parents and was authored by github-actions[bot] and committed by GitHub on 2026-10-25T12:15:03Z. It matches the extract.
- **Owner-identity commit.** Service-Desk 48e9d87d… was authored by shumpmaster, committed by GitHub at 2026-11-09T13:49:35Z, with a single parent and a single added file under decisions/. It matches the extract.
- **First question file.** Service-Desk c1c9a564… is by the orchestrator@agents.invalid identity at 2026-09-30T19:04:45Z, and exactly one file under questions/ is added in it. Per `git show`, it is also the first agents.invalid commit, so it matches the §2 start date. I did not open any file. The Model-Lab and POOM first-question commits are the first agents.invalid commits too.
- **PR membership.** For a random sample of 150 PRs (25 / 50 / 75 across the three repositories), `git rev-list <p1>..<p2>` returns the same commit set as the extract's `commits` list in every case.
- **Label rule.** Re-applying the label rule of extract.py to `git log --no-renames` added paths gives questions 540 / 82 / 29 and decisions 78 / 1 / 1, equal to the memo.

The label counts need a caveat the memo does not give. By the label rule, "question" files in Service-Desk sit in three places:
- 253 under decisions/questions/
- 190 under questions/
- 97 under tests/

The 78 "decision" files include 26 under tests/. POOM's 29 include two in template folders. The memo's note about "template copies" does not cover the test-folder share, and it never says that decisions/questions/ is labelled as a question.

## 4. What the memo must correct
1. **Marking.** The question asks for each count to be marked as one the extract supports, supports only in part, or cannot support, with what it would take to measure it. The memo marks everything "A" (grade) and nothing else. It also says "Every figure here is counted from the extract (grade A)". It needs the question's three-way mark on each figure. Examples:
   - Who made the changes: in part, since identity is not authorship.
   - Question and decision file counts: in part.
   - File overlap: in part, because it is a coarse test.
   - Revert count: in part, since only subjects starting "Revert" are found.
2. **Lead wording.**
   - "Agent identities wrote 94.2%" and "the owner's identity wrote 5.8%" are stronger than the memo's own §2 limit. It should say "commits carry an agent identity as author", not "wrote".
   - The 14-day figures (202, 42, 33 and 37, 17, 6) include PRs whose 14-day window is not complete: 82 in Service-Desk, 85 in Model-Lab and 12 in POOM. The lead mentions the incomplete windows only for 60 days. It should say so for 14 days, and that file overlap is a coarse test, not a measure of rework.
   - "Files first added with a question label: 540, 82 and 29" is worded as questions. The memo should say they are label counts: they include files under a tests folder and under decisions/questions, a label that the memo's coding doubts do not mention.
3. **Rule vs script.**
   - Built work in the script also includes governance/OPERATING_MODEL_VERSION and the ".jsonl.lock" extension.
   - The script puts docs/design/inventory- files under records; the memo's rule text does not name this.
   - The memo's rule text lists the template folders as checked before records, but the script checks them after the session, handoff and notes labels and before the review, dispatch and brief paths. The result is the same, but the text should match the script.
4. **Paths in the memo.** The question says not to report any path or file name. The appended script names specific unlabelled paths: docs/LEDGER.md, docs/DIGEST.md, docs/LESSONS.md, docs/CHECKPOINT.md, docs/IMPROVEMENT_REGISTER.md, docs/sprints/PROGRESS.md, docs/design/JOIN_UP_REVIEW.md, docs/audit/CLAIMS_REGISTER.md, intake/estimates.jsonl, CHANGELOG.md, VERSION and the extract folder name. They should be replaced by rules or counted by class.
5. **Second view of lines.** The question asks for changed lines as a second view beside each count. §1 gives it. The §3 file counts, the §4 counts and the §2 shares of PRs give no lines. The memo should supply them or say why not.

Files: /tmp/q017-check/q017.py, /tmp/q017-check/out.txt, /tmp/q017-check/own/recount.py, /tmp/q017-check/own/r2.py. The memo and extract under /home/user/Model-Lab/research/ were not changed, and I filed no library entries.
