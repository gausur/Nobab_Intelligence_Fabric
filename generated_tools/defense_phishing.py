#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-27 22:01:44.718812

import re
import email
from urllib.parse import urlparse

def is_phishing_url(url):
    parsed_url = urlparse(url)
    if parsed_url.netloc == "":
        return False
    return True

def is_phishing_email(message):
    # check for common phishing URL patterns
    pattern = re.compile(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),][61D[K
re.compile(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-re.compile(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),](?:%[0-9a-fA-F][0-9a-fA-F]))+")
    for part in message.walk():
        if part.get_content_type() == "text/plain":
            body = part.get_payload(decode=True)
            matches = re.findall(pattern, body)
            if len(matches) > 0:
                return True
    return False

def mitigate_phishing_attack(message):
    # remove any suspicious URLs from the email message
    for part in message.walk():
        if part.get_content_type() == "text/html":
            body = part.get_payload(decode=True)
            cleaned_body = re.sub(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[48D[K
re.sub(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0re.sub(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", "", body)
            part.set_payload(cleaned_body)

    # remove any suspicious attachments from the email message
    for part in message.walk():
        if part.get_content_type() == "application/octet-stream":
            body = part.get_payload(decode=True)
            cleaned_body = re.sub(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[48D[K
re.sub(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0re.sub(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", "", body)
            part.set_payload(cleaned_body)

def main():
    message = email.message_from_string("""\
From: Bob <bob@example.com>
To: Alice <alice@example.com>
Subject: Phishing Attack!

Hello,

This is a phishing attack. Click on the link to download the attachment.

Sincerely,
Bob""")
    if is_phishing_email(message):
        mitigate_phishing_attack(message)
        print("Phishing email detected and mitigated.")
    else:
        print("No phishing email detected.")

if __name__ == "__main__":
    main()