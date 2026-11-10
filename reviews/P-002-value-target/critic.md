Verdict: PASS

*The Critic on questions/P-002-value-target.md, the value-target question for the screening (P-002): round 1 (FAIL), round 2 (FAIL), round 3 (PASS); briefs 238, 239 and 240. Each round a fresh session on a different model from the card's writer, started by the Chief of Staff (session_01QBwHGKirN166RhxQTHuAt9), 2026-11-10. Recorded verbatim by the Orchestrator from the helper's return; the round's own verdict line is recorded as "The round's verdict was …" (LL-68). The verdict above is the latest round's. After round 3, its findings 1, 2, 3, 6 (who records the draw and works out the result), 8, 9, 10, 12 (why not being blind matters) and 13 were applied as wording; findings 4, 5, 7 and 11 were not acted on, and the rest of finding 6 and finding 12 stay open. The card the Critic read is the content of commit 451dd08 (the brief names 969bdc1, the same content before its committer was rewritten).*

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

## Round 2 (brief 239)

The round's verdict was FAIL.

Card checked: /home/user/ml-critic-239/questions/P-002-value-target.md, round 2, read cold. Three findings are blocking and eleven are non-blocking. I hold no command tool, so I ran nothing: I read the three scripts line by line and re-did the card's arithmetic by hand from the printed output. Every Context source was opened.

Self-implication flag (D-050): round 1 was a Critic check. No round 1 "holds" is overturned. Finding 2 below raises trial length, which round 1 rated non-blocking (its item 18), to part of a blocking finding, because the redraft's design multiplies the pieces a trial needs. Finding 3 is a gap round 1's item 3 could have named and did not.

## What holds

- **Two-look code.** `two_look` in /home/user/ml-critic-239/intake/P-002-value-target-odds-2026-11-10.md does what the card says:
  - keep at look 1 if the one-sided Fisher value is at or under the line;
  - otherwise go on only if the method arm has strictly fewer touches (`elif x<y`);
  - then test all 60 per arm together at the same line.
  - The line search keeps the largest line whose no-effect keep rate is at or under the target, and `twolook2.py` re-checks the fixed lines 0.097 and 0.022 at both starting shares.
- **Rounding.** Every card figure matches the output:

  | Card line | Card says | Output |
  |---|---|---|
  | 40 | 7 and 4 in 10; under 1 in 10; "half or more" | 0.71, 0.42; 0.078, 0.061; 0.49, 0.57 |
  | 41 | 4 and 2 in 10; 1 in 70 to 80; a quarter to two-fifths | 0.41, 0.19; 0.014, 0.013; 0.23, 0.38 |
  | 53 | 8 and 4 in 10; 9 and 7 in 10; 3 to 7 in 10 go on | 0.77, 0.43; 0.92, 0.70; 0.27 to 0.71 |
  | 38 | 1 in 7 | 1 - 0.922 x 0.927 = 0.145 |
  | 26 | 13 points | 1.96 x sqrt(0.25/60) = 0.127 |

- **Mistakes per 10 (line 43).** My sums from the two-look output, missed plus useless kept:

  | Share that really helps | Start | At 1 in 10 | At 1 in 40 |
  |---|---|---|---|
  | 1 in 10 | 1 in 2 | 0.08 + 0.84 = 0.92 | 0.23 + 0.22 = 0.45 |
  | 1 in 10 | 3 in 10 | 0.30 + 0.89 = 1.19 | 0.57 + 0.19 = 0.76 |
  | half | 1 in 2 | 0.40 + 0.47 = 0.87 | 1.15 + 0.12 = 1.27 |
  | half | 3 in 10 | 1.50 + 0.50 = 2.00 | 2.85 + 0.11 = 2.96 |

  The card's "about 1", "half to four-fifths", "1 to 2" and "1 to 3" are within rounding, though 0.76 is nearer three-quarters. See finding 1 for what the rounding hides.
