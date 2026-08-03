#!/usr/bin/env python3
# Nobab AI defense for ransomware
# Generated 2026-08-03 21:00:10.849135

import os
import hashlib

def detect_ransomware(file):
    # Calculate the SHA256 hash of the file
    with open(file, "rb") as f:
        data = f.read()
    hash = hashlib.sha256(data).hexdigest()

    # Check if the hash is in the known bad hash list
    with open("bad_hashes.txt", "r") as f:
        bad_hashes = set(f.read().splitlines())
    if hash in bad_hashes:
        return True
    else:
        return False

def mitigate_ransomware(file):
    # Extract the file name from the path
    filename = os.path.basename(file)
    
    # Move the file to a safe location
    with open(f"safe_{filename}", "wb") as f:
        f.write(data)

# Main loop
while True:
    # Wait for a new file to be created in the monitored directory
    new_file = os.path.join(os.getcwd(), "new_files", "filename")
    if not os.path.isfile(new_file):
        continue
    
    # Detect and mitigate ransomware attacks
    if detect_ransomware(new_file):
        mitigate_ransomware(new_file)

# Clean up the monitored directory
os.remove(new_file)