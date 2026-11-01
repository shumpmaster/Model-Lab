Verdict: FAIL

Reason: the B and C sources are now reachable and most of them support the memo. I opened about 35 pages, and none contained instructions aimed at agents. FAIL stands for four reasons:
- Two memo figures do not match their sources: c2 (GEPA) and b9 (+4% for developer-written files).
- Some claims have no source I could open: the OpenAI blog, claude.com, the Cognition 2026 follow-up, and c11.
- The c0, c11 and F20 absence claims cannot be checked.
- The bolded claim in bottom line 3 has only one source.

**How I opened sources.** WebFetch still fails with ENOTFOUND for every host. Plain curl through the session proxy works for arxiv.org, ncsc.gov.uk, csrc.nist.gov and nvlpubs.nist.gov, metr.org, cognition.ai, owasp.org, ai.meta.com, cookbook.openai.com, code.claude.com and platform.claude.com, research.trychroma.com, and proceedings.iclr.cc. openai.com returns 403 and claude.com/blog returns 404. The coordinator's note about the missing files is resolved. I read the memo and the earlier check from git commits on `orch/p001-research-questions` before the files appeared on disk. The earlier A-item results are carried over unchanged. I wrote no files in the repo and did not open the barred directories.

**Limits of this check.**
- For arXiv papers I read the abstract and, where noted, the full text. Venue claims (ICLR, NeurIPS, EMNLP, UIST) were not checked, except that the ICLR 2025 page for the telephone-game paper opened and carries the same abstract. A venue listing of the same paper is not an independent source.
- The Anthropic multi-agent post and its Willison write-up were not re-opened. The earlier A result stands.
- Items a1–a4 and the other anthropic.com and repository items are unchanged from the earlier check and are not repeated below.

**Table: item · claim · source opened · result · note**

