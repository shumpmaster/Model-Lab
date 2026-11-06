Verdict: PASS

*The Critic on questions/P-001-harness-landing.md, brief 101 (docs/briefs/101-critic.md, on branch claude/chief-of-staff-p001-build-5m9j1d) for round 1 and brief 102 for round 2; a resumed session on a different model from the card's writer. Recorded verbatim by the Orchestrator, 2026-11-05. The first line is the latest round's verdict; round 1's was FAIL. After round 2 passed, the Chief of Staff changed only what attributes or removes claims, on round 2's finding 4: the WHY's line on not offering a change to the check is now the Chief of Staff's stated reason, and its words "outside this decision" are removed.*

## Round 1 (commit 211e335)

Two findings block the card, and both are about what the options really do. The rest of the card reads well. Its opening is plain, and its recommendation is labelled as the Chief of Staff's judgement.

1. BLOCKING. Option B and Context bullet 6 say exempted commits "skip every check of their range". The card also implies the exemption makes the failing check pass. Reading governance/checks/surface_guard.py shows two things the card does not say.
   - `range_violations` (lines 308-316) skips an exempt commit as a commit under check. But `independence_violations` (lines 371-400) takes its list of specs from the checked commits only, and takes its list of sessions from `history`. `history` (line 232) is every non-merge commit reachable from the head, exempt or not.
   - So exempting the three builder commits helps only while no other checked commit in the range names the same spec. If any commit in the range carries "Spec: S-001", the guard still reads the exempt builder commits and the check author's commit as one session, and it still fails.
   - The same holds for every later range on S-001, because the exempt commits stay in the history it reads. The milestone line is "Build-2, Build-3".
   - B's gain ("the reviewed commits land as they are") is therefore conditional. Its cost is understated, and "Reversible: yes, by removing the listing" is only true in that removing it makes the failure come back.
   - Fix: say exactly what an exemption skips (the per-commit checks) and what it does not (the commits still count as evidence in the independence rule). Say under what condition B lets the harness land, and what happens at the next S-001 range.
   - The cited lines of SURFACES.md, lines 115-118, do hold the ledger-entry and R3 claims.

2. BLOCKING. Option C is not stated fairly or consistently.
   - C says "a new builder, started as a session of its own with its own id". The card's own source, LL-65 (docs/LESSONS.md, "Cause"), says a helper started with the Agent tool has no session id of its own that the brief records.
   - So the card does not say how C gets that id. It could be an owner-started top-level session, as in E-001, or a made-up label as in A. That is a cost, and it is missing.
   - The recommendation's "wanting no change to how helpers sign (then B or C)" is wrong for C if the id is a label. C would then change signing too.
   - "Cost: … three new review rounds" is a guess presented as a figure. The 1.3 and 1.0 million tokens are true as totals. I summed the Builder helper lines of the session file (355,075 + 474,630 + 510,540 = 1,340,245) and the Reviewer lines (245,508 + 347,728 + 371,399 = 964,635).
   - A rebuild with the fixes already known need not repeat three rounds. Say "an estimate" or drop "three".

3. Not blocking. In option A, "an id naming its own helper session under this one" overclaims. LL-65 proposes a constructed label (`<session id>/<role>-<brief>`), not a real session id. The guard only compares strings (lines 388-398), so a label passes it. Say it is a label the guard accepts.
   - A's cost does name the departure from CLAUDE.md and the precedent for later helpers. Good.
   - No check I saw (sessions, trace) constrains the format of the id for helpers.

4. Not blocking. The recommendation's reasons lean a little: "B hides the commits from all their checks, and C repeats a build that passed." Both phrases are advocacy, not fact. State neutral costs in the options instead.

