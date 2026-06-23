#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-23 16:24:00.440318

import re
import requests
from urllib import parse

def detect_phishing(url):
    parsed = parse.urlparse(url)
    domain = parsed.netloc
    if not re.match(r'^[a-z0-9.-]+$', domain):
        return False
    try:
        headers = requests.head(url, allow_redirects=False).headers
        content_type = headers.get('content-type')
        if content_type and 'text/html' in content_type:
            return True
    except Exception:
        pass
    return False