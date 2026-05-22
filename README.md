# pyqbe

Python bindings for [QBE](https://c9x.me/compile/), a compiler backend that generates optimized assembly. Pass QBE IR as a string, get assembly back — no external QBE binary needed.

> **Note:** This is a hobby project.

## What is this?

[QBE](https://c9x.me/compile/) is a small, fast compiler backend (think LLVM but ~10k lines of C). `pyqbe` wraps it as a Python package so you can generate assembly programmatically without shelling out to a binary.

```python
import pyqbe

ir = """
function w $add(w %a, w %b) {
@start
    %c =w add %a, %b
    ret %c
}
"""

asm = pyqbe.compile(ir)
print(asm)
```

## Why?

If you're building a compiler, DSL, or code generation tool in Python, you need a backend. QBE gives you optimized assembly for free — `pyqbe` makes it accessible from Python without any system dependencies.

## Targets

QBE supports:

- `amd64` — Linux (SysV ABI) and macOS
- `arm64` — Linux and macOS (Apple Silicon)
- `riscv64` — Linux
- `amd64_win` — Windows (64-bit, requires UNIX toolchain)

## Installation

```bash
pip install pyqbe
```

### From source

Requires a C compiler and `g++` with pybind11.

```bash
git clone --recurse-submodules https://github.com/Marpuriganesh/pyqbe
cd pyqbe
pip install .
```

> `--recurse-submodules` is required — QBE is included as a git submodule.

## Status

> **Early development.** API is not stable.

- [x] QBE as git submodule
- [ ] `wrapper/qbe_api.c` — FILE* shim + C entry point
- [ ] `wrapper/binding.cpp` — pybind11 glue
- [ ] `meson.build` — build config
- [ ] GitHub Actions + cibuildwheel for prebuilt wheels
- [ ] Windows scenario (deferred)

## How it works

QBE's `parse()` function takes a `FILE*`. `pyqbe` wraps this with a thin shim that turns a Python string into an in-memory `FILE*` (`fmemopen` on Linux/macOS, `tmpfile` fallback on Windows), calls QBE's internals directly, and captures the assembly output — all in-process.

```
Python string (QBE IR)
        ↓
   string_to_file()        ← FILE* shim
        ↓
   qbe parse() + emit()    ← QBE internals
        ↓
   assembly string
```

## Related

- [QBE](https://c9x.me/compile/) — the compiler backend this wraps
- [LowPy](https://gitlab.com/my-compiler/lowpy-python) — systems programming language using pyqbe as its backend

## License

QBE is MIT licensed. `pyqbe` wrapper code is also MIT licensed.