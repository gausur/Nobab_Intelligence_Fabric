#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-05-27 10:56:13.493452

import re

def is_phishing_url(url):
    """
    Detects if the given URL is a phishing site.
    """
    # Check if the URL contains any suspicious characters
    for char in ['http://', 'https://']:
        if char not in url:
            return False
    # Check if the URL is from a known phishing domain
    for domain in ['phishingsite.com', 'maliciousdomain.net']:
        if domain in url:
            return True
    # If none of the above conditions are met, it's not a phishing site
    return False

def mitigate_phishing(url):
    """
    Mitigates the given URL by redirecting to the safe browsing page.
    """
    import webbrowser
    webbrowser.open('https://safe-browsing.org/')

def main():
    url = input("Enter a URL: ")
    if is_phishing_url(url):
        mitigate_phishing(url)
    else:
        print("The URL seems safe.")

if __name__ == '__main__':
    main()