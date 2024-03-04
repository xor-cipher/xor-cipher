"""Simple, reusable and optimized XOR ciphers in Python."""

__description__ = "Simple, reusable and optimized XOR ciphers in Python."
__url__ = "https://github.com/xor-cipher/xor-cipher"

__title__ = "xor_cipher"
__author__ = "nekitdev, RealistikDash"
__license__ = "MIT"
__version__ = "4.0.0"

from xor_cipher.core import (
    cyclic_xor,
    cyclic_xor_in_place,
    cyclic_xor_in_place_unsafe,
    cyclic_xor_unsafe,
    xor,
    xor_in_place,
)

__all__ = (
    "cyclic_xor",
    "cyclic_xor_in_place",
    "cyclic_xor_in_place_unsafe",
    "cyclic_xor_unsafe",
    "xor",
    "xor_in_place",
)


try:
    from xor_cipher.extension import (
        cyclic_xor,
        cyclic_xor_in_place,
        cyclic_xor_in_place_unsafe,
        cyclic_xor_unsafe,
        xor,
        xor_in_place,
    )

except ImportError:  # pragma: no cover
    pass
