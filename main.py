# maraud, v0.0.1.dev-alpha WIP
# (main code and documentation)

# Copyright (c) 2025 Kian Schmalzl

# -- Links & Resources --
# Github Page ....................... https://github.com/schmalzl/maraud
# Documentation ..................... https://github.com/schmalzl/maraud/blob/master/docs/docs.md
# Releases & Changelog .............. https://github.com/schmalzl/maraud/blob/master/docs/changelog.txt
# Issues & support .................. https://github.com/schmalzl/maraud/issues


# Import sys for pycache deactivation
import sys
# Disable creation of bytecode when debugging.
sys.dont_write_bytecode = True

# main includes
import os               # file access and manipulation
import sys              # recieve commandline arguments
import platform         # OS & architecture information
# yt-dlp downloader api
import yt_dlp           # type: ignore
import time             # timeout
import colorama         # terminal styling
from colorama import init, Fore, Back, Style

# constants
VERSION_STR = "0.0.1.dev-alpha"
REV = "WIP"
COPYRIGHT = "(c) 2025 Kian Schmalzl"

def version():
    client_system = platform.system()
    architecture = platform.machine()
    client = ""
    if client_system == "Windows":
        client = "win"
    elif client_system == "Darwin":
        client = "apple"
    elif client_system == "Linux":
        client = "unix"
    full_arch_str = client + "_" + architecture
    print(f"maraud ({full_arch_str}, {REV}) {VERSION_STR}")
    print(f"Copyright {COPYRIGHT}")
    print("")

def help():
    print("USAGE...")

def excp_invalidUsage():
    print("maraud: " + Fore.LIGHTRED_EX + "fatal error: " + Fore.RESET + "invalid input")
    print("process terminated.")
    print("")

def run():
    init(autoreset=True)    # initialize colorama with autoreset enabled.

    if len(sys.argv) > 1:
        # sys.argv[array]
        # check first argv
        if(sys.argv[1] == "--version" or sys.argv[1] == "-v"):
            version()
        elif(sys.argv[1] == "--help" or sys.argv[1] == "-h"):
            help()
        elif(sys.argv[1] == "-i"):
            print("starting...")
        else:
            excp_invalidUsage()
    else:
        # throw exception
        excp_invalidUsage()


# program entry point
if __name__ == "__main__":
    run()