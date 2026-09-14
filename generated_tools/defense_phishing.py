#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-09-14 15:29:45.190866

import re

def detect_phishing_attacks(url):
    pattern = r"^https?://"
    if re.match(pattern, url):
        return "Phishing attack detected"
    else:
        return "No phishing attack detected"