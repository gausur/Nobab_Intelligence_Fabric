#!/usr/bin/env python3
# Nobab AI defense for ransomware
# Generated 2026-07-11 21:43:23.950407

import os
import json
import time

def check_for_ransomware(directory):
    files = os.listdir(directory)
    for file in files:
        if not file.endswith('.exe'):
            continue
        with open(os.path.join(directory, file), 'rb') as f:
            data = f.read()
            if b'Ransomware' in data:
                print('Possible ransomware detected!')
                mitigate_ransomware(directory)
                break

def mitigate_ransomware(directory):
    files = os.listdir(directory)
    for file in files:
        if not file.endswith('.exe'):
            continue
        with open(os.path.join(directory, file), 'rb') as f:
            data = f.read()
            # Remove the ransomware code
            data = data.replace(b'Ransomware', b'')
            # Write the modified data back to the file
            with open(os.path.join(directory, file), 'wb') as f:
                f.write(data)

# Start the script in a loop, checking for ransomware every 5 minutes
while True:
    check_for_ransomware('/home/user/Downloads')
    time.sleep(300)