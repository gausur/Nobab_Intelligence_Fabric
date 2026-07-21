#!/usr/bin/env python3
# Nobab AI defense for ransomware
# Generated 2026-07-21 22:00:49.359329

import os
import shutil
import subprocess

def detect_ransomware():
    # Check if the system is running a vulnerable version of Windows
    if "Windows" in platform.system() and platform.version().startswith("10[33D[K
platform.version().startswith("10"):
        # Check if the system has the necessary registry keys set
        try:
            with open(r"Software\Microsoft\Windows NT\CurrentVersion\Winlog[24D[K
NT\CurrentVersion\Winlogon", "rb") as f:
                reg_data = f.read()
                if b"EnableLUA" not in reg_data or b"PromptForPasswordOnSec[24D[K
b"PromptForPasswordOnSecureDesktop" not in reg_data:
                    return True
        except FileNotFoundError:
            pass

        # Check if the system has any known ransomware files/folders
        for root, dirs, files in os.walk(os.getcwd()):
            for file in files:
                if "ransomware" in file.lower():
                    return True
            for folder in dirs:
                if "ransomware" in folder.lower():
                    return True
        return False
    else:
        # Not running Windows or not vulnerable, return False
        return False

def mitigate_ransomware():
    # Check if the system is running a vulnerable version of Windows
    if detect_ransomware():
        # Disable the "Lock this device" feature in the registry
        try:
            subprocess.check_call(["reg", "add", r"HKLM\Software\Microsoft\[26D[K
r"HKLM\Software\Microsoft\Windows NT\CurrentVersion\Winlogon", "/v", "Disab[6D[K
"DisableLockMode", "/d", "1", "/t", "REG_DWORD", "/f"])
        except subprocess.CalledProcessError:
            pass

        # Disable the "Secure Desktop" feature in the registry
        try:
            subprocess.check_call(["reg", "add", r"HKLM\Software\Microsoft\[26D[K
r"HKLM\Software\Microsoft\Windows NT\CurrentVersion\Winlogon", "/v", "Promp[6D[K
"PromptForPasswordOnSecureDesktop", "/d", "0", "/t", "REG_DWORD", "/f"])
        except subprocess.CalledProcessError:
            pass

        # Remove any known ransomware files/folders
        for root, dirs, files in os.walk(os.getcwd()):
            for file in files:
                if "ransomware" in file.lower():
                    try:
                        os.remove(os.path.join(root, file))
                    except FileNotFoundError:
                        pass
            for folder in dirs:
                if "ransomware" in folder.lower():
                    try:
                        shutil.rmtree(os.path.join(root, folder))
                    except FileNotFoundError:
                        pass

if __name__ == "__main__":
    mitigate_ransomware()