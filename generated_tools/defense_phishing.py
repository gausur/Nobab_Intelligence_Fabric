#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-11-19 19:23:35.183923

import re
import requests

def detect_phishing(url):
    try:
        response = requests.get(url, timeout=5)
        html = response.text
        if re.search(r"<title>.*?</title>", html):
            title = re.search(r"<title>.*?</title>", html).group(0)
            if re.search(r"phishing", title, re.IGNORECASE):
                return True
        if re.search(r"<meta name=\".*?\" content=\".*?\">", html):
            meta = re.search(r"<meta name=\".*?\" content=\".*?\">", html).group(0)
            if re.search(r"phishing", meta, re.IGNORECASE):
                return True
        return False
    except requests.exceptions.Timeout:
        return False

def mitigate_phishing(url):
    if detect_phishing(url):
        return "Phishing detected"
    else:
        return "No phishing detected"