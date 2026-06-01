#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-01 23:02:19.674108

import re
import smtplib
from email import message_from_string

def is_phishing_email(email):
    """
    Check if the given email is a phishing email by checking for suspicious[10D[K
suspicious content in the subject line and the sender's email address.
    """
    # Extract the subject line and sender's email address from the email me[2D[K
message
    subject = email['subject']
    sender = email['from']

    # Check if the subject line contains any suspicious keywords or phrases[7D[K
phrases
    if re.search(r'\bphishing\b|\bsuspicious\b|\bfake\b', subject, f[1D[K
flags=re.IGNORECASE):
        return True

    # Check if the sender's email address is from a known spammer domain
    if '@' in sender and re.search(r'\bspammydomain\b', sender, flags=re.IG[11D[K
flags=re.IGNORECASE):
        return True

    # If none of the above checks match, assume the email is not a phishing[8D[K
phishing email
    return False

def mitigate_phishing_attack(email):
    """
    Mitigate a phishing attack by sending a response to the sender indicati[8D[K
indicating that the message was detected as a phishing attempt.
    """
    # Extract the recipient's email address from the email message
    recipient = email['to']

    # Create a new email message with the appropriate headers and body
    msg = message_from_string('To: {recipient}\nSubject: Phishing Attack De[2D[K
Detected\n\nThis is an automated response to indicate that your message was[3D[K
was detected as a phishing attempt. Please do not respond to this message.\[9D[K
message.\n')

    # Send the new email message to the recipient's email address
    smtplib.sendmail('phishing@example.com', recipient, msg.as_string())

# Read in an email message from stdin
email = message_from_string(sys.stdin.read())

# Check if the email is a phishing attack and mitigate it if necessary
if is_phishing_email(email):
    mitigate_phishing_attack(email)