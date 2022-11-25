# Changelog

<!-- changelogging: start -->

## 2.0.0 (2022-10-24)

Complete rework of the entire API.

### Features

- Add `cyclic_xor_string_unsafe` as the part of the *unsafe* API.
- Add `xor_in_place`.
- Add `cyclic_xor_in_place`.
- Add `cyclic_xor_in_place_unsafe`.

### Changes

- Bump the minimal Python version to `3.7`.
- Rename `xor_static -> xor`.
- Rename `xor_cyclic -> cyclic_xor`.
- Rename `xor_cyclic_unsafe -> cyclic_xor_unsafe`.
- Rename `xor_static_str -> xor_string`.
- Rename `xor_cyclic_str -> cyclic_xor_string`.
  This function now expects `key` of type `str` instead of `bytes`.

## 1.0.3 (2022-10-20)

### Features

- Add `xor_cyclic_unsafe`, introducing the *unsafe* API.

### Fixes

- Add key length check in `xor_cyclic`.

## 1.0.2 (2022-09-19)

### Fixes

- Fix type annotations.

## 1.0.1 (2022-09-19)

### Fixes

- Fix extension builds.

## 1.0.0 (2022-09-19)

Initial release.
