# Changelog

Format: newest first. Skills are prompts, so "breaking" means a change in behavior an agent will notice (labels, hard stops, script flags).

## Unreleased (next: 0.2.0)

### Added
- Skills: `changelog-release-notes-writer`, `runbook-writer` and `postmortem-writer` (blameless review; one smoke run, see `evals/README.md`); `docs-lifecycle` branch E (release and operations docs).
- Two eval cases for the new skills (run once, results in `evals/README.md`).
- `scripts/install.py`: links or copies the skills into an agent's skills folder (junctions on Windows, symlinks elsewhere; never overwrites); `--only` / `--exclude` to choose skills.
- `scripts/readme-index.py`: generates the skill index in `README.md` from each `SKILL.md`; CI fails when it is out of date.
- CI also compares the shared scripts with the canonical copies in `ai-workflow-suite`.
- `.claude-plugin/plugin.json` so the repo installs as a Claude Code plugin (not yet checked with `claude plugin validate`).
- `LICENSE` (MIT).

### Changed
- Skill descriptions are English only and shorter (4 trigger phrases, at most 650 characters) to cut the context every installed skill costs. The trigger evals keep their Vietnamese prompts to check that matching still works.
- `docs-lifecycle` offers branches A, C and E only when there is no course context (B and D are built on the SEP490 / SWP490 templates).
- `scripts/validate.py` is now the shared validator from `ai-workflow-suite` (allows `evals/`, checks `../<skill>/` links).
- All twelve skills carry the same "untrusted content" rule.

## 0.1.0

Ten skills: `docs-lifecycle`, `readme-writer`, `diagram-writer`, `api-doc-writer`, `adr-writer`, `docs-sync-auditor`, `srs-sdd-writer`, `pm-report-writer`, `user-guide-writer`, `review2-pack-writer`, with helper scripts, `scripts/validate.py` and evals.
