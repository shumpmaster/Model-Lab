# Q-017 memo: who makes, merges and changes again the organisation's changes, as of 2026-11-09 (Researcher, round 2, 2026-11-09)

*The Researcher's memo for Q-017, round 2 (brief 231, docs/briefs/231-researcher.md), revised after the Source checker's round 1 (research/Q-017-source-check.md); round 1 (brief 229) is in this file's history. Recorded verbatim by the Orchestrator (session_01QBwHGNSLmSrYQgS6BPjV8p), 2026-11-09, from the helper's return; only this italic line is the Orchestrator's.*

**Marks.** Each figure carries one of the question's three marks:
- **[S] supported:** the extract records it, and the count follows from the rule stated here.
- **[P] supported in part:** the count is exact by its rule, but the rule measures less than the words of the question. Each one says what is missing and what it would take to measure it.
- **[N] not supported:** the extract cannot give it. Each one says what it would take.

A mark on a heading or a table holds for every figure under it unless a figure carries its own.

The extract has 447 merged pull requests [S]: 312 in Service-Desk, 85 in Model-Lab and 50 in Personal-Org-Operating-Model (POOM). They change 322,755, 87,968 and 109,461 lines (added plus removed; binary files count none) [S]. Of plain (non-merge) commits, 94.2%, 98.9% and 97.8% carry an agent identity as author, and 5.8%, 1.1% and 2.2% carry the owner's identity [P: an identity is not proof of who did the work]. No commit carries a co-author trailer [S as a count of trailers]. The extract takes the merge commit's author as the account that merged. In Service-Desk that is the owner's account for 226 of 312 pull requests (72.4%) and a workflow bot for the other 86 (27.6%). In Model-Lab it is the owner's account for all 85, and in POOM for all 50 [S for the account; P for who acted through it]. 48/312 (15.4%), 6/85 (7.1%) and 16/50 (32.0%) pull requests contain at least one commit under the owner's identity [P]. Files first added under a question label number 540, 82 and 29, and under a decision label 78, 1 and 1 [P]. These count labelled files, not questions put to the owner or answers given. The label goes by folder name at any depth. The source check found, against git, that Service-Desk's 540 include 97 files in its test folder and 253 in a question folder nested in its decision folder, and that its 78 include 26 in the test folder. No commit subject starts "Revert" [P: a revert worded otherwise is not found]. Within 14 days of merging, a later merged pull request changed at least one of the same files (files edited in turn by design left out) for 202/312, 42/85 and 33/50 pull requests [P]. File overlap is a coarse test: it does not show that the same lines changed, or that the earlier change was reworked. A later commit's subject named the pull request's number within 14 days for 37, 17 and 6 [P: a number may be a record, an issue or another repository's pull request]. The 14-day counts include pull requests whose 14-day window was not complete on 2026-11-09: 82 of 312 in Service-Desk (43 of the 202 and 7 of the 37), all 85 in Model-Lab, and 12 of 50 in POOM (7 of the 33 and none of the 6). All 447 were merged less than 60 days before 2026-11-09, so no 60-day window is complete. Every figure is counted from the extract by the script at the end, except the label locations above. Those are the source check's finding from git and cannot be seen in the extract.

## 1. Units

**Summary.** The 447 merged pull requests and their lines are counted per month [S]. Their kind comes from a path rule of this memo's own, so the kind counts are supported only in part [P]. Plain commits on the default branch outside every merged pull request number 434, 4 and 1 [S]. What they were (direct pushes, or work whose pull request is not in the extract) is not supported [N].

**Rules.**
- A pull request is one line of a repository's pull-request file. Its month is the month of merged_at (UTC).
- Each changed path is put into one kind by rules on folder names and file-name words; no single path is listed. The rules are checked in this order, and the first match wins:
  1. a question or decision label: **owner question or answer**;
  2. a session, handoff or notes label: **records**;
  3. a project-plan or idea label: **plan or spec**;
  4. anything in POOM's shipped template and kit folders: **built** (so a ledger template inside a kit counts as built);
  5. anything in a top-level folder for reviews, dispatch logs, status, digests, queue, triage or intake: **records**;
  6. anything in a docs subfolder for briefs, reports, handover, trials, archive, checkpoints or audit: **records**;
  7. in the design folder, anything in its build-screenshot or audit subfolders, and any file directly in it whose name starts "audit-" or "inventory-": **records**;
  8. a file at the top level or anywhere in the docs folder whose name is upper-case and either is one of ledger, digest, lessons, checkpoint, progress, changelog or version, or ends "_REGISTER" or "_REVIEW": **records**;
  9. anything in a top-level research, library or experiments folder, in a docs research subfolder, or in the design folder's reference-image subfolder: **research**;
  10. anything in a top-level specs folder or in a docs subfolder for proposals, sprint plans, gate cases or design (the rest of the design folder), and the upper-case mission and scope files directly in docs: **plan or spec**;
  11. anything in a top-level source, tests, tools, scripts, CI or agent-definition folder, or in the governance folder's checks subfolder; a top-level ignore file; any path ending .py, .js, .mjs, .sh, .yml, .yaml, .toml, .json, .jsonl.lock, .css or .woff2; and an upper-case file directly in the governance folder whose name ends "_VERSION": **built**;
  12. everything left: **other** (mainly rule and guidance prose, such as the agents file, readmes, the operating-model text, governance prose, glossary and setup).
- A pull request is counted under every kind it touches, and flagged when it touches more than one.
- Changed lines are added plus removed. Binary files count 0 lines; Service-Desk has 525 binary entries.

**Pull requests per month: count (changed lines) [S]**
- Service-Desk:
  - 2026-09: 1 (15,305)
  - 2026-10: 245 (289,165)
  - 2026-11: 66 (18,285)
- Model-Lab:
  - 2026-11: 85 (87,968)
- POOM:
  - 2026-09: 10 (57,938)
  - 2026-10: 28 (42,078)
  - 2026-11: 12 (9,445)

**By kind [P: the kinds come from this memo's path rule, which is not checked against what each file was for; checking it would take reading the files, or the owner's own map of folders].** Each entry is: pull requests touching the kind / lines in that kind's files / single-kind pull requests (their lines).

| Kind | Service-Desk | Model-Lab | POOM |
|---|---|---|---|
| built | 90 / 188,888 / 1 (7) | 8 / 20,554 / 0 | 26 / 64,836 / 0 |
| plan or spec | 100 / 60,698 / 7 (657) | 19 / 2,690 / 0 | 31 / 18,902 / 1 (2) |
| research | 29 / 6,634 / 1 (74) | 21 / 42,423 / 0 | 5 / 431 / 0 |
| records only | 173 / 49,382 / 21 (796) | 62 / 18,331 / 16 (2,833) | 49 / 21,168 / 11 (112) |
| owner question/answer | 204 / 14,803 / 107 (4,792) | 54 / 3,730 / 18 (1,084) | 22 / 1,283 / 0 |
| other | 22 / 2,350 / 0 | 4 / 240 / 1 (9) | 19 / 2,841 / 0 |
| flagged (more than one kind) | 175 | 50 | 38 |

- Labelled files are classed by their label wherever they sit. So the owner question/answer row includes labelled files in test and template folders (see the opening paragraph and §3).

**Commits [S].** The extract lists each pull request's commits, and no commit appears in two pull requests. Local merge commits ("other-merge") are counted apart from the work they bring in; that work is counted through its plain commits. Merge commits list no files, so they have no lines.

| | Service-Desk | Model-Lab | POOM |
|---|---|---|---|
| plain commits in a merged pull request (lines) | 1,648 (322,755) | 844 (87,968) | 827 (109,461) |
| plain commits on the default branch in no merged pull request (lines) | 434 (85,303) | 4 (20,915) | 1 (1) |
| other-merge commits inside a pull request | 291 | 38 | 70 |
| other-merge commits outside any pull request | 73 | 0 | 0 |

- Service-Desk's 434 commits outside any pull request: 375 carry an agent identity as author and 59 the owner's identity [P, as in §2]. 356 touch records, 116 research, 49 owner question/answer files, 1 plan and 1 other [P, by the kind rule].
- Of Service-Desk's 73 local merges outside pull requests, 1 names a merged pull request [S].

**What the extract cannot show here [N].**
- Whether the path-to-kind rule matches what the work was for. It would take reading the files, or a map of folders from the owner.
- Pull request titles. It would take pull-request metadata from GitHub.
- Pull requests closed without merging. In the numbering, 29 Service-Desk numbers and 1 POOM number have no merged line [S as a gap in the numbers]. They may be closed pull requests, issues, or merges made another way, and the extract cannot say which. It would take GitHub's list of pull requests and issues.
- Whether commits outside every pull request were direct pushes or work whose pull request is not in the extract.

## 2. Who made and merged each change

**Summary.** The counts below are of identities: which identity is the author of each commit, and which account authored each merge commit [S as identities]. As counts of who did the work or who decided to merge, they are supported only in part [P]. An agent session may commit under the owner's settings, and the identities say nothing about who started a session or a workflow. Measuring that would take session logs that tie each commit to the session, and through it to the person, that made it.

**Rule.** The extract's author_class is used as given.
- A pull request's commits are classed by author, other-merge commits included. A second view counts plain commits only.
- The account that merged a pull request is the author of its merge commit, as the extract's README defines it.
- The "other" names are kept as a separate class. Shares are given both ways: with "other" counted as not an agent, and with it counted as an agent.

**Names (commit counts) [S].**
- **Agent class:**
  - Service-Desk: orchestrator 1,100; chief-of-staff 484; builder 476; definer 207; source-checker 28.
  - Model-Lab: orchestrator 474; chief-of-staff 354; definer 23; builder 18; check-author 7.
  - POOM: orchestrator 704; tools-builder 159.
- **Owner class:** shumpmaster. Service-Desk 346 (226 merges, 120 plain); Model-Lab 94 (85, 9); POOM 68 (50, 18).
- **Other class:**
  - github-actions[bot]: 86 in Service-Desk, all pull-request merges.
  - "Claude": Service-Desk 31, Model-Lab 1, POOM 17, every one an other-merge commit. The README gives "a tool's default identity" as an example of the other class. The extract does not say which tool or session used the name [N for who is behind it].
- "Claude" is also the committer on 684, 6 and 25 commits whose author is an agent identity.
- Committer names besides "Claude": GitHub, orchestrator, chief-of-staff, builder, definer, check-author, tools-builder.
- All 147 plain commits under the owner's identity have GitHub as committer and change exactly one file [S]:
  - Service-Desk: 72 records added, 46 question/answer files added, 1 built file modified, 1 other added.
  - Model-Lab: 5 records added, 1 record modified, 2 question/answer files added, 1 other added.
  - POOM: 17 records added, 1 other added.

**Per pull request [S as identities; P as who did the work].** Lines are the pull request's changed lines.

| | Service-Desk (312) | Model-Lab (85) | POOM (50) |
|---|---|---|---|
| agent commits only (lines) | 259 (155,242) | 78 (73,170) | 32 (34,073) |
| agent + owner | 45 (137,599) | 6 (11,124) | 15 (39,893) |
| agent + other | 5 (1,697) | 1 (3,674) | 2 (33,067) |
| agent + other + owner | 3 (28,217) | 0 | 1 (2,428) |
| with an owner-identity commit | 48 (15.4%; 165,816 lines) | 6 (7.1%; 11,124) | 16 (32.0%; 42,321) |
| without one | 264 (84.6%; 156,939) | 79 (92.9%; 76,844) | 34 (68.0%; 67,140) |
| all-agent, "other" counted as not agent | 259 (83.0%; 155,242) | 78 (91.8%; 73,170) | 32 (64.0%; 34,073) |
| all-agent, "other" counted as agent | 264 (84.6%; 156,939) | 79 (92.9%; 76,844) | 34 (68.0%; 67,140) |

- Counting plain commits only, the split of agent-only against agent + owner is 264/48, 79/6 and 34/16, with the same lines as the "without" and "with" rows.
- No pull request has a co-author class [S as a count of trailers]. Whether anyone worked alongside is not supported [N]; it would take session records.

**Merging account [S for the account; P for who acted; N for who started a workflow-bot merge].**
- Service-Desk:
  - Owner's account: 226 (72.4%; 318,799 lines). 48 of these have an owner-identity commit (165,816 lines) and 178 do not (152,983).
  - github-actions[bot]: 86 (27.6%; 3,956 lines), none with an owner-identity commit.
- Model-Lab: owner's account 85 (100%; 87,968 lines). 6 have an owner-identity commit (11,124) and 79 do not (76,844).
- POOM: owner's account 50 (100%; 109,461 lines). 16 have an owner-identity commit (42,321) and 34 do not (67,140).
- Merges made outside GitHub (other-merge) carry no lines, since merge commits list no files:
  - Service-Desk 364: 333 with an agent identity as author, 31 "Claude".
  - Model-Lab 38: 37 agent, 1 "Claude".
  - POOM 70: 53 agent, 17 "Claude".

**Commit level [S as identities; P as who did the work].**
- Plain commits:
  - Service-Desk: agent identity 1,962 (94.2%, 407,360 lines); owner identity 120 (5.8%, 698 lines).
  - Model-Lab: agent 839 (98.9%, 108,845 lines); owner 9 (1.1%, 38 lines).
  - POOM: agent 810 (97.8%, 109,425 lines); owner 18 (2.2%, 37 lines).
- All commits. Merge commits are included and carry no lines, so this view has no line count:
  - Service-Desk: agent 83.2%, owner 12.5%, other 4.2%.
  - Model-Lab: 90.2%, 9.7%, 0.1%.
  - POOM: 91.0%, 7.2%, 1.8%.
- Leaving out pull-request merge commits. The lines are as for plain commits, since the other merges carry none:
  - Service-Desk: 93.8%, 4.9%, 1.3%.
  - Model-Lab: 98.9%, 1.0%, 0.1%.
  - POOM: 96.1%, 2.0%, 1.9%.

**When the agents.invalid convention starts [S].** In each repository exactly one non-agent commit comes before the first agents.invalid commit, and it carries the owner's identity.

| | First agents.invalid commit | Owner-identity plain commits after it |
|---|---|---|
| Service-Desk | 2026-09-30T19:04:45Z | 119 |
| Model-Lab | 2026-11-01T16:58:40Z | 8 |
| POOM | 2026-09-24T14:59:13Z | 17 |

**What the extract cannot show [N].**
- Who actually did the work. An identity is not proof of it.
- Whether owner-identity commits were made by the owner or by a session using the owner's settings. All 147 are single-file commits that GitHub committed, and the extract cannot tie them to either.
- Who is behind the "Claude" identity.
- Who started each workflow-bot merge.
- Each of these would take session and workflow logs tied to commits.

## 3. Questions put to the owner

**Summary.** The counts are of files first added under a question or decision label [P]. A label is given by folder name at any depth. So the counts include labelled files in test and template folders, and in a question folder nested in the decision folder, and the extract cannot tell these apart. A question file does not show that the owner was asked, nor a decision file who answered. Matching a question to its answer is an estimate on a weak test [P], and mostly it cannot be done [N].

**Rule.**
- Each labelled file's events are sorted by commit_date.
- A file is counted once, at its first "added". Later "added" events are re-additions.
- A file belongs to a pull request when its first-adding commit is in that pull request's commit list.
- Matching rule (an estimate): a unit (a merged pull request, or a plain commit outside every pull request) that first-adds a decision file and also deletes a question file is a candidate match.
- Moves are estimated as a question file deleted and another added in the same commit with equal line counts.
- Second view: the lines that the first-adding commit added to each file, and the changed lines of the pull requests that first-add one or more.

**Where the labelled files sit.** The extract's own script gives a path a question label when a question folder appears at any depth in it, and a decision label in the same way [S as the rule]. The extract shows only the label, so the folder cannot be seen in it. The source check re-applied that rule to git, which is outside the extract, so its findings are not rechecked here:
- Service-Desk question-label files: 253 in a question folder nested in the decision folder, 190 in the top-level question folder, 97 in the test folder.
- Service-Desk decision-label files: 26 of the 78 in the test folder.
- POOM question-label files: 2 of the 29 in template folders.

**Figures [P: label counts, as above].**

| | Service-Desk | Model-Lab | POOM |
|---|---|---|---|
| Question-label files first added | 540 (Sep 1, Oct 494, Nov 45) | 82 (all Nov) | 29 (Sep 17, Oct 6, Nov 6) |
| lines added at first addition | 8,889 (Sep 9, Oct 7,843, Nov 1,037) | 1,592 | 583 (Sep 362, Oct 90, Nov 131) |
| re-additions | 3 | 3 | 0 |
| deletions | 189 | 41 | 27 |
| still present at the end | 351 | 44 | 2 |
| first-added through merged pull requests | 516 in 175 pull requests (8,643 lines) | 79 in 48 (1,563) | 29 in 12 (583) |
| changed lines of the pull requests that first-add one or more / none | 196,759 / 125,996 | 62,667 / 25,301 | 32,973 / 76,488 |
| first-added outside any pull request | 24 (246 lines) | 3 (29) | 0 |
| first-adding commit by agent / owner identity | 518 / 22 | 80 / 2 | 29 / 0 |
| Decision-label files first added | 78 (Sep 1, Oct 49, Nov 28) | 1 (Nov) | 1 (Sep) |
| lines added at first addition | 978 (Sep 6, Oct 556, Nov 416) | 48 | 6 |
| re-additions | 0 | 0 | 0 |
| deletions | 1 | 0 | 0 |
| first-added through merged pull requests | 52 in 26 pull requests (921 lines) | 0 | 1 in 1 (6) |
| changed lines of the pull requests that first-add one or more / none | 52,386 / 270,369 | 0 / 87,968 | 31,959 / 77,502 |
| first-added outside any pull request | 26 (57 lines) | 1 (48) | 0 |
| first-adding commit by agent / owner identity | 54 / 24 | 1 / 0 | 1 / 0 |

- Service-Desk pull requests by the number of question-label files they first add: none 137; one 99; two 37; three 8; four 11; then one to three pull requests at each count from 5 to 22; one pull request adds 75.
- Model-Lab: none 37; one 31; two 11; three 2; four 2; five 1; seven 1.
- POOM: none 38; one 6; two 4; six 1; nine 1.
- No lines are given for re-additions, deletions and files still present. The lines of a deleted or re-added file measure its size, not an act of asking or answering, so they would add no second view of these counts.

**Matching questions to answers [P: an estimate on a weak test].**

| | Service-Desk | Model-Lab | POOM |
|---|---|---|---|
| Units that first-add a decision and delete a question | 3 (2 one-to-one; 3 decisions, 4 questions) | 0 | 0 |
| Units that first-add a decision and delete no question | 49 | 1 | 1 |
| Units that delete a question and first-add no decision | 78 | 29 | 12 |
| Probable moves of question files (estimated) | 7 | 0 | 1 |

- A move shows as one deletion plus a first addition, so it can inflate first additions.
- No lines are given for the matching. The test is about which labelled files a unit adds and deletes, and a unit's lines would measure the unit, not the match.

**What the extract cannot show [N].**
- Which question a decision answers. Labels are opaque, so beyond the weak same-unit test above no match can be made. It would take the files' content, or a register that links each answer to its question.
- Whether a question was ever shown to the owner. It would take a record of what the owner was shown.
- Who wrote an answer.
- Decisions given in conversation, which leave no file. They would take the conversation logs.
- Which labelled files are test or template copies, since the extract hides the folder. It would take the unlabelled paths, or a label that keeps the kind of folder.

## 4. Merged changes later reverted or changed again

**Summary.** No commit subject starts "Revert" [P]. Two things are counted for 14, 30 and 60 days [P]: later commits that name a pull request's number, and later merged pull requests that change one of the same files. File overlap is a coarse test, since the extract has no line-level history. A named number may be a record or an issue rather than a fix. Many windows are not yet complete, and every 60-day window is incomplete [S]. These are counts of later changes; they do not judge whether the earlier change was at fault.

**Rule.** For each pull request, three tests are run for windows of 14, 30 and 60 days after merged_at. A later commit falls in a window by its commit_date, and a later pull request by its merged_at.
- **Revert:** a commit marked revert (its subject starts "Revert").
- **Named:** a later commit whose mentions_prs includes the pull request's number.
- **File overlap:** a later merged pull request that shares at least one file. This is a coarse test, because a shared file is not a shared line.
- **Left out of the overlap test** (files edited in turn by design), counted as distinct files in pull requests. The rule, by folder name and file-name word:
  - session, handoff and notes labels;
  - anything in the top-level folders for dispatch logs and status;
  - digests: anything in the top-level digest folder, and the upper-case digest file at the top level or in docs;
  - ledgers, registers, logs, changelog and version: the upper-case ledger, lessons, checkpoint, progress, changelog and version files and "_REGISTER" files at the top level or in docs, and any .jsonl file directly in the top-level intake folder;
  - generated files: anything in a folder whose name ends "-extract" (this extract's earlier versions), and package lock files (names ending "-lock.json").
- Left out, by class [S as counts by this rule]:
  - Service-Desk 71 of 2,622 files (5,428 of 322,755 lines): session records 30, handoff records 27, ledgers/registers/logs/changelog/version 6, digests 4, package lock files 2, status records 1, notes 1.
  - Model-Lab 51 of 685 (27,801 of 87,968 lines): handoff 19, this extract's earlier versions 15, session 12, digests 3, ledgers 2.
  - POOM 8 of 575 (3,365 of 109,461 lines): ledgers etc. 5, digests 3.
- After those are left out, 14, 9 and 11 pull requests have no file left to test.
- Supplementary test: overlap with later plain commits outside every pull request.
- A window counts as complete when merged_at plus the window is no later than 2026-11-09T00:00Z.

**Reverts [P].** No commit in any repository has a subject starting "Revert", so the count is 0 in every window. A revert worded otherwise, or made by a new change, is not found. Finding one would take commit messages or a diff-level comparison.

**Named and overlap counts [P: named numbers may be records or issues; overlap is by file, not line; the complete/incomplete split is S].**

| Window | Group | n | Named | Overlap with a later pull request | Named or overlap | Overlap with a later commit outside pull requests |
|---|---|---|---|---|---|---|
| **Service-Desk** | | | | | | |
| 14 days | complete | 230 | 30 | 159 | 167 | 12 |
| 14 days | incomplete | 82 | 7 | 43 | 45 | 1 |
| 30 days | complete | 53 | 5 | 38 | 40 | 12 |
| 30 days | incomplete | 259 | 36 | 165 | 175 | 1 |
| 60 days | all incomplete | 312 | 41 | 203 | 215 | 13 |
| **Model-Lab** (every window incomplete) | | | | | | |
| 14, 30 and 60 days | incomplete | 85 | 17 | 42 | 52 | 0 |
| **POOM** | | | | | | |
| 14 days | complete | 38 | 6 | 26 | 26 | 0 |
| 14 days | incomplete | 12 | 0 | 7 | 7 | 0 |
| 30 days | complete | 23 | 2 | 14 | 14 | 0 |
| 30 days | incomplete | 27 | 4 | 19 | 19 | 0 |
| 60 days | all incomplete | 50 | 6 | 33 | 33 | 0 |

**The same counts in changed lines (second view).** Each cell is the changed lines of the pull requests counted in the matching cell above. The last column is the earlier pull requests' lines in the files that a later pull request in the window changed again. It measures the earlier change's lines in shared files, not how many of those lines the later change touched.

| Window | Group | n | Named | Overlap with a later pull request | Named or overlap | Overlap with a later commit outside pull requests | Earlier lines in shared files |
|---|---|---|---|---|---|---|---|
| **Service-Desk** | | | | | | | |
| 14 days | complete | 266,921 | 87,401 | 258,582 | 259,194 | 16,764 | 161,270 |
| 14 days | incomplete | 55,834 | 4,046 | 49,009 | 49,086 | 853 | 18,090 |
| 30 days | complete | 42,574 | 10,761 | 42,041 | 42,087 | 16,764 | 31,923 |
| 30 days | incomplete | 280,181 | 82,296 | 265,557 | 266,246 | 853 | 149,217 |
| 60 days | all incomplete | 322,755 | 93,057 | 307,598 | 308,333 | 17,617 | 181,140 |
| **Model-Lab** | | | | | | | |
| 14, 30 and 60 days | incomplete | 87,968 | 20,845 | 65,813 | 71,542 | 0 | 9,546 |
| **POOM** | | | | | | | |
| 14 days | complete | 100,016 | 28,977 | 98,373 | 98,373 | 0 | 53,378 |
| 14 days | incomplete | 9,445 | 0 | 8,920 | 8,920 | 0 | 3,103 |
| 30 days | complete | 63,671 | 10,688 | 63,571 | 63,571 | 0 | 42,155 |
| 30 days | incomplete | 45,790 | 18,289 | 43,722 | 43,722 | 0 | 16,875 |
| 60 days | all incomplete | 109,461 | 28,977 | 107,293 | 107,293 | 0 | 59,030 |

- Pull requests merged less than 60 days before 2026-11-09: 312/312, 85/85 and 50/50 [S].
- Of the numbers in mentions_prs, 148/148, 44/44 and 52/53 equal a merged pull-request number in the same repository [S]. Even so, a number may refer to an issue or to another repository's pull request.

**What the extract cannot show [N].**
- Reverts worded any other way.
- Fixes that name nothing.
- Whether a shared file means a change to the same lines. It would take line-level history for each changed file.
- Whether a mention is a fix or only a record, such as filing a review. It would take commit subjects and messages.
- Whether the earlier change was at fault.

## 5. What the records cannot show (limits on every figure above)

**Summary.** These limits hold for every figure above [N for each]. Where the extract's coding may be wrong is listed after them.

- Decisions, approvals and reviews given in conversation, or in pull-request reviews and comments. These are not in the extract.
- Pull-request titles, and pull requests closed without merging.
- The owner's time.
- Work dropped before any commit.
- Fixes that do not name what they fix.

**Where the extract's coding may be wrong:**
- Labelling is by folder name at any depth. A path anywhere under a question or decision folder gets that label. So test and template copies, and question files kept inside the decision folder, count under the question or decision label (the source check's figures are in §3). Any path containing the chief-of-staff role name becomes a handoff label, so an agent-definition file for that role would be classed as a record.
- Copies of record-named files in test and template folders are classed as built by this memo's rule, and they stay in the overlap test (3 distinct files in Service-Desk, 4 in POOM).
- A rename shows as a delete plus an add, so moved files count as new.
- The owner class rests partly on an author-name match.
- A revert is found only by the subject prefix "Revert".
- mentions_prs takes any "#n" in a subject.
- A pull request merged by a local merge, not by GitHub, has no pull-request line.
- Author date differs from commit date on 86, 43 and 18 commits (Service-Desk, Model-Lab, POOM) [S]. All dating here uses commit_date.
- Binary files count no lines.
- The Model-Lab records contain earlier versions of this extract (15 files, left out of the overlap test as generated files).

**What it would take to measure better:** pull-request metadata and review records; line-level history for each changed file; revert detection from the message body or the diff; unlabelled paths, or labels that keep the kind of folder; session and workflow logs tied to commits; and the conversation logs where decisions were given.

## Script (run as `python3 -I q017.py <extract folder>`; it reads only the extract)

The script classes paths by rules on folder names and file-name words, and it lists no single path or file. Its output for every figure of the first round is unchanged. This was checked against that round's script on all 4,292 distinct paths: each gets the same kind and the same left-out class. The script also prints the new line views.

```python
# Q-017 counts. Reads only the extract folder. Run: python3 -I q017.py <extract folder>
import json, collections, datetime as dt, sys
D=sys.argv[1].rstrip("/")+"/"   # the extract folder
REPOS=["Service-Desk","Model-Lab","Personal-Org-Operating-Model"]
REF=dt.datetime(2026,11,9,tzinfo=dt.timezone.utc)   # question's "as of" date, 00:00 UTC
def T(s): return dt.datetime.strptime(s,"%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=dt.timezone.utc)
# Path rules by folder name and file-name word; no single path is listed.
CODE_EXT=(".py",".js",".mjs",".sh",".yml",".yaml",".toml",".json",".jsonl.lock",".woff2",".css")
LABEL_QA=("<questions:","<decisions:")
LABEL_REC=("<cos-session:","<cos-handoff:","<notes:")
LABEL_PLAN=("<project-plan:","<ideas:")
TEMPLATE_TOP={"template","template-v3","portfolio-template"}            # POOM's shipped kit folders
REC_TOP={"reviews","dispatch-log","status","digest","queue","triage","intake"}
REC_DOCS={"briefs","reports","handover","trials","archive","checkpoints","audit"}
REC_DESIGN_SUB={"builds","audits"}; REC_DESIGN_PREFIX=("audit-","inventory-")
RES_TOP={"research","library","experiments"}
PLAN_TOP={"specs"}; PLAN_DOCS={"proposals","sprints","gates","design"}
BUILT_TOP={"src","tests","tools","scripts",".github",".claude"}
REC_WORDS={"LEDGER","DIGEST","LESSONS","CHECKPOINT","PROGRESS","CHANGELOG","VERSION"}
PLAN_WORDS={"MISSION","SCOPE"}
def parts(p): return p.split("/")
def stem(p):
    b=parts(p)[-1]; return b[:-3] if b.endswith(".md") else b
def caps(p): s=stem(p); return s.replace("_","").replace("-","").isalpha() and s.isupper()
def rec_name(p):  # the repository's own upper-case record file (at the top or in the docs folder): ledger, digest, lessons,
    # checkpoint, progress, changelog, version, or a name ending _REGISTER or _REVIEW. Copies in template or test folders are not.
    s=stem(p); q=parts(p); return caps(p) and (len(q)==1 or q[0]=="docs") and (s in REC_WORDS or s.endswith(("_REGISTER","_REVIEW")))
def kind(p):
    s=parts(p); top=s[0]; sub=s[1] if len(s)>2 else None
    if p.startswith(LABEL_QA): return "owner_qa"
    if p.startswith(LABEL_REC): return "records"
    if p.startswith(LABEL_PLAN): return "plan"
    if top in TEMPLATE_TOP and len(s)>1: return "built"
    if len(s)>1 and top in REC_TOP: return "records"
    if top=="docs" and sub in REC_DOCS: return "records"
    if top=="docs" and len(s)>2 and s[1]=="design" and (s[2] in REC_DESIGN_SUB and len(s)>3 or (len(s)==3 and s[2].startswith(REC_DESIGN_PREFIX))): return "records"
    if rec_name(p): return "records"
    if (top in RES_TOP and len(s)>1) or (top=="docs" and sub=="research") or (top=="docs" and sub=="design" and len(s)>3 and s[2]=="references"): return "research"
    if (top in PLAN_TOP and len(s)>1) or (top=="docs" and sub in PLAN_DOCS) or (top=="docs" and len(s)==2 and caps(p) and stem(p) in PLAN_WORDS): return "plan"
    if (top in BUILT_TOP and len(s)>1) or (top=="governance" and sub=="checks") or (len(s)==1 and p.startswith(".") and p.endswith("ignore")) or p.endswith(CODE_EXT) \
       or (top=="governance" and len(s)==2 and caps(p) and stem(p).endswith("_VERSION")): return "built"
    return "other"
def by_design(p):
    s=parts(p); top=s[0]
    if p.startswith("<cos-session:"): return "session records"
    if p.startswith("<cos-handoff:"): return "handoff records"
    if p.startswith("<notes:"): return "notes"
    if top=="dispatch-log" and len(s)>1: return "dispatch logs"
    if top=="status" and len(s)>1: return "status records (generated/updated each run)"
    if (top=="digest" and len(s)>1) or (rec_name(p) and stem(p)=="DIGEST"): return "digests"
    if (rec_name(p) and stem(p)!="DIGEST" and not stem(p).endswith("_REVIEW")) or (top=="intake" and len(s)==2 and p.endswith(".jsonl")):
        return "ledgers, registers, logs, changelog and version"
    if any(x.endswith("-extract") for x in s[:-1]) or s[-1].endswith("-lock.json"): return "generated files"
    return None
KINDS=["built","plan","research","records","owner_qa","other"]
def lines(f): return (f["added"] or 0)+(f["removed"] or 0)
def pct(a,b): return f"{a}/{b} ({100*a/b:.1f}%)" if b else f"{a}/0"
OUT=[]
def pr_(*a): print(*a)
G=collections.Counter()
for r in REPOS:
    C=[json.loads(l) for l in open(D+r+".commits.jsonl")]
    P=[json.loads(l) for l in open(D+r+".prs.jsonl")]
    H={c["hash"]:c for c in C}
    order={c["hash"]:i for i,c in enumerate(reversed(C))}   # git log order reversed = oldest first
    P.sort(key=lambda p:p["merged_at"])
    inpr={}
    for p in P:
        for h in p["commits"]: inpr[h]=p["pr"]
    pr_("\n"+"="*30,r,"commits",len(C),"merged PRs",len(P))
    # ---------- 1. units
    pr_("\n[1] PRs per month of merged_at (count / changed lines)")
    m=collections.Counter(); ml=collections.Counter()
    for p in P:
        k=p["merged_at"][:7]; m[k]+=1; ml[k]+=sum(lines(f) for f in p["files"])
    for k in sorted(m): pr_("  ",k,m[k],ml[k])
    pr_("   total",len(P),sum(ml.values()))
    kc=collections.Counter(); kl=collections.Counter(); kpl=collections.Counter(); single=collections.Counter(); singlel=collections.Counter()
    nmulti=0; combos=collections.Counter()
    for p in P:
        ks=collections.Counter()
        for f in p["files"]: ks[kind(f["path"])]+=lines(f)
        ks_set=set(ks) if p["files"] else {"(no files)"}
        tot=sum(ks.values())
        for k in ks_set: kc[k]+=1; kl[k]+=ks.get(k,0); kpl[k]+=tot
        if len(ks_set)>1: nmulti+=1
        else: single[next(iter(ks_set))]+=1; singlel[next(iter(ks_set))]+=tot
        combos[tuple(sorted(ks_set))]+=1
    pr_("   by kind (PRs counted under each kind they touch; lines in that kind's files; lines of those PRs in total)")
    for k in KINDS+["(no files)"]:
        if kc[k] or single[k]: pr_(f"     {k:9s} PRs {kc[k]:4d} lines_in_kind {kl[k]:7d} pr_total_lines {kpl[k]:7d} | single-kind PRs {single[k]} lines {singlel[k]}")
    pr_("   flagged (more than one kind):",nmulti,"of",len(P))
    pr_("   commonest kind combinations:",combos.most_common(6))
    # commits outside merged PRs
    out=[c for c in C if c["hash"] not in inpr and c["kind"]=="plain"]
    om_in=[c for c in C if c["kind"]=="other-merge" and c["hash"] in inpr]
    om_out=[c for c in C if c["kind"]=="other-merge" and c["hash"] not in inpr]
    pl_in=[c for c in C if c["kind"]=="plain" and c["hash"] in inpr]
    pr_("\n[1] commits: merge-pr",sum(c["kind"]=="merge-pr" for c in C),
        "| plain in a merged PR",len(pl_in),"lines",sum(lines(f) for c in pl_in for f in c["files"]),
        "| plain in no merged PR",len(out),"lines",sum(lines(f) for c in out for f in c["files"]),
        "| other-merge inside a PR",len(om_in),"| other-merge outside any PR",len(om_out))
    pr_("    plain-in-no-PR by month",sorted(collections.Counter(c["commit_date"][:7] for c in out).items()),
        "by author class",dict(collections.Counter(c["author_class"] for c in out)))
    okind=collections.Counter(); 
    for c in out:
        for k in {kind(f["path"]) for f in c["files"]}: okind[k]+=1
    pr_("    plain-in-no-PR commits touching each kind",dict(okind))
    # outside-PR commits: are they after the last merge (pending) ?
    lastm=P[-1]["merged_at"]
    pr_("    plain-in-no-PR committed after the last merged PR:",sum(c["commit_date"]>lastm for c in out))
    pr_("    binary file entries (null line counts):",sum(1 for c in C for f in c["files"] if f["added"] is None))
    # ---------- 2. who
    pr_("\n[2] identities (author names by class; committer names)")
    names=collections.defaultdict(collections.Counter)
    for c in C: names[c["author_class"]][c["author"]]+=1
    for k in names: pr_("   ",k,dict(names[k]))
    pr_("    committers",dict(collections.Counter(c["committer"] for c in C)))
    pr_("    'other' authors by commit kind",dict(collections.Counter((c["author"],c["kind"]) for c in C if c["author_class"]=="other")))
    pr_("    agent-authored commits whose committer is 'Claude'",sum(1 for c in C if c["author_class"]=="agent" and c["committer"]=="Claude"))
    fa=min(c["commit_date"] for c in C if c["author_class"]=="agent")
    pr_("    first agents.invalid commit",fa,"| non-agent commits before it",sum(1 for c in C if c["commit_date"]<fa and c["author_class"]!="agent"),
        "| owner plain commits after it",sum(1 for c in C if c["commit_date"]>=fa and c["author_class"]=="owner" and c["kind"]=="plain"))
    # per PR
    cat=collections.Counter(); catl=collections.Counter()
    any_owner=any_other=0; plain_only=collections.Counter()
    merger=collections.Counter(); merger_x=collections.Counter()
    merger_l=collections.Counter(); owner_l=collections.Counter(); plain_only_l=collections.Counter()
    for p in P:
        cc=collections.Counter(H[h]["author_class"] for h in p["commits"])
        pc=collections.Counter(H[h]["author_class"] for h in p["commits"] if H[h]["kind"]=="plain")
        lab="+".join(sorted(cc)); cat[lab]+=1; catl[lab]+=sum(lines(f) for f in p["files"])
        if cc["owner"]: any_owner+=1
        if cc["other"]: any_other+=1
        plain_only["+".join(sorted(pc)) or "(none)"]+=1
        merger[(p["merge_commit_author"],p["merge_commit_author_class"])]+=1
        merger_x[(p["merge_commit_author"],"has owner commit" if cc["owner"] else "no owner commit")]+=1
        pl=sum(lines(f) for f in p["files"])
        merger_l[(p["merge_commit_author"],"has owner commit" if cc["owner"] else "no owner commit")]+=pl
        owner_l["has owner commit" if cc["owner"] else "no owner commit"]+=pl
        plain_only_l["+".join(sorted(pc)) or "(none)"]+=pl
    n=len(P)
    pr_("    PRs by author classes of their commits (incl. other-merge):",dict(cat),"lines",dict(catl))
    pr_("    PRs by author classes of their plain commits only:",dict(plain_only))
    pr_("    PRs with >=1 owner-identity commit",pct(any_owner,n),"| without",pct(n-any_owner,n))
    pr_("    PRs with >=1 'other' commit",pct(any_other,n),
        "| all-agent if 'other' counted as non-agent:",pct(cat.get("agent",0),n),
        "| all-agent if 'other' counted as agent:",pct(sum(v for k,v in cat.items() if "owner" not in k),n))
    pr_("    co-author classes on PRs:",dict(collections.Counter(tuple(p["co_author_classes"]) for p in P)))
    pr_("    merging account:",{f"{a} ({b})":pct(v,n) for (a,b),v in merger.items()})
    pr_("    merging account x owner commit:",dict(merger_x),"lines",dict(merger_l))
    pr_("    lines of PRs with / without an owner-identity commit:",dict(owner_l),"| plain-only split lines:",dict(plain_only_l))
    pr_("    other-merge commits (merges outside GitHub):",len(om_in)+len(om_out),"by author",dict(collections.Counter((c["author"],c["author_class"]) for c in om_in+om_out)),
        "by committer",dict(collections.Counter(c["committer"] for c in om_in+om_out)))
    # commit level
    pls=[c for c in C if c["kind"]=="plain"]
    pr_("    commit level, plain commits by class:",{k:pct(v,len(pls)) for k,v in collections.Counter(c["author_class"] for c in pls).items()},
        "lines",{k:sum(lines(f) for c in pls if c["author_class"]==k for f in c["files"]) for k in sorted({c["author_class"] for c in pls})})
    pr_("    commit level, all commits by class:",{k:pct(v,len(C)) for k,v in collections.Counter(c["author_class"] for c in C).items()},
        "| excluding merge-pr commits:",{k:pct(v,len(C)-n) for k,v in collections.Counter(c["author_class"] for c in C if c["kind"]!="merge-pr").items()})
    pr_("    plain commits in a PR by class",dict(collections.Counter(c["author_class"] for c in pl_in)),
        "| plain commits in no PR by class",dict(collections.Counter(c["author_class"] for c in out)))
    # ---------- 3. questions / decisions
    pr_("\n[3] owner questions and decisions")
    ev=collections.defaultdict(list)   # path -> [(date,ord,status,hash)]
    for c in C:
        for f in c["files"]:
            if f["path"].startswith(("<questions:","<decisions:")):
                ev[f["path"]].append((c["commit_date"],order[c["hash"]],f["status"],c["hash"],f))
    first={}; readd=collections.Counter(); deletes=collections.Counter(); present=collections.Counter()
    firstadd_commits={}
    for p_,es in ev.items():
        es.sort(); lab=p_[1:p_.index(":")]
        adds=[e for e in es if e[2]=="added"]
        if adds:
            first[p_]=adds[0]; firstadd_commits.setdefault(adds[0][3],[]).append(p_)
            readd[lab]+=len(adds)-1
        else: readd[lab+"_never_added_in_extract"]+=1
        deletes[lab]+=sum(e[2]=="deleted" for e in es)
        if es[-1][2]!="deleted": present[lab]+=1
    for lab in ("questions","decisions"):
        fs=[(p_,e) for p_,e in first.items() if p_.startswith("<"+lab)]
        pr_(f"   {lab}: files first added {len(fs)}; per month",sorted(collections.Counter(e[0][:7] for _,e in fs).items()),
            "; re-additions",readd[lab],"; deletions",deletes[lab],"; present at end",present[lab],
            "; touched but never added",readd[lab+"_never_added_in_extract"])
        viapr=collections.Counter(inpr.get(e[3]) for _,e in fs)
        npr=sum(1 for k in viapr if k is not None)
        pr_(f"     first-added through a merged PR: {sum(v for k,v in viapr.items() if k is not None)} files in {npr} PRs (of {len(P)}); outside any merged PR: {viapr.get(None,0)}")
        pr_("     lines added by the first-adding commits (second view):",sum(e[4]["added"] or 0 for _,e in fs),
            "per month",sorted({m_:sum(e[4]["added"] or 0 for _,e in fs if e[0][:7]==m_) for m_ in {e[0][:7] for _,e in fs}}.items()),
            "| via a merged PR",sum(e[4]["added"] or 0 for _,e in fs if inpr.get(e[3]) is not None),
            "| outside",sum(e[4]["added"] or 0 for _,e in fs if inpr.get(e[3]) is None))
        prl=collections.Counter(); 
        for p in P: prl["adds >=1" if viapr[p["pr"]] else "adds none"]+=sum(lines(f) for f in p["files"])
        pr_("     changed lines of the PRs that first-add >=1 / none:",dict(prl))
        dist=collections.Counter(viapr[p['pr']] for p in P)
        pr_("     PRs by number of first-added files:",sorted(dist.items()))
    # moves: same commit deletes a question file and adds one with equal line count
    mv=0; mvd=0
    for c in C:
        dq=[f for f in c["files"] if f["path"].startswith("<questions:") and f["status"]=="deleted"]
        aq=[f for f in c["files"] if f["path"].startswith("<questions:") and f["status"]=="added"]
        used=set()
        for d in dq:
            for i,a in enumerate(aq):
                if i not in used and a["added"]==d["removed"]: used.add(i); mv+=1; break
        dd=[f for f in c["files"] if f["path"].startswith("<decisions:") and f["status"]=="deleted"]
        ad=[f for f in c["files"] if f["path"].startswith("<decisions:") and f["status"]=="added"]
        u2=set()
        for d in dd:
            for i,a in enumerate(ad):
                if i not in u2 and a["added"]==d["removed"]: u2.add(i); mvd+=1; break
    pr_("   probable moves (same commit: one deleted, one added, equal line counts): questions",mv,"decisions",mvd)
    # matching: units (PR, or commit outside PRs) that add a decision and delete a question
    units=[("pr",p["pr"],p["commits"]) for p in P]+[("commit",c["hash"][:8],[c["hash"]]) for c in out]
    both=one2one=dec_only=q_del_only=0; dec_in_both=q_in_both=0
    for typ,idn,hs in units:
        qd=sum(1 for h in hs for f in H[h]["files"] if f["path"].startswith("<questions:") and f["status"]=="deleted")
        da=sum(1 for h in hs if h in firstadd_commits for p_ in firstadd_commits[h] if p_.startswith("<decisions:"))
        if qd and da:
            both+=1; dec_in_both+=da; q_in_both+=qd
            if qd==1 and da==1: one2one+=1
        elif da: dec_only+=1
        elif qd: q_del_only+=1
    pr_("   units (merged PRs + plain commits in no PR) that first-add a decision AND delete a question:",both,
        f"(1:1 {one2one}; decisions in them {dec_in_both}, questions deleted in them {q_in_both})",
        "| first-add decision, no question deleted:",dec_only,"| delete question, no decision added:",q_del_only)
    # ---------- 4. later change
    pr_("\n[4] later changes")
    excl=collections.defaultdict(set)
    for p in P:
        for f in p["files"]:
            b=by_design(f["path"])
            if b: excl[b].add(f["path"])
    pr_("   left out: changed lines of those files in merged PRs",sum(lines(f) for p in P for f in p["files"] if by_design(f["path"])),
        "of",sum(lines(f) for p in P for f in p["files"]))
    pr_("   left out (distinct files):",{k:len(v) for k,v in excl.items()},"total",sum(len(v) for v in excl.values()),
        "of",len({f["path"] for p in P for f in p["files"]}))
    FS={p["pr"]:{f["path"] for f in p["files"] if not by_design(f["path"])} for p in P}
    mention=collections.defaultdict(list)
    prnums={p["pr"] for p in P}
    allm=[x for c in C for x in c["mentions_prs"]]
    pr_("   mentions_prs numbers:",len(allm),"of which a merged PR number in this repo:",sum(x in prnums for x in allm))
    for c in C:
        for x in c["mentions_prs"]: mention[x].append(c)
    for W in (14,30,60):
        res=collections.Counter()
        for p in P:
            t0=T(p["merged_at"]); t1=t0+dt.timedelta(days=W); comp=t1<=REF
            shared=set().union(*[FS[p["pr"]]&FS[q["pr"]] for q in P if t0<T(q["merged_at"])<=t1])
            ov=bool(shared)
            ovd=any(FS[p["pr"]]&{f["path"] for f in c["files"]} for c in out if t0<T(c["commit_date"])<=t1)
            nm=any(t0<T(c["commit_date"])<=t1 for c in mention[p["pr"]])
            rv=any(c["revert"] and t0<T(c["commit_date"])<=t1 for c in C)
            pl=sum(lines(f) for f in p["files"])
            for tag,cond in (("all",True),("complete" if comp else "incomplete",True)):
                res[(tag,"L_n")]+=pl; res[(tag,"L_named")]+=pl*nm; res[(tag,"L_ov")]+=pl*ov; res[(tag,"L_either")]+=pl*(ov or nm); res[(tag,"L_direct")]+=pl*ovd
                res[(tag,"L_shared")]+=sum(lines(f) for f in p["files"] if f["path"] in shared)
                res[(tag,"n")]+=1
                res[(tag,"overlap_later_PR")]+=ov; res[(tag,"overlap_direct_commit")]+=ovd
                res[(tag,"named")]+=nm; res[(tag,"revert")]+=rv; res[(tag,"overlap_PR_or_named")]+=(ov or nm)
                res[(tag,"no_checked_files")]+=(not FS[p["pr"]])
        for tag in ("all","complete","incomplete"):
            if res[(tag,"n")]:
                pr_(f"   {W}d {tag:10s} n={res[(tag,'n')]:3d} revert={res[(tag,'revert')]} named={res[(tag,'named')]} "
                    f"overlap_laterPR={res[(tag,'overlap_later_PR')]} overlap_or_named={res[(tag,'overlap_PR_or_named')]} "
                    f"overlap_direct_commit={res[(tag,'overlap_direct_commit')]} prs_with_no_checked_files={res[(tag,'no_checked_files')]}")
                pr_(f"       lines of those PRs: n={res[(tag,'L_n')]} named={res[(tag,'L_named')]} overlap_laterPR={res[(tag,'L_ov')]} "
                    f"overlap_or_named={res[(tag,'L_either')]} overlap_direct_commit={res[(tag,'L_direct')]} | lines of the earlier PRs in files a later PR changed again={res[(tag,'L_shared')]}")
    pr_("   PRs merged < 60 days before",REF.date(),":",sum(T(p["merged_at"])>REF-dt.timedelta(days=60) for p in P),"of",len(P))
    # ---------- extra checks used in the memo
    pr_("\n[extra]")
    pr_("   owner plain commits: committers",dict(collections.Counter(c["committer"] for c in pls if c["author_class"]=="owner")),
        "files per commit",dict(collections.Counter(len(c["files"]) for c in pls if c["author_class"]=="owner")),
        "kind/status of their files",dict(collections.Counter((kind(f["path"]),f["status"]) for c in pls if c["author_class"]=="owner" for f in c["files"])))
    pr_("   other-merge commits outside any PR that name a merged PR:",sum(any(x in prnums for x in c["mentions_prs"]) for c in om_out))
    nums=sorted(prnums); pr_("   PR numbers",nums[0],"to",nums[-1],"; numbers in that range with no merged PR line:",len(set(range(nums[0],nums[-1]+1))-prnums))
    pr_("   label files first added, by author class of the adding commit:",
        dict(collections.Counter((p_[1:p_.index(":")],H[e[3]]["author_class"]) for p_,e in first.items())))
```

---

## Change list (item: what changed → which correction it answers)

- **Marks (new block at top):** replaced "grade A" with the question's three marks [S]/[P]/[N]. Every figure, table and heading now carries one, and each [P]/[N] says what is missing and what it would take to measure it. → Correction 1 (marking).
- **Opening paragraph:** "Agent identities wrote" / "the owner's identity wrote" became "carry an agent identity as author" / "carry the owner's identity". It now says file overlap is a coarse test and not a measure of rework, and gives the 14-day incomplete groups (82 / 85 / 12, and their share of the 202 / 42 / 33 and 37 / 17 / 6). The label figures are worded as counts of labelled files, with where they sit (test folder, question folder nested in the decision folder), attributed to the source check's git finding. The "every figure is grade A" sentence was replaced. The whole paragraph was re-read against LL-71. → Corrections 1 and 2.
- **Item summaries (new, §1–§5):** a summary line for each item, worded no more strongly than its figures and marked. Re-read against LL-71. → Corrections 1 and 2.
- **§1 rule text:** rewritten as a numbered list in the script's exact order. The template/kit rule now sits after all label rules and before the review, dispatch and brief folders. The list now includes the inventory- files under records, the .jsonl.lock extension, and the governance _VERSION file under built. → Correction 3.
- **Script:** the named file lists (the eleven files the check listed and the extract folder) were replaced by rules: upper-case record-word file names at the top level or in docs, a "-extract" folder suffix, a "-lock.json" suffix, .jsonl files directly in intake, a top-level ignore file, and a governance "_VERSION" name. Folder prefixes became folder-name classes. I checked it against the round-1 script on all 4,292 distinct paths: 0 differ in kind or left-out class. All round-1 figures are reproduced. The only differences are dict key order. → Correction 4.
- **§4 left-out list:** now stated as the rule, not as files. It now includes lines (5,428 / 27,801 / 3,365). The Model-Lab "generated" note is corrected: the 15 are all this extract's earlier versions, not lockfiles. Service-Desk's 2 are package lock files. → Corrections 4 and 5, plus a wording fix I found myself.
- **Second view of lines:**
  - §2: lines for the with/without owner-commit rows, the all-agent rows, the merging account × owner commit split, and the plain-only split. It says why all-commit shares have no lines (merge commits list no files).
  - §3: lines added at first addition (per month, through a PR, outside), and the lines of PRs that first-add one or more files against none. It says why there are no lines for re-additions, deletions and matching.
  - §4: a full second table in lines, plus the earlier PRs' lines in shared files.
  → Correction 5.
- **§3 "Where the labelled files sit" (new) and §5 coding doubts:** the extract's labelling rule works at any depth, and the source check's folder counts are given by kind of folder, with no paths. §5 also notes that record-named copies in test and template folders (3 in Service-Desk, 4 in POOM) are classed as built. → Correction 2 (label counts).
- **§2 "Claude":** no longer asserted to be "a tool's default identity". It is now tied to the README's example, with who is behind it marked [N]. → Correction 2 (wording strength).
- **Header:** dropped the round-1 Orchestrator italic line and the brief reference. The Orchestrator should add its own recording line.

Working files (all under /tmp/q017/): q017.py (revised script), new.out (its output), orig.py and orig.out (round 1), cmp.py (the path-rule equivalence check), memo.md (this memo). Nothing in /home/user was changed.

Total tokens: I cannot see my token count.
