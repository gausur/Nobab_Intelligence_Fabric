#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-09-15 14:03:01.912429

import re
import socket

def is_phishing_url(url):
    pattern = re.compile(r"^https?:\/\/[a-zA-Z0-9\-\.]+\.[a-zA-Z]{2,3}(\/|$[61D[K
re.compile(r"^https?:\/\/[a-zA-Z0-9\-\.]+\.[a-zA-Z]{2,3}(\/|$)")
    if not pattern.match(url):
        return False
    domain = urlparse(url).netloc
    if not re.match(r"^[a-zA-Z0-9\-\.]+\.[a-zA-Z]{2,3}$", domain):
        return False
    try:
        ip = socket.gethostbyname(domain)
        if ip in ["127.0.0.1", "::1"]:
            return False
        ip_address = ipaddress.ip_address(ip)
        if ip_address.is_loopback or ip_address.is_private:
            return False
    except (socket.gaierror, ipaddress.AddressValueError):
        return False
    return True

def mitigate_phishing_attack(url):
    if is_phishing_url(url):
        print("Phishing attack detected")
        return False
    return True

def main():
    url = input("Enter the URL: ")
    if mitigate_phishing_attack(url):
        print("Access granted")
    else:
        print("Access denied")

if __name__ == "__main__":
    main()