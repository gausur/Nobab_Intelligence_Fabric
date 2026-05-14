#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-05-14 00:01:16.384843

import re
import smtplib
from email.message import EmailMessage

def is_phishing(email):
    # Check if the email contains a suspicious link or attachment
    for part in email.iter_attachments():
        if re.search(r"http[s]?://[^\.]+\.[a-z]{2,}$", part.get_content_typ[20D[K
part.get_content_type()):
            return True
    for part in email.iter_parts():
        if re.search(r"<script>|<iframe>", part.get_payload(), flags=re.IGN[12D[K
flags=re.IGNORECASE):
            return True
    # Check if the email is from a suspicious domain or IP address
    if re.search(r"\b(spam|phishing)\b", email.get("From"), flags=re.IGNORE[15D[K
flags=re.IGNORECASE):
        return True
    return False

def mitigate_phishing(email):
    # Remove suspicious links and attachments
    for part in email.iter_attachments():
        if re.search(r"http[s]?://[^\.]+\.[a-z]{2,}$", part.get_content_typ[20D[K
part.get_content_type()):
            part.set_payload(None)
    for part in email.iter_parts():
        if re.search(r"<script>|<iframe>", part.get_payload(), flags=re.IGN[12D[K
flags=re.IGNORECASE):
            part.set_payload(None)
    # Remove suspicious headers
    for header in ["From", "Reply-To", "Return-Path"]:
        if re.search(r"\b(spam|phishing)\b", email.get(header), flags=re.IG[11D[K
flags=re.IGNORECASE):
            email[header] = None
    # Send the mitigated email to the intended recipient
    smtplib.sendmail("noreply@example.com", email.get("To"), email.as_strin[14D[K
email.as_string())