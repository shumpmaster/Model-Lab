Verdict: FAIL

*The Critic's neutrality check (D-055) of research questions Q-015 and Q-016 for P-002: round 1 (FAIL); brief 196. Each round a fresh session on a different model from the questions' writer, started by the Chief of Staff (session_01QBwHGNSLmSrYQgS6BPjV8p), 2026-11-09. Recorded verbatim by the Orchestrator from each helper's return; each round's own verdict line is recorded as "The round's verdict was …" (LL-68). The verdict above is the latest round's.*

## Round 1 (brief 196)

The round's verdict was FAIL.

Two blocking findings, one in each question. The rest are non-blocking. I did not read the barred folders. For the library I read README.md lines 1-185 and then searched the rest of it for the Q-010 to Q-014 rows; I did not open individual entries.

**Q-015**

1. BLOCKING, line 5, the maker-reported methods are not put evenly. The question says "Include methods reported only by their makers, marked as such; a method's being new or untested is not a reason to leave it out."
   - Claims get two asks: "what was claimed and what was measured".
   - Weaknesses get one narrow ask: "any case where it was found no better than a simpler setup, or worse".
   - The "new or untested" clause guards only against leaving methods out, so the whole tilt is toward inclusion.
   - A maker's weaknesses are mostly not "no better than a simpler setup". They are cost, failure modes and incidents, limits of the conditions tested, whether anyone outside the maker repeated it, whether it is still in use, and what the maker sells.
   - "Marked as such" asks for source kind, but the question text never asks for the source's stake. Only the depth line mentions it.
   - The only comparator is a "simpler setup". People alone or a single agent are not named, though "simpler setup" may cover the single-agent case.
   - To fix this, ask for failures, costs and limits for each method as fully as claims, and ask for the source's stake and any outside check.

2. Non-blocking, line 9, "Which ways ... are candidates to try on the organisation's own work". This frames the answer as adoption candidates. "The organisation" is also undefined for a Researcher who knows nothing of the project. Lines 13-15 repeat the candidate-for-trial framing. Line 15 does balance it with "set aside" and "no better ... recorded".

3. Non-blocking, line 5, wording that may presume a result.
   - "organised, run and improved in practice" presumes these systems get improved.
   - "how such systems are changed over time" overlaps "improved" and the library's prompt and harness entries.

4. Non-blocking gaps an expert would expect:
   - Cost and latency (the library has Q-009-F10-1 on token use, but the question does not ask for it).
   - Security and permission models (prompt injection and tool access).
   - Accountability, audit trail and incident handling.
   - Comparison with human-only teams.
   - Survivorship (whether the practice is still in use).
   - Independent versus self-run evaluation.
   - The scope is seven areas "even thinly" at depth 3, so it is large. The Chief of Staff should accept that knowingly.

5. Non-blocking, line 7, the library exclusion. It names Q-002, Q-009 and Q-010 to Q-014.
   - Q-010 to Q-014 cover extrapolation, replication, trial power, change control and de-adoption. They bear little on this question and add noise.
   - The more relevant entries are not named:
     - handoffs: Q-005 (I-PASS, SBAR) and Q-007 (handoff patterns, drift, compaction);
     - agent checking and judges: Q-002-F-g, F-h, F-l and F-m, and the Q-003 judge entries;
     - the project's own pipeline records (Q-006, Q-008).
   - Without them a Researcher may re-research these.

6. Form is fine: all three sections, topics and depth are present, as in Q-012. Plainness is good apart from item 2.

**Q-016**

7. BLOCKING, line 15, "becomes a candidate for the value target". This is project jargon, and it tells the Researcher that a target exists for the share of work, which is the owner's lean you asked me to check for. The Researcher cannot know what "value target" means. Line 11 also frames the decision as how the organisation measures "the share of its work its agents carry". Name no target; speak of "a measure to use" instead.

8. Non-blocking, line 5, published share-of-work figures. The question asks for "what each figure counts and who reported it", but not the reporter's stake or whether anyone outside checked it. Such figures mostly come from firms that sell or run AI. This is the same maker-reporting issue as Q-015, and the two questions treat it differently. Ask for the source's kind and stake as Q-015 does, and for any gap between the figure and an outside check.

9. Non-blocking, line 5, "how much of a body of work AI agents carry" and "the share of work". These presume that a single share is meaningful. The question does ask about gaming and misreading, and about trade-offs, which helps. It does not ask how "work", the denominator, is defined for mixed human and AI work, or how a person's and an agent's contribution are told apart. Those are the main sources of misreading.

10. Non-blocking gaps:
   - Measures of calibration, meaning whether trust matches how often the work is right.
   - Acceptance and survival of AI output as a proxy, for example code retained or merged.
   - Self-report versus telemetry as collection methods.
   - Time-saved and value measures versus share measures.
   - Lag between the work and when defects show up.
   - Measures for non-code work such as plans and documents. The question mentions "documents" but gives no sign that measures for them are known.
   - The cost of measuring.
   - Comparison against a no-AI baseline.

11. Non-blocking, line 7, the library exclusion. It omits relevant entries the Researcher would otherwise repeat:
   - Q-005-LF-Q005-14: alert override rates of 49% to 96%.
   - Q-006 to Q-008: the project's own return and first-pass counts.
   - The Q-009 trust and rework entries are covered, because Q-009 is named. These include METR, DORA, Veracode, F2-8 on Claude Code PRs, and F10-6/F10-7 on reviewer load and perceived speed.

12. Form is fine. The topics ("ai-share-of-work", "human-trust") may not match the library's topic words exactly. Check them against the library's topic list.

**Overlap between the two**
- Q-015's "how agents' work is checked" and "how failures are found" brush against Q-016's review, override and defect measures. They are separable: Q-015 asks about methods of running and checking, Q-016 about measures of share, trust and durability.
- Neither question says which owns the review rate and the override rate. As Q-012 did, add a sentence saying that Q-016 owns measuring them and Q-015 owns the methods of checking.
- Both ask for the same kind of per-source stake information, but only Q-015 asks for it in words. Align them.

**Blocking items to fix before dispatch:** item 1 (Q-015 line 5) and item 7 (Q-016 line 15). Resubmit for a recheck once they are fixed.
