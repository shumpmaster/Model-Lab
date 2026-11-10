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

## Round 2 (brief 232)

The round's verdict was FAIL.

The corrections are almost all made and every script figure reproduces. Three small items remain: one count that doesn't match the memo's own rule, an overbroad "every figure" sentence, and paths and file names left in the memo.

I extracted the memo's script to /tmp/q017-check2/q017.py and ran `python3 -I q017.py /home/user/Model-Lab/research/Q-017-extract`. It exited with code 0 and wrote only under /tmp/q017-check2/. I also ran my own checks there (own.py, own2.py). I did not need the repositories. I read no forbidden material and did not use the web.

## 1. Figures re-checked against the rerun

| Figure | Result | Reason |
|---|---|---|
| Opening paragraph: 447 PRs (312 / 85 / 50) and lines (322,755 / 87,968 / 109,461) | holds | Matches the script output. |
| Opening: plain commits by agent identity 94.2 / 98.9 / 97.8%, owner 5.8 / 1.1 / 2.2% | holds | Same as round 1. |
| Opening: no co-author trailer; no commit marked revert | holds | Same as round 1. |
| Opening: merging account 226 / 86 (Service-Desk), 85 (Model-Lab), 50 (POOM) | holds | Same as round 1. |
| Opening: PRs with an owner-identity commit 48/312, 6/85, 16/50 | holds | Same as round 1. |
| Opening: question-label files 540 / 82 / 29, decision-label 78 / 1 / 1 | holds | Same as round 1. |
| Opening: 14-day file overlap 202 / 42 / 33; named 37 / 17 / 6 | holds | Same as round 1. |
| Opening: 14-day incomplete groups 82 / 85 / 12, with 43 of 202, 7 of 37, 7 of 33, 0 of 6 | holds | Matches the rerun's complete/incomplete rows (159+43, 30+7, 26+7, 6+0). |
| Opening: all 447 merged within 60 days of 2026-11-09 | holds | 312, 85 and 50 of the same totals. |
| §1 monthly PR counts and lines, kind table, flagged 175 / 50 / 38 | holds | Exact match to the script output. |
| §1 commit table and 375 / 59 split; 356 / 116 / 49 / 1 / 1 kinds | holds | Exact match. |
| §1 29 and 1 PR-number gaps; 525 binary entries | holds | Exact match. |
| §2 names, committer "Claude" on 684 / 6 / 25, 147 owner single-file commits and their split | holds | Exact match. |
| §2 per-PR table, line splits, merging account by owner commit, commit-level shares, convention-start dates | holds | Exact match. |
| §3 both tables, PR distributions, matching rows, moves 7 / 0 / 1 | holds | Exact match, including lines at first addition and changed lines of PRs that add one or more. |
| §4 left-out counts and lines (71/2,622, 5,428; 51/685, 27,801; 8/575, 3,365), by class | holds | Exact match; the Model-Lab 15 are the extract's earlier versions and the Service-Desk 2 are lock files. |
| §4 PRs with no file left to test (14 / 9 / 11) | holds | Exact match. |
| §4 count table, all windows and groups | holds | Exact match. |
| §4 line table, including the "earlier lines in shared files" column | holds | Exact match. |
| §4 mentions_prs 148/148, 44/44, 52/53 | holds | Exact match. |
| §5 author date differs from commit date on 86 / 43 / 18 | holds | My own count gives 86 / 43 / 18, but the script doesn't print it. |
| §5 "3 in Service-Desk, 4 in POOM" record-named copies in test and template folders | does not hold | See "Still to correct", item 1. |
| Figures round 1 confirmed | unchanged | None changed. The Researcher reports only dict key order differing, and that comparison was not rerun here. |

## 2. Round 1's corrections

