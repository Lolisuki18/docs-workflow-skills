# docs-workflow-skills

A set of Agent Skills (open `SKILL.md` format) for writing and auditing project documentation from real code. Works with any agent that reads `SKILL.md` folders (Claude Code, Cursor, Gemini CLI, Codex, ...).

Four areas:

1. **Code-first technical docs** - README, diagrams, API docs, ADRs.
2. **SDLC project reports** - Report 1-7, Weekly Report, Project Tracking, built from the course templates.
3. **Review 2 package** - BM01-BM04 with cross-form checks.
4. **Audit** - docs-vs-code sync and the BM02 standard self-review run.

## Principles

- **Evidence before prose.** Skills read code, config, DB scripts, git log or supplied documents first. No invented endpoints, commands, env vars, UI labels or progress numbers.
- **Gaps are marked, not filled:** `[Cần bổ sung: ...]`.
- **Plain technical tone.** No promotional wording.
- **Progressive disclosure.** Each `SKILL.md` stays short; templates, rubrics and conventions live in `references/` (one level deep).

## Skills

| Skill | Purpose | Status |
|---|---|---|
| [`docs-lifecycle`](docs-lifecycle/SKILL.md) | Orchestrator, 4 phases, routes to branches A-D | Batch 1 |
| [`readme-writer`](readme-writer/SKILL.md) | README and onboarding from manifests, Dockerfile, `.env.example` | Batch 1 |
| [`diagram-writer`](diagram-writer/SKILL.md) | Use Case, ERD, Sequence, Activity, State, Architecture; Mermaid/PlantUML as source, `.drawio` export | Batch 1 |
| [`api-doc-writer`](api-doc-writer/SKILL.md) | API spec (Markdown / OpenAPI 3.x) from routers, DTOs, validators, auth | Batch 1 |
| [`adr-writer`](adr-writer/SKILL.md) | Architecture Decision Records in `docs/adr/` | Batch 1 |
| [`docs-sync-auditor`](docs-sync-auditor/SKILL.md) | Read-only docs-vs-code audit; BM02 Standard Mode | Batch 1 |
| [`srs-sdd-writer`](srs-sdd-writer/SKILL.md) | Report 3 SRS, Report 4 SDD; traceability, 4 required diagrams, technology declaration, rubric self-check | Batch 2 |
| [`pm-report-writer`](pm-report-writer/SKILL.md) | Report 1, 2, 7, Weekly, Tracking; Report 5 packaging from real test results | Batch 2 |
| [`user-guide-writer`](user-guide-writer/SKILL.md) | Report 6 from the real UI; role-based, `[Screenshot: ...]` placeholders | Batch 2 |
| [`review2-pack-writer`](review2-pack-writer/SKILL.md) | Review 2 forms BM01-BM04, cross-form checks, PDF naming, 7-item checklist | Batch 2 |

## Routing branches (`docs-lifecycle`)

- **A** Repo technical docs
- **B** SDLC project reports (Report 1-7, Weekly, Tracking)
- **C** Docs-vs-code audit
- **D** Review 2 Package

Details: [`doc-routing-map.md`](docs-lifecycle/references/doc-routing-map.md).

## Repository layout

```text
docs-workflow-skills/
├── README.md
├── docs-lifecycle/        SKILL.md + references/doc-routing-map.md
├── readme-writer/         SKILL.md
├── diagram-writer/        SKILL.md + references/{mermaid-conventions,drawio-xml-guide}.md
├── api-doc-writer/        SKILL.md
├── adr-writer/            SKILL.md
├── docs-sync-auditor/     SKILL.md + references/bm02-standard-prompt.md
├── srs-sdd-writer/        SKILL.md + references/{report3-srs-template,report4-sdd-template,evaluation-rubric}.md
├── pm-report-writer/      SKILL.md + references/{report1-intro,report2-pmp-schedule,report3-tracking,report5-test-packaging,report7-final,weekly-report}-template.md
├── user-guide-writer/     SKILL.md + references/report6-user-guide-template.md
└── review2-pack-writer/   SKILL.md + references/{bm01..bm04 templates, review2-guide-summary}.md
```

## Install

Copy or symlink each skill folder (the 10 folders at the repo root) into your agent's skills directory (project-level or user-level). Examples (paths depend on the agent version; check its docs):

```powershell
# Claude Code, project-level
Get-ChildItem -Directory | Where-Object { Test-Path (Join-Path $_.FullName 'SKILL.md') } | ForEach-Object { Copy-Item -Recurse $_.FullName .claude\skills\ }
```

Each skill folder name equals the `name` in its frontmatter; do not rename folders.

## Usage

Start with the orchestrator: ask for "write the docs for this repo" or name a deliverable ("draw the ERD", "audit the docs"). The orchestrator opens each reply with `[Docs Phase X/4: ...]`, stops after Phase 1 for your confirmation of scope and file list, then gathers evidence, drafts and checks.

## Optional editor extension

For `.drawio` files install **Draw.io Integration** (`hediet.vscode-drawio`) in VS Code, Cursor or a compatible IDE. `diagram-writer` reminds you whenever it creates a `.drawio` file and can add it to `.vscode/extensions.json` if you agree.

## Conventions for skill authors

- `name`: kebab-case, identical to the folder name.
- `description`: third person; what it does + EN/VI trigger keywords + `Do NOT use for ...` exclusions.
- `SKILL.md` < 250 lines; supporting material one level down in `references/`.
- No IDE-specific tool names.

## Source templates

SDLC skills are based on the course template set (SEP490 Report 1-7, Weekly Report, Project Tracking, Test Report/Unit Test, Student Guide, Evaluation Form) and the SWP490 Review 2 package (BM01-BM04 and the preparation guide).
