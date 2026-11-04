# Change C3 — research: the source check returns a memo only for a fault it can show

*Candidate change for the fair test (experiments/E-003.md, spec S-001). Text only: it is applied to
the check's working copy by the harness, never to a live role file (docs/PROJECT.md section 4).*

kind of work: research (to its source check)   cause aimed at: the check itself   length: three
sentences, 64 words

## Why this change
- For research, the check is the largest cause the records name: 7 of the 14 research returns with findings, against 1 for the instructions and 1 for source access (research/Q-008-memo.md §4, tallies).
- Two of the check's seven came from what the checker could not open, not from the memo: the Model-Lab Q-005 first check ("no web item could be opened") and the Q-007 first check (only some hosts resolved). A third return, the later Q-002 to Q-004 check, is put down to source access, where the sessions could not open outside sources (Q-008 §4, research, Model-Lab). In each, sources that could not be opened ended in a return.
- The other five check causes are not reached by this text: a checker's own withdrawn error (Model-Lab Q-006), a standard missing a rule (SD Q-006, three returns), a pack missing the question file (SD Q-005, since fixed in Service-Desk's pack, Service-Desk governance/PACKS.toml `[roles.source-checker]`). C3 is aimed at a part of the check's share, and the record says so.
- The risk is plain: a check that forgives what it cannot open may pass claims no one verified. The test therefore counts a pass under C3 only where the held-back check, which must open the sources itself, also passes the memo (E-003, Measure).

## The text
Inserted into the source checker's brief as its own paragraph, directly after the task statement.

```
A source you cannot open is not by itself a fault in the memo. List each one as
"Not opened: <source>, <why>", and judge the claims that rest on it only by whether the memo
states its grade and that it was not opened. Return the memo only for a fault you can show from
what you opened or from the memo's own text.
```

## Application rule
- This change is to the check, not to the work. Each new memo is judged twice on the same text: once by the source check with its brief unchanged, once with this paragraph added. The memo itself is the real researcher's round-1 submission, unchanged.
- Nothing else in the two check briefs, role files or copies differs.

## Removal test (pre-mortem R6)
C3 comes out, and the brief returns byte for byte to its text without the paragraph, when any of these holds:
1. it does not clear V1 for research in this test, or it fails the false-pass guard (E-003, Deciding threshold);
2. it was kept, and over the first 30 memos checked under the changed operating model research misses V2, removed at the operating model's next scheduled review, not adjusted;
3. the AI model that runs the source check changes, and a re-test on that model does not clear V1.

The harness checks the clean-removal half for every memo, as for C1.
