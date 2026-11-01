Verdict: PASS

The Critic's check of the reworded M1 line and questions/P-001-open-unknowns.md, on a different model from their writer (brief: docs/briefs/16-critic.md), verbatim: round 1 (FAIL; M1 PASS), round 2 (PASS). Recorded by the orchestrator. Session session_01QBwHGHrHnEvMNYgKDoaH8w, 2026-11-01.

## Round 1
Verdict: FAIL
M1: PASS
Question: FAIL

I wrote no files. I read everything cited in the brief, plus OPERATING_MODEL.md §2, §3 and §4 item 7.

1. (M1, non-blocking) The reworded M1 line is an achievement and not a task. It is plain English and has a `· why:`. Its "done when" now matches what research/Q-008-memo.md delivered:
   - Counts per kind are in §2.
   - Causes where a record names one are in §4.
   - What the records cannot show is in §5: 61 of 84 residual, and 41 with no record of findings.
   - The starting figures (first-try pass counts) are in the bottom-line table 2.

2. (M1, non-blocking, advise a rename) The name still reads "The causes of rework are known (M1)". The memo shows the opposite for most returns, and PROJECT.md U5 says "mostly not". The "done when" no longer promises causes, so the name now over-claims, and an owner reading it cold would be misled. A name such as "The count of past rework is on record" would match. The why ("research found wording may matter less than inputs and how work is split") rests on the earlier research, not on the memo. It is still true as written, because it says what the research found. The memo does not confirm it: it names instructions in 1 return and split in 1.

3. (Question, blocking) The options are not put evenly. Option B lists as its cost that it "uses some of the 100 test runs". Option A also spends those runs, because it runs the replay check in Design. The RECOMMENDATION says so itself: "testing replay in Design costs the same runs as testing it now". So B carries a cost that A shares, and A's own cost leaves out the real difference. Under A the owner rules the Design gate without knowing whether the planned test can run at all. That gap appears only inside the recommendation. Fix: state A's and B's costs on the same terms, and name the real difference, which is timing and what the owner knows at the gate.

4. (Question, blocking) The recommendation's deciding reason is not supported by any cited record. "Costs the same runs as testing it now" is not in PROJECT.md section 7 or section 8, or in the budget record. Section 8 says only that the replay and judge-consistency runs together are planned at no more than 40. Either cite it or label it as the Chief of Staff's own judgement.

5. (Question, non-blocking) The budget context line omits the owner's condition. The record (decisions/questions/P-001-test-budget.md) gives about 100 runs "with checkpoints" on tokens used and remaining. PROJECT.md section 6 also says the project stops and goes to the owner if the 100 runs run out before the fair test is ready. That bears directly on option B and is not mentioned.

6. (Question, non-blocking) The claims about U2 to U4 match PROJECT.md section 7 apart from small narrowings:
   - "judge a sample twice" narrows "repeated judgements".
   - The title and option A say "open into Design", while PROJECT.md says "Design and Build" and U4's test runs in Build.
   - The Context bullet says "into Define", which is jargon and differs from the card's own wording.
   - "No change helps" is accepted in P-001-no-change-result.md as "changing the instructions doesn't help", which is narrower than U4's "any change".
   - Nothing is presented as the owner's view without a record.

7. (Question, non-blocking) DEFAULT: none and TIMEOUT: none depart from the template, which asks for a letter and hours. Here they are right for the kind. §2 says a defaulted answer is never read as the owner's own ruling, and item 7 needs the owner's recorded ruling. Add a line saying why there is no default, so the departure is not read as an omission.

8. (Question, non-blocking) "WHO HAS CHECKED IT" cites reviews/P-001-open-unknowns/critic.md, which does not exist yet. The Orchestrator must record this verdict there before the question is put. The WHY uses the term "load-bearing unknown" without explaining it, though the sentences around it make it clear enough.

9. (Question, structure, no defect) The decision-card parts are all present:
   - the decision;
   - why it is the owner's;
   - background, in four lines;
   - two options with gain, cost and reversibility;
   - a recommendation with confidence and what would change it;
   - who has checked it;
   - a default.

Resubmit the question after fixes 3 and 4. M1 can be committed now. Fix 2 is advised and not required.

## Round 2
Verdict: PASS
M1: PASS
Question: PASS

I wrote no files. I re-read questions/P-001-open-unknowns.md whole and the renamed M1 line in docs/PROJECT.md section 3 (line 46), both on branch cos/p001-m1-and-unknowns.

1. (M1, resolved) The new name is "How often work is sent back, and what the records show of why, is known (M1)". It is an achievement, in plain English, with no codes in the name. It now matches the "done when" and what research/Q-008-memo.md delivered: counts per kind, causes where records name them, and what the records cannot show. The "done when" and the why are unchanged, and the why is still true. My finding 2 is resolved.

2. (Question, resolved) Finding 3, the uneven options. The shared run cost is now stated once, above the options: either way the replay check uses some of the 100 runs, and the options differ only in when it runs and what you know at the Design gate. Option A's cost now names the real difference: the owner rules the gate without knowing whether the test can run. Option B's cost is only the wait.

3. (Question, resolved) Finding 4, the unsupported reason. The recommendation is now labelled "the Chief of Staff's judgement", and the shared-runs point is stated as part of the options. This is acceptable.

4. (Question, resolved) Finding 5, the budget condition. The context line now includes the checkpoints on tokens. It also includes the stop-and-return-to-owner condition if the runs run out, which cites the budget record and PROJECT.md section 6.

5. (Question, resolved) Finding 6, the small mismatches:
   - The title and option A now say "Design and Build".
   - Test 2 now reads "repeat judgements".
   - "Define" is explained in a parenthesis.
   - Item 3 now says "changing the instructions", which matches the owner's recorded ruling.

6. (Question, resolved) Finding 7, the default. DEFAULT: none now says why: a default is never read as your ruling. TIMEOUT: none stands, and that is right for the kind.

7. (Question, resolved) Finding 8, the check record. The card cites reviews/P-001-open-unknowns/critic.md, which you say now exists at /home/user/wt/ml-orch/reviews/P-001-open-unknowns/critic.md. I did not open it. Its round-1 content is my verdict. Add this round-2 verdict to it before the question is put, so the cited record covers the version the owner sees.

8. (Question, non-blocking, no action needed) The owner-facing text is plain. Every claim matches its cited record, and nothing is presented as the owner's view without a record. All the decision-card parts are present.