| Item | Claim | Source opened | Result | Note |
|---|---|---|---|---|
| a5 | Sharded instructions lower performance by 39% on average over six tasks; models that take a wrong turn "do not recover" | arxiv.org/abs/2505.06120 | Supports | Abstract: "average drop of 39% across six generation tasks"; "increase in unreliability"; "get lost and do not recover". "Recap turns did not fully repair" and the 36% secondary figure were not checked. |
| a6 | Text drifts to attractors through chains of LLMs; toxicity stronger than length; open-ended instructions give stronger attraction | arxiv.org/abs/2407.04503; the ICLR 2025 proceedings page | Supports | "toxicity leading to stronger attractors than length"; "more open-ended instructions lead to stronger attraction effects". Same paper at both sites. |
| a7 (B half) | Chroma: 18 models, degrading with input length, worse with distractors | research.trychroma.com/context-rot | Supports | "evaluation across 18 LLMs"; "even under these minimal conditions, model performance degrades as input length increases". Distractors are said to degrade performance, citing prior work. I did not read the date. |
| a8 | MAST: 14 modes in 3 groups; 1,000+ or 1,642 traces; per-mode shares | arxiv.org/abs/2503.13657 and PDF | Supports, with version differences | Abstract: "14 unique modes", "1600+ annotated traces". The PDF says 1642. Shares differ by version: inter-agent misalignment 32.3% in one figure and 44.2% in another. Information withholding 0.80% or 0.85%. Disobey role spec 1.5% or 11.5%. The memo's C note on version disagreement is right. |
| a9 | MetaGPT SOPs as structured documents raise code-generation success; "cascading hallucinations" | arxiv.org/abs/2308.00352 | Supports in part | Abstract: encodes SOPs; "more coherent solutions than previous chat-based multi-agent systems". "Cascading hallucinations" is the authors' own framing. The ICLR 2024 page was not opened. |
| a10 | Cognition: "Share context", "Actions carry implicit decisions"; conflicting parallel writes | cognition.ai/blog/dont-build-multi-agents | Supports | Principle 1: "Share context, and share full agent traces". Principle 2: "Actions carry implicit decisions, and conflicting decisions carry bad results". The page is from 2025. The 2026 follow-up ("writes stay single-threaded") was not found, so that part is unreachable. |
| a11 (second source) | Anchoring studies on LLM judges | none | Unreachable | The memo cites no URL. The ICLR listing was not located. |
| a12 | Self-recognition correlates linearly with self-preference; fine-tuning changes both | arxiv.org/abs/2404.13076 | Supports | "a linear correlation between self-recognition capability and the strength of self-preference bias". The NeurIPS 2024 page was not opened. |
| b1 | Greshake et al.: indirect prompt injection, no direct interface | arxiv.org/abs/2302.12173 | Supports | "remotely (without a direct interface) exploit LLM-integrated applications by strategically injecting prompts into data likely to be retrieved". The AISec 2023 pages were not checked. |
| b1 | NIST AI 100-2e2025, section 3.4 "Indirect Prompt Injection Attacks and Mitigations", agent security | csrc.nist.gov landing page and the PDF at nvlpubs.nist.gov | Supports | Published March 2025. Contents list "3.4. Indirect Prompt Injection Attacks and Mitigations". Text on hijacking a GenAI agent is in the section. |
| b1 | OWASP 2025 Top 10 keeps prompt injection at #1 | genai.owasp.org/llmrisk/llm01-prompt-injection | Supports | The page is "LLM01:2025 Prompt Injection", first in the list. |
| b2 (NCSC) | No inherent data/instruction distinction; "may never be totally mitigated"; reduce likelihood and impact; distrust vendors who "stop" it | ncsc.gov.uk blog | Supports | Quote: "As there is no inherent distinction between 'data' and 'instruction', it's very possible that prompt injection attacks may never be totally mitigated". Also "reduce the risk and the impact" and "Beware any that claim they can 'stop' prompt injection". Dated 8 December 2025, by Dave Chismon. |
| b3 | Claude.com follow-up gives 16.7–17.6% under stronger attacks | claude.com/blog | Unreachable | 404 at the URL I guessed. The correct URL is unknown. |
| b4 | AgentDojo: under 66% of tasks solved with no attack; a secondary detector cut attack success to 8%; "important instructions" the strongest | arxiv.org/abs/2406.13352 and PDF | Supports, except the last point | "Current LLMs solve less than 66% of AgentDojo tasks in the absence of any attack"; "the attack success rate drops to 8%". "Important instructions" appears only as a figure legend; I did not confirm it was the strongest attack. |
| b5 | Prompt Infection: self-replicating across agents; tagging plus other safeguards needed | arxiv.org/abs/2410.07283 | Supports in part | Abstract: "self-replicate across interconnected agents"; "even when agents do not publicly share all communications"; tagging "when combined with existing safeguards, significantly mitigates". "Reach agents that never read outside input" is not in the abstract in those words. |
| b6 | Design patterns paper: six patterns including dual LLM, plan-then-execute, context-minimisation | arxiv.org/abs/2506.08837 and PDF | Supports | The PDF names Action-Selector, Plan-Then-Execute, LLM Map-Reduce, Dual LLM, Code-Then-Execute and Context-Minimization. |
| b6 | Meta "Agents Rule of Two" | ai.meta.com/blog/practical-ai-agent-security | Supports | Dated October 31, 2025. "agents must satisfy no more than two of the following three properties within a session". The first-party page is now opened, so this is no longer secondary. |
| b6 | OpenAI Instruction Hierarchy (Wallace et al.) | arxiv.org/abs/2404.13208 | Supports in part | Abstract: "drastically increases robustness"; applied to GPT-3.5. I did not check the memo's "likely still vulnerable" wording. |
| b7 | IFScale: best of 20 models reaches 68% at 500 instructions; bias toward earlier instructions | arxiv.org/abs/2507.11538 and PDF | Supports | "20 state-of-the-art models"; "only achieve 68% accuracy at the max density of 500". The PDF says the primacy bias peaks around 150–200 instructions. Venue not checked. The Arize rerun (C) was not opened. |
| b8 | ManyIFEval: all-instructions satisfied falls faster than single instructions, up to ten | arxiv.org/abs/2509.21051 (title "When Instructions Multiply") | Supports in part | Abstract: up to ten instructions across ten LLMs, "performance consistently degrades as the number of instructions increases". The "faster than single-instruction" detail is not in the abstract. The authors and EMNLP venue were not checked. |
| b9 | AGENTS.md paper: files followed; LLM-generated "slightly reduced" success; cost +19–23%; developer files +4% | arxiv.org/abs/2602.11988 and PDF | Partly supports, one figure contradicted | Cost: "over 20% on average"; 20% and 23% in the two settings. LLM-generated files have "a marginal negative effect on task success rates", and the paper says neither effect is statistically significant. Developer-written files: +2.4% on average with p = 21%, not +4%. The memo's "19–23%" is slightly off (the paper says 20–23%). |
| b10 | CLAUDE.md under about 200 lines; "Longer files consume more context and reduce adherence" | code.claude.com/docs/en/memory | Supports in part | "target under 200 lines per CLAUDE.md file. Longer files consume more context and reduce adherence." The cut-test question "Would removing this cause Claude to make mistakes?" was not found on this page, so that wording is not confirmed. |
| b11 | METR: o3 hacks in 0.7% of HCAST runs and every trajectory on one RE-Bench task; other models too | metr.org/blog/2025-06-05-recent-reward-hacking | Supports | "hacks in 0.7% of runs across all HCAST tasks"; "o3 eventually reward-hack in every single trajectory we generated" on one RE-Bench task. The page also shows o1 and Claude 3.7 Sonnet examples. The page says "reward hacks"; "modified tests or scoring code" is the memo's paraphrase. |
| b12 | ImpossibleBench: GPT-5 cheating cut from 92% to 1%; stronger models cheat more | arxiv.org/abs/2510.20270 and PDF | Supports, with a qualifier | "appropriate prompt could dramatically reduce GPT-5's cheating from 92% to 1% on Conflicting-LiveCodeBench". The paper says more capable models generally cheat more, but newer Claude models cheat less than Sonnet 3.7. |
| b13 | OpenAI "Detecting misbehavior…": strong optimisation against a CoT monitor gives obfuscated reward hacking | openai.com blog, which returned 403; the underlying paper arxiv.org/abs/2503.11926 | Blog unreachable; paper supports | The paper says "with too much optimization, agents learn obfuscated reward hacking, hiding their intent within the CoT". The openai.com page itself is unconfirmed. |
| b16 | Claude 4 guidance on "precise instruction following"; "above and beyond" must be asked for | platform.claude.com claude-4-best-practices | Supports in part | "Claude's latest models are trained for precise instruction following and benefit from explicit direction". I did not find the "above and beyond" wording. |
| b16 | GPT-5 guidance: contradictory or vague instructions more damaging | cookbook.openai.com GPT-5 prompting guide | Supports | "poorly-constructed prompts containing contradictory or vague instructions can be more damaging to GPT-5 than to other models". |
| b17 | Sclar: formatting changes accuracy by up to 76 points; about 10 on average across 50+ tasks; persists with size and instruction tuning | arxiv.org/abs/2310.11324 and PDF | Supports, except one figure | "up to 76 accuracy points … LLaMA-2-13B"; "Sensitivity remains even when increasing model size … or performing instruction tuning". The "about 10 on average" figure was not found; the PDF gives a median spread of 7.5 points. |
| c1 | Reflexion: 91% pass@1 on HumanEval vs 80% for GPT-4 | arxiv.org/abs/2303.11366 | Supports | "91% pass@1 accuracy … surpassing the previous state-of-the-art GPT-4 that achieves 80%". The oracle caveat is the memo's secondary reading. |
| c2 | GEPA beats GRPO by about 10% on average with up to 35× fewer rollouts | arxiv.org/abs/2507.19457 and PDF | Does not support the figure | Abstract: GEPA beats GRPO "by 6% on average and by up to 20%, while using up to 35x fewer rollouts". "Over 10%" is the margin over the MIPROv2 prompt optimiser. The decagon.ai bloat claim (50 to 500 samples, 75% longer prompts) was not opened. |
| c3 | ACE: brevity bias, context collapse; delta updates; +10.6% on agents, +8.6% on finance | arxiv.org/abs/2510.04618 and PDF | Supports | Abstract matches. The 18k to 122 token collapse is in the paper itself: 18,282 tokens at 66.7 accuracy, then 122 tokens at 57.1. So that item is primary, not secondary. "Grow-and-refine" is confirmed. The online fall to 67.3 against 70.7 was not located. |
| c4 | Generic prompt additions can hurt; compliance from 26/30 to 9/30 | arxiv.org/abs/2601.22025 | Supports | "from 26/30 to 9/30" for Qwen 2.5 on RAG when generic rules are appended to the user prompt. The tests are small (30 cases per suite, local 8B models), and the memo should say so. |
| c6 | Rubric edits that pass benchmark validation shift judge preferences in a set direction; up to 27.9% (harmlessness) and 9.5% (helpfulness) | arxiv.org/abs/2602.13576 | Supports | Abstract: "systematic and directional shifts"; "difficult to detect through aggregate benchmark metrics"; "up to 9.5% (helpfulness) and 27.9% (harmlessness)". Title is "Rubrics as an Attack Surface". The 27.9% comes from goal-directed adversarial rubric edits, not ordinary edits. The memo's "up to 27.9%" omits that. |
| c7 | Judge prompt perturbations (rubric order, score labels, reference answers) shift scores | arxiv.org/abs/2506.22316 | Supports | "rubric order bias, score ID bias, and reference answer score bias". |
| c8 | Criteria drift (Shankar et al.) | arxiv.org/abs/2404.12272 (the Berkeley PDF was not opened) | Supports | "criteria drift: users need criteria to grade outputs, but grading outputs helps users define criteria". The UIST 2024 venue was not checked. |
| Not opened | Willison, decagon.ai, Arize, claude.com follow-up, openai.com blog, Cognition 2026 follow-up, iclr.cc and neurips.cc listings, owasp.org Top-10 index | n/a | Unreachable or not opened | See the rows above. |
| c0, c11, F20 | Absence claims | n/a | Not checkable | My searches were not repeated. These stay C. |

