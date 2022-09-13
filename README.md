# xor-cipher
A simple, reusable, optimised XOR cipher for Python.

## What is xor-cipher
xor-cipher is a fast implementation of the XOR cipher written using Cython. Our tests show that it can in some cases be >1000x faster than pure Python implementations.
It has been optimised to breeze through datasets of any size..

It features the implementations of the cyclic XOR cipher (key of any size) and the static XOR cipher (single-byte key).

Alongside this, it offers a simple string API which wraps around the fast Cython internals.

## Example
A demonstration of the features of this library.

### Examples working with bytes

Cyclic XOR Example

```py
from xor_cipher import xor_cyclic

content = b'0\n\x1e\x14\x00^X\x18\x1d\n\x03\x16Y'
key = b"xor"

decoded = xor_cyclic(content, key)
print(decoded)
>>> b'Hello, world!'
```

Static XOR Example

```py
from xor_cipher import xor_static

content = b'Yt}}~=1f~c}u0'
key = 0x11

decoded = xor_static(content, key)
print(decoded)
>>> b'Hello, world!'
```

### Examples working with strings
Exquivalent functions exist for working with string content. These functions are `xor_cyclic_str` and `xor_static_str`.
They additionally offer arguments to handle encoding.
