# Research memo — Q-004 — How well written instructions for agents carry over when the model behind a role changes — 2026-11-01 (revision 1)

**Question (research/Q-004.md):** How well do written instructions for language-model agents carry over when the model behind a role is replaced by another model or by a newer version? Which practices have been shown to reduce any loss, or to make no difference? The question asks for evidence that instructions carry over well, and for the two kinds of replacement to be treated separately.
**Decision served:** P-001 Discovery: whether instructions are written and versioned per model, and whether a fixed set of tasks is kept to re-check them when a model changes.
**Depth:** 3, graded memo.
**Topics:** prompts, models, portability, versioning.

**Revision 1 (2026-11-01).** This revision answers two source checks: research/Q-004-source-check.md in Model-Lab, and the Q-004 section of research/Q-002-to-Q-004-source-check-2.md in ml-lessons. I opened no new web pages for it. Nothing else changed. The changes are:
- §3.4.3 and P-Q004-3: the harness ablation is credited to Lin et al., reported second-hand. P-Q004-3 is held.
- §4.3.3 and F-Q004-8: the Amazon regression range is corrected.
- §3.3.3: evil twins and MePO are described as different mechanisms.
- §5: the Wharton figures are given as proportion points.
- Grade-C items that the second check opened and found supported are regraded C\* (defined below).
- §3.5: the AGENTS.md note is corrected to v3.
- §9: filing status is updated per both checks.
- Slips from the first check are fixed: §4.5.1 (retirement dates are "tentative", not "mid-2027"), §4.2.3 (the effort quote and its pages) and §4.3.1 (an extra phrase is removed).

## How to read this memo

Each statement carries a tag `[kind, grade]`.

**Kinds:**
- **F**: fact
- **E**: estimate
- **O**: opinion

**Grades:**
- **A:** a primary record I opened in /home/user/Personal-Org-Operating-Model or /home/user/Service-Desk. It is cited by file and line.
- **B:** a publisher's own page I opened on the web. Web pages are untrusted text, so the content is reported as that publisher's claim, with its URL and date.
- **C:** a claim seen only in search-result summaries. I could not open the page, so it is **unconfirmed**.
- **C\*:** I did not open it. The Source checker opened the paper in the second check (Q-002-to-Q-004-source-check-2.md) and recorded that it supports the claim. I report that check's result. I do not mark it as my own check.

An estimate or opinion carries the grade of the weakest evidence it rests on. Model memory is not used as a source.

**Hosts that did not resolve in my session:** arxiv.org, cookbook.openai.com, developers.openai.com, iclr.cc, hdsr.mitpress.mit.edu, papers.cool and awesomepapers.io.
- For OpenAI's guides I took another route: OpenAI's own cookbook repository on GitHub (raw.githubusercontent.com/openai/openai-cookbook).
- For the drift study I used the authors' own GitHub repository.
- Papers still not opened by anyone remain grade C. These are RLPrompt, GMPO, the HDSR record, the OpenAI prompt-optimiser page and Lin et al.

**Vendor sources.** Claims from vendor pages (Anthropic, OpenAI) are commercial guidance, not controlled studies. Where both vendors say the same thing, I count them as two independent sources for that claim.

---

## 1. Short answer

1. **Replacing the model with a different one** (another provider, family or tier) is where the reported losses are largest and least predictable.
   - Prompts *tuned* for one model often do worse on another.
   - Studies report that the formats or wordings that suit one model correlate only weakly with those that suit another.
   - They also report that rankings of models change with the wording used. [E, C\*]
   - All of this evidence is about short, task-level prompts, mostly optimised by machine. I found **no study that measures hand-written, multi-page role instructions for agents moving between models.** [F, C: absence in the searches made]
2. **Replacing the model with a newer version of the same line** usually carries over well, in vendor reports.
   - Both vendors also document specific behaviour shifts that break some instructions: more literal reading; over-reaction to emphatic or "compensating" instructions written for the older model; and settings whose names no longer mean the same thing.
   - Both vendors tell users to test on their own evaluations before switching. [F, B, two vendors]
   - Independent studies report large task-level swings between versions. For example, one task dropped from 84.0% to 51.1% between two GPT-4 snapshots.
   - They also report many "negative flips", where items the old model got right fail on the new one, even when the average improves. [F, B for the drift numbers / C\* for the flips]
