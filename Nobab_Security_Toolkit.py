#!/usr/bin/env python3
"""
Nobab Security Toolkit – Auto‑generated from 3 threat intelligence entries.
Build date: 2026-05-13T20:17:56.612386
This toolkit performs basic threat detection and logging.
"""

import os, sys, time, socket, subprocess
from datetime import datetime

LOG_FILE = "nobab_toolkit.log"

def log(msg):
    ts = datetime.now().isoformat()
    with open(LOG_FILE, "a") as f:
        f.write(f"{ts} | {msg}\n")
    print(msg)

def check_suspicious_processes():
    suspicious = ["malware", "crypt", "ransom", "exploit"]
    try:
        procs = subprocess.check_output(["ps", "aux"], text=True).lower()
        for kw in suspicious:
            if kw in procs:
                log(f"Suspicious keyword '{kw}' found in running processes.")
    except:
        pass

def check_network_connections():
    try:
        result = subprocess.check_output(["ss", "-tunp"], text=True)
        est = result.count("ESTAB")
        log(f"Network: {est} established connections.")
    except:
        pass

def main():
    log("🚀 Nobab Security Toolkit started.")
    check_suspicious_processes()
    check_network_connections()
    log("✅ Scan completed.")

if __name__ == "__main__":
    main()


# Threat intelligence used:
# 1. {'keyword': 'ransomware', 'time': 1778702691.926188}
# 2. {'keyword': 'phishing', 'time': 1778702711.8421142}
# 3. {'keyword': 'zero day exploit', 'time': 1778702719.6737304}
