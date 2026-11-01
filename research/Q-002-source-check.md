Verdict: PASS
(All A and B items confirmed, with 3 listed slips. No C or D item could be confirmed or refuted, because arxiv.org did not resolve and I stopped trying other academic hosts. Checked 2026-11-01. I wrote no files and filed nothing.)

Slips, none of which changes a grade:
- S1. §3.6 and §1.6 put "often believed it had succeeded when it had not" in quotation marks. The swe-bench-sonnet page says: "it often 'thinks' that it has succeeded when the task actually is a failure." The meaning is the same, but the quoted words are not on the page. Fix the quote.
- S2. §3.3 and §8 say the Chroma README (B) supports "18 models". The README gives no model count; it confirms only the "varies significantly" sentence. The count stays C or D.
- S3. §2 gives the MAST venue as NeurIPS 2025 D&B. The MAST README I opened says only "arXiv preprint, arXiv:2503.13657 (2025)". The venue is unconfirmed.

**A. Repository records (A-grade)**

| Item | Claim | Source | Result | Note |
|---|---|---|---|---|
| A1 | The brief is a fixed one-line route template plus a common header and return form, filled with ids only | BRIEFS.toml:1-2, 9-13, 17-36 | confirmed | Lines 1-2 say "one per route, filled with the plan entry's ids only". Lines 9-13 hold header, doer_return, gate_return, user_return and checker_return. Lines 17-36 hold the route templates. |
| A2 | Packs set must_read, may_read, must_not_see, include_feedback | PACKS.toml:1-9 | confirmed | These lines are the header comment, which defines all four fields. |
| A3 | Plan rounds are capped at three | OPERATING_MODEL.md:203-206 | confirmed | Stop rule (D-044): "three each". |
| A4 | Checkers run on different models from the doers | OPERATING_MODEL.md:251-253 | confirmed | Model diversity (D-056). |
| A5 | Hidden holdouts are kept from the Builder | OPERATING_MODEL.md:247-248, 324-325 | confirmed | "The Builder sees the locked checks but never the hidden holdouts"; "readable only by CI". |
| A6 | The no-re-run rule | OPERATING_MODEL.md:299 | confirmed | "No re-running for a better answer." |
| A7 | Sessions are fresh by design | builder.md:8 | confirmed | "Every session is fresh, one role per task". |
| A8 | specs/S-001.md is 22,883 lines | Service-Desk | confirmed | `wc -l` returns 22883. |
| A9 | M3B has 14 plan-review rounds on file | reviews/M3B/ | confirmed | _plan-review-r1 to r14-verbatim.md, 14 files. |

**B. Web pages (B-grade)**

| Item | Claim | Source | Result | Note |
|---|---|---|---|---|
| B1 | Three factors explained 95% of BrowseComp variance; token usage alone 80%; the others are tool calls and model | multi-agent-research-system, 2025-06-13 | confirmed | Date is Jun 13, 2025. |
| B2 | "prompt engineering was our primary lever"; "spawning 50 subagents for simple queries"; "vague enough that subagents misinterpreted the task"; "performed the exact same searches as other agents" | same page | confirmed | Quoted words match. |
| B3 | Multi-agent beat single-agent Opus 4 "by 90.2%"; "about 15× more tokens than chats" | same page | confirmed | |
| B4 | "not a good fit"; coding tasks parallelise less; "not yet great at coordinating and delegating" | same page | confirmed | The page's wording is "fewer truly parallelizable tasks than research". |
| B5 | "a 40% decrease in task completion time" from revised tool descriptions | same page | confirmed | |
| B6 | SWE-bench Verified 22% (Claude 3 Opus), 33% (Claude 3.5 Sonnet, old), 49% (Claude 3.5 Sonnet, new) | swe-bench-sonnet, 2025-01-06 | confirmed | Figures and date match. "Same scaffold" is the memo's framing; I confirmed the "vary significantly based on this scaffolding" sentence but not that the scaffold was held fixed across all three rows. |
| B7 | "model often believed it had succeeded when it had not" | same page | not confirmed as a quote | See S1. The substance is confirmed. |
| B8 | "brittle logic"; "vague, high-level guidance"; "laundry list of edge cases"; "diverse, canonical examples"; recall "decreases"; "finite resource"; "attention budget"; summaries "often 1,000-2,000 tokens" | effective-context-engineering, 2025-09-29 | confirmed | |
| B9 | "we actually spent more time optimizing our tools than the overall prompt"; edit tool changed to require absolute paths | building-effective-agents, 2024-12-19 | confirmed | |
| B10 | "Even small refinements to tool descriptions can yield dramatic improvements"; held-out test sets | writing-tools-for-agents, 2025-09-11 | confirmed | |
| B11 | mini-swe-agent: "Just some 100 lines of python"; no tools other than bash; "Scores >74%"; "as LMs have become more capable, a lot of this is not needed at all to build a useful agent!" | github.com/SWE-agent/mini-swe-agent | confirmed | The README says "Does not have any tools other than bash". The memo does not put that phrase in quotation marks, so it is fine. |
| B12 | Personas: 162 personas, 4 model families, 2,410 questions; "does not improve model performance" | Prompting-with-Social-Roles README | confirmed | The README names no venue, and the Findings of EMNLP 2024 attribution is unconfirmed. It links arXiv 2311.10054. |
| B13 | Who&When: README confirms venue and 184 tasks | Agents_Failure_Attribution | confirmed | The README says "ICML 2025 spotlight" and "184 annotated failure tasks". The 53.5% and 14.2% figures are not on the page. |
| B14 | MAST README confirms title, authors, "over 1K annotated MAS traces" | MAST repo | confirmed | Venue: see S3. |
| B15 | Sclar README confirms title and authors | formatspread | confirmed | The venue shown is arXiv. ICLR 2024 is unconfirmed. |
| B16 | Laban README (§8) | lost_in_conversation | confirmed for title and authors only | The 39% figure is not in the README. It remains C. |
| B17 | SWE-agent README confirms the NeurIPS 2024 venue | SWE-agent | confirmed | The +10.7 and 18.0% figures are not on the page; the memo already says it confirms the venue only. |

