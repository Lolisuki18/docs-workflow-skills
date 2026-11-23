# Project Tracking workbook (template structure)

Extracted from `Report3_Project Tracking.xlsx`. Started in Week 3 together with Report 3 (Product Backlog + draft Iteration Backlogs) and updated with every iteration. The Student Guide says the team may convert it to Google Sheets or track the same information in GitLab/Trello/Asana.

Four sheets: **WBS, Issues, Defects, Q&A**. Keep sheet names and column names exactly.

## Sheet `WBS`
Title cell: `PROJECT WORK BREAKDOWN STRUCTURE`.

| # | Function/Screen | Feature | Level* | Function/Screen Details | Planned | Status |
|---|---|---|---|---|---|---|

- `#`: running number (template formula `=ROW()-8`; in text output just 1, 2, 3...).
- `Function/Screen`: screen or function name = SRS screen/function name. Sample values (Home Page, User Login...) are illustrations.
- `Feature`: grouping (sample groups: Common, Public, Marketing, Admin) = SRS feature.
- `Level*`: `Simple` / `Medium` / `Complex`.
- `Planned`: `Iteration n` (sample: Iteration 1-4).
- `Status`: `Pending` (sample default); real states: take from the team's tracker.

Complexity rule from the sheet footnote - rate by number of fields on the screen or number of transactions:

| Level | Fields | Transactions |
|---|---|---|
| simple | <= 7 | <= 3 |
| medium | <= 15 | <= 7 |
| complex | > 15 | > 7 |

`fields` = screen components or database table fields; `transactions` = action buttons, user or database transactions. Count them from the real screen/code, show counts if asked.

## Sheet `Issues`
Title: `PROJECT ISSUES`.

| # | Issue | Potential Impact | Priority | Owner | Open Date | Close Date | Status | Notes |
|---|---|---|---|---|---|---|---|---|

Template defaults: Priority `Medium`, Status `Open`. Owner = member short code (sample style `HuyNMG`) - use the team's real codes.

## Sheet `Defects`
Title: `PROJECT DEFECTS`.

| Feature | Function/Screen | Tester | Defect Description | Assign To | Status | Notes |
|---|---|---|---|---|---|---|

Template default Status `Pending`. Defects come from real test runs/bug reports only. Must be consistent with Report 5 failed results and Defect list thresholds at Review 2/Defense (no open Critical/High).

## Sheet `Q&A`
Title: `PROJECT Q&A`.

| Date | Question | By | Priority | Status | Note (answer, other notes) |
|---|---|---|---|---|---|

Defaults: Priority `Medium`, Status `Open`.

## Filling rules
- Source rows from SRS features/screens, backlog/issue tracker, real defect reports. No filler rows; leave the table with only real rows.
- WBS `Feature`/`Function/Screen` strings equal SRS and Report 2 WBS names.
- Planned iteration matches the schedule (Report 2).
- Output as one Markdown table or CSV per sheet (`tracking-WBS.csv`, `tracking-Issues.csv`, `tracking-Defects.csv`, `tracking-QA.csv`).
