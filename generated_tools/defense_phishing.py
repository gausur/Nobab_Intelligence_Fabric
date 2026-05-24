#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-05-24 13:07:21.635156

import re
from urllib.parse import urlparse

def is_phishing(url):
    parsed = urlparse(url)
    domain = parsed.netloc
    if not re.match(r"^[a-zA-Z0-9.-]+$", domain):
        return False
    else:
        return True