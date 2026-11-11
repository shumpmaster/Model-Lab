# Triage — P-002's brief, FAIL at Critic round 3

*Triage's return (brief: docs/briefs/250-critic-triage.md), a fresh Critic session on a different model from the plan's writer, verbatim. Recorded by the Orchestrator. Session session_01QBwHGJRsdA6DND96m5Z9xE, 2026-11-11, on the fixed copy Model-Lab@4d0286a.*

Verdict: none

Scope: I read the brief, the three Critic rounds, both cards as put, the two decision records (P-002-value-target.md and P-002-trial-gates.md), the stop rule and routing text, the Q-017 memo (by search only) and the value-target Critic record (by search only). I did not reopen docs/PROJECT.md or the odds Reviewer record. I accept the round 1 and 2 findings on V2 and the odds as those rounds recorded them.

## 1. The trace

The failure was not a lack of progress. Blocking findings went 2, then 1, then 1, and total findings went 11, 8, 6. Round 3 itself found every round 1 and 2 finding answered. The pattern is that each round's fix wrote new text, and the next round found a fault in that new text.

**Round 1 (brief 246)**
- Blocking 1: no role owned picking leads and writing each research question. The Chief of Staff and the Input reader now own those steps.
- Blocking 2: the guard against the prompt engine's counting window (V2) covered trials but not methods entering the model (M14) or this project's own pieces. The section 8 constraint pairs and "Proposed" wording now cover them.
- Non-blocking findings 3 and 5 were the first sign of the late failure. They said the plan attributed to a record things the record does not hold, and that "proposed" and "ruled" were mixed up.

**Round 2 (brief 247)**
- Blocking 1: nothing in section 7 asked whether a method can be switched on and off piece by piece. U5 now covers it.
- Non-blocking 5: "30 each way", "5 short reads" and the design being "the owner's" were not in the cited record. The Critic could not open the cards, because the files were removed and only commit hashes were cited. Its remedy was "cite the commit or intake that holds them, or mark them as the card's terms". The brief took the second route and wrote "a term of the card the owner answered".
- Round 2 also passed section 6's "Proposed" list as "not presented as ruled", without opening either card.

**Round 3 (brief 249)**
- The cards were supplied for the first time.
- Blocking: both cards put the 5 short reads, the 3-card cap and the two-week limit in a list headed "Proposed under every option ... (proposals; your ruling makes them so)". P-002-value-target.md says those proposals are "not yet ruled one by one". The brief lists the cap and the two-week limit as proposed but treats the 5 short reads as ruled in section 4 and in section 6's cost line. The last bullet also says every listed item was on a card, which two are not.

## 2. Routing

- **Defect:** the brief's section 6 and section 4. It is a claim about what the owner ruled that the records do not support.
- **Originating stage:** stage 2 Shape ("the project document drafted"). Under feedback routing this is "a fact ... wrong → 2". It is not stage 3 or 4: no criteria or checks are wrong, so this is not a "criteria were wrong" case and needs no owner approval to log it.
- **Contributing stage:** the Critic checks in rounds 1 and 2 (see section 4 below). They did not catch it, and one suggested remedy led to the wording round 3 failed.
- **Process gap:** the cards as put were not in the Critic's copy at rounds 1 and 2. They were deleted, and the brief cited commit hashes the Critic could not open. The Chief of Staff handed them over only at round 3.

## 3. Root cause

The decision records and cards do not say plainly which trial terms the owner ruled and which are still proposals.
- The owner ruled option A on cards that put a ruled design next to a "Proposed ... your ruling makes them so" list.
- The decision record's ruling line names only the approvals and "two looks planned per trial". It adds that the rest is "not yet ruled one by one".
- The brief drew on the cards loosely.
- Earlier rounds flagged the symptom line by line, and each fix re-attributed a line without checking its status against the ruling record.
- The proposals appear in the owner-time list, the stop-rule list and the odds list, and nobody had one list of ruled against proposed to check against.

## 4. Each blocking finding

