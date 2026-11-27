# Changelog

Format: newest first. Skills are prompts, so "breaking" means a change in behavior an agent will notice (labels, hard stops, script flags).

## [Unreleased]

## [1.0.0] - 2026-11-27

### Added
- Shared `scripts/run-evals.py` (copy of the canonical file in `ai-workflow-suite`; `turns:` multi-turn convention, `--dry-run`).
- Eval cases `postmortem-01` (no incident named: declines, writes no file) and `postmortem-02` (explicit timeline: only supplied facts, gaps marked).
- `docs-lifecycle`: an existing flat evidence file is migrated to the module folder only after asking once.
- Skills: `changelog-release-notes-writer`, `runbook-writer` and `postmortem-writer` (blameless review; one smoke run, see `evals/README.md`); `docs-lifecycle` branch E (release and operations docs).
- Two eval cases for the new skills (run once, results in `evals/README.md`).
- `scripts/install.py`: links or copies the skills into an agent's skills folder (junctions on Windows, symlinks elsewhere; never overwrites); `--only` / `--exclude` to choose skills.
- `scripts/readme-index.py`: generates the skill index in `README.md` from each `SKILL.md`; CI fails when it is out of date.
- CI also compares the shared scripts with the canonical copies in `ai-workflow-suite`.
- `.claude-plugin/plugin.json` so the repo installs as a Claude Code plugin (not yet checked with `claude plugin validate`).
- `LICENSE` (MIT).

### Changed
- References now load on demand per step: course branches B and D moved to `docs-lifecycle/references/doc-routing-map-course.md` (read only for course context); `srs-sdd-writer` and `review2-pack-writer` templates load after the first hard stop; `pm-report-writer` reads its template when it drafts. Measured (tokens = bytes / 3.8), eager: `srs-sdd-writer` 4,642 -> 1,915 (-59%), `review2-pack-writer` 6,050 -> 2,489 (-59%), `pm-report-writer` 2,770 -> 1,642 (-41%), `docs-lifecycle` 4,191 -> 3,943 (-6%); path A, C, E (9 skills) 16,818 -> 16,570 (-1.5%).
- Real-run fixes: `readme-writer` keeps an existing README's section order and adds only missing sections (reorder only on request); `api-doc-writer` documents and flags runtime deviations and verifies endpoints with real requests; `runbook-writer` runs every Confirm step before writing it (else `not run`) and checks cwd-relative paths, duplicate listeners and blind health checks; `docs-lifecycle` lists `_evidence.md` in the Phase 1 file list and says to copy untracked plan requirement ids into docs.
- Evals: `adr-01` and `ug-01` gain an approval turn, `ug-01` scopes the vocabulary ban to end-user instructions, and the evals README status matches the results log.
- Skills tuned after agents ran them on a tiny Python CLI: `docs-lifecycle` gains a "Small scope" rule, a skipped-skills line in the handover, guidance for branch B/D requests without course context, mandated-files wording, line-reference and git-ignored-source rules.
- `runbook-writer`, `postmortem-writer`, `api-doc-writer` and `user-guide-writer` now stop early (and point to `readme-writer` or the changelog) when there is no operable system, no named incident, no network API or no end-user UI.
- `srs-sdd-writer` checks that the user wants the course template and has a "Lite mode"; `adr-writer` handles implied alternatives, scope updates and dates; `diagram-writer` has a "type not applicable" outcome, a lightweight check without a renderer and a proportionality rule; `readme-writer` and `changelog-release-notes-writer` cover rotting counts, section reordering, stdlib-only projects, unmerged branches and untagged versions.
- Skill descriptions are English only and shorter (4 trigger phrases, at most 650 characters) to cut the context every installed skill costs. The trigger evals keep their Vietnamese prompts to check that matching still works.
- `docs-lifecycle` offers branches A, C and E only when there is no course context (B and D are built on the SEP490 / SWP490 templates).
- `scripts/validate.py` is now the shared validator from `ai-workflow-suite` (allows `evals/`, checks `../<skill>/` links).
- Every skill carries the same "untrusted content" rule.
- Hard stops: sub-skill stops that only confirm path, overwrite or numbering are satisfied by the `docs-lifecycle` Phase 1 file-list approval (each stop says so); stops that approve content (draft approval, ADR status, existing README outline) still apply. `api-doc-writer`'s format/overwrite question is no longer labelled a hard stop.
- Labels: sub-skills keep the `[Docs Phase X/4]` label inside `docs-lifecycle` and use their own `[ADR X/6]`-style labels only standalone. The `(per CONVENTIONS.md)` pointers are removed; the small-project rule is written inline and shared (about 5 or fewer source files, or about 500 lines or fewer, one actor).
- Module namespacing in one form (single-module repos omit `<module>/`): `docs/<module>/` for adr, diagrams, api, user-guide, runbook, postmortem and release notes, `docs/<module>/_evidence.md`, `<module>/README.md`, `<module>/CHANGELOG.md`. The `docs/[<module>/]` bracket notation is gone.
- Gap placeholders follow the reply language (`[Needs input: ...]` English, `[Cần bổ sung: ...]` Vietnamese), also in `docs-lifecycle` and the runbook and postmortem templates.
- `adr-writer`: alternatives are listed only when the user or repo names them, otherwise one `Alternatives considered: [Needs input: ...]` line; a git-ignored plan is never cited as a source.
- `user-guide-writer`: a lite form (what the app is, getting started, tasks, troubleshooting) for non-course, single-actor apps; the Report 6 template is used when the user asks for it.
- `docs-lifecycle` Phase 4 gains a mechanical `file:line` re-derivation with `grep -n` and a "no counts that rot" reminder.
- `diagram-writer`: `drawio-xml-guide.md` now matches what `drawio_gen.py` emits (160 px layer spacing, swimlane `startSize=28`, `collapsible=0`).

### Fixed
- `diagram-writer/scripts/drawio_gen.py` no longer crashes (empty `max()`) when an edge spans layers that hold no nodes; `scripts/test_drawio_gen.py` covers LR and TB.

## 0.1.0

Ten skills: `docs-lifecycle`, `readme-writer`, `diagram-writer`, `api-doc-writer`, `adr-writer`, `docs-sync-auditor`, `srs-sdd-writer`, `pm-report-writer`, `user-guide-writer`, `review2-pack-writer`, with helper scripts, `scripts/validate.py` and evals.
