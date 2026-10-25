#!/usr/bin/env python3
"""Check educational notebook integrity and run the provided demonstrations.

No external dependencies required: uses the Python standard library only.
Interactive input examples receive harmless scripted values so CI cannot block.
An incomplete exercise is expected to print a reminder rather than raise.
"""
from __future__ import annotations

import contextlib
import io
import json
import pathlib
import re
import sys
import traceback

ROOT = pathlib.Path(__file__).resolve().parents[1]
NOTEBOOKS = {
    "Python_1_lecture_code.ipynb": 20,
    "Python_2_lecture_code.ipynb": 10,
    "Pokedex_capstone.ipynb": 0,
}
THAI_PATTERN = re.compile(r"[\u0e00-\u0e7f]")
INVALID_HEADING = re.compile(r"^#{1,6}(?!\s|#)", flags=re.MULTILINE)


def scripted_input(prompt: str = "") -> str:
    """Deterministic answers for existing introductory input examples."""
    prompt = prompt.lower()
    if "name" in prompt or "product" in prompt:
        return "Eevee"
    if "height" in prompt:
        return "165.5"
    if "price" in prompt:
        return "25.5"
    return "10"


def validate_notebook(filename: str, minimum_labs: int) -> int:
    path = ROOT / filename
    nb = json.loads(path.read_text(encoding="utf-8"))
    if nb.get("nbformat") != 4:
        raise AssertionError(f"{filename}: expected notebook format version 4")
    if not isinstance(nb.get("cells"), list):
        raise AssertionError(f"{filename}: missing cells list")
    lab_count = 0
    executed = 0
    namespace: dict = {"__name__": "__main__", "input": scripted_input}
    for index, cell in enumerate(nb["cells"], start=1):
        source = cell.get("source", [])
        source = "".join(source) if isinstance(source, list) else source
        if THAI_PATTERN.search(source):
            raise AssertionError(f"{filename}, cell {index}: untranslated Thai source")
        if cell.get("cell_type") == "markdown":
            lab_count += source.count("### Training Lab ")
            if INVALID_HEADING.search(source):
                raise AssertionError(f"{filename}, cell {index}: malformed Markdown heading")
        elif cell.get("cell_type") == "code":
            if cell.get("outputs"):
                raise AssertionError(f"{filename}, cell {index}: committed execution output")
            if cell.get("execution_count") is not None:
                raise AssertionError(f"{filename}, cell {index}: stale execution count")
            try:
                program = compile(source, f"{filename}#cell{index}", "exec")
                with contextlib.redirect_stdout(io.StringIO()):
                    exec(program, namespace)
                executed += 1
            except Exception as exc:
                tb = traceback.format_exc()
                raise AssertionError(
                    f"{filename}, code cell {index} failed ({type(exc).__name__}: {exc})\n{tb}"
                ) from exc
        else:
            raise AssertionError(f"{filename}, cell {index}: unknown cell type")
    if lab_count < minimum_labs:
        raise AssertionError(f"{filename}: expected {minimum_labs} training labs, found {lab_count}")
    print(f"PASS {filename}: {len(nb['cells'])} cells, {executed} executed, {lab_count} labs")
    return executed


def main() -> int:
    count = 0
    for name, required in NOTEBOOKS.items():
        count += validate_notebook(name, required)
    print(f"Validated and executed {count} instructional code cells.")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (AssertionError, OSError, ValueError) as err:
        print(f"FAILED: {err}", file=sys.stderr)
        sys.exit(1)
