Verdict: PASS

The Critic's check of the problem statement (docs/PROJECT.md section 2) and the pre-mortem (section 7), on a different model from their writer (brief: docs/briefs/08-critic.md), verbatim: rounds 1 and 2 (FAIL), round 3, a focused check of the round-2 fix (PASS). Recorded by the orchestrator. Session session_01QBwHGHrHnEvMNYgKDoaH8w, 2026-11-01.

## Round 1
Verdict: FAIL

I checked the Section 2 problem paragraph and the "How other fields solved it" list, and the Section 7 pre-mortem. I checked them against the Q-002 to Q-007 memos, the corrections confirmation, and the milestone lines M1 to M3. The problem statement is neutral and plain enough. Section 2 has three blocking defects: its field bullets say more than the memos support, they rest on held entries, and they carry no transfer checks. The pre-mortem has one blocking citation mismatch (R4). Details follow.

**Problem statement paragraph**

1. NON-BLOCKING. The paragraph does not presuppose that changing instructions is the answer. It names five causes, including "the check itself", and says "changing only what helps", which allows "change nothing". It meets D-055 and LL-02. Two small points:
   - "make work pass its check first time more often" treats every sent-back round as waste. Q-006 §7 item 6 says "round" does not always mean rework, and a round can be the check catching a real defect. The paragraph should say so, or say how M1 will count a "return".
   - The heading "How other fields solved it" presumes the fields solved it. Q-005 shows mixed results: Ontario found no effect, and the English replication found a secular trend.

**"How other fields solved it" list**

2. BLOCKING. The first bullet ("Written hand-over tools and checklists…") says more than Q-005 does.
   - "helped where the failure they targeted was common": Q-005 §1 item 1 says this is opinion (M). P-2 was weakened from H to M, and the baseline-rate reading is the Researcher's own inference (L). SURPASS (F5) cuts against it.
   - "did nothing where it was mandated as text alone": Ontario found no change, but the cause is not established. "Not actually used" is the Researcher's paraphrase of Leape's editorial, not his words (F2).
   - The memo's third condition is missing. Effects came inside a package of training, coaching, culture and peer pressure (F8, F11, F12), and no study separates the written form's own effect (§3.2 opinion).
   - "carried out in full" rests on F4 / LF-Q005-04 and LP-Q005-01, which the confirmation holds back. F4 is one source, observational, with a confounder the memo admits is the Researcher's own remark.
   - "Surgery, intensive care, shift handover" is presented as proof that written tools help, without these caveats.

3. BLOCKING. The second bullet ("Fixes after single incidents…") overreaches and rests on held entries.
   - "fixes that do not depend on remembering a rule worked better": the action hierarchy (F22) is a ranking of fix types by how much they rely on memory. It is not outcome evidence.
   - Q-005 §3.4 says no study measures the net effect of incident-driven rules as a class (LF-Q005-20 is held).
   - LF-Q005-11 (F21) and LF-Q005-12 (F22) are both held. The confirmation also notes F22's tier contents differ from IHI's.
   - "mostly weak written reminders" is loose. The categories were training 20%, process change 19.6% and policy reinforcement 15.2%.
   - The memo's balancing point is omitted: a single severe incident can expose a real general gap (P-10, F15, F16, F25). This breaks the "benefits and risks put evenly" standard.

4. BLOCKING for the first claim, non-blocking for the rest. The third bullet ("Rule sets grow…") is unsupported as a solution.
   - "Fields that keep them usable retire rules on a schedule": F30 is the authors' recommendation to reassess guidelines every 3 years, not evidence that scheduled retirement keeps rule sets usable.
   - Sunset evidence is mixed and mostly advocacy (F33, P-13, rated L).
   - The supporting facts are held or unreachable: LF-Q005-13 (F26) unreachable, LP-Q005-06 held and marked opinion, F28 and F29 unopened.
   - "until they are not followed" rests on those same entries.
   - P-11 says the review interval is unknown for agents.

5. NON-BLOCKING. The fourth bullet ("Before-and-after comparisons…") overstates.
   - "misled in both directions": the memo says "can mislead in either direction" (P-8). Its examples (F3, F9) show only overstatement.
   - LF-Q005-01 and LP-Q005-07 are held.
   - "Compare… on the same past tasks (M2)" assumes replaying past tasks is faithful. Q-003 §7 and Q-001 B4 leave this open, and Q-005 D6 says it "may be possible". Neither the bullet nor the pre-mortem says so.

