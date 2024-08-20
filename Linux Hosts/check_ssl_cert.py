#!/usr/bin/env python3
import os
import ssl
from datetime import datetime, timezone

def get_certificate_expiry(cert_file):
    try:
        with open(cert_file, 'rb') as f:
            cert_data = f.read()
            
        cert_info = ssl._ssl._test_decode_cert(cert_file)
        
        expiry_date_str = cert_info['notAfter']
        expiry_date = datetime.strptime(expiry_date_str, "%b %d %H:%M:%S %Y %Z")
        expiry_date = expiry_date.replace(tzinfo=timezone.utc)
        
        return expiry_date
    except Exception as e:
        raise ValueError(f"Error reading certificate: {e}")

def check_certificate_expiry(cert_file, warning_days=30, critical_days=7):
    try:
        expiry_date = get_certificate_expiry(cert_file)
        days_remaining = (expiry_date - datetime.now(timezone.utc)).days
        
        if days_remaining <= critical_days:
            print(f"2 \"SSL Certificate\" - {days_remaining} days remaining")
        elif days_remaining <= warning_days:
            print(f"1 \"SSL Certificate\" - {days_remaining} days remaining")
        else:
            print(f"0 \"SSL Certificate\" - {days_remaining} days remaining")
    
    except Exception as e:
        print(f"2 \"SSL Certificate\" - Unable to check certificate: {e}")

def main():
    certificates = [
        {"cert_file": "/path/to/cert/file.cert", "warning_days": 30, "critical_days": 7}, #Change file location (.cert or .pem) and adjust threshold for warning/critical.
        # Add more certificates as needed.
    ]
    
    for cert in certificates:
        check_certificate_expiry(
            cert["cert_file"], 
            cert.get("warning_days", 30), 
            cert.get("critical_days", 7)
        )

if __name__ == "__main__":
    main()