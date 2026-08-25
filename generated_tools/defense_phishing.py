#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-25 07:40:45.206911

import re
import smtplib

# Regex to match phishing emails
phishing_regex = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}"

# Function to check if email is phishing
def is_phishing(email):
    if re.match(phishing_regex, email):
        return True
    else:
        return False

# Function to send email to the recipient
def send_email(recipient, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("your_email@gmail.com", "your_email_password")
    server.sendmail("your_email@gmail.com", recipient, message)
    server.quit()

# Main function
def main():
    # Get the email from the user
    email = input("Enter the email: ")

    # Check if the email is phishing
    if is_phishing(email):
        # Send an email to the recipient
        send_email(email, "This is a phishing email. Please do not click an[2D[K
any links or provide any personal information.")
        print("Phishing attack detected. Email has been sent to the recipie[7D[K
recipient.")
    else:
        # If the email is not phishing, print a message
        print("This is not a phishing email. You can continue to browse the[3D[K
the website.")

if __name__ == "__main__":
    main()