from xor_cipher.cipher import xor_static
from xor_cipher.cipher import xor_cyclic

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
