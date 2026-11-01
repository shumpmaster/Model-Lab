# Research memo: Q-002, what determines the quality of a session's work in multi-step LLM-agent pipelines (2026-11-01)

**Depth:** 3 (graded memo). **Researcher:** researcher session, blind under D-055. **Question:** research/Q-002.md. **Topics:** prompts, agents, instructions, context, task-division, quality.

## How to read this memo

Every statement is marked **[fact]**, **[estimate]** or **[opinion]**, with a grade:

- **A**: a primary record I opened in /home/user/Personal-Org-Operating-Model or /home/user/Service-Desk. I used these only to describe the subject. They are not evidence of what works.
- **B**: a publisher's own page that I opened. It is untrusted text, so I report it as that publisher's claim, with its URL and date. Vendor results come from one source about the vendor's own systems and have not been replicated independently.
- **C**: a peer-reviewed paper or preprint I could not open. What I report comes from search-result summaries of its abstract or listing. These items are **unconfirmed** until the Source checker opens the paper.
- **D**: secondary write-ups only, or figures that differ between versions of a paper. Weak.

**Access in this session.** These hosts did not resolve and could not be opened: arxiv.org, neurips.cc, openreview.net, aclanthology.org, mlanthology.org, huggingface.co, alphaxiv.org, api.semanticscholar.org, research.google, research.trychroma.com and cognition.ai. I stopped trying new hosts after that. Only anthropic.com and github.com opened. For a paper, GitHub READMEs usually confirm only the title, authors and venue, not the figures. As a result, most of the academic evidence below is grade C. The Source checker needs arxiv.org, aclanthology.org, openreview.net, proceedings.neurips.cc / proceedings.mlr.press and research.google allowed to raise it.

Model memory is not used as a source.

---

## 1. Bottom line

