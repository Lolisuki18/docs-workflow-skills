# Mermaid (and PlantUML) Conventions

Diagram-as-code is the canonical source. Mermaid by default; PlantUML when the repo already uses it.

## 1. File layout

- Mermaid: `docs/diagrams/<type>-<subject>.md`, content layout:

````text
# <Title>
<one sentence: what it shows>

```mermaid
...
```

Evidence: `path/File.java`, `db/migrations/001_init.sql`
````
- PlantUML: `docs/diagrams/<type>-<subject>.puml` (`@startuml` ... `@enduml`).
- Type prefixes: `usecase`, `erd`, `sequence`, `activity`, `state`, `architecture`.
- Embedding in a README/SDD: paste the fenced block or link to the file. Keep one source; do not hand-edit copies.

## 2. Global conventions

- Identifiers verbatim from code. Display labels may add spaces only inside quoted labels; the id stays original.
- Avoid characters that break Mermaid: in flowchart/architecture/ERD node and edge labels, wrap labels containing `()`, `:`, `/`, `#`, `;` in double quotes; in `sequenceDiagram` messages, avoid quoting and replace `;` with `,`; use `<br/>` for line breaks; no raw `<` `>` outside quotes.
- Size limits: sequence <= 6 participants and ~20 messages; flowchart/activity <= ~15 nodes; ERD <= ~12 entities (split by module otherwise).
- Direction: `TD` for processes, `LR` for architecture/pipelines.
- One comment line `%% Evidence: <files>` at top is allowed and encouraged.
- Unknown element -> do not draw it; note `%% TODO [Cần bổ sung: ...]`.

## 3. Per type

### Use Case
Mermaid has no native use-case diagram; use `flowchart LR`:
```text
flowchart LR
  Patron([Patron])
  Admin([Administrator])
  subgraph System["Meal Ordering"]
    UC01((View Menu))
    UC02((Order a Meal))
  end
  Patron --> UC01
  Patron --> UC02
  Admin --> UC01
  UC02 -. "<<include>>" .-> UC01
```
- Actors outside the subgraph, use cases inside; actor names = roles in code/spec; use case names = verb + object.
- `<<include>>`/`<<extend>>` only if specified. Number use cases to match the SRS table (`UC01`).
- PlantUML alternative: `actor`, `usecase`, `rectangle` blocks - preferred when many actors/relations.

### ERD (logical)
```text
erDiagram
  USERS ||--o{ ORDERS : "places"
  ORDERS ||--|{ ORDER_ITEMS : "contains"
  USERS { bigint id PK
          varchar email UK
          varchar role }
```
- Entity name = real table name (keep case from the script). Columns: `type name [PK|FK|UK]`.
- Cardinality: `||` exactly one, `o|` zero-or-one, `}o` zero-or-many, `}|` one-or-many. Derive from FK nullability and uniqueness.
- Include at least PK/FK columns; add other columns when the doc is a data dictionary. Whatever is shown must exist in the script.
- Check both ways: table in script and not in diagram, table in diagram and not in script.

### Sequence
```text
sequenceDiagram
  autonumber
  actor U as Customer
  participant C as OrderController
  participant S as OrderService
  participant R as OrderRepository
  U->>C: POST /api/v1/orders
  C->>S: create(CreateOrderRequest)
  S->>R: save(order)
  R-->>S: order
  S-->>C: OrderResponse
  C-->>U: 201 Created
```
- One flow per diagram. Participants are real classes or external systems.
- Use `alt/else`, `opt`, `loop` only for branches present in code (validation failure, not-found).
- Arrow style: `->>` call, `-->>` return.

### Activity / Flowchart
```text
flowchart TD
  A([Start]) --> B[Patron books slot]
  B --> C{Slot available?}
  C -- Yes --> D[Receptionist confirms]
  C -- No --> E[System suggests another slot]
  D --> F([End])
```
- Business level, actor swimlanes via `subgraph` per actor (name = role).
- Decisions are diamonds with labelled exits; every path reaches an end node.
- Name the workflow with the same ID used in SRS/BM (e.g. `WF-01`) in the title.

### State Machine
```text
stateDiagram-v2
  [*] --> PENDING
  PENDING --> CONFIRMED: confirm()
  PENDING --> CANCELLED: cancel()
  CONFIRMED --> COMPLETED: complete()
  COMPLETED --> [*]
  CANCELLED --> [*]
```
- States = enum values / status column values verbatim. Transition label = trigger (method, endpoint or FR id).
- List states with no exit and transitions without a triggering FR as gaps in the handover.
- One diagram per main entity that has a lifecycle.

### System Architecture
```text
flowchart LR
  Browser[Web Client] -->|HTTPS| API[Backend API]
  API --> DB[(PostgreSQL)]
  API -->|SMTP| Mail[Email Service]
```
- Components from modules/compose/config. Shapes: `[ ]` service, `[( )]` database, `{{ }}` external/third-party.
- Label edges with protocol or data. Show deployment boundaries with `subgraph` (Dev/Staging/Prod) only if config proves them.
- Every third-party service in code (payment, auth, storage, AI API) must appear; no service that is not in code.

## 4. PlantUML quick notes

- Prefer for dense use-case and component diagrams. Same naming and evidence rules.
- Wrap in `@startuml`/`@enduml`; `skinparam linetype ortho` improves readability of component diagrams.
- Commit the `.puml`; rendered images are optional artifacts.

## 5. Mermaid syntax pitfalls

- `end` as a node id breaks flowcharts; use `End`/`finish`.
- Reserved words in ER attribute names: quote or rename only the display (not allowed to change the source name - note it in the handover).
- Unescaped `;` in sequence messages ends the statement; replace by `,` inside text.
- Keep one blank line between the fence and the content; do not indent the fence inside lists.