6. NON-BLOCKING. The fifth bullet (agent pipelines) matches Q-002 §1 items 4 and 5, but with three gaps.
   - "Vague delegation" rests on a single vendor page (B).
   - "Reasoning prompts" rests on Wharton Report 2 (SSRN 5285532), which Q-002 §6 lists as unopened. Only Report 3 was confirmed.
   - Wording-sensitivity evidence that cuts the other way is omitted: Sclar's up-to-76-point swings, and Yang et al.'s +4.8% from requirements-aware optimisation.

7. BLOCKING. The standard in §6 requires a transfer check on conditions for every borrowed principle, and none appears.
   - The "Here:" lines carry principles straight across without stating the conditions each depends on.
   - Q-005 §4 says mechanisms built on fatigue, motivation and social pressure do not transfer (D1, P-3).
   - It says the capacity analogue for "rule sets grow" is only assumed (D4).
   - It says the I-PASS and Keystone effects ran through social routes.
   - "Prefer a tool permission… wherever one will do" fixes a design direction at Discovery as a "Here:" conclusion. It should be framed as a candidate to test.

**Pre-mortem**

8. BLOCKING. R4's sources do not support its claim.
   - R4 is about fitting changes to past tasks and failing on new work. It cites "Q-004 §1; Q-003 §4".
   - Q-004 §1 is about replacing the model.
   - Q-003 §4 is about sample sizes.
   - The memo content that does say optimising on more failures "can bloat instructions and overfit" is Q-007 bottom line 3(c). The GEPA transfer result is in Q-002 (D, unopened).
   - R4 also relies on "the second value target", and Section 6 holds no value targets yet. That reference dangles.

9. NON-BLOCKING. R2 has a citation slip and misses the opposite risk.
   - Slip: it cites "Q-003 §0 item 3". The memo has no §0, and that item is §1 item 3.
   - The 20-point keep bar comes from the plan, not from Q-003. Q-003 says a 20-point gain is detected only about 70–77% of the time, and a 10-point gain about 25%.
   - The opposite failure is missing: real moderate gains discarded as "no difference". Q-003 §6 offers alternatives (an interval rather than a verdict, a more sensitive measure such as findings or rounds, a narrower claim, transcript reading), and R2 omits them.
   - "What counts as one run against the 100-run limit" (Q-003 §7) could cut the usable sample by 2 to 4 times.

10. NON-BLOCKING. R3's fix may already be in place and may be too weak.
    - "Judge on a different model from the work" is already the pipeline's rule (Q-002 §5).
    - Q-003 §1 item 2 and F-h1 infer that doer and checker are in the same provider family, and Q-003 §7 leaves the different-provider question open.
    - The mitigation should say a different family or provider, or a panel (Verga).
    - R3 covers bias and gaming but not a checker that is simply noisy. Q-003 RQ-a notes checker repeatability reduces power. Q-006 §0 item 5 records one memo getting two different verdicts with the same file hash.
    - Q-007 bottom line 2, which R3 cites, includes "wording can raise or lower gaming". The confirmation says this has one source for lowering and none for raising. R3 does not repeat the claim, but the citation should be narrowed.

11. NON-BLOCKING. R5 and R6 are broadly supported, with caveats.
    - R5 correctly cites Q-004 §1 items 1–2 and the tentative dates in §4.5.1. It should add that Q-004 found no study of hand-written multi-page role instructions moving between models, and no controlled evidence for the re-test practices.
    - R6 leans on P-7 (held entries) and P-6, whose agent-side mechanism is assumed.

12. NON-BLOCKING. R7 is accurate (Q-006 §0 items 1 and 4) but incomplete. It omits the survivorship and missing-record problems that bear directly on M1's baseline:
    - records of closed or dropped items are absent;
    - 37 of 104 dispatches have no control record;
    - the dispatch log stops on 2026-10-08;
    - rounds overstate rework.

13. BLOCKING, because it breaks the rule R8 sets itself. R8 says "Rely only on library entries that passed the Source checker". The Section 2 draft cites held entries (LF-Q005-04, -11, -12, -13, LP-Q005-01, -06, -07), which contradicts R8's own mitigation. R8's wording "most outside sources could not be opened" is true of the Researchers' sessions but not of the later source checks. LL-12 and LL-22 are real lessons, but the owner cannot read them as bare ids.

