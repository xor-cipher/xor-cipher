from hypothesis import strategies

from xor_cipher.keys import BYTE, ZERO

binary_strategy = strategies.binary()
bytes_strategy = strategies.integers(ZERO, BYTE)
