#!/usr/bin/env python3
# Nobab AI defense for ransomware
# Generated 2026-07-28 00:03:08.095095

import os
import time
import json
from collections import deque

class RansomwareDetector:
    def __init__(self, max_size=100):
        self.max_size = max_size
        self.deque = deque(maxlen=max_size)
        self.data = {}

    def append(self, data):
        if len(self.deque) == self.max_size:
            self.popleft()
        self.deque.append(data)
        self.data[data["timestamp"]] = data

    def popleft(self):
        oldest_key = min(self.data, key=lambda k: self.data[k]["timestamp"][25D[K
self.data[k]["timestamp"])
        del self.data[oldest_key]
        return self.deque.popleft()

    def get_stats(self):
        stats = {
            "total_files": len(self.data),
            "unique_files": len(set(self.data)),
            "new_files": len([d for d in self.data if d["is_new"]]),
            "old_files": len([d for d in self.data if not d["is_new"]])
        }
        return stats

    def save(self, filename):
        with open(filename, "w") as f:
            json.dump(self.data, f)

    def load(self, filename):
        with open(filename, "r") as f:
            self.data = json.load(f)

def main():
    detector = RansomwareDetector()
    while True:
        try:
            # Check for new files in the current directory
            for file in os.listdir("."):
                if not os.path.isfile(file):
                    continue
                # Check if the file is new or old
                if os.path.getctime(file) > time.time() - 60 * 60 * 24:
                    detector.append({"filename": file, "is_new": True})
                else:
                    detector.append({"filename": file, "is_new": False})
            # Save the statistics to a file
            detector.save("ransomware_stats.json")
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    main()