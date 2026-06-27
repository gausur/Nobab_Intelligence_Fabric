#!/usr/bin/env python3
# Nobab AI defense for ransomware
# Generated 2026-06-27 20:06:28.455752

import os
import sys
import json
import hashlib
from datetime import datetime

def is_ransomware(filepath):
    # Check if the file is a text file
    if not os.path.isfile(filepath) or not os.path.istext(filepath):
        return False
    
    # Get the file's hash
    with open(filepath, 'rb') as f:
        data = f.read()
    md5sum = hashlib.md5(data).hexdigest()
    
    # Check if the file is a known ransomware file
    ransomware_files = [
        {'hash': '8f9637b78d0aaf26e22b14f7d0cfc965', 'path': 'ransomware/en[14D[K
'ransomware/encrypt.txt'},
        {'hash': 'c54dce7c8b7413c5e6dbb0a41ed0b81c', 'path': 'ransomware/de[14D[K
'ransomware/decrypt.txt'}
    ]
    for ransomware_file in ransomware_files:
        if md5sum == ransomware_file['hash']:
            return True
    
    # Check if the file contains known ransomware strings
    ransomware_strings = [
        'ransomware',
        'encrypt',
        'decrypt'
    ]
    with open(filepath, 'r') as f:
        contents = f.read()
    for string in ransomware_strings:
        if string in contents:
            return True
    
    return False

def mitigate_ransomware(filepath):
    # Delete the file
    os.remove(filepath)
    
    # Log the event
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    log_entry = {
        'timestamp': timestamp,
        'filename': filepath
    }
    with open('ransomware_mitigation.log', 'a') as f:
        json.dump(log_entry, f)

def main():
    # Iterate over all files in the current directory
    for filename in os.listdir('.'):
        filepath = os.path.join('.', filename)
        
        # Check if the file is a ransomware file
        if is_ransomware(filepath):
            mitigate_ransomware(filepath)
    
    sys.exit()