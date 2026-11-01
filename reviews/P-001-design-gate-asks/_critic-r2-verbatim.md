The Critic's round 2 on four Design-gate questions (brief: docs/briefs/12-critic.md), on a different model from their writer, verbatim. Recorded by the orchestrator. Session session_01QBwHGHrHnEvMNYgKDoaH8w, 2026-11-01. Not a verdict file (its name starts with `_`); each question's verdict is in reviews/P-001-<question>/critic.md.

---

Verdict: PASS

All four questions pass in round 2. Every blocking finding from round 1 is resolved. Three of the remaining non-blocking findings carry over, and I raise three new non-blocking ones (desk-follow-ups 3 and 4, spend-ceiling 1). I re-read each whole file on cos/p001-design-gate-asks, and read LL-28 at /home/user/wt/ml-orch/docs/LESSONS.md.

P-001-desk-follow-ups: PASS
- Round 1 finding 1 (blocking, LL-28 missing): resolved. LL-28 now exists at lines 218-224. It records the portfolio pull request that the desk does not show, the uncounted library patterns, and the workaround of the Chief of Staff sending the link. That supports gap 3 and Context bullet 4, which now also cites RARE_DIRS.
- Finding 2 (milestone): resolved. "Milestone: M6" fits "Every slip in this work corrected", and the question fixes LL-21, LL-23, LL-25 and LL-28.
- Finding 3 (gap 6 presented as settled): resolved. Gap 6 is now "An open question for you inside this work" and Context bullet 6 matches the reviewer's Q2/N1.
- Finding 4 (default A): resolved. The card now says that "If this question defaults to A, nothing starts before the Design gate … a default is never your ruling." DEFAULT: A with TIMEOUT: 72 is allowed for a reversible question.
- Finding 5 (the cited critic record): resolved, per your note that the verdicts are now recorded.
- Finding 6 (background length): still open, non-blocking. The WHY and the six-gap list are long but readable.
- New 1, non-blocking: gap 6 is an owner question (should deploy approval be enforced for the Service Desk only, or open to any project). None of options A to C answers it, since they only route work. Say that it is carried into the new desk item. The claim "Today the check allows either" has no cited record beyond the reviewer's question.
- New 2, non-blocking: "The workarounds already cover the gaps that could hide work waiting on you" now rests on LL-28 and LL-23, which are in the log. Gap 2 has no workaround, and the card says so through its recommendation line.

P-001-researcher-web: PASS
- Round 1 finding 1 (blocking, evidence misstated): resolved. The recommendation is now A. It quotes the memo's "structural limits on what each role reads and can do … rather than wording alone", which matches Q-007-memo bottom line 2. It also quotes the pattern "Keep untrusted-text readers without tools and pass on only structured results", which matches Q-007-P01. It states that this is the Input reader's design. Context bullet 5 quotes the source whole.
- Finding 2 (the Source checker not shown to catch injected claims): resolved. This is now stated in option B's cost and in the "what would change it" line.
- Finding 3 (background length): resolved. The background is now two short paragraphs.
- DEFAULT none and TIMEOUT none are still right for a rule change. Options A to C are even, and the facts are unchanged and supported (researcher.md line 4, L-0005, F08, F09).
- New findings: none.

P-001-spend-ceiling: PASS
- Round 1 finding 1 (blocking, REVERSIBILITY label): resolved. The label now reads "costly (the ceiling can be changed; money spent under B is not returned)". "costly" is a valid word, and the asks-merge check will not treat the question as reversible. Option B now says "Reversible: the ceiling can be changed later; money spent is not returned."
- Finding 2 (blocking, unsupported option C): resolved. Option C is removed. The WHY ("the brief cannot go to the Design gate") is now consistent with the two remaining options.
- Finding 3 (spent nothing so far): resolved. The line is removed.
- Finding 4 (pay-as-you-go and the no-timeline ruling): resolved. B now says "if your plan offers paid usage beyond its limit", and the timeline reasoning is labelled "the Chief of Staff's reading".
- DEFAULT none and TIMEOUT none are right. The facts check out as in round 1.
- New 1, non-blocking: "The ceiling can be raised later if the test's budget at the Build gate needs it" has no cited record. The model allows the owner to change a ceiling, but nothing cited says so.

P-001-library-rules: PASS
- Round 1 finding 1 (PR #3 could not be opened): resolved. The bullet now also cites Q-007-memo.md lines 10 and 15 and library/README.md, which support the claim. I still could not open PR #3 itself.
- Finding 2 (label set incomplete): resolved. Option A's labels now include "a primary record opened" and "opinion (for patterns)".
- Finding 3 (the second idea "will use the library most"): resolved. Option C now says only that the second idea "gives evidence on how the library is used".
- Finding 4 (WHY length): still open, non-blocking.
- DEFAULT none and TIMEOUT none are right, and the count of 88 is correct. No new findings.
