Verdict: PASS

*The Source checker's deciding check of the Q-014 library entries, as the owner ruled (decisions/questions/P-002-research-stop-2.md): one check of every filed entry against its source, the memo set aside. A fresh session on a different model from the Researcher, brief 192 (docs/briefs/192-source-checker.md). Recorded verbatim by the Orchestrator (session_01QBwHGNSLmSrYQgS6BPjV8p) from the helper's return, 2026-11-09.*

All 21 facts and 3 patterns were checked against sources opened in this session. None was removed. 11 were reworded, and 13 hold as written apart from edits that apply to all 24: memo-referring notes removed, checked-on date set to 2026-11-09, and an "opened by" line added for this session. Every README row matches its entry.

Sources opened and how:
- Fetched directly: the NAO web page and PDF, the Haycock ISPOR page, the York release, the Pharmaceutical Journal page, the Cochrane abstract, AJMC, ISO/TC 211, RFC 4450, PEP 1, Zalando, Kubernetes, ICH Q12, Medicines Australia, the EuroScan PDF and the Laughland PDF.
- Han Siong PDF: read from the file the fetch tool saved.
- PubMed abstract, Leggett and Niven: read through NCBI E-utilities, not the web pages (PubMed web page needs cookies; PMC pages came back as stubs).
- EuroScan Figure 1 (5 agencies for "removal of obsolete technologies") was read from the rendered page image.
- No earlier-record quote was used in place of opening a page.

| id | source opened | result | reason |
|---|---|---|---|
| Q-014-1 | aidic.it PDF (Han Siong) | holds; memo note removed | 9.1%, 149 of 1,633, 630 cases, 1990-2015, sixth rank, "not decreasing" all confirmed; the 9.1% base is already stated as cause attributions |
| Q-014-2 | same PDF | holds | typology shares 45.6, 30.9, 10.1, 8.1, 5.4, the Flixborough sentence, time-constraint and bypass passages, and the "competent personnel" sentence all confirmed |
| Q-014-3 | icheme.org PDF (Laughland) | reworded | figures confirmed (9% of citations, 92 MOC citations, 39 = 42%, 2007-2011). "ABB sells audits" replaced by what the paper says: ABB conducts MoC audits and gap analyses |
| Q-014-4 | same PDF | reworded | the paper calls these lists "A summary of the findings", worded as actions. The entry called them "recommendations" and said they "imply" gaps. Retitled and rewritten to say only that; memo note removed |
| Q-014-5 | same PDF | holds | all quotes confirmed; the bypass wording is a concern, not a rate |
| Q-014-6 | NAO web page and report PDF | holds | £968m, 15% and 48% overspend, 35% combined, "not possible to evaluate", and the "not designed to assess value for money" line (found in the PDF, not on the web page) |
| Q-014-7 | PubMed abstract via E-utilities; Pharmaceutical Journal page | reworded | abstract numbers confirmed (47 indications, 9 (18%) ESMO, 26 (55%) NICE rejections). The news page does name Richard Sullivan, so "names no author" was corrected |
| Q-014-8 | ISPOR abstract page | reworded | quotes and counts confirmed. "Consultancy serves pharmaceutical clients" is not on the page; now says authors are at Costello Medical and funding is not stated |
| Q-014-9 | York release | reworded | £18,317 and 4,367 QALYs confirmed. The release says "likely to fall", not "may fall", and calls the figure "likely to be an overestimate"; added the "up to £80 million" context and removed the memo reading |
| Q-014-10 | PMC3542085 via E-utilities (Leggett) | holds; memo note removed | barrier quotes, 54% and 50% advisory figures, the nine interviewees and the one-interviewee 50% acceptance estimate all confirmed |
| Q-014-11 | Cochrane abstract | holds | 65 reviews, 43%, and both quotes confirmed |
| Q-014-12 | PMC4596285 via E-utilities (Niven) | holds | 109 papers, "greatest likelihood", the Chamberlain do-not-do result in one included study, the sustainability-plan passage and the citation-count mismatch all confirmed |
| Q-014-13 | AJMC page | holds | 7 of 70 services, 2 declined, 3 flat, 2 rose, data to Q3 2013, Anthem VP lead author |
| Q-014-14 | EuroScan PDF | holds | 15 of 17 responded, 5 agencies named removal of obsolete technologies (Figure 1), 7 of 15 under 2 FTE, criteria themes, no conflicts reported |
| Q-014-15 | ISO/TC 211 page | reworded | 5 and 3 years, the vote options, the 8-week ballot and the confirm-a-TS-once recommendation are confirmed. "Not binding" applies only to the planning group's guidance in meeting reports. Added the site disclaimer (content managed by a third party, accuracy not guaranteed by ISO). "Edited 2022-07-27" is the last change-log entry |
| Q-014-16 | RFC 4450 text | holds | "never been followed", the 2004-05 experiment, "some 125" documents, 44 listed versus 61 in the text |
| Q-014-17 | PEP 1 | holds; memo note removed | all quotes confirmed; page last modified 2026-11 |
| Q-014-18 | Zalando post | holds | one reference to the input reader's finding number (F014-27) reworded |
| Q-014-19 | Kubernetes page | reworded | rule 4a text confirmed. Page re-read in full, so "partly read" is dropped. Added that it covers API versions only and the #52185 exception |
| Q-014-20 | ICH Q12 concept paper PDF | reworded | quotes and dates confirmed. "Industry benefits from lighter change control" was not in the source; replaced by the paper's own "benefit industry, regulators and patients". Memo note removed |
| Q-014-21 | Medicines Australia PDF | reworded | quote confirmed. "Wants faster access for its members' products" replaced by what the paper argues (accelerating patient access). Memo note removed |
| P22 | its origin facts Q-014-2 and Q-014-4 | reworded | origin text follows the reworded -4; the pattern is marked as opinion beyond its origins; memo note removed |
| P23 | its origin facts Q-014-12 and Q-014-13 | reworded | origin entries confirmed; marked as opinion beyond them; memo note removed |
| P24 | its origin fact Q-014-8 | reworded | origin confirmed; stake wording matched to Q-014-8; memo-based notes removed |

Commit: on branch build/source-checker/q-014 in /home/user/lib-q-014, one commit "Source-check Q-014 library entries against their sources", author source-checker <source-checker@agents.invalid>. It touches README.md, the 21 facts and the 3 patterns, and the worktree is clean. The last paragraph is exactly:
Agent-Session: session_01QBwHGNSLmSrYQgS6BPjV8p/source-checker-192
Spec: none (library filing from research Q-014, P-002)
Not pushed. The commit message carries no Co-Authored-By or Claude-Session lines.

Still open (none blocks PASS):
- All 21 facts are single-source and stay not load-bearing, as their status lines already say.
- Q-014-13 and Q-014-7 rest partly on news pages. For Q-014-13 the JAMA paper was not opened. For Q-014-7 the abstract was opened, so the figures stand on the abstract.
- The Gambetti 80% claim (in Q-014-1) and the OSHA and NPRA tables behind Q-014-3 were not opened; the entries already say so.
- The shelf-life question remains an owner call.
- I cannot see my total token count.
