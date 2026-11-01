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
- **Correction proposed:** options to the owner before the second idea's Discovery starts.
- **Status:** open.

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
