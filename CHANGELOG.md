# Changelog

<!-- changelogging: start -->

## [5.0.0](https://github.com/xor-cipher/xor-cipher/tree/v5.0.0) (2024-06-26)

### Changes

- The core was rewritten in Rust. ([#55](https://github.com/xor-cipher/xor-cipher/pull/55))

### Removals

- Removed `unsafe` functions. ([#55](https://github.com/xor-cipher/xor-cipher/pull/55))

## 4.0.0 (2024-03-04)

### Changes

- Added byte key validation.

### Removals

- Removed `xor_string`, `cyclic_xor_string` and `cyclic_xor_string_unsafe`.
- `DEFAULT_ENCODING` and `DEFAULT_ERRORS` are not used anymore, therefore they were removed as well.

### Internal

- Improved typing.

## 3.2.1 (2024-02-26)

No significant changes.

## 3.2.0 (2024-02-25)

### Internal

- Improved typing.

## 3.1.0 (2024-01-15)

### Internal

- Dropped Python 3.7 support.

## 3.0.1 (2023-06-02)

No significant changes.

## 3.0.0 (2023-01-05)

- Moved `xor_cipher.extension` imports into `xor_cipher` prelude instead of `xor_cipher.core`.
  This makes it easy to generate proper documentation and
  allows to test both python and cython implementations.

## 2.4.0 (2023-01-05)

### Internal

- Migrated to using `setuptools`.

## 2.3.1 (2022-12-12)

### Features

- Exported *in-place* functions.

## 2.3.0 (2022-10-29)

### Changes

- Transferred the project to the [`xor-cipher`](https://github.com/xor-cipher) organization.

## 2.2.2 (2022-10-25)

### Features

- Fixed the memory leak for functions which created copies of the initial buffer.

## 2.2.1 (2022-10-25)

### Features

- Optimized the process of memory copying (both in performance and memory usage).

## 2.2.0 (2022-10-25)

### Features

- Added `py.typed` file to signify that the library is typed.

## 2.1.0 (2022-10-25)

No significant changes.

## 2.0.0 (2022-10-24)

### Features

- Added `cyclic_xor_string_unsafe` as the part of the *unsafe* API.
- Added `xor_in_place`.
- Added `cyclic_xor_in_place`.
- Added `cyclic_xor_in_place_unsafe` as the part of the *unsafe* API.

### Changes

- Bumped the minimal Python version to `3.7`.
- Renamed `xor_static -> xor`.
- Renamed `xor_cyclic -> cyclic_xor`.
- Renamed `xor_cyclic_unsafe -> cyclic_xor_unsafe`.
- Renamed `xor_static_str -> xor_string`.
- Renamed `xor_cyclic_str -> cyclic_xor_string`.
  This function now expects `key` of type `str` instead of `bytes`.

## 1.0.3 (2022-10-20)

### Features

- Added `xor_cyclic_unsafe`, introducing the *unsafe* API.

### Fixes

- Added key length check in `xor_cyclic`.

## 1.0.2 (2022-09-19)

### Fixes

- Fixed type annotations.

## 1.0.1 (2022-09-19)

### Fixes

- Fixed extension builds.

## 1.0.0 (2022-09-19)

Initial release.
