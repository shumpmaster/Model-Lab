# Ruling needed: how long a library fact stays trusted, and how its strength is labelled

Milestone: Discovery-5

WHY: Your portfolio now holds a library of 88 checked facts and patterns. Two of its rules are open: how long a fact may be relied on before it must be checked again (its "shelf life"), which the operating model leaves to you, and how an entry's strength is labelled, which no rule settles. Today each entry carries the shelf life its research proposed, and its strength is labelled strong, moderate or weak by mapping the research's letter grades, which do not all mean the same thing: in one memo "A" means "the researcher opened it", not "strong evidence". Until you rule, later projects may rely on stale facts, or read a label as stronger than it is. These are rules for the whole model, so your choice lands there under its own rules.

OPTIONS:
  A. **Each entry keeps the shelf life its research proposed, and strength is relabelled from what was checked.** A label says what backs the fact: two independent sources opened; one source opened; vendor's own statement; or a calculation. *Gain:* labels say plainly what a reader can lean on; no shelf lives change. *Cost:* the 88 entries are relabelled once, by the Source checker; proposed shelf lives vary by researcher. *Reversible:* yes.
  B. **Fixed shelf lives by kind of fact, plus the relabelling in A.** For example: facts about AI models and vendors' products, 6 months; research findings about AI, 18 months; findings from other fields, 5 years. *Gain:* one predictable rule, shortest where things change fastest. *Cost:* the 88 entries get new shelf lives as well as new labels; the periods are a judgement, not measured. *Reversible:* yes.
  C. **Keep things as they are** until the second idea (screening AI practice), which will use the library most, gives evidence. *Gain:* no work now. *Cost:* the labels' mixed meaning stays, and a reader may over-trust a fact. *Reversible:* yes.

RECOMMENDATION: B, with medium confidence: AI facts go stale fast, and a fixed rule means no one has to judge each entry. What would change it: if you would rather not set periods without data, A.
WHO HAS CHECKED IT: the Critic, on a different AI model from the writer (record: reviews/P-001-library-rules/critic.md).
RISK CLASS: R3 (a rule of the model)   REVERSIBILITY: reversible   BLAST RADIUS: every project that relies on the library
DEFAULT: none — a rule change is never defaulted   TIMEOUT: none

## Context
- Library facts carry a checked-on date and a shelf life, and shelf lives are an open owner call; past it, a fact is re-checked before a project relies on it (source: Personal-Org-Operating-Model OPERATING_MODEL.md §6 "The library")
- The library holds 69 facts and 19 patterns filed on 2026-11-01, each with its research's proposed shelf life (source: portfolio library/README.md)
- The Source checker mapped letter grades to strong, moderate and weak, and noted that one memo's "A" means opened, which may overstate vendor self-reports (source: portfolio PR #3, "What this means for you")
- The fact form has no field for what backs the strength beyond the grade (source: portfolio library/facts/_TEMPLATE.md)
