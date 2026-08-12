#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-12 22:37:46.659420

import re
import requests

def is_phishing_site(url):
    """
    Detects if the given URL is a phishing site by checking for common phis[4D[K
phishing patterns.

    Args:
        url (str): The URL to check.

    Returns:
        bool: True if the URL is a phishing site, False otherwise.
    """
    pattern = re.compile(r"(^|\.)(g(oogle|mail))\.com$")
    return pattern.match(url) or url.endswith(".onion")

def mitigate_phishing_attack(ip):
    """
    Mitigates a phishing attack by blocking the IP address of the attacker.[9D[K
attacker.

    Args:
        ip (str): The IP address of the attacker.

    Returns:
        None
    """
    requests.post("http://localhost:8080/block_ip", json={"ip": ip})

def main():
    url = input("Enter URL to check: ")
    if is_phishing_site(url):
        print("Phishing site detected!")
        mitigate_phishing_attack(get_ip_from_url(url))
    else:
        print("No phishing site detected.")

if __name__ == "__main__":
    main()