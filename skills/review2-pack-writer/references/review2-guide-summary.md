# Review 2 Preparation Guide - summary (v1.0, 10/2026)

Source: `SWP490_R2_Huong-dan-chuan-bi-Review-2_1.pdf` (7 pages). Audience: students, supervisors, reviewers. Documents in English; presentation/answers in Vietnamese or English.

## Five goals
1. Finalise the registration form (final version).
2. Review SRS and SDD on the finalised scope.
3. Fix mandatory product requirements: mandatory features, acceptance criteria, NFRs.
4. Fix Defense 1.1 targets: main workflows, demo scenarios, functional test-case count, Viva eligibility thresholds.
5. Verify each member's ownership through their ability to explain and defend their part.

Review 2 is the last point at which the registration form can change. The Review 2 results are the only basis for Defense 1.1 (Council 1.1) and the Viva (Council 1.2).

## Four documents to submit (all PDF)

| # | Document | Form | File |
|---|---|---|---|
| 1 | Proposed final registration form + Record of Changes | course form + BM03 | `..._R2_Registration.pdf` |
| 2 | Reports 1-5 and Project Tracking (code, DB script, tests, CI in repo at tag `review-2`) | course report templates | `..._R2_Report<n>.pdf` |
| 3 | SRS/SDD self-review report | BM02 | `..._R2_SelfReview.pdf` |
| 4 | Design Brief | BM01 | `..._R2_DesignBrief.pdf` |

BM04 (Review 2 Commitment) is completed after the review session, within 3 working days, confirmed by both reviewers and the supervisor: `..._R2_Commitment.pdf`.

## Requirements for SRS and SDD
- System Overview (architecture) diagram: components, external services, main data flows.
- Logical ERD and database design; the database script matches the ERD.
- State machine diagram per main entity with a lifecycle.
- Activity diagram or flowchart for main business flows, showing actors; no internal processing detail.
- Diagrams stored as source code (Mermaid or PlantUML) in the repo.
- Report 4 technology declaration: third-party services; development technology with versions; source code and DevOps; deployment environments (dev, staging, production; where; how to deploy and roll back); AI tools (tool, model, stages).

## Registration form
Keep the approved project code and title; keep the course form; number the next version and attach BM03. Changes must be consistent with SRS, SDD and BM01 sections 1, 6, 7. No changes -> resubmit the current form and tick "No changes" in BM03. Accepted reasons: Review 1 feedback, Iteration 1 findings, constraints from data, partners or technology. Changes that significantly reduce business complexity need full justification.

## Self-review (BM02)
Run the standard prompt with a coding agent that can read the whole repo, on tag `review-2`, with the proposed final registration form as scope. Do not edit the prompt. Paste raw AI results into BM02, no edits or deletions. Fill Team response: Fixed (commit link), Kept (reason), Planned (owner, due). High findings Kept/Planned go to BM01 section 5. Number of findings is not penalised; hiding findings is. Reviewers re-run the prompt on parts of the repo.

## Design Brief (BM01): sections and limits

| Section | Content | Limit |
|---|---|---|
| 0 Header | project code/name, team, supervisor, repo link (tag `review-2`), version, date | - |
| 1 Scope | changes vs current form; out of scope with reasons | "No changes" allowed |
| 2 System at a Glance | problem, users, core value; reference architecture diagram | <= 150 words |
| 3 Key Design Decisions | options considered, chosen option, reason, owner | exactly 5 rows |
| 4 Top Risks | impact, how verified or mitigated | 3 rows |
| 5 Known Gaps | mismatches between form, SRS, SDD, code, with plan | no limit |
| 6 Mandatory Features | measurable acceptance criteria and test | per scope |
| 7 Non-Functional Req. | metric, threshold, measurement | <= 6 rows |
| 8 Ownership Map | each member 2-3 parts and >= 1 main workflow | 1 row per member |

English, <= 4 A4 pages (font 11, margins 2 cm) for sections 0-8; Appendix A not counted. Acceptance criteria are acceptable when they can be written as a test with a clear pass/fail. Pass example: "A fully booked slot cannot be selected; the confirmation email is sent within 60 seconds." Fail example: "The booking screen is user-friendly."

