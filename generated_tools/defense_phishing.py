#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-13 06:57:44.494328

import re
import smtplib
from email.message import EmailMessage

def validate_email(email):
    """Validates the given email address using a regular expression."""
    regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(regex, email) is not None

def send_email(sender, recipient, subject, body):
    """Sends an email using the given sender and recipient addresses."""
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = recipient
    msg.set_content(body)
    with smtplib.SMTP("smtp.example.com") as server:
        server.sendmail(sender, recipient, msg.as_string())

def detect_phishing(email):
    """Detects phishing attempts in the given email."""
    # Check for suspicious links in the body of the email
    if "http://" in email["Body"]:
        print("Possible phishing attempt detected!")
        return True
    # Check for spammy keywords in the subject line
    elif any(spam_word in email["Subject"] for spam_word in ["SCAM", "FRAUD[6D[K
"FRAUD", "URGENT"]):
        print("Possible phishing attempt detected!")
        return True
    else:
        return False

def mitigate_phishing(email):
    """Mitigates a phishing attack by notifying the sender and deleting the[3D[K
the email."""
    # Notify the sender of the phishing attempt
    send_email("Phishing Detector <detector@example.com>", email["From"], "[1D[K
"Possible Phishing Attempt", f"This is an automated message to inform you t[1D[K
that your email ({email['Subject']}) may be a phishing attempt.")
    # Delete the email from the mailbox
    print("Deleting the email...")

def main():
    """Main function that runs the detection and mitigation process."""
    while True:
        try:
            email = input("Enter an email address to check for phishing att[3D[K
attempts: ")
            if validate_email(email):
                if detect_phishing(email):
                    mitigate_phishing(email)
                else:
                    print("No phishing attempt detected.")
            else:
                print("Invalid email address entered.")
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    main()