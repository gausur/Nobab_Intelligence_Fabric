#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-23 21:27:21.530711

import re
import smtplib
from email.message import EmailMessage
from urllib.parse import urlparse

def is_phishing_url(url):
    parsed = urlparse(url)
    return (parsed.netloc == "example.com" and parsed.path == "/login") or [K
(parsed.netloc == "example.com" and parsed.path == "/register")

def is_phishing_email(email):
    return re.match(r"^.*\.(com|net|org)$", email)

def mitigate_phishing(message):
    if is_phishing_url(message.get("ref")):
        print("Phishing URL detected!")
        message["ref"] = ""
    if is_phishing_email(message.get("from")):
        print("Phishing email address detected!")
        message["from"] = ""
    return message

def send_email(message):
    smtplib.SMTP("localhost").sendmail(
        message["from"],
        message["to"],
        message["text"],
        {
            "Content-Type": "text/plain",
            "Subject": message["subject"]
        }
    )

def main():
    message = EmailMessage()
    message.set_content("Hello, world!")
    message["from"] = "john@example.com"
    message["to"] = "jane@example.org"
    message["subject"] = "Test email"
    mitigate_phishing(message)
    send_email(message)

if __name__ == "__main__":
    main()