#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-16 06:31:34.973151

import re
import smtplib
from email import message_from_string

def detect_phishing(email):
    msg = message_from_string(email)
    if msg.get('Subject') == 'Your account has been compromised':
        return True
    else:
        return False

def mitigate_phishing(email, sender, recipient):
    msg = message_from_string(email)
    smtplib.SMTP('smtp.gmail.com', 587).sendmail(sender, recipient, msg.as_[7D[K
msg.as_bytes())