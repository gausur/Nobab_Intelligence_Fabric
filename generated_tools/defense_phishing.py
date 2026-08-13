#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-13 17:53:50.630060

import re
import urllib.parse
from collections import deque

def is_phishing(url):
    # Check if the URL is valid
    try:
        parsed_url = urllib.parse.urlparse(url)
    except ValueError:
        return False

    # Check if the domain is in the Public Suffix List
    if not parsed_url.netloc or parsed_url.netloc[-1] != ".":
        return False

    public_suffix = urllib.parse.publicsuffix(parsed_url.netloc)
    if public_suffix is None:
        return False

    # Check if the URL contains any suspicious patterns
    for pattern in SUSPICIOUS_PATTERNS:
        if re.search(pattern, url):
            return True

    return False

def mitigate_phishing(url):
    # Remove any suspicious query parameters
    parsed_url = urllib.parse.urlparse(url)
    new_query = {}
    for key, value in parse.parse_qs(parsed_url.query).items():
        if key not in SUSPICIOUS_QUERY_PARAMETERS:
            new_query[key] = value

    new_url = parsed_url._replace(query=urllib.parse.urlencode(new_query, d[1D[K
doseq=True))
    return urllib.parse.urlunparse(new_url)

def main():
    # Load the Public Suffix List and suspicious patterns
    with open("psl.txt", "r") as f:
        psl = [line.strip() for line in f]
    with open("suspicious_patterns.txt", "r") as f:
        suspicious_patterns = [re.compile(line) for line in f]

    # Create a queue of URLs to check
    urls = deque([url])

    # Iterate over the queue and check each URL
    while len(urls) > 0:
        url = urls.popleft()
        if is_phishing(url):
            mitigated_url = mitigate_phishing(url)
            print(f"Phishing attempt detected for {url}. Mitigating...")
            print(f"Mitigated URL: {mitigated_url}")
        else:
            print(f"URL is safe: {url}")

if __name__ == "__main__":
    main()