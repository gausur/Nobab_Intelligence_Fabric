#!/usr/bin/env python3
# Nobab AI defense for ransomware
# Generated 2026-07-12 14:29:23.892685

import os
import sys
import json
import time

# Define the list of extensions to check for in files
extensions = ['.txt', '.docx', '.xlsx', '.pptx', '.pdf']

# Define the list of ransomware keywords to look for in file names and cont[4D[K
contents
keywords = ['ransom', 'crypt', 'encrypt', 'lock', 'virus', 'malware']

# Define the directory to scan
directory = '/path/to/scan'

# Define the output file name
output_file = 'ransomware_detection.txt'

# Create a list of files to scan
files_to_scan = []
for root, dirs, files in os.walk(directory):
    for file in files:
        if any(file.endswith(extension) for extension in extensions):
            files_to_scan.append(os.path.join(root, file))

# Create a list of ransomware files
ransomware_files = []
for file in files_to_scan:
    with open(file, 'r') as f:
        contents = f.read()
        if any(keyword in contents for keyword in keywords):
            ransomware_files.append(file)

# Write the list of ransomware files to a file
with open(output_file, 'w') as f:
    json.dump(ransomware_files, f)