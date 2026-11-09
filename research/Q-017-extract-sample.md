# Hand check of the Q-017 extract against the repositories (LL-73)

*Run by the Orchestrator (session_01QBwHGNSLmSrYQgS6BPjV8p) on 2026-11-09, as the owner ruled (decisions/questions/P-002-q017-decide.md), before the deciding check. Not for the Researcher: the question limits it to research/Q-017-extract/.*

Sample: in each repository, up to two merged pull requests from each combination of how they were merged (merge or squash) and the class of their merge commit's author, drawn at random with a fixed seed (17), and three plain commits with files. Each was compared with git directly (git show, rev-list, diff and name-status on origin/main). Columns: repository, pull request or commit, how, author class, then whether the extract matches git on the author class, the date (UTC), the pull request number in the subject, the pull request's own commits, the count of those commits by author class (for a plain commit, each file's added/modified/deleted status), and how the pull request's file list compares with git's net diff.

```
Service-Desk | 133 | merge | agent | True | True | True | True | True | same
Service-Desk | 128 | merge | agent | True | True | True | True | True | same
Service-Desk | 146 | merge | other | True | True | True | True | True | same
Service-Desk | 137 | merge | other | True | True | True | True | True | same
Service-Desk | 251 | merge | owner | True | True | True | True | True | same
Service-Desk | 286 | merge | owner | True | True | True | True | True | same
Service-Desk | 176 | squash | agent | True | True | True | True | True | same
Service-Desk | 177 | squash | agent | True | True | True | True | True | same
Service-Desk | commit 5c88823573 | plain | agent | True | True | - | - | True | 10 files
Service-Desk | commit 0a66acd70e | plain | agent | True | True | - | - | True | 2 files
Service-Desk | commit e960e2e5e9 | plain | owner | True | True | - | - | True | 1 files
Model-Lab | 53 | merge | owner | True | True | True | True | True | same
Model-Lab | 35 | merge | owner | True | True | True | True | True | same
Model-Lab | commit b225e9b9e0 | plain | agent | True | True | - | - | True | 7 files
Model-Lab | commit 3c8ea0dc04 | plain | agent | True | True | - | - | True | 1 files
Model-Lab | commit 2e8ffa0428 | plain | agent | True | True | - | - | True | 1 files
Personal-Org-Operating-Model | 34 | merge | owner | True | True | True | True | True | extract has 1 more, 0 fewer than the net diff
Personal-Org-Operating-Model | 18 | merge | owner | True | True | True | True | True | same
Personal-Org-Operating-Model | commit 00c22a3b1e | plain | agent | True | True | - | - | True | 2 files
Personal-Org-Operating-Model | commit 6c7f76f573 | plain | agent | True | True | - | - | True | 1 files
Personal-Org-Operating-Model | commit e5e294f0c1 | plain | agent | True | True | - | - | True | 1 files
```

Result: every sampled item matches on every field checked. One pull request's file list holds one more path than git's net diff: the extract lists every file the pull request's commits touched, including one changed and then changed back, while the net diff shows only what remained. The README says the file list is the union of the commits' paths.

Not covered by this sample: commits by the "other" class other than merge commits (a tool's default identity), and the owner's address classing beyond the sampled commits.
