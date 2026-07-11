#!/usr/bin/env python3
# Nobab AI defense for ransomware
# Generated 2026-07-11 07:12:28.072730

import os
import time
import json

def main():
    # Initialize variables
    file_types = ["txt", "docx", "xlsx", "pptx", "pdf"]
    file_extensions = []
    ransomware_files = []
    timestamp = int(time.time())

    # Get list of all files in the current directory
    for root, dirs, files in os.walk("."):
        for f in files:
            file_name, file_extension = os.path.splitext(f)
            if file_extension.lower() in file_types:
                file_extensions.append(file_extension[1:])

    # Check for ransomware files
    for extension in file_extensions:
        if not os.path.isfile(f"{extension}.ransomware"):
            continue
        with open(f"{extension}.ransomware", "r") as f:
            data = json.load(f)
            if data["timestamp"] < timestamp:
                ransomware_files.append(f"{extension}.ransomware")

    # Remove ransomware files
    for file in ransomware_files:
        os.remove(file)

if __name__ == "__main__":
    main()