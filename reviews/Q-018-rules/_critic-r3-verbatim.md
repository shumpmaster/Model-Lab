# The Critic's third re-check of S-002's corrected counting rules (brief 293)

*Recorded verbatim by the Orchestrator; the verdict file is reviews/Q-018-rules/critic.md. Brief 293 (docs/briefs/293-critic.md), on Model-Lab@a5d1893, the rules as corrected by brief 292 (commit c03fa8f, merged at 63d66de). The Critic runs on a different model from S-002's writer (D-056) and apart from the Researcher.*

Verdict: PASS

**In plain words.** The blocking fault is fixed. RT5 now reads each record's own statement of what it is before it looks at the file name. Records that say they are part of a value target (trial-gates, two-look-line) are now left out until the owner rules on Open question 3. The stop-rule choice whose name holds "build-gate" (build-gate-stop) is now counted. Every other record the Definer listed gives the result RT5's definition calls for, and so do the two sample cases, ML#92 and ML#47. Findings 2 to 7 are each fixed. Both places where the Definer did not use my wording are sound, and its finding-6 wording is more accurate than mine was. Four non-blocking points remain. The first is an example count in the new branch rule: it says one branch heads 8 merged pull requests, but only 5 were merged by the cut-off. That number came from my own earlier finding, so it implicates my check. The other three are small wording gaps. The draw, the sample, the seed, the cut-off and the edge-case filters are untouched.

**Self-implication (D-050):** finding 1 below repeats a miscount from my brief 291 check (reviews/Q-018-rules/_critic-r2-verbatim.md:32, "heads 8 merged pull requests"). I did not apply the cut-off when I counted. Triage should note it.

## Findings

**1. Non-blocking (self-implication). specs/S-002.md:59: "`claude/chief-of-staff-discovery-yh4eyi` heads 8" does not hold under the same sentence's own rule.**
- The rule says "merged by the cut-off".
- The cut-off is 2026-11-12 00:00 UTC (:84).
- Service-Desk.list.jsonl:324-334 shows that #356 (merged 2026-11-12T00:17:24Z), #360 (01:13:12Z) and #361 (03:29:53Z) merged after the cut-off. So by the cut-off the branch heads 5: #348, #350, #353, #354 and #355.
- The rule's result does not change, because 5 is still more than one.
- Fix: write "heads 5 by the cut-off".

**2. Non-blocking. specs/S-002.md:254, question 13's reason against option (b) goes a little too far.**
- The text says "(b) would need a field no record gives".
- But P-001-open-unknowns's class sentence names its definition-of-ready item in the same sentence: "(OPERATING_MODEL.md §4, definition of ready item 7)" (decisions/questions/P-001-open-unknowns.md:3). A coder could read (b) from that.
- The fairer wording: no record's class names a definition of ready, so (b) would rest on a citation that comes after the class, not on the class itself.
- The options, the recommendation and the rest of the reasoning are fair.

**3. Non-blocking. specs/S-002.md:51, two coding gaps in the class reading.**
- (i) "Names other rulings too", the trigger for listing a record in rule (b), is not given as a test. For example, it does not say whether "its ceilings" in P-002-design-gate's class counts as another ruling.
  - This changes no result, since such a record is left out either way. It only affects the listing.
  - Simplest fix: list every class that is not exactly "A phase gate", "A value target" or "Part of a value target".
- (ii) "The sentence of its `Asked:` line" sets no rule for where a sentence ends.
  - On every Model-Lab `Asked:` line I read, splitting at a full stop followed by a space finds the right sentence, including `….md. A phase gate, …` (P-002-design-gate.md:6) and the "or a proxy" form (P-001-build-gate.md:5, P-001-build-gate-terms.md:5).
  - So this does not block. It is worth one clause.

**4. Non-blocking. specs/S-002.md:51: I could not confirm the example `R3 (part of a value target, the owner's own ruling)`.**
- No current file in the three repositories holds a `RISK CLASS:` line with ", the owner's own". The only matches are S-002 itself and the Definer's worktree copy.
- It may be in a deleted question file. I had no git, so I could not check. If it is not, label it as made up.

## Brief item 1: RT5's class-first reading, case by case
- **trial-gates (in to out): right.** Its class is "Part of a value target" (decisions/questions/P-002-trial-gates.md:6), so rule (b) leaves it out.
- **two-look-line (in to out): right.** It has the same class (P-002-two-look-line.md:6).
- **build-gate-stop (out to in): right.** Its class is "A choice under the stop rule after the cards' third failed check" (P-001-build-gate-stop.md:5). Rule (a) counts it, and it is listed because its milestone is Design-6.
  - :51 no longer clashes with itself on this record: the clause "a ruling on a stop rule … is counted under RT1 whatever milestone" now agrees with rule (a).
