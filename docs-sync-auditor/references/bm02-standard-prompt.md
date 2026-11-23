# BM02 Standard Prompt (verbatim)

Source: "Hướng dẫn chuẩn bị Review 2" v1.0 (10/2026), section 05, and form BM02 section 2.
**Do not modify, translate, shorten or extend the text between the markers.** It is used exactly as issued by the course.

> Verification: the block below was compared programmatically against the prompt cell of `SWP490_R2_BM02_Self_Review_Report_1.docx` and is identical (only the trailing newline differs). If the course issues a new version, replace the block with the new official text from the BM02 `.docx` and bump the version line above.

<!-- BEGIN BM02 PROMPT -->
You are reviewing the SRS and SDD of a software capstone project against its
registration form and source code. Report only; do not change any file.

Inputs: the registration form, SRS, SDD (with diagrams), source code and
database script in this repository.

Check:
1. Scope: FRs in the SRS not covered by the registration form, and
   registration items with no FR.
2. Requirements: FRs without an actor or testable acceptance criteria;
   NFRs without metric, threshold and measurement method.
3. Data: entities missing from the Logical ERD; ERD entities or attributes
   missing from the database script, and tables not in the ERD.
4. States: for each main entity, states used in code but missing from its
   state machine; transitions with no triggering FR; states with no exit.
5. Flows: main business flows in activity diagrams with no implementation
   or no test.
6. Architecture: components or third-party services in code but not in the
   architecture diagram, and the reverse.
7. Design vs code: modules, APIs or business rules implemented differently
   from the SDD.

Output one table: ID | Category | Location | Finding | Severity
(High/Medium/Low) | Evidence. Then list the 5 most important findings.
If something cannot be verified from the repository, say so; do not guess.
<!-- END BM02 PROMPT -->

## Run requirements (from the guide)

1. Run with a coding agent that can read the whole repo, on the exact `review-2` tag, using the **proposed final registration form** as the scope baseline.
2. Paste the agent's **raw output** into BM02 section 3 without editing, deleting or reordering findings. Record AI tool and model, run date, repo tag/commit, registration form version.
3. Team adds only the `Team response` column: `Fixed (commit link)`, `Kept (reason)`, `Planned (owner, due date)`.
4. High findings with `Kept` or `Planned` must be copied to BM01 section 5 (Known Gaps).
5. Reviewers re-run the prompt on parts of the repo; trimmed or altered output counts as dishonest.

## Category names used in the table

`Scope`, `Requirements`, `Data`, `States`, `Flows`, `Architecture`, `Design vs code` (matching the 7 checks).

## Mapping to BM02 sections

| BM02 section | Content | Who fills |
|---|---|---|
| 1 Run Information | project, AI tool/model, run date, tag, form version, version, date | team |
| 2 Standard Prompt | the block above | unchanged |
| 3 Findings and Team Response | raw AI table + Team response | AI output + team |
| 4 Top 5 Findings | the AI's own top 5 | AI output |
| 5 Summary | counts by severity: Total / Fixed / Kept / Planned | computed from section 3 |
