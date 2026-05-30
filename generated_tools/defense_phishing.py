#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-05-30 18:01:50.997859

import re
import urllib.request
from email.utils import parseaddr

def is_valid_email(email):
    if not email:
        return False
    try:
        parseaddr(email)
        return True
    except Exception:
        return False

def get_domain(url):
    if not url:
        return None
    parsed = urllib.parse.urlsplit(url)
    if not parsed.netloc:
        return None
    return parsed.netloc

def is_phishing_site(url, email):
    domain = get_domain(url)
    if not domain:
        return False
    email_domain = get_domain(email)
    if not email_domain:
        return False
    return domain == email_domain

def mitigate_phishing(url, email):
    if is_phishing_site(url, email):
        print("Possible phishing site detected!")
        print("Domain:", get_domain(url))
        print("Email:", email)
        return True
    return False