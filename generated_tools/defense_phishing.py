#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-02 23:56:27.652385

import re
import smtplib
from email.message import EmailMessage

def is_phishing(email):
    # Check if the email is from a known spammy domain
    if email["From"].lower().endswith("spammydomain.com"):
        return True
    
    # Check if the email contains a suspicious link
    for part in email.walk():
        if part.get_content_maintype() == "text" and "http://" in part.get_[9D[K
part.get_payload():
            url = part.get_payload().split("http://")[1]
            if any(x in url for x in ["phishing", "scam", "malware"]):
                return True
    
    # Check if the email contains a suspicious attachment
    for part in email.walk():
        if part.get_content_type() == "application/zip" and any(x in part.g[6D[K
part.get_filename() for x in ["phishing", "scam", "malware"]):
            return True
    
    return False

def mitigate_phishing(email):
    # Remove the email from the spam folder if it is a phishing attack
    if is_phishing(email):
        smtplib.SMTP("smtp.gmail.com", 587).sendmail(email["From"], email["[7D[K
email["To"], "Please do not open this email.")
    
    # Remove the email from the spam folder if it contains a suspicious lin[3D[K
link or attachment
    else:
        smtplib.SMTP("smtp.gmail.com", 587).sendmail(email["From"], email["[7D[K
email["To"], "Please do not click on any links in this email.")
    
def main():
    # Parse the email from stdin
    email = EmailMessage()
    email.set_content(sys.stdin.read())
    
    # Detect and mitigate phishing attacks
    if is_phishing(email):
        mitigate_phishing(email)
    
if __name__ == "__main__":
    main()