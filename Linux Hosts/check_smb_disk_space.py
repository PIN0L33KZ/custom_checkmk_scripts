#!/usr/bin/env python3
import psutil
import sys

def check_disk_usage(mount_point):
    try:
        disk_usage = psutil.disk_usage(mount_point)
        
        used_percentage = disk_usage.percent
        free_percentage = 100 - used_percentage

        warning_threshold = 80.0 #Adjust the threshold if needed.
        critical_threshold = 90.0 #Adjust the threshold if needed.

        # Determine the status based on thresholds
        if used_percentage >= critical_threshold:
            status_code = 2
        elif used_percentage >= warning_threshold:
            status_code = 1
        else:
            status_code = 0

        print(f"{status_code} \"SMB disk space\" - {used_percentage:.2f}% used, {free_percentage:.2f}% free")

    except Exception as e:
        print(f"2 \"SMB disk space\" - Error: {str(e)}")
        sys.exit(2)

if __name__ == "__main__":
    mount_point = "/" #Change your mount point if needed.
    check_disk_usage(mount_point)