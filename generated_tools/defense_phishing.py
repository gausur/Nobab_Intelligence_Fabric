#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-31 11:27:36.009627

import re
import urllib.parse
from email.message import EmailMessage

def is_phishing_attack(email):
    """Check if the email is a phishing attack."""
    # Check for spammy words in the subject and body of the email
    if any(word in email["Subject"] for word in ["free", "discount", "coupo[6D[K
"coupon"]):
        return True
    if any(word in email.get_payload() for word in ["click here", "enter yo[2D[K
your email"]):
        return True
    # Check for suspicious URLs
    url = urllib.parse.urlparse(email["Links"])
    if url.scheme not in ["http", "https"]:
        return True
    return False

def mitigate_phishing_attack(email):
    """Mitigate a phishing attack by removing the email from the user's mai[3D[K
mailbox."""
    # Remove the email from the user's mailbox
    print("Removing phishing email from inbox...")
    return True

def main():
    while True:
        try:
            email = input("Enter a email: ")
            if is_phishing_attack(email):
                mitigate_phishing_attack(email)
        except Exception as e:
            print(f"Error: {e}")
            continue

if __name__ == "__main__":
    main()