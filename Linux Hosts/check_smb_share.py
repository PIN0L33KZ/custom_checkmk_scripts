#!/usr/bin/env python3
import subprocess
import sys

def check_samba_share(share, username=None, password=None):
    command = ['smbclient', '-L', share, '-N']
    
    if username and password:
        command = ['smbclient', '-L', share, '-U', f'{username}%{password}']

    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode != 0:
            print(f"2 \"SMB share\" - Share is not available")
            sys.exit(2)
        
        if "Sharename" in result.stdout:
            print(f"0 \"SMB share\" - Share is available")
        else:
            print(f"2 \"SMB share\" - Share is not available")
    
    except Exception as e:
        print(f"2 \"SMB share\" - Exception occurred: {str(e)}")
        sys.exit(2)

if __name__ == "__main__":
    check_samba_share('//SERVER/SHARE', 'USER', 'PASSWORD') #Change to your smb-share (example: //10.0.0.5/share1) aswell as to your smb-user and password.