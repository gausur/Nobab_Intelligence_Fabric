#!/usr/bin/env python3
# Nobab AI defense for ransomware
# Generated 2026-05-15 17:30:27.890659

import os
import sys
import hashlib
import subprocess
from datetime import datetime, timezone

# Define the list of known ransomware extensions
known_extensions = ['.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.pd[4D[K
'.pdf']

def detect_ransomware(filepath):
    # Get the file extension
    ext = os.path.splitext(filepath)[1]
    if ext in known_extensions:
        return True
    else:
        return False

def mitigate_ransomware(filepath):
    # Create a hash of the file to detect tampering
    hasher = hashlib.sha256()
    with open(filepath, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            hasher.update(chunk)
    hash_value = hasher.hexdigest()
    
    # Create a new file with the same contents
    new_filepath = os.path.join(os.getcwd(), 'decrypted')
    with open(new_filepath, 'wb') as f:
        with open(filepath, 'rb') as g:
            for chunk in iter(lambda: g.read(4096), b''):
                f.write(chunk)
    
    # Check if the hashes match
    new_hash = hashlib.sha256(open(new_filepath, 'rb').read()).hexdigest()
    if hash_value == new_hash:
        print('File is not tampered with')
    else:
        print('File is tampered with')
        os.remove(new_filepath)
        sys.exit(1)
    
    # Remove the original file
    os.remove(filepath)

def main():
    if len(sys.argv) != 2:
        print('Usage: python ransomware_detector.py <filename>')
        sys.exit(1)
    
    filepath = sys.argv[1]
    if detect_ransomware(filepath):
        mitigate_ransomware(filepath)
    else:
        print('File is not ransomware')
    
if __name__ == '__main__':
    main()