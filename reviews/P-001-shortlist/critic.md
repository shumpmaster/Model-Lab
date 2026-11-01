Verdict: PASS

The Critic's cold reading of the owner questions drafted from Q-001's shortlist, verbatim: round 1 (FAIL, seven files), round 2 on the rework (FAIL), round 3 confirmation (PASS). Recorded by the orchestrator. Session: session_01QBwHGJH9m3A4Ray7WpHzBo, 2026-11-01.

## Round 1
Verdict: FAIL

**Summary.** Two cards are not ready to put to the owner. The session-records card treats the Chief of Staff's own words as the owner's. It also leaves out that the owner has already endorsed recording each brief. The worst-work card tells the owner what frustrates them, sets a default for it, and its background and context argue for the recommended option. Four more cards have smaller fairness or sourcing faults. Only the test-budget card has its default and reversibility right on a spending question, and its wording still needs fixing. Skipping the map's question 1 is fair on substance, with two caveats noted at the end.

---

### P-001-session-records.md: FAIL (blocking)
1. **The Context line misattributes its source.** "The owner's earlier account: briefs are written by hand per dispatch…" is wrong. IDEAS.md (evidence list, last bullet) attributes it to "the Chief of Staff's own account in the session, 2026-10-30". Change to: "The Chief of Staff's own account (2026-10-30): briefs are written by hand for each dispatch and nothing records which led to clean first passes (source: portfolio ideas/IDEAS.md, 'Evidence from the Service Desk's launch')."
2. **The question is partly answered by the owner's recorded words.** IDEAS.md records the proposal put to the owner: "Record each agent brief and role card against how its work went…". The owner replied: "I think that should probably be in there too." So the owner has already said briefs should be recorded. Option C ("No — … measure only the automatic pipeline") contradicts that and should be dropped. The card should then ask only where the recording applies (A, the whole model, or B, this project first). Add a Context line quoting the owner's words. Retitle the card: "Should recording briefs and the model for conversation-started agents start in this project only, or across the model now?"
3. **WHY: "which is how most of Service-Desk's later work ran"** is unsupported. The map says the shares are unknown (memo C3: "unknown (shares)"; C2: "may lack"). Change to: "which is how much of Service-Desk's later work ran; how much is not yet known."
4. **WHY: "adds a few minutes per dispatch"** has no source. Either cite one or write "adds some work per dispatch (not yet measured)."

### P-001-worst-work.md: FAIL (blocking)
1. **The card recommends and defaults the owner's own feelings.** A recommendation of what "frustrates you most", which becomes the owner's answer after 168 hours, records a feeling the owner never expressed. Either keep the title and set "RECOMMENDATION: none — only you can say" and "DEFAULT: none", or reframe the title as "Which kind of agent work should the project look at first?" and keep a recommendation.
2. **WHY argues for option A.** "The launch evidence points at specs and briefs: the launch plan failed three reviews, traced to the planner being briefed without the gate's rules." Remove that sentence from WHY, which should give background, not a case for one option.
3. **The evidence is selective.**
   - The triage's root cause has two parts: first "The route… was put to the owner before the plan was sized, first unfairly", then the Definer briefing (M3C/_triage-r3-critic-verbatim.md:20-21). The card cites only the second.
   - IDEAS.md's evidence list also records that the Critic caught "several [owner questions] that were not fairly put". That supports option D and is left out. Add: "A Critic check of owner questions caught several not fairly put, each reworded (source: portfolio ideas/IDEAS.md, evidence list)." The Context line should quote both root causes.
4. **The recommendation leans on the 14 rounds as evidence about spec instructions.** "the map's records support measuring it (one plan review ran to 14 rounds)" is not what the map says. It records the cause as unknown (A7) and lists "Blaming the wording for what the inputs or the split caused… 14-round reviews" as a design trap. Change to: "M3B's plan review ran to 14 rounds; why is not yet known, and it may be the spec's size rather than its instructions (memo A7)."
5. **Options are missing.** The map's question 8 lists "reviewing" and "tracing failures"; the card drops both. Restore them or say why they are left out.

### P-001-no-change-result.md: FAIL (non-blocking alone)
1. **WHY makes option B look bad.** "otherwise the project is set up to change things whatever the evidence says." Replace with a neutral line: "This decides whether the project may end without new instructions."
2. **The owner's recorded intention is missing from Context.** "my intention is to have a refined prompt engine…" (IDEAS.md, 2026-11-01) bears directly on option B. Add it as a Context line.
3. **Neither option states its cost**, which the template requires.
   - A should add: "cost: the project may end with no new instructions to show."
   - B should add: "cost: a change may be adopted that testing did not show to help."
