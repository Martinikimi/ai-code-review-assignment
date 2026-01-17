def count_valid_emails(emails):
    """
    Count strings that resemble valid email addresses based on basic rules.

    Rules applied:
    - Must be a string.
    - Contains exactly one '@'.
    - Local part (before '@') is non-empty.
    - Domain part (after '@') contains at least one dot, not at start or end.
    - No spaces in the string.
    - Length between 3 and 254 characters (RFC 5321).

    Args:
        emails: List of strings to check.

    Returns:
        int: Count of strings passing the basic email format checks.
    """
    if not isinstance(emails, list):
        return 0

    count = 0
    for email in emails:
        # Ensure it's a string
        if not isinstance(email, str):
            continue

        # Length sanity (RFC 5321 max total length = 254)
        if len(email) < 3 or len(email) > 254:
            continue

        # Exactly one '@'
        if email.count("@") != 1:
            continue

        # Split into local and domain parts
        local, domain = email.split("@", 1)

        # Check local and domain non-empty
        if not local or not domain:
            continue

        # Domain must contain at least one dot, and not start/end with dot
        if "." not in domain:
            continue
        if domain.startswith(".") or domain.endswith("."):
            continue

        # No spaces allowed anywhere in the email
        if " " in email:
            continue

        # If all checks pass, count as valid
        count += 1

    return count