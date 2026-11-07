Verdict: FAIL

*The Critic on docs/briefs/119-sheet-lead.md and the changes to docs/briefs/113-work-session.md after the owner's K1 ruling, brief 120 (docs/briefs/120-critic.md, on branch claude/p-001-model-lab-continue-ohykg9) for round 1 and brief 121 for round 2; the Critic session of briefs 114 to 116, resumed, on a different model from the briefs' writer. Recorded verbatim by the Orchestrator, 2026-11-07. The first line is the latest round's verdict, and each round's verdict line is given here rather than in its section (LL-68).*

## Round 1 (commit e0411a9)

Brief 120: brief 119 against brief 110, and brief 113 against round 3, under the owner's ruling B (decisions/questions/P-001-k1-transcript-reach.md). Copies are in /tmp/claude-0/-home-user/9a06fe22-60e0-580d-8926-30c8a46558b9/scratchpad/fix-rule and /tmp/claude-0/-home-user/9a06fe22-60e0-580d-8926-30c8a46558b9/scratchpad/fix-work3. I diffed both pairs: the only changes in each are the ones you named. One gap in brief 119's step 6 blocks: it no longer stops when the sheets repository is in a listing.

### What passes
- **Brief 119 accepts the Orchestrator's record as it stands** (fix-rule/reviews/E-003/built/sessions.md):
  - `k1-i: refused …` and `k1-ii: refused …` meet "read `refused`".
  - `k1-iii: returned 1 events` matches `returned <n> events`.
  - The `limit:` line names decisions/questions/P-001-k1-transcript-reach.md.
  - `k1: fail`, with part (iii) the only part not refused, matches the new rule.
  - The canary can only be in the two error lines; step 6 still checks for it.
- **Brief 119 still stops when part (i) or (ii) is not refused, or the canary is shown.**
- **Brief 113's record would pass brief 119's step 6 when only part (iii) returned.** Its step 2 records `k1-i`/`k1-ii: refused …`, `k1-iii: returned <count> events`, `k1: fail`, and then `limit: k1-iii returned; … (decisions/questions/P-001-k1-transcript-reach.md)`. Each line meets step 6. If the work session does not hold `list_events`, `k1-iii: refused …` passes as before.
- **Brief 113's exception does what the ruling says and no more.** It applies only when part (iii) is the only part not refused and the listing showed the sheets repository absent. Any other failure still waits for the owner, as the ruling's second bullet says.
- **The bars the ruling keeps are unchanged in both briefs.** Brief 113's "What you never do" still bars `list_events`, `get_event`, `send_message` and `add_repo`. Brief 119's line 18 bars are unchanged.
- **The other changes are consistent:** brief 110 is now 119 in brief 113's first-message line and step 2, brief 119 is added to the excluded briefs in step 7, and the recorded lines cite the ruling.

### Findings
1. **Blocking: brief 119's step 6 no longer catches the sheets repository in a listing.**
   - Under brief 110, step 6 required `k1: pass`, and K1 gives `pass` only when the listing shows the sheets repository absent. That was the only route by which step 6 caught a listing showing it.
   - Brief 119 accepts `k1: fail` "with part (iii) its only part not refused". A record whose parts (i) and (ii) were refused, part (iii) returned, and whose listing showed secret-marking would read `k1: fail` and pass step 6. A `limit:` line naming the ruling would make that record pass, and the sheet lead would start the Check author.
   - That contradicts S-001 K1, the ruling's second bullet ("the sheets repository in a listing … still stops them") and brief 113's own exception, which requires the listing absent.
   - Fix: add to step 6 that each record's `listing:` line does not name shumpmaster/secret-marking. Both records have a `listing:` line: the Orchestrator's names its four repositories, and brief 113's records one per turn.
