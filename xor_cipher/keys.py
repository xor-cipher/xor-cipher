from annotated_types import Interval
from typing_extensions import Annotated

__all__ = ("ZERO", "BYTE", "byte", "validate_key")

ZERO = 0x00
"""The minimum key value."""

BYTE = 0xFF
"""The maximum key value."""

EXPECTED_KEY = f"expected key in range [{ZERO}, {BYTE}]"

byte = Annotated[int, Interval(ge=ZERO, le=BYTE)]
"""Represents byte keys."""


def validate_key(key: byte) -> None:
    """Validates the byte key.

    Arguments:
        key: The key to validate.
    """
    if key < ZERO:
        raise ValueError(EXPECTED_KEY)

    if key > BYTE:
        raise ValueError(EXPECTED_KEY)
