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
