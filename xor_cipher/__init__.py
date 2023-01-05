"""Simple, reusable and optimized XOR ciphers in Python."""

__description__ = "Simple, reusable and optimized XOR ciphers in Python."
__url__ = "https://github.com/xor-cipher/xor-cipher"

__title__ = "xor_cipher"
__author__ = "nekitdev, RealistikDash"
__license__ = "MIT"
__version__ = "2.4.0"

from xor_cipher.core import (
    DEFAULT_ENCODING,
    DEFAULT_ERRORS,
    FAST,
    cyclic_xor,
    cyclic_xor_in_place,
    cyclic_xor_in_place_unsafe,
    cyclic_xor_unsafe,
    cyclic_xor_string,
    cyclic_xor_string_unsafe,
    xor,
    xor_in_place,
    xor_string,
)

__all__ = (
    "DEFAULT_ENCODING",
    "DEFAULT_ERRORS",
    "FAST",
    "cyclic_xor",
    "cyclic_xor_in_place",
    "cyclic_xor_in_place_unsafe",
    "cyclic_xor_unsafe",
    "cyclic_xor_string",
    "cyclic_xor_string_unsafe",
    "xor",
    "xor_in_place",
    "xor_string",
)
