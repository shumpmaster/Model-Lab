# Ruling needed: how we will know the screening worked, when we stop, and what happens to a method a small trial cannot prove

Milestone: Discovery-2

WHY: Part 4 of this card asks whether to go below a written rule of the operating model: "Every load-bearing fact cites a source someone else has opened and confirmed; two independent sources for load-bearing facts". Its option A would let a method be tried in this project on one source, from now on. That is a lighter standard, so choosing it also sends the standard to the model as a proposal, as the record of your ruling on the screening's aim noted. The rest of the card sets how success is measured, the target, the date and when we stop. That is yours alone and never defaults. Until it is set, the plan cannot say how a method is tried and kept, and the brief cannot go to you for the Design gate.

Your words: "how multi agent systems are run and optimized. For example, when anthropic says “90% of their work is performed by Claude” I want to achieve that level of agentic efficiency, trust, success in the strategy ideation and coding work from my operating model", and "Faith to me meant that we test/adopt methods that are promising rather than only those that are fully credentialed?" (your ruling on the aim).

**What the records show** (the count of the three repositories to 8 November, Q-017):
- 94 to 99 in every 100 ordinary commits (not merges) were made under an agent's name. A name is not proof of who did the work, but on a count of who made the changes the 90% level is already passed, so that count could not show a gain.
- How often you stepped in is not reliably recorded: about 15, 7 and 32 in 100 pull requests hold a change under your name, but questions asked in conversation leave no file, and your time is not in the records.
- Whether work held up is not recorded: no commit is marked as an undo (one worded otherwise would not be found), and a repair cannot be told from follow-on work.

**Words used below.**
- A **piece** is a merged pull request, in any of the three repositories, that changes built work, a plan or research; one that only files or answers a question, or only adds records, is not a piece.
- A **touch** is a time you stepped in on a piece before it merged: a question to you about it, a fix you made, or a piece you sent back. Merging is not a touch.
- A **trial** tests one method on one kind of work. Each new piece of that kind is assigned, before work on it starts, to "with the method" or "without", by shuffled draws so each side gets 30, in the same weeks, so that nothing else changing in those weeks can pass for the method. Every piece still passes all its usual checks and your merge, and can be undone.
- **Holds up**: the method's pieces do no worse, by more than chance at 1 in 10, on two checks: passing their independent check first time, and not being reopened for a fault within 30 days. A reopening is marked by the reviewer of the later change, not the piece's maker. You also see 5 of each trial's pieces at random, unlabelled; one you would not have accepted counts as reopened. A trial is judged 30 days after its last piece.

**Limits of this design, under every option.**
- **It is a coarse guard against harm.** A method that doubles how often pieces fail a check, from 10, 15 or 25 in 100, is caught only about 3 to 7 times in 10 at 30 pieces each way (5 to 9 in 10 at 60), and less often the rarer the fault; the reopen share has no starting figure yet. A harmless method fails it by chance about 1 time in 7 (up to about 1 in 5 with a second look), taking the two checks as independent. The main protection stays the usual checks and your merge, which no trial skips, and the review date of every kept method. Plans pass their first check only 2 times in 44 today, so for plans that check guards little.
- **Trials are slow.** In the count, which runs from September to 8 November with most of it from October, 55 pull requests touched research, 150 plans and 124 built work across the three repositories. At that pace one trial of research takes months, and of plans or built work several weeks, before any second look and the 30-day wait.
- **Only methods that can be switched piece by piece fit.** A change to rules or to how sessions run cannot be, and a method that leaks into the "without" pieces shrinks the difference. How to try such methods is left to each trial's plan, which would say it is weaker.
- **Not blind.** The agents and the Chief of Staff, who logs questions put in conversation by hand, know which pieces carry the method; only your 5-piece sample is unlabelled. So agents could ask you less on those pieces; the hold-up checks are there to catch that. The draw is recorded in the log, and each trial's result is worked out by the Reviewer, not by whoever ran it.

**What must be built.** A log of touches and reopenings, specced in Design and built by the Builder only after you approve the Design gate, with the spend ceiling. It reads records and changes nothing in the prompt engine's work. It counts a starting figure over 60 pieces before the first trial.

