# Notes (Optional)

## Task 1 – Average Order Value

### Assumptions Made

1. **Status matching** – Only exact string `"cancelled"` (two L's) is considered a cancelled order; variations like `"canceled"` or `"CANCELLED"` are treated as valid.

2. **Numeric types** – Only `int` and `float` are accepted as valid amounts; string numbers (e.g., `"100"`) are skipped, as automatic conversion could mask data‑quality issues.

3. **Return value for no valid data** – Returning `0.0` was chosen over raising an exception to allow batch processing to continue.,

4. **Silent skipping** – Malformed entries (non‑dict, missing keys, wrong types) are skipped without warning; in production, logging might be added.

### Design Trade‑Offs Considered

- **`Decimal` vs `float`** – Used `float` for simplicity and compatibility; `Decimal` would be more accurate for monetary values but adds complexity.

- **Early exit on empty input** – Could return `0.0` immediately, but kept loop‑based logic for consistency with non‑empty but all‑invalid cases.

- **Validation strictness** – Could raise specific exceptions (`ValueError`, `KeyError`) for invalid input, but chose fail‑silent to support resilience in batch jobs.

### Limitations

- Does not handle localized or varied cancellation statuses.

- Non‑numeric strings are ignored, not converted (e.g., `"150.50"` → skipped).

- Large lists are processed in O(n) time but all in memory; streaming is not supported.

### Alternative Approach (Not Implemented)

A more functional style using comprehension:

```python
valid_amounts = [
    o.get("amount") for o in orders
    if isinstance(o, dict)
    and o.get("status") != "cancelled"
    and isinstance(o.get("amount"), (int, float))
]
if not valid_amounts:
    return 0.0
return sum(valid_amounts) / len(valid_amounts)




## Task 2 – Count Valid Emails

### Assumptions Made
1. **Validity definition** – “Valid email” is interpreted as a string meeting basic format rules, not full RFC‑5322 compliance.

2. **No regex preference** – Used explicit string checks for readability and transparency over regex.

3. **Length limits** – Enforced RFC‑5321 maximum length (254 chars) and a minimum of 3 chars to filter obvious non‑emails.

4. **Domain dot requirement** – Required at least one dot in domain, and dot cannot be at start/end of domain (common invalid patterns).

5. **Space prohibition** – Disallowed spaces anywhere in the email, as they are invalid in standard email addresses.

### Design Trade‑Offs Considered

**Strictness vs. simplicity** – Could have added more checks (e.g., valid TLDs, quoted local parts, plus‑addressing), but chose minimal set that catches most invalid patterns.

**Regex vs. manual checks** – Regex would be shorter but harder to debug; explicit checks make validation steps transparent.

**Return value for invalid input** – Non‑list input returns 0; considered raising `TypeError` but kept fail‑silent for batch processing resilience.

### Limitations

Does not validate against official RFC‑5322 grammar (e.g., comments, quoted strings, IP‑literal domains).

Does not check DNS MX records or whether domain actually exists.

Unicode and internationalized email addresses are handled only to the extent Python strings allow; no special normalization.

### Alternative Approach (Not Implemented)

Using a lightweight third‑party library like `email-validator` would be robust but violates “no external dependencies” implied constraint.

Alternatively, a single regex could replace manual checks but would reduce readability and debuggability.


## Task 3 – Aggregate Valid Measurements

### Assumptions Made

**Valid measurement definition** – Any value convertible to `float` via `float(v)` without raising `ValueError` or `TypeError`.

 `None` is **explicitly skipped** before conversion attempt, keeping logic clear

**Return value for no valid data** – `0.0` chosen over raising an exception to allow batch processing to continue.

**Error tolerance** – Non‑convertible entries are silently skipped; in production, logging might be added for debugging.

### Design Trade‑Offs Considered

**Explicit `None` check** – Could rely solely on `try‑except`, but explicit check clarifies intent and slightly improves performance.

`float()` vs. `Decimal` – Used `float` for simplicity and broad compatibility; `Decimal` would be more precise for financial data but requires all inputs to be `Decimal`‑compatible.

**Handling `NaN`/`inf`** – `float("NaN")` and `float("inf")` are allowed; could filter them out, but left as‑is unless spec prohibits.

**Input type flexibility** – Accepts any iterable, not just lists; but does not handle non‑iterable input (fails gracefully with `TypeError`).

### Limitations

Boolean values `True`/`False` convert to `1.0`/`0.0`, which may be unintended depending on context.

Complex numbers or custom objects with `__float__` method are accepted if `float()` works.

No protection against overflow for extremely large numbers.

Skipping invalid entries silently may hide data‑quality issues.

### Alternative Approach (Not Implemented)

Using `filter()` and `map()` with a safe conversion helper:

```python
def safe_float(x):
    try:
        return float(x)
    except (ValueError, TypeError):
        return None

valid = filter(None, map(safe_float, values))