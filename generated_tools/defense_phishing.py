#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-10-25 00:46:21.146653

import re
import smtplib
from email.message import EmailMessage

def detect_phishing(email):
    # Check if the email is a valid email address
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return False

    # Check if the email is from a trusted sender
    if email.split("@")[1] not in ["gmail.com", "yahoo.com", "outlook.com"][14D[K
"outlook.com"]:
        return False

    # Check if the email contains a malicious attachment
    if "virus.exe" in email.get_payload():
        return True

    # Check if the email contains a malicious link
    if "http://" in email.get_payload():
        return True

    # Check if the email contains a malicious IP address
    if re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return True

    return False

def mitigate_phishing(email):
    # Remove the malicious attachment
    if "virus.exe" in email.get_payload():
        email.replace_payload(email.get_payload().replace("virus.exe", "cle[4D[K
"clean.exe"))

    # Remove the malicious link
    if "http://" in email.get_payload():
        email.replace_payload(email.get_payload().replace("http://", "https[6D[K
"https://"))

    # Remove the malicious IP address
    if re.match(r"[^@]+@[^@]+\.[^@]+", email):
        email.replace_payload(email.get_payload().replace("http://", "https[6D[K
"https://"))

    return email

# Test the script
email = EmailMessage()
email["from"] = "john.doe@gmail.com"
email["to"] = "jane.doe@yahoo.com"
email["subject"] = "Test Phishing Email"
email["body"] = "Hello Jane, I'm John. I found this website that looks susp[4D[K
suspicious. Click on this link to visit it. http://www.suspiciouswebsite.co[31D[K
http://www.suspiciouswebsite.com"

print(detect_phishing(email)) # False
print(mitigate_phishing(email)) # False

email = EmailMessage()
email["from"] = "john.doe@gmail.com"
email["to"] = "jane.doe@yahoo.com"
email["subject"] = "Test Phishing Email"
email["body"] = "Hello Jane, I'm John. I found this website that looks susp[4D[K
suspicious. Click on this link to visit it. http://www.suspiciouswebsite.co[31D[K
http://www.suspiciouswebsite.com"

print(detect_phishing(email)) # True
print(mitigate_phishing(email)) # True