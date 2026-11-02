Verdict: PASS

The Critic's definition-of-ready check of the whole project document (docs/PROJECT.md, Part 1 and Part 2), on a different model from its writer (brief: docs/briefs/17-critic.md), verbatim: round 1 (FAIL), round 2 (PASS). Recorded by the orchestrator. Session session_01QBwHGN4kVVA3rfHx2b4FsF, 2026-11-02.

## Round 1
Verdict: FAIL
Item 1: PASS
Item 2: PASS
Item 3: PASS
Item 4: PASS
Item 5: PASS
Item 6: PASS
Item 7: PASS
Item 8: FAIL
Item 9: PASS
Part 2: FAIL

Findings. I read /home/user/Model-Lab/docs/PROJECT.md cold, against the OPERATING_MODEL.md §4 definition of ready, the Model-Lab decisions, research and LESSONS records, and the portfolio's IDEAS.md and library README.

1. BLOCKING, Item 8, section 5 (Limits) against section 7 (U3, R3).
   - Section 5 says the data go "only to the AI service the sessions already run on". It also says "no paid services, data, tools or extra usage" beyond the owner's plan.
   - Section 7 U3 and R3 count on "judges from a different model family or provider where available".
   - A different provider breaks both limits, unless the owner overrides the ceiling in their own words at the time. Section 8's list of constraints checked against each other does not catch this.
   - Checked against decisions/questions/P-001-spend-ceiling.md, which allows only the plan, with an owner override.
   - Fix: either say "a different model family within the plan's service", or add the constraint to section 8 with the resolution. The resolution could be that a different provider is used only if the owner overrides, with the U3 fallback applying otherwise.

2. BLOCKING, Part 2 list rule, last bullet ("What the owner has objected to").
   - The line "no status pages now that the project is on the desk" is described in the document itself as "a standing preference" (docs/handoff/2026-11-01-chief-of-staff.md:19).
   - A portfolio-wide default does not change per project, so under the rule it belongs in the portfolio intent, not here. Remove it or move it.
   - Nearby, the LL-11 and LL-17 mentions are the Chief of Staff's own record, not the owner's words. The document labels them as such, so that is acceptable.
   - The other Part 2 quotes match decisions/questions/P-001-test-budget.md, P-001-time-and-limit.md, P-001-worst-work.md, P-001-work-repo.md, P-001-lessons-log.md, P-001-session-move-notice.md and portfolio ideas/IDEAS.md.

3. Non-blocking, Item 3 (section 3).
   - The italic instruction asks for "deliverables two levels deep, with the dependencies between them". Section 3 lists only the milestones, with no stated dependencies.
   - The order is implied by the section 2 chain: M1 to M2 to M4 to M5, with M3 beside them. Add one line saying so.
   - Milestone check: M1 to M6 each read as an achievement, with phase and why, and no ` · ` inside any why.
   - Standards: Discovery-1 to 8 and Design-1 to 6 each have a taken-on line with a plain-words why. The names and counts match the model's table (OPERATING_MODEL.md lines 151-164).

4. Non-blocking, Item 6 and section 6 against decisions/questions/P-001-value-target.md and P-001-after-the-count.md.
   - V1 and V2 and their chance thresholds (1 in 40 and 1 in 25), the "no calendar date" and the miss rule all match the ruling.
   - The starting figures match research/Q-008-memo.md: plans 2 of 44, research 5 of 19 (2 of 19 if the later-added check counts), built work 32 of 80 (27 of 75 without the five single-pass PR files), and the Critic 1 of 20.
   - The cutoffs of 5, 13 and 18, and the power of about 89, 69 and 58, are consistent with my own binomial check.
   - Q-008-source-check.md round 2 is PASS.
   - V1's wording is ambiguous. "Raised by 20 points" is stated, but "kept when chance alone would produce it at most 1 time in 40" could mean a smaller significant gain is also kept. Say which it is.
   - Section 6 still lists as a stop condition "the recount shows the instructions are not a meaningful cause". Q-008 names instructions as the primary cause in only 1 of 125 classified returns. The owner's "go on now" ruling (P-001-after-the-count.md) answered this. A short clause in section 6 would record that the stop was met and ruled.