- **Q-017 sentences (lines 9 to 12, 76, 93 to 95).** All match /home/user/ml-critic-239/research/Q-017-memo.md: 447; 94.2, 98.9 and 97.8%; the 86 bot merges; no "Revert" subject with its caveat; repair against follow-on not told apart; 66 + 85 + 12 = 163. Exceptions are in findings 2 and 9.
- **Owner's words and rulings.** Both quotes on line 7 (with the question mark), "Both equally", "no data out", stay separate and "Set at Design gate" match the two decisions records. The rule on line 5 is quoted exactly from the knowledge method.
- **Other sources.** 2 of 44, 5 of 19, 32 of 80, the 1-in-40 line and the 30 real-use pieces match docs/PROJECT.md section 6. Q-016-5 says what line 29 says. The model citations say what Context claims.
- **Form.** Template fields, Milestone line and Context are present; no default and no timeout is right for a value target. The opening paragraph has no paths or ids and leads with the departure (LL-08, S-026).

## Round 1 findings: answered or not

| # | Round 1 finding | Status |
|---|---|---|
| 1 | Two-look claim unsupported | Answered: designed, computed, moved to part 3 A, with what is compared and why it is not a re-run. Residual in finding 4. |
| 2 | Before-and-after design | Answered for trials by the coin toss. The new design's costs are not stated (finding 2); the target itself is still before-and-after (finding 5). |
| 3 | "Holds up" undefined | Partly: the test, the 30-day judging, the starting figures, the independent marker and the owner's sample are all there. How often the guard misses real harm is not (finding 3). |
| 4 | Part 1 C's starting figures | Answered: C is rewritten and the unknown starting figure is said plainly. |
| 5 | Departure not stated as LL-08 asks | Answered: first line, rule quoted, "someone else" restored, the part 3 C combination flagged. Residual in finding 10. |
| 6 | Trade shown from one side | Largely answered: the keep line is now a choice with both costs shown. The recommendation misreads them (finding 1). |
| 7 | Target not judgeable at its date | Mostly answered: latest 60 pieces, all kinds together, chance line, 13 points. Which repositories is still unsaid (findings 2 and 5). |
| 8 | "Most often quoted outside"; commits | Answered. |
| 9 | "No change was undone outright" | Answered. |
| 10 | Weak patterns stated as findings | Answered: removed. |
| 11 | The 90% and the 50% estimate | Answered. |
| 12 | Dropped question mark | Answered. |
| 13 | Prompt-engine overlap | Answered (line 81). |
| 14 | R4, R5, R12 plans not carried | Answered for those three. R14 is not carried (finding 8). |
| 15 | What must be built | Partly: phase, spec and owner are given; repositories and who knows the arm are not (finding 2). |
| 16 | Part 3 C against "Killed, not tuned" | Answered. |
| 17 | Reversibility | Answered. |
| 18 | Plan line, trial length, owner time | Partly: the plan line is given for the recommended set only; trial length is "not yet known" (finding 2); owner time is given. |
| 19 | Critic record did not exist | Answered: it exists, and currently records FAIL. |
| 20 | Plainness on a phone | Partly (finding 12). |

## Blocking

1. **Lines 43 and 47 (part 2): the recommendation's reason is not what the card's own figures show.**
   - Line 47 says B makes fewer mistakes "if most methods tried do not help", and to pick A "if you expect most screened methods to help". That puts the switch at one half.
   - On the intake's two-look figures the switch is much lower. The two lines tie when about 3 in 10 methods really help at a start of 1 in 2 (0.15π = 0.069(1-π), π = 0.32), and about 2 in 10 at a start of 3 in 10 (0.27π = 0.078(1-π), π = 0.22).
   - So if 3 or 4 in 10 help, most still do not help, yet A makes fewer mistakes. At half helping A wins at both starts (0.87 against 1.27; 2.00 against 2.96). The card's "1 to 2 against 1 to 3" hides that at the low end.
   - "As the research suggests" leans on the 9-in-10 figure. /home/user/ml-critic-239/research/Q-013-memo.md §1 says that figure counts "bad ideas and buggy implementation" together, that reading it as a no-effect share "is therefore an assumption", and that it comes from web-scale programmes. Line 43 drops the first two caveats and says "the research found" for one B-grade source.
   - "More than half of ideas fail" sits in the range where A wins or ties, so it does not support B.
   - "Part 3's option A recovers much of what it misses" is counted twice: the line 43 comparison already includes part 3 A.
   - The owner's "Both equally" was about adopting a *harmful* method. Line 43 counts *useless* ones kept; the harmful case is finding 3.

