#!/usr/bin/env python3
# Nobab AI defense for ransomware
# Generated 2026-06-03 18:21:34.555655

import os
import re

def detect_ransomware(file_path):
    # Check if the file is readable
    if not os.access(file_path, os.R_OK):
        print("Error: File is not readable")
        return

    # Read the first 1024 bytes of the file
    with open(file_path, "rb") as f:
        data = f.read(1024)

    # Look for known ransomware patterns in the first 1024 bytes
    if re.search(r"^[A-Za-z0-9]{5,}!", data):
        print("Ransomware detected")
        return

# Iterate through all files and directories in the current directory
for root, dirs, files in os.walk("."):
    for file in files:
        # Skip hidden files and directories
        if not file.startswith("."):
            detect_ransomware(os.path.join(root, file))