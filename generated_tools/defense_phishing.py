#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-10-18 16:18:17.461671

import re
import sys
import json

# Define a regular expression to match phishing links
PHISHING_REGEX = r"^(?:http|https)://[\w-]+(?:(?:\.[\w-]+)+|:80|:443)(?:/[\[58D[K
r"^(?:http|https)://[\w-]+(?:(?:\.[\w-]+)+|:80|:443)(?:/[\w-./?%&=]*)?$"

# Define a function to check if a link is phishing
def is_phishing(link):
    return re.match(PHISHING_REGEX, link)

# Define a function to mitigate phishing attacks
def mitigate(link):
    if is_phishing(link):
        print("This link is a phishing attempt!")
    else:
        print("This link is safe.")

# Get the command-line arguments
args = sys.argv[1:]

# Check if there are any command-line arguments
if len(args) == 0:
    print("Usage: python phishing_detection.py <link>")
    sys.exit(1)

# Get the link from the command-line arguments
link = args[0]

# Check if the link is phishing
mitigate(link)