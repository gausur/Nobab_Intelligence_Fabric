#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-24 02:20:02.194312

import re

def detect_phishing(url):
    pattern = re.compile(
        r"^(?:http|https)://(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+([67D[K
r"^(?:http|https)://(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{r"^(?:http|https)://(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|"
        r"localhost|"
        r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})(?::\d+)?(?:/|[/?]\S+)$",
        re.IGNORECASE,
    )
    if not pattern.match(url):
        return "Invalid URL"
    else:
        return "Valid URL"

def mitigate_phishing(url):
    if "http://" in url or "https://" in url:
        return url.replace("http://", "https://")
    else:
        return url

url = input("Enter the URL: ")
result = detect_phishing(url)
if result == "Valid URL":
    print("The URL is valid.")
    print("The mitigated URL is:", mitigate_phishing(url))
else:
    print("The URL is invalid.")