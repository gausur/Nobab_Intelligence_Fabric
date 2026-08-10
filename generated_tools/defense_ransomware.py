#!/usr/bin/env python3
# Nobab AI defense for ransomware
# Generated 2026-08-10 15:56:34.523635

import os
import sys
import json
import hashlib
import base64
from datetime import datetime, timedelta

class RansomwareDetector:
    def __init__(self):
        self.data = None
        self.hashes = []

    def read_data(self):
        try:
            with open('data.json', 'r') as f:
                self.data = json.load(f)
        except FileNotFoundError:
            pass

    def generate_hashes(self, files=[]):
        for file in files:
            with open(file, 'rb') as f:
                hash = base64.b64encode(hashlib.sha256(f.read()).digest())
                self.hashes.append((file, hash))

    def check_for_ransomware(self):
        for file, hash in self.hashes:
            if hash not in self.data['known_good']:
                print('Ransomware detected!')
                return True
        return False

    def mitigate_ransomware(self):
        if not self.check_for_ransomware():
            return
        print('Mitigating ransomware...')
        for file, hash in self.hashes:
            if hash not in self.data['known_good']:
                try:
                    os.remove(file)
                    print(f'Deleted {file}')
                except FileNotFoundError:
                    pass
        sys.exit()

def main():
    detector = RansomwareDetector()
    detector.read_data()
    files = os.listdir('.')
    detector.generate_hashes(files)
    if detector.check_for_ransomware():
        detector.mitigate_ransomware()

if __name__ == '__main__':
    main()