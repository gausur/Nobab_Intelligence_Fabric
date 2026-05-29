#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-05-29 00:06:19.378944

import re
from urllib.parse import urlparse

def is_phishing(url):
    parsed_url = urlparse(url)
    if parsed_url.netloc.endswith('gmail.com'):
        return False
    elif parsed_url.netloc.endswith('yahoo.com'):
        return False
    elif parsed_url.scheme != 'https':
        return True
    else:
        return False