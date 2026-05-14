#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-05-14 16:08:38.365552

import re
import urllib.parse
import requests
from bs4 import BeautifulSoup

def is_phishing(url):
    # Check if the URL contains any suspicious keywords or patterns
    for keyword in ["phish", "scam", "fake"]:
        if keyword in url:
            return True
    
    # Check if the domain name is registered as a phishing domain
    try:
        domain = urllib.parse.urlsplit(url).netloc
        whois_data = requests.get("https://www.whois.com/whois/" + domain).[8D[K
domain).text
        for line in whois_data.split("\n"):
            if "phishing" in line.lower():
                return True
    except:
        pass
    
    # Check the HTML content of the page for suspicious attributes or eleme[5D[K
elements
    try:
        response = requests.get(url)
        html = BeautifulSoup(response.content, "html.parser")
        for tag in ["a", "link"]:
            if html.find_all(tag, href=re.compile("^http://")):
                return True
    except:
        pass
    
    # If none of the above checks yielded a positive result, the URL is lik[3D[K
likely legitimate
    return False