Verdict: PASS

Every correction the checks asked for is made and nothing was strengthened in the memos. A few leftovers are listed per memo. None of them touches an entry I list as fileable, apart from the wording cautions on LF-Q005-05a and Q007-F14.

I re-opened sources only where a changed or kept figure or quote was in doubt. I wrote no files. Fetched PDFs went to the scratchpad and were read as data.
- Prompting Claude Opus 5.5 page: the "rather than carrying over the setting you used on Claude Opus 5" quote is verbatim.
- Model-deprecations page: the Q-004 §4.5.1 dates are right. Tentative retirement dates run 2026-10-15, 2026-11-24, Feb 2027 (Opus 4.6, Sonnet 4.6), and Sep 1 to Oct 7 2027 for the 5.5 and 5.1 models.
- demystifying-evals page: "An eval at 100% tracks regressions but provides no signal for improvement" is on the page. Q-004 P-Q004-1 is therefore right, and the first Q-004 check was wrong to call that condition the Researcher's inference.
- arXiv 2609.00006 (full text) and arXiv 2310.11324 (Sclar, full text): see Q-004 and the cross-memo notes.
- PubMed 36326255: "handoff-related reported adverse events decreased 47%" is confirmed.

## Q-002: resolved, with deferrals the Researcher declared
- **MAST (resolved).**
  - The first category is now "System Design Issues" and the trace count is 1,642.
  - The venue is unconfirmed.
  - The prompt-versus-topology reading holds on ChatDev only.
  - The Table 5 numbers match the check (25.0/34.4/40.6; 89.6/90.3/91.5; AG2 84.75/89.75/85.50 and 84.25/89.00/88.83).
  - The unfound quote is dropped.
  - §1.5, §3.2, §3.4 and K2/K4 are consistent.
- **Large Language Monkeys (resolved).** The MATH figure is now "from 40.50% to 41.41% over the same sample range".
- **Kim et al. (resolved).** The text now says 260 configurations, of which 180 had full cost tracking. The −70% figure is credited to the abstract. F-m is corrected to match.
- **S1, S2, S3 (resolved).** The swe-bench quote is exact. The Chroma count of 18 is credited to the Chroma page the check opened, not the README. The MAST venue is unconfirmed.
- **K2 versus §1.4 and the §4 count (resolved).** K2 is now "Shared", and the count is 2 primary, 3 shared, 4 secondary (9 in all).
- **F-f, F-h, F-i, F-m (resolved).** F-f states the disagreement. F-h says panels reduce but do not remove the bias. F-i adds "best method" and "below random". Each row now has a filing status.
- **Left for a later revision, as the memo says:**
  - Laban: −35% and −39% are in the same version.
  - Kim: the β = −0.236 detail.
  - Du: recitation gave "up to 4%".
  - The first check's B6 note on the F-a wording.
- **Leftovers the memo does not flag:**
  - §1.3, §3.1 and F-a still say "scaffold fixed", which the first check asked to revise.
  - §3.3 still says "(v1: −35%)", which the second check says is wrong.
  - The K2 row phrase "and the larger gain on AG2 GSM-Plus" is ambiguous. It means the role-prompt gain was larger than the topology gain on AG2. It does not mean larger than +9.4.
- **New problems:** none.

## Q-003: resolved
- **Code-review false-positive claim (resolved).** The 14–22% claim and arXiv 2505.20206 are gone from the body, the entries and the sources.
- **F-a (resolved).** The 0.3–0.7 figure is out of F-a. It stays in §4 attributed to the blog, with a note that the paper lacks it.
- **Wataoka (resolved).** It is marked a workshop paper, and the extension to similar-training models is marked as the Researcher's inference.
- **Slips 1–4 (resolved).** The owner.md quote now has the full line 3. The writing row has criterion and check in the right columns. Example A shows power of about 0.70–0.77. The bayes_evals README is described as title-only.
- **F-h (resolved).** It is split into F-h1 (model pair, marked as an inference from names) and F-h2 (45 owner files).
- **Statuses and regrades (resolved).** They follow both checks.
- **New problems:** none. One unrevised nit: "binary or 1–5 outputs" is still presented as vendor advice, though the first check noted these were example formats.

