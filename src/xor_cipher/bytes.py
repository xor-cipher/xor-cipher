from typing import Literal

__all__ = ("MIN_BYTE", "MAX_BYTE", "expect_byte", "is_not_byte")

MIN_BYTE: Literal[0] = 0
"""The minimum byte value."""

MAX_BYTE: Literal[255] = 255
"""The maximum byte value."""

EXPECTED_BYTE = "expected `byte` (`int` in range `[0, 255]`)"


def is_not_byte(value: int) -> bool:
    return value < MIN_BYTE or value > MAX_BYTE


def expect_byte(value: int) -> int:
    """Ensures the [`int`][int] value provided is in `[0, 255]` range.

    Arguments:
        value: The value to check.

    Raises:
        ValueError: If the given value is outside the expected range.
    """
    if is_not_byte(value):
        raise ValueError(EXPECTED_BYTE)

    return value
