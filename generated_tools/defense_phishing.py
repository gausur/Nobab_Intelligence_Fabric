#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-10-01 22:13:01.729996

import re
import urllib.parse

def is_phishing_url(url):
    parsed_url = urllib.parse.urlparse(url)
    domain = parsed_url.netloc
    pattern = re.compile("[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)+")
    if not pattern.match(domain):
        return True
    return False

def mitigate_phishing(url):
    if is_phishing_url(url):
        return "Phishing attempt detected. Blocked."
    else:
        return "Not a phishing attempt. Allowed."

url = "http://www.phishing-site.com/login.php"
print(mitigate_phishing(url))