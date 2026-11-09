Verdict: FAIL

*The Critic's neutrality check (D-055) of research question Q-017 for P-002: round 1 (FAIL); brief 216. Each round a fresh session on a different model from the question's writer, started by the Chief of Staff (session_01QBwHGNSLmSrYQgS6BPjV8p), 2026-11-09. Recorded verbatim by the Orchestrator from each helper's return; each round's own verdict line is recorded as "The round's verdict was …" (LL-68). The verdict above is the latest round's.*

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
