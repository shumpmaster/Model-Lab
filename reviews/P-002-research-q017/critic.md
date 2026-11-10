Verdict: PASS

*The Critic's neutrality check (D-055) of research question Q-017 for P-002: round 1 (FAIL), round 2 (FAIL), round 3 (FAIL; the stop rule applies), then the deciding check the owner ruled (FAIL), then the deciding check of the narrowed question (FAIL), then the deciding check of the fixed extract (PASS); briefs 216 to 218, 221, 224 and 228. After the last, its points 2A, 2B and 3a to 3e were applied as stated limits and wording. Each round a fresh session on a different model from the question's writer, started by the Chief of Staff (session_01QBwHGNSLmSrYQgS6BPjV8p), 2026-11-09. Recorded verbatim by the Orchestrator from each helper's return; each round's own verdict line is recorded as "The round's verdict was …" (LL-68). The verdict above is the latest round's. The review-file check refuses the verdict label anywhere but at a line's start, so the deciding check's one quotation of a verdict line inside a sentence is shown as `Verdict : PASS | FAIL …` (as in reviews/P-001-harness-trade-offs/critic.md).*

## Round 1 (brief 216)

The round's verdict was FAIL.

I checked /home/user/Model-Lab/research/Q-017.md against research/_QUESTION.md and against research/Q-008.md, Q-006-memo.md and Q-008-memo.md. I did not open docs/projects/, docs/PROJECT.md, the contents of decisions/ or questions/, or any ideas/ folder. The question needs a rework before it goes to a Researcher. Line numbers refer to Q-017.md.

**1. Neutrality**

1. [Blocking] Lines 22-28, "The decision it serves" and "What each answer would change". These name a "value target for the screening project" and list the three figures it will aim at: the agents' share, how often the supervisor steps in, and whether work holds up. That tells the Researcher a target exists, which figures it concerns, and which direction is wanted (more agent work, less supervisor intervention, little rework). The Researcher also learns the "screening project" exists, which is project content. Q-008 carried similar text and passed, but this is the exact signal D-055 bars. Either keep this section out of the Researcher's copy, or reduce it to a neutral purpose such as "a baseline description of the records". I am not rewriting it.
2. [Non-blocking] Line 7 and line 13. "Need correcting later", "corrected" and "held up" treat any later change as a fault fixed. Item 5 can show that a later change happened, not that the earlier work was faulty. A plainer count would be "reverted, or changed by a later pull request that names it".
3. [Non-blocking] Line 11. The only headline share is "no commit by the supervisor's identity", and only "the others" are listed. That presents agent-alone work as the measure of interest and is asymmetric. Ask for both ends (the share with and without a supervisor commit), and for commit-level counts as well as pull-request-level ones.
4. [Non-blocking] Line 16. "Report every figure on equal terms" is good and matches Q-008. No numeric target appears in the question. Line 11 pairs "step in" with "carry", which reads as autonomy against intervention; a neutral label such as "commits by identity" would avoid that.

**2. Gaps and repeatability**

5. [Blocking] Line 11, item 2. "The supervisor's own identity" is never named, so the count cannot be repeated.
   - Identity is not the same as who did the work. A Claude Code session may commit under the owner's git configuration, which would count as the supervisor. Agent work from before the agents.invalid convention would land in "any other identity".
   - Orchestrator and Chief of Staff commits are also agents.invalid (per the CLAUDE.md files).
   - Ask for the exact addresses and names, and a rule for merge commits, GitHub web-merge identities, and co-author trailers. Say this proxy is a limit under item 6 (line 14), whose examples omit it.
6. [Blocking] Line 11 and line 7. "Step in" is measured only by supervisor commits and question files.
   - The most direct record of a supervisor step at merge is who merged the pull request (merged_by), plus supervisor review comments. Neither is mentioned. Without them, a pull request the supervisor merged by hand would count as "agents carried it".
   - Approvals and questions given in chat are not in the records, and the supervisor's time is the only item 6 example that touches this.
7. [Blocking] Line 9, line 5 and line 13. There is no as-of date, and the question does not say how to treat recent merges.
   - Q-006 and Q-008 are dated 2026-11-01 and the repositories keep moving.
   - Item 5's 30-day window cannot be judged for work merged within 30 days of the cut-off. Ask for an as-of date and for merges inside the window to be reported separately.
8. [Blocking] Line 13, item 5. "Edits the same lines within 30 days" is not repeatable.
   - It does not say how overlap is measured (blame, hunk overlap, or file level).
   - Specs and logs are large files that are edited iteratively by design (Q-006 notes a 22,883-line spec), as are regenerated digests. Planned follow-on drafts and extensions would register as corrections.
   - There is no rule separating "correction" from "planned later work". The lessons logs are subjective evidence, and "and its equivalents" is undefined.
   - The 30-day figure is not shown to be anything but a chosen window; ask for a sensitivity range such as 14, 30 and 60 days.
9. [Blocking] Line 15, item 4. The rounds count is left undefined where the earlier memos had to define it.
   - Q-008 fixed "piece", "round", "passed at first try", later-added checks, focused and confirmation checks, and pieces with no verdict.
   - Q-006 notes that the stop rule means three plan rounds and three build rounds, and that "past it" needs a definition.
   - Q-017 says only "three failed rounds".
   - Without these definitions the figures will not be repeatable or comparable with Q-008.
