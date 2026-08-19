#!/usr/bin/env python3
# Nobab AI defense for ransomware
# Generated 2026-08-19 15:27:47.907657

import os
import json

def detect_ransomware(filename):
    # Check if the file is a directory
    if os.path.isdir(filename):
        return "Not a ransomware attack"
    
    # Read the file contents
    with open(filename, "r") as file:
        contents = file.read()
    
    # Check if the file contains the ransomware string
    if "ransomware" in contents:
        return "Ransomware attack detected"
    else:
        return "Not a ransomware attack"

def mitigate_ransomware(filename):
    # Delete the file
    os.remove(filename)
    return "Ransomware attack mitigated"

if __name__ == "__main__":
    # Get the filename from the command line arguments
    filename = sys.argv[1]
    
    # Detect and mitigate the ransomware attack
    if detect_ransomware(filename) == "Ransomware attack detected":
        mitigate_ransomware(filename)
    else:
        print("Not a ransomware attack")