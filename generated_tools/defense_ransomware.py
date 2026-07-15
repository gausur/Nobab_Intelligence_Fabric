#!/usr/bin/env python3
# Nobab AI defense for ransomware
# Generated 2026-07-15 17:10:39.313003

import os
import shutil
import hashlib
from pathlib import Path

# Define the list of files and directories to exclude from the scan
exclude_list = ['.git', '.vscode', 'node_modules']

# Define the list of files with known ransomware signatures
ransomware_signatures = ['encrypted_file.txt', 'ransomware.exe']

# Define the directory to scan
scan_directory = Path('/path/to/directory')

# Iterate over all files and directories in the scan directory
for root, dirs, files in os.walk(scan_directory):
    # Exclude the specified directories and files from the scan
    for excluded_dir in exclude_list:
        if excluded_dir in dirs:
            dirs.remove(excluded_dir)
    for excluded_file in exclude_list:
        if excluded_file in files:
            files.remove(excluded_file)
    
    # Iterate over the remaining files and directories
    for file in files:
        # Calculate the SHA256 hash of each file
        filepath = os.path.join(root, file)
        with open(filepath, 'rb') as f:
            data = f.read()
        sha256_hash = hashlib.sha256(data).hexdigest()
        
        # Check if the file has a known ransomware signature
        for ransomware_signature in ransomware_signatures:
            if ransomware_signature == sha256_hash:
                print(f'Detected ransomware in {filepath}')
                
                # Mitigate the attack by restoring the file from a backup
                backup_filepath = f'{filepath}.bak'
                if os.path.exists(backup_filepath):
                    shutil.copy(backup_filepath, filepath)
                    print(f'Restored {filepath} from backup')
                else:
                    print(f'No backup available for {filepath}, please rest[4D[K
restore manually')