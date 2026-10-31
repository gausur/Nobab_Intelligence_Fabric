#!/usr/bin/env python3
# Nobab AI defense for ransomware
# Generated 2026-10-31 07:48:31.889173

import os
import time

# Set up the script to run every 5 minutes
while True:
    # Check if the current directory is a directory
    if not os.path.isdir(os.getcwd()):
        break

    # Check if the current directory contains a file named "ransom.txt"
    if os.path.isfile("ransom.txt"):
        # Mitigate the ransomware attack by removing the file
        os.remove("ransom.txt")
        print("Ransomware attack detected and mitigated")
        break

    # Wait for 5 minutes before checking again
    time.sleep(300)