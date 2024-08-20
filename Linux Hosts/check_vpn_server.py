#!/usr/bin/env python3
import os
def check_openvpn():
    process_name = "/usr/sbin/openvpn" #Change to your openvpn binary (default is: /usr/sbin/openvpn).
    try:
        process_count = os.popen(f"pgrep -f {process_name} | wc -l").read().strip()
        process_count = int(process_count)

        if process_count > 0:
            print("0 VPN Server - VPN Server is running")
        else:
            print("2 VPN Server - VPN Server is not running")
    except Exception as e:
        print(f"3 VPN Server - Error occurred: {str(e)}")

if __name__ == "__main__":
    check_openvpn()