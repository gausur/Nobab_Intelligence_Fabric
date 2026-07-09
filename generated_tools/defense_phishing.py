#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-09 00:04:09.967392

import re
import smtplib
from email.parser import Parser
from email.header import decode_header
from email.utils import getaddresses

def detect_phishing(email):
    """
    Detect phishing attacks in an email using regex and the Sender header.
    
    Args:
        email (str): The email message to be analyzed.
    
    Returns:
        bool: True if the email is a phishing attack, False otherwise.
    """
    # Regex to detect suspicious keywords in the email body
    pattern = r"(https?:\/\/)?(www\.)?(paypal|amazon|walmart|bank|credit)\b[61D[K
r"(https?:\/\/)?(www\.)?(paypal|amazon|walmart|bank|credit)\b"
    
    # Check if the email contains any of the suspicious keywords
    if re.search(pattern, email):
        return True
    
    # Get the Sender header from the email
    sender = Parser().parse_header(email).get("From")
    
    # Extract the address and name from the Sender header
    address, name = decode_header(sender)
    
    # Check if the address is a valid email address
    try:
        address = getaddresses([address])[0]
    except Exception as e:
        return False
    
    # Check if the domain of the Sender header is in the whitelist
    domain = address.split("@")[1]
    if domain not in ["gmail.com", "yahoo.com", "hotmail.com"]:
        return True
    
    # Check if the email contains any spammy keywords
    pattern = r"(spam|virus|phishing|scam)"
    if re.search(pattern, email):
        return True
    
    return False