# Ruling needed: how we will know the screening worked, when we stop, and what happens to a method a small trial cannot prove

Milestone: Discovery-2

WHY: Part 4 of this card asks whether to go below a written rule of the operating model: "Every load-bearing fact cites a source someone else has opened and confirmed; two independent sources for load-bearing facts". Its option A would let a method be tried on one source; that is a lighter standard, and so a proposal to the model, as your ruling on the screening's aim already said. Apart from that, this card sets how success is measured, the target, the date and when we stop. That is yours alone: it is never delegated and never defaults. Until it is set, the plan cannot say how a method is tried and kept, and the brief cannot go to you for the Design gate.

Your words: "how multi agent systems are run and optimized. For example, when anthropic says “90% of their work is performed by Claude” I want to achieve that level of agentic efficiency, trust, success in the strategy ideation and coding work from my operating model", and "Faith to me meant that we test/adopt methods that are promising rather than only those that are fully credentialed?" (your ruling on the aim).

**What the records show (the count of 447 merged pull requests to 9 November, Q-017).**
- 94 to 99 in every 100 ordinary commits (not counting merges) were made under an agent's name. A name is not proof of who did the work, but on a count of who made the changes, the 90% level is already passed, so that count could not show a gain.
- How often you had to step in is not recorded: questions asked in conversation leave no file, and your time is recorded nowhere. Your account merged every pull request except 86 merged by a robot on the desk.
- Whether work held up is not recorded either. No commit is marked as an undo (one worded otherwise would not be found), and the records cannot tell a repair from ordinary follow-on work.

**Words used below.**
- A **piece** is a merged pull request that changes built work, a plan or research; one that only files or answers a question, or only adds records, is not a piece.
- A **touch** is a time you had to step in on a piece before it merged: a question put to you about it, a fix you made, or a piece you sent back. Merging is not a touch.
- A **trial** tests one method on one kind of work (plans, research or built work). Each new piece of that kind is assigned by a coin toss, written down before work on it starts, to "with the method" or "without", in the same weeks, so nothing else that changes in those weeks can pass for the method. A trial is 30 pieces each way.
- **Holds up**: the method's pieces do no worse on two checks, by more than chance (the same test as below, at 1 in 10): passing their independent check at the first try, and not being reopened for a fault within 30 days. A reopening is marked by the reviewer of the later change, not by the piece's maker, and you are shown 5 of each trial's pieces at random, unlabelled; one you would not have accepted counts as reopened. A trial is judged 30 days after its last piece. Today plans pass their first check 2 times in 44, research 5 in 19 and built work 32 in 80, so for plans this check guards little; the reopen share has no starting figure yet.

**What must be built.** A log of touches and reopenings, designed and built in Design, under its own spec, by the agent that owns that work. It reads records and changes nothing in the prompt engine's work. It must count the starting figure, 60 pieces, before the first trial. Questions put in conversation are logged by hand by the Chief of Staff, so some may be missed; a method could also cut touches by agents asking less, which is what the hold-up checks are there to catch.

OPTIONS: in four parts, below, each ruled on its own and each ending with its own recommendation.

## Part 1: the measure and the target

The measure under every option: the share of pieces that needed at least one touch. The starting figure is that share over the 60 pieces before the first trial, all kinds together (60 pieces leaves it uncertain by about 13 points either way). At the date, it is counted again over the latest 60 pieces.

  A. **Halve the share of work that needs you.** *Target:* at the date, the share is at most half the starting figure, the fall clears chance at the line you choose in part 2, and the work holds up. *Gain:* it measures your "efficiency, trust" as less of you per piece, and works from whatever the starting figure turns out to be. *Cost:* the starting figure is unknown until 60 pieces are logged, so you cannot yet see how far half is.
  B. **Nine pieces in ten need no touch.** *Target:* at the date, at least 54 of the latest 60 pieces needed no touch, and the work holds up. *Gain:* it is the level you named. *Cost:* the 90% is your example and is not checked; who said it and what it counts are not recorded, and one outside estimate, informal and graded weak, put the company-wide share of merged code at "more like 50%" (Q-016-5). If the starting figure is already near nine in ten, the target says little; if it is far below, it may be out of reach.
  C. **Choose the measure now, set the number after the starting count.** *Target:* set by you once the 60 starting pieces are counted, before the first trial. *Gain:* the number rests on the real starting figure. *Cost:* this part comes back to you a second time.

*Reversible, for every option:* yes, until the first trial starts. After that, changing the target discards the starting count and is a new target.

RECOMMENDATION (part 1): A, with medium confidence: it measures your involvement and works from any starting figure. If you want your own level as the target, B; if you would rather see the starting figure first, C.

## Part 2: how sure a trial must be before a method is kept

