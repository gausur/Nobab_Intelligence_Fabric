#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-07 21:04:27.686261

import re
import smtplib
from email.mime.text import MIMEText

def is_phishing_attempt(email):
    # Check if the email contains a link to a malicious website
    if re.search(r"https?://[^\s]+", email.body):
        return True

    # Check if the email contains a suspicious sender or recipient
    if re.search(r"\b(phishing|scam|fraud)\b", email.sender) or \
            re.search(r"\b(phishing|scam|fraud)\b", email.recipient):
        return True

    # Check if the email contains a common phishing tactic, such as a fake [K
"urgent" message
    if re.search(r"\b(important|time sensitive|urgent|hurry|action required[8D[K
required)\b", email.subject):
        return True

    # Check if the email contains a suspicious attachment or file
    for part in email.parts:
        if part["Content-Disposition"] and \
                re.search(r"filename=\S*[.]exe|[.]zip|[.]rar", part["Conten[12D[K
part["Content-Disposition"]):
            return True

    # Check if the email contains a suspicious HTML content
    if re.search(r"<script.*?</script>", email.content):
        return True

    # If all checks pass, it's probably not a phishing attempt
    return False

def mitigate_phishing_attempt(email):
    # Send a report to the sender and recipient
    report = "This is an automated response to notify you that we have dete[4D[K
detected a potential phishing attempt. Please do not click on any links or [K
download any attachments from this email."
    smtplib.sendmail(email.sender, [email.sender, email.recipient], report)[7D[K
report)

def main():
    # Parse the incoming email and extract its relevant parts
    email = parse_email(sys.stdin.read())

    # Check if it's a phishing attempt
    if is_phishing_attempt(email):
        mitigate_phishing_attack(email)

if __name__ == "__main__":
    main()