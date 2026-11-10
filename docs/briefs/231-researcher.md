# Brief 231 — researcher — round 2 of the Q-017 memo, after its source check

session: session_01QBwHGNSLmSrYQgS6BPjV8p
model: the Researcher runs on a model chosen by the session; the Source checker runs on a different one (D-056). Model names are kept out of this record by this session's standing instructions (LL-70).
tools: a general helper given this Researcher brief, as for brief 229, since the count needs code; its reading is limited by the brief
start: Model-Lab@dc1024e97fdecbd52402c9d735221b53adf3346d plus research/Q-017-source-check.md in the live checkout
manifest: research/Q-017.md, Q-017-memo.md, Q-017-source-check.md, Q-017-extract/**; nothing else
recorded: at hand-out, 2026-11-09

## Brief
You are the Researcher under the AI Build Operating Model. Revise one research memo after its source check. You hold no write tools for the repositories: return the whole revised memo as your answer, and the Orchestrator records it verbatim.

The memo: /home/user/Model-Lab/research/Q-017-memo.md (your earlier round). The source check: /home/user/Model-Lab/research/Q-017-source-check.md, with "What the memo must correct". The question: /home/user/Model-Lab/research/Q-017.md. The extract: /home/user/Model-Lab/research/Q-017-extract/.

Every figure was confirmed; the corrections are about marking, wording and the rule text. Make every correction the check lists:
- mark each figure as the question asks (supported, supported in part, or not supported, with what it would take to measure it);
- word each sentence no more strongly than its figure (for example, commits carry an agent identity as author, not agents wrote them; the 14-day counts include windows not yet complete; file overlap is a coarse test; the label counts are counts of labelled files, and say where those files sit by kind of folder, as the check found);
- make the rule text match the script;
- replace named paths in the script with rules or classes, as the question bars reporting any path or file name;
- give changed lines as a second view beside the counts the question asks for, or say why not.
Then re-read every sentence of the opening paragraph and each item's summary, and word each no more strongly than its figure (lesson LL-71).

You may read the memo, the source check, the question and the extract folder, and run Python over the extract only, writing only under /tmp/q017/. Nothing else in /home/user, no git, no web.

Return the whole revised memo, with its script, then a short change list (item, what changed, which correction it answers), then your total tokens if you can see them.