4. **Option A bundles two outcomes** ("stops, or moves to whichever other cause…"). Moving to another cause is a change of scope that would need its own ruling. Say so: "…or, by a separate ruling, moves to…".

### P-001-instruction-approval.md: FAIL (non-blocking alone)
1. **Option B may not be allowed today.** If role-file changes count as rule changes, B delegates a rule change, and the rulebook says rule changes are never delegable (OPERATING_MODEL.md §2:97-98). Add to B: "Needs first a ruling that role-file wording changes are not rule changes, or a rule change to allow it."
2. **"passed its registered test"** is jargon. Write "passed a test agreed in advance."
3. The recommendation and default are both "decide later", so the card costs the owner attention only to defer. Consider withdrawing it and raising it at the Design gate. At minimum, WHY should say what is lost by answering now rather than later.
4. All three Context lines are supported (BRIEFS.toml:2; OPERATING_MODEL §2 lines 97-98; memo C5, H3).

### P-001-model-changes.md: FAIL (non-blocking alone)
1. **WHY states as fact what the Context line says is unconfirmed.** "Published research reports that instructions tuned for one model can do worse on another" matches memo F1, which is "assumed (reported, not opened)". Change to: "One paper, not yet checked, reports that instructions tuned for one model can do worse on another."
2. **"New models arrive every few months"** has no source. Cite one or cut it.
3. **Option B states no cost.** Add: "cost: problems are found only after they affect work, possibly by you."
4. **Blast radius is understated.** "this project's scope only" ignores two things: the model-diversity rule (Context line 2, which is supported by §5:251-253), and the owner's wish that results be "integrated into the operating model completely". Change to: "this project now; every project's roles if adopted into the model."
5. As with instruction-approval, a "decide later" recommendation and default makes this a candidate to withdraw until the research returns.

### P-001-time-and-limit.md: FAIL (minor)
1. **"the Design gate by early December"** is wrong for option C. Four weeks from 1 November is about 29 November. Change to "by about 29 November."
2. **The recommendation's "needs about a week"** has no source. Cite one or write "an estimate."
3. **"You said less of your time is not a goal here"** paraphrases the owner. Quote instead: "You said success is 'a combination of all but lower agent usage and less of my time'."
4. All three Context lines are supported (§3:114 "[open: the length]"; IDEAS.md quote verbatim; NEXT-SESSION.md:22).

### P-001-test-budget.md: FAIL (minor; class and default right)
1. **Risk class, default and timeout are correct.** R3, irreversible, "DEFAULT: none (spending never defaults)" and "TIMEOUT: none" match §2:93-94.
2. **WHY misreads the figures.** "One reviewer run in Service-Desk used between about 57,000 and 214,000 tokens" is wrong: the memo's figures span several reviewer runs, and most runs recorded no figure (G1, C2). Change to: "Reviewer runs in one Service-Desk session used between about 57,000 and 214,000 tokens each; most runs recorded no figure."
3. **Option A doesn't say what 100 runs means in usage.** Add: "at the sizes seen, about 6 to 21 million tokens."
4. **"then reset at the Build gate" is unclear.** It leaves open whether Build is covered. Change to: "covering Discovery and Design; a new limit is put to you at the Build gate."
5. **The recommendation's reasons have no source.** "runs are what you can see on your plan's usage" is unsourced, and "100 is enough to learn whether testing is feasible" is unsupported: the memo marks the sample size needed as unknown (G2). Reword as estimates.
6. **Option C states no cost.** Add: "cost: past records are incomplete (most conversation work has no recorded brief or model), so a fair before/after test may not be possible."
7. **The third Context line misstates the owner.** "The owner ranked lower agent usage outside this project's goals" is wrong: the owner did not rank anything. In a spending card the paraphrase also leans toward spending. Change to: "Asked how to judge success, the owner said: 'a combination of all but lower agent usage and less of my time' (source: portfolio ideas/IDEAS.md, 2026-11-01)."

### Plain English across the files
- The cards mostly use words the owner knows from Service-Desk (brief, role file, gate, tokens).
- Fix "registered test", "graded memo", "reset at the Build gate" and "baseline" where they appear.