OPTIONS: in four parts, below, each ruled on its own.

## Part 1: the measure and the target

The measure: the share of pieces that needed at least one touch. The starting figure is that share over the 60 pieces before the first trial, all kinds together (uncertain by about 13 points either way). At the date, it is counted again over the latest 60. Holding up, for the target, means the latest 60 pieces do no worse on the two checks than the starting 60, by more than chance at 1 in 10. The two counts are months apart, so anything else that changed in between, such as a new AI model or the prompt engine's changes, counts too; the trials, not the target, show which methods helped.

  A. **Halve the share of work that needs you.** As it would be written: "V1: share of pieces needing at least one owner touch, over the latest 60 pieces, at most half the starting figure, the fall clearing chance at the part 2 line, with the work holding up; checked 12 months after the first trial starts". *Gain:* it measures your "efficiency, trust" as less of you per piece, from any starting figure. *Cost:* the starting figure is unknown until counted; and even if the share truly halves, the count shows it only about 4 to 5 times in 10 at starts of 1 in 2 and 3 in 10, and less often at lower starts, so a miss is weak evidence on its own.
  B. **Nine pieces in ten need no touch.** As it would be written: "V1: at least 54 of the latest 60 pieces needed no owner touch, with the work holding up; checked 12 months after the first trial starts". *Gain:* it is the level you named. *Cost:* the 90% is your example and is not checked; who said it and what it counts are not recorded, and one informal outside estimate, graded weak, put the company-wide share of merged code at "more like 50%" (Q-016-5). If the start is already near nine in ten, the target says little; if far below, it may be out of reach.
  C. **Choose the measure now, set the number after the starting count.** As it would be written: "V1: share of pieces needing at least one owner touch, over the latest 60 pieces, target set by the owner once the starting 60 are counted; checked 12 months after the first trial starts". *Gain:* the number rests on the real starting figure. *Cost:* this part comes back to you.

*Reversible:* yes, until the first trial starts; after that a change discards the starting count and is a new target.

RECOMMENDATION (part 1): A, medium confidence: it sets the target from the real starting figure without fixing a level now, though a low start makes it hard to show. B if you want your own level as the target; C if you would rather see the starting figure first.

## Part 2: how sure a trial must be before a method is kept

A method is kept when its pieces needed you less often than the others by enough that chance alone would produce it at most once in the number chosen here, and the work holds up. You said missing a helpful method and adopting a harmful one worry you "Both equally"; harm is the hold-up guard's job, above. This part trades a useful method missed against a useless one kept.

  A. **1 in 10.** A useless method is kept at most about 1 time in 10.
  B. **1 in 40, the prompt engine's line.** A useless method is kept about 1 time in 40 or less.

