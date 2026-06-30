#!/usr/bin/env python3
# Nobab AI defense for ransomware
# Generated 2026-06-30 06:52:41.449736

import os
import sys
import json
from pathlib import Path

def main():
    # Get the list of all files in the current directory
    files = []
    for file in os.listdir(os.getcwd()):
        if os.path.isfile(file):
            files.append(file)
    
    # Iterate over each file and check for ransomware patterns
    for file in files:
        with open(file, "r") as f:
            contents = f.read()
            if "demand" in contents or "extort" in contents:
                print("Ransomware detected!")
                # Mitigate the attack by deleting the affected file
                os.remove(file)
                break
    
if __name__ == "__main__":
    main()