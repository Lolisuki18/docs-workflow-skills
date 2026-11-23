# Examples: good vs bad README content

Names are illustrations.

## Commands

Evidence: `package.json` has `"scripts": { "dev": "vite", "build": "vite build", "test": "vitest run" }`; CI runs `npm ci && npm test`.

Good:

````markdown
```bash
npm ci
npm run dev
```
````

Bad: `npm run start:dev` (script does not exist), `yarn install` when only `package-lock.json` exists, `docker compose up` when no compose file exists.

## Environment variables

Evidence: `.env.example` lists `DATABASE_URL=`, `JWT_SECRET=`; code reads `process.env.PORT || 3000`.

Good:

| Name | Description | Required | Default / Example |
|---|---|---|---|
| `DATABASE_URL` | Database connection string | yes | `postgres://user:pass@localhost:5432/app` (example from `.env.example`) |
| `PORT` | HTTP port | no | `3000` (`src/server.ts:9`) |

Bad: documenting `API_KEY` that no file mentions; showing a real secret; marking everything "required" without checking.

## Prerequisites

Good: "Node.js >= 20 (`engines` in `package.json`), PostgreSQL 16 (image `postgres:16` in `docker-compose.yml`)."
Bad: "Node.js (latest)" or a version found nowhere in the repo.

## Description

Good: "REST API for appointment booking in clinics. Patients book slots; receptionists confirm; doctors record visits."
Bad: "A powerful, blazing-fast, next-generation platform."

## Handover wording

Good: "Ran `npm ci` and `npm test`: install ok, 42 tests passed. Not run: Docker flow (Docker unavailable)."
Bad: "All commands tested."
