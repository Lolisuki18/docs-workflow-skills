# Report 4 - Software Design Document (template structure)

Extracted from `Report4_Software Design Document.docx`, extended with the Review 2 requirements from the Review 2 preparation guide. Keep template headings and numbering; add the Review 2 items in the places indicated.

Student Guide milestone: Week 5 delivers **System Design and Database Design**; Software Packages 1-3 update **Class and Sequence Diagrams**.

## I. Record of Changes

| Date | A* / M, D | In charge | Change Description |
|---|---|---|---|

## II. Software Design Document

### 1. System Design

#### 1.1 System Architecture
System Overview / architecture diagram: components, external services, main data flows (via `diagram-writer`, canonical Mermaid/PlantUML). Every component and third-party service present in code must appear; none that is absent from code.

Add here (Review 2): **1.1.1 Technology Declaration** - table below.

#### 1.2 Package Diagram
Diagram plus:
| No | Package | Description |
|---|---|---|
Packages = real modules/namespaces/folders.

### 2. Database Design
Logical ERD (via `diagram-writer`) plus table list:
| No | Table | Description |
|---|---|---|
Description cell also lists:
- Primary keys: `<list of primary key fields>`
- Foreign keys: `<list of foreign key fields>`

Rules: ERD, this table list and the database script contain the **same tables, columns, PK/FK**. Check both directions (in script not in ERD; in ERD not in script). Reference the script path.

### 3. Detailed Design
Per feature/function `3.x <Feature/Function Name>`:
- 3.x.1 Class Diagram
- 3.x.2 `<Sequence Diagram Name 1>`
- 3.x.3 `<Sequence Diagram Name 2>`
- 3.x.4 ...
Use real classes and methods. Add for Review 2:
- **State machine diagram** per main entity with a lifecycle (states = enum values; each transition names its trigger/FR).
- **Activity diagram or flowchart** per main business flow, showing actors; business level (no internal processing detail). Name it with the workflow ID when the team uses workflow IDs (e.g. `WF-01`) so BM04 can reference "Activity diagram (Report 4 section)".

## Mandatory diagram set (Review 2)

| # | Diagram | Where | Notes |
|---|---|---|---|
| 1 | System Overview (architecture) | 1.1 | components, external services, data flows |
| 2 | Logical ERD | 2 | DB script matches |
| 3 | State machine | 3.x | each main entity with a lifecycle |
| 4 | Activity / flowchart | 3.x | main business flows, with actors |

Diagrams are stored as source code (Mermaid or PlantUML) in the repo (e.g. `docs/diagrams/`). `.drawio` copies are optional exports.

## Technology Declaration (Review 2)

Fill from manifests, Docker/CI/deploy config and the team's statements. Missing -> `[Cần bổ sung: ...]`.

| Group | What to declare | Evidence |
|---|---|---|
| Third-party services | Service name, purpose (Authentication, Storage, Payment, AI APIs, ...), data sent to it | SDK imports, config, env var names |
| Development technology | Front-end, Back-end, Mobile, Database - each **with version** | manifests, Dockerfile |
| Source code and DevOps | Platform (GitHub, GitLab, Azure DevOps), CI/CD, branching rules | CI files, repo settings |
| Deployment environments | Dev, staging, production; where deployed; how to deploy; **how to roll back** | compose/IaC/deploy scripts, runbook |
| AI tools | Tool, model, and stages used (specification, design, code, testing, review) | team statement; `[Cần bổ sung]` if unknown |

AI declaration is mandatory under the AI-use rules: tools, models and stages must be stated in Report 4.

## Traceability from design
- Each FR in Report 3 maps to at least one sequence diagram or class set and to tables/API in this report.
- Each API in the API table exists in code (`api-doc-writer`).
- Each state in a state machine exists in code; each transition has a triggering FR.
