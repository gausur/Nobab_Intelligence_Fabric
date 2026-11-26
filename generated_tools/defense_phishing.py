#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-11-26 06:09:47.295101

import re
import smtplib

def is_phishing_url(url):
    """
    Check if the given URL is a phishing URL.
    """
    return re.search(r"(http|https)://(www\.|)phishing\.com", url)

def is_phishing_email(email):
    """
    Check if the given email address is a phishing email.
    """
    return re.search(r"phishing@[a-zA-Z0-9]+\.[a-zA-Z]{2,}", email)

def is_phishing_message(message):
    """
    Check if the given message is a phishing message.
    """
    return is_phishing_url(message) or is_phishing_email(message)

def mitigate_phishing_attack(message):
    """
    Mitigate a phishing attack by sending an email to the sender with a phishing report.
    """
    sender = message["From"]
    receiver = message["To"]
    subject = "Phishing Attack Report"
    body = "The following message is a phishing attack: {}".format(message)
    smtplib.sendmail(sender, receiver, subject, body)

def main():
    message = input("Enter a message to detect phishing attacks: ")
    if is_phishing_message(message):
        mitigate_phishing_attack(message)

if __name__ == "__main__":
    main()