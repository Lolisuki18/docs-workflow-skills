# Report 2 - Project Management Plan + Schedule (template structure)

Extracted from `Report2_Project Management Plan.docx` and `Report2_Sample Project Schedule.pdf`. Student Guide: due end of **Week 2**; updated in Weeks 3, 5, 7, ... with the schedule/tracking.

## I. Record of Changes
| Date | A* / M, D | In charge | Change Description |
|---|---|---|---|

## II. Project Management Plan

### 1. Overview
#### 1.1 Scope & Estimation
| # | WBS Item | Complexity | Est. Effort (man-days) |
|---|---|---|---|
Hierarchical numbering: feature `1`, functions `1.1`, `1.2`. Feature effort = sum of its functions (template: Feature 1 = 21 with 4 + 7 + ... ). Complexity: Simple / Medium / Complex using the thresholds in `report3-tracking-template.md`. Effort values come from the team's estimate; never fabricate - `[Cần bổ sung: estimate]`.

#### 1.2 Project Objectives
| # | Testing Stage | Test Coverage | No. of Defects | % of Defect | Notes |
|---|---|---|---|---|---|
Stages in the template: `1 Reviewing`, `2 Unit Test`, `3 Integration Test` (add System/Acceptance if the team plans them). These are **targets** at planning time; later actuals come from real results only. The template's guidance asks for an overall objective description plus target metrics for quality, time (`Milestone Timeliness (%)`) and cost (`Allocated Effort (man-days)` split across requirement, design, coding, testing, project management).

#### 1.3 Project Risks
| # | Risk Description | Impact | Possibility | Response Plans |
|---|---|---|---|---|

### 2. Management Approach
#### 2.1 Project Process
Process model (the guide recommends, but does not require, RUP: Initiation, Planning & Requirement, Software Designing, Implementation, Verification, Transition) and iterations.
#### 2.2 Quality Management
Approach to reach the quality objectives. Template examples: Defect Prevention, Reviewing, Unit Testing, Integration Testing, System Testing.
#### 2.3 Training Plan
| Training Area | Participants | When, Duration | Waiver Criteria |
|---|---|---|---|
Template examples: Java Spring Boot, Git/Github (Mandatory). Use the project's real stack from manifests.

### 3. Project Deliverables
| # | Deliverable | Due Date | Notes |
|---|---|---|---|
Dates `dd/MM/yyyy`. Use the Student Guide milestones (Reports 1-7, Software Packages 1-3, Full Package, Final Package) with the team's real dates.

### 4. Responsibility Assignments
Matrix: `Responsibility | <member 1> | <member 2> | ...` with one column per member (template header uses `Name + student code`). Cell codes (template legend): **D** = Do, **R** = Review, **S** = Support, **I** = Informed, blank = omitted. Rows in the template: Project Planning & Tracking, Prepare Project Introduction Document, Prepare SRS Document (Overview Part), ... one row per report/activity.

### 5. Project Communications
| Communication Item | Who/ Target | Purpose | When, Frequency | Type, Tool, Method(s) |
|---|---|---|---|---|

### 6. Configuration Management
#### 6.1 Document Management
Where and how documents are stored and versioned.
#### 6.2 Source Code Management
Repository platform, branching strategy, review rules - read from the real repo/CI.
#### 6.3 Tools & Infrastructures
| Category | Tools / Infrastructure |
|---|---|
Template rows: Technology, Database, IDEs/Editors, ... Fill from manifests/config (versions).

## Sample Project Schedule (PDF structure)

Table columns: `ID | Name | Duration | Start | Finish | Predecessors | Resource Names | Notes`. Dates `dd/mm/yy hh:mm` in the sample (work day 08:00-17:00). Tool: Microsoft Project or ProjectLibre (Student Guide); detailed tasks may live in GitLab/Trello/Asana.

Stages (RUP-based sample, 65 working days, Week 1-15):

| Stage | Weeks | Tasks (summary) |
|---|---|---|
| Initiation (Stage 1) | 1 | Prepare Report 1 -> Deliver Report 1 (Project Introduction) |
| Planning & Requirement (Stage 2) | 2-3 | Project Planning (Prepare Project Plan v0.9 -> Deliver Report 2); Project Preparing (Create Technical Prototype, Technical Training/Self Study); Requirement Analyzing (Write SRS v0.9, Update Project Plan v1.0 -> Deliver Report 3: SRS v0.9 + Plan v1.0) |
| Software Designing (Stage 3) | 4-5 | Write SDS v0.9, Update Project Plan v1.1 -> Deliver Report 4 (SDS v0.9 + Plan v1.1) |
| Implementation (Stage 4) | 6-11 | Code Iteration 1/2/3, each: Update SRS & SDS, Create Test Cases, Code + UT + IT, Complete Software Package n; then Deliver Report 5 (Test Report) |
| Verification (Stage 5) | 12-13 | Execute ST & Fix Bugs; Prepare for Deployment; Update Project Documents; Complete Full Software Package |
| Transition (Stage 6) | 14-15 | Software Optimization (Optimize/Refactor Codes; Execute UAT & Fix Bugs; Deploy Final Code); User Guides (Prepare, Deliver Report 6); Prepare Final Project Report; Prepare Thesis Presentation; Deliver Report 7 |

Predecessor notation in the sample: task ID, `SS` (start-to-start), `FS-2 days`, `SS+2 days`, `;` separating several predecessors. Milestones have 0 days.

When producing a schedule: dates from the semester calendar the user gives (the sample's 2021 dates are illustration only), actual status from git/tracker. Export as a Markdown table or CSV with the columns above.

## Consistency checks
- 1.1 WBS features equal SRS features and tracking WBS.
- 3 Deliverables dates equal the schedule's milestone dates.
- 4 columns equal the team table in Report 1.
