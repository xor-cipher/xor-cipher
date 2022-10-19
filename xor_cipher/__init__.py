from typing import TYPE_CHECKING

if TYPE_CHECKING:
    def xor_static(content: bytes, key: int) -> bytes:
        """Creates a copy of `content` and XORs each individual byte with `key`."""

        ...

    def xor_cyclic(content: bytes, key: bytes) -> bytes:
        """Creates a copy of `content` and XORs each individual byte with the `key` cyclically."""

        ...

    def xor_cyclic_unsafe(content: bytes, key: bytes) -> bytes:
        """Same as `xor_cyclic`, however it ommits key length checks. This is faster, but only use
        when the `key` originates from a trusted source."""

        ...
else:
    from xor_cipher.cipher import xor_static
    from xor_cipher.cipher import xor_cyclic
    from xor_cipher.cipher import xor_cyclic_unsafe

def xor_static_str(
    content: str,
    key: int,
    encoding: str = "utf-8",
    errors: str = "strict",
) -> str:
    """A wrapper around `xor_static` that handles the encoding of the string."""

    return xor_static(
        content.encode(encoding=encoding, errors=errors),
        key,
    ).decode(encoding=encoding, errors=errors)

def xor_cyclic_str(
    content: str,
    key: bytes,
    encoding: str = "utf-8",
    errors: str = "strict",
) -> str:
    """A wrapper around `xor_cyclic` that handles the encoding of the string."""

    return xor_cyclic(
        content.encode(encoding=encoding, errors=errors),
        key,
    ).decode(encoding=encoding, errors=errors)
