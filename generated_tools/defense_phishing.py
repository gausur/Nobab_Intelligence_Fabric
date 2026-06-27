#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-27 06:27:22.709034

import re
import ssl

def is_phishing_site(url):
    # Check if the URL is HTTPS
    if not url.startswith("https"):
        return False
    
    # Extract the domain name from the URL
    domain = url.split("/")[2]
    
    # Check if the domain name is in the list of known phishing sites
    with open("phishing_sites.txt", "r") as f:
        for line in f:
            if line.strip() == domain:
                return True
    
    return False

def mitigate_phishing(url, user_input):
    # Check if the URL is a phishing site
    if is_phishing_site(url):
        print("This website is a known phishing site. Please be cautious.")[11D[K
cautious.")
    
    # Check if the user input is a valid email address
    if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", us[2D[K
user_input):
        print("Invalid email address.")
    
    # Check if the SSL certificate is valid
    try:
        ssl.get_server_certificate((domain, 443))
    except ssl.CertificateError:
        print("SSL certificate is invalid. Please make sure you are using a[1D[K
a secure connection (https://).")

def main():
    url = input("Enter the website URL: ")
    user_input = input("Enter your email address: ")
    mitigate_phishing(url, user_input)

if __name__ == "__main__":
    main()