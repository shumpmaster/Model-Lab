# Ruling needed: how the touch log is guarded in trials, since its keeper knows each piece's side

Milestone: M9

The touch log records each time you step in during a conversation, and the live count reads it. The Chief of Staff keeps it and decides whether a touch is logged at all, and which piece it is put against. In a trial the Chief of Staff knows which pieces carry the method, so a touch left out or put against the wrong piece could, even without meaning to, favour one side. The monthly cross-check compares records with the log, so it cannot catch a conversation touch that was never written down. Whichever you choose, it will be listed among the trial's limits. Nothing is frozen, so nothing here is irreversible.

WHY: the trial's deciding measure counts the log's touches, so an unchecked keeper who knows the sides is a way to steer it; the plan cannot freeze until this is chosen (specs/S-002.md, J9; reviews/S-002-rulings-3/critic.md, finding 1).
OPTIONS:
  A. Leave it as a stated limit of the trial.
     Gain: no extra work.
     Cost: nothing catches a touch left out or put against the wrong piece.
  B. Before each trial look is judged, you confirm or add to that look's conversation lines through the desk.
     Gain: you are the one person who knows every time you stepped in, so the log is checked against the truth.
     Cost: a short list for you to read before each look.
  C. Before each trial look is judged, a fresh session that is not told the sides checks the log against the session records.
     Gain: no work for you, and the checker is blind to the side.
     Cost: a touch that left no trace in any session record is still missed.
RECOMMENDATION: B, with fair confidence (the Chief of Staff's judgement): only you know every time you stepped in, and a trial look is rare enough that the list stays short. What would change it: wanting no extra step for you (then C).
WHO HAS CHECKED IT: the Critic's re-check of the rulings written in raised it (reviews/S-002-rulings-3/_critic-verbatim.md, finding 1).
RISK CLASS: R0, a question only   REVERSIBILITY: reversible   BLAST RADIUS: the live count of touches in trials (E-004)
DEFAULT: none: the plan changes only on your answer   TIMEOUT: none

## Context
- The Chief of Staff writes every conversation touch's line in the touch log, with the piece it is put against (source: specs/S-002.md, J9)
- The agents and the Chief of Staff know which pieces carry the method (source: experiments/E-004.md, "What this trial cannot catch")
- The monthly cross-check compares records with the log and cannot catch a conversation touch never logged (source: reviews/S-002-rulings-3/_critic-verbatim.md, finding 1)
