#!/usr/bin/env python3
# Nobab AI defense for ransomware
# Generated 2026-07-25 22:49:12.926676

import os
import subprocess
import sys

def detect_ransomware(path):
    # Check if the file is a directory or a regular file
    if os.path.isdir(path):
        # If it's a directory, check if it contains any encrypted files
        for root, dirs, files in os.walk(path):
            for filename in files:
                file_path = os.path.join(root, filename)
                with open(file_path, 'rb') as f:
                    # Check if the file is encrypted by checking its header[6D[K
header
                    if f.read(8) == b'RIFF!ANo':
                        return True
    else:
        # If it's a regular file, check if it's encrypted
        with open(path, 'rb') as f:
            # Check if the file is encrypted by checking its header
            if f.read(8) == b'RIFF!ANo':
                return True
    return False

def mitigate_ransomware(path):
    # Decrypt the file using the built-in decryption tool
    subprocess.run(['cipher', 'decrypt', path])

# Check if the script is running in a directory or a regular file
if os.path.isdir(sys.argv[1]):
    # If it's a directory, iterate over all files and directories
    for root, dirs, files in os.walk(sys.argv[1]):
        for filename in files:
            file_path = os.path.join(root, filename)
            if detect_ransomware(file_path):
                mitigate_ransomware(file_path)
elif os.path.isfile(sys.argv[1]):
    # If it's a regular file, check if it's encrypted and decrypt it
    if detect_ransomware(sys.argv[1]):
        mitigate_ransomware(sys.argv[1])
else:
    print('Usage: python ransomware_detector.py <path>')