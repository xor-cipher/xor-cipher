from setuptools import setup

# Cython MUST be imported after setuptools.
from Cython.Build import cythonize

def read_readme() -> str:
    with open("README.md") as f:
        return f.read()

setup(
    name= "xor_cipher",
    version= "1.0.0",
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
        "Development Status :: 3 - Alpha",
        "Topic :: Database",
    ],
    python_requires=">=3.6",

    url= "https://github.com/RealistikDash/xor_cipher",
    project_urls= {
        "GitHub: repo": "https://github.com/RealistikDash/xor_cipher",
        "GitHub: issues": "https://github.com/RealistikDash/xor_cipher/issues"
    },

    long_description_content_type= "text/markdown",
    long_description= read_readme(),

    ext_modules= cythonize(
        "xor_cipher/cipher.pyx",
        #annotate= True,
    ),
    packages=["xor_cipher"],
)