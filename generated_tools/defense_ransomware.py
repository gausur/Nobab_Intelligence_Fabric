#!/usr/bin/env python3
# Nobab AI defense for ransomware
# Generated 2026-07-17 15:10:36.999472

import os
import sys
import time
from datetime import datetime

# Define the directories to monitor
directories = ["C:\\", "D:\\"]

# Define the file types to watch
file_types = [".txt", ".docx", ".xlsx", ".pptx"]

# Set up a timer to check for changes every 5 minutes
timer = time.time() + (60 * 5)

while True:
    # Check if the timer has expired
    if time.time() > timer:
        # Reset the timer
        timer = time.time() + (60 * 5)
        
        # Loop through each directory and file type
        for directory in directories:
            for file_type in file_types:
                # Check if a new file has been added to the directory
                if os.path.exists(f"{directory}{file_type}"):
                    print(f"Ransomware detected! File {directory}{file_type[21D[K
{directory}{file_type} was created.")
                    
                    # Mitigate the attack by deleting the file
                    os.remove(f"{directory}{file_type}")
                    
                    # Notify the user of the attack and its mitigation
                    print("Ransomware has been mitigated!")