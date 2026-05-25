#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-05-25 19:20:03.684039

import re
import smtplib
from email.utils import getaddresses

def check_phishing_attack(email):
    addresses = getaddresses([email])
    if len(addresses) != 1:
        return False
    address, domain = addresses[0].split("@")
    if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", em[2D[K
email):
        return False
    try:
        smtplib.SMTP("smtp.gmail.com")
    except smtplib.SMTPException:
        return True
    return False