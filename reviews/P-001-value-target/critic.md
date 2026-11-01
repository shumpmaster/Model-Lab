Verdict: PASS

The Critic's check of the value-target question (questions/P-001-value-target.md), on a different model from its writer (brief: docs/briefs/07-critic.md), verbatim: rounds 1 to 3 (FAIL), round 4, a focused check of the round-3 fix (PASS). Recorded by the orchestrator. Session session_01QBwHGHrHnEvMNYgKDoaH8w, 2026-11-01.

## Round 1
Verdict: FAIL

I read questions/P-001-value-target.md cold. I opened the cited records: the three owner rulings, the portfolio IDEAS.md 2026-11-01 entry, Q-003 and Q-006, and OPERATING_MODEL §1, §2 and §4.

The figures check out against their records. Those are the 70–77% and ~25% power figures, 1 of 17, 2 of 12 and 15 of 50, and the "100 runs through Discovery and Design" limit. The problems are in the miss and stop rule, the date, the card parts and the plainness.

1. BLOCKING. The shared "miss" and stop rule does not fit all three options.
   - The text is "Under every option, the miss and the stop rule are… Miss on target 1: no change clears 20 points."
   - Option B measures rounds per piece, not points of pass rate, so "20 points" is the wrong yardstick for it.
   - Option C sets no number at all, so there is nothing to miss.
   - Fix: give B and C their own miss lines, or reword the shared rule so it follows whichever measure and number the owner picks.

2. BLOCKING. The date is missing and the ruling is stretched to cover it.
   - OPERATING_MODEL §4 item 6 requires a date.
   - The question says "no calendar date, as you ruled" and "You ruled there is no fixed timeline."
   - The owner's ruling (P-001-time-and-limit) was no fixed length for Discovery. Its own Note says the value target "still needs a date and a miss… set when the value target is drafted."
   - Fix: say plainly that the date is a trigger (30 pieces of each kind at a rule review), or ask the owner for a date or an explicit "no date" ruling for the target itself. Do not attribute that to the earlier ruling.

3. BLOCKING. The decision-card parts in §2 are incomplete.
   - There is no confidence level and no "what would change it" on the recommendation.
   - There is no "who has checked it" line.
   - "What happens if the owner doesn't decide" appears only implicitly, in WHY and DEFAULT.
   - Fix: add those parts, or state where they will be added after this check.

4. BLOCKING. Option A's rationale overclaims, and the recommendation is not even-handed.
   - "A kept result is believable" is not supported by Q-003. At 70–77% power, a real 20-point gain is missed about 1 time in 4.
   - Q-003 §4 says "below about 15–20 points… a coin-flip chance or less." The question's "a gain much smaller than 20 points cannot be told apart from chance" is a loose paraphrase.
   - A's text never states the miss risk or the false-keep risk, and that risk is its main cost.
   - Fix: state the detection odds and the chance of keeping a useless change in A's Cost.

5. BLOCKING. Options B and C are not put evenly.
   - C's Cost says "the 20-point limit of a 100-run test does not change with the count." That argues for A against C rather than stating C's cost.
   - B's cost is argued in A's terms and its logic is muddled: "because most work would need to be taken to a pass, which costs more runs per task."
   - A's Cost is a single short clause, while the others carry argument.
   - Fix: write each option's gain, cost and reversibility in parallel form, and keep the case for A in the RECOMMENDATION only.

6. BLOCKING. The target is stated too loosely to be checked.
   - Target 1 does not say whether the 100 runs are split across plans, research and build.
   - If 100 runs cover all three kinds, each kind has far fewer than the 50 pairs behind Q-003's power figures.
   - Target 2 says "today's figure for that kind" without saying which figure. The Q-006 counts are small (2 of 12) and M1's recount is still pending.
   - Target 2 uses 30 pieces per kind in "any project", with no word on how noisy 30 pieces are or on differing mixes. A 20-point gain on 30 pieces could be chance.
   - Fix: say which baseline is used and how large the uncertainty is.

7. Non-blocking. The Context bullet that says the owner's core goal is "to minimize the gaps…" is quoted correctly, but the body turns it into "close the gaps in how work passes between agents." That is the Chief of Staff's gloss. The owner's words are about "traditional orchestrated workflows for vibe coding, strategy." The gloss comes from PROJECT.md M1's why, not from the owner. Mark it as a paraphrase, or quote the owner's words.

8. Non-blocking. The question applies the owner's "all but lower agent usage and less of my time" correctly. But "Each status update gives the tokens used… and the number of questions put to you" is not in the owner's rulings. Only the token checkpoints are ruled (P-001-test-budget). The question count is an unrequested addition.

9. Non-blocking. The miss on target 1 says "keep only the record of each agent's brief and model (M3), put that into the model, and close the project." No owner ruling covers this outcome. The no-change ruling covers only "no change helps is acceptable." Present it as a proposal.

