# Runbook template

Save as `docs/runbook.md` (or `docs/ops/<system>.md`). Keep sections in this order so readers always find things in the same place.

```markdown
# Runbook - <system name>

Last verified: <date> by <who> against <commit or tag>
Environments: <names from the repo; [Cần bổ sung] if unknown>

## 1. Quick index
| Symptom | Go to |
|---|---|
| Site or API unreachable | 5.1 |
| Error rate high | 5.2 |
| Slow responses | 5.3 |
| Cannot deploy / deploy failed | 4.1, 4.2 |

## 2. System sheet
| Component | Purpose | Run command / image | Port | Health check | Logs |
|---|---|---|---|---|---|
| <name> | ... | `<from compose/CI>` | ... | `<endpoint or command>` | `<where>` |

Dependencies: <database, queue, third-party APIs and what happens when each is down>
Configuration: <env var names and where they are set; secrets by name and store>

## 3. Access and contacts
| Role | Who | How to reach |
|---|---|---|
| Owner | [Cần bổ sung] | |
| On-call | [Cần bổ sung] | |

## 4. Routine procedures
### 4.1 Deploy
Pre-checks: <green CI, correct branch/tag, backup taken>
Steps: 1. `<command>` -> expected: <output>  2. ...
Verify: <health check, smoke test>
### 4.2 Roll back
When to roll back: <criteria>
Steps: ...
Cannot be rolled back: <migrations that drop data, with the backup used instead>
### 4.3 Migrate / back up / restore / rotate a secret / scale
...

## 5. Incident playbooks
### 5.1 <Symptom>
Confirm: <command or dashboard, expected vs bad output>
Likely causes (from this repo): <cause with `path` reference>
Steps: 1. ... (flag destructive steps: WARNING)
Verify recovery: ...
Escalate when: <time or condition> to <role>

## 6. After an incident
- [ ] Timeline written (detected, mitigated, resolved)
- [ ] Root cause and contributing factors
- [ ] Follow-up tasks with owners
- [ ] Runbook updated where it was wrong or missing a step

## 7. Known gaps
<Missing health checks, alerts, backups, rollback paths noticed while writing>
```

## Style

- One action per numbered step; imperative verbs.
- Show the exact command in a code block and what success looks like.
- Say which environment a command touches; never leave it implicit.
- Prefer a link to the source script over copying a long script.
