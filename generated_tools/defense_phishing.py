#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-09 00:01:33.958590

import re
from email.message import EmailMessage
from typing import Dict, List, Optional

class PhishingDetector:
    def __init__(self):
        self.whitelist = ["gmail.com", "yahoo.com"]
        self.blacklist = ["example.com", "fakeemail.net"]
    
    def is_phishing(self, message: EmailMessage) -> bool:
        """Detect if the email is a phishing attack"""
        # Check if the sender's domain is in the blacklist
        if message.sender[1].lower() in self.blacklist:
            return True
        
        # Check if the recipient's domain is in the whitelist
        if message.recipients[0][1].lower() not in self.whitelist:
            return True
        
        # Check if the email contains spammy keywords or phrases
        for word in ["free", "discount", "promotion", "click here"]:
            if re.search(word, message.text_content(), re.IGNORECASE):
                return True
        
        # No phishing detected
        return False
    
    def mitigate(self, message: EmailMessage) -> Optional[EmailMessage]:
        """Mitigate the phishing attack by adding a warning to the email"""[8D[K
email"""
        if not self.is_phishing(message):
            return None
        
        # Create a new email with the original sender and recipient
        new_message = EmailMessage()
        new_message["From"] = message["From"]
        new_message["To"] = message["To"]
        
        # Add a warning to the email body
        new_message.set_content(f"WARNING: This is a phishing attack. Do no[2D[K
not click on any links or provide any personal information.")
        
        return new_message