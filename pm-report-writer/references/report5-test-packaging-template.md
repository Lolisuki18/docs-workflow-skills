# Report 5 - Test Documentation packaging (template structure)

Extracted from `Report5_Test Documentation.docx`, `Report5_Test Report.xlsx` and `Report5_Unit Test.xls`. The Student Guide splits Report 5 into three templates:

| File | Purpose |
|---|---|
| `Report5_Unit Test` (.xls) | unit test case specification and tracking |
| `Report5_Test Report` (.xlsx) | integration, system, acceptance test cases and tracking |
| `Report5_Test Documentation` (.docx) | testing plan and consolidation of project testing information |

Milestones: Week 5 delivers the Test Documentation except Test Cases and Test Reports (II.4, II.5); Software Packages 1-3 add UT, IT and Defects List; the Full Package adds ST, IT, Defects List.

## Packaging rules (read first)

- **Package only.** Do not write or redesign test cases or the QA process. Read real outputs: test runner reports (JUnit/xUnit/TRX/pytest/jest, etc.), CI artifacts, coverage reports, existing QA spreadsheets.
- **Never invent Pass/Fail numbers**, dates, testers, test IDs or LOC. If no real run exists: `[Cần bổ sung: chưa có kết quả chạy test cho <module>]` and leave result cells empty/`Pending` as in the template; counts of Passed/Failed are not typed.
- Counts are computed from the actual result rows; show the source file for every sheet.
- Map each result to a function/feature using the real test names/paths. A result that cannot be mapped is listed under "Unmapped results", not forced into a sheet.
- Result vocabulary (Test Report): `Passed`, `Failed`, `Pending`, `N/A`. Unit test: `Passed`, `Failed`, `Untested`, with type `N`ormal / `A`bnormal / `B`oundary.

## A. Test Documentation (.docx) structure

### I. Record of Changes
`Date | A* / M, D | In charge | Change Description`

### II. Testing Documentation
1. **Scope of Testing** - template guidance: target-of-test features, functions and non-functional requirements that will or will not be tested; the stages/levels applied (Unit, Integration, System), each with in-charge, inputs/time, focus and acceptance criteria; constraints and assumptions that may affect test design, development or implementation. Modules come from the SRS.
2. **Test Strategy**
   - 2.1 Testing Types - e.g. functional, regression, security; only those really planned/run. Template guidance: for each type give **objective, technique, completion criteria**.
   - 2.2 Test Levels - matrix header: `Type of Tests | Unit | Integration | System | Acceptance`, rows = test types, cell `X` where applied.
   - 2.3 Supporting Tools - `Purpose | Tool | Vendor/In-house | Version` (from package manifests/CI: test framework, coverage tool).
3. **Test Plan**
   - 3.1 Human Resources - `Worker/Doer | Role | Specific Responsibilities/Comments`
   - 3.2 Test Environment - `Purpose | Tool | Provider | Version` (OS, browser, DB, server from config)
   - 3.3 Test Milestones - `Milestone Task | Start Date | End Date` (from the project schedule)
4. **Test Cases** - template guidance: Unit Test cases are in `Report5_Unit Test.xls`; other test cases (IT, ST, AT) are in the Test Report workbook (`Report5_Test Report`). Give the consolidated list/reference (IDs, counts).
5. **Test Reports** - template guidance: test results, statistics and the relevant test analysis. Consolidated results: totals per module with the statistics below.

## B. Test Report (.xlsx) sheets

| Sheet | Content |
|---|---|
| `Cover` | `TEST REPORT DOCUMENT`; Project Name, Project Code, Document Code (`<Project Code>_<XXX>_v<x.x>`), Creator, Issue Date, Version; Record of change table: `Effective Date | Version | Change Item | *A,D,M | Change description | Reference` |
| `Test Cases` | `TEST CASE LIST`; Project Name, Project Code, Test Environment Setup Description (Server, Database, Web Browser, ...); table `No | Function Name | Sheet Name | Description | Pre-Condition` |
| `Test Statistics` | Project Name, Project Code, Document Code (`<Project Code>_Test Report_v<x.x>`), Creator, Reviewer/Approver, Issue Date, Notes (modules in this release); table `No | Module code | Passed | Failed | Pending | N/A | Number of test cases`; `Sub total`; `Test coverage`; `Test successful coverage` |
| `Feature 1`, `Feature 2`, ... | one sheet per feature, see below |

Feature sheet header: `Feature`, `Test requirement`, `Number of TCs`, then the round summary:

