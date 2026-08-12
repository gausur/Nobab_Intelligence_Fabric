#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-12 18:54:50.057444

import re
import urllib.request
import json
from collections import defaultdict

def extract_domains(text):
    """Extract all domains from a piece of text"""
    return re.findall(r'https?://([^\s]+)', text)

def is_phishing_domain(domain):
    """Check if a domain is on the PhishTank blacklist"""
    try:
        url = f'https://api.phishtank.org/v1/data?url={domain}&fields=url,p[61D[K
f'https://api.phishtank.org/v1/data?url={domain}&fields=url,phish_id'
        response = json.loads(urllib.request.urlopen(url).read())
        if response['results']:
            return True
    except:
        pass
    return False

def mitigate_phishing(text):
    """Replace any phishing domains in the text with a placeholder"""
    for domain in extract_domains(text):
        if is_phishing_domain(domain):
            text = re.sub(f'{domain}', '<PHISHING_DOMAIN>', text)
    return text

def main():
    """Main function"""
    with open('input.txt') as f:
        content = f.read()
    mitigated_content = mitigate_phishing(content)
    with open('output.txt', 'w') as f:
        f.write(mitigated_content)

if __name__ == '__main__':
    main()