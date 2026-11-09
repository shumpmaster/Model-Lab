Verdict: FAIL

*The Critic's check of P-002's problem statement and what other fields found (docs/projects/P-002.md section 2) and its pre-mortem (section 7): round 1 (FAIL), round 2 (FAIL); briefs 193 and 194. Each round a fresh session on a different model from the plan's writer, started by the Chief of Staff (session_01QBwHGNSLmSrYQgS6BPjV8p), 2026-11-09. Recorded verbatim by the Orchestrator from each helper's return; each round's own verdict line is recorded as "The round's verdict was …" (LL-68). The verdict above is the latest round's.*

## Round 1 (brief 193)

The round's verdict was FAIL.

I checked section 2 (problem and "What other fields found") and the section 7 pre-mortem of /home/user/Model-Lab/docs/projects/P-002.md. I compared them with the library entries (/home/user/portfolio/library/facts/ and patterns/), research/Q-010-memo.md, Q-011-memo.md and Q-013-memo.md, decisions/questions/P-002-target.md and P-002-groundwork-shortlist.md, and the form of docs/PROJECT.md. I did not read docs/handoff/ or sessions/.

Findings (B = blocking, N = non-blocking):

1. (B) Section 2, "What other fields found". There is no transfer check on any borrowed principle. The knowledge method (§6) and P-001's passed form (docs/PROJECT.md lines 26-32) require, for each finding, the conditions it depended on and whether they hold for agents, with those judgements labelled as opinion. P-002 has only "may mean here". Examples:
   - The manufacturing-firms study (Q-011-11) comes from a different field, with innovation output as its measure.
   - The Android and Stack Overflow figure (Q-011-10) concerns copied code.
   - The living-review search test (Q-012-15) found trials that "did not alter the results".
   - The Choosing Wisely, Zalando and process-safety audit points (Q-014-12, -13, -18, -4) come from medicine, a company's self-report and chemical plants.
   - Q-014-P22 and Q-012-P1 each say transfer to a small AI-build organisation is untested, and the plan carries that no further.
   - Nothing marks any statement as fact, estimate or opinion either.

2. (B) Section 2, problem statement. The factual claims in it are unsourced and unmarked.
   - "Most are reported by people who sell, promote or simply like them, few are tested by anyone independent" has no citation.
   - "Waiting for a method to be fully proven means adopting it after it has stopped being new" is the owner's view ("faith", P-002-target.md) or the Chief of Staff's reading, written as fact. It needs an opinion mark, or the owner's quote.
   - "a claimed gain can shrink or vanish" is only supported later, by 26% conformity (a secondary citation) and one preprint.

3. (B) Section 2, problem statement, last sentence. It does not state a problem; it states the solution: "find promising methods early, try each ... in a small trial ..., keep what helps, and retire what does not." That is the screening pipeline. A neutral problem statement would give the gap between what the person wants and what they can get or check today. The trial, keep and retire design belongs in the strategy chain.

4. (B) Pre-mortem R2 against R5 and R9. The answers pull against each other, and the plan does not say so.
   - R2 trials only methods "promising a large gain", and reports smaller gains as "not shown".
   - R5 retires by default unless a method "has shown value".
   - With 10 to 20 runs, most trials will end "not shown", so most promising leads would be retired. That is exactly R9, "nothing was ever tried".
   - R9's answer ("go to trial on the owner's choice; the bar is set at the value-target card") does not say what happens to a not-shown result.
   - The owner's "faith" aim (P-002-target.md) is the very thing this tension undermines.

5. (B) Pre-mortem, missing risks an expert would expect.
   - Cost. The time and money ceiling is "Set at Design gate", so there is no risk row for screeners, automated research prompts and trials costing more than they return, or for the owner's review time beyond proposal cards. R6 covers only proposal volume.
   - Measurement. There is no row for the measure itself failing: there is no baseline, and agents may grade their own trials. P-001's own evidence (docs/PROJECT.md line 32) notes that model judges favour their own output. The "share of work done by agents" is also admitted at line 61 to be unresearched, and "strategy ideation" has no named way to measure success at all. R1 and R3 lean on an undefined "measure".
   - Trial harm. There is no row for a trial on the owner's live work breaking that work, or for a trial being contaminated by a model change during the trial (the confound R4 names only for kept methods).
   - Order of work. There is no row for the dependency on the prompt engine going first. R11 covers only overlap of tests.

