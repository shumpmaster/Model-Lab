# Ruling needed: the fair test's harness passed its review but a check refuses it, because its builder and the checks' writer signed with one session id

Milestone: Build-2, Build-3

The harness scripts passed their review, and with your correction of the one wrong check, every locked check passes on them. They cannot land yet. A check that keeps the checks' writer and the builder apart reads both as one session, because both helpers signed their work with this session's id, as their briefs told them to. They were two separate helpers on two different AI models. Landing the two changes one after the other does not help: the check looks at the whole history, and the corrected check is already in it. I said otherwise earlier, and was wrong. You decide how the record shows they were two. Nothing has been changed.

WHY: the check is enforced by CI and is not routed around; the builder's work cannot land until it passes or is exempted. The record of who did what is what this check exists to protect.
OPTIONS:
  A. Re-sign — the builder makes its three commits again with the same content, each signed with an id naming its own helper session under this one; the reviewer confirms the content is byte for byte what it passed. Gain: every check runs in full on the work, and the record shows the two helpers apart. Cost: the commits that land are not the ones the reviewer read, only identical to them; the signing form departs from the one the project's mechanics file gives, and later helpers would sign the same way. Rules out: nothing. Reversible: yes.
  B. Exempt — the three commits are listed as skipped by the check, with a ledger entry saying why; a change you rule on as high risk. Gain: the reviewed commits land as they are. Cost: those commits skip every check of their range, not only this one; the record still cannot show the two helpers apart. Rules out: nothing. Reversible: yes, by removing the listing.
  C. Rebuild — a new builder, started as a session of its own with its own id, builds the harness again to the same checks, and it is reviewed again. Gain: nothing set aside or skipped. Cost: the build and its review again, which took about 1.3 and 1.0 million tokens this time, and three new review rounds. Rules out: nothing. Reversible: yes.
RECOMMENDATION: A, with medium confidence (the Chief of Staff's judgement): it keeps every check running and makes the record say what happened; B hides the commits from all their checks, and C repeats a build that passed. What would change it: wanting the exact commits the reviewer read to land (then B), or wanting no change to how helpers sign (then B or C).
WHO HAS CHECKED IT: the Reviewer found the shared signature; the Chief of Staff read the check's code for why landing separately fails; the Critic checks this card.
RISK CLASS: R0 (questions/**)   REVERSIBILITY: reversible   BLAST RADIUS: when the harness lands; A also how every later helper signs; B the exempt list and the ledger
DEFAULT: none, since each option bears on how a CI-enforced check is met, which only you rule   TIMEOUT: none

## Context
- The harness passed the Reviewer at round 3 (source: reviews/S-001/_reviewer-build.md)
- With the corrected check, the whole locked suite passes on the harness (source: reviews/57/reviewer.md, section 1)
- The check refuses one session that wrote both a spec's checks and its code, looking at every commit reachable from the change for that spec (source: governance/checks/surface_guard.py, `independence_violations`)
- The Check author's and the Builder's commits carry the same session id (source: reviews/57/reviewer.md, finding 1)
- The two helpers ran on different models, from different briefs (source: docs/briefs/90-builder.md; docs/briefs/99-check-author.md, on branch claude/chief-of-staff-p001-build-5m9j1d)
- Exempted commits skip every check of their range; adding one needs a ledger entry and is high risk (source: governance/SURFACES.md, the exempt block; governance/checks/surface_guard.py, `range_violations`)
- The project's mechanics file gives the signing form as the session id (source: CLAUDE.md)
- The first version of the lesson on this proposed landing separately, which the check's code rules out (source: docs/LESSONS.md LL-65, on branch claude/chief-of-staff-p001-build-5m9j1d)
- The build used 1,340,245 tokens and its review 964,635 across three rounds, as reported (source: sessions/chief-of-staff/session_01QBwHGNGKXFwvVVdzkei5aT.jsonl)