**Bottom-line points and patterns now resting on opened sources**

- **Bottom line 1 (handoffs).**
  - Underspecified briefs and compression are supported by the earlier A items a1, a2 and a4.
  - Compression and multi-turn loss now have independent support in Laban (a5).
  - The drift strand is confirmed by the telephone-game paper (a6).
  - The anchoring strand has no confirmed second source (a11). Sycophancy is confirmed by a11's A half. Self-preference is confirmed by a12.
  - "No study compares blind and full-context handoffs" is an absence claim and cannot be checked.
  - Cognition's argument against restricting what a role sees is confirmed.
- **Bottom line 2 (override).**
  - NCSC and Anthropic agree that injection is not solved and may never be fully mitigated. Two independent sources are confirmed.
  - "Dropped more often as their number grows" is confirmed by IFScale and ManyIFEval.
  - "Wording can raise or lower gaming sharply" is supported by ImpossibleBench for GPT-5 on one benchmark. It is a single source; METR shows gaming exists but not the wording effect.
  - "Newer models follow instructions more literally" has two vendor pages. Anthropic's "precise instruction following" is confirmed. OpenAI's "more damaging to GPT-5 than to other models" is confirmed. The "above and beyond" detail is not confirmed.
- **Bottom line 3 (checkers).**
  - The bolded claim, that a checker change shifts verdicts in a set direction while validation looks fine, is confirmed in the abstract of one source only (c6).
  - c7 and c8 are related but do not show the same effect. c9 (A) supports calibration only.
  - So the claim has one source and is not confirmed as load-bearing.
  - The sentence also leaves out that c6's 27.9% comes from adversarial edits.
