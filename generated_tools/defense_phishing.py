#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-24 11:23:15.812187

import re
import smtplib

def is_phishing_url(url):
    return re.search(r"phishing\.com", url) is not None

def is_phishing_email(email):
    return re.search(r"@phishing\.com", email) is not None

def mitigate_phishing(url, email):
    if is_phishing_url(url):
        smtplib.sendmail(email, "phishing@example.com")
    elif is_phishing_email(email):
        smtplib.sendmail(url, "phishing@example.com")

if __name__ == "__main__":
    mitigate_phishing("https://phishing.com", "john.doe@phishing.com")