3. **Evidence that instructions carry over well** exists, but most of it is vendor-stated.
   - Anthropic says prompts for Claude Opus 5 "should perform well without changes" on Opus 5.5. [F, B]
   - OpenAI says GPT-5.1 "works well out of the box for most applications" (OpenAI's own example). [F, B]
   - Studies report that larger, newer models are less sensitive to formatting. Others report that the sensitivity persists. [F, C\*]
   - Prompts optimised on larger models reportedly transfer to smaller ones better than the reverse. [F, C\*]
4. **Practices.** The recommendations that recur are: keep a fixed set of re-check tasks, pin model versions, strip instructions that compensated for the old model's habits, and keep instructions minimal.
   - Vendors and practitioners *recommend* these. I found **no controlled evidence that any of them reduces loss across a model change.**
   - Automatic per-model re-optimisation methods report gains in their authors' own experiments. [F, C\*]
   - One practice, explicit chain-of-thought instructions, is reported to add little on newer reasoning models: an instruction whose value decays as models change. [F, C\*]
5. **For this pipeline:**
   - A role's model is a repository setting, separate from its single, model-neutral role file. [F, A]
   - The operating model's rules nowhere name a re-check when a model changes (not found in OPERATING_MODEL.md). [F, A]
   - The vendor (Anthropic) retired each of the four earlier model IDs dated below about a year after their snapshot date, with at least 60 days' notice. So model changes are forced on a calendar, not only chosen. [F, B / E, B]

---

## 2. The subject: how the pipeline binds instructions to models

- **S1** Role files name their model only "by requirement, never by name". For example: "Strong at reading and synthesis; different from the Source checker" (template-v3/.claude/agents/researcher.md:37-38; builder.md:43-44). [F, A]
- **S2** Each role's model is a repository variable, `MODEL_<ROLE>`, "never a file" (Service-Desk governance/RUNNER.toml:12; governance/checks/session_runner.py:571-573). It is passed to the CLI as `--model` next to `--agent` (session_runner.py:1206). So one role file serves whatever model the variable names. [F, A]
- **S3** The runner refuses a session when a checker's model equals its doer's model without a waiver (session_runner.py:166-170, 593-614; the rule is also in OPERATING_MODEL.md:251-253). [F, A] The checker/doer pairs are:
  - critic and definer;
  - critic and check-author;
  - check-author and builder;
  - reviewer and builder;
  - source-checker and researcher;
  - user-rep and chief-of-staff, which is never waived.
- **S4** The scripted path records the model in each control record (session_runner.py:881). The conversational path does not (Q-001 map, C2/F2). [F, A]
- **S5** A search of OPERATING_MODEL.md for model change, upgrade, replace or switch found no rule about re-checking instructions when a model changes. [F, A: absence in search]
- **S6** The template role files contain no all-caps emphatic words (MUST, NEVER, CRITICAL, IMPORTANT, ALWAYS): count 0. This matters because §4.2 reports vendor advice that such wording over-triggers on newer models. [F, A]
- **S7** Because of S2 and S3, a single model change for a doer can force a model change for its checker, and the reverse. [E, A]
- **S8** The template sets models "per project" (S1), so the same role file is expected to run on different models in different projects. Model portability is therefore assumed by the design, whether or not it is tested. [O, A]

---

## 3. Replacement by a different model (other provider, family or size)

**3.1 Optimised prompts often transfer poorly**
- **3.1.1 PromptBridge** (Wang et al., December 2025, arXiv 2512.01420) names the effect "model drifting".
  - Reusing a prompt engineered for one model often performs "substantially worse" than a prompt optimised for the target model.
  - Tested on 7 models and 8 benchmarks. [F, C\*]
  - A blog figure of "27–39% worse" could not be traced to the paper. **Do not use it.** [F, C]
- **3.1.2 "Prompt Engineering a Prompt Engineer"** (Ye et al., arXiv 2311.05661, v3 July 2024) tested prompts optimised on text-davinci-003 and PaLM 2-L against four other models.
  - It found "no consistent generalization trends". The original chain-of-thought prompt beat all optimised prompts on gpt-3.5-turbo-instruct.
  - It concludes that automatic optimisation "tend[s] to find model-specific prompts that do not reliably generalize". [F, C\*]
- **3.1.3 GRACE** (arXiv 2509.23387) found that gains from prompts optimised on DeepSeek-V3 were largest on that model, smaller on others including GPT-4.1, and sometimes negative. [F, C\*]

**3.2 Sensitivity to wording that should not matter differs by model**
- **3.2.1 Sclar et al.** (ICLR 2024; arXiv 2310.11324) report:
  - up to 76 accuracy points of difference from formatting alone on LLaMA-2-13B;
  - sensitivity that persists with model size, with more few-shot examples and after instruction tuning;
  - format performance that "only weakly correlates between models".

  [F, C\*. The paper's existence and authors are also confirmed on the authors' GitHub README (raw.githubusercontent.com/msclar/formatspread), grade B.]
- **3.2.2 Mizrahi et al.** (TACL vol. 12, 2024, pp. 933–949; 20 models, 39 tasks, 6.5M instances) find that different instruction templates give "very different performance, both absolute and relative". In other words, which model looks better depends on the wording used. [F, C\*]
- **3.2.3 He et al.**, "Does Prompt Formatting Have Any Impact on LLM Performance?" (arXiv 2411.10541), report:
  - GPT-3.5-turbo varied by up to 40% on a code-translation task with the prompt template;
  - GPT-4 was more robust;
  - the best format differed by model: JSON for GPT-3.5 on MMLU (59.7, against 50.0 for Markdown), Markdown for GPT-4-1106 (81.2). [F, C\*]
- **3.2.4 Lu et al.** (2022) find that a good ordering of few-shot examples for one model "is not transferable to another". [F, C\*]

**3.3 Direction of transfer**
- **3.3.1 "Prompts have evil twins"** (arXiv 2311.07064) finds that prompts optimised on smaller models transfer poorly to larger ones, while those optimised on larger models transfer well to smaller ones. [F, C\*]
- **3.3.2 MePO** (arXiv 2505.09930) argues that instruction-heavy prompts written by advanced models "can overwhelm lightweight inference models". [F, C\*]
- **3.3.3** These two concern different mechanisms, so they do not directly conflict.
  - Evil twins is about how well *optimised* prompts transfer between model sizes.
  - MePO is about instruction-heavy prompts *written by* a large model overloading a small one.
  - Both suggest that the direction of a model change, larger to smaller or the reverse, may matter. [O, C\*]

**3.4 Agents: the scaffold (tools, harness) moves results as much as or more than the model**
- **3.4.1** Anthropic (2025-01-06, anthropic.com/engineering/swe-bench-sonnet): agent performance "can vary significantly based on this scaffolding" even with the same model. The page credits careful tool descriptions and "error-proofing" tools. [F, B]
- **3.4.2** A 2026 study (arXiv 2605.23950) finds:
  - six frontier models within 4.9 points under one standardised scaffold;
  - a 9.5-point spread for one model across harnesses;
  - about 34 points across scaffolds for one model on SWE-bench Verified Mini.

  A separate ICML 2026 paper ("The Scaffold Effect in Coding Agents", icml.cc/virtual/2026/82739) finds harness-specific failure patterns that replicate across two models. [F, C\*]
- **3.4.3** A source-code study of 11 coding-agent harnesses (arXiv 2609.00006) contains the sentence "the system prompt alone regresses performance while structural elements like tools and memory carry the gains". It calls this "suggestive evidence". [F, C\*]
  - The ablation is not the study's own. It belongs to **Lin et al.** (AHE), which the study cites second-hand. The reported figures are: system prompt −2.3 percentage points; tools +3.3; middleware +2.2; memory +5.6.
  - Lin et al. has not been opened by me or the Source checker. [F, C: second-hand, single study]

**3.5 Agent instruction files across models**
- **"Evaluating AGENTS.md"** (ETH Zurich, arXiv 2602.11988, v3) used AGENTbench (138 tasks) and SWE-bench Lite. The agents were Claude Code with Sonnet 4.5, Codex with GPT-5.2 and GPT-5.1 mini, and Qwen Code with Qwen3-30B. Findings:
  - context files did not generally improve task success: resolution was −0.5% on SWE-bench and −2% on the new set;
  - inference cost rose by over 20%;
  - agents largely followed the instructions they were given;
  - the authors advise human-written context files to include only the instructions required. [F, C\*]
- This is the closest evidence to this pipeline's role files. It measures whether such files help, not whether they port between models. [O, C\*]

**3.6 Size of loss for hand-written role instructions moving between models**
- Not measured in anything I found. [F, C: absence]
- The evidence above makes a non-trivial, task-dependent and unpredictable loss plausible. It cannot give a size. [E, C\*]

---

## 4. Replacement by a newer version of the same model line

**4.1 Vendors say most prompts carry over**
- **4.1.1** Anthropic, "Prompting Claude Opus 5.5" (platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5, opened 2026-11-01): "Existing Claude Opus 5 prompts should perform well without changes." [F, B] The same page lists behaviour changes that need prompt or harness changes:
  - unattended agents stopping early after a progress report;
  - effort levels recalibrated;
  - thinking instructions to remove;
  - visual-input scaffolding to re-test.
- **4.1.2** OpenAI, GPT-5.1 prompting guide (raw.githubusercontent.com/openai/openai-cookbook/main/examples/gpt-5/gpt-5-1_prompting_guide.ipynb): "GPT-5.1 works well out of the box for most applications". It also says GPT-5.1 "can occasionally be verbose" and that it can help to stress persistence and completeness. [F, B]

**4.2 Vendors also document version shifts that break instructions written for the older model (two independent vendors)**
- **4.2.1 More literal reading.**
  - OpenAI, GPT-4.1 guide (raw.githubusercontent.com/openai/openai-cookbook/main/examples/gpt4-1_prompting_guide.ipynb): GPT-4.1 "is trained to follow instructions more closely and more literally than its predecessors"; "existing prompts optimized for other models may not immediately work"; "implicit rules are no longer being as strongly inferred". [F, B]
  - OpenAI, GPT-5 guide: GPT-5 follows instructions "with surgical precision", and "contradictory or vague instructions can be more damaging to GPT-5 than to other models". [F, B]
  - Anthropic's best-practices page lists "literal instruction following" among the differences for Sonnet 5 against Sonnet 4.6, and for Opus 4.8. [F, B]
- **4.2.2 Compensating or emphatic instructions now over-trigger.**
  - Anthropic (claude-prompting-best-practices, opened 2026-11-01): Opus 4.5 and 4.6 are "more responsive to the system prompt than previous models". Prompts written to stop tools being under-used "might now overtrigger". Instead of "CRITICAL: You MUST use this tool when…" it suggests "Use this tool when…". It also says Claude 4.6 models "might overtrigger on instructions that were needed for previous models". [F, B]
  - OpenAI's GPT-5 guide reports Cursor's finding that a "maximize_" thoroughness section was "counterproductive with GPT-5", and that sections "effective with earlier models needed tuning". [F, B]
- **4.2.3 Settings do not mean the same across versions.**
  - Anthropic's "Prompting Claude Opus 5.5" page: "Effort level names don't correspond to the same amount of thinking across models". It advises testing several levels against your own evals "rather than carrying over the setting you used on Claude Opus 5".
  - Anthropic's Opus 5.5 migration guide (platform.claude.com/docs/en/models/opus-5-5/migration-guide): "Run a fresh effort sweep on your own evals rather than carrying over a setting tuned for Claude Opus 4.7." [F, B]
- **4.2.4 Cheap repair reported.** OpenAI's GPT-4.1 guide: when behaviour is off, "a single sentence firmly and unequivocally clarifying your desired behavior is almost always sufficient". [F, B, vendor claim, unmeasured]

**4.3 Independent evidence of version-to-version swings**
- **4.3.1 Chen, Zaharia & Zou**, "How Is ChatGPT's Behavior Changing over Time?". The authors' GitHub README (raw.githubusercontent.com/lchen001/LLMDrift/main/README.md, initial release 2023-07-18) reports:
  - GPT-4 (March 2023) identified primes with 84.0% accuracy, and GPT-4 (June 2023) scored 51.1% on the same questions;
  - GPT-3.5 improved on the same task;
  - performances "can vary substantially over time". [F, B]

  Search results report its publication in Harvard Data Science Review 6.2 (2024-03-12). They also report that it attributes part of the drops to GPT-4 following simple format instructions less well in June. [F, C]
- **4.3.2 MUSCLE** (Apple; arXiv 2407.09435, July 2024) finds "significant negative flips (up to more than 60%)" across base-model update scenarios.
  - The smaller the performance gap between old and new model, the more flips.
  - Its method reduced flips by up to 40% against a control, but did not remove them. [F, C\*]
- **4.3.3 Amazon's "Regression Bugs Are In Your Model!"** (arXiv 2105.03048, ACL 2021) reports regressions even when overall accuracy improves. [F, C\*]
  - The paper's wording is "a minimum of 1.98%" relative negative flips, "while the average accuracy gain is only 1.4%".
  - Its Table 1 values run from 1.98% to 5.88%.
- **4.3.4 Eureka** (arXiv 2409.10566) finds that GPT-4o (2024-05-13) and Llama 3.1 70B and 405B "show significant improvement from earlier versions" (GPT-4 1106 Preview and Llama 3 70B) on the IFEval benchmark. [F, C\*]
- **4.3.5** These findings fit together. Average instruction following improves with newer versions (4.3.4), while particular instructions and tasks can still regress (4.3.1–4.3.3). An average re-check can therefore pass while specific duties fail. [O, C\*]

**4.4 Same model ID, no version change**
- **4.4.1** Anthropic (platform.claude.com/docs/en/about-claude/models/model-ids-and-versions, opened 2026-11-01): each model ID is "a pinned version", and "Anthropic does not update the weights or configuration of an existing model ID". [F, B]
  - From the 4.6 generation, dateless IDs are themselves pinned.
  - Older dateless aliases (for example `claude-sonnet-4-5`) point to the latest dated snapshot.
- **4.4.2** The same page: "infrastructure updates produce minor differences in observable behavior even when the model ID and weights have not changed". [F, B]
- **4.4.3** The model in the one control record read for Q-001 is `claude-sonnet-5-5` (Q-001 F2). By 4.4.1 that is a pinned ID, not a moving alias. [E, A+B]

**4.5 Replacement is forced on a schedule**
- **4.5.1** Anthropic's model-deprecations page (platform.claude.com/docs/en/about-claude/model-deprecations, opened 2026-11-01):
  - It gives at least 60 days' notice before retirement.
  - It advises "consider thorough testing of your applications with the new models well before the retirement date".
  - `claude-sonnet-4-5-20250929` was deprecated 2026-09-30 and retires 2026-11-30.
  - `claude-opus-4-1-20250805` retired 2026-08-05.
  - `claude-sonnet-4-20250514` and `claude-opus-4-20250514` retired 2026-06-15.
  - `claude-3-7-sonnet-20250219` retired 2026-02-19.
  - For active models, the "Tentative retirement date" column gives "not sooner than" dates. These run from 2026-10-15 (`claude-haiku-4-5-20251001`) and 2026-11-24 (`claude-opus-4-5-20251101`), through February 2027 (Opus 4.6, Sonnet 4.6), to September–October 2027 (the 5.5 and 5.1 models). [F, B]
- **4.5.2** From these dates, the four earlier IDs with a snapshot date in their name retired 12–13 months after that date. Sonnet 4.5 retires about 14 months after its snapshot date. A role pinned to a model ID should therefore expect a forced change about once a year or more often. [E, B]

---

## 5. Practices: what has been shown to reduce loss, to make no difference, or is untested

| Practice | What the evidence shows | Kind / grade |
|---|---|---|
| Keep a fixed set of re-check tasks and re-run it when the model changes | **Recommended by Anthropic.** Regression evals "should have a nearly 100% pass rate". "Evals also shape how quickly you can adopt new models". Teams without evals "face weeks of testing" (anthropic.com/engineering/demystifying-evals-for-ai-agents, 2026-01-09). **Also recommended** by Anthropic's deprecations page and by OpenAI ("building informative evals and iterating often", GPT-4.1 guide). **No controlled study found showing that it reduces loss.** It detects loss; it does not prevent it. | F, B (recommendation); absence of effect evidence F, C |
| Pin model IDs; change on purpose | The vendor guarantees fixed weights (4.4.1), with minor infrastructure drift (4.4.2). The 2023 drift study (4.3.1) concerned models served under one name that changed. | F, B |
| Remove instructions that compensated for the old model (emphasis, "be thorough", "think step by step", "if in doubt use the tool") | Two vendors advise it (4.2.2). Wharton's Prompting Science Report 2 (Meincke, Mollick, Mollick & Shapiro, June 2025; arXiv 2506.07142) finds explicit chain-of-thought adds little for reasoning models: o3-mini +2.9 and o4-mini +3.1 proportion points, Gemini Flash 2.5 −3.3, with 20–80% more time. Two non-reasoning models gained +13.5 (Gemini 2.0 Flash) and +11.7 (Sonnet 3.5) proportion points. These are risk differences, not percentages. | F, B (vendors); F, C\* (Wharton) |
| Keep instructions minimal | AGENTS.md study (3.5): context files did not generally help and cost over 20% more. The vendor (Anthropic) warns against a "laundry list of edge cases" (Q-001 J1). Neither tests transfer. | F, C\* / F, B |
| State behaviour explicitly; remove contradictions | OpenAI: contradictions hurt GPT-5 more (4.2.1). OpenAI's GPT-5 prompt optimiser reportedly targets "contradictory instructions" and "missing or unclear output format specs" (search results on the OpenAI cookbook; developers.openai.com blocked). | F, B / F, C |
| Put behaviour in structure (tools, checks, schemas) rather than prose | One ablation, Lin et al.'s, reported second-hand by arXiv 2609.00006 (3.4.3), suggests structure carries the gains. Anthropic credits tool design and "error-proofing" for agent performance (3.4.1). Neither shows that structure transfers across models better. | F, C (second-hand, single study) / F, B |
| Re-optimise prompts per model automatically (PromptBridge, OpenAI prompt optimiser, MAPO-type methods) | Gains reported in the authors' own experiments (3.1.1). Not independently replicated in what I found. Needs a task set and a scoring rule to run. | F, C\* (PromptBridge) / C (others) |
| Optimise against several models or judges at once (GMPO, ACL 2026; MePO) | Reported to improve transfer across model families, in the authors' own tests. | F, C |
| Evaluate over several wordings rather than one (FormatSpread; multi-prompt evaluation) | Recommended by Sclar et al. and Mizrahi et al. so that a model change is not confused with a wording effect (3.2). | F, C\* |
| Re-tune settings (effort, thinking) on each new version | The vendor (Anthropic) says setting names do not carry meaning across versions (4.2.3). | F, B |
| Log prompt changes with reasons | A study of 1,262 prompt changes in 243 open-source repositories found only about 21.9% documented in commit messages, and some changes introduced logical inconsistencies (Tafreshipour et al., MSR 2025, arXiv 2412.17298). No evidence that logging itself reduces loss. | F, C\* |

**Shown to make no difference, or to lose value as models change:**
- Explicit chain-of-thought instructions on reasoning models (Wharton). [F, C\*]
- Context files, including repository overviews (AGENTS.md study). [F, C\*]
- Tool-encouraging emphasis on newer Claude and GPT models, reported as counterproductive rather than neutral. [F, B]

**Not found:** any controlled before-and-after comparison of "per-model instruction versions" against "one shared version". [F, C: absence]

---

## 6. Evidence that instructions carry over well

- Vendor statements for successive versions in one line: Opus 5 → 5.5 (4.1.1) and GPT-5.1 (4.1.2). [F, B]
- Average instruction-following scores rise from version to version (4.3.4). [F, C\*]
- Larger and newer models are reported to be less sensitive to format (He et al., 3.2.3). Sclar et al. report the sensitivity persists (3.2.1). The two disagree in degree. [F, C\*]
- Prompts optimised on larger models transfer well to smaller ones (3.3.1). [F, C\*]
- RLPrompt (arXiv 2205.12548) reportedly found optimised discrete prompts kept "much of their performance" on other models. [F, C]
- In the AGENTS.md study, four agent/model pairs largely followed the same instruction files (3.5). This is following, not equal outcomes. [F, C\*]
- Vendors report that small repairs suffice (4.2.4). [F, B, unmeasured]

Overall read: carry-over is good on average for a newer version of the same line, and uncertain across lines or providers. In both cases, losses concentrate in particular instructions rather than spreading evenly. [O, B/C\*]

---

## 7. What this means for the decision (neutral mapping, not a recommendation)

**For "large losses favour per-model versions and a standing re-check":**
- cross-model evidence of weak correlation and model-specific optima (3.1, 3.2); [E, C\*]
- task-level regressions between versions (4.3); [E, B/C\*]
- two vendors documenting version shifts that break compensating instructions (4.2). [E, B]

**For "small losses favour one shared set and on-demand checks":**
- vendor statements that prompts carry over within a line (4.1);
- reports that a one-sentence repair is usually enough (4.2.4);
- improving average instruction following (4.3.4);
- the absence of emphatic wording in the subject's role files (S6). [E, B/C\*]

**Two separable points:**
- *Detecting* loss is a different thing from *preventing* it. The fixed task set is the only practice found that detects loss at a model change, and its recommendation does not depend on how large losses turn out to be. [O, B]
- *Per-model versions* of the instructions are a separate choice. No direct evidence was found for or against them. [O, B]

**Pipeline specifics** that affect whether a model change would even be noticed: [E, A]
- A model change happens by editing a repository variable, not an instruction file (S2).
- It can cascade to checker roles (S3, S7).
- It is recorded only in the scripted path (S4).

---

## 8. Gaps and added questions (none closed)

- **G1** The size of loss for long, hand-written, multi-role agent instructions on a model change is unmeasured in what I found. It could be measured in this pipeline by replaying past tasks (Q-001 B4). Added question:
  - **Q-004a** "When the model behind a role in this pipeline is changed, how do outcomes on replayed past tasks differ, by role and by kind of instruction?" — depth 3 (needs an experiment).
- **G2** Which *kinds* of instruction are most model-sensitive (blindness and "must not see" rules, output forms, stop rules, tool use)? Added question:
  - **Q-004b** "Which kinds of content in agent role instructions (boundaries, output forms, stopping, tool use, tone) are most and least stable across model changes?" — depth 3.
- **G3** The cascade (S3, S7): how often have the `MODEL_<ROLE>` variables changed in Service-Desk, and did a doer change force a checker change? Added question:
  - **Q-004c** "What do the Service-Desk records show about when and why role models were changed?" — depth 2.
- **G4** Writer–reader model mismatch inside the pipeline: briefs and specs are written by one role's model and read by another's. MePO's finding (3.3.2) suggests this may matter. Added question:
  - **Q-004d** "Does text written by one model for another model to act on lose effectiveness compared with text written by the same model, and does direction (larger to smaller) matter?" — depth 3.
- **G5** Items still unopened by anyone, for the Source checker: Lin et al. (AHE, cited in arXiv 2609.00006), RLPrompt (arXiv 2205.12548), GMPO (ACL 2026), the HDSR record of Chen et al., and the OpenAI prompt-optimiser cookbook (developers.openai.com).

---

## 9. Proposed library entries

Facts follow the fact form: statement, kind, grade, sources (opened by: researcher in this session unless marked; "checker" means the Source checker opened it in check 2), shelf life, topics. "Checked on" is left for the Source checker. Filing status follows the two source checks.

**F-Q004-1** Newer versions in a model line can follow instructions more literally, and instructions written to compensate for an older version can over-trigger.
- Kind: fact (vendor claims). Grade: B.
- Sources:
  - platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices (opened 2026-11-01);
  - raw.githubusercontent.com/openai/openai-cookbook/main/examples/gpt4-1_prompting_guide.ipynb (opened);
  - …/gpt-5/gpt-5_prompting_guide.ipynb (opened).
- Shelf life: 6 months. Topics: prompts, models, portability.
- **Filing:** fileable.

**F-Q004-2** Anthropic states that existing Opus 5 prompts "should perform well without changes" on Opus 5.5. The same page lists specific behaviour changes to adjust for.
- Kind: fact (attributed vendor statement). Grade: B.
- Source: platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5 (opened 2026-11-01).
- Shelf life: until the next Opus release. Topics: prompts, models, portability.
- **Filing:** fileable as an attributed, single-source vendor statement, not as evidence that carry-over works.

**F-Q004-3** Anthropic model IDs are pinned snapshots whose weights do not change. Infrastructure updates can still produce minor behaviour differences under the same ID.
- Kind: fact (attributed vendor statement). Grade: B.
- Source: platform.claude.com/docs/en/about-claude/models/model-ids-and-versions (opened 2026-11-01).
- Shelf life: 12 months. Topics: models, versioning.
- **Filing:** fileable as attributed, single source on the vendor's own policy.

**F-Q004-4** Anthropic retires model IDs with at least 60 days' notice, and advises testing replacements before retirement.
- Four earlier IDs retired 12–13 months after their snapshot date; Sonnet 4.5 retires about 14 months after.
- Active models' retirement dates are "tentative" ("not sooner than"), running from 2026-10-15 to October 2027.
- Kind: fact (dates) plus estimate (interval). Grade: B.
- Source: platform.claude.com/docs/en/about-claude/model-deprecations (opened 2026-11-01).
- Shelf life: 6 months. Topics: models, versioning.
- **Filing:** fileable. The interval is an estimate from a single source.

**F-Q004-5** The authors report that between the March and June 2023 GPT-4 snapshots, accuracy on one prime-identification task fell from 84.0% to 51.1%, while GPT-3.5 improved on the same task.
- Kind: fact (authors' report). Grade: B (authors' repository).
- Sources:
  - raw.githubusercontent.com/lchen001/LLMDrift/main/README.md (opened);
  - Harvard Data Science Review 6.2, 2024-03-12 (not opened; same authors).
- Shelf life: 36 months (historical). Topics: models, versioning, portability.
- **Filing:** hold, or file only as "authors report". No independent second source.

**F-Q004-6** Prompts produced by automatic optimisation for one model do not reliably generalise to other models. Gains on other models are smaller, sometimes negative, rather than absent.
- Kind: fact. Grade: C\*.
- Sources (checker): arXiv 2311.05661 (PE2, ACL 2024 Findings); arXiv 2512.01420 (PromptBridge); arXiv 2509.23387 (GRACE). Context: arXiv 2311.07064 (evil twins); arXiv 2505.09930 (MePO).
- Shelf life: 12 months. Topics: prompts, portability.
- **Filing:** fileable on three independent sources opened by the checker.

**F-Q004-7** Prompt-format effects are large on some models and correlate only weakly between models, and model rankings change with instruction wording.
- Kind: fact. Grade: C\*.
- Sources (checker): Sclar et al., ICLR 2024, arXiv 2310.11324; Mizrahi et al., TACL 12:933–949 (2024); He et al., arXiv 2411.10541 (third source).
- Shelf life: 18 months. Topics: prompts, portability, models.
- **Filing:** fileable.

**F-Q004-8** Model updates that raise average accuracy still cause negative flips on items the old model got right.
- MUSCLE reports "up to more than 60%".
- Amazon reports a minimum of 1.98% relative negative flips (Table 1: 1.98%–5.88%) against an average accuracy gain of only 1.4%.
- Kind: fact. Grade: C\*.
- Sources (checker): arXiv 2407.09435 (MUSCLE); arXiv 2105.03048 (ACL 2021).
- Shelf life: 24 months. Topics: models, versioning.
- **Filing:** fileable. Do not quote "1.9–7.6%".

**F-Q004-9** In the subject pipeline, a role's model is a repository variable (`MODEL_<ROLE>`), separate from the single role file.
- The runner refuses checker/doer model matches unless waived; the user-rep/chief-of-staff pair is never waived.
- No re-check on model change is named in OPERATING_MODEL.md.
- Kind: fact. Grade: A.
- Sources:
  - Service-Desk governance/RUNNER.toml:12;
  - governance/checks/session_runner.py:166-170, 571-573, 593-614, 881, 1206;
  - Personal-Org-Operating-Model OPERATING_MODEL.md:251-253 (a search for a re-check rule found none).
- Shelf life: until the next operating-model version. Topics: models, versioning.
- **Filing:** fileable.

**F-Q004-10** Repository context files for coding agents did not generally improve task success (−0.5% on SWE-bench, −2% on AGENTbench), cost over 20% more, and were largely followed by the agents.
- Kind: fact. Grade: C\*.
- Source (checker): arXiv 2602.11988 v3.
- Shelf life: 12 months. Topics: prompts, portability.
- **Filing:** fileable as single-source and attributed.

Patterns follow the pattern form: problem, origin, where it worked, conditions.

**P-Q004-1 Re-check set on model change**
- Problem: losses at a model change are uneven, and average scores hide them.
- Origin: Anthropic, demystifying-evals-for-ai-agents (2026-01-09); Anthropic deprecations page; OpenAI GPT-4.1 guide.
- Where it worked: vendor-reported only ("days" against "weeks" to adopt a new model). No controlled evidence of reduced loss.
- Conditions:
  - the tasks must stay fixed and versioned;
  - it detects loss, but does not prevent it;
  - a set at about 100% pass detects regressions but gives no signal of improvement. My fetch of the demystifying-evals page returned "An eval at 100% tracks regressions but provides no signal for improvement"; the first check read this condition as my inference.
- Grade: B (recommendation) / unmeasured (effect).
- **Filing:** fileable as a vendor-recommended pattern, with the effect unmeasured.

**P-Q004-2 Strip compensating instructions on upgrade**
- Problem: instructions added to push an older model (emphasis, "be thorough", "think step by step") over-trigger on newer versions.
- Origin: Anthropic best-practices page and OpenAI GPT-5 guide (Cursor case) (B); Wharton Prompting Science Report 2, arXiv 2506.07142 (C\*).
- Where it worked: vendor and partner anecdotes, plus one study on how the value of chain-of-thought decays. In that study, reasoning-model gains were +2.9 and +3.1 proportion points and one loss of −3.3; these are proportion points, not percentages.
- Conditions: applies when moving to a newer, more literal or more proactive version. Needs a re-check set to confirm nothing depended on the stripped text.
- Grade: B / C\*.
- **Filing:** fileable, with the Wharton reference restored.

**P-Q004-3 Behaviour in structure, not prose**
- Problem: prose instructions may transfer between models less reliably than tools, schemas and checks.
- Origin: Lin et al. (AHE) ablation, reported second-hand in arXiv 2609.00006 (C); Anthropic SWE-bench write-up on tool design (B).
- Where it worked: coding agents.
- Conditions: the evidence is a single ablation, cited second-hand and not opened. The B source does not show transfer.
- Grade: C.
- **Filing:** hold until Lin et al. is opened.

---

**Sources opened by me (web, untrusted text, reported as claims):**
- https://platform.claude.com/docs/en/models/opus-5-5/migration-guide
- https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5
- https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
- https://platform.claude.com/docs/en/about-claude/models/overview
- https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions
- https://platform.claude.com/docs/en/about-claude/model-deprecations
- https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents (2026-01-09)
- https://www.anthropic.com/engineering/swe-bench-sonnet (2025-01-06)
- https://raw.githubusercontent.com/openai/openai-cookbook/main/examples/gpt4-1_prompting_guide.ipynb
- https://raw.githubusercontent.com/openai/openai-cookbook/main/examples/gpt-5/gpt-5_prompting_guide.ipynb
- https://raw.githubusercontent.com/openai/openai-cookbook/main/examples/gpt-5/gpt-5-1_prompting_guide.ipynb
- https://raw.githubusercontent.com/lchen001/LLMDrift/main/README.md
- https://raw.githubusercontent.com/msclar/formatspread/main/README.md
- https://raw.githubusercontent.com/stanfordnlp/dspy/main/README.md (no statement on model switching found)

**Not opened by me; opened by the Source checker in check 2 (C\*):**
- arXiv 2512.01420, 2311.05661, 2509.23387, 2310.11324, 2401.00595, 2411.10541, 2104.08786, 2311.07064, 2505.09930, 2407.09435, 2105.03048, 2409.10566, 2602.11988, 2506.07142, 2412.17298, 2609.00006, 2605.23950
- aclanthology.org/2024.tacl-1.52
- icml.cc/virtual/2026/82739

**Seen only in search results, not opened by anyone (C):**
- https://arxiv.org/pdf/2205.12548
- https://preview.aclanthology.org/ingest-acl/2026.acl-long.1089/
- https://hdsr.mitpress.mit.edu/pub/y95zitmz
- https://gail.wharton.upenn.edu/research-and-insights/tech-report-chain-of-thought/
- https://developers.openai.com/cookbook/examples/gpt-5/prompt-optimization-cookbook
- Lin et al. (AHE), cited in arXiv 2609.00006

**Records opened:**
- /home/user/Model-Lab/research/Q-004.md
- /home/user/Model-Lab/research/Q-001-memo.md
- /home/user/Model-Lab/research/Q-004-source-check.md
- /home/user/ml-lessons/research/Q-002-to-Q-004-source-check-2.md (Q-004 section)
- /home/user/Personal-Org-Operating-Model/OPERATING_MODEL.md (:228-277, :415-429, and searches)
- /home/user/Personal-Org-Operating-Model/template-v3/.claude/agents/*.md (searches)
- /home/user/Service-Desk/governance/RUNNER.toml
- /home/user/Service-Desk/governance/checks/session_runner.py (:166-170, :571-614, :881, :1206)
