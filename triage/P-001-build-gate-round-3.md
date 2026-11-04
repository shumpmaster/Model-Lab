# Triage — the two Build-gate questions, FAIL at Critic round 3

*Triage's return (brief: docs/briefs/55-critic-triage.md), a fresh Critic session on claude-sonnet-5-5, verbatim. Recorded by the orchestrator. Session session_01QBwHGKFFgmANWaCNGxCLZd, 2026-11-04.*

Verdict: none

# Triage: the Build-gate cards (questions/P-001-build-gate.md and questions/P-001-build-gate-terms.md), FAIL at round 3

Read-only. I ran nothing. I read from /home/user/ml-triage at 8a101ed. I read every file the brief listed, plus the stop rule's text (OPERATING_MODEL §4, lines 203-210) and AGENTS.md §5 and "Plain English first". I recomputed the weeks by reading sizing.py and output.txt, not by running them. I did not read docs/handoff, docs/LESSONS.md, sessions, docs/reports, any -notes.md or the git history.

**Self-implication flag (D-050).** This session is fresh, but its own record does not clear the earlier Critic checks, so I flag these:
- Round 1 finding 12 and round 2 "Checked and true" both passed the "32 to 64" weeks that round 3 now challenges. Round 3 undone also says the sizing was not re-derived. All three rounds say they did not re-derive sizing, and none opened sizing.py's `par` line. Finding 4 below is therefore a miss in rounds 1 and 2.
- Round 1 finding 3 itself wrote "up to 183 to 366 session starts if K5 fails". The redraft copied it, and round 2 G2 then failed it.
- Round 1 finding 5 (option C has no power or gain) was non-blocking. Round 2 G1 made the same gap blocking.
- Round 2 said the "stop to the owner" wording was accurate. Round 3 finding 2 reverses that.
- Round 3 blocking finding 1 is, I find, a false positive (below).
- No round checked the cards against the decision-card form (§2, lines 69-73: "2-3 options", background of at most 5 lines).
- Round 1 did not read S-001 lines 195-324 and did not open E-003.

## 1. The trace

### Round 1 (all five blocking findings confirmed, all present in the first draft)

