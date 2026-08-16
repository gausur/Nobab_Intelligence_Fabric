#!/usr/bin/env python3
# Nobab AI defense for ransomware
# Generated 2026-08-16 17:15:06.735559

import os
import re
import subprocess

# Define the list of ransomware extensions
ransomware_extensions = [".ransomware", ".cryptolocker", ".locker", ".decry[7D[K
".decryptor"]

# Define the list of suspicious files
suspicious_files = []

# Iterate over the files in the current directory
for file in os.listdir():
    # Check if the file has a ransomware extension
    if any(file.endswith(ext) for ext in ransomware_extensions):
        # Add the file to the suspicious files list
        suspicious_files.append(file)

# Check if any suspicious files were found
if len(suspicious_files) > 0:
    # Print a warning message
    print("WARNING: Possible ransomware attack detected!")
    print("Suspicious files:", ", ".join(suspicious_files))

    # Ask the user if they want to continue with the attack
    decision = input("Continue with the attack? [Y/n]: ")
    if decision.lower() != "y":
        # If the user doesn't want to continue, exit the script
        print("Aborting attack...")
        exit(1)

# Otherwise, continue with the attack
print("Continuing with attack...")

# Launch the ransomware attack
subprocess.run(["ransomware", "attack"])