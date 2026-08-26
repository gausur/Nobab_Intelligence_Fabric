#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-26 13:47:47.187864

import re
import requests

def detect_phishing(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            content = response.content.decode("utf-8")
            if re.search(r"[a-zA-Z0-9]{5,}", content):
                print("Possible phishing attack detected!")
                return True
            else:
                return False
        else:
            print("Error fetching URL")
            return False
    except requests.exceptions.ConnectionError:
        print("Error connecting to the server")
        return False

def main():
    url = input("Enter the URL to check: ")
    if detect_phishing(url):
        print("Phishing attack detected!")
    else:
        print("No phishing attack detected.")

if __name__ == "__main__":
    main()