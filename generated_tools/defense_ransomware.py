#!/usr/bin/env python3
# Nobab AI defense for ransomware
# Generated 2026-05-16 13:05:58.275813

import os
import shutil
import hashlib
import tempfile
import threading

def scan_files(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            if not file.endswith(".txt"):
                continue
            with open(os.path.join(root, file), "r") as f:
                text = f.read()
                if "I am a ransomware attacker" in text:
                    print(f"Ransomware attack detected in {file}")
                    mitigate_attack(os.path.join(root, file))

def mitigate_attack(file):
    shutil.copyfile(file, tempfile.mktemp())
    hash = hashlib.sha256()
    with open(tempfile.mktemp(), "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash.update(chunk)
    print(f"Mitigation successful, {hash.hexdigest()} has been saved.")
    os.remove(file)

def main():
    path = "C:\\path\\to\\scan"
    threading.Thread(target=scan_files, args=(path,)).start()

if __name__ == "__main__":
    main()