def calculate_average_order_value(orders):
    """
    Calculate the average order value for non-cancelled orders.

    Args:
        orders: List of dicts, each with keys "status" and "amount".

    Returns:
        float: Average amount of non-cancelled orders.
               Returns 0.0 if there are no valid orders.
    """
    total = 0.0
    valid_count = 0

    for order in orders:
        # Skip entries that are not dictionaries
        if not isinstance(order, dict):
            continue

        # Safe access to keys
        status = order.get("status")
        amount = order.get("amount")

        # Include only non-cancelled orders with numeric amounts
        if status != "cancelled" and isinstance(amount, (int, float)):
            total += amount
            valid_count += 1

    # Avoid division by zero
    if valid_count == 0:
        return 0.0

    return total / valid_count
