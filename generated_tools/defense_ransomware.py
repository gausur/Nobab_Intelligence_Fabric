#!/usr/bin/env python3
# Nobab AI defense for ransomware
# Generated 2026-07-01 04:17:01.072271

import os
import re
import time

def detect_ransomware(directory):
    # Find all files in the directory and its subdirectories
    files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            files.append(os.path.join(root, file))
    
    # Check if any of the files are encrypted with a known ransomware exten[5D[K
extension
    for file in files:
        if re.search(r"\.enc", file):
            return True
    
    # If no files are encrypted, check if there are any suspicious file mod[3D[K
modifications within the past hour
    for file in files:
        modified = os.path.getmtime(file)
        if time.time() - modified > 3600:
            return True
    
    # If no ransomware is detected, return False
    return False