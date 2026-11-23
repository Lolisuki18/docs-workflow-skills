# Examples: good vs bad requirement content

All names are illustrations.

## Acceptance criteria

| Quality | Text |
|---|---|
| Good | "A fully booked slot cannot be selected; the confirmation email is sent within 60 seconds." (testable pass/fail) |
| Good | "Submitting the form with an empty `email` shows `MSG02` under the field and no request is sent." |
| Bad | "The booking screen is user-friendly." (not testable) |
| Bad | "The system should respond quickly." (no metric, threshold, method) |

## NFR row

Good: `NFR-02 | Performance | p95 response time of GET /api/v1/orders | <= 500 ms at 50 concurrent users | k6 script docs/perf/orders.js on staging`
Bad: `NFR-02 | Performance | fast | high | testing`

## FR with traceability

| FR | Actor | UC | Entity | API | Screen | Test |
|---|---|---|---|---|---|---|
| FR-03 Cancel order | Customer | UC05 Cancel Order | orders | `POST /api/v1/orders/{id}/cancel` | Order Details | TC-F03-01..03 |

Bad: FR with empty Actor and UC columns, or an API that is not in the controller. Empty cell = gap to list, not to fill with a guess.

## Business rule and message

Good: `BR-04 | An order can be cancelled only while status is PENDING.` (code: `OrderService.cancel` throws if status != PENDING)
Good: `MSG05 | Toast | Order cancelled | "Your order was cancelled."` (text copied from `messages.properties:57`)
Bad: invented rule "Orders are delivered within 30 minutes" with no code or spec behind it.

## Rubric result block

Good: "Rubric result: A 4/4, B 8/9, C 7/8 ... Fail: B-7 FR-05 has no actor (SRS 3.4.1). Not verifiable: C-6 staging URL unknown."
Bad: "Document meets all criteria."
