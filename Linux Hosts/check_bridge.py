#!/usr/bin/env python3
import requests
import sys

BRIDGE_IP = "YOUR_HUE_BRIDGE_IP" #Change to your Phillips-Hue Bride ip address.

def check_hue_bridge_status():
    url = f"http://{BRIDGE_IP}/api/config"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(f"0 \"Bridge\" - Bridge is available")
            return 0
        else:
            print(f"2 \"Bridge\" - Bridge is not available HTTP-{response.status_code}")
            return 2
    except requests.exceptions.RequestException as e:
        print(f"2 \"Bridge\" - Unable to connect to Bridge: {str(e)}")
        return 2

if __name__ == "__main__":
    exit_code = check_hue_bridge_status()
    sys.exit(exit_code)