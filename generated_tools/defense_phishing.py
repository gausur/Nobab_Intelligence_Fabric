#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-24 01:54:58.936864

import re
import smtplib
from email.message import EmailMessage

# Define the pattern for matching phishing URLs
PHISHING_PATTERN = r"(http|https)://(www\.)?(\w+\.)*[a-zA-Z0-9]+.(com|net|o[56D[K
r"(http|https)://(www\.)?(\w+\.)*[a-zA-Z0-9]+.(com|net|org)/"

# Define the list of safe domains to allow
SAFE_DOMAINS = ["example.com", "example.net"]

def check_phishing(email):
    # Parse the email message
    msg = EmailMessage.parse(email)

    # Extract the URLs from the message body and attachments
    urls = re.findall(PHISHING_PATTERN, msg.get_payload())

    # Check if any of the URLs are phishing
    for url in urls:
        domain = urlparse.urlparse(url).netloc
        if not any(domain == safe_domain for safe_domain in SAFE_DOMAINS):
            print("Phishing URL detected:", url)
            return True

    # No phishing URLs found, return False
    return False

# Test the function with a sample email
email = "Subject: Phishing attack\nFrom: example@example.com\nTo: user@exam[9D[K
user@example.com\n\n<a href=\"http://www.phishingurl.com/page\">Click here [K
to visit the website</a>"
if check_phishing(email):
    print("Phishing attack detected!")
else:
    print("No phishing attack detected.")