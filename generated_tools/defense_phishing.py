#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-05-19 13:54:56.502318

import re
import requests
from bs4 import BeautifulSoup

def is_phishing(url):
    # Check if the URL is valid
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
    except requests.exceptions.RequestException as e:
        print('Error:', e)
        return False

    # Check if the URL contains suspicious keywords or phrases
    keywords = ['phishing', 'scam', 'fraud']
    for keyword in keywords:
        if keyword in url:
            return True

    # Check if the page contains a meta tag with a description of the websi[5D[K
website
    meta_description = soup.find('meta', {'name': 'description'})
    if not meta_description:
        return False

    # Check if the meta description contains suspicious keywords or phrases[7D[K
phrases
    for keyword in keywords:
        if keyword in meta_description['content']:
            return True

    # Check if the page contains a form that is not secure (HTTPS)
    forms = soup.find_all('form')
    for form in forms:
        if form['action'].startswith('http://'):
            return True

    # Check if the page contains an image with a suspicious filename or ext[3D[K
extension
    images = soup.find_all('img')
    for image in images:
        filename = image['src']
        if re.search(r'[\\\/]', filename) or not re.search(r'\.(jpg|jpeg|pn[26D[K
re.search(r'\.(jpg|jpeg|png|gif)$', filename):
            return True

    # Check if the page contains a link to an external website (domain diff[4D[K
different from the URL)
    links = soup.find_all('a')
    for link in links:
        if not link['href'].startswith(url):
            return True

    # If none of the above checks failed, then it's likely a legitimate web[3D[K
website
    return False