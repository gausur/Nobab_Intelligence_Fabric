#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-15 20:11:59.830405

import re
import smtplib
from email.message import EmailMessage
from email.utils import parseaddr

def is_phishing_email(msg: str) -> bool:
    # check if the email contains a suspicious domain
    pattern = r"@suspicious\.[a-z]+$"
    if re.search(pattern, msg):
        return True
    # check if the email contains a link to a known malicious website
    pattern = r"https?://malicious\.website/[a-zA-Z0-9]+"
    if re.search(pattern, msg):
        return True
    return False

def get_sender_email(msg: str) -> str:
    # extract the sender's email address from the message
    pattern = r"From: (?P<name>.*) <(?P<email>.*)>$"
    match = re.search(pattern, msg)
    if not match:
        return None
    name = match.group("name")
    email = match.group("email")
    return parseaddr(f"{name} <{email}>")[1]

def get_recipient_email(msg: str) -> str:
    # extract the recipient's email address from the message
    pattern = r"To: (?P<name>.*) <(?P<email>.*)>$"
    match = re.search(pattern, msg)
    if not match:
        return None
    name = match.group("name")
    email = match.group("email")
    return parseaddr(f"{name} <{email}>")[1]

def mitigate_phishing_attack(msg: str) -> None:
    # check if the message is a phishing attack
    if is_phishing_email(msg):
        # extract the sender's and recipient's email addresses
        sender = get_sender_email(msg)
        recipient = get_recipient_email(msg)
        # send an alert to the recipient's email address
        msg = EmailMessage()
        msg["Subject"] = "Phishing Attack Detected"
        msg["From"] = sender
        msg["To"] = recipient
        msg.set_content("We have detected a phishing attack on your account[7D[K
account. Please be cautious when clicking links or providing personal infor[5D[K
information.")
        smtplib.sendmail(msg)
    # return the original message
    return msg