#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-16 15:30:02.953516

import re
import smtplib
from email.message import EmailMessage
from email.utils import parseaddr

def check_phishing(email):
    """Check if the email is a phishing attempt."""
    # Check for common phishing words and phrases
    if any(word in email.body for word in ["free", "discount", "gift"]):
        return True
    # Check for spammy domains
    if any(domain in email.from_email for domain in ["spam", "scam", "phish[6D[K
"phish"]):
        return True
    # Check for suspicious URLs
    if any(url in email.body for url in ["http://", "https://"]):
        return True
    return False

def mitigate_phishing(email, client_id, client_secret):
    """Mitigate a phishing attack by sending a warning email."""
    # Create an EmailMessage object
    msg = EmailMessage()
    msg["Subject"] = "Phishing Attempt Detected"
    msg["From"] = parseaddr(email.from_email)[1]
    msg["To"] = client_id
    msg.set_content("A phishing attempt was detected on your account.")
    # Send the warning email using SMTP
    smtplib.sendmail(client_secret, [client_id], msg.as_string())

def main():
    # Read the email from stdin
    email = EmailMessage()
    for line in sys.stdin:
        email.add_body(line)
    # Check if the email is a phishing attempt
    if check_phishing(email):
        mitigate_phishing(email, client_id, client_secret)

if __name__ == "__main__":
    main()