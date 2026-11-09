Verdict: FAIL

*The Critic's neutrality check (D-055) of research question Q-017 for P-002: round 1 (FAIL), round 2 (FAIL); briefs 216 and 217. Each round a fresh session on a different model from the question's writer, started by the Chief of Staff (session_01QBwHGNSLmSrYQgS6BPjV8p), 2026-11-09. Recorded verbatim by the Orchestrator from each helper's return; each round's own verdict line is recorded as "The round's verdict was …" (LL-68). The verdict above is the latest round's.*

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
