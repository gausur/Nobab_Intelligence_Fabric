#!/usr/bin/env python3
# Nobab AI defense for ransomware
# Generated 2026-05-22 02:38:26.861136

import os
import time
import shutil

# Define the directory to monitor for changes
directory = '/path/to/monitor'

# Define the list of files to ignore
ignore_list = ['file1', 'file2']

# Define the threshold for detecting changes (in seconds)
threshold = 300 # 5 minutes

while True:
    # Get the current time
    now = time.time()
    
    # Walk through the directory and its subdirectories
    for root, dirs, files in os.walk(directory):
        # Iterate over the list of files
        for file in files:
            # Skip any ignored files
            if file in ignore_list:
                continue
            
            # Get the full path to the file
            file_path = os.path.join(root, file)
            
            # Check if the file has been modified since the last check
            try:
                stat = os.stat(file_path)
                if now - stat.st_mtime > threshold:
                    print('Detected changes in ' + file_path)
                    shutil.copy(file_path, '/path/to/backup') # Backup the [K
file to a safe location
            except OSError:
                pass # File not found, ignore it