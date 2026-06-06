#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-06 09:59:19.129929

import re
from urllib.parse import urlparse

def is_phishing_url(url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    if "." not in domain:
        return False
    tlds = ["com", "net", "org", "edu"]
    for tld in tlds:
        if domain.endswith("." + tld):
            return True
    return False

def is_phishing_email(sender, recipient, subject, body):
    if not sender or not recipient or not subject or not body:
        return False
    if "://" in sender or "://" in recipient:
        return True
    if "phishing" in subject.lower() or "scam" in subject.lower():
        return True
    if "http" in body or "https" in body:
        return True
    return False

def mitigate_phishing_attack(url, sender, recipient, subject, body):
    if is_phishing_url(url) or is_phishing_email(sender, recipient, subject[7D[K
subject, body):
        print("Phishing attack detected!")
    else:
        print("No phishing attack detected.")