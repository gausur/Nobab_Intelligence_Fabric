#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-08 10:22:03.481600

import re

def is_phishing(url):
    pattern = r"^(http|https)://(www\.)?[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za[61D[K
r"^(http|https)://(www\.)?[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_r"^(http|https)://(www\.)?[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Zaz0-9+&@#/%=~_|]"
    if re.match(pattern, url):
        return True
    else:
        return False

def mitigate_phishing(url):
    if is_phishing(url):
        return "Invalid URL"
    else:
        return url