10. Non-blocking. The stop rules cover run exhaustion and the M1 finding. They say nothing about what happens if fewer than 30 pieces of some kind are ever checked. Add that case.

11. Non-blocking. The baseline figures come only from the "conversational path" records (Q-006). The body says "from the Service Desk's records" without that limit. Q-006 §0 item 1 also says causation cannot be read from them.

12. Non-blocking (plain English).
    - Terms left unexplained or code-like in the plain parts: "paired test", "fair test (M2)", "rule review", "killed, not tuned", "R3", "M1/M2/M3", "the model" (it means the operating model but reads like an AI model in "each agent's brief and model"), and "power".
    - The "killed, not tuned" phrase is quoted as the model's, and I could not find those exact words in OPERATING_MODEL.md. Verify it or drop the quotation marks.
    - M-codes should follow the plain milestone name, not lead it.

13. Non-blocking. The "Context" section has 8 bullets, against the ≤5-line background rule in §2. Check whether the template's Context is exempt. Consider trimming.

## Round 2
Verdict: FAIL

One new blocking finding (N1): the keep rule in Option A does not match the odds quoted for it. Of my 13 round-1 findings, 12 are resolved and 1 is partly resolved. I recomputed the new figures; they are below.

**Round-1 findings**
1. Miss and stop rule did not fit all three options: resolved. Each option now has its own Miss line, and the shared items are labelled proposals.
2. No date, and the ruling stretched to cover it: resolved. The new "date under every option" paragraph says the earlier ruling did not cover the target's date. It makes choosing an option the ruling on "no calendar date" and offers a calendar date as an alternative.
3. Card parts missing: resolved in form. Confidence, what would change it, who checked it, and "if you do not decide the project waits" are all present. The cited record (reviews/P-001-value-target/critic.md) does not exist yet. The Orchestrator should write this verdict there; as it stands the line is a forward reference.
4. Option A overclaimed "believable": resolved in intent. Detection odds and false-alarm odds are now stated, but see N1.
5. Options not even: resolved. The tilt is gone from C's cost, B's logic is cleaner, and each option has gain, cost and reversibility. B says "how well it can detect a one-round fall has not been worked out yet". That is honest, but it leaves A with figures and B without. It is non-blocking, and the recommendation says so.
6. Target too loose: partly resolved. The baseline is now "the recounted figure", 50 tasks per kind is stated, and 300 runs for three kinds is disclosed (50 × 2 × 3 = 300, correct). The target is still not stated in a form the stated odds support (N1).
7. The "gaps" gloss: resolved. The owner's words are quoted whole, including his spelling.
8. Question count in status updates: resolved. It is removed. See N3 on "remaining".
9. Miss outcome presented as a ruling: resolved. It is now under "Proposed… your ruling makes them so".
10. Fewer than 30 pieces: resolved. A six-month rule is added, labelled a proposal.
11. Baseline limited to conversation-started records: resolved. The text now says so, and that causes cannot be shown.
12. Jargon: mostly resolved. "Paired" is explained, "AI model" is spelled out, and milestones are named in words. R3 stays in the risk line. The quotation "Killed, not tuned" is still not found verbatim in OPERATING_MODEL.md. Verify it or drop the quotation marks. Non-blocking.
13. Context length: resolved. There are 5 bullets.

**Recomputed figures**
- **Paired test, "wrongly kept about 1 time in 40":** supported. Q-003 §4 uses a two-sided exact test at α = 0.05, which is 2.5% one-sided.
- **30 pieces, one-sided 5%, against the starting figures** (my own binomial calculation):

| Kind | Baseline → target | Passes needed to count as a gain | False alarm | Chance a real 20-point gain shows |
|---|---|---|---|---|
| Plans | 1/17 → about 26% | 5 or more of 30 | about 3% | about 90% |
| Research | 2/12 → about 37% | 9 or more | about 4–5% | about 80% |
| Build | 3/10 → 50% | 14 or more | about 4% | about 70% |

  - "About 7 in 10" is therefore the worst case (build). It is not correct for plans or research.
  - "About 1 in 25" is fair.
  - These odds treat the starting figures as exact. Research (2 of 12) is not, and the recount will replace them. This is stated only loosely.

**New findings**
- **N1. Blocking. The rule in Option A does not match the odds quoted for it.**
  - A keeps a change only if the pass rate is "at least 20 points" higher.
  - The odds quoted ("catches a real 20-point gain about 7 times in 10", "about 3 in 10 real 20-point gains are missed") are for a statistical significance test, not a raw 20-point cutoff.
  - If the true gain is exactly 20 points, a raw "observed at least 20" rule passes only about half the time. In real use on plans it needs 8 of 30 against the 5-of-30 significance cutoff, and power at that cutoff is about 50%.
  - The "7 in 10" and "3 in 10 missed" figures therefore do not describe the rule as written.
  - Fix: either define the keep rule as the significance test (observed gain large enough that the false-alarm chance is at most the stated 1 in 40 or 1 in 25), or restate the odds for the raw 20-point rule.
  - Q-003's power figures also rest on assumed discordance (25% and 5%). Say they are assumptions.
