# incbin

**Goal**: embed an external file inside a binary.

**Method 1**: Use Python script to dump file bytes as a C-string into `.cpp` file \
**Method 2**: Use `.incbin` technique
[shown here](https://gist.github.com/mmozeiko/ed9655cf50341553d282)

**Caveat**:
- The external file should be embedded in `lib.so`
- `main` should be able to access the external file from `lib.so` through a
  global variable

## Results

Method 1 (`GENERATE_RESOURCES`) always works.

Method 2 works depending on:
- The compiler/linker (I tested `g++-10` and `clang++-10`)

- Whether the global variable has `__attribute__((weak))` (`ATTRIBUTE_WEAK`)
  - This seems to fix the issue for `g++-10`, but not for `clang++-10`

- Whether the global variable is `const` (`CONST`)
  - If `const` is used, there will be a big unintialized "placeholder" for the
    external file in `main`, inflating the executable size

- Whether the global variable is used in `lib.cpp` (`LIB_PASSTHROUGH`)

The `./build_all.py` script tries all possibilities. My output on Ubuntu 20.04 is in `output.log`:

```
...
Successful cmds:
./build.py g++-10 GENERATE_RESOURCES
./build.py g++-10 ATTRIBUTE_WEAK
./build.py g++-10 GENERATE_RESOURCES LIB_PASSTHROUGH
./build.py g++-10 GENERATE_RESOURCES ATTRIBUTE_WEAK
./build.py g++-10 LIB_PASSTHROUGH ATTRIBUTE_WEAK
./build.py g++-10 ATTRIBUTE_WEAK CONST
./build.py g++-10 GENERATE_RESOURCES LIB_PASSTHROUGH ATTRIBUTE_WEAK
./build.py g++-10 GENERATE_RESOURCES ATTRIBUTE_WEAK CONST
./build.py g++-10 LIB_PASSTHROUGH ATTRIBUTE_WEAK CONST
./build.py g++-10 GENERATE_RESOURCES LIB_PASSTHROUGH ATTRIBUTE_WEAK CONST
./build.py clang++-10 GENERATE_RESOURCES
./build.py clang++-10 GENERATE_RESOURCES LIB_PASSTHROUGH
./build.py clang++-10 GENERATE_RESOURCES ATTRIBUTE_WEAK
./build.py clang++-10 GENERATE_RESOURCES LIB_PASSTHROUGH ATTRIBUTE_WEAK
```
