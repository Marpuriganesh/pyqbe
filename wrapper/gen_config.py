import platform
import os


def main():
    # Detect platform details (uname / uname -m)
    system = platform.system()
    machine = platform.machine()

    match (system, machine):
        case ("Linux", "x86_64"):
            target = "T_amd64_sysv"
        case ("Darwin", "x86_64"):
            target = "T_amd64_apple"
        case ("Darwin", "arm64"):
            target = "T_arm64_apple"
        case ("Windows", "AMD64") | ("Windows", "x86_64"):
            target = "T_amd64_win"
        case ("Linux", "aarch64") | ("Linux", "arm64"):
            target = "T_arm64"
        case ("Linux", "riscv64"):
            target = "T_rv64"
        case ("Windows", "ARM64") | ("Windows", "aarch64"):
            target = "T_arm64"  # no arm64_win in QBE yet
        case _:
            target = "T_amd64_sysv"  # default to something reasonable

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