Mistakes per 10 methods tried (useful ones missed plus useless ones kept, with part 3's option A), where "start" is the share of pieces needing you today, not yet known:

| If this many tried methods really halve it | Start | A: 1 in 10 | B: 1 in 40 |
|---|---|---|---|
| 1 in 10 | 1 in 2 | 0.9 | 0.5 |
| 1 in 10 | 3 in 10 | 1.2 | 0.8 |
| 5 in 10 | 1 in 2 | 0.9 | 1.3 |
| 5 in 10 | 3 in 10 | 2.0 | 3.0 |

These figures, like the keep odds in part 3, are before the hold-up checks, which fail a harmless method about 1 time in 7 to 1 in 5 and so lower every keep figure by about that much; the tie point does not move. The two tie when about 2 to 3 in 10 tried methods really help: below that B makes fewer mistakes, above it A does. No source gives that share for screened methods. In web experiments more than half of ideas fail, and in some areas 9 in 10 experiments do, counting bad ideas and faulty set-ups together (Q-013); whether that carries to screened methods is not known. Part 4's option A would let more untested methods in.

*Reversible:* yes, until the first trial starts.

RECOMMENDATION (part 2): none. The choice turns on how many screened methods you expect to help, which no record gives, and on how you weigh a useful method missed against a useless one kept, which is yours.

## Part 3: what happens to a trial that ends "not shown"

"Not shown" means the gain did not clear the part 2 line. With so few pieces it is not the same as "does not help" (the plan's reading of the research, section 2).

  A. **One planned second look.** The trial's plan says, before it starts: if the method is not kept at 30 pieces each way but its pieces needed you less often, 30 more each way are assigned straight away and all 60 each way are judged together. Both looks use one line, fixed once the starting share is counted, a little stricter than the part 2 line so that a useless method is still kept no more often than that line (checked at starting shares of 1 in 2 and 3 in 10). If the first look's hold-up checks fail when judged, the second look stops and the method is dropped. This is one trial planned whole before it starts, not a re-run after seeing results, which the operating model forbids. *Gain:* a useful halving is kept about 8 and 4 times in 10 (starts of 1 in 2 and 3 in 10) at 1 in 40, against 4 and 2 in 10 with one look; at 1 in 10, about 9 and 7 against 7 and 4. *Cost:* between about 3 and 7 trials in 10 go on, doubling their pieces, your touches and their length.
  B. **Drop at once.** The method is dropped and its result filed in the library; it may come back only with a trial plan that is truly different. *Gain:* simplest and least of your time. *Cost:* useful methods dropped after one small trial, the risk the plan names in advance.
  C. **Keep on promise, with a review.** A "not shown" method that holds up stays in this project's way of working, is reviewed after its next 30 pieces and removed if it still shows nothing; it reaches the operating model only after a trial shows a gain. *Gain:* the most room for faith. *Cost:* it keeps a method that missed the line set before its trial, against the model's rule "Killed, not tuned" and the plan's risk of adopting what is popular rather than what helps; with part 4's option A, a method could stay with neither two sources nor a shown gain.

*Reversible:* yes, for trials not yet started.

RECOMMENDATION (part 3): A, medium confidence: a fair second chance inside the rules. B if your time on trials matters most; C if you would rather keep a promising method in use while it proves itself.

## Part 4: what a method needs before it may be tried

  A. **One source, opened and confirmed by someone else, describing it.** It is tried only once its conditions are read against ours (clear misfits are not tried) and any outside code, prompt or skill is checked before it runs, with no data out, as you ruled. Trials on one source may start in this project; the lighter standard itself goes to the operating model as a proposal at the end of the cycle. Under part 3's A or B, keeping rests only on our own trial. *Gain:* new methods tried while new, as you asked. *Cost:* more trials of hype, each costing pieces, touches and weeks.
  B. **Two independent sources, as for any fact the work relies on.** *Gain:* fewer trials of hype; no departure from the rule. *Cost:* new methods often have one source, so they wait, against your "promising rather than only those that are fully credentialed".

*Reversible:* yes.

RECOMMENDATION (part 4): A, medium confidence: it is the standard you described, and our own trial still decides. B if you would rather run fewer trials and adopt later.

RECOMMENDATION: A for parts 1, 3 and 4; none for part 2, as given there.

**Proposed under every option** (proposals; your ruling makes them so):
- **Date:** each trial is judged 30 days after its last piece; the target is checked 12 months after the first trial starts, since trials take weeks to months, and at each screening review after that. To set another date, or none, say so.
- **Miss:** you rule whether to re-aim the screening or close it. Kept methods stay only on their own results; none is adjusted to pass.
- **After the first five trials:** a summary comes to you, and you rule whether to go on. Five drops in a row can happen by chance even if methods help: with part 3's option A, about 1 to 4 times in 10 if half really help, and about 5 to 8 in 10 if 1 in 10 do; more often with one look.
- **Stop and come back to you** if the starting count shows fewer than 6 of 60 pieces needed you (little room to gain).
- **Stop a trial at once** if its first look fails the hold-up checks, or it breaks work you rely on. A change of AI model during a trial voids it.
- **Every kept method:** a review date six months on and a way to remove it; a change of AI model triggers a re-check of the methods kept under the old one.
- **Apart from the prompt engine:** one method per kind of work at a time. The hold-up checks use the prompt engine's measure, first-time pass, only as a guard. No method that could change how often work passes its first check is tried on a kind of work while the prompt engine is testing that kind or counting its 30 real-use pieces; the Design gate rules whether any trial may start before the prompt engine finishes.
- **Your time:** touches are the measure, and each status update reports them; each trial adds 5 short reads and one result card. Spend and time ceilings are set at the Design gate, as you ruled; no trial runs before then.

WHO HAS CHECKED IT: the Critic, on a different AI model from the writer, passed it at round 3 (record: reviews/P-002-value-target/critic.md). The odds are the Chief of Staff's own calculations; the Critic read the code and checked them by hand, but no one else has run them, and an independent run is proposed before the Design gate.
RISK CLASS: R3 (a value target, the owner's own ruling)   REVERSIBILITY: reversible until the first trial starts   BLAST RADIUS: how the screening's trials are run and judged, which methods are kept, and which reach the operating model and the desk
DEFAULT: none — value targets are never delegated or defaulted   TIMEOUT: none

## Context
- A value target states a measure, target, date and miss, including the cost to the owner's time; value targets are never delegable (source: Personal-Org-Operating-Model OPERATING_MODEL.md §1 item 13, §2 "Delegation grants", §4 definition of ready item 6)
- The two-source rule, quoted, and the experiment rules: a frozen registration, no re-running for a better answer, null results are results (source: Personal-Org-Operating-Model OPERATING_MODEL.md, "The knowledge method (D-032)" and "The experiment playbook (D-047)")
- The owner's aim and meaning of "faith"; the 90% figure used only as their example; the record's note that a lighter evidence standard comes to the owner at this card as a proposal to the model (source: decisions/questions/P-002-target.md, the owner's words and "How it is carried out")
- The owner's answers that both risks weigh equally, outside tools only with no data out, the screening separate from the prompt engine, time and money set at the Design gate (source: decisions/questions/P-002-groundwork-shortlist.md, answers 3, 6, 7 and 8)
- Ordinary commits under an agent identity 94.2%, 98.9% and 97.8%; pull requests with an owner-identity commit 48/312, 6/85 and 16/50; no commit subject starts "Revert"; an identity is not proof (source: research/Q-017-memo.md, opening paragraph and §2, §4)
- Questions asked in conversation, repairs told apart from follow-on work, and the owner's time are not in the extract (source: research/Q-017-memo.md §3 and §4 "What the extract cannot show", §5)
- Pull requests touching research 29, 21 and 5; plans 100, 19 and 31; built work 90, 8 and 26; months covered September to November (source: research/Q-017-memo.md §1, "Pull requests per month" and "By kind")
- First-time pass: plans 2 of 44, research 5 of 19, built work 32 of 80; the prompt engine's line is 1 in 40 and its real-use count is 30 pieces of each kind (source: docs/PROJECT.md section 6; decisions/questions/P-002-q017-decide.md)
- An informal outside estimate put Anthropic's company-wide share of merged lines written by AI at "more like 50%", graded weak (source: portfolio library/facts/Q-016-5.md)
- Few-run trials find only large effects; more than half of ideas fail, and in some domains 90% or more of experiments, counting bad ideas and buggy implementation together, a web-scale figure; a rule fixed in advance for more than one look keeps the false-result rate where it was set (source: research/Q-013-memo.md, "Answer as far as the evidence goes" and §1, §2)
- "Not shown" is not "does not help" as the plan's reading of that research (source: docs/projects/P-002.md section 2, "Few runs can only show large differences")
- Every odds figure, the mistakes table, the hold-up guard from both sides, the target's chance of showing a real halving and the five-drops figures are the Chief of Staff's exact one-sided Fisher calculations, with scripts and output (source: intake/P-002-value-target-odds-2026-11-10.md, rounds 1 to 3)
- The pre-mortem risks this plan carries: R1, R2, R3, R4, R5, R9, R10, R11, R12, R14, R15, R16, R17 (source: docs/projects/P-002.md section 7)
- The Critic's rounds 1 and 2 (source: reviews/P-002-value-target/critic.md)