2. **Lines 17, 53, 75 to 76 and 80: the coin-toss design's costs and limits are not stated; only its gain is.**
   - **Size in calendar terms.** A trial now needs 60 new pieces of one kind, or 120 with the second look, plus 30 days, after a 60-piece starting count, with one method per kind at a time. Line 76 says how many pieces were of one kind "is not counted".
   - **The memo does count by kind.** Q-017 §1 "By kind" gives pull requests touching each kind over the whole extract (about seven weeks, marked supported in part):

     | Kind | Service-Desk | Model-Lab | POOM |
     |---|---|---|---|
     | built | 90 | 8 | 26 |
     | plan or spec | 100 | 19 | 31 |
     | research | 29 | 21 | 5 |

     All research in three repositories is 55, fewer than one trial. The card instead shows 163 pull requests of every kind in nine days, which flatters the pace.
   - **Date and stop rule cannot be weighed.** The owner is asked to accept "six months" and "the first five trials" without seeing that few trials may finish by then.
   - **Which repositories.** The card never says where pieces come from (round 1 items 7 and 15). Model-Lab alone has 8 built-work pull requests.
   - **Per-piece switching.** The design needs a method that can be turned on and off piece by piece, by the same agents in the same weeks. One that changes rules or session structure cannot be. One that leaks to the "without" pieces shrinks the difference and reads as "not shown".
   - **Not blind.** The measure is the owner stepping in, and conversation questions are hand-logged by the Chief of Staff. Both know which pieces carry the method. Line 20 says only that some "may be missed". The 5-piece sample is unlabelled; the touch count is not.
   - **Arm sizes.** A plain coin toss does not give 30 each way; the card does not say how the arms are filled.
   - **Second-look timing.** Line 53 drops a method that "does not hold up" at the first look, but hold-up is judged 30 days after the last piece. The card does not say whether the second 30 wait for that.

3. **Lines 18, 38 and 79: the hold-up guard's odds are shown from one side.**
   - The card gives how often the guard wrongly fails a harmless method (1 in 7). It never gives how often it passes a method that really makes work worse.
   - It is the same test on 30 pieces each way at 1 in 10, so the intake's own figures apply by swapping the arms. A method that doubles a fault share from 25 to 50 in 100 is caught about 7 times in 10. One that doubles it from 15 to 30 is caught about 4 in 10, so it passes about 6 in 10. At lower shares it is caught less often still.
   - The reopen share has no starting figure. Line 18 admits the weakness only for plans' first-check floor.
   - The owner's sample is 5 pieces across both arms, which can show little.
   - "Adopting a harmful one" is half of "Both equally" and is pre-mortem R3. Every option's target ends "and the work holds up", so the owner will read it as assurance.
   - Under two looks the guard is applied more than once, so the 1-in-7 false-fail figure is also too low for part 3 A. The intake computes it for one look, with the two checks assumed independent; the card does not say so.

## Non-blocking

4. **Line 53: "still kept no more often than the line you chose" is checked at two starting shares only.** The intake says "at either starting share shown". At a start of 3 in 10 the figure is 0.099 against 0.100. One-look Fisher holds at every share; a shared two-look line does not. The starting share is unknown, so the card should say the line is fixed once it is counted, or that the claim holds at the two shares tested.

5. **Lines 26, 28 and 72: the target is itself a before-and-after comparison, and its odds are not shown.**
   - The latest 60 pieces are set against the starting 60, six months apart, all kinds mixed. Model changes, the prompt engine's changes, the mix of kinds and drift in hand-logging all count as the screening. The card's title promises "how we will know the screening worked".
   - PROJECT.md's V2 sets a precedent for a before-and-after target, so this is a limit to state, not a bar.
   - If the share truly halves, the counted share lands at or under half the counted start only about half the time, before the chance test. The intake's 50-per-arm figures put the chance test at 1 in 40 at 0.67 and 0.35.
   - "The work holds up" is defined for a trial's two arms, not for the target's two periods.

6. **Line 80: "the first five trials all end with the method dropped" will often trigger by chance.** Under the recommended set, with half of methods real at a start of 3 in 10, a trial keeps about 0.5 x 0.43 x 6/7 = 0.19, so five drops in a row happen about 1 time in 3. With 1 in 10 real it is about 2 times in 3. The card does not say so.

7. **Line 76: "the first nine days of November".** Line 9 says "to 9 November", and the memo's reference time is the start of the 9th. This is small.