A method is kept when its pieces need you less often than the others by enough that chance alone would produce the difference at most once in the number you choose here, and the work holds up. You said missing a helpful method and adopting a harmful one worry you "Both equally". The figures below are for 30 pieces each way and a method that truly halves the share; "start" is the share of pieces that need you today, which is not yet known, so two are shown. They are before the hold-up checks, which fail a harmless method about 1 time in 7 by chance.

  A. **1 in 10.** One trial keeps a real halving about 7 times in 10 at a start of 1 in 2, and about 4 in 10 at a start of 3 in 10. A method that does nothing is kept fewer than 1 time in 10. *Gain:* fewer real gains missed. *Cost:* if only 1 method in 10 tried really helps, about half or more of the methods kept would do nothing.
  B. **1 in 40, the prompt engine's line.** One trial keeps a real halving about 4 times in 10 at a start of 1 in 2, and about 2 in 10 at 3 in 10; a method that does nothing is kept about 1 time in 70 to 80. *Gain:* fewer useless methods kept: if 1 in 10 tried really helps, about a quarter to two-fifths of those kept would do nothing. *Cost:* more real gains missed, which part 3 can soften.

Which makes fewer mistakes depends on how many tried methods really help. Counting, per 10 methods tried, the real ones missed plus the useless ones kept (with part 3's option A): if 1 in 10 really helps, about 1 mistake at 1 in 10 against between half and four-fifths of one at 1 in 40; if half really help, about 1 to 2 at 1 in 10 against 1 to 3 at 1 in 40. In web experiments, the research found that more than half of ideas fail, and in some areas 9 in 10 experiments do (Q-013); whether that holds for screened methods is not known, and part 4's option A would let more untested methods in.

*Reversible:* yes, until the first trial starts.

RECOMMENDATION (part 2): B, with medium confidence: if most methods tried do not help, as the research suggests, it makes fewer mistakes, and part 3's option A recovers much of what it misses. If you expect most screened methods to help, A.

## Part 3: what happens to a trial that ends "not shown"

"Not shown" means the gain did not clear the line in part 2; it is not the same as "does not help" (Q-013). Small trials of a real gain will often end this way.

  A. **One planned second look.** Before a trial starts, its plan says: if the method is not kept at 30 pieces each way but its pieces needed you less often ("leans the right way"), 30 more each way are assigned, and all 60 each way are judged together. Both looks use one line, fixed in advance and set slightly stricter so that a method that does nothing is still kept no more often than the line you chose in part 2. This is one trial registered whole before it starts, not a re-run after seeing results, which the operating model forbids. At 1 in 40, a real halving is then kept about 8 times in 10 at a start of 1 in 2 and about 4 in 10 at a start of 3 in 10 (at 1 in 10: about 9 and 7 in 10). Still not shown after the second look: the method is dropped and the result is filed in the library. A method whose pieces do worse, or that does not hold up, is dropped at the first look. *Gain:* a promising method gets a second chance without raising the chance of keeping a useless one. *Cost:* between about 3 and 7 trials in 10 go on to the second look, doubling their pieces and your touches on them.
  B. **Drop at once.** A "not shown" method is dropped and the result filed; it may come back only with a trial plan that is truly different. *Gain:* simplest and least of your time. *Cost:* promising methods dropped after one small trial, the risk the plan names in advance.
  C. **Keep on promise, with a review.** A "not shown" method that holds up stays in this project's way of working and is reviewed after its next 30 pieces, then removed if it still shows nothing. It reaches the operating model only after a trial shows a gain. *Gain:* the most room for faith. *Cost:* it keeps a method that missed the line set before its trial, against the model's rule "Killed, not tuned" and the plan's first risk, adopting what is popular rather than what helps; with part 4's option A, a method could stay with neither two sources nor a shown gain.

*Reversible:* yes, for trials not yet started.

RECOMMENDATION (part 3): A, with medium confidence: it gives promising methods a fair second chance inside the rules. If your time on trials matters most, B; if you would rather keep a promising method in use while it proves itself, C.

## Part 4: what a method needs before it may be tried

  A. **One source, opened and confirmed by someone else, describing the method.** It is tried only if its conditions have been read against ours (clear misfits are not tried) and any outside code, prompt or skill has been checked before it runs, with no data out, as you ruled. This is below the model's two-source rule, and choosing it makes it a proposal to the operating model at the end of the cycle. Under part 3's A or B, keeping rests only on our own trial. *Gain:* new methods can be tried while they are new, as you asked. *Cost:* more trials of methods that turn out to be hype; each trial costs pieces and touches.
  B. **Two independent sources, as for any fact the work relies on.** *Gain:* fewer trials of hype; no departure from the rule. *Cost:* new methods often have one source, so they wait for a second, against your "promising rather than only those that are fully credentialed".

*Reversible:* yes.

RECOMMENDATION (part 4): A, with medium confidence: it is the standard you described, and our own trial still decides. If you would rather run fewer trials and adopt later, B.

RECOMMENDATION: A, B, A, A, for parts 1 to 4; each part's reason is given after it.

**As it would be written in the plan (with the recommendations):** "V1: share of pieces of work that needed at least one owner touch before merging, over the latest 60 pieces, at most half the starting figure counted over the 60 pieces before the first trial, the fall clearing chance at 1 in 40 and the work holding up; checked six months after the first trial starts".

**Proposed under every option, for the date, the miss and the stop rule** (proposals; your ruling makes them so):
- **Date:** each trial is judged 30 days after its last piece. The target is checked six months after the first trial starts, and at each screening review after that. To set no date, or another, say so.
- **How long a trial takes:** not yet known; the log will show it. For scale, 163 pull requests of every kind merged in the first nine days of November across the three repositories, but how many were pieces of one kind is not counted.
- **Miss:** if the target is not reached at the check, you rule whether to re-aim the screening or close it. Kept methods stay only on their own results; none is adjusted to pass.
- **Every kept method:** a review date six months on and a way to remove it; a change of AI model triggers a re-check of the methods kept under the old one. A change of model during a trial voids that trial.
- **Stop at once:** a trial stops if its pieces fail the hold-up checks at the first look, or if it breaks work you rely on.
- **Stop and come back to you:** if the starting count shows fewer than 6 of the 60 pieces needed you (little room to gain); or if the first five trials all end with the method dropped (you rule whether to re-aim, for example with other sources, or close).
- **Apart from the prompt engine:** one method per kind of work at a time. The hold-up checks use the prompt engine's measure, first-time pass, only as a guard, never as a target. No method that could change how often work passes its first check is tried on a kind of work while the prompt engine is testing that kind, or counting its 30 real-use pieces; the Design gate rules whether any trial may start before the prompt engine finishes, as the plan already proposes.
- **Your time:** touches are the measure itself, and each status update reports them. Each trial adds 5 short reads for you and one result card. Your hours are recorded nowhere. The ceilings on spend and on your time are set at the Design gate, as you ruled, and no trial runs before then.

WHO HAS CHECKED IT: the Critic, on a different AI model from the writer (record: reviews/P-002-value-target/critic.md).
RISK CLASS: R3 (a value target, the owner's own ruling)   REVERSIBILITY: reversible until the first trial starts   BLAST RADIUS: how the screening's trials are run and judged, which methods are kept, and which reach the operating model and the desk
DEFAULT: none — value targets are never delegated or defaulted   TIMEOUT: none

## Context
- A value target states a measure, target, date and miss, including the cost to the owner's time; value targets are never delegable (source: Personal-Org-Operating-Model OPERATING_MODEL.md §1 item 13, §2 "Delegation grants", §4 definition of ready item 6)
- The two-source rule, quoted, and the experiment rules: a frozen registration, no re-running for a better answer, null results are results (source: Personal-Org-Operating-Model OPERATING_MODEL.md, "The knowledge method (D-032)" and "The experiment playbook (D-047)")
- The owner's aim, their meaning of "faith", the 90% figure used only as their example, and the rule that the evidence standard comes to the owner at this card as a proposal to the model (source: decisions/questions/P-002-target.md)
- The owner's answers that both risks weigh equally, that outside tools are allowed only with no data out, that the screening stays separate from the prompt engine, and that time and money are set at the Design gate (source: decisions/questions/P-002-groundwork-shortlist.md, answers 3, 6, 7 and 8)
- 447 merged pull requests; ordinary commits under an agent identity 94.2%, 98.9% and 97.8%; the owner's account merged all but 86 bot merges; no commit subject starts "Revert"; an identity is not proof (source: research/Q-017-memo.md, opening paragraph and §2, §4)
- Questions asked or answered in conversation, repairs told apart from follow-on work, and the owner's time are not in the records (source: research/Q-017-memo.md §3 "What the extract cannot show", §4 "What the extract cannot show", §5)
- 163 merged pull requests in November to the 9th: 66, 85 and 12 (source: research/Q-017-memo.md §1, "Pull requests per month")
- First-time pass at the independent check: plans 2 of 44, research 5 of 19, built work 32 of 80; the prompt engine's line is 1 in 40 and its real-use count is 30 pieces of each kind in any project (source: docs/PROJECT.md section 6, V1, V2 and "Starting figures"; decisions/questions/P-002-q017-decide.md)
- An outside, informal estimate put Anthropic's company-wide share of merged lines written by AI at "more like 50%", graded weak (source: portfolio library/facts/Q-016-5.md)
- Few-run trials reliably find only large effects; a significant result is less likely to be real where most changes fail; more than half of ideas fail, and in some domains 9 in 10 experiments; a rule fixed in advance for more than one look keeps the false-result rate where it was set (source: research/Q-013-memo.md, "Answer as far as the evidence goes" and §1)
- Every odds figure, the two-look lines, the hold-up guard's false-fail chance and the mistakes per 10 methods are the Chief of Staff's exact one-sided Fisher calculation, with scripts and output (source: intake/P-002-value-target-odds-2026-11-10.md, rounds 1 and 2)
- The risks this card's plan carries: R1, R2, R3, R4, R5, R9, R10, R11, R12, R14, R15, R16, R17 (source: docs/projects/P-002.md section 7)
- The Critic's round 1 findings this draft answers (source: reviews/P-002-value-target/critic.md)
