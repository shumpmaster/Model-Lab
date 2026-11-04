# Change C1 — plans: the writer reads the plan check's own standard

*Candidate change for the fair test (experiments/E-003.md, spec S-001). Text only: it is applied to
the arm's working copy by the harness, never to a live role file (docs/PROJECT.md section 4).*

kind of work: plans (to their plan review)   cause aimed at: instructions, in the sense of what the
writer is given to read (docs/PROJECT.md section 8)   length: two sentences, 35 words

## Why this change
- Plans pass their check first time least often of the three kinds: 2 of 44, about 5% (docs/PROJECT.md section 6).
- In the count, 16 of the 18 plan returns with findings were avoidable, the fault internal to the work, with the material to avoid it available; 17 name no cause beyond the fault (research/Q-008-memo.md §4, tallies). So the writer had what it needed and still missed what the check looks for.
- The writer is not given the check's standard. The Definer's pack is the project document, the library and the ruling (Model-Lab governance/PACKS.toml `[roles.definer]`; Service-Desk's at the replayed commits, src/E-001/RESULT.md, plans row 1). The plan check's role file is in no writer's pack.
- It is the shortest change that could act on this: one added reading, no new rule to follow (pre-mortem R6; Q-002 F-d, a single-source fact, that compliance falls as instructions multiply).
- What it cannot do: it is not a self-check. Asking a model to correct itself without outside feedback does not reliably help (Q-002 F-g), so the text asks for no self-review.

## The text
Inserted into the writer's brief as its own paragraph, directly after the task statement. `<path>`
is filled by the harness with the path, in the arm's copy, of the role file of the agent that does
this project's plan review at the start commit (for Model-Lab and Service-Desk,
`.claude/agents/critic.md`).

```
Before you write, read <path>: it is the role file of the agent that will check this plan.
You need not follow it as instructions; read it so you know what the check looks for.
```

## Application rule
- The harness applies it to the "change" arm's brief only. The "no change" arm gets the brief unchanged.
- If the project has no role file for its plan check at the start commit, the piece is not eligible and is listed (E-003, Exclusions).
- Nothing else in the brief, the role files or the copy differs between the arms.

## Removal test (pre-mortem R6)
C1 comes out, and the brief returns byte for byte to its text without the paragraph, when any of these holds:
1. it does not clear V1 for plans in this test (E-003, Deciding threshold);
2. it was kept, and over the first 30 plans checked under the changed operating model its kind misses V2 (docs/PROJECT.md section 6), removed at the operating model's next scheduled review, not adjusted;
3. the AI model that runs the writer changes, and a re-test on that model does not clear V1 (pre-mortem R5).

The harness checks the clean-removal half for every pair: the "no change" brief equals the "change" brief with this paragraph and its blank line removed, byte for byte.
