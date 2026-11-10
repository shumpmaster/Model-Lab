# Hand check of the Q-017 extract against the repositories (LL-73)

*Run by the Orchestrator (session_01QBwHGNSLmSrYQgS6BPjV8p) on 2026-11-09, after the owner's ruling to fix the merge coding and test each rule on its edge cases (decisions/questions/P-002-q017-next.md); the first hand check is in this file's history. Not for the Researcher: the question limits it to research/Q-017-extract/.*

## 1. Rules and edge cases, tested over the whole extract

Each line: the rule, whether it holds, and the figures behind it.

```
Service-Desk: each pull request number appears once | holds | 312 lines, 312 numbers
Service-Desk: every merge commit has two parents | holds | 
Service-Desk: no single-parent commit is coded as a merge | holds | 0 found
Service-Desk: no commit is in two pull requests' commit lists | holds | 0 in two or more
Service-Desk: every pull request lists at least one commit | holds | 
Service-Desk: every merge committed by GitHub is a pull request line | holds | 312 GitHub merges, 312 pull request lines made by GitHub
Service-Desk: merges made outside GitHub are not pull request lines | holds | 27 merges outside GitHub that name a pull request, coded other-merge
Service-Desk: every file has a status of added, modified or deleted | holds | {'modified': 3785, 'added': 2975, 'deleted': 200}
Service-Desk: no address and no subject field in the extract | holds | 
Service-Desk: the other class, by name and kind | holds | {('Claude', 'other-merge'): 31, ('github-actions[bot]', 'merge-pr'): 86}
Service-Desk: commits in the extract equal commits on the default branch | holds | 2758 and 2758
Model-Lab: each pull request number appears once | holds | 85 lines, 85 numbers
Model-Lab: every merge commit has two parents | holds | 
Model-Lab: no single-parent commit is coded as a merge | holds | 0 found
Model-Lab: no commit is in two pull requests' commit lists | holds | 0 in two or more
Model-Lab: every pull request lists at least one commit | holds | 
Model-Lab: every merge committed by GitHub is a pull request line | holds | 85 GitHub merges, 85 pull request lines made by GitHub
Model-Lab: merges made outside GitHub are not pull request lines | holds | 13 merges outside GitHub that name a pull request, coded other-merge
Model-Lab: every file has a status of added, modified or deleted | holds | {'modified': 705, 'added': 752, 'deleted': 50}
Model-Lab: no address and no subject field in the extract | holds | 
Model-Lab: the other class, by name and kind | holds | {('Claude', 'other-merge'): 1}
Model-Lab: commits in the extract equal commits on the default branch | holds | 971 and 971
Personal-Org-Operating-Model: each pull request number appears once | holds | 50 lines, 50 numbers
Personal-Org-Operating-Model: every merge commit has two parents | holds | 
Personal-Org-Operating-Model: no single-parent commit is coded as a merge | holds | 0 found
Personal-Org-Operating-Model: no commit is in two pull requests' commit lists | holds | 0 in two or more
Personal-Org-Operating-Model: every pull request lists at least one commit | holds | 
Personal-Org-Operating-Model: every merge committed by GitHub is a pull request line | holds | 50 GitHub merges, 50 pull request lines made by GitHub
Personal-Org-Operating-Model: merges made outside GitHub are not pull request lines | holds | 7 merges outside GitHub that name a pull request, coded other-merge
Personal-Org-Operating-Model: every file has a status of added, modified or deleted | holds | {'modified': 1402, 'added': 577, 'deleted': 31}
Personal-Org-Operating-Model: no address and no subject field in the extract | holds | 
Personal-Org-Operating-Model: the other class, by name and kind | holds | {('Claude', 'other-merge'): 17}
Personal-Org-Operating-Model: commits in the extract equal commits on the default branch | holds | 948 and 948
```

The first run of these tests, before the fixes below, failed three of them: nine pull request numbers appeared twice in Service-Desk (local merges whose subject names a pull request, coded as pull requests beside GitHub's own merge), 64 commits sat in two pull requests' lists as a result, and three GitHub merges in Personal-Org-Operating-Model were missed (subjects of the form "Merge pull request #n: …"). The fixes: a pull request merge is now a two-parent commit committed by GitHub whose subject names a pull request; every other merge is other-merge. Service-Desk's merged pull requests went from 327 to 312: the six review-record commits and the nine local merges dropped out.

## 2. Fields against git, on a sample

Sample: in each repository, up to two merged pull requests for each class of merge-commit author, drawn at random with a fixed seed (17), and three plain commits with files. Columns: repository, pull request or commit, kind, author class, then whether the extract matches git on the author class, the date (UTC), the pull request number in the subject, the pull request's own commits, and the count of those commits by author class (for a plain commit, each file's status), and how the pull request's file list compares with git's net diff.

```
Service-Desk | 105 | merge | other | True | True | True | True | True | same
Service-Desk | 124 | merge | other | True | True | True | True | True | same
Service-Desk | 20 | merge | owner | True | True | True | True | True | same
Service-Desk | 248 | merge | owner | True | True | True | True | True | extract has 9 more, 0 fewer than the net diff
Service-Desk | commit 6c34acb6a7 | plain | agent | True | True | - | - | True | 1 files
Service-Desk | commit 516fa2e6e0 | plain | agent | True | True | - | - | True | 8 files
Service-Desk | commit f6c1afbb72 | plain | agent | True | True | - | - | True | 3 files
Model-Lab | 16 | merge | owner | True | True | True | True | True | same
Model-Lab | 1 | merge | owner | True | True | True | True | True | extract has 1 more, 0 fewer than the net diff
Model-Lab | commit b217e471b3 | plain | agent | True | True | - | - | True | 3 files
Model-Lab | commit 386bc357d2 | plain | agent | True | True | - | - | True | 2 files
Model-Lab | commit 048c0468bf | plain | agent | True | True | - | - | True | 1 files
Personal-Org-Operating-Model | 35 | merge | owner | True | True | True | True | True | extract has 1 more, 0 fewer than the net diff
Personal-Org-Operating-Model | 26 | merge | owner | True | True | True | True | True | extract has 1 more, 0 fewer than the net diff
Personal-Org-Operating-Model | commit cff80ace5c | plain | agent | True | True | - | - | True | 3 files
Personal-Org-Operating-Model | commit c346f0ec05 | plain | agent | True | True | - | - | True | 2 files
Personal-Org-Operating-Model | commit 88f72fecb9 | plain | agent | True | True | - | - | True | 3 files
```

Every sampled item matches on every field. Where a pull request's file list holds more paths than git's net diff, the extra paths are files its commits touched and later changed back; the README says the file list is the union of the commits' paths.
