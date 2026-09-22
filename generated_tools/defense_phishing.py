#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-09-22 10:43:09.688045

import re
import smtplib

def is_phishing_email(email):
    """
    Check if the given email is a phishing email.

    Args:
        email (str): The email address to check.

    Returns:
        bool: True if the email is a phishing email, False otherwise.
    """
    # Check if the email is valid
    if not re.match(r"^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$", email):
        return False

    # Check if the email is from a known phishing domain
    if email.split("@")[1] in ["phishing.com", "phishing.net", "phishing.or[12D[K
"phishing.org"]:
        return True

    return False

def mitigate_phishing_email(email):
    """
    Mitigate a phishing email.

    Args:
        email (str): The email address to mitigate.
    """
    # Mark the email as spam
    smtplib.SMTP("smtp.gmail.com", 587)
    smtplib.starttls()
    smtplib.login("spam@gmail.com", "spampassword")
    smtplib.sendmail("spam@gmail.com", email, "This is a spam email.")

def main():
    """
    Main function to run the script.
    """
    email = input("Enter email address: ")

    if is_phishing_email(email):
        mitigate_phishing_email(email)
        print("Phishing email mitigated.")
    else:
        print("Not a phishing email.")

if __name__ == "__main__":
    main()