#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-13 17:10:25.574488

import re
import urllib.parse

def is_phishing(url):
    parsed = urllib.parse.urlparse(url)
    domain = parsed.netloc
    if not domain:
        return False
    if "@" in domain:
        return True
    if len(domain) > 6 and all(c.isdigit() for c in domain):
        return True
    if any(c.isupper() for c in domain):
        return True
    return False

def mitigate_phishing(url):
    parsed = urllib.parse.urlparse(url)
    domain = parsed.netloc
    if "@" in domain:
        domain = domain.split("@")[1]
    if len(domain) > 6 and all(c.isdigit() for c in domain):
        domain = re.sub(r"\d", "", domain)
    if any(c.isupper() for c in domain):
        domain = re.sub(r"[A-Z]", "", domain)
    return urllib.parse.urlunparse((parsed.scheme, parsed.netloc, parsed.pa[9D[K
parsed.path, parsed.params, parsed.query, parsed.fragment))