- **Part (c) generally.**
  - "Failure-driven changes help with a reliable outcome signal and a held-out check" is supported by Reflexion, GEPA and ACE. The GEPA figure in the memo must be corrected to 6% average and up to 20%.
  - "Rewriting erodes detail" is confirmed by ACE.
  - The claim that optimising on more failures bloats and overfits prompts rests on decagon.ai, which I did not open. It is not confirmed.
- **Patterns.**
  - P01 (structural isolation) now rests on three independent confirmed sources: the design-patterns paper, Meta's Rule of Two, and the NCSC advice on deterministic protections. No controlled comparison with wording-only defences was found, so the "where it worked" line must stay as written.
  - P02 (batch revision against a held-out set) has GEPA and ACE confirmed. The practitioner report is unopened, and "regression set near 100%" rests on Anthropic (A).
  - P03 (anchor checker changes) has c6 confirmed and c8 and c9 as weaker supports. The remedy itself is untested, and the memo says so.
  - P04 (complete task descriptions) is supported by a1 (A) and Laban (confirmed). The Laban claim is about multi-turn splitting, not briefs, so the link is indirect.

**Library entries: may it be filed**

I applied the strict rule that a load-bearing fact needs two independent sources I opened, and that same-publisher pages and a paper plus its venue listing count as one. The memo marks none of the entries as load-bearing or not, so the single-source decisions are the coordinator's. I do not change grades.

| Entry | Decision | Why |
|---|---|---|
| Q007-F01 | May file, single-source self-report | A confirmed; Willison is not independent. |
| Q007-F02 | May file only as a single-publisher fact | Both pages are Anthropic. The telephone-game and Laban results support related but different claims. |
| Q007-F03 | May file, single-source | Laban confirmed; the ICLR listing is not independent. |
| Q007-F04 | May file, single-source | a6 confirmed. |
| Q007-F05 | May file as 2src | Anthropic plus Chroma, both opened and independent. |
| Q007-F06 | May file, single-source | Unchanged. |
| Q007-F07 | May file, single-source | a12 confirmed. |
| Q007-F08 | May file as 2src | Greshake and NIST section 3.4, both opened. |
| Q007-F09 | May file as 2src | Anthropic and NCSC, both opened. |
| Q007-F10 | May file, single-source self-report, with the earlier wording fix | Drop "its strongest model". |
| Q007-F11 | May file, single-source, with the claim narrowed | Self-replication across agents is confirmed. "Reaching agents that never read outside input" is not. |
| Q007-F12 | May file as 2src for the direction; the 68% at 500 is single-source | IFScale and ManyIFEval are independent. |
| Q007-F13 | May file, single-source, with fixes | Say "marginal negative effect, not statistically significant", and "cost over 20%". Do not use +4%. |
| Q007-F14 | May file as 2src that gaming exists; the 92% to 1% is single-source | METR and ImpossibleBench. The METR wording is "reward hacks", not "modified tests". |
| Q007-F15 | May file, single-source self-report | Add that the 95% also followed a less constrained scaffold. |
| Q007-F16 | May file, single-source, with a fix | Keep "up to 76 points" and drop "about 10 on average". |
| Q007-F17 | Hold if load-bearing; may file as single-source | One source. Say the 27.9% comes from adversarial rubric edits. |
| Q007-F18 | May file, single-source | Venue unchecked. |
| Q007-F19 | May file, single-source | Numbers confirmed in the paper itself. |
| Q007-F20 | Not filed | Absence claim; cannot be confirmed. |
| Q007-F21 | May file, single-source | Unchanged. |
| Q007-P01 | May file | Three independent opened sources for the principle; keep the no-controlled-comparison caveat. |
| Q007-P02 | May file, with the GEPA correction | Origin figures need fixing; the practitioner report is unopened. |
| Q007-P03 | Hold if the checker-instruction claim is load-bearing; otherwise may file | Rests on one source plus related items. |
| Q007-P04 | May file, with the Laban link marked indirect | |

**Memo corrections needed before anything is filed**
- c2: GEPA beats GRPO by 6% on average and up to 20%, not about 10%.
- b9: developer-written files gave +2.4% (p = 21%), not +4%; LLM-generated files had a marginal negative effect, not statistically significant; cost rose 20% to 23%.
- b17: remove "about 10 points on average".
- c3: the 18k to 122 token example is in the ACE paper, not a secondary source.
- c6: state that the 27.9% comes from adversarial rubric edits.
- b10: the "Would removing this cause mistakes?" wording was not found on the memory page.
- F10 and F15: the earlier wording fixes still apply.

**Files opened.** /home/user/Model-Lab/research/Q-007-memo.md and /home/user/Model-Lab/research/Q-007-source-check.md (present on disk at the end), and /home/user/Model-Lab/research/Q-007.md for the question text.
