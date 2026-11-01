Verdict: PASS

Every A/B item in Q-004-memo.md was confirmed. There are three small slips (listed below) and no failed items. All grade-C items are unreachable from this session. Nothing was upgraded and no files were written.

Network: arxiv.org, aclanthology.org, hdsr.mitpress.mit.edu, gail.wharton.upenn.edu, developers.openai.com, icml.cc, iclr.cc, papers.ssrn.com and export.arxiv.org either do not resolve or return 403 from the proxy. These hosts need allowing before the C items can be checked.

## A/B items

| Item | Claim | Source | Result | Note |
|---|---|---|---|---|
| S1 | Role files name models "by requirement, never by name" (Strong at reading and synthesis; different from the Source checker) | researcher.md:38; builder.md:44 | confirmed | The memo's ranges 37-38 and 43-44 include the heading line, which is fine. |
| S2 | `MODEL_<ROLE>` is a repository variable, "never a file"; `--model` is passed next to `--agent` | RUNNER.toml:12; session_runner.py:571-573, 1206 | confirmed | |
| S3 | Runner refuses a checker on the same model as its doer without a waiver; the pairs are as listed; user-rep/chief-of-staff is never waived | session_runner.py:166-170, 593-616; OPERATING_MODEL.md:251-253 | confirmed | All six pairs match. |
| S4 | The scripted path records the model; the conversational path does not | session_runner.py:881; Q-001 F2/C2; control record 0-62b8dda7dcf2.json:60 | confirmed | The record reads `"model": "claude-sonnet-5-5"`. |
| S5 | OPERATING_MODEL.md has no rule to re-check when a model changes | OPERATING_MODEL.md, searched | confirmed | Searches for model, re-check, regression, replay, swap and upgrade found nothing. §10 (lines 417-429) covers changing the operating model's own rules, not the LLM behind a role. |
| S6 | Role files contain no all-caps MUST, NEVER, CRITICAL, IMPORTANT or ALWAYS | template-v3/.claude/agents/*.md | confirmed | Count is 0 in all 9 files. |
| S7, S8 | Estimate and opinion drawn from S2 and S3 | | consistent | No separate source. |
| 3.4.1 | "can vary significantly based on this scaffolding"; tool descriptions and "error-proof"; 2025-01-06 | anthropic.com/engineering/swe-bench-sonnet | confirmed | The URL redirects to /research/swe-bench-sonnet. The quote and "error-proof" are on the page; the date was confirmed by a fetch summary. |
| 3.2.1 (README) | The formatspread README confirms the paper's existence and authors | raw.githubusercontent.com/msclar/formatspread README | confirmed | Authors Sclar, Choi, Tsvetkov, Suhr and arXiv:2310.11324 appear in the BibTeX. This confirms existence only; the findings stay C. |
| 4.1.1 | Opus 5 prompts "should perform well without changes"; the page lists four behaviour changes | prompting-claude-opus-5-5 | confirmed | The four are early stops after progress reports, effort recalibration, thinking instructions to remove, and visual scaffolding to re-test. |
| 4.1.2 | GPT-5.1 "works well out of the box for most applications"; "can occasionally be verbose"; stress persistence and completeness | openai-cookbook gpt-5-1_prompting_guide.ipynb | confirmed | |
| 4.2.1 | GPT-4.1: "more closely and more literally than its predecessors"; "may not immediately work"; "implicit rules are no longer being as strongly inferred" | gpt4-1_prompting_guide.ipynb | confirmed | Verified in the raw notebook. |
| 4.2.1 | GPT-5: "surgical precision"; contradictory or vague instructions "more damaging to GPT-5 than to other models" | gpt-5_prompting_guide.ipynb | confirmed | |
| 4.2.1 | Anthropic lists "literal instruction following" for Sonnet 5 vs 4.6 and for Opus 4.8 | claude-prompting-best-practices, index table | confirmed | The Opus 4.8 row does not name a baseline. |
| 4.2.2 | Opus 4.5/4.6 "more responsive to the system prompt"; may "overtrigger"; "CRITICAL: You MUST use this tool when…" becomes "Use this tool when…"; 4.6 "might overtrigger on instructions that were needed for previous models" | claude-prompting-best-practices lines 488, 1128 | confirmed | |
| 4.2.2 | Cursor found "maximize_" "counterproductive with GPT-5"; sections "effective with earlier models needed tuning" | gpt-5_prompting_guide.ipynb | confirmed | |
| 4.2.3 | "Effort level names don't correspond to the same amount of thinking across models"; "a fresh effort sweep on your own evals rather than carrying over a setting tuned for an earlier model" | cited as the Opus 5.5 migration guide | confirmed in substance, attribution slip | Slip 2 below. |
| 4.2.4 | "a single sentence firmly and unequivocally clarifying your desired behavior is almost always sufficient" | GPT-4.1 guide | confirmed | |
| 4.3.1 | GPT-4 prime accuracy 84.0% (March) vs 51.1% (June); GPT-3.5 better in June; "can vary substantially over time"; initial release 2023.07.18 | LLMDrift README | confirmed | The README says "can vary substantially over time". The memo's "and for the worse in some tasks" is not in the caption I saw. It is outside the quoted words and does not matter. |
| 4.4.1, 4.4.2 | Each ID is a "pinned version"; "Anthropic does not update the weights or configuration of an existing model ID"; dateless IDs pinned from 4.6; older aliases such as `claude-sonnet-4-5` point to the latest snapshot; "infrastructure updates produce minor differences in observable behavior" | model-ids-and-versions | confirmed | |
| 4.4.3 | `claude-sonnet-5-5` is a pinned ID | model-ids-and-versions; Q-001 F2 | confirmed | |
| 4.5.1 | At least 60 days' notice | model-deprecations | confirmed | |
| 4.5.1 | Advises "thorough testing … well before the retirement date" | model-deprecations | confirmed | The page says "consider thorough testing". |
| 4.5.1 | Sonnet 4.5 (`claude-sonnet-4-5-20250929`): deprecated 2026-09-30, retires 2026-11-30 | model-deprecations | confirmed | |
| 4.5.1 | `claude-opus-4-1-20250805` retired 2026-08-05; `claude-sonnet-4-20250514` and `claude-opus-4-20250514` retired 2026-06-15; `claude-3-7-sonnet-20250219` retired 2026-02-19 | model-deprecations | confirmed | |
| 4.5.1 | Current models are listed "not sooner than" mid-2027 | model-deprecations | not confirmed (slip 1) | Slip 1 below. |
| 4.5.2 / §1.5 | Retired about 12-13 months after the snapshot date; Sonnet 4.5 about 14 months | computed from the dates above | confirmed | Opus 4.1 and Sonnet 3.7 are 12 months. Sonnet 4 and Opus 4 are 13 months. Sonnet 4.5 is about 14 months, from 2025-09-29 to 2026-11-30. |
| 5, evals row | "should have a nearly 100% pass rate"; "Evals also shape how quickly you can adopt new models"; "weeks of testing"; 2026-01-09 | anthropic.com/engineering/demystifying-evals-for-ai-agents | confirmed | The URL redirects to /research/… |
| 5, evals row | OpenAI: "building informative evals and iterating often" | GPT-4.1 guide | confirmed | |
| 5, minimal row | Anthropic warns against a "laundry list of edge cases" | anthropic.com/engineering/effective-context-engineering-for-ai-agents | confirmed | The memo cites Q-001 J1. The phrase is not on the best-practices page. I opened the real source and it is there. |
| 5, other B cells | Pin IDs (4.4.1); re-tune settings (4.2.3); explicit behaviour (4.2.1) | as above | confirmed | |

## Slips (none load-bearing)

1. **§4.5.1, "current models are listed 'not sooner than' mid-2027".**
   - The table gives Oct 15, 2026 (`claude-haiku-4-5-20251001`), Nov 24, 2026 (`claude-opus-4-5-20251101`) and Feb 2027 (Opus 4.6, Sonnet 4.6).
   - The latest entries are Sep-Oct 2027, and the column header is "Tentative retirement date".
   - "Mid-2027" is wrong as a summary. The 4.5.2 interval estimate does not use it.
2. **§4.2.3, quote and attribution.**
   - The "Effort level names don't correspond…" sentence is on the Opus 5.5 prompting page, not the migration guide.
   - The migration guide says "Run a fresh effort sweep on your own evals rather than carrying over a setting tuned for Claude Opus 4.7". The memo has "an earlier model" inside the quotation marks.
   - The claim holds. The citation and the quoted wording need correcting.
3. **§4.3.1, extra phrase.** "and for the worse in some tasks" was not found in the README caption. It is outside the quoted material and the substance is unaffected.

## Grade-C items

I tried to open every C source and all were unreachable. No C item is supported or refuted, and none can be filed.

| Item | Source | Result |
|---|---|---|
| 3.1.1 PromptBridge | arxiv 2512.01420 | unreachable (arxiv.org does not resolve) |
| 3.1.2 | arxiv 2311.05661 | unreachable |
| 3.1.3 | arxiv 2509.23387 | unreachable (same host) |
| 3.2.1 findings | arxiv 2310.11324 | unreachable (existence confirmed via README, see above) |
| 3.2.2 | aclanthology.org/2024.tacl-1.52 | unreachable |
| 3.2.3 | arxiv 2411.10541 | unreachable (same host) |
| 3.2.4, 3.3.1, 3.3.2 | arxiv | unreachable (same host) |
| 3.4.2 | arxiv 2605.23950; icml.cc | unreachable |
| 3.4.3 | arxiv 2609.00006 | unreachable (same host) |
| 3.5 AGENTS.md study | arxiv 2602.11988 | unreachable |
| 4.3.1 journal record | hdsr.mitpress.mit.edu | unreachable (403) |
| 4.3.2 MUSCLE | arxiv 2407.09435 | unreachable |
| 4.3.3, 4.3.4 | arxiv 2105.03048, 2409.10566 | unreachable (same host) |
| §5 Wharton CoT | arxiv 2506.07142; gail.wharton.upenn.edu | unreachable |
| §5 MSR 2025 | arxiv 2412.17298 | unreachable (same host) |
| §5 OpenAI optimiser | developers.openai.com | unreachable (403) |
| §5 GMPO (ACL 2026) | preview.aclanthology.org | not opened; same blocked network (aclanthology.org does not resolve) |
| §6 RLPrompt | arxiv 2205.12548 | unreachable (same host) |

## Conclusions resting on failed or unconfirmed items

No A/B item failed, so nothing rests on a failed item. These rest on C items that are unconfirmed:

- **§1.1 and §3 (different-model replacement).**
  - The finding that losses are largest and least predictable rests entirely on C sources.
  - The memo grades it [E, C], so the grade is honest.
  - Any reading of §7's "large losses" column that leans on 3.1 and 3.2 should be treated as unconfirmed.
- **§1.2.** The "negative flips" half rests on C (MUSCLE and the Amazon paper). The 84.0% to 51.1% half is B and confirmed.
- **§1.3 and §6, last two bullets of the carry-over evidence.** "Larger models are less sensitive to format" and "optimised on larger transfers to smaller" are C. The vendor statements are B and confirmed.
- **§1.4 and §5.** The Wharton chain-of-thought claim and the AGENTS.md "minimal" claim are C. The vendor advice behind P-Q004-2 is confirmed.
- **§7 and §4.3.5.** "Average re-check can pass while specific duties fail" is [O, C]. It is supported only by the 4.3.1 drift study (B, confirmed) plus C sources.
- **P-Q004-3 (behaviour in structure, not prose).** Rests on a single C ablation. The B part (Anthropic credits tool design) is confirmed but does not show that structure transfers better.
- **§3.6 and G1.** The claim that no study measures hand-written role instructions is an absence claim from searches. It cannot be confirmed by opening anything.

## Library entries

| Entry | File as proposed? | Note |
|---|---|---|
| F-Q004-1 | Yes | Anthropic and OpenAI each say the same thing, and I opened all three sources. I read them as independent corroboration. |
| F-Q004-2 | Yes, with a flag | Single source. File it as an attributed vendor statement ("Anthropic states…"), not as evidence that carry-over works. Anthropic is the only authority for its own page, so no independent second source exists. The GPT-5.1 line is a different fact and does not corroborate it. |
| F-Q004-3 | Yes, with a flag | Single vendor source about the vendor's own policy. File it as attributed. |
| F-Q004-4 | Yes | The dates and the 12-13 / 14 month interval are confirmed. Add that current models' retirement dates are "tentative", not "mid-2027". Single source, so file the interval as an estimate. |
| F-Q004-5 | Hold, or file as "authors report" only | The README is the authors' own claim and is not independent. The journal source (HDSR) is unreachable and is the same authors anyway, so there is no independent second source. File only as a B-graded authors' report with the HDSR source marked not opened, or wait. |
| F-Q004-6 | No | Grade C, sources unreachable. |
| F-Q004-7 | No | Findings unconfirmed. Only the existence of Sclar et al. is confirmed. |
| F-Q004-8 | No | Grade C, sources unreachable. |
| F-Q004-9 | Yes | Grade A, with several records agreeing: RUNNER.toml, session_runner.py and OPERATING_MODEL.md. The re-check absence is based on my own searches. The entry cites OPERATING_MODEL.md:251-254, and line 254 is a different sentence ("Models are named by requirement in rules…"), so it could be cited as 251-253. |
| F-Q004-10 | No | Grade C, source unreachable. |
| P-Q004-1 | Yes, as a vendor-recommended pattern | Origin and the three sources are confirmed. The "no signal of improvement" condition is the researcher's inference, not on the page. Keep "effect unmeasured". |
| P-Q004-2 | Only the B part | File on the two vendor sources (Anthropic best practices, OpenAI GPT-5 guide) as grade B. Drop the Wharton reference until it is opened. |
| P-Q004-3 | No | Grade C, single unconfirmed ablation. |

Records opened (read-only): /home/user/Model-Lab/research/Q-004-memo.md, /home/user/Model-Lab/research/Q-004.md, /home/user/Model-Lab/research/Q-001-memo.md and Q-001-source-check*.md (only to trace J1, F2, C2 and B4), /home/user/Personal-Org-Operating-Model/OPERATING_MODEL.md, /home/user/Personal-Org-Operating-Model/template-v3/.claude/agents/*.md, /home/user/Service-Desk/governance/RUNNER.toml, /home/user/Service-Desk/governance/checks/session_runner.py, and /home/user/Service-Desk/reviews/Q-001/_control/0-62b8dda7dcf2.json (line 60).
