#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-09-12 02:22:56.237004

import re
import email
from email.parser import Parser
from urllib.parse import urlparse

def is_phishing_url(url):
    parsed_url = urlparse(url)
    if parsed_url.scheme == "http" and parsed_url.netloc.endswith("com"):
        return True
    return False

def is_phishing_email(email_message):
    if email_message.is_multipart():
        for part in email_message.get_payload():
            if is_phishing_url(part.get_content_maintype()):
                return True
    return False

def main():
    message = Parser().parsestr(sys.stdin.read())
    if is_phishing_email(message):
        print("Phishing attack detected!")
    else:
        print("No phishing attack detected.")

if __name__ == "__main__":
    main()