8. **Line 100 and line 17: R14's plan is not carried.** R14 says "Trials run on copies or on work that can be redone". The design puts the method on half of all new real pieces of a kind. Line 79 stops a trial only after it "breaks work you rely on".

9. **Lines 11 and 82: "is not recorded" and "recorded nowhere" are stronger than the memo.**
   - The memo marks stepping-in as supported in part: owner-identity commits in 48/312, 6/85 and 16/50 pull requests, and question-file counts. It does not mark it as absent.
   - The memo says the owner's time is not in the extract, which is narrower than "nowhere".
   - Round 1 was right that these cannot be the starting figure; "not reliably recorded" would match the memo.
   - Line 10's figures cover all ordinary commits, including 439 outside the 447 pull requests; the heading implies otherwise.

10. **Line 5: "as your ruling on the screening's aim already said".** The sentence about a lighter standard being a proposal to the model is in the Chief of Staff's "How it is carried out" section of /home/user/ml-critic-239/decisions/questions/P-002-target.md, not in the owner's words.

11. **Line 51: "not the same as 'does not help' (Q-013)".** The memo supports the inference (low power) but does not say this. The sentence is the Chief of Staff's "may mean here" in /home/user/ml-critic-239/docs/projects/P-002.md section 2.

12. **Plainness on a phone (round 1 item 20, partly answered).**
    - "Leans the right way" is now defined, and the undefined "line written before it starts" is gone.
    - Line 43 is the hardest sentence on the card ("about 1 mistake at 1 in 10 against between half and four-fifths of one at 1 in 40"); a small table would carry it.
    - Lines 18 and 53 run to about 130 and 200 words. The background is far past the five lines D-019 sets.
    - The card asks for four part rulings and eight proposals in one sitting.

13. **Line 72: the plan line is given for the recommended set only.** Round 1 item 18 asked for it under each option; B's and C's would differ in kind.

14. **Line 20: "the agent that owns that work" is unnamed, and "built in Design" is not explained.** The card does not say whether building in Design needs the owner's leave, as the prompt engine's test runs did.

## Files read

- /home/user/ml-critic-239/questions/P-002-value-target.md
- /home/user/ml-critic-239/questions/_TEMPLATE.md
- /home/user/ml-critic-239/reviews/P-002-value-target/critic.md
- /home/user/ml-critic-239/intake/P-002-value-target-odds-2026-11-10.md
- /home/user/ml-critic-239/research/Q-017-memo.md
- /home/user/ml-critic-239/research/Q-013-memo.md
- /home/user/ml-critic-239/docs/projects/P-002.md (sections 2 and 7)
- /home/user/ml-critic-239/docs/PROJECT.md (section 6)
- /home/user/ml-critic-239/docs/LESSONS.md (LL-08)
- /home/user/ml-critic-239/AGENTS.md (§5)
- /home/user/ml-critic-239/decisions/questions/P-002-target.md
- /home/user/ml-critic-239/decisions/questions/P-002-groundwork-shortlist.md
- /home/user/ml-critic-239/decisions/questions/P-002-q017-decide.md
- /home/user/portfolio/library/facts/Q-016-5.md
- /home/user/Personal-Org-Operating-Model/OPERATING_MODEL.md (§1, §2, definition of ready, knowledge method, experiment playbook)

## Round 3 (brief 240)

The round's verdict was PASS.

Card checked: /home/user/ml-critic-240/questions/P-002-value-target.md, round 3, read cold. No finding is blocking; thirteen are non-blocking. All three round 2 blocking findings are answered.

I hold no command tool, so I ran nothing. I read the five scripts line by line and re-did the card's arithmetic by hand from the printed output. Nobody other than the writer has run the scripts. Every Context source was opened and says what its line claims.

Self-implication flag (D-050): rounds 1 and 2 were Critic checks. No earlier "holds" is overturned. Findings 1 and 2 below are gaps that round 2 could have named and did not (its finding 5 gave "about half" for the target, at the same two starting shares).

## What holds

