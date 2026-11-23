# Examples: good vs bad API documentation

Names are illustrations; take real ones from code.

## Endpoint entry

Evidence: `OrderController.java:42 @PostMapping("/orders")` under `@RequestMapping("/api/v1")`; `CreateOrderRequest` has `@NotEmpty @Size(max=50) List<Item> items`; `SecurityConfig.java:31` requires role `CUSTOMER`; `GlobalExceptionHandler.java:18` maps `MethodArgumentNotValidException` to 400 with `{code, message, details}`.

Good:

````markdown
### POST /api/v1/orders

Creates an order for the authenticated user.  _(OrderController.java:42)_

- **Auth:** Bearer JWT, role `CUSTOMER` _(SecurityConfig.java:31)_

| Field | Type | Required | Constraints |
|---|---|---|---|
| items | array<Item> | yes | not empty, max 50 |

| Status | Meaning | Body |
|---|---|---|
| 201 | Created | `OrderResponse` |
| 400 | Validation failed | `ErrorResponse` (`VALIDATION_ERROR`) |
| 401 | Missing/invalid token | `ErrorResponse` |
````

Bad:
- Path `/orders` without the `/api/v1` prefix.
- "Auth: required" with no role, or "public" because the name sounds public.
- Status `404` listed although no code path returns it.
- Field `couponCode` documented but not in the DTO.
- Example payload with `items: []` while the validator forbids empty.

## Handover wording

Good: "Documented 23 of 23 endpoints found (routers: `src/routes/*.ts`). Not verifiable: behaviour behind the API gateway (config not in repo)."
Bad: "All endpoints documented."
