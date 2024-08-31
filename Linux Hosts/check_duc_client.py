#!/usr/bin/env python3

import os
import sys
import subprocess

def check_noip_duc():
    # Path to the noip-duc binary
    noip_duc_path = "/usr/bin/noip-duc"
    
    # Check if the noip-duc binary exists
    if not os.path.isfile(noip_duc_path):
        print(f"2 DUC - {noip_duc_path} does not exist")
        return 2

    try:
        # Check if the noip-duc process is running
        result = subprocess.run(["pgrep", "-f", noip_duc_path], stdout=subprocess.DEVNULL)
        
        if result.returncode == 0:
            # Process is running
            print(f"0 DUC - {noip_duc_path} is running")
            return 0
        else:
            # Process is not running
            print(f"2 DUC - {noip_duc_path} is not running")
            return 2

    except Exception as e:
        # If there's an error, return an unknown status
        print(f"3 DUC - Unknown error: {str(e)}")
        return 3

if __name__ == "__main__":
    sys.exit(check_noip_duc())