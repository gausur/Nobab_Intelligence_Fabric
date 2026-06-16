#!/usr/bin/env python3
# Nobab AI defense for ransomware
# Generated 2026-06-16 18:00:13.262807

import os
import sys
import subprocess
from pathlib import Path

def detect_ransomware(path):
    # Check if the file has the correct permissions
    st = os.stat(path)
    mode = oct(st.st_mode & 0o777)[-3:]
    if mode != "644":
        print("Incorrect permission detected")
        return True
    
    # Check if the file is a regular file
    if not os.path.isfile(path):
        print("Not a regular file")
        return False
    
    # Check if the file has a suspicious extension
    basename, extension = os.path.splitext(path)
    if extension in [".exe", ".dll", ".sys"]:
        print("Suspicious extension detected")
        return True
    
    # Check if the file's owner is root
    uid = st.st_uid
    if uid != 0:
        print("File owned by non-root user")
        return False
    
    # Check if the file has been modified recently
    mtime = st.st_mtime
    if time.time() - mtime < 60*60*24:
        print("Recent modification detected")
        return True
    
    # Check if the file is in a suspicious location
    parent_dir = os.path.dirname(path)
    if parent_dir in ["/etc", "/bin", "/sbin"]:
        print("Suspicious location detected")
        return False
    
    # If none of the above checks failed, assume the file is safe
    return False

def mitigate_ransomware(path):
    # Remove the file
    try:
        os.remove(path)
    except OSError:
        print("Unable to remove file")
    
    # Check if the file was removed successfully
    if not os.path.exists(path):
        print("File removed successfully")
    else:
        print("Failed to remove file")

if __name__ == "__main__":
    path = sys.argv[1]
    if detect_ransomware(path):
        mitigate_ransomware(path)
    else:
        print("No ransomware detected")