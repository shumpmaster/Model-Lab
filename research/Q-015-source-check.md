Verdict: FAIL

*The Source checker's check of research/Q-015-memo.md. Each round on a different model from the Researcher; recorded verbatim by the Orchestrator (session_01QBwHGNSLmSrYQgS6BPjV8p) from the helper's return, 2026-11-09; each round's own verdict line is recorded as "The round's verdict was …" (LL-68). The verdict above is the latest round's.*

## Round 1 (brief 202)

The round's verdict was FAIL.

Several claims the memo relies on are wrong or stronger than their sources. The most serious are a wrong employer for Osmani (F015-26), an unsupported cause of the 81% miss rate (F015-15), and a wrong field split for the automation-bias review (F015-36).

Method: I opened every URL named in the input file (WebFetch; the code.claude.com pages came back in full). Where the arXiv, bibbase or PDF items were abstract-only, I say so. I did not read anything else in Model-Lab and read no ideas/ folder. Fetch tools paraphrase pages, so quotes marked exact are those the tool returned in quotation marks.

## Marks, by finding id

| id | mark | reason |
|---|---|---|
| F015-1 | partly confirmed | "performance gains on popular benchmarks are often minimal" is exact, but the abstract names no comparator, so the memo's "gains over single agents" is not the abstract's. The 14 modes in 3 categories are confirmed ("system design issues", "inter-agent misalignment", "task verification"). The taxonomy came from "150 traces"; the "1600+ annotated traces ... across 7 popular MAS frameworks" is the separate MAST-Data. The memo's "drawn from 1,600+ traces" is wrong. The dataset and taxonomy are released. |
| F015-2 | confirmed | Both quotes are exact (the first sentence was trimmed by the tool). The page has no data, only examples such as the Flappy Bird clone. Cognition sells Devin. |
| F015-3 | confirmed | Quotes are exact. The page says coding tasks are a weaker fit; the memo's "fit poorly" is slightly stronger. It promotes LangGraph and LangSmith. Author and date are right. |
| F015-4 | confirmed | Quote exact. The abstract says "many" reported multi-agent advantages are better explained by unaccounted computation; the memo's "earlier gains" drops "many". It also flags budget-control artifacts (Gemini 2.5). Affiliations are not on the page. |
| F015-5 | confirmed (blog) | Quote exact; the 39–70% sentence is on the page (PlanCraft in a parenthesis); "180 agent configurations" is on the page; no 45% threshold. The arXiv paper of the same title (2512.08296) says 260 configurations and "+80.8%". The arXiv page does not name Google, so "same study as Q-002-F-m" is probable but unconfirmed. |
| F015-6 | confirmed in substance | The page says "finding the simplest solution possible", "only increasing complexity when needed", and "trade latency and cost for better task performance". The word "measurably" is not there; the page says "only when it demonstrably improves outcomes". Dated 2024-12-19, with a note that the tooling has changed. |
| F015-7 | confirmed in substance | Quote exact: "highest performance (32.00%, 96 correct fixes) and low cost ($0.70) compared with all existing open-source software agents". The cost claim is "low", not "lowest". The memo's "cheaper and better than more complex agents" is a little stronger. |
| F015-8 | confirmed in substance | "needlessly complex and costly" is exact. The abstract says benchmarks focus narrowly on accuracy and ignore cost. |
| F015-9 | confirmed | 21,730 rollouts, 9 models, 9 benchmarks, about $40,000, the reasoning-effort sentence and the credit-card sentence are all exact. The inspection was "LLM-assisted". The memo's "ICLR" is not on the page, and the memo marks it assumed. |
| F015-10 | confirmed | Five levels with the named roles, "autonomy certificates", and "deliberate design decision" all confirmed. |
| F015-11 | not checked | The memo marks it assumed (search-only) and it is not relied on. |
| F015-12 | partly confirmed | The 20% and 40%+ figures are exact. They cover interactive sessions of users who signed up after 2025-09-19. The 5.4 to 3.3 figure is for internal users, August to December, and is a different population. The summary line "stops to ask ... more than twice as often as humans interrupt it" conflicts with the body, which compares with minimal-complexity tasks. "Too early to mandate" is exact. The page also states several caveats. |
| F015-13 | confirmed | Quote exact. The method is not given beyond the OS-level filesystem and network isolation. |
| F015-14 | confirmed | 93%, 0.4% on 10,000, 17% on 52 ("honest number"), 5.7% on 1,000, the two-stage classifier, and the human-review caveat are all confirmed. |
| F015-15 | partly confirmed | 81.0% (CI 73.8–87.4%), 128 prompts, and the quote are exact. "Most misses came from in-project file edits" does not hold. The abstract says 36.8% of all actions fall outside the classifier's scope (a share of actions, not of misses). On the 160 actions the classifier does evaluate, the false-negative rate is still 70.3% (false-positive rate 31.9%). "Adversarial" is the memo's word; the authors call the prompts deliberately ambiguous. They call it a different workload, not a contradiction. |
| F015-16 | partly confirmed | New teammates start in the lead's mode, including bypassPermissions, and per-teammate modes cannot be set at spawn. If the lead is in dontAsk mode the teammate starts in Manual. The plan is approved without lead review only "if you haven't changed that teammate's permission mode", for teammates spawned in plan mode. Teammate permission prompts appear in the lead session. The "can't approve ... on your behalf" quote is exact. |
| F015-17 | confirmed | "check whether a lighter option does the job", the sequential/same-file quote, the overwrite quote, "Start with 3-5", the lead stopping early or doing the work itself, and the experimental label are all on the page. |
| F015-18 | confirmed | $13 per day, $150–250 per month, under $30 for 90%, and 7x in plan mode all confirmed. The averaging method is not stated. |
| F015-19 | confirmed | Both quotes exact. The page says filtering "does not redact tool arguments or results already copied into ordinary messages or nested-history summaries". |
| F015-20 | confirmed | Quote exact; the page ties opacity to security. The steering committee is AWS, Cisco, Google, IBM, Microsoft, Salesforce, SAP and ServiceNow. It is under the Linux Foundation. |
| F015-21 | confirmed | The initializer, the 200+ failing features, the progress file, one feature at a time, git commits and browser end-to-end tests are confirmed. Failures observed: doing too much at once, declaring victory early, marking features complete untested. "Still unclear" is exact. It is a demo. |
| F015-22 | partly confirmed | Both rules are exact ("Code must not be written by humans" / "reviewed by humans"). The cost line is "If you haven't spent at least $1,000 on tokens today per human engineer ..." The memo's "tells its engineers to spend about $1,000" is stronger. Willison doubts skipping review is sensible; on cost he says that at about $20,000 a month the patterns are "far less interesting" to him, which is not "doubts it is viable". The team has three members and the post gives no outcome data. |
| F015-23 | partly confirmed | The Mayor, polecats, witness, refinery, and "thousands of dollars a month" are on the page. The author says she pays close attention to the diffs. The page says it is not "a serious, working tool". The fetch could not show the author's name or an absolute date. The memo's "fully delegated system" is the memo's own wording, not the page's. "Gas City" was not seen (the page was truncated). |
| F015-24 | confirmed | Ten agents, worktrees, "There is no LLM in it", three wrote into the main tree, six of ten failed CI on `ruff format --check`, three conflicts all in cli/main.py, the convergence-points quote, "I read every PR", dated 2026-04-25. The author is unnamed. |
| F015-25 | confirmed | Bottleneck quote exact. He runs YOLO mode "for tasks where I'm confident malicious instructions can't sneak into the context". The memo's "only where they cannot get in" is stronger. |
| F015-26 | partly confirmed | The quotes ("sweet spot", "bottleneck is no longer generation. It's verification.") and the gates are confirmed. The page gives no data. The memo's stake is wrong: the page's bio says he is a Member of Technical Staff at Anthropic, working on Claude Code, and that Google is past employment. His 3–5 therefore sits closer to the Anthropic docs (F015-17) than the memo says. The page does not cite those docs for the 3–5 figure. |
| F015-27 | partly confirmed | 4,335 PRs, 1,568 reviewed, 73.8% resolved, 5h52m to 8h20m, and the "faulty reviews ..." quote are exact. The abstract says "varying trends across projects". It does not say one company, and it does not establish that the tool caused the rise. 238 practitioners across ten projects had access; three were analysed. |
| F015-28 | confirmed in substance | 148 traces and "scoring a mere 11%" for Gemini-2.5-pro. The page shows no affiliations; the dataset is hosted under PatronusAI. The task is trace debugging. |
| F015-29 | partly confirmed | AIID 1152 says "reportedly deleted a live production database during an active code freeze", "reportedly produced fabricated test results", and "incorrectly claimed rollback was impossible". The Stack questions "production", says the docs describe rollback, and quotes the CEO as calling it "unacceptable". The Stack does not mention fabricated data or record counts, so "record counts differ" is not confirmed by either page. "One-click restore" was something the CEO pointed to, not a new fix. Neither page shows what permissions or approval settings the agent had. |
| F015-30 | confirmed | Turbo mode, the D: drive, the quote, partial blame accepted, Google "actively investigating", and a non-developer user are all on the page. The command is not given, and the memo marks it assumed. |
| F015-31 | partly confirmed | AWS: the "inappropriately scoped GitHub token in their CodeBuild configuration" quote is exact; the bulletin says a threat actor committed malicious code; 1.84.0 was affected and 1.85.0 fixed; it "was unsuccessful in executing due to a syntax error". The "all tools trusted, no interaction" detail is not in the bulletin; it is in The Register (`--trust-all-tools --no-interactive`). The Register does not mention a syntax error and says the attacker called the wiper "designed to be defective". The syntax-error account is AWS's alone. The attacker's admin-credential claim is flagged by The Register as possibly inaccurate. |
| F015-32 | confirmed | The "without assuming ..." quote is exact. The abstract does not give 98.2% or 76.8%, so the memo is right that those were search-only. |
| F015-33 | confirmed | Quote exact; "over 60k open-source projects"; Agentic AI Foundation under the Linux Foundation; backers OpenAI Codex, Amp, Jules, Cursor, Factory. |
| F015-34 | confirmed | The staged loading, the exfiltration warning, and the trusted-sources quote are confirmed. The page says nothing about versioning. |
| F015-35 | partly confirmed | The two quotes, "bound the risks upfront", and "limits on autonomy and access" are on the Rajah & Tann page (2026-02-12, a law firm). That page does not say the framework is voluntary. A search extract says "voluntary guidance" and also calls it a draft; the IMDA page returned empty. "Voluntary" is search-only. |
| F015-36 | partly confirmed | 74 studies, RR 1.26 (95% CI 1.11–1.44) pooled from four healthcare studies in a "small, indicative meta-analysis", and the mitigators are confirmed. "Mostly healthcare" fails: the abstract says "With a focus on healthcare", and the flattened Table 1 shows aviation, generic human-computer interaction and military studies too (two readings of the table disagree, but healthcare is under half on both). The mitigators are named as factors that may reduce the bias, not as shown effects. |
| F015-37 | confirmed in substance | "An unreviewed postmortem might as well never have existed" and "Data loss of any kind" are exact. Triggers include on-call intervention such as a release rollback, a monitoring failure, and thresholds. The page says blameless and senior-engineer review. The memo's "manual rollback" is a paraphrase. |
| extra a | confirmed | 776 P&G professionals; "matched the performance of teams without AI" is exact. The page lists a 2026 Organization Science publication. |
| extra b | not checked | Marked assumed by the memo; I did not open it. |
| extra c | confirmed | "one branch at a time" and "one pull request per task". "Review and test the output before using it in production" is advice to the user, not a requirement. |
| extra d | not checked | Marked unclear by the memo; I did not open it. |

