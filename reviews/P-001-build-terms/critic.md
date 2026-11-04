Verdict: PASS

# The Critic on M2's reworded "done when" and the project document's lines restated to the Build-gate terms, verbatim

*Brief 66 (docs/briefs/66-critic.md) for round 1 and brief 68 (docs/briefs/68-critic.md) for round 2; each a fresh session on a different model from the lines' writer. Recorded verbatim by the Orchestrator, 2026-11-04. The first line is the latest round's verdict; in round 2's contract its "- Verdict: PASS." is written "- (Verdict) PASS.", since the verdict check allows that word only at the start of a line.*

## Round 1

Verdict: FAIL

M2's reworded line and V1 pass. The one thing that fails is a "past tasks" line the restatement missed (finding 4a). That line is a one-line fix and does not touch M2 or V1.

All file paths below are in the fixed copy, /tmp/claude-0/-home-user/a9cd8a0a-147c-550f-94b8-72427d1045fd/scratchpad/fix-terms/. I had no shell, so I could not run `git show`. I judged every line from the current text of docs/PROJECT.md against the records. I did not diff old against new, so I cannot say which seven lines changed.

**Findings**

1. M2 (docs/PROJECT.md line 57): pass, not blocking.
   - Form: it reads `<name> (M2) · done when … · phase: Design · why: …`, as the form requires.
   - Achievement: "A fair test of the changes is ready" names a state reached, not an action.
   - "Done when": it matches specs/S-001.md, open question 2, word for word.
   - Why: still true with new work. "The owner accepted that no change may be the result" is in the no-change ruling. "The research found that about 100 paired runs can only show large gains" is a statement of what the research found, so the move to new work does not falsify it. "The test must be set up before it is run" still holds.

2. V1 (line 108): pass, not blocking. It is identical to the plan's proposed text in specs/S-001.md, open question 1, including the 1-in-40 clause, the "sized to see a 20-point gain" clause and the "checked when testing ends" clause.

3. The other changed lines are true of their records and consistent with the document. Not blocking.
   - Line 117, testing budget: "size A, 60 pieces of each kind, built work first, then plans, then research, 732 runs and about 132 million tokens" matches decisions/questions/P-001-build-gate.md, line 1. It also matches option A in the S-001 table (line 96: 60 pairs each, 732 runs, 132 million). The terms ruling carries term 2 as "one kind after another" in that order.
   - Line 153, "Paired test": the definition (each new piece done or checked both ways, from the same starting point, over the same period) is consistent with V1. The claim that past tasks could not be replayed faithfully is supported by reviews/E-001/reviewer.md, which states that the registration's own outcome for every kind is the fallback.
   - Line 157: "the fair test's 732 runs" is consistent with line 117, and the "about 100 runs through Design" ruling is kept separate.
   - Lines 22 and 108: "new work, both with and without the change from the same starting point over the same period" is consistent with M2 and V1.
   - Line 66 (M4) and line 99 (spend ceiling) are consistent with the Build gate ruling.
   - "About 300 runs" no longer appears anywhere in the document.

4. Unchanged lines that still state the plan in terms of past tasks:
   - 4a. Line 158, section 8, "Constraints checked against each other": "a kind with too few past tasks to test is reported as such, not dropped". This states the plan, not what Discovery said. It contradicts V1, M2 and the line 153 definition, and the terms ruling said to restate all such lines. Blocking. Fix: "too few new pieces".
   - 4b. Line 134, the pre-mortem preamble, defines a "paired test" as running "the same past tasks with and without a change and compares them task by task". That is a glossary definition, and it now disagrees with line 153's definition of the same term. The pre-mortem's risk text itself is Discovery-time and can stay as it is. Not blocking, but I recommend aligning the definition with line 153, or marking the sentence as the definition as it stood at Discovery.
   - 4c. Line 31 (section 2, research "may mean here"): "ideally on the same tasks, if past tasks can be replayed faithfully, which is not yet known". It reports the research at the time, but "not yet known" is now stale. Not blocking. Consider adding "(since found not to be, reviews/E-001/reviewer.md)".
   - 4d. Line 129 (U2 row) is a Discovery-time unknown with its fallback, and the fallback is what the plan now does. Line 146 (R9) is the same. Both are fine as at-the-time statements, so I name them without a finding.

