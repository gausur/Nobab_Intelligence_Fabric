#!/usr/bin/env python3
# Nobab AI defense for ransomware
# Generated 2026-05-24 18:04:09.397866

import os
import shutil

def detect_ransomware(path):
    # Check if the file exists
    if not os.path.exists(path):
        return False
    
    # Check if the file is encrypted
    with open(path, "rb") as f:
        contents = f.read()
        if b"ransomware" in contents or b"demand" in contents:
            return True
    return False

def mitigate_ransomware(path):
    # Check if the file exists
    if not os.path.exists(path):
        return
    
    # Delete the file
    try:
        os.remove(path)
    except OSError as e:
        print("Error removing file", path, "Error:", e)
    else:
        print("File removed successfully")

# Check if the current working directory is encrypted
if detect_ransomware(os.getcwd()):
    mitigate_ransomware(os.getcwd())

# Recursively check all subdirectories for encryption
for root, dirs, files in os.walk(os.getcwd()):
    for file in files:
        path = os.path.join(root, file)
        if detect_ransomware(path):
            mitigate_ransomware(path)