10. [Blocking] Line 15 against the records Q-006 and Q-008 relied on. Item 4 omits the dispatch-log. For the scripted research items the log is the only per-round record, because research/*-source-check.md keeps only the last verdict (Q-008-memo §5, triage/Q-011.md:26). It is not in the "Records to read" (line 18), so the counts will be systematically short. Pull-request verdict files also duplicate series round files. Q-008 needed an explicit frame rule for this, and Q-017 gives none, so double counting is likely.
11. [Non-blocking] Line 9, item 1.
    - Pull requests count equally whatever their size, and no size measure is offered as a secondary view.
    - The question does not say how to treat pull requests closed unmerged, direct pushes to main with no pull request, or pull requests that fit two classes. Item 6 mentions only "work done outside the records".
    - Dropped work, which Q-006 §7 flags as a survivorship bias, is not mentioned. Item 4's pieces and item 1's merged pull requests are different populations, so say how they join.
12. [Non-blocking] Line 11, item 3.
    - "Filed" and "answered" are counted from file names and dates. A question file is not proof the supervisor was asked, and an answer file does not show who answered.
    - Q-006 recorded decisions made by proxy. Contents are barred, so this cannot be resolved, but it should be listed as a limit.
    - Say how a question file is matched to its answer, and how a file is attached to a pull request.

**3. Reading limits and blindness**

13. [Blocking] Line 18. The permitted sources carry the hoped-for answer, the Chief of Staff's recommendation and the owner's leanings.
    - "Git history" and "pull request merge commits" expose commit subjects, pull request titles, and diffs of the barred paths. Only commit dates and file names are allowed there, so the question must say how (for example, list dates and names without subjects or patches). Pull request titles are needed for classing, which conflicts with this unless stated.
    - sessions/ includes Chief of Staff session records. Lessons logs record rulings. The Q-008 memo's disclosure shows that reviews/ files quote project content, and that reviews/Q-008/critic.md quoted an earlier draft of that question. So reviews/Q-017* and sessions/chief-of-staff would let the Researcher see this question's own critique.
    - Git history also holds earlier versions of docs/projects/ and docs/PROJECT.md. Say these may not be read through history.
    - Exclude, by path: reviews/Q-017*, research/Q-017*, Chief of Staff notes, sessions/chief-of-staff and any *-notes.md. Or name the permitted ones.
14. [Non-blocking] Line 18. The earlier memos include opinions and recommendations (Q-006 §8, Q-008 "where cause can be shown") and refer to the P-001 project. Reading them before counting risks anchoring. The Q-008 memo had the same issue and disclosed it. Consider requiring the counts first, with the memos opened only for the comparison.
15. [Non-blocking] Name-only reading is workable for questions/ and decisions/ on file names and commit dates. But file names themselves can carry project content (for example P-001-harness-landing-style ids). Say names may be used only as counts and dates, and not reported.

**4. Form**

16. [Non-blocking] The sections match the form: header, "The question", "The decision it serves", "What each answer would change", and the topics and depth lines. The depth line carries extra words after the number, which is harmless. The topic "measurement" cannot be checked: I found no library files in /home/user/Model-Lab to match it against, and the other topics match Q-008's.

**5. Plainness for a Researcher who knows nothing of the project**

17. [Non-blocking] Several terms are undefined or inconsistent:
    - "supervisor" (lines 7, 11, 13) and "owner" (line 9, "owner question or answer") look like two people;
    - "operating model", "built work", "plan", "records only", "stop rule", "lessons logs and their equivalents", "source-check" and "agent identity";
    - "piece" and "passing" in item 4.
    The file does not say what reviews/ rounds are, or what sessions/ and docs/briefs/ hold or why they are relevant. Records are named as shumpmaster/... but the earlier memos use local paths, so say which the Researcher has.
18. [Blocking] "The screening project" (line 23) is meaningless to a blind Researcher and should not appear (see finding 1).

**6. Overlap with Q-006 and Q-008**

19. [Non-blocking] Item 4 largely repeats Q-006 §4 and "Rounds past the stop rule", and Q-008 §2. Its new part is tying rounds to merged pull requests and extending past 2026-11-01. Items 1 to 3 and 5 are new, so this is not a re-run under D-047, but the question should say item 4 is a recount. It should also say how the unit changes (series or piece to merged pull request) so differences from the earlier figures can be explained. The earlier memos' known traps (11 of 341 files with no Verdict, duplicated pull request files, missing round files, the dispatch log ending 2026-10-08, absent records of closed items) belong in item 6.

**Citation check.** Not applicable (this is a question check, not a phase gate).

Blocking findings: 1, 5, 6, 7, 8, 9, 10, 13 and 18. The rest are non-blocking.

## Round 2 (brief 217)

The round's verdict was FAIL.

Round 2 check of /home/user/Model-Lab/research/Q-017.md and its extract (README.md, extract.py, three .jsonl files). I did not open docs/projects/, docs/PROJECT.md, the contents of decisions/ or questions/, or any ideas/ folder. I read the extract's subjects and paths with searches only. Line numbers refer to Q-017.md unless stated.

**Round 1 findings: answered or not**
- 1 (decision and value-target text; blocking): answered. Lines 37-43 are now neutral. No target, direction or project name appears.
- 2 ("corrected" wording): answered. Line 27 says "This counts later changes; it does not judge whether the earlier change was at fault."
- 3 (asymmetric share): answered. Line 7 and line 13 ask for both ends, and line 13 asks for commit-level counts as well.
- 4 (neutral labels): answered. "Report every figure on equal terms" is at line 31.
- 5 (identities; blocking): answered in the question at line 12 and line 14. The extract's classing has a gap, see 7 below.
- 6 (who merged; blocking): partly answered. Line 13 uses the merge commit's author, but it does not cover squash merges, see 1 below. Review comments are named as a limit at line 33.
- 7 (as-of date and recent merges; blocking): answered at lines 7 and 27.
- 8 (same-lines test; blocking): answered at line 27, which asks for file level, 14/30/60-day windows, a list of excluded files, and revert/naming reported apart from overlap.
- 9 (rounds undefined; blocking): answered at lines 18-23.
- 10 (dispatch-log and double counting; blocking): answered at line 20 (identity by piece, checker and date) and line 25 (dispatch-log named).
- 11 (units, closed-unmerged, direct pushes, size view): answered at line 9.
- 12 (question-file limits and matching): answered at line 16.
- 13 (reading limits; blocking): NOT answered. The path exclusions at line 33 are good, but the extract leaks, see 2 to 4 below.
- 14 (anchoring on the memos): answered at line 25.
- 15 (file names used only as counts): answered at line 16.
- 16 (form): answered, see item 11 below.
- 17 and 18 (plainness, "screening project"): mostly answered. "Owner" is used throughout and "supervisor" is gone. See item 12 below for what remains.
- 19 (overlap): answered. Line 18 says the item is a recount, and line 25 asks for a comparison.

**New findings**

*Blindness: the extract*

1. [Blocking] Subjects carry the owner's rulings and leanings. extract.py nulls a subject only when a changed path is under the barred records. Many subjects about those rulings sit on commits that touch other paths and survive. Examples from a keyword sample:
   - Model-Lab.jsonl line 229: "…by the owner's ruling on the harness landing".
   - Model-Lab.jsonl line 248: "…on the owner's ruling A".
   - Model-Lab.jsonl line 267: "…on the owner's ruling A".
   - Model-Lab.jsonl line 313: "…as the owner ruled".
   - Model-Lab.jsonl line 61: "…as the owner ruled".
   - Model-Lab.jsonl line 214: "the trade-offs ruled A and C".
   - Model-Lab.jsonl line 174: "the K1 record notes the owner's ruling: the transcript read is a stated limit".
   - Model-Lab.jsonl line 388: "the Build gate for P-001, proceed at size A, with the terms as recommended". This also shows a recommendation.
   - Model-Lab.jsonl line 469: "…under the owner's ruling B: …".
   - Service-Desk.jsonl line 349: "Record the owner's answers: the widget keeps its data on the phone only (P-004) (#290)". This is the content of an answer.
   - Service-Desk.jsonl line 385: "Record the owner's answer: the widget runs the desk's own code (P-004) (#284)".
   - Service-Desk.jsonl line 393: "the owner's answer to the widget question, verbatim (A)".
   - Service-Desk.jsonl line 359: "Raise the pipeline's total size limit to 128 MiB … (your ruling, B) (#287)".
   - Service-Desk.jsonl line 311: "the owner's answer to the data-route question, verbatim (the widget sends it to portfolio)".
   - Many subjects also name a project's aims or plans, for example Model-Lab.jsonl lines 42, 106 ("the screening's follow-up research questions") and 137.

   The question's own limit at line 33 ("the extract leaves out the subject of any commit that touches those records; other subjects may be read for classing") is therefore false in effect. A Researcher who reads for classing will see the owner's rulings and some project aims. Fix the extract: for example, null subjects that match ruling, answer, owner or P-0nn words, or drop all subjects except the "Merge pull request" form and a coarse kind. Or let the question state this as a disclosed limit and the Orchestrator accept it. I am not choosing for them.

2. [Blocking] File paths in each commit's `files` list are not screened. Paths such as questions/P-002-research-stop-3.md, decisions/questions/P-002-target.md, docs/projects/P-002.md and reviews/P-002-groundwork-shortlist/critic.md name the barred files and the project. Line 16 allows file names for counts and matching only ("do not report them"). The extract shows them to the Researcher anyway, and also shows project ids and topics, for example "target", "groundwork-shortlist" and "research-stop". Consider redacting these names in the extract to a type and a date, or state the limit.

3. [Non-blocking, needs one line] "Q-017" names two different things. Service-Desk has its own Q-017 files (status/Q-017.toml, queue/Q-017-stop-3.md, decisions/Q-017/ and subjects at Service-Desk.jsonl lines 451, 545 and 547). Line 33 bars "any other file about this question, Q-017". A Researcher will either be confused or will open Service-Desk's Q-017 files. Say that the Service-Desk Q-017 items are not this question, or say how to tell them apart. Line 451 ("…shows the Chief of Staff's recommendation") is visible in the extract. It is about the other Q-017, but it reads as a recommendation signal. I did not see any leaked content about this question's own Critic rounds. The extract was made from origin/main and the round 1 file is not in it.

*Workability without git*

4. [Blocking] Squash merges are not covered. Service-Desk.jsonl has 241 subjects ending "(#n)", which are squash-style merges. It has only 73 "Merge pull request" commits, and 464 null subjects, so the PR number is hidden whenever the commit touched a barred path. Line 13 says GitHub records a merge "as a commit titled 'Merge pull request #n', committed by GitHub and authored by the merging account". That is not true of squash merges, which are authored by the PR author. No rule says how to count them as merged pull requests, how to see who merged them, or how to count a null-subject commit. The "owner" and "agent" counts for merges depend on this, so the counts cannot be repeated from the extract. Line 9 says "no pull request … as far as the extract shows", which does not help here. Add a rule for squash merges and for null-subject commits, and a rule for a PR whose number cannot be read.

5. [Blocking] Classing "from its title" (line 9) cannot be done. A merge commit's subject is only "Merge pull request #n from <account>/<branch>", and the PR title is in the body, which the extract leaves out. Squash subjects give a title, but 464 Service-Desk subjects are nulled. Name what the Researcher classes from: branch name and paths. Say that a merge commit's `files` list is empty (git log --numstat with no merge option shows none for merges) and that a PR's files come from the union of its branch commits. Say how to tell the branch commits from the first-parent history (parents and ancestry). None of this is stated, and without git the Researcher must walk the parents list by hand. Item 5's "later pull request changes the same files" depends on the same rule.

6. [Non-blocking] The timestamp is the author date, and the question does not say which date to use for "per month" and the 14/30/60-day windows. For a PR it should be the merge commit's date, and a timezone (UTC) should be stated. A rebased or re-signed commit (the extract shows re-signing in subjects) keeps an old author date, so the choice matters.

7. [Non-blocking] Line 12 lists "other" as a class. The extract's `cls` classes by exact names or a noreply suffix. "Create owner.md" commits through the web interface may be owner or other. The 135 "other" commits (117 in Service-Desk) need a stated treatment, and the question's line 12 asks for one. Also, extract.py's third owner test depends on `sys.argv[1]`, an address that is not recorded in the README, so the owner's addresses cannot be re-checked. That is acceptable if the README says the extract was run with the owner's configured address. Add the sentence.

8. [Non-blocking] Item 4's records (verdict files under reviews/, source-check and entries-check files, and Service-Desk's dispatch-log/) are in the current files, so that count is workable without git. Dates for those rounds must come from the files or from the extract by file path. Say which. A verdict file's date is in its text, but the question does not say whether the commit date is a fallback.

*Other checks*

9. Neutrality: I found no wording that presumes an answer, favours a high or low share, or signals what the owner wants. "Report every figure on equal terms" is kept. The "stop rule" is defined by its content in line 22. Item 2's "agent" and "owner" labels are neutral.

10. Gaps: the set of counts is now good. Items 1-6 cover what an expert would expect: who made, who merged, who was asked, rounds, rework, limits. One small addition: item 2 does not say to give the commit-to-PR assignment rule, which is the same hole as finding 5. Item 6 should name the squash and null-subject limit once it is added.

11. Form: matches research/_QUESTION.md (header, The question, The decision it serves, What each answer would change, topics, depth). Non-blocking: the question text is long and holds the definitions inside six numbered items. It is workable.

12. Plainness: remaining terms with no gloss are "built work", "records only", "gate case", "stop rule" (defined), "dispatch-log", "source check" and "entries-check". A Researcher meeting "owner question" and "critic" must infer them. Non-blocking: add a one-line gloss of each kind of piece and what a "checker" is.

13. Overlap with Q-006-memo and Q-008-memo: item 4 is stated as a recount, with the changed unit and the comparison made after the counts. Items 1-3 and 5 are new. This is not a re-run under D-047. Pass.

**Blocking findings:** 1, 2, 4, 5. The rest are non-blocking. The question text itself is close to ready; the extract and the PR-counting rules are what fail the blindness and repeatability checks.

## Round 3 (brief 218)

The round's verdict was FAIL.

Round 3 check of /home/user/Model-Lab/research/Q-017.md and its rebuilt extract. I read no commit subjects (the extract has none). I did not open docs/projects/, docs/PROJECT.md, the contents of decisions/ or questions/, or any ideas/ folder. I searched the extract's paths and listed some Model-Lab files, and I read one line each of intake/requests/Q-017.toml and the handoff files' grep counts. Line numbers refer to Q-017.md.

**Round 2 findings: answered or not**
- R2-1 (subjects carry rulings and aims; blocking): answered. The extract has no subject, message, title or branch field at all. README line 5 says so, and a search for those keys found nothing.
- R2-2 (barred and project paths in `files`; blocking): mostly answered. questions/, decisions/, docs/projects/ and sessions/chief-of-staff/ paths and P-nnn segments are now opaque labels (README line 24, extract.py lines 13-20). Leftovers are in finding 3 below, non-blocking.
- R2-3 (two Q-017s): answered at line 33, which says Service-Desk's Q-017 items are unrelated and may be read.
- R2-4 (squash merges; blocking): answered. Line 13 separates squash from merge and says what a squash can and cannot show. The `how` field and README lines 17-19 give the rule. The null-subject problem no longer exists.
- R2-5 (classing, and the PR-to-commit rule; blocking): answered. Line 9 classes from paths. prs.jsonl gives the PR's own commits and the union of their files (README lines 19 and 21), so no parent-walking is needed.
- R2-6 (which date): answered. Line 9 says merged_at, UTC, and README line 18 says merged_at is the merge or squash commit's date. Minor gap in finding 5.
- R2-7 (the "other" class and the owner address): answered. Line 12 asks for a treatment of "other", and README line 3 says the owner's configured address was used for classing and not written.
- R2-8 (round dates): answered. Line 25 says to use the verdict file's text, then the file's commit date in commits.jsonl.
- R2-12 (a gloss for each piece kind): partly answered, see finding 6.
- Round 1 finding 13 (reading limits), which round 2 found unanswered: still NOT answered, see finding 1.

**Findings**

1. [Blocking] Lines 33 and 37-43 against the files the Researcher may read. Line 33 allows "the three repositories' current files" and bars only: questions/, decisions/, docs/projects/, docs/PROJECT.md, ideas/, sessions/chief-of-staff/, *-notes.md, reviews/P-002-research-q017/, and research/Q-017*.md in Model-Lab. Other files still carry the hoped-for answer, the Chief of Staff's recommendation or the owner's leanings. The extract also lists several of them in its `files`, so the Researcher is pointed at them.
   - /home/user/Model-Lab/intake/requests/Q-017.toml says "P-002 (the screening) ... the starting figures for its value target ... pre-mortem R12". This is the exact signal round 1 finding 1 barred, and it contains the project name and the target. It is readable under line 33.
   - /home/user/Model-Lab/docs/briefs/216-critic.md, 217-critic.md and 218-critic.md name Q-017 and are the briefs of its own check rounds. The extract lists docs/briefs/ paths.
   - /home/user/Model-Lab/docs/handoff/2026-11-09-chief-of-staff-p002-3.md names Q-017 and P-002, and the other docs/handoff/*chief-of-staff* files (19 in Model-Lab, many `-p002-n` in the extract's Service-Desk list too) are Chief of Staff handoffs. Handoffs are the notes-like, recommendation-bearing files that the sessions/chief-of-staff and *-notes.md bars were meant to cover.
   - digest/project.md and digest/p-001.md, docs/LESSONS.md (round 1 said lessons logs record rulings), and docs/reports/ were not named in the bar.
   - The count work needs none of these. Item 4 needs reviews/, research/*-source-check.md and *-entries-check.md, and dispatch-log/. Item 5 already excludes logs and digests. Name the permitted records instead of the repositories' whole current files, or add these paths to the bar: intake/, docs/briefs/, docs/handoff/, digest/, docs/LESSONS.md and the other bar-adjacent paths. Alternatively the Orchestrator can strip them from the Researcher's copy of the repositories. Deleting a bar is not a fix, since the extract still lists the paths. I am not choosing for them.

2. [Non-blocking, depends on 1] Line 33 itself names reviews/P-002-research-q017/. That tells the Researcher a project P-002 exists and that this question has been checked. It does no harm beyond that, but the same bar could be worded by pattern (for example "reviews/ for items about this question") without the project id. The question's own header (line 3) also names reviews/P-002-research-q017/.

3. [Non-blocking] Path names that survive redaction still carry project ids and topics. extract.py line 20 redacts only a segment that starts with "P-" and three digits. These are not caught: docs/handoff/2026-11-08-chief-of-staff-p002-1.md and similar (lowercase "p002"), digest/p-004.md, docs/handoff/2026-11-04-chief-of-staff-widget.md, experiments/EXP-008-widget-refresh-documents.md, reviews/S-037/_owner-answer-q031.md, and reviews/S-037/_owner-instruction-2026-11-05.md. The file contents are not shown, so this is a topic and project-id leak rather than a ruling leak. Line 16's "use names only to count" covers only the labelled paths. Either widen the redaction (case-insensitive p-?\d{3}, "widget") or extend line 16's "do not report" to every file name.

4. [Non-blocking] Lines 41-43. "Each count becomes a figure that later work can be compared against" signals that a later comparison is planned. Round 2 passed it and it names no direction or target, so I do not make it blocking. A plainer "a described baseline of the organisation's own records" would do. Neutrality otherwise holds. "Report every figure on equal terms", both-ends counts, and "does not judge whether the earlier change was at fault" are all kept, and no number or wording favours a high or low share.

5. [Non-blocking] Line 27 and item 5. The windows are measured from the earlier PR's merged_at. The question does not say whether the later commit's author_date or commit_date decides whether it falls in the 14, 30 or 60 days, and the extract has both. Rebased commits make these differ. Name one.

6. [Non-blocking] Plainness (line 18 and onward). "Built work (code, tests, tools)", "checker", "piece" and "round" are defined. Still unglossed: "records only", "other" kind, "gate case" (partly), "dispatch-log", "source check", "entries-check", and "critic of a question put to the owner". A Researcher who knows nothing of the project must infer them from the file names. One line each would do. "Records only" has no stated path rule, so that class cannot be repeated by someone else.

7. [Non-blocking] Workability without git. Items 1-3 and 5 are workable from the extract: PRs and their own commits and files are given, the merge versus squash is a field, and the owner and agent classes are given. Item 4 is workable from the current files plus commits.jsonl for dates. Two things need a sentence: (a) commits with kind "plain" and pr null on the default branch that belong to no PR can only be told from branch commits through prs.jsonl `commits` lists, so say to use those lists as the assignment rule; (b) the extract has only commits reachable from origin/main, so closed-unmerged PRs and direct pushes appear only as plain commits, which line 9 already mostly says.

8. Gaps. The set of counts is complete for the stated purpose (who made, who merged, how often asked, rounds, rework, limits). Each count is defined enough to repeat, given findings 5 to 7. Item 6 lists the right limits, including squash merges and identities that are not proof of authorship.

9. Form. It matches research/_QUESTION.md: header, The question, The decision it serves, What each answer would change, and the topics and depth lines. It is long, with definitions inside six items, but it is workable.

10. Overlap with research/Q-006-memo.md and Q-008-memo.md. Item 4 is stated as a recount with a changed unit (pieces tied to merged PRs), extended to 2026-11-09, and the comparison to the two memos is made after the Researcher's own counts. Items 1-3 and 5 are new. This is not a re-run under D-047.

**Blocking: finding 1 only.** Everything else is non-blocking. If the Orchestrator restricts the Researcher's readable files (the intake request, the check-round briefs, the Chief of Staff handoffs, the digests and the lessons log), the question and extract would pass. This round 3 is the last before the stop rule; the fix is a bar and permitted-record list, not another rewrite of the counts.

## Deciding check (brief 221, decisions/questions/P-002-q017-stop.md)

The round's verdict was FAIL.

The question is now blind and neutral enough, and round 3's blocking finding is answered. The rounds coding fails: it would give wrong counts for first-try passes, rounds per piece and the stop rule. This goes back to the owner under /home/user/Model-Lab/decisions/questions/P-002-q017-stop.md. I did not rewrite the question or the extract.

**Round 3's findings: answered or not**
- Round 3, finding 1 (blocking: the readable files carried the intake request, handoffs, digests and lessons): ANSWERED. /home/user/Model-Lab/research/Q-017.md line 41 limits the Researcher to the extract folder and the question, and bars git, GitHub and the web. I found no ruling, recommendation, aim or project name in the question or in README.md. The extract holds no subject, message, title or branch. The only project items still visible are labelled `<…:id>` or `item-<id>`.
- Finding 2 (the bar naming the P-002 review folder): ANSWERED. Neither the question nor its header names a P-002 review folder any more.
- Finding 3 (project ids and topics left in path names): MOSTLY ANSWERED. extract.py line 21 now redacts `p-?\d{3}` and "widget", case-insensitively. Some names remain, for example `owner-request-…`, `owner-answers-…`, `reviews/S-037/_owner-answer-q031.md` and `_owner-instruction-…`. They show that an owner request or answer exists, not what it says. Line 41's "do not report any path" covers them. Non-blocking.
- Finding 4 (the "later work can be compared against" wording): ANSWERED. Lines 45-47 now say "a described baseline".
- Finding 5 (which date decides the windows): ANSWERED. Line 35 says the later commit's commit_date or the later pull request's merged_at, and line 9 says merged_at in UTC.
- Finding 6 (glosses): PARTLY ANSWERED. "Checker", "piece", "round", "stop rule" and "source checker" are glossed. "Records only", "other" and "dispatch log" have no path rule and no gloss.
- Finding 7 (assignment rule and closed pull requests): ANSWERED. Line 17 uses the pull request's own `commits` list as the rule, and lines 17 and 37 name direct pushes and closed-unmerged pull requests.

**Blocking findings: the rounds coding (rounds.py and the three .rounds.jsonl files)**

1. Briefs and READMEs are coded as passing verdicts.
   - rounds.py reads every `.md` under reviews/. A reviewer's brief holds a template line, "Verdict : PASS | FAIL with evidence per item", and the coder takes it as `pass`.
   - In the Personal-Org-Operating-Model rounds file, 9 rows are brief files, for example reviews/2/_reviewer-brief1-verbatim.md, reviews/3/_reviewer-brief-s004.md, reviews/4/_reviewer-brief.md and _reviewer-brief-round2.md, and reviews/5/ and reviews/7/ equivalents.
   - I read reviews/3/_reviewer-brief-s004.md in the repository; its only verdict line (line 27) is that template.
   - `reviews/README.md` is also coded as a `pass` in Service-Desk (line 544) and Model-Lab (line 187), with checker "unknown".
   - These are invented rounds, and all are passes.

2. Ordinary headings are coded as rounds.
   - The splitter matches any heading that starts `## Round n`, so "## Round 1's B1, confirmed fixed" or "## Round 2 findings" becomes a round.
   - Service-Desk reviews/227/reviewer.md has two real rounds. The extract gives three rows, the third "round 1, pass-from-file". I checked the headings at lines 135 and 176.
   - Model-Lab reviews/S-001/plan.md: its "## Round 1 findings, one by one" and "## Round 2 findings" headings are coded as rounds 1 and 2, both `pass`. Its second series, headed "New draft, round 1" to "5", is not coded at all.
   - The same file also has four duplicate rows for item-73125bf7, round 2 (rows 119-121).
   - Duplicate round numbers with opposite verdicts break "first round" and "three in a row", and they distort `pass-from-file`.

3. One check is split into several pieces, and one verdict is counted several times.
   - The piece name keeps `_reviewer-verbatim.md` apart from `reviewer.md`.
   - Personal-Org reviews/32: the round-1 FAIL file is one piece, and `reviewer.md` (the final PASS) is another. The extract therefore shows a piece that failed with no pass, and a piece that passed first time.
   - The same split happens in reviews/40: r1 fail and r2 fail are one piece, and the pass in `reviewer.md` is another. A three-fail stop-rule count cannot be made from that.
   - In reviews/4, the final PASS appears three times: round2-verbatim, `reviewer.md` and brief-round2. Their pieces differ, so the question's "matched by piece, checker and date" rule (line 28) cannot merge them.

4. Dates on single-file verdicts give false first-try passes.
   - For a file with no round sections, the date is the date the file was first added, but the verdict is the file's final content.
   - Service-Desk Q-006 source check: the file row is `pass` dated 2026-10-02T00:31:04Z, but the dispatch log shows `fail` at 00:31:21 and the pass only on 10-04 (lines 5 and 758-774).
   - Q-001 and Q-005 do the same: a file `pass` is dated seconds before the dispatch `fail`.
   - "First round in date order" therefore returns a pass for pieces that failed first. The "matched by the dispatch line's record" rule has no tie-break either, because several dispatch lines share one record.

5. Dispatch lines for roles that are not checkers are coded as rounds.
   - rounds.py keeps every dispatch line that has a `verdict` key, including researcher, definer, definer-freeze, check-author and critic-triage, all with verdict `none` and no checker's outcome.
   - Examples: Service-Desk rows 723-725, 748, 789-791 and 856.
   - Item 4 says "a round is one line of the extract", so these inflate the rounds-per-piece counts and the `none` count. The README calls them "verdict records".
   - The extract has no field that marks a row as an independent check.

6. Item 4 of the question does not define ties, `none` first rounds or "kind".
   - Many multi-round files carry identical dates. Examples: reviews/226 to 231 in Service-Desk, and several Model-Lab critic files (item-80d822b3, item-4747edb7, item-b72ccf4f, item-91f1840b). "First round in date order" has no tie-break, and the question does not say to use the round number.
   - Many pieces open with round 1 `none`, with only the last round coded `pass-from-file`. For example, Model-Lab item-f204f458 and reviews/51 (rounds 1-3 `none`). The question does not say whether a piece whose first round is `none` counts as a first-try pass, a fail, or unknown.
   - Line 33 asks for figures "per kind", but the rounds extract has no kind field and the question does not say how to derive one.
   - A `none` record is not necessarily a pass or a fail, so rates computed without a stated rule cannot be repeated.

**Non-blocking findings**

7. Coding that is too coarse.
   - `owner.md` rows (the owner's approval at merge) are coded as a checker "owner", so they enter piece and first-try counts as if they were independent checks.
   - `plan.md` falls to checker "unknown", though README line 31 says plan-review files are the reviewer.
   - Gate files (`_design-gate-n-critic.md`, `_build-gate-n-critic.md`) have no Verdict line and are coded `none`. They are gate opinions, not pieces.
   - "Unknown", "owner" and similar checkers cover about 281 rows over the three files, counted together.
   - Dispatch rows have `round: null` and a piece id such as "P-003", which does not match a verdict file's path, so linking pieces to pull requests through files works for the verdict files only.
   - The dispatch log has some verdict lines tied to the reviews/S-00x/plan.md record; the verdict-file side of the same check cannot be matched by piece or date.

8. Single-file verdicts overwritten between commits lose their earlier rounds, which is a limit to state under item 6.

9. Questions and answers.
   - The commits file records added and removed line counts only, not whether a file was added or deleted. "First added" can only mean the earliest commit listing that label, and removal of a question cannot be told from an edit.
   - A rename changes the label, because the label is a hash of the path. A question moved to decisions/ would look like a new decision file.
   - The question permits saying "cannot be matched", but item 6 should name these two limits.

10. Gloss and path rules (carried from round 3, point 6). "Records only" and "other" have no path rule, so the Researcher invents one. That is acceptable only if the question says so, which line 9 does ("with a stated rule"). "Dispatch log" and "entries-check" are unglossed in the question; the README covers them.

11. Form and overlap. The form matches research/_QUESTION.md. Item 4 is stated as a recount that keeps the comparison to the earlier memos until after the Researcher's own counts. This is not a re-run (D-047). The neutrality wording holds: "Report every figure on equal terms", both ends for every count, and "does not judge whether the earlier change was at fault".

**What would make it pass.** Fix the coding and re-run rounds.py, or have the question tell the Researcher how to handle each case:
- drop the brief and README files;
- split sections only on "## Round n" headings that are followed by a verdict, or only at the start of a round;
- group the series files and `reviewer.md` into one piece per PR and checker;
- date single-file verdicts by the last commit that changed the Verdict line, or mark them as overwritten;
- mark non-checker dispatch lines;
- state the tie-break, and how a first round of `none` is counted.

A fresh Critic check should follow.

Files read: /home/user/Model-Lab/research/Q-017.md, /home/user/Model-Lab/research/Q-017-extract/ (README.md, extract.py, rounds.py, the three .rounds.jsonl files, and keyword searches of the commits and prs files), /home/user/Model-Lab/reviews/P-002-research-q017/critic.md, /home/user/Model-Lab/decisions/questions/P-002-q017-stop.md, and verdict files in the three repositories (Service-Desk reviews/227, Personal-Org-Operating-Model reviews/3, 4, 32 and 40, Model-Lab reviews/S-001/plan.md). I read them from the working tree, not origin/main, so they may differ from the default branch.

## Deciding check of the narrowed question (brief 224, decisions/questions/P-002-q017-decide.md)

The round's verdict was FAIL.

Q-017 narrowed question and extracts, deciding check. The question and extract are blind and neutral, and no rounds material remains. The extract's squash coding is wrong in Service-Desk, and the hand check did not catch it. This goes back to the owner per the ruling. I did not rewrite the question or the extract.

Limit on my own test: my tools in this session had no shell and no git, so I could not run git show or git log against the three repositories. My test of accuracy is therefore a test of the extract against itself (counts, duplicates, field consistency, extract.py's logic) and not against origin/main. Finding 1 is evidence from the extract alone. It does not need the repositories to stand.

1. [Blocking] Six "squash" pull requests in Service-Desk are not squash merges, and their numbers are counted twice.
   - Evidence, /home/user/Model-Lab/research/Q-017-extract/Service-Desk.prs.jsonl:
     - Lines 144, 146, 148, 150, 152 and 154 are `how: squash` for PR 182, 181, 180, 178, 177 and 176.
     - Each has merge_commit_author "orchestrator" (agent). Each holds one commit whose only files are reviews/<n>/reviewer.md and, for most, design-reviewer.md. Those are review records of the PR with the same number.
     - The same six numbers also appear as ordinary `how: merge` lines at 143, 145, 147, 149, 151 and 153.
     - Service-Desk.commits.jsonl lines 1479, 1495, 1537 and 1539 show PR 182 and 177 as the pr of two commits each.
   - Cause, extract.py lines 49 and 51: any single-parent commit whose subject ends "(#n)" is classed "squash-pr". These are orchestrator commits that record reviews and end by naming the PR they review. They are not merges of a pull request.
   - Effect on the counts:
     - Service-Desk shows 327 merged pull requests, of which 6 are phantoms. Per-month counts, the "squash" count, and the agent merging-account share are all wrong.
     - A squash is supposed to take its author from the pull request's author. These six give an agent account, which contradicts the question's line on squashes.
     - The later-change test also counts PR numbers twice.
   - README lines 9 and 17 say "squash-pr" is a single-parent commit with a "(#n)" subject. That matches the code, so a Researcher following the README cannot tell these from real squashes. The question (item 2) tells the Researcher to count squashes separately and say what they show, so the six would be reported as real.
   - The hand check missed it. Its sample did draw squash PRs 176 and 177, and it marked each "True" on the subject's PR number. It never asked whether that number belongs to a distinct merged pull request, and it never checked for duplicate numbers. Both 176 and 177 are in the phantom list.
   - Fix needed: re-code or drop these six in the extract, or say in the README and question how to treat a number that appears as both a merge and a "squash". The hand check should then be redone on that point.

2. [Blocking, same root as 1] The hand check is not sound or sufficient as written.
   - It compares each field to git, but it never tests the kind coding itself. The cases that matter are:
     - a single-parent commit whose subject merely ends "(#n)";
     - a merge by an agent identity that is a local merge and not a GitHub merge. Service-Desk has 8 `how: merge` pull requests with agent merge authors, for example "definer", and line 2446 of the commits file is a "merge-pr" authored and committed by "Claude". The sample did not cover them.
   - It also says its coverage gap is "commits by the other class other than merge commits". My search shows no "other"-class commit in the extract is plain or squash. All 135 "other" commits are merges: "Claude" local merges, and github-actions[bot] merges committed by GitHub in Service-Desk only. So that stated gap is empty, and it should say so. The hand check's "other" sample (Service-Desk 146 and 137, merge) did cover the class as it exists.
   - Added, modified and deleted status: extract.py's name-status mapping is sound in code (A, M, D; "other" for anything else). The extract has no "other" status anywhere. The hand check covered 3 plain commits per repository, 15 in all, which is thin for a status field. The check I could do is consistency: every file in commits.jsonl has a status from {added, modified, deleted}.

3. [Non-blocking] README lines 9 and 17 describe "merge-pr" as a merge commit "that GitHub made". The code also gives that kind to a local merge whose subject names a pull request. The question's line that "for a merge, the merge commit's author is the account that merged it" is then inexact for agent-authored merge-pr lines. The Researcher is told to state limits, and the README should say it.

4. [Non-blocking] Item 4 and `mentions_prs` come from subjects only. Any "#n" in a subject is read as a pull request number, which may be an issue or a pull request of another repository, since all three repositories share one numbering style. The extract holds no revert at all (`revert: true` appears nowhere), and 213 commits have `mentions_prs` set. The question's separate reporting of reverts and naming covers this, but "cannot tell a PR from an issue or another repository's PR" belongs in item 5's limits.

5. [Non-blocking] Item 3, "first added … per month and per merged pull request".
   - prs.jsonl files carry no status field, only path and line counts. Status exists only in commits.jsonl. The count is repeatable through each PR's `commits` list. The question should say that, and which date gives the month (commit_date of the adding commit, or the PR's merged_at).
   - A file added, deleted and re-added counts twice unless "first" is defined by earliest date. Matching a question to its answer by "adds the decision label and deletes the question label" is workable. Renames show as delete plus add under a new label, as the README says.

6. [Non-blocking] "The decision it serves" still says "how its checked work fares". The narrowed question has no count for that, so this line is a leftover from the rounds item. Remove or reword it.

7. [Non-blocking] The 466 "other-merge" commits (73 in Personal-Org-Operating-Model, 38 in Model-Lab, 355 in Service-Desk) are local merges of agent branches. Item 1's "commits on the default branch that belong to no merged pull request" will include the merge commits themselves. Add one line on whether to count the merge commits or only their content.

Checks that passed:
- Blindness and neutrality (check 1). The question is neutral. It names no project, target, direction or ruling, and it keeps "report every figure on equal terms", both ends for each count, and "does not judge whether the earlier change was at fault". No rounds file, rounds script or rounds wording remains. A glob of /home/user/Model-Lab/research/Q-017-extract/ shows only README.md, extract.py and the six jsonl files. A search for "round" in README.md and extract.py finds nothing. Matches in the jsonl files are file-path segments, which the "do not report any path" rule covers. The extract has no subject, message, title, branch or address field. Two stray words in the paths, "owner-answers" and "owner-request", are carried over from my earlier non-blocking note.
- Internal consistency. The commit files total 4,664 lines (958 Model-Lab, 948 Personal-Org-Operating-Model, 2,758 Service-Desk). Each repository's count of merge-pr and squash-pr commits equals the number of lines in its prs file (84, 47 and 327, 458 in all). Every file path has a status from {added, modified, deleted}.
- Question 3, repeatability. Items 1, 2 and 4 can be counted from the extract alone and repeated, once finding 1 is fixed. Item 2's "other" treatment is workable, since other consists of the "Claude" local merges (a default identity) and github-actions[bot] merges. Item 4's windows are defined by commit_date and merged_at in UTC, and its file overlap runs through prs.jsonl `files`, with the unreviewed exclusion of "logs, ledgers, digests, session records" workable from labels and path names.

Files read: /home/user/Model-Lab/research/Q-017.md, /home/user/Model-Lab/research/Q-017-extract/ (README.md, extract.py, and searches of all six jsonl files), /home/user/Model-Lab/research/Q-017-extract-sample.md, /home/user/Model-Lab/reviews/P-002-research-q017/critic.md, /home/user/Model-Lab/decisions/questions/P-002-q017-decide.md.

## Deciding check of the fixed extract (brief 228, decisions/questions/P-002-q017-next.md)

The round's verdict was PASS.

Limit on my test: I had no shell and no git, only Read, Grep and Glob. I could not run extract.py or check the extract against the three repositories. My tests are of the extract against itself, plus a read of extract.py's logic. I did not re-run the Orchestrator's hand check in Q-017-extract-sample.md. I took its recorded figures as the Orchestrator's, and they agree with what I counted.

1. The earlier blocking finding is fixed (blocking check: passed).
- Pull request lines per file: Service-Desk 312, Model-Lab 85, Personal-Org-Operating-Model 50. These match the commits files' merge-pr counts (312, 85, 50) and the hand check's figures.
- The six former phantoms (pull requests 176, 177, 178, 180, 181, 182) now appear once each in Service-Desk.prs.jsonl (lines 143 to 148). In commits.jsonl each has one "pr" value (lines 1479, 1504, 1517, 1531, 1537, 1541).
- No "how" or "squash" field remains anywhere in the extract or in extract.py.
- No single-parent commit is coded merge-pr or other-merge, and no two-parent commit is coded plain.
- All 447 merge-pr commits have GitHub as committer. No other-merge commit has GitHub as committer.
- No plain commit carries a pr number.
- Commit file lines are 2758, 971 and 948. These equal the hand check's "extract equals default branch" figures, which I could not recheck against git.
- No "other" file status appears, and 3,757 commit lines carry a status of added, modified or deleted.

2. Coding rules and tests (non-blocking, with two gaps).
- extract.py is sound. A pull request merge is a commit with two parents, committed by GitHub, whose subject starts "Merge pull request #n" or ends "(#n)". Every other merge is other-merge, and the pull request's own commits come from parent 1 to parent 2. This matches the README and the ruling.
- The hand check's invariants test the changed rule directly. They cover one line per pull request number, no single-parent merge, no commit in two pull requests' lists, and every GitHub merge being a pull request line. The 15-item field sample against git is reasonable, and its "other" class is now only merges.
- Gap A: no test covers a single-parent commit committed by GitHub whose subject names a pull request, which is what a real squash merge looks like. Such a commit would silently become plain and fall in "no merged pull request". I checked the extract: 147 plain commits are committed by GitHub (120 in Service-Desk), and none has a mentions_prs value. So no squash merge is hidden today. The test should be added, and the README should say that such commits are plain.
- Gap B: the revert rule ("Revert" prefix) has no test, and the extract holds zero reverts. The question reports reverts separately, so this is only a stated-limit matter. A revert whose subject does not start "Revert" is not found.
- The test "every GitHub merge is a pull request line" is partly circular, because it uses the same rule. It is still useful as a check on the count.

3. Blindness, neutrality and repeatability.
- Blind: no subject, title, message, branch or email field exists in the extract. Paths are labelled. The question gives no project name, target, direction or ruling.
- Neutral: "Report every figure on equal terms", both ends for each count, and "does not judge whether the earlier change was at fault" are all kept.
- Items 1, 2 and 4 can be counted from the extract alone and repeated.
- My last check's non-blocking points that bear on the counts are still not answered in the question or README. Please state them as limits or add a sentence each:
  a. Item 4 and mentions_prs: a "#n" in a subject may be an issue or another repository's pull request. 223 commits have mentions_prs set.
  b. Item 3: prs.jsonl has no file status, so "first added" must go through each pull request's commits list. The question does not say which date gives the month, or how to treat a file that is added, deleted and added again.
  c. Item 1: the 472 other-merge commits (364 in Service-Desk, 70 in Personal-Org-Operating-Model, 38 in Model-Lab) will fall in "commits that belong to no merged pull request". The question does not say whether to count the merge commits or only their content.
  d. README: "merge-pr" is now accurate, but it should say the author of a merge-pr commit is the merging account only for GitHub's own merges.
  e. "The decision it serves" (line 38) still says "how its checked work fares". The narrowed question has no such count, so reword or remove it.

None of these blocks the count. Each makes a Researcher's figures harder to repeat unless it is stated as a limit.

Files read: /home/user/Model-Lab/research/Q-017.md, /home/user/Model-Lab/research/Q-017-extract/README.md, /home/user/Model-Lab/research/Q-017-extract/extract.py, searches of the six .jsonl files in that folder, /home/user/Model-Lab/research/Q-017-extract-sample.md, /home/user/Model-Lab/reviews/P-002-research-q017/critic.md, /home/user/Model-Lab/decisions/questions/P-002-q017-next.md.
