#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-28 00:02:54.718506

import re
import requests
from bs4 import BeautifulSoup

def is_phishing(url):
    """Check if the URL is a phishing site"""
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        title = soup.title.string
        if "phishing" in title.lower():
            return True
        else:
            return False
    except requests.exceptions.RequestException:
        return None

def mitigate_phishing(url):
    """Mitigate phishing attacks by blocking the URL"""
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        title = soup.title.string
        if "phishing" in title.lower():
            print("Blocking phishing site:", url)
            return False
        else:
            return True
    except requests.exceptions.RequestException:
        return None