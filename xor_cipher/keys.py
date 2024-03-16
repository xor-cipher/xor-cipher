from annotated_types import Interval
from typing_extensions import Annotated

__all__ = ("MIN_KEY", "MAX_KEY", "byte", "validate_key")

MIN_KEY = 0x00
"""The minimum key value."""

MAX_KEY = 0xFF
"""The maximum key value."""

EXPECTED_KEY = f"expected key in range [{MIN_KEY}, {MAX_KEY}]"

byte = Annotated[int, Interval(ge=MIN_KEY, le=MAX_KEY)]
"""Represents byte keys."""


def validate_key(key: int) -> None:
    """Validates the byte key.

    Arguments:
        key: The key to validate.
    """
    if key < MIN_KEY:
        raise ValueError(EXPECTED_KEY)

    if key > MAX_KEY:
        raise ValueError(EXPECTED_KEY)
