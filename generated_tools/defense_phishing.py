#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-25 10:27:01.605806

import re

def detect_phishing(url):
    pattern = r"(https?:\/\/)?([\da-z\.-]+\.[a-z]{2,6})(\/([\/\w \.-]*\/)*?[10D[K
\.-]*\/)*?)"
    match = re.match(pattern, url)
    if match:
        domain = match.group(2)
        if domain.endswith(".gov"):
            return "Phishing attack detected!"
    return "No phishing attack detected."

def mitigate_phishing(url):
    pattern = r"(https?:\/\/)?([\da-z\.-]+\.[a-z]{2,6})(\/([\/\w \.-]*\/)*?[10D[K
\.-]*\/)*?)"
    match = re.match(pattern, url)
    if match:
        domain = match.group(2)
        if domain.endswith(".gov"):
            return "Mitigated phishing attack!"
    return "No phishing attack detected."