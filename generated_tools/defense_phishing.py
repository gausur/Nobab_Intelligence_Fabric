#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-10-15 20:47:39.622438

import re
import urllib

def detect_phishing(url):
    # Check if the URL is valid
    if not urllib.parse.urlparse(url).scheme:
        return False

    # Check if the URL contains a suspicious domain
    domain = urllib.parse.urlparse(url).netloc
    if domain.lower().endswith('google.com'):
        return True

    # Check if the URL contains a suspicious path
    path = urllib.parse.urlparse(url).path
    if re.search(r'/phishing-page\.html$', path):
        return True

    # Check if the URL contains a suspicious parameter
    params = urllib.parse.urlparse(url).query
    if re.search(r'param=value', params):
        return True

    return False

def mitigate_phishing(url):
    # Replace the URL with a safe one
    safe_url = url.replace('google.com', 'example.com')
    safe_url = safe_url.replace('phishing-page.html', 'index.html')
    safe_url = safe_url.replace('param=value', 'param=safe')
    return safe_url

def main():
    # Get the URL from the user
    url = input("Enter the URL: ")

    # Detect and mitigate phishing attacks
    if detect_phishing(url):
        print("The URL is a phishing site.")
        url = mitigate_phishing(url)
    else:
        print("The URL is not a phishing site.")

    # Print the safe URL
    print(url)

if __name__ == '__main__':
    main()