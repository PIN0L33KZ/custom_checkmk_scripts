#!/usr/bin/env python3
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
NEXTCLOUD_URL = "https://NEXTCLOUD_SERVER/status.php" #Change to your nextcloud server.

def check_nextcloud_status():
    try:
        response = requests.get(NEXTCLOUD_URL, timeout=5, verify=False)
        if response.status_code == 503:
            print("1 \"Nextcloud\" - Nextcloud is in maintenance mode")
            return

        response.raise_for_status()
        data = response.json()

        if data.get("installed") and data.get("maintenance") == False:
            print("0 \"Nextcloud\" - Nextcloud is running and not in maintenance mode")
        elif data.get("maintenance"):
            print("1 \"Nextcloud\" - Nextcloud is in maintenance mode")
        else:
            print("2 \"Nextcloud\" - Nextcloud is unavailable")

    except requests.exceptions.HTTPError as http_err:
        if http_err.response.status_code == 503:
            print("1 \"Nextcloud\" - Nextcloud is in maintenance mode")
        else:
            print(f"2 \"Nextcloud\" - HTTP error occurred: {http_err}")
    except Exception as e:
        print(f"2 \"Nextcloud\" - Could not retrieve Nextcloud status: {e}")

if __name__ == "__main__":
    check_nextcloud_status()