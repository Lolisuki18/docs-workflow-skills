# BM02 - SRS/SDD Self-Review Report (Review 2) - form structure

Header line: `SWP490 · CAPSTONE PROJECT · REVIEW 2 · BM02`. Title: `SRS/SDD Self-Review Report – Review 2`.
Rules in the form: run the standard prompt on the proposed final registration form and the repository at tag `review-2`. **Keep every finding exactly as produced by the AI; add only the Team response column.** Export to PDF. File name `SWP490_<ProjectCode>_R2_SelfReview.pdf`.

This skill packages; it does not produce or alter findings. The run itself is done with `docs-sync-auditor` (BM02 Standard Mode) or by the team's own agent.

## 1. Run Information
| Field | Value |
|---|---|
| Project code | |
| Project name | |
| Team | |
| Supervisor | |
| AI tool and model | |
| Run date | |
| Repository tag / commit | |
| Registration form version used | |
| Version | |
| Date | |

Fill `Repository tag / commit` from git (`git rev-parse HEAD`, `git tag --points-at HEAD`). AI tool/model and run date from the actual run; unknown -> `[Cần bổ sung]`.

## 2. Standard Prompt
Insert the prompt **verbatim** from `docs-sync-auditor/references/bm02-standard-prompt.md` (between the BEGIN/END markers). Do not modify it.

## 3. Findings and Team Response
Team response: `Fixed (link to commit)` · `Kept (reason)` · `Planned (owner and due date)`. Do not delete any finding.
| ID | Category | Location | Finding | Severity | Evidence | Team response |
|---|---|---|---|---|---|---|
- ID, Category, Location, Finding, Severity, Evidence = AI output, unchanged (IDs `SR-01`...).
- Team response = team's decision. Suggested wording is a draft only when requested.
- Example row in the form (`SR-01 | Data | SDD §4 ERD | Entity Voucher used in code but missing from ERD | High | Voucher.java | Fixed – commit a1b2c3d`) is an illustration; delete it.

## 4. Top 5 Findings (as reported by the AI)
| # | Finding ID | Summary |
|---|---|---|
Copy the AI's own top-5 list.

## 5. Summary
| Severity | Total | Fixed | Kept | Planned |
|---|---|---|---|---|
| High | | | | |
| Medium | | | | |
| Low | | | | |
Counts are computed from section 3 rows. `Total = Fixed + Kept + Planned` unless a row has no response yet (report as incomplete).

Every High finding marked Kept or Planned must also appear in BM01 section 5 (Known Gaps).

## Packaging checks
- [ ] Section 3 rows are byte-identical to the AI output apart from the added Team response column.
- [ ] Every row has a Team response.
- [ ] Section 5 counts match section 3.
- [ ] High + Kept/Planned list handed to BM01 section 5 (cross-check X1).
- [ ] Run metadata complete; tag/commit is `review-2`.
