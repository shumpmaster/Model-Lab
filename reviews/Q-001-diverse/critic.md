Verdict: FAIL

The Critic's neutral-phrasing check of research question Q-001, re-run on a different model from the question's writer after L-0002, verbatim. Recorded by the orchestrator. Session: session_01QBwHGJH9m3A4Ray7WpHzBo, 2026-11-01. The groundwork map had already been made from the question; how these findings are carried is in docs/LEDGER.md, L-0003.

## Round 1 (model-diverse)
Verdict: FAIL

The question is close to passing. It meets the form and opens correctly, but it has one real neutrality problem and some gaps. I checked only Q-001.md against _QUESTION.md and _GROUNDWORK.md. OPERATING_MODEL.md §4–§6 are not quoted below. A grep of the file for section headings returned no match, and I read only lines 244 and 288 as hits.

**Form check (passes)**
- It has the three required sections, the `topics:` line and the `depth:` line, in the right order.
- The question text begins "Groundwork map:", so the Researcher will produce a groundwork map.
- Depth 3 is allowed. The "(groundwork map; known items graded and sourced)" gloss matches the groundwork form.

**Findings**

1. **Neutrality, the one real problem: the framing presumes instructions are the thing to change.**
   - "before deciding whether and how these instructions should be changed, observed or measured" does include "whether". But the surrounding framing is "instruction quality", "writing, running and measuring instructions", and "the risks of changing instructions".
   - "What each answer would change" says "Each area found to be unknown becomes a research request or a registered experiment". That implies every unknown leads to more work, and it leaves out "leave it alone".
   - The line "including leaving things as they are" is in the baseline bullet only. Change to: "…including the option of changing nothing, and the case that the instructions are not the limiting factor."
   - In the "What each answer would change" section, add the possibility that an area is found not worth pursuing or already known. For example: "…becomes a research request or a registered experiment, or is set aside as not worth the cost".

2. **Neutrality, minor: a risk-only bullet and an unbalanced benefits bullet.**
   - "the risks of changing instructions in response to individual failures, including growth, conflict between rules, and fitting to the checks rather than the goal" lists only downsides, and it names the downsides specifically. The benefit side is absent.
   - Suggested wording: "the benefits and risks of changing instructions in response to individual failures (for example, what is gained, and growth, conflict between rules, fitting to the checks)".
   - The same applies to "including where written procedure was found to help little or to harm". Add "as well as where it was found to help".
   - This is the clearest hint of a leaning in the document. It reads as skeptical of written procedure.

3. **Neutrality: unattributed pipeline detail.**
   - The description, "Independent checkers then review the work, and failed work goes back for another round with the checker's findings", is factual.
   - "pipeline of AI agents under one human owner" reads as neutral. I found nothing else that states a hoped-for answer or a preferred solution, and nothing that names an owner's leaning.
   - The "shumpmaster/…" repository paths point the Researcher at the owner's own system. That is acceptable as inputs. The text should say it is to be treated as the subject under study, not as evidence of what works.

4. **Gap: alternatives to written instructions.**
   - The first bullet compares the instructions against model, inputs, task split and checks. The scope never asks about non-instruction levers as alternatives: tooling, retrieval or context design, or changing the number of checkers or rounds.
   - Add to bullet 1: "…and what other levers (tooling, context design, checker count or rounds) would address the same failures".

5. **Gap: what counts as "good work" and the ground truth for it.**
   - Bullet 2 asks how quality can be measured, but no bullet asks how to define "good work" or who judges it. Checkers are themselves model-run, so the measurement could be circular. A rater or the owner as judge, rater agreement, and the reliability of the checkers as a measuring instrument all belong in the scope.
   - Add: "how 'good work' is defined and judged, and how reliable the checkers are as a yardstick".

6. **Gap: how the instruction text itself is built.**
   - The scope has nothing on instruction design: length, structure, examples, specificity, and tone. An expert would expect this under the heading of what determines output quality.
   - Add it, or state that it is out of scope. Nothing says anything is out of scope. The scope has no "not in scope" statement, which makes the map open-ended against its owner-shortlist limit of 8.

7. **Gap: other agent-specific areas.**
   - Handoff failures: information lost between roles, and whether a role sees what it should (the visibility rules). The "must not see" and context-pack design is named in the description but is not a bullet to map.
   - Security and manipulation: instructions that can be overridden by content in the inputs (injection), or that agents might ignore, game, or follow too literally.
   - The existing reviews' own failure modes are only half covered by "how this interacts with the pipeline's existing reviews and checks".

8. **Minor form point: the "decision it serves".**
   - "The shape of the Discovery for this project: which questions go to the owner, which go to research, and which need an experiment" is a decision about process, but "this project" is not named. The reader has to guess which project. Name it, for example "the Discovery of <project>".
   - It also never says what the value target is, although it mentions "its value target, scope and plan". A cold reader cannot tell what is being decided.

**What I would not change**
- The bullet on kinds of task and the bullet on owner time are fine as written. They name both the owner's decisions and the cost.

Once findings 1 and 2 are fixed it passes on neutrality. Findings 4 to 7 are gaps the Researcher might be expected to cover without prompting, so I have not made them failures on their own. Finding 8 and the missing out-of-scope statement are form and clarity issues.
