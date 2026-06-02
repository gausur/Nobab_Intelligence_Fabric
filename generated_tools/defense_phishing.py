#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-02 21:47:01.627525

import re
import urllib
import requests

def is_phishing(url):
    """
    Check if the given URL is a phishing website.
    Return True if it is, False otherwise.
    """
    # Check if the URL contains any suspicious keywords
    if any(keyword in url for keyword in ["free", "discount", "gift", "scam[5D[K
"scam"]):
        return True
    
    # Check if the URL is a redirect to another website
    try:
        resp = requests.head(url)
        location = resp.headers["Location"]
        if urllib.parse.urlparse(location).hostname != urllib.parse.urlpars[20D[K
urllib.parse.urlparse(url).hostname:
            return True
    except requests.exceptions.RequestException:
        pass
    
    # Check if the URL is a valid SSL certificate
    try:
        resp = requests.get(url)
        if not resp.ok or "https" not in url or "www." not in url:
            return True
    except requests.exceptions.RequestException:
        pass
    
    # If the URL is not a phishing website, check if it contains any suspic[6D[K
suspicious content
    try:
        resp = requests.get(url)
        if re.search("[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}", res[3D[K
resp.text):
            return True
    except requests.exceptions.RequestException:
        pass
    
    # If the URL is not a phishing website and does not contain any suspici[7D[K
suspicious content, it is likely safe
    return False

def main():
    """
    Main function to test the is_phishing function.
    """
    urls = ["https://www.example.com", "http://www.example.com"]
    for url in urls:
        if is_phishing(url):
            print(f"{url} is a phishing website.")
        else:
            print(f"{url} is not a phishing website.")

if __name__ == "__main__":
    main()