#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-28 03:45:14.463620

import re
from urllib.parse import urlparse

def is_phishing(url):
    parsed = urlparse(url)
    hostname = parsed.hostname
    pattern = r"^[a-zA-Z0-9.-]+$"
    if re.match(pattern, hostname):
        return False
    else:
        return True

def mitigate_phishing(url):
    if is_phishing(url):
        raise ValueError("Phishing attempt detected")
    else:
        pass