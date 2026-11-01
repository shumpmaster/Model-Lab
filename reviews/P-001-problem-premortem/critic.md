Verdict: FAIL

The Critic's check of the problem statement (docs/PROJECT.md section 2) and the pre-mortem (section 7), on a different model from their writer (brief: docs/briefs/08-critic.md), verbatim. Recorded by the orchestrator. Session session_01QBwHGHrHnEvMNYgKDoaH8w, 2026-11-01.

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
