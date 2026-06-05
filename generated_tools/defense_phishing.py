#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-05 16:28:52.999518

import re
import smtplib
from email.mime.text import MIMEText
from urllib.parse import urlparse

def is_phishing_url(url):
    parsed = urlparse(url)
    domain = parsed.netloc
    if domain in [
        "example.com",  # replace with actual phishing domains
        "example2.com",
        "example3.com",
    ]:
        return True
    else:
        return False

def send_email(recipient, subject, message):
    sender = "no-reply@example.com"  # replace with actual email address
    msg = MIMEText(message)
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = recipient
    s = smtplib.SMTP("smtp.example.com")  # replace with actual SMTP server[6D[K
server
    s.send_message(msg)
    s.quit()

def detect_phishing_url(message):
    urls = re.findall(r"https?://\S+", message)
    for url in urls:
        if is_phishing_url(url):
            send_email("admin@example.com", "Possible Phishing Attack", f"P[3D[K
f"Phishing URL detected: {url}")

def main():
    message = input("Enter a message to be analyzed: ")
    detect_phishing_url(message)

if __name__ == "__main__":
    main()