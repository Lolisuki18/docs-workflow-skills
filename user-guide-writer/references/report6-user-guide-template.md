# Report 6 - Release Package & User Guides (template structure)

Extracted from `Report6_Software User Guides.docx`. Student Guide: due end of **Week 14 (Transition)**; output Report 6 plus updated schedule/tracking. Content: final deliverable package, installation guides and software user manual. Report 7 Part VI reuses this report.

## I. Record of Changes
| Date | A* / M, D | In charge | Change Description |
|---|---|---|---|
(`*A - Added, M - Modified, D - Deleted`)

## II. Release Package & User Guides

### 1. Deliverable Package
Template guidance: list all source programs, scripts and documents **with the version number in this release**; customise or delete rows that do not apply.

| No. | Deliverable Item | Description |
|---|---|---|
| 1 | Project Schedule/Tracking | |
| 2 | Project Backlog | |
| 3 | Source Codes | |
| 4 | Database Script(s) | |
| 5 | Final Report Document | |
| 6 | Test Cases Document | |
| 7 | Defects List | |
| 8 | Issues List | |
| 9 | Slide | |

Fill `Description` with real file/folder paths, versions (tag/commit) and format. Remove rows that do not exist; do not list files absent from the repo or release.

### 2. Installation Guides
#### 2.1 System Requirements
Template guidance: system requirements needed to support the application, including software and relevant configurations. From manifests, Dockerfile, config (OS, runtime versions, browser, DB).
#### 2.2 Installation Instruction
Installation instructions and configuration guidelines. Commands from real scripts/CI (reuse `readme-writer` output); screens with the real labels.

### 3. User Manual
#### 3.1 Overview
Overview of the application; if possible a workflow figure showing all features.
#### 3.2 Workflow 1
Purpose of the workflow, a workflow diagram and other relevant diagrams, then detailed guidance: brief description and **step-by-step instructions with the user interface** screenshots for each function.
#### 3.3 Workflow 2
... repeat per workflow (the template shows 2; add as many as the product needs).

## Recommended per-workflow layout (inside 3.x)
1. Purpose (1-2 sentences, end-user language)
2. Who can do this (role) and what you need first
3. Workflow diagram (Mermaid flowchart via `diagram-writer`, or `[Screenshot: ...]`)
4. Steps: numbered, one action each, with the exact on-screen label in bold
5. Expected result for each key step
6. Common problems and messages (real message text from the UI/i18n)
