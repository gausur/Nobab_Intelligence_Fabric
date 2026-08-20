#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-20 20:20:40.447365

import re
import urllib.parse

def is_phishing_url(url):
    # Check if the URL is a phishing site by matching it against a list of [K
known phishing sites
    phishing_sites = ["phishing.site", "example.com", "another.phishing.sit[21D[K
"another.phishing.site"]
    if url.hostname in phishing_sites:
        return True
    return False

def is_phishing_email(email):
    # Check if the email address is a phishing address by matching it again[5D[K
against a list of known phishing domains
    phishing_domains = ["phishing.com", "example.com", "another.phishing.co[20D[K
"another.phishing.com"]
    if email.split("@")[1] in phishing_domains:
        return True
    return False

def mitigate_phishing_attack(url, email):
    # If the URL is a phishing site or the email address is a phishing addr[4D[K
address, redirect the user to a safe site
    if is_phishing_url(url) or is_phishing_email(email):
        return urllib.parse.urlencode({"url": "https://safe.site"})
    return urllib.parse.urlencode({"url": url})

def main():
    # Get the URL and email address from the user
    url = input("Enter URL: ")
    email = input("Enter email: ")
    # Mitigate the phishing attack by redirecting the user to a safe site
    return mitigate_phishing_attack(url, email)

if __name__ == "__main__":
    main()