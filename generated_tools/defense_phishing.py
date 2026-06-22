#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-22 02:58:44.988858

import re
import smtplib

def is_phishing_email(subject, sender):
    """
    Check if the email subject and sender match a known phishing pattern.

    Parameters:
        subject (str): The subject line of the email.
        sender (str): The email address of the sender.

    Returns:
        bool: True if the email is likely to be a phishing attack, False ot[2D[K
otherwise.
    """
    # Check for common phishing patterns in the subject and sender
    pattern = re.compile(r'Fake|Scam|Phish')
    return (pattern.search(subject) or pattern.search(sender)) is not None

def mitigate_phishing_attack(email):
    """
    Mitigate a phishing attack by marking the email as spam and reporting i[1D[K
it to the relevant authorities.

    Parameters:
        email (str): The email message to be processed.
    """
    # Mark the email as spam
    email['X-Spam-Flag'] = 'True'
    # Report the email to the relevant authorities
    smtplib.sendmail(email['From'], ['spam@example.com'])

def main():
    # Read the email message from stdin
    email = input()
    # Check if the email is a phishing attack
    if is_phishing_email(email['Subject'], email['Sender']):
        # Mitigate the phishing attack
        mitigate_phishing_attack(email)