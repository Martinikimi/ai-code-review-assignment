def average_valid_measurements(values):
    """
    Calculate the average of values convertible to float, ignoring None and invalid entries.

    Args:
        values: Iterable of values (may include None, strings, numbers, etc.).

    Returns:
        float: Average of convertible values, or 0.0 if none exist.
    """
    total = 0.0
    valid_count = 0

    for v in values:
        # Skip None explicitly
        if v is None:
            continue

        # Try converting to float; skip on failure
        try:
            num = float(v)
            total += num
            valid_count += 1
        except (ValueError, TypeError):
            # Non‑convertible value (e.g., "abc", [], {})
            continue

    # Avoid division by zero
    if valid_count == 0:
        return 0.0

    return total / valid_count