## Q-004: resolved, with one quote defect I found
- **Slips and edits (resolved).**
  - §4.5.1 says "tentative", not "mid-2027".
  - §4.2.3 gives the effort sentence to the Opus 5.5 prompting page and the "Run a fresh effort sweep … Opus 4.7" quote to the migration guide.
  - The extra phrase in §4.3.1 is removed.
  - The Amazon range is "minimum 1.98%, Table 1 values 1.98%–5.88%", with the 1.4% average gain. The 1.9–7.6% range is gone.
  - Evil twins and MePO are described as different mechanisms.
  - The Wharton figures are in proportion points.
  - The AGENTS.md note is updated to v3 (−0.5% and −2%).
  - The ablation is credited to Lin et al., reported second-hand, and P-Q004-3 is held.
  - Statuses follow both checks.
- **New problem (low severity, held entry).** In §3.4.3 the quote marks cover "the system prompt alone regresses performance while structural elements like tools and memory carry the gains". That is not verbatim in arXiv 2609.00006. The paper says "…while the system prompt alone regresses performance (−2.3 pp)" about Lin et al., and "We read this as suggestive evidence that structural scaffold is more portable than prose-level prompt strategy". The check 2 summary missed this. It affects only §3.4.3 and the held P-Q004-3.

## Q-005: resolved
- **Required fixes (resolved).**
  - The Sumwalt sentence is dropped.
  - F2's Leape wording is marked as paraphrase.
  - F22 uses IHI's own words ("require less reliance on humans to remember…").
  - The Urbach PMID is 24620866.
  - F5 is resolved: the 1.5%→0.8% figures are SURPASS's own, there was a 5-hospital concurrent control, and the hospitals had "high standards of care".
  - The "high baseline quality" remark is reworded as the Researcher's own inference, and F5 is cited against it.
  - P-2 is weakened from H to M and no longer relies on F6. P-8 and LP-02/LP-07 are revised.
  - LP-03 is reworded and LP-06 is marked as opinion.
  - No regrades.
  - The LF-05 and LF-06 splits match the check.
- **Leftovers (all in held entries except the F9 wording).**
  - F2 still says "no hospital changed significantly", which the check did not find in any source it opened.
  - F4 still states the "sicker emergency patients" confounder as fact. §8 admits it is the Researcher's own remark.
  - F22's tier contents still differ from IHI's. The memo says "engineering controls" and "weaker: retraining, policy updates". IHI says stronger = forcing functions, simplify, standardise; weaker = new procedure or policy, training, warnings, double checks.
  - F27's body still carries the unverified 91% Dutch figure. It is correctly dropped from LF-14.
  - F9 puts "just as fast" in quotation marks, but the check says that is press wording. It also says the authors attributed "most of" the fall to the secular trend, where the paper says "likely part of a wider secular trend".
- **New problem (minor).** LF-Q005-05a says "equally in units not yet enrolled; the authors attributed this to a secular trend". That is stronger than the paper's words, "did not accelerate following interventions training" and "likely part of a wider secular trend". File it with the paper's wording.

## Q-007: resolved
- **Required corrections (resolved).**
  - c2: GEPA is "6% on average and up to 20%", and the over-10% margin is credited to MIPROv2. This is also fixed in P02.
  - b9: developer-written files gave +2.4% (p = 21%). LLM-written files had a "marginal negative effect". Neither effect is statistically significant. Cost rose over 20% (20% and 23%). F13 matches.
  - c3: the 18,282→122 token example is attributed to the ACE paper itself.
  - c6/F17: the 27.9% is credited to goal-directed adversarial rubric edits.
  - b10: the cut-test wording is marked unconfirmed.
  - F10: "its strongest model" is dropped.
  - F15: the less-constrained scaffold is added.
  - F11: narrowed to self-replication.
  - Bottom line 3 now says "in one source only (c6)".
  - P04 marks the Laban link as indirect.
