#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-22 22:05:42.145709

import re
import urllib.parse
import requests
from bs4 import BeautifulSoup

def is_phishing(url):
    # Check if the URL is valid and has a domain
    try:
        parsed_url = urllib.parse.urlparse(url)
        domain = parsed_url.netloc
        if not domain:
            return False
    except ValueError:
        return False

    # Make a request to the URL and get the HTML content
    try:
        response = requests.get(url)
        html = response.content
    except requests.exceptions.RequestException:
        return False

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")

    # Check if the URL contains any suspicious elements
    for element in soup.find_all():
        if is_suspicious(element):
            return True

    # Check if the domain is known to be a phishing site
    if is_known_phishing_site(domain):
        return True

    # If none of the above criteria are met, then the URL is not a phishing[8D[K
phishing site
    return False

def is_suspicious(element):
    # Check if the element contains any suspicious attributes or text conte[5D[K
content
    for attribute in element.attrs:
        if is_suspicious_attribute(attribute):
            return True
    for child in element.children:
        if is_suspicious_content(child.string):
            return True
    return False

def is_suspicious_attribute(attribute):
    # Check if the attribute name contains any suspicious characters or val[3D[K
values
    if re.search(r"[\W_]", attribute[0]):
        return True
    if re.search(r"^on\w+", attribute[0]):
        return True
    if re.search(r"\bhref\s*=\s*(['\"])javascript:", attribute[1]):
        return True
    return False

def is_suspicious_content(content):
    # Check if the content contains any suspicious patterns or values
    if re.search(r"[\W_]", content):
        return True
    if re.search(r"\bjavascript:", content, re.IGNORECASE):
        return True
    if re.search(r"\bbase64\(", content):
        return True
    return False

def is_known_phishing_site(domain):
    # Check if the domain is known to be a phishing site by checking a blac[4D[K
blacklist
    with open("phishing_sites.txt", "r") as f:
        for line in f:
            if domain == line.strip():
                return True
    return False