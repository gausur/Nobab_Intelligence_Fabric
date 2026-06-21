#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-21 21:10:37.315852

import re

def detect_phishing(url):
    pattern = r"(?i)https?:\/\/[a-z0-9._%+-]+[a-z0-9.-]+\.[a-z]{2,}\/?\S*"
    if not re.match(pattern, url):
        return False
    else:
        return True