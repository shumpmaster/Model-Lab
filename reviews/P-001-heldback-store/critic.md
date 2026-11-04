Verdict: PASS

The Critic's check of questions/P-001-heldback-store.md (brief: docs/briefs/37-critic.md), on claude-sonnet-5-5, a different model from the question's writer, verbatim. Recorded by the orchestrator. Session session_01QBwHGMBo8kZsMCS2EvKNwd, 2026-11-04. FAIL at round 1; PASS at round 2 (commit 6dce93a), whose two non-blocking notes were then applied in the wording it suggested.

## Round 1
Findings. Blocking ones come first.

1. BLOCKING. Option A's central gain is stated as fact, and no record shows it (LL-46).
   - The card says "the sessions that do the work being tested never hold that repository". It also says judging "runs in its own session with that repository attached".
   - No record I can read shows that the work's sessions would lack the new repository. No record shows the environment can attach a repository to the judging session only.
   - The nearest records point both ways.
     - docs/handoff/2026-11-04-chief-of-staff.md:20 says a separate cloud session attaches repositories with add_repo, and that attaching a private repository needs the owner's approval in that session.
     - docs/briefs/25-builder.md:16 says the same attach step.
     - Context bullet 3 of the card says all four repositories sit in this environment and "every helper it starts can read them". That bullet is why B fails. If an environment-wide repository list is the mechanism, a new repository added to it is as visible as the portfolio.
   - What is recorded is that attaching is a per-session act. Nothing recorded stops any other session from attaching a repository the owner has authorised.
   - Fix: either cite a record that shows per-session attachment keeps the new repository away from the work's sessions, or reword A's gain as a design intent that depends on how sessions are set up, and say what is unproven. A's cost should also name the owner's approval each time a judging session attaches a private repository.

2. BLOCKING. A's "Rules out: nothing" and the opening's "either can be changed later" are not supported, and the cost accounting is lopsided.
   - Rules out: B has a stated cost ("a test whose secrecy does not rest on instruction"). A is given none, though A has real ones:
     - dependence on the owner creating the repository;
     - a standing approval step for each judging session;
     - a new thing to keep for 60 to 121 weeks.
   - Moving from B to A later does not undo exposure. Sheets written into a repository every session can read cannot be un-seen. If the sheets were exposed, they would have to be rewritten and re-fingerprinted. So "reversible" and "can be changed later" hold only if no exposure happened. The card should say so.

