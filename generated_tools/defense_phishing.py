#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-20 03:25:42.874041

import re
import email
from urllib.parse import urlparse

def is_phishing_url(url):
    parsed = urlparse(url)
    return parsed.scheme == "http" and parsed.netloc.endswith(".com")

def is_phishing_email(message):
    # Check if the email contains a URL that looks like a phishing link
    for part in message.walk():
        if part.get_content_type() == "text/plain" and part.get("Content-Di[20D[K
part.get("Content-Disposition") == "inline":
            body = part.get_payload(decode=True)
            if re.search(r"(?i)\b((?:ht|f)tp\S*|mailto\S*)", body):
                return True
    # Check if the email contains a suspicious attachment
    for part in message.walk():
        if part.get_content_type() == "application/octet-stream" and part.g[6D[K
part.get("Content-Disposition") == "attachment":
            return True
    return False

def mitigate(message):
    # Check if the email contains a URL that looks like a phishing link
    for part in message.walk():
        if part.get_content_type() == "text/plain" and part.get("Content-Di[20D[K
part.get("Content-Disposition") == "inline":
            body = part.get_payload(decode=True)
            # Replace the URL with a safe one
            body = re.sub(r"(?i)\b((?:ht|f)tp\S*|mailto\S*)", r"http://safe[13D[K
r"http://safe.url/", body)
            # Replace any suspicious attachments with a warning message
            if part.get_content_type() == "application/octet-stream":
                body = "WARNING: SUSPICIOUS ATTACHMENT DETECTED. DO NOT OPE[3D[K
OPEN."
            part.set_payload(body, decode=True)
    return message