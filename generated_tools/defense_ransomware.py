#!/usr/bin/env python3
# Nobab AI defense for ransomware
# Generated 2026-06-10 11:36:33.651694

import os
import sys
import subprocess
import hashlib

def get_file_hash(filename):
    with open(filename, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()

def check_for_ransomware():
    # Check for common ransomware extensions
    if os.path.isfile('C:\Program Files\WinRAR.exe'):
        print('Ransomware detected!')
    elif os.path.isfile('C:\Program Files (x86)\WinRAR.exe'):
        print('Ransomware detected!')
    elif os.path.isfile('C:\Program Files\7-Zip\7z.exe'):
        print('Ransomware detected!')
    else:
        return False
    
    # Check for common ransomware files and folders
    file_list = [
        'C:\Users\User\Documents\ransom.txt',
        'C:\Users\User\Downloads\ransom.exe',
        'C:\Users\User\Desktop\ransom.jpg'
    ]
    
    for file in file_list:
        if os.path.isfile(file):
            print('Ransomware detected!')
            return True
            
    # Check for common ransomware registry keys
    reg_key = 'HKEY_CURRENT_USER\Software\WinRAR'
    try:
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_key) as key:
            value, _ = winreg.QueryValueEx(key, '')
            if 'Ransomware' in value:
                print('Ransomware detected!')
                return True
    except FileNotFoundError:
        pass
    
    return False

def mitigate_ransomware():
    # Restore files and folders
    file_list = [
        'C:\Users\User\Documents\ransom.txt',
        'C:\Users\User\Downloads\ransom.exe',
        'C:\Users\User\Desktop\ransom.jpg'
    ]
    
    for file in file_list:
        try:
            subprocess.check_call(['robocopy', file, get_file_hash(file)])
        except FileNotFoundError:
            pass
            
    # Remove registry keys
    reg_key = 'HKEY_CURRENT_USER\Software\WinRAR'
    try:
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_key) as key:
            winreg.DeleteKey(key)
    except FileNotFoundError:
        pass
            
if __name__ == '__main__':
    if check_for_ransomware():
        mitigate_ransomware()