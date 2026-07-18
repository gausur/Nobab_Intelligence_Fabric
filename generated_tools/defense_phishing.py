#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-18 16:48:01.137496

import re
import smtplib
from email.parser import Parser
from typing import List

class PhishingDetector:
    def __init__(self, whitelist: List[str]):
        self.whitelist = whitelist
    
    def detect_phishing(self, message: str) -> bool:
        try:
            parser = Parser()
            parsed = parser.parsestr(message)
            sender = parsed["From"]
            recipient = parsed["To"]
            subject = parsed["Subject"]
            body = parsed.get_payload()
            
            if sender in self.whitelist:
                return False
            if recipient not in self.whitelist:
                return True
            if re.search(r"http[s]?://\w+\.\w+", subject):
                return True
            if re.search(r"http[s]?://\w+\.\w+", body):
                return True
            if re.search(r"(?i)click here to confirm your account", body):
                return True
            if re.search(r"(?i)please click the link below", body):
                return True
        except:
            pass
        
        return False
    
    def mitigate_phishing(self, message: str) -> None:
        try:
            parser = Parser()
            parsed = parser.parsestr(message)
            sender = parsed["From"]
            recipient = parsed["To"]
            subject = parsed["Subject"]
            body = parsed.get_payload()
            
            if sender in self.whitelist:
                return
            if recipient not in self.whitelist:
                return
            if re.search(r"http[s]?://\w+\.\w+", subject):
                return
            if re.search(r"http[s]?://\w+\.\w+", body):
                return
            if re.search(r"(?i)click here to confirm your account", body):
                return
            if re.search(r"(?i)please click the link below", body):
                return
        except:
            pass
        
        smtplib.sendmail(sender, recipient, "This is a phishing attack. Do [K
not click on any links or provide any personal information.", [])