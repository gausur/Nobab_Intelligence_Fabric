#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-11 07:14:02.610236

import re
import requests
from bs4 import BeautifulSoup

def detect_phishing(url):
    # Check if the URL is valid
    try:
        r = requests.get(url)
        soup = BeautifulSoup(r.content, "html.parser")
    except requests.exceptions.RequestException as e:
        print("Invalid URL:", e)
        return
    
    # Check for suspicious HTTP headers
    if r.headers["Content-Type"] != "text/html":
        print("Suspicious Content-Type header detected.")
        return
    if r.headers["Server"] != "Apache/2.4.7 (Ubuntu) Server at example.com [K
Port 80":
        print("Suspicious Server header detected.")
        return
    
    # Check for suspicious HTML tags and attributes
    tags = soup.find_all(["script", "iframe", "link", "a"])
    for tag in tags:
        if tag.name == "script":
            if tag.attrs.get("src"):
                print("Suspicious script tag with src attribute detected.")[11D[K
detected.")
            elif tag.text.strip():
                print("Suspicious script tag with non-empty text content de[2D[K
detected.")
        elif tag.name == "iframe":
            if tag.attrs.get("src"):
                print("Suspicious iframe tag with src attribute detected.")[11D[K
detected.")
            elif tag.text.strip():
                print("Suspicious iframe tag with non-empty text content de[2D[K
detected.")
        elif tag.name == "link":
            if tag.attrs.get("href"):
                print("Suspicious link tag with href attribute detected.")
            elif tag.text.strip():
                print("Suspicious link tag with non-empty text content dete[4D[K
detected.")
        else:
            print("Suspicious {} tag detected.".format(tag.name))
    
    # Check for suspicious URLs in the HTML content
    urls = soup.find_all("a")
    for url in urls:
        if not re.match(r"https?://[^\s]+", url["href"]):
            print("Suspicious URL detected.")
    
    # Check for suspicious HTTP status codes
    if r.status_code != 200:
        print("Suspicious HTTP status code detected: {}.".format(r.status_c[22D[K
{}.".format(r.status_code))

# Example usage:
detect_phishing("https://www.example.com")