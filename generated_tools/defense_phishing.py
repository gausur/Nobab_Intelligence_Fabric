#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-21 21:58:57.824014

import re
from urllib.parse import urlparse
from email.message import EmailMessage
from smtplib import SMTPException

def is_phishing(email):
    # Check if the email contains a malicious link
    for part in email.walk():
        if part.get_content_type() == "text/html":
            for link in re.findall(r"<a\s+(?:[^>]*?\s+)?href=\"(.*?)\"", pa[2D[K
part.get_payload(decode=True)):
                url = urlparse(link)
                if url.scheme == "http" and url.netloc != email.mail_from:
                    return True
    # Check if the email is signed by a trusted domain
    for part in email.walk():
        if part.get_content_type() == "application/pgp-signature":
            signature = part.get_payload(decode=True)
            try:
                verifier = SMTPException("", 0, None)
                verifier.verify_sig(email, signature)
                return False
            except SMTPException as e:
                if e.smtp_code == "554":
                    return True
    # Check if the email is from a trusted sender
    for part in email.walk():
        if part.get_content_type() == "text/plain" and email.mail_from != "[1D[K
"postmaster@example.com":
            return True
    return False