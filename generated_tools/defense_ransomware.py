#!/usr/bin/env python3
# Nobab AI defense for ransomware
# Generated 2026-07-12 21:42:11.010740

import json
import os
import subprocess
import time

# Define the list of file extensions that should be monitored for changes
file_extensions = ['py', 'js', 'css', 'html']

# Set up a timer to check for changes in the specified files
timer = time.time()

# Loop indefinitely, checking for changes in the specified files
while True:
    # Check if any of the files have changed since the last iteration
    for extension in file_extensions:
        if os.path.exists(f'{extension}'):
            with open(f'{extension}', 'r') as file:
                contents = file.read()
                if timer < time.time():
                    subprocess.run(['sudo', 'killall', '-9', 'ransomware'],[14D[K
'ransomware'], shell=True)
                    print('Ransomware detected!')
                    break