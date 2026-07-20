#!/usr/bin/env python3
# Nobab AI defense for ransomware
# Generated 2026-07-20 09:55:22.416008

import json
import os
import re
import subprocess
import sys

def main():
    # Load the configuration file
    with open("config.json", "r") as f:
        config = json.load(f)
    
    # Set up the directory to monitor
    dir_to_monitor = config["dir_to_monitor"]
    
    # Set up the ransomware signatures
    ransomware_signatures = config["ransomware_signatures"]
    
    # Create a watchdog for the directory
    wd = subprocess.Popen(["watchdog", "--directory", dir_to_monitor], stdo[4D[K
stdout=subprocess.PIPE)
    
    # Loop indefinitely, monitoring the directory and looking for ransomwar[9D[K
ransomware activity
    while True:
        line = wd.stdout.readline()
        
        if not line:
            break
        
        # If a file was modified, check it against the ransomware signature[9D[K
signatures
        match = re.match(r"^(?P<file_path>.+)\s+\[modified\]\s*$", line)
        if match:
            file_path = match.group("file_path")
            
            # Open the file and read its contents
            with open(file_path, "r") as f:
                contents = f.read()
            
            # Check each ransomware signature against the file's contents
            for sig in ransomware_signatures:
                if re.search(sig, contents):
                    print(f"Ransomware detected! File path: {file_path}")
                    
                    # Mitigate the ransomware attack by deleting the file
                    os.remove(file_path)
                    
                    break

if __name__ == "__main__":
    main()