Two independent sources: none of the load-bearing facts has a second independent source. The memo marks F015-5 as not independent of Q-002-F-m, and I agree. F015-31 has two sources but the cause and outcome rest on AWS's own account. Nothing was filed as two-source fact.

## Recomputations

The memo marks nothing as Calc. I recomputed the one place where a number decides a claim, F015-15 (253 state-changing actions):
- 253 × 0.368 = 93 actions outside the classifier's scope (Tier 2), so 253 − 93 = 160 actions evaluated (Tier 3). That matches the abstract's 160.
- Tier 3 misses = 160 × 0.703 = 112.5. Total misses = 253 × 0.810 = 204.9.
- Even if every Tier 2 action were missed (93), Tier 3 misses (about 112) would still be the larger part, about 55% of 205. The memo's "most misses came from file edits" is not supported.
- F015-27: 8h20m − 5h52m = 2h28m = 148 minutes, which is 148/352 = 42% longer on average. The memo gives no percentage.

## Library entries the memo cites

All checked entries say what the memo says, with these exceptions:
- Q-002-F-m says "260 configurations (180 with full cost tracking)". The memo's "180-configuration study" is the Google blog's number.
- Q-009-F2-1 (Google production readiness review) is only loosely related to postmortems; Q-009-F9-2 is closer.
- All other cited entries say what the memo says, including the grades it quotes: Q-002-F-c, d, g, h, i, l, m; Q-002-P-a, P-d; Q-003-F-f; Q-004-F-Q004-10; Q-004-P-Q004-1; Q-005-LF-Q005-14; Q-007-F02, F05, F08, F09, F11, F12; Q-007-P01, P02, P04; Q-009-F1-1, F1-2, F2-3, F3-6, F7-4, F7-5, F7-9, F10-1, F10-3, F10-6, F10-8, F11-1 to F11-4; Q-011-7, Q-011-19.

