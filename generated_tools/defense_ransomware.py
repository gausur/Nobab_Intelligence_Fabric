#!/usr/bin/env python3
# Nobab AI defense for ransomware
# Generated 2026-06-17 17:49:49.519915

import os
import re

def detect_ransomware(path):
    # Check if the file is a directory
    if not os.path.isdir(path):
        return False
    
    # Check if the file has a .exe extension
    if not path.endswith('.exe'):
        return False
    
    # Check if the file name contains "Ransom" or "Encrypt"
    if re.search(r'(?i)ransom|encrypt', path):
        return True
    
    # Check if any of the files in the directory has a .exe extension
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.exe'):
                return True
    
    return False

def mitigate_ransomware(path):
    # Check if the file is a directory
    if not os.path.isdir(path):
        return
    
    # Check if the file has a .exe extension
    if not path.endswith('.exe'):
        return
    
    # Remove the file or directory
    os.remove(path)

# Example usage
if detect_ransomware('C:/Users/User/Downloads/Ransomware.exe'):
    mitigate_ransomware('C:/Users/User/Downloads/Ransomware.exe')
else:
    print("No ransomware detected")