# Ruling needed: whether the "later work" codes in live trials are checked by someone who does not know each piece's side

Milestone: M9

You ruled that, in the live count, the Chief of Staff decides whether each question asks for later work, and a question that does is not counted against the piece. In a trial the Chief of Staff knows which pieces carry the method being tried, and nobody checks those codes. So a code could, even without meaning to, favour one side. The plan lists every other way someone who knows the sides could steer a trial, but not this one. Whichever you choose, it will be listed. Nothing is frozen, so nothing here is irreversible.

WHY: the trial's deciding measure counts touches, and an unchecked coder who knows the sides is a way to steer it; the plan cannot freeze until this is chosen (specs/S-002.md, J1 and J9; reviews/S-002-rulings-2/critic.md, finding 1).
OPTIONS:
  A. Leave it as a stated limit of the trial: the Chief of Staff codes, unchecked, and the plan says so.
     Gain: no extra work.
     Cost: a coder who knows the sides decides which questions count, with nothing to catch a lean.
  B. Before each trial look is judged, a fresh session that is not told the sides checks every "later work" code on trial pieces; a code it does not confirm counts on the piece.
     Gain: the codes stay, and each one is checked by someone blind to the side.
     Cost: one more session before each look.
  C. For trial pieces only, treat every question as "not said", so it always counts on the piece under way; the "later work" code is kept for the starting figure and pieces outside trials.
     Gain: no judgement at all on trial pieces, so nothing to steer; both sides are counted the same way.
     Cost: both sides' touch counts run a little high, by the same rule.
RECOMMENDATION: C, with fair confidence (the Chief of Staff's judgement): it takes the judgement out of the trial altogether at no extra cost, and since both sides are counted alike the comparison stays fair. What would change it: wanting trial touch counts that match the starting figure's reading exactly (then B).
WHO HAS CHECKED IT: the Critic's re-check of the rulings written in raised it (reviews/S-002-rulings-2/_critic-verbatim.md, finding 1).
RISK CLASS: R0, a question only   REVERSIBILITY: reversible   BLAST RADIUS: the live count of touches in trials (E-004)
DEFAULT: none: the plan changes only on your answer   TIMEOUT: none

## Context
- In the live count the Chief of Staff codes `later_work` in the touch log (source: specs/S-002.md, J9; decisions/questions/P-002-later-work-coder.md, once #108 merges)
- The agents and the Chief of Staff know which pieces carry the method (source: experiments/E-004.md, "What this trial cannot catch")
- No second check of the live codes exists, and no list of what a trial cannot catch names it (source: reviews/S-002-rulings-2/_critic-verbatim.md, finding 1)
