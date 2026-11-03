# Environment check before Design — P-001 (2026-11-03)

*The environment assessment the lessons log asks for before work that depends on the session's environment (LL-22), run by the Chief of Staff at the start of Design, session session_01QBwHGN4kVVA3rfHx2b4FsF.*

## What Design needs
1. **Replay (U2):** past tasks re-run at the repository state they started from, so each repository's full history must be readable.
2. **Judge consistency (U3):** the same work judged more than once, by judges on a different AI model from the work, within the existing plan (docs/PROJECT.md section 8, the outside-judges constraint).
3. **Records of past tasks:** briefs, review records and research memos (research/Q-008-memo.md names the strata).
4. **No outside sources:** neither check reads the web.

## What was found
| Need | Result | How tested |
|---|---|---|
| Full history | Model-Lab (216 commits from 2026-11-01) and portfolio (18) were full clones. Service-Desk and Personal-Org-Operating-Model were shallow; `git fetch --unshallow` succeeded: Service-Desk 2,232 commits from 2026-09-30, Personal-Org-Operating-Model 844 from 2026-09-24. A fresh session must unshallow again (each session clones fresh). | `git rev-parse --is-shallow-repository`, `git rev-list --count`, `git fetch --unshallow` |
| Agents at a past state | A git worktree at any past commit can be given to a helper as its working directory. | Worktrees used this session (LL-19's practice) |
| Judge models | Helpers can be started on four models from one provider: Opus 5.5, Sonnet 5.5, Haiku 5.5 and Fable 5.1. All are the same provider, so U3's "different model family or provider" can be met only as a different model within it, unless the owner overrides the spend ceiling. Whether these count as different families is not established. | The helper tool's model choices |
| Usage figures | Each helper reports its tokens, tool uses and time at return; the session's own status gives context use and an estimated cost (LL-37). | This session |
| Network | Not needed for either check. | — |

## For the owner
Nothing needs changing in the environment for the replay and consistency checks. One limit to know: every judge comes from one provider, so the judges' independence is limited (pre-mortem R3); the registrations must say so.
