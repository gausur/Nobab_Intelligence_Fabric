#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-03 05:42:19.364152

import re

def is_phishing(url):
    pattern = r"(^|\.)(google|facebook|twitter|linkedin)\.(com|net|org)$"
    match = re.search(pattern, url)
    if match:
        return False
    else:
        return True

def mitigate_phishing(url):
    pattern = r"(^|\.)(google|facebook|twitter|linkedin)\.(com|net|org)$"
    match = re.search(pattern, url)
    if match:
        return False
    else:
        return True