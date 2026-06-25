#!/usr/bin/env python3
# Nobab AI defense for ransomware
# Generated 2026-06-25 00:04:14.516802

import os
import sys

def detect_ransomware(directory):
    # Check if the directory contains any encrypted files
    for file in os.listdir(directory):
        if "." not in file:
            continue
        extension = file.split(".")[-1]
        if extension == "enc":
            return True
    return False

def mitigate_ransomware(directory):
    # Delete all encrypted files
    for file in os.listdir(directory):
        if "." not in file:
            continue
        extension = file.split(".")[-1]
        if extension == "enc":
            os.remove(os.path.join(directory, file))

def main():
    # Check if the script is being run with sudo privileges
    if not os.getuid() == 0:
        print("This script must be run with sudo privileges.")
        sys.exit(1)

    # Get the directory to scan for ransomware
    directory = input("Enter the directory to scan for ransomware: ")

    # Check if the directory exists and is readable
    if not os.path.isdir(directory):
        print("The specified directory does not exist.")
        sys.exit(1)
    elif not os.access(directory, os.R_OK):
        print("You do not have read access to the specified directory.")
        sys.exit(1)

    # Detect and mitigate ransomware in the directory
    if detect_ransomware(directory):
        print("Ransomware detected in the directory.")
        mitigate_ransomware(directory)
        print("Mitigation successful.")
    else:
        print("No ransomware detected in the directory.")

if __name__ == "__main__":
    main()