**Six-part contract**
1. Outcome: FAIL, for finding 4a only. The M2 line and V1 may stand once 4a is fixed; the Critic's check of the M2 line passes.
2. Evidence: docs/PROJECT.md lines 22, 31, 57, 99, 108, 117, 129, 134, 146, 153, 157 and 158; specs/S-001.md lines 90-99 and 334-335; decisions/questions/P-001-build-gate.md line 1; decisions/questions/P-001-build-gate-terms.md; reviews/E-001/reviewer.md line 5.
3. Checked: the M2 form, whether M2 is an achievement, and that M2's "done when" and V1 match the plan text exactly. Also the budget figures, the document's own consistency, and a search for "past tasks" and "300" across the document.
4. Not checked: the old-versus-new diff (no shell). The 1-in-40 threshold against decisions/questions/P-001-value-target.md. The other S-001 sections beyond the cited table and open questions.
5. Risks: none beyond finding 4a. Left alone, it leaves the project document saying the test uses past tasks.
6. Next: the Chief of Staff fixes line 158 and, if it chooses, 4b and 4c. Those edits touch no milestone line, so M2 does not need a further Critic check for them.

## Round 2

Verdict: PASS

All three findings are resolved and no blocking finding remains. I read docs/PROJECT.md and reviews/E-001/reviewer.md in the fixed copy, and ran a search for "past tasks", "300 runs" and "about 300".

**Findings**

1. 4a, line 158: resolved, not blocking. The line now reads "a kind with too few new pieces to test is reported as such, not dropped". That is consistent with V1, M2 and the line 153 definition.

2. 4b, line 134: resolved, not blocking. The pre-mortem's "paired test" definition now carries "(the pre-mortem's definition as it stood at Discovery; the test now pairs new work, section 8, "Paired test")". This marks the old wording as Discovery-time and points to line 153. That is true of the document and accurate.

3. 4c, line 31: resolved, not blocking. The line keeps "not yet known (Q-003 §7)" as the research's wording at the time. It adds "the replay check since found they cannot (reviews/E-001/reviewer.md)".
   - The reviewer record supports this. Plans, built work and research all go to the fallback.
   - Plans fail the faithful grade and the template grade.
   - Built work fails both grades, and HD1 fails F4 and F7.
   - Research has a web-free stratum of 0 passing.
   - "Cannot" compresses "the thresholds were not met, so the fallback applies". A purist might want "could not, at the registered thresholds". I consider this acceptable and it needs no change.

4. Line 153 ("Paired test"): true of its record. It says new work is done or checked with and without the change, and that past tasks could not be replayed faithfully (reviews/E-001/reviewer.md). The reviewer's record gives that outcome for each kind. "About 300 runs" appears nowhere in the document.

5. The lines that still say "past tasks" are all at-the-time statements:
   - Line 129 (U2 row): it states the unknown and the fallback of comparing new work with and without the change.
   - Line 146 (R9): it names that same fallback.
   - Line 141 (R4): it describes the fitting risk and says nothing of the plan's design.
   - No line states the plan as using past tasks. Not blocking.

6. M2 and V1: unchanged and not re-checked, as instructed. Line 108 (V1) still says "paired test on new work".

**Six-part contract**
- (Verdict) PASS.
- Findings: the six above, none blocking.
- Evidence: the PROJECT.md lines 31, 108, 129, 134, 141, 146, 153 and 158, and the reviewer.md outcome sections for plans, built work and research.
- Scope: the three changed lines and the whole-document search for plan statements built on past tasks or about 300 runs.
- Not checked: M2 and V1 (unchanged, passed at round 1), and anything outside docs/PROJECT.md and reviews/E-001/reviewer.md.
- Self-implication: none. This round checks only changes made after my round 1, and no finding implicates my earlier check beyond the 4a miss that I already recorded.
