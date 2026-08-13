#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-13 14:19:14.500456

import requests
from bs4 import BeautifulSoup

def is_phishing(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        if "phish" in soup.text.lower():
            return True
        else:
            return False
    except requests.exceptions.ConnectionError as e:
        print("Failed to connect to {}: {}".format(url, str(e)))
        return False

def mitigate_phishing(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        if is_phishing(url):
            print("Possible phishing attack detected!")
        else:
            print("No phishing attacks detected.")
    except requests.exceptions.ConnectionError as e:
        print("Failed to connect to {}: {}".format(url, str(e)))