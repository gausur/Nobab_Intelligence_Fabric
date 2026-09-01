#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-09-01 19:04:00.169322

import re

def is_phishing_url(url):
    """
    Check if a URL is a phishing website.
    """
    # Check if the URL contains any suspicious keywords
    keywords = ["free", "discount", "coupons", "gift", "survey", "win", "sc[3D[K
"scam", "fake", "phishing"]
    for keyword in keywords:
        if keyword in url:
            return True
    return False

def mitigate_phishing_attack(url):
    """
    Mitigate a phishing attack by blocking the URL.
    """
    # Block the URL using a firewall
    firewall = ["iptables", "-I", "INPUT", "DROP", "PROTO=tcp", "dport=80"][11D[K
"dport=80"]
    subprocess.run(firewall)

def main():
    # Get the URL from the user
    url = input("Enter the URL: ")

    # Check if the URL is a phishing website
    if is_phishing_url(url):
        # Mitigate the phishing attack by blocking the URL
        mitigate_phishing_attack(url)
        print("Phishing attack detected! URL blocked.")
    else:
        print("No phishing attack detected.")

if __name__ == "__main__":
    main()