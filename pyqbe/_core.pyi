from enum import StrEnum

class Target(StrEnum):
    """Target architecture for QBE compilation."""

    AMD64_SYSV = "amd64_sysv"
    """x86-64 Linux (SysV ABI)"""
    AMD64_APPLE = "amd64_apple"
    """x86-64 macOS"""
    AMD64_WIN = "amd64_win"
    """x86-64 Windows (64-bit, requires UNIX toolchain)"""
    ARM64 = "arm64"
    """ARM64 Linux"""
    ARM64_APPLE = "arm64_apple"
    """ARM64 macOS (Apple Silicon)"""
    RV64 = "rv64"
    """RISC-V 64-bit Linux"""

def compile(ir: str, target: Target | str | None = None) -> str:
    """
    Compile QBE IR to target assembly.

    Args:
        ir: QBE IR string to compile.
        target: Target architecture. Defaults to current platform.

    Returns:
        Assembly string for the target architecture.
    """
    ...
