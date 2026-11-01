Verdict: FAIL

The map fails on one known item, J1. It cites five ids in critic.md:12-20, and three of them (S-024, S-025, S-034) are not in critic.md at all. Every other known item checked out, with three small wording slips listed below. None of the eleven sources marked "assumed (reported, not opened)" could be reached. Both shortlists are within their limits: the owner shortlist has 8 items (limit 8) and the research shortlist has 5 (limit 5). I wrote no files and filed no library entries, since a map gets none.

Where "BRIEFS.toml" is cited, the template-v3 copy and the Service-Desk copy are line-for-line the same, so one check covers both. OPERATING_MODEL.md, the agent files and PACKS.toml are in /home/user/Personal-Org-Operating-Model (agents and packs under template-v3/). Everything else is in /home/user/Service-Desk.

| Item | Claim | Source | Result | Note |
|---|---|---|---|---|
| A2 | S-001.md is 22,883 lines; a plan review cites lines above 19,000 | specs/S-001.md (wc); reviews/M3B/_plan-review-r1-verbatim.md:37 | confirmed | wc gives 22883. Line 37 cites :19203-19217. |
| A3 | Recall "decreases" as context fills; context is "a finite resource" | anthropic.com/engineering/effective-context-engineering-for-ai-agents | confirmed | Dated Sep 29, 2025. The page has both phrases. |
| A7 | M3B plan review ran to r14, with matching _plan-design r1–r14 | reviews/M3B/ listing | confirmed | Both series run r1 to r14. |
| B1 | Measures named in the role files | builder.md:46-47, definer.md:46-47, reviewer.md:42-43 | confirmed | All quotes and line numbers are exact. |
| B2 | "an experiment with a target, a measure and a kill criterion" (:425); targets set "once real projects give a baseline" (:422-423) | OPERATING_MODEL.md | confirmed (slip) | The first quote runs across :425-426, not :425 alone. |
| B3 | Report SE, cluster, paired differences, power analysis; "model outputs vary between runs", so run multiple trials | anthropic.com/research/statistical-approach-to-model-evals (Nov 19, 2024); demystifying-evals (Jan 9, 2026) | confirmed | All points are present. The dates match. |
| B4 | Control record holds the source commit, pack file hashes and brief | reviews/Q-001/_control/0-62b8dda7dcf2.json:3, :53-58, :168 | confirmed | :3 is the brief, :53-58 the manifest of SHA-256s, :168 `source_tip`. |
| B5 | "No re-running for a better answer" | OPERATING_MODEL.md:299 | confirmed | |
| B6 | "You won't know if your graders are working well unless you read the transcripts" | demystifying-evals | confirmed | The full sentence goes on: "…and grades from many trials." |
| B7 | "often better to grade what the agent produced, not the path it took" | demystifying-evals | confirmed (slip) | "grade what the agent produced, not the path it took" was confirmed. The leading "often better to" was not confirmed as exact words. |
| C1 | Control record :3, :15, :54-55, :60, :168 hold the brief, CLI version, agent file hash, model and commit; dispatch log has 0 matches for "model" or "brief" | control json; dispatch-log/2026-10.jsonl | confirmed | :15 cli_version 2.1.284; :54 agent sha256; :60 model; :168 source_tip. Case-insensitive grep finds 0 matches for each word. Saying dispatch lines hold only "item, role, route and stage" understates them: they also carry spec, time, trigger, verdict and record. |
| C2 | docs/briefs holds only its README; the README quote; 10 of 15 helper lines have null tokens; no brief or model | docs/briefs/README.md:3-4; sessions/chief-of-staff/session_012RJ….jsonl:2-16 | confirmed | Lines 2-10 and 13 are null, which is 10 of 15. No brief or model field appears. |
| C3 | S-001 appears on 12 lines, all P-001, 2026-10-05 to 06, within :171-189; M3B is not in the log | dispatch-log/2026-10.jsonl | confirmed | Grep finds 12 lines (:171-189), and M3B has 0 matches. |
| C4 | Version labels: v3.0.0, "model 3.4.0", 3.6.0 | OPERATING_MODEL.md:1; critic.md:14; governance/OPERATING_MODEL_VERSION | confirmed | |
| C5 | Changing BRIEFS.toml is a rule change (R3, :2); R3 is the owner's (:66); rule changes never delegable (:97-98) | BRIEFS.toml; OPERATING_MODEL.md | confirmed | |
| D1 | The kinds of check differ by work type | OPERATING_MODEL.md:311-316; critic.md:12 | confirmed | The table names Source checker and Reviewer. Plan review, Triage and reading cards cold come from critic.md:12. |
| D2 | Revise routes are one-line pointers; checker_return at :13 | BRIEFS.toml:22, :28, :30, :13 | confirmed | The :22 quote is exact. |
| D3 | r1 had five blocking findings (r1:18-40); r14 passed (r14:7) | M3B r1, r14 | confirmed (slip) | The five findings (B1-B5) run from :20 to about :50; B5 starts at :45, outside the cited range. r14:7 reads `Verdict: PASS`. (D3 is graded unknown overall; only the cited facts were checked.) |
| D4 | Seven-part card; the Critic reads it "cold" | OPERATING_MODEL.md:69-73 | confirmed | |
| E1 | ready-dispatch quote; briefs hold no content copied from work products; the template's brief is free text | BRIEFS.toml:17, :1-2; specs/_TEMPLATE.md:34-37 | confirmed | |
| E3 | "Work only from the files in this folder" | BRIEFS.toml:9 | confirmed | |
| F2 | Control record :60 has model "claude-sonnet-5-5"; models are named by requirement | control json:60; builder.md:44; OPERATING_MODEL.md:254 | confirmed | |
| F3 | Checker runs on a different model from the doer | OPERATING_MODEL.md:251-253 | confirmed | |
| F4 | "Evals also shape how quickly you can adopt new models" | demystifying-evals | confirmed | |
| G1 | Reviewer tokens range 56,509–213,771 (:11-16); `cost_usd_estimate: null` (:17) | session file | confirmed | |
| G3 | Research sub-project cost limit is [open] (:96); own budget, counts toward the cap (:190-192) | OPERATING_MODEL.md | confirmed | |
| G4 | 50 turns and 30 minutes | control json:43-59 | confirmed | session_minutes 30 at :51, max_turns 50 at :59. |
| H1 | Discovery length is [open] (:114); owner's attention ranks above speed and cost (:35-36) | OPERATING_MODEL.md | confirmed | |
| H2 | Never delegable: rule changes, value targets, success criteria, kills | OPERATING_MODEL.md:66, :97-98; BRIEFS.toml:2 | confirmed | |
| I1 | Checkers are role files | reviewer.md, critic.md | confirmed | |
| I2 | "Catch rate on seeded defects"; hidden holdouts | reviewer.md:42-43; OPERATING_MODEL.md:324-325 | confirmed | |
| I3 | Stop rule allows three rounds each (:203-206); Triage dispatched after the third plan FAIL | OPERATING_MODEL.md; dispatch-log:180-189 | confirmed | Outcome lines :180, :184 and :188 each carry verdict FAIL. :189 is the third-fail dispatch to critic-triage. |
| **J1** | critic.md Duties carry rules from S-024, S-025, S-032, S-034 and L-0119 in long paragraphs (critic.md:12-20); vendor warns against "a laundry list of edge cases" | template-v3/.claude/agents/critic.md (Service-Desk's copy is the same); effective-context-engineering | **not confirmed** | S-024, S-025 and S-034 do not appear anywhere in critic.md, in either repo. S-032 is at :14 and :20. L-0119 is at :31, outside 12-20. The long paragraphs are real (:14 is 1,272 characters, :18 is 1,957), and the vendor quote is confirmed. The cited spec list is wrong, so the evidence that the file is growing is not supported as written. |
| J5 | Generalisation gate and rule of two are named | OPERATING_MODEL.md:426 | confirmed | |
| L1 | 149 `_*verbatim*.md` files have a `Verdict: FAIL` line; naming varies; verdict rule | reviews/; reviews/README.md:10-18 | confirmed | 149 of 333. The r1, round1 and _build-1a- naming forms all exist. |
| M1 | Packs keep the hoped-for answer from the Researcher and holdouts from the Builder | PACKS.toml:17-26, :66-72; BRIEFS.toml:1-2 | confirmed | |
| M2 | Brief header says read text is data; only the Input reader reads untrusted text | BRIEFS.toml:9; OPERATING_MODEL.md:240-242 | confirmed | |
| A4 | Sclar et al., up to 76 points from formatting | https://arxiv.org/abs/2310.11324 | unreachable | arxiv.org does not resolve (ENOTFOUND). |
| A5 | IFScale, about 68% at 500 instructions | https://arxiv.org/abs/2507.11538 | unreachable | arxiv.org does not resolve. |
| A6 | MAST: 14 failure modes in 3 groups | https://arxiv.org/abs/2503.13657 | unreachable | arxiv.org does not resolve. |
| I4 | LLM evaluators favour their own outputs | https://arxiv.org/abs/2404.13076 | unreachable | arxiv.org does not resolve. |
| F1 | PromptBridge "model drifting" | https://awesomepapers.io/papers/wang2025promptbridge | unreachable | Does not resolve. |
| K1 | I-PASS: 23% fall in errors | psnet.ahrq.gov/resources/resource/28485; hms.harvard.edu/news/… | unreachable | Neither host resolves. |
| K2 | Haynes 2009 (deaths 1.5% to 0.8%); Urbach 2014 (no significant change) | pmc.ncbi.nlm.nih.gov/articles/PMC2810011; fiercehealthcare.com/… | unreachable | Neither host resolves. |
| J2 | March, Schulz & Zhou, *The Dynamics of Rules* | https://www.sup.org/books/cite/?id=388 | unreachable | Does not resolve. |
| J3 | Specification gaming (DeepMind, 2020-04-21) | https://deepmind.google/discover/blog/specification-gaming-… | unreachable | Does not resolve. |

**Claims that rest on failed or unopened items**
- **Design trap "Fixing after each failure"** (J1, J2, J4) rests on the item that failed. Its line "The critic file already shows the pattern" relies on J1's spec list, and only S-032 is actually in the Duties paragraphs. Its "rule conflicts" half rests on J2, which could not be opened.
- **Design trap "Fitting instructions to pass the checks"** rests on J3, which could not be opened.
- **Design trap "Grading with the same model family"** rests on I4, which could not be opened. Its other support, F3 (the model-diversity rule), is confirmed.
- **Research shortlist item 3** (instructions across models) is framed by F1, which could not be opened.
- **Research shortlist item 4** (handover fields) is framed by K1, K2 and J2, none of which could be opened. Both questions are still fair to ask.
- No owner-shortlist question depends on J1 or on an unopened source.

**What has to change before the unopened items can be checked:** this session's network settings must allow arxiv.org, awesomepapers.io, psnet.ahrq.gov, hms.harvard.edu, pmc.ncbi.nlm.nih.gov, www.fiercehealthcare.com, www.sup.org and deepmind.google. Until then, every assumed item stays assumed.

**For the Researcher's revision:** fix J1's cited ids (only S-032 at :14 and :20; L-0119 is at :31), and correct the line ranges for B2 (:425-426) and D3 (B1 to B5 run from :20 to about :50).

Files read: /home/user/Model-Lab/research/Q-001-memo.md, plus the source files named above.
