from typing import Literal
from annotated_types import Ge, Le
from typing_extensions import Annotated, TypeIs

__all__ = ("MIN_BYTE", "MAX_BYTE", "byte", "check_byte")

MIN_BYTE: Literal[0] = 0
"""The minimum byte value."""

MAX_BYTE: Literal[255] = 255
"""The maximum byte value."""

byte = Annotated[int, Ge(MIN_BYTE), Le(MAX_BYTE)]
"""Represents byte values ([`int`][int] values in range `[0, 255]`)."""

EXPECTED_BYTE = "expected `byte` (`int` in range `[0, 255]`)"


def is_byte(value: int) -> TypeIs[byte]:
    """Checks if the `value` is [`byte`][xor_cipher.typing.byte].

    Arguments:
        value: The value to check.

    Returns:
        Whether the given value is [`byte`][xor_cipher.typing.byte].
    """
    return MIN_BYTE <= value <= MAX_BYTE


def check_byte(value: int) -> None:
    """Ensures the `value` is [`byte`][xor_cipher.typing.byte].

    Arguments:
        value: The value to check.

    Raises:
        ValueError: If the given value is *not* [`byte`][xor_cipher.typing.byte].
    """
    if not is_byte(value):
        raise ValueError(EXPECTED_BYTE)
