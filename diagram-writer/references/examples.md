# Examples: good vs bad diagram output

All names below are illustrations. Real names come from the project.

## ERD

Evidence: `V1__init.sql` creates `orders(id PK, user_id FK -> users.id NOT NULL, status)` and `users(id PK, email UNIQUE)`.

Good (matches the script exactly, cardinality from FK + NOT NULL):

```text
erDiagram
  users ||--o{ orders : "places"
  users  { bigint id PK
           varchar email UK }
  orders { bigint id PK
           bigint user_id FK
           varchar status }
```

Bad - and why:
- `User ||--|| Order` : renamed tables (`User`, `Order`), wrong cardinality (FK is many-to-one).
- Extra entity `Payment` that has no table in the script -> invented element.
- Missing `status` column although it exists -> data dictionary drifts.

## State machine

Evidence: `enum OrderStatus { PENDING, CONFIRMED, COMPLETED, CANCELLED }`; `confirm()` PENDING->CONFIRMED, `complete()` CONFIRMED->COMPLETED, `cancel()` PENDING->CANCELLED.

Good:

```text
stateDiagram-v2
  [*] --> PENDING
  PENDING --> CONFIRMED: confirm()
  PENDING --> CANCELLED: cancel()
  CONFIRMED --> COMPLETED: complete()
  COMPLETED --> [*]
  CANCELLED --> [*]
```

Bad: draws `CONFIRMED --> CANCELLED` because "it makes sense" (no code path), omits `CANCELLED`, or labels transitions "next" instead of the trigger. Report such gaps in the handover instead of drawing them.

## Sequence

Good: participants are real classes (`OrderController`, `OrderService`, `OrderRepository`), messages are real method names, one `alt` only where the service has an `if/throw`.

Bad: generic participants (`Frontend`, `Backend`, `DB`) with no relation to code, or 12 participants in one diagram.

## Handover wording

Good: "Elements matched to evidence: 14/14. Omitted: `Payment` (no table, no entity class found). Not rendered (no Mermaid CLI available)."
Bad: "Diagram is accurate and complete."
