#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-20 17:20:40.980959

import re
import urllib.parse
from email.message import EmailMessage

def is_phishing_url(url):
    # Check if the URL contains any suspicious characters or patterns
    for char in ["://", "www.", ".com", ".org", ".net"]:
        if char in url:
            return False
    return True

def extract_email(message):
    # Extract the email address from the message body
    match = re.search(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", me[2D[K
message)
    if match:
        return match.group()
    else:
        return None

def is_phishing_email(email):
    # Check if the email address contains any suspicious characters or patt[4D[K
patterns
    for char in ["@", ".com", ".org", ".net"]:
        if char in email:
            return False
    return True

def main():
    # Read the message from stdin
    message = sys.stdin.read()

    # Parse the message as an EmailMessage object
    msg = EmailMessage()
    msg.set_payload(message)
    msg.parse()

    # Extract the email address and URL from the message
    email = extract_email(msg.get_payload())
    url = msg.get("From").split("<")[1].split(">")[0]

    # Check if the email address or URL is suspicious
    if is_phishing_email(email) or is_phishing_url(url):
        print("Phishing attack detected!")
    else:
        print("No phishing attack detected.")

if __name__ == "__main__":
    main()