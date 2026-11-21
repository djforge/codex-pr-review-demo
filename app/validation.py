import re


SKU_PATTERN = re.compile(r"^[A-Z0-9]+(?:-[A-Z0-9]+)*$")


def valid_sku(value: str) -> bool:
    """Accept normalized, non-empty SKU values."""
    return bool(value and len(value) <= 40 and SKU_PATTERN.fullmatch(value))
