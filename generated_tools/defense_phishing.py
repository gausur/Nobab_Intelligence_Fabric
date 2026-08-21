#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-21 05:28:05.978095

import re
import urllib.parse

def is_phishing_url(url):
    parsed_url = urllib.parse.urlparse(url)
    hostname = parsed_url.netloc
    if not hostname.endswith('.com'):
        return False
    if hostname.startswith('www.'):
        hostname = hostname[4:]
    if hostname.endswith('.org'):
        return True
    return False

def is_phishing_email(email):
    if not email.endswith('.com'):
        return False
    if email.startswith('www.'):
        email = email[4:]
    if email.endswith('.org'):
        return True
    return False

def mitigate_phishing_attack(url, email):
    if is_phishing_url(url):
        print("Phishing URL detected: " + url)
        return
    if is_phishing_email(email):
        print("Phishing email detected: " + email)
        return
    print("No phishing attack detected")

url = input("Enter URL: ")
email = input("Enter email: ")
mitigate_phishing_attack(url, email)