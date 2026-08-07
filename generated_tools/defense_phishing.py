#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-07 23:31:33.409559

import re
from urllib.parse import urlparse

def is_phishing_url(url):
    parsed_url = urlparse(url)
    hostname = parsed_url.hostname
    if hostname.endswith("google.com"):
        return False
    else:
        return True

def mitigate_phishing_attack(url, user_agent):
    if is_phishing_url(url):
        print("Phishing attack detected!")
        # Log the attack
        with open("phishing_attacks.log", "a+") as f:
            f.write(f"{user_agent} visited {url}\n")
        return False
    else:
        return True

if __name__ == "__main__":
    url = input("Enter the URL: ")
    user_agent = input("Enter the User Agent: ")
    result = mitigate_phishing_attack(url, user_agent)
    print(f"Result: {result}")