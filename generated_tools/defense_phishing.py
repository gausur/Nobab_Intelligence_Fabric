#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-05-25 17:05:58.974240

import re
import smtplib

def detect_phishing(email):
    if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', em[2D[K
email):
        return False
    
    try:
        smtplib.SMTP('smtp.gmail.com', 587)
        return True
    except Exception:
        return False