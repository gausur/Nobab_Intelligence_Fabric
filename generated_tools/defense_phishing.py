#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-06 11:20:08.989259

import re
import urllib.parse
from email.message import EmailMessage

def is_phishing_attempt(email):
    # Check if the email contains a suspicious link
    if "://" in email.body:
        # Extract the URL from the email body
        url = re.search("https?://[^\s]+", email.body).group()
        
        # Parse the URL to extract its components
        parsed_url = urllib.parse.urlsplit(url)
        
        # Check if the URL's hostname is in the email's sender domain
        if parsed_url.hostname and parsed_url.hostname.endswith(email.sende[40D[K
parsed_url.hostname.endswith(email.sender):
            return True
    
    return False

def mitigate_phishing_attempt(email):
    # Replace the suspicious link with a placeholder text
    email.body = re.sub("https?://[^\s]+", "Click here to proceed.", email.[6D[K
email.body)
    
    # Send the modified email to the recipient
    return email