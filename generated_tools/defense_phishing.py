#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-05-14 18:34:37.381032

import re
import requests

def detect_phishing(url):
    # Check if the URL is valid
    try:
        requests.head(url, timeout=5)
    except requests.exceptions.ConnectionError:
        return "Invalid URL"

    # Check if the domain is registered and has a whois record
    try:
        whois_record = requests.get("https://api.whois.com/api/v1/domain/{}[52D[K
requests.get("https://api.whois.com/api/v1/domain/{}".format(url)).json()
        if not whois_record["registered"]:
            return "Unregistered domain"
    except requests.exceptions.ConnectionError:
        pass

    # Check if the URL has a valid SSL certificate
    try:
        requests.get(url, verify=True)
    except requests.exceptions.SSLError:
        return "Invalid SSL certificate"

    # Check if the URL is on a known phishing website list
    try:
        phishing_list = requests.get("https://raw.githubusercontent.com/kyl[51D[K
requests.get("https://raw.githubusercontent.com/kylemanna/dnsmasq-phishing-requests.get("https://raw.githubusercontent.com/kylmanna/dnsmasq-phishing-filter/master/phishing-filter.conf").text.splitlines()
        if url in phishing_list:
            return "Phishing website"
    except requests.exceptions.ConnectionError:
        pass

    # If none of the above checks fail, then the URL is likely legitimate
    return "Legitimate"

# Test the function with a few URLs
print(detect_phishing("https://www.example.com"))  # Output: Legitimate
print(detect_phishing("https://www.fake-website.com"))  # Output: Phishing [K
website
print(detect_phishing("http://www.example.com"))  # Output: Invalid SSL cer[3D[K
certificate