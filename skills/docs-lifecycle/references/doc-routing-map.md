# Doc Routing Map

Used in Phase 1 of `docs-lifecycle` to map a request to a branch, a sub-skill and an output location.

## Branch (A) - Repo technical documentation

| User intent (EN / VI) | Skill | Default output | Primary evidence |
|---|---|---|---|
| README, onboarding, "how to run" / viết README, hướng dẫn chạy | `readme-writer` | `README.md` | manifests, Dockerfile, `.env.example`, CI |
| Diagram: use case, ERD, sequence, activity, state, architecture / vẽ sơ đồ | `diagram-writer` | `docs/diagrams/*.md` (Mermaid) or `*.puml`; optional `*.drawio` | entities, migrations, services, controllers |
| API spec, endpoint list, OpenAPI / tài liệu API | `api-doc-writer` | `docs/api/*.md` or `docs/api/openapi.yaml` | routers, controllers, DTOs, validators, auth middleware |
| Architecture decision, "why did we choose X" / ghi lại quyết định kiến trúc | `adr-writer` | `docs/adr/NNN-ten-quyet-dinh.md` | code, config, git log, user's stated rationale |

## Branch (B) - SDLC project reports

| Report | Skill | Template source |
|---|---|---|
| Report 1 Project Introduction | `pm-report-writer` | `references/report1-intro-template.md` |
| Report 2 PMP + Schedule | `pm-report-writer` | `references/report2-pmp-schedule-template.md` |
| Report 3 SRS | `srs-sdd-writer` | `references/report3-srs-template.md` |
| Report 4 SDD | `srs-sdd-writer` | `references/report4-sdd-template.md` |
| Report 5 Test packaging (from real test results) | `pm-report-writer` | `references/report5-test-packaging-template.md` |
| Report 6 Release Package & User Guides | `user-guide-writer` | `references/report6-user-guide-template.md` |
| Report 7 Final Project Report | `pm-report-writer` | `references/report7-final-template.md` |
| Weekly Report | `pm-report-writer` | `references/weekly-report-template.md` |
| Project Tracking (WBS / Issues / Defects / Q&A) | `pm-report-writer` | `references/report3-tracking-template.md` |

Report 7 aggregates Reports 1-6: when requested, check the sources are current first (route through the corresponding skills).

## Branch (C) - Audit

| User intent | Skill | Output |
|---|---|---|
| "Are docs still accurate", "docs lệch code", after a large diff | `docs-sync-auditor` (default mode) | discrepancy table, read-only |
| "Run the BM02 self-review", "chạy prompt rà soát SRS/SDD" | `docs-sync-auditor` (BM02 Standard Mode) | raw AI finding table for BM02 |

## Branch (D) - Review 2 Package

| User intent | Skill | Output |
|---|---|---|
| Prepare Review 2 files, Design Brief, Commitment, Record of Changes, "hồ sơ Review 2", BM01-BM04 | `review2-pack-writer` | BM01-BM04 content, cross-check report, naming and checklist |

Review 2 depends on branches (A)-(C): SRS/SDD (with 4 required diagram types), self-review run, repo tag `review-2`. Check these exist before drafting forms.

## Disambiguation

- "Document the API" with no more detail -> (A) `api-doc-writer`. "Write the SRS" -> (B) `srs-sdd-writer`; the API table inside the SDD is produced by `api-doc-writer`, not a separate request.
- "Check my docs" -> (C). "Fix my docs" -> (C) first (report), then the owning writer skill after the user confirms.
- "Draw ER diagram" -> `diagram-writer`; "Describe the database" in the SDD -> `srs-sdd-writer`, which asks `diagram-writer` for the ERD.
- Test case design belongs to QA/test skills, not here. Report 5 only *packages* real results.
- Unclear request -> ask one question listing branches A-D; do not guess.

## Suggested ordering for a full documentation pass

1. (A) README -> diagrams -> API docs -> ADRs
2. (B) Report 3 -> Report 4 -> Report 5 packaging -> Report 6 -> Report 1/2 refresh -> Report 7
3. (C) audit
4. (D) Review 2 forms (when the milestone is near)
