#!/usr/bin/env python3
# Nobab AI defense for ransomware
# Generated 2026-06-06 23:05:31.007351

import os
import socket

def is_ransomware(ip):
    try:
        s = socket.create_connection((ip, 80), timeout=5)
        s.sendall(b"GET / HTTP/1.0\n\n")
        data = s.recv(4096)
        if b"<html>" in data:
            return True
    except socket.error:
        pass
    return False

def mitigate_ransomware(ip):
    if is_ransomware(ip):
        os.system("iptables -A INPUT -s {} -j DROP".format(ip))

mitigate_ransomware("192.0.2.1")