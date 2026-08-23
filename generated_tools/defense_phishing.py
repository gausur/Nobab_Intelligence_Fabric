#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-23 23:14:49.317457

import requests
import re

def detect_phishing(url):
    try:
        r = requests.get(url)
        html = r.text
        if re.search(r"<script>|<style>|<iframe>", html):
            return True
        else:
            return False
    except:
        return False

def mitigate_phishing(url):
    try:
        r = requests.get(url)
        html = r.text
        if re.search(r"<script>|<style>|<iframe>", html):
            return url + "?phish=true"
        else:
            return url
    except:
        return url

url = "https://example.com"
if detect_phishing(url):
    print("This URL is a phishing site!")
else:
    print("This URL is safe!")