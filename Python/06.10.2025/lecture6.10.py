import os
import sys


interface_version = "a0.1"
py_version = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"

print(f"[aPCCI a0.1][LOG] Python program started running from file: {os.path.basename(__file__)}")
print(f"[aPCCI a0.1][LOG] aPCCI (ahfuba's Python Command Console Interface) is running. Version {interface_version}")
print("[aPCCI a0.1][LOG] Python is a language of Python Software Foundation (PSF). Visit https://www.python.org/ for more information. I don't own Python or any of its components.")
print(f"[aPCCI a0.1][LOG] Python version: {py_version}")



integer = 53
char = "A"
float_num = 3.14
string = "need me sleep"
boolean = True
print(f"[aPCCI a0.1][SCRIPT] Variable integer initialized with value: {integer}")
print(f"[aPCCI a0.1][SCRIPT] Variable char initialized with value: {char}")
print(f"[aPCCI a0.1][SCRIPT] Variable float_num initialized with value: {float_num}")
print(f"[aPCCI a0.1][SCRIPT] Variable string initialized with value: {string}")
print(f"[aPCCI a0.1][SCRIPT] Variable boolean initialized with value: {boolean}")

EXIT_INPUT = input("[aPCCI a0.1][LOG] Press any key to terminate the program...")

def handle_EXIT_INPUT():
    if EXIT_INPUT:
        print("[aPCCI a0.1][LOG] Program terminated by user input.")
        os.sleep(1000)
        os._exit(0)