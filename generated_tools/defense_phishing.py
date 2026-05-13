#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-05-13 11:59:30.090880

import re
from email.message import EmailMessage

class PhishingDetector:
    def __init__(self, email_text):
        self.email = email_text
    
    def is_phishing(self):
        if "http://" in self.email or "https://" in self.email:
            return True
        else:
            return False
    
    def get_domain(self):
        domain = re.search("[a-zA-Z0-9.-]+", self.email)
        if domain:
            return domain.group()
        else:
            return None
    
    def is_in_spam_folder(self, spam_folder):
        if spam_folder in self.email:
            return True
        else:
            return False
    
    def get_sender_name(self):
        name = re.search("[a-zA-Z ]+", self.email)
        if name:
            return name.group()
        else:
            return None