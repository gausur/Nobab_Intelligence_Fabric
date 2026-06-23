#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-06-23 23:04:59.233561

import re
import requests
from bs4 import BeautifulSoup

# Define the list of URLs that are considered safe
safe_urls = ['https://www.google.com', 'https://www.yahoo.com']

def is_phishing(url):
    # Check if the URL is in the list of safe URLs
    if url in safe_urls:
        return False
    
    # Get the HTML content of the page using requests
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Check for common phishing indicators such as suspicious domains or li[2D[K
links
    if soup.find('a', href=re.compile('.*\.phishing')):
        return True
    
    # Check for social engineering tactics such as fake logins or registrat[9D[K
registration forms
    if soup.find('form', action=re.compile('.*login')) and soup.find('form'[16D[K
soup.find('form', action=re.compile('.*register')):
        return True
    
    # Check for common phishing patterns such as the use of misleading head[4D[K
headings or subtle color changes
    if len(soup.find_all('h1')) > 1 or len(soup.find_all('h2')) > 0 or len([4D[K
len(soup.find_all('h3')) > 0:
        return True
    
    # Check for the use of misleading language or spelling errors
    if soup.find('span', {'class': re.compile('.*text-muted')}):
        return True
    
    # Check for the use of a white screen with a message at the bottom, ind[3D[K
indicating that the page has been redirected
    if len(soup.find_all('p', {'style': re.compile('.*white.*')})) > 0:
        return True
    
    return False

def mitigate(url):
    # Display a warning message to the user
    print("Warning! This website may be attempting to phish you.")
    
    # Ask the user if they want to proceed with the connection
    proceed = input("Do you want to proceed? (y/n): ")
    
    # If the user says no, exit the program
    if proceed.lower() != 'y':
        print("Exiting...")
        exit(0)
    
    # Otherwise, proceed with the connection
    else:
        return url

# Get the URL from the user and pass it to the is_phishing function
url = input("Enter a URL: ")
if is_phishing(url):
    mitigate(url)
else:
    print("This website is safe.")