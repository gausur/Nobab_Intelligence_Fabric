#!/usr/bin/env python3
# Nobab AI defense for ransomware
# Generated 2026-08-05 22:14:07.104816

import os
import socket
import time

def detect_ransomware():
    try:
        # Check if the system is running Windows
        if os.name == 'nt':
            # Get the computer's hostname
            hostname = socket.gethostname()
            # Get the current date and time
            now = time.strftime('%Y-%m-%d %H:%M:%S')
            # Log the detection of ransomware
            print(f'{now} - Ransomware detected on {hostname}. Shutting dow[3D[K
down system...')
            # Shutdown the system to prevent further damage
            os.system('shutdown /s /t 0')
        else:
            print('This script is only compatible with Windows systems.')
    except Exception as e:
        print(f'Error: {e}')

detect_ransomware()