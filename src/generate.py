#!/usr/bin/env python3

from pathlib import Path
import sys


def to_c_str(data: bytes):
    s = "".join(f"\\x{b:02x}" for b in data)
    return '"' + s + '"'


options = sys.argv[1:]

with open("src/splash.png", "rb") as f:
    data = f.read()

print(f"[*] len(data) = {len(data)}")
name = "splash"

if "ATTRIBUTE_WEAK" in options:
    if "CONST" in options:
        hpp = """#pragma once
extern "C" const unsigned char __attribute__((weak)) {name}[];
extern "C" const int __attribute__((weak)) {name}_size;
""".format(
            name=name
        )
    else:
        hpp = """#pragma once
extern "C" unsigned char __attribute__((weak)) {name}[];
extern "C" int __attribute__((weak)) {name}_size;
""".format(
            name=name
        )
else:
    if "CONST" in options:
        hpp = """#pragma once
extern "C" const unsigned char {name}[];
extern "C" const int {name}_size;
""".format(
            name=name
        )
    else:
        hpp = """#pragma once
extern "C" unsigned char {name}[];
extern "C" int {name}_size;
""".format(
            name=name
        )

if "CONST" in options:
    # Double check if extern is necessary
    cpp = """
extern "C" const unsigned char {name}[] = {data};
extern "C" const int {name}_size = {size};
""".format(
        name=name, size=len(data), data=to_c_str(data)
    )
else:
    cpp = """
unsigned char {name}[] = {data};
int {name}_size = {size};
""".format(
        name=name, size=len(data), data=to_c_str(data)
    )

generated = Path("src/generated")
if not generated.exists():
    generated.mkdir()

with open(generated / "resources.hpp", "w") as f:
    f.write(hpp)

with open(generated / "resources.cpp", "w") as f:
    f.write(cpp)
