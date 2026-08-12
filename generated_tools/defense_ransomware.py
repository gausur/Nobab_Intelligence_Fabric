#!/usr/bin/env python3
# Nobab AI defense for ransomware
# Generated 2026-08-12 18:52:49.422931

import os
import re
import subprocess
from pathlib import Path

# Define the directories to be scanned
scan_dirs = ['/', '/home']

# Define the files and extensions to be searched
search_files = ['*.docx', '*.xlsx', '*.pptx', '*.pdf', '*.txt']

# Define the ransomware signature file
ransomware_sig = 'ransomware.sig'

# Function to scan a directory for ransomware files
def scan_directory(dir):
    # Loop through each file in the directory
    for file in os.listdir(dir):
        # Check if the file is a valid extension
        if file.endswith(search_files):
            # Check if the file has the ransomware signature
            with open(file, 'rb') as f:
                if re.search(ransomware_sig, f.read()):
                    print(f'Ransomware detected in {file}')
                    # Mitigate the ransomware attack by renaming the file
                    os.rename(file, file + '.bak')
                    # Remove the file from the directory
                    os.remove(file)
                    print('Mitigation successful')
        else:
            continue

# Function to scan all directories in a list
def scan_directories(dirs):
    for dir in dirs:
        scan_directory(dir)

scan_directories(scan_dirs)