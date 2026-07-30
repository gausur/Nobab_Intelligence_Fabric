#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-07-30 23:57:04.043128

import re
import requests

def is_phishing(url):
    if not url:
        return False
    parsed = urlparse(url)
    domain = parsed.netloc
    if not domain:
        return False
    try:
        whois_data = get_whois_data(domain)
        if whois_data and "registrar" in whois_data:
            registrar = whois_data["registrar"]
            if registrar == "GoDaddy" or registrar == "Bluehost":
                return True
    except Exception as e:
        print(f"Error while checking phishing status of {url}: {e}")
    return False

def get_whois_data(domain):
    try:
        whois_response = requests.get(f"https://whois.internic.net/{domain}[50D[K
requests.get(f"https://whois.internic.net/{domain}").text
        whois_parser = whois.Parser()
        return whois_parser.parse_domains([whois_response])[0]
    except Exception as e:
        print(f"Error while retrieving WHOIS data for {domain}: {e}")

def main():
    url = "https://www.example.com"
    if is_phishing(url):
        print("This URL is a phishing site!")
    else:
        print("This URL is not a phishing site.")

if __name__ == "__main__":
    main()