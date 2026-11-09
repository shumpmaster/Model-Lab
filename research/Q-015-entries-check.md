Verdict: PASS

*The Source checker's deciding check of the Q-015 library entries, as the owner ruled (decisions/questions/P-002-research-stop-3.md): one check of every filed entry against its source, the memo set aside. A fresh session on a different model from the Researcher, brief 214 (docs/briefs/214-source-checker.md). Recorded verbatim by the Orchestrator (session_01QBwHGNSLmSrYQgS6BPjV8p) from the helper's return, 2026-11-09.*

Every Q-015 entry (22 facts, 2 patterns) was checked against its source and now says no more than that source. Nothing was removed. All 24 entries were opened in this check, so the earlier record was used for none of them. arXiv abstracts came from the live abstract pages. Vendor, press and docs pages were fetched as full page text and read directly. I could not see my own token total.

| id | source opened | result | reason |
|---|---|---|---|
| Q-015-1 | arxiv.org/abs/2604.02460 | reworded | The sentence is exact. Added the abstract's own qualifiers: the information-theoretic argument, MAS becoming competitive when context use degrades or more compute is spent, the "matched budgets" design, and "many" rather than all. Dropped the Contextual AI aside. |
| Q-015-2 | research.google blog; arxiv.org/abs/2512.08296 | reworded | The blog calls it "our new paper" and links arXiv 2512.08296, so "probable, not confirmed" was wrong; it is the same study. The 80.9/80.8 and 180/260 differences stay noted, and the entry is still not independent of Q-002-F-m. The "45% threshold" is not on the blog. |
| Q-015-3 | arxiv.org/abs/2503.13657 | reworded | Quotes hold. "UC Berkeley" removed because the page shows no affiliations. |
| Q-015-4 | arxiv.org/abs/2407.01489 | reworded | Quote holds. "(UIUC)" removed because it is not on the page. |
| Q-015-5 | arxiv.org/abs/2407.01502 | reworded | Now follows the abstract's words. "Princeton" and "position paper" removed because neither is on the page. |
| Q-015-6 | arxiv.org/abs/2510.11977 | reworded | Figures hold. Removed the memo reference. "Run the leaderboard" became "introduce/built" to match the abstract. No venue is shown. |
| Q-015-7 | anthropic.com/research/measuring-agent-autonomy | reworded | Figures and caveats hold. "Argues against mandates" overstated "too early to mandate", so it was removed. The Limitations section is now cited for the caveats. |
| Q-015-8 | anthropic.com/engineering/claude-code-auto-mode | reworded | Figures hold. Added that the 10,000 calls are from Anthropic employees and that the 52 actions were curated from denied or post-hoc-flagged sessions. The quote is now "not a drop-in replacement for careful human review on high-stakes infrastructure". |
| Q-015-9 | arxiv.org/abs/2604.04978 | reworded | Figures hold. The claim that the misses are "not mainly file edits" went beyond the abstract, which says Tier 2 contributes and Tier 3 FNR is still 70.3%. Reworded, and the memo-style note removed. |
| Q-015-10 | anthropic.com/engineering/claude-code-sandboxing | holds | The 84% quote, approval-fatigue wording and isolation description match. |
| Q-015-11 | code.claude.com/docs/en/agent-teams | reworded | Quotes hold. The title said plans are approved "by default"; it now states the condition (lead in plan mode, teammate mode unchanged). The memo-style note was removed. |
| Q-015-12 | code.claude.com/docs/en/agent-teams | holds | All four quotes and the "lead can stop early" caveat match. |
| Q-015-13 | code.claude.com/docs/en/costs | holds | $13, $150-250, $30 for 90% of users, and 7x in plan mode all match. |
| Q-015-14 | openai.github.io/openai-agents-python/handoffs/ | reworded | The "does not redact" sentence is about the built-in remove_all_tools filter, not input filters in general. Title and statement fixed, and the page's pointer to custom input filters added. |
| Q-015-15 | arxiv.org/abs/2412.18531 | reworded | Figures and the ICSE SEIP comment hold. The abstract does say the tool "led to longer pull request closure times", so the "does not establish cause" claim was replaced with what the abstract says. The Q-016 and memo notes were removed. |
| Q-015-16 | arxiv.org/abs/2505.08638 | reworded | Quote holds. The Input-reader/Patronus note was replaced by what the page shows (a dataset link under PatronusAI; affiliation unconfirmed). |
| Q-015-17 | AWS bulletin AWS-2025-015; theregister.com 2025/07/24 | reworded | AWS and Register details hold. Removed "so the agent ran without confirmation", an inference the article does not make. Added the prompt's content, taken from the Register. The "admin credentials" claim is now stated as the article words it. |
| Q-015-18 | incidentdatabase.ai/cite/1152; thestack.technology | holds | The AIID quotes, the Stack's rollback, "production", CEO and dev/prod separation points all match, and no fabricated data appears in the Stack. |
| Q-015-19 | theregister.com 2025/12/01 | holds | Turbo mode, the D: drive, the Recycle Bin, the agent's reply, "actively investigating" and the user's background all match. |
| Q-015-20 | simonwillison.net/2026/Feb/7/software-factory/ | reworded | Quotes hold. Removed the unverified "redirects to delinea.com" and the memo-style note. |
| Q-015-23 | PMC3240751 (JAMIA full text) | reworded | 74 of 13,821 papers, RR 1.26 (1.11-1.44), the mediators and the mitigators all match. Dropped the speculative "under half" estimate. Dropped the OUP URL, which returned 403, because PMC carries the same abstract and text. |
| Q-015-24 | arxiv.org/abs/2503.03704 | reworded | Quotes hold. Removed the memo reference and the unopened "later critique" mention. |
| Q-015-P21 | simonwillison.net/2025/Oct/5/parallel-coding-agents/ | reworded | The YOLO-mode quote and the Codex Cloud use for riskier tasks hold. "Where it worked" had tied the listed task kinds to YOLO mode, which the post does not say; fixed. |
| Q-015-P22 | sre.google/sre-book/postmortem-culture/ | holds | The triggers including "Data loss of any kind", blameless wording, senior-engineer review and "An unreviewed postmortem might as well never have existed" all match. |

Commit: 83f80d5 on build/source-checker/q-015 in /home/user/lib-q-015, committed as source-checker. The last paragraph is exactly the Agent-Session line (`session_01QBwHGNSLmSrYQgS6BPjV8p/source-checker-214`) and the Spec line you gave. Not pushed. It changed the Q-015 entries and their README rows. Each Sources line now records this check as an opener. The README rows were updated for entries 2, 5, 6, 8, 9, 14, 16, 17 and 24. The commit also touched P22, but only its opener line.

Still open, none of it affecting the verdict:
- library/facts/Q-002-F-m.md, outside this set, states "17.2x" (and, per its own title, errors amplified across 260 configurations). The arXiv abstract I read has 260 configurations but no 17.2 or 4.4 figure. It may be in the paper body, which I did not open; someone should check that entry.
- The README intro still says shelf lives are "the memo's proposals". That is generic text for the older rows and outside my lane, so I left it.
- Q-015-18 and Q-015-19 remain weak (C), single-report incidents, correctly marked not load-bearing.