- **P-002-target (in, unchanged): right.** It has no `Asked:` line and no question file ("recorded with no question file", P-002-target.md:5). The name test does not mark it, since "target" alone is not `value-target`. It is counted and listed under Discovery-2.
- **P-001-build-gate-terms (out, unchanged): right.** Its class is "Touches the value target (term 1) and a rule change (term 4)" (:5). It is left out whole and listed.
  - This leaves its rule-change part out as well. That is the cautious reading until Open question 3 is ruled, and the listing keeps it in view.
- **Both design gates and P-001-build-gate (out): right.**
  - P-001-design-gate.md:4 and P-001-build-gate.md:5 give "A phase gate".
  - P-002-design-gate.md:6's class names a phase gate and "a value target's terms" together with other rulings, so it is left out whole and listed.
- **Both value targets (out): right.** P-001-value-target.md:3 and P-002-value-target.md:6 give "A value target".
- **Service-Desk m3c-launch-gate (out by name): right.**
  - No Service-Desk decision record holds the class form today.
  - Its only question file's `RISK CLASS:` line (questions/P-003-baseline-proof.md:13) has no ", the owner's own" parenthesis.
  - Personal-Org-Operating-Model has no `decisions/` folder, and no question file there holds the form.
  - So rule (d), by name, applies to both. glance-waits-gates ("gates") and gate-card are still counted.
  - "As first added" I could not check (no git).
- **ML#92: right.** Its window runs from 02:25:28 to 02:38:01 (sample.jsonl:5). The decision record first added at 02:32:58 (label b3609d4c, named by its own file) falls inside it, and leaving trial-gates out removes that touch.
  - I could not tie the label to trial-gates myself, because I cannot compute SHA-1. The trial-gates record says it was filed in PR #91, and ML#92 adds or changes it, which fits.
- **ML#47: right.** The decision record first added at 21:44:54 falls inside the 21:06:47 to 22:14:29 window (sample.jsonl:10). But every file #47 changes is records or owner question or answer, so it is no piece by RP2 and nothing changes.
- **ML#43, #69, #93 and #98:** none of the moved records lands in their windows.
  - ML#93's in-window record named by its number is P-002-brief-stop ("filed in PR #93"). Its `Asked:` line has no class ("No default."), so it falls to its deleted question file's `RISK CLASS:` line, or else to its name. It is counted either way, unless that deleted file's class names a gate, which I could not check.
- **Can the class be coded from the records as first added?**
  - Yes for every Model-Lab decision record I read, apart from finding 3.
  - The fallback to the question file needs the git history of deleted question files, which I could not read.

## Brief item 2: findings 2 to 7
- **Finding 2: fixed** (see item 3 below).
- **3(a): sound** (:59).
  - The reuse cases are confirmed: #300 and #310 (list.jsonl:286, :295), and #348 to #361 (:324-334), with finding 1's count.
  - Skipping to the next named subject and listing the record is safe. A wrong pick, such as a statement whose next subject is a pull request it only compares with, is caught by the listing.
  - No record before the cut-off names either branch. The only ones that do are reviews/356 and reviews/360, both after the cut-off.
