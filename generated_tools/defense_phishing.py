#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-26 21:53:00.062443

import re
import email

def is_phishing(email):
    # Check if the email contains a suspicious link
    if 'http://' in email or 'https://' in email:
        return True

    # Check if the email contains a malicious attachment
    for part in email.iterparts():
        if part.get_content_maintype() == 'application' and part.get_filena[15D[K
part.get_filename().endswith('.exe'):
            return True

    return False

def mitigate_phishing(email):
    # Remove suspicious links from the email
    for link in re.findall('http://[^"]+', email):
        email = email.replace(link, '')

    # Remove malicious attachments from the email
    for part in email.iterparts():
        if part.get_content_maintype() == 'application' and part.get_filena[15D[K
part.get_filename().endswith('.exe'):
            email = email.replace(part.get_payload(), '')

    return email