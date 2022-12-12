# `xor-cipher`

[![License][License Badge]][License]
[![Version][Version Badge]][Package]
[![Downloads][Downloads Badge]][Package]

[![Documentation][Documentation Badge]][Documentation]
[![Check][Check Badge]][Actions]
[![Test][Test Badge]][Actions]

> *Simple, reusable and optimized XOR ciphers in Python.*

`xor-cipher` is a fast implementation of the XOR cipher written using Cython.
Our tests show that it can be `1000x` faster than pure Python implementations.
It has been optimized to breeze through datasets of any size.

## Installing

**Python 3.7 or above is required.**

### pip

Installing the library with `pip` is quite simple:

```console
$ pip install xor-cipher
```

Alternatively, the library can be installed from source:

```console
$ git clone https://github.com/xor-cipher/xor-cipher.git
$ cd xor-cipher
$ python -m pip install .
```

### poetry

You can add `xor-cipher` as a dependency with the following command:

```console
$ poetry add xor-cipher
```

Or by directly specifying it in the configuration like so:

```toml
[tool.poetry.dependencies]
xor-cipher = "^2.3.1"
```

Alternatively, you can add it directly from the source:

```toml
[tool.poetry.dependencies.xor-cipher]
git = "https://github.com/xor-cipher/xor-cipher.git"
```

## Examples

### Simple Cipher

Use the `xor` function to perform the simple XOR cipher:

```python
>>> from xor_cipher import xor
>>> xor(b"Hello, world!", 0x42)
b"\n'..-nb5-0.&c"
```

### Cyclic Cipher

Use the `cyclic_xor` function to perform the cyclic XOR variation:

```python
>>> from xor_cipher import cyclic_xor
>>> cyclic_xor(b"Hello, world!", b"BLOB")
b"\n)#.-`o5->#&c"
```

### String Cipher

`xor-cipher` provides `xor_string` and `cyclic_xor_string` as variations of
`xor` and `cyclic_xor`, respectively:

```python
>>> from xor_cipher import xor_string
>>> xor_string("Hello, world!", 0x42)
"\n'..-nb5-0.&c"
```

### In-Place Cipher

There are functions to perform the XOR cipher in-place, on `bytearray` instances:

```python
>>> from xor_cipher import xor_in_place
>>> data = bytearray(b"Hello, world!")
>>> xor_in_place(data, 0x42)
>>> data
bytearray(b"\n'..-nb5-0.&c")
```

## Documentation

You can find the documentation [here][Documentation].

## Support

If you need support with the library, you can send an [email][Email].

## Changelog

You can find the changelog [here][Changelog].

## Security Policy

You can find the Security Policy of `xor-cipher` [here][Security].

## Contributing

If you are interested in contributing to `xor-cipher`, make sure to take a look at the
[Contributing Guide][Contributing Guide], as well as the [Code of Conduct][Code of Conduct].

## License

`xor-cipher` is licensed under the MIT License terms. See [License][License] for details.

[Email]: mailto:support@xor-cipher.com

[Actions]: https://github.com/xor-cipher/xor-cipher/actions

[Changelog]: https://github.com/xor-cipher/xor-cipher/blob/main/CHANGELOG.md
[Code of Conduct]: https://github.com/xor-cipher/xor-cipher/blob/main/CODE_OF_CONDUCT.md
[Contributing Guide]: https://github.com/xor-cipher/xor-cipher/blob/main/CONTRIBUTING.md
[Security]: https://github.com/xor-cipher/xor-cipher/blob/main/SECURITY.md

[License]: https://github.com/xor-cipher/xor-cipher/blob/main/LICENSE

[Package]: https://pypi.org/project/xor-cipher
[Documentation]: https://xor-cipher.github.io/xor-cipher

[License Badge]: https://img.shields.io/pypi/l/xor-cipher
[Version Badge]: https://img.shields.io/pypi/v/xor-cipher
[Downloads Badge]: https://img.shields.io/pypi/dm/xor-cipher

[Documentation Badge]: https://github.com/xor-cipher/xor-cipher/workflows/docs/badge.svg
[Check Badge]: https://github.com/xor-cipher/xor-cipher/workflows/check/badge.svg
[Test Badge]: https://github.com/xor-cipher/xor-cipher/workflows/test/badge.svg
