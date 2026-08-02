#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-02 13:03:26.911567

import re
import requests
from bs4 import BeautifulSoup

def is_phishing_attempt(url):
    # Check if the URL is valid
    if not url or not re.match(r'^https?://', url):
        return False

    # Send a HEAD request to the URL and check the status code
    response = requests.head(url)
    if response.status_code != 200:
        return False

    # Get the HTML content of the page and parse it using BeautifulSoup
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'lxml')

    # Check for common phishing tactics such as misleading titles, suspicio[8D[K
suspicious URLs, and missing security certificates
    if not soup.title or soup.title.string.lower().startswith('phish'):
        return True
    if not soup.find('img', {'src': re.compile(r'^https?://')):
        return True
    if not soup.find('script', {'src': re.compile(r'^https?://')}):
        return True
    if not soup.find('link', {'href': re.compile(r'^https?://'), 'rel': 'st[3D[K
'stylesheet'}):
        return True
    if soup.find('input', {'type': 'password', 'value': re.compile(r'^https[19D[K
re.compile(r'^https?://')}):
        return True
    if soup.find('a', {'href': re.compile(r'^https?://'), 'text': 'Login'})[9D[K
'Login'}):
        return True
    if soup.find('form', {'action': re.compile(r'^https?://')}):
        return True

    # If the URL is not a phishing attempt, check for suspicious page conte[5D[K
content
    if not soup.find('h1', {'class': 'page-title'}):
        return False
    if not soup.find('p', {'class': 'page-description'}):
        return False
    if not soup.find('div', {'id': 'content'}):
        return False

    # If the URL is a phishing attempt, block it and display an error messa[5D[K
message to the user
    print('Phishing attack detected!')
    return True

# Test the function with some example URLs
url = 'http://www.example.com'
print(is_phishing_attempt(url))  # Should output "False"

url = 'http://www.evil-phishing.com'
print(is_phishing_attempt(url))  # Should output "True"