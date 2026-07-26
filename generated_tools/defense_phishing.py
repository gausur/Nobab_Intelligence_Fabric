#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-26 22:55:20.765017

import re
import requests
from urllib.parse import urlparse

def is_phishing(url):
    parsed = urlparse(url)
    if parsed.scheme not in ("http", "https"):
        return False
    response = requests.get(url)
    text = response.text
    if re.search(r"<script>|<iframe>", text, flags=re.IGNORECASE):
        return True
    else:
        return False

def mitigate_phishing(url):
    parsed = urlparse(url)
    if parsed.scheme not in ("http", "https"):
        return None
    response = requests.get(url)
    text = response.text
    if re.search(r"<script>|<iframe>", text, flags=re.IGNORECASE):
        return None
    else:
        return url