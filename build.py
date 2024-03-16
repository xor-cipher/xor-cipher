from pathlib import Path
from subprocess import call
from sys import executable as INTERPRETER_STRING
from typing import Any, Dict, Sequence, TypeVar
from zipfile import ZipFile

from entrypoint import entrypoint

SetupKeywords = Dict[str, Any]

S = TypeVar("S", bound=SetupKeywords)

INTERPRETER_PATH = Path(INTERPRETER_STRING)

ROOT = Path(__file__).parent

RESULT_NAME = "xor_cipher"
RESULT_PATH = ROOT / RESULT_NAME

SHARED_OBJECT = ".so"
PYTHON_DLL = ".pyd"

EXTENSIONS = frozenset((SHARED_OBJECT, PYTHON_DLL))

POETRY = "poetry"
RUN = "run"
MATURIN = "maturin"
BUILD = "build"
INTERPRETER = "-i"
OUTPUT = "-o"
RELEASE = "-r"

TARGET = "target"
WHEELS = "wheels"
WHEEL = ".whl"

OUTPUT_PATH = ROOT / TARGET / WHEELS

FAILED_TO_FIND_EXTENSIONS = "failed to find extensions"


def build_command() -> Sequence[str]:
    return (
        MATURIN,
        BUILD,
        RELEASE,
        INTERPRETER,
        INTERPRETER_PATH.as_posix(),
        OUTPUT,
        OUTPUT_PATH.as_posix(),
    )


def build(setup_keywords: S) -> S:
    result = call(build_command())

    if result:
        return setup_keywords

    wheel = WHEEL
    extensions = EXTENSIONS

    output_path = OUTPUT_PATH
    result_path = RESULT_PATH

    for path in output_path.iterdir():
        if path.suffix == wheel:
            with ZipFile(path) as zip_file:
                for string_path in zip_file.namelist():
                    archive_path = Path(string_path)

                    if archive_path.suffix in extensions:
                        file_path = result_path / archive_path.name

                        with zip_file.open(string_path) as file:
                            file_path.write_bytes(file.read())

    return setup_keywords


@entrypoint(__name__)
def main() -> None:
    build({})
