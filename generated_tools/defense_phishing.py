#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-09-22 19:29:29.820608

import re
import smtplib

def detect_phishing_attacks(email_body):
    # Use regular expressions to match common phishing URLs
    url_regex = re.compile(r"https?://[^\s]+", re.IGNORECASE)
    urls = url_regex.findall(email_body)

    # Check if any of the URLs are known phishing sites
    phishing_sites = ["phishing-site.com", "another-phishing-site.com"]
    for url in urls:
        if url in phishing_sites:
            return True

    # Check if the email contains any suspicious keywords
    suspicious_keywords = ["free", "discount", "deal", "scam"]
    for keyword in suspicious_keywords:
        if keyword in email_body:
            return True

    # If no phishing attacks detected, return False
    return False

def mitigate_phishing_attacks(email_body):
    # Use the smtplib library to send an email to the recipient
    # with a warning about the phishing attack
    sender = "phishing-detection@example.com"
    recipient = "john.doe@example.com"
    message = "This is a warning email regarding a potential phishing attac[5D[K
attack. Please be cautious and do not click on any suspicious links or down[4D[K
download any attachments."
    smtplib.sendmail(sender, recipient, message)

def main():
    # Read the email body from stdin
    email_body = input()

    # Detect and mitigate phishing attacks
    if detect_phishing_attacks(email_body):
        mitigate_phishing_attacks(email_body)

if __name__ == "__main__":
    main()