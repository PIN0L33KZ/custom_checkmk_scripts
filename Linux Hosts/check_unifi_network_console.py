#!/usr/bin/env python3
import subprocess
import sys

def check_unifi_console():
    process_name = "unifi" #Check if your process name is indeed unifi.

    try:
        output = subprocess.check_output(["pgrep", "-f", process_name])
        if output:
            print(f"0 \"Unifi Console\" - Network Console is running")
            sys.exit(0)
        else:
            print(f"2 \"Unifi Console\" - Network Console is not running")
            sys.exit(2)
    except subprocess.CalledProcessError:
        print(f"2 \"Unifi Console\" - Network Console is not running")
        sys.exit(2)

if __name__ == "__main__":
    check_unifi_console()