- **3(b): fixed.** "In a record with no heading, in that paragraph alone". It matches Service-Desk's reviews/S-001-trial-view-2/_build-review-round1-verbatim.md:1-3.
- **3(c): fixed.** "a `Verdict:` line (in any letter case)".
- **3(d): fixed.** The whole-word rule, the dropped `origin/` and the rule for hash prefixes are defined. The hash rule also settles the short-prefix gap I raised on the Definer's script.
- **3(e): fixed** (:60). Only words of the record's own kind (by path) are read, for a piece of that kind. This matches Personal-Org-Operating-Model's reviews/20/reviewer.md:4 and Service-Desk's reviews/77/reviewer.md:3.
- **Finding 4: fixed** (:47, :50). Sample line 67 (ML#98) is the only case with `"dispatch_from": "brief record"`.
- **5(a): fixed** (:108). "(step 6)" is now glossed.
- **5(b) and 5(c): fixed** (:107).
  - The step now asks for every merged pull request's number, head branch and own commits.
  - It states that `head_ref` is kept in clear in `<repository>.list.jsonl`, which matches the extract's README:9.
  - Own commits of pull requests outside the window are not in the extract yet. That is the widening the Definer lists as undone.
- **Finding 6: the Definer's wording is sound and more exact than mine.**
  - github_reads.json:5-7 shows SD#6's comment at 11:38:45, before its merge at 11:44:45 (sample.jsonl:38), and PO#11's at 01:11:23, before its merge at 01:51:56 (:42).
  - So 10 comments came before merging. My wording, "all 8 counted before merging", would have been false.
  - The 8 named (Service-Desk #11 ×3 and #78; Personal-Org-Operating-Model #18, #30 ×2 and #35) match reviews/Q-018/_critic-verbatim.md:53-60.
- **Finding 7: fixed** (:46). It now says from which later commit a record that names the piece only in an append is read.
  - A small gap remains: it does not say when a record starts to count that names the piece only by being one of its own files, through a later commit of the piece. I found no sampled case.

## Brief item 3: question 13
- It no longer argues Open question 3. It mentions question 3 only as the condition for the hold.
- The "stepping in" argument is gone, and trial-gates is no longer an example.
- Options (a) to (c) are kept, and there is a recommendation, (a).
- Its claims check out against P-002-target.md:5, P-001-open-unknowns.md:3 and P-001-time-and-limit.md:9.
- Finding 2 above has the one overstatement.

## Brief item 4: nothing else changed
- The diff's four hunks change only lines 46, 47, 50, 51, 59, 60, 107, 108 and 254 of specs/S-002.md, as the Definer said.
- Line 84 (the draw, the seed, the cut-off and the window) and the edge-case table (:86-105) are not in the diff.
- In step 3 (:107), the sentence on E-K2's filter reads the same, word for word.
- Only S-002 is in the diff, so the sample files are not touched by it.

## Six-part contract
- **Changed:** nothing; I hold no write tool.
- **Why:** brief 293, the re-check of brief 292's corrections on their cases (P-002, M8).
- **Verified:** with Read, Grep and Glob, I read:
  - the diff /tmp/claude-0/-home-user/b9b3c098-5ac2-5fab-85c9-5ae65240ab9c/scratchpad/s002-292.diff, specs/S-002.md (:18-44, :84, :244, :254), docs/briefs/292-definer.md and reviews/Q-018-rules/_critic-r2-verbatim.md;
  - in Model-Lab decisions: every `Asked:` line with "never a default", and P-002-target, P-001-build-gate-terms, P-001-build-gate, P-002-design-gate and P-002-brief-stop in full;
  - every `RISK CLASS:` line in the three repositories;
  - the class form in Service-Desk's decisions, and its gate-named files;
  - from the extract: sample.jsonl (dispatch, merge, file classes and the record fields for lines 5, 7, 10 and 67), Service-Desk.list.jsonl (the reused branches), github_reads.json and README.md:9;
  - Service-Desk reviews/S-001-trial-view-2 round 1, reviews/77 and the 356/360 branch mentions; Personal-Org-Operating-Model reviews/20; and reviews/Q-018/_critic-verbatim.md:48-63.
- **Undone:** I had no git and no shell, so I did not check:
  - the records "as first added";
  - the deleted question files' `RISK CLASS:` lines, including brief-stop's and the RT5 example;
  - the SHA-1 labels;
  - that commit c03fa8f changes only S-002;
  - the governance checks or surface_guard.
- **Needed outside my surface:**
  - The Definer: findings 1 to 4 (all non-blocking), at the next revision.
  - The Orchestrator: widen the extract for C1's statement test and for RT5's class field.
  - Triage: the self-implication flag on finding 1.
- **Open questions:** for the owner, 11 to 14, unchanged; question 13 now reads fairly.

Key paths: /home/user/Model-Lab/specs/S-002.md, /home/user/Model-Lab/decisions/questions/P-002-trial-gates.md, /home/user/Model-Lab/decisions/questions/P-002-two-look-line.md, /home/user/Model-Lab/decisions/questions/P-001-build-gate-stop.md, /home/user/Model-Lab/decisions/questions/P-001-build-gate-terms.md, /home/user/Model-Lab/decisions/questions/P-002-design-gate.md, /home/user/Model-Lab/decisions/questions/P-002-brief-stop.md, /home/user/Model-Lab/research/Q-018-extract/Service-Desk.list.jsonl, /home/user/Model-Lab/research/Q-018-extract/github_reads.json, /home/user/Model-Lab/research/Q-018-extract/sample.jsonl