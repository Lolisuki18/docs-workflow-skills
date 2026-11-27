# Postmortem template

Save as `docs/<module>/postmortems/YYYY-MM-DD-short-title.md` (single-module repos omit `<module>/`). Gap placeholder: `[Needs input]` in English documents, `[Cần bổ sung]` in Vietnamese ones (follow the reply language).

```markdown
# Postmortem: <short title>

- **Date of incident:** YYYY-MM-DD, <start> to <end> (<time zone>) [Needs input if unknown]
- **Status:** Draft | Reviewed
- **Severity:** <level used by the team, or [Needs input]>
- **Authors:** <roles or names given by the user>
- **Systems involved:** <services, jobs, databases>

## Summary
Two or three sentences: what broke, for whom, for how long, and how it was fixed.

## Impact
| What | Measure | Source |
|---|---|---|
| Users / requests affected | | |
| Duration | | |
| Data loss or corruption | | |
| Cost or contractual effect | | |

## Timeline
| Time (<tz>) | Event | Source |
|---|---|---|
| | Change deployed / trigger | commit `abc123`, deploy run |
| | First alert or report (detection) | |
| | Escalation | |
| | Mitigation applied | |
| | Resolved | |

## Root cause
- **Trigger:** what changed or failed (evidence: `path:line` or log line).
- **Root cause:** confirmed | likely (what would confirm it).
- **Contributing factors:** missing alert, no rollback path, unclear ownership, test gap.
- **Why safeguards did not catch it:** ...

## Detection and response
How it was detected, how long that took, what slowed the response.

## What went well
- ...

## What went badly
- ...

## Where we got lucky
- ...

## Action items
| # | Action | Type (prevent / detect / mitigate / process) | Owner | Due | How we verify it |
|---|---|---|---|---|---|
| 1 | | | [Needs input] | [Needs input] | |

## Open questions
- Evidence we could not get: ...

## Appendix
Relevant log excerpts (secrets removed), commands used, links given by the user.
```

## Style

- Past tense, plain words, no adjectives about people.
- Prefer "the deploy job ran without the migration" over "someone forgot".
- Every number has a source; every unknown is a placeholder.
