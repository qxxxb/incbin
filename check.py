#!/usr/bin/env python3

from colorama import Fore, Back, Style, init
import subprocess
import sys

init()

with open("lib.so", "rb") as f:
    lib = f.read()

with open("main", "rb") as f:
    main = f.read()

with open("src/splash.png", "rb") as f:
    splash = f.read()

success = True

if splash in lib:
    print(f"{Fore.GREEN}[+] lib contains splash")
else:
    print(f"{Fore.RED}[+] lib does not contain splash")
    success = False

if splash in main:
    print(f"{Fore.RED}[-] main contains splash")
    success = False
else:
    print(f"{Fore.GREEN}[+] main does not contain splash")

if len(main) >= len(splash):
    print(f"{Fore.RED}[-] main is larger than splash")
    success = False
else:
    print(f"{Fore.GREEN}[+] main is smaller than splash")


output = subprocess.check_output("./main")
if splash[:48].hex().encode() in output:
    print(f"{Fore.GREEN}[+] splash has correct address")
else:
    print(f"{Fore.RED}[-] splash has incorrect address")
    success = False

sys.exit(not success)
