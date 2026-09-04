#!/usr/bin/env python3
# Nobab AI defense for ransomware
# Generated 2026-09-04 20:08:12.123984

import os
import subprocess

def detect_ransomware():
    # Check if the system is running Windows
    if os.name == 'nt':
        # Use the tasklist command to get a list of running processes
        tasklist_output = subprocess.check_output(['tasklist'])
        # Check if the ransomware process is running
        if 'ransomware.exe' in tasklist_output.decode('utf-8'):
            # Display an error message
            print('Ransomware detected!')
            # Try to shut down the ransomware process
            subprocess.check_call(['taskkill', '/im', 'ransomware.exe'])
            # Display a message indicating that the ransomware has been shu[3D[K
shut down
            print('Ransomware has been shut down.')
    else:
        # Display an error message indicating that the ransomware detection[9D[K
detection is only supported on Windows
        print('Ransomware detection is only supported on Windows.')

detect_ransomware()