5. Non-blocking, Item 7 against decisions/questions/P-001-open-unknowns.md.
   - U2, U3 and U4 each name a test and a fallback, and a recorded owner ruling accepts them. U1 and U5 are closed by Q-008, with figures matching the memo (21, 2 and 61 of 84, plus 41 with no findings).
   - U4's test runs in Build, one step beyond "open into Define" in the model text. The owner accepted it explicitly ("Design and Build").
   - The ruling record is second-hand, taken from the handoff. Its asked-date, 2026-11-02, sits under a 2026-11-01 session id. This is acceptable, but note it.

6. Non-blocking, section 2 (what other fields found).
   - The sentence "each is graded C (seen in search extracts from two or more independent hosts…)" is too broad. The library README (/home/user/portfolio/library/README.md) says LF-Q005-07 and LF-Q005-10 rest on a single opened source, and LF-Q005-14 has a weak second source.
   - Reword the sentence, or mark those three. The facts themselves match the library: LF-Q005-02, -03, -05a, -06a, -06b, -08, -15 and LP-Q005-09.

Items 1, 2, 4, 5 and 9 are met. Section 5's T1 matches AGENTS.md line 3, and section 9's "The owner is the user." is not contradicted anywhere. The Critic cleared both section 6 and section 7 against their rulings, and neither shows a mismatch. Fixing findings 1 and 2 would flip the verdict to PASS.

## Round 2
Verdict: PASS
Item 1: PASS
Item 2: PASS
Item 3: PASS
Item 4: PASS
Item 5: PASS
Item 6: PASS
Item 7: PASS
Item 8: PASS
Item 9: PASS
Part 2: PASS

I re-read /home/user/Model-Lab/docs/PROJECT.md. Each round-1 change is in the document as described, and I found no new problems.

1. Round-1 finding 1 (blocking, Item 8) is resolved. The section 8 constraint on line 147 now pairs judges from a different model family or provider (U3, R3) with the spend ceiling and data boundaries.
   - A different provider is used only if the owner overrides the spend ceiling in their own words.
   - Otherwise judges come from a different model family within the plan's service, and U3's fallback applies if that is not consistent enough.
   - This matches decisions/questions/P-001-spend-ceiling.md and the section 5 data boundary. Section 7 U3 (line 118) still says "or provider where available", which the section 8 line now qualifies.

2. Round-1 finding 2 (blocking, Part 2) is resolved. The last bullet (line 176) no longer carries the status-page sentence. LL-11 and LL-17 stay, and are labelled as the Chief of Staff's record, not the owner's words.

3. Round-1 finding 3 (Item 3) is resolved. A Dependencies paragraph (line 37) gives the order: M1, then M2, then M4, then M5. M3 is built beside them and lands with M5, and M6 comes at the end. It matches the section 2 chain.

4. Round-1 finding 4 is the V1 wording, which is the owner's ruled text and unchanged. It does not block readiness.
   - V1 states the 20-point target and says the test is sized to see a 20-point gain, which fixes the intended reading.
   - It matches decisions/questions/P-001-value-target.md.
   - If the owner wants a smaller significant gain kept, that is a later ruling, not a gap in the brief.
   - Non-blocking.

5. Round-1 finding 4's other half (section 6 stop condition) is resolved. The stop condition on line 103 now says it was met by the recount and ruled "go on now", citing decisions/questions/P-001-after-the-count.md.
   - It says the recount "names the instructions as the cause of 1 return". That is accurate against research/Q-008-memo.md, where 1 of 84 returns with findings has instructions as the primary cause.
   - Non-blocking observation: "1 return" is the primary-cause count. The memo also lists instructions as a contributing cause on one further return (M3C), which does not change the point.

6. Round-1 finding 6 (section 2 grading sentence) is resolved. Line 26 now marks LF-Q005-07 and LF-Q005-10 as resting on a single opened source and LF-Q005-14 as having a weak second source. This matches /home/user/portfolio/library/README.md.

7. Round-1 finding 5 (Item 7 ruling record) is unchanged and non-blocking. The ruling in decisions/questions/P-001-open-unknowns.md is second-hand, taken from the handoff. U4's test runs in Build, which the owner accepted as "Design and Build".

Sections 1, 4, 5, 6 and 7 (apart from the item above), the milestone lines and section 9 are unchanged from round 1, when I found them met.