### Not asking the map's question 1: fair, with two caveats
IDEAS.md records the owner choosing among almost the same options: "fewer review rounds; less of the owner's time; lower agent usage; better research". The owner answered: "a combination of all but lower agent usage and less of my time", with the core goal to "minimize the gaps…". Re-asking would ask the owner to repeat themselves, so skipping it is fair, with two caveats:
1. **The answer is a combination, not one goal first.** The owner deliberately did not rank. The Discovery-3 record ("the owner's answers to its shortlist recorded") should file question 1 as answered from the record, quoting the owner's words. It should not say the owner picked one. The worst-work card already covers the ordering in part.
2. **One option was never put to the owner.** The map's "fewer problems reaching you" was not offered. The record should note it as not covered, or it should be folded into the worst-work question.

Files reviewed: /home/user/Model-Lab/questions/P-001-*.md (seven files), /home/user/Model-Lab/research/Q-001-memo.md, /home/user/portfolio/ideas/IDEAS.md, /home/user/portfolio/ideas/NEXT-SESSION.md, /home/user/Service-Desk/reviews/M3C/_triage-r3-critic-verbatim.md, /home/user/Personal-Org-Operating-Model/OPERATING_MODEL.md, /home/user/Personal-Org-Operating-Model/template-v3/governance/BRIEFS.toml.

## Round 2
Verdict: FAIL

**Summary.** Every round-1 finding is resolved. One new problem blocks the pass: two cards cite a source-check record that does not exist. The fix is to remove that citation.

**Blocking: a cited record does not exist**
- Two Context lines cite `research/Q-001-source-check.md`, which is not in the Model-Lab tree:
  - P-001-session-records.md, Context line 2 (line 16): "…(source: research/Q-001-memo.md, C1, confirmed in research/Q-001-source-check.md)"
  - P-001-test-budget.md, Context line 1 (line 16): "…(source: research/Q-001-memo.md, G1, confirmed in research/Q-001-source-check.md)"
- A record that does not exist cannot support a claim. Delete ", confirmed in research/Q-001-source-check.md" from both lines, or file the source check first and keep the citation only if it confirms C1 and G1.

**Non-blocking**
- **P-001-test-budget.md:** options A and B state no cost; only C does.
  - Add to A: "Cost: about 6 to 21 million tokens of your plan's usage if all are used."
  - Add to B: "Cost: you must pick a figure now, before the research has sized what a test needs."

**Resolved and checked, with nothing new unfair**
- **no-change-result:**
  - WHY is now neutral.
  - Both options state their cost.
  - The owner's intention is quoted exactly as it appears in IDEAS.md.
  - The separate ruling for moving to another cause is now stated.
- **session-records:**
  - The Chief of Staff's account is attributed correctly.
  - The owner's endorsement is quoted exactly.
  - The options are narrowed to where recording starts, and each states its cost.
  - "how much is not yet known" and "not yet measured" are added.
- **worst-work:**
  - It is reframed as "look at first", with all six kinds of work as options.
  - It has no recommendation and no default.
  - WHY no longer argues for one option.
  - The Context now gives both root causes (triage lines 20-21, checked), says the cause of the 14 rounds is unknown, and adds the evidence on unfair questions.
  - "TIMEOUT: none" is right, since only the owner can answer.
- **time-and-limit:**
  - Option C's date is now about 29 November.
  - The recommendation is labelled an estimate.
  - The owner is quoted, not paraphrased.
- **test-budget:**
  - WHY gives the token figures as a range across runs.
  - Option A now shows its token range and makes clear the Build gate sets a new limit.
  - C states its cost.
  - The recommendation is labelled an estimate, with a new G2 Context line.
  - The owner is quoted, not paraphrased.
  - R3, irreversible, "DEFAULT: none" and "TIMEOUT: none" are correct.
- **Withdrawals:** instruction-approval and model-changes are withdrawn to the Design gate. That resolves my earlier findings on both, including the round-1 point that a "decide later" ask spends the owner's attention only to defer.
- **Question 1:** the planned record answers it from the owner's recorded words, quoting the owner's combination of goals, and notes "fewer problems reaching you" as not covered. That meets both caveats from round 1.

Files: /home/user/Model-Lab/questions/P-001-session-records.md, /home/user/Model-Lab/questions/P-001-test-budget.md

## Round 3
Verdict: PASS

Both fixes are in place in the two files you changed. The other three passed at round 2 unchanged.

- **P-001-session-records.md:** the source-check citation is gone from Context line 2, and no other line in the file mentions it.
- **P-001-test-budget.md:**
  - The source-check citation is gone from Context line 1.
  - Option A now carries my exact cost wording (line 8), and so does option B (line 9).
  - Option C's cost is unchanged.
  - All three options now state a cost.