## Review session (order)
1. Finalise the registration form (review Record of Changes and BM01 s.1; reviewers accept/adjust each change).
2. Present the Design Brief (5 decisions, 3 risks, Kept/Planned findings).
3. Change scenario: reviewers give a scenario in the final scope (add a role, add an entity state, third-party outage, 10x load); the team analyses impact on diagrams and code: which entities, states, flows, APIs, tests change. AI use is allowed but reasoning must be presented.
4. Fix product requirements and Defense 1.1 targets (features, acceptance criteria, NFRs; workflows, demos, test counts, thresholds).
5. Ownership verification: random members explain their owned parts and workflows, open code, answer "what if" questions. Result: Pass / Partly / Not verified.

## Outcome

| Conclusion | Condition | Next |
|---|---|---|
| Pass | design holds under change scenarios; all members Pass or Partly | proceed per Commitment |
| Conditional pass | design points to fix, or a member Not verified | supervisor checks the fix list by the due dates |
| Re-review | design fails change scenarios, or many members Not verified | re-review with one reviewer before continuing |

## Defense 1.1 goals (minimums)

- **Main workflow:** a complete business flow from an actor's start action to the final business outcome. Valid when >= 2 actors or >= 3 mandatory features, and it changes the state of >= 1 main entity. Minimum number = number of members. Exactly one owner per workflow; every member owns >= 1; each workflow has an activity diagram in the SDD.
- **Demo scenarios:** per workflow >= 1 main + >= 1 exception (wrong data, business rule violation, insufficient permission, external service failure). Run on the staging environment declared in Report 4, not on personal machines. Sample data loaded by a script in the repo. The Council may pick scenarios at random and change input data.
- **Functional test cases:**

| Source | Minimum | Requirement |
|---|---|---|
| each mandatory feature | 3 | 1 main flow; 1 data/business-rule check; 1 exception or authorization |
| each main workflow | 1 | end-to-end test of the main scenario |
| each main-entity state transition | 1 | includes invalid transitions that are rejected |
| each agreed NFR | 1 | measured against the agreed metric and threshold |

  Example from the guide: 15 features x 3 + 5 workflows + 12 transitions + 4 NFRs = 66. Report 5 test-case fields: ID, related feature or workflow, precondition, steps, data, expected result, how run (automatic/manual), actual result.

- **Viva eligibility thresholds:**

| Criterion | Minimum | Checked by |
|---|---|---|
| Main workflows | 100 % run end-to-end | demo of >= 2 random workflows |
| Demo scenarios | 100 % main pass; >= 80 % exception pass | scripted demo; Council may change data |
| Test case count | >= committed number | Report 5 vs Commitment |
| Test pass rate | >= 90 % overall; 100 % of main-path tests of mandatory features | rerun automated tests; test report |
| Automation | >= 50 % of test cases run in CI | CI run on the submission |
| Defects | no open Critical or High | defect list |
| Individual | each member demos their workflow and meets personal commitments | per member |

All criteria met -> eligible for the Viva; otherwise the team goes to Council 2 with a record of unmet criteria. Reviewers may set higher minimums; the team may commit higher, not lower.

## What the team must prove at the councils

| Item | Defense 1.1 | Viva |
|---|---|---|
| Scope | product meets the final registration form | - |
| Workflows, features | all thresholds in 9.4; each workflow checked against its Commitment block | demo per agreed scenarios on data provided by the Council |
| NFR | results measured the agreed way | explain results and limits |
| SRS, SDD | rerun the review prompt on the final version; no unexplained High finding | - |
| Required fixes | all done with commits | - |
| Individual | each member opens the repo, shows their part, runs tests | individual Q&A with a small change on their owned part |
| Documents | Reports 1-6, Full Software Package, Review 2 Commitment | Report 7, defense slides, final product set |

## AI-use rules
Declare tools, models and stages in Report 4. Every member is accountable for everything in the part they own, including AI-generated content. No real partner data, personal data, passwords, API keys or confidential information in AI tools; use synthetic data. Every AI output that enters the product passes review or tests before merging to the main branch. Do not edit the raw BM02 results; do not present unverified AI output as the team's analysis.

## Submission checklist (7 items)
1. `..._R2_Registration.pdf` with BM03
2. `..._R2_Report<n>.pdf` (Reports 1-5) and updated Project Tracking
3. Report 4: architecture diagram, Logical ERD, state machine, activity diagram, technology table
4. Repo tag `review-2`; Iteration 1 runs; CI runs automated tests
5. `..._R2_SelfReview.pdf`: raw results, run info, Team response for all findings
6. `..._R2_DesignBrief.pdf`: sections 0-8, <= 4 pages, Appendix A, repo link
7. Each member has prepared their owned part and main workflow

File naming pattern: `SWP490_<ProjectCode>_R2_<Name>.pdf`.
