#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-27 09:28:02.879896

import requests
from bs4 import BeautifulSoup

def is_phishing(url):
    try:
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, "html.parser")
        links = [link["href"] for link in soup.find_all("a")]
        for link in links:
            if "://" not in link or "www." in link or ".com/" in link:
                return True
        return False
    except requests.exceptions.RequestException:
        return None