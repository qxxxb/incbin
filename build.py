#!/usr/bin/env python3

KNOWN_FLAGS = ["GENERATE_RESOURCES", "LIB_PASSTHROUGH", "ATTRIBUTE_WEAK", "CONST"]

import subprocess
import sys


def run(cmd: str):
    print(f"[*] {cmd}")
    res = subprocess.run(cmd, shell=True)
    assert res.returncode == 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} compiler [flags...]")
        sys.exit(1)

    CC = sys.argv[1]
    options = sys.argv[2:]

    if "GENERATE_RESOURCES" in options:
        run(f"./src/generate.py {' '.join(options)}")

    if "GENERATE_RESOURCES" in options:
        resources_cpp = "src/generated/resources.cpp"
    else:
        resources_cpp = "src/resources.cpp"

    flags = []

    for known_flag in KNOWN_FLAGS:
        if known_flag in options:
            flags.append(f"-D{known_flag}")

    flags_str = " ".join(flags)

    run(f"{CC} -shared -o lib.so -fPIC src/lib.cpp {resources_cpp} {flags_str}")
    run(f"{CC} -L. -Wl,-rpath=. -o main src/main.cpp -l:lib.so {flags_str}")
