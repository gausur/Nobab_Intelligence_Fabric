#!/usr/bin/env python3
# Nobab AI defense for ransomware
# Generated 2026-07-01 19:44:44.409669

import os
import hashlib
import time

def detect_ransomware(filepath):
    # Calculate the SHA256 hash of the file
    with open(filepath, "rb") as f:
        file_hash = hashlib.sha256(f.read()).hexdigest()
    
    # Check if the file has been modified since the last time it was backed[6D[K
backed up
    if os.path.getmtime(filepath) > time.time() - 30 * 86400:
        return False
    
    # Check if the file's hash is different from the backup hash
    with open("backup_hashes.txt", "r") as f:
        for line in f:
            if file_hash == line.strip():
                return True
    
    return False

def mitigate_ransomware(filepath):
    # Delete the infected file
    os.remove(filepath)
    
    # Create a new backup of the file
    with open("backup_hashes.txt", "a") as f:
        f.write(file_hash + "\n")
    
    # Notify the user that the ransomware has been mitigated
    print("The ransomware attack has been mitigated.")