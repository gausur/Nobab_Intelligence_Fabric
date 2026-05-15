#!/usr/bin/env python3
# Nobab AI defense for ransomware
# Generated 2026-05-15 21:00:26.464171

import os
import re
import json
import sys
from urllib import request
from pathlib import Path

# Define the list of extensions to consider as malicious files
malicious_extensions = ['.exe', '.dll', '.scr']

# Define the list of directories to scan recursively
scan_directories = ['/path/to/directory1', '/path/to/directory2']

# Define the list of files to ignore during the scan
ignore_files = ['some_file.txt', 'another_file.doc']

def is_malicious(filename):
  extension = Path(filename).suffix
  if extension in malicious_extensions:
    return True
  else:
    return False

def get_file_size(filename):
  stat = os.stat(filename)
  return stat.st_size

def get_last_modified(filename):
  stat = os.stat(filename)
  return stat.st_mtime

def scan_directory(directory, ignore_files=[]):
  for root, dirs, files in os.walk(directory):
    for file in files:
      if file not in ignore_files:
        filename = os.path.join(root, file)
        if is_malicious(filename):
          print("Malicious file detected: " + filename)
          size = get_file_size(filename)
          modified = get_last_modified(filename)
          print("File size: " + str(size))
          print("Last modified: " + str(modified))

def scan_directories():
  for directory in scan_directories:
    scan_directory(directory, ignore_files)

scan_directories()