- **R1-1 (no owner for the screener):** a fault in the brief. Real.
- **R1-2 (no guard against the prompt engine's counting window):** a fault in the brief. Real.
- **R2-1 (U5, switching per piece):** a fault in the brief, and one round 1 should have caught.
  - Round 1 read the value-target record, and that record's round 2 text (line 209) already held the point.
  - **D-050 flag: round 1's check.**
- **R3-1 (5 short reads shown as ruled, and the "each of the others" claim):** a real fault in the brief, with no false positive.
  - Both cards list the 5 short reads as proposals, and the decision record says the other proposals are not ruled one by one.
  - Earlier rounds should have caught it.
  - Round 2 had the bullet in front of it and passed the ruled/proposed labelling.
  - The brief's own wording "a term of the card the owner answered" came from round 2's suggested remedy. **D-050 flag: round 2's check.**
  - One part of the false claim is a regression from the fix to round 1's finding 2. The "no method entering the model" proposal is on neither card; the brief added it in its own words.
  - The 30-each-way size is less clear. It sits in the card's Words, which the owner's answer A covers, but the decision record's ruling line does not name it. I count it as ruled, with a possible risk that someone later calls it unruled.

## 5. Round 3 non-blocking findings

- **2 (cards "removed", with no record saying so):** real and small. The record of the cards as put is the intake files, and the brief should cite those.
- **3 (the Researcher and Source checker hold WebSearch and WebFetch, against "the one role that reads outside text"):** real. The brief should scope the sentence to the feeds or say how outside text reaches those two roles. Rounds 1 and 2 touched this area and passed it, so this is a minor D-050 flag on their checks of that row.
- **4 (M9's "is written in a registered experiment" reads like a document task):** real. It is arguably a fail under the definition of ready ("fail any milestone ... reads as an action or a task"), not just a suggestion. Rounds 1 and 2 passed M9's wording, so this is a minor D-050 flag on their milestone reads. M8's "written as rules" is saved by its second half, which names applied results.
- **5 ("about seven weeks" is not in Q-017 §1):** real.
  - My search of the memo found no such span. The memo's only hit is a count line.
  - The figure came from the Critic's own earlier record, not a primary source.
  - Round 1's finding 9 repeated it and round 2 confirmed it.
  - **D-050 flag: rounds 1 and 2.** Round 3 flagged this itself.
- **6 (link 4, "falls on both sides alike", stronger than the card):** real but minor, and covered by the U5 sentence after it. It needs a softer verb, not a round. I did not reread the card's exact wording for this line.

## 6. Which stop-rule option the evidence supports

**One focused confirmation review.** The evidence does not support the other three options.
- **Re-specify and re-scope:** the criteria and scope are not what failed. Round 3 passed the milestones, the owners table, the limits and section 9. Every round 1 and 2 finding is answered.
- **Drop:** no finding questions whether the project is worth doing.
- **The case for a focused review:**
  - The one blocking finding is narrow and mechanical. Add the 5 short reads to the "Proposed" list (or cite where the owner ruled them). Say which listed items are on a card and which are the Chief of Staff's own.
  - The non-blocking findings are cheap to fix at the same time.
  - The findings are shrinking, not repeating.
- **Conditions on the confirmation review:**
  - It reads the cards and intake files, which round 3 had and rounds 1 and 2 did not.
  - It is limited to a check of every ruled-or-proposed label in sections 3, 4 and 6 against the decision records, with the fixes to non-blocking findings 2 to 5 included.
  - It is a fresh session on a different model.
- **Accepting work despite a failed check is not an option.** The summary to the owner should name the root cause above and the D-050 flags on rounds 1 and 2.

Files: /home/user/ml-triage-250/docs/projects/P-002.md; /home/user/ml-triage-250/reviews/P-002-brief/critic.md; /home/user/ml-fixed-249-cards/P-002-trial-gates-at-3ae1268.md; /home/user/ml-fixed-249-cards/P-002-value-target-at-964da47.md; /home/user/ml-triage-250/decisions/questions/P-002-value-target.md; /home/user/ml-triage-250/decisions/questions/P-002-trial-gates.md.
