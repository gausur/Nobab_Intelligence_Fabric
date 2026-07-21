#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-21 18:16:07.398311

import re
import urllib.parse
from typing import List

def extract_urls(text: str) -> List[str]:
    """Extract URLs from a piece of text."""
    return re.findall(r"https?://\S+", text)

def is_phishing_url(url: str) -> bool:
    """Check if the URL is a phishing site."""
    # Check if the URL contains any suspicious subdomains or parameters
    for domain in ["fake", "gamers", "scam", "paypal"]:
        if domain in urllib.parse.urlparse(url).netloc:
            return True
    for parameter in ["verify=false", "payment_method=creditcard"]:
        if parameter in urllib.parse.urlparse(url).query:
            return True
    # Check if the URL is a known phishing site
    with open("phishing_sites.txt") as f:
        for line in f:
            if line.strip() == url:
                return True
    return False

def mitigate_phishing(text: str) -> str:
    """Mitigate phishing attacks by removing URLs from the text."""
    urls = extract_urls(text)
    for url in urls:
        if is_phishing_url(url):
            text = text.replace(url, "REDACTED")
    return text

def main():
    with open("input.txt", "r") as f:
        text = f.read()
    mitigated_text = mitigate_phishing(text)
    with open("output.txt", "w") as f:
        f.write(mitigated_text)

if __name__ == "__main__":
    main()