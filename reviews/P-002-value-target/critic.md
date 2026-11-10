Verdict: FAIL

*The Critic on questions/P-002-value-target.md, the value-target question for the screening (P-002): round 1 (FAIL); brief 238. A fresh session on a different model from the card's writer, started by the Chief of Staff (session_01QBwHGKirN166RhxQTHuAt9), 2026-11-10. Recorded verbatim by the Orchestrator from the helper's return; the round's own verdict line is recorded as "The round's verdict was …" (LL-68). The verdict above is the latest round's. The card the Critic read is the content of commit 451dd08 (the brief names 969bdc1, the same content before its committer was rewritten).*

## Round 1 (brief 238)

The round's verdict was FAIL.

Card checked: /home/user/ml-critic-238/questions/P-002-value-target.md (round 1, read cold). Seven findings are blocking and thirteen are non-blocking. No earlier check of mine is implicated.

I could not run the odds script, since I hold no command tool. I read it line by line and checked the four quoted n=30 figures by a continuity-corrected normal approximation instead. Every Context source was opened.

## What holds

- **Odds script and rounding.** The logic in /home/user/ml-critic-238/intake/P-002-value-target-odds-2026-11-10.md is sound: one-sided Fisher, every outcome pair enumerated, false keep computed with both arms at the starting share. My approximation gives 0.68, 0.42, 0.41 and 0.19 against the output's 0.71, 0.42, 0.41 and 0.19. The card's "about 7 in 10", "about 4 in 10", "about 4 and 2 in 10" and "fewer than 1 time in 10" (0.078 and 0.061) are fair roundings.
- **Q-017 figures.** 447 pull requests, 94.2/98.9/97.8%, 48/312, 6/85, 16/50, the 86 bot merges and 202/312 ("about 2 in 3") all match the memo's opening paragraph, §2 and §4.
- **Owner's rulings.** "Both equally", "Yes, no data out", stay separate, and "Set at Design gate" match answers 3, 6, 7 and 8 of decisions/questions/P-002-groundwork-shortlist.md. The route of the evidence standard to this card matches decisions/questions/P-002-target.md.
- **Other sources.** The first-time pass figures and the 1-in-40 line match docs/PROJECT.md section 6. R2 to R17 exist as described in docs/projects/P-002.md section 7. The model citations (§1 item 13, §2, §4 item 6, D-032, D-047) say what the card claims.
- **Form.** The template's fields, the Milestone line and Context are present. No default and no timeout is correct for a value target.

## Blocking

1. **Line 31 (part 2 A): the "1 in 10 across both looks" claim is unsupported, and its cost is left out.**
   - The intake record computes single-look odds only. No two-look rule is designed or computed anywhere.
   - For the false-keep chance to stay at 1 in 10 over two looks, the first look's line must be stricter than 1 in 10. Fisher's slack (0.078 and 0.061 actual) covers only part of that.
   - So under A, the odds on line 29 (7 and 4 in 10) do not apply to the first trial, and the card does not say so.
   - "Without lowering the bar" and the recommendation on line 35 rest on this unshown claim.
   - The card also does not say what the second trial is compared against: the original "before" pieces, or the first trial's pieces.
   - On the no-re-run rule: a two-stage trial registered whole before the first stage is one registration and fits D-047 and "pre-declared sequential rule" (Q-013). But line 32 presents B as what "the operating model's experiment rules ask", which leaves A reading as outside them. The card never says in plain words why A is not a re-run.

2. **Line 29: "a method that does nothing is wrongly kept fewer than 1 time in 10" holds for chance alone, and the design is before-and-after.**
   - The comparison is against "the pieces done just before it". Anything else that changes between the two periods counts as the method: the kind of work, a rule change, the prompt engine's changes, the new log itself.
   - research/Q-013-memo.md, which the card cites, puts "single-period or AB designs" outside what few-run trials can show. It says a basic AB design makes causal inference "difficult" and that serial correlation cuts power.
   - The script assumes independent pieces. The card states none of this as a cost.
   - The prompt engine's V1 uses a paired with-and-without test for this reason.

