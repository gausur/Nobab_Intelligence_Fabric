#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-30 01:45:46.965835

import re
import urllib.parse
from email import message_from_bytes

def detect_phishing(email_message):
    # Check if the email is from a legitimate sender
    sender = email_message["From"]
    if not is_legitimate_sender(sender):
        return False
    
    # Check if the email contains a link to a suspicious domain
    for part in email_message.walk():
        if part.get_content_type() == "text/html":
            body = part.get_payload()
            links = re.findall(r"https?://[^\s]+", body)
            for link in links:
                url = urllib.parse.urlparse(link)
                if is_suspicious_domain(url.hostname):
                    return False
    
    # Check if the email contains a malicious attachment
    for part in email_message.walk():
        if part.get_content_type() == "application/octet-stream":
            name = part.get_filename()
            if name and is_malicious(name):
                return False
    
    # If none of the above checks failed, the email is likely legitimate
    return True

def is_legitimate_sender(sender):
    # Check if the sender's domain is known to be legitimate
    domain = urllib.parse.urlparse(sender).hostname
    return domain in legitimate_domains

def is_suspicious_domain(domain):
    # Check if the domain is known to be suspicious
    return domain in suspicious_domains

def is_malicious(name):
    # Check if the attachment name is known to be malicious
    return name in malicious_attachments

legitimate_domains = ["example.com", "gmail.com"]
suspicious_domains = ["phishing.site", "scam.org"]
malicious_attachments = ["virus.exe", "ransomware.exe"]