3. Not blocking. One Context fact cites a record that does not say it.
   - Bullet 5 cites specs/S-001.md, "Budget options by kind and order". That table supports "60 to 121 weeks" (option A, one after another, at the Service Desk's pace). It says nothing about a session's machine being reclaimed.
   - I found no record for the reclaim claim. Split the bullet and give a source for the machine fact, or soften it.

4. Not blocking. The two non-file sources are acceptable only in part.
   - Source 1 is "the session's own record of its sources, session_01QB...". It is acceptable for the fact that four repositories are held. It is thin for "every helper it starts can read them".
   - On that point, the on-disk checkouts under /home/user (Model-Lab, Service-Desk, Personal-Org-Operating-Model, portfolio) confirm four repositories. My own plan-review work has read portfolio paths from this environment, so read access is corroborated for this session.
   - Source 2 is "the session's repository listing, 2026-11-04", for portfolio private and Model-Lab and Service Desk public. I could not confirm it from any file. The checkouts' git config shows only github.com/shumpmaster/... remote URLs, with no visibility flag. I accept it as a dated session observation, but it rests on a listing no record holds.
   - Every claim, and A's whole case, depends on the private/public fact. Ask for the listing's output to be recorded, for example in the card or the handoff.
   - The card is silent on whether Personal-Org-Operating-Model and Service-Desk are private or public. It says Service Desk is public.

5. Not blocking. The options are mostly fair, but the layout leans toward A.
   - B's gain is only "no new repository; nothing needed from you". It is not credited with simplicity, with no extra attach step, or with keeping the sheets in the owner's own private store.
   - The RECOMMENDATION ("only A keeps them out of the work's reach") repeats finding 1's unproven claim.
   - Recommending A is reasonable, but the recommendation line should carry the same caveat.

6. Not blocking. A reasonable option is missing.
   - Option C: the sheets are not held by any session or repository. The owner keeps them, or a store outside GitHub holds them (for example the owner's own encrypted storage), and a judging session is handed the one sheet it needs at run time. This is the strongest answer to "last as long as the test" without exposing sheets to the work.
   - Option D: the sheets sit in the portfolio repository but are encrypted, with the key given only to the judging session. This is an in-between that needs no new repository.
   - The card should say why these are out, or add them.

7. Not blocking. The opening paragraph is plain, but not fully compliant.
   - It has no ids or paths, and it states the cost to the owner and the reversibility. That is good.
   - "(the last fit-together check, finding 2)" is a cross-reference in jargon the owner has not been told. "Fit-together check" is not explained.
   - Under AGENTS.md "Plain English first", leading with anything failed or skipped is expected. The opening could say plainly that the plan failed its last check for lack of this answer.
   - The WHY line uses paths. That is acceptable, since it is not the opening.

8. Not blocking. Risk class, reversibility, default and timeout.
   - RISK CLASS R0 is right: questions/** is R0 in governance/risk-paths.toml:23.
   - REVERSIBILITY "reversible" follows from R0, subject to finding 2's exposure point.
   - DEFAULT "none" and TIMEOUT "none" depart from AGENTS.md §5, which says reversible questions adopt the recommendation at timeout. The reason given (A needs the owner's own action) is sound, and the precedent in decisions/questions/P-001-plan-stop.md ("the owner's own choice, never a default") supports it. The template's DEFAULT field wants a letter and TIMEOUT wants hours. State the departure in the field, for example "none, by the choice-question rule", so it does not read as an omission.

9. Checked and true of the cited records.
   - reviews/S-001/plan.md "Round 4" finding 2 says the store location and fingerprint method for the held-back checks are in no record. That matches the card's WHY and Context bullet 1.
   - S-009 AC8 "Known limit" says where the sets are stored is not decided (Open Items group 2). That matches Context bullet 2.
   - decisions/questions/P-001-plan-stop.md says the owner chose A, the focused fix. The rule change is drafted for separate approval. That matches Context bullet 6.
   - The "60 to 121 weeks" figure matches the S-001 table for option A.
   - The card's form matches questions/_TEMPLATE.md: Milestone line, WHY, OPTIONS, RECOMMENDATION and Context are all present.

Six-part contract:
1. Changed: nothing. I hold no write tool.
2. Why: to check the owner question cold against its cited records, per brief 37.
3. Verified:
   - I read questions/P-001-heldback-store.md and questions/_TEMPLATE.md.
   - I read reviews/S-001/plan.md Round 4 finding 2 and S-009 AC8.
   - I read the S-001 "Budget options by kind and order" table and decisions/questions/P-001-plan-stop.md.
   - I read AGENTS.md §5 and "Plain English first", and governance/risk-paths.toml.
   - I read the git remote URLs of the checkouts under /home/user.
   - I grepped the handoff and briefs for the attach rules.
   - I ran no command.
4. Undone:
   - I could not confirm private or public status from any file.
   - I did not read governance/SURFACES.md or the session runner for how packs limit what a session can read.
   - I did not check the Service-Desk or Personal-Org-Operating-Model files beyond the cited AC8.
5. Needed outside my lane: the Chief of Staff to fix findings 1 to 3 (the writer fixes; I do not). A recorded copy of the repository listing for finding 4.
6. Open questions: does the environment let a repository be attached to one session only, with no standing access for the others? The answer decides whether A's gain is true.

Files: /home/user/Model-Lab/questions/P-001-heldback-store.md (under review).

## Round 2
Round 2 findings. None are blocking.

1. Round-1 finding 1 (A's protection stated as fact): resolved.
   - A now says its protection holds only if judging sessions alone are started with the new repository. It says outright that this "rests on how sessions are set up, which no test has yet shown".
   - The cost now names the approval wherever a session asks to attach a private repository.
   - Context bullet 3 and intake/P-001-environment-2026-11-04.md lines 21-23 and 26 back the mechanism. Repositories are chosen at session start, and subagents share the container.
   - The recommendation carries the same condition.

2. Round-1 finding 2 (A's costs and "Rules out: nothing", and the claim that either can be changed later): resolved.
   - A now has costs and rules out judging from the work's session.
   - The opening and the blast radius both say a sheet the work may have seen must be rewritten and re-fingerprinted.

3. Round-1 finding 3 (the machine-reclaim claim miscited): resolved, with a small weakness.
   - Context bullet 5 now cites the intake file, and so does the 60-to-121-weeks bullet 6 (to S-001).
   - Intake line 28 admits the reclaim fact comes from "this session's operating instructions ... not a file record". It is disclosed honestly. I accept it as a dated session observation.

4. Round-1 finding 4 (the two non-file sources): resolved.
   - The repository listing is now recorded in intake lines 5-15. It gives portfolio and the operating model as private, and Model-Lab and Service Desk as public. That matches Context bullet 4.
   - The listing is copied by the Chief of Staff and is not independently checkable. That is acceptable for a dated tool observation.

5. Round-1 findings 5 and 6 (fairness, and a missing option): resolved.
   - B now has fair gains.
   - Option C (the owner keeps the sheets) is added. The encrypted-sheets idea is dismissed with a sound reason: the key would need the same hidden place.
   - C's arithmetic checks out against AC5 (specs/S-001.md:131): 60 × (2 + 2 + 1) = 300 judging sessions.

6. Round-1 findings 7 and 8 (the opening, and default/timeout): resolved.
   - The opening has no ids or paths, and "fit-together check" is gone.
   - DEFAULT none and TIMEOUT none are now explained by the choice-question precedent and the point that each option needs the owner's action. Risk class R0 stays correct, since questions/** is R0 in governance/risk-paths.toml.
   - Minor and non-blocking: the opening's "partly" and "may run for over a year" are fair to the records (60 to 121 weeks).

7. Non-blocking, new. The card omits a caveat that its own intake records.
   - Intake line 27 says nothing read shows whether the environment's settings add a repository to every new session.
   - If they do, A's condition cannot be met and A collapses to B. The card's "which the first judging would confirm" only partly covers this. It would be fairer to name this unknown in A's gain, or to say the owner should check the environment's repository settings when creating the repository.

8. Non-blocking, new. C's gain wording is slightly too strong.
   - "No repository or session ever holds them except the one judging" ignores the writing helper's session and the Chief of Staff's session, through which the owner receives each sheet. The text of each sheet passes through them once.
   - Say "no repository holds them, and only the writing session and the judging one see each".

Six-part contract:
1. Changed: nothing. I hold no write tool.
2. Why: to check the redrafted P-001 question and the new intake record against my round-1 findings, per brief 37.
3. Verified:
   - I read questions/P-001-heldback-store.md and intake/P-001-environment-2026-11-04.md.
   - I re-read specs/S-001.md AC5 at line 131 and checked the 300-session sum by hand.
   - I relied on my round-1 reads for the rest, including the plan Round 4 finding 2, AC8, risk-paths.toml and AGENTS.md §5.
   - I ran no command.
4. Undone:
   - I did not re-read reviews/P-001-heldback-store/critic.md.
   - I did not check the "github.access" documentation page itself, only the extracts.
   - I did not confirm the repository visibility myself.
5. Needed outside my lane: the Chief of Staff may fix findings 7 and 8 (the writer fixes; I do not). Neither stops the card going to the owner.
6. Open questions: do the environment's settings add a repository to every new session? (Finding 7.)

File: /home/user/Model-Lab/questions/P-001-heldback-store.md
