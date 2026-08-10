#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-10 15:55:14.802804

import re
import urllib.parse

def is_phishing(url):
    parsed = urllib.parse.urlparse(url)
    domain = parsed.netloc
    if not re.match("^[a-z0-9]+([\\.-][a-z0-9]+)*$", domain):
        return True
    else:
        return False

def mitigate_phishing(url):
    if is_phishing(url):
        print("This URL may be a phishing attack. Please proceed with cauti[5D[K
caution.")
    else:
        print("This URL is safe to visit.")