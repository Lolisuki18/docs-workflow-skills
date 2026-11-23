# Weekly Report (template structure)

Extracted from `Project Weekly Report_GroupName.xlsx`. One workbook per group; one sheet per week (template sheet name `Wx`, e.g. `W1`, `W2`).

## Header block
| Cell | Content |
|---|---|
| A1 | `PROJECT REPORT` |
| A2 / B2 | `Group` / group name |
| A3 / B3 | `Week` / `dd/mm/yyyy-dd/mm/yyyy` |

## I. Status Report
| # | Project Task | In-charge | Status | Notes (Work Item in Details) |
|---|---|---|---|---|
Tasks worked on during the week. Status values in the template: `Pending`, `In Progress` (add `Done` or the tracker's real states).

## II. Project Issues
| # | Project Issue | Owner | Status | Notes (Solution, Suggestion, etc.) |
|---|---|---|---|---|

## III. Next Week Plan
| # | Project Work Item | In-charge | Deadline | Notes (Task Details, etc.) |
|---|---|---|---|---|

## IV. Other Project Masters/Suggestions
| # | Project Matter/Suggestions | Raised By | Date | Notes |
|---|---|---|---|---|

(The heading spelling "Masters" is as in the template; keep it.)

## How to fill (evidence)
1. Week range: from the user or the semester calendar; use Monday-Sunday only if the team's calendar says so.
2. Section I from `git log --since=<start> --until=<end>` (authors, subjects, merged PRs), closed/open issues, tracking sheet changes. Group commits by task; `In-charge` = commit/PR author mapped to the team's member codes (ask if mapping unknown). Status from the tracker/PR state, not from guessing.
3. Section II from open issues/blockers the user reports and Issues sheet rows.
4. Section III from backlog items planned for next week (WBS `Planned` iteration) and the user's plan. Deadlines are real dates or `[Cần bổ sung]`.
5. Section IV from notes the user supplies.
6. Never pad rows or invent tasks to make the week look full. An empty section is allowed: write `None this week` only if the user confirms.

## Output
One Markdown table per section under the header block, or CSV per section (`weekly-W<n>-status.csv`, etc.), ready to paste into sheet `Wx`.
