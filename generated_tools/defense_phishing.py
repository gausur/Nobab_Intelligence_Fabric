#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-20 05:07:34.609366

import re
import smtplib
from email import message_from_string

def is_phishing_email(email):
    # Check if the email contains suspicious patterns
    if re.search(r"[\w\.]+@[\w\.]+\.(?:com|net|org)", email["From"]):
        return True
    else:
        return False

def mitigate_phishing_email(email):
    # Send a response to the sender with a warning message
    smtplib.SMTP("localhost").sendmail(
        "no-reply@example.com", email["From"],
        "Warning: This is a phishing email. Do not click on any links or pr[2D[K
provide any personal information."
    )

# Iterate over the emails in the file and detect and mitigate phishing atta[4D[K
attacks
with open("emails.txt", "r") as f:
    for email in f:
        if is_phishing_email(email):
            mitigate_phishing_email(email)