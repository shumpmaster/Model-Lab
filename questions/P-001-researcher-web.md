# Ruling needed: may researchers read web pages themselves?

Milestone: Discovery-8

WHY: The operating model contradicts itself. Its rule says text from the web is read only by the Input reader, a role that can write nothing and passes on structured findings. But the Researcher's role file gives it web search and web fetch, and every research brief in this project let the Researcher read the web directly. Since this was found, no new research here reads the web until you rule. This is a change to the model's rules, which is yours to decide. Whichever you choose lands in the operating model under its own rules.

What is known: web pages can carry hidden instructions aimed at AI agents ("prompt injection"); it is a recognised kind of attack, and a vendor and a UK government security agency say it is not solved and may never be fully prevented (portfolio library: Q-007-F08, Q-007-F09). Today the Researcher holds no write tools and no shell, and every memo it writes is checked source by source by a Source checker on a different AI model.

OPTIONS:
  A. **The rule governs: only the Input reader reads the web.** The Researcher loses its web tools and works from the Input reader's findings. *Gain:* the role that reasons about the project never reads untrusted text. *Cost:* an extra step and more tokens for every research item, and detail can be lost in the Input reader's summary. *Reversible:* yes.
  B. **The tool grant governs: researchers may read the web directly.** The rule is changed to allow it, naming the limits that already exist (no write tools, no shell, every page treated as a claim, a Source checker on a different AI model). *Gain:* research stays as fast and cheap as it has been. *Cost:* a role that reasons about the project reads text that may carry hidden instructions; the limits contain what it can do, but not what it might write in its memo, which the Source checker must catch. *Reversible:* yes.
  C. **Leave both as they are until the prompt engine has evidence.** Research here goes on without the web, and the question returns with this project's results on how instructions and tool grants interact. *Gain:* the rule is decided on evidence. *Cost:* the contradiction stays in the model meanwhile, and any research needing outside sources waits. *Reversible:* yes.

RECOMMENDATION: B, with low-to-medium confidence: the limits that contain an injected instruction (no write tools, no shell, an independent Source checker) are already in place, and the outside evidence favours limits on what a role can do over wording alone (research Q-007). What would change it: evidence that a memo carried an injected claim past a Source checker, which would favour A.
WHO HAS CHECKED IT: the Critic, on a different AI model from the writer (record: reviews/P-001-researcher-web/critic.md).
RISK CLASS: R3 (a change to the model's rules)   REVERSIBILITY: reversible   BLAST RADIUS: every project's research, and the Researcher's and Input reader's role files
DEFAULT: none — a rule change is never defaulted   TIMEOUT: none

## Context
- Untrusted text, including web pages, is read only by the Input reader, which holds no write tools (source: Personal-Org-Operating-Model OPERATING_MODEL.md §5 "Who sees what")
- The Researcher's role file grants web search and web fetch (source: Personal-Org-Operating-Model template-v3/.claude/agents/researcher.md line 4)
- The research briefs for Q-001 to Q-007 let each Researcher read the web directly, and no further dispatch reads the web until this is resolved (source: docs/LEDGER.md L-0005; docs/LESSONS.md LL-07)
- Indirect prompt injection is a recognised attack class, not considered solved (source: portfolio library/facts/Q-007-F08.md, Q-007-F09.md)
- The research found structural limits on what each role reads and can do recommended over wording alone (source: research/Q-007-memo.md, bottom line 2)