- **Scripts.**
  - `two_look` keeps at look 1 when the Fisher value is at or under the line, goes on only when the method arm has strictly fewer touches, and tests all 60 per arm at the same line.
  - `holdup.py` calls the test on the fault-free shares, so "worse" is the direction tested. Its 30-per-arm figures (0.42, 0.71) equal the touch test's figures for the same shares, as symmetry requires.
  - `two_look_guard_false` is a true upper bound: it treats every trial as going on.
  - `target_met` requires both `2*x<=y` and the Fisher line, as the card's V1 for option A is worded.
  - Five drops: I re-did all eight rows by hand from the two-look figures with the 0.80 hold-up pass rate, and all match.
- **Rounding.** Every figure on the card matches the output.

  | Card line | Card says | Output |
  |---|---|---|
  | 21 | harm caught 3 to 7 in 10 (5 to 9 at 60 each way) | 0.30 to 0.71 (0.49 to 0.93) |
  | 21 | harmless method fails 1 in 7; up to 1 in 5 with a second look | 0.145; 0.20 |
  | 32 | 13 points | 0.127 |
  | 34 | 4 to 5 in 10 | 0.41 to 0.54 |
  | 46 to 47 | at most about 1 in 10; about 1 in 40 or less | 0.093 to 0.099; 0.021 to 0.024 |
  | 68 | 8 and 4, against 4 and 2; 9 and 7, against 7 and 4; 3 to 7 in 10 go on | 0.77, 0.43, 0.41, 0.19; 0.92, 0.70, 0.71, 0.42; 0.27 to 0.71 |
  | 90 | 1 to 4 in 10; 5 to 8 in 10 | 0.07 to 0.37; 0.47 to 0.77 |

- **Mistakes per 10 (lines 51 to 56).** My sums from the fixed-line two-look output, missed plus useless kept:

  | Share that really helps | Start | A: 1 in 10 | B: 1 in 40 |
  |---|---|---|---|
  | 1 in 10 | 1 in 2 | 0.08 + 0.84 = 0.92 | 0.23 + 0.22 = 0.45 |
  | 1 in 10 | 3 in 10 | 0.30 + 0.89 = 1.19 | 0.57 + 0.19 = 0.76 |
  | 5 in 10 | 1 in 2 | 0.40 + 0.47 = 0.87 | 1.15 + 0.12 = 1.27 |
  | 5 in 10 | 3 in 10 | 1.50 + 0.50 = 2.00 | 2.85 + 0.11 = 2.96 |

  The card's eight cells are these, rounded. The tie at "about 2 to 3 in 10" is right (0.32 and 0.22), and so is its direction.
- **Q-017 sentences (lines 9 to 12, 22; Context 106 to 108).** All match /home/user/ml-critic-240/research/Q-017-memo.md.
  - 94.2, 98.9 and 97.8% of non-merge commits, with the identity caveat.
  - 15.4, 7.1 and 32.0% of pull requests, now "not reliably recorded".
  - No "Revert" subject, with its caveat; fault not judged.
  - Owner's time and conversation decisions are not in the extract.
  - By kind: 29 + 21 + 5 = 55, 100 + 19 + 31 = 150, 90 + 8 + 26 = 124.
  - September to 8 November, with 273 of the 447 in October.
- **Other sources.**
  - Both owner quotes on line 7 are exact.
  - The rule on line 5 is quoted exactly, and its framing is now attributed to the record's note, not to the owner.
  - "Both equally", "Yes, no data out", stay separate and "Set at Design gate" match answers 3, 6, 7 and 8.
  - 2 of 44, the 1-in-40 line and the 30 real-use pieces match docs/PROJECT.md section 6.
  - Q-016-5 says what line 35 says.
  - Line 58 carries Q-013's caveats: bad ideas and faulty set-ups counted together, a web-scale figure, transfer unknown.
  - "Killed, not tuned" and "No re-running for a better answer" are in the model as cited.
  - The thirteen risks listed on line 114 exist, and their plans are carried.
- **Form.** The template's fields, the Milestone line and Context are present. No default and no timeout is right for a value target. The departure leads the WHY with the rule quoted (LL-08), and the opening holds no paths or ids (S-026).

## Round 2 findings: answered or not

