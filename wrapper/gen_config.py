import platform
from pathlib import Path


def main():
    # Detect platform details (uname / uname -m)
    system = platform.system()
    machine = platform.machine()

    # 1. Check for macOS (Darwin)
    if "Darwin" in system:
        if "arm64" in machine:
            target = "T_arm64_apple"
        else:
            target = "T_amd64_apple"

    # 2. Check for Linux / Other OS
    else:
        if "aarch64" in machine or "arm64" in machine:
            target = "T_arm64"
        elif "riscv64" in machine:
            target = "T_rv64"
        else:
            target = "T_amd64_sysv"

    # Locate qbe/config.h relative to this script's directory
    script_dir = Path(__file__).parent.resolve()
    output_file = script_dir / "qbe" / "config.h"

    # Ensure the directory exists and write the file
    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text(f"#define Deftgt {target}\n")


if __name__ == "__main__":
    main()
