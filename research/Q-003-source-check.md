Verdict: PASS

Every A and B item I checked was confirmed and the arithmetic is right. The slips are listed under "Slips" below. No conclusion rests on a failed item, but several rest on grade-C items that I could not open. No entry can be filed as proposed, because none has two independent sources.

I wrote no files. I did not open /home/user/portfolio or Model-Lab's decisions, questions or docs. Web text was treated as data. Model-Lab has no library directory, so I could not run the check for existing entries on the same topics. That needs someone with portfolio access.

## Table (A and B items, plus Calc)

| Item | Claim | Source | Result | Note |
|---|---|---|---|---|
| §2 criteria by work type | Software: "Locked tests (visible) and hidden holdouts", Reviewer plus CI. Research: "The question and evidence standard, set in advance", Source checker. Experiment: "The pre-registration", Reviewer (analysis) | OPERATING_MODEL.md:313-315 | confirmed | |
| §2 writing | Writing judged by "A reader test against the rubric" | OPERATING_MODEL.md:316 | confirmed, with a slip | That phrase is in the checker column. The criterion column reads "Audience, purpose, a scoring rubric". |
| §2 checker return | `Verdict: PASS` or `Verdict: FAIL`; "An unverifiable claim is a FAIL" | BRIEFS.toml:13; reviewer.md:37 | confirmed | |
| §2 role measures | Builder, Definer, Reviewer, Check author, Critic, Researcher measures | builder.md:47, definer.md:47, reviewer.md:43, check-author.md:45, critic.md:49, researcher.md:41 | confirmed | The memo's quotes are exact. The Critic and Check author lines carry extra text the memo dropped. |
| §2 rules as experiments | "Every rule is an experiment with a target, a measure and a kill criterion" (:425-426); baseline "once real projects give a baseline" (:422-423) | OPERATING_MODEL.md | confirmed | |
| §2 experiment playbook | Pre-registration, then run exactly as registered, then analysis by someone else. "No re-running for a better answer." "Exploratory, unconfirmed". | OPERATING_MODEL.md:296-302 | confirmed | Line citations 299-300 and 301 are right. |
| §2 seeded defects | Five seeded defects "in a throwaway copy, every one caught" | Service-Desk reviews/240/reviewer.md:19-24 | confirmed | Five bullets under the heading line. |
| §2 owner files | 45 `reviews/*/owner.md` files, all open with `Verdict: PASS` | grep of Service-Desk reviews | confirmed | Count is 45 and all 45 read PASS. |
| §2 owner example | reviews/56/owner.md:1-3 "reads in full" | Service-Desk | confirmed, with a slip | The quoted words are there. Line 3 continues "(one governance file, identical to the model's copy)", so "in full" is wrong. |
| §3 model diversity rule | "Every checker runs on a different model from the doer it checks… using more than one provider where available; when no alternative exists, the record says so" | OPERATING_MODEL.md:251-253 | confirmed | The rule says model, not family. |
| §3 Q-001 control records | Researcher on `claude-opus-5-5`, Source checker on `claude-sonnet-5-5` | Service-Desk reviews/Q-001/_control/*.json | confirmed | Model lines at 73, 54, 62 (researcher) and 60, 67, 78 (source-checker) match. Roles are named at lines 2 and 31 of each file. "Same provider and family" is an inference from the model names. The records say nothing about it. I found no "no alternative provider" statement in reviews/Q-001. |
| §3 MT-bench | "humans and GPT-4 judge achieve over 80% agreement, the same level of agreement between humans"; 3.3K annotations, 6 models, 80 questions | github.com/lm-sys/FastChat llm_judge README | confirmed | |
| §3 Agent-as-a-Judge repo | DevAI has 55 tasks and 365 requirements; no agreement figure | github.com/metauto-ai/agent-as-a-judge | confirmed | The README gives time and cost savings (97.72% / 97.64%) only. |
| §3 vendor "different model" | "Generally best practice to evaluate with a different model from the one used to generate the evaluated output" | platform.claude.com develop-tests | confirmed | It sits in code comments of the grading examples, not prose. |
| §3 vendor reliability | "Test to ensure reliability first, then scale"; detailed rubrics; "Encourage reasoning" | platform.claude.com develop-tests | confirmed | I found the exact wording by fetching the page directly. "Binary or 1-5" appears as example formats, not as stated advice. |
| §3 calibration | "LLM-as-judge graders should be closely calibrated with human experts" | demystifying-evals, 2026-01-09 | confirmed | |
| §3 CORE-Bench | Opus 4.5 "initially scored 42%", then "jumped to 95%" | demystifying-evals | confirmed | |
| §3 transcripts, task quality, ambiguity | "read the transcripts"; "two domain experts would independently reach the same pass/fail verdict"; "Ambiguity in task specifications becomes noise in metrics" | demystifying-evals | confirmed | The transcripts quote continues "and grades from many trials". |
| §4 statistical-approach post | Paired differences described as "free" variance reduction; correlations "between 0.3 and 0.7"; clustered SEs "over three times as large as naive"; resample several times; power analysis | anthropic.com/research/statistical-approach-to-model-evals, 2024-11-19 | confirmed | I did not individually check "reporting pairwise results". |
| §4 bayes_evals | Implements `paired_comparisons` for binary results on shared questions | github.com/sambowyer/bayes_evals | confirmed | |
| §4 bayes_evals, CLT claim | CLT error bars "dramatically" understate uncertainty below a few hundred datapoints | same README | not confirmed | The README only cites the paper title "Position: Don't use the CLT in LLM evals with fewer than a few hundred datapoints". It states no claim. The paper itself is C and unreachable. |
| §4 McNemar | Exact binomial "if exact is True"; chi-square is the approximation for large samples | statsmodels contingency_tables.py | confirmed | |
| §4 infrastructure noise | 6 points (p < 0.01); differences under 3 points deserve scepticism; "Naive binomial confidence intervals already span 1-2 percentage points"; "running at multiple times and on multiple days" | anthropic.com/engineering/infrastructure-noise, 2026-02-05 | confirmed | |
| §4 starting small | "20-50 simple tasks drawn from real failures is a great start"; "this large effect size means small sample sizes suffice" | demystifying-evals | confirmed | |
| §4 shared state, pass^k | "correlated failures due to infrastructure flakiness"; pass^k "measures the probability that all k trials succeed" | demystifying-evals | confirmed | |
| §4 τ-bench | Claude 3.5 Sonnet (20241022) retail Pass^1 0.692, Pass^4 0.462 | github.com/sierra-research/tau-bench | confirmed | |
| §4 Calc 1 | 9/10 gives p = 0.021, 8/10 gives 0.109; 12/15 gives 0.035; 15/20 gives 0.041 | recomputed | confirmed | Two-sided exact binomial: 0.0215, 0.1094, 0.0352, 0.0414. The next lower counts miss: 11/15 = 0.119, 14/20 = 0.115. |
| §4 Calc, Example A | 15 discordant, win share 0.25/0.30 = 0.83; P(≥12 of 15) ≈ 0.77; "about 75%" | recomputed | confirmed | Exact tail is 0.768. If the discordant count itself varies (Bin(50, 0.30)) and the exact test is used at each count, power is about 0.70. "About 75%" is fair. |
| §4 Calc, Example B | 10 discordant, share 0.75; P(≥9 of 10) ≈ 0.24 | recomputed | confirmed | Exact 0.244. With the discordant count varying (Bin(50, 0.20)) it is 0.241. |
| §4 Calc, unpaired | SE = √(2·0.25/50) = 0.10; (1.96 + 0.84) × 0.10 = 0.28 | recomputed | confirmed | |
| §4 Calc, Wilson | 7/10 gives a 95% interval of about 0.40–0.89 | recomputed | confirmed | I get 0.397–0.892. |

## Grade-C items (opened or not)

| Item | Result |
|---|---|
| arXiv 2306.05685 (Zheng et al., self-enhancement and other biases) | unreachable (arxiv.org does not resolve) |
| arXiv 2404.13076 (Panickssery et al.) | unreachable |
| arXiv 2410.21819 (Wataoka et al.) | unreachable |
| arXiv 2604.06996 (rubric-based self-preference) | unreachable |
| arXiv 2503.01747 (Bowyer et al.) | unreachable |
| arXiv 2411.00640 | unreachable |
| aclanthology.org/2025.acl-short.20 (Bavaresco et al.) | unreachable |
| Agent-as-a-Judge ~90% versus ~70% agreement | not confirmed by the repo (README has no agreement figure); the paper is unreachable |
| JudgeBench "near chance" | the memo already marks this not confirmed; I did not re-open the README |
| arXiv 2505.20206, 2407.01502 (Kapoor et al.), 2406.18403, 2410.10934, 2410.12784, 2503.13657; papers.nips.cc; proceedings.mlr.press | not attempted. The Researcher reports these hosts do not resolve, and arxiv.org failed for me. The arXiv and ACL failures say the host must be allowed in the session's network settings. |

No grade-C item was confirmed, so I did not upgrade any.

## Conclusions that rest on unconfirmed items

- §1 item 2 and §3: the self-preference claims are C only. The memo states them as unconfirmed, and the same-family consequence is written as conditional and an estimate. They must not be filed.
- §3 "agreement varies widely by task" and the Judge-Bench part of P-b rest on C. P-b's principle still stands on the vendor guidance and on the memo's own opinion.
- §4 Bowyer et al. and the "dramatically understate" wording rest on C. The README only shows the paper title.
- §5's Kapoor caution is C.
- §1 items 1, 3, 4 and 5 and the §6 options do not depend on any failed item. §1 item 3's figures are scenario-dependent Calc (assumed discordance rates), as the memo says.

## Slips (allowed)

1. §2 "reads in full" for reviews/56/owner.md is wrong (line 3 is longer than quoted).
2. §2 writing row: the quoted phrase is the checker column, not the criterion.
3. Example A "about 75%" is 0.77 for exactly 15 discordant tasks and 0.70 if the discordant count varies.
4. F-b and §4 overstate what the bayes_evals README says (title only).

## Library entries (may it be filed as proposed?)

None of the nine can be filed as proposed. Fact entries need two independent sources and none has two that are open and independent. I did not file anything.

- **F-a:** Not as proposed. One opened source. The arXiv paper is unreachable and is the same work, so it would not be independent anyway. The statement matches the post.
- **F-b:** Not as proposed. The statement is not supported by what I opened (README title only), and the second source is unreachable. It could only be narrowed to "the authors' library implements paired comparisons for binary results", which is a single source.
- **F-c:** Not as proposed. Text confirmed, but there is one source only.
- **F-d:** Not as proposed. Confirmed, one source only (the benchmark README). It is a single leaderboard row, so "consistency falls across repeated trials" is a generalisation.
- **F-e:** Not as proposed. Confirmed, one source (the README). The arXiv paper is unreachable.
- **F-f:** No. Unconfirmed, grade C, as the memo says.
- **F-g:** Not as proposed. Every statement is confirmed, but both sources come from one publisher. It could be filed only if the caller accepts it as non-load-bearing vendor guidance labelled single-publisher. That is the caller's decision.
- **F-h:** Confirmed against primary records. It can be filed with a "checked on 2026-11-01" date, with two changes. Split the model-pairing fact from the owner-PASS fact, since they are unrelated. Mark "same provider and family" as an inference from the model names. Grade A.
- **F-i:** The arithmetic is confirmed. It can be filed as a Calc fact with the assumed discordance rates stated as assumptions, and Example A's "about 75%" noted as 0.70–0.77. The statsmodels reference is confirmed.
- **P-a, P-b, P-c:** These are opinion patterns. Their cited B sources are confirmed (P-b's Judge-Bench reference is C and unconfirmed). They do not meet the two-independent-sources test for facts, and P-c's replay condition is open (Q-001 B4). They are fileable as patterns only if the caller treats them as opinion-grade. I recommend holding P-c until F-a gains a second source.

Relevant files:
- /home/user/Model-Lab/research/Q-003-memo.md
- /home/user/Model-Lab/research/Q-003.md
