#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-24 04:37:24.548489

import re
import urllib

def is_phishing_url(url):
    pattern = r"^https?://"
    if re.match(pattern, url):
        return True
    else:
        return False

def mitigate_phishing_attack(url):
    if is_phishing_url(url):
        urllib.parse.urlencode(url, quote_via=urllib.parse.quote_plus)
        urllib.parse.urlencode(url, safe=':/?@')
    else:
        return url

def main():
    url = input("Enter a URL: ")
    mitigated_url = mitigate_phishing_attack(url)
    print(f"Mitigated URL: {mitigated_url}")

if __name__ == "__main__":
    main()