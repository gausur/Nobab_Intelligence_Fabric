#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-06 17:03:33.633486

import re
import requests
from urllib.parse import urlparse

def is_phishing(url):
    parsed_url = urlparse(url)
    if not parsed_url.netloc or not parsed_url.path:
        return False
    if "." not in parsed_url.netloc:
        return False
    if "://" not in url:
        return False
    if re.search(r"\bgoogle\b", url, flags=re.IGNORECASE):
        return True
    elif re.search(r"\bamazon\b", url, flags=re.IGNORECASE):
        return True
    else:
        return False

def mitigate_phishing(url):
    if is_phishing(url):
        print("Possible phishing attack detected!")
        requests.get(url)
    else:
        print("No phishing attacks detected.")

mitigate_phishing("https://www.google.com/search?q=phishing+attack&oq=phishmitigate_phishing("https://www.google.com/search?q=phishing+attack&oq=phishing+attack")