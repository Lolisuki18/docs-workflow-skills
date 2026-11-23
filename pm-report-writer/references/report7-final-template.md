# Report 7 - Final Project Report (template structure)

Extracted from `Report7_Final Project Report.docx`. Student Guide: due end of **Week 15** with the Final Project Products (database scripts, source code and related files, test documents and defects list, project schedule/tracking) and the defense slides. It consolidates the final updated Parts 1-6.

## Cover page (table layout in the template)
- `MINISTRY OF EDUCATION AND TRAINING`
- `FPT UNIVERSITY`
- `Capstone Project Document`
- `[Project name]`
- `<Group Name>`
- `Group Members`: `<Member name><RollNo><Student code>` per member
- `Supervisor`
- `Ext Supervisor`

## Front matter
- **Acknowledgement** - written by the team; do not generate personal sentiments, ask the user.
- **Definition and Acronyms** - table `Acronym | Definition` (e.g. project acronym, AWS, BA in the sample). Collect every acronym used across the report.

## Body (Heading 1 parts, each reuses the matching report)

| Part | Title | Source report | Sections (same numbering as the source) |
|---|---|---|---|
| I | Project Introduction | Report 1 | 1 Overview (1.1 Project Information, 1.2 Project Team), 2 Product Background, 3 Existing Systems, 4 Business Opportunity, 5 Software Product Vision, 6 Project Scope & Limitations |
| II | Project Management Plan | Report 2 | 1 Overview (1.1-1.3), 2 Management Approach (2.1-2.3), 3 Project Deliverables, 4 Responsibility Assignments, 5 Project Communications, 6 Configuration Management (6.1-6.3) |
| III | Software Requirement Specification | Report 3 | 1 Product Overview, 2 User Requirements, 3 Functional Requirements (3.1 System Functional Overview, 3.2 `<Feature>` / 3.2.1 `<Function>` ...), 4 Non-Functional Requirements (4.1, 4.2), 5 Requirement Appendix (5.1-5.4) |
| IV | Software Design Description | Report 4 | 1 System Design (1.1 System Architecture, 1.2 Package Diagram), 2 Database Design, 3 Detailed Design (3.x Class Diagram, Sequence Diagrams) |
| V | Software Testing Documentation | Report 5 | 1 Scope of Testing, 2 Test Strategy (2.1-2.3), 3 Test Plan (3.1-3.3), 4 Test Cases, 5 Test Reports |
| VI | Release Package & User Guides | Report 6 | 1 Deliverable Package (table `No. | Deliverable Item | Description`; first rows: Schedule/Task Tracking, Project Backlog, Source Codes), 2 Installation Guides (2.1, 2.2), 3 User Manual (3.1 Overview, 3.2 Workflow 1, 3.3 Workflow 2) |

Parts I-VI do **not** include a separate Record of Changes section in the template (the cover and definitions replace it); keep the part titles and numbering as above.

## Procedure
1. Check each source report is current: compare dates/versions with the repo and git log; if a source is stale, say which and ask whether to refresh it through its skill (`srs-sdd-writer`, `user-guide-writer`, others in this skill) before merging.
2. Copy content from the *current* source documents; do not re-write or "improve" facts. Update only cross-references, numbering and the front matter.
3. Build Definition and Acronyms from the merged text.
4. Verify consistency: team table (Part I) = responsibility matrix (Part II); feature names equal across III, WBS and VI; Part V numbers equal the Report 5 files; Part VI deliverable list equals the real final package contents.
5. Anything missing -> `[Cần bổ sung: ...]` (list in handover).
