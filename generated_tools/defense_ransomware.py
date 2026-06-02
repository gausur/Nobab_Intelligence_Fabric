#!/usr/bin/env python3
# Nobab AI defense for ransomware
# Generated 2026-06-02 18:37:35.658045

import os
import sys
import subprocess
import json

def check_for_ransomware(path):
    # Check if the file is a symbolic link
    if os.path.islink(path):
        return True

    # Check if the file has the correct permissions
    stat = os.stat(path)
    if not (stat.st_mode & 0o755):
        return True

    # Check if the file is owned by root or a trusted user
    if stat.st_uid != 0 and stat.st_gid != 0:
        return True

    return False

def scan_directory(path, results):
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            if check_for_ransomware(file_path):
                results.append({"file": file_path})

def scan_system():
    results = []
    scan_directory("/", results)
    return results

if __name__ == "__main__":
    print(json.dumps(scan_system()))