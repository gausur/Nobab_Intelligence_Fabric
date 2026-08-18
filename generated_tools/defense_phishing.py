#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-18 00:46:27.419986

import re
import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup

def detect_phishing(url):
    try:
        # Parse the URL and extract the domain
        url_parsed = urlparse(url)
        domain = url_parsed.netloc

        # Check if the domain is in the list of known phishing domains
        if domain in PHISHING_DOMAINS:
            return True

        # Fetch the HTML page and extract the links
        html = requests.get(url).text
        soup = BeautifulSoup(html, "html.parser")
        links = [link["href"] for link in soup.find_all("a")]

        # Check if any of the links are to a known phishing domain
        for link in links:
            if link.startswith("http"):
                link_parsed = urlparse(link)
                link_domain = link_parsed.netloc
                if link_domain in PHISHING_DOMAINS:
                    return True

        # If we reach this point, the URL is not a phishing site
        return False
    except requests.exceptions.RequestException:
        # If we encounter any errors, return False
        return False

# List of known phishing domains
PHISHING_DOMAINS = [
    "example.com",
    "example2.com",
    "example3.com",
    "example4.com",
]