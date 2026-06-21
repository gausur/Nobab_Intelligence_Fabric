#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-21 05:55:43.533115

import re

def detect_phishing(url):
    pattern = r"^https?:\/\/.*\.(?:goo|yah)gle\.[^\.]+\/url\?"
    if re.match(pattern, url):
        return "Phishing detected!"
    else:
        return "No phishing detected."

def mitigate_phishing(url):
    pattern = r"^https?:\/\/.*\.(?:goo|yah)gle\.[^\.]+\/url\?"
    if re.match(pattern, url):
        return url.replace("google", "dummy")
    else:
        return url