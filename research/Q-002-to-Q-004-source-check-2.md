Verdict: FAIL

The papers are now reachable. I opened every named paper on arxiv.org (abstract plus full PDF text), plus aclanthology.org, proceedings.mlr.press, papers.nips.cc, research.trychroma.com, metr.org and icml.cc. I wrote no files, filed nothing and upgraded no grade.

FAIL is because these checked items do not support their claim as written:
- Q-002: Large Language Monkeys MATH figure.
- Q-002: Kim et al. configuration count.
- Q-002: the "topology beat prompt" reading of MAST.
- Q-003: the code-review false-positive range.
- Q-004: the Amazon regression range.
- Q-004: the attribution of the harness ablation.

The details are in the notes below. Every other checked item supports its claim.

"Supports" means the figure or sentence is in the paper. Quotes are exact.

## Q-002

| Item | Claim | Source opened | Result | Note |
|---|---|---|---|---|
| MAST shares | 14 modes, 3 categories. About 41.8% / 36.9% / 21.3%. 1,600+ traces | arXiv 2503.13657v3 PDF | Supports | The share figure reads "System Design Issues (41.8%), Inter-Agent Misalignment (36.9%), Task Verification (21.3%)". v3 calls the first category "System Design Issues", not "specification". It lists 1,642 traces across 7 frameworks. The NeurIPS 2025 D&B venue is not on the arXiv page. |
| MAST interventions | ChatDev ProgramDev 25.0 / 34.4 / 40.6. Topology beats prompt. "simple fixes are still insufficient" | same, Table 5 (App. H) | Supports the figures. Does not support the reading, and the quote is not in the paper. | The table is: ChatDev ProgramDev 25.0 / 34.4 / 40.6; HumanEval 89.6 / 90.3 / 91.5. AG2 on GSM-Plus is the reverse: with GPT-4, 84.75 / 89.75 (prompt) / 85.50 (topology); with GPT-4o, 84.25 / 89.00 / 88.83. Topology wins only on ChatDev. The text says role specs alone give +9.4% on ChatDev, and "max improvements of 15.6%" (a verification step). The closest sentence to the quote is "not all failure modes are resolved". |
| IFScale | 20 models. Best 68% at 500. Earlier instructions favoured, bias peaking at 150–200 | arXiv 2507.11538 abstract and PDF | Supports | Seven providers. The paper says the primacy bias peaks at 150–200, then fades toward 1.0–1.5 above 300 instructions. The NeurIPS 2025 venue is not on the arXiv page. |
| Yang et al. | "2x as likely to regress", more than 20% drops, +4.8%. Listing all requirements does not reliably help | arXiv 2505.13360v3 | Supports | The abstract also says LLMs infer unspecified requirements by default 41.1% of the time. The ACL 2026 Findings venue is not on the page. |
| Levy et al. | Accuracy about 0.92 to 0.68 at about 3,000 tokens | arXiv 2402.14848; aclanthology 2024.acl-long.818 | Supports | The paper says "on average over all tested models, a drop in accuracy from 0.92 to 0.68". ACL 2024 confirmed. |
| Du et al. | 13.9%–85% across 5 models. The drop persists when irrelevant tokens are masked. Reciting the evidence helps | arXiv 2510.05381 | Supports | Findings of EMNLP 2025 confirmed. The recitation fix gave "up to 4%" for GPT-4o on RULER. |
| Liu et al. | Middle of context used worst. TACL 12:157–173 | arXiv 2307.03172; aclanthology 2024.tacl-1.9 | Supports | The paper is about position, not length. |
| Chroma Context Rot | 18 models degrade with input length | research.trychroma.com/context-rot | Supports | The page says "we evaluate 18 LLMs". It also says distractor impact grows with length. I did not extract numeric distractor figures. |
| Kim et al. | Independent 17.2×, centralised 4.4×. Negative returns above about 45% single-agent accuracy. Up to 70% degradation. "180 configurations" | arXiv 2512.08296v3 | Supports the figures. Does not support "180". | The paper uses 260 configurations. 180 is the subset with full cost tracking. The abstract gives −70.0% on sequential planning, so this is not secondary-only. The 45% effect is β=−0.236 (p=0.004). Cross-validated R²=0.373. |
| Huang et al. | Intrinsic self-correction struggles and sometimes degrades. ICLR 2024 | arXiv 2310.01798 | Supports | Comment line: ICLR 2024. |
| Kamoi et al. | Works with reliable external feedback. TACL 12:1417–1440 | arXiv 2406.01297 | Supports | It is a critical survey. The bottleneck is "feedback generation" in the memo; the abstract says "(2) self-correction works well in tasks that can use reliable external feedback". |
| Panickssery et al. | Judges favour own generations. Self-recognition correlates linearly with self-preference. NeurIPS 2024 | arXiv 2404.13076; papers.nips.cc page | Supports | Same title on the NeurIPS 2024 page. |
| Verga et al. | A panel of diverse models beats a single large judge, with less intra-model bias | arXiv 2404.18796 | Supports | Panel of smaller models from disjoint families. Over 7× cheaper. |
| Who&When | Best method 53.5% agent, 14.2% step. 184 failure tasks. ICML 2025 | arXiv 2505.00212; PMLR v267 listing | Supports | 127 multi-agent systems. "some methods performing below random". |
| METR reward hacking | Models modified tests or scoring code. About 1–2% of o3 attempts | metr.org/blog/2025-06-05-recent-reward-hacking; metr.org/evaluations/openai-o3-report | Supports | The o3 report says "between 1% and 2% of all task attempts by o3 across HCAST and RE-Bench contained some attempt at reward hacking". |
| HAL (Kapoor et al.) | 21,730 rollouts, 9 benchmarks, 9 models. Only 2 benchmarks with the same scaffold for 4 or more models | arXiv 2510.11977 | Supports | The ICLR 2026 venue is not on the arXiv page. |
| Laban et al. | About −39% multi-turn. 200,000+ conversations. 15 models. Unreliability +112%, aptitude −16% | arXiv 2505.06120 | Supports | −35% is in the Figure 1 caption and −39% is the averaged figure, both in the same version. The ICLR 2026 venue is not on the page. |
| Large Language Monkeys | SWE-bench Lite 15.9% to 56% at 250 samples. "MATH 38.7% to 39.8%, 100 to 10,000 samples" | arXiv 2407.21787 | Supports SWE-bench. Does not support the MATH figures. | The paper says: "from 40.50% to 41.41% over the same sample range", with Llama-3-8B-Instruct and majority vote or reward model. The plateau is real; the numbers differ. |
| Smit et al. and arXiv 2502.08788 | Debate does not reliably beat self-consistency or ensembling | arXiv 2311.17371; PMLR v235 (pp. 45883–45905); arXiv 2502.08788 | Supports | 2502.08788 is a position paper: 5 methods, 9 benchmarks, 4 models. |
| Zheng et al. (personas) | 162 personas, 4 families, 2,410 questions, no improvement | arXiv 2311.10054 | Supports | Findings of EMNLP 2024 confirmed. |
| Sclar et al. | Up to 76 points (LLaMA-2-13B). About 10 on average across 50+ tasks. Median spread 6.4 for GPT-3.5 | arXiv 2310.11324 | Supports | Sensitivity persists with model size, shots and instruction tuning. ICLR 2024 confirmed. |
| ProSA | Larger models more robust. Few-shot helps | arXiv 2410.12405 | Supports | EMNLP Findings 2024. |
| He et al. | GPT-3.5 up to 40% by template. GPT-4 more robust | arXiv 2411.10541 | Supports | The page says "Submitted to NAACL 2025". |
| GEPA | Beats MIPROv2 by over 10% (+12 on AIME-2025). Beats GRPO by 6% with up to 35× fewer rollouts | arXiv 2507.19457 | Supports | ICLR 2026 oral. These figures are in the abstract. I did not open arXiv 2607.14004. |
| τ-bench | gpt-4o under 50%. pass^8 under 25% in retail | arXiv 2406.12045 | Supports | |
| Meincke et al. Report 3 | Simple prompt variations "might not be as effective as previously assumed" | arXiv 2508.00614 | Supports | Tipping and threats have no significant effect. |
| SWE-agent | +10.7 points, or 18.0% vs 11.0% on Lite | arXiv 2405.15793 abstract | Not verified | The abstract gives pass@1 12.5% on SWE-bench and 87.7% on HumanEvalFix. I did not open the PDF for the Lite figures. |

