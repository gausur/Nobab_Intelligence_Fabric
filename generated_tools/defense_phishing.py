#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-05-16 07:55:17.648058

import re
import requests
from bs4 import BeautifulSoup

def is_phishing_url(url):
    # Check if the URL is valid
    try:
        response = requests.get(url)
        if response.status_code != 200:
            return False
    except requests.exceptions.RequestException as e:
        print("Error: {}".format(e))
        return False

    # Parse the HTML content of the URL
    soup = BeautifulSoup(response.content, "html.parser")

    # Check if the page contains any suspicious elements
    for element in soup.find_all():
        # Skip over non-phishing elements
        if not isinstance(element, str):
            continue

        # Check if the element is a known phishing URL
        if re.search(r"https://login\.facebook\.com/login\.php", element):
            return True

    # No suspicious elements found
    return False

def mitigate_phishing_attack(url, username, password):
    # Check if the URL is a phishing attack
    if is_phishing_url(url):
        print("Phishing attempt detected!")
        return

    # Proceed with logging in normally
    login_data = {
        "username": username,
        "password": password
    }

    response = requests.post(url + "/login", data=login_data)
    if response.status_code != 200:
        print("Login failed!")
        return

    # Login successful, proceed with the application
    print("Login successful!")
    return

def main():
    url = input("Enter the URL to login to: ")
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    mitigate_phishing_attack(url, username, password)

if __name__ == "__main__":
    main()