#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-05-18 14:35:35.937373

import re
import requests
from bs4 import BeautifulSoup

def is_phishing(url):
    """Check if the URL is a phishing site."""
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, "html.parser")
    form = soup.find("form", {"action": re.compile(r"^/login$")})
    return bool(form)

def mitigate_phishing(url):
    """Mitigate phishing attacks by redirecting to a safe page."""
    if is_phishing(url):
        return "https://example.com/safe"
    else:
        return url