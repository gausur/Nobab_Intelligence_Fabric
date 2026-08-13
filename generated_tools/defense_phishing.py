#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-13 20:36:14.893819

import re
import smtplib
from email.mime.text import MIMEText
from urllib.parse import urlparse

def is_phishing_url(url):
    # Check if the URL is a phishing website
    parsed_url = urlparse(url)
    hostname = parsed_url.hostname
    if "google" in hostname:
        return True
    elif "facebook" in hostname:
        return True
    elif "twitter" in hostname:
        return True
    else:
        return False

def send_email(recipient, subject, body):
    # Send an email to the recipient with the phishing URL
    msg = MIMEText(body)
    msg["Subject"] = subject
    s = smtplib.SMTP("localhost")
    s.sendmail("no-reply@example.com", [recipient], msg.as_string())
    s.quit()

def main():
    # Get the URL from the command line arguments
    url = sys.argv[1]

    if is_phishing_url(url):
        # Send an email to the recipient with the phishing URL
        send_email("recipient@example.com", "Phishing Attempt Detected", f"[2D[K
f"The following URL was detected as a phishing attempt: {url}")

if __name__ == "__main__":
    main()