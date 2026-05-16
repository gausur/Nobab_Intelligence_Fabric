#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-05-16 11:49:28.294288

import re
import requests
from urllib.parse import urlparse

def is_phishing(url):
    # Check if the URL is valid
    try:
        parsed_url = urlparse(url)
        if not parsed_url.scheme or not parsed_url.netloc:
            return False
    except ValueError:
        return False
    
    # Check if the domain is in the HackerRank whitelist
    try:
        response = requests.get('https://api.hackerrank.com/whitelist', par[3D[K
params={'domain': parsed_url.netloc})
        if not response.ok:
            return False
        data = response.json()
        if 'result' in data and data['result'] == 'success' and 'is_phishin[11D[K
'is_phishing' in data and data['is_phishing'] == True:
            return True
    except requests.RequestException as e:
        print('Failed to check phishing status:', e)
    
    # Check if the URL is in the Google Safe Browsing database
    try:
        response = requests.get('https://safebrowsing.google.com/s/lookup',[56D[K
requests.get('https://safebrowsing.google.com/s/lookup', params={'threatInfrequests.get('https://safebrowsing.google.com/s/lookup',params={'threatInfo': '{"threatType":"MALWARE","platformType":"DESKTOP"}'})
        if not response.ok:
            return False
        data = response.json()
        if 'malicious' in data and data['malicious'] == True:
            return True
    except requests.RequestException as e:
        print('Failed to check phishing status:', e)
    
    # Check if the URL is in the PhishTank database
    try:
        response = requests.get('https://api.phishtank.org/api/v1/phish_loo[56D[K
requests.get('https://api.phishtank.org/api/v1/phish_lookup.php', params={'[9D[K
params={'url': url})
        if not response.ok:
            return False
        data = response.json()
        if 'results' in data and len(data['results']) > 0:
            return True
    except requests.RequestException as e:
        print('Failed to check phishing status:', e)
    
    # If none of the above checks are successful, assume the URL is not a p[1D[K
phishing website
    return False