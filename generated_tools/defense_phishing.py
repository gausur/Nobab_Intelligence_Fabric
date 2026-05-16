#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-05-16 13:04:44.822898

import re
import requests
from bs4 import BeautifulSoup

def is_phishing(url):
    # Check if the URL is a valid HTTP or HTTPS URL
    if not (url.startswith("http://") or url.startswith("https://")):
        return False

    # Make an HTTP request to the URL and get the HTML response
    try:
        response = requests.get(url)
    except Exception as e:
        print("Failed to fetch URL:", e)
        return False

    # Check if the HTML response contains any suspicious strings or tags
    soup = BeautifulSoup(response.text, "html.parser")
    for tag in soup.find_all():
        if re.search(r"phishing|scam|fraud", tag.string):
            return True

    # Check if the URL is hosted on a known phishing website
    try:
        whois = requests.get("https://api.hackertarget.com/whois/?q={}".for[59D[K
requests.get("https://api.hackertarget.com/whois/?q={}".format(url)).text
    except Exception as e:
        print("Failed to fetch WHOIS info:", e)
        return False

    if re.search(r"phishing|scam|fraud", whois):
        return True

    return False