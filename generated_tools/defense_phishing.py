#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-03 02:57:26.600583

import re
import smtplib

def is_phishing(email):
    if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", em[2D[K
email):
        return False
    try:
        smtplib.SMTP("smtp.gmail.com", 587).connect()
        smtplib.SMTP("smtp.yahoo.com", 587).connect()
        smtplib.SMTP("smtp.outlook.com", 587).connect()
    except smtplib.SMTPException:
        return True
    return False