I did not re-open the OpenAI SWE-bench Verified screening percentage, Cognition, or Brown et al. beyond the rows above.

### Q-002 library entries that may now be filed

Two independent sources opened:
- F-c: Levy, Du and Chroma. Liu supports the placement point only.
- F-f: Sclar, He and ProSA. The wording must change. Sclar says sensitivity persists with larger models and more shots, while ProSA and He say larger models are more robust and few-shot helps. State the disagreement.
- F-g: Huang and Kamoi.
- F-h: Panickssery, Verga, Wataoka and arXiv 2604.06996 (all opened in Q-003). Say that panels reduce but do not remove the bias.
- F-l: Smit and arXiv 2502.08788.
- P-b: Levy, Du, Liu and Chroma, plus Anthropic.
- P-d: Huang, Kamoi, Panickssery, Verga and METR.
- P-e: Sclar and τ-bench.

One independent source opened. File only as single-source and attributed, not load-bearing:
- F-d: IFScale.
- F-e: Zheng, whose repo has the same authors.
- F-i: Who&When, same authors as its README. Add that this is the best method and some methods were below random.
- F-j: Yang.
- F-k: Laban.
- F-m: Kim. Correct "180" to 260, or say 180 had cost tracking.

Unchanged and outside this pass: F-a, F-b, P-a and P-c, which rest on Anthropic or SWE-agent. The SWE-agent figures are unverified.

