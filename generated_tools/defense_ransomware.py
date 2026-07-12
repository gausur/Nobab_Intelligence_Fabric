#!/usr/bin/env python3
# Nobab AI defense for ransomware
# Generated 2026-07-12 22:44:54.445467

import os
import shutil
import subprocess
import time
from pathlib import Path

# Define the directories to scan
directories = ["/path/to/scan", "/another/path"]

# Define the files to exclude from the scan
exclude_files = ["*.txt", "*.docx"]

# Define the ransomware patterns to detect
ransomware_patterns = [
    "encrypt",
    "pay",
    "demand",
    "reboot",
    "shutdown",
    "system",
    "control",
]

# Set up a timer for the scan
start_time = time.time()

# Iterate over the directories to scan
for directory in directories:
    # Create a Path object for the directory
    path = Path(directory)
    
    # Get a list of all files and subdirectories in the directory
    files = path.glob("**/*")
    
    # Iterate over the files and subdirectories
    for file in files:
        # Check if the file is a directory
        if file.is_dir():
            continue
        
        # Get the filename of the file
        filename = file.name
        
        # Check if the filename matches any of the excluded files
        if any(exclude in filename for exclude in exclude_files):
            continue
        
        # Open the file and read its contents
        with open(file, "r") as f:
            data = f.read()
            
        # Check if the file contains any of the ransomware patterns
        for pattern in ransomware_patterns:
            if pattern in data:
                print(f"Ransomware detected in {file}")
                
                # Mitigate the attack by rebooting the system
                subprocess.run(["reboot"])

# Calculate the duration of the scan
end_time = time.time() - start_time
print(f"Scan took {end_time:.2f} seconds")