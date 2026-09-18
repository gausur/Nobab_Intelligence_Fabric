#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-09-18 19:22:54.415700

import re

def is_phishing_url(url):
    return re.match(r"https?:\/\/(www\.)?phishing\.com", url)

def mitigate_phishing_attack(url):
    if is_phishing_url(url):
        print("Phishing attack detected!")
    else:
        print("No phishing attack detected.")

def main():
    mitigate_phishing_attack("https://www.example.com")

if __name__ == "__main__":
    main()