6. (N) Pre-mortem, early signs. Several are late results, not early signs.
   - R1 ("kept methods do not move the measure") and R4 ("then the measure falls") are outcomes. The measure also has no definition until the value-target card.
   - R10's sign ("helps in reports from large organisations but not in our trial") is the failure itself.
   - R10's answer ("the trial decides; no checklist") meets the risk only after a trial is spent, which is the cost it is meant to avoid.
   - R9's source cites "four source-check rounds on two memos", which is a process fact, not evidence that a bar is too high. Q-012-source-check.md shows 14 mentions of rounds, and I did not confirm "four" for it.

7. (N) Claim stronger than its source.
   - "Claims shrink when someone else tests them". The sources are 26% of external replications "conform to the original" (a secondary citation, grade C, 2014 paper not opened) and a preprint abstract on prompting techniques. Neither measures shrinkage.
   - "Looking outside helps up to a point". Q-011-11 is an association ("related to"), not a cause. Read as written, it tells the owner looking helps.
   - "Findings about AI models go stale quickly". Q-012-3 is drift of hosted models, not decay of practice findings (its own status line says so). Q-012-4 is weak (C), abstract only, one task type (Python functions), and "not load-bearing", yet it is the source for R4. The plan omits that Qwen models kept benefiting.
   - "Cheap alerts miss a lot" and R8 ("missed what mattered"). Q-012-15 is one review, and the four missed trials "did not alter the results", so "what mattered" was not shown to be lost. The plan leaves that out. Q-012-17's overlap figure is also not a miss rate.

8. (N) Stakes and who-says-it are missing.
   - Q-014-13 is a news report of insurer data, with the lead author at the insurer.
   - Q-014-4 is typed opinion and comes from a consultancy.
   - Q-011-19 involves a security vendor's blog.
   - Q-012-13 supports cost of ongoing scanning in living reviews, not "feeds go unread", and is cited in R6 for it.
   - The Zalando line is correctly marked self-report.

9. (N) Q-013-memo.md points (section 2, small trials). The plan drops the memo's own hedge: the 10-run and 20-run figures are at 80% power, under the memo's assumptions. "A plan changed mid-trial" is not what the memo says; it concerns repeated looks and early stopping. The Q-010 claim ("No conditions checklist was found ... in any field") is faithful. The Q-011 "no study compares" line is faithful.

10. (N) "May mean here" lines. They mostly read as plan decisions, not readings to be tested: "treat a reported gain as a ceiling", "retirement by default", "the owner's 'no data out' rule stands". Item 3 also puts a ruling inside a reading. P-001's form labelled these as the Researcher's own opinions; this plan should do the same.

11. (N) Fit with Part 2. The problem statement matches the owner's aims in P-002-target.md: share of work carried, trust and success, promising methods, and not mistaking share for quality. It correctly does not use the "90%" figure. It does not name strategy ideation or coding, or the feeds, screeners and adoption into the model and desk that the owner described. That is fine for an industry-free statement, but item 3 shows part of that pipeline leaking in.

12. (N) Plainness on a phone.
    - The problem's final sentence runs about 100 words.
    - Jargon should be unpacked or cut: "standard deviation of the run-to-run differences", "inverted U", "context-aware analysis", "threat-intelligence feeds", "paired trial".
    - The table is wide: five columns, long cells.
    - R7's "Input reader" is not explained.

Not a finding: the placeholder that the strategy chain follows once the value target is ruled is stated openly, and I did not count it against the plan.

## Round 2 (brief 194)

The round's verdict was FAIL.

Round 2 check of /home/user/Model-Lab/docs/projects/P-002.md: the problem statement, "What other fields found" (section 2), and the pre-mortem (section 7). I compared them with the library entries (Q-011-4, Q-012-4, Q-012-17, Q-014-12, Q-014-13, pattern Q-014-P22), the Q-010, Q-011, Q-012, Q-013 and Q-014 memos, decisions/questions/P-002-target.md, the shortlist, and docs/PROJECT.md. One finding blocks (item 1). The rest do not.