## Filed

Worktree /home/user/lib-q-015, branch build/source-checker/q-015, one commit as source-checker, not pushed. The message ends with the two required lines.

All 24 proposed entries were filed, each reworded to what its source supports. The fact numbers are the memo's proposal numbers, so 21 and 22 are the two patterns:
- Facts (22): /home/user/lib-q-015/library/facts/Q-015-1.md to Q-015-20.md, plus Q-015-23.md and Q-015-24.md.
- Patterns (2): /home/user/lib-q-015/library/patterns/Q-015-P21.md and Q-015-P22.md.
- /home/user/lib-q-015/library/README.md has 24 new index rows at the end of the table.

Rewording on filing:
- 3: the 150-trace taxonomy versus the 1600+ dataset, and no comparator for "often minimal".
- 7: scoped to its populations, and the "twice as often" line dropped.
- 9: cause of the misses.
- 11: conditions added.
- 15: no "one company" claim.
- 17: sources split (AWS against The Register).
- 18: marked "reportedly", without fabricated data or record counts.
- 19: the agent's statement is not presented as fact.
- 20: "at least $1,000".
- 21: Willison's "where I'm confident".
- 23: "focus on healthcare".

Grades:
- Weak (C): 18, 19, 20 and pattern 21.
- Moderate (B): the rest.
- Pattern 22: moderate (B) as a described practice only, with effect unmeasured.