3. **Lines 15 and 29: the quoted odds leave out the "holds up" condition, which is undefined as a test.**
   - A method is kept only if the touch test clears and both hold-up shares are "no lower" and "no higher".
   - Read literally on 30 pieces, a method that changes nothing fails each raw comparison close to half the time. The real chance of keeping a good method is then well below 7 or 4 in 10.
   - Line 49 hints at a margin ("beyond a line written before it starts"), but line 15 does not.
   - The reopen check needs 30 days after each piece, yet line 47 says a trial is judged "when its written size is done". Those cannot both hold.
   - No starting figure exists for the reopen share. The first-time pass figures (plans 2 of 44, research 5 of 19, built 32 of 80) are in Context but never shown to the owner; "no lower than 5 in 100" for plans guards almost nothing.
   - The reopen mark is made "by whoever makes the later change", a self-report. Pre-mortem R12 asks for judges independent of the worker.

4. **Line 23 (part 1 C): the starting figures and the gain are not what the records hold for the measure as defined.**
   - Line 15 defines a piece as excluding question-only and records-only pull requests. The 85, 93 and 68 in 100 are shares of all 447 pull requests (264/312, 79/85, 34/50).
   - Q-017 §2 shows all 147 owner-name commits are single-file commits, almost all adding records or answer files (desk: 72 records, 46 question or answer files, 1 built file). On defined pieces the figure is unknown and probably near 100, so "a starting figure exists today" is not true.
   - "No new log" is not true either: "holds up" applies under every option and its second check needs a new log.
   - "Which the records show are most of your involvement" is not in Q-017. §3 and §5 say the records cannot show questions asked or answered.
   - The stop line "fewer than 1 piece in 10 needs you" (line 50) would trigger at once for this repository under C.
   - C is put more weakly and less accurately than A and B, which leans the choice.

5. **Lines 5 and 39 (part 3): the departure is not stated as LL-08 asks.**
   - LL-08 asks for it in the first line, quoting the rule. It sits in the last sentence of the WHY paragraph and in the fourth sentence of option A, as a paraphrase.
   - The rule's words are "Every load-bearing fact cites a source someone else has opened and confirmed; two independent sources for load-bearing facts".
   - It is hedged ("if you read the rule as covering methods to be tried"). The owner's own ruling record already frames it as "a lighter standard than the model's two-source rule would be a proposal to the model".
   - "One source someone has opened" also drops "someone else".
   - "Keeping it rests only on our own trial" is false if the owner picks part 2 C, where a method stays with no shown gain. The parts are ruled separately and the card does not flag the combination.

6. **Lines 29, 35 and 42: the trade the owner is ruling is shown from one side.**
   - The card says 1 in 40 "misses more real gains". It does not say what 1 in 10 means for the methods kept.
   - Q-013 makes the point with a worked example: where most tried changes are not real, a large share of results that clear the line are false, and real ones are overstated below 0.5 power.
   - On the card's own figures, if 1 method in 10 tried is real, about half of those kept would do nothing (my arithmetic: 0.1×0.42 against 0.9×0.061, and 0.1×0.71 against 0.9×0.078).
   - Part 3 A raises the share of hype tried, which makes this worse. The parts interact and the card says neither.
   - The 1-in-10 line is derived from "Both equally" by the writer and put "under every option" with no alternative. It is part of the value target, so it should be offered as a choice or marked as a proposal the owner may change, as the date is.

7. **Lines 21 to 22 and 47: the target has no stated way of being judged at its date.**
   - "That share halved" is checked "six months after the first trial starts", but the card does not say over which pieces, how many, of which kinds, in which repositories, or whether by raw count or beyond chance.
   - A 30-piece starting figure is uncertain by roughly 18 points either way.
   - The prompt engine's V2 states all of this; a value target must state its measure and target so that it can be counted.
   - The card also does not say whether the starting 30 pieces and each trial's pieces are of one kind of work or mixed, though line 51 implies trials run per kind.

## Non-blocking