| Correction | Result | Reason |
|---|---|---|
| 1. Three-way marks with "what it would take" | holds | The mark key, per-figure marks, and a "would take" line on each [P] and [N] item are present. The word "grade" no longer appears. |
| 2a. "wrote" changed to "carry an agent identity as author" | holds | The opening paragraph and §2 say "carry". |
| 2b. 14-day incomplete windows stated; overlap called coarse | holds | Stated in the opening paragraph. |
| 2c. Label counts worded as labelled files, with where they sit | holds | Both the opening paragraph and §3 give the 253 / 190 / 97 and 26 locations, attributed to the source check. The 253+190+97 sum to 540. |
| 3. Rule text matches the script | holds | The 12 numbered rules follow the script's order. The template rule comes after the label rules, and the inventory- files, `.jsonl.lock` and `_VERSION` are included. I compared every rule with `kind()`. |
| 4. No specific paths in the script | mostly holds | See "Still to correct", item 3 for the memo prose. The script now uses folder-name and file-name-word classes (there is an upper-case ledger/digest word list and a `-lock.json` suffix rule), and no full path is listed. Folder names such as "template-v3" and "portfolio-template" remain as classes. I judge that acceptable. |
| 5. Second view of lines in §2, §3, §4 | holds | Added, with reasons stated where lines are not given (re-additions, deletions, matching). The line figures match the rerun. |

## 3. Wording against LL-71

I read each sentence of the opening paragraph and the five item summaries. Each is worded no more strongly than its figure and carries a mark. "Carry an agent identity" is [P]. File overlap is called coarse and [P]. The label counts are [P]. Reverts are [P]. Windows are [S] as a split and [P] as a measure. Who is behind "Claude" is [N]. I found none overstated. The exception is the "every figure" sentence in item 2 below.

## Still to correct

1. **§5 "3 in Service-Desk, 4 in POOM" (record-named copies in test and template folders).**
   - The count is not computed by the script.
   - Under the memo's own rule 8, the word list plus names ending `_REGISTER` or `_REVIEW`, the POOM count is 7, not 4. The 4 counts only the word-list names. Service-Desk's 3 is right either way.
   - All 7 POOM copies stay in the overlap test.
   - Either state 7 or say which names the 4 covers, and make the script print it.
2. **"Every figure is counted from the extract by the script at the end, except the label locations above."**
   - This is overbroad. The script does not print the §5 author-date counts (86 / 43 / 18) or the copies counts above.
   - Either add them to the script or narrow the sentence.
3. **Paths and file names remain in the memo.**
   - The italic first line names a brief path and the source-check file. It is the Orchestrator's own line, so the Orchestrator should decide.
   - The final "Working files" line names /tmp/q017/, q017.py, new.out, orig.py, orig.out, cmp.py and memo.md. Remove it from the memo.
   - These are not extract paths, but check 4 asks for no path or file name.

I could not see my token total.

## Round 3 (brief 234)

The round's verdict was FAIL.

One sentence in the memo is wrong against the script output. Everything else holds. I extracted the memo's script to /tmp/q017-check3/q017.py. I ran `python3 -I q017.py /home/user/Model-Lab/research/Q-017-extract` with output to /tmp/q017-check3/out.txt. It exited 0 and wrote nothing to stderr. I did not need the repositories, read no forbidden material, and did not use the web. I could not see my token total.

