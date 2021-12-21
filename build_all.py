#!/usr/bin/env python3

import subprocess
from build import KNOWN_FLAGS
import itertools

COMPILERS = ["g++-10", "clang++-10"]
successful_cmds = []

for compiler in COMPILERS:
    for r in range(len(KNOWN_FLAGS) + 1):
        for p in itertools.combinations(KNOWN_FLAGS, r):
            flags = " ".join(p)
            cmd = f"./build.py {compiler} {flags}"
            print(f"[*] build cmd = {cmd}")
            subprocess.run(cmd, shell=True)

            res = subprocess.run("./check.py", shell=True)
            print(f"[*] check return code = {res.returncode}")
            if res.returncode == 0:
                successful_cmds.append(cmd)

            print()

print("Successful cmds:")
for cmd in successful_cmds:
    print(cmd)
