# Report 3 - Software Requirement Specification (template structure)

Extracted from `Report3_Software Requirement Specification.docx`. Keep headings, numbering and table columns exactly. Sample rows in the original (Patron, Menu Manager, Order a Meal, BR-01...) are illustrations only.

Student Guide milestone: Week 3 delivers the full Part I and, for Part II, sections **II.1 Product Overview, II.2 User Requirements, II.3.1 System Functional Overview**; the rest is completed in later iterations. Each Software Package iteration updates the Functional Requirements (3.x) of this report.

## I. Record of Changes

| Date | A* / M, D | In charge | Change Description |
|---|---|---|---|

`A` = Added, `M` = Modified, `D` = Deleted. Template has 13 blank rows.

## II. Software Requirement Specification

### 1. Product Overview
Short description of the product, context, and boundaries. Source: Report 1 vision/scope, repo README, registration form.

### 2. User Requirements

#### 2.1 Actors
| # | Actor | Description |
|---|---|---|
Actors = roles that exist in code/spec (role enums, guards). One row per actor.

#### 2.2 Use Cases
##### 2.2.1 Diagram(s)
Use Case diagram(s) via `diagram-writer`. Actor and use-case names identical to 2.1 and 2.2.2.

##### 2.2.2 Descriptions
| ID | Use Case | Actors | Use Case Description |
|---|---|---|---|
ID format `01`, `02`... (template) - keep the project's chosen format consistently (e.g. `UC01`).

### 3. Functional Requirements

#### 3.1 System Functional Overview
##### 3.1.1 Screens Flow
Screen navigation diagram (flowchart). Screens = real frontend routes/pages.

##### 3.1.2 Screen Descriptions
| # | Feature | Screen | Description |
|---|---|---|---|

##### 3.1.3 Screen Authorization
Matrix: first column `Screen`, then one column per role (`Role-Name1`, `Role-Name2`, ...). Cell = `X` if the role may access the screen/activity. Rows may be screens or screen activities. Source: route guards, permission config.

##### 3.1.4 Non-Screen Functions
| # | Feature | System Function | Description |
|---|---|---|---|
Batch jobs, schedulers, event handlers, integrations, notifications.

##### 3.1.5 Entity Relationship Diagram
ERD via `diagram-writer` (logical ERD), then:
| # | Entity | Description |
|---|---|---|

#### 3.2 `<Feature Name 1>`
##### 3.2.1 `<Function Name 1>`
##### 3.2.2 `<Function Name 2>`
#### 3.3 `<Feature Name 2>` ... (repeat per feature/function)

Per function the template gives only the heading. Recommended content (to keep traceability, not additional template sections): Function ID (FR-nn), related use case, actor, screen, trigger, pre-conditions, main flow, alternative/exception flow, validation rules, business rules (BR-nn), messages (MSGnn), data (entities/fields), related API, acceptance criteria (testable).

### 4. Non-Functional Requirements
#### 4.1 External Interfaces
User interface, hardware, software/third-party interfaces, communication (protocols).
#### 4.2 Quality Attributes
4.2.1 Usability, 4.2.2 Reliability, 4.2.3 Performance, 4.2.4 `...` (security, maintainability, etc. as needed).
Each NFR: metric, threshold, measurement method (Review 2 requirement).

### 5. Requirement Appendix

#### 5.1 Business Rules
| ID | Rule Definition |
|---|---|
`BR-01`, `BR-02`... Rules must exist in code or approved spec.

#### 5.2 Common Requirements
Cross-cutting requirements (validation conventions, audit logging, pagination, etc.).

#### 5.3 Application Messages List
| # | Message code | Message Type | Context | Content |
|---|---|---|---|---|
`MSG01`...; types e.g. In line, In red under the text box, Toast message. Take real text from i18n/message files.

#### 5.4 Other Requirements...
Remaining requirements; recommended place for the **traceability matrix** (FR x Actor, UC, Entity, API, Screen, Test).

## Companion tracking
With Report 3 the team starts the Product Backlog and draft iteration backlogs using `Report3_Project Tracking` (see pm-report-writer).
