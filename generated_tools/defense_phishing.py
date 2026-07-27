#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-27 02:05:56.979690

import requests
from bs4 import BeautifulSoup

def is_phishing_site(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        forms = soup.findAll("form")
        for form in forms:
            if form.has_attr("action"):
                action = form["action"]
                if not action.startswith("https://") and not action.startsw[14D[K
action.startswith("http://"):
                    return True
        return False
    except Exception:
        return False

def mitigate_phishing_attack(url):
    if is_phishing_site(url):
        print("Phishing site detected!")
    else:
        print("No phishing site detected.")

mitigate_phishing_attack("https://www.example.com/")