- **N2. Non-blocking.** Context bullet 4 cites the Chief of Staff's own calculation as the source of the 30-piece odds, with no filed record. File the calculation, or give its inputs. Say the odds differ by kind.
- **N3. Non-blocking.** "Each status update shows the tokens used and remaining, as you asked." The test-budget ruling's Note says the Chief of Staff cannot read the owner's remaining plan allowance. It can report only whether the weekly limit currently allows use and when it resets. Reword to what can actually be reported.
- **N4. Non-blocking.** The recommendation says a test of about 100 runs per kind. The 100 runs the owner allowed through Design cover only one kind. The body discloses this, but the recommendation should not read as if the allowance suffices.

*Orchestrator's note on round 2, item 12:* "Killed, not tuned." is at OPERATING_MODEL.md line 46 (§1, spine item 4), in bold with a capital K; the quotation stands.

## Round 3
Verdict: FAIL

The failure is one wording defect in the keep rule (new finding N5). It is a quick fix. N1 to N4 are resolved, and I confirmed that "Killed, not tuned" is at OPERATING_MODEL.md line 46.

**Round-2 findings**
- N1 (keep rule did not match the quoted odds): resolved in substance. The rule is now the significance rule: 1 in 40 in the test and 1 in 25 in real use. Twenty points is the gain the test is sized to see. The odds are stated for that rule, and the assumption behind the test's discordance is stated too.
  - I recomputed the real-use odds, using exact binomial one-sided 5% with n = 30.
  - Plans: 5 passes of 30, false alarm about 3%, detection about 92%. Matches.
  - Research: 10 passes, false alarm about 2%, detection about 71%. The 10-pass choice is sound, since 9 passes gives about 5.4%, over the 5% rule.
  - Build: 14 passes, false alarm about 4%, detection about 71%. Matches.
  - The "9 in 10 plans, 7 in 10 research and build" text agrees with this. So does "1 in 25", which is the largest of the false-alarm figures.
- N2 (calculation not filed): resolved. Context now gives the calculation's inputs and results per kind. One caveat is that it cites "reviews/P-001-value-target/critic.md, round 2". The Orchestrator must record my round-2 verdict there for that citation to hold. Until then it points at a file that does not exist.
- N3 (token "remaining" overpromise): resolved. The text now reports what the helpers use and says the plan's remaining allowance cannot be read, which matches the test-budget ruling's Note.
- N4 (100 runs per kind vs. the 100-run allowance): resolved. The recommendation now says all three kinds need about 300 runs, beyond the 100 allowed, and that the test budget comes to the owner at the Build gate.
- Item 12: confirmed. "Killed, not tuned" appears at OPERATING_MODEL.md line 46. The Q-003 citation was corrected to §1 item 3 and §4, which is right.

**New findings**
- N5. Blocking, one-line fix. The wording of the keep rule is inverted.
  - The test paragraph says: "larger than chance alone would produce more than 1 time in 40."
  - Option A (2) says: "more than chance would give 1 time in 25."
  - Read plainly, these say chance often produces the difference, which is the opposite of what is meant.
  - The intended meaning is that chance alone would produce a difference this large no more than 1 time in 40 (test) or 1 in 25 (real use).
  - This is the rule the owner is being asked to rule on, so it must be unambiguous in plain English.
  - Fix: reword both so the meaning is "so large that chance alone would produce it at most 1 time in 40 (or 1 in 25)."
- N6. Non-blocking. The Option A real-use rule is judged against "the recounted figure". The quoted odds use today's figures, and the text says the recount will move them. That is acceptable, but the card could add that the real-use odds will be restated once the recount is in.

## Round 4 (focused)
Verdict: PASS

I have no git tool here. So I re-read the whole file and compared it with the round-3 text I read. The only differences are the two keep-rule sentences (N5) and the restated-odds clause (N6). I found nothing else changed.

1. N5 (inverted keep-rule wording): resolved, non-blocking now.
   - The "How the test works" paragraph now reads "so large that chance alone would produce it at most 1 time in 40".
   - Option A (2) now reads "by so much that chance alone would produce it at most 1 time in 25".
   - Both now say what the rule means, and the figures match the recomputed odds: 3%, 2% and 4% false alarms, which are all at most 1 in 25.
2. N6 (odds to be restated after the recount): resolved. Option A (2) now says the real-use odds "treat today's figures as exact; they will be restated once the recount is in".
3. Nothing else changed.
   - Options B and C, the date paragraph and the proposed miss and stop rules are the same.
   - The recommendation, the check line, the risk line and the Context bullets are the same.
   - My earlier checks therefore still hold, including "Killed, not tuned" at OPERATING_MODEL.md line 46.
   - The Context citation to my round-2 recomputation now resolves, since you say rounds 1–3 are recorded in reviews/P-001-value-target/critic.md.
4. New findings: none.
