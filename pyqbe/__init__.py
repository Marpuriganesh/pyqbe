try:
    from _pyqbe import compile
except ImportError:
    pass  # not built yet

from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("pyqbe")
except PackageNotFoundError:
    __version__ = "unknown"  # not installed yet


from enum import StrEnum


class Target(StrEnum):
    AMD64_SYSV = "amd64_sysv"
    AMD64_APPLE = "amd64_apple"
    AMD64_WIN = "amd64_win"
    ARM64 = "arm64"
    ARM64_APPLE = "arm64_apple"
    RV64 = "rv64"


__all__ = ["compile", "Target"]
