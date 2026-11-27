# Doc Routing Map - course branches (B) and (D)

Used in Phase 1 of `docs-lifecycle` only when the project has SEP490 / SWP490 course context. Branches (A), (C) and (E) are in `doc-routing-map.md`.

## Branch (B) - SDLC project reports

| Report | Skill | Template source |
|---|---|---|
| Report 1 Project Introduction | `pm-report-writer` | `references/report1-intro-template.md` |
| Report 2 PMP + Schedule | `pm-report-writer` | `references/report2-pmp-schedule-template.md` |
| Report 3 SRS | `srs-sdd-writer` | `references/report3-srs-template.md` |
| Report 4 SDD | `srs-sdd-writer` | `references/report4-sdd-template.md` |
| Report 5 Test packaging (from real test results) | `pm-report-writer` | `references/report5-test-packaging-template.md` |
| Report 6 Release Package & User Guides | `user-guide-writer` | `references/report6-user-guide-template.md` |
| Report 7 Final Project Report | `pm-report-writer` | `references/report7-final-template.md` |
| Weekly Report | `pm-report-writer` | `references/weekly-report-template.md` |
| Project Tracking (WBS / Issues / Defects / Q&A) | `pm-report-writer` | `references/report3-tracking-template.md` |

Report 7 aggregates Reports 1-6: when requested, check the sources are current first (route through the corresponding skills).

## Branch (D) - Review 2 Package

| User intent | Skill | Output |
|---|---|---|
| Prepare Review 2 files, Design Brief, Commitment, Record of Changes, "hồ sơ Review 2", BM01-BM04 | `review2-pack-writer` | BM01-BM04 content, cross-check report, naming and checklist |

Review 2 depends on branches (A)-(C): SRS/SDD (with 4 required diagram types), self-review run, repo tag `review-2`. Check these exist before drafting forms.