14. NON-BLOCKING. Missing failure modes that the research names:
    - Replay is not faithful, so paired testing cannot run (Q-003 §7, Q-001 B4). M2 and R2 both depend on it.
    - The checker is noisy or inconsistent, as distinct from biased or gamed (finding 10).
    - The test setting shifts during the test: pack contents changed mid-week (Q-006 §0 item 5), and a model change during testing acts like a secular trend (Q-005 P-8). R5 touches only the model change.
    - The budget unit is undefined (finding 9).
    - Very long inputs are a possible confound (Q-002 §3.3, the 22,883-line S-001).
    - The five failure modes the brief expected (gaming, over-fitting, model change, too small a test, records that cannot show causes) are all present as R3, R4, R5, R2 and R7.

15. NON-BLOCKING. Plain-language gaps for the owner:
    - "gain of 20 points" does not say percentage points of first-pass rate.
    - "paired test", "mechanised check", "held-back check", "stop rule", "value target" and "Source checker" are unexplained.
    - "LL-12, LL-22" are bare ids.
    - R1's early sign depends on M1 being able to assign causes, which R7 says may not be possible for conversational work. The table should say so.

**To clear the FAIL:** fix findings 2, 3, 4 (first claim), 7, 8 and 13. The cleanest route is to attribute each bullet to its source with the memo's own caveats, drop or mark each claim that rests on a held entry, add a "conditions and transfer" clause to each bullet, and re-source R4.

## Round 2
Verdict: FAIL

The redraft fixes all 15 earlier findings except one point on sourcing. I re-read section 2 (lines 16–24) and section 7 (lines 68–82) of /home/user/wt/ml-cos/docs/PROJECT.md against the Q-002 to Q-007 memos, the corrections confirmation, and Q-006's source check with its Round 2 PASS. One new blocking finding (N1) fails the round.

**Status of my 15 earlier findings**

1. Resolved. The paragraph now separates returns that caught a real fault from avoidable ones, and the count is tied to the milestone. "Solved it" became "found".
2. Resolved. The checklist and handover bullet uses only LF-02, LF-03, LF-06a, LF-06b and LF-07, all fileable. It states the bundle and coaching condition, that no study separates the written tool's own effect, and that why Ontario saw nothing is not established.
3. Resolved. The single-incident bullet is gone and nothing in its place rests on held entries.
4. Resolved. The rules-out-of-date bullet says plainly that LF-15 is the authors' recommendation and not evidence that scheduled review works. The overrides and non-compliance bullet uses LF-10 and LF-14, both fileable.
5. Resolved. LF-05a is worded as the paper words it ("did not accelerate", "likely part of a wider secular trend"). "May mislead" replaces "misled in both directions", and replay fidelity is stated as not yet known (Q-003 §7).
6. Resolved. The reasoning-prompts and vague-delegation claims are gone. The agent-pipelines bullet uses F-f, P-e, F-g, F-h and F-c (fileable) and F-d (single source, labelled). Q-002 §1 items 4–5 is marked as the Researcher's estimate and not a filed fact.
7. Mostly resolved. Each bullet now has conditions, transfer and "may mean here" as a candidate. The remaining defect is how the transfer lines are sourced (see N1).
8. Resolved in substance. R4 now cites Q-007 bottom line 3, quoted verbatim and labelled the Researcher's opinion, and the dangling "second value target" is removed. One small residue remains (N2).
9. Resolved. The Q-003 section numbers are correct (§1 item 3, §4, §6, §7). The opposite risk of discarding real moderate gains is added, with the report "not shown, with its range". The run-budget unit is fixed before testing.
10. Resolved. R3 now covers the different-family or provider judge, a panel, repeat judgements to measure consistency, and inconsistent verdicts. It cites Q-003 §7 and Q-006 §0 item 5. Q-006's check confirms item 5 once it is read as "packs also differed", and R3 does not over-read it.
11. Resolved. R5 adds the mid-test setting shift, and states there is no study on long hand-written role instructions (Q-004 §1 item 1). R6 labels the agent mechanism as assumed.
12. Resolved. R7 now covers missing records of dropped work, a third of dispatches, and nothing after 8 October (Q-006 §7). "A third" is 37 of 104, about 36%, which is acceptable.
13. Resolved. The Section 2 draft now uses only cleared facts, so it no longer contradicts R8. R8 says "many outside sources", and LL-12 and LL-22 are explained in words.
14. Resolved. R9 (replay), checker noise (R3), setting shift (R5) and budget unit (R2) are added. The long-input confound (Q-002 §3.3) is still absent, but that is non-blocking.
15. Mostly resolved. "First-time pass rate" and "paired test" are defined, and R2 no longer uses "points". Residual jargon is noted at N3.

