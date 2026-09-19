#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-09-19 13:50:48.748469

import re
import smtplib

def detect_phishing(url):
    # Check if the URL is a valid HTTPS URL
    if not re.match(r"^https://", url):
        return False

    # Check if the URL is a known phishing domain
    if url in KNOWN_PHISHING_DOMAINS:
        return True

    # Check if the URL is a subdomain of a known phishing domain
    for domain in KNOWN_PHISHING_DOMAINS:
        if url.endswith(domain):
            return True

    # Check if the URL is a known phishing domain with a different top-leve[8D[K
top-level domain
    for domain in KNOWN_PHISHING_DOMAINS:
        if url.endswith(domain.split(".")[-1]):
            return True

    return False

def mitigate_phishing(url):
    # Check if the URL is a known phishing domain
    if detect_phishing(url):
        # Send an email to the user with a phishing warning
        email_body = "Phishing warning: the URL you have visited is a known[5D[K
known phishing domain. Please be cautious and avoid clicking on any links o[1D[K
or providing any personal information."
        smtplib.sendmail("noreply@example.com", "user@example.com", email_b[7D[K
email_body)

# Known phishing domains
KNOWN_PHISHING_DOMAINS = ["phishing.com", "malicious.net"]

# Main function
def main():
    # Get the URL from the user
    url = input("Please enter the URL: ")

    # Detect and mitigate phishing attacks
    detect_phishing(url)
    mitigate_phishing(url)

if __name__ == "__main__":
    main()