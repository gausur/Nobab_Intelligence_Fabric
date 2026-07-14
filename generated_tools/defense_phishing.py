#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-14 17:07:11.652009

import re

def detect_phishing(url):
    pattern = r"^https?://" + r"|".join([r"\w+\.(?:google|yahoo|bing)\.\w+"[45D[K
r"|".join([r"\w+\.(?:google|yahoo|bing)\.\w+", r"\w+\.google\.\w+"])
    if re.match(pattern, url):
        return False
    else:
        return True

def mitigate_phishing(url):
    print("This URL is likely a phishing site!")

if __name__ == "__main__":
    url = input("Enter the URL to check: ")
    if detect_phishing(url):
        mitigate_phishing(url)