**New findings**

N1. BLOCKING. Several transfer lines cite Q-005's own principle labels (P-3, P-4, P-8, P-6, D1) as support. They are the memo's unfiled opinions (M) and are not library entries.
   - P-3, P-4 and P-8 correspond to LP-Q005-03, -04 and -07, all held by the confirmation. P-6 corresponds to LP-Q005-06, also held and marked opinion. D1 is stated as opinion.
   - Examples: "agents have no training, culture or peer pressure (Q-005 D1, P-3)… effect sizes… cannot be carried over"; "(Q-005 P-4)"; "a model or version change… acts like such a trend (Q-005 P-8)" in section 2, and "Q-005 P-6" in R6.
   - The only transfer cite that is on solid ground is P-11, which rests on fileable LP-Q005-09 (on LF-15 only).
   - The section's lead says only cleared findings are used, and these cites are not findings.
   - The draft should either label each as "the Researcher's transfer opinion, unfiled (Q-005 §4)" or drop the cite. The P-8 line's agent-side premise rests on Q-001 C4/F1, which are assumed.

N2. NON-BLOCKING. R4 also cites Q-002 P-e. That pattern is about telling wording noise from an effect, and it does not support over-fitting or a held-out set. The memo's own "held-out check" wording in Q-007 bottom line 3 is the real support.

N3. NON-BLOCKING. Small plain-language and completeness points.
   - "mechanised check", "Source checker", "model family" and "chance" are still unexplained for the owner.
   - The first bullet omits the randomised trial's own caveat that its mortality result was not significant (LF-Q005-03).
   - The Q-007 single-source finding that changing a checker's instructions shifts verdicts (c6) is a possible pre-mortem line, but it is not required.

**To clear:** resolve N1 only. N2 and N3 may be fixed at the writer's discretion.

## Round 3 (focused)
Verdict: PASS

I could not run `git diff`. I hold only Read, Grep and Glob, so I re-read the full text of section 2 (lines 16–24) and the section 7 pre-mortem (lines 68–82) of /home/user/wt/ml-cos/docs/PROJECT.md. I checked the three named fixes in that text. I cannot independently confirm that nothing else changed. Of the lines I read, the problem paragraph and the section 7 intro, table, and closing paragraph match what I passed in round 2, apart from the fixes below. Whoever dispatched me should confirm "nothing else changed" from the diff.

**N1, resolved.**
- Every transfer judgement now carries the label "the Researcher's opinion, unfiled, Q-005 §4", or for the rules-out-of-date bullet "the Researcher's opinion, Q-005 §4 P-11".
- The intro line now says the transfer judgements are opinions, not filed facts.
- The P-8 line says "resting on an assumed premise" and is softened to "may act like such a trend".
- R6's source cell now reads "the Researcher's unfiled opinion that rule growth transfers in altered form, its agent mechanism assumed (Q-005 §4)", with Q-002 F-d labelled single source.
- The P-3, P-4, P-6 and P-8 label cites are gone from the text.
- Q-002 F-d is described as "a filed single-source fact", which matches the confirmation.

**N2, resolved.**
- R4 no longer cites Q-002 P-e.
- Its source now quotes Q-007 bottom line 3 as the Researcher's opinion. The quotes "when there is a reliable outcome signal and a held-out check" and "can bloat instructions and overfit" match the memo verbatim.

**N3, resolved for the parts the writer took on.**
- The randomised trial now says its fall in deaths was not significant, which matches LF-Q005-03.
- "Mechanised check", "model family" and "Source checker" are now explained.

**New, non-blocking.**
1. R9 still cites "Q-005 §4 D6", which is the memo's opinion-grade condition. It is unlabelled, though the claim is only that replay "may be possible" and the row's wording stays conditional.
2. The explanation of "mechanised check" sits in the section 2 bullet about rules not being followed, while the term next appears in R6 in section 7. A short repeat at R6 would help the owner, but this does not block.
3. The long-input confound (Q-002 §3.3) is still not in the pre-mortem. I had already marked this as not required.

*Orchestrator's note:* the Critic asked for confirmation from the diff. `git diff HEAD~1` of commit "Problem statement: label the transfer judgements…" on cos/p001-discovery-2 changes only docs/PROJECT.md, in the twelve replaced lines named in the round-3 message; nothing else changed.