| Item | Result | Reason |
|---|---|---|
| Opening paragraph: 447 PRs (312/85/50) and lines 322,755 / 87,968 / 109,461 | holds | Match the output. |
| Opening: plain commits by agent identity 94.2 / 98.9 / 97.8%, owner 5.8 / 1.1 / 2.2% | holds | Match the output. |
| Opening: no co-author trailer; no commit marked revert | holds | The script now prints both as commit-level counts of 0 in all three repositories. |
| Opening: merging account 226 / 86, 85, 50; PRs with an owner-identity commit 48/312, 6/85, 16/50 | holds | Match the output. |
| Opening: label-file counts 540/82/29 and 78/1/1 | holds | Match the output. The 97/253/26 locations come from git (round 1) and are labelled as such. |
| Opening: 14-day overlap 202/42/33 and named 37/17/6 | holds | Match the output. |
| Opening: incomplete 14-day windows 82 (43 of 202, 7 of 37), 85, 12 (7 of 33, 0 of 6) | holds | Match the output's complete/incomplete rows. |
| Opening: all 447 merged less than 60 days before 2026-11-09 | holds | 312/312, 85/85, 50/50. |
| §1 monthly PR counts and lines, kind table, flagged 175/50/38, single-kind counts | holds | Exact match. |
| §1 commit table, 375/59 split, 356/116/49/1/1, 525 binary entries, 29 and 1 gaps in PR numbers | holds | Exact match. |
| §2 names and counts, "Claude" committer on 684/6/25, the 147 owner single-file commits and their split | holds | Exact match. |
| §2 per-PR table and lines, merging account by owner commit, commit-level shares, convention-start dates, 119/8/17 | holds | Exact match. |
| §3 both tables (months, lines, re-additions, deletions, still present, via PR or outside, agent/owner split, PR line splits) | holds | Exact match. |
| §3 matching rows (3/49/78; 0/1/29; 0/1/12) and moves 7/0/1; Model-Lab and POOM PR distributions | holds | Exact match. |
| §3 Service-Desk distribution: "one to three pull requests at each count from 5 to 22" | does not hold | Counts present: 5:2, 6:3, 7:1, 8:2, 9:2, 10:1, 11:2, 14:2, 15:1, 16:1, 18:1, 22:1. Counts 12, 13, 17, 19, 20 and 21 have no pull request, so "each count" is wrong. |
| §4 left-out classes and lines (71/2,622 and 5,428; 51/685 and 27,801; 8/575 and 3,365); no file left 14/9/11 | holds | Exact match. |
| §4 count table, all windows and groups, including the direct-commit column | holds | Exact match. |
| §4 line table, including "earlier lines in shared files" | holds | Exact match. |
| §4 mentions_prs 148/148, 44/44, 52/53 | holds | Exact match. |
| §5 author date differs from commit date: 86/2,758, 43/971, 18/948 | holds | Now printed by the script. |
| §5 record-named copies: Service-Desk 3, Model-Lab 0, POOM 7 (4 word list + 3 _REGISTER/_REVIEW), all classed built, none left out | holds | The script prints these. Round 2 correction 1 is made. |
| Figures rounds 1 and 2 confirmed | unchanged | The changes against round 1's output are new print lines (line views, copies, author dates, co-author and revert counts) and a reformatted "non-agent commits before it" line. No earlier figure changed. |
| Round 2 correction 1: the §5 copies count | holds | See the copies row above. |
| Round 2 correction 2: "every figure" sentence narrowed and script prints what the memo cites | holds | The sentence now reads "printed by the script, or a sum of figures it prints, except the label locations". The sums I checked: 318,799 = 152,983 + 165,816, and 147 = 120 + 9 + 18. The script paragraph no longer claims a "4,292 paths" check. |
| Round 2 correction 3: no paths or working files | holds | The "Working files" line is gone and the run line names no script file. The italic Orchestrator line names only a session id, and the text names "brief 233", which is a number, not a path. I found no slash path or file name with an extension in the prose. |
| Round 1 corrections 1 to 5 (marks, "carry" wording, rule text matches script, rules in place of paths, line views) | hold | Marks and "would take" lines are present. "Wrote" is not used. The rule text follows the script's order. The line views are present, and the memo gives its reason where it gives none. |
| LL-71 for the opening paragraph and the §1 to §5 summaries | holds | Each sentence is worded no more strongly than its figure and carries its mark. The §4 "Many windows" is now counts, and the §3 "mostly" is now "beyond that test". |
| No path or file name in the memo and script | holds, with a note | The script lists only folder-name and file-name-word classes, as round 2 accepted. It also contains the extract's label prefixes (cos-session, cos-handoff, notes, project-plan, ideas, questions, decisions). The question bars reporting labels. I treat these as rule terms, not reported figures, and do not count the note against the verdict. The Orchestrator can decide whether to strip them. |

## What the memo must still correct
1. In §3, the Service-Desk distribution of pull requests by number of question-label files first added says "one to three pull requests at each count from 5 to 22". Not every count from 5 to 22 occurs. Replace it with the counts that do, for example "one to three pull requests at each of the counts 5 to 11, 14, 15, 16, 18 and 22, none at 12, 13, 17, 19, 20 or 21". Before the "one pull request adds 75" clause, the list is 5:2, 6:3, 7:1, 8:2, 9:2, 10:1, 11:2, 14:2, 15:1, 16:1, 18:1, 22:1.

Files: /tmp/q017-check3/q017.py, /tmp/q017-check3/out.txt. The memo and extract were not changed, and I filed no library entries.
