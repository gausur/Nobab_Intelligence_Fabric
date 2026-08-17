#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-17 16:19:56.374147

import re
import ssl

def detect_phishing(url):
    # Use the URL to extract the domain name
    domain = url.split("://")[1].split("/")[0]

    # Check if the domain is in the HSTS preload list
    try:
        hsts = ssl.get_server_certificate((domain, 443), ssl.PROTOCOL_TLSv1[18D[K
ssl.PROTOCOL_TLSv1)
        hsts = re.search(r"HSTS:(\S+)", hsts)
        if hsts:
            return True
    except ssl.SSLError:
        pass

    # Check if the domain has a valid SSL certificate
    try:
        ssl.get_server_certificate((domain, 443), ssl.PROTOCOL_TLSv1)
        return False
    except ssl.SSLError:
        return True

def mitigate_phishing(url):
    # Use the URL to extract the domain name
    domain = url.split("://")[1].split("/")[0]

    # Check if the domain is in the HSTS preload list
    try:
        hsts = ssl.get_server_certificate((domain, 443), ssl.PROTOCOL_TLSv1[18D[K
ssl.PROTOCOL_TLSv1)
        hsts = re.search(r"HSTS:(\S+)", hsts)
        if hsts:
            return True
    except ssl.SSLError:
        pass

    # Check if the domain has a valid SSL certificate
    try:
        ssl.get_server_certificate((domain, 443), ssl.PROTOCOL_TLSv1)
        return False
    except ssl.SSLError:
        return True

def main():
    url = input("Enter the URL to check: ")
    if detect_phishing(url):
        print("Phishing attack detected!")
    else:
        print("No phishing attack detected.")

if __name__ == "__main__":
    main()