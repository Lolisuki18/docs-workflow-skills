# BM01 - Design Brief (Review 2) - form structure

Header line of the form: `SWP490 · CAPSTONE PROJECT · REVIEW 2 · BM01`. Title: `Design Brief – Review 2`.
Rules in the form: sections 0-8 maximum **4 A4 pages** (font 11, margins 2 cm); Appendix A is not counted. Remove all grey guidance text and example rows, export to PDF. File name `SWP490_<ProjectCode>_R2_DesignBrief.pdf`.

## 0. Header
| Field | Value |
|---|---|
| Project code | |
| Project name | |
| Team | |
| Supervisor | |
| Repository link (tag review-2) | |
| Version | |
| Date | |

## 1. Scope
### 1.1 Registration Changes
Summary only; details in BM03. Write "No changes" if none.
| Section | Current | Proposed | Reason |
|---|---|---|---|

### 1.2 Out of Scope
| Item | Reason |
|---|---|

## 2. System at a Glance
Maximum **150 words**: the problem, the users, the core value. Link to the architecture diagram in the SDD.

## 3. Key Design Decisions
Exactly **5** decisions, each with one owner.
| ID | Decision | Options considered | Chosen option and rationale | Owner | Related FR / diagram |
|---|---|---|---|---|---|
| D1 ... D5 | | | | | |
Source ideas: ADRs in `docs/adr/` (see `adr-writer`), SDD decisions, git history. Use real decisions only.

## 4. Top Risks
3 rows (`R1`-`R3`).
| ID | Risk | Impact | How we verify or mitigate | Owner |
|---|---|---|---|---|

## 5. Known Gaps
Mismatches between registration form, SRS, SDD and code. **Include every High finding marked Kept or Planned in BM02.**
| ID | Gap | Location | Plan | Owner | Due |
|---|---|---|---|---|---|
For BM02-derived rows put the finding ID (e.g. `SR-03`) in `Gap` or `Location` so the cross-check X1 can match them.

## 6. Proposed Mandatory Features
Within the scope in section 1. Acceptance criteria must be testable with a clear pass/fail result.
| ID | Feature | Actor | Acceptance criteria (testable) | Test | Status |
|---|---|---|---|---|---|
`ID` format `F-01`; `Test` = test case IDs (e.g. `TC-F01-01..03`); `Status` = Done / In progress / Planned. (The form's example row "Book appointment" is an illustration only.)

## 7. Non-Functional Requirements
Maximum **6 rows**. Each needs a metric, a threshold and a measurement method.
| ID | Quality attribute | Metric | Threshold | Measurement method |
|---|---|---|---|---|

## 8. Ownership Map
One row per member. Each member owns **2-3 parts** and at least **one main workflow** (Appendix A1).
| Member | Role | Owned parts (2-3) | Main workflow owned | Key decisions / PRs |
|---|---|---|---|---|

## Appendix A - Defense 1.1 Targets (not counted in the 4 pages)

### A1. Main Workflows
Minimum number = number of team members. A valid workflow involves >= 2 actors or >= 3 mandatory features, and changes the state of >= 1 main entity.
| ID | Workflow | Actors | Trigger | Business outcome | Features | Entity states | Owner |
|---|---|---|---|---|---|---|---|

### A2. Demo Scenarios
Per workflow: at least 1 main and 1 exception scenario. Run on staging with seeded data.
| ID | Workflow | Type | Preconditions and data | Main steps | Expected result | Presenter |
|---|---|---|---|---|---|---|
IDs `DS-01`, `DS-02`...; `Type` = Main / Exception.

### A3. Functional Test Case Target
| Source | Count | Minimum per item | Subtotal |
|---|---|---|---|
| Mandatory features | | 3 | |
| Main workflows (end-to-end) | | 1 | |
| State transitions of main entities | | 1 | |
| Agreed NFRs | | 1 | |
| Committed total | | | |
Automated in CI: at least **50 %** of the committed total.

## Page-budget estimate (when no renderer is available)
Treat as a rough estimate only and report it as such. A4, font 11, 2 cm margins: about 500 words of running text per page, but tables use roughly half that density. Practical budget for sections 0-8: <= ~1,700 words including table text, with section 2 <= 150 words. Exceeding ~1,500 words or more than ~45 table rows in sections 1-8 -> warn "likely over 4 pages". Prefer rendering to PDF (word processor or converter) and counting pages.

## Filling notes
- Section 6 and 7 must equal the final BM04 sections 3 and 4.
- Section 8 owners equal the BM04 workflow owners and member blocks.
- Link to evidence by path (SDD section, diagram file), not by copying text.