5. Not blocking. A fourth route is missing and not mentioned as ruled out: change the guard to accept a helper's own id form. That is what LL-65's "correction proposed" says for the model. The card can say why it is not offered, for instance that governance/** is high risk and outside this decision.

6. Not blocking. Smaller points.
   - The opening says "every locked check passes". It is 228 tests with 2 skipped by design (reviews/57/reviewer.md section 1). Say "pass or are skipped by design".
   - "With your correction of the one wrong check" is true. reviews/57/owner.md exists, but the card does not cite it.
   - The opening says the Reviewer found the shared signature. That is true (reviews/57/reviewer.md finding 1). That Reviewer suggested landing separately. The card rightly says it does not help, because `history` (line 232) includes the check author's commit. LL-65 admits its first version proposed this, and the card reports that fairly.

Verified true:
- The Reviewer passed the harness at round 3 (first line of reviews/S-001/_reviewer-build.md).
- The three builder commits are 3861b38, a42c2df and 9caff21.
- Briefs 90 and 99 name the same Agent-Session value and the different models (opus and sonnet).
- CLAUDE.md gives the trailer as `<session id>`.
- The independence rule is as the card says: "one session wrote both checks and code".

Whose judgement is whose: the recommendation is labelled the Chief of Staff's judgement and there is no default. That is consistent. The "I said otherwise earlier, and was wrong" line is honest, but it is in the first person in the owner-facing paragraph, so the voice is clear. Length: the card is cut down, though its opening is about 170 words.

Six-part contract
- Changed (by file): none. I have no write tool.
- Why: round 1 cold read of questions/P-001-harness-landing.md against the decision-card standard, and against what surface_guard.py actually does.
- Verified (command + output): I read only.
  - The card.
  - reviews/57/reviewer.md.
  - reviews/S-001/_reviewer-build.md, round 3 and line 1.
  - governance/checks/surface_guard.py lines 224-233 and 278-427.
  - governance/SURFACES.md lines 110-120.
  - CLAUDE.md.
  - docs/briefs/90-builder.md and docs/briefs/99-check-author.md.
  - LL-65 in docs/LESSONS.md.
  - sessions/chief-of-staff/session_01QBwHGNGKXFwvVVdzkei5aT.jsonl.
  - v3_checks.py lines 145-176 (the sessions and trace checks), for any limit on the id's form.
  I did not read docs/reports/**.
- Undone: I ran nothing, including the guard. The conclusion in finding 1 comes from reading the code, not from running it. I did not read the whole of the 2,000-line v3_checks.py, only the parts that name session ids. I did not confirm that PR #57 merged.
- Needed outside my surface: the Chief of Staff redrafts the card for findings 1 and 2, and ideally 3 to 6. Then round 2.
- Open questions: does the independence rule fire in the landing range, or only later? That depends on whether any checked commit in the range carries "Spec: S-001". The Chief of Staff can settle it by running `surface_guard.py diff` on the exempted range before the card is filed.

## Round 2 (commit 387af76)

Both round 1 blockers are fixed, and I found nothing new that blocks. Findings 3 to 5 are optional.

1. Not blocking. Round 1 finding 1 (what an exemption skips) is fixed, and the intake record supports it.
   - Context bullet 3 now says the check "takes the specs from the commits checked and the sessions from every commit reachable, exempt or not". That matches surface_guard.py: `independence_violations` reads its specs from the checked commits, and its sessions from `history`, which is every non-merge commit reachable.
   - Option B now says it lands, and that "every later commit of the builder's on this plan then fails the same check, from any session". The intake record (the Option B section) shows the landing range OK with 3 exempt, then a later builder commit from `session_other` failing with "the exempt commits are still in the history the check reads".
   - B's cost and its "Rules out: later work under this plan, until that fix" now follow from that run. The "exempt commits also skip their other checks" matches the code.

2. Not blocking. Round 1 finding 2 (option C) is fixed.
   - C now says a new cloud session is started with its own id, "as an earlier step's builder was". docs/briefs/25-builder.md supports that: the Builder there ran as a separate cloud session with its own session id.
   - LL-65 supports "a helper started from this session has no id of its own on record".
   - "Gain: … no new signing form" is consistent.
   - The cost is now "estimated from this time's 1.3 and 1.0 million tokens, fewer if its findings are fixed first". That is labelled an estimate. The token totals are true (sums of the session file's helper lines: 1,340,245 and 964,635).
   - C was not run on a copy, and the card does not claim it was. The recommendation says A is "the only option tried".

3. Not blocking. Option A is supported by the runs and is stated plainly.
   - The intake record shows the same tree as 9caff21 (`git diff --quiet 9caff21 HEAD`), the landing range OK with 4 commits checked, and a later builder commit from `session_other` OK.
   - The card says the check "compares the ids as text, so it accepts the label". That is honest that the check is met by the form of the id, not by a real separate session.
   - Two small gaps. The run compared only the final tree, so "byte for byte" per commit is left to the reviewer, as the card says. And "passes … on later work" holds only while later helpers sign with a label, which the cost line says.
   - "Reversible: yes" for A is a little generous. The label stays in the history and the precedent stays too. Optional wording: "the change, yes; the label stays on record".

4. Not blocking. The WHY says "Changing the check itself is not offered: it is a governance file, outside this decision, and the operating model's change is already proposed." That is the Chief of Staff's judgement stated as fact. Label it as such, for example "I leave it out because…". LL-65's "correction proposed" and status "open" support the "already proposed" part. The owner could still rule on a guard change, so the card should not say it is outside the decision.

5. Not blocking, smaller points.
   - The intake record also says the full governance check on A passes every step except `record_checks merges`, which fails locally on any orchestrator merge commit (LL-29). The card does not mention it, which is fine because that failure is not the check at issue.
   - No run covers B's or C's full check. The card only claims the guard runs.
   - C does not say who starts the cloud session. If the owner does, that is a cost to the owner.
   - The recommendation's reasons are now neutral. "Hides" and "repeats a build that passed" are gone, and the reason is the tried result. Whose judgement is whose is clear, since the recommendation is labelled the Chief of Staff's, at medium confidence.
   - The opening is plain and has no paths or ids. It says what failed and what the owner decides, and it admits the earlier mistake in the first person. The card is short enough.

Citations checked and true: reviews/S-001 round 3 PASS; reviews/57 section 1, finding 1 and owner.md; surface_guard.py; SURFACES.md exempt block (ledger entry, R3); CLAUDE.md; briefs 25, 90 and 99; LL-65; and the token totals.

Six-part contract
- Changed (by file): none. I have no write tool.
- Why: round 2 cold read of the redrafted questions/P-001-harness-landing.md. It checks that each changed sentence is true of its record and that the intake runs support what each option is said to do.
- Verified (command + output): I read only.
  - The new card and the intake record of runs.
  - docs/briefs/25-builder.md.
  - LL-65 (in the fix-rec2 copy).
  - My round 1 reads of surface_guard.py, SURFACES.md, CLAUDE.md, reviews/57, reviews/S-001, briefs 90 and 99, and the session file; I treated them as unchanged. I did not re-open them.
  - I did not read docs/reports/**.
- Undone: I ran nothing. I rely on the Chief of Staff's recorded runs for what the guard does on each option. I did not re-run them, and C was not run by anyone. I did not re-compare the round 1 card line by line, beyond reading its sentences in memory.
- Needed outside my surface: the Orchestrator records this as round 2 in reviews/P-001-harness-landing/critic.md. The Chief of Staff can then take the card to the owner.
- Open questions: none.
