# Evaluation Rubric for Report 3 (SRS) and Report 4 (SDD)

## Official weights (from the Student Guide and Evaluation Form)

| Criterion | On-going Assessment (supervisor) | Thesis Defence (committee) |
|---|---|---|
| Software Requirement (Report 3) | 16% | 15 (of 100) |
| Software Design (Report 4) | 18% | 10 (of 100) |
| Related: Testing (Report 5) | 18% | 10 |
| Related: Implementation | 32% | 35 |

Final mark = OGA x 50% + TDA x 50%, scale 0-10, one decimal place.

The per-criterion scoring detail is in the course syllabus ("Assessment Matrix" sheet), which was **not** among the provided files. `[Cần bổ sung: Assessment Matrix của Syllabus]` - this rubric therefore is a **self-check derived from the templates, the Review 2 guide and the BM02 standard prompt**, not the official marking sheet. Do not present it as official scores.

## How to run

For every item mark **Pass / Fail / Not verifiable**, add evidence (`doc:line` vs `code:line`), then list fixes. Do not assign numeric grades.

## A. Structure (both reports)
- [ ] Record of Changes table present with columns `Date | A*/M,D | In charge | Change Description`; this change has a row.
- [ ] All template headings present, in order, with template numbering. Non-applicable sections marked `N/A - reason`.
- [ ] No template sample rows or placeholder text (`<<...>>`, "Order a Meal", "Angular 7") left in.
- [ ] No unexplained acronyms; Definition/Acronyms consistent.

## B. Report 3 - SRS
- [ ] 2.1 every actor exists in code/spec; every use-case actor is in 2.1.
- [ ] 2.2.2 every use case has ID, actor(s), description; diagram matches the table.
- [ ] 3.1.2 each screen exists as a route/page; 3.1.3 matrix covers every screen in 3.1.2 and every role in 2.1.
- [ ] 3.1.5 ERD entities all appear in the entity table, and in the DB script.
- [ ] Each FR: actor, trigger, flow, validation, testable acceptance criteria (pass/fail wording).
- [ ] Each NFR: metric + threshold + measurement method.
- [ ] `BR-nn` and `MSGnn` are unique, referenced by FRs, and found in code/i18n.
- [ ] Traceability matrix: no FR without actor/UC; no UC without FR; no FR without entity (unless non-data) and API/screen.
- [ ] Scope: FRs not in the registration form are flagged; registration items with no FR are flagged.

## C. Report 4 - SDD
- [ ] 1.1 architecture diagram lists every component and third-party service found in code, and nothing absent from code.
- [ ] 2 Logical ERD, table list and DB script agree (tables, columns, PK, FK) in both directions.
- [ ] State machine exists for each main entity with a lifecycle; every enum value appears; every state has an exit or is marked terminal; each transition has a triggering FR.
- [ ] Activity/flowchart exists for each main business flow, with actors; flows have an implementation and a test (or are flagged).
- [ ] Class and sequence diagrams use real class/method names; one per feature/function in scope for the iteration.
- [ ] Technology declaration complete: third-party services, stack with versions, source/DevOps, environments incl. deploy and rollback, AI tools (tool, model, stages).
- [ ] Diagram sources stored in the repo as Mermaid/PlantUML.
- [ ] Modules, APIs and business rules in the SDD match the code (no "implemented differently").

## D. Cross-document
- [ ] Identical names across Report 1/2/3/4/5/6 and the code.
- [ ] Report 3 features appear in the Project Tracking WBS; Report 5 test cases reference FRs.
- [ ] Every claim has a source or is marked `[Cần bổ sung]`.

## E. Style
- [ ] Sentences state facts and requirements; no promotional wording.
- [ ] Tables have consistent IDs and no empty mandatory cells.

## Result block (put in the handover message)

```
Rubric result: A x/y, B x/y, C x/y, D x/y, E x/y
Fail: <items with evidence>
Not verifiable: <items with reason>
Open [Cần bổ sung]: <list>
```
