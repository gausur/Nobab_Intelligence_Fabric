#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-07 16:46:05.499680

import re
import smtplib

def check_email(email):
    if not re.match(r"^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$", email):
        return False
    return True

def check_url(url):
    if not re.match(r"^https?://", url):
        return False
    return True

def mitigate_phishing(email, url):
    if not check_email(email) or not check_url(url):
        return
    try:
        smtplib.SMTP("smtp.gmail.com", 587).sendmail(email, email, f"Subjec[8D[K
f"Subject: Phishing Attack Detected\n\n{url}")
    except smtplib.SMTPException:
        pass

def main():
    mitigate_phishing("someone@example.com", "http://www.evilsite.com/")

if __name__ == "__main__":
    main()