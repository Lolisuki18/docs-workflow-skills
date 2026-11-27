# Doc Routing Map

Used in Phase 1 of `docs-lifecycle` to map a request to a branch, a sub-skill and an output location.

## Branch (A) - Repo technical documentation

| User intent (EN / VI) | Skill | Default output | Primary evidence |
|---|---|---|---|
| README, onboarding, "how to run" / viết README, hướng dẫn chạy | `readme-writer` | `README.md` | manifests, Dockerfile, `.env.example`, CI |
| Diagram: use case, ERD, sequence, activity, state, architecture / vẽ sơ đồ | `diagram-writer` | `docs/diagrams/*.md` (Mermaid) or `*.puml`; optional `*.drawio` | entities, migrations, services, controllers |
| API spec, endpoint list, OpenAPI / tài liệu API | `api-doc-writer` | `docs/api/*.md` or `docs/api/openapi.yaml` | routers, controllers, DTOs, validators, auth middleware |
| Architecture decision, "why did we choose X" / ghi lại quyết định kiến trúc | `adr-writer` | `docs/adr/NNN-ten-quyet-dinh.md` | code, config, git log, user's stated rationale |

Branches (B) and (D) (course SEP490 / SWP490) are in `doc-routing-map-course.md`; read it when the project has course context or the request names a Report, SRS/SDD or Review 2 form.

## Branch (C) - Audit

| User intent | Skill | Output |
|---|---|---|
| "Are docs still accurate", "docs lệch code", after a large diff | `docs-sync-auditor` (default mode) | discrepancy table, read-only |
| "Run the BM02 self-review", "chạy prompt rà soát SRS/SDD" | `docs-sync-auditor` (BM02 Standard Mode) | raw AI finding table for BM02 |

## Branch (E) - Release and operations docs

Not tied to any course; works for company and open-source projects.

| User intent (EN / VI) | Skill | Default output | Primary evidence |
|---|---|---|---|
| Changelog, release notes, "what changed in v1.2" / viết changelog, ghi chú phát hành | `changelog-release-notes-writer` | `CHANGELOG.md`, release notes text | git tags, `git log` between tags, merged PR text |
| Runbook, ops guide, incident playbook, deploy and rollback / hướng dẫn vận hành | `runbook-writer` | `docs/runbook.md` | Dockerfile, compose, CI/CD, infra files, health endpoints, scripts |
| Postmortem, incident report, RCA / báo cáo sự cố | `postmortem-writer` | `docs/postmortems/YYYY-MM-DD-title.md` | logs, deploy history, commits, alerts and messages the user supplies |

Branches (B) and (D) apply only with SEP490 / SWP490 course context. Without it, skip them.

## Disambiguation

- "Document the API" with no more detail -> (A) `api-doc-writer`. "Write the SRS" -> (B) `srs-sdd-writer`; the API table inside the SDD is produced by `api-doc-writer`, not a separate request.
- "Check my docs" -> (C). "Fix my docs" -> (C) first (report), then the owning writer skill after the user confirms.
- "Draw ER diagram" -> `diagram-writer`; "Describe the database" in the SDD -> `srs-sdd-writer`, which asks `diagram-writer` for the ERD.
- Test case design belongs to QA/test skills, not here. Report 5 only *packages* real results.
- "Release notes" for users -> (E); Report 7 (final project report) -> (B).
- Unclear request -> ask one question listing branches A-E; do not guess.

## Suggested ordering for a full documentation pass

1. (A) README -> diagrams -> API docs -> ADRs
2. (B) Report 3 -> Report 4 -> Report 5 packaging -> Report 6 -> Report 1/2 refresh -> Report 7
3. (C) audit
4. (D) Review 2 forms (when the milestone is near)
5. (E) Runbook once deploy exists; changelog and release notes at every release
