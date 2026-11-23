# Report 3 - Software Requirement Specification (template structure)

Extracted from `Report3_Software Requirement Specification.docx`. Keep headings, numbering and table columns exactly. Sample rows in the original (Patron, Menu Manager, Order a Meal, BR-01...) are illustrations only.

Student Guide milestone: Week 3 delivers the full Part I and, for Part II, sections **II.1 Product Overview, II.2 User Requirements, II.3.1 System Functional Overview**; the rest is completed in later iterations. Each Software Package iteration updates the Functional Requirements (3.x) of this report.

## I. Record of Changes

| Date | A* / M, D | In charge | Change Description |
|---|---|---|---|

`A` = Added, `M` = Modified, `D` = Deleted. Template has 13 blank rows.

## II. Software Requirement Specification

### 1. Product Overview
Template guidance: overall description with a short introduction and a **context diagram** showing the boundary between the system and everything else: external entities (software, hardware, people, other systems) and the data, control and material flows between them. Report 7 adds: the environment of use, anticipated users, known constraints, assumptions and dependencies. Source: Report 1 vision/scope, repo README, registration form.

### 2. User Requirements

#### 2.1 Actors
| # | Actor | Description |
|---|---|---|
Template guidance: an actor is a person (or another software system or hardware device) that interacts with the system to perform a use case. Questions to find actors: who/what is notified when something occurs; who/what provides information or services to the system; who/what helps the system respond to and complete a task. Actors = roles that exist in code/spec (role enums, guards). One row per actor.

#### 2.2 Use Cases
##### 2.2.1 Diagram(s)
Use Case diagram(s) via `diagram-writer`. Actor and use-case names identical to 2.1 and 2.2.2.

##### 2.2.2 Descriptions
| ID | Use Case | Actors | Use Case Description |
|---|---|---|---|
Template guidance: a use case describes a sequence of interactions between the system and an external actor that gives the actor an outcome of value; names are **verb + object** and descriptive. Diagrams may be several (actor-UC and UC-UC relationships). ID format: the template shows `01`, `02`...; this skill set uses `UC01`, `UC02`... consistently (see ID conventions in `SKILL.md`).

### 3. Functional Requirements

#### 3.1 System Functional Overview
##### 3.1.1 Screens Flow
Template guidance: system screens and the relationships among them as a diagram; pop-up screens (e.g. Import Order) may use an oval, screens with several information tabs (e.g. Order Details) may be marked, and text/background formatting may distinguish them. Screens = real frontend routes/pages.

##### 3.1.2 Screen Descriptions
| # | Feature | Screen | Description |
|---|---|---|---|

##### 3.1.3 Screen Authorization
Matrix: first column `Screen`, then one column per role (`Role-Name1`, `Role-Name2`, ...). Cell = `X` if the role may access the screen/activity. Rows may be screens or screen activities. Source: route guards, permission config.

##### 3.1.4 Non-Screen Functions
| # | Feature | System Function | Description |
|---|---|---|---|
Template guidance: non-screen system functions such as batch/cron jobs, services, APIs. Also schedulers, event handlers, integrations, notifications.

##### 3.1.5 Entity Relationship Diagram
ERD via `diagram-writer` (logical ERD), then:
| # | Entity | Description |
|---|---|---|

#### 3.2 `<Feature Name 1>`
##### 3.2.1 `<Function Name 1>`
##### 3.2.2 `<Function Name 2>`
#### 3.3 `<Feature Name 2>` ... (repeat per feature/function)

Template guidance for each function (a screen or a non-screen function listed in 3.1.4):
- **Function trigger** - how it is triggered (navigation path, timing frequency, ...).
- **Function description** - actors/roles, purpose, interface, data processing, ...
- **Screen layout** - a mock-up prototype of the screen (screens only).
- **Function details** - data, validation, business rules and functionality for both normal and abnormal cases, so the reader can imagine how it works.

For traceability also record (extra, not template sections): Function ID (`FR-01`), related use case (`UC01`), pre-conditions, messages (`MSG01`), related API, testable acceptance criteria. Report 7 phrasing: "profile the functional specification for the feature, with the details on each function".

### 4. Non-Functional Requirements
#### 4.1 External Interfaces
Template guidance: information to ensure the system communicates properly with users and with external hardware or software/system elements. User interface, hardware, software/third-party interfaces, communication (protocols).
#### 4.2 Quality Attributes
4.2.1 Usability, 4.2.2 Reliability, 4.2.3 Performance, 4.2.4 `...` (security, maintainability, etc. as needed).
Template guidance per attribute:
- **Usability:** required training time for normal and power users; measurable task times for typical tasks, or usability based on systems users know; conformance to common usability standards (e.g. IBM CUA, Microsoft GUI standards).
- **Reliability:** availability (xx.xx %, hours of use, maintenance access, degraded mode), MTBF, MTTR, accuracy (precision/resolution), maximum bug or defect rate (bugs/KLOC or per function point), defect categories (minor, significant, critical) with a definition of "critical" (e.g. complete data loss).
- **Performance:** response time for a transaction (average, maximum), throughput (transactions/second), capacity (customers/transactions), resource utilisation (memory, disk, communications); reference related use cases by name.
Each NFR: metric, threshold, measurement method (Review 2 requirement).

### 5. Requirement Appendix

#### 5.1 Business Rules
| ID | Rule Definition |
|---|---|
Template guidance: common business rules the system must follow, in table form. `BR-01`, `BR-02`... Rules must exist in code or approved spec.

#### 5.2 Common Requirements
Template guidance: "fill all the common requirements here". Cross-cutting requirements (validation conventions, audit logging, pagination, etc.).

#### 5.3 Application Messages List
| # | Message code | Message Type | Context | Content |
|---|---|---|---|---|
`MSG01`...; types e.g. In line, In red under the text box, Toast message. Take real text from i18n/message files.

#### 5.4 Other Requirements...
Remaining requirements; recommended place for the **traceability matrix** (FR x Actor, UC, Entity, API, Screen, Test).

## Companion tracking
With Report 3 the team starts the Product Backlog and draft iteration backlogs using `Report3_Project Tracking` (see pm-report-writer).
