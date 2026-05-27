#!/usr/bin/env python3
# Nobab AI defense for ransomware
# Generated 2026-05-27 17:58:04.076682

import os
import json
from collections import defaultdict

# Define the list of malicious files and their hashes
malicious_files = ["ransom.exe", "encryptor.dll", "decryptor.exe"]
hashes = {
    "ransom.exe": "1234567890abcdef",
    "encryptor.dll": "abcdef1234567890",
    "decryptor.exe": "fedcba987654321"
}

# Define the list of safe files and their hashes
safe_files = ["file1.txt", "file2.docx"]
hashes = {
    "file1.txt": "0000000000000000",
    "file2.docx": "1111111111111111"
}

# Define the list of directories to scan
directories = ["C:\\Users\\John Doe\\Downloads", "C:\\Program Files"]

# Define the list of extensions to consider for files to scan
extensions = [".exe", ".dll", ".txt", ".docx"]

# Define the function to hash a file and return its hash
def hash_file(filename):
    with open(filename, "rb") as f:
        data = f.read()
    return hashlib.md5(data).hexdigest()

# Define the function to scan a directory for malware
def scan_directory(directory):
    for file in os.listdir(directory):
        filename = os.path.join(directory, file)
        if not os.path.isfile(filename):
            continue
        extension = os.path.splitext(filename)[1]
        if extension not in extensions:
            continue
        hash = hash_file(filename)
        if hash in hashes:
            return True, filename
    return False, None

# Define the function to scan for malware in all directories
def scan_directories():
    for directory in directories:
        result, filename = scan_directory(directory)
        if result:
            print("Malware detected in file:", filename)

# Define the main function
def main():
    # Scan for malware in all directories
    scan_directories()

if __name__ == "__main__":
    main()