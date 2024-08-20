#!/usr/bin/env python3
import sys
import urllib.request
import json

def check_minecraft_server():
    host = "MINECRAFT_SERVER_IP" #Change to your Minecraft server ip or domain.
    url = f"https://api.mcsrvstat.us/2/{host}"
    try:
        request = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(request) as response:
            if response.status == 200:
                data = json.loads(response.read().decode())
                if data.get('online'):
                    players_online = data['players']['online']
                    players_max = data['players']['max']
                    
                    print(f"0 \"Minecraft Server\" - Server is Available, Players online: {players_online}/{players_max}")
                    sys.exit(0)
                else:
                    print("2 \"Minecraft Server\" - Server is Unavailable | \"players=0;0;0;0\"")
                    sys.exit(2)
            else:
                print(f"1 \"Minecraft Server\" - Could not reach API. HTTP Status Code: {response.status}")
                sys.exit(2)
    except Exception as e:
        print(f"2 \"Minecraft Server\" - An error occurred: {str(e)}")
        sys.exit(2)

if __name__ == "__main__":
    check_minecraft_server()