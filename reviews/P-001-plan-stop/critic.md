Verdict: FAIL

The Critic's check of questions/P-001-plan-stop.md (brief: docs/briefs/35-critic.md), on claude-sonnet-5-5, a different model from the question's writer, verbatim. Recorded by the orchestrator. Session session_01QBwHGMBo8kZsMCS2EvKNwd, 2026-11-04.

## Round 1
Critic check of questions/P-001-plan-stop.md. Brief: /home/user/Model-Lab/docs/briefs/35-critic.md. Read-only. I ran nothing.

Most of the card is true to its records. Three things fail it: a path in the opening paragraph, a claim the records do not make that carries the recommendation, and options that lean towards A.

1. BLOCKING. The opening has a path and jargon.
- Line 5 ends with "(triage/P-001-S-001-round-4.md)". AGENTS.md "Plain English first" bars file paths in the opening paragraph. Use a cross-reference such as "(Triage, round 4)" and keep the path in Context.
- The paragraph says "hidden marking sheets", "fingerprinted", "blind Check author" and "Reviewer who analyses the results". These are not explained. The options then call the same thing "blind held-back checks", so one thing has two names.
- It never says what the owner will see or decide. It never says whether any of it is irreversible (D ends the test).

2. BLOCKING. "Triage found the measures, size and options sound" is not in the record.
- RECOMMENDATION line 13 says this. Context bullet 2 (line 19) says Triage "found no fault in the measures, size or options". Line 5 says it found nothing wrong with them.
- Triage says only that no threshold, size, option or criterion meaning is touched by these four findings.
- Triage did not check findings 5 to 11. It did not check the round 4 table's term differences. Round 4 itself lists differences in how the deciding pass is defined (term-meaning difference (a)) and in which model plans and built work run on (findings 8 and 9).
- Triage also says finding 4 involves "AC4's glob". The card should say "not touched by these four" and then name what was left unchecked.
- This sentence carries the whole case for A over B, so it must match the record.

3. BLOCKING. The options are not put fairly, and every gap favours A. The template asks for gain, cost and what each option rules out (LL-05, LL-08).
- A's cost "about two helper sessions" appears in no record. B's "several sessions and rounds" and "delays the Build gate most" also appear in none. Either cite a record or say the cost is not estimated.
- A hides its dependency on the rule change.
  - Line 9 says A "rules out nothing".
  - Triage says that if the owner declines the pack and runner change, AC4 cannot be met and the blind checks cannot exist.
  - The rule change also covers the held-back store and fingerprint rule, a ledger entry for any change to the holdouts file, and the roster row. The card lists only two of these.
- B is shown as redoing sound work, but the card never says B still needs the same tool fixes. The tool fixes are outside the spec, so a rewrite does not remove them.
- C understates its cost. The stop rule says a narrowed plan is a new draft and starts again at round one. The card says "a new draft for the narrowed part".
- C and D do not state what they rule out. C rules out the blind held-back checks. D rules out any result for this question.
- D's "the project would go to you for a re-aim or close" has no cited record.
- A "gain" is not stated for any option.

4. Not blocking. The claims below check out against their records.
- The plan passed at round 3. The join-up review at round 4 failed it with four blocking findings. Triage confirmed findings 1 to 3 and 4 as a contradiction.
- Triage's cause is stated as one root cause across the four. That is slightly strong, because finding 4 originates in a spec written before the pack existed (stage 6). Say "mainly".
- The stop rule is quoted correctly. The four fixed options match AGENTS.md and OPERATING_MODEL §4.
- "A fourth round is allowed only on your choice" is correct, as is "comes back to you the same way".
- "Three smaller ones in the same files" matches Triage's widening to findings 5, 6 and 9. Say which findings they are, and that they were not blocking.
- Context bullet 4 matches reviews/39 finding 4. That finding says the runner cannot dispatch the new pack role, which is the same point as bullet 4's "cannot yet hand it out on their own". Context bullet 3 matches Round 3.
- Line 5 calls finding 4 "would also hide the Check author's own task sheet". That is accurate only as the spec's list applied by the runner. Triage refuted "can never pass", because J8 reads the pack's own patterns. Add "if the list were used as written".

5. Not blocking. Risk class, reversibility, default and timeout need fixing.
- Risk class (line 14) says R0 and states a reason, but the template says "computed". The question file is R0 (questions/**).
- Option A leads to changes in governance/**, which risk-paths.toml puts in R3 (owner approval). A's blast radius should say so.
- "Reversible for A to C" is shaky when A's consequence is an R3 rule change.
- DEFAULT "none" and TIMEOUT "none" are right in substance. A defaulted choice would break the stop rule's "owner's choice". The template expects a letter and hours, though. The card's parenthetical "a stop-rule choice is never defaulted" is not in the cited rule text, so cite it or reword.
- The Milestone line "M2, Design-5, Design-6" matches the template form. I did not verify those milestone names in docs/PROJECT.md. S-001's header names M2 only.

6. Not blocking. LL-46.
- Option A says "the tools learn to give the blind Check author its own list, and the Reviewer gets the records it needs".
- No record shows this works. Reviews/39 shows the runner today cannot dispatch the pack (finding 4), and the Reviewer has no path to the records.
- Phrase it as "would need" or "is proposed", not as what the tools will do.

Fixes the Chief of Staff must make before this can pass:
- Remove the path from the opening paragraph and write it in plain words.
- Replace "sound" with what Triage said and what it left unchecked.
- State each option's gain, cost and what it rules out, in parallel form.
- Cite records for the costs or drop them.
- Say A depends on the owner approving the rule change, and that B also needs it.
- Say C is a new draft from round one.
- Align the risk-class line with R3 for A's consequences.

## Six-part contract
1. Changed: nothing.
2. Why: to check the decision card cold against its cited records, the stop rule and the question form (brief 35).
3. Verified: I read questions/P-001-plan-stop.md, questions/_TEMPLATE.md, triage/P-001-S-001-round-4.md, reviews/S-001/plan.md (Rounds 3 and 4), reviews/39/reviewer.md, the Plan stop rule in /home/user/Personal-Org-Operating-Model/AGENTS.md line 38, OPERATING_MODEL.md §4 "Stop rule", Model-Lab AGENTS.md §5 and "Plain English first", and governance/risk-paths.toml. I grepped the questions for other DEFAULT lines and found no precedent for "none".
4. Undone: I did not confirm that Design-5 and Design-6 exist as milestone names. I did not read specs/S-001.md or the runner itself. I relied on the Round 4 and Triage text for what they say. I did not check the question against CI form checks.
5. Needed outside my lane: the Chief of Staff rewrites the card. This review implicates no earlier Critic check of the card. Triage implicates the Critic's earlier plan rounds, but that is not this check.
6. Open questions: (a) Should the card name the 3 smaller findings (5, 6, 9)? (b) Should the Service Desk's PACKS.toml also be in the rule change, per reviews/39 finding 5? (c) Does the owner want DEFAULT and TIMEOUT written "none" or in some other form the template allows?

Files: /home/user/Model-Lab/questions/P-001-plan-stop.md, /home/user/Model-Lab/triage/P-001-S-001-round-4.md, /home/user/Model-Lab/reviews/S-001/plan.md, /home/user/Model-Lab/reviews/39/reviewer.md, /home/user/Model-Lab/governance/risk-paths.toml.
