try:
    from xor_cipher_core import cyclic_xor, cyclic_xor_in_place, xor, xor_in_place

except ImportError:  # pragma: no cover
    pass

__all__ = ("xor", "cyclic_xor", "xor_in_place", "cyclic_xor_in_place")
