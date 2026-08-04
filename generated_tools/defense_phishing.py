#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-04 22:09:42.957923

import re
import urllib
from email.parser import Parser

# Regular expression to match email addresses in the message body
EMAIL_REGEX = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

def is_phishing(message):
    # Check if the message contains a link to a suspicious website
    if re.search(r"https?://[^/]*(yahoo|google|facebook)\.[^/]*", message.g[9D[K
message.get("body")):
        return True
    
    # Check if the message contains an email address that is not from the s[1D[K
sender
    for email in re.findall(EMAIL_REGEX, message.get("body")):
        if email != message.get("from"):
            return True
    
    return False

def mitigate_phishing(message):
    # Check if the message is a phishing attempt and mitigate accordingly
    if is_phishing(message):
        print("Phishing attempt detected!")
        print("Message ID:", message.get("id"))
        print("From:", message.get("from"))
        print("Subject:", message.get("subject"))
        print("Body:", message.get("body"))
    
    # Print the original message if it is not a phishing attempt
    else:
        print("Message ID:", message.get("id"))
        print("From:", message.get("from"))
        print("Subject:", message.get("subject"))
        print("Body:", message.get("body"))

# Example usage:
message = {
    "id": 1234,
    "from": "john@example.com",
    "subject": "Your account has been compromised",
    "body": "Click here to reset your password: https://www.google.com/logi[27D[K
https://www.google.com/login"
}
mitigate_phishing(message)