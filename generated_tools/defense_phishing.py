#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-18 21:43:59.141919

import re
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

def detect_phishing(email):
    # Check if the email is a phishing attempt by looking for common patter[6D[K
patterns
    # in the sender's email address and the email content.
    if re.search(r"@gmail\.com$", email["From"]) and "phish me out" in emai[4D[K
email["Subject"]:
        return True
    elif re.search(r"@hotmail\.com$", email["From"]) and "dummy email" in e[1D[K
email["Body"]:
        return True
    else:
        return False

def mitigate_phishing(email):
    # Send a response to the sender indicating that their email is not a ph[2D[K
phishing attempt.
    msg = MIMEText("This is not a phishing attempt. Please proceed with cau[3D[K
caution.")
    msg["From"] = formataddr((email["From"], "no-reply@example.com"))
    msg["To"] = email["From"]
    msg["Subject"] = "Phishing Attempt Detected"
    smtplib.sendmail("no-reply@example.com", email["From"], msg.as_string()[15D[K
msg.as_string())

def main():
    # Read the email from stdin and parse it into a dictionary.
    email = {"From": None, "To": None, "Subject": None, "Body": None}
    for line in sys.stdin:
        if not line:
            break
        key, value = line.strip().split(":", 1)
        email[key] = value.decode()

    # Detect and mitigate any phishing attempts.
    if detect_phishing(email):
        mitigate_phishing(email)

if __name__ == "__main__":
    main()