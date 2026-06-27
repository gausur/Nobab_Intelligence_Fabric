#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-27 18:07:44.211618

import re
import urllib.request
from email.utils import parseaddr

def is_valid_email(email):
    regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.search(regex, email) is not None

def extract_email_from_url(url):
    regex = r"mailto:(.*)"
    match = re.search(regex, url)
    if match:
        return match.group(1)
    else:
        return None

def is_phishing_site(url):
    site_name = urllib.request.urlopen(url).geturl()
    site_name = site_name.split("/")[2]
    return site_name in ["gmail", "yahoo", "outlook"]

def mitigate_phishing(url):
    if is_phishing_site(url):
        print("Warning: Phishing site detected!")
    else:
        print("Site not recognized as phishing.")

if __name__ == "__main__":
    url = input("Enter URL to check: ")
    mitigate_phishing(url)