| # | Round 2 finding | Status |
|---|---|---|
| 1 | Part 2 recommendation misread the figures | Answered. The recommendation is gone, the table and tie point are correct, the caveats are restored, and harm is routed to the guard. No double count remains. See finding 4. |
| 2 | Coin-toss costs and limits not stated | Answered. Pace by kind, the three repositories, per-piece switching, leakage, not blind, shuffled draws for 30 each way, and second-look timing are all on the card (lines 15, 17, 22 to 24, 68). Residuals in findings 5 to 7. |
| 3 | Hold-up guard shown from one side | Answered (line 21). Residuals in findings 2 and 8. |
| 4 | Two-look claim checked at two shares only | Answered (line 68: "fixed once the starting share is counted", "checked at starting shares of 1 in 2 and 3 in 10"). |
| 5 | Target is before-and-after; odds not shown | Mostly answered (lines 32, 34). "The work holding up" is still undefined for the target's two periods (finding 3). |
| 6 | Five drops in a row by chance | Answered (line 90); see finding 9. |
| 7 | "Nine days of November" | Answered: "to 8 November" on lines 9 and 22. |
| 8 | R14 not carried | Answered: usual checks, the owner's merge, "can be undone", the stop on broken work, and a model change voiding a trial. |
| 9 | "Not recorded" stronger than the memo | Answered. |
| 10 | "As your ruling already said" | Answered. |
| 11 | "Not shown" credited to Q-013 | Answered: now "the plan's reading of the research, section 2". |
| 12 | Plainness on a phone | Partly (finding 12). |
| 13 | Plan line for the recommended set only | Answered: each option of part 1 has its line. |
| 14 | Who builds the log, and when | Answered (line 26). |

Round 1 items that round 2 left partly answered:

| # | Round 1 item | Status |
|---|---|---|
| 3 | "Holds up" undefined as a test | Answered. |
| 7 | Target not judgeable at its date | Answered, except the hold-up clause (finding 3). |
| 15 | What must be built | Answered. |
| 18 | Plan line, trial length, owner time | Answered. |
| 20 | Plainness on a phone | Partly (finding 12). |

## Judgement on the points the brief names

- **Coin-toss design.** It is sound. With shuffled 30-and-30 assignment before work starts, Fisher's test is the randomisation test, so the false-keep figures do not depend on pieces being independent; only the power figures do. Its costs and limits are now stated.
- **Two-look rule.** The code and every figure are correct as read.
- **Part 2.** Offering no recommendation is honest. The tie point depends on a share no record gives, and the facts are shown evenly.
- **Hold-up guard.** It is now shown from both sides.
- **Trial length and the 12-month date.** They are consistent with the memo's counts.

## Non-blocking

1. **Lines 34 and 40 (part 1): "works from any starting figure" and "about 4 to 5 times in 10" hold only at the two starts computed.**
   - The intake's round 3 computes the target at starts of 1 in 2 and 3 in 10 only. The card gives the figure without naming them, though line 68 does name them for its own figures.
   - At lower starts the chance falls. By my hand arithmetic (exact Fisher, not run): with a starting count of 6 of 60, the lowest the stop line on line 91 lets through, the target is met only at 1 or fewer of 60 on the 1-in-10 line, and only at 0 of 60 on the 1-in-40 line. If the share truly halves, that happens about 2 times in 10 and 1 time in 20.
   - Line 91 itself calls a low start "little room to gain".
   - The recommendation's other reason, "it measures your involvement", is equally true of B and C.
   - It is non-blocking because line 34 already says a miss is weak evidence and the start is unknown, C is offered for exactly this case, and line 38 keeps the part open until the first trial, after the starting count.

2. **Lines 51 to 56 and 68: the keep odds and the mistakes table leave out the hold-up guard, and the card does not say so.**
   - The intake says "the card's keep odds are before that". Line 21 says a harmless method fails the guard 1 time in 7, up to 1 in 5.
   - So a useful halving kept "about 8 and 4 times in 10" is nearer 6 to 7 and 3 to 4. The table's "useful ones missed" is too low and its "useless ones kept" slightly too high.
   - The tie point does not move, because the guard scales both lines alike.
   - Line 90's five-drops figures do include the guard, so the card is not consistent with itself.

3. **Lines 34 to 36: "with the work holding up" is still undefined for the target.** Line 18 defines holding up between a trial's two arms. The V1 lines apply it to two periods months apart. This is round 2 finding 5, last point, unanswered.

4. **Line 62: part 2 has no recommendation, where D-019 asks for one with its confidence and what would change it.** I judge the purpose met: the line says what the choice turns on, and the question cannot default. Line 58's closing sentence, "Part 4's option A would let more untested methods in", points toward B without saying so. It is a fair fact, but it is the only pointer in the part.

