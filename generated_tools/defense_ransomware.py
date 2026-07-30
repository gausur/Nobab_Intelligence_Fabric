#!/usr/bin/env python3
# Nobab AI defense for ransomware
# Generated 2026-07-30 21:03:41.731980

import socket
import os

def detect_ransomware(ip, port):
    try:
        s = socket.socket()
        s.connect((ip, port))
        s.send("Hello!".encode())
        response = s.recv(1024)
        if "RANSOMWARE" in response.decode():
            return True
    except:
        pass
    return False

def mitigate_ransomware(ip, port):
    try:
        s = socket.socket()
        s.connect((ip, port))
        s.send("CANCEL".encode())
        response = s.recv(1024)
        if "CANCELED" in response.decode():
            return True
    except:
        pass
    return False

def main():
    ip = input("Enter IP address: ")
    port = input("Enter port number: ")
    if detect_ransomware(ip, port):
        mitigate_ransomware(ip, port)
        print("Ransomware detected and mitigated!")
    else:
        print("No ransomware detected.")

if __name__ == "__main__":
    main()