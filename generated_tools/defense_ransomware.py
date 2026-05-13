#!/usr/bin/env python3
# Nobab AI defense for ransomware
# Generated 2026-05-13 23:01:20.816873

import os
import socket
import sys

def check_for_ransomware(path):
    try:
        with open(path, 'rb') as f:
            contents = f.read()
    except FileNotFoundError:
        return False

    if b'RANSOMWARE' in contents:
        print('[!] Ransomware detected at {}'.format(path))
        return True

def mitigate_ransomware(path):
    try:
        os.remove(path)
    except FileNotFoundError:
        pass

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python ransomware_detector.py <directory>')
        sys.exit(1)

    directory = sys.argv[1]
    for root, dirs, files in os.walk(directory):
        for file in files:
            path = os.path.join(root, file)
            if check_for_ransomware(path):
                mitigate_ransomware(path)