5. **Line 23: methods that cannot be switched piece by piece are "left to each trial's plan".** The card does not say on what line such a method is kept, or that the weaker plan comes to the owner. A before-and-after trial, which round 1 finding 2 was about, could return here.

6. **Lines 15 and 17: a piece is a merged pull request, so work abandoned or never merged is unseen.**
   - A method whose pieces are sent back and dropped pays no penalty.
   - A piece's kind is settled by what the merged pull request changes, yet the draw is made before work starts. The memo flags 263 of 447 pull requests as touching more than one kind.
   - The card does not say who makes and records the draw, or who computes a trial's result. D-047 asks for analysis by someone who did not run it.

7. **Lines 92 and 93: "a change of AI model" is undefined, and its cost is not stated.** Trials run for weeks to months, and roles run on different models. The card does not say which change voids a trial, how often that is likely, or whether a "re-check" of a kept method is a fresh trial.

8. **Line 21: the guard's examples are fault shares of 10 to 25 in 100, which the card does not say.**
   - The only fault shares on record are far higher: 42 of 44, 14 of 19 and 48 of 80 pieces fail the first check, and those cannot double.
   - The reopen share has no starting figure, and the card does not say so.
   - "Up to 1 in 5" uses fault shares of 60% and 20%. With the two worst shares printed (0.118 and 0.115) it is 0.22.
   - The two checks are assumed independent, in the intake only.

9. **Line 90: the five-drops figures assume part 3's option A, under "Proposed under every option".** With one look (option B), drops in a row are more likely. By hand, at 1 in 40, a start of 3 in 10 and half of methods real, it is about 6 in 10 against the 4 shown. The low end, 0.07, is under 1 in 10.

10. **Line 78 and line 5: "It goes to the operating model as a proposal at the end of the cycle" is ambiguous.** "It" could be the method or the lighter standard. The card does not say plainly whether choosing A lets one-source trials start in this project before the model's rule is changed.

11. **Line 88: the target is checked again "at each screening review after that".** "Screening review" is not defined. The card does not say how a later check sits with the ruling on a miss in line 89.

12. **Plainness on a phone (round 1 item 20, round 2 finding 12; still partly answered).**
    - The table answers round 2's hardest sentence.
    - The background before the options is now about twenty lines, against the five D-019 sets.
    - Lines 18, 21, 68 and 94 are each well over 100 words.
    - The owner is asked for four part rulings and eight proposals in one sitting.
    - Line 24 says who knows which pieces carry the method, but not why that matters: agents could ask less on those pieces.

13. **Lines 97 and 113: nobody but the writer has run the odds scripts, and the body does not say the figures are the writer's own.**
    - The Critic read the code in all three rounds and ran nothing.
    - The intake's round 3 records that the first version of the harm script printed 0.00 for every row before it was corrected.
    - The figures I could cross-check by symmetry and by hand agree. An independent run before the Design gate would close the gap.
    - Line 35 says who said the 90% and what it counts "are not recorded"; the ruling record says "not checked here".

## Files read

- /home/user/ml-critic-240/questions/P-002-value-target.md
- /home/user/ml-critic-240/questions/_TEMPLATE.md
- /home/user/ml-critic-240/reviews/P-002-value-target/critic.md
- /home/user/ml-critic-240/intake/P-002-value-target-odds-2026-11-10.md
- /home/user/ml-critic-240/research/Q-017-memo.md
- /home/user/ml-critic-240/research/Q-013-memo.md
- /home/user/ml-critic-240/docs/projects/P-002.md (sections 2 and 7)
- /home/user/ml-critic-240/docs/PROJECT.md (section 6)
- /home/user/ml-critic-240/docs/LESSONS.md (LL-08)
- /home/user/ml-critic-240/AGENTS.md (§5)
- /home/user/ml-critic-240/decisions/questions/P-002-target.md
- /home/user/ml-critic-240/decisions/questions/P-002-groundwork-shortlist.md
- /home/user/ml-critic-240/decisions/questions/P-002-q017-decide.md
- /home/user/portfolio/library/facts/Q-016-5.md
- /home/user/Personal-Org-Operating-Model/OPERATING_MODEL.md (§1, §2, definition of ready, stop rule, knowledge method, experiment playbook)