| Testing Round | Passed | Failed | Pending | N/A |
|---|---|---|---|---|
| Round 1 / 2 / 3 | counts | counts | counts | counts |

Test-case table columns:
`Test Case ID | Test Case Description | Test Case Procedure | Expected Results | Pre-conditions | Round 1 | Test date | Tester | Round 2 | Test date | Tester | Round 3 | Test date | Tester | Note`
Rows are grouped under a function-name row (`Function A`...). Round cells hold `Passed/Failed/Pending/N/A`.

Formulas (from the workbook):
- Number of TCs = count of test case ID rows.
- Round counts = count of cells equal to each result in that round column.
- Sub total = sum of each column over modules.
- **Test coverage (%) = (Passed + Failed) x 100 / (Total - N/A)**
- **Test successful coverage (%) = Passed x 100 / (Total - N/A)**

## C. Unit Test (.xls) sheets

| Sheet | Content |
|---|---|
| `Guideline` | how to build and read unit test cases (see below) |
| `Cover` | `UNIT TEST DOCUMENT`; Project Name, Code, Document Code, Creator, Issue Date, Version; Record of change |
| `Functions` | `Function List`; Project Name/Code; **Normal number of Test cases/KLOC** (template value 100); Test Environment Setup Description; table `No | Requirement/Name | Class Name | Function Name | Function Code (Optional) | Sheet Name | Description | Pre-Condition` |
| `Statistics` | `UNIT TEST REPORT`; header like Test Statistics; table `No | Function code | Passed | Failed | Untested | N | A | B | Total Test Cases`; `Sub total`; `Test coverage`; `Test successful coverage`; `Normal case`, `Abnormal case`, `Boundary case` percentages |
| `Function n` | one sheet per function |
| `Example` | worked example |

Function sheet layout: `Function Code`, `Function Name`, `Created By`, `Executed By`, `Lines of code`, `Lack of test cases`; `Test requirement`; counters `Passed | Failed | Untested | N/A/B | Total Test Cases`; matrix with columns `UTCID01 ... UTCIDnn`; rows: `Condition` (`Precondition`, then inputs and their values), `Confirm` (`Return`, `Exception`, `Log message`), `Result` with `Type(N: Normal, A: Abnormal, B: Boundary)`, `Passed/Failed`, execution date. An `O` in a cell marks which value/outcome that test case uses.

Guideline sheet (full text read):
- One sheet per function; `Cover` has general information; `Functions` lists classes and functions (fill `Normal number of Test cases/KLOC` to check the unit-test count against the customer's requirement or the norm; create the function sheet before linking to it); the statistics sheet gives test coverage and test successful coverage, summarised for normal/abnormal/boundary cases. Recheck the `Sub total` formulas when functions are added.
- **Combination of test cases:** fill the LOC of the tested function and the per-KLOC norm; `Lack of test cases` shows how many are missing. If the number is short the creator explains why. If the per-KLOC norm is not recorded, `Lack of test cases` is **not calculated**. (Observed sample values: 100 LOC / 15 TCs -> -5, 300 LOC / 15 TCs -> 15, consistent with `norm x LOC/1000 - total`; verify in the file.)
- **Condition** = precondition (state that must exist before the test, e.g. a file) + input values of three types. Example for `5 <= input <= 10`: normal 6,7,8,9; boundary 5,10; abnormal -1,11,...
- **Confirmation** = expected results compared with the actual output: function return value, log messages in a log file, screen messages. Same as expected -> passed, otherwise failed.
- **Type and result:** type N/A/B chosen from the input data; result `P`/`F` (or `OK`/`NG` by team habit).
- Other fields: `Function Code` and `Function Name` update automatically from the function list; `Created By`, `Executed By`, `Lines of code`, `Test requirement` (optional).
Compute LOC from the real source only.

## D. Procedure for packaging

1. Locate real results; list files used. If none -> report and stop; do not fabricate.
2. Parse results into rows: ID/name, function/feature, result, date (from the run), tester (who ran or `CI`).
3. Fill Test Statistics / Statistics via the formulas above from the counted rows.
4. Fill document parts (II.1-II.3, 3.x) from config/manifests/schedule; unknown -> `[Cần bổ sung]`.
5. Output Markdown tables or CSV per sheet (`report5-<sheet>.csv`) for pasting into the original files.
6. Verify: Passed + Failed + Pending + N/A = Number of TCs per module; totals equal the sum of modules; coverage percentages recomputed.
