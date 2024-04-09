// results
use pyo3::PyResult;
// errors
use pyo3::exceptions::PyValueError;
// guards
use pyo3::marker::Python;
// types
use pyo3::types::{PyByteArray, PyBytes, PyInt, PyModule};
// macros
use pyo3::{pyfunction as py_function, pymodule as py_module, wrap_pyfunction as wrap_py_function};

mod rust;

static EXPECTED_BYTE: &'static str = "expected `byte` (`int` in range `[0, 255]`)";

#[py_function]
fn xor<'py>(python: Python<'py>, data: &'py PyBytes, key: &'py PyInt) -> PyResult<&'py PyBytes> {
    let rust_key = key
        .extract()
        .map_err(|_| PyValueError::new_err(EXPECTED_BYTE))?;

    if rust_key == 0 {
        return Ok(data);
    }

    let mut rust_data = data.as_bytes().to_owned();

    rust::xor_in_place(&mut rust_data, rust_key);

    Ok(PyBytes::new(python, &rust_data))
}

#[py_function]
fn cyclic_xor<'py>(python: Python<'py>, data: &'py PyBytes, key: &'py PyBytes) -> &'py PyBytes {
    let rust_key = key.as_bytes();

    if rust_key.len() == 0 {
        return data;
    }

    let mut rust_data = data.as_bytes().to_owned();

    rust::cyclic_xor_in_place(&mut rust_data, rust_key);

    PyBytes::new(python, &rust_data)
}

#[py_function]
fn xor_in_place(data: &PyByteArray, key: &PyInt) -> PyResult<()> {
    let rust_key = key
        .extract()
        .map_err(|_| PyValueError::new_err(EXPECTED_BYTE))?;

    let rust_data = unsafe { data.as_bytes_mut() };

    rust::xor_in_place(rust_data, rust_key);

    Ok(())
}

#[py_function]
fn cyclic_xor_in_place(data: &PyByteArray, key: &PyBytes) {
    let rust_key = key.as_bytes();

    let rust_data = unsafe { data.as_bytes_mut() };

    rust::cyclic_xor_in_place(rust_data, rust_key);
}

#[py_module]
fn extension(python: Python<'_>, module: &PyModule) -> PyResult<()> {
    module.add_function(wrap_py_function!(xor, python)?)?;
    module.add_function(wrap_py_function!(cyclic_xor, python)?)?;
    module.add_function(wrap_py_function!(xor_in_place, python)?)?;
    module.add_function(wrap_py_function!(cyclic_xor_in_place, python)?)?;

    Ok(())
}
