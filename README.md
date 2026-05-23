# pyqbe

Python bindings for [QBE](https://c9x.me/compile/), a compiler backend that generates optimized assembly. Pass QBE IR as a string, get assembly back — no external QBE binary needed.

> **Note:** This is a hobby project. API is not stable.

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

# Explicit target
asm = pyqbe.compile(ir, pyqbe.Target.ARM64_APPLE)
```

## Why?

If you're building a compiler, DSL, or code generation tool in Python, you need a backend. QBE gives you optimized assembly for free — `pyqbe` makes it accessible from Python without any system dependencies.

## Installation

```bash
pip install pyqbe
```

Prebuilt wheels are available for:

| Platform | Architecture |
|----------|-------------|
| Linux | x86-64, ARM64, RISC-V 64 |
| macOS | x86-64, Apple Silicon (ARM64) |
| Windows | x86-64 |

### From source

Requires a C compiler, `g++`, and pybind11.

```bash
git clone --recurse-submodules https://gitlab.com/my-compiler/pyqbe
cd pyqbe
pip install .
```

> `--recurse-submodules` is required — QBE is included as a git submodule.

## Targets

```python
import pyqbe

# Auto-detect current platform (default)
asm = pyqbe.compile(ir)

# Explicit target using Target enum
asm = pyqbe.compile(ir, pyqbe.Target.AMD64_SYSV)    # x86-64 Linux
asm = pyqbe.compile(ir, pyqbe.Target.AMD64_APPLE)   # x86-64 macOS
asm = pyqbe.compile(ir, pyqbe.Target.AMD64_WIN)     # x86-64 Windows
asm = pyqbe.compile(ir, pyqbe.Target.ARM64)         # ARM64 Linux
asm = pyqbe.compile(ir, pyqbe.Target.ARM64_APPLE)   # Apple Silicon
asm = pyqbe.compile(ir, pyqbe.Target.RV64)          # RISC-V 64 Linux

# Or pass as a plain string
asm = pyqbe.compile(ir, "amd64_sysv")
```

## How it works

QBE's `parse()` function takes a `FILE*`. `pyqbe` wraps this with a thin shim that turns a Python string into an in-memory `FILE*` (`fmemopen` on Linux/macOS, `tmpfile` on Windows), calls QBE's internals directly, and captures the assembly output — all in-process. No subprocess, no temp files, no system QBE installation needed.

```
Python string (QBE IR)
        ↓
   string_to_file()        ← FILE* shim
        ↓
   qbe parse() + emit()    ← QBE internals (statically linked)
        ↓
   assembly string
```

## Status

- [x] QBE as git submodule
- [x] `wrapper/qbe_api.c` — FILE* shim + C entry point
- [x] `wrapper/binding.cpp` — pybind11 glue
- [x] `meson.build` — build config
- [x] GitHub Actions + cibuildwheel — prebuilt wheels for all platforms
- [x] Published to PyPI
- [x] Tested on macOS (Apple Silicon) and Windows
- [ ] Prebuilt static/dynamic libraries for C++ consumers (planned)

## Related

- [QBE](https://c9x.me/compile/) — the compiler backend this wraps
- [LowPy](https://gitlab.com/my-compiler/lowpy-python) — systems programming language using pyqbe as its backend

## License

QBE is MIT licensed. `pyqbe` wrapper code is also MIT licensed.