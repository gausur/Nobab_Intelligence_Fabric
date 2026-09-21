#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-09-21 17:36:03.206437

import re

def is_phishing_attack(url):
    if re.match(r"https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", url):
        return True
    else:
        return False

def mitigate_phishing_attack(url):
    if is_phishing_attack(url):
        return "Phishing attack detected. Please report to the appropriate [K
authorities."
    else:
        return "No phishing attack detected."

if __name__ == "__main__":
    url = input("Enter the URL: ")
    print(mitigate_phishing_attack(url))