# Evals

`evals.json` holds behavioural test cases for the 13 skills: 20 positive cases (prompt, fixture description, expected behaviour, forbidden behaviour) and 2 negative cases that must not trigger any skill.

Status: **partly executed** (see Results log); the cases of the other skills are written, not executed. Structure checks are automated (`python scripts/validate.py`); behaviour must be checked by running an agent.

## How to run a case manually

1. Create the fixture described in `setup` (a small throwaway repo is enough) and install the skills.
2. Start a fresh agent session in the fixture and send `prompt` unchanged.
3. Tick every `expect` item and confirm no `must_not` item happened. Record Pass/Fail, the agent and its version, and the date.
4. For trigger problems, compare the skill that activated with `skill`; adjust that skill's `description` (keep it <= 900 characters) and rerun the negative cases.

## Using skill-creator

The `skill-creator` skill can run these prompts as evals and optimise each `description`. Feed it `prompt` and `expect` per case; keep `must_not` as grader instructions.

## Adding cases

Add a real failure you observed: one prompt, the smallest fixture that reproduces it, and one or two checkable expectations. Prefer cases about invented facts (commands, endpoints, labels, numbers) because that is the main risk this skill set exists to prevent.

## Results log

| Date | Agent / model | Case | Result | Notes |
|---|---|---|---|---|
| 2026-11-23 | Claude subagent, SKILL.md only | changelog-01 | PASS | Used the v1.0.0..v1.1.0 range, listed the `--legacy` removal found only in the diff as a breaking change, left out chore commits and listed them, no invented issue numbers. |
| 2026-11-23 | Claude subagent, SKILL.md only | runbook-01 | PASS | Commands came from the compose and workflow files, contacts and dashboards left as `[Cần bổ sung]`, destructive steps flagged, gaps (no backup, no monitoring) reported. |

Method: one run per case by a Claude subagent that was handed only the SKILL.md (and the references the skill names) and the user request, in a throwaway folder. This tests behaviour (steps, hard stops, no invented facts), not triggering: the skill was given to the agent, not chosen by it. Graded by the same model family against the case's graders or checklist, so read it as a smoke test, not a benchmark. Multi-turn scenarios were run for turn 1 only.
