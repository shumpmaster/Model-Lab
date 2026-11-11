# The screening's trial terms: what the owner ruled, and what is only proposed

*Written by the Chief of Staff, 2026-11-11, before the Design gate case, as LL-79's correction and Triage's root cause ask (docs/LESSONS.md LL-79; triage/P-002-brief-round-3.md, section 3): one list of every trial term, each marked ruled or proposed, from the owner's rulings and the two cards as put. It changes no ruling and no line of the brief; it is what the gate case cites when it asks the owner to rule the proposals. Revised after the gate Critic's view of case 1 (reviews/P-002/_design-gate-1-critic.md, the list's findings 1 to 6): T4, T16 and T20 narrowed or marked to confirm, T25 and T29 completed, and T32 to T34 added.*

## What this means for you

Every term of how a method is tried and kept is listed once below, marked either ruled by you or only proposed. Thirty-four are ruled. Twelve of those are ruled only in the sense that they were in the text of the cards you answered but not in the words of your answer, so the gate asks you to confirm them; the brief already treats them as ruled. Twenty are proposals, seventeen from your cards and three of the Chief of Staff's own, and the Design gate asks you to rule each. Two places where the cards disagree with each other are named at the end. Nothing here is irreversible.

## How each term is marked

- **Ruled**: in the words of the owner's answer, in the ruling line of its record, or in the text of the option the owner chose, which that record says was ruled.
- **Ruled, confirm**: in the text the owner answered (a card's words, its "under every option" lines or its limits), but not in the owner's words, the ruling line, or the record's account of what was ruled. The brief treats it as ruled; the gate asks the owner to confirm it.
  One exception: the stop after a failed first look (P6) is in the trial-gates card's "under every option" lines but in the value-target card's proposals; it is marked proposed, the stricter of the two (the first difference, below).
- **Proposed, card**: on a card under "Proposed under every option ... (proposals; your ruling makes them so)", which the value-target record says are "not yet ruled one by one" and go to the Design gate.
- **Proposed, Chief of Staff**: on neither card; the Chief of Staff's own design.

## The records

- The value-target card as put: questions/P-002-value-target.md at commit 964da47 (here **VT card**); the owner's answers and the ruling: decisions/questions/P-002-value-target.md (**VT record**).
- The trial-gates card as put: questions/P-002-trial-gates.md at commit 3ae1268 (**TG card**); the owner's answer and the ruling: decisions/questions/P-002-trial-gates.md (**TG record**).
- The owner's earlier answers: decisions/questions/P-002-groundwork-shortlist.md (**shortlist record**).
- How the session put each card, in the owner's question tool: intake/P-002-owner-value-target-answers-2026-11-10.md and intake/P-002-owner-trial-gates-answer-2026-11-11.md. These hold the owner's words and the short form the tool showed, not the cards' full proposals lists, which only the two card files hold.

## Ruled

| # | Term | Mark | Where |
|---|---|---|---|
| T1 | A **piece** is a merged pull request, in any of the three repositories, that changes built work, a plan or research; one that only files or answers a question, or only adds records, is not a piece | Ruled | VT card, "Words used below", which part 1's option A uses; VT record, ruling line ("pieces of work") |
| T2 | A **touch** is a time the owner stepped in on a piece before it merged: a question about it, a fix the owner made, or a send-back; merging is not a touch | Ruled | As T1 |
| T3 | The measure: the share of pieces needing at least one touch before merging | Ruled | VT record, part 1, "Halve share needing you (Recommended)"; VT card, part 1, option A |
| T4 | The target: over the latest 60 pieces, at most half the starting figure counted over the 60 pieces before the first trial, the fall clearing chance at 1 in 10, with the work holding up | Ruled | VT record, parts 1 and 2; VT card, part 1, option A's line |
| T5 | The target is checked 12 months after the first trial starts | Ruled | VT record, "What was put" (part 1's question named it); VT card, part 1, option A's line |
| T6 | A miss comes back to the owner to re-aim the screening or close it | Ruled | VT record, "What was put" |
| T7 | The keep line: a method is kept only if chance alone would give its fall at most 1 time in 10 | Ruled | VT record, part 2, "1 in 10 (catch more)" |
| T8 | To be tried, a method needs one source someone else has opened and confirmed | Ruled | VT record, part 4, "One source is enough (Recommended)" |
| T9 | Before a trial, the method's conditions are read against ours, and clear misfits are not tried | Ruled | VT card, part 4, option A; VT record, "How it is carried out" |
| T10 | Before a trial, any outside code, prompt or skill is checked before it runs, with no data out | Ruled | VT card, part 4, option A; VT record, "How it is carried out"; shortlist record, answer 6 ("Yes, no data out") |
| T11 | The lighter evidence standard (T8) goes to the operating model as a proposal at the end of the cycle | Ruled | VT card, part 4, option A and WHY; VT record, "How it is carried out" |
| T12 | Every method comes to the owner first on a plain-English **entry card**, saying what the change would be, how it is done today, why, and its impact and risks; nothing is tried without the owner's approval | Ruled | TG record, ruling line; the owner's words in the VT record, part 3 |
| T13 | After its trial, a **results card**, in more detail, like a gate card, comes to the owner, who approves or rejects putting the method into the operating model on any result, passed or not | Ruled | TG record, ruling line and the owner's words, "I decide every result (Recommended)"; TG card, option A |
| T14 | Nothing is dropped automatically; every result comes to the owner | Ruled | TG record, ruling line; TG card, "Under every option" |
| T15 | Two looks are planned per trial | Ruled | TG record, ruling line |
| T16 | The second look: if the first look leaned the right way (the method's pieces needed the owner less often) but did not pass, 30 more pieces each way are assigned, and all are judged together on a slightly stricter line, so that a useless method passes about as often as at one look (the card said "no more often"; the independent run found up to about 0.106, which P18 addresses); it is planned before the trial starts, so it is one trial, not a re-run | Ruled, confirm | TG card, the paragraph after the odds table; the ruling line holds only "two looks planned per trial" (T15); reviews/P-002-value-target-odds/reviewer.md |
| T17 | A method the owner approves enters the operating model only through the model's own change process, which the owner also rules; nothing enters the Service Desk automatically | Ruled | TG card, option A; TG record, "How it is carried out"; shortlist record, answer 5 |
| T18 | Adopting a method whose trial did not pass goes against "Killed, not tuned", and that departure goes to the operating model as a proposal | Ruled | TG card, WHY; TG record, "How it is carried out" |
| T19 | Every results card says plainly when a method was not passed and why, including when its work did worse | Ruled | TG card, option A; TG record, "How it is carried out" |
| T20 | The log of touches and reopenings is specced in Design and built only after the Design gate | Ruled | VT record, "How it is carried out"; VT card, "What must be built" |
| T21 | No trial runs before the Design gate | Ruled | VT record, "How it is carried out" |
| T22 | The spend and owner-time ceilings are set at the Design gate | Ruled | shortlist record, answer 8, "Set at Design gate" |
| T23 | A trial: each new piece of one kind is assigned, before work on it starts, to "with the method" or "without", by shuffled draws, so each side gets 30, in the same weeks | Ruled, confirm | VT card, "Words used below"; TG card, "Words" |
| T24 | A trial is **passed** when the method's pieces needed the owner less often by more than chance at 1 in 10, and its work held up; anything else is not passed | Ruled, confirm | TG card, "Words" |
| T25 | **Holds up**, for a trial: the method's pieces do no worse, by more than chance at 1 in 10, at passing their first independent check and at not being reopened for a fault within 30 days; a reopening is marked by the reviewer of the later change, not the piece's maker | Ruled, confirm | VT card, "Words used below" (the same paragraph holds the five-piece unlabelled sample, P14, a proposal) |
| T26 | Every trial piece still passes all its usual checks and the owner's merge, and can be undone | Ruled, confirm | VT card, "Words used below" |
| T27 | The entry card says what the first assessment rests on, and carries the trial's plan, which is then fixed | Ruled, confirm | TG card, "Under every option", marked "Added by the Chief of Staff"; not in the ruling line (the brief's round 4, finding 2) |
| T28 | The results card carries the Critic's view and a recommendation | Ruled, confirm | TG card, "Under every option", marked "Added"; the Critic's view, but not the recommendation, is in the TG record, "How it is carried out" (the brief's round 4, finding 2) |
| T29 | Each piece's draw is recorded in the log, and each trial's result is worked out by the Reviewer, not by whoever ran it; questions put to the owner in conversation are logged by hand by the Chief of Staff, so only the owner's sample is unlabelled | Ruled, confirm | VT card, "Limits of this design", "Not blind" |
| T30 | Only a method that can be switched on and off piece by piece fits this trial; how to try any other is left to that method's own trial plan, which would say it is weaker | Ruled, confirm | VT card, "Limits of this design" |
| T31 | The two cards per method are the two approvals; each trial adds one entry card and one results card to the owner's time | Ruled | TG record, ruling line; the TG card's "Two cards per trial" line, under its proposals, describes their cost, not a choice (the brief's round 4, finding 1) |
| T32 | **Holding up, for the target**: the latest 60 pieces do no worse than the starting 60, by more than chance at 1 in 10, at passing their first independent check and at not being reopened for a fault within 30 days; the starting figure counts all kinds of work together | Ruled, confirm | VT card, part 1, the sentences before the options; option A's line says only "with the work holding up" |
| T33 | The log reads records and changes nothing in the prompt engine's work | Ruled, confirm | VT card, "What must be built" |
| T34 | The target is reversible until the first trial starts; after that a change discards the starting count and is a new target | Ruled, confirm | VT card, part 1, "Reversible" |

## Proposed, for the owner to rule at the Design gate

| # | Term | Mark | Where |
|---|---|---|---|
| P1 | Each trial is judged 30 days after its last piece | Proposed, card | VT card, proposals, "Date" (also in its "Holds up" words) |
| P2 | The target is also checked at each screening review after the 12-month check | Proposed, card | VT card, proposals, "Date" |
| P3 | On a miss, kept methods stay only on their own results; none is adjusted to pass | Proposed, card | VT card, proposals, "Miss" |
| P4 | After the first five trials a summary comes to the owner, who rules whether to go on | Proposed, card | VT card, proposals |
| P5 | Stop and come back to the owner if the starting count shows fewer than 6 of 60 pieces needed them | Proposed, card | VT card, proposals |
| P6 | Stop a trial at once if its first look fails the hold-up checks (the second look then does not run, and the result comes to the owner) | Proposed, card | VT card, proposals; the TG card also has it under "Under every option", marked "Added" (see the first difference, below) |
| P7 | Stop a trial at once if it breaks work the owner relies on | Proposed, card | VT card, proposals |
| P8 | A change of AI model during a trial voids it | Proposed, card | VT card, proposals |
| P9 | Every kept method gets a review date six months on, and a way to remove it | Proposed, card | VT card, proposals |
| P10 | A change of AI model triggers a re-check of the methods kept under the old one | Proposed, card | VT card, proposals |
| P11 | One method per kind of work at a time | Proposed, card | VT card, proposals, "Apart from the prompt engine" |
| P12 | No method that could change how often work passes its first check is tried on a kind of work while the prompt engine is testing that kind or counting its 30 real-use pieces | Proposed, card | VT card, proposals, "Apart from the prompt engine" |
| P13 | The Design gate rules whether any trial may start before the prompt engine finishes | Proposed, card | VT card, proposals; the brief's pre-mortem R15 |
| P14 | The owner reads 5 pieces per look, at random and unlabelled; one the owner would not have accepted counts as reopened | Proposed, card | TG card, proposals ("5 short reads per look"); the VT card puts "5 of each trial's pieces" in its "Holds up" words and "5 short reads" per trial in its proposals (see the second difference, below) |
| P15 | At most 3 entry cards wait on the owner at once; the next waits in a queue the desk shows | Proposed, card | TG card, proposals |
| P16 | Results cards are never held back, reach the owner within two weeks of a trial being judged, and never outnumber the entry cards approved | Proposed, card | TG card, proposals |
| P17 | Each status update reports touches, and counts cards waiting and answered, with the spend | Proposed, card | VT card, proposals, "Your time"; TG card, proposals |
| P18 | The two-look line is set in the trial design so that it stays at most 1 in 10 at every starting share, or is kept at about 1 in 10 as now (0.093 and 0.099 at the two shares computed, up to about 0.106 at others) | Proposed, Chief of Staff | intake/P-002-value-target-odds-2026-11-10.md, round 4; reviews/P-002-value-target-odds/reviewer.md |
| P19 | No method enters the operating model while the prompt engine is testing or counting the kind of work it changes, unless the owner rules otherwise for that method on its results card | Proposed, Chief of Staff | the brief, sections 3 and 8 (docs/LESSONS.md LL-78) |
| P20 | No trial runs before the trial design (M9) is frozen, the starting count (M11) is on record and the owner has set the ceilings | Proposed, Chief of Staff | the brief, section 3, "Dependencies" |

The brief's last bullet of section 6 lists P1, P4 to P12 and P14 to P16 (with the two cards of T31), and P18 and P19; P13 is in its sections 7 (R15) and 8; P2, P3 and P17 are on the cards but not in the brief; and P20 is in its section 3. The brief also proposes, outside the trial terms, the fallbacks for the open unknowns U1 to U5 (section 7), which the gate asks the owner to accept one by one, and a tier question if three or more of the project's agents would run at once (section 5).

## Two places where the cards differ

1. **Stopping after a failed first look (P6).** The TG card puts it under "Under every option", which option A carries, marked "Added by the Chief of Staff"; the VT card puts it in its proposals. The brief lists it as proposed. The gate asks the owner to rule it with the other proposals.
2. **The owner's short reads (P14).** The VT card puts 5 unlabelled pieces per trial inside its definition of "holds up", and 5 short reads per trial in its proposals; the TG card proposes 5 per look, which is 10 for a trial that takes its second look. Both are proposals at most, as Triage found (triage/P-002-brief-round-3.md, section 4). The gate asks the owner which, if either.

## Two figures on the cards since corrected

The cards' figures were worked out by the Chief of Staff; the independent run corrected two of them in the brief and the odds record, not on the cards (reviews/P-002-value-target-odds/reviewer.md, round 1, findings 2 and 4):
1. The value-target card says a true halving shows on the count "about 4 to 5 times in 10"; at the 1 in 10 line the owner chose, it is about 5 in 10 (0.53 and 0.54).
2. Both cards say the held-up checks turn away a harmless method "up to 1 in 5" with two looks; the worst pair of starting shares gives 0.22.

