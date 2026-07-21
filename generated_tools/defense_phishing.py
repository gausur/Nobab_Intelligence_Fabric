#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-21 14:58:22.610551

import re

def is_phishing(url):
    if not url:
        return False

    regex = r"^https?://.*\.(?:com|net|org)/"
    matches = re.search(regex, url)

    if matches:
        return True
    else:
        return False

def mitigate_phishing(url):
    if is_phishing(url):
        return None
    else:
        return url