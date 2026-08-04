#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-04 00:05:31.898530

import re
import smtplib
from email.message import EmailMessage

def is_phishing_url(url):
    pattern = r"^https?://.*\.(\w+)$"
    if not re.match(pattern, url):
        return False
    tlds = ["com", "net", "org", "edu", "gov"]
    for tld in tlds:
        if url.endswith("." + tld):
            return True
    return False

def send_email(recipient, subject, body):
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = "phishing@example.com"
    msg["To"] = recipient
    msg.set_content(body)
    smtplib.SMTP("localhost").sendmail(msg["From"], [msg["To"]], msg.as_str[10D[K
msg.as_string())

def mitigate_phishing(url):
    if is_phishing_url(url):
        send_email("admin@example.com", "Phishing Attack Detected", f"The f[1D[K
following URL was detected as a phishing attack: {url}")

if __name__ == "__main__":
    url = input("Enter the URL to be checked for phishing attacks: ")
    mitigate_phishing(url)