Round 1 findings:
1. No transfer check (blocking): answered. Each point now has Conditions, Transfer and May mean here, with fact, estimate or opinion marked on the evidence lines. The Q-014-P22 and Q-012-P1 untested-transfer caveats are carried.
2. Unsourced claims in the problem statement (blocking): partly answered. See item 1 below.
3. The problem statement stated the solution (blocking): answered. It now gives the gap and three limits, with no trial, keep or retire design.
4. R2, R5 and R9 pulled against each other (blocking): answered, with one remaining weakness (item 4 below).
5. Missing risks (blocking): answered. R12 (measure and judge), R13 (cost), R14 (trial harm) and R15 (order) were added. One gap remains (item 6 below).
6. Early signs were late outcomes (non-blocking): mostly answered. R1, R4 and R10 now have observable signs, and the R10 answer now meets its risk.
7. Claims stronger than their sources (non-blocking): answered. "Fewer held" now carries its 26% and preprint base. Q-011-11 is marked as an association. Q-012-3 is marked as model drift, not practice decay. Q-012-4 is marked weak, abstract only, one task type, with the Qwen contrast. Q-012-15 carries "did not alter the results". Q-012-17 is marked as overlap, not a miss rate.
8. Stakes and who-says-it (non-blocking): answered. The insurer, the vendor blog, the Zalando self-report and the consultancy opinion are named. R6 now cites Q-014-18.
9. Q-013 hedge (non-blocking): answered. 80% power and the assumptions are stated, and the text now concerns repeated looks. This matches the memo.
10. "May mean here" read as decisions (non-blocking): partly answered. See item 2 below.
11. Fit with Part 2 (non-blocking): fine.
12. Plainness (non-blocking): partly answered. See item 7 below.

Judgement 1: The problem statement uses no industry's terms ("one person", "delegated workers"). It states a problem, not a solution. It fits P-002-target.md: share of work carried, justified trust, promising methods and not mistaking share for quality. It correctly does not use the 90% figure.

Judgement 2: The section 2 figures match their sources: 26% and 82%; 2,707 firms; 15.4% and 97.9%; 46.8% and 0.52%; the Q-012-3 and Q-012-4 quotes; 1 of 4 alerts; 2.5% to 4.0%; 2 of 7 services; the Q-014-12 quote; Zalando as a self-report; the Q-013 power figures; the Q-010 and Q-011 absence claims. I did not re-open Q-014-4, Q-014-18 or Q-012-15 beyond the memo lines; they matched the memo.

Findings:
1. (Blocking) Problem statement, first limit ("Which ways of running the team would help is unknown"). It is still unsourced and unmarked.
   - "The ways change quickly" cites nothing.
   - "Few have been tested by anyone independent of the people reporting them" cites nothing. Q-011-input says there is no systematic rate for vendor or practitioner claims, so this is the Chief of Staff's reading, not a fact.
   - "Where claims were re-tested, fewer held (Q-011-1, Q-011-4)" generalises from one secondary-cited software-engineering mapping and one preprint abstract. The section 2 bullet hedges these correctly, but the statement does not.
   - Round 1 item 2 was blocking. Mark these as opinion or estimate, or add a source and the hedge used in the section 2 bullet.
2. (Non-blocking) Several "May mean here" lines still read as plan decisions: "check outside material before it runs", "each kept method needs a set review", "use more than one source", "a few chosen sources". The header calls them opinion, which helps. Phrasing them as readings would finish round 1 item 10.
3. (Non-blocking) R7 cites shortlist item 6 for more than it says. Item 6 holds only "Yes, no data out". "Read only as data, by the one role allowed to read the web" and "outside code, prompts and skills are checked before use" are the model's and the plan's, not the owner's. Cite the model rule or label them proposals.
4. (Non-blocking) R9 names the R2/R5 tension but resolves nothing. It hands the "not shown" outcome (stop, or keep on trial with a review date) to the owner at the value-target card, with no stated default. That fits the owner's "faith" line, and the early sign is observable. The risk is named, not met.
5. (Non-blocking) R15 says screening that does not touch instructions "can start first". That sits uneasily with the owner's order, "first the prompting idea, then the cutting edge idea" (Part 2). Say plainly that the owner decides it at the Design gate.
6. (Non-blocking) One missing risk remains: integration into the operating model and desk. The owner's purpose is "a pipeline to integrating those back into the operating model and ultimately service desk", and the desk is "never updated automatically". Nothing covers adopted methods failing to land, or several adopted methods interacting. The Q-013 memo says few-run trials cannot see interactions.
7. (Non-blocking) Plainness on a phone is better but not done.
   - Prose still has "paired comparison", "80% power", "standard deviation of the run-to-run differences" and "curvilinearly (taking an inverted U-shape)".
   - "Threat-indicator feeds" is jargon.
   - The pre-mortem is still a five-column table with long cells.
   - R13's source reads "the same record", which is unclear.
   - Plain glosses would help, for example "10 runs only show a gain about as big as the usual run-to-run swing".
