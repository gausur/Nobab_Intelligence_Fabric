#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-05-31 18:04:43.905379

import re
from email.parser import Parser

def is_phishing(email):
    # Check if the email contains spam keywords
    spam_keywords = ['phish', 'phishing', 'scam', 'hack']
    for keyword in spam_keywords:
        if keyword in email.lower():
            return True
    # Check if the email is from a suspicious domain
    domain = Parser().parsestr(email).get('From')
    suspicious_domains = ['phish-me.com', 'scam-domain.com']
    if domain in suspicious_domains:
        return True
    # Check if the email contains a malicious link
    link_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[6D[K
]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    for url in re.findall(link_pattern, email):
        if 'phish' in url or 'scam' in url:
            return True
    return False

def mitigate_phishing(email):
    # Remove spam keywords from the email
    spam_keywords = ['phish', 'phishing', 'scam', 'hack']
    for keyword in spam_keywords:
        email = email.replace(keyword, '')
    # Remove suspicious domains from the email
    domain = Parser().parsestr(email).get('From')
    suspicious_domains = ['phish-me.com', 'scam-domain.com']
    if domain in suspicious_domains:
        email = email.replace(domain, '')
    # Remove malicious links from the email
    link_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[6D[K
]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    for url in re.findall(link_pattern, email):
        if 'phish' in url or 'scam' in url:
            email = email.replace(url, '')
    return email