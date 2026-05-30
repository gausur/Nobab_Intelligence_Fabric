#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-05-30 20:49:15.600520

import re
import email
from urllib.parse import urlparse

def is_phishing_attack(email):
    # Check if the email contains any suspicious links
    for part in email.iter_parts():
        if part.get_content_type() == 'text/html':
            soup = BeautifulSoup(part.get_payload(), 'html.parser')
            for link in soup.find_all('a'):
                href = urlparse(link['href'])
                if href.netloc != email.mail_from and href.netloc not in ['[2D[K
['www.example.com', 'example.com']:
                    return True

    # Check if the email contains any suspicious attachment names
    for part in email.iter_parts():
        if part.get_content_type() == 'application/pdf' and re.search(r'[a-[15D[K
re.search(r'[a-z]+\.exe', part.get('name')):
            return True

    # Check if the email contains any suspicious content
    for part in email.iter_parts():
        if part.get_content_type() == 'text/plain':
            text = str(part.get_payload())
            if re.search(r'[a-z]+\.exe', text):
                return True

    # Check if the email contains any suspicious headers
    for header in email.items():
        if header.name == 'From':
            from_addr = header.value
            if from_addr != email.mail_from:
                return True

    # No suspicious patterns found, return False
    return False