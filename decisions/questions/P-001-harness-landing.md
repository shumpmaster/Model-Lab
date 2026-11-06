Ruling: A — re-sign: the builder makes its three commits again with the same content, each signed with a label naming it as this session's builder; the reviewer confirms the content is byte for byte what it passed
Question: questions/P-001-harness-landing.md
Milestone: Build-2, Build-3

Asked: 2026-11-06, in the Chief of Staff's session session_01QBwHGNGKXFwvVVdzkei5aT, by the session's question tool, from questions/P-001-harness-landing.md (filed in PR #58; Critic: reviews/P-001-harness-landing/critic.md, PASS at round 2). No default. Reversible.

## The owner's words, verbatim
The owner chose: "A: Re-sign (Recommended)".

## How it is carried out
- The Builder remakes its three commits (3861b38, a42c2df, 9caff21) on a new branch from the same start (ed35668), same content and author, each signed `Agent-Session: session_01QBwHGNGKXFwvVVdzkei5aT/builder-90`.
- The Reviewer confirms each new commit's tree is byte for byte the tree of the commit it replaces, and that the guard passes on the landing.
- The harness then lands with a merge commit; later helpers of this project sign with a label naming their role and brief.
