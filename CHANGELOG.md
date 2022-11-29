# Changelog

<!-- changelogging: start -->

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

Complete rework of the entire API.

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
