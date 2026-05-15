#!/usr/bin/env python3
# Nobab AI defense for ransomware
# Generated 2026-05-15 09:46:04.554177

import socket
import re

def detect_ransomware(data):
    pattern = re.compile(r"^[a-z0-9A-Z]+$")
    if not pattern.match(data):
        return True
    else:
        return False

def mitigate_ransomware():
    socket.close()

if __name__ == "__main__":
    data = input("Enter data to detect ransomware: ")
    if detect_ransomware(data):
        print("Ransomware detected!")
        mitigate_ransomware()