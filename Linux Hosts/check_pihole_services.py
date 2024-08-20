#!/usr/bin/env python3
import subprocess
import sys

def check_service(service_name):
    try:
        output = subprocess.check_output(["pgrep", "-f", service_name])
        if output:
            return True
        else:
            return False
    except subprocess.CalledProcessError:
        return False

def check_pihole_services():
    process_names = [
        "pihole-FTL", 
        "systemd-timesyncd", 
        "dhclient", 
        "apache2" #Change to nginx if necessary.
    ]
    display_names = [
        "DNS resolver",
        "Timesync service",
        "DHCP Client service",
        "Web server"
    ]

    all_services_running = True

    for i in range(len(process_names)):
        service = process_names[i]
        description = display_names[i]
        
        if check_service(service):
            print(f"0 \"{description}\" - {service.capitalize()} is running")
        else:
            print(f"2 \"{description}\" - {service.capitalize()} is not running")
            all_services_running = False

    if all_services_running:
        sys.exit(0)
    else:
        sys.exit(2)

if __name__ == "__main__":
    check_pihole_services()