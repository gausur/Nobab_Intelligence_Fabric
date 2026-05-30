#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-05-30 16:11:12.115003

import re
import requests
from bs4 import BeautifulSoup

def is_phishing(url):
    """Check if the URL is a phishing site"""
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        # Check for suspicious keywords in the page source
        keywords = ["phish", "scam", "fraud", "paypal"]
        for keyword in keywords:
            if keyword in soup.text:
                return True
        # Check for suspicious domain names
        if "." in url and url.split(".")[-2] != "com":
            return True
    except requests.exceptions.RequestException:
        pass
    return False

def mitigate_phishing(url):
    """Mitigate phishing attacks by redirecting to a safe page"""
    if is_phishing(url):
        # Redirect to a safe page
        print("Redirecting to a safe page...")
        return "https://www.example.com/safe-page"
    else:
        # Return the original URL
        return url

def main():
    """Main function"""
    # Get the input URL from the user
    url = input("Enter the URL: ")
    # Check if the URL is a phishing site and mitigate it if necessary
    mitigated_url = mitigate_phishing(url)
    print(f"The original URL is {url}. The mitigated URL is {mitigated_url}[15D[K
{mitigated_url}")

if __name__ == "__main__":
    main()