8. **Line 10:** "the measure most often quoted outside" has no source. Q-016-P24 says outside figures count characters, lines and functions, not commits. "Commits" should read non-merge commits; counting all commits gives 83.2, 90.2 and 91.0 in 100, so the desk is under 90.
9. **Line 12:** "No change was undone outright" overstates the memo, which says no commit subject starts "Revert" and a revert worded otherwise is not found. "Mostly ordinary follow-on work, not repairs" is unsupported and contradicts the same sentence's "the records cannot tell the two apart".
10. **Line 13:** the two library patterns are weak (C) opinion patterns marked "not load-bearing". The card states them as findings with no grade.
11. **Line 22 (part 1 B):** "the 90% you quoted counts code written" cites no record. research/Q-016-memo.md gives "unit not stated", "many teams, not uniformly", and an outside estimate of about 50% (library fact Q-016-5). The owner's ruling record says the figure "is not used as a fact". An owner weighing B should see the 50% estimate.
12. **Line 7:** the "faith" quote drops the owner's closing question mark, which the record has.
13. **Prompt-engine overlap (lines 15 and 51):** "holds up" uses the first-time pass rate, which is the prompt engine's own measure (V1, V2), and the body never says so. Using it as a guard, not a target, does not by itself break "stay separate". But line 51 bars only methods that change agents' instructions; any screened method can move first-time pass rates during the prompt engine's V2 count of 30 pieces "in any project". "Is testing" does not clearly cover that count.
14. **Line 69:** the card says it answers R5 and R12, but it does not carry their plans.
    - R5's plan gives every kept method a review date and a way out. Only part 2 C has a review date.
    - R12's plan includes "the owner's sample" and independent judges. Neither is in the card.
    - R4's re-check of kept methods on a model change is absent; line 49 covers only a change during a trial.
15. **What must be built:** the card says a log is needed, but not who builds it, in which repositories, under what spec, or how it starts "now" during Discovery without disturbing the prompt engine's work. Hand-logging of touches by agents who know a trial is running is unblinded; a method can cut touches simply by agents asking less.
16. **Line 33 (part 2 C):** it keeps a method that missed its registered line. The card does not set that against "Killed, not tuned" or pre-mortem R1.
17. **Reversibility:** every option says "yes" with nothing more. Changing the measure or the line after trials have run discards their starting figures, and changing a target after seeing results runs against "Predeclare before computing".
18. **Missing from the target:**
    - The line as it would be written in section 6 (`V1: <measure>, <target>, <date>`) under each option.
    - How long 30 pieces takes, so the owner can see a trial's length.
    - Any estimate of the owner's time per trial, though the ceilings are rightly left to the Design gate.
19. **Line 54:** it names reviews/P-002-value-target/critic.md, which did not exist at this check.
20. **Plainness on a phone:**
    - The background runs to five dense paragraphs against the "≤ 5 lines" the card standard sets. Lines 15, 29, 31 and 39 are each over 100 words.
    - The card asks for three part rulings plus six proposals in one sitting.
    - "Leans the right way" and "a line written before it starts" are undefined.
    - "About 4 in 10 if 3 in 10 do (at 1 in 40: about 4 and 2 in 10)" is hard to parse.
    - The opening paragraph holds no paths or ids and leads with the departure, which is right.

## Files read

- /home/user/ml-critic-238/questions/P-002-value-target.md
- /home/user/ml-critic-238/questions/_TEMPLATE.md
- /home/user/ml-critic-238/intake/P-002-value-target-odds-2026-11-10.md
- /home/user/ml-critic-238/research/Q-017-memo.md
- /home/user/ml-critic-238/research/Q-013-memo.md
- /home/user/ml-critic-238/research/Q-016-memo.md (searched for the 90% figure only)
- /home/user/ml-critic-238/docs/projects/P-002.md (sections 2 and 7)
- /home/user/ml-critic-238/docs/PROJECT.md (section 6)
- /home/user/ml-critic-238/docs/LESSONS.md (LL-08)
- /home/user/ml-critic-238/AGENTS.md (§5)
- /home/user/ml-critic-238/decisions/questions/P-002-target.md
- /home/user/ml-critic-238/decisions/questions/P-002-groundwork-shortlist.md
- /home/user/ml-critic-238/decisions/questions/P-002-q017-decide.md
- /home/user/portfolio/library/patterns/Q-016-P24.md
- /home/user/portfolio/library/patterns/Q-016-P25.md
- /home/user/portfolio/library/facts/Q-016-5.md (title and status lines, by search)
- /home/user/Personal-Org-Operating-Model/OPERATING_MODEL.md (§1, §2, §4, §6)
