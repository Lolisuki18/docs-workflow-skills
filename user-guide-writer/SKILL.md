---
name: user-guide-writer
description: Writes Report 6 (Release Package & User Guides) - deliverable package, installation guide and role-based user manual - in friendly end-user language by reading the real frontend screens, routes, menus and labels, and marks every spot that needs an image with [Screenshot: description + area to circle in red]. Use when the user says "user guide", "user manual", "Report 6", "installation guide", "how-to for end users", "hướng dẫn sử dụng", "tài liệu người dùng", "viết Report 6", "hướng dẫn cài đặt cho người dùng", "manual theo vai trò". Do NOT use for developer README (readme-writer), API docs (api-doc-writer), SRS/SDD (srs-sdd-writer), PM reports, weekly/tracking, test reports (pm-report-writer), Review 2 forms (review2-pack-writer), or docs-vs-code audits (docs-sync-auditor).
---

# user-guide-writer

Writes the user-facing guide from what the interface actually contains.

## Hard rules

- **Read the real UI before writing.** Routes, page components, menu/nav definitions, form fields, button text, i18n/message files, role guards. Never invent a button, menu, tab, field, route or message. A label not found in code -> `[Cần bổ sung: label of <control> on <screen>]`.
- **No backend vocabulary** toward end users: avoid API, endpoint, database, table, JWT, token, server, payload, ORM, status code. Say "the system saves your order", "you will see an error message". (Installation guide for administrators may use technical terms; keep them in 2.x only.)
- **Screenshots are placeholders**, never fabricated images: `[Screenshot: <screen name> - <what is visible> - circle in red: <control/area>]`.
- Friendly, direct, second person ("Select **Save**"), short sentences, one action per step. No marketing language.
- Separate flows **by role**. Show a feature only to roles that can use it (from route guards/permissions), and say what the other roles will see (e.g. no menu item).
- Read `references/report6-user-guide-template.md` first; keep its headings and numbering.

## Workflow

1. **Scope.** Which release/iteration, which roles, language of the guide (default English as the report template; ask if Vietnamese is wanted - labels still quoted exactly as shown in the UI).
2. **Discover the UI** (evidence list `screen -> file:line`):
   - Route table / router config -> screen list and URLs (URLs only if users must type them).
   - Navigation components -> menu structure per role.
   - Page components -> headings, form fields (label, required marker, hints), buttons, tables (column names), dialogs.
   - i18n/message files -> exact success/error messages.
   - Guards/permissions -> who sees what.
   - Mobile/desktop apps: screens/activities/storyboards and their strings resources.
3. **Build a role x screen map.** One row per screen; columns = roles (X = can use). Mismatch with SRS 3.1.3 Screen Authorization -> report it, do not hide it.
4. **Identify workflows** (end-to-end tasks users perform) from SRS use cases/main workflows and routes. Order by the user's journey: sign in -> main tasks -> account/profile.
5. **Draft** following the template: 1 Deliverable Package, 2 Installation Guides, 3 User Manual (3.1 Overview, 3.2... one section per workflow, grouped by role).
6. **Add screenshot placeholders** at: each new screen, each form before submit, each result/confirmation, each error message the guide mentions.
7. **Self-check** and hand over.

## Step format

```text
**Task: Place an order** (role: Customer)

1. Open **Products** in the top menu.
   [Screenshot: Products page - product list with Add to cart buttons - circle in red: the Products menu item]
2. Select **Add to cart** next to the product you want.
3. Select **Cart**, then **Checkout**.
   Result: you see "<exact success message from the app>".
```

For each task include: purpose, role, what you need first, numbered steps with exact labels in bold, expected result, common problems with the real message text and what to do.

## Installation Guides (2.x)

- 2.1 System Requirements: from manifests/Docker/config; for end users of a hosted web app, list supported browsers only if declared somewhere, else `[Cần bổ sung]`.
- 2.2 Installation Instruction: reuse verified commands (see `readme-writer`); configuration values by name, never real secrets.
- Deliverable Package (1): real files with version/tag; omit rows not delivered.

## Self-check before handover

- [ ] Every button/menu/field/tab/message quoted exists in code (evidence list); none invented.
- [ ] No backend terms in section 3.
- [ ] Each workflow is under the correct role; role/screen map matches guards.
- [ ] Each step is one action; each key step has `[Screenshot: ...]` with a red-circle target.
- [ ] Steps reproduce a real path through the app (routes exist, order is possible).
- [ ] Template headings preserved; Record of Changes row added.
- [ ] `[Cần bổ sung]` items listed.

## Handover message

File written, roles and workflows covered, screens read, number of screenshot placeholders, labels not found in code, deviations between guards and SRS authorization, what was not verified (the app was not run unless you ran it).