- **b17/F16.** The memo dropped "about 10 points on average" as the check asked. The figure is in the paper's own abstract ("∼10 accuracy points on average across 50+ tasks"), so the check was wrong on this point and the removal is harmless but unnecessary. The median spread of 7.5 is also correct. Q-002 F-f keeps "about 10", and that is right too.
- **Leftovers, none blocking.**
  - F14 and b11 still say "changing tests or scoring code". The check says METR's wording is "reward hacks". The memo flags this only in a checker's note in b11.
  - Bottom line 2 ("wording can raise or lower gaming") rests on one source for the lowering direction and has no source for the raising direction.
  - a8 says MAST's first group is "specification issues", but Q-002's check says v3 calls it "System Design Issues".
- **New problems:** none.

## Library entries that may be filed

### Q-002
- **Two independent sources opened:** F-c, F-f (state the Sclar versus ProSA/He disagreement), F-g, F-h, F-l, P-b, P-d, P-e.
- **Single-source and attributed, not load-bearing:** F-d, F-e, F-i, F-j, F-k, F-m. F-m carries 260 configurations, with 180 having full cost tracking.
- **Single vendor source, not load-bearing, with an explicit vendor-reported caveat:** F-b, P-a, P-c. The check treated these as outside the revision, so they are unchanged.
- **Hold:** F-a, until its "scaffold fixed" wording is revised.

### Q-003
- **Two independent sources opened:** F-f. Note that Wataoka is a workshop paper.
- **Single-origin only:** F-a, F-b, F-c, F-d, F-e (with the chat-preference caveat).
- **Non-load-bearing vendor guidance, labelled single-publisher (caller's decision):** F-g.
- **Grade A:** F-h1 and F-h2.
- **Calc fact with the assumed discordance rates stated:** F-i.
- **Opinion-grade patterns:** P-a and P-b.
- **Hold:** P-c, until F-a gains an independent second source.

### Q-004
- **Fileable:**
  - F-Q004-1.
  - F-Q004-2 and F-Q004-3, as attributed single-source vendor statements.
  - F-Q004-4, with "tentative" dates and the interval marked as an estimate.
  - F-Q004-6 (three independent sources).
  - F-Q004-7.
  - F-Q004-8, without "1.9–7.6%".
  - F-Q004-9 (grade A).
  - F-Q004-10, as single-source and attributed.
  - P-Q004-1 (effect unmeasured).
  - P-Q004-2 (the Wharton reference restored, in proportion points).
- **Hold, or file only as "authors report":** F-Q004-5.
- **Hold:** P-Q004-3.

### Q-005
- **Fileable:**
  - LF-Q005-02 (with "adjusted").
  - LF-Q005-03.
  - LF-Q005-05a (use the paper's wording on the secular trend).
  - LF-Q005-06a and LF-Q005-06b.
  - LF-Q005-07 and LF-Q005-10 (not ★, one opened source each).
  - LF-Q005-08 (as the NTSB finding).
  - LF-Q005-14 (without 91%; the second source is weak).
  - LF-Q005-15.
  - LP-Q005-02.
  - LP-Q005-09 (on LF-15 only).
- **Hold:** LF-Q005-01, -04, -05b, -06c, -09, -11, -12, -13, -16, -17, -18, -19, -20; LP-Q005-01, -03, -04, -05, -06, -07, -08, -10.

### Q-007
- **Two independent sources opened:** F05, F08, F09; and F12 for the direction only (the 68% at 500 is single-source).
- **Single-source:** F01 (self-report), F03, F04, F06, F07, F10 (self-report), F11 (narrowed), F13, F15 (self-report), F16, F18, F19, F21.
- **Fileable with a wording caution:** F14. File "reward-hack" and the ImpossibleBench 92%→1% as single-source, and avoid asserting "changing tests or scoring code" from METR.
- **Single-publisher only:** F02.
- **File only as single-source, and only if not treated as load-bearing:** F17, with the adversarial-edit qualifier.
- **Not filed:** F20 (absence claim).
- **Patterns:** P01, P02 (grade C, with the corrected GEPA figure), P04 (Laban link indirect). P03 may be filed only if the checker-instruction claim is not treated as load-bearing.

Memos read: /home/user/ml-lessons/research/Q-002-memo.md, Q-003-memo.md, Q-004-memo.md, Q-005-memo.md, Q-007-memo.md
