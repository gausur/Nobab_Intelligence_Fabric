#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-17 20:01:48.813861

import re
import smtplib
from email.message import EmailMessage

def is_phishing_email(msg):
    if msg["Subject"].startswith("Fwd: "):
        return True
    elif msg["Subject"].startswith("Re: "):
        return True
    else:
        return False

def mitigate_phishing_attack(msg):
    # Send a bounce message to the sender
    with smtplib.SMTP("localhost") as server:
        msg = EmailMessage()
        msg["Subject"] = "Your message has been flagged as spam"
        msg["From"] = "noreply@example.com"
        msg["To"] = msg["From"]
        msg.set_content("Sorry, your message has been blocked due to phishi[6D[K
phishing concerns.")
        server.sendmail(msg)
    # Print a warning message to the user
    print("Warning: This is likely a phishing email. Do not respond or clic[4D[K
click any links.")

# Main function
def main():
    with open("phishing_emails.txt", "r") as f:
        for line in f:
            msg = EmailMessage()
            msg.set_content(line)
            if is_phishing_email(msg):
                mitigate_phishing_attack(msg)

if __name__ == "__main__":
    main()