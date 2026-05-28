#!/usr/bin/env python3
# Nobab AI defense for ransomware
# Generated 2026-05-28 22:29:45.177447

import os
import shutil
import subprocess
import sys

def detect_ransomware(file):
    # Check if the file is a directory
    if os.path.isdir(file):
        # If it's a directory, recursively check all files and directories [K
inside
        for root, dirs, files in os.walk(file):
            for f in files:
                detect_ransomware(os.path.join(root, f))
    else:
        # If it's a file, check if it has the ransomware signature
        with open(file, "rb") as f:
            data = f.read()
            if b"I am not a RANSOMWARE!" in data:
                print("Ransomware detected!")
                # Remove the file and its parent directory if it's empty
                os.remove(file)
                dirname = os.path.dirname(file)
                if not os.listdir(dirname):
                    shutil.rmtree(dirname)
            else:
                print("No ransomware detected.")

def main():
    # Parse command-line arguments
    args = sys.argv[1:]
    if len(args) != 2:
        print("Usage: python detect_ransomware.py <file>")
        exit()
    file = args[0]
    detect_ransomware(file)

if __name__ == "__main__":
    main()