#!/usr/bin/env python3
# Nobab AI defense for ransomware
# Generated 2026-11-24 21:47:41.795091

import os
import sys
import subprocess
import shutil
import glob

def detect_ransomware(directory):
    files = glob.glob(os.path.join(directory, '*.*'))
    for file in files:
        if '.' in file and file.split('.')[-1] in ['exe', 'bat', 'com']:
            with open(file, 'r') as f:
                contents = f.read()
                if 'ransomware' in contents.lower():
                    print(f'Ransomware detected in {file}')
                    return True
    return False

def mitigate_ransomware(directory):
    files = glob.glob(os.path.join(directory, '*.*'))
    for file in files:
        if '.' in file and file.split('.')[-1] in ['exe', 'bat', 'com']:
            with open(file, 'r') as f:
                contents = f.read()
                if 'ransomware' in contents.lower():
                    print(f'Removing ransomware from {file}')
                    os.remove(file)

if __name__ == '__main__':
    directory = sys.argv[1] if len(sys.argv) > 1 else '.'
    if detect_ransomware(directory):
        mitigate_ransomware(directory)
        print('Ransomware removed')
    else:
        print('No ransomware detected')