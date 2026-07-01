#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-01 17:13:24.283136

import re
import urllib.parse

def is_phishing(url):
    parsed_url = urllib.parse.urlparse(url)
    hostname = parsed_url.hostname
    if not hostname:
        return False
    if hostname.endswith("gmail.com"):
        return True
    if hostname == "www.google.com":
        path = parsed_url.path
        if path.startswith("/search?"):
            params = urllib.parse.parse_qs(parsed_url.query)
            if "q" in params and params["q"][0].lower().startswith("phishin[42D[K
params["q"][0].lower().startswith("phishing website"):
                return True
    return False

def mitigate_phishing(url):
    parsed_url = urllib.parse.urlparse(url)
    hostname = parsed_url.hostname
    if not hostname:
        return url
    if hostname.endswith("gmail.com"):
        return "https://www.google.com/mail/"
    if hostname == "www.google.com":
        path = parsed_url.path
        if path.startswith("/search?"):
            params = urllib.parse.parse_qs(parsed_url.query)
            if "q" in params and params["q"][0].lower().startswith("phishin[42D[K
params["q"][0].lower().startswith("phishing website"):
                return "https://www.google.com/search?q=phishing+website&so[52D[K
"https://www.google.com/search?q=phishing+website&source=hp"
    return url

def main():
    while True:
        url = input("Enter URL: ")
        if is_phishing(url):
            print("Phishing URL detected!")
            url = mitigate_phishing(url)
        else:
            print("No phishing URL detected.")
        print(f"Mitigated URL: {url}")

if __name__ == "__main__":
    main()