#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-23 10:33:11.378370

import re
import requests
from bs4 import BeautifulSoup

def detect_phishing(url):
    # Send a request to the URL and get the HTML response
    response = requests.get(url)
    html = response.content

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")

    # Check if the HTML contains any suspicious tags or attributes
    for tag in soup.find_all("a"):
        if tag["href"].startswith("javascript:"):
            return True

    # Check if the HTML contains any suspicious CSS styles
    for style in soup.find_all("style"):
        for rule in style.text.split("\n"):
            if rule.lower().startswith("position: absolute;"):
                return True

    return False

def mitigate_phishing(url):
    # Send a request to the URL and get the HTML response
    response = requests.get(url)
    html = response.content

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")

    # Remove any suspicious tags or attributes from the HTML
    for tag in soup.find_all("a"):
        if tag["href"].startswith("javascript:"):
            del tag["href"]

    # Remove any suspicious CSS styles from the HTML
    for style in soup.find_all("style"):
        for rule in style.text.split("\n"):
            if rule.lower().startswith("position: absolute;"):
                del rule

    return soup.prettify()