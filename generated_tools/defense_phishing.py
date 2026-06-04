#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-04 19:17:52.274286

import re
import requests

# Define the list of allowed domains
allowed_domains = ["example1.com", "example2.com"]

# Define the regular expression pattern for detecting phishing sites
phishing_pattern = r"(?i)((?=https?:\/\/.*(paypal|amazon|google|facebook).*[56D[K
r"(?i)((?=https?:\/\/.*(paypal|amazon|google|facebook).*)\b((?:https?:\/\/)r"(?i)((?=https?:\/\/.*(paypal|amazon|google|facebook).*\b((?:https?:\/\/)?(?:www\.)?(paypal|amazon|google|facebook).*))"

# Define the regular expression pattern for detecting phishing emails
phishing_email_pattern = r"((?=From\s.*(paypal|amazon|google|facebook).*\b)[50D[K
r"((?=From\s.*(paypal|amazon|google|facebook).*\b)\b((?:From\s)*(?:www\.)?(r"((?=From\s.*(paypal|amazon|google|facebook).*\b)b((?:From\s)*(?:www\.)?(paypal|amazon|google|facebook).*))"

# Define the function to check if a URL is valid and not phishing
def validate_url(url):
    # Check if the URL is valid and not phishing
    if re.match(phishing_pattern, url) and url.startswith("http") and any(d[5D[K
any(domain in url for domain in allowed_domains):
        return True
    else:
        return False

# Define the function to check if an email is valid and not phishing
def validate_email(email):
    # Check if the email is valid and not phishing
    if re.match(phishing_email_pattern, email) and any(domain in email for [K
domain in allowed_domains):
        return True
    else:
        return False

# Define the main function to detect and mitigate phishing attacks
def detect_and_mitigate():
    # Get the user input
    url = input("Enter a URL: ")
    email = input("Enter an email address: ")
    
    # Check if the URL is valid and not phishing
    if validate_url(url):
        print("The URL is valid and not phishing.")
    else:
        print("The URL is invalid or phishing.")
    
    # Check if the email is valid and not phishing
    if validate_email(email):
        print("The email address is valid and not phishing.")
    else:
        print("The email address is invalid or phishing.")
    
# Run the main function to detect and mitigate phishing attacks
detect_and_mitigate()