2. **Non-blocking: the "Only step 6 differs from brief 110" sentence.** It is true in substance, but the title, session line, recorded line and the first message's path also differ. Saying "only step 6 differs in what the session does" would be exact.
3. **Non-blocking: the Orchestrator's part (iii) was run against the old sheet session.** That session was session_01QBwHGMdAN8qZZjthob7jc1, which now stops at its step 6. Brief 119's new session has a new id, and its step 6 still tells the owner that id "for K1's part (iii)". Only the work session will now probe the new session. The ruling accepts the existing record, so this is not a fault. A clause saying the Orchestrator's record stands as recorded and the new id is for the work session's probe would avoid the owner asking the Orchestrator to re-probe.
4. **Non-blocking:** the J4 block has no field for the limit. The ruling puts the limit in "every kind's record", which is the Orchestrator's records and not either brief. No change is needed in these briefs.

### Six-part contract
- **changed:** none (read-only check).
- **why:** check that briefs 119 and 113 carry out ruling B on K1 part (iii), and nothing more, against S-001 K1 and the Orchestrator's K1 record.
- **verified:** `diff` of brief 110 against 119 and of brief 113 (fix-work3) against 113 (fix-rule): only the named lines differ. I read the ruling, the Orchestrator's sessions.md, and step 6 and step 2 line by line against S-001 K1's cases.
- **undone:** none.
- **needed outside my surface:** the Orchestrator to add the listing condition to brief 119's step 6 (finding 1), and to consider findings 2 and 3.
- **open questions:** should the Orchestrator probe the new sheet session's id, or does its record against the old session stand for K1 part (iii)?

## Round 2 (commit b766bb4)

Round 2 (brief 121) of brief 119. I compared /tmp/claude-0/-home-user/9a06fe22-60e0-580d-8926-30c8a46558b9/scratchpad/fix-rule2/docs/briefs/119-sheet-lead.md with the round 1 copy in fix-rule. Only the session line and step 6 changed. Brief 113 and the Orchestrator's sessions.md are byte-identical to round 1. All three of my round 1 findings are addressed, but the new listing test would stop the session on the Orchestrator's own record, which the ruling says must pass.

### Round 1 findings
1. **The sheets repository in a listing (was blocking):** the gap is closed, but the new wording fails the Orchestrator's record (finding 1 below). Step 6 now requires that "no `listing:` line names shumpmaster/secret-marking". That closes the round 1 hole: a record whose listing shows the repository now stops the session, as S-001 K1 and the ruling's second bullet require.
2. **"Only step 6 differs" wording:** answered. It now reads "Only step 6 differs from brief 110 in what the session does", which is exact.
3. **The old sheet session's id:** answered. Step 6 now says the new id is for the work session's probe. It also says the Orchestrator's record, made against brief 110's session, stands, and marks that as the Orchestrator's reading. The ruling does not settle whether the Orchestrator must probe again; it accepts the record as it was found, so the reading is needed. It is also no looser than the ruling: the route is already known to exist, and it is stated as a limit.
4. **No field for the limit in the J4 block:** nothing was needed in the brief, and nothing changed.

### Findings
1. **Blocking: the new listing test stops the session on the Orchestrator's own record.**
   - The Orchestrator's listing line in fix-rule2/reviews/E-003/built/sessions.md ends: "(the session's status and the checkouts under /home/user; shumpmaster/secret-marking absent)".
   - That line names shumpmaster/secret-marking. Read as written, step 6 ("no `listing:` line names shumpmaster/secret-marking") stops with `stopped: k1` on the record the ruling says must pass.
   - Brief 110 and brief 119 both stress exact reading (the block forms, `refused` read literally), so a literal reading is the likely one.
   - Fix: word it as "no `listing:` line lists shumpmaster/secret-marking among the session's repositories (a line that records it absent passes)". Brief 113's `listing: <repositories, comma-separated>` form meets that test without a parenthetical. The record should not be edited, since it is a record.

### Six-part contract
- **changed:** none (read-only check).
- **why:** check round 2 of brief 119 against my round 1 findings, the ruling and the Orchestrator's K1 record.
- **verified:** diffed 119 between fix-rule and fix-rule2 (session line and step 6 only). Diffed 113 and sessions.md between the copies (identical). Read the new step 6 against each line of sessions.md and against brief 113's record forms.
- **undone:** none.
- **needed outside my surface:** the Orchestrator to reword step 6's listing condition (finding 1).
- **open questions:** none.
