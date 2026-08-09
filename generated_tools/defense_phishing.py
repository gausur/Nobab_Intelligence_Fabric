#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-09 13:43:48.921197

import re
import urllib.parse
from email.message import EmailMessage

def is_phishing_attempt(email):
    message = EmailMessage.from_string(email)
    uri = urllib.parse.urlparse(message.get('From'))
    domain = uri.netloc.lower()
    if not domain or domain == 'localhost' or domain.endswith('.local'):
        return False
    if message.get('Subject').lower().startswith('fwd:'):
        return True
    if re.match(r'.*@([\d]{1,3}\.){3}[\d]{1,3}', message.get('From')):
        return True
    if re.search(r'http://|https://|www\.|\.com$', message.get('Link')):
        return True
    if re.match(r'.*@([\d]{1,3}\.){3}[\d]{1,3}', message.get('TextBody')):
        return True
    return False

def mitigate_phishing_attempt(email):
    message = EmailMessage.from_string(email)
    if is_phishing_attempt(message):
        print("Phishing attempt detected!")
        # TODO: Add further mitigation steps here
    else:
        print("No phishing attempt detected.")