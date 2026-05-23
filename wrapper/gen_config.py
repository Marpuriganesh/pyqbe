import platform
import os


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
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # output_file = script_dir / "qbe" / "config.h" --- IGNORE ---
    output_file = os.path.join(script_dir,"..", "qbe", "config.h")

    # Ensure the directory exists and write the file
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, "w") as f:
        f.write(f"#define Deftgt {target}\n")


if __name__ == "__main__":
    main()
