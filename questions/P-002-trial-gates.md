# Ruling needed: your two approvals on every screened method, and whether you may adopt one its trial did not pass

Milestone: Discovery-2

WHY: Option A, recommended, goes outside a written rule of the operating model, "Killed, not tuned": "A design that fails its predeclared gate dies. It may be replaced by a genuinely different design (§5), never adjusted until it passes." Choosing A also sends that change to the model as a proposal, as your part 4 answer did for evidence. B and C stay inside it. This card replaces part 3 of the value-target question, which you answered with your own design, because "An automated pipeline could end up killing a lot. I think ultimately every suggestion needs a very tight review with approval from me. Effectively another gate." It is part of the value target, so it is yours alone and never defaults. Until it is ruled, the plan cannot say what happens after a trial, and the brief cannot go to you for the Design gate.

Your words on how it should work: "the new ideas enter with a very plain English summary. Effectively just a very clear clean assessment of what the change would be, how we do it today, why we would potentially do it, and what is the impact & risks - based on the initial assessment. Then if I approve, it’s tested and tried, then the results come in a similar more detailed format à la the gate of which I approve or reject the final implementation to the model".

**Words.**
- A **piece** is a merged pull request that changes built work, a plan or research. A **trial** runs 30 pieces with the method and 30 without, assigned by shuffled draws before work starts.
- A trial is **passed** when the method's pieces needed you less often by more than chance at the 1 in 10 line you chose, and its work **held up**: no worse, by more than chance at 1 in 10, at passing its first independent check or at not being reopened for a fault. Anything else is **not passed**.
- **One-source entry** is your part 4 answer: one confirmed source is enough to try a method.

**Under every option:**
- **Entry card (your design).** Each method comes to you first as a short plain-English card: what the change would be, how we do it today, why we might do it, and its impact and risks. Nothing is tried unless you approve it. *Added by the Chief of Staff:* the card says what the first assessment rests on, and carries the trial's plan, which is then fixed.
- **Results card (your design).** After the trial, the results come to you in more detail, like a gate card. *Added:* it carries the Critic's view and a recommendation. Nothing enters the operating model or the desk without your approval there.
- **Nothing is dropped by the pipeline.** Every result comes to you.

**How often a trial passes a method that truly halves how often work needs you**, before the hold-up checks (which also turn away a harmless method about 1 time in 7 with one look, up to 1 in 5 with two):

| | If half of pieces need you today | If 3 in 10 do |
|---|---|---|
| One look | about 7 in 10 | about 4 in 10 |
| Two looks, planned in advance | about 9 in 10 | about 7 in 10 |

A second look means: if the first look leaned the right way (the method's pieces needed you less often), 30 more each way, judged together on a slightly stricter line so a useless method passes no more often. It is planned on the entry card, so it is one trial planned whole, not a re-run after seeing results. Many useful methods will still come back "not passed".

OPTIONS: (these letters are new; they do not match the earlier part 3's)
  A. **You decide every result, as you worded it.** Two looks planned. On any result, passed or not, you approve or reject putting the method into the operating model; the results card says plainly when it was not passed and why. *Gain:* your approval decides every time, and nothing promising is lost to a small trial. *Cost:* methods with no passed trial can enter the model, against "Killed, not tuned" and the plan's first risk, adopting what is popular rather than what helps; with one-source entry, such a method rests on one source and your judgement. *Reversible:* yes; a method comes out of the model by a model change, which you rule.
  B. **You approve passed results; for the rest, reject or one new design.** Two looks planned. Only a passed method may go into the model, with your approval. On a "not passed" result you reject it, or approve one genuinely different trial design on a fresh entry card; the Critic checks it is genuinely different, and a method that fails twice goes back to the screening. *Gain:* every method in the model passed a trial. *Cost:* your approval cannot keep a "not passed" method; about 3 to 5 trials in 10 run twice as long. The rule allows a failed design to be "replaced by a genuinely different design"; B reads a new trial design as that, and if the stricter reading holds (only a different method counts), B's only answer to "not passed" is to reject. *Reversible:* yes, for trials not yet started.
  C. **As B, one look only.** *Gain:* shorter, simpler trials. *Cost:* fewer useful methods pass (the one-look row above). *Reversible:* yes, for trials not yet started.

RECOMMENDATION: A, with low confidence. It is what you asked for; a small trial is weak evidence either way, and you rule every change to the model in any case, with the trial's result and the Critic's view in front of you. What would change it: if you want the model to take only methods a trial has passed, B; if shorter trials matter more, C.
WHO HAS CHECKED IT: the Critic, on a different AI model from the writer, failed rounds 1 and 2 (record: reviews/P-002-trial-gates/critic.md). The odds are the Chief of Staff's own calculations, read and checked by hand by the Critic, not yet run by anyone else; an independent run is proposed before the Design gate.
RISK CLASS: R3 (part of a value target, the owner's own ruling)   REVERSIBILITY: reversible (as given for each option)   BLAST RADIUS: which screened methods are tried and put into the operating model and the desk, how long trials take, and how many cards come to the owner
DEFAULT: none — value targets are never delegated or defaulted   TIMEOUT: none

**Proposed under every option, for your time** (proposals; your ruling makes them so):
- Two cards per trial (a new design under B or C adds two more), and 5 short reads per look of pieces shown to you unlabelled, so you see the work itself.
- At most 3 entry cards wait on you at once; the next waits in a queue the desk shows. Results cards are never held back, and reach you within two weeks of a trial being judged.
- How many methods the screening will bring, and how long a card takes you, are not known yet. Your hours are not recorded, so each status update counts cards waiting and answered, with the spend.

## Context
- The owner's answers to the value-target question: parts 1, 2 and 4 ruled; part 3 answered with this design, in their words, with its reason (source: intake/P-002-owner-value-target-answers-2026-11-10.md)
- The definitions and trial design this card builds on, as passed by the Critic at round 3 (source: questions/P-002-value-target.md at commit 5995412, kept in history once that question closes; reviews/P-002-value-target/critic.md)
- The odds at the 1 in 10 line: one look 0.71 and 0.42, two looks 0.92 and 0.70, trials going on to a second look 0.27 to 0.48, the hold-up checks failing a harmless method 0.145 with one look and up to 0.20 with two (source: intake/P-002-value-target-odds-2026-11-10.md, rounds 2 and 3)
- "Killed, not tuned", quoted (source: Personal-Org-Operating-Model docs/archive/OPERATING_MODEL_v2.5.1.md, principle 4, which OPERATING_MODEL.md §1 item 4 keeps "Unchanged")
- Null results are results; no re-running for a better answer; repeated reframing goes back to Discovery (source: Personal-Org-Operating-Model OPERATING_MODEL.md, "The experiment playbook (D-047)")
- Rule changes are the owner's to make (source: Personal-Org-Operating-Model OPERATING_MODEL.md §2, "Never delegable: … rule changes")
- The desk is never updated automatically (source: decisions/questions/P-002-groundwork-shortlist.md, answer 5)
- The pre-mortem's risks on adopting what is popular, "not shown" methods, methods landing in the model, and the owner flooded (source: docs/projects/P-002.md section 7, R1, R9, R16, R18)
- The Critic's rounds 1 and 2 (source: reviews/P-002-trial-gates/critic.md)
