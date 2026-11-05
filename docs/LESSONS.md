# Lessons log — Model-Lab

*Every slip, error and miss in this work, recorded the session it is found (decisions/questions/P-001-lessons-log.md). Each entry is corrected within the workflow at the end of the cycle: it becomes a change in the result integrated into the operating model, or it is closed with a reason. Entries are added and their status updated; none is deleted.*

Fields: **what happened** · **caught by** · **cause** · **correction proposed** · **status**. "Who" names a role, not a person; the Chief of Staff's own slips are listed like any other.

Status: `open` (correction not yet made) · `fixed here` (fixed in this project; the model change is still to come) · `closed` (with reason).

## 2026-11-01 — Discovery of P-001, session_01QBwHGJH9m3A4Ray7WpHzBo

### LL-01 Questions put to the owner before they could be filed
- **What happened:** the work-repository questions were asked in the session before any project existed, so they could not be filed first as the model requires (S-033).
- **Caught by:** the Chief of Staff, at the time; recorded in decisions/questions/P-001-work-repo.md.
- **Cause:** the model has no place to file an ask that comes before a project exists.
- **Correction proposed:** a filing place for pre-project asks (for example the portfolio repository's decision queue), named in the model.
- **Status:** open.

### LL-02 The first research question leaned towards the hoped-for answer
- **What happened:** Q-001 assumed the outcome would be a system for measuring and improving prompts, and missed cost, owner time, versioning, task types and over-fitting. Later, a Critic on a different model found it still leaned towards "instructions are the thing to change" and was sceptical of written procedure.
- **Caught by:** the Critic, twice (reviews/Q-001/critic.md; reviews/Q-001-diverse/critic.md).
- **Cause:** the writer knew the owner's intention; neutral phrasing was left to the check rather than drafted in.
- **Correction proposed:** a neutral-drafting checklist for research questions (benefits and risks both asked; "whether" before "how"; a "not the limiting factor" branch; an out-of-scope line).
- **Status:** fixed here (L-0003); model change open.

### LL-03 Checkers ran on the same model as the work they checked
- **What happened:** every helper the Chief of Staff started ran on its own model, including the Critic on its writing and the Source checker on the Researcher. Re-run on a different model, one check that had passed then failed.
- **Caught by:** the Chief of Staff, when saving the briefs and models (docs/LEDGER.md L-0002).
- **Cause:** a conversation-started helper inherits the session's model unless told otherwise; nothing in the Chief of Staff's dispatches enforced the model-diversity rule, which the scripted runner does enforce.
- **Correction proposed:** the conversational path names each helper's model and checks the pair, as the runner does; recorded with each brief.
- **Status:** fixed here (checkers now started on another model); model change open.

### LL-04 Helpers not logged in the session record when started
- **What happened:** the model requires a session line for each helper started; the first helpers were logged only after the fact.
- **Caught by:** the Chief of Staff.
- **Cause:** the logging is manual and easy to defer.
- **Correction proposed:** log the helper at dispatch, together with its brief and model (the brief-recording ruling, decisions/questions/P-001-session-records.md).
- **Status:** fixed here; model change open.

### LL-05 Owner questions misattributed and unfairly put
- **What happened:** the first seven drafted owner questions quoted the Chief of Staff's own words as the owner's, recommended (and defaulted) an answer about the owner's own frustrations, re-asked something already answered, and leaned towards the recommendation. Three rounds to pass.
- **Caught by:** the Critic (reviews/P-001-shortlist/critic.md).
- **Cause:** drafting from memory of the conversation rather than from the recorded words; a recommendation written for every question by habit.
- **Correction proposed:** every quote in a question cites the record it comes from; questions about the owner's own experience carry no recommendation or default; check the intent before asking.
- **Status:** fixed here; model change open.

### LL-06 A review record misnamed, and pushed with a failing check
- **What happened:** reviews/Q-001/critic-diverse.md broke the review-file naming rule; it was committed and pushed while the governance check was red, then moved (L-0004).
- **Caught by:** the governance check, read after the push.
- **Cause:** the push ran in the same command as the check, without stopping on its failure.
- **Correction proposed:** never push in the same step as a check unless the push is conditional on it passing.
- **Status:** fixed here (practice changed); closed for the model unless it recurs.

### LL-07 Researchers briefed to read the web directly
- **What happened:** the rulebook says untrusted text is read only by the Input reader, but the researcher's own agent file grants web tools, and every research brief let the Researcher read the web.
- **Caught by:** the Researcher on Q-007 (research/Q-007-memo.md, S-b2); logged as L-0005.
- **Cause:** the model contradicts itself (rule against tool grant); the brief followed the tool grant.
- **Correction proposed:** the owner rules which governs; the model then makes the rule and the agent file agree.
- **Status:** open; to the owner with the Design gate.

### LL-08 A route presented as the model's rule when it was an exception
- **What happened:** the desk-tests question first called the fast route "the route the model allows"; under the model's re-entry rule it is an exception.
- **Caught by:** the Critic (reviews/P-001-add-project-tests/critic.md in Service-Desk).
- **Cause:** the writer favoured the recommendation and read the rules to fit it.
- **Correction proposed:** a question that recommends going outside a rule says so in its first line, quoting the rule.
- **Status:** fixed here; model change open.

### LL-09 An option named the wrong agent for the work
- **What happened:** the desk-tests option said "the agent that writes tests" (the check author) would fix them, but those tests are in the Builder's lane; a check-author commit would have been refused. Corrected after the owner had ruled, and told to the owner.
- **Caught by:** the Chief of Staff, reading the surface map after the ruling.
- **Cause:** the surface map was not checked before the options were written.
- **Correction proposed:** before an option names who does the work, check the surface map.
- **Status:** fixed here; model change open.

### LL-10 A Builder's return missed for about 45 minutes
- **What happened:** the desk Builder had finished and returned; the Chief of Staff did not notice until it checked the agent's transcript.
- **Caught by:** the Chief of Staff.
- **Cause:** many helpers running at once; one return arrived without a visible notice.
- **Correction proposed:** a running list of dispatched helpers and their state, checked before each status message.
- **Status:** open.

### LL-11 The owner told twice that merged pull requests were still waiting
- **What happened:** pull requests #1 and #2 were merged at about 12:03 (owner's time), but the Chief of Staff kept listing them as waiting.
- **Caught by:** the owner ("so i understand you didnt create the first pull request?").
- **Cause:** pull-request state was not checked before reporting; GitHub's list shows them as closed.
- **Correction proposed:** check the live state of every pull request before telling the owner it waits on them.
- **Status:** fixed here (practice changed); model change open.

### LL-12 Research dispatched before checking the network could reach its sources
- **What happened:** six researchers ran while most academic, medical and government sites were blocked; two memos then failed their source checks, and most findings stay unconfirmed.
- **Caught by:** the Researchers and Source checkers.
- **Cause:** source access was not tested before dispatch, and the owner was told late.
- **Correction proposed:** before dispatching research, test the expected source hosts and put any network change to the owner first.
- **Status:** open (waiting on the owner's network change).

### LL-13 Merge commits made under a wrong identity
- **What happened:** two branch-update merges were committed under a placeholder email; fixed before they were pushed.
- **Caught by:** the Chief of Staff.
- **Cause:** a one-line command built the identity carelessly.
- **Correction proposed:** none for the model; closed.
- **Status:** closed (fixed before push).

### LL-14 Errors in research memos caught by the checks
- **What happened:** the groundwork map cited rule numbers that are not in the file it described (J1); the quality memo contradicted itself on one failure kind; the records memo had counting errors and overstated one claim. A Source checker also wrongly called one plan "never passed", and withdrew it.
- **Caught by:** the Source checker, or the Researcher on the checker's error.
- **Cause:** large counts and long files read by hand; the checks worked as designed.
- **Correction proposed:** none beyond the checks; recorded as evidence for the project (how often first drafts carry errors).
- **Status:** closed (fixed by the process); kept as evidence.

### LL-15 The desk's "add a project in one line" promise did not hold
- **What happened:** adding Model-Lab broke 50 of the desk's tests, which pinned today's two projects.
- **Caught by:** the Builder.
- **Cause:** the tests were written against the live project list.
- **Correction proposed:** the tests use their own fixed list (L-0021 in Service-Desk).
- **Status:** fixed here, under review.

### LL-16 The model's tools assume one project per repository
- **What happened:** Model-Lab holds both ideas, but the tools read a single project document per repository, so the second idea cannot start here as things stand.
- **Caught by:** the Chief of Staff, at setup.
- **Cause:** the model never needed two projects in one repository before.
- **Correction proposed:** options to the owner before the second idea's Discovery starts. Options were brought in Service-Desk (questions/P-002-plan-place.md, PR #268), where the desk's new work hit the same limit; on 2026-11-03 the owner chose B, "B: own plan, tools first (Recommended)": the model's tools change so a repository holds one plan document per project item, under Personal-Org-Operating-Model's own rules (Service-Desk decisions/questions/P-002-plan-place.md). The same change serves the second idea here.
- **Status:** open (the tools change is not yet specified or built).

### LL-17 The pace outran the owner
- **What happened:** results and asks arrived faster than the owner could follow; the owner asked for a single status page.
- **Caught by:** the owner.
- **Cause:** every return was reported as it came, instead of at natural points.
- **Correction proposed:** report at natural points, with one standing status page that is kept current.
- **Status:** fixed here (status page); model change open.

### LL-18 The lessons log's own first commit mixed two owners' files
- **What happened:** the owner's instruction (the Chief of Staff's lane) and the log (the Orchestrator's lane) were committed together under one identity, and pushed, because an earlier `git add -A` had staged both. Split into two commits before any pull request; the branch was re-pushed.
- **Caught by:** the Chief of Staff, from git's "nothing to commit" on the second commit.
- **Cause:** staging everything before committing by lane.
- **Correction proposed:** stage by lane only; run the surface guard's diff check before every push, not only before merging a builder's branch.
- **Status:** fixed here; model change open.

### LL-19 Source checkers sent to a checkout on the wrong branch
- **What happened:** to write the lessons log, the Chief of Staff switched the shared Model-Lab checkout to a branch without the research memos, then dispatched three source checkers at that checkout. One returned unable to find the memos; the others were told mid-run.
- **Caught by:** the Source checker on Q-002 to Q-004.
- **Cause:** one working copy shared between the Chief of Staff's own edits and its helpers' reads.
- **Correction proposed:** helpers read from a fixed path or worktree for the branch they need; the Chief of Staff edits other branches in their own worktrees.
- **Status:** fixed here (separate worktree for the lessons branch); model change open.

### LL-20 A merge made under the default identity again (LL-13 recurred)
- **What happened:** updating Service-Desk's answer branch from main made a merge commit under the environment's default name; fixed before it was pushed.
- **Caught by:** the Chief of Staff, checking the commit's author before pushing.
- **Cause:** `git merge` without the identity flags; the same slip as LL-13.
- **Correction proposed:** LL-13 is reopened. Set the identity once per repository for the session's lane, and have the surface guard's diff check run before every push (LL-18).
- **Status:** open (recurred).

### LL-21 A new project would have shown on the desk as finished
- **What happened:** the Design reviewer found that once Model-Lab is readable, its Home tile would read "Next: no milestone left to reach", because its project document had no milestone lines yet, as is normal early in Discovery.
- **Caught by:** the Design reviewer, by rendering the desk with Model-Lab's real records.
- **Cause:** two at once. The desk reads "no milestone line" as "all reached" (Service-Desk src/public/lib/home.js:645), and the Chief of Staff added the project to the desk before drafting its milestones.
- **Correction proposed:** draft a project's milestones before it goes on the desk; and a desk fix so a project with no milestone lines shows "not recorded", put to the owner as its own change to the graduated desk.
- **Status:** open (milestones being drafted; the desk fix not yet put to the owner).

### LL-22 No check of the environment's network before research begins
- **What happened:** the owner asked for this entry, after LL-12: research ran for hours before anyone found that the cloud environment's network blocked most research sources, and the owner then had to change the environment's settings mid-project.
- **The owner's words, verbatim (2026-11-01):** "a lesson learned that needs to be added is a Claude code environment assessment to determine if sources for research need to be given access."
- **Caught by:** the owner.
- **Cause:** nothing in the model asks for the session's environment (its network access, tools and limits) to be checked against what the work will need before the work starts.
- **Correction proposed:** an environment assessment at the start of any project's Discovery, and before research is dispatched: list the kinds of sources the research will need, test that the environment can reach them, and put any needed change to the owner first, with the exact steps. The same step can cover the other things a session needs (tools, repositories, permissions).
- **Status:** open; to become a model change at the end of the cycle.

### LL-23 A waiting deploy reached the owner with no notice
- **What happened:** after the owner merged #263 in Service-Desk, the preview deploy started and waited for approval, but the owner saw no request and said "Merged but no deployment request". The Chief of Staff found the waiting run and sent its link.
- **Caught by:** the owner.
- **Cause:** GitHub's own notice of a waiting deployment did not reach the owner, and the desk's operating notes ("Approving a deploy") assume it does; the Chief of Staff also did not send the run's link when asking for the merge.
- **Correction proposed:** whenever the Chief of Staff asks for a merge that starts a deploy, it finds the waiting run and gives the owner its link in the same message; and the desk's operating notes say where to find a waiting run when no notice comes.
- **Status:** fixed here (practice changed); a correction to the desk's notes is open.

### LL-24 Helper session lines lapsed again (LL-04 recurred)
- **What happened:** after LL-04 was fixed for the first three helpers, the next 26 helpers were again not logged at dispatch; they were backfilled from their transcripts, with start and end times only and every usage figure null.
- **Caught by:** the Chief of Staff, at a natural stopping point.
- **Cause:** logging stays manual and is skipped when many helpers run at once; the reported token figures were not copied as they arrived.
- **Correction proposed:** LL-04 is reopened. The session line and the brief are written in the same step as the dispatch (the brief-recording ruling); and the line takes the figures the helper reports when it returns.
- **Status:** open (recurred).

## 2026-11-01 — Discovery of P-001, session_01QBwHGHrHnEvMNYgKDoaH8w

### LL-25 The desk does not tell the owner when work must move to a new session
- **What happened:** the owner asked for this entry. A long piece of work has to stop at a natural point and carry on in a fresh session (the model's "stopping point before compaction"); the previous session did so with a handoff file, and the owner had to start the new session from it by hand. Nothing on the desk told the owner that the move was due, or where the handoff was.
- **The owner's words, verbatim (2026-11-01):** "One thing for the lessons learned - I would like the desk to notify me when the conversation needs to move from one session to another. Let’s ensure that change becomes part of the operating model and desk"
- **Caught by:** the owner.
- **Cause:** the model's stopping-point rule (OPERATING_MODEL.md, AGENTS.md "Working rules") says to write a handoff and tell the owner in the conversation, but gives the handoff no form the desk can read, and the desk has no notice for it.
- **Correction proposed:** in the operating model, a handoff written at a stopping point takes a fixed place and form in the project, naming the next step and the message to start the new session with; on the desk, a notice to the owner when a project's latest handoff waits for a new session, with that message ready to copy. Ruled by the owner (decisions/questions/P-001-session-move-notice.md): the change goes into both the model and the desk.
- **Status:** open; to the model and the desk under their own rules (the desk is graduated, so its part is new work the Chief of Staff files and the owner approves the route for).

### LL-26 The problem statement and pre-mortem cited findings the source checks had held back
- **What happened:** the Chief of Staff's first draft of the problem statement drew its "how other fields solved it" lines from Q-005's principles, several of which rest on entries the source-check confirmation holds back; it gave no transfer check on conditions, stated opinions as findings, and cited sections that do not support the claim (R4) or do not exist ("Q-003 §0"). The value-target question carried the same wrong section number.
- **Caught by:** the Critic (reviews/P-001-problem-premortem/critic.md, findings 2–4, 7, 8, 13; reviews/P-001-value-target/critic.md).
- **Cause:** drafting from the memos' short answers without reading each claim against the confirmation's hold list and the memo's own grades; section numbers written from memory.
- **Correction proposed:** before a drafted claim cites research, look up the entry's filing status in the confirmation (or the library, once filed) and cite only fileable entries, with their caveats; copy section numbers from the memo, never from memory.
- **Status:** fixed here (redrafted); model change open.

### LL-27 A question's pull request opened with a body that failed the form check
- **What happened:** the value-target question's pull request (#9) was opened with Context bullets ending in a full stop after the source; the pr-body check requires each bullet to end with its closing bracket, and failed. The body was corrected in place.
- **Caught by:** the pr-body check, read after opening.
- **Cause:** the body was written by hand and not run through the repository's own pr-body check before the pull request was opened.
- **Correction proposed:** run `governance_checks.py pr-body` on the drafted body locally before opening any pull request (the Chief of Staff now does so with a saved event file).
- **Status:** fixed here (practice changed); model change open (the check's message could name the trailing-character rule).

### LL-30 An answered question came back when the brief was merged
- **What happened:** the value-target question was drafted on the brief's branch, then filed from a separate branch (PR #9) and closed by the answer record (PR #10). The brief's pull request (#12) still carried the question file, so merging it after #10 put the answered question back on the default branch, where the desk would read it as waiting. Tidied away in PR #14.
- **Caught by:** the Chief of Staff, checking the default branch after the owner's merges.
- **Cause:** a question file drafted on a long-running branch and copied to an asks branch, never removed from the first.
- **Correction proposed:** draft a question only on its own asks branch, or remove it from the drafting branch once filed; and check the default branch's questions/ after every merge.
- **Status:** fixed here (PR #14); model change open.

### LL-31 The owner was given a wrong count of library facts and patterns
- **What happened:** answering whether the portfolio has desk access, the Chief of Staff said the desk would count "the 72 facts" but not "the 16 patterns". The library holds 69 facts and 19 patterns (88 entries, as the Source checker returned and the library pull request said).
- **Caught by:** the Chief of Staff, counting the merged library.
- **Cause:** the figures were written from memory, not counted from the Source checker's table.
- **Correction proposed:** count before stating any figure to the owner; corrected to the owner in the same session.
- **Status:** fixed here (owner told); closed for the model unless it recurs.

### LL-28 A portfolio pull request waiting on the owner does not show on the desk
- **What happened:** the library's pull request (portfolio #3) waits for the owner's merge, but the desk reads the portfolio repository only for its idea log, decision queue, rulings, intent and library fact names, not its pull requests, so nothing on the desk shows it waiting. The desk also counts library facts but not library patterns.
- **The owner's words, verbatim (2026-11-01):** asked "Does the portfolio have desk access?", and on being told of the gap, "Yes." to logging it and adding it to the desk follow-ups.
- **Caught by:** the owner's question; the Chief of Staff, reading the desk's configuration and portfolio reader (Service-Desk src/config/projects.json; src/public/lib/portfolio.js, RARE_DIRS).
- **Cause:** the desk was built to read the portfolio's records, not to treat it as a project with work in flight (Service-Desk decisions/questions/P-001-portfolio-read.md); the model has the Source checker open pull requests in the portfolio, which the desk was not designed for.
- **Correction proposed:** a desk follow-up, put to the owner with the Design gate: show the portfolio's open pull requests that wait on the owner, and count library patterns beside facts. Until then, the Chief of Staff gives the owner the link to every portfolio pull request that waits on them, in the same message (as for deploys, LL-23).
- **Status:** open; to the owner with the Design gate (desk follow-ups).

### LL-29 A push went ahead after a red governance check (LL-06 recurred)
- **What happened:** adding LL-28, the Chief of Staff ran the governance checks, committed and pushed in one command; the checks reported FAILED and the push went ahead. The failure was `record_checks merges`, which, run locally on a branch, judges the orchestrator's record commits as if they were on the default branch; in a pull request and after a merge commit it judges only the merge, and CI passed on the same branch (PR #13). So nothing wrong was pushed, but the push did not wait for the check.
- **Caught by:** the Chief of Staff, reading the command's output.
- **Cause:** the check's result was piped into `tail` inside a `set -e` command, so its failure did not stop the push; the same slip as LL-06.
- **Correction proposed:** LL-06 is reopened. Push only in a separate step after reading a passing result; and, for the model, run the local governance check the way CI does (against a test merge, or with the branch named) so a local run does not report a false failure that teaches people to ignore red.
- **Status:** open (recurred).

### LL-32 The owner was told two lessons were in a pull request that had already merged without them
- **What happened:** LL-28 and LL-29, and the handoff's new desk follow-up, were pushed to the branch of PR #13 and the owner was told "Both entries are in Model-Lab #13". The owner merged #13 before that push reached it, so the entries never reached the default branch; the Critic found the missing LL-28 while checking a question that cites it. Restored here, after LL-31 (so the log reads LL-27, LL-30, LL-31, LL-28, LL-29, LL-32).
- **Caught by:** the Critic (reviews/P-001-desk-follow-ups/critic.md, finding 1).
- **Cause:** commits were pushed to a pull request the owner was already merging, and the claim was made without checking the merged commit; the same family as LL-11.
- **Correction proposed:** never add commits to a pull request already put to the owner; open a new one instead. Before telling the owner that something is in a pull request, check the pull request's head, and after a merge, check the default branch.
- **Status:** fixed here (restored); model change open.

### LL-33 The owner was told asks pull requests would merge on their own; none can here
- **What happened:** three times this session the Chief of Staff told the owner that a question, answer or session-lines pull request "should merge on their own" through the asks-merge workflow. The workflow's log for Model-Lab says "no asks-merge grant stands in docs/LEDGER.md; nothing is merged": the owner merged #9, #10, #11 and #14 themselves, and #16 sat waiting.
- **Caught by:** the Chief of Staff, reading the workflow's log when #16 did not merge.
- **Cause:** the model's asks-merge delegation needs the owner's grant in each project's ledger; Model-Lab has none, and the Chief of Staff assumed it from the workflow's presence and from #9 closing quickly.
- **Correction proposed:** check the project's ledger for the grant before telling the owner anything will merge without them; offer the owner the grant as a question if they want it.
- **Status:** fixed here (owner told); the grant is the owner's choice.

### LL-34 The owner's token checkpoint double-counted helpers sent back for another round
- **What happened:** when a helper is sent a further round (a Critic's round 2, a Researcher's revision), the figure it reports is its running total, not that round's use. The Chief of Staff logged each running total as a new helper line and summed them, telling the owner "about 900,000" tokens for the first part of the session; the true figure was about 499,000. The session lines already on the default branch hold those running totals.
- **Caught by:** the Chief of Staff, logging the Researcher's revision, whose reported figure was larger than its first.
- **Cause:** the reported figure's meaning was not checked; the S-033 helper line has no field to mark a running total.
- **Correction proposed:** log only the increase for a resumed helper (done from the Researcher's revision on), and correct the figure to the owner; for the model, the session line should say whether a figure is a running total or one round's.
- **Status:** fixed here (owner told the corrected figure); model change open.

### LL-35 The desk's milestone screen is confusing, and for this project its standard milestones can never show as reached
- **What happened:** the owner, looking at Model-Lab's project page on the desk: "This milestone look is confusing, 1 milestone but 6/8 5 standard but none look like that in the desk?" Each phase's headline ("0 of 6 reached") adds the project's own milestones to the standard ones the desk can track, leaving out those the model marks "not recorded" (for Discovery, 1 own plus 5 of 8 standard). The words "taken on, not recorded by the model" are not explained. And although this Discovery has met several standard milestones (the value target, the groundwork answers, the research), every standard milestone reads "not recorded", because the checks read standard milestones only from the automatic pipeline's dispatch log, and this project's Discovery has run from a conversation with no dispatch-log entries (Personal-Org-Operating-Model tools/v3_checks.py, the `lines` method: with no item blocks, every standard milestone is "not recorded").
- **Caught by:** the owner.
- **Cause:** two at once. The desk's counts and wording were designed for the pipeline path; and the model gives a conversation-run project no record the standard milestones can be read from.
- **Correction proposed:** a desk change (counts that separate the project's own milestones from the standard checklist, and plain words for "not recorded") joins the desk work the owner ruled for after the Design gate (decisions/questions/P-001-desk-follow-ups.md); a model change gives conversation-run work a record the standard milestones read from, or reads them from the project's own records, as Discovery-2's rule already does when an item exists.
- **Status:** open; desk part routed by the owner's ruling, model part with this project's lessons.

### LL-36 The real-use odds were worked out at the wrong cutoff
- **What happened:** writing the count's starting figures into the brief, the Chief of Staff computed the "gain counts at" thresholds at a 5% chance cutoff while the same sentence, and the owner's ruling, say "at most 1 time in 25" (4%). Two of four thresholds, and their odds, were wrong.
- **Caught by:** the Critic (reviews/P-001-after-the-count/critic.md, finding 1).
- **Cause:** the calculation reused the earlier script's cutoff without re-reading the ruled one.
- **Correction proposed:** state the cutoff in the calculation itself and check it against the ruling before quoting a figure.
- **Status:** fixed here (recomputed at 1 in 25); closed for the model unless it recurs.

### LL-37 A session's own usage can be read after all
- **What happened:** the Chief of Staff told the owner, and the test-budget ruling's note records, that a session cannot read its own tokens or cost, so every end line held `null`. On 2026-11-01 the session's own status (the session tool's `get_session`) showed its context use (about 594,000 of 1,000,000 tokens), its input, output and cache tokens, and an estimated cost (about $49.77).
- **Caught by:** the Chief of Staff, checking context use before answering the owner's question about continuing.
- **Cause:** the model's rule (OPERATING_MODEL.md §8 "Chief of Staff sessions") says the session "cannot read its own tokens or cost"; it was taken as fact without testing.
- **Correction proposed:** end lines take the session's own figures where its status gives them; token checkpoints to the owner include the session's own use and estimated cost; the model's sentence is corrected. Remaining plan allowance is still not readable.
- **Status:** open; to the model with this project's lessons. Practice changed here from now on.

## 2026-11-02 — Discovery of P-001, session_01QBwHGN4kVVA3rfHx2b4FsF

### LL-38 A session's last records were pushed but never put in a pull request
- **What happened:** at the third stopping point, the previous session pushed its records (brief 16, the Critic's rounds on M1 and the open-unknowns question, LL-37, the handoff update) and its session lines to two branches, but opened no pull request for either, so neither reached the default branch; the handoff on the default branch still showed the second stopping point. Found at the start of this session and carried into its pull request with merge commits.
- **Caught by:** the Chief of Staff, comparing the remote branches with the default branch at session start.
- **Cause:** the session ended right after pushing; nothing checks that every pushed branch has a pull request or a stated reason not to.
- **Correction proposed:** before a session ends, list its pushed branches and open a pull request for each (or say in the handoff why not); a new session compares remote branches with the default branch before reading the handoff as current.
- **Status:** fixed here; model change open.

### LL-39 Two sessions gave the same lessons-log number to different entries
- **What happened:** the pull-request briefing session added "LL-36" (a push after a red check, in Service-Desk) on its own branch, while this project's log already holds a different LL-36 (the real-use odds); LL-37 is used on a third branch. If the briefing branch merges as it stands, two entries share an id.
- **Caught by:** the Chief of Staff, reading the unmerged branches at session start.
- **Cause:** sessions number entries from the log as they last saw it, on separate branches, with no check for repeated ids.
- **Correction proposed:** renumber the briefing session's entry when it lands (as the next free number); for the model, a check that lessons-log ids are unique, and sessions in parallel take numbers only when the entry lands.
- **Status:** fixed here (the briefing entry landed as LL-42); model change open.

### LL-40 A conversation-run project's gate case cannot show its milestones from the timeline
- **What happened:** the Design gate case must copy its milestone list exactly as the check prints it from the timeline; for this project the timeline prints nothing, because its Discovery ran from a conversation with no pipeline records (the cause LL-35 names). The case carries an empty block and a hand-written table of the standard milestones with their records.
- **Caught by:** the Chief of Staff, running the gate check on the draft case.
- **Cause:** as LL-35: the timeline reads standard milestones only from the pipeline's dispatch log and status files.
- **Correction proposed:** with LL-35's model part: give conversation-run work a record the timeline reads.
- **Status:** open; with LL-35.

### LL-41 Commits made under the default identity again (LL-13, LL-20 recurred)
- **What happened:** three Chief of Staff commits on the Design gate case and its question were made with `git commit -a` and no identity flags, so they carried the environment's default author; one also swept the session lines into a gate-case commit. Found by the surface guard's diff check before the push and re-authored; nothing wrong was pushed.
- **Caught by:** the surface guard's diff check, run before pushing (the practice from LL-18).
- **Cause:** a quick follow-up commit typed without the identity flags; the repository has no identity set for the session, so git falls back to the default.
- **Correction proposed:** set the session lane's identity once in the repository's config at session start, so a bare commit cannot fall back to the default; never use `commit -a` across lanes. For the model: the template's session start sets it.
- **Status:** open (recurred); the pre-push guard check worked.

### LL-42 A push went ahead after a red governance check again, this time in Service-Desk (LL-06, LL-29 recurred)
- **What happened:** filing the two route questions for the pull-request briefing page (Service-Desk questions/P-002-route.md and P-002-follow-ups.md), the Chief of Staff ran the governance checks and the push in one command; the checks reported FAILED and the push went ahead. The two failures were `record_checks merges`, the local-only false failure on the orchestrator's review-record commit that LL-29 describes, and `v3_checks trace`, which fails on the unchanged branch too because the session's clone holds only recent history and cannot see the desk's older sprint merges. So nothing wrong was pushed, but the push did not wait for the check.
- **Caught by:** the Chief of Staff, reading the command's output.
- **Cause:** the working rule from LL-29 (push only in a separate step after reading a passing result) lives in Model-Lab's handoffs and lessons, which a Chief of Staff session working in Service-Desk does not read at start.
- **Correction proposed:** in this session, push only as a separate step after reading the checks. For the model: carry the push rule into the template's AGENTS.md working rules, and make the local check run the way CI does (LL-29), so a red local run means something.
- **Status:** open (recurred).
- **Number:** filed on its own branch as LL-36 while this log already held a different LL-36; renumbered on landing to the next number free on every branch (LL-38 to LL-41 are taken by the open Design-gate pull request), as LL-39 there proposes. The Service-Desk handoff of 2026-11-02 still calls it LL-36.

### LL-43 The owner's Design-gate approval cannot be seen by the checks, so M1 cannot be marked reached
- **What happened:** the owner ruled the Design gate "proceed" and accepted M1. Adding M1's reached mark failed the milestones check: it reads a project's approval only from the automatic pipeline's status record (status/P-001.toml), which the Orchestrator script writes and this conversation-run project does not have. The mark was taken out; the rulings are recorded.
- **Caught by:** the milestones check, run before pushing.
- **Cause:** as LL-35 and LL-40: the model's tools read phase and approval only from pipeline records.
- **Correction proposed:** a way for a conversation-run project's gate ruling to reach the status record (the Orchestrator writes it from the ruling record, or the checks read the ruling record), put to the owner with LL-35's model part; until then, M1's mark waits.
- **Status:** open; with LL-35 and LL-40.

## 2026-11-03 — Design of P-001, session_01QBwHGN4kVVA3rfHx2b4FsF

### LL-44 The Definer was briefed to tag its commits with experiment ids, which the scope check rejects
- **What happened:** the Chief of Staff's brief told the Definer to end its commits with `Spec: E-001` (or E-002). The repository's scope check fails every builder commit whose `Spec:` names no file in specs/, so all eight commits failed it. Found before anything was pushed; the Definer rebuilt its branch under a draft spec, S-001 (the fair test, M2), with the registrations' reviewed text unchanged apart from the frozen line's commit.
- **Caught by:** the full governance check, run before merging the Definer's branch.
- **Cause:** the brief was written without checking how the checks read the `Spec:` trailer; the model gives experiments no id of their own that the checks accept, so they sit under a spec.
- **Correction proposed:** before briefing a builder, check what its commits' trailers must name (as LL-09 asks for the surface map); for the model, say in the experiment playbook that a registration sits under its spec and its commits name that spec.
- **Status:** fixed here; model change open.

### LL-45 A private repository's work was copied into a public one without checking first, and the ask was put without a question file
- **What happened:** the Chief of Staff started the Builder's replay session with access to the private operating-model repository, and told it to copy every helper transcript into Model-Lab, without checking that Model-Lab is public. Two replays' transcripts and patches from the private repository were pushed to a public branch before anyone noticed. The Chief of Staff then put the choice (make it private, remove it, or leave it) to the owner in the session without filing a question first. The owner ruled to leave it public (decisions/questions/P-001-model-lab-public.md).
- **Caught by:** the Chief of Staff, checking the repositories' visibility before landing the branch, after the Builder flagged the owner's email in three transcripts.
- **Cause:** the brief was written without checking where the records would be published; the project's data boundary names which AI service data may go to, but not which repositories are public.
- **Correction proposed:** before a brief moves records between repositories, check each one's visibility and say in the brief what may be copied; for the model, the data classes name repository visibility, and the environment check (LL-22) lists it.
- **Status:** fixed here (the owner ruled); model change open.

## 2026-11-04 — Design of P-001, session_01QBwHGLd77YbwCSMSPU26vW

### LL-46 An owner question described an option's effects without checking the code that decides them
- **What happened:** the gate-record question (questions/P-001-gate-record.md) first said a hand-written status record "could make [the script] start helper sessions or raise cards"; the Critic showed that an inert state exists. The redraft then called a "waiting-owner" record inert and the desk's response "not checked"; the Critic showed the script rejects such a record and the desk flags it as waiting on the owner. It passed at round 3, the last allowed.
- **Caught by:** the Critic, twice (reviews/P-001-gate-record/critic.md, rounds 1 and 2).
- **Cause:** the options' costs were written from a reading of one function, not from the code paths that decide them (the routing table, `check_status`, the desk's reader); "not checked" was written where checking was possible.
- **Correction proposed:** before an option states what a system will do, trace it through the code that decides it, and write "not checked" only for what cannot be checked; for the model, the question template asks for each option's effects to cite the record or code that shows them (as LL-09 asks for the surface map).
- **Status:** fixed here (practice changed); model change open.

### LL-47 A helper's reported figures were lost when the container restarted
- **What happened:** the Definer (brief 27) finished just before the session's worker restarted; its hand-back text survived in its transcript, but the token figure the harness reports at return was never delivered, so its session line records `tokens: null`.
- **Caught by:** the Chief of Staff, logging the Definer's return after the restart.
- **Cause:** the reported figure lives only in the return notice; the session line is written after the notice arrives, so a restart in between loses it.
- **Correction proposed:** for the model, the session line takes the figures from the helper's own transcript where the notice is lost, or the runner records them as the helper ends; the token checkpoint to the owner states which helpers' figures are missing.
- **Status:** open.

## 2026-11-04 — Design of P-001, session_01QBwHGMBo8kZsMCS2EvKNwd

### LL-48 A push went ahead beside a red governance check (LL-06, LL-29, LL-42 recurred)
- **What happened:** after a stop hook asked for untracked work to be committed and pushed, the Chief of Staff ran the full governance checks and the push as two calls sent at the same time, so the push did not wait for the result. The checks were red: `record_checks merges`, the known local false failure on the orchestrator's brief commits (LL-29), and `v3_checks gates`, a real failure in the first draft of the Build gate case (over 350 words, and placeholder lines without citations). The draft case reached the branch of draft pull request #39 with its gate check failing.
- **Caught by:** the Chief of Staff, reading the checks' output after the push.
- **Cause:** two calls that depend on each other were sent together; the rule "push only in a separate step after reading a passing result" was known and still not followed under a prompt to push.
- **Correction proposed:** as LL-29 and LL-42: a push is never sent in the same step as the checks it depends on; for the model, a pre-push hook that runs the checks the way CI does, so the rule does not rest on memory.
- **Status:** open (recurred); the case was fixed in the next commit.

### LL-49 A conversation-run project's Build gate case cannot cite its own spec
- **What happened:** the first draft of the Build gate case cited specs/S-001.md for the test's figures and options; `v3_checks gates` refused every such citation, because it builds the gate Critic's pack from the item's status record, `status/P-001.toml`, whose `spec` fills `{spec}`, and this project has no status record. The Design gate case met no such limit only because it cited no spec.
- **Caught by:** `v3_checks gates`, run on the draft.
- **Cause:** as LL-35, LL-40 and LL-43: the tools read a project's state only from pipeline records; the gate-record ruling forbids writing a status record by hand until the model changes.
- **Correction proposed:** with the gate-record change in the operating model (decisions/questions/P-001-gate-record.md): the record that carries the owner's ruling also carries the item's spec, so a conversation-run case can cite it; until then the Build gate case's citations of its spec are reported as this known gap.
- **Status:** open; with LL-43.

### LL-50 An owner question stated what a system would do without a record that shows it (LL-46 recurred)
- **What happened:** the first draft of the held-back store question said the sessions doing the tested work "never hold" the new private repository, and gave that option no costs; no record showed how the environment gives a session its repositories. The Critic failed it (reviews/P-001-heldback-store/critic.md, round 1, findings 1 and 2). The environment's own documentation, read afterwards, shows the protection holds only if judging sessions are started separately with that repository and the work's sessions never are.
- **Caught by:** the Critic.
- **Cause:** the option's gain was written from an expectation of how sessions work, not from a record; the environment's documentation was read only after the check, though it was available before.
- **Correction proposed:** as LL-46: before an option states what a system will do, read the record or documentation that decides it and cite it; record environment facts that an ask rests on in the project (as intake/P-001-environment-2026-11-04.md now does); for the model, the environment check of LL-22 records them at the start.
- **Status:** open (recurred); the question was redrafted. It recurred once more the same day: the second plan-stop card called its first option's secrecy "real" against the store question's own recorded caveat (reviews/P-001-plan-stop-2/critic.md, finding 1); the card is being rewritten after the store answer.

## 2026-11-04 — Design of P-001, session_01QBwHGKs5xh6cq2DgNNozv7

### LL-51 Uncommitted lines set aside in the checkout a Critic was reading (LL-19 recurred)
- **What happened:** three reworded standard-milestone lines in docs/PROJECT.md were left uncommitted on purpose, since a Critic must check a reworded line before it stands, and a Critic was dispatched to read them in the shared Model-Lab checkout. When a stop hook asked for uncommitted work to be committed and pushed, the Chief of Staff stashed the file there to run the checks on a clean tree, then saw that this hid the lines from the Critic and restored them within seconds. The Critic's return quotes the new lines, so its reading was not affected (reviews/P-001-standard-lines/critic.md).
- **Caught by:** the Chief of Staff, at once.
- **Cause:** as LL-19: one working copy shared between the Chief of Staff's own changes and a helper's reads; the clean copy for the checks was made only after the slip.
- **Correction proposed:** run pre-push checks in a separate worktree at the commit being pushed (done from then on), and never change a checkout a running helper was pointed at; for the model, with LL-19, helpers read from a fixed worktree for their brief.
- **Status:** fixed here (practice changed); model change open with LL-19.

### LL-52 An owner question left out what the pipeline's loop does on a red check (LL-46, LL-50 recurred)
- **What happened:** the first draft of the gate-citation question (questions/P-001-gate-citation.md) traced option A's red check through the gate check and CI, but not through the pipeline's loop, which holds all dispatches and merges while the default branch's latest check is red and files a CI-hold card after an hour; it also left out that quoting the criteria in the case breaks its 350-word limit. The Critic failed it at round 1 (reviews/P-001-gate-citation/critic.md, findings 1 and 2). Traced afterwards: the loop does not run in Model-Lab today, since it stops at its first step for want of its token setting.
- **Caught by:** the Critic, before the card reached the owner.
- **Cause:** the trace followed the check that refuses the citation, not every system that reads that check's result; the workflow header that names the loop's reaction was read for its trigger only.
- **Correction proposed:** as LL-46: when an option makes a check fail, list every reader of that check's result (CI, the loop, the asks-merge workflow, the desk) and trace each; for the model, the question template asks for it.
- **Status:** fixed here (redrafted for round 2); model change open with LL-46.

### LL-53 The two Build-gate cards used all three Critic rounds and still failed
- **What happened:** the gate card and the terms card failed the Critic at rounds 1, 2 and 3 (reviews/P-001-build-gate/critic.md). Each round fixed the findings before it and added new claims that were not traced: at round 3, option C2's chance stated the 100-piece figure for plans that stay at 60, and both cards said every failure "comes to you first" where the plan puts only some first checks to the owner as a question (LL-46, LL-50 again). The Build gate case went through three versions in the same session, each held by the gate Critic; case 3's main remaining finding is that it cannot show the terms card, which sits under questions/, outside the gate Critic's pack.
- **Caught by:** the Critic and the gate Critic.
- **Cause:** two at once. The cards carry most of a 370-line plan's figures and options, redrafted quickly between rounds, with each new sentence checked against the finding it answered but not against every record it touches. And, as LL-49, the gate tools assume the pipeline's records: a conversation-run case can cite neither the plan nor the cards the owner rules with it.
- **Correction proposed:** at the stop rule, Triage traces the cause and the owner rules how the cards go on (OPERATING_MODEL §4 "Stop rule"); before any redraft, every changed sentence is checked against the record it states, not only the finding it answers; for the model, with LL-49 and the gate-record change, a gate case can cite its item's cards and spec.
- **Status:** open. The stop rule was applied in session_01QBwHGKFFgmANWaCNGxCLZd: Triage traced the root cause to the cards' length (triage/P-001-build-gate-round-3.md); the owner ruled them cut down (decisions/questions/P-001-build-gate-stop.md, its record waiting on PR #47's merge), and the cut-down cards passed at their round 2 (reviews/P-001-build-gate/critic.md). The model part stays open.

## 2026-11-04 — Design of P-001, session_01QBwHGKFFgmANWaCNGxCLZd

### LL-54 A figure in the plan passed eight checks without anyone opening the script that makes it
- **What happened:** the plan tied its "32 to 64 weeks" to the order "the next kind collects while the previous is judged"; the script computes that figure as the slowest single kind, true only if all three kinds collect from the start. Three plan-review rounds and two card rounds passed it, and the recommended term on the terms card rested on it, until the cards' third round flagged it as minor and Triage rated it a plan fault (triage/P-001-build-gate-round-3.md, finding 4). Triage also found two more slips in the plan's statement of the owner's part. The Definer corrected all three; plan rounds 4 and 5 passed them (reviews/S-001/plan.md).
- **Caught by:** the Critic (cards' round 3, finding 4) and Triage.
- **Cause:** the checks compared the plan's figures with its own tables and output file, never with what the script's code computes; the meaning of a column ("together") was taken from its label.
- **Correction proposed:** a check of a figure that drives a decision reads the code that produces it, not only its output; for the model, the plan-review brief names the scripts behind the decision figures as must-read.
- **Status:** fixed here (the plan corrected); model change open.

### LL-55 The stop rule was applied to card checks, which no rule covers
- **What happened:** the cards' third failed Critic round was treated as "the last allowed", and the stop rule applied, at the owner's instruction; Triage and the Critic found that the model's three-round limit is written for plan and build rounds only, and no rule counts card checks or restarts their count (triage/P-001-build-gate-round-3.md; reviews/P-001-build-gate-stop/critic.md, round 1). The stop-rule question had to offer "the limit does not apply to cards" as an option and mark the redrafted cards' round count as an assumption.
- **Caught by:** Triage and the Critic.
- **Cause:** the model's stop rule names plans and built work; decision cards have their own repeated checks but no limit, and an earlier session applied the limit by analogy.
- **Correction proposed:** the model says whether, and how, the stop rule counts checks of decision cards, and whether a cut-down or redrafted card starts its count again.
- **Status:** open; to the model with this project's lessons.

### LL-56 A gate case was sent to its Critic two words over its limit, after an edit not re-checked
- **What happened:** the gate check passed on case 4; a one-line edit afterwards ("a week or more") was committed without re-running it, and the gate Critic's fixed copy was taken at that commit, 352 words against 350. The pre-push run caught it; the case was trimmed before the push, and the Critic, reading the fixed copy, counted about 349 by its own method (reviews/P-001/_build-gate-4-critic.md).
- **Caught by:** the full governance check, run in the separate check worktree before the push (the practice from LL-48 and LL-51).
- **Cause:** the check was run on the working tree before the edit was committed, and not again on the commit given to the Critic.
- **Correction proposed:** run the form check on the exact commit a helper's fixed copy is made from, as for a push.
- **Status:** fixed here (practice changed); closed for the model unless it recurs.

## 2026-11-04 — Build gate of P-001, session_01QBwHGJ9ZMyT9fK17HjfmCc

### LL-57 Read-only Critics were briefed to run git commands they cannot run
- **What happened:** brief 66 told the Critic to read the reworded lines with `git show`; the Critic has no shell, so it judged the lines from the current text only and said so in its return. The first draft of brief 69 again pointed it at `git diff` and `git show`; the Chief of Staff caught that before dispatch and gave it fixed copies at each commit to compare instead (docs/briefs/69-critic.md).
- **Caught by:** the Critic (reviews/P-001-build-terms/critic.md, round 1, opening paragraph), then the Chief of Staff.
- **Cause:** the brief was written from the Chief of Staff's own tools, not the helper's; the Critic's agent file grants Read, Grep and Glob only.
- **Correction proposed:** before a brief names a command, check the helper's tool grant; for a read-only checker, give a fixed copy for each version it must compare. For the model: the brief template names the helper's tools.
- **Status:** fixed here (practice changed); model change open.

### LL-58 Four line pointers in the fair test's plan pointed at the wrong lines through five plan rounds
- **What happened:** S-001's "Facts relied on" and one other line cited docs/PROJECT.md:96, :99 (twice) and :147 for V1, the starting figures and the outside-provider rule; those lines held other text. The plan passed five review rounds with them. The Critic's check of the settled text, run before the freeze landed, found them; the Definer corrected them and froze again (reviews/S-001/_critic-settled.md, round 1, finding 1).
- **Caught by:** the Critic.
- **Cause:** line-number citations drift as the cited file changes, and no check reads them; the plan reviews checked what the facts say, not where the pointers land.
- **Correction proposed:** a check that each `file:line` citation in a spec exists and holds the cited words, or citations by section heading; for the model, with LL-54, the plan-review brief asks for every pointer behind a decision figure to be opened.
- **Status:** fixed here (corrected before the freeze); model change open.

### LL-59 A checker's brief first named the same model as the work it checks
- **What happened:** brief 73 first set the Critic on claude-sonnet-5-5 to check the Check author's locked checks, which were written on claude-sonnet-5-5. Found and corrected to claude-opus-5-5 before dispatch.
- **Caught by:** the Chief of Staff, rereading the brief before dispatch.
- **Cause:** the Critic's usual model was carried over from briefs where the writer was the Chief of Staff (claude-opus-5-5); the model-diversity pair is the checker and the work's own writer, which changes with the work.
- **Correction proposed:** every checker brief names the checked work's writer and model, and the pair is compared before dispatch (as LL-03 asks); for the model, the runner's diversity check covers conversation-started helpers.
- **Status:** fixed here (corrected before dispatch); model change open with LL-03.

### LL-60 Three reading-only Critic rounds passed locked tests that would fail a correct build
- **What happened:** the Critic passed S-001's locked checks at round 3. The required Reviewer on pull request #51, which can run code, then found two tests that a correct build would fail: an AC6 fixture whose expected class contradicts E-003 Step 5, and J4 string matches that a byte-faithful fill of E-002's template cannot meet, since the template wraps the phrase across a line (reviews/51/reviewer.md, findings 1 and 2). It reproduced both with reference scripts. The checks were not yet locked, so they went back to the Check author.
- **Caught by:** the Reviewer.
- **Cause:** the Critic holds no shell, so it judged each test's expectation by reading; round 2 re-read only the changed files, and no round ran an expectation against the frozen text.
- **Correction proposed:** a check of locked tests runs each expectation against a small reference built from the frozen text before it passes (the Reviewer's method here); for the model, Build-1's record is the Critic's pass, so either the Critic's check of tests gets a shell or the Reviewer's run is part of Build-1.
- **Status:** open; the checks are being corrected before they lock.

### LL-61 Each fix to one test's record selection opened a new hole beside it
- **What happened:** J7's and J8's choice of which recorded manifest to check was changed four times (rounds 2 to 5 of the locked checks). Each change closed the case its finding named and opened a neighbouring one: a malformed record skipped, then a blind manifest listing the registration skipped, then a blind manifest lacking the extract skipped (reviews/S-001/_critic-checks.md, rounds 2 to 5; reviews/51/reviewer.md, round 3). Round 5 of the Critic and round 3 of the Reviewer failed the same hole independently. The Chief of Staff stopped there and put the stop to the owner, rather than run a sixth round under no rule (LL-55).
- **Caught by:** the Critic and the Reviewer.
- **Cause:** as LL-53: each fix was made and checked against the finding it answered, not against the whole set of records the test must classify; the selection logic has four inputs and was never written as a table of every case.
- **Correction proposed:** a fix to classification logic lists every input combination and its required result before it is written, and the check reruns all of them; for the model, LL-55's rule on how check rounds are counted covers locked checks too.
- **Status:** fixed here: the owner ruled one focused round (decisions/questions/P-001-checks-stop.md), each test got its own setting, and the Reviewer's run of every case passed (reviews/51/reviewer.md, round 4); model change open with LL-55.

### LL-62 An answer branch was pushed in the same step as its commit, before any check ran (LL-06, LL-29, LL-42, LL-48 recurred)
- **What happened:** recording the owner's answer to the checks' stop question, the Chief of Staff committed and pushed cos/p001-answer-checks-stop in one command, with no check run first. The full check, run straight after on that exact commit merged onto the default branch, passed, so nothing wrong was pushed.
- **Caught by:** the Chief of Staff, reading its own command after it ran.
- **Cause:** a small records commit, made right after the owner answered, felt too simple to check; the rule lives in the session's working notes, not in a hook.
- **Correction proposed:** as LL-48: a pre-push hook that runs the checks the way CI does, so the rule does not rest on memory.
- **Status:** open (recurred).
