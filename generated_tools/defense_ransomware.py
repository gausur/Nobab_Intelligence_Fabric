#!/usr/bin/env python3
# Nobab AI defense for ransomware
# Generated 2026-10-29 23:54:00.684430

import os
import sys

def detect_ransomware(file_path):
    with open(file_path, 'rb') as f:
        data = f.read()
        if b'ransom' in data:
            return True
    return False

def mitigate_ransomware(file_path):
    if detect_ransomware(file_path):
        print("Ransomware detected!")
        os.remove(file_path)
        sys.exit(1)
    else:
        print("No ransomware detected.")

def main():
    file_path = sys.argv[1]
    mitigate_ransomware(file_path)

if __name__ == '__main__':
    main()