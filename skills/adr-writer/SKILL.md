---
name: adr-writer
description: Writes Architecture Decision Records into docs/adr/NNN-ten-quyet-dinh.md with Context, Options Considered, Decision and Consequences/Trade-offs, grounded in the actual code, config and git history. Use when the user says "write an ADR", "record this decision", "why did we choose X", "document architecture decision", "viết ADR", "ghi lại quyết định kiến trúc", "lưu quyết định thiết kế". Do NOT use for README (readme-writer), API docs (api-doc-writer), diagrams (diagram-writer), SRS/SDD design sections (srs-sdd-writer), Review 2 Key Design Decisions table (review2-pack-writer), or for judging whether a decision is correct.
---

# adr-writer

Records one architectural decision per file so the team can later see what was decided, what else was considered, and the cost.

## Hard rules

- One decision per ADR. Split compound decisions.
- Document the decision **actually in effect** (verify in code/config) or explicitly proposed. Do not invent history, dates, authors, benchmarks or rejected alternatives that nobody considered. If the user did not name alternatives and none are visible in the repo/git log, ask, or write `[Cần bổ sung: options considered]`.
- No advocacy language. State trade-offs on both sides.
- Never rewrite an accepted ADR's decision. To change a decision, add a new ADR that supersedes it and update the old one's Status line only.

## Workflow

1. **Scope the decision.** Ask (once) if unclear: what is decided, who decided, when, status (Proposed / Accepted / Deprecated / Superseded by NNN).
2. **Gather evidence.** Where the decision shows up: dependency manifests, config files, infrastructure files, module layout, migration history, `git log -S`/`git log --follow` around the introducing commit, PR text or issue links if available. Record sources.
3. **Check existing ADRs.** List `docs/adr/`; use the next number `NNN` (3 digits, no gaps reuse). If the folder has a different convention (e.g. `0001-`), follow it. Look for overlap or contradiction and link related ADRs.
4. **Write** `docs/adr/NNN-ten-quyet-dinh.md` (kebab-case, ASCII, no diacritics, max ~6 words).
5. **Update the index** `docs/adr/README.md` (table: `NNN | Title | Status | Date`). Create it if missing.
6. **Self-check** and hand over.

## Template

```markdown
# NNN. <Decision title as a statement>

- **Status:** Proposed | Accepted | Deprecated | Superseded by [NNN](NNN-....md)
- **Date:** YYYY-MM-DD
- **Deciders:** <names or roles; [Cần bổ sung] if unknown>
- **Related:** <ADR links, issues, FR IDs, diagrams>

## Context

<Problem and forces: requirements, constraints (team skills, deadline, budget, infrastructure),
current state in the code with `path` references. Facts only, 5-12 lines.>

## Options Considered

### Option 1: <name>
- Description: ...
- Pros: ...
- Cons: ...

### Option 2: <name>
- ...

## Decision

We will <chosen option>, because <reasons tied to the Context>.
<Scope: what it applies to and what it does not.>

## Consequences / Trade-offs

- **Positive:** ...
- **Negative / costs:** ...
- **Risks and how they are checked or mitigated:** ...
- **Follow-ups:** <migrations, tasks, ADRs to write>
```

## Quality bar

- Context explains *why a decision was needed*, not a tech tutorial.
- At least 2 real options (the "do nothing" option counts only if genuinely considered).
- Decision sentence names the concrete technology/pattern and its scope.
- Consequences include at least one real cost.
- Every claim about the codebase has a path reference.

## Typical ADR topics (for prompting the user)

database choice, monolith vs modular vs services, auth mechanism, state management, API style (REST/GraphQL), message broker, hosting/deploy model, ORM vs raw SQL, third-party service selection, branching and CI strategy.

## Handover message

Report file path, number assigned, status, sources read, `[Cần bổ sung]` items, and any older ADR that this one overlaps with or should supersede (do not edit it without confirmation).
