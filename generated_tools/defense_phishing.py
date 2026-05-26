#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-05-26 17:56:06.857449

import re
from urllib.parse import urlparse
from email.utils import parseaddr

def is_phishing(url):
    """Check if the URL is a phishing site"""
    parsed = urlparse(url)
    domain = parsed.netloc
    if "." not in domain:
        return False
    top_level_domain = domain.split(".")[-1]
    if top_level_domain in ["com", "org", "gov", "edu"]:
        return True
    else:
        return False

def is_phishing(email):
    """Check if the email address is a phishing email"""
    parsed = parseaddr(email)
    domain = parsed[1].split("@")[-1]
    if "." not in domain:
        return False
    top_level_domain = domain.split(".")[-1]
    if top_level_domain in ["com", "org", "gov", "edu"]:
        return True
    else:
        return False

def mitigate(url):
    """Mitigate the phishing attack by redirecting to a trusted site"""
    parsed = urlparse(url)
    domain = parsed.netloc
    if is_phishing(domain):
        return "https://www.google.com/search?q={}".format(domain)
    else:
        return url

def mitigate(email):
    """Mitigate the phishing attack by redirecting to a trusted site"""
    parsed = parseaddr(email)
    domain = parsed[1].split("@")[-1]
    if is_phishing(domain):
        return "https://www.google.com/search?q={}".format(domain)
    else:
        return email