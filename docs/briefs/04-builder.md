# Brief 04 — builder — Service-Desk: add Model-Lab to the desk

session: session_01QBwHGJH9m3A4Ray7WpHzBo
model: claude-opus-5-5
recorded: from the helper's own transcript, 2026-11-01, after the owner's ruling (decisions/questions/P-001-session-records.md)

## Brief (2026-11-01T17:01:56.992Z)

You are the Builder for the Service-Desk project at /home/user/Service-Desk (read its AGENTS.md, CLAUDE.md and your agent file .claude/agents/builder.md first). This is one of the desk's four settings jobs after launch, "adding a project" (S-001 AC26; ruling L-0020 in docs/LEDGER.md; procedure in docs/handover/desk-operations.md, "Adding a project").

Brief:
- Add the project `Model-Lab`, repository `shumpmaster/Model-Lab`, default branch `main`, model `v3`, to src/config/projects.json. It is a new v3 project (the owner's work repository for two operating-model improvement projects; it has no deploys and no product page). Only one project plans, so `planning` is false. It has no deploys, so `deploysNeedOwner` is false or absent as the schema allows. Give it `webCommitsToDefault`, `contentPrefill` and `contentParam` the same as the other entries. Leave `actionsUsage` out unless the schema requires it. Check every field against the config validator and the spec's J7 join sheet, and say in your return what you chose for each and why.
- Keep everything else unchanged: no other project, no page code, no wording.
- Regenerate whatever the build generates from the config (src/tools/build.mjs), so generated copies stay in step.
- Run the full suite (`npm --prefix src ci && npm --prefix src test`, and `node src/tools/build.mjs`) and the governance checks (`governance/checks/check_all.sh .`). If an existing test asserts the exact project list, do not edit any locked or acceptance test yourself: report it as needing the check author's change, with the file and line, and stop before committing.
- Work in a worktree: `git -C /home/user/Service-Desk worktree add /home/user/sd-add-model-lab -b build/builder/add-model-lab origin/main` (fetch main first). Commit as `git -c user.name=builder -c user.email=builder@agents.invalid commit`, message ending with a trailer paragraph: `Agent-Session: session_01QBwHGJH9m3A4Ray7WpHzBo` and `Spec: S-001`. Do not push and do not open a pull request.

Return the six-part contract: changed (by file) · why · verified (command + output) · undone · needed outside your surface · open questions.

## Follow-up 1 (2026-11-01T17:01:57.008Z)

<system-reminder>
Your final report is delivered through SubagentHandback: when your work is complete, call SubagentHandback({message: <your full report>}). The call ends your run, so make it your last step. Only a SubagentHandback call reaches your caller as your result; plain text you write at the end is not delivered. Do not also send the report with SendMessage: your caller would get it twice.
</system-reminder>

