#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-02 10:30:14.545565

import re
import smtplib

def check_email(email):
    """Check if an email is a phishing attempt."""
    regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if not re.match(regex, email):
        return False
    else:
        return True

def check_sender(sender):
    """Check if the sender is a legitimate source."""
    blacklist = ["spam@example.com", "scammer@example.com"]
    if sender in blacklist:
        return False
    else:
        return True

def check_subject(subject):
    """Check if the subject line looks like a phishing attempt."""
    regex = r"^[a-zA-Z0-9\s]+[:\s]+[a-zA-Z0-9\s]+$"
    if not re.match(regex, subject):
        return False
    else:
        return True

def check_attachments(attachments):
    """Check if the email has any suspicious attachments."""
    for attachment in attachments:
        extension = os.path.splitext(attachment)[1]
        if extension not in [".pdf", ".docx", ".xlsx"]:
            return False
    return True

def check_message(msg):
    """Check the message body for phishing attempts."""
    regex = r"^[a-zA-Z0-9\s]+[:\s]+[a-zA-Z0-9\s]+$"
    if not re.match(regex, msg.decode("utf-8")):
        return False
    else:
        return True

def main():
    """Main function to call all the other functions."""
    email = input("Enter the email address to check: ")
    sender = email.split("@")[0]
    subject = input("Enter the subject line: ")
    attachments = []
    message = input("Enter the message body: ")

    if check_email(email) and check_sender(sender) and check_subject(subjec[20D[K
check_subject(subject) and check_attachments(attachments):
        print("The email is likely a phishing attempt.")
    else:
        print("The email is not likely a phishing attempt.")

if __name__ == "__main__":
    main()