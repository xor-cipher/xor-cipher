from setuptools import setup, Extension
import os

def read_readme() -> str:
    with open("README.md") as f:
        return f.read()

cythonise = os.environ.get("CYTHONISE")

extension = "c" if not cythonise else "pyx"

cy_extensions = [
    Extension("xor_cipher.cipher", [f"xor_cipher/cipher.{extension}"]),
    Extension("xor_cipher", ["xor_cipher/__init__.py"]),
]

if cythonise:
    from Cython.Build import cythonize
    extensions = cythonize(cy_extensions)
else:
    extensions = cy_extensions

setup(
    name= "xor_cipher",
    version= "1.0.2",
    description= "A simple, reusable, optimised XOR cipher for Python. ",
    license= "MIT",
    classifiers= [
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.6",

    url= "https://github.com/RealistikDash/xor_cipher",
    project_urls= {
        "GitHub: repo": "https://github.com/RealistikDash/xor_cipher",
        "GitHub: issues": "https://github.com/RealistikDash/xor_cipher/issues"
    },

    long_description_content_type= "text/markdown",
    long_description= read_readme(),

    ext_modules= extensions,
    packages=["xor_cipher"],
)