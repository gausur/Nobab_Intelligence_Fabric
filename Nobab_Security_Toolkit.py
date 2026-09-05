#!/usr/bin/env python3
"""
Nobab Security Toolkit – Auto‑generated from 3 threat intelligence entries.
Build date: 2026-09-05T10:50:08.446324
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
# 1. {'keyword': 'zero day exploit', 'time': 1788603665.8468313}
# 2. {'keyword': 'ransomware', 'time': 1788603589.86651}
# 3. {'keyword': 'phishing', 'time': 1788603627.3813133}
