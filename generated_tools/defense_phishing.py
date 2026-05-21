#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-05-21 18:59:47.180126

import re
from email.parser import Parser

def is_phishing_attack(message):
    # Check if the message has a subject line that contains "free" or "disc[5D[K
"discount"
    if re.search(r'free|discount', message.get('subject')):
        return True
    
    # Check if the message has a body that contains a link to a suspicious [K
website
    if re.search(r'http[s]?://(?!www\.google\.)[^.]+\.[^.]+', message.get('[13D[K
message.get('body')):
        return True
    
    # Check if the message has a sender email address that is not from a we[2D[K
well-known and trusted domain
    if not re.match(r'@example[.]com$', message.get('sender')):
        return True
    
    return False

def mitigate_phishing_attack(message):
    # Delete the message to prevent further phishing attacks
    del message
    
# Read the email message from stdin
parser = Parser()
message = parser.parse(sys.stdin)

if is_phishing_attack(message):
    mitigate_phishing_attack(message)