**C. Grade-C and D items.** Where I list a result below, I tried to open the source.
- Unreachable (arxiv.org did not resolve): IFScale 2507.11538, Yang et al. 2505.13360, Laban 2505.06120, Kim et al. 2512.08296. I stopped trying other academic hosts, as the environment message advised.
- Not tried for the same reason: every other C or D item. That covers Levy, Du, Liu, Chroma paper, HAL, ProSA, He et al., GEPA, MAST figures, Huang, Kamoi, Monkeys, Smit, Panickssery, Verga, METR, τ-bench, Cognition, SWE-bench Verified screening and the Wharton reports.
- "Supports" or "does not support": none can be reported. The repo READMEs neither support nor contradict the specific figures (B13, B14, B16, S2).
- Nothing was upgraded.

**D. Counting**
- The §4 table holds 9 rows, K1 to K9, and the 2+2+5 split sums to 9.
- The split matches the table's "Instructions decisive?" column for K1 and K9 (yes), K4 (shared), and K3, K5, K7, K8 (no).
- K6 is the only row where the table does not say "shared": it reads "Tool descriptions are instructions; vendor-only evidence". The shared-lead label is a judgement.
- The K2 row says "Limited", which counts it among the five secondary kinds. §1.4 names role compliance as a narrow set where instructions are the largest lever. These two statements conflict, and the memo should reconcile them.
- The "2 of 9" estimate is arithmetically consistent. It carries the memo's own caveats: it is unweighted, and the frequency in this pipeline is unknown. Its support is thin:
  - K1 and K9 rest mainly on one vendor page (B), plus C items for K1.
  - K2, K3, K4, K7 and K8 rest on C or D items I could not open.

**E. Conclusions resting on failed or unopened items.** No A or B item failed except the S1 wording slip, which is not load-bearing.
- §1.1 (no study splits variance across all levers) is a negative result from searches. It is not checkable from here.
- §1.4 to §1.6 and §4 lean heavily on unopened C and D evidence for everything outside the Anthropic claims. The memo already flags this as unconfirmed.
- §4's K2 and K4 "instructions not decisive" calls rest on MAST role-prompt versus topology figures (C or D, which conflict between versions). Treat these as provisional.
- The §1.3 / F-a framing "scaffold fixed" is supported only by the "vary significantly" sentence (see B6).

**F. Proposed library entries (a "checked on" date of 2026-11-01 would apply to any entry filed)**

| Id | May it be filed as proposed? | Why |
|---|---|---|
| F-a | Not as a load-bearing fact | Confirmed, but there is one vendor source and no independent second source. File only with an explicit "single-source, vendor-reported" caveat, and revise the wording per B6. |
| F-b | Not as a load-bearing fact | Confirmed (B1), single vendor source about its own system. Same caveat. |
| F-c to F-m | No | All are grade C. I could not open any of the papers, so they cannot be confirmed. "Several independent sources" for F-c, F-f, F-g, F-h, F-l is untested. Hold until a session with arxiv.org, aclanthology.org, openreview.net, proceedings.neurips.cc, proceedings.mlr.press and research.google allowed re-checks them. |
| F-i | No | The venue and the 184 tasks are confirmed. The 53.5% and 14.2% figures are not. |
| P-a | Not as load-bearing | The pattern is confirmed on the vendor page. Its other cited support, the context-engineering guidance, is the same publisher and so not independent. |
| P-b | No | Grade C. Only the Anthropic half (B8) is confirmed. |
| P-c | Not as load-bearing | All three B sources are Anthropic, so there is no independent second source. The SWE-agent support is C or D. |
| P-d, P-e | No | Grade C, unconfirmed. |

Nothing is filed, because no entry has two independent confirmed sources. The checker will not upgrade anything.
