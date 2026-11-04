# Intake — P-001: the session environment's repositories, 2026-11-04

*Recorded by the Chief of Staff (session_01QBwHGMBo8kZsMCS2EvKNwd) as the record behind the held-back store question (questions/P-001-heldback-store.md), at the Critic's request (reviews/P-001-heldback-store/critic.md, round 1, finding 4). Observations of this session's tools, copied as they were returned.*

## The account's repositories and their visibility (the session's repository listing, 2026-11-04)
| Repository | Visibility |
|---|---|
| shumpmaster/Service-Desk | public |
| shumpmaster/Model-Lab | public |
| shumpmaster/Personal-Org-Operating-Model | private |
| shumpmaster/portfolio | private |
| shumpmaster/scratch | public |
| shumpmaster/fantasy-edge | private |
| shumpmaster/fantasy-edge-site | public |
| shumpmaster/Operations-Hub | private (archived) |

## This session's repositories (the session's own status, 2026-11-04)
The session was started with four sources: Personal-Org-Operating-Model, Service-Desk, portfolio and Model-Lab, each checked out under /home/user.

## How a session gets its repositories (the environment's documentation, page "github.access", read 2026-11-04), verbatim extracts
- "A session's repositories are chosen when it starts, so where you cannot attach one here, the person starts a new session with it selected."
- "Subagents you start share this container and cannot read it either"
- "Once access is fixed, add_repo, if you have it, attaches the repository to this session."

## What follows, and what is not shown
- Helpers started from a session share its machine, so they can read every repository that session holds.
- A repository chosen for one session is not thereby in another; nothing read here shows whether the environment's settings add a repository to every new session.
- A session's machine is reclaimed after a period of inactivity, so anything kept only in its own storage is lost (this session's operating instructions, 2026-11-04; not a file record).

## The held-back store (added 2026-11-04, after the owner's ruling, decisions/questions/P-001-heldback-store.md)
- The owner created the repository shumpmaster/secret-marking; the session's repository listing shows it private.
- It is not among this session's sources and has not been attached to it, so no helper this session starts can read it.
- Not yet shown: whether the environment's settings add it to new sessions (the owner's check, as the ruling says).

## Tools this session holds for starting and waking sessions (the tools' own descriptions, read 2026-11-04)
*Observations of the Chief of Staff's tool list, copied from the descriptions as given; not tested here.*
- `create_session` starts a new cloud session; it takes an optional `source_url` ("Optional git repository URL to check out") and `source_revision`, and `environment_id` ("Defaults to the calling session's environment"). A session it starts is told it was sent by this session.
- `send_later` schedules a message into this session at a future time: "Delivery survives container restarts"; "If a turn is running in this session when the message is due, the message waits".
- `create_trigger` creates a scheduled task that fires into this session, a named other session ("must be in your account"), or a fresh session each time; the minimum interval is normally hourly.
- `send_message` delivers a message to another session; "The call returns when the message is delivered, not when it is answered".
- `list_events` reads another session's transcript events (user messages, assistant responses, tool calls).
- Not shown by any of these: whether a session started with one `source_url` can still reach other repositories through its own GitHub tools, and whether a scheduled wake resumes a session whose machine was reclaimed with its working files intact.
