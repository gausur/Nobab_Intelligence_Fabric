#!/usr/bin/env python3
# Nobab AI defense for ransomware
# Generated 2026-05-16 20:53:15.904014

import os
import hashlib
import json
from datetime import datetime

# Define the list of detected file extensions
file_extensions = ['.doc', '.xls', '.ppt', '.pdf']

# Define the directory to scan
scan_directory = '/path/to/directory'

# Create a dictionary to store the results
results = {}

# Iterate over each file in the directory
for root, dirs, files in os.walk(scan_directory):
    for file in files:
        # Get the full path of the file
        file_path = os.path.join(root, file)
        
        # Check if the file has a detected extension
        if any(file_path.endswith(ext) for ext in file_extensions):
            # Open the file and read its contents
            with open(file_path, 'r') as f:
                content = f.read()
                
            # Calculate the SHA256 hash of the file's contents
            hash = hashlib.sha256(content.encode('utf-8')).hexdigest()
            
            # Check if the hash is in the known ransomware list
            if hash in RANSOMWARE_HASHES:
                # Add the file to the results dictionary
                results[file_path] = {'hash': hash, 'size': os.path.getsize[15D[K
os.path.getsize(file_path)}
                
# Print the results
print(json.dumps(results, indent=4))