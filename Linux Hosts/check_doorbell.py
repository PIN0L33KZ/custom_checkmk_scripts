#!/usr/bin/env python3
import subprocess
import sys

def check_host():
    try:
        process = subprocess.Popen(
            ["ping", "-c", "5", "-W", "1", "DOORBELL_IP"], #Change to your Ring-Doorbell ip address.
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        stdout, stderr = process.communicate()

        if process.returncode == 0:
            # Host is reachable
            print(f"0 \"Doorbell\" - Doorbell is reachable")
            sys.exit(0)
        else:
            # Host is unreachable
            print(f"2 \"Doorbell\" - Doorbell is unreachable")
            sys.exit(2)

    except Exception as e:
        print(f"2 \"Doorbell\" - An error occurred: {str(e)}")
        sys.exit(2)

if __name__ == "__main__":
    check_host()
