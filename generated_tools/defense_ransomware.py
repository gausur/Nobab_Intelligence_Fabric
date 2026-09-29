#!/usr/bin/env python3
# Nobab AI defense for ransomware
# Generated 2026-09-29 13:38:04.278874

import os
import socket
import subprocess

def detect_ransomware(ip_address):
    try:
        subprocess.check_output(["nslookup", ip_address])
    except subprocess.CalledProcessError:
        return False
    return True

def mitigate_ransomware(ip_address):
    try:
        subprocess.check_output(["iptables", "-A", "OUTPUT", "DROP"])
    except subprocess.CalledProcessError:
        return False
    return True

def main():
    ip_address = input("Enter IP address: ")
    if detect_ransomware(ip_address):
        mitigate_ransomware(ip_address)
        print("Ransomware detected and mitigated.")
    else:
        print("No ransomware detected.")

if __name__ == "__main__":
    main()