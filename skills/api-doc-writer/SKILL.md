---
name: api-doc-writer
description: Generates API specifications (Markdown or OpenAPI 3.x) by reading real routers, controllers, DTOs, validators and auth middleware, including status codes, error codes and realistic example payloads taken from the code. Use when the user says "document the API", "write API docs", "generate OpenAPI / Swagger", "list endpoints", "API reference", "tài liệu API", "viết đặc tả API", "liệt kê endpoint", "sinh OpenAPI". Do NOT use for README (readme-writer), diagrams (diagram-writer), decision records (adr-writer), end-user guides (user-guide-writer), or for checking existing API docs against code (docs-sync-auditor). When the API table is part of an SDD, srs-sdd-writer calls this skill.
---

# api-doc-writer

Turns real server code into an accurate API specification. If the code does not say it, the doc does not say it.

## Hard rules

- Every endpoint, field, status code and error code must trace to a source location. Record `file:line` in your evidence list.
- Never invent endpoints, parameters, headers, enum values, error codes or rate limits. Unknown -> `[Cần bổ sung: ...]`.
- Example payloads must conform to the real DTO/validator constraints. Use obviously fake values (`user@example.com`, `"string"`), never real personal data or secrets.
- No promotional text. One factual sentence per endpoint summary.

## Workflow

### 1. Locate the surface

| Stack hint | Where endpoints live |
|---|---|
| Express/Fastify/Koa/Nest | route files, `@Controller`/`@Get` decorators, `app.use` mounts (resolve prefixes!) |
| Spring | `@RestController`, `@RequestMapping` (class + method prefix), `@ControllerAdvice` |
| ASP.NET | `[ApiController]`, `[Route]`, minimal API `MapGet/MapPost` |
| Django/DRF/FastAPI/Flask | `urls.py`, viewsets, routers, `@app.get` |
| Go/Rust/PHP | handler registration (`mux.Handle`, `Router`, `Route::`) |
| Existing spec | `openapi.*`, `swagger.*` - treat as a claim to verify, not as truth |

Resolve **full paths** (global prefix + controller prefix + method path + version).

### 2. Extract per endpoint

- Method, full path, handler name.
- Path / query / header / body parameters: name, type, required, constraints (from validators: length, regex, min/max, enum).
- Request body DTO and response DTO (field list with types and nullability).
- Auth: middleware/guard/annotation -> required role/scope, token type. "Public" only if no guard applies.
- Status codes actually returned (explicit `res.status`, `ResponseEntity`, thrown exceptions mapped by the global handler).
- Error body shape from the global exception handler and the list of error codes/messages defined in code.
- Pagination, sorting, filtering parameters if implemented.
- Side effects worth knowing (sends email, emits event) only if visible in the handler/service.

### 3. Choose the format

- Ask once if unspecified: Markdown (default for human reading, SDD tables) or OpenAPI 3.x (tooling).
- Markdown: `docs/api/README.md` index + one file per resource group, or a single file when < ~20 endpoints.
- OpenAPI: `docs/api/openapi.yaml`, OpenAPI 3.0.x or 3.1.x consistent with the repo's tooling. Use `components/schemas` for DTOs, `components/securitySchemes` for auth, shared `responses` for the error shape. Validate syntax if a validator is available; otherwise say it was not validated.

### 4. Markdown template per endpoint

````markdown
### POST /api/v1/orders

Creates an order for the authenticated user.

- **Auth:** Bearer JWT, role `CUSTOMER`  _(OrderController.java:42, SecurityConfig.java:31)_
- **Request body:** `CreateOrderRequest`

| Field | Type | Required | Constraints |
|---|---|---|---|
| items | array<OrderItem> | yes | size 1..50 |

**Example request**
```json
{ "items": [{ "productId": 1, "quantity": 2 }] }
```

**Responses**

| Status | Meaning | Body |
|---|---|---|
| 201 | Created | `OrderResponse` |
| 400 | Validation failed | `ErrorResponse` (code `VALIDATION_ERROR`) |
| 401 | Missing/invalid token | `ErrorResponse` |
````

Group by resource. Start the doc with: base URL (only if in config, else `[Cần bổ sung]`), auth overview, common error shape, error-code table, pagination convention.

### 5. Summary table (for SDD or index)

`Method | Path | Description | Auth | Request DTO | Response DTO | Source`. Keep names identical to the code so `srs-sdd-writer` can trace Feature -> API.

## Self-check before handover

- [ ] Endpoint count in doc equals count found in code (state both numbers).
- [ ] Full paths include all prefixes.
- [ ] Every documented status code is produced by code; every thrown exception mapped.
- [ ] Required/optional flags come from validators/DTO annotations.
- [ ] Auth column derived from guards/middleware, not from naming.
- [ ] Example payloads pass the documented constraints.
- [ ] Open `[Cần bổ sung]` items listed.

## Handover message

State: format and files written, endpoints documented vs found, evidence files read, anything unverifiable (e.g. behaviour behind a gateway not in the repo).