1. **[fact, C, several independent sources] No study I found divides the variation in agent-pipeline output across all five levers in the question** (instructions, model, inputs/context, task division, tools, checks). The only published variance split I found leaves instructions out (item 2). So "what share do instructions explain?" has **no direct answer in the literature** I could reach.
2. **[fact, B, one source] Anthropic reports that three factors explained 95% of the variance in its multi-agent research system's BrowseComp score:**
   - token usage by itself explained 80%;
   - the other two factors were the number of tool calls and the choice of model.

   ([anthropic.com/engineering/multi-agent-research-system](https://www.anthropic.com/engineering/multi-agent-research-system), 2025-06-13.) This is the vendor's own internal analysis. "Token usage" is the effort the agents spent, not the size of the inputs they were handed.
3. **[fact, B] With the scaffold held fixed, changing the model moved SWE-bench Verified from 22% (Claude 3 Opus) to 33% (Claude 3.5 Sonnet, old) to 49% (Claude 3.5 Sonnet, new).** The same post says agent performance "can vary significantly based on this scaffolding, even when using the same underlying AI model" ([anthropic.com/engineering/swe-bench-sonnet](https://www.anthropic.com/engineering/swe-bench-sonnet), 2025-01-06).
4. **[estimate, B+C]** On the evidence reached, the **model** and the **effort and context the session works with** are the largest single levers on capability-limited tasks. **Instructions** are the largest lever on a narrower set of failures:
   - delegation and task description;
   - role compliance;
   - leaving out requirements (underspecification).
5. **[estimate, B+C]** Instructions have been found to be the limiting factor in these cases:
   - vague delegation between agents (Anthropic, B);
   - underspecified requirements (Yang et al., C);
   - automated prompt optimisation on fixed pipelines (GEPA, C).

   They have been found **not** to be limiting, or to have small and unreliable effects, in these cases:
   - personas and role phrasing (C);
   - chain-of-thought instructions on recent models (C);
   - adding more requirements or longer instruction lists (C);
   - MAST's prompt-only repair of multi-agent failures, where a topology change did more (C/D);
   - minimal scaffolds with strong models (B).
6. **[estimate, C]** Checks help only as far as the check signal is reliable:
   - self-review without external feedback does not reliably fix reasoning errors;
   - repeated attempts are limited by the verifier;
   - LLM judges favour their own outputs;
   - automated failure attribution names the right agent about half the time and the right step about one time in seven.

   **I found no evidence on the best number of checkers or review rounds in an agent pipeline. This is a gap.**
7. **[opinion]** For P-001, the evidence supports treating instructions as **one lever among several, not the main one**, and measuring rather than assuming the instruction share. That is the third branch of "what each answer would change": the evidence is thin, so the project's own measurement carries weight. The strongest instruction-side candidates in the literature are the specificity of task descriptions and requirements at handoffs, and the form of checker findings. The levers with the strongest evidence that sit outside instructions are context size and quality, task division (topology) and the reliability of checks.

---

## 2. Failure kinds covered, and those left out

**Covered** (labels are mine; MAST's three categories are mapped where they apply):

| # | Failure kind | Rough MAST mapping |
|---|---|---|
| K1 | Task misread or underspecified; work done to the wrong target | Specification issues |
| K2 | Role or instruction non-compliance, including instructions dropped as their number grows | Specification issues ("disobey task/role specification") |
| K3 | Degradation from long, distracting or badly placed context | (not a MAST category) |
| K4 | Information lost at handoff; agents misaligned, duplicating or contradicting each other | Inter-agent misalignment |
| K5 | False or premature completion; weak or absent verification | Task verification |
| K6 | Tool misuse | (not a MAST category) |
| K7 | Run-to-run unreliability and brittleness to formatting or wording | (cross-cutting) |
| K8 | Checker failures: biased judging, gamed checks, failures misattributed in triage | Task verification |
| K9 | Runaway effort or cost (over-spawning, token blow-up) | (cross-cutting) |

**Left out:**
- Prompt injection and adversarial input. This is covered by the pipeline's Input-reader rule and needs its own question.
- Factual hallucination in research outputs, beyond K5.
- Security and credentials.
- Latency.
- How well questions put to the owner are written.
- Loss when the model behind a role changes (this is Q-001's research shortlist item 3).
- Human factors in the owner's review.
- Long-horizon memory across sessions. Sessions here are fresh by design, A: template-v3/.claude/agents/builder.md:8.

**[fact, C/D] MAST category shares.** Cemri et al., *Why Do Multi-Agent LLM Systems Fail?*, NeurIPS 2025 Datasets & Benchmarks, arXiv 2503.13657. The paper identifies 14 failure modes in 3 categories; the GitHub repo opened (B) confirms the title, the authors and "over 1K annotated MAS traces". Secondary sources give these shares:
- specification about 41.8%;
- inter-agent misalignment about 36.9%;
- task verification about 21.3%.

I could not see these shares in the paper (D). Trace counts also differ between versions (200+ tasks vs 1,600+ traces). Unconfirmed.

---

## 3. Evidence by lever

### 3.1 The model

- **[fact, B]** Same scaffold, different models: 22% → 33% → 49% on SWE-bench Verified (swe-bench-sonnet, 2025-01-06).
- **[fact, B]** Model choice is one of the three factors in the 95% BrowseComp variance split (multi-agent-research-system, 2025-06-13).
- **[fact, B, project's own claim]** mini-swe-agent: "Just some 100 lines of python", no tools other than bash, "Scores >74% on the SWE-bench verified benchmark". Its README says: "as LMs have become more capable, a lot of this is not needed at all to build a useful agent!" ([github.com/SWE-agent/mini-swe-agent](https://github.com/SWE-agent/mini-swe-agent), opened 2026-11-01).
- **[fact, C]** HAL (Kapoor et al., ICLR 2026, arXiv 2510.11977):
  - 21,730 rollouts across 9 benchmarks and 9 models;
  - only 2 benchmarks were ever run with the same scaffold for 4 or more models, so comparisons across models are often confounded with the scaffold.

  A secondary analysis of HAL data ("Just a Wrapper?", mitfuturetech.substack.com, D) reports that one scaffold helps some models and hurts others. Unconfirmed.
- **[fact, C]** Larger models are more robust to prompt variation:
  - ProSA (Zhuo et al., EMNLP Findings 2024, arXiv 2410.12405);
  - He et al. 2024 (arXiv 2411.10541): GPT-3.5-turbo varied by up to 40% by template on a code-translation task, and GPT-4 was more robust.

  Two independent sources; both unconfirmed.
- **[estimate]** The model is a large, first-order lever. The share of output that the scaffold and instructions decide appears to shrink as models get stronger. Evidence: mini-swe-agent (B, self-reported), ProSA and He et al. (C), and the Wharton chain-of-thought result below (C).

### 3.2 Instructions: content and design

**Where instructions were the limiting factor**
- **[fact, B]** Anthropic's multi-agent research system: "prompt engineering was our primary lever for improving these behaviors". The failures it fixed included:
  - "spawning 50 subagents for simple queries";
  - delegation instructions "vague enough that subagents misinterpreted the task";
  - subagents that "performed the exact same searches as other agents".

  (multi-agent-research-system, 2025-06-13.) This covers failure kinds K1, K4 and K9.
- **[fact, C]** Yang et al., *What Prompts Don't Say* (arXiv 2505.13360; listed as Findings of ACL 2026):
  - underspecified prompts are "2x more likely to regress over model or prompt changes", sometimes with accuracy drops of more than 20%;
  - **but** simply listing more requirements "does not reliably help";
  - requirements-aware optimisation gave +4.8% on average.

  Unconfirmed.
- **[fact, C]** MAST interventions on ChatDev (ProgramDev), as reported by secondary sources (D): baseline 25.0%, improved role prompt 34.4%, new topology 40.6%. The paper's own text, per the search: "simple fixes are still insufficient". The headline gain is +14% in v1 and +15.6% in v2. Unconfirmed; the figures conflict between versions.
- **[fact, C]** GEPA (Agrawal et al., ICLR 2026 oral, arXiv 2507.19457): reflective prompt evolution beats MIPROv2 by more than 10 points (+12 on AIME-2025). Secondary sources (D) report it beats GRPO by about 6% on average with up to 35× fewer rollouts. One 2026 study, *Do Agent Optimizers Compound?* (arXiv 2607.14004, D, not opened), reports GEPA prompts hard-coding task-specific details and transferring negatively to later tasks. Unconfirmed.
- **[fact, C]** Sensitivity to wording that should not matter (Sclar et al., ICLR 2024, arXiv 2310.11324; version at par.nsf.gov/biblio/10520219):
  - up to 76 accuracy points between near-equivalent formats on LLaMA-2-13B, and about 10 points on average across 50+ tasks;
  - a later version reports a median spread of 6.4 points for GPT-3.5;
  - the sensitivity persists with larger models, more examples and instruction tuning.

  The GitHub repo (B) confirms only the title and authors.

  **[opinion]** This shows wording *can* move results a lot, but arbitrarily. It sets a noise floor that a deliberate instruction change has to beat; it is not evidence that better-written instructions help.

**Where instructions were not the limiting factor, or had small or unreliable effects**
- **[fact, C+B]** Personas: 162 personas across 4 open model families and 2,410 factual questions; adding personas to system prompts "does not improve model performance" against a no-persona control, and the best persona is hard to pick in advance (Zheng et al., EMNLP Findings 2024). The finding is quoted in the repo README I opened ([github.com/Jiaxin-Pei/Prompting-with-Social-Roles](https://github.com/Jiaxin-Pei/Prompting-with-Social-Roles)); the venue comes from search only.
- **[fact, C]** Chain-of-thought instructions: the value is falling, with small gains on reasoning models that are rarely worth the time cost (Meincke, Mollick et al., *Prompting Science Report 2*, SSRN 5285532, June 2025). Report 3 (tipping and threats, arXiv 2508.00614) concludes that simple prompt variations "might not be as effective as previously assumed". I did not see its specific numbers. Unconfirmed.
- **[fact, C]** Instruction load (IFScale; Jaroslawicz et al., arXiv 2507.11538; listed at NeurIPS 2025 venues):
  - 20 models tested, at up to 500 simultaneous instructions;
  - the best models reached 68% accuracy at 500 instructions;
  - earlier instructions were favoured, with the bias peaking at 150–200 instructions.

  Unconfirmed.
- **[fact, B]** Vendor guidance warns against both over-specified, "brittle logic" prompts and "vague, high-level guidance". It advises against "a laundry list of edge cases" and for "diverse, canonical examples" ([effective-context-engineering-for-ai-agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents), 2025-09-29). This is guidance, not a measured result.
- **[fact, C]** Examples: one or more few-shot examples reliably reduce prompt sensitivity (POSIX and ProSA, EMNLP Findings 2024). This is about stability, not quality. Unconfirmed.
- **[estimate]** On length, structure, examples and tone:
  - **length:** helps up to the point of covering the requirements, then has a ceiling (IFScale, Yang et al.);
  - **structure and format:** matters most for weaker models (He et al., ProSA);
  - **examples:** improve stability (ProSA, POSIX);
  - **tone, persona and incentives:** show no reliable effect (Zheng et al., Wharton reports).

  **[estimate]** Specificity about *what* is to be produced and *which requirements* hold is the instruction property with the most support. That rests on Anthropic (B) and Yang et al. (C).

### 3.3 Inputs and context: size and quality

- **[fact, C, several independent sources] Quality falls as input length grows, even when the task is held fixed:**
  - Levy, Jacoby & Goldberg, *Same Task, More Tokens*, ACL 2024: average accuracy fell from about 0.92 to about 0.68 at roughly 3,000 tokens;
  - Du et al., Findings of EMNLP 2025, arXiv 2510.05381: drops of 13.9% to 85% across 5 models even with perfect retrieval, and the drop persists when irrelevant tokens are masked. Reciting the evidence before answering mitigates it;
  - Liu et al., *Lost in the Middle*, TACL 2024, 12:157–173: information placed in the middle of the context is used worst;
  - Hong, Troynikov & Huber, *Context Rot* (Chroma, July 2025): 18 models degrade with input length; the repo README (B) confirms "model performance varies significantly as input length changes, even on simple tasks". The figures on distractor effects come only from secondary sources (D).

  The two-source rule is met on the direction of the effect. Every source is unconfirmed (C).
- **[fact, B]** Anthropic says recall "decreases" as the context grows; context is "a finite resource" with an "attention budget"; subagents should return condensed summaries "often 1,000-2,000 tokens" (effective-context-engineering, 2025-09-29).
- **[fact, C]** Input quality, as distinct from size:
  - *LLMs Get Lost in Multi-Turn Conversation* (Laban et al., arXiv 2505.06120; ICLR 2026): across 15 models and 200,000+ simulated conversations, giving the same information piecemeal over turns rather than all at once dropped performance by about 39% (v1: −35%). Most of the loss was unreliability (about +112%), not aptitude (about −16%);
  - SWE-bench Verified (OpenAI, Aug 2024): 93 developers screened 1,699 samples and kept 500. Underspecified issue statements and unfair tests were the main grounds for exclusion. The exact percentage differs between summaries (D).

  Unconfirmed.
- **[fact, A] Subject.** In Service-Desk, specs/S-001.md is 22,883 lines (line count, 2026-11-01). That is far beyond the input lengths at which the studies above report degradation. **[opinion]** This does not show the length caused any failure here; it is a candidate confound when judging instruction effects.

### 3.4 Task division and topology

- **[fact, B]** Anthropic reports:
  - a multi-agent system beat single-agent Claude Opus 4 "by 90.2%" on an internal research evaluation, using "about 15× more tokens than chats";
  - domains that need shared context or have many dependencies between agents "are not a good fit", and most coding tasks parallelise less well than research;
  - "LLM agents are not yet great at coordinating and delegating to other agents in real time".

  (multi-agent-research-system, 2025-06-13.)
- **[fact, C]** Kim et al. / Google Research, *Towards a Science of Scaling Agent Systems* (arXiv 2512.08296, Dec 2025), across 180 configurations:
  - independent multi-agent setups amplified errors up to 17.2×, while a central orchestrator held it to 4.4×;
  - returns from adding agents turned negative once single-agent accuracy passed about 45%.

  The figure of up to 70% degradation on sequential tasks comes only from secondary sources (D). Unconfirmed. The MIT Media Lab project page (search result) repeats the 17.2× figure.
- **[fact, D]** Cognition (Walden Yan):
  - *Don't Build Multi-Agents* (2025-06-12) argues that subagents handed only a summary lose upstream decisions and produce conflicting work;
  - a 2026-04-22 follow-up says designs where "writes stay single-threaded" work.

  I could not open cognition.ai; this comes from secondary summaries only.
- **[fact, C]** MAST: the topology change (DAG to cyclic) gave more than the prompt change on ChatDev (see 3.2). Unconfirmed.
- **[estimate]** Task division is a co-equal lever with instructions for failure kinds K4 and K9. Splitting helps parallel, read-heavy work and hurts sequential, tightly coupled work. A pipeline of sequential stages, each handing written artefacts to the next, is the second kind, so its handoff artefacts carry the load.

### 3.5 Tools and context design

- **[fact, B]** Anthropic:
  - for the SWE-bench agent, "we actually spent more time optimizing our tools than the overall prompt", and the edit tool was changed to require absolute paths ([building-effective-agents](https://www.anthropic.com/research/building-effective-agents), 2024-12-19);
  - "Even small refinements to tool descriptions can yield dramatic improvements", checked on held-out test sets ([writing-tools-for-agents](https://www.anthropic.com/engineering/writing-tools-for-agents), 2025-09-11);
  - a tool-testing agent that rewrote a tool description gave "a 40% decrease in task completion time" (multi-agent-research-system).
- **[fact, C/D]** SWE-agent (Yang et al., NeurIPS 2024): a designed agent–computer interface beats a raw shell. Secondary sources give +10.7 points or 18.0% vs 11.0% on SWE-bench Lite; the figures conflict. The repo README (B) confirms the venue only.
- **[opinion]** Tool descriptions are themselves instructions. In this pipeline the analogue is the brief templates, the pack manifests and the return forms (A: template-v3/governance/BRIEFS.toml, PACKS.toml).

### 3.6 Checks after the session

- **[fact, C]** Intrinsic self-correction:
  - without external feedback, LLMs struggle to self-correct reasoning, and performance sometimes falls (Huang et al., ICLR 2024, arXiv 2310.01798);
  - self-correction works where reliable external feedback exists, and the bottleneck is generating the feedback (Kamoi et al., TACL 2024, 12:1417–1440).

  Two independent sources agree. Unconfirmed.
- **[fact, C]** Repeated attempts plus selection (Brown et al., *Large Language Monkeys*, arXiv 2407.21787):
  - coverage rises with samples (SWE-bench Lite 15.9% → 56% at 250 samples);
  - majority voting and reward models plateau (MATH: 38.7% → 39.8% from 100 to 10,000 samples);
  - verifiers are the bottleneck.

  Unconfirmed.
- **[fact, C]** Debate and more agents: multi-agent debate "do[es] not reliably outperform" self-consistency or ensembling, though tuning agreement rates helped (Smit et al., ICML 2024, PMLR 235:45883–45905). arXiv 2502.08788 reports the same. Two sources; unconfirmed.
- **[fact, C]** Judge bias:
  - LLM evaluators recognise and favour their own generations, and self-recognition correlates linearly with self-preference (Panickssery, Bowman & Feng, NeurIPS 2024);
  - a panel of judges from different model families beat a single large judge, with less bias between models (Verga et al., Cohere, arXiv 2404.18796).

  Unconfirmed.
- **[fact, C]** Triage-like attribution: the best automated method named the responsible agent 53.5% of the time and the failing step 14.2% of the time (Who&When; Zhang et al., ICML 2025, PMLR 267). The GitHub README (B) confirms the venue and the "184 annotated failure tasks". Unconfirmed.
- **[fact, C]** Gamed checks:
  - METR, *Recent Frontier Models Are Reward Hacking* (2025-06-05): models modified tests or scoring code;
  - in METR's o3 report, about 1–2% of task attempts contained attempted reward hacking.

  Unconfirmed.
- **[fact, B]** Anthropic: the model "often believed it had succeeded when it had not" (swe-bench-sonnet).
- **[fact, C]** Run-to-run consistency: in τ-bench (Yao et al., ICLR 2025), gpt-4o succeeded on under 50% of tasks, and pass^8 was below 25% in the retail domain. Unconfirmed.
- **Gap: number of checkers and rounds. [fact]** I found no study measuring how the number of review rounds or reviewers in a sequential agent pipeline affects final quality. The nearest evidence is repeated sampling (verifier-limited), debate (no reliable gain) and juries (a panel beats a single judge on bias).

  **[fact, A] Subject.** Service-Desk M3B has 14 plan-review rounds on file (reviews/M3B/_plan-review-r1 … r14-verbatim.md, glob 2026-11-01). The stop rule caps plan rounds at three (OPERATING_MODEL.md:203-206). Why M3B ran 14 rounds is not established here.

---

## 4. Failure kind × lever: what has been shown to address each

| Failure kind | Lever(s) with evidence | Evidence and grade | Instructions decisive? |
|---|---|---|---|
| K1 Task misread or underspecified | Instructions (specify requirements and the delegated task); inputs (well-specified tasks) | Anthropic delegation fixes (B); Yang et al. 2× regression (C); SWE-bench Verified screening (C) | **Yes, partly.** Specifying helps; listing everything does not (C) |
| K2 Role or instruction non-compliance | Fewer and more focused instructions; model | IFScale 68% at 500 (C); MAST role-prompt gain smaller than topology gain (C/D) | Limited: more instructions lower compliance |
| K3 Context degradation | Inputs and context design (trim, summarise, recite evidence, placement) | Levy (C); Du (C); Liu (C); Chroma (C/D); Anthropic (B) | **No.** Context lever dominates |
| K4 Handoff loss and misalignment | Task division and topology; detail in handoff descriptions; all information given at once | Anthropic (B); Google scaling (C); Laban et al. (C); Cognition (D) | Shared. Handoff text is an instruction, but topology mattered more in MAST (C/D) |
| K5 False completion, weak verification | External checks with reliable signals (tests); not self-review | Huang (C); Kamoi (C); swe-bench-sonnet (B); Monkeys (C) | **No.** Check lever dominates |
| K6 Tool misuse | Tool design and descriptions | Anthropic ×3 (B); SWE-agent (C/D) | Tool descriptions *are* instructions; vendor-only evidence |
| K7 Run-to-run unreliability and format brittleness | Model (larger is more robust); examples; repeated trials when measuring | Sclar (C); ProSA/POSIX (C); He et al. (C); τ-bench (C) | Wording is a noise source, not a fix |
| K8 Checker failure (bias, gaming, misattribution) | Checker diversity (different model families, panels); hidden tests; human reading | Panickssery (C); Verga (C); METR (C); Who&When (C) | No |
| K9 Runaway effort or cost | Instructions (effort scaling rules); topology | Anthropic 50-subagent fix and 15× tokens (B) | **Yes**, on one vendor's evidence |

**[estimate]** Instructions are a primary lever for 2 of the 9 kinds (K1, K9). They share the lead on 2 more (K4, K6) and are secondary or ineffective for the other 5. This count is mine and unweighted. How often each kind occurs in *this* pipeline is unknown.

---

## 5. The subject pipeline: where each lever sits

These are records of the subject, A-grade, opened 2026-11-01. They are not evidence of what works.

- **[fact, A]** The scripted brief is a fixed one-line route template plus a common header and return form, filled with ids only (template-v3/governance/BRIEFS.toml:1-2, :9-13, :17-36). In that path, task-specific content reaches the session through the pack, the spec or question it names, not through the brief.
- **[fact, A]** Packs set what each role sees: must_read, may_read, must_not_see and include_feedback (template-v3/governance/PACKS.toml:1-9).
- **[fact, A]** Checkers must run on different models from the doers they check (OPERATING_MODEL.md:251-253). Hidden holdouts are kept from the Builder (OPERATING_MODEL.md:247-248, :324-325).
- **[opinion]** On this structure, "instructions" in P-001's sense covers four separate objects:
  - (a) role files;
  - (b) brief templates;
  - (c) the specs and questions that the pack carries;
  - (d) checker finding forms, routed back via include_feedback.

  The literature's strongest instruction effects (K1, K4) concern (c) and (d), the content handed over, more than (a) and (b), the standing wording. The strongest effects outside instructions are context size (K3), the stage topology (K4) and check reliability (K5, K8). The pipeline already partly addresses K8 through model diversity and holdouts.

---

## 6. Gaps and added questions

I add these questions. None is closed.

1. **Q-new-a.** What share of failed rounds in Service-Desk falls into each failure kind K1–K9, judged by a reader blind to the instruction version? This overlaps Q-001's research shortlist item 5. It decides how to weight the levers locally.
2. **Q-new-b.** Does splitting or trimming very long specs (for example, the 22,883-line S-001) change plan-review pass rates, holding instructions fixed? It decides whether context size enters scope.
3. **Q-new-c.** What evidence exists on the number of review rounds or reviewers in sequential agent pipelines, beyond sampling and debate studies? I found none. This may need a level-4 spike, or a level-5 expert with the owner's approval.
4. **Q-new-d.** Do checker finding forms (structure, specificity, file and line evidence) change how quickly a revising session converges? Kamoi et al. put the bottleneck in feedback generation (C). I found no direct test in agent pipelines.
5. **Source access.** Every C-grade item needs a session with arxiv.org, aclanthology.org, openreview.net, proceedings.neurips.cc, proceedings.mlr.press and research.google allowed. Escalation: no paid source is needed.

---

## 7. Proposed library entries

**Facts** ("checked on" is left to the Source checker)

| id | Statement | Sources | Grade | Shelf life | Topics |
|---|---|---|---|---|---|
| F-a | With the scaffold fixed, model choice moved SWE-bench Verified 22% → 33% → 49% | anthropic.com/engineering/swe-bench-sonnet (2025-01-06) | B (one vendor source) | 12 months | agents, quality, model |
| F-b | In one multi-agent research system, token usage explained 80% of BrowseComp variance; tokens, tool calls and model together explained 95% | anthropic.com/engineering/multi-agent-research-system (2025-06-13) | B (one source) | 12 months | agents, task-division, quality |
| F-c | LLM accuracy falls as input length grows with the task held fixed, well below the context limit | Levy et al. ACL 2024; Du et al. Findings EMNLP 2025; Liu et al. TACL 2024; Chroma 2025; Anthropic 2025-09-29 | C (several independent sources, unconfirmed) | 12 months | context, quality |
| F-d | Instruction compliance falls as the number of simultaneous instructions rises (best models about 68% at 500), with earlier instructions favoured | IFScale arXiv 2507.11538 | C (one source) | 6 months | instructions, prompts |
| F-e | Persona or role statements in system prompts do not improve accuracy on objective questions | Zheng et al. Findings EMNLP 2024; github.com/Jiaxin-Pei/Prompting-with-Social-Roles | C/B | 18 months | prompts, instructions |
| F-f | Near-equivalent prompt formats can move accuracy by up to 76 points (about 10 on average); the sensitivity is smaller in larger models and with few-shot examples | Sclar et al. ICLR 2024; ProSA, POSIX EMNLP Findings 2024; He et al. 2024 | C (several sources) | 12 months | prompts, quality |
| F-g | Intrinsic self-correction does not reliably improve reasoning; self-correction works with reliable external feedback | Huang et al. ICLR 2024; Kamoi et al. TACL 2024 | C (two independent sources) | 18 months | quality, checks |
| F-h | LLM judges favour their own generations; panels drawn from several model families reduce this | Panickssery et al. NeurIPS 2024; Verga et al. 2024 | C (two sources) | 18 months | quality, checks |
| F-i | The best automated failure attribution in multi-agent systems found the responsible agent 53.5% of the time and the step 14.2% of the time | Zhang et al. ICML 2025 (PMLR 267); github.com/ag2ai/Agents_Failure_Attribution (venue only) | C | 12 months | agents, checks |
| F-j | Underspecified prompts are about 2× more likely to regress across model or prompt changes; listing more requirements does not reliably help | Yang et al. arXiv 2505.13360 | C (one source) | 12 months | instructions, prompts |
| F-k | Giving task information piecemeal over turns rather than at once cut performance by about 39%, mostly through unreliability | Laban et al. arXiv 2505.06120 / ICLR 2026 | C (one source) | 12 months | context, instructions |
| F-l | Multi-agent debate does not reliably beat self-consistency or ensembling | Smit et al. ICML 2024; arXiv 2502.08788 | C (two sources) | 18 months | checks, task-division |
| F-m | Independent parallel agents amplified errors up to 17.2×, and a central orchestrator up to 4.4×; adding agents gave negative returns above about 45% single-agent accuracy | Kim et al. arXiv 2512.08296 | C (one source) | 12 months | task-division, agents |

**Patterns**

| id | Problem it solves | Principle | Origin | Where it worked | Conditions it depends on | Grade | Shelf life | Topics |
|---|---|---|---|---|---|---|---|---|
| P-a | Subagents misread or duplicate delegated work (K1, K4) | Each delegation states the objective, output format, tools or sources, and task boundaries | Anthropic multi-agent research system | That system, per the vendor (B) | Parallel, read-heavy tasks; a strong lead model | B | 12 months | agents, instructions, task-division |
| P-b | Quality loss from long or noisy context (K3) | Hand each session the smallest sufficient context; return condensed summaries; put key material at the start or end, or have the model recite the evidence first | Context-length studies; Anthropic guidance | Benchmarks (C); vendor practice (B) | Tasks where the relevant material can be isolated | C/B | 12 months | context |
| P-c | Agents misuse tools (K6) | Test tools with the model; rewrite descriptions and interfaces to be error-proof (for example, absolute paths); check against held-out tasks | Anthropic; SWE-agent | SWE-bench agents (B, C) | Tool-heavy work | B | 12 months | agents, tooling |
| P-d | Checks that do not catch errors (K5, K8) | Prefer external, executable or independent checks over self-review; use checkers from other model families; keep tests hidden from the doer | Self-correction, judge-bias and reward-hacking literature | Benchmarks (C) | A reliable external signal must exist | C | 18 months | checks, quality |
| P-e | Mistaking prompt noise for an instruction effect (K7) | Measure a wording change against run-to-run and format variance on the same tasks (paired, repeated) before adopting it | Sclar et al.; τ-bench pass^k | Benchmarks (C) | Budget for repeated runs; pre-registration (the pipeline's no-re-run rule, OPERATING_MODEL.md:299, A) | C | 18 months | prompts, quality |

---

## 8. Sources

**Opened** (web pages are untrusted text and reported as claims):
- https://www.anthropic.com/engineering/multi-agent-research-system (2025-06-13)
- https://www.anthropic.com/research/building-effective-agents (2024-12-19)
- https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents (2025-09-29)
- https://www.anthropic.com/engineering/writing-tools-for-agents (2025-09-11)
- https://www.anthropic.com/engineering/swe-bench-sonnet (2025-01-06)
- https://github.com/multi-agent-systems-failure-taxonomy/MAST
- https://github.com/chroma-core/context-rot
- https://github.com/msclar/formatspread
- https://github.com/microsoft/lost_in_conversation
- https://github.com/ag2ai/Agents_Failure_Attribution
- https://github.com/Jiaxin-Pei/Prompting-with-Social-Roles
- https://github.com/SWE-agent/SWE-agent
- https://github.com/SWE-agent/mini-swe-agent

**Records opened (A):**
- In /home/user/Personal-Org-Operating-Model:
  - OPERATING_MODEL.md (lines 134–333 and 386–432, plus a heading search)
  - template-v3/governance/BRIEFS.toml
  - template-v3/governance/PACKS.toml
  - template-v3/.claude/agents/builder.md
- In /home/user/Service-Desk:
  - specs/S-001.md (line count only)
  - reviews/M3B/ (file list only)
- /home/user/Model-Lab/research/Q-001-memo.md (the groundwork map, for context)

**Seen only in search results, not opened** (the host was blocked or not tried):
- arXiv 2503.13657 (MAST), plus sites.google.com/berkeley.edu/mast
- arXiv 2310.11324 and par.nsf.gov/biblio/10520219 (Sclar)
- arXiv 2507.11538 (IFScale)
- arXiv 2311.10054 and ACL Anthology 2024.findings-emnlp.888 (personas)
- SSRN 5285532 and arXiv 2508.00614 (Wharton reports)
- arXiv 2505.13360 (underspecification)
- arXiv 2507.19457 (GEPA)
- arXiv 2607.14004 (optimizer transfer)
- arXiv 2608.13867
- ACL Anthology 2024.tacl-1.9 (Lost in the Middle)
- ACL Anthology 2024.acl-long.818 (Same Task, More Tokens)
- arXiv 2510.05381 (context length alone)
- research.trychroma.com/context-rot
- arXiv 2505.06120 (multi-turn)
- openai.com/index/introducing-swe-bench-verified
- arXiv 2512.08296 and research.google blog (scaling agent systems)
- cognition.ai/blog/multi-agents-working
- arXiv 2405.15793 and the NeurIPS page (SWE-agent)
- arXiv 2510.11977 (HAL)
- mitfuturetech.substack.com ("Just a Wrapper?")
- arXiv 2310.01798 (self-correction)
- ACL Anthology 2024.tacl-1.78 (Kamoi)
- arXiv 2407.21787 (Monkeys)
- PMLR v235 smit24a (MAD)
- arXiv 2502.08788
- arXiv 2404.18796 (PoLL)
- NeurIPS 2024 proceedings (Panickssery)
- PMLR v267 zhang25cq (Who&When)
- metr.substack.com 2025-06-05 and evaluations.metr.org/openai-o3-report
- arXiv 2406.12045 and proceedings.iclr.cc 2025 (τ-bench)
- arXiv 2410.12405 (ProSA)
- arXiv 2411.10541 (format)

**Hosts that did not resolve in this session:** arxiv.org, neurips.cc, openreview.net, aclanthology.org, mlanthology.org, huggingface.co, alphaxiv.org, api.semanticscholar.org, research.google, research.trychroma.com, cognition.ai.
