#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-11 11:49:05.567560

import re
import requests
from bs4 import BeautifulSoup

def is_phishing_url(url):
    # Check if the URL contains any suspicious keywords or patterns
    if "https://" in url:
        return False
    elif "http://" in url:
        return True
    else:
        raise ValueError("Invalid URL")

def get_url_content(url):
    # Send a GET request to the URL and retrieve the response content
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        raise ValueError("Failed to fetch URL")

def get_suspicious_patterns(content):
    # Check for suspicious patterns in the content using regular expression[10D[K
expressions
    patterns = ["http://", "https://"]
    for pattern in patterns:
        if re.search(pattern, content):
            return True
    return False

def get_suspicious_keywords(content):
    # Check for suspicious keywords in the content using regular expression[10D[K
expressions
    keywords = ["phishing", "scam", "fraud"]
    for keyword in keywords:
        if re.search(keyword, content):
            return True
    return False

def detect_phishing_attacks():
    # Detect phishing attacks by checking the URL and content of a website
    url = input("Enter the URL to check: ")
    content = get_url_content(url)
    if is_phishing_url(url):
        print("Phishing attack detected!")
        return True
    elif get_suspicious_patterns(content) or get_suspicious_keywords(conten[30D[K
get_suspicious_keywords(content):
        print("Suspicious URL or content detected!")
        return False
    else:
        print("No phishing attack detected.")
        return True

if __name__ == "__main__":
    detect_phishing_attacks()