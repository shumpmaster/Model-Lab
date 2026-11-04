# Change C2 — built work: the builder is handed its inputs by name

*Candidate change for the fair test (experiments/E-003.md, spec S-001). Text only: it is applied to
the arm's working copy by the harness, never to a live role file (docs/PROJECT.md section 4).*

kind of work: built work (to its build review)   cause aimed at: material handed over   length:
two sentences of fixed text (10 words) plus the list the harness fills

## Why this change
- Material handed over is the largest cause the records name for built work: 5 of the 16 built-work returns with findings, beside 11 with no cause named beyond the fault or the worker's own slip (research/Q-008-memo.md §4, tallies). Across all kinds it is the second-largest named cause, 8 of 21 (bottom line 4).
- Those returns came from inputs that disagreed or were not handed over whole: two owner rulings in conflict (SD HD1), a table that did not list what the build needed (POOM S-017), a spec that disagreed with its check (POOM S-014), records that changed under the work (SD PR 263, VT3) (Q-008 §4, built work).
- The builder is handed its inputs as broad patterns: the spec, the project document, every locked check and every check file (`tests/acceptance/**`, `checks/**`; src/E-001/RESULT.md, built row 1). Accuracy falls as inputs grow longer, well below the context limit (Q-002 F-c), so a short exact list may help the builder see the inputs that bear on its task before it builds.
- It is one added reading and nothing else. Round 1's draft also told the builder what to do when two inputs disagree; that was a second change, a rule to follow, and it is dropped, so that a gain can be put down to the list alone (pre-mortem R6; plan review round 1, finding 6).
- Some of these causes cannot be reached by text: inputs that change while the work is under way (SD PR 263, VT3) are left out of the test (E-003, Exclusions). C2 aims at the rest: at most 3 of the 16 built-work returns with findings. That puts its likely gain below the 20 points the test is sized for (S-001, "What the test can and cannot show").

## The text
Inserted into the builder's brief as its own paragraph, directly after the task statement.

```
The inputs for this task, by path: <list>. Read these first.
```

`<list>` is filled by the harness, mechanically, from files at the start commit only, as a
comma-separated list of repository paths in this order, each once:
1. the spec file the task names, with the line range of the stage or section the task statement cites, written `specs/<spec id>.md:<first line>-<last line>` (the whole file, with no range, if the task cites no stage or section);
2. every repository path the task statement names, expanded to files present at the start commit;
3. every ruling file under `decisions/` that the cited stage or section names;
4. every locked check file that names the spec's id (a `join-test: <spec id>/` marker or the spec id in its path).

Cases:
- **The task names no spec:** items 1, 3 and 4 are empty and the list is item 2 alone.
- **The list holds only the spec:** the piece is eligible and the list holds the spec alone.
- **The list is empty** (no spec and no path named): the piece is not eligible, since there is nothing to hand over, and it is listed (E-003, Exclusions 6).

The harness records the filled list with the pair.

## Application rule
- The harness applies it to the "change" arm's brief only. The "no change" arm gets the brief unchanged, with its usual pack.
- Nothing is removed from the "change" arm's pack: C2 adds a list, it does not narrow what may be read.
- Nothing else in the brief, the role files or the copy differs between the arms.

## Removal test (pre-mortem R6)
C2 comes out, and the brief returns byte for byte to its text without the paragraph, when any of these holds:
1. it does not clear V1 for built work in this test (E-003, Deciding threshold);
2. it was kept, and over the first 30 built pieces checked under the changed operating model its kind misses V2, removed at the operating model's next scheduled review, not adjusted;
3. the AI model that runs the builder changes, and a re-test on that model does not clear V1.

The harness checks the clean-removal half for every pair, as for C1.
