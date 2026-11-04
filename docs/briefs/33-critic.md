# Brief 33 — critic — Design's join-up review for S-001 (Design-5)

session: session_01QBwHGMBo8kZsMCS2EvKNwd
model: claude-sonnet-5-5 (the plan's writer, the Definer, ran on claude-opus-5-5; D-056)
recorded: at dispatch, 2026-11-04 (LL-04, LL-24)

## Brief

You are the Critic (your role file: /home/user/Model-Lab/.claude/agents/critic.md). Today is 2026-11-04. A fresh session, read-only: you edit nothing, commit nothing, push nothing; your return is recorded verbatim by the Orchestrator.

Your task is the join-up review closing Design for the project P-001 in /home/user/Model-Lab (at commit 5bb3727, branch claude/chief-of-staff-design-u3hdz2), in the form of docs/design/JOIN_UP_REVIEW.md, "Design" part, as your role file's plan-review paragraph describes. The plan review of specs/S-001.md passed at round 3 (reviews/S-001/plan.md) without this section; you are adding it, not re-running the plan review.

The project has no screens or views; say so in one line. Its design is a set of parts that must fit together, so check them side by side, never one at a time: specs/S-001.md (criteria, join sheets J1 to J8, Needed outside, Areas touched); experiments/E-003.md; experiments/E-003/check-author-extract.md; experiments/E-003/C1-plans-read-the-check.md, C2-built-named-inputs.md, C3-research-check-what-it-can-open.md; the new per-task pack `[roles.S-001-holdout]` at the end of governance/PACKS.toml, beside `[roles.check-author]` (read only those two tables of that file); governance/HOLDOUTS.md; the role files and playbook the extract names (.claude/agents/critic.md, reviewer.md, source-checker.md; docs/playbooks/); and the project document's milestones M2 to M4 and section 6 (docs/PROJECT.md). Where a join depends on how a tool resolves a record, you may read governance/checks/session_runner.py and governance/checks/govlib.py.

Fill the form's Design table with these checks, adapted to parts instead of screens:
1. One meaning per term, threshold and id across the parts (a pair, a run, a kind, a held-back check, the deciding pass, the judge).
2. One route: each piece of work and each record passes between parts by one path, and each join sheet's two ends say the same thing about it.
3. Consistent names, paths and ids: every path or id one part names exists in the part it points to, as named.
4. No two parts doing the same job, and no job without a part.
5. Every datum the design needs is available from the records, or listed as a needed change.
Rate each difference as a finding: blocking (the parts cannot work together as written) or non-blocking (carried into the Build gate's case as a risk). A blocking one fails the review.

Return, first, a column-0 line `Verdict: PASS` or `Verdict: FAIL`; then the section, headed `## Join-up review — Design, 2026-11-04`, in the form's Design part, with the Sign-off line left as the form has it; then numbered findings, each with file and line and marked blocking or not; then the six-part contract.
