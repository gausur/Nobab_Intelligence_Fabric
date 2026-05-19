#!/usr/bin/env python3
# Nobab AI defense for ransomware
# Generated 2026-05-19 22:11:23.468193

import os
import sys
import subprocess
import hashlib

# Define the directory to scan
directory = "/path/to/scan"

# Define the list of files and directories to ignore
ignore_list = ["ignored_file1", "ignored_dir1", "ignored_file2"]

# Define the list of extensions to check for ransomware
extensions = [".exe", ".dll", ".sys", ".scr"]

# Define the hashes to look for in order to determine if a file is ransomwa[8D[K
ransomware or not
ransomware_hashes = {
    "ransomware1": "9324809c265b70a3dbba91f8b3675e96",
    "ransomware2": "4ac9979f81be366396de65ba2d864f6e"
}

# Define the hash function to use for hashing files
hash_function = hashlib.md5()

# Scan the directory and its subdirectories
for root, dirs, files in os.walk(directory):
    # Ignore any directories or files in the ignore list
    ignored = [d for d in dirs if d in ignore_list]
    dirs[:] = [d for d in dirs if d not in ignored]
    ignored = [f for f in files if f in ignore_list]
    files[:] = [f for f in files if f not in ignored]

    # Check each file against the ransomware hashes
    for file in files:
        file_path = os.path.join(root, file)
        try:
            with open(file_path, "rb") as f:
                content = f.read()
            hash_function.update(content)
            file_hash = hash_function.hexdigest()
            if file_hash in ransomware_hashes:
                print("Ransomware detected! File:", file_path)
        except Exception as e:
            print("Error opening file:", file_path, "Exception:", str(e))

# Mitigate the ransomware attack by deleting all files with the affected ha[2D[K
hashes
for file in files:
    file_path = os.path.join(root, file)
    try:
        if hash_function.hexdigest() in ransomware_hashes:
            print("Deleting ransomware file:", file_path)
            subprocess.check_call(["rm", "-f", file_path])
    except Exception as e:
        print("Error deleting file:", file_path, "Exception:", str(e))