#!/usr/bin/env python3
# Nobab AI defense for phishing
# Generated 2026-08-13 16:49:45.896037

import re
import smtplib
from email.message import EmailMessage
from typing import List, Tuple

class PhishingDetector:
    def __init__(self, emails: List[str], patterns: List[Tuple[str, str]]):[7D[K
str]]):
        self.emails = emails
        self.patterns = patterns

    def detect_phishing(self) -> bool:
        for email in self.emails:
            if not self._is_valid_email(email):
                continue
            subject = self._get_subject(email)
            body = self._get_body(email)
            for pattern, replacement in self.patterns:
                if re.search(pattern, subject) or re.search(pattern, body):[6D[K
body):
                    print("Phishing detected! Subject:", subject, "Bo[3D[K
"Body:", body)
                    return True
        return False

    def _is_valid_email(self, email: str) -> bool:
        try:
            smtplib.SMTP('localhost').sendmail('', '')
            return True
        except Exception as e:
            print("Invalid email address:", email)
            return False

    def _get_subject(self, email: str) -> str:
        with open(email, 'r') as f:
            for line in f:
                if line.startswith('Subject:'):
                    return line[9:]
        return ''

    def _get_body(self, email: str) -> str:
        with open(email, 'r') as f:
            for line in f:
                if line.startswith('From'):
                    break
            return ''.join(f.readlines())

if __name__ == '__main__':
    detector = PhishingDetector(['test@example.com'], [('phishy', 'phishing[9D[K
'phishing')])
    print(detector.detect_phishing())