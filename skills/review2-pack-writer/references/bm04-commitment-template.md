# BM04 - Review 2 Commitment - form structure

Header line: `SWP490 · CAPSTONE PROJECT · REVIEW 2 · BM04`. Title: `Review 2 Commitment`.
Rules in the form: completed within **3 working days after Review 2**, confirmed by both reviewers and the supervisor. It is the sole basis for Defense 1.1 and the Viva. One block per main workflow (section 6) and one per member (section 7): duplicate or delete blocks to match the team. Export to PDF. File name `SWP490_<ProjectCode>_R2_Commitment.pdf`.

Content comes from the Review 2 outcome and BM01 as agreed with reviewers; do not invent commitments. Reviewer-completed fields stay blank.

## 1. Project Information
Project code, Project name, Team, Supervisor, Review 2 date, Reviewer 1, Reviewer 2, Version, Date.

## 2. Final Registration Form
| Field | Value |
|---|---|
| Final version | |
| Approved at Review 2 (Yes/No) | |
| Attached file name | |
After this point the project scope does not change.

## 3. Mandatory Features
| ID | Feature | Actor | Acceptance criteria | Workflow | Owner |
|---|---|---|---|---|---|
Each feature belongs to >= 1 workflow, has one owner and testable criteria. Equals BM01 section 6.

## 4. Non-Functional Requirements
| ID | Quality attribute | Metric | Threshold | Measurement method | Owner |
|---|---|---|---|---|---|

## 5. Out of Scope
| Item | Reason |
|---|---|

## 6. Workflow Commitments
Minimum number of main workflows = number of team members. Exactly one owner per workflow. Each mandatory feature belongs to >= 1 workflow.

### 6.n Workflow WF-0n (repeat per workflow)
| Field | Value |
|---|---|
| Workflow name | |
| Owner (one member) | |
| Supporting members | |
| Actors | |
| Trigger | |
| Business outcome | |
| Main entity state path | |
| Activity diagram (Report 4 section) | |

Features in this workflow
| Feature ID | Feature | Acceptance criteria | Test case IDs |
|---|---|---|---|

Demo scenarios
| Scenario ID | Type | Preconditions and data | Main steps | Expected result | Presenter |
|---|---|---|---|---|---|
IDs `DS-0na` (Main), `DS-0nb` (Exception), more rows as needed.

Committed test cases
| Test type | Count | Automated in CI | Responsible member(s) |
|---|---|---|---|
| Feature tests (≥ 3 per feature) | | | |
| End-to-end workflow test (≥ 1) | | | |
| State transition tests (≥ 1 per transition) | | | |
| Total for this workflow | | | |

Pass criteria at Defense 1.1
| Criterion | Committed |
|---|---|
| Runs end-to-end on staging with seeded data | Yes |
| Main scenario passes | Yes |
| Exception scenarios passing | |
| Test pass rate for this workflow | |
| Open Critical / High defects | 0 |

Reviewer note
| Note | |
|---|---|
(left blank)

## 7. Individual Commitments
One block per member. Every member owns >= 1 main workflow and 2-3 parts. Each test case and each fix is counted for one member only.

### 7.n Member n
| Field | Value |
|---|---|
| Full name | |
| Student ID | |
| Role in team | |

Ownership
| Type | Items (IDs / names) | Notes |
|---|---|---|
| Main workflow(s) owned | | |
| Mandatory features owned | | |
| Modules / entities owned | | |
| Design decisions owned (D-IDs) | | |
| NFRs responsible | | |

Delivery commitments to Defense 1.1
| Commitment | Committed (count / IDs) | Due |
|---|---|---|
| Functional test cases written | | |
| Of which automated in CI | | |
| Demo scenarios presented | | |
| Required fixes owned (section 9) | | |
| Documentation sections (Report / section) | | |

Ownership verification at Review 2 (completed by reviewers)
| Result | Weak points observed | Follow-up (by whom, by when) |
|---|---|---|
| ☐ Verified / ☐ Partly verified / ☐ Not verified | | |

Member confirmation: `Signature / date` (blank).

## 8. Summary and Cross-check
### 8.1 By workflow
| Workflow | Owner | Features | Demo scenarios (main / exception) | Test cases | Automated |
|---|---|---|---|---|---|
| WF-01 ... | | | | | |
| Total | | | | | |

### 8.2 By member
| Member | Workflows owned | Features | Test cases | Automated | Demo scenarios | Review 2 verification |
|---|---|---|---|---|---|---|
| Member 1 ... | | | | | | |
| Total | | | | | | |

The totals in 8.1 and 8.2 must both equal the committed numbers in 8.3.

### 8.3 Committed Numbers
| Item | Value |
|---|---|
| Number of main workflows | |
| Number of demo scenarios (main / exception) | |
| Committed functional test cases | |
| Of which automated in CI | |

### 8.4 Eligibility Thresholds for the Viva
| Criterion | Minimum threshold | Agreed threshold |
|---|---|---|
| Main workflows | 100% run end-to-end | |
| Demo scenarios | 100% main; ≥ 80% exception | |
| Test case count | ≥ committed number | |
| Test pass rate | ≥ 90% overall; 100% main-path tests of mandatory features | |
| Automation | ≥ 50% run in CI | |
| Defects | No open Critical or High defects | |
| Individual | Each member demos the workflow they own and meets their delivery commitments | |

Agreed thresholds are not lower than the minimums.

## 9. Required Fixes
Items from the Review 2 minutes and Planned items from BM02.
| ID | Item | Related workflow | Owner | Due |
|---|---|---|---|---|

## 10. Review 2 Conclusion (completed by reviewers)
`☐ Pass   ☐ Conditional pass   ☐ Re-review`

## 11. Confirmation
| Role | Full name | Signature | Date |
|---|---|---|---|
| Reviewer 1 | | | |
| Reviewer 2 | | | |
| Supervisor | | | |
| Team leader | | | |

## Arithmetic checks to run
- 8.1 column sums = 8.2 column sums = 8.3.
- Test cases in 8.3 >= minimum formula: `3 x features + workflows + state transitions + NFRs`.
- Automated >= 50 % of test cases (round up).
- Each feature appears in a workflow block; each test case ID appears for exactly one member.
- 7.n owners cover every workflow in section 6; every member owns >= 1 workflow.
