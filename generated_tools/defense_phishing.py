#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-11 01:52:32.190823

import re
import sys

def is_phishing_url(url):
    pattern = r"^https?://" + "|".join([
        "www",
        "mail",
        "google",
        "facebook",
        "linkedin",
        "twitter",
        "youtube",
        "instagram",
        "pinterest",
    ]) + "\.com$"
    return re.search(pattern, url) is not None

def mitigate_phishing_attack(url):
    if is_phishing_url(url):
        print("Phishing attack detected:", url)
        sys.exit(1)
    else:
        print("No phishing attacks detected.")
        sys.exit(0)

if __name__ == "__main__":
    mitigate_phishing_attack(sys.argv[1])