#!/usr/bin/env python3
# Nobab AI defense for ransomware
# Generated 2026-07-19 21:46:41.496486

import os
import sys

# Define the list of suspicious files and folders
suspicious_files = ["/etc/passwd", "/etc/shadow"]
suspicious_folders = ["/etc/ssh", "/home/user/.ssh"]

# Iterate over the list of suspicious files and folders
for file in suspicious_files:
    if os.path.exists(file):
        # Check if the file has been modified since last boot
        if not os.stat(file).st_mtime:
            print("Possible ransomware attack detected!")
            sys.exit(1)

# Iterate over the list of suspicious folders
for folder in suspicious_folders:
    # Check if the folder exists and is not empty
    if os.path.exists(folder) and os.listdir(folder):
        print("Possible ransomware attack detected!")
        sys.exit(1)