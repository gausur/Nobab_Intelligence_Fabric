#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-26 20:30:08.346627

import re
import smtplib

def check_phishing(email):
    # Check for common phishing URLs
    urls = re.findall('https?://\S+', email)
    for url in urls:
        if 'facebook.com' in url or 'google.com' in url or 'twitter.com' in[2D[K
in url:
            return False
    
    # Check for common phishing words
    words = re.findall('\b(facebook|google|twitter)\b', email)
    for word in words:
        if word.lower() == 'facebook' or word.lower() == 'google' or word.l[6D[K
word.lower() == 'twitter':
            return False
    
    # Check for spammy words
    words = re.findall('\b(spam|junk|scam)\b', email)
    if len(words) > 0:
        return False
    
    return True

def mitigate_phishing(email):
    # Remove any URLs from the email body
    urls = re.findall('https?://\S+', email)
    for url in urls:
        email = email.replace(url, '')
    
    # Remove any spammy words from the email body
    words = re.findall('\b(spam|junk|scam)\b', email)
    for word in words:
        email = email.replace(word, '')
    
    return email

# Test the function with a sample email
email = 'This is a phishing email. Visit https://www.facebook.com/ and clic[4D[K
click on the "Login" button.'
if check_phishing(email):
    print('Email is likely phishing.')
else:
    print('Email is not likely phishing.')