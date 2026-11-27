# docs-workflow-skills

A set of Agent Skills (open `SKILL.md` format) for writing and auditing project documentation from real code. Works with any agent that reads `SKILL.md` folders (Claude Code, Cursor, Gemini CLI, Codex, ...).

Five areas:

1. **Code-first technical docs** - README, diagrams, API docs, ADRs.
2. **SDLC project reports** - Report 1-7, Weekly Report, Project Tracking, built from the course templates.
3. **Review 2 package** - BM01-BM04 with cross-form checks.
4. **Audit** - docs-vs-code sync and the BM02 standard self-review run.
5. **Release and operations docs** - changelog, release notes, runbook (not tied to any course).

## Skill index

<!-- skills:start -->
**13 skills.** This index is generated from each `SKILL.md`; run `python scripts/readme-index.py` to refresh it.

| Skill | What it does |
|---|---|
| [`adr-writer`](adr-writer/SKILL.md) | Writes Architecture Decision Records into docs/adr/ with Context, Options Considered, Decision and Consequences/Trade-offs |
| [`api-doc-writer`](api-doc-writer/SKILL.md) | Generates API specifications (Markdown or OpenAPI 3.x) by reading real routers, controllers, DTOs, validators and auth middleware |
| [`changelog-release-notes-writer`](changelog-release-notes-writer/SKILL.md) | Writes CHANGELOG.md entries (Keep a Changelog format) and release notes from the real git history between two tags or commits |
| [`diagram-writer`](diagram-writer/SKILL.md) | Draws software diagrams (Use Case, ERD, Sequence, Activity, State Machine, System Architecture) from real entities, migrations |
| [`docs-lifecycle`](docs-lifecycle/SKILL.md) | Orchestrates documentation work in 4 phases (Discovery & Routing, Evidence Gathering, Drafting |
| [`docs-sync-auditor`](docs-sync-auditor/SKILL.md) | Audits existing documentation (README, API docs, diagrams, SRS/SDD, User Guide) against the source code or the latest git diff, read-only by default |
| [`pm-report-writer`](pm-report-writer/SKILL.md) | Writes SDLC project-management reports from the course templates |
| [`postmortem-writer`](postmortem-writer/SKILL.md) | Writes a blameless post-incident review from real evidence (logs, deploy history, commits, alerts, chat excerpts the user supplies) |
| [`readme-writer`](readme-writer/SKILL.md) | Generates or updates README.md and onboarding instructions by reading the real package.json / pom.xml / *.csproj / pyproject.toml / Dockerfile /... |
| [`review2-pack-writer`](review2-pack-writer/SKILL.md) | Prepares the SWP490 Review 2 package - Design Brief BM01 (with Appendix A), Self-Review BM02 (packaging only) |
| [`runbook-writer`](runbook-writer/SKILL.md) | Writes operations runbooks from the real repository and infrastructure files |
| [`srs-sdd-writer`](srs-sdd-writer/SKILL.md) | Writes Report 3 (SRS) and Report 4 (SDD) from real code, DB schema and use-case input, following the course templates |
| [`user-guide-writer`](user-guide-writer/SKILL.md) | Writes Report 6 (Release Package & User Guides) - deliverable package, installation guide and role-based user manual |
<!-- skills:end -->

## Principles

- **Evidence before prose.** Skills read code, config, DB scripts, git log or supplied documents first. No invented endpoints, commands, env vars, UI labels or progress numbers.
- **Gaps are marked, not filled:** `[Cần bổ sung: ...]`.
- **Plain technical tone.** No promotional wording.
- **Progressive disclosure.** Each `SKILL.md` stays short; templates, rubrics and conventions live in `references/` (one level deep).

## Skills

`Status` is the delivery batch: Batch 1 = code-first technical docs and audit, Batch 2 = SDLC course reports and the Review 2 package, Batch 3 = release and operations docs. All 13 skills pass `scripts/validate.py`.

| Skill | Purpose | Status |
|---|---|---|
| [`docs-lifecycle`](docs-lifecycle/SKILL.md) | Orchestrator, 4 phases, routes to branches A-E | Batch 1 |
| [`readme-writer`](readme-writer/SKILL.md) | README and onboarding from manifests, Dockerfile, `.env.example` | Batch 1 |
| [`diagram-writer`](diagram-writer/SKILL.md) | Use Case, ERD, Sequence, Activity, State, Architecture; Mermaid/PlantUML as source, `.drawio` export | Batch 1 |
| [`api-doc-writer`](api-doc-writer/SKILL.md) | API spec (Markdown / OpenAPI 3.x) from routers, DTOs, validators, auth | Batch 1 |
| [`adr-writer`](adr-writer/SKILL.md) | Architecture Decision Records in `docs/adr/` | Batch 1 |
| [`docs-sync-auditor`](docs-sync-auditor/SKILL.md) | Read-only docs-vs-code audit; BM02 Standard Mode | Batch 1 |
| [`srs-sdd-writer`](srs-sdd-writer/SKILL.md) | Report 3 SRS, Report 4 SDD; traceability, 4 required diagrams, technology declaration, rubric self-check | Batch 2 |
| [`pm-report-writer`](pm-report-writer/SKILL.md) | Report 1, 2, 7, Weekly, Tracking; Report 5 packaging from real test results | Batch 2 |
| [`user-guide-writer`](user-guide-writer/SKILL.md) | Report 6 from the real UI; role-based, `[Screenshot: ...]` placeholders | Batch 2 |
| [`review2-pack-writer`](review2-pack-writer/SKILL.md) | Review 2 forms BM01-BM04, cross-form checks, PDF naming, 7-item checklist | Batch 2 |
| [`changelog-release-notes-writer`](changelog-release-notes-writer/SKILL.md) | CHANGELOG.md and release notes from the real git range; breaking changes found in the diff | Batch 3 |
| [`runbook-writer`](runbook-writer/SKILL.md) | Deploy, rollback and symptom-based incident playbooks from compose, CI and infra files | Batch 3 |
| [`postmortem-writer`](postmortem-writer/SKILL.md) | Blameless post-incident review from real evidence: timeline, causes, impact, action items | Batch 3 |

## Routing branches (`docs-lifecycle`)

- **A** Repo technical docs
- **B** SDLC project reports (Report 1-7, Weekly, Tracking)
- **C** Docs-vs-code audit
- **D** Review 2 Package
- **E** Release and operations docs (changelog, release notes, runbook, postmortem)

Branches B and D are built on the SEP490 / SWP490 course templates; for a non-course project the orchestrator offers A, C and E only.

Details: [`doc-routing-map.md`](docs-lifecycle/references/doc-routing-map.md).

## Repository layout

```text
docs-workflow-skills/
├── README.md
├── scripts/validate.py          structure checks for all skills (also run by CI)
├── evals/                       behavioural test cases (evals.json + how to run)
├── .github/workflows/validate.yml
├── docs-lifecycle/        SKILL.md + references/doc-routing-map.md, doc-routing-map-course.md
├── readme-writer/         SKILL.md + references/examples.md
├── diagram-writer/        SKILL.md + references/{mermaid-conventions,drawio-xml-guide,examples}.md
│                          + scripts/{drawio_gen,erd_vs_sql}.py
├── api-doc-writer/        SKILL.md + references/examples.md
├── adr-writer/            SKILL.md
├── docs-sync-auditor/     SKILL.md + references/bm02-standard-prompt.md
├── srs-sdd-writer/        SKILL.md + references/{report3-srs-template,report4-sdd-template,evaluation-rubric,examples}.md
├── pm-report-writer/      SKILL.md + references/{report1-intro,report2-pmp-schedule,report3-tracking,report5-test-packaging,report7-final,weekly-report}-template.md
│                          + scripts/{report5_stats,csv_to_xlsx,fill_docx_table}.py
├── user-guide-writer/     SKILL.md + references/report6-user-guide-template.md
├── changelog-release-notes-writer/  SKILL.md + references/templates.md
├── runbook-writer/        SKILL.md + references/runbook-template.md
├── postmortem-writer/     SKILL.md + references/postmortem-template.md
└── review2-pack-writer/   SKILL.md + references/{bm01..bm04 templates, review2-guide-summary}.md
                           + scripts/{check_review2,bm01_pages}.py
```

## What a run looks like

These excerpts come from a test run on a sample app (`Test-skill`, a small habit tracker plus two other toy modules), not from a production project. Excerpt of `docs/habitly/adr/001-localstorage-for-persistence.md`, written by `adr-writer` from the sample habit tracker's code (header and the start of the decision). Facts the repo could not show are left as `[Needs input]` instead of being invented:

Source: `Test-skill/docs/habitly/adr/001-localstorage-for-persistence.md`, quoted verbatim.

````markdown
# 001. Keep habit data in the browser's localStorage under one key

- **Status:** Accepted
- **Date:** 2026-11-27 (commit `8ec8923`; `[Needs input: decision date - not recorded]`)
- **Deciders:** `[Needs input: deciders - not recorded]`
- **Related:** [003](003-json-export-import-backup.md), [Architecture diagram](../diagrams/architecture-habitly.md)
## Decision

We keep all habit data in `localStorage` as one JSON value under `habitly.v1`, with a version field inside the value (`version: 1`, `habitly/src/domain/habits.js:6`). It applies to the web page in `habitly/` only.

Handling of bad storage, as implemented:
- Unparseable or invalid stored data is copied to `habitly.v1.corrupt`, the app starts empty and shows a notice (`habitly/src/storage.js:30-37`). The next change then saves over `habitly.v1`; the copy under the corrupt key is not removed by the app.
- If reading throws, the app starts empty and says changes will not be saved (`habitly/src/storage.js:22-27`). This includes the case where reading the `localStorage` property itself throws: `getStore()` returns `null` instead (`habitly/src/storage.js:8-14`, `habitly/src/ui/app.js:13`).
- If writing fails, the app shows a message that changes will be lost on reload (`habitly/src/ui/app.js:25`).
````

## Install as a Claude Code plugin

After the repos are published, the marketplace lives in `ai-workflow-suite`:

```bash
claude plugin marketplace add Lolisuki18/ai-workflow-suite
claude plugin install docs-workflow-skills@lolisuki18-skills
```

The manifest (`.claude-plugin/plugin.json`) has **not** been checked with `claude plugin validate` yet. Plugin skills are namespaced by the plugin name. The script install below does not need any of this.

## One-command install

```powershell
python scripts/install.py                    # links every skill into ~/.claude/skills
python scripts/install.py --agent gemini     # presets: claude, gemini, cursor, codex, antigravity, windsurf, cline, roo, agents
python scripts/install.py --dry-run          # preview; --copy to copy; --uninstall to remove
```

Junctions on Windows (no admin), symlinks elsewhere; existing skills are never overwritten.

## Helper scripts (optional, Python 3)

Scripts make rule checks exact instead of relying on the agent's arithmetic. Skills use them when Python is available and say so when it is not.

| Script | What it does |
|---|---|
| `diagram-writer/scripts/erd_vs_sql.py` | Compare a Mermaid ERD with SQL `CREATE TABLE` statements, both directions |
| `diagram-writer/scripts/drawio_gen.py` | Build a `.drawio` from a JSON node/edge list with a validated layered layout |
| `pm-report-writer/scripts/report5_stats.py` | Report 5 counts, coverage and successful coverage from real result rows |
| `pm-report-writer/scripts/csv_to_xlsx.py` | Template-shaped `.xlsx` (Tracking, Weekly) from CSV; needs `openpyxl` |
| `pm-report-writer/scripts/fill_docx_table.py` | Fill a table of the course `.docx` template from CSV, keeping its formatting; refuses a changed header; `--header-row R` for two-level headers; needs `python-docx` |
| `review2-pack-writer/scripts/check_review2.py` | Cross-form checks X1, X2, X3, X5, X6, X7, X9, X13 and the test-case formula |
| `review2-pack-writer/scripts/bm01_pages.py` | Page count of BM01 sections 0-8 from a PDF/DOCX (needs `pypdf`; DOCX needs LibreOffice) |

## Validation and evals

```powershell
python scripts/validate.py   # Windows: py scripts/validate.py
```

Checks `name` = folder, third-person English `description` of at most 650 characters with `Do NOT use`, no duplicate triggers, files under 250 lines, balanced code fences, existing references and scripts that compile without `SyntaxWarning`. The same command runs in GitHub Actions on every push and pull request. Behavioural test cases are in [`evals/`](evals/README.md) (written, not yet executed).

## ID conventions

Shared by all skills: `A-01`, `UC01`, `FR-01`, `NFR-01`, `BR-01`, `MSG01`, `FE-01`, `LI-01`, `F-01`, `WF-01`, `DS-01a/b`, `D1-D5`, `R1-R3`, `SR-01`, `TC-F01-01`.

## Install

Copy or symlink each skill folder (the 13 folders at the repo root, each containing `SKILL.md`) into your agent's skills directory, project-level or user-level. Folder names must stay equal to the `name` in each `SKILL.md`.

| Agent | Project-level folder | Notes |
|---|---|---|
| Claude Code | `.claude/skills/` | user-level: `~/.claude/skills/` |
| Cursor | `.cursor/skills/` | also reads `.claude/skills/` and `.codex/skills/`; enable Agent Skills in settings if your version requires it |
| Gemini CLI | `.gemini/skills/` or `.agents/skills/` | user-level: `~/.gemini/skills/`; the feature may be experimental and need enabling; check with `gemini skills list` |
| Codex | `.agents/skills/` | newer docs; an older page used `.codex/skills/` |
| Antigravity, Windsurf, others | see the tool's documentation | not verified here; any tool that reads `SKILL.md` folders can use this repo unchanged |

Paths were taken from each vendor's documentation at the time of writing; they change between versions, so confirm against your tool's docs. For a tool without skill support, add a rule file that tells the agent to read the matching `SKILL.md` before documentation tasks.

```powershell
# project-level install for Claude Code (change the target for another agent)
New-Item -ItemType Directory -Force .claude\skills | Out-Null
Get-ChildItem -Directory | Where-Object { Test-Path (Join-Path $_.FullName 'SKILL.md') } | ForEach-Object { Copy-Item -Recurse $_.FullName .claude\skills\ }
```

### Windows and Python

The helper scripts and `scripts/validate.py` need Python 3. On Windows the `python` command can point to the Microsoft Store alias and fail with "The file cannot be accessed by the system". Use the launcher instead:

```powershell
py scripts/validate.py
```

or install Python from python.org and turn off *Settings -> Apps -> Advanced app settings -> App execution aliases* for `python.exe`. Replace `python` by `py` in every command in this repository on Windows.

## Usage

Start with the orchestrator: ask for "write the docs for this repo" or name a deliverable ("draw the ERD", "audit the docs"). The orchestrator opens each reply with `[Docs Phase X/4: ...]`, stops after Phase 1 for your confirmation of scope and file list, then gathers evidence, drafts and checks.

## Optional editor extension

For `.drawio` files install **Draw.io Integration** (`hediet.vscode-drawio`) in VS Code, Cursor or a compatible IDE. `diagram-writer` reminds you whenever it creates a `.drawio` file and can add it to `.vscode/extensions.json` if you agree.

## Conventions for skill authors

- `name`: kebab-case, identical to the folder name.
- `description`: third person; what it does + English trigger phrases + `Do NOT use for ...` exclusions.
- `SKILL.md` < 250 lines; supporting material one level down in `references/` (documents) or `scripts/` (code).
- No IDE-specific tool names.

## Sibling repos

| Repo | Covers |
|---|---|
| [`dev-workflow-skills`](https://github.com/Lolisuki18/dev-workflow-skills) | idea → plan → code → tests → audit, bug investigation |
| [`pull-request-skills`](https://github.com/Lolisuki18/pull-request-skills) | PR description, PR review, review replies, pre-PR self-review, code comments |
| [`qa-workflow-skills`](https://github.com/Lolisuki18/qa-workflow-skills) | QA/STLC: test plan, test matrix, E2E, defects, summary report |
| [`docs-workflow-skills`](https://github.com/Lolisuki18/docs-workflow-skills) (this one) | documentation and SDLC reports |

Each repo is self-contained. `code-comment-writer` (in `pull-request-skills`) covers comments inside source code; this repo covers documents.

## Source templates

SDLC skills are based on the course template set (SEP490 Report 1-7, Weekly Report, Project Tracking, Test Report/Unit Test, Student Guide, Evaluation Form) and the SWP490 Review 2 package (BM01-BM04 and the preparation guide).
