#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-19 05:19:29.057056

import re
import smtplib
from email.message import EmailMessage

def detect_phishing(email):
    # Check if the email is from a trusted domain
    if not re.search("^.*@(gmail|yahoo|hotmail).com$", email["From"]):
        return False
    
    # Check if the email contains a malicious attachment or URL
    if re.search("virus|malware|scam", email.as_string(), re.I):
        return True
    
    # Check if the email contains a phishing link
    if re.search("http://.*\.com/.*(login|signup)", email.as_string()):
        return True
    
    return False

def mitigate_phishing(email, sender_ip):
    # Block the IP address of the phishing attacker
    smtplib.SMTP("localhost", 25).sendmail(email["From"], email["To"], "Blo[4D[K
"Blocked by phishing detection system")
    
    # Inform the user about the detected phishing attempt
    message = EmailMessage()
    message["Subject"] = "Phishing Attempt Detected"
    message["From"] = "phishing@example.com"
    message["To"] = email["From"]
    message.set_content("Your email address was used in a phishing attempt [K
from {}.\n".format(sender_ip) + 
                        "Please check your email account for any suspicious[10D[K
suspicious activity and report any false positives to our team.")
    
    smtplib.SMTP("localhost", 25).sendmail(message["From"], message["To"], [K
message.as_string())