- **G-1 (the opening did not lead with the skipped checks).** The plan's "In plain words" (S-001:10-13) says it. The first draft left it out. Writing fault.
- **G-2 (power stated as fact).** Present from the first draft. S-001:13 and :42-44 and output.txt:79 give 0.80, falling to 0.51 and 0.54. Writing fault.
- **G-3 (the wakes outside the budget).** Present in the first draft. S-001:16 and :124 state it. Writing fault.
- **T-8 (the "eight terms" against the plan's nine questions).** Present from the first draft. Q3, Q5 and Q8 each have two or three parts (S-001:336, :338, :341-345). The plan's nine questions are really about 16 asks. Writing fault, made worse by plan packaging.
- **T-9 (term 7A hid its departure from the owner's wording).** Present from the first draft. S-001:342 says so itself. Writing fault.

### Round 2 (seven blocking findings)

- **G1 (option C unfairly put).** Present in round 1's text. Round 1 rated it non-blocking (its finding 5). Round 2's escalation was reasonable but inconsistent with round 1. Confirmed. Writing fault plus Critic inconsistency.
- **G2 (the "up to 183 to 366" worst case).** Confirmed against S-001:130 and :135 (243 to 487). It was added by the round-1 redraft, which copied the Critic's own round 1 wording.
  - The plan states it wrongly too. S-001:17 says A's growth is "up to about 180 to 360 in all". Its own table at :130 and :135 reaches 243 to 487. **That is a plan misstatement (stage 3).**
- **G3 (the case's lettering clashed with the card's).** Confirmed. Added when the card was relettered in the round-1 redraft (the plan's A, B, C, D became the card's A, C1, B, C2). Writing fault, and it lies in the case, outside the two cards.
- **T1 (the value-target quotation).** Confirmed in substance. I cannot tell from the findings whether term 1's fragment came from the first draft or the redraft. Round 1 did not compare term 1 to S-001:334-335, so if it was there, it was missed. The current text now matches S-001:334-335 word for word.
- **T2 (9B's "fully apart" gain).** S-001:344 says "Little isolation is gained". Confirmed, and a writing fault. Present or added: not determinable. Round 1 said nothing about the gain, so it was missed if present.
- **T3 (term 10 asks for fallbacks without saying what they are).** Confirmed. Term 10 was new in the round-1 redraft, built to meet round 1 finding 8. Added by the redraft.
- **T4 (the claim "every part of the nine except budget and size").** Confirmed against S-001:338. The sentence was added by the redraft, which makes it a fresh overclaim. Writing fault.

### Round 3

**Finding 1 (C2's chance) is refuted as stated.**
- The card's own preamble (gate card line 9) says: "'Chance' below is the chance of seeing a real 20-point gain in built work".
- For built work at 100 pieces, output.txt:83-84 gives 0.96 under the middle assumption and 0.71 with judge error. Both match "about 24 in 25, or about 7 in 10".
- Round 3 quoted the option line without the definition. It is a reading risk, not a falsehood: an owner can read the figure as the whole option's chance. In C2, plans stay at 60 pieces (0.80 and 0.45, output.txt:48-49).
- Under A, B, C1 and C2, Chance means built work's chance. The words "in built work" should sit on each option or in a note under C2.
- This is non-blocking, and the redraft added it (the G1 fix).

**Finding 2 ("comes to you first") is confirmed for the terms card. It is mostly supported for the gate card.**
- Terms 10A: "every failure that would change your part comes to you first" is not held by S-001. Only K1, K3, K4 and K5-at-its-first-check become a question (S-001:177, :180, :181, :187).
  - K7: the Orchestrator tries first. Then the owner just sends wake messages (S-001:189). No go-on-or-stop question is offered.
  - K5 in the Orchestrator's own session, and K5 failing at a later wake, are not questions (S-001:183-185).
  - Term 10's own body says the Orchestrator tries first, so the gain line contradicts it.
- Gate card, recommendation: "a failed first check there comes to you before more is spent". Mostly true. K1, K3, K4 and K5 become a question. K2 stops the lead and the owner starts a new session. K7 does not give "before more is spent".
- A fix inside the cards' text meets it. Name the checks that are asked as a question (K1, K3, K4, K5 at its first check). Say the wake-message duty simply falls to the owner. This needs no record outside the cards.
- Added by the redraft, in the T3 fix and the K5 rewording.

**Finding 4 ("32 to 64 weeks") is confirmed. It is under-rated as non-blocking, and it is a plan fault.**
- sizing.py:144-146 computes "together" as `par = max(weeks_for(...))` over the kinds. That is the longest kind (research, 32 to 64) with all three kinds collecting from day one. This is term 2C ("all at once").
- Collecting one kind after another is the sum, 7 to 15 + 21 to 42 + 32 to 64 = 60 to 121 (output.txt:90).
- "The next kind starts collecting while the previous is judged" (2A) is neither figure. The plan never computes it.
  - If the next kind opens only when the previous finishes collecting, the total is near the sum. Only the judging tail of about 2 weeks per kind overlaps (S-001:120).
  - If it opens early (judging runs weekly, from the first export), 2A is close to 2C.
  - The plan gives no opening rule.
- The plan's own text is inconsistent:
  - S-001:15 ("32 to 64 if collected together") and :337 tie the figure to "collected together", and then offer two ways of overlapping with no separate figure.
  - S-001:90 glosses "together" as "the next kind collects while the previous is judged".
  - Output.txt:90-93 labels the max column "together".
- Terms 2A's gain ("about 32 to 64 weeks ... instead of 60 to 121") and 2C's "the plan gives no separate figure for its weeks" are therefore both wrong against sizing.py.
  - 2C's figure is exactly the 32 to 64 that 2A claims.
  - The recommended option's headline gain rests on a figure no record derives for it (LL-46, LL-50). This is a decision-driving figure, so it should have been blocking.
- The gate card's "32 to 64 if the kinds collect side by side" is true as full overlap. It is not tied to 2A there.
- No frozen criterion cites the figure (grep of the proposal found nothing), so no frozen text needs to change.
- **Records that would need to change:**
  - S-001:90 (the gloss) and :337 (Q4). Add a staggered row with a stated opening rule, or say "32 to 64 only if all three open at once".
  - sizing.py:135-149 and output.txt:89-93: relabel `par` "all three at once" and compute a staggered figure.
  - Then terms 2A, 2C and Context.
- A card-only fix is possible. Say "32 to 64 only if all three kinds collect at once (2C); the plan gives no figure for 2A". It is true, but it removes 2A's stated gain and weakens its recommendation. That is a content judgement for the Chief of Staff and the owner, not a wording fix.

**The other round 3 items.**
- Item 3 (B, C1 and C2 omit the "about 1 in 2" caveat): non-blocking, correct. It stays true under the preamble's "middle assumption".
- Item 5 (K1 limit not on the cards): non-blocking. Round 3 says the case has it at section 5. The K1 limit is that the secret check is kept from the writer of these cards by instruction alone (S-001:18). It touches the cards' writer, so it should be on the gate card.
- Item 6: "a little over half" is 0.45 against 0.80. Right for the middle assumption.
- Item 7: the Orchestrator's K7 ask (weekly landing, S-001:189) is not in the plan's ranges (:126-135). The "worst named fallback" is therefore not the worst. This is a plan gap.
- Items 8 and 9 stand as non-blocking.

### Root cause and originating stage

**Primary root cause: the cards' scope.** The cards are not decisions. They are figure-exact transcriptions of a 373-line plan, and they grew with every redraft.
- The gate card has options A, B, C1, C2, D, E and F. The terms card has 11 terms. The card form allows "2-3 options" and background of at most 5 lines (OPERATING_MODEL §2, lines 69-73). The gate card's Context has 10 lines.
- Each round added content to meet findings: carry every part, give C power, give the worst ranges, name the fallbacks. Each addition carried new ranges and claims, and about 20 numeric or behavioural claims need a separate check.
- Blocking findings by round: 5, then 7, then 2 (1 after my refutation). They fell, but nearly every new blocker sits in text added to cure the previous round. The pattern fits a growing-surface problem, not a drafting slip.
- The Critic's rounds drove the growth and never asked for the cards to be cut (D-050 above).

**Contributing stage 3 faults (the Definer's plan).**
- S-001:17: "up to about 180 to 360" against the table's 243 to 487.
- S-001:90 and :337: the "together" gloss and the missing staggered figure.
- S-001:126-135: no Orchestrator K7 ask, no combined failures.
- S-001:336-345: compound open questions. Q3, Q5 and Q8 each carry two to three asks. This explains why the terms card runs to 11 terms.

**Routing (§4 "Feedback routing").**
- Wrong claims about records: the Chief of Staff's drafting, which is not a pipeline stage.
- Wrong or inconsistent figures in the plan: stage 3.
- A gap in Critic coverage: stage 6 (the Critic's own check). It missed the weeks figure three times.
- "Criteria were wrong" is not engaged. No criterion needs to change.

## 2. Round 3's two blocking findings

| Finding | Meets the test? | Fix inside the cards? |
|---|---|---|
| C2's chance | Refuted as a falsehood; a clarity point | Yes. Add "in built work" to each Chance, or a note that plans in C2 stay at 4 in 5 (9 in 20 with judge error) |
| "Comes to you first" | Confirmed on terms 10A; mostly supported on the gate card | Yes. Name K1, K3, K4 and K5-at-its-first-check as questions. Say the wake-message duty falls to the owner. No outside record needed |

Finding 4 (the weeks) is the one that depends on a record outside the cards.
- A wording fix inside the cards is possible but removes 2A's stated gain.
- A true figure for 2A needs the plan, sizing.py and output.txt to change (see the records above).

## 3. The stop rule's options

I note two points about the rule first.
- OPERATING_MODEL §4:203-206 and AGENTS.md:38 name plan rounds and build rounds. Neither names a round of checking an owner card.
- Brief 54 treats round 3 as "the last allowed", so the Orchestrator applies the rule by analogy. I found no card-round limit in the files I was assigned. Whether the stop rule's option set governs cards is "not checked" beyond that. If the owner reads the rule as not covering cards, a fourth round would not be barred.

**Re-specify.**
- For these cards: the Chief of Staff drafts new cards from round one. The plan would also change if the Definer is asked to correct lines 17, 90, 126-135 and 337. A rewritten plan "starts again at round one" (AGENTS.md:38, which states this for plans). I found no equivalent for cards: "not checked".
- Effect: the whole cards, and the freeze, wait for a full new set of checks. The Build gate cannot pass without the cards (§4:199, "nothing goes past a gate until the owner rules").
- Evidence does not support it. The rewrite reopens ground the Critic accepted in three rounds.

**Re-scope.**
- Cut the cards to the decision.
- Gate card: the sizes the owner chooses, plus hold, recycle and kill (§4:199). The sizes cite the plan's one table (S-001:94-99, :126-135) by line, not by re-transcribed ranges.
- Terms card: only the terms the owner must rule before the freeze (Q1, Q2, Q4, Q5, Q8, Q9 per S-001:353). Terms with a plan default are listed, not argued.
- Who: the Chief of Staff drafts; a fresh Critic session on a different model checks (D-037, D-056). The card form is the rule that decides (§2:69-73, "2-3 options", background of at most 5 lines).
- Effect: it removes most of the claim surface that has failed. Whether a re-scoped card starts again at round one is "not checked". The rule says it for plans only.
- It does not solve the weeks figure, which still needs the plan record, or a statement that the plan gives no figure for 2A.

**Drop.**
- Dropping either card leaves the Build gate unruled. The plan's open questions 5, 8 and 9 must be ruled before the freeze (S-001:353).
- Without the terms card the plan cannot freeze. Without the gate card, the budget (the "about 100 runs" ruling covers only Discovery and Design, P-001-test-budget) is unruled.
- Dropping the whole test would be a kill, which is never delegable (OPERATING_MODEL:98).
- Not supported.

**One focused confirmation review.**
- The Chief of Staff fixes exactly: 10A and the gate recommendation ("comes to you first"); the C2 chance reading; term 2A's and 2C's weeks; and the Orchestrator K7 ask in term 10. No new claim is added.
- A fresh Critic session checks only those lines and a diff showing nothing else changed. Any added claim fails it.
- The Definer corrects S-001:17, :90, :337 and the table at :126-135, with sizing.py and output.txt relabelled. Whether those edits need plan re-review is "not checked" (AGENTS.md:38 speaks of a rewrite).
- Decided by the stop rule (§4:206) and AGENTS.md:38 ("Record the owner's choice as a ledger ruling before the next round; a FAIL in that confirmation review goes back to the owner the same way"). The 2A/2C weeks and the K7 ask depend on the plan records.

**Who rules.**
- The owner must rule. The delegation text (OPERATING_MODEL:94-97) lets a signed, time-limited, logged grant cover "choosing a focused confirmation review at the stop rule".
- docs/LEDGER.md at this commit holds only L-0001 to L-0005. None is a delegation, so no grant covers it.
- The earlier stops were ruled by the owner through questions (decisions/questions/P-001-plan-stop.md and plan-stop-2.md).
- Accepting the cards despite the failed check is never an option (§4:206).

**Which option the evidence supports.**
- A focused confirmation review, after the minimal re-scope above, preceded by the plan erratum for S-001:17, :90 and :337.
- Reasons:
  - Blocking findings fell from 5 to 7 to 2, and of the two, one is a false positive.
  - The remaining defects are one-line text fixes, plus one plan figure.
  - A re-specify rebuilds exactly the text that has failed three times.
  - Drop cannot move the gate.
- Caution: this is not "just fix two lines". Each earlier round's fix added new errors. The confirmation must be strictly diff-limited, and any new claim must fail it.
- **What would change it:**
  - If the owner rules that card checks fall outside the stop rule, a plain round 4 is allowed.
  - If the Definer cannot supply a defensible staggered figure for 2A, the cards should say plainly that none exists and drop 2A's gain. That alters the recommendation. The Chief of Staff and the owner should then look again at whether 2A is still the recommended answer.
  - If a diff-limited confirmation review again adds new errors, re-scope is the better call.

## Six-part contract

1. **Changed:** nothing. I hold no write tool.
2. **Why:** to trace the three-round failure of the two Build-gate cards to its root cause and originating stage, and to set out the stop rule's options (brief for Triage, under OPERATING_MODEL §4 "Stop rule").
3. **Verified:**
   - I read the full text of the three Critic rounds, both cards, S-001 (lines 1-194 and 333-373; the middle part was not read), sizing.py and output.txt, E-003.md lines 1-70, the round 3 case and the gate Critic's view, the owner's rulings plan-stop, plan-stop-2, gate-citation, worst-work, e002-not-tested and test-budget, the earlier Triage rounds 4 and 5, docs/LEDGER.md, AGENTS.md §3-§5 and the stop rule's lines in OPERATING_MODEL §2 and §4.
   - I checked the figures A, B, C1 and C2 against output.txt and the plan's tables by eye.
   - I checked the V1 and M2 quotations in term 1 word for word against S-001:334-335.
   - I confirmed the weeks arithmetic (sum 60 to 121, max 32 to 64) from sizing.py:144-146 and output.txt:90-93.
4. **Undone:**
   - Not run: sizing.py. I read it and its output.
   - Not read: S-001 lines 195-332; docs/briefs/47, 52 and 54 beyond their text; the earlier cards' text for rounds 1 and 2. I judged "present or added" from the findings' own quotations. For T1 and T2 I could not tell.
   - Not read: the full E-003 beyond line 70, reviews/S-001/plan.md, PACKS.toml.
   - I did not check whether a plan erratum needs plan re-review, or whether the rule's re-round-one clause applies to cards. Stated above as "not checked".
5. **Needed outside my lane:**
   - The owner: choose among the stop rule's options, and say whether the stop rule applies to card checks. No delegation exists.
   - The Chief of Staff: draft the diff-limited fixes (or the re-scoped cards), and add the Orchestrator K7 ask to term 10.
   - The Definer: correct S-001:17, :90, :337 and the table at :126-135, with sizing.py and output.txt relabelled and a staggered figure with an opening rule.
   - The Orchestrator: record the owner's choice as a ledger ruling before the next round (AGENTS.md:38), and dispatch the next Critic session. The brief should include the diff limit.
   - A fresh Critic: run the confirmation review. It must open sizing.py.
6. **Open questions:**
   - Does the stop rule cover card checks? Is a card-round count anywhere in the rules?
   - What opening rule should define the staggered kinds (2A)? Does it need a new run of sizing.py?
   - Will a plan erratum to S-001:17, :90 and :337 re-open plan review? The plan is a draft (`status: draft`, `frozen_at: <commit>`).
   - Should the cards state the Orchestrator's K7 ask, or should the plan's ranges carry it?

Files: /home/user/ml-triage/reviews/P-001-build-gate/critic.md, /home/user/ml-triage/questions/P-001-build-gate.md, /home/user/ml-triage/questions/P-001-build-gate-terms.md, /home/user/ml-triage/specs/S-001.md, /home/user/ml-triage/experiments/E-003/sizing.py, /home/user/ml-triage/experiments/E-003/output.txt, /home/user/ml-triage/docs/LEDGER.md, /home/user/Personal-Org-Operating-Model/OPERATING_MODEL.md
