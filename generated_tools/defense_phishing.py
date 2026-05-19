#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-05-19 10:59:34.037412

import re
import smtplib
from email.message import EmailMessage

def is_phishing_attack(email):
    """Check if the given email is a phishing attack."""
    if not email or not isinstance(email, str):
        return False
    
    # Check for common phishing patterns
    if re.search(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email)[6D[K
email) is None:
        return True
    
    # Check for suspicious URLs in the email body
    if re.search(r"http://|https://|www\.", email):
        return True
    
    return False

def mitigate_phishing_attack(email, sender):
    """Mitigate a phishing attack by sending an alert to the sender."""
    if not is_phishing_attack(email):
        return
    
    msg = EmailMessage()
    msg["Subject"] = "Phishing Attack Alert"
    msg["From"] = sender
    msg["To"] = email
    msg.set_content("We have detected a phishing attack in your email. Plea[4D[K
Please do not click on any links or provide any personal information.")
    
    try:
        smtplib.sendmail(sender, email, msg.as_string())
    except Exception as e:
        print(f"Error sending alert to {email}: {e}")

if __name__ == "__main__":
    mitigate_phishing_attack("example@email.com", "admin@company.com")