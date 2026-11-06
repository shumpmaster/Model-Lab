# Ruling needed: the fair test's harness passed its review but a check refuses it, because its builder and the checks' writer signed with one session id

Milestone: Build-2, Build-3

The harness scripts passed their review, and with your correction of the one wrong check, every locked check passes on them or is skipped by design. They cannot land yet. A check that keeps the checks' writer and the builder apart reads both as one session, because both helpers signed their work with this session's id, as their briefs said. They were two helpers on two different AI models. Landing the two changes one after the other does not help, as I wrongly said earlier: the check reads the whole history. You decide how the record shows they were two. Nothing has been changed.

WHY: the check is enforced by CI and is not routed around. The Chief of Staff leaves out changing the check itself, since it is a governance file and the operating model's change is already proposed.
OPTIONS:
  A. Re-sign — the builder makes its three commits again with the same content, each signed with a label naming it as this session's builder; the check compares the ids as text, so it accepts the label; the reviewer confirms the content is byte for byte what it passed. Gain: the check passes now and on later work, tried on a copy. Cost: the commits that land are identical to, not the same as, the ones reviewed; the signing departs from the form in the project's mechanics file, and later helpers would sign this way. Rules out: nothing. Reversible: yes.
  B. Exempt — the three commits are listed as skipped, with a ledger entry; a high-risk change you rule on. Gain: the reviewed commits land unchanged. Cost: tried on a copy, the harness lands, but every later commit of the builder's on this plan then fails the same check, from any session, so the test's later work needs its own fix; the exempt commits also skip their other checks. Rules out: later work under this plan, until that fix. Reversible: yes, by removing the listing.
  C. Rebuild — a new cloud session is started for the builder, with its own session id, as an earlier step's builder was; it builds the harness again to the same checks, and it is reviewed again. Gain: nothing set aside or skipped, and no new signing form. Cost: the build and review again, estimated from this time's 1.3 and 1.0 million tokens, fewer if its findings are fixed first. Rules out: nothing. Reversible: yes.
RECOMMENDATION: A, with medium confidence (the Chief of Staff's judgement): it is the only option tried that lets both this work and later work pass without a further change. What would change it: wanting the exact reviewed commits to land, with a further fix for later work (then B), or wanting no new signing form (then C).
WHO HAS CHECKED IT: the Reviewer found the shared signature; the Chief of Staff read the check's code and ran it on each option; the Critic checks this card.
RISK CLASS: R0 (questions/**)   REVERSIBILITY: reversible   BLAST RADIUS: when the harness lands; A also how later helpers sign; B the exempt list, the ledger and later work under this plan; C the cost of a rebuild
DEFAULT: none, since each option bears on how a CI-enforced check is met, which only you rule   TIMEOUT: none

## Context
- The harness passed the Reviewer at round 3 (source: reviews/S-001/_reviewer-build.md)
- With the owner's correction, the locked suite passes on the harness, 2 tests skipped by design (source: reviews/57/reviewer.md, section 1; reviews/57/owner.md)
- The check refuses one session that wrote both a spec's checks and its code; it takes the specs from the commits checked and the sessions from every commit reachable, exempt or not (source: governance/checks/surface_guard.py, `range_violations` and `independence_violations`)
- The Check author's and the Builder's commits carry the same session id (source: reviews/57/reviewer.md, finding 1)
- The two helpers ran on different models, from different briefs (source: docs/briefs/90-builder.md; docs/briefs/99-check-author.md, on branch claude/chief-of-staff-p001-build-5m9j1d)
- The check run on each option on copies: as they are, it fails; B lands and then fails the next builder commit under S-001; A passes both (source: intake/P-001-harness-landing-runs-2026-11-05.md)
- Adding an exemption needs a ledger entry and is high risk (source: governance/SURFACES.md, the exempt block)
- The project's mechanics file gives the signing form as the session id (source: CLAUDE.md); a helper started from this session has no id of its own on record (source: docs/LESSONS.md LL-65, on branch claude/chief-of-staff-p001-build-5m9j1d)
- An earlier step's builder ran as a cloud session of its own, started from the Chief of Staff's session (source: docs/briefs/25-builder.md)
- The build used 1,340,245 tokens and its review 964,635 across three rounds, as reported (source: sessions/chief-of-staff/session_01QBwHGNGKXFwvVVdzkei5aT.jsonl)
