# The second Critic's check of every later_work code (brief 330)

*Recorded verbatim by the Orchestrator. Brief 330 (docs/briefs/330-critic.md), on Model-Lab@48fee4a, the codes of reviews/Q-018-later-work/_critic-coder-verbatim.md against records pack q018-pack-323. By S-002 step 3, *Later work*, the two codes not confirmed (rows 60 and 61, Personal-Org-Operating-Model #49) are taken as "not said", and listed for the owner with both readings.*

Confirmed: 129 of 131

| Row | Label | Commit | Coder's code | My code | Reason |
|---|---|---|---|---|---|
| 60 | de17627b | 568cd6e0 | later work | this piece | The piece's own commits draft and plan-review S-037. The record asks the owner to approve that draft. |
| 61 | de17627b | 0e57b841 | later work | this piece | The same approval of S-037's plan, which this piece drafted. The added line only rewords option A. |

**Why rows 60 and 61 differ.** Personal-Org-Operating-Model #49's `Spec:` trailers give only S-036, so the coder read Q-031 as being about other work. But #49's own commits also write S-037: drafts 1 and 2 of specs/S-037-short-history.md, plan review rounds 1 and 2, and S-037's lesson. Q-031 asks the owner to approve that draft "as reviewed (draft 2…)", and its option B sends the draft back to plan review. Step 3 says a ruling on a spec "whose work the piece carries" reads as being about the piece. That is the same reason row 41 (Q-024 on S-033 in #35) is coded "this piece". The freeze and the build do come after the piece lands, so "later work" can be argued. Under S-002 step 3, a code I do not confirm is taken as "not said". These two rows therefore count on #49 and go to the owner with both readings. Service-Desk #237's picture questions (rows 28 to 31) are a different case and I confirm them. The pictures are records-class files that #237 adds, not plan work it carries. The context of the owner's ruling (decisions/questions/P-002-later-work-questions.md) also says #237 "only files them".

**Answers to the coder's three questions**

1. **An append is coded from the lines its commit adds.** I agree. "What a touch is" reads "each later commit's added lines as that commit adds them". It also says the record as first added, and the appends before the one that names the piece, are not read for it. RT1(a) counts each append as one more question, and the later-work reading is made "for each question RT1(a) would count (a record's first add or an append …)". I read surrounding text only to make sense of a reworded line. This answer moves no rows. Rows 93 to 96 and 98 to 99 would not move under the whole-record reading either: the only earlier text about S-022 is the relayed line in section C.4, which holds none of the owner's words and asks nothing.

2. **A line that only relays an earlier decision on the piece's spec, or names it as the next step, does not ask about the piece.** I agree. S-002's test is a part that "asks about the piece under way". A relay or a next-step mention asks nothing.
   - Rows 70 and 74: S-025 appears only in the option text ("then S-025", "Then I revise S-025").
   - Rows 92 and 97: S-022 appears only in "Earlier decisions that still stand", which is not marked as the owner's words.
   - Row 71 is the closest case. Its option text says S-025 "keeps going … in parallel and lands after", which states no change to S-025, so it asks about the joint S-023/S-024 build.

   This answer moves no rows.

3. **A notes file is coded from its own words (row 35).** I agree. S-002 reads whether a question asks for later work "from its record's own words", and a notes file is its own record. RT1(a) also leaves out every file ending `-notes.md`, so row 35's code changes no count; it stays "not said" and is listed. Row 124 is also a notes file, coded from its own words, which is consistent. This answer moves no rows.

**Changed (by file):** nothing. I am read only and wrote no file.

**Why:** brief 330 asks a second, fresh Critic to check every one of the 131 `later_work` codes against the records pack (S-002 step 3, *Later work*; decisions/questions/P-002-later-work-coder.md).

**Verified:** by reading only; I ran no command.
- I read each of the 131 rows' records in `records2/` at the commit named, and every added line of each commit. That includes the redrafts the coder read only in part (rows 15 to 19, 126 to 128 and 130 to 131) and the full `asked:` lines of rows 86 and 87 (L-0135 and L-0136). The codes stand after that reading: row 86 is S-024's freeze and row 87 is S-025's.
- For each sampled piece I checked the pack's file list, commits, window, and its `Spec:` and brief widening line in the L<nn> file. That check is how I found that #49's own commits write S-037.

**Undone:** nothing in the brief. As the brief asks, I give no count of touches or pieces.

**Needed outside my surface:**
- The Orchestrator should record rows 60 and 61 as "not said", list them for the owner with both readings, and add the checked codes to the extract's `later_work` field.

**Open questions:**
1. Does a plan-approval question count as being about a piece when the piece's own commits wrote the plan but its `Spec:` trailers name a different spec? Rows 60 and 61 turn on this. A ruling would settle similar cases in the live count.

No finding here touches an earlier check of mine. This is a fresh session, and I made no earlier check of these codes.

Files read:
- /home/user/Model-Lab/AGENTS.md
- /home/user/Model-Lab/docs/briefs/330-critic.md
- /home/user/Model-Lab/specs/S-002.md ("What a touch is", RT1 to RT7, steps 3 to 5)
- /home/user/Model-Lab/decisions/questions/P-002-later-work-questions.md
- /home/user/Model-Lab/decisions/questions/P-002-later-work-coder.md
- /home/user/Model-Lab/reviews/Q-018-later-work/_critic-coder-verbatim.md
- In /tmp/claude-0/-home-user/3bf22eb7-3034-5300-9273-72fad23a7eb4/scratchpad/q018-pack-323:
  - INDEX.md and CODING.md
  - the L<nn> files of the 24 coded pieces
  - their records under records2/
