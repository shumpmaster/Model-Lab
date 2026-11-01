# Brief 08 — critic — the problem statement and pre-mortem, read cold

session: session_01QBwHGHrHnEvMNYgKDoaH8w
model: claude-sonnet-5-5 (the writer, the Chief of Staff, runs on claude-opus-5-5; D-056)
recorded: at dispatch, 2026-11-01 (LL-04, LL-24)

## Brief

You are the Critic (your role file: /home/user/Model-Lab/.claude/agents/critic.md). Today is 2026-11-01. Check two drafted parts of the project document /home/user/wt/ml-cos/docs/PROJECT.md (branch cos/p001-discovery-2): in section 2, the paragraph starting "**The problem, stated without reference to any industry**" and the list "How other fields solved it" under it; and in section 7, the "**Pre-mortem**" paragraph and table. Read nothing else of the project document beyond what you need to understand those parts (the milestone lines in section 3 may be read, since the drafts refer to M1 to M3).

The standard they must meet (/home/user/Personal-Org-Operating-Model/OPERATING_MODEL.md):
- §6 "The knowledge method": the problem is stated in industry-free terms; the search for fields that solved it is reflected; every borrowed principle gets a transfer check on its conditions.
- §4 standard milestones "The right problem chosen" (a plain problem statement, checked against how others have solved it) and "The risks are known" (the pre-mortem; its risks shape the research).
- Neutrality (D-055 spirit, and the project's lessons LL-02 in /home/user/Model-Lab/docs/LESSONS.md): the problem statement does not presuppose that changing instructions is the answer; benefits and risks are put evenly.
- Every cited claim is supported by the research memo section it cites: open /home/user/Model-Lab/research/Q-002-memo.md, Q-003-memo.md, Q-004-memo.md, Q-005-memo.md, Q-006-memo.md, Q-007-memo.md and research/Q-002-to-Q-007-corrections-confirmation.md as needed, and check that each claim says no more than its source. Flag anything resting on an entry the confirmation holds back.
- The pre-mortem covers the failure modes the research names that a reader would expect (for example, gaming of checks, over-fitting, model change, too small a test, records that cannot show causes); flag any important one missing.
- Plain enough for the owner, a smart non-expert.

Write no files. Return as your final message a record whose first line, in column 0, is exactly `Verdict: PASS` or `Verdict: FAIL`, then numbered findings, each marked blocking or non-blocking, with the words concerned and what is wrong (do not rewrite the text).