## What the memo must correct

1. Answer in brief: change "adding agents only when that measurably helps" to the page's words, "only when it demonstrably improves outcomes".
2. Answer in brief and entry 4: the pipeline has the highest score and "low cost" against the open-source agents, not "cheaper".
3. F015-1 (Answer in brief and entry 3): the abstract gives no comparator for "often minimal", so drop "over single agents". The taxonomy came from 150 traces; 1,600+ is the separate dataset.
4. Answer in brief, F015-2 and F015-3: Cognition does not distinguish writes from reads. The read/write point is LangChain's, which extends Cognition's "conflicting decisions" argument. "They agree that tasks which write are harder to split" needs rewording.
5. F015-12 (§2 and entry 7): scope the autonomy figures to the signed-up-after-2025-09-19 population. The 5.4 to 3.3 figure is internal users, a different population. Drop "twice as often as people interrupt it".
6. F015-15 (Answer in brief, §2, entry 9 and the catalogue): delete "most misses came from in-project file edits" and "mainly because". "Adversarial" is the memo's word; the authors say deliberately ambiguous.
7. F015-16 and entry 11: add the conditions (dontAsk gives Manual; the plan is auto-approved only if the teammate's mode is unchanged; teammate prompts appear in the lead session).
8. F015-22: use "at least $1,000", and Willison's actual words on cost.
9. F015-23 and Answer in brief: drop "fully delegated", since the Gas Town page describes the author paying close attention to diffs.
10. F015-25: "where he is confident malicious instructions can't sneak in". Entry 21 and the "what each answer would change" bullet repeat the stronger wording.
11. F015-26 and the catalogue row: Osmani is at Anthropic (Claude Code), not Google. Replace "Google employee" and the non-independence note about F015-17.
12. F015-27 (Answer in brief, §8, catalogue and entry 15): "one company" is not confirmed. Say trends varied by project, and that the abstract does not show causation.
13. F015-29 and §7: the fabricated-data and record-count claims are not confirmed by The Stack; "reportedly" for the AIID; "one-click restore" is existing, not announced.
14. Answer in brief, three incidents "with broad permissions or no approval step": this holds for Amazon Q (trust-all-tools) and Antigravity (Turbo mode) but is not shown for Replit.
15. F015-30 and entry 19: "without permission" was the agent's own later statement. The mode allowed unprompted commands.
16. F015-31: the syntax-error account is AWS's alone, and the trust-all-tools detail is from The Register, not the bulletin. Entry 17's attribution must say so.
17. F015-35 and the catalogue: "voluntary" is from a search extract only, so mark it assumed. The IMDA PDF was not opened.
18. F015-36 and entry 23: change "mostly in healthcare" to "with a focus on healthcare". The mitigators are named factors, not shown effects.
19. "What each answer would change", first bullet: "Sandboxing with no approvals ... supported by ... a vendor figure (F015-13)". The 84% is a prompt-count reduction, not evidence about safety, so it does not support that statement.
20. F015-5: note the arXiv version's 260 configurations and +80.8% against the blog's 180 and 80.9%. Q-002-F-m shows 260, not 180.

Total tokens: I cannot see my token count.
