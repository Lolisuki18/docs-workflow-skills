# Evals

`evals.json` holds behavioural test cases for the 10 skills: 17 positive cases (prompt, fixture description, expected behaviour, forbidden behaviour) and 2 negative cases that must not trigger any skill.

Status: **written, not executed yet**. Structure checks are automated (`python scripts/validate.py`); behaviour must be checked by running an agent.

## How to run a case manually

1. Create the fixture described in `setup` (a small throwaway repo is enough) and install the skills.
2. Start a fresh agent session in the fixture and send `prompt` unchanged.
3. Tick every `expect` item and confirm no `must_not` item happened. Record Pass/Fail, the agent and its version, and the date.
4. For trigger problems, compare the skill that activated with `skill`; adjust that skill's `description` (keep it <= 900 characters) and rerun the negative cases.

## Using skill-creator

The `skill-creator` skill can run these prompts as evals and optimise each `description`. Feed it `prompt` and `expect` per case; keep `must_not` as grader instructions.

## Adding cases

Add a real failure you observed: one prompt, the smallest fixture that reproduces it, and one or two checkable expectations. Prefer cases about invented facts (commands, endpoints, labels, numbers) because that is the main risk this skill set exists to prevent.
