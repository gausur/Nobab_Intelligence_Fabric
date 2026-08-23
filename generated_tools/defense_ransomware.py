#!/usr/bin/env python3
# Nobab AI defense for ransomware
# Generated 2026-08-23 20:14:44.537284

import os
import stat
import shutil

def detect_ransomware(path):
    # Check if the file is encrypted
    if os.path.isfile(path) and stat.S_ISREG(os.stat(path).st_mode):
        with open(path, "rb") as f:
            data = f.read()
            if b"ransom" in data:
                print("Ransomware detected in file:", path)
                return True
    return False

def mitigate_ransomware(path):
    # Remove the file
    if os.path.isfile(path):
        os.remove(path)
        print("File removed:", path)
    # Remove the directory
    elif os.path.isdir(path):
        shutil.rmtree(path)
        print("Directory removed:", path)
    else:
        print("Path does not exist:", path)

def main():
    # Check if the path exists
    if not os.path.exists(sys.argv[1]):
        print("Path does not exist:", sys.argv[1])
        return

    # Detect and mitigate ransomware
    for root, dirs, files in os.walk(sys.argv[1]):
        for file in files:
            full_path = os.path.join(root, file)
            if detect_ransomware(full_path):
                mitigate_ransomware(full_path)

if __name__ == "__main__":
    main()