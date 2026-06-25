#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-25 19:06:52.338484

import re

def is_phishing_attempt(url):
    pattern = r"^(?:http|https)://(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])[61D[K
r"^(?:http|https)://(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{r"^(?:http|https)://(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|localhost|\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})(?::\,6}\.?|[A-Z0-9-]{2,}\.?)|localhost|\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})(?::\d{1,5})?(?:/?|[/?]\S+)$"
    if not re.match(pattern, url):
        return False

    pattern = r"^www\.([A-Z0-9]+(?:-[A-Z0-9]+)*)\.com$"
    domain = re.search(pattern, url)
    if domain is None:
        return False

    pattern = r"^[a-z0-9]{16}$"
    random_string = re.search(pattern, url)
    if random_string is not None:
        return True

    return False

def mitigate_phishing_attempt(url):
    # replace the URL with a warning message
    print("WARNING: Phishing attempt detected!")

# example usage
url = "http://www.example.com/qwertyuiopasdfghjklzxcvbnm1234567890"
if is_phishing_attempt(url):
    mitigate_phishing_attempt(url)