### Q-002 conclusions that changed

- The claim that MAST shows topology beating the prompt (§1.5, §3.4 and the K2/K4 rows of §4) holds only for ChatDev ProgramDev. On AG2 GSM-Plus the prompt gain is as large or larger. Weaken it.
- Fix F-m and the Monkeys MATH numbers.
- The direction of the context, self-correction, judge-bias, persona and wording-noise conclusions stands.
- "Several independent sources" is now confirmed for context length and self-correction.

## Q-003

| Item | Claim | Source opened | Result | Note |
|---|---|---|---|---|
| Panickssery et al. | Judges favour own output. Linear link to self-recognition. NeurIPS 2024 | arXiv 2404.13076; papers.nips.cc | Supports | Fine-tuning experiments. |
| Wataoka et al. | Self-preference is tied to lower perplexity (familiar text) | arXiv 2410.21819v2 | Supports | The venue is the NeurIPS 2024 Safe Generative AI Workshop. The memo's "would extend to models with similar training" is its own inference, not in the abstract. |
| arXiv 2604.06996 | Judges favour own or own-family outputs even with objective rubrics. A high rate alone may be leniency | arXiv 2604.06996v3 | Supports | The abstract says judges "can be more than 50% more likely" to mark a failed rubric as satisfied when it is their own. Ensembling helps but does not eliminate the bias. The paper's own text says a high rate alone "does not constitute bias". |
| Bavaresco et al. (Judge-Bench) | 20 datasets, 11 models, large variance by dataset. Validate against humans. ACL 2025 | arXiv 2406.18403; aclanthology 2025.acl-short.20 | Supports | The arXiv comment says "main conference". The Anthology lists it as a short paper (pp. 238–255). |
| MT-Bench paper | Over 80% agreement with humans. Position, verbosity and self-enhancement bias | arXiv 2306.05685 | Supports | NeurIPS 2023 Datasets and Benchmarks. |
| Bowyer et al. | CLT error bars understate uncertainty below a few hundred items. Bayesian or frequentist alternatives | arXiv 2503.01747; proceedings.mlr.press/v267/bowyer25a | Supports | ICML 2025 spotlight position paper, pp. 81143–81184. |
| arXiv 2411.00640 | Paired differences are "free" variance reduction. Clustered SEs can be over 3× naive ones. Power planning | arXiv 2411.00640 PDF | Supports, with one gap | Table 4: "clustered standard errors can be over 3X larger". Paired text: a "free" reduction. The "0.3–0.7" question-score correlation figure is not in the paper (the blog's claim). |
| Kapoor et al. (AI Agents That Matter) | Repeated sampling raises accuracy. Cost-controlled evaluation | arXiv 2407.01502 | Supports | The paper covers retry, warming and majority vote. The TMLR 2025 venue is not on the page. |
| Agent-as-a-Judge | About 90% vs 70% agreement with human consensus on DevAI | arXiv 2410.10934 | Supports | "aligns more closely with the consensus of our human judges (90%) as compared to LLM-as-a-Judge (70%)". The ICML 2025 venue is not on the page. The 76–92% single-human figure was not found by search. |
| arXiv 2505.20206 | 14–22% false positives for GPT-4o and Gemini 2.0 Flash | arXiv 2505.20206 | Does not support as stated | The text reports false-positive rates only in Figure 4, with no 14–22% figure. The text's "up to 22.87%" is a difference in regression and correction ratios. Standard deviations on false-positive rate are 1.02–1.93%. |

### Q-003 library entries that may now be filed

- F-f: Panickssery, Wataoka and 2604.06996 are all opened and independent. Note that Wataoka is a workshop paper.
- F-a: single-origin only. The Anthropic blog and the paper are the same work, so this is not two independent sources. The paper now confirms the statement. Drop the 0.3–0.7 figure.
- F-b: single-origin only. The arXiv, PMLR and repo are all the same authors. The statement is in the abstract, which resolves the earlier "README title only" problem.
- F-e: single-origin, with the chat-preference caveat.
- P-a and P-b: Kapoor and Judge-Bench are now opened, so the cited support is confirmed. They are opinion-grade patterns.
- P-c: still depends on F-a gaining an independent second source.
- F-c, F-d, F-g, F-h and F-i are not C or D items and are unchanged.

### Q-003 conclusions that changed

- "Self-preference reported in several papers" is now confirmed by four opened papers.
- The 14–22% code-review false-positive claim is removed.
- The rest of the conclusions stand.

## Q-004

| Item | Claim | Source opened | Result | Note |
|---|---|---|---|---|
| PromptBridge | "Model drifting". 7 models, 8 benchmarks. Reuse often "substantially worse" | arXiv 2512.01420 | Supports | Example: a GPT-5 prompt scoring 99.39% gets 68.70% on transfer. The blog's "27–39% worse" appears to garble "27.39% improvement on SWE-Bench for o3", which is a gain. Do not use it. |
| Ye et al. (PE2) | No consistent generalisation. The CoT prompt beats all optimised prompts on gpt-3.5-turbo-instruct. Optimised prompts are model-specific | arXiv 2311.05661v3 | Supports | ACL 2024 Findings. Prompts optimised for text-davinci-003 were tested on four other models. The "model-specific prompts that do not reliably generalize" sentence is verbatim. |
| GRACE | Gains largest on DeepSeek-V3, smaller on others, sometimes negative | arXiv 2509.23387, App. Table 7 | Supports | Averages: DeepSeek-V3 77.45 to 94.13; Llama-3.3-70B 77.93 to 85.17; GPT-4.1 74.31 to 80.21. Epistemic on GPT-4.1 falls to 82.50 against 87.00 zero-shot. |
| Sclar findings | 76 points. Persists with size, shots and tuning. Weak correlation between models | arXiv 2310.11324 | Supports | The abstract says "format performance only weakly correlates between models". |
| Mizrahi et al. | TACL 12:933–949. 20 models, 39 tasks, 6.5M instances. "very different performance, both absolute and relative" | arXiv 2401.00595; aclanthology 2024.tacl-1.52 | Supports | |
| He et al. | GPT-3.5 up to 40%. GPT-3.5 MMLU JSON 59.7 vs Markdown 50.0. GPT-4-1106 Markdown 81.2 | arXiv 2411.10541 | Supports | GPT-4-1106 on JSON is 73.9. |
| Lu et al. 2022 | A good ordering for one model "is not transferable to another" | arXiv 2104.08786 abstract | Supports | |
| Evil twins | Optimised on smaller models transfer worse to larger. Larger to smaller transfer well | arXiv 2311.07064 | Supports | EMNLP 2024 Main. |
| MePO | Prompts written by large models can hurt lightweight models | arXiv 2505.09930 | Supports | The abstract: instruction-heavy prompts from advanced LLMs "can overwhelm lightweight inference models". The mechanism differs from evil twins, so the memo's "conflict on direction" is weaker than stated. |
| MUSCLE | Negative flips up to more than 60%. Smaller gap means more flips. Up to 40% reduction | arXiv 2407.09435 | Supports | "significant negative flips (up to more than 60%)". The method reduces but does not remove flips. |
| Amazon regression bugs | Regressions on 1.9%–7.6% of inputs | arXiv 2105.03048 | Partly supports | Text: "A minimum of 1.98% RNF… while the average accuracy gain is only 1.4%". Table 1 values run 1.98%–5.88%. "7.6%" was not found. ACL 2021 main confirmed. |
| Eureka | IFEval gains from older to newer GPT and Llama versions | arXiv 2409.10566 | Supports | GPT-4o 2024-05-13 and Llama 3.1 70B/405B "show significant improvement from earlier versions (GPT-4 1106 Preview and Llama 3 70B)". |
| Evaluating AGENTS.md | No improvement, cost up over 20%. Instructions followed. 138 tasks. Sonnet 4.5, GPT-5.2, GPT-5.1 mini, Qwen3-30B | arXiv 2602.11988v3 | Supports | v3 is consistent: not generally better; resolution rate −0.5% on SWE-bench and −2% on the new set. "Human-written context files should only include instructions required…" The "two abstract versions disagree" issue does not appear in v3. |
| Wharton CoT report | o3-mini +2.9, o4-mini +3.1, Flash 2.5 −3.3. +13.5 and +11.7 for non-reasoning models. 20–80% more time | arXiv 2506.07142 | Supports | These are risk differences in proportion points, not percentages. The +13.5 is Gemini 2.0 Flash and +11.7 is Sonnet 3.5. I did not open SSRN or the Wharton site. |
| Tafreshipour et al. | 1,262 changes, 243 repos, 21.9% documented | arXiv 2412.17298 | Supports | MSR 2025. |
| arXiv 2609.00006 | "System prompt alone regresses performance while structural elements carry the gains" | arXiv 2609.00006 PDF | Partly supports | The sentence is there, but the ablation belongs to Lin et al. [85] (AHE: system prompt −2.3 pp; tools +3.3, middleware +2.2, memory +5.6). The harness study cites it second-hand and calls it "suggestive evidence". |
| arXiv 2605.23950 | Six models within 4.9 points under one scaffold. 9.5-point spread for one model. About 34 points across scaffolds | arXiv 2605.23950 | Supports | 41.0–45.9% under SEAL. Opus 4.5 +9.5 pp (SEAL to Claude Code). The 34-point figure is Sonnet 4.5, 68% to 34% on SWE-bench Verified Mini, cited from HAL. |
| ICML 2026 page | Harness-specific failure patterns replicate across two models | icml.cc/virtual/2026/82739 | Supports | The paper is "The Scaffold Effect in Coding Agents". Qwen 3.6 Plus and MiniMax M2.5, 3 harnesses, 50 tasks. It is a different paper from 2605.23950. |

Not opened in this pass: RLPrompt (2205.12548), GMPO, the HDSR page, the OpenAI prompt-optimiser cookbook and the Wharton site.

### Q-004 library entries that may now be filed

- F-Q004-6: PE2, PromptBridge and GRACE, three independent sources opened. Evil twins and MePO add context. Note that GRACE shows smaller gains, not none.
- F-Q004-7: Sclar and Mizrahi, with He as a third.
- F-Q004-8: MUSCLE and Amazon. Do not quote 1.9–7.6%; use "minimum 1.98%" and the 1.4% average accuracy gain.
- F-Q004-10: single source, the AGENTS.md study. File as single-source and attributed.
- P-Q004-2: the Wharton paper is now opened, so the reference the earlier check dropped can return. Do not describe the numbers as percentages.
- P-Q004-3: hold. The ablation is Lin et al.'s, which I did not open.
- F-Q004-1 to 5 and 9 are B or A and unchanged.

### Q-004 conclusions that changed

- §3.4.3: credit the ablation to Lin et al., reported second-hand.
- §4.3.3: the Amazon range is wrong.
- §3.3.3: the "conflict" between evil twins and MePO is about different mechanisms.
- The main conclusions stand: prompt transfer across models is weak; versions can regress per item despite averages; no controlled evidence on mitigation practices.
