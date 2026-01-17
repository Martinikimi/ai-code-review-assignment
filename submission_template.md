# AI Code Review Assignment (Python)

## Candidate
- Name: Martin Ikimi Kimani
- Approximate time spent:

---

# Task 1 — Average Order Value

## 1) Code Review Findings
### Critical bugs
-
Wrong divisor — The function divides by total orders (len(orders)) instead of only non-cancelled orders, producing mathematically incorrect averages.

Division by zero — Empty input list leads to ZeroDivisionError.

Unsafe key access — Missing "status" or "amount" keys cause KeyError.

Type errors — Non-numeric amount values (e.g., strings) raise TypeError during addition.

### Edge cases & risks
- 
All orders cancelled — Returns 0.0, which could be misinterpreted as “average is zero” rather than “no valid data.”

Non-dict items in list — Causes KeyError or TypeError during iteration.

Status string variations — Only exact match "cancelled" is excluded; "canceled", "CANCELLED", or other variants are treated as valid.

Negative or zero amounts — Allowed unless business rules forbid; function should handle them correctly.

Input not a list — Passing a non-iterable (e.g., None, integer) breaks iteration; passing a non-list iterable (e.g., tuple) may work but len() could fail.

Large datasets — While time complexity is O(n), memory usage could be high if orders is a generator (converted to list by len() in original code).

### Code quality / design issues
- 
Lack of input validation — Assumes ideal data; real-world data often contains missing keys, wrong types, or malformed entries.

Poor error handling — Crashes on expected edge cases instead of graceful degradation.

Misleading AI explanation — States “correctly excludes cancelled orders” but excludes them only from sum, not divisor.

No documentation — Missing docstring, parameter descriptions, or return type clarification.

Inconsistent return type — Uses float division (/) but no indication in function contract; may surprise callers expecting integer division in some contexts.



## 2) Proposed Fixes / Improvements
### Summary of changes
- 
Introduce valid_count — Count only non-cancelled orders with numeric amounts; use this as divisor.

Safe key access — Replace order["key"] with order.get("key") to avoid KeyError.

Type checking — Ensure amount is int or float before addition.

Graceful degradation — Skip non-dict entries and invalid data silently.

Handle zero valid orders — Return 0.0 when valid_count == 0 (covers empty input and all-cancelled).

Add documentation — Include docstring with parameter and return description.

### Corrected code
See `correct_task1.py`

> Note: The original AI-generated code is preserved in `task1.py`.

 ### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?

Empty list — Verify returns 0.0 (no crash, meaningful default).

All cancelled orders — Confirm returns 0.0 (indicates no valid data).

Mixed valid/cancelled orders — Ensure divisor counts only non-cancelled orders (critical logic fix).

Malformed data — Missing keys, non-dict items, non-numeric amounts → should be skipped silently.

Large input — Performance remains linear; no memory issues with iteration.

Negative/zero amounts — If allowed, ensure they are included in average calculation.

Non‑list iterables — Tuples, generators should work (if iterable and support len() or iteration).

Status edge cases — "cancelled" vs "canceled", case sensitivity, None status

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates average order value by summing the amounts of all non-cancelled orders and dividing by the number of orders. It correctly excludes cancelled orders from the calculation.

### Issues in original explanation
- 
Factually incorrect — It says “dividing by the number of orders” but should be “dividing by the number of non-cancelled orders.”

Overlooks errors — Fails to mention division‑by‑zero risk, missing‑key errors, or type safety.

Misleading claim — States it “correctly excludes cancelled orders,” but they are excluded only from the sum, not the divisor.

### Rewritten explanation
- 
This function calculates the average order value for non‑cancelled orders by summing their amounts and dividing by the count of such orders. It safely ignores malformed entries, missing keys, and non‑numeric values, returning 0.0 when no valid orders exist.

## 4) Final Judgment

Decision: Request Changes

Justification: The original code contains critical logical errors (wrong divisor) and lacks robustness (crashes on empty/malformed input). The proposed fixes are minimal, safe, and preserve the intended functionality without over‑engineering.

Confidence & unknowns: High confidence in identified issues. Unknowns include business rules on status variants ("canceled"), whether negative amounts are allowed, and if Decimal precision is required for monetary values. Assumed exact match "cancelled" per original spec.
---



# Task 2 — Count Valid Emails

## 1) Code Review Findings
### Critical bugs
- 

### Edge cases & risks
- 

### Code quality / design issues
- 

## 2) Proposed Fixes / Improvements
### Summary of changes
- 

### Corrected code
See `correct_task2.py`

> Note: The original AI-generated code is preserved in `task2.py`. 


### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function counts the number of valid email addresses in the input list. It safely ignores invalid entries and handles empty input correctly.

### Issues in original explanation
- 

### Rewritten explanation
- 

## 4) Final Judgment
- Decision: Approve / Request Changes / Reject
- Justification:
- Confidence & unknowns:

---

# Task 3 — Aggregate Valid Measurements

## 1) Code Review Findings
### Critical bugs
- 

### Edge cases & risks
- 

### Code quality / design issues
- 

## 2) Proposed Fixes / Improvements
### Summary of changes
- 

### Corrected code
See `correct_task3.py`

> Note: The original AI-generated code is preserved in `task3.py`.

### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?


## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates the average of valid measurements by ignoring missing values (None) and averaging the remaining values. It safely handles mixed input types and ensures an accurate average

### Issues in original explanation
- 

### Rewritten explanation
- 

## 4) Final Judgment
- Decision: Approve / Request Changes / Reject
- Justification:
- Confidence & unknowns:
