#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-21 01:53:49.347243

import re
import requests
from bs4 import BeautifulSoup

def is_phishing(url):
    # Check if the URL is valid
    if not url.startswith('http'):
        return False
    
    # Send a HEAD request to get the response headers only
    try:
        resp = requests.head(url, allow_redirects=True)
    except requests.exceptions.RequestException:
        return False
    
    # Check if the response is valid
    if not resp.ok or 'Content-Type' not in resp.headers:
        return False
    
    # Get the content type of the page
    content_type = resp.headers['Content-Type']
    
    # Check if the content type is a text/html document
    if 'text/html' not in content_type:
        return False
    
    # Send another HEAD request to get the final URL
    try:
        final_url = resp.headers['Location']
    except KeyError:
        final_url = url
    
    # Check if the final URL is a phishing site
    if not is_phishing(final_url):
        return False
    
    # Get the HTML of the page
    try:
        resp = requests.get(final_url)
    except requests.exceptions.RequestException:
        return False
    
    # Check if the response is valid
    if not resp.ok or 'Content-Type' not in resp.headers:
        return False
    
    # Get the HTML of the page
    html = resp.text
    
    # Check for phishing patterns in the HTML
    soup = BeautifulSoup(html, 'lxml')
    
    # Check if the page contains a form with an action attribute
    form = soup.find('form', attrs={'action': re.compile(r'^https://.*\.com[29D[K
re.compile(r'^https://.*\.com/.*$')})
    if not form:
        return False
    
    # Check if the form has a field with a name attribute
    input_field = form.find('input', attrs={'name': re.compile(r'^username|[23D[K
re.compile(r'^username|email$')})
    if not input_field:
        return False
    
    # Check if the page contains a link to a website other than the final U[1D[K
URL
    links = soup.find_all('a')
    for link in links:
        href = link.attrs['href']
        if not href.startswith(final_url):
            return False
    
    # Check if the page contains a meta tag with a refresh attribute
    meta = soup.find('meta', attrs={'http-equiv': 'refresh'})
    if meta:
        return False
    
    return True