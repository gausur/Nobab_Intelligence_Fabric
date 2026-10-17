#!/usr/bin/env python3
# Nobab AI defense for ransomware
# Generated 2026-10-17 23:45:16.538362

import os
import re
import subprocess

# Define the list of files and directories to be monitored
files = ["/etc/passwd", "/etc/shadow", "/etc/group"]
directories = ["/etc/", "/var/", "/usr/"]

# Define the regex pattern for detecting ransomware
pattern = r"^[A-Z]{4}[0-9]{4}[a-z]{4}$"

# Function to check if the file contains the ransomware pattern
def check_file(file_path):
    with open(file_path, "r") as file:
        contents = file.read()
        if re.search(pattern, contents):
            return True
    return False

# Function to scan the files and directories
def scan(files, directories):
    for file in files:
        if check_file(file):
            print(f"Ransomware detected in file: {file}")
    for directory in directories:
        for root, dirs, files in os.walk(directory):
            for file in files:
                if check_file(os.path.join(root, file)):
                    print(f"Ransomware detected in file: {file}")

# Function to mitigate the ransomware attack
def mitigate():
    # Restart the system to prevent further damage
    subprocess.call(["sudo", "reboot"])
    print("System rebooted")

# Main function to run the script
def main():
    scan(files, directories)
    mitigate()

if __name__ == "__main__":
    main()