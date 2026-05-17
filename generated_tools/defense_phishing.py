#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-05-17 17:53:48.699053

import re
import smtplib
from email.message import EmailMessage
from urllib.parse import urlparse

def is_phishing_url(url):
    parsed = urlparse(url)
    if parsed.scheme not in ["http", "https"]:
        return False
    if parsed.netloc == "example.com":
        return True
    return False

def is_phishing_email(msg):
    if msg.is_multipart():
        for part in msg.get_payload():
            if is_phishing_url(part.get("Content-Location")):
                return True
    else:
        return is_phishing_url(msg["Content-Location"])

def mitigate_phishing(msg):
    if is_phishing_email(msg):
        smtplib.SMTP("mail.example.com").sendmail("from@example.com", "to@e[5D[K
"to@example.com", msg.as_string())

def main():
    with open("email.txt") as f:
        for line in f:
            mitigate_phishing(EmailMessage().parse(line))

if __name__ == "__main__":
    main()