---
name: docs-sync-auditor
description: Audits existing documentation (README, API docs, diagrams, SRS/SDD, User Guide) against the source code or the latest git diff, read-only by default, outputting a discrepancy table (doc_file:line vs code_file:line) with Critical/Medium/Minor severity and editing only after user confirmation. Its BM02 Standard Mode runs the course's verbatim 7-check prompt for the Review 2 self-review. Use when the user says "audit docs", "check docs against code", "docs out of date", "find mismatches", "run BM02 self-review", "kiểm tra tài liệu có lệch code không", "đối chiếu docs với code", "rà soát SRS/SDD", "chạy prompt BM02". Do NOT use for writing docs (readme-writer, srs-sdd-writer), filling Review 2 forms (review2-pack-writer), or auditing code quality or security.
---

# docs-sync-auditor

Finds where documentation no longer matches reality. Read-only unless the user confirms a fix.

## Hard rules

- **Read-only by default.** Do not create, edit or delete any file until the user confirms specific findings. The only allowed write before confirmation is the report file the user explicitly asked for.
- Every finding needs both sides of the evidence: `doc_file:line` and `code_file:line` (or `git diff` hunk). No evidence on one side -> say which side is missing; do not guess.
- Report what is, not what should be. Do not invent code behaviour; anything not verifiable from the repo is listed under "Not verifiable".
- Concise, factual wording. No opinions about writing quality.

## Modes

| Mode | When | Reference |
|---|---|---|
| **Default Audit** | docs vs current code, or docs vs a git range | this file |
| **BM02 Standard Mode** | user wants the Review 2 self-review run | `references/bm02-standard-prompt.md` |

If the user's request does not say which, ask one question.

## Default Audit workflow

### 1. Scope
Confirm: which docs (README, API docs, diagrams, SRS/SDD, User Guide, ADRs, tracking), which code (whole repo, a module, or `git diff <base>..HEAD` / last N commits). If a diff is given, start from changed files and trace to the docs that mention them.

### 2. Build the claim list
Extract verifiable claims from each doc, with `file:line`:

| Doc | Claims to check |
|---|---|
| README | commands, scripts, ports, env vars, versions, folder tree, links |
| API docs | method + full path, params, auth, status/error codes, DTO fields |
| Diagrams | tables/columns/FKs, classes, participants, states and transitions, components, actors |
| SRS | actors vs roles, use cases vs routes/services, FR vs implementation, business rules, messages |
| SDD | packages, tables, class/sequence participants, tech declarations |
| User Guide | screen names, menu/button labels, routes, role permissions |
| ADR | decision still reflected in manifests/config |

### 3. Verify against code
For each claim find the source (grep, read, parse manifests, read migrations). Classify: **Match**, **Mismatch**, **Missing in docs** (code feature undocumented), **Missing in code** (documented, not found), **Not verifiable**.

### 4. Severity

| Level | Definition |
|---|---|
| **Critical** | Following the doc fails or misleads materially: wrong run/setup command, wrong endpoint/auth/required field, ERD missing or wrong for real tables, state machine missing used states, documented feature absent or removed, UI label/route that does not exist |
| **Medium** | Incomplete or partly wrong but workable: missing optional param, outdated version, undocumented new endpoint/field/role, diagram lacks a minor entity, stale link to existing alternative |
| **Minor** | Cosmetic or low impact: naming casing, typos in identifiers, outdated wording, ordering, redundant text |

### 5. Report
Output (in chat, and to a file only if asked, e.g. `docs/audit/docs-sync-<date>.md`):

```
Summary: N findings - Critical a, Medium b, Minor c. Claims checked: X. Not verifiable: Y.

| ID | Severity | Doc (doc_file:line) | Code (code_file:line) | Discrepancy | Suggested fix |
|----|----------|---------------------|-----------------------|-------------|---------------|
| D-01 | Critical | README.md:42 `npm run start:dev` | package.json:12 (script is `dev`) | Command does not exist | Change to `npm run dev` |
```
Then lists: **Missing in docs**, **Not verifiable** (with reason), **Scope covered / not covered**.

Sort Critical -> Medium -> Minor. Use stable IDs `D-01...`.

### 6. Fix phase (only after confirmation)
Ask which IDs to fix (all Critical / selected IDs / none). For each approved ID: edit only the cited doc location, keep style, re-verify against the code, and list changed lines. Never change source code to match docs. If code seems wrong rather than the doc, report it as a question, not a fix.

## BM02 Standard Mode

Purpose: produce the raw finding table that goes into BM02 section 3.

1. Load `references/bm02-standard-prompt.md`. Use the text between the BEGIN/END markers **verbatim** as the instruction. Do not paraphrase, translate, shorten or add checks.
2. Inputs: the proposed final registration form, SRS, SDD with diagrams, source code and DB script in the repo at the tag/commit the user names (`review-2`). If a required input is missing, say so in the output and continue with the rest; do not invent it.
3. Output exactly what the prompt asks: one table `ID | Category | Location | Finding | Severity (High/Medium/Low) | Evidence`, then the 5 most important findings.
4. **Hard rules for this mode**
   - Findings are **never edited, merged, reworded, reordered or deleted** by this skill or by later steps. The team only adds a `Team response` column outside the AI output.
   - Anything that cannot be verified from the repository must be **declared explicitly** as "cannot be verified from the repository" with the reason - not guessed and not silently dropped.
   - Read-only: change no file. Do not auto-fix findings.
   - IDs follow `SR-01`, `SR-02`, ...
5. Record run metadata for BM02 section 1: AI tool and model (if known to you; otherwise `[Cần bổ sung: model]`), run date, repo tag/commit (read from git), registration form version used.
6. After the run, offer (do not do) the follow-ups: team responses (`Fixed (commit)` / `Kept (reason)` / `Planned (owner, due)`), and copying High findings marked Kept/Planned to BM01 section 5 - this belongs to `review2-pack-writer`.

## Self-check before handover

- [ ] Each finding has doc and code evidence (or an explicit "missing" side).
- [ ] Severity follows the definitions above (BM02 mode: the AI's own High/Medium/Low, untouched).
- [ ] Nothing was modified without confirmation.
- [ ] "Not verifiable" items are listed with reasons.
- [ ] Counts in the summary equal the table rows.
