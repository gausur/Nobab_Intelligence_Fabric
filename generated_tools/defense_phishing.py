#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-05-16 16:52:40.436860

import re
import smtplib
from email.message import EmailMessage

def is_phishing_attack(email):
    # Check if the email contains a malicious URL
    url = re.search(r"https?://\S+", email)
    if url:
        # Make sure the URL is not from a known good domain
        if not url.group().startswith("http://www.google.com"):
            return True
    return False

def mitigate_phishing_attack(email, recipient):
    # Send an email to the recipient warning them of the potential phishing[8D[K
phishing attack
    msg = EmailMessage()
    msg["Subject"] = "Phishing Attack Detected"
    msg.set_content("We have detected a potential phishing attack in your a[1D[K
account.\n\nPlease do not click on any links or provide any personal inform[6D[K
information.")
    smtplib.sendmail(recipient, email)

def main():
    # Read the email from stdin
    email = input().strip()
    recipient = "recipient@example.com"

    if is_phishing_attack(email):
        mitigate_phishing_attack(email, recipient)

if __name__ == "__main__":
    main()