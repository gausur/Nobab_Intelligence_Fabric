#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-02 09:55:58.461691

import re
import smtplib
from email import message_from_string
from email.utils import parseaddr

def is_phishing(email):
    """
    Detect if an email is a phishing attack by checking the subject and bod[3D[K
body for suspicious keywords.
    :param email: The email to be analyzed.
    :return: True if the email is a phishing attack, False otherwise.
    """
    subject = email["subject"]
    body = message_from_string(email.get_payload()).get_content()
    suspicious_keywords = ["fake", "scam", "urgent", "click here", "importa[8D[K
"important"]
    for keyword in suspicious_keywords:
        if keyword in subject or keyword in body:
            return True
    return False

def mitigate_phishing(email):
    """
    Mitigate a phishing attack by sending an alert to the sender and deleti[6D[K
deleting the email.
    :param email: The email to be mitigated.
    """
    server = smtplib.SMTP("localhost")
    server.sendmail("noreply@example.com", parseaddr(email["from"]), "This [K
is a phishing attack. Please do not respond.")
    server.quit()
    del email

if __name__ == "__main__":
    with open("phishing_emails.txt") as f:
        for line in f:
            email = message_from_string(line)
            if is_phishing(email):
                mitigate_phishing(email)