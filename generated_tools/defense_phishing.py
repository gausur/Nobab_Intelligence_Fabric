#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-02 22:03:47.548197

import re

def is_phishing_url(url):
    pattern = r"https?://\w+\.\w+/\w+"
    return bool(re.match(pattern, url))

def mitigate_phishing_attack(request_headers):
    if "Referer" in request_headers:
        referer_url = request_headers["Referer"]
        if is_phishing_url(referer_url):
            return {"Content-Type": "text/plain"}, "